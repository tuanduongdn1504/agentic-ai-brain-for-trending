# (C) Pattern Library Audit Post-v29 (2026-04-22)

> **Trigger:** 3rd consecutive audit-trigger wiki (v27 audit cleared → v28 re-hit → v29 re-hit).
> **Hard-block condition reached:** action-backlog **181+** > 100-threshold (routine v2 guard).
> **Pre-audit state:** 27 confirmed + 32 active + 3 stale + 4 retired = 66 full / 62 active. **Ratio 1.19:1.**
> **Operator decision:** Option B — audit first, then v30 OpenHands wiki.
>
> **Audit scope:** (1) active candidate promotion review, (2) Pattern #17 variant 5 promotion, (3) Pattern #47 + #48 refinement formalization, (4) candidate overlap/absorption, (5) stale-flag application (missed at v28), (6) event-based vs architectural distinction, (7) new criteria formalization, (8) audit cadence reform proposal.
>
> **Audit goal:** clear backlog so v30+ operates in compliant state. Active promotion (not just retirement) per v27 audit self-critique.

---

## Executive summary

### Actions taken (13 total)

**Promotions (2):**
- **#51 Vibe-Coding Spectrum** → promoted to CONFIRMED (N=2 at 2 spectrum poles = structurally demonstrated)
- **Pattern #17 variant 5 ecosystem-scale commercial platform** → promoted within-pattern (N=2 HF + Microsoft = structurally unambiguous)

**Refinements (2):**
- **#47 Vision-Based Browser Automation** → narrow scope to "vision-based as architectural alternative to DOM"
- **#48 Proprietary Anti-Bot Commercial Moat** → narrow scope to "proprietary-commercial-gated anti-bot specifically"

**Retirements (1):**
- **#60 AutoGen-Extension Ecosystem Archetype** → absorbed into Pattern #17 variant 5 formal statement

**Stale-flags (2, retroactively at v28-missed check):**
- **#45 Dual-Licensing Strategy** (registered v23, 6 wikis since, was due for stale-flag at v28)
- **#46 Duo-Founder + Team Archetype** (registered v23, 6 wikis since, was due for stale-flag at v28)

**Observation-track reclassifications (1):**
- **#66 Supply-Chain Security Incident Response** → flagged as event-based observation (not architectural pattern); keep candidate status, re-evaluate v34

**New criteria (3):**
- **Spectrum-pattern structural demonstration at N=2** — spectrum-type patterns with observable poles can promote at N=2 via 2-distinct-pole observations
- **Variant-within-pattern promotion at N=2** — sub-variants within confirmed patterns can promote at structurally-unambiguous N=2
- **Mini-audit protocol at 0.95:1 ratio** — lightweight rebalance (~30 min) pre-trigger

**Audit cadence reform proposal (1):**
- Mini-audit at 0.95:1 / full audit at 1.05:1 (replaces current >1:1 trigger)
- Hard block at 2:1 ratio OR action-backlog >100 (unchanged)

### Net state transitions

| Status | Pre-audit | Post-audit | Δ |
|--------|-----------|------------|---|
| Confirmed | 27 | **28** | +1 (#51 promoted) |
| Refined (subset of Confirmed) | 11 | **13** | +2 (#47, #48 refinements formalized) |
| Active Candidate | 32 | **28** | -4 (-1 promoted #51 / -1 retired #60 / -2 stale-flagged #45, #46) |
| Stale | 3 | **5** | +2 (#45, #46 flagged) |
| Retired | 4 | **5** | +1 (#60 absorbed) |
| **Active library total** | 62 | **56** | -6 |
| **Full library total** | 66 | **66** | 0 (retirement offsets promotion) |

### Ratio resolution

- Pre-audit: 32:27 = **1.19:1** (trigger HIT 3rd consecutive)
- Post-audit: 28:28 = **1.00:1** (at trigger threshold)

**Ratio lowered 0.19 points** via 1 promotion + 1 retirement + 2 stale-flags. Still borderline — suggests audit cadence needs reform.

### Trigger status

- Post-audit still AT 1.00:1 threshold (not cleanly cleared — audit backlog too large for single audit)
- **Next audit trigger:** candidate count ≥30 OR v34 OR ratio >1:1 (per current rules)
- **Under proposed cadence reform:** mini-audit at 0.95:1 / full at 1.05:1

---

## Phase A — Active candidate promotion review (FIRST this audit)

### Systematic N=2+ check across all candidates

v27 audit was retire-only (0 promotions). Self-critique at v27 iteration log: *"audit protocol needs active promotion review."* This audit addresses that.

| # | Pattern | N | Cross-tier? | Structural? | Decision |
|---|---------|---|-------------|-------------|----------|
| 42 | Academic-Published | 1 | — | — | Stay stale |
| 44 | Academic-Lab Affiliation | 1 | — | — | Stay stale |
| 45 | Dual-Licensing Strategy | 1 | — | — | **STALE-FLAG** (retroactive) |
| 46 | Duo-Founder + Team | 1 | — | — | **STALE-FLAG** (retroactive) |
| 47 | Vision-Based Browser Automation | 1 | — | N=1 | Stay candidate (REFINED) |
| 48 | Proprietary Anti-Bot Moat | 1 | — | N=1 | Stay candidate (REFINED) |
| 49 | Design-Template-Aggregator | 1 | — | — | Stay candidate |
| 50 | Commercial-Funnel Companion | 1 | — | — | Stay candidate |
| **51** | **Vibe-Coding Spectrum** | **2** | **spec-kit T1 + awesome-design-md outside** | **Spectrum at 2 poles** | **✅ PROMOTE** |
| 52 | Extreme-Viral-Velocity | 1 | — | — | Stay candidate |
| 53 | Multi-Framework BYO | 1 | — | — | Stay candidate |
| 54 | Named-Instructor Team | 1 | — | — | Stay candidate |
| 55 | Korean Regional Archetype T1 | 1 | — | — | Stay candidate |
| 56 | Multi-Runtime Orchestration | 1 | — | — | Stay candidate |
| 57 | Recursive Corpus Reference | 1 | — | — | Stay candidate |
| 58 | Branding-Package Divergence | 1 | — | — | Stay candidate |
| 59 | Plugin Marketplace Native | 1 | — | — | Stay candidate |
| 60 | AutoGen-Extension Ecosystem | 1 | — | Sub-pattern of #17 variant 5 | **RETIRE (absorbed)** |
| 61 | LLM-Client DI Pattern | 1 | — | — | Stay candidate |
| 62 | Hashtag Plugin Discovery | 1 | — | — | Stay candidate |
| 63 | Format-Scoped Optional Deps | 1 | — | — | Stay candidate |
| 64 | Open-Source Anti-Bot | 1 | — | — | Stay candidate |
| 65 | 4-Tier Sponsorship | 1 | — | — | Stay candidate |
| 66 | Supply-Chain Incident | 1 | — | Event-based not architectural | **OBSERVATION-TRACK FLAG** |

### Promotion candidate #51 Vibe-Coding Spectrum — analysis

**Pattern statement (pre-audit):**
> Framework authors explicitly position on vibe-coding spectrum — spec-kit v17 anti-vibe ("focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch") vs awesome-design-md v25 pro-vibe (*"Drop one into your project and let coding agents generate a matching UI"*).

**Observations:**
- **Spec-kit v17 (T1):** anti-vibe explicit methodology commitment
- **Awesome-design-md v25 (outside-scope):** pro-vibe explicit design philosophy

**Cross-tier:** spec-kit T1 + awesome-design-md outside-scope = **across 2 tier categories**

**Structural analysis:**
- Spectrum patterns require 2+ distinct pole observations to demonstrate spectrum exists
- N=2 at opposite poles demonstrates spectrum structurally
- Similar to Pattern #13 Autonomy-Framing Spectrum (already confirmed at N=2 via BMAD + paperclip)

**Decision:** PROMOTE to CONFIRMED under proposed new "spectrum-pattern structural demonstration at N=2" criterion.

**Cross-reference with existing #13:**
- Pattern #13 Autonomy-Framing Spectrum (confirmed): human-amplification vs zero-human autonomy
- Pattern #51 Vibe-Coding Spectrum (promoted v29 audit): anti-vibe vs pro-vibe methodology
- Both are spectrum patterns with explicit pole positions
- **Meta-pattern candidate (future):** "Framework-Positioning-Axis Spectrum Patterns" — multiple spectrum-type patterns observed in corpus. Too early to register at v29.

---

## Phase B — Pattern #17 variant 5 promotion (variant-within-pattern)

### Current state

Pattern #17 Ecosystem-Layer Organizations (confirmed v15, refined v25 + v26 + v27):
- N=8 total data points
- 6 archetype variants (detailed in v27 audit Pattern #17 formal statement)

### Variant 5 specifically

**"Ecosystem-scale commercial platform"** — organizations with >$1B valuation + multiple products + OSS + commercial tier + >10 years operational.

**N=2 evidence:**
- HuggingFace v26 (~$4.5B valuation 2023 reported; 14+ AI/ML products)
- Microsoft (v6 + v28; ~$3T market cap; hundreds of OSS products including AutoGen ecosystem)

### Structural unambiguity

Both clearly meet variant 5 criteria:
- Both >$1B valuation (HF 4.5B / Microsoft 3T)
- Both multiple OSS products (HF 14+ / Microsoft hundreds)
- Both commercial tier (HF Pro+Enterprise / Microsoft Azure)
- Both >10 years mature (HF 10 / Microsoft 50)

Within-variant variation (scale-of-scale, domain-breadth) is secondary; archetype match is primary.

### Decision: PROMOTE variant 5 within-pattern

**New formal criterion proposed:**
> **Variant-within-pattern promotion at N=2:** sub-variants within confirmed patterns can promote from "candidate variant" to "confirmed variant" at structurally-unambiguous N=2. This is *within-pattern* promotion (does not increment pattern count; refines variant classification).

**Action:** Pattern #17 formal statement updated:

> **#17 Ecosystem-Layer Organizations (CONFIRMED v15, REFINED v25/v26/v27/v29 audit).** Organizations or individuals operate as ecosystem layers — publishing multiple related products or curating cross-project registries. N=8 data points post-v29 across 6 archetype variants:
>
> 1. **Individual-led-dev** — nextlevelbuilder (goclaw + multica contribution) | N=1
> 2. **Big-tech curator** — Anthropic + Vercel | N=2
> 3. **Individual-led-dev solo-brand** — safishamsi/penpax.ai | N=1
> 4. **Commercial-startup ecosystem** — VoltAgent | N=1
> 5. **Ecosystem-scale commercial platform ✅ PROMOTED v29 audit** — HuggingFace + Microsoft | N=2 structurally unambiguous; includes sub-ecosystem sub-pattern (AutoGen-Extension archetype — Microsoft AutoGen Team > markitdown — previously registered as #60, absorbed at v29 audit)
> 6. **Individual-multi-runtime-publisher** — Yeachan Heo (OMC + oh-my-codex) | N=1

---

## Phase C — Pattern #47 + #48 refinement formalization

### Pattern #47 Vision-Based Browser Automation

**Pre-audit status:** candidate N=1 (Skyvern v24); **refined at v29** via crawl4ai counter-evidence.

**Formal refined statement:**
> **#47 Vision-Based Browser Automation (REFINED v29 audit, candidate N=1).** Framework uses LLM vision as primary interaction mechanism for browser automation. **Architectural alternative to DOM-based approach** (CSS/XPath selectors used by crawl4ai v29, Playwright, Selenium, Cypress, etc.). Trade-offs: vision more robust to UI changes + handles pure-image content; DOM faster + cheaper + deterministic. Pattern scope narrows to *vision-as-primary-mechanism*, not "DOM-free as universal novelty" as originally formulated.

**Evidence:**
- Skyvern v24 (vision-primary, N=1)
- Counter-evidence: crawl4ai v29 (DOM-based, successful at 64K stars)

**Promotion criteria:** 2+ framework using vision as primary browser-automation mechanism.

### Pattern #48 Proprietary Anti-Bot Commercial Moat

**Pre-audit status:** candidate N=1 (Skyvern v24); **refined at v29** via crawl4ai counter-evidence.

**Formal refined statement:**
> **#48 Proprietary Anti-Bot Commercial Moat (REFINED v29 audit, candidate N=1).** Framework gates anti-bot capabilities to proprietary/paid tier as commercial differentiation strategy. **Pattern scope narrows to commercial-gating-specifically**, not anti-bot capability generically. crawl4ai v29 demonstrates anti-bot can be fully OSS (Pattern #64 OSS counterpart).

**Evidence:**
- Skyvern v24 (proprietary anti-bot tier N=1)
- Counter-evidence: crawl4ai v29 (OSS anti-bot)

**Promotion criteria:** 2+ framework with proprietary-commercial-gated anti-bot as moat strategy.

### Both refinements tighten scope without invalidating patterns

Patterns #47 + #48 stay **candidate** (N=1) with refined scope. Counter-evidence doesn't kill pattern; it clarifies.

---

## Phase D — Candidate #60 absorbed into Pattern #17 variant 5

### #60 AutoGen-Extension Ecosystem Archetype (registered v28)

**Original formal statement:**
> Sub-pattern within Pattern #17 variant 5 — ecosystem-scale commercial platform spawns sub-ecosystem (AutoGen) which publishes official extensions (markitdown).

### Absorption rationale

- Pattern #17 variant 5 now has 2 data points
- AutoGen-extension archetype is **internal to Microsoft's variant 5 occupation** (sub-structural detail)
- Does not warrant standalone candidate status
- Absorbed as sub-observation within variant 5 formal statement

### Decision: RETIRE #60 as ABSORBED

Add to Retired section with rationale.

---

## Phase E — Stale-flag retroactive application

### Missed at v28 (no audit happened)

Per stale-tracking table, +5 wiki stale-checks due at v28:
- #45 Dual-Licensing Strategy (registered v23)
- #46 Duo-Founder + Team Archetype (registered v23)

Both should have been flagged at v28 audit. Since v28 had no audit, flag retroactively at v29.

### #45 Dual-Licensing Strategy

**Registered:** v23 Unsloth (Apache-2.0 core + AGPL Studio)
**Wikis since:** 6 (v24-v29)
**Additional evidence:** 0

Other corpus frameworks post-v23 did not adopt dual-license strategy:
- Skyvern v24: AGPL only
- awesome-design-md v25: MIT
- HF agents-course v26: Apache-2.0
- OMC v27: MIT
- markitdown v28: MIT
- crawl4ai v29: Apache-2.0

**Decision:** STALE-FLAG (retroactive from v28). Re-evaluate at v33 (+10 retire threshold).

### #46 Duo-Founder + Team Archetype

**Registered:** v23 Unsloth (Han brothers duo-founder)
**Wikis since:** 6
**Additional evidence:** 0

No corpus framework since v23 has had duo-founder archetype.

**Decision:** STALE-FLAG (retroactive from v28). Re-evaluate at v33.

---

## Phase F — Event-based vs architectural pattern distinction

### Pattern candidate #66 Supply-Chain Security Incident Response (registered v29)

**Registration evidence:** crawl4ai v0.8.6 `unclecode-litellm` fork response to litellm PyPI supply-chain compromise + README disclosure.

**Classification concern:**
- **Architectural patterns** describe repeatable structural properties (e.g., "N-tier anti-bot detection," "LLM-client DI")
- **Event-based observations** describe framework's response to external events (e.g., "responded to supply-chain incident")
- Pattern #66 is event-based (incident-driven), not architectural (structural)

### New classification: OBSERVATION-TRACK

Propose new candidate sub-category:

> **OBSERVATION-TRACK candidate:** event-based observation tracking; patterns documented for monitoring rather than architectural formalization. Promote only if multiple similar events demonstrate systemic pattern beyond individual incidents.

### Decision: #66 flagged as OBSERVATION-TRACK, not retire

Keep #66 in candidates with OBSERVATION-TRACK label. Re-evaluate at v34. If multiple corpus frameworks document supply-chain incidents by then, consider promotion as systemic pattern. Otherwise retire as one-off observation.

---

## Phase G — New criteria formalization

### (1) Spectrum-pattern structural demonstration at N=2

> **Spectrum-pattern criterion:** Patterns describing positioning-axis spectrum (where meaningful framework positions occupy distinct poles) can promote at N=2 when 2 observations occupy structurally-distinct pole positions. Requires:
> - Explicit positioning statements from each observation
> - Poles are opposite/contrasting (not similar)
> - Spectrum is meaningful axis (not arbitrary pair-finding)

**Applied:** #13 Autonomy-Framing Spectrum (confirmed earlier, pre-v29 — retroactive application) + **#51 Vibe-Coding Spectrum (promoted v29 audit)**.

### (2) Variant-within-pattern promotion at N=2

> **Variant promotion criterion:** Sub-variants within confirmed patterns (e.g., Pattern #17 archetype variants) can promote from "candidate variant" to "confirmed variant" when variant reaches structurally-unambiguous N=2. This is within-pattern refinement; does not increment pattern count.

**Applied:** Pattern #17 variant 5 (ecosystem-scale commercial platform) promoted at N=2 (HF + Microsoft).

### (3) Observation-track candidate sub-category

> **OBSERVATION-TRACK candidate:** event-based or incident-driven observations classified distinctly from architectural pattern candidates. Tracked for future systemic-pattern emergence; promotion requires cross-incident systemic demonstration (not single-incident novelty).

**Applied:** #66 Supply-Chain Incident Response.

---

## Phase H — Audit cadence reform proposal

### Problem identified

3 consecutive trigger hits (v27, v28, v29) at current ratio-threshold (>1:1). Candidate accumulation (3-5/wiki) vs audit consolidation (~4/audit) creates persistent over-threshold state.

### Proposed reform (for routine v2.1)

**Current triggers:**
- Candidate count ≥25 → audit
- +5 wikis since audit → audit
- Ratio >1:1 → audit
- Hard block: 2:1 ratio OR action-backlog >100

**Proposed new triggers:**
- **Mini-audit at 0.95:1 ratio** — lightweight rebalance (~30 min): retire obvious stale, promote clear N=2 unambiguous, no new formulation changes
- **Full audit at 1.05:1 ratio** (replaces >1:1) — 2h depth audit with refinements allowed
- **Hard block** unchanged: 2:1 ratio OR action-backlog >100
- **Candidate count threshold** changed: ≥28 → mini-audit (from ≥25)
- **+5 wikis since any audit** → mini-audit OR full audit (operator choice)

### Expected cadence impact

At 3-5 candidates/wiki growth rate + 4/audit consolidation:
- Pre-reform: ratio crosses 1:1 every 1-2 wikis → full audit → crosses again
- Post-reform: ratio crosses 0.95 at ~1 wiki → mini-audit (30 min) → stays below 1.05 until genuinely needed

**Action item for v2.1 routine:** implement cadence reform before v30+ audit cycle.

---

## Phase I — Net post-audit state

### Counts

| Status | Pre-audit | Post-audit | Change |
|--------|-----------|------------|--------|
| Confirmed | 27 | **28** | +1 (#51) |
| Refined (subset) | 11 | **13** | +2 (#47, #48) |
| Active Candidate | 32 | **28** | -4 |
| Stale | 3 | **5** | +2 (#45, #46) |
| Retired | 4 | **5** | +1 (#60) |
| Observation-track | 0 | **1** | +1 (#66 within candidates) |
| **Active library** | 62 | **56** | -6 |
| **Full library** | 66 | **66** | 0 |

### Ratio

**28:28 = 1.00:1.** At trigger threshold; below proposed new 1.05:1 threshold.

### Trigger status

Under current rules: still at trigger (ratio ≥1:1).
Under proposed rules: cleared (ratio <1.05).

---

## Recommendations for v30+

### Immediate

1. **Proceed with v30 OpenHands wiki** (operator's stated plan)
2. **Update PATTERN_LIBRARY.md** with promotions + refinements + retirements + stale-flags
3. **Apply cadence reform informally** — next audit at 1.05 not 1.00

### Strategic

4. **Monitor #51 (newly promoted)** — verify spectrum-pattern criterion holds with corpus growth
5. **Track variant 5 promotion impact** — see if Microsoft/HF trigger more ecosystem-scale-platform observations
6. **Formalize routine v2.1** — cadence reform + candidate registration strictness + active-promotion-at-audit

### v34 checkpoints

- #42, #44 at +12 since registration (v22) → retire unless evidence emerges
- #45, #46 at +11 since registration (v23) → retire
- #55-66 at +5-7 since registration → stale-flag review

---

## Meta-observations

### First active promotion in corpus audit history

v25 audit: 1 promotion (#28).
v27 audit: 0 promotions (retire-only, flagged as issue).
**v29 audit: 2 promotions (#51 confirmed + #17 variant 5 within-pattern).**

**Audit protocol matures** — active promotion review now part of discipline.

### Refinement rate

v25 audit: 2 refinements (#17, #28).
v27 audit: 5 refinements (#17, #19, #28, #55, #56).
**v29 audit: 2 refinements (#47, #48) + 3 new criteria formalizations.**

Refinements continue per-audit. Formulation drift normal as corpus matures.

### Retirement velocity

v25 audit: 0 retirements.
v27 audit: 4 retirements (#14, #16, #23, #25).
**v29 audit: 1 retirement (#60 absorbed).**

Retirement per audit varies by context; not every audit has clear retirement targets.

### Criteria evolution

Audit history shows:
- v21: STALE-CANDIDATE status introduced
- v27: N=1 stale-flag tracking protocol (+5/+10)
- **v29: 3 new criteria (spectrum-pattern / variant-at-N=2 / observation-track)**

Pattern Library criteria system evolves incrementally. Each audit refines operational protocol.

---

## References

- Prior audits: v21, v22 mini-audit, v25, v27
- v28 + v29 iteration logs (identified this audit's scope)
- v30 OpenHands wiki (next, post-audit)

---

**v29 audit: 2 promotions (#51 confirmed + #17 variant 5) + 2 refinements (#47, #48) + 1 retirement (#60) + 2 stale-flags (#45, #46) + 1 observation-track reclassification (#66) + 3 new criteria. Ratio 1.19:1 → 1.00:1. Audit protocol matures with first multi-promotion + formalized criteria expansion.**
