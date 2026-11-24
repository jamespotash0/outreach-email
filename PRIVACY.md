# Privacy policy

Last updated: November 24, 2026

outreach-email is a set of instructions (an Agent Skill) that runs inside your AI agent, such as Claude Code. Its author runs no server and collects no data from you.

## What it stores, and where

- **Your background file**, `~/.outreach-email/background.md`: what you tell it about yourself (name, work history, projects, links) so drafts can draw on it.
- **Your lessons file**, `~/.outreach-email/lessons.md`: lessons you save with the `learn` command.

Both are plain files on your own computer. Nothing is uploaded anywhere by the skill. Delete the `~/.outreach-email` folder to remove them.

## What it reads

- What you paste or type: drafts, emails, notes about the person you're writing to.
- Public information about recipients (their posts, talks, company news), when your agent has web search and you ask it to research someone. Those searches go through your agent's own tools.

## What it sends

- **Nothing by default.**
- **Optional, opt-in only:** after `learn`, the skill can suggest a general lesson to this project as a GitHub issue. It removes names, companies, and identifying details, shows you the exact text, and only files the issue after you approve it. The issue is public on GitHub, under your account.

## Third parties

Your conversations with your AI agent are handled by that agent's provider (for example, Anthropic for Claude) under their own privacy policy. This skill doesn't change that.

## Audience

Not intended for users under 18.

## Contact

Questions: open an issue at https://github.com/jamespotash0/outreach-email/issues
