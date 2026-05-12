# Pattern #76 amendment draft (ready to paste after Step 10 closes 2026-05-13)

> **Purpose:** Pre-drafted evidence-note to append to `_patterns/03-active-candidates.md` Pattern #76 entry (lines 588-595) after Step 10 finalization.
> **Session B verdict held:** structural sanity-check confirms pilot tested ADVERSARIAL-REVIEW-PROMPT layer only, NOT framework-level subagent architecture. Pattern #76 stays STAGED.
> **Pass 3 independence:** Pass 3 retry outcome (2026-05-13T02:03Z) can refine Proposition A/B propositional numbers but CANNOT change this structural verdict — pilot scope is what it is.

---

## Sanity-check against Pattern #76 definition (vault Session B 2026-05-12 evening)

Pattern #76 as registered at v63 audit requires **4 architectural components** to be present as documented architectural primitives:

| Component | Pattern #76 specifies | This pilot's BMAD baseline | This pilot's codex-plugin-cc |
|-----------|----------------------|------------------------------|------------------------------|
| **Implementer subagent** (TDD: RED→GREEN→REFACTOR) | YES — distinct named role | NO — no implementer in pilot | NO — review-only |
| **Reviewer subagent** (named role distinct from implementer) | YES — `kiro-review` in cc-sdd | PARTIAL — `bmad-review-adversarial-general` is a skill, not framework-architecture role | PARTIAL — `/codex:adversarial-review` is a slash command, not architectural role |
| **Auto-debug-on-rejection** (`kiro-debug` returns ROOT_CAUSE/FIX_PLAN) | YES — explicit rejection-loop | NO — no rejection loop | NO — no rejection loop |
| **Fresh-evidence completion gate** (`kiro-verify-completion`) | YES — VERIFIED/NOT_VERIFIED/MANUAL_VERIFY_REQUIRED | NO — no verification cycle | NO — no verification cycle |

**Score:** BMAD baseline: 0/4 full + 1/4 partial. codex-plugin-cc: 0/4 full + 1/4 partial. **Neither qualifies as Pattern #76 N=2 evidence.**

The pilot conflated **adversarial-review-as-prompt-framing** (which both tested tools provide) with **adversarial-review-as-architectural-primitive** (which Pattern #76 actually defines). These are 2 distinct phenomena at different layers. Pilot data is valid for the PROMPT layer; Pattern #76 is about ARCHITECTURE.

---

## Recommended evidence-note text (paste after current line 595)

```markdown
**2026-05-13 pilot v3.2 hireui evidence (vault Session B sanity-check confirmed 2026-05-12 evening):** Tool-level adversarial review (BMAD's `bmad-review-adversarial-general` + codex-plugin-cc's `/codex:adversarial-review`) tested on real harness work (61-file / 17-commit diff). Results show tool-level adversarial framing produces substantive findings (Pass 1: 18 findings, 7+ initial real bugs). **Pilot does NOT test framework-level subagent role separation** per Pattern #76 4-component definition — both tested tools score 0/4 full + 1/4 partial against (implementer + reviewer + auto-debug + completion-gate) architectural primitives. **Provides Proposition C evidence** (tool-level adversarial has independent value) but **does NOT satisfy promotion bar**. Pattern #76 remains N=1 (cc-sdd v61 baseline).

**Tool-level vs framework-level distinction:** Tool-level adversarial review skills (slash commands / prompted reviews) are a separate phenomenon — proposed as future candidate pattern if 2nd corpus example emerges. Pattern #76 explicitly NARROW to architectural-primitive framing to preserve distinctive claim (architecture vs ad-hoc skill).

**v66 audit recommendation:** Keep staged. Watch for 2nd-framework candidates: (a) BMAD v11 FULL agent-system (not just adversarial-review skill — does v11 codify implementer+reviewer split as primitive?); (b) OpenHands v30 re-check for less-structured vs adversarial subagent dispatch; (c) any v62-v66 framework releases with named-role architecture; (d) cc-sdd v62-v66 evolution if it ships further architectural primitives. v71 retire-check unchanged.
```

---

## 2nd-framework candidates to scout (between v63 ship and v66/v71)

### Priority 1 — frameworks already in corpus with subagent architecture

| Subject | Wiki | What to verify |
|---------|------|----------------|
| **BMAD v11** | corpus pre-v63 | Re-read framework docs: does v11 codify implementer+reviewer as named-role primitive, or just persona-system with cooperative dispatch? Pattern #76 rationale specifically excludes BMAD as "cooperative not adversarial" — verify this still holds in v11+. |
| **OpenHands v30** | corpus | Re-read framework architecture: less-structured subagent orchestration per Pattern #76 rationale. Check if any 2026 release adds adversarial role-separation. |
| **AutoGPT v59** | corpus | Multi-agent architecture exists. Verify whether agent-dispatch is cooperative (delegate-and-trust) or adversarial (delegate-and-challenge). |
| **cc-sdd v61** (N=1 baseline) | corpus | Track future cc-sdd releases for architectural-primitive evolution. v3.x kiro-* architecture is the N=1 anchor. |

### Priority 2 — non-corpus frameworks to investigate

| Subject | Why interesting |
|---------|-----------------|
| **Aider** | Aider's `--auto-test` mode dispatches edit + test phases; check if test phase has reviewer-subagent semantics |
| **Continue.dev** | Has agent-system with named tools; check if reviewer role is documented primitive |
| **SWE-agent** (Princeton/research) | Academic agent-system; check whether reviewer-subagent appears in architecture papers |
| **Devin** (Cognition) | Proprietary but documented; check public architecture descriptions for reviewer-subagent |
| **Codename Goose** (Block) | Documented framework architecture |

### Priority 3 — pre-register watch criteria

For ANY new framework wiki shipped between v64 and v71, Phase 0 probe should check:

```
Pattern #76 N=2 verification checklist (in Phase 0 probe):
- [ ] Framework documents EXPLICIT implementer subagent as named role?
- [ ] Framework documents EXPLICIT reviewer subagent as named role distinct from implementer?
- [ ] Framework documents rejection-loop semantics (reviewer can reject implementer output → triggers re-impl)?
- [ ] Framework documents fresh-evidence completion gate (verification cycle distinct from review)?
- [ ] All 4 components documented as ARCHITECTURAL PRIMITIVES (not opt-in skills)?

If 4/4 YES → register as Pattern #76 N=2 evidence
If 3/4 YES → register as partial-evidence with note about missing component
If <3/4 YES → not Pattern #76 evidence; consider new candidate pattern if tool-level adversarial review present
```

This checklist becomes a routine v2.2 codification candidate.

---

## Why this verdict is STRUCTURAL (Pass 3 independence proof)

Pass 3 (codex adversarial framing) when it runs 2026-05-13T02:03Z will produce a Pass 3 finding count + overlap-with-BMAD matrix. None of those outcomes can change the structural fact that:

1. **Neither tool tested has all 4 Pattern #76 architectural components.** Pass 3 doesn't add implementer subagent, doesn't add auto-debug rejection loop, doesn't add completion-gate verification. The 4-component test is structural, not numerical.

2. **Even if Pass 3 produces 50 findings with 100% overlap with BMAD's 18,** that would prove "adversarial framing dominates tool choice" (Proposition A) but says NOTHING about framework-architecture qualification.

3. **The pilot was designed as a Pattern #76 evidence-gathering exercise but in retrospect tested a DIFFERENT phenomenon** (adversarial review as prompt layer, not as architecture). This isn't a pilot-failure — it's a pilot-scope discovery. Both pieces of evidence (tool-level value + framework-level absence) are useful corpus contributions.

**Therefore:** Pattern #76 stays STAGED N=1 regardless of Pass 3 outcome. The evidence-note above can be appended to vault Pattern #76 entry as soon as Step 10 finalizes Pass 3 numbers.

---

## Open questions surfaced for operator review

1. **Should the pilot have been framed differently?** Retrospective question — original pilot plan §3.5 §1 framed it as "Pattern #76 empirical comparison" but the actual test scope is narrower. Pilot plan v3.3 (post-pilot revision) should clarify "pilot tests tool-level adversarial review skills; framework-level architecture comparison requires different corpus subjects."

2. **Should we register a NEW candidate Pattern #79 Tool-Level Adversarial Review as Skill?** Pre-register criteria: 2+ tools shipping adversarial-review-as-prompt-framing skill (where "shipping" means OSS-available or documented in framework). At minimum: BMAD ships `bmad-review-adversarial-general`, codex-plugin-cc ships `/codex:adversarial-review` → already N=2 evidence for a NEW pattern. Worth registering at v66 mini-audit.

3. **Does cc-sdd's `kiro-review` skill ALSO qualify as tool-level adversarial review (separate from the framework architecture it's embedded in)?** If yes, that's a 3rd evidence point for the NEW tool-level pattern AND preserves cc-sdd's framework-level role for Pattern #76 itself. Two-layer pattern decomposition.

These questions are for v66 mini-audit deliberation, not pilot Step 10.

---

## Action sequence after Step 10 closes 2026-05-13

```
1. [vault Session B] Append evidence-note text above to _patterns/03-active-candidates.md
   between current line 595 and 597 (before the --- separator)
2. [vault Session B] Update header line 588 emoji + status if needed (likely stays 🟡 N=1 stale-risk-flagged)
3. [vault Session B] Commit vault: "Append Pattern #76 evidence note from pilot v3.2 hireui (structural verdict: stays N=1)"
4. [v66 mini-audit deliberation] Register routine v2.2 candidate: "Phase 0 probe checklist for Pattern #76 N=2 verification" (the 5-question gate above)
5. [v66 mini-audit deliberation] Decide whether to register NEW Pattern #79 Tool-Level Adversarial Review as Skill candidate (N=2 evidence already exists: BMAD + codex-plugin-cc; +1 if cc-sdd kiro-review also qualifies independently)
```

---

## Cross-references

- Pilot pattern-76 evidence (provisional): `pattern-76-evidence-2-of-3.md` (this folder)
- Step 10 provisional ablation: `step-10-provisional-analysis.md` (this folder)
- Pilot plan v3.2: `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md`
- Pattern #76 vault entry: `/Users/Cvtot/KJ OS Template/_patterns/03-active-candidates.md` lines 588-595
- v63 EARLY mini-audit (where Pattern #76 was registered): `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-07 Pattern Library mini-audit post-v61 (early-elected; 1 promotion + 3 NEW candidates + 6 within-pattern decisions).md`
