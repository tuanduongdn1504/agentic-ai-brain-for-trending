# Dockprom — one-command Prometheus + Grafana monitoring stack

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 8)
- Repo: https://github.com/stefanprodan/dockprom
- Metadata (GitHub API, 2026-06-04): **6,528★** · config/compose (`language: null`) · MIT · created 2016-09-25 · last push 2026-03-06 (oldest repo of the 8; periodically maintained)

## What it is
- **Not a product** — a curated **docker-compose stack** that wires together the standard Docker monitoring toolchain so you don't assemble it by hand:
  - **Prometheus** (metrics DB, :9090) + **Pushgateway** (:9091)
  - **Grafana** (dashboards, :3000) — pre-provisioned with Docker Host / Containers / Monitor Services dashboards
  - **cAdvisor** (container metrics) + **NodeExporter** (host metrics)
  - **AlertManager** (:9093) + **Caddy** (reverse proxy + basic auth)

## What it replaces (operator framing)
- The "weeks of work" teams spend standing up a Prometheus/Grafana monitoring stack from scratch — reduced to one `docker-compose up`.

## Install
```bash
git clone https://github.com/stefanprodan/dockprom && cd dockprom
ADMIN_USER='admin' ADMIN_PASSWORD='admin' \
ADMIN_PASSWORD_HASH='$2a$14$...' docker-compose up -d
# Caddy v2 requires a bcrypt HASH, not plaintext:
# docker run --rm caddy caddy hash-password --plaintext 'yourpassword'
```
- Ships 3 prebuilt alert groups: monitoring-targets, Docker host (CPU/mem/storage load), and per-container (down / high-CPU / high-mem). AlertManager → email/Slack/Pushover/webhook.

## Key Takeaways
- Pure **convenience/glue** value: every component is already free and open-source; Dockprom's contribution is the *assembled, pre-dashboarded configuration*. The cost it kills is **integration time**, not a license.
- Best fit: a single Docker host / small fleet where you want classic exporter-based metrics fast. For Kubernetes-scale or zero-instrumentation, the eBPF tools ([[coroot]], [[groundcover-caretta]]) fit better.
- Exporter/pull model = no kernel/eBPF dependency, but you do add per-target exporters (vs eBPF auto-discovery).
- Complements [[dozzle]] (logs) and monitors [[coolify]]-run hosts/containers. See [[cost-displacement-thesis]].
