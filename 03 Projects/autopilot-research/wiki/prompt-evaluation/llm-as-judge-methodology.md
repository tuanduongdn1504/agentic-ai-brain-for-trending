# LLM-as-judge methodology — pitfalls & fixes

> **Sources (verified):** [Anthropic develop-tests](https://platform.claude.com/docs/en/docs/test-and-evaluate/develop-tests), [Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), arXiv [2504.14716](https://arxiv.org/abs/2504.14716v2), [JudgeBench](https://www.emergentmind.com/topics/judgebench), [Confident AI](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method). Extends [[prompt-evaluation/grader-types-deep-dive]].

Model graders are flexible but fail in predictable ways. The fixes:

## 1. Score clustering → reasoning before score

- **Symptom:** ask for a bare score and the model defaults to safe middling values (the lesson's "always a 6").
- **Fix:** require **strengths → weaknesses → reasoning → score**, in that order. Anthropic docs: *"Ask the LLM to think first before deciding an evaluation score… increases evaluation performance, particularly for tasks requiring complex judgement."*
- ⚠️ Specific "+10–15% improvement" figures sometimes quoted are **not** in Anthropic's docs (correction; see [[prompt-evaluation/source-provenance]]). The *direction* is documented; the magnitude is not.

```python
# Reasoning-first graded scoring (current model IDs)
prompt = f"""Grade this answer against the rubric.
<rubric>{rubric}</rubric>
<answer>{answer}</answer>
1. Identify specific strengths
2. Identify specific weaknesses
3. Reason against each rubric criterion
4. THEN output a single score 1-10
Respond as JSON: {{"strengths":"...","weaknesses":"...","reasoning":"...","score":7}}"""
resp = client.messages.create(model="claude-opus-4-8", max_tokens=1024,
                              messages=[{"role":"user","content":prompt}])
```

## 2. Position / verbosity / self-preference bias

- **Pairwise judging is unstable:** preferences **flip in ~35% of cases** when you swap A/B order, vs only **~9%** for pointwise absolute scoring (arXiv 2504.14716). 
- **Fix (pairwise):** run the judge **twice in opposite orders** (A,B) and (B,A); only credit a winner if it wins **both** orderings (JudgeBench).
- **Implication:** for most needs, prefer **pointwise** (score each output independently against a rubric) over pairwise comparison.

## 3. Output reliability → Structured Outputs

- The lesson extracts JSON via **prefill `\`\`\`json` + stop sequence** — works, but can still mis-parse.
- The **Structured Outputs API guarantees schema-compliant JSON via constrained decoding** — *"JSON is guaranteed to match the schema."* No parse errors. Use it for production graders.

## 4. Grader-model choice

- Anthropic example code notes it's *"generally best practice to use a different model to evaluate than the model used to generate."* ⚠️ This is an incidental code comment, **not** a formally benchmarked recommendation (verdict: *partially-supported*).
- Practical read: a **stronger grader** (Opus) judging a weaker generator (Sonnet/Haiku) is reasonable; JudgeBench shows judge accuracy climbs from ~55% (base) → ~73% (rubric + chain-of-thought) → ~81% (top reward models).

## 5. Consistency aids

- **Few-shot examples** in the grader prompt raised one study's GPT-4 judge consistency from **65.0% → 77.5%** (Confident AI). Include 2–3 "good vs bad" graded examples.
- **Detailed, modular rubrics** beat one vague holistic ask. Nested-rubric schemes (Complete Rubric Evaluation / Pointwise Rubric Evaluation, arXiv 2503.23989) score sub-criteria separately, forcing differentiation.

## 6. ⚠️ Temperature 0 ≠ determinism

- Even at `temperature=0`, *"a zero temperature did not guarantee identical outputs across every run, route, or backend implementation."* Claims of "100% deterministic at temp 0" are **unsupported** (correction). 
- **Mitigation:** run each grade 2–3× and take the **median**; flag low-confidence scores for human review.

## Calibration discipline

Trust a model grader only after checking it against humans on a sample: do its scores track yours? Where it diverges, that's where to add rubric detail or few-shot examples. (⚠️ Specific inter-rater thresholds like "Cohen's κ ≥ 0.6" floating around the web were **not** found in Anthropic's docs — don't cite them as Anthropic guidance.)

## Key Takeaways

- Reasoning-first kills score clustering (documented, magnitude not).
- Pairwise flips ~35% vs ~9% pointwise — prefer pointwise, or swap-and-require-agreement.
- Structured Outputs > prefill-and-parse for guaranteed JSON.
- Stronger-grader-than-generator is sensible but not a hard Anthropic rule.
- Few-shot + detailed rubrics raise consistency; temp 0 is not deterministic — median-of-N + calibrate against humans.
