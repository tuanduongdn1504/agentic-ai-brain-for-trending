# (C) Dual-AR + GRPO + RVQ Architecture

> **Type:** Entity — technical core architecture
> **Parent:** [[(C) index]]
> **Sources:** README architecture section + arXiv 2603.08823 (2026 S2 Tech Report)
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

fish-speech S2 Pro employs a **Dual-Autoregressive (Dual-AR) architecture** — Slow AR (4B params) for semantic/prosody planning + Fast AR (400M params) for frame-level generation, with **RVQ codec** (10 codebooks, ~21 Hz) as decoder. Alignment via **GRPO** (Group Relative Policy Optimization). Achieves 0.195 RTF, ~100ms TTFA, 0.54% WER CN / 0.99% WER EN on Seed-TTS Eval.

## 2. Key claims

1. Dual-AR separates semantic planning (Slow 4B) from acoustic generation (Fast 400M)
2. RVQ codec at ~21 Hz is lowest framerate in TTS (highest info/token)
3. GRPO = first RL alignment for TTS in corpus (LLM-technique cross-transfer)
4. 10M hours training = foundation-model-scale corpus
5. 3 corpus-first architectural elements

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| Dual-AR 4B+400M | README + arXiv 2603.08823 | High |
| RVQ 10 codebooks @ 21 Hz | README architecture | High |
| GRPO alignment | speech.fish.audio + README | High |
| 10M hours training | speech.fish.audio | High |
| Benchmarks | Seed-TTS Eval + EmergentTTS-Eval | High (published) |

## 4. Architecture diagram

```
Text input (80+ languages, emotion tags)
           ↓
  ┌────────────────────┐
  │ Slow AR (4B params)│  ← semantic + prosody + emotion planning
  │ Qwen3-derived?     │
  └─────────┬──────────┘
            ↓ semantic acoustic tokens
  ┌────────────────────┐
  │ Fast AR (400M)     │  ← frame-level detail + speed
  └─────────┬──────────┘
            ↓ fine-grained acoustic tokens
  ┌────────────────────┐
  │ RVQ Decoder        │  ← 10 codebooks, ~21 Hz
  │ (Residual Vector   │
  │  Quantization)     │
  └─────────┬──────────┘
            ↓
  Audio output (24 kHz sample rate)
```

## 5. Slow AR (4B params)

### Role

- Handles **semantic representation** — what to say, how to emphasize
- Processes **emotion tags** — `[whisper]`, `[excited]`, `[laugh]` → internal state
- **Prosody planning** — pitch contour, rhythm, pauses
- Produces **semantic acoustic tokens** (coarse, low-rate)

### Likely architecture

README mentions Qwen3 as influence. 4B param count consistent with Qwen3-based backbone. Attention + MLP stack, likely ~24-32 layers.

### Why big model for planning

Semantic planning requires language understanding comparable to LLM. 4B at this layer enables:
- Context-aware pronunciation (homographs disambiguated by context)
- Emotional inference from punctuation/context
- Multilingual semantic transfer

## 6. Fast AR (400M params)

### Role

- Takes **semantic tokens** from Slow AR
- Generates **fine-grained acoustic tokens** at frame rate
- **Low-latency** — needs to keep up with streaming

### Why small model for generation

Once semantic plan is fixed, acoustic detail generation is more local/mechanical. 400M suffices. Enables:
- Real-time streaming (~100ms TTFA)
- 3,000+ tokens/s throughput on H200
- Low $/hour cloud serving

## 7. RVQ Codec — 10 codebooks @ ~21 Hz

### Residual Vector Quantization

- **Cascade of 10 quantizers** — first codebook captures coarse audio structure; subsequent codebooks refine residuals
- **~21 Hz frame rate** — very low vs typical TTS codecs (50-100 Hz)
- Each frame encoded via 10 tokens (one per codebook)

### Implications of low framerate

At 21 Hz:
- 1 minute audio = 1,260 frames = 12,600 tokens (at 10 codebooks)
- LLM context 32K ≈ 2.5 minutes continuous audio
- At 128K context ≈ 10 minutes continuous generation

Enables:
- Long-form narration
- Multi-turn context preservation
- Streaming with low token rate

### Corpus-first

**First RVQ codec** explicitly detailed in corpus. First low-framerate (21 Hz) TTS codec mentioned.

## 8. GRPO Alignment

### Group Relative Policy Optimization

GRPO = RL variant used in DeepSeek-R1 / Qwen-R1 for LLM alignment. Adapted for TTS generation.

### Mechanism

1. Generate multiple samples per text+emotion-tag prompt
2. Human/automated evaluator ranks samples
3. **Relative preference** — compare within group (not absolute reward)
4. Policy update via GRPO objective

### Why GRPO for TTS

- **Preference-based:** TTS quality is subjective; pairwise preference > absolute metric
- **Group-relative:** multiple samples per prompt allows within-batch preference signal
- **Stable:** avoids reward-hacking seen in PPO-style RLHF

### Result

- **EmergentTTS-Eval win rate: 81.88%**
- Emotional tag fidelity improved via alignment
- Natural prosody preferred over monotone baseline

### Corpus-first

**First RL alignment for generation** in Storm Bear corpus. Prior: LLM-space only. Signals alignment-technique cross-modality transfer.

## 9. Training corpus — 10 million hours

### Scale comparison

| Dataset | Hours | Domain |
|---------|-------|--------|
| LibriSpeech | 960 | EN audiobook |
| Common Voice | ~20K | Multilingual reads |
| Whisper training | ~680K | Multilingual speech |
| **fish-speech S2 Pro** | **10M (10,000K)** | **Multilingual speech + voices** |

**fish-speech training corpus ≈ 15× Whisper.** Foundation-model scale.

### Implications

- Zero-shot voice cloning from 10-30s reference
- 80+ language support without phoneme requirements
- Emotional/prosodic range from natural variation in corpus

## 10. Performance profile

### On NVIDIA H200

| Metric | Value |
|--------|-------|
| Real-Time Factor (RTF) | 0.195 (5.13× faster than real-time) |
| Time-to-first-audio (TTFA) | ~100ms |
| Throughput | 3,000+ acoustic tokens/s |
| Audio sample rate | 24 kHz |

### On consumer GPUs (estimated)

- RTX 4090: RTF ~0.5-0.8 (still faster than real-time)
- RTX 3090: RTF ~0.8-1.2 (near real-time)
- CPU only: not officially supported at production quality

## 11. Benchmarks

### Seed-TTS Eval (WER)

| Language | WER |
|----------|-----|
| Chinese | 0.54% |
| English | 0.99% |

Lower is better. Comparable to or exceeds ElevenLabs, OpenAI TTS, Azure Neural TTS on Seed-TTS Eval (per arXiv claim).

### EmergentTTS-Eval (preference win-rate)

- **81.88% win rate** vs baseline TTS systems

Higher is better. Demonstrates GRPO alignment effectiveness.

## 12. Edges + failure modes

### Known limitations

- **Out-of-distribution voices** — voice clone quality depends on reference audio quality
- **Code-switching** — mixing languages mid-sentence may degrade
- **Very short inputs** — <3 words may have insufficient context
- **Background noise in reference** — clean reference audio recommended
- **Emotional tag conflicts** — `[whisper]` + `[shout]` undefined behavior
- **Long-form drift** — multi-minute continuations may lose speaker consistency (Fast AR locality bias)

### Unverified claims

- "Best TTS both open source and closed source" — marketing claim; independent benchmarks vary
- RTF/TTFA on consumer GPUs — only H200 numbers published
- 80+ languages — Tier 3 (70+) quality likely variable

## 13. Related concepts

- [[(C) Multilingual 80+ Language TTS + 7-Lang README]] — multilingual scope enabled by this architecture
- [[(C) 39 AI INC + Research-Paper-Chain Lineage]] — research lineage contributing to architecture
- [[(C) Outside-Scope + Pattern 19 4th Archetype + Storm Bear]] — how architecture fits outside-scope
- Pattern #8 (research benchmark emergence) — Seed-TTS + EmergentTTS-Eval = 5th data point
- Parent: [[(C) index]]

## References

- README architecture section
- arXiv 2603.08823 (2026 S2 Tech Report)
- arXiv 2411.01156 (2024 v1.4 paper)
- speech.fish.audio

---

**Dual-AR (Slow 4B + Fast 400M) + RVQ (10 codebooks @ 21Hz) + GRPO RL alignment + 10M hours training. 3 corpus-first architectural elements. 0.54% WER CN, 0.99% WER EN, 81.88% win rate, RTF 0.195 on H200. Foundation-model-scale TTS.**
