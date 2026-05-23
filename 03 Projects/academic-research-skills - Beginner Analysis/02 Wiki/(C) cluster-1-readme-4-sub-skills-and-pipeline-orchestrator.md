# (C) Cluster 1 — README + Repo Metadata: 4-Sub-Skill Architecture + 10-Stage Pipeline-Orchestrator + Material Passport Audit-Layer

**Source**: https://github.com/Imbad0202/academic-research-skills (README + repo metadata + release notes v3.9.2 2026-05-18)
**Fetched**: 2026-05-22 (Phase 0 + Phase 2 ingestion)
**Wiki version**: v90 (FIRST under routine v2.3 baseline)

---

## 1. Subject self-positioning

Self-tagline: *"A comprehensive suite of Claude Code skills for academic research, covering research, writing, peer review, and publication pipeline stages."*

Repo description verbatim from GitHub API metadata. Project scope is explicitly **academic-research vertical** with four named pipeline stages — research, writing, peer review, publication. This is corpus-first for an **academic-research-vertical T1 sub-archetype** in the v60+ window (no prior T1 Assistant Skill subject has been explicitly scoped to academic vertical; v76 agent-skills-standard was generic standards-layer, v77 easy-vibe was vibe-coding pedagogy, v85 ui-ux-pro-max-skill was design-vertical, v82/v83 were design-vertical).

## 2. 4-Sub-Skill Architecture with Independent Versioning

| # | Sub-skill | Version | Stage | Agent count |
|---|-----------|---------|-------|-------------|
| 1 | Deep Research | v2.8 | Research-gathering | 13 |
| 2 | Academic Paper | v3.0 | Writing | 12 |
| 3 | Academic Paper Reviewer | v1.8 | Peer review | 7 |
| 4 | Academic Pipeline | v3.7 | Publication / Orchestration | 10 |

**42 total agents** across the 4-sub-skill bundle. Each sub-skill carries an **independent SemVer-style version** — v2.8 / v3.0 / v1.8 / v3.7 — which is CORPUS-FIRST in v60+ window: prior multi-skill subjects (v75 impeccable 14-harness, v81 taste-skill 12-skill, v83 open-design 31-skill, v85 ui-ux-pro-max 18-platform) shipped without per-sub-skill independent versioning. The 4th sub-skill **Academic Pipeline** plays the **pipeline-orchestrator role** explicitly — distinct from a peer sub-skill — making the architecture not flat-multi-skill but **nested-with-orchestrator**.

This nested-with-orchestrator shape is the **load-bearing structural property** of the NEW T1 sub-archetype proposal at Phase 4b PRIMARY.

## 3. 10-Stage Publication Pipeline

The Academic Pipeline orchestrator drives a 10-stage explicit run-order:

1. Topic-selection
2. Literature-survey ingest
3. Outline draft
4. Section-level drafting
5. Citation insertion + bibliography construction
6. Peer-review simulation (via Academic Paper Reviewer)
7. Revision pass
8. Format compliance (journal-template adaptation)
9. Submission packaging
10. Post-submission audit (Material Passport audit-layer; see §5)

Each stage delegates to specific named agents from the 42-agent total. This is a **Linear-Workflow-Pipeline Skill Bundle** sub-archetype echo — but with explicit orchestrator (the Academic Pipeline sub-skill itself routes between stages), distinguishing it from v84 image-blaster which was Linear-Workflow-Pipeline WITHOUT explicit orchestrator (state-propagation-via-JSON-files only; flat 8-skill set with prose run-order).

Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" applies at install layer (see §4) — not at orchestrator layer. The orchestrator architecture is **internal to the bundle**, not a Pattern #84 axis.

## 4. 3 Install Channels

The subject ships **three parallel install pathways** — also CORPUS-FIRST in the multi-distribution axis for an academic-skill bundle:

1. **Claude Plugin Marketplace**:
   ```
   /plugin marketplace add Imbad0202/academic-research-skills
   /plugin install academic-research-skills
   ```
   This invokes the `/plugin marketplace add` install command — Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=2 STRENGTHENING (v85 ui-ux-pro-max-skill = N=1 anchor; v90 = N=2; **PROMOTION-ELIGIBLE at v95 audit**).

2. **Git + Symlink**:
   ```bash
   git clone https://github.com/Imbad0202/academic-research-skills.git ~/projects/academic-research-skills
   ln -s ~/projects/academic-research-skills/skills/* ~/.claude/skills/
   ```
   Symlink-to-`~/.claude/skills/` install pattern echoes v88 teleport clone-as-sibling-directory but with symlink (not direct clone-as-sibling-target).

3. **Codex Sibling Distribution**:
   Parallel installable for the Codex agent runtime — `.codex/` directory packaging adjacent to `.claude/` skills tree. This is a 2-harness narrow distribution (Claude Code + Codex), distinct from mega-distribution subjects like v85 (18 platforms) or v83 (16 harnesses).

**Distribution intent reading**: The 3-channel matrix balances **convenience** (Marketplace one-command) with **transparency** (git+symlink for power-user inspection) and **runtime diversity** (Codex sibling for non-Claude users). Not a v83-style 4-distribution-method matrix at single product layer because Codex is a separate runtime, not a separate distribution mechanism for the same artifact.

## 5. Material Passport Schema with Multiple Audit Layers

**Material Passport** is the subject's named artifact for tracking the **provenance, quality, and stage-readiness** of each generated artifact through the pipeline. The README describes it as carrying:

- Per-stage timestamp + agent-identifier ("which agent produced this output")
- Citation provenance ("which source backed which claim")
- Audit-layer annotations (peer-review verdicts, format-compliance flags, revision history)
- Material composition manifest ("what content blocks were drawn from where")

This is **CORPUS-FIRST "Material Passport" terminology** in the v60+ corpus. Library-vocab "Material Passport Schema with Multiple Audit Layers" PROVISIONAL N=1 registered at this wiki for v95 stale-check.

Functionally adjacent to v89 VibeCodingTracker cost-attribution-via-LiteLLM (both are quantitative-provenance-tracking-at-agent-output-layer) but axis differs: VCT tracks token/cost economics; Material Passport tracks academic-citation provenance + quality audit. Storm Bear vault application: Material Passport's audit-layer schema **could complement wiki-build quality-discipline** (per-cluster/entity-page provenance + fact-verification stamps + cross-reference integrity audit) — but functional-fit is INDIRECT (paper-writing ≠ wiki-curation), per Phase 0.9 (b) MODERATE PASS verdict.

## 6. 3-Locale i18n

The README and core SKILL.md files ship in **3 locales**:

- Traditional Chinese (zh-TW) — primary author locale
- Simplified Chinese (zh-CN) — Mainland reader coverage
- Japanese (ja) — secondary Asian-academic-market reach

This is a CORPUS-FIRST **Multi-Asian-Locale i18n (zh-TW + zh-CN + ja) at Single Subject** in v60+ window (v89 VibeCodingTracker had EN + zh-TW + zh-CN 3-Chinese-variant; v77 easy-vibe had 13-locale i18n; v83 open-design had 13-locale; but the **specific zh-TW + zh-CN + ja combination** — explicitly excluding English-primary — is a Taiwan-anchored Asian-academic-market positioning distinct from English-primary multi-locale).

Library-vocab "Multi-Asian-Locale i18n (zh-TW + zh-CN + ja) at Single Subject" PROVISIONAL N=1.

## 7. Quantitative Claims at README Surface

The README discloses several quantitative metrics:

- **31% citation error rate** from internal stress testing
- **$4-6 cost estimate** for a 15,000-word paper end-to-end pipeline run
- **42 agents** across 4 sub-skills (13 + 12 + 7 + 10)
- **10-stage** pipeline-orchestrator workflow
- **v3.9.2** latest release (bundle-level version on top of per-sub-skill versions)
- **422 commits** across project lifetime
- **3 install channels**

The 31% citation error rate is particularly noteworthy: **CORPUS-FIRST honest quantitative error-rate disclosure** at academic-research subject. Echoes Pattern #83 Honest-Deficiency-Disclosure (CONFIRMED at v69 N=5) but at a **specific metric layer** — error-rate-as-quantitative-disclosure rather than the more common feature-deficit-as-narrative-disclosure.

Library-vocab "Citation-Error-Rate-as-Honest-Quantitative-Disclosure" PROVISIONAL N=1.

## 8. Engagement Profile

| Metric | Value | Reading |
|---|---|---|
| Stars | 19,200 | Mega-scale active |
| Forks | 1,600 | Active-deployment 0.083 fork_ratio (moderate) |
| Watchers | 66 | NEGATIVE-EVIDENCE for v90 audit's CONFIRMED N=4 "Try-Once-and-Move-On Profile" — that pattern is **scale-correlated to micro-scale**; v90 mega-scale breaks it |
| Open issues | 23 | NEGATIVE-EVIDENCE for "Engagement-Deficit-Extreme-With-Active-Forks" CONFIRMED N=4 — also scale-correlated to micro-scale |
| Open PRs | 2 | Mild external contribution |
| Commits | 422 | Active maintenance |
| Latest release | v3.9.2 (2026-05-18) | Active release cadence |

The **NEGATIVE-EVIDENCE at mega-scale** for two CONFIRMED N=4 Library-vocab items is the most important Pattern Library finding at this cluster: it validates the v2.3 §20 "Density-not-scale-correlated" finding by **contrast** — Engagement-Deficit and Try-Once *are* scale-correlated to micro-scale, while Coupled-Design Density (also CONFIRMED N=4) is NOT scale-correlated. This is a **scale-correlation hypothesis** worth carrying to v95 audit for Library-vocab promotion-criterion refinement.

## 9. License: CC-BY-NC 4.0

Creative Commons Attribution-NonCommercial 4.0. This is **N=2 STRENGTHENING for the Pattern #45 CC-NC family sub-typology** (v77 easy-vibe was CC BY-NC-SA 4.0 = N=1 anchor; v90 academic-research-skills = N=2; v95 audit will check N=3 to determine promotion to sub-typology formalization or continued PROVISIONAL hold). Pattern #45 sub-typology taxonomy currently 5-variant (45a/b/c/d/e — Unlicense added at v90 audit); CC-NC family would become 45f or fold into 45c artifact-scope-split depending on framing-decision at v95.

The NC clause aligns with the academic-research context: non-commercial use only — consistent with university + individual researcher use cases the README explicitly addresses. No Pro tier or SaaS offering observed (unlike v78 ECC's dual MIT-OSS-plus-Pro-SaaS-tier).

## 10. Summary

This cluster establishes the **product structural surface**:
- 4 nested versioned sub-skills with 1 orchestrator role = nested-with-orchestrator architecture
- 42 agents + 10-stage explicit pipeline
- Material Passport audit-layer schema (corpus-first terminology)
- 3 install channels (Marketplace plugin + git+symlink + Codex sibling)
- 3-Asian-locale i18n (zh-TW + zh-CN + ja, no English primary)
- 31% citation error-rate honest-disclosure + $4-6 paper-cost
- CC-BY-NC 4.0 (Pattern #45 CC-NC family N=2 STRENGTHENING)
- Mega-scale engagement breaking 2 micro-scale-correlated Library-vocab profiles

**Phase 4b PRIMARY justification**: structural-membership criteria (academic-research vertical + nested-sub-skill architecture + pipeline-orchestrator role) are load-bearing for the NEW T1 sub-archetype proposal — Library-vocab vehicle is insufficient because 4-nested-versioned-sub-skill structure is a **structural property of T1 sub-archetype membership**, not a standalone vocabulary item.

See cluster-2 for owner-profile and Taiwan-cluster context, entity pages for Pattern Library implications, Phase 4b proposal document for sub-archetype registration detail.
