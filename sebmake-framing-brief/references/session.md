# The session, the freeze, and after

How a framing brief is produced with people: before the session, during, at the freeze, and once it is frozen.

## Contents

1. Who is in the room
2. Before the session
3. The agenda — full form, two hours
4. The agenda — short form, one hour
5. Running it
6. The freeze
7. When a confirmation is refused
8. After the freeze
9. The gap report
10. Knowing whether it works

---

## 1 · Who is in the room

Four voices and a facilitator. Teams name them differently; map their people to these.

| Voice | Brings | Says at the freeze |
| --- | --- | --- |
| **Decider** — sponsor, head of product, client | The why and the scope | "The problem and the scope are the ones I want" |
| **Product** — writes the spec that follows | Strategy, data, first elements | "I can write the spec" |
| **Design** | The experience | "I can start the design" |
| **Engineering** | Feasibility, the only authority on it | "No major obstacle in here" |
| **Facilitator** | Nothing: runs the agenda, holds the keyboard | Does not confirm |

- **Whoever presents does not facilitate.** A person defending their paper cannot also guarantee the agenda was covered.
- One person can hold two voices. They say both sentences.
- A missing voice is written in the brief: "No designer on this subject; the design sentence is not said." Never dropped silently.
- **Without the decider, the brief cannot freeze.** Say it when the session is scheduled, not when it ends.

What each one stops doing is the real argument for the session. The decider stops arbitrating by message, on demand. Product stops writing a paper nobody reread. Design stops filling in a section after a breakdown decided without it. Engineering stops receiving work built on a framing it never saw.

## 2 · Before the session

**Pre-filling is not optional.** With an empty page, the hour goes into typing. With a brief pre-filled and marked `[proposed]`, it goes into deciding.

1. Look for an existing brief on the subject (step 1 of the skill).
2. Estimate the size (step 3): neither too big nor too small, its executive summary on one A4 page. A subject that needs two briefs needs two sessions; one too small needs none.
3. Pre-fill the brief from the first elements. Assumptions go to questions, never into the body.
4. Send the open questions, one per thread, each to a named person, with an answer asked for before the session. Include anyone outside the room who owns a line: personal data, money, a contract, another team.
5. Send the brief the day before, with its executive summary when one was asked for. The agenda is the brief.
6. If the session is recorded, plan to say so when it opens.

**The risk of pre-filling is anchoring**: the room approves what is on screen. The parade is in the facilitation — open each block with the question, never by reading the screen.

## 3 · The agenda — full form, two hours

A default. Adapt the minutes, keep the order and the last twenty.

| Time | What happens | Block |
| --- | --- | --- |
| 0:00 | The problem and what changes — **said by the decider**, in their words, before anything is presented | Context |
| 0:10 | The author presents the first elements: today, the proof, what we will count | Context |
| 0:25 | In, out, later | 1 · Scope |
| 0:50 | The rules, each with its question | 2 · Rules |
| 1:00 | *First check*: what is still empty or `[proposed]` | — |
| 1:15 | Scenarios, then the principles of each screen | 3 · 4 |
| 1:30 | The date | 6 · Deadline |
| 1:40 | *Second check*, then **reading aloud**, block by block | — |
| 1:55 | **The freeze round** | The freeze |

Two subjects in one morning means two sessions. Never a second subject in the same slot: reading aloud and the freeze are the last minutes, and they are what gets cut when time runs out.

## 4 · The agenda — short form, one hour

| Time | What happens | Block |
| --- | --- | --- |
| 0:00 | The requester explains, with three real cases | — |
| 0:10 | The principle and its proof | 1 |
| 0:20 | The diagram and the rules | 2 · 3 |
| 0:30 | Watch-outs: the right word, what is not in the request | 4 |
| 0:38 | What exists | 5 |
| 0:45 | The success criterion: the three cases, pass and fail | 6 |
| 0:52 | Reading aloud | — |
| 0:57 | **The bet**, signed by each member of the trio | 7 |

The requester explains and leaves the signing to the trio. A question for the decider goes out the same day with its default answer and its deadline.

## 5 · Running it

- **The agenda is the structure of the brief**, never the structure of the author's paper. Otherwise the session inherits the paper's holes without seeing them. The order of the page is what guarantees nothing was skipped.
- **The brief is projected and filled in on screen**, top to bottom. The template and the agenda are the same object. When Claude holds the file with the facilitator, it follows the same order, one block at a time, and runs the checker at the end of each block.
- **The decider says the problem in their own words.** Not the product person on their behalf. If it does not come out, the subject does not freeze: this is the only blocking absence. They speak first, before the draft is read, so they do not adopt its wording.
- **Get the "out" said explicitly.** It is where scope evaporates.
- **Get engineering to speak.** If they said nothing, the technical constraint was not looked for. A constraint is never deduced: unspoken, it does not exist.
- What goes beyond the first elements and that the decider did not settle in the session is not decided in their place, even with them in the room. It leaves as a question, owner: the decider.
- **The check during the session** compares the brief with the template: empty blocks, `[proposed]` lines, questions without options, "out" lines without a destination. It does not compare the brief with what was said.
- **"Said but not written" is caught by reading aloud, and by nothing else.** It is a human check and it cannot be replaced.
- **The last minutes are never shortened.** If time is short, shorten the debate.

## 6 · The freeze

Read the brief aloud, then go round the table: engineering, product, design, and the decider last, so that nobody aligns on the person who decides. Four sentences, each ticked by its owner or written in a comment: `Freeze signed · role · id`. The facilitator does not confirm.

Conditions, checkable in five minutes:

- [ ] The context is filled in, and the why comes from the decider.
- [ ] The proof and the measure are written, or written as missing with who counts them.
- [ ] Every line that commits someone outside the room has their answer, or a question with an owner and a date.
- [ ] If G1 is "reduced", the lines that leave are already in "waits".
- [ ] Every "will not be in it" line names where the thing lives.
- [ ] Every block has content, or a named question.
- [ ] Every decision to make is ticked, or stays open with an owner and a date written under it.
- [ ] No question that decides the why or the scope is still open.
- [ ] Every open question sent to a person has an answer, or a date — "before the next session" when none is fixed.
- [ ] Every scope line traces to a source; none was added by the author alone.
- [ ] No `[proposed]` or `[to provide]` remains.
- [ ] Each of the four lines was ticked by its owner.

`scripts/check_brief.py --freeze` covers the mechanical part.

> **We can freeze with holes. We cannot freeze with a disagreement on the why or the scope.**

**When the freeze is not the normal one** — a voice absent, one person freezing alone to unblock work — write it in the brief, in a visible line, with the reason and what the next session will do: confirm or reopen. An exception stated is a decision; an exception passed over is a hole in the method.

**A verdict before the freeze.** Some teams test the idea with users before freezing: the brief is drafted, a rough prototype is tested, and the freeze follows the verdict. Then the freeze block gains one condition — the verdict is positive, or contradicted and arbitrated in writing by the decider. A negative verdict allows one loop: prototype and brief updated, then a second test. A second no, and the subject leaves.

## 7 · When a confirmation is refused

| What is refused | What happens |
| --- | --- |
| Something is **missing** | It becomes a question with an owner and a date. The brief freezes. |
| A decision that touches **neither the why nor the scope** is not made | It stays open: one line under it names its owner and a date. The brief freezes. |
| A **disagreement** on the why or on the scope | No freeze. The subject comes back to a session. Everything downstream depends on it, and a named hole cannot carry it. |
| Engineering refuses on **feasibility** | No freeze. |
| A question whose answer **overflows the frame** — a new team, a second subject | It is no longer a closing: the subject returns to a session. |
| A scope question **nobody disputes** is still unticked | Not a disagreement: the decider ticks it, and the brief freezes. |
| A **second** session ends without a freeze | The decider writes the outcome: the subject stops, or it splits. No third session on the same page. |

## 8 · After the freeze

The body no longer moves. Two kinds of writing remain allowed, and no other:

1. **The answer to a question**, written on its line and dated, without erasing the wording.
2. **Notes and sources.**

Then:

- Design starts the same day. Discovery is behind.
- Thirty days after release, the count and the verdict go in the notes and sources. Below the threshold, the people who froze it sign again: remove, rework or keep.
- Product writes the spec. The brief is its reference.
- A change after the freeze goes through one channel: a written gap, signed by whoever owns that part. By default an addition waits for the next version.
- If a recording exists, it is the archive and the safety net, not the source. A document frozen at 10:30 cannot derive from files published after 10:30. What the recording holds and the brief does not is **posted as a finding**, not applied; a material gap becomes a question or sends the subject back.

## 9 · The gap report

Once frozen, the brief is the reference the spec is compared with. At each new version of the spec, post a report as a comment:

| Category | Meaning |
| --- | --- |
| **In the brief, absent from the spec** | Scope lost on the way |
| **In the spec, absent from the brief** | Scope added without a decision |
| **Divergent** | Both speak of it and disagree |

- Quote the line of the brief and the place in the spec for each item.
- **The report never writes into the spec.** It is posted; people decide.
- Name who arbitrates each category. Without a name per category the report becomes noise that nobody reads.
- It protects design first: design explores on the strength of the brief, and an unseen drift in the spec costs that exploration.

## 10 · Knowing whether it works

Before the first run, count the product questions raised after design started on the last two subjects: that is the number to beat. Then measure:

- The brief froze in the session, on time.
- **The number of product questions raised after the freeze.** The most telling measure.
- The delay between the freeze and the first screen. Target: the same day.
- The share of closed blocks against named holes. A named hole is not a failure; an unnamed one is.
- How many times a frozen brief was reopened.

**The stop rule.** After three briefs, if the product questions asked after the freeze have not fallen below the number to beat, the brief aligns nobody and costs each person the length of a session. Stop it.
