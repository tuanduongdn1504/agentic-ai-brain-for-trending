# Video-to-Original Crosswalk: Claude Code + OpenTelemetry = Claude Command Center

> **Video:** Mansel Scheffel (atomicOps), *Claude Code + OpenTelemetry = Claude Command Center*, YouTube dITtLiC9FzM (2026-04-22, 15:54)
>
> **Thesis:** Observability-first dashboards (metrics + logs) deliver more operational value than elaborate multi-agent "mission control" systems. Argues against context bloat via skills + scheduling instead of autonomous agents; proposes Telegram human-in-the-loop (HITL) approval gate for ad-hoc tasks.

## Source

**Raw file:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-06-20-claude-code-otel-command-center.md`

**Original resources cited/inferred:**
- https://code.claude.com/docs/en/monitoring-usage (Claude Code official OpenTelemetry docs)
- https://code.claude.com/docs/en/sessions.md (JSONL session logging)
- https://opentelemetry.io/docs/ (OpenTelemetry specification)
- https://www.anthropic.com/engineering/code-execution-with-mcp (MCP token optimization)
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching (cache hit rate mechanics)

---

## Mapping Table: Video Claim → Original Source → Verdict

| Video Claim | Creator Quote (Timestamp) | Original Resource | Verdict | Notes |
|---|---|---|---|---|
| OpenTelemetry released to Max/Pro plans; previously enterprise-only | [02:17] "they finally released to people on the Max and Pro plans. Previously, it was only for enterprise people" | Claude Code official monitoring-usage docs | **CONFIRMED (partial)** | Official docs show CLAUDE_CODE_ENABLE_TELEMETRY available on Pro/Max. No evidence of enterprise-only era — likely always available to these tiers. "Finally released" may be creator's perception, not fact. |
| JSONL logs track everything Claude and Claude Cowork use | [01:50] "JSONL logs, which is just tracking everything that Claude and Claude co-work use" | Claude Code sessions.md + community tools (ryoppippi/ccusage, ccstat) | **CONFIRMED** | Claude Code writes JSONL at `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`. Cowork writes identical JSONL format to `~/Library/Application Support/Claude/local-agent-mode-sessions/`. Both track complete transcript + token usage (input/output/cache_creation/cache_read). |
| Shiny but mediocre dashboard inside Claude Code GUI, fed partially by OTEL | [02:17] "this shiny little mediocre dashboard inside Claude code in the GUI. This dashboard over here is fed partially from OTEL" | Claude Code official docs + command reference | **PARTIALLY REFUTED** | Native usage *views* DO exist — `/cost` (session API cost), `/usage` (tokens + plan limits), `/stats` (usage heatmap), the statusline — plus a **Console Analytics dashboard** for Team/Enterprise. But these read local/account data, **not** the OTEL pipeline, and none is a customizable OTEL-fed *panel* dashboard. The rich command center in the video is the creator's **external** build (Grafana/Datadog/etc.). So "shiny dashboard… fed by OTEL" conflates a native view with a custom OTEL build. |
| OTEL exposes cache hit rate, token usage by model, MCP/tool latency + error rate, per-skill cost | [04:29], [09:33], [10:27] "cache hit rate", "latency and error rate of all the tools", "cost… per run" | Claude Code metrics/events catalog (verified official) | **CONFIRMED** | claude_code.cost.usage metric; token.usage metric with type=[input\|output\|cacheRead\|cacheCreation] and model attribute; tool_result event has duration_ms and success attribute; cost.usage metric has skill.name attribute. All verified in official metric/event catalogs. |
| Don't use named agents; use skills on schedules instead | [00:27]–[00:55] "You do not need named agents… It's way more efficient just to use skills and have them running on demand, on schedules" | Claude Code skills architecture + /schedule command | **CONFIRMED** | Skills exist as first-class reusable units. Scheduling via Cowork UI or Claude Code CLI is documented. Agent-per-task pattern does increase context load. |
| Cowork handles 98% of what mission control can do | [00:55] "co-work… 98% if not more of what you can do… in this little graphical user interface" | Anthropic Cowork docs (public beta 2026-Q1) | **CREATOR'S ESTIMATE, UNVERIFIED** ⚠️ | Cowork provides interactive multi-turn UI for Claude Code. The "98%" figure is creator's subjective assessment, not a documented metric. Flag as opinion. |
| Task-queue with per-skill model assignment reduces context load | [06:49]–[07:16] "assign the model… Don't use Opus for everything. Sonnet works fine for most tasks" | Claude Code platform docs + Anthropic Platform cost optimization (Puneet Shah, May 2026) | **CONFIRMED** | Per-skill model assignment is a first-class feature. Anthropic Platform team explicitly highlights this as Lever 3c for cost reduction. Reduces context bloat by routing task-appropriate work to smaller models. |
| Requires-approval task pings Telegram; you approve from phone | [07:43]–[08:09] "requires approval… linked to my cell phone via Telegram… It's asking for approval. All I need to do is hit approve" | Telegram Bot API + Claude Code Channels (beta) | **CONFIRMED (pattern) / IMPLEMENTATION UNVERIFIED** ⚠️ | The MECHANISM (Telegram API + approve callback) is standard + feasible. The creator's specific UI implementation is custom-built and unreleased. Cannot replicate exact implementation without creator's codebase. See [[../telegram-remote-control-stack/_index]] for documented setup recipe. |
| AI news monitor used 32 million tokens across 23 sessions | [10:27] "our AI news monitor… ran it over 23 sessions… used 32 million tokens" | Creator's personal metric from JSONL analysis | **CREATOR'S PERSONAL DATAPOINT, UNVERIFIABLE** ⚠️ | This is the creator's own measured usage. No public data to verify. User can reproduce by parsing their own `~/.claude/projects` JSONL with `ccusage` tool if desired. |
| Cache hit rate is the #1 cost reduction metric | [04:29] "cache hit rate… super important… save you some of your usage limit" | Anthropic Platform team (Puneet Shah, Code with Claude London May 2026) | **CONFIRMED (first-party)** | Anthropic Platform team explicitly frames prompt caching as #1 lever: "90% off cached reads", ">80% hit rate target". Official docs: https://platform.claude.com/docs/en/build-with-claude/prompt-caching. Video shows observability UI visualization of this metric — measurement layer, not discovery. |
| Timestamp in system prompt kills cache hit rate | [Implied from 04:29 context] | Anthropic Platform guidance (Puneet Shah) | **CONFIRMED (first-party)** | Direct quote from Anthropic Platform talk: "The #1 silent cache killer is a timestamp in the system prompt. Any byte change in the prefix invalidates everything after it." Documented in [[../claude-api-cost-optimization/_index]] as critical cache discipline. |
| MCP is token-hungry and pollutes context; code execution is workaround | [12:44] "MCP… it is really hungry… constant back and forths… pollute… There are ways around using MCP directly. We can use code execution" | Anthropic engineering post: "Code execution with MCP: building more efficient agents" + Platform tool-search docs | **CONFIRMED** | Baseline 55K tokens for typical 5-10 MCP setup. Code execution documented 98.7% reduction (150K→2K tokens). Tool search + defer_loading >85% reduction. Cross-referenced in [[../claude-api-cost-optimization/_index]] as Lever 2a–2c. |
| Notion tools (update-pages, create-databases, search) show high latency | [12:44] "working in Notion, update pages really slow, create databases slow, search is slow" | Anthropic engineering post (hypothetical examples, not Notion-specific) | **PARTIAL / UNCONFIRMED** ⚠️ | Anthropic engineering post documents MCP latency issue in general but uses hypothetical examples (Google Drive, Salesforce, Slack), NOT Notion. Community reports (dev.to, r/mcp) confirm MCP overhead is real; Notion not singled out in first-party sources. Creator may have measured own Notion latency, but it's not in originals. |
| Build your own dashboard via prompt; copy → paste → plan mode | [15:00]–[15:27] "copy this prompt… flip it over to plan mode… do some of the latest research for the hotel logs and JSON L" | Creator's unreleased prompt (Google Drive folder + Skool community) | **METHOD CONFIRMED / IMPLEMENTATION UNVERIFIED** ⚠️ | The METHOD (plan-mode agent task with docs-grounding) is standard practice. The actual prompt lives at https://drive.google.com/drive/folders/15NZmCSXg3PEXWE1UumodEfJUXY9oF95W (access unknown) + requires membership in https://skool.com/ainative (paid community). Cannot verify exact behavior or quality without access. |

---

## What the Video ADDS Beyond Official Originals

### 1. **Observability-first Contrarian Thesis**
The video's core argument — "skip mission control complexity, go observability-first" — is NOT present in official Claude Code docs. Official documentation focuses on "how to configure telemetry"; it does not recommend observability-first as an *architectural philosophy*. The creator distills this insight from first principles (MCP context bloat → solution is observability + scheduling, not more agents).

### 2. **Curated Dashboard Panel Selection**
The panels shown are hand-picked from the official OTEL metric + event catalog, but the specific visualizations are creator-built:
- **"Posture"** skill (MCP poisoning audits) — creator's unreleased custom build ⚠️
- **"Context health"** skill (context engineering efficiency) — creator's unreleased custom build ⚠️
- **"IQ agent"** (task router between Sonnet/Opus based on task complexity) — creator's unreleased custom build ⚠️
- **"Task queue with requires-approval → Telegram notification"** — creator's custom HITL layer

The originals expose the RAW metrics/events; the video shows ONE POSSIBLE COMPOSITION into operational dashboards. Other compositions (per-model token trends, cache-hit-rate per-skill, error-rate alerting) are equally valid.

### 3. **Telegram-Approval HITL Pattern**
The specific "requires-approval → Telegram ping → approve-from-phone → resume" pattern is NOT documented in Anthropic's official docs. It's a custom integration the creator built. The video demonstrates the practical HITL workflow; the originals provide only the building blocks (Telegram API, Claude Code SDK, Channels beta, Stop Hooks). See [[../telegram-remote-control-stack/_index]] for the documented setup recipe (Recipe A already pilot-verified).

### 4. **"Skip Mission Control, Use Cowork" Editorial Position**
The creator explicitly argues AGAINST trendy autonomous-agent dashboards. This is editorial opinion on top of technical facts. Official docs describe Cowork's capabilities; they do not recommend "Cowork instead of mission control." The video's contrarian positioning is the value-add; the facts are standard.

---

## What the Video SIMPLIFIES or CONFLATES

### 1. **OTEL ≠ JSONL (terminology loose)**
The video uses "OTEL" loosely to describe:
- JSONL session logs (Claude Code's native LOCAL storage format, NOT OTEL protocol)
- Exported metrics via OTLP (which IS OTEL protocol)
- In-GUI dashboard visualization (claimed to be "partially OTEL-fed" — NOT confirmed in official docs)

**Reality:** OTEL is the EXPORT LAYER (metrics+logs → OTLP endpoint to external backends). JSONL is Claude Code's LOCAL STORAGE LAYER. They are orthogonal. You can analyze JSONL locally without OTEL; you can export via OTEL without ever looking at JSONL.

### 2. **Distributed Traces Completely Absent**
OTEL has THREE signals: metrics, logs, **traces**. The video focuses entirely on metrics and logs. Distributed tracing (span lineage across API calls, tool calls, hook executions) requires CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1 and is in beta. Traces are not discussed.

### 3. **Dashboard Engineering Work Is Invisible**
The video shows a fully functional dashboard with zero explanation of:
- Which observability backend (Grafana? Datadog? Custom? — **NEVER NAMED** ⚠️)
- How the panels query OTEL data (PromQL for Prometheus? SQL for managed backend?)
- How the Telegram integration hooks into the queue (polling? webhooks? stop-hook?)
- The 30–50 hours of dashboard infrastructure work

The creator's "build your own" prompt is meant to accelerate this, but it's gated behind Google Drive + Skool community membership (not public).

---

## Critical Omissions and Gotchas

### 1. **The Backend Identity is Intentionally Undisclosed** ⚠️
The video never states which observability platform the creator uses. Without knowing the backend, viewers cannot reproduce the exact stack. The OTEL protocol supports 90+ vendors (Prometheus, Loki, Honeycomb, Datadog, New Relic, SigNoz, Logfire, Splunk, etc.). The creator chose one; viewers must choose independently.

### 2. **Collector Setup Not Addressed** ⚠️
OTEL requires a Collector component (receives OTLP → processes → exports to backend). The video assumes it's running but never explains:
- How to deploy it (Docker Compose? Kubernetes? Local binary?)
- Which config (receivers, processors, exporters for the backend of choice)?
- Port defaults (4317 gRPC, 4318 HTTP)?

Official OpenTelemetry Collector docs are comprehensive but separate from Claude Code docs. Users must follow both.

### 3. **Cost/Cardinality Tradeoff Unstated** ⚠️
Exporting telemetry at scale has real cost implications:
- **Self-hosted (Prometheus + Loki):** Zero license, high ops burden (storage, backups, alerting, Kubernetes expertise)
- **Managed (Grafana Cloud):** ~$6.50 per thousand metric series per month
- **SaaS (Datadog):** Fully usage-based, can be $1000+/month for high-volume telemetry

The creator's personal "news monitor using 32M tokens" would be expensive to observe if paying per metric series. The video does not mention this tradeoff.

### 4. **OTLP Endpoint Security Not Covered** ⚠️
By default, OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 (plaintext HTTP). Production deployments require:
- mTLS certificates (OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE / CLIENT_KEY)
- API keys (OTEL_EXPORTER_OTLP_HEADERS=Authorization:Bearer token)
- Network isolation (firewall, private VPC)

The video mentions none of this.

### 5. **"Build Your Own" Prompt is Gated** ⚠️
Creator states [15:00]: "I've written you a prompt" to build the dashboard. **Reality:** The prompt lives at https://drive.google.com/drive/folders/15NZmCSXg3PEXWE1UumodEfJUXY9oF95W (Google Drive, access unknown) + requires membership in https://skool.com/ainative (paid community).

The prompt itself is **not publicly reproducible** without:
- Access to the Google Drive folder
- Paid Skool community membership

### 6. **Three Key Components Are Unreleased Custom Builds** ⚠️
Three core panels/skills shown are creator's proprietary builds, not publicly available:
- **"IQ agent"** (task router between Sonnet/Opus based on task complexity) — unreleased
- **"Posture skill"** (MCP poisoning audits) — unreleased
- **"Context skill"** (context engineering efficiency audit) — unreleased

The demo assumes viewers have these (or will build them). Official Claude Code does not include them.

### 7. **"Plan Mode" Reference is Procedural, Not Automatic** ⚠️
Creator says [15:27]: "flip it over to plan mode. Of course, you don't just want to yolo your way through this."

**What is "plan mode"?** Claude Code's `/plan` command (interactive planning before execution). The creator's custom prompt presumably instructs the LLM to use `/plan` internally. This is a procedural step, not a UI mode. Viewers must read the actual prompt to understand the workflow.

---

## Verified Configuration Reference

**OTEL Configuration (all verified against official docs):**

```bash
# Enable telemetry (required; opt-in)
CLAUDE_CODE_ENABLE_TELEMETRY=1

# Exporter choices (default: none until configured)
OTEL_METRICS_EXPORTER=otlp|prometheus|console|none
OTEL_LOGS_EXPORTER=otlp|console|none
OTEL_TRACES_EXPORTER=otlp|console|none  # requires CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1

# OTLP endpoint (default: http://localhost:4317)
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_EXPORTER_OTLP_PROTOCOL=grpc|http/json|http/protobuf

# Export intervals (in milliseconds)
OTEL_METRIC_EXPORT_INTERVAL=60000    # default
OTEL_LOGS_EXPORT_INTERVAL=5000       # default

# Cardinality controls
OTEL_METRICS_INCLUDE_SESSION_ID=true|false        # default true
OTEL_METRICS_INCLUDE_ACCOUNT_UUID=true|false      # default true
OTEL_METRICS_INCLUDE_VERSION=true|false           # default false
OTEL_METRICS_INCLUDE_ENTRYPOINT=true|false        # default false

# Content logging (opt-in; off by default)
OTEL_LOG_USER_PROMPTS=1         # enable prompt content logging
OTEL_LOG_TOOL_DETAILS=1         # enable Bash commands, MCP names, tool input
OTEL_LOG_TOOL_CONTENT=1         # enable full tool input/output (60KB truncation)
OTEL_LOG_RAW_API_BODIES=1|file:<dir>  # full Messages API bodies
```

**Metric Catalog (8 metrics; from the first-party `monitoring-usage` docs fetch):**
- `claude_code.session.count` (count) ✅
- `claude_code.lines_of_code.count` (count) ✅
- `claude_code.pull_request.count` (count) ⚠️ single-source (not re-confirmed by cross-check)
- `claude_code.commit.count` (count)
- `claude_code.cost.usage` (USD) — includes `skill.name` attribute ✅
- `claude_code.token.usage` (tokens) — includes type=[input|output|cacheRead|cacheCreation], model attribute (the `type` key itself ⚠️ not re-confirmed)
- `claude_code.code_edit_tool.decision` (count) ⚠️ single-source (may surface as a `tool_decision` event)
- `claude_code.active_time.total` (seconds) ✅

> ⚠️ The ✅ names were corroborated by an independent cross-check; the ⚠️ names came only from the first-party docs fetch and weren't re-verified (docs truncation). See [[source-provenance]].

**Event Catalog (24+ events verified):**
user_prompt, tool_result, api_request, api_error, api_refusal, api_request_body, api_response_body, tool_decision, permission_mode_changed, auth, mcp_server_connection, internal_error, plugin_installed, plugin_loaded, skill_activated, at_mention, api_retries_exhausted, hook_registered, hook_execution_start, hook_execution_complete, hook_plugin_metrics, compaction, feedback_survey

**Tool Result Event Attributes (for MCP latency + error rate):**
- `duration_ms` — latency of tool call
- `success` — true/false for error rate tracking

---

## Key Takeaways

1. **Observability ≠ mission control:** The video's main claim is architectural opinion, not technical discovery. Metrics + logs are useful; autonomous-agent dashboards add complexity. This insight is creator's distillation, not official guidance.

2. **OTEL is the export layer; JSONL is local storage:** These are orthogonal concerns. Both are useful; conflating them is a common mistake.

3. **Cache hit rate is the #1 cost lever (first-party).** The video's dashboard visualization of this metric is the measurement layer, not a new discovery. Anthropic Platform team already made this explicit.

4. **Requires-approval → Telegram → phone approval is a feasible HITL pattern.** Uses standard APIs (Telegram Bot, Claude Code Channels, Stop Hooks). The creator's implementation is unreleased; the mechanics are documented in [[../telegram-remote-control-stack/_index]] (Recipe A already pilot-verified).

5. **The backend is intentionally unspecified.** Viewers must choose from 90+ OTLP-compatible backends and build the dashboard panels themselves. Self-hosted (Prometheus + Loki) is free but ops-intensive. Managed (Grafana Cloud, Datadog) has monthly cost.

6. **Per-skill model assignment + scheduled tasks > autonomous agents.** This is sound engineering and aligns with Anthropic Platform recommendations. Reduces context load and cost without requiring elaborate dashboards.

7. **MCP is context-expensive; code execution (programmatic tool calling) is the documented workaround.** Video defers this to "another video"; verified 98.7% token reduction in originals ([[../claude-api-cost-optimization/_index]]).

8. **IQ agent, Posture, Context skill are creator-specific unreleased builds.** Viewers should not expect to find these in Claude Code docs or public repos. Implementation details are unverifiable.

9. **Timestamp in system prompt is a silent cache killer.** First-party Anthropic guidance (Puneet Shah). Affects every cached session — critical for observability discipline.

10. **"Plan mode" is procedural (`/plan` command), not automatic.** The creator's prompt presumably instructs the LLM to use it. Viewers must access the prompt to understand the exact workflow.

---

## For Operators: How to Get Started

**If you want to replicate this stack:**

1. **Choose your backend first:** Datadog (simplest SaaS), Grafana Cloud (cost-effective managed LGTM), or self-hosted Grafana+Prometheus+Loki (no license, high ops burden)

2. **Follow official Claude Code monitoring-usage docs:** Set CLAUDE_CODE_ENABLE_TELEMETRY=1 + exporter configuration

3. **Deploy observability stack:** Use official OTel Collector docs + vendor-specific setup guides

4. **Implement requires-approval HITL:** Follow [[../telegram-remote-control-stack/_index]] Recipe A (already pilot-verified 2026-05-08)

5. **Build dashboard panels:** Via PromQL (Prometheus) or SQL (managed backend) to expose the 8 metrics + key events

6. **(Optional) Access creator's prompt:** Via https://skool.com/ainative or https://bit.ly/3TinLo5 to accelerate dashboard-building (paid community)

**Most valuable to adopt immediately (first-party recommendations):**
- Cache-hit-rate monitoring (target >80%; Anthropic: 90% off cached reads)
- Per-skill model assignment (Sonnet for simple tasks, Opus for complex reasoning)
- Scheduled tasks instead of autonomous agents (reduces context bloat)
- Timestamp discipline in system prompts (avoid silent cache invalidation)

These are documented in [[../claude-api-cost-optimization/_index]] and deliver 3–5x cost reduction without custom dashboard engineering.

---

## Next Action

Decide: Do you want observability dashboards now (high setup cost, high insight gain) or defer and start with scheduled tasks + per-skill model assignment (low setup, high ROI)? The video makes the case for dashboards; the originals make the case for prompt-caching discipline. Both are complementary.
