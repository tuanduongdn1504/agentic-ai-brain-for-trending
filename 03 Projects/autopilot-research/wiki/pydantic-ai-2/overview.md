# Overview — Pydantic AI 2.0 and the "capability" primitive

## Source

- Video: [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](https://www.youtube.com/watch?v=PY7xIxybYNc) — Cole Medin (@ColeMedin), 2026-07-10, 15:00, ~19.6K views, 216K subs at ingest.
- `raw/2026-07-14-pydantic-ai-2.md` (full transcript, yt-dlp EN auto-captions).
- Verified via Workflow `wf_01eb5573-0b3` (18 agents: 7 dives + 10 refute-first verifiers + 1 completeness critic) against first-party sources, plus one main-loop follow-up WebFetch to resolve a critic-flagged contradiction (see [[lean-core-vs-harness-and-monty]]).

## What the video claims

Pydantic AI — Cole's "favorite AI agent framework," which he's covered since January 2025 — shipped a 2.0 release that reorganizes the whole framework around one new primitive: the **capability**. A capability bundles an agent's instructions, tools, lifecycle hooks, and model settings into a single composable unit — Lego-block-style reuse across agents, replacing what Cole calls the "hodgepodge" of scattered constructor kwargs in 1.0. He walks through a demo repo (his own `orbit-support-agent`, built with both a 1.0-style and a 2.0-style implementation of the same support bot) and the official launch article's "harness vs lean core" split, then closes on the Monty sandbox project for the "code mode" harness capability.

## Release facts (CONFIRMED)

- **Pydantic AI v2.0.0** released **2026-06-23**, after 7 betas — about 2.5 weeks before this video, matching Cole's "they just put out their 2.0 release."
- Repo: [github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) — ~18.5K★, MIT license, maintained by the Pydantic organization (Samuel Colvin's company, Pydantic Services Inc). No acquisition or corporate-change claim found anywhere.
- Official launch article: [pydantic.dev/articles/pydantic-ai-v2](https://pydantic.dev/articles/pydantic-ai-v2).
- **"Capability" is a real, documented class** at `pydantic.dev/docs/ai/core-concepts/capabilities/` — not marketing copy. Its own definition matches Cole's paraphrase almost verbatim: *"A capability bundles an agent's instructions, tools, lifecycle hooks, and model settings into a single, composable unit."*
- The launch article does tell readers to point a coding agent at the capabilities docs, close to Cole's on-screen quote — the full sentence is *"point a coding agent at the [capabilities docs] and it builds most of what you need"* (Cole's paraphrase drops the outcome clause but preserves the instruction).

## Demo repo (CONFIRMED)

Cole's `orbit-support-agent` repo exists: [github.com/coleam00/orbit-support-agent](https://github.com/coleam00/orbit-support-agent), created 2026-07-05, last pushed 2026-07-10 (the same day the video went up), 9★, no license file. It genuinely contains both an `agent_v1_style.py` (1.0-era "before") and a capability-based `main.py`/`capabilities.py` (2.0 "after") — the side-by-side comparison shown on screen is real, not staged. `coleam00` is confirmed as Cole Medin's own GitHub handle (bio: "Generative AI specialist").

## Where this sits in the corpus

This is **Cole Medin's third appearance** in the autopilot wiki, after [[../harness-engineering/archon-harness-builder-anchor]] (his Archon harness-builder deep-dive) and the [[../harness-engineering/_index|harness-engineering authoritative anchor]] (his Anthropic large-codebases walkthrough). Prior verification already established: real 214–216K-subscriber educator, runs the paid **Dynamous** community (AI Agent Mastery + Agentic Coding courses), GitHub handle `coleam00`. This pass didn't need to re-derive his identity — it focused on the new technical claims about Pydantic AI 2.0 itself.

## Scorecard headline

**10 claims verified: 2 CONFIRMED / 6 CORRECT-BUT-INCOMPLETE / 1 MISLEADING / 1 OVERSIMPLIFIED / 0 FALSE / 0 FABRICATED.** Full ledger in [[claims-scorecard]]. The failure mode here is the same shape as most of this corpus: omission and imprecision, not fabrication. See [[capability-primitive-and-mcp-framing]] for the one MISLEADING claim (the MCP-servers-as-subset framing inverts the actual architecture).
