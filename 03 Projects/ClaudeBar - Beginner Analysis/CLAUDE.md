# ClaudeBar — Beginner Analysis (project CLAUDE.md)

**Subject:** `tddworks/ClaudeBar` (v157 wiki ship, 2026-06-05).
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY: T2 observability sub-archetype → N=4 + metering sub-flavor → N=3 (NO new standalone); registry 06 §F noted.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A macOS menu-bar application monitoring AI coding assistant usage quotas across multiple providers."** Native **Swift 97.2% + SwiftUI** (Tuist build), MIT, macOS 15+/Swift 6.2+. Tracks **real-time quota** (session / weekly / model %) for **10 AI coding tools** — Claude, Codex, Gemini, GitHub Copilot, Antigravity, Z.ai, Kimi, Kiro, Amp, OpenCode Go — with color-coded status gauges (green/yellow/red), system notifications on quota-status change, configurable auto-refresh, per-provider toggles, and themes (incl. `.itermcolors` import). Relies on each provider's CLI (`claude`, `codex`, `kimi`, …) or direct API auth. Ships a `.claude/skills/add-provider/` TDD skill for extending provider support. Goal-aligned (observes/operates coding agents); directly vault-useful (multi-provider quota at a glance for a heavy Claude Code user). Owner `tddworks` (GitHub org); v0.4.65; 1.2k★.

## Verdict rationale
- **(b) STRONG** = real-time multi-provider quota monitoring = goal #1 (operating coding agents — know your Claude/Codex/etc. budget) + a real Storm-Bear workflow. **STRONG-not-STRONGEST** = an observability utility *around* the agents, not the substrate.
- **(a) FAIL** = `tddworks` org ("TDD works"), no cultural-peer signal, not (a)-7. No rescue needed (b carries).
- (c) STRONG (native Swift/SwiftUI + Tuist + **784 commits / 106 releases / v0.4.65 / 1.2k★** + 10-provider support + TDD add-provider skill; MIT). (d) STRONG (T2 observability sub-archetype N=4 / metering sub-flavor N=3 + Swift-native-macOS cluster + Pattern #84 cross-tool + v153 quota adjacency).

## §35 / streak
**§35 STAYS CLEAR** — window {v155 GA, v156 GA, v157 GA} = 0 OG (5 consecutive goal-aligned ships v153→v157). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:19·OG:11 [7 ov] → **GA:20·OG:11 [7 ov]** (20th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=4** (v89 VibeCodingTracker + v109 cclog-cli + v154 agentpet + v157 ClaudeBar) — and crucially the **metering/quota sub-flavor reaches a clean N=3** (v89 usage/cost + v109 logs/metrics + v157 quota), DISTINCT from the **ambient-pet live-status sub-flavor N=3** (v154/v155/v156 = the separately-tracked desktop-pet-status-surface standalone). Both sub-flavors now at N=3 → strongly **PROMOTION-ELIGIBLE**; recommend the audit CONFIRM the sub-archetype + formalize the two sub-flavors (and reconcile the pet-surface standalone as the ambient sub-flavor — see honest caveat). **§28: 0 new standalones** (a tier-sub-archetype strengthening, NOT a mint). NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Swift-native-macOS cluster N+1 (v99 cmux + v100 Easydict + v154 agentpet + v157); Pattern #84 cross-tool (10 providers); **v153 ai-switcher quota adjacency** (ClaudeBar *observes/displays* quota; v153 *manages + auto-switches* on quota — a clean observability-vs-management split); LV-C4 high-release-cadence (106 releases / v0.4.65); `.claude/skills/add-provider/` TDD internal-dev skill (thin; product-extension tooling, the tddworks ethos); `.itermcolors` theme import; NOT a #52 claim (1.2k★ but creation date unstated → velocity unestablished, not API-verified).

## Provenance (§37)
≈**1.2k★** / 100 forks / **784+ commits** / **106 releases** (latest v0.4.65, Jun 2 2026) / 48 open issues / MIT / Swift 97.2% (+ Shell) / native macOS menu-bar (SwiftUI, Tuist; macOS 15+, Swift 6.2+) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Creation date unstated → velocity unestablished → **NOT a #52 claim.** Owner `tddworks` (GitHub org).

## Pilot
**Strong pilot candidate** — MIT, mature (784 commits / 106 releases), native, and genuinely useful for a heavy Claude Code user (multi-provider quota at a glance + notifications before you hit a wall). `install-snapshot` first (or build from source via Tuist); reversible. ⚠️ But this is the **5th "manage/monitor AI coding tools" ship in a row (v153–v157), ZERO piloted** — the catalogue is well past ripe; the highest-value move is the **overdue audit** (now FOUR ripe N=3 calls) or actually **piloting** one of these five.

Shipped on branch `wiki/v157-claudebar` (stacked on the unmerged v156 branch). Not auto-merged — operator merges.
