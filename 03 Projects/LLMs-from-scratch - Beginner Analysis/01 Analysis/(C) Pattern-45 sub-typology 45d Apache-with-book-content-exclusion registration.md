# Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" — Registration Proposal-Document

> **Phase 4b PRIMARY** for v74 wiki build (rasbt/LLMs-from-scratch).
> **SECOND formal sub-typology proposal-document in corpus history** (after v69's 45c).
> Proposed for registration at v74 wiki ship; v75 first-cycle stale-check + v80 retire-check; formal sub-variant promotion at N=2 emergence.

## Subject + verbatim license clause

**Subject:** `rasbt/LLMs-from-scratch` (v74) — Sebastian Raschka's official code repository companion to Manning's *Build a Large Language Model (From Scratch)* (2024).

**LICENSE.txt lines 26-30 (verbatim):**

> *""Source" form shall mean the preferred form for making modifications, **explicitly excluding any books specific to this software and any related images**, and includes but is not limited to software source code, documentation source (**excluding books and images related to this software**), and configuration files."*

**Standard Apache-2.0 "Source form" definition for comparison:**

> *""Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files."*

**Modification mechanism:** Apache-2.0 license **adds explicit exclusion clauses** for books + related images + book-documentation-source, while preserving the rest of Apache-2.0 verbatim. This is **INTRA-Apache modification** — single license file with carve-out clauses within the license definition itself.

## Pattern #45 history recap

Pattern #45 Dual-Licensing was:
- **REGISTERED** at v23 Unsloth (N=1 stale-flagged)
- **PROMOTED to CONFIRMED** at v60 EXTENDED MINI-AUDIT under criterion 2 structural-N=2 (Unsloth v23 Apache+commercial + AutoGPT v59 MIT+PolyForm-Shield)
- **EXTENDED** at v69 audit with sub-typology 45c "Artifact-Scope-Split with Acceptable-Use-Enumeration" registration (FIRST formal sub-typology proposal-document in corpus history; CloakBrowser v69)

**Existing Pattern #45 sub-typology taxonomy:**
- **45a "Apache + commercial-shield"** — Unsloth v23 — tier-based dual-license
- **45b "MIT + PolyForm-Shield"** — AutoGPT v59 — single-license-with-non-OSI-wrapper
- **45c "MIT-wrapper + Proprietary-Binary with Acceptable-Use"** — CloakBrowser v69 — dual-file artifact-scope split with Acceptable Use enumeration

**v74 proposes:**
- **45d "Apache-modified intra-license carve-out"** — LLMs-from-scratch v74 — single-file Apache-2.0 with "Source form" modified to exclude books + related images + book-documentation-source

## Sub-typology 45d structural distinction

### Comparison table — all four 45 sub-typologies

| Property | 45a Unsloth | 45b AutoGPT | 45c CloakBrowser | **45d LLMs-from-scratch (NEW v74)** |
|----------|-------------|-------------|-------------------|--------------------------------------|
| **License file count** | Multi (Apache + commercial-license) | Single (MIT wrapped by PolyForm-Shield) | Dual (LICENSE MIT + BINARY-LICENSE.md proprietary) | **Single (Apache-2.0 modified)** |
| **Modification mechanism** | Tier-based dual-license | Wrapping non-OSI license | Artifact-scope split | **Intra-license carve-out clause** |
| **Carve-out target** | Commercial-tier (paid features) | Non-commercial use restrictions | Binary artifact (compiled output) | **Books + images + book-documentation-source** |
| **OSS coverage** | Free-tier covered by Apache | Codebase MIT but use PolyForm-restricted | Wrapper code MIT covered | **Code Apache-2.0 covered; books NOT covered** |
| **Revenue mechanism** | Commercial-tier licensing | Limited commercial use | OEM/SaaS B2B carve-out + Acceptable Use enumeration | **Book sales (Manning publication revenue)** |
| **Print-publishing relevance** | N/A (tool repo) | N/A (tool repo) | N/A (browser repo) | **Critical (book-companion-repo archetype)** |
| **Distinguishing axis** | Commercial-tier-restriction | Non-commercial-use-restriction | Compiled-artifact-restriction | **Print-content-restriction** |

### 6 distinguishing mechanisms of 45d

1. **Single license file modification** (not dual-file split like 45c; not wrapper like 45b)
2. **Content-type-based carve-out** (books + images), not artifact-scope (binary vs wrapper) or commercial-tier (free vs paid)
3. **Apache-2.0 BASE preserved verbatim** — modification is ONLY at "Source form" definition (one paragraph); everything else is standard Apache-2.0
4. **Print-publishing copyright preservation** — specific to book-companion-repo archetype (carves out Manning-copyrighted content from Apache coverage)
5. **CITATION.cff declares "Apache-2.0"** but actual LICENSE.txt is modified — surface declaration vs structural reality mismatch (GitHub auto-classifier returns "NOASSERTION" which is structurally more accurate)
6. **No commercial-licensing alternative** — no commercial-tier mention; the carve-out is for copyright preservation not commercial gating

## Promotion criteria evaluation

Per v69 audit precedent (criterion-set for sub-typology registration):

| Criterion | Evaluation | Confidence |
|-----------|------------|-----------|
| 1 — corpus-first structural property | PASS — intra-Apache book-content-carve-out is corpus-first | HIGH |
| 2 — mechanism-distinct from prior sub-typologies | PASS — 45a/b/c are tier-based / wrapper-based / artifact-scope-based; 45d is content-type-carve-out-within-single-license | HIGH |
| 3 — clear definition + falsification tests | PASS — definable as "Apache-2.0 with Source form modified to exclude specific content-types"; falsified if subject uses unmodified Apache-2.0 or dual-file license or has no book/print-publishing context | HIGH |
| 4 — N=1 stale-flag with future re-evaluation | PASS — corpus-typical N=1 stale-tracking discipline | DEFAULT |
| 5 — promotion criteria sustainable at v75+ formal sub-variant promotion | PASS — N=2 emergence likely if `rasbt/machine-learning-book` (Packt 2022 companion) or future book-companion subjects use same Apache-modified pattern | DEFAULT |

**Verdict: HIGH confidence sub-typology registration. REGISTER 45d as sub-typology within Pattern #45. v75 stale-check + v80 retire-check. Formal sub-variant promotion at N=2 emergence.**

## Falsification tests pre-registered

| Evidence | Effect on 45d |
|----------|---------------|
| Another book-companion repo adopts Apache-modified intra-license carve-out | **STRENGTHENS** 45d — sub-variant promotion at N=2 |
| A subject adopts Apache-modified carve-out for non-book content (e.g., images-only or audio-only carve-out) | **REFINES** 45d taxonomy — generalize to "Apache-modified content-type-carve-out" |
| A subject adopts MIT-modified or BSD-modified content-type-carve-out | **EXTENDS** 45d to multi-license-base sub-typology |
| Sebastian Raschka's `rasbt/machine-learning-book` (Packt 2022 companion) is found to use same Apache-modified pattern | **CONFIRMS** 45d as Raschka-portfolio discipline (sister 19e evidence) and provides retroactive N=2 |
| Sebastian Raschka's `rasbt/reasoning-from-scratch` (sequel Manning book) is wiki'd in future and uses same Apache-modified pattern | **CONFIRMS** 45d as Manning-publication-companion discipline + retroactive N=2 |
| A non-Raschka book-companion repo (e.g., Packt/Manning/O'Reilly companion from different author) adopts Apache-modified carve-out | **CROSS-VALIDATES** 45d as broader pattern beyond single-author discipline; cross-author N=2 = stronger promotion case |
| No additional 45d evidence in next 5 wikis (v75-v79) | **WEAKENS** 45d — preserve N=1 stale-flagged through v80 retire-check |
| Discovered: prior corpus subject (re-audited) already exemplifies 45d | **CORRECTS** — retroactive N=2 strengthens accordingly |
| The book-content-carve-out in LLMs-from-scratch is found to be Manning-publisher-standard-clause used in all Manning book repos | **REFRAMES** 45d as "publisher-standard-Apache-modification" rather than author-specific discipline |

## Cross-pattern coupled-design analysis

v74 exhibits 4-pattern coupled-design:

1. **NEW Pattern #45 sub-typology 45d (THIS proposal)** — Apache-modified license
2. **NEW T3 sub-archetype "Educational-Book-Companion"** — book-as-primary-artifact
3. **NEW Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio"** — Raschka multi-book portfolio
4. **NEW Pattern #52 sub-class "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)"** — multi-year sustained velocity

**Tight coupling around single archetype constraint (educational-book-companion):**
- License (45d) shaped by need to preserve print-content copyright
- Tier (T3 Educational-Book-Companion) shaped by book-as-primary-artifact
- Portfolio (19e) shaped by multi-book Manning + Packt cross-publisher discipline
- Velocity (Pattern #52 sub-class) shaped by multi-year book-companion sustenance

**Library-vocabulary item #9 Cross-Pattern Coupled-Design strengthening:** v74 is 4-pattern correlation at single wiki — sister to v60 (4-pattern), v65 (5+-pattern corpus-record), v73 (multiple sub-mechanism candidates).

**Distinguishing v74 coupling vs prior coupling:** All 4 patterns in v74 are CONSTRAINT-DERIVED — they flow from the educational-book-companion archetype constraint rather than from independent dimensions. This is a **NEW cross-pattern coupling sub-mechanism candidate** — "archetype-derived-pattern-cluster" where one archetype constraint shapes multiple patterns simultaneously.

## Sister-observation: CITATION.cff vs LICENSE.txt declaration mismatch

**CITATION.cff (verbatim):**
```yaml
license: "Apache-2.0"
```

**LICENSE.txt (Apache-2.0 with modified "Source form"):**
- Apache-2.0 base preserved
- "Source form" definition modified to exclude books + images + book-documentation-source

**Structural mismatch:**
- CITATION.cff declares standard Apache-2.0 SPDX identifier
- LICENSE.txt is Apache-2.0 WITH MODIFICATIONS (effectively NOASSERTION per GitHub auto-classifier)
- License-text PREVAILS legally (LICENSE.txt is authoritative)
- CITATION.cff is for academic/scientific citation purposes (no legal binding)

**Observational note:** Not a defect — the modification is small enough that calling it Apache-2.0 in citation context is reasonable shorthand. But it's corpus-rare structural mismatch worth tracking.

**Sister to Pattern #83 Honest-Deficiency-Disclosure (PROMOTED v69 audit):**
- 83a security-disclosure
- 83b methodology-disclosure
- 83c legal-operational-disclosure
- 83d experimental-status-disclosure
- 83e license-axis-as-disclosure-surface
- **83f candidate "license-declaration-vs-actual-mismatch"** ← NEW sub-mechanism if N=2 emerges (v74 LLMs-from-scratch + future subject)

Defer 83f sub-mechanism decision to v75+ audit.

## Sister-observation: book-companion-repo as corpus-novel archetype

45d as a sub-typology is **inseparable from the book-companion-repo archetype**. The license modification mechanism (carving out books + images) only makes sense in the book-companion context. This suggests:

**Hypothesis:** 45d is **archetype-locked sub-typology** — it can ONLY emerge within Educational-Book-Companion T3 sub-archetype + Pattern #19 sub-mechanism 19e + Pattern #52 sub-class.

**Falsification test:** If 45d emerges in non-book-companion context (e.g., game-companion or course-material-companion), the archetype-lock hypothesis is FALSIFIED and 45d becomes broader content-type-carve-out sub-typology.

**Forward observation candidate:** Track whether 45d expands to other content-type-carve-out subjects beyond books.

## v75 audit-batch placement recommendation

v75 audit (next natural-cadence) should evaluate:

1. **45d first-cycle stale-check** (v74 + 1 wiki = v75 minimum threshold)
2. **45d N=2 promotion-eligibility test** — look for second book-companion or Apache-modified subject
3. **Retroactive N=2 check against `rasbt/machine-learning-book`** (Packt 2022 companion) — if it uses same Apache-modified pattern, retroactive N=2 establishment is valid (sister to v62 audit gap retroactive Pattern #52 establishment)
4. **45d vs other 45 sub-typology cross-pattern interaction analysis** — confirm mechanism-distinction holds
5. **Pattern #83 sub-mechanism 83f candidate "license-declaration-vs-actual-mismatch"** — N=2 emergence check
6. **Archetype-derived-pattern-cluster cross-pattern coupling sub-mechanism candidate** — Library-vocabulary item #9 N+1 strengthening

## Routine v2.x lessons

**For routine v2.3 codification queue (post-v74):**

1. **Intra-license carve-out as recognized Pattern #45 sub-typology** — alongside 45a tier-based + 45b wrapper-based + 45c dual-file-artifact-scope-split
2. **License-declaration-vs-actual mismatch tracking (potential 83f sub-mechanism)** — Phase 0 sub-procedure to check CITATION.cff (or equivalent license-declaring artifact) against LICENSE.txt for consistency
3. **Print-publishing-constraint detection** — Phase 0 sub-procedure to identify when subject is shaped by print-publishing constraints (book-companion archetype detection)
4. **Archetype-derived-pattern-cluster framing** — Library-vocabulary item #9 sub-mechanism for when multiple patterns flow from single archetype constraint
5. **Affiliate-link homepage detection (OC-R sister)** — Phase 0 sub-procedure to flag GitHub `homepage` field = affiliate redirect

## What this entity does NOT propose

To maintain "NEVER fabricate" discipline:

- **NOT a top-level Pattern #45 re-promotion** — Pattern #45 already CONFIRMED at v60 audit
- **NOT a claim that 45d is "best" licensing approach** — observational distinction only
- **NOT a legal opinion on Apache-2.0 modification validity** — that's beyond corpus scope; documented as observation
- **NOT a prediction that book-companion-repos universally adopt 45d** — N=1 PROVISIONAL; future evidence will refine
- **NOT a recommendation that Storm Bear vault adopt 45d** — Storm Bear is not a print-publisher
- **NOT a CITATION.cff vs LICENSE.txt criticism** — the declaration vs actual mismatch is observational only, not pejorative

## Phase 4b PRIMARY conclusion

**Recommendation:** Register Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" at N=1 PROVISIONAL with HIGH confidence verdict.

**Confidence verdict:** HIGH — corpus-first intra-Apache modification mechanism; 6 distinguishing properties; mechanism-distinct from prior 45a/b/c sub-typologies; falsification tests pre-registered; cross-pattern coupled-design observation strengthens at v74.

**Status pending audit:** Sub-typology 45d REGISTERED at N=1 PROVISIONAL; v75+ promotion to formal sub-variant at N=2 emergence (likely candidates: `rasbt/machine-learning-book` retroactive check + future book-companion subjects).

**Phase 4b vehicle:** SECOND formal sub-typology proposal-document in corpus history (after v69's 45c registration). Validates v69 audit's establishment of sub-typology proposal-document as 5th Phase 4b vehicle.

**Sister observations registered concurrently:**
- NEW T3 sub-archetype "Educational-Book-Companion" (within-T3-archetype expansion)
- NEW Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio" candidate
- NEW Pattern #52 sub-class "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)" candidate
- OC-R "Affiliate-Link-As-Repository-Homepage" (N=1)
- OC-S "Methodology-Influence-Node-Without-Operational-Tool" (N=2 with v63 Karpathy sister — EARLY-promotion-eligible at v75+ audit)
- OC-T "Print-Book-Constraint-As-Architecture" (N=1)
- Sister Pattern #83 sub-mechanism 83f candidate "license-declaration-vs-actual-mismatch"
