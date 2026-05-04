# (C) Entity 1 — Rowboat Core Product: knowledge-graph-personal-AI-coworker

**Source scope:** `apps/x` Electron flagship + TRACKS.md + knowledge/ subsystem + integrations + voice + BYO model + Cmd+K Copilot

## 1. Identity

**Name:** Rowboat (app namespace `x` in monorepo)
**Type:** Electron desktop personal-AI-coworker application
**Primary interface:** Tiptap-based markdown editor + sidebar Copilot chat + inline Cmd+K + track chips
**Core artifact:** User's local Obsidian-compatible Markdown vault at `~/.rowboat/` or user-chosen directory

## 2. Capability overview

**3 verbatim claims from README:**

| Capability | Verbatim |
|---|---|
| Remember | *"the important context you don't want to re-explain (people, projects, decisions, commitments)"* |
| Understand | *"what's relevant right now (before a meeting, while replying to an email, when writing a doc)"* |
| Help you act | *"by drafting, summarizing, planning, and producing real artifacts (briefs, emails, docs, PDF slides)"* |

**5 use cases from README:**
1. Meeting prep from prior decisions, threads, open questions
2. Email drafting grounded in history and commitments
3. Docs & decks generated from ongoing context (including PDF slides)
4. Follow-ups: capture decisions, action items, owners
5. On-your-machine help: create files, summarize into notes, run workflows using local tools (explicit reviewable actions)

**5 inline examples from README:**
- `Build me a deck about our next quarter roadmap` → generates PDF using context from knowledge graph
- `Prep me for my meeting with Alex` → pulls past decisions, open questions, relevant threads (brief or voice note)
- Track a person, company or topic through live notes
- Visualize, edit, update knowledge graph anytime (it's just Markdown)
- Record voice memos that automatically capture and update key takeaways

## 3. Architectural overview

```
┌─────────────────────────────────────────────────────────┐
│  Electron Renderer (React 19 + Vite + Tiptap editor)    │
│  • Note editor with inline track chips                  │
│  • Sidebar Copilot chat                                 │
│  • Cmd+K command palette                                │
│  • Track modal (click chip to manage)                   │
└───────────────────┬─────────────────────────────────────┘
                    │ IPC (contextBridge)
                    ▼
┌─────────────────────────────────────────────────────────┐
│  Electron Main Process (Node.js)                         │
│  • ipc.ts (29.8KB IPC handlers)                         │
│  • oauth-handler.ts (14.0KB Google OAuth)               │
│  • composio-handler.ts (11.4KB external tools)          │
│  • browser/ (5-file embedded browser for local-sites)   │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  packages/core/src/ (22 subsystems, @x/core workspace)  │
│  • knowledge/ (35 modules, 280-330KB)                   │
│  • application/assistant/ (Copilot + skills)            │
│  • agents/ (agent runtime)                              │
│  • voice/ (Deepgram STT + ElevenLabs TTS)               │
│  • mcp/ (MCP client/server)                             │
│  • composio/ (external tool bridge)                     │
│  • models/ (provider abstraction)                       │
│  • workspace/ (vault file ops)                          │
│  • ... 14 more                                          │
└───────────────────┬─────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  Local Markdown Vault (Obsidian-compatible)             │
│  • knowledge/ folder (user's actual working memory)     │
│  • gmail_sync/ folder (synced email threads)            │
│  • calendar/ folder (synced calendar events)            │
│  • fireflies/ folder (meeting transcripts)              │
│  • knowledge_graph_state.json (change detection)        │
│  • events/pending/ + events/done/ (event pipeline)      │
└─────────────────────────────────────────────────────────┘
```

## 4. Knowledge graph subsystem

**Build pipeline (from `knowledge/README.md`):**

1. `sync_gmail.ts` / `sync_calendar.ts` / `sync_fireflies.ts` pull source data
2. Source files written as markdown under their folders
3. `build_graph.ts` orchestrates: batch-processes source files
4. `note_creation.ts` agent extracts entities → markdown notes with backlinks
5. `graph_state.ts` tracks processed files via hybrid mtime+hash detection

**Change detection discipline (corpus-first):**
- Quick check: mtime unchanged → skip
- Verification: mtime changed, hash unchanged → skip (false positive)
- Process: hash changed → actually changed → process

**State file:** `WorkDir/knowledge_graph_state.json` with per-file `{ mtime, hash, lastProcessed }`

**5 specialized agents:**

| Agent | Purpose | File | Size |
|---|---|---|---|
| `note_creation` | Entity extraction from emails/transcripts → markdown notes | note_creation.ts | 40.1KB |
| `labeling_agent` | Email auto-labeling | labeling_agent.ts | 12.2KB |
| `inline_task_agent` | Inline task management | inline_task_agent.ts | 15.2KB |
| `note_tagging_agent` | Auto-tagging notes | note_tagging_agent.ts | 5.9KB |
| `track-run` | Track Block execution | track/run-agent.ts | (see TRACKS.md §3) |

**Agent state separation discipline:** 4 explicit `*_state.ts` modules (agent_notes_state / inline_task_state / labeling_state / note_tagging_state) + central `graph_state.ts` + `version_history.ts`. Corpus-first explicit agent-state-from-logic separation at T5.

## 5. Track Blocks (corpus-first architecture)

**Concept:** Living blocks of content embedded in markdown notes that auto-refresh on schedule, when relevant events arrive, or on demand.

**Example (Chicago-time track refreshed hourly):**

~~~markdown
```track
trackId: chicago-time
instruction: Show the current time in Chicago, IL in 12-hour format.
active: true
schedule:
  type: cron
  expression: "0 * * * *"
```

<!--track-target:chicago-time-->
2:30 PM, Central Time
<!--/track-target:chicago-time-->
~~~

**4 trigger types:**

| Trigger | When fires | Use case |
|---|---|---|
| **Manual** | User/Copilot hits Run | One-off refreshes |
| **Cron** | Exact cron times | Daily morning briefing, hourly weather |
| **Window** | At most once per cron occurrence, within time-of-day window | "Sometime in the morning" updates |
| **Once** | Once at future time, then never | One-shot scheduled tasks |
| **Event-driven** | Matching event arrives | Auto-update on new email / calendar event |

Schedule + eventMatchCriteria can co-exist.

**Event routing (2-pass LLM pipeline):**

1. **Pass 1** (liberal classifier in `routing.ts`): LLM with `Pass1OutputSchema` structured output batches 20 tracks, returns candidate `{trackId, filePath}[]`. Prefers false positives.
2. **Pass 2** (strict agent veto in `run-agent.ts`): Track-run agent reads event payload + target region, decides whether event *genuinely* warrants update. Skips if not relevant.

**Single-writer invariant:** Renderer never writes files. All on-disk changes go through backend helpers in `knowledge/track/fileops.ts`. Avoids races with scheduler/event-processor.

**Concurrency guard:** `runningTracks: Set<string>` keyed by `${trackId}:${filePath}`. Duplicate calls return `{ action: 'no_update', error: 'Already running' }`.

**No retry storms:** `lastRunAt` set at run *start* (not end). Crash mid-run marks track as ran; scheduler doesn't replay.

**FIFO event processing:** Monotonic `IdGen` IDs → lexicographic filenames → strict FIFO.

**8 prompts catalog:** routing-system / routing-user / track-run-instructions / track-run-message / tracks-skill-Copilot / Copilot-trigger-paragraph / run-track-block-context / calendar-sync-digest.

**Schema source-of-truth:** `packages/shared/src/track-block.ts` Zod `TrackBlockSchema`. Copilot skill auto-generates schema documentation via `stringifyYaml(z.toJSONSchema(TrackBlockSchema))` at module load.

**Event sources (2 active producers):**
- `sync_gmail.ts` emits `email.synced` events (3 call sites after successful thread syncs)
- `sync_calendar.ts` emits `calendar.synced` events (bundled per sync with `summarizeCalendarSync()` markdown digest)

**Corpus-first signals:** Track Blocks architecture has 10+ corpus-first primitives (YAML-fenced-in-markdown + 4-trigger-types + 2-pass-classifier + single-writer-invariant + concurrency-guard + no-retry-storms + FIFO-event-processing + auto-generated-skill-schema-from-Zod + "Pass 1 liberal / Pass 2 strict" separation + event-match-criteria-as-natural-language).

## 6. Copilot assistant (Cmd+K + sidebar chat)

**Integration points:**
- Cmd+K in editor → Copilot modal with cursor context
- Sidebar chat → mention `@note-name` to attach note
- Copilot can: create/edit/delete track blocks, run tracks, proactively suggest tracks when user signals interest

**Trigger words for track suggestions** (from `instructions.ts:73`):
*track*, *monitor*, *watch*, *keep an eye on*, "every morning tell me X", "show the current Y in this note", "pin live updates of Z here", plus any Cmd+K request implying auto-refresh.

**Skill loading:** Copilot's `loadSkill('tracks')` builtin tool injects 318-line skill content into system prompt on-demand (not always loaded — progressive context loading).

**Builtin tools** (from `builtin-tools.ts`):
- `update-track-content` (low-level): rewrite target region between markers
- `run-track-block` (high-level): trigger run with optional `context` parameter
- `workspace-edit` / `workspace-readFile` (generic vault file ops)

## 7. Integrations (6 user-configurable + 2 mentioned)

**Configuration convention:** `~/.rowboat/config/*.json` with standardized `{ "apiKey": "<key>" }` format.

| Integration | Config file | Required? | Purpose |
|---|---|---|---|
| Google (Gmail + Calendar + Drive) | OAuth credentials via 7-step setup | **Yes** (core data source) | Primary data sync |
| Deepgram | `deepgram.json` | Optional | Voice input / voice notes STT |
| ElevenLabs | `elevenlabs.json` | Optional | Voice output TTS |
| Exa | `exa-search.json` | Optional | Web research search |
| Composio | `composio.json` | Optional | External tool marketplace |
| MCP | Generic MCP server config | Optional | Any MCP-compatible server |
| Fireflies | (mentioned) | Optional alternative | Alternative meeting-notes capture |
| Klavis | `KLAVIS_API_KEY` env (start.sh) | Optional | Cloud agent infrastructure |

**Standardized config format (corpus-first cross-integration):**
```json
{ "apiKey": "<key>" }
```
Every API key file uses same format. Discoverable + deterministic.

## 8. Bring-your-own-model (Pattern #28 strengthening)

**Native providers (from `apps/cli/package.json` + `apps/rowboatx/package.json`):**

| Provider | Package | Notes |
|---|---|---|
| Anthropic | `@ai-sdk/anthropic` v2.0.44 | Native |
| OpenAI | `@ai-sdk/openai` v2.0.53 | Native |
| Google | `@ai-sdk/google` v2.0.25 | Native |
| OpenRouter | `@openrouter/ai-sdk-provider` v1.2.6 | Native |
| Ollama | `ollama-ai-provider-v2` v1.5.4 | **Local** |
| OpenAI-compatible | `@ai-sdk/openai-compatible` v1.0.27 | Abstraction for any OpenAI-compatible API (including LM Studio) |

**Abstraction layer:** Vercel AI SDK v5.0.102 + Vercel AI Gateway (ai-gateway-for-multi-provider-routing).

**Claim:** *"Swap models anytime — your data stays in your local Markdown vault."*

**Model resolution logic** (from TRACKS.md routing.ts): *"gateway if signed in, local provider otherwise; prefers `knowledgeGraphModel` from config."* — AI Gateway is fallback strategy for signed-in users; local Ollama/LM Studio preferred if configured.

**Config:** `~/.rowboat/config/models.json` with schema `{ provider: { flavor, apiKey?, baseURL?, headers? }, model: string }`.

**Models catalog cache:** `~/.rowboat/config/models.dev.json` (OpenAI/Anthropic/Google only).

## 9. MCP extensibility

**Claim:** *"Rowboat can connect to external tools and services via Model Context Protocol (MCP). That means you can plug in (for example) search, databases, CRMs, support tools, and automations - or your own internal tools."*

**Examples cited:** Exa (web search), Twitter/X, ElevenLabs (voice), Slack, Linear/Jira, GitHub, "and more."

**Implementation:** `@modelcontextprotocol/sdk` v1.20.2 (both server and client).

**Tool-count:** Not surfaced in README. Based on mention-list + integrations = ~7 MCP integration surfaces + generic MCP server support. **Tier-1-basic (1-5 tools) classification per Pattern #18 v42-mini-audit codification.**

**Bidirectional MCP:** Package dependency suggests both MCP server (rowboat exposes knowledge-graph tools) and MCP client (rowboat consumes external MCP servers). Direction not explicitly documented in public docs.

## 10. Voice subsystem

**Voice input (STT):** Deepgram API via `~/.rowboat/config/deepgram.json`
- Use case: voice memos that auto-update knowledge graph
- Latency/cost: not documented

**Voice output (TTS):** ElevenLabs API via `~/.rowboat/config/elevenlabs.json`
- Use case: meeting prep briefs delivered as voice notes
- Quality: ElevenLabs is premium-tier, so quality excellent but cost per-character

**Workflow integration:** Voice memos → knowledge graph auto-update. Voice briefs ("Prep me for my meeting with Alex") delivered as TTS audio or text.

**Observation:** Using 3rd-party voice APIs (Deepgram + ElevenLabs) is pragmatic but incurs cost + data-flow-to-provider. No local-Whisper option documented despite local-first positioning. Minor local-first-caveat.

## 11. Local-sites + embedded browser

`apps/x/apps/main/src/browser/` has 5 files: control-service.ts (9.3KB) + ipc.ts (2.8KB) + navigation.ts (1.2KB) + page-scripts.ts (18.4KB) + view.ts (23.6KB) = 57KB embedded-browser subsystem.

**Purpose (inferred):** Headless/embedded browser for local-sites scraping or page interaction (likely powering Exa web-search integration + Firecrawl scraping fallback).

**Comparison to browser-use v41:** browser-use is standalone browser-agent framework (full T5). Rowboat embeds browser as secondary capability for research + sites. Distinct scope.

## 12. PDF deck generation

**README claim:** *"Build me a deck about our next quarter roadmap → generates a PDF using context from your knowledge graph"*

**Implementation hint:** `html-to-docx.d.ts` type declaration file in `apps/x/apps/main/src/` suggests HTML→DOCX conversion pipeline (presumably PDF via print-to-PDF or similar).

**Status:** Feature claimed but implementation not explored in sources probed.

## 13. Corpus-first observations (Entity 1 tally)

| # | Observation |
|---|---|
| 1 | Knowledge-graph-as-Markdown explicitly Obsidian-compatible at T5 |
| 2 | Track Blocks: YAML-fenced live-updating notes with 4 trigger types + 2-pass classifier |
| 3 | Hybrid mtime+hash change detection documented technique |
| 4 | Single-writer invariant explicit discipline |
| 5 | Auto-generated Copilot skill schema from Zod source-of-truth |
| 6 | Standardized `{ "apiKey": "<key>" }` cross-integration config format |
| 7 | 5 specialized agents in single product |
| 8 | Agent-state-separation discipline (4 `*_state.ts` modules) |
| 9 | 22-subsystem core-package architectural decomposition |
| 10 | `claude-cowork` identity signal (repo topic) |
| 11 | Voice memo → knowledge graph auto-update workflow |
| 12 | Event-driven + scheduled + manual track triggers in unified primitive |

## 14. Pattern cross-references

- **Pattern #17 variant 3** — Rowboat Labs YC-S24 ecosystem-startup strengthening
- **Pattern #18** — MCP Tier-1-basic (1-5 tools surfaced) + bidirectional implied
- **Pattern #19 archetype 1 (Karpathy)** — implicit structural parallel observation (knowledge-graph-as-Markdown)
- **Pattern #22 AGENTS.md** — counter-evidence (CLAUDE.md present, AGENTS.md absent)
- **Pattern #28 Multi-Provider** — 11th data point (6 native + Vercel AI SDK + AI Gateway + LM Studio local option)
- **Pattern #50 Commercial-Funnel** — 6th data point (7-surface funnel)

## 15. Limitations + caveats

- **Bus-factor:** YC-stage-startup 2-4 person team
- **EN-only:** No i18n (VN/CN/JA/KO absent)
- **Hosted-LLM data flow:** Local-first data-at-rest, but prompts flow to LLM provider unless Ollama/LM Studio configured
- **Voice cost:** Deepgram + ElevenLabs both paid APIs
- **Product-pivot risk:** Legacy SaaS code still in repo; unclear maintenance strategy for 2-product codebase
- **No mobile:** Desktop-only
- **No multi-user:** Single-user personal coworker; team features would require legacy SaaS tier
- **No vault-sync:** User-managed (Git / iCloud / Dropbox / etc. — not built-in)

## Cross-references to wiki siblings

- **v15 multica** — 1st Electron in corpus (T2 managed-agents-platform); rowboat 2nd Electron (T5 personal-productivity)
- **v30 OpenHands** — T5 SWE-agent; comparable 5-deployment-surface complexity
- **v38 DeepTutor** — T5 education; i18n contrast (9-language vs EN-only)
- **v41 browser-use** — T5 browser-agent; comparable multi-provider breadth
