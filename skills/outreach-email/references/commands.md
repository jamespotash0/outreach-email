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
4. Find the file and section that already covers each lesson and add a line or two there. Add to an existing rule before creating a new section. Quote at most a short line (a subject, a turn of phrase) as an illustration. Never paste the email in as a template.
5. Don't record outcomes or facts you weren't given.
6. Tell the user which files changed and the lesson each one now carries. If you can't edit files, give them the exact edits instead.
