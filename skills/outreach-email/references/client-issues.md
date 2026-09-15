# Client issues

Emails to clients or customers when something went wrong: an outage, a missed deadline, a billing error, a bad delivery, an employee's mistake, a data or security incident. Also the updates and resolution notes that follow. The goal is to keep the client's trust by being specific, accountable, and reliable about what happens next.

Register: calm, direct, and human, in the user's voice but steadier. No jokes, no `->` asides, no lowercase `hey`. Warm but not effusive. Never defensive.

This is not legal advice. When money, contracts, or data are involved, the draft is a starting point for the user and whoever approves it.

---

## Gather the facts first

Don't draft until you know these, or have marked what's unknown. Ask in one message:

- **What happened**, in plain terms, and what the client actually experienced.
- **Scope:** which clients, systems, orders, or data; whether any data was lost or exposed.
- **Timeline:** when it started, when it was noticed, whether it's resolved (with time zone).
- **Cause:** confirmed, or still being investigated.
- **Fix:** what's been done, and what will change so it doesn't recur.
- **What the client needs to do**, if anything.
- **Who owns it:** one named contact.
- **What's already been said or promised**, to whom, and where.
- **What's approved:** credits, refunds, dates, wording. **Is legal or security involved?**

Anything unknown stays unknown in the email ("we're still confirming the cause"), never a guess. **Don't pass along an unconfirmed theory either**, even hedged ("the leading theory is a token issue"): the client hears it as the cause, and if it changes, the second explanation reads as a cover story. Keep theories internal until confirmed.

**Get the direction of the failure exactly right.** Before drafting, restate the incident to yourself in one plain sentence from the client's side and check it against the user's words: closed vs. open, overcharged vs. undercharged, sent vs. not sent, early vs. late. Users describe incidents in shorthand ("techs showed up to jobs that were already closed"), and inverting it in the email ("jobs marked closed that weren't") tells the client you don't understand what happened. If the shorthand is ambiguous, ask.

## Structure

What makes an apology work, in order of how much it matters: **taking responsibility**, then **offering a fix**, then explaining what happened and expressing regret. Asking for forgiveness matters least; skip it.

1. **Say what happened and own it, in the first two sentences.** Specific failure, specific impact, "that's on us," "I'm sorry." Active voice: "we deployed a bad config," never "mistakes were made."
2. **Where things stand:** fixed or still in progress.
3. **Why, in a sentence**, if confirmed. Otherwise say it's still being confirmed and when they'll hear.
4. **What they need to do**, or "nothing on your end."
5. **What's changing:** one or two specific steps, not a promise that it can never happen again.
6. **Making it right**, only if approved.
7. **Next update by [day/time, time zone]**, and a direct way to reach a named person.

**Subject lines are descriptive.** The client should know what this is before opening: `[Issue] affecting your [orders/system] on [date]`, `Update: [issue], resolved`.

## Language

| Instead of | Write |
|---|---|
| We apologize for any inconvenience | We're sorry we delayed your payroll run on Tuesday. |
| Mistakes were made / an error occurred | We sent the wrong file. / We deployed a change that broke checkout. |
| We're sorry if you were affected / sorry if you feel that way | You're right, we should have told you sooner. |
| Due to an issue with our vendor... | This is still our responsibility. [Vendor detail only if it helps them act.] |
| This will never happen again | We've added [check] so this is caught before it reaches you. |
| One of our team members made an error | Our process let [the mistake] through; we've added [review step]. |
| We take this very seriously | [Show it: the specific fix, the named owner, the update time.] |
| We're working hard to resolve this ASAP | Our team is working on [specific thing]. Next update by 3pm ET. |

Once confirmed, rule out the worst fear plainly: "No data was lost." "This was not caused by an attack." Only when confirmed.

Blameless toward individuals: name the process gap, not the person. Never throw an employee or vendor under the bus in a client email.

## Liability lines to hold

Own the event and the fix; leave legal conclusions to people authorized to make them.

- **Say:** "we caused," "that's on us," "we're sorry," "we should have caught this."
- **Don't say:** "negligent," "breach of contract," "liable," "we'll cover all your losses," or anything that characterizes legal responsibility.
- **Don't promise** credits, refunds, SLA remedies, dollar amounts, or dates unless the user confirms they're approved. Put them in a `[slot]` and flag it.
- Apology laws mostly protect sympathy in medical settings; don't assume they cover business emails.

**Security or data incidents: stop and flag.** Tell the user to involve legal counsel and their security lead before sending, because notification laws can start a clock at discovery (GDPR: 72 hours to the regulator). Say "security incident" rather than "breach" until counsel confirms, don't speculate about cause or scope, and do tell affected people what data was involved and what they should do to protect themselves. Draft, but mark the draft as needing legal review in the note after it.

## Timing

- **First notice fast**, even with little information: what's affected, that the user is on it, when the next update comes. Silence reads as hiding.
- **Updates at the promised time even when nothing's new.** "Still working on it; next update at 4pm" keeps trust; a missed update loses it.
- **Resolution note** when it's fixed: what happened, what was affected (including whether data was lost), what's changing.
- **Written follow-up** for serious incidents within days to two weeks: timeline, cause, prevention steps.
- **Don't send broad apologies for problems clients didn't notice and weren't affected by.** It draws attention to the failure and can lower trust. Fix it and document it internally.

## By audience

**One key client.** A named sender who owns the relationship (account manager, or exec to exec when the harm is serious). Their specific impact, not a generic notice. For anything serious, the user should call first; the email is the written recap: "Following up on our call, here's what happened and what we're doing."

**Many customers.** One accountable voice (a founder or leader for big incidents), plain language, and the four blocks clients scan for: what happened, what we did, what you need to do, what's next. Bold labels are fine here; it's a notice, not a personal note.

**Making it right.** The apology does more than compensation; people forgive a sincere apology more readily than a payment. If a credit is approved, state it simply as a goodwill gesture: "We've applied a credit of [amount] to your next invoice." Don't lead with it and don't use it to replace the apology.

## Skeletons

**Single key client**

> Subject: [Issue] affecting your [system/order] on [date]
>
> Hi [Name],
>
> I wanted to tell you directly: on [date] we [specific failure], which meant [their concrete impact]. That's on us, and I'm sorry.
>
> Where things stand: [fixed at time / still working on it]. [Cause in one sentence, or: we're still confirming the cause and I'll tell you as soon as we know.] [Anything they need to do, or: nothing is needed on your end.]
>
> What we're changing: [one or two specific steps].
>
> [Only if approved: We've applied [credit] to your account.]
>
> I'll send an update by [day, time, time zone]. You can reach me directly at [phone].
>
> [Name]
> [Title]

**Broad customer notice**

> Subject: [Service] disruption on [date]: resolved
>
> Between [start] and [end, time zone], [what customers couldn't do]. [If confirmed: No data was lost.] We're sorry. You rely on us for [X], and we let you down.
>
> **What happened:** [plain cause, or: still under investigation]
> **What we did:** [fix]
> **What you need to do:** [steps, or: nothing]
> **What's next:** [prevention steps; full write-up by date]
>
> Questions: [contact]. [Status page URL, if any.]
>
> [Named leader, title]

## Output note

One strong draft usually beats three variants here. When variants help, split by *who sends and how much detail*: "Account manager, specific and short" / "Exec to exec, fuller." Always end with a line listing what must be confirmed before sending: cause, credits, dates, and legal or security review when relevant.
