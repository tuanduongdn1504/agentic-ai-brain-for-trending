#!/usr/bin/env python3
"""Regression test for the anchor-validation grader in bin/autopilot-drain.py.

This is pilot A1 from output/(C) 2026-06-16-prompt-evaluation-pilot-methods.md —
the first inhabitant of evals/, applying the Anthropic "Grading with AI" lesson
(wiki/prompt-evaluation/) as a deterministic CODE grader + fail-loud gate.

WHY each case matters (Rule 9 — tests verify intent, not just behavior):
  - The 2026-05-14 anchor-miss incident ingested off-target bundles because
    operator-declared anchors were silently dropped. validate_anchors() turns
    that silent drop into a loud, objective signal; drain_topic() halts on it.
  - If these tests ever fail, the overnight cron could resume ingesting
    off-target bundles (FAIL path) or wrongly halt good runs (PASS path).

Run:   python evals/test_anchor_validation.py      (exits non-zero on failure → CI-ready)
No network, no API cost, deterministic.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("drain", ROOT / "bin" / "autopilot-drain.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

failures = []


def check(name, cond):
    print(f"  [{'✓' if cond else '✗'}] {name}")
    if not cond:
        failures.append(name)


def fake_video(vid, ch):
    return {"url": f"https://www.youtube.com/watch?v={vid}", "title": f"vid {vid}",
            "channel": ch, "channel_followers": 100_000, "view_count": 50_000,
            "upload_date": m.dt.date.today().strftime("%Y%m%d"), "duration": 700}


print("== _video_id: URL-form robustness ==")
check("watch?v= form", m._video_id("https://www.youtube.com/watch?v=nYMcPrnRzhI") == "nYMcPrnRzhI")
check("youtu.be form", m._video_id("https://youtu.be/GjakSOir2dE") == "GjakSOir2dE")
check("trailing &param", m._video_id("https://www.youtube.com/watch?v=nYMcPrnRzhI&t=10s") == "nYMcPrnRzhI")

print("== validate_anchors: the four verdicts ==")
vid = lambda u: {"url": u}
A = "https://www.youtube.com/watch?v=AAAAAAAAAAA"
B = "https://youtu.be/BBBBBBBBBBB"
C = "https://www.youtube.com/watch?v=CCCCCCCCCCC"
check("n/a when no anchors declared", m.validate_anchors([], [vid(C)])["verdict"] == "n/a")
check("PASS when included (even with &param)", m.validate_anchors([A], [vid(A + "&t=5"), vid(C)])["verdict"] == "PASS")
check("WARN at exactly 50% included", m.validate_anchors([A, B], [vid(A), vid(C)])["verdict"] == "WARN")
check("FAIL below threshold", m.validate_anchors([A, B], [vid(C)])["verdict"] == "FAIL")
check("FAIL when the single declared anchor is dropped", m.validate_anchors([A], [vid(C)])["verdict"] == "FAIL")

print("== drain_topic wiring: fail-loud gate halts before NotebookLM ==")
nb_calls = {"n": 0}
m.nb_create = lambda name: nb_calls.__setitem__("n", nb_calls["n"] + 1) or "fake-nb"
m.yt_meta = lambda url: None  # declared anchor is unreachable
m.yt_search = lambda q: [fake_video(f"F{i}FFFFFFFFF", f"C{i}") for i in range(1, 5)]
r = m.drain_topic({"heading": "ZZ test dead anchor", "query": "t",
                   "anchors": ["https://www.youtube.com/watch?v=DEADBEEF123"]}, dry_run=False)
check("real drain with dead anchor returns None (aborted)", r is None)
check("NotebookLM was never reached (0 nb_create calls)", nb_calls["n"] == 0)

print("== drain_topic wiring: PASS proceeds (stops only at dry-run) ==")
G = "https://www.youtube.com/watch?v=GOODANCHOR1"
m.yt_meta = lambda url: {**fake_video("GOODANCHOR1", "AnchorCh"), "anchor": True}
r2 = m.drain_topic({"heading": "ZZ test good anchor", "query": "t", "anchors": [G]}, dry_run=True)
check("good-anchor dry-run returns None (stopped at dry-run, not aborted)", r2 is None)

print()
if failures:
    print(f"FAILED: {len(failures)} check(s): {failures}")
    sys.exit(1)
print("ALL ANCHOR-VALIDATION CHECKS PASSED ✅")
