# Source provenance & verification log

> **Why this article exists:** the autopilot-research constitution forbids fabrication (invariant #4). This logs exactly what was ingested, what was verified against first-party sources, and what the adversarial pass **corrected or threw out**.

## The sources

| | |
|---|---|
| **Entry-point video** | [nYMcPrnRzhI](https://www.youtube.com/watch?v=nYMcPrnRzhI) — BizMate AI Official, Vietnamese dub: "CHẤM ĐIỂM BẰNG AI \| Building with Claude — Bài 17", 601s, uploaded 2026-06-16 |
| **"Original resource" video** | [GjakSOir2dE](https://www.youtube.com/watch?v=GjakSOir2dE) — re-upload of the **original English** audio (`en-orig` captions), 601s, placeholder title |
| **Canonical original** | Anthropic **"Building with the Claude API" → Prompt Evaluations** course, model-graded lesson — [github.com/anthropics/courses](https://github.com/anthropics/courses/blob/master/prompt_evaluations/README.md) |
| **Transcript capture** | `raw/2026-06-16-grading-with-ai-lesson17.md` (yt-dlp `--write-auto-subs`, en-orig, srv1→clean) |

Both videos are the **identical 601-second lesson** — confirmed by exact duration match + content. Video 1 is BizMate's localization; Video 2 is the original English audio.

## Verification method

Adversarial Workflow `wf_dd6c7095-c76` — **16 agents**, 6 research facets (courses repo, official docs, LLM-as-judge methodology, code grading, eval tooling, agent/RAG). Each facet's claims were **independently fact-checked** against the cited `source_url` by a second skeptical agent (verdicts: supported / partially-supported / unverifiable), then a completeness critic reviewed coverage. ~520s, 230 tool calls.

## ✅ Verified-supported (high confidence)

- Three grader types (code / model / human) — cookbook + docs.
- Reasoning-before-score increases eval performance — Anthropic docs (direction confirmed).
- 8 success-criteria dimensions; "20–50 from real failures"; "prioritize volume over quality"; "show your prompt to a colleague" — docs, verbatim.
- 9-lesson Prompt Evaluations course structure — courses README.
- Pairwise flips ~35% vs ~9% pointwise (arXiv 2504.14716); JudgeBench 55→73→81%; few-shot 65→77.5% (Confident AI); Structured Outputs guarantees schema; RAGAS 4 metrics; pass@k/pass^k.

## ⚠️ Corrected / rejected during verification

| Claim (as first drafted) | Correction |
|---|---|
| Cookbook uses `claude-opus-4-8` | Cookbook actually uses **`claude-opus-4-1`**. (Current models are Opus 4.8 / Sonnet 4.6 / Haiku 4.5 — used in *our* runnable examples, accurately labeled.) |
| Aggregation uses `statistics.mean` | Cookbook uses **`sum(grades)/len(grades)*100%`** — no `statistics` import. |
| `ast.parse()` proves code is executable | **False.** It catches obvious syntax errors only; `compile()` can still raise; bare `return 42` parses but isn't valid. |
| 5 success-criteria dimensions | Anthropic lists **8** (privacy preservation + context utilization are separate, not folded into "operational"). |
| Model graders use `<result>` tags | Cookbook uses **`<correctness>`** tags (docs example uses `<result>`); both valid, tag name differs by source. |
| "Reasoning before score gives +10–15%" | Anthropic confirms the *effect*, **not** any percentage. |
| "Promptfoo acquired by OpenAI, March 2026" | **No source.** GitHub only says "used by OpenAI and Anthropic." Likely fabricated. |
| Temperature 0 → 100% deterministic | **Unsupported** — temp 0 does not guarantee identical outputs across runs/routes/backends. |
| DeepEval "3M downloads / 20M daily evals"; a "Latitude" OSS tool; Cohen's κ≥0.6 as Anthropic guidance; "PREPAIR" framework; RAG citation 65–70% baseline | **Unverifiable** from the cited sources — excluded. |

## Provenance caveats

- The original English lesson lives on **Anthropic's course platform**; the YouTube copies are third-party re-uploads/localizations. Treat the [anthropics/courses](https://github.com/anthropics/courses) repo as the authority.
- Several deep-dive facts come from **non-Anthropic** sources (arXiv, JudgeBench/EmergentMind, Confident AI, RAGAS). They're cited as such — they corroborate, they're not Anthropic doctrine.

## Key Takeaways

- Two YouTube videos = one Anthropic lesson; the real original is the courses repo.
- The lesson's *core* (3 grader types, reasoning-before-score, decide-criteria-upfront) is fully first-party-verified.
- The adversarial pass removed a fabricated acquisition, a wrong model ID, an `ast.parse` over-claim, and several unverifiable stats — exactly the no-fabrication discipline this vault requires.
