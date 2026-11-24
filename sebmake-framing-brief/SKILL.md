---
name: sebmake-framing-brief
description: "Write, check and freeze a framing brief (\"brief de cadrage\", BC) — the one-page document a team agrees on before any spec or design starts, which freezes why a subject matters and what is in and out of scope. Use this skill whenever someone wants to frame, scope or kick off a feature, a project or a request; turn notes, a concept paper, a meeting transcript or mockups into a brief; prepare or run a framing, scoping or kickoff session; find out whether a brief is ready to freeze; or compare a spec with a brief that was frozen. Use it even when the words \"framing brief\" are absent — \"cadrer un sujet\", \"note de cadrage\", \"scoping doc\", \"one-pager before the PRD\", \"what's in and what's out\", \"on gèle le périmètre\". From a bare idea in one sentence it draws the brief map: how many briefs, in which order, and what each must settle. It first estimates the size of the subject (too small for a brief, short form, full form, or too big and to split), asks the person the few things only they know, and works live with them during the session. It delivers the brief, a one-page executive summary on A4, or both, in the person's language (English and French templates included)."
---

# Framing brief

A framing brief is the page a team agrees on **before** anyone writes a spec or draws a screen. It freezes two things: **why** the subject exists, and **what is in and out**. Nothing is built or specified in it.

It exists because the moment a team agrees on a subject usually has no support. It happens in fragments, its only trace is one person's paper, and the disagreements surface three documents later, when they are expensive. The brief gives that moment one page that everybody reads, fills in together and signs.

Three ideas hold the whole thing up. Keep them in mind; every rule below follows from one of them.

1. **The brief is the support of the session, not its minutes.** It is pre-filled before, filled in on screen during, read aloud and frozen at the end.
2. **It freezes with holes, never with a disagreement.** A missing fact becomes a named question with an owner and a date, and the brief freezes anyway. A disagreement on the why or the scope sends the subject back to a session.
3. **Nobody decides in someone else's place** — you least of all. What the owner of a decision has not said is a question for them, however obvious the answer looks.

## What you may be asked for

| The person wants | What you do |
| --- | --- |
| A brief from notes, a paper, a transcript or mockups | Steps 1 to 8 below |
| To know whether a subject deserves a brief, or how many | Step 3, the size estimate |
| How many briefs an idea needs, and what goes in each — often from one sentence ("an app so that parents know each morning whether the school bus runs") | The section "The brief map" below |
| A one-page executive summary of a brief, for a decider or someone absent | Step 6, "The executive summary" |
| To prepare or run the session | Read `references/session.md`, give the agenda and the questions to send |
| To fill the brief live, during the session | Step 4, "In the session" |
| To know whether a brief can freeze | The section "Can it freeze?" below |
| To record what the session decided | Update the brief: tick, turn ⚠️ into ✔, remove the `[proposed]` marks that were confirmed, list the holes |
| To compare a spec with a frozen brief | The gap report, last section of `references/session.md` |

## Step 1 — Look for what already exists

Before writing, look for a brief on the same subject wherever the team keeps them: the tracker, the docs tool, the folder you were given. If you find one, **say so before you start**: what exists, in which state, and the options (update it, split it, write a new one). Then wait for the choice.

The risk is the duplicate, not the absence. A second brief on a subject that already has one creates two scopes, and people do not know the first one exists. If you cannot search their tools, ask whether a brief exists, with the questions of Step 4.

## Step 2 — Read the material and sort it

Read everything you were given, mockups first when there are any. Sort each statement into one of four piles:

- **Decided**, by the person who owns that decision. Note who and when.
- **Proposed**, by the author of the paper or by someone who does not own the decision.
- **Open**: nobody answered.
- **Contradictory**: two sources say different things.

Who said it matters as much as what was said. The why and the scope belong to the decider (the sponsor, the head of product, the client). Feasibility belongs to engineering. What one person wrote before the session — the requester's message, a product manager's paper — is a proposal until its owner confirms it, unless it quotes a decision that owner already made. When the material does not say who gave a line, that is a question for the person (Step 4).

Three checks at this point save the brief later:

- **Screens against decisions.** When mockups arrived after earlier decisions, compare them. Design often moves past what was framed. A screen that contradicts a decision becomes a question; do not pick a side silently.
- **Nothing invented.** No deadline, number, rule, scope line, constraint or name that is not in the material. What is missing becomes a question with an owner, or `[to provide]`. A date given as "Monday" stays "Monday" when you cannot know the calendar date. An answer date nobody gave is "before the session", or "before the next session" when none is fixed — never a date you chose.
- **Who else must say yes.** Personal data, money, a contract, a law, a vendor, another team: when the subject touches one and its owner has not spoken, send that owner an open question. Never write the constraint yourself. A legal answer rules out the short form.

## Step 3 — Estimate the size

A brief frames a subject whose executive summary fits on one A4 page: neither too big nor too small. Estimate it from the sorted material before you write a line. The size decides everything after it: a ticket, one brief in the short form, one in the full form, or several briefs.

Count these, from the material only:

| What you count | What counts as one |
| --- | --- |
| Outcomes | A sentence "who can now do what" that the subject delivers |
| Groups whose habit changes | Members, staff, a partner: each one that will do something new |
| Flows | A path one group follows from start to end, with its own screens to design |
| Rules | What the material states or proposes as a rule |
| Decisions to make | Each disagreement, and each choice nobody has made yet |
| Outside owners | Law, money, personal data, a vendor, another team |

Then read the counts against this grid:

| Size | The signs | What you do |
| --- | --- | --- |
| **Too small** | One outcome, no decision to make, one rule at most, nobody's habit changes beyond a detail of one screen | No brief. Say why in one line, and propose a ticket or the brief it belongs to. If the person still wants one, use the short form. |
| **Short form** | One outcome, one group, built on what exists, four rules at most, one question for the decider | One brief, short form |
| **Full form** | One outcome, up to five rules, up to four decisions, up to five facts to ask | One brief, full form |
| **Too big** | Two outcomes, or two groups that each need their own flow, or past five rules or four decisions | Split before you write: one brief per outcome, or a vision brief and one per flow |

Give the estimate first, with the counts that decide it: "One outcome, one group, three rules, one question for Paul: short form." A count is a reason the person can check; "it feels big" is not.

A group that only receives what another group's flow produces is not a second subject. The front desk that scans a pass a member created is a scope line of the member's brief. It becomes its own subject when it has its own screens to design and its own decisions.

When the estimate says too big, propose the cut — past three briefs, as a brief map (section "The brief map"). Name each brief by its outcome sentence, say which one freezes first, and ask which one to write now. The one that freezes first is the one the others depend on: the vision before its flows, and a flow whose result another flow uses before that other one. When two briefs depend on nothing but the vision, they freeze side by side. If the person cannot answer now, write the one that freezes first: what belongs to the others goes in its "will not be in it", each line pointing to the brief that will hold it. When it says too small, do not write a brief to have one: a framing session costs several people an hour or two.

The executive summary checks the estimate. When the message, the scope and the decisions to make do not fit on its one page, the subject is too big: say so and propose the cut. When they fit and only the wording overflows, shorten sentences, never a line of content.

## Step 4 — Ask what only the person knows

The person working with you is usually preparing the session, or sitting in it. In a few seconds they can answer what the material leaves unclear. An answer now is worth more than a `[to provide]` the room has to chase. So ask before you write.

Ask one batch: five questions at most, the most blocking first. Make each one answerable in a line or by picking an option, and number them so the person can reply "1 Thomas, 2 yes". Ask only what the person can know and the material does not say:

- **The size**, when the estimate says too big or too small: the cut you propose. Always first, because it changes everything after.
- **The format**: the brief, the one-page executive summary, or both. Always the second question, right after the size: to stay at five, merge two other questions rather than drop this one. With no answer, write the brief and offer the summary in one line. "The brief" means the brief in the form the estimate chose, short or full; say it that way, so nobody hears "the full form".
- **Who gave a line**, when the material does not say: the requester, someone in the trio, the decider. Its mark depends on it.
- **Who decides**, when nobody is named.
- **Whether a brief already exists** (Step 1), when you cannot search their tools.
- **A fact the material points to without giving it**: the number behind "lots of complaints", the time of the session, the calendar date of "Monday".
- **What is not in this request**, when the material leaves nothing out.

Do not ask the person what belongs to someone else. A choice the room must make becomes a `T` in the brief. A fact only another person has becomes an open question sent to them. Asking the person to settle a disagreement between two colleagues would make them decide in someone else's place.

Then write with what you got. An answer is a source: note it as "<name>, in this conversation". It removes a `[proposed]` mark only when the person who answers owns that decision.

When the person says to go ahead, or cannot answer now, do not wait. Write with the marks and `[to provide]`, and put the unanswered questions at the top of your message.

**In the session.** When the person tells you the room is meeting now, work block by block, in the order of the brief. Show the block, take what the room says, update the file, and run the checker at the end of each block. Remove a `[proposed]` mark only when the person tells you its owner confirmed it aloud. Keep each turn short: the room is waiting on you.

## Step 5 — Choose the form

| | Short form | Full form |
| --- | --- | --- |
| The subject | One outcome, builds on something that exists | New ground, several screens or several roles |
| Size | About a week of work | More than a week, or more than one team downstream |
| Rules | Four at most, none legal or computed | Up to five, some legal, computed or dependent |
| Session | One hour, ends on a signed bet | Two hours, ends on four sentences |
| Template | `assets/template-short.<lang>.md` | `assets/template-full.<lang>.md` |
| Filled example | `assets/example-short.en.md` | `assets/example-full.en.md` |

If the person names a form, use it. Otherwise the estimate chose it: say which and why in one line.

The page is the ceiling of what a few people can fill in **and read aloud** in one session. Do not fill the open questions to their cap: ask only what the session needs before it can decide. A request nobody followed up, a detail the spec will settle, who asked for what: these go in the notes, not in an open question.

If the person keeps one brief past four decisions, keep the disagreements first. A question where two named people hold two positions always keeps its `T` and its *blocks the freeze*; a question nobody disputes is the one that goes to the decider as an open question, or to the session. Two positions on one line — "Dario wants it, I think later" — are a disagreement, never a request nobody followed up, and never a line filed in "waits": that would pick the side that said "later".

## Step 6 — Write it

Copy the template for the chosen form and language, keep its sections in order, and fill it. Read the matching example once before you write: it shows the density to aim for.

Write in the language the person writes in. Templates exist in English (`.en.md`) and French (`.fr.md`). For another language, translate the English template and keep the identifiers (`R1`, `T1`, `O1`, `F1`, `G1`) and the marks (`[proposed]`, ⚠️, ✔) as they are.

The rules that matter most, each with its reason. The details and the traps are in `references/writing-rules.md`; read it before your first brief in a conversation.

- **Mark what is not confirmed, line by line.** Every line that comes from someone who does not own it ends with `[proposed]` (`[proposé]` in French); a decided line carries no mark and names who decided it. Never mark a whole section when one line in it is decided: the mark on the heading hides that line. This is what lets a team pre-fill a brief without the draft passing for a decision, and no mark may remain at the freeze. What one person wrote before the session stays `[proposed]`, whoever wrote it, unless it quotes a decision its owner already made.
- **In the scope, the rules and the scenarios, a line no source gives is a question, not a proposal.** `[proposed]` carries what someone in the material said. What you think is missing — the old way that stops, a site, a plan, a role — is asked: a `T` under the scope, or an open question to the decider. A question in the material ("maybe?", "no idea", "??") stays a question too. A line you wrote yourself, marked `[proposed]`, reads as somebody's position.
- **The slots the template asks for are yours to propose.** The context lines, what we count, a line for what must not get worse, the default of a question to the decider: fill them from the material, mark them `[proposed]`, and say in the notes that the draft proposed them. An empty slot gives the room nothing to react to; a marked proposal does. A default is always the most prudent answer: with no reply, the risky thing does not happen.
- **Say how we know, and how we will know.** The context says what people do today instead, gives a proof (a fact seen or heard, by whom and how often, and a number, or *missing* with who counts it) and names what we will count thirty days after release, with a threshold and what must not get worse. The short form carries the same in its proof, its bet and its thirty-day table. What we count starts from a number the material already gives — usually the proof's own number; propose it. Only the threshold waits for the decider. A bet that no result can contradict is not a bet, and a threshold chosen after the result is not a threshold.
- **A decision to make is a question with boxes.** An identifier (`T1`), a question that ends with a question mark, two to four options, and always a last option **Other**. No context sentence before the options. People answer a list of options in seconds; they argue with a paragraph. The reasons are not lost for that: who holds each option, and why, goes in the notes and sources. The options do not lean: the rule above a question never states one of them, and the option from the paper is never first.
- **Each question sits under what it decides**, flagged ⚠️: under its rule, or under the scope when it has no rule. Say after the title what else it decides. The reader then sees the hole exactly where it is, and nobody has to hunt for it in a separate section.
- **A disagreement is written as a question, and it is not a hole.** When two people disagree on the why or the scope, mark the disputed line `[proposed]`, put both positions as options of a `T` under the scope, and write after its title that it *blocks the freeze*. Do not pick a side. Only a disagreement carries those words: a scope question nobody disputes is simply ticked in the session.
- **A question with no options is asked outside the brief.** A fact to check, or someone to go and ask, is sent to a named person, one question per thread, with the date the answer is needed. The brief keeps one pointer line per question: who, about what, by when. A table of questions in a document notifies nobody.
- **Scope has three groups**: what this version contains, what will not be in it (and where it lives instead), what waits for a later version. The last two are different decisions: the first never comes back, the second does.
- **Counted.** Five rules, three or four decisions to make, five open questions, three or four scenarios, three or four principles per screen. Beyond the caps, split. The brief has no page limit; what must fit on one A4 page is its executive summary.
- **Plain words.** A twelve-year-old should follow it. One idea per line, sentences of fifteen words or fewer, a diagram before a paragraph, no sentence that comments on the document itself.
- **Product only.** No development schedule, no list of work items, no calendar section, no inventory of components. Those are decided after the freeze, by other people, on other documents.

### The executive summary

The summary is the one page someone reads who will not fill in the brief: the decider before the session, a person who was absent, a manager. It is read, not filled in: no boxes, no marks. Template: `assets/template-summary.<lang>.md`; example: `assets/example-summary.en.md`.

- **It comes from the brief and adds nothing.** Same identifiers, same question titles, same people. When the brief changes, rewrite the summary from it; never edit the summary alone.
- **When no brief stands behind it** — only the summary was asked for — sort the material as for a brief first, then write the summary, and say so at the top, in place of the Brief line: `⚠️ **No brief behind this summary yet.** It is written from the request; the brief comes before the freeze.` In French: `⚠️ **Pas encore de brief derrière ce résumé.** Il est écrit d'après la demande ; le brief vient avant le gel.` End the summary on what must be found out first, not on what "is in the brief". The checker warns when a summary says nothing either way.
- **The message first.** Two or three sentences in a neutral voice, third person: who can now do what, why now, and what the session must settle before the brief can freeze.
- **Then one before / after diagram**, copied from the template with its styles. Row TODAY: what people do today, from the brief's Today line, ending on the cost the proof counts. Row AFTER: the path the scope opens, ending on what changes for the person, from the brief's "So that" or measure. Three steps per row at most, three or four words per box, left to right: the two rows must not look alike, and a longer row shrinks below what a printed page can read. Nothing in it that the brief does not say. The details are in `references/writing-rules.md`, section 15.
- **Five bullets of one line, each with a bold label.** The first says what is settled, and by whom, or that nothing is: everything else is proposed, and the summary must not pass a draft for a decision. Then why now (today and the proof, with its number), what is in, what is out and what waits, what is still to find out (who, by when).
- **To decide**: one line per `T` and `G1`, its options in a row with Other, who holds which, and *blocks the freeze* when two named people disagree. The disagreements come first.
- **How we will know**, in one or two sentences, then **Next step**: the session, what it settles first, who freezes.
- **One A4 page**: about 380 words, as the checker counts them, which leaves room for the diagram. When the message, the scope and the decisions do not fit, the subject is too big (Step 3). Rules, scenarios, screen principles and sources stay in the brief.
- **For a short-form brief**, the message is the principle, "In" holds the rules in one line, "To decide" holds `Q1`, the question for the decider, with its default, and `Q2`, the threshold, "How we will know" holds the pass and fail lines, and "Next step" the bet to sign. The short form numbers these two questions in its watch-outs (`Q1`, `Q2`) so the summary and the checker can follow them.

## Step 7 — Check it

Run the checker on the file:

```bash
python3 scripts/check_brief.py path/to/brief.md
python3 scripts/check_brief.py path/to/brief.md --freeze
python3 scripts/check_brief.py path/to/brief-summary.md --brief path/to/brief.md
python3 scripts/check_brief.py path/to/brief-map.md
```

Without a flag it checks a draft: sections, the Today, proof and measure lines, what missing the date costs, the decider last in the freeze round, the caps, the shape of each question, boxes that would not be tickable, sentences too long. With `--freeze` it also refuses any remaining `[proposed]`, any question left unticked unless an owner and a date are written under it, any value left "to set", and any freeze line its owner has not ticked. On an executive summary (its title ends with "executive summary") it checks the message, the five bullets, the decisions and the one-page length; with `--brief` it also checks that every identifier and question title matches the brief, and that no decision of the brief is missing; a summary that says neither which brief stands behind it nor that none does gets a warning. On a brief map (its title starts with "Brief map" or "Carte des briefs") it checks the vision brief first, an outcome, a form and a freeze order on every row, the diagram, no rule and no box, and the one-page length. It exits with 1 when something must be fixed.

Fix the errors. For a warning about a cap, do not delete content to pass: tell the person the subject should be split and let them choose.

Then check what a script cannot see:

- Does each statement in the body trace back to the material, and to the right person?
- Is each line of "what will not be in it" pointing somewhere real, whose owner knows it is coming?
- Does a line commit someone outside the room — the law, the money, another team? Then they have been asked.
- Does everyone whose habit changes appear in the scope, and does the old way stay, stop or count?
- Do two blocks contradict each other — a scenario that assumes a rule the brief leaves open, a scope line a question could remove?
- If the brief has a parent or sibling brief, do they still agree?

## Step 8 — Hand it over

Give three things, and keep the message short:

1. **The brief**, as a Markdown file named `brief-<subject>.md`, or pasted where the person asked; the executive summary as `brief-<subject>-summary.md` when it was asked for; a brief map as `brief-map-<subject>.md` (`carte-des-briefs-<sujet>.md` in French).
2. **The questions to send**, grouped by person, each with the date the answer is needed. They stay out of the brief body.
3. **Three lines**: the size estimate and the form, with the counts behind them; what is still `[proposed]`; what would block the freeze today.

Do not explain the method in the message. If the person wants the brief posted in their tracker and you have the tool to do it, confirm first: posting and mentioning people notifies them.

## The brief map

Someone often arrives with an idea, not a subject: "I want an app so that parents know each morning whether the school bus runs." That is several briefs, and the first useful answer is how many, in which order, and what each must settle. The brief map gives it on one A4 page. Template: `assets/template-map.<lang>.md`; example: `assets/example-map.en.md`.

1. **Estimate as in Step 3, on the idea.** Count the outcomes hidden in it ("does the bus run?" holds whether it is running, which bus is the child's, when it reaches the stop, and the notice that brings them together), the groups whose habit would change, the decisions it raises, and the outside owners it touches: an authority, a data source, legal, personal data. Give the estimate first, with its counts.
2. **Cut by outcome.** Brief 0 is the vision: who it is for, the promise, what is out. Then one brief per outcome, each named by its sentence "who can now do what", with the form its own size calls for. A brief that waits for an outside owner's yes — a law, personal data, money, another team — takes the full form, whatever its size. Past seven briefs it is a programme, not a subject: group them, or map the first release only.
3. **Order the freeze.** The vision first; then the brief the others depend on; briefs that depend only on the vision freeze side by side; the one that brings the others together freezes last. Draw it as the template's diagram, left to right.
4. **Under each brief, what it must settle**: two questions at most, worded as questions. A question an outside owner must answer says so ("legal decides"). The prudent default holds here too: when data is missing, the answer is never "yes".
5. **Off the map**: what the idea brings to mind but the first version should not carry, each with "later" or "not in it", to confirm.
6. **Nothing invented, and very little material.** One sentence gives almost nothing. What you add from general knowledge — how a domain is regulated, which data exists, which classes or categories apply — is a question to check with its owner, never a rule, a scope line or a figure. The map says how many briefs and what each must settle; it does not fill them in for the team.

Ask the Step 4 batch before you draw, in the same order, five questions:

1. **The cut**: the briefs you see, and the vision first. Is the cut right?
2. **The format**: the map alone, the map and the vision brief, or every brief.
3. **For whom first, and where**: one question — the people the first version serves, and the country or market when a law governs the subject.
4. **Who decides.**
5. **Whether a brief already exists.**

The questions go in your message, not on the map. With no answer, deliver the map alone and offer the vision brief in one line.

## Can it freeze?

When someone hands you a brief and asks whether it can freeze, the answer they need is short and sorted.

1. Run the checker with `--freeze`, then read the notes and sources: what the session left unsettled is usually written there, not in the body.
2. Answer **yes or no** in the first line.
3. Sort what is in the way into two lists. **What sends the subject back**: a disagreement on the why or the scope, a feasibility refusal, an answer that overflows the frame (a new team, a second subject), a count that does not match its list (it may hide a line nobody agreed to). **What can be fixed now**: marks to confirm, a question to tick — a scope question nobody disputes is one: the decider ticks it —, a missing Other, a box that cannot be ticked, a vague destination, a freeze round out of order. A team that sees both in one list fixes the easy ones and freezes over the real one. A `[proposed]` line that would overflow the frame once confirmed — a sixth rule, a second team — goes in the second list, with "split if kept": the decider may still drop it.
4. Say who has to do what. Most of these need a person, not an edit.
5. Offer a corrected copy. If you make one, change the form only: move a box to a list line, add the missing Other, put the freeze round back in order with the decider last, add the template's line where a required one is missing (Today, Proof, the cost of missing the date) with `[to provide]` and nothing else. One addition goes further, because without it the copy would read as settled: when the notes record two named people disagreeing on the why or the scope, and the body states the disputed line as decided, write the disagreement the way a draft does. Mark that line `[proposed]` without rewording it, and add a `T` under the scope with the next free number: each position as an option, **Other** last, nothing ticked, *blocks the freeze* after its title. Never pick a side. Apart from that, never write content into those lines, tick an answer, add or remove a `[proposed]` mark, change a count or cut a rule. Report those instead.
6. Every defect appears in one of the two lists, including the ones you fixed in the copy.

A question may stay open through the freeze when it decides neither the why nor the scope: write its owner and a date under it (`references/session.md`, section 6).

## The session and the freeze

The brief is frozen at the end of the session, by the people in the room, in their own words. In the full form, four sentences, the decider last so that nobody aligns on the person who decides:

- **Engineering** — "no major obstacle in here"
- **Product** — "I can write the spec"
- **Design** — "I can start the design"
- **Decider** — "the problem and the scope are the ones I want"

Each one ticks their own line, or writes it in a comment: `Freeze signed · role · id`. In the short form, each member of the trio signs the bet the same way.

The facilitator runs the session, holds the keyboard and does not confirm. You never write a signature, tick a freeze line or record a decision nobody made. Teams differ: map their people to these voices, and when a voice is missing or one person freezes alone, the brief says so in a visible line.

`references/session.md` has the agenda minute by minute, what to do when a confirmation is refused, and what happens after the freeze: the body no longer moves, two kinds of writing remain allowed, and the brief becomes the reference the spec is compared with.

## Files

- `assets/template-full.en.md`, `assets/template-full.fr.md` — the full form
- `assets/template-short.en.md`, `assets/template-short.fr.md` — the short form
- `assets/template-summary.en.md`, `assets/template-summary.fr.md` — the one-page executive summary
- `assets/template-map.en.md`, `assets/template-map.fr.md` — the brief map, from an idea to a set of briefs
- `assets/example-full.en.md`, `assets/example-short.en.md`, `assets/example-summary.en.md`, `assets/example-map.en.md` — filled examples; the summary is the full example's
- `references/writing-rules.md` — how to write each block, and the traps
- `references/session.md` — before, during and after the session; the gap report
- `scripts/check_brief.py` — the checker (Python 3.9 or later, no dependency)
