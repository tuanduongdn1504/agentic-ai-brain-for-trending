# Finetuning, Dataset Engineering & Inference Optimization (Ch. 7–9)

## Source

**The chapters the 41-minute video largely skips.** Grounded directly in Chip Huyen's own chapter summaries ([chiphuyen/aie-book/chapter-summaries.md](https://github.com/chiphuyen/aie-book/blob/main/chapter-summaries.md)) + the verified ToC — *not* third-party blogs. See [[overview]], [[source-provenance]].

> Why this article exists: "demo → production" lives mostly in chapters 7–10. A summary that stops at agents has skipped the part where you cut cost, adapt the model, and build the data flywheel. This is the gap most relevant to **hireui's first production LLM feature**.

---

## Chapter 7 — Finetuning

**Central question (Huyen): "When to finetune versus when to use RAG"** — this choice shapes your whole architecture.

- Fine-tuning sits **last** in the order-of-operations (prompt → RAG → agents → *then* fine-tune) — reach for it only after cheaper levers are exhausted.
- It "touches old (transfer learning) and new (PEFT) concepts," making it conceptually complex despite straightforward implementation.
- **Full-parameter finetuning became impractical** as models scaled (memory grew prohibitively). Hence:
  - **PEFT (Parameter-Efficient Fine-Tuning)** — train only a small set of parameters → big memory savings.
  - **Quantized training** — reduce bit precision to fit in memory (see Ch.9 quantization).
  - **LoRA (Low-Rank Adaptation)** — popular for parameter efficiency, data efficiency, and **modularity** (combine multiple LoRAs).
  - **Model merging** — combine several finetuned models into a better single model; useful for on-device deployment + model upscaling.
- **The real obstacle is data, not compute.** Huyen, verbatim: **"Finetuning is easy, but getting data for finetuning is hard."** (→ which is exactly why Ch.8 exists.)
- **Reasons NOT to finetune** (the book devotes a section to this): if prompting/RAG get you there, fine-tuning adds data-collection burden, training/serving complexity, and maintenance cost for marginal gain.

> **For hireui:** almost certainly **don't fine-tune** for a first recruitment feature. Prompt + RAG over your job/candidate data will go further, faster, cheaper. Revisit only if a measured eval shows a domain gap prompting/RAG can't close.

---

## Chapter 8 — Dataset Engineering

**Core principle (Huyen, verbatim):** *"To build a dataset to train a model, you start by thinking through the behaviors you want your model to learn and then design a dataset to show these behaviors."*

- **Data requirements differ by phase** — pre-training vs instruction-finetuning vs preference-finetuning need different data.
- **Three criteria across all phases: quality, coverage, quantity.** And the headline: **"A small amount of high-quality data can outperform a large amount of noisy data."**
- **Diversity is critical** — many teams find improving *diversity* (not just volume) is the key to performance gains.
- **Data synthesis** — AI-generated synthetic data is now practical for realistic/complex data. *But* synthetic data **must be evaluated before training** ("quality verification is as challenging as evaluation of other AI outputs" → see [[evaluation]]). Watch for **model collapse** when training on synthetic data.
- **Data processing** — inspect, **deduplicate**, clean, and filter.
- **What you can't automate (verbatim):** *"You can't automate thinking through what data you want. You can't easily automate annotation guidelines. You can't automate paying attention to details."*

> **For the autopilot/Storm Bear vaults:** this *is* your source-ingestion discipline by another name — curation > volume, dedupe, clean, filter, and evaluate before you "train" (here, before you compile into the wiki). The librarian rules and `raw/_inventory.md` coverage discipline are dataset engineering applied to a knowledge base.

---

## Chapter 9 — Inference Optimization

**Key principle (Huyen, verbatim):** *"A model's usability depends heavily on its inference cost and latency."*

- **Efficiency metrics:** **latency** split into **TTFT (time-to-first-token, the *prefill* phase)** and **TPOT (time-per-output-token, the *decode* phase)**; plus **throughput** and **utilization**.
- **Two distinct bottlenecks** require different fixes: **prefill is compute-bound, decode is memory-bound.** (This is the dual-bottleneck the deep-dive flagged.)
- **Two levels of optimization:**
  - **Model-level** (quantization, distillation, attention efficiency) — *may alter model behavior.*
  - **Inference-service-level** (batching, parallelism, **prompt caching**) — *typically preserves the model unchanged.*
- **Workload picks the technique:** **KV caching** matters more for long contexts; **prompt caching** for multi-turn conversations.
- **Most impactful in general:** quantization, tensor parallelism, replica parallelism, attention-mechanism optimization.
- **Reality for app developers:** *"Most application developers use model APIs with built-in optimization rather than implementing techniques directly."* You usually buy inference efficiency (via the provider) rather than build it — but you must still **choose models + caching strategy** for cost/latency.

> **Direct bridge to [[../claude-api-cost-optimization/_index]]:** prompt caching (~0.1× cost on cache hits), context engineering, and model routing/advisor are the *application-layer* version of this chapter. This is the production cost lever the video never mentions.

---

## Key Takeaways

- **Fine-tune last, and usually not at all** for a first app — prompt + RAG win on cost/speed; "finetuning is easy, getting the data is hard."
- **Dataset engineering = quality > quantity + diversity + dedupe/clean/filter + evaluate synthetic data.** Curation can't be fully automated. (Your vault's ingestion discipline *is* this.)
- **Inference optimization = cost + latency**, with a **prefill (compute-bound) vs decode (memory-bound)** split; app developers mostly buy it via APIs + **caching**.
- These three chapters are where **"demo → production" economics actually live** — and where the video stops short.

## Cross-links

- [[overview]] (the prompt→RAG→agents→finetune order) · [[rag]] (the alternative to finetuning) · [[evaluation]] (evaluate synthetic data + model choice) · [[production-architecture-and-feedback]] (Ch.10 ties these together)
- [[../claude-api-cost-optimization/_index]] (Ch.9 at the application layer) · [[../cowork-third-party-inference/_index]] (host-vs-API / BYOM) · [[../prompt-evaluation/_index]] (eval synthetic data)
