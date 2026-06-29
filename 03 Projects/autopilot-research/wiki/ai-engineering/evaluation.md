# Evaluation — Measuring What Matters (Ch. 3–4)

## Source

Video sections "Evaluation: Measuring What Matters" → "Evaluation Pipeline for Production" + Huyen *AI Engineering* Ch.3 (Evaluation Methodology) & Ch.4 (Evaluate AI Systems). The book's most-emphasized topic. See [[overview]], [[source-provenance]].

> **The thesis, verbatim (Ch.4):** *"Not having a reliable evaluation pipeline is one of the biggest blockers to AI adoption."* And: *"No perfect evaluation method exists. It's impossible to capture the ability of a high-dimensional system using one- or few-dimensional scores."*

## Why evaluation is *the* core skill

- **You can't improve what you don't measure.** Evaluation turns AI development "from guesswork into engineering." Without it you're "just hoping."
- Good evaluation lets you: measure progress, compare models/approaches, **catch regressions early**, align with business goals, and build user trust. It is the **feedback system for AI quality**.

## Why AI evaluation is *hard* (vs traditional ML)

Foundation-model outputs are **open-ended and subjective** (probabilistic, not deterministic). What makes it hard:

- **Open-ended outputs** — many valid answers can exist.
- **Subjective quality** — helpfulness, clarity, tone, safety are hard to score automatically.
- **Context-dependent** — a "good" answer depends on task, user intent, and domain (a poorly-phrased request yields a "worse" answer that isn't the model's fault).
- **Multidimensional** — quality, safety, **cost**, and **latency** all matter at once. *AI quality is not a single metric.*

Ch.3 also covers **language-modeling metrics** the video skips — **entropy, cross-entropy, bits-per-character/byte, perplexity** — and their careful interpretation, plus an **introduction to embeddings** (used in similarity scoring and in [[rag]]).

## Two families of evaluation methods

| Family | What | How | Measures |
|---|---|---|---|
| **Exact / objective** | deterministic or verifiable outcomes | checked programmatically — code tests, math answers, **schema validation**, functional correctness, similarity-to-reference | correctness, functional performance |
| **Subjective** | quality judged by humans or AI | rubric scoring by a human (with context) or by another model | user experience, nuanced quality (helpfulness, tone, creativity, explanation quality) |

This maps 1:1 onto the **code vs model vs human** grader taxonomy in [[../prompt-evaluation/_index]]: *code-grade what code can; model-grade the rest; humans are the gold standard but slow.*

## AI-as-a-judge (a.k.a. LLM-as-a-judge)

**One model evaluates another model's output** using a rubric or side-by-side comparison.

How it works (the video's 4 steps): (1) define a rubric + examples → (2) generate candidate outputs → (3) ask a judge model to score/rank → (4) aggregate scores and compare. Example: outputs A & B go through a judge → A scores 90%, B 75% → A wins.

**Limitations (Huyen, Ch.3 — do not ignore these):** judges are **subjective** and "their scores need to be interpreted in the context of what judges are being used." Known failure modes: **bias, inconsistency, model-specific preferences** (and position/verbosity bias — see [[../prompt-evaluation/_index]]). Ch.3 also covers **which models can act as judges**, and **preference models** (specialized judges for predicting user preference).

> **Comparative / ranking evaluation** (Ch.3, skipped by the video): rank model *pairs* against each other rather than scoring each independently — this is how public leaderboards (e.g. Chatbot Arena-style) work. It complements pointwise scoring but has its own challenges.

## Model selection is *not* just leaderboards (Ch.4)

- Public benchmarks "identify poor models but cannot determine the best model for **your** application." Leaderboards use different datasets/tasks/metrics, may not match your domain or language, ignore cost/latency/UX, and change fast.
- **What to do instead:** (1) define your use case + success criteria *first*; (2) build a **private evaluation set**; (3) run **side-by-side benchmarks** on *your* data; (4) evaluate **quality, safety, cost, and latency**; (5) make **data-driven** decisions.
- **Build vs buy / host vs API** depends on **seven factors** (Ch.4): data privacy, data lineage, performance, functionality, control, cost, compliance. (Directly relevant to hireui candidate-PII — see [[../cowork-third-party-inference/_index]] for the BYOM/sovereignty angle.)
- **Evaluation criteria** (Ch.4): domain-specific capability, generation capability (incl. factual consistency + safety), instruction-following capability, and cost+latency.

## Design your evaluation pipeline (Ch.4, 3 steps)

1. **Evaluate all components in a system** — not just the final answer; each stage (retriever, prompt, tool, model) gets measured.
2. **Create an evaluation guideline** — what "good" means, with rubric + examples.
3. **Define evaluation methods and data** — which method (exact/AI-judge/human) and which test set.

## The production evaluation loop (video's framing)

`Test set (tasks, prompts, edge cases)` → `System version (model + prompt + tools + RAG)` → `Evaluator (human or AI judge)` → `Score (quality, safety, cost, latency)` → `Decision (ship / hold / improve)` → `Monitoring (production drift)` → back to test set.

> **Re-evaluate after every change** — prompt change, model change, data change, tool change. Any of them can silently break the system.

## Key Takeaways

- **Evaluation is the biggest blocker to AI adoption** — build the pipeline before you scale.
- Split into **exact** (code-checkable) vs **subjective** (human / AI-judge); combine methods because no single score captures a high-dimensional system.
- **AI-as-judge is powerful but biased** — use rubrics, interpret scores in context, and beware position/preference bias.
- **Don't pick models off leaderboards** — define success criteria, build a private eval set, benchmark on your own data across quality/safety/cost/latency.
- **Evaluate every component**, and **re-evaluate after every change** (prompt/model/data/tool).

## Cross-links

- [[../prompt-evaluation/_index]] — the operational how-to (graders, reasoning-before-score, Console eval, Promptfoo/DeepEval/RAGAS); this chapter is its conceptual backbone
- [[foundation-models]] (why outputs vary → why eval is hard) · [[rag]] (evaluate the retriever) · [[agents-and-memory]] (agent eval = trajectory + outcome)
- [[../agentic-analytics-harness/_index]] — "observability over scorecards"; daily trace-driven eval in production
