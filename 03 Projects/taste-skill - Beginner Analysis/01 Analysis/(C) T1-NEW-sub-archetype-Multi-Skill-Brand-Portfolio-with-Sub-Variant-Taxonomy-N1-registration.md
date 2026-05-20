# (C) Phase 4b PRIMARY proposal — NEW T1 sub-archetype "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" PROVISIONAL N=1 registration

**Wiki**: v81 (`Leonxlnx/taste-skill`)
**Date**: 2026-05-20
**Routine**: `llm-wiki-routine-v2.2` (seventeenth execution)
**Confidence verdict**: **MEDIUM** (revised 2026-05-20 — see §10 self-review)
**Proposal type**: NEW T1 sub-archetype registration at PROVISIONAL N=1; promotion-eligibility-window v85-v90.

---

## 1. Sub-archetype definition (provisional)

A **T1 Assistant Skill bundle** structured as N distinct skills (typically **8-15**), each addressing a specific design/aesthetic-preference or workflow-sub-mode, unified by:

1. **Single brand identity** — one author/maintainer, one brand name, optional custom-domain investment.
2. **Setting-based spectrum-control mechanism** — shared dimensional axes (layout / motion / density / typography) with per-skill positions on those axes.
3. **Portable multi-harness installation** — packaged for `npx skills add` or equivalent skill-CLI install vectors across multiple AI harness ecosystems.
4. **Sub-variant taxonomy decomposable along orthogonal axes** — the N skills are not arbitrary; they partition cleanly along 2-4 axes (aesthetic × workflow × platform-extension being the v81 case).

**Tier**: T1 Assistant Skill / design-language (existing tier).

**Distinct from**: T1 Single-Skill Multi-Target Distribution (v75 impeccable canonical anchor).

---

## 2. Empirical evidence from v81 taste-skill

### 12-skill 3-axis decomposition

```
Axis A — Aesthetic-variants (4 skills):
  taste-skill (base) · minimalist-skill · brutalist-skill · soft-skill

Axis B — Workflow-variants (4 skills):
  redesign-skill · image-to-code-skill · output-skill · stitch-skill

Axis C — Platform/extension-variants (4 skills):
  gpt-tasteskill · imagegen-frontend-web · imagegen-frontend-mobile · brandkit
```

**4 + 4 + 4 = 12 = clean tri-axis partitioning** = non-arbitrary architectural choice.

### Brand identity unity

- Single author (Leon Lin / Leonxlnx).
- Single brand name ("taste-skill" / "Anti-Slop Frontend Framework").
- Custom domain (`tasteskill.dev`) brand-investment surface.
- Unified design-philosophy (anti-slop curation overlay).

### Setting-spectrum mechanism

README explicit dimensional controls:
- *"Layout experimentation (lower: centered/clean · higher: asymmetric/modern)"*
- *"Motion ranges from hover to scroll/magnetic"*

Spectrum granularity (continuous vs discrete vs verbal) unverified at Phase 0 — does NOT affect sub-archetype validity (mechanism exists; granularity is implementation-detail).

### Multi-harness install vector

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "<skill-name>"
```

4-harness ecosystem (Claude Code + Codex + Cursor + ChatGPT Images).

### Validation signal

- 18,264 stars at 90 days = 202.93 stars/day Pattern #52 N=4 HIGH-NOT-EXTREME band.
- 1,560 forks / 92 watchers / 14 open issues / push activity within recent window.
- 8 named GitHub Sponsors = modest community-funding base validating positioning.

---

## 3. Distinction from prior T1 corpus subjects (retrospective descriptions)

**Honest framing**: There is **no formal T1 sub-archetype taxonomy** currently registered in the Pattern Library — unlike T5 (9 sub-archetypes) or Pattern #18 (shared-backend-service sub-archetype with B1/B2/B3 protocol-variants). The names below are **retrospective descriptions** of prior T1 wikis used as comparative landmarks, not registered sub-archetypes. v81 is proposed as the **FIRST formally-registered T1 sub-archetype**.

| Prior T1 subject (retrospective description) | Anchor | Distinct from v81 because |
|---|---|---|
| Design-language single-skill multi-target | v75 impeccable | Skill count: 1 vs 12; multiplicity at distribution layer vs content layer = **DIRECT architectural inversion** |
| Standards-codification skill catalog | v76 agent-skills-standard | Intent = codification + token-efficiency (259 skills × 20+ frameworks); not a brand-aesthetic-portfolio |
| Reverse-engineering reference archive | v65 claude-code-system-prompts | Intent = reference/archive; not a deployable skill bundle |
| Multi-harness operator-system at velocity | v78 ECC | Operator-system scale (60 agents + 232 skills + 75 commands); not a focused design-skill bundle |
| Provider-agnostic agentic framework | v71 agents-best-practices | Reference + methodology framework; single-skill not multi-skill bundle |

**Architectural inversion with v75 = the sharpest distinction** — both T1 / design-language but inverted at multiplicity-layer (v75 = 1 skill × 14 harnesses; v81 = 12 skills × ~4 harnesses).

**Tier-distinct comparators** (acknowledged outside T1 scope, listed for completeness): v66 agentmemory (T2), v74 LLMs-from-scratch (T3), v68 zero (T1 programming-language-as-agent-substrate sub-archetype PROVISIONAL N=1 from v68).

---

## 4. Promotion-criteria checklist

| Criterion | v81 status | Verdict |
|---|---|---|
| **(1) Corpus-first** | Multi-skill-brand-portfolio at T1 / design-language tier — no prior corpus subject matches at multiplicity-layer-of-content | **PASS** |
| **(2) Distinct from prior T1 subjects** | 5 prior T1 retrospective comparators all distinct (see §3) — sharpest distinction = v75 inversion | **PASS** |
| **(3) Mechanism articulable** | 4-property definition (brand-unity + setting-spectrum + portable-install + sub-variant-taxonomy) | **PASS with caveat** — only property #4 (sub-variant taxonomy across ≥8 skills) is fully distinguishing vs v75; properties #1-3 are partially shared. Tighter definition: "T1 design-language skill bundle with N ≥ 8 distinct skills decomposable along orthogonal axes under unified brand." |
| **(4) Variant-within-pattern** | 3 axes × 4 skills internal decomposition = sub-variant taxonomy within the sub-archetype | **STRETCH** — Pattern Library convention typically applies criterion 4 to **cross-instance variation (N=2+)**, not within-instance internal variation. Honest reading: criterion 4 is a stretch interpretation at N=1; may not survive v85 audit. |
| **(5) Confidence verdict** | 4/5 criteria PASS + 1 STRETCH (criterion 4) + 12-skill partition has ≥2 outlier-risks (soft-skill axis-A placement + brandkit axis-C placement both unverified at Phase 0) | **MEDIUM** |

**Verdict**: PROVISIONAL N=1 registration eligible at **MEDIUM confidence**. The architectural-inversion-with-v75 framing is the load-bearing claim; the criterion-4 PASS and clean-tri-axis cleanness are weaker and may be downgraded at v85 audit.

---

## 5. Promotion path / audit schedule

### Audit-cycle window

- **v82-v84**: passive monitoring for N=2 candidates (any new multi-skill-brand-portfolio with clean axis decomposition + brand-identity unity + custom-domain or equivalent brand-investment).
- **v85 audit**: first formal N=2 evaluation. Outcomes:
  - **N=2 present** → PROMOTE to confirmed sub-archetype with 2-instance basis.
  - **N=2 absent** → continue PROVISIONAL N=1.
- **v90 audit**: terminal decision. Outcomes:
  - **N=2 still present** → confirmed (delayed promotion).
  - **N=2 absent → RETIRE as singular-anchor sub-archetype** (or KEEP as PROVISIONAL if exceptional evidence justifies).

### N=2 candidate signal (what to watch for)

Future corpus subject matching ALL of:
- T1 Assistant Skill / design-language tier (or analogous design-discipline-skill tier).
- ≥8 distinct skill folders / artifact-units under single brand.
- Clean axis decomposition (2-4 orthogonal axes; not arbitrary).
- Multi-harness install vector (Claude Code + Codex + Cursor + others).
- Brand-investment signal (custom domain OR equivalent dedicated marketing surface).
- Optional: setting-spectrum or analogous shared mechanism across skills.

---

## 6. Related Pattern Library candidates registered alongside v81

### Pattern #19 NEW sub-mechanism 19l candidate

**"Munich-Solo-Founder-with-Multi-Skill-Design-Brand-Portfolio"**:
- Geography: Munich.
- Profile: solo-developer + 104-repo portfolio + 819 followers + GitHub Sponsors + custom-domain brand-investment.
- Output mode: multi-skill design-brand portfolio.
- Distinct from 19a-19k existing sub-mechanisms.
- PROVISIONAL N=1; same v85-v90 promotion window as the T1 sub-archetype.

### Anti-Slop-Design-Curation observation track (framing revised)

**Framing decision**: NOT a Pattern #51 sub-pole. Pattern #51 axis is vibe-coding-spectrum (PRO-VIBE-explicit ↔ Anti-vibe-with-pragmatic-acknowledgment). Anti-slop is **orthogonal** to that axis — it positions on design-aesthetic-quality dimension, not on vibe-coding-discipline dimension. Registering it as a Pattern #51 sub-pole would conflate axes.

**Revised registration**: NEW observation track candidate "Anti-Slop-Design-Curation as design-aesthetic-quality positioning" PROVISIONAL N=1. Distinct dimension from Pattern #51's vibe-coding-spectrum. If N=2 sustains in v82-v90 window, evaluate as candidate for separate Pattern OR as Library-vocabulary item OR as Pattern #51 axis-expansion (with explicit axis-rename to encompass both dimensions). Currently tracked at OC layer only.

### Library-vocabulary item #12 `llms.txt` N=2 STRENGTHENING

- v77 easy-vibe PROVISIONAL N=1 (curriculum-stage-router role) → v81 taste-skill N=2 (skill-bundle-router role).
- PROMOTION-ELIGIBLE at v85 audit.
- **Honest N-count**: 2 instances of `llms.txt` artifact specifically (v77 + v81). v75 `HARNESSES.md` + v76 `AGENTS.md` are **different artifact types** — they belong to a separate (yet-unregistered) "LLM-routing-artifact" meta-category, NOT to item #12's `llms.txt` taxonomy. Prior wiki narrative conflated these; this proposal counts honest N=2 for item #12.
- Separate observation candidate: "LLM-routing-artifact meta-category" (4-instance evidence across `HARNESSES.md` + `AGENTS.md` + `llms.txt` × 2) — currently tracked at OC layer only; not part of item #12.

---

## 7. Risks / contraindications to registration

1. **Soft-skill outlier risk** — if `soft-skill` doesn't fit the 4-skill Axis A aesthetic-variant partition (e.g., if it's actually a workflow-variant or a meta-utility), the clean 4+4+4 partitioning weakens. Mitigation: Phase 4 SKILL.md spot-check during follow-up wiki maintenance.
2. **Single-anchor risk** — N=1 registrations face terminal-audit retire OR sustain decision. Historical retire-rate not quantified in available state-history; flag for v85 audit retrospective analysis. v81 has MEDIUM (not HIGH) confidence verdict and 2 documented partition-risks; auditor should weight retire-risk accordingly.
3. **v75 sub-archetype overlap risk** — if v75's "Single-Skill Multi-Target Distribution" sub-archetype is later expanded to include "multi-skill" variants, the v81 sub-archetype could be retroactively absorbed. Mitigation: explicit multiplicity-layer distinction maintained in audit records.
4. **Promotion-criteria criterion 4 ambiguity** — "variant-within-pattern" applies to the 3-axis × 4-skills internal decomposition, but it could be argued this is sub-variant taxonomy not pattern-variants. Mitigation: criterion 4 PASS reasoning explicitly cited in v85 audit record.

---

## 8. Decision rationale (operator-visible)

**Why register NEW sub-archetype rather than mark v81 as v75-strengthening?**

- v75 ↔ v81 share **tier** (T1) and **domain** (design-language) but **invert** at multiplicity-layer.
- Treating v81 as v75-strengthening would lose the architectural distinction.
- T1 / design-language tier is **architecturally rich enough** to host multiple sub-archetypes (existing precedent: T2 service tier hosts shared-backend-service + platform-primitive + others).
- Registration cost is low (PROVISIONAL N=1 + v85-v90 audit-cycle window).
- Promotion path is explicit (N=2 in v85-v90 window) and retire path is explicit (N=2 absent terminal).

**Recommendation**: REGISTER as PROVISIONAL N=1 with **MEDIUM** confidence verdict. The architectural-inversion-with-v75 framing is the load-bearing claim; criterion 4 PASS and partition cleanness are weaker. Proceed to Phase 5 iteration log + Phase 6 vault-sync with this proposal as a Pattern Library state-transition input.

---

## 9. Cross-references

- **Cluster 2**: `02 Wiki/(C) cluster-2-12-skill-inventory.md` — 12-skill folder enumeration + 3-axis decomposition evidence.
- **Entity 1**: `02 Wiki/(C) entity-1-core-product-12-skill-bundle.md` — operational + architectural framing.
- **Entity 3**: `02 Wiki/(C) entity-3-pattern-T1-multi-skill-brand-portfolio-sub-archetype.md` — sub-archetype-scoped entity page.
- **Entity 4**: `02 Wiki/(C) entity-4-storm-bear-meta-plus-pattern-implications.md` — Pattern Library state-transition package.
- **CLAUDE.md**: project-root file — Phase 0 classification snapshot + pre-registered PRIMARY proposal anchor.
- **v75 impeccable Phase 4b proposal**: `03 Projects/impeccable - Beginner Analysis/01 Analysis/(C) Pattern-84-84c-N4-strengthening-CORPUS-RECORD-14-harness-multi-target-distribution.md` (direct-sister wiki PRIMARY for reference).

---

## 10. Self-review record (2026-05-20 post-Phase-6)

After Phase 6 vault-sync, this proposal was self-reviewed per operator request. Five substantive corrections applied in tightening pass:

1. **Verdict downgrade HIGH → MEDIUM** (§4 + frontmatter + §8) — original HIGH overclaimed; criterion-4 stretch + 2 partition outlier-risks justify MEDIUM.
2. **§3 comparison table reframed** — original implied 6 formally-registered T1 sub-archetypes; honest framing is that **no formal T1 sub-archetype taxonomy exists yet**, the names were retrospective descriptions. v81 is proposed as the FIRST formally-registered T1 sub-archetype, which strengthens (not weakens) the proposal.
3. **Pattern #51 sub-pole framing dropped** — anti-slop is orthogonal to vibe-coding-spectrum axis; demoted to separate observation track candidate at OC layer (§6). NOT a Pattern #51 sub-pole.
4. **Library-vocab #12 N-count corrected** — honest N=2 (v77 + v81 `llms.txt` only); HARNESSES.md + AGENTS.md are different artifact types and belong to a separate "LLM-routing-artifact" meta-category track, not item #12.
5. **30% retire-rate stat removed** — was unsourced; replaced with audit-retrospective flag (§7 risk #2).

The architectural-inversion-with-v75 framing survives intact and remains the load-bearing claim. Surrounding scaffolding tightened to match.
