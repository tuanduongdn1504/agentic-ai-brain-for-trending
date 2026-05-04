# (C) T4 5-Way Comparison + Pattern 17 Variant 5 Validation (Phase 4b v28)

> **Type:** Phase 4b deliverable — T4 tier extension + Pattern #17 variant 5 structural validation + 4 new candidate registrations
> **Project:** v28 markitdown
> **Date:** 2026-04-22
> **Parent:** [[(C) index]]
> **Primary focus:** T4 extends to N=5 + variant 5 N=2 validation (HuggingFace + Microsoft) + 4 new candidates (#60-63) + Storm Bear pilot #4 elevation

---

## 1. Executive summary

v28 markitdown extends **Tier 4 Agent-as-bridge to N=5** — T4 becomes 3rd tier reaching N≥5 (after T1 N=9). Adds **T4e official-corporate-narrow-utility** archetype. **Validates Pattern #17 variant 5 (ecosystem-scale commercial platform) at N=2** with Microsoft joining HuggingFace — structurally unambiguous promotion-candidate. Registers **4 new pattern candidates** (#60-63). **Audit trigger RE-HITS** at 29:27 ratio post-candidates.

## 2. T4 5-way matrix (20-axis)

### Roster

| # | Wiki | Version | Author | Stars | Archetype |
|---|------|---------|--------|-------|-----------|
| 1 | notebooklm-py | v7 | teng-lin | ~300 | T4b unofficial-solo-narrow |
| 2 | gws | v13 | Google (corporate) | 25K | T4a official-corporate-broad |
| 3 | graphify | v16 | safishamsi | 30K | T4c solo-broad-local |
| 4 | TrendRadar | v19 | sansan0 (CN) | 52.1K | T4d solo-broad-external |
| 5 | **markitdown** | **v28** | **Microsoft AutoGen Team** | **114K** | **T4e NEW official-corporate-narrow-utility** |

### 20-axis comparison

| Axis | notebooklm-py v7 | gws v13 | graphify v16 | TrendRadar v19 | **markitdown v28** |
|------|------------------|---------|--------------|---------------|-------------------|
| **Stars** | ~300 | 25K | 30K | 52.1K | **114K** |
| **License** | MIT | Apache-2.0 | MIT | GPL-3.0 | **MIT** |
| **Language** | Python | Rust 98.8% | Python 100% | Python | **Python 3.10+** |
| **Organization** | Solo | Google corporate | Solo | Solo CN | **Microsoft corporate (AutoGen Team)** |
| **Region** | Unclear | US | Unclear | CN | **US** |
| **Purpose** | NotebookLM API bridge | Google Workspace CLI | Knowledge graph builder | News aggregator | **File → Markdown converter** |
| **Scope breadth** | Narrow (1 service) | Broad (11+ services) | Broad (files + code + media) | Broad (11 platforms) | **Narrow (11 formats, 1 task)** |
| **Official publisher status** | Unofficial | **Official Google** | Unofficial | Unofficial | **Official Microsoft** |
| **Primary surface** | Python + CLI + Skill | CLI + Python | CLI + Skill | Python + GH Actions | **CLI + Python + Docker** |
| **Surfaces (count)** | 3 | 2+ | 2 | 2 | **3** |
| **Plugin system** | None | None | None | None | **`#markitdown-plugin` hashtag + `markitdown-ocr`** |
| **LLM integration** | None | Model Armor safety | Claude vision | LiteLLM 100+ | **`llm_client` DI + Azure DocIntel** |
| **Governance depth** | Light (solo) | Tri-file corporate | Medium + SECURITY.md | Medium | **Microsoft CLA + COC + Security + Devcontainer** |
| **Distribution** | pip | cargo + brew | pip | pip | **pip + Docker + uv-compat** |
| **i18n** | EN only | EN only | en+ja+ko+zh | CN+EN | **EN only** |
| **Community scale** | Tiny | Google-corporate-backed | 30K community | CN-viral | **114K corporate-amplified** |
| **Pattern #18 OpenClaw** | N/A | ❌ (corporate opt-out) | ✅ | ✅ | **N/A (library, not agent framework)** |
| **Pattern #22 AGENTS.md** | No | Yes (tri-file) | Yes | No | **No (library, correct deviation)** |
| **Pattern #24 SECURITY.md** | No | Yes | Yes (first-party) | No | **Yes (probable) + explicit README section** |
| **Pattern #27 Community-Viral** | No | Corporate-amplified | Solo-scale | CN-viral | **Corporate-amplified 6th path** |

## 3. T4 archetype quadrant coverage at N=5

### Multi-axial placement (organizational × scope × scale)

**Organization × Scope grid:**

| | Narrow scope | Broad scope |
|---|--------------|-------------|
| **Official-corporate** | **T4e markitdown (114K) ← NEW** | T4a gws (25K) |
| **Solo-unofficial-local** | T4b notebooklm-py (~300) | T4c graphify (30K) |
| **Solo-unofficial-external** | — | T4d TrendRadar (52.1K) |

**Coverage 5 of 6 quadrants** (missing: solo-narrow-external).

### Scale observations

- **Corporate narrow** > solo narrow by 380× (114K vs 300)
- **Corporate narrow** > corporate broad by 4.5× (114K vs 25K)
- **Narrow-utility outperforms broad-bridge** at top scale (markitdown > gws)

**Hypothesis:** Narrow single-purpose utilities easier to demonstrate and adopt than broad multi-service bridges. Corporate backing + narrow utility = scale multiplier.

## 4. Pattern #17 variant 5 N=2 validation

### Variant 5 definition (from v26 formalization)

> **Variant 5: Ecosystem-scale commercial platform.** Organization >$1B valuation + multiple products + OSS + commercial tier + >10 years operational.

### N=2 evidence

| Dimension | HuggingFace (v26) | Microsoft (v6 + v28) |
|-----------|-------------------|----------------------|
| Age | ~10 years | ~50 years |
| Valuation | ~$4.5B (2023 reported) | ~$3T market cap |
| Core identity | AI/ML-focused | Broad computing |
| OSS products | 14+ (Hub, Transformers, Datasets, Spaces, smolagents, Inference, Learn, etc.) | Hundreds (VS Code, TypeScript, PowerShell, AutoGen, .NET, markitdown, etc.) |
| Commercial tier | Pro + Enterprise Hub + Inference Endpoints | Azure (all services) |
| Corpus entries | 1 (HF agents-course T3) | 2 (ai-agents-for-beginners T3 + markitdown T4) |
| **Variant 5 match** | ✅ | ✅ |

### Structural coherence assessment

Differences are **within-variant variation** not cross-archetype distinction:
- Scale-of-scale variation (4.5B vs 3T) — both exceed $1B threshold
- Domain-breadth variation (AI/ML-only vs multi-domain) — both are ecosystem-scale
- Corpus-entry variation (1 vs 2) — both visible in corpus

**Unambiguous variant match at N=2.** Meets formal "structurally unambiguous at N=2" criterion per Pattern Library promotion rules.

### Recommendation

**Promote variant 5 from candidate-variant to confirmed-variant** within Pattern #17 formal statement. Pattern #17 itself was confirmed at v15; v28 refines variant classification.

### Pattern #17 post-v28 variant state (after v28 audit)

| # | Variant | Status | N |
|---|---------|--------|---|
| 1 | Individual-led-dev | Confirmed | 1 |
| 2 | Big-tech curator | Confirmed | 2 |
| 3 | Individual-led-dev solo-brand | Confirmed | 1 |
| 4 | Commercial-startup ecosystem | Confirmed | 1 |
| **5** | **Ecosystem-scale commercial platform** | **✅ PROMOTED at v28** | **2 (HF + Microsoft)** |
| 6 | Individual-multi-runtime-publisher | Confirmed | 1 |

**Variant 5 first variant to reach structurally-unambiguous N=2 within Pattern #17.**

## 5. 4 new pattern candidates

### #60 AutoGen-Extension Ecosystem Archetype

**Definition:** Sub-pattern within Pattern #17 variant 5 — ecosystem-scale commercial platform spawns sub-ecosystem (AutoGen) which publishes official extensions (markitdown).

**Evidence:** Microsoft > AutoGen Team > markitdown.

**N=1.** Promote at 2+ ecosystem-scale commercial platforms with similar sub-ecosystem structure.

### #61 LLM-Client DI Pattern

**Definition:** Library accepts `llm_client` as dependency-injected parameter for optional LLM features. Duck-typed OpenAI-compatible interface. Core works without client.

**Evidence:** markitdown `MarkItDown(llm_client=OpenAI(), llm_model="gpt-4o")`.

**Distinct from Pattern #28 Multi-Provider AI Support:** #28 is framework-level routing; #61 is library-level DI contract.

**N=1.** Promote at 2+ libraries with similar `llm_client`-DI optional-feature pattern.

### #62 Hashtag-Based Plugin Discovery

**Definition:** Framework enables plugin discovery via public-social-media hashtag (e.g., GitHub repo topics `#markitdown-plugin`) rather than centralized marketplace.

**Evidence:** markitdown `#markitdown-plugin` hashtag.

**Contrast with:** spec-kit 80+ marketplace + OMC Claude Code plugin marketplace + BMAD community modules — all centralized.

**N=1.** Promote at 2+ frameworks with hashtag-based plugin discovery.

### #63 Format-Scoped Optional Dependencies

**Definition:** Library uses pip extras (`[format]`) to scope install size per-feature.

**Evidence:** `pip install 'markitdown[pdf, docx, pptx]'`.

**N=1.** Promote at 2+ Python corpus libraries with per-format optional deps.

## 6. Pattern Library state post-v28

### Counts

| Category | Count | Change from v27 audit |
|----------|-------|-----------------------|
| Confirmed | 27 | 0 (variant 5 promoted within #17; not new confirmed) |
| Active Candidate | **29** | +4 (#60-63) |
| Stale-Candidate | 3 | 0 |
| Retired | 4 | 0 |
| **Active library total** | **59** | +4 |
| **Full library total** | **63** | +4 |

### Ratio

**29:27 = 1.07:1 — AUDIT TRIGGER HIT** (>1:1).

Also: candidate count 29 ≥ 28 threshold HIT.

**Both triggers crossed. Audit required before v29.**

### Audit trigger cadence observation

| Wiki | Post-wiki ratio | Trigger status |
|------|-----------------|----------------|
| v25 audit | 0.74:1 | Cleared |
| v26 | 0.81:1 | Clear |
| v27 | 1.00:1 | HIT |
| v27 audit | 0.93:1 | Cleared |
| v28 | 1.07:1 | **HIT (2nd consecutive wiki)** |

**Observation:** v27 audit cleared 1.00:1 → 0.93:1, but v28 pushed back to 1.07:1 in 1 wiki. **Audit-to-trigger cadence = 1 wiki.** Pattern Library is growing candidates faster than can consolidate.

**Implication for v2.1 routine:** post-audit, next wiki likely triggers again unless candidate-density reduces. Consider:
- Stricter candidate-registration criteria
- Pre-registration candidate review against existing patterns
- Longer audit window (clear more candidates per audit)

## 7. T4 emergent patterns at N=5

### Pattern A — Narrow-utility > broad-bridge at scale

markitdown 114K (narrow) >> gws 25K (broad) → narrow single-purpose wins.

### Pattern B — Corporate-backing amplifies (same Pattern #12 refined)

2 corporate T4 (gws + markitdown) both document-heavy governance. 3 solo T4 lighter governance. Pattern #12 holds at T4.

### Pattern C — T4 is largest scale tier for non-corporate solo

TrendRadar 52.1K solo-broad ceiling. markitdown corporate 114K crushes solo ceiling.

### Pattern D — T4 archetype saturation approaching

5 distinct archetype variants at N=5. Future T4 additions harder to justify as "genuinely different."

## 8. Storm Bear pilot ranking updated at v28

### New ranking (post-v28)

1. **spec-kit v17** (corporate SDD methodology)
2. **OMC v27** (Scrum-ceremony alignment)
3. **BMAD v11** (VN methodology + 45K)
4. **markitdown v28 🆕** (**direct utility for Scrum-doc ingestion**)
5. gws v13 (VN enterprise + Google)
6. codymaster v12 (VN peer-category)
7. multica v15 (Linear-analog team UX)
8. graphify v16 (vault-applicability direct)
9. agency-agents v18 (144 agents)

### Rationale for markitdown at #4

- **Direct utility** — immediate Scrum-doc ingestion value
- **Low commitment** — one-time per document (not daily-workflow)
- **Low risk** — MIT + Microsoft stability
- **Low install friction** — pip + 1 CLI command
- **High composability** — works alongside spec-kit/OMC/BMAD methodologies

## 9. Strategic implications

### Corpus coverage signals

- T4 N=5 with 5 archetypes = most-archetype-diverse tier per-entry
- Microsoft 2nd corpus entrant = ecosystem-scale platform getting corpus representation
- Pattern #17 variant 5 N=2 = first within-pattern variant reaching structural N=2

### v28 audit cadence concern

2 consecutive audits needed (v27, v28) = candidate accumulation faster than consolidation. **Possible corrective actions:**
1. Pre-registration candidate review (reject overlap with existing)
2. Stricter novelty threshold (2-pattern-minimum-difference from existing)
3. Longer stale-wait before retirement (10+ wikis harder to reach)

### v29+ options

1. **AUDIT REQUIRED before v29** (2nd consecutive)
2. **Storm Bear vault action bundle** (HIGH priority 5-action from v27 diagnostic still pending)
3. **Browser-agent peer** (browser-use) — validate #47 + #48 at N=2
4. **2nd Korean T1 wiki** — validate #55 at N=2
5. **Routine v2.1 refactor** (162+ cumulative action items)

## 10. 4 new candidate density observations

### Density vs prior wikis

| Wiki | New candidates | Total corpus candidates post-wiki |
|------|----------------|-----------------------------------|
| v25 awesome-design-md | 4 | 24 |
| v26 HF agents-course | 2 | 22 (post-v25 audit = 20 → +2) |
| v27 OMC | 5 | 27 |
| v28 markitdown | 4 | 29 (post-v27 audit = 25 → +4) |

**Average 3.75 new candidates per recent wiki.** Consistent with architectural-novelty phase.

### Cumulative audit cost

Each audit = ~2-3 hours labor (per v27 audit example). If audit needed per 1-2 wikis, **audit-cost dominates** wiki-cost.

**Routine v2.1 action:** formalize "mini-audit on audit trigger" as lightweight 30-min rebalancing vs full 2-hour audit. Prevents audit overhead from blocking wiki throughput.

## 11. Related concepts

- [[(C) index]]
- [[(C) 11-Format Support + Optional Dependencies + Scoped APIs]]
- [[(C) Microsoft AutoGen Team + Corporate Governance + Pattern 17 Variant 5 Validation]]
- [[(C) LLM-Client DI Pattern + Plugin Hashtag Discovery + 4 New Candidates]]
- [[(C) T4 Extends to N=5 + Storm Bear Vault Applicability + Meta]]
- PATTERN_LIBRARY.md (post-v28 state)

## 12. References

- cross-corpus T4 analysis (v7 + v13 + v16 + v19 + v28)
- Pattern #17 state history (v15 confirm + v25 refine + v26 variant registration + v28 variant promotion)
- 27 prior iteration logs
- 3 Pattern Library audit documents (v21 + v25 + v27)

## 13. Edges + limitations

- **T4 saturation approaching** — future T4 additions face "genuinely different" bar
- **Pattern #17 variant 5 promotion** is judgment call (structurally-unambiguous-at-N=2 threshold)
- **4 new candidates at N=1** — high stale-flag risk at v33 audit
- **Audit cadence concern** — candidate accumulation > consolidation rate
- **Storm Bear pilot ranking subjectivity** — weighting between methodology/utility/regional not systematic
- **Microsoft corpus coverage** remains partial (2 of potentially 10+ Microsoft AI/agent products)

---

**v28 Phase 4b = T4 extends to N=5 + Pattern #17 variant 5 N=2 validation (promotion candidate) + 4 new candidates (#60-63) + audit trigger re-hit at 29:27 = 1.07:1. markitdown is Storm Bear pilot #4. 19th consecutive Storm Bear meta. 2nd consecutive audit required.**
