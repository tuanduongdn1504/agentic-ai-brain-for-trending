# Phase 4b deliverable — Pattern #21 SDD Methodology Emergence: un-stale + promotion case at v61

> **Routing mode (primary):** Un-stale mechanism applied to Pattern #21 SDD Methodology Emergence
> **Routing mode (secondary):** Cross-archetype N=4 evidence + structural-unambiguity-at-N=2 criterion + counter-evidence to v60 audit lineage-rejection
> **Subject:** [`gotalab/cc-sdd`](https://github.com/gotalab/cc-sdd) — wiki v61
> **Date:** 2026-05-07
> **Audience:** Storm Bear vault operator preparing for next mini-audit (v63 natural cadence)

---

## TL;DR

**Pattern #21 SDD Methodology Emergence has been STALE-CANDIDATE since v25 audit (8 wikis past v17 spec-kit with no new SDD-centered framework).** Promotion criterion: *"1+ more framework centering Spec-Driven Development, ideally at different tier"* with re-evaluation flagged for *"v30 OR if SDD framework emerges at T2-T5"*. v60 mini-audit (2026-05-07) explicitly considered un-staling via gsd-2 v54 → REJECTED on lineage-grounds (gsd-2 = same lineage as GSD v5; aidevops v47 verified NOT SDD-centered).

**cc-sdd v61 satisfies the un-stale criterion v60 audit blocked**: independent organization (gotalab solo-Japanese) + independent author + independent intellectual lineage (Kiro IDE — first external-IDE methodology lineage in corpus). When OpenSpec v58 (Fission-AI pseudonymous-org SDD framework) is also accounted for (currently missing from Pattern #21 evidence list — fact-verification gap from v58 build → v60 audit), the corpus has **N=4 independent SDD-centered T1 frameworks across 4 distinct organizational archetypes**.

**Recommendation for next mini-audit:** UN-STALE Pattern #21 + promote under criterion #2 structural-unambiguity-at-N=2 with formal-statement extension. Cross-tier criterion #1 cannot yet be satisfied (all 4 T1) — preserves cross-tier promotion option for future v62+ wiki if T2-T5 SDD framework emerges.

---

## 1. Pattern #21 current state

From `_patterns/03-active-candidates.md` lines 17-22:

> **#21 SDD Methodology Emergence** — STALE-CANDIDATE (flagged v25 audit)
> **Status at v25 audit:** Flagged STALE-CANDIDATE — N=2 single-tier (both T1) after 8 wikis since v17 spec-kit. Mini-audit v22 flagged approaching stale; full audit v25 confirms.
> **Evidence:** GSD v5 (feature-level) + spec-kit v17 (whole methodology).
> **Required for promotion:** 1+ more framework centering Spec-Driven Development, ideally at different tier.
> **Re-evaluation:** at v30 OR if spec-driven framework emerges at T2-T5.
> **Rationale:** v18-v25 corpus additions (8 wikis) had zero new SDD-centered frameworks. May be T1-specific or zeitgeist-timed phenomenon past peak.

From v60 mini-audit results (`_patterns/05-recent-additions.md` line 58):

> **Pattern #21 SDD Methodology Emergence UN-STALE candidate → REJECTED (DEFER)** — Fact-verification correction caught v54 agent overstatement: aidevops v47 verified NOT SDD-centered (entity page explicit "Not a methodology framework ≠ spec-kit v17 SDD / BMAD v11 BMM / GSD v5"); gsd-2 v54 is GSD v5 successor (same gsd-build org, same-lineage). Cross-org count corrected from claimed N=4 → actual N=2 (gsd-build with 2 wikis + GitHub/Microsoft with 1); all T1. Stale-flag criterion "Required for promotion: 1+ more framework centering Spec-Driven Development, ideally at different tier" NOT met. **STAYS STALE-CANDIDATE.** Re-evaluate at v60+ wiki OR if independent SDD-centered framework emerges at T2-T5.

**Gap noted:** v60 mini-audit re-evaluation language says "v60+ wiki OR if independent SDD-centered framework emerges at T2-T5" — explicitly leaves open re-evaluation by INDEPENDENT framework (not requiring T2-T5). This is what cc-sdd v61 provides.

---

## 2. cc-sdd v61 evidence — independence verification

### 2.1 Organization independence

| Test | cc-sdd v61 result |
|---|---|
| Same org as gsd-build (GSD v5 / gsd-2 v54)? | ❌ NO — gotalab solo-Japanese, not gsd-build |
| Same org as Microsoft / GitHub (spec-kit v17)? | ❌ NO — solo-Japanese, not corporate |
| Same org as Fission-AI (OpenSpec v58)? | ❌ NO — gotalab solo-attribution, not pseudonymous-org |
| Independent organization? | ✅ **YES** — gotalab is structurally distinct from all prior corpus SDD orgs |

### 2.2 Author independence

| Test | cc-sdd v61 result |
|---|---|
| Same author as GSD v5 / gsd-2 v54? | ❌ NO |
| Same author as spec-kit v17? | ❌ NO |
| Same author as OpenSpec v58? | ❌ NO (Fission-AI is pseudonymous-org with hidden members) |
| Independent author? | ✅ **YES** — gotalab is independent solo-Japanese author |

### 2.3 Intellectual lineage independence

| Test | cc-sdd v61 result |
|---|---|
| Same lineage as GSD (feature-shaped SDD)? | ❌ NO — cc-sdd uses 6-step workflow with discovery routing, not feature-level shape |
| Same lineage as spec-kit (9-article constitution)? | ❌ NO — cc-sdd has 3 explicit human-approval gates, not constitution-gates |
| Same lineage as OpenSpec (per-tool format translation)? | ❌ NO — cc-sdd is Skills-mode primary with adversarial review, not per-tool format adapter |
| Independent intellectual lineage? | ✅ **YES** — cc-sdd has Kiro IDE methodology lineage (corpus-first external-IDE lineage; not previously observed) |

### 2.4 SDD-centeredness verification

| Test | cc-sdd v61 result |
|---|---|
| Specifications as core artifact? | ✅ YES — `requirements.md` / `design.md` / `tasks.md` |
| Spec-first workflow? | ✅ YES — 6-step workflow with discovery → spec-init → requirements → design → tasks → impl |
| Boundary-first design? | ✅ YES — explicit Boundary markers per-task; File Structure Plan in design.md |
| Contract semantics? | ✅ YES — *"specifications as contracts between system components rather than top-down commands"* |
| Architecture-as-foundation? | ✅ YES (corpus-first explicit acknowledgment) — *"writing more specs will not create independence"* without architecture |
| EARS-format requirements? | ✅ YES (corpus-first explicit EARS reference) |
| Methodology-shaped (not feature-shaped)? | ✅ YES — full SDD methodology with Skills harness implementation |

**Conclusion: cc-sdd v61 is structurally and semantically a full SDD-centered framework, independent of prior 3 corpus SDD framework lineages.**

---

## 3. N=4 cross-archetype evidence (post-v61)

### 3.1 4 independent SDD-centered T1 frameworks in corpus

| Wiki | Framework | Org archetype | Key methodology features |
|---|---|---|---|
| v5 | get-shit-done (GSD) | Solo-product-line (gsd-build) | feature-shaped SDD |
| v17 | spec-kit | Corporate (Microsoft / GitHub) | 9-article constitution + 80+ marketplace + AI-disclosure policy |
| v54 | gsd-2 | Solo-product-line (gsd-build, GSD successor) | feature-shaped SDD continuation [SAME LINEAGE as v5] |
| v58 | OpenSpec | Pseudonymous-org (Fission-AI) | per-tool format translation 30+ tools |
| **v61** | **cc-sdd** | **Solo-Japanese (gotalab)** | **Multi-platform Skills harness + Kiro IDE lineage + adversarial review** |

**Distinct organizational archetypes (collapsing same-lineage):**
1. **Solo-product-line** (gsd-build with v5 + v54) — 1 lineage / 2 wikis
2. **Corporate official** (Microsoft / GitHub with v17) — 1 lineage / 1 wiki
3. **Pseudonymous-org** (Fission-AI with v58) — 1 lineage / 1 wiki
4. **Solo-international (Japanese)** (gotalab with v61) — 1 lineage / 1 wiki ← NEW

### 3.2 Fact-verification gap noted

`_patterns/03-active-candidates.md` Pattern #21 evidence list currently shows:
> **Evidence:** GSD v5 (feature-level) + spec-kit v17 (whole methodology).

This is the v25-audit-era evidence list, not updated post-OpenSpec v58. **Fact-verification gap to address at next mini-audit:** OpenSpec v58 should be added to Pattern #21 evidence list as N=3 observation (independent of GSD/spec-kit).

cc-sdd v61 then becomes N=4 observation.

### 3.3 Cross-tier observation

All 4 frameworks remain T1 currently. Pattern #21 v25-audit promotion criterion was *"ideally at different tier"* — preference, not gate.

**Cross-tier observation pending:** Pattern #21 default-criterion #1 (≥3 observations across 2+ tiers) cannot yet be satisfied. Promotion via criterion #1 deferred until T2-T5 SDD framework appears in corpus.

---

## 4. Promotion path analysis (5 structural-promotion criteria)

Per routine v2.1 §"5 structural-promotion criteria":

### 4.1 Criterion #1 — Default ≥3 observations across 2+ tiers

**Status: FAIL** — all 4 SDD frameworks are T1.

**Path forward:** Wait for T2-T5 SDD framework to emerge in corpus. v62+ corpus monitoring item.

### 4.2 Criterion #2 — Structural-unambiguity-at-N=2

**Status: PASS** — 4 frameworks are structurally unambiguous SDD-centered (per §2.4 verification table). Each observation is criterially clean — no ambiguity about whether subject is SDD-framework.

**Path forward:** **PROMOTE under criterion #2 at next mini-audit.** Formal-statement extension to clarify: "SDD methodology meta-pattern operates across organizational archetypes (solo-product-line + corporate + pseudonymous-org + solo-international) at T1 currently; cross-tier expansion pending T2-T5 SDD framework emergence."

### 4.3 Criterion #3 — Spectrum-pattern-at-N=2

**Status: N/A** — Pattern #21 is not a spectrum pattern.

### 4.4 Criterion #4 — Variant-within-pattern-at-N=2

**Status: N/A** — Pattern #21 is methodology-emergence pattern, not a variant of confirmed pattern (would be promotion to standalone confirmed, not variant within parent).

### 4.5 Criterion #5 — Meta-pattern-at-N=3-consolidation

**Status: PASS-eligible** — could promote if Pattern #21 reformulated as meta-pattern wrapping sub-archetypes.

**Path forward:** ALTERNATIVE to criterion #2 promotion. If chosen, would consolidate observations into meta-pattern formulation:
- Sub-archetype 1: Feature-shaped SDD (GSD v5 / gsd-2 v54)
- Sub-archetype 2: Constitution-shaped SDD (spec-kit v17)
- Sub-archetype 3: Per-tool-format-translation SDD (OpenSpec v58)
- Sub-archetype 4: Multi-platform-Skills-harness SDD (cc-sdd v61)

Trade-off: meta-pattern formulation may over-fit current 4 observations. Criterion #2 promotion is cleaner.

**RECOMMENDATION: Promote under criterion #2 (structural-unambiguity-at-N=2) at next mini-audit.** Reserve criterion #5 meta-pattern consolidation for future audit if 6+ SDD frameworks accumulate with clearer sub-archetype distinctions.

---

## 5. Counter-evidence to v60 audit lineage-rejection

v60 mini-audit (2026-05-07) explicitly considered Pattern #21 un-stale and rejected:

> Cross-org count corrected from claimed N=4 → actual N=2 (gsd-build with 2 wikis + GitHub/Microsoft with 1); all T1. Stale-flag criterion "Required for promotion: 1+ more framework centering Spec-Driven Development, ideally at different tier" NOT met. **STAYS STALE-CANDIDATE.**

The v60 audit was correct on its evidence (gsd-2 = same lineage, aidevops not SDD-centered). cc-sdd v61 adds the missing piece: an **independent organization + independent author + independent intellectual lineage** SDD-centered framework.

**Validation of v60 audit discipline:**
- v60 audit lineage-test correctly held the line — preventing fabricated cross-org count
- v61 brings genuinely independent evidence — satisfying the criterion v60 audit blocked
- This is exactly the corpus health-loop working: audit discipline + subsequent evidence resolution

**Routine v2.2 candidate codification:** "When un-stale candidate fails lineage-test, also evaluate independence-test on subsequent wikis before staying stale indefinitely. Lineage-test rejection should not preclude un-stale by independent observation; document the bar (independent org + independent author + independent intellectual lineage) clearly so subsequent observations can be evaluated against it."

---

## 6. Mini-audit checklist (for v63 natural cadence)

Items for next mini-audit re Pattern #21:

- [ ] **Add OpenSpec v58 to Pattern #21 evidence list** (fact-verification gap from v58 build → v60 audit; should be evidence list update independent of v61 work)
- [ ] **Add cc-sdd v61 to Pattern #21 evidence list** (new observation; independent of all prior 3 lineages)
- [ ] **Un-stale Pattern #21** (criterion satisfied: 1+ more framework centering SDD, independent organization + author + intellectual lineage)
- [ ] **Promote Pattern #21 under criterion #2 structural-unambiguity-at-N=2** (4 observations criterially clean SDD-centered)
- [ ] **Update formal statement** to acknowledge T1-currently / cross-tier-pending and 4-archetype distribution
- [ ] **Document Storm Bear meta-archetype reflection:** vault is solo-VN; cc-sdd shows solo-international (Japanese) successfully implementing methodology; broadens Pattern #55 archetype family
- [ ] **Codify routine v2.2 candidate:** lineage-test vs independence-test ordering for un-stale evaluation
- [ ] **Codify routine v2.2 candidate:** EARS-format-requirements as Pattern Library candidate watch (N=1 stale-flagged at v61)
- [ ] **Codify routine v2.2 candidate:** External-IDE-methodology lineage type as observation watch (N=1 stale-flagged at v61)

---

## 7. Adjacent Pattern Library updates this wiki contributes (not Pattern #21 directly)

### 7.1 Pattern #18 protocol-translation Layer 2 sub-archetype

**Candidate registration:** "agent-platform-format-translation-installer" — install-time per-platform skill format translation (cc-sdd 8 platforms; distinct from v60 free-claude-code 6-provider runtime API protocol translation and v58 OpenSpec 30+ tools per-tool format translation).

**Status:** N=1 candidate at v61. Stale-flag at registration per N=1 stale-risk discipline. Re-evaluate at v66/v71.

**Overlap pre-check:** vs OpenSpec v58 mechanism — different timing (install-time vs ?), different platform count (8 vs 30+), different maturity-tier-distribution (mixed vs flat). <70% overlap; can register as separate sub-archetype.

### 7.2 Pattern #51 Vibe-Coding spectrum NUANCE

**Counter-evidence:** cc-sdd is anti-vibe BUT explicitly acknowledges vibe-coding's legitimate use cases ("/kiro-discovery can legitimately conclude that no specification is needed"; "If the discipline feels like overhead, your specs are probably too big").

**Action:** Counter-evidence-driven refinement candidate. Narrows Pattern #51's anti-vibe pole formulation to "anti-vibe-with-pragmatic-acknowledgment" sub-pole; pure-anti-vibe remains spec-kit v17 reference observation.

### 7.3 Pattern #55 solo-regional T1 archetype Japan extension

**Strengthening:** Japan added as 4th regional archetype:
- Solo-VN (codymaster v12 — Pattern #55 N=1 original VN focus)
- Solo-CN (TrendRadar v19 — multi-tier)
- Solo-Korean (OMC v27 — Pattern #55 N=1 Korean)
- **Solo-Japanese (cc-sdd v61 — gotalab) ← NEW**

**Action:** Consider promoting Pattern #55 from Korean-specific to **solo-East-Asian-individual meta-archetype** at next mini-audit, OR keep per-region distinct and add Japan as separate sub-pattern.

### 7.4 Pattern #19 first-mover-authority-without-lineage strengthening

**Strengthening:** gotalab has 4-product ecosystem-portfolio (cc-sdd + skillport + uxaudit + claude-code-marimo) all in Claude Code / Agent Skills space. Strengthens N=2 first-mover-authority observation from v60 (utility-tool sub-type).

**Action:** Pattern #19 already CONFIRMED; cc-sdd evidence reinforces ecosystem-portfolio sub-variant at N=2+.

### 7.5 Pattern #57 polarity (NO contribution)

**Status:** cc-sdd does NOT explicitly cite spec-kit / OpenSpec / GSD by name. Conservative-attribution does NOT apply (no citing-subject foil-style critique or positive-comparison-parallel of corpus subjects).

**Action:** No 57 contribution at v61. Pattern #57 family unchanged.

### 7.6 Pattern #22c AGENTS.md ↔ CLAUDE.md duplication observation

**Observation:** cc-sdd ships both AGENTS.md and CLAUDE.md (project root) with high content overlap. Does NOT include the explicit-sync-comment-header observed in v60 free-claude-code (corpus-first there).

**Action:** Pattern #22c remains N=1 explicit-sync-comment-header (v60 free-claude-code only); cc-sdd v61 is "natural-no-sync-comment" observation — N=1 evidence on the absent-sync-comment side. No promotion needed; just observation point.

---

## 8. Cross-references (for audit reviewer)

**Pattern Library state files:**
- `_patterns/03-active-candidates.md` (Pattern #21 evidence list; Pattern #18 candidates)
- `_patterns/02b-confirmed-patterns-v42-plus.md` (Pattern #51 spectrum; Pattern #55 archetype)
- `_patterns/05-recent-additions.md` (v60 mini-audit results re Pattern #21 rejection)
- `_patterns/01-audit-history.md` (audit cadence + criteria reform history)

**Sibling SDD wikis:**
- v5 GSD entity files
- v17 spec-kit entity files
- v54 gsd-2 entity files
- v58 OpenSpec entity files
- v61 cc-sdd entity files (this wiki — `02 Wiki/(C) cc-sdd entity.md`)

**Routine v2.1 reference:**
- `05 Skills/llm-wiki-routine-v2.1.md` — 5 structural-promotion criteria (§"5 structural-promotion criteria (v2.1 consolidated)")
- `05 Skills/llm-wiki-routine-v2.1.md` — Mini-audit protocol (§"Mini-audit protocol (NEW in v2.1)")
- `05 Skills/llm-wiki-routine-v2.1.md` — Audit cadence reform (§"Audit cadence reform (v2.1 — replaces v2 >1:1 trigger)")

---

## 9. Storm Bear vault decision context

**Vault state at v61 (per CLAUDE.md root):**
- Confirmed patterns: 41 (post-v60 audit)
- Active candidates: 17
- Stale candidates: 1 (Pattern #52 only)
- Ratio: 0.415:1 (largest buffer in corpus history; well below 0.95:1 mini-audit trigger)
- Streaks: 24-consecutive ZERO-NEW-ACTIVE-CANDIDATES; Storm Bear meta-entity 2-consecutive (post-v60 RESTART)

**v61 wiki impact (projected):**
- Confirmed: 41 → 41 (no promotions at wiki-ship; promotion deferred to next mini-audit)
- Active candidates: 17 → 18-19 (Pattern #18 Layer 2 sub-archetype + potentially EARS / external-IDE-lineage candidates)
- Stale: 1 → 0 (potential — if Pattern #21 un-stales at next mini-audit)
- Ratio: 0.415:1 → ~0.44:1 (still well below trigger)

**v63 mini-audit projected impact (if recommendations adopted):**
- Confirmed: 41 → 42 (Pattern #21 promoted)
- Active candidates: 18-19 → 18-19 (Pattern #21 moves from active+stale to confirmed; new candidates remain)
- Stale: 0 → 0
- Ratio: 0.44:1 → 0.43:1 (improved)

**Pilot ranking decision context:**
- cc-sdd v61 enters HIGH-OPERATIONAL pilot list (top-3 alongside free-claude-code v60)
- Both pilots orthogonal layers (proxy vs methodology) — viable simultaneous pilots
- Vault operator decision: pilot cc-sdd before next mini-audit (would inform Storm Bear meta-entity Phase 0.9 evidence on direct-deployment criterion (b))

---

## 10. Final recommendation

**For next mini-audit (v63 natural cadence per pre-registered v60 audit triggers):**

1. **Update Pattern #21 evidence list** to include OpenSpec v58 (fact-verification gap from v58 build) + cc-sdd v61 (this wiki). Final evidence: GSD v5 + spec-kit v17 + OpenSpec v58 + cc-sdd v61 = N=4 observations.
2. **UN-STALE Pattern #21** — independent SDD-centered framework criterion satisfied by cc-sdd (independent org + independent author + independent intellectual lineage Kiro IDE).
3. **Promote Pattern #21 under criterion #2 structural-unambiguity-at-N=2** with formal-statement extension covering:
   - 4 observations criterially clean SDD-centered
   - 4 distinct organizational archetypes (solo-product-line + corporate + pseudonymous-org + solo-international)
   - All T1 currently; cross-tier promotion under criterion #1 reserved for future T2-T5 SDD framework emergence
4. **Document v60 → v61 audit decision arc** as routine-discipline validation:
   - v60 lineage-test rejected un-stale correctly (gsd-2 = same lineage)
   - v61 independence-evidence resolved un-stale correctly (cc-sdd = independent)
   - Codify "lineage-test then independence-test" ordering as routine v2.2 candidate

**For Storm Bear vault (v62 wiki-build window):**

1. Pilot `npx cc-sdd@latest --claude-skills` in 1 sandbox vault project (~1h setup + 1-week measurement)
2. Compare against ad-hoc Claude Code workflow on same feature
3. Consider parallel free-claude-code v60 pilot (orthogonal layer)
4. Document pilot findings in `04 Reviews/` for v63 mini-audit context

**For corpus monitoring (v62-v65 wiki window):**

1. Watch for T2-T5 SDD framework — would satisfy Pattern #21 default-criterion #1 cross-tier
2. Watch for 2nd external-IDE-methodology lineage observation (Pattern #21 sub-archetype consolidation potential)
3. Watch for 2nd install-time per-platform skill-format translator (Pattern #18 Layer 2 N=2 promotion eligibility)
4. Continue per-wiki Pattern #51 vibe-coding spectrum nuance evidence accumulation

---

**Wiki version:** v61
**Phase 4b primary routing mode:** un-stale mechanism applied to Pattern #21 SDD Methodology Emergence
**Velocity:** ~75-90 min compressed-scope direct-write (estimated)
**Status: DONE_WITH_CONCERNS** — concern: fact-verification gap noted at §3.2 (Pattern #21 evidence list missing OpenSpec v58 from v60 audit); recommend mini-audit address.
