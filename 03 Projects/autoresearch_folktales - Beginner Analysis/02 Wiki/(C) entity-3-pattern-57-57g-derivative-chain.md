# (C) Entity 3 — Phase 4b PRIMARY: Pattern #57 NEW sub-variant 57g "Second-Order-Derivative-Chain via intermediate-adapter"

**Phase 4b PRIMARY entity** (pre-registered at Phase 0; structures around Pattern Library PRIMARY deliverable).

**Pre-registration**: `v79 autoresearch_folktales: Phase 0 pre-registered Pattern #57 NEW sub-variant 57g candidate "Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter" PROVISIONAL N=1 registration as Phase 4b PRIMARY`.

**Cross-link target**: Entities 1 + 2 + 4 + Cluster 1 + Cluster 2 + Cluster 3 all reference this entity.

## 13-section canonical format

### 1. What is Pattern #57 (background)

**Pattern #57 = corpus-recursive citation** (CONFIRMED pattern; v60+ active).

**Current sub-variants** (post-v78):
- **57a**: corpus-foundation-individual citation (e.g., Karpathy / Bostrom / Lance Martin cited as influence)
- **57b**: corpus-project citation (one corpus subject cites another by URL)
- **57c-product**: corpus-product citation (corpus subject explicitly names another corpus subject as product/dependency)
- **57c**: 3+ corpus-subject ecosystem-citation in single subject
- **57d**: long-citation-chain (3+ hops within corpus)
- **57e**: Multi-Source-Derivative-Attribution-Chain via NOTICE.md (v75 candidate)
- **57f**: **Corpus-Recursive-Anchor-Self-Reference** (v78 PROVISIONAL N=1 — wiki revisits its own anchor subject)

### 2. NEW sub-variant 57g candidate: definition

**57g "Second-Order-Derivative-Chain-of-Corpus-Foundation-Subject via intermediate-adapter"** PROVISIONAL N=1 registration.

**Definition**: A corpus subject that is a DERIVATIVE of a corpus-foundation-subject's PUBLIC CODEBASE, mediated by an EXPLICIT INTERMEDIATE ADAPTER (not direct fork; an intermediate party performs cross-platform / cross-substrate / cross-OS / cross-runtime layer-work), with all 3 actors (foundation + adapter + this subject) attributed in the subject's own documentation.

**Structure**:
```
Corpus-foundation-subject (v9 corpus member)
        ↓ [public codebase fork]
Intermediate-adapter (NOT in corpus; performs cross-substrate work)
        ↓ [public codebase fork]
This subject (v79 corpus member; explicitly attributes both upstreams)
```

**Distinct from**:
- **57a**: corpus-foundation-individual citation — citation only, no codebase chain
- **57b/c**: corpus-project citation — direct one-hop reference
- **57c-product**: corpus-subject product-relationship — within single tier
- **57d**: long-citation-chain — citation hops, not codebase forks
- **57e**: Multi-Source-Derivative-Attribution via NOTICE.md — multi-source within one artifact (v75 impeccable: Anthropic frontend-design + ehmo/typecraft-guide-skill)
- **57f**: Corpus-Recursive-Anchor-Self-Reference — same subject revisited at delta time

→ **57g is uniquely: codebase-derivative + sequential-2-hop + intermediate-adapter-NOT-in-corpus + explicit-attribution-of-all-3-actors**.

### 3. N=1 evidence: v79 autoresearch_folktales

**Evidence document (verbatim from README Credits section)**:

> - Original autoresearch: Andrej Karpathy
> - macOS/MPS adaptation: miolini/autoresearch-macos
> - Dataset: merve/folk-mythology-tales

**Plus URLs cited in README**:
- `https://github.com/karpathy/autoresearch` (v9 corpus subject)
- `https://github.com/miolini/autoresearch-macos` (intermediate adapter; NOT in corpus)
- `https://github.com/karpathy/nanochat` (Karpathy-internal upstream; underlying training implementation)

**Chain structure**:
```
karpathy/autoresearch (v9 corpus parent, 2025-Q1 era; methodology source)
                ↓
            miolini/autoresearch-macos (intermediate adapter; macOS-layer work; NOT corpus member)
                ↓
            thu-vu92/autoresearch_folktales (v79 corpus subject; Apple Silicon MPS + folktales dataset)
```

**Per-criterion evaluation** (source-celebrity-derivative-distillation criteria from routine v2.2):

| Criterion | Status | Evidence |
|-----------|--------|----------|
| (1) Author ≠ source individual | ✅ PASS | Thu Vu ≠ Karpathy ≠ miolini |
| (2) Explicit source attribution with URL | ✅ PASS | All 3 GitHub URLs cited in README Credits |
| (3) Public observations as raw material | ✅ PASS | All 3 upstream artifacts are public GitHub repos |
| (4) Installable artifact packaging | ✅ PASS | uv-installable Python package; README quick-start sequence |

→ **All 4 source-celebrity-derivative-distillation criteria PASS**.

### 4. Structural diversity: what's preserved + what's modified

**Preserved verbatim from Karpathy original**:
- `program.md` agent skill (byte-identical or near-byte-identical based on text comparison)
- 5-min fixed-time-budget
- val_bpb evaluation metric
- Single-modifiable-file architecture
- git-state-tracking + branch-naming-discipline
- 9-step experiment loop
- "NEVER STOP" autonomy escalation

**Modified at train.py + dependency-layer (Thu Vu's contribution)**:
- FlashAttention-3 → native PyTorch SDPA + manual sliding-window causal masking
- `torch.compile` MPS-incompatible paths disabled
- Metal-compatible optimizer states (Muon + AdamW)
- No distributed training (single-Apple-Silicon-device)

**Modified at dataset-layer**:
- folk-mythology-tales dataset (Hugging Face: `merve/folk-mythology-tales`) vs Karpathy original web-text corpus

**Inherited from intermediate-adapter (miolini)**:
- Some/all of the MPS-compatibility groundwork (cannot verify without comparing miolini's repo vs Thu Vu's repo directly; but credit-attribution implies miolini supplied some adapter-layer code)

### 5. Promotion criteria evaluation (5 + 1 dimension routine v2.2)

| # | Criterion | Status at N=1 |
|---|-----------|--------------|
| 1 | Default: ≥3 observations across 2+ tiers | FAIL at N=1; need N≥3 |
| 2 | Structural-unambiguity-at-N=2 | FAIL at N=1; need N=2 |
| 3 | Spectrum-pattern-at-N=2 | N/A — sub-variant not spectrum |
| 4 | Variant-within-pattern-at-N=2 | PRESENT (57g is sub-variant within Pattern #57); FAIL at N=1; need N=2 |
| 5 | Meta-pattern-at-N=3-consolidation | N/A |
| NEW v2.2 | Cross-archetype N-counting | N/A at N=1 |

**Verdict**: REGISTER as PROVISIONAL N=1 sub-variant. Re-evaluate at N=2.

**Expected promotion trigger**: when another corpus subject emerges with similar 3-actor codebase-derivative-chain-via-intermediate-adapter structure. Examples of potential N=2 future subjects:
- A future MPS-port-via-intermediate-adapter of nanoGPT / nanochat (Karpathy lineage)
- A future macOS-port via someone else's adapter of any v60+ corpus framework
- A future Apple-Silicon-port via miolini adapter of a different ML framework

### 6. Stale-check + retire-check schedule

- **First-cycle stale-check at v84** (+5 wikis from registration)
- **Retire-check at v89** (+10 wikis from registration)
- **N+1 acceleration possible** if a v80-v83 wiki provides N=2 evidence (would trigger 1-wiki rapid-evolution at sub-variant layer, advancing Library-vocabulary item #10 evidence)

### 7. Distinguishing from v78's 57f

**v78 57f "Corpus-Recursive-Anchor-Self-Reference"**:
- Same subject revisited at time-delta (v1 ECC 2026-04-17 → v78 ECC 2026-05-20 at 33-day delta)
- Anchor identity preserved (`affaan-m/everything-claude-code` → `affaan-m/ECC`)
- 0-hop (identity, not chain)
- Maximum depth of self-reference

**v79 57g "Second-Order-Derivative-Chain via intermediate-adapter"**:
- DIFFERENT subject (Thu Vu's repo ≠ Karpathy's repo)
- Methodology inheritance via 2-hop chain (Karpathy → miolini → Thu Vu)
- INTERMEDIATE ADAPTER not in corpus (miolini)
- 2-hop chain depth

→ **Clean sub-variant taxonomy 57f vs 57g**:

| Axis | 57f | 57g |
|------|-----|-----|
| Subject identity | Same as anchor | Different from anchor |
| Hop count | 0 (self-reference) | 2 (chain) |
| Intermediate adapter | N/A | Required (NOT in corpus) |
| Time relation | Delta from anchor | Delta from corpus-foundation |
| Layer of preservation | Methodology + corpus-evaluation snapshot | Methodology only (technical-layer modified) |

### 8. 2-wiki consecutive sub-variant accumulation observation

**v78 57f registered + v79 57g registered = 2-wiki consecutive Pattern #57 sub-variant accumulation arc.**

→ **Library-vocabulary item #10 strengthening evidence at sub-variant-layer** (distinct from prior item #10 instances at top-level-pattern-layer):
- v62→v63 Pattern #76 1-wiki counter-evidence cycle (TIED FASTEST at top-level)
- v64→v65 Pattern #78 1-wiki un-stale-via-N=2-evidence cycle (TIED FASTEST at top-level)
- **v78→v79 Pattern #57 2-wiki consecutive sub-variant accumulation (NEW EVIDENCE at sub-variant-layer)**

This is a different DIMENSION than prior item #10 instances:
- Prior: pattern-evolution (registration → counter-evidence within 1 wiki)
- v78→v79: sub-variant-accumulation (sub-variant registration → sub-variant registration in 1-wiki gap; both at PROVISIONAL N=1; no immediate promotion-acceleration yet but cluster-strengthening at Pattern #57 sub-variant-taxonomy)

→ At v80+ audit: consider whether sub-variant-accumulation in N-wiki gap deserves its OWN observational meta-pattern.

### 9. Sub-taxonomy decision

**Sub-taxonomy proposal at v80 audit**: REGISTER 57g as PROVISIONAL sub-variant within Pattern #57. Re-evaluate at N=2.

**Alternative considered**: PROMOTE TO TOP-LEVEL Pattern at N=2 if structurally-orthogonal to existing Pattern #57 framing. Currently 57g fits cleanly under Pattern #57's "corpus-recursive citation" umbrella; no top-level promotion needed.

**Alternative considered**: MERGE 57f + 57g into single "Corpus-Recursive-with-Depth-Variants" sub-variant. REJECTED — 57f and 57g have distinct mechanisms (self-reference vs chain-hop) that warrant separate sub-variants.

### 10. Audit checklist for v80 audit

- [ ] Verify 57g N=1 evidence package is complete (this entity + Cluster 1 §11 + Cluster 2 §15)
- [ ] Stale-check at v84 (5-wiki rule)
- [ ] Retire-check at v89 (10-wiki rule)
- [ ] N+1 acceleration scan v80-v83 wikis for similar 2-hop-codebase-derivative structures
- [ ] Distinct-from-57f confirmation (no merge)
- [ ] Pattern #57 sub-variant taxonomy update: 7 sub-variants (57a/57b/57c-product/57c/57d/57e/57f/57g) — wait, that's 8. Let me re-check. 57a/57b/57c/57c-product/57d/57e/57f/57g → 8. The 57c + 57c-product distinction is a sub-sub-variant. Re-verify naming convention.

### 11. Cross-references to evidence documents

- **Cluster 1** § 5 "Methodology lineage" + § 10 "Credits section"
- **Cluster 2** § 1 "Cluster scope" + § 2 "Positioning of program.md" (verbatim Karpathy inheritance)
- **Cluster 3** § 2 "Hugging Face datasets integration" + § 3 "Apple Silicon hardware-substrate-pinned distribution"
- **Entity 1** § 1 "What is it" + § 2 "Tier placement + archetype" + § 10 "Cross-wiki sibling references"
- **Entity 2** § 1 "Packaging tool" + § 10 "Cross-wiki distribution-pattern intersections"
- **Entity 4** Storm Bear meta-entity strength categorization (STRONG INCLUDE 3/4 via criterion (d) STRONG PASS — corpus-recursive at second-order-chain depth)

### 12. Implications for Phase 5 Pattern Library register update

**Direct register updates** (will be applied at Phase 5):
1. Register 57g as PROVISIONAL N=1 sub-variant in Pattern #57 entry
2. Add stale-check at v84 + retire-check at v89 to stale-tracking table
3. Update Library-vocabulary item #10 with v78→v79 sub-variant-accumulation strengthening evidence at sub-variant-layer
4. Cross-pattern coupled-design item #9 strengthening: 7+-pattern coupled-design at single wiki (Pattern #57 + #83 + #84 + #66 + #18 + #19 + #45 + Library-vocab item #10)

### 13. Recommended verdict (PROVISIONAL)

**REGISTER 57g sub-variant as PROVISIONAL N=1 candidate within Pattern #57.**

**Confidence**: HIGH for the registration itself (clean evidence chain; all 4 source-celebrity-derivative-distillation criteria PASS; structural distinctness from 57f confirmed).

**Confidence**: LOW for any promotion-related discussion at v80+ until N=2 evidence emerges.

**No top-level promotion implications at v80** — 57g sits under Pattern #57 which is already CONFIRMED; sub-variant registration is administrative.

**Phase 4b PRIMARY proposal-document location**: `01 Analysis/(C) Pattern-57-57g-second-order-derivative-chain-of-corpus-foundation-subject-N1-registration.md`
