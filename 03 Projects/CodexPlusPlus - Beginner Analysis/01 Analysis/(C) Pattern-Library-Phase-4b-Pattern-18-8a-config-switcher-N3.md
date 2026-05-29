# (C) Pattern Library Phase 4b — CodexPlusPlus (v117)

**Routine:** v2.4. **Date:** 2026-05-29. **PRIMARY = Pattern #18 sub-archetype #8 "Multi-Source LLM Aggregator" → 8a config-switcher N+1, pushing overall #8 to N=3 = PROMOTION-ELIGIBLE.** No state change asserted at ship (promotion is an audit decision). v2.4 §28 honored: zero new standalone Library-vocab minted.

---

## PRIMARY — Pattern #18 #8 8a config-switcher N+1 (→ N=3 promotion-eligible)

### Context (v115 audit)
The v115 mini-audit **label-generalized Pattern #18 sub-archetype #8 to "Multi-Source LLM Aggregator"** with two sub-variants, PROVISIONAL N=2, promotion-eligible at N=3:
- **8a config-switcher** — rewrites a runtime config to switch the single active provider. Anchor: **v73 cc-switch** (Tauri 2 desktop, switches Claude Code providers).
- **8b live-routing-proxy** — all providers live behind one endpoint with fallover. Anchor: **v112 freellmapi**.

### v117 evidence
CodexPlusPlus's headline feature writes `~/.codex/config.toml` (Base URL + API key) to point **Codex** at a custom OpenAI-compatible endpoint while preserving official login — i.e. it switches the single active provider by rewriting a runtime config. **This is a textbook 8a config-switcher**, mechanism-identical to v73 cc-switch, applied to a *different* coding agent (Codex vs Claude Code) by a *different* author at *different* scale.

### Count
- **8a config-switcher:** v73 cc-switch + **v117 CodexPlusPlus = N=2** (2 authors, 2 target agents, both Tauri-2 desktop).
- **Overall #8 Multi-Source LLM Aggregator:** v73 (8a) + v112 (8b) + **v117 (8a) = N=3** → **PROMOTION-ELIGIBLE to CONFIRMED** at the next audit (~v119–v120).

### Honest caveats (load-bearing)
1. For Codex++, provider-switching is **one feature of a broader enhancement harness** (CDP injection, session management, plugins, worktrees), not its whole identity — unlike v73 cc-switch, which *is* a provider-switcher. The 8a registration is on the *provider-switching feature*, scoped honestly.
2. Both 8a instances are now **Tauri-2 desktop config-switchers** — the sub-variant may be narrowing toward "Tauri-desktop-config-switcher" specifically; the audit should check whether 8a is a general mechanism or a stack-coincidence before promoting.
3. Promotion is an **audit decision**, not asserted at ship. State UNCHANGED at v117.

Proposal: promote Pattern #18 #8 to CONFIRMED N=3 at the next audit, with 8a (v73+v117) / 8b (v112) sub-variants documented.

---

## SECONDARY (honest, mostly N+1 / NOTE)

1. **Pattern #18 sub-mechanism B2 "CDP-variant" — N+1.** Codex++ injects into the Codex renderer via Chromium DevTools Protocol = a CDP-based external harness (cf. v69 CloakBrowser CDP; B1 MCP v70 / B2 CDP / B3 OpenAI-compatible v112). Strengthens B2. NOTE.
2. **Pattern #52 EXTREME-VIRAL pulse-class — N+1.** ~351 stars/day × 23 days = clear pulse (>300/d), but window « 90d so NOT Multi-Month-Sustained and NOT a promotion. Notably fast accrual; worth a velocity note, nothing more.
3. **Pattern #83 declared-but-unresolved-license — N+1.** README carries a license *badge* but GitHub API resolves no SPDX/LICENSE → the 83f "declares-but-no-resolvable-LICENSE" family (cf. v74/v76/v77). NOTE; verify at audit whether a LICENSE file exists.
4. **Pattern #66 supply-chain — within-pattern NOTE.** Real considerations: external launcher injects code via CDP + rewrites `config.toml` to route API traffic through custom/middle-layer endpoints + funded by API-relay sponsors (JOJO Code / AIGoCode / PackyCode). An honest credential/trust surface; recorded as a security caveat, not a new pattern.
5. **Pattern #19 / China-Mainland sub-cluster — strengthening, NOT a new axis.** v82+v83+v91+v94+v100+**v117** = 6 by-event. (a) PASS inferred from community signals. No new (a) sub-axis (China-Mainland established).

---

## Library-vocab (v2.4 §28 discipline) — ZERO new standalones

Two candidate observations, both **filed into existing clusters, not minted** (cap = ≤2 new standalones/wiki; clustering-first):
- **"Tauri-2 desktop management-tool for a coding agent"** (v73 cc-switch + v117) → file into **LV-C7 Packaging/Runtime-Substrate** as a 2-instance cluster observation (watch toward a promotable sub-claim).
- **"API-relay / middle-layer reseller economy (Chinese-Mainland)"** (sponsors JOJO Code / AIGoCode / PackyCode; provider-switching as its client) → file into **LV-C2 Cost/Capacity-Economics-of-Free-Cheap-Inference**, which already holds the N=2 "Cost-Attribution-via-External-Service" promotion-eligible sub-claim (LiteLLM v89 + pricing-service v109). Codex++ is adjacent evidence of the same economic theme — strengthens LV-C2's relevance; the audit should judge whether it lifts the sub-claim toward N=3.

**No standalone Library-vocab registered.** The honest call: both observations belong in existing clusters, and minting near-duplicates is exactly what §28 forbids.

---

## State after v117

| Field | Value |
|---|---|
| Confirmed Patterns | **46** (UNCHANGED at ship) |
| Active candidates | ~25 (UNCHANGED) |
| Library-vocab CONFIRMED | **8** (UNCHANGED) |
| Library-vocab PROVISIONAL | ~11 tracked in registry (UNCHANGED — 0 new mints; 2 observations filed into LV-C2 + LV-C7) |
| Routine version | **v2.4 CURRENT** |
| Streak | **"45+2\*"** (was "44+2\*"; +1 clean PASS; 1st consecutive clean PASS post-v116 override) |

**Queued for next audit (~v119–v120):** (1) **Pattern #18 #8 → CONFIRMED N=3** decision (with the 8a-narrowing-to-Tauri-desktop check); (2) LV-C2 N=3 check incl. the Codex++ relay-economy evidence; (3) LV-C7 Tauri-desktop-harness 2-instance watch; (4) carry-forward: pre-existing 44-vs-45-PASS discrepancy + 2-data-point override-frequency review (from v116).

---

## Storm Bear's blunt take

Clean STRONG INCLUDE, and a genuinely useful one — unlike the Sana detour, this is *on-corpus*. The real prize is the Pattern #18 #8 promotion-eligibility: cc-switch finally has a same-mechanism sibling (config-switch a coding agent's provider by rewriting its config), so the Multi-Source-LLM-Aggregator archetype is at N=3 and should go CONFIRMED at the next audit — with the honest check that both config-switchers happen to be Tauri-2 desktop apps, which might mean the sub-variant is narrower than it looks. Two honest deductions keep this from being a 4×STRONG: (b) is MODERATE because it's a *Codex* tool that routes away from Claude, and (a) is an *inferred* China-Mainland PASS, not a declared one. And the load-bearing caveat for any pilot: this thing injects into your agent via CDP and reroutes your API key through middle-layer endpoints funded by relay sponsors, with no resolvable license — fascinating to study, trust-carefully to run.
