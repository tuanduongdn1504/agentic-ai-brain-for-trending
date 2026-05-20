# (C) Entity 1 — Core product: 12-skill anti-slop bundle architecture

**Entity scope**: The taste-skill product itself — what you install, what it does, how the 12 skills interact, and what design-output guarantee it claims.

## Identity statement (verbatim where possible)

- **Repo**: [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)
- **Tagline**: *"Portable Agent Skills that upgrade AI-built interfaces: stronger layout, typography, motion, and spacing instead of boilerplate-looking UIs."*
- **Secondary tagline**: *"The Anti-Slop Frontend Framework for AI Agents."*
- **License**: MIT
- **Custom domain**: `tasteskill.dev`
- **Stars / Forks / Subscribers / Open issues / Age (Phase 0 snapshot 2026-05-20)**: 18,264 / 1,560 / 92 / 14 / 90 days

## 12-skill bundle composition (3-axis decomposition)

The 12 folders under `skills/` partition cleanly along 3 orthogonal axes:

### Axis A — Aesthetic-variants (4 skills)

| Skill | Folder | Purpose |
|---|---|---|
| Base aesthetic | `taste-skill` | Root brand-skill; default taste-rules |
| Minimalist | `minimalist-skill` | Centered/clean layout pole |
| Brutalist | `brutalist-skill` | Asymmetric/modern layout pole |
| Soft | `soft-skill` | Soft-design pole (less documented in README matrix) |

### Axis B — Workflow-variants (4 skills)

| Skill | Folder | Purpose |
|---|---|---|
| Redesign | `redesign-skill` | Improve existing UI |
| Image-to-code | `image-to-code-skill` | Translate visual reference → frontend code |
| Output-enforcement | `output-skill` | Enforce output format / quality gates |
| Stitch | `stitch-skill` | Compose layouts from parts |

### Axis C — Platform/extension-variants (4 skills)

| Skill | Folder | Purpose |
|---|---|---|
| GPT/Codex variant | `gpt-tasteskill` | Cross-platform skill for GPT/Codex harness |
| Image-gen web | `imagegen-frontend-web` | Image-gen reference for web frontend |
| Image-gen mobile | `imagegen-frontend-mobile` | Image-gen reference for mobile frontend |
| Brandkit | `brandkit` | Branding + identity layer |

**Clean 4 + 4 + 4 = 12 partitioning** strengthens "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" as a non-arbitrary architectural choice.

## Dimensional-control mechanism (setting-spectrum)

README explicit dimensions:
1. **Layout dimension** — *"lower: centered/clean · higher: asymmetric/modern"*.
2. **Motion dimension** — *"ranges from hover to scroll/magnetic"*.
3. **(Implicit) Density / spacing dimension** — taglines mention "spacing".
4. **(Implicit) Typography dimension** — taglines mention "typography".

**Granularity**: continuous-numeric vs discrete-tier (1-5) vs verbal-qualifier — **not pinned at Phase 0/2**. Open question for Phase 4.

**Mechanism placement**: dimensional settings likely live in per-skill `SKILL.md` files within the 12 folders. Setting-resolution at LLM-runtime (skill prompts the agent with specific dimensional positions per use).

## Framework-agnostic output discipline

README claims compatibility across:
- **React**
- **Vue**
- **Svelte**

Output is **design-intent rules + visual-pattern guidance** rather than framework-coupled boilerplate. This places taste-skill at **design-intent abstraction layer** above frontend-framework layer.

## What the product *does* (operational outcome)

1. User installs one or more of 12 skills via `npx skills add`.
2. User invokes Claude Code / Codex / Cursor with an installed skill active.
3. Skill prompts the agent with design-discipline rules + spectrum-tuned settings.
4. Agent produces frontend code (any of React/Vue/Svelte) following the design discipline.
5. Output should be **above the "slop" baseline** — non-default-LLM-aesthetic, with intentional layout/typography/motion/spacing choices.

## Architectural inversion vs v75 impeccable

| Axis | v75 impeccable | v81 taste-skill |
|------|----------------|-----------------|
| Skill count | **1 canonical skill** | **12 distinct skills** |
| Harness target count | **14 harness directories** | **~4 harness ecosystem** (Claude Code + Codex + Cursor + ChatGPT Images) |
| Multiplicity layer | **Distribution layer** (1 skill → many harness configs) | **Content layer** (many skills → fewer harness configs) |
| Author profile | Paul Bakaus — Creative Technologist at Google + jQuery UI | Leon Lin — Munich solo founder + 104-repo portfolio |
| License | Apache 2.0 + NOTICE.md (2-source derivative attribution) | MIT (plain, no derivative chain observed) |
| Pricing | OSS only | OSS + GitHub Sponsors (no Pro tier) |
| Brand surface | GitHub-native | Custom domain `tasteskill.dev` |

**Conclusion**: same T1 Assistant Skill / design-language tier; **inverted at layer-of-multiplicity dimension** = NEW sub-archetype "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" PROVISIONAL N=1 distinct from v75's "Single-Skill Multi-Target Distribution" archetype.

## Anti-slop philosophy as quality-curation product framing

**"Slop"** = boilerplate / generic / default-LLM-aesthetic UIs that emerge as path-of-least-resistance LLM frontend output.

**Anti-slop = quality-curation overlay product**:
- Not a vibe-coding-spectrum position (orthogonal to PRO-VIBE-explicit ↔ Anti-vibe axis).
- Design-aesthetic-quality axis specifically.
- Pattern #51 **NEW sub-pole candidate "Anti-Slop-Design-Curation"** PROVISIONAL N=1.
- Audit decision at v85: promote IF N=2 sustains OR retire as single-anchor-axis.

## Pattern Library implications (Entity 1 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW T1 sub-archetype "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy"** | 12-skill 3-axis-decomposable bundle + unified brand + setting-spectrum + portable install | **Phase 4b PRIMARY PROVISIONAL N=1** |
| **Pattern #52 N=4 HIGH-NOT-EXTREME** | 18,264 stars / 90 days = 202.93/d mid-life-cycle | STRONG strengthening |
| **Pattern #57 sub-variant 57c-product** | 4-harness ecosystem citation | STRONG within-pattern |
| **Pattern #51 NEW sub-pole "Anti-Slop-Design-Curation"** | Anti-slop framing on design-aesthetic-quality axis | PROVISIONAL N=1 |
| **Pattern #19 NEW sub-mechanism 19l candidate** | Munich-solo-founder + multi-skill-design-brand-portfolio | PROVISIONAL N=1 |
| **Library-vocabulary item #9 Cross-Pattern Coupled-Design** | 6+ pattern coupling at single subject | Strengthening |

## Open questions migrated from Cluster 1+2

- Settings granularity (continuous vs discrete vs verbal)
- `soft-skill` vs README 9-matrix discrepancy
- Per-skill SKILL.md cross-consistency
- Per-skill harness-coverage matrix
- @blueemi99 relationship
- Disclaimer section content
