# multi-agent-orchestration

> **Topic index.** Coordinator / hub-and-spoke multi-agent orchestration, taught by ExamPro's "Claude Architect" video and traced back to the three Anthropic engineering writings it's built on.
> **Source:** ExamPro "Claude Architect: Multi-Agent Orchestration" — Andrew Brown / ExamPro (third-party paid course, [exampro.co/cca-f](https://www.exampro.co/cca-f)), [vRYBG_R8JAI](https://www.youtube.com/watch?v=vRYBG_R8JAI), 2026-04-29, 2h9m. **NOT first-party Anthropic.** Compiled 2026-06-20 (path 5 yt-dlp transcript + a deep-dive/verify Workflow `wf_d77d2e85-2dc`, 24 agents).
> **What's verified vs. third-party framing:** [[multi-agent-orchestration/source-provenance]].

## Why it's here

A 2h9m live vibe-build of a hub-and-spoke **coordinator** (a job-application screener), walked through 10 stages from "what is hub-and-spoke" to "port it to the Claude Agent SDK." It's a clean, concrete demonstration of patterns that are **lifted from Anthropic's own canonical writings** — so this topic does double duty: capture the video's teaching, *and* deep-dive the originals behind it (the user's explicit ask). The worked example — a **job-application screener** — is also a near-1:1 analog for an agentic feature in [[external|Storm Bear: hireui]] (the user's Goal #2), which is why the pilot-methods file leans on it.

## Articles

**Video knowledge (what the video teaches):**

- [[multi-agent-orchestration/overview]] — the map: hub-and-spoke, the coordinator's jobs, the 10-stage arc, source lineage, pedagogical caveats.
- [[multi-agent-orchestration/hub-and-spoke-and-coordinator]] — the architecture + coordinator's 4 jobs + the basic build + the MAX-STEPS loop guard (sections 1–3).
- [[multi-agent-orchestration/decomposition-and-partitioning]] — narrow-decomposition failure (the EV-market example) + safeguard tools, dynamic selection, research partitioning, the planner-vs-coordinator split (sections 4–6).
- [[multi-agent-orchestration/refinement-and-observability]] — the refinement loop (evaluator-optimizer) + observability as a choke point + productionization (sections 7–8).
- [[multi-agent-orchestration/refactoring-and-agent-sdk-port]] — refactor-for-ownership + the Agent SDK port (`@tool` + in-process MCP server) (sections 9–10).

**Original-resource deep-dives (the source material) + the bridge:**

- [[multi-agent-orchestration/building-effective-agents-deep-dive]] — Anthropic's pattern taxonomy (prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer; when *not* to use agents).
- [[multi-agent-orchestration/multi-agent-research-system-deep-dive]] — Anthropic's production orchestrator-worker system (Opus lead + Sonnet subagents; 90.2% eval gain; token economics; delegation discipline; eval rigor).
- [[multi-agent-orchestration/agent-sdk-deep-dive]] — the Claude Agent SDK (the porting target): `@tool`, `create_sdk_mcp_server`, `query()`/`ClaudeAgentOptions`, subagents, hooks, sessions.
- [[multi-agent-orchestration/video-to-original-crosswalk]] — **the bridge article**: a master table mapping each video term → the canonical Anthropic pattern → its original source, plus what the video adds / simplifies / omits.
- [[multi-agent-orchestration/source-provenance]] — verification log: source tiers, what's confirmed, what's third-party framing, what was stripped (a fabricated CCA-F-exam framing + a cross-topic "Blobotomy" leak).

## Apply it

Pilot methods (16 ranked, across knowledge-pipeline / hireui Goal-#2 / Claude-Code-harness / Scrum-coaching): `output/(C) 2026-06-20-multi-agent-orchestration-pilot-methods.md`.

## Status & gaps

- **Sources:** the video (full transcript) + the three Anthropic originals (fetched + verified) + the Claude Code sub-agents docs. Bulk pattern content is well-corroborated (video ↔ first-party originals agree).
- **Gap — adversarial counter-example:** no "when hub-and-spoke is the wrong choice" article yet. The crosswalk's section (C) "what the originals cover that the video omits" partially fills this (start-simple, when-not-to-use-agents).
- **Gap — SDK specifics drift:** exact Claude Code subagent details (frontmatter fields, nested-subagent depth, version numbers) are from a single doc fetch and flagged in [[multi-agent-orchestration/source-provenance]] — re-verify against current docs before relying on them.
- **Promotion note:** strong companion to [[harness-engineering/_index]] + [[agentic-analytics-harness/_index]]; consider as Storm Bear Pattern-Library evidence (orchestrator-workers / adversarial-review) at the next mini-audit cadence.

## Cross-links

[[harness-engineering/_index]] (parent discipline) · [[agentic-analytics-harness/_index]] (a *production* multi-agent harness; the "don't fragment knowledge across agents" lesson lives there, not here) · [[prompt-evaluation/_index]] (eval-first) · [[claude-api-cost-optimization/_index]] (the token-cost discipline the video omits) · [[ai-operating-system/_index]] · [[claude-md-12-rules/_index]] (Rule 5 = coordinator-as-judgment).
