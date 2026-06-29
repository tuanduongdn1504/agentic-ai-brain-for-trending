# OpenTelemetry: The Open Standard

> **What this article does:** Explains OpenTelemetry (OTel) the CNCF open standard — the three signals (traces/metrics/logs), OTLP wire protocol (gRPC 4317, HTTP 4318), Collector architecture, semantic conventions — so readers understand what the Claude Code + OTEL video means by "command center" and "OTEL". Key clarification: Claude Code emits **metrics and logs only** (not full distributed traces), so the "command center" dashboard is metrics/logs-driven.

> **Source video:** Mansel Scheffel, "Claude Code + OpenTelemetry = Claude Command Center", 2026-04-22, atomicOps consultancy. Timestamp [02:17] introduces OTel as the load-bearing observability protocol.

## Source

**Raw file:** `/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research/raw/2026-06-20-claude-code-otel-command-center.md`

**Original resources:**
- [OpenTelemetry documentation](https://opentelemetry.io/docs/) — official specs, SDKs, semantic conventions, collector guides
- [OTLP specification](https://opentelemetry.io/docs/specs/otel/protocol/exporter/) — wire protocol (gRPC, HTTP)
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) — architecture (receivers, processors, exporters)
- [Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) — standardized naming across platforms
- Claude Code monitoring docs (Max/Pro plans) — metric and event catalog

---

## What is OpenTelemetry?

OpenTelemetry (OTel) is a **CNCF-governed, vendor-neutral open standard** for collecting, processing, and exporting telemetry data (observability signals) from applications and infrastructure. It resulted from the 2019 merger of OpenTracing and OpenCensus, representing significant industry commitment from 90+ vendor partners.

**Core principle:** Emit observability data once, route to any backend without lock-in. The protocol is backend-agnostic — Datadog, Grafana, Prometheus, Loki, Honeycomb, Splunk, AWS, New Relic, Dynatrace, and 80+ others all speak OTLP natively.

---

## The Three Signals

OTel standardizes **three orthogonal observability signals** that together answer "HOW?", "WHAT?", and "WHY?" about system behavior:

### **Traces** — Request flow through services
- Records the path a request (or workflow) takes as it moves through systems
- Each trace contains **spans** (individual operations with start/end time, attributes, status)
- Spans form a directed acyclic graph (DAG) showing parent/child relationships and timing
- Example: HTTP request → database query → cache lookup → response
- **Claude Code caveat:** Claude Code does NOT emit full distributed traces in the traditional sense (no root/child span lineage through external API calls). It emits metrics and logs instead. ⚠️

### **Metrics** — Quantitative runtime measurements
- Gauge: current value (e.g., active connections)
- Counter: monotonically increasing tally (e.g., total requests)
- Histogram: distribution of values (e.g., request latency percentiles)
- Example: `http.server.request.duration = 45ms`, `system.cpu.usage = 42%`
- **Claude Code emits:** token usage by model, cache hit rate, MCP/API latency and error rates, skill activations, cost per run
- Collected at regular intervals (e.g., every 60 seconds)

### **Logs** — Timestamped event records
- Structured or free-form text with timestamp, severity, attributes
- Tied to specific events in the application lifecycle
- Used for debugging and auditing
- **Claude Code emits:** JSONL logs capturing all Claude and Cowork activity (session transcripts, events)
- Can be sampled (not all logged) to reduce volume

**Key insight:** Traces are expensive (fine-grained span data), metrics are cheap (aggregated), logs are in between. Use the right signal for the right question.

---

## OTLP: The Wire Protocol

**OTLP (OpenTelemetry Protocol)** is the standardized transport for emitting signals from applications to observability backends. It is **backend-agnostic** — the protocol focuses on HOW data is structured and moved, not WHERE it goes.

### **Transport options**

| Transport | Port | Use Case |
|---|---|---|
| **gRPC + Protobuf** (HTTP/2) | **4317** | Default, bidirectional, efficient binary, low latency |
| **HTTP/Protobuf** | **4318** | Recommended default for new deployments, firewall-friendly |
| **HTTP/JSON** | Variable | Compatibility with systems that don't support Protobuf |

Most enterprise deployments use **4317 (gRPC)**; **4318 (HTTP/Protobuf)** is the specification recommendation for new builds.

### **Latency**

OTLP transports emit data at ~100ms typical latency, enabling near-real-time dashboards and alerting. This is fast enough for human-in-the-loop (HITL) approval workflows (e.g., Telegram alerts when a scheduled task needs sign-off).

### **Backend-agnostic routing**

Once a system emits OTLP, you can:
1. Plug any OTLP-compliant backend (Datadog, Grafana, Prometheus, Loki, custom HTTP receiver) without code changes
2. Use the same OTLP data stream across multiple backends simultaneously (e.g., Grafana for dashboards + Splunk for long-term archive)
3. Switch backends by changing only the OTLP exporter endpoint configuration

This is the **leverage of the standard** — the protocol is stable, the routing is flexible.

---

## OpenTelemetry Collector Architecture

The **OTel Collector** is a standalone daemon that receives, processes, and exports telemetry. It runs in two modes:

### **Agent mode** (per-system, local)
- Lightweight daemon on each application server
- Collects telemetry from local processes (via gRPC, HTTP, or protocol-specific receivers like Prometheus scrape)
- Pre-processes (batch, transform, filter) before export
- Reduces network chatter and central load

### **Gateway mode** (centralized)
- Collector runs on a central node
- Multiple agents or applications push to the gateway
- Gateway aggregates, processes, and exports to backends
- Useful for organizations with strict data residency / firewall rules

### **Pipeline architecture: Receivers → Processors → Exporters**

```
[Applications/Agents]
         ↓
    [Receivers]  (accept OTLP, Prometheus, Jaeger, Fluent, Syslog, ...)
         ↓
    [Processors]  (batch, memory limit, trace sampling, encryption, filtering, ...)
         ↓
    [Exporters]   (send to Datadog, Grafana, Prometheus, Loki, S3, stdout, ...)
```

**Example receiver:** `otlp` (listens on port 4317/4318 for OTLP telemetry)
**Example processor:** `batch` (batches 512 spans before export, improves throughput)
**Example exporter:** `grafana` (sends to Grafana Cloud), `prometheus` (exposes `/metrics` for scrape)

**Deployment note:** The Collector itself can be containerized (Docker) or run as a system service (systemd). It is often the first layer in an observability stack.

---

## Semantic Conventions

**Semantic Conventions** are standardized naming and attribute schemas for operations, resources, and events across traces, metrics, logs, and profiles. They ensure interoperability across platforms and teams.

Examples:
- `http.method` = "GET", `http.status_code` = 200, `http.response_content_length` = 1024
- `db.system` = "postgresql", `db.operation` = "SELECT", `db.rows_affected` = 42
- `rpc.service` = "MyService", `rpc.method` = "GetUser"

**Adoption:** Semantic Conventions are recommended but **not enforced by OTLP itself**. Adoption varies by tool. Using them ensures your telemetry is understood by downstream systems and colleagues.

---

## SDK vs. API

### **API** — What your code calls
- Interfaces for recording spans, metrics, logs, baggage (context propagation)
- Language-specific: Python, Java, Go, JavaScript, .NET, Ruby, PHP, Rust, etc.
- Example: `tracer.start_as_current_span("my_operation")` (Python)

### **SDK** — The implementation layer beneath the API
- Processes and batches telemetry (span processing, metric aggregation, resource attribution)
- Configures transport (OTLP exporter endpoint, TLS, authentication)
- Handles lifecycle (initialization, shutdown, resource cleanup)

**Auto-instrumentation:** Many languages offer auto-instrumentation that injects OTel collection without code changes (e.g., Java bytecode instrumentation, Python monkey-patching). This simplifies adoption in legacy applications.

---

## Claude Code + OTEL: Metrics and Logs Only

**Important clarification:** Claude Code emits **metrics and logs**, NOT full distributed traces in the traditional sense.

### **What Claude Code emits (Max/Pro plans)**

**Metrics (quantitative, aggregated):**
- Token usage by model (Claude 3.5 Sonnet, Opus, Haiku)
- Cache hit rate (% of requests served from Anthropic's prompt cache)
- MCP tool latency and error rates
- API/tool latency and error rates
- Skill activation frequency (count per 24 hours)
- Cost per run (USD)

**Logs (JSONL format):**
- Session transcripts (all Claude and Cowork activity)
- Event records with timestamp
- Full context for debugging individual runs

**Not emitted:**
- Span-level distributed traces (no root/child lineage through external API calls)
- Profile data (CPU flame graphs, memory allocation stacks)

### **The in-GUI dashboard**

The Claude Code GUI dashboard is **partially fed by OTLP metrics**. The creator (Mansel Scheffel) built a **custom, metrics-and-logs-driven dashboard** that supplements the GUI. This custom dashboard required:
1. Running an OTel Collector locally (agent mode) to receive OTLP from Claude Code
2. Configuring a backend (Grafana + Prometheus + Loki, or a managed service)
3. Writing custom dashboard panels and alerting logic
4. Routing events to Telegram for human-in-the-loop (HITL) approval

**The video claim:** ⚠️ "OTEL gives you real-time info you can exploit because there is a ton of documentation" [02:17]

**Verification:** CONFIRMED. OpenTelemetry documentation is comprehensive (specs, SDKs, semantic conventions, Collector guides, 90+ vendor integrations). Real-time metric and log emission is standard via OTLP at <100ms latency. Documentation abundance IS a genuine advantage for building custom observability solutions. **Caveat:** The user must write custom dashboard, alerting, and event routing logic — it is not automatic.

---

## Real-Time Exploitation Feasibility

With OTel, real-time exploitation of Claude Code observability is **fully feasible** but requires work:

### **The minimal stack**

1. **OTel Collector (agent mode)** — runs locally on your dev machine or CI/CD box, receives OTLP from Claude Code
2. **Observability backend** — open-source (Grafana + Prometheus for metrics + Loki for logs) or managed (Grafana Cloud, Datadog, Honeycomb)
3. **Custom dashboard and alerting** — write Grafana panels, set threshold alerts, hook alerts to Telegram/Slack/email

### **Example workflow**
- Claude Code emits metric `skill.activations.count = 10` every 60 seconds
- Collector receives OTLP, forwards to Prometheus
- Prometheus scrapes every 15 seconds, stores time-series
- Grafana queries Prometheus, displays real-time skill activation chart
- Alert rule triggers if activation rate drops below threshold, sends Telegram notification
- Operator receives notification, reviews logs, takes action

### **Latency budget**
- Claude Code → Collector: ~10–50ms (local network)
- Collector → Backend: ~10–100ms (depends on network + backend)
- Dashboard render: ~100–500ms (browser)
- **Total:** ~200ms typical, enabling human-in-the-loop approval

---

## CNCF Governance and Industry Adoption

- **Project status:** Incubating → Graduated (2023)
- **Governance:** Technical Steering Committee (TSC) with representatives from major vendors (Google, Splunk, Microsoft, Uber, etc.)
- **Vendor support:** 90+ observability platforms and 50+ instrumentation libraries
- **Standards compliance:** Aligns with W3C Trace Context and W3C Baggage specifications

---

## Key Takeaways

- **OpenTelemetry is the industry standard** for vendor-neutral, multi-signal observability (traces, metrics, logs)
- **OTLP is the wire protocol** — gRPC on port 4317, HTTP/Protobuf on 4318, backend-agnostic routing
- **Three signals:**
  - Traces (request flow) — NOT emitted by Claude Code
  - **Metrics** (quantitative, aggregated) — EMITTED by Claude Code (token, cache, latency, cost)
  - **Logs** (JSONL events) — EMITTED by Claude Code (session transcripts, events)
- **Collector architecture** (receivers → processors → exporters) runs in agent or gateway mode, enabling flexible deployment
- **Semantic conventions** standardize naming across platforms; adoption is voluntary but recommended
- **Real-time exploitation is fully feasible** at ~100–200ms latency with a custom dashboard + alerting stack
- **Claude Code's "command center" is a custom, metrics-and-logs-driven dashboard**, not a full tracing waterfall; the creator built it using OTel metrics + JSONL logs + Telegram HITL
- **Documentation advantage:** OTel has extensive docs and 90+ vendor integrations, making custom observability solutions buildable without vendor lock-in

---

## Related Articles

- [[overview]] — autopilot-research claude-code-observability topic overview
- [[claude-code-opentelemetry]] — Claude Code's OTEL emission configuration (Max/Pro plans)
- [[observability-backend-stack]] — deploying Grafana + Prometheus + Loki for OTel data
- [[cost-cache-token-metrics]] — token usage and cache hit rate as the #1 cost lever
- [[mcp-and-skill-cost-metrics]] — latency and error rate tracking for MCP tools and skills
- [[task-queue-scheduling-telegram-hitl]] — event-driven Telegram approval pattern for scheduled tasks
- [[jsonl-logs-and-native-dashboard]] — Claude Code JSONL session logs and in-GUI monitoring
- [[code-execution-mcp-workaround]] — alternative to MCP for reducing latency in skill execution

**Cross-topic:**
- [[../claude-api-cost-optimization/_index]] — cache hit rate = the #1 cost lever; token spend optimization
- [[../telegram-remote-control-stack/_index]] — the Telegram HITL approval stack (already piloted as Recipe A)
- [[../agentic-analytics-harness/_index]] — observability-over-scorecards at production scale (Omni/Blobby lesson)
- [[../prompt-evaluation/_index]] — trace-driven eval triage
- [[../harness-engineering/_index]] — observability as a harness property
- [[../claude-code-hooks/_index]] — hooks as the deterministic complement to telemetry
- [[../autonomous-loops-human-in-the-loop/_index]] — the HITL approval pattern
- [[../claude-skills/_index]] — skill cost metrics
