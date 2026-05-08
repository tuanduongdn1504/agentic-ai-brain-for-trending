#!/usr/bin/env bash
# bot-start — launch claude --channels in a detached tmux session.
#
# Why tmux + caffeinate:
# - tmux: bot survives terminal-window-close (you can close iTerm and the bot keeps running)
# - caffeinate -i: prevents idle sleep WHILE the bot runs; releases when bot stops
# - DOES NOT survive reboot — for that, see bin/OVERNIGHT-SETUP.md launchd pattern
#
# Usage: bot-start
# Then: bot-status (check) / bot-attach (view live) / bot-stop (kill)

set -euo pipefail

SESSION="claude-channels"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 1. Verify prereqs
for cmd in tmux caffeinate claude bun; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "ERROR: $cmd not found in PATH" >&2
        exit 1
    fi
done

# 2. If session already exists, ask user (avoid duplicate listeners — Telegram 409 conflict)
if tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "tmux session '$SESSION' already running."
    echo "To replace it: bot-stop, then bot-start."
    echo "To view: bot-attach"
    exit 0
fi

# 3. Verify token configured
TOKEN_FILE="$HOME/.claude/channels/telegram/.env"
if [[ ! -s "$TOKEN_FILE" ]]; then
    echo "ERROR: $TOKEN_FILE missing or empty." >&2
    echo "Run: claude → /telegram:configure <token> first." >&2
    exit 1
fi

# 4. Launch under tmux + caffeinate.
# Wrap the inner command so it stays alive even if claude exits — that way we
# can capture errors via `tmux capture-pane` instead of the session vanishing.
INNER='exec caffeinate -i -m claude --channels plugin:telegram@claude-plugins-official 2>&1; echo; echo "[bot-start.sh] claude --channels exited (rc=$?). Window stays open for debug — Ctrl-B D to detach."; sleep 999999'
tmux new-session -d -s "$SESSION" -c "$PROJECT_ROOT" "$INNER"

# 5. Brief pause + verify
sleep 3
if ! tmux has-session -t "$SESSION" 2>/dev/null; then
    echo "ERROR: tmux session died immediately." >&2
    echo "Possible causes:" >&2
    echo "  - tmux can't find 'claude' or 'caffeinate' in PATH" >&2
    echo "  - inner shell parsing broke (try running the command manually)" >&2
    exit 1
fi

# 6. Capture last 30 lines from session — surface any startup errors
PANE_OUT=$(tmux capture-pane -t "$SESSION" -p 2>/dev/null | tail -30)
if echo "$PANE_OUT" | grep -qE "(error|Error|ERROR|409 Conflict|cannot find|not found)"; then
    echo "WARN: bot started but pane shows errors:" >&2
    echo "---" >&2
    echo "$PANE_OUT" >&2
    echo "---" >&2
    echo "Run 'bot-attach' to see live output. 'bot-stop' to kill." >&2
    exit 2
fi

echo "✓ Bot started in tmux session '$SESSION'"
echo "  Project dir: $PROJECT_ROOT"
echo ""
echo "  Commands:"
echo "    bot-status   — check process state"
echo "    bot-attach   — view live bot output (Ctrl-B D to detach)"
echo "    bot-stop     — kill the bot"
echo ""
echo "  Bot is reachable at: @BearResearchBot"
