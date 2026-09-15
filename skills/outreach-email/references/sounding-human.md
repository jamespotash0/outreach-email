# Sounding human

The reason this matters more here than almost anywhere else: a hiring manager, investor, client, or colleague who suspects an email was AI-generated stops reading and discounts everything in it, including the true parts. The cost isn't stylistic, it's that the email stops working. And the tells below are now widely recognized — they've been catalogued publicly, they get shared around, and people spot them fast.

The good news is that the example emails already avoid nearly all of this. The risk isn't the user's writing drifting toward AI patterns; it's a draft importing them from the outside. Read the examples for rhythm, and check the draft against the list below before handing it over.

---

## The constructions to strip

**"Not X, but Y" / "It's not A, it's B" / "not just X, but also Y."** The most recognizable tell there is. It reads as a rhetorical flourish that sounds insightful without adding information.

> The ceiling isn't model quality, it's whether someone will put their name on the answer.

Just say the second half: *the hard part is getting someone to put their name on the answer.*

**Rule of three.** Three adjectives, three parallel clauses, three examples where two would do. Count the items in any list before shipping. If the source detail had two things in it, keep two.

> paperwork nobody has time for, missed calls, installers driving all over the place

The original observation had two items. The third was invented for cadence.

**Participle tails.** A sentence that ends with `-ing` doing commentary on itself: *underscoring the importance of*, *highlighting how*, *reflecting a broader shift*, *emphasizing their commitment to*, *showcasing*, *demonstrating*. These sound like analysis but assert nothing checkable. Cut the tail, or make it a real sentence with a subject.

**Copula avoidance.** *serves as*, *stands as*, *represents*, *marks a*, *functions as*, *boasts*, *features* where *is* or *has* would do. "Karat is solving X" beats "Karat represents a shift toward X."

**Grand significance.** *a pivotal moment*, *a testament to*, *speaks to a broader*, *the evolving landscape of*, *a key turning point*. Nobody writes this in an email to a person they met yesterday.

**Vague authority.** *many teams struggle with*, *industry observers note*, *it's widely understood that*. In a cold email this is filler standing where a specific observation should be.

**Chatbot residue.** *I hope this finds you well*, *I hope you're doing well*, *hope things have been good on your end*, *I hope this helps*, *let me know if you'd like*, *happy to help*, *don't hesitate to reach out*. These are the assistant's own habits leaking into the user's email. Start with the actual first thing.

**Staged run-ups and signposting.** *I wanted to reach out because*, *quick question:*, *I'll keep this brief*, *the reason I'm writing is*. Announcing the sentence instead of writing it.

**Pre-empting objections nobody raised.** *I know you're busy, but*, *I know this is out of the blue*. One acknowledgement of how slammed they are can work when it sets up an easier ask (see the coin email); a run-up that apologizes for the email existing doesn't.

**Stacked hedges.** *just*, *perhaps*, *might possibly*, *I think maybe*. One is human. Three in a paragraph reads as nervous or generated.

**Same opener, sentence after sentence.** I... I... I.... Vary it, often by starting with the thing about them.

**The dramatic one-line closer.** A short standalone sentence meant to land like a mic drop (*That's the future I want to build.*). Nobody writes these to someone they met yesterday.

**Leftovers.** Unfilled `[placeholders]`, a `Subject:` line inside the body, "here's a revised version," knowledge-cutoff hedges (*as of my last update*). Any one of these tells the recipient exactly how the email was made.

## Vocabulary that reads as machine-written

crucial, pivotal, robust, leverage, delve, underscore, showcase, tapestry, testament, landscape (figurative), intricate, meticulous, garner, foster, bolster, align with, resonate with, seamless, holistic, comprehensive, unlock, empower, elevate, transformative, game-changing, at the intersection of, deeply, truly, that said, vibrant, thrilled, passionate.

Two notes on this list. *Resonated with me* appears in the weakest email in the examples, which is not a coincidence. And *align with* has a specific failure mode in job emails (and its cousins in pitches: "aligns with your thesis"): "my experience aligns well with the role" is the exact sentence a recruiter has read four hundred times this month.

## Punctuation

**Em dashes: one per email at most, and prefer zero.** The example emails reach for parentheses, colons, semicolons, commas, and `->` instead. Spaced em dashes stacked two and three to a paragraph are a strong tell, and this is the pattern most likely to leak in from the drafting side rather than from the user's own voice.

**Straight apostrophes and quotes**, not curly. `don't`, not `don’t`.

**No bold, no headers, no horizontal rules** in an email body. The one exception is the short bulleted background block in a warm-intro email, which works because the reader is scanning to decide whether to forward.

**Exclamation points:** the examples use them, roughly one per email, usually on congratulations or the sign-off. More than that reads as performed enthusiasm.

## The review pass

Run this on every draft before handing it over:

1. **Mechanical check.** If you can run code, run `python3 scripts/lint_email.py` on the draft (subject on the first line as `Subject: ...`). It catches em dashes, curly quotes, stock phrases, listed vocabulary, placeholders, and Title Case subjects. A flag is a prompt to look, not an automatic rewrite: a flagged word inside a real quote from the recipient can stay. If you can't run code, do the same check by eye against this file.
2. **Trace every claim.** For each fact about the user (dates, durations, who, numbers, origins), point to the line in `background.md` or the message it came from. For each fact about the recipient, point to the user's message or a source you looked at. Anything without a source gets cut, softened to what the source says, or turned into a `[slot]`. Durations, origin stories, and *how-and-why glue* are where drift happens most: "the last year" when the file says four months, or "mostly by cutting queues like that" attached to a result whose method the file never states. A clause explaining how or why the user achieved something needs a source like any number does.
3. **Mark the tells** the script can't see: rule of three, participle tails, grand significance, the dramatic closer, prose smoother than anything in `examples.md`.
4. **Rewrite without changing a claim.** Every fact in stays in; nothing new gets added. Fixing a tell is never an excuse to invent a detail.
5. **Read it aloud** (in your head). If a sentence would sound odd said to the person's face, rewrite it the way you'd say it.

## What human writing looks like here

Read the example emails and notice the texture that no template produces: a semicolon splicing two thoughts that should be separate sentences, a sentence starting with "Likewise," a comma splice in "congrats on the raise, that's huge!", lowercase "hey," the parenthetical credential dropped mid-thought, "which got me as I have been collecting coins since I was about 15."

Some of that is technically imperfect. Leave it imperfect. Polishing those edges is exactly what makes a draft read as generated, because the smoothing-out is the signature. If a sentence in a draft is more grammatically tidy than anything in the examples, it's probably wrong.

The deeper version of this: AI writing gets caught because it's generic dressed up as significant. It says a lot of impressive-sounding things that would be equally true of any subject. Every fix in this file is downstream of the specificity test in SKILL.md — a sentence carrying a real, checkable, particular detail almost never trips these patterns, because it's too busy saying something.
