# gh-aw - Beginner Analysis — Claude Context

> **Wiki number:** 48 (corpus position)
> **Routine:** `05 Skills/llm-wiki-routine-v2.1.md` (9th v2.1-era execution)
> **Date:** 2026-04-25
> **Source:** `00 Source/gh-aw/` (full main branch tarball, 1.2 GB)
> **Source URL:** https://github.com/github/gh-aw

---

## Phase 0 — 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T4 Agent-as-bridge primary** (8th T4 entrant + NEW T4i sub-archetype: agentic-workflow-compiler-for-CICD). Bridge: human/agent intent (markdown) → executable GitHub Actions YAML (`.lock.yml`). Distinct from spec-kit v17 (T1 methodology) by being a CICD-execution bridge, not assistant-prompt-set. |
| **Archetype** | **GitHub-corporate-official-with-research-lineage** — github/* org direct ownership (2nd github/* corpus entry after spec-kit v17). Migrated from `githubnext/gh-aw` → `github/gh-aw` at v0.40.1 (2026-02-03), graduating from GitHub Next research org to mainline. Pattern #17 variant 2a sub-distinction strengthening (GitHub vs Microsoft vs Google big-tech-curator). |
| **Scale tier** | Medium (5-20K) — 4,367 stars at ~8.5 months ≈ 514 stars/month sustained-organic. Not viral; corporate-amplified-organic. |
| **Primary lang** | Go (cmd/gh-aw + cmd/gh-aw-wasm; 1,789 .go files in pkg/ alone, ~1,805 Go files total) + WASM variant + JS (`*.cjs` runtime-copied) + shell (`*.sh` runtime-copied). |
| **Packaging** | `gh extension install github/gh-aw` (GitHub CLI extension model) + `curl install-gh-aw.sh \| bash` + Homebrew (`brew install gh-aw` per CHANGELOG) — 3 install surfaces. |
| **Origin story** | Research-incubation-graduated-to-mainline. **GitHub Next research project** (Peli de Halleux + Don Syme + Eric Aftandilian + Krzysztof Cieślak) → graduated from `githubnext/` to `github/` org at v0.40.1 (2026-02-03). Distinct lineage signal — second GitHub-mainline entry after spec-kit but with research-incubation provenance. |
| **Methodology** | **Markdown-as-source-truth-compiled-to-YAML** + safe-output sanitization + compile-time validation + agentic-development dogfooding (core team uses Copilot agent + local agents to develop gh-aw; "we use our own tools to build our tools"). |
| **Governance file count** | **CORPUS-RECORD-TIER 12+ files** (LICENSE + README 21KB + AGENTS.md 49.8KB **CORPUS-LARGEST AGENTS.md** + CONTRIBUTING.md 27.8KB + DEVGUIDE.md 38KB + SECURITY.md + SUPPORT.md + DEADCODE.md + SKILL.md + CHANGELOG.md + CODEOWNERS + CODE_OF_CONDUCT.md + create.md + install.md + debug.md + .architecture.yml). **Beats aidevops v47** (which had multi-tier-distributed governance). |
| **Agent/skill count** | **EXTREME tier (corpus-near-record)** — 24 specialized skill subdirs in `skills/` + 22 pkg subdirs + 201 paired workflow `.md`/`.lock.yml` files in `.github/workflows/` + 63 scratchpad engineering notes + 22 docs + 3 specs. **Total primitive count ~3,200+** (1,805 .go + 1,224 .md). Comparable to aidevops v47 (~2,665+). |
| **i18n coverage** | **EN-only** (notable absence at github-corporate-official tier; spec-kit v17 also EN-only). |
| **Intellectual influence** | **CORPUS-FIRST research-lineage to GitHub Next**: Peli de Halleux (`@pelikhan`) + Don Syme (`@dsyme`, F# creator) + Krzysztof Cieślak (`@krzysztof-cieslak`, Ionide creator) + Eric Aftandilian (`@eaftan`). All 4 are GitHub Next researchers. **Pattern #19 archetype 2 methodology-lineage strengthening**: research-incubation→mainline-graduation as observable origin pathway. **First Don Syme + Krzysztof Cieślak corpus citations.** |
| **Agent platforms supported** | **5 first-class engines**: `copilot` / `claude` / `codex` / `custom` (extensible) + GitHub Actions runners as universal substrate. **MCP-first** (GitHub MCP server + custom MCP servers via gh-aw-mcpg gateway). |

## Phase 0.5 — pattern pre-check (v2.1 mandatory)

**Existing pattern strengthenings (consolidation-forward — DEFAULT):**

1. **Pattern #17 variant 2a corporate-official strengthening** — github/gh-aw is 2nd github/* corpus entry. Sub-distinction sharpens: spec-kit v17 = methodology framework (T1); gh-aw v48 = workflow-compiler bridge (T4). **Same parent github org, distinct product archetypes — confirms variant 2a accommodates multi-product portfolios.** STRENGTHEN, do not register new variant.
2. **Pattern #19 archetype 2 methodology-lineage strengthening** — GitHub Next research-incubation → mainline-graduation (`githubnext/gh-aw` → `github/gh-aw` v0.40.1) is observable origin pathway. 4 named GitHub Next researchers (Peli + Don Syme + Krzysztof Cieślak + Eric Aftandilian) constitute the research-cluster. **NOT a new individual-author node** (lineage-cluster, not single individual; analogous to Anthropic-team-cluster precedent at v34/v47). Strengthen archetype 2 with research-incubation-graduated-to-mainline observation.
3. **Pattern #18 MCP layer strengthening** — gh-aw + companion `gh-aw-mcpg` (MCP Gateway routing MCP server calls through unified HTTP gateway) = formal infrastructure layer above per-runtime MCP. **N=1 observation: "MCP-gateway-as-unified-routing-infrastructure"** — strengthen #18 (do not register new candidate).
4. **Pattern #22 AGENTS.md strengthening** — github-corporate-official with **49.8 KB AGENTS.md and NO CLAUDE.md alias** = corpus-largest AGENTS.md at github-corporate-official tier. **AGENTS.md-only sub-variant continues at corporate-official tier** (spec-kit v17 + gh-aw v48 both AGENTS.md-primary at github-org tier). Strengthen #22 sub-variant tracking.
5. **Pattern #28 Multi-Provider strengthening** — gh-aw supports 4 named engines (copilot/claude/codex/custom) + extensibility. **Engine-selection-as-frontmatter-axis sub-observation** — strengthen #28 (do not register).
6. **Pattern #66 Supply-Chain OBSERVATION-TRACK MAJOR STRENGTHENING** — gh-aw is **strongest corpus data point yet for transitive trust-boundary defense-in-depth**. SHA-pinned dependencies + AWF firewall (`gh-aw-firewall` — domain-based egress control) + MCP gateway (`gh-aw-mcpg`) + compile-time validation + tool allow-listing + sanitized `safe-outputs` + sandboxed execution + input sanitization + network isolation + human approval gates + W3C-style **Security Architecture Specification** (3 conformance levels) + SBOM (SPDX + CycloneDX) generation. STRENGTHEN OT (do not promote to architectural pattern; observation-track sub-category appropriate per v29 audit codification).
7. **Pattern #69 Agent-PR Fast-Track Governance Protocol companion observation** — gh-aw's "Traditional Pull Requests Are Not Enabled for non-Core team members" + "agentic plans in issues" = inverse-protocol observation. Where #69 documented `🤖🤖🤖` (contributor opt-in fast-track) + `lgtm`/`lgtmi` (maintainer approval), gh-aw observes **inverse**: non-core PR rejection by default + agentic-plan-in-issue convention. **Within-#69 observational** (not new candidate; consolidation-forward).
8. **Pattern #2 Distribution Evolution strengthening** — `gh extension install` + curl bash + Homebrew = 3-surface (medium for corpus; below crawl4ai/aidevops corpus-max tier).

**Un-stale check:** All 4 stale candidates (#45 / #52 / #71 / #72) checks negative. Disciplined.

**Counter-evidence check:**
- Pattern #12 Governance-Depth refined v42 3-factor model: gh-aw = corporate-official + heavy-governance (12+ files) — fits org-axis dominantly, **5th counter-evidence to "solo→light prediction" alongside claude-hud + pi-mono + ruflo + aidevops** (refined formulation HOLDS strongly).
- Pattern #22 AGENTS.md-only sub-variant: github-corporate-official entries (spec-kit v17 + gh-aw v48) preserve AGENTS.md-only convention even with Copilot+Claude+Codex multi-engine integration. **Counter-evidence to 22c authoritative-with-shim aidevops v47 sub-variant** — at github-corporate-official tier the 3-layer-shim inversion is NOT the convention.

**Overlap pre-check (v2.1 NEW Phase 0.6) — proposed candidates evaluated:**

| Proposed candidate | Overlap analysis | Decision |
|--------------------|------------------|----------|
| "Markdown-as-source-truth-compiled-to-YAML/CI" archetype | High overlap with Pattern #22 + Pattern #2 + spec-kit/aidevops corpus precedents | **REJECT standalone**; observe within Pattern #22 scope |
| "Research-incubation-to-mainline-graduation" lineage pathway | Within Pattern #19 archetype 2 | **REJECT standalone**; strengthen #19 |
| "Agentic-plan-in-issue inverse-PR governance" | Within Pattern #69 inverse-observation | **REJECT standalone**; observe within #69 |
| "MCP-gateway-as-unified-routing-infrastructure" | Within Pattern #18 strengthening (N=1 observational; needs N=2 for taxonomy extension) | **REJECT standalone**; strengthen #18 |
| "Engine-selection-as-frontmatter-axis" | Within Pattern #28 sub-observation | **REJECT standalone**; strengthen #28 |
| "Compile-time-validation defense-in-depth" | Within Pattern #66 OT strengthening | **REJECT standalone**; strengthen OT #66 |
| "W3C-style Security Architecture Specification" | Within Pattern #66 + Pattern #12 governance-depth | **REJECT standalone**; observe within both |
| "SBOM (SPDX + CycloneDX) supply-chain transparency" | Within Pattern #66 OT strengthening | **REJECT standalone**; strengthen OT #66 |
| ".architecture.yml file-line-count threshold manifest" | Novel primitive but N=1 observational; consolidation-forward | **DO NOT register**; observe within Pattern #12 governance-depth |
| "Compiled-lock-file convention (`.lock.yml`)" | Within Pattern #2 + observable; N=1 | **REJECT standalone**; observe within Pattern #2 |

**Outcome: 0 new active candidates target (extending zero-streak to 12 consecutive wikis v37-v48 — NEW LONGEST in corpus history, extends v47 11-streak).** 0 new OBSERVATION-TRACKs. Text-book consolidation-forward discipline application.

**Storm Bear meta-entity applicability check (Phase 0.9):**

Storm Bear meta-entity warranted for v48 because:
- **AGENTS.md template directness** — gh-aw 49.8 KB AGENTS.md + spec-kit v17 reference + aidevops v47 22c sub-variant = 3 corpus templates for vault CLAUDE.md refactor (v27 diagnostic HIGH item #1, deferred 28 sessions).
- **`skills/` directory pattern** — 24 specialized skill subdirs ≈ Storm Bear `05 Skills/` directory pattern. Direct architectural reference.
- **Markdown-as-source-truth philosophy** — gh-aw compiles markdown workflows to executable YAML, structurally parallel to Storm Bear vault-as-markdown-knowledge-base.
- **Research-lineage-graduation observable** — GitHub Next → mainline pathway is reference for any Storm Bear potential publishing trajectory.

**37th consecutive Storm Bear meta-entity** (v10-v48 streak preserved).

---

## Primitive-count flagging (Phase 0.9 + Phase 5)

- **Probed primitive-count: ~3,200+** (1,805 .go files + 1,224 .md files; 24 skill subdirs + 22 pkg subdirs + 201 paired workflow files + 63 scratchpad notes + 22 docs + 3 specs + 12+ governance files)
- **Outcome: EXTREME tier** (2nd in corpus after aidevops v47 ~2,665+; gh-aw is ~20% larger primitive surface)
- **4-entity allocation:**
  1. Core product (gh-aw CLI extension + workflow compiler + 5-engine support)
  2. Companion ecosystem (gh-aw-firewall AWF + gh-aw-mcpg MCP Gateway + gh-aw-actions library + GitHub Next research lineage)
  3. Pattern implications + T4 8-way + research-incubation-graduation + Pattern #66 strongest data point
  4. **37th consecutive Storm Bear meta-entity** (AGENTS.md template + skills/ pattern + markdown-source-truth)
- **Lossy compression accepted:** per-skill detail (24 skills) + per-engine config detail + per-workflow examples (201 workflows) + scratchpad notes (63) — citation-not-replication
- **5 follow-up deep-dive wikis flagged for routine v2.2:**
  - `gh-aw — Engine Architecture Deep Dive` (5-engine support: copilot/claude/codex/custom + per-engine constraints)
  - `gh-aw — Skills System Deep Dive` (24 specialized skill subdirs + skill-optimizer daily workflow)
  - `gh-aw — Security Architecture Spec Deep Dive` (W3C-style spec + 3 conformance levels + threat model)
  - `gh-aw — Companion Ecosystem Deep Dive` (AWF + MCP Gateway + gh-aw-actions library)
  - `gh-aw — Workflow Catalog Deep Dive` (201 paired .md/.lock.yml workflows + githubnext/agentics catalog)
- **Velocity expectation:** EXTREME tier ~3-3.5h (within +50-75% tolerance per aidevops v47 precedent)

---

## Phase 4b routing decision

**Primary mode: Tier-extension + new sub-archetype + research-lineage-strengthening** — T4 extends to N=8 with NEW **T4i agentic-workflow-compiler-for-CICD-bridge sub-archetype** (compiles markdown workflows → GitHub Actions YAML; distinct from 7 prior T4 sub-archetypes).

**Secondary mode: Pattern #66 OT strongest-data-point analysis** — defense-in-depth at corporate-official tier with W3C-style spec + SBOM + AWF firewall + MCP gateway + compile-time validation.

**Tertiary mode: Lineage-cluster observation** — research-incubation-graduated-to-mainline pathway via GitHub Next 4-researcher cluster (Peli + Don Syme + Krzysztof Cieślak + Eric Aftandilian).

---

## Cross-references (other corpus wikis)

- **spec-kit v17** — sister github/* corpus entry (T1 methodology). Same parent org, distinct product archetypes.
- **aidevops v47** — recent EXTREME-tier comparison (2,665+ vs 3,200+ primitives) + Pattern #28 cross-provider verification + Pattern #22 sub-variant 22c + AGENTS.md governance template.
- **awesome-mcp-servers v31** — Pattern #18 MCP-runtime-standard ancestor; gh-aw consumes MCP servers via gateway.
- **OpenHands v30** — academic-commercial fusion T5 SWE-agent peer (different tier, complementary positioning).
- **claude-howto v32** — Pattern #19 Boris Cherny 3rd-4th touchpoint precedent (Anthropic-team-cluster citation style); gh-aw uses GitHub Next research-cluster style.
- **OMC v27** — Pattern #18 Western-community OpenClaw precedent (gh-aw is GitHub-corporate-official, distinct positioning).
- **graphify v16** — T4 bridge sibling (code → knowledge graph; gh-aw = markdown → CI workflow; bridge family).
- **markitdown v28** — T4 corporate-narrow-utility precedent (Microsoft); gh-aw = github-corporate-broad-bridge.
- **claude-context v40** — T4 commercial-ecosystem-startup precedent (Zilliz); gh-aw is corporate-official non-commercial sibling.
- **rowboat v43** — Pattern #57 Recursive Corpus Reference precedent (implicit Karpathy); gh-aw has explicit GitHub Next lineage.

---

## Source materials clusters (Phase 2 plan)

1. **Cluster 1 — User-facing surface**: README.md (988 lines, ~120 actual content + ~860 community attribution) + create.md + install.md + debug.md + SKILL.md + Quick Start docs site link + Peli's Agent Factory blog reference + Companion projects section
2. **Cluster 2 — Contributor + agent governance**: AGENTS.md (49.8 KB) + CONTRIBUTING.md (27.8 KB) + DEVGUIDE.md (38 KB) + CODEOWNERS + CODE_OF_CONDUCT + DEADCODE.md + skills/ system + scratchpad/ engineering notes + agentic-development dogfooding philosophy
3. **Cluster 3 — Architecture + security + companion ecosystem**: cmd/ (gh-aw + gh-aw-wasm) + pkg/ (22 subdirs, 1,789 .go files, parser w/ //go:embed schemas) + actions/ (setup runtime file copying) + .github/workflows/ (201 paired .md/.lock.yml) + specs/ (W3C-style security architecture) + .architecture.yml + SECURITY.md + SBOM (SPDX + CycloneDX) + companion projects (gh-aw-firewall AWF + gh-aw-mcpg MCP Gateway + gh-aw-actions)

---

## Storm Bear pilot relevance (preliminary)

**Direct pilot candidacy: LOW** (requires GitHub Actions, write permissions, LLM API key, willingness to grant agents repo-write access — not casual evaluation; security responsibility binding).

**Observational value: HIGH-MEDIUM** for:
- AGENTS.md template (49.8 KB at corporate-official tier; concrete refactor reference)
- skills/ directory architecture (24 specialized skill subdirs; structural reference for vault `05 Skills/`)
- Compile-time validation philosophy (markdown specs validated before execution; reference for Storm Bear's potential validation discipline)
- Research-incubation-graduation pathway (if Storm Bear ever publishes externally)

**Pilot ranking estimate post-v48: Not in top 11.** Domain mismatch (CICD-workflow vs Markdown-knowledge-vault); HIGH friction (security-binding deployment).

---

## Next phases

- Phase 1: Project scaffolding (this CLAUDE.md ✅ + INDEX + LOG + OPEN-QUESTIONS)
- Phase 2: 3 cluster summaries
- Phase 3: 4 entity pages (incl. 37th consecutive Storm Bear meta)
- Phase 4a: Bilingual VN+EN beginner guide (~13 sections, security framing prominent)
- Phase 4b: T4 8-way + research-incubation-graduation + Pattern #66 strongest data point + EXTREME tier deliverable
- Phase 5: Iteration log v48 + Pattern Library updates (target: 0 new active candidates, 12-streak)
- Phase 6: Vault sync (PATTERN_LIBRARY.md + CLAUDE.md state block + project entry + GOALS.md session)

---

**Status: Phase 0 complete. Phase 1 scaffolding in progress.**
