# (C) fish-speech — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) — 29.8K ⭐, 2.5K forks, **Fish Audio Research License** (custom non-OSI)
> **Tagline:** *"SOTA Open Source TTS"*
> **Philosophy:** *"The best text-to-speech system among both open source and closed source"*
> **Wiki:** `(C) index` — 20th LLM Wiki in Storm Bear corpus (**2nd outside-scope, after build-your-own-x v8**)
> **Audience:** VN developers + multimedia creators + accessibility engineers

---

## ⚠️ Read this FIRST — License boundary / Ranh giới giấy phép

### 🇻🇳 Tiếng Việt

**fish-speech KHÔNG phải open-source chuẩn OSI.** License custom "Fish Audio Research License" cho phép:
- ✅ **Nghiên cứu cá nhân / học thuật** — miễn phí
- ✅ **Đánh giá / thử nghiệm** — miễn phí
- ❌ **Sử dụng thương mại** — CẦN mua license từ Fish Audio (39 AI, INC.)
- ❌ **Dịch vụ Scrum coaching thu phí** — cần paid license
- ❌ **Dùng trong sản phẩm client** — cần paid license
- ❌ **Dùng để train foundation model khác** — CẤM (anti-distillation clause)

**Nếu bạn là Storm Bear operator làm commercial Scrum coaching:** fish-speech KHÔNG dùng được cho commercial. Xem xét Coqui TTS (MIT) / XTTS-v2 / ElevenLabs API / OpenAI TTS API thay thế.

### 🇬🇧 English

**fish-speech is NOT standard OSI open-source.** Custom "Fish Audio Research License" permits:
- ✅ Personal/academic research — free
- ✅ Evaluation/experimentation — free
- ❌ Commercial use — requires paid license from Fish Audio (39 AI, INC.)
- ❌ Paid Scrum coaching services — paid license required
- ❌ Client product use — paid license required
- ❌ Training competing foundation model — PROHIBITED (anti-distillation clause)

**If commercial use intended:** consider alternatives — Coqui TTS (MIT), XTTS-v2, ElevenLabs API, OpenAI TTS API.

---

## Part 1 — fish-speech là gì? / What is fish-speech?

### 🇻🇳 Tiếng Việt

**fish-speech** là hệ thống **text-to-speech (TTS) đa ngôn ngữ** SOTA (state-of-the-art) by Fish Audio (legal entity: **39 AI, INC.**). Training trên **10 triệu giờ audio** qua **80+ ngôn ngữ**, với zero-shot voice cloning từ 10-30 giây reference.

**Điểm nổi bật:**
- **29.8K stars** (#6 trong Storm Bear corpus)
- **Custom license** (first non-OSI trong corpus)
- **80+ languages** — tier 1 (CN/EN/JP flagship), tier 2 (7 strong), tier 3 (70+)
- **Dual-AR architecture** — Slow AR (4B) + Fast AR (400M) + RVQ codec
- **GRPO RL alignment** — first RL alignment for TTS trong corpus
- **15,000+ emotion/instruction tags** — `[whisper]`, `[excited]`, `[laugh]` inline
- **7-language README** — largest i18n in corpus (EN + 简体中文 + PT + JP + KR + AR + ES)
- **Voice cloning** — 10-30s sample, no fine-tuning
- **Seed-TTS Eval:** 0.54% WER CN / 0.99% WER EN
- **EmergentTTS-Eval:** 81.88% win rate
- **RTF 0.195 trên H200** (5× real-time)
- **~100ms time-to-first-audio** — streaming OK
- **2 arXiv papers** (2024 v1.4 + 2026 S2)

### 🇬🇧 English

fish-speech is a SOTA multilingual TTS system by Fish Audio (legal: 39 AI, INC.). Trained on 10M hours of audio across 80+ languages, with zero-shot voice cloning from 10-30s reference. Dual-AR architecture (Slow 4B + Fast 400M + RVQ), GRPO alignment, 15,000+ inline emotion tags, 7-language documentation.

---

## Part 2 — Corpus firsts at v20

| Signal | fish-speech | Corpus context |
|--------|-------------|----------------|
| **First non-OSI license** | ✅ | Prior: MIT / Apache / ISC / GPL / CC0 all OSI |
| **First anti-distillation clause** | ✅ | Cannot train competing foundation models |
| **First attribution-display clause** | ✅ | "Built with Fish Audio" required |
| **First litigation-termination clause** | ✅ | Anti-patent-troll provision |
| **First research-paper-chain lineage** | ✅ | 7 prior research cited — Pattern #19 4th archetype |
| **First 7-language README** | ✅ | Exceeds graphify CJK-quad (4 langs) |
| **First foundation-model-as-product** | ✅ | 2nd outside-scope after build-your-own-x |
| **First open-core commercial entity** | ✅ | 39 AI, INC. explicit |
| **First SGLang production** | ✅ | LMSYS inference runtime |
| **First TTS benchmark family** | ✅ | Seed-TTS WER + EmergentTTS-Eval |
| **First 10M-hours training explicit** | ✅ | Foundation-model-scale corpus |
| **First natural-language emotion tags** | ✅ | 15,000+ inline control |
| **First GRPO RL alignment for generation** | ✅ | Cross-modality transfer |
| **First 80+ language support** | ✅ | Breadth exceeds prior |
| **First 2-arXiv-publication pattern** | ✅ | 2024 v1.4 + 2026 S2 |

---

## Part 3 — Outside-scope placement

### 🇻🇳 Vì sao outside-scope?

Storm Bear vault focus = agent frameworks, methodology, services, education, bridges, applications. **fish-speech là foundation model (TTS), không phải agent framework.**

Precedent: **build-your-own-x v8** (education aggregator) là wiki outside-scope đầu tiên. **fish-speech v20 = wiki outside-scope thứ 2.**

**Vẫn worth analysis vì:**
- Custom license = first in corpus (pattern observation)
- Research-paper-chain = Pattern #19 4th archetype (NEW)
- 7-language i18n = corpus-largest
- Foundation-model archetype → may expand Storm Bear scope

### 🇬🇧 Why outside-scope?

fish-speech is a TTS foundation model — could be *capability* used by an agent (voice output) but not itself an agent framework. 2nd outside-scope wiki after build-your-own-x v8.

---

## Part 4 — Cài đặt / Installation

### 🇻🇳 3 deployment options

#### Option A: Python pip (cho experimentation)

```bash
# Install from PyPI (check official docs for latest)
pip install fish-speech

# Or clone + install from source
git clone https://github.com/fishaudio/fish-speech.git
cd fish-speech
pip install -e .

# Download model weights from HuggingFace
huggingface-cli download fishaudio/s2-pro
```

#### Option B: Docker (cho production inference)

```bash
# Pull pre-built image
docker pull fishaudio/fish-speech:latest

# Run WebUI
docker run -p 7860:7860 --gpus all fishaudio/fish-speech:latest

# Run inference server (SGLang)
docker run -p 8000:8000 --gpus all fishaudio/fish-speech:latest \
  python -m fish_speech.server --model-path /models/s2-pro
```

#### Option C: HuggingFace Spaces / Inference API

- Use `fishaudio/s2-pro` model card on HuggingFace
- Community Spaces with Gradio demo

### 🇬🇧 Hardware requirements

| Tier | GPU | Expected RTF |
|------|-----|--------------|
| Flagship (official) | NVIDIA H200 | 0.195 |
| High-end consumer | RTX 4090 | ~0.5 |
| Mid-range consumer | RTX 3090 | ~0.8 |
| Low-end / minimal | RTX 3060 | ~1.5 (slower than real-time) |
| CPU only | N/A | not supported at quality |

---

## Part 5 — Sử dụng / Usage examples

### 🇻🇳 Python API example

```python
from fish_speech import TTS

# Load model
tts = TTS.from_pretrained("fishaudio/s2-pro")

# Simple generation
audio = tts.generate(
    text="Xin chào, tôi là trợ lý AI.",
    language="vi",  # Vietnamese (Tier 3)
)
audio.save("output.wav")

# With emotion tags
audio = tts.generate(
    text="[excited] Chúng ta đã thắng! [laugh]",
    language="vi",
)

# Voice cloning
reference_audio = "my_voice_30s.wav"
audio = tts.generate(
    text="[whisper] Đây là giọng được clone.",
    reference_audio=reference_audio,
)
```

### 🇬🇧 CLI example

```bash
# Direct generation
fish-speech generate \
  --text "Hello world with [excited] emotion!" \
  --language en \
  --output hello.wav

# Voice cloning
fish-speech generate \
  --text "This uses a cloned voice" \
  --reference my_voice.wav \
  --output cloned.wav

# Multilingual
fish-speech generate \
  --text "[whisper] Mixing English và tiếng Việt" \
  --output mixed.wav
```

---

## Part 6 — Emotion tags deep dive

### 🇻🇳 15,000+ tags

fish-speech hỗ trợ inline natural-language control:

#### Named emotions

- `[happy]`, `[sad]`, `[angry]`, `[excited]`
- `[whisper]`, `[shout]`, `[laugh]`, `[cry]`
- `[sarcastic]`, `[romantic]`, `[formal]`, `[casual]`

#### Action tags

- `[sigh]`, `[yawn]`, `[cough]`, `[gasp]`
- `[singing]`, `[humming]`

#### Free-form (model infers)

- `[speaking like a pirate]`
- `[as if giving a lecture]`
- `[in a dramatic voice]`

### 🇬🇧 Usage pattern

```
Text: "[whisper] I have a secret. [laugh] Just kidding!"
Output: audio with whispered first phrase, laughter, normal tone for second
```

---

## Part 7 — Voice cloning

### 🇻🇳 Zero-shot cloning

1. **Record reference audio:** 10-30 seconds, clean (no background noise)
2. **Pass to TTS:** no fine-tuning required
3. **Generate in reference voice:** cross-language preserved

### 🇬🇧 Quality factors

- **Clean reference** = better clone (quiet environment, single speaker)
- **10-30s duration** = sweet spot (shorter = underconstrained, longer = no additional benefit)
- **Speaker consistency** = reference should be 1 person, not multi-speaker
- **Speaking style** = neutral reference, fish-speech adds emotion via tags

### Cross-language cloning

English reference → can generate in Chinese with same voice timbre. Works for Tier 1/2 languages; Tier 3 variable.

---

## Part 8 — Pattern #19 research-paper-chain

### 🇻🇳 Lý do lineage quan trọng

Storm Bear corpus track **intellectual lineage** (ai/đâu là nguồn cảm hứng). Pattern #19 có 4 archetypes:

1. **Individual-author** — cite cá nhân cụ thể (Karpathy, John Lam)
2. **Methodology** — build trên idea system (SDD, BMAD)
3. **Community-viral no-lineage** — emerge từ community demand
4. **Research-paper-chain** — cite network of prior research — **fish-speech (NEW v20)**

### fish-speech lineage (7 citations)

| # | Project | Vai trò |
|---|---------|---------|
| 1 | VITS2 | Baseline TTS quality |
| 2 | Bert-VITS2 | Text encoder |
| 3 | GPT VITS | AR approach |
| 4 | MQTTS | RVQ precursor |
| 5 | GPT Fast | Inference optimization |
| 6 | GPT-SoVITS | Voice cloning |
| 7 | Qwen3 | LLM backbone (4B Slow AR) |

### 🇬🇧 Implication

Foundation-model space likely clusters in archetype (4). Storm Bear corpus will document more research-paper-chain lineage as foundation-model wikis added.

---

## Part 9 — Storm Bear relevance (VN operator)

### 🇻🇳 Đánh giá cho Scrum coach

**Relevance level:** 🔴 **LOW** — pattern observation value, not pilot tool.

**Signal points:**
- ❌ **License blocker** — commercial Scrum coaching use cần paid license
- ❌ **Outside-scope** — không phải agent framework
- ⚠️ **VN language Tier 3** — quality chưa verified
- ✅ **Foundation-model capability** — nếu muốn voice output cho agent, có thể xem xét (với research license limitation)
- ❌ **GPU infrastructure** — cần H200 cho production quality
- ❌ **Anti-distillation** — không dùng được để train custom TTS

### When fish-speech IS relevant

- **Research experimentation** (pattern observation + TTS architecture learning)
- **Personal voice projects** (non-commercial)
- **Academic paper writing** (citable architecture)
- **Understanding foundation-model licensing landscape**

### When fish-speech NOT relevant

- Pure commercial Scrum coaching
- Client product with VN voice output
- Building competing TTS foundation model
- Zero-GPU environments

### Scrum ceremony mapping (research-use only)

| Ceremony | Use case |
|----------|----------|
| Sprint demo (research) | Generate sample voice output as POC |
| Retrospective (research) | Explore pattern observation findings |
| Backlog refinement | Learn foundation-model architecture |

---

## Part 10 — 4-week learning roadmap (research-only)

### Week 1: Setup + single-language experiments

- Day 1-2: Install fish-speech (Docker or pip), download s2-pro weights
- Day 3-4: Generate English + Chinese samples, verify quality
- Day 5-7: Try emotion tags, observe output variation

### Week 2: Multilingual + voice cloning

- Day 8-10: Test Vietnamese output quality (Tier 3 assessment)
- Day 11-12: Record reference audio, try zero-shot cloning
- Day 13-14: Cross-language cloning (EN reference → VN output)

### Week 3: Architecture + arXiv paper

- Day 15-17: Read 2026 S2 tech report (arXiv 2603.08823)
- Day 18-19: Study Dual-AR + GRPO architecture
- Day 20-21: Compare with Coqui / XTTS / OpenAI TTS

### Week 4: Decision + alternatives

- Day 22-24: Evaluate commercial alternative needs (research → production path)
- Day 25-26: If commercial use needed → contact 39 AI, INC. for pricing OR switch to Coqui/ElevenLabs
- Day 27-28: Document findings + archive learning

---

## Part 11 — Tradeoffs + limitations

### Strengths

- ✅ **SOTA quality claim** — benchmarks published on standard eval
- ✅ **80+ languages** — broadest in open-source TTS
- ✅ **Voice cloning** — 10-30s sample, zero-shot
- ✅ **Emotion control** — 15,000+ inline tags
- ✅ **Streaming** — ~100ms TTFA, production-viable
- ✅ **Research rigor** — 2 arXiv papers
- ✅ **7-language docs** — broad i18n

### Limitations

- ❌ **Research license** — commercial requires paid tier
- ❌ **GPU required** — H200 for flagship performance
- ❌ **Model size** — 4B Slow + 400M Fast = 4.4B params (large storage)
- ❌ **Tier 3 quality variable** — low-resource languages weaker
- ❌ **Not agent framework** — wrapper needed for agent integration
- ❌ **Vietnamese likely Tier 3** — quality requires testing
- ❌ **Anti-distillation clause** — limits derivative use
- ❌ **Attribution display required** — "Built with Fish Audio"
- ❌ **SGLang ops complexity** — production deployment requires infrastructure expertise

---

## Part 12 — Alternatives for commercial use

### 🇻🇳 Khi fish-speech license blocker

| Alternative | License | Quality | Languages | Commercial OK? |
|-------------|---------|---------|-----------|----------------|
| **Coqui TTS** | MIT | Good | ~30 | ✅ |
| **XTTS-v2** | Coqui-MPL | Good | ~16 | ✅ (check) |
| **Tortoise TTS** | Apache-2.0 | Good | ~3 | ✅ |
| **ElevenLabs API** | Commercial | Excellent | ~30 | ✅ (paid) |
| **OpenAI TTS API** | Commercial | Excellent | ~30 | ✅ (paid) |
| **Azure Neural TTS** | Commercial | Excellent | ~140 | ✅ (paid) |
| **fish-speech** | **Custom non-OSI research** | **SOTA** | **80+** | **❌ research only** |

### Recommendation for VN Scrum coach

- **Research/learning:** fish-speech OK
- **Commercial VN TTS:** ElevenLabs Vietnamese (if available) OR Azure Neural TTS VN OR Coqui TTS with VN training

---

## Part 13 — References + next action

### Wiki pages

- [[(C) index]]
- [[(C) README + 7-language i18n + philosophy cluster summary]]
- [[(C) Dual-AR architecture + GRPO + research-lineage cluster summary]]
- [[(C) Custom LICENSE + 39 AI INC + SGLang production cluster summary]]
- [[(C) Dual-AR + GRPO + RVQ Architecture]]
- [[(C) Multilingual 80+ Language TTS + 7-Lang README]]
- [[(C) 39 AI INC + Research-Paper-Chain Lineage]]
- [[(C) Outside-Scope + Pattern 19 4th Archetype + Storm Bear]]

### Cross-wiki siblings

- Outside-scope precedent: build-your-own-x v8 (education aggregator)
- CN-ecosystem peer: TrendRadar v19 (CN-community)
- Research-lineage contrast: autoresearch v10 (Karpathy individual) vs fish-speech (research-chain)
- i18n predecessor: graphify v16 (CJK-quad)

### Official

- Repo: https://github.com/fishaudio/fish-speech
- Docs: https://speech.fish.audio
- HuggingFace: https://huggingface.co/fishaudio/s2-pro
- Discord: https://discord.gg/Es5qTB9BcN
- arXiv v1.4: https://arxiv.org/abs/2411.01156
- arXiv S2: https://arxiv.org/abs/2603.08823

### 🎯 Suggested next action (Storm Bear)

**Primary:** Still strongly recommend **running graphify on vault** (pending from v16, **4+ sessions overdue**, ~30-60 min + $5-20 Claude API). fish-speech is pattern observation, not pilot tool.

**Secondary:** If curious about TTS, **evaluate Coqui TTS** first (MIT license, commercial OK, lower barrier).

**If fish-speech research-use desired:** Use 4-week roadmap above. Respect license commercial boundary.

---

**Wiki 20/20 — 2nd outside-scope wiki + FIRST non-OSI license + FIRST research-paper-chain lineage (Pattern #19 4th archetype) + 5 new pattern candidates (#31-35) + Pattern #29 refined + Pattern #18 strengthened (CN N=2) + Pattern #8 most rigorous data point. Routine `llm-wiki-routine-v2.md` 2nd execution. Commercial use BLOCKED by custom license.**
