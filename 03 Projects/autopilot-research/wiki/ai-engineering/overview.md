# AI Engineering — Overview (the big picture)

## Source

- **Video (entry point):** Anas Riad, "AI Engineering in 41 Minutes: From Demo to Production" ([geQqpO_AFMo](https://www.youtube.com/watch?v=geQqpO_AFMo), 2026-06-17, 41:54, 17.4K views) — a third-party chapter-walkthrough.
- **Original resource (load-bearing):** Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, Kindle 2024-12-04 / paperback 2025-01-07, 534pp). Companion repo: [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book).
- Raw: `raw/2026-06-29-ai-engineering-chip-huyen.md`. Provenance + corrections: [[source-provenance]].

## What "AI engineering" is (the central reframing)

- **AI engineering = building applications on top of *pre-trained* foundation models** (adapting them), as distinct from **ML engineering = building models from scratch** (collect data → train → serve). This distinction is the book's organizing thesis. Per Huyen's own chapter summary: AI engineering "differs from ML engineering by introducing new challenges and solutions specific to foundation models" and "is an evolution from ML engineering rather than a replacement."
- The video frames the goal as turning a foundation model into a product that is **useful, safe, fast, and reliable** — four objectives the presenter groups as **quality** (accurate + useful output), **safety** (not harmful; data private/secure), **speed & cost** (coupled — faster usually costs more), and **feedback** (learn and improve over time).
- The book's one-line mission, in the video's words: **"move from a simple demo to a real product."** That is the whole point of the discipline — and the reason this topic is the bullseye for [[../prompt-evaluation/_index]]-style rigor and for **hireui's first LLM features** (a demo→production problem with zero legacy).

## Why the discipline exists *now* (3 forces)

1. **Better model capability** — modern foundation models write, reason, summarize, code, and generalize across tasks; agents can chain steps.
2. **Easy access through APIs** (and MCP for external tools) — you consume intelligence as a service instead of training it.
3. **Lower time-to-build** — Replit/Lovable-class tooling makes a first cut nearly instant. *More demand + lower barrier to entry = a new engineering discipline.*

## Demo ≠ production (the gap the discipline closes)

| Demo | Production |
|---|---|
| one prompt, manual testing | system design + **evaluation pipelines** |
| one model call | context + tools + **model routing** |
| low stakes, no monitoring | **guardrails + reliability + monitoring + feedback loops** |
| runs on your laptop, a few users | hundreds of users, cost + latency under control, debuggable |

> The single most-cited production lesson in the book (verbatim, Ch.4): **"Not having a reliable evaluation pipeline is one of the biggest blockers to AI adoption."** Demos skip evaluation; products cannot. See [[evaluation]].

## The full AI engineering lifecycle (as the video lays it out)

1. **Use case** — what problem are we actually solving? (Build only if there's a problem.)
2. **Model selection** — OpenAI / Claude (Opus/Sonnet) / Gemini / Llama / open weights. *Not just leaderboards* — see [[evaluation]].
3. **Evaluation** — define the success metric *before* building. What are we optimizing, and how do we measure it?
4. **Improve quality** — prompts → RAG → agents → fine-tuning (in roughly that order of cost/effort). See [[prompt-engineering-and-guardrails]], [[rag]], [[agents-and-memory]], [[finetuning-dataset-inference]].
5. **Production architecture** — make it reliable + usable at scale. See [[production-architecture-and-feedback]].
6. **Monitoring** — track failures, cost, latency (the "MLOps" layer).
7. **Feedback loop** — *never consider a system done.* Models change, data drifts; keep iterating.

## The intentional order-of-operations (a load-bearing book thesis)

- **Start with prompt engineering** (fastest, cheapest lever; changes behavior without changing the model) → **then RAG** (give it the facts it lacks) → **then agents** (planning + tools for multi-step tasks) → **fine-tuning last** (Ch.7 frames it as effectively a last resort; "Finetuning is easy, but getting data for finetuning is hard").
- Corollary the video stresses repeatedly: **foundation models are probabilistic, not deterministic.** If a task can be solved deterministically (a Python function), don't reach for a model. Build "your workflows around their probabilistic nature" (Huyen, Ch.2). This is why sampling, hallucination, evaluation, and guardrails dominate the discipline — see [[foundation-models]].

## The book's 10-chapter map (verified TOC)

1. Introduction to Building AI Applications with Foundation Models → [[overview]] + [[book-author-and-video]]
2. Understanding Foundation Models → [[foundation-models]]
3. Evaluation Methodology → [[evaluation]]
4. Evaluate AI Systems → [[evaluation]]
5. Prompt Engineering → [[prompt-engineering-and-guardrails]]
6. RAG and Agents → [[rag]] + [[agents-and-memory]]
7. Finetuning → [[finetuning-dataset-inference]]
8. Dataset Engineering → [[finetuning-dataset-inference]]
9. Inference Optimization → [[finetuning-dataset-inference]]
10. AI Engineering Architecture and User Feedback → [[production-architecture-and-feedback]]

> The video covers chapters 1–6 well and **largely skips 7–10**. Those skipped chapters are where most of the *production* discipline lives — which is exactly what "demo → production" requires. This wiki fills them in from Huyen's own chapter summaries.

## Key Takeaways

- **AI engineering = adapting pre-trained foundation models into products; ML engineering = training models.** Different discipline, different bottlenecks.
- The job is **demo → production**: system design + evaluation + context + guardrails + monitoring + feedback — not a single clever prompt.
- **Evaluation is the #1 blocker** to shipping; define success metrics before you build.
- **Order of levers:** prompt → RAG → agents → fine-tune. Reach for the cheapest one that works; treat fine-tuning as last resort.
- Foundation models are **probabilistic** — design around sampling, hallucination, and uncertainty rather than pretending they're deterministic.

## Cross-links

- [[../prompt-evaluation/_index]] — the eval discipline this book formalizes (Ch.3–4)
- [[../claude-api-cost-optimization/_index]] — the cost/latency lever (Ch.9 inference optimization)
- [[../multi-agent-orchestration/_index]] — Ch.6 agents at system scale
- [[../claude-code-memory-systems/_index]] — Ch.6 memory + RAG as a memory substrate
- [[../agentic-analytics-harness/_index]] — a production foundation-model harness (the book's lessons, lived)
