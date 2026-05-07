#!/usr/bin/env python3
"""
Autopilot drain — Path A (mechanical Python orchestrator).

Reads raw/topics-queue.md, processes every topic with Status:pending, and
writes one analysis file per topic to raw/<date>-<slug>.md. Updates queue
in-place to move drained topics to ## Completed section.

Output per topic: yt-search top-15 → auto-pick top 6 → NotebookLM bundle
+ summary + 4 asks (Trends / Outliers / Gaps / Key Takeaways).

NO synthesis to wiki articles — that's the next-morning compile step.

Designed for unattended overnight execution. Idempotent: existing raw
output files are skipped (if a topic was partially drained, re-running
picks up where it left off).

Usage:
    python bin/autopilot-drain.py             # drain all pending topics
    python bin/autopilot-drain.py --max 1     # drain just the first pending
    python bin/autopilot-drain.py --dry-run   # show what would be drained, no calls
"""
import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("AUTOPILOT_ROOT", Path(__file__).parent.parent))
QUEUE_FILE = PROJECT_ROOT / "raw" / "topics-queue.md"
RAW_DIR = PROJECT_ROOT / "raw"
LOOP_LOG_DIR = PROJECT_ROOT / "loop-log"

TODAY = dt.date.today().isoformat()
NOW_HOUR = dt.datetime.now().strftime("%H")

YT_SEARCH_N = 15
SOURCES_PER_TOPIC = 6
RECENCY_MONTHS = 6
MIN_VIEWS = 1000
MIN_DURATION_SEC = 60 * 5
NOTEBOOKLM_RETRY = 2

# ----------------------------------------------------------------------
# Logging
# ----------------------------------------------------------------------

LOG_LINES: list[str] = []


def log(msg: str, also_print: bool = True):
    stamp = dt.datetime.now().strftime("%H:%M:%S")
    line = f"[{stamp}] {msg}"
    LOG_LINES.append(line)
    if also_print:
        print(line, flush=True)


def flush_loop_log():
    LOOP_LOG_DIR.mkdir(parents=True, exist_ok=True)
    out = LOOP_LOG_DIR / f"(C) {TODAY}-{NOW_HOUR}-autopilot-overnight.md"
    header = (
        f"# (C) Autopilot Overnight Drain — {TODAY}-{NOW_HOUR}\n\n"
        f"> **Mode:** Path A (mechanical Python orchestrator)\n"
        f"> **Trigger:** unattended (launchd UserAgent)\n"
        f"> **Started:** {TODAY} {NOW_HOUR}:??\n\n"
        f"---\n\n"
        f"## Raw run log\n\n```\n"
    )
    footer = "\n```\n"
    body = "\n".join(LOG_LINES)
    out.write_text(header + body + footer, encoding="utf-8")
    print(f"\nLoop log: {out}")


# ----------------------------------------------------------------------
# Queue parsing
# ----------------------------------------------------------------------

def parse_queue() -> tuple[list[dict], str]:
    """Return (pending_topics, raw_text). Each topic: {heading, query, notes, raw_block}."""
    if not QUEUE_FILE.exists():
        log(f"ERROR: no queue file at {QUEUE_FILE}")
        return [], ""
    text = QUEUE_FILE.read_text(encoding="utf-8")

    # Split at "## Completed" marker (only pending lives above it)
    parts = re.split(r"^## Completed\b", text, maxsplit=1, flags=re.MULTILINE)
    pending_section = parts[0]

    topics = []
    # Match "## <heading>\n\n... block ..." up to the next "## " or end-of-section
    pattern = re.compile(r"^## (?!Completed)(.+?)\n\n(.*?)(?=\n## |\Z)", re.DOTALL | re.MULTILINE)
    for m in pattern.finditer(pending_section):
        heading = m.group(1).strip()
        block = m.group(2)
        # extract query (in backticks)
        qmatch = re.search(r"\*\*Query:\*\*\s*`([^`]+)`", block)
        if not qmatch:
            log(f"  skip (no Query in block): {heading}")
            continue
        status_match = re.search(r"\*\*Status:\*\*\s*(\w+)", block)
        status = status_match.group(1).lower() if status_match else "unknown"
        if status != "pending":
            continue
        topics.append({
            "heading": heading,
            "query": qmatch.group(1).strip(),
            "raw_block": "## " + heading + "\n\n" + block.rstrip(),
        })
    return topics, text


def slugify(s: str, maxlen: int = 50) -> str:
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[\s_-]+", "-", s)
    return s[:maxlen].strip("-") or "untitled"


def move_topic_to_completed(text: str, topic: dict, raw_path: Path, notebook_id: str) -> str:
    """Remove topic block from pending area + append to Completed section."""
    block_pattern = re.compile(
        r"## " + re.escape(topic["heading"]) + r"\n\n.*?(?=\n## |\Z)",
        re.DOTALL,
    )
    new_text = block_pattern.sub("", text, count=1)
    # Clean up doubled blank lines left behind
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)

    completion_entry = (
        f"\n### {topic['heading']} ✅\n"
        f"- **Drained:** {TODAY} by overnight orchestrator\n"
        f"- **Raw analysis:** `{raw_path.relative_to(PROJECT_ROOT)}`\n"
        f"- **NotebookLM:** `{notebook_id}`\n"
    )

    # Append before end of file (after the "_(none yet)_" placeholder if present)
    if "_(none yet)_" in new_text:
        new_text = new_text.replace("_(none yet)_", completion_entry.strip())
    else:
        # Insert after "## Completed\n" marker
        new_text = re.sub(
            r"(## Completed\s*\n)",
            r"\1" + completion_entry,
            new_text,
            count=1,
        )
    return new_text


# ----------------------------------------------------------------------
# yt-dlp search + selection
# ----------------------------------------------------------------------

def yt_search(query: str) -> list[dict]:
    """Run yt-dlp and return list of video dicts."""
    cmd = [
        "yt-dlp", "--skip-download",
        "--print", '%(upload_date)s|%(title)s|%(channel)s|%(duration)s|%(view_count)s|%(like_count)s|%(channel_follower_count)s|%(webpage_url)s',
        f"ytsearch{YT_SEARCH_N}:{query}",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        log(f"  yt-dlp timeout for: {query}")
        return []
    if result.returncode != 0:
        log(f"  yt-dlp non-zero exit: {result.stderr[:200]}")
    videos = []
    for line in result.stdout.splitlines():
        parts = line.split("|")
        if len(parts) != 8:
            continue
        upload_date, title, channel, duration, view_count, like_count, follower, url = parts
        try:
            videos.append({
                "upload_date": upload_date,
                "title": title.strip(),
                "channel": channel.strip(),
                "duration": int(duration) if duration.isdigit() else 0,
                "view_count": int(view_count) if view_count.isdigit() else 0,
                "like_count": int(like_count) if like_count.isdigit() else 0,
                "channel_followers": int(follower) if follower.isdigit() else 0,
                "url": url.strip(),
            })
        except ValueError:
            continue
    return videos


def select_videos(videos: list[dict], n: int = SOURCES_PER_TOPIC) -> list[dict]:
    """Filter by recency + minimums, score, return top N."""
    cutoff = (dt.date.today() - dt.timedelta(days=RECENCY_MONTHS * 30)).strftime("%Y%m%d")
    filtered = [
        v for v in videos
        if v["upload_date"] >= cutoff
        and v["view_count"] >= MIN_VIEWS
        and v["duration"] >= MIN_DURATION_SEC
    ]
    if len(filtered) < n:
        # Fall back: relax recency
        log(f"  only {len(filtered)} pass recency filter; relaxing")
        filtered = [
            v for v in videos
            if v["view_count"] >= MIN_VIEWS and v["duration"] >= MIN_DURATION_SEC
        ]

    # Score: log(views) + engagement_ratio * 5 (engagement = views/followers if followers known)
    import math
    for v in filtered:
        eng_ratio = v["view_count"] / v["channel_followers"] if v["channel_followers"] > 0 else 0.5
        recency_days = (dt.date.today() - dt.datetime.strptime(v["upload_date"], "%Y%m%d").date()).days
        recency_bonus = max(0, 1 - (recency_days / 365))
        v["score"] = math.log10(max(1, v["view_count"])) + eng_ratio * 3 + recency_bonus * 2

    # Channel diversity: cap 2 videos per channel max
    filtered.sort(key=lambda x: -x["score"])
    picked = []
    channel_counts: dict[str, int] = {}
    for v in filtered:
        if channel_counts.get(v["channel"], 0) >= 2:
            continue
        picked.append(v)
        channel_counts[v["channel"]] = channel_counts.get(v["channel"], 0) + 1
        if len(picked) >= n:
            break
    return picked


# ----------------------------------------------------------------------
# NotebookLM CLI wrappers
# ----------------------------------------------------------------------

def nb(*args: str, timeout: int = 300, capture: bool = True, retries: int = 0) -> tuple[int, str, str]:
    """Run notebooklm <args>. Returns (rc, stdout, stderr)."""
    cmd = ["notebooklm"] + list(args)
    last_err = ""
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(cmd, capture_output=capture, text=True, timeout=timeout)
            if r.returncode == 0:
                return r.returncode, r.stdout, r.stderr
            last_err = (r.stderr or "")[:300]
            if attempt < retries:
                log(f"    retry {attempt+1}/{retries} after rc={r.returncode}: {last_err[:80]}")
                time.sleep(5)
        except subprocess.TimeoutExpired:
            last_err = f"timeout after {timeout}s"
            if attempt < retries:
                log(f"    retry {attempt+1}/{retries} after timeout")
    return 1, "", last_err


def nb_create(name: str) -> str | None:
    rc, out, err = nb("create", name, retries=NOTEBOOKLM_RETRY)
    if rc != 0:
        log(f"  create failed: {err}")
        return None
    m = re.search(r"Created notebook:\s+([0-9a-f-]+)", out)
    return m.group(1) if m else None


def nb_use(nb_id: str) -> bool:
    rc, _, err = nb("use", nb_id[:12], retries=NOTEBOOKLM_RETRY)
    return rc == 0


def nb_add_source(url: str) -> bool:
    rc, _, err = nb("source", "add", url, timeout=120, retries=NOTEBOOKLM_RETRY)
    if rc != 0:
        log(f"    add source failed for {url}: {err[:80]}")
    return rc == 0


def nb_wait_ready(expected_count: int, max_wait_sec: int = 300) -> bool:
    deadline = time.time() + max_wait_sec
    while time.time() < deadline:
        rc, out, _ = nb("source", "list", "--json", timeout=60)
        if rc == 0:
            try:
                statuses = [s.get("status") for s in json.loads(out).get("sources", [])]
                ready = sum(1 for s in statuses if s == "ready")
                if ready >= expected_count and len(statuses) >= expected_count:
                    return True
            except json.JSONDecodeError:
                pass
        time.sleep(5)
    return False


def nb_summary() -> str:
    rc, out, err = nb("summary", timeout=180, retries=NOTEBOOKLM_RETRY)
    if rc != 0:
        return f"[summary failed: {err[:120]}]"
    # Strip CLI noise above the actual content
    cleaned = re.sub(r"^.*?(?=Summary:|\bThe )", "", out, flags=re.DOTALL)
    return cleaned.strip()


def nb_ask(question: str) -> str:
    rc, out, err = nb("ask", question, timeout=240, retries=NOTEBOOKLM_RETRY)
    if rc != 0:
        return f"[ask failed: {err[:120]}]"
    cleaned = re.sub(r"^.*?(?=Answer:|Continuing|\b[A-Z])", "", out, flags=re.DOTALL)
    return cleaned.strip()


# ----------------------------------------------------------------------
# Per-topic drain
# ----------------------------------------------------------------------

ASK_QUESTIONS = [
    ("Trends", "What are the dominant trends and shared patterns across these videos? Focus on tactical practices, tooling choices, and recurring techniques that multiple speakers advocate. Be specific about who said what."),
    ("Outliers", "Where do the speakers disagree or diverge? Identify outlier opinions, contrarian takes, and places where one speaker contradicts another. Be specific about who said what."),
    ("Gaps", "What's NOT covered in these videos that someone implementing this in production should know? Identify gaps and 5-7 specific follow-up topics worth investigating."),
    ("Takeaways", "Synthesize 7-10 actionable rules or configurations a developer should adopt from these videos. Each takeaway 1-2 sentences, specific, attributed where possible."),
]


def drain_topic(topic: dict, dry_run: bool = False) -> dict | None:
    heading = topic["heading"]
    query = topic["query"]
    slug = slugify(heading)
    out_path = RAW_DIR / f"{TODAY}-{slug}.md"

    if out_path.exists() and out_path.stat().st_size > 1000:
        log(f"  SKIP (already drained): {out_path.name}")
        return None

    log(f"--- Drain: {heading}")
    log(f"  query: {query}")
    log(f"  slug:  {slug}")

    log("  step 1/5: yt-search")
    videos = yt_search(query)
    log(f"    got {len(videos)} videos")
    if len(videos) < 3:
        log("  ABORT: insufficient yt results")
        return None

    log("  step 2/5: select top sources")
    picked = select_videos(videos, SOURCES_PER_TOPIC)
    log(f"    picked {len(picked)}:")
    for i, v in enumerate(picked, 1):
        log(f"      {i}. [{v['upload_date']}] {v['title'][:60]} — {v['channel']} ({v['view_count']:,} views)")

    if dry_run:
        log("  DRY RUN — stopping here")
        return None

    log("  step 3/5: notebooklm bundle")
    nb_name = f"autopilot-overnight-{slug}-{TODAY}"
    nb_id = nb_create(nb_name)
    if not nb_id:
        log("  ABORT: notebook create failed")
        return None
    log(f"    notebook: {nb_id}")
    if not nb_use(nb_id):
        log("  ABORT: notebook use failed")
        return None

    added = 0
    for v in picked:
        if nb_add_source(v["url"]):
            added += 1
    log(f"    added {added}/{len(picked)} sources")
    if added == 0:
        log("  ABORT: no sources added")
        return None

    log("  step 4/5: wait for ready")
    if not nb_wait_ready(added):
        log("  WARN: not all sources ready, proceeding anyway")

    log("  step 5/5: analysis (1 summary + 4 asks)")
    sections = []
    sections.append(("1. Summary", nb_summary()))
    for label, q in ASK_QUESTIONS:
        log(f"    asking: {label}")
        sections.append((f"{len(sections)+1}. {label}", nb_ask(q)))

    # Write output
    body = [
        f"# {heading}",
        "",
        f"**Notebook:** {nb_id}",
        f"**Sources:** {added} YouTube videos",
        f"**Generated:** {TODAY} (overnight orchestrator)",
        f"**Query:** `{query}`",
        "",
        "## Sources",
        "",
    ]
    for i, v in enumerate(picked[:added], 1):
        body.append(f"{i}. [{v['upload_date']}] **{v['channel']}** — {v['title']}")
        body.append(f"   - {v['url']}")
        body.append(f"   - {v['view_count']:,} views, {v['duration']//60}:{v['duration']%60:02d} duration")
    body.append("")
    body.append("---")
    body.append("")
    for title, content in sections:
        body.append(f"## {title}")
        body.append("")
        body.append(content)
        body.append("")
        body.append("---")
        body.append("")
    out_path.write_text("\n".join(body), encoding="utf-8")
    log(f"  ✅ wrote {out_path} ({out_path.stat().st_size:,} bytes)")
    return {"out_path": out_path, "notebook_id": nb_id, "topic": topic}


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Autopilot overnight drain")
    parser.add_argument("--max", type=int, default=None, help="max topics to drain (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="show plan without making API calls")
    args = parser.parse_args()

    log(f"=== Autopilot drain start {TODAY} ===")
    log(f"AUTOPILOT_ROOT: {PROJECT_ROOT}")
    log(f"queue: {QUEUE_FILE}")

    topics, raw_text = parse_queue()
    log(f"pending topics: {len(topics)}")
    for i, t in enumerate(topics, 1):
        log(f"  {i}. {t['heading']}")

    if not topics:
        log("Nothing to drain. Exiting.")
        flush_loop_log()
        return

    targets = topics if args.max is None else topics[: args.max]
    log(f"will drain: {len(targets)}")

    drained = []
    for t in targets:
        try:
            result = drain_topic(t, dry_run=args.dry_run)
            if result:
                drained.append(result)
        except Exception as e:
            log(f"  EXCEPTION on '{t['heading']}': {type(e).__name__}: {e}")

    if drained and not args.dry_run:
        log(f"--- updating queue ({len(drained)} drained)")
        cur_text = QUEUE_FILE.read_text(encoding="utf-8")
        for d in drained:
            cur_text = move_topic_to_completed(
                cur_text, d["topic"], d["out_path"], d["notebook_id"]
            )
        QUEUE_FILE.write_text(cur_text, encoding="utf-8")
        log("  queue updated")

    log(f"=== Done. drained={len(drained)} of {len(targets)} ===")
    flush_loop_log()


if __name__ == "__main__":
    main()
