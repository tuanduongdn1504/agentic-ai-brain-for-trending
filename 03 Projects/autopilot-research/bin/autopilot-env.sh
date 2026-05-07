#!/usr/bin/env bash
# autopilot-env.sh — activate project-local venv + override Playwright cache.
# Worktree-agnostic: self-locates from ${BASH_SOURCE[0]} so the SAME script works
# regardless of which git worktree (or moved location) it lives in.
#
# Usage: cd to the autopilot-research project root in your worktree, then:
#   source bin/autopilot-env.sh
#
# What this does:
#   0. Resolves AUTOPILOT_ROOT to this script's parent dir (i.e., project root)
#   1. Activates Python venv at .venv/ (so `python`, `pip`, `notebooklm` resolve to project-local installs)
#   2. Overrides PLAYWRIGHT_BROWSERS_PATH so notebooklm-py's browser cache (~280 MB) lands inside the project
#   3. Optionally redirects XDG cache/config — opt-in (commented below)
#
# Cleanup: `rm -rf .venv` removes ~350 MB.
# Full nuke: `rm -rf .venv .cache .config` removes everything project-local-installed.

# 0. Self-locate. AUTOPILOT_ROOT = parent dir of this script's directory (bin/).
#    ${BASH_SOURCE[0]} works when sourced; falls back to $0 in plain shells.
__src="${BASH_SOURCE[0]:-$0}"
__script_dir="$( cd -- "$( dirname -- "$__src" )" >/dev/null 2>&1 && pwd )"
AUTOPILOT_ROOT="$( cd -- "$__script_dir/.." >/dev/null 2>&1 && pwd )"
export AUTOPILOT_ROOT
unset __src __script_dir

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
