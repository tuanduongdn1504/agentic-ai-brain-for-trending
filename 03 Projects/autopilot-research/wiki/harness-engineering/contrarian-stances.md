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
