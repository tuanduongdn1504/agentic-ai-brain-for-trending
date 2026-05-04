# (C) Custom LICENSE + 39 AI INC + SGLang production cluster summary

> **Cluster:** Fish Audio Research License (custom non-OSI) + 39 AI, INC. commercial entity + SGLang production inference
> **Parent:** [[(C) index]]
> **Sources:** LICENSE file + README attribution + speech.fish.audio commercial hints
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Fish Audio Research License** — custom non-OSI license (first in corpus)
2. **39 AI, INC.** — legal entity separate from Fish Audio brand (first open-core commercial in corpus)
3. **SGLang production inference** — ecosystem-layer infrastructure (first explicit in corpus)

## 2. Fish Audio Research License — custom non-OSI

### License identification

- **Full name:** "Fish Audio Research License Agreement"
- **Last updated:** March 7, 2026
- **License type:** Custom (non-OSI-approved)
- **Copyright holder:** **39 AI, INC. All Rights Reserved** (revealed via attribution clause)

### Corpus license distribution post-v20

| License | Count | Wikis |
|---------|-------|-------|
| MIT | 16 | ECC, SP, gstack, GSD, BMAD, gws-peers, graphify, spec-kit, agency-agents, goclaw, paperclip, autoresearch, multica, deer-flow, notebooklm-py, build-your-own-x |
| Apache-2.0 | 1 | gws v13 |
| ISC | 1 | codymaster v12 |
| GPL-3.0 | 1 | TrendRadar v19 |
| CC0 | 1 | build-your-own-x (content) |
| **Custom non-OSI** | **1** | **fish-speech v20 (FIRST)** |

### Commercial boundary clause

> *"Commercial Purpose means any use primarily intended for or directed toward commercial advantage or monetary compensation."*

**Scope includes:**
- Product creation (using fish-speech in a product)
- Internal business operations (company TTS)
- Any service generating revenue "**whether directly or indirectly**"

**Broader than GPL copyleft** — GPL allows commercial use (with copyleft obligation); fish-speech research license **prohibits commercial use** entirely without separate paid license.

### Non-commercial permitted uses

- **Academic/scientific research** ("academic or scientific advancement")
- **Personal/hobbyist** use
- **Evaluation** only (not production deployment)

### Attribution requirements (corpus-first)

Distributors MUST:
1. Provide the Agreement to third parties
2. Include notice: *"This model is licensed under the Fish Audio Research License, Copyright © 39 AI, INC. All Rights Reserved"*
3. **Prominently display "Built with Fish Audio"** on websites, interfaces, or documentation

**Corpus-first:** mandatory attribution-display clause. No other corpus wiki requires brand display beyond LICENSE file.

### Anti-distillation clause (corpus-first)

> *"You may not use the Materials or Derivative Works to create or improve any foundational generative AI model."*

**Implications:**
- Cannot train a competing TTS foundation model using fish-speech outputs
- Cannot use fish-speech-generated synthetic data for model training
- Cannot fine-tune fish-speech then claim the fine-tune as new foundation model

**Corpus-first:** explicit anti-distillation. Signals 39 AI, INC. concerned about competitive distillation (common in 2025-2026 foundation-model space).

### Derivative work clause

- **Users own Derivative Works** they create (fine-tunes, LoRAs)
- **Fish Audio retains ownership of original Materials**
- **Definition covers:** modifications, fine-tuning, **"low-rank adaptation"** models

### Litigation-termination clause (corpus-first)

> *"Litigation by licensees against Fish Audio automatically terminates all granted licenses."*

**Purpose:** anti-patent-troll, anti-litigation-abuse. Common in modern open-source licenses (Apache-2.0 has patent clause) but **explicit termination for ANY suit** is stricter than OSI norms.

### Enforcement mechanism

- Breach → termination
- Indemnification requirement (licensee indemnifies Fish Audio from 3rd-party claims)
- No warranty, as-is

## 3. 39 AI, INC. — open-core commercial entity

### Entity reveal

LICENSE attribution clause reveals:
- **Brand name:** Fish Audio
- **Legal entity:** 39 AI, INC.
- **Separation:** OSS released by 39 AI, INC. under "Fish Audio" brand

### Corpus organizational archetype evolution

| Archetype | Examples | v20 addition |
|-----------|----------|--------------|
| Solo individual | Karpathy (autoresearch), Jesse Vincent (SP), Garry Tan (gstack), sansan0 (TrendRadar), msitarzewski (agency-agents) | — |
| Solo formalized (LLC) | BMAD (BMad Code LLC) | — |
| Solo regional (VN) | codymaster (Tody Le) | — |
| Corporate official | gws (Google), spec-kit (GitHub/Microsoft), deer-flow (ByteDance) | — |
| Community-ambiguous | paperclip, GSD | — |
| Education corporate | course v6 (Microsoft) | — |
| **Open-core commercial entity** | **— (new)** | **fish-speech (39 AI, INC.)** |

### Distinction from prior corporate

- **gws / spec-kit / deer-flow** = pre-existing-corporation-opens-source
- **fish-speech 39 AI, INC.** = **research-lab-turns-commercial-with-OSS-funnel**

fish-speech model: use OSS to build reputation + research credibility → commercial API/enterprise tier as monetization.

### Pattern #31 candidate: Open-Core Commercial Entity

**Formal statement (candidate):**
> "Research-lab-origin organizations may operate open-core models where open-source release under restrictive custom license funnels interest toward commercial paid tier. Distinct from (1) pre-existing-corp-opens-source and (2) community-formalized-LLC."

**Evidence at v20:** 1 (fish-speech / 39 AI, INC.)

**Required for promotion:** 2+ research-lab commercial entities with similar structure.

**Prediction:** Likely to appear more in foundation-model space (Black Forest Labs / Mistral / Anthropic earlier phases show similar pattern).

## 4. SGLang production inference (corpus-first)

### SGLang overview

**SGLang** = LMSYS project for high-throughput LLM inference. Features:
- **Continuous Batching** — dynamic request merging
- **Paged KV Cache** — memory-efficient KV storage
- **CUDA Graph** — reduced kernel launch overhead
- **RadixAttention prefix caching** — shared-prefix request acceleration

### fish-speech SGLang integration

Docs reference `SGLang-Omni README` for server setup. Production features:
- Multi-user concurrent serving
- Low-latency streaming (~100ms TTFA at scale)
- GPU efficiency (30-50% over baseline HuggingFace inference)

### Corpus-first SGLang

Prior corpus frameworks use:
- Direct HuggingFace `model.generate()` (most)
- vLLM (some inference backends)
- llama.cpp (local inference)
- **fish-speech = first SGLang mention**

### Ecosystem signal

SGLang adoption signals **production-inference maturity**. Foundation-model organizations increasingly adopt SGLang/vLLM for serving (vs research-tier HuggingFace direct). fish-speech aligns with this trend.

### Related corpus infrastructure

- **LiteLLM** (TrendRadar v19) — provider abstraction (100+ APIs)
- **MCP** (multiple) — agent-to-tool protocol
- **SGLang** (fish-speech v20) — LLM inference runtime
- **Pattern #30 3-Layer Stratification** now has evidence at each layer

## 5. Commercial positioning

### speech.fish.audio ecosystem

- **Open-source repo** (research license) — model weights, training code, inference
- **Commercial Fish Audio website** — "live playground" (hinted; pricing not public)
- **Enterprise API** — implied via "Server Inference" + "SGLang server" options, pricing opaque

### Open-core funnel

```
GitHub OSS (research license) → HuggingFace model → Community adoption
                                                     ↓
                              Commercial inquiry → 39 AI, INC. paid tier
```

### Revenue-pathway comparison

| Wiki | Revenue model |
|------|---------------|
| Most corpus | None disclosed (grant/personal) |
| BMAD v11 | LLC (consulting implied, not confirmed) |
| gws v13 | Google product (revenue integrated) |
| spec-kit v17 | GitHub product (revenue integrated) |
| **fish-speech v20** | **Open-core (OSS research license → commercial API)** |

**fish-speech = cleanest open-core funnel in corpus.** Others are either pure-OSS or pre-existing-corporate-integrated.

## 6. Legal considerations for Storm Bear VN operator

### Research-only use (OK)

- **Personal experimentation** — building TTS samples for learning
- **Academic research** — analyzing model behavior
- **Evaluation** — testing vs other TTS (ElevenLabs, OpenAI TTS)

### Commercial use (LICENSE blocker)

- ❌ **Scrum coaching service with voice output** — commercial use
- ❌ **Internal business operations** (internal team tools using TTS) — commercial use
- ❌ **Revenue-generating service** (client work, SaaS) — commercial use
- ❌ **Derivative products** sold (apps with fish-speech audio output)
- ✅ **IF commercial:** must acquire separate paid license from Fish Audio

### Attribution obligation (regardless of use)

Even research use requires:
- Agreement inclusion
- "Built with Fish Audio" display if distributing derivatives

### Risk assessment for Storm Bear

| Use case | License OK? |
|----------|-------------|
| Personal voice experimentation | ✅ |
| Vault-internal TTS (no distribution) | ✅ |
| Sharing a fine-tune publicly | ⚠️ (must attribute, no commercial) |
| Voice output for a paid Scrum coaching app | ❌ (requires paid license) |
| Commercial VN dubbing service | ❌ (requires paid license) |

## 7. Pattern refinements at v20

### Pattern #29 GPL-3.0 → License-Category-Diversity

**Pre-v20 formulation (v19 candidate):**
> "Copyleft licensing (GPL-3.0, AGPL) emerges as community-preservation commitment in agent-space."

**v20 refinement (candidate):**
> "License diversity beyond permissive-default (MIT/Apache) expands as frameworks commodify. GPL-3.0 = copyleft community-preservation; custom non-OSI (fish-speech) = commercial-funnel gatekeeper. Both signal productization boundaries distinct from permissive-OSS norm."

### Pattern #33 candidate: Non-OSI Custom License

**Formal statement:**
> "Custom non-OSI-approved licenses emerge in high-value foundation-model space, where research-only clauses create commercial-tier funnel."

**Evidence at v20:** 1 (fish-speech)

**Prediction:** Likely common in foundation-model commercial entities (Stable Diffusion, Llama-3 custom licenses are comparable).

### Pattern #34 candidate: Anti-Distillation License Clause

**Formal statement:**
> "As foundation models commodify, licenses add anti-distillation clauses prohibiting use of model outputs to train competing foundation models."

**Evidence at v20:** 1 (fish-speech)

**Prediction:** Will likely become standard in foundation-model space (Meta Llama-3 license has similar).

## 8. Cross-corpus absence signals

### What fish-speech doesn't have

- ❌ **AGENTS.md** (Pattern #22 industry standard not adopted)
- ❌ **OpenClaw/Hermes** (Pattern #18 regional: CN-origin consistent with TrendRadar)
- ❌ **SECURITY.md** (Pattern #24 T1-standard, but fish-speech isn't T1)
- ❌ **LiteLLM** (Pattern #28, not applicable — this is foundation model, not LLM consumer)
- ❌ **CONTRIBUTING.md prominent** (foundation models != community code)
- ❌ **Karpathy lineage** (Pattern #19 v20 4th archetype has different lineage type)

### Absence interpretation

fish-speech's absences are **consistent with foundation-model-as-product archetype**:
- Foundation models have fewer community-code contributions → minimal governance
- Commercial-license entities avoid OpenClaw/Hermes (community-platform identifier)
- Research-lab origin + academic lineage (not individual-lineage Karpathy-style)

**Hypothesis:** Foundation-model outside-scope wikis systematically differ from agent-framework in-scope wikis along these axes.

## 9. Key observations

### Cluster-level

- **Fish Audio Research License** = first non-OSI in corpus (+4 corpus-first clauses: attribution-display, anti-distillation, litigation-termination, indirect-revenue)
- **39 AI, INC.** = first open-core commercial entity (research-lab-to-commercial funnel)
- **SGLang production** = first explicit LMSYS inference runtime in corpus

### Cross-corpus

- **Pattern #29 refined** to license-category-diversity
- **Pattern #31/33/34 new candidates** registered
- **Pattern #18 strengthened** (CN-origin + foundation-model both skip OpenClaw/Hermes)

## 10. References

- Parent: [[(C) index]]
- Source: github.com/fishaudio/fish-speech LICENSE + README attribution + speech.fish.audio
- Sibling clusters: [[(C) README + 7-language i18n + philosophy cluster summary]] + [[(C) Dual-AR architecture + GRPO + research-lineage cluster summary]]

---

**Cluster summary: Fish Audio Research License (custom non-OSI, first in corpus) + 39 AI, INC. open-core commercial entity + SGLang production inference. 4 corpus-first license clauses (attribution-display, anti-distillation, litigation-termination, indirect-revenue). Pattern #29 refined, Patterns #31/#33/#34 registered. Commercial-license blocker for Storm Bear operator VN Scrum coaching use.**
