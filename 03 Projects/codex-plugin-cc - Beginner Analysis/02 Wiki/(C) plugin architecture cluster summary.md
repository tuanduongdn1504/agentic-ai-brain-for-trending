# Cluster 2 — Plugin architecture

> **Sources:** plugins/codex/ tree structure (agents/ + commands/ + hooks/ + prompts/ + schemas/ + skills/ + scripts/ + CHANGELOG); .claude-plugin/ marketplace metadata.
> **Wiki:** codex-plugin-cc v62.

---

## 1. plugins/codex/ directory structure

| Subdirectory | Inferred purpose | Corpus context |
|---|---|---|
| `agents/` | Agent skill implementations (Codex-side?) | Plugin-architecture primitive |
| `commands/` | Slash command implementations (`/codex:review`, etc.) | Pattern #59 marketplace-plugin primitive |
| `hooks/` | Lifecycle hooks (pre/post review? auth? session?) | NEW corpus-first hooks-as-plugin-primitive at corporate scale |
| `prompts/` | Prompt templates (incl. `/codex:adversarial-review` framing prompt likely here) | KEY: adversarial-review reframing lives in prompt template, not separate role |
| `schemas/` | JSON schemas for agent skills | Plugin-architecture primitive |
| `skills/` | Skill definitions (Anthropic-skills-protocol-compatible?) | anthropics/skills protocol implicit |
| `scripts/` | Build / utility scripts | Plugin-tooling |

**Top-level files:** CHANGELOG + LICENSE + NOTICE.

## 2. .claude-plugin/ marketplace metadata

Standard Claude Code plugin marketplace structure. Enables:
- `/plugin marketplace add openai/codex-plugin-cc`
- `/plugin install codex@openai-codex` (uses `openai-codex` namespace)

**Observation:** Plugin uses `codex@openai-codex` namespacing convention (`<plugin>@<marketplace>`). Pattern #59 corporate-marketplace-publication observation; sub-variant for namespace strategy.

## 3. Adversarial-review prompt-framing inferred location

Per README: `/codex:adversarial-review` *"reframes existing review function"* with adversarial prompt. Inferred implementation:
- Same Codex review function as `/codex:review`
- Adversarial system prompt OR adversarial user prompt prefix
- Likely lives in `plugins/codex/prompts/adversarial-review.md` (or similar)

**Distinction from cc-sdd v61 architectural primitive:**
- cc-sdd: `kiro-review` is separate subagent skill with distinct invocation path (different agent role, different lifecycle)
- codex-plugin-cc: `/codex:adversarial-review` is same skill as `/codex:review` with prompt variation (same agent role, same lifecycle, different prompt)

This is **prompt-engineering-variant vs architectural-role-separation distinction** — fundamental mechanism difference.

## 4. Background-task primitive (4-command lifecycle)

```
/codex:rescue --background "task description"   # start
/codex:status                                     # poll
/codex:result <session-id>                       # retrieve
/codex:cancel <session-id>                       # abort
```

**4-command background-job lifecycle is corpus-first explicit surface** at this granularity. Prior corpus subjects (cc-sdd v61 `/kiro-impl` autonomous mode) had implicit long-running execution; codex-plugin-cc surfaces explicit lifecycle commands.

## 5. Authentication architecture

- Local authentication via Codex app server
- Reuses existing Codex configurations (interop)
- ChatGPT subscription OR OpenAI API key required
- Cross-vendor authentication: Claude Code session does NOT authenticate to Codex; user must authenticate to Codex separately

**Observation:** Cross-vendor-authentication-required mechanism — distinct from in-platform plugin authentication. Plugin host (Claude Code) does not proxy authentication to plugin backend (Codex).

## 6. Pattern #18 Layer 2 sub-archetype analysis

Pattern #18 protocol-translation layer state post-v62:

| Sub-archetype | Wiki | Mechanism | Translation timing |
|---|---|---|---|
| api-protocol-translation-proxy | free-claude-code v60 | Anthropic Messages API ↔ 6 provider protocols | Runtime (request-response) |
| install-time-per-platform-skill-format-translator | cc-sdd v61 | Per-platform skill format adapter | Install-time |
| **competitor-platform-bridge-as-plugin** | **codex-plugin-cc v62** | **Cross-vendor IDE plugin (Claude Code → Codex)** | **Runtime (delegation-based)** |

**Insight:** 3 distinct Pattern #18 Layer 2 sub-archetypes now, all N=1. Each represents different translation mechanism. Could unify as "cross-tool-integration-architectures" meta-pattern at future audit if 5+ sub-archetypes accumulate.

## 7. Plugin namespace conventions

`codex@openai-codex`:
- Plugin name: `codex`
- Marketplace: `openai-codex`

vs. prior corpus plugins:
- `oh-my-claudecode` (single-segment)
- `claude-hud` (single-segment)
- `claude-context` (single-segment)

**Observation:** Corporate-org publisher uses `org-namespace` convention; solo publishers use single-segment. Pattern #59 sub-distinction observable.

## 8. Corpus-first observations

- **CORPUS-FIRST hooks/ + prompts/ + schemas/ as plugin-primitive sextet** at OpenAI corporate scale (agents + commands + hooks + prompts + schemas + skills = 6 plugin-primitive types)
- **CORPUS-FIRST 4-command background-task lifecycle primitive** (rescue + status + result + cancel)
- **CORPUS-FIRST cross-vendor authentication-required plugin** (Claude Code host + Codex backend, separate auth)
- **CORPUS-FIRST plugin namespace convention `org-namespace`** at corporate scale (vs solo single-segment)

## 9. Absences

- ❌ NO MCP server / client (Codex backend not MCP-exposed)
- ❌ NO Anthropic-skills file format (uses Claude Code plugin schema, not anthropics/skills runtime)
- ❌ NO multi-platform support (Claude Code only — single-host design)
- ❌ NO bidirectional integration (Codex CLI cannot invoke Claude Code; one-direction Claude-Code → Codex only)

## 10. Pattern advancement check

- **Pattern #76 counter-evidence-driven refinement** — confirmed (prompt-framing vs role-separation distinction explicit at architecture level)
- **Pattern #59 corporate-scale strengthening** — Microsoft-scale-equivalent (OpenAI) plugin marketplace publication
- **Pattern #18 Layer 2 cross-vendor-bridge sub-archetype** — N=1 candidate
- **NEW corpus-first cross-vendor cooperation observation** — N=1 stale-flagged candidate
- **Pattern #19 corporate-strategic archetype N=2 cross-org** (Microsoft + OpenAI; was 1-org with 2 products before)
