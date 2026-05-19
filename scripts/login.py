"""Open LinkedIn and sign in using credentials from .env.

Usage:
    python scripts/login.py

Install browsers once:
    playwright install chromium
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

# Allow running as: python scripts/login.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.async_api import async_playwright

from src.config import load_config, PROJECT_ROOT


async def main() -> None:
    cfg = load_config()
    email = cfg["linkedin_email"]
    password = cfg["linkedin_password"]
    if not email or not password:
        print("Set LINKEDIN_EMAIL and LINKEDIN_PASSWORD in .env (see .env.example)")
        sys.exit(1)

    profile_dir: Path = cfg["browser_user_data_dir"]  # type: ignore[assignment]
    profile_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            headless=bool(cfg["headless"]),
            viewport={"width": 1280, "height": 800},
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://www.linkedin.com/login", wait_until="domcontentloaded")

        await page.fill("#username", str(email))
        await page.fill("#password", str(password))
        await page.click('button[type="submit"]')
        await page.wait_for_load_state("networkidle", timeout=60_000)

        print("Login flow finished. Check the browser window.")
        print(f"Session profile: {profile_dir}")
        if not bool(cfg["headless"]):
            print("Close the browser window when done, or press Ctrl+C.")
            try:
                await asyncio.sleep(3600)
            except KeyboardInterrupt:
                pass
        await context.close()


if __name__ == "__main__":
    asyncio.run(main())
