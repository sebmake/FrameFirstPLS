#!/usr/bin/env python3
"""Check a framing brief written in Markdown.

Works on the full form, the short form, the executive summary and the brief map, in English or French.
Python 3.9 or later, no dependency.

    python3 check_brief.py brief.md            # check a draft
    python3 check_brief.py brief.md --freeze   # check before the freeze
    python3 check_brief.py brief.md --json     # machine-readable output
    python3 check_brief.py summary.md --brief brief.md  # a summary against its brief

Exit code: 0 when nothing must be fixed, 1 when at least one ERROR is found,
2 when the file cannot be read or is not recognised as a brief.

Levels
    ERROR  must be fixed (malformed, or not allowed at the freeze)
    WARN   a judgement call: a cap is passed, a sentence is long, a line is vague
    INFO   a count, for the hand-over message
"""

import argparse
import json
import os
import re
import sys

CAPS = {
    "rules_full": 5,
    "rules_short": 4,
    "decisions": 4,
    "scenarios": 4,
    "principles": 4,
    "open_questions": 5,
    "options": 4,
    "sentence_words": 25,
    # The brief has no page limit; its executive summary fits on one A4 page:
    # about 380 words in Arial 11 pt with 2 cm margins, with the before / after diagram.
    "words_summary": 380,
    # A brief map holds its diagram, one row per brief and what each must settle on one A4 page.
    "words_map": 330,
}

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "sept": 7,
    "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12,
}

RE_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RE_FENCE = re.compile(r"^\s*(```|~~~)")
RE_CHECK_ITEM = re.compile(r"^\s*(?:>\s*)*[-*+]\s+\[([ xX])\]\s+(.*)$")
RE_BOX = re.compile(r"\[[ xX]\]")
RE_OTHER = re.compile(r"^\**\s*(other|autre)\b", re.I)
RE_QUESTION = re.compile(
    r"^\s*(?P<mark>⚠️?|✔️?|✅)?\s*\*\*(?P<kind>[TG])(?P<num>\d+)\s*[·.:]\s*(?P<title>.+?)\*\*"
)
RE_RULE = re.compile(r"^\s*\*\*R(\d+)\b")
RE_SCENARIO = re.compile(r"^\s*\*\*(scenario|scénario)\s+\d+", re.I)
RE_SCREEN = re.compile(r"^\s*\*\*F(\d+)\s*[—–-]")
RE_PROPOSED = re.compile(r"\[(proposed|proposé|propose|proposée)\]", re.I)
RE_TO_PROVIDE = re.compile(r"\[(to provide|à fournir|a fournir)\]", re.I)
RE_LEGEND = re.compile(r"(marked|marquées?|marqués?)\s+`?\[propos", re.I)
RE_PLACEHOLDER = re.compile(
    r"<(verb|object|verbe|objet|frame name|nom du cadre|the target date|la date visée|subject|lang|what we count|the threshold|the 30-day threshold|what must not get worse|ce qu'on compte|le seuil|ce qui ne doit pas se dégrader)>",
    re.I,
)
RE_LONE_ELLIPSIS = re.compile(r"(?<![\w…])…|(?<![\w.])\.\.\.(?!\.)")
RE_GLUED = re.compile(r"[^\s*]\*\s\*\*[^\s*]")
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_ID_MENTION = re.compile(r"\b([RT])(\d+)\b")
RE_HELD_OPEN = re.compile(r"(open at the freeze|ouverte au gel)", re.I)
RE_BLOCKS = re.compile(r"(blocks the freeze|bloque le gel)", re.I)
RE_CLOSED = re.compile(r"\b(closed|close|closes|fermée?|clôturée?)\b", re.I)
RE_WORD = re.compile(r"[^\W_]+(?:['’-][^\W_]+)*", re.UNICODE)

FULL_SECTIONS = [
    ("context", r"\b(context|contexte)\b"),
    ("scope", r"\b(scope|périmètre|perimetre)\b"),
    ("rules", r"\b(rules|règles|regles)\b"),
    ("freeze", r"\b(the freeze|le gel|freeze|gel)\b"),
]
SHORT_SECTIONS = [
    ("principle", r"\b(principle|principe)\b"),
    ("diagram", r"\b(diagram|schéma|schema)\b"),
    ("rules", r"\b(rules|règles|regles)\b"),
    ("watch-outs", r"(watch-?outs?|vigilance)"),
    ("what exists", r"(what exists|existant)"),
    ("success criterion", r"(success criteri|critère de réussite|critere de reussite)"),
    ("bet", r"\b(bet|pari)\b"),
]


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, code, line, message):
        self.items.append({"level": level, "code": code, "line": line, "message": message})

    def count(self, level):
        return sum(1 for i in self.items if i["level"] == level)


def load(path):
    with open(path, "r", encoding="utf-8") as handle:
        raw = handle.read().splitlines()
    lines = []
    in_fence = False
    for text in raw:
        if RE_FENCE.match(text):
            in_fence = not in_fence
            lines.append("")
            continue
        lines.append("" if in_fence else text)
    return lines


def no_code(text):
    return RE_INLINE_CODE.sub("", text)


def headings(lines):
    found = []
    for index, text in enumerate(lines):
        match = RE_HEADING.match(text)
        if match:
            found.append((index, len(match.group(1)), match.group(2).strip()))
    return found


def section_of(lines):
    """For each line, the lower-cased text of the last heading above it."""
    current = ""
    result = []
    for text in lines:
        match = RE_HEADING.match(text)
        if match:
            current = match.group(2).strip().lower()
        result.append(current)
    return result


def notes_start(lines):
    pattern = re.compile(r"^(#{1,6}\s*|\*\*)\s*notes (and|et) sources", re.I)
    for index, text in enumerate(lines):
        if pattern.match(text.strip()):
            return index
    return len(lines)


def detect_form(lines, forced):
    if forced:
        return forced
    numbering = r"^(\d+\s*[·.:)-]\s*)?"
    heads = [text.lower() for _, _, text in headings(lines)]
    if heads and re.search(r"(executive summary|résumé exécutif|resume executif)", heads[0]):
        return "summary"
    if heads and re.search(r"^(brief map|carte des briefs)\b", heads[0]):
        return "map"
    if any(re.match(numbering + r"(the bet|le pari)\b", head) for head in heads):
        return "short"
    if any(re.match(numbering + r"(the freeze|le gel)\b", head) for head in heads):
        return "full"
    return None


def is_other(option_text):
    return bool(RE_OTHER.match(option_text.strip()))


def strip_marks(text):
    text = no_code(text)
    text = re.sub(r"^\s*(?:>\s*)*([-*+]\s+)?(\[[ xX]\]\s+)?", "", text)
    return text.replace("**", "").replace("__", "").strip()


def check_sections(lines, form, report):
    heads = [text.lower() for _, _, text in headings(lines)]
    wanted = FULL_SECTIONS if form == "full" else SHORT_SECTIONS
    for name, pattern in wanted:
        if not any(re.search(pattern, head) for head in heads):
            report.add("ERROR", "S1", None, "section missing: %s" % name)


def check_marks(lines, freeze, report):
    for index, text in enumerate(lines):
        if RE_HEADING.match(text) and RE_PROPOSED.search(text):
            report.add("WARN", "P4", index + 1, "[proposed] on a heading covers every line under it: mark line by line if any of them is decided")
    proposed = [i for i, t in enumerate(lines) if RE_PROPOSED.search(t) and not RE_LEGEND.search(t)]
    to_provide = [i for i, t in enumerate(lines) if RE_TO_PROVIDE.search(t)]
    if proposed:
        if freeze:
            for index in proposed[:12]:
                report.add("ERROR", "P1", index + 1, "still marked [proposed]: confirm it aloud or turn it into a question")
            if len(proposed) > 12:
                report.add("ERROR", "P1", None, "%d more lines still marked [proposed]" % (len(proposed) - 12))
        else:
            report.add("INFO", "P1", None, "%d line(s) still marked [proposed]" % len(proposed))
    if to_provide:
        level = "ERROR" if freeze else "INFO"
        report.add(level, "P2", to_provide[0] + 1, "%d value(s) still [to provide]" % len(to_provide))


def check_leftovers(lines, freeze, limit, report):
    level = "ERROR" if freeze else "WARN"
    hits = []
    for index, text in enumerate(lines[:limit]):
        if not text.strip():
            continue
        bare = no_code(text)
        if RE_PLACEHOLDER.search(bare):
            hits.append(index)
            continue
        match = RE_CHECK_ITEM.match(text)
        if match and is_other(match.group(2)):
            continue
        if RE_LONE_ELLIPSIS.search(bare):
            hits.append(index)
    for index in hits[:8]:
        report.add(level, "P3", index + 1, "template text left unfilled")
    if len(hits) > 8:
        report.add(level, "P3", None, "%d more unfilled template lines" % (len(hits) - 8))


def check_boxes(lines, report):
    for index, text in enumerate(lines):
        bare = no_code(text)
        if RE_BOX.search(bare) and not RE_CHECK_ITEM.match(bare):
            report.add("ERROR", "K1", index + 1, "a box here cannot be ticked: boxes must start a list line (- [ ] ...), never sit in a table or a paragraph")
        if RE_GLUED.search(bare):
            report.add("WARN", "K2", index + 1, "italic glued to bold: put a dash or a line break between them")


def collect_questions(lines):
    """Return the T and G questions with their options."""
    questions = []
    total = len(lines)
    for index, text in enumerate(lines):
        match = RE_QUESTION.match(text)
        if not match:
            continue
        context = []
        options = []
        cursor = index + 1
        while cursor < total:
            line = lines[cursor]
            if not line.strip():
                if options:
                    # a blank line ends the list unless more boxes follow
                    ahead = cursor + 1
                    while ahead < total and not lines[ahead].strip():
                        ahead += 1
                    if ahead < total and RE_CHECK_ITEM.match(lines[ahead]):
                        cursor = ahead
                        continue
                    break
                cursor += 1
                continue
            item = RE_CHECK_ITEM.match(line)
            if item:
                options.append({"line": cursor + 1, "ticked": item.group(1) != " ", "text": item.group(2)})
                cursor += 1
                continue
            if options:
                break
            if RE_HEADING.match(line) or RE_QUESTION.match(line) or RE_RULE.match(line) or line.strip() == "---":
                break
            context.append(cursor + 1)
            cursor += 1
        # an italic line right under the options may name the hole: owner and date
        after = cursor
        while after < total and not lines[after].strip():
            after += 1
        held_open = after < total and bool(RE_HELD_OPEN.search(lines[after]))
        questions.append({
            "id": match.group("kind") + match.group("num"),
            "kind": match.group("kind"),
            "mark": match.group("mark") or "",
            "title": match.group("title").strip(),
            "line": index + 1,
            "context": context,
            "options": options,
            "held_open": held_open,
            "blocks": bool(RE_BLOCKS.search(text)),
        })
    return questions


def check_questions(lines, freeze, report):
    questions = collect_questions(lines)
    seen = {}
    for question in questions:
        qid, line = question["id"], question["line"]
        if qid in seen:
            report.add("ERROR", "Q4", line, "%s is defined twice (first at line %d): identifiers never repeat" % (qid, seen[qid]))
        seen[qid] = line
        options = question["options"]
        real = [o for o in options if not is_other(o["text"])]
        if len(real) < 2:
            report.add("ERROR", "Q1", line, "%s needs at least two options to tick, as list lines" % qid)
        elif len(real) > CAPS["options"]:
            report.add("WARN", "Q1", line, "%s has %d options: four at most, or it is two questions" % (qid, len(real)))
        if question["kind"] == "G" and not RE_COST.search(lines[line - 1]):
            report.add("ERROR", "S5", line, "%s does not say what missing the date costs: the decider's words, or [to provide]" % qid)
        if options and not is_other(options[-1]["text"]):
            report.add("ERROR", "Q2", options[-1]["line"], "%s: the last option must be Other" % qid)
        title = question["title"].rstrip()
        if not title.endswith("?"):
            report.add("WARN", "Q3", line, "%s is not written as a question" % qid)
        if question["context"]:
            report.add("WARN", "Q5", question["context"][0], "%s: no context sentence between the question and its options" % qid)
        ticked = [o for o in options if o["ticked"]]
        if freeze:
            if not ticked and question["blocks"]:
                report.add("ERROR", "F6", line, "%s holds a disagreement on the why or the scope and has no answer: the subject goes back to a session" % qid)
            elif not ticked and question["held_open"]:
                report.add("WARN", "F5", line, "%s stays open through the freeze, with an owner and a date: fine only if it touches neither the why nor the scope" % qid)
            elif not ticked:
                report.add("ERROR", "F1", line, "%s has no answer ticked, and no owner with a date under it" % qid)
            elif question["mark"].startswith("⚠"):
                report.add("WARN", "F2", line, "%s is answered but still flagged ⚠️: turn it into ✔" % qid)
        if len(ticked) > 1:
            report.add("WARN", "F3", line, "%s has %d answers ticked: one answer per question" % (qid, len(ticked)))
    decisions = [q for q in questions if q["kind"] == "T"]
    if len(decisions) > CAPS["decisions"]:
        report.add("WARN", "C2", decisions[CAPS["decisions"]]["line"],
                   "%d decisions to make, cap is %d: the subject is not ripe, propose a split" % (len(decisions), CAPS["decisions"]))
    return questions


def check_rules(lines, form, report):
    found = {}
    for index, text in enumerate(lines):
        match = RE_RULE.match(text)
        if not match:
            continue
        rid = "R" + match.group(1)
        if rid in found:
            report.add("ERROR", "Q4", index + 1, "%s is defined twice (first at line %d)" % (rid, found[rid]))
        else:
            found[rid] = index + 1
    cap = CAPS["rules_full"] if form == "full" else CAPS["rules_short"]
    if len(found) > cap:
        report.add("WARN", "C1", None, "%d rules, cap is %d for the %s form: propose a split, or the other form" % (len(found), cap, form))
    return found


def check_references(lines, rules, questions, limit, report):
    defined = set(rules) | {q["id"] for q in questions}
    for index, text in enumerate(lines[:limit]):
        if text.lstrip().startswith("*") and RE_CLOSED.search(text):
            for kind, num in RE_ID_MENTION.findall(no_code(text)):
                defined.add(kind + num)
    reported = set()
    for index, text in enumerate(lines[:limit]):
        for kind, num in RE_ID_MENTION.findall(no_code(text)):
            ref = kind + num
            if ref not in defined and ref not in reported:
                reported.add(ref)
                report.add("WARN", "Q6", index + 1, "%s is mentioned but not defined in this brief" % ref)


def check_counts(lines, sections, report):
    scenarios = [i for i, t in enumerate(lines) if RE_SCENARIO.match(t)]
    if len(scenarios) > CAPS["scenarios"]:
        report.add("WARN", "C3", scenarios[CAPS["scenarios"]] + 1,
                   "%d scenarios, cap is %d: keep the ones that say when it is right" % (len(scenarios), CAPS["scenarios"]))
    total = len(lines)
    for index, text in enumerate(lines):
        if not RE_SCREEN.match(text):
            continue
        principles = 0
        cursor = index + 1
        while cursor < total:
            line = lines[cursor]
            item = RE_CHECK_ITEM.match(line)
            if item:
                if not is_other(item.group(2)):
                    principles += 1
            elif line.strip():
                break
            cursor += 1
        if principles > CAPS["principles"]:
            report.add("WARN", "C4", index + 1, "%d principles on this screen, cap is %d: principles, not an inventory" % (principles, CAPS["principles"]))
    open_ids = set()
    table_line = None
    for index, text in enumerate(lines):
        if re.search(r"(open questions|questions ouvertes)", sections[index]):
            for num in re.findall(r"\bO(\d+)\b", no_code(text)):
                open_ids.add(num)
            if text.strip().startswith("|") and table_line is None:
                table_line = index + 1
    if table_line is not None:
        report.add("WARN", "C5", table_line, "open questions in a table: one pointer line per question, the wording lives in its thread")
    if len(open_ids) > CAPS["open_questions"]:
        report.add("WARN", "C5", None, "%d open questions, cap is %d" % (len(open_ids), CAPS["open_questions"]))
    for index, text in enumerate(lines):
        if not re.search(r"(open questions|questions ouvertes)", sections[index]):
            continue
        if re.match(r"^\s*[-*+]\s+\*\*O\d+\*\*", text) and not RE_WHEN.search(no_code(text)):
            report.add("WARN", "W4", index + 1, "this open question says nothing about when the answer is needed: a date, or \"before the next session\"")


def bullets_after(lines, start):
    """Bullet lines that follow an intro line, until the next block."""
    found = []
    cursor = start + 1
    total = len(lines)
    while cursor < total:
        line = lines[cursor]
        stripped = line.strip()
        if not stripped:
            cursor += 1
            continue
        if re.match(r"^[-*+]\s+(?!\[)", stripped):
            found.append((cursor, stripped))
            cursor += 1
            continue
        break
    return found


def check_scope(lines, report):
    contains = re.compile(r"^\*\*(what this version contains|ce que (cette version|le mvp) contient)\*\*(.*)$", re.I)
    out = re.compile(r"^\*\*(what will not be in it|ce qui n['’]y entrera pas)\*\*", re.I)
    for index, text in enumerate(lines):
        stripped = text.strip()
        match = contains.match(stripped)
        if match:
            items = bullets_after(lines, index)
            announced = None
            number = re.search(r"\b(\d+)\b", match.group(3))
            if number:
                announced = int(number.group(1))
            else:
                for word in RE_WORD.findall(match.group(3).lower()):
                    if word in NUMBER_WORDS:
                        announced = NUMBER_WORDS[word]
                        break
            if announced is not None and items and announced != len(items):
                report.add("WARN", "W3", index + 1, "the sentence announces %d items, the list has %d: recount" % (announced, len(items)))
        if out.match(stripped):
            for line_index, bullet in bullets_after(lines, index):
                if RE_TO_PROVIDE.search(bullet):
                    continue
                body = no_code(bullet)
                has_arrow = "→" in body or "->" in body
                not_exist = re.search(r"(does not exist|doesn['’]t exist|n['’]existe pas)", body, re.I)
                if not has_arrow and not not_exist:
                    report.add("WARN", "W1", line_index + 1, "this line does not say where the thing lives instead (→ a brief, an owner, a date)")
                elif has_arrow:
                    destination = re.split(r"→|->", body)[-1].strip(" .").lower()
                    if destination in ("later", "plus tard", "tbd", "à voir", "a voir", "?", ""):
                        report.add("WARN", "W2", line_index + 1, "\"%s\" is not a destination" % (destination or "nothing"))


def template_lines():
    """Lines copied word for word from a template: the template's own text, not the room's."""
    here = os.path.dirname(os.path.abspath(__file__))
    found = set()
    for name in ("template-full.en.md", "template-full.fr.md", "template-short.en.md", "template-short.fr.md"):
        path = os.path.join(here, "..", "assets", name)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as handle:
            for text in handle.read().splitlines():
                text = " ".join(text.split())
                if text and "…" not in text:
                    found.add(text)
    return found


def body_range(lines, form):
    """The body is what the room reads and decides: from the context to the deadline (full form),
    from the principle to the bet sentence (short form). Header, freeze round, signatures and notes are out."""
    end = notes_start(lines)
    start = None
    for index, text in enumerate(lines[:end]):
        match = RE_HEADING.match(text)
        if not match:
            continue
        title = match.group(2).strip().lower()
        if start is None and re.search(r"\b(context|contexte|principle|principe)\b", title):
            start = index
        elif start is not None and form == "full" and re.search(r"\b(the freeze|le gel)\b", title):
            end = index
            break
    if start is None:
        start = 0
    if form == "short":
        for index in range(start, end):
            if re.match(r"^\|\s*(who|qui)\s*\|", lines[index].strip(), re.I):
                end = index
                break
    return start, end


def check_prose(lines, form, limit, report):
    long_lines = []
    words_total = 0
    words_body = 0
    fixed = template_lines()
    start, end = body_range(lines, form)
    for index, text in enumerate(lines):
        stripped = text.strip()
        if not stripped:
            continue
        found = len(RE_WORD.findall(no_code(stripped)))
        words_total += found
        if start <= index < end and " ".join(stripped.split()) not in fixed and not re.match(r"^\|\s*[-:]+\s*\|", stripped):
            words_body += found
        if index >= limit or stripped.startswith("|") or stripped.startswith("#"):
            continue
        clean = strip_marks(stripped).replace("*", "")
        for sentence in re.split(r"(?<=[.!?…])\s+|\s·\s", clean):
            count = len(RE_WORD.findall(sentence))
            if count > CAPS["sentence_words"]:
                long_lines.append((index + 1, count))
                break
    for line, count in long_lines[:5]:
        report.add("WARN", "L1", line, "a sentence of %d words: aim for fifteen" % count)
    if len(long_lines) > 5:
        report.add("WARN", "L1", None, "%d more long sentences" % (len(long_lines) - 5))
    return words_body, words_total


def check_freeze_block(lines, sections, freeze, report):
    unsigned = []
    items = []
    for index, text in enumerate(lines):
        if not re.search(r"\b(the freeze|le gel)\b", sections[index]):
            continue
        item = RE_CHECK_ITEM.match(text)
        if item:
            items.append((index, item.group(2)))
            if item.group(1) == " ":
                unsigned.append(strip_marks(text).split("—")[0].strip())
    count = len(items)
    deciders = [i for i, (_, label) in enumerate(items) if RE_DECIDER.search(label.split("—")[0])]
    if deciders and deciders[-1] != count - 1:
        report.add("ERROR", "S4", items[deciders[-1]][0] + 1, "the decider's line must come last in the freeze round, so that nobody aligns on them")
    if count == 0:
        report.add("ERROR", "S2", None, "the freeze block has no line to tick")
    elif freeze and unsigned:
        report.add("ERROR", "F4", None, "freeze lines not ticked by their owner yet: %s" % ", ".join(unsigned))


def check_short(lines, sections, freeze, report):
    text_all = "\n".join(lines)
    bet = re.search(r"(we bet that|on parie que)\**(.*)", text_all, re.I)
    if not bet:
        report.add("ERROR", "B1", None, "the bet sentence is missing (\"We bet that if ..., then ...\")")
    elif not re.search(r"\d|to provide|à fournir|<", bet.group(2)):
        report.add("WARN", "B5", None, "the bet names no number to reach: a bet no result can contradict is not a bet")
    criterion = "\n".join(t for i, t in enumerate(lines) if re.search(r"(success criteri|critère de réussite|critere de reussite)", sections[i]))
    has_pass = re.search(r"(passed if|réussi si|reussi si)", criterion, re.I)
    has_fail = re.search(r"(failed if|échec si|echec si)", criterion, re.I)
    if not (has_pass and has_fail):
        report.add("ERROR", "B2", None, "the success criterion needs a pass line and a fail line")
    for index, text in enumerate(lines):
        if not re.search(r"(watch-?outs?|vigilance)", sections[index]):
            continue
        if text.strip().startswith("|") and "⚠" in text:
            if not re.search(r"(no written answer|sans réponse écrite|sans reponse ecrite)", text, re.I):
                report.add("WARN", "B3", index + 1, "the question for the decider has no default answer if nobody replies")
            if not re.search(r"\*\*Q\d+\s*[·.:]", text):
                report.add("WARN", "B6", index + 1, "a question for the decider without its identifier: Q1, Q2, so the summary and the checker can follow it")
    if any(RE_SCENARIO.match(t) for t in lines):
        report.add("WARN", "B4", None, "acceptance scenarios in a short brief: they belong to the implementation tickets")
    if freeze:
        waiting = [strip_marks(t).split("|")[1].strip() for i, t in enumerate(lines)
                   if re.search(r"\b(bet|pari)\b", sections[i]) and t.strip().startswith("|") and "⬜" in t]
        if waiting:
            report.add("INFO", "F4", None, "bet not signed yet: %s" % ", ".join(w.replace("⬜", "").strip() for w in waiting))


RE_UNSET = re.compile(r"(to set in the session|to be set|\bTBD\b|à fixer|à définir)", re.I)
RE_TODAY = re.compile(r"\*\*(today|aujourd['’]hui)\*\*", re.I)
RE_COST = re.compile(r"(missing it costs|(la|le) manquer co[uû]te)", re.I)
RE_DECIDER = re.compile(r"\b(decider|décideur|décideuse|decideur)\b", re.I)
RE_WHEN = re.compile(r"\b(by|before|until|pour|avant|d['’]ici)\b|\d", re.I)


def check_decider_short(lines, report):
    """Short form: the header names who decides."""
    header = []
    for text in lines:
        if text.startswith("## "):
            break
        header.append(text)
    if not re.search(r"\*\*(decides|décide|decide)\*\*", "\n".join(header), re.I):
        report.add("WARN", "S6", None, "the header names nobody who decides: add a Decides row, with a name or [to provide]")


def check_today_short(lines, sections, report):
    """Short form: the principle says what people do today instead."""
    body = "\n".join(t for i, t in enumerate(lines) if re.search(r"\b(principle|principe)\b", sections[i]))
    if not RE_TODAY.search(body):
        report.add("ERROR", "S3", None, "the principle has no Today row: what people do instead, and what it costs")


def check_context(lines, sections, report):
    """Full form: the context carries a Today line, a proof line and a measure line."""
    body = "\n".join(t for i, t in enumerate(lines) if re.search(r"\b(context|contexte)\b", sections[i]))
    if not RE_TODAY.search(body):
        report.add("ERROR", "S3", None, "the context has no Today line: what people do instead, and why it is not enough")
    if not re.search(r"\*\*(proof|preuve)\*\*", body, re.I):
        report.add("ERROR", "S3", None, "the context has no Proof line: a fact seen or heard and a number, or written as missing")
    if not re.search(r"\*\*(we will know it worked|on saura que ça a marché)\*\*", body, re.I):
        report.add("ERROR", "S3", None, "the context has no \"We will know it worked\" line: what we count, today and in thirty days")


def check_unset(lines, limit, freeze, report):
    """A value left to set later cannot pass the freeze."""
    if not freeze:
        return
    for index, text in enumerate(lines[:limit]):
        if RE_UNSET.search(no_code(text)):
            report.add("ERROR", "F7", index + 1, "a value left to set later: write it before the freeze, or mark it [to provide]")


def check_reduced(lines, questions, freeze, report):
    """G1 ticked "reduced": the lines that leave must already be in "waits"."""
    if not freeze:
        return
    reduced = [q for q in questions if q["kind"] == "G" and any(o["ticked"] and re.search(r"(reduced|réduit)", o["text"], re.I) for o in q["options"])]
    if not reduced:
        return
    waits = re.compile(r"^\*\*(what waits for a later version|ce qui attend une version ultérieure)\*\*", re.I)
    count = 0
    for index, text in enumerate(lines):
        if waits.match(text.strip()):
            count = len(bullets_after(lines, index))
    if count == 0:
        report.add("ERROR", "F8", reduced[0]["line"], "G1 is \"reduced\" but nothing is in \"waits\": write the lines that leave before the freeze")
    else:
        report.add("WARN", "F8", reduced[0]["line"], "G1 is \"reduced\": check that every line that leaves is in \"waits\"")


def question_titles(lines):
    """{id: normalised title} for every T, G and R line."""
    found = {}
    for text in lines:
        match = RE_QUESTION.match(text)
        if match:
            title = match.group("title")
            found[match.group("kind") + match.group("num")] = re.sub(r"[^\w]+", " ", title.lower()).strip()
            continue
        match = re.search(r"\*\*Q(\d+)\s*[·.:]\s*(.+?)\*\*", text)
        if match:
            found["Q" + match.group(1)] = re.sub(r"[^\w]+", " ", match.group(2).lower()).strip()
            continue
        match = re.match(r"^\s*(?:[-*]\s+)?\*\*R(\d+)\b\s*[·.:]?\s*(.*?)\*\*", text)
        if match:
            found["R" + match.group(1)] = re.sub(r"[^\w]+", " ", match.group(2).lower()).strip()
    return found


def check_summary(lines, full_path, report):
    """The executive summary: one A4 page, a message, five one-line bullets, the decisions, the next step."""
    end = len(lines)
    message = None
    for index, text in enumerate(lines):
        if re.match(r"^\s*\*\*(the message|le message)\b", text.strip(), re.I):
            message = index
            break
    if message is None:
        report.add("ERROR", "E1", None, "no message paragraph: start with **The message.** — who can now do what, why now, what the session settles")
        start = 0
    else:
        start = message + 1
    bullets = []
    for index in range(start, end):
        text = lines[index].strip()
        if RE_HEADING.match(text):
            break
        if re.match(r"^[-*]\s+\*\*", text):
            bullets.append(index)
    if len(bullets) > 5:
        report.add("WARN", "E2", bullets[5] + 1, "%d bullets under the message: five at most, one line each" % len(bullets))
    if bullets and not re.search(r"\*\*(settled|acquis|nothing is settled|rien n'est acquis)", lines[bullets[0]], re.I):
        report.add("WARN", "E3", bullets[0] + 1, "the first bullet says what is settled, or that nothing is")
    for index in bullets:
        count = len(RE_WORD.findall(no_code(lines[index])))
        if count > 35:
            report.add("WARN", "E4", index + 1, "a bullet of %d words: one line each" % count)
    for index, text in enumerate(lines):
        if RE_BOX.search(text) and RE_CHECK_ITEM.match(text):
            report.add("WARN", "E5", index + 1, "a box to tick: the summary is read, the boxes live in the brief")
            break
    for index, text in enumerate(lines):
        match = RE_QUESTION.match(re.sub(r"^\s*[-*]\s+", "", text))
        if match and match.group("kind") == "T":
            if not match.group("title").rstrip().endswith("?"):
                report.add("WARN", "E6", index + 1, "T%s is not written as a question" % match.group("num"))
            if not re.search(r"\b(other|autre)\b", text, re.I):
                report.add("WARN", "E6", index + 1, "T%s gives no Other among its options" % match.group("num"))
    header = "\n".join(lines[:message] if message is not None else lines[:4])
    pointer = re.search(r"\b(?:full brief|brief complet|brief)\s*:\s*([^·\n]*)", header, re.I)
    not_yet = pointer and re.search(r"(not yet|none|to write|to prepare|pas encore|aucun|à écrire|à préparer)", pointer.group(1), re.I)
    if pointer and not not_yet:
        pass
    elif re.search(r"⚠.*(no brief|pas encore de brief)", "\n".join(lines), re.I):
        report.add("INFO", "E12", None, "no brief behind this summary yet: write the brief before the freeze")
    else:
        report.add("WARN", "E12", None, "say at the top whether a brief stands behind this summary: its file, or ⚠️ No brief behind this summary yet")
    if full_path:
        full = question_titles(load(full_path))
        mine = question_titles([re.sub(r"^\s*[-*]\s+", "", t) for t in lines])
        for qid, title in sorted(mine.items()):
            if qid not in full:
                report.add("ERROR", "E7", None, "%s is not in the brief: the summary adds nothing of its own" % qid)
            elif title and full[qid] and title != full[qid]:
                report.add("WARN", "E7", None, "%s is worded differently in the brief: keep the same title" % qid)
        for qid in sorted(full):
            if qid[0] in "TGQ" and qid not in mine:
                report.add("WARN", "E8", None, "%s is in the brief but not in the summary's decisions" % qid)


def check_summary_diagram(path, report):
    """One before / after diagram, left to right, two rows of three steps at most, short boxes."""
    with open(path, "r", encoding="utf-8") as handle:
        raw = handle.read()
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", raw, re.S)
    if not blocks:
        report.add("WARN", "E9", None, "no before / after diagram under the message: copy it from the template")
        return
    if len(blocks) > 1:
        report.add("WARN", "E9", None, "%d diagrams: the summary carries one" % len(blocks))
    block = blocks[0]
    direction = re.search(r"^\s*(?:flowchart|graph)\s+(\w+)", block, re.M)
    if direction and direction.group(1).upper() not in ("LR", "RL"):
        report.add("WARN", "E10", None, "the diagram runs top to bottom: on A4 it fills half the page; draw it left to right")
    rows = [line for line in block.splitlines() if re.search(r"-\.->|==>|-->", line)]
    if len(rows) > 2:
        report.add("WARN", "E10", None, "%d rows in the diagram: two, TODAY and AFTER" % len(rows))
    for row in rows:
        labels = re.findall(r'"([^"]+)"', row)
        if len(labels) > 5:
            report.add("WARN", "E10", None, "a row of %d steps: three at most, or the text shrinks below what paper can read" % (len(labels) - 2))
        for label in labels:
            if len(RE_WORD.findall(label)) > 5:
                report.add("WARN", "E10", None, "the box \"%s\" is long: three or four words" % label)
    if not (re.search(r"classDef\s+today\b", block) and re.search(r"classDef\s+after\b", block)):
        report.add("WARN", "E11", None, "the template's styles are missing: without them the two rows look alike")


def check_map(path, lines, report):
    """The brief map: the vision first, one row per brief with an outcome, a form and a freeze order,
    what each must settle, a left-to-right diagram, no rule and no box."""
    rows = []
    for index, text in enumerate(lines):
        match = re.match(r"^\|\s*\*\*(\d+)\s*[·.:]\s*(.+?)\*\*\s*\|(.*)$", text.strip())
        if match:
            cells = [c.strip() for c in match.group(3).strip().strip("|").split("|")]
            rows.append((index, match.group(1), match.group(2), cells))
    if not rows:
        report.add("ERROR", "M1", None, "no brief rows: one row per brief, starting with **0 · Vision**")
        return
    if rows[0][1] != "0" or not re.search(r"\bvision\b", rows[0][2], re.I):
        report.add("WARN", "M1", rows[0][0] + 1, "the first row is not brief 0, the vision")
    if len(rows) > 7:
        report.add("WARN", "M2", rows[7][0] + 1, "%d briefs: past seven it is a programme; map the first release, or group them" % len(rows))
    for index, num, name, cells in rows:
        outcome = cells[0] if cells else ""
        form = cells[1].lower() if len(cells) > 1 else ""
        order = cells[2] if len(cells) > 2 else ""
        if not outcome or outcome in ("…", "..."):
            report.add("WARN", "M3", index + 1, "brief %s has no outcome sentence: what changes for the person" % num)
        if not re.search(r"\b(short|full|courte|complète|complete)\b", form):
            report.add("WARN", "M3", index + 1, "brief %s has no form: short or full" % num)
        if not order or order in ("…", "..."):
            report.add("WARN", "M3", index + 1, "brief %s says nothing of when it freezes" % num)
    settle = {}
    for text in lines:
        match = re.match(r"^\s*[-*]\s+\*\*(\d+)\s*[·.:]", text)
        if match:
            settle[match.group(1)] = text
    for index, num, name, cells in rows:
        if num not in settle:
            report.add("WARN", "M4", index + 1, "brief %s has no line saying what it must settle" % num)
        elif settle[num].count("?") > 2:
            report.add("WARN", "M4", index + 1, "brief %s carries more than two questions: keep the two that block it" % num)
    with open(path, "r", encoding="utf-8") as handle:
        raw = handle.read()
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", raw, re.S)
    if not blocks:
        report.add("WARN", "M5", None, "no diagram of the freeze order: copy it from the template")
    else:
        direction = re.search(r"^\s*(?:flowchart|graph)\s+(\w+)", blocks[0], re.M)
        if direction and direction.group(1).upper() not in ("LR", "RL"):
            report.add("WARN", "M5", None, "the diagram runs top to bottom: draw it left to right")
    for index, text in enumerate(lines):
        if RE_RULE.match(text):
            report.add("WARN", "M6", index + 1, "a rule on the map: rules belong to the brief itself")
            break
    for index, text in enumerate(lines):
        if RE_CHECK_ITEM.match(text):
            report.add("WARN", "M6", index + 1, "a box to tick on the map: the boxes belong to the briefs")
            break


def run(path, freeze, forced_form, full_path=None):
    lines = load(path)
    form = detect_form(lines, forced_form)
    report = Report()
    if form is None:
        report.add("ERROR", "S0", None, "not recognised as a framing brief: no \"The freeze\" (full form) or \"The bet\" (short form) heading")
        return None, report, 0
    if form == "map":
        check_map(path, lines, report)
        check_leftovers(lines, False, len(lines), report)
        words = sum(len(RE_WORD.findall(no_code(t.strip()))) for t in lines if t.strip())
        if words > CAPS["words_map"]:
            report.add("WARN", "L2", None, "%d words: about %d fit on one A4 page with the diagram; shorten the rows, or map the first release only" % (words, CAPS["words_map"]))
        return form, report, (words, words)
    if form == "summary":
        check_summary(lines, full_path, report)
        check_summary_diagram(path, report)
        check_leftovers(lines, False, len(lines), report)
        words = sum(len(RE_WORD.findall(no_code(t.strip()))) for t in lines if t.strip())
        if words > CAPS["words_summary"]:
            report.add("WARN", "L2", None, "%d words: about %d fit on one A4 page; shorten the writing, or the subject is too big" % (words, CAPS["words_summary"]))
        return form, report, (words, words)
    sections = section_of(lines)
    limit = notes_start(lines)
    check_sections(lines, form, report)
    check_marks(lines, freeze, report)
    check_leftovers(lines, freeze, limit, report)
    check_boxes(lines, report)
    rules = check_rules(lines, form, report)
    questions = []
    if form == "full":
        questions = check_questions(lines, freeze, report)
        check_counts(lines, sections, report)
        check_scope(lines, report)
        check_freeze_block(lines, sections, freeze, report)
        check_context(lines, sections, report)
        check_reduced(lines, questions, freeze, report)
    else:
        check_short(lines, sections, freeze, report)
        check_today_short(lines, sections, report)
        check_decider_short(lines, report)
    check_unset(lines, limit, freeze, report)
    check_references(lines, rules, questions, limit, report)
    words = check_prose(lines, form, limit, report)
    return form, report, words


def describe(words, form=None):
    body, total = words if isinstance(words, tuple) else (words, words)
    if form == "summary":
        return "%d words (one A4 page holds about %d)" % (total, CAPS["words_summary"])
    if form == "map":
        return "%d words (one A4 page holds about %d)" % (total, CAPS["words_map"])
    return "%d words in the body, %d in the whole file" % (body, total)


def main():
    parser = argparse.ArgumentParser(description="Check a framing brief written in Markdown.")
    parser.add_argument("path", help="the brief, a Markdown file")
    parser.add_argument("--freeze", action="store_true", help="check what the freeze requires")
    parser.add_argument("--form", choices=["full", "short", "summary", "map"], help="force the form instead of detecting it")
    parser.add_argument("--brief", "--full", dest="full", metavar="BRIEF", help="for an executive summary: the brief it comes from, to compare identifiers and titles")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args()

    try:
        form, report, words = run(args.path, args.freeze, args.form, args.full)
    except (OSError, UnicodeDecodeError) as error:
        print("cannot read %s: %s" % (args.path, error), file=sys.stderr)
        return 2

    errors, warnings = report.count("ERROR"), report.count("WARN")
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    items = sorted(report.items, key=lambda i: (order[i["level"]], i["line"] or 0))

    if args.json:
        print(json.dumps({
            "path": args.path, "form": form, "mode": "freeze" if args.freeze else "draft",
            "words_body": words[0] if isinstance(words, tuple) else words,
            "words_file": words[1] if isinstance(words, tuple) else words, "errors": errors, "warnings": warnings, "findings": items,
        }, ensure_ascii=False, indent=2))
    else:
        mode = "freeze check" if args.freeze else "draft check"
        print("%s — %s form, %s, %s" % (args.path, form or "unknown", mode, describe(words, form)))
        for item in items:
            where = "line %-4d" % item["line"] if item["line"] else "         "
            print("%-5s %-3s %s %s" % (item["level"], item["code"], where, item["message"]))
        print("---")
        if errors:
            print("%d error(s), %d warning(s). Fix the errors." % (errors, warnings))
        elif warnings:
            print("No error, %d warning(s). Read them: each one is a judgement call." % warnings)
        else:
            print("Nothing to fix.")
    if form is None:
        return 2
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
