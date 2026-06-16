# The empirical-eval workflow & success criteria (Anthropic official)

> **Sources (verified):** [Anthropic develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests), [prompting best practices](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices), [demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), [anthropics/courses prompt_evaluations README](https://github.com/anthropics/courses/blob/master/prompt_evaluations/README.md), [Console Eval Tool](https://platform.claude.com/docs/en/docs/test-and-evaluate/eval-tool).

The grading lesson is **one step inside a bigger cycle.** The full loop:

```
define success criteria → design test cases → get completions → grade → aggregate → refine → repeat
```

> *"Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations to measure performance against them. This cycle is central to prompt engineering."* — Anthropic docs.

## Step 1 — Define success criteria (8 dimensions)

Anthropic lists **eight** common success-criteria dimensions (⚠️ not 5 — correction; see [[prompt-evaluation/source-provenance]]):

1. Task fidelity · 2. Consistency · 3. Relevance and coherence · 4. Tone and style · 5. Privacy preservation · 6. Context utilization · 7. Latency · 8. Price

Criteria must be **measurable**:

| | |
|---|---|
| ❌ Bad | "Safe outputs" |
| ✅ Good | "Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter" |

## Step 2 — Design test cases

- **Source from real failures.** *"20–50 simple tasks drawn from real failures is a great start."*
- **Prioritize volume over quality:** *"More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals."*
- **Start lean, don't wait for the perfect suite.** Test both when a behavior **should** and **shouldn't** occur. Ensure a reference/golden answer exists per case.
- Test-case structure: **input** + **golden answer** (or a **rubric** for open-ended) + **metadata** for categorization.

## Step 3–5 — Complete, grade, aggregate

- Run the prompt over every test case → collect outputs.
- Grade each with the right grader ([[prompt-evaluation/grader-types-deep-dive]]).
- Aggregate: the cookbook uses `sum(grades) / len(grades) * 100%` for accuracy (⚠️ not `statistics.mean` — correction). The lesson averaged 1–10 scores to **7.33**. Either way: **one number you can trend.**

## Bonus: prompt clarity (the golden rule)

The eval that matters before any grader: *"Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."* And: **examples are one of the most reliable ways to steer output — include 3–5, relevant + diverse + structured in `<example>` tags.**

## The 9-lesson course map (the "original resource")

Lesson 17 "Grading with AI" is the **model-graded** beat of Anthropic's Prompt Evaluations course:

1. Evaluations 101
2. Writing human-graded evals with Anthropic's Workbench
3. Writing simple code-graded evals
4. Writing a classification eval
5. Promptfoo for evals: an introduction
6. Writing classification evals with Promptfoo
7. Custom graders with Promptfoo
8. **Model-graded evals with Promptfoo** ← the lesson
9. Custom model-graded evals with Promptfoo

> *"Start from the beginning with Evaluations 101, as each lesson builds on key concepts taught in previous ones."* The course's thesis: **inability to measure performance is the biggest blocker to production LLM deployment.**

## The Console Eval Tool (first-party, no code)

Anthropic's Console **Evaluate** tab: prompts with `{{variable}}` placeholders, **auto-generate test cases** (via Claude Sonnet), manual `+ Add Row` / CSV import, **5-point quality grading**, **side-by-side** prompt-variant comparison, and **prompt versioning** to re-run old test sets against new prompts. The zero-setup on-ramp before you script anything.

## Key Takeaways

- Grading is step 4 of a 6-step cycle that begins with **measurable** success criteria (8 dimensions).
- Test cases: 20–50 from real failures, volume > individual-case polish, golden answer or rubric per case.
- Aggregate to one number; trend it across prompt versions.
- The course is 9 sequential lessons; "Grading with AI" is the model-graded beat.
- The Console Eval Tool lets you do all of this **without code** first.
