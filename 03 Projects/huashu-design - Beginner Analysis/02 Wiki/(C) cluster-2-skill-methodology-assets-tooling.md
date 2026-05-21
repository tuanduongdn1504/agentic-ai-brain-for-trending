# (C) Cluster 2 — SKILL.md methodology + assets + tooling

**Source bundle**: `SKILL.md` (60,618 bytes) + `assets/` (SFX library + JSX components + showcases) + `demos/` + `references/` + `scripts/` (audio mixing + PPTX/PDF export + TTS pipelines) + `.env.example`.

## SKILL.md — 60KB monolithic skill specification

**Largest single skill file in corpus to date** (v82 60KB > prior largest observed in routine v2.2 window).

**Inferred role at Phase 0** (full content not Phase 2 fetched; structure inferred from README + tree):
- Single authoritative skill specification (vs v81 taste-skill's per-skill SKILL.md × 12 model)
- Likely enumerates the "5 schools × 20 philosophies" taxonomy = 100-item design-philosophy reference
- Probably covers the 5 Core Mechanics in operational detail
- Likely includes Anti AI-slop Rules CSS-technique exhaustive list
- May include workflow templates / output-format specifications / animation timeline DSL

**Library-vocabulary candidate** — monolithic-single-SKILL.md-as-comprehensive-domain-standards (distinct from v76 agent-skills-standard's 259-skill × 500-token-each O(1) hierarchical model; distinct from v81 12-skill SKILL.md per-folder model).

## assets/ directory — multimedia bundle

### `assets/sfx/` — Sound Effects library

Organized SFX categories:
- container
- feedback
- impact
- keyboard
- magic
- progress
- terminal
- transition
- UI

**CORPUS-FIRST sound-effects-library bundled with T1 design-skill** — neither v75 nor v81 ship SFX. Indicates v82's output format scope extends to video / animation / interactive presentations (MP4 + 60fps timeline confirms).

### `assets/showcases/` — example gallery

Demonstration projects across multiple themes:
- cover (presentation covers)
- infographic
- PPT (PowerPoint variants)
- website variants

**CORPUS-FIRST showcase-gallery bundled at scale** — heavy `assets/` content (222MB repo size driver).

### `assets/` JSX components

Frames + animations + HTML/JS assets for presentations.

**Pattern observation**: `assets/` mixed-format bundle (audio + JSX + HTML + JS) is unusual for a "design skill" — v82 is broader than design-only, it's a **multimedia-output-skill with design as one of N output modes**.

## demos/ directory

Interactive HTML demos showcasing design patterns and workflows. Distinct from `assets/showcases/`:
- `assets/showcases/` = example outputs (the skill PRODUCES these)
- `demos/` = interactive demonstrations (the user EXPLORES these to learn workflows)

## references/ directory — technical guides

Documentation on:
- Animation practices
- Audio design
- Workflows
- Video export
- Voiceover pipeline

**Library-vocabulary observation** — references/-folder-as-LDS-supplement (distinct from v74 LLMs-from-scratch bonus-folder vs main-chapter print-locked structure; v82 references/ = methodology supplements supporting the monolithic SKILL.md).

## scripts/ directory — automation tools

Shell + Node.js scripts for:
- Audio mixing
- Format conversion
- PDF export
- PPTX export
- TTS integration

**Output-format breadth axis**:
- v75 impeccable = design rules + CLI detector (zero-output-files; rules apply at agent runtime)
- v81 taste-skill = design rules + 12 skill prompts (zero-output-files; prompts apply at agent runtime)
- v82 huashu-design = **design rules + actual file-output pipelines** (HTML + MP4 + GIF + PPTX + PDF + voiceover audio)

**v82 is structurally distinct from v75 + v81** at output-pipeline-vs-prompt-only axis. v75 + v81 are "agent-guidance skills"; v82 is "agent-guidance skill + multimedia-output toolchain."

## Technology stack analysis

**Mixed-stack subject**:
- HTML (primary language per GitHub API)
- Adobe ExtendScript (JSX components in `assets/`) — uncommon in corpus
- Python (scripts/)
- Node.js (scripts/)
- Shell (scripts/)

**Pattern #84 84a Tool-tolerance evidence** — v82 doesn't constrain user's tool choice; rather, integrates with whatever toolchain user has + provides scripts to bridge. Tool-tolerant at output-pipeline layer.

## `.env.example` configuration

Suggests configurable runtime — likely API keys for TTS service or external service integrations. **No live secrets observed** at Phase 0 (only `.env.example` template; actual `.env` git-ignored).

## "5 schools × 20 philosophies" taxonomy (per README claim)

100-philosophy total framework. Specific enumeration NOT extracted at Phase 0 (would require SKILL.md full-fetch). Phase 2 cluster-2 deeper-fetch recommended for sub-typology evidence.

**If verified at later cycle**: 100-philosophy taxonomy at single design-skill = highest taxonomic-density observed in T1 design-skill cluster (v75 = 27 anti-pattern rules + 23 commands + 7 reference domains; v81 = 12 skills × 3 axes = 36 cells; v82 = potentially 100 philosophies = 2.7× density).

## Pattern Library implications (Cluster 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **Monolithic-single-SKILL.md as comprehensive-LDS** | 60KB single file | Library-vocabulary candidate |
| **Multimedia-output toolchain bundled with design-skill** | HTML + MP4 + GIF + PPTX + PDF + voiceover + SFX library + 60fps animation | CORPUS-FIRST in T1 design-skill cluster |
| **Pattern #84 84a Tool-tolerance evidence** | Mixed-stack agent-tooling integration via scripts/ | Within-pattern strengthening |
| **"Agent-guidance skill + multimedia-output toolchain" sub-typology distinction** | v82 vs v75/v81 prompts-only | Sub-typology candidate within T1 design-skill tier |
| **`references/` folder as methodology-supplement LDS layer** | Animation practices + audio design + workflows + video export + voiceover pipeline | Pattern #78 within-pattern observation |
| **`.env.example` + scripts/ external-service integration** | Runtime-configurable external services (likely TTS) | Pattern #66 supply-chain within-pattern |

## Cross-wiki siblings (Cluster 2)

- **v75 impeccable** — design rules + CLI detector model; v82 contrasts with output-pipeline bundle
- **v81 taste-skill** — 12 per-skill SKILL.md files; v82 monolithic 60KB SKILL.md
- **v76 agent-skills-standard** — 259-skill × ~500-token-each O(1) lookup model; v82 = single comprehensive monolithic
- **v74 LLMs-from-scratch** — main-chapter print-locked + bonus-folder LDS-evolution dual-layer; v82 SKILL.md + references/ similar dual-layer pattern at different domain

## Absences / open questions surfaced

- 5 schools × 20 philosophies enumeration — SKILL.md full-content unfetched
- Per-script behavior matrix (which output-pipelines work end-to-end at user-runtime?)
- TTS service identity (which provider does scripts/ integrate with?)
- JSX components actual usage (Adobe ExtendScript = After Effects integration likely)
- 60fps animation export mechanism (custom Stage + Sprite DSL or library-backed?)
- `.env.example` field list (configurable runtime parameters)

These migrate to expanded `(C) open questions.md` at Phase 4 pass.
