# Content guidelines (colleague-safe + employer-safe)

Your audience includes people at your **current company** — managers, coworkers, recruiters. Cursor must **reject or rewrite** drafts that look like a job search **or** that reference current work.

## Employer safety (HARD RULE — overrides everything)

**Never mention or imply Sahil's current company, team, product, or work.** This is the top priority — above tone, above warmth, above "the anecdote is better".

- **Never use:** `we`, `our team`, `our app`, `our grid`, `our dashboard`, `we shipped`, `we run`, `we deploy`, `we wrapped`, `we had`, `we cut`, `this sprint`, `last sprint`, `last week we`, `we just rolled out`
- **Never name:** company names, client names, customer names, internal tools, codenames, project nicknames, repo names, private SDKs, Slack channels, ticket IDs
- **Never include:** product surfaces unique to the employer (`operator tablet`, `floor tablet`, `fleet dashboard`, `the admin UI`), customer/scale numbers (rps, MAU, ARR, headcount, row counts attached to current work)
- **Never anything from** `content/blocked-phrases.txt`

**Always reframe as one of:**

- **Past-personal:** `I've shipped real-time dashboards…`, `a few years back I was building…`, `early in my frontend career I…`
- **Hypothetical / archetypal:** `imagine a virtualized grid with 800+ live rows…`, `picture an operator view that…`, `a common pattern I've seen is…`
- **Teaching / second person:** `you'll want to…`, `the senior habit is…`, `the fix is boring — …`

**Rewrite test:** Could someone at the current company recognize a project, customer, teammate, metric, or product surface? If yes, rewrite.

## Safe topics (posts)

- General technical opinions, tradeoffs, tools, patterns — **decoupled from current work**
- Past learnings reframed as personal or hypothetical
- Conference talks, courses, open-source, side learning (not "side job hunt")
- Industry news with a technical take

## Avoid (blocked by guardrails)

- "Open to work", "looking for roles", "DM for opportunities"
- Criticizing your employer or saying you want to leave (also: praising, naming, or hinting at the employer)
- `#OpenToWork`, resume links, recruiter CTAs

## Comments (1–2/day; more if Sahil pastes extra URLs)

- **Same rules as posts:** easy conversational Indian English, no em dash (`—`), employer-safe
- Match **`content/VOICE.md`** — peer engineer, 1–3 sentences, specific insight
- Add value: stack, pattern, tradeoff, or brief past-personal experience (`I've seen…`, `I ran into…`)
- **Explain acronyms inline** (PKCE, OIDC, RSC, etc.) in plain words when you use them
- **Do not** say `we saw…`, `our team…`, or anything that implies a current employer — same rule as posts
- Do not comment "Great post!" or "Thanks for sharing!" (sounds like a bot)

## Posts

- Match **`content/VOICE.md`** — Sahil's hooks, numbered sections, production lens, one question at end
- **Easy English:** simple words, short sentences, warm tone. Not essay-polished.
- **No em dash (`—`)** in LinkedIn body text. Use full stops, commas, or new lines.
- Numbered section labels on their own line; body on the next line

## Connection notes

- Neutral networking: shared interest, enjoyed their post, same community
- No mention of job search or “pick your brain about opportunities”

## Workflow

1. Ask Cursor for today's content. Cursor saves files in your voice:
   - `drafts/YYYY-MM-DD.md` — post + hashtags
   - `comments/YYYY-MM-DD.md` — up to 2 comments (you supply target URLs)
   - `connects/YYYY-MM-DD.md` — connect notes (you supply profile URLs)
2. Open LinkedIn in your browser, copy-paste, click Post / Send.
3. Tell Cursor *"I posted it"* — it appends to `storage/post-history.jsonl`.
