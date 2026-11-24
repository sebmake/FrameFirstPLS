# Writing rules

How to write each block of a framing brief, and the traps that come back every time. Read it once before your first brief in a conversation.

## Contents

1. What a brief carries, and what it leaves out
2. Two formats, and the caps
3. Plain words
4. Context, proof and measure
5. The `[proposed]` mark
6. Questions
7. Scope
8. Rules
9. Scenarios
10. Screens
11. The short form
12. Several briefs on one subject
13. Title, notes and terms
14. Rendering traps
15. The before / after diagram of the executive summary
16. The brief map

---

## 1 · What a brief carries, and what it leaves out

A brief answers two questions: why are we doing this, and how far does it go. Everything else belongs to a later document.

Leave these out, even when the material is full of them:

- **Where and when it gets developed.** No development schedule, no "no engineering slot is planned" line. The brief is upstream of that decision, and a line about a missing slot reads like a defect when it is the normal state.
- **The list of work items.** The brief may ask whether the subject is too big. It does not list the pieces: the breakdown happens after the freeze, on a scope that no longer moves. A list written before is wrong the moment the session changes one line.
- **A calendar section.** One question carries the date: does the subject make it, yes, reduced, no. Its title says what missing the date costs, in the decider's words, or `[to provide]`. "Yes, reduced" counts only when the lines that leave are already in "waits".
- **An inventory of components.** Columns, fields and buttons belong to the implementation ticket.

One exception: a question that the session itself raised is recorded, because it was asked. A question you deduced from reading a roadmap is not.

A question that does not belong to the document creates a false hole, and a false hole blocks the freeze.

## 2 · Two formats, and the caps

A subject is the right size when a few people can settle it in one session. Two formats carry it:

- **The brief** — in the short or the full form, the support of the session, filled in and frozen. It has no page limit: the caps below keep it readable aloud.
- **The executive summary** — one A4 page, read by someone who will not fill in the brief. It is written from the brief and adds nothing (SKILL.md, Step 6).

| Block | Cap |
| --- | --- |
| Rules | 5 (4 in the short form) |
| Decisions to make (`T`) | 3 or 4 |
| Open questions (`O`) | 5 |
| Scenarios | 3 or 4 |
| Principles per screen | 3 or 4 |
| Executive summary | about 380 words, one A4 page |

**Why the summary is the page, not the brief.** Printed on A4 (Arial 11 pt, 2 cm margins, tables in 10 pt), an empty template already fills more than a page in the short form and two in the full form: its blocks, boxes and tables take the room, not the words. A summary in prose and one-line bullets holds the message, the diagram, the scope and the decisions in about 380 words. When it cannot, the subject is too big.

**The checker reports the body's words** — the context to the deadline, or the principle to the bet sentence — and the whole file's. It leaves out the diagram's code, the Markdown marks and any line copied word for word from a template.

**The notes are an annex, not a second brief.** One line per source: who said what, and the reason behind each position.

Past a cap, the subject is not ripe: it splits. Say so and propose the split. Cutting content to fit hides the problem, and a brief that hits every cap takes no more additions: sharpen what is there, or comment.

## 3 · Plain words

The test: a twelve-year-old follows it.

- One idea per line. Sentences of fifteen words or fewer.
- A diagram, a table or a list before a paragraph. Blocks of prose are correct and unread.
- Say what the thing does for the person, in the person's words. No internal code names in the body; they go in the notes.
- **No comment on the document.** "Without this answer the rest is useless", "we invent nothing here", a line that recounts the questions, a caption that repeats the diagram: delete. A line that carries no fact, no question and no owner goes.
- No empty connectors: "on this last point", "as mentioned above".

## 4 · Context, proof and measure

The context is the why, and it is the decider's. Three lines say who, what and what changes; three more say what people do today, how we know, and how we will know.

- **As** names the people who feel it, and when: "the parent of a pupil, the week a lesson clashes", not "users". A persona that is everyone is no one.
- **I want** is an outcome, in their words. A screen or a button there is scope smuggled into the why: move it to the scope and ask what it is for.
- **Today** says what they do instead, and why it is not enough. A habit that works well enough beats a new feature. If they do nothing, say so.
- **Proof** is a fact *seen* or *heard*, by whom and how many times, and a number. Once is an anecdote: say so. A missing number is written *missing*, with who counts it and by when. Evidence against the subject is kept like any other fact.
- **We will know it worked** names what we count, its value today, the threshold thirty days after release, and what must not get worse. The threshold belongs to the decider; until they give it, it is `[to provide]`.

**When the requester is not the decider.** The person who asks may propose a threshold; the decider sets it. A number from the requester is written with `[proposed]` and their name in the notes. It becomes the threshold when the decider says it, in the session or in writing. A number nobody gave stays `[to provide]`, with the decider named as the one who gives it.

Prefer what the team can count without asking users: calls, tickets, a register someone already keeps. A measure that needs many user sessions rarely happens.

**What we count is proposed, the threshold is not.** When the proof already counts something — 38 paper sign-ins a week, 61 calls a month — that is the first candidate for what we count: write it, marked `[proposed]`, with today's value. Leave "what we count" `[to provide]` only when the material counts nothing at all. The threshold stays the decider's.

## 5 · The `[proposed]` mark

A pre-filled brief is useful only if nobody mistakes the draft for a decision.

- A line ends with `[proposed]` when it comes from someone who does not own it: the author of the paper, a colleague, a sketch.
- A line that quotes a decision made by its owner carries no mark. It names who decided, in italics — *Nora, 2 March* — and the notes give the source.
- **What one person wrote before the session is a proposal, whoever wrote it.** The requester's message, the product paper, a sketch: each line stays `[proposed]` until its owner (table below) confirms it, unless it quotes a decision that owner already made. When the material does not say who gave a line, ask the person you work with; do not guess its owner.
- **Mark line by line, never a section.** A mark on a heading covers every line under it, including the ones the decider settled: the reader can no longer tell them apart. A heading may carry the mark only when not one line under it is decided. Many marks on a page are the honest state of a draft; they go one by one, as the room confirms each line.
- **No source, no line — in the scope, the rules and the scenarios.** What the material does not say is not written there as a proposal, even marked. The old way that stops, a site, a plan, a role you think is missing: ask it, as a `T` under the scope or an open question to the decider. A line you wrote alone and marked `[proposed]` reads as somebody's position, and the room approves it as one.
- **A question in the material stays a question.** "Maybe the code opens the door?? no idea" is not a scope line waiting for an answer; it is an open question, or an option of a `T`. Writing it as a line, even marked, is the hardening trap below.
- **The slots the template asks for are yours to propose.** The context lines (As, I want, So that), what we count, the line for what must not get worse, the default of a question to the decider: fill them from the material, mark them `[proposed]`, and add one line in the notes, "proposed by the draft". The rule above does not apply to them: an empty slot gives the room nothing to react to. Choose the proposal that commits least. For a default, that is the most prudent answer: the one that takes no risk the decider has not accepted. When in doubt, the action does not happen.
- A guess is not a proposal. A guess becomes a question.
- A missing value you cannot propose is `[to provide]`.
- A date stays as it was given. "Monday" stays "Monday" when the calendar date is unknown; a deadline nobody gave is `[to provide]`.
- None of these marks survives the freeze.

**The hardening trap.** A position copied from an earlier document loses its warning on the way. The paper said "probably monthly ⚠️"; the brief says "billed monthly". Scenarios are where this slips most easily, because a scenario states its premise as a fact. When you copy, carry the mark.

**Who owns what.**

| Subject | Owner |
| --- | --- |
| The why, the scope, the date | The decider |
| Feasibility, technical constraints | Engineering |
| The rules as they will be specified | Product |
| The experience, the screens | Design |
| Personal data, money, a contract, a law, a vendor, another team | Its owner, asked by name before the session. No answer: the line stays `[proposed]`, or becomes a question with an owner and a date. |

A constraint is never deduced. If engineering did not say it, it has not been looked for: ask.

Nobody in the room owns the law, the money or another team's work. When the subject touches one, send its owner an open question and never write the constraint yourself. A legal answer rules out the short form.

## 6 · Questions

There are two kinds, and they do not live in the same place.

### Decisions to make — `T`

Something the room can settle by choosing.

```
⚠️ **T1 · Is the reason mandatory?** — *also decides R2, scenario 3*

- [ ] Yes, always
- [ ] Only above a threshold
- [ ] No
- [ ] **Other** — …
```

- A product question, in question form, ending with a question mark.
- Two to four options, then **Other**. Always. If nobody can tick Other and write, a wrong option gets ticked to move on.
- No context sentence between the title and the options. If the question needs a paragraph to be understood, it is two questions, or it is not ready.
- After the title, in italics, what it decides: the rules, scope lines, scenarios and principles that depend on the answer. Include what an answer would bring into the scope: "also decides whether payment enters the scope". The link then reads both ways.
- The options stay bare, and the reasons are kept. Who holds each option, and why, goes in the notes and sources, one line per position. A brief that offers "free" against "paid" without the reason for either makes the room argue it again from zero.
- It sits right under the rule it opens. A question with no rule sits under the scope, and the scope line it touches says so: `(⚠️ **T3**, below)`.
- The header lists the decisions in one line, each with where it sits: `To decide: T1 how many moves per term? (under the scope) · T2 …`. The decider reads that line first, and reading order no longer follows numbering.
- Not a `T`: the cycle, the workload, the order of development.
- **The options do not lean.** A rule that waits for a `T` states only what is settled, then "settled by **T2**"; it never states one of the options. The option from the paper is never first: a room ticks the first box it recognises.

**A subject with no agreed content gets no rule.** When nobody has settled whether a thing exists at all (a price, a limit), do not write a rule to hold the question. Put the question under the scope line it would add or remove.

**A disagreement blocks the freeze, and nothing else does.** When two named people hold different positions on the why or the scope, mark the disputed line `[proposed]`, give each position as an option, and say it in the italics:

```
⚠️ **T4 · Can group lessons move, or single lessons only?** — *decides the scope line "A parent moves one lesson": blocks the freeze*

- [ ] Single lessons only
- [ ] Single and group lessons
- [ ] **Other** — …
```

Name who holds each position in the notes, not in the options. Do not pick a side, and do not let the brief read as if one had been picked.

**Spot a disagreement in a single line.** "Dario wants recurring guests, I think later" is two named people and two positions: a disagreement, even tucked in a list of "other things people mentioned". It is not a request nobody followed up, and it never goes to "waits": filing it there picks the side that said "later".

**Under the cap, disagreements keep their place.** When there are more than four decisions to make, a disagreement always stays a `T` that blocks the freeze. The questions nobody disputes are the ones that move: to the decider as an open question with its options in the thread, or to the session.

A scope question that nobody disputes — the paper simply did not say — does not carry *blocks the freeze*. It is ticked in the session like any other; left unticked, it stops the freeze through the ordinary rule below. Writing "blocks the freeze" on every open scope line tells the room there is a conflict where there is only a blank, and hides the real one.

**A question left open at the freeze.** A `T` that decides neither the why nor the scope may stay open through the freeze, as a named hole. Write one italic line under its options:

```
*Open at the freeze — owner: Nora, by 20 March.*
```

In French: `*Ouverte au gel — porteur : Nora, pour le 20 mars.*` Without that line, an unticked question stops the freeze. A question marked *blocks the freeze* can never carry it. When the owner gives no date, write "by the next session" (*pour la prochaine séance*); never pick a date for them.

**Identifiers never move.** `T2` stays `T2` when it is moved, answered or closed. Other briefs and the spec quote it. Retired numbers leave a gap; do not renumber.

**After the session.** A settled question turns from ⚠️ to ✔, with the ticked box. Without that, a brief keeps ⚠️ everywhere and nobody sees what is still open. A question that was closed without being answered stays as one italic line saying it is closed and why. It stops the next session from reopening it.

**Ticked box against old text.** A box ticked in the session can contradict a paragraph written before it. After recording answers, reread the blocks each answer decides and rewrite them.

### Open questions — `O`

Something nobody in the room can choose: a fact to check, a person to go and ask.

**`O` or `T`?** If the room could tick between two to four answers, it is a `T`, even when the decider is the one who answers. It becomes an `O` only when the answer needs work before the session (which sites are ready, how many guests came last month), or when the `T` cap is reached and nobody disputes it; its options then go in the thread. A disagreement is never moved to an `O`.

- One question per thread or comment, addressed to a named person, with the date the answer is needed. Use the person's name, not their role: the point is that they get notified and answer on their own time.
- When the material names nobody for it, write the role and `[to provide]`, and ask the requester who it is. Never pick a person.
- When no session date is fixed, the answer is needed "before the next session" (*avant la prochaine séance*). Never invent a calendar date.
- **Ask only what the session needs before it can decide.** Five is a ceiling, not a target. A request nobody followed up ("someone in ops asked for the guest's photo"), who asked for what, a detail the spec will settle: write it in the notes, with its source. The room can raise it; it does not cost an open question. A request one person wants and another defers is not "not followed up": it is a disagreement, and a `T`.
- The full wording and the answer live in the thread. When there is no tracker, give the questions in your message, grouped by person.
- The brief keeps one pointer line per question, in block 5 of the full form: who, about what, by when. Five at most, as plain list lines, never a table.

```
* **O1** · Tomas — free slots of one teacher, per day — answer by Friday 6 March
```

- A line of the body that waits for one of them says so in words: "(waits for **O1**)". It carries no ⚠️.
- The short form has no block for them. A fact to check about what exists goes in "What exists" as a row "❓ to check", with the name of the person asked.

**The ⚠️ marks a decision to make that is still open, and nothing else.** An open question (`O`) does not carry it. Neither does a plain production warning ("the screens only exist at desktop width"), which is written as text. Otherwise the reader looks for a box to tick.

## 7 · Scope

Three groups of bullets, each introduced by a sentence that carries its definition.

```
**What this version contains** — six items, and nothing else.

**What will not be in it**, because it lives elsewhere or does not exist.

**What waits for a later version**, without leaving the target.
```

- **Contains**: what gets built, not how. Announce the count in the sentence; it forces a recount at each addition.
- **Will not be in it**: each line says where the thing lives instead, after an arrow, or says it does not exist. "Later" is not a destination; another brief, an owner or a date is. This is where scope evaporates when it is left vague.
- A line that hands something to another team or brief names who there knows it is coming. A destination nobody expects is a line that will come back.
- Each person whose work or habit changes has a line in one of the three groups, and so does the old way of doing it: it stays, it stops, or it counts in the new rule. When the material does not say which, it is a question for the decider, never a line you write.
- When the product has plans or paid options, one "contains" line says which get it, and who pays when each use costs money. Not said: a `T` under the scope.
- Every "contains" line traces to a source. A line you would add yourself is a question (§5, "No source, no line").
- **Waits**: same subject, after the target date. These lines come back; the previous ones do not. Mixing the two is the classic mistake, because they are not decided the same way.
- One sentence per bullet. A bullet that overflows mixes two things.
- A design task is not a scope line. "Redo the banner" goes in the notes; the scope line says the banner text is rewritten.
- When a version is frozen smaller than the target, what leaves is named in one of the last two groups. Never deleted: that is what lets a team freeze without losing the target.

## 8 · Rules

One block per rule: a bold identifier and title, its nature in italics, then one or two sentences.

```
**R2 · A booking needs a paid deposit** — *product*

A booking is confirmed only once the deposit is received.
```

- Nature: *product*, *legal*, *calculation*, *dependency*.
- Add *one-way* to the nature when the rule cannot be undone after release: money moved, data deleted, a promise made to customers. Ask engineering or the decider; never deduce it. A one-way rule is the one to read twice in the session: `**R3 · A cancelled lesson is refunded at once** — *calculation · one-way*`.
- Five at most. These are the rules that shape the design; the full set is written in the spec.
- A rule whose answer depends on a question says so in its body: "Whether it is mandatory is settled by **T1**."
- No table for rules: a box inside a table cannot be ticked, and the question must sit under its rule.

## 9 · Scenarios

Given, when, then. Three or four: the ones that say when it is right. One nominal case, the refusal that matters, the edge that people will argue about. Detailed acceptance criteria belong to the implementation tickets.

A scenario must not assume the answer to an open question. If it does, mark it `[proposed]` and name the question.

## 10 · Screens

This block exists only when screens exist. It changes what the brief is for: the room validates intentions on real screens.

- One block per screen, three or four **principles**. A principle is an intention the room can approve or refuse: "invoices and credit notes live in one list", "the amount is typed, never computed", "no action from this panel".
- Not a principle: "a table with six columns", "a blue button on the right".
- Name each screen by the name of its frame in the design file, never by an internal identifier.
- Tick boxes must start a list line. A compact line with several boxes renders as plain text and nothing can be ticked.
- A screen with no mockup has principles that stay open. Say it; do not tick on its behalf.

Before writing this block, reread the earlier decisions against the screens (step 2 of the skill). If the design shows a payment screen and the decision said "no payment here", the brief cannot settle it alone: it becomes a `T`.

## 11 · The short form

Seven blocks, for a request that fits in about a week. Same idea, lighter body.

1. **The principle** — one bold sentence: who sees or does what. Then for whom, what they do today instead, and the proof: one feedback and one number. Say whether the feedback was *seen* (watched happening) or *heard* (reported), by whom, and how many times; once is an anecdote. A missing number is written *missing*, with who counts it and from when.
2. **The diagram** — the path, with the one question the screen answers.
3. **The rules** — the few that product proposes. Details come later, on the mockup.
4. **The watch-outs** — the question for the decider (`Q1`) and the threshold (`Q2`), each numbered so the summary and the checker can follow it, the right word to use, a rule that is coming, and what is not in this request.
5. **What exists** — what is already built, in review, cancelled, waiting. Starting from what exists is the point of the short form.
6. **The success criterion** — testable before building, on three cases, with a pass line and a fail line. Then the thirty-day table: what we look at, who counts it, the threshold, and one row for what must not get worse. Under it, what happens below the threshold: remove, rework or keep, signed again like the verdict.
7. **The bet** — "We bet that if …, then <what we count> reaches <the threshold>", signed by each member of the trio. Under it, the part most likely to be wrong; the first test aims at that part.

Specific to this form:

- **"Held by"** is the person who keeps the brief up to date and runs its sessions. When nobody was named, write `[to provide]`; do not guess.
- **"Decides"** names the person who answers the questions marked ⚠️ and sets the threshold. When the material only says who a question goes to ("a question for Paul, the owner"), write that name, marked `[proposed]`. When it says nothing, `[to provide]`.
- **A question to the decider carries its default.** "With no written answer before Thursday 2 pm: no." The week does not stop for a silence. When nobody gave a default, propose the most prudent answer, marked `[proposed]`: the one that takes no risk the decider has not accepted ("Can a seller hand over gear that is not fully ticked? With no written answer: no"). It stays a proposal until the trio accepts it. "As today" is not prudent by itself: today's habit may be the risk the subject exists to remove.
- **Signatures are comments, written by the person themself**: `Bet signed · role · id`. Same format for the verdict and the freeze. You prepare the table; you never write a signature.
- **The requester explains and does not sign**, unless they are one of the trio.
- **No breakdown into screens.** The designer owns it.
- **No acceptance criteria.** The success criterion stays; acceptance criteria go to the implementation tickets.
- **A threshold is written before the freeze**, or it is `[to provide]`. "To set in the session" passes nothing: a threshold chosen after seeing the result is not a threshold.
- **The threshold is the decider's, not the requester's.** When they are two people, ask it with the question for the decider, in the watch-outs. A number the requester proposed is its default; with none, the default is `[to provide]` and the bet waits for it.
- **A bet that no result can contradict is not a bet.** Its "then" is the first row of the thirty-day table.
- **Someone outside the trio must say yes** (personal data, money, another team): it is a row of the watch-outs, with their name and the date asked. A legal answer sends the subject to the full form.
- **"Not in this request" is a scope line, not a slot to propose.** List only what the material leaves out, with its source. When it leaves out nothing, write `[to provide]` and ask the requester; never draw the boundary yourself.
- **Two rows of the watch-outs are optional**: "The right word" and "A rule that is coming". Keep them when the material gives one. When it gives none, remove the row: `[to provide]` there would ask someone to invent a word or a rule.

## 12 · Several briefs on one subject

A large subject becomes one brief for the vision and one per screen or flow.

- The vision freezes first. The screen briefs depend on it.
- Dependencies are written in prose in each brief, so they survive a copy.
- **A screen brief does not update itself.** When the vision changes, reread each child for the changed word. This gap is invisible when you reread one brief alone. Two checks pay for themselves: follow one word across all the briefs, and compare ticked answers with text written earlier.
- Quote questions by brief and identifier: "T2 of the vision brief".

## 13 · Title, notes and terms

**Title.** A verb and an object: "Reschedule a lesson", not "Lesson management". The rule bends when a noun names the right actor better; what matters is that the title cannot be read two ways. The full form carries a prefix so that briefs can be told from other tickets: `[Brief] — Reschedule a lesson` in English, `[BC] — Reporter un cours` in French, or the tag the team already uses. The short form has no prefix: it is the ticket of the week itself.

**Notes and sources** is the only section, with answers to questions, that may change after the freeze. It holds:

- Sources, one line each: what the source says.
- Reasons, options that were dropped, numbers that were quoted.
- **Binding terms**: the words the team commits to, with one meaning each.
- **Terms heard**: words used in the session that are not defined yet. A dated list, no definition. They are heard for the first time in this room; noting them stops the glossary from running months late.
- The trace of a renumbering or a reassigned identifier, if one could not be avoided.

Watch pairs of near-synonyms that are not the same thing ("without creating an account" is not "without an account"). When two words compete, pick one and write it in the binding terms.

## 14 · Rendering traps

Most trackers and docs tools render Markdown with small differences. These cost a session when they fail on screen:

- **A box is tickable only at the start of a list line**: `- [ ] text`. Inside a table or in the middle of a paragraph it is plain text.
- **No italic glued to bold.** `»* **The` merges into a broken run of asterisks in several editors. Put a dash or a line break between them.
- **A mention written as plain `@name` may notify the person** when pasted. In a template, write names in `code`. In a real question, mention on purpose.
- **Mermaid** renders in most tools. If theirs does not, replace the diagram with a five-line list using arrows.
- Keep one blank line before and after a list of boxes; some editors attach it to the previous paragraph otherwise.

## 15 · The before / after diagram of the executive summary

The summary carries one picture, right under the message: what people do today, and what they will do. A decider reads it before any line of text, so it must say the why on its own.

```
TODAY  ┄┄▸ step ┄┄▸ step ┄┄▸ step ┄┄▸ (the cost)
AFTER  ━━▸ step ━━▸ step ━━▸ step ━━▸ (the gain)
```

**Where each box comes from.** Nothing in the picture is new:

| Box | Taken from the brief |
| --- | --- |
| TODAY, the steps | The Today line of the context (the principle's Today in the short form) |
| TODAY, the last box | The cost the proof counts: "61 calls a month", "3 customers waiting" |
| AFTER, the steps | The path the scope opens, in the order the person lives it |
| AFTER, the last box | What changes for the person: the "So that" line, or what we will count |

When the proof has no number yet, the cost box says what is lost in words ("found by hand"), never a figure you chose.

**Why it is drawn this way.** The two rows must not look alike, in colour and without it: printed in black and white, the dashed grey row and the solid row still differ.

| | TODAY | AFTER |
| --- | --- | --- |
| Label | light pill, grey text | black pill, white text |
| Steps | grey boxes, dashed border, faded text | amber boxes, solid thick border |
| Arrows | dotted `-.->` | thick `==>` |
| Last box | red: the cost | green: the gain |

Copy the block from the template with its `classDef` lines and its spacing line; change only the words.

**What keeps it readable on paper.** Left to right, two rows, three steps per row at most, three or four words per box. Printed on A4, a row of five long boxes shrinks to half size and its text drops under 6 pt; a top-to-bottom diagram fills half the page and pushes the summary onto a second one. The checker warns when the diagram goes vertical, a row grows past three steps or a box past five words.

## 16 · The brief map

The map answers "how many briefs, and what goes in each" when all there is, is an idea. It is one A4 page: the estimate, a diagram of the freeze order, one row per brief, what each must settle, and what stays off the map.

**Finding the outcomes in an idea.** Ask what the person must be able to do, then what that needs. "Know each morning whether the school bus runs" needs to know whether it is running (the operator's disruptions), which bus is the child's (the line and the stop), when it reaches the stop, and a notice that brings them together. Each "needs" that has its own decisions is a brief; one that has none is a scope line of another brief.

**The row of a brief.** A number (0 for the vision), a name of one to three words, the sentence "what changes for the person", the form its size calls for, and when it freezes. No rule, no scope line, no screen: those belong to the brief itself.

**The freeze order.** The vision first. Then whatever the others depend on. Briefs that depend on nothing but the vision freeze side by side. The brief that brings the others together freezes last, and the diagram shows it with a dashed outline.

**What comes from you, not from the person.** A map from one sentence leans on general knowledge: how the domain is regulated, which official data exists, which categories apply. Write none of it as a fact. "Does the operator share where the bus is?" is a question for the room; "the operator publishes live positions" is a claim you have not checked. Name the owner who will answer: an authority, a data provider, legal, the owner of personal data.

**Size of the map.** Seven briefs at most; past that, map the first release, or group briefs by outcome. About 330 words, as the checker counts them: French takes more room than English, and a map of 357 French words already spills onto a second page.

