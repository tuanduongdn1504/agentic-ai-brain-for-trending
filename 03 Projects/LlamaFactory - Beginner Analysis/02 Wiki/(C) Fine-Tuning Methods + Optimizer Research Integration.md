# (C) Fine-Tuning Methods + Optimizer Research Integration

> **Type:** Entity — technical depth (fine-tuning methods + optimizer research)
> **Parent:** [[(C) index]]
> **Sources:** README methods section + arXiv 2403.13372 + optimizer papers
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

LlamaFactory integrates **6 fine-tuning methods** (Full, Freeze, LoRA, QLoRA, OFT, QOFT) and **5 cutting-edge optimizers** (GaLore, BAdam, APOLLO, Adam-mini, Muon — all 2024 research). Performance stack includes FlashAttention-2, Unsloth, Liger Kernel, and contamination-free packing. Enables **70B model fine-tuning on 2×24GB consumer GPUs** via QLoRA+FSDP. **Pattern #43 candidate formalized:** Optimizer-Research Integration Velocity — framework integrates cutting-edge research rapidly as competitive edge.

## 2. Key claims

1. 6 fine-tuning methods (most in comparable frameworks)
2. 5 novel 2024 optimizers integrated (research-velocity competitive edge)
3. FSDP+QLoRA enables 70B on 2×24GB (consumer hardware democratization)
4. 4 performance libraries (FlashAttention-2 + Unsloth + Liger + contamination-free)
5. Pattern #43 candidate (Optimizer-Research Integration Velocity)

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 6 fine-tuning methods | README | High |
| 5 optimizer integration | README + individual optimizer papers | High |
| 70B on 2×24GB claim | README + community benchmarks | Medium (depends on config) |
| Performance library integration | README + benchmarks | High |

## 4. Fine-tuning methods — 6 methods

### Method classification

| Method | Params trained | Memory | Quality | Speed |
|--------|----------------|--------|---------|-------|
| **Full** | 100% | Highest | 100% | Slowest |
| **Freeze** | ~20-50% | High | ~95% | Medium |
| **LoRA** | <1% (adapter) | Low | ~90-95% | Fast |
| **QLoRA** | <1% + 4-bit quant | Lowest | ~90-95% | Fast |
| **OFT** | <1% (orthogonal) | Low | ~90-95% | Fast |
| **QOFT** | <1% + 4-bit quant | Lowest | ~90-95% | Fast |

### Full-tuning vs parameter-efficient

**Full:** all weights updated; needs 8× parameter count GPU memory (e.g., 7B model needs 56GB).

**Parameter-efficient (LoRA et al.):** only trainable adapters updated; can fit on consumer GPUs.

### OFT vs LoRA (novel)

OFT (Orthogonal Fine-Tuning, 2023-2024 research):
- Instead of adding adapters, constrain updates to orthogonal transformations
- **Preserves pretrained knowledge better** (avoids catastrophic forgetting)
- Same efficiency as LoRA

QOFT = quantized variant for memory efficiency.

**Most fine-tuning frameworks don't include OFT yet.** LlamaFactory ships it ahead of competition.

## 5. Cutting-edge optimizer integration (5 novel 2024 optimizers)

### Optimizer catalog

| Optimizer | Year | Innovation |
|-----------|------|-----------|
| **GaLore** (Gradient Low-Rank Projection) | 2024 | Low-rank gradient projection → full-training in LoRA memory |
| **BAdam** (Block-coordinate Adam) | 2024 | Update blocks of params sequentially → memory efficiency |
| **APOLLO** | 2024 | Adafactor-like with further memory reduction |
| **Adam-mini** | 2024 | Adam variant with reduced optimizer state (~45% less memory) |
| **Muon** | 2024 | Spectral-normalization-based; Keller Jordan et al. |

### GaLore significance

- Enables **full-tuning** of LLaMA-7B on 24GB consumer GPU
- Previously required LoRA for consumer hardware
- Breakthrough: full-tuning memory reduced to LoRA levels

### Muon significance

- Emerging optimizer in research community (2024)
- Reportedly faster convergence than Adam for large-scale training
- LlamaFactory integrates within months of publication

### Research-integration velocity

Pattern: LlamaFactory ships research optimizers within 1-6 months of publication. Most production frameworks wait 1-2 years.

## 6. Pattern #43 candidate — Optimizer-Research Integration Velocity

### Formal statement (candidate)

> "Framework integrates cutting-edge research (optimizers, RL methods, fine-tuning techniques) within 1-6 months of publication, faster than corporate-stable frameworks. Research-velocity is competitive edge."

### Evidence at v22

1 (LlamaFactory — 5 novel 2024 optimizers + 5 RL methods shipped within research-current window)

### Required for promotion

2+ frameworks with similar research-velocity pattern.

### Prediction

Research-first frameworks (academic-community backed) may cluster in this pattern. Competitive with corporate-stable frameworks that prioritize consistency over velocity.

### Contrast with corporate-stable

- **Corporate frameworks** (e.g., TRL by HuggingFace): ships stable methods, delays adoption of unstable research
- **Research-velocity frameworks** (LlamaFactory): ships research, iterates on stability

Both valid models. Different target audiences.

## 7. Performance optimization suite (4 libraries)

### Library integration

| Library | Contribution | Speedup typical |
|---------|--------------|-----------------|
| **FlashAttention-2** | Memory-efficient attention | 2-3× for long contexts |
| **Unsloth** | Custom CUDA kernels for LoRA | 2× LoRA training |
| **Liger Kernel** | Chunked cross-entropy + fused ops | 1.5-2× overall |
| **Contamination-free packing** | Sequence-packing without token leakage | Throughput gains |

### Contamination-free packing (novel)

**Standard packing:** concatenate sequences to fill context → attention leaks between sequences → contaminates training

**Contamination-free packing:** attention mask blocks cross-sequence attention → clean training despite packing

**LlamaFactory ships contamination-free packing** — reduces dataset token waste while preserving training integrity.

### Cross-framework comparison

| Framework | Performance libs |
|-----------|------------------|
| TRL alone | FlashAttention-2 only |
| Axolotl | FlashAttention-2 + Unsloth |
| Unsloth alone | Custom kernels (2× LoRA) |
| **LlamaFactory** | **FlashAttention-2 + Unsloth + Liger + contamination-free (4)** |

**LlamaFactory = most performance-optimization integrated.**

## 8. Distributed training — FSDP+QLoRA breakthrough

### The 70B on 2×24GB claim

**Hardware:** 2× NVIDIA RTX 3090 or 4090 (24GB each = 48GB total)

**Method:**
1. **QLoRA** quantizes LLaMA-70B weights to 4-bit (~35GB unquantized → 9GB quantized)
2. **LoRA adapters** add minimal trainable params (~200MB)
3. **FSDP** shards the quantized model across 2 GPUs
4. Each GPU holds ~4.5GB of model weights + training state

### Significance

**Democratizes 70B fine-tuning** to consumer hardware. Previously required:
- 8× A100 80GB (~$15/hour cloud) minimum
- Or 4× A100 40GB
- Or specialized enterprise GPUs

Now: 2× consumer GPUs (~$3-5K one-time cost, zero hourly).

### Memory-innovation layered stack

```
┌──────────────────────────────────┐
│ 1. QLoRA (4-bit quantization)    │ → reduces weights 4×
├──────────────────────────────────┤
│ 2. LoRA (adapter-only training)  │ → avoids optimizer states for full weights
├──────────────────────────────────┤
│ 3. FSDP (sharding across GPUs)   │ → distributes remaining memory
├──────────────────────────────────┤
│ 4. GaLore (low-rank gradients)   │ → further memory reduction if used
└──────────────────────────────────┘
```

Each layer compounds memory savings.

## 9. Megatron-core backend (corpus-first)

### NVIDIA Megatron-core integration

LlamaFactory also supports Megatron-core for:
- **Tensor parallelism** (split attention heads / MLP)
- **Pipeline parallelism** (split layers across GPUs)
- **Context parallelism** (split sequence)
- **Enterprise-scale** training (hundreds of GPUs)

### Dual-mode framework

| Mode | Target |
|------|--------|
| Consumer (QLoRA + FSDP) | Researchers + individuals |
| Enterprise (Megatron-core) | Labs + corporations |

**LlamaFactory = first corpus framework spanning consumer ↔ enterprise** in single repo.

## 10. Fine-tuning workflow example

### End-to-end LoRA fine-tuning

```bash
# Install
pip install llamafactory

# Download base model (or use HuggingFace cache)
huggingface-cli download Qwen/Qwen2.5-7B-Instruct

# Launch Gradio WebUI
llamafactory-cli webui

# Or CLI-direct fine-tuning
llamafactory-cli train \
  --model_name_or_path Qwen/Qwen2.5-7B-Instruct \
  --dataset alpaca_gpt4_en \
  --finetuning_type lora \
  --lora_rank 8 \
  --lora_alpha 16 \
  --num_train_epochs 3 \
  --learning_rate 2e-4 \
  --output_dir ./qwen-finetuned
```

### Time-to-first-fine-tune

- Install: 5 minutes
- Download base model: 5-30 minutes (model size dependent)
- Config + launch: 1-2 minutes
- Training (LoRA on 10K examples): 30-60 minutes (depends on GPU)

**Total: ~1 hour to first fine-tuned model** on typical hardware.

## 11. Edges + failure modes

### Known failure modes

- **Memory OOM** — even with QLoRA+FSDP, long sequences (>4K tokens) can OOM
- **Training divergence** — aggressive learning rate can cause loss explosion
- **Catastrophic forgetting** — LoRA adapters may erase pretrained capabilities
- **Overfitting** — small datasets + high rank = overfit
- **Reward hacking** — PPO alignment can exploit reward model patterns
- **OFT/QOFT maturity** — newer methods may have edge-case bugs
- **Optimizer instability** — cutting-edge optimizers (Muon) may be less stable than Adam

### Hyperparameter sensitivity

Despite unified framework, training quality still requires:
- Dataset quality (garbage in, garbage out)
- Hyperparameter tuning (learning rate critical)
- Monitoring + early stopping (prevent overfitting)
- Evaluation on held-out set (not training metrics)

**LlamaFactory doesn't replace expertise** — it reduces framework-complexity, not training-complexity.

## 12. Related concepts

- [[(C) 100+ Model Support + Unified Training Stages]] — stage context
- [[(C) Training methods + optimizers + research-lineage cluster summary]] — broader context
- [[(C) Academic-Lab Archetype + Pattern 19 4th Archetype N=2 Validation]] — research connections
- Pattern #43 Optimizer-Research Integration Velocity — formalized here
- Parent: [[(C) index]]

## References

- README methods section
- arXiv 2403.13372 (ACL 2024)
- GaLore / BAdam / APOLLO / Adam-mini / Muon papers (individual)
- QLoRA paper (Tim Dettmers et al., 2023)

---

**6 fine-tuning methods (Full/Freeze/LoRA/QLoRA/OFT/QOFT) + 5 cutting-edge 2024 optimizers (GaLore/BAdam/APOLLO/Adam-mini/Muon) + 4 performance libraries (FlashAttention-2/Unsloth/Liger/contamination-free). FSDP+QLoRA enables 70B model fine-tuning on 2×24GB consumer GPUs. Megatron-core backend for enterprise. Pattern #43 candidate (Optimizer-Research Integration Velocity) formalized — framework integrates cutting-edge research within 1-6 months as competitive edge.**
