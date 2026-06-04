# (C) Autopilot Loop — 2026-06-04-13

> **Trigger:** `/loop autopilot research <operator brief>` (manual session-bound burst)
> **Topic:** self-hosted-devops-oss — 8 operator-curated open-source DevOps tools
> **Started:** 2026-06-04T13:29 (+07)
> **Ended:** 2026-06-04T~13:55 (+07)
> **Duration:** ~25m
> **Worktree:** `.claude/worktrees/jovial-ramanujan-7ccbe5` (branch `claude/jovial-ramanujan-7ccbe5`)

## Pre-flight deviations (logged per invariant #4 — never fabricate)
- **No `.venv` in this worktree** → `notebooklm-py` + yt-pipeline (Strategy A/B) unavailable; `notebooklm login` also needs interactive Google OAuth, infeasible in an autonomous loop.
- **Substituted Strategy → path 3-webfetch / GitHub-API direct fetch.** GitHub repos are best served by `curl https://api.github.com/repos/<o>/<r>` (metadata) + `.../readme` (content) anyway. This is a legitimate ingestion surface (path 3/6) and avoids fabrication: all metadata is from the live API; all README content is verbatim source.
- **`yt-dlp` present system-wide** (unused this run).

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio | Note |
|-------|---------------|-------------|------------|-------|------|
| 1 | 8 repos (1 consolidated raw file) | 1 (cold-start: topic absent) | 2 (follow-up gaps surfaced) | primary topic gap CLOSED (1.0 vs baseline); cold-start artifact surfaces 2 sub-gaps | created full topic: 10 files |

**Goal-driven success measure (Rule 4) — more meaningful than gap-ratio for a curated-list task:** operator named 8 specific repos → **8/8 compiled (100% scope)** with verified metadata + honest caveats.

## Sources ingested
- `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (path 3-webfetch; GitHub API metadata for all 8 + verbatim README extracts + operator brief). Repos:
  - Infisical/infisical · coollabsio/coolify · podman-container-tools/buildah (moved from containers/buildah) · ctrlplanedev/ctrlplane · coroot/coroot · amir20/dozzle · groundcover-com/caretta · stefanprodan/dockprom

## Wiki articles created/updated
- `wiki/self-hosted-devops-oss/_index.md` (NEW)
- `wiki/self-hosted-devops-oss/infisical.md` (NEW)
- `wiki/self-hosted-devops-oss/coolify.md` (NEW)
- `wiki/self-hosted-devops-oss/buildah.md` (NEW)
- `wiki/self-hosted-devops-oss/ctrlplane.md` (NEW)
- `wiki/self-hosted-devops-oss/coroot.md` (NEW)
- `wiki/self-hosted-devops-oss/dozzle.md` (NEW)
- `wiki/self-hosted-devops-oss/groundcover-caretta.md` (NEW)
- `wiki/self-hosted-devops-oss/dockprom.md` (NEW)
- `wiki/self-hosted-devops-oss/cost-displacement-thesis.md` (NEW — synthesis)
- `wiki/_master-index.md` (UPDATED — added "self-hosted-devops-oss" topic; FIRST non-Claude/non-agent topic in the wiki)

## Final metric
- `gaps_closed_ratio` = **1.0** against cold-start baseline (primary topic gap closed); **scope completion = 8/8 (100%)**.
- 2 follow-up gaps newly surfaced + logged (see below).
- Stop reason: **target_ratio reached + finite operator-curated scope fully covered**. Per autopilot invariant #6 (never recurse) and `/loop` dynamic-mode finite-task rule → loop STOPS (no ScheduleWakeup).

## Accuracy / honesty notes (invariant #4, Rule 12 fail-loud)
- **All repo metadata verified** via live GitHub API 2026-06-04 (stars/license/language/created/last-push).
- **All pricing claims flagged UNVERIFIED** ($22k Vault / $25 dyno / $19 user / $23 host = operator-brief figures only).
- **Corrected operator framing where inaccurate:**
  - "Groundcover" → the OSS repo is **Caretta** (a service map), NOT the full commercial Groundcover product; Caretta last pushed 2025-03-17 (~15mo stale).
  - **Buildah** moved orgs (`containers/` → `podman-container-tools/`).
  - **Infisical** "fully free" is true only for the MIT core, not the commercial `ee/` directory.
  - **Coolify** "$0" is a license claim — README itself states ~$4–5/mo per VPS.
  - **Ctrlplane** flagged: early-stage (146★, 2024) + AGPL-3.0 copyleft = highest adoption risk of the 8.
  - "Almost banned / billions in lost revenue" = rhetoric; several tools have their own paid Cloud/Enterprise tiers (coexistence/freemium, not suppression).

## Top-3 unclosed gaps (follow-up ingests)
1. **Pricing verification** — fetch each vendor's current pricing page to confirm/replace the operator's cost figures (watch for bot-protection → use `(C) bypass-403-escalation.md` tier discipline).
2. **eBPF observability deep-compare** — Coroot vs the Groundcover *product* vs Caretta as a dedicated comparison article (the 3-way distinction is currently only sketched).
3. **No hands-on pilot** — lowest-friction pilot = Dozzle (one `docker run`); highest-savings pilot = Coolify. Ctrlplane + Caretta need an explicit risk decision before any pilot.

## Suggested next action
Pilot **Dozzle** (5-min, zero-risk) or **Coolify** (biggest bill-killer) on a sandbox VPS and write the result to `output/`, OR run a follow-up ingest on live vendor pricing to verify the cost claims. This topic is a strong candidate to leave as-is (operator said "LƯU LẠI" — save — and it's saved + cross-linked); no promotion to Storm Bear curated wiki recommended yet (single-cycle, unverified pricing).
