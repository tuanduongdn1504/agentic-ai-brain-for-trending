# (C) Ruflo — Open Questions

## Scope & positioning

1. Is Cognitum.One a legal commercial entity (LLC/Inc) or a product brand only?
2. Does Flow Nexus have paying customers yet, or is it pre-launch reference-only in README?
3. What is the Agentics Foundation's legal structure (501(c), unincorporated community, trademark)?
4. Is ruv.io AI Platform a separate product from Ruflo, or a landing page for Ruflo?
5. Why is v3.5 called "v3.5" when v3.0 → v3.5 is a 5-iteration jump (no v3.1, v3.2, v3.3, v3.4 stable)?

## Architecture

6. Are the Rust WASM kernels (policy engine / embeddings / proof system) actually shipped in the npm package, or only in @ruvector/* sibling packages?
7. How does the 313 MCP tool count stay maintainable — is there auto-generation, or is it hand-maintained?
8. Is the 5-consensus-protocol list (Byzantine, Raft, Gossip, CRDT, Quorum) fully functional, or are some stubs?
9. What fraction of the 100+ agents are "real" vs "placeholder templates"?
10. How does the 3-tier model routing (WASM / Haiku / Sonnet-Opus) handle multi-provider (Google/Cohere/Ollama) — does Haiku-tier fallback to cheapest-of-provider?

## Governance & legal

11. Does the 70+ ADR set have versioning/CI enforcement, or is it documentation-only?
12. Is there an AGENTS-vs-CLAUDE.md drift policy (both files exist at 20.7 + 38.9 KB)?
13. How is the IPFS/Pinata plugin registry governed — who decides what plugins are accepted?
14. What is the security@cognitum.one response history — any past CVE disclosures?

## Ecosystem & commercial

15. Which of the @ruvector/* packages are OSS-only vs which have commercial tiers?
16. What is the commercial relationship between agentic-flow (separate repo) and Ruflo — are they same maintainer?
17. Does the Agentics Foundation Discord have paying membership tiers?

## Learning & intelligence

18. Is SONA/EWC++/MoE actually running at sub-ms latency in production, or benchmarked in specific configs only?
19. How much of the "self-learning" is actual online-learning vs pattern-retrieval-with-boosts?
20. Is the 9-RL-algorithm claim validated with benchmarks, or only implemented?

## Storm Bear specific

21. If operator pilots Ruflo for Scrum-coaching, which of 313 MCP tools are most relevant? (Estimate top-5 for Scrum primitive-set.)
22. Is Ruflo's overhead justified for 1-person-Scrum-coach workflow, or is it enterprise-only (team of 5+)?
23. Can Ruflo + Claude Code integrate with existing vault-based knowledge management (LLM Wiki pattern)?
24. Does Ruflo's plugin marketplace accept contributed plugins from solo authors?
25. Is "Dual-Mode Claude+Codex" useful for Storm Bear, or does it double the cost without Scrum-coach value?

## Pattern library

26. Does the v27 Pattern #58 structural parallel hold at the rebrand level, or is v42 genuinely a different phenomenon (rename-with-transition vs fresh-branding)?
27. Pattern #12 refinement: if solo-heavy-governance reaches N=4+ (beyond pi-mono + claude-hud + ruflo), does original "organization correlation" formulation fully retire, or reformulate as "maintainer-philosophy + maturity" predictor?
28. Pattern #18 MCP formal-statement-update: what threshold distinguishes "MCP-heavy" (T2 GitNexus 16) from "MCP-platform-scale" (ruflo 313)? Proposed: 100+ tools = platform-scale tier.
