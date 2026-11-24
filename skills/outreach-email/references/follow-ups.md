# Follow-ups, channels, and replies

Applies to every scenario. Scenario files add their own timing where it differs (interview check-ins in `job-search.md`, investor follow-ups in `investors.md`, internal nudges in `internal.md`, incident update cadence in `client-issues.md`).

Evidence note: timing and length numbers come mostly from sales-email datasets and career advice sites. Treat them as defaults; the user's read of the relationship wins.

---

## Nudges (no reply yet)

**The rule for every nudge:** it brings one new thing and makes sense to someone who never opened the earlier email. A nudge that only says "following up" asks them to go find the first one, which they won't.

New things that count: a recent post, launch, or hire of theirs; something the user built, shipped, or learned since; a sharper or easier version of the ask; a deliverable (a teardown, a sample, an update with real numbers).

Never: "just checking in," "bumping this," "did you see my last email," "I never heard back," a bare "Thoughts?", guilt, or apology for following up. In sales data, "Thoughts?" and "never heard back" both measurably lowered meetings.

Send as a **reply in the same thread** so context travels with it, unless the first email clearly never landed.

### Cadence after cold outreach

| Nudge | When | Shape |
|---|---|---|
| 1 | 3-5 business days after the first | 2-4 sentences, one new angle, same ask or easier |
| 2 | 5-7 business days after nudge 1 | 1-3 sentences; can switch channel |
| Stop | after nudge 2 | Silence is an answer. |

Nudge 1 is where most follow-up replies come from; give it real effort. A "closing the loop" last note is optional: say it's the last one, give an easy out, leave the door open, and then don't contact them again about this. Long persistence (the eighth email that finally got a reply) only works when every email adds weight and the relationship is still plausible; don't recommend it by default.

A reply isn't the only payoff. A short, no-pressure cold email with one small, specific offer can go unanswered and still make the next meeting warm ("you're the one who emailed"). Write every cold email so the user would be glad to be remembered for it, which means no guilt in the nudges either.

## Replying when they do respond

Reply fast and short. Match their length; a two-line reply gets a three-line answer. If they asked anything ("how'd you come across it?"), answer it in the first line; skipping it is the most common miss. Then respond to what they said with one real thing from the user's experience.

**Turning a door-opener into the ask.** Don't ask in the first reply unless they invite it ("what are you working on?", "are you looking?"). Ask on the second or third exchange, or sooner if they're warm, and build it off the conversation: "your point about product backgrounds is part of why I'm asking: I'm a PM looking at teams like yours, is there a role or a person worth talking to?"

**Once a conversation is live, get specific.** Cold emails do better asking about interest; active threads do better proposing concrete times. Offer two or three, or accept theirs. If they offer to meet somewhere, say yes if the user honestly can.

**Close the loop after they help.** Same-day thanks. A week or two later, something useful with "no need to reply" (an article that connects to what they said). A few weeks after that, what the user did with their advice and how it went. This is how one reply becomes a relationship.

## LinkedIn

| Format | Hard limit | Aim for |
|---|---|---|
| Connection request note | 300 chars (some free accounts see 200) | under 250 |
| InMail | 200-char subject, 1,900-char body | under 400 chars |
| DM to an existing connection | 8,000 chars | email length or shorter |

A connection note is the email's hook and ask with everything else removed: one true specific about them, one clause about the user, a reason to accept. No credential paragraph, no link. Count characters (`scripts/lint_email.py --max-chars 300` when code execution is available) and report the count with the draft. Free accounts get only a handful of personalized notes a month, so each should be the strongest angle.

A second channel alongside email (commenting thoughtfully on their post, a short DM) can help a high-stakes cold email get noticed. Once, not a campaign.

## Asking a contact for an intro

Write two things:

1. **The ask to the connector.** Short, names the person specifically and why, acknowledges they're spending social capital, gives an easy out: "totally fine if it's not a fit to intro." Moderately close contacts (people the user knows but doesn't talk to often) are often the most useful connectors, more than best friends.
2. **A forwardable blurb** they can paste without editing: one line on who the user is, the specific reason for this recipient, a bounded ask (15-20 minutes, or "who's the right person for X"), and contact info. Written so it works forwarded.

For investors, see the double opt-in note in `investors.md`.

---

## Networking intros (someone connects you to a person)

For intros that open a door (a coffee, an industry conversation, a possible opportunity), not investor intros, which follow `investors.md`.

Two short messages, same day (see the networking intro exchanges in `examples.md`):

1. **Reply on the intro thread.** Thank the connector by name, a line to the new person, and say you'll reach out separately. That moves the connector out of the scheduling.
2. **Message the new person directly.** Who you are in a clause (including the name you go by, if the connector used a different one), thanks for the time, defer to their location and schedule, and one open question ("how does your schedule look next week?").

When they offer options, pick one in a line and confirm the one missing detail (the exact place).

**When the user has to offer times, offer the times that work best, not every time they're free.** Two or three tight windows, with a line that they'll work around the other person's schedule if none fit. Never explain why those are the windows (work hours, days off, what they do the rest of the week). That isn't dishonest, it's not oversharing, and a first impression should read as someone with a full calendar who's making room.

> Weak: I work Tuesday-Thursday 9am-6pm, so I can do a call after work or on my lunch break. Otherwise I can meet in person Monday or Friday.
>
> Better: I'm free Tuesday or Wednesday 12-1, or Friday morning for coffee. If none of those work, happy to work around your schedule.

Match the channel they were intro'd on: a text intro gets texts, not an email.
