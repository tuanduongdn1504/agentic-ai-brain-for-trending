#!/usr/bin/env bash
# Fetch a YouTube caption track, PREFERRING the human-authored one.
#
# YouTube exposes two kinds of track and yt-dlp's flags choose between them:
#   --write-subs       → human-authored ("Available subtitles")
#   --write-auto-subs  → ASR machine transcript ("Available automatic captions")
# Both emit `Kind: captions` in the VTT header, so the file itself does not
# announce which you got. Pulling ASR when a human track exists silently
# corrupts product names, person names and quotes — and every downstream
# scorecard then grades against a corrupted transcript.
#
# Usage: fetch-captions.sh <video-url-or-id> <out-basename> [lang]
set -euo pipefail

URL="${1:?usage: fetch-captions.sh <url-or-id> <out-basename> [lang]}"
OUT="${2:?usage: fetch-captions.sh <url-or-id> <out-basename> [lang]}"
LANG_="${3:-en}"

case "$URL" in http*) ;; *) URL="https://www.youtube.com/watch?v=${URL}" ;; esac

# Do NOT pipe yt-dlp into grep here: `grep -q` exits on first match, SIGPIPEs
# yt-dlp, and `pipefail` then reports the fetch as failed even when it wrote the
# file — silently downgrading every video to ASR. Test the artifact, not the log.
rm -f "${OUT}.${LANG_}.vtt"
yt-dlp --skip-download --write-subs --sub-langs "$LANG_" --sub-format vtt \
    -o "$OUT" "$URL" >/dev/null 2>&1 || true

if [ -s "${OUT}.${LANG_}.vtt" ]; then
  echo "track=human file=${OUT}.${LANG_}.vtt"
  exit 0
fi

echo "NOTE: no human-authored '${LANG_}' track; falling back to ASR auto-subs." >&2
yt-dlp --skip-download --write-auto-subs --sub-langs "$LANG_" --sub-format vtt \
    -o "$OUT" "$URL" >/dev/null 2>&1 || true

if [ -s "${OUT}.${LANG_}.vtt" ]; then
  echo "track=asr file=${OUT}.${LANG_}.vtt"
  echo "WARNING: ASR track — quotes are NOT safe to grade verbatim." >&2
  exit 0
fi

echo "ERROR: no '${LANG_}' caption track of either kind for ${URL}" >&2
exit 1
