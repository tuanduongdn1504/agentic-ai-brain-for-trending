# (C) License-axis — Dual-licensing MIT + PolyForm-Shield un-stales Patterns #45 and #72

> **Entity 2 of 4** — AutoGPT v59
> **Type:** Pattern-test entity (license-axis convergence; double un-stale event corpus-rare)

---

## 1. What it is (one-line)

AutoGPT v59's **dual-licensing structure (MIT for Classic + Forge + sister projects; PolyForm Shield for autogpt_platform/) is the FIRST UN-STALE event for both Pattern #45 Dual-Licensing (35 wikis stale since Unsloth v23) AND Pattern #72 PolyForm-Family-License (26 wikis stale since GitNexus v33) — corpus-rare double un-stale at single wiki.**

## 2. Verbatim license declaration (from README)

> "Polyform Shield License (autogpt_platform folder) and MIT License (everything else)"

> "the Polyform Shield License represents 'our in-development platform' effort, while MIT licensing covers 'the original stand-alone AutoGPT Agent' and related projects"

## 3. License structure post-v59

**Dual-licensing scheme:**

| Surface | License | Type | Restriction |
|---|---|---|---|
| `autogpt_platform/` (NEW Platform) | **PolyForm Shield** | Source-available, non-OSI, standardized-license-family | Permits all uses EXCEPT building competing service |
| `classic/` + Forge + benchmark + frontend | **MIT** | OSI-approved permissive | None |
| Sister projects (GravitasML + Code Ability) | **MIT** | OSI-approved permissive | None |

**License declared on GitHub API:** NOASSERTION (because dual-license is not single SPDX-id; common at multi-license repos).

## 4. PolyForm-Shield characteristics

**PolyForm Shield License** = one of 5 PolyForm Project licenses (Shield + Noncommercial + Internal-Use + Small-Business + Strict).

**Shield-specific restriction:** "permitted to use the software for any purpose other than building a product or service that competes with the licensor's product or service."

**Distinct from PolyForm-Noncommercial (GitNexus v33):** Noncommercial restricts ALL commercial use; Shield permits commercial use UNLESS competing.

**Distinct from SUL (n8n v56 / oh-my-openagent v52):** SUL (Sustainable Use License) restricts hosting-as-service-to-third-parties; Shield restricts competing-product-creation.

## 5. Pattern #45 Dual-Licensing UN-STALE event (corpus-first since v23 — 35 wikis)

**Pattern #45 history:**
- **Registered v23** (Unsloth, 2026-04-XX) — N=1 Apache-2.0 + commercial; STALE-flagged
- **v24-v58** — 35 consecutive wikis with no 2nd dual-licensing observation; STALE
- **UN-STALES at v59** AutoGPT MIT + PolyForm-Shield = N=2 STRUCTURAL across 2 distinct license-pairs + 2 tiers (Unsloth T5 + AutoGPT T1+T5)

**Promotion path at v60 mini-audit:**
- **Criterion 2 structural-N=2 SATISFIED:** 2 structurally-unambiguous dual-licensing observations (Unsloth Apache+commercial + AutoGPT MIT+PolyForm-Shield); each observation criterially clean (open-source-baseline + commercial/source-available-companion)
- **Criterion 1 default ≥3-cross-tier:** PARTIAL (2 tiers: T5 + T1+T5; needs 1 more cross-tier observation for criterion 1)
- **Recommended action at v60:** PROMOTE to CONFIRMED under criterion 2 structural-N=2

**First un-stale event for Pattern #45 in 35 wikis** — second-longest stale-to-un-stale gap in corpus history (after Pattern #42 + #44 un-stale at v30 OpenHands which had 8-wiki gap).

## 6. Pattern #72 PolyForm-Family-License UN-STALE event with RENAME (corpus-first since v33 — 26 wikis)

**Pattern #72 history:**
- **Registered v33** (GitNexus) — N=1 PolyForm-Noncommercial; STALE-flagged
- **v34-v58** — 26 consecutive wikis with no 2nd PolyForm observation; STALE
- **UN-STALES at v59** AutoGPT PolyForm-Shield = N=2 STRUCTURAL across 2 distinct PolyForm-family flavors

**Recommended RENAME at v60 mini-audit:**
- Pattern #72 PolyForm-Noncommercial → **Pattern #72 PolyForm-Family-License** (broader family scope)
- Sub-variants:
  - **72a Noncommercial** (GitNexus v33 — restricts commercial use entirely)
  - **72b Shield** (AutoGPT v59 — restricts competing-product creation only)
- **Criterion 4 variant-within-pattern-at-N=2 SATISFIED** (within renamed parent pattern, 2 sub-variants observed)
- **Recommended action at v60:** RENAME parent + PROMOTE 72a + 72b under criterion 4

**First un-stale event for Pattern #72 in 26 wikis.**

## 7. Pattern #29 non-commercial-restriction-custom-license sub-context grows N=4

**Pre-v59 state:** N=3 promotion-candidate at v60 (omo SUL + GitNexus PolyForm-Noncommercial + n8n SUL across 3 tiers T1+T2+T5).

**Post-v59 state:** **N=4 across 4 distinct tier-instances + 4 distinct license-name-instances** = corpus's most-richly-categorized pattern axis maintained:

| Wiki | Tier | License | Sub-flavor | Restriction-axis |
|---|---|---|---|---|
| GitNexus v33 | T5 | PolyForm-Noncommercial | standardized-non-OSI / noncommercial | commercial-use-entirely |
| oh-my-openagent v52 | T1 | SUL-1.0 | bespoke-non-OSI | hosting-as-service-restricted |
| n8n v56 | T2 | n8n-SUL | bespoke-non-OSI | hosting-as-service-restricted |
| **AutoGPT v59** | **T1+T5** | **PolyForm-Shield** | **standardized-non-OSI / shield** | **competing-product-restricted** |

**NEW sub-sub-axis emerging within Pattern #29 sub-context:**
- **standardized-non-OSI** (GitNexus PolyForm-Noncommercial + AutoGPT PolyForm-Shield) — both PolyForm-family
- **bespoke-non-OSI** (omo SUL-1.0 + n8n SUL) — both Sustainable Use License flavors

2-vs-2 sub-sub-axis emergent at v59 = potential Pattern #29 sub-context refinement at v60 mini-audit.

## 8. Why this matters for Storm Bear vault publishing decision (item v27 #5 carries forward)

**Storm Bear vault publishing strategy** has access to multiple license-precedents post-v59:

| Approach | Restricts | Use-case fit |
|---|---|---|
| **MIT** (most permissive) | Nothing | Storm Bear vault current license; max community + max no-restriction |
| **Apache-2.0 + commercial** (Unsloth-style) | Commercial requires separate license | Dual-licensing for non-commercial-open + commercial-paid revenue model |
| **PolyForm-Noncommercial** (GitNexus-style) | All commercial use | Restricts commercial entirely — NOT FIT for Storm Bear if commercial Scrum-coaching deployment desired |
| **PolyForm-Shield** (AutoGPT-style NEW v59) | Competing product/service only | Permits Scrum-coaching consultation use; restricts only competing-platforms creation. **POTENTIAL FIT for Storm Bear if vault becomes commercializable knowledge-platform** |
| **SUL** (n8n + oh-my-openagent style) | Hosting-as-service to third parties | Restricts third-party hosting; permits internal commercial use. **POTENTIAL FIT for Storm Bear if hosted-vault-as-service is commercializable surface** |

**v59 recommendation for v27 HIGH bundle item #5 (vault license decision):** MIT remains current default; PolyForm-Shield emerges as 2nd-most-considerable option if vault becomes commercializable competing-knowledge-platform-blocker desired (e.g., if Storm Bear monetizes brain-setup-v2 + skills-collection at scale).

## 9. Pattern Library promotion-candidate summary at v60 mini-audit

**LARGEST mini-audit projected in corpus history** (12+ items vs prior maxima ~6):

1. Pattern #57 57c formal extension N=8 + 57c-anti-pattern-foil sub-variant (post-v58)
2. Pattern #18 Layer 1 STRONGEST 30+ tools formal extension (post-v58)
3. Pattern #19 org-level-pseudonymity sub-variant (post-v58)
4. Pattern #51 anti-vibe pole 2-consecutive-wikis observational (post-v58)
5. Pattern #52 OBSERVATIONAL FLAG time-axis verification (carried from v57)
6. Process-owning-meta-frameworks observation-track candidate (deferred)
7. Phase 0.9 STRICT-amendment N=4 emergent STRICT-triad pattern + 1st disciplined-skip documentation (v59 NEW)
8. **Pattern #45 Dual-Licensing PROMOTION** under structural-N=2 (v59 NEW)
9. **Pattern #72 PolyForm-Family-License rename + variant-within-pattern-at-N=2 PROMOTION** (v59 NEW)
10. **Pattern #19 founder-personal → org-stewardship sub-variant N=2 promotion candidate** (v59 NEW)
11. **Pattern #27 community-viral corpus-historical-foundational sub-observation** documentation (v59 NEW)
12. **Pattern #69 EXTREME-tier formal-statement-extension to N=7** (v59 NEW)

**Projected ratio improvement at v60 mini-audit:** 0.436:1 → ~0.30-0.35:1 (3-5 promotions; 0-2 retirements).

## 10. Cross-references to siblings

- **Unsloth v23** — Pattern #45 N=1 precedent (Apache-2.0 + commercial)
- **GitNexus v33** — Pattern #72 PolyForm-Noncommercial N=1 precedent
- **omo v52** — Pattern #29 sub-context SUL bespoke-non-OSI
- **n8n v56** — Pattern #29 sub-context n8n-SUL bespoke-non-OSI

## 11. Pattern Library impact summary

5 patterns directly impacted at v59 by this entity alone:
- #45 UN-STALES + promotion-candidate v60
- #72 UN-STALES + RENAME + promotion-candidate v60
- #29 sub-context grows N=4 + NEW sub-sub-axis standardized-vs-bespoke
- Pattern #19 reinforces founder-to-org sub-variant N=2 (also touched)
- Pattern #27 corpus-historical-foundational data point (also touched)

## 12. Open questions

- See Q1-3 (license-axis questions): PolyForm-Shield-vs-Noncommercial flavor distinctions; AutoGPT licensing history; Storm Bear-business-PolyForm-Shield compatibility decision

## 13. Storm Bear pilot relevance

**HIGH for license-axis pattern-vocabulary contribution** — adds structural-axis vocabulary to Storm Bear's vault license-decision toolkit (item v27 #5).

**MEDIUM-LOW for direct deployment** pending license-acceptability decision (PolyForm-Shield doesn't block Scrum-coaching consultation but needs explicit OK).

**Specific recommendation:** include PolyForm-Shield as 2nd-most-considered license option for Storm Bear vault publishing decision (after current MIT default).
