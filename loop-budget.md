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

- 2026-07-03 · wiki-ship v191 (AI-For-Beginners): crossed the 80% line of the 3M soft cap (~2.5–2.7M est., workflow 2.08M + main loop) during doc-writing → self-throttled per the binding rule: no further fan-outs; the optional loop-verifier agent SKIPPED (inline hand-verification stands — every corpus claim hand-grepped); ship completed as the operator-requested deliverable under the 3M soft cap. Re-check the v191 claim set at the ~v192 audit.
- 2026-07-09 · wiki-ship v200 (career-ops, THE 200th LLM-WIKI): crossed the 80% line of the 3M soft cap (~2.9M est., workflow 2.45M [13-agent Haiku] + main loop) during doc-writing → self-throttled per the binding rule + the v191 precedent: no further fan-outs; the optional loop-verifier agent SKIPPED (inline hand-verification stands — 7 confabulations caught by hand; all corpus/collision/identity/mint claims + all load-bearing quantitative facts hand-verified); ship completed as the operator-requested deliverable under the 3M soft cap. Re-check the v200 claim set (the 1 NEW §C standalone + its NO-MINT alternative) at the badly-overdue ~v192 audit.
- 2026-08-18 · wiki-ship v239 (dsh-web-ui): **within cap, no throttle.** One read-only research workflow (the 1 allowed fan-out) — **16 agents, 0 errors, ~1.73M subagent tokens, 352 tool uses, 411s** — plus main-loop hand-verification. Est. total ~2.0–2.2M of the 3M soft cap (~70%), **below the 80% report-only line**; no second fan-out, no loop-verifier agent needed (inline hand-verification stands — all corpus/collision/identity/mint claims and every load-bearing quantitative fact hand-verified; six errors caught, two of them mine). ⭐ **Infrastructure note: the `Workflow` tool worked for the first time since ~v200** — v238's ship failed with all 18 agents *prompt-too-long* at ~207.2K vs a 200K limit, and the v238 shim compaction (537,679 → ~132KB) was the fix; confirmed in a **fresh session**. Shim ~142KB after this ship. The `_state`/shim size discipline is load-bearing infrastructure — re-growing it past the subagent-context floor re-breaks fan-out.

- **2026-08-26 · wiki-ship v281 (ComfyUI): ⚠️ CAP EXCEEDED — ~5.73M subagent tokens against the 3M per-ship soft cap (~191%).** Cause: the 20-agent deep-dive workflow (`wf_718ce74b-d4a`) ran while **the machine went to sleep mid-run**; agents stalled and retried across **8.6 wall-clock hours** — 48 agent starts for 20 planned slots, **9 of 15 tracked agents errored** (stalls, StructuredOutput retry-cap), 6 completed. The overrun is retry/stall waste, not analysis depth. **Action taken per the binding rule ("On exceed"): all fan-outs stopped, ship finished in report-only mode on hand verification, escalated here and in `loop-run-log.md` (`outcome: "escalated"`), and disclosed to the operator in the session summary and inside the ship's own METHOD sections.** Coverage held because the five dimensions that failed (ai-review-layer, security, ci-surface, claims-audit, architecture) had already been hand-covered before launch. **Prevention for next ship:** cap wall-clock per fan-out and treat a stalled agent as fatal rather than retrying 6×; a sleeping host is now a known and expensive failure mode.

- **2026-09-03 · wiki-ship v282 (scroll-craft): SELF-THROTTLED — crossed the 80% line of the 3M per-ship soft cap (~2.6M est.: fleet 2.238M + main loop).** One read-only research workflow (the 1 allowed fan-out) — **17 agents, 0 errors, 3 empty (StructuredOutput), ~2.238M subagent tokens, 396 tool uses, 1,050 s** — plus main-loop hand verification. **Action taken per the binding rule: report-only mode entered — no further fan-outs, and the optional loop-verifier agent SKIPPED** (inline hand-verification stands, consistent with the v191/v200/v239 precedent). **Coverage held:** the three empty fleet dimensions (`skill-procedure`, `verify-harness`, `engine`) had **already been hand-covered before launch**, and every corpus/collision/identity/mint claim plus every load-bearing quantitative fact was verified by hand from the clone. ⭐ **The v281 prevention worked:** wall-clock was 17.5 minutes against v281's 8.6 hours, no agent stalled, and 0 agents errored — the machine did not sleep and no agent was retried into the ground. Shim ended at **198,100 bytes** (from 196,056) — kept under the 200KB budget by compacting the v273 head block, since re-growing the shim past the subagent-context floor re-breaks fan-out (the v238 lesson).
