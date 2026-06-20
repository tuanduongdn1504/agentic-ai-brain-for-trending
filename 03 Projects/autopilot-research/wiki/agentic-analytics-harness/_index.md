# Topic: agentic-analytics-harness

> **What:** How **Omni** (a BI/analytics platform) built **"Blobby"** — a production agentic analytics assistant **powered by Claude and built with Claude Code** (99% of platform code). A case study in *product* harness engineering, told by Cofounder & CTO **Chris Merrick** at **Code with Claude: Extended London (2026-05-20)**.
> **Why it matters here:** The corpus's **first *product/analytics* harness** — every prior [[harness-engineering/_index|harness-engineering]] article is about *coding* agents. Omni shows the same discipline applied to an end-user feature that runs **103.3B tokens/month** in production.
> **Compiled:** 2026-06-20 · path-5 yt-dlp (⚠️ **caption-gap** — see [[agentic-analytics-harness/source-provenance|source-provenance]]) + first-party Omni blogs + talk recap.

---

## Articles

| Article | What it covers |
|---|---|
| [[agentic-analytics-harness/overview]] | The talk, Blobby, the numbers table, the 5 engineer-applicable principles, the 5 production lessons |
| [[agentic-analytics-harness/multi-agent-architecture]] | Coordinator + summarization sub-agent, the two-loop structure (50-iteration outer loop), conversation-memory rebuild, **"Blobotomy 1" split-brain** lesson |
| [[agentic-analytics-harness/tool-design-and-sizing]] | Tool design + sizing, **4 core tools → 45-tool portfolio**, **"Blobotomy 2" SQL-over-custom-format** (3–4 attempts → 1), Arrow→CSV |
| [[agentic-analytics-harness/semantic-layer-as-context]] | The semantic layer as "intelligence backbone", `ai_context`/`sample_values`/`synonyms`/`descriptions`, 3 injection levels, ~200k/175k char budget, feedback loop |
| [[agentic-analytics-harness/evals-and-error-recovery]] | **Error recovery = highest-ROI lever**, strict validation/guardrails, evals (LLM-as-judge + 8-criteria benchmarks + daily session triage), observability-over-scorecards |
| [[agentic-analytics-harness/source-provenance]] | ⚠️ Caption-gap disclosure, T1-first-party vs T2-talk-recap tiering, the 4-vs-45-tools reconciliation, what's verified vs single-source |

## Pilot methods

How to apply this to the operator's working flows (knowledge pipeline / hireui / Claude Code harness / Scrum coaching): **`output/(C) 2026-06-20-agentic-analytics-harness-pilot-methods.md`** — 14 ranked methods.

## Cross-links

- [[harness-engineering/_index]] — parent discipline; Omni = first **product-domain** harness case study (candidate sibling/promotion evidence at next audit).
- [[claude-api-cost-optimization/_index]] — Omni's prompt-caching + Haiku/Sonnet routing are the same levers, *measured in production*.
- [[prompt-evaluation/_index]] — Omni's LLM-as-judge + 8-criteria benchmark construction + session triage extend the grading discipline.
- [[ai-operating-system/_index]] · [[claude-cowork/_index]] — sibling "build an agent that talks to your data/tools" framings.
- [[claude-md-12-rules/_index]] — "colocate context with definitions" and "model-native formats" echo the 12-rule read-before-write / simplicity rules.

## Status & gaps

- **N=1 case study, single talk.** Rich, but one company.
- **⚠️ No verbatim transcript** (video uncaptioned) — bulk verified against Omni first-party blogs; talk-specific numbers (45 tools, 50 iterations, 5 "Blobotomy" cycles, 8 eval criteria, Haiku→Sonnet date) are **single-source (recap)**, flagged in [[agentic-analytics-harness/source-provenance]].
- **Gap:** no first-party confirmation of the exact tool count / iteration cap / eval criteria. Optional adversarial-Workflow verification pass available.
