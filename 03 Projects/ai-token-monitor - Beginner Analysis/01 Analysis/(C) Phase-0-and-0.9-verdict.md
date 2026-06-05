# (C) soulduse/ai-token-monitor — Phase 0 + Phase 0.9 STRICT verdict (v158)

**Subject:** `soulduse/ai-token-monitor` — https://github.com/soulduse/ai-token-monitor
**Date:** 2026-06-05 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal.** ai-token-monitor = *"A system tray application … that monitors token usage, costs, and activity across multiple AI coding tools in real-time."* The subject is a token/cost **observability** surface for AI coding agents (Claude Code + Codex + OpenCode). Goal #1, directly applicable to running Claude Code heavily. It observes the agents (parses their session JSONL), not an app that merely uses an LLM.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
Owner `soulduse` — no visible location/bio, no cultural-peer signal, not a Foundational-Vendor-Direct-Source ((a)-7). **(a) FAIL.** No (a)-rescue needed or attempted (b carries the goal-aligned include; the v150/v155/v157 shape). No axis minted (I won't infer Korean/Asian from a bare handle — the v139/v97→v115 discipline).

### (b) Goal-relevance — **STRONG** (load-bearing)
Real-time token + cost + activity monitoring across **Claude Code + Codex + OpenCode** (parsing each tool's session JSONL via file watchers, per-provider cost models). For a heavy Claude Code user, token/cost awareness across providers is operating-the-agents infrastructure. **STRONG-not-STRONGEST** = an observability utility *around* the agents, not the agent substrate or a methodology (the v140/v143/v144/v153/v154/v157 calibration).

### (c) Instructive engineering — **STRONG**
**Tauri v2** (Rust backend + React 19 frontend) + JSONL session parsing + file watchers + per-provider cost models + a **Postgres (PLpgSQL) shared backend** powering the social features + webhook integrations (Discord/Slack/Telegram). Mature: **339 commits / 73 releases / v0.19.12**. MIT. The shared-backend social layer is a real architectural commitment (not a throwaway feature). STRONG.

### (d) Corpus connectivity — **STRONG**
- **T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=5**; **metering/cost sub-flavor → N=4** (v89 VibeCodingTracker + v109 cclog-cli + v157 ClaudeBar + v158 ai-token-monitor).
- **JSONL-session-parsing-as-mechanism** (the v89 log-parsing observability mechanism, Pattern #84 84c.1) + **Tauri-but-NOT-LV-C7** (observes, doesn't control) + **Pattern #84 cross-tool** (3 providers) + the new social-leaderboard standalone.

---

## §35 — Soft Off-Goal-Rate Ceiling — **STAYS CLEAR**
- Rolling-3-ship window after v158 = **{v156 GA, v157 GA, v158 GA} = 0 OG → CLEAR** (6 consecutive goal-aligned ships v153→v158).
- **NOT an override** → override-frequency triggers UNCHANGED (7-in-20 trailing from v152; lifetime overrides 10 UNCHANGED).

## §37 — Fact-provenance
≈**227★** / 44 forks / **339 commits** / **73 releases** (latest v0.19.12) / MIT / TypeScript 62.2% + Rust 29.9% + PLpgSQL 7.1% / Tauri v2 system-tray (macOS + Windows) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; env mocks the GitHub API). Creation date unstated → velocity/age unestablished → **NOT a Pattern #52 claim.** Owner `soulduse` (no location/bio).

## Streak (v2.6 §32)
GA:20 · OG:11 [7 ov] → **GA:21 · OG:11 [7 ov]** (21st GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125). Six consecutive goal-aligned ships (v153→v158).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** 1 NEW standalone "Social/Competitive Leaderboard for AI-Coding Usage" N=1 CORPUS-FIRST. **SECONDARY** T2 observability sub-archetype → N=5 / metering sub-flavor → N=4. **§28: 1 new standalone (≤2); registry 06 ACTUALLY edited** (§C row + §F note, rule-5). NO confirmed-count change (46 / 9).

## Pilot
**Pilot candidate** (MIT, mature, parses existing Claude Code JSONL — no agent reconfiguration). Caveat: the social leaderboard/chat upload usage to a shared backend (privacy trade-off; local tracking works without it). ⚠️ **6th "manage/monitor AI coding tools" ship in a row (v153–v158), ZERO piloted** — audit (FIVE ripe promotion calls) or pilot, not a v159.

## Honest non-claims
- (b) STRONG, held **not** STRONGEST (observability utility around the agents).
- (a) FAILS (bare handle, no signal) — not laundered, no axis minted (no Korean/Asian inference from "soulduse").
- PRIMARY standalone is genuinely corpus-first + load-bearing (a shared Postgres backend + leaderboard + chat = a real privacy-inverting social layer, not a throwaway) — minting it is discipline, not inflation-despite-6-in-a-row (the test is corpus-first + load-bearing).
- SECONDARY is a tier-sub-archetype strengthening (N=5 / metering N=4), NOT a mint — the N promotions are the **audit's** call, filed not asserted.
- Tauri but **NOT** an LV-C7 management-GUI (it observes, doesn't control) — explicitly not inflated into LV-C7.
- NOT a #52 claim (creation date unstated; metrics not API-verified).
- NO new top-level Pattern; NO confirmed-count change (46 / 9).
