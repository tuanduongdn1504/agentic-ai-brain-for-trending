# Entity 3 — Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" (Phase 4b PRIMARY)

> **Phase 4b PRIMARY:** v74 contributes NEW Pattern #45 sub-typology 45d candidate. SECOND formal sub-typology proposal-document in corpus history (after v69's 45c). Full proposal-document at `01 Analysis/(C) Pattern-45 sub-typology 45d Apache-with-book-content-exclusion registration.md`.

## Why this entity exists

Pattern #45 Dual-Licensing was PROMOTED to CONFIRMED at v60 audit + EXTENDED with sub-typologies at v69 audit (45c absorbed into Pattern #45 confirmed entry). v74 contributes **NEW sub-typology 45d candidate** — a corpus-novel licensing mechanism where Apache-2.0 itself is modified (rather than the license being one of two files or wrapping/wrapped).

## Verbatim Apache-2.0 modification clause (LICENSE.txt lines 26-30)

> *""Source" form shall mean the preferred form for making modifications, **explicitly excluding any books specific to this software and any related images**, and includes but is not limited to software source code, documentation source (**excluding books and images related to this software**), and configuration files."*

**Standard Apache-2.0 "Source form" definition for comparison:**
> *""Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files."*

**Modification:** LLMs-from-scratch LICENSE.txt **adds explicit exclusion clauses** for books + related images + book-documentation-source, while preserving the rest of Apache-2.0 verbatim. This is **intra-Apache modification** — a single license file with carve-out within the license definition itself.

## Sub-typology 45d structural distinction

### Comparison to prior Pattern #45 sub-typologies

| Sub-typology | License-shape | Subjects | Distinguishing axis |
|--------------|---------------|----------|---------------------|
| **45a "Apache + commercial-shield"** | Tier-based dual | Unsloth v23 | Free-tier Apache + commercial-tier non-Apache (commercial shield via tier) |
| **45b "MIT + PolyForm-Shield"** | Single-license-with-wrapper | AutoGPT v59 | PolyForm-Noncommercial wraps MIT codebase |
| **45c "MIT-wrapper + Proprietary-Binary with Acceptable-Use"** | Dual-file artifact-scope split | CloakBrowser v69 | LICENSE MIT for wrapper + BINARY-LICENSE.md proprietary for binary |
| **45d "Apache-modified intra-license carve-out"** | Single-file Apache-modified | **LLMs-from-scratch v74** | Apache-2.0 "Source form" definition modified to exclude books + images |

### 6 distinguishing mechanisms of 45d

1. **Single license file** (not dual-file split like 45c)
2. **Carve-out by content-type** (books + images), not by artifact-scope (binary vs wrapper) or commercial-tier (free vs paid)
3. **Apache-2.0 BASE preserved** — modification is ONLY at "Source form" definition (one paragraph); everything else verbatim Apache-2.0
4. **Print-publishing copyright preservation** — specific to book-companion-repo archetype (carves out Manning-copyrighted content from Apache coverage)
5. **CITATION.cff declares "Apache-2.0"** but actual LICENSE.txt is modified — surface declaration vs structural reality mismatch (NOASSERTION at GitHub auto-classifier is more accurate)
6. **No commercial-licensing alternative** — no commercial-tier mention; the carve-out is for copyright preservation not commercial gating

### Verification against prior sub-typology promotion criteria

Per v69 audit precedent (criterion-set for sub-typology registration):

- ✅ **Criterion 1 — corpus-first structural property:** PASS — intra-Apache modification for book-content-carve-out is corpus-first
- ✅ **Criterion 2 — mechanism-distinct from prior sub-typologies:** PASS — 45a/b/c are tier-based / wrapper-based / artifact-scope-based; 45d is content-type-carve-out-within-single-license
- ✅ **Criterion 3 — clear definition + falsification tests:** PASS — definable as "Apache-2.0 with Source form modified to exclude specific content-types"; falsified if subject uses unmodified Apache-2.0 or dual-file license

**Verdict: HIGH confidence sub-typology registration.**

## Proposal-document content

### 1. Promotion criteria evaluation

| Criterion | Evaluation | Confidence |
|-----------|------------|-----------|
| Sub-typology corpus-first structural property | PASS — intra-Apache book-content-carve-out is novel mechanism | HIGH |
| Mechanism-distinct from 45a/b/c | PASS — content-type-carve-out within single license file | HIGH |
| Clear definition + falsification tests | PASS — definable + testable | HIGH |
| N=1 stale-flag with v75 re-evaluation | PASS — corpus-typical stale-tracking | DEFAULT |

**Verdict: REGISTER 45d as sub-typology within Pattern #45. v75 stale-check + v80 retire-check. Formal sub-variant promotion at N=2 emergence.**

### 2. Falsification tests pre-registered

| Evidence | Effect |
|---|---|
| Another book-companion repo adopts Apache-modified intra-license carve-out | **STRENGTHENS** 45d — sub-variant promotion at N=2 |
| A subject adopts Apache-modified carve-out for non-book content (e.g., images-only or audio-only carve-out) | **REFINES** 45d taxonomy — generalize to "Apache-modified content-type-carve-out" |
| A subject adopts MIT-modified or BSD-modified content-type-carve-out | **EXTENDS** 45d to multi-license-base sub-typology |
| Sebastian Raschka's `rasbt/machine-learning-book` (Packt 2022 companion) is found to use same Apache-modified pattern | **CONFIRMS** 45d as Raschka-portfolio discipline (sister 19e evidence) |
| No additional 45d evidence in next 5 wikis | **WEAKENS** 45d — preserve N=1 stale-flagged through v80 |
| Discovered: prior corpus subject (re-audited) already exemplifies 45d | **CORRECTS** — strengthens accordingly |

### 3. Sister-observation: CITATION.cff license declaration vs LICENSE.txt reality mismatch

**CITATION.cff declares:** `license: "Apache-2.0"` (standard SPDX identifier)

**LICENSE.txt is:** Apache-2.0 WITH MODIFIED "Source form" definition (effectively NOASSERTION per GitHub auto-classifier)

**This is a structural mismatch** worth flagging at v75+ audit:
- CITATION.cff is for academic/scientific citation purposes
- LICENSE.txt is the legally-binding license terms
- Declaring "Apache-2.0" in CITATION.cff while having modified Apache-2.0 in LICENSE.txt may create downstream confusion

**Observational note:** Not a defect (license-text-prevails over CITATION.cff declarations); but corpus-rare mismatch worth tracking. Sister to Pattern #83 Honest-Deficiency-Disclosure (v69 PROMOTED) — could be 83f sub-mechanism candidate "license-declaration-vs-actual-mismatch" if N=2 emerges.

### 4. Routine v2.x lessons

**For routine v2.3 codification queue:**

1. **Intra-license carve-out as recognized Pattern #45 sub-typology** — alongside 45a tier-based + 45b wrapper-based + 45c dual-file-artifact-scope-split
2. **License-declaration-vs-actual mismatch tracking** — Phase 0 sub-procedure to check CITATION.cff (or equivalent license-declaring artifact) against LICENSE.txt for consistency
3. **Print-publishing-constraint detection** — Phase 0 sub-procedure to identify when subject is shaped by print-publishing constraints (book-companion archetype detection)

## What this entity does NOT propose

To maintain "NEVER fabricate" discipline:

- **NOT a top-level Pattern #45 re-promotion** — Pattern #45 already CONFIRMED at v60 audit
- **NOT a claim that 45d is "best" licensing approach** — observational distinction only
- **NOT a legal opinion on Apache-2.0 modification validity** — that's beyond corpus scope; documented as observation
- **NOT a prediction that book-companion-repos universally adopt 45d** — N=1 PROVISIONAL; future evidence will refine

## v75 audit-batch placement recommendation

v75 audit (next natural-cadence) should evaluate:
- 45d first-cycle stale-check (v74 + 1 wiki = v75 minimum)
- 45d N=2 promotion-eligibility test (look for second book-companion or Apache-modified subject)
- Possibly: 45d N=2 retroactive check against `rasbt/machine-learning-book` (Packt 2022 companion) — if it uses same Apache-modified pattern, retroactive N=2 establishment is valid (sister to v62 audit gap retroactive Pattern #52 establishment)
- 45d vs other 45 sub-typology cross-pattern interaction analysis

## Phase 4b PRIMARY conclusion

**Recommendation:** Register Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" at N=1 PROVISIONAL with HIGH confidence verdict. v75 first-cycle stale-check + v80 retire-check.

**Confidence verdict:** HIGH — corpus-first intra-Apache modification mechanism; 6 distinguishing properties; mechanism-distinct from prior 45a/b/c sub-typologies; falsification tests pre-registered.

**Status pending audit:** Sub-typology 45d REGISTERED at N=1 PROVISIONAL; v75+ promotion to formal sub-variant at N=2 emergence (likely candidates: `rasbt/machine-learning-book` retroactive check + future book-companion subjects).

**Phase 4b vehicle:** SECOND formal sub-typology proposal-document in corpus history (after v69's 45c registration). Validates v69 audit's establishment of sub-typology proposal-document as 5th Phase 4b vehicle.

## Related cross-references

- **Pattern #45 confirmed entry (v60 audit):** `_patterns/02b-confirmed-patterns-v42-plus.md`
- **v69 45c first sub-typology proposal-document (precedent):** `03 Projects/CloakBrowser - Beginner Analysis/01 Analysis/(C) Pattern-45 sub-typology 45c wrapper-OSS + binary-proprietary-with-acceptable-use registration.md`
- **v69 OVERDUE-NATURAL-CADENCE audit (45c absorption):** `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE...).md`
- **v74 Subject + license verification:** `02 Wiki/cluster-1-readme-book-metadata-license.md`
