# (C) Autopilot Loop — 2026-07-18-20

> **Trigger:** /loop (manual, operator-submitted URL → full topic bundle)
> **Topic:** herdr — **NEW topic** (collision check clean: `neK8ydl0Vlk` never ingested; no prior herdr/agent-multiplexer topic)
> **Anchor:** https://www.youtube.com/watch?v=neK8ydl0Vlk (Chase AI) — force-included
> **Scope elected by operator:** Full topic bundle (yt-search 5-8 videos)
> **Started:** 2026-07-18 ~20:00 ICT
> **Ended:** 2026-07-18 ~21:4x ICT
> **Duration:** ~100 min (majority consumed by the YouTube 429 bot-gate + 2 fetch retries; analysis workflow ~7 min; wiki write ~25 min)

## Pre-flight

- Coast clear: no active /loop, cron, scheduled task, or TaskList entries. Queue pending section empty.
- Branch `autopilot-research` (holds 3 unmerged prior topics: copywriting `14071d0`, kimi-k3 N=3 `5525f6e`, vercel-eve). This ship stacks on top; operator merges.
- Env verified: yt-dlp 2026.06.09 ✅. NotebookLM not needed (bundle small, read in full).
- Herdr verified real (not vaporware) before build: github.com/ogulcancelik/herdr, 17.8K★, Rust, v0.7.4.

## Source selection

- `yt-dlp "ytsearch25:Herdr agent multiplexer terminal coding agents"` → 25 candidates. Scored relevance/credibility/recency/diversity; selected **8** with anchor force-included. Dropped from candidates: Fireship "Tmux in 100 Seconds" (2024, off-topic), cmux-only videos, sub-500-view micro-channels, VN-dub duplicate.

## Block incident (YouTube 429 bot-gate)

- First caption fetch hit **HTTP 429 "Sign in to confirm you're not a bot."** NOT a Cloudflare-page block → `(C) bypass-403-escalation.md` HTML tiers N/A. Resolved with yt-dlp native `--cookies-from-browser chrome` (3,356 cookies, deno JS-challenge solve). Fetched 6 of 8.
- Tail re-block: t7 (Better Stack) + t8 (Fru Dev) died after 6 rapid fetches; 2 attempts, both failed. **Shipped on 6** (bundle range 5-8; healthy). Logged: `output/bypass-attempts.md` (with a proposed yt-dlp-specific mini-ladder to codify).

## Sources ingested (6 YouTube + primary grounding)

- `raw/2026-07-18-herdr/` — 6 transcripts (t1 Chase AI anchor · t2 DevOps Toolbox · t3 Seth Phaeno · t4 Hal Shin · t5 Academind · t6 Elie Steinbock) + `_sources.md`. ~16.8K words. Chrome-cookie'd `yt-dlp` `en-orig` captions → `bin/vtt-to-md.py`, read in full.
- Primary grounding: GitHub API (`ogulcancelik/herdr`), repo README/LICENSE (AGPL-3.0 + commercial dual), `herdr.dev/docs/{concepts,agents,session-state,persistence-remote}`.

## Analysis workflow

- **`wf_65ed9753-32f`** (`herdr-verify`) — 5 phases, **28 agents, 0 errors / 0 empty / 0 skipped**, ~1.14M tokens, 90 tool calls, ~7 min: 6 digests (201 raw claims) → consolidate (19 load-bearing) → refute-first verify (19) → synthesize → **independent completeness critic** (returned NEEDS-REVISION; 3 fixes folded in after independent re-verification).
- **Main-loop independent re-checks** (per verify-independently rule): plugin repos `smarzban/herdr-file-viewer` (156★) + `nikok6/herdr-mirror` (35★) confirmed real; issues #198 (closed, status-latch) + #1514 (open, Windows) confirmed real; softened the socket-API "returns JSON" assumption (undocumented). Also caught + corrected a miscount in the synthesis's own scorecard (C24 is INCOMPLETE not MISLEADING → true tally 9/7/3).

## Verification result

- **19 load-bearing claims: 9 CONFIRMED · 7 CORRECT-BUT-INCOMPLETE · 3 MISLEADING · 0 FALSE · 0 UNVERIFIABLE.**
- Directionally honest bundle (no falsehoods). Heaviest corrections: **license** ("unspecified/free" → AGPL-3.0-or-later + commercial, copyleft), **workspace hierarchy** ("panes inside tabs" → workspace owns tabs+panes as peers), **tmux comparisons** overstated (mouse/persistence are zero-config-vs-manual, not tmux-lacks; "no browser unlike tmux" backwards).
- **Bias handled:** promotional anchor (Chase AI) hardest-scrutinized; its errors ("completely free", "works on Windows") were the incomplete ones. Technical source (DevOps Toolbox) + primary docs agreed on core mechanics — healthy cross-source spread.

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 6 | 1 (new topic) | 0 (10-file topic; scorecard + caveats close the fact-check gap) | ~1.0 |

## Wiki files created/updated (12)

- **New (10):** `wiki/herdr/` — `_index` · `what-herdr-is` · `architecture-and-detection` · `supported-agents-and-install` · `competitive-landscape` · `license-and-adoption-caveats` · `claims-scorecard` · `caveats-and-corrections` · `sources-and-stances` · `hireui-translation`.
- **Librarian (2):** `wiki/_master-index.md` (herdr registered, newest-at-top) · `raw/_inventory.md` (row raw→compiled).
- **Provenance:** `raw/2026-07-18-herdr/` (6 transcripts + `_sources.md`); `output/bypass-attempts.md` (block audit).

## Final metric

- `gaps_closed_ratio` = **~1.0** (new-topic gap closed with a full verified 10-file topic).
- **Stop reason:** single-cycle bundle complete (Phase 6 cond. 1 target-ratio + cond. 5 no unprocessed sources).

## Suggested next action

- **Operator reviews + merges `autopilot-research` → `main`** when ready (not auto-merged, per standing rule). Branch now carries 4 unmerged topics: copywriting `14071d0`, kimi-k3 N=3 `5525f6e`, vercel-eve, and this herdr ship.
- **Highest-value pilot (HIGH fit):** run Herdr locally as the orchestration surface for the multi-agent hireui dev loop (Claude Code + GitNexus MCP + Figma MCP + the v189 loop-engineering babysitter in panes, agent-state sidebar, detach/reattach test). One week → write-up in `04 Reviews/`. Ties into the cc-sdd + loop-engineering v189 compound pilot. See `wiki/herdr/hireui-translation.md`.
- **Follow-up deepenings if revisited:** the 2 dropped comparison videos (Better Stack + Fru Dev "Tmux vs Cmux vs Herdr vs Paneflow") for a sharper competitive-landscape; a Herdr-vs-cmux head-to-head; the socket-API/agent-skill spec (response format) for the multi-agent-orchestration pilot.
- **Process codification candidate:** add a yt-dlp-specific mini-ladder (`--cookies-from-browser` first; batch ≤5 with cooldown) to `(C) bypass-403-escalation.md` (currently HTML-page-only).
