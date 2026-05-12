# Pilot v3.2 Step 10 — Final ablation analysis (TEMPLATE, fill after Pass 3)

> **Template purpose:** Pass 3 auto-retry lands ~2026-05-13T02:03Z. When it does, the cron task will copy this template to `step-10-final-analysis.md` and fill the `_pending_` placeholders. Operator can then review one finished doc instead of regenerating structure.

## Pilot evaluation summary (≤ 200 words for vault Pattern #76 evidence)

_one-paragraph fill_ — Pattern #76 (Adversarial Subagent Review Architecture at Framework Level) [supported / weakly supported / undermined / inconclusive]. Evidence: on a 61-file 17-commit harness diff, BMAD adversarial mandate produced 18 findings (7+ initial real bugs); codex neutral produced 2 (both real code-level bugs BMAD missed, 0/18 overlap); codex adversarial produced [N] findings ([X]/18 BMAD-overlap, [Y] codex-unique). The framing-vs-tool decomposition reads: [verdict]. Pattern #76 should be [keep staged / promote to active / retire / amend to scope=tool-level only].

## Pass results

| Pass | Stratum | Tool | Wall-clock | Findings | Real bugs (initial) | Severity ceiling |
|---|---|---|---|---|---|---|
| 1 | A baseline | bmad-review-adversarial-general | 203s | 18 | 7 | CRITICAL |
| 2 | B neutral | /codex:review | 346s | 2 | 2 | P2 |
| 3 | B adversarial | /codex:adversarial-review | _N_ s | _N_ | _N_ | _ |

## Cross-pass overlap matrix

| BMAD F-id | Topic | Pass 2 caught? | Pass 3 caught? | Operator-confirmed real bug? |
|---|---|---|---|---|
| F-01 | telemetry asymmetry | NO | _y/n_ | YES (Pass 1 + refined Pass 2) |
| F-02 | Pattern #76 scope mismatch | NO | _y/n_ | _operator triage_ |
| F-03 | B-A17 count=5 doctored | NO | _y/n_ | YES (doc admits) |
| F-04 | Phase 2 vapor | NO | _y/n_ | YES (doc admits) |
| F-05 | mv non-atomic | NO | _y/n_ | YES (verifiable) |
| F-06 | YAML extraction brittle | NO | _y/n_ | YES (verifiable) |
| F-07 | 3 zero-relevance mattpocock skills | NO | _y/n_ | YES (SKILL.md content) |
| F-08 | no audit trail | adjacent (C2-2) | _y/n_ | YES |
| F-09 | gitignore ratchet | NO | _y/n_ | YES (workflow) |
| F-10 | ORIG_HEAD over-fires | NO | _y/n_ | YES (git docs) |
| F-11 | prefix vocab undocumented | NO | _y/n_ | YES |
| F-12 | primary_alternative inconsistency | NO | _y/n_ | YES (file diff) |
| F-13 | commit bundling | NO | _y/n_ | YES (git show) |
| F-14 | thresholds unitless | NO | _y/n_ | SUBJECTIVE |
| F-15 | doc self-inconsistency | NO | _y/n_ | HISTORY |
| F-16 | rubric versioning | NO | _y/n_ | SUBJECTIVE |
| F-17 | dateline omission | NO | _y/n_ | LOW |
| F-18 | mattpocock-handoff scope drift | NO | _y/n_ | LOW |
| **C2-1** | skill name/dir mismatch | — | _y/n if Pass 3 also found_ | YES (verifiable) |
| **C2-2** | telemetry session scoping | — | _y/n if Pass 3 also found_ | YES (verifiable) |
| **C3-N** | _Pass 3 unique findings_ | — | _add rows_ | _ |

## Headline metrics

### Overlap rate (BMAD-vs-codex)

- Pass 2 (neutral) overlap with BMAD: 0/18 = **0%**
- Pass 3 (adversarial) overlap with BMAD: _N_/18 = **_X_%**
- **Δ from Pass 2 → Pass 3:** [adversarial framing closes / does not close] the overlap gap by _X percentage points_

### Codex-unique rate

- Pass 2 codex-unique: 2/2 = 100% (vs BMAD)
- Pass 3 codex-unique vs BMAD: _N_/_total Pass 3_ = _X_%
- Pass 3 codex-unique vs Pass 2: _N_ (does Pass 3 add findings beyond C2-1, C2-2?)

### Cost dynamics

| Metric | Pass 1 BMAD | Pass 2 codex neutral | Pass 3 codex adversarial |
|---|---|---|---|
| Wall-clock (s) | 203 | 346 | _N_ |
| Findings | 18 | 2 | _N_ |
| Real-bugs initial | 7 | 2 | _N_ |
| Cost per finding (s) | 11 | 173 | _N_ |
| Cost per real-bug (s) | 29 | 173 | _N_ |
| Approx output tokens | 1700 | 450 | _N_ |
| Severity ceiling | CRITICAL | P2 | _ |

## Framing-vs-tool decomposition (THE pilot output)

The pilot's central hypothesis: **framework-level adversarial framing** (e.g., BMAD's XML task file with rubric + ≥10 floor) matters more than **tool/model identity** for producing high-finding-density reviews.

### Test design

- Pass 1 = framing ON + BMAD tool
- Pass 2 = framing OFF + codex tool
- Pass 3 = framing ON + codex tool

### Decision tree from observed data

```
                              Pass 3 overlap with BMAD
                              high (>50%)        low (<20%)
Pass 3 findings count   ┌──────────────────┬──────────────────┐
                  high  │  FRAMING DOMINATES│  TOOL DOMINATES   │
                  (>10) │  Pattern #76 ✅    │  but codex catches│
                        │  strongly supported│  different topics │
                        │                    │  Pattern #76      │
                        │                    │  weakly supported │
                        ├──────────────────┼──────────────────┤
                  low   │  CODEX CAN'T     │  CODEX HAS LOW    │
                  (≤5)  │  PRODUCE BREADTH │  CEILING — tool   │
                        │  EVEN WITH FRAMING│  rate-limit       │
                        │  Pattern #76      │  dominates        │
                        │  scope = BMAD-only│  Pattern #76 ?    │
                        │  Stratum B retire │  inconclusive     │
                        └──────────────────┴──────────────────┘
```

### Verdict

_fill after Pass 3_:
- Findings count: _N_ → quadrant row [high / low]
- Overlap with BMAD: _X_% → quadrant column [high / low]
- **Verdict:** [framework framing dominates / tool dominates / codex has low ceiling / scope = BMAD-only]
- **Pattern #76 conclusion:** [supported / weakly supported / undermined / inconclusive — needs more data on framework-level subagent architecture which this pilot did not test]

## Operator decisions enabled by this data

### Tooling

1. **Stratum A (BMAD)** — _keep / amend / retire_ + rationale
2. **Stratum B (codex)** — _keep / amend / retire_ + rationale
3. **Combine BMAD + codex?** Recommended sequencing for future reviews?
4. **Augment BMAD's XML task with code-trace prompts** (to catch the kind of bugs codex caught) — yes/no?

### Pilot output for vault

1. **Pattern #76 update** — promote / retire / amend
2. **Cross-session evidence note** to attach to vault `_patterns/03-active-candidates.md` Pattern #76

### HIR-1162 schema validation

- B-A18 lifecycle (count=1 → resolved without breaching ≥3 threshold) demonstrates: _schema works as designed / needs adjustment_
- Threshold defensibility (3/5) — confirmed by B-A18 not breaching / still untested at threshold
- Audit trail gap (F-08) — resolved by post-pilot fix or accepted as-is

### Skill management infrastructure

- C2-1 (name/dir mismatch) — fix approach confirmed: [normalize frontmatter / glob lookup]
- C2-2 (telemetry session scoping) — same fix as F-08 audit-trail

## Final ablation JSON

```json
{
  "pilot": "v3.2 adversarial-review hireui",
  "step": 10,
  "status": "FINAL",
  "completion_date": "2026-05-13",
  "passes": {
    "pass_1": {"tool": "bmad-review-adversarial-general", "wall_clock_s": 203, "findings": 18, "real_bugs_op_confirmed": "_N_", "severity_ceiling": "CRITICAL"},
    "pass_2": {"tool": "codex:review", "wall_clock_s": 346, "findings": 2, "real_bugs_op_confirmed": "_N_", "severity_ceiling": "P2"},
    "pass_3": {"tool": "codex:adversarial-review", "wall_clock_s": "_N_", "findings": "_N_", "real_bugs_op_confirmed": "_N_", "severity_ceiling": "_"}
  },
  "metrics": {
    "overlap_pass_2_vs_pass_1": "0/18 (0%)",
    "overlap_pass_3_vs_pass_1": "_N_/18 (_X_%)",
    "pass_3_codex_unique_vs_pass_1": "_N_",
    "pass_3_codex_unique_vs_pass_2": "_N_",
    "framing_dominates_tool": "_yes/no/partial_",
    "pattern_76_verdict": "_supported / weakly supported / undermined / inconclusive_"
  },
  "decisions": {
    "retire_bmad": "_yes/no/keep_",
    "retire_codex": "_yes/no/keep_",
    "combine_strategy": "_describe_",
    "augment_bmad_with_code_trace": "_yes/no_",
    "pattern_76_action": "_promote/retire/amend_",
    "hir_1162_schema_validated": "_yes/needs-adjustment_"
  },
  "post_pilot_fix_sprint": "see .pilot-log/post-pilot-fix-sprint.md (after Step 10 closes)",
  "vault_propagation": {
    "pattern_76_evidence_note": "needs to be attached to vault _patterns/03-active-candidates.md",
    "pilot_log_copy_to_vault": "copy .pilot-log/* to vault pilot-log/ per Hybrid Option 3+5"
  }
}
```

## Vault propagation

When Step 10 closes:
1. Copy `.pilot-log/*` to `/Users/Cvtot/KJ OS Template/03 Projects/_pilots/2026-05-11 adversarial-review-v3-hireui/pilot-log/`
2. Append Pattern #76 evidence section to `/Users/Cvtot/KJ OS Template/_patterns/03-active-candidates.md` Pattern #76 entry — link to `.pilot-log/step-10-final-analysis.md`
3. Update vault `_state/pilot-ranking-2026-05-07.md` if this pilot's outcome affects next-pilot ordering
4. Notify Session B (vault) for any cross-session decisions (F-02, F-07)
