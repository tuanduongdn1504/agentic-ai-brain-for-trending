# Overview — the Observability-First Command Center

> **Source video:** Mansel Scheffel, *Claude Code + OpenTelemetry = Claude Command Center* (atomicOps, 2026-04-22, 15:54) — [00:01]–[02:17], [04:34]–[05:00], [09:05], [14:34]–[15:00]
> **Creator:** Mansel Scheffel (@atomicOps, AI consultancy, New York) — THIRD-PARTY, not Anthropic first-party

## Source

- Raw transcript: `../../raw/2026-06-20-claude-code-otel-command-center.md`
- Original resource URLs (embedded in video):
  - Claude Code monitoring/OpenTelemetry official docs: https://code.claude.com/docs/en/monitoring-usage
  - OpenTelemetry spec: https://opentelemetry.io/
  - Creator's prompt + guide: https://drive.google.com/drive/folders/15NZmCSXg3PEXWE1UumodEfJUXY9oF95W
  - Skool community: https://skool.com/ainative

## Thesis: "Observability First" vs the "Mission Control Theater"

The video contrasts **observability-first design** (Scheffel's approach) with the **elaborate "mission control" dashboards trending on YouTube** (what he calls "context bloat"):

- **The YouTube trend:** Multi-layer agent orchestration with visual dashboards, named agents, custom UI components, Pikachu pictures and Tamagotchi figures
- **Scheffel's critique:** "A seven-layer microservice that absolutely doesn't need to exist"; "context bloat"; "theater that doesn't move the business needle"
- **His posture:** For the agent front-layer, "just use Cowork" — ⚠️ **creator's estimate: Cowork does "98% or more" of what an elaborate AI OS does** (not independently verifiable); it's purpose-built for business users
- **What actually matters:** Observability, cost discipline, and performance diagnostics; not flashy UI

> Key quote: "You don't need Pikachu pictures and Tamagotchi figures. You just need to make money or execute on your goals."

## The Command Center: Architecture & Posture

### Persistent local daemon (always running)

The command center is **not a dashboard you open on demand** — it's a **persistent daemon** that lives on the local system and:
- Continuously finds work to do (task queue, scheduled tasks)
- Reports on everything Anthropic gives the system (JSONL logs, OpenTelemetry metrics/events)
- Identifies opportunities for cost savings, performance improvements, and security hygiene

### Two data sources from Anthropic

1. **JSONL logs** — Session transcripts stored at `~/.claude/projects/<encoded-path>/<session-id>.jsonl`
   - Tracks every message, tool call, and token usage (input, output, cache_creation, cache_read)
   - Default 30-day retention (configurable)
   - Source of truth for exact per-session replay and offline cost analysis
   - Native commands: `/cost`, `/stats`, `/status`, statusline footer (all JSONL-backed)

2. **OpenTelemetry (OTEL)** — Real-time telemetry pipeline (vendor-agnostic standard)
   - Enable: `CLAUDE_CODE_ENABLE_TELEMETRY=1` (opt-in; telemetry is strictly opt-in)
   - Exports metrics, logs, and traces (traces requires `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`)
   - Exporters: OTLP (gRPC/HTTP), Prometheus, console
   - Default OTLP endpoint: `http://localhost:4317` (metrics/logs), `http://localhost:4318/v1/traces`
   - ⚠️ **Video claims plan history:** "finally released to Max and Pro plans; previously enterprise-only" — **unconfirmed** by first-party docs; official documentation shows available on Pro and Max with no evidence of prior enterprise-only era
   - **No native in-product dashboard:** Official docs contain zero mention of in-GUI telemetry dashboard, `/cost`, `/usage`, or `/status` commands tied to OTEL. All OTEL dashboards must be built externally (Grafana, Datadog, Prometheus, etc.). The `/cost`, `/stats`, `/status` native commands read from JSONL, not OTEL.

## Five Dashboard Panels (The Observability Layer)

### 1. Posture — Two evergreen health checks (never static, run on schedule)

- **Security audit** (MCP poisoning risk, skill configuration, environment settings)
- **Context health** (inefficiencies in context handling, load reduction opportunities)
- Both evolve as the AI landscape changes; re-run on regular intervals (not once-and-done)

### 2. Token usage by model

- Overview of total tokens consumed across all sessions
- Window: "last X days" (configurable)
- Tied to cache hit rate panel for cost optimization strategy

### 3. Cache hit rate

- Critical for cost optimization — Anthropic's cache service is "the #1 cost lever"
- Exposed via `cache_read_tokens` and `cache_creation_tokens` on the `api_request` event
- Directly tied to subscription usage limits (not API billing overage)

### 4. MCP / API tool latency & error rate

- Tracks duration (latency) and success rate of tool calls via `tool_result` event
- Helps identify slow, error-prone MCP integrations (e.g., Notion `update_pages`, `create_database` slow)
- **Actionable:** May prompt switching from MCP to code execution workaround (untrapped in separate video)

### 5. Skill activations, frequency, and cost per run

- **Activations:** How many times each skill was triggered in the last 24 hours
- **Frequency:** Breakdown of token consumption per skill
- **Cost per run** (not accumulated): Individual skill execution cost, enabling per-skill performance optimization
- ⚠️ **Creator's example:** News monitor skill used 32 million tokens across 23 sessions — **this is Scheffel's personal datapoint, not independently verifiable from first-party sources**; user can reproduce by running `ccusage` on their own `~/.claude/projects` JSONL files

## Complementary Layers (Creator's Custom Implementation)

### Task Queue & Scheduling (Human-in-the-Loop Approval)

⚠️ **This layer is Scheffel's custom stack, not a built-in Claude Code feature.**

- **Scheduled tasks:** Cron-based skill execution (e.g., "morning brief at 9am daily")
- **Ad-hoc queue:** Interactive or one-shot skill execution with model assignment per task
- **Requires Approval flag:** Blocks execution until human approves via Telegram (requires separate Telegram bot + integration)
- **Telegram integration:** Mobile approval while task waits in queue (documented in [[../telegram-remote-control-stack/_index]])
- **Model assignment per skill:** Prevent unnecessary Opus usage; use Sonnet for simpler tasks

> Scheffel: "Think about WHY you're building it. Most things don't need mission control — they need Cowork or a schedule."

### Event-driven alerts & routing

- Failed task → alert to phone or downstream system
- Downstream system (third-party integrator) re-runs workflow or escalates
- Requires observability infrastructure to detect failures in the first place

## OTEL Metrics & Events Catalog (What's Observable)

### Available metrics (8 total)

| Metric | Unit | Attributes | Use case |
|--------|------|-----------|----------|
| `claude_code.session.count` | count | session_id, account_uuid | Session volume |
| `claude_code.lines_of_code.count` | count | version, account_uuid | Coding activity |
| `claude_code.pull_request.count` | count | version, account_uuid | PR/version control activity |
| `claude_code.commit.count` | count | version, account_uuid | Commit frequency |
| `claude_code.cost.usage` | USD | skill.name, model, account_uuid | Per-skill cost breakdown |
| `claude_code.token.usage` | tokens | type=[input/output/cacheRead/cacheCreation], model | Token spend by type & model |
| `claude_code.code_edit_tool.decision` | count | decision=[accept/reject/modify], version | Code review acceptance rate |
| `claude_code.active_time.total` | seconds | session_id, account_uuid | User active time |

### Available events (24+ total; subset relevant to observability)

| Event | Attributes | Use case |
|-------|-----------|----------|
| `user_prompt` | content (if OTEL_LOG_USER_PROMPTS=1), session_id | Audit trail of user inputs |
| `api_request` | input_tokens, output_tokens, cache_read_tokens, cache_creation_tokens, model, error_code | API call metrics; cache hit detection |
| `api_error` | error_code, error_message, retry_count | Error tracking & alerting |
| `tool_result` | duration_ms, success, tool_name, error (if enabled) | MCP/API latency & error rate |
| `skill_activated` | skill.name, skill_id | Skill usage frequency |
| `mcp_server_connection` | server_name, status | MCP connection health |
| `hook_execution_start` / `hook_execution_complete` | hook_id, duration_ms | Hook latency & success |

### Configuration flags (enable logging of sensitive data)

- `OTEL_LOG_USER_PROMPTS=1` — Log prompt content (default disabled; PII risk)
- `OTEL_LOG_TOOL_DETAILS=1` — Log tool names, arguments, Bash commands (default disabled)
- `OTEL_LOG_TOOL_CONTENT=1` — Log full input/output (default disabled; 60KB truncation)
- `OTEL_LOG_RAW_API_BODIES=1|file:<dir>` — Full Messages API bodies (default disabled; untruncated to disk option)

## Key Takeaways

- **Observability ≠ Mission Control UI.** The valuable work happens in dashboards (Grafana, Datadog) fed by OTEL/JSONL, not in elaborate agent orchestration theater.
- **JSONL + OTEL are complementary.** JSONL: exact replay, offline analysis, works on any plan; OTEL: real-time streaming, server-side metering, requires telemetry pipeline setup.
- **Cache hit rate is the #1 cost lever.** Optimize subscription usage (on-plan) before worrying about API overage.
- **Persistent daemon, not dashboard-on-demand.** Real systems should continuously monitor, alert, and escalate — not rely on human manual observation.
- ⚠️ **Cowork handles most use cases.** Creator claims Cowork does "98%+ of interactive use cases" (not independently verifiable); if you need a front-layer agent conversation, use Cowork; don't build a custom mission control.
- **Model assignment per task is a force multiplier.** Sonnet for simple work, Opus for complex reasoning; reduces token waste and cost per run.
- **Skill cost-per-run tracking surfaces inefficiency opportunities.** ⚠️ Creator's example: news monitor refactored to 1/10th the token cost after observing 32M-token usage spike (personal datapoint, not independently verifiable).
- **Security + context health are evergreen.** Re-run posture checks on regular intervals; AI landscape evolves, and so should your baselines.

## Topic map — Claude Code Observability

This article is the entry point to the topic. Articles in this topic:

| Article | Purpose |
|---------|---------|
| [[overview]] | Thesis, architecture, and key contrasts (you are here) |
| [[claude-code-opentelemetry]] | OTEL config reference + cardinality controls + gotchas |
| [[opentelemetry-standard]] | OTEL signals, OTLP protocol, semantic conventions, ecosystem |
| [[observability-backend-stack]] | Grafana, Prometheus, Loki, Datadog, managed OTEL platforms |
| [[cost-cache-token-metrics]] | OTEL metrics for cost, cache hit rate, token breakdown by model |
| [[mcp-and-skill-cost-metrics]] | MCP latency/error rate, skill activations, cost-per-run |
| [[task-queue-scheduling-telegram-hitl]] | Task scheduling, Telegram approval, event-driven escalation |
| [[jsonl-logs-and-native-dashboard]] | JSONL format, retention, /cost /stats /status, ccusage parser |
| [[code-execution-mcp-workaround]] | MCP latency solutions (promised in separate video, not yet available) |
| [[video-to-original-crosswalk]] | Mapping video timestamps to first-party resources |
| [[source-provenance]] | Creator credentials, THIRD-PARTY status, atomicOps background |

## Cross-topic links

- [[../claude-api-cost-optimization/_index]] — Cache hit rate is the #1 cost lever; token spend patterns
- [[../claude-code-hooks/_index]] — Deterministic complement to telemetry; hooks as automation surface
- [[../telegram-remote-control-stack/_index]] — Telegram HITL approval pattern (Scheffel uses for task queue; operator already piloted Recipe A)
- [[../autonomous-loops-human-in-the-loop/_index]] — Persistent daemon + human approval loop pattern
- [[../claude-cowork/_index]] — Creator recommends Cowork as the front-layer UI; ~98% of use cases claim
- [[../prompt-evaluation/_index]] — Trace-driven eval triage (same observability discipline at smaller scale)
- [[../agentic-analytics-harness/_index]] — Observability over scorecards; daily trace-driven session triage at scale
- [[../harness-engineering/_index]] — Observability as a core harness property
- [[../claude-skills/_index]] — Skill cost metrics, activation frequency, per-run cost
- [[../agent-dashboard-os/_index]] — Prior weak observability landscape topic (reconciliation: that was abstract 6-video bundle; this is concrete first-party-anchored Claude Code + OTEL implementation)
