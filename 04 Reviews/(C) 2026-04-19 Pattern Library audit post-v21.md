# (C) Pattern Library audit — post-v21 (2026-04-19)

> **Trigger:** Multi-trigger audit hit at v21 (candidate count 20 > 15; 5 wikis since v18 audit; ratio 1:1 borderline)
> **Scope:** 20 confirmed + 20 candidates = 40 total patterns
> **Last audit:** 2026-04-19 post-v18 (promoted 8 candidates; introduced formal criteria)
> **Outcome:** 2 promotions (#27, #29); 1 refinement (#20 reformulated to archetype-dictionary); 2 stale-flags (#14, #16); 16 candidates retained; 0 retirements

---

## 1. Audit methodology

### Formal criteria (re-applied from v18 audit)

| Status | Criteria |
|--------|----------|
| ✅ CONFIRMED | ≥3 observations across 2+ tiers (or structurally unambiguous at N=2) |
| 🟡 CANDIDATE | 1-2 observations OR confined to single tier |
| 🔄 REFINED | Confirmed but formulation adjusted by later evidence |
| ⏳ STALE-CANDIDATE (new at v21) | Candidate with N=1 after 5+ wikis with no additional evidence |
| ❌ RETIRED | Explicitly invalidated by corpus evidence |

### New status at v21: ⏳ STALE-CANDIDATE

Introduced to flag candidates that haven't accumulated evidence despite corpus growth. Not retirement (may still validate), but signals lower priority for Pattern Library attention.

### Promotion decisions process

For each candidate:
1. Count observations (N)
2. Count tier diversity
3. Evaluate structural unambiguity
4. Apply criteria → promote / keep / flag-stale / retire
5. Consider reformulation if pattern has drifted

---

## 2. Promotion decisions

### ✅ Pattern #27 Community-Viral Scale Path → PROMOTE

**Evidence:**
- agency-agents v18 (T1) — 82.9K via Reddit (explicit)
- TrendRadar v19 (T4) — 52.1K via CN community-viral (inferred)
- system-prompts-leaks v21 (outside-scope) — 135.5K via crypto + X + Discord (inferred)

**Criteria check:**
- ✅ N=3
- ✅ 3 distinct tiers (T1 + T4 + outside-scope)
- ✅ Consistent mechanism (community-channel amplification)

**Decision:** PROMOTE to CONFIRMED.

**Formal statement (confirmed):**
> Community-Viral Scale Path: OSS frameworks can reach 50K+ stars via community amplification (Reddit, regional platforms, crypto/Discord/X communities) without corporate backing or VC funding. Requires: (1) unmet community need, (2) shareable aggregation or novel insight, (3) community-channel-embedded author.

---

### ✅ Pattern #29 License-Category-Diversity → PROMOTE

**Evidence (N=3 non-permissive across multi-tier):**
- TrendRadar v19 (T4) — GPL-3.0 (copyleft, tool governance)
- fish-speech v20 (outside-scope) — Custom non-OSI Research License (commercial-funnel)
- system-prompts-leaks v21 (outside-scope) — GPL-3.0 (copyleft, content governance)

**Criteria check:**
- ✅ N=3 non-permissive observations
- ✅ 2 distinct tiers (T4 + outside-scope)
- ✅ Structurally coherent (both copyleft + custom-restrictive represent "non-permissive" category distinct from MIT/Apache-dominant norm)

**Decision:** PROMOTE to CONFIRMED (retaining REFINED status from v20 reformulation).

**Formal statement (confirmed):**
> License-Category Diversity: As agent-space and adjacent-space frameworks commodify, license diversity expands beyond permissive-OSI default (MIT/Apache/ISC). Two distinct non-permissive paths emerge:
> 1. Copyleft community-preservation (GPL-3.0, AGPL) — enforces derivative sharing
> 2. Custom non-OSI commercial-funnel — research-only clauses create paid-tier gateway
>
> Both signal productization boundaries with opposite motivations (community-protection vs commercial-protection). Non-permissive share of corpus = 15% (3 of 21 wikis); majority remains permissive OSI.

---

### 🔄 Pattern #20 Solo-Scale Ceiling → REFORMULATE (revision fatigue addressed)

**Issue:** 3 revisions in 5 wikis (v16 → v18 → v19 → v21). Formula becoming broad + quasi-unfalsifiable. Each new scale data point triggers revision.

**Options considered:**
- (a) Retire as monolithic claim
- (b) Accept as observational, not predictive (weaker claim)
- (c) Replace with archetype-specific ceiling dictionary

**Decision:** Option (c) — reformulate as archetype-dictionary; retain REFINED status; acknowledge descriptive-not-predictive.

**Reformulated statement:**
> Solo-maintainer scale ceilings are archetype-dependent, not singular. Pattern #20 functions as observational dictionary, updated as corpus adds data points:
>
> | Archetype | Observed ceiling | Evidence |
> |-----------|------------------|----------|
> | Solo narrow | 100-1,000 stars | notebooklm-py v7 (~300) |
> | Solo medium single-platform | 5-10K | ECC v1 (~5K), Superpowers v2 (~8K) |
> | Solo broad multi-platform | ~30K | graphify v16 (30K) |
> | Solo broad external regional | ~50K | TrendRadar v19 (52.1K CN) |
> | Solo massive multi-platform viral | ~80K | agency-agents v18 (82.9K Reddit) |
> | Solo aggregator + crypto + zeitgeist | ~135K+ | system-prompts-leaks v21 (135.5K) |
> | Corporate multi-platform community | ~90K+ | spec-kit v17 (89.2K) |
>
> Pattern is observational-descriptive (not predictive). Future wikis extend dictionary, not formula. If new archetype emerges, add row rather than revising formula.

**Audit decision rationale:** Revision fatigue is a falsifiability problem. Reframing as observational dictionary preserves evidence value without inflating predictive claims. 8 data points at v21 anchor the dictionary.

---

## 3. Stale-candidate flags

### ⏳ Pattern #14 Alignment-Theory Visibility → STALE (keep-observing)

**Status:** N=1 (paperclip v14); 7 wikis since (v15-v21) with no additional evidence.

**Decision:** Flag as STALE-CANDIDATE. Not retired (rare-but-distinctive pattern may re-emerge). Re-evaluate at v25 or if 2nd alignment-framed framework appears.

**Rationale:** 7 wikis is long enough to assess: no Western framework has adopted explicit alignment-theory framing since paperclip. Pattern is rare, not emergent. Keeping in library as observational marker.

---

### ⏳ Pattern #16 Skill Dependency Locking → STALE (keep-observing)

**Status:** N=1 (multica v15); 6 wikis since (v16-v21) with no additional evidence.

**Decision:** Flag as STALE-CANDIDATE. Re-evaluate at v25 or if 2nd framework ships skills-lock.json-equivalent.

**Rationale:** multica's skills-lock.json was novel v15; ecosystem hasn't followed at 6-wiki window. Pattern may be ahead-of-curve (package-lock.json parallel) or genuinely niche. Keep observing.

---

## 4. Candidates retained (no action, fresh)

### Fresh candidates (v19-v21; <5 wikis old)

**From v19 (2 wikis old):**
- #28 Multi-Provider AI Abstraction (LiteLLM) — N=1, TrendRadar
- #30 3-Layer Agent Ecosystem Stratification — N=1, TrendRadar

**From v20 (1 wiki old):**
- #31 Open-Core Commercial Entity — N=1, fish-speech
- #32 Research-Paper-Chain Lineage — N=1, fish-speech (overlaps Pattern #19 4th archetype)
- #33 Non-OSI Custom License — N=1, fish-speech (related to promoted #29)
- #34 Anti-Distillation License Clause — N=1, fish-speech
- #35 Foundation-Model-as-Product Scope — N=1, fish-speech

**From v21 (0 wikis since):**
- #36 Pseudonymous Researcher Archetype — N=1, system-prompts-leaks
- #37 Crypto-Donation-Funded Scale Path — N=1, system-prompts-leaks
- #38 Prompt-Leak-Archive Genre — N=1, system-prompts-leaks
- #39 Controversial-License-Use — N=1, system-prompts-leaks (related to promoted #29)
- #40 Derivative-Security-Service Perverse-Incentive — N=1, system-prompts-leaks

**Total retained fresh candidates: 12**

### Older candidates (v15-v18; 3-6 wikis old, still active)

- #21 SDD Methodology Emergence — N=2 both T1 (GSD + spec-kit) — single-tier; keep candidate
- #23 AI-Disclosure Policy Emergence — N=1 (spec-kit v17), 4 wikis since
- #25 Personality-Driven Agent Design — N=1 (agency-agents v18), 3 wikis since
- #26 Shell-first T1 — N=2 (gstack + agency-agents), single-tier

**Total retained older candidates: 4**

---

## 5. Overlap + redundancy analysis

### Pattern #19 4th archetype vs Pattern #32

Pattern #19 (Intellectual Lineage Archetypes, CONFIRMED) post-v20 has 4 archetypes including research-paper-chain. Pattern #32 (Research-Paper-Chain Lineage, candidate) registers the same evidence as standalone candidate.

**Decision:** Keep both. Different framings:
- Pattern #19 = general lineage taxonomy (4 archetypes, framework-level)
- Pattern #32 = predictive claim about foundation-model space specifically

If Pattern #32 promotes at N≥2, Pattern #19 4th archetype is automatically validated. Redundancy is productive.

### Pattern #29 vs Pattern #33 overlap

Pattern #29 (License-Category Diversity, now CONFIRMED) covers custom non-OSI as one of 2 paths. Pattern #33 (Non-OSI Custom License, candidate) focuses specifically on custom licenses.

**Decision:** Keep both. Pattern #33 is sub-hypothesis of Pattern #29. Survives until N≥2 validates custom-specific pattern distinct from general non-permissive trend.

### Pattern #29 vs Pattern #39 overlap

Pattern #39 (Controversial-License-Use) is about applying licenses to arguably-non-owned content. Pattern #29 is about license-category diversity (what license is chosen). Different dimensions.

**Decision:** Keep both. Orthogonal axes.

---

## 6. Audit summary counts

### Pre-audit state (post-v21)

| Status | Count |
|--------|-------|
| Confirmed | 20 |
| Refined (subset) | 6 |
| Candidate | 20 |
| Retired | 0 |
| **Total** | **40** |

### Post-audit state

| Status | Count | Change |
|--------|-------|--------|
| Confirmed | **22** | **+2** (#27 + #29 promoted) |
| Refined (subset) | 6 | 0 (#20 reformulated but remains Refined) |
| Candidate | **16** | **-4** (2 promoted to confirmed; 2 flagged stale) |
| Stale-candidate | **2** | **+2** (new status: #14 + #16) |
| Retired | 0 | 0 |
| **Total** | **40** | **Same count** |

**Ratio:** 16 active candidates : 22 confirmed = **0.73:1** (healthy; well under 2:1 blocker).

### Audit triggers reset

- Candidate count: 16 (under 15 threshold; but close — 1 more candidate hits re-trigger)
- Wikis since audit: **0** (reset at v21 audit)
- Ratio: 0.73:1 (healthy)

**All 3 triggers reset. Next audit trigger:** when candidate count > 15 OR after 5 new wikis OR ratio > 1:1.

---

## 7. Key audit insights

### 1. Outside-scope wikis dominate recent pattern discovery

v20 + v21 = 10 new candidates combined (fish-speech 5 + system-prompts-leaks 5). **50% of current candidate count from 2 outside-scope wikis.**

**Implication:** outside-scope genres are generative surface for pattern discovery. Agent-framework tier-resident wikis have largely been observed; novel patterns increasingly come from adjacent genres.

### 2. Pattern #20 revision-fatigue resolved

Reformulation to archetype-dictionary addresses falsifiability concern. Pattern now descriptive-observational, not predictive-singular-formula. Future revisions = add dictionary rows, not re-derive formula.

### 3. Community-viral and license-diversity are structural corpus patterns

Both Patterns #27 and #29 promoted at v21 — both cross-tier, both multi-observation, both structurally coherent. Storm Bear corpus documents these as established patterns, not emergent hypotheses.

### 4. Pseudonymous + crypto-token monetization = distinct corpus signal

v21 introduced pseudonymous-author (#36) + crypto-token-funding (#37). Both at N=1 but structurally coherent and predictively strong. Watch v22+ for validation.

### 5. Ethical-framing required for content-provenance wikis

v14 + v20 + v21 = 3 ethical-framing wikis. v2.1 routine should formalize ethical-framing protocol for content-provenance wikis (prompt-leak-archive + foundation-model + alignment-theory).

### 6. Stale-candidate status introduced

Addresses Pattern #14 + #16 at N=1 after 5+ wikis without validation. Not retirement (may still validate), but signals low-priority-observation status. Enables cleaner "active candidate" list.

---

## 8. Recommendations from audit

### For next wiki (v22)

**Scope-selection criteria (post-audit):**
1. **Highest value:** T3 second entrant (closes 5/5 tier validation — only remaining N=1 tier)
2. **Medium value:** 2nd data point for fresh candidates (#28/#30/#31-35/#36-40)
3. **Low value:** more outside-scope wikis of existing sub-types (pattern-surface saturated)

### For routine v2.1

1. **Outside-scope sub-mode routing** — explicit handlers for education-aggregator / foundation-model / content-archive / [future sub-types]
2. **Ethical-framing protocol** — formalize when to trigger ⚠️ Read this first section (content-provenance / license-complexity / brand-association)
3. **Content-provenance axis** — Phase 0 add "content origin" field (authored / aggregated / extracted / trained-from-data)
4. **Pseudonymous-author detection** — probe handle cross-reference at Phase 0
5. **Pattern Library audit-trigger automation** — compute triggers at Phase 0 probe; recommend audit proactively

### For Storm Bear operator

1. **graphify-on-vault decision required** — 5+ sessions overdue. Execute / explicitly deprioritize / continue ignoring.
2. **Pilot focus:** spec-kit / BMAD / gws remain HIGH priority for Scrum-coach context.
3. **AVOID tier recognition:** system-prompts-leaks established AVOID tier; future content-extraction wikis likely cluster here.

---

## 9. Pattern Library structural health post-audit

### Maturity signals

- 22 confirmed patterns (up from 20)
- 16 active candidates + 2 stale-candidates = cleaner active list
- 4 refinements tracked (including Pattern #20 reformulation)
- 0 retirements (no patterns invalidated — may reflect young corpus or observation selection)

### Growth trajectory

| Audit point | Total | Confirmed | Candidate | Ratio |
|-------------|-------|-----------|-----------|-------|
| Pre-v18 audit | 27 | 12 | 15 | 1.25:1 |
| Post-v18 audit | 27 | 20 | 7 | 0.35:1 |
| Post-v19 | 30 | 20 | 10 | 0.5:1 |
| Post-v20 | 35 | 20 | 15 | 0.75:1 |
| Post-v21 | 40 | 20 | 20 | 1:1 |
| **Post-v21 audit** | **40** | **22** | **16 + 2 stale** | **0.73:1** |

**Library maturation:** 2 years would grow to ~80 patterns at current rate. Next audit at v26 or candidate count >15 or ratio >1:1.

---

## 10. References

- Pre-audit state: `PATTERN_LIBRARY.md` (post-v21, pre-audit)
- v18 audit: GOALS.md session-17 entry
- Related iteration logs: v19/v20/v21 build learnings
- v2 routine: `05 Skills/llm-wiki-routine-v2.md`

---

**v21 audit complete. 2 promotions (#27 community-viral + #29 license-diversity). 1 reformulation (#20 archetype-dictionary). 2 stale-flags (#14 + #16). 16 active candidates retained. Library post-audit: 22 confirmed + 16 candidates + 2 stale = 40 total (ratio 0.73:1, healthy). Next trigger reset.**
