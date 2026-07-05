---
source: operator-submitted single video (path 5/6 hybrid — yt-dlp transcript + GitHub API ground truth)
topic: fullstack-docker-cicd
generated: 2026-07-05
video: https://www.youtube.com/watch?v=lEcULR30-GM
title: "Master Full-Stack Docker & CI/CD – Build a Production-Ready Pipeline"
channel: freeCodeCamp.org (11.7M subs)
instructor: Gavin Lon (GitHub GavinLonDigital; captions garble the name as "Gavin Lawn")
uploaded: 2026-02-12
duration: 3:58:43
views_at_ingest: 102,624 (2026-07-05)
likes_at_ingest: 3,239
sponsor: Hostinger grant (stated in description + intro)
transcript_chars: 240,505 (5,316 timestamped lines; read IN FULL in main loop)
original_resources:
  - https://github.com/GavinLonDigital/MagicStream (original app repo, 146★, NO docker files)
  - https://github.com/GavinLonDigital/MagicStreamDocker (Dec 2025)
  - https://github.com/GavinLonDigital/MagicStreamDeploy (Jan 2026)
  - https://github.com/GavinLonDigital/MagicStreamApp (Feb 2026 — built live in course)
  - https://github.com/GavinLonDigital/MagicStreamMastery (Feb 2026 — Docker Manager segment)
  - prerequisite course: https://www.youtube.com/watch?v=jBf7of9JTV8 (14:45:25, 2025-09-30, ~146K views)
verify_workflow: wf_da1a6823-d91 (9 dive + 14 refute-first verify agents)
---

# freeCodeCamp "Master Full-Stack Docker & CI/CD" (Gavin Lon) — raw digest

## What the course is

A ~4h deployment-only course: takes the existing MagicStream app (React 19 + Vite / Go + gin / MongoDB, OpenAI one-word review-sentiment feature; built in the separate 14h45m prerequisite course) from bare-metal dev to a containerized production deployment on a Hostinger VPS with a GitHub Actions CI/CD pipeline. Explicit separation-of-concerns pitch: "you don't need the coding course to follow the DevOps course."

## Structure — deliberately "back-to-front" [00:08:32]

Instructor states he inverted the usual order: **deploy the easy way FIRST** (Hostinger Docker Manager, 0:08–0:40), then spend 3h20m going "under the hood" building the same thing manually. Rationale: show what the managed tool abstracts away, then earn the understanding.

### Part 1 — Docker Manager path (0:08:29–0:40:25)
- Hostinger VPS panel → Docker Manager → **Compose from URL**: paste the *raw* GitHub URL of `docker-compose.yaml` from MagicStreamMastery → auto-creates project.
- Env vars set in visual editor: SECRET_KEY, REFRESH_TOKEN_SECRET_KEY, OPENAI_API_KEY, API_HOST_IP (VPS name or IP), ALLOWED_ORIGINS (CORS) → Deploy button.
- DB = MongoDB **Atlas** (URI hardcoded in the Mastery compose file — see red flags).
- CI/CD demo: edit Home component → `git add . && git commit && git push` → GitHub Action builds images + pushes to DockerHub → **operator clicks Deploy in Docker Manager** to pull + recreate containers. So this path is CI + *manual-button* CD.
- Stated deliberate omissions [00:33:06]: "I haven't included test automation or HTTPS for security in this deployment functionality deliberately so as not to convolute the overall process."
- Other compose options shown: Compose manually (visual editor), One-click deploy (predefined stacks: n8n, WordPress...).

### Part 2 — Under the hood (0:40:25–3:17:41)
1. **Local bare-metal baseline** (0:40–0:57): download repo ZIP (not git clone!), `npm install`, local MongoDB Community + Compass, create `magic-stream-app` DB, import 4 collections (movies/genres/rankings/users) from repo seed JSON, `.env` files client+server, `go run .`, `npm run dev`. Demo login bobjones@hotmail.com / Password1!
2. **Dockerfiles** (0:57–1:22): server `golang:1.24.2-alpine`, WORKDIR /app, copy go.mod/go.sum → `go mod download` (layer-cache explanation), EXPOSE 8080, CMD go run main.go. Client `node:20-alpine`, npm install, EXPOSE 5173, CMD npm run dev -- --host. `docker build -t magic-stream-api:1.0.0 .`; **live mistake preserved**: `docker run -d --p` → "unknown flag" → corrected to `-p` [01:09:37]. Port-mapping container-vs-host explained at length. Docker Desktop used as primary GUI for images/containers.
3. **docker-compose.yaml** (1:22–1:33): one command replaces two `docker run`s; network `magic-stream-app_default` auto-created; `.env` at compose root injected via `${VAR}`.
4. **Vite runtime-env fix** (1:33–1:45): problem framed as "env var baked into the image ... because we created the react application using vit" → fix = `public/env.template.js` + `envsubst` at container start → `env.js` → `<script src="/env.js">` → `window.__ENV?.API_URL` in axiosConfig.js + useAxiosPrivate hook (replaces `import.meta.env`). Dev image `apk add --no-cache gettext`.
5. **Containerized MongoDB** (1:45–2:00): `mongo:latest` service + named volume `movies:/data/db` + healthcheck (mongosh ping) + **one-shot seed container** (`mongosh mongodb://db:27017/... /seed-data/seed.js`, `restart: "no"`, `depends_on: condition: service_healthy`). DB name changes local `magic-stream-app` → containerized `magic-stream-movies`. Volumes = data survives container destruction, stored on host.
6. **Dev/prod split** (2:00–2:19): `Dockerfile.dev`/`Dockerfile.prod` ×2 (`-f` flag on build). Client prod = multi-stage `node:20-alpine AS build` → `npm ci` → `vite build` → `nginx:stable-alpine` + envsubst CMD, EXPOSE 80. Server prod = multi-stage `golang:1.24-alpine` → `go build -o api-golang` → `alpine:latest`, EXPOSE 8080. Compose split: base `docker-compose.yaml` + `docker-compose.dev.yaml` + `docker-compose.prod.yaml` overrides — explicitly analogized to **inheritance** [02:10:21].
7. **Compose Watch** (2:19–2:24): `docker compose -f docker-compose.yaml -f docker-compose.dev.yaml watch` — package.json/go.mod → `rebuild`, source tree → `sync`. Live demo: H2 heading edit hot-reloads in browser. Claim made that Go side hot-reloads the same way [02:16:13] (⚠️ see verify — sync alone cannot restart `go run`).
8. **DockerHub push** (2:24–2:39): username-prefixed tags `gavinlon/magic-stream-web-prod:1.0.0`, `docker push`; forgot-the-dot build error preserved on camera; PAT with read/write/delete + 30-day expiry created later for CI.
9. **HTTPS→HTTP cookie downgrade** (2:36–2:42): original code = Secure HTTP-only cookies for HTTPS; course replaces loginUser/logoutHandler with HTTP variants copied from MagicStreamDeploy "so as not to muddy the waters with certificate-related code" in the Action; explicit encouragement to add HTTPS later.
10. **New repo + version bump** (2:42–3:08): git init/add/commit/branch -M main/remote add/push to new `MagicStreamApp` repo; image versions bumped 1.0.0→1.0.1 in dev + prod compose (`IMAGE_TAG` env var in prod), rebuilt + repushed both prod images.
11. **Manual one-time VPS setup** (3:08–3:17): Hostinger browser terminal, Ubuntu 24.04, as **root**: `mkdir magic-stream-app && cd` → `git clone https://github.com/GavinLonDigital/magic-stream-app.git .` → `nano .env` (paste values, localhost→VPS name, port 8081) → `docker compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d` → app live on `http://<vps>:8081`. "Not secured. That's correct." [03:16:57]
12. **GitHub Action CI/CD** (3:17–3:58): `.github/workflows/deploy.yml` — on push main → checkout (fetch-depth 0) → DockerHub login → metadata-action (sha-short + latest tags) → build-push-action ×2 (Dockerfile.prod each) → webfactory/ssh-agent@v0.9.0 → ssh-keyscan into known_hosts → ssh: `export IMAGE_TAG=... && cd $APP_DIR && git pull origin main && docker compose -f docker-compose.yaml -f docker-compose.prod.yaml pull && up -d --remove-orphans`. **6 secrets**: DOCKERHUB_USERNAME, DOCKERHUB_TOKEN, HOSTINGER_APP_DIR, HOSTINGER_USER(=root), HOSTINGER_HOST(=IP), HOSTINGER_SSH_KEY. Keypair: `ssh-keygen -t ed25519 -C "github actions hostinger"`, empty passphrase; public key → `~/.ssh/authorized_keys`, `chmod 700 ~/.ssh`, `chmod 600 authorized_keys`. **IMAGE_TAG must be REMOVED from VPS .env** so `:latest` is pulled [03:45:40]. Instructor admits first workflow runs failed ("very fiddly... trial and error") [03:47:31]. Final demo: heading change → push → green tick → live on VPS.

## Repo-family ground truth (fetched 2026-07-05, before verify workflow)

- **MagicStream** (146★, JS, created 2025-06-24, pushed 2025-10-01): NO Docker/CI files — pure app code + seed data. Companion to the 14h45m build course.
- **MagicStreamDocker / MagicStreamDeploy / MagicStreamApp / MagicStreamMastery**: all share layout — `Client/magic-stream-client/Dockerfile.{dev,prod}`, `Server/MagicStreamServer/Dockerfile.{dev,prod}`, `docker-compose.{,dev.,prod.}yaml`, `.github/workflows/deploy.yml`.
- **All four deploy.yml differ** (4 distinct hashes). Docker→Deploy: image names gain `-prod` suffix. Deploy→App: whitespace only. **App→Mastery: entire SSH deploy stage REMOVED** (Mastery = build+push only; CD is the Docker Manager button).
- **⚠️ Committed secret**: Mastery `docker-compose.yaml` hardcodes `MONGODB_URI: mongodb+srv://GavinL:Password1@magic-stream-movies.7qnqryr.mongodb.net` (with db/seed services commented out). Never used the credential; text-presence only.
- Client package.json: react ^19.1.0, vite ^6.3.5, react-player ^2.16.0, react-router-dom ^7.6.2, axios ^1.9.0, bootstrap 5. Server go.mod: go 1.24.2, gin v1.10.1, langchaingo v0.1.13, golang-jwt v5.2.2, mongo-driver v2.2.2.
- Workflow oddity: metadata-action computes `type=sha,format=short` + `type=raw,value=latest`, but build-push-action tags with the single `steps.meta.outputs.version` — sha tag likely dead config (⚠️ verify C4).

## Quotable framings

- "Stop saying it works on my machine and start shipping professional-grade software to the cloud." [00:00:00]
- "It is going to make you way more marketable as a developer to have at least a basic DevOps knowledge." [00:07:01]
- "I'm certainly not advocating for going under the hood and creating all the details yourself unnecessarily whenever you want to do a deployment." [00:38:30]
- "In production, you don't really want to seed your data like this... just for demonstration purposes." [02:17:42]
- "If you make any tiny little mistake, it won't work... it's a bit of trial and error here." [03:47:57]

<!-- compiled: 2026-07-05 -->
