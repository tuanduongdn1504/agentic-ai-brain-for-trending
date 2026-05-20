# (C) Cluster 2 — 12-skill inventory + skills/ tree + llms.txt

**Source bundle**: `skills/` directory listing at `Leonxlnx/taste-skill`@main (GitHub API tree fetch) + per-skill folder names + `llms.txt` artifact at repo root + README "Skills" section 9-code-skill matrix.

## The 12 skill folders (verbatim folder names from GitHub tree fetch)

| # | Folder | Inferred category | README-matrix presence |
|---|--------|-------------------|------------------------|
| 1 | `taste-skill` | Base aesthetic | Yes (root brand-skill) |
| 2 | `minimalist-skill` | Aesthetic-variant: minimalist | Yes |
| 3 | `brutalist-skill` | Aesthetic-variant: brutalist | Yes |
| 4 | `soft-skill` | Aesthetic-variant: soft (unverified label) | **Discrepancy — not in 9-matrix?** |
| 5 | `redesign-skill` | Workflow: redesign existing UI | Yes |
| 6 | `image-to-code-skill` | Workflow: image-to-code translation | Yes |
| 7 | `output-skill` | Workflow: output-format enforcement | Yes |
| 8 | `stitch-skill` | Workflow: stitch / compose layouts | Yes |
| 9 | `gpt-tasteskill` | Cross-platform: GPT/Codex variant | Yes |
| 10 | `imagegen-frontend-web` | Image-gen for web frontend reference | Partial (image-gen bucket) |
| 11 | `imagegen-frontend-mobile` | Image-gen for mobile frontend reference | Partial (image-gen bucket) |
| 12 | `brandkit` | Branding + identity layer | Partial |

**Discrepancy flag**: README declares 9 code skills + 3 image-gen skills implicitly grouped. Folder count = 12. The 9-vs-12 gap maps to **3 implicit-grouping skills** (soft-skill + 2 imagegen-* variants treated as "1 image-gen umbrella + soft-as-variant-of-base").

## `llms.txt` artifact at repo root

**Presence verified** at Phase 0 via repo-tree fetch. **Library-vocabulary item #12 N=2 strengthening** (v77 easy-vibe was first PROVISIONAL N=1 instance with curriculum-routing `llms.txt`; v81 taste-skill is N=2 with skill-bundle-routing `llms.txt`).

**Inferred role** (not Phase 2 fetched yet; content speculative pending Phase 2 verification):
- AI-Agent-optimized index pointing LLM consumers at the 12-skill catalog.
- Likely enumerates skills + decision-criteria for which skill to load per intent.
- Distinct from v77's curriculum-stage routing (Stage 0-3 pedagogy mapping).
- Distinct from v75 impeccable's `HARNESSES.md` (harness-target routing).
- Distinct from v76 agent-skills-standard's `AGENTS.md` (provider-router 3-tier hierarchical lookup).

**4-instance Library-vocabulary item #12 sub-typology candidates** (4 consecutive wikis with distinct LLM-optimization-artifact-type — CORPUS-RECORD pattern-density):
- v75 = `HARNESSES.md` (harness-target router)
- v76 = `AGENTS.md` (provider-tier-lookup router)
- v77 = `llms.txt` (curriculum-stage router)
- v81 = `llms.txt` (skill-bundle-router)

Pending Phase 2 confirmation of v81 `llms.txt` actual content vs inferred role.

## 12-skill bundle architecture analysis

### Architectural choice: separate skills vs single-skill-many-modes

**Trade-offs surfaced**:

| Axis | Separate skills (v81 chosen) | Single skill many modes (hypothetical) |
|------|------------------------------|----------------------------------------|
| User explicit choice | Strong — user runs `npx skills add ... --skill "minimalist"` | Weak — mode-flag less discoverable |
| Independent evolution | Each skill can revise without cross-impact | Mode revisions risk regression on other modes |
| Install footprint | User installs only what they want | One install captures all modes |
| Documentation surface | Per-skill SKILL.md + curated examples per variant | One large SKILL.md with mode-branching |
| Brand portfolio surface | 12 distinct branded variants signal richness | One skill with internal toggle |
| Discoverability | High via folder enumeration on `skills/` | Lower (modes hidden inside one skill) |

**v81 chose separate skills** — consistent with "brand portfolio with sub-variant taxonomy" framing. **Architectural inversion** vs **v75 impeccable's 1-skill × 14-harness** approach: v75 = single canonical skill replicated across many harness targets (multi-target distribution layer); v81 = many distinct skills × fewer harness targets (multi-skill content layer).

### Setting-based dimensional control

README mentions:
- *"Layout experimentation (lower: centered/clean · higher: asymmetric/modern)"*
- *"Motion ranges from hover to scroll/magnetic"*

**Interpretation candidates**:
- (a) Continuous numeric per dimension (e.g., layout=0.3, motion=0.7).
- (b) Discrete tier per dimension (e.g., 1-5).
- (c) Verbal qualifier per dimension (e.g., "subtle"/"moderate"/"strong").

Mechanism granularity **unverified at Phase 0**; flag for Phase 2 deeper-fetch into per-skill SKILL.md to find exact setting-syntax. Continuous-vs-discrete distinction is a known open question.

### Sub-brand variant typology (12-skill decomposition)

**3 typological axes** observable in 12-folder layout:

1. **Aesthetic-variants** (4): `taste-skill` (base) + `minimalist-skill` + `brutalist-skill` + `soft-skill` — design-language-pole differentiators.
2. **Workflow-variants** (4): `redesign-skill` + `image-to-code-skill` + `output-skill` + `stitch-skill` — task-mode differentiators.
3. **Platform/extension-variants** (4): `gpt-tasteskill` + `imagegen-frontend-web` + `imagegen-frontend-mobile` + `brandkit` — platform-specific or auxiliary extensions.

**4 + 4 + 4 = 12 = clean tri-axis partitioning**, which strengthens the "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" Phase 4b PRIMARY proposal — the 12 skills aren't arbitrary; they decompose along 3 orthogonal axes (aesthetic / workflow / platform-extension).

## Per-skill SKILL.md governance

Each of the 12 folders likely contains its own `SKILL.md` (Claude Code skill standard) at minimum. **Not Phase 0 verified across all 12**. Phase 2 spot-check recommended:
- `taste-skill/SKILL.md` — base spec.
- `minimalist-skill/SKILL.md` — most-likely variant spec.
- `image-to-code-skill/SKILL.md` — distinct workflow spec.

Cross-skill consistency (shared header conventions / shared dimensional-spectrum references / shared brand-voice) is a key sub-typology question for Phase 4b proposal.

## Pattern Library implications (Cluster 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW T1 sub-archetype "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy"** | 12-skill folder layout + 3-axis decomposition (4 aesthetic + 4 workflow + 4 platform-ext) + unified brand + portable install | **Phase 4b PRIMARY PROVISIONAL N=1 registration** |
| **Library-vocabulary item #12 N=2 strengthening** | `llms.txt` artifact at root (v77 was N=1 PROVISIONAL → v81 N=2 PROMOTION-ELIGIBLE at v85) | STRONG strengthening |
| **Pattern #78 within-pattern LDS** | Per-skill SKILL.md × 12 + cross-skill design-spectrum dimensional-control = layered domain-standards | Within-pattern moderate |
| **Pattern #66 supply-chain** | 12 distinct install vectors (one per skill); broader attack-surface than 1-skill projects | Within-pattern strengthening |
| **Pattern #84 84c.1 N+1 strengthening at repo-stored layer** | Each skill addresses multi-harness target (Claude Code + Codex + Cursor + ChatGPT Images) | Within-pattern strengthening |
| **Library-vocabulary item #9 Cross-Pattern Coupled-Design** | Multi-skill bundle + setting-spectrum + multi-harness + brand-portfolio = 4-axis coupling | Strengthening |

## Cross-wiki siblings (Cluster 2)

- **v75 impeccable** — DIRECT SISTER + architectural inversion (1-skill × 14-harness vs 12-skill × ~4-harness).
- **v76 agent-skills-standard** — 259-skill codification at *standards layer* vs v81's 12-skill at *brand-portfolio layer*; distinct sub-typology under skill-collection meta-archetype.
- **v77 easy-vibe** — `llms.txt` N=1 → N=2 strengthening via v81.
- **v63 Karpathy nanochat-skills** — single-author multi-skill portfolio prior anchor.

## Absences / open questions surfaced

- **Per-skill SKILL.md content** not fetched (12 spec docs unread at Phase 0).
- **`llms.txt` actual content** not fetched (presence-verified only).
- **Setting-syntax** (continuous vs discrete vs verbal) unverified.
- **soft-skill alias-vs-undocumented** question unresolved.
- **Cross-skill consistency** (shared header / shared brand-voice / shared dimensional refs) unverified.
- **Per-skill harness-target enumeration** unverified (does every skill support all 4 harnesses or do some have narrower harness support?).

These migrate to expanded `(C) open questions.md` Phase 4 pass.
