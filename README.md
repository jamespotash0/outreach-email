# outreach-email

An [Agent Skill](https://agentskills.io) that writes emails in your own voice that people actually answer:

- **Cold and warm outreach** to founders, execs, experts, partners: it researches the person (writing, podcasts, talks, portfolio), finds a real connection to you, and decides whether to open a door or make the ask, and how long to go.
- **Job search:** interview thank-yous, hiring-manager and recruiter emails, check-ins when you're ghosted, rejection replies.
- **Investors:** cold pitches, forwardable intro blurbs, post-meeting follow-ups, replies to a pass, monthly updates.
- **Internal:** cross-team asks, notes to execs, status updates, nudges, escalations, saying no.
- **Client issues:** outage, missed deadline, or billing-error emails that own the problem without over-promising or admitting legal liability.

One skill folder, no agent-specific code. It runs anywhere the SKILL.md format is supported (Claude Code, Codex, Cursor, Gemini CLI, Grok Build, Hermes, Copilot, and more) and uploads as a zip to Claude.ai, ChatGPT, and Perplexity.

## Install

**Any coding agent, one command** ([skills CLI](https://github.com/vercel-labs/skills), detects Claude Code, Codex, Cursor, Gemini CLI, Grok, Hermes, Copilot, Windsurf, OpenCode, Cline, Goose, Amp and 60+ more):

```sh
npx skills add jamespotash0/outreach-email -g            # pick agents interactively
npx skills add jamespotash0/outreach-email -g -a '*' -y  # every detected agent
```

**Plugin marketplaces**

| Agent | Command |
|---|---|
| Claude Code | `/plugin marketplace add jamespotash0/outreach-email` then `/plugin install outreach-email@outreach-email` |
| Codex | `codex plugin marketplace add jamespotash0/outreach-email` |
| Gemini CLI | `gemini extensions install https://github.com/jamespotash0/outreach-email` |
| VS Code / Copilot | Command palette: "Chat: Install Plugin From Source", paste the repo URL |
| Cursor | Reads the root `plugin.json`; or use `npx skills` above |

**Chat apps (upload a zip)**

Build the zip with the skill files at its root:

```sh
cd skills/outreach-email && zip -r ../../outreach-email.zip . -x '.*'
```

| App | Where |
|---|---|
| Claude.ai / Claude desktop | Customize > Skills > + > Upload a skill (code execution on) |
| ChatGPT | Customize > Skills > + > Upload a Skill (Business/Enterprise: Plugins > Skills) |
| Perplexity Computer | Skills > Create skill > Upload a skill |
| Perplexity Agent API / Claude API | Upload through `/v1/skills` and reference the skill id |
| Perplexity Spaces, ChatGPT Projects, custom GPTs | No skill support: paste `SKILL.md` into the instructions and upload the `references/` files |

Zipped uploads don't carry your filled-in `background.md` back out. Fill it in first (or let the skill interview you, then paste the result into the file) and re-upload.

**By hand.** Clone once and symlink into each agent, so they all share one `background.md`:

```sh
git clone https://github.com/jamespotash0/outreach-email.git ~/outreach-email
ln -s ~/outreach-email/skills/outreach-email ~/.agents/skills/outreach-email   # Codex, Cursor, Gemini, Grok, Copilot, Windsurf, Goose
ln -s ~/outreach-email/skills/outreach-email ~/.claude/skills/outreach-email   # Claude Code
ln -s ~/outreach-email/skills/outreach-email ~/.hermes/skills/outreach-email   # Hermes Agent
```

Paths drift between releases; check your agent's docs if the skill doesn't show up.

## First use

Ask for an email ("what should I send Dana after my final round?", "need to tell Acme about yesterday's outage"). The first time, the skill asks a few questions to fill in the parts of `skills/outreach-email/references/background.md`: only the sections that scenario needs (your experience and personal threads, your role and company, or your startup's numbers). Every later email draws on that file.

> **Privacy:** your filled-in `background.md` stays local. It's in `.gitignore`, so it won't be committed or pushed. Zip uploads to Claude.ai, ChatGPT, or Perplexity do include it if you zip after filling it in, which is what you want there.

## What's inside

```
.claude-plugin/marketplace.json     Claude Code (and Codex) marketplace
plugin.json                         Agent Plugins 1.0: VS Code, Copilot, Cursor, Codex
gemini-extension.json               Gemini CLI extension
skills/outreach-email/
  SKILL.md                          core: scenario routing, research, play and length, voice, output
  references/background.template.md structure for your asset pool; background.md (gitignored) is created on first use
  references/examples.md            annotated real emails, specifics bracketed out
  references/finding-the-connection.md  researching the recipient and building the hook
  references/job-search.md          interviews, hiring managers, recruiters, rejections
  references/investors.md           pitches, intros, post-meeting, passes, updates
  references/internal.md            asks, exec emails, updates, nudges, escalation
  references/client-issues.md       incident and apology emails, liability lines
  references/follow-ups.md          nudges, replies, LinkedIn, intro requests
  references/sounding-human.md      AI-writing tells and the review pass
  references/perspectives.md        what practitioners and datasets say, including where they disagree
  scripts/lint_email.py             mechanical check for drafts (Python 3, no deps)
```

`python3 skills/outreach-email/scripts/lint_email.py draft.txt` flags em dashes, curly quotes, stock phrases and non-apologies, leftover placeholders, and Title Case subjects. Add `--max-chars 300` for LinkedIn connection notes and `--selftest` to check the script itself.

## Credits

Scenario guidance draws on published advice from Michael Seibel and Aaron Harris (YC), Elizabeth Yin, Hunter Walk, Paul Graham, Fred Wilson, and SaaStr (investors); HBR, Rogers and Lasky-Fink's research on writing for busy readers, and the GitLab handbook (internal); Lewicki et al.'s apology research, Atlassian and PagerDuty incident communication guides, and the GitLab, Buffer, Cloudflare, and 37signals incident write-ups (client issues); Gong, Lavender, 30 Minutes to President's Club, Hunter, and Boomerang reply-rate data; [Hunter's cold email guide](https://hunter.io/cold-email-guide/how-to-write-email-outreach/); and job-search stories from Morning Brew, Notion, interviewing.io, and Aakash Gupta.


This skill's review pass and tell list draw on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and [blader/humanizer](https://github.com/blader/humanizer). Nudge and follow-up guidance comes from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (cold-email), [noamseg/interview-coach-skill](https://github.com/noamseg/interview-coach-skill), and [Ask a Manager](https://www.askamanager.org/2007/08/when-to-follow-up-after-interview.html). The one-line gaps list and the channel-length variant come from [alinafe82/job-hunting-skills](https://github.com/alinafe82/job-hunting-skills). Timing data is from [Woodpecker](https://woodpecker.co/blog/cold-email-statistics/), [Belkins](https://belkins.io/blog/cold-email-response-rates), [Lavender](https://www.lavender.ai/blog/cold-email-101), and [LinkedIn](https://www.linkedin.com/help/linkedin/answer/a411986/inmail-character-limits).

MIT licensed.
