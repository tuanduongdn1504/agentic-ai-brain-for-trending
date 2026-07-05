# TNT we-event harness — operational mechanics (12 components, 2 loops, 3 gates)

> The operational-schema article for [[tnt-cursor-cli-factory-anchor]]. Everything below is repo ground truth (`projects/ai-harnessed_we-event-app/ai-harness/`, fetched 2026-07-05; extracts in `raw/2026-07-05-tnt-we-event-repo-extracts/repo/`).
> Substrate: **bash + jq + one Node script + JSON config + markdown prompts. Zero frameworks.** Cursor CLI (`agent -p --force --output-format stream-json`) is the only AI dependency; Playwright MCP the only MCP.

## Component map (from HARNESS-DESIGN.md — his own 12-component decomposition)

| Component | Implementation |
|---|---|
| Model | `config/models.json` — all four roles default `auto`; per-role env overrides (`AIH_MODEL`, `AIH_REVIEWER_MODEL`, …) |
| Prompt | 4 thin role prompts (`agents/*.prompt.md`) with `{{SLICE_*}}` template variables; **policy lives in config, not prompts** |
| Context | `config/context-map.json` — per-agent-type `alwaysRead` (2–4 docs) + per-slice doc list (3–4 docs). Implementer is told "do NOT load the entire docs/ tree" |
| Tools | Cursor CLI + Playwright MCP (`.cursor/mcp.json`, headless, output-dir pinned into `generated/runs/`) |
| Workflow | `workflows/ralph-loop.json` + `testgen-loop.json` — max 30 iterations, `commitOnPass`, branch prefix `aih/` |
| Memory/State | `state/progress.md` (append-only run ledger) + `state/guardrails.md` ("Ralph Signs" lessons) + `whole-app-backlog.json` (26 slices, 4 phases: infra 4 / backend 10 / frontend 9 / testing 3) |
| Test cases | 66 JSON artifacts in `docs/test-cases/items/<tag>.json` keyed by requirement tag (73 tags: AC-01..17, FR-01..36, BR, NFR) + `test-case-index.json` state |
| Validation | `run-checks.sh` (computational) + `run-browser-test.sh` (Playwright MCP gate) |
| Guardrails | `state/guardrails.md` + `forbiddenPatterns` regex in ralph-loop.json |
| Observability | `generated/runs/<timestamp>-*.json` + `loop.log` |
| Feedback loops | failed gate → guardrail append → **prior-failure summaries injected into next implementer prompt** (`build-prompt.sh` → `build_implementer_prior_gate_feedback()`) |
| Human review | `workflows/human-review-checklist.md`; `mergeReady` slices demand `HUMAN_REVIEW_PASS <id>` sign-off |

## The Ralph loop (one iteration, `ralph-once.sh`)

```
pick slice (deterministic: lowest priority with passes:false, jq sort — no randomness)
→ doc-drift check (EVERY iteration, per referenced tag)
→ test-case gate (optional|required mode)
→ implementer agent (fresh context, NO --resume; state on disk + git)
→ computational checks (run-checks.sh)
→ browser functional test (frontend/test slices; Playwright MCP)
→ AI review (read-only static)
→ mark passes:true → append progress → git commit "aih: complete slice <id>" (--no-verify)
→ if mergeReady: banner HUMAN REVIEW REQUIRED
```

Three role-differentiated Cursor invocations (lib/common.sh): implementer plain; **reviewer `--mode plan --trust`** (Cursor plan mode forbids edits — read-only enforced at CLI level, plus MUST-NOT prompt boundaries); **tester `--trust --approve-mcps`** (browser only). Reviewer prompt: *"Trust `pass: true` on bundled checks — do not re-validate by execution"* — evidence bundling (git diff 50KB head + changed files + checks JSON + browser-test JSON) instead of privilege.

## The TestGen loop (separate, parallelizable)

```
pick requirement tag from backlog acceptance-union where index not current
→ doc fingerprint (SHA256 over sorted paths + file contents, resolved via testgen-docs-map.json)
→ testgen agent writes docs/test-cases/items/<tag>.json ONLY (schema-validated + traceability-checked)
→ sync slice metadata → mark tag current → commit (TestGen-owned paths only)
```

- TestGen emits **only integration/e2e/browser layers**; unit tests are implementer-owned (colocated `*.test.ts` + `testRequirements`). Clean generation/authorship boundary.
- **12-technique coverage taxonomy** baked into the prompt + schema enum (scenario-matrix, flow-a/b/c lifecycle, module-integration, http-contract, rbac-negative, pagination, state-transition, browser-journey, concurrency, boundary-error) + a mandatory coverage self-check before `TESTGEN_DONE`. Test quality is *specified*, not hoped for.
- **Doc drift**: editing a doc changes its fingerprint → `check-test-case-drift.sh` resets the tag to `current:false` AND flips `passes:false` on every slice whose acceptance references it → both loops re-converge. **Docs are the single source of truth with deterministic invalidation** — SDD enforced by `shasum`, not by discipline.
- Ad-hoc lane: `aih:testgen:enhance -- FR-08 "free-text instructions"` — human-guided regeneration without waiting for drift.

## Signal protocol + process control (stream-agent-output.js)

- Typed end signals: `SLICE_DONE/SLICE_BLOCKED/REVIEW_PASS/REVIEW_FAIL/BROWSER_TEST_PASS/FAIL/TESTGEN_DONE/BLOCKED/COMPLETE/HUMAN_REVIEW_PASS`.
- Detection = regex scan over the **trailing 4KB** of streamed output (`SIGNAL_SCAN_TAIL_CHARS=4096`); on signal → grace timer (`signalGraceMs` 15s) → SIGTERM tree → SIGKILL. Dual watchdog: **idle timeout 5 min** (stream silence) + **max wall 1h**, each polled at 5s.
- Why this exists: Cursor's `-p` mode has community-documented hangs (never exits) — the watchdog + signal-grace design is a *practitioner mitigation for a real platform reliability gap*, not overengineering. Timeout → guardrail append → loop exits nonzero.

## Forbidden-patterns gate (declarative anti-slop)

`ralph-loop.json → computationalChecks.forbiddenPatterns`: regexes with scoped paths + messages — in-memory Map repos, SQLite (Postgres-via-Compose mandated), `mockEvents` fixture arrays in pages, `lorem ipsum`, demo copy. Runtime validation: DB health via Compose, API `GET /api/v1/health` expect `{status:ok, db:connected}`, web HTTP 200. The persistence policy is a **hard fail, in config** — the "no mock data" rule other corpus speakers state as advice is here machine-enforced.

## Known weaknesses (verified, not hypothetical)

1. **4KB tail-scan**: a signal emitted >4KB before end-of-stream is missed → timeout path (CONFIRMED from source).
2. **context-map paths are not existence-validated** at prompt-build time — a renamed doc silently vanishes from agent context (REFUTED-claim inversion: no validation step exists).
3. **Preview-stack restart failure logs WARN but does not abort** the browser-test path (hesd variant common.sh) — a down stack can surface as confusing browser-test failures.
4. `testgen-docs-map.json` is **manually maintained** — new tags need a human routing rule (no planner regenerates it).
5. Guardrails file accumulates noise (dozens of duplicate "checks failed — see file" lines from a bootstrap thrash-loop) alongside genuinely distilled lessons — no compaction step. Cf. consolidation-gate designs in [[external|Storm Bear: agent-memory-architecture]].
6. Reviewer read-only is best-effort (plan mode + prompt), not sandboxed.

## Key takeaways

- **Determinism-first**: slice pick, drift detection, gate ordering, signal handling, commit policy — all code; the model only implements/tests/reviews. The cleanest Rule-5 ("if code can answer, code answers") instantiation in the individual-scale layer.
- **Fresh context per iteration + state on disk/git** — same design conclusion as Archon's fresh-context⇒artifact-driven and Pocock's blank-slate reset, reached independently.
- The feedback loop is *specific*: latest failed run JSONs are summarized and injected into the next prompt — failure information survives the context reset **without** resuming the transcript.
- Thin prompts / fat config: role prompts are ~50–90 lines; policy (patterns, gates, timeouts, models) lives in versioned JSON.
- Portable pieces requiring nothing but bash+jq: signal-tail-scan watchdog, doc-fingerprint drift reset, forbidden-patterns config gate, prior-failure prompt injection, human-review checklist w/ typed sign-off.

## Related

[[tnt-cursor-cli-factory-anchor]] · [[tnt-factory-run-empirics]] · [[tnt-vs-corpus-positioning]] · [[archon-workflow-primitives]] (the framework-shaped sibling of these mechanics) · [[anthropic-large-codebases-anchor]] (7-component vs his 12-component decomposition)
