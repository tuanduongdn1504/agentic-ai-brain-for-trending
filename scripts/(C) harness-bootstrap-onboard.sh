#!/usr/bin/env bash
set -euo pipefail

DRY_RUN=0
YES=0
VERIFY_ONLY=0
RUN_DOCTOR=0

usage() {
  cat <<'EOF'
Storm Bear harness bootstrap

Usage:
  bash "scripts/(C) harness-bootstrap-onboard.sh" [--dry-run] [--yes] [--verify] [--doctor]

Options:
  --dry-run   Show actions without writing files.
  --yes       Apply local config changes without an interactive confirmation.
  --verify    Verify existing local harness config only.
  --doctor    Run codex doctor after writing or verifying.
  -h, --help  Show this help.

This script writes local machine config under ~/.claude, ~/.codex, ~/.gemini, and ~/.ping-island.
It does not copy auth tokens or Codex hook trust hashes.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1 ;;
    --yes) YES=1 ;;
    --verify) VERIFY_ONLY=1 ;;
    --doctor) RUN_DOCTOR=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
  shift
done

log() {
  printf '[harness] %s\n' "$*"
}

warn() {
  printf '[harness][warn] %s\n' "$*" >&2
}

die() {
  printf '[harness][error] %s\n' "$*" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"
}

repo_root() {
  local script_dir
  script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  cd "$script_dir/.." && pwd
}

REPO_ROOT="$(repo_root)"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_ROOT="$HOME/.storm-bear-harness-backups/$TIMESTAMP"

PING_BRIDGE="$HOME/.ping-island/bin/ping-island-bridge"
PING_CONFIG="$HOME/.ping-island/bridge-config.json"
AGENTPET_BIN="/Applications/AgentPet.app/Contents/MacOS/agentpet"

CLAUDE_SETTINGS="$HOME/.claude/settings.json"
CODEX_HOOKS="$HOME/.codex/hooks.json"
CODEX_CONFIG="$HOME/.codex/config.toml"
GEMINI_SETTINGS="$HOME/.gemini/settings.json"

confirm_write() {
  if [[ "$VERIFY_ONLY" -eq 1 || "$DRY_RUN" -eq 1 || "$YES" -eq 1 ]]; then
    return
  fi

  cat <<EOF
This will write local harness config files for:
  $CLAUDE_SETTINGS
  $CODEX_HOOKS
  $CODEX_CONFIG
  $GEMINI_SETTINGS
  $PING_BRIDGE
  $PING_CONFIG

Backups will be placed under:
  $BACKUP_ROOT
EOF
  printf 'Continue? [y/N] '
  read -r answer
  case "$answer" in
    y|Y|yes|YES) ;;
    *) die "Cancelled." ;;
  esac
}

backup_file() {
  local target="$1"
  [[ -e "$target" ]] || return 0

  local rel="${target#$HOME/}"
  local backup="$BACKUP_ROOT/$rel"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "Would back up $target -> $backup"
    return 0
  fi

  mkdir -p "$(dirname "$backup")"
  cp -p "$target" "$backup"
  log "Backed up $target -> $backup"
}

install_file_from_tmp() {
  local tmp="$1"
  local target="$2"
  local mode="${3:-}"

  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "Would write $target"
    return 0
  fi

  backup_file "$target"
  mkdir -p "$(dirname "$target")"
  cp "$tmp" "$target"
  if [[ -n "$mode" ]]; then
    chmod "$mode" "$target"
  fi
  log "Wrote $target"
}

check_prereqs() {
  need_cmd jq

  [[ "$(uname -s)" == "Darwin" ]] || warn "This bootstrap is designed for macOS."

  local paths=(
    "/Applications/AgentPet.app"
    "/Applications/Ping Island.app"
    "/Applications/Antigravity IDE.app"
    "/Applications/Obsidian.app"
  )

  for path in "${paths[@]}"; do
    if [[ ! -e "$path" ]]; then
      warn "Missing expected app: $path"
    fi
  done

  command -v claude >/dev/null 2>&1 || warn "claude CLI not found on PATH."
  command -v codex >/dev/null 2>&1 || warn "codex CLI not found on PATH."
}

write_ping_island_files() {
  local tmp
  tmp="$(mktemp)"
  cat >"$tmp" <<'EOF'
#!/bin/zsh
export ISLAND_SOCKET_PATH='/tmp/island.sock'
export PING_ISLAND_BRIDGE_CONFIG="$HOME/.ping-island/bridge-config.json"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
candidates=(
  "$SCRIPT_DIR/PingIslandBridge"
  "$SCRIPT_DIR/IslandBridge"
  "/Applications/Ping Island.app/Contents/MacOS/PingIslandBridge"
  "/Applications/Ping Island.app/Contents/MacOS/IslandBridge"
)

for candidate in "${candidates[@]}"; do
  if [ -n "$candidate" ] && [ -x "$candidate" ]; then
    exec "$candidate" "$@"
  fi
done

echo "PingIslandBridge binary not found" >&2
exit 127
EOF
  install_file_from_tmp "$tmp" "$PING_BRIDGE" "755"
  rm -f "$tmp"

  tmp="$(mktemp)"
  jq -n '{routePromptsToTerminal: false}' >"$tmp"
  install_file_from_tmp "$tmp" "$PING_CONFIG" "644"
  rm -f "$tmp"
}

generate_codex_hooks() {
  jq -n --arg ping "$PING_BRIDGE" --arg agentpet "$AGENTPET_BIN" '
    def ping_cmd($source): "\"" + $ping + "\" --source " + $source;
    def agentpet_cmd($agent): "\"" + $agentpet + "\" hook --agent " + $agent;
    {
      PermissionRequest: [
        {hooks: [{command: ping_cmd("codex"), timeout: 86400, type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ],
      PostToolUse: [
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ],
      PreToolUse: [
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ],
      SessionStart: [
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ],
      Stop: [
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ],
      SubagentStop: [
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]},
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"}
      ],
      UserPromptSubmit: [
        {hooks: [{command: ping_cmd("codex"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("codex"), type: "command"}]}
      ]
    }
  '
}

generate_claude_hooks() {
  jq -n --arg ping "$PING_BRIDGE" --arg agentpet "$AGENTPET_BIN" '
    def ping_cmd($source): "\"" + $ping + "\" --source " + $source;
    def agentpet_cmd($agent): "\"" + $agentpet + "\" hook --agent " + $agent;
    {
      Notification: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      PermissionRequest: [
        {hooks: [{command: ping_cmd("claude"), timeout: 86400, type: "command"}], matcher: "*"}
      ],
      PostToolUse: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}], matcher: "*"}
      ],
      PreCompact: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}], matcher: "auto"},
        {hooks: [{command: ping_cmd("claude"), type: "command"}], matcher: "manual"}
      ],
      PreToolUse: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}], matcher: "*"},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      SessionEnd: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}]},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      SessionStart: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}]},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      Stop: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}]},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      SubagentStop: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}]},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ],
      UserPromptSubmit: [
        {hooks: [{command: ping_cmd("claude"), type: "command"}]},
        {hooks: [{command: agentpet_cmd("claude"), type: "command"}]}
      ]
    }
  '
}

generate_gemini_hooks() {
  jq -n --arg ping "$PING_BRIDGE" --arg agentpet "$AGENTPET_BIN" '
    def ping_cmd($source): "\"" + $ping + "\" --source " + $source;
    def agentpet_cmd($agent): "\"" + $agentpet + "\" hook --agent " + $agent;
    def both:
      [
        {hooks: [{command: agentpet_cmd("gemini"), type: "command"}]},
        {hooks: [{command: ping_cmd("gemini"), type: "command"}]}
      ];
    {
      AfterAgent: both,
      AfterTool: both,
      BeforeAgent: both,
      BeforeTool: both,
      Notification: both,
      SessionEnd: both,
      SessionStart: both
    }
  '
}

merge_hooks_into_json_file() {
  local target="$1"
  local hook_generator="$2"
  local hooks_tmp out_tmp

  hooks_tmp="$(mktemp)"
  out_tmp="$(mktemp)"
  "$hook_generator" >"$hooks_tmp"

  if [[ -s "$target" ]] && jq empty "$target" >/dev/null 2>&1; then
    jq --slurpfile hooks "$hooks_tmp" '.hooks = $hooks[0]' "$target" >"$out_tmp"
  else
    jq --slurpfile hooks "$hooks_tmp" -n '{hooks: $hooks[0]}' >"$out_tmp"
  fi

  install_file_from_tmp "$out_tmp" "$target" "644"
  rm -f "$hooks_tmp" "$out_tmp"
}

ensure_codex_config() {
  local tmp
  tmp="$(mktemp)"

  if [[ "$DRY_RUN" -eq 0 ]]; then
    mkdir -p "$HOME/.codex"
  fi
  if [[ -e "$CODEX_CONFIG" ]]; then
    cp "$CODEX_CONFIG" "$tmp"
  else
    : >"$tmp"
  fi

  if ! grep -Eq '^service_tier[[:space:]]*=[[:space:]]*"default"' "$tmp"; then
    local with_service
    with_service="$(mktemp)"
    {
      printf 'service_tier = "default"\n'
      cat "$tmp"
    } >"$with_service"
    mv "$with_service" "$tmp"
  fi

  local project_header
  project_header="[projects.\"$REPO_ROOT\"]"
  if ! grep -Fqx "$project_header" "$tmp"; then
    {
      printf '\n%s\n' "$project_header"
      printf 'trust_level = "trusted"\n'
    } >>"$tmp"
  fi

  install_file_from_tmp "$tmp" "$CODEX_CONFIG" "600"
  rm -f "$tmp"
}

write_provider_hooks() {
  merge_hooks_into_json_file "$CODEX_HOOKS" generate_codex_hooks
  merge_hooks_into_json_file "$CLAUDE_SETTINGS" generate_claude_hooks
  merge_hooks_into_json_file "$GEMINI_SETTINGS" generate_gemini_hooks
  ensure_codex_config
}

verify_json_file() {
  local target="$1"
  if [[ ! -s "$target" ]]; then
    warn "Missing or empty: $target"
    return 1
  fi
  jq empty "$target"
}

verify_hooks() {
  local failures=0

  verify_json_file "$CODEX_HOOKS" || failures=$((failures + 1))
  verify_json_file "$CLAUDE_SETTINGS" || failures=$((failures + 1))
  verify_json_file "$GEMINI_SETTINGS" || failures=$((failures + 1))

  if [[ "$failures" -eq 0 ]]; then
    log "Codex hook matrix:"
    jq -r '.hooks | to_entries[] | .key as $event | .value[]? | .hooks[]? | [$event, .command] | @tsv' "$CODEX_HOOKS"
  fi

  if [[ ! -x "$PING_BRIDGE" ]]; then
    warn "Ping-Island bridge wrapper is not executable: $PING_BRIDGE"
    failures=$((failures + 1))
  fi

  if [[ "$RUN_DOCTOR" -eq 1 ]]; then
    if command -v codex >/dev/null 2>&1; then
      codex doctor --summary --ascii --no-color || true
    else
      warn "Skipping codex doctor: codex not found on PATH."
    fi
  fi

  if [[ "$failures" -gt 0 ]]; then
    die "Verification failed with $failures issue(s)."
  fi

  log "Verification complete."
}

main() {
  check_prereqs

  if [[ "$VERIFY_ONLY" -eq 1 ]]; then
    verify_hooks
    exit 0
  fi

  confirm_write

  write_ping_island_files
  write_provider_hooks

  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "Dry run complete. No files were written."
    exit 0
  fi

  verify_hooks

  cat <<EOF

Next steps:
  1. Start Claude Code, Codex, and Antigravity once on this device.
  2. In Codex, approve/trust hook prompts so ~/.codex/config.toml gets local trusted_hash entries.
  3. Run:
       codex doctor --summary --ascii --no-color

Reminder:
  Do not commit ~/.claude, ~/.codex, ~/.gemini, or ~/.ping-island into this repo.
EOF
}

main "$@"
