# Cluster 3 — CHANGELOG + multi-agent installer + npm packaging

> Source: `CHANGELOG.md` + `package.json` + npm registry · fetched 2026-05-19

## Release cadence

- **v0.7.6:** 2026-05-13
- **v0.7.7:** 2026-05-17 (multi-agent installer)
- **v0.7.8:** 2026-05-17 (OpenCode config fix)
- **v0.7.9:** 2026-05-18

Recent 4 releases span 6 days = ~1.5 releases/day sustained at v0.7.x. Project age 121 days with implied 28+ releases at older cadence; current cadence has accelerated.

**Comparison with recent corpus subjects:**
- v68 zero: 3 releases in 2 days = 1.5/day (corpus-record cadence)
- v69 CloakBrowser: 28+ releases in 86 days = 0.33/day (corpus-record sustained-cadence)
- **v70 codegraph: 4 releases in 6 days at recent end = 0.67/day** (mid-range)

## v0.7.7 Multi-Agent Installer (corpus-novel pattern)

CHANGELOG v0.7.7 (2026-05-17) introduces:

> *"Multi-agent installer with interactive selection for Claude Code, Cursor, Codex CLI, and OpenCode. Non-interactive flags (`--target`, `--location`, `--yes`) support scripting. Auto-wiring for project-local agent configs."*

**Mechanism breakdown:**
- **Interactive mode:** prompts user to select 1-or-more agents from list
- **Non-interactive mode:** `--target=cursor,claude --yes` (comma-separated multi-target)
- **Auto-wiring:** writes per-platform config (e.g., `~/.claude.json` for Claude Code, `.cursor/rules/codegraph.mdc` for Cursor) automatically

This is **corpus-novel multi-agent-installer pattern** — single command configures multiple agent platforms in one operation. Could become Pattern #2 Distribution Evolution sub-variant or NEW pattern.

→ **OC-L Multi-Agent-Installer-Pattern observational candidate.**

## v0.7.8 OpenCode installer fix + AGENTS.md auto-generation

CHANGELOG v0.7.8 (2026-05-17):

> *"OpenCode installer now correctly targets `opencode.jsonc` instead of `opencode.json`, ensuring the CodeGraph entry appears in OpenCode sessions. Users should 'Re-run `codegraph install --target=opencode` after upgrading.'"*

> *"Added: The installer creates an `AGENTS.md` file with usage guidance, and preserves user comments during config updates via surgical JSON edits."*

**Two observations:**

1. **OpenCode (v67 corpus subject) config-target regression-fix.** The v0.7.7 introduction targeted `opencode.json` but OpenCode uses `opencode.jsonc` (JSON with comments). Fixed in v0.7.8. → corpus-citation 57c-product strengthening (codegraph integrates with v67 corpus subject; even regression-fixes are corpus-relevant).

2. **AGENTS.md auto-generation:** The installer GENERATES an `AGENTS.md` file in user's project with usage guidance. Corpus-novel — most corpus subjects ship AGENTS.md handwritten; codegraph generates AGENTS.md programmatically.

→ **OC-N Auto-generated AGENTS.md from tool installer observational candidate.**

**Surgical JSON edits with comment preservation** is also a corpus-rare engineering choice — most tools rewrite entire JSON files. Surgical-edit-with-comment-preservation suggests serious investment in respecting user customizations.

## v0.7.6 Binary executable permission fix

CHANGELOG v0.7.6 (2026-05-13):

> *"Fixed: The published 0.7.5 tarball shipped the binary without executable permissions. The build process now applies `chmod +x` before packaging."*

This is a **Pattern #83 honest-deficiency-disclosure** instance — explicitly naming the v0.7.5 packaging-error + the remediation. Sister to Pattern #83 sub-mechanism 83a security-disclosure (transparent error disclosure).

Pattern #83 was just promoted at v69 audit; codegraph adds within-pattern N+1 evidence for transparent-bug-disclosure sub-mechanism.

## package.json — lean dependency profile

```json
{
  "name": "@colbymchenry/codegraph",
  "version": "0.7.9",
  "description": "Supercharge Claude Code with semantic code intelligence. 94% fewer tool calls • 77% faster exploration • 100% local.",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "bin": {
    "codegraph": "./dist/bin/codegraph.js"
  },
  ...
}
```

**Runtime dependencies (10):**
- `@clack/prompts` 1.3.0 — interactive CLI prompts
- `commander` 14.0.2 — CLI parsing
- `fast-string-width` 3.0.2 + `fast-wrap-ansi` 0.2.0 + `sisteransi` 1.0.5 — ANSI terminal output utilities
- `jsonc-parser` 3.3.1 — JSON-with-comments parser (for opencode.jsonc + others)
- `node-sqlite3-wasm` 0.8.30 — wasm SQLite fallback
- `picomatch` 4.0.3 — glob matching
- `tree-sitter-wasms` 0.1.11 — multi-language wasm parsers
- `web-tree-sitter` 0.25.3 — tree-sitter runtime

**Optional dependencies (1):**
- `better-sqlite3` 11.0.0 — native SQLite (faster path; wasm is fallback)

**Dev dependencies (5):**
- `@types/better-sqlite3` 7.6.0 + `@types/node` 20.19.30 + `@types/picomatch` 4.0.2
- `typescript` 5.0.0
- `vitest` 2.1.9

**Observation:** Lean dependency set (10 runtime + 1 optional = 11 total). Compare:
- v66 agentmemory: 6 runtime deps (smaller; delegates to iii-engine)
- v68 zero: 0 runtime deps (compiler-bootstrap, no external)
- v69 CloakBrowser: 2 runtime deps (playwright + httpx; binary is artifact)

codegraph at 11 deps is **mid-range corpus-typical** for TypeScript tools.

## scripts pipeline (verbatim)

```json
"scripts": {
  "build": "tsc && npm run copy-assets && node -e \"require('fs').chmodSync('dist/bin/codegraph.js', 0o755)\"",
  "preuninstall": "node dist/bin/uninstall.js",
  "copy-assets": "node -e \"const fs=require('fs'); ... (copy schema.sql + wasm files)\"",
  ...
}
```

**Notable:**
- `build`: tsc + copy-assets + chmod +x (3-step build; v0.7.6 fix integrated)
- `preuninstall`: runs uninstall.js to clean up installer-written configs in user's project
- `copy-assets`: explicit copy of schema.sql + tree-sitter wasm files (CLAUDE.md flagged this as critical)

The `preuninstall` hook is **corpus-rare** — most npm packages don't clean up after themselves on uninstall. codegraph's installer writes config to `~/.claude.json` etc.; preuninstall removes them.

→ **OC-O? Bidirectional-Installer-Discipline (install + uninstall coverage)** observational candidate. Pattern #2 Distribution Evolution sub-variant.

## Engines + version bounds

```json
"engines": {
  "node": ">=18.0.0 <25.0.0"
}
```

Node 18-24 supported. Wide enough to cover LTS + current; bounded above to prevent runtime surprises in unreleased Node versions.

## bin entry — single CLI entrypoint

```json
"bin": {
  "codegraph": "./dist/bin/codegraph.js"
}
```

Single CLI entrypoint mapped to `codegraph` global command. Standard npm bin pattern.

## Files-shipped manifest

```json
"files": [
  "dist",
  "scripts",
  "README.md"
]
```

Ships dist + scripts + README only. No source code, no tests, no config — clean tarball. Corpus-typical.

## What's NOT in package.json

- No `repository` field (probably elsewhere; or oversight)
- No `bugs` field
- No `homepage` field
- No `funding` field (no GitHub Sponsors / Patreon)
- No `private` flag (it's published)
- No `engines.npm` (only `engines.node`)

Minimal metadata — pure functional packaging.

## CHANGELOG style

CHANGELOG follows **Added / Fixed / Changed** sectioning per release (visible from probe). User-perspective framing per CLAUDE.md mandate.

**Comparison with Pattern #83 sub-mechanism candidates:**
- 83a security-disclosure: codegraph CHANGELOG v0.7.6 chmod +x fix = mild evidence (packaging-error vs CVE)
- 83b methodology-disclosure: codegraph CHANGELOG doesn't disclose methodology limits explicitly
- 83c legal-operational-disclosure: codegraph has no legal-operational disclosure (no dual-use concerns)
- 83d experimental-status-disclosure: codegraph at v0.7.9 is pre-1.0 but no prominent experimental-status banner
- 83e license-axis-as-disclosure-surface: MIT license; no Acceptable Use enumeration

Pattern #83 N+1 evidence is WEAK for codegraph — packaging-bug fix at most. Defer to v70+ audit if more evidence accumulates.

## Multi-agent integration insights from CHANGELOG

The recent v0.7.7 + v0.7.8 reveal **operational complexity of multi-agent support**:
- v0.7.7 introduced multi-agent installer
- v0.7.8 fixed OpenCode config target regression (`.json` → `.jsonc`)

This suggests **multi-agent target maintenance is non-trivial** — each agent platform has its own config file format + location + naming convention. codegraph internalizes all 4 platform-specifics.

→ Pattern #18 sub-mechanism B "one-binary-many-CLIENTS" maintenance-cost observation: the more clients, the more per-client config-target maintenance. codegraph's 4-platform support requires sustained per-platform fix-cycles.

## What this changelog tells us about velocity

4 releases in 6 days (May 13-18) suggests **active iteration on multi-agent installer + config-target correctness**. The v0.7.7 → v0.7.8 same-day fix indicates rapid response to discovered regressions (corpus-positive observation).

Project trajectory:
- v0.x → pre-1.0 (current at v0.7.9)
- 4-month age with ~28+ releases total = sustained release cadence
- Recent acceleration around multi-agent installer feature

Pre-1.0 status with active iteration matches corpus-pattern of mid-life-cycle developer-tools (similar shape to v66 agentmemory ~35-day-age at v0.9.x).
