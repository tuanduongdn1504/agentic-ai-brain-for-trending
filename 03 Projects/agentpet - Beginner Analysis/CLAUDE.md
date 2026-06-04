# agentpet — Beginner Analysis (project CLAUDE.md)

**Subject:** `ntd4996/agentpet` ("AgentPet") (v154 wiki ship, 2026-06-04).
**Verdict:** **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS-MODERATE (declared-VN cultural-peer) · (b) STRONG · (c) STRONG · (d) STRONG.
**Routine:** v2.6 (§31/§35/§37).
**Requested:** "build LLM wiki ... macOS app to manage multiple AI coding tools."

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis verdict + §35-CLEAR + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY T2 Observability sub-archetype → N=3 + SECONDARY 1 NEW standalone; registry 06 edited.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
**"A native macOS menu-bar app that monitors multiple AI coding agents simultaneously using a desktop-pet character that responds to agent activity states."** Swift 95.9% + SwiftUI; a Unix-socket daemon ingests agent events + a CLI helper + a universal wrapper (`agentpet run -- <command>`). Shows a **live list of every agent** (colored status dot + project + current action + per-state timer) across **Claude Code, Codex, Gemini CLI, Cursor, Windsurf, opencode, GLM (Z.AI)**; a **desktop pet reacts to the aggregate state** (working / waiting / done / celebrate); **native notifications** when an agent finishes or needs input; an **online pet library** with one-click download. Squarely goal #1 (operating *multiple* coding agents at once) and directly vault-applicable. Owner **Nguyễn Thành Đạt** (`ntd4996`, declared Vietnamese name); MIT; macOS 13+; v1.1.6.

## Verdict rationale
- **(b) STRONG** = the load-bearing axis: live multi-agent run-state monitoring + "finished / needs input" notifications for Claude Code + 6 peers = dead-center goal #1 AND a real Storm-Bear workflow (don't lose track of parallel sessions). **STRONG-not-STRONGEST** = an ambient monitoring/notification surface *around* the agents, not the substrate.
- **(a) PASS-MODERATE** = `ntd4996` = **Nguyễn Thành Đạt**, a declared full Vietnamese name (diacritics) → a solid cultural-peer + direct peer to Storm Bear; **firmer than v153 ai-switcher's handle-inference** (location still undeclared, so MODERATE not STRONG). Even under the PENDING v151-audit rec-(ii), a declared Vietnamese name is a real cultural signal.
- (c) STRONG (clean native Swift/SwiftUI + Unix-socket daemon + CLI helper + universal wrapper; 114 commits / v1.1.6 = more mature than v153's 11 commits; MIT). (d) STRONG (T2 observability sub-archetype N=3 + Swift-native-macOS cluster v99/v100 + Pattern #84 cross-tool + VN cluster).

## §35 / streak
**§35 — FULLY CLEARS.** v154 GA → rolling-3 window {v152 OG, v153 GA, v154 GA} = 1 OG ≤ 1 → **CLEAR** (v154 scrolls v151 out; the v151/v152 breach is resolved). NOT an override → override-frequency UNCHANGED (7-in-20 trailing; lifetime 10). Streak GA:16·OG:11 [7 ov] → **GA:17·OG:11 [7 ov]** (17th GOAL-ALIGNED PASS).

## Pattern Library
**PRIMARY: T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=3** (v89 VibeCodingTracker + v109 cclog-cli + v154 agentpet) → **PROMOTION-ELIGIBLE.** ⚠️ Honest sub-flavor split flagged for audit: v89/v109 = usage-metering / log-analysis (after-the-fact); v154 = **live real-time run-state monitoring + ambient notification** (operational). Audit confirms-the-broad-class-at-N=3 OR splits metering(N=2) / live-status(N=1). **SECONDARY: 1 NEW section-C standalone** "Ambient/Affective Multi-Agent Status Surface (reactive desktop-pet UI)" N=1 CORPUS-FIRST (a reactive pet/avatar as the agent-state display = corpus-first UX device). **§28: 1 new standalone (≤2); registry 06 ACTUALLY edited (rule-5).** NO confirmed-count change (46 patterns / 9 Library-vocab CONFIRMED). Observations (NOT minted): Swift-primary native-macOS cluster N+1 (v99 cmux + v100 Easydict + v154); Pattern #84 cross-tool (7 named agents + universal wrapper); VN cultural-peer cluster N+1 (now DECLARED-VN, firmer than v153); VN observability micro-cluster (v109 + v154 both VN authors); universal-CLI-wrapper-for-any-agent (`agentpet run --`); Pattern #18 #8 NOT applicable (not provider aggregation); micro-scale (40★) NOT #52.

## Provenance (§37)
≈**40★** / 10 forks / **114 commits** / **v1.1.6** (Jun 4 2026) / MIT / Swift 95.9% / native macOS menu-bar (SwiftUI, macOS 13+) — page-stated as of 2026-06 via WebFetch, **NOT independently API-verified §37.4** (env mocks the GitHub API). Micro-scale → **NOT a #52 claim.** Owner Nguyễn Thành Đạt (`ntd4996`, VN declared, location undeclared).

## Pilot
**Pilot candidate (firmer than v153)** — MIT-licensed, more mature (114 commits / v1.1.6), and genuinely vault-useful (live status + "needs input" notifications across parallel Claude Code sessions). Native macOS, builds with Xcode 16/Swift 6, or grab the release. `install-snapshot` first; reversible. Joins the un-piloted goal-aligned backlog (v153 ai-switcher + v150 Paseo + v149 Scrapling + v144 headroom).

Shipped on branch `wiki/v154-agentpet` (stacked on the unmerged v153 branch). Not auto-merged — operator merges.
