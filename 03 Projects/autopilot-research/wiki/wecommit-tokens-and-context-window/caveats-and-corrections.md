# Caveats and Corrections

## ⭐ The headline: our own pipeline produced the only fabrication

The source fabricated nothing. **This project's extraction stage did.**

Reading video 2's pricing table, the extractor reported the speaker discussing **"Claude 3.5 Opus"** ($10/$50), **"Claude 3 Opus"** ($5/$25) and **"Claude 3.5 Sonnet"** ($2/$10). He says none of those things. A grep of the transcript shows he says **Fable 5**, **Opus 5**, **Sonnet 5** and **Haiku** — and "Claude 3.5 Opus" is not a model that has ever existed.

**The diagnostic detail that makes this worth recording:** the extractor wrote the error into its own `asr_garble` field — the field whose entire purpose is to catch mis-hearings — in the *wrong direction*:

```
Fable 5  →  Claude 3.5 Opus     ← the CORRECT name, "corrected" into a nonexistent one
Oppus    →  Opus (Claude 3)     ← correct model, mislabelled as a legacy version
Sonet    →  Sonnet (Claude 3.5) ← correct model, mislabelled as a legacy version
```

It treated **current model names as ASR corruption** and "restored" them to the names in its training prior. The safeguard became the vector.

**How it was caught — three independent stages, in order:**

1. A **refute-first verifier** noticed the model names don't exist in first-party docs and said so explicitly: *"the model nomenclature is fabricated by the extractor, not stated in the videos."*
2. The **main loop grepped the transcript** and confirmed the actual names.
3. **First-party pricing** confirmed the *numbers* were right all along, so the source's claim survives intact.

**The lesson, for this vault's method:** an extractor with a stale prior does not merely miss things — it **overwrites correct data with confident wrong data**, and it will do so inside the field designed to prevent that. Extraction cannot be trusted on any fast-moving proper noun (model names, versions, prices, product names). Grep the transcript. This is also live evidence for the source's own thesis that a generator must never be its own verifier ([[banking-principle-for-agent-correctness]]).

## Verifier over-reaches (6 verdicts overridden)

The verification stage was not uniformly reliable in the other direction either. It made **five excellent catches** (the fabrication above, plus two genuinely valuable precision fixes) and **six over-reaches** — including two verdicts asserted with **no URL** in a run that required one, and one date-check it never performed. Every override is itemised with reasoning in [[claims-scorecard]] § *The six main-loop overrides*.

The pattern worth remembering: the verifier was strongest when checking a **fact against a document**, and weakest when **arguing against a judgement** ("never let AI self-check", "AI doesn't know your criteria") — where it refuted the theory while conceding the practice.

## ASR garble map — the transcripts are not quotable verbatim

All four tracks are **automatic captions only** (no human-authored subtitles exist for any of them). English technical terms are consistently mangled. Do not quote these transcripts as the speaker's exact words without checking the audio.

**Across all four videos:**

| ASR output | Actual term |
|---|---|
| `clot`, `Clot` | **Claude** |
| `prom` | **prompt** |
| `Tocen` | **token** |
| `Elm` | **LLM** |
| `contex Windows` | **context window** |
| `Asient`, `Asian`, `aent` | **agent** |
| `aentic AI` | **agentic AI** (20+ occurrences in video 3) |
| `code X` | **Codex** |
| `Oppus` | **Opus** |
| `Sonet` | **Sonnet** |
| `hai cu` | **Haiku** |

**Video-specific:**

| ASR output | Actual term |
|---|---|
| `attention is own unit` | *Attention Is All You Need* (2017) |
| `mem GPT` | **MemGPT** |
| `Open Claw` | **OpenClaw** |
| `Herm Agent` | **Hermes Agent** |
| `nút`, `Nucleus` | **NotebookLM** |
| `postb`, `postque` | **PostgreSQL** |
| `VDQ`, `Ví IQ` | **VidIQ** |
| `té` | `tách` (to split) |
| `khoá` | `quá` |
| `sao nhão` | `xao nhãng` (distraction) |
| `thép` | `phép` (as in `phép tính`, calculation) |
| `giải thuật` | algorithm |

### ⚠️ The `cache` trap

He uses the Vietnamese word **`cách`** as a transliteration of English **"cache"**, and the ASR renders it inconsistently as `cách` / `kch` / `CCH` / `cách`. Since `cách` is also an ordinary Vietnamese word meaning "way/method", **the caching passage reads as gibberish unless you know this substitution**. It is the single most confusing stretch of the anchor transcript, and it is why the cache write/read verdict needed a manual override ([[claims-scorecard]] override #1).

## Limits of this ingest

- **No video frames were examined.** Every on-screen artifact — the tokenizer UI, the pricing page, the dashboards, the SQL demo — is known only through narration. Which tokenizer he used is therefore **unknowable from this ingest**.
- **`count_tokens` was not runnable** (no `ant` CLI, no `ANTHROPIC_API_KEY`), so the headline Vietnamese 7:1 ratio stays **unverified** rather than confirmed.
- **Video 2 was initially under-extracted** — 15 claims for 59:26, versus 28 for the 26:58 anchor. The completeness critic flagged it and the missing architecture section was recovered by direct transcript reading ([[agent-org-chart-architecture]]). Had the critic not run, the most substantial content in the longest video would have been silently dropped.
- **His demos are deliberately partial.** He states twice that sensitive agents and data were removed before filming. Honest, and it means the system is described rather than audited.
- **Commercial context:** he sells a "Coaching Agentic AI (no-code)" program, and each video closes with a soft pitch. The method stands on its own merits; the incentive is on the record.

## What to un-learn from this bundle

1. **Vietnamese is not charged at a higher rate.** It costs more because it emits more tokens. Volume, not price. → [[vietnamese-token-inflation]]
2. **Caching is a ~90% discount, not a surcharge.** He quotes only the 1.25×/2× write premium and never the 0.1× read. → [[prompt-caching-as-taught]]
3. **"AI has no memory" describes the model, not the platform.** Caching, compaction, context editing and memory stores all exist. → [[statelessness-and-context-cost]]
4. **Sonnet 5 at $2/$10 expires 2026-08-31.** Standard is $3/$15. → [[claude-pricing-ladder]]
5. **Anthropic memory is four surfaces, not just Projects.** → [[agent-forgetfulness-and-vendor-memory]]
6. **The banking principle has textbook names** — atomicity, compensating transactions, reversible migrations. Its novelty is the *gate-placement rule*, not the principle. → [[banking-principle-for-agent-correctness]]

## Cross-links

- [[claims-scorecard]] · [[source-provenance]] · [[overview]]
