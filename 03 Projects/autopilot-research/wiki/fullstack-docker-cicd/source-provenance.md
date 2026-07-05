# Source provenance

## Pipeline

- **Path:** operator-submitted single video (yt-dlp transcript + GitHub-API/DockerHub/official-docs ground truth; **no NotebookLM**).
- **Transcript:** `yt-dlp --write-auto-subs --write-subs --sub-langs "en.*" --sub-format vtt` → `clean_vtt.py` dedup → **240,505 chars / 5,316 timestamped lines, read IN FULL in the main loop** (4 reads).
- **Repo ground truth:** all Docker/CI files from the 5 MagicStream repos fetched via `raw.githubusercontent.com` + `api.github.com` before the workflow (`repo-truth/`).
- **Verification:** Workflow `wf_da1a6823-d91` — **9 dive + 14 refute-first verify agents**, ~1,170,854 subagent tokens, 413 tool calls, **zero agent deaths**. Model: Haiku 4.5 subagents.
- **Raw digest:** `raw/2026-07-05-fcc-docker-cicd-gavin-lon.md`.

## Source tiers

| Tier | Sources |
|---|---|
| **T0 primary — the video** | `lEcULR30-GM` transcript (full) + yt-dlp metadata/description |
| **T0 primary — the code** | `GavinLonDigital/{MagicStream, MagicStreamDocker, MagicStreamDeploy, MagicStreamApp, MagicStreamMastery}` at HEAD (raw files + commit/tree API); DockerHub public tags API for `gavinlon/magic-stream-*-prod` |
| **T1 official docs** | docs.docker.com (Compose Watch, build-push), github.com/docker/metadata-action README, github.com/webfactory/ssh-agent, nginx Docker image docs, Vite/CRA/webpack env docs, hostinger.com/support/* |
| **T1 identity** | freecodecamp.org/news/author/GavinLon, github.com/GavinLonDigital, youtube.com/c/gavinlon |
| **T2 context** | freeCodeCamp sponsorship pages; prerequisite course `jBf7of9JTV8` metadata |

## The 14 verdicts (refute-first)

**12 CONFIRMED / 2 PARTIAL / 0 REFUTED / 0 UNVERIFIED.**

| # | Claim (abbrev) | Verdict |
|---|---|---|
| C1 | Original MagicStream repo has no Docker/CI files | **CONFIRMED** (3× 404 at HEAD + transcript) |
| C2 | Mastery `deploy.yml` = build+push only; the other 3 have full SSH deploy stage | **CONFIRMED** (line-count + content diff at HEAD) |
| C3 | Mastery compose hardcodes live Atlas credential `GavinL:Password1@...` | **CONFIRMED** (raw file HEAD; isolated to Mastery; 120+ days) |
| C4 | `type=sha` tag is dead config; deploys are `:latest` only | **CONFIRMED** (metadata-action priority + DockerHub shows no `sha-*` tags) |
| C5 | Go server does NOT hot-reload under Compose Watch; Vite client does | **CONFIRMED** (`go run` + `action: sync`, no air) |
| C6 | Env-baking mis-framed as Vite-specific; it's all static SPAs; nginx does it natively | **CONFIRMED** (CRA/webpack docs + nginx 1.19 templates) |
| C7 | Docker Manager path is CI + manual-button CD (no auto-redeploy) | **CONFIRMED** (transcript + Hostinger docs) |
| C8 | Instructor identity / prior courses / prerequisite | **PARTIAL** (name "Lon" vs spoken "Lawn"; 14h45m vs "15h" — see [[caveats-and-corrections]]) |
| C9 | Stack versions (React 19 / Vite 6 / Go 1.24 / gin 1.10 / langchaingo / mongo v2) | **CONFIRMED** (live `package.json` + `go.mod`) |
| C10 | Exactly 6 secrets; ed25519 keygen + authorized_keys + chmod 700/600 | **CONFIRMED** (workflow refs + transcript) |
| C11 | Instructor states HTTPS + tests deliberately omitted, recommends HTTPS later | **CONFIRMED** (3 quoted timestamps + repo files) |
| C12 | Video metadata (2026-02-12, 3:58:43, ~102.6K views, Hostinger grant, prereq + repo links) | **CONFIRMED** (yt-dlp) |
| C13 | HTTPS→HTTP cookie downgrade (`Secure: true`→`false`), copied from Deploy repo | **CONFIRMED** (both userController.go files diffed) |
| C14 | Seed-in-prod one-shot container gated on healthcheck; prod-inappropriate per instructor; commented out in Mastery | **PARTIAL** (present-but-commented-out in Mastery; active in App/Deploy — precision qualifier) |

## Verifier behavior this pass

- **No misfires requiring main-loop override**, unlike several recent topics. The two PARTIALs are genuine precision nuances the verifiers surfaced correctly (C8 name-spelling; C14 commented-vs-active seed), not confabulations.
- **No discard-as-garble overturns.** All date-sensitive claims (repo timeline, DockerHub tags, video metadata, Atlas credential) ground-truthed on first check.
- **Empirical confirmation used where possible** — C4 was confirmed not just by reading `metadata-action` docs but by querying DockerHub's live tag list (only `latest`/`1.0.0`/`1.0.1`, zero `sha-*`).

## Ground-truth artifacts retained

`repo-truth/` (in scratchpad): `README.md`, `docker-compose.{,dev.,prod.}yaml`, 4 Dockerfiles, `go.mod`, `package.json`, and all four repos' `deploy.yml`. Transcript: `fcc-docker-cicd-transcript.txt`. Workflow output: `tasks/wbuv44obc.output`.

## Key takeaways

- Single-video source, but ground-truthed against live code (5 repos), official docs, and DockerHub's API — not transcript-only.
- 12/14 CONFIRMED, 2 precision PARTIALs, nothing refuted, zero deaths — a clean verification pass.
- The strongest evidence is empirical: the committed credential and the dead sha-tag were both confirmed by fetching the actual artifacts, not by inference.
