# The originals — the 5-repo MagicStream family

## Source

GitHub API commit/tree forensics on all five repos (verified 2026-07-05); raw file fetches at HEAD; prerequisite course `jBf7of9JTV8`.

## The family

All under `github.com/GavinLonDigital`. The app was built in the prerequisite course; the deploy layer was iterated across four sibling repos, culminating in the two used on camera.

| Repo | Created | Role | Docker/CI files? | Notable |
|---|---|---|---|---|
| **MagicStream** | 2025-06-24 | Original app (companion to the 14h45m build course `jBf7of9JTV8`) | **None** (verified: Dockerfile / compose / workflow all 404 at HEAD) | 146★; pure app code + seed JSON; the code-only baseline |
| **MagicStreamDocker** | 2025-12-11 | First containerization pass | Full: 4 Dockerfiles, 3 compose files, `deploy.yml` (13 revisions) | image names *without* `-prod` suffix |
| **MagicStreamDeploy** | 2026-01-13 | Deploy iteration; source of the HTTP cookie handlers | Full; `deploy.yml` (1 revision) | the repo students copy the HTTP login/logout handlers from |
| **MagicStreamApp** | 2026-01-31 | Built live in the "hard way" section; the CI/CD demo repo | Full; `deploy.yml` has the **SSH deploy stage** | what the terminal-path Action deploys |
| **MagicStreamMastery** | 2026-02-03 | Used in the intro **Docker Manager** segment | Full; `deploy.yml` is **build+push only** | **hardcodes the Atlas credential**; DB+seed commented out |

Video published **2026-02-12**, 9 days after the Mastery repo (and its committed credential) were created. Timeline is internally consistent: Docker → Deploy → App → Mastery, each building on the last.

## The key structural split: Mastery vs. the others (verified CONFIRMED)

The four docker repos' `deploy.yml` files are **all different** (4 distinct hashes). The load-bearing difference:

- **MagicStreamApp / Docker / Deploy** `deploy.yml` = **72 lines**, includes the full SSH deploy stage (`webfactory/ssh-agent@v0.9.0` → `ssh-keyscan` → `ssh "... git pull && docker compose pull && up -d --remove-orphans"`). → **true hands-off CD**.
- **MagicStreamMastery** `deploy.yml` = **54 lines**, ends after "Build & push Web image." **No SSH stage.** → CI only; the CD half is the **manual Docker Manager Deploy button**.

This is exactly the two-paths-in-one-course structure: the intro (Mastery) leans on the managed UI for CD; the hard-way section (App) automates CD over SSH. (See [[deployment-strategy-rationale]] and [[cicd-github-actions-pipeline]].)

## The committed credential (verified CONFIRMED)

`MagicStreamMastery/docker-compose.yaml` at HEAD (commit `651750d`) line 34:
```
MONGODB_URI: mongodb+srv://GavinL:Password1@magic-stream-movies.7qnqryr.mongodb.net/?appName=Magic-Stream-Movies
```
- Introduced 2026-02-03 (commit `87e355b`), **never removed** — publicly exposed 120+ days.
- **Isolated to Mastery only**: the other three docker repos use `mongodb://db:27017` (local container, no credential).
- Not tested, not used — text-presence check only. Full treatment in [[security-and-production-gaps]]; this is the topic's single most serious real-world issue.

## Image/version facts (verified CONFIRMED)

Client `package.json`: `react ^19.1.0`, `vite ^6.3.5`, `react-player ^2.16.0`, `react-router-dom ^7.6.2`, `axios ^1.9.0`, bootstrap 5. Server `go.mod`: `go 1.24.2`, `gin v1.10.1`, `langchaingo v0.1.13`, `golang-jwt/jwt/v5 v5.2.2`, `mongo-driver/v2 v2.2.2`. Prod images: client `node:20-alpine → nginx:stable-alpine`, server `golang:1.24-alpine → alpine:latest`.

## The prerequisite course

`jBf7of9JTV8` — "Build a Full Stack Movie Streaming App in Go" (freeCodeCamp, 2025-09-30, **14:45:25** per yt-dlp; freeCodeCamp's own article rounds it to "15 hours"). Same instructor, same app; teaches the Go/gin + React + MongoDB Atlas + OpenAI/LangChainGo build, and — notably — the *original* secure-cookie/HTTPS auth that this deploy course downgrades to HTTP ([[security-and-production-gaps]]).

## Key takeaways

- Five repos: one code-only original + four deploy iterations; the timeline is clean and matches the course narrative.
- **Mastery = CI-only (Docker Manager CD); App = full SSH CD** — the two-paths structure is baked into which repo has the SSH stage.
- The Atlas credential is **Mastery-only** and still live at HEAD — the topic's headline real-world risk.
- Stack is current: React 19 / Vite 6 / Go 1.24 / gin 1.10.
