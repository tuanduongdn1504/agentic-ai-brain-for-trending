# Entity 3 — Pattern #45 NEW sub-typology 45c + Phase 4b PRIMARY

> Phase 4b PRIMARY deliverable — within-pattern sub-typology proposal for Pattern #45 Dual-Licensing Discipline

## Why this entity exists

Pattern #45 Dual-Licensing Discipline was PROMOTED to Confirmed at v60 EXTENDED MINI-AUDIT (2026-05-07) under criterion 2 structural-N=2 (Unsloth v23 Apache-2.0 + commercial-shield + AutoGPT v59 MIT + PolyForm-Shield). The promotion narrative noted that Pattern #45 captures *"a license shape that hybridizes OSS permission with commercial-protection clauses to enable both community adoption and commercial moat."*

CloakBrowser at v69 adds a **third structural sub-variant** with mechanisms substantively distinct from 45a/45b. This entity proposes formalizing this as Pattern #45 sub-typology 45c.

## Pattern #45 sub-variant taxonomy (proposed)

### 45a — OSS-with-commercial-shield clause (Unsloth v23, 2026-04-XX)

**Form:** Single LICENSE file (Apache-2.0) with commercial-use clauses inline.

**Distinguishing mechanism:** Apache-2.0 permits broad use + modification + redistribution; commercial-shield clause adds liability protection for project against commercial misuse.

**Revenue model:** Implicit — Apache-2.0 base allows commercial integrators; commercial-shield is defensive-only.

### 45b — OSS-overlaid-with-PolyForm-Family-restriction (AutoGPT v59, 2026-05-XX)

**Form:** Single LICENSE file (MIT) with PolyForm-Shield-Restrictions overlay.

**Distinguishing mechanism:** MIT base permits broad use; PolyForm-Shield-Restrictions overlay limits use that would compete with the project's commercial offering (anti-cannibalization).

**Revenue model:** Direct — PolyForm-Family-License limits competing commercial offerings; CloakHQ commercial product is the implicit moat.

### 45c — Artifact-scope-split-with-Acceptable-Use-enumeration (CloakBrowser v69, 2026-02-22+)

**Form:** TWO separate license files at repo root.
- `LICENSE` (MIT, for wrapper source code)
- `BINARY-LICENSE.md` (Proprietary + Acceptable Use, for compiled binary)

**Distinguishing mechanisms (4):**
1. **Artifact-scope split** — license boundary follows artifact compilation rather than usage tier
2. **Acceptable Use enumeration** — explicit prohibited-use list (credential stuffing / brute-force / fraud / unauthorized auth)
3. **Bounded liability cap** — $100 max aggregate liability (vs unbounded "AS IS" disclaimer in 45a/45b)
4. **OEM/SaaS commercial-licensing carve-out** — B2B revenue gate as primary monetization mechanism

**Revenue model:** Explicit B2B — direct end-user use is free; embedding in third-party-distributed products requires separate OEM/SaaS license inquiry.

## Why 45c qualifies as sub-typology (vs strengthening 45a/45b)

The promotion criteria for Pattern #45 sub-typology registration:

### Criterion 1: Structurally distinct from prior sub-variants ✅ STRONG PASS

Two separate license files at repo root is structurally distinct from 45a/45b single-file approaches. The artifact-scope-split principle (license boundary follows compilation artifact) is a different conceptual frame than the usage-tier-split principle (45a/45b: same artifact, different license terms by use case).

### Criterion 2: Mechanism cluster has internal coherence ✅ STRONG PASS

The 4 distinguishing mechanisms cohere as a deliberate B2B-licensing-architecture:
- Artifact-scope split + Acceptable Use → user-facing legal clarity
- Bounded liability + OEM/SaaS carve-out → revenue/risk-management for CloakHQ
- The mechanisms are not random — they form a coherent risk-mitigation + revenue-generation framework

### Criterion 3: Adds Pattern Library descriptive power ✅ MODERATE-STRONG PASS

Without 45c, Pattern #45 cannot capture: (a) artifact-scope splits, (b) explicit prohibited-use enumeration, (c) bounded liability caps as separate from "AS IS", (d) B2B-OEM carve-outs as primary revenue gates. These are all real license-axis mechanisms observed in the wild that Pattern #45 should capture.

→ **All 3 criteria PASS; 45c sub-typology PROPOSED for registration at v69 audit.**

## Sub-typology 45c stale-check protocol

- **v70 stale-check:** Verify 45c remains observationally accurate at next 1+ wiki cycles (no contrary evidence emerges)
- **v75 retire-check:** If no second 45c-shaped subject emerges by v75 (5 wiki gap), consider whether 45c should remain as observational or be retired to OBSERVATION-TRACK
- **Promotion eligibility:** If a second corpus subject adopts 45c-shaped licensing (artifact-scope split + Acceptable Use + bounded liability + OEM carve-out), promote to formal Pattern #45 sub-variant
- **Mechanism-prediction test:** v70+ audit should evaluate whether the 4 mechanisms in 45c remain co-occurring or split into sub-variants 45c1/45c2/etc. (e.g., is artifact-scope-split necessarily accompanied by Acceptable Use enumeration?)

## Pre-registration of "what would falsify 45c"

To maintain audit-layer fact-verification discipline (v60 audit pattern), pre-register what evidence would weaken or invalidate the 45c sub-typology:

| Evidence | Effect |
|----------|--------|
| Another corpus subject adopts 45c-shape (artifact-scope split + Acceptable Use) | **STRENGTHENS** (toward N=2 sub-variant promotion at criterion 4) |
| Another corpus subject adopts ONE mechanism but not others (e.g., artifact-scope split alone) | **REFINES** — mechanism-decoupling suggests sub-variant should split into sub-sub-variants |
| No second 45c-shape subject appears in next 5 wikis | **WEAKENS** — sub-typology becomes N=1-stale-flagged |
| Discovered: prior corpus subject (re-audited) already exemplifies 45c-shape | **CORRECTS** — 45c was retroactively present; sub-typology was discovered later but exists at N≥2 in corpus history |
| CloakBrowser changes license to drop one of the 4 mechanisms | **WEAKENS** — instability suggests 45c was incidental not structural |

## Pattern #83 N=5 consolidation evidence (no separate proposal-document)

CloakBrowser also contributes to Pattern #83 Honest-Deficiency-Disclosure Discipline as N=5 consolidation evidence. **No separate proposal-document filed at v69** because:
- Pattern #83 was already PROMOTION-ELIGIBLE at N=3 from v67 (v67 proposal-document filed)
- v68 added N=4 consolidation evidence (noted in iteration log; no new proposal)
- v69 adds N=5 consolidation evidence (noted in iteration log; no new proposal)
- Pattern #83 promotion happens at v69 audit batch (~24-25 items LARGEST)

**v69 Pattern #83 evidence summary (5 disclosure surfaces in single subject):**
1. **BINARY-LICENSE explicit security disclaimer** — `"THE BINARY IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED..."`
2. **CHANGELOG #217 path-traversal security fix** — explicitly named + linked
3. **`$100 max-liability cap`** — defensive financial framing (not hidden)
4. **Acceptable Use enumeration** — explicit prohibition list (not vague)
5. **macOS platform-tier-disparity disclosure in README** — *"macOS fingerprints have inconsistencies aggressive sites catch..."*

These 5 surfaces are structurally distinct (LICENSE / CHANGELOG / Liability / Acceptable Use / Platform-disparity) — corpus-broadest multi-surface saturation continues from v67/v68 trajectory.

## What 45c registration looks like in Pattern Library

Proposed entry in `_patterns/03-active-candidates.md` (under existing Pattern #45 section):

```markdown
### Pattern #45 sub-typology 45c — Artifact-Scope-Split with Acceptable-Use-Enumeration

**Source:** CloakBrowser v69 (2026-02-22 → 2026-05-18 observation)

**Structural form:** Two separate license files at repo root, with license boundary following artifact-compilation scope rather than usage-tier scope.

**Distinguishing mechanisms (4 co-occurring):**
1. Artifact-scope split — MIT wrapper-source + Proprietary compiled-binary
2. Acceptable Use enumeration — explicit prohibited-use list in binary license
3. Bounded liability cap — fixed-dollar max-aggregate-liability ($100)
4. OEM/SaaS commercial-licensing carve-out — B2B revenue-gate for product-embedders

**Status:** OBSERVATIONAL at N=1 v69; v70 stale-check + v75 retire-check; promotion to formal sub-variant at criterion 4 variant-within-pattern-at-N=2 if second 45c-shape subject emerges.

**Sister observation:** 45a Unsloth v23 (commercial-shield clauses inline) + 45b AutoGPT v59 (PolyForm-Shield overlay). 45c is structurally distinct (two-file artifact-scope-split vs single-file hybrid).
```

## Phase 4b PRIMARY conclusion

**Proposal:** Register Pattern #45 sub-typology 45c at v69 iteration log + 03-active-candidates.md. Defer promotion-to-formal-sub-variant to v69 audit batch (where Pattern #45 promotion may be re-evaluated alongside Pattern #83 promotion).

**Confidence:** **HIGH** — all 3 promotion criteria PASS; mechanism-cluster is internally coherent; structurally distinct from 45a/45b; descriptive-power gain is substantive.

**Trade-offs acknowledged:**
- N=1 alone is below sub-variant promotion threshold (requires N=2 per criterion 4)
- Sub-typology registration is a softer commitment than promotion — appropriate at v69; promotion deferred to N=2 emergence
- Pattern #45 already promoted at v60; sub-typology is within-pattern strengthening + nomenclature formalization (vs new pattern registration which v68 did for Pattern #86)

**Routine v2.2 lesson captured:** "Sub-typology proposal-document discipline" — for cases where new evidence adds a substantively distinct sub-variant within an already-promoted pattern, a sub-typology proposal-document is the appropriate vehicle (vs full new-pattern registration or simple within-pattern strengthening note). Add to routine v2.3 codification queue.
