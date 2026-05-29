# (C) Phase 4b PRIMARY — Library-vocab "Vendored-Dependency-Author Promoted to Direct Subject" PROVISIONAL N=1

**Vehicle:** routine v2.3 §3 Phase 4b vehicle #7 (Library-vocab observational-layer registration).
**Confidence:** HIGH (the corpus-recursive chain is verifiable from prior state).
**Subject:** v105 `op7418/guizang-social-card-skill`.

## The observation

op7418 (歸藏/Guizang) entered the corpus **as a vendored dependency, not as a subject**:

- **v83 open-design** bundled `skills/guizang-ppt/` (op7418's `guizang-ppt-skill`) in-tree.
- **v91 html-anything** vendored `op7418/guizang-ppt-skill` in its cross-product skill-vendoring chain.

In both cases op7418's work was a **building-block inside another author's subject** — never analyzed directly. At v105, a **different op7418 product** (`guizang-social-card-skill`, a sibling to the vendored `guizang-ppt-skill`) becomes the **direct subject**.

This is a corpus-recursive event: a previously-vendored-dependency author is promoted to direct-subject status via a *sibling* product.

## Proposed Library-vocab item

> **"Vendored-Dependency-Author Promoted to Direct Subject"** — a subject whose author was previously present in the corpus only as a *vendored/bundled dependency inside another subject's repository*, now analyzed as a direct subject in their own right (here via a sibling product, not the originally-vendored one).

## Relationship to v93 "Retrospective-Promotion-from-Cited-to-Subject"

Structurally adjacent but distinct:

| Axis | v93 anthropics/skills (cited→subject) | v105 op7418 (vendored→subject) |
|---|---|---|
| Prior corpus presence | **Cited/referenced** in prose at multiple wikis | **Vendored/bundled** as a dependency skill (v83 in-tree, v91 vendored) |
| Same product? | Same repo promoted from cited to subject | **Different sibling product** by same author |
| Layer | Reference-citation layer | Dependency/build-artifact layer |

Recommendation: register as a **distinct Library-vocab item** (this doc) rather than folding into v93 — the vendoring-as-dependency layer and the sibling-product hop are materially different from prose-citation-of-same-repo. Note the kinship to v93 explicitly and watch both as a possible future "Prior-Presence-to-Direct-Subject" parent class at v2.4 codification.

## Promotion ladder

- **N=1 PROVISIONAL** at v105.
- First-cycle stale-check at next audit (v106 if audit-only, else v110).
- N=2 watch: any future subject whose author was previously only vendored/bundled in the corpus.
- 15-wiki forced-retire (≈v120) if N=1-only, per Library-vocab retire-check cadence.

## SECONDARY observations (held at OC layer per cascade-discipline — NOT registered at ship)

1. **Pattern #28 sister "Editorial-Build-Validator" N=2 STRENGTHENING** — v75 impeccable (`npx impeccable detect` + STYLE.md denylist, 27 anti-pattern rules) + v105 (`validate-social-deck.mjs`, 6 deterministic Playwright QA rules: overflow / type-size / footer-collision / 4-band density / frame-overflow / Swiss identity). 30-wiki gap. PROMOTION-ELIGIBLE watch at next audit.
2. **Pattern #19 sub-mechanism 19m "Chinese-AI-Native-Coder-Influencer-with-Multi-Product-Portfolio" N=2 STRENGTHENING** — v82 alchaincyf (花叔) anchor + v105 op7418 (歸藏). Both: large-following Chinese AI influencer + multi-product skill/prompt portfolio + `npx skills add` distribution + design-skill output.
3. **Pattern #88 Anti-Slop-Design-Curation N+1** — op7418 publicly iterates "Stop Slop / 去 AI 味" skills (5 core rules + 6-item pre-delivery checklist + 5-dimension quantitative evaluation per his own posts); the social-card skill's fixed-palette discipline + 6-rule validator embody 88c machinery-with-enforcement.
4. **Pattern #83 83f license-declaration-mismatch N+1** — `package.json` declares `"license": "ISC"` (npm-init boilerplate default, empty author/description) while repo LICENSE is **AGPL-3.0**.
5. **China-Mainland sub-cluster N+1 + Asian-LOCATED cluster N+1** — by-event (v82 + v83/v91 + v94 + v100 + v105).
6. **Pattern #52 EXTREME-VIRAL pulse N+1** — ~400 stars/day × 2 days (pulse, not sustained; joins v63/v68/v78/v82/v83/v94 pulse instances).
7. **Pattern #82 quantitative-marketing** (28 layouts / 10 themes / 6 rules / 11 categories / 3 sizes / 9 assets) + **Pattern #78 LDS** (15 reference spec docs).
8. **`npx skills add` install-convention** continuity within the op7418 / Chinese design-skill ecosystem (v82 + v83 + v105).
9. **AGPL-3.0 NOT corpus-first** — prior AGPL subjects exist in v1–v60 chapters. Recorded as an honest non-claim; notable only as strong-copyleft for a single-author design skill and as a license-divergence from op7418's Apache-bundled sibling.

## v2.4 codification candidates contributed

- "Vendored-Dependency-Author Promoted to Direct Subject" as a possible corpus-recursive event sub-class (§26 taxonomy extension; sits alongside Class 1–4 + v93 cited-to-subject).
- "Prior-Presence-to-Direct-Subject" candidate parent class unifying v93 (cited) + v105 (vendored).
