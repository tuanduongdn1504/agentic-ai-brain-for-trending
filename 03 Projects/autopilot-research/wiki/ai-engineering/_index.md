# ai-engineering

> **Topic index.** The discipline of turning **foundation models into useful, safe, fast, reliable products** — i.e. taking an AI app from **demo → production**. Organized around the verified 10-chapter structure of the canonical text.
>
> **Original (load-bearing):** Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, Kindle 2024-12-04 / paperback 2025-01-07, 534pp, 10 chapters). Companion repo: [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) (16.3K★).
>
> **Entry point:** Anas Riad's video "AI Engineering in 41 Minutes: From Demo to Production" ([geQqpO_AFMo](https://www.youtube.com/watch?v=geQqpO_AFMo), 2026-06-17, 41:54) — a faithful chapter-walkthrough (covers Ch.1–6; **skips the production half Ch.7–10**, which this wiki fills in from Huyen's own chapter summaries).
>
> **Verification:** Workflow `wf_508f1c32-b7b` (15 agents: 5 finders + 9 independent skeptics + critic) + direct primary-source fetch. Corrections logged in [[source-provenance]]. Constitutional rule #4 honored.
>
> **This is the wiki's first *conceptual / book* topic** (sibling to [[../prompt-evaluation/_index]]) rather than a tool/repo topic — the foundational discipline the other topics specialize.

---

## Articles

- [[ai-engineering/overview]] — the big picture: AI-engineering-vs-ML-engineering, the four objectives, demo≠production, the full lifecycle, the prompt→RAG→agents→finetune order, and the 10-chapter map.
- [[ai-engineering/foundation-models]] — **Ch.1–2**: what a foundation model is, tokens/self-supervision, **sampling** (temperature/top-p/top-k/penalties), structured outputs, test-time compute, and **why hallucinations happen**.
- [[ai-engineering/evaluation]] — **Ch.3–4**: the book's most-emphasized topic — exact vs subjective eval, **AI-as-judge** + its limits, model selection beyond leaderboards, the 3-step eval pipeline. *"Not having a reliable evaluation pipeline is one of the biggest blockers to AI adoption."*
- [[ai-engineering/prompt-engineering-and-guardrails]] — **Ch.5**: the cheapest lever; the 5-part prompt anatomy; prompting as a production system; **prompt injection/jailbreaking + defenses**; end-to-end guardrails.
- [[ai-engineering/rag]] — **Ch.6 (RAG)**: why context matters, the offline-index/online-query pipeline, **BM25 vs embeddings vs hybrid**, retrieval optimization (chunking/query-rewrite/metadata/re-rank), and RAG failure modes.
- [[ai-engineering/agents-and-memory]] — **Ch.6 (Agents)**: RAG-vs-agents, the plan-act-observe loop, **tools + least-privilege permissions**, the four kinds of memory, and agent failure modes.
- [[ai-engineering/finetuning-dataset-inference]] — **Ch.7–9 (the video skips these)**: when *not* to finetune (LoRA/PEFT/merging), dataset engineering (quality>quantity, synthesis, dedupe), inference optimization (prefill/decode, caching). *Grounded in Huyen's own chapter summaries.*
- [[ai-engineering/production-architecture-and-feedback]] — **Ch.10 (the capstone)**: the 5-step production architecture (context → guardrails → router/gateway → caches → agents) + monitoring/observability + the **user-feedback data flywheel**.
- [[ai-engineering/book-author-and-video]] — the originals: book metadata + verified TOC, **Chip Huyen**'s background/credibility, the prior bestseller, and the video creator (**Anas Riad** — third-party summarizer, not official).
- [[ai-engineering/source-provenance]] — the verified-vs-corrected ledger (the `huyenchip.com/ai-engineering`-404 correction, the "third-party-not-official" flag, the author-reported reception caveat, etc.).

## Pilot methods (how to apply this to your flow)

A ranked menu of application methods + a critic's reframe lives in **`output/(C) 2026-06-29-ai-engineering-pilot-methods.md`**. Four angles: **hireui Goal #2** (the bullseye — its first LLM feature is a literal demo→production problem), the **autopilot/Storm Bear vaults** (the wiki *is* a RAG system; AI-as-judge = your verify workflows), the **personal Claude Code / prompt-eval pilot** (Ch.3–4 deepen the discipline you're already running), and **Scrum coaching** (teach the lifecycle + eval-first discipline).

## Cross-topic links

- [[../prompt-evaluation/_index]] — operational eval (Anthropic course) ↔ this book's Ch.3–4 conceptual backbone
- [[../claude-api-cost-optimization/_index]] — Ch.9 inference-optimization at the application layer (caching/routing/advisor)
- [[../multi-agent-orchestration/_index]] — Ch.6 agents at system scale (the Anthropic originals)
- [[../claude-code-memory-systems/_index]] — Ch.6 memory + RAG-as-memory; the Karpathy LLM-Wiki lineage (this vault)
- [[../agentic-analytics-harness/_index]] — a real production foundation-model harness living these lessons
- [[../cowork-third-party-inference/_index]] — Ch.4 host-vs-API / BYOM / data-sovereignty
- [[../claude-code-observability/_index]] — Ch.10 monitoring/observability in practice

## Key Takeaways

- **AI engineering = adapting pre-trained foundation models into products** (vs ML engineering = training models). The job is **demo → production**.
- **Evaluation is the #1 blocker** to shipping; define success metrics first, build a private eval set, evaluate every component, re-evaluate after every change.
- **Order of levers: prompt → RAG → agents → fine-tune** (last resort). Reach for the cheapest one that works.
- The **production half (Ch.7–10)** — finetuning economics, dataset engineering, inference cost, the 5-layer architecture, feedback loops — is where most real engineering lives, and is exactly what the video skips.
- Foundation models are **probabilistic**: design around sampling, hallucination, guardrails, and observability — don't pretend they're deterministic.
