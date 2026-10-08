# (C) Autopilot Overnight Drain — 2026-09-14-23

> **Mode:** Path A (mechanical Python orchestrator)
> **Trigger:** unattended (launchd UserAgent)
> **Started:** 2026-09-14 23:??

---

## Raw run log

```
[23:54:08] === Autopilot drain start 2026-09-14 ===
[23:54:08] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[23:54:08] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[23:54:08] pending topics: 1
[23:54:08]   1. Claude Managed Agents in production — the founders' roundtable (outcomes / memory / sandboxing) (+ 1 anchor)
[23:54:08] will drain: 1
[23:54:08] --- Drain: Claude Managed Agents in production — the founders' roundtable (outcomes / memory / sandboxing)
[23:54:08]   query: Claude Managed Agents
[23:54:08]   slug:  claude-managed-agents-in-production-the-founders-r
[23:54:08]   anchors: 1 URL(s) declared — will force-include
[23:54:08]   step 0/5: probe anchor URLs
[23:54:41]     ✓ anchor: [20260908] How founders build on Claude Managed Agents — Claude (90,668 views)
[23:54:41]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[01:23:56]     got 15 videos
[01:23:56]   step 2/5: select top sources
[01:23:56]     picked 6 (1 anchor + 5 yt-search):
[01:23:56]       1. [ANCHOR] [20260908] How founders build on Claude Managed Agents — Claude (90,668 views)
[01:23:56]       2. [20260630] How to Build an AI Agent with Claude Code (Claude AI Agent T — AI Master (384,549 views)
[01:23:56]       3. [20260409] Claude Managed Agents is AMAZING. Here's How to Build Any Ag — Build Great Products (90,863 views)
[01:23:56]       4. [20260409] Claude Managed Agents Full Tutorial: How to Setup Your First — Bart Slodyczka (47,197 views)
[01:23:56]       5. [20260408] I Tested Claude's New Managed Agents... What You Need To Kno — Nate Herk | AI Automation (177,254 views)
[01:23:56]       6. [20260526] Ship your first Managed Agent — Claude (87,043 views)
[01:23:56]   anchor validation: PASS (1/1 declared anchors in bundle, overlap=100%)
[01:23:56]   step 3/5: notebooklm bundle
[01:24:00]     retry 1/2 after rc=1: 
[01:29:42]     retry 2/2 after rc=1: 
[01:29:49]   create failed: 
[01:29:49]   ABORT: notebook create failed
[01:29:49] === Done. drained=0 of 1 ===
```
