# MCP and Skill Cost Metrics

> **Context:** Mansel Scheffel (atomicOps, Claude Code + OpenTelemetry = Claude Command Center). Timestamps [09:33]–[14:08]. The **activity panel** of the observability dashboard: understanding tool latency, error rate, skill activations, and per-skill cost to diagnose inefficiency and avoid wasted tokens.

## Source

- Raw file: `../../raw/2026-06-20-claude-code-otel-command-center.md`
- Video: Mansel Scheffel, [Claude Code + OpenTelemetry = Claude Command Center](https://www.youtube.com/watch?v=dITtLiC9FzM), 2026-04-22, 15:54
- Cross-referenced: Claude Code official monitoring-usage docs, Anthropic engineering "Code execution with MCP", Platform.claude.com docs

---

## MCP/API Tool Latency & Error Rate

The **activity panel** exposes latency (duration, via `duration_ms` on tool result events) and error rate (via `success` attribute) for every MCP and API call Claude makes in your environment.

- **Why it matters:** Repeated high error rates indicate a tool is trying to do something it can't (e.g., web_fetch returning "access denied" on the same endpoint repeatedly). Without seeing this, you keep burning tokens on failing calls.
- ⚠️ **Video example:** ⚠️ web_fetch showing high error rate → creator example [09:59]: indicates a skill is constantly hitting a protected endpoint or resource it lacks permission to access. (Unconfirmed against official Anthropic docs; creator's diagnostic pattern.)
- **Latency insight:** ⚠️ Notion tools (update-pages, create-databases, search) are noted as slow in MCP deployments [12:44]. (Unconfirmed in first-party Anthropic docs; video creator's observed pattern. Anthropic engineering post uses hypothetical examples—Google Drive, Salesforce, Slack—not production Notion deployments.)
- **Alternative:** Local alternatives (Obsidian) avoid MCP entirely; the cost is visual loss.
- **Solution path:** observability first → identify slow/failing tools → decide: (a) optimize the MCP server, (b) use code execution instead (see [[code-execution-mcp-workaround]]), or (c) replace with local alternative.

---

## Skill Activations & Frequency-vs-Consumption

The **activations view** (last 24h) tracks:

- **How many times** each skill ran (count in past 24 hours)
- **Total tokens consumed** per skill across those runs (including all sessions where that skill was invoked)
- **Frequency distribution:** e.g., creator's case [10:27]: "AI News Monitor ran 23 sessions"

### Key discipline: audit-driven optimization

⚠️ **Creator example [10:27]:** one of his automated skills (AI News Monitor) was burning tokens per day due to inefficient context usage. The creator claims the fix will drop token spend "massively" [10:54], but does not quantify the delta. This is a **creator observation, not a reproducible metric from official docs.**

- **Skill cost per run:** separate view showing cost-per-activation (not cumulative), so you can identify which individual tasks are expensive [13:40].
- **Environment scope:** metrics roll up across all environments you're running skills in. If a skill is running in 3 environments (e.g., local machine, Cowork, cloud agent), its cost metrics reflect all three [13:40].

### Model assignment as context-load lever

When creating skills, assign the **model explicitly** to the skill definition. Don't default all tasks to Opus [06:49], [07:16].

- Many tasks don't need Opus. A "create gamma deck" task sounds like it needs Opus reasoning, but if the Gamma design agent does most of the work, Sonnet is sufficient.
- Per-skill model assignment is a [[cost-cache-token-metrics|cost]] lever and a [[../claude-code-hooks/_index|context-load management]] practice.

---

## FAILURES View & Event-Driven Alerting

The **failures panel** shows every failed skill run (if any) with:

- Session ID
- Model used
- Duration
- Failure reason (extracted from the event)

**Event-driven response:** When a skill fails, trigger an automated action:

- Phone alert (via Telegram HITL, see [[task-queue-scheduling-telegram-hitl]])
- Remediation workflow (e.g., retry with different model, escalate to human, send to a downstream system)
- Audit trail (logged via OTEL events)

⚠️ **Creator emphasis [11:49]:** This is critical for client-facing AI operating systems. If you deploy an autopilot for a client and something silently fails, they won't know unless you have observability + event-driven alerting feeding back to you. The anxiety of "is my system still working?" is solved by proactive monitoring.

---

## RECENT SESSIONS View

Displays the last N completed skill runs (creator's demo: 10 out of 19 sessions [11:22]):

- **Session ID** — unique identifier for the run
- **Model** — which Claude model was assigned
- **Duration** — how long the task took
- **Outcome** — pass/fail (and reason if failed)
- **Filtering:** drill down to failed sessions, or by model, or by timestamp

This view enables **post-hoc debugging** and **trend analysis** (e.g., "is Sonnet suddenly slower than last week?").

---

## Skills Registry

The **skills registry** (right-hand side of dashboard, [14:08]) lists **every skill across all your environments** with a brief description of what each one does.

- **Purpose:** audit trail. Know what's running. Identify stale/obsolete skills that should be deleted.
- **Cardinality:** can grow large if you're running many skills. Manual cleanup periodically.
- **Environment scope:** includes skills from local IDE, Cowork, cloud agents — one unified view.

---

## Context Health Panel

Tied to [[../claude-code-hooks/_index|context engineering]] and referenced in creator's video on context engineering [14:08]. Shows where your environment is inefficient in how it uses context:

- Patterns identified: e.g., loading the same tools repeatedly, duplicating schema definitions, missing tool defer_loading, etc.
- Actionable report: what to change to improve context efficiency

---

## OTEL Configuration for Activity Metrics

To enable MCP/tool latency + error rate + skill cost metrics:

**Enable telemetry (required flag):**
```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=1
```

**Metrics exporter (choose one):**
```bash
export OTEL_METRICS_EXPORTER=otlp        # OpenTelemetry Protocol (to collector)
export OTEL_LOGS_EXPORTER=otlp           # Logs (tool results, events)
```

**Collector endpoint (default):**
```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317  # gRPC
# or per-signal override:
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://localhost:4318/v1/metrics
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://localhost:4318/v1/logs
```

**Metrics available (OTEL auto-exports these via [[opentelemetry-standard|OpenTelemetry standard]]):**

- `claude_code.cost.usage` (USD) — per-skill cost breakdown via `skill.name` attribute
- `claude_code.token.usage` (tokens) — with `type=[input|output|cacheRead|cacheCreation]`; watch cache_read for [[cost-cache-token-metrics|cache hit rate]]
- Tool result event: `duration_ms`, `success` (latency + error rate)
- Event: `skill_activated` (count of activations per 24h window)

**Optional: expose tool names in logs (required for MCP troubleshooting):**
```bash
export OTEL_LOG_TOOL_DETAILS=1   # logs MCP tool names, skill names, argument values
export CLAUDE_CODE_ENABLE_TELEMETRY=1  # prerequisite
```

### Gotcha: cardinality explosion

`OTEL_METRICS_INCLUDE_SESSION_ID=true` (default) means every session generates a unique metric series. For high-volume deployments (100+ sessions per day), this explodes your metrics backend storage cost. Consider disabling:

```bash
export OTEL_METRICS_INCLUDE_SESSION_ID=false
```

---

## Key Takeaways

- **Observability surfaces the problems.** You can't fix what you can't see. Without tool latency + error rate visibility, you keep burning tokens on slow/failing MCP calls.
- **Skill frequency-vs-consumption audit** reveals which automations are token hogs. ⚠️ Creator case: one skill fix claimed to convert "massive" token spend → minimal spend [10:54], but delta not quantified.
- **Per-skill model assignment** is a context-load lever; don't default to Opus.
- **Event-driven alerting on failures** (via [[task-queue-scheduling-telegram-hitl|Telegram HITL]]) is essential for client-facing autopilots.
- **Skills registry = audit trail.** Know what's running. Clean up obsolete skills.
- **Context health panel** surfaces inefficiencies in how you load tools/schemas; tied to [[../claude-code-hooks/_index|hook discipline]] + [[cost-cache-token-metrics|cache hit rate tuning]].
- ⚠️ **No native *OTEL-fed* dashboard in Claude Code.** Native usage *views* do exist (`/cost`, `/usage`, `/stats`, the statusline — local/account-fed, not OTEL; plus a Console Analytics dashboard for Team/Enterprise), but the customizable OTEL-fed panel dashboard the video shows must be built externally via OTLP exporters (Grafana, Prometheus, Datadog). The creator's "shiny but mediocre OTEL-fed dashboard inside Claude code in the GUI" [02:17] conflates a native view with his own external OTEL build.
- **MCP is token-hungry.** Baseline: 55,000–67,000 tokens for 5–10 MCPs before any work begins. See [[code-execution-mcp-workaround]] for the alternative: code execution + tool search reduce MCP context bloat by 85–98%.

---

## Forward Links

- [[code-execution-mcp-workaround]] — when MCP latency is unacceptable, use code execution + tool search to avoid schema bloat
- [[../claude-api-cost-optimization/_index]] — cache hit rate is the #1 cost lever; token spend optimization
- [[task-queue-scheduling-telegram-hitl]] — Telegram approval pattern for human-in-the-loop workflows
- [[jsonl-logs-and-native-dashboard]] — OTEL session logs + how to export to Grafana/Prometheus
- [[claude-code-opentelemetry]] — OTEL configuration deep-dive (all env vars, exporter options, security)
- [[cost-cache-token-metrics]] — cache_read_tokens, cache_creation_tokens, per-model token tracking
- [[../prompt-evaluation/_index]] — trace-driven eval triage (same observability discipline at eval layer)
- [[../autonomous-loops-human-in-the-loop/_index]] — Telegram approval pattern + failure recovery automation
- [[../harness-engineering/_index]] — observability as a first-class harness property
