# (C) Pattern #83 Honest-Deficiency-Disclosure Discipline — N=3 promotion proposal

**Author:** v67 wiki ship (opencode-antigravity-auth, 2026-05-18)
**Status:** Phase 4b PRIMARY deliverable
**Audit target:** Next mini-audit (v68 natural cadence trigger OR v69 audit window)
**Pattern Library reference:** [PATTERN_LIBRARY.md](../../../PATTERN_LIBRARY.md) + [_patterns/03-active-candidates.md](../../../_patterns/03-active-candidates.md#83-honest-deficiency-disclosure-discipline-new-v66-early-mini-audit--registered-n2-stale-risk-flagged)
**Routine reference:** [llm-wiki-routine-v2.2.md](../../../05 Skills/llm-wiki-routine-v2.2.md) §"Phase 4b NEW Pattern candidate proposal-document discipline"
**Sibling proposal exemplars:** v64 Pattern #19 N=3 promotion proposal + v65 Pattern #78 N=2 promotion proposal

---

## 1. Current status (pre-promotion baseline)

**Pattern #83 Honest-Deficiency-Disclosure Discipline** is currently registered as **CANDIDATE N=2 stale-risk-flagged** at v66 EARLY mini-audit (2026-05-14).

### Pattern statement (verbatim from registration)

> Framework or reference archive explicitly discloses limitations, accuracy boundaries, prior security exposure periods, or methodology gaps in user-facing surface (README / CHANGELOG / release notes) rather than minimizing or obscuring. Distinct from formal anti-vibe discipline (Pattern #51) — Pattern #51 is upfront-positioning; Pattern #83 is ongoing-disclosure of specific deficiencies.

### Existing N=2 evidence

| # | Subject | Wiki | Disclosure type | Strength |
|---|---------|------|----------------|----------|
| 1 | claude-seo | v64 | v1.9.6 release notes disclose 10 named VULN fixes with severity tags + acknowledgment of prior exposure period; does NOT minimize | STRONG |
| 2 | claude-code-system-prompts | v65 | CHANGELOG discloses 49 "no-change placeholder" versions as honest version-tracking artifact; README "Maintained by Piebald AI, not by Anthropic" disclaimer; "±20 tokens tolerance from runtime" explicit accuracy boundary | STRONG |

### Promotion criteria (3, from registration)

1. **Explicit numerical or categorical deficiency disclosure** (not just generic "limitations" section)
2. **User-facing surface** (README + CHANGELOG + release notes), not buried in docs
3. **Does NOT minimize or normalize** the deficiency (e.g., "yeah we exposed VULNs for 2 weeks before patching" rather than "minor security update")

### Required for promotion (registration text)

> *"Required for promotion: 3+ subjects with honest-deficiency-disclosure discipline."*

→ Adding v67 opencode-antigravity-auth as 3rd subject = **promotion-eligible**.

---

## 2. N=3 evidence proposal — opencode-antigravity-auth (v67)

### Subject profile

- Author: NoeFabris (solo independent engineer, `@dopesalmon` on X)
- Stats at v67: 10,500 stars / 1 fork / 91 releases / 691 commits / age 159 days
- Tier: T4 Bridge (Opencode ↔ Google Antigravity OAuth + Unified Gateway API)
- License: MIT
- TypeScript 97.6% / npm package

### Five distinct Pattern #83 disclosure surfaces (per Entity 3 catalog)

The subject does not just satisfy Pattern #83's criteria — it does so at FIVE INDEPENDENT disclosure surfaces, exceeding the threshold of "any-one-of":

| Surface | Type | Content (verbatim or paraphrase) | Criterion-1 ✅ | Criterion-2 ✅ | Criterion-3 ✅ |
|---------|------|----------------------------------|--------------|--------------|--------------|
| 1 | README `[!CAUTION]` block (open-by-default at top of README) | *"Using this plugin (and any proxy for Antigravity) violates Google's Terms of Service. A number of users have reported their Google accounts being **banned** or **shadow-banned** (restricted access without explicit notification)."* | Categorical disclosure of TOS violation + ban/shadow-ban risk | README opening section | "Your account may be suspended or permanently banned" — non-minimized |
| 2 | README "Legal" footer (collapsed `<details>` at bottom) | *"Terms of Service risk — may violate ToS of AI model providers / Account risk / No guarantees / Assumption of risk"* | 4-bullet categorical disclosure | README footer (still user-facing) | "All legal, financial, and technical risks" — non-minimized |
| 3 | README "Intended Use" disclaimer | *"Personal / internal development only / Respect internal quotas and data handling policies / Not for production services or bypassing intended limits"* | Categorical limitation of intended use | README content | "Not for production services" — directly restricts use, non-minimized |
| 4 | docs/ANTIGRAVITY_API_SPEC.md status banner | *"Last Updated: December 13, 2025"* + *"Status: Verified by Direct API Testing"* | Categorical: empirical-discovery status (not vendor contract) | Documentation directory | Honest about non-vendor-contract status |
| 5 | CHANGELOG entries (267 lines, 91 releases) | Multiple "Fixed #N" entries naming detection-patterns + enforcement responses, e.g., *"Auth headers aligned with official Gemini CLI... to reduce 'account ineligible' errors and potential bans"*; *"Linux users now masquerade as macOS (Antigravity does not support Linux as a native platform)"*; *"Skip account over 90% to prevent Google penalties"* | Quantitative (90% threshold) + categorical (issue-specific) | CHANGELOG = user-facing | "Linux users now masquerade as macOS" is brutally honest |

### Three-criteria evaluation (per registration)

| Criterion | Verdict | Evidence summary |
|-----------|---------|------------------|
| **(1) Explicit numerical or categorical deficiency disclosure** | ✅ **STRONG PASS** | Categorical: TOS violation, account ban, shadow-ban, ineligibility, assumption-of-risk, "not for production". Quantitative: 90% soft quota threshold; 49% CHANGELOG line-budget for failure-mode documentation. |
| **(2) User-facing surface (README + CHANGELOG + release notes)** | ✅ **STRONG PASS** | `[!CAUTION]` block is the 3rd major section of the README, open-by-default. CHANGELOG is link-prominent. Disclaimers also appear in docs/ directory. Multiple user-facing surfaces saturated. |
| **(3) Does NOT minimize or normalize** | ✅ **STRONG PASS** | "Your account may be suspended or permanently banned" is the opposite of minimization. "Linux users now masquerade as macOS" is brutally honest about platform misrepresentation. "Assumption of risk" formula is legal-disclaimer-grade. |

→ **All 3 promotion criteria SATISFIED with STRONG PASS verdicts at 5 distinct disclosure surfaces.**

---

## 3. Structural diversity table (post-promotion 3-subject coverage)

A confirmed pattern at N=3 should span structurally distinct subjects to demonstrate generalizability. Post-promotion Pattern #83 coverage:

| Dimension | claude-seo (v64) | claude-code-system-prompts (v65) | opencode-antigravity-auth (v67) | Diversity verdict |
|-----------|-----------------|----------------------------------|--------------------------------|-------------------|
| **Tier** | T1 domain-vertical-skill-collection | T1 reverse-engineering-reference-archive | T4 Bridge OAuth-plugin | ✅ 3-tier-axis distinct (T1 + T1-sub + T4) |
| **Archetype** | Solo individual + community contributions (Pro Hub Challenge) | Corporate-org (Piebald AI) | Solo individual (NoeFabris) | ✅ Solo vs corporate-org distinct |
| **Deficiency type disclosed** | Security VULN exposure period | Methodology accuracy boundary + maintainer-vs-source disclaimer | TOS violation + account-ban risk + intended-use boundary | ✅ Security vs methodology vs legal/operational distinct |
| **Disclosure surface** | Release notes primary | CHANGELOG + README primary | README opening `[!CAUTION]` + Legal footer + CHANGELOG entries (5 surfaces) | ✅ Different primary surfaces |
| **Quantitative disclosure component** | 10 named VULNs with severity | ±20 tokens accuracy tolerance | 90% soft quota threshold | ✅ All include quantitative dimension |
| **Adversarial-relationship axis** | None (own-author code) | None (third-party archive, vendor-tolerant) | YES — adversarial vendor relationship (Google enforces) | ✅ Distinct relationship axes |

**Verdict:** Coverage is structurally diverse across 6 dimensions. Pattern #83 is NOT a single-archetype-locked observation; it generalizes across solo + corporate authors, T1 + T4 tiers, security + methodology + legal deficiencies, and cooperative + adversarial vendor relationships.

---

## 4. Promotion criteria evaluation (5 criteria from Pattern Library v2.2)

Pattern Library's standard promotion criteria (from `_patterns/01-audit-history.md` and routine v2.2 §"Mini-audit protocol"):

1. **Structural unambiguity at N=2** — Pattern observable with structural clarity at the second instance (independent of N=3 evidence).
2. **Mechanism specifiability** — The pattern's mechanism can be stated independent of its instances.
3. **Sub-typology readiness** — At N=3, sub-taxonomy variants observable.
4. **Cross-archetype evidence** — Pattern observed across structurally distinct archetypes.
5. **Cross-tier evidence** OR **Cross-archetype evidence equivalent**.

### Evaluation

| # | Criterion | Verdict | Evidence |
|---|-----------|---------|----------|
| 1 | Structural unambiguity at N=2 | ✅ SATISFIED | v64 + v65 unambiguously matched the formal statement at registration (v66 EARLY mini-audit). |
| 2 | Mechanism specifiability | ✅ SATISFIED | Mechanism = "explicit deficiency disclosure on user-facing surface, non-minimized". Stated independent of instances. |
| 3 | Sub-typology readiness | ⚠️ PARTIAL | At N=3, candidate sub-taxonomy emerges: 83a security-disclosure (v64) / 83b methodology-disclosure (v65) / 83c legal-operational-disclosure (v67). However, recommending **deferring sub-taxonomy to v69 audit** until 4th-or-5th evidence stabilizes which dimensions split vs. unify. |
| 4 | Cross-archetype evidence | ✅ SATISFIED | Solo (v64 + v67) + corporate-org (v65); domain-vertical (v64) + reverse-engineering (v65) + bridge-utility (v67). |
| 5 | Cross-tier evidence | ✅ SATISFIED | T1 (v64, v65) + T4 (v67) = 2 distinct tiers. |

**Overall verdict:** 4 of 5 SATISFIED + 1 PARTIAL (sub-taxonomy deferred). Promotion-eligible at next audit.

---

## 5. Recommended verdict

**Recommended action:** **PROMOTE Pattern #83 Honest-Deficiency-Disclosure Discipline from CANDIDATE (N=2 stale-risk-flagged) to CONFIRMED at next audit (v68 natural cadence or v69 audit window).**

### Confidence level

**HIGH confidence** for promotion based on:
- All 3 registration criteria satisfied with STRONG PASS verdicts
- 5 distinct disclosure surfaces in v67 subject alone (saturation evidence)
- Structural diversity across 6 dimensions (solo/corp, T1/T4, security/methodology/legal, etc.)
- 4-of-5 standard promotion criteria satisfied (5th = sub-typology, deferred as standard practice)

### Tagging recommendation

If promoted, register as **CONFIRMED** within the Pattern Library; assign **Tier-Taxonomy classification** under "ongoing-disclosure-discipline" alongside Pattern #51 Vibe-Adjacent Positioning Spectrum (related but distinct).

### Sub-taxonomy decision

**Defer sub-taxonomy to v69 audit.** The 3-subject evidence suggests 3 emergent sub-types (83a security / 83b methodology / 83c legal-operational) but a 4th-5th subject is needed to stabilize which dimensions split vs. unify. Following the v60-v65 strengthen-over-discover discipline, deferral is the conservative choice.

---

## 6. Acceleration consideration (v2.2 NEW per v65 lesson)

Does this proposal qualify for **acceleration audit** (audit at +1 wiki vs +2-3 natural cadence)?

**Per routine v2.2 acceleration criteria:** acceleration is warranted when *"high-impact promotion is ripe (e.g., LONGEST stale arc)"*.

**Pattern #83 acceleration analysis:**
- **Registration:** v66 EARLY mini-audit (2026-05-14)
- **Wiki count from registration to promotion-readiness:** v67 (this wiki) = **1 wiki**
- **Speed comparison:** Same speed as Pattern #78 promotion arc (also 1 wiki from N=2 → N=3, i.e., from v65 registration to v66 promotion). NOT faster.
- **Impact:** Pattern #83 has substantial cross-tier + cross-archetype evidence; promotion would consolidate the disclosure-discipline observational track that's been accumulating since v60+.

**Recommendation:** **DO NOT REQUEST ACCELERATION.** Wait for v68 natural cadence audit OR operator-elected v69 timing. The promotion is ready; acceleration adds operational urgency without proportional benefit.

If an acceleration audit IS elected (operator's discretion, e.g., paired with another high-impact promotion), Pattern #83 is ready for inclusion.

---

## 7. Audit checklist (for next-audit operator deliberation)

When deliberating Pattern #83 promotion at the next audit, verify:

- [ ] All 3 registration criteria satisfied — confirmed by 3-subject evidence table in Section 2
- [ ] At least 1 quantitative disclosure component in each subject (v64 = 10 VULNs; v65 = ±20 tokens; v67 = 90% threshold) — confirmed
- [ ] No subject's disclosure relies on a "limitations" section that minimizes via boilerplate ("known issues") — confirmed (3 subjects all use specific named deficiencies)
- [ ] Structural diversity across at least 2 distinct dimensions — confirmed at 6 dimensions (Section 3)
- [ ] Mechanism specifiability re-checked — Pattern #83 mechanism is specifiable independent of instances (Section 4)
- [ ] Sub-taxonomy decision: ADOPT or DEFER — recommendation: DEFER to v69 (3-subject evidence emerging but premature)
- [ ] Cross-reference Pattern #51 Vibe-Adjacent Positioning Spectrum sub-pole — Pattern #83 distinct (Pattern #51 = upfront-positioning; #83 = ongoing-disclosure-of-specific-deficiencies)
- [ ] No overlap >70% with another confirmed pattern — verified: Pattern #51 is the closest semantic neighbor; mechanism distinct
- [ ] Auditor's independent verification: read the 3 disclosure-surface tables in section 2; verify subject text matches Pattern #83 criteria

---

## 8. Evidence document cross-references

**Primary evidence sources (verifiable):**

| Source | Subject | Location |
|--------|---------|----------|
| README.md `[!CAUTION]` block | v67 opencode-antigravity-auth | [README.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/README.md) §"Terms of Service Warning — Read Before Installing" (lines 23-35) |
| README "Legal" footer | v67 opencode-antigravity-auth | README.md §"Legal" (lines 695-718) |
| docs/ANTIGRAVITY_API_SPEC.md status banner | v67 opencode-antigravity-auth | [docs/ANTIGRAVITY_API_SPEC.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/ANTIGRAVITY_API_SPEC.md) (lines 1-10) |
| CHANGELOG.md entries | v67 opencode-antigravity-auth | [CHANGELOG.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/CHANGELOG.md) (v1.0.0 → v1.6.0, 267 lines) |
| v1.9.6 release notes (10 VULN disclosure) | v64 claude-seo | claude-seo wiki Cluster 3 + CHANGELOG.md v1.9.6 entry |
| CHANGELOG 49 placeholders + README accuracy tolerance | v65 claude-code-system-prompts | claude-code-system-prompts wiki Cluster 1 + Cluster 2 + README §"Accuracy" |

**Wiki cross-references:**

- [v67 entity-3-antigravity-unified-gateway.md](../02 Wiki/entity-3-antigravity-unified-gateway.md) — Phase 4b PRIMARY entity with full Pattern #83 evidence catalog
- [v67 cluster-1-readme-and-tos-framing.md](../02 Wiki/cluster-1-readme-and-tos-framing.md) — verbatim TOS warning extraction
- [v67 cluster-3-quota-api-and-changelog.md](../02 Wiki/cluster-3-quota-api-and-changelog.md) — CHANGELOG-as-disclosure-surface evidence
- v64 claude-seo wiki — N=1 evidence
- v65 claude-code-system-prompts wiki — N=2 evidence
- v66 EARLY mini-audit registration document — original Pattern #83 registration

---

## 9. Post-promotion follow-up (if promoted)

After promotion at next audit:

1. **Update `_patterns/02b-confirmed-patterns-v42-plus.md`** with full Pattern #83 promoted entry
2. **Remove from `_patterns/03-active-candidates.md`** (or mark as PROMOTED)
3. **Update PATTERN_LIBRARY.md confirmed count** (43 → 44)
4. **Update active candidate count** (27 → 26 — net -1 from promotion, +N from new candidates registered at audit)
5. **Update ratio** (active/confirmed) — recompute
6. **Defer sub-taxonomy to v69 audit** — log as deferred audit item
7. **Cross-pattern coupled-design observation:** Pattern #83 co-occurs with Pattern #51 anti-vibe-with-pragmatic-acknowledgment in v67 evidence (NoeFabris's explicit upfront-acknowledgment-of-risk is anti-vibe; ongoing CHANGELOG disclosure is Pattern #83). Library-vocabulary item #9 cross-pattern coupled-design N+1 evidence.

---

## 10. Summary recommendation

**PROMOTE Pattern #83 Honest-Deficiency-Disclosure Discipline from CANDIDATE (N=2 stale-risk-flagged) to CONFIRMED at next audit.**

- All 3 registration criteria satisfied with STRONG PASS verdicts
- N=3 evidence from v64 + v65 + v67 (this wiki)
- Structural diversity across 6 dimensions
- 4-of-5 standard promotion criteria satisfied (sub-taxonomy deferred to v69)
- HIGH confidence verdict

No acceleration request; await v68 natural-cadence or v69 audit window.
