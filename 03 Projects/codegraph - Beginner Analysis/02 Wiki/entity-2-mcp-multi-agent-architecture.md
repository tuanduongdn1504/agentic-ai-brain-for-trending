# Entity 2 — Multi-agent MCP server architecture + protocol-variants

> codegraph's MCP-server-as-multi-platform-augmentation-layer + the protocol-variants observation

## Multi-agent architecture summary

codegraph operates as a **single Node binary** that serves MCP tools to **4 agent platforms** (Claude Code / Cursor / Codex CLI / OpenCode). The architectural shape is **one-binary-many-CLIENTS via MCP** — Pattern #18 sub-archetype shared-backend-service sub-mechanism B.

The 4 platforms have **distinct config file formats + locations**:

| Agent | Config Location | Format |
|-------|---|---|
| Claude Code | `~/.claude.json` | JSON |
| Cursor | `.cursor/rules/codegraph.mdc` | Markdown rules |
| Codex CLI | `~/.codex/AGENTS.md` | Markdown agents file |
| OpenCode | `opencode.jsonc` | JSON-with-comments |

codegraph's installer handles all 4 per-platform writes in a single operation:

```bash
codegraph install --target=cursor,claude,codex,opencode --yes
```

This is **corpus-novel multi-agent-installer-pattern** — single command writes per-platform configs in one operation.

## Protocol-variants observation (sub-mechanism B formalization candidate)

Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" now has N=3 evidence across **2 protocol-variants**:

### MCP variant (N=2)

| Subject | Tool count | Client count | Protocol |
|---------|-----------|--------------|----------|
| v66 agentmemory | 51 MCP tools | 15+ agent platforms | MCP |
| v70 codegraph | 8 MCP tools | 4 agent platforms | MCP |

**Mechanism characteristics:**
- MCP server is the multiplexing point
- Each client (Claude Code / Cursor / etc.) connects to MCP server independently
- Tool schema is platform-agnostic; per-platform config-target write handles platform-specific config formats
- Tool granularity varies (51 vs 8) — agentmemory finer-grained, codegraph coarser-grained

### CDP variant (N=1)

| Subject | Use case | Protocol |
|---------|----------|----------|
| v69 CloakBrowser | `cloakserve` CDP server mode | Chrome DevTools Protocol |

**Mechanism characteristics:**
- CDP (Chrome DevTools Protocol) — established protocol for browser automation
- Multiple framework clients connect to single CloakBrowser binary via CDP
- More legacy-specific (Chromium-tied) vs MCP (agent-ecosystem-wide)

## Protocol-variants formalization proposal

**For v70 Phase 4b PRIMARY:** Formalize sub-mechanism B as having **2 protocol-variants**:
- **B1: MCP variant** (agentmemory v66 + codegraph v70 = N=2)
- **B2: CDP variant** (CloakBrowser v69 = N=1)

This makes sub-mechanism B promotion-eligible (N=3 with 2 protocol-variants) per criterion 4 variant-within-pattern-at-N=2.

**Decision deferred to v70+ audit:** Should sub-mechanism B split into B1 + B2 as formal sub-sub-variants, OR remain unified with protocol-variants as observational?

## Per-platform config-target maintenance cost observation

codegraph's v0.7.7 → v0.7.8 same-day fix illustrates **multi-platform maintenance cost**:

- v0.7.7 (2026-05-17): Multi-agent installer introduced; OpenCode target hardcoded to `opencode.json`
- v0.7.8 (2026-05-17): OpenCode target corrected to `opencode.jsonc` (OpenCode actually uses JSONC)

The same-day regression-fix indicates rapid response to discovered cross-platform inconsistencies. **Sustained multi-platform maintenance requires per-platform-specific knowledge** — codegraph maintains 4 platform-config-formats simultaneously.

→ **OC-P Multi-Platform Config-Target Maintenance Cost observational candidate** (cost grows as platform-count grows; each platform-specific format requires sustained per-platform fix cycles).

## MCP tool granularity comparison

| Subject | Tool count | Design philosophy |
|---------|-----------|-------------------|
| v66 agentmemory | 51 tools | **Fine-grained** — each memory operation explicit |
| v70 codegraph | 8 tools | **Coarse-grained** — lightweight tools for targeted lookups |

**Design philosophy distinction:** agentmemory exposes detailed primitives (51 tools for memory CRUD + query + decay + reflection); codegraph exposes coarser-grained operations (8 tools for code-graph queries).

codegraph CLAUDE.md explicitly guides agent usage:
- *"Use `codegraph_explore` as the primary tool"* — single high-level tool for exploration
- *"Main session may use lightweight tools (`search`, `callers`, `impact`, `node`) for targeted lookups"* — 4 specific tools for narrow queries

**Sister observation:** The coarse-grained-with-explicit-usage-guidance pattern is **product-defined-agent-usage-discipline** — codegraph dictates how agents should use the tools. Sister to Pattern #18 sub-mechanism candidate.

## Configuration write strategy: surgical JSON edits

v0.7.8 introduced:

> *"surgical JSON edits with comment preservation"*

When codegraph writes to `~/.claude.json` or `opencode.jsonc`, it:
1. Parses existing JSON/JSONC (preserving comments + formatting)
2. Surgically inserts/updates only its own entries
3. Re-serializes preserving original formatting

This is **corpus-rare engineering investment** — most npm tools blindly rewrite config files (clobbering user customizations). Surgical edits respect user state.

→ **OC-Q Surgical-Config-Edits-vs-Clobber observational candidate.**

## Why this architecture matters at corpus level

The **MCP-server-as-multi-platform-augmentation-layer** is emerging as a **dominant corpus shape** for T2 Service:

| Subject | Tier | MCP integration | Multi-platform reach |
|---------|------|-----------------|----------------------|
| agentmemory v66 | T2 | 51 tools | 15+ platforms |
| codegraph v70 | T2 | 8 tools | 4 platforms |
| Skyvern v24 | T2 | (legacy, pre-MCP era) | 1 platform |
| crawl4ai v29 | T2 | (legacy, pre-MCP era) | Standalone |

**Trend observation:** Newer T2 Service corpus subjects (post-MCP-protocol-emergence) adopt MCP-multi-platform shape. Older T2 (Skyvern v24, crawl4ai v29) are pre-MCP standalone. → Library-vocabulary item candidate: **MCP-Multi-Platform-As-Emerging-T2-Service-Default** (post-Anthropic-MCP-protocol release ~2026).

## Comparison with non-corpus multi-platform tools

codegraph's per-platform config-target architecture has corpus-external parallels:
- `eslint` (writes per-IDE configs to `.eslintrc` + `.vscode/settings.json` + etc.) — similar pattern, pre-MCP era
- `prettier` (similar to eslint shape)
- `husky` (writes `.git/hooks/*` per Git event)

These are **per-tool config-target writers** but not MCP-multi-agent-augmentation. The MCP-multi-agent-augmentation specifically is corpus-novel — emerged with MCP protocol availability.

## Storm Bear lessons from Entity 2

For the vault operator:

- **MCP is becoming the corpus-default for multi-platform agent augmentation.** When designing vault tooling that needs multi-IDE support, MCP server architecture (one binary + per-platform config-target write) is the corpus-validated pattern.
- **Per-platform config-target maintenance is non-trivial.** Each agent platform has its own config format + location + naming convention. Supporting N platforms = N config-target codepaths. Plan for it.
- **Surgical config edits respect user state.** When a vault tool writes to existing config files, prefer surgical edits (parse + minimal-mutation + preserve formatting) over full rewrite (clobber). Corpus-rare engineering but high-value for user trust.
- **Tool granularity is a design choice.** 51 tools (agentmemory) vs 8 tools (codegraph) — both work; trade-off is exposure-granularity vs ease-of-use. For vault tooling, lean toward coarse-grained-with-explicit-guidance unless deep primitives are necessary.
