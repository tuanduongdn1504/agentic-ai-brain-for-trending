# Contrarian stances — what Lopopolo positions against

> Lopopolo's explicit oppositions to industry norms. Each stance is a load-bearing argument and a testable position — community pushback or counter-evidence belongs in this article via "Counter-evidence" subsections.

## 1. Manual implementation by engineers

Lopopolo banned his team from touching code editors. He calls it **"borderline negligent"** for teams not to operate at $2-3K/day token throughput as a labor replacement.
- *talk · podcast*
- **Pushback to anticipate:** small teams, regulated industries, codebases with unusual constraints
- **Counter-evidence target:** teams shipping equivalent quality with traditional manual coding — does productivity gap close at certain task profiles?

## 2. Synchronous pre-merge code review

Calls pre-merge review **"low signal"** and the primary remaining bottleneck. Argues for **post-merge code review** + durable automated guardrails.
- *talk [08:19] · cross-medium agreement #3*
- **Tension:** standard SOC2 / ISO compliance frameworks require pre-merge approval gates
- **Counter-evidence target:** defect-cost data from teams that adopted post-merge model

## 3. Human-centric repository architecture

Positions against monolithic folders, MVC-style decomposition without strict isolation, "human habit" structures. Advocates extreme modularity (750 isolated packages cited as exemplar).
- *talk · podcast [01:12:24]*
- **Tension:** classical "premature abstraction" warning; package-explosion overhead in non-agent contexts
- **Counter-evidence target:** comparative case studies on hyper-modular vs monolithic for human + agent hybrid teams

## 4. Code as "burden"

> "Code is free... infinitely parallel"

Dismisses the long-held belief that more code = more maintenance liability. Argues agents handle refactor/delete without human effort, so the burden assumption no longer holds.
- *cross-medium agreement #1*
- **Pushback:** even if production cost is zero, cognitive cost for human reviewers (and downstream agents) is non-zero
- **Counter-evidence target:** signal-to-noise studies on agent-generated codebases over time

## 5. Predefined agent scaffolds

Positions against "scaffolding" school where agents are placed in **"boxes with a predefined set of state transitions"**. Argues the modern reasoning-model harness should let the model choose its own tools and execution paths — **"the harness be the whole box"**.
- *talk · podcast*
- **Tension:** opposes much of the "agent framework" ecosystem (LangGraph, CrewAI, etc.)
- **Already a tension axis** in [[external|workflow-ai-coding/_index]] (skills-over-agents architecture vs framework-driven)

## 6. Standard software dependencies

Agrees with Bret Taylor that **"software dependencies are going away"**. Targets the **"bloat"** and **"overhead"** of **"bullshit plugins"** — argues agents should vendor only the lines actually needed.
- *talk [26:00, 27:00]* · *Bret Taylor cited*
- **Tension:** opposes ecosystem-scale dependency networks (npm, PyPI, etc.)
- **Bounded by:** [[open-questions#5]] (Datadog/Temporal complexity ceiling)

## 7. Optimizing tools for human legibility

Recounts an anecdote of building a visual debugging tool for a human — **"wrong"** — because it kept a human in the loop unnecessarily when an agent could parse raw trace data directly.
- *talk*
- **Implication:** tooling investment should default to agent-readable formats first, human visualization second
- **Tension:** developer-experience traditions, accessibility, debuggability when agents fail

## 8. Model Context Protocol (MCP)

> "pretty bearish on" MCP

Argues MCP **"forcibly injects all those tokens in the context"** and **"messes with auto compaction"**, causing agents to "forget" how to use tools.
- *podcast*
- **Direct conflict** with Anthropic-aligned tooling thesis covered in [[external|telegram-remote-control-stack/_index]]
- **High-priority research follow-up:** Anthropic's response or measurement of the same phenomenon; this is a community-level disagreement

## 9. Passive "Plan Mode" approvals

Warns that humans approve plans without reading them, **"effectively potentially wasting time on a rollout with instructions that like are bad"**.
- *podcast [31:00]*
- **Tension:** plan-mode is a maturity pattern in Anthropic's [[external|workflow-ai-coding/_index]] coverage — direct disagreement axis

## 10. Long-running migrations

> "there's never going to be a migration that hangs open for six months... we can finish them now"

Rejects the industry default of multi-month migrations as artifact of human-bandwidth limitation, not technical necessity.
- *podcast*
- **Counter-evidence target:** post-mortem of any harness-engineered migration that DID hang open — does the prediction hold or fail?

## How to extend

When future ingests find counter-evidence or community pushback:
1. Add `### Counter-evidence YYYY-MM-DD` subsection under the relevant stance
2. Quote the source verbatim where possible
3. Don't soften Lopopolo's position retroactively — preserve the original strong claim AND the counter

These stances form the **disagreement axis** for the broader harness-engineering research thread. A topic with no live disagreements is a closed thread — the more counter-evidence accumulates here, the more this topic remains a valuable research surface.

---

## External counter-stances from sibling drains (added 2026-05-30)

Stances that are NOT from Lopopolo but constitute live counter-positions to broader harness-engineering consensus surfaced in sibling drains. These belong here because they shape the disagreement axis for the topic as a whole.

### 11. John Kim — "very very hard to NOT use MCPs" (anti-MCP stance, corpus-strongest)

> "I try very very hard to not use MCPs"

Meta Staff Engineer position from [[getting-started-consensus-and-divergences]] §Divergences-3. Argues MCPs "blow up your context window" and token usage. Prefers writing manual scripts for validation.

- *Source: John Kim "How I use Claude Code (Meta Staff Engineer Tips)" — 2026-02-07, 435K views*
- **The corpus-strongest minority position** against otherwise unanimous MCP-as-default consensus (N=4 of 6 in 2026-05-30 drain + the entire 2026-05-29 claude-cowork corpus advocate MCP heavily)
- **Composes with Lopopolo's MCP stance** (§9 above) — both org-scale (Lopopolo) and personal-scale (Kim) articulate MCP-token-injection concerns. N=2 across scales adds confidence the concern is real.
- **Counter-evidence target:** quantitative measurement of token-budget impact per MCP. If MCP overhead is <5% of context per turn, concern is overblown. If >20%, Kim's position becomes the default for high-volume agent work.

### 12. Tù Bà Khuỳm — anti-Markdown / pro-SQLite memory (V2 harness, corpus-first)

Documented in [[personal-repo-tu-ba-khuym-getting-started]]. V2 harness moves away from Markdown for project memory; uses SQLite for project decisions + agent action traces + friction logs.

- *Source: Tù Bà Khuỳm "Bắt đầu Harness Engineering từ đâu? Từ đây!!" — 2026-05-30, 469 views*
- Stated rationale: SQLite is **more precise** and **less prone to being ignored or filled incorrectly** by the agent compared to a text file
- **Counter-position to:** the cross-corpus Markdown consensus (N=14+ across org-scale + individual-scale articles)
- **Counter-evidence target:** does SQLite scale beyond single-laptop / single-operator? Multi-machine sync + schema migration + cross-project sharing unaddressed (see [[open-questions]] §11-14)

### 13. Productive Dude / Avthar — pro-proprietary-framework-branding (3 acronyms in 1 drain)

2026-05-30 drain surfaced **3 competing proprietary prompting frameworks** in a single ingest:

| Framework | Source | Scope |
|---|---|---|
| **GCAO** | Productive Dude | Goal · Context · Action · Output |
| **DBS** | Productive Dude | Direction · Blueprints · Solutions (for Skills) |
| **PSB** | AI with Avthar | Plan · Setup · Build (for project lifecycle) |

This is itself a corpus signal: harness-engineering content is at the **proprietary-framework-branding** maturity stage. Distinct from:
- Mnilax's 12-rule CLAUDE.md (numbered behavioral contract)
- Anthropic's 7-component decomposition (from [[anthropic-large-codebases-anchor]])
- Lopopolo's terminology set (from [[terminology]])

The vault's own posture is **closer to rules + phases** than to 3-letter-acronyms — engineering-discipline branding rather than marketing branding.

- **Counter-evidence target:** N=2+ adoption signal for any single framework outside its creator's direct audience would suggest the framework is becoming load-bearing rather than personal-brand-driven.
