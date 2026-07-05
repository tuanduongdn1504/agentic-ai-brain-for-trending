# (C) Pilot methods — applying the freeCodeCamp Docker & CI/CD course to your workflow

> **Source topic:** [[wiki/fullstack-docker-cicd/_index]] — Gavin Lon's "Master Full-Stack Docker & CI/CD" (freeCodeCamp, `lEcULR30-GM`), verified 12 CONFIRMED / 2 PARTIAL / 0 refuted (`wf_da1a6823-d91`).
> **Created:** 2026-07-05
> **Your contexts:** hireui (TalentAxis recruitment SaaS, `/Users/Cvtot/monorepo/hireui`, Goal-#2 real-software deploy target) · autopilot-research pipeline + vault · personal Claude harness · Scrum coaching · evals harness (`evals/`)
> **How to read:** methods grouped A–E by where they land. Each has an effort tag and a "why this course earns it." **Skip-list at the bottom** is as important as the menu — this is a deploy/DevOps course, not an AI-coding course, so several natural-looking applications are traps.

---

## The one-paragraph orientation

This is the corpus' **first deploy-layer topic** — every other topic is about *writing* code with AI; this one is about *shipping* it (containerize → registry → cloud VPS → automate). That makes it the most directly relevant topic yet to hireui's **Goal #2 ("build software with these tools")** — because Goal #2 is not finished when the code works, it's finished when it *ships*, and shipping is exactly the half this course covers. The catch: the course is honest about its cosmetic omissions (HTTPS, tests) but ships a live committed database credential it never mentions — so the highest-value pilots are as much about the **verification discipline the course lacks** as about the mechanics it teaches well.

**Headline recommendation (do these three first):**
1. **A1 — committed-secret CI grep-gate** (zero-install, ~30 min) — the course's single worst gap becomes your cheapest safeguard.
2. **A2 — base + dev + prod compose "inheritance"** for hireui's deploy (~half a day) — the strongest reusable pattern in the course.
3. **A3 — SSH-deploy GitHub Action with the sha-tag-not-`latest` fix** (~half a day) — hands-off CD, with the course's dead-config bug pre-corrected.

---

## Class A — hireui: real deployment pipeline (highest leverage; this is Goal #2's shipping half)

### A1 — Committed-secret CI grep-gate ⭐ (zero-install, ~30 min)
The course's headline failure is a live `mongodb+srv://GavinL:Password1@...` sitting in a public compose file for 120+ days. Turn that into your cheapest guarantee it never happens in hireui: add a CI step (or a pre-commit hook) that greps tracked files for connection-string/secret patterns (`://[^/]*:[^@]*@`, `sk-`, `AKIA`, `-----BEGIN`, high-entropy `.env`-shaped assignments) and **fails the build** on a hit. Even better, wire a real scanner (`gitleaks` / `trufflehog`) as a required check. **Why:** this is the course's most expensive teaching gap converted into a one-time, permanent safeguard for a SaaS handling candidate PII. Respects hireui's CONSTITUTION (a check, not a refactor); runs on an `agent-*` branch per I-2.

### A2 — Base + dev + prod compose "inheritance" for hireui ⭐ (~half a day)
Adopt the course's cleanest pattern: one base `docker-compose.yaml` with shared service definitions + `docker-compose.dev.yaml` and `docker-compose.prod.yaml` overrides, merged with `-f base -f override`. Dev override = source-mount + dev servers + local DB; prod override = pinned registry images + `restart: always` + no dev tooling. **Why:** hireui is a monorepo; this gives you one environment definition with per-environment deltas instead of drifting parallel files. Vendor-neutral, works against any deploy target. Keep secrets out of all three (see A1).

### A3 — SSH-deploy GitHub Action, with the sha-tag fix baked in ⭐ (~half a day)
Lift the course's `deploy.yml` (checkout → DockerHub/registry login → `metadata-action` → `build-push-action` → `webfactory/ssh-agent` → `ssh-keyscan` → SSH `git pull` + `compose pull` + `up -d --remove-orphans`) — **but fix the verified dead config**: use `tags: ${{ steps.meta.outputs.tags }}` (not `outputs.version`) so images get **both** `:latest` **and** an immutable `sha-<short>` tag, giving you real rollback. Deploy by digest/sha in prod, not `:latest`. **Why:** the course teaches a working hands-off-CD shape and a subtle bug in the same file; you get the shape and skip the bug.

### A4 — Multi-stage prod Dockerfiles + non-root USER (~2–3 hrs)
Copy the course's genuinely good multi-stage prod pattern (build stage → slim runtime: static assets on nginx, compiled binary on alpine) for hireui's services, and **close the gap the course leaves**: add a non-root `USER`, pin base images by digest (not `:latest`/`:stable-alpine`), and add a `HEALTHCHECK`. **Why:** small, secure, reproducible prod images; the course gives you 80% and you add the 20% it omits ([[wiki/fullstack-docker-cicd/security-and-production-gaps]]).

### A5 — HTTPS / TLS as a first-class deploy requirement (constraint line, ~15 min to write)
The course *deliberately* runs plain HTTP with `Secure: false` auth cookies and says "add HTTPS later." For a recruitment SaaS, "later" is now. Add a hireui CONSTITUTION / deploy-checklist line: **no production deploy without TLS termination and `Secure`/`HttpOnly`/`SameSite` cookies.** **Why:** the course itself flags this as the thing to fix; make it a gate, not a TODO.

### A6 — Runtime env injection for hireui's frontend (~2–3 hrs, *if* hireui ships a static SPA build)
If any hireui frontend is a statically-built SPA that needs per-environment config, adopt the runtime-injection pattern (`env.template.js` + nginx's native `envsubst` templates + a `window.__ENV` read) so one image runs in dev/staging/prod. **But** apply the corrections: scope `envsubst` to named vars, add `Cache-Control: no-cache` on the injected file, and prefer nginx's built-in template mechanism over a hand-rolled CMD. **Why:** one-image-many-environments without rebuilds. **Check first** whether hireui uses Next.js SSR/RSC — if so this is largely moot (server reads env at runtime), so verify the build model before spending the time.

### A7 — Deploy-target decision ADR for hireui (~1–2 hrs)
Write a short ADR using this topic's 2×2 (managed ↔ self-hosted × time-to-deploy ↔ cost-to-operate): where does hireui sit, and why? Managed (Vercel/Render/Hostinger-style) optimizes ops-friction; self-hosted (Coolify, per [[external|Storm Bear: self-hosted-devops-oss]]) optimizes cost. **Why:** forces the deploy decision to be explicit and revisitable instead of accidental. Pairs with E1.

---

## Class B — autopilot-research pipeline + vault self-improvement

### B1 — Containerize the autopilot-research pipeline (~half a day)
The pipeline (`bin/autopilot-drain.py`, the notebooklm/yt skills, the `.venv` with Playwright) is ~700MB of finicky per-worktree setup. A `Dockerfile` + `docker-compose.yaml` would make it reproducible across worktrees and one `docker compose run` to drain a topic. **Why:** the CLAUDE.md already documents the exact env-drift pain ("this user's `python3` shim was broken," per-worktree `.venv`) that containers exist to kill — this is the course's core thesis applied to your own tooling. Keep it optional (the local `.venv` path stays valid).

### B2 — "Stated-vs-silent" audit as a standing verify lens ⭐ (prompt addition, ~20 min)
This course's most transferable *meta*-lesson: it was candid about easy omissions and silent about the dangerous one. Add a line to the verify-agent / skeptic prompt template for **tutorial/course topics**: *"Separately list what the source explicitly acknowledges omitting vs. what it silently omits; a source's on-camera candor is not a warranty for the rest."* **Why:** it's exactly how this pass caught the committed credential the instructor never mentioned — codify it so the next course topic gets the same treatment for free.

### B3 — Empirical-confirmation-over-doc-inference habit (prompt addition, ~15 min)
The strongest verdict this pass (C4, dead sha-tag) was confirmed not by reading `metadata-action` docs but by **querying DockerHub's live tag list** and seeing zero `sha-*` tags. Add to the verify template: *"Where a claim about a live artifact is checkable against a live API/registry/endpoint, prefer the empirical check over doc-inference."* **Why:** turns "the docs say it should" into "the registry shows it does/doesn't."

### B4 — Deterministic link-check ship-gate for wiki topics (~1–2 hrs, reusable)
Independent of this course but reinforced by its `--remove-orphans`-style determinism: add a pre-commit/CI step that resolves every `[[wiki link]]` and relative path in a shipped topic against the branch tree and fails on a broken link — pinning the git ref (the hoidanit review-race lesson). **Why:** the vault ships wikis constantly; a deterministic gate beats agent link-checks that race on branch switches.

---

## Class C — subscribe / follow / queue

### C1 — Follow Gavin Lon for the deploy/DevOps beat (queue line)
He's a prolific freeCodeCamp educator (C#/.NET/Blazor → Neo4j → n8n → now Docker/CI-CD) with a consistent "build-then-deploy" arc and a companion-repo discipline. Queue his channel (`youtube.com/c/gavinlon`) + freeCodeCamp for the next deploy-focused course. **Why:** deploy-layer content is rare in the corpus; he's a reliable source of it.

### C2 — Watch the prerequisite build course only if you want the app internals (skip otherwise)
`jBf7of9JTV8` (14h45m) builds MagicStream itself (Go/gin + React + MongoDB Atlas + OpenAI/LangChainGo). **Skip unless** you specifically want a Go+gin+Mongo reference build — the deploy course stands alone, as its own intro insists. **Why:** 14h45m is a big spend for context you don't need to apply the deploy patterns.

### C3 — Queue a Coolify / self-hosted-devops-oss cross-read (queue line)
Before A7's deploy decision, re-read [[external|Storm Bear: self-hosted-devops-oss]] so the managed-vs-self-hosted call is informed by both poles, not just the sponsored one. **Why:** this course only shows the managed side; the vault already holds the counter-case.

---

## Class D — Scrum coaching

### D1 — "Deploy is part of Done" workshop artifact (~1–2 hrs)
Use the course's back-to-front structure as a coaching device: teams that treat deployment as someone-else's-problem ship "done" code that isn't shippable. Build a Definition-of-Done checklist from this topic's gap catalog — TLS, no committed secrets, healthchecks, rollback-able tags, a test gate — and run it as a team exercise. **Why:** concrete, verified, non-abstract; turns "it works on my machine" into a shared DoD.

### D2 — The stated-vs-silent gap as a code-review culture lesson (~30 min talk)
The course is a clean case study in how *acknowledged* limitations lull reviewers into trusting the *unacknowledged* ones. Coach reviewers to ask "what did the author NOT mention?" not just "is what they mentioned correct?" **Why:** the committed credential survived 120+ days precisely because the on-camera honesty about HTTPS made everything else feel vetted.

### D3 — DevOps-literacy-as-marketability framing for junior devs (~30 min)
The instructor's pitch — "basic DevOps knowledge makes you more marketable" — is a good, true motivator for the junior-onboarding curriculum you're already building (see hoidanit D1). Add a "ship your own project end-to-end once" milestone. **Why:** pairs with the VN-junior-onboarding thread; shipping-literacy is a durable differentiator.

---

## Class E — evals / bake-offs

### E1 — Managed-vs-self-hosted deploy bake-off for hireui ⭐ (~1 day, one-time)
Stand up a hireui staging deploy two ways — a managed target (Vercel/Render/Hostinger-style Docker Manager) and a self-hosted Coolify box — and measure: time-to-first-deploy, steady-state monthly cost, ops-touches-per-week, rollback ease. Feed the winner into A7's ADR. **Why:** resolves the managed-vs-self-hosted fork with hireui's real numbers instead of the course's sponsor-shaped default.

### E2 — CI pipeline correctness eval (~2–3 hrs)
Adapt this course's `deploy.yml` into hireui's pipeline, then write a tiny eval that asserts the things the course got wrong: (a) a pushed image carries an immutable `sha-*` tag (not just `:latest`); (b) a deliberately-planted fake secret trips the A1 gate; (c) `docker compose config` validates for all three env overlays. **Why:** encodes the verified corrections as regression tests — the pipeline can't silently regress into the course's bugs.

### E3 — Compose Watch reload verification (~1 hr, if you containerize any Go/compiled service)
If B1 or any hireui backend runs in a dev container, verify hot-reload actually works before trusting it: the course *claims* Compose Watch reloads a Go server and it doesn't (`go run` + `action: sync` = no reload). Test it, and if broken, switch to `sync+restart` or add `air`. **Why:** a verified-false claim from the source; don't inherit the broken DX assumption.

---

## Skip-list (natural-looking applications that are traps)

- **❌ Don't copy the course's `deploy.yml` verbatim** — it ships the dead `type=sha` config (deploys mutable `:latest`, no rollback). Always apply the A3 `outputs.tags` fix.
- **❌ Don't trust "Compose Watch hot-reloads everything"** — false for compiled backends (Go). Only the Vite/HMR client reloads as configured (E3).
- **❌ Don't adopt the "it's a Vite problem" framing** — env-baking is every static SPA; don't switch bundlers thinking it fixes anything (it doesn't).
- **❌ Don't deploy as `root` or over plain HTTP** — the course does both for teaching simplicity; both are non-negotiable to fix for hireui (A5, and a dedicated deploy user).
- **❌ Don't treat Docker Manager (or any managed UI) as fully automated CD** — its CD is manual-button unless you add the SSH Action (A3). Know which half you have.
- **❌ Don't take Hostinger as the recommended target** — that's the paid grant talking; the mechanics are vendor-neutral, the target is a real decision (A7/E1).
- **❌ Don't over-index on this being an "AI coding" course** — it isn't; it's DevOps. The AI-workflow pilots live in the other topics. This one's value is the shipping layer + the verification discipline.

## Critic reframe (the one-sentence honest take)

This course is a **solid, current, honestly-scoped mechanics tutorial wrapped around one silent production-grade security failure** — so the right way to "apply" it is to take the genuinely good patterns (compose overrides, multi-stage builds, SSH-deploy Action) into hireui *while* installing the guardrails the course itself lacks (secret-gate, sha-tags, TLS, non-root), and to bank the stated-vs-silent audit as a permanent verify lens for every future tutorial-sourced pattern.

## Suggested next action

Do **A1 (committed-secret grep-gate)** this week on an `agent-*` branch in hireui — it's ~30 min, zero-install, and closes the exact hole this course left open — then scope **A2 + A3** (compose overlays + fixed SSH-deploy Action) as hireui's shipping story for Goal #2. Queue **E1** (managed-vs-self-hosted bake-off) for when a staging deploy is worth a day. If you'd rather start from the vault side, **B2 (stated-vs-silent verify lens)** is a 20-minute prompt edit that pays off on the next course topic.
