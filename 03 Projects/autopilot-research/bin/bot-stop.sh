#!/usr/bin/env bash
# bot-stop — kill the claude-channels tmux session + its child processes
set -euo pipefail
SESSION="claude-channels"

if ! tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "No '$SESSION' tmux session running."
    exit 0
fi

# Send Ctrl-C first for clean Claude shutdown
tmux send-keys -t "$SESSION" C-c
sleep 1

# Kill the session
tmux kill-session -t "$SESSION"
echo "✓ Stopped bot tmux session"

# Belt-and-braces: kill any orphan bun processes
PIDS=$(pgrep -f "bun server.ts" || true)
if [[ -n "$PIDS" ]]; then
    echo "  Killing orphan bun server.ts: $PIDS"
    kill $PIDS 2>/dev/null || true
fi
