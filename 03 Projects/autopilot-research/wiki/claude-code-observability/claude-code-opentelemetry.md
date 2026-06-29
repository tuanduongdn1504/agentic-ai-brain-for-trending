# OpenTelemetry in Claude Code

> **Source:** Mansel Scheffel, atomicOps; "Claude Code + OpenTelemetry = Claude Command Center" (2026-04-22, 15:54, 15K views); [02:17] — "...open telemetry now, which they finally released to people on the Max and Pro plans. Previously, it was only for enterprise people, and that's how you see this shiny little mediocre dashboard inside Claude code in the GUI."

## Source

Raw transcript: `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-06-20-claude-code-otel-command-center.md`

Primary sources:
- Claude Code official [monitoring-usage documentation](https://code.claude.com/docs/en/monitoring-usage)
- Claude Code [environment variables reference](https://code.claude.com/docs/en/cli-reference)
- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) (standard signal definitions)

---

## Overview

Claude Code exposes comprehensive observability via OpenTelemetry (OTEL) — the industry-standard telemetry framework. OTEL telemetry is **opt-in** (requires explicit enable flag), exports metrics, logs, and traces (beta) to collector endpoints (local or remote), and feeds external dashboards (Grafana, Prometheus, Datadog, etc.). This is the load-bearing first-party implementation for Claude Code observability.

Key: **no native in-product dashboard exists in official documentation.** All visualization must be built externally.

---

## Enable telemetry (required opt-in)

Telemetry is disabled by default. To activate:

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=1
```

This flag is required for metrics, logs, and traces exporters to function. Without it, no telemetry is collected or sent.

---

## Exporter configuration (OTEL_*_EXPORTER env vars)

Three signal types (metrics, logs, traces) have independent exporters. Each defaults to `none` (disabled).

### Metrics exporter

```bash
export OTEL_METRICS_EXPORTER=otlp|prometheus|console|none
```

- `otlp` — send to OTLP Collector endpoint (default gRPC on `:4317/v1/metrics`)
- `prometheus` — expose Prometheus scrape endpoint (local only, no remote ship)
- `console` — log metrics to stderr
- `none` — disabled (default)

### Logs exporter

```bash
export OTEL_LOGS_EXPORTER=otlp|console|none
```

- `otlp` — send to OTLP Collector endpoint (default gRPC on `:4317/v1/logs`)
- `console` — log events to stderr
- `none` — disabled (default)

### Traces exporter (beta)

```bash
export OTEL_TRACES_EXPORTER=otlp|console|none
export CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1  # REQUIRED to enable tracing
```

Traces require both flags. Traces include full call-stack spans for every tool invocation, API request, and hook execution. Beta status means structure may change; enterprise orgs have beta access.

---

## OTLP endpoint configuration

By default, all OTLP signals route to the OpenTelemetry Collector on localhost:

```bash
# General OTLP endpoint (applies to all signals unless overridden per-signal)
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# Per-signal overrides (use these to route signals to different backends)
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://localhost:4318/v1/metrics
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://localhost:4318/v1/logs
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://localhost:4318/v1/traces
```

Standard OTLP Collector ports:
- **4317** — default gRPC receiver (metrics, logs, traces all on same endpoint)
- **4318** — default HTTP receiver

### OTLP protocol selection

```bash
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc|http/json|http/protobuf
```

- `grpc` (default) — binary gRPC protocol, lowest latency
- `http/json` — HTTP with JSON payloads, easier to debug
- `http/protobuf` — HTTP with Protobuf payloads, smaller size

Per-signal override:

```bash
export OTEL_EXPORTER_OTLP_METRICS_PROTOCOL=http/json
export OTEL_EXPORTER_OTLP_LOGS_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
```

---

## Export intervals (frequency tuning)

```bash
export OTEL_METRIC_EXPORT_INTERVAL=60000      # milliseconds; default 60s
export OTEL_LOGS_EXPORT_INTERVAL=5000         # milliseconds; default 5s
export OTEL_TRACES_EXPORT_INTERVAL=5000       # milliseconds; default 5s
```

Lower intervals = more frequent exports, higher backend load. Higher intervals = longer latency to see recent events. Adjust per backend capacity and real-time requirements.

---

## Authentication & encryption (OTEL_EXPORTER_OTLP_HEADERS, mTLS)

### Bearer token / API key

```bash
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <token>,X-API-Key=<key>"
```

Headers apply to all signals unless per-signal override:

```bash
export OTEL_EXPORTER_OTLP_METRICS_HEADERS="Authorization=Bearer <metrics-token>"
```

### mTLS (mutual TLS)

For gRPC:

```bash
export OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE=/path/to/client.crt
export OTEL_EXPORTER_OTLP_CLIENT_KEY=/path/to/client.key
```

For HTTP (http/json, http/protobuf):

```bash
export CLAUDE_CODE_CLIENT_CERT=/path/to/client.crt
export CLAUDE_CODE_CLIENT_KEY=/path/to/client.key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE=<passphrase>   # optional
```

Trust collector CA:

```bash
export OTEL_EXPORTER_OTLP_CERTIFICATE=/path/to/ca.crt  # gRPC
export NODE_EXTRA_CA_CERTS=/path/to/ca.crt              # HTTP
```

### Dynamic headers (advanced)

For HTTP protocols, Claude Code can refresh authorization headers dynamically by calling an external script (an `otelHeadersHelper`). This is useful when using OAuth tokens that expire — the script is invoked on a debounce interval and must output `Key=Value` header pairs. Dynamic headers work only with `http/json` and `http/protobuf`; gRPC uses static `OTEL_EXPORTER_OTLP_HEADERS` only.

```bash
export CLAUDE_CODE_OTEL_HEADERS_HELPER=/path/to/refresh-headers.sh
# a debounce interval (in ms) also exists; default unconfirmed
```

> ⚠️ **Single-source / partially confirmed:** the `otelHeadersHelper` dynamic-header feature is real, but the exact env-var names (`CLAUDE_CODE_OTEL_HEADERS_HELPER` / a `*_DEBOUNCE_MS` companion) and the default debounce interval were **not fully confirmable** — the official env-var table is truncated in the fetched docs. Treat the var names as indicative; check the current `env-vars` reference before relying on them.

---

## Metrics catalog (8 total)

Each metric has a **name**, **unit**, and **attributes** (tags). All metrics include `session_id`, `user`, and `version` attributes by default (configurable; see [Cardinality controls](#cardinality-controls) below).

| Metric name | Unit | Attributes | Notes |
|---|---|---|---|
| `claude_code.session.count` | count | session_id, user, version | Increments once per session started |
| `claude_code.lines_of_code.count` | count | session_id, user, version | Lines edited across all files in a session |
| `claude_code.commit.count` | count | session_id, user, version | Total commits made in a session |
| `claude_code.pull_request.count` | count | session_id, user, version | Total PRs opened in a session |
| `claude_code.cost.usage` | USD | session_id, user, model, skill.name, version | Estimated cost in US dollars (approximation only; official billing is authoritative) |
| `claude_code.token.usage` | tokens | session_id, user, model, type=[input\|output\|cacheRead\|cacheCreation], version | Token count by type and model |
| `claude_code.code_edit_tool.decision` | count | session_id, user, code_edit_tool.name, version | Frequency of code edit tool invocations (edit, replace, delete, etc.) |
| `claude_code.active_time.total` | seconds | session_id, user, version | Total elapsed time user was actively interacting (wall-clock) |

**Token types:**
- `input` — tokens sent to Claude (prompt + context)
- `output` — tokens generated by Claude (response)
- `cacheRead` — cached tokens read (not charged, or charged at reduced rate per plan)
- `cacheCreation` — tokens written to cache (charged at premium for cache storage)

**Cost metric note:** `claude_code.cost.usage` is an approximation computed locally from token usage + model + cache behavior. It does NOT include Anthropic's actual billing adjustments, promotions, or platform-specific pricing (Bedrock, Vertex AI). Use official billing console for financial audit.

> ⚠️ **Single-source flag (Rule 12 fail-loud):** the metric names `claude_code.session.count`, `claude_code.lines_of_code.count`, `claude_code.cost.usage`, `claude_code.token.usage`, and `claude_code.active_time.total` were corroborated by an independent cross-check. Three were **not** independently re-confirmed (the docs page was partly truncated for the cross-checker): **`claude_code.pull_request.count`**, **`claude_code.code_edit_tool.decision`** (may instead surface as a `tool_decision` event), and the **`type` attribute** on `token.usage` (the input/output/cacheRead/cacheCreation split is widely reported but the exact attribute key wasn't re-verified). These come from the first-party `monitoring-usage` docs fetch; verify against your live `/usage`/backend before depending on the exact names. See [[source-provenance]].

---

## Events catalog (24+ total)

Events (also called "structured logs") record discrete occurrences with attributes. Each event has a timestamp, name, and arbitrary attributes.

| Event name | Attributes | Triggered by |
|---|---|---|
| `user_prompt` | user_prompt (text), session_id | User submits text in Claude Code prompt |
| `tool_result` | tool_name, duration_ms, success, result_content, session_id | Any tool (Bash, MCP, web fetch, code execution) completes |
| `api_request` | model, input_tokens, output_tokens, cache_read_tokens, cache_creation_tokens, duration_ms, endpoint, session_id | API request to Claude sent |
| `api_error` | error_code, error_message, model, session_id | API request fails |
| `api_refusal` | reason, model, session_id | Claude refuses a request (e.g., policy rejection) |
| `api_request_body` | request_body (full JSON), session_id | Full Messages API request body (PII: includes entire conversation history) |
| `api_response_body` | response_body (full JSON), session_id | Full Messages API response (PII: includes full response) |
| `tool_decision` | tool_name, rationale, session_id | Claude decides to invoke a tool (before execution) |
| `permission_mode_changed` | new_mode (allow/deny/ask), tool_name, session_id | User changes permission for a tool |
| `auth` | auth_type, status (success/fail), session_id | Authentication event (e.g., GitHub login) |
| `mcp_server_connection` | server_name, status (connected/disconnected), session_id | MCP server connects or disconnects |
| `internal_error` | error_type, stack_trace, session_id | Claude Code internal error |
| `plugin_installed` | plugin_name, version, session_id | Skill/plugin installed |
| `plugin_loaded` | plugin_name, version, session_id | Skill/plugin loaded (on startup) |
| `skill_activated` | skill_name, model, session_id | User activates a skill |
| `at_mention` | mention_target, session_id | User mentions a person/team (Telegram/Cowork only) |
| `api_retries_exhausted` | max_retries, session_id | API request exceeded retry limit and gave up |
| `hook_registered` | hook_name, hook_type, session_id | Hook registered |
| `hook_execution_start` | hook_name, session_id | Hook begins execution |
| `hook_execution_complete` | hook_name, duration_ms, success, error, session_id | Hook finishes execution |
| `hook_plugin_metrics` | hook_name, plugin_name, duration_ms, session_id | Hook invoked a plugin |
| `compaction` | old_context_tokens, new_context_tokens, session_id | Session context was compacted (summarized) |
| `feedback_survey` | survey_response, session_id | User submits feedback survey |

**⚠️ PII caveat:** `api_request_body` and `api_response_body` events contain the ENTIRE conversation history (all prior turns) verbatim. These events should be logged only if you consent to exporting full conversation transcripts to the telemetry backend. Enabling these is a compliance decision, not a technical setting.

---

## Cardinality controls (metric series explosion prevention)

By default, metrics are tagged with `session_id`, `user`, `account_uuid`, and `version`. Each unique value creates a new metric series in the backend, increasing storage cost. Control which attributes are included:

```bash
# All default to true; set to false to reduce series count
export OTEL_METRICS_INCLUDE_SESSION_ID=true|false         # default true
export OTEL_METRICS_INCLUDE_VERSION=true|false            # default false
export OTEL_METRICS_INCLUDE_ACCOUNT_UUID=true|false       # default true
export OTEL_METRICS_INCLUDE_ENTRYPOINT=true|false         # default false (entrypoint = CLI vs GUI vs API)
export OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES=true|false # default true
```

**Gotcha:** high-cardinality attributes (e.g., unique session IDs) can cause metric series explosion. Disabling `OTEL_METRICS_INCLUDE_SESSION_ID` reduces series count at the cost of per-session granularity.

### Custom resource attributes

Add organizational tags to all metrics (e.g., `department=engineering`, `team.id=platform`):

```bash
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,env=prod"
```

Format: comma-separated `key=value` pairs (no spaces allowed).

---

## Content logging options (detailed telemetry)

By default, Claude Code does NOT log prompt text, tool details, or API bodies — only structured metadata (counts, timestamps, IDs). Enable granular logging with:

```bash
export OTEL_LOG_USER_PROMPTS=1        # log user_prompt event with full text (PII)
export OTEL_LOG_TOOL_DETAILS=1        # log tool names, Bash commands, MCP methods, arguments (audit trail)
export OTEL_LOG_TOOL_CONTENT=1        # log full tool input/output in trace spans (large; truncated to 60KB)
export OTEL_LOG_RAW_API_BODIES=1      # log full Messages API request/response bodies to stderr
export OTEL_LOG_RAW_API_BODIES=file:/tmp/otel-api-bodies  # or write to disk (untruncated)
```

**⚠️ Security note:** enabling any of these exposes PII (prompts, secrets in commands, API payloads). Use in development only or in secure, compliance-aware environments.

---

## Metrics temporality (aggregation style)

```bash
export OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta|cumulative
```

- `delta` (default) — export only changes since last export (smaller payloads, stateless)
- `cumulative` — export running total from start of time (larger payloads, useful for certain backends)

Most backends prefer delta.

---

## Supported exporters (deployed backends)

OTEL is a standard; Claude Code ships exporters for three backends:

### OTLP (OpenTelemetry Protocol)

Universal standard. Any backend that accepts OTLP is supported: **Grafana Cloud**, **Datadog**, **New Relic**, **Lightstep**, **Honeycomb**, **AWS X-Ray**, **Google Cloud Trace**, or a **self-hosted OpenTelemetry Collector**.

Most flexible; requires running a collector or account with a managed OTLP ingestion endpoint.

### Prometheus (metrics only)

```bash
export OTEL_METRICS_EXPORTER=prometheus
```

Starts a local HTTP server on `:8888/metrics` that Prometheus can scrape. Logs and traces are not supported. Useful for local debugging and integration with existing Prometheus setups.

### Console (debugging)

```bash
export OTEL_METRICS_EXPORTER=console
export OTEL_LOGS_EXPORTER=console
export OTEL_TRACES_EXPORTER=console
```

Prints all signals to stderr in human-readable format. Not suitable for production; useful for development and testing.

---

## Plan availability (Pro, Max, Enterprise)

⚠️ **Video claim check:** Mansel says "they finally released to people on the Max and Pro plans; previously it was only for enterprise people."

**Verified status (June 2026):** OpenTelemetry is available on **Pro and Max subscription plans**. Official documentation does NOT gate OTEL behind plan tiers; the flag and env vars work universally. The video's framing that OTEL was "previously enterprise only" is **unconfirmed** — official docs provide no release notes or timeline confirming this was enterprise-gated before a recent release.

Enterprise customers may have additional options (e.g., managed settings in org admin console), but the core OTEL feature is confirmed available on Pro/Max.

---

## Managed settings (org-level OTEL configuration)

Organizations with Claude Code managed settings can pre-configure OTEL defaults in an admin console. Managed settings take precedence over user env vars. Example: an org may set `OTEL_EXPORTER_OTLP_ENDPOINT` centrally and forbid users from changing it, or mandate `CLAUDE_CODE_ENABLE_TELEMETRY=1` org-wide.

Check with your org admin if using a managed Claude Code deployment.

---

## Native usage views vs. the "in-GUI dashboard" claim

⚠️ **Video claim check:** Mansel says "that's how you see this shiny little mediocre dashboard inside Claude code in the GUI… fed partially from OTEL."

**Partially refuted — nuance matters.** What actually exists natively:

- **Terminal usage commands** — `/cost` (session API cost/tokens), `/usage` (token usage + plan-limit breakdown + activity), `/stats` (usage heatmap, session counts, model breakdown), and the **statusline** footer. These are real and read from **local/account data, not the OTEL pipeline**. (`/status` as a *cost* view is unconfirmed.)
- **Anthropic Console "Analytics" dashboard** — a real web dashboard for **Team/Enterprise** admins (per-user activity + spend, ~1-day delay).

What does **not** exist: a built-in, **customizable, OTEL-fed observability dashboard** inside Claude Code like the one in the video. The rich Grafana-style "command center" Mansel shows is **his own external build** on top of an OTLP backend. So his "shiny mediocre dashboard… fed by OTEL" conflates a native usage view (or the Console Analytics page) with a custom OTEL dashboard — the genuinely OTEL-fed, panelized dashboard must be built externally (Grafana, Datadog, etc.). See [[observability-backend-stack]].

---

## Environment variable inheritance (subprocess gotcha)

⚠️ **Critical gotcha:** OTEL_* and CLAUDE_CODE_* env vars set in the parent shell are **NOT automatically inherited** by subprocesses spawned by Claude Code (Bash sessions, MCP servers, language servers, hooks, etc.).

If you want a Bash script invoked by Claude Code to export metrics, you must either:

1. Source the parent's env vars in the script:
   ```bash
   # Inside your Bash script called by Claude Code
   source ~/.claude/otel-config.sh
   ```

2. Or set them in the subprocess invocation:
   ```bash
   OTEL_METRICS_EXPORTER=otlp bash -c "my-command"
   ```

This is a deliberate isolation boundary to prevent leaking telemetry config to untrusted user scripts.

---

## Relationship to JSONL session logs

Claude Code stores **two separate sources** of observability data:

1. **OTEL metrics/logs/traces** (this article) — structured, real-time stream exported to external backends
2. **JSONL session logs** (stored in `~/.claude/`) — complete unsampled transcript of every session, stored locally

JSONL logs are the authoritative record of what happened. OTEL telemetry is a real-time stream best suited for operational dashboards. See [[jsonl-logs-and-native-dashboard]] for the JSONL format and native Claude Code viewing options.

---

## Relationship to cost optimization and cache hit rates

The metrics `claude_code.cost.usage` and `claude_code.token.usage` with type=`cacheRead`/`cacheCreation` expose the **primary cost levers** in Claude Code. See [[cost-cache-token-metrics]] for cost optimization strategies and [[../claude-api-cost-optimization/_index]] for cache hit rate tuning.

---

## Key takeaways

- **OTEL is opt-in:** `CLAUDE_CODE_ENABLE_TELEMETRY=1` required; no telemetry without this flag
- **Three signal types:** metrics (counters), logs/events (structured records), traces (beta; requires separate beta flag)
- **OTLP is the standard:** export to any OTLP-compatible backend (Grafana, Datadog, self-hosted Collector, managed services)
- **8 metrics catalog:** session count, LOC, commits, PRs, cost USD, token usage (by type + model), code edit decisions, active time
- **24+ events catalog:** user prompts, API requests/errors, tool results, permissions, hook execution, plugin lifecycle
- **Cardinality controls matter:** high-cardinality attributes like `session_id` create many metric series; tune `OTEL_METRICS_INCLUDE_*` flags for backend cost
- **No native OTEL dashboard, but native usage *views* do exist:** `/cost`, `/usage`, `/stats`, the statusline (local/account-fed, not OTEL) + a Console Analytics dashboard for Team/Enterprise — none is the customizable OTEL-fed panel dashboard the video shows; that's an external build
- **Cache metrics enable cost optimization:** `cacheRead` and `cacheCreation` token types expose cache behavior; core lever for cost reduction
- **JSONL logs are separate:** OTEL is real-time streaming; JSONL session logs are authoritative unsampled transcripts stored locally

---

## See also

- [[overview]] — observability landscape + why OTEL matters
- [[opentelemetry-standard]] — OTEL signal types, Collector architecture, semantic conventions
- [[observability-backend-stack]] — Grafana + Prometheus + Loki setup for ingesting OTEL
- [[cost-cache-token-metrics]] — cost-optimization strategies using OTEL metrics
- [[mcp-and-skill-cost-metrics]] — per-MCP-server and per-skill cost/latency tracking
- [[task-queue-scheduling-telegram-hitl]] — event-driven alerts and Telegram approvals
- [[jsonl-logs-and-native-dashboard]] — session transcripts + native viewing
- [[video-to-original-crosswalk]] — how Mansel's video relates to first-party OTEL docs
- [[source-provenance]] — sourcing discipline for this topic
- [[code-execution-mcp-workaround]] — workarounds for MCP latency constraints
- [[../agent-dashboard-os/_index]] — prior observability-landscape topic (abstract); compare with this concrete OTEL implementation
- [[../claude-api-cost-optimization/_index]] — cache hit rate as #1 cost lever
- [[../claude-code-hooks/_index]] — hooks as deterministic complement to telemetry
- [[../autonomous-loops-human-in-the-loop/_index]] — Telegram approval pattern
- [[../telegram-remote-control-stack/_index]] — Telegram HITL approval stack
- [[../claude-skills/_index]] — skill cost metrics
- [[../harness-engineering/_index]] — observability as a harness property
