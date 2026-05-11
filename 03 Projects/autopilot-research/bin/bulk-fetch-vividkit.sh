#!/usr/bin/env bash
# Bulk-fetch all vividkit.dev /vi/guides/* pages.
# Tier 0 sufficient (no Cloudflare on vividkit per 2026-05-11 probe).
set -euo pipefail

# Self-locate from script location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUT_DIR="$PROJECT_ROOT/raw/vividkit-guides"
mkdir -p "$OUT_DIR"

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

SLUGS=(
  what-is-claudekit
  cli
  claude-mechanics
  how-ck-works
  inside-claudekit
  commands
  workflows
  permissions
  hooks
  flowchart
  ccs
  ck-with-codex
  coexistence
  fix-logs
  ide-config
  migrate
  mobile-coding
  promotions
  remote-control
  session-recovery
  uiux
)

echo "Fetching ${#SLUGS[@]} guides → $OUT_DIR/"
for slug in "${SLUGS[@]}"; do
  url="https://www.vividkit.dev/vi/guides/$slug"
  html="$OUT_DIR/${slug}.html"
  status=$(curl -sL -A "$UA" \
    -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
    -H "Accept-Language: vi-VN,vi;q=0.9,en;q=0.8" \
    --compressed \
    -o "$html" \
    -w "%{http_code}|%{size_download}" \
    "$url")
  echo "  $slug → $status"
done

echo ""
echo "Converting to clean MD..."
for slug in "${SLUGS[@]}"; do
  html="$OUT_DIR/${slug}.html"
  md="$OUT_DIR/${slug}.md"
  if [ -f "$html" ]; then
    "$PROJECT_ROOT/.venv/bin/python" "$PROJECT_ROOT/bin/html-to-clean-md.py" \
      "$html" "$md" \
      --url "https://www.vividkit.dev/vi/guides/$slug" \
      --selector "main" \
      2>&1 | tail -1
  fi
done

echo ""
echo "Total MD files written:"
ls "$OUT_DIR"/*.md | wc -l
