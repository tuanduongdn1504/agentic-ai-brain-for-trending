# Instruction layer — Markdown file hierarchy

The foundation primitive of every AIOS in the corpus. **Ross Mike's contrarian "95% don't need this"** is the sharpest disagreement and worth reading first.

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Trends-1 + §Outliers-1

## The shared pattern (N=4 pro-structure)

Persistent local `.md` files define agent identity, role, and memory. Naming conventions vary by tool but the underlying practice is identical:

| File | Purpose | Source |
|---|---|---|
| `claude.md` | Static context for Claude Code | Ben AI |
| `agents.md` | Static context for generic agents | Multiple |
| `soul.md` | Personality + values | Mani Kanasani |
| `identity.md` | Agent's "face" — name, emoji | Mani Kanasani |
| `user.md` | Human's preferences | Mani Kanasani |
| `memory.md` | Persistent learning across sessions | Remy Gaskell, Simon Scrapes |

## Mani Kanasani's identity hierarchy (most-developed)

A three-file split for the agent's self-definition:

```
soul.md       ← personality / values (WHO am I)
identity.md   ← name / face / branding (HOW am I addressed)
user.md       ← human's preferences (WHO am I serving)
```

Together: the agent has a coherent "personality + face + audience awareness" at every invocation. Maps to a vault-level analog where this trio could live alongside CLAUDE.md.

## Ben AI's "instruction layer as map"

Ben AI frames `claude.md` as an **"instruction layer" or "map"** that tells the agent how to navigate a complex folder structure. Not a behavior contract — a **navigation primitive**. This shifts emphasis from "what to do" to "where to look."

## The Ross Mike counter (the corpus's central outlier)

Ross Mike pushes back hard on the heavy-`.md` orthodoxy:

> "95% of people don't need this"

Specific objections:
- Modern models (GPT-5.4, Claude 4.6) are "exceptionally good" out of the box
- They know they need a microphone to record a podcast without being told
- Large instruction files — some 1,000 lines — **burn thousands of unnecessary tokens on every turn**
- Heavy context can actually make models **"dumb"** as the context window nears its limit

This is the single sharpest disagreement axis in the corpus. Worth resolving by **measurement** (compare token usage + output quality with and without heavy `.md`) rather than dogma.

## Reconciliation — when each side is right

| Context | Pro-structure (N=4) is right | Ross Mike contrarian is right |
|---|---|---|
| Scheduled / autopilot tasks | YES — agent needs context every run | Less so — operator might preload context per task |
| Multi-agent / sub-agent dispatch | YES — each subagent needs scoped identity | Less so — single-agent sessions can lean on model defaults |
| Brand-voice / professional output | YES — voice file produces consistency | Less so — explicit per-prompt voice cue may suffice |
| Casual / exploratory use | Marginal | YES — defaults are good enough |
| Token cost is critical | Lean files matter | Skip entirely if model defaults work |

The choice isn't dogmatic — depends on **how much output consistency matters** and **whether the same agent runs many times**.

## How this composes with vault patterns

| Vault layer | Maps to |
|---|---|
| Vault-root `CLAUDE.md` | Storm Bear's behavioral contract (12-rule Mnilax extension) |
| Per-project `CLAUDE.md` | Project-scoped identity + librarian rules |
| `_state/` chapters | Long-term memory equivalents |
| Per-skill `SKILL.md` | Maps to the corpus's "skills" concept (see [[skills-architecture-progressive-disclosure]]) |

The vault's `CLAUDE.md` hierarchy at vault-root → project → skill is **structurally identical** to the corpus's `soul.md → identity.md → user.md` pattern at a different scale. See [[../claude-md-12-rules/_index]] for the behavioral-contract version.

## Key Takeaways

- **All AIOS implementations use persistent `.md` instruction files** — the only question is how heavy
- **Mani Kanasani's 3-file identity hierarchy** (soul / identity / user) is the most-developed framework — adopt if running multi-agent or scheduled workloads
- **Ross Mike's counter is empirically grounded** — large `.md` files DO inflate token costs and can degrade quality at context-window limits
- **The right call is measurement** — instrument token usage + output quality with/without heavy files, then decide
- **Vault's CLAUDE.md hierarchy is the same pattern** — corpus convergence across scales validates this as fundamental

## Related

- [[overview]] — AIOS framing
- [[skills-architecture-progressive-disclosure]] — same token-pressure concern, different surface
- [[memory-and-context-rot]] — where heavy context fails worst
- [[../claude-cowork/contextual-engineering]] — the Cowork-product instance of this pattern
- [[../claude-md-12-rules/_index]] — the behavioral-contract version
