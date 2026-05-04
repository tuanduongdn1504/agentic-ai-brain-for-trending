# (C) val_bpb Metric + Evaluation Fairness

> Entity page — Measurement concept
> Sources: README metric section + autoresearch evaluation methodology
> Format: 13-section canonical

## 1. What is it / Nó là gì

**val_bpb = validation bits-per-byte** — metric used by autoresearch. **Vocabulary-size-independent** measure of model quality. Lower = better. Enables fair comparison across architectural variations (different vocab sizes, attention patterns, optimizers). Single objective agent optimizes.

**bits-per-byte** = avg information content needed to encode next byte of held-out data. Model confidence → lower bpb → better.

## 2. Why it matters / Sao quan trọng

### Traditional ML metrics have limitations

**Cross-entropy loss:**
- Depends on vocabulary size
- Bigger vocab = smaller loss (trivially)
- **Can't compare** across vocab changes

**Perplexity:**
- Exponentiated cross-entropy
- Same vocab-dependency issue
- Traditional NLP metric

**Token accuracy:**
- Position-invariant but binary
- Can't measure confidence

### val_bpb solves

- **Vocabulary-invariant:** bits of information per BYTE (not per token)
- **Universal scale:** comparable across tokenizers
- **Continuous:** captures confidence gradation
- **Information-theoretic:** grounded in Shannon entropy

## 3. Mathematical intuition (simplified)

### Setup
- Model M produces probability p(token | context)
- Evaluate on held-out validation set
- Compute total cross-entropy
- **Convert to bits-per-byte:**

```
bpb = cross_entropy / (bytes_in_validation * log(2))
```

### Interpretation

- **8 bits/byte:** Model says nothing useful (pure uniform)
- **0 bits/byte:** Model perfectly predicts (impossible)
- **Real-world range:** ~0.8-2 bits/byte typical for language models

### Lower = better
- Agent optimizes DOWN
- val_bpb = 0.83 better than 0.87

## 4. Why fairness matters for autoresearch

### Agent modifies train.py

Changes could include:
- **Different vocab size** (8192 → 16384)
- **Different tokenizer** (BPE → Unigram)
- **Different attention pattern** (SSSL → L)
- **Different optimizer** (Muon+AdamW → AdamW alone)

**Without vocab-invariant metric:**
- Agent could increase vocab → smaller loss by construction
- "Improvement" is artifact of tokenization, not model quality
- Misleading research

**With val_bpb:**
- Vocab change = different encoding efficiency
- Fair comparison via byte normalization
- Agent must find real improvements

## 5. Fixed 5-min budget = complementary fairness

Metric fairness (val_bpb) + time fairness (5-min budget) = **double fairness**:

1. **Same metric unit** — val_bpb
2. **Same time budget** — 5 min wall-clock
3. **Same data** — prepare.py fixed
4. **Same evaluation** — program.md forbids alteration

→ **Any improvement = real architectural insight**, not metric gaming or budget exploitation.

### Variables allowed to vary
- Model architecture (depth, attention, ...)
- Optimizer
- Batch size
- Sequence length
- Vocab size (but val_bpb normalizes)
- Any hyperparameter

### Variables held constant
- Training data
- Evaluation data
- Metric (val_bpb)
- Wall-clock budget (5 min)

## 6. Agent behavior under val_bpb + budget

### Optimal agent strategy

Try hypotheses that could improve val_bpb within 5 min:
- Better attention pattern → more efficient learning
- Better optimizer → faster convergence
- Better batch size → better gradient signal
- Smaller model if it converges faster in budget

### What agent should NOT optimize

- **Total parameters** — irrelevant (val_bpb normalizes)
- **Training time** — fixed (not a knob)
- **Inference speed** — not measured
- **Energy consumption** — not measured

### What agent DOES optimize (direct)

- **val_bpb at 5-min mark**

### What agent optimizes (emergent)

- **Architectural efficiency per compute** — implicit from budget constraint
- **Fast-converging hypotheses** — slow converging = lost

## 7. Memory as secondary metric

program.md mentions: VRAM increases acceptable only for meaningful gains.

**Implication:** Implicit multi-objective — val_bpb primary, memory secondary. Agent penalizes memory-hungry changes that only marginally improve val_bpb.

### Secondary metrics risk

- Agent may avoid valuable high-memory experiments
- Smaller models preferred even when bigger would be better long-term
- Over-bias toward constrained search

## 8. Trade-offs / Limitations

### Strengths
- **Vocab-invariant** — solves real comparison problem
- **Information-theoretic** — grounded, not ad-hoc
- **Continuous** — captures nuance
- **Single-value** — easy agent objective

### Weaknesses
- **Narrow objective** — ignores downstream task performance
- **Training-time metric** — doesn't measure generalization beyond val set
- **No robustness measurement** — model might overfit val set
- **Byte-level assumption** — may not match actual use case (tokens often more natural)
- **Single data distribution** — val set fixed; doesn't test OOD

## 9. Comparison to sibling metric approaches

### T1 agent tools (ECC, Superpowers, gstack, GSD)
- **No formal metric** — user judges quality
- **Subjective** — "did Claude help?"
- **No iteration optimization** — per-user per-session

### T2 goclaw
- Platform-level metrics (uptime, latency, throughput)
- Not agent-quality metrics

### T3 course
- Subject completion metric
- Quiz scores

### T4 notebooklm-py
- **Per-call success/fail** — binary
- No quality metric per invocation

### T5 deer-flow
- **Per-task completion** — did agent complete task?
- Quality = human review
- No val_bpb-like optimization loop

### **T5 autoresearch**
- **val_bpb explicit** — enables iteration loop
- Most quantitative of all wikis

→ **autoresearch uniquely quantitative.** Others rely on subjective quality.

## 10. Common pitfalls

1. **Metric hacking** — agent finds way to improve val_bpb without real improvement (e.g., collapse to high-frequency tokens)
2. **Validation set memorization** — agent somehow gets access to val (should be prevented by prepare.py)
3. **Overfitting val_bpb** — model optimized for this specific distribution; fails elsewhere
4. **Ignoring training instability** — crashes treated as reverts; but unstable-then-good might be valuable
5. **Forgetting compute cost** — val_bpb improvement at 10x compute = meaningless; budget enforces
6. **Single-metric tunnel vision** — model robustness, fairness, latency ignored
7. **Noise interpretation** — 1% val_bpb change might be random; need confidence intervals (not done)

## 11. When NOT to use val_bpb-style metric

- **Multi-objective research** — many metrics matter (performance + fairness + cost + robustness)
- **Downstream-task focused** — val_bpb doesn't predict task success
- **Production ML** — serving metrics matter, not just val_bpb
- **Small datasets** — val_bpb noisy with limited validation data
- **Categorical outputs** — accuracy/F1 often more natural

## 12. Storm Bear vault relevance

### Storm Bear lacks quantitative metric

Storm Bear wikis evaluated subjectively:
- 13-section format compliance (boolean)
- Published guide quality (implicit)
- Cross-reference count (mentioned in iteration logs)

**Risk:** Drift, inconsistent quality over time.

### Could Storm Bear adopt quantitative metric?

**Candidate Storm Bear metrics:**

1. **Section compliance score** — entity page = 13 sections present = 1.0
2. **Cross-ref density** — links per 100 lines
3. **Bilingual balance** — VN tokens : EN tokens ratio
4. **Freshness** — days since last update
5. **Graph connectivity** — how many siblings does wiki reference

**Combined quality score** could enable routine-version comparison (v1 vs v2 quality).

### Would enable routine-evolution experiments

If Storm Bear adopts wiki-quality metric:
- Routine v2 test: build 3 wikis with v2
- Compare quality scores vs v1 baseline
- Statistical: routine v2 improves quality by X%?
- Keep v2 if yes, else refine

**autoresearch pattern applied to knowledge domain.** Karpathy's approach generalized.

## 13. References / Nguồn

- Source: [[(C) README summary]] (val_bpb definition + methodology) + [[(C) program.md agent skill summary]] (metric optimization instructions)
- Related entities:
  - [[(C) 5-Minute Experiment Loop]] (metric evaluated here)
  - [[(C) Program.md as Agent Skill]] (metric defined in skill)
  - [[(C) Karpathy's Meta-contribution to Storm Bear]] (pattern generalizes)
- External:
  - Shannon entropy (information theory foundation)
  - Bits-per-byte tradition (data compression community, applied to LM)
