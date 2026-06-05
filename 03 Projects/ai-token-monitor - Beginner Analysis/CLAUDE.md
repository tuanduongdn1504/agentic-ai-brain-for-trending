# ai-token-monitor — Beginner Analysis (project CLAUDE.md)

**Subject:** `soulduse/ai-token-monitor` (v158 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY 1 NEW standalone (social-leaderboard layer) + SECONDARY metering sub-flavor → N=4; registry 06 edited.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A system tray application for macOS and Windows that monitors token usage, costs, and activity across multiple AI coding tools in real-time."** Built with **Tauri v2 (Rust backend + React 19 frontend)**, MIT. Parses session **JSONL** files from Claude Code (`~/.claude/projects/`), Codex (`~/.codex/sessions/`), and OpenCode (`~/.local/share/opencode/`) via file watchers → real-time token/cost stats with per-provider cost models. **The corpus-first twist:** a **social/competitive layer** — a GitHub-style activity heatmap (2D/3D), a **leaderboard** comparing daily/weekly/monthly usage *with other developers*, **chat** for leaderboard members, monthly/yearly recap cards (top model, busiest day, streaks), and webhook alerts (Discord/Slack/Telegram). The PLpgSQL (Postgres) in the stack confirms a **shared backend** for those social features. Goal-aligned (observes the coding agents) + vault-useful (token/cost awareness). Owner `soulduse` (no location); v0.19.12; 227★.

## Verdict rationale
- **(b) STRONG** = real-time token/cost monitoring across Claude Code + Codex + OpenCode = goal #1 + a real heavy-Claude-Code workflow. **STRONG-not-STRONGEST** = an observability utility *around* the agents, not the substrate.
- **(a) FAIL** = `soulduse` handle, no visible cultural-peer/location signal, not (a)-7. No rescue needed (b carries). No axis minted.
- (c) STRONG (Tauri v2 + Rust + React 19 + JSONL parsing + file watchers + per-provider cost models + Postgres social backend; **339 commits / 73 releases / v0.19.12**; MIT). (d) STRONG (T2 observability sub-archetype N=5 / metering sub-flavor N=4 + JSONL-parsing mechanism + Tauri-but-not-LV-C7 + Pattern #84 cross-tool + the new social-leaderboard standalone).

## §35 / streak
**§35 STAYS CLEAR** — window {v156 GA, v157 GA, v158 GA} = 0 OG (6 consecutive goal-aligned ships v153→v158). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:20·OG:11 [7 ov] → **GA:21·OG:11 [7 ov]** (21st GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: 1 NEW section-C standalone "Social/Competitive Leaderboard for AI-Coding Usage (shared-backend token-metering + dev-vs-dev comparison + chat)" N=1 CORPUS-FIRST** — the corpus's first metering tool that INVERTS the local/private default: uploads usage to a shared Postgres backend to enable a dev-vs-dev leaderboard, chat, and recap cards. Distinct from the local/private metering tools (v89 VibeCodingTracker / v109 cclog-cli / v157 ClaudeBar) and from the local-first privacy-conscious pets (v154/v155). **SECONDARY: T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=5; metering/quota/cost sub-flavor → N=4** (v89 + v109 + v157 + v158) — tier layer, PROMOTION-ELIGIBLE (now very robust), recommend the audit CONFIRM. **§28: 1 new standalone (≤2); registry 06 §C row added + §F noted (rule-5).** NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): **Tauri-but-NOT-LV-C7** (it OBSERVES, doesn't control the agent — the v118-adjacent / agentpet "not LV-C7" line); JSONL-session-parsing-as-mechanism (the v89 log-parsing observability mechanism, Pattern #84 84c.1); Pattern #84 cross-tool (3 providers); webhook-alerts (Discord/Slack/Telegram); **privacy-inversion** (shared backend vs the local-first prior monitors — a notable trade-off); micro-no (227★, velocity unestablished → NOT #52).

## Provenance (§37)
≈**227★** / 44 forks / **339 commits** / **73 releases** (latest v0.19.12) / MIT / TypeScript 62.2% + Rust 29.9% + PLpgSQL 7.1% / Tauri v2 system-tray (macOS + Windows) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity unestablished → **NOT a #52 claim.** Owner `soulduse` (no location/bio).

## Pilot
**Pilot candidate** (MIT, mature 339c/73 releases, parses your existing Claude Code JSONL — zero agent reconfiguration). ⚠️ Caveat: the social leaderboard/chat features upload usage to a shared backend (privacy trade-off) — the local token-tracking works without opting into the social layer. `install-snapshot` first; reversible. ⚠️ This is the **6th "manage/monitor AI coding tools" ship in a row (v153–v158), ZERO piloted** — the audit is critically overdue (FIVE ripe promotion calls now); pilot or audit, don't catalogue a v159.

Shipped on branch `wiki/v158-ai-token-monitor` off main (at b5813df = v157). Not auto-merged — operator merges.
