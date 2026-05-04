# (C) Cluster 2: Architecture + Monorepo + Temporal + Agents

> **Sources:** CLAUDE.md (15.4 KB) + package.json + pnpm-workspace.yaml + turbo.json + `apps/` listing + `apps/cli/` + `apps/worker/` + `apps/worker/prompts/` (13 prompt files) + `apps/worker/src/services/` (11 services)
> **Cluster role:** Contributor-facing + technical architecture documentation
> **Status:** ✅ Complete

---

## 1. Monorepo structure (pnpm-workspaces + Turborepo)

```
shannon/
├── apps/
│   ├── cli/      — @keygraph/shannon (published to npm, bundled tsdown)
│   └── worker/   — @shannon/worker (private, Temporal worker + pipeline logic)
├── Dockerfile           — 2-stage build (builder + Chainguard Wolfi runtime)
├── docker-compose.yml   — Infra only (Temporal; port 7233/8233)
├── entrypoint.sh
├── shannon              — Node entry point (#!/usr/bin/env node)
├── pnpm-lock.yaml       — 80.7 KB
├── pnpm-workspace.yaml  — catalog pins @anthropic-ai/claude-agent-sdk ^0.2.38
├── turbo.json           — 3 tasks (build / check / clean)
├── biome.json           — lint + format
├── tsconfig.base.json   — shared compiler options
├── tsconfig.json
└── package.json         — v0.0.0 root (private)
```

**Tooling:** pnpm@10.33.0 + Turborepo 2.5 + Biome 2 + TypeScript 5.9 + @types/node 25.

## 2. Dual CLI architecture (npx vs Local)

**Auto-detection** via `SHANNON_LOCAL=1` env var set by `./shannon` entry point (`apps/cli/src/mode.ts`). Otherwise npx mode.

| Aspect | **npx** (`npx @keygraph/shannon`) | **Local** (`./shannon`) |
|--------|-----------------------------------|--------------------------|
| Install | Zero-install via npm | Clone the repo |
| Image | Pulled from Docker Hub (`keygraph/shannon:latest`) | Built locally (`shannon-worker`) |
| State | `~/.shannon/` | Project directory |
| Credentials | `~/.shannon/config.toml` (via `shn setup`) or env vars | `./.env` |
| Config | `~/.shannon/config.toml` (via `shn setup`) | N/A |
| Prompts | Bundled in Docker image | Mounted from `./apps/worker/prompts/` (live-editable) |

**Corpus-first dual-mode TOML-vs-dotenv split** at T5. TOML via `smol-toml` parser (`apps/cli/src/config/resolver.ts`).

## 3. CLI package (`apps/cli/`)

Published as `@keygraph/shannon` on npm. **Contains only Docker orchestration logic** — no Temporal SDK, no business logic, no prompts. Bundled with tsdown for single-file ESM output.

Key files:
- `apps/cli/src/index.ts` — CLI dispatcher (setup / start / stop / logs / workspaces / status / build / uninstall / info)
- `apps/cli/src/mode.ts` — auto-detection
- `apps/cli/src/docker.ts` — compose lifecycle + image pull/build + ephemeral `docker run` worker spawning
- `apps/cli/src/home.ts` — state directory mgmt
- `apps/cli/src/env.ts` — .env loading + TOML fallback + credential validation + env flag building
- `apps/cli/src/config/resolver.ts` — cascading config (env vars → `~/.shannon/config.toml`)
- `apps/cli/src/config/writer.ts` — TOML serialization + secure file persistence (0o600 permissions)
- `apps/cli/src/commands/setup.ts` — Interactive TUI wizard via `@clack/prompts` for provider credential setup (npx only)
- `apps/cli/src/paths.ts` — repo/config path resolution (bare name → `./repos/<name>`, or absolute/relative)
- `apps/cli/infra/compose.yml` — bundled Temporal compose for npx mode

## 4. Worker package (`apps/worker/`)

**Private**; Temporal worker + pipeline logic + prompts + configs.

```
apps/worker/
├── configs/
│   ├── config-schema.json    — JSON Schema for YAML config validation
│   └── example-config.yaml
├── prompts/                   — 13 prompt files (~260 KB total)
│   ├── pipeline-testing/
│   ├── shared/                — 5 partial templates
│   │   ├── _exploit-scope.txt
│   │   ├── _rules.txt
│   │   ├── _target.txt
│   │   ├── _vuln-scope.txt
│   │   └── login-instructions.txt
│   ├── exploit-auth.txt       — 24.7 KB
│   ├── exploit-authz.txt      — 25.8 KB
│   ├── exploit-injection.txt  — 26.4 KB
│   ├── exploit-ssrf.txt       — 27.8 KB
│   ├── exploit-xss.txt        — 24.2 KB
│   ├── pre-recon-code.txt     — 27.3 KB
│   ├── recon.txt              — 27.3 KB
│   ├── report-executive.txt   — 7.1 KB
│   ├── vuln-auth.txt          — 18.2 KB
│   ├── vuln-authz.txt         — 20.1 KB
│   ├── vuln-injection.txt     — 24.4 KB
│   ├── vuln-ssrf.txt          — 19.9 KB
│   └── vuln-xss.txt           — 20.9 KB
├── src/
│   ├── ai/                    — Claude Agent SDK integration (claude-executor.ts with retry)
│   ├── audit/                 — crash-safe append-only logging (workflow-logger + log-stream)
│   ├── interfaces/
│   ├── scripts/               — save-deliverable CLI
│   ├── services/              — business logic (11 files)
│   ├── temporal/              — workflow + activity + worker entry
│   ├── types/                 — Result<T,E>, ErrorCode, AgentName, ActivityLogger
│   ├── utils/                 — file I/O + formatting + concurrency
│   ├── config-parser.ts       — 19.2 KB YAML + JSON Schema validation
│   ├── paths.ts               — centralized path constants (PROMPTS_DIR / CONFIGS_DIR / WORKSPACES_DIR)
│   ├── progress-indicator.ts  — 1.3 KB TUI
│   └── session-manager.ts     — 7.4 KB AGENTS record (authoritative agent definitions)
```

## 5. Services (11 business-logic files)

`apps/worker/src/services/` — Temporal-agnostic business logic layer:

1. **agent-execution.ts** (10.4 KB) — `AgentExecutionService.execute` with steps 1-9; lifecycle management via AGENTS registry
2. **config-loader.ts** (3.2 KB) — YAML + schema loading
3. **container.ts** (6.1 KB) — DI container per-workflow; excludes AuditSession (parallel safety)
4. **error-handling.ts** (8.3 KB) — `ErrorCode` enum + `Result<T,E>` + retry logic (3 attempts/agent)
5. **exploitation-checker.ts** (2.4 KB)
6. **git-manager.ts** (9.2 KB) — per-agent git checkpoints; resumable state
7. **index.ts** (1.1 KB) — barrel export
8. **preflight.ts** (15.2 KB) — pre-scan validation
9. **prompt-manager.ts** (10.5 KB) — variable substitution `{{TARGET_URL}}`, `{{CONFIG_CONTEXT}}`, `{{LOGIN_INSTRUCTIONS}}`
10. **queue-validation.ts** (9.4 KB) — exploitation queue (structured JSON) validation
11. **reporting.ts** (5.4 KB) — final report synthesis

**Corpus-first:** Services-as-boundary architecture with explicit `Result<T,E>` + `ActivityLogger` injection for Temporal-agnostic testing. Similar rigor level to crawl4ai v29 / markitdown v28 but with explicit CQRS-adjacent service layering.

## 6. Temporal orchestration

**Durable workflow orchestration with crash recovery, queryable progress, intelligent retry, and parallel execution (5 concurrent agents in vuln/exploit phases).**

Key files:
- `apps/worker/src/temporal/workflows.ts` — Main workflow (`pentestPipelineWorkflow`)
- `apps/worker/src/temporal/activities.ts` — Thin wrappers: heartbeat loop + error classification + container lifecycle (business logic delegated to services)
- `apps/worker/src/temporal/activity-logger.ts` — `TemporalActivityLogger` implementation
- `apps/worker/src/temporal/summary-mapper.ts` — `PipelineSummary` → `WorkflowSummary`
- `apps/worker/src/temporal/worker.ts` — combined worker + client entry; **per-invocation task queue**, submits workflow, waits for result
- `apps/worker/src/temporal/shared.ts` — types + interfaces + query definitions

**Corpus-first:** Temporal.io durability as T5 core orchestration primitive. Prior T5s used LangGraph (deer-flow) / raw PyTorch (autoresearch) / custom (paperclip) / Playwright-direct (Skyvern, browser-use) / custom pipeline (OpenHands) / academic custom (DeepTutor) / custom (rowboat). Shannon is first Temporal-backed T5.

## 7. 13 specialized agents (`apps/worker/src/session-manager.ts`)

Per SHANNON-PRO.md and CLAUDE.md, Shannon uses 13 specialized agents across 5 phases:

| Phase | Agent Count | Agents (mapped from prompt files) |
|-------|-------------|-----------------------------------|
| 1. Pre-Reconnaissance | 1 | pre-recon-code |
| 2. Reconnaissance | 1 | recon |
| 3. Vulnerability Analysis | 5 (parallel) | vuln-injection / vuln-xss / vuln-ssrf / vuln-auth / vuln-authz |
| 4. Exploitation | 5 (parallel, conditional) | exploit-injection / exploit-xss / exploit-ssrf / exploit-auth / exploit-authz |
| 5. Reporting | 1 | report-executive |
| **Total** | **13** | 13 prompt files |

**Execution model (from SHANNON-PRO.md):**
> *"Phases 1 and 2 (reconnaissance) run sequentially. Phases 3 and 4 (vulnerability analysis and exploitation) run as pipelined parallel: each vulnerability/exploit pair is independent. When a vulnerability agent finishes for a given attack domain, the corresponding exploit agent starts immediately, even if other vulnerability agents are still running. Phase 5 (reporting) runs after all exploitation is complete."*

**Agent methodology matrix (5 vuln-analysis agents — from SHANNON-PRO.md):**

| Agent | Approach | What It Analyzes |
|-------|----------|------------------|
| **Injection** | Source → Sink taint | User input reaching SQL / command / file / template / deserialization sinks |
| **XSS** | Sink → Source taint | HTML rendering contexts (innerHTML / document.write / event handlers / eval) |
| **SSRF** | Sink → Source taint | HTTP clients / raw sockets / URL openers / headless browsers |
| **Auth** | Guard validation | Missing controls: rate-limiting / session / token-entropy / password-hashing / HSTS / SSO/OAuth |
| **Authz** | Guard validation | Missing authz checks before side-effects: horizontal (ownership) / vertical (role) / context/workflow |

## 8. Claude Agent SDK integration

- Package: `@anthropic-ai/claude-agent-sdk` ^0.2.38 (pinned via pnpm catalog)
- Config: `maxTurns: 10_000` + `bypassPermissions` mode (per CLAUDE.md: *"SDK-First — Claude Agent SDK handles autonomous analysis"*)
- Browser automation: `playwright-cli` with session isolation (`-s=<session>`)
- TOTP generation: `generate-totp` CLI tool
- Login flow template: `apps/worker/prompts/shared/login-instructions.txt` (supports form / SSO / API / basic)

## 9. Docker architecture

- **Infra** (`docker-compose.yml`): Temporal (port 7233/8233) on network `shannon-net`
- **Dockerfile** (5.4 KB): 2-stage build — (1) builder + (2) Chainguard Wolfi runtime (minimal hardened base); uses pnpm; entrypoint `CMD ["node", "apps/worker/dist/temporal/worker.js"]`
- **Ephemeral workers** via `docker run --rm` — one per scan, each with unique task queue and isolated volume mounts
- **Target repo mounted as READ-ONLY** inside worker container (protects against accidental modifications during analysis)
- Host gateway handling via `--add-host` flag (no separate `docker-compose.docker.yml`)

**Corpus-first security-isolation architecture:** Read-only mount + ephemeral container + per-scan Temporal task queue = stricter isolation than Skyvern (persistent worker) / browser-use (single container) / OpenHands (mutable sandbox).

## 10. Audit + Deliverables system

**Crash-safe append-only logging** in `workspaces/{hostname}_{sessionId}/`:

```
workspaces/{hostname}_{sessionId}/
├── session.json              — metrics + session data
├── workflow.log              — human-readable workflow log
├── agents/                   — per-agent execution logs
├── prompts/                  — prompt snapshots for reproducibility
└── deliverables/
    └── comprehensive_security_assessment_report.md
```

**Components:**
- `WorkflowLogger` (audit/workflow-logger.ts) — unified human-readable per-workflow logs
- `LogStream` (audit/log-stream.ts) — shared stream primitive
- `save-deliverable` CLI (scripts/save-deliverable.ts)
- **Git checkpoints** per-agent → resume from clean validated state
- **Prompt snapshots** → reproducibility (corpus-first prompt-versioning discipline)

## 11. Key design patterns (from CLAUDE.md)

- **Configuration-Driven** — YAML configs with JSON Schema validation
- **Progressive Analysis** — each phase builds on previous results
- **SDK-First** — Claude Agent SDK handles autonomous analysis
- **Modular Error Handling** — `ErrorCode` enum, `Result<T,E>` for explicit error propagation, automatic retry (3 attempts/agent)
- **Services Boundary** — activities are thin Temporal wrappers; `services/` owns business logic; no Temporal imports in services
- **DI Container** — per-workflow `container.ts`; excludes AuditSession (parallel safety)
- **Ephemeral Workers** — each scan runs in own `docker run --rm` container with per-invocation task queue

## 12. Code style (from CLAUDE.md §Code Style Guidelines)

**Biome handles formatting and linting** (single quotes, semicolons, trailing commas, 2-space indent, 120 char width).

**Principles:**
- *"Optimize for readability, not line count — three clear lines beat one dense expression."*
- Use descriptive names
- Prefer explicit logic over clever one-liners
- Early returns + guard clauses instead of deep nesting
- **"Never use nested ternary operators"** — use if/else or switch
- Extract complex conditions into well-named boolean variables

**TypeScript conventions:**
- `function` keyword for top-level (not arrow functions)
- Explicit return types on exported/top-level functions
- `readonly` for data that shouldn't be mutated
- `exactOptionalPropertyTypes` enabled — use spread for optional props, not direct `undefined`

**Avoid:** combining concerns / dense callback chains / sacrificing readability for DRY / one-off abstractions / **backwards-compatibility shims** (*"delete the old code, don't preserve it"*)

**Comment patterns:**
- `/** JSDoc */` for file headers and exported functions/interfaces
- `// N. Description` — numbered sequential steps when 3+ distinct phases
- `// === Section ===` — high-level dividers between function groups (not for sequential steps)
- `// NOTE:` / `// WARNING:` / `// IMPORTANT:` — gotchas
- **Never:** obvious comments / conversation references / history ("moved from X")

**Corpus-first:** Explicit "no backwards-compat shims" + "timeless comments" discipline at T5 commercial-startup scope.

## 13. Package installation policy

Per CLAUDE.md: *"Package managers are configured with a minimum release age (7 days). Requires pnpm >= 10.16.0. If `pnpm install` fails due to a package being too new, do not attempt to bypass it — report the blocked package to the user and stop."*

**Corpus-first:** Explicit supply-chain-hardening via minimum-release-age policy. Echoes Pattern #66 supply-chain observation-track but as preventive architectural discipline.

## 14. Adding a new agent (workflow, from CLAUDE.md)

4-step pattern:
1. Define agent in `apps/worker/src/session-manager.ts` (add to `AGENTS` record); types in `types/agents.ts`
2. Create prompt template in `apps/worker/prompts/` (e.g., `vuln-newtype.txt`)
3. Two-layer pattern: thin activity wrapper in `temporal/activities.ts` (heartbeat + error classification); `AgentExecutionService` handles lifecycle automatically via `AGENTS` registry
4. Register activity in `temporal/workflows.ts` within appropriate phase

**Corpus-first:** Explicit activity/service separation-of-concerns documented at agent-addition level — Temporal-idiomatic + unit-testable.

## 15. Corpus-firsts in Cluster 2

1. TypeScript pnpm-workspaces monorepo at T5 AI-pentester scope
2. Temporal.io as T5 core orchestration primitive
3. 13 specialized agents + 13 prompt files matching 1:1
4. Dual CLI mode (npx `.env` vs local TOML) with auto-detection
5. Chainguard Wolfi runtime in Dockerfile (hardened minimal base)
6. Read-only target repo mount + ephemeral container + per-scan Temporal task queue isolation
7. Services-as-boundary architecture with `Result<T,E>` + `ActivityLogger` DI
8. Per-agent git-checkpoint resume mechanism
9. Prompt snapshots for reproducibility (prompt-versioning discipline)
10. Minimum-release-age package policy (supply-chain preventive discipline)
11. Pipelined-parallel execution (exploit starts when vuln completes, not after all vuln complete)
12. `maxTurns: 10_000` + `bypassPermissions` Claude Agent SDK configuration
13. `generate-totp` CLI tool for automatic 2FA handling
14. `@clack/prompts` TUI setup wizard for credential configuration
15. tsdown bundler for single-file ESM CLI distribution

## Cross-wiki links

- Temporal precedents at T5: none (corpus-first for T5 Temporal adoption)
- Claude Agent SDK peers: [[OpenHands]] v30 uses multiple-LLM-provider abstraction; Shannon uses Claude SDK directly with `bypassPermissions`
- Monorepo T5 peers: [[pi-mono]] v36 (7-package solo-monorepo T1 — different scope); [[ruflo]] v42 (2-package T1+T2 dual)
- Playwright peers: [[Skyvern]] v24 / [[browser-use]] v41 (both use Playwright at T5; Shannon uses `playwright-cli` differently as pentesting tool not primary automation)
- Services-layer discipline peers: [[crawl4ai]] v29 / [[markitdown]] v28 / [[browser-use]] v41 (all have clear abstraction layers)
