# (C) Cluster 1 — README + IMAGE-BLAST workflow + multi-vendor BYOK at asset-generation layer

**Source bundle**: README.md (2,761 bytes; 7 sections) + repo description metadata.

## Verbatim taglines

1. *"An image-to-world skillset for Claude."* (GitHub repo description)
2. *"Creates 3D environments, SFX, and meshes from a single image using Claude skills, World Labs, and FAL."* (README first line)
3. *"Can take you from an image to a fully meshed 3D environment in < 5 minutes, great for jumpstarting 3D work. Go full blast."* (README tagline)
4. *"IMAGE-BLAST it."* (catchphrase repeated 5× in Examples section)

## README 7-section structure

1. **image-blaster** — title + tagline
2. **Quickstart** — `git clone` + `cd` + `claude` install via `curl -fsSL https://claude.ai/install.sh | bash` + paste World Labs + FAL API keys + put image in `input/` directory + "ask Claude to blast it and confirm each step with me"
3. **Description** — 3 output classes: (1) 3D models `.glb`/`.obj` of dynamic objects + (2) Gaussian splat `.spz` of static environment + (3) ambient looping + object-specific physics SFX `.mp3`
4. **Extensions** — embed under game-engine / DCC software / web-app: Unity / Unreal / Godot / Blender / 3DS Max / Maya / Three.js / Electron
5. **Advanced** — 5 generation models named: `marble-1.1` (World Labs explorable env) + `nano-banana` (default image-edit) + `gpt-image-2` (alt image-edit) + `hunyuan-3d` (FAL 3D object) + `elevenlabs-sfx` (ambient + per-object sound)
6. **Examples** — 5 IMAGE-BLAST use cases: video game level concepts + childhood bedroom + robot environment + film location scout + architectural rendering
7. **Development** — remove `/app` from `.claudeignore` to give Claude write-access to the React viewer

## Output asset taxonomy

| Output class | File extension | Use case | Source service |
|---|---|---|---|
| 3D static environment | `.spz` (Gaussian splat) | explorable static env | World Labs Marble 1.1 |
| 3D dynamic objects | `.glb`, `.obj` | per-object meshes | FAL Hunyuan-3D (or Meshy) |
| Ambient + physics SFX | `.mp3` | sound design | ElevenLabs SFX |
| Image edits | (images) | source cleanup + clean plates + object refs | nano-banana (default) or gpt-image-2 (alt) |

## Hunyuan parameters surfaced (corpus-record-detail at 3D layer)

Verbatim parameter table from README Advanced section:
- `--face-count <40000-1500000>` (default 50,000; Hunyuan API default 500,000)
- `--enable-pbr true|false` (default true)
- `--generate-type Normal|LowPoly|Geometry` (Normal = textured; LowPoly = polygon reduction; Geometry = white geometry-only; default Normal)
- `--polygon-type triangle|quadrilateral` (for LowPoly; default triangle)

## Multi-vendor BYOK at asset-generation layer (CORPUS-FIRST in v60+ window)

| External service | Provides | API key needed |
|---|---|---|
| **World Labs** | Marble 1.1 environment generation | YES (paste) |
| **FAL** | Hunyuan-3D object generation | YES (paste) |
| **ElevenLabs** | SFX (ambient + object) | implied (no explicit step but model named) |
| **nano-banana** | image-edit (default) | implied |
| **gpt-image-2** | image-edit (alternate) | implied |

= **4-5 external vendor API integration** with BYOK at asset-generation layer (vs v83's BYOK at LLM layer; vs v80's OpenAI + Gemini dual-LLM at decision layer).

Library-vocabulary candidate "Multi-Vendor BYOK at Asset-Generation Layer (Non-LLM)" PROVISIONAL N=1 — distinct from v83's "Local-First + BYOK-at-Every-Layer" at LLM-layer + v80's "LLM-Inversion-Architecture" at decision-layer.

## Distribution: single-method

`git clone` + `bun install` (implied) + `claude` CLI (installed via `curl -fsSL https://claude.ai/install.sh | bash`) + paste API keys + run.

= 1 distribution method vs v83's 4-method matrix + v75's `npx skills add`. **Lowest distribution-method count in T1 cluster post-v60.**

## Pattern Library implications (Cluster 1 scope)

| Pattern / Item | Evidence | Strength |
|---|---|---|
| **Pattern #52 SUSTAINED-MODERATE-HIGH sub-class N strengthening** | ~128/d × 30d at 25-150/d band | Sub-class N strengthening (joins v77 + v82-mid-window comparison) |
| **Library-vocab candidate "Multi-Vendor BYOK at Asset-Generation Layer"** | World Labs + FAL + ElevenLabs + image-edit-providers | PROVISIONAL N=1 |
| **CORPUS-FIRST 5-external-AI-model citation density in v60+ window** | marble-1.1 + nano-banana + gpt-image-2 + hunyuan-3d + elevenlabs-sfx | Within Pattern #57 sub-variant 57c-product (external-service citations, NOT corpus subjects) |
| **CORPUS-FIRST creative-tech-vertical T1 skill in v60+ window** | image-to-3D-world pipeline (not design-language, not coding, not Scrum) | NEW vertical observation |
| **IMAGE-BLAST verbal-catchphrase as identity-marker** | "IMAGE-BLAST it." repeated 5× | Within-pattern Pattern #82 quantitative-marketing sister observation |

## Cross-wiki siblings (Cluster 1)

- **v83 open-design** — 4-distribution-method matrix vs v84 1-method; both have multi-external-service integration but v83 at LLM-layer + v84 at asset-generation-layer
- **v80 SmartMacroAI** — LLM-Inversion-Architecture (LLM-as-tool-mode-option) sibling pattern at different layer (decision vs generation)
- **v79 autoresearch_folktales** — single-narrow-purpose subject sibling (LLM-training pipeline vs image-to-3D pipeline)

## Open questions specific to Cluster 1

- Whether `nano-banana` / `gpt-image-2` / `elevenlabs-sfx` are first-class API keys requested or implied via other services
- Whether v84 supports any harness besides Claude Code (`.cursor/` directory exists but `.cursor/rules` size not Phase 0 probed)
- Whether IMAGE-BLAST catchphrase is documented at any non-README artifact
