# (C) Autopilot Overnight Drain — 2026-09-27-23

> **Mode:** Path A (mechanical Python orchestrator)
> **Trigger:** unattended (launchd UserAgent)
> **Started:** 2026-09-27 23:??

---

## Raw run log

```
[23:47:33] === Autopilot drain start 2026-09-27 ===
[23:47:33] AUTOPILOT_ROOT: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research
[23:47:33] queue: /Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/topics-queue.md
[23:47:33] pending topics: 1
[23:47:33]   1. Claude Managed Agents in production — the founders' roundtable (outcomes / memory / sandboxing) (+ 1 anchor)
[23:47:33] will drain: 1
[23:47:33] --- Drain: Claude Managed Agents in production — the founders' roundtable (outcomes / memory / sandboxing)
[23:47:33]   query: Claude Managed Agents
[23:47:33]   slug:  claude-managed-agents-in-production-the-founders-r
[23:47:33]   anchors: 1 URL(s) declared — will force-include
[23:47:33]   step 0/5: probe anchor URLs
[23:48:01]     ✓ anchor: [20260908] How founders build on Claude Managed Agents — Claude (110,329 views)
[23:48:01]   step 1/5: yt-search (filling 5 of 6 slots; 1 from anchors)
[01:05:45]     got 15 videos
[01:05:45]   step 2/5: select top sources
[01:05:45]     picked 6 (1 anchor + 5 yt-search):
[01:05:45]       1. [ANCHOR] [20260908] How founders build on Claude Managed Agents — Claude (110,329 views)
[01:05:45]       2. [20260630] How to Build an AI Agent with Claude Code (Claude AI Agent T — AI Master (516,451 views)
[01:05:45]       3. [20260409] Claude Managed Agents is AMAZING. Here's How to Build Any Ag — Build Great Products (92,197 views)
[01:05:45]       4. [20260409] Claude Managed Agents Full Tutorial: How to Setup Your First — Bart Slodyczka (49,169 views)
[01:05:45]       5. [20260408] I Tested Claude's New Managed Agents... What You Need To Kno — Nate Herk | AI Automation (178,364 views)
[01:05:45]       6. [20260410] Claude Managed Agents Clearly Explained (and why it matters) — Corey Ganim (6,794 views)
[01:05:45]   anchor validation: PASS (1/1 declared anchors in bundle, overlap=100%)
[01:05:45]   step 3/5: notebooklm bundle
[01:05:48]     retry 1/2 after rc=1: 
[01:05:55]     retry 2/2 after rc=1: 
[01:06:01]   create failed: 
[01:06:01]   ABORT: notebook create failed
[01:06:01] === Done. drained=0 of 1 ===
```
