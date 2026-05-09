# Terminology — terms Lopopolo introduces or redefines

> Each term below is defined as Lopopolo uses it. Other articles in this wiki link here via `[[terminology#term-anchor]]`. When a future ingest contests a definition or proposes a competing one, append a "Variant definitions" subsection — don't overwrite.

## Harness engineering

The discipline of optimizing an entire codebase, workflow, and organizational structure around **agent legibility** and **agent autonomy** rather than human ergonomics. The "harness" is the surrounding system (build, repo structure, observability, skills, governance) within which a reasoning model operates.
- *anchor: synthesis "Concepts & terminology"*
- Adjacent (not synonym): "agent infrastructure", "agentic harness", "scaffolding" (which Lopopolo positions AGAINST — see [[contrarian-stances]])

## Token billionaire

An engineer (or team) operating at ~1B tokens/day in agent inference, treating token-cost as commodity rather than scarce resource. Lopopolo argues this throughput is **the operating point** where harness engineering becomes effective; below it, gains are illusory.
- *talk · podcast (cost figures)*
- See claim #2 in [[core-claims]]

## Symphony

OpenAI's internal **Elixir/Beam-based orchestration layer** that coordinates hundreds of concurrent coding agents — supervises long-running agent processes, reworks failing outputs, schedules across repos. Choice of Elixir cited as load-bearing: native process supervision + GenServers handle the concurrency primitive natively.
- *talk [32:00, 45:07]* · *podcast (technical justification)*
- **Status:** internal at OpenAI; exposed to enterprises via [[#frontier|Frontier]]

## Frontier

OpenAI's **enterprise platform** for deploying observable, governable, safe agents at scale. Wraps Symphony + safety specs + observability + governance tooling so external companies (Stripe, Snowflake, Brex cited as target profile) can adopt agentic workflows with auditability.
- *talk [01:03, 01:02:05]*
- Lopopolo's team is "Frontier Product Exploration"

## Ghost libraries (≈ spec-driven software)

A method of distributing software as a **high-fidelity specification** rather than source code. The agent reproduces the system locally from the spec — no original source needs to ship. Term used interchangeably with "spec-driven software" in the anchor.
- *podcast (primary)* · *talk*
- **Open:** at what spec fidelity does this break down? Anchor doesn't say.

## Agent-legibility

Architectural principle: structure code, packages, and documentation so AI models can **easily parse and reason about** them. Concretely manifests as: hyper-modular packages (claim #5), explicit ADRs as breadcrumbs, agent-targeted markdown files (`agents.mmd`, `core_beliefs.md`), CLI-over-GUI tool choices.
- *cross-medium agreement #4*
- **Antonym (Lopopolo's term):** "human habit" architecture

## Dark factory

Internal nickname for OpenAI teams operating with **zero human-written code AND no human pre-merge review**. Evocative of unstaffed manufacturing floors. Distinct from "lights-out" because humans still steer at the system-design layer.
- *talk · synthesis*

## Ralph loop

Iterative protocol: agent A implements a spec, agent B reviews implementation against an upstream reference, the spec is updated, repeat until high-fidelity reproduction. Named in podcast; talk references the same pattern without the name.
- *podcast (primary citation)*
- Cross-link: [[external|workflow-ai-coding/_index]] also covers a "Ralph Wiggum loop" pattern attributed to Geoffrey Huntley — same idea or convergent? **Open question.**

## Skills

Reusable, prompt-injected primitives encoded into the repository that teach agents how to perform specific actions (launch dev stack, resolve merge conflict, run smoke test). Lopopolo's team uses **5–10 skills** as a tight, curated set — explicitly opposed to large skill libraries.
- *talk · podcast*
- Cross-link: [[external|claude-code-hooks/_index]] (different mechanism — hooks are deterministic shell, skills are prompt-injected) and [[external|workflow-ai-coding/_index]] (skills-over-agents architecture)

## Isomorphic (to human engineers)

Lopopolo redefines this mathematical term to mean: a model whose end-to-end software-engineering output is **functionally equivalent** to a human engineer's. He claims GPT-5.2 was the first model to clear this bar in his evaluation.
- *podcast [01:53]* · *talk [04:43]*
- Most contested term in the anchor — see claim #8 in [[core-claims]]

---

## How to extend this glossary

Future research ingests should:
- Add new terms via `## <Term>` headings, alphabetically
- Quote the original speaker verbatim where possible (citation block under the heading)
- If multiple sources define the same term differently, create a "Variant definitions" subsection rather than overwriting
- Link from this glossary to articles where the term is used heavily, so readers can see usage in context
