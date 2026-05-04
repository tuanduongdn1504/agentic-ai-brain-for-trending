# (C) T4 6-Way Comparison + Pattern 47/48 Refinement + 3 New Candidates (Phase 4b v29)

> **Type:** Phase 4b deliverable — T4 N=6 tier extension + Pattern #47/#48 refinement + 3 new pattern candidates (#64-66)
> **Project:** v29 crawl4ai
> **Date:** 2026-04-22
> **Parent:** [[(C) index]]

---

## 1. Executive summary

v29 crawl4ai extends **Tier 4 Agent-as-bridge to N=6** — T4 becomes 2nd-largest tier after T1 N=9. Adds **T4f solo-enterprise-scale-web-utility** archetype. **Refines Pattern #47** (vision-DOM-free → vision-based-alternative) and **Pattern #48** (anti-bot moat → proprietary-commercial-specific) via crawl4ai counter-evidence. Registers **3 new pattern candidates** (#64-66). **Pattern #31 3rd data point PENDING** via Cloud API Closed Beta. **Audit trigger RE-HITS 3rd consecutive wiki** at 32:27 = 1.19:1 ratio.

## 2. T4 6-way matrix (20-axis)

### Roster

| # | Wiki | Stars | Archetype |
|---|------|-------|-----------|
| 1 | notebooklm-py v7 | ~300 | T4b unofficial-solo-narrow |
| 2 | gws v13 | 25K | T4a official-corporate-broad |
| 3 | graphify v16 | 30K | T4c solo-broad-local |
| 4 | TrendRadar v19 | 52.1K | T4d solo-broad-external |
| 5 | markitdown v28 | 114K | T4e official-corporate-narrow-utility |
| 6 | **crawl4ai v29** | **64K** | **T4f NEW solo-enterprise-scale-web-utility** |

### 20-axis comparison

| Axis | notebooklm-py v7 | gws v13 | graphify v16 | TrendRadar v19 | markitdown v28 | **crawl4ai v29** |
|------|-----------------|---------|--------------|---------------|----------------|-----------------|
| **Stars** | ~300 | 25K | 30K | 52.1K | 114K | **64K** |
| **License** | MIT | Apache-2.0 | MIT | GPL-3.0 | MIT | **Apache-2.0** |
| **Language** | Python | Rust | Python | Python | Python | **Python** |
| **Organization** | Solo | Google corporate | Solo | Solo CN | Microsoft corporate | **Solo** |
| **Region** | Unclear | US | Unclear | CN | US | **Unclear** |
| **Purpose** | NotebookLM API bridge | Google Workspace CLI | Knowledge graph builder | News aggregator | File → Markdown converter | **Web → Markdown crawler** |
| **Scope** | Narrow (1 service) | Broad (11+ services) | Broad (files + code + media) | Broad (11 platforms) | Narrow (11 formats, 1 task) | **Broad (web scraping)** |
| **Official status** | Unofficial | Official Google | Unofficial | Unofficial | Official Microsoft | **Unofficial** |
| **Surfaces (count)** | 3 | 2+ | 2 | 2 | 3 | **3 (CLI + Python + Docker)** |
| **Plugin system** | None | None | None | None | Hashtag discovery | **None (but hooks ubiquitous)** |
| **LLM integration** | None | Model Armor safety | Claude vision | LiteLLM 100+ | `llm_client` DI + Azure DocIntel | **LiteLLM fork (all LLMs)** |
| **Anti-bot** | N/A | N/A | N/A | Light | N/A | **OSS 3-tier + proxy + Shadow DOM** |
| **Governance depth** | Light (solo) | Corporate tri-file | Medium + SECURITY.md | Medium | Microsoft corporate | **Solo-enterprise-depth** |
| **Distribution** | pip | cargo + brew | pip | pip | pip + Docker + uv | **pip + Docker** |
| **i18n** | EN only | EN only | en+ja+ko+zh | CN+EN | EN only | **EN only** |
| **Community scale** | Tiny | Google-corporate-backed | 30K | CN-viral | 114K corporate-amplified | **64K solo-organic** |
| **Monetization** | None | Google commercial | None | None | None explicit | **4-tier sponsorship + Cloud API soon** |
| **Commercial path** | None | Google Workspace | Penpax brand | None | Azure integration | **Cloud API (Pattern #31 pending)** |
| **Pattern #27 Viral** | No | Corporate-amplified | Solo-scale | CN-viral | Corporate-amplified (6th) | **Solo-organic-sustained (7th)** |
| **Supply-chain incident** | — | — | — | — | — | **v0.8.6 unclecode-litellm fork** |

## 3. T4 archetype observations at N=6

### Multi-axial quadrant coverage

**6 distinct variants at 6 wikis** — highest archetype diversity per entry in corpus.

### Corporate vs solo distribution at T4

- Corporate: 2 (gws + markitdown) = 33%
- Solo: 4 (notebooklm-py + graphify + TrendRadar + crawl4ai) = 67%

**Solo dominates T4** despite corporate highest-scale (markitdown 114K). Solo aggregate span: 300 to 64K.

### Scale distribution observations

- **Corporate-narrow** > corporate-broad by 4.5× (markitdown 114K vs gws 25K)
- **Solo-broad** similar range (graphify 30K ≈ TrendRadar 52K ≈ crawl4ai 64K)
- **Solo-narrow** tiny (notebooklm-py 300)

**Pattern observation:** narrow-utility + corporate backing = highest scale. Broad-scope + solo = 30-65K scale.

## 4. Pattern #47 + #48 refinement

### Refinement for Pattern #47 Vision-DOM-Free Browser Automation

**Original (v24):** Framework uses LLM vision instead of XPath/CSS selectors.

**Counter-evidence (v29):** crawl4ai is successful DOM-based crawler at 64K stars.

**Refined formulation:**
> **#47 Vision-Based Browser Automation as ARCHITECTURAL ALTERNATIVE.** Framework uses LLM vision as primary interaction mechanism for browser automation (Skyvern v24). Alternative paradigm to DOM-based (crawl4ai + Playwright + Selenium + Cypress). Trade-offs: vision more robust + handles pure-image; DOM faster + cheaper + deterministic. Pattern narrows to vision-specific, not "DOM-free" as universal novelty.

### Refinement for Pattern #48 Proprietary Anti-Bot Commercial Moat

**Original (v24):** Framework gates anti-bot capabilities to paid tier as commercial differentiator.

**Counter-evidence (v29):** crawl4ai has comprehensive OSS anti-bot (3-tier + proxy + Shadow DOM).

**Refined formulation:**
> **#48 Proprietary Anti-Bot COMMERCIAL Moat.** Specifically: anti-bot capabilities gated to proprietary/paid tier as commercial differentiation strategy. crawl4ai demonstrates anti-bot itself can be OSS; moat-specificity is commercial-gating, not anti-bot capability. Pattern narrows to specifically-proprietary-gated anti-bot.

### Introduces Pattern #64 as OSS counterpart

See next section.

## 5. 3 new pattern candidates

### Pattern #64 Open-Source Anti-Bot Detection

**Definition:** Framework implements comprehensive anti-bot detection + evasion capabilities open-source (not commercial-gated). Typically: tiered detection, proxy escalation, Shadow DOM flattening, stealth mode, consent popup handling.

**Evidence N=1:**
- crawl4ai v0.8.5: 3-tier detection + proxy escalation + Shadow DOM + consent popup removal + stealth mode

**Distinct from #48 (proprietary moat):** #64 is OSS counterpart.

**Promotion criteria:** 2+ frameworks with comprehensive OSS anti-bot (≥3 features).

### Pattern #65 4-Tier Sponsorship Monetization

**Definition:** Solo-project monetization via explicitly tiered sponsorship ($5-$2000/mo structured benefits). Tiers target different user segments (believers / builders / teams / enterprises). Distinct from unstructured GitHub Sponsors; distinct from LLC; distinct from open-core.

**Evidence N=1:**
- crawl4ai: $5 Believer / $50 Builder / $500 Growing Team / $2000 Data Infrastructure Partner

**Distinct from corpus peers:**
- OMC v27: generic GitHub Sponsors (unstructured)
- BMAD v11: LLC formalization
- fish-speech/Skyvern: open-core

**Promotion criteria:** 2+ solo project with ≥4 structured sponsorship tiers + tier-specific benefits.

### Pattern #66 Supply-Chain Security Incident Response

**Definition:** Framework documents upstream supply-chain compromise + emergency response in public README. Transparency-first security posture.

**Evidence N=1:**
- crawl4ai v0.8.6: replaced `litellm` with `unclecode-litellm` fork due to PyPI supply-chain compromise; prominent README disclosure

**Corpus first:** first documented supply-chain incident response in Storm Bear corpus.

**Promotion criteria:** 2+ frameworks documenting supply-chain incident response publicly.

## 6. Pattern #31 Open-Core 3rd data point PENDING

### Current state

Pattern #31 (CONFIRMED v24): N=2 (fish-speech v20 + Skyvern v24).

### crawl4ai's trajectory

- **OSS core:** Apache-2.0, `pip install crawl4ai`
- **Cloud API Closed Beta:** launching soon
- **Future formal entity:** possibly unclecode LLC or similar (undeclared)

**3rd data point will validate** when Cloud API launches. Current v29 = pending.

### Post-v29 Pattern #31 projected

| # | Framework | OSS | Commercial |
|---|-----------|-----|-----------|
| 1 | fish-speech v20 | Apache-2.0 core | 39 AI INC enterprise |
| 2 | Skyvern v24 | AGPL core | Skyvern-AI cloud |
| **3 (future)** | **crawl4ai v29+** | **Apache-2.0** | **Cloud API** |

## 7. Pattern Library state post-v29

### Counts

| Category | Count | Change |
|----------|-------|--------|
| Confirmed | 27 | 0 |
| Refined (subset of Confirmed) | 9 | 0 (Patterns #47, #48 formulations adjusted but not incremented — refined status tracked separately) |
| Active Candidate | **32** | +3 (#64, #65, #66) |
| Stale-Candidate | 3 | 0 |
| Retired | 4 | 0 |
| **Active library** | **62** | +3 |
| **Full library** | **66** | +3 |

### Ratio

**32:27 = 1.19:1 — AUDIT TRIGGER HIT (3rd consecutive wiki)**.

### Audit cadence concern escalates

| Wiki | Post-wiki ratio | Trigger |
|------|-----------------|---------|
| v25 audit | 0.74:1 | Cleared |
| v26 | 0.81:1 | Clear |
| v27 | 1.00:1 | HIT |
| v27 audit | 0.93:1 | Cleared |
| v28 | 1.07:1 | HIT (2nd consecutive wiki) |
| v29 | 1.19:1 | HIT (3rd consecutive wiki) |

**Trend:** ratio climbing. Candidate accumulation exceeds consolidation. Audit urgency HIGH.

## 8. Storm Bear pilot ranking at v29

### Updated ranking

1. spec-kit v17 (methodology)
2. OMC v27 (Scrum-ceremony alignment)
3. BMAD v11 (VN methodology)
4. markitdown v28 (document ingestion)
5. **crawl4ai v29 🆕** (web research utility)
6. gws v13 (VN enterprise)
7. codymaster v12 (VN peer-category)
8. multica v15 (Linear-analog)
9. graphify v16 (vault-applicability)
10. agency-agents v18 (144 agents)

**crawl4ai at #5** — direct web research utility, composable with markitdown v28. Solo author caveat moves it below Microsoft-stability markitdown.

## 9. Emergent corpus patterns

### 3 consecutive solo-enterprise-scale wikis (v27, v28, v29)

- v27 OMC: solo Korean 30K
- v28 markitdown: Microsoft corporate 114K (NOT solo)
- v29 crawl4ai: solo unclecode 64K

**Solo dominant recently.**

### Multi-pattern strengthening visible

Recent wikis simultaneously strengthen multiple confirmed patterns:
- **Pattern #27 Community-Viral:** 7 data points total, 4 in recent 4 wikis
- **Pattern #20 Solo-Scale Ceiling:** dictionary grows 3 rows in 3 wikis
- **Pattern #28 Multi-Provider AI Support:** 5 data points, 2 recent

### Pattern Library matures

Confirmed patterns persist + accumulate data. Candidate churn continues.

## 10. Strategic implications

### Corpus maturity

Post-v29, corpus has:
- 29 wikis
- 6 tiers occupied (5 tier + outside-scope)
- 27 confirmed patterns
- 32 active candidates + 3 stale + 4 retired
- 20 consecutive Storm Bear meta-entities

**Corpus is structurally mature.** New patterns emerge naturally; old patterns retire or strengthen.

### Audit urgency

**3rd consecutive audit trigger + 1.19:1 ratio trajectory** = Pattern Library entering unstable state. Must audit before v30 at latest.

### Corpus-application phase continues

v27 Storm Bear vault diagnostic + v28 markitdown + v29 crawl4ai = utility-focus phase. Storm Bear pilot ranking now at #5 (3 new pilot candidates in 3 wikis).

## 11. Related concepts

- [[(C) index]]
- [[(C) Browser Orchestration + Markdown Pipeline + BM25 Filtering]]
- [[(C) Open-Source Anti-Bot Detection + Pattern 47 48 Refinement]]
- [[(C) Solo-Enterprise-Scale 3rd Corpus Data Point + 4-Tier Sponsorship + Pattern 31 Candidate]]
- [[(C) T4 Extends to N=6 + Storm Bear Web-Research Applicability + Meta]]
- PATTERN_LIBRARY.md post-v29 state

## 12. References

- Cross-corpus T4 analysis (v7, v13, v16, v19, v28, v29)
- Pattern Library history (v24 registration of #47, #48; v29 refinement)
- 28 prior iteration logs

## 13. Edges + limitations

- **T4 saturation approaching** — 6 archetypes at N=6, diminishing returns per new entry
- **Pattern #47 + #48 refinement** is judgment call (refinement vs new-pattern split)
- **3 candidates at N=1** — stale-flag risk at v34 if no follow-on
- **Pattern #31 3rd data point contingent** on Cloud API launch (speculative)
- **Audit cadence urgency** — 3 consecutive wikis triggering; structural issue
- **Solo-enterprise-scale ceiling observation** — N=3 may not be sufficient for formal ceiling value

---

**v29 Phase 4b = T4 extends to N=6 + Pattern #47/#48 refinements + 3 new candidates (#64-66) + Pattern #31 3rd data point pending + audit trigger 3rd consecutive wiki. crawl4ai is Storm Bear pilot #5. 20th consecutive Storm Bear meta. 11th v2 routine execution.**
