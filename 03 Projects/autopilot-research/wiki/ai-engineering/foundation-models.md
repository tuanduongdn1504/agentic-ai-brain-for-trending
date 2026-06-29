# Foundation Models, Tokens, Sampling & Hallucinations (Ch. 1–2)

## Source

Video sections "What Is a Foundation Model?" → "Why Hallucinations Happen" + Huyen *AI Engineering* Ch.1–2 (verified chapter summary). See [[overview]], [[source-provenance]].

## What a foundation model is

- A **general-purpose model adaptable to many tasks** (think ChatGPT: research, Q&A, drafting). Examples: GPT, Claude, Gemini, Llama.
- **Multimodal** = can take in and emit text, images, audio, video. "When you hear multimodal, it just means the model can use images/audio/text and output the same."
- **Adaptable** in two main ways: **inject your own context** (RAG — see [[rag]]) or **fine-tune** to change behavior (see [[finetuning-dataset-inference]]).

## The lineage (how we got here)

`Language models` (learn patterns from text) → `Large language models` (same, but scaled — data, compute, parameters; e.g. 7B vs 120B params → more nuance) → `Foundation models` (general-purpose, often multimodal) → `AI applications` (what you build on top by adapting a model to a real use case).

> **scale + post-training + better input interfaces** = what makes modern AI applications possible.

## Tokens & self-supervision

- **Token** = the unit a model reads and predicts — roughly a word or word-fragment ("AI", "engineering", "turns" are tokens). Tokenization is how the model "understands" your input.
- **Self-supervision** = the model learns by **predicting the next token** from massive *unlabeled* text. No human labels needed for pre-training — that's why these models could scale.
- Mental model the video hammers: **a foundation model is a next-token prediction machine.** It looks smart but it is **probabilistic, not deterministic.**

## Sampling — why outputs change every run

The model produces a **probability distribution over the next token** and *samples* from it. Same prompt → different valid answers. Key knobs (Ch.2 "Sampling Strategies"):

- **Temperature** — controls randomness. **Near 0 = factual/deterministic-ish; near 1 = creative.** (Can exceed 1 for more chaos.)
- **Top-p (nucleus)** — restrict choices to the smallest set of tokens whose probability mass ≥ p.
- **Top-k** — restrict to the k most-likely tokens.
- **Presence / frequency penalties** — reduce repetition.
- **System load / non-determinism** — even temp-0 isn't perfectly reproducible (batching, hardware). (Echoes the temp-0-≠-determinism caveat in [[../prompt-evaluation/_index]].)

> Different models (Claude vs GPT vs Gemini) give different answers because they were **trained differently** — different data + architecture. This is *why* "Claude is better at coding, GPT at X" debates exist: it's training, not magic. Huyen: build "your workflows around their probabilistic nature."

Beyond sampling, Ch.2 also covers **structured outputs** (constraining the model to valid JSON/schema — load-bearing for production; see [[prompt-engineering-and-guardrails]]) and **test-time compute** (spend more inference-time reasoning to improve answers — the basis of "thinking" modes).

## Hallucinations — why they happen

A **hallucination** is when the model **confidently makes something up that isn't true** (the video's example: "Who won the 2024 Mars Cup?" → a fluent, fully-invented answer). It happens more than people admit because models are *trained to always produce an answer.* Causes:

1. **Knowledge gap** — anything after the training cutoff is unknown; without web/tool access the model guesses instead of saying "I don't know."
2. **Pattern completion / probabilistic generation** — the most-probable next token is **not always the true one**; the model fills gaps with plausible-sounding text.
3. **Weak grounding** — with poor/no context, the answer drifts. Sampling itself ("the probabilistic nature") "enables creative tasks but introduces inconsistency and hallucinations" (Huyen, Ch.2).

**Mitigations** (developed across later chapters): better **context** (RAG → [[rag]]), **evaluation** to catch it (→ [[evaluation]]), and **guardrails** including "if you don't know, say you don't know" instructions (→ [[prompt-engineering-and-guardrails]]).

## Also in Ch.1–2 (often glossed by the video)

- **Foundation-model use cases** (Ch.1): coding, image/video, writing, education, conversational bots, information aggregation, data organization, workflow automation.
- **Planning AI applications** (Ch.1): use-case evaluation, **setting expectations**, milestone planning, maintenance.
- **The AI engineering stack** (Ch.1): three layers of the stack; AI-engineering-vs-ML-engineering; AI-engineering-vs-full-stack-engineering.
- **Training data** (Ch.2): multilingual + domain-specific models; data curation matters even when you only *consume* models (it explains their blind spots).
- **Post-training** (Ch.2): supervised fine-tuning + preference fine-tuning ("human preference is diverse and impossible to capture in a single mathematical formula").

## Key Takeaways

- A foundation model is a **multimodal, general-purpose, adaptable next-token predictor** — probabilistic, not deterministic.
- **Sampling knobs** (temperature/top-p/top-k/penalties) explain why outputs vary; tune temperature low for facts, high for creativity.
- **Hallucinations** come from knowledge gaps, probabilistic pattern-completion, and weak grounding — and are reduced by context + evaluation + guardrails, not eliminated.
- If a task is deterministic, **use code, not a model** — reserve the probabilistic tool for genuinely open-ended work.

## Cross-links

- [[evaluation]] · [[rag]] · [[prompt-engineering-and-guardrails]]
- [[../prompt-evaluation/_index]] (sampling/temperature determinism caveat) · [[../claude-api-cost-optimization/_index]] (structured outputs + test-time compute = cost)
