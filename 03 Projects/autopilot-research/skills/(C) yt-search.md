# Skill: yt-search

> **Type:** Worker skill (project-local to autopilot-research)
> **Created:** 2026-04-29
> **Backend:** `yt-dlp` (external CLI)
> **Reused by:** `(C) yt-pipeline.md`, `(C) autopilot-research-routine.md`

---

## Purpose

Search YouTube and return structured video results with engagement metadata. Filters to recent uploads by default (last 6 months). Output is human-readable but machine-parseable, optimised for downstream selection by `yt-pipeline`.

---

## Contract

| Aspect | Value |
|--------|-------|
| **Input** | search query string + optional `--months <N>` (default 6) + optional `--limit <N>` (default 20) |
| **Backend** | `yt-dlp ytsearch<N>:"<query>"` with `--write-info-json --skip-download` |
| **Output** | structured list of top-N videos with metadata |
| **Side effects** | writes `.info.json` files to a temp dir; cleaned on exit |

---

## Output fields per video

- **Title** — the video title
- **Channel** — channel name
- **Subscriber count** — comma-formatted (e.g., `1,250,000`)
- **View count** — comma-formatted
- **Duration** — `HH:MM:SS` format
- **Upload date** — `YYYY-MM-DD`
- **URL** — full `https://www.youtube.com/watch?v=...` URL
- **Engagement ratio** — `views / subscribers` as percentage (e.g., `12.4%`)

---

## Setup gate

Before invoking, verify dependency:

```bash
which yt-dlp
```

If not found, abort with this message:

> **yt-dlp not installed.** Install via either:
> - macOS: `brew install yt-dlp`
> - Python: `pip install yt-dlp`
>
> After install, retry. yt-search will not estimate or fake results.

---

## Invocation procedure

When invoked with a topic string `<query>`:

1. **Pre-flight:** verify `yt-dlp --version` succeeds.
2. **Build search command:**
   ```bash
   yt-dlp \
     "ytsearch20:<query>" \
     --skip-download \
     --write-info-json \
     --no-warnings \
     -o "/tmp/ytsearch-%(id)s.%(ext)s" \
     --print-json \
     2>/dev/null
   ```
3. **Parse JSON lines** from stdout. Each line is one video's metadata.
4. **Filter by upload date:** drop videos with `upload_date` older than `(today - <months> * 30)` days. Default `<months>` = 6.
5. **Compute engagement ratio:** `view_count / channel.subscriber_count` (handle missing/zero subscribers as `N/A`).
6. **Format output** (see template below).
7. **Cleanup:** `rm /tmp/ytsearch-*.info.json /tmp/ytsearch-*.json` on exit.

---

## Output template

```
═══════════════════════════════════════════════════════════════
 YouTube search results for: "<query>"
 Filter: uploaded ≤ <months> months ago | Limit: <limit>
 Found: <N> matching videos
═══════════════════════════════════════════════════════════════

[1] <title>
    Channel:      <channel> (<sub_count> subscribers)
    Views:        <view_count>
    Duration:     <duration>
    Uploaded:     <upload_date>
    Engagement:   <ratio>%
    URL:          <url>

───────────────────────────────────────────────────────────────

[2] <title>
    ...
```

---

## Edge cases

- **Channel subscriber count hidden:** display as `hidden`; mark engagement as `N/A`
- **No results:** print `No matching videos found.` and exit with code 1
- **Live streams / scheduled premieres:** include but mark as `[LIVE]` or `[UPCOMING]` in the title
- **Age-restricted content:** yt-dlp may omit; skip silently with a count in summary
- **Network failure:** abort, print verbatim error, exit code 2

---

## Constitutional rules

1. **NEVER fake results** — if yt-dlp returns 0 or fewer than requested videos, report the actual count
2. **NEVER skip the upload-date filter** — if a result has no `upload_date`, drop it (don't guess)
3. **NEVER expose `.info.json` paths** in the output — they're internal
4. **ALWAYS clean up** `/tmp/ytsearch-*` files on exit (success or failure)

---

## Examples

### Example 1: basic search

```
yt-search "Claude Code hooks"
```

### Example 2: longer time window

```
yt-search --months 12 "agent frameworks 2026"
```

### Example 3: tight result set

```
yt-search --limit 5 "Andrej Karpathy LLM"
```

---

## Programmatic interface (for yt-pipeline)

When called by `(C) yt-pipeline.md`, return the result as **machine-readable JSON** instead of formatted text. Trigger this mode with `--json` flag. Schema:

```json
{
  "query": "...",
  "filter_months": 6,
  "results": [
    {
      "title": "...",
      "channel": "...",
      "channel_subscribers": 1250000,
      "view_count": 155000,
      "duration_seconds": 723,
      "upload_date": "2026-03-15",
      "url": "https://www.youtube.com/watch?v=...",
      "engagement_ratio": 0.124
    },
    ...
  ]
}
```

This is the preferred interface for downstream automation. The text-formatted output above is for human consumption only.

---

## Next action (per Storm Bear convention)

After running yt-search and reviewing results, the user typically either:
1. Picks a video URL manually and feeds it to `(C) notebooklm.md ingest`
2. Hands the topic to `(C) yt-pipeline.md` for autonomous selection + ingestion of the top 5-8
