# Grading with AI — overview (Lesson 17)

> **Source:** `raw/2026-06-16-grading-with-ai-lesson17.md` (yt-dlp transcript of [nYMcPrnRzhI](https://www.youtube.com/watch?v=nYMcPrnRzhI) / [GjakSOir2dE](https://www.youtube.com/watch?v=GjakSOir2dE)); canonical original = Anthropic "Building with the Claude API" → Prompt Evaluations → "Model-graded evals" lesson ([anthropics/courses](https://github.com/anthropics/courses/blob/master/prompt_evaluations/README.md)).

## What a grader is

- A **grader** takes model output and returns an **objective signal** — a number, a true/false, anything machine-readable.
- Very commonly a **number 1–10** (10 = high quality, 1 = low). Not required, but the default convention.
- The point: turn "is this output good?" (subjective, un-trackable) into a metric you can **average, trend, and optimize against**.

## The three grader types

| Type | Mechanism | Strength | Weakness |
|---|---|---|---|
| **Code** | output → a code snippet you author | deterministic, fast, free, reliable | only works for checkable things (format, syntax, exact match) |
| **Model** (LLM-as-judge) | output → an *additional* model API call | flexible — judges quality, instruction-following, completeness | costs a call; non-deterministic; needs calibration |
| **Human** | output → a person | most flexible, gold standard | slow + tedious + expensive |

Anthropic's cookbook states code-based grading is "by far the best grading method if you can design an eval that allows for it" ([building_evals.ipynb](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb)). See [[prompt-evaluation/grader-types-deep-dive]].

## Decide your criteria *upfront*

The lesson's discipline: before grading, name **exactly which aspects of the response you care about**. The lesson's worked example (grading Claude's code-generation answers) used three criteria:

1. Output is **only** Python / JSON / regex — no extra explanation. → **code grader** (format check)
2. The code has **valid syntax** — no typos. → **code grader** (syntax check)
3. The answer **clearly addresses the task** with accurate logic. → **model grader** (judgment)

> Rule of thumb: **code-grade what code can, model-grade the rest.**

## The model-grader walkthrough (`grade_by_model`)

1. Pass in the **test case** (input + metadata) and the **output** from the original model call.
2. Send a **fairly long grader prompt** that: sets a role, asks the model to evaluate an AI-generated solution, prints the task, lists the generated solution, and gives explicit response directions.
3. **Ask for strengths, weaknesses, reasoning, AND a score** — not a bare score.
4. Extract clean JSON via a **prefilled `\`\`\`json` assistant turn + a stop sequence** (closing `\`\`\``), then `json.loads`.
5. Wire it into `run_test_case`: replace the placeholder score with `grade_by_model(test_case, output)`; pull out `score` + `reasoning`.
6. **Aggregate**: average all the scores → one objective number (the lesson got **7.33**).

## ⭐ The load-bearing insight: reasoning before score

> "If you ask for a score by itself, you very often get scores of just **6** — the model assumes 'could be better, could be worse, give it a 6.' By asking for reasoning, strengths and weaknesses, you make it **hone in** and decide on a more concrete score." — Lesson 17

This is **confirmed by Anthropic's official docs**: under "Tips for LLM-based grading" — *"Encourage reasoning: Ask the LLM to think first before deciding an evaluation score… This increases evaluation performance, particularly for tasks requiring complex judgement"* ([develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests)). The mechanism that fixes **score clustering** — see [[prompt-evaluation/llm-as-judge-methodology]].

> ⚠️ The lesson parses raw `json.loads` after a prefill+stop-sequence. Today there's a stronger option: the **Structured Outputs API** *guarantees* schema-compliant JSON via constrained decoding — no parse errors. See [[prompt-evaluation/llm-as-judge-methodology]].

## Key Takeaways

- Grader = output → objective signal (default: 1–10).
- Three types — code / model / human; prefer code, escalate to model for judgment, reserve human for the gold standard.
- Decide criteria upfront; split them across grader types.
- **Reasoning before score** is the highest-ROI single technique — it's both the lesson's punchline and Anthropic's documented best practice.
- Average the per-case scores → the metric you iterate against.
