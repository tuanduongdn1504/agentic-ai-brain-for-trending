# Pillar 1 — Fundamentals, not internals

## Source
Quân IT, [`RcF6ofU2nLs`](https://www.youtube.com/watch?v=RcF6ofU2nLs) [02:31–04:23].

## What he says

- To be an AI **engineer**, you only need the **basic principles** of AI — *not* a deep mechanistic understanding of how it all works.
- Deep internals are for **AI researchers** — the people at OpenAI / Meta ("Facebook") / X paid "a few million dollars a year" to build *new frontier models* that beat the incumbents (he names **DeepSeek** and **Kimi**). *"If you're skilled enough to do that job, you're not watching my channel."*
- The fundamentals he lists you *should* understand (conceptually): **neural network**, how a model is **trained**, **weight**, **token**, **iteration**, **attention mechanism** — enough to read the basic papers and grasp how the core works.
- The analogy again: like **blockchain** — you can build DeFi / NFT / tokens / GameFi without understanding proof-of-work consensus or the hashing internals. *"You just need to be able to build things."*

## Verified facts behind the pillar

- **DeepSeek** (C2a) and **Kimi / Moonshot AI** (C2b) are both **CONFIRMED** real frontier LLMs (2026 releases). His garbled "Dipsic" = DeepSeek.
- **Researcher comp "a few million/yr"** (C2c) is **MISLEADING** — median frontier-lab researcher comp is ~$1–1.5M; only the top 5–10% reach "a few million" ($2M+). His *point* (it's an elite, very-high-paid, different job) still holds; the *magnitude* is slightly inflated. See [[quanit-becoming-ai-engineer-2026/caveats-and-corrections|caveats]].

## The sharpest caveat in the whole talk

This pillar contains the video's biggest oversimplification, flagged by the critical appraisal:

- *"You don't need to understand the internals"* is fine if it means **"you don't need transformer math."**
- It is an **overstatement** if it slides into **"you don't need to understand *when and why* models fail."** An AI engineer shipping systems must have **failure-mode literacy**: hallucination behaviour, degradation as context fills, token-limit effects, embedding-model drift in RAG, fine-tuning overfitting. That is not researcher math — it's operational knowledge — and it is *not optional*.
- Full treatment in [[quanit-becoming-ai-engineer-2026/critical-appraisal|critical-appraisal]].

## Key Takeaways

- **Concepts, not calculus** — neural-net / weight / token / attention as *literacy*, not as a research skill. Correct in spirit.
- The **researcher-vs-engineer split is the single most useful idea in the talk**: don't mistake the job of *making* models for the job of *building with* them.
- **But hold the "no internals" line loosely** — reframe it as "no transformer math, yes failure-mode literacy." This is where a mid-career engineer should *add* to Quân's advice, not just take it.
- Sits against [[ai-engineering/_index]] (Chip Huyen's Ch.1–3 cover exactly these fundamentals at the right depth) and [[agent-memory-architecture/_index]] (where embedding/context-window behaviour becomes load-bearing).
