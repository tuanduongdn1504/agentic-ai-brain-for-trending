# (C) CLAUDE + AGENTS + CONTRIBUTING cluster summary — multica

> **Sources:** CLAUDE.md (21,846 B — largest in corpus) + AGENTS.md (1,892 B pointer-with-content) + CONTRIBUTING.md (13,706 B — not fetched verbatim, structure inferred) + HANDOFF_ARCHITECTURE_AUDIT.md (18,208 B — not fetched)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster — heaviest agent-documentation root in corpus

multica has **7 substantial root-level .md docs** totaling **~90KB**:

| Doc | Size | Role |
|-----|------|------|
| CLAUDE.md | 21,846 B | **Largest in corpus** — Claude Code contributor guide |
| HANDOFF_ARCHITECTURE_AUDIT.md | 18,208 B | Architecture audit (not fetched) |
| CLI_AND_DAEMON.md | 14,507 B | CLI + Agent Daemon architecture |
| CONTRIBUTING.md | 13,706 B | Community contribution guide |
| README.md | 9,045 B | User-facing positioning |
| SELF_HOSTING_ADVANCED.md | 8,502 B | Advanced self-hosting |
| README.zh-CN.md | 8,315 B | Chinese translation |
| SELF_HOSTING.md | 7,129 B | Self-hosting guide |
| CLI_INSTALL.md | 5,664 B | CLI installer docs |
| SELF_HOSTING_AI.md | 2,027 B | AI self-hosting |
| AGENTS.md | 1,892 B | Pointer with content |

**Combined: 110KB+ of docs at root.** Heaviest doc-per-project in corpus.

**Comparison:**
- gws v13: 3 agent-facing docs (CLAUDE 110B + AGENTS 11KB + CONTEXT 2.6KB) = ~14KB
- paperclip v14: AGENTS.md + README + ROADMAP + adapter-plugin = modest docs
- BMAD v11: README 6KB + README_VN 7.5KB + CHANGELOG 94KB = changelog-heavy but docs-lighter
- **multica v15: 7 docs of 5-22KB each = documentation-heaviest in corpus**

→ Cluster required to handle volume efficiently.

## 2. CLAUDE.md — 21,846 B = architecture + contributor bible

### Role framing (verbatim)

> *"You are a Claude agent assisting with Multica, an AI-native task management platform (similar to Linear but with agents as first-class citizens). You should understand the full architecture and contribute consistently across the codebase while respecting strict architectural boundaries."*

**Observations:**
- Claude addressed in 2nd person
- "AI-native task management" = Linear-analog framing
- "Strict architectural boundaries" = non-negotiable constraints

### Architecture summary (from CLAUDE.md)

```
server/              — Go backend (Chi + sqlc + gorilla/websocket)
apps/web/            — Next.js frontend
apps/desktop/        — Electron app (electron-vite)
packages/core/       — Headless business logic (zero React DOM)
packages/ui/         — Atomic UI components (zero business logic)
packages/views/      — Shared business pages (no framework routing)
packages/tsconfig/   — Shared TypeScript config
```

**Key principle:** *"Internal packages export raw .ts/.tsx files (no pre-compilation). The consuming app's bundler compiles them directly."*

→ No compile step between packages — faster dev iteration.

### State management rules (HARD)

**Hard rule:** *"Never duplicate server data into Zustand. If it came from the API, it belongs in the Query cache."*

| Layer | Owns |
|-------|------|
| **TanStack Query** | All server state (issues, users, workspaces) |
| **Zustand** | Client state (UI selections, filters, drafts, modals) |
| **React Context** | Platform plumbing only |
| **WebSocket events** | INVALIDATE queries (never write to stores directly) |

**This is the strictest state-management discipline in corpus.** Architectural safety rail.

### Package boundary constraints (NON-NEGOTIABLE)

- `packages/core/` — **zero localStorage, zero process.env, zero UI libraries**
- `packages/ui/` — **zero @multica/core imports**
- `packages/views/` — **zero next/*, zero react-router-dom, zero stores**
- App-specific platform wiring lives in `apps/*/platform/`

**"Non-negotiable" explicit framing.** Matches paperclip v14's "5 invariants" style — architectural constitution.

### Development commands

```bash
make dev              # One-command dev (auto-setup + start everything)
make check            # Full verification: typecheck + unit tests + Go tests + E2E
pnpm dev:web          # Next.js dev (port 3000)
pnpm dev:desktop      # Electron dev with HMR
make server           # Go server (port 8080)
make test             # Go tests
pnpm test             # TS unit tests (Vitest)
pnpm typecheck        # TypeScript strict mode
```

**Makefile-driven** — appropriate for polyglot Go + TS monorepo.

### Testing requirements

Tests follow the code, not the app:
- **Shared business logic** → `packages/core/*.test.ts` (Vitest, Node)
- **Shared UI components** → `packages/views/*.test.tsx` (Vitest, jsdom)
- **Platform-specific wiring** → app-level test files
- **E2E flows** → `e2e/*.spec.ts` (Playwright)
- **Go logic** → `server/*` (standard `go test`)

**Key principle:** *"Never test shared component behavior in an app's test file."*

### Coding conventions

- TypeScript strict mode
- English-only comments
- Atomic commits (`feat(scope)`, `fix(scope)`)
- Avoid broad refactors
- Single-word or `/{noun}/{verb}` routes (never hyphenated root routes)
- No compatibility layers unless requested

### Cross-platform rules (new page workflow)

1. Add component to `packages/views/<domain>/`
2. Wire route in both `apps/web/` AND `apps/desktop/`
3. Use `useNavigation().push()` (never framework-specific APIs in shared code)
4. Accept `wsId` as parameter (don't call `useWorkspaceId()` internally)
5. Platform chrome (drag strips, tab system) stays app-specific

**Multi-app consistency discipline** — only project in corpus with mandated dual-app codepath.

### Desktop-specific rules

- Routes = 3 categories: **session routes** (workspace-scoped) / **transition flows** (pre-workspace) / **error states**
- Transition flows (create workspace, accept invite) = `WindowOverlay` state, NOT routes
- `setCurrentWorkspace(slug, uuid)` = singleton source of truth
- Destructive operations: clear workspace → navigate → mutate
- Full-window views need top drag strip for macOS window-move

**Most granular desktop discipline in corpus.**

### Verification workflow

```
1. Run `make check` (full pipeline)
2. Read error output, fix, re-run
3. For faster iteration: targeted checks first (pnpm typecheck, pnpm test, make test)
4. Finish with full `make check` before marking complete
```

## 3. AGENTS.md (1,892 B) — pointer with content

**Opens with:**
> *"This file is a concise pointer document. All authoritative architecture, coding rules, commands, and conventions live in **CLAUDE.md**"*

**But contains substantial original content:**
- Architecture section (Go + Next.js + Electron + pnpm/Turborepo)
- State Management section (TanStack Query + Zustand separation)
- Package Boundaries section (hard rules)
- Commands section (development commands)

**Pattern interpretation:** AGENTS.md = concise summary serving as quick-reference; CLAUDE.md = authoritative deep-dive. Both contain architecture info (some duplication = maintenance risk, acknowledged).

**Contrast with paperclip's pattern:** paperclip CLAUDE.md = 1-liner pointing to AGENTS.md (opposite direction). multica CLAUDE.md = 21KB authoritative source, AGENTS.md = 2KB summary.

**Contrast with gws tri-file:** gws has CLAUDE.md 1-line + AGENTS.md 209-line + CONTEXT.md 44-line (3 distinct audiences). multica has CLAUDE.md authoritative + AGENTS.md redundant summary (2 docs, 1 audience).

## 4. Constitutional governance comparison

| Framework | Inviolable constraints | Count |
|-----------|------------------------|-------|
| paperclip v14 | 5 control-plane invariants + 4 governance primitives | **9 explicit** |
| **multica v15** | **"Non-negotiable" package boundaries (3) + Hard state rule (1) + cross-platform rules (5)** | **9 explicit** |
| gws v13 | Adversarial-input policy + 4 validators | ~5 |
| BMAD v11 | Skill validator rules | 1 |
| Others | Implicit | 0-2 |

→ **multica matches paperclip** in explicit constraint count. Both use "non-negotiable" / "inviolable" language. Strong corpus-level constitutional-governance pattern.

## 5. HANDOFF_ARCHITECTURE_AUDIT.md (18,208 B — not fetched verbatim)

Title suggests **architecture audit document** — likely:
- Comprehensive architecture walkthrough
- Historical decisions + rationale
- Known technical debt
- Handoff context for new contributors

**Routine v2 action item candidate:** "For corpus projects with HANDOFF_* or ARCHITECTURE_* docs, fetch during Phase 0 for ground truth."

## 6. CLI_AND_DAEMON.md (14,507 B — not fetched)

Covers CLI + Agent Daemon architecture — the local-execution layer.

**Inferred contents:**
- CLI command reference
- Daemon process model
- WebSocket communication pattern
- Agent adapter interface

**Corpus significance:** multica's local Agent Daemon + cloud orchestration is a **hybrid pattern** (local execution + cloud coordination). CLI_AND_DAEMON.md documents this.

## 7. SELF_HOSTING trio (SELF_HOSTING + _ADVANCED + _AI = 17.6KB)

Three self-hosting docs:
- **SELF_HOSTING.md** (7KB) — basic setup
- **SELF_HOSTING_ADVANCED.md** (8.5KB) — advanced configuration
- **SELF_HOSTING_AI.md** (2KB) — AI model self-hosting (bring-your-own-LLM endpoint)

**Corpus-first:** dedicated AI-model self-hosting doc. Lets users host inference (Ollama etc) themselves.

**Implication:** multica supports **private on-prem LLM inference** — enterprise/privacy-sensitive use case. paperclip doesn't explicitly support this.

## 8. CLI_INSTALL.md (5.6KB — not fetched)

Install documentation for `multica` CLI.

**Inferred:**
- Homebrew formula
- Script installer
- PowerShell installer
- Verification steps

## 9. Doc architecture comparison

### paperclip v14 doc pattern
- README (positioning)
- AGENTS.md (contributor minimal)
- ROADMAP.md (trajectory)
- adapter-plugin.md (refactor notes)
- CONTRIBUTING.md (standard)
- SECURITY.md (standard)

### gws v13 doc pattern
- README
- CLAUDE.md (1-line pointer)
- AGENTS.md (209-line contributor)
- CONTEXT.md (agent runtime rules)
- CHANGELOG + SECURITY

### **multica v15 doc pattern**
- README + README.zh-CN (user bilingual)
- **CLAUDE.md 21KB (authoritative)** + AGENTS.md summary
- HANDOFF_ARCHITECTURE_AUDIT (historical handoff)
- CLI_AND_DAEMON + CLI_INSTALL (runtime docs)
- **SELF_HOSTING trio** (3 separate deployment docs)
- CONTRIBUTING (standard)

→ **multica = deepest doc organization** for deployment complexity. Self-hosting gets 3 docs (basic/advanced/AI) reflecting complex self-host surface.

## 10. Cross-references

- [[(C) README + zh-CN summary]] — user-facing positioning
- [[(C) Skills + Architecture + skills-lock cluster summary]] — package detail
- [[(C) Electron Desktop + Multi-Platform Architecture]] (Phase 3 entity) — cross-platform discipline deep-dive

## 11. Open questions surfaced

- AGENTS.md pointer-with-content maintenance risk (Q1)
- HANDOFF_ARCHITECTURE_AUDIT.md contents (new — Q26)
- CLI_AND_DAEMON architecture specifics (new — Q27)
- Why 3-way SELF_HOSTING split? Audience differentiation? (new — Q28)
- CLAUDE.md + AGENTS.md duplication handling (new — Q29)
- Self-hosted AI model support scope (new — Q30)
