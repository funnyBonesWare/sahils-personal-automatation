# LinkedIn Automation

Private project for LinkedIn workflows (posting, engagement, messaging, etc.) using browser automation. Credentials stay in local `.env` only.

## Status

Early scaffold. Implemented so far:

- Environment-based config (`src/config.py`)
- Persistent browser session login (`scripts/login.py`)

Planned capabilities (add scripts as needed):

- Scheduled or manual posts
- Connection / follow-up flows
- Feed engagement (with strict rate limits)
- Export analytics or lead lists

> **Compliance:** Automating LinkedIn may violate [LinkedIn’s User Agreement](https://www.linkedin.com/legal/user-agreement). Use conservative delays, a real account, and only workflows you are allowed to run. This repo is for personal/private use.

## Setup

```bash
cd ~/linkedin-automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
# Edit .env with your credentials
```

## First run — save session

```bash
python scripts/login.py
```

Uses a persistent Chromium profile under `storage/browser-profile` so later scripts can reuse the logged-in session without re-entering credentials every time.

## Project layout

```
linkedin-automation/
├── src/
│   └── config.py       # .env loader
├── scripts/
│   └── login.py        # Sign in & persist session
├── storage/            # gitignored — browser profile, exports
├── .env.example
└── requirements.txt
```

## Environment variables

| Variable | Description |
|----------|-------------|
| `LINKEDIN_EMAIL` | Account email |
| `LINKEDIN_PASSWORD` | Account password |
| `BROWSER_USER_DATA_DIR` | Persistent profile path (default: `storage/browser-profile`) |
| `HEADLESS` | `true` / `false` (default: `false` for login) |
| `ACTION_DELAY_SECONDS` | Pause between automated actions (default: `3`) |

## Security

- Never commit `.env` or `storage/`
- Repository is **private** on GitHub
- Rotate passwords if `.env` is ever exposed

## License

Private — personal use only.
