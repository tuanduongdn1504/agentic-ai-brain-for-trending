# Security & production-readiness gaps

## Source

Security-lens dive over all `repo-truth/` files + transcript; refute-first verified. Each gap tagged **STATED** (instructor acknowledged on camera) or **SILENT** (unmentioned). This is a knowledge-base catalog for a teaching course — text analysis only, no active probing.

## The framing that matters

The course makes a **defensible pedagogical bargain** on two fronts and says so out loud: HTTPS and automated tests are dropped "so as not to convolute the overall process," with an explicit "add HTTPS later, it's important." That honesty is real and worth crediting. The problem is the gap between what's *acknowledged* (the easy, obvious simplifications) and what's *silent* (a live production credential leak). A learner who trusts the on-camera candor will assume the un-flagged parts are safe. They are not.

## HIGH severity

| # | Gap | Tag | One-line fix |
|---|---|---|---|
| 1 | **Hardcoded MongoDB Atlas credential** `GavinL:Password1@...` committed in `MagicStreamMastery/docker-compose.yaml`, public 120+ days, never removed | **SILENT** | Rotate the Atlas password immediately; move URI to a secret/`.env`; purge from git history |
| 2 | **HTTP-only cookies with `Secure: false`** — original app used `Secure: true` for HTTPS; course rewrites login/logout to `Secure: false` so auth tokens transit **unencrypted** over the public internet | **STATED** (as a deliberate HTTPS-avoidance choice) | Restore HTTPS (TLS termination) and `Secure: true` before any real use |
| 3 | **SSH deploy as `root`** — `HOSTINGER_USER=root`; the Action runs deploy commands as root on the VPS | **STATED** (instructor sets it to root on camera, without flagging the risk) | Create a dedicated deploy user with a narrow `sudoers` entry for `docker compose` only |
| 4 | **Public HTTP port 8081** — React frontend exposed over plain HTTP, no TLS/reverse proxy | **SILENT** | Front with nginx/Caddy/Cloudflare doing TLS; redirect 80→443 |

## MEDIUM severity (all SILENT unless noted)

| # | Gap | One-line fix |
|---|---|---|
| 5 | **No healthchecks** on web/api in prod compose (only Mongo has one) — no auto-restart on a hung process | add `healthcheck:` + `restart` conditions |
| 6 | **No resource limits** (CPU/memory) — one container can starve a shared VPS | `deploy.resources.limits` |
| 7 | **Containers run as root** — no `USER` directive in either prod image | add a non-root `USER` |
| 8 | **Mutable `:latest` deploys, no rollback** — the `type=sha` tag is dead config ([[cicd-github-actions-pipeline]]) | push `outputs.tags` (adds a `sha-` tag); pin/rollback by digest |
| 9 | **`ssh-keyscan` without `-H`, TOFU every run** — accepts host key unverified; MITM-able in the runner network | pre-register a pinned host key fingerprint |
| 10 | **Secrets pasted via `nano` on the VPS** — no secret manager, no encryption at rest | use a secrets manager / restricted `.env` perms |
| 11 | **No automated tests in CI** | **STATED** (deliberately omitted) — add `npm test` + `go test` as fail-gates before build |
| 12 | **No image vulnerability scanning** (Trivy/Scout) | add a scan step post-build |
| 13 | **`git pull` on the VPS mixes gitops + imageops** — deploy pulls both code and images, two sources of truth | separate: images from registry, config via one channel |
| 14 | **No staging environment** despite the course mentioning staging | add a `develop→staging` workflow alongside `main→prod` |

## LOW severity (SILENT)

| # | Gap | Note |
|---|---|---|
| 15 | **Unpinned base images** (`alpine:latest`, `nginx:stable-alpine`) | pin by digest for reproducibility/supply-chain |
| 16 | **Sequential single-runner builds, no buildx cache** | slower CI; add `cache-from`/`cache-to` |
| 17 | **No audit logging** on deploys | — |
| 18 | **Unguarded `envsubst`** (no var allowlist) in the SPA env-injection | scope to named vars ([[vite-runtime-env-injection]]) |
| 19 | **No `env.js` cache-busting** — stale runtime config possible | `Cache-Control: no-cache` on `env.js` |
| 20 | **OpenAI API key entered on camera** | assume-revoked; never show real keys on screen |
| 21 | **Empty-passphrase SSH key** | acceptable for CI, but pair with key rotation + least-privilege user |

Tally: **4 HIGH / 10 MEDIUM / 7 LOW = 21**. Roughly **3 stated on camera** (HTTPS downgrade, root user, test omission) vs. **~18 silent**, headed by the committed credential.

## How to read this for the vault / hireui

- This is a **model teaching-integrity case**: honest about the cosmetic simplifications, silent on the dangerous one. When lifting *any* pattern from a tutorial, run exactly this stated-vs-silent audit — the on-camera candor is not a warranty for the rest.
- The **credential-in-compose** pattern is the exact anti-pattern to catch in review: secrets belong in a manager or an un-committed `.env`, never in a tracked compose/manifest. A committed-secret grep is a cheap CI gate ([[cicd-github-actions-pipeline]] is where it'd hook in).
- The HIGH-4 (secret, HTTP cookies, root deploy, plain-HTTP port) are the minimum patch list before *any* of this touches a real deployment.

## Key takeaways

- 21 gaps: 4 HIGH, 10 MEDIUM, 7 LOW.
- Stated: HTTPS, tests, root user. Silent (and worst): the live committed Atlas credential.
- The mechanics are teachable and correct; the security posture needs the HIGH-4 patched before production.
- Use the stated-vs-silent split as a reusable audit lens for any tutorial-sourced pattern.
