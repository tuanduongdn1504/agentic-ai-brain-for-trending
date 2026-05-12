# Cluster 2 — SKILL.md + CLAUDE.md + behavioral artifact format

## What this cluster covers

The internal structural choice: how a single 4-principle behavioral guideline ships across 3 platforms (Claude Code skill / Claude Code root CLAUDE.md / Cursor rule). Source files: `skills/karpathy-guidelines/SKILL.md`, `CLAUDE.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.cursor/rules/karpathy-guidelines.mdc`.

## File-level redundancy by design

The 4-principle content appears in 3 nearly-identical files:

| File | Lines | Format | Purpose |
|------|------:|--------|---------|
| `CLAUDE.md` (root) | 65 | Plain Markdown | Per-project install via curl |
| `skills/karpathy-guidelines/SKILL.md` | 67 | YAML frontmatter + Markdown | Claude Code skill (anthropics/skills protocol) |
| `.cursor/rules/karpathy-guidelines.mdc` | (similar) | Cursor rule format | Cursor IDE auto-apply |

**Operator discipline note from CURSOR.md:** *"When you change the four principles, keep CLAUDE.md and `.cursor/rules/karpathy-guidelines.mdc` in sync. If the published skill/plugin text should match, update SKILL.md as well."*

This is **manual-sync-discipline at small scale** — distinct from cc-sdd v61's install-time format translator (which auto-generates per-platform files). karpathy-skills accepts manual-sync overhead because content is small (4 principles, ~65 lines).

## SKILL.md frontmatter (anthropics/skills protocol conformance)

```yaml
---
name: karpathy-guidelines
description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.
license: MIT
---
```

Three-field minimum: `name` + `description` + `license`. Conforms to anthropics/skills v62-corpus-validated frontmatter pattern (per agent-skills-of-vercel v51 / mattpocock-skills v57 cross-reference).

**Description field discipline:** the description starts with *"Use when..."* trigger language — matching anthropics/skills best-practice for skill-discovery routing. Compare to mattpocock-skills v57 which uses similar trigger phrasing across its 19 skills.

## plugin.json structure

```json
{
  "name": "andrej-karpathy-skills",
  "description": "Behavioral guidelines to reduce common LLM coding mistakes...",
  "version": "1.0.0",
  "author": {"name": "forrestchang"},
  "license": "MIT",
  "keywords": ["guidelines", "best-practices", "coding", "karpathy"],
  "skills": ["./skills/karpathy-guidelines"]
}
```

**Single-skill plugin** — `skills` array contains 1 entry. Compare to corporate-multi-skill plugins which array dozens.

## marketplace.json structure

```json
{
  "name": "karpathy-skills",
  "id": "karpathy-skills",
  "owner": {"name": "forrestchang"},
  "metadata": {"description": "...", "version": "1.0.0"},
  "plugins": [
    {
      "name": "andrej-karpathy-skills",
      "source": "./",
      "category": "workflow",
      ...
    }
  ]
}
```

**Marketplace name vs plugin name distinction:** marketplace = `karpathy-skills` (collection identity); plugin = `andrej-karpathy-skills` (artifact identity). Pattern #59 Claude Code Plugin Marketplace conformance.

Category: `workflow` (vs `tool`/`agent`/`skill`-other categories).

## Cursor rule pattern (`.mdc` format)

`.cursor/rules/karpathy-guidelines.mdc` ships with `alwaysApply: true` — meaning the rule applies to every Cursor session automatically without user opt-in per-message.

**Cross-platform asymmetry observation:** Claude Code installs the plugin (per-project or per-vault); Cursor applies the rule globally on the project. Different activation models.

## Single-skill granularity vs multi-skill collection — corpus comparison

| Subject | Skills count | Granularity model |
|---------|-------------:|-------------------|
| **andrej-karpathy-skills v63** | **1** | Single behavioral-guideline-as-skill |
| mattpocock-skills v57 | 19 | Author-original curated collection |
| awesome-claude-skills v50 | many | Community-curated meta-collection |
| agent-skills-of-vercel v51 | several | Corporate-curated collection |

**Verdict:** karpathy-skills represents the **finest-grained T1 Augmentation in corpus** — single behavioral document, distributed in skill-format wrapper for marketplace participation. The wrapper is incidental; the content IS just a behavioral document.

## Sub-archetype proposal: behavioral-guideline-document-distributed-as-skill

Distinct from:
- **curated-collection** (mattpocock / awesome-claude-skills / vercel) — multiple skills aggregated
- **methodology-harness** (cc-sdd / spec-kit / OpenSpec / GSD) — workflow scaffold with multiple primitives
- **single-purpose-tool-skill** (any narrow-task skill) — does ONE specific task

karpathy-skills is **behavioral-overlay** — modifies HOW the LLM approaches ANY task, doesn't add new task-execution capability. Scope = global behavioral modification, not task-domain expansion.

## What this cluster reveals about distribution strategy

forrestchang chose **maximum reach per minimum content**: 4 principles × 3 platforms × 2 languages = 24 install/language pairs from ~65 lines of source content. This is **distribution-leverage extreme** — corpus-rare ratio.

Compare to cc-sdd v61: ~3.3K stars / 8 platforms / 13 languages = much higher content per platform but lower viral velocity. karpathy-skills optimizes for *reach* not *depth*.
