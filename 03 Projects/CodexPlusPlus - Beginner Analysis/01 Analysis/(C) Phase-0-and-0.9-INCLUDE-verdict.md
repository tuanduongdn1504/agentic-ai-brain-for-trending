# (C) Phase 0 + Phase 0.9 INCLUDE verdict — CodexPlusPlus (v117)

**Routine:** v2.4. **Fetched:** 2026-05-29. **Verdict:** **STRONG INCLUDE 4/4** (no criterion fails; load-bearing strength = (c)(d) STRONG). First clean PASS after the v116 Sana OVERRIDE → post-override clean-PASS counter restarts at 1.

---

## Phase 0 — scope gate

| Gate | Result |
|---|---|
| Repo reachable + readable | ✅ `BigPizzaV3/CodexPlusPlus` |
| License present | ⚠️ **Not specified** (GitHub API SPDX = none); README shows a license *badge* but no resolvable LICENSE file → Pattern #83 declared-but-unresolved-license. Does NOT block Phase 0 (scale + activity floors met) but flagged. |
| Active / recently pushed | ✅ pushed 2026-05-29; created 2026-05-06 (~23 days, very active; 181 open issues) |
| Scale floor (≥1★) | ✅ **8,077★** |
| Tier classification | **T2 Service / desktop enhancement-harness** (external CDP-injection wrapper + Tauri management tool; sibling to v73 cc-switch) |

**Phase 0 = PASS.** Squarely in-scope: a harness/tooling layer for an autonomous coding agent (OpenAI Codex). Directly adjacent to v62 codex-plugin-cc + v73 cc-switch.

---

## Phase 0.9 — STRICT 4-criterion INCLUDE filter

### (a) Author cultural-peer to Storm Bear — **PASS (inferred)**

BigPizzaV3 = solo developer, `owner.type: User`, profile bare (no declared name/location/bio), account created 2025-10-11 (~7.6 mo old), 11 repos / 55 followers. Location is **inferred China-Mainland** from unambiguous community signals: a QQ discussion group (1103050832), Alipay + WeChat donation channels, bilingual zh/EN README, and Chinese-Mainland API-relay sponsors (JOJO Code, AIGoCode, PackyCode).

This is an **inference-tolerant (a) PASS**, consistent with the corpus precedents v100 tisfeng (inferred China-Mainland), v98 mukul975 (Indian-name inferred), v99 (inferred founders). It extends the **China-Mainland sub-cluster** (v82 + v83 + v91 + v94 + v100 + **v117** = 6 by-event) and the broader Asian-LOCATED cluster. **Honest flag:** the PASS rests on community-signal inference, not a declared profile — recorded as such, no new (a) sub-axis coined (China-Mainland is already established).

### (b) Goal-relevance / vault-utility — **MODERATE**

The documented #1 goal is "master Claude and autonomous agents for software development." Codex++ enhances **OpenAI Codex, not Claude**, and its provider-switching routes traffic to custom/middle-layer endpoints — i.e. it routes *away* from Claude (mirrors v112 freellmapi). It is **not** core vault work, and Storm Bear runs Claude Code, not Codex.

What lifts it from WEAK to MODERATE: (i) it's genuinely about *autonomous coding-agent tooling*, the corpus's home turf; (ii) the **architecture is worth studying** (non-invasive CDP-injection harness + provider middle-layer); (iii) conditional utility *if* Codex ever enters the workflow, with a reversible macOS arm64 install. Honestly **MODERATE** — not inflated to STRONG.

### (c) Instructive / exemplary — **STRONG**

A clean reference design on three axes:
1. **Non-invasive enhancement via CDP injection** — launch the target app with DevTools Protocol open and inject JS into the live renderer instead of patching binaries/`app.asar`. Uninstall = delete launcher; target untouched.
2. **Provider-switching middle-layer** — write `~/.codex/config.toml` (Base URL + key) to route to an OpenAI-compatible endpoint while preserving official login state; sync provider metadata before switching.
3. **Dual silent-launcher + management-tool design** (Tauri 2 + React) with self-update.

Directly instructive for the harness / one-binary-many-clients / provider-portability patterns the corpus tracks. **STRONG.**

### (d) Corpus connectivity — **STRONG**

- **v73 cc-switch** — near-direct sibling: Tauri 2 desktop provider-manager that switches Claude Code providers by rewriting config. Codex++ does the same for Codex via `config.toml`. → **Pattern #18 #8 8a config-switcher** sibling.
- **v62 codex-plugin-cc** — Codex tooling lineage.
- **v69 CloakBrowser** — CDP-based external harness (→ Pattern #18 sub-mechanism B2 CDP-variant).
- **Pattern #18 #8 Multi-Source LLM Aggregator** (v115-generalized: 8a config-switcher v73 / 8b live-routing-proxy v112) — Codex++ = 8a N+1.
- China-Mainland sub-cluster; Pattern #52 EXTREME-VIRAL pulse; Pattern #83 license; Pattern #66 supply-chain.

**STRONG.**

---

## Verdict

| Criterion | Result |
|---|---|
| (a) cultural-peer | **PASS (inferred China-Mainland)** |
| (b) goal-relevance / vault-utility | **MODERATE** (Codex-not-Claude side-utility + architecture study) |
| (c) instructive | **STRONG** |
| (d) corpus connectivity | **STRONG** |

**STRONG INCLUDE 4/4** — no criterion fails; the INCLUDE is load-bearing on (c)(d), with (a) an honest inferred-PASS and (b) an honest MODERATE.

**Finding-2 calibration note:** (b) was deliberately held at MODERATE rather than inflated — Codex++ routes away from Claude and isn't core vault work; (a) is flagged as inferred rather than asserted as a hard PASS. Healthy rubric discrimination.

**Streak:** "44+2\*" → **"45+2\*"** (45 PASS + 2 OVERRIDE; v117 = 1st consecutive clean PASS after the v116 Sana override, post-override counter restarts at 1). The pre-existing 44-vs-45-PASS count discrepancy remains flagged for the ~v119–v120 audit, not reconciled here.

**Pilot:** **NOT a Tier-1 vault pilot** — Codex-specific, routes away from Claude, unresolved license, supply-chain caveat (CDP injection + middle-layer routing + relay sponsors). Conditional/study-only: pilot ONLY if Codex enters the workflow, and then snapshot-first + throwaway-key + inspect `config.toml`.
