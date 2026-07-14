# pydantic-ai-2 — Topic Index

> **Topic:** Pydantic AI's v2.0 release and its new single organizing primitive, the **capability** — a composable bundle of instructions, tools, lifecycle hooks, and model settings, replacing scattered 1.0-era constructor kwargs
> **Source video:** [Pydantic AI 2.0: The New Best Way to Build AI Agents is Composing Capabilities](https://www.youtube.com/watch?v=PY7xIxybYNc) (`PY7xIxybYNc`), Cole Medin (@ColeMedin), 2026-07-10, 15:00, ~19.6K views, 216K subs at ingest — **first-party** framework coverage, no code/repo of his own beyond the demo repo he built for the video
> **Compiled:** 2026-07-14 (path 5 yt-dlp + Workflow `wf_01eb5573-0b3`, 18 agents = 7 dives + 10 refute-first verifiers + 1 completeness critic; ~737K tokens, 171 tool calls, 0 errors) + 1 main-loop follow-up fetch to resolve a critic-flagged contradiction

## Articles

- [[overview]] — release facts, the demo repo, and where Cole Medin sits in this corpus (his 3rd appearance)
- [[capability-primitive-and-mcp-framing]] — the capability definition (CONFIRMED) and the one MISLEADING claim: MCP servers aren't really "a subset of" a capability
- [[progressive-disclosure-and-skills-lineage]] — real UX-parity with Anthropic Agent Skills, but not spec-parity (a third-party adapter is needed for agentskills.io compliance)
- [[lean-core-vs-harness-and-monty]] — the core/harness split, and the Monty sandbox contradiction the workflow's own critic caught and this pass resolved
- [[v1-to-v2-composability-claim]] — why "1.0 had no composability" overstates a real (but narrower) 1.0 limitation
- [[langchain-crewai-comparison]] — the one pure-opinion claim in the video, dressed as a technical differentiator
- [[nimbalyst-sponsor-fact-check]] — the sponsor's real name (auto-captions garbled it as "Nimble list") and where its "100% local" framing quietly excludes its team tier
- [[claims-scorecard]] — the full 10-claim ledger + the verifier-discipline notes
- [[source-provenance]] — ingestion path, workflow stats, known gaps

## One-line thesis

A technically credible, first-party framework update covered by a repeat corpus presenter (Cole Medin) with a clean track record — every mechanism he demos is real and reproducible (the capability primitive, its docs, his own before/after demo repo, the Monty sandbox), and the only errors are the corpus's familiar shape: a backwards containment metaphor (MCP-as-subset), a dropped clause in a quote, an overstated 1.0 limitation, an unqualified sponsor "100% local" claim, and one pure-opinion competitive claim — zero false or fabricated claims.

## Pilot relevance

Lightweight note in `output/(C) 2026-07-14-pydantic-ai-2-pilot-note.md` — the **capability** pattern (bundle instructions + tools + hooks + settings into one reusable, progressively-disclosed unit) is a useful *conceptual* pattern for structuring hireui's planned Match-Explain LLM feature's system-prompt/tool/guardrail composition, independent of Pydantic AI's Python-only implementation (hireui is TypeScript). Not a code-level adoption candidate; a design-pattern one.

## Cross-topic links

- [[../harness-engineering/archon-harness-builder-anchor]] + [[../harness-engineering/_index]] — Cole Medin's two prior corpus appearances (Archon; Anthropic large-codebases walkthrough); this is his 3rd.
- [[../github-copilot-cli-agents/agent-skills-shared-standard]] — the prior finding (GitHub + Claude Agent Skills = same `agentskills.io` spec) this topic extends into a three-way comparison: two vendors sharing one spec, Pydantic AI converging independently on the same UX.
- [[../miai-cv-matching-agent/_index]] — this wiki's other production agent-framework source, built on LangChain's `create_agent`; the direct counter-example for the video's LangChain "less control" framing.
- [[../multi-agent-orchestration/_index]] — adjacent agent-framework/orchestration coverage.
- [[../google-ai-studio-github-import/pricing-privacy-data]] + [[../local-ai-coding-agents/_index]] — sibling "free/local" sponsor-claim-oversell findings (Nimbalyst joins the pattern).

## Key Takeaways

- **The capability primitive is real, documented, and matches Cole's on-screen explanation almost verbatim** — this isn't marketing language, it's an actual class shipped in Pydantic AI v2.0.0 (released 2026-06-23).
- **The one architectural error is a backwards metaphor, not a fabrication:** capabilities wrap MCP servers as one tool source among several; MCP servers aren't literally "a subset of" a capability.
- **Progressive disclosure is genuinely UX-equivalent to Anthropic's Agent Skills — even Pydantic's own docs say so — but it's an independent implementation, not the same portable spec**; a third-party adapter (`pydantic-ai-skills`) exists specifically to bridge the two.
- **The Monty sandbox is real and does power code mode**, but ships in a separately-versioned package (`pydantic-ai-harness` v0.6.0, released one day before this video) rather than bundled into core `pydantic-ai` — resolving a contradiction the workflow's own critic caught between two verifier passes.
- **"1.0 had no composability" overstates the real 1.0 limitation** — toolsets were already reusable across agents in 1.0; what v2.0 actually unifies is the *surrounding* scattered kwargs (instrumentation, hooks, history processing), not tool reuse itself.
- **The one pure-opinion claim** ("Pydantic AI stands above LangChain and CrewAI") isn't supported by the launch article and doesn't hold up cleanly against LangChain's own middleware system — treat it as Cole's preference, not a technical fact.
- **Zero false or zero fabricated claims across 10 checked** — this sits with [[../local-ai-coding-agents/_index]] and [[../github-copilot-cli-agents/_index]] near the top of this corpus's honesty spectrum.
