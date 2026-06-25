#!/usr/bin/env bash
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$DIR/.keep-active.pid"

if [[ ! -f "$PID_FILE" ]]; then
  echo "Not running (no PID file)."
  exit 0
fi

PID="$(cat "$PID_FILE")"
if kill -0 "$PID" 2>/dev/null; then
  kill "$PID"
  echo "Stopped keep-active (PID $PID)."
else
  echo "Process $PID not found; cleaning up PID file."
fi
rm -f "$PID_FILE"
