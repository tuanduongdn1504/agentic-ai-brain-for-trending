# Overview — the course, the app, the shape

## Source

- Video: [Master Full-Stack Docker & CI/CD – Build a Production-Ready Pipeline](https://www.youtube.com/watch?v=lEcULR30-GM) — freeCodeCamp.org (11.7M subs), uploaded 2026-02-12, **3:58:43**, ~102,624 views / ~3,239 likes at ingest (2026-07-05). Sponsored by a **Hostinger grant** (stated in description + intro).
- Raw digest: `raw/2026-07-05-fcc-docker-cicd-gavin-lon.md`

## What it teaches

Take an already-built full-stack app to production, containerized, with an automated deploy pipeline. The app is **MagicStream**: a movie-streaming demo with a React 19 (Vite) client, a Go + gin web API, MongoDB storage, and an OpenAI-powered feature that reduces a movie review to a one-word sentiment. The app itself was built in a **separate 14h45m prerequisite course** (`jBf7of9JTV8`, 2025-09-30); this course is *deployment only* and opens with an explicit DevOps separation-of-concerns pitch: "you don't need to watch the older code course to follow along."

The tagline sets the frame: *"Stop saying it works on my machine and start shipping professional-grade software to the cloud."* Containers are pitched as the cure for environment drift; a light-touch argument is made that even app developers should carry basic DevOps knowledge to be "more marketable."

## The "back-to-front" structure [00:08:32]

The course is deliberately inverted:

1. **The easy way first (0:08–0:40):** deploy MagicStream to a Hostinger VPS via the **Docker Manager** UI — "Compose from URL" pointed at a raw GitHub `docker-compose.yaml`, env vars set in a visual editor, one Deploy click. Then a CI/CD demo: edit code → push → a GitHub Action builds+pushes images to DockerHub → **click Deploy in Docker Manager** to pull and recreate containers.
2. **The hard way (0:40–3:58):** rebuild the same result by hand — local baseline, Dockerfiles, `docker build`/`docker run`, Compose, containerized Mongo with volumes+seed, dev/prod file splits, Compose Watch, DockerHub push, a one-time manual VPS setup, and finally a full GitHub Actions pipeline that SSHes into the VPS for hands-off CD.

The stated rationale [00:38:30]: *"I'm certainly not advocating for going under the hood and creating all the details yourself unnecessarily... but let's go under the hood a little bit to gain a deeper understanding."* The managed tool is the recommended default; the manual walk-through exists to demystify it.

## Headline verified findings

All verified refute-first against primary sources (repo files at HEAD, official docs, the transcript, DockerHub's public API, yt-dlp). Full evidence in [[source-provenance]].

- **CONFIRMED — the original repo is code-only.** `GavinLonDigital/MagicStream` (146★) has no Dockerfile, no compose file, no workflow; the entire container/CI layer lives in four sibling repos. ([[the-originals]])
- **CONFIRMED — the Docker Manager path is CI + *manual* CD.** After images push to DockerHub the operator must click Deploy; Hostinger has no auto-redeploy webhook. Only the terminal-path GitHub Action wires true hands-off CD via SSH. ([[cicd-github-actions-pipeline]])
- **CONFIRMED — a real MongoDB Atlas credential is committed** in the Mastery repo's compose file (`GavinL:Password1@...`), public since 2026-02-03, never removed, never mentioned on camera. ([[security-and-production-gaps]])
- **CONFIRMED — the Go server does not hot-reload under Compose Watch** as configured; only the Vite client does. ([[docker-compose-and-watch]])
- **CONFIRMED — the `type=sha` image tag is dead config**; every deploy is a mutable `:latest`. ([[cicd-github-actions-pipeline]])
- **CONFIRMED — the env-baking problem is mis-framed as Vite-specific**; it's every static SPA, and the fix is a standard pattern. ([[vite-runtime-env-injection]])
- **CONFIRMED — the instructor states on camera that HTTPS and automated tests are deliberately omitted** "so as not to convolute the overall process," and recommends adding HTTPS later. ([[security-and-production-gaps]])
- **PARTIAL — instructor name:** canonical spelling is **Gavin Lon** (freeCodeCamp author page, GitHub `GavinLonDigital`, YouTube `c/gavinlon`); he pronounces it such that auto-captions render "Gavin Lawn." Same person, not a garble in the wrong-word sense. ([[caveats-and-corrections]])

## Who the instructor is

**Gavin Lon** — London-based software engineer (20+ yrs), freeCodeCamp core contributor, historically a **C#/.NET/Blazor** educator (top repo `ShopOnlineSolution`, a Blazor cart, 187★; freeCodeCamp C# book + Microsoft C# certification + Advanced C# + Neo4j + n8n + React-with-.NET courses). This Docker/CI-CD course is a DevOps expansion of that catalog, and the direct sequel to his Sept-2025 MagicStream build course. ([[caveats-and-corrections]] for the identity detail.)

## Key takeaways

- The value is the **end-to-end arc**: a real app, containerized, pushed to a registry, deployed to a real cloud VPS, then automated — the shipping half that most "build with AI" content skips.
- The **managed-first, manual-second** structure is a good teaching pattern and worth stealing for internal docs: show the happy path, then peel one layer.
- Treat the course as **reference-with-asterisks**: the mechanics are sound and current (React 19 / Vite 6 / Go 1.24 / gin 1.10), but several security and correctness details need patching before any of it touches production — catalogued in [[security-and-production-gaps]] and [[caveats-and-corrections]].
