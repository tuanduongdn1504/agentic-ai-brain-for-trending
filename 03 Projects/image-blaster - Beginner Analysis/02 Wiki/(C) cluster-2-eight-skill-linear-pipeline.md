# (C) Cluster 2 — 8-skill `.claude/skills/` linear-workflow-pipeline architecture

**Source bundle**: `.claude/skills/` directory listing (8 sub-skills) + 3 SKILL.md files Phase 0 fetched (image-blast-project + image-blast-world + image-blast-3d) + settings.json allowlist enumeration.

## 8-skill enumeration (verbatim from `.claude/skills/`)

1. **image-blast-project** — project envelope initializer (run first)
2. **image-blast-plate** — image plate cleanup (clean-plate generation)
3. **image-blast-uncover** — object extraction from scene (identify removable objects)
4. **image-blast-world** — 3D static environment (Gaussian splat `.spz` via World Labs Marble 1.1)
5. **image-blast-3d** — single 3D object (per-object `.glb`/`.obj` via Hunyuan or Meshy)
6. **image-blast-sfx** — ambient + object-specific SFX (via ElevenLabs)
7. **image-blast-image-edit** — image edit helper (nano-banana default / gpt-image-2 alt)
8. **image-blast-wildcard** — (unverified; placeholder/escape-hatch skill)

## Linear-Workflow-Pipeline architecture (CORPUS-FIRST T1 sub-archetype candidate)

```
   ┌──────────────────────┐
   │ image-blast-project  │ ← run FIRST per SKILL.md ("Use before other image-blast skills")
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐    ┌──────────────────────┐
   │ image-blast-plate    │───▶│ image-blast-uncover  │
   │ (clean-plate)        │    │ (object extraction)  │
   └──────────────────────┘    └──────────┬───────────┘
                                          │
                          ┌───────────────┼───────────────┐
                          ▼               ▼               ▼
              ┌──────────────────┐ ┌─────────────┐ ┌──────────────┐
              │ image-blast-world│ │ image-blast │ │ image-blast  │
              │ (3D static env)  │ │     -3d     │ │     -sfx     │
              │ World Labs       │ │ (per object)│ │ (ElevenLabs) │
              └──────────────────┘ │ Hunyuan/    │ └──────────────┘
                                   │  Meshy      │
                                   └─────────────┘
   image-blast-image-edit ← helper, runs as needed throughout pipeline
   image-blast-wildcard   ← escape-hatch
```

**Pipeline step ordering** is enforced by `image-blast-project` SKILL.md verbatim claim *"Use before other image-blast skills"* + downstream-recommendation logic (project skill reports inventory + recommends sequential next-step agents in priority order).

= **NEW T1 sub-archetype "Linear-Workflow-Pipeline Skill Bundle" PROVISIONAL N=1** — distinct from:
- v75 impeccable: 1 skill × 14 harnesses (single-skill multi-target)
- v81 taste-skill: 12 skills × 3-axis taxonomy (aesthetic + workflow + platform variants)
- v82 huashu-design: 1 monolithic 60KB SKILL.md
- v83 open-design: 31 featured skills + ~280-tree (featured-vs-leaf-skill split)
- v84 image-blaster: **8 skills as ordered pipeline-step decomposition with explicit run-order**

## Per-skill methodology highlights (from 3 SKILL.md fetched)

### image-blast-project (entry-point + state-manager)
- Resolves project slug → creates `worlds/<slug>/` directory hierarchy
- Generates `project.json`, `scene.json`, `image.json` via project-state helper
- Stages images from `input/` to stable source paths
- Reports inventory + identifies missing components + recommends next agents in priority order
- **Workflow-orchestration role** (not just a skill — also the pipeline router)

### image-blast-world (Gaussian-splat static env)
- Uses highest-index visible image from `worlds/$0/source/` if no explicit image
- Synthesizes "clean-plate caption" by SUBTRACTING confirmed removed objects from original scene description (from `worlds/$0/image.json`)
- Calls World Labs helper with synthesized "empty environment" prompt
- Downloads all referenced world assets (`.spz` + colliders + panoramas + thumbnails) to local `worlds/$0/output/world/` paths
- **Local-first asset loading discipline** — frontend only accesses local files; World Labs URLs serve as provenance metadata only

### image-blast-3d (per-object 3D mesh)
- Validates inputs; requests missing world slug or object clarification
- Locates object definition or creates minimal intent JSON
- Generates "image-edit prompt" requesting **isolated object extraction** with verbatim discipline: *"white background, centered, tight crop, studio lighting"*
- Executes asset pipeline generator; reuses reference images on subsequent runs unless `--regenerate-reference`
- **Provider switch** between Hunyuan (default) + Meshy with distinct parameter sets:
  - Hunyuan: `--face-count`, `--generate-type`, `--polygon-type`, `--enable-pbr`
  - Meshy: `--target-polycount`, `--topology`, `--should-remesh`, `--enable-rigging`, animation settings
- **Atomic-object discipline**: "atomic object creation — excluding pairs, clusters, or adjacent items"

## Skill-architecture patterns observed

1. **Explicit run-order** (project-first) — enforced via SKILL.md prose + project-skill's downstream-recommendation logic
2. **Local-first asset loading** — world skill explicitly downloads + serves locally; cloud-URLs are provenance-only
3. **Atomic-unit discipline** — 3d skill creates ONE object per invocation (no pairs/clusters)
4. **Subtractive prompt synthesis** — world skill builds "clean plate" caption by subtracting extracted objects from original scene
5. **Provider abstraction with explicit parameter shape** — 3d skill supports 2 providers with distinct parameter taxonomies
6. **Reference-image caching** — 3d skill reuses references unless explicit `--regenerate-reference` (efficiency discipline)
7. **JSON state propagation** — project.json + scene.json + image.json + object.json files propagate state across pipeline steps

## Pattern Library implications (Cluster 2 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **NEW T1 sub-archetype "Linear-Workflow-Pipeline Skill Bundle"** | 8-skill ordered pipeline-step decomposition with explicit run-order + state propagation | PROVISIONAL N=1 |
| **CORPUS-FIRST atomic-unit discipline at sub-skill granularity** | image-blast-3d "atomic object creation" prose | Within-pattern Pattern #78 LDS sub-mechanism |
| **CORPUS-FIRST subtractive prompt synthesis pattern** | world skill builds "clean plate" caption by subtracting extracted objects | Library-vocabulary candidate PROVISIONAL N=1 |
| **CORPUS-FIRST local-first asset-loading discipline at sub-skill scope** | world skill downloads cloud assets to local paths; cloud URLs = provenance-only | Within-pattern Pattern #66 supply-chain sister observation |
| **Pattern #78 within-pattern LDS-density** | 8 SKILL.md + project.json + scene.json + image.json + object.json schema + 2 hooks + settings.json | Within-pattern strengthening (MID-density vs v83 STRONGEST) |

## Cross-wiki siblings (Cluster 2)

- **v81 taste-skill** — 12-skill bundle vs v84 8-skill pipeline (architectural-axis distinction: variant-taxonomy vs run-order-pipeline)
- **v83 open-design** — 31-featured + 280-tree vs v84 8-pipeline (scale distinction; v84 smaller + more-disciplined ordering)
- **v76 agent-skills-standard** — 259-skill bundle vs v84 8-pipeline (organization principle distinction: standards-library-by-framework vs run-order-pipeline)
- **v75 impeccable** — 1-skill-multi-harness vs v84 8-skill-1-harness (axis-of-multiplicity inversion)

## Open questions specific to Cluster 2

- Full content of remaining 5 SKILL.md files (plate, uncover, sfx, image-edit, wildcard) not Phase 0 fetched
- Whether `image-blast-wildcard` is an escape-hatch / generic-fallback skill or has specific purpose
- Whether sub-skill scripts under `.claude/scripts/` reveal additional helper architecture
- Whether `image-blast-project` skill is corpus-significant as a workflow-orchestration sub-archetype
