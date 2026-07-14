# Claims scorecard

10 claims, independently re-verified against first-party sources (refute-first — each verifier fetched sources itself rather than trusting the dive team). **2 CONFIRMED / 6 CORRECT-BUT-INCOMPLETE / 1 MISLEADING / 1 OVERSIMPLIFIED / 0 FALSE / 0 FABRICATED.**

| # | Claim | Verdict | Article |
|---|---|---|---|
| 1 | Pydantic AI shipped a 2.0 release built around a new single primitive, "capability" | **CONFIRMED** | [[overview]] |
| 2 | A capability bundles instructions, tools, lifecycle hooks, and model settings into one composable unit | **CONFIRMED** | [[capability-primitive-and-mcp-framing]] |
| 3 | Capabilities are "a layer above MCP servers" — MCP is a subset of what you add to a capability | **MISLEADING** | [[capability-primitive-and-mcp-framing]] |
| 4 | Progressive disclosure ("just like skills in Claude Code, Codex, GitHub Copilot") | **CORRECT_BUT_INCOMPLETE** | [[progressive-disclosure-and-skills-lineage]] |
| 5 | Two layers: "lean core" (thinking/web search/tool search) vs "harness" (e.g. code mode) | **CORRECT_BUT_INCOMPLETE** | [[lean-core-vs-harness-and-monty]] |
| 6 | Monty is Pydantic's own lightweight open-source sandbox for code mode | **CORRECT_BUT_INCOMPLETE** | [[lean-core-vs-harness-and-monty]] |
| 7 | Launch article literally says "Just point your coding agent at the capabilities docs" | **CORRECT_BUT_INCOMPLETE** | [[overview]] |
| 8 | Nimbalyst (sponsor) is free, open-source, 100% local, no lock-in, nothing to sign up for | **CORRECT_BUT_INCOMPLETE** | [[nimbalyst-sponsor-fact-check]] |
| 9 | Pydantic AI 1.0 had "no organization and no composability" | **CORRECT_BUT_INCOMPLETE** | [[v1-to-v2-composability-claim]] |
| 10 | Pydantic AI "stands above" LangChain and CrewAI on customizability/control | **OVERSIMPLIFIED** | [[langchain-crewai-comparison]] |

## Reading the pattern

Zero claims were false or fabricated. The one MISLEADING claim (#3) gets a real architectural relationship backwards (capability-wraps-MCP, not MCP-as-subset-of-capability) rather than inventing something — an easy mental-model slip when explaining your own product live. The OVERSIMPLIFIED claim (#10) is pure opinion dressed as a technical differentiator. Everything else is CORRECT_BUT_INCOMPLETE: real mechanisms, described accurately, missing one caveat each (harness ships as a separate versioned package; the vendor-parity comparison is UX-parity not spec-parity; a quote drops its own second clause; a sponsor's "100% local" quietly excludes its team tier; "no composability" overstates a real 1.0 limitation).

This lands close to [[../local-ai-coding-agents/_index]] and [[../github-copilot-cli-agents/_index]] on the corpus's honesty spectrum — a technically credible presenter whose small errors are all in the direction of enthusiasm, not deception.

## Verifier-discipline note (Rule 12 — fail loud)

The workflow's own completeness critic flagged a real contradiction in the first pass on claim #6 (Monty): one dive found Monty's README still says "will (soon) be used" while a verifier found a separate package marketing it as already shipped. Rather than picking a verdict and moving on, this was resolved with one additional main-loop WebFetch (see [[lean-core-vs-harness-and-monty]] for the resolution: it ships in `pydantic-ai-harness` v0.6.0, released 2026-07-09 — one day before the video — while Monty's own README is simply stale). Separately, the critic's own claim tally had a minor off-by-one (mislabeled claim #10 as "#9" and dropped the real claim #9 from its count) — noted here rather than silently corrected, since a critic's own arithmetic slip is itself worth recording per this project's fail-loud discipline.

## Source-checking note

Cross-referenced against the video's own transcript (read in full in the main loop, not just the dive/verify agents' summaries) to confirm claim #4 — the Claude Code/Codex/GitHub Copilot comparison is Cole's own on-screen wording, not something a verifier synthesized from external sources.
