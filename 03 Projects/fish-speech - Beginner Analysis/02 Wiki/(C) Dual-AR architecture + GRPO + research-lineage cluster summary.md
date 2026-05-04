# (C) Dual-AR architecture + GRPO + research-lineage cluster summary

> **Cluster:** Technical architecture (Dual-AR + RVQ + GRPO) + 7-research-citation lineage + arXiv publications
> **Parent:** [[(C) index]]
> **Sources:** README architecture section + arXiv 2603.08823 (2026 S2) + arXiv 2411.01156 (2024 v1.4)
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Dual-Autoregressive architecture** — Slow AR 4B + Fast AR 400M + RVQ codec
2. **GRPO alignment** — Group Relative Policy Optimization (RL for TTS)
3. **Research-paper-chain lineage** — 7 prior research projects cited as influences

## 2. Architecture — Dual-Autoregressive (Dual-AR)

### Two-stage AR design

```
Text input
    ↓
[Slow AR — 4B params]
    ↓ (semantic acoustic tokens)
[Fast AR — 400M params]
    ↓ (fine-grained acoustic tokens)
[RVQ decoder — 10 codebooks, ~21 Hz]
    ↓
Audio output (24kHz)
```

### Role division

- **Slow AR (4B):** semantic prosody/emotion planning from text — high-capacity reasoning
- **Fast AR (400M):** frame-level acoustic detail — low-latency generation
- **RVQ codec:** residual vector quantization decoder, 10 codebooks, ~21 Hz frame rate → 24kHz audio

### Rationale

Traditional TTS bottleneck: single AR model must handle both semantic planning + acoustic detail. Dual-AR **separates concerns** — big model for planning, small model for fast generation. Similar to speculative decoding in LLMs (big draft, small verifier) — but inverted (big planner, small generator).

## 3. RVQ codec (corpus-first)

### Residual Vector Quantization

- **10 codebooks** — cascade of quantizers
- **~21 Hz** frame rate (vs common 50-100 Hz TTS codecs)
- **Lower framerate** = more information per token, longer context window in AR model

### Impact

At 21 Hz, 1 minute of audio = 1,260 tokens. LLM context window 32K → ~25 minutes continuous audio generation. Enables:
- Long-form narration (audiobooks)
- Multi-turn conversation with full context
- Streaming (low token rate → low latency)

## 4. GRPO alignment (corpus-first for generation)

### Group Relative Policy Optimization

GRPO = RL alignment technique from DeepSeek-R1 / Qwen-R1 line. Adapted for TTS by fish-speech.

### Alignment objective (inferred)

- Human preference: natural prosody + emotion matching tags
- Reward: win-rate on listener comparisons (EmergentTTS-Eval-like)
- Optimization: relative ranking of generated samples per prompt

### Result

- **EmergentTTS-Eval 81.88% win rate** vs baselines
- **0.54% WER CN / 0.99% WER EN** on Seed-TTS Eval

### Significance

**First explicit RL alignment for TTS generation in Storm Bear corpus.** RL-alignment was historically LLM-only (RLHF → DPO → GRPO). fish-speech demonstrates **alignment techniques transferring cross-modality** (LLM → TTS).

## 5. Research-paper-chain lineage (7 citations)

### Credits from README

> *"This work draws on the shoulders of many prior research projects: VITS2, Bert-VITS2, GPT VITS, MQTTS, GPT Fast, GPT-SoVITS, Qwen3."*

### Decomposition

| # | Project | Contribution |
|---|---------|--------------|
| 1 | **VITS2** | Variational Inference TTS with Adversarial Learning — baseline quality |
| 2 | **Bert-VITS2** | BERT-conditioned VITS variant — text representation |
| 3 | **GPT VITS** | GPT-style autoregressive TTS — AR approach |
| 4 | **MQTTS** | Multi-quantizer TTS — RVQ precursor |
| 5 | **GPT Fast** | Fast AR inference optimization — latency |
| 6 | **GPT-SoVITS** | Voice cloning from limited samples — few-shot cloning |
| 7 | **Qwen3** | LLM backbone (Alibaba) — 4B Slow AR architecture likely derived |

### Pattern #19 4th archetype

**Corpus Pattern #19 "Intellectual Lineage Archetypes" state pre-v20:**
- (1) Individual-author lineage — Karpathy (3 wikis) + John Lam (spec-kit v17)
- (2) Methodology-lineage — SDD (GSD v5 + spec-kit v17) + BMAD
- (3) Community-viral no-lineage — agency-agents v18 + TrendRadar v19 (N=2)

**v20 fish-speech introduces 4th archetype:**
- (4) **Research-paper-chain lineage** — cites 7 prior academic/research projects, builds on published foundations

**Distinction from (1):** individual-author lineage = 1 person as node; research-paper-chain = 7 projects as node network.

**Distinction from (2):** methodology = shared ideological framework (SDD, BMAD); research-chain = shared technical foundations (architectures, datasets, techniques).

**Distinction from (3):** no-lineage = deliberate community-origin without cited predecessors; research-chain = explicit predecessor-citation (opposite).

**Prediction:** Foundation-model-space frameworks likely cluster in research-paper-chain archetype (Stable Diffusion chain, LLaMA chain, Qwen chain all cite predecessors).

## 6. arXiv publications

### 2 formal academic artifacts

| Paper | arXiv ID | Year | Content |
|-------|----------|------|---------|
| **Fish-Speech v1.4** | 2411.01156 | 2024 | Original architecture + benchmarks |
| **Fish-Speech S2 Pro** | 2603.08823 | 2026 | Dual-AR + GRPO + RVQ + 10M hours training |

### Pattern #8 Empirical Research — 5th data point

**Prior corpus research-benchmark evidence:**
1. codymaster v12 — SkillsBench +18.6pp
2. autoresearch v10 — val_bpb metric
3. graphify v16 — 71.5× token reduction
4. spec-kit v17 — 48× productivity claim
5. **fish-speech v20 — Seed-TTS WER + EmergentTTS-Eval 81.88% win rate + 2 arXiv papers**

fish-speech is **most formally-published** of corpus — prior 4 benchmarks were documentation-embedded; fish-speech has peer-review-adjacent arXiv preprints.

## 7. Technical innovations

### Corpus-first technical elements

1. **Dual-AR architecture** — two-model cascade for TTS (Slow planner + Fast generator)
2. **RVQ 10-codebook codec at 21 Hz** — lowest framerate, highest info-density
3. **GRPO RL alignment for TTS** — first non-LLM alignment in corpus
4. **15,000+ emotion/instruction tags** — inline natural language control
5. **10M hours training** — foundation-model-scale corpus
6. **2 arXiv publications** — most formal research artifact in corpus

### Comparison with corpus novel architectures

| Wiki | Novel architecture |
|------|-------------------|
| gws v13 | Dynamic Discovery Service (runtime CLI gen) |
| graphify v16 | Graph-topology clustering without embeddings |
| multica v15 | Hybrid local-daemon + cloud-orchestration |
| TrendRadar v19 | LiteLLM 100+ provider abstraction |
| **fish-speech v20** | **Dual-AR + GRPO + RVQ — research-grade novelty** |

## 8. Performance profile (H200 GPU)

- **Real-Time Factor:** 0.195 (5.13× faster than real-time)
- **Time-to-first-audio:** ~100ms (streaming-capable for conversational UX)
- **Throughput:** 3,000+ acoustic tokens/s
- **Context:** ~21 Hz → long-form generation feasible

## 9. Model distribution

### HuggingFace

- **fishaudio/s2-pro** — flagship S2 Pro model card
- Historical: fishaudio/fish-speech-1.2, fishaudio/fish-speech-1.4

### Docker

- **fishaudio/fish-speech** — Docker Hub (pre-built inference container)

### Local

- **pip install** — Python SDK + CLI
- **inference.ipynb** — Jupyter demo notebook
- **WebUI** — Gradio-based interface

## 10. SGLang integration

### Inference production via SGLang

SGLang = LMSYS LLM inference runtime optimized for:
- **Continuous Batching** — dynamic request batching
- **Paged KV Cache** — memory efficiency
- **CUDA Graph** — kernel launch overhead elimination
- **RadixAttention prefix caching** — repeated prompt acceleration

### fish-speech SGLang server

Docs reference `SGLang-Omni README` for server setup. SGLang enables:
- Multi-user concurrent inference
- Low-latency streaming (100ms TTFA achievable at scale)
- Reduced $/hour for cloud deployment

### Cross-corpus note

**First SGLang explicit mention** in Storm Bear corpus. Other frameworks use vLLM, llama.cpp, or direct model.generate(). SGLang adoption signals production-inference maturity.

## 11. Key observations

### Cluster-level

- **Dual-AR + GRPO + RVQ** = research-grade novel architecture (3 corpus-firsts)
- **7-research citation lineage** = Pattern #19 4th archetype
- **2 arXiv publications** = most formal research artifact in corpus
- **SGLang production** = first explicit LMSYS inference framework

### Cross-corpus

- **5th Pattern #8 benchmark data point** — most rigorous (arXiv + WER + win-rate vs prior documentation-embedded)
- **Pattern #19 4th archetype** (research-paper-chain)

## 12. References

- Parent: [[(C) index]]
- Source: README.md architecture section + arXiv 2603.08823 + arXiv 2411.01156
- Sibling clusters: [[(C) README + 7-language i18n + philosophy cluster summary]] + [[(C) Custom LICENSE + 39 AI INC + SGLang production cluster summary]]

---

**Cluster summary: Dual-AR architecture (Slow 4B + Fast 400M) + RVQ 10-codebook codec at 21Hz + GRPO RL alignment + research-paper-chain lineage (7 citations) + 2 arXiv papers. Pattern #19 4th archetype (research-paper-chain) formalized. Pattern #8 5th research-benchmark data point (most rigorous). 3 corpus-first architectural elements.**
