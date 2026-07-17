---
title: "(C) geti — Pilot Methods Menu"
subject: open-edge-platform/geti (Intel® Geti™)
wiki_version: v213
date: 2026-07-17
---

# Pilot Methods Menu · v213 · Intel® Geti™

**The honest framing:** Geti's *domain* (computer-vision model-building) is off both of the vault's goals. Its *on-goal value* is the **agent-nativity architecture** — a mature, source-verifiable, cross-harness **first-party agent-skill suite** that lets a coding agent operate a real product end-to-end. **Read the seam, borrow the packaging discipline, apply it to hireui.** Only pilot the CV product itself if you have an actual vision project.

**⭐ One-thing path: A1 → B5 → D16** (read the first-party skill suite → distil the "how to ship a product's agent-skill suite" discipline into the vault + hireui spec → spec hireui's own first-party agent-skill suite on an `agent-*` branch).

**Fence (applies throughout):** `install-snapshot` before running `install.sh`/`install.ps1` (both are `curl|bash` / `irm|iex` installers pulling a **large container / Windows app** that runs a **local training engine**) · scratch machine / VM first · Apache-2.0 → safe to **borrow the skill-packaging patterns** · optional Ultralytics YOLO models = **AGPL-3.0** (don't productize those) · treat as **knowledge / architecture study**, don't adopt the CV product for hireui · hireui work per its CONSTITUTION (I-2 `agent-*` branch · I-8 operator-installs · GitNexus-first; no LLM spend yet → design/spec) · pin the release (v3.0.0) / commit.

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐ — Read the first-party agent-skill suite.** Study `skills/README.md` (the two-bucket layout, the portable-frontmatter authoring standard) + one `getitune-*` SKILL.md end-to-end. Internalize the shape: canonical `skills/` → committed symlinks into `.claude/` + `.agents/` → a model-invoked, portable, per-step "Done when:" skill. This is the reference artifact for the whole menu.
- **A2 — Read the cross-harness mechanism.** How `.claude/skills/<name>` and `.agents/skills/<name>` are *committed symlinks* into one source, kept honest by `agent_skills.py sync` + a pre-commit/CI `validate` gate (a manifest-drift good-pole). Contrast the ponytail-v168 generator (which copies rule files) and OfficeCLI v206 (auto-installs a SKILL.md).
- **A3 — Read `AGENTS.md`-imports-`CLAUDE.md`.** The "one canonical `AGENTS.md`, thin `CLAUDE.md` that imports it" pattern — a clean answer to the multi-harness instruction-file sprawl (#12). Compare to the vault's own `CLAUDE.md`.
- **A4 — Map the "agent-native retrofit" landscape.** Place geti on the two vectors: SKILL (TimesFM v193 → geti v213) vs MCP (palmier-pro v192 → tabularis v212). Write yourself a one-pager on when to make a product agent-native via *skills* (read/guided/multi-step ops with completion gates) vs *an MCP server* (structured, typed tool calls).

## B — Borrow patterns into the vault / a spec (zero or near-zero install)

- **B5 ⭐ — Distil "how to ship a product's first-party agent-skill suite" into the vault's `05 Skills/` authoring standard.** Canonical source + committed-symlink mirror + sync/validate gate + portable `name`/`description` frontmatter + **per-step checkable completion criteria** ("Done when: …") + a smoke-test-first step. This upgrades the vault's own skill discipline, zero install.
- **B6 — Steal the per-step "Done when:" completion-gate discipline** into any vault/hireui skill or loop (composes with agent-skills v184's verification gates + the vault's verify rule + the v189 loop-verifier).
- **B7 — Adopt the `AGENTS.md`-canonical / `CLAUDE.md`-imports pattern** as the standard for any repo you want operable by more than one harness (hireui, side projects).
- **B8 — Write a "make your product agent-native" decision doc** (skill-vector vs MCP-vector) into the vault, seeded from A4 — reusable for every future product decision.

## C — Hands-on trial (scratch machine, low risk)

- **C9 — Install-snapshot + install Geti on a scratch machine** (Docker container or the Windows app) and run the annotate → train → export loop on a public toy dataset (10–20 images) to feel the low-data interactive loop.
- **C10 — Install the `getitune-*` skills into a scratch `~/.claude/skills/`** (or clone + let the committed symlinks resolve) and **let Claude Code drive a `getitune` training run** end-to-end (discover model → prepare dataset → train 1 epoch → export OpenVINO). This is the *real* on-goal exercise: watch a coding agent operate a product through a first-party skill suite.
- **C11 — Measure the skill discipline.** Note where the per-step "Done when:" gates catch the agent (dataset-format error, shape error, missing checkpoint) — capture the failure modes as inputs to your own skill-authoring standard (B5).
- **C12 — Try `getitune` from the Python API directly** (`create_engine(...)` / `engine.train()`) in a scratch venv (`uv sync --extra cpu`) to separate "the engine" from "the agent skill that drives it."

## D — hireui / Goal-#2 (behind the CONSTITUTION fence)

- **D13 — Spec hireui's agent-nativity from geti's template.** Decide: should Claude Code operate hireui via a **skill suite** (geti/TimesFM vector) or an **MCP server** (palmier-pro/tabularis vector)? Recommendation: a **skill suite** for guided multi-step recruiter ops, an **MCP server** for typed data access (the tabularis v212 read-only pattern). Design doc on an `agent-*` branch.
- **D16 ⭐ — Spec hireui's own first-party agent-skill suite** (canonical `skills/` + committed symlinks + sync/validate gate + portable frontmatter + "Done when:" gates), e.g. `hireui-creating-a-requisition` / `hireui-screening-a-candidate` / `hireui-generating-an-offer` / `hireui-using-the-pipeline`. Compose with the palmier-pro v192 MCP-template thread + the OfficeCLI v206 offer-letter path + the career-ops v200 / miai-cv-matching scoring rubric. A completed spec on an `agent-*` branch = a real Goal-#2 artifact.
- **D17 — Wire a completion-gated screening skill.** Apply the "Done when:" discipline to hireui's first LLM feature (Match-Explain / candidate-scoring) so the agent proves each step before advancing — the fixed+legible+audited path the RATIFIED candidate-LLM legibility ADR requires.
- **D18 — (speculative, flag as thin) hireui + vision.** If hireui ever touches images (ID-doc verification, headshot moderation), geti is the on-prem, privacy-preserving, small-data vision trainer — but recruitment isn't computer vision; don't force it. Record as a "someday/maybe," not a pilot.

## E — Off-goal but real (personal use)

- **E19 — Any real computer-vision hobby/project?** Geti is a genuinely excellent low-data, 100%-local, no-cloud vision-model builder (10–20 images → train → OpenVINO export). Use it as-is; borrow nothing for hireui.
- **E20 — Edge deployment demo.** Export a model to OpenVINO and run it on a Core Ultra / Arc box to feel the "cloud-like capability at the edge" pitch — useful intuition for the Open Edge Platform space, off-goal for the vault.

## F — Vault-meta / audit follow-ups

- **F21 — File the DEFERRED watch axis** "computer-vision / vision-MLOps annotate-train-deploy platform (+ first-party agent-skill suite to operate it)" for the ~v221 audit.
- **F22 ⭐ — File the sharpest audit question:** are the **SKILL vector** (TimesFM v193 + geti v213) and the **MCP vector** (palmier-pro v192 + tabularis v212) **one meta-class** — "agent-native retrofit of a product-first application" — or two? Plus the reviewable §C-mint alternatives (alt-1 first-party-skill-suite; alt-2 CV-platform), both currently LOSE to NO-MINT.
- **F23 — Record geti as the first computer-vision member** of the model/training-substrate tier (LlamaFactory v22 / Unsloth v23 / fish-speech v20 / TimesFM v193 / DeepSpec v186 / GLM-5 v176) for the tier-taxonomy review.
- **F24 — Cross-ref the first-party-agent-skill-packaging thread** (TimesFM v193 / OfficeCLI v206 / geti v213) into `_patterns/06` §F as a tracked, non-minted facet.
