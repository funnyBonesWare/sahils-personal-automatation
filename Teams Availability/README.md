# Teams Availability

Keeps you showing as **Available** in Microsoft Teams by preventing macOS from going idle. Teams marks you Away when the system has had no keyboard or mouse activity for ~5 minutes; this script taps the virtual **F18** key every 60 seconds (invisible — no physical Mac keyboard has F18, so nothing is typed).

No installs. Uses built-in Python 3 + macOS CoreGraphics.

## One-time setup

1. **Grant Accessibility permission** to the app that runs the script (Terminal, iTerm, or Cursor):
   - **System Settings → Privacy & Security → Accessibility**
   - Add your terminal app and turn it on.

2. **Test permissions:**

   ```bash
   cd "Teams Availability"
   chmod +x keep-active.py start.sh stop.sh
   python3 keep-active.py --once
   ```

   You should see: `Nudge OK. Accessibility permission looks good.`

## Run for the day

**Foreground** (live output in terminal + `keep-active.log`):

```bash
python3 keep-active.py
```

**Background** (log file only — watch with `tail -f keep-active.log`):

```bash
./start.sh
# in another terminal:
tail -f keep-active.log
# later
./stop.sh
```

## Options

| Flag | Default | Meaning |
|------|---------|---------|
| `-i`, `--interval` | `60` | Seconds between nudges (1 min) |
| `-j`, `--jitter` | `20` | Random extra seconds so timing is not robotic |
| `--once` | — | Single nudge; verify permissions |

Example — nudge every 3 minutes:

```bash
python3 keep-active.py -i 180
```

## Auto-start on login (optional)

```bash
PLIST="$HOME/Library/LaunchAgents/com.sahil.teams-keep-active.plist"
cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.sahil.teams-keep-active</string>
  <key>ProgramArguments</key>
  <array>
    <string>$(which python3)</string>
    <string>$(cd "$(dirname "$0")" && pwd)/keep-active.py</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$(cd "$(dirname "$0")" && pwd)/keep-active.log</string>
  <key>StandardErrorPath</key>
  <string>$(cd "$(dirname "$0")" && pwd)/keep-active.log</string>
</dict>
</plist>
EOF
launchctl load "$PLIST"
```

Unload later: `launchctl unload "$PLIST"`

## Notes

- This only affects **idle detection** (mouse/keyboard inactivity). It does not change a manually set status like Busy or Do not disturb.
- Your employer may have policies about presence tools — use at your own discretion.
- `keep-active.log` and `.keep-active.pid` are gitignored.
