# (C) Multilingual 80+ Language TTS + 7-Lang README

> **Type:** Entity — multilingual breadth + i18n documentation
> **Parent:** [[(C) index]]
> **Sources:** README language list + 7-language README files + speech.fish.audio
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

fish-speech supports **80+ languages for TTS generation** with tiered quality (Tier 1: CN/EN/JP flagship; Tier 2: 7 strong; Tier 3: 70+ additional). Documentation shipped in **7 languages** (EN + 简体中文 + Português + 日本語 + 한국어 + العربية + Español) — **largest i18n surface in Storm Bear corpus** (exceeds graphify CJK-quad and TrendRadar CN+EN bilingual). No phoneme requirement — text-conditioned only.

## 2. Key claims

1. 80+ language TTS support (claim; not all independently verified)
2. 7-language README — corpus-largest i18n documentation
3. No phoneme requirement — text-conditioned zero-shot multilingual
4. Tiered language quality reflects training-corpus distribution
5. Documentation i18n correlates with product multilingual scope

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| 80+ languages | speech.fish.audio | Medium (corpus-breadth, quality varies) |
| 7-language README | github.com/fishaudio/fish-speech repo | High |
| No phoneme requirement | README feature list | High |
| Tier 1/2/3 quality | speech.fish.audio | Medium (inferred from training emphasis) |

## 4. Language tier structure

### Tier 1 — flagship quality

**3 languages:** Chinese (Mandarin), English, Japanese

- Most training data
- Best benchmark scores (Seed-TTS Eval 0.54% CN WER, 0.99% EN WER)
- Voice cloning highest-quality
- Emotional tag fidelity best

### Tier 2 — strong quality

**7 languages:** Korean, Spanish, Portuguese, Arabic, Russian, French, German

- Substantial training data
- Production-viable quality
- Voice cloning viable
- Emotional tags functional

### Tier 3 — 70+ additional languages

- "Global coverage of 70+ additional languages"
- Quality variable — documentation honest about coverage vs quality tradeoff
- Low-resource languages likely weaker

### Corpus distribution comparison

| Wiki | Language breadth |
|------|-----------------|
| Most corpus frameworks | EN-only |
| deer-flow v9 | CN+EN |
| graphify v16 | CJK-quad (en+ja+ko+zh) |
| TrendRadar v19 | CN+EN |
| agency-agents v18 | EN + CONTRIBUTING_zh-CN.md |
| **fish-speech v20** | **80+ language support** (product) + **7-language docs** (operational) |

## 5. 7-language README presence

### Language list

| # | Language | File |
|---|----------|------|
| 1 | English | README.md (primary) |
| 2 | 简体中文 Chinese | README.zh-CN.md |
| 3 | Português | README.pt-BR.md |
| 4 | 日本語 Japanese | README.ja.md |
| 5 | 한국어 Korean | README.ko.md |
| 6 | العربية Arabic | README.ar.md |
| 7 | Español Spanish | README.es.md |

### Pattern in corpus

**Corpus-largest i18n.** Prior corpus high-water-marks:
- graphify v16: CJK-quad (4 langs)
- TrendRadar v19: bilingual CN+EN (2 langs)
- multica/deer-flow: zh-CN translations (2 langs each)

**Jump from 4 to 7 languages** = 75% increase in i18n surface.

### Rationale for 7-language docs

Product claims 80+ language support operationally. Documentation i18n should **match product operational scope**. 7 languages cover majority of Tier 1 + Tier 2 user base:
- 3 flagship (CN/EN/JP) = majority adoption
- 4 Tier 2 (PT/KR/AR/ES) = specific regional markets

**Not covered:** RU, FR, DE (Tier 2 but weaker documentation). Suggests i18n follows community-demand, not alphabetic completeness.

## 6. No phoneme requirement (novel)

### Traditional TTS pipeline

```
Text → Phonemizer (language-specific) → G2P → Acoustic model → Audio
```

Phonemizer = grapheme-to-phoneme conversion. Language-specific, rule-based, often inaccurate for:
- Proper nouns
- Code-switched text
- Homographs
- Low-resource languages

### fish-speech pipeline

```
Text → Slow AR (handles "reading") → Fast AR → RVQ → Audio
```

**No phoneme step.** Semantic model learns text→sound directly via corpus scale.

### Implications

- **Proper nouns:** handled in-context (no phonemizer mispronunciation)
- **Code-switching:** fluent mid-sentence language mixing
- **Low-resource:** language ability scales with corpus presence, not phoneme-table existence
- **Emotional tags:** integrated into text representation

### Tradeoff

Requires **massive corpus** (10M hours) for text→audio learning without phoneme scaffold. Traditional TTS works with 10-100 hours per language; fish-speech needs foundation-scale corpus to match.

## 7. Emotion tag support across languages

### Inline tag examples

```
English: [whisper] this is a secret
Chinese: [whisper] 这是一个秘密
Japanese: [whisper] これは秘密です
Arabic: [whisper] هذا سر
```

Same tag syntax across 80+ languages — unified control surface.

### 15,000+ tags

- Named emotions: happy, sad, angry, excited, whispered, shouting
- Contextual tags: laughing, crying, yawning, singing
- Style tags: sarcastic, romantic, formal, casual
- Free-form text: model interprets novel tags from context

## 8. Multi-speaker + voice cloning

### Zero-shot voice cloning

- **Reference audio:** 10-30 seconds
- **No fine-tuning required**
- **Works cross-language** — English voice can generate Japanese output preserving timbre

### Multi-speaker from single reference

- Single audio with multiple speakers → model separates
- Can generate dialogue where different speakers maintain distinct voices

### Implications for multilingual product

- **Dubbing pipeline:** clone original speaker → generate target-language output with original voice
- **Accessibility:** personalized TTS voices for visually-impaired users
- **Content localization:** podcast/audiobook multi-language production

## 9. Quality tradeoffs by language tier

### Tier 1 flagship (CN/EN/JP)

- Near-human quality in formal contexts
- Good emotional range
- Strong voice cloning

### Tier 2 strong (KR/ES/PT/AR/RU/FR/DE)

- Production-viable quality
- Adequate emotional range
- Voice cloning works, quality lower than Tier 1

### Tier 3 (70+ additional)

- Variable quality
- Low-resource languages (e.g., African languages, Southeast Asian minority languages) likely weakest
- Marketing-style framing — operationally may not be production-ready for all

### Honest framing

fish-speech honestly tiers languages rather than claiming uniform "80+ language support." Contrasts with some competitors (Google TTS "100+ languages" — but many minimal quality).

## 10. Edges + failure modes

### Multilingual edges

- **Mixed scripts** (Japanese text with English loanwords + katakana) — generally handled
- **Tonal languages** (Mandarin, Vietnamese, Thai) — tone handling via corpus learning
- **Cursive scripts** (Arabic, Hebrew, Urdu) — tokenization may vary
- **Right-to-left** (Arabic, Hebrew) — text direction handled at Slow AR level
- **Code-switching** (English + CJK in tech context) — good; better than phoneme-based TTS

### Known failure modes

- **Low-resource language accents** in Tier 3 — variable
- **Rare dialects** — may approximate with standard variety
- **Nonsense text** — may still generate plausible-sounding output (hallucination)
- **Very long text** without paragraph breaks — may lose coherence after few minutes

## 11. Comparison with competitors

### ElevenLabs (closed-source)

- **Languages:** ~30 (with quality focus)
- **Voice cloning:** Pro tier only, unlimited samples
- **Emotion control:** stability + style sliders
- **License:** commercial SaaS

### OpenAI TTS (closed-source)

- **Languages:** dozens (GPT-4o family)
- **Voice cloning:** not offered
- **Emotion control:** limited
- **License:** API commercial

### fish-speech (open-source research license)

- **Languages:** 80+ (with honest tier distribution)
- **Voice cloning:** 10-30s reference, no fine-tune
- **Emotion control:** 15,000+ inline tags
- **License:** research-only free; commercial paid

## 12. VN relevance

### Vietnamese language status

Vietnamese likely **Tier 3** (among 70+ additional). Specific quality claims not published. Practical implication:
- Research/experimentation: viable
- Production VN TTS: quality assessment needed via own testing

### VN dubbing/localization potential

- EN→VN dubbing: possible but Tier-3 VN output may not match ElevenLabs VN quality
- VN voice cloning: depends on VN corpus presence in training data
- **Recommendation:** test VN output quality directly before production commitment

## 13. Related concepts

- [[(C) Dual-AR + GRPO + RVQ Architecture]] — architecture enabling multilingual scale
- [[(C) 39 AI INC + Research-Paper-Chain Lineage]] — lineage influence on multilingual capability
- [[(C) Outside-Scope + Pattern 19 4th Archetype + Storm Bear]] — documentation-i18n pattern
- Pattern #6 (Localization Emergence) — fish-speech is extreme of corpus i18n trend
- Parent: [[(C) index]]

## References

- README.md language list + 7 README translations
- speech.fish.audio language coverage
- arXiv papers for training corpus description

---

**80+ language TTS support (Tier 1 CN/EN/JP flagship; Tier 2 7 strong; Tier 3 70+ variable). 7-language README = corpus-largest i18n (EN + 简体中文 + PT + JP + KR + AR + ES). No phoneme requirement (text-conditioned via 10M hours training). Zero-shot cross-language voice cloning from 10-30s sample. Corpus high-water-mark for i18n, +75% vs graphify CJK-quad prior.**
