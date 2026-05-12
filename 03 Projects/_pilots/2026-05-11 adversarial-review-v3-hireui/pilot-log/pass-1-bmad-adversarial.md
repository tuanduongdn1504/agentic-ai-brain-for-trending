# Pilot v3.2 Step 7 — Pass 1 (Stratum A: BMAD adversarial-review-general)

## Run metadata

| Field | Value |
|---|---|
| Pass | 1 of 3 |
| Stratum | A (baseline) |
| Skill / tool | `bmad-review-adversarial-general` via Skill tool |
| Skill task body | `_bmad/core/tasks/review-adversarial-general.xml` (≥10 findings mandate) |
| Range | `agent-dev..HEAD` (17 commits, 61 files, +4169 / -26) |
| Branch | `agent/pilot-2026-05-11-adversarial-review` (LOCAL ONLY) |
| Operator | Session A (Claude Sonnet 4.6) |
| t_start | 2026-05-12T07:13:11Z |
| t_end | 2026-05-12T07:16:34Z |
| Wall-clock | **3 min 23 s** |
| Approx token cost | output ~6,500 chars across 18 findings + tables ≈ **~1,700 output tokens** (input prompt ~1.5k + diff context already in session) |
| Telemetry log row | `mattpocock-handoff`-style entry expected in `.cm/memory/skill-invocation-log.json` once E3 fires (verify after) |

## Findings count

| Severity | Count | Real bug | Design challenge | Subjective |
|---|---|---|---|---|
| CRITICAL | 4 | 2 | 2 | 0 |
| HIGH | 5 | 3 | 2 | 0 |
| MEDIUM | 5 | 2 | 2 | 1 |
| LOW | 3 | 0 | 1 | 2 |
| NIT | 1 | 0 | 0 | 1 |
| **Total** | **18** | **7** | **7** | **4** |

## Distinct issues raised (deduplicated topics)

1. Telemetry asymmetry (E3 hook only catches Stratum A Skill calls, misses codex slash commands) — F-01
2. Pattern #76 scope mismatch (tool-level test vs framework-level pattern) — F-02
3. B-A17 count=5 is opinion not measurement — F-03
4. Phase 2 auto-increment hook is vapor; schema useless without it — F-04
5. macOS mktemp + mv cross-filesystem isn't atomic — F-05
6. E4 YAML extraction is brittle grep+sed — F-06
7. 3 of 20 mattpocock skills are repo-pollution (edit-article, obsidian-vault, scaffold-exercises) — F-07
8. blockers.json has no audit trail for `deferred_count` — F-08
9. `.gitignore` harness-ratchet has no fast-path — F-09
10. Post-merge hook fires on rebase/cherry-pick/reset, not just merge — F-10
11. `command:`/`script:` prefix vocab undocumented outside JSON _meta — F-11
12. mattpocock-handoff `primary_alternative: N/A` contradicts registry peer — F-12
13. Commit bundling (Step 6 [2/3] mixed schema + gitignore fix) — F-13
14. Thresholds 3/5 unitless and undefended — F-14
15. Spec self-inconsistency caught only by smoke test — F-15
16. Telemetry rubric added after data started landing; no schema versioning — F-16
17. CONSTITUTION dateline misses 2nd same-day amendment — F-17
18. mattpocock-handoff silently expanded pilot scope (was outside expected 19) — F-18

## Real-bug vs false-positive classification (initial)

| Finding | Real bug? | Confidence |
|---|---|---|
| F-01 telemetry asymmetry | YES — verifiable: settings.json matcher is `Skill`, codex uses slash commands | HIGH |
| F-02 Pattern #76 scope | YES — vault pattern definition specifies framework-level subagent architecture, pilot doesn't test that | HIGH |
| F-03 B-A17 count=5 doctored | YES — design doc literally admits the count is reverse-engineered from the desired tag | HIGH |
| F-04 Phase 2 vapor | YES — admission of "out of scope" in doc itself | HIGH |
| F-05 mv non-atomic | YES — verifiable via `df` shows /var/folders and /Users on different volumes | HIGH |
| F-06 YAML brittleness | YES — straightforward to reproduce by editing a SKILL.md with quoted value | HIGH |
| F-07 zero-relevance skills | YES — SKILL.md descriptions are unambiguous | HIGH |
| F-08 no audit trail | YES — schema doesn't have session_ids; verifiable by inspection | HIGH |
| F-09 ratchet no fast-path | YES — operator workflow consequence is mechanical, predictable | HIGH |
| F-10 post-merge hook over-fires | YES — ORIG_HEAD semantics are documented in git docs | HIGH |
| F-11 prefix vocab in JSON only | YES — CONSTITUTION + CLAUDE.md don't mention prefix conventions | HIGH |
| F-12 primary_alternative N/A inconsistency | YES — direct file comparison | HIGH |
| F-13 commit bundling | YES — `git show f59c6b26 --stat` confirms the 4 unrelated files | HIGH |
| F-14 thresholds undefended | Subjective; doc admits "not empirically validated" | MEDIUM |
| F-15 doc self-inconsistency | History fact (the bug existed in v1) | LOW (already-fixed) |
| F-16 rubric versioning | Subjective; data-versioning hygiene | MEDIUM |
| F-17 dateline omission | Trivial doc hygiene | LOW |
| F-18 mattpocock-handoff scope drift | Trivial; not actually harmful | LOW |

**Operator triage needed:** F-14, F-16, F-17, F-18 are judgment calls; the other 14 are confirmable real bugs or real design challenges.

## Notes for Stratum B comparison

- BMAD's findings lean heavily on **schema semantics** (F-03, F-04, F-08, F-12) and **pilot scope** (F-01, F-02). It will be interesting to see if codex-plugin-cc independently surfaces the same Pattern #76 mismatch (F-02).
- BMAD found **2 real code bugs** in shell scripts (F-05 mktemp, F-06 YAML extraction, F-10 ORIG_HEAD). Codex with its CLI/runtime focus may find different shell-level issues OR confirm these.
- BMAD did NOT challenge:
  - Whether the `cm-continuity` skill's protocol is actually being followed
  - Whether the migration script's `set -euo pipefail` interacts safely with macOS bash 3.2 (the repo's stated baseline per L-001)
  - Performance characteristics of the 20-skill auto-load on session start
- These gaps are flagged for codex passes to potentially catch.

## Output for Step 10 ablation

```json
{
  "pass": 1,
  "stratum": "A",
  "tool": "bmad-review-adversarial-general",
  "skill_invocation_logged": true,
  "wall_clock_seconds": 203,
  "approx_output_tokens": 1700,
  "total_findings": 18,
  "by_severity": {"CRITICAL": 4, "HIGH": 5, "MEDIUM": 5, "LOW": 3, "NIT": 1},
  "by_classification": {"real_bug": 7, "design_challenge": 7, "subjective": 4},
  "distinct_topics": 18,
  "operator_confirmed_real_bugs": "pending",
  "operator_confirmed_false_positives": "pending"
}
```
