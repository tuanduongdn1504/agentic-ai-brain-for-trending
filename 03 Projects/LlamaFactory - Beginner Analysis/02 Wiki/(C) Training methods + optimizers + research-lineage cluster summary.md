# (C) Training methods + optimizers + research-lineage cluster summary

> **Cluster:** Fine-tuning methods depth + optimizer research integration + PEFT/TRL/QLoRA/FastChat lineage
> **Parent:** [[(C) index]]
> **Sources:** README training methods section + arXiv 2403.13372 + research lineage citations
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **6 fine-tuning methods + 9 training stages** — comprehensive training workflow
2. **5 cutting-edge optimizers integrated** — GaLore + BAdam + APOLLO + Adam-mini + Muon
3. **Research-paper-chain lineage** — PEFT + TRL + QLoRA + FastChat + 100+ research projects (Pattern #19 4th archetype N=2)

## 2. Fine-tuning methods detail

### 6-method matrix

| Method | Trainable % | Memory | Quality | Speed |
|--------|-------------|--------|---------|-------|
| **Full-tuning** | 100% | Highest | Highest (ceiling) | Slowest |
| **Freeze-tuning** | ~20-50% (select layers) | High | High | Medium |
| **LoRA** (Low-Rank Adaptation) | <1% | Low | Medium-High | Fast |
| **QLoRA** (Quantized LoRA) | <1% | Lowest | Medium-High | Fast |
| **OFT** (Orthogonal Fine-Tuning) | <1% | Low | Medium-High | Fast |
| **QOFT** (Quantized OFT) | <1% | Lowest | Medium-High | Fast |

### LoRA family dominance

LoRA + QLoRA remain dominant in community usage:
- Training 1% of params achieves 90%+ of full-tuning quality
- Enables consumer-GPU training
- Swappable adapters (can maintain 10+ task-specific adapters)

### OFT / QOFT (newer)

Orthogonal Fine-Tuning — preserves pretrained representations via orthogonal constraint:
- Better for avoiding catastrophic forgetting
- QOFT adds quantization for memory efficiency
- Ship in LlamaFactory ahead of other frameworks

## 3. Training stages — 9 stages unified

### Full training pipeline

```
Stage 1: Pre-training (from-scratch)
         ↓
Stage 2: Supervised Fine-Tuning (SFT)
         - Task-specific demonstrations
         ↓
Stage 3: Reward Modeling
         - Train reward model on human preferences
         ↓
Stage 4: RL alignment (5 methods available)
         - PPO (2017)
         - DPO (2023)
         - KTO (2024)
         - ORPO (2024)
         - SimPO (2024)
```

### 5 RL alignment methods

**Pattern #43 candidate — Optimizer-Research Integration Velocity:**

LlamaFactory integrates 5 RL methods spanning ~7 years of research:

| Method | Year | Innovation |
|--------|------|-----------|
| **PPO** (Proximal Policy Optimization) | 2017 | Schulman et al. — stable policy gradient |
| **DPO** (Direct Preference Optimization) | 2023 | Rafailov et al. — no reward model needed |
| **KTO** (Kahneman-Tversky Optimization) | 2024 | Ethayarajh et al. — prospect-theory framing |
| **ORPO** (Odds Ratio Preference Optimization) | 2024 | Hong et al. — SFT + preference in one step |
| **SimPO** (Simple Preference Optimization) | 2024 | Meng et al. — reference-free variant |

**LlamaFactory ships all 5 simultaneously.** Research-to-production velocity is rapid.

### Most comprehensive RL catalog in corpus

No other Storm Bear corpus wiki integrates this many RL methods. Closest peer: fish-speech v20 (GRPO for TTS — 1 method).

## 4. Optimizer research integration — 5 novel optimizers

### Cutting-edge optimizers integrated

| Optimizer | Year | Memory innovation |
|-----------|------|-------------------|
| **GaLore** (Gradient Low-Rank Projection) | 2024 | 8B full-training on 24GB GPU |
| **BAdam** | 2024 | Block-coordinate optimization |
| **APOLLO** | 2024 | Adafactor + memory reduction |
| **Adam-mini** | 2024 | Adam with reduced memory |
| **Muon** | 2024 | Spectral-normalization optimizer |

### Why novel optimizers matter

Beyond LoRA/QLoRA parameter-efficiency, these optimizers reduce memory-usage of the **training process itself** (gradients, optimizer states). Unlocks full-tuning at lower hardware.

### Research-velocity-as-feature

Pattern: LlamaFactory ships research optimizers within months of publication. Distinct from corporate fine-tuning tools that stabilize on older methods.

**Pattern #43 candidate formalization:** Framework integrates cutting-edge research (optimizers, RL methods, fine-tuning techniques) rapidly. Research-velocity is competitive edge.

## 5. Distributed training backends

### Backend options

| Backend | Use case |
|---------|----------|
| **DDP** (Distributed Data Parallel) | Multi-GPU same model |
| **FSDP** (Fully Sharded Data Parallel) | Large models sharded across GPUs |
| **DeepSpeed** (Microsoft) | ZeRO optimizer stages 1/2/3 |
| **Megatron-core** (NVIDIA) | Tensor + pipeline parallelism |

### FSDP + QLoRA — 70B on 2×24GB

Novel combination:
- QLoRA quantizes weights to 4-bit
- FSDP shards across GPUs
- Result: 70B-param model fine-tunable on 2×24GB consumer GPUs

### Megatron-core — corpus-first

First Storm Bear wiki mentioning Megatron-core. Signals LlamaFactory serves both:
- Community: QLoRA + FSDP
- Enterprise: Megatron-core + tensor parallelism

## 6. Research-paper-chain lineage (Pattern #19 4th archetype validation)

### Citation network

```
┌─────────────────────────────────────────┐
│ Foundation research cited:               │
│ - PEFT (HuggingFace; LoRA, prefix tuning)│
│ - TRL (HuggingFace; RLHF pipeline)      │
│ - QLoRA (Tim Dettmers et al., 2023)     │
│ - FastChat (lmsys; SFT pipeline)        │
└─────────────────────┬───────────────────┘
                      │
                      ↓
            LlamaFactory v22
                      │
                      ↓
┌─────────────────────────────────────────┐
│ Downstream research cited:              │
│ - 100+ research projects (model fams)   │
│ - RL methods: PPO/DPO/KTO/ORPO/SimPO   │
│ - Optimizers: GaLore/BAdam/APOLLO/      │
│   Adam-mini/Muon                        │
└─────────────────────────────────────────┘
```

### Pattern #19 4th archetype validation

**Pre-v22 state (post-v20):** Pattern #19 4th archetype (research-paper-chain) at N=1 (fish-speech v20 — 7 citations).

**v22 adds LlamaFactory:**
- PEFT + TRL + QLoRA + FastChat foundation citations
- 100+ research projects downstream
- ACL 2024 peer-reviewed publication

**N=2 validation.** Pattern #19 4th archetype now structurally confirmed.

### Pattern #32 promotion-readiness

Pattern #32 (Research-Paper-Chain Lineage standalone candidate) has N=2:
- fish-speech v20 (foundation-model-space)
- LlamaFactory v22 (training-infrastructure-space)

**Different outside-scope sub-types = 2 tier-equivalent categories.**

Per Pattern Library criteria ("≥3 observations across 2+ tiers OR structurally unambiguous at N=2"):
- N=2 observations ✓
- 2 distinct sub-types ✓
- Structurally unambiguous (extensive citation patterns both cases) ✓

**Pattern #32 PROMOTION-READY.**

## 7. Performance optimization suite

### 4 performance libraries integrated

| Library | Contribution |
|---------|--------------|
| **FlashAttention-2** | Attention compute speedup |
| **Unsloth** | 2× faster LoRA training |
| **Liger Kernel** | Custom CUDA kernels for training |
| **Contamination-free packing** | Sequence-packing without leakage |

### Cross-framework comparison

| Framework | Performance libs |
|-----------|------------------|
| Axolotl | FlashAttention-2, Unsloth |
| **LlamaFactory** | **FlashAttention-2 + Unsloth + Liger Kernel + contamination-free** |
| TRL alone | FlashAttention-2 |

**LlamaFactory = most performance-optimization integrated.**

## 8. Agent-adjacent features

### Function-calling dataset support

Although LlamaFactory is training-infrastructure (outside Storm Bear agent-scope), it supports:
- **Agent tuning via function-calling datasets** — fine-tune models on tool-use demonstrations

Means: Storm Bear operator could use LlamaFactory to fine-tune a model for their specific Scrum coaching agent.

### Scope note

Topic tag "agent" in repo metadata signals awareness of agent-use-case. But fine-tuning framework ≠ agent framework.

## 9. Evaluation tooling

### Integrated benchmarks

- **MMLU** (Massive Multitask Language Understanding)
- **C-Eval** (Chinese Eval)
- **CMMLU** (Chinese MMLU)

### Experiment tracking

- **W&B** (Weights & Biases)
- **SwanLab** (CN alternative)

### Pattern #8 6th data point

LlamaFactory supports published benchmarks natively. Plus ACL 2024 peer-reviewed publication. **6th corpus evidence of empirical-research-as-feature (Pattern #8)**, with strongest rigor level to date (peer-reviewed venue).

## 10. Cross-framework landscape

### Fine-tuning framework ecosystem

| Framework | Scope | Stars |
|-----------|-------|-------|
| TRL (HuggingFace) | RLHF pipeline | ~15K |
| PEFT (HuggingFace) | Parameter-efficient methods | ~20K |
| Axolotl | Configuration-driven training | ~10K |
| Unsloth | Speed-optimized LoRA | ~30K |
| **LlamaFactory** | **Unified all-above + more** | **70.3K** |

**LlamaFactory = largest-scale fine-tuning framework** (measured by stars).

### Why #1 scale?

- **Unified** — replaces fragmented tooling
- **Broadest models** — 100+ families
- **Research-velocity** — newest methods integrated quickly
- **WebUI + CLI + API** — accessibility across expertise levels
- **ACL 2024** — academic credibility
- **CN community** — large user base
- **Efficient at scale** — FSDP+QLoRA on consumer GPUs

## 11. Key observations

### Cluster-level

- **6 fine-tuning methods + 9 training stages** — comprehensive
- **5 RL alignment methods** — most in any comparable framework
- **5 cutting-edge optimizers** — research-velocity competitive edge
- **4 performance libraries** — FlashAttention-2 + Unsloth + Liger + contamination-free
- **Research-paper-chain lineage** — PEFT + TRL + QLoRA + FastChat + 100+ projects

### Cross-corpus

- **Pattern #19 4th archetype N=2 validation** (via fish-speech v20 + LlamaFactory v22)
- **Pattern #32 promotion-ready** (2 observations across 2 outside-scope sub-types)
- **Pattern #8 6th data point** (ACL 2024 peer-reviewed)
- **Pattern #43 candidate** (Optimizer-Research Integration Velocity)

## 12. References

- Parent: [[(C) index]]
- Source: README methods + training section + arXiv 2403.13372
- Sibling clusters: [[(C) README + 100+ models + positioning cluster summary]] + [[(C) Deployment + community + ACL 2024 cluster summary]]

---

**Cluster summary: 6 fine-tuning methods + 9 training stages + 5 RL alignment methods + 5 cutting-edge optimizers + 4 performance libraries. Research-paper-chain lineage (PEFT + TRL + QLoRA + FastChat + 100+ research) validates Pattern #19 4th archetype at N=2 (via fish-speech v20 + LlamaFactory v22). Pattern #32 Research-Paper-Chain Lineage PROMOTION-READY. Pattern #43 candidate (Optimizer-Research Integration Velocity) formalized. Pattern #8 6th and most-rigorous data point (ACL 2024 peer-reviewed venue).**
