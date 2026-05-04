# (C) T5 4-way Comparison + Pattern #31 Promotion (v24 Phase 4b)

> **Type:** Phase 4b deliverable — T5 tier extension
> **Purpose:** Document T5 at N=4 (4 archetypes) + Pattern #31 promotion + cross-corpus pattern updates
> **Sources:** v9 + v10 + v14 + v24 T5 wikis + corpus synthesis
> **Status:** ✅ Phase 4b published

---

## 1. Summary

v24 Skyvern extends T5 Agent-as-application to **N=4 with 4 distinct organizational archetypes** (corporate + solo + community-platform + commercial-entity). First T5 with **domain-specific application focus** (browser automation). Validates **Pattern #31 Open-Core Commercial Entity at N=2** (with fish-speech v20) → PROMOTE to CONFIRMED. Plus Pattern #29 AGPL N=2, Pattern #19 community-viral-lineage sub-variant, Pattern #8 7th data point, 2 new candidates (#47 vision-DOM-free + #48 anti-bot moat).

## 2. T5 4-way snapshot

| Dimension | deer-flow v9 | autoresearch v10 | paperclip v14 | **Skyvern v24** |
|-----------|--------------|-------------------|----------------|------------------|
| **Stars** | 62K | 74K | 55.9K | **21.3K** |
| **License** | MIT | MIT | MIT | **AGPL-3.0** |
| **Archetype** | Corporate (ByteDance) | Solo-known (Karpathy) | Community-platform | **Commercial-entity** |
| **Domain** | Research | ML experiments | Orchestration | **Browser automation** |
| **Scope** | Broad generalist | Narrow specialist | Broad generalist | **Narrow specialist** |
| **Primary lang** | Python + TS | Python | TypeScript | Python + JS |
| **Stack** | LangGraph + Next.js | PyTorch raw | Express + React monorepo | Playwright + LLM |
| **Deployment** | Docker + K8s | Local CLI | pip + Docker | pip + Docker + **Cloud** |
| **Commercial tier** | Internal ByteDance | None | None | **Skyvern Cloud (paid)** |
| **Lineage archetype** | Corporate-internal | Individual-author | Alignment-theory | **Community-viral lineage** |
| **Benchmarks** | Not highlighted | val_bpb metric | promptfoo evals | **WebBench 64.4% + WebVoyager 85.8%** |
| **Multi-LLM** | Configurable | Single model | Agent adapter (BYO) | **8+ providers native** |
| **Community** | GitHub + Discord | GitHub | Discord primary | Discord + Twitter + LinkedIn |

## 3. 4 archetypes at T5 (fully occupied)

### Archetype matrix

| Archetype type | T5 occupant |
|----------------|-------------|
| Corporate | deer-flow (ByteDance) |
| Solo-known-figure | autoresearch (Karpathy) |
| Community-platform | paperclip (55.9K community) |
| **Commercial-entity** | **Skyvern (Skyvern-AI commercial)** ← NEW v24 |

### Archetype diversity assessment

**T5 has 4 distinct archetypes at N=4** — maximum archetype-per-wiki efficiency.

Compare:
- **T1 (N=8):** 8 archetypes, 1 per wiki (diversity-per-wiki = 100%)
- **T5 (N=4):** 4 archetypes, 1 per wiki (diversity-per-wiki = 100%)
- **T4 (N=4):** 3 archetypes (gws/notebooklm-py/graphify/TrendRadar — some archetype overlap)

T5 = most efficient archetype exploration so far.

## 4. Pattern #31 Open-Core Commercial Entity → PROMOTION

### Evidence

| # | Wiki | Sub-type | Evidence |
|---|------|----------|----------|
| 1 | fish-speech v20 | Outside-scope foundation-model | 39 AI INC + custom research-license + commercial paid tier |
| 2 | **Skyvern v24** | **T5 browser-agent** | **Skyvern-AI + AGPL-3.0 + Skyvern Cloud anti-bot proprietary** |

### Structural criteria at N=2

Both share:
- Commercial entity founded around product (not community-to-commercial transition)
- OSS core with restrictive license (custom non-OSI / AGPL)
- Proprietary commercial tier with domain-specific differentiator
- OSS as lead-gen + credibility
- Commercial tier as revenue
- Distinct from pre-existing-corp-opens-source / community-formalized-LLC / pure-OSS solo

### Cross-scope validation

- **Outside-scope foundation-model:** fish-speech v20
- **T5 browser-agent:** Skyvern v24

**Pattern spans 2 scope categories** — structurally unambiguous at N=2 across distinct sub-types.

### Promotion

**Pattern #31 PROMOTE to CONFIRMED at v24.**

### Confirmed formal statement

> **Pattern #31 Open-Core Commercial Entity (CONFIRMED v24):** Organizational archetype for frameworks where commercial entity founds both OSS product + proprietary commercial tier simultaneously (not community-to-commercial transition). OSS core uses restrictive license (custom non-OSI, AGPL, or similar) protecting against vendor appropriation while preserving community access. Proprietary tier adds domain-specific differentiator (anti-distillation / anti-bot / enterprise features) unavailable in OSS. Distinct from: (a) pre-existing-corp-opens-source, (b) community-formalized-LLC, (c) pure-OSS solo. Observed at N=2 across 2 scope categories (foundation-model fish-speech v20 + T5 browser-agent Skyvern v24).

## 5. Pattern #45 vs Pattern #31 — scope clarification

### Distinction (sharpened at v24)

- **Pattern #45 Dual-Licensing Strategy:** Multiple OSS licenses within single product family; all components remain OSS (e.g., Apache core + AGPL UI)
- **Pattern #31 Open-Core Commercial Entity:** OSS core + proprietary (non-OSS) commercial tier

### Corpus examples

- Unsloth v23: Pattern #45 (dual-OSS-license) — Apache core + AGPL UI, both OSS
- fish-speech v20: Pattern #31 (open-core) — custom-non-OSI OSS + commercial paid tier
- Skyvern v24: Pattern #31 (open-core) — AGPL OSS + Skyvern Cloud proprietary

**Patterns #31 and #45 are distinct** — different structural licensing strategies. Both can co-exist in single framework hypothetically.

## 6. Pattern #29 License-Category Diversity — strengthening

### AGPL-3.0 corpus count post-v24

| # | Wiki | AGPL scope |
|---|------|-----------|
| 1 | Unsloth Studio v23 | UI component only (dual-license with Apache core) |
| 2 | **Skyvern v24** | **Full OSS repo (single-license)** |

### Non-permissive corpus post-v24

| License | Count | Wikis |
|---------|-------|-------|
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| **AGPL-3.0** | **2** | **Unsloth Studio v23 + Skyvern v24** |
| Custom non-OSI | 1 | fish-speech v20 |
| **Total non-permissive** | **5** | **21% of 24 wikis** |

Non-permissive trend continues. AGPL N=2 specifically.

## 7. Pattern #19 community-viral-lineage sub-variant

### Sub-variant hypothesis

Pattern #19 archetype 3 (Community-viral) splits into:

| Sub-variant | Examples | Evidence |
|-------------|----------|----------|
| **3a Community-viral no-lineage** | agency-agents v18 + TrendRadar v19 | No acknowledged ancestors; Reddit/Twitter-born |
| **3b Community-viral lineage** | **Skyvern v24** | Acknowledges BabyAGI + AutoGPT community-viral ancestors |

### Registration

**Sub-variant candidate at N=1 (Skyvern).** Requires 2nd framework citing community-viral predecessors to validate.

### Validation path

Watch T5/T1 frameworks citing AutoGPT / BabyAGI / CamelAI / MetaGPT / CrewAI / Devin-style community-viral ancestors.

## 8. Pattern #8 Research-Benchmark Integration — 7th data point

| # | Wiki | Benchmark |
|---|------|-----------|
| 1 | codymaster v12 | SkillsBench +18.6pp |
| 2 | autoresearch v10 | val_bpb |
| 3 | graphify v16 | 71.5× token reduction |
| 4 | spec-kit v17 | 48× productivity |
| 5 | fish-speech v20 | Seed-TTS Eval |
| 6 | LlamaFactory v22 | ACL 2024 |
| 7 | **Skyvern v24** | **WebBench 64.4% + WebVoyager 85.8%** |

Pattern #8 gains browser-automation rigor tier (technical-report, not peer-reviewed).

## 9. New candidates at v24

### #47 Vision-DOM-Free Browser Automation

> **Pattern #47 (CANDIDATE N=1):** Browser-automation frameworks increasingly use vision + LLM instead of DOM/XPath selectors, trading latency + LLM cost for resilience to UI changes. Specific to browser-automation T5 sub-specialty.

Evidence: Skyvern v24.
Validation: External frameworks (browser-use, Agent-E, LaVague) match. Monitor for in-corpus N=2.

### #48 Proprietary-Anti-Bot Commercial Moat

> **Pattern #48 (CANDIDATE N=1):** Open-core browser-automation frameworks use proprietary anti-bot measures as commercial differentiator. OSS handles ideal-case; Cloud handles adversarial-case. Specific to browser-automation Pattern #31 sub-pattern.

Evidence: Skyvern v24.
Validation: Requires 2nd browser-agent framework with similar anti-bot moat.

## 10. Pattern #9 multi-axial — T5 update

### Resolution D (multi-axial) post-v24

| Archetype × scope | Narrow | Broad |
|-------------------|--------|-------|
| Corporate | — | deer-flow (research) |
| Solo-known | autoresearch (ML) | — |
| Community-platform | — | paperclip (orchestration) |
| **Commercial-entity** | **Skyvern (browser)** | — |

Skyvern fills **commercial-entity-narrow-scope** quadrant previously empty.

### Probabilities (unchanged from v23)

- A: 25% / B: 10% / C: 15% / **D: 50%** (leading)

Pattern #9 stays at Resolution D leading model.

## 11. Pattern Library state post-v24

### Counts

| Category | Pre-v24 | Post-v24 | Change |
|----------|---------|----------|--------|
| Confirmed | 25 | **26** | +1 (#31 promoted) |
| Active candidates | 19 | **20** | +2 new (#47, #48) − 1 promoted (#31) = net +1 |
| Stale candidates | 2 | 2 | unchanged |
| **Total** | **46** | **48** | **+2** |

**Ratio:** 20:26 = **0.77:1 (healthy).**

### Audit triggers

- Candidate count: 20 (trigger at 24)
- Wikis since last audit: 3 (v22 mini-audit)
- Ratio: 0.77:1 (well below 2:1)

**No trigger hit at v24.** Next trigger: +4 candidates OR v28 OR major corpus event.

## 12. Storm Bear operator relevance

### T5 cross-comparison

| Wiki | Storm Bear direct applicability |
|------|----------------------------------|
| deer-flow v9 | LOW — research agent, not Scrum coach fit |
| autoresearch v10 | LOW — ML research, not Storm Bear domain |
| paperclip v14 | LOW-MEDIUM — orchestration, conceptually relevant |
| **Skyvern v24** | **MEDIUM — Scrum metric collection utility** |

### Skyvern-specific Storm Bear use

**Potential:**
- Jira/Linear cross-team status scraping
- DORA metric dashboard extraction
- Retrospective data collection
- Enterprise SaaS scraping without APIs

**Friction:**
- AGPL-3.0 for team deployment (source disclosure ambiguity)
- Anti-bot gated to Cloud ($)
- Chrome-only browser support

**Verdict:** MEDIUM — potential internal pilot tool; avoid client-facing SaaS without AGPL audit.

## 13. v24 routine v2.1 action items

1. **Archetype #9 generalization** — "Commercial-entity with OSS-core + proprietary tier" (from foundation-model-specific)
2. **Pattern #31 vs #45 distinction** — Phase 0 axis 8 explicit handling
3. **Pattern #19 sub-variant support** — 3a/3b community-viral split
4. **T5 domain-specialization recognition** — generalist vs specialist sub-pattern
5. **Browser-automation sub-register** — if more browser-agents analyzed, consolidate #47 + #48
6. **Validation-density mode proven twice** — v23 + v24 both promoted patterns successfully

## 14. Corpus milestone tracking

### v24 = 24th wiki

- **6th v2 routine execution** — production-stable
- **T5 extends to N=4** — 4 archetypes, all occupied
- **19 consecutive wikis at ~2h velocity plateau** (v6-v24)
- **14th Storm Bear meta-entity** — consecutive pattern continues
- **Only T3 remains at N=1** — closure gap persists

### Pattern Library

- **26 confirmed + 20 active + 2 stale = 48 total**
- **Ratio 0.77:1 (healthy)**
- **No audit trigger hit**

## 15. Retrospective — validation-density continues

### v23 (Unsloth) outcome

- 2 promotions (#41 + #43) + 2 scope refinements (#42 + #44) + 2 strengthenings (#29 + #32) + 2 new (#45 + #46)

### v24 (Skyvern) outcome

- 1 promotion (#31) + 4 strengthenings (#29 + #19 + #8 + #28) + 2 new (#47 + #48) + 1 scope clarification (#45 vs #31)

### Pattern

Validation-density mode yields **6-10 pattern-library actions per ~2h wiki**. Consistent across v23 + v24. Proven routine pattern.

## 16. References

- T5 wikis: v9 deer-flow, v10 autoresearch, v14 paperclip, v24 Skyvern
- PATTERN_LIBRARY.md (pre-v24 state)
- v22 mini-audit document
- Pattern #9 history (T5 v10 + T4 v13 + cross-tier v16 + T1 v17)

---

**T5 extends to N=4 (4 archetypes: corporate + solo + community-platform + commercial-entity). First T5 with domain-specific application focus (browser automation). Pattern #31 Open-Core Commercial Entity PROMOTES to CONFIRMED (N=2 across foundation-model + T5 sub-types). Pattern #29 AGPL N=2. Pattern #19 community-viral-lineage sub-variant hypothesis. Pattern #8 7th data point. 2 new candidates (#47 + #48). Pattern Library state: 26 confirmed + 20 active + 2 stale = 48 total (0.77:1 healthy).**
