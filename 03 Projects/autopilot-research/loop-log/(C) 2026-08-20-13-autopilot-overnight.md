# (C) Autopilot Overnight Drain — 2026-08-20-13

> **Mode:** Path A (mechanical Python orchestrator)
> **Trigger:** unattended (launchd UserAgent)
> **Started:** 2026-08-20 13:??

---

## Raw run log

```
[13:22:39] === Autopilot drain start 2026-08-20 ===
[13:22:39] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[13:22:39] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[13:22:39] pending topics: 1
[13:22:39]   1. Local LLM coding on Apple Silicon — the 64GB Mac mini M4 middle of the hardware ladder (+ 1 anchor)
[13:22:39] will drain: 1
[13:22:39] --- Drain: Local LLM coding on Apple Silicon — the 64GB Mac mini M4 middle of the hardware ladder
[13:22:39]   query: local LLM coding agent Mac mini M4 64GB RAM offline
[13:22:39]   slug:  local-llm-coding-on-apple-silicon-the-64gb-mac-min
[13:22:39]   anchors: 1 URL(s) declared — will force-include
[13:22:39]   step 0/5: probe anchor URLs
[13:22:41]     ✓ anchor: [20260819] Thử local LLM, coding trên Mac mini M4, 64GB ram | quanIT — Quân IT (1,755 views)
[13:22:41]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[13:22:58]     got 15 videos
[13:22:58]   step 2/5: select top sources
[13:22:58]     picked 6 (1 anchor + 5 yt-search):
[13:22:58]       1. [ANCHOR] [20260819] Thử local LLM, coding trên Mac mini M4, 64GB ram | quanIT — Quân IT (1,755 views)
[13:22:58]       2. [20260301] The Unbeatable Local AI Coding Workflow (Full 2026 Setup) — Zen van Riel (259,982 views)
[13:22:58]       3. [20260630] Finally, The CORRECT Way to Run Local AI on a Mac — Samuel Gregory (59,285 views)
[13:22:58]       4. [20260618] Local AI Coding is Finally Good Enough — ForrestKnight (179,582 views)
[13:22:58]       5. [20260522] M4 Pro Mac Mini 24GB RAM vs Local LLMs: Can It Handle It? — WEBdoze (7,291 views)
[13:22:58]       6. [20260610] The Best LOCAL Agentic Coding Workflow (Complete Guide) — Tech With Tim (179,322 views)
[13:22:58]   anchor validation: PASS (1/1 declared anchors in bundle, overlap=100%)
[13:22:58]   DRY RUN — stopping here
[13:22:58] === Done. drained=0 of 1 ===
```
