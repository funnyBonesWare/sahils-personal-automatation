# Sahil's Personal Automations

Private monorepo for personal workflow automation — **everything is prompt-driven from Cursor**. No Python, no cron, no API keys.

## Projects

| Folder | Description |
|--------|-------------|
| [**LinkedIn Automation**](LinkedIn%20Automation/) | Daily LinkedIn post, comments, and connection notes — Cursor writes content in Sahil's voice, Sahil copy-pastes into LinkedIn |
| [**Teams Availability**](Teams%20Availability/) | Keeps Microsoft Teams from marking you idle — tiny mouse nudge every 4 minutes on macOS |

More automations can be added as sibling folders later (e.g. Jira summaries, weekly exports). Each project owns its own `.cursor/rules/*.mdc`.

---

## How it works

1. Open this repo in Cursor.
2. Ask Cursor for what you want, e.g. *"write today's LinkedIn post"*.
3. Cursor reads the relevant rules + voice files, then saves output to a dated markdown file inside the project folder.
4. You copy-paste the content into the target app yourself.

That's it. No scripts, no browser automation. See each project's README for the specific prompts and file layout.

---

Private — personal use only.
