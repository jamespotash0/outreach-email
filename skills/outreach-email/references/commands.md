# Command playbooks

Playbooks for the commands in SKILL.md that need more than the main flow. Agent files are in this skill's `agents/` folder. Where you can't spawn that agent, read its file and do the work yourself, following the same input, checks, and return.

## angles

Find the angle without drafting yet.

1. Research the recipient as in `finding-the-connection.md`. In team mode, run the research agents in parallel.
2. Run `agents/angle-finder.md` once per lens (four lenses, in parallel when you can). Without subagents, work through the four lenses yourself, one at a time, and don't let a strong early idea stop you from finishing the others.
3. Merge the results into the hook sheet: the three or four strongest angles, each with its hook line, subject, and source.
4. Ask the user only what those angles need (their half, in prose, three questions at most).
5. Stop there. Offer to draft from whichever angle they pick (that's `cold`).

## critique

The user pastes an email, their own draft or one they've sent.

1. If you don't know who it's going to, ask one question: their role and how they know the user. Otherwise go on.
2. Run `agents/recipient-critic.md` with the email and the one-line recipient description, nothing else.
3. Run `scripts/lint_email.py` on it if you can run code.
4. Return the critic's verdict, the lint flags worth acting on, then one revised version that keeps the user's voice and fixes only what the critique found. Don't rewrite lines that worked.

## learn

The user shares an email (theirs or someone else's) to make the skill better. The goal is lessons, not templates: why it got opened, why it was easy to answer, what made it bold or different.

1. If you don't know them, ask about the outcome (replied? how fast? what happened?) and who the recipient was. One question. If there's no outcome, say the lesson comes from judgment, not results.
2. Pull out the lessons: the reason to open it, how fast it got to the point, what made it easy to answer, what was bold, and what to tighten. Note anything that depends on who the recipient was (see "What you can ask whom" in SKILL.md).
3. Make each lesson hold in more than one situation: a role that's open, missing, or changed; a different industry; a different kind of recipient.
4. Save each lesson where it will last:
   - **The user is working in a git clone of this skill's repo** (the skill folder is inside a git work tree they're editing): find the file and section that already covers the lesson and add a line or two there. Add to an existing rule before creating a new section.
   - **Otherwise** (an installed copy, which updates overwrite): append to `~/.outreach-email/lessons.md`, one short entry per lesson, under a heading naming the scenario file it belongs to (e.g. `## job-search.md`). Create the file if it's missing. If you can't write files, give them the entry to save there.
   Either way, quote at most a short line (a subject, a turn of phrase) as an illustration. Never paste the email in as a template.
5. Don't record outcomes or facts you weren't given.
6. Tell the user where each lesson went.
7. **Offer to share it upstream** (installed copies only), once: "Want to suggest this for everyone who uses the skill?" If yes, write a version with every name, company, product, and identifying detail removed, show it to them, and only after they approve, open an issue on `jamespotash0/outreach-email` (with `gh issue create` if available; otherwise give them the text and the link `https://github.com/jamespotash0/outreach-email/issues/new`). The issue holds the general lesson and which file it belongs in, never the email.
