#!/usr/bin/env bash
# autopilot-env.sh — activate project-local venv + override Playwright cache.
#
# Usage:
#   source "/Users/Cvtot/KJ OS Template/03 Projects/autopilot-research/bin/autopilot-env.sh"
#
# What this does:
#   1. Activates Python venv at .venv/ (so `python`, `pip`, `notebooklm` resolve to project-local installs)
#   2. Overrides PLAYWRIGHT_BROWSERS_PATH so notebooklm-py's browser cache (~280 MB) lands inside the project
#   3. Optionally redirects XDG cache/config — opt-in (commented below)
#
# Cleanup: `rm -rf .venv` removes ~350 MB.
# Full nuke: `rm -rf .venv .cache .config` removes everything project-local-installed.

AUTOPILOT_ROOT="/Users/Cvtot/KJ OS Template/03 Projects/autopilot-research"
export AUTOPILOT_ROOT

# 1. Activate venv (created via: python3 -m venv .venv)
if [ -f "$AUTOPILOT_ROOT/.venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  . "$AUTOPILOT_ROOT/.venv/bin/activate"
else
  echo "[autopilot-env] WARNING: .venv not found at $AUTOPILOT_ROOT/.venv" >&2
  echo "[autopilot-env] Run setup from $AUTOPILOT_ROOT/CLAUDE.md (Setup section)." >&2
fi

# 2. Project-local Playwright browser cache (~280 MB lands here, NOT in ~/.cache/ms-playwright)
export PLAYWRIGHT_BROWSERS_PATH="$AUTOPILOT_ROOT/.venv/playwright-browsers"

# 3. (OPT-IN) Project-local XDG dirs — uncomment to make EVERY tool that respects XDG
#    write its config + cache inside the project. Cleaner cleanup but may surprise other tools
#    that read from these paths during the same shell session.
# export XDG_CACHE_HOME="$AUTOPILOT_ROOT/.cache"
# export XDG_CONFIG_HOME="$AUTOPILOT_ROOT/.config"
# mkdir -p "$XDG_CACHE_HOME" "$XDG_CONFIG_HOME"

# Confirmation (silent in pipelines; toggle via AUTOPILOT_VERBOSE=1)
if [ "${AUTOPILOT_VERBOSE:-0}" = "1" ]; then
  echo "[autopilot-env] active. AUTOPILOT_ROOT=$AUTOPILOT_ROOT" >&2
  echo "[autopilot-env] python=$(command -v python)" >&2
  echo "[autopilot-env] PLAYWRIGHT_BROWSERS_PATH=$PLAYWRIGHT_BROWSERS_PATH" >&2
fi
