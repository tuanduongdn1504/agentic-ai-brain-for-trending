# Pilot v3.2 Step 7 — adversarial-review three-pass comparison

> **Local working log.** Gitignored (per `.gitignore` line 53 `.pilot-log/`).
> Copy to vault `pilot-log/` at end of pilot (Hybrid Option 3+5 architecture):
> `/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log/`

## Pass status

| Pass | Stratum | Tool | Status | Findings |
|------|---------|------|--------|----------|
| 1 | A baseline | `bmad-review-adversarial-general` (Skill tool) | ✅ DONE 2026-05-12T07:13:11Z–07:16:34Z (3m 23s) | 18 |
| 2 | B neutral | `/codex:review --base agent-dev` (Skill-dispatched) | ✅ DONE 2026-05-12T07:24:07Z–07:29:53Z (5m 46s) | 2 |
| 3 | B adversarial | `/codex:adversarial-review --base agent-dev` (direct codex-companion.mjs after retry) | ✅ DONE 2026-05-13T02:24:39Z–~02:46Z (~20m) — B-A18 resolved | **17** |

## Why 3 passes

- **Pass 1 (BMAD Stratum A)** = baseline cynical review from the existing harness. Establishes "what BMAD catches on this diff."
- **Pass 2 (Codex neutral)** = control. Reveals whether finding gaps in Stratum B are because the *tool* is weaker OR because the *adversarial framing* is what produces findings.
- **Pass 3 (Codex adversarial)** = main comparator. Direct match-up against Pass 1 under the same adversarial mandate, different tool/model.

## Step 10 ablation will compare

Per-pass:
- Wall-clock duration
- Approx token cost
- Distinct topics raised
- Real-bug vs design-challenge vs subjective classification
- Operator-confirmed real bugs vs false positives

Cross-pass:
- **Overlap rate** between BMAD findings and codex findings (sanity: do both tools see the obvious stuff?)
- **Codex-unique findings** (does codex catch what BMAD missed?)
- **BMAD-unique findings** (what does codex miss that BMAD got?)
- **Cost per confirmed real bug** = (wall_clock × token_cost) / real_bugs

## Files in this directory

| File | What |
|------|------|
| `README.md` | this file — overall pilot status |
| `pass-1-bmad-adversarial.md` | Pass 1 full findings + metadata (18 findings) |
| `pass-2-codex-review.md` | Pass 2 full capture (2 findings) |
| `pass-3-codex-adversarial.md` | Pass 3 full capture (17 findings) + full match-up matrix |
| `step-10-final-analysis.md` | Step 10 ablation analysis FINAL (all 3 passes complete) |
| `step-8-triage.md` | operator triage worksheet (37 findings, Session B's 4 cross-session decisions integrated) |
| `pattern-76-evidence-2-of-3.md` | Pattern #76 structural evidence note (still applicable post-Pass 3) |
| `post-pilot-fix-sprint.md` | sequenced backlog after Step 10 closes (revised with Pass 3 findings) |

## E3 telemetry note

Per BMAD Pass 1 finding F-01: E3 PostToolUse hook only fires on `Skill` tool calls. Pass 1 was captured (`bmad-review-adversarial-general` row at `07:13:35Z` in `.cm/memory/skill-invocation-log.json`). **F-01 partially refuted in Pass 2:** when codex slash commands are dispatched via the Skill tool (e.g., `Skill(skill="codex:review")`), E3 DOES fire — the asymmetry only affects direct `/slash` invocations from the user. Pass 2 + Pass 3 attempts both produced Skill log entries; for findings comparison, the slash-command-vs-Skill-dispatch path matters.

## Pass 3 retry success (2026-05-13)

Pass 3 first attempt 2026-05-12T07:30:47Z failed at 07:32:17Z with codex usage limit. B-A18 filed (count=1, attention_tag=null). Retry 2026-05-13T02:24:39Z in Session A (after operator checkout to pilot branch) completed ~20m wall-clock with **17 findings (7 HIGH + 9 MEDIUM + 1 LOW; 12 real bugs + 5 design challenges)**. **44% overlap with BMAD Pass 1** + **9 codex-unique findings including 6 HIGH real bugs BMAD missed entirely**. B-A18 resolved 2026-05-13T02:46Z. HIR-1162 schema runtime exercise: lifecycle clean (count=1 attention_tag=null throughout, no threshold breach). Full Step 10 ablation analysis: `.pilot-log/step-10-final-analysis.md`.

## After all 3 passes

1. Operator triages each finding as: real-bug / design-challenge / subjective / false-positive
2. Build the match-up matrix in `pass-3-codex-adversarial.md`
3. Compute headline metrics (overlap rate, codex-unique rate, cost-per-bug)
4. Write Step 10 ablation summary
5. Copy `.pilot-log/*.md` to vault `pilot-log/`
6. Decide pilot conclusion: keep both Stratum A + B? Retire one? Augment?

## Open items from Pass 1 worth following

These are the Pass 1 findings that should drive immediate follow-up commits regardless of Step 10's verdict:

- **F-05** mv non-atomic — quick shell fix
- **F-06** YAML extraction brittle — replace grep+sed with `yq` or python yaml
- **F-10** ORIG_HEAD over-fires — guard with `.git/MERGE_HEAD` check
- **F-12** mattpocock-handoff `primary_alternative: N/A` — update SKILL.md frontmatter
- **F-03** B-A17 count=5 doctored — schema split or rename field

The CRITICALs F-01/F-02/F-04 require operator-level decisions (telemetry redesign, pilot scope, Phase 2 hook commitment) so they're not just "fix and commit" — they're "discuss and decide."
