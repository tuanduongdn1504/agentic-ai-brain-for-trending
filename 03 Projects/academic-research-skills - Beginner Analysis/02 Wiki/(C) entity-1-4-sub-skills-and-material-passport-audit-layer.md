# (C) Entity 1 — Core Product: 4-Nested-Versioned-Sub-Skill Architecture + 42-Agent Total + 10-Stage Pipeline-Orchestrator + Material Passport Audit-Layer + 31% Citation Error-Rate Honest-Disclosure

**Type**: Core-product entity
**Wiki version**: v90 (FIRST under routine v2.3 baseline)
**Sources**: cluster-1 (README + repo metadata), cluster-2 (owner profile context)

---

## Definition

`academic-research-skills` is a **Claude Code skill bundle for the academic-research vertical**, structured as 4 nested versioned sub-skills (Deep Research v2.8 + Academic Paper v3.0 + Academic Paper Reviewer v1.8 + Academic Pipeline v3.7) totaling 42 agents, orchestrated by the Academic Pipeline sub-skill across a 10-stage publication workflow, with **Material Passport schema** tracking per-stage audit provenance, and an honestly disclosed **31% citation error rate** at the README surface.

## Why this is a single entity (not 4)

The 4 sub-skills are deliberately **packaged as a single bundle** under one repository + one Marketplace install + one release version (v3.9.2 bundle-level on top of per-sub-skill versions). The orchestrator role of Academic Pipeline (4th sub-skill) is the **integration layer** that makes the 4 sub-skills cohere into a publication pipeline rather than a loose collection. Treating them as 4 separate entities would lose the **orchestrator architecture** which is the load-bearing structural property of the proposed NEW T1 sub-archetype.

This is structurally distinct from v81 taste-skill's 12-skill multi-skill-brand-portfolio (no orchestrator; flat sub-variant taxonomy) and from v84 image-blaster's 8-skill linear-workflow-pipeline (no explicit orchestrator sub-skill; state-propagation-via-JSON-files only). v90 academic-research-skills sits at a **distinct structural point** in the multi-skill design space.

## Architecture details

### 4-Sub-Skill Decomposition

| Sub-skill | Version | Agent count | Role |
|---|---|---|---|
| Deep Research | v2.8 | 13 | Source-gathering, literature-survey, citation extraction |
| Academic Paper | v3.0 | 12 | Drafting, section-level writing, format compliance |
| Academic Paper Reviewer | v1.8 | 7 | Peer-review simulation, revision feedback |
| Academic Pipeline | v3.7 | 10 | Orchestration, stage-routing, Material Passport stamping |

**Independent SemVer per sub-skill** is CORPUS-FIRST in v60+ window for nested-sub-skill subjects.

### 10-Stage Pipeline (Academic Pipeline orchestrator)

The Academic Pipeline sub-skill routes the work through 10 stages, delegating to specific agents from the 42-agent total at each stage. See cluster-1 §3 for the full stage list.

### Material Passport schema

Per-stage artifact carries:
- Timestamp + producing-agent-identifier
- Citation provenance (source-to-claim mapping)
- Audit-layer annotations (peer-review verdicts, format-compliance flags)
- Material composition manifest

CORPUS-FIRST "Material Passport" terminology in v60+ window. **Library-vocab "Material Passport Schema with Multiple Audit Layers" PROVISIONAL N=1** registered for v95 stale-check.

### 31% citation error rate honest-disclosure

The README surface discloses internal stress-testing measurement: **~31% of citations produced by the pipeline contain errors** (URL mismatches, attribution errors, fabricated references). This is CORPUS-FIRST quantitative-error-rate honest-disclosure at academic-research subject. **Library-vocab "Citation-Error-Rate-as-Honest-Quantitative-Disclosure" PROVISIONAL N=1** registered.

Echoes Pattern #83 Honest-Deficiency-Disclosure (CONFIRMED N=5 at v69 promotion + v90 audit re-verification) but at a **specific quantitative-metric layer** rather than narrative-disclosure layer. Pattern #83 sub-mechanism 83f sister-candidate "Quantitative-Error-Rate-Disclosure" PROVISIONAL N=1 — distinct from existing 83f.1/.2/.3/.4 sub-variants which are license-declaration-vs-actual-mismatch axes.

### 3 Install channels

1. Claude Plugin Marketplace (`/plugin marketplace add` + `/plugin install`) — Pattern #84 84c.1 sub-sub-mechanism "Marketplace-Plugin-Install" N=2 STRENGTHENING (v85 N=1 + v90 N=2; PROMOTION-ELIGIBLE at v95)
2. Git clone + symlink to `~/.claude/skills/`
3. Codex sibling distribution (`.codex/` parallel packaging)

### 3-Locale i18n

zh-TW (primary) + zh-CN + ja. CORPUS-FIRST specific Multi-Asian-Locale (no English-primary) at single subject in v60+ window.

## Pattern Library implications

### Strengthening events

| Pattern / Library-vocab | Type | Implication |
|---|---|---|
| Pattern #84 84c.1 "Marketplace-Plugin-Install" | Sub-sub-mechanism N=1 → N=2 | PROMOTION-ELIGIBLE at v95 |
| Pattern #45 CC-NC family | Sub-typology N=1 → N=2 | v77 + v90; v95 N=3 watch |
| Pattern #83 sub-mechanism 83f sister-candidate "Quantitative-Error-Rate-Disclosure" | NEW PROVISIONAL N=1 | v95 first-cycle stale-check |
| Library-vocab "Engagement-Deficit-Extreme-With-Active-Forks" (CONFIRMED N=4 at v90 audit) | NEGATIVE-EVIDENCE at mega-scale | scale-correlated to micro-scale only |
| Library-vocab "Try-Once-and-Move-On Profile" (CONFIRMED N=4 at v90 audit) | NEGATIVE-EVIDENCE at mega-scale | scale-correlated to micro-scale only |
| Library-vocab "Coupled-Design Density Not Scale-Dependent" (CONFIRMED N=4 at v90 audit) | Re-verification at mega-scale | density observed at mega-scale subject = CONFIRMS scale-independence |

### NEW registrations at v90

| Item | Type | Status |
|---|---|---|
| **T1 sub-archetype "Academic-Research-Skill-Suite with Pipeline-Orchestrator"** | NEW T1 sub-archetype | PROVISIONAL N=1 |
| Library-vocab "Material Passport Schema with Multiple Audit Layers" | NEW Library-vocab | PROVISIONAL N=1 |
| Library-vocab "Citation-Error-Rate-as-Honest-Quantitative-Disclosure" | NEW Library-vocab | PROVISIONAL N=1 |
| Library-vocab "Nested-Versioned-Sub-Skill Architecture with Pipeline-Orchestrator" | NEW Library-vocab | PROVISIONAL N=1 |
| Library-vocab "Multi-Asian-Locale i18n (zh-TW + zh-CN + ja) at Single Subject" | NEW Library-vocab | PROVISIONAL N=1 |
| Pattern #83 sub-mechanism 83f sister-candidate "Quantitative-Error-Rate-Disclosure" | NEW sister-candidate | PROVISIONAL N=1 |

## Comparison to peer multi-skill subjects

| Aspect | v75 impeccable | v81 taste-skill | v84 image-blaster | v85 ui-ux-pro-max | **v90 academic-research-skills** |
|---|---|---|---|---|---|
| Multiplicity layer | 1-skill × 14-harness | 12-skills × ~4-harness | 8-skill linear-pipeline | 1-skill × 18-platform | **4-nested-versioned-sub-skill × ≥2-harness** |
| Orchestrator | None | None | None (state-via-JSON-files) | None | **YES (Academic Pipeline sub-skill)** |
| Sub-skill versioning | N/A | Shared | Shared | N/A | **Independent SemVer per sub-skill** |
| Vertical | Design | Design | Creative-tech (image→3D) | Design (UI/UX) | **Academic-research** |
| Agent total | N/A | N/A | N/A | N/A | **42 agents** |
| Honest-disclosure | NOTICE.md attribution | None observed | None observed | None observed | **31% citation error-rate** |
| Audit-layer schema | None | None | None | None | **Material Passport schema** |

The unique combination of (orchestrator + independent-versioning + academic-vertical + 42-agent + Material-Passport + error-rate-disclosure) makes v90 a **structural NEW T1 sub-archetype** rather than a Library-vocab variant within existing T1 sub-archetypes.

## Functional fit for Storm Bear vault (Phase 0.9 (b) MODERATE)

- **DIRECT-FIT mapping**: academic-paper-writing ≠ wiki-curation. Vault does not produce papers.
- **INDIRECT-FIT adaptation**: Material Passport audit-layer schema could **complement** wiki-build quality-discipline (per-cluster/entity provenance + fact-verification stamps + cross-reference integrity audit). Estimated adaptation effort 4-8 hours to extract the schema-shape from `Imbad0202/academic-research-skills` and re-cast for wiki-artifact provenance.
- **LOW-COST-OF-TRIAL**: `/plugin marketplace add Imbad0202/academic-research-skills` ≤5-min install, reversible.

**Pilot ranking**: Position #5 CONDITIONAL — NOT recommended for unconditional pilot. If Storm Bear ever needs **provenance-audit-discipline** for vault artifacts (a future state, not current), revisit Material Passport schema as adaptation source.

## Suggested next-action (vault application)

Do NOT install the full bundle. Instead, when Material Passport adaptation becomes valuable for vault provenance-discipline, fetch the specific Material Passport schema files from `Imbad0202/academic-research-skills/skills/academic-pipeline/material-passport.md` (or equivalent) and read in isolation — no install required for schema-extraction.
