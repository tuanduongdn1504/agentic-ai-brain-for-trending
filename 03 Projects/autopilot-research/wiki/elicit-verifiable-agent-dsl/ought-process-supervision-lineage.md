# Lineage — Ought, factored cognition, process supervision → Elicit

## Source

- Double deep-dive into the originals + verify (ought-lineage + elicit-company + elicit-evals verdicts, all CONFIRMED) — see [[source-provenance]].

## The decade-deep chain

| When | What | Why it matters to the talk |
|---|---|---|
| **2017** | **Ought** founded (nonprofit) by **Andreas Stuhlmüller**; core idea = **factored cognition** (decompose sophisticated reasoning into small, verifiable, mostly-independent subtasks) | The intellectual root of "make the process legible and checkable" |
| ~2022 | **ICE** (Interactive Composition Explorer), `oughtinc/ice` — Python library + trace visualizer for LM programs (~568★) | Direct ancestor of "the plan is a program you can inspect/trace" |
| **2022-04-06** | **"Supervise Process, not Outcomes"** — Stuhlmüller & Byun (ought.org) | The talk's "mechanism matters" IS this thesis: process-based systems (supervise reasoning steps) over outcome-based end-to-end optimization; safer + better differential capabilities |
| **2023-10-16** | **"Factored Verification"** (Charlie George & Stuhlmüller, arXiv:2310.10627) — automated hallucination detection in paper summaries (reductions e.g. GPT-4 0.84→0.46) | Eval/verification culture that becomes checklist item 8 |
| **2023-09-25** | **Elicit spins out of Ought** as a **public benefit corporation**, **$9M** seed | The company whose values the architecture instantiates |
| **Jan 2022** | **James Brady** joins (Ought, then Elicit) as **Head of Engineering** | The speaker; pre-spinout tenure |
| **2025-03** | Eval posts: **"How we evaluated Elicit Reports"** (17 PhD researchers; 29 Elicit vs 120 competitor reports; Wilcoxon) + **"Systematic Review"** (recall 93.6%, specificity 62.8%; extraction 94% internal / 99.4% external) | "Dedicated eval team who are great" — real, documented |
| **2025-12-09** | **Research Agents** launched — 4 workflows: competitive landscapes, research landscapes, clinical trial analyses, topic exploration | The demo's product surface ([[demo-research-landscape]]) |
| **2026-03-03** | **Elicit API** — 138M+ papers; OpenAPI 3.1.0 | Product scale |
| **2026-05-20** | **This talk** (CWC London) | ÆPL as the productized form of process supervision |
| **2026-06-30** | Research Agent upgraded; workflow-limits → **monthly usage pool** | Post-talk commercial evolution |

Leadership: **Andreas Stuhlmüller (CEO), Jungwon Byun (COO)**, James Brady (Head of Engineering).

## The through-line

- "Supervise process, not outcomes" (2022) is a *safety/alignment* thesis. ÆPL (2026) is its *product engineering* instantiation: a legible, checkable, faithfully-executed **process** is exactly a program in a language weak enough to inspect and strong enough to run.
- Factored cognition → the ÆPL program IS a factoring: named steps (search / join / enrich / curate) composed into a plan other agents can critique.
- This makes Elicit a rare case where a company's alignment research and its shipping architecture are the *same idea* at two altitudes — the official description's "architectural choices as concrete instantiations of company values" is literally true, with a paper trail.

## Cross-links

- Process-vs-outcome supervision echoes the corpus's "verify intent not surface" (Rule 9 in vault CLAUDE.md) and the eval-anchor discipline in [[../prompt-evaluation/_index]].
- Contrast with outcome-graded RL agents and freeform loops: [[../pocock-agentic-workflow/_index]], [[../harness-engineering/_index]].

## Key Takeaways

- ÆPL is not a 2026 invention out of nowhere — it's a 2017-rooted alignment agenda shipped as product architecture.
- "Mechanism matters" = "Supervise Process, not Outcomes," restated for a customer audience.
- Elicit's eval practice is independent of the DSL and predates it — verification is org DNA, not a feature.
- The lineage is a credibility signal: the talk's claims sit on a public, dated, primary-source trail (Ought blog, arXiv, Elicit blog).
