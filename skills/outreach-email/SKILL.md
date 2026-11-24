---
name: outreach-email
description: Writes the user's emails and messages in their own voice when a specific person needs to read it and act. Covers cold and warm outreach (founders, execs, hiring managers, recruiters, investors, potential partners, anyone worth meeting), job-search emails (interview thank-yous, check-ins, rejection replies), pitching VCs and angels and investor follow-ups, internal company emails (asks, updates, replies, nudges, escalations), and client emails when something went wrong (outages, missed deadlines, billing or delivery mistakes). Use whenever the user wants to email, message, reach out to, follow up with, reply to, pitch, thank, or apologize to someone, or asks for a subject line or LinkedIn note, even if they never say "email", as in "what should I send Sarah after that call", "want to reach out to the Acme founder", "need to tell the client about the outage", "it's been two weeks, nothing".
argument-hint: "[angles | cold | critique | follow-up | learn | setup] [who or what]"
license: MIT
compatibility: Works in any Agent Skills-compatible agent (Claude Code, Claude.ai, ChatGPT, Codex, Cursor, Gemini CLI, Grok Build, Hermes, Copilot, Perplexity, and others). No tools required; uses web search and Python 3 when available.
metadata:
  version: "3.1"
---

# Outreach email

One voice, many situations. Every email this skill writes has a specific reader who owes the user nothing, and it has to earn that person's attention and a response.

## Commands

Most requests come in plain words ("email the Jerry founder") and need no command: follow the rest of this file. When the user names one, route it:

| Command | What it does | Follow |
|---|---|---|
| *(none, invoked bare)* | Show this table as a short menu and ask what they need. Never auto-run a command. | |
| `angles [who]` | Research and angle-hunting, then the hook sheet and questions. No draft. | `references/commands.md#angles` |
| `cold [who]` | The full flow: angles, the user's answers, drafts, recipient critic. Uses team mode when available. | This file, from "Find the connection" |
| `critique` | Reads a pasted email as the recipient would, runs the checker, returns fixes and one revised version. | `references/commands.md#critique` |
| `follow-up` | A nudge or follow-up on an existing thread; push toward sending something made, not a bump. | `references/follow-ups.md` |
| `learn` | Turns a shared email (and its outcome) into lessons folded into this skill's files. Not templates. | `references/commands.md#learn` |
| `setup` | Fill in or update `background.md`. | "First-run setup" below |

## Pick the scenario

Read the matching file before drafting. If the request spans two (a client apology that also asks for a renewal), read both; if it's unclear which applies, the recipient decides it.

| Scenario | Examples | Read | Register |
|---|---|---|---|
| **Job search** | Thank-you after an interview, cold email to a hiring manager, recruiter follow-up, ghosted check-in, rejection reply | `references/job-search.md` | The user's own voice (`examples.md`) |
| **Investors** | Cold email to a VC or angel, warm intro blurb, post-pitch follow-up, investor update, replying to a pass | `references/investors.md` | Direct, numbers-forward, still human |
| **Internal** | Cross-team ask, email to an exec, status update, reply when you don't know yet, nudge, escalation, pushback | `references/internal.md` | Clear and warm; ask first |
| **Client issues** | Outage, missed deadline, billing error, bad delivery, data or security incident | `references/client-issues.md` | Calm, accountable, specific; never casual |
| **General outreach** | Networking, replying to a networking intro, asking an expert a question, partnership, podcast or speaking ask, customer discovery | Nothing extra: this file is enough | The user's own voice |

Also read `references/follow-ups.md` for any nudge, reply to a response, LinkedIn message, intro request, or networking intro someone made for the user.

## The theory

For anything cold, and most of the rest:

- **Personalized.** About *them*: something they wrote, built, said, decided, or care about.
- **Brief.** As short as the job allows. Busy people answer what they can answer in a minute.
- **No work to respond.** They can read it once and reply from what they already know: no looking anything up, no planning a meeting, no writing more than a line or two. "Who on your team handles portfolio hiring?" can be answered in seconds. "Any thoughts on how I should approach this?" asks them to sit down and think, so it waits, then gets forgotten.
- **A real connection inside.** Their true thing linked to the user's true thing, or a genuine question about their thinking.
- **A subject that makes them want to open it.** Nothing else matters if it stays unopened.
- **Differentiated.** They get a pile of these. Only this sender could have written this one; that's what earns an answer.
- **Bold and human.** Write like a confident person, not a careful applicant. Use a little play (turn their own phrase around), make a claim the user will stand behind ("hand me your hardest, messiest problem"), and aim at *their* goal in their terms ("help get Jerry to 50m users"). A safe, hedged email reads like everyone else's. Bold doesn't mean inflated: every claim still has to be true of the user.
- **A give, not just a take.** A conversation between equals, not a request for charity: lead with something useful to them (an observation, a pattern the user has seen, a small piece of work) and keep the ask tiny and sized ("15 minutes," not "a call to explore").

All of it rests on one test: **could this sentence be sent to a different person or company without changing a word?** If yes, it's filler, and filler is what makes an email feel like a template. When the input only supports filler, go back and ask for a sharper detail rather than shipping the vague version.

> What you shared about the culture, being very team-oriented, really resonated with me.

> I was especially excited to hear how heavily the team leans on [two named tools] in their daily workflow.

The first is polite noise. The second could only come from someone who was in that conversation.

## Before drafting

Paths are relative to this skill's folder. Read every time:

- **`background.md`**: look first at `~/.outreach-email/background.md` (outside the skill folder, so updates never wipe it), then at `references/background.md` in this skill's folder. Use the first one that exists. It's the user's asset pool (who they are, their role and company, their venture if they have one, what they've built, personal threads). A menu, not a résumé: pull the one or two items that connect to this reader. **If the file doesn't exist, still contains `TODO` or `TEMPLATE` markers, or the sections this scenario needs are empty or `[bracketed]`, do the first-run setup below first.** It's personal and kept out of version control, so a fresh install won't have one; `references/background.template.md` has the structure. Never take the user's name from anywhere else (git config, OS account, email address); if it isn't in the file or conversation, sign as `[your name]`. If a `background.example.md` exists, it shows a finished file; never pull details from it.
- **`references/examples.md`**: real emails the user sent, annotated. The voice lives in these. **Examples show moves, not lines:** openers, closers, and connective phrases can be reused; the recall and bridge (the middle) never can.
- **`references/sounding-human.md`**: what makes writing read as machine-generated, and the review pass every draft goes through. A reader who suspects generated text discounts everything in it, including the true parts.
- **The scenario file** from the table above.

When a choice isn't settled by these (which framework, how long, when to send, what kind of ask), or the user asks what works and why, consult `references/perspectives.md`: practitioner and data-backed views, including ones that disagree, with guidance on picking between them.

## First-run setup

When `background.md` lacks what this scenario needs, don't draft. Say the skill needs to know the user first and it takes a few minutes. Ask only for the sections this scenario uses, a few questions at a time, in prose:

- **Always:** name for sign-offs; the one-line credential they'd use to situate themselves.
- **Job search and general outreach:** most recent role (what the company does, who it sold to, what they owned, outcomes with numbers) and earlier roles in a line each; two or three things they've built, each with *why it exists* (push past "for my portfolio"); personal threads with one concrete proof each.
- **Investors:** the company in one sentence, stage, traction with real numbers, the raise (amount, instrument, who's in), team background, why now.
- **Internal and client issues:** their role, team, company, who they report to, and the clients or teams they deal with most.

If they paste a résumé, LinkedIn, or deck, start from it and ask only about what it lacks. Then write the completed sections into `~/.outreach-email/background.md` (or, if you can't write there, `references/background.md` in this skill's folder), following `background.template.md`'s structure and its *Reach for this when:* pattern (save it yourself if you can write files; otherwise hand it over), and use it for the session. Whether a partial fill is enough is their call.

## Intake

**Never invent.** Not about the recipient, the company, the conversation, or the incident. A fabricated "I loved what you said about X" costs the user the relationship; a fabricated cause or timeline in a client email can cost the account.

**The same goes for the user.** Every fact about them (dates, durations, origins, who a project was for, numbers, traction) must be in `background.md` or the conversation as written. No plausible embellishments ("this year," "for most of my childhood," "growing fast"). If a line needs a detail you don't have, use a slot or rephrase so it doesn't need one.

**Recipient facts** (names, titles, raises, posts, hobbies) come from the user or a source you looked at this session, never from memory stated as current.

When context is thin, ask before drafting: in prose, four questions max, skipping anything already given. The scenario file says what matters most.

**If they say not to ask or signal they're rushed** ("just write it", "quick pls"), draft anyway. Put each missing specific in a `[bracketed slot]` saying what belongs there, never fill it with something plausible, and list the slots in one line after the drafts. Two honest slots beat an invented detail.

## Find the connection (cold and warm external outreach)

**There's no formula.** The examples and moves in this skill show range, not steps. Your job is to find the creative angle for *this* person: the thing that makes them open it, smile, and want to reply. Usually it's hiding in their own words or the user's history, and it comes from digging and asking, not from filling in a template. If two drafts for different recipients could share a structure sentence for sentence, the angle hasn't been found yet.

For any email to someone outside the user's company who doesn't already know them (job, investor, partner, networking), read `references/finding-the-connection.md` and act as the user's research partner, not just their typist:

1. **Research the recipient** if you have web search: personal site, writing, podcasts, talks, side projects, company news, portfolio or thesis for investors, career overlaps with the user. Without web access, name the two or three places most worth checking and ask the user to paste what they find.
2. **Show a short hook sheet**: strongest findings with source and date, each matched to something in `background.md` or marked "no match yet."
3. **Ask for the matching half**: something similar they've done or built; common ground (school, city, company, people, hobby); a real way to add value (an honest product observation, a small teardown or mock, a useful intro).
4. **Then pick the play and draft**, leading with the hook that has a genuine match on the user's side.

A user who already gave a strong hook, or said not to ask, skips the questions: draft from the top hook and show the hook sheet after the drafts.

### Team mode (optional: only if you can spawn subagents)

For a cold email that matters (a target company, an investor, a senior person), and only if your environment can run subagents in parallel (for example Claude Code's Agent tool), split the work. Don't use it for nudges, thank-yous, texts, internal, or client emails, or when the user is rushed. Without subagents, do the same steps yourself in sequence.

1. **Research, in parallel.** Two or three agents, each with one source area from `finding-the-connection.md` (their writing and posts; podcasts, talks, and interviews; company news and product). Each returns at most five findings with source, date, and their exact words where possible. Each must verify the person and never guess.
2. **Angles, in parallel.** One `agents/angle-finder.md` agent per lens (their own words, shared history, the give, the bold claim), each given the findings, the relevant `background.md` facts, and the user's goal. They work separately, so they don't all settle on the same safe idea.
3. **You pick and ask.** Merge into the hook sheet, choose the two or three strongest angles, and ask the user only what those angles need. This step stays with you; the user's half can't be researched.
4. **Draft** the variants, one per angle.
5. **Recipient critic.** One fresh `agents/recipient-critic.md` agent gets only the drafts and a line on the recipient, not your reasoning. Fix what's real, then run the review pass in `sounding-human.md`.

In Claude Code these agents are registered as `outreach-angle-finder` and `outreach-recipient-critic`. Elsewhere, give a general subagent the file's contents as its instructions, or with no subagents, follow the file yourself.

Tell the user in one line that you're using team mode and roughly how long it'll take.

## Pick the play and the length

**The play.** Every outreach email is one of two:

- **Door-opener:** get a conversation, ask later. No ask in the email; the goal is a reply. Engage with their idea, ask one question only they can answer.
- **Direct ask:** interest stated, ask made (a referral, a meeting, a look at the deck, a decision).

Direct ask when there's a clear, timely reason (an open role, a raise in progress, a warm intro, an obvious match, a deadline). Door-opener when the recipient publishes ideas, there's no open door yet, they're heavily pitched with no warm path, or the match needs a conversation to become visible. The user's stated goal overrides. When signals split, make one variant the other play, labeled. Internal and client-issue emails are always direct: the reader needs to know what's being asked of them. Scenario files have their own signals.

**The length** is set by what the email has to carry, not a target. List the jobs it has (hook, bridge, credential, proof, update, ask), give each one or two sentences, stop.

| Go shorter (about 50-100 words) | Go longer (about 150-300 words) |
|---|---|
| Heavily pitched or very senior reader; one hook and one ask is enough | A warm intro: they agreed to hear the user out |
| Someone in a hot moment (just raised, just launched, mid-crisis) | A track record or traction the ask depends on |
| The hook is strong enough to stand alone | A door-opener engaging a substantive argument of theirs |
| Nudges, LinkedIn, anything read on a phone in passing | A client incident that needs impact, cause, fix, and next update |
| The reader writes in one-liners | A decision memo or update the reader will act on |

Every paragraph has one job (if deleting it loses nothing, delete it), and the ask is visible on a phone without much scrolling. Longer never means more questions.

## Subject line

For outreach, the subject has one job: earn the open. Short (two to six words), concrete, usually lowercase, naming the hook: `coin collector + tech`, `saw your projects page`, `loved your piece on duo PMs`, `following up on [name]'s intro`, `been in your content orbit`, or their own words quoted back (`a friend in your pocket`, a line the founder once used for their product). It reads like a note from someone who already knows them and opens a small loop the body closes.

The failure mode describes the *email* instead of the *connection*: "Introduction," "Quick question," "Exploring opportunities at [Company]," `[Company] x [Name]`, a bare `Loved your post!`, Title Case, a mechanically inserted first name. People who get pitched recognize a template subject instantly.

Tests: could it plausibly be from someone they know? Does it name something true about *them*? Would it work if the email had no ask? Does it promise value or state a benefit? (rewrite it).

**Exceptions:** internal and client-issue subjects are *descriptive*, because the reader is triaging, not deciding whether to open. Investor subjects can lead with the strongest fact. The scenario files show the format.

**The preview line counts.** The first words of the body show next to the subject. "Congrats on the Series A! Read your post about..." keeps the loop open; "I'm reaching out because..." closes it.

## Body moves

- **The bridge:** something true about them, connected to something true about the user, in that order. Their hobby, the user's same hobby; their side project from a personal annoyance, the user's. It works because it's real; a manufactured bridge is worse than none.
- **Their idea, your question** (door-opener): quote their wording back, apply it somewhere specific, ask the one question you actually have.
- **Credibility-forward** (no honest bridge): warm intro or domain overlap up front, then substance: what the user built, what it did, why this recipient specifically.
- **Add value before asking:** an honest observation from using their product, a small piece of work in their format, a useful intro. Offer it without strings: "made a quick teardown of the quote flow, happy to send it."
- **Relevance beats personalization for senior readers.** Directors and above respond far more to something about their company or problem than to a personal detail; personal hooks land better with individual contributors and founders who talk about themselves publicly.
- **Mostly about them.** More sentences about the reader and their world than about the user.
- **Size the ask to their job.** The reasons people open and answer don't change by recipient. What changes is which asks are possible. Something that's part of their job can be broad and direct. Anything else is a favor, so keep it narrow and one line. See the table below.
- **Designing the ask:** easy to say yes to (a redirect or an "interested?" beats a calendar slot on a cold email); one clear question; a reason ("because") when the ask is a real favor; an easy out when it helps ("either way, congrats on the launch").
- **Plain words.** Short sentences a busy person reads once. Simple beats sophisticated in every reply-rate study.
- **The first line is the point.** The sentence after the greeting is the hook or the reason for writing. No warm-up, no pleasantries, no introducing yourself by name (it's in the signature), no "thought I'd reach out" (they can see that you did). Deletion test: delete the opener and reread. If the email works just as well, it was decoration.

### What you can ask whom

The hook, brevity, and specificity stay the same for everyone. The ask is what changes, because it has to fit what this person can give without it costing them much.

| Recipient | Part of their job (ask directly) | A favor (keep small, or don't ask) | Ask that fits |
|---|---|---|---|
| **Recruiter** | Taking a candidate, saying whether the user fits a role, explaining the process | Advice on the user's career, intros outside their roles | "Here's my background for the [role]; open to a quick screen?" |
| **VC talent / platform partner** | Pointing candidates to portfolio companies, their talent network, intros to founders who are hiring | Vouching for someone they haven't met, a meeting with a partner | "Any pointers on the best way to get connected with portfolio companies?" |
| **Founder / CEO (small company)** | Hiring, talking about their product and plans, deciding fast | A long call, career advice | Interest plus "worth a conversation?", or "who on the team should I talk to about [role]?" |
| **Hiring manager** | Filling their role, judging fit for it | Referring the user to other teams | "Interested in [role]; [one line of proof]. Open to a chat?" |
| **Employee / peer on the team** | Answering a question about their own work or what the team is like | A referral, passing a résumé to their manager, anything that puts their name on the user | One specific question about their work. A referral comes later, if at all. |
| **Executive at a large company** | Very little from a cold email | Almost any ask | Something relevant to their problem plus a redirect: "who's the right person for [topic]?" |
| **Investor** | Hearing pitches that fit their thesis, saying yes or no | Advice on a deal they won't do, intros to other investors | "Raising [amount] for [one line]; want the deck?" |

A redirect ("who's the right person?") or a yes/no works almost everywhere when the right ask isn't clear. Asking a stranger for a referral almost never does.

## Voice and register

The user's voice lives in `examples.md`: contractions, `->` for asides, `hey [name],` for founders and cold outreach, `Hi [Name],` when more formal, sign-offs like `— [Name]`, `Best, [Name]`, `Thanks, [Name]`. Enthusiasm attached to a reason. Slight informality and imperfect punctuation are features; don't smooth them into corporate voice.

Register shifts by scenario (see the table up top), but the person doesn't: a client apology from this user still sounds like them, just steadier, with no jokes, `->` asides, or lowercase greeting. Match the reader's own register when they've written first.

## Never

- "I hope this email finds you well" / "Hope things have been good on your end" / "I'm reaching out because" / "thought I'd reach out" / "My name is..." / "I came across your profile" / "I wanted to express my sincere gratitude"
- "Just checking in" / "bumping this" / "per my last email" / "did you see my last email"
- "We apologize for any inconvenience" and other non-apologies (see `client-issues.md`)
- "passionate about," "leverage," "synergies," "circle back"
- Praise anyone could receive: "doing amazing things in the space," "such an exciting time"
- Excitement with no specific attached; more than one exclamation point, roughly
- Promises the user can't personally keep (credits, dates, "this will never happen again")

## Output

**Keep the user in the loop.** The user makes the calls; the drafts are for reacting to. End every round of drafts with one to three short questions in prose (never a pop-up picker), for example: which variant to carry forward; tone (kind, direct, simple, casual peer); any wording they'd say differently; the real detail behind a `[slot]`. On revisions, apply their feedback, still return the variants, and ask again about anything left open. Don't stall before the first draft to ask these; drafts first, questions after.

Return **two or three full variants that differ by angle, not by tone.** Tone variants make the user pick between shades of the same email; angle variants make them pick which true thing to lead with. Label each by angle in a few words ("Coin hook + trades bridge," "Traction-first," "Own it, then the fix"). Two variants are enough for short messages (nudges, LinkedIn notes, rejection replies, quick internal replies); don't invent an angle the material doesn't have. For a client incident, one strong draft plus a note on what to confirm can beat three variants.

For each variant, in order: the angle label, `Subject: ...` on its own line (whenever it starts a thread), then the body. If the environment has an email-draft tool (for example `message_compose_v1` with `kind: "email"` on Claude.ai, or a connected Gmail draft tool), use it, one variant per entry; otherwise plain text. **Never send an email yourself**; create drafts only, and only when asked.

Before handing over, run the review pass at the end of `references/sounding-human.md` on each variant.

After the drafts, one to three lines at most: which play and length you chose and the signal that decided it ("door-opener, short: no open role and he posts a lot"); the `[slots]` to fill; recipient facts you looked up and where; anything that needs confirming before sending (legal review for incidents, numbers for investors). Don't summarize the emails back.

**When to send**, if it comes up or the user is scheduling cold outreach: early in the week (Monday through Wednesday, Monday first), morning in the recipient's time zone. The effect is small next to relevance, so never hold a timely email for it; thank-yous go the same day, and incident and internal emails go when needed.

If a detail in `background.md` is stale or the user corrects it, use what they said and offer to update the file.
