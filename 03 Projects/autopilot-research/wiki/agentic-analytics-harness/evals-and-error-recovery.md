# Evals, error recovery, and observability

## Source

First-party (validation/guardrails, prompt caching, security): [omni.co — Building Omni's architecture for agentic analytics](https://omni.co/blog/building-omnis-architecture-for-agentic-analytics) [T1]. Evals + error-recovery-as-ROI + token economics: ai-heartland.com talk recap [T2]. See [[agentic-analytics-harness/source-provenance]].

## Error recovery = the highest-ROI lever [T2]

The single most surprising claim of the talk: **the biggest quality win came from error handling, not prompt wording.** Three parts:

1. **Teach the agent recovery strategies** — what to do when a query fails, returns nothing, or returns something implausible.
2. **Set an execution / retry budget** — bounded retries so recovery doesn't become an infinite loop (ties to the 50-iteration cap in [[agentic-analytics-harness/multi-agent-architecture]]).
3. **Author high-quality error messages** — every error explains **"what happened"** + **"how to fix it."** The error message is *prompt context for the next attempt*, so a good one is worth more than a clever instruction.

> Result: "**dramatic eval-score improvements with minimal prompt changes**," outpacing other optimization efforts. **Transferable finding:** before tuning prompts, make your tools fail *informatively*.

## Validation and guardrails [T1]

- "**Strict validation** around tool inputs and outputs, **detectors for malformed state**, and **integration tests** that check behavior across steps."
- Concrete guardrail: **"after summarizing, don't re-query unless filters changed."** (Stops the agent re-doing work — a cheap, deterministic rule.)
- The agent "can recognize when its assumptions didn't hold and adjust its approach" — but the *harness* enforces the floor.

## Evals — three pillars [T2]

1. **LLM-as-Judge** — automated quality benchmarking on core response correctness. (Same technique as [[prompt-evaluation/_index]]; here it's run on production analytics answers.)
2. **Benchmark-question construction — 8 quality criteria** for a *good* eval question: **evaluability, coverage, realism, difficulty, non-redundancy, discriminative power, semantic clarity, data selectivity.** (A rubric for *what makes a test worth having* — directly extends the [[prompt-evaluation/_index]] "20–50 cases from real failures" discipline.)
3. **Session triage via Claude Code** — **daily** analysis of **FAILED user sessions**; **trace-driven root-cause** identification, **prioritized over aggregate metrics.**

## Observability over scorecards [T2]

- Merrick **values observability over scorecard metrics**: "I can read **raw traces** to understand **'why did this fail'** rather than rely on judge verdicts."
- The eval *number* tells you *that* something regressed; the *trace* tells you *why*. Omni optimizes for the second.
- This mirrors the operator's own [[prompt-evaluation/_index]] note ("read the transcript to see what the model actually sees") and the autopilot routine's preference for reading loop-logs over trusting the `gaps_closed_ratio` alone.

## Cost & safety as harness properties [T1]

- **Prompt caching** is load-bearing: "You can't just dump entire result sets into the model context; it's too expensive and **breaks prompt caching**, which we rely on to keep things fast and predictable." → same levers as [[claude-api-cost-optimization/_index]], at 103.3B tokens/month.
- **Security:** the agent "can only ever run **as the current user**" — it inherits existing permissions and can never see data the user can't. Non-negotiable, and *structural* (enforced by the harness, not the prompt).

## Model & token economics [T2]

- **Haiku → Sonnet migration (Aug 2025):** agentic loops need longer context; complex chains exceeded Haiku's envelope.
- **Tokens: 1.2B/month (Aug 2025) → 103.3B/month (Apr 2026).** Sonnet let customers answer previously-unanswerable questions → adoption surge → **compounding** usage (each successful query raised next-session usage). 103.3B cross-confirmed; growth dates single-source.

## Key Takeaways

- **Make tools fail informatively before you tune prompts** — error-message quality was Omni's #1 quality lever.
- **A good eval question has 8 testable properties** — use the rubric to audit your own eval set, not just to write new ones.
- **Triage failures by reading traces, daily** — root-cause beats dashboards; automate the triage *with* Claude Code.
- **Bound retries; add deterministic guardrails** ("don't re-query unless filters changed") — cheap rules catch expensive loops.
- **Caching + summarize-don't-dump + run-as-current-user** are harness properties, not afterthoughts — they're how cost and safety stay predictable at scale.
