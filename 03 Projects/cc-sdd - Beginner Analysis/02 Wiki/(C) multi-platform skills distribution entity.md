# Entity: Multi-platform Skills format translation — agent-platform-format-translation-installer (corpus-first)

> **Wiki:** cc-sdd v61 / 2026-05-07
> **Format:** 13-section canonical entity page

---

## 1. Identity / one-line definition

**Multi-platform Skills format translation** is cc-sdd's mechanism for translating SDD harness skill definitions into per-agent-platform native skill formats at install time, supporting 8 AI coding agents (Claude Code / Codex / Cursor / Copilot / Windsurf / OpenCode / Gemini CLI / Antigravity).

## 2. Source

- Mechanism documented in: README.md (Supported Platforms table) + docs/guides/skill-reference.md + AGENTS.md (cross-agent compatibility note) + npm CLI installer (`npx cc-sdd@latest --<platform>-skills`)
- Code lives in: `tools/cc-sdd/` (TypeScript installer) + `.agents/skills/cc-sdd-new-agent/` (template skill for adding new agents)

## 3. Tier placement

The mechanism is **deployment-layer** within cc-sdd's T1 SDD harness. It is NOT itself a tier-classifiable subject — it's a sub-component of cc-sdd v61.

For Pattern Library purposes: this mechanism is candidate **Pattern #18 Layer 2 sub-archetype** "agent-platform-format-translation-installer" (N=1 first observation; install-time translation; distinct from runtime API protocol translation seen at v60 free-claude-code).

## 4. Core mechanism

**Install-time translation flow:**

```
User: npx cc-sdd@latest --claude-skills
  ↓
CLI installer reads: .agents/skills/cc-sdd-new-agent/ template
  ↓
Translates to Claude Code native skill format:
  - Output directory: .claude/skills/kiro-*/
  - File naming: per-platform conventions
  - Frontmatter: per-platform metadata
  - Slash command syntax: per-platform constraints (dash vs colon, etc.)
  ↓
User runs: /kiro-discovery (now native to Claude Code)
```

**Per-platform output directory pattern:**
- `--claude-skills` → `.claude/skills/kiro-*/`
- `--codex-skills` → `.codex/skills/kiro-*/`
- `--cursor-skills` → `.cursor/skills/kiro-*/`
- `--copilot-skills` → `.copilot/skills/kiro-*/` (or VS Code extension equivalent)
- `--windsurf-skills` → `.windsurf/skills/kiro-*/`
- `--opencode-skills` → `.opencode/skills/kiro-*/`
- `--gemini-skills` → `.gemini/skills/kiro-*/`
- `--antigravity` → Antigravity-specific structure (experimental)

## 5. Workflow / per-platform translation table

| Platform | Status | Skill format | Slash syntax | Subagent support |
|---|---|---|---|---|
| Claude Code | Stable | Native skills (post-Skills mode) | `/kiro-discovery` | Yes (Task tool) |
| Codex | Stable | Codex skills | `/kiro-discovery` | Yes |
| Cursor IDE | Beta | Cursor skills | `/kiro-discovery` | Limited |
| GitHub Copilot | Beta | Copilot skills (VS Code ext) | varies | Limited |
| Windsurf IDE | Beta | Windsurf skills | varies | Limited |
| OpenCode | Beta | OpenCode skills | `/kiro-discovery` | Limited |
| Gemini CLI | Beta | Gemini skills | varies | Limited |
| Antigravity | Experimental | Antigravity-specific | TBD | TBD |

**Observation:** Maturity tier is unequal-distributed (2 stable / 5 beta / 1 experimental). Claude Code is reference-stable. Other platforms tracked as derivative implementations.

## 6. Differentiators (vs other corpus translation mechanisms)

| Dimension | OpenSpec v58 (per-tool format translation) | free-claude-code v60 (T4 6-provider API translation) | n8n v56 (16-LLM routing) | mattpocock-skills v57 (Claude Code only) | **cc-sdd v61** |
|---|---|---|---|---|---|
| **Translation timing** | Install-time | **Runtime** (request-response) | Runtime | Build-time | **Install-time** |
| **Translation target** | Per-tool skill format | API protocol (Anthropic Messages ↔ provider) | LLM provider | Build artifact | **Per-platform skill format** |
| **Platform count** | 30+ tools | 6 providers | 16 LLMs | 1 (Claude Code) | **8 platforms** |
| **Maturity distribution** | Unclear | Homogeneous (all stable) | Homogeneous | Single | **2 stable / 5 beta / 1 experimental** |
| **Tier classification** | T1 (methodology) | T4 (translation bridge) | T1 (platform) | T1 (Skills builder) | **T1 (SDD harness)** |
| **Architectural primitive** | Per-tool format adapter | API protocol proxy | Multi-LLM router | Skill template | **Per-platform skill format adapter** |

**Key distinction:** cc-sdd's translation is **install-time + skill-format + 8 platforms** — distinct combination not previously observed in corpus.

OpenSpec v58 most-similar mechanism (per-tool format translation) — but at 30+ tools and unclear maturity. cc-sdd's smaller platform count + explicit maturity tiers + Skills mode primary pivot makes it a structurally distinct sub-archetype.

## 7. Origin / lineage

The mechanism emerged at v3.0.0 (2026-04-10) as part of cc-sdd's "major architectural shift introducing Agent Skills mode as the primary installation target." Prior versions used command-based installs without explicit per-platform translation.

Lineage:
- Pre-v3.0: command-based installs (per-platform-aware but not Skills-format-translated)
- v3.0+: Skills-mode-as-primary install target with explicit per-platform translation
- Reflects industry trend toward Agent Skills as native AI agent primitive

External lineage:
- mattpocock-skills v57 popularized Agent Skills authoring for Claude Code
- Claude Skills became Anthropic-blessed primitive ~late 2025
- cc-sdd v3.0 absorbed Skills-mode primitive and extended to 8 platforms

## 8. Adoption signals

- v3.0.0 deprecated command-based installs (still available, not primary)
- 5-of-8 platforms still beta — adoption broadening but unevenly mature
- v3.0.2 fixed missing `description` field in Codex template — active per-platform refinement
- Greek added v2.0.5 → 13-language i18n is dimension-orthogonal to platform translation but indicates active maintenance

## 9. Limitations / failure modes

- **Maturity-tier-mixed** — 5-of-8 platforms beta. Production teams may avoid beta platforms.
- **Per-platform-format drift** — each platform's skill format evolves independently; cc-sdd must track changes
- **Skill semantics may not translate cleanly** — some skills (e.g., kiro-impl autonomous mode requiring subagent dispatch) may behave differently per platform
- **Antigravity experimental** — should not be used in production
- **No multi-platform skill validation** — installer doesn't (per docs) verify behavior parity across platforms

## 10. Storm Bear vault applicability

**Direct relevance:** Vault uses Claude Code (stable on cc-sdd). `--claude-skills` install path is production-ready.

**Indirect relevance:** If vault adds Codex / Cursor for specific tasks, cc-sdd would translate same SDD harness automatically.

**Pilot consideration:** Multi-platform isn't immediately useful for vault (single-platform Claude Code workflow). The translation mechanism is supportive infrastructure for cc-sdd, not a primary feature for vault use.

## 11. Open questions

- Q4 (open questions): Why colon → dash syntax migration at v3.0? Is this Skills mode constraint or stylistic?
- Per-platform skill semantics parity testing — does cc-sdd ship cross-platform parity tests? Not visible from ingested docs.
- Q13 (open questions): Pattern #18 Layer 2 sub-archetype overlap — does OpenSpec v58 30+ tools per-tool format translation count as N=1 prior observation? If yes, cc-sdd is N=2 promotion-eligible at next mini-audit. If no, cc-sdd is N=1 stale-flagged at registration.

## 12. Cross-references

**Direct ecosystem peers:**
- [OpenSpec v58](../../OpenSpec%20-%20Beginner%20Analysis/) — 30+ tools per-tool format translation (closest analog)
- [free-claude-code v60](../../free-claude-code%20-%20Beginner%20Analysis/) — runtime API protocol translation (T4)
- [n8n v56](../../n8n%20-%20Beginner%20Analysis/) — 16-LLM routing platform
- [mattpocock-skills v57](../../mattpocock-skills%20-%20Beginner%20Analysis/) — Agent Skills builder (Claude Code)

**Other multi-platform corpus subjects:**
- [agent-skills-of-vercel](../../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — Vercel-specific
- [awesome-claude-skills](../../awesome-claude-skills%20-%20Beginner%20Analysis/) — Claude Skills directory

**Pattern Library entries referenced:**
- Pattern #18 protocol-translation (Layer 2 sub-archetype candidate at v61)
- Pattern #57 57c-positive-comparison-parallel (cc-sdd does NOT explicitly cite OpenSpec — does NOT extend 57c)

## 13. Next action

For Pattern Library: register **Pattern #18 Layer 2 sub-archetype "agent-platform-format-translation-installer"** as N=1 candidate at v61. Stale-flag at registration per N=1 stale-risk discipline. Re-evaluate at v66/v71 for 2nd observation OR overlap with OpenSpec v58 mechanism (>70% pre-check).

For Storm Bear vault: not action-required (single-platform Claude Code use already supported via `--claude-skills`).

For corpus: monitor for next install-time per-platform skill-format translator (separate from runtime API protocol translation) to test pattern stability.
