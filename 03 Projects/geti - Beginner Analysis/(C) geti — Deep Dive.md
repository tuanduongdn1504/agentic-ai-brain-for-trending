---
title: "(C) geti — Deep Dive"
subject: open-edge-platform/geti (Intel® Geti™)
wiki_version: v213
date: 2026-07-17
verdict: GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG] per §40 — NO MINT
author: Claude (Opus 4.8)
---

# Intel® Geti™ (`open-edge-platform/geti`) — Deep Dive · v213

> *"Build computer vision models in a fraction of the time and with less data."* — repo tagline
> *"Geti™ is an end-to-end Vision AI application that takes you from raw images to a deployed computer vision model."* — README opening

**Operator-requested** ("build LLM wiki for `https://github.com/open-edge-platform/geti`").

## What it is (one paragraph)

Geti is Intel's **end-to-end, open-source computer-vision AI platform** — an interactive application that takes you from *raw images* to a *deployed vision model* in one place: **annotate → train → optimize → run inference → improve** in a rapid train–predict–annotate loop, from as few as **10–20 labelled images**. It runs **locally** as a single container or a native **Windows app** (no cloud), and every model auto-exports with **OpenVINO™** for deployment across the full Intel® XPU portfolio (Arc GPUs, Core Ultra) — with NVIDIA® CUDA and CPU-only execution also supported. It ships a **state-of-the-art model catalog** (RF-DETR, DINOv3 DETR, YOLO26, Mask R-CNN, …), **smart annotation** (bounding-box → quick-selection → interactive segmentation, powered by Segment Anything / SAM3), active-learning sample selection, dataset import/export (COCO / Pascal VOC / YOLO / native), and covers classification, detection, instance/semantic segmentation, and keypoint detection.

The **training engine** is a library called **`getitune`** (published on PyPI as `getitune`) — the **successor to Intel's OpenVINO Training Extensions (`otx`)**, which this repo previously hosted (`otx` is now deprecated). Geti **v3.0.0** (Jun 18 2026) is the current release; the codebase is **Apache-2.0**, a shift from Geti's history as a **commercial/licensed Intel product** (part of the Intel Tiber Edge Platform; docs at `docs.geti.intel.com`). A separate SDK repo, `open-edge-platform/geti-sdk` (formerly `openvinotoolkit/geti-sdk`), provides a Python SDK for the platform.

## Facts (hand-verified)

| Field | Value | Provenance |
|---|---|---|
| Repo | `open-edge-platform/geti` | — |
| Tagline | "Build computer vision models in a fraction of the time and with less data." | GitHub desc (gh api) |
| License | **Apache-2.0** (optional Ultralytics YOLO models carry **AGPL-3.0**) | README + gh api |
| Languages | **Python 70.5% · TypeScript 27.3%** · SCSS/Just/Shell/PowerShell | GitHub page |
| Stars / forks | **~1.3k★ / 472 forks** — page-stated §37.4 → **NOT #52** | gh api (mocked metric) |
| Releases | **77**; latest **v3.0.0 (Jun 18 2026)** | GitHub page |
| Default branch | `develop` (git repo created 2018-10-26 as an internal Intel repo; open-sourced 2026) | gh api |
| Author org | **open-edge-platform** = **Intel** (Open Edge Platform); **NOT Anthropic** | gh + WebSearch |
| Homepage | `docs.geti.intel.com` | gh api |
| Training engine | `getitune` (PyPI `getitune`; successor to OpenVINO Training Extensions `otx`) | README |
| SDK | separate repo `open-edge-platform/geti-sdk` | WebSearch |
| Install | `curl -fsSL …/install.sh \| bash` · `irm …/install.ps1 \| iex` · Docker `ghcr.io/open-edge-platform/geti-${ACCELERATOR}` | README |
| System req | 8 threads / 16 GB RAM / 40 GB disk; GPU optional (Intel XPU or NVIDIA) | README |

## The load-bearing finding — a first-party AGENT-SKILL SUITE (the on-goal hook)

A plain computer-vision MLOps platform would be **off both of the vault's goals** (not Claude, not autonomous agents for software development, not recruitment). Geti is not plain. The repo root ships `AGENTS.md`, `CLAUDE.md`, and **three skill directories** — and this is what makes it a goal-*adjacent* subject rather than pure off-goal capture.

**One canonical `skills/` source, mirrored cross-harness by committed symlinks** (from `skills/README.md`, verbatim):

- `skills/` holds the canonical, repo-specific agent skills, grouped into two **buckets** — **Library** (`getitune`: models, recipes, training, export, optimization, inference, the `getitune` CLI) and **Application** (`geti`: FastAPI backend, React UI, the OpenAPI contract, the REST pipeline).
- `.claude/skills/<name>` and `.agents/skills/<name>` are **committed symlinks** into `../../skills/<bucket>/<name>` — *"so a fresh clone works for agents (no setup step)."* A `python3 .github/scripts/skills/agent_skills.py sync` regenerates them; a **pre-commit hook runs `sync` then `validate`**, and CI runs `validate` on the PR. (This sync-then-validate gate is a **manifest-drift-CI good-pole** — the claude-seo v64 / financial-services v141 family.)
- Skills follow the **open [Agent Skills](https://agentskills.io) format** — *"Write to the **portable core** so a skill works across every agent, not just one."* Frontmatter = the portable subset only (`name`, `description`, optional `license`); default to model-invoked skills. Each skill also gets an optional `agents/openai.yaml` interface file (`display_name`/`short_description`/`default_prompt`) — *"optional metadata for the OpenAI client [that] must not change portable behavior."*
- `AGENTS.md` is *"the canonical repo-wide instruction file for agentic tools"* and *"CLAUDE.md imports this file for Claude Code compatibility."*

**The 12 skills (directory-verified):**

*Dev-workflow* (build Geti with a coding agent): `geti-backend-dev` · `geti-ui-dev` · `geti-library-dev` · `geti-docs-update` · `geti-openapi-sync`.

*Product-usage* (a coding agent **operates** Geti / the `getitune` engine): `getitune-discovering-models` · `getitune-preparing-datasets` · `getitune-training-a-model` · `getitune-optimizing-a-model` · `getitune-exporting-a-model` · `getitune-running-inference` · `geti-using-the-pipeline`.

The product-usage skills are **genuine, well-authored operating skills**, not docs. From `skills/library/getitune-training-a-model/SKILL.md` (verbatim frontmatter):

> *"Train a computer-vision model with the getitune library … using its Python API or CLI. Use when a user wants to train, fine-tune, or evaluate a model with `create_engine(...)` and `engine.train()/engine.test()`, run `getitune train`/`getitune test`, pick or override a recipe under `getitune.recipe.<task>`, choose a device (cpu/gpu/xpu/cuda), warm-start from a checkpoint, or debug a training run."*

The skill body walks a coding agent through the workflow with **per-step checkable completion criteria** ("*Done when: `create_engine(...)` returns without a `ValueError`/`FileNotFoundError`*"; "*Smoke-test the wiring first with a tiny run before a long run*") — a discipline that echoes agent-skills v184's verification gates and the vault's own verify rule.

**There is NO MCP server.** Verified three ways: (1) AGENTS.md and `skills/README.md` contain zero references to "mcp"/"Model Context Protocol"; (2) a recursive git-tree grep of the whole `develop` branch for `mcp` returns nothing but the 12 `agents/openai.yaml` interface files. Geti's agent-nativity is delivered **entirely through the first-party Agent-Skill suite**, not an MCP server. This is the **TimesFM v193 vector** (a product/model that ships a first-party Claude Code Agent Skill), **not** the palmier-pro v192 vector (a product retrofitted with a first-party MCP server).

## Architecture (documented, not source-cloned)

- **`library/` (`getitune`)** — a low-code transfer-learning training engine. An `Engine` from `create_engine(model, data, work_dir, device)` pairs a model/recipe (YAML under `library/src/getitune/recipe/<task>/`) with an auto-detected dataset (via Datumaro; COCO/YOLO/VOC/native) and returns `engine.train()`/`engine.test()`. Two equal entry points (Python API + `getitune` CLI). Hardware extras: `uv sync` (cpu) / `--extra xpu` / `--extra cuda`.
- **`application/`** — the Geti product: `application/backend/` (FastAPI `geti`), `application/ui/` (React), the OpenAPI contract, the REST pipeline. Smart annotation + active learning + the train–predict–annotate UI loop.
- **`skills/`** — the first-party agent-skill suite (above).
- **Deployment** — every model exports to OpenVINO IR (and ONNX); runs on Intel XPU, NVIDIA CUDA, or CPU; optimizations incl. quantization / reduced-precision inference for edge.
- **2026.1 line** adds SAM3/SAM3.1 with a modular pipeline, HuggingFace integration, a dedicated OpenVINO backend, quantized-model support, and a label-free multi-category "canvas" training mode (from the Open Edge Platform 2026.1 release notes).

## Honest caveats

- **NOT source-cloned.** All facts are from the rendered repo page, `gh` file/tree contents, the raw README/AGENTS.md/skills-README, one product-usage SKILL.md, and Intel/WebSearch sources — no local clone was built (the ~205K CLAUDE.md shim overflows subagent context, so no deep-dive workflow was run; the v200→v212 self-throttle). Engineering internals below the file level are documented, not code-verified.
- **The hard AI is upstream.** The model architectures (RF-DETR, DINOv3, YOLO26, Mask R-CNN, SAM3) and the inference/optimization runtime (OpenVINO) are external; `getitune`/Geti orchestrate, package, and productize them into an annotate-train-deploy loop. The distinctive Geti contribution is the *platform* + the *low-data interactive loop* + the *first-party agent-skill suite*, not the model science.
- **Metrics are page-stated** (§37.4 — the GitHub API is mocked for stars/forks/dates); ~1.3k★ → this is **not** a Pattern #52 viral-velocity claim.
- **Optional Ultralytics YOLO models carry AGPL-3.0** — a license note distinct from the Apache-2.0 repo; don't productize those without accepting AGPL.
- **Formerly commercial.** Geti was a licensed Intel product (Tiber Edge Platform) before this Apache-2.0 open-sourcing; the "history" framing is corroborated by Intel's own product pages + HN threads, not by an explicit README statement.

## Corpus placement (hand-verified, collision-clean)

Sanity-anchored hand-grep of `_state/` + `_patterns/` (anchors `magika`=11 files, `timesfm`=2 hit → grep works):

- **`geti` / `open-edge-platform` / "computer vision" / "annotation" = 0 hits** → collision-clean; **corpus-FIRST for the computer-vision / vision-MLOps annotation-train-deploy platform DOMAIN**.
- **`Intel` hits are all "intel·ligence·/intel·lectual" or a "macOS Intel x64" build-target note** → **no prior Intel-authored subject** → geti is the **first Intel / open-edge-platform author** (#19 19a).
- **`YOLO` hits are GitHub *achievement badges*** on author profiles, not the object-detection model; the **"MLOps" hit is mlsysbook v197** (a *textbook that teaches* MLOps, not a CV platform); the **`OpenVINO` hit is a passing provider-list mention** ("OpenVINO Model Server" as one of 41 integrations in an aggregator subject).
- The corpus's ML-training/model neighbors — **LlamaFactory v22 / Unsloth v23** (LLM weight-space fine-tuning), **fish-speech v20** (TTS), **TimesFM v193** (forecasting FM), **DeepSpec v186** (speculative decoding), **GLM-5 v176** (LLM) — are all **different modalities/tasks; none is computer vision, none is an annotation platform.** Geti is the corpus's **first computer-vision member of the model/training-substrate tier.**

See the Verdict for the full 4-axis rating, the NO-MINT reasoning, the two reviewable alternatives, and the pattern-layer secondaries. See the Pilot Methods Menu for the 24-method application ladder.
