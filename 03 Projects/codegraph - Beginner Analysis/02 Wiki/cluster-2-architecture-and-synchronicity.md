# Cluster 2 — CLAUDE.md + architecture + synchronicity discipline

> Source: `CLAUDE.md` (subject's own CLAUDE.md at repo root) · fetched 2026-05-19

## Corpus-rare observation: subject has CLAUDE.md at root

codegraph ships its own `CLAUDE.md` at repo root — this is a **corpus-rare meta-recursive observation**. The vault's substrate (Claude Code) reads CLAUDE.md files; codegraph as a code-graph tool FOR Claude Code also ships a CLAUDE.md.

Corpus comparison:
- v51 agent-skills-of-vercel — skill collection (no CLAUDE.md at root since it ships SKILL.md per-skill)
- v66 agentmemory — has `AGENTS.md` but not `CLAUDE.md` (chose AGENTS.md as preferred convention)
- v68 vercel-labs/zero — has AGENTS.md (no CLAUDE.md)
- v69 CloakBrowser — no CLAUDE.md (404 at probe)
- **v70 codegraph — has CLAUDE.md at root**

Other corpus subjects with CLAUDE.md at root require enumeration; codegraph adds N to that observational track.

## Project identity (verbatim from CLAUDE.md)

> CodeGraph is "a local-first code intelligence system that parses any supported codebase with tree-sitter, stores symbols/edges/files in SQLite (FTS5)."

**Key positioning phrase:** *"extraction is deterministic — derived from AST, not LLM-summarized"*

This is **corpus-novel anti-LLM-summarization positioning** — codegraph differentiates itself from LLM-based code-intel approaches (semantic-search, embedding-based) by emphasizing deterministic AST-derived extraction. Could be NEW observational candidate: **Deterministic-AST-vs-LLM-Summarization** as product-axis.

## Core architectural pipeline

The CLAUDE.md describes the system as a sequential pipeline:

```
File-system events
        ↓
ExtractionOrchestrator (tree-sitter parsing)
        ↓
DatabaseConnection (SQLite FTS5)
        ↓
ReferenceResolver (import/name matching + framework-aware)
        ↓
GraphQueryManager (BFS/DFS traversal + impact radius)
        ↓
ContextBuilder (assemble for AI consumption)
        ↓
MCP Server / CLI / Public API (src/index.ts CodeGraph class)
        ↓
Claude Code / Cursor / Codex / OpenCode
```

**5-layer architecture** with clear separation of concerns. The public API surface is `src/index.ts` containing the `CodeGraph` class.

## Module organization (verbatim from CLAUDE.md)

- **Database layer** (`src/db/`): Dual backends using native `better-sqlite3` with transparent fallback to WebAssembly (`node-sqlite3-wasm`)
- **Extraction** (`src/extraction/`): Per-language extractors + specialized handlers for Svelte / Vue / Liquid / Delphi (handler-class-per-language pattern)
- **Resolution** (`src/resolution/`): Framework-aware pattern matching (Express, Rails, Django, etc.)
- **Graph operations** (`src/graph/`): BFS/DFS traversal + impact radius analysis

**Dual-backend SQLite (native + wasm fallback)** is a corpus-observation worth noting:
- Native better-sqlite3 = fastest path
- WASM fallback = cross-platform reliability (when native compile fails)
- "Transparent" = automatic selection at runtime

Similar to Pattern #66 supply-chain-awareness sub-archetype: dual-implementation as resilience strategy.

## Critical synchronicity discipline (verbatim from CLAUDE.md)

> *"Three files must stay synchronized when updating MCP tool behavior:*
> *- `server-instructions.ts`*
> *- `instructions-template.ts`*
> *- `.cursor/rules/codegraph.mdc`"*

**This is corpus N+1 evidence for OC-E Synchronicity-Discipline-As-Policy** (registered at v68 zero).

**Mechanism comparison:**

| Subject | Synchronicity mechanism | Mode |
|---------|------------------------|------|
| v68 zero | Examples + docs + tests + contracts aligned with current behavior | **BEHAVIORAL** alignment |
| v70 codegraph | 3 MCP-tool-behavior files (server-instructions + template + Cursor rules) | **CONFIGURATION** alignment |

**Sister-observation OR N=2 under broader OC-E?** The mechanism distinction (behavioral vs configuration) is meaningful. Could split into:
- OC-E1 behavioral-synchronicity (v68 zero)
- OC-E2 configuration-synchronicity (v70 codegraph)

Or treat as N=2 evidence for broader OC-E "file-synchronicity-as-policy." Defer mechanism-distinction decision to v70+ audit.

## Critical maintenance disciplines (verbatim)

> *"Any new SQL or grammar wasm must be copied or it won't ship"*

This is a **build-discipline-as-product-requirement** observation. The `package.json` `copy-assets` script explicitly handles SQL schema + wasm files copy to dist:

```json
"copy-assets": "node -e \"const fs=require('fs');fs.mkdirSync('dist/db',{recursive:true});fs.copyFileSync('src/db/schema.sql','dist/db/schema.sql');fs.mkdirSync('dist/extraction/wasm',{recursive:true});fs.readdirSync('src/extraction/wasm').filter(f=>f.endsWith('.wasm')).forEach(f=>fs.copyFileSync('src/extraction/wasm/'+f,'dist/extraction/wasm/'+f))\""
```

CLAUDE.md flag-as-discipline + package.json automate = **CI-discipline-as-build-step**. Sister to Pattern #81 sub-variant 81a CI-enforced (claude-seo v64 5-version-source atomic-bump).

> *"Installer changes require test coverage in `installer-targets.test.ts`"*

47 parameterized tests validate idempotency + state recovery for installer behavior. Corpus-rare **installer-discipline-with-test-coverage**.

> *"Node version: `>=18.0.0 <25.0.0`"*

Tight version bound (~7-year range) — corpus-typical for Node.js libraries.

## Release process (verbatim)

> *"Update `CHANGELOG.md` first (user perspective, grouped by type), then run `./scripts/release.sh`."*

Release discipline:
1. CHANGELOG-FIRST (user-perspective, grouped by type)
2. Automated release script

**Corpus observation:** Other corpus subjects:
- v66 agentmemory CHANGELOG-FIRST + git-trailer-extraction for contributors
- v68 zero CHANGELOG documented in AGENTS.md with workflow
- v69 CloakBrowser CHANGELOG-FIRST (28+ releases, 0.33 releases/day)
- v70 codegraph CHANGELOG-FIRST with automated release.sh

CHANGELOG-FIRST is **becoming corpus-consistent discipline** — potential meta-pattern observation.

## Per-language extractor handler-class-per-language pattern

CLAUDE.md notes specialized handlers exist for **Svelte / Vue / Liquid / Delphi** beyond the per-language tree-sitter extractors.

Why these 4?
- **Svelte + Vue** — HTML-template-with-embedded-script languages (need specialized handlers because tree-sitter alone doesn't capture template-script boundary)
- **Liquid** — Shopify-template language (Colby's other project shopify-graphql-admin-mcp suggests author-domain expertise)
- **Delphi** — legacy Pascal-family (rare in modern tooling; intentional inclusion)

This is **author-domain-influenced specialized-handler selection**. Pattern #19 founder-personal lineage 19a sub-archetype evidence: the author's portfolio (Shopify-adjacent + AI-tooling) influences technical scope.

## Database persistence + transparency

CLAUDE.md mentions: *"native `better-sqlite3` with transparent fallback to WebAssembly"*

**Why dual-implementation:**
- better-sqlite3 native: 5-10× faster on supported platforms
- WASM fallback: works on Apple Silicon / non-x64 / sandboxed envs / unsupported Node versions
- Transparent = runtime auto-selection without user config

This is **Pattern #66 supply-chain-awareness sub-mechanism**: dual-implementation as cross-platform resilience strategy. Sister to v69 CloakBrowser dual-mac/linux/windows binary distribution.

## What's NOT in CLAUDE.md

- No code-of-conduct
- No contributor guidelines (presumably elsewhere)
- No deployment / hosting discussion (consistent with "100% local" positioning)
- No telemetry policy (consistent)
- No author bio inline (only in author profile + GitHub)

CLAUDE.md is **purely technical-product-rules** for Claude Code to use when modifying codegraph. No fluff, no marketing.

## Critical-rule-density analysis

CLAUDE.md contains ~5-6 critical rules in ~150-line file. Critical-rules-per-line ratio is high. Sister to v68 zero AGENTS.md (similar high-rule-density at ~190 lines).

**Observation:** Corpus subjects optimized for AI-coding-agent-use tend toward terse, rule-dense governance files. Different shape from corpus subjects optimized for human-developer-onboarding (which tend toward verbose, narrative-rich governance files).

→ **NEW observational candidate: Rule-Density-As-AI-Optimization** (terse + rule-dense governance files signal optimization for AI agent consumption rather than human onboarding). Sister to OC-E Synchronicity-Discipline.
