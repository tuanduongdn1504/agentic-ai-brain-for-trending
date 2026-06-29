# (C) Autopilot Loop — 2026-06-20-14 (claude-code-observability)

> **Trigger:** manual — operator submitted a single video URL with the ask "build knowledge from this video + **double deep-dive into the original resource** + show **many pilot methods** for my working flow"
> **Topic:** claude-code-observability (NEW)
> **Started:** ~2026-06-20T12:58+07:00
> **Ended:** ~2026-06-20T14:1x+07:00
> **Duration:** ~75 min (incl. a 12-min background Workflow)
> **Ultracode:** ON (Workflow-orchestrated, exhaustive)

## Source

- Primary video: **dITtLiC9FzM** — Mansel Scheffel (atomicOps), "Claude Code + OpenTelemetry = Claude Command Center" (2026-04-22, 15:54, 15,211 views). **Third-party creator, NOT first-party Anthropic.**
- WebFetch failed (YouTube SPA) → `yt-dlp 2026.06.09 --write-auto-subs --sub-langs en-orig,en` → `bin/vtt-to-md.py` → 553 cue / 35-para / ~4,016-word transcript, **read in full**. Raw: `raw/2026-06-20-claude-code-otel-command-center.md` (25K incl. description).
- Path 5 (yt-dlp-only); no NotebookLM (primary-source-first).

## Method

1. Identified video + pulled transcript + description (the description carried the timestamps + the gated Google-Drive/Skool "build your own" prompt).
2. Read full transcript → mapped the real (contrarian, observability-first) thesis + the two data sources (OTEL + JSONL).
3. **Workflow `wf_5398ccab-88a`** (29 agents): 6 original-resource deep-dives (claude-code-guide for the Claude Code OTel + JSONL ones) → 10 draft→verify pipelines (each article adversarially verified against the research findings + transcript) → critic sweep + provenance + pilot-seed.
4. **Follow-up first-party fact-check** (claude-code-guide agent) on contested facts → caught an over-correction.
5. Applied critic + fact-check fixes by hand; wrote `_index` + a corrected `source-provenance` + the pilot menu; updated `_master-index` + `_inventory`.

## Per-cycle metrics

| Cycle | Sources | Gaps before | Gaps after | Ratio |
|-------|---------|-------------|------------|-------|
| 1 | 1 video + 6 originals deep-dived | 1 (cold-start) | 0 | 1.0 |

`gaps_closed_ratio` = **1.0** (cold-start — the topic itself was the gap; now 12 files, fully cross-linked, provenance + pilot complete). Stop reason: target reached in 1 cycle (single-video deep-dive scope).

## Wiki articles created (12 files — `wiki/claude-code-observability/`)

- `_index.md` (NEW topic) · `overview.md` · `claude-code-opentelemetry.md` (load-bearing) · `opentelemetry-standard.md` · `observability-backend-stack.md` · `cost-cache-token-metrics.md` · `mcp-and-skill-cost-metrics.md` · `task-queue-scheduling-telegram-hitl.md` · `jsonl-logs-and-native-dashboard.md` · `code-execution-mcp-workaround.md` · `video-to-original-crosswalk.md` · `source-provenance.md`
- `_master-index.md` UPDATED (+claude-code-observability, with the Rule-7 reconciliation note vs agent-dashboard-os).
- `output/(C) 2026-06-20-claude-code-observability-pilot-methods.md` — **18 ranked methods** (C personal `~/.claude` / A autopilot-vault / B hireui-Goal-#2 / D Scrum) + skip-list + skeptic reframe.
- `raw/_inventory.md` row → `compiled`.

## Verify corrections (Rule 12 fail-loud)

- **Over-correction caught + fixed (the important one):** a research agent hit a 404 on the `/cost` docs page and concluded "no `/cost`/`/usage`/`/status` commands exist." **Wrong** — `/cost`, `/usage`, `/stats` + the statusline DO exist (local/account-fed, **not** OTEL-fed); there's also a Console **Analytics dashboard** for Team/Enterprise. What's true: no built-in *customizable OTEL-fed panel dashboard*. Fixed across 4 articles + provenance via a first-party fact-check.
- **"Previously enterprise-only"** OTEL plan history → **unconfirmed** (no docs evidence; flagged).
- **Single-source-flagged metric names:** `claude_code.pull_request.count`, `claude_code.code_edit_tool.decision`, the token.usage `type` attribute key, and the `CLAUDE_CODE_OTEL_HEADERS_HELPER` var name — from the first-party docs fetch but not re-confirmed by the cross-check (docs truncation).
- **Cache-read cost** fixed from a stray "50%" to **~0.1× (≈90% off)** (Rule 7 — matched the verified [[claude-api-cost-optimization]] figure).
- **Community stacks:** only `ColeMurray/claude-code-otel` + `ryoppippi/ccusage` confirmed real; 4 others demoted to "unverified leads" + fabricated "last commit 2026-05-XX" / "Maintenance: Active" placeholders removed.
- **Link hygiene:** fixed mis-applied cross-vault forms (`[[external|Storm Bear: …]]` / `[[../../topic]] (Storm Bear curated wiki)`) — these are *same-wiki* autopilot topics → `[[../topic/_index]]`. Final sweep: 0 bare cross-topic links, 0 stray files (critic confirmed).
- **Creator's own builds flagged unverifiable:** command-center UI, "IQ agent" router, posture/context/security skills, the paywalled Google-Drive/Skool "build your own" prompt.

## Cross-topic wiring

Cross-linked to: claude-api-cost-optimization (the levers this measures) · agentic-analytics-harness (observability-over-scorecards) · telegram-remote-control-stack (HITL/alerts, pilot-verified) · prompt-evaluation (trace triage) · claude-cowork (the "just use Cowork" stance) · claude-code-hooks · autonomous-loops-human-in-the-loop · claude-skills · harness-engineering · agent-dashboard-os (**Rule-7 reconciliation** — this concretizes that abstract landscape).

## Workflow usage

`wf_5398ccab-88a`: 29 agents, ~1.585M subagent tokens, 268 tool uses, ~12 min. + 1 follow-up claude-code-guide fact-check (~49K tokens). 6/6 research agents returned; 10/10 articles written+verified; critic reported 3 issues (all fixed) + 0 stray files.

## Top residual / open items (not blocking)

1. The 3 single-source metric names + `otelHeadersHelper` var name should be re-confirmed against a live `/usage`/backend (flagged inline + in provenance).
2. The OTEL "previously enterprise-only" history remains unconfirmed.
3. 4 community-stack repos are unverified leads (only ColeMurray + ccusage confirmed).

## Suggested next action

Operator pilot: run **C1** (`npx ccusage@latest --daily` after a quick npm-security-check — 2 min, zero setup) to see your real token/cost split, then **C3 this week** (`CLAUDE_CODE_ENABLE_TELEMETRY=1` + the `ColeMurray/claude-code-otel` local Grafana stack) to put your **cache-hit-rate gauge** live — the missing measurement layer for the [[claude-api-cost-optimization]] pilot. Goal-#2 track: **B1** (hireui dev-time cost baseline). Files are staged on the `autopilot-research` branch (uncommitted) — say the word and I'll commit.
