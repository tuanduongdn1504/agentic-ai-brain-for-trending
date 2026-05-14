# Pattern #78 Living-Domain-Standards Tracking — N=2 promotion proposal

> **Audience:** v66 mini-audit deliberation (accelerated) OR v67 stale-check (default)
> **Wiki:** v65 claude-code-system-prompts (2026-05-13 → 2026-05-14)
> **Status:** Top-level candidate registered N=1 stale-flagged v64 → **N=2 v65 wiki ship (1-wiki turnaround — FASTEST in 64-wiki corpus history)** — promotion-eligible under criterion #2 structural-unambiguity-at-N=2

## Pattern #78 current status (per `_patterns/03-active-candidates.md` v64 registration)

> **Definition:** Agents codify external-authority quality-criteria with explicit deprecation-aware schemas + dated standards-version tracking — distinct from coding-methodology codification (Pattern #21 SDD). Distinct from Pattern #28 progressive disclosure (LOAD vs TRACK). The agent INTERNALIZES the external standards' versioning system rather than reasoning from a frozen snapshot.
>
> **Criteria:**
> 1. Explicit external-authority citation with date (e.g., "September 2025 Quality Rater Guidelines")
> 2. Deprecation-tracking discipline (e.g., "HowTo: Deprecated (Sept 2023)" with deprecation date)
> 3. Versioned absorption of external-standards updates (release notes track when external standard moved, agent absorbed the change)
>
> **Required for promotion:** 2+ subjects satisfying all 3 criteria.
> **Re-evaluation:** v67 stale-check / v72 retire-check.

## N=2 evidence at v65

### Subject 1: claude-seo v64 (78a multi-vendor industry domain standards)

**3-criteria evaluation:**

| Criterion | Evidence |
|---|---|
| (1) Explicit external-authority citation with date | "Updated to September 2025 Quality Rater Guidelines" / "INP replaced FID on March 12, 2024" / "Schema.org v29.4 additions" / "December 2025 core update" / "Anthropic Claude Code skill specification (February 2026)" |
| (2) Deprecation-tracking discipline | **8 deprecation events with specific dates**: HowTo Sept 2023 / FAQ Aug 2023 / SpecialAnnouncement July 2025 / FID Sept 9 2024 (removed from Chrome tools) / FID-replaced-by-INP March 12 2024 / YMYL-only E-E-A-T scope expanded December 2025 / ClaimReview deprecated / VehicleListing deprecated June 2025 |
| (3) Versioned absorption ledger | CHANGELOG v1.0 → v1.9.9 (~11 versions over ~95 days) with per-release external-standards absorption + 5-version-source atomic-bump CI discipline + 13 manifest-consistency assertions |

**Sub-mechanism characterization: 78a multi-vendor-industry-domain-standards** — tracks Google Quality Rater Guidelines + Schema.org + Core Web Vitals + ISO 639/3166 codes + Anthropic Claude Code skill spec (5 distinct authoritative sources, industry-level domain).

**Wiki document:** `03 Projects/claude-seo - Beginner Analysis/02 Wiki/entity-3-domain-vertical-and-living-standards.md`

### Subject 2: claude-code-system-prompts v65 (78b single-vendor product-internals archive)

**3-criteria evaluation:**

| Criterion | Evidence |
|---|---|
| (1) Explicit external-authority citation with date | "Claude Code v2.1.140 (May 12th, 2026)" — README opening line; per-version commit-hash-anchored CHANGELOG entries (e.g., `# [2.1.140](https://github.com/Piebald-AI/claude-code-system-prompts/commit/0082871)`); README also tracks "Updated within minutes of each Claude Code release" |
| (2) Deprecation-tracking discipline | `**REMOVED:**` markers per CHANGELOG version entry (e.g., v2.1.129: "Agent Prompt: Verification specialist — Removed the adversarial verification subagent prompt"); `**NEW:**` markers for additions; HTML comment at CHANGELOG top: *"Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts"* |
| (3) Versioned absorption ledger | **211 KB CHANGELOG / 1,896 lines / 176 versions** (127 full + 49 no-change placeholder) since v2.0.14; per-version commit-hash + token-delta (`_+N tokens_`) + per-prompt change-description |

**Sub-mechanism characterization: 78b single-vendor-product-internals-archive** — tracks Anthropic Claude Code system prompts (single authority + single product) with **maximum-granularity** (per-patch version + per-prompt-fragment change-description + per-version commit-hash provenance).

**Wiki document:** `03 Projects/claude-code-system-prompts - Beginner Analysis/02 Wiki/entity-2-pattern-78-n2-strengthening.md`

### Cross-archetype structural diversity at N=2

| Aspect | 78a (claude-seo v64) | 78b (claude-code-system-prompts v65) |
|---|---|---|
| **Authority type** | Multi-vendor INDUSTRY standards | Single-vendor PRODUCT internals |
| **Authority cardinality** | 4+ distinct sources (Google + W3C + Schema.org + ISO) | 1 source (Anthropic Claude Code) |
| **Tracking granularity** | Quarter/year-level deprecation dates | Per-patch-version + per-prompt-fragment |
| **Version cadence** | ~11 versions over ~95 days | **176 versions over ~176 days (16× faster)** |
| **Absorption mechanism** | Each release notes external-standards absorption | Per-version commit-hash + token-delta + per-prompt change description |
| **Reverse-engineering required** | NO (Google publishes guidelines openly) | **YES** (Anthropic ships compiled binary; extraction needed) |
| **Vendor relationship** | Tracker is third-party but unaffected by vendor | Tracker is third-party + tolerated by vendor |
| **Author archetype** | Solo-individual (AgriciDaniel — AI Workflow Architect) | Corporate-org (Piebald-AI commercial company) |
| **CHANGELOG size** | ~35 KB / 607 lines | **211 KB / 1,896 lines (6× larger)** |
| **Granularity per change** | Bullet-point natural language | Token-delta quantified + commit-hash provenance + per-prompt description |

**Structural diversity at N=2**: 2 fundamentally distinct sub-mechanisms — multi-vendor industry vs single-vendor product. The mechanisms are **NOT coincidental variations**; they represent the 2 categories an agent might track (industry-domain standards vs single-vendor-product internals). Exhaustive 2-axis taxonomy.

## Promotion criteria evaluation

Per `_patterns/02-promotion-criteria.md` (referenced):

### Criterion #1: At-least-N=2 with non-coincidental sub-mechanism

**SATISFIED**. 2 distinct sub-mechanisms (78a + 78b) with explicit structural differences across 10 axes (table above). Non-coincidental: represents the 2 fundamentally distinct categories an agent might track.

### Criterion #2: Structural-unambiguity-at-N=2

**SATISFIED**. The 3 criteria are testable against future subjects:
- A subject claiming to track external standards but lacking explicit dates → FAILS criterion 1
- A subject acknowledging external authority but not tracking deprecation → FAILS criterion 2
- A subject claiming to track but without versioned absorption ledger → FAILS criterion 3
- A vendor documenting their OWN product (not third-party) → does NOT qualify; pattern is about third-party absorption-and-tracking, not authoring

### Criterion #3: Cross-archetype evidence

**SATISFIED** with 2 maximally-distinct archetypes:
- **claude-seo v64**: solo-individual + AI Workflow Architect + 5-product SEO-vertical ecosystem (Pattern #19 19c sub-mechanism)
- **claude-code-system-prompts v65**: corporate-org + commercial-agentic-IDE company + reverse-engineering-reference-archive (Pattern #19 19d NEW sub-mechanism at v65)

Solo-individual + corporate-org = maximally distinct archetype-pair.

### Criterion #4: Mechanism specificity

**SATISFIED**. 3-criteria definition is precise; can be mechanically applied to future subjects. Sub-mechanism distinction (78a/78b) also specifiable via authority-cardinality + tracking-granularity test.

### Criterion #5: Discrimination from existing patterns

**SATISFIED**:
- Distinct from **Pattern #21 SDD Methodology Emergence** (coding-methodology codification — SDD/TDD frameworks; Pattern #78 is about external-authority tracking, not coding-methodology)
- Distinct from **Pattern #28 Progressive Disclosure** (LOAD vs TRACK — #28 is about how to load context progressively; #78 is about how to track external authority versioning)
- Distinct from **Pattern #18 Multi-Platform** (host-platform diversity; #78 is external-authority diversity)
- Distinct from **NEW Pattern #79 Continuous-Reverse-Engineering Reference Archive (proposed v65)** (different claim about extraction-from-compiled-source; #78 is about tracking-discipline regardless of source-availability)

## 1-wiki un-stale-via-N=2-evidence cycle — meta-observation

This is the **SECOND observed 1-wiki rapid-pattern-evolution cycle in corpus history** (TIED FASTEST):

| Cycle | Registration date | Counter-evidence/un-stale date | Gap |
|---|---|---|---|
| **Pattern #76 counter-evidence** (v63 mini-audit → v62 codex-plugin-cc) | 2026-05-07 (Pattern #76 registered v63 mini-audit) | 2026-05-08 (codex-plugin-cc v62 wiki ship, counter-evidence) | **1 wiki / 1 day** |
| **Pattern #78 un-stale-via-N=2** (v64 claude-seo → v65 claude-code-system-prompts) | 2026-05-13 (Pattern #78 registered v64 wiki ship) | 2026-05-13/14 (claude-code-system-prompts v65 wiki ship, N=2 evidence) | **1 wiki / 0-1 day — TIED FASTEST** |

**Pattern Library meta-observation candidate**: "1-wiki rapid-pattern-evolution observational track" — when patterns register and immediately receive corpus evidence to evolve. Observational at v65; consider for v66 audit deliberation.

**Routine v2.2 codification candidate (NEW v65)**: "1-wiki rapid-evolution detection discipline" — when N+1 wiki provides evidence to evolve N wiki's pattern registration, log meta-observation as Library-vocabulary candidate AND consider promotion-acceleration.

## Recommended verdict

### Primary recommendation: PROMOTE Pattern #78 at v66 audit (accelerated) OR v67 stale-check (default)

**Promote Pattern #78 Living-Domain-Standards Tracking from candidate to CONFIRMED with 2 sub-mechanisms registered:**

- **78a multi-vendor-industry-domain-standards** (claude-seo v64 baseline)
- **78b single-vendor-product-internals-archive** (claude-code-system-prompts v65)

Justification:
- **N=2 with maximal structural diversity** (10-axis distinction) = exceeds criterion #2 threshold
- **2 maximally-distinct archetypes** = strong criterion #3 evidence
- **Mechanism specifiable** = criterion #4 satisfied with test cases
- **Discriminates from existing patterns** = criterion #5 satisfied
- **Promotion acceleration justified by FASTEST corpus-history un-stale cycle** (1-wiki turnaround tied with Pattern #76 counter-evidence cycle)

### Acceleration consideration: v66 vs v67

**Default per v64 registration**: re-evaluate v67 stale-check (+3 wikis from v64).

**Acceleration to v66 mini-audit possible** because:
- N=2 evidence available 1 wiki post-registration (FASTEST cycle)
- Pattern #78 already on v66 mini-audit pre-registration agenda (per v64 ship)
- Cross-archetype evidence already strong (solo + corporate)
- 10-axis structural diversity confirmed at N=2

**Operator decision at v66 audit**: accelerate Pattern #78 promotion to v66, OR await v67 stale-check window per standard discipline. Either path is defensible.

**Recommendation**: ACCELERATE to v66 — the evidence is strong, and Pattern #78 is already on v66 agenda; deferring to v67 adds 2-wiki delay without benefit.

### Sub-taxonomy decision

Register **both 78a + 78b as sub-mechanisms within confirmed Pattern #78** at promotion. The 2 sub-mechanisms are structurally distinct enough to warrant separate registration. Future N=3+ evidence may add 78c (e.g., Linux kernel changelog mirror archive) or consolidate to fewer sub-mechanisms; that's a future operator decision.

## v66 audit checklist for Pattern #78 (if PROMOTE)

- [ ] In `_patterns/04-confirmed-patterns.md`, ADD Pattern #78 CONFIRMED entry:
  - Definition (from v64 registration + v65 refinements)
  - 2 sub-mechanisms (78a + 78b) with subject + author + sub-mechanism characterization
  - Criterion #2 + #3 + #4 + #5 satisfaction summary
- [ ] In `_patterns/03-active-candidates.md`, REMOVE Pattern #78 candidate entry
- [ ] In `_patterns/05-recent-additions.md`, log the v66 promotion (or v67 if deferred) with audit timestamp
- [ ] Update PATTERN_LIBRARY.md state-block: confirmed count 42 → 43; active count 21 → 20; ratio 0.500:1 → 0.465:1
- [ ] Pre-register v69 audit item: "Pattern #78 sub-mechanism N=3+ expansion deliberation (78c+ candidates)"
- [ ] Log 1-wiki un-stale cycle as Library-vocabulary item #10 candidate (sister to v60 cross-pattern coupled-design item #9)

If operator DEFERS to v67:

- [ ] Keep N=2 evidence in `_patterns/03-active-candidates.md`
- [ ] Note in v66 audit document why deferral
- [ ] Re-register at v67 stale-check window

## Evidence document cross-references

This proposal's primary evidence:
- **v64 claude-seo Entity 3**: `03 Projects/claude-seo - Beginner Analysis/02 Wiki/entity-3-domain-vertical-and-living-standards.md`
- **v64 claude-seo Cluster 3**: `03 Projects/claude-seo - Beginner Analysis/02 Wiki/cluster-3-ecosystem-and-changelog.md`
- **v65 claude-code-system-prompts Entity 2** (this wiki's primary deliverable): `03 Projects/claude-code-system-prompts - Beginner Analysis/02 Wiki/entity-2-pattern-78-n2-strengthening.md`
- **v65 claude-code-system-prompts Cluster 3**: `03 Projects/claude-code-system-prompts - Beginner Analysis/02 Wiki/cluster-3-changelog-and-ecosystem.md`
- **v65 claude-code-system-prompts Cluster 2** (extraction methodology context): `03 Projects/claude-code-system-prompts - Beginner Analysis/02 Wiki/cluster-2-extraction-methodology.md`

## Conclusion

Pattern #78 Living-Domain-Standards Tracking has achieved **N=2 cross-archetype strengthening within 1 wiki of original registration** — the FASTEST un-stale cycle in 64-wiki corpus history (TIED with Pattern #76 1-wiki counter-evidence cycle v63→v62).

**Recommended verdict**: ACCELERATE PROMOTION to v66 mini-audit (vs default v67 stale-check) under criterion #2 structural-unambiguity-at-N=2 with 2 sub-mechanisms registered:
- **78a multi-vendor-industry-domain-standards** (claude-seo v64)
- **78b single-vendor-product-internals-archive** (claude-code-system-prompts v65)

This is the **STRONGEST single Pattern Library contribution emerging from v65 claude-code-system-prompts wiki ship.**

---

> *Prepared by Claude during v65 wiki build (2026-05-13 → 2026-05-14). For v66/v67 audit deliberation. Storm Bear vault, llm-wiki-routine-v2.1.*
