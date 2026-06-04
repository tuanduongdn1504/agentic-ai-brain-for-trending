# Infisical — open-source secrets & PKI platform

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 1)
- Repo: https://github.com/Infisical/infisical · Site: https://infisical.com · Docs: https://infisical.com/docs
- Metadata (GitHub API, 2026-06-04): **27,195★** · TypeScript · created 2022-08-05 · last push 2026-06-04 (very active)

## What it is
- Open-source platform for **secrets management, certificates/PKI, and privileged access management**.
- Centralizes app config + secrets (API keys, DB credentials) so they're not scattered in `.env` files or leaked into git.
- Operator framing: a free self-hostable replacement for **HashiCorp Vault Enterprise** (claimed ~$22k/yr/cluster — *vendor figure, unverified*).

## Key features
- **Dashboard** — secrets across projects + environments (dev/staging/prod).
- **Secret Syncs** — push to GitHub Actions, Vercel, AWS Secret Manager; integrate Terraform, Ansible.
- **Versioning + Point-in-Time Recovery** — roll back secret/project state.
- **Secret Rotation** — auto-rotate Postgres/MySQL/AWS-IAM creds on a schedule.
- **Dynamic Secrets** — generate ephemeral on-demand creds (Postgres/MySQL/RabbitMQ).
- **Secret Scanning / leak prevention** — `infisical scan` (140+ secret types) + pre-commit hook.
- **Kubernetes Operator** + **Infisical Agent** (inject secrets without code changes).
- **PKI** — internal + external CA (Let's Encrypt/DigiCert/MS AD CS), cert lifecycle (ACME/EST), revocation/CRL.
- **KMS**, **SSH signed certs**, machine-identity auth (K8s/GCP/Azure/AWS/OIDC/Universal), **RBAC + approval workflows**, audit logs.
- SDKs: Node/Python/Go/Ruby/Java/.NET + CLI + REST API.

## Install (self-host, ~10 min per operator brief)
```bash
git clone https://github.com/Infisical/infisical && cd "$(basename $_ .git)" \
  && cp .env.example .env && docker compose -f docker-compose.prod.yml up
# → create account at http://localhost:80
```

## Licensing nuance (verify before enterprise use)
- Core repo is **MIT**, **except the `ee/` directory** = premium enterprise features requiring an Infisical license.
- GitHub API reports the license as `NOASSERTION`/"Other" precisely because of this mix — so "fully free" is true for the OSS core, not for the `ee/` enterprise features.

## Key Takeaways
- Strongest "replace a paid enterprise tool" case of the 8 — Vault Enterprise is genuinely expensive and Infisical's OSS core is broad (secrets + PKI + KMS + access control).
- The displacement is the **license fee**, not total cost: you still run + secure the Postgres-backed deployment yourself.
- Mixed licensing (`ee/`) means "open-source" ≠ "all features free" — read the `ee/` boundary before depending on a feature.
- Mature + very active (27k★, daily pushes) → low adoption risk.
- Related: [[cost-displacement-thesis]] · secrets feed into pipelines built by [[buildah]] and deployed by [[coolify]]/[[ctrlplane]].
