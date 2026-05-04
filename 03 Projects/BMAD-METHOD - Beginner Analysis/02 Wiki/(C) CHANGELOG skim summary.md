# (C) CHANGELOG skim summary — BMAD-METHOD

> **Source:** `CHANGELOG.md` (~94 KB, skimmed not read in full)
> **WebFetch:** 2026-04-19 (extraction pass for key milestones)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why skim, not full read

CHANGELOG is **94 KB** — approximately 1 year of dense release notes covering 5 major versions + 60+ alpha/beta iterations. Full ingestion would exceed entity-page utility. Strategy: extract **evolution arc + major version deltas + anomalies**, leave micro-version detail in source.

Pattern matches v10 autoresearch scripts-cluster approach (skim for structure, not completeness).

## 2. Five-phase evolution (v1 → v6) — one year, April 2025 → April 2026

| Version | Date | Theme | Milestone |
|---------|------|-------|-----------|
| **v1.0.0** | 2025-04-06 | **Foundation** | Initial tech demo — "specialized AI agent personas" for planning + execution |
| **v2.0.0** | 2025-04-17 | **Modularization** | Template Separation + quality validation checklists; agents decoupled from templates |
| **v3.0.0** | 2025-05-20 | **Orchestration** | Unified agent experience via orchestrator concept; web-first approach |
| **v4.0.0** | 2025-06-20 | **Professionalization** | Complete architectural overhaul; NPM package distribution; "from collection of prompts → distributable framework" |
| **v5.0.0** | — | **(Skipped)** | NPX registry corruption — version marker burned, development jumped to v6 |
| **v6.0.0** | 2026-01 (beta) | **Architecture Rebuild** | Skills-based architecture — "Everything now installs as a skill" |
| **v6.3.0** | 2026-04-09 | Current | Czech + Vietnamese translations; Amelia consolidation; community module browser; universal source support; Junie (JetBrains) |

**Arc:** tech demo → modular templates → unified orchestrator → NPM framework → skills rewrite. Each major is a conceptual breaking change, not just feature addition.

## 3. v5 NPX corruption — historical oddity

> CHANGELOG verbatim: *"Note: Version 5.0.0 was skipped due to NPX registry issues that corrupted the version. Development continues with v6.0.0-alpha.0."*

**Interpretation:** NPX registry state got into a bad place for the `5.0.0` marker. Rather than fight the registry, project burned the number and moved on. **Pragmatic decision** — preserves semver hygiene (never re-use a published number) at cost of version continuity.

Lesson for Storm Bear vault: document the quirk so future readers don't infer feature gaps between v4 and v6.

⚠️ **Correction to Phase 0 log:** Phase 0 said "NPM corruption" — CHANGELOG specifically says **NPX** (the npx runner / registry fetch path, not npm publish). Minor but accurate.

## 4. Release cadence — rapid within versions

| Interval | Days | Mode |
|----------|------|------|
| v1 → v2 | 11 | Sprint |
| v2 → v3 | 33 | Deliberate |
| v3 → v4 | 21 | Sprint |
| Within v4 | 40+ releases in ~3 months | **Weekly iteration** |
| v6 pre-release | 23+ alpha versions, Sep 2025 → Feb 2026 | **~2-3 weeks per alpha** |

**Signal:** high-velocity, alpha-heavy development. Users on `@next` tag see weekly churn; `@latest` stable releases come slower. CONTRIBUTING codifies this (see `CONTRIBUTING + AGENTS cluster summary`).

## 5. Breaking changes pattern — every 1-2 majors

- **v2** — template separation (existing users must restructure templates away from agents)
- **v4** — NPM architecture redesign (prompt-library users must migrate to framework)
- **v6** — skills conversion (everything installs as skill; v4 module layout is not v6 module layout)

**Frequency:** ~every major version. Users in production must budget migration time per major. **Not a "stable API" framework** — this is a churning methodology.

## 6. Module introduction timeline

| Module | First appearance | Notes |
|--------|------------------|-------|
| **BMM** (BMad Method core) | v4.0.0 | Fully established by v6 |
| **CIS** (Creative Intelligence Suite) | v4.10.0+ | Added mid-v4 iteration |
| **BMGD** (Game Dev Studio) | v4.20.0 introduced; major expansion v6.0.0-alpha.18 | Game dev focus added late |
| **BMB** (BMad Builder) | v6.0.0-alpha.14 | Workflow/module/agent builders — meta-tooling |
| **TEA** (Test Architect) | Through v6.0.0-alpha.23; moved to external module in v6.0.0-alpha.3 | Externalization signals maturity — TEA is separable |

**Architecture trend:** Core → domain-specific extensions → meta-builder → externalization. Mirrors how mature ecosystems evolve (core + stdlib + 3rd party).

## 7. v6.3 specifics (current release, April 9 2026)

**Major additions:**
- **Translations:** Complete Czech (cs-CZ) + Vietnamese (vi-VN) documentation sets
- **Agent consolidation:** Removed **Barry** (quick-flow-solo-dev), **Quinn** (QA), **Bob** (Scrum Master) → roles absorbed into **Amelia** developer persona
- **Community module browser:** Three-tier selection — (1) official, (2) community (category drill-down from marketplace index), (3) custom URL
- **Universal source support:** GitHub, GitLab, Bitbucket, self-hosted — plugin installation works across all
- **Junie (JetBrains AI)** platform support added

**Signal:** v6.3 = **ecosystem maturation** release. Less core feature, more platform reach + discoverability. Marketplace browser = BMAD moving toward distribution-hub model.

## 8. Amelia consolidation — why it matters

Three agents → one is a **trend signal**:

- v6.2 and earlier: Barry + Quinn + Bob + Amelia = 4 dev-adjacent agents with overlapping scope
- v6.3: Amelia absorbs all three, remains single Developer persona

**Interpretation:** BMAD team observed over-fragmentation. Users couldn't keep straight which agent for which task. Consolidation reduces cognitive load at cost of agent diversity. **Trend toward fewer, broader agents** — opposite direction from GSD (33 agents, deeper specialization).

Entity page `(C) 12+ Specialized Agents` (Phase 3) should lead with this consolidation as the headline v6.3 story.

## 9. Community module browser — marketplace emergent

v6.3's **official / community / custom-URL** tier = BMAD evolving from **framework → platform**. Parallels:
- NPM ecosystem (official modules / community packages / local installs)
- Claude Code plugin marketplace
- Cursor extensions

**Question:** will community modules ever be paid? Revenue model unclear. Logged to open questions (Q6).

## 10. Cross-references to siblings

- **GSD (TÂCHES)** — 33 agents, no consolidation trend (yet). BMAD diverges with Amelia merge.
- **gstack (Garry Tan)** — ~15 specialist roles, also corporate-backed. Similar "virtual engineering team" framing.
- **Superpowers (Jesse)** — TDD + 7-stage workflow, single-maintainer. Way less churn than BMAD.
- **ECC (Affaan)** — skills-based (parallels v6's conversion). Different scope.
- **autoresearch (Karpathy, T5)** — minimal release cadence, 1 author. Opposite of BMAD's multi-version churn.

## 11. Source skim strategy note

Full CHANGELOG has 60+ sub-versions with per-release changelogs. For wiki purposes, **majors + v6.3 + anomalies** are sufficient. If Storm Bear operator needs migration-guide specifics, direct link to repo CHANGELOG at a pinned version.

## Open questions surfaced from CHANGELOG

- What specifically broke in v5 NPX registry corruption? (Q4 existing)
- Will v7 come? What conceptual shift would warrant another major? → Q18
- Amelia consolidation proves fewer agents = better. Why do peers (GSD 33) go opposite direction? → Q19
- Community module browser launched v6.3 — how many community modules exist today? → Q20
