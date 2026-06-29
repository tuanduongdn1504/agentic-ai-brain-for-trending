# Cost, cache & token metrics — where your tokens actually go

> **Video:** Mansel Scheffel (atomicOps), "Claude Code + OpenTelemetry = Claude Command Center" (2026-04-22), timestamps [04:05]–[04:32], [10:17]–[11:00], [13:40]. Shows the observability panel: token usage by model over a window, cache hit rate (why it matters), per-skill cost breakdown, and how to audit token spend to improve efficiency.

## Source

- **Video transcript:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-06-20-claude-code-otel-command-center.md`
- **Official reference:** Claude Code OpenTelemetry monitoring-usage documentation (https://code.claude.com/docs/en/monitoring-usage)
- **Cross-topic context:** [[../claude-api-cost-optimization/_index]] (cache hit rate as the #1 cost lever), [[../autonomous-loops-human-in-the-loop/_index]] (the HITL approval pattern with requires-approval → Telegram), [[../claude-skills/_index]] (skill cost metrics), [[../claude-code-hooks/_index]] (hooks as deterministic complement to telemetry)

---

## The observability metrics overview

When you enable OpenTelemetry, the metrics layer exposes three primary views:

- **Token usage by model** — cumulative tokens (input + output) consumed by each model (Claude 3.5 Sonnet, Opus, etc.) over a configurable time window (last 24h, 7d, 30d). Helps you understand which workloads are burning the most tokens.
- **Cache hit rate** — ratio of cached input reads to total input tokens. Critical metric; see "Why cache hit rate matters" below.
- **Cost per skill** — breakdown of token spend per skill activation. Shows which skills are most expensive to run, allowing you to optimize the most costly ones first (via model downgrade, context reduction, or architecture redesign).

The creator's setup also includes **skill activations** (how many times each skill ran in last 24h) and **session history** with model assignment, duration, and cost per session — letting you correlate high-cost sessions to their source.

---

## Why cache hit rate matters (the #1 cost lever)

Cache hit rate is your #1 measurement point for [[../claude-api-cost-optimization/_index]]. Here's why:

**Cost reduction:** Cached input tokens bill at approximately **0.1x the rate of uncached input tokens** — a ~90% discount. Example: 1M cached input tokens costs ~1/10 what 1M uncached input tokens costs.

**Rate limit multiplication:** Cached reads do NOT count against your rate limit. An 80% cache hit rate effectively multiplies your rate limit by 5x: if your non-cached throughput would burn your limit, cached throughput lets you stay well below it.

**Latency:** Cached prefixes return faster from Anthropic's backend than re-computing them fresh.

⚠️ **The timestamp-in-system-prompt killer:** The single biggest cache-break is a timestamp in your system prompt. Any byte change in the cached prefix invalidates everything after it. See [[../claude-api-cost-optimization/_index]] for specific guidance: move timestamps to user message, or use cache_control at the boundary to freeze the system prompt.

---

## Real-world token burn example (creator datapoint)

The creator's AI news monitor skill (running across 23 sessions over a period) consumed **32 million tokens** — described as unexpectedly high and prompting an efficiency audit. Once identified via the cost metrics, the skill was rewritten to be dramatically more efficient while producing the same output.

⚠️ **This 32M-token figure is unverified** (could not reproduce against official API logs or billing data). Use it as illustrative of the scale of waste possible, not as a benchmark or first-party claim.

The key lesson: **Observability exposes the problem; you fix it by rewriting the skill.** Without the cost metrics, the waste would be invisible.

---

## Excalidraw and inherently expensive tasks

The creator notes that Excalidraw skill activations are naturally expensive because the task (drawing many slides with detailed visual layouts) requires the model to generate substantial output. Observability helps distinguish between:

- **Inherently expensive skills** (Excalidraw, complex document generation) — OK to be high-cost; focus on whether the output justifies it
- **Wasteful skills** (like the news monitor before optimization) — cost is not proportional to value; fix the skill logic
- **Tools with latency tax** (Notion MCP operations like update_page, create_database, search — all slow) — consider replacing with alternative (e.g., local Obsidian instead of Notion if you only need document storage)

---

## Per-skill cost metric

The `claude_code.cost.usage` metric exposes cost broken down by `skill.name` attribute:

```
metric: claude_code.cost.usage (USD)
attributes:
  - skill.name = "morning_brief"     (cost per run of this skill)
  - skill.name = "ai_news_monitor"   (cost per run of this skill)
  - skill.name = "excalidraw_deck"   (cost per run of this skill)
```

**"Cost per run" vs "accumulated cost":** The observability view shows both:
- **Accumulated view:** total spend across all invocations of a skill (morning_brief across multiple executions = high total)
- **Per-run cost:** average cost per single skill invocation (morning_brief = X tokens per execution)

Use per-run cost to identify the most expensive single skill run; use accumulated cost to find which skill drains the most budget overall.

**Optimization lever:** Once you identify a high-per-run cost skill, consider:
1. Downgrading the model (use Sonnet instead of Opus if the skill doesn't need full reasoning)
2. Reducing context size (trim unnecessary files, examples, or system instructions)
3. Restructuring the task (e.g., use code execution instead of MCP for repetitive operations)

---

## Subscription vs API framing

The creator frames it as: "If this stuff was actually going out through the API and not on my subscription, it'd be a waste of money."

This observation highlights the **implicit cost audit** available via Claude Code subscription:
- If you see a skill burning 100k tokens per run and you only invoked it once, that's acceptable within your monthly Pro/Max subscription
- But if you ran it 100 times, the same skill on a pay-as-you-go API would have cost thousands — a wake-up call to optimize

**Corollary:** Skills that are expensive on API pricing should be redesigned, regardless of whether you're on subscription or metered. The subscription masks the waste; observability reveals it so you can fix it.

---

## Enabling cost metrics via OpenTelemetry

To expose token usage, cache hit rate, and per-skill cost:

**Environment variables (minimal setup):**

```bash
CLAUDE_CODE_ENABLE_TELEMETRY=1                              # Required; telemetry is opt-in
OTEL_METRICS_EXPORTER=otlp|prometheus|console               # Choose backend
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317           # Default for OTLP
```

**Metrics produced (exact names from official catalog):**

- `claude_code.token.usage` (count) — with `type` attribute = [input, output, cacheRead, cacheCreation]
- `claude_code.cost.usage` (USD) — with `skill.name` attribute for per-skill breakdown
- `claude_code.session.count` (count)
- `claude_code.active_time.total` (seconds)

**Events with cache detail:**

The `api_request` event (from OTEL logs) carries:
- `cache_read_tokens` — how many input tokens came from cache
- `cache_creation_tokens` — how many new input tokens were written to cache
- Compute cache hit rate as: `cache_read_tokens / (cache_read_tokens + cache_creation_tokens)`

For the complete list of environment variables, cardinality controls, authentication options (mTLS), and event catalog, see [[claude-code-opentelemetry]].

**Note:** ⚠️ The panelized "dashboard UI" the video shows is **custom-built by the creator, not a first-party feature** — the customizable OTEL-fed dashboard must be built externally (Grafana, Prometheus, Datadog, custom OTLP consumer). For a quick *native* cost read you do have `/cost` (session API cost), `/usage` (token + plan-limit view), and `/stats` (usage heatmap) — but these read local/account data, not the OTEL pipeline. See [[observability-backend-stack]] for the external dashboard and [[jsonl-logs-and-native-dashboard]] for the native views.

---

## Observability as the measurement layer for cost optimization

This metrics collection serves a specific purpose in the [[../autonomous-loops-human-in-the-loop/_index]] + [[../claude-api-cost-optimization/_index]] stack:

1. **Cost optimization requires measurement** — you cannot improve what you don't measure. The cost metrics are the measurement layer.
2. **Identify the problem** — the news monitor example (32M tokens) would never have been discovered without this view.
3. **Quantify the fix** — after rewriting the skill, the same metrics show the improvement in real time.
4. **Set targets** — cache hit rate >80% is achievable (Anthropic Platform team guidance); observability lets you track progress toward it.
5. **Correlate with HITL approvals** — when a requires-approval task (sent to Telegram for human veto) is approved, you can audit the token cost of that decision in this metrics layer.

---

## Gotchas and limitations

- **Approximate costs only:** The `claude_code.cost.usage` metric is a best-effort approximation. Official billing from Claude Console (Anthropic's billing dashboard) is the authoritative cost source.
- **Cardinality explosion:** OTEL_RESOURCE_ATTRIBUTES with high-cardinality values (e.g., unique user IDs for every session) will explode your metrics backend storage. Use cardinality controls (see [[claude-code-opentelemetry]] for `OTEL_METRICS_INCLUDE_SESSION_ID` and related flags).
- **Default settings mask some costs:** Tool details (Bash commands, MCP names) are NOT logged by default. Enable via `OTEL_LOG_TOOL_DETAILS=1` if you need full audit trail of what operations the model invoked.
- **Cache metric only visible at event layer:** The cache_read_tokens / cache_creation_tokens attributes are exposed only in the OTEL `api_request` event. If you export metrics only (not logs/events), you lose cache visibility.
- **No native alert threshold:** OTEL itself does not set alerts (e.g., "alert if cost > $100/day"). You must implement that in your backend (Grafana alert rules, Prometheus rules, custom script).
- **Cowork coverage claim unverified:** The creator states Cowork can do "98% if not more of what you can do with your AI operating system." This is the creator's framing, not a measured claim. Cowork is a front-layer GUI for interactive sessions; observability tooling is separate from Cowork's capabilities.

---

## Key takeaways

- **Cache hit rate is the #1 lever** for cost reduction (~90% discount on cached reads, plus rate limit multiplication). The cost metrics make it visible.
- **Per-skill cost breakdown** lets you identify wasteful skills (e.g., the news monitor's 32M tokens) and optimize the highest-impact ones first.
- **Timestamp in system prompt is the silent cache killer** — any byte change invalidates everything after. Move timestamps to user message or use cache_control.
- **Observability exposes the waste; you fix it by rewriting the skill** — the cost metrics measure; the [[../claude-api-cost-optimization/_index]] lever (prompt caching) reduces.
- **Subscription vs API framing** — a skill that's "acceptable" on subscription might cost thousands on API; use observability to distinguish real efficiency from hidden waste.
- **Excalidraw and other inherently expensive tasks are OK** if the output justifies the cost; observability helps you tell the difference.
- **Requires-approval + Telegram HITL** (shown in the video) works with these cost metrics — when a human approves a task from their phone, you can audit its token cost immediately.
- **No native OTEL dashboard** ⚠️ — the panelized command center is custom-built; the OTEL-fed dashboard must be built externally (Grafana/Prometheus/Datadog). Native `/cost`, `/usage`, `/stats` give a quick local cost read (not OTEL-fed).
- **Available on Pro and Max plans** — OpenTelemetry is available to all subscription tiers (Pro, Max), not enterprise-only.

---

## See also

- [[overview]] — entry point to the claude-code-observability topic
- [[claude-code-opentelemetry]] — how to enable and configure OpenTelemetry (env vars, exporters, cardinality controls)
- [[opentelemetry-standard]] — OTEL spec, signals, OTLP protocol, backends
- [[observability-backend-stack]] — building dashboards with Grafana, Prometheus, Loki, Datadog
- [[mcp-and-skill-cost-metrics]] — diving deeper into per-tool latency and error rate
- [[../autonomous-loops-human-in-the-loop/_index]] — the HITL approval pattern (Telegram + requires-approval)
- [[../claude-api-cost-optimization/_index]] — prompt caching, cache hit rate targets, timestamp gotchas
- [[../claude-code-hooks/_index]] — hooks as the deterministic complement to telemetry
- [[../claude-skills/_index]] — skill design and cost management
