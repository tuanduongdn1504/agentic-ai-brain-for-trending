# (C) Entity 2 — Architecture + Distribution: dual-product-in-monorepo + 4-surface

**Source scope:** 7-app monorepo + Rowboat Labs commercial entity + YC S24 + 4-surface distribution + legacy SaaS stack + triple-runtime architecture

## 1. 7-app monorepo

| App | Status | Purpose |
|---|---|---|
| `apps/x/` | **Primary flagship** | Electron desktop personal-AI-coworker |
| `apps/rowboat/` | **Legacy (maintained-but-secondary)** | Next.js multi-agent SaaS |
| `apps/rowboatx/` | Active | Next.js sibling frontend (likely transition target) |
| `apps/cli/` | Active | `@rowboatlabs/rowboatx` v0.16.0 Hono + ink CLI server |
| `apps/python-sdk/` | Active | `rowboat` v5.0.1 PyPI Python SDK |
| `apps/docs/` | Active | mkdocs-style documentation site |
| `apps/experimental/` | Incubation | chat_widget + simulation_runner + tools_webhook |

**Classification:**
- Production-primary: 1 (`apps/x`)
- Production-secondary: 3 (`apps/rowboat` legacy + `apps/rowboatx` transition + `apps/cli`)
- Developer-facing: 2 (`apps/python-sdk` + `apps/docs`)
- Incubation: 1 (`apps/experimental` with 3 sub-projects)

## 2. Dual-product strategy (corpus-first observation)

**Product 1 (January 2025 launch — legacy):**

- **Identity:** Rowboat multi-agent SaaS framework
- **Location in repo:** `apps/rowboat/` (Next.js dashboard) + `apps/rowboatx/` (frontend companion) + `apps/python-sdk/` (Python client)
- **Tech stack:** Next.js + Auth0 + MongoDB + Redis + Qdrant + RAG + Firecrawl + S3 + Composio + Klavis + Twilio (voice) + Gemini-file-parsing
- **Target:** developers/teams building multi-agent workflows
- **Distribution:** Docker self-host + (presumed) hosted SaaS tier
- **Python SDK targets this product's API**

**Product 2 (flagship pivot — current primary):**

- **Identity:** Rowboat knowledge-graph-personal-AI-coworker
- **Location in repo:** `apps/x/` Electron app + `apps/cli/` CLI server
- **Tech stack:** Electron + React + Vite + TailwindCSS + Tiptap + Vercel AI SDK + local Markdown vault + (optional Qdrant)
- **Target:** end users (personal productivity)
- **Distribution:** Mac/Windows/Linux desktop binaries

**docker-compose.yml evidence of dismantling:** 6 services commented out (rowboat_agents / copilot / tools_webhook / simulation_runner / chat_widget / twilio_handler). Legacy multi-agent SaaS infrastructure being wound down.

**Shared subsystems:** `apps/cli/src/` has matching subsystem names to `apps/x/packages/core/src/` (agents / application / config / di / knowledge / mcp / models / runs). Suggests logic convergence: CLI = alternative runtime for same core.

**Observation classification:**
- **Pattern #58 Branding-Package Divergence (CONFIRMED v42)** — potential 3rd data point (product-pivot-in-monorepo sub-variant). **Observational only** — flag for 3rd data point watch; do NOT register standalone at v43. Distinct from 58a (oh-my-claudecode rename) + 58b (ruflo rebrand-with-transitional-preserve) — this is product-strategy-pivot.

## 3. Electron app architecture (apps/x nested pnpm workspace)

**Dependency order:** shared → core → preload → renderer + main

**Why esbuild bundles:**
*"pnpm uses symlinks for workspace packages. Electron Forge's dependency walker can't follow these symlinks. esbuild bundles everything into a single file, eliminating the need for node_modules in the packaged app."* (CLAUDE.md verbatim).

**Corpus-first esbuild-bundle-for-Electron-Forge-symlink-workaround documented technique.**

**Tech stack:**

| Layer | Technology |
|---|---|
| Desktop | Electron 39.x |
| UI | React 19, Vite 7 |
| Styling | TailwindCSS, Radix UI |
| State | React hooks (no Redux/Zustand) |
| AI | Vercel AI SDK + 6 native providers + Vercel AI Gateway + Ollama + models.dev catalog |
| IPC | Electron contextBridge |
| Build | TypeScript 5.9, esbuild, Electron Forge |
| Code signing | APPLE_ID + APPLE_PASSWORD + APPLE_TEAM_ID env vars |

**Editor tech:** Tiptap with custom `track-block` extension (atom node for Track Block chips).

**22 core subsystems in `packages/core/src/`:**
account / agent-schedule / agents / application / auth / billing / composio / config / di / knowledge / local-sites / mcp / models / pre_built / runs / search / services / slack / voice / workspace + index

**Notable:** `billing/` subsystem exists — suggests paid tier integration point (but no user-facing billing in current README).

## 4. 4-surface OSS distribution (corpus-first T5)

| Surface | Mechanism | Target | Maturity |
|---|---|---|---|
| **Mac/Windows/Linux binaries** | rowboatlabs.com/downloads + GitHub releases | End users | Primary since pivot |
| **Docker compose** | docker-compose.yml + start.sh | Self-hosters (legacy audience) | Maintained-but-secondary |
| **npm `@rowboatlabs/rowboatx`** | v0.16.0 | Developers integrating CLI | Active (16 minor releases) |
| **PyPI `rowboat`** | v5.0.1 | Developers integrating with API | Active (v5.x mature) |

**Corpus comparison:**
- Most prior T5 wikis have 1-2 distribution surfaces
- OpenHands v30 had 5 (SDK + CLI + GUI + Cloud + Enterprise) — commercial-tier-heavy
- Rowboat v43 has 4 OSS-only surfaces — **corpus-first 4-OSS-only distribution at T5**

**Pattern #2 Distribution Evolution** — within-pattern observation at T5 corpus-first level.

## 5. Legacy SaaS stack preserved in docker-compose.yml

**Active services (profile-controlled):**
- `rowboat` (Next.js dashboard, port 3000) — main entry
- `mongo:latest` — MongoDB persistence
- `redis:latest` — Redis caching + queues
- `qdrant` (custom Dockerfile.qdrant) — **vector DB corpus-first** at T5 OSS stack
- `setup_qdrant` + `delete_qdrant` — lifecycle management
- `rag-worker` — RAG processing (Firecrawl + S3 + Gemini-file-parsing)
- `jobs-worker` — Background jobs
- `docs` (port 8000) — Docs site

**Commented-out services (6):** rowboat_agents + copilot + tools_webhook + simulation_runner + chat_widget + twilio_handler.

**Enterprise-SaaS-stack-fingerprint:**
- Auth0 (multi-tenant authentication with multi-user)
- Composio-triggers-webhook
- Billing API integration
- Gmail + Google Calendar + Firecrawl + Composio + Klavis
- S3 uploads with AWS creds
- Chat widget + Twilio voice

**Corpus context:** 70+ env vars in .env.example reflects enterprise-multi-tenant SaaS complexity. Distinct from personal-single-user Electron app simplicity.

## 6. Rowboat Labs commercial entity

**Identity signals:**

| Signal | Value |
|---|---|
| Homepage | https://www.rowboatlabs.com |
| GitHub org | rowboatlabs |
| Twitter | @rowboatlabshq |
| Discord | discord.gg/wajrgmJQ6b |
| YouTube | 2 videos (demo + intro) |
| Trendshift | repository 13609 |
| **YC batch** | **S24 (Summer 2024)** |
| Domain email | rowboatlabs.com (ramnique@rowboatlabs.com confirmed) |

**7-surface commercial-funnel** ties ruflo v42 for corpus-most-elaborate funnel. Distinct composition:
- Ruflo's: vertical-tier (free OSS / cloud paid / commercial-entity Cognitum.One)
- Rowboat's: horizontal-distribution (multi-channel community + media + accelerator association)

**Pattern #50 Commercial-Funnel Companion Platform** — 6th data point strengthening.

## 7. YC S24 — corpus-first project-level explicit batch acknowledgment

**Badge in README header** (verbatim):
```html
<a href="https://www.ycombinator.com">
  <img src="https://img.shields.io/badge/Y%20Combinator-S24-orange">
</a>
```

**Comparison to prior corpus:**

| Wiki | YC connection | Project-level badge? |
|---|---|---|
| v3 gstack | Garry Tan YC President personal framework | ❌ Personal context, not project signal |
| v25 awesome-design-md | VoltAgent commercial startup | ❌ No batch declared |
| v43 rowboat | **Rowboat Labs YC S24 batch** | ✅ **Corpus-first** |

**Pattern #17 variant 3 observation:** YC-S24-batch-association = observational sub-classification of commercial-startup variant 3. Do NOT register as standalone sub-variant (consolidation-forward discipline). Within-pattern strengthening only.

## 8. Team composition (publicly visible)

**Confirmed Rowboat Labs members:**
1. **Ramnique Singh** (ramnique@rowboatlabs.com) — Python SDK author surfaced via PyPI metadata

**Inferred:**
- YC S24 batches typically 2-4 person founding teams
- Jan 2025 GitHub creation suggests post-YC-batch (W24=Winter 2024 / S24=Summer 2024; S24 runs ~Jun-Aug 2024 → Jan 2025 = post-Demo-Day launch)
- 1.3K forks at 9.7% fork ratio suggests healthy contributor engagement (team + external)

**Bus-factor:** Medium — YC-stage-startup 2-4 person team (more robust than solo-maintainer, less than established commercial entity).

## 9. License + monetization

**License:** Apache-2.0 (LICENSE 11.1KB / 201 lines, unmodified standard Apache-2.0).

**Monetization model (observed):**
- No paid tier currently declared on rowboatlabs.com
- `billing/` subsystem in `apps/x/packages/core/src/` suggests paid tier coming
- Legacy `apps/rowboat/` had Auth0 + billing infrastructure (enterprise SaaS mode)

**Pattern #31 Open-Core observation:** 7th data point strengthening in sub-classification 31c (open-source-with-undeclared-monetization). Sub-classification observational only at v43:
- 31a: open-source-with-paid-cloud-tier-declared (Skyvern v24, OpenHands v30, browser-use v41)
- 31b: open-source-with-paid-enterprise-directory (markitdown v28)
- 31c: open-source-with-undeclared-monetization (rowboat v43, ruflo v42)

## 10. Architecture corpus-firsts

| # | Observation |
|---|---|
| 1 | Product-pivot-in-monorepo (legacy SaaS coexists with new Electron flagship) |
| 2 | Triple-runtime architecture (Electron + CLI server + legacy SaaS + Python SDK) |
| 3 | esbuild-bundle-for-Electron-Forge-symlink-workaround documented technique |
| 4 | 22-subsystem single-core-package architectural decomposition |
| 5 | Qdrant in T5 OSS stack (not unique to rowboat — GitNexus v33 had LadybugDB; crawl4ai v29 indirect — but first Qdrant in T5 compose stack) |
| 6 | 4-surface OSS-only distribution at T5 |
| 7 | 7-surface commercial-funnel at T5 OSS startup |
| 8 | YC S24 batch project-level README badge (first in 43 wikis) |
| 9 | `claude-cowork` repo topic identity signal |
| 10 | `billing/` subsystem in OSS core suggesting paid tier infrastructure |

## 11. Pattern cross-references

- **Pattern #17 variant 3 commercial-startup** — 14th data point (Rowboat Labs YC-S24 + 4-surface distribution + 7-surface funnel)
- **Pattern #31 Open-Core Commercial Entity** — 7th data point (sub-classification 31c undeclared-monetization)
- **Pattern #50 Commercial-Funnel** — 6th data point (7-surface funnel)
- **Pattern #58 Branding-Package Divergence** — 3rd data point watch (product-pivot-in-monorepo observational variant)
- **Pattern #2 Distribution Evolution** — T5 4-surface-OSS-only corpus-first

## 12. Limitations

- Product-pivot mid-life creates code-debt (legacy SaaS preserved but services commented-out)
- Dual-product strategy unclear — is legacy maintained or deprecated?
- No explicit migration path for legacy-SaaS users to new Electron app
- No formal service-level-agreement for legacy Docker-compose deployment
- Team-size small (YC-stage); scaling ambiguous
- No stated roadmap for paid tier launch despite `billing/` subsystem existence

## Cross-references

- **v15 multica** — 1st Electron + T2 managed-agents-platform; contrast with rowboat T5 personal-productivity Electron 2nd
- **v30 OpenHands** — 5-deployment-surface comparable; academic-commercial vs YC-startup archetypal contrast
- **v42 ruflo** — 3-layer commercial-funnel comparable; ruflo EXTREME primitive-count vs rowboat YELLOW
- **v3 gstack** — YC-individual-context vs YC-batch-project-level distinction
