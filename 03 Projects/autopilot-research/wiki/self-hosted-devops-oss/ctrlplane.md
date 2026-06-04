# Ctrlplane — deployment orchestration layer

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 4)
- Repo: https://github.com/ctrlplanedev/ctrlplane · Site: https://ctrlplane.dev · Docs: https://docs.ctrlplane.dev
- Metadata (GitHub API, 2026-06-04): **146★** · TypeScript · **AGPL-3.0** · created 2024-08-16 · last push 2026-06-03

## What it is
- The **orchestration layer between CI/CD pipelines and infrastructure**: `Your CI (builds) → Ctrlplane (orchestrates) → Your Infra (deploys)`.
- Decides *when* a release is ready, *where* it deploys, and *what gates* it must pass — handling env promotion, verification, approvals, and rollbacks.
- Targets multi-cloud, multi-region, multi-service deployments from one definition.

## What it replaces (operator framing)
- The pile of bespoke, hand-maintained deploy scripts/glue that DevOps teams build over years.

## Key features
- **Gradual rollouts** — deploy to targets sequentially with verification between each.
- **Policy gates** — approvals, environment sequencing, deployment windows.
- **Automated verification** — Datadog / Prometheus / any HTTP check; pass → promote, fail → **auto-rollback**.
- **Infrastructure inventory** — unified view of what version runs on which cluster/region.
- **Pluggable execution** — ArgoCD, Kubernetes Jobs, GitHub Actions, Terraform Cloud, or custom agents (Ctrlplane decides; your existing tools execute).

## Install
- Docker or Kubernetes — see https://docs.ctrlplane.dev/installation (quickstart claims first service in ~15 min).

## ⚠️ Maturity & license flags (read before adopting)
- **Early-stage:** 146★, repo created 2024-08 — by far the youngest and least battle-tested of the 8. Treat as "promising / evaluate," not "proven."
- **AGPL-3.0:** strong network-copyleft. If you modify Ctrlplane and offer it as a network service, AGPL obligations attach. Fine for internal use; review with legal before building a product on top.

## Key Takeaways
- Fills a real gap (deploy *orchestration/policy*, distinct from CI like GitHub Actions and from appliers like ArgoCD) — it coordinates them rather than replacing them.
- Best fit: orgs with 10+ services across many envs/regions that already feel the pain of manual promotion + verification.
- The two caveats (immaturity + AGPL) make it the highest-risk pick of the 8 despite the appealing pitch — pilot, don't bet production on it yet.
- Consumes images from [[buildah]], pulls secrets from [[infisical]], verifies via metrics from [[coroot]]/[[dockprom]]; overlaps conceptually with [[coolify]] (which bundles deploy + host mgmt for simpler setups). See [[cost-displacement-thesis]].
