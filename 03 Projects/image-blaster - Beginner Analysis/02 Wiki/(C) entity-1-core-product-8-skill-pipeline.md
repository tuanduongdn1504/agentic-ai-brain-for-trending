# (C) Entity 1 — Core product: 8-skill image-to-world pipeline + IMAGE-BLAST workflow

**Entity scope**: What `image-blaster` IS, its 8-skill linear pipeline, the 5-example use-case framing, and architectural distinction from prior T1 skill bundles.

## Identity statement

- **Repo**: [`neilsonnn/image-blaster`](https://github.com/neilsonnn/image-blaster)
- **Owner**: Neilson K-S (SF solo indie creative-tech developer; neilsonks.com + @neilsonks)
- **Tagline (primary)**: *"An image-to-world skillset for Claude"*
- **Tagline (extended)**: *"Creates 3D environments, SFX, and meshes from a single image using Claude skills, World Labs, and FAL"*
- **Tagline (positioning)**: *"Can take you from an image to a fully meshed 3D environment in < 5 minutes, great for jumpstarting 3D work. Go full blast."*
- **License**: MIT
- **Stars / Forks / Subs / Issues / Age**: 3,836 / 379 / 39 / 5 / 30 days (Phase 0 fetch 2026-05-21)
- **Velocity**: ~128 stars/day SUSTAINED-MODERATE-HIGH sub-class N strengthening

## Product composition (compact)

### 8 named pipeline-step skills

| # | Skill | Role | External service |
|---|---|---|---|
| 1 | **image-blast-project** | Project envelope initializer + workflow router | (none) |
| 2 | **image-blast-plate** | Image plate cleanup (clean-plate gen) | (image-edit provider) |
| 3 | **image-blast-uncover** | Object extraction from scene | (image-edit provider) |
| 4 | **image-blast-world** | 3D static env (Gaussian splat `.spz`) | World Labs Marble 1.1 |
| 5 | **image-blast-3d** | Per-object 3D mesh (`.glb`/`.obj`) | FAL Hunyuan-3D / Meshy |
| 6 | **image-blast-sfx** | Ambient + object-specific SFX (`.mp3`) | ElevenLabs |
| 7 | **image-blast-image-edit** | Image editing helper | nano-banana default / gpt-image-2 alt |
| 8 | **image-blast-wildcard** | Escape-hatch / generic-fallback | (unverified) |

### Output asset taxonomy

- **3D models**: `.glb`, `.obj` (per-object dynamic)
- **Gaussian splat**: `.spz` (static environment)
- **SFX**: `.mp3` (ambient looping + object-specific physics sounds)
- **Image edits**: (helper outputs throughout pipeline)

### Engine + DCC compatibility (README Extensions section)

- Game engines: **Unity, Unreal, Godot**
- DCC software: **Blender, 3DS Max, Maya**
- Web/desktop apps: **Three.js, Electron**

### 5 IMAGE-BLAST example use-cases (verbatim README Examples)

1. Video game level concepts — `IMAGE-BLAST it.`
2. Your childhood bedroom — `IMAGE-BLAST it.`
3. Need an environment for a robot — `IMAGE-BLAST it.`
4. A film location scout — `IMAGE-BLAST it.`
5. An architectural rendering — `IMAGE-BLAST it.`

## Linear-Workflow-Pipeline architecture (NEW T1 sub-archetype candidate)

**Skill bundle organized as ordered pipeline-step decomposition with explicit run-order**:

```
project → plate → uncover → world ┐
                                   ├→ 3d → sfx
                                   ┘
                  image-edit helper (runs throughout pipeline)
                  wildcard (escape-hatch)
```

**Pipeline ordering enforced by**:
1. `image-blast-project` SKILL.md prose: *"Use before other image-blast skills"*
2. Project-skill's downstream-recommendation logic: reports inventory + identifies missing components + recommends sequential next-step agents in priority order
3. State files (`project.json` + `scene.json` + `image.json` + `object.json`) propagate state between pipeline steps

= **NEW T1 sub-archetype "Linear-Workflow-Pipeline Skill Bundle"** PROVISIONAL N=1 — distinct from prior T1 skill-bundle organizations.

## Architectural placement in T1 skill cluster

| Axis | v75 impeccable | v81 taste-skill | v82 huashu-design | v83 open-design | **v84 image-blaster** |
|---|---|---|---|---|---|
| Skill count | 1 monolithic | 12 sub-variants | 1 monolithic | 31 featured (~280 tree) | **8 pipeline-step** |
| Organization | single-skill-multi-harness | tri-axis taxonomy (4+4+4) | monolithic-60KB | featured + leaf-skill split | **ordered pipeline-step decomposition** |
| Harnesses | 14 | ~4 | 6 | 16 | **1 (Claude Code only)** |
| External services | none | none | image-edit | Anthropic + OpenAI + Gemini etc. (LLM layer) | **World Labs + FAL + ElevenLabs + image-edit providers (asset-generation layer)** |
| BYOK layer | none | none | LLM | LLM | **asset-generation (non-LLM)** |
| Run-order | N/A | N/A (variant select) | N/A | mode-switch | **explicit linear-pipeline** |
| Domain vertical | design-language | design-language | design-language | design-language | **creative-tech / image-to-3D-world** |

**v84 = first creative-tech-vertical T1 skill** in v60+ window (prior v75/v81/v82/v83 all design-language).

## Pattern Library implications (Entity 1 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW T1 sub-archetype "Linear-Workflow-Pipeline Skill Bundle"** | 8-skill ordered pipeline with explicit run-order + state propagation | PROVISIONAL N=1 |
| **CORPUS-FIRST creative-tech-vertical T1 skill in v60+ window** | image-to-3D-world pipeline (not design-language, not coding, not Scrum) | NEW vertical observation |
| **Pattern #82 quantitative-marketing density** | 5-example IMAGE-BLAST catchphrase repetition + 8-engine compat + 5-model citation | MID within-pattern |
| **Pattern #78 LDS density** | 8 SKILL.md + project.json/scene.json/image.json/object.json schema + settings.json + 2 hooks | MID within-pattern (below v83 STRONGEST) |
| **Library-vocabulary candidate "Multi-Vendor BYOK at Asset-Generation Layer (Non-LLM)"** | World Labs + FAL + ElevenLabs + image-edit-providers at asset-generation NOT LLM layer | PROVISIONAL N=1 |
| **Library-vocabulary candidate "Subtractive Prompt Synthesis Pattern"** | world skill builds "clean plate" caption by subtracting extracted objects from original scene | PROVISIONAL N=1 |
| **Library-vocabulary candidate "Atomic-Unit Skill Discipline"** | image-blast-3d "atomic object creation — excluding pairs, clusters, or adjacent items" | PROVISIONAL N=1 |

## Open questions specific to Entity 1

- Content of remaining 5 SKILL.md files (plate, uncover, sfx, image-edit, wildcard)
- Whether wildcard is true escape-hatch or specific-purpose-skill
- Whether 8-skill count is intended-final or expected-to-grow
- Whether atomic-unit discipline generalizes beyond 3d-object skill
