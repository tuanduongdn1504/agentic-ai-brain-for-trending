# Tokenization Mechanics (as taught)

> **Source:** anchor [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) [00:28]–[15:19]. Verdicts in [[claims-scorecard]].

## The thesis he opens with

People chase prompt tips and never learn the unit the model actually operates on. His framing at [00:28]: **token is the smallest unit AI works on, and it drives both what you pay and the quality of what you get back** — yet nobody studies it.

His authority claim at [01:49]: ~15 years optimising databases for banks and corporations taught him that **the way to optimise any system is to understand its smallest unit of operation.** Tokens are that unit for LLMs. It is a genuinely good framing and it is the spine of the whole bundle.

## What a token is

- Text is converted to token **numbers** before the model sees it; the model returns token numbers that are converted back to text ([02:45]).
- **The character-to-token ratio is not 1:1** and is not stable ([03:40]). He demos 10 characters → 6 tokens.
- Tokens come from a fixed **vocabulary** ("bộ từ điển") built in advance ([15:19]).

## How the vocabulary is built — he describes BPE without naming it

At [08:54] he describes the algorithm as *"a data-compression algorithm from 1994 that finds the most frequently occurring adjacent pairs and replaces them"*, and at [09:51] as *scanning a large text corpus for which substrings most often occur together and adding those to the dictionary.*

That is an accurate description of **byte-pair encoding**, originally published by Philip Gage in 1994 as a compression technique and later adapted for NLP subword tokenization. The 1994 date is right.

> ⚠️ **He never says "BPE", "byte-pair encoding", or "tokenizer" in any of the four videos** — a grep across all 36,373 words returns zero hits for any tokenizer name. The label "BPE" in this article is *ours*, applied to his description. See [[source-provenance]] §2 for why that distinction matters.

## The quirks he demos

These are the examples he puts on screen ([05:05]–[05:33]):

| Input | Tokens (as shown) |
|---|---|
| `100` | 1 |
| `1000` | 2 |
| `10000` | 2 |
| `strawberry` (no leading space) | 3 |
| ` strawberry` (leading space) | 1 |

His point is the right one: these look arbitrary but fall out of vocabulary construction — frequent strings earned their own entry, rarer ones get split. **The leading-space effect is real and well documented** (BPE vocabularies contain space-prefixed word forms, so `" word"` is often a single token while `"word"` splits).

> ⚠️ **Which tokenizer produced these exact counts is unknown.** He never names the tool and no frames were analysed. The *phenomena* are real; the *specific counts* are tokenizer-dependent and are not reproducible from this ingest. Treat the table as illustrative, not as a citable measurement.

## The strawberry / count-the-Rs explanation

This is the strongest passage in the anchor, and notably more honest than most explainers ([13:28]–[14:53]):

1. **The mechanism:** the model cannot count the 3 Rs in "strawberry" because it never sees characters — it sees token ids. Split as `str` + `aw` + `berry`, the Rs are buried inside separate chunks (1 in `str`, 2 in `berry`).
2. **He explicitly says newer models fixed this** — *"các mô hình sau… các hãng AI họ đã xử lý được rồi"* (later models, the AI companies have handled it). Most explainers still present strawberry as a live failure; he does not.
3. **He lists real mitigations:** split the string into separate characters so no two letters share a token; insert separators; make it reason before answering; or — his preferred answer — **run an external script that counts the characters**, because "one simple line of code can count it, but the AI is not running a program, so it can be wrong."

That last mitigation is the seed of [[four-rules-for-token-discipline]] rule 1, and it is the correct engineering answer.

## Why this matters downstream

Everything else in the bundle is a consequence of this section:

- Vocabulary is built mostly from English → [[vietnamese-token-inflation]]
- Everything in the chat becomes tokens, and the model has no memory → [[statelessness-and-context-cost]]
- The model manipulates token ids, not numbers → never let it do arithmetic ([[four-rules-for-token-discipline]])

## Cross-links

- [[mosh-ai-powered-apps/tokens-and-cost]] — the corpus' other tokenization treatment (English-language course; carries the **never-tiktoken-for-Claude** rule)
- [[vietnamese-token-inflation]] · [[statelessness-and-context-cost]] · [[claims-scorecard]]
