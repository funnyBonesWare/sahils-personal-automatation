"""Load settings from environment / .env file."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_config(env_path: Path | None = None) -> dict[str, str | bool | int | Path]:
    path = env_path or PROJECT_ROOT / ".env"
    if path.is_file():
        load_dotenv(path)

    headless = os.getenv("HEADLESS", "false").strip().lower() in ("1", "true", "yes")
    delay = int(os.getenv("ACTION_DELAY_SECONDS", "3"))

    profile = os.getenv("BROWSER_USER_DATA_DIR", "storage/browser-profile")
    profile_path = PROJECT_ROOT / profile if not Path(profile).is_absolute() else Path(profile)

    return {
        "linkedin_email": os.getenv("LINKEDIN_EMAIL", "").strip(),
        "linkedin_password": os.getenv("LINKEDIN_PASSWORD", "").strip(),
        "browser_user_data_dir": profile_path,
        "headless": headless,
        "action_delay_seconds": delay,
    }
