# LinkedIn Automation (Cursor-only)

Part of **[Sahil's Personal Automations](../README.md)**.

**Cursor writes the content in Sahil's voice. Sahil pastes it into LinkedIn manually.**

No Python. No Playwright. No API key. No cron. The entire workflow is one Cursor prompt per day plus a copy-paste.

---

## Setup

Nothing to install. The first time you use this:

1. Open the monorepo in Cursor.
2. Make sure the `.cursor/rules/linkedin-automation.mdc` rule is loaded (it is, automatically — globs match this folder).
3. (Optional) Paste your recent LinkedIn posts into `storage/profile/recent-posts.md` so Cursor avoids repeating themes.
4. (Optional) Write a short bio into `storage/profile/sahil-siddiqui-profile.md`.

---

## Daily workflow

### 1. Ask Cursor for today's content

Example prompts:

> Write today's LinkedIn post. Pick a fresh idea — don't repeat my last 5 themes.

> Give me 3 post ideas for today, pick the strongest, save the draft.

> I want to comment on these 2 posts: <URL1>, <URL2>. Write the comments.

> I'm sending connection requests to: <profile URL 1>, <profile URL 2>. Write the notes.

You can also edit `prompts/daily-request.md` first and just say *"do today's content"*.

### 2. Cursor saves files (you do not have to)

| File | Content |
|------|---------|
| `drafts/YYYY-MM-DD.md` | Post body + hashtags |
| `comments/YYYY-MM-DD.md` | Up to 2 comments, each with target URL + comment text |
| `connects/YYYY-MM-DD.md` | Connect requests, each with profile URL + short note |

### 3. You copy-paste into LinkedIn

Open LinkedIn in your browser, paste the post, click Post. Repeat for comments and connection notes.

### 4. Log it

Tell Cursor *"I posted it"* or *"log today's post"*. Cursor appends a line to `storage/post-history.jsonl` so the next idea pass knows what's already been published.

---

## Folder layout

```
LinkedIn Automation/
├── .cursor/rules/             # full operating manual for Cursor
├── content/
│   ├── VOICE.md               # tone, structure, anti-patterns — Cursor reads this every time
│   ├── GUIDELINES.md          # colleague-safe rules
│   └── blocked-phrases.txt    # phrases the draft must not contain
├── prompts/                   # optional brief Sahil edits before asking
├── drafts/YYYY-MM-DD.md       # today's post (Cursor writes)
├── comments/YYYY-MM-DD.md     # today's comments (Cursor writes)
├── connects/YYYY-MM-DD.md     # today's connect notes (Cursor writes)
└── storage/
    ├── post-history.jsonl     # one line per published post (Cursor appends)
    └── profile/               # voice context (Sahil pastes/edits)
```

---

## Voice & safety

- **`content/VOICE.md`** — required reading for Cursor before every post/comment.
- **`content/GUIDELINES.md`** — colleague-safe rules (coworkers follow this account).
- **`content/blocked-phrases.txt`** — phrases that auto-fail a draft.

If a draft sounds like generic AI thought leadership, ask Cursor *"rewrite — this doesn't sound like me"*.

---

## Compliance

This repo contains no automation that touches LinkedIn directly. You publish manually, so the workflow is within LinkedIn's User Agreement. Personal use only.
