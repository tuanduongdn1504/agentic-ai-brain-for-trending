# Pilot v3.2 Step 10 — Ablation analysis (PROVISIONAL, 2-of-3 passes)

> **Status:** PROVISIONAL — Pass 3 blocked on codex usage limit (B-A18). Finalize after 2026-05-13T01:58Z retry.
> **Why publish provisional:** Pass 1 (BMAD adversarial) + Pass 2 (codex neutral) already yields actionable signal for Pattern #76 evaluation and pilot scope decisions. Pass 3 will either reinforce or revise the read; documented assumptions are explicit so the revision delta is auditable.

## TL;DR (one-sentence read)

On a 61-file, 17-commit harness diff, BMAD adversarial mandate (Pass 1) produced 18 findings dominated by **design/spec-layer challenges**, while codex neutral review (Pass 2) produced 2 findings at the **implementation-defect layer** — with **0% overlap on distinct topics**. The two strata appear complementary, not substitutable. Pass 3 will determine whether adversarial framing closes that overlap gap or whether tool/model identity dominates.

## Headline numbers

| Metric | Pass 1 BMAD adversarial | Pass 2 codex neutral | Pass 3 codex adversarial |
|---|---|---|---|
| Wall-clock | 3m 23s | 5m 46s | ❌ blocked at 1m 30s |
| Findings | 18 | 2 | _pending_ |
| Real bugs (initial classification) | 7 | 2 | _pending_ |
| Design challenges | 7 | 0 | _pending_ |
| Subjective | 4 | 0 | _pending_ |
| Severity ceiling | CRITICAL | P2 (≈ MEDIUM) | _pending_ |
| Approx output tokens | ~1700 | ~450 | _pending_ |
| Cost per finding (sec) | ~11s | ~173s | _pending_ |
| Cost per real bug (sec) | ~29s | ~173s | _pending_ |
| Overlap with BMAD | n/a | **0/18 (0%)** | _pending_ |
| Tool-unique findings | n/a | 2 (NEW topics) | _pending_ |

## Empirical findings (so far)

### Finding 1: The two strata fish in different ponds

**Pass 1 BMAD topics (deduplicated 18):**
- Schema/spec layer: F-03 doctored count, F-04 vapor Phase 2, F-08 no audit trail, F-12 primary_alternative inconsistency, F-14 thresholds unitless, F-16 rubric versioning
- Scope/pilot framing layer: F-02 Pattern #76 scope mismatch, F-13 commit bundling, F-18 mattpocock scope drift
- Code-level: F-05 mv non-atomic, F-06 YAML extraction, F-10 ORIG_HEAD over-fires
- Doc hygiene: F-11 prefix vocab undocumented, F-17 dateline omission, F-15 doc self-inconsistency
- Tooling/observability: F-01 telemetry asymmetry, F-09 gitignore ratchet
- Curation: F-07 zero-relevance skills

**Pass 2 codex topics (2):**
- Code-level integration: C2-1 skill name vs directory mismatch, C2-2 telemetry-log session scoping

**Read:** Codex (neutral) goes straight to where the code actually executes (hook lookup paths, query semantics). BMAD (adversarial mandate) ranges across design, schema, scope, doc hygiene, and code — wider net but shallower on code-execution specifics.

### Finding 2: F-01 partial refutation

Pass 1 F-01 claimed E3 PostToolUse hook only catches Stratum A (`Skill` tool calls). **Pass 2 disproved that claim for the Skill-dispatched path** — when `/codex:review` is invoked via `Skill(skill="codex:review")`, E3 DOES fire (telemetry row appeared in `.cm/memory/skill-invocation-log.json`). F-01 only stands for direct user-typed `/slash` commands. Operator implication: stratum-B telemetry is recoverable if invocations are always dispatched via Skill, not directly via slash.

### Finding 3: Both tools missed the same things

Neither pass surfaced (as of 2-of-3):
- Whether `cm-continuity` skill's protocol is actually followed in this session
- macOS bash 3.2 compatibility of `set -euo pipefail` in migration script
- Performance of 20-skill auto-load on session start
- Whether `mattpocock-handoff` invocation (which DID happen) actually produced the documented artifact

These are **higher-order behavioral checks** — they require running the harness and observing, not reviewing static diff. Both adversarial review tools have a "review code from text" surface and both share that surface's blind spot.

### Finding 4: Cost dynamics

- BMAD: 1 finding per 11s, 1 real bug per 29s
- Codex neutral: 1 finding per 173s, 1 real bug per 173s
- Naive "findings per second" massively favors BMAD (16× higher rate)
- But codex's findings have higher **code-traceability** — every finding has a file:line reference and a reproduce-step. BMAD's findings vary: some are crisp (F-05 mv), some need operator decision (F-04 vapor)
- **Effective ratio depends on the question** — if the question is "did this diff introduce a code bug?", codex's slower deeper pass may be more cost-effective. If the question is "are we shipping a coherent change?", BMAD's wider net matters more.

## Pattern #76 evidence assessment

Pattern #76 (Adversarial Subagent Review Architecture at Framework Level) claims that framework-level subagent architecture is the differentiator. **The 2-of-3 data so far:**

- BMAD's adversarial mandate is the framework-level prompting (XML task file, structured rubric, ≥10 finding floor).
- Codex neutral has NO equivalent framework — it's "review this diff" with default prompting.
- BMAD found 18 findings; codex neutral found 2.
- **Naive read:** framework adversarial framing produces more findings → supports Pattern #76.
- **Strong-form challenge:** but 0/18 overlap means BMAD's extra 16 findings could be **lower-signal** (subjective, design challenges, judgment calls) while codex's 2 are real code bugs BMAD missed. So "more findings" ≠ "better review."

**Pass 3 is the decisive variable.** If `/codex:adversarial-review` (codex tool + adversarial framing) produces:
- 18+ findings with high BMAD overlap → framing dominates tool/model → **Pattern #76 strongly supported**
- 2–5 findings still mostly code-level (similar to Pass 2) → tool/model dominates framing → **Pattern #76 weakly supported or undermined**
- Mixed result → framework helps but isn't sole differentiator

## Operator decision dependencies (Pass 3 unblocked)

These pilot Step 10 decisions need Pass 3 data:

1. **Retire BMAD?** Only if Pass 3 reproduces all BMAD findings AND adds codex-style code-level depth.
2. **Retire codex-plugin?** Only if Pass 3 fails to add anything beyond Pass 1 + Pass 2.
3. **Keep both?** Default if Pass 3 confirms complementarity (likely).
4. **Augment BMAD with code-trace prompts?** Likely yes regardless, since Pass 2's 2 codex-unique findings are clearly within reach of an adversarial XML task that demands code-execution path tracing.

## Decisions actionable on 2-of-3 data (no Pass 3 dependency)

These can land before Pass 3 retry, regardless of outcome:

1. **F-01 refinement:** update CLAUDE.md skill-management policy to note that slash-dispatched-via-Skill produces telemetry; direct slash does not.
2. **C2-1 fix:** normalize `mattpocock-*` SKILL.md frontmatter `name:` to match directory basename, OR update `check-skill-policy.sh` to resolve directory by glob/registry index. Pick approach + land it.
3. **C2-2 fix:** add session_id to telemetry log entries; filter `check-skill-policy.sh` primary-check query to current session only.
4. **F-05/F-06/F-10 quick fixes** from BMAD Pass 1 (mv atomicity, YAML extraction, ORIG_HEAD guard) — operator-confirmed real bugs, mechanical fixes.

## Open questions for Step 10 finalization

- Does Pass 3 retrieve operator-confirmed real bug counts vs initial classification? (currently BMAD 7-real-bugs is initial classifier, not operator-confirmed)
- What's the cost-per-confirmed-real-bug ratio after operator triage?
- Does Pass 3 produce CRITICAL-severity findings BMAD missed? (would be evidence FOR codex)
- Does Pass 3 reproduce F-02 Pattern #76 scope mismatch? (would be evidence that codex can do meta-pilot critique under adversarial framing)

## Data sources

- Pass 1 full capture: `.pilot-log/pass-1-bmad-adversarial.md`
- Pass 2 full capture: `.pilot-log/pass-2-codex-review.md`
- Pass 3 failure record: `.pilot-log/pass-3-codex-adversarial.md`
- Telemetry log: `.cm/memory/skill-invocation-log.json` (Skill-dispatched invocations only)
- Blocker file: `.cm/memory/blockers.json` (B-A18 records Pass 3 failure)
- Pilot reference: `/Users/Cvtot/KJ OS Template/04 Reviews/(C) 2026-05-11 adversarial-review pilot v3 - hireui real monorepo.md`

## Ablation JSON (provisional)

```json
{
  "pilot": "v3.2 adversarial-review hireui",
  "step": 10,
  "status": "PROVISIONAL_2_OF_3_PASSES",
  "passes_complete": [1, 2],
  "passes_blocked": [3],
  "blocker": "B-A18 (codex usage limit, retry after 2026-05-13T01:58Z)",
  "metrics": {
    "pass_1_bmad_adversarial": {
      "wall_clock_seconds": 203,
      "findings": 18,
      "real_bugs_initial": 7,
      "design_challenges": 7,
      "subjective": 4,
      "severity_ceiling": "CRITICAL",
      "approx_output_tokens": 1700,
      "telemetry_logged": true
    },
    "pass_2_codex_neutral": {
      "wall_clock_seconds": 346,
      "findings": 2,
      "real_bugs_initial": 2,
      "design_challenges": 0,
      "subjective": 0,
      "severity_ceiling": "P2",
      "approx_output_tokens": 450,
      "telemetry_logged": true
    },
    "overlap_pass_1_vs_pass_2": "0/18 (0%)",
    "tool_unique_pass_2": 2
  },
  "provisional_conclusion": "Strata appear complementary on harness work; framing-vs-tool decomposition needs Pass 3.",
  "decisions_independent_of_pass_3": [
    "F-01 refinement (slash-vs-Skill dispatch)",
    "C2-1 (skill name/dir normalization)",
    "C2-2 (session_id in telemetry)",
    "F-05 / F-06 / F-10 quick fixes from BMAD"
  ],
  "decisions_blocked_on_pass_3": [
    "Retire BMAD vs codex vs keep both",
    "Cost-per-real-bug final number",
    "Pattern #76 framework-vs-tool decomposition"
  ]
}
```
