# Deployment strategy — managed vs. self-hosted, and the sponsor lens

## Source

Course intro + Docker Manager segment [00:08:29]–[00:40:25]; Hostinger official docs (support pages, verified 2026-07-05); cross-read against [[external|Storm Bear: self-hosted-devops-oss]].

## The three deploy paths this course actually shows

1. **Hostinger Docker Manager (managed UI).** Paste a raw `docker-compose.yaml` URL → "Compose from URL" → set env vars in a visual editor → Deploy. Container status, logs, and a browser terminal are built in. Verified: Docker Manager ships **free on all Hostinger KVM VPS tiers** (KVM 1 $6.49/mo → KVM 8 $25.99/mo as of mid-2026), Ubuntu 24.04 is a stock template, root SSH is the default, and a browser terminal auto-authenticates as root.
2. **Manual VPS + Docker Compose (terminal).** SSH in (as root), `git clone`, `nano .env`, `docker compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d`. This is the "one-time setup" before automation.
3. **GitHub Actions → SSH → VPS (automated CD).** The Action builds+pushes images, then SSHes into the VPS to `git pull` + `docker compose pull` + `up -d --remove-orphans`. This is the only path with true hands-off deployment.

## The manual-CD gotcha (verified)

The intro's Docker Manager demo is **CI + manual CD**: the GitHub Action pushes new images to DockerHub, but *someone still clicks Deploy* in the Docker Manager UI to pull and recreate. Verified against Hostinger's docs — there is **no auto-redeploy webhook, polling, or image-watch** in Docker Manager; automatic redeploy on new images requires external tooling (e.g. Watchtower) or the SSH-based Action from path 3. The course never spells this out in the Docker Manager section, so a viewer can leave thinking the managed path is fully automated when it isn't. Only path 3 closes that loop.

## The 2×2: what optimizes what

|  | **Low time-to-first-deploy** | **Low cost-to-operate at scale** |
|---|---|---|
| **Managed** | **Hostinger Docker Manager** (this course) — click-to-deploy, free with the VPS, sponsor-aligned; you still rent the VPS and get manual-CD unless you add the Action | Vercel / Render / Fly — great DX, bills climb with usage |
| **Self-hosted** | Coolify one-click on your own box — near-PaaS UX, you own the metal | **Coolify / Dozzle / self-hosted stack** (see [[external|Storm Bear: self-hosted-devops-oss]]) — lowest steady-state cost, highest ops burden |

Hostinger Docker Manager sits **upper-left** (fast to start, managed) and the vault's Coolify thesis sits **lower-right** (cheapest to run, self-hosted). They are answering different questions, not disagreeing.

## Sponsor bias — surfaced, not buried

The course is **explicitly Hostinger-grant-funded** (stated in the intro and description, with a branded discount code). Consequences to keep in view:

- Hostinger Docker Manager is the *only* deploy target shown. Coolify, Dokploy, DigitalOcean App Platform, Fly, Render — none are compared. GitHub Actions is the only CI/CD tool.
- The framing "deployment is drudgery; Docker Manager makes it painless" is true *and* sponsor-convenient. The painless part is real; the "this is the way" implication is the paid placement talking.
- This is the same pattern flagged in [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] (instructor says "Claude Code is the best" on camera but picks Copilot for students because it's "popular and safe"). **Prime directive handling: document the bias, don't discard the content** — the Docker/Compose/CI mechanics are vendor-neutral and reusable; only the deploy *target* is sponsored.

## Applicability to hireui / the vault

- If ops-friction is the constraint and budget is fine → a managed path (Hostinger-style, or the DX-heavier Vercel/Render) gets you shipping fastest.
- If steady-state cost is the constraint → the [[external|Storm Bear: self-hosted-devops-oss]] Coolify route wins, at the cost of you owning uptime.
- The **vendor-neutral** takeaways — base+dev+prod compose overrides, runtime env injection, the SSH-deploy Action, `--remove-orphans` rolling replace — transfer to *any* target. That's the part worth lifting.

## Key takeaways

- Three deploy paths in one video; only the SSH-Action path is truly hands-off CD.
- Docker Manager is genuinely low-friction and free-with-VPS, but its CD is manual unless you add the Action.
- Managed-vs-self-hosted is a real objective fork (ops-friction vs. cost), not a contradiction with the corpus.
- The sponsor bias is real and one-sided on the *target*; the mechanics are portable and unaffected.
