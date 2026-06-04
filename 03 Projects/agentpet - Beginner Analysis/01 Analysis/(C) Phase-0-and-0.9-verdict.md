# (C) ntd4996/agentpet ("AgentPet") — Phase 0 + Phase 0.9 STRICT verdict (v154)

**Subject:** `ntd4996/agentpet` — https://github.com/ntd4996/agentpet
**Date:** 2026-06-04 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS-MODERATE (declared-VN cultural-peer) · (b) STRONG · (c) STRONG · (d) STRONG.

---

## Phase 0 — scope gate
**On-goal.** AgentPet is *"a native macOS menu-bar application that monitors multiple AI coding agents simultaneously using a desktop-pet character that responds to agent activity states."* The whole purpose is **operating/observing multiple AI coding agents** (Claude Code + 6 peers) — squarely goal #1, and directly applicable to how Storm Bear runs Claude Code across parallel sessions. Not an app that merely *uses* an LLM (the off-goal v123/v152 shape); the subject IS agent infrastructure.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **PASS-MODERATE** (declared-VN; firmer than v153)
- Owner `ntd4996` = **Nguyễn Thành Đạt** — a **declared full Vietnamese name** (diacritics). Vietnamese is a registered cultural-peer axis and a **direct peer to Storm Bear** (Vietnamese). This is a **solid declared-name signal**, firmer than v153 ai-switcher's handle-only inference (`hoangpm96`).
- Held **MODERATE not STRONG** only because **location/employer is still undeclared** (declared name, undeclared location). Even under the PENDING v151-audit rec-(ii) ("require a solid (a) signal, not a name-heritage inference"), a declared full Vietnamese name is a genuine cultural signal — this is a real PASS, not a rescue. (And (b) carries the include regardless.)

### (b) Goal-relevance — **STRONG** (load-bearing)
Live, real-time monitoring of **multiple AI coding agents at once** — per-agent status (working/waiting/done) + project + per-state timer, aggregate-state ambient signal, and **native notifications when an agent finishes or needs input** — across Claude Code, Codex, Gemini CLI, Cursor, Windsurf, opencode, GLM, plus a universal wrapper for any CLI agent. This is dead-center goal #1 (operating autonomous coding agents) AND a concrete Storm-Bear workflow win (don't lose a parallel session to "waiting for input"). **STRONG-not-STRONGEST** = an ambient observability/notification surface *around* the agents, not the agent substrate or a methodology (the v140/v143/v144/v153 utility-around-agents calibration).

### (c) Instructive engineering — **STRONG**
Clean **native Swift + SwiftUI** menu-bar app: a **Unix-socket daemon** ingests agent events, a **CLI helper** + **universal wrapper** (`agentpet run -- <command>`) instrument any agent, single SwiftPM package, macOS 13+. More mature than v153 (114 commits / v1.1.6 / 59→ active releases vs v153's 11 commits / no license). MIT. STRONG.

### (d) Corpus connectivity — **STRONG**
- **T2 "AI-Agent Observability/Metering Tool" sub-archetype → N=3** (v89 VibeCodingTracker + v109 cclog-cli + v154 agentpet).
- **Swift-primary native-macOS cluster** (v99 cmux + v100 Easydict + v154 agentpet) — observation.
- **Pattern #84 cross-tool** (7 named agents + a universal wrapper) + **VN cultural-peer cluster** (v76/v80/v85/v153/v154) + **VN observability micro-cluster** (v109 Lê Thanh Quảng + v154 both VN). Pattern #18 #8 NOT applicable (no provider aggregation).

---

## §35 — Soft Off-Goal-Rate Ceiling — **FULLY CLEARS**
- The ceiling was breached after v152 and only **satisfied** (not cleared) by v153. A GOAL-ALIGNED v154 now scrolls v151 out of the window:
- Rolling-3-ship window after v154 = **{v152 OG, v153 GA, v154 GA} = 1 OG ≤ 1 → CLEAR.** The v151/v152 double-off-goal breach is **resolved.**
- **NOT an override** → override-frequency triggers UNCHANGED (7-in-20 trailing from v152; lifetime overrides 10 UNCHANGED; the next audit's mandated override review stands, v154 adds nothing).

## §37 — Fact-provenance
≈**40★** / 10 forks / **114 commits** / latest **v1.1.6** (Jun 4 2026) / MIT / Swift 95.9% / native macOS menu-bar (SwiftUI, macOS 13 Ventura+; Xcode 16 / Swift 6 to build) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; env mocks the GitHub API). Micro-scale → **NOT a Pattern #52 claim.** Owner Nguyễn Thành Đạt (`ntd4996`, VN declared, location undeclared).

## Streak (v2.6 §32)
GA:16 · OG:11 [7 ov] → **GA:17 · OG:11 [7 ov]** (17th GOAL-ALIGNED PASS; NOT an override; "49+3\*" frozen @v125).

## Pattern Library — see `(C) Pattern-Library-Phase-4b.md`
**PRIMARY** T2 Observability sub-archetype → N=3 (PROMOTION-ELIGIBLE; sub-flavor split flagged). **SECONDARY** 1 NEW standalone (ambient/affective pet-UI status surface). §28: 1 new standalone (≤2); **registry 06 ACTUALLY edited** (rule-5). NO confirmed-count change (46 / 9).

## Pilot
**Firmer pilot candidate than v153** — MIT, mature (114 commits / v1.1.6), genuinely vault-useful (live multi-session status + "needs input" notifications). Native macOS; build with Xcode 16/Swift 6 or use a release; `install-snapshot` first; reversible. Joins the un-piloted goal-aligned backlog (v153 + v150 + v149 + v144).

## Honest non-claims
- (b) STRONG, held **not** STRONGEST (ambient monitoring around the agents, not the substrate).
- (a) is a real declared-VN PASS, held MODERATE (location undeclared) — firmer than v153, not laundered.
- T2 observability sub-archetype N=3 has a genuine sub-flavor split (metering vs live-status) — flagged for the audit to confirm-or-split, NOT asserted as a clean broad-class promotion.
- NOT a Tauri/LV-C7 instance (it's native Swift, not Tauri — explicitly not inflated into LV-C7).
- Pattern #18 #8 NOT applicable (no provider aggregation).
- NOT a #52 claim (40★/114 commits; metrics not API-verified).
- 1 new standalone; NO new top-level Pattern; NO confirmed-count change (46 / 9).
