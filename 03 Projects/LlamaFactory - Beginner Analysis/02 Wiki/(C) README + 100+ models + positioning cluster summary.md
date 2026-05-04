# (C) README + 100+ models + positioning cluster summary

> **Cluster:** README positioning + 100+ model support + unified training-stage framing
> **Parent:** [[(C) index]]
> **Sources:** github.com/hiyouga/LLaMA-Factory README (EN + zh-CN) + llamafactory.readthedocs.io
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Positioning as "unified efficient fine-tuning"** — consolidates previously-fragmented tooling
2. **100+ LLM/VLM model support** — broadest model coverage in corpus
3. **Unified training-stage framing** — pre-train through RLHF in single framework

## 2. Positioning — "Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)"

### Core positioning statement

From README tagline:
> *"Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)"*

### Positioning dimensions

**Unified:** single framework replacing 5+ fragmented tools:
- **PEFT** (HuggingFace) — LoRA / QLoRA / other adapters
- **TRL** (HuggingFace) — reward modeling + PPO / DPO
- **QLoRA** (Tim Dettmers et al.) — quantized training
- **FastChat** — SFT pipeline

LlamaFactory consolidates these into coherent fine-tuning workflow.

**Efficient:** performance-optimization focus:
- FlashAttention-2
- Unsloth integration
- Liger Kernel
- Contamination-free packing
- FSDP+QLoRA for memory-constrained settings

**100+ LLMs & VLMs:** breadth-of-support emphasis (vs narrow training pipelines):
- LLMs: LLaMA, Qwen, Mistral, Mixtral-MoE, DeepSeek, Gemma, GLM, Phi, InternLM, MiniCPM, Falcon, 90+ others
- VLMs: vision-language models (multi-modal)

**ACL 2024:** peer-reviewed academic venue (not arXiv-only preprint).

## 3. 100+ model support (broadest in corpus)

### Primary supported families

**English-centric:**
- **LLaMA family** (Meta)
- **Mistral + Mixtral-MoE** (Mistral AI)
- **Gemma** (Google)
- **Phi** (Microsoft)
- **Falcon** (TII)

**CN-centric:**
- **Qwen** (Alibaba)
- **DeepSeek** (DeepSeek AI)
- **GLM** (ZhipuAI)
- **InternLM** (InternLM)
- **MiniCPM** (ModelBest)

**+90 other families** — continuous addition via community contributions.

### Cross-corpus comparison

| Wiki | Model support breadth |
|------|----------------------|
| ECC v1 | 1 (Claude Code) |
| fish-speech v20 | 1 (its own model family, 80+ languages output) |
| TrendRadar v19 | 100+ via LiteLLM (for inference, not training) |
| **LlamaFactory v22** | **100+ models for fine-tuning (first training-side breadth)** |

**LlamaFactory = first corpus wiki with 100+ model support for TRAINING** (vs inference or wrapping).

### CN ecosystem coverage

LlamaFactory natively supports 5+ CN-origin model families (Qwen, DeepSeek, GLM, InternLM, MiniCPM). **Validates Pattern #18 regional hypothesis**: CN-ecosystem models have full integration alongside Western models — training-infrastructure is regional-neutral.

## 4. Unified training stages (9 stages)

### Training stage progression

```
1. Pre-training
     ↓
2. Supervised Fine-Tuning (SFT)
     ↓
3. Reward Modeling
     ↓
4-9. RL alignment stages:
     - PPO (Proximal Policy Optimization)
     - DPO (Direct Preference Optimization)
     - KTO (Kahneman-Tversky Optimization)
     - ORPO (Odds Ratio Preference Optimization)
     - SimPO (Simple Preference Optimization)
```

### 5 RL alignment methods

LlamaFactory integrates 5 distinct RL alignment methods. Most fine-tuning frameworks offer 1-2. Rapid research integration is LlamaFactory's competitive edge.

**Pattern #43 candidate (Optimizer-Research Integration Velocity):** LlamaFactory integrates cutting-edge RL alignment research quickly. PPO → DPO → KTO → ORPO → SimPO represents ~18 months of research chronology; LlamaFactory ships all 5.

### Cross-framework comparison

| Framework | RL methods |
|-----------|-----------|
| TRL alone | PPO + DPO + KTO |
| Axolotl | PPO + DPO |
| **LlamaFactory** | **PPO + DPO + KTO + ORPO + SimPO (5)** |
| Unsloth | Limited (LoRA-focused) |

**LlamaFactory = most RL methods integrated** of comparable frameworks.

## 5. Fine-tuning methods (6 methods)

### Method catalog

| Method | Parameter efficiency | Memory |
|--------|---------------------|--------|
| **Full-tuning** | 100% params trained | Highest |
| **Freeze-tuning** | Subset of layers | Medium |
| **LoRA** | Low-rank adapters | Low |
| **QLoRA** | Quantized LoRA | Lowest |
| **OFT** | Orthogonal fine-tuning | Low |
| **QOFT** | Quantized OFT | Lowest |

### QLoRA + FSDP — 70B on 2×24GB GPUs

Aggressive memory optimization claim:
- LLaMA-70B fine-tuning on 2×RTX 3090/4090 (24GB each)
- Uses: QLoRA (4-bit quantization) + FSDP (Fully Sharded Data Parallel)
- Democratizes 70B fine-tuning to consumer-grade hardware

### Cross-framework memory comparison

| Method | 70B hardware requirement |
|--------|--------------------------|
| Full-tuning | 8×A100 80GB minimum |
| Standard LoRA | 4×A100 80GB |
| QLoRA | 1×A100 80GB OR 2×A100 40GB |
| **LlamaFactory QLoRA+FSDP** | **2×24GB consumer GPUs** |

Enables community + individual researchers to fine-tune 70B models.

## 6. VLM (Vision-Language Model) support

### Multi-modal fine-tuning

Beyond text LLMs, supports:
- LLaVA family
- Qwen-VL family  
- MiniCPM-V
- Phi-3.5-vision
- InternVL
- Gemma-Vision

**Broader than most fine-tuning frameworks** which are text-only.

## 7. Cross-Storm Bear overlap

### Corpus relationships

| Corpus wiki | Overlap with LlamaFactory |
|-------------|---------------------------|
| autoresearch v10 (Karpathy ML research) | Adjacent — both training-infra, different scope (autoresearch=autonomous research loop) |
| fish-speech v20 | Peer — both foundation-model-space, research-paper-chain lineage |
| deer-flow v9 (ByteDance) | Adjacent — CN-ecosystem, but deer-flow is application not training |
| TrendRadar v19 (LiteLLM) | Adjacent — both multi-provider, but TrendRadar inference-side |

### Pattern #19 4th archetype peer

LlamaFactory + fish-speech = **2 data points for research-paper-chain lineage archetype** (Pattern #19 4th). Both cite extensive prior-research networks:
- fish-speech: 7 citations (VITS2, Bert-VITS2, GPT VITS, MQTTS, GPT Fast, GPT-SoVITS, Qwen3)
- LlamaFactory: PEFT + TRL + QLoRA + FastChat + 100+ research

**Archetype now structurally validated at N=2.**

## 8. Community + documentation

### Community channels

- **Discord** — global community
- **WeChat user groups** — CN community (primary)
- **Blog platform** — research + tutorials
- **GitHub Issues** — 978 open (active development)

### Documentation

- **Official docs:** llamafactory.readthedocs.io
- **README bilingual** — EN + zh-CN
- **ACL 2024 paper** — formal methodology documentation

### No commercial tier

**Free cloud options:**
- Google Colab integration
- Alibaba PAI-DSW
- LLaMA Factory Online (free tier)

**No paid offerings.** Distinct from fish-speech v20 open-core model.

## 9. Comparison with v20 fish-speech (research-first peer)

Both are research-first, peer-reviewed-adjacent:

| Dimension | fish-speech v20 | LlamaFactory v22 |
|-----------|-----------------|-------------------|
| Publication | 2 arXiv preprints | **ACL 2024 peer-reviewed** |
| License | Custom non-OSI (commercial tier) | **Apache-2.0 permissive** |
| Author | 39 AI INC (corporate entity) | hiyouga + Lab4AI (academic) |
| Model count | 1 (their own) | 100+ (fine-tuning target) |
| Research lineage | 7 citations | PEFT+TRL+QLoRA+FastChat + 100+ |
| Genre | Foundation-model-as-product | Training-infrastructure |
| Commercial | Explicit paid tier | No paid offering |

**Both validate Pattern #19 4th archetype** — different commercial structures.

## 10. Key observations

### Cluster-level

- **Unified framework** consolidates PEFT + TRL + QLoRA + FastChat (research-paper-chain lineage)
- **100+ model support** — broadest training-target in corpus
- **9 training stages** — most comprehensive pipeline
- **ACL 2024 peer-reviewed** — first peer-reviewed venue in corpus
- **Efficiency focus** — FSDP+QLoRA 70B on 2×24GB consumer GPUs

### Cross-corpus

- **Pattern #19 4th archetype at N=2** (research-paper-chain validates)
- **Pattern #32 promotion-ready** (2 data points consistent)
- **Pattern #8 6th data point** (most rigorous: ACL peer-reviewed)
- **Pattern #18 regional-neutral** (CN + Western models equally supported)

## 11. References

- Parent: [[(C) index]]
- Source: github.com/hiyouga/LLaMA-Factory README + docs.llamafactory.readthedocs.io
- arXiv: 2403.13372 (ACL 2024)
- Sibling clusters: [[(C) Training methods + optimizers + research-lineage cluster summary]] + [[(C) Deployment + community + ACL 2024 cluster summary]]

---

**Cluster summary: "Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)" positioning. 100+ models (English + CN families) + 9 training stages (pre-train through 5 RL methods) + 6 fine-tuning methods (Full/Freeze/LoRA/QLoRA/OFT/QOFT). Research-paper-chain lineage consolidates PEFT + TRL + QLoRA + FastChat. ACL 2024 peer-reviewed publication. First peer-reviewed venue in Storm Bear corpus. Pattern #19 4th archetype validates at N=2 via fish-speech v20 + LlamaFactory v22 peer evidence.**
