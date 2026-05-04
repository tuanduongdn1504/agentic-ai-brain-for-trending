# (C) README + 7-language i18n + philosophy cluster summary

> **Cluster:** README.md (English primary) + 7-language i18n presence + positioning
> **Parent:** [[(C) index]]
> **Sources:** github.com/fishaudio/fish-speech/README.md + speech.fish.audio
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Positioning + philosophy** — SOTA TTS claim, anti-closed-source framing
2. **7-language README presence** — largest i18n in corpus
3. **Use-case breadth** — voice cloning, multi-speaker, multilingual, emotional control

## 2. Positioning — SOTA claim

### Tagline

> **"SOTA Open Source TTS"**

### Full positioning (speech.fish.audio)

> *"the best text-to-speech system among both open source and closed source"*

### Anti-closed-source framing

> *"Leveraging Large Language Models for Advanced Multilingual Text-to-Speech"*

fish-speech positions itself as **challenger to commercial TTS** (ElevenLabs, OpenAI TTS, Azure TTS) at open-source quality parity. Distinct from:
- Competitor-category framing (paperclip "zero-human companies")
- Productivity framing (spec-kit 48× speedup)
- **Quality-parity framing** (fish-speech benchmark-vs-closed-source)

## 3. Philosophy — "soul" via fine-grained control

### Emotion/instruction tags

**15,000+ emotion/instruction tags** + free-form text support. Inline natural language control:

```
[whisper] this is a secret
[excited] we won!
[laugh] that's ridiculous
```

### Design statement

> *"fine-grained control of prosody and emotion using natural language tags"*

**Novel design:** instead of separate emotion parameters (valence/arousal vectors) or reference-audio-based emotion transfer, fish-speech uses **inline text tags** — prompt-style control familiar from LLM usage.

## 4. 7-language README presence (largest i18n in corpus)

### Languages

| # | Language | README file |
|---|----------|-------------|
| 1 | English | README.md (primary) |
| 2 | 简体中文 (Chinese Simplified) | README.zh-CN.md |
| 3 | Português | README.pt-BR.md |
| 4 | 日本語 (Japanese) | README.ja.md |
| 5 | 한국어 (Korean) | README.ko.md |
| 6 | العربية (Arabic) | README.ar.md |
| 7 | Español (Spanish) | README.es.md |

### Corpus i18n comparison

| Wiki | i18n |
|------|------|
| graphify v16 | CJK-trio (en+ja+ko+zh) — 4 langs |
| TrendRadar v19 | CN+EN bilingual — 2 langs |
| multica v15 | zh-CN translation — 2 langs |
| deer-flow v9 | zh-CN translation — 2 langs |
| **fish-speech v20** | **EN + CN + PT + JP + KR + AR + ES — 7 langs** |

**7 languages = corpus-largest.** Rationale: TTS product aims 80+ languages operationally; documentation breadth matches product scope. Pattern: documentation i18n correlates with product multilingual scope.

## 5. 80+ language support

### Tier structure

**Tier 1 (flagship):** Chinese, English, Japanese
**Tier 2 (strong):** Korean, Spanish, Portuguese, Arabic, Russian, French, German
**Tier 3:** 70+ additional languages

No phoneme requirements — purely text-conditioned (novel vs many TTS systems requiring phonetic transcription).

### Training corpus

**10 million hours audio** — foundation-model-scale corpus. Comparable to:
- Whisper (OpenAI): ~680K hours
- **fish-speech: ~10M hours (15× Whisper scale)**

Implication: fish-speech is **foundation-model-scale**, not task-specific fine-tune. Scale enables zero-shot voice cloning + multilingual transfer.

## 6. Feature list

### Core TTS capabilities

- **Fine-grained control** — 15,000+ emotion/instruction tags inline
- **Multi-speaker generation** — from single reference audio, produce multiple distinct speakers
- **Multi-turn generation** — context-aware continuation across turns
- **Rapid voice cloning** — 10-30s sample, no fine-tuning required
- **Multilingual** — 80+ languages, no phoneme requirement

### Performance claims (H200 GPU)

- **Real-Time Factor (RTF):** 0.195 (5× faster than real-time)
- **Time-to-first-audio:** ~100ms (streaming-capable)
- **Throughput:** 3,000+ acoustic tokens/s

### Benchmarks published

- **Seed-TTS Eval:** 0.54% WER on Chinese, 0.99% WER on English
- **EmergentTTS-Eval:** 81.88% win rate
- **vs closed-source:** "best TTS among both open source and closed source" (unverifiable but claimed)

## 7. Use cases (documented)

### From README

- **Voice cloning** — podcast production, audiobook narration, personalized assistants
- **Multilingual dubbing** — cross-language content production
- **Accessibility** — screen readers, visually-impaired tools
- **Interactive agents** — real-time voice for conversational AI
- **Streaming** — low-latency production via SGLang

### Cross-agent integration potential (not explicit)

TTS is *capability* for agents — not itself agent framework. fish-speech could serve voice-output layer for:
- Voice-enabled Claude Desktop (hypothetical)
- Multilingual customer support agents
- Accessibility layers over any agent framework

## 8. Install + deployment options

### Install channels

- **pip install** — Python package (primary)
- **Docker** — `fishaudio/fish-speech` Docker Hub
- **HuggingFace** — `fishaudio/s2-pro` model card
- **SGLang server** — production inference
- **WebUI** — Gradio interface for local use
- **Inference.ipynb** — Jupyter notebook for experimentation

### Hardware requirements

- **Recommended:** NVIDIA H200 (for quoted RTF 0.195)
- **Viable:** consumer GPUs (RTX 3090/4090) at reduced throughput
- **CPU:** not officially supported at production quality

## 9. Community + governance

### Community

- **Discord:** https://discord.gg/Es5qTB9BcN
- **QQ Channel** (CN-community — suggests CN-origin or CN-heavy user base)
- **HuggingFace** comments + community

### Governance artifacts

- **README.md** (7 languages)
- **LICENSE** (Fish Audio Research License — custom non-OSI)
- **docs site:** speech.fish.audio (mkdocs-based)
- **pyproject.toml**

**Absent (compared to corpus):**
- ❌ AGENTS.md (Pattern #22 industry standard) — not present
- ❌ CONTRIBUTING.md — not prominent
- ❌ CODE_OF_CONDUCT.md — not prominent
- ❌ SECURITY.md — not prominent
- ❌ OpenClaw/Hermes references (Pattern #18 consistent — CN-origin + foundation-model both skip)

Pattern match: fish-speech has **minimal community-contribution governance** compared to agent frameworks in corpus. Reflects foundation-model-as-product nature (consumer, not community contribution).

## 10. Citation (BibTeX documented)

From README:

```bibtex
@article{fishaudio2026s2,
  title={Fish-Speech S2 Pro: [full title TBD]},
  author={Fish Audio},
  journal={arXiv preprint arXiv:2603.08823},
  year={2026}
}

@article{fishaudio2024v14,
  title={Fish-Speech v1.4},
  author={Fish Audio},
  journal={arXiv preprint arXiv:2411.01156},
  year={2024}
}
```

Pattern: **2 arXiv publications** = formal research corpus contribution. Positions fish-speech as research artifact, not only product.

## 11. Key observations

### Cluster-level

- **7-language README** = corpus-largest i18n (operational scope requirement)
- **Foundation-model-scale** — 10M hours, distinct from task-specific fine-tunes
- **Inline emotion tags** — novel vs parametric emotion control
- **Quality-parity positioning** — benchmark-driven vs closed-source comparison
- **arXiv-published** — formal research artifact (5th Pattern #8 data point)

### Cross-corpus

- **Largest i18n** — exceeds graphify CJK-quad, TrendRadar CN+EN
- **2nd CN-ecosystem presence** — after TrendRadar v19 (Pattern #18 regional evidence)
- **1st foundation-model product** in corpus — outside-scope but novel pattern

## 12. References

- Parent: [[(C) index]]
- Source: github.com/fishaudio/fish-speech README.md + speech.fish.audio
- Sibling clusters: [[(C) Dual-AR architecture + GRPO + research-lineage cluster summary]] + [[(C) Custom LICENSE + 39 AI INC + SGLang production cluster summary]]

---

**Cluster summary: README + 7-language i18n + positioning. SOTA TTS claim + 80+ languages + 15,000+ emotion tags + 10M hours training + foundation-model-scale. 7-language i18n = corpus-largest. Quality-parity framing vs closed-source commercial TTS.**
