#!/usr/bin/env python3
"""
Convert YouTube auto-sub VTT → clean markdown with [MM:SS] timestamps.

Strips the rolling-caption duplicates and inline <c> word-timing tags that
YouTube auto-subs emit. Emits one paragraph per ~15-30 sec of speech.

Usage: vtt-to-md.py <input.vtt> <output.md> [--title "Optional title"]
"""
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple


def parse_cue_time(line):
    m = re.match(r"^(\d+):(\d+):(\d+)\.\d+ -->", line)
    if not m:
        return None
    h, mm, ss = (int(x) for x in m.groups())
    return h * 3600 + mm * 60 + ss


def fmt_mmss(total_sec):
    h, rem = divmod(total_sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def main():
    if len(sys.argv) < 3:
        print("usage: vtt-to-md.py <input.vtt> <output.md> [--title T]", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    title = ""
    if "--title" in sys.argv:
        title = sys.argv[sys.argv.index("--title") + 1]

    cues = []  # type: List[Tuple[int, str]]
    current_time = None  # type: Optional[int]
    for raw in src.read_text(encoding="utf-8").splitlines():
        t = parse_cue_time(raw)
        if t is not None:
            current_time = t
            continue
        if not raw.strip():
            continue
        if raw.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        if "<c>" in raw or "<" in raw and re.search(r"<\d{2}:\d{2}", raw):
            continue
        text = raw.strip()
        if not text:
            continue
        if cues and cues[-1][1] == text:
            continue
        cues.append((current_time or 0, text))

    out = []  # type: List[str]
    if title:
        out.append(f"# {title}\n")
    out.append(f"> Source: {src.name}\n> Converted: {Path(__file__).name}\n> Format: `[MM:SS] line` — verbatim auto-sub, deduplicated, word-timing tags stripped\n")

    paragraph = []  # type: List[str]
    paragraph_start = None  # type: Optional[int]
    PARAGRAPH_SEC = 25
    for t, text in cues:
        if paragraph_start is None:
            paragraph_start = t
        paragraph.append(text)
        if t - paragraph_start >= PARAGRAPH_SEC:
            out.append(f"**[{fmt_mmss(paragraph_start)}]** " + " ".join(paragraph))
            paragraph = []
            paragraph_start = None
    if paragraph and paragraph_start is not None:
        out.append(f"**[{fmt_mmss(paragraph_start)}]** " + " ".join(paragraph))

    dst.write_text("\n\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {dst} — {len(cues)} unique cue lines, {sum(1 for x in out if x.startswith('**['))} timestamped paragraphs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
