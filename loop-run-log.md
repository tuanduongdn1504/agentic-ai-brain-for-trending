# loop-run-log.md — Storm Bear vault

Append-only run history (loop-engineering v189 convention, adapted from `templates/loop-run-log.md.template` @ `f18df04`). One JSON object per line per run. Fields: `run_id` (ISO8601), `pattern`, `duration_s`, `items_found`, `actions_taken`, `escalations`, `tokens_estimate` (main-loop + workflows, estimate not metered), `outcome` (`no-op | report-only | fix-proposed | escalated`). Prune entries >90 days at audits. Entries marked `"backfilled": true` were reconstructed from session records at adoption time (2026-07-02).

```jsonl
{"run_id": "2026-07-02T03:30:00Z", "pattern": "wiki-ship", "duration_s": 5400, "items_found": 1, "actions_taken": 1, "escalations": 0, "tokens_estimate": 2400000, "outcome": "fix-proposed", "note": "v189 loop-engineering ship on wiki/v189-loop-engineering (wf_fbe77308-374 ~1.96M + main loop); operator merged", "backfilled": true}
{"run_id": "2026-07-02T04:30:00Z", "pattern": "pilot-a3-b5", "duration_s": 1800, "items_found": 16, "actions_taken": 0, "escalations": 2, "tokens_estimate": 150000, "outcome": "report-only", "note": "A3 gap-map + B5 loop-audit (vault 25/L0, hireui 32/L0); 2 escalations to operator: (C)-prefix waiver + I-8 install gate; read-only, zero installs", "backfilled": true}
{"run_id": "2026-07-02T05:00:00Z", "pattern": "pilot-c-block", "duration_s": 900, "items_found": 0, "actions_taken": 7, "escalations": 0, "tokens_estimate": 60000, "outcome": "fix-proposed", "note": "C9-C14: five convention files + loop-verifier agent + loop-triage/loop-budget skills on pilot/v189-loop-a3-b5; operator merges"}
```
