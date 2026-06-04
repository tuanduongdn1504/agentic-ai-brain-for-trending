<!-- compiled: 2026-06-04 -->
# Raw — Self-hosted DevOps OSS (8 repos) — operator-curated brief

> **Ingested:** 2026-06-04 13:29 (+07)
> **Path:** 3-webfetch / GitHub-API direct fetch (NOT yt-pipeline — no `.venv`/notebooklm in this worktree; GitHub repos are best served by direct API + README fetch anyway)
> **Trigger:** `/loop autopilot research <operator brief>` (manual session-bound burst)
> **Fetch method:** `curl https://api.github.com/repos/<owner>/<repo>` (metadata) + `.../readme` with `Accept: application/vnd.github.raw` (README content). All numbers below are from the live GitHub API on 2026-06-04. Pricing/cost figures are from the OPERATOR BRIEF (a Vietnamese DevOps roundup) and are NOT independently verified in this compile.
> **Constitutional note (#4 never fabricate):** repo metadata = verified via API. Vendor pricing comparisons = operator-supplied claims, flagged as unverified. Groundcover "free community" = product-tier claim distinct from the Caretta OSS repo.

---

## Operator brief (verbatim, translated context)

Framing: "8 DevOps GitHub repos almost banned from existing — because they silently cost enterprise software billions in revenue. SAVE THIS."

1. **Infisical** — Open-source secrets manager. Replaces HashiCorp Vault Enterprise (claimed ~$22,000/year per cluster). Self-hosted Infisical is free; ~10 min to install.
2. **Coolify** — Self-host Heroku & Netlify. Heroku charges $25/dyno/month; Netlify $19/user/month. Coolify runs unlimited apps on your own server at $0.
3. **Buildah** — Build production Docker images without the Docker daemon and without root. For rootless CI/CD containers. Many pipelines should use it but don't.
4. **Ctrlplane** — Deploy software across Kubernetes, cloud functions and VMs from one platform. Replaces hand-built manual deploy scripts. Free & open-source.
5. **Coroot** — Full-stack eBPF observability, no code changes. No SDK, no instrumentation — install and it auto-maps every service, dependency and bottleneck.
6. **Dozzle** — Web-based real-time Docker log viewer. No Elasticsearch, no Kibana, no heavy logging cost. Just live, centralized logs.
7. **Groundcover** — eBPF Kubernetes monitoring; auto-detects services in-cluster without instrumentation. Datadog charges ~$23/host. Groundcover community edition is free.
8. **Dockprom** — Complete Prometheus + Grafana stack for Docker via one `docker-compose` command. Teams normally spend weeks building this; the repo does it in ~60s.

---

## Verified GitHub metadata (live API, 2026-06-04)

| # | Tool | Repo (full_name) | Stars | Lang | License (SPDX) | Homepage | Created | Last push | Maturity flag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Infisical | `Infisical/infisical` | 27,195 | TypeScript | MIT (core) — API reports `NOASSERTION`/"Other" due to commercial `ee/` dir | infisical.com | 2022-08-05 | 2026-06-04 | mature, very active |
| 2 | Coolify | `coollabsio/coolify` | 56,420 | PHP (Laravel) | Apache-2.0 | coolify.io | 2021-01-25 | 2026-06-03 | mature, very active (default branch `v4.x`) |
| 3 | Buildah | `podman-container-tools/buildah` (was `containers/buildah` — 301 redirect) | 8,824 | Go | Apache-2.0 | buildah.io | 2017-01-26 | 2026-06-02 | mature (CNCF/Podman family), active |
| 4 | Ctrlplane | `ctrlplanedev/ctrlplane` | 146 | TypeScript | **AGPL-3.0** | ctrlplane.dev | 2024-08-16 | 2026-06-03 | **EARLY-STAGE** (146★, created 2024) — flag |
| 5 | Coroot | `coroot/coroot` | 7,685 | Go | Apache-2.0 | coroot.com | 2022-08-22 | 2026-06-03 | mature, very active |
| 6 | Dozzle | `amir20/dozzle` | 13,169 | Go | MIT | dozzle.dev | 2018-10-30 | 2026-06-03 | mature, very active |
| 7 | Caretta (by groundcover) | `groundcover-com/caretta` | 2,018 | Go | Apache-2.0 | (groundcover.com) | 2022-11-21 | **2025-03-17** | **STALE ~15 months** — flag; one OSS component, NOT the full Groundcover product |
| 8 | Dockprom | `stefanprodan/dockprom` | 6,528 | (compose/config — `language: null`) | MIT | — | 2016-09-25 | 2026-03-06 | mature config-stack, periodically updated |

---

## Per-tool extracted facts (faithful README extracts)

### 1. Infisical — `Infisical/infisical`
- **What:** open-source platform for **secrets, certificates, and privileged access management** ("the open-source secret management platform"). Centralizes API keys, DB credentials, configs; internal PKI.
- **Replaces (operator claim):** HashiCorp Vault Enterprise (~$22k/yr/cluster, unverified).
- **Features (verbatim from README):** Dashboard (secrets across projects/envs); Secret Syncs (GitHub/Vercel/AWS/Terraform/Ansible); Secret versioning + Point-in-Time Recovery; Secret Rotation (Postgres/MySQL/AWS IAM); Dynamic Secrets (ephemeral on-demand); Secret Scanning & leak prevention (`infisical scan`, pre-commit hook, 140+ secret types); Kubernetes Operator; Infisical Agent (inject secrets without code changes); Internal + External CA (Let's Encrypt/DigiCert/MS AD CS); Certificate Lifecycle Mgmt (ACME/EST); KMS; SSH signed certs; machine-identity auth (K8s/GCP/Azure/AWS/OIDC/Universal); RBAC + approval workflows; audit logs; SDKs (Node/Python/Go/Ruby/Java/.NET); CLI; API.
- **Install (verbatim):** `git clone https://github.com/Infisical/infisical && cd "$(basename $_ .git)" && cp .env.example .env && docker compose -f docker-compose.prod.yml up` → account at http://localhost:80
- **OSS vs paid:** repo is MIT EXCEPT `ee/` directory (premium enterprise features need an Infisical license). Managed Infisical Cloud + self-hosted Enterprise offering exist.

### 2. Coolify — `coollabsio/coolify`
- **What:** open-source & self-hostable **PaaS** alternative to Heroku / Netlify / Vercel. Manages servers, apps, databases on your own hardware via SSH (VPS, bare metal, Raspberry Pi). API desc: "deploy static sites, databases, full-stack applications and 280+ one-click services."
- **Replaces (operator claim):** Heroku ($25/dyno/mo), Netlify ($19/user/mo), Vercel (unverified).
- **Key positioning (verbatim):** "No vendor lock-in… all configurations are saved to your server. If you stop using Coolify you can still manage your running resources (you lose the automations and magic)."
- **Install (verbatim):** `curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash`
- **Cost note (verbatim from README):** recommended setup = one server for Coolify + one+ for resources; "A server is around 4-5$/month." Paid Cloud version exists (HA + email notifications + support + less maintenance). So self-host cost ≠ $0 — it's the VPS cost (~$4-5/mo), with no Coolify license fee.

### 3. Buildah — `podman-container-tools/buildah`
- **What:** CLI to build **OCI / docker-format container images**. Part of the Podman/containers family. Creates working containers from scratch or a base image; builds via Containerfile/Dockerfile OR without one; mount/unmount rootfs; commit to image.
- **Key differentiator (verbatim):** "building images with and without Dockerfiles while **not requiring any root privileges**." "follows a simple fork-exec model and **does not run as a daemon**." Lower-level coreutils-style interface; golang API can be vendored into other tools.
- **Buildah vs Podman:** Buildah specializes in BUILDING images (`buildah run` ≈ Dockerfile RUN); Podman manages/runs containers (`podman run` ≈ `docker run`). Podman uses Buildah's Go API for Dockerfile builds.
- **Use case (operator framing):** rootless, daemonless image builds for CI/CD — pipelines "should use but don't."

### 4. Ctrlplane — `ctrlplanedev/ctrlplane`
- **What:** "the **orchestration layer between your CI/CD pipelines and your infrastructure**." Decides WHEN releases are ready, WHERE to deploy, WHAT gates to pass — env promotion, verification, approvals, rollbacks. (API desc: "deployment orchestration tool that simplifies multi-cloud, multi-region, and multi-service deployments.")
- **Replaces (operator claim):** hand-built manual deploy scripts teams maintain for years.
- **Features (verbatim):** Gradual Rollouts (sequential targets + verification between each); Policy Gates (approvals, env sequencing, deploy windows); Automated Verification (Datadog/Prometheus/HTTP); Auto-Rollback; Infrastructure Inventory (K8s + cloud + custom); Pluggable Execution (ArgoCD, K8s Jobs, GitHub Actions, Terraform Cloud, custom agents).
- **For:** platform teams, DevOps/SRE at scale, orgs with 10+ services across envs, multi-region.
- **Install:** Docker or Kubernetes (docs.ctrlplane.dev/installation). Dev: `docker compose -f docker-compose.dev.yaml up -d; pnpm i && pnpm build; pnpm dev` → localhost:5173.
- **⚠️ Maturity + license:** 146★, created 2024-08, **AGPL-3.0** (network-copyleft — meaningful for SaaS use). Youngest + least-proven of the 8.

### 5. Coroot — `coroot/coroot`
- **What:** open-source **observability & APM with AI-powered Root Cause Analysis**. Combines metrics, logs, traces, continuous profiling, SLO-based alerting + predefined dashboards/inspections.
- **Replaces (operator framing):** instrumentation-heavy APM / commercial observability.
- **Zero-instrumentation (verbatim):** "Metrics, logs, traces, and profiles are gathered automatically by using **eBPF**." Service Map "covers 100% of your system with no blind spots." Predefined inspections audit each app with no config. eBPF instrumentation captures requests on legacy/third-party services with no code changes. OpenTelemetry-compatible.
- **Other features:** App Health Summary; SLO tracking; distributed tracing 1-click; log patterns (ClickHouse-backed search); 1-click CPU/mem profiling; built-in expertise ("automatically identify over 80% of issues"); Deployment Tracking (no CI/CD integration needed; compares each release); **Cost Monitoring** (per-app cloud cost, AWS/GCP/Azure, no cloud-account access needed).
- **Install:** Docker container OR any Kubernetes cluster (docs.coroot.com). Apache-2.0. Live demo at demo.coroot.com. Coroot Enterprise exists.

### 6. Dozzle — `amir20/dozzle`
- **What:** lightweight **web-based real-time log viewer for containers** (Docker, Swarm, K8s). "It doesn't store any log files — designed purely for live log viewing." ~7 MB compressed image.
- **Replaces (operator claim):** Elasticsearch + Kibana / heavy logging stacks (for the live-tail use case).
- **Features (verbatim):** fuzzy container-name search; regex log search; SQL-query log search; small memory footprint; split-screen multi-log; live CPU/mem stats; multi-user auth + forward-proxy auth; Swarm mode; Agent mode (multiple Docker hosts); dark mode. Works with Colima + Podman. Needs Docker Engine 19.03+ (API 1.40+).
- **Honest scope limit (verbatim):** "doesn't support offline searching. Products like Loggly, Papertrail, or Kibana are better suited for full search capabilities." → Dozzle is live-tail, NOT log retention/search.
- **Install (verbatim):** `docker run --name dozzle -d --volume=/var/run/docker.sock:/var/run/docker.sock -v dozzle_data:/data -p 8080:8080 amir20/dozzle:latest` → localhost:8080. (Collects anonymous Google Analytics unless `--no-analytics`.)

### 7. Caretta (by groundcover) — `groundcover-com/caretta`
- **IMPORTANT distinction:** the operator brief item is **Groundcover** (the commercial eBPF observability SaaS, Datadog competitor, with a free Community tier). The **open-source repo** is **Caretta** — groundcover's standalone OSS eBPF tool. They are NOT the same artifact.
- **What Caretta is (verbatim):** "a lightweight, standalone tool that instantly creates a visual **network map of the services running in your cluster**." Uses eBPF to map all service network interactions in K8s + Grafana to visualize. Minimal footprint, no cluster modifications. "demonstrates the power of using eBPF for observability solutions, which is our vision at groundcover."
- **Install (verbatim):** Helm — `helm repo add groundcover https://helm.groundcover.com/` → `helm install caretta --namespace caretta --create-namespace groundcover/caretta`. Ships Victoria Metrics + Grafana (both disableable). Main metric `caretta_links_observed` (Prometheus-compatible).
- **Requirements:** Linux kernel ≥ 4.16 + CO-RE support (Docker for Mac not supported).
- **⚠️ Staleness:** last push **2025-03-17** (~15 months before this ingest). Caretta is a demo/building-block, not actively-developed full monitoring. Groundcover's full product (the "free community" claim) is the commercial platform, not this repo.

### 8. Dockprom — `stefanprodan/dockprom`
- **What:** NOT a product — a curated **docker-compose monitoring stack** wiring **Prometheus + Grafana + cAdvisor + NodeExporter + AlertManager + Caddy** (reverse-proxy/basic-auth) for Docker host + container monitoring.
- **Replaces (operator framing):** the weeks of work teams spend assembling a Prometheus/Grafana stack from scratch ("~60s" via one compose up).
- **Install (verbatim):** `git clone https://github.com/stefanprodan/dockprom && cd dockprom` → `ADMIN_USER='admin' ADMIN_PASSWORD='admin' ADMIN_PASSWORD_HASH='...' docker-compose up -d`. (Caddy v2 needs a bcrypt password HASH.)
- **Ships:** Prometheus :9090, Pushgateway :9091, AlertManager :9093, Grafana :3000 (pre-provisioned Docker Host + Containers + Monitor Services dashboards), NodeExporter, cAdvisor, Caddy. 3 prebuilt alert groups (monitoring-targets / host / containers).
- **Maturity:** oldest repo (created 2016), 6,528★, MIT, periodically maintained (last push 2026-03-06).

---

## Cross-tool observations (for synthesis article)

- **Two eBPF observability entrants** — Coroot (7.7k★, Apache-2.0, ACTIVE, full APM) and Caretta (2k★, Apache-2.0, STALE, service-map-only). Coroot is the stronger standalone OSS pick; Caretta is a groundcover building-block.
- **Two Prometheus/Grafana paths** — Dockprom (compose-stack-you-run) vs Coroot/Caretta (eBPF auto-instrument). Dozzle is orthogonal (live logs, not metrics).
- **License spread:** 5× permissive (MIT/Apache), 1× AGPL-3.0 (Ctrlplane — copyleft, flag for SaaS), 1× mixed (Infisical MIT + commercial `ee/`).
- **Maturity spread:** Coolify (56k★) and Infisical (27k★) are heavyweight; Ctrlplane (146★) is early-stage; Caretta is stale.
- **"Free" nuance:** none are truly $0 to operate — they remove the *license/SaaS fee* but you pay for the server (Coolify README: ~$4-5/mo VPS) + your own ops time. The displacement is license-cost, not total-cost-of-ownership.
- **Pricing claims unverified:** $22k/yr Vault, $25/dyno Heroku, $19/user Netlify, $23/host Datadog are operator-brief figures; vendor pricing changes — verify before citing.
