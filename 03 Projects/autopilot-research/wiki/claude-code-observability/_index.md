# Claude Code Observability — the OpenTelemetry "command center"

> **Topic:** How to make your *own* Claude Code usage observable — token spend, cache hit rate, MCP/tool latency + error rate, per-skill cost — via Claude Code's first-party **OpenTelemetry** export + **JSONL** session logs, visualized in an external dashboard.
> **Source video:** Mansel Scheffel (atomicOps), **"Claude Code + OpenTelemetry = Claude Command Center"** ([dITtLiC9FzM](https://www.youtube.com/watch?v=dITtLiC9FzM), 2026-04-22, 15:54, ~15.2K views) — **third-party creator, NOT first-party Anthropic.**
> **Compiled:** 2026-06-20 (path 5 yt-dlp full transcript + double deep-dive of the originals + adversarial verify, Workflow `wf_5398ccab-88a`).
> **Maintained by:** Claude Code librarian per `../../CLAUDE.md`.

---

## What this is (and the contrarian thesis)

The video's clickbait title undersells a sharp, **contrarian** argument: most "mission control" agent dashboards on YouTube are **context bloat** ("a seven-layer microservice that doesn't need to exist"). For the agent *front-layer*, the creator says just use [[../claude-cowork/_index|Cowork]]. The real value of a command center is **observability-first** — and that's the genuinely first-party-grounded part, because Claude Code emits two data sources you can exploit:

1. **OpenTelemetry (OTEL)** — opt-in (`CLAUDE_CODE_ENABLE_TELEMETRY=1`) metrics + events/logs over OTLP, to any backend (Grafana/Prometheus/Loki, Datadog, …). This is the load-bearing original.
2. **JSONL session logs** — every session transcript at `~/.claude/projects/.../<uuid>.jsonl` (tokens incl. cache, tools, model), parseable offline (e.g. `ccusage`).

The panels that matter: **token-by-model**, **cache hit rate** (the #1 cost lever — the measurement layer for [[../claude-api-cost-optimization/_index]]), **MCP/tool latency + error rate**, **skill activations + cost-per-run**, **context health**, **skills registry** — plus a small task/scheduling layer with **Telegram approval (HITL)**.

> **Headline for the operator:** the highest-leverage move here is on **your own `~/.claude`** — flip on `CLAUDE_CODE_ENABLE_TELEMETRY=1` + a local Grafana/Prometheus and you can *see* your real token/cache/MCP/skill spend today. That directly measures the cache-hit-rate + token levers from your cost-optimization pilot. Pilot menu: `output/(C) 2026-06-20-claude-code-observability-pilot-methods.md`.

---

## Articles in this topic

| Article | What it covers |
|---|---|
| [[overview]] | The observability-first thesis, the "skip mission control / use Cowork" stance, the two data sources, and the topic map |
| [[claude-code-opentelemetry]] | **The load-bearing original** — `CLAUDE_CODE_ENABLE_TELEMETRY` + the OTEL_* config, the metric & event catalogs, exporters, cardinality controls, plan availability, native usage views |
| [[opentelemetry-standard]] | What "OTEL" actually is (CNCF) — the 3 signals, OTLP (4317/4318), the Collector, semantic conventions; why backend-agnostic emission is the leverage; Claude Code emits metrics+logs, not full traces |
| [[observability-backend-stack]] | Turning OTLP into a dashboard — Collector → Prometheus + Loki → Grafana, vs managed (Grafana Cloud / Datadog / Honeycomb); self-host-vs-managed tradeoff; community stacks (verify before use) |
| [[cost-cache-token-metrics]] | The cost panels — token-by-model, **cache hit rate** (~0.1× / ~90%-off reads; the timestamp killer), per-skill cost, "where your tokens actually go", subscription-vs-API framing |
| [[mcp-and-skill-cost-metrics]] | The activity panels — MCP/API latency + error rate, web_fetch-error diagnosis, skill activations vs consumption, failures + event-driven alerts, recent sessions, slowest tools, context health, skills registry |
| [[task-queue-scheduling-telegram-hitl]] | The small task layer — schedule-the-predictable vs ad-hoc, per-skill **model assignment**, requires-approval → **Telegram HITL**, event-driven alerting |
| [[jsonl-logs-and-native-dashboard]] | The 2nd data source — JSONL transcript format + token fields, native `/cost` `/usage` `/stats` + statusline, `ccusage`, JSONL-vs-OTEL decision |
| [[code-execution-mcp-workaround]] | The deferred "another video" — why MCP is token-hungry + the **code-execution / programmatic tool calling** fix (load tools on demand, filter results in code) |
| [[video-to-original-crosswalk]] | Every video claim → canonical original → verdict; what the video ADDS / SIMPLIFIES / OMITS (+ the "build your own" method) |
| [[source-provenance]] | What's first-party-verified vs creator-personal vs unverifiable; the over-correction caught in verify; single-source-flagged metric names |

---

## How this relates to the prior `agent-dashboard-os` topic (Rule 7)

[[../agent-dashboard-os/_index]] is the **abstract observability *landscape*** (tracing / status-line / tmux / sandboxes) from a weak, ⚠️-anchor-miss 6-video bundle. This topic is the **concrete, first-party-anchored Claude-Code-OTEL *implementation*** of that landscape. Where they overlap on OTEL specifics, **prefer this topic** — it's grounded in the first-party `monitoring-usage` docs + an adversarial verify pass, not a NotebookLM bundle. They complement, not duplicate.

---

## Related topics

- [[../claude-api-cost-optimization/_index]] — cache hit rate + token spend are the metrics this dashboard *measures*; observability is the measurement layer for that cost pilot
- [[../agentic-analytics-harness/_index]] — Omni's "observability over scorecards" + daily trace-driven session triage = the same discipline at production scale
- [[../telegram-remote-control-stack/_index]] — the Telegram HITL approval stack (operator already pilot-verified Recipe A)
- [[../prompt-evaluation/_index]] — trace-driven eval triage (observability feeds eval)
- [[../claude-cowork/_index]] — the creator's "just use Cowork" front-layer recommendation
- [[../claude-code-hooks/_index]] — hooks as the deterministic complement to telemetry
- [[../autonomous-loops-human-in-the-loop/_index]] — the HITL approval framing (drafts-not-sends)
- [[../claude-skills/_index]] — skill cost metrics
- [[../harness-engineering/_index]] — observability as a first-class harness property
