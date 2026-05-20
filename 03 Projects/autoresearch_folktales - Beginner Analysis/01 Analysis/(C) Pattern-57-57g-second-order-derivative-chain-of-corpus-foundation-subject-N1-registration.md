# (C) Pattern #57 NEW sub-variant 57g "Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter" — N=1 registration proposal

**Proposal-document discipline** (per routine v2.2 §"NEW Pattern candidate proposal-document"):

- **Status**: PROVISIONAL REGISTRATION at v79 ship (2026-05-20)
- **Confidence**: HIGH for registration itself; LOW for any promotion discussion at v80+ until N=2 evidence emerges
- **Evidence depth**: N=1 (this proposal documents a single subject — v79 thu-vu92/autoresearch_folktales)
- **Sub-variant taxonomy**: 57g — new sub-variant within already-CONFIRMED Pattern #57
- **Top-level promotion implications at v80**: NONE (Pattern #57 already CONFIRMED; sub-variant registration is administrative)
- **First-cycle stale-check**: v84 (5-wiki rule)
- **Retire-check**: v89 (10-wiki rule)

## 1. Current status of Pattern #57 (background)

**Pattern #57 = corpus-recursive citation** (CONFIRMED pattern; v60+ active).

**Current sub-variants (pre-v79)**:
- **57a** — corpus-foundation-individual citation (e.g., Karpathy / Bostrom / Lance Martin cited as influence)
- **57b** — corpus-project citation (one corpus subject cites another by URL)
- **57c-product** — corpus-product citation (subject explicitly names another corpus subject as product/dependency)
- **57c** — 3+ corpus-subject ecosystem-citation in single subject
- **57d** — long-citation-chain (3+ hops within corpus)
- **57e** — Multi-Source-Derivative-Attribution-Chain via NOTICE.md (v75 impeccable PROVISIONAL N=1 candidate)
- **57f** — **Corpus-Recursive-Anchor-Self-Reference** (v78 ECC PROVISIONAL N=1 — wiki revisits its own anchor subject at delta time)

**Sub-variant taxonomy depth at pre-v79**: 7 sub-variants documented.

## 2. NEW sub-variant 57g — definition

**57g "Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter"** PROVISIONAL N=1 registration.

### Definition

A corpus subject that is a DERIVATIVE of a corpus-foundation-subject's PUBLIC CODEBASE, mediated by an EXPLICIT INTERMEDIATE ADAPTER (not direct fork; an intermediate party performs cross-platform / cross-substrate / cross-OS / cross-runtime layer-work), with all 3 actors (foundation + adapter + this subject) attributed in the subject's own documentation.

### Structure

```
Corpus-foundation-subject (in corpus; the source methodology)
        ↓ [public codebase fork]
Intermediate-adapter (NOT in corpus; performs substrate/platform/runtime adapter work)
        ↓ [public codebase fork]
This subject (in corpus; the wiki target)
```

### Required criteria for 57g classification

1. **Foundation must be IN-CORPUS** (a v-numbered corpus subject)
2. **Intermediate adapter must be EXPLICITLY ATTRIBUTED** (not just used silently; explicit URL citation)
3. **Intermediate adapter must NOT be in corpus** (otherwise the chain would be a 3-corpus-subject 57c sub-variant, distinct)
4. **Subject is DERIVATIVE of codebase** (not derivative of public-observations like tweets / talks — those are 57c-product or source-celebrity-derivative-distillation)
5. **All 3 actors documented in subject's README or equivalent**
6. **Methodology of foundation is preserved with modifications localized to substrate-layer** (otherwise the work is a new framework inspired-by, not a 2-hop derivative)

## 3. N=1 evidence: v79 autoresearch_folktales

### Foundation (in corpus)

**`karpathy/autoresearch`** — v9 corpus subject. Andrej Karpathy's autonomous-agent ML-research framework.

**Wiki**: `03 Projects/autoresearch - Beginner Analysis/`

**Original methodology**: 5-min fixed time budget + val_bpb metric + single-modifiable-file + never-stop-autonomy + git-state-tracking + 9-step experiment loop.

### Intermediate adapter (NOT in corpus)

**`miolini/autoresearch-macos`** — NOT a v-numbered corpus subject.

**Role**: macOS layer adapter; provides macOS-compatibility groundwork for Karpathy's original CUDA-targeted framework.

**Evidence of explicit attribution** (from Thu Vu's README Credits section):
> *"macOS/MPS adaptation: miolini/autoresearch-macos"*

### Subject (in corpus, this v79 wiki)

**`thu-vu92/autoresearch_folktales`** — v79 corpus subject.

**Modifications layered on top of intermediate adapter**:
1. Apple Silicon / MPS deeper adaptation (FlashAttention-3 removal; PyTorch SDPA substitution; torch.compile-disabled paths; Metal-compatible optimizer states)
2. folk-mythology-tales dataset (via Hugging Face `merve/folk-mythology-tales`)

**Methodology preservation**:
- `program.md` agent skill byte-identical or near-byte-identical to Karpathy original (verbatim agent instructions)
- 5-min fixed time-budget unchanged
- val_bpb evaluation metric unchanged
- 9-step experiment loop unchanged
- single-modifiable-file architecture unchanged
- "NEVER STOP" autonomy escalation unchanged

→ **Modifications confined to substrate-layer (train.py + dependency-config + dataset-config); methodology layer preserved verbatim**. Clean separation matches 57g definition criterion #6.

## 4. Structural diversity table

| Criterion | Evaluation |
|-----------|------------|
| In-corpus foundation | ✅ Karpathy v9 |
| Explicit intermediate-adapter attribution | ✅ miolini cited in README Credits |
| Intermediate-adapter NOT in corpus | ✅ miolini = unwikied subject |
| Codebase-derivative | ✅ Python code forked + modified |
| Methodology preserved with substrate-layer modifications only | ✅ program.md verbatim + train.py modified |
| All 3 actors documented | ✅ Karpathy + miolini + Thu Vu credited |

→ All 6 sub-variant-criteria PASS at N=1.

## 5. Source-celebrity-derivative-distillation criteria (v2.2 routine § 4 criteria)

Re-checking the 4 source-celebrity-derivative-distillation criteria from routine v2.2:

| Criterion | Status | Evidence |
|-----------|--------|----------|
| (1) Author ≠ source individual | ✅ PASS | Thu Vu ≠ Karpathy ≠ miolini |
| (2) Explicit source attribution with URL | ✅ PASS | All 3 GitHub URLs in README Credits |
| (3) Public observations as raw material | ✅ PASS | All 3 upstream artifacts public |
| (4) Installable artifact packaging | ✅ PASS | uv-installable Python package |

→ All 4 criteria PASS — strengthens 57g registration confidence.

## 6. Promotion criteria evaluation (5 + 1 dimension routine v2.2)

| # | Criterion | Status at N=1 |
|---|-----------|--------------|
| 1 | Default: ≥3 observations across 2+ tiers | FAIL at N=1; need N≥3 |
| 2 | Structural-unambiguity-at-N=2 | FAIL at N=1; need N=2 |
| 3 | Spectrum-pattern-at-N=2 | N/A — sub-variant not spectrum |
| 4 | Variant-within-pattern-at-N=2 | APPLICABLE (57g is sub-variant within Pattern #57); FAIL at N=1; PROMOTION-ELIGIBLE at N=2 |
| 5 | Meta-pattern-at-N=3-consolidation | N/A |
| NEW v2.2 | Cross-archetype N-counting | N/A at N=1 |

**Recommended verdict**: REGISTER as PROVISIONAL N=1 sub-variant within Pattern #57.

## 7. Distinguishing 57g from existing sub-variants

### Distinct from 57a (corpus-foundation-individual citation)
- 57a is **citation only**, no codebase chain
- 57g requires **codebase fork + modification**

### Distinct from 57b/57c (corpus-project citation)
- 57b/57c are **direct one-hop reference between corpus subjects**
- 57g requires **2-hop chain via NON-CORPUS intermediate adapter**

### Distinct from 57c-product (corpus-product citation)
- 57c-product is **product-relationship within single tier** (Codex uses Claude Code; cross-wiki product chains)
- 57g is **codebase-derivative chain across tiers + via intermediate**

### Distinct from 57d (long-citation-chain)
- 57d is **citation hops** (3+ subjects connected by citations)
- 57g is **codebase forks** (functional inheritance, not citation-only)

### Distinct from 57e (NOTICE.md multi-source attribution)
- 57e is **multi-source within ONE attribution-file** (v75 impeccable: Anthropic frontend-design + ehmo/typecraft-guide-skill in NOTICE.md)
- 57g is **sequential 2-hop chain through an intermediate adapter** (chain depth)

### Distinct from 57f (anchor-self-reference)
- 57f is **same subject revisited at time-delta** (v78 ECC: v1 anchor → v78 anchor-self at 33-day delta)
- 57g is **DIFFERENT subject** derivative via chain depth

→ **Clean sub-variant 57f vs 57g taxonomy**:

| Axis | 57f | 57g |
|------|-----|-----|
| Subject identity | Same as anchor | Different from anchor |
| Hop count | 0 (self-reference) | 2 (chain) |
| Intermediate adapter | N/A | Required (NOT in corpus) |
| Time relation | Delta from anchor (within wiki series) | Delta from corpus-foundation (within methodology lineage) |
| Layer of preservation | Methodology + corpus-evaluation snapshot | Methodology only (substrate-layer modified) |
| Number of authors in chain | 1 (same author, but different snapshot) | 3 (foundation + adapter + this subject) |

## 8. 2-wiki consecutive sub-variant accumulation observation

**v78 57f registered + v79 57g registered = 2-wiki consecutive Pattern #57 sub-variant accumulation arc.**

→ **Library-vocabulary item #10 strengthening evidence at sub-variant-layer** — distinct from prior item #10 instances at top-level-pattern-layer:

| Prior #10 instance | Layer | Cycle speed |
|--------------------|-------|-------------|
| v62→v63 Pattern #76 counter-evidence | top-level (registration + counter) | 1 wiki (TIED FASTEST) |
| v64→v65 Pattern #78 un-stale-via-N=2 | top-level (registration + N=2) | 1 wiki (TIED FASTEST) |
| **v78→v79 Pattern #57 sub-variant accumulation** | sub-variant layer (registration + adjacent-registration) | 1 wiki gap |

This is a DIFFERENT DIMENSION than prior item #10 instances:
- Prior: pattern-evolution (registration → counter-evidence within 1 wiki at top-level)
- v78→v79: sub-variant-accumulation (sub-variant registration → adjacent sub-variant registration; both at PROVISIONAL N=1; no immediate promotion-acceleration but cluster-strengthening within Pattern #57)

→ At v80 audit: consider whether sub-variant-accumulation in N-wiki gap deserves its OWN observational meta-pattern, distinct from current Library-vocabulary item #10 framing.

## 9. Audit checklist for v80

- [ ] Verify 57g N=1 evidence package is complete (this proposal + Entity 3 + Cluster 1 §11 + Cluster 2 §15)
- [ ] Stale-check schedule at v84 (5-wiki rule)
- [ ] Retire-check schedule at v89 (10-wiki rule)
- [ ] N+1 acceleration scan v80-v83 for similar 2-hop-codebase-derivative-with-intermediate-adapter structures
- [ ] Confirm distinct from 57f (no merge)
- [ ] Update Pattern #57 sub-variant taxonomy entry — 8 sub-variants total post-v79: 57a / 57b / 57c-product / 57c / 57d / 57e / 57f / 57g
- [ ] Update Library-vocabulary item #10 with sub-variant-layer evidence
- [ ] Consider whether sub-variant-accumulation deserves separate observational meta-pattern

## 10. Pre-Phase-6 fact-verification

**Cross-checked against existing Pattern Library state**:
- Pattern #57 status: CONFIRMED (verified from `_patterns/02b-confirmed-patterns-v42-plus.md` discussion in CLAUDE.md state-block)
- Pattern #57 existing sub-variants: 57a/57b/57c/57c-product/57d/57e (v75)/57f (v78) — taxonomy at 7 entries pre-v79
- Pattern #57 evidence list: includes Karpathy (v9), forrestchang/karpathy-skills (v63), nanochat (v60-range Karpathy artifact), many others
- Library-vocabulary item #10 status: codified at routine v2.2 with v62→v63 + v64→v65 baseline evidence; v78→v79 adds NEW sub-variant-layer dimension

**No retroactive corrections triggered by v79 evidence on prior wikis**.

## 11. Recommended verdict

**REGISTER 57g sub-variant as PROVISIONAL N=1 candidate within Pattern #57.**

- Confidence in registration: **HIGH** (clean evidence chain; all 6 sub-variant-criteria PASS; structural distinctness from 57f confirmed; all 4 source-celebrity-derivative-distillation criteria PASS)
- Confidence in promotion-related discussion at v80+: **LOW** until N=2 evidence emerges
- Top-level Pattern #57 status: UNCHANGED (already CONFIRMED)
- Sub-variant taxonomy expansion: 7 → 8 sub-variants

**No top-level promotion implications at v80** — 57g sits under Pattern #57 which is already CONFIRMED; sub-variant registration is administrative.

## 12. Evidence document cross-references

- **Cluster 1** (User-facing docs): § 5 "Methodology lineage" + § 10 "Credits section" + § 12 "Pattern Library implications"
- **Cluster 2** (program.md): § 1 "Cluster scope" + § 2 "Positioning" + § 11 "Cross-wiki sibling intersections" + § 15 "Phase 4b PRIMARY confirmation"
- **Cluster 3** (Technical/distribution): § 2 "Hugging Face datasets integration" + § 3 "Apple Silicon MPS adaptation" + § 13 "Pattern Library implications"
- **Entity 1** (Core product): § 1 "What is it" + § 2 "Tier placement + archetype" + § 9 "Dataset substitution"
- **Entity 2** (Distribution): § 1 "Packaging tool" + § 10 "Cross-wiki distribution-pattern intersections"
- **Entity 3** (Phase 4b PRIMARY): full entity — most-detailed evidence package
- **Entity 4** (Storm Bear meta + Pattern Library implications package): § 5 "(d) STRONG PASS" + § 8 "Pattern Library implications package"

## 13. Filing instructions for Phase 6 vault sync

**Where this proposal lives**: `03 Projects/autoresearch_folktales - Beginner Analysis/01 Analysis/(C) Pattern-57-57g-second-order-derivative-chain-of-corpus-foundation-subject-N1-registration.md` (this file).

**Where to register at Pattern Library**:
- Add 57g entry to `_patterns/03-active-candidates.md` (Active Candidates section)
- Update `_patterns/05-recent-additions.md` § "v79 strengthening block" with PRIMARY narrative
- Update PATTERN_LIBRARY.md root shim (if explicit Pattern #57 sub-variant mention exists; otherwise skip)
- Update stale-tracking table with v84 stale-check + v89 retire-check entries

**No top-level state transitions to apply** — Pattern Library counts unchanged (45 confirmed / 29 active / 0.644 ratio); Pattern #57 already CONFIRMED.
