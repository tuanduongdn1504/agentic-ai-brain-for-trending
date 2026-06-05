# (C) Command Center build-pilot — session 2 findings (2026-06-02)

> **Date:** 2026-06-02
> **Type:** Pilot session findings / backlog (continuation of `(C) 2026-06-01 Command Center build-pilot handoff (state + worktree dispatch convention).md`).
> **Scope:** Phone-exercise of the v0.7.0 review-gate + v0.7.1 accept flows (handoff §6). Validated the accept flow on real hardware; surfaced two new product findings (filed below) and deferred the reviewer-spawn validation behind an account usage limit.

## Session outcome (scorecard)

| Piece | Status |
|---|---|
| **v0.7.1 `/accept` flow — end-to-end on real phone** | ✅ **VALIDATED** 2026-06-02 |
| Dispatcher → implementer real path + failure-marking | ✅ validated (claims, spawns in correct project cwd w/ bypassPermissions, records session, fails cleanly) |
| **v0.7.0 reviewer spawn (`_run_review` real claude under launchd)** | ⏸ **DEFERRED** — code-confirmed (shares the v0.7.2/3 hardened spawn), empirical run blocked by account usage-limit 429 |
| Dispatcher 429-handling | 🆕 **bug found** — Finding 1 |
| Dispatched-task env scope | 🆕 **finding** — Finding 2 |

**How accept was validated (Option B — no claude spawn, so unaffected by the usage limit):** seeded ops_task #5 directly into `awaiting_approval` with `review_verdict=NOT_VERIFIED` + `output_summary='pilot run OK'`. The bridge pushed a real `❓ REVIEW NEEDED #5` ping (`notification_log` row: `event_type=review_gated`, `event_key=5`, `telegram_message_id=24`, `chat_id=1443607501`). Operator replied `/accept 5` → task `done`, `review_overridden=1`, `output_summary` preserved, `review_verdict` kept for audit, audit activity `task_review_overridden` written (`{"task_id":5,"prior_verdict":"NOT_VERIFIED","review_feedback_first_120":"pilot (simul…"}`), **no re-run**. The v0.7.0 escalation→notification path and the v0.7.1 accept resolution are proven on real hardware.

**Why reviewer-spawn is deferred (Option A):** two real review-mode tasks (#4 on 2026-06-01, #6 on 2026-06-02) both died at the *implementer* stage with an account usage-limit 429 (Finding 1) before the reviewer could run. `_run_review` is code-confirmed to use the identical hardened spawn as the implementer — `CLAUDE_CLI` override + `--dangerously-skip-permissions` + `cwd=_task_cwd()` + `_build_env()` (dispatcher.py:636-650 vs the implementer at :316-328 / :354-368) — so it should work, but it has never run a real claude under launchd. Retry in a free quota window (a usage-limit reset with no parallel heavy Claude sessions, e.g. this Opus session).

---

## Finding 1 — Dispatcher terminal-`fail`s a transient usage-limit 429 (should re-queue / retry)

**Severity:** Medium (operational). On a usage-capped plan, every queued task during a cap window is silently marked `failed` and must be manually re-created.

**Evidence (two independent occurrences):**
- Task #4 (2026-06-01 09:23 UTC) and task #6 (2026-06-02 05:22 UTC): both ended `status=failed`, `error_message=rc=1`, `cost_usd=0`, `consecutive_failures=1`, duration ~1.4–8.9 s, target file never written.
- Implementer claude session `is_error=1`; transcript assistant message: `"error":"rate_limit","isApiErrorMessage":true,"apiErrorStatus":429`, content text `"You've hit your limit · resets <time> (Asia/Saigon)"` (6:30pm on #4, 1:50pm on #6 — the window rolls).

**Root path:** `_run_stream` / `_run_classic` return `ok=False` on rc≠0 (dispatcher.py ~342 / ~368). `run_once` treats a not-`ok` implementer result as a failure → `fail_task(...)` → `status=failed`, `consecutive_failures++`. No distinction between a transient rate-limit and a genuine task failure.

**Proposed fix:** detect the rate-limit/usage-limit signal — parse the stream-json `result` line's `is_error`/`subtype`, or the assistant message's `error":"rate_limit"` / `apiErrorStatus":429` — and treat it as **retryable**: re-queue to `pending` (optionally `scheduled_for` = the parsed reset time, or a backoff) instead of terminal `failed`, and do **not** increment `consecutive_failures` for a 429.

**Relationship:** directly extends backlog item #2 (v0.7.4 `is_error` success-detection — "dispatcher trusts returncode only"). v0.7.4 should not merely parse `is_error`; it should **classify** rate-limit/429 as retryable vs a real error as failed.

**Also affects the reviewer:** a 429 during `_run_review` hits its rc≠0 fail-safe (dispatcher.py ~664) → `MANUAL_VERIFY_REQUIRED` → the task escalates to a human as "unverifiable," when it was merely rate-limited. A 429 in review should be retryable too, not escalate.

---

## Finding 2 — Dispatched headless tasks inherit the operator's full interactive Claude Code environment

**Severity:** Medium (least-privilege / scope + efficiency). Did **not** cause the 429s — surfaced incidentally from the implementer transcripts.

**Evidence:** the dispatched implementer's session transcript (sessions `0d46020d` / `882acb2c`, both run in the project cwd with `permissionMode: bypassPermissions`, `entrypoint: sdk-cli`) contains, before the model call:
- `deferred_tools_delta`: CronCreate/CronDelete/CronList, EnterPlanMode/ExitPlanMode, Monitor, NotebookEdit, PushNotification, RemoteTrigger, Task{Create,Get,List,Output,Stop,Update}, WebFetch, WebSearch, **`mcp__plugin_telegram_telegram__{download_attachment,edit_message,react,reply}`**.
- `mcp_instructions_delta`: `plugin:telegram:telegram`.
- `skill_listing`: 14 skills.

**Root cause:** `_build_env()` (dispatcher.py:80) does `os.environ.copy()` (+ OTEL vars), and the spawn argv sets no `CLAUDE_CONFIG_DIR`, no `--strict-mcp-config`, no MCP/plugin disabling — so the dispatched `claude -p` loads the operator's global `~/.claude` config (MCP servers, plugins, skills).

**Risk:** a `--dangerously-skip-permissions` headless task can reach the Telegram `reply`/`react`/`edit_message` tools, `Cron*` (schedule jobs), `Task*` (spawn agents), and `WebFetch`/`WebSearch` — far beyond what a scoped task runner needs (write files / run project commands). Plus startup latency + token overhead from loading MCP servers + skills on every task.

**Proposed fix:** run the dispatched child with an isolated, minimal config — set `CLAUDE_CONFIG_DIR` to a dedicated dir with no MCP servers/plugins, and/or pass `--strict-mcp-config` with an empty/scoped `--mcp-config`, and restrict allowed tools to what tasks need. Verify normal file-writing tasks still pass (e.g. tasks #2/#3 shape).

---

## Pilot artifacts left in the live install (cleanup pending operator call)

- Skill `cc-review-pilot` (`autonomy=auto`, `review_mode=1`) — **kept** for the deferred Option-A reviewer-spawn retry. Remove with `DELETE FROM skills WHERE name='cc-review-pilot'` when done.
- ops_tasks #4 (`failed`, 429) and #6 (`failed`, 429) — throwaway; deletable.
- ops_task #5 (`done`, `review_overridden=1`) — the accept-flow evidence; keep or delete.

## Retry plan for the deferred reviewer-spawn (Option A)

Re-dispatch a review-mode task assigned to `cc-review-pilot` (criteria designed to escalate — see `/tmp/cc_taskA.json` shape) in a free quota window, and confirm from the backend: implementer succeeds → a **second** claude session is minted (the reviewer) → `review_verdict` is set → `cost_usd` ≈ 2× a single run → task escalates (or completes if VERIFIED). No phone needed; the accept resolution is already proven.
