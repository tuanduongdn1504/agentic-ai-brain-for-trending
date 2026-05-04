# (C) CLAUDE.md + Architecture Summary

> **Sources:**
> - `00 Sources/goclaw/CLAUDE.md` (267 lines, ~15KB) — full read
> - `00 Sources/goclaw/docs/00-architecture-overview.md` (580 lines, ~22KB) — **skim-first** per routine >20KB rule (full read first 150 lines, skim rest)
> - `00 Sources/goclaw/docs/01-agent-loop.md` (792 lines, ~30KB) — **skim-first** (read stages section + skim rest)
>
> **Ingested:** 2026-04-18
> **Routine context:** Source #2 of 3 (Phase 2)

---

## TL;DR

**VI:** Source #2 combine dev conventions + core architecture. Key findings:
1. **Tech stack ambitious:** Go 1.26 + PG 18 + Wails desktop + React 19 + 20+ LLM providers (bao gồm Claude CLI/Codex/ACP)
2. **Agent Loop V3:** Pipeline-based 8-stage (context→history→prompt→think→act→observe→memory→summarize), pluggable, feature-flagged từ V2 monolithic
3. **Plan Verification Rules:** 17 disciplined rules cho multi-phase planning (mirror Superpowers's eval discipline but more tactical)
4. **i18n first-class:** Vietnamese + Chinese + English catalogs, locale propagated via context

**EN:** Combined dev conventions + core architecture. Ambitious tech stack (Go+PG+Wails+React+20 providers), V3 pipeline agent loop, 17 plan verification rules, first-class i18n (en/vi/zh).

---

## Part 1: Dev conventions (CLAUDE.md)

### Language policy (distinctive)

> "Always respond in the same language as the user's prompt. If the user writes in Vietnamese, respond in Vietnamese. If in English, respond in English."

→ **First-class bilingual agent behavior.** Match audience = Vietnamese-speaking devs/users.

### Tech stack overview

**Backend:** Go 1.26, Cobra CLI, gorilla/websocket, pgx/v5 (no ORM), golang-migrate, go-rod/rod (browser), telego (Telegram)

**Web UI:** React 19, Vite 6, TypeScript, Tailwind CSS 4, Radix UI, Zustand, React Router 7. `ui/web/`. **pnpm required.**

**Desktop UI:** React 19, Vite 6, TypeScript, Tailwind CSS 4, Zustand, Framer Motion. `ui/desktop/frontend/`. **pnpm.**

**Desktop App:** Wails v2 (`//go:build sqliteonly`). Embeds gateway + React frontend in single binary.

**Database:** PostgreSQL 18 với pgvector (standard). SQLite via `modernc.org/sqlite` (desktop/lite). Raw SQL với `$1, $2` (PG) or `?` (SQLite). Nullable: `*string`, `*time.Time`.

→ **Ambitious but cohesive stack.** Single binary output from complex multi-language codebase.

### Project structure (key modules)

```
cmd/                          CLI commands, gateway startup, onboard wizard
internal/
├── agent/                    Agent loop (think→act→observe)
├── pipeline/                 8-stage V3 pipeline
├── providers/                20+ LLM providers + ACP
├── channels/                 7 messaging channels
├── store/                    Dual-DB (pg/ + sqlitestore/)
├── vault/                    Knowledge Vault (wikilinks + hybrid search + FS sync)
├── skills/                   SKILL.md loader + BM25
├── memory/                   pgvector hybrid search
├── consolidation/            Memory consolidation workers (episodic, semantic, dreaming)
├── eventbus/                 DomainEventBus (typed events, worker pool, dedup)
├── orchestration/            BatchQueue[T] generic
├── scheduler/                Lane-based (main/subagent/cron/team)
├── permissions/              RBAC
├── edition/                  Edition system (Lite vs Standard)
├── i18n/                     en/vi/zh catalogs
└── workspace/                WorkspaceContext resolver (6 scenarios)
```

→ **Well-organized layering.** Each concern isolated. Reusable patterns everywhere.

### Key patterns (11 distinctive)

1. **Store layer via Dialect pattern** — interface-based, shared helpers, dual-DB (PG + SQLite)
2. **Agent identity dual-pattern** — UUID for DB/FK/events, agent_key for logs/paths/UI
3. **Context files dual-level** — `agent_context_files` (agent-level) + `user_context_files` (per-user)
4. **Provider adapter + ModelRegistry** — pluggable, forward-compat resolver
5. **8-stage pipeline với callbacks** — always-on execution, pluggable stages
6. **DomainEventBus** — typed events, worker pool, dedup, retry
7. **3-tier memory progressive loading** — L0 auto-inject, L1/L2 on-demand
8. **Context propagation via WithX** — `store.WithAgentID(ctx)`, etc.
9. **Request middleware composable** — cache/tier/guards, zero-alloc hot path
10. **Self-evolution 3-progressive-stage** — metrics → suggestions → guardrailed apply/rollback
11. **Orchestration delegate tool** — inter-agent delegation, 3 modes, token-aware

### Running commands

```bash
go build -o goclaw . && ./goclaw onboard && source .env.local && ./goclaw
./goclaw migrate up

# Integration tests (requires pgvector pg18 on port 5433)
docker run -d --name pgtest -p 5433:5432 -e POSTGRES_PASSWORD=test -e POSTGRES_DB=goclaw_test pgvector/pgvector:pg18
TEST_DATABASE_URL="postgres://postgres:test@localhost:5433/goclaw_test?sslmode=disable" \
  go test -v -tags integration ./tests/integration/

# Layered tests
make test-invariants  # P0 - tenant isolation (blocking)
make test-contracts   # P1 - API schemas
make test-scenarios   # P2 - user journeys
make test-critical    # P0 + P1 (pre-merge)

# Desktop
cd ui/desktop && wails dev -tags sqliteonly
make desktop-build VERSION=0.1.0
make desktop-dmg VERSION=0.1.0
```

→ **Layered test tiers** (P0/P1/P2) match enterprise CI patterns.

### Plan Verification Rules (DISTINCTIVE discipline)

CLAUDE.md has 17 explicit rules cho multi-phase plan verification. Similar to Superpowers's 11 Rationalizations table but **tactical** (how to verify claims) vs philosophical (how to recognize anti-patterns).

**Key rules:**
1. Verify factual claims against code (re-grep/re-count every number, path, endpoint)
2. Trace semantics, not just cite lines (WHEN/WHY fields mutate)
3. No fabricated identifiers — every symbol must cite `file:line`
4. Struct scope audit before adding state (lifetime before field)
5. Gate-premise test math (list all early-returns before asserting independence)
6. Port = config-shape match (faithful port = match upstream config shape or flag divergence)
7. Verify external API endpoints via `docs-seeker`
8. Grep delete scope DEEP — `grep -rn '<symbol>' .` whole repo
9. Signature-change callers enumeration
10. Alias/shim coverage
11. Scout desktop and web separately (different structure, i18n)
12. Re-scout on scope change
13. Cross-phase gates explicit
14. Zero-coverage characterization test = blocker step
15. i18n keys ordering (add key + 3 catalogs BEFORE handler code)
16. Context key style convention check
17. Verify pass MANDATORY after rewrite

**Red-team practice:** After planner completes, run `code-reviewer`/`brainstormer` in audit mode.

**Pattern to avoid:** user asks → planner writes → report "done"
**Safer pattern:** user asks → scout → planner writes → audit-verify → report

→ **Match Superpowers's 2-stage review + gstack's blame-with-receipts.** Convergent discipline across 3 most-opinionated frameworks.

### Post-implementation checklist

```bash
go fix ./...                        # Apply Go version upgrades
go build ./...                      # PG build
go build -tags sqliteonly ./...     # Desktop build
go vet ./...                        # Static analysis
go test -race ./tests/integration/  # Race detector
```

**Plus 8 Go conventions + dual-DB migrations + i18n strings + SQL safety + DB query reuse + solution design + tenant-scope guards + skip load/stress tests.**

→ **Extensive.** Goes beyond most CLAUDE.md files. Match ambition of tech stack.

### Mobile UI/UX rules (BONUS discipline)

13 explicit mobile UX rules:
- `h-dvh` not `h-screen`
- 16px input font-size (iOS zoom prevention)
- Safe areas (`safe-top`, `safe-bottom`, etc.)
- 44px touch targets
- Virtual keyboard handling (`useVirtualKeyboard()` hook)
- Portal dropdowns `pointer-events-auto` for Radix Dialog compat
- Route params as source of truth (no duplicate state)

→ **Mobile-first design seriousness.** None of 3 siblings have equivalent detail.

---

## Part 2: Architecture overview (00-architecture-overview.md)

### System diagram (simplified)

```
Clients (WS / HTTP / 7 channels)
   ↓
Gateway (WS server, HTTP API, method router, rate limiter, RBAC)
   ↓
Channel Manager + Pairing Service
   ↓
Core Engine (Message Bus + Scheduler-4-Lanes + Agent Router + Agent Loop + Hook Dispatcher)
   ↓
LLM Providers (Anthropic / OpenAI-compat / ACP) + Tool Registry (30+ tools) + Store Layer (10+ stores)
```

→ **Multi-protocol, multi-tenant, multi-provider.** Layered cleanly.

### Module map (50+ modules)

Full architectural breakdown trong CLAUDE.md summary part 1 above. Key additions từ doc:

- `internal/hooks/` — Agent lifecycle hooks (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStart/Stop) với CommandHandler + HTTPHandler + regex/CEL matchers + audit logging + edition gating + cost safeguards
- `internal/subagent/` — lifecycle: spawn, roster, task persistence, announce queue (producer-consumer), auto-retry, per-edition rate limiting
- `internal/hooks/handlers/` — CommandHandler (Lite-only), HTTPHandler (SSRF-hardened, retry-once on 5xx, encrypted auth headers)
- `internal/tracing/otelexport/` — Optional OpenTelemetry OTLP exporter (opt-in via build tags)
- `internal/channels/whatsapp/` — Native WhatsApp via whatsmeow (v3)

### Consolidation pipeline (memory worker architecture)

Async via worker pools với dedup + retry:
1. **Episodic** — recent facts → session summaries
2. **Semantic** — embeddings → knowledge graph
3. **Dreaming** — synthesis → promote to semantic

Event-driven via DomainEventBus.

→ **Sophisticated memory architecture.** Inspired by human memory consolidation during sleep ("dreaming" stage).

---

## Part 3: Agent Loop V3 (01-agent-loop.md)

### Think → Act → Observe cycle

Each agent owns a `Loop` instance (provider + model + tools + workspace + agent type).

**Flow:**
1. `RunRequest` enters loop
2. LLM thinks
3. Optionally calls tools
4. Observes results
5. Repeats up to **20 iterations** or until final text response
6. Exits as `RunResult`

### V3 Pipeline architecture

Feature-flagged via `pipeline_enabled`. `runViaPipeline()` orchestrates 8-stage pipeline:

```
Setup (runs once)
└─ ContextStage — inject context, workspace, per-user files

Iteration Loop (max 20)
├─ ThinkStage — build system prompt, filter tools, call LLM
├─ PruneStage — soft/hard trim, memory flush
├─ ToolStage — execute tool calls (parallel)
├─ ObserveStage — process tool results
└─ CheckpointStage — max iter / cancellation check

Finalize (runs once, bg context if cancelled)
└─ FinalizeStage — 7-step sanitization, flush, emit event
```

**Discrepancy note:** Marketing says "8 stages" (context→history→prompt→think→act→observe→memory→summarize) but implementation = 7 Stage classes. Mapping:
- Context = ContextStage
- History + Prompt = (within ThinkStage)
- Think = ThinkStage
- Act = ToolStage
- Observe = ObserveStage
- Memory = PruneStage (triggers memory flush)
- Summarize = FinalizeStage

### Stage Details highlights

**ThinkStage** most complex:
- Resolve workspace + context files dynamically
- Build system prompt (**15+ sections**)
- Inject conversation summary if exists
- Run history pipeline (`limitHistoryTurns → sanitizeHistory`)
- Filter tools through PolicyEngine (RBAC)
- Call LLM, record span with token counts
- Emit `chunk` events (streaming) or single response

**PruneStage** (opt-in via `contextPruning.mode: "cache-ttl"`):
- Estimate token ratio vs context window
- **≥25%** → soft trim (keep first/last 3000 chars)
- **≥50%** → hard clear (placeholder)
- Run `sanitizeHistory` to fix broken tool_use/tool_result pairs
- Trigger memory flush if compaction threshold exceeded

**ToolStage:**
- Single tool: sequential (no goroutine overhead)
- Multiple tools: parallel via goroutines, sort results by index
- Emit `tool.call` before + `tool.result` after
- Record tool span

**FinalizeStage:**
- 7-step output sanitization pipeline
- Flush buffered messages atomically
- Emit `run.completed` or `run.failed` event

---

## Distinctive patterns

### Pattern 1: Dialect + dual-DB

Interface `Dialect` + helpers (`NilStr`, `BuildMapUpdate`, `BuildScopeClause`) enable same code work on PostgreSQL AND SQLite.

→ **Reusable pattern** cho any tool needing dual-backend.

### Pattern 2: Agent identity dual-pattern

UUID for DB/FK/events; agent_key for logs/paths/UI.

> "See `docs/agent-identity-conventions.md`"

→ **Anti-pattern it avoids:** using human-readable ID in foreign keys (rename breaks FKs). Using UUID in logs (opaque).

### Pattern 3: Context propagation

`store.WithAgentID(ctx)`, `store.WithUserID(ctx)`, `store.WithAgentType(ctx)`, `store.WithLocale(ctx)`, `store.WithTenantID(ctx)`.

→ Match Go idiomatic context propagation. Clean tenant/locale boundaries.

### Pattern 4: 17 Plan Verification Rules

See Part 1 CLAUDE.md summary. Convergent discipline với Superpowers + gstack.

### Pattern 5: Feature-flag V2/V3 migration

V2 monolithic legacy + V3 pipeline new path. Both behave same externally. Internal migration via flag.

→ **Classic rewrite-without-disruption pattern.** 

### Pattern 6: 4-lane scheduler

Main / subagent / cron / team lanes. Per-session serialization + per-edition rate limits.

### Pattern 7: Tenant-scope guards discipline

> "`RoleAdmin` is not a tenant check. Writes to global tables must gate with `http.requireMasterScope`. Writes to tenant-scoped tables must gate with `http.requireTenantAdmin` + SQL `WHERE tenant_id = $N`."

→ **Multi-tenant security hygiene** explicit. Most apps muddle this.

---

## Open questions resolved

- ✅ Q1: 8-stage pipeline vs Superpowers 7-stage vs gstack Sprint Pipeline — **Different abstraction levels.** goclaw's = internal agent execution loop (low-level); Superpowers/gstack = developer workflow (high-level). Orthogonal.
- ✅ Q6: Self-evolution guardrails — can refine communication style + CAPABILITIES.md, **cannot change identity, name, or core purpose**. 3 progressive stages (metrics → suggestions → apply/rollback).

## Open questions raised

- ⏸ ACP provider integration pattern — can goclaw spawn Claude Code sessions với gstack skills? If yes, **major integration opportunity**
- ⏸ Agent hooks system — compare với ECC hooks. Overlap?
- ⏸ DomainEventBus — reusable as standalone pattern cho Storm Bear vault event tracking?
- ⏸ Mobile UI/UX rules — 13 rules valuable cho Storm Bear nếu build mobile companion ever

---

## Cross-references

- [[(C) README summary]]
- [[(C) Key Docs deep dive]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Philosophy and Contribution Culture summary.md` — voice protection + discipline convergence
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) CLAUDE.md summary.md` — CLAUDE.md as dev culture artifact comparison

## Citations

- `CLAUDE.md` (full, 267 lines)
- `docs/00-architecture-overview.md` lines 1-150 (component diagram + module map)
- `docs/01-agent-loop.md` lines 1-100 (V3 pipeline stages)
- Plan Verification Rules: CLAUDE.md lines 125-165 (17 numbered rules)
- Mobile UI rules: CLAUDE.md lines 237-265 (13 numbered rules)
