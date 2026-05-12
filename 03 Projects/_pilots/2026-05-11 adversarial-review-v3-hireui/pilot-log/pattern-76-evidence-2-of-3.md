# Pattern #76 evidence note — 2-of-3 passes (provisional)

> **Audience:** vault `_patterns/03-active-candidates.md` Pattern #76 evaluator, v66 mini-audit decision-maker
> **Status:** PROVISIONAL (Pass 3 retry pending 2026-05-13T02:03Z). Pass 3 will refine the numbers but is unlikely to change the structural read below.
> **Header position:** This pilot was framed around Pattern #76 evidence. The data so far requires a more careful interpretation than the pilot plan suggested.

## Pattern #76 as registered (v63 mini-audit)

**Statement:** "AI agent frameworks codify adversarial-by-design subagent role separation as architectural primitive — implementer subagent + reviewer subagent + auto-debug + fresh-evidence completion gate, with explicit role boundaries and rejection-loop mechanics."

**Promotion bar:** "2+ frameworks with adversarial-by-design subagent role separation as documented architectural primitive (explicit reviewer + implementer + rejection loop)."

**Evidence at v63:** cc-sdd v61 only (N=1, stale-risk-flagged).

## What this pilot actually tests

| Pattern #76 component | This pilot tests it? |
|---|---|
| Adversarial review prompt/mandate | ✅ YES — BMAD's `review-adversarial-general.xml` is exactly this |
| Implementer subagent (TDD RED→GREEN→REFACTOR) | ❌ NO — no implementer/reviewer split tested; review-only pass |
| Reviewer subagent as named role distinct from implementer | ⚠️ PARTIAL — BMAD skill IS a reviewer role but no implementer subagent in this pilot |
| Auto-debug-on-rejection (`kiro-debug` returns ROOT_CAUSE/FIX_PLAN) | ❌ NO — no rejection loop, single-pass output |
| Fresh-evidence completion gate (`kiro-verify-completion`) | ❌ NO — no verification cycle |
| Role boundaries documented as architectural primitive | ❌ NO — BMAD review is a SKILL invoked ad-hoc, not architectural rule |

**Conclusion: this pilot tests the ADVERSARIAL REVIEW PROMPT layer of Pattern #76, not the FULL framework-level subagent architecture the pattern is defined as.** It is BMAD Pass 1's F-02 finding, taken seriously: the pilot scope is narrower than the pattern.

This is not a fatal flaw for the pilot — it just means the pilot's output is **necessary-but-not-sufficient evidence** for Pattern #76.

## What the pilot data DOES tell us (Pattern-#76-relevant)

### Headline observation from 2-of-3 passes

| Comparison | Finding count | Real bugs initial | Overlap |
|---|---|---|---|
| Pass 1 BMAD adversarial framing | 18 | 7 | (baseline) |
| Pass 2 codex neutral (no framing) | 2 | 2 | 0/18 (0%) |
| Pass 3 codex adversarial framing | _N_ (pending) | _N_ (pending) | _N_/18 (pending) |

**Two strata fish in different ponds:** BMAD adversarial ranges across design/spec/scope/code; codex neutral drills into implementation defects (skill name/dir mismatch, telemetry session scoping). 0 direct topic overlap.

### Three propositions this lets us evaluate

**Proposition A:** "Adversarial framing produces more findings than neutral framing, all else equal."
- Pass 1 (18) > Pass 2 (2), but this confounds tool AND framing. Pass 3 (codex + adversarial framing) is the disambiguator.
- **2-of-3 read:** weakly supported pending Pass 3.

**Proposition B:** "Tool/model identity matters as much or more than framing for review output."
- 0/18 overlap between Pass 1 and Pass 2 suggests tool-driven topic-coverage difference. But this is a single observation pair and Pass 3 might flip it.
- **2-of-3 read:** competing-hypothesis pending Pass 3.

**Proposition C:** "Tool-level adversarial review provides measurable value even WITHOUT framework-level subagent architecture."
- Pass 1's 18 findings (4 CRITICAL, 5 HIGH) on a 17-commit harness diff are evidently substantive — even without implementer/reviewer split or rejection loop.
- **2-of-3 read:** SUPPORTED. Tool-level adversarial review is non-trivial.

### Pattern #76 evidence implications

| Pattern #76 status option | Pilot evidence so far supports it? |
|---|---|
| Promote with N=2 (cc-sdd + hireui-tool-level) | ❌ NO — hireui pilot does not implement framework-level architecture per Pattern #76 definition |
| Keep staged + amend definition to include "tool-level adversarial review skills" | ⚠️ POSSIBLE — but dilutes the pattern's distinctive claim (architectural primitive vs ad-hoc skill) |
| Keep staged + retire if no 2nd framework lands framework-level architecture by v71 | ✅ DEFENSIBLE — consistent with v63 stale-risk flag |
| Retire as cc-sdd-specific | ⚠️ PREMATURE — pilot doesn't speak to this either way |

**Recommendation for v66 mini-audit:** **Keep Pattern #76 staged**. This pilot provides Proposition C evidence (tool-level adversarial has value) which is a useful PREREQUISITE for asking whether framework-level architecture adds further lift, but does not itself satisfy the 2+ framework promotion bar.

## What WOULD constitute Pattern #76 evidence

A future test would need:
- A framework that codifies **explicit reviewer subagent** as named role (not just a skill someone happens to invoke)
- Distinct from **implementer subagent** that ships in the same framework
- With **rejection loop** semantics (reviewer can reject implementer output, triggers re-implementation cycle)
- Documented as **architectural primitive** (in framework docs, not as an opt-in skill)

Candidate frameworks to watch (per Pattern #76 rationale section):
- BMAD's full agent-system (NOT this pilot's adversarial-review-only test) — does v11 actually codify implementer+reviewer split as primitive?
- OpenHands v30 — described as "less-structured subagent orchestration"; needs re-check
- Any new framework launches between now and v66

## Adjustment to vault state

The vault entry for Pattern #76 at line 588-595 of `_patterns/03-active-candidates.md` should be amended with an evidence-note (when Pass 3 lands):

> **2026-05-13 pilot v3.2 hireui evidence:** Tool-level adversarial review (BMAD's `bmad-review-adversarial-general` + codex-plugin-cc's `/codex:adversarial-review`) tested on real harness work; results show tool-level adversarial framing produces substantive findings (Pass 1: 18 findings, 7+ initial real bugs on 17-commit diff). Pilot does NOT test framework-level subagent role separation per Pattern #76 definition. **Provides Proposition C evidence** (tool-level adversarial has independent value) but **does not satisfy promotion bar**. Recommendation: keep staged, await 2nd framework with framework-level architecture by v71.

## Open questions for Session B (vault) re-eval

1. Should Pattern #76 promotion bar be relaxed to include tool-level adversarial review skills, OR strict to framework-level architecture only?
2. Is BMAD's full agent-system (NOT just the adversarial-review skill tested here) closer to Pattern #76 than this pilot revealed?
3. Are there v66-window framework releases worth scouting for 2nd-framework evidence before retiring the pattern?

## What changes when Pass 3 lands

Headline numbers and overlap matrix get filled. Three propositions get clearer answers:
- Proposition A (framing produces more findings): confirmed/refuted at 2-of-3 = 99% / 1%
- Proposition B (tool dominates framing): becomes testable
- Proposition C (tool-level adversarial has value): already supported, Pass 3 mostly redundant

**The Pattern #76 verdict above does NOT depend on Pass 3 outcomes** — it's structural (pilot scope vs pattern definition). Pass 3 refines the propositional analysis but doesn't change the "necessary-but-not-sufficient" framing.
