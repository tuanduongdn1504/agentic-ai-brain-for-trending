# (C) awesome-claude-skills — Project CLAUDE.md

> **Wiki v50 of Storm Bear corpus — CORPUS HALF-CENTURY MILESTONE.**
> Source: `ComposioHQ/awesome-claude-skills` (https://github.com/ComposioHQ/awesome-claude-skills)
> Routine: `05 Skills/llm-wiki-routine-v2.1.md` (8th v2.1-era execution)
> Started: 2026-04-25 / Shipped: 2026-04-25

---

## Phase 0 — Pre-flight summary

**Probe-vs-clone correction (CRITICAL)**:
- Initial probe estimated ~30 external skill links + ~30 in-repo subdirs.
- Cloned source reveals: **864 SKILL.md files / 905 directories / 832 entries inside `composio-skills/`** subdir.
- This is **NOT a small aggregator**. It is a **HYBRID at EXTREME primitive count** — aggregator README + bundled in-repo skill-library + 832-entry Rube-MCP-wrapper directory.
- **Primitive-count tier: EXTREME** (5th in corpus after ruflo v42 ~500 / aidevops v47 ~2,665+). 864 SKILL.md ≈ aidevops range / 1.7× ruflo.

**License correction (CRITICAL)**:
- README badge + `## License` section claims "Apache License 2.0".
- **Repo root has NO `LICENSE` file** (verified via `/bin/ls`).
- 9 in-repo skills have their own `LICENSE.txt` (Apache-2.0 verbatim) — these are the Anthropic-published skills wholesale-imported with original LICENSE preserved (artifacts-builder, brand-guidelines, canvas-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, webapp-testing).
- Other 22 top-level skills + 832 composio-skills entries carry NO license file at all.
- README acknowledges: *"Individual skills may have different licenses - please check each skill's folder for specific licensing information."*
- **Result**: corpus-first **absent-LICENSE-at-root-with-README-claim** sub-context (4th absent-LICENSE data point in corpus after bizos v37 / dive-into-llms v39 / others).

---

## 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE — Pattern #68 awesome-list-genre meta-pattern 4TH DATA POINT + audience sub-type c (AI-runtime-infrastructure-directory) reaches N=2** |
| **Archetype** | **Hybrid aggregator + bundled-in-repo skill-library + commercial-product-entry-as-skill** (corpus-first sub-variant within Pattern #68) — Composio commercial-AI-tool-infrastructure-startup |
| **Scale tier** | Large-XX-large (56,200 stars / ~6 months ≈ 9,367 stars/month sustained-aggregator-amplified-community-viral) |
| **Primary lang** | **Python 100% per GitHub linguist** (62 .py files = helper scripts inside top-level skills); content is markdown SKILL.md |
| **Packaging** | Plugin-marketplace-native via `marketplace.json` (corpus-first directory-scoped marketplace.json) + `claude --plugin-dir ./connect-apps-plugin` local-dir-plugin install + 31 top-level skills cloneable via clone-and-copy + 832 composio-skills wrappers consumed via Rube MCP runtime |
| **Origin story** | Commercial-startup (Composio Inc., founded 2023-03-21) + commercial-product-driven aggregator (lead-gen for Composio platform/Rube MCP) + active 6-month maintenance (created 2025-10-17) |
| **Methodology** | Awesome-list-genre meta-pattern + curation-as-runtime-infrastructure + commercial-product-as-fulfillment-layer (Rube MCP fulfills 832 of 864 skills) |
| **Governance** | **Light** (README 33KB + CONTRIBUTING.md 4.4KB + 9 per-skill LICENSE.txt; **NO root LICENSE / NO SECURITY / NO CODE_OF_CONDUCT / NO AGENTS.md / NO CLAUDE.md**) |
| **Agent/skill count** | **864 SKILL.md files** (corpus-first SKILL.md catalog at 800+ scale): 31 top-level skills + 832 composio-skills Rube-MCP wrappers + 1 marketplace.json at composio-skills/.claude-plugin/ |
| **i18n** | **EN-only** (notable absence at 56K + commercial-startup scale) |
| **Intellectual influence** | Tool-lineage (Anthropic skills system + Composio Rube MCP); explicit RECURSIVE CORPUS REFERENCE — lists `obra/superpowers` (Storm Bear v2 wiki subject) 5× across 5 different superpowers skills + lists `anthropics/skills` (referenced in v40 claude-context + others) — **Pattern #57 5th data point CORPUS-FIRST aggregator-mediated recursion** |
| **Agent platforms** | Universal Claude-Skills-compatible (Claude.ai + Claude Code + Claude API); `connect-apps-plugin` Claude-Code-specific (`claude --plugin-dir ./connect-apps-plugin` + `/connect-apps:setup`) |

---

## Phase 0.5 pattern pre-check (consolidation-forward; target: extend zero-streak to 14)

| Pattern | Action | Rationale |
|---------|--------|-----------|
| **#68 Awesome-List-Genre Meta-Pattern** | **STRENGTHEN N=4** | 4th data point in confirmed meta-pattern. Audience sub-type c (AI-runtime-infrastructure-directory) reaches N=2 (joins awesome-mcp-servers v31). NEW HYBRID SUB-VARIANT observation: aggregator-with-bundled-in-repo-skills (corpus-first; vs prior 3 pure-aggregator). |
| **#50 Commercial-Funnel Companion Platform** | **STRENGTHEN N=9 — corpus-strongest commercial-funnel observed** | UTM-tracked banner + dashboard.composio.dev + platform.composio.dev + connect-apps-plugin commercial-product-entry bundled-in-repo + "20,000+ developers" + 832/864 skills require Rube MCP commercial product to function. New observation: **commercial-product-as-fulfillment-layer-for-aggregated-skills** sub-variant. |
| **#29 License-Category-Diversity** | **STRENGTHEN — 4th absent-LICENSE sub-context** | "absent-LICENSE-at-root-with-README-Apache-2.0-claim" (badge + License section claim, no LICENSE file). 4th data point in absent-LICENSE-sub-category after bizos v37 / dive-into-llms v39 (and observation noted at v50). Per-skill LICENSE.txt variation in 9 of 31 top-level skills. Formalization-candidate at next mini-audit. |
| **#57 Recursive Corpus Reference** | **STRENGTHEN N=5 — CORPUS-FIRST aggregator-mediated recursion** | Lists `obra/superpowers` (Storm Bear v2 wiki subject) 5× (test-driven-development / brainstorming / root-cause-tracing / finishing-a-development-branch / using-git-worktrees) + `anthropics/skills` (corpus-shared dependency in v40 / others). 5th data point. NEW SUB-VARIANT: aggregator-mediated-multi-citation-recursion (vs direct-citation in prior 4). |
| **#17 Ecosystem-Layer Organizations variant 3 commercial-startup** | STRENGTHEN ~19th data point | Composio = commercial-AI-tool-infrastructure-startup; 70 public repos; composio.dev + dashboard + platform + AgentsKB sister + Rube MCP product. Strong variant-3 fit. |
| **#59 Plugin Marketplace Native** | **STRENGTHEN — corpus-first directory-scoped marketplace.json** | `composio-skills/.claude-plugin/marketplace.json` (v2.0.0; schema-referenced). Plus `connect-apps-plugin` separate plugin manifest. NEW SUB-VARIANT: directory-as-marketplace (vs 59a marketplace+npm OMC v27 / 59b marketplace-only claude-hud v35). |
| **#18 Agent Runtime Standardization (MCP layer)** | STRENGTHEN | Topics include `mcp` + `rube`; in-repo `mcp-builder/` skill specifically for building MCP servers; 832/864 skills require Rube MCP. Layer-1 MCP universal-adoption corpus reinforcement at aggregator scale. |
| **#19 archetype 4 no-explicit-individual-lineage** | STRENGTHEN | Composio cites no individual lineage (corporate-startup positioning); only org-level branding. |
| **#27 Community-Viral Scale Path** | STRENGTHEN ~22nd observation | 56K / ~6 months ≈ 9.4K stars/month sustained-aggregator-amplified-commercial-viral sub-path. |
| **#22 AGENTS.md** | STRENGTHEN aggregator-genre absence | NO AGENTS.md / NO CLAUDE.md at root (consistent with awesome-list-genre absence pattern). |
| **#2 Distribution Evolution** | STRENGTHEN | 4 surfaces: (1) clone-and-copy to `~/.config/claude-code/skills/`, (2) marketplace via Claude Code, (3) `claude --plugin-dir` local-dir, (4) Skills API programmatic. |

**Un-stale checks**: Pattern #45 (dual-licensing) — **NEGATIVE** (single-license claim, not dual). Pattern #52 (extreme-viral-velocity) — **NEGATIVE** (9.4K/month is sustained, not extreme; cf. #27 19th data point preserved). Pattern #74 (business-OS-as-product OT) — N/A. **All un-stale checks negative — disciplined.**

**Counter-evidence observations**:
- Pattern #12 governance-depth refined v42 3-factor: Composio = commercial-startup + medium-ambition (aggregator-as-lead-gen, not enterprise-platform) + medium scale → predicts light governance → CONFIRMED (no SECURITY / no CoC / no AGENTS.md). Refined formulation HOLDS.
- Pattern #22 AGENTS.md: aggregator-genre continues to abstain (build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31 / awesome-claude-skills v50 = 4/4 awesome-list-genre wikis without AGENTS.md). Genre-specific absence pattern.

**Consolidation-forward outcome**: 11 candidate observations evaluated → **0 new active candidates registered / 0 new OBSERVATION-TRACKs**. ALL routed to within-existing-pattern strengthening. **14-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK ACHIEVED** (v37-v50; extends v49's 13-streak; new corpus record).

**N=1 stale-risk-flagging**: N/A (zero new registrations).

---

## Phase 0.9 — Primitive-count flagging (5th EXTREME in corpus)

**Primitive surface**: 864 SKILL.md files / 905 directories / 31 top-level skills + 832 composio-skills wrappers + 70+ README categories + 4 distribution surfaces + 9 per-skill LICENSE files + 5 obra/superpowers references + ~120 external curated links.

**Outcome: EXTREME (5th in corpus)** — between ruflo v42 ~500+ and aidevops v47 ~2,665+. 864 SKILL.md is the densest single-file-type corpus observation (vs 1,792 .md in aidevops which were heterogeneous). **EXTREME sub-tier "skill-catalog-density"** observation (832 nearly-identical structured SKILL.md files in single subdirectory).

**Compression strategy**:
- 4-entity format preserved + aggressive citation-not-replication.
- 832 composio-skills cited as catalog-aggregate; only 1 sample (slackbot-automation) read end-to-end.
- 70+ App Automation README categories grouped, not enumerated per-skill.
- 5 follow-up deep-dive wikis flagged for v2.2:
  1. Rube MCP architecture deep-dive (commercial product underlying 832 skills)
  2. Composio toolkit ecosystem deep-dive (composio.dev/toolkits 1000+ apps)
  3. composio-skills/.claude-plugin/marketplace.json marketplace pattern deep-dive
  4. obra/superpowers cross-corpus recursion deep-dive (5-skill citation pattern)
  5. AgentsKB sister product deep-dive (agentskb.com)
- Velocity: ~3h target (within EXTREME +50-100% tolerance band; v47 aidevops baseline ~3h-3h 30min).

---

## Storm Bear meta-entity per-wiki applicability check (v2.1 Phase 0.9)

**APPLICABLE → 39th consecutive Storm Bear meta-entity (v10-v50).** Justification:
1. **Direct utility (MEDIUM-HIGH)**: Storm Bear vault has its own `05 Skills/` directory; awesome-claude-skills lists 5 skills directly relevant to vault automation (file-organizer, content-research-writer, meeting-insights-analyzer, tailored-resume-generator, changelog-generator).
2. **Pattern #57 recursion**: lists `obra/superpowers` (Storm Bear v2 wiki subject) 5× — corpus-mediated cross-validation.
3. **Architectural reference**: 864-SKILL.md catalog at scale = potential reference for Storm Bear publishing strategy (v27 diagnostic HIGH item #2).
4. **Marketplace.json template**: composio-skills directory-scoped marketplace.json could template a future Storm Bear public skill marketplace.

Frame entity as "awesome-claude-skills as Storm Bear skill-shopping list + recursion observation + 50-wiki milestone reflection".

---

## Cross-wiki ecosystem signals at v50

- **Pattern #57 RECURSIVE CORPUS REFERENCES (5 explicit + 1 implicit)**:
  - `obra/superpowers` (Storm Bear v2) cited 5× in awesome-claude-skills README
  - `anthropics/skills` (referenced in v40 claude-context + multiple) cited 5× in Document Processing + Development & Code Tools sections
- **Composio commercial product = Rube MCP** — corpus-first commercial product appears as fulfillment-layer for an aggregator's curated content (Pattern #50 corpus-strongest)
- **AgentsKB.com** sister product mentioned at README footer — outside-scope hint at Composio's broader product ecosystem
- **70 Composio public repos** — variant 3 commercial-startup-ecosystem strongest single-org evidence at v50

---

## Deliverables (13 files, this project)

1. CLAUDE.md (this file)
2. `01 Cluster Summaries/(C) Cluster 1 — README aggregator + 70+ categories + Anthropic skills + community curation.md`
3. `01 Cluster Summaries/(C) Cluster 2 — In-repo Composio-built skills + 832 Rube wrappers + skill-creator + plugin manifests.md`
4. `01 Cluster Summaries/(C) Cluster 3 — Composio commercial ecosystem + Rube MCP + UTM funnel + AgentsKB.md`
5. `02 Entity Pages/(C) awesome-claude-skills — Aggregator Core + Pattern #68 N=4.md`
6. `02 Entity Pages/(C) Composio In-Repo Skill Library + 832-Wrapper Catalog.md`
7. `02 Entity Pages/(C) Composio Commercial Ecosystem + Rube MCP + Pattern #50 Corpus-Strongest.md`
8. `02 Entity Pages/(C) Storm Bear Meta-Entity v50 — 50-Wiki Milestone + Pattern #57 Recursion Vector.md`
9. `03 Beginner Guide/(C) awesome-claude-skills — Beginner Guide.md` (bilingual VN+EN)
10. `04 Phase 4b Deliverable/(C) v50 — Pattern #68 4th + Pattern #50 Corpus-Strongest + 50-Wiki Milestone.md`
11. `05 Iteration Log/(C) v50 — awesome-claude-skills iteration log.md`
12. `INDEX.md`
13. `LOG.md` + `OPEN-QUESTIONS.md` (root)

---

## Reporting target (when complete)

- Deliverable count: 13
- Primitive-count tier: **EXTREME (5th in corpus)**
- Scope: outside-scope — Pattern #68 4th data point + sub-type c N=2
- Pattern Library delta: **0 new active candidates / 0 new OT** (consolidation-forward; 14-streak achieved)
- Storm Bear pilot ranking: skill-shopping pilot table refresh; primary recommendation = clone+copy 5 selected skills (~30 min)
- **v50 corpus half-century milestone observation**

---

## v27 diagnostic HIGH bundle status: **30 SESSIONS DEFERRED** (BLOCKING-RECOMMENDATION 6× threshold)

awesome-claude-skills provides 2 concrete reference assets for v27 HIGH bundle execution:
- **Item #1 (vault CLAUDE.md refactor)**: 864-SKILL.md catalog architecture as scale reference
- **Item #2 (Storm Bear publishing strategy)**: composio-skills/.claude-plugin/marketplace.json as concrete marketplace template

**STRONGLY RECOMMENDED**: Execute v27 diagnostic HIGH bundle before v51. 50-wiki milestone is natural cadence-break.
