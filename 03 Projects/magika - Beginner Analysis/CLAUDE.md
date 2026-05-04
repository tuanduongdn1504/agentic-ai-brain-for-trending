# magika - Beginner Analysis — CLAUDE.md

> **Created:** 2026-04-24
> **Wiki #:** v44 (44th Storm Bear corpus wiki)
> **Routine:** `llm-wiki-routine-v2.1.md` (6th v2.1-era execution)
> **Source:** https://github.com/google/magika
> **Status:** Phase 0-1 complete; executing Phases 2-6

---

## Positioning (verbatim)

> "Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accurate detection. Under the hood, Magika employs a custom, highly optimized model that only weighs about a few MBs, and enables precise file identification within milliseconds, even when running on a single CPU. Magika has been trained and evaluated on a dataset of ~100M samples across 200+ content types (covering both binary and textual file formats), and it achieves an average ~99% accuracy on our test set."

> "Magika is used at scale to help improve Google users' safety by routing Gmail, Drive, and Safe Browsing files to the proper security and content policy scanners, processing hundreds billions samples on a weekly basis."

## 12-axis classification (v2.1 Phase 0)

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE** — ML-security-classifier (8TH outside-scope sub-type candidate; NEW) |
| **Archetype** | **Google Research big-tech corporate-research-lab + Apache-OSS + academic-paper-lineage + industrial-scale-deployment** |
| **Scale tier** | **Medium (16.6K stars)** — deployment-scale is "hundreds billions weekly at Google" (distinct concept from star-count) |
| **Primary lang** | Python 33.1% + Rust 26.3% + TypeScript 18.4% + Svelte 4.9% + Go 3.9% (5-language multi-binding) |
| **Packaging tool** | **6-channel corpus-most-multi-channel**: pipx / brew / curl installer / PyPI / npm / crates.io |
| **Origin story** | Academic-research + Google Research internal + ICSE 2025 peer-reviewed (12 authors including Elie Bursztein) |
| **Methodology** | ML-classifier deep-learning model (~100M training samples) + per-content-type threshold system + 3 prediction modes |
| **Governance file count** | **Medium (3 files)** — LICENSE + CONTRIBUTING + CITATION.cff + 19 GitHub workflows CI/CD + OpenSSF Best Practices badge + CodeQL + .gemini/ Gemini Code Assist config |
| **Agent/skill count** | N/A — not an agent framework; 216 content types in standard_v3_3 model (treated as opaque classifier output) |
| **i18n coverage** | EN-only (academic/security research artifact) |
| **Intellectual influence cited** | Research-paper-chain lineage (arXiv 2409.13768 + ICSE 2025) |
| **Agent platforms supported** | N/A (not agent-targeted) |

## Scope classification rationale

**OUTSIDE-SCOPE per Storm Bear corpus definition:**
- Not primarily an agent framework
- Not extending Claude Code or agent platforms
- Not used BY agents as primary framing (could be invoked by agents for file-type-routing, but that's not primary use)
- Primary use is at Google infrastructure-scale for file-type-routing in Gmail/Drive/Safe Browsing + VirusTotal + abuse.ch
- Decision: outside-scope **ML-security-classifier 8th sub-type** (precedent: fish-speech v20 foundation-model, LlamaFactory v22 training-infra, etc.)

**Distinct from 7 prior outside-scope sub-types:**
1. education-aggregator (build-your-own-x v8)
2. foundation-model (fish-speech v20)
3. prompt-leak-archive (system-prompts-leaks v21)
4. training-infrastructure (LlamaFactory v22 + Unsloth v23)
5. design-template-aggregator (awesome-design-md v25; absorbed into #68 at v31 mini-audit)
6. MCP-server-aggregator (awesome-mcp-servers v31; absorbed into #68 at v31 mini-audit)
7. business-OS-as-product (bizos v37 OT#74)
8. **ML-security-classifier (magika v44)** — NEW

Does NOT fit Pattern #68 Awesome-List-Genre Meta-Pattern (single library, not curated list). NOT consolidation-target.

## Phase 0.5 Pattern pre-check — MANDATORY

### Strengthening / promotion candidates

1. **Pattern #42 Academic-Published Peer-Reviewed Framework** (CONFIRMED v31 via N=2 ACL 2024 + ICLR 2025) → **3rd data point ICSE 2025 Google magika**. Venue diversity: ACL (NLP) + ICLR (ML) + **ICSE (Software Engineering) NEW**. With N=3 across 3 CS conference classes, strengthens default ≥3-cross-tier path (tier spread: outside-scope + T5 + outside-scope = 2 tiers). **Action:** document as strengthening-to-N=3; propose formulation-extension acknowledging 3-venue-class diversity.
2. **Pattern #44 Academic-Lab Affiliation Archetype** (CONFIRMED v31 via N=4) → Google Research is NEW sub-variant **44d corporate-research-lab** (distinct from 44a-c academic-university variants: Lab4AI, UIUC+CMU, HKU+SJTU+NUS+Huawei). Strengthens pattern with institutional-type diversity.
3. **Pattern #17 variant 2 big-tech-curator** (CONFIRMED) → **5th data point** (Microsoft v6 + v28 + v34 + Google gws v13 + Google magika v44). **Corpus-first confirmed-variant with 5 data points.** Google now 2-entrant for variant 2.
4. **Pattern #29 License-Category-Diversity** — Apache-2.0 strengthening (consistent with gws v13 and LlamaFactory v22 outside-scope).
5. **Pattern #12 Governance-Depth (refined)** — Google corporate baseline (OpenSSF Best Practices + CodeQL + 19 workflows + CONTRIBUTING CLA + CITATION.cff + .gemini Gemini Code Assist) = strong corporate baseline confirming refined formulation ("correlates with organization + maintainer-philosophy, not scale").
6. **Pattern #2 Distribution Evolution** — 5-surface multi-binding (Rust CLI + Python + JS+WASM + Go + Rust crate) + 6-channel deployment (pipx/brew/curl/PyPI/npm/crates.io). **Corpus-most-multi-channel observation** strengthening.
7. **Pattern #58 Branding Divergence (OBSERVATION-TRACK)** — `website/` + `website-ng/` duality = **3rd observation watch data point** (after OMC v27 + ruflo v42). Website-transition-within-same-repo sub-variant 58c.

### Observational / counter-evidence

8. **Pattern #27 Community-Viral** — 16.6K stars is medium; industrial-deployment-scale ("hundreds billions weekly at Google internal use") is distinct from community-viral-star-count. **Observational sub-observation** within #27 (not new candidate).
9. **Pattern #31 Open-Core Commercial Entity** — Google magika is **fully OSS without commercial moat**. Observational counter-evidence (does not invalidate #31; #31 is about commercial entities with OSS+commercial split; Google research has different model — corporate-research-lab fully-OSS).
10. **Pattern #42 CITATION.cff observation** — corpus-first explicit Citation File Format. Academic-citation-discipline-indicator observational note within #42.
11. **Pattern #22 AGENTS.md** — absent (consistent with outside-scope academic/ML tools).
12. **OpenSSF Best Practices badge** — corpus-first. Within-Pattern-#12 governance observation (not standalone candidate).
13. **Gemini Code Assist config (.gemini/)** — corpus-first. Within-Pattern-#12 Google-internal-tooling observation.

### Overlap pre-check

All proposed observations route to within-existing-pattern strengthening. **0 new active candidates target** (8-consecutive-zero-registration streak goal v37-v44 extending 7-streak).

### Un-stale check

- #45 Dual-Licensing — not applicable (single Apache-2.0)
- #52 Extreme-Viral-Velocity — not applicable (16.6K not extreme velocity)
- No other stale candidates match. All negative.

## Phase 0.9 Primitive-count probe

Estimated primitives:
1. Rust CLI (magika binary + 22 options)
2. Python API (Magika class + identify_bytes + identify_path + identify_stream)
3. JavaScript/TypeScript library (Magika + MagikaNode + magika-js CLI)
4. Go bindings (WIP)
5. Rust crate library (magika on crates.io separate from magika-cli)
6. WASM web demo
7. 9 model versions (v1 → v3_3 + fast_v2_1 + begonly_v2_1)
8. 216 content types (treated as citation-not-replication — reference standard_v3_3/README.md)
9. 3 prediction modes (high-confidence / medium-confidence / best-guess)
10. 19 GitHub workflow CI/CD primitives
11. 6 distribution channels

**Estimated: ~6-8 distinct primitive-types → GREEN-to-light-YELLOW.**
**Decision:** GREEN fits 4-entity format cleanly. 216 content types use citation-not-replication (cite `assets/models/standard_v3_3/README.md` don't enumerate). Multi-binding stack handled in single distribution/ecosystem entity.

## Storm Bear meta-entity applicability (Phase 0.9)

**Applicable = YES (33rd consecutive).** Meta-entity included to:
- Document Storm Bear pilot relevance LOW-MEDIUM (observational > direct pilot)
- Note ML-security-classifier 8th outside-scope sub-type lineage
- Pattern #42 N=3 promotion-strengthening documentation
- 8-streak zero-new-candidates extension commentary
- Google 2nd corpus entrant (gws v13 + magika v44) — organizational archetype note

## Phase 4b routing mode

**Primary:** Outside-scope 8th sub-type + Pattern #42 N=3 default-criterion strengthening (formulation-extension candidate).

**Secondary:** Pattern #17 variant 2 5-data-point milestone + Pattern #44 sub-variant 44d corporate-research-lab formalization.

## Sibling references (mandatory Phase 2-4b cross-links)

- **v22 LlamaFactory** — Pattern #42 founding ACL 2024 data point + outside-scope training-infra sub-type precedent
- **v30 OpenHands** — Pattern #42 ICLR 2025 2nd data point; promoted at v31 mini-audit
- **v13 gws** — Pattern #12 / #17 variant 2 / Google big-tech corporate precedent + first corporate-official T4
- **v8 build-your-own-x** — first outside-scope precedent
- **v20 fish-speech** — outside-scope foundation-model precedent
- **v23 Unsloth** — outside-scope training-infra 2nd entrant (N=2 → promoted)
- **v25 awesome-design-md / v31 awesome-mcp-servers** — Pattern #68 awesome-list-genre meta-pattern (for contrast: magika is NOT awesome-list)
- **v37 bizos** — outside-scope business-OS-as-product (7th sub-type; precedent for 8th)

## Final deliverables target

- 1 project CLAUDE.md (this file)
- 3 cluster summaries (User-facing README + positioning / Multi-surface distribution + ecosystem / Research credentials + governance discipline)
- 4 entity pages (Core classifier product / Distribution + 5-language multi-binding / Pattern implications meta + Storm Bear 33rd consecutive)
- 1 bilingual VN+EN beginner guide (~400-450 lines, 10-12 parts — observational framing primary; LOW-MEDIUM pilot relevance)
- 1 Phase 4b primary deliverable (Outside-scope 8th sub-type + Pattern #42 N=3 strengthening + Pattern #17 variant 2 5-data-point milestone + Pattern #44 sub-variant 44d formalization) ~600-700 lines
- 1 iteration log v44 with 13 sections
- 1 index + 1 log + 1 open-questions

## Cross-references

- Parent routine: `/Users/Cvtot/KJ OS Template/05 Skills/llm-wiki-routine-v2.1.md`
- Pattern register: `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md`
- Root CLAUDE: `/Users/Cvtot/KJ OS Template/CLAUDE.md`
- Root GOALS: `/Users/Cvtot/KJ OS Template/GOALS.md`
