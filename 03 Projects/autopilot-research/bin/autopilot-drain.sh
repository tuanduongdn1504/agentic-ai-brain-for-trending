#!/usr/bin/env bash
# Wrapper for autopilot-drain.py — invoked by launchd UserAgent at scheduled time.
#
# Uses caffeinate -i to prevent idle sleep WHILE the drain runs (auto-releases
# when the script exits). Does NOT modify pmset / system sleep settings.
#
# All stdout/stderr is captured to a dated log file in loop-log/ for post-mortem
# inspection.

set -euo pipefail

# Self-locate project root (this script lives in <root>/bin/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

# Activate venv via the existing env shim
# shellcheck disable=SC1091
source "$PROJECT_ROOT/bin/autopilot-env.sh"

LOG_DIR="$PROJECT_ROOT/loop-log"
mkdir -p "$LOG_DIR"
TS="$(date +%Y-%m-%d-%H%M)"
STDOUT_LOG="$LOG_DIR/autopilot-overnight-${TS}.stdout.log"
STDERR_LOG="$LOG_DIR/autopilot-overnight-${TS}.stderr.log"

echo "[$(date)] starting autopilot drain (caffeinate)" >> "$STDOUT_LOG"

# caffeinate -i  : prevent idle sleep
# caffeinate -m  : also prevent disk sleep
# Wrap the python invocation so caffeinate is released the moment drain exits.
caffeinate -i -m \
  python "$PROJECT_ROOT/bin/autopilot-drain.py" \
  >> "$STDOUT_LOG" 2>> "$STDERR_LOG"

EXIT_CODE=$?
echo "[$(date)] drain exited rc=$EXIT_CODE" >> "$STDOUT_LOG"
exit $EXIT_CODE
