# Entity 3 — T1 domain-vertical-skill-collection NEW sub-archetype + Living-Domain-Standards Tracking NEW candidate

> **Type:** 2 NEW Pattern Library top-level candidates registered at v64
> **Pattern Library implications:** 2 NEW candidates N=1 stale-flagged at v64 (un-stale criteria specified)
> **Cross-references:** [Cluster 1 features section](./cluster-1-readme-and-commands.md) / [Cluster 2 architecture](./cluster-2-architecture-and-skill-system.md)

## NEW candidate 1 of 2: T1 Augmentation domain-vertical-skill-collection sub-archetype

### Definition

**T1 Augmentation skill-collection where 100% of primitives are scoped to a single domain vertical** (SEO, in claude-seo's case). Distinct from:

- **General-purpose collections** (e.g., mattpocock-skills v57 — 19 skills across coding/refactoring/git/etc., no single domain anchor)
- **Curated-meta aggregators** (e.g., awesome-claude-skills v50 — many skills, curated, not authored single-source)
- **Corporate-curated collections** (e.g., agent-skills-of-vercel v51 — Vercel-internal skill curation, multi-domain)
- **Single-artifact behavioral collections** (e.g., karpathy-skills v63 — 1 skill, behavioral-overlay, not a collection)

### Evidence N=1 at v64

claude-seo: **43 primitives total** (25 sub-skills + 18 sub-agents) all SEO-vertical:

- Technical SEO / E-E-A-T content / Schema / Sitemap / Images / GEO / Local + Maps / Hreflang / Google APIs / Backlinks / Cluster / SXO / Drift / E-commerce / Programmatic / Competitor pages / Plan / FLOW framework integration / DataForSEO + Banana + Firecrawl extensions

**Every single primitive is SEO-scoped.** No "git" / "refactoring" / "testing" / "documentation" skills. The vertical-specialization is the distinguishing axis, not the size.

### Sub-archetype criteria

For a future subject to register as N=2 evidence for this candidate:

1. ✅ **T1 Augmentation** (Claude Code surface, skill collection function)
2. ✅ **≥10 primitives** (not single-artifact like karpathy-skills; not toy-size)
3. ✅ **100% single-domain-vertical scope** (no general-purpose mixing)
4. ✅ **Author or org explicitly identifies the vertical** in README / CLAUDE.md / first paragraph
5. ✅ **Cross-skill workflow chains within the vertical** (not just standalone tools)

### Hypothetical un-stale candidates (watch list for v65-v70)

If/when published:
- **`claude-legal`** — 25+ legal-vertical primitives (contract analysis / litigation research / IP / compliance)
- **`claude-medical`** — 25+ medical-vertical primitives (clinical decision support / EHR / coding)
- **`claude-finance`** — 25+ finance-vertical primitives (financial analysis / compliance / reporting)
- **`claude-devops`** — could qualify if 100% DevOps-vertical (but aidevops v47 is closer to mixed; verify)
- **`claude-sales`** — sales/CRM/pipeline vertical primitives

**Un-stale criterion:** 2nd domain-vertical T1 collection appears in corpus. v64 N=1 stale-flagged with re-evaluation at v67 (+3 wikis) per standard stale-flag duration.

### Why this matters

The **vertical-specialization mechanism** is structurally distinct from prior T1 sub-archetypes. It implies a different go-to-market strategy (target domain practitioners specifically, not all Claude Code users), different community contribution discipline (Pro Hub Challenge specifically for SEO domain experts), and different cross-product portfolio shape (5-product SEO ecosystem vs general-purpose tooling).

**v64 wiki PROPOSES this as a NEW T1 sub-archetype candidate** — un-stale or retire at v67 audit.

---

## NEW candidate 2 of 2: Living-Domain-Standards Tracking

### Definition

**Agents codify external-authority quality-criteria with explicit deprecation-aware schemas + dated standards-version tracking** — distinct from coding-methodology codification (SDD/TDD/etc.). The agent tracks living external standards with versioned absorption discipline.

### 3 criteria (proposed)

1. **Explicit external-authority citation with date** (e.g., "Updated to September 2025 Quality Rater Guidelines")
2. **Deprecation-tracking discipline** (e.g., "HowTo: Deprecated (Sept 2023)" with deprecation date)
3. **Versioned absorption of external-standards updates** (release notes track when external standard moved, agent absorbed the change)

### Evidence N=1 at v64 — extensive within claude-seo

#### Criterion 1 — Versioned external authority citations

| External authority | Version cited | Where |
|---|---|---|
| Google Quality Rater Guidelines | **September 2025** | README "E-E-A-T Analysis" / `seo-content/SKILL.md` |
| Core Web Vitals | **LCP / INP / CLS current targets** (versioned) | README "Core Web Vitals" |
| Generative Engine Optimization | targets AI Overviews + ChatGPT + Perplexity (each platform versioned) | `seo-geo/SKILL.md` |
| Schema.org | versioned schema types (v29.4 additions noted in CHANGELOG v1.1.0) | `seo-schema/SKILL.md` + `schema/templates.json` |
| ISO 639-1 + ISO 3166-1 | hreflang language/region validation | `seo-hreflang/SKILL.md` |
| Anthropic Claude Code skill specification | **February 2026 spec compliance** | CHANGELOG v1.0.0 Architecture section |

#### Criterion 2 — Deprecation-tracking discipline

| Standard | Status | Date |
|---|---|---|
| **HowTo schema** | **Deprecated** | **September 2023** |
| **FAQ schema** | **Restricted to gov/health sites** | **August 2023** |
| **SpecialAnnouncement schema** | **Deprecated** | **July 2025** |
| **FID metric** | **Replaced by INP** | **March 12, 2024** |
| **FID in Chrome tools** | **Removed** | **September 9, 2024** |
| **YMYL-only E-E-A-T scope** | **Expanded to ALL competitive queries** | **December 2025 core update** |
| **ClaimReview schema** | Deprecated | (noted in CHANGELOG v1.1.0) |
| **VehicleListing schema** | Deprecated | **June 2025** (noted v1.1.0) |

**8 deprecation events tracked with specific dates** — this is **the strongest deprecation-tracking observed in any corpus subject to date.**

#### Criterion 3 — Versioned absorption of external-standards updates

| Release | External-standards absorption |
|---|---|
| v1.0.0 (2026-02-07) | INP-replaced-FID (March 2024) absorbed; HowTo/FAQ/SpecialAnnouncement deprecation absorbed; E-E-A-T per Sept 2025 Quality Rater Guidelines |
| v1.1.0 (2026-02-07) | E-E-A-T per December 2025 core update; Schema.org v29.4 additions (ConferenceEvent + PerformingArtsEvent + LoyaltyProgram); ClaimReview + VehicleListing deprecations; e-commerce schema `returnPolicyCountry` now required |
| v1.6.1 (2026-03-27) | Anthropic plugin spec compliance (auto-discovery transition); `model: sonnet` + `maxTurns` per agent standards |
| v1.7.0 (2026-03-28) | Google API integration (4-tier credential model per Google's API tiers as of release date) |
| v1.8.1 (2026-04-06) | Image SERP via DataForSEO (as DataForSEO added Google Images SERP coverage) |
| v1.9.0 (2026-04-14) | AGENTS.md format introduction (multi-platform skill discovery format as it emerged in 2026 corpus) |

Each release includes a tagged version-stamp on absorbed external-standards updates. **The agent INTERNALIZES the external standards' versioning system** rather than reasoning from a frozen snapshot.

### Distinction from existing patterns

**NOT Pattern #21 SDD Methodology Emergence** — Pattern #21 tracks coding-methodology codification (Specify → Design → Develop). Living-Domain-Standards tracks **external authoritative standards** that change OUTSIDE the agent (Google deprecates HowTo, agent absorbs).

**NOT Pattern #28 Progressive Disclosure** — Pattern #28 is about how to LOAD knowledge progressively. Living-Domain-Standards is about how to TRACK external authority versioning.

**NOT Pattern #18 Multi-Platform** — Pattern #18 is host-platform diversity. Living-Domain-Standards is external-authority diversity.

### Hypothetical un-stale candidates (watch list for v65-v70)

Subjects that could provide N=2 evidence:
- A **medical-coding skill collection** that tracks ICD-10 / ICD-11 version transitions + deprecated codes
- A **GDPR/privacy-compliance agent** that tracks GDPR amendments + dated case-law absorption
- A **clean-energy regulation agent** that tracks evolving FERC / NERC / state-PUC standards
- A **financial-reporting agent** that tracks GAAP / IFRS versioned updates
- A **localization agent** that tracks Unicode CLDR + ISO version transitions with deprecations

**Un-stale criterion:** 2nd subject in corpus with all 3 criteria satisfied. v64 N=1 stale-flagged with re-evaluation at v67 (+3 wikis).

### Why this matters

The **Living-Domain-Standards mechanism** is fundamentally different from frozen-knowledge codification. The agent has a **standards-tracking discipline** as a project invariant — every release must check if external standards moved + absorb changes + version-stamp them. The CHANGELOG itself becomes a **standards-absorption ledger**.

For Storm Bear vault relevance: this is interesting as a **knowledge-base maintenance discipline** at the agent level. The Storm Bear vault tracks wiki state + Pattern Library state + pilot state with version-discipline; claude-seo tracks SEO-external-standards with version-discipline. Same mechanism at different objects.

---

## Why these 2 NEW candidates are registered together

Both candidates **emerge from the same v64 subject** (claude-seo) and share a common structural property: **the project is built around tracking and codifying an external domain with explicit versioning and deprecation discipline.**

They are however **distinct claims**:

- **NEW T1 sub-archetype** = WHAT KIND of T1 collection (claim about T1 sub-taxonomy)
- **Living-Domain-Standards Tracking** = HOW the codification works (claim about mechanism)

A future subject could satisfy ONE without the other:
- A hypothetical `claude-legal` general-overview-skill (10 primitives covering legal vertical broadly without deprecation-tracking) = T1 domain-vertical YES, Living-Domain-Standards NO
- A hypothetical `code-generator` general-purpose with Anthropic-spec-versioning discipline = T1 domain-vertical NO, Living-Domain-Standards YES (Anthropic spec as external standard)

Both candidates therefore deserve separate registration. v66 audit deliberates them independently.

## Phase 5 registration plan

In `_patterns/03-active-candidates.md`, append two new entries:

```markdown
### Pattern #80 — T1 Augmentation Domain-Vertical-Skill-Collection (NEW v64 — N=1 stale-flagged)

**Definition:** T1 Augmentation skill-collection where 100% of primitives are scoped to a single domain vertical, with cross-skill workflow chains within the vertical.

**Criteria:**
1. T1 Augmentation (Claude Code surface, skill collection function)
2. ≥10 primitives
3. 100% single-domain-vertical scope
4. Author/org explicitly identifies the vertical in README first paragraph
5. Cross-skill workflow chains within the vertical

**Evidence:**
- N=1: v64 claude-seo (43 primitives, SEO vertical, 5-step cross-product workflow chain)

**Un-stale criterion:** 2nd domain-vertical T1 collection appears in corpus.
**Re-evaluate at:** v67 (+3 wikis).
```

```markdown
### Pattern #81 — Living-Domain-Standards Tracking (NEW v64 — N=1 stale-flagged)

**Definition:** Agents codify external-authority quality-criteria with explicit deprecation-aware schemas + dated standards-version tracking — distinct from coding-methodology codification.

**Criteria:**
1. Explicit external-authority citation with date
2. Deprecation-tracking discipline
3. Versioned absorption of external-standards updates (release notes ledger)

**Evidence:**
- N=1: v64 claude-seo (Google Quality Rater Guidelines Sept 2025 / Core Web Vitals / Schema.org / GEO platforms / 8 deprecation events with dates / CHANGELOG-as-absorption-ledger)

**Un-stale criterion:** 2nd subject satisfying all 3 criteria.
**Re-evaluate at:** v67 (+3 wikis).
```

Numbering tentative pending v66 actual audit (other NEW candidates may register in v65 wikis).

See [Entity 4 — multi-platform + full Pattern Library implications](./entity-4-multi-platform-and-patterns.md) for the complete v64 implications package.
