# RAG, vector stores, and context limits — the reality checks

## Source

- Deep-dive dimension `video-claims-audit` of workflow `wf_4356f040-686` (2 adversarial verifiers) + main-loop claude-api ground truth for Claude model facts.

## Top-k RAG — the video is right

- "RAG normally uses a top-k search method" — ✅ CONFIRMED as the industry default: embed → similarity (cosine/dot/L2) → top-k nearest neighbors, ANN indexes at scale. Typical k = 3–5; diminishing returns past ~10.
- The video's lay explanation ("AI turns every word into a list of numbers, then does similarity search") conflates **tokenization** (subword units) with **embeddings** (dense vectors) — acceptable pedagogy, technically two different pipeline stages.
- Generative Agents' richer score (recency × importance × relevance, [[generative-agents-reflection]]) is the upgrade worth knowing for *interaction* memory, where pure semantic similarity misses time and salience.

## Vector stores — one substrate among several

Verified production substrate census (details in [[how-chatgpt-memory-works]] / [[how-claude-memory-works]] / [[memgpt-letta-sleep-time]]):

| System | Semantic-memory substrate | Retrieval |
|---|---|---|
| ChatGPT memory | Pre-computed summary dossier | **None — injected wholesale** |
| Claude (all 4 surfaces) | Files / mounted text docs / timed summary | File reads; model-directed |
| Letta core memory | In-context memory blocks | Always loaded |
| Letta archival memory | **Vector-backed database** | Semantic search ✅ |
| Generative Agents | Memory stream + embeddings | recency×importance×relevance |
| Custom product memory (the video's e-commerce case) | Often pgvector/Pinecone/Chroma | top-k RAG ✅ |

- Verdict on "semantic and episodic memory are saved in vector stores": **REFUTED as a universal, valid as a builder pattern** — correct for big heterogeneous corpora, wrong for the assistant-memory systems the video names.

## Context windows — 2026 ground truth

- Authoritative (Anthropic docs / claude-api reference, 2026-06 cache): **Claude Fable 5, Opus 4.8/4.7/4.6, Sonnet 5, Sonnet 4.6 = 1M context** (128K max output); **Haiku 4.5 = 200K**. Gemini flagship models are 1M-class. The broader ecosystem (Llama, Mistral, most open models) sits at **128K–256K**.
- So the video's "context window for most LLMs is roughly 1 million tokens": **overstated as an ecosystem claim, roughly right for the frontier tier** — 1M is now standard on frontier Claude/Gemini, not on "most LLMs."
- ⚠️ Several workflow agents "refuted" the 1M claim using stale third-party blogs asserting "Claude caps at 200K" — themselves wrong against Anthropic's own docs. Logged in [[source-provenance]]; lesson: model-capability claims need vendor-primary sources, third-party comparison blogs rot in months.

## "Overloading context makes models slower and less accurate" — strongly evidence-backed

- **Lost in the Middle** — Liu et al. 2023, [arXiv:2307.03172](https://arxiv.org/abs/2307.03172): accuracy drops >30% when relevant info sits mid-context, across model families; U-shaped position curve.
- **Chroma "context rot" (2025)**: 18 models tested; every one degrades with length; practical **safe budgets ~150K–400K even on 1M-window models** (advertised ≠ usable).
- **NoLiMa (ICML 2025)**: with lexical-overlap cues removed, 11 of 13 models fall below 50% of their short-context baseline **by 32K tokens**.
- This is the same context-rot thread as [[../claude-code-memory-systems/_index]]'s 200-line rule and [[../claude-api-cost-optimization/_index]]'s context engineering — the video asserts it without sources; the sources exist and are stronger than the claim.

## Key Takeaways

- The efficiency argument for selective memory is **better than the video makes it**: not just cost — measured accuracy collapses well before the advertised window fills.
- Substrate decision rule: **always-relevant + small → inject it all (ChatGPT pattern); curated + auditable → files (Anthropic pattern); large + heterogeneous → vector RAG (Letta-archival pattern)**. Pick per memory type, not one-size-fits-all.
- Budget to *effective* context (~hundreds of K at best), never to the advertised window.
