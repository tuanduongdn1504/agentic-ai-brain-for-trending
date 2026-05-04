# (C) Cluster 2 — Architecture + monorepo + integrations + Track Blocks

**Sources:** CLAUDE.md (5.4KB) + docker-compose.yml (8.2KB, 269 lines) + .env.example + start.sh + build-electron.sh + apps/x/TRACKS.md (26.0KB feature deep-dive) + apps/x/ structure + apps/x/packages/core/src/ subsystems + apps/cli/package.json + apps/python-sdk/

## 1. 7-app monorepo structure

```
rowboat/
├── apps/
│   ├── x/                 # Electron desktop app (NEW FLAGSHIP — knowledge-graph-personal-AI-coworker)
│   ├── rowboat/           # Next.js web dashboard (LEGACY — multi-agent SaaS, Auth0+Mongo+Redis+Qdrant+RAG)
│   ├── rowboatx/          # Next.js frontend + companion to legacy SaaS
│   ├── cli/               # @rowboatlabs/rowboatx v0.16.0 npm CLI (Hono server + ink TUI)
│   ├── python-sdk/        # rowboat v5.0.1 PyPI client SDK (by Ramnique Singh @rowboatlabs.com)
│   ├── docs/              # Documentation site (mkdocs-style)
│   └── experimental/      # chat_widget + simulation_runner + tools_webhook (3 incubation projects)
├── CLAUDE.md              # AI coding agent context (5.4KB) — Anthropic-runtime-aligned
├── README.md              # User-facing readme (6.4KB)
├── docker-compose.yml     # Legacy SaaS deployment (269 lines)
├── .env.example           # 70+ env vars across MongoDB+Redis+Qdrant+Auth0+OpenAI+Composio+Klavis+S3+Firecrawl
├── google-setup.md        # 7-step Google OAuth integration guide (3.9KB)
├── start.sh               # Docker compose orchestrator
└── build-electron.sh      # Electron app build wrapper
```

**Corpus-first observation:** **Product-pivot-in-monorepo** — legacy `apps/rowboat` (multi-agent SaaS, Jan 2025 launch) coexists with new `apps/x` Electron flagship (personal-AI-coworker pivot). Repo evolved from one product into another while preserving legacy code (not deleted, presumably maintained-but-secondary). Distinct from clean rebrand (Pattern #58 sub-variant 58a/58b) — this is product-strategy-pivot retaining old + new in same repo. **Observational only at v43 — flagged for Pattern #58 3rd data point watch.**

## 2. `apps/x` Electron app architecture (NESTED pnpm workspace)

```
apps/x/                            # Outer workspace
├── package.json                    # Workspace root, dev scripts
├── pnpm-workspace.yaml             # Defines workspace packages
├── pnpm-lock.yaml                  # 572.3KB lockfile (large dependency surface)
├── TRACKS.md                       # 26KB Track Blocks feature deep-dive doc
├── apps/
│   ├── main/                       # Electron main process (Node.js)
│   │   ├── src/main.ts             # 10.4KB entry
│   │   ├── src/ipc.ts              # 29.8KB IPC handlers (richest surface)
│   │   ├── src/oauth-handler.ts    # 14.0KB
│   │   ├── src/composio-handler.ts # 11.4KB
│   │   ├── src/auth-server.ts      # 3.1KB
│   │   ├── src/test-agent.ts       # 577B
│   │   ├── src/browser/            # 5 files: control-service / ipc / navigation / page-scripts / view (23.6KB)
│   │   ├── forge.config.cjs        # Electron Forge config
│   │   └── bundle.mjs              # esbuild bundler
│   ├── renderer/                   # React 19 UI (Vite 7 + Tiptap editor + TailwindCSS + Radix UI)
│   └── preload/                    # Electron preload scripts (contextBridge)
└── packages/
    ├── shared/                     # @x/shared - Types, utilities, validators (Zod schemas)
    └── core/                       # @x/core - Business logic, AI, OAuth, MCP
```

**Build dependency order:** shared → core → preload → renderer + main. `npm run deps` builds shared+core+preload sequentially.

**Bundling discipline:** esbuild bundles to single CommonJS file. Why? *"pnpm uses symlinks for workspace packages. Electron Forge's dependency walker can't follow these symlinks. esbuild bundles everything into a single file, eliminating the need for node_modules in the packaged app."* (CLAUDE.md verbatim). Corpus-first esbuild-bundle-for-electron-forge-symlink-workaround documented technique.

**Tech stack:**

| Layer | Technology |
|---|---|
| Desktop | Electron 39.x |
| UI | React 19, Vite 7 |
| Styling | TailwindCSS, Radix UI |
| State | React hooks (no Redux/Zustand) |
| AI | Vercel AI SDK + OpenAI/Anthropic/Google/OpenRouter providers + Vercel AI Gateway + Ollama + models.dev catalog |
| IPC | Electron contextBridge |
| Build | TypeScript 5.9, esbuild, Electron Forge |
| Code signing | APPLE_ID + APPLE_PASSWORD + APPLE_TEAM_ID env vars (Mac notarization production) |

## 3. `packages/core/src/` subsystems (22 modules)

| Subsystem | Purpose |
|---|---|
| `account/` | User account + identity |
| `agent-schedule/` | Agent scheduling (separate from Track Block scheduling) |
| `agents/` | Agent runtime + definitions |
| `application/assistant/` | Copilot system prompt + skills + builtin tools (skills/tracks/skill.ts ~318 lines) |
| `auth/` | Authentication (OAuth + Google) |
| `billing/` | Billing surface (placeholder for paid tier?) |
| `composio/` | Composio external tool integration |
| `config/` | User config files at `~/.rowboat/config/*.json` |
| `di/` | Dependency injection (awilix) |
| `knowledge/` | **35 modules — flagship subsystem** (knowledge graph build + sync + agents + tracks) |
| `local-sites/` | Local-site browsing/scraping primitive |
| `mcp/` | MCP client/server integration |
| `models/` | Model resolution + provider abstraction |
| `pre_built/` | Pre-built workflows? |
| `runs/` | Agent run lifecycle |
| `search/` | Search primitive |
| `services/` | Service abstractions |
| `slack/` | Slack integration (mentioned in README MCP list) |
| `voice/` | Voice STT (Deepgram) + TTS (ElevenLabs) |
| `workspace/` | Workspace abstraction (file ops in user vault) |

**Corpus-first signal:** 22 named subsystems in single core package = corpus-deepest core-package architectural decomposition at T5. Comparable to OpenHands v30 5-deployment-surface complexity but better organized as single package.

## 4. `packages/core/src/knowledge/` (35 modules — flagship)

| Module | Size | Purpose |
|---|---|---|
| `note_creation.ts` | 40.1KB | Largest knowledge-system module — entity extraction agent |
| `sync_gmail.ts` | 29.8KB | Gmail thread sync + event emission |
| `sync_calendar.ts` | 28.3KB | Calendar event sync + summarize digest publishing |
| `inline_tasks.ts` | 26.6KB | Inline task management |
| `sync_fireflies.ts` | 22.5KB | Fireflies meeting-notes sync |
| `tag_system.ts` | 20.1KB | Tag taxonomy + auto-tagging |
| `inline_task_agent.ts` | 15.2KB | Agent for inline task processing |
| `labeling_agent.ts` | 12.2KB | Email labeling agent |
| `agent_notes.ts` | 11.9KB | Agent notes primitive |
| `knowledge_index.ts` | 10.1KB | Knowledge graph index |
| `label_emails.ts` | 9.1KB | Email labeling logic |
| `tag_notes.ts` | 8.7KB | Note tagging logic |
| `ensure_daily_note.ts` | 8.0KB | Daily note auto-creation |
| `fireflies-client-factory.ts` | 8.0KB | Fireflies API factory |
| `summarize_meeting.ts` | 7.4KB | Meeting summarization |
| `version_history.ts` | 7.1KB | Version control for knowledge graph |
| `agent_notes_agent.ts` | 5.6KB | Agent for agent-notes |
| `note_system.ts` | 5.8KB | Note system primitive |
| `note_tagging_agent.ts` | 5.9KB | Note tagging agent |
| `run_pipeline.ts` | 5.8KB | Pipeline runner |
| `graph_state.ts` | 4.0KB | Graph state management |
| `agent_notes_state.ts` | 1.8KB | Agent notes state |
| `inline_task_state.ts` | 1.3KB | Inline task state |
| `labeling_state.ts` | 1.3KB | Labeling state |
| `note_tagging_state.ts` | 1.3KB | Note tagging state |
| `repo.ts` | 3.2KB | Repo abstraction |
| `runtime.ts` | 57.5KB | LARGEST single file — agent runtime orchestrator |
| `utils.ts` | 1.4KB | Utilities |
| `file-lock.ts` | 553B | File-locking primitive |
| `limit_event_items.ts` | 302B | Event-item count limiter |
| `welcome.md` | 1.5KB | Welcome content |
| `track/` | (separate subdir) | Track Blocks subsystem |
| `chrome-extension/` | (subdir) | Chrome extension assets |
| `granola/` | (subdir) | Granola integration (meeting transcription alt?) |
| `README.md` | 7.0KB | Knowledge graph system docs (hybrid mtime+hash change detection) |

**Total:** ~280-330 KB of TypeScript across knowledge subsystem alone.

**5 specialized agents identified:**
1. `note_creation` — entity extraction from emails/transcripts → markdown notes
2. `labeling_agent` — email labeling
3. `inline_task_agent` — inline task management
4. `note_tagging_agent` — note tag assignment
5. `track-run` — Track Block execution (in `track/run-agent.ts`)

**State management discipline:** 4 explicit `*_state.ts` modules + central `graph_state.ts` + `version_history.ts`. State separation from agent logic = corpus-first explicit-state-separation discipline at T5 knowledge-system architecture.

## 5. Knowledge graph build pipeline (from `knowledge/README.md`)

**Components:**
- `build_graph.ts` — main orchestrator; processes source files in batches; only new/changed files
- `graph_state.ts` — hybrid mtime+hash change detection (state in `WorkDir/knowledge_graph_state.json`)
- `sync_gmail.ts` + `sync_fireflies.ts` — pull data, save as markdown, trigger graph build

**Change detection (hybrid mtime+hash):**
1. **Quick check:** Compare file mtime — if unchanged → skip
2. **Verification:** If mtime changed, compute content hash — if hash unchanged → false positive → skip
3. **Process:** If hash changed → file actually changed → process

**Why hybrid:** efficient (only hashes potentially changed files) + reliable (confirms actual content changes). **Corpus-first hybrid-mtime-hash-change-detection at T5 knowledge-graph subsystem.**

**State file structure:** `WorkDir/knowledge_graph_state.json` per-file `{ mtime, hash, lastProcessed }`.

## 6. Track Blocks subsystem (corpus-first scheduled-live-updating-notes architecture)

**TRACKS.md is 26KB feature deep-dive** — most-elaborate single-feature documentation in corpus at T5.

**Concept:** Living blocks of content embedded in markdown notes that auto-refresh on schedule, when relevant events arrive, or on demand.

**Anatomy:**
- YAML code fence (` ```track ... ``` `) defines what to produce + when
- Sibling HTML-comment region (`<!--track-target:ID-->...<!--/track-target:ID-->`) holds generated output, rewritten each run
- Single note can hold many independent tracks (one for weather, one for email digest, one for project summary)

**Trigger types (4):**

| Trigger | When fires | Expression |
|---|---|---|
| **Manual** | Only when user/Copilot hits Run | Omit `schedule`, leave `eventMatchCriteria` unset |
| **Scheduled — cron** | Exact cron times | `schedule: { type: cron, expression: "0 * * * *" }` |
| **Scheduled — window** | At most once per cron occurrence, only within time-of-day window | `schedule: { type: window, cron, startTime, endTime }` |
| **Scheduled — once** | Once at future time, then never | `schedule: { type: once, runAt }` |
| **Event-driven** | When matching event arrives | `eventMatchCriteria: "Emails about Q3 planning"` |

Schedule + eventMatchCriteria can co-exist on single track.

**Creation paths (3):**
1. Hand-write YAML fence in note (Tiptap `track-block` extension picks up instantly)
2. Cmd+K with cursor context (Copilot loads `tracks` skill, splices block via `workspace-edit`)
3. Sidebar chat (mention note, ask for track, Copilot appends)

**Architecture:**
```
Editor chip ──click──► TrackModal (React)
                            │
                            ├──► IPC: track:get / update / replaceYaml / delete / run
                            │
Backend (main process)
  ├─ Scheduler loop (15s) ──┐
  ├─ Event processor (5s) ──┼──► triggerTrackUpdate() ──► track-run agent
  └─ Copilot tool run-track-block ──┘                          │
                                                                ▼
                                                  update-track-content tool
                                                                │
                                                                ▼
                                                  target region rewritten on disk
```

**Single-writer invariant (corpus-first explicit):** *"the renderer is never a file writer. All on-disk changes go through backend helpers in `packages/core/src/knowledge/track/fileops.ts`."* Avoids races with scheduler/runner writing runtime fields.

**Pass 1 routing (LLM classifier):** liberal classifier batches tracks at 20-track-batch, structured `Pass1OutputSchema` output. Prefers false positives.

**Pass 2 decision (in track-run agent):** vetoes false positives before touching target region. Quoted verbatim from runner.ts:23-62: *"Determine whether this event genuinely warrants updating the track content. If the event is not meaningfully relevant on closer inspection, skip the update — do NOT call `update-track-content`. Only call the tool if the event provides new or changed information that should be reflected in the track."*

**Concurrency guard:** `runningTracks: Set<string>` keyed by `${trackId}:${filePath}`. Duplicate calls return `{ action: 'no_update', error: 'Already running' }`.

**FIFO discipline:** Monotonic `IdGen` IDs → lexicographic filenames → strict FIFO event processing.

**No retry storms:** `lastRunAt` set at run *start* (not end). Crash mid-run leaves track marked as ran; scheduler doesn't replay.

**8 prompts in catalog** (TRACKS.md "Prompts Catalog" section): routing-system / routing-user-template / track-run-instructions / track-run-message / tracks-skill (Copilot-facing) / Copilot-trigger-paragraph / run-track-block-context-description / calendar-sync-digest-template.

**Schema source-of-truth:** `packages/shared/src/track-block.ts` defines `TrackBlockSchema` (Zod). The Copilot skill auto-generates its schema documentation via `stringifyYaml(z.toJSONSchema(TrackBlockSchema))` at module load — corpus-first auto-generated-skill-schema-from-Zod-source-of-truth discipline.

## 7. `apps/cli/` — `@rowboatlabs/rowboatx` v0.16.0

```json
{
  "name": "@rowboatlabs/rowboatx",
  "version": "0.16.0",
  "bin": { "rowboatx": "bin/app.js" },
  "license": "Apache-2.0",
  "author": "Rowboat Labs"
}
```

**Dependencies (key):**
- `ai` (Vercel AI SDK) v5.0.102
- `@ai-sdk/anthropic` v2.0.44 + `@ai-sdk/openai` v2.0.53 + `@ai-sdk/google` v2.0.25 + `@ai-sdk/openai-compatible` v1.0.27 + `@openrouter/ai-sdk-provider` v1.2.6 + `ollama-ai-provider-v2` v1.5.4 = **6 native AI providers + 1 abstraction** (Vercel AI SDK)
- `@modelcontextprotocol/sdk` v1.20.2 (MCP)
- `hono` v4.10.7 + `@hono/node-server` v1.19.6 + `hono-openapi` v1.1.1 (HTTP server with OpenAPI)
- `googleapis` v169.0.0 + `google-auth-library` v10.5.0 + `@google-cloud/local-auth` v3.0.1 (Google integration)
- `ink` v5.1.0 + `ink-select-input` + `ink-spinner` + `ink-text-input` (React-for-CLI TUI framework)
- `awilix` v12.0.5 (DI container)
- `zod` v4.1.12 + `json-schema-to-zod` v2.6.1 + `yaml` v2.8.2 + `nanoid` v5.1.6 + `node-html-markdown` v2.0.0
- `eventsource-parser` v1.1.2 (SSE)
- `react` v18.3.1 + `yargs` v18.0.0

**Output:** Builds to `dist/` via `tsc`, ships `dist` + `bin` directories on npm.

**Subsystems** (in `apps/cli/src/`): agents / application / config / di / entities / examples / knowledge / mcp / models / runs / scripts / shared / tui + app.ts (21.9KB) + server.ts (6.0KB) + app.js (4.0KB).

**Architectural sibling to `apps/x`** — many subsystem names match (agents, application, config, di, knowledge, mcp, models, runs). Suggests CLI is alternative-runtime for same core logic, not separate codebase.

## 8. `apps/python-sdk/` — `rowboat` v5.0.1 PyPI

```toml
[project]
name = "rowboat"
version = "5.0.1"
authors = [{ name = "Ramnique Singh", email = "ramnique@rowboatlabs.com" }]
dependencies = ["requests>=2.25.0", "pydantic>=2.0.0"]
```

**Single named author confirmed:** Ramnique Singh @rowboatlabs.com (Rowboat Labs employee identity surfaced via PyPI metadata).

**API surface:** `Client` class with `run_turn(messages, conversationId?, mockTools?)` method. Returns `result.turn.output[-1].content` + `conversationId`. Stateless API, conversation state tracked client-side.

**Mock tools:** `mockTools` argument allows testing specific tool configurations without invoking real tools.

**Targets legacy `apps/rowboat` SaaS API** — Python SDK is for the multi-agent SaaS (Auth0 + projectId + apiKey), not the new Electron desktop app. Confirms dual-product reality.

## 9. Legacy `apps/rowboat/` (Next.js multi-agent SaaS)

**Subsystems:** actions / api / billing / components / composio / lib / onboarding / projects / providers / scripts / styles / utils

**Notable:** `billing/` exists in legacy but not in `apps/x` — suggests legacy SaaS had paid tier (or attempted to), new Electron app is OSS-only currently.

**docker-compose.yml services (active + commented):**
- ✅ `rowboat` — Next.js dashboard (port 3000)
- ✅ `setup_qdrant` + `delete_qdrant` (Qdrant vector DB management) — profile-gated
- ✅ `rag-worker` — RAG processing worker (uses Firecrawl + S3 uploads + Gemini file parsing)
- ✅ `jobs-worker` — Background job worker
- ✅ `mongo:latest` — MongoDB
- ✅ `redis:latest` — Redis
- ✅ `qdrant` — Vector DB (custom Dockerfile.qdrant)
- ✅ `docs` — Docs site (port 8000) — profile-gated
- 💤 `rowboat_agents` (port 3001) — COMMENTED OUT
- 💤 `copilot` (port 3002) — COMMENTED OUT
- 💤 `tools_webhook` (port 3005) — COMMENTED OUT
- 💤 `simulation_runner` — COMMENTED OUT
- 💤 `chat_widget` (port 3006) — COMMENTED OUT
- 💤 `twilio_handler` (port 4010) — COMMENTED OUT (voice infra)

**Observation:** 6 services commented out = legacy multi-agent SaaS infrastructure being dismantled. Suggests product-pivot in active progress.

**Auth0 + MongoDB + Redis + Qdrant + S3 + Firecrawl + Gemini-file-parsing + Composio + Klavis + Composio-triggers-webhook** = **enterprise-SaaS-stack-fingerprint** preserved in repo even as Electron app gains primacy.

**Corpus context:** This dual-product preservation is **observational only** — Pattern #58 (Branding-Package Divergence, CONFIRMED v42) covers naming/package divergence; rowboat's case is product-strategy-pivot which is structurally distinct (different scope, different target audience). Flag for Pattern #58 3rd-data-point watch but DO NOT register standalone.

## 10. Cluster 2 corpus-firsts

| # | Observation | Confidence |
|---|---|---|
| 1 | Product-pivot-in-monorepo (legacy SaaS coexists with new Electron flagship) | HIGH (corpus-first explicit dual-product retention) |
| 2 | Track Blocks: YAML-fenced live-updating notes with 4 trigger types | HIGH (corpus-first scheduled-region-rewrite-in-markdown architecture) |
| 3 | Single-writer invariant explicit (renderer never writes; backend helpers only) | HIGH (corpus-first explicit single-writer discipline) |
| 4 | Hybrid mtime+hash change detection for knowledge graph | HIGH (corpus-first documented technique) |
| 5 | Auto-generated Copilot skill schema from Zod source-of-truth | HIGH (corpus-first runtime-skill-doc-generation) |
| 6 | Pass-1 LLM routing (liberal) + Pass-2 agent veto (strict) — 2-pass classifier pattern | HIGH (corpus-first 2-pass event-routing pattern) |
| 7 | esbuild-bundle-for-Electron-Forge-symlink-workaround documented technique | HIGH (corpus-first solution for pnpm-workspace+Electron-Forge issue) |
| 8 | 22-subsystem core-package decomposition at T5 | HIGH (corpus-deepest single-package architectural decomposition) |
| 9 | 5 specialized agents in single product | MEDIUM (comparable to OpenHands/multica primitive count) |
| 10 | Triple-runtime architecture (Electron + CLI server + Python SDK target same logic) | HIGH (corpus-first explicit triple-runtime-with-shared-core observation) |
| 11 | TRACKS.md 26KB single-feature deep-dive doc | HIGH (corpus-first dedicated single-feature engineering deep-dive) |
| 12 | Vercel AI SDK + Vercel AI Gateway = corpus-first Vercel-AI-Gateway mention at T5 | MEDIUM (Vercel AI SDK common, AI Gateway less so) |

## 11. Pattern observations from Cluster 2

- **Pattern #28 Multi-Provider strengthening** — 6 native providers + Vercel AI SDK abstraction + Vercel AI Gateway = ~7-8 provider surface
- **Pattern #18 MCP** — `@modelcontextprotocol/sdk` v1.20.2 in CLI; bidirectional MCP (server + client) implied; tool count not surfaced (Tier-1-basic 1-5 zone per v42-mini-audit codification)
- **Pattern #17 variant 3 strengthening** — Rowboat Labs YC-startup with 4-surface OSS distribution + 1 commercial entity + 22 subsystems = ecosystem-startup-architecture-depth at YC-S24-stage
- **Pattern #2 Distribution Evolution** — Mac DMG + Windows .exe + Linux + Docker + npm + PyPI = 6 distinct distribution mechanisms across 4 surface types

## 12. Cluster 2 absences

- No tests directory surfaced in core (could exist; not in top-level)
- No CHANGELOG.md
- No SECURITY.md (notable absence given OAuth credentials handling)
- No mention of mobile platform support
- No multi-user / team collaboration features in `apps/x` (legacy `apps/rowboat` had Auth0 multi-user)
- No mention of E2E encryption for vault data
- No mention of vault-sync mechanism (Git? iCloud? user-managed?)
- No mention of upgrade-path for users from legacy SaaS to new Electron app
