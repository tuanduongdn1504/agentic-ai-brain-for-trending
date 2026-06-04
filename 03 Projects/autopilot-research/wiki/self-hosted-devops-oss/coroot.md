# Coroot — zero-instrumentation eBPF observability & APM

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 5)
- Repo: https://github.com/coroot/coroot · Site: https://coroot.com · Docs: https://docs.coroot.com · Live demo: https://demo.coroot.com
- Metadata (GitHub API, 2026-06-04): **7,685★** · Go · Apache-2.0 · created 2022-08-22 · last push 2026-06-03 (very active)

## What it is
- Open-source **observability + APM** that combines metrics, logs, traces, continuous profiling, and SLO-based alerting with predefined dashboards/inspections — plus **AI-powered Root Cause Analysis**.
- Core selling point: **zero-instrumentation** via **eBPF** — no SDK, no code changes.

## Why it's on the list (operator framing)
- "Install and it auto-maps every service, dependency and bottleneck." Removes the instrumentation tax of traditional APM and the per-host bill of commercial observability.

## Key features
- **eBPF auto-collection** — metrics/logs/traces/profiles gathered automatically; **Service Map covers 100% of the system** with predefined inspections (no config). Can instrument legacy/third-party services with no code changes. OpenTelemetry-compatible.
- **App Health Summary** + **SLO tracking** + single consolidated alert per failing SLO.
- **Distributed tracing** (1-click anomaly investigation) + **log patterns** (ClickHouse-backed search).
- **1-click profiling** — CPU/memory down to the line of code.
- **Built-in expertise** — claims it can automatically identify 80%+ of issues.
- **Deployment Tracking** — discovers every K8s rollout, compares each release to the previous, no CI/CD integration needed.
- **Cost Monitoring** — per-application cloud cost (AWS/GCP/Azure) without cloud-account access.

## Install
- Run as a Docker container or deploy into any Kubernetes cluster — https://docs.coroot.com. Apache-2.0 OSS core; a **Coroot Enterprise** edition also exists.

## Key Takeaways
- The strongest **standalone OSS** observability pick of the 8 — full APM (metrics+logs+traces+profiles+RCA), actively developed, permissive license.
- Directly comparable to (and more complete than) [[groundcover-caretta]]: both are eBPF/K8s observability, but Coroot is a maintained full product where Caretta is a stale service-map building-block.
- eBPF approach = the real differentiator vs the [[dockprom]] exporter-stack: no instrumentation/agents-per-app, at the cost of a Linux-kernel/eBPF dependency.
- "Free" caveat: OSS core is free; advanced features may sit in Coroot Enterprise — check the edition boundary. See [[cost-displacement-thesis]].
