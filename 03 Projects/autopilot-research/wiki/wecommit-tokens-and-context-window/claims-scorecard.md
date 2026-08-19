# Claims Scorecard

> **Method.** 72 claims extracted across 4 videos (67 load-bearing) → 7 refute-first verifier clusters with live first-party lookups + 1 corpus-collision grep + 1 completeness critic (Workflow `wf_2bd9115e-d48`, 13 agents, 0 errors / 0 empty / 0 skipped, ~968K tokens, 177 tool calls, 7.6 min) → **Opus main-loop adjudication**, which re-read the raw transcripts and **overrode six verdicts**.

## Reconciliation

| Stage | Count |
|---|---|
| Raw verdicts returned by verifiers | **48** |
| − reclassified as **extraction artifacts** (our pipeline's error, not the source's) | −5 |
| **= source-claim verdicts adjudicated** | **43** |
| of which **overridden by the main loop** | 6 |

## Final distribution (43 source claims)

| Verdict | n | Share |
|---|---|---|
| **CONFIRMED** | 25 | 58% |
| **CORRECT-BUT-INCOMPLETE / IMPRECISE** | 13 | 30% |
| **CORRECT-AT-PUBLICATION, NOW STALE** | 2 | 5% |
| **UNVERIFIED** (could not be settled in this environment) | 2 | 5% |
| **FALSE** | 1 | 2% |
| **FABRICATED** | **0** | — |

**Profile: a technically-sound practitioner explainer.** The failure mode is *imprecision and omission*, not error — and the single FALSE is peripheral to the topic. The pricing, caching arithmetic and tokenization mechanics — the parts a reader would act on — hold up.

> ⭐ **The most important line in this scorecard: the only fabrication in this whole compilation was produced by our own extraction pipeline, not by the source.** See [[caveats-and-corrections]].

## The six main-loop overrides

Each was settled by re-reading the raw transcript, checking a publication date, or consulting first-party pricing — not by trusting the verifier.

| # | Claim | Verifier said | Adjudicated | Why |
|---|---|---|---|---|
| 1 | Cache write $6.25 (5-min) / $10 (1-hour) | MISLEADING — "quoted write prices where read prices apply" | **CONFIRMED** | At [20:22] he says verbatim *"cách **phần ghi** này"* — "this cache **write** part". He labelled the column correctly, and $6.25/$10 are exactly 1.25×/2× the $5 base. **The verifier misread him.** |
| 2 | Cache expiry forces a costly full re-read | MISLEADING — "it's a 1.25×/2× write, not full cost" | **CONFIRMED** | A re-write at 1.25×–2× is *more* than an uncached read. His framing understates the penalty rather than overstating it. Pedantic objection. |
| 3 | Never let AI self-check its own output | **FALSE** — cites Constitutional AI | **CORRECT-BUT-INCOMPLETE** | Verifier cited **no URL**; its own correction conceded his point. And **this run proves him right** — the extractor's fabricated model names were caught by an *independent* stage, never by self-check. Full argument in [[banking-principle-for-agent-correctness]]. |
| 4 | AI doesn't inherently know pass/fail criteria | MISLEADING — "LLMs are fine-tuned to follow criteria" | **CONFIRMED in practice** | No URL. The verifier's own correction restates his advice ("always specify criteria explicitly"). Refuting the theory while conceding the practice is not a refutation. |
| 5 | ChatGPT memory has no timestamp metadata | MISLEADING — "Dreaming V3 added timestamps 2026-06-04" | **CORRECT AT PUBLICATION, NOW STALE** | **The video is 2026-04-22 — six weeks *before* Dreaming V3.** The verifier hedged "if the video was made after June 4" and never checked. The completeness critic independently caught the same miss. |
| 6 | Model pricing figures | 2 FALSE + 3 MISLEADING on model names | **Source CONFIRMED; extraction at fault** | He says **Fable 5 / Opus 5 / Sonnet 5 / Haiku**. "Claude 3 Opus" and "Claude 3.5 Opus" were invented by our extractor. Verified by grep + first-party pricing. |

## CONFIRMED — the load-bearing wins

| Claim | Evidence |
|---|---|
| Fable 5 = $10 / $50 per 1M | First-party pricing: $10.00 / $50.00 — **exact** |
| Opus 5 = $5 / $25 per 1M | $5.00 / $25.00 — **exact** |
| Haiku = $1 per 1M input | $1.00 — **exact** |
| **Output costs ~5× input** | Holds at *every* tier: $10→$50, $5→$25, $2→$10, $1→$5 |
| Cache write = 1.25× (5-min TTL), 2× (1-hour TTL) | Confirmed; his $6.25/$10 arithmetic is exact |
| Cache reuse costs less than full price | Reads ≈ 0.1× base input (he never states the number — see below) |
| Model is stateless; whole history is re-sent and re-billed each turn | Correct, and the right teaching anchor |
| Vietnamese produces more tokens than English for equivalent meaning | Confirmed; subword vocabulary frequency + UTF-8 multi-byte diacritics |
| Tokenizer vocabulary built by frequent-adjacent-pair merging, "compression algorithm from 1994" | Accurate description of **byte-pair encoding** (Gage, 1994) — though he never names it |
| Leading space changes tokenization (` strawberry` vs `strawberry`) | Real, well-documented BPE behaviour |
| Strawberry R-count failure is a tokenization artifact, **and newer models fixed it** | Correct — and more honest than most explainers |
| Transformer (2017 *Attention Is All You Need*) has no native memory component | Correct |
| CoALA's four memory types; Generative Agents' **25** village agents; MemGPT's RAM/disk virtual memory | All three correctly attributed and described |
| Lost-in-the-middle is real and not solved by a bigger window | Correct |
| Accuracy and cost-saving move together, not against each other | Independently matches the Anthropic Platform-team "context engineering is intelligence-positive" thesis |
| Deterministic work must be delegated to code, not predicted by the model | Correct; the mechanism behind programmatic tool calling |
| Reversibility should decide where the human gate goes | Sound; standard names are transaction atomicity / compensating transactions |

## CORRECT-BUT-INCOMPLETE / IMPRECISE — the 13

The highest-value ones:

1. **"Vietnamese costs more money"** → costs more **volume**; the per-token *rate* is identical for every language. The phrasing invites exactly the wrong inference for his audience. → [[vietnamese-token-inflation]]
2. **He never states the ~90% cache-read discount** (0.1× input). Quoting only the 1.25×/2× *write* premium makes caching look like a surcharge instead of the biggest lever available. → [[prompt-caching-as-taught]]
3. **"AI has no memory" is true of the model, not the platform** — omits caching, compaction, context editing, and memory tools/stores. → [[statelessness-and-context-cost]]
4. **VN inflation mechanism** attributed to "not trained on Vietnamese" — conflates tokenizer-vocabulary construction with model training, and omits UTF-8/diacritics.
5. **Anthropic's memory = "Projects"** — one of four surfaces; the GA file-based memory tool already existed when he filmed. → [[agent-forgetfulness-and-vendor-memory]]
6. **"Pricing varies 100×"** — within Claude the input spread is 10×; 100× needs the cheapest hosted open models. Loose, and inconsistent with his own precise table.
7. **The banking principle omits its standard names** (atomicity / compensating transactions / reversible migrations), which makes a 1983-vintage principle sound like a personal discovery.
8. **Lost-in-the-middle *cause*** ("models trained on human documents that front/back-load importance") — plausible, contested, stated too confidently.
9. **Prompt-caching caveats absent:** byte-exact prefix matching, the ~1024-token minimum cacheable prefix, and the timestamp-in-system-prompt cache killer.

## CORRECT AT PUBLICATION, NOW STALE — the 2

| Claim | Was right | Now |
|---|---|---|
| **Sonnet 5 = $2 / $10** (video 2026-08-02) | Yes — introductory pricing | ⏰ **Intro pricing ends 2026-08-31**; standard is **$3 / $15**. Applying his figure after that date understates cost by 50%. **12 days from this compile.** |
| **ChatGPT memory has no timestamps** (video 2026-04-22) | Yes | Superseded by Dreaming V3 on 2026-06-04 |

## UNVERIFIED — the 2 (stated as boundaries, not filled in)

1. **`chuyên nghiệp` = 7 tokens vs `professional` = 1 token.** Settling it requires `POST /v1/messages/count_tokens`, which **was not runnable here** — no `ant` CLI, no `ANTHROPIC_API_KEY`. The ratio is plausible (published Vietnamese-vs-English ratios sit in the 2.5×–7× band) but plausible is not verified. Exact command in [[vietnamese-token-inflation]].
2. **Which tokenizer produced his on-screen counts.** He never names one in any of the four videos, and no frames were analysed. Unreachable from an audio transcript. → [[source-provenance]] §2–3.

## FALSE — the 1

**NotebookLM free tier = "50 notebooks/month"** ([`4PKT7vFo334`] [24:24]). Google's own support documentation gives **100 notebooks per user account, with no monthly renewal**. Flagged by the verifier against Google support docs plus two secondary sources; **not independently re-checked in the main loop**, and peripheral to this topic's subject matter. Recorded for completeness, not load-bearing.

## Cross-links

- [[caveats-and-corrections]] — the ASR garble map and the extraction-error record
- [[source-provenance]] — what could and could not be established about the sources
- [[overview]] · [[hireui-relevance]]
