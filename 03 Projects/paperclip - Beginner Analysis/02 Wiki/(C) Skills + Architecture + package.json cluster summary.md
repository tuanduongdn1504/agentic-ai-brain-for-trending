# (C) Skills + Architecture + package.json cluster summary — paperclip

> **Sources:** skills/ folder listing (4 skills) + package.json scripts + pnpm-workspace implicit + root folder structure
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

This cluster covers **the technical substrate** of paperclip: what ships (skills), how it's built (monorepo architecture), what runs (package.json scripts). Combined they reveal engineering disposition distinct from README's product positioning.

## 2. Skills — only 4 (lightest multi-skill T5)

From skills/ folder listing:

| Skill | Likely purpose (inferred) |
|-------|---------------------------|
| `paperclip` | Core skill — basic paperclip operations |
| `paperclip-create-agent` | Onboard new agent into paperclip company |
| `paperclip-create-plugin` | Scaffold plugin for paperclip |
| `para-memory-files` | Memory/state file management (durable memory roadmap item) |

**Total: 4 skills.**

### Interpretation

paperclip deliberately **limits skill count**. Focus is **orchestration**, not skill library. Contrast:
- codymaster v12: 79 skills — "full SaaS team"
- gws v13: 110 skills — Workspace API bridge
- paperclip v14: 4 skills — orchestration control plane

**Design thesis:** skills are for extending paperclip's capabilities (create-agent, create-plugin). The actual agent work is delegated to BYO agents (OpenClaw / Claude Code / Codex / Cursor / Bash / HTTP). paperclip doesn't duplicate skill library; it orchestrates agents that have their own skills.

**Lightweight-orchestrator architecture** is novel in T5 context:
- deer-flow: Skill System with progressive loading (its own skills)
- autoresearch: 1 mega-skill (program.md as agent skill)
- paperclip: 4 meta-skills + BYO agents (their skills)

## 3. Monorepo architecture (from root folders + package.json)

### Workspace structure (pnpm)

Implied `pnpm-workspace.yaml` with packages likely:
- `@paperclipai/server` — Express API + Drizzle + Postgres
- `@paperclipai/ui` — React dashboard
- `@paperclipai/cli` — onboarding + config (invoked as `paperclipai` command)
- `@paperclipai/db` — Drizzle schema + migrations
- `packages/*` — shared utilities + types
- `skills/*` — 4 skills above

### Root folders + roles

| Folder | Role |
|--------|------|
| `.agents/` | Per-company agent configs (AGENTS.md pattern from README) |
| `.claude/` | Claude Code integration (likely instructions) |
| `.github/` | CI + issue templates + PR template |
| `cli/` | CLI package source |
| `doc/` + `docs/` | Dual docs folders (doc = spec-level; docs = user-facing via mintlify) |
| `docker/` | Dockerfile + compose for production |
| `evals/` | LLM evaluation (promptfoo configs) |
| `packages/` | Monorepo shared packages |
| `patches/` | pnpm patches (embedded-postgres 18.1.0-beta.16 patched) |
| `releases/` | Release artifacts |
| `report/` | Telemetry/reporting |
| `scripts/` | Build + release + dev utility scripts |
| `server/` | Server package source |
| `skills/` | 4 skills |
| `tests/` | E2E + release smoke tests |
| `ui/` | UI package source |

### Root files

- `package.json` — monorepo root (name: `paperclip`, private: true, type: module)
- `pnpm-workspace.yaml` — workspace config
- `pnpm-lock.yaml` — locked deps
- `Dockerfile` — production container
- `.env.example` — environment variable template
- `.npmrc` — npm registry config (for package publishing)
- `tsconfig.*.json` — TypeScript configs (likely base + per-package)
- `vitest.config.ts` — test runner config
- `AGENTS.md` — contributor rules
- `CONTRIBUTING.md` — community contribution guide
- `ROADMAP.md` — product trajectory
- `SECURITY.md` — security policy
- `adapter-plugin.md` — adapter refactor notes
- `README.md` + `LICENSE`

## 4. Tech stack detail (from package.json)

### Core dependencies (from package.json context)

- **TypeScript 5.7.3** — strict mode likely
- **Node 20+** (engines constraint)
- **pnpm 9.15.4** (packageManager pinned)
- **esbuild 0.27.3** (bundling)
- **cross-env** (cross-platform env vars)

### Test infrastructure

- **Vitest 3.0.5** — unit + integration tests
- **Playwright 1.58.2** — E2E tests (browser automation)
  - Standard E2E: `tests/e2e/playwright.config.ts`
  - Multi-user authenticated: `tests/e2e/playwright-multiuser-authenticated.config.ts`
  - Release smoke: `tests/release-smoke/playwright.config.ts`
- **promptfoo 0.103.3** — LLM eval framework (NEW IN CORPUS)

### LLM evaluation (first corpus project with this)

```bash
# From package.json scripts:
"evals:smoke": "cd evals/promptfoo && npx promptfoo@0.103.3 eval"
```

promptfoo is a leading open-source LLM eval framework (promptfoo.dev). Having it integrated into paperclip's dev workflow = **empirical discipline** signal.

**Storm Bear corpus precedent:** autoresearch v10 had val_bpb metric; codymaster v12 had SkillsBench +18.6pp; paperclip v14 adds **promptfoo** as third empirical approach.

## 5. Scripts inventory (40+ npm scripts)

Organized by purpose:

### Dev scripts
- `dev` / `dev:watch` / `dev:once` — start dev server (embedded PGlite)
- `dev:list` / `dev:stop` — lifecycle management
- `dev:server` / `dev:ui` — individual package dev
- `preflight:workspace-links` — ensures workspace links before build

### Build scripts
- `build` — all packages
- `typecheck` — strict TS check
- `build:npm` — package for npm publication

### Test scripts
- `test` / `test:run` / `test:watch` — Vitest
- `test:e2e` / `test:e2e:headed` — Playwright
- `test:e2e:multiuser-authenticated` — multi-tenant scenarios
- `test:release-smoke` — pre-release validation
- `evals:smoke` — LLM evaluation

### Database scripts
- `db:generate` — Drizzle schema codegen
- `db:migrate` — run migrations
- `db:backup` — backup via `./scripts/backup-db.sh`

### Release scripts (mature discipline)
- `release` — main release
- `release:canary` / `release:stable` — channel-specific
- `release:github` — GitHub release creation
- `release:rollback` — rollback latest

### Smoke tests (OpenClaw-specific)
- `smoke:openclaw-join` — OpenClaw join mode
- `smoke:openclaw-docker-ui` — OpenClaw docker UI mode
- `smoke:openclaw-sse-standalone` — OpenClaw SSE standalone mode

**3 OpenClaw runtime modes** revealed. Confirms OpenClaw is distinct from paperclip (needs smoke testing against paperclip) and has multiple deployment patterns.

### CLI entry
- `paperclipai`: `node cli/node_modules/tsx/dist/cli.mjs cli/src/index.ts` — CLI invocation

### Meta/observability
- `metrics:paperclip-commits` — self-measurement of commit velocity
- `check:tokens` — forbidden tokens check (security?)
- `secrets:migrate-inline-env` — migration for env-based secrets

## 6. Release discipline

**3-channel release model:**
- **canary** — bleeding edge (like BMAD's `@next`)
- **stable** — production (like BMAD's `@latest`)
- **github** — GitHub release artifact

**Rollback built-in** — `release:rollback` script. Signal of operational maturity.

Parallels:
- BMAD v11: `@next` / `@latest` + weekly cadence
- gws v13: canary + stable + changesets
- paperclip v14: canary + stable + rollback

**Corpus trend:** mature frameworks converge on canary/stable + rollback discipline.

## 7. PGlite + Postgres hybrid

**Dev:** Embedded PGlite (lightweight Postgres-compatible, runs in-process, no external DB install)
**Prod:** External PostgreSQL

**Implementation via pnpm patch:**
```json
"patchedDependencies": {
  "embedded-postgres@18.1.0-beta.16": "patches/embedded-postgres@18.1.0-beta.16.patch"
}
```

paperclip patches a beta version of embedded-postgres — they're on the bleeding edge of the PGlite ecosystem.

**Why this matters:**
- Zero-setup dev — users don't install Postgres separately
- Production keeps standard Postgres (familiar ops)
- Seamless transition via Drizzle ORM

**First corpus project using PGlite.** Contrast:
- BMAD: Markdown files, no DB
- codymaster: SQLite
- gws: no DB (stateless CLI)
- deer-flow: external DB

## 8. Security signals

From package.json + root files:

- `SECURITY.md` — security policy file present
- `check:tokens` script — forbidden-tokens scanning
- `secrets:migrate-inline-env` — secret management utility
- `.env.example` — template for env vars (no secrets committed)
- `.gitleaks.toml` — leak detection (implied from script)
- `deny.toml` — cargo-deny-style policy file (unusual in TS project; maybe custom)

**Security posture is deliberate.** Enterprise-grade for a self-described "community" project.

## 9. Testing discipline

**Test matrix:**
- Unit (Vitest)
- E2E single-user (Playwright)
- E2E multi-user authenticated (Playwright — validates multi-tenant governance)
- Release smoke (Playwright — pre-release canary validation)
- LLM evaluation (promptfoo)
- Smoke tests for OpenClaw adapter (3 modes)

**6 distinct test categories.** Most comprehensive test posture in corpus.

## 10. The infrastructure signals what paperclip really is

**README positioning:** "Open-source orchestration for zero-human companies"

**Infrastructure signals:**
- Express + Drizzle + PostgreSQL = production DB application
- Multi-tenant authenticated tests = enterprise target
- 3-channel release + rollback = mature product ops
- promptfoo evals = empirical quality gate
- Embedded PGlite dev = zero-friction onboarding
- `@paperclipai/` npm namespace = published packages

**Conclusion:** infrastructure is that of a **commercial-grade product**, not a hobbyist open-source project. This reinforces the "community-platform" archetype hypothesis — organizational backing (whether VC / stealth-corp / foundation) is essentially visible through the infrastructure even if not disclosed publicly.

## 11. Cross-references

- [[(C) README summary]] — product positioning
- [[(C) AGENTS + ROADMAP + adapter-plugin cluster summary]] — engineering contract + trajectory
- [[(C) Zero-Human Companies Orchestration + Governance Layer]] (Phase 3 entity) — how invariants are implemented
- [[(C) BYO Agent Adapter System + OpenClaw Standard]] (Phase 3 entity) — adapter layer

## 12. Open questions surfaced

- Exact `@paperclipai/*` package count? (new — Q30)
- PGlite beta patch reason? (new — Q31)
- promptfoo eval coverage — what gets evaluated? (Q10)
- `deny.toml` — Rust-style policy file in TS project; what enforces it? (new — Q32)
- `check:tokens` forbidden tokens inventory? (new — Q33)
- Multi-user authenticated test coverage — what % of flows? (new — Q34)
- OpenClaw 3 runtime modes — which is primary? (Q11)

## 13. Corpus-first observations

- **First PGlite embedded DB** — dev-friendly production-ready pattern
- **First promptfoo integration** — LLM eval as dev-loop component
- **First "deny.toml"** in TS project — policy-as-code signal
- **First "paperclip-commit-metrics" script** — self-measurement of development
- **First 3-mode release channels** — canary/stable/github with rollback
