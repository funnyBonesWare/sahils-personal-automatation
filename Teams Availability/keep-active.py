#!/usr/bin/env python3
"""Keep macOS (and Microsoft Teams) from marking you idle.

Posts a harmless F18 key tap on a timer. macOS only resets idle time on real
input events — cursor warps alone do not count. F18 exists on no physical
keyboard, so nothing is typed or clicked.

Requires Accessibility permission for the terminal app running this script.
"""

from __future__ import annotations

import argparse
import ctypes
import random
import signal
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
LOG_FILE = SCRIPT_DIR / "keep-active.log"

# CoreGraphics event types
kCGHIDEventTap = 0
kCGEventKeyDown = 10
kCGEventKeyUp = 11
kVK_F18 = 0x4F  # virtual key — not present on physical Mac keyboards


class CGPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


_CG = ctypes.CDLL("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")
_CG.CGEventCreate.restype = ctypes.c_void_p
_CG.CGEventGetLocation.argtypes = [ctypes.c_void_p]
_CG.CGEventGetLocation.restype = CGPoint
_CG.CGEventCreateKeyboardEvent.restype = ctypes.c_void_p
_CG.CGEventCreateKeyboardEvent.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint16,
    ctypes.c_bool,
]
_CG.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]

_RUNNING = True


def _handle_signal(_signum: int, _frame: object) -> None:
    global _RUNNING
    _RUNNING = False


def _mouse_position() -> tuple[float, float]:
    event = _CG.CGEventCreate(None)
    pt = _CG.CGEventGetLocation(event)
    return pt.x, pt.y


def _post_key(code: int, down: bool) -> None:
    event = _CG.CGEventCreateKeyboardEvent(None, code, down)
    if not event:
        raise OSError("CGEventCreateKeyboardEvent returned null.")
    _CG.CGEventPost(kCGHIDEventTap, event)


def nudge() -> tuple[float, float]:
    """Tap F18 (invisible) and return current cursor position for logging."""
    _post_key(kVK_F18, True)
    _post_key(kVK_F18, False)
    x, y = _mouse_position()
    return x, y


def _log(message: str) -> None:
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}"
    print(line, flush=True)
    with LOG_FILE.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def _sleep_until(deadline: float, label: str) -> None:
    """Sleep in 1s ticks; log a heartbeat every 60s so the terminal stays alive."""
    heartbeat = 60
    last_beat = time.monotonic()
    while _RUNNING and time.monotonic() < deadline:
        time.sleep(1)
        now = time.monotonic()
        if now - last_beat >= heartbeat:
            remaining = max(0, int(deadline - now))
            _log(f"waiting — {remaining}s until {label}")
            last_beat = now


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prevent Microsoft Teams / macOS from marking you idle."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=60,
        help="Seconds between nudges (default: 60 = 1 minute).",
    )
    parser.add_argument(
        "-j",
        "--jitter",
        type=int,
        default=20,
        help="Random extra seconds added each cycle (default: 20).",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Nudge once and exit (useful for testing permissions).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.interval < 30:
        print("Interval must be at least 30 seconds.", file=sys.stderr)
        return 1

    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    try:
        x, y = nudge()
    except OSError as exc:
        _log(f"ERROR: {exc}")
        _log(
            "Grant Accessibility to this terminal: "
            "System Settings → Privacy & Security → Accessibility"
        )
        return 1

    if args.once:
        _log(f"nudge OK (F18 tap) at cursor ({x:.0f}, {y:.0f})")
        return 0

    _log(
        f"started — nudging every ~{args.interval}s "
        f"(+0–{args.jitter}s jitter). Ctrl+C to stop."
    )
    _log(f"nudge OK (F18 tap) at cursor ({x:.0f}, {y:.0f})")

    while _RUNNING:
        wait = args.interval + (random.randint(0, args.jitter) if args.jitter else 0)
        next_at = datetime.now() + timedelta(seconds=wait)
        _log(f"next nudge in {wait}s (at {next_at.strftime('%H:%M:%S')})")
        deadline = time.monotonic() + wait
        _sleep_until(deadline, "next nudge")

        if not _RUNNING:
            break

        try:
            x, y = nudge()
            _log(f"nudge OK (F18 tap) at cursor ({x:.0f}, {y:.0f})")
        except Exception as exc:
            _log(f"ERROR on nudge: {exc}")
            return 1

    _log("stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
