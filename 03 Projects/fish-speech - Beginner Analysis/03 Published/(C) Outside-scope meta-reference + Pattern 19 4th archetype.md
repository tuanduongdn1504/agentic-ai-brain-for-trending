# (C) Outside-scope meta-reference — fish-speech v20 + Pattern #19 4th archetype formalization

> **Purpose:** Document fish-speech as 2nd outside-scope wiki (after build-your-own-x v8). Formalize Pattern #19 4th archetype (research-paper-chain). Refine Pattern #29 to license-category-diversity. Register 5 new pattern candidates (#31-35). Strengthen Pattern #18 regional refinement (2nd CN-ecosystem data point).
> **Parent:** [[(C) index]]
> **Status:** ✅ Phase 4b deliverable, v20 (outside-scope meta-reference mode — 2nd use in corpus)

---

## 1. Why this deliverable

### Outside-scope framing justification

fish-speech is **not an agent framework**. It's a TTS foundation model. Storm Bear's core scope (5-tier taxonomy: T1-T5) doesn't apply. Standard Phase 4b deliverables (N-way comparison, tier extension, taxonomy evolution) are inapplicable.

**Precedent:** build-your-own-x v8 — outside-scope meta-reference deliverable. v8 established "outside-scope" as valid Phase 4b routing mode in v2 routine (16-mode framework).

**v20 extends** outside-scope mode to 2nd use + different sub-type (foundation-model vs v8 education-aggregator). Validates v2 routine's flexibility.

### Pattern discovery justification

Even outside-scope, fish-speech yields significant pattern discovery:
- Pattern #19 4th archetype (research-paper-chain) — major classification expansion
- Pattern #29 refinement (license-category-diversity)
- 5 new pattern candidates (#31-35)
- Pattern #18 regional strengthening
- Pattern #8 most rigorous data point

## 2. Outside-scope classification

### Storm Bear 5-tier taxonomy

| Tier | Definition | fish-speech fit? |
|------|-----------|------------------|
| T1 | Agent-as-assistant (ECC, SP, gstack, GSD, BMAD, codymaster, spec-kit, agency-agents) | ❌ not an assistant |
| T2 | Agent-as-service (goclaw, multica) | ❌ not a service platform |
| T3 | Agent-as-education (course) | ❌ not education |
| T4 | Agent-as-bridge (notebooklm-py, gws, graphify, TrendRadar) | ❌ not a bridge |
| T5 | Agent-as-application (deer-flow, autoresearch, paperclip) | ❌ not an application |
| **Outside** | **Not agent-specific** | **✅** |

### Outside-scope sub-categorization (emerging)

| Sub-type | Wiki | v20 addition? |
|----------|------|---------------|
| Education aggregator | build-your-own-x v8 | — |
| **Foundation-model-as-product** | **fish-speech v20** | **NEW** |

Pattern #35 candidate formalizes foundation-model-as-product as distinct sub-category.

## 3. Pattern #19 4TH ARCHETYPE — research-paper-chain

### Pre-v20 state (3 archetypes, refined v18)

| # | Archetype | Example | Lineage node |
|---|-----------|---------|--------------|
| 1 | Individual-author | Karpathy (autoresearch + touchpoints), John Lam (spec-kit) | Person |
| 2 | Methodology | SDD (GSD + spec-kit), BMAD | Idea system |
| 3 | Community-viral no-lineage | agency-agents (Reddit), TrendRadar (CN community) | None (emergent) |

### v20 addition

| # | Archetype | Example | Lineage node |
|---|-----------|---------|--------------|
| **4** | **Research-paper-chain** | **fish-speech (7 research citations)** | **Research project network** |

### fish-speech lineage decomposition

```
VITS2 ───┐
Bert-VITS2 ───┤
GPT VITS ───┼─→ fish-speech S2 Pro
MQTTS ───┤
GPT Fast ───┤
GPT-SoVITS ───┤
Qwen3 ───┘
```

### Archetype distinctions

| Dimension | (1) Individual | (2) Methodology | (3) Community-viral | (4) Research-chain |
|-----------|----------------|-----------------|---------------------|-------------------|
| Node type | Person | Idea | None | Research project |
| Node count | 1-2 | 1 idea | 0 | 3-10 typical |
| Citation style | "inspired by X" | "based on methodology" | None | "builds on [list]" |
| Domain tendency | Agent frameworks | Methodology frameworks | Community frameworks | Foundation models |
| Typical scale | Small-medium | Medium | Large (viral) | Medium-large |

### Updated Pattern #19 formal statement

> "Frameworks in agent-adjacent space exhibit 4 distinct intellectual-lineage archetypes:
> 1. **Individual-author** — cite specific person(s) as primary influence (node = person)
> 2. **Methodology** — build on shared idea system (node = idea, SDD/BMAD/TDD)
> 3. **Community-viral no-lineage** — emerge from community demand without cited predecessors (node = none)
> 4. **Research-paper-chain** — build on network of cited academic/research projects (node = research project, 3-10 typical)
>
> Archetype distribution varies by space: agent-frameworks skew toward (1-3); foundation-models skew toward (4)."

### Prediction

Foundation-model space will likely populate archetype (4) at N≥3:
- Stable Diffusion cites GAN + diffusion + VAE research chain
- LLaMA-3 cites prior LLM architectures
- Mistral cites MoE + Llama chain
- Gemma cites Gemini + PaLM chain

Storm Bear corpus addition of foundation-model wikis will validate.

## 4. Pattern #29 REFINED — License-Category-Diversity

### Pre-v20 (v19 candidate)

**Pattern #29 GPL-3.0 in Agent-Space:**
> "Copyleft licensing (GPL-3.0, AGPL) emerges as community-preservation commitment in agent-space."

Evidence: 1 (TrendRadar v19)

### v20 refinement

**License diversity expands beyond OSI-approved norms.** Two distinct non-permissive paths:

1. **Copyleft community-preservation** (GPL-3.0) — ensures modifications shared back
2. **Custom non-OSI commercial-funnel** (Fish Audio Research License) — research free, commercial paid

### Refined formal statement

> "License diversity beyond permissive-default (MIT/Apache) expands as frameworks commodify. Two distinct non-permissive paths emerge:
> 1. Copyleft community-preservation (GPL-3.0, AGPL) — enforces derivative-work sharing
> 2. Custom non-OSI commercial-funnel — research-only clauses create paid-tier gateway
>
> Both signal productization boundaries distinct from permissive-OSS norm, with opposite motivations (community-protection vs commercial-protection)."

### Corpus license distribution post-v20

```
Permissive OSI  │██████████████████│ 18 (MIT 16 + Apache 1 + ISC 1)
Copyleft OSI    │█│ 1 (GPL-3.0 TrendRadar)
Public Domain   │█│ 1 (CC0 build-your-own-x content)
Custom non-OSI  │█│ 1 (Fish Audio Research — fish-speech)
```

3 non-permissive data points across 20 wikis. Pattern #29 still candidate (N=2 if counting GPL + custom as related) pending more data.

## 5. 5 new Pattern candidates at v20

### #31 Open-Core Commercial Entity

**Formal statement:**
> "Research-lab-origin organizations operate open-core models — restrictive OSS license funnels interest toward commercial paid tier. Distinct from (a) pre-existing-corp-opens-source (gws, spec-kit, deer-flow) and (b) community-formalized-LLC (BMAD)."

**Evidence at v20:** 1 (fish-speech / 39 AI, INC.)
**Required:** 2+ similar research-lab-commercial entities
**Prediction:** Strong — foundation-model space common pattern

### #32 Research-Paper-Chain Lineage

**Formal statement:**
> "Foundation-model frameworks cite explicit network of prior research projects as intellectual lineage (Pattern #19 4th archetype). Typical citation count: 3-10 prior projects."

**Evidence at v20:** 1 (fish-speech with 7 citations)
**Required:** 2+ frameworks with similar citation pattern
**Prediction:** Strong — foundation-model space default

### #33 Non-OSI Custom License

**Formal statement:**
> "Custom non-OSI-approved licenses emerge in high-value foundation-model space, typically with research-only clauses creating commercial-tier funnel."

**Evidence at v20:** 1 (fish-speech)
**Required:** 2+ similar custom licenses
**Prediction:** Strong — Meta Llama-3, Stable Diffusion, Mistral have comparable

### #34 Anti-Distillation License Clause

**Formal statement:**
> "As foundation models commodify, licenses add anti-distillation clauses prohibiting use of model outputs to train competing foundation models."

**Evidence at v20:** 1 (fish-speech explicit clause)
**Required:** 2+ similar clauses
**Prediction:** Strong — will become standard in foundation-model licenses

### #35 Foundation-Model-as-Product Scope Category

**Formal statement:**
> "Foundation-model-as-product warrants distinct scope category from agent-framework / service / education / bridge / application. Sub-type of outside-scope."

**Evidence at v20:** 1 (fish-speech)
**Required:** 2+ foundation-model outside-scope wikis
**Prediction:** Medium — depends on Storm Bear corpus diversification

## 6. Pattern #18 — regional refinement strengthened

### Pre-v20 state (refined v19)

> "Pattern #18 (refined v19): Runtime standardization (OpenClaw dominant, Hermes secondary) is WESTERN community-platform ecosystem phenomenon. CN-ecosystem uses parallel infrastructure (MCP-direct + LiteLLM + Cherry Studio)."

Adoption rates:
- Western-community-platform: 5/5 (100%)
- Western-corporate: 0/1 (0%)
- CN-community-platform: 0/1 (0%)

### v20 addition

fish-speech = **2nd CN-origin wiki** (first: TrendRadar v19). Both skip OpenClaw/Hermes.

Updated adoption rates:
- Western-community-platform: 5/5 (100%)
- Western-corporate: 0/1 (0%)
- **CN-ecosystem (any archetype): 0/2 (0%)** — strengthened 2nd data point
- **Foundation-model (any region): 0/1 (0%)** — new absent-archetype

### Combined hypothesis

OpenClaw/Hermes adoption appears **regional + archetype-specific**:
- ✅ Western + community-platform: 100%
- ❌ Western + corporate: skip
- ❌ CN-ecosystem (regardless of archetype): skip
- ❌ Foundation-model: skip

Pattern #18 is **layered regional+archetypal refinement**, not universal community-platform-specific.

## 7. Pattern #8 — 5th most-rigorous data point

### Pattern #8 Empirical Research Emergence — corpus history

| # | Wiki | Evidence | Formality |
|---|------|----------|-----------|
| 1 | codymaster v12 | SkillsBench +18.6pp | Framework-internal benchmark |
| 2 | autoresearch v10 | val_bpb metric | Karpathy personal metric |
| 3 | graphify v16 | 71.5× token reduction | Documentation claim |
| 4 | spec-kit v17 | 48× productivity | Documentation claim |
| 5 | **fish-speech v20** | **Seed-TTS WER + EmergentTTS-Eval 81.88% + 2 arXiv preprints** | **Academic peer-review-adjacent** |

### fish-speech rigor leadership

**First corpus framework with:**
- 2 arXiv preprints (2024 v1.4 + 2026 S2)
- Public benchmarks on standard eval suites (not framework-internal)
- Methodology documented at academic paper depth
- Peer-review process (arXiv preprint preparation implies it)

Signals research-first organizational culture (characteristic of research-lab + research-paper-chain archetype pairing).

## 8. Cross-wiki corpus state post-v20

### Corpus taxonomy

| Tier | N | Wikis |
|------|---|-------|
| T1 | 8 | ECC, SP, gstack, GSD, BMAD, codymaster, spec-kit, agency-agents |
| T2 | 2 | goclaw, multica |
| T3 | 1 | course |
| T4 | 4 | notebooklm-py, gws, graphify, TrendRadar |
| T5 | 3 | deer-flow, autoresearch, paperclip |
| Outside | 2 | build-your-own-x, **fish-speech (NEW)** |
| **Total** | **20** | |

**Outside-scope doubled at v20.** Only T3 remains N=1.

### Pattern Library post-v20

| Status | Count | Change |
|--------|-------|--------|
| Confirmed | 20 | 0 |
| Refined | 5 (subset) | +1 (#29 license-diversity) |
| Candidate | 15 | +5 (#31-35) |
| Retired | 0 | — |
| **Total** | **35** | **+5** |

**Ratio:** 15:20 = 0.75:1 (still healthy, well under 2:1)

**⚠️ Audit trigger approaching:** 15 candidates at threshold. Audit candidate if corpus hits 16-17 candidates or 5 more wikis.

## 9. Storm Bear strategic implications

### Pilot ranking updated at v20

| # | Framework | Priority | Rationale |
|---|-----------|----------|-----------|
| 1 | spec-kit | HIGH | Enterprise + SDD + corporate |
| 2 | BMAD | HIGH | VN translation + methodology |
| 3 | gws | HIGH | VN enterprise + Google |
| 4 | agency-agents | MEDIUM | 144 agents ready |
| 5 | codymaster | MEDIUM | VN peer |
| 6 | multica | MEDIUM | Linear-analog |
| 7 | graphify | HIGH (direct, STILL PENDING 4 sessions) | Vault applicability |
| 8 | TrendRadar | LOW-MEDIUM | Pattern observation |
| 9 | **fish-speech** | **LOW** | **Outside-scope + license blocker** |

### Outstanding blockers

- ⚠️ **graphify-on-vault 4+ sessions overdue** since v16 (every v17/v18/v19/v20 iteration log flagged; action not taken)
- **T3 second entrant** still pending (only remaining N=1 tier)
- **Pattern Library audit** candidate after 1-2 more wikis

### Corpus diversification paths

- **Foundation-model space** (fish-speech v20 opened door) — LLaMA / Mistral / Stable Diffusion wikis
- **CN-ecosystem** expansion (fish-speech = 2nd; more CN frameworks would validate Pattern #18 regional)
- **T3 closure** — any agent-education framework beyond course v6
- **Commercial-adjacent** — open-core pattern more data

## 10. v2 Routine evaluation at 2nd execution

### What worked (2nd time)

- ✅ **12-axis Phase 0 classification** — caught outside-scope + custom-license + research-chain at probe
- ✅ **Consolidation guard** — passed (0.5:1 ratio post-v19)
- ✅ **Cross-wiki absence detection** — flagged NO OpenClaw/Hermes, NO LiteLLM (not applicable), NO AGENTS.md as systematic signals
- ✅ **Pattern Library direct update** (Phase 5) — 5 new candidates + 1 refinement to apply
- ✅ **Storm Bear meta-entity** — 11th consecutive wiki (v10-v20) executed automatically
- ✅ **Phase 4b routing decision** — outside-scope mode (2nd use) activated smoothly
- ✅ **Branch fallback** — main worked, no fallback needed

### v2 routine enhancements observed at v20

- **Outside-scope sub-categorization need** — as 2 outside-scope wikis of different sub-types emerge, may need routing sub-mode
- **Research-lineage probe** — v2 could add explicit "count cited predecessors" axis to Phase 0 for Pattern #19 archetype detection
- **Commercial-entity probe** — v2 could add "OSS-with-commercial-entity" check for Pattern #31 detection

These are v2.1 refinement candidates, not blocking.

## 11. Next observation points

### Pattern validation targets

- **Pattern #19 research-chain (4th archetype):** need 2nd foundation-model wiki with similar citation network
- **Pattern #28 LiteLLM:** still N=1 (TrendRadar)
- **Pattern #30 3-layer stratification:** still N=1 (TrendRadar)
- **Pattern #31 open-core commercial:** need 2nd research-lab-commercial
- **Pattern #32 research-chain:** need 2nd foundation-model
- **Pattern #33 non-OSI:** need 2nd custom-license framework
- **Pattern #34 anti-distillation:** need 2nd similar clause
- **Pattern #35 foundation-model scope:** need 2nd foundation-model outside-scope wiki

### Corpus completion targets

- **T3 second entrant** (closes 5/5 tier validation)
- **Pattern #18 CN test** — 3rd CN-origin framework
- **graphify-on-vault** — direct action

## 12. Edges + failure modes

### Outside-scope routing concern

With 2 outside-scope wikis at v20 (build-your-own-x + fish-speech), corpus is accumulating non-agent content. Risk:
- Dilution of Storm Bear agent-focus
- Pattern noise from non-agent frameworks affecting agent-pattern inference

**Mitigation:** Pattern Library should tag which patterns are agent-specific vs cross-space (e.g., Pattern #19 archetypes apply to both; Pattern #18 agent-runtime is agent-specific).

### Pattern #19 4th archetype at N=1

Research-paper-chain archetype has 1 data point. Hypothesis until validation. Should remain candidate in Pattern Library, not confirmed.

### Pattern #31-35 all at N=1

All 5 new candidates are single-observation. Typical validation risk: may not survive 2nd data point.

## 13. References

- Parent: [[(C) index]]
- v8 outside-scope precedent: `../../build-your-own-x - Beginner Analysis/03 Published/(C) Meta-reference — build-your-own-x outside-scope.md` (if exists)
- Pattern Library: `../../../PATTERN_LIBRARY.md`
- v2 routine: `../../../05 Skills/llm-wiki-routine-v2.md`
- Pattern #19 history: GOALS.md v10 onwards

---

**v20 outside-scope meta-reference + Pattern #19 4th archetype (research-paper-chain) formalization. 5 new pattern candidates (#31-35). Pattern #29 refined to license-category-diversity. Pattern #18 regional strengthened (CN N=2). Pattern #8 most rigorous data point (5th). 2nd v2 routine execution validated outside-scope mode handling. Storm Bear pilot relevance LOW (license + outside-scope blockers). graphify-on-vault 4+ sessions overdue.**
