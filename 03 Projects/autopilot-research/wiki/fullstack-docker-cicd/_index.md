# fullstack-docker-cicd — topic index

> **What:** A ~4h freeCodeCamp course, **"Master Full-Stack Docker & CI/CD – Build a Production-Ready Pipeline"** (video `lEcULR30-GM`, 2026-02-12, Hostinger-grant-sponsored), that takes an existing full-stack app — **MagicStream** (React 19 + Vite client / Go + gin server / MongoDB, with an OpenAI review-sentiment feature) — from local bare-metal dev to a containerized production deployment on a **Hostinger VPS**, first the easy way (Hostinger **Docker Manager** UI) then the hard way (Dockerfiles → Compose → DockerHub → **GitHub Actions** CI/CD over SSH). Instructor: **Gavin Lon** (GitHub `GavinLonDigital`, a longtime C#/.NET/Blazor freeCodeCamp educator).
> **Created:** 2026-07-05 (operator-submitted single video; 240K-char transcript read in full in the main loop; double deep-dive into the 5-repo MagicStream family + Hostinger/Docker/GitHub-Actions originals; 9 dive + 14 refute-first verify agents, workflow `wf_da1a6823-d91`, ~1.17M tokens, 413 tool calls, **12 CONFIRMED / 2 PARTIAL / 0 refuted, zero agent deaths**).
> **Why it matters here:** the corpus is deep on *how agents write code* but thin on *how the code actually ships*. This is the first end-to-end **deploy layer** — containerization + CI/CD to a real cloud VPS — and it maps cleanly onto hireui's Goal-#2 shipping story and onto the vault's [[external|Storm Bear: self-hosted-devops-oss]] cost thesis (managed Hostinger vs. self-hosted Coolify). It is also a **teaching-integrity case study**: the course is honest about *some* omissions on camera (HTTPS, tests) yet ships a live production-grade credential leak it never mentions.

## Articles

- [[overview]] — the course, the "back-to-front" structure, the MagicStream app, headline verified findings
- [[deployment-strategy-rationale]] — Hostinger Docker Manager vs. self-hosted (Coolify) vs. the manual VPS path; the 2×2 managed/self-hosted × time-to-deploy/cost matrix; sponsor bias, surfaced not buried
- [[docker-fundamentals-as-taught]] — images/containers/Dockerfiles, layer caching, dev/prod split, multi-stage prod builds (nginx + scratch-ish alpine), the port-mapping and `-p` live-error teaching moments
- [[docker-compose-and-watch]] — single-command orchestration, base+dev+prod override "inheritance", containerized Mongo + volumes + one-shot seed, and the **Compose Watch Go-hot-reload correction**
- [[vite-runtime-env-injection]] — the `env.template.js` + `envsubst` + `window.__ENV` runtime-config pattern, and why the "this is a Vite problem" framing is **wrong** (it's every static SPA; nginx does it natively)
- [[cicd-github-actions-pipeline]] — the `deploy.yml` walkthrough, 6 repo secrets, ed25519 keygen + `authorized_keys`, the **dead `type=sha` tag config**, and the mutable-`:latest` deploy
- [[the-originals]] — the 5-repo MagicStream family forensics (which repo has what, the timeline, the Mastery-vs-App workflow split)
- [[security-and-production-gaps]] — the 21-gap catalog, **stated-on-camera vs. silent**, headed by the committed MongoDB Atlas credential
- [[caveats-and-corrections]] — name spelling, prerequisite-duration nuance, the two PARTIAL verdicts, sponsor framing, version drift
- [[source-provenance]] — pipeline, source tiers, all 14 verdicts, the workflow accounting

## Key takeaways (topic level)

1. **Deploy is the missing half.** Where [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] and the JSM/Pocock topics stop at "the app runs," this course is *only* about shipping it — containerize → registry → cloud → automate. That's the layer hireui's Goal #2 actually lives in. ([[overview]])
2. **"Back-to-front" is the pedagogy.** Deploy the easy way first (Docker Manager, ~30 min), *then* rebuild it by hand for 3h to expose what the UI abstracts. Explicitly not advocating hand-rolling every deploy — the point is understanding the abstraction. ([[overview]], [[deployment-strategy-rationale]])
3. **The taught "CI/CD" splits two ways.** The Docker Manager path is **CI + manual-button CD** (you click Deploy after images push); only the terminal path wires the GitHub Action to SSH into the VPS for true hands-off CD. Both are in the same video, in different repos. ([[cicd-github-actions-pipeline]], [[the-originals]])
4. **Honest about the easy gaps, silent on the dangerous one.** On camera the instructor says he *deliberately* dropped HTTPS and automated tests "so as not to convolute" the pipeline — a defensible teaching choice. Off camera, the repo used for the Docker Manager demo hardcodes a real MongoDB Atlas username+password that has been public for 120+ days and is never mentioned. ([[security-and-production-gaps]])
5. **Two technical claims don't survive verification.** (a) Compose **Watch does not hot-reload the Go server** as configured — `go run` is a compiled process, `action: sync` only copies files; only the React/Vite side actually hot-reloads. (b) The env-baking problem is framed as **Vite-specific** but is inherent to every statically-built SPA; the workaround is a standard pattern nginx even ships natively. ([[docker-compose-and-watch]], [[vite-runtime-env-injection]])
6. **The `type=sha` image tag is dead config.** `docker/metadata-action` computes a short-SHA tag, but `build-push-action` consumes only `outputs.version` (which resolves to `latest`), so every deploy overwrites `:latest` with no immutable, rollback-able tag — confirmed empirically (DockerHub shows only `latest` + hand-pushed `1.0.0`/`1.0.1`, zero `sha-*` tags). ([[cicd-github-actions-pipeline]])
7. **Managed vs. self-hosted is a real fork, not a contradiction.** This course optimizes ops-friction (managed Hostinger, sponsor-aligned); the vault's [[external|Storm Bear: self-hosted-devops-oss]] optimizes cost (self-hosted Coolify). Same problem, different objective — document the trade, don't average it. ([[deployment-strategy-rationale]])

## Cross-links

- [[external|Storm Bear: self-hosted-devops-oss]] — the cost-optimization counterpart; Coolify/Dozzle vs. Hostinger Docker Manager as opposite poles of the deploy-UX spectrum
- [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] — sibling beginner full-stack course (VN, NestJS/React); this one is its deploy-layer complement — docs-first-then-build vs. build-then-ship
- [[external|Storm Bear: telegram-remote-control-stack]] — shares the VPS + Docker + SSH deployment substrate (Tailscale/Cloudflare Tunnel hardening recipes apply directly here)
- [[external|Storm Bear: harness-engineering]] — the CI/CD pipeline is a concrete "humans steer, agents/automation execute" runtime harness at the deploy layer

## Source

- Primary video: https://www.youtube.com/watch?v=lEcULR30-GM (freeCodeCamp.org, 3:58:43, ~102.6K views)
- Raw digest: `raw/2026-07-05-fcc-docker-cicd-gavin-lon.md`
- Originals: `github.com/GavinLonDigital/{MagicStream, MagicStreamDocker, MagicStreamDeploy, MagicStreamApp, MagicStreamMastery}` + prerequisite `youtube.com/watch?v=jBf7of9JTV8`
