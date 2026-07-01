# Antigravity vs Claude Code vs Cursor vs Windsurf/Kiro

## Source

Synthesis of the verification workflow's cross-platform comparison + `cursor.com/docs/rules` + `kiro.dev/docs/steering`. See [[google-antigravity-skills/source-provenance]]. Companion to [[google-antigravity-skills/anthropic-agent-skills-portability]].

---

## Concept-by-concept map

| Concept | **Antigravity** | **Claude Code** | **Cursor** | **Windsurf / Kiro** |
|---|---|---|---|---|
| **Project instructions** | `GEMINI.md` + `AGENTS.md` | `CLAUDE.md` + `AGENTS.md` | `.cursor/rules/*.mdc` (+ `AGENTS.md`) | `.windsurf/rules/*.md` · Kiro `.kiro/steering/*.md` (+ `AGENTS.md`) |
| **Reusable skill format** | `SKILL.md` (YAML + MD) | `SKILL.md` (YAML + MD) | `.mdc` rule files | `.md` rule/steering files |
| **Project skills dir** | `.agents/skills/` | `.claude/skills/` | `.cursor/rules/` | `.windsurf/rules/` · `.kiro/steering/` |
| **Global skills dir** | `~/.gemini/config/skills/` | `~/.claude/skills/` | `~/.cursor/rules/` | `~/.windsurf/…` · `~/.kiro/steering/` |
| **Cross-tool portability** | `AGENTS.md` | `AGENTS.md` | `AGENTS.md` | `AGENTS.md` |
| **Invocation** | semantic match **or** `/skill-name` | semantic match (`disable-model-invocation` to force user-only) | `@rule-name` mention **or** glob auto-attach | trigger field (always / manual / model-decision / glob) · Kiro `#steering-name` |
| **Skill creation** | manual files (no generator cmd) | manual files (+ Skill Creator skill) | manual `.mdc` | manual `.md` |
| **Multi-agent orchestration** | native (2.0 desktop hub, parallel subagents, state handoff) | collaborator model (primary + summoned) | single-agent | single session (Cascade) |
| **Discovery** | progressive disclosure | progressive disclosure | manual `@` / glob | trigger-field-driven |

## The three things that actually matter

1. **`SKILL.md` is shared** by Antigravity, Claude Code, and (with conversion) Cursor/Windsurf — because it's **Anthropic's open format**. This is the strongest portability axis.
2. **`AGENTS.md` is the universal rules layer** — the *only* file that works unchanged across all of them. If you standardize on one thing, standardize on this.
3. **Invocation semantics differ** — Antigravity & Claude Code route by the skill's `description` (semantic); Cursor routes by `@mention`/glob; Windsurf/Kiro by an explicit trigger field. So a ported skill *loads* differently even when its body is identical. Budget a small edit to frontmatter/trigger when moving.

## Where each is distinctive

- **Antigravity:** the only one with a **first-class multi-agent orchestration surface** (the 2.0 desktop hub, parallel subagents) baked in — and it's **free** with **multi-model** (incl. Claude). Weakest on maturity (public preview; see [[google-antigravity-skills/caveats-and-limitations]]).
- **Claude Code:** the deepest, most stable skills+hooks+MCP ecosystem; native `SKILL.md`; the operator's home base.
- **Cursor:** rules-as-`.mdc` with glob auto-attach; strong editor UX; no `SKILL.md`-native, but reads `AGENTS.md`.
- **Windsurf/Kiro:** trigger-field rules; Kiro is spec/steering-first (see [[../harness-engineering/_index]] for the Kiro-methodology lineage note).

## Practical takeaway for the operator

You already run **Claude Code** as your primary harness. Antigravity is **not a replacement** — it's a **free, standards-compatible second surface** you can point your *same* skills/rules at. The migration cost between them is essentially a **directory rename** (`.claude/skills/` ↔ `.agents/skills/`) plus keeping shared rules in `AGENTS.md`. That's the whole thesis of the pilot menu.

## Key Takeaways

- **`SKILL.md` (skills) + `AGENTS.md` (rules)** are the two portable primitives across Antigravity, Claude Code, Cursor, and Kiro.
- **`AGENTS.md` is the only unchanged-across-all rules file** — standardize on it.
- **Invocation differs** (semantic vs `@mention`/glob vs trigger-field) — a ported skill needs a small frontmatter tweak.
- **Antigravity's differentiator** is built-in **multi-agent orchestration + free multi-model**; its cost is **public-preview immaturity**.
- For you: Antigravity is a **free second surface for the harness you already have**, not a switch away from Claude Code.
