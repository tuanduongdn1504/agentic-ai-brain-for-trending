# Eval tooling landscape + agent / RAG evals

> **Sources (verified):** [Console Eval Tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool), [Promptfoo](https://github.com/promptfoo/promptfoo), [DeepEval CI/CD](https://deepeval.com/docs/evaluation-unit-testing-in-ci-cd), [Braintrust versioning](https://www.braintrust.dev/articles/best-prompt-versioning-tools-2025/), [Kinde CI for evals](https://www.kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions/), [demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system), [RAGAS metrics](https://docs.ragas.io/en/v0.1.21/concepts/metrics/), arXiv [2503.23989](https://arxiv.org/html/2503.23989).

## Tooling — first-party → OSS → platforms

| Tool | What | Notes |
|---|---|---|
| **Anthropic Console Eval** | No-code test cases, 5-pt grading, side-by-side, versioning | first-party; best on-ramp |
| **Promptfoo** | YAML-config, CLI-first eval runner; multi-model compare; 50+ red-team plugins | OSS, MIT, ~22.3K★; Anthropic's course teaches it (lessons 5–9) |
| **DeepEval** | pytest-native; `assert_test()` + `deepeval test run`; 50+ metrics (faithfulness, hallucination, relevancy…) | OSS; CI/CD-gating, regression detection |
| **RAGAS** | RAG-specific metric suite | OSS |
| **Braintrust / Langfuse / Confident AI** | Prompt versioning + A/B + per-variant cost/latency/quality tracking | platforms |
| **TribeAI/claude-evals** | production eval harness for Claude Agent SDK; 50-case golden set; model sweeps | third-party reference impl |

> ⚠️ Verification killed a fabricated claim that **"Promptfoo was acquired by OpenAI March 2026"** — no source supports it; GitHub only says "used by OpenAI and Anthropic." Also unverified: DeepEval "3M downloads / 20M daily evals," a "Latitude" tool. See [[prompt-evaluation/source-provenance]].

## Evals in CI (regression gates)

The durable pattern — **fail the build if quality drops**:
1. On PR / commit touching prompt or agent code, check out a **golden dataset** (fixtures).
2. Run the prompt/agent over the inputs.
3. Grade with **code graders** (string/regex/JSON) + **LLM judges**.
4. **Fail the build** if mean score drops below baseline threshold (e.g. >10% regression) → blocks merge.

GitHub Actions + `ANTHROPIC_API_KEY` secret; deterministic checks run free, model judges cost per-run. This is how a one-off eval becomes a **guardrail**.

## Evaluating agents (multi-step / tool use)

- **Transcript** = the full record: outputs + tool calls + reasoning.
- **Grade the outcome, not the path.** Agents find creative valid routes; brittle step-by-step rubrics punish them. *"Evaluate what the agent produced, not the path it took"* unless the path itself matters.
- **Tool-call correctness** (did it call the right tool with the right args) is a natural **code grader**.
- **Non-determinism metrics:** `pass@k` (success in *k* attempts) and `pass^k` (all *k* succeed) capture flaky agent behavior.
- **Start small:** Anthropic's multi-agent team *"started with ~20 queries representing real usage"* — enough to see the impact of changes; scale later.

## Evaluating RAG / knowledge retrieval

**RAGAS four core metrics:**
- **Faithfulness** — is the answer grounded in the retrieved context (no hallucination)?
- **Answer relevancy** — does it actually address the question?
- **Context precision** — is the retrieved context on-point?
- **Context recall** — did retrieval get everything needed?

Faithfulness + answer-relevancy are natural **model graders**; precision/recall need labeled retrieval ground truth. Directly relevant to grading a **knowledge-wiki article**: "is every claim supported by a cited source?" is a faithfulness check.

## Rubric structures for complex outputs

- **CRE (Complete Rubric Evaluation):** one nested-JSON pass scoring many sub-criteria at once (keys = methods/dimensions).
- **PRE (Pointwise Rubric Evaluation):** one rubric point per call — more expensive, forces stricter differentiation.

## Key Takeaways

- On-ramp order: **Console Eval (no-code) → Promptfoo/DeepEval (scripted) → CI gate (guardrail)**.
- Put evals in CI to make quality a merge gate, not a vibe.
- Agents: grade outcomes not paths; tool-calls are code-gradable; use pass@k for flakiness; start with ~20 real queries.
- RAG/wiki: faithfulness + relevancy + context precision/recall; "every claim cited" is a faithfulness grader.
- Verification matters — it caught a fabricated acquisition and bogus adoption stats.
