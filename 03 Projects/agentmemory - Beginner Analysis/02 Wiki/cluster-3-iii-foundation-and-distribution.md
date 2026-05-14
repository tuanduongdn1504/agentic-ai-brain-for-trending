# Cluster 3 — iii-engine foundation + distribution + integrations

> **Sources:** README "iii Engine Foundation" + "REST API" sections, package.json, repo tree, integrations/ directory, platform table

## "agentmemory is already a running iii instance"

This cluster feeds the **PRIMARY Pattern Library deliverable** (Entity 2). The README states the foundation relationship in unusually strong terms:

> *"agentmemory **is already a running iii instance**. It uses iii primitives exclusively."*

Not "built with iii." Not "uses the iii SDK." **Is a running iii instance.** The project self-identifies as an *instance of the host platform*. agentmemory rolls **none of its own infrastructure** — every infrastructure concern is delegated to an [iii-engine](https://github.com/iii-hq/iii) primitive:

| Concern | iii primitive used | What a normal TS project would roll itself |
|---|---|---|
| HTTP serving | **HTTP Triggers** | Express.js / Fastify |
| Storage + vectors | **KV State** | SQLite / Postgres + pgvector |
| Real-time streams | **Streams** | SSE / Socket.io |
| Process supervision | **Worker Supervision** | pm2 / systemd |
| Observability | **OTEL Integration** | Prometheus / Grafana |
| Plugin / extension system | **Function Registry** | Custom plugin system |

The README literally annotates each primitive with the thing it *"replaces."* The "Zero external databases" headline claim from Cluster 1 is a *consequence* of this: there is no separate database because **KV State is the database**, and KV State belongs to iii-engine.

## The repo's own metrics, in iii terms

> *"118 source files · ~21,800 LOC · 800 tests · 123 functions · 34 KV scopes"*

Note the unit on the last two: **"123 functions"** and **"34 KV scopes."** A normal project would count modules and database tables. agentmemory counts *iii Function Registry entries* and *iii KV State scopes* — its own internal vocabulary is the host platform's vocabulary. This is the structural tell that distinguishes Platform-Primitive Foundation from ordinary "uses a framework as a dependency."

## Extension is via the host platform's CLI

agentmemory is extended **not by editing agentmemory**, but by invoking iii-engine's own CLI:

```bash
iii worker add iii-pubsub     # Multi-instance fan-out
iii worker add iii-cron       # Scheduled lifecycle
iii worker add iii-queue      # Durable retries
iii worker add iii-sandbox    # Isolated code execution
```

So the upgrade path for "I need cron-based memory consolidation" is *not* `npm install` a plugin — it is `iii worker add iii-cron`. The extension surface belongs to iii, not to agentmemory. This is the strongest single piece of N=1 evidence for the Platform-Primitive Foundation candidate: **even the project's extensibility is the platform's, not its own.**

## The dependency that proves it (package.json)

```json
"dependencies": {
  "@anthropic-ai/claude-agent-sdk": "^0.2.56",
  "@anthropic-ai/sdk": "^0.39.0",
  "@clack/prompts": "^1.2.0",
  "dotenv": "^16.4.7",
  "iii-sdk": "^0.11.2",
  "zod": "^4.0.0"
}
```

Six runtime dependencies. No HTTP framework. No database driver. No ORM. No vector-DB client. No process manager. No metrics library. **The entire infrastructure stack is the single `iii-sdk` line.** The other five deps are: two Anthropic SDKs (for the LLM-provider + agent-SDK integrations), `@clack/prompts` (the `npx` setup wizard), `dotenv` (config), `zod` (validation). For a project that is *also* a 107-endpoint REST server with triple-stream search and an OTEL trace surface, a six-dependency `package.json` is only possible because iii-engine is the substrate.

The version coupling is tight and brittle: `iii-sdk ^0.11.2`, and the CHANGELOG (Cluster 2) records the project **pinned iii-engine to v0.11.2 because v0.11.6+ broke it.** Platform-Primitive Foundation is a power move *and* a coupling risk — when the foundation moves, the instance must move with it or freeze.

## Distribution — one npm command

> *"npx @agentmemory/agentmemory"*

Package: **`@agentmemory/agentmemory` v0.9.12**, Apache-2.0, `main: dist/index.mjs`, built with `tsdown`. The `npx` invocation launches the memory server (port 3111) + the real-time viewer (port 3113). Prerequisites: **Node.js ≥ 20** and **either the `iii-engine` binary or Docker** (`docker-compose.yml` + `iii-config.docker.yaml` are in the repo root). `@clack/prompts` powers an interactive setup wizard on first run.

## The 15+ platform integration mechanism — shared backend, not coexistence

Cluster 1 listed the platforms; this cluster is about the **mechanism**. agentmemory reaches 15+ agent platforms, but the mechanism is **distinct from every prior multi-platform corpus subject**:

| Integration tier | Platforms | Mechanism |
|---|---|---|
| **Deepest — hooks + MCP + skills** | Claude Code (12 hooks), Codex CLI (6 hooks) | Plugin with lifecycle hooks (`.claude-plugin/`, `.codex-plugin/`) |
| **MCP server** | Cursor, Claude Desktop, Cline, Roo Code, Windsurf, Gemini CLI, OpenCode | Standard `mcpServers` config block |
| **MCP + plugin** | Hermes, OpenClaw | Deep memory-provider integration |
| **MCP or REST** | Goose, Aider, Kilo Code, pi | Multiple pathways |
| **REST API** | Any agent (32+ claimed) | 107 programmatic HTTP endpoints |

**Why this is a NEW Pattern #18 sub-archetype.** Prior corpus multi-platform mechanisms:
- **Pattern #18 Layer 1 — cross-IDE *coexistence*** (claude-seo v64): ship parallel per-platform config files (CLAUDE.md + AGENTS.md + ...) so each platform reads its own.
- **Pattern #18 Layer 2 — protocol/format *translation*** (free-claude-code v60 runtime API-proxy; cc-sdd v61 install-time skill-format translator; OpenSpec v58 per-tool format): translate one artifact into each platform's format.

agentmemory does **neither**. It runs **one shared backend service** and every agent platform is just a *client* of it. The memory lives in one place; the 15+ platforms are connection methods, not copies. The README's phrase — *"One server, memories shared across all agents"* — is the mechanism name. (Caveat: per Cluster 2 Finding #2, *cross-agent sharing* of that one server's memory is partly still on the ROADMAP — but the *architecture* is shared-backend regardless.)

This is a **3rd structural mechanism within Pattern #18's multi-platform space**: coexistence (Layer 1) / translation (Layer 2) / **shared-backend-service (NEW)**.

## The REST API surface

> *"107 endpoints on port 3111 (protected with `AGENTMEMORY_SECRET` bearer token when configured)."*

Representative endpoints:
- `POST /agentmemory/session/start` — start + get context
- `POST /agentmemory/smart-search` — hybrid search
- `POST /agentmemory/observe` — capture observation
- `POST /agentmemory/remember` — save insight
- `POST /agentmemory/forget` — delete observations
- `GET /agentmemory/health` — always public
- `GET /agentmemory/profile` — project profile
- `POST /agentmemory/graph/query` — knowledge-graph query

The REST surface is what makes the "32+ agents" claim possible — any HTTP-capable agent is a client. It is also what makes agentmemory a **T2 Service** and not a T1 Augmentation: the substance is a server with a documented API, and the Claude Code plugin is just one (privileged) client of it.

## Repository structure

```
agentmemory/
├── .claude-plugin/       # Claude Code plugin (12 hooks + MCP + skills)
├── .codex-plugin/        # Codex CLI plugin (6 hooks)
├── .github/              # CI workflows
├── src/                  # main codebase (TS, ~21,800 LOC across 118 files)
├── test/                 # test suite (~827 tests)
├── plugin/               # agent integrations
├── packages/mcp/         # MCP server
├── integrations/         # Cursor, Claude Desktop, OpenClaw, Hermes, ... configs
├── examples/python/      # Python REST-client examples
├── benchmark/            # performance reports (LongMemEval-S harness)
├── website/              # documentation site
├── assets/               # images, badges
├── iii-config.yaml       # iii-engine config
├── iii-config.docker.yaml
├── docker-compose.yml
├── package.json  tsconfig.json  tsdown.config.ts
└── [11 governance .md files — see Cluster 2]
```

The `integrations/` directory holding per-platform config and the dual `.claude-plugin/` + `.codex-plugin/` at root are the physical footprint of the shared-backend mechanism — thin client-adapters, one per platform, all pointing at the same server.

## Pattern Library signals from Cluster 3

- **PRIMARY — NEW candidate: Platform-Primitive Foundation (N=1, stale-flagged).** agentmemory is built *entirely* on iii-engine's primitives, self-identifies as *"a running iii instance,"* counts itself in the host platform's units (functions / KV scopes), and is extended via the host platform's CLI. Distinct from "uses a framework as a dependency." Full registration proposal in Phase 4b. Un-stale criterion: a 2nd subject built entirely-on-another-platform's-primitives with self-as-instance framing.
- **Pattern #18 Agent Runtime Standardization — NEW sub-archetype: shared-backend-service.** 3rd structural multi-platform mechanism alongside Layer 1 coexistence + Layer 2 translation. One server, 15+ platforms as clients. Distinct enough to register as a sub-archetype within the most-refined pattern in the library.
- **Pattern #2 Distribution Evolution** — single-command `npx` distribution; npm; `tsdown` build. Corpus-typical for TS projects.
- **Platform-coupling-risk observation** — the `iii-sdk ^0.11.2` pin + the v0.11.6 incompatibility (Cluster 2) is the *cost* side of Platform-Primitive Foundation: tight version coupling to the foundation. Note in Entity 2 as the candidate's built-in tension.
- **Pattern #57 / cross-corpus** — `.codex-plugin/` packaging is a structural sibling to codex-plugin-cc v62; the knowledge-graph query stream is a structural sibling to vault project graphify.
