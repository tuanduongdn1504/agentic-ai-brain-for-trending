# Groundcover / Caretta — eBPF K8s service map (OSS) vs the commercial platform

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 7)
- OSS repo: https://github.com/groundcover-com/caretta · Vendor: https://groundcover.com
- Metadata (GitHub API, 2026-06-04): **2,018★** · Go · Apache-2.0 · created 2022-11-21 · **last push 2025-03-17 (~15 months stale at ingest)**

## ⚠️ Read this first — two different things
The operator brief says "**Groundcover** — eBPF K8s monitoring … community edition free (Datadog alternative)." That conflates two artifacts:
- **Groundcover** = a **commercial** eBPF observability **SaaS/platform** (a Datadog competitor) that offers a free Community/Cloud tier. It is *not* a single open-source repo.
- **Caretta** = groundcover's **open-source** standalone eBPF tool (the actual GitHub repo) — it builds an instant **service dependency map**, not the full monitoring product.

So the free, open-source thing you can `helm install` today is **Caretta**; the "free community monitoring" claim refers to **Groundcover's product tier**, which is a separate commercial offering with its own terms.

## What Caretta is
- Lightweight, standalone tool that instantly draws a **visual network/service map** of a Kubernetes cluster.
- Uses **eBPF** to map all service network interactions + **Grafana** to visualize; minimal footprint, no cluster modifications.
- Self-described as a demonstration of "the power of using eBPF for observability… our vision at groundcover."

## Install (Helm)
```bash
helm repo add groundcover https://helm.groundcover.com/ && helm repo update
helm install caretta --namespace caretta --create-namespace groundcover/caretta
```
- Ships Victoria Metrics + Grafana (both disableable). Main metric `caretta_links_observed` (Prometheus-compatible).
- **Requirements:** Linux kernel ≥ 4.16 + CO-RE support (Docker for Mac not supported).

## What it replaces (operator claim — unverified)
- Datadog (~$23/host). True for the **Groundcover product**; Caretta alone only replaces the *service-map* slice, not full APM/monitoring.

## Key Takeaways
- **Maturity warning:** Caretta's last commit was ~15 months before this ingest — treat it as a stable demo / building-block, not actively-developed monitoring.
- If you want a *maintained, full, open-source* eBPF observability tool, **[[coroot]]** is the better pick (active, broader, Apache-2.0). Caretta is narrower (service map) and stale.
- The "Groundcover free community" pitch points you toward the **vendor's commercial platform**, not this repo — evaluate that separately and don't assume "open-source" applies to it.
- Honest comparison and the displacement caveat live in [[cost-displacement-thesis]].
