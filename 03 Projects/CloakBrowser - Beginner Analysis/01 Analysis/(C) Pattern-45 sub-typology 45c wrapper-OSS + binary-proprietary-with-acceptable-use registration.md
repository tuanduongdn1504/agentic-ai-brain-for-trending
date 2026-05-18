# (C) Pattern #45 sub-typology 45c registration proposal — "wrapper-OSS + binary-proprietary-with-acceptable-use-restrictions"

> Phase 4b PRIMARY proposal-document for v69 CloakBrowser wiki · routine v2.2 · audit-target v69 batch

## Executive summary

**Proposal:** Register Pattern #45 Dual-Licensing Discipline NEW sub-typology **45c — Artifact-Scope-Split with Acceptable-Use-Enumeration** based on CloakBrowser v69 evidence (N=1).

**Confidence:** **HIGH** — all 3 sub-typology promotion criteria PASS; mechanism-cluster internally coherent; structurally distinct from prior 45a/45b sub-variants; descriptive-power gain substantive.

**Status at registration:** OBSERVATIONAL at N=1; v70 stale-check + v75 retire-check; formal promotion to sub-variant at N=2 emergence (criterion 4 variant-within-pattern-at-N=2).

**Audit-decision flag:** Pattern #45 may be re-evaluated alongside Pattern #83 promotion at v69 audit batch (~24-25 items, LARGEST in corpus history).

---

## 1. Pattern #45 background

Pattern #45 Dual-Licensing Discipline was PROMOTED to Confirmed at **v60 EXTENDED MINI-AUDIT (2026-05-07)** under criterion 2 structural-N=2:
- **45a Unsloth v23** (2026-04-XX) — Apache-2.0 + commercial-shield clauses inline
- **45b AutoGPT v59** (2026-05-XX) — MIT + PolyForm-Shield-Restrictions overlay

The promotion narrative noted Pattern #45 captures *"a license shape that hybridizes OSS permission with commercial-protection clauses to enable both community adoption and commercial moat."*

Both 45a and 45b share structural form:
- **Single LICENSE file at repo root**
- **Hybrid OSS + commercial-protection clauses inline within the file**
- **Usage-tier-split scope** (same artifact, different terms by use case)

CloakBrowser v69 introduces a **structurally distinct mechanism cluster** that warrants a separate sub-typology classification.

---

## 2. CloakBrowser 45c evidence

### 2.1 Form (verbatim file structure)

```
CloakBrowser repo root:
├── LICENSE                    ← MIT (~22 lines, standard MIT terms)
├── BINARY-LICENSE.md          ← Proprietary + Acceptable Use (~155 lines, 17 clauses)
└── (other repo files)
```

**Distinguishing form #1:** Two separate license files at repo root, with license boundary following artifact-compilation scope.

### 2.2 Acceptable Use enumeration (verbatim, BINARY-LICENSE.md)

> *"Without limiting the above, the following uses are expressly prohibited:*
> *- Unauthorized access to financial, banking, healthcare, or government authentication systems*
> *- Credential stuffing, brute-force login attempts, or automated account creation*
> *- Circumventing authentication on systems you do not own or have authorization to test*
> *- Any activity that constitutes fraud, identity theft, or unauthorized data collection"*

**Distinguishing form #2:** Explicit enumeration of prohibited use cases (4 specific prohibitions) — not vague "for legitimate purposes only" framing.

### 2.3 Bounded liability cap (verbatim, BINARY-LICENSE.md)

> *"CLOAKHQ'S TOTAL AGGREGATE LIABILITY SHALL NOT EXCEED ONE HUNDRED US DOLLARS (US $100)."*

**Distinguishing form #3:** Fixed-dollar max-aggregate-liability cap (rather than unbounded "AS IS, NO LIABILITY" framing typical of OSS license shapes).

### 2.4 OEM/SaaS commercial-licensing carve-out (verbatim, BINARY-LICENSE.md)

> *"OEM/SaaS license required — Bundling, embedding, or pre-installing the Binary into a product, hosted service, or cloud artifact distributed to third parties requires a separate OEM license. This includes running the Binary on your infrastructure to serve third-party customers (e.g., browser-as-a-service). Contact cloakhq@pm.me for OEM/SaaS licensing."*

**Distinguishing form #4:** Explicit B2B commercial-licensing carve-out as primary revenue mechanism (vs ambiguous "commercial use" treatment in 45a/45b).

### 2.5 Additional distinguishing features (not promotion-criteria-essential but contextually significant)

- **Internal-use carve-out** — permits internal-infrastructure caching/baking (Artifactory, Nexus, Docker registries, VM templates) without redistribution gate
- **Indemnification clause** — user agrees to indemnify CloakHQ for legal exposure
- **Trademark Notice + Attribution opt-in** — softer trademark protection vs prior corpus shapes
- **ungoogled-chromium upstream attribution** — explicit 3-level transitive license attribution (BSD-3-Clause Chromium → ungoogled-chromium → CloakHQ patches)

---

## 3. Pattern #45 sub-variant taxonomy (proposed)

### 3.1 Existing sub-variants

#### 45a — OSS-with-commercial-shield clause (Unsloth v23)

- **Form:** Single LICENSE file (Apache-2.0)
- **Mechanism:** Apache-2.0 base + commercial-use clauses inline
- **Scope basis:** Usage-tier-split (same artifact, different terms by use case)
- **Revenue model:** Implicit (Apache-2.0 permits commercial integrators)

#### 45b — OSS-overlaid-with-PolyForm-Family-restriction (AutoGPT v59)

- **Form:** Single LICENSE file (MIT)
- **Mechanism:** MIT base + PolyForm-Shield-Restrictions overlay
- **Scope basis:** Usage-tier-split (anti-cannibalization framing)
- **Revenue model:** Direct (PolyForm-Family-License limits competing commercial offerings)

### 3.2 NEW sub-variant — 45c

#### 45c — Artifact-Scope-Split-with-Acceptable-Use-Enumeration (CloakBrowser v69)

- **Form:** TWO separate license files (LICENSE + BINARY-LICENSE.md)
- **Mechanism:** Different licenses per artifact (MIT wrapper / Proprietary binary)
- **Scope basis:** **Artifact-scope-split** (license boundary follows compilation artifact)
- **Revenue model:** B2B-explicit (OEM/SaaS commercial-licensing carve-out)
- **Defensive scaffolding:** Acceptable Use + bounded liability + indemnification + termination

---

## 4. Promotion criteria evaluation

### Criterion 1: Structurally distinct from prior sub-variants ✅ STRONG PASS

| Dimension | 45a | 45b | 45c |
|-----------|-----|-----|-----|
| License-file count | 1 | 1 | **2** |
| Scope basis | Usage-tier | Usage-tier | **Artifact-scope** |
| Mechanism-coupling | Apache-2.0 + commercial-shield (inline) | MIT + PolyForm-Shield (overlay) | **MIT (wrapper) + Proprietary (binary, separate file)** |
| Prohibited-use treatment | Generic disclaimer | Generic disclaimer | **Explicit enumeration (4 prohibitions)** |
| Liability framing | Standard "AS IS" | Standard "AS IS" | **Bounded $100 cap** |
| Revenue mechanism | Implicit (broad commercial) | Direct (PolyForm-protected) | **B2B-explicit (OEM/SaaS carve-out)** |

Six distinct structural dimensions distinguish 45c from 45a/45b. → STRONG PASS.

### Criterion 2: Mechanism cluster has internal coherence ✅ STRONG PASS

The 4 distinguishing mechanisms of 45c are not random — they form a coherent B2B-licensing-architecture:

```
USER-FACING LEGAL CLARITY                      CLOAKHQ-FACING RISK-REVENUE
──────────────────────────                     ─────────────────────────────
Artifact-scope split    ┐                  ┌─  Bounded liability cap
                        │                  │
Acceptable Use list     ┤  ←  coheres  →  ├─  Indemnification + Termination
                        │                  │
Trademark Notice        ┘                  └─  OEM/SaaS B2B carve-out
                                                ↓
                                            Primary revenue mechanism
```

The mechanism-cluster has internal coherence as a deliberate dual-use-product-licensing-architecture: protect-against-misuse (left side) + monetize-legitimate-commercial-embedding (right side). → STRONG PASS.

### Criterion 3: Adds Pattern Library descriptive power ✅ MODERATE-STRONG PASS

Without 45c, Pattern #45 cannot capture:

| Pattern feature 45c adds | Missing from 45a/45b |
|---|---|
| Artifact-scope-split licensing | Both 45a + 45b use usage-tier-split |
| Explicit prohibited-use enumeration | Neither 45a nor 45b enumerate prohibited uses |
| Bounded fixed-dollar liability cap | Both 45a + 45b use unbounded "AS IS" framing |
| B2B OEM/SaaS commercial-licensing carve-out as primary revenue | Both 45a + 45b have implicit/secondary revenue treatment |
| Internal-use carve-out (Artifactory/Nexus/VM/Docker) | Neither 45a nor 45b address internal-distribution scenarios |

These features are real license-axis mechanisms that occur in OSS-with-proprietary-binary projects — Pattern #45 should be able to capture them. → MODERATE-STRONG PASS.

→ **All 3 promotion criteria PASS; sub-typology 45c PROPOSED for registration.**

---

## 5. Pre-registered falsification tests

To maintain audit-layer fact-verification discipline (v60 audit precedent: 3 audit-layer fact-verification corrections in corpus history have falsified prior claims), pre-register what evidence would weaken or invalidate the 45c sub-typology classification:

| Evidence type | Effect on 45c | Action |
|---|---|---|
| Another corpus subject independently adopts 45c-shape (artifact-scope split + Acceptable Use enumeration + bounded liability + OEM carve-out) | **STRENGTHENS** | Promote to formal Pattern #45 sub-variant at N=2 (criterion 4 variant-within-pattern-at-N=2) |
| Another corpus subject adopts ONE 45c mechanism but not others (e.g., artifact-scope split without Acceptable Use) | **REFINES** | Split 45c into sub-sub-variants 45c1/45c2/etc. with the specific mechanism-coupling observed |
| No second 45c-shape subject appears in next 5 wikis (v70-v74) | **WEAKENS** | Sub-typology becomes N=1-stale-flagged; consider downgrading to OBSERVATION-TRACK |
| Discovered: prior corpus subject (re-audited) already exemplifies 45c-shape | **CORRECTS** | Pre-existing N≥2 in corpus history; 45c was discovered later but structurally existed earlier |
| CloakBrowser changes license to drop one of the 4 mechanisms (e.g., removes Acceptable Use enumeration) | **WEAKENS** | Mechanism instability suggests 45c was incidental not structural |
| Audit-layer fact-verification reveals one of the verbatim quotes is misattributed or paraphrased rather than direct | **CORRECTS** | Iteration log records correction; sub-typology stands if other evidence holds |

---

## 6. v69 audit-batch placement recommendation

The v69 audit batch is now **~24-25 items** (v68 carry-over ~20 + v69 new ~5), making it the LARGEST in corpus history. Recommended placement of Pattern #45 sub-typology 45c registration within batch:

| Audit item | Decision type | Recommended order |
|---|---|---|
| Pattern #83 PROMOTION (v64+v65+v67+v68+v69 N=5 evidence) | PROMOTION | 1st (highest-confidence; pre-eligible) |
| Pattern #84 REFINEMENT (84a/84b sub-mechanism decision) | REFINEMENT | 2nd (already-pending; v66 carry) |
| Pattern #45 sub-typology 45c registration | **SUB-TYPOLOGY REGISTRATION** | **3rd (NEW pattern-machinery work)** |
| Pattern #86 T1 sub-archetype #7 stale-check (v68 carry) | STALE-CHECK | 4th (early stale-check) |
| Pattern #87 Skill-As-Binary-Bootstrap stale-check (v68 carry) | STALE-CHECK | 5th |
| OC-A through OC-F (v68) stale-checks | STALE-CHECK batch | 6th-11th |
| OC-1 through OC-3 (v67) stale-checks | STALE-CHECK batch | 12th-14th |
| OC-G through OC-J (v69) registration | NEW OBSERVATIONAL | 15th-18th |
| Pattern #74-82 + #85 stale-checks (existing carry) | STALE-CHECK batch | 19th-24th |
| Tier-Taxonomy Review T6 (v68 carry; ELEVATED at v69) | DECISION | 25th (audit-end) |

Sub-typology 45c registration is **low-risk** (within already-promoted Pattern #45; no top-level promotion) but **adds descriptive power** to the Pattern Library.

---

## 7. Routine v2.2 lessons captured

**v2.3 codification queue items from v69:**

1. **"Sub-typology proposal-document discipline"** — when new evidence adds a substantively distinct sub-variant within an already-promoted pattern, a formal sub-typology proposal-document is the appropriate vehicle (vs full new-pattern registration OR simple within-pattern strengthening note). This is the v69 exemplar.

2. **"Dual-use subject framing as Phase 0 sub-procedure"** — when a corpus subject has dual-use exposure (legitimate vs prohibited uses both plausible), routine v2.x should codify an explicit Phase 0 framing decision before Phase 2 ingestion. The framing decision affects: (a) Phase 4a beginner-guide tone, (b) Phase 5 iteration-log disclosure, (c) overall wiki posture (knowledge-base vs operational-manual). v69 made this decision implicitly at Phase 0; v2.3 should codify.

3. **"Audit batch >20-items splitting consideration"** — v68 + v69 both produce audit batches at LARGEST-in-corpus-history size. Routine v2.x should evaluate whether single-batch audits should split into sub-audits (license-axis / detection-evasion / fork-strategy / etc.) when batch size exceeds ~15-20 items.

---

## 8. Conclusion

**Recommendation:** REGISTER Pattern #45 sub-typology 45c at v69 iteration log + `_patterns/03-active-candidates.md`. Defer formal sub-variant promotion to v70+ audit upon N=2 emergence.

**Confidence verdict:** HIGH — all 3 sub-typology promotion criteria PASS with internally-coherent mechanism cluster + 4 distinguishing structural dimensions + substantive descriptive-power gain to Pattern Library.

**Status pending audit:** OBSERVATIONAL at N=1 v69; v70 stale-check + v75 retire-check; formal promotion to sub-variant 45c at N=2 emergence (criterion 4 variant-within-pattern-at-N=2).
