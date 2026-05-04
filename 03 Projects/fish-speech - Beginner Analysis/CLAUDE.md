# fish-speech - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`fishaudio/fish-speech`](https://github.com/fishaudio/fish-speech) — **"SOTA Open Source TTS"** (State-of-the-art multilingual text-to-speech system).

**29.8K stars (6th largest in corpus), 2.5K forks (8.4% ratio), FISH AUDIO RESEARCH LICENSE (first non-OSI custom license in corpus), Python 80.8% + TypeScript 14.3% + Dockerfile 3%, v1.5.1 (May 31, 2025), main-branch, 27 open issues, 152 watchers**. Default branch `main`. **Author: Fish Audio (brand) / 39 AI, INC. (legal entity)** — **first open-core commercial entity in corpus**.

**Scope status: OUTSIDE STORM BEAR CORE SCOPE** — foundation model (TTS), not agent framework. Closest precedent: build-your-own-x v8 (outside-scope meta-reference). Analyzed for pattern observation value (custom license + research-lineage archetype + foundation-model-as-product).

**Positioning:** *"SOTA Open Source TTS"* / *"the best text-to-speech system among both open source and closed source"* / *"Leveraging Large Language Models for Advanced Multilingual Text-to-Speech"*.

**Core product:** TTS foundation model
- **80+ languages** (Tier 1: Chinese/English/Japanese; Tier 2: Korean/Spanish/Portuguese/Arabic/Russian/French/German; 70+ more)
- **Dual-Autoregressive architecture** — Slow AR (4B params) + Fast AR (400M) + RVQ audio codec (10 codebooks, ~21 Hz)
- **GRPO alignment** (Group Relative Policy Optimization RL alignment for TTS)
- **10M hours training audio** — foundation-model-scale corpus
- **15,000+ emotion/instruction tags** via `[whisper]` `[excited]` `[laugh]` inline natural language control
- **Voice cloning from 10-30s samples** — no fine-tuning required
- **Multi-speaker from single reference audio**
- **SGLang production inference** — streaming, Continuous Batching, Paged KV Cache, RadixAttention prefix caching
- **Benchmarks:** 0.54% WER CN / 0.99% WER EN (Seed-TTS Eval); 81.88% win rate EmergentTTS-Eval; RTF 0.195 on H200
- **arXiv publications:** 2603.08823 (2026 S2 tech report) + 2411.01156 (2024 v1.4)

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE** (foundation model; not agent framework). 2nd outside-scope after build-your-own-x v8. |
| **Archetype** | **Research-lab + open-core commercial** — 39 AI, INC. operates commercial Fish Audio brand; OSS release under custom research license |
| **Scale tier** | Large (29.8K stars) |
| **Primary lang** | Python 80.8% + TypeScript 14.3% + Dockerfile 3% |
| **Packaging** | pip + Docker (fishaudio/fish-speech) + HuggingFace (fishaudio/s2-pro) + SGLang server |
| **Origin story** | **Research-lab (arXiv-documented)** — v1.4 paper 2024; S2 paper 2026; iterative research program |
| **Methodology** | NONE (foundation model product, not methodology) |
| **Governance files** | README (7-lang) + LICENSE (custom) + mkdocs docs + pyproject.toml |
| **Agent/skill count** | N/A (foundation model, not agent framework) |
| **i18n** | **7-language README** — EN + 简体中文 + Português + 日本語 + 한국어 + العربية + Español (largest in corpus; beats graphify CJK-quad and TrendRadar bilingual) |
| **Intellectual influence** | **Research-paper-chain:** VITS2 + Bert-VITS2 + GPT VITS + MQTTS + GPT Fast + GPT-SoVITS + Qwen3. **4th Pattern #19 archetype** (beyond individual / methodology / community-viral) |
| **Agent platforms** | SGLang server (inference-infra, agent-adjacent); HuggingFace model hub |

**Tier placement rationale:** OUTSIDE-SCOPE because:
- fish-speech is a TTS foundation model; it does not orchestrate agents, provide agent skills, or wrap LLM inference for agents
- Could be a *capability* an agent invokes (voice output) but that role is downstream, not the artifact itself
- 2nd outside-scope entry — build-your-own-x v8 was education aggregator; fish-speech is foundation model. Different outside-scope sub-categories.

**License alert (first non-OSI in corpus):**
- Custom "Fish Audio Research License" by 39 AI, INC.
- **Non-Commercial only** — academic/personal/evaluation use free; commercial = separate paid license
- **Anti-distillation clause** — cannot use Materials to "create or improve any foundational generative AI model" (first in corpus)
- **Attribution display** — "Built with Fish Audio" prominently displayed on websites/UIs (first in corpus)
- **Litigation termination** — filing suit against Fish Audio auto-terminates all licenses (first in corpus)
- **Derivative work ownership** — user owns derivatives, but cannot use for foundation-model training
- **Impact for Storm Bear VN operator:** ⚠️ Commercial Scrum coaching use requires paid license. Research-only OK.

**Critical Pattern tests at v20:**

- **Pattern #9 Resolution D:** N/A for outside-scope. 2nd outside-scope data point adds corpus diversity evidence.
- **Pattern #18 (OpenClaw/Hermes):** NOT MENTIONED. fish-speech is CN-origin org-backed. **Strengthens Pattern #18 regional refinement** (Western-community-platform-specific; CN-ecosystem + foundation-model both skip). Possibly foundation-model archetype also distinct from community-framework archetype on this axis.
- **Pattern #19 Intellectual Lineage — MAJOR 4TH ARCHETYPE:** research-paper-chain (cites 7 prior research). Distinct from:
  - (1) individual-author (Karpathy, John Lam)
  - (2) methodology (SDD/BMAD)
  - (3) community-viral (agency-agents / TrendRadar)
  - (4) **research-paper-chain (NEW: fish-speech)** — multiple academic-project citations forming explicit research lineage
- **Pattern #20 Solo-Scale Ceiling:** N/A (organizational, not solo)
- **Pattern #28 LiteLLM:** N/A (TTS, not LLM inference)
- **Pattern #29 GPL-3.0 → License-Category-Diversity refinement:** corpus now spans MIT / Apache / ISC / GPL / **custom-non-OSI**. Pattern #29 may generalize to "copyleft + custom-restrictive licensing emerges in agent-adjacent space as ethical/commercial boundary."
- **Pattern #30 3-Layer Stratification:** N/A (not agent framework)
- **Pattern #8 Empirical Research Emergence:** 5TH DATA POINT — fish-speech has formal arXiv + WER benchmarks + EmergentTTS-Eval. Prior: codymaster SkillsBench / autoresearch val_bpb / graphify 71.5× token / spec-kit 48× productivity / **fish-speech 0.54% WER + 81.88% win rate**.

**NEW Pattern candidates at v20:**

- **#31 candidate: Open-Core Commercial Entity** — 39 AI, INC. operates commercial Fish Audio brand separate from OSS release. Distinct from BMAD LLC (community formalization) and GitHub/Microsoft (pre-existing corporate). First explicit "commercial-entity-owns-OSS-brand" in corpus.
- **#32 candidate: Research-Paper-Chain Intellectual Lineage** — Pattern #19 4th archetype. fish-speech cites 7 prior research. Likely common in foundation-model space.
- **#33 candidate: Non-OSI Custom License** — first in corpus. Signals productization boundary (research-free, commercial-paid).
- **#34 candidate: Anti-Distillation License Clause** — explicit prohibition on using materials to train foundation models. First in corpus. May become standard as foundation models commodify.
- **#35 candidate: Foundation-Model-as-Product scope category** — distinct from agent-framework / agent-service / agent-education / agent-bridge / agent-application. May warrant 6th scope category or separate "model-as-artifact" axis.

**Novel elements at v20:**
1. **First non-OSI license** — Fish Audio Research License (custom)
2. **First anti-distillation clause** — prohibits foundation-model training from materials
3. **First attribution-display clause** — "Built with Fish Audio" on UIs
4. **First litigation-termination clause** — anti-patent-troll provision
5. **First research-paper-chain lineage archetype** — 7 prior research cited
6. **First 7-language README** — broadest i18n in corpus
7. **First foundation-model-as-product** outside-scope entry
8. **First open-core commercial entity** — 39 AI, INC. brand separation
9. **First SGLang explicit production** — Continuous Batching + Paged KV Cache + RadixAttention
10. **First TTS benchmark family** — Seed-TTS Eval WER + EmergentTTS-Eval
11. **First 10M-hours training corpus scale** explicit
12. **First natural-language emotion tags** in corpus (15,000+ tags)
13. **First GRPO RL alignment** for generation model
14. **First 80+ language support** in corpus
15. **First 2-arXiv-publication pattern** (v1.4 2024 + S2 2026)

**Phase 4b routing = OUTSIDE-SCOPE META-REFERENCE + research-lineage archetype formalization.** Parallels v8 build-your-own-x outside-scope approach; extends with Pattern #19 4th archetype documentation + 5 new pattern candidates.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**20th auto-execution, 2nd v2 routine execution, 2nd outside-scope wiki**):

- **Ingest sources via WebFetch** — README (7-lang, fetch EN primary) + LICENSE + docs site (speech.fish.audio)
- **Cross-reference với 19 sibling wikis** — primarily v8 build-your-own-x (outside-scope precedent); secondary v19 TrendRadar (CN-ecosystem origin), v17 spec-kit (corporate archetype comparison), v16 graphify (CJK i18n precedent)
- **Phase 4b = outside-scope meta-reference + Pattern #19 4th archetype** — document research-paper-chain as distinct lineage type
- **Beginner roadmap** — angle: developers wanting voice-output capability for agents; Scrum coach use case: meeting transcription/synthesis, accessibility. ⚠️ License blocker for commercial use.

**Prime directive:** Outcome = wiki + outside-scope meta-reference + document Pattern #19 4th archetype (research-paper-chain) + register 5 new pattern candidates (#31-35) + refine Pattern #29 to license-category-diversity.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 2nd v2 routine execution. Phase 4b = **outside-scope meta-reference with research-lineage archetype formalization**.

## Key People / Organization

- **Fish Audio** — brand name for TTS research/product
- **39 AI, INC.** — legal entity behind Fish Audio (LICENSE attribution reveals)
- **SGLang team** — inference infrastructure ecosystem partner
- **HuggingFace** — model hosting (fishaudio/s2-pro)
- **Research lineage cited (7):** VITS2, Bert-VITS2, GPT VITS, MQTTS, GPT Fast, GPT-SoVITS, Qwen3
- **Cross-project:** 19 sibling wikis. This is 20th = first research-lineage 4th archetype + first non-OSI license.

## Folder Structure

```
fish-speech - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-04 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 19 siblings MANDATORY** — especially v8 outside-scope precedent
- **Pattern Library direct update** (v2 routine Phase 5)
- **Document Pattern #19 4th archetype** (research-paper-chain)
- **Document Pattern #29 license-diversity refinement** (non-OSI emerging)
- **Flag license commercial restriction** prominently in beginner guide

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 20th LLM Wiki, 2nd outside-scope, 2nd v2 execution

### Expected milestones

- [x] Phase 0 Pre-flight with v2 12-axis classification
- [ ] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 — README+philosophy / Architecture+benchmarks+research-lineage / LICENSE+commercial-boundary+SGLang)
- [ ] Phase 3 Entity pages (4 — Dual-AR architecture+GRPO / Multilingual 80+ language TTS / 39 AI INC open-core + Research-paper-chain lineage / Storm Bear outside-scope meta + Pattern #19 4th archetype)
- [ ] Phase 4a Beginner published guide bilingual (with license commercial-restriction prominent warning)
- [ ] Phase 4b **Outside-scope meta-reference + Pattern #19 4th archetype deliverable**
- [ ] Phase 5 Iteration log v20 + PATTERN_LIBRARY.md update (5 new candidates + Pattern #19 archetype + Pattern #29 refinement)
- [ ] Phase 6 Vault file updates
