# prompt-evaluation

> **Topic index.** How to measure LLM output quality with **graders** — code, model (LLM-as-judge), and human — turning subjective "is this good?" into an objective signal you can drive prompt iteration against.
>
> **Origin:** Anthropic **"Building with the Claude API"** course → **"Prompt Evaluations"** module → **Lesson 17 "Grading with AI"** (entry point: BizMate AI Vietnamese dub [nYMcPrnRzhI](https://www.youtube.com/watch?v=nYMcPrnRzhI) + original English [GjakSOir2dE](https://www.youtube.com/watch?v=GjakSOir2dE)). Deep-dived against the [anthropics/courses](https://github.com/anthropics/courses) repo, the [anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook), Anthropic's official test-and-evaluate docs, and the broader LLM-as-judge literature.
>
> **Verification:** adversarially verified via Workflow `wf_dd6c7095-c76` (16 agents, 6 facets each fact-checked). Corrections logged in [[prompt-evaluation/source-provenance]]. Constitutional rule #4 (never fabricate) honored — every claim carries a `source_url`.

---

## Articles

- [[prompt-evaluation/overview]] — the Lesson 17 core: what a grader is, the three grader types, the model-grader walkthrough, and the single most important technique (**reasoning before score**).
- [[prompt-evaluation/grader-types-deep-dive]] — code vs model vs human graders in depth, with verified Anthropic code/rubric examples and the decision rule for which to use.
- [[prompt-evaluation/llm-as-judge-methodology]] — model-grader pitfalls & fixes: score clustering, position/verbosity bias, pairwise-vs-pointwise, structured outputs, grader-model choice, the temperature-≠-determinism caveat.
- [[prompt-evaluation/eval-workflow-and-criteria]] — Anthropic's official empirical-eval workflow: 8 success-criteria dimensions, test-case design ("20–50 from real failures", volume>quality), the cyclical loop, the 9-lesson course map, the Console Eval tool.
- [[prompt-evaluation/eval-tooling-and-agent-rag]] — the tooling landscape (Promptfoo, DeepEval, RAGAS, Braintrust/Langfuse, GitHub-Actions regression gates) + evaluating agents & RAG (trajectory vs final-answer, RAGAS 4 metrics, pass@k).
- [[prompt-evaluation/source-provenance]] — the two videos, the canonical original course, and the full verified-vs-corrected log (what the deep-dive confirmed and what it threw out).

## Pilot methods (how to apply this to your flow)

15 ranked application methods + a critic's reframe live in `output/(C) 2026-06-16-prompt-evaluation-pilot-methods.md`. Three angles: the **knowledge pipeline** (grade autopilot/Storm Bear wiki ships), **hireui** (eval-first harness for its first AI feature), and **Claude Code skills/prompts** (regression-test outputs).

## Cross-topic links

- Sister topic (same BizMate/Anthropic source lineage): [[claude-api-cost-optimization/_index]]
- Validation-loops discipline: [[harness-engineering/_index]]
- Rule 9 "tests verify intent, not behavior": [[claude-md-12-rules/_index]]
- Human-checkpoint grading: [[autonomous-loops-human-in-the-loop/_index]]

## Key Takeaways

- A **grader** converts model output → an objective signal (commonly a 1–10 score or a binary correct/incorrect).
- Three grader types: **code** (deterministic, free, fast — use whenever possible), **model** (flexible judgment, costs an API call, needs care), **human** (gold standard, slow + expensive).
- **Decide evaluation criteria upfront**, then code-grade what code can (format, syntax, exact match) and model-grade the rest (quality, instruction-following).
- The lesson's load-bearing insight: **make the model grader emit reasoning/strengths/weaknesses *before* the score** — ask for a bare score and you get clustered 6s. Anthropic's docs confirm: "ask the LLM to think first… increases evaluation performance."
- Aggregate per-case scores into one number (average) — that's the metric you iterate prompts against.
