# (C) tddworks/ClaudeBar — Phase 0 + Phase 0.9 STRICT verdict (v157)

**Subject:** `tddworks/ClaudeBar` — https://github.com/tddworks/ClaudeBar
**Date:** 2026-06-05 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal.** ClaudeBar = *"A macOS menu-bar application monitoring AI coding assistant usage quotas across multiple providers."* The subject is a quota-**observability** surface for AI coding agents (Claude Code + 9 peers). Goal #1, and directly applicable to running Claude Code heavily (know your session/weekly/model budget before you hit a wall). Not an app that merely *uses* an LLM — it observes the agents themselves.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
Owner `tddworks` — a GitHub org named for "TDD works" (test-driven-development ethos; the `.claude/skills/add-provider/` skill is TDD-based). No cultural-peer/geographic signal, not a Foundational-Vendor-Direct-Source ((a)-7). **(a) FAIL.** No (a)-rescue needed or attempted (b carries the goal-aligned include; the v150/v155 shape). No axis minted.

### (b) Goal-relevance — **STRONG** (load-bearing)
Real-time quota tracking across **10 AI coding tools** in the menu bar (session/weekly/model %, color-coded gauges, notifications on quota-status change, auto-refresh, per-provider toggles). For a heavy Claude Code user this is operating-the-agents infrastructure — knowing your budget across Claude/Codex/Gemini/etc. at a glance is a concrete workflow win. **STRONG-not-STRONGEST** = an observability utility *around* the agents, not the agent substrate or a methodology (the v140/v143/v144/v153/v154 calibration).

### (c) Instructive engineering — **STRONG**
Native **Swift/SwiftUI** + **Tuist** project generation; per-provider quota adapters over each provider's CLI (`claude`, `codex`, `kimi`, …) or direct API auth; color-coded status, notifications, theme system (incl. `.itermcolors` import); a `.claude/skills/add-provider/` **TDD-based** skill for extending provider coverage. Very mature: **784+ commits / 106 releases / v0.4.65 / 1.2k★** (high release cadence). MIT. STRONG.

### (d) Corpus connectivity — **STRONG**
- **T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=4** (v89+v109+v154+v157); the **metering/quota sub-flavor reaches N=3** (v89+v109+v157), distinct from the ambient-pet sub-flavor (v154/v155/v156).
- **Swift-native-macOS cluster** (v99 cmux + v100 Easydict + v154 agentpet + v157) + **Pattern #84 cross-tool** (10 providers) + **v153 ai-switcher quota adjacency** (observe vs manage) + LV-C4 high-release-cadence.

---

## §35 — Soft Off-Goal-Rate Ceiling — **STAYS CLEAR**
- Rolling-3-ship window after v157 = **{v155 GA, v156 GA, v157 GA} = 0 OG → CLEAR** (5 consecutive goal-aligned ships v153→v157; the v151/v152 breach resolved at v154 stays resolved).
- **NOT an override** → override-frequency triggers UNCHANGED (7-in-20 trailing from v152; lifetime overrides 10 UNCHANGED).

## §37 — Fact-provenance
≈**1.2k★** / 100 forks / **784+ commits** / **106 releases** (latest v0.4.65, Jun 2 2026) / 48 open issues / MIT / Swift 97.2% (+ Shell 2.8%) / native macOS menu-bar (SwiftUI, Tuist; macOS 15+, Swift 6.2+) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; env mocks the GitHub API). Creation date unstated → velocity/age unestablished → **NOT a Pattern #52 claim.** Owner `tddworks` (GitHub org).

## Streak (v2.6 §32)
GA:19 · OG:11 [7 ov] → **GA:20 · OG:11 [7 ov]** (20th GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125). Five consecutive goal-aligned ships (v153 + v154 + v155 + v156 + v157).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** T2 observability sub-archetype → N=4, metering sub-flavor → N=3 (PROMOTION-ELIGIBLE; recommend the audit CONFIRM + formalize the metering vs ambient-pet sub-flavors). **§28: 0 new standalones** (a tier-sub-archetype strengthening). NO confirmed-count change (46 / 9). §F running-log note added (rule-5).

## Pilot
**Strong pilot candidate** (MIT, very mature, genuinely useful multi-provider quota-at-a-glance for a heavy Claude Code user). ⚠️ **5th "manage/monitor AI coding tools" ship in a row (v153–v157), ZERO piloted** — the catalogue is well past ripe; **run the overdue audit** (four ripe promotion calls) or **pilot one of the five**, not a v158.

## Honest non-claims
- (b) STRONG, held **not** STRONGEST (observability utility around the agents).
- (a) FAILS (org, no cultural-peer signal) — not laundered, no axis minted.
- PRIMARY is a **tier-sub-archetype strengthening** (T2 observability N=4 / metering N=3), **NOT** a new mint — §28 cap used at 0; ClaudeBar is a clean metering instance, not corpus-first enough to warrant a standalone (anti-inflation; contrast v89 which *introduced* the sub-archetype).
- ⚠️ **Honest overlap flagged for the audit:** the ambient-pet sub-flavor of this observability sub-archetype (v154/v155/v156) is the SAME thing as the separately-tracked "desktop-pet-status-surface" standalone (N=3). The audit must reconcile these — is the pet-surface a standalone, OR the ambient sub-flavor of the observability sub-archetype? Do NOT double-count.
- ClaudeBar *observes* quota; v153 ai-switcher *manages + auto-switches* on quota — distinct (observability vs management), noted not conflated.
- NOT a #52 claim (creation date unstated; metrics not API-verified).
- NO new top-level Pattern; NO confirmed-count change (46 / 9). N=3/N=4 promotions are the **audit's** call, filed not asserted.
