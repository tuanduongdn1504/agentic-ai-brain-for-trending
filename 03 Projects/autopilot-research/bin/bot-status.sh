#!/usr/bin/env bash
# bot-status — quick health check for claude-channels tmux session + processes
SESSION="claude-channels"

echo "=== Bot status ==="
if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "tmux session '$SESSION': RUNNING"
    tmux list-sessions | grep "^$SESSION:"
else
    echo "tmux session '$SESSION': NOT RUNNING"
fi

echo ""
echo "=== Processes ==="
ps aux | grep -E "(bun server\.ts|bun run.*claude-plugins-official|claude --channels)" | grep -v grep || echo "(none)"

echo ""
echo "=== Bot pid file ==="
if [[ -f ~/.claude/channels/telegram/bot.pid ]]; then
    PID=$(cat ~/.claude/channels/telegram/bot.pid)
    echo "PID file says: $PID"
    if ps -p "$PID" >/dev/null 2>&1; then
        echo "PID is alive"
    else
        echo "PID is STALE (no process)"
    fi
else
    echo "(no bot.pid — bot probably never started)"
fi

echo ""
echo "=== Audit log (last 5 lines) ==="
if [[ -f ~/.claude/channels/telegram/audit.log ]]; then
    tail -5 ~/.claude/channels/telegram/audit.log
else
    echo "(no audit log yet)"
fi
