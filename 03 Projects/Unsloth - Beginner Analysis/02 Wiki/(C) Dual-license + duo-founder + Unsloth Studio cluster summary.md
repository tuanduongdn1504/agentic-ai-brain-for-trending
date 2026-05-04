# (C) Dual-license + duo-founder + Unsloth Studio cluster summary

> **Cluster:** Dual-licensing strategy (Apache core + AGPL UI) + Han brothers duo-founder archetype + Unsloth Studio WebUI
> **Parent:** [[(C) index]]
> **Sources:** LICENSE files + README attribution + Unsloth Studio description
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Dual-licensing** — Apache-2.0 (core) + AGPL-3.0 (Studio UI) — first in corpus
2. **Duo-founder + team archetype** — Daniel Han + Michael Han + Unsloth team — 10th organizational archetype
3. **Unsloth Studio WebUI** — AGPL-3.0 separate UI product

## 2. Dual-licensing strategy (first in corpus)

### License split

| Component | License | Rationale |
|-----------|---------|-----------|
| **Unsloth Core** (library, CLI, Python API) | **Apache-2.0** | Permissive for commercial code reuse + integration |
| **Unsloth Studio** (WebUI, interface) | **AGPL-3.0** | Strongest copyleft; SaaS must share source |

### Strategic rationale

**Apache-2.0 core:**
- Enables LlamaFactory-like platforms to integrate Unsloth as performance library
- No commercial barrier
- Standard OSS norm
- Maximizes ecosystem adoption

**AGPL-3.0 Studio:**
- If cloud vendor deploys Unsloth Studio as SaaS → must release source
- Prevents competitor from vendorizing Unsloth Studio UI as paid service
- Protects Unsloth team's UI investment
- Forces "either open or build your own" choice for would-be commercial forks

### Pattern #45 candidate formalization

**Formal statement (candidate):**
> Dual-licensing strategy: framework splits license between core library (permissive) and UI/deployment layer (strong copyleft). Enables ecosystem adoption for code reuse while protecting UI/service differentiation against commercial appropriation. AGPL-3.0 UI specifically prevents SaaS-vendorization.

**Evidence at v23:** 1 (Unsloth — Apache core + AGPL Studio UI).

**Required for promotion:** 2+ similar dual-license structures.

**Prediction:** Medium-likely — as OSS frameworks mature, dual-licensing emerges as business-model-preservation strategy. MongoDB + similar precedents outside corpus.

### AGPL-3.0 — first in corpus

**Corpus license distribution post-v23:**

| License | Count | Wikis |
|---------|-------|-------|
| MIT | 16 | majority |
| Apache-2.0 | 3 | gws v13 + LlamaFactory v22 + **Unsloth v23 (core)** |
| ISC | 1 | codymaster v12 |
| GPL-3.0 | 2 | TrendRadar v19 + system-prompts-leaks v21 |
| **AGPL-3.0** | **1** | **Unsloth Studio v23 (FIRST)** |
| CC0 | 1 | build-your-own-x v8 (content) |
| Custom non-OSI | 1 | fish-speech v20 |

### Pattern #29 (License-Category Diversity, confirmed v21) +1 data point

Non-permissive corpus distribution post-v23:
- **Copyleft:** GPL-3.0 × 2 + AGPL-3.0 × 1 = 3
- **Custom non-OSI:** 1
- **Total non-permissive:** 4 of 23 wikis (17%)

Pattern #29 continues to accumulate evidence.

## 3. Duo-founder + team archetype

### The Han brothers

From citation:
> *"Daniel Han, Michael Han and Unsloth team"*

Same surname + team framing suggests:
- **Likely brothers** (Han brothers duo-founder pattern)
- **Or close collaborators** (less likely given name match)
- **Team size unknown** — "Unsloth team" implied but not enumerated

### Distinct from prior corpus archetypes

| Archetype | Examples | Distinction from Unsloth |
|-----------|----------|---------------------------|
| Pure-solo known | Karpathy, Jesse Vincent, sansan0 | Single individual |
| Solo formalized LLC | BMad Code | Solo with legal entity |
| Solo VN-context | Tody Le | Regional solo |
| Corporate official | Google, GitHub, ByteDance | Pre-existing corporation |
| Community-ambiguous | paperclip, GSD | Anonymous/unclear |
| Education corporate | Microsoft | Pre-existing education-vertical |
| Open-core commercial | 39 AI INC | Commercial entity with OSS funnel |
| Pseudonymous | x1xhlol | Intentional anonymity |
| Academic-lab | hiyouga + Lab4AI | University research backing |
| **Duo-founder + team** | **Daniel Han + Michael Han + Unsloth team** | **2 co-founders + unnamed team** |

### Pattern #46 candidate formalization

**Formal statement (candidate):**
> 10th organizational archetype: duo-founder + team. Two co-founders (often siblings or close collaborators) + unnamed/informal team. Distinct from pure-solo (1 person), LLC (formalized legal), corporate (pre-existing), academic-lab (university), pseudonymous (anonymous), community-ambiguous (unclear). Common in modern AI startups with minimal disclosure.

**Evidence at v23:** 1 (Han brothers + Unsloth team).

**Required for promotion:** 2+ duo-founder frameworks.

**Prediction:** Medium-likely — AI startup landscape has many similar duo-founder patterns (Anthropic founders, Mistral founders, etc.). May validate with next startup-backed framework in corpus.

### Organizational archetype count post-v23

**10 organizational archetypes now documented in corpus.** Pattern #19 + #44 + #46 progressively map the organizational-structure space of agent-adjacent OSS.

## 4. Unsloth Studio WebUI

### What Studio is

- Web-based UI for training + running models
- Local inference (Gemma 4 / Qwen3.5 / DeepSeek / gpt-oss)
- Point-and-click fine-tuning interface
- Alternative to CLI for non-coding users

### License rationale (AGPL-3.0)

- **Commercial SaaS deployment:** must release source to users
- **Private deployment:** can modify without sharing (local use)
- **Community contributions:** welcomed, copyleft preserved

### Parallel to LlamaFactory's LLaMA Board

Both:
- Gradio-based (likely)
- Local WebUI for fine-tuning
- Model selection + hyperparameter config
- Training launch + monitoring

Differences:
- LlamaFactory LLaMA Board: Apache-2.0 (same as core)
- **Unsloth Studio: AGPL-3.0** (distinct from Apache core)

### Strategic implication

Unsloth team's license choice signals:
- UI as primary commercial protection surface
- Core library maximum permissive for ecosystem adoption
- Future monetization may come via Studio (cloud-hosted? managed?)

## 5. Company structure (inferred)

### Unsloth AI

- Organization name: **Unsloth AI**
- Incorporation: unclear (not disclosed)
- Funding: unclear (not disclosed)
- Headquarters: unclear
- Headcount: unclear ("team" mentioned)

### Possible structures

1. **Y Combinator / Techstars startup** (common for 2023-era AI startups)
2. **Bootstrap duo-founder** (Han brothers self-funded)
3. **Research-spinoff** (from prior lab work)
4. **VC-backed stealth** (funding not disclosed yet)

### Cross-framework comparison

| Framework | Disclosure level |
|-----------|-------------------|
| fish-speech v20 | Legal entity 39 AI INC revealed via LICENSE |
| BMAD v11 | LLC formalized (BMad Code LLC) |
| LlamaFactory v22 | Academic-lab affiliation (Lab4AI) |
| **Unsloth v23** | **Minimal — Unsloth AI name only; Han + team** |

Unsloth = **minimal-disclosure** pattern. Signals startup/scale-up phase where organizational structure is secondary to product.

## 6. No academic publication or affiliation

### Distinct from LlamaFactory

| Dimension | LlamaFactory v22 | Unsloth v23 |
|-----------|-------------------|--------------|
| arXiv preprint | 2403.13372 | None |
| Peer-reviewed publication | ACL 2024 | None |
| Academic-lab affiliation | Lab4AI | None |
| Research paper co-authors | Multiple | N/A |

### Scope refinement — Patterns #42 + #44

**Pattern #42 Academic-Published Peer-Reviewed Framework (candidate):**
- LlamaFactory validates
- Unsloth does NOT validate
- **Scope refinement:** #42 correlates with academic-lab affiliation, not universal in training-infra space
- Remains N=1 candidate

**Pattern #44 Academic-Lab Affiliation Archetype (candidate):**
- LlamaFactory validates (Lab4AI)
- Unsloth does NOT validate (Unsloth AI company)
- **Scope refinement:** #44 is specific to academic-lab, not all research-heavy frameworks
- Remains N=1 candidate

### Informative failure

Unsloth failing to validate #42 + #44 IS informative — refines scope of those patterns. Not all training-infrastructure frameworks are academic-lab-affiliated. Company/duo-founder archetype (like Unsloth) = distinct pathway.

## 7. Research-paper-chain lineage (Pattern #32 data point #3)

### Acknowledged predecessors

From README citations:
- **llama.cpp** (ggerganov) — inference engine
- **HuggingFace** (transformers, TRL) — ecosystem foundation
- **PyTorch** (Meta) — ML framework
- **Torch AO** (PyTorch) — architecture optimizations
- **NVIDIA NeMo DataDesigner** — data tooling

### Shorter than LlamaFactory's lineage

- LlamaFactory: **PEFT + TRL + QLoRA + FastChat + 100+ research projects**
- fish-speech: **7 research citations**
- **Unsloth: ~5 acknowledged predecessors** (less formal citation format)

### Pattern #32 confirmed N=3 post-v23

Pattern #32 (Research-Paper-Chain Lineage) confirmed at v22. Unsloth adds 3rd data point:
- fish-speech v20 (outside-scope foundation-model) — 7 citations
- LlamaFactory v22 (outside-scope training-infra) — foundation + 100+
- **Unsloth v23 (outside-scope training-infra) — 5 acknowledged predecessors**

**Pattern #32 now N=3** across 2 outside-scope sub-types. Further strengthens confirmed pattern.

### Lineage depth variability

Interesting: Pattern #32 data points vary in citation depth:
- fish-speech: academic-style formal citations (7 research projects)
- LlamaFactory: academic-style formal (foundation + 100+ research)
- Unsloth: README-acknowledgements style (shorter list, informal)

Pattern may need sub-classification at N=4+ if depth variability proves structural.

## 8. Comparison with LlamaFactory (co-validator)

| Dimension | LlamaFactory v22 | Unsloth v23 |
|-----------|-------------------|--------------|
| License | Apache-2.0 | **Dual: Apache + AGPL** |
| Author archetype | Academic-lab (Lab4AI) | **Duo-founder company (Han + team)** |
| Academic publication | ACL 2024 | **None** |
| Disclosure level | Academic affiliation + paper co-authors | **Minimal (company + team)** |
| Research lineage | Extensive academic-style | **Shorter informal acknowledgements** |

**Same outside-scope sub-type (training-infra); different organizational patterns.** Validates Pattern #41 structurally while refining Pattern #42 + #44 scope.

## 9. Key observations

### Cluster-level

- **Dual-licensing** (Apache core + AGPL UI) — first in corpus; Pattern #45 candidate
- **Han brothers duo-founder** — 10th organizational archetype; Pattern #46 candidate
- **AGPL-3.0** — first in corpus; strengthens Pattern #29
- **No academic publication** — distinct from LlamaFactory; refines Pattern #42 scope
- **No academic-lab affiliation** — distinct from LlamaFactory; refines Pattern #44 scope

### Cross-corpus

- **Pattern #29 License-Category Diversity** — adds AGPL-3.0 (N=4 non-permissive total)
- **Pattern #32 Research-Paper-Chain Lineage** — adds 3rd data point (N=3 now)
- **Pattern #45 Dual-Licensing Strategy** — NEW candidate
- **Pattern #46 Duo-Founder + Team Archetype** — NEW candidate
- **Patterns #42 + #44 scope refinement** — academic-lab-correlated, not universal

## 10. References

- Parent: [[(C) index]]
- Source: LICENSE files (Apache + AGPL) + README attribution + Unsloth Studio description
- Sibling clusters: [[(C) README + performance claims + 500 models cluster summary]] + [[(C) Custom Triton kernels + GRPO + consumer-GPU focus cluster summary]]
- LlamaFactory v22 peer: academic-lab contrast
- fish-speech v20: commercial entity contrast

---

**Cluster summary: Dual-licensing (Apache-2.0 core + AGPL-3.0 Unsloth Studio UI) first in corpus — Pattern #45 candidate + Pattern #29 +1 data point (AGPL-3.0). Han brothers duo-founder archetype (10th organizational archetype) — Pattern #46 candidate. No academic publication (distinct from LlamaFactory ACL 2024) — refines Pattern #42 scope. No academic-lab affiliation (distinct from Lab4AI) — refines Pattern #44 scope. Pattern #32 Research-Paper-Chain Lineage +1 data point (N=3 now; shorter/informal citation style).**
