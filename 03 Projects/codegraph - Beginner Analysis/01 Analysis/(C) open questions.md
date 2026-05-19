# (C) Open questions — codegraph v70 wiki build

## Identity + author profile

1. Colby McHenry's 20-repo portfolio includes shopify-graphql-admin-mcp + n8n-gcp-firebase + frontend-audit-skill — what's the unifying axis? AI-tooling-for-AI-coding-agents seems primary; but the Shopify products suggest cross-domain work. Multi-domain portfolio vs single-domain-portfolio sub-pattern question.
2. The author profile says "15+ years building software" — is this a part-time/side-project profile or a full-time/professional-product profile? 20 repos with 5K+ stars on lead product suggests serious investment.
3. Does codegraph have commercial revenue stream? MIT licensed; no sponsor/Patreon visible in README; pure OSS profile.

## Technical architecture

4. tree-sitter-wasms covers 19+ languages — what's the boundary of language coverage? CLAUDE.md mentions "TypeScript, JavaScript, Python, Go, Rust, Java, C#, PHP, Ruby, C, C++, Swift, Kotlin, Dart, Svelte, Liquid, Pascal/Delphi." Why these specific 18? Are there languages excluded by design?
5. The framework-aware route detection covers 13 frameworks (Django, Flask, FastAPI, Express, Rails, Spring, etc.). What's the framework-recognition methodology? Tree-sitter-AST patterns or heuristic-keyword-matching?
6. SQLite with FTS5 + better-sqlite3-native + wasm fallback architecture — what triggers the wasm fallback? Performance comparison?
7. "94% fewer tool calls / 77% faster exploration" benchmarks — what's the test methodology? Are these reproducible? Statistically significant? CHANGELOG doesn't enumerate benchmark suite versions.

## MCP server + multi-agent integration

8. The MCP server tools: search + context + impact + call-trace — what's the tool-count? How granular are these tools (single vs composite)?
9. Codex CLI / Cursor / OpenCode / Claude Code each have different MCP integration patterns. How does codegraph normalize across the 4 platforms? The installer handles per-platform config writes (v0.7.7).
10. v0.7.8 OpenCode installer fix (target `opencode.jsonc` not `opencode.json`) — was this a regression from v0.7.7 introduction OR was OpenCode the always-broken target?

## Pattern Library implications

11. Pattern #18 sub-mechanism B "one-binary-many-CLIENTS" has 3 evidence points now (agentmemory v66 MCP + CloakBrowser v69 CDP + codegraph v70 MCP). Should the audit formalize sub-mechanism B further into B1 (MCP variant) and B2 (CDP variant)? Or are these variants observationally equivalent?
12. OC-E Synchronicity-Discipline distinction — codegraph CLAUDE.md mandates 3-file sync (server-instructions.ts + instructions-template.ts + .cursor/rules/codegraph.mdc). v68 zero mandates examples + docs + tests aligned to current behavior. Different mechanism (config vs behavioral) OR same broader OC-E?
13. The "AGENTS.md auto-generation by installer" pattern — corpus-novel. Could become Pattern: "Tool-Authored Agent-Context-File" if N=2 emerges.
14. The "Pre-Indexed-Context-Layer" positioning vs runtime-exploration — could be NEW pattern axis OR sub-archetype within Pattern #18.
15. Pattern #19 founder-personal lineage: 20 repos for colbymchenry vs 5 for AgriciDaniel (v64) vs ~12 for rohitg00 (v66 agentmemory). What's the cardinality range? Is there a sub-mechanism for "founder with 20+ repos"?

## Quantitative-claim-marketing observation

16. codegraph leads with "94%/77%/100%" three-number marketing positioning. v69 CloakBrowser led with "0.9/Pass/30 sites." Different domains (code-graph vs stealth) but similar marketing-positioning strategy. Sister observation candidate.
17. Quantitative-benchmark-marketing-as-positioning observation: does this correlate with developer-tools archetype? Or is it broader?

## Comparison with codebase-exploration alternatives

18. Codegraph competes/coexists with grep + ast-grep + ripgrep + sourcegraph + GitHub code search + Claude Code's native Read/Grep tools. What's the niche it claims that's defensible?
19. The benchmark claim "77% faster exploration" implies a baseline — is the baseline Claude Code's default native tools, or an old codegraph version, or grep-only?
20. tree-sitter coverage gaps (e.g., shell scripting? Lua? Erlang?) — are these intentional or pending?

## Pilot candidacy

21. codegraph is potentially vault-deployable for Storm Bear (would augment Claude Code on the vault's own codebase). Is this a pilot candidate?
22. Vault hireui-harness codebase is TypeScript-heavy — codegraph supports TypeScript 95.4% primary. Strong fit for pilot.
23. Vault's wiki corpus is mostly markdown — not codegraph's target. Pilot would be narrow-scope (vault TypeScript codebase only).
24. Compared to v66 agentmemory (memory-layer pilot candidate) — codegraph is code-graph-layer pilot candidate. Different problem-domains. Could potentially pilot BOTH.

## Wiki-build process

25. MODERATE INCLUDE 2/4 STRICT for Storm Bear meta-entity — breaks v68 + v69 WEAK streak. Strength categorization continues to discriminate empirically. v70 calibration data point for v2.3.
26. The (a) FAIL is the limiting criterion — author is solo software-developer (peer to half of Storm Bear's profile). If (a) were re-evaluated with "developer-component-only-peer" relaxation, would WEAK become STRONG? Routine v2.3 calibration consideration.
27. Phase 4b PRIMARY = Pattern #18 N+1 sub-mechanism strengthening (within-pattern). Not new-pattern registration, not promotion-proposal. Sub-mechanism formalization proposal-document discipline (NEW vehicle at v70).
28. The corpus-rare observation that codegraph itself has CLAUDE.md at root — is this corpus-N=2 (other corpus subjects with CLAUDE.md at root)? Need to enumerate.
29. v70 4th-consecutive-wiki post-v69-audit-reset — does routine v2.2 expect wiki velocity to slow after audit? Or does v70 close-on-v69-audit timing suggest accelerating velocity?
30. The "interactive multi-agent installer" pattern (npx codegraph installer with platform selection) — would this generalize as a Phase 0 codification candidate for wiki probing tooling (e.g., per-platform installer pattern as Pattern #2 Distribution Evolution sub-variant)?
