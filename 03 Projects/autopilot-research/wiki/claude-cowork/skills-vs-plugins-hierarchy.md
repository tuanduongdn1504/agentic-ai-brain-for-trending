# Skills vs Plugins hierarchy — the recipe vs the chef

The clearest taxonomy clarification from the 2026-05-30 follow-up drain. Two practitioners (Eliot Prince + Darrel Wilson, N=2) converge on a structural hierarchy that the original 2026-05-29 claude-cowork wiki treated as a single concept.

## Source

- Raw: [`raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md`](../../raw/2026-05-30-anthropic-cowork-first-party-documentation-setup-c.md) (NotebookLM `b05d3444-6dbb-4955-a8fb-be9b021a0350`, §Trends-2)

## The two-tier hierarchy

| Tier | Metaphor | What it is | Scope |
|---|---|---|---|
| **Skills** | "Recipe card" (Prince) / "reference outline" (Wilson) | A repeatable, **single-task** instruction set in Markdown | One specific output (e.g., LinkedIn-post format, branded invoice) |
| **Plugins** | "Experienced chef" (Prince) / bundle (Wilson) | **Bundle of multiple Skills + Connectors** representing an entire job function | Full job role (e.g., "Full Stack Marketer") |

This is the corpus-first explicit articulation of the two-tier composition. The 2026-05-29 claude-cowork wiki ([[skills-to-plugins-pipeline]]) used the terms more loosely — partially because the original 6-source bundle used Skill / Plugin somewhat interchangeably.

## Why this matters

The hierarchy enables a **compositional discipline**:

- **Author Skills first** — small, focused, single-task. Each Skill is independently testable.
- **Bundle into Plugins** — package N related Skills + their required Connectors into a deployable unit.
- **Distribute Plugins as job-function-shaped artifacts** — "Full Stack Marketer plugin" rather than "30 individual marketing-related skills."

This matches the **Unix philosophy** applied to AI capabilities:
- Skills = small sharp tools (`grep`, `sed`, `awk`)
- Plugins = pipelines composing them (`grep | sed | awk` baked into a Makefile target)

## Composition with prior wiki content

| Prior claim (existing wiki) | Refinement (this drain) |
|---|---|
| "Skill" used loosely for any reusable instruction | Skill = single task only |
| Plugin terminology ambiguous (sometimes = skill, sometimes = larger unit) | Plugin = bundle of skills + connectors = job function |
| Jack Roberts's "handover test" applies to either | Handover test more naturally fits Plugin promotion (job-function readiness) |
| Build-via-failure (Ross Mike) produces single skills | Multiple build-via-failure runs → bundle into a Plugin |

The new clarification doesn't invalidate existing wiki content — it refines the granularity.

## Implications for the vault

The vault's `05 Skills/` is currently a **flat list** of Skills (vault Skill-files). If the vault adopts this two-tier hierarchy, the natural extension would be:

- **`05 Skills/`** — individual Skill files (Anthropic-format `SKILL.md` + supporting files), each single-task
- **`05 Plugins/`** (new) — Plugin bundles that compose multiple Skills for a full operator workflow (e.g., "Storm Bear Librarian plugin" bundling routine v2.2 + skill-references + …)

This is **NOT yet implemented** in the vault and is just a consequence of adopting the two-tier framing. Worth raising at next pattern-library audit.

## Production-readiness considerations

For the two-tier hierarchy to scale:

1. **Skill discoverability** — operator must find the right Skill from a registry; progressive disclosure ([[skills-to-plugins-pipeline]]) handles this
2. **Plugin versioning** — when a Skill inside a Plugin updates, what happens to consumers? (corpus does not address)
3. **Plugin dependency declaration** — Plugin should declare which Skills it bundles; corpus does not show a manifest format
4. **Plugin marketplace** — Mani Kanasani (from sister [[../ai-operating-system/_index]]) mentions `npx playbooks` and "thousands of open-source skills"; Plugin-distribution standards are emerging but not codified

Each of these is a gap worth a future drain.

## Distribution insight from this drain

Eliot Prince's framing implicitly endorses the **plugin marketplace** model: pre-built plugins as job-function-shaped purchases. Ross Mike from the sister [[../ai-operating-system/off-the-shelf-vs-handbuilt-skills]] is the contrarian — but Ross's anti-distribution stance is for **Skills**, not necessarily for **Plugins**. The reconciliation:

- Skills (granular, operator-specific) — **build-your-own** (Ross Mike)
- Plugins (job-function bundles) — **marketplace is legitimate** (Prince, Wilson, Kanasani)

This is the cleanest reconciliation of the corpus's sharpest disagreement axis.

## Key Takeaways

- **Two-tier hierarchy**: Skills (single-task recipes) + Plugins (job-function bundles)
- **N=2 corpus convergence** (Prince + Wilson) — moderate confidence; worth re-confirming with first-party Anthropic docs when available
- **Unix-philosophy applied to AI** — small sharp tools (Skills) composing into pipelines (Plugins)
- **Reconciles the Camp A vs Camp B distribution debate** — build-your-own at Skill level, marketplace OK at Plugin level
- **Vault implication**: consider splitting `05 Skills/` to add `05 Plugins/` for bundle-level artifacts; not yet implemented

## Related

- [[overview]] — Cowork product positioning (taxonomy refined here)
- [[skills-to-plugins-pipeline]] — the codify-after-success pattern that authors Skills (this article refines the destination of that pattern)
- [[mcp-connectors-landscape]] — Plugins bundle Connectors; this article complements the Connectors discussion
- [[../ai-operating-system/skills-architecture-progressive-disclosure]] — sister-topic progressive-disclosure mechanism
- [[../ai-operating-system/off-the-shelf-vs-handbuilt-skills]] — sister-topic distribution debate; reconciled here
- [[external|Storm Bear: agent-skills-standard (v76)]] — the portable-skill format standard
