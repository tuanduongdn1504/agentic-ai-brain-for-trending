# The GitHub Actions CI/CD pipeline

## Source

Transcript [03:17:41]–[03:58:00]; ground-truth `.github/workflows/deploy.yml` from the four docker repos; `docker/metadata-action` + `docker/build-push-action` + `webfactory/ssh-agent` docs; DockerHub public tags API.

## What the pipeline does (the SSH-deploy variant)

On push to `main`, the Action (`deploy.yml` in `MagicStreamDocker`/`Deploy`/`App`):

1. **Checkout** (`actions/checkout@v4`, `fetch-depth: 0`).
2. **Login to DockerHub** (`docker/login-action@v3`, username+token from secrets).
3. **Compute metadata** (`docker/metadata-action@v5`) for both images, tags `type=sha,format=short` + `type=raw,value=latest`.
4. **Build & push** API and web images (`docker/build-push-action@v6`, each with its `Dockerfile.prod`), tagged `${{ steps.meta.outputs.version }}`.
5. **Start ssh-agent** (`webfactory/ssh-agent@v0.9.0`) with the VPS private key.
6. **`ssh-keyscan`** the VPS host into `known_hosts`.
7. **Deploy over SSH**: `export IMAGE_TAG=... && cd $APP_DIR && git pull origin main && docker compose -f docker-compose.yaml -f docker-compose.prod.yaml pull && ... up -d --remove-orphans`.

Step 7 is what makes this true hands-off CD; `--remove-orphans` gives the rolling replace ("seamless to the user").

## The 6 secrets (verified CONFIRMED)

Exactly six repo secrets, referenced in the workflow and created on camera:

| Secret | Value | Purpose |
|---|---|---|
| `DOCKERHUB_USERNAME` | `gavinlon` | registry login |
| `DOCKERHUB_TOKEN` | PAT (read/write/delete, 30-day expiry) | registry login |
| `HOSTINGER_SSH_KEY` | ed25519 **private** key | Action → VPS auth |
| `HOSTINGER_HOST` | VPS IP | SSH target |
| `HOSTINGER_USER` | `root` | SSH user |
| `HOSTINGER_APP_DIR` | `magic-stream-app` | `cd` target on VPS |

Key generation taught: `ssh-keygen -t ed25519 -C "github-actions-hostinger"` with **empty passphrase**; **public** key appended to the VPS's `~/.ssh/authorized_keys`; `chmod 700 ~/.ssh` and `chmod 600 authorized_keys`. Standard mechanics — but note the deploy user is **root** (see [[security-and-production-gaps]]).

## ⚠️ CORRECTION — the `type=sha` tag is dead config (verified CONFIRMED, empirically)

The workflow computes a short-SHA tag *and* a `latest` tag in `metadata-action`, but `build-push-action` consumes only `${{ steps.meta.outputs.version }}` — **not** `outputs.tags`. Per the official `metadata-action` README, `outputs.version` is the **single highest-priority** tag, and `type=raw` (default priority 200) beats `type=sha` (priority 100). So:

- `outputs.version` always resolves to **`latest`**.
- The short-SHA tag is **computed but never applied** to any pushed image — dead configuration.
- **Empirical confirmation:** DockerHub's public API for `gavinlon/magic-stream-api-prod` shows only three tags — `latest`, `1.0.1`, `1.0.0` (the last two hand-pushed earlier in the course) — and **zero `sha-*` tags**.

**Consequences:** every CI deploy overwrites the mutable `:latest`; there is no immutable, per-commit image tag, so **no clean rollback** to a specific commit from the registry. The likely intended fix is `tags: ${{ steps.meta.outputs.tags }}` (push *all* computed tags), which would give both `latest` and a rollback-able `sha-<short>`.

## The manual one-time VPS setup that precedes automation [03:08:18]

Before the Action can deploy, a human does a one-time bootstrap over the Hostinger browser terminal (as root): `mkdir magic-stream-app && cd`, `git clone`, `nano .env` (paste secrets, replace `localhost` with the VPS name, set port 8081), then `docker compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d`. A critical gotcha stated at [03:45:40]: **remove `IMAGE_TAG` from the VPS `.env`** so the compose `${IMAGE_TAG:-latest}` default pulls `:latest` (which is what the Action pushes).

## The honesty note the course earns

At [03:47:31] the instructor shows that his own first several workflow runs **failed**: *"some of them didn't work... I had some of the settings slightly incorrect... it is very fiddly and it's very easy to make little mistakes... if you make any tiny little mistake, it won't work."* This is accurate and useful — YAML+secrets+SSH pipelines are exactly this brittle — and it's a rare bit of on-camera failure-transparency.

## Key takeaways

- The SSH-deploy Action is a clean, real hands-off-CD pattern: build+push → ssh-agent → keyscan → `git pull` + `compose pull` + `up -d --remove-orphans`.
- **The `type=sha` tag never fires** — deploys are mutable `:latest` with no rollback pin; fix by using `outputs.tags`, not `outputs.version`.
- 6 secrets, ed25519 keypair, root deploy user (harden this — see [[security-and-production-gaps]]).
- A manual VPS bootstrap precedes automation, and `IMAGE_TAG` must be *removed* from the VPS `.env` for `:latest` to win.
