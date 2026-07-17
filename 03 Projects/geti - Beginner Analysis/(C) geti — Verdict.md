---
title: "(C) geti — Verdict"
subject: open-edge-platform/geti (Intel® Geti™)
wiki_version: v213
date: 2026-07-17
routine: LLM Wiki Routine v2.7
---

# Verdict · v213 · Intel® Geti™ (`open-edge-platform/geti`)

## Rating — GOAL-ALIGNED INCLUDE 3/4 (per §40)

| Axis | Call | Why |
|---|---|---|
| **(a) Anthropic-affiliation / registered (a)-7** | **FAIL** | Author = **Intel** (open-edge-platform). NOT Anthropic; no declared affiliation, no registered vendor-direct source. §41: no name/heritage/locale/notability rescue. **First Intel / open-edge-platform author** (#19 19a data-point). |
| **(b) Goal-relevance** | **MODERATE** (keys the tier) | The **domain** (computer-vision MLOps / annotate-train-deploy) is off both goals — but the repo ships a **genuine first-party agent-skill suite** (agentskills.io format; `getitune-*` product-usage skills that let a coding agent drive the whole vision-ML loop + dev skills), mirrored cross-harness (`.claude/` + `.agents/`), with `AGENTS.md`→`CLAUDE.md`. That agent-interface is squarely on the **agent-skills substrate the vault studies** + is a real **"how a product ships first-party skills to be operated by a coding agent"** template (directly relevant to making hireui agent-native). The **TimesFM v193 calibration**: off-domain, on-goal agent-interface. **STRONG defensible** on the skill-suite axis; **OFF-GOAL defensible** on the domain axis → **GOAL-ALIGNED per §40** (operator-requested goal-adjacent), OFF-GOAL CAPTURE recorded as the reviewable alternative. |
| **(c) Substance** | **STRONG** | Mature, large, formerly-commercial Intel platform; real annotate-train-optimize-deploy loop; SOTA catalog (RF-DETR/DINOv3/YOLO26/SAM3); OpenVINO export across Intel XPU + NVIDIA + CPU; `getitune` (the OTX successor) + CLI + a separate SDK; a genuinely well-authored first-party skill suite (per-step "Done when:" gates, committed-symlink cross-harness, sync/validate CI). 77 releases / v3.0.0. **Caveats:** NOT source-cloned (WebFetch/gh/docs); hard AI is upstream (model architectures + OpenVINO — Geti packages/orchestrates); stars page-stated (§37.4 → NOT #52); optional Ultralytics YOLO models = AGPL-3.0. |
| **(d) Connections** | **STRONG** | TimesFM v193 (direct precedent — off-domain product ships a first-party Claude Code agent skill; the DEFERRED "agent-native retrofit" watch axis) · palmier-pro v192 §C standalone (product-first app retrofitted with a first-party agent interface — but MCP vector; geti = SKILL vector → cross-ref/contrast) · the agent-skills-collection family (agent-skills v184 §C#4 / CodexKit v121 / karpathy v63 / agent-skills-standard v76 / OfficeCLI v206) · #84 84c cross-harness · #12 AGENTS.md-canonical-imports-CLAUDE.md · the ML-training/model-substrate tier (LlamaFactory v22 / Unsloth v23 / fish-speech v20 / DeepSpec v186 / GLM-5 v176 — geti = first computer-vision member) · magika v44 (Google ML classifier, loose) · **hireui agent-nativity template** (Goal #2). |

**§40** applies: an **operator-requested, goal-*adjacent*** subject defaults **GOAL-ALIGNED** on (b) MODERATE+, with the OFF-GOAL CAPTURE reading recorded as the equally-defensible operator/audit-reviewable alternative (the meetily v196 / TimesFM v193 / AIRI v210 handling). Gray-zone/goal-adjacent ≠ off-goal per §31.

## Pattern outcome — **NO MINT**

**Counts UNCHANGED: 46 top-level patterns / 11 CONFIRMED Library-vocab. §C live standalones 42 (unchanged). Tracked PROVISIONAL surface ≈49 (unchanged). Max top-level pattern #85 (unchanged).**

1. **Corpus-FIRST for the computer-vision / vision-MLOps annotation-train-deploy platform DOMAIN** — but **corpus-first-for-a-DOMAIN ≠ a mintable §C capability class** (the meetily v196 / TimesFM v193 / AIRI v210 discipline; §C vocab is capability/tool-shaped). → a **corpus-knowledge data-point + a DEFERRED watch axis** "computer-vision / vision-MLOps annotate-train-deploy platform (+ a first-party agent-skill suite to operate it)."

2. **The "product ships a first-party agent-skill suite to be operated by a coding agent" facet** — geti is a **richer 2nd instance on the SKILL vector** of the DEFERRED "product/model retrofitted to be agent-native via a first-party agent interface" watch axis:
   - **SKILL vector:** TimesFM v193 (one skill + Vertex endpoint) → **geti v213 (a full dev+usage suite, cross-harness, sync/validate-gated).**
   - **MCP vector:** palmier-pro v192 (first-party MCP server) → tabularis v212 (N=2, non-port).
   - Geti **strengthens** the DEFERRED axis but does **NOT** cross a mint bar (a packaging move, spread across two vectors; §28 anti-inflation; the axis was flagged DEFERRED at v193). The sharpest audit question this ship raises (recorded, not minted): **are the SKILL vector and the MCP vector one meta-class — "agent-native retrofit of a product-first application" — or two?** Defer to the ~v221 audit.

3. **⚠️ NOT a genuine N=3 of the palmier-pro v192 MCP standalone.** Geti is on the exact "product retrofitted to be agent-native" theme that tabularis v212 just took to N=2, but it **ships NO MCP server** (verified by full-tree grep). It is the **skill vector, not the MCP vector** — recorded explicitly so a future reader does not mis-file it as the v192 non-port N=3 (that role is still open for a Figma/Notion/Linear/Blender-class first-party-MCP product).

### Reviewable alternatives (operator / ~v221 audit)

- **(alt-1) §C standalone — "First-Party Agent-Skill Suite Shipped With a Product to Operate It"** (would credit TimesFM v193 + [weakly] OfficeCLI v206 + geti v213). Defensible on the serve-sim v183 / fff v194 corpus-first-for-surface precedent. **LOSES** to NO-MINT: the facet is a packaging/delivery move already tracked at the DEFERRED-axis + Pattern layer; §28 phantom-count; and OfficeCLI v206 is agent-FIRST (MCP-is-the-product) so the instance set is not clean.
- **(alt-2) §C standalone — "Computer-Vision Annotate-Train-Deploy Platform (agent-operable)"** (N=1). Defensible on the domain-first-mint temptation. **LOSES** on domain-not-capability (meetily v196 discipline) + not-world-first (Roboflow / CVAT / Label Studio / Encord / V7 / Landing AI populate the vision-MLOps/annotation space).

Either alternative → **counts UNCHANGED 46/11.**

## Secondary observations (recorded, NOT minted)

- **#19 19a** — first Intel / open-edge-platform author (institutional data-point; Intel a returning *hardware-name* only via "macOS Intel x64" build-target mentions, never a subject author).
- **#84 84c** cross-harness — one canonical `skills/` source, **committed symlinks** into `.claude/` + `.agents/`, portable agentskills.io frontmatter, per-skill `agents/openai.yaml`. **NO N-bump** (per v86; this is *not* the ponytail-v168 14-platform generator mechanism — it's a symlink mirror of one source).
- **#81-adjacent (manifest-drift-CI good-pole)** — `agent_skills.py sync` + pre-commit `validate` + CI `validate` keep the symlink manifest honest (the claude-seo v64 / financial-services v141 family). NO N-bump.
- **#12** — `AGENTS.md` (canonical, imports into `CLAUDE.md`) + `.claude/skills` + `.agents/skills`. Incidental; NO N-bump.
- **First-party-agent-skill-packaging cross-ref** — TimesFM v193 (one skill) / OfficeCLI v206 (auto-installed SKILL.md) / geti v213 (a full suite).
- **ML-training/model-substrate tier data-point** — geti = the **first computer-vision member** (LlamaFactory v22 / Unsloth v23 LLM-fine-tune · fish-speech v20 TTS · TimesFM v193 forecasting · DeepSpec v186 spec-decoding · GLM-5 v176 LLM). A platform-not-model sub-flavor.
- **#66 supply-chain** — `curl -fsSL install.sh | bash` / `irm install.ps1 | iex` + a large container/Windows app + a **local training engine that runs on your machine** + optional AGPL-3.0 YOLO models → install-snapshot + scratch-machine fence.

## Non-claims

NOT #52 (stars page-stated §37.4) · NOT #57 (no corpus subject cited as an influence — Datumaro/OpenVINO/HuggingFace/Ultralytics are non-corpus) · NOT a §C mint · **NOT a genuine N=3 of palmier-pro v192** (no MCP server — the skill vector) · NOT world-first (Roboflow/CVAT/Label-Studio/Encord/V7/Landing-AI precede; corpus-first-for-the-DOMAIN only) · NOT a new top-level pattern (max #85) · NOT the first ML-training subject (LlamaFactory v22 preceded; geti = first CV platform) · NOT the first MCP-server / Tauri-desktop subject (n/a) · NOT source-cloned (flagged).

## Tier

**T5 Application** (a full, human-usable, installable computer-vision MLOps platform) with a **first-party agent-skill-suite facet** (T1-flavored) — analogous to the TimesFM v193 provisional tier "domain model shipped as an installable package + a Claude Code agent skill," but a **platform**, not a model.

## Streak / §35

- Streak **GA:72 → GA:73** (59 consecutive goal-aligned ships v153→v213, under the GA reading; even under the OFF-GOAL reading of v213 the window stays clear).
- **§35 CLEAR** — window {v211 GA, v212 GA, **v213 GA**} = 0 OFF-GOAL (v212 audit is an audit, not a ship). Under the OFF-GOAL alternative reading of v213 = 1 OG ≤ 1 → still clear.

## Verification (per `feedback_wiki_verify_independently_check_collisions`)

✅ Verdict produced **INLINE + fully hand-verified** — **no workflow / no subagent relied on** (the ~205K shim overflows every subagent >200K → prompt-too-long; the v200→v212 self-throttle precedent). Source hand-fetched (rendered repo page + `gh` file/tree contents + raw README + AGENTS.md + `skills/README.md` + one product-usage SKILL.md + a full `develop`-tree grep for `mcp`); identity + commercial→OSS history + landscape by WebSearch; **collision + domain-first + the no-MCP fact + the "not-a-v192-N=3" call by sanity-anchored hand-grep** (anchors magika/timesfm hit → grep works; geti/open-edge/computer-vision/annotation = 0 hits; Intel hits = "intelligence"/build-target only). `inflation_check` HELD (0 mints; §C standalone alternatives DECLINED per §28 + recorded as reviewable; counts 46/11 unchanged; max #85; no N-bumps).
