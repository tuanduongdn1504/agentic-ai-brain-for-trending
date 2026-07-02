# loop-budget.md — Storm Bear vault

Token caps + kill switch (loop-engineering v189 convention, adapted from `templates/loop-budget.md.template` @ `f18df04`). **Rule (binding, from the loop-budget skill): at ≥80% of a cap → report-only mode (no sub-agent fan-outs, no fixes); at ≥100% OR `loop-pause-all` present in STATE.md → exit immediately with a one-line note in STATE.md.** Estimates count main-loop + subagent/workflow tokens.

## Caps

| Loop | Unit | Max runs | Max tokens | Max workflow/sub-agent fan-outs |
|---|---|---|---|---|
| Wiki-ship (v2.6 routine) | per ship | 1 ship/session | **3M soft cap** (recent ships: ~1.0–2.0M workflow + main loop) | 1 read-only research workflow (≤16 agents) |
| Pilot runs (A/B/C/D/E methods) | per day | 4 | 1M | 1 |
| Autopilot-research | per day | 2 sessions | 1.5M | per its own repo's rules |
| Ad-hoc `/loop` (session) | per day | — | 500k | 0 above L1 |
| Memory consolidation | per week | 1 | 200k | 0 |

## Kill switch

- Add a line `loop-pause-all` to STATE.md → High Priority → every loop exits immediately on its next check.
- Resume: operator removes the line.

## On exceed

1. Stop fan-outs; finish in report-only mode. 2. Append the event to `loop-run-log.md` (`outcome: "escalated"`, note the cap). 3. Tell the operator in the session summary.

## Alerts This Period

—
