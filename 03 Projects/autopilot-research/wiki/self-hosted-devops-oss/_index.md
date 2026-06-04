# self-hosted-devops-oss

> Operator-curated roundup (2026-06-04) of **8 open-source, self-hostable DevOps tools** framed as replacements for expensive commercial SaaS/enterprise software. Ingested via direct GitHub API + README fetch (path 3-webfetch) — no YouTube/NotebookLM. All repo metadata verified against the live GitHub API on 2026-06-04; all **pricing/cost claims are operator-brief figures, NOT independently verified**.

**Theme:** "kill the enterprise bill by self-hosting." The honest synthesis ([[cost-displacement-thesis]]) stresses that *free = no license fee, not zero cost*, and flags two adoption-risk tools.

## Articles

| Article | Category | What it displaces | Note |
|---|---|---|---|
| [[infisical]] | Secrets / PKI | HashiCorp Vault Enterprise | MIT core + commercial `ee/`; 27k★ |
| [[coolify]] | PaaS / deploy | Heroku / Netlify / Vercel | Apache-2.0; 56k★ (most popular) |
| [[buildah]] | Container build | Docker daemon + root (risk, not a bill) | Apache-2.0; Podman family |
| [[ctrlplane]] | Deploy orchestration | bespoke deploy scripts | ⚠️ AGPL-3.0 + early-stage (146★) |
| [[coroot]] | Observability / APM (eBPF) | Datadog / instrumented APM | Apache-2.0; 7.7k★ — best OSS pick |
| [[dozzle]] | Live container logs | Kibana / Loggly / Papertrail | MIT; live-tail only (not retention) |
| [[groundcover-caretta]] | eBPF K8s service map | Datadog (the *product*, not this repo) | ⚠️ ~15mo stale; map ≠ full APM |
| [[dockprom]] | Metrics stack (glue) | weeks of Prometheus/Grafana setup | MIT; one `docker-compose up` |
| [[cost-displacement-thesis]] | **Synthesis** | — | mapping table + 6 honest caveats |

## How they compose
Build ([[buildah]]) → secrets ([[infisical]]) → deploy ([[coolify]] or [[ctrlplane]]) → observe ([[coroot]] / [[dockprom]] + [[dozzle]]).

## Status / gaps
- **Compiled:** 2026-06-04, 1 cycle, cold-start (8 tool articles + 1 synthesis + this index).
- **Open gaps / next ingests:**
  - Pricing claims unverified — a follow-up could fetch each vendor's current pricing page (watch for bot-protection → use [[external|bypass-403-escalation]] discipline).
  - Coroot vs Groundcover-product vs Caretta — a deeper eBPF-observability comparison could be its own article.
  - No hands-on pilot yet — Dozzle (lowest friction) or Coolify (highest savings) would be the natural first pilot; Ctrlplane/Caretta need a risk decision first.
- **Cross-topic:** this topic is orthogonal to the vault's existing Claude/agent topics; loosely related to the [[external|Storm Bear]] cost-discipline thread (self-host trades SaaS fee for ops labor).
