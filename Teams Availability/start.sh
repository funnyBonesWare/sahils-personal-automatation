#!/usr/bin/env bash
# Start keep-active in the background. Logs to keep-active.log in this folder.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$DIR/.keep-active.pid"
LOG_FILE="$DIR/keep-active.log"
SCRIPT="$DIR/keep-active.py"

if [[ -f "$PID_FILE" ]]; then
  OLD_PID="$(cat "$PID_FILE")"
  if kill -0 "$OLD_PID" 2>/dev/null; then
    echo "Already running (PID $OLD_PID). Run ./stop.sh first."
    exit 1
  fi
  rm -f "$PID_FILE"
fi

nohup python3 "$SCRIPT" >/dev/null 2>&1 &
echo $! >"$PID_FILE"
echo "Started keep-active (PID $(cat "$PID_FILE"))."
echo "Watch nudges: tail -f $LOG_FILE"
