# Grader types — deep dive (code / model / human)

> **Source:** [anthropic-cookbook/misc/building_evals.ipynb](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb) + [Anthropic develop-tests docs](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests) (both verified). Extends [[prompt-evaluation/overview]].
>
> ⚠️ **Model IDs:** the cookbook examples cite `claude-opus-4-1`; examples below use **current** IDs (`claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`) since those are what you'd run today.

## 1. Code-based graders — prefer these

Standard code (mostly string matching + regex) grades the output. *"By far the best grading method if you can design an eval that allows for it, as it is super fast and highly reliable"* (cookbook). Zero API cost, deterministic, instant — perfect for CI gates.

Common patterns:
- **Exact match / contains** — `output.strip().lower() == golden.lower()`, or `key_phrase in output`.
- **JSON validity + schema** — `json.loads()` (raises on bad syntax) then `jsonschema.validate()` (raises on schema violation).
- **Regex / keyword** — required keywords present, forbidden keywords absent.
- **Readability** — `textstat.flesch_kincaid_grade(text)` against a target reading level.
- **Length bounds**, numeric tolerance, classification accuracy when ground truth exists.

```python
# Exact-match accuracy (verified pattern, Anthropic docs)
def evaluate_exact_match(model_output, correct_answer):
    return model_output.strip().lower() == correct_answer.lower()

accuracy = sum(
    evaluate_exact_match(out, case["answer"])
    for out, case in zip(outputs, cases)
) / len(cases)
```

> ⚠️ **`ast.parse()` does NOT prove code runs.** Parsing source into an AST catches *obvious* syntax errors but is not full validation — `compile()` can still raise further `SyntaxError`, and a snippet like a bare `return 42` parses yet isn't executable. (Correction caught during verification; see [[prompt-evaluation/source-provenance]].) Use `compile()` for stricter validation, and even that doesn't prove semantic correctness.

## 2. Model-based graders (LLM-as-judge) — flexible judgment

Feed the output into *another* model call asking it to judge against a rubric. *"Claude is highly capable of grading itself, and can be used to grade a wide variety of tasks that might have historically required humans, such as analysis of tone… or accuracy in free-form question answering"* (cookbook).

The verified Anthropic cookbook pattern uses **`<thinking>` for reasoning + a result tag** (`<correctness>` in the cookbook; the docs example uses `<result>`):

```python
def build_grader_prompt(answer, rubric):
    return f"""You will be provided an answer and a rubric.
<answer>{answer}</answer>
<rubric>{rubric}</rubric>
First, think through whether the answer is correct based on the rubric
inside <thinking></thinking> tags. Then output 'correct' or 'incorrect'
inside <correctness></correctness> tags."""
```

For **graded (1–N) scoring**, force reasoning + structured fields first (see the score-clustering fix in [[prompt-evaluation/llm-as-judge-methodology]]). Anthropic's docs recommend: **detailed clear rubrics**, **empirical/specific output formats** (e.g. 1–5 scale, not vibes), and **encourage reasoning** before the score.

When code can't capture it (tone, helpfulness, faithfulness, "did it actually answer the question"), this is your tool.

## 3. Human graders — the gold standard

A person reads the output, compares to the golden answer, assigns a score. *"The most capable grading method… but also incredibly slow and expensive"* (cookbook). Use it to:
- **Calibrate** your model grader (does the judge agree with you?).
- **Spot-check** a small random sample to catch silent drift the automated graders miss.
- Grade the genuinely subjective things on a low-volume basis.

## The decision rule

```
Can a deterministic check answer it?           → CODE grader   (free, gate in CI)
Needs judgment but high volume / repeatable?   → MODEL grader  (with reasoning-first)
Subjective + low volume + need ground truth?   → HUMAN grader  (calibration + spot-check)
```

Anthropic explicitly recommends **combining multiple grader types** rather than relying on one — code-grade the structure, model-grade the substance, human-grade a sample.

## Key Takeaways

- Code first: cheapest, deterministic, the right thing to put in a CI gate.
- `ast.parse` ≠ "runs" — a real correction; use `compile()` and don't overclaim.
- Model graders unlock judgment that code can't express — but only with reasoning-first rubrics.
- Humans calibrate and spot-check; they don't scale.
- Best practice is a **blend** matched to each criterion, not one grader for everything.
