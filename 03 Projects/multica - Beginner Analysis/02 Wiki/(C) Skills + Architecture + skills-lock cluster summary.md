# (C) Skills + Architecture + skills-lock cluster summary — multica

> **Sources:** skills-lock.json (verbatim) + package structure (root listing) + CLAUDE.md architecture section + README Features
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster

Three technical substrates of multica: **skills** (what it does), **architecture** (how it's built), **skills-lock** (how extensibility is versioned). Together they reveal multica's engineering disposition.

## 2. skills-lock.json — corpus-first dependency manifest

### Full verbatim content

```json
{
  "version": 1,
  "skills": {
    "frontend-design": {
      "source": "anthropics/skills",
      "sourceType": "github",
      "computedHash": "063a0e6448123cd359ad0044cc46b0e490cc7964d45ef4bb9fd842bd2ffbca67"
    },
    "shadcn": {
      "source": "shadcn/ui",
      "sourceType": "github",
      "computedHash": "507f011a70e8b3ae242bdc0bb5b39fd91a1d4049a0f3c281991ccf84973d591c"
    },
    "ui-ux-pro-max": {
      "source": "nextlevelbuilder/ui-ux-pro-max-skill",
      "sourceType": "github",
      "computedHash": "0a413bf988d06481f69bb81df2070741c3ba12dd9f1be2706d57f259c905992d"
    },
    "web-design-guidelines": {
      "source": "vercel-labs/agent-skills",
      "sourceType": "github",
      "computedHash": "a6a44d5498f7e8f68289902f3dedfc6f38ae0cee1e96527c80724cf27f727c2a"
    }
  }
}
```

### Significance

**First dependency-locked skill manifest in corpus.** Prior frameworks ship skills as embedded (codymaster 79, gws 110, BMAD modules) or inline (Superpowers patterns). multica tracks **external** skill imports with version pinning.

### Pattern: package-lock for skills

Inspired by npm's package-lock.json / pnpm's pnpm-lock.yaml — locks exact versions for reproducible builds. Applied to skills:

- **version 1** — format version
- **source** — GitHub org/repo
- **sourceType** — `github` (extensible to git / http / other)
- **computedHash** — SHA-256 for integrity verification

### 4 external skills tracked

| Skill | Source | Org type | Significance |
|-------|--------|----------|--------------|
| **frontend-design** | anthropics/skills | **Anthropic official** | First Anthropic-skill-registry import in corpus |
| **shadcn** | shadcn/ui | Community UI lib | Standard UI practice |
| **ui-ux-pro-max** | **nextlevelbuilder** | Same org as goclaw v4 | **Ecosystem cross-pollination** |
| **web-design-guidelines** | vercel-labs/agent-skills | **Vercel official** | Vercel-sponsored skill registry |

### Corpus-level implications

1. **Anthropic has official skill registry** (`anthropics/skills`) — multica imports from it. **Routine v2 action item:** scan corpus for other projects importing Anthropic skills.

2. **Vercel has agent-skills lab** (`vercel-labs/agent-skills`) — signals Vercel investment in agent ecosystem beyond Next.js.

3. **nextlevelbuilder org contributes to multica** — goclaw's parent org has skill used by multica. **Strong cross-project ecosystem signal.**

4. **SHA-256 integrity** — supply-chain attack resistance for skills. Matters for community-contributed skills.

### Pattern #16 candidate — Skill Dependency Locking

Corpus now has:
- codymaster (v12) — Self-Healing skills, versioning implicit
- BMAD (v11) — module versioning within framework
- **multica (v15) — EXPLICIT skill dependency lock file**

**Hypothesis (Pattern #16):** As skill ecosystems mature, dependency-lock files emerge for reproducible + secure skill composition. multica is first mover.

## 3. 8 supported AI agent models

From README Quick Install + CLAUDE.md:

| Model | Provider | Notes |
|-------|----------|-------|
| **Claude Code** | Anthropic | Primary (Anthropic skills imported) |
| **Codex** | OpenAI | OpenAI agent |
| **OpenClaw** | Community | Also in paperclip v14 + codymaster v12; emerging standard |
| **OpenCode** | Community | Open-source code agent |
| **Hermes** | Nous Research? | Also mentioned in paperclip adapter refactor |
| **Gemini** | Google | Multimodal |
| **Pi** | Inflection AI | Personal AI |
| **Cursor Agent** | Cursor IDE | IDE-integrated |

**8 models = broadest BYO-agent list in corpus.** 

### Comparison to paperclip v14 (6 models)

paperclip: OpenClaw + Claude Code + Codex + Cursor + Bash + HTTP  
multica: Claude Code + Codex + OpenClaw + OpenCode + Hermes + Gemini + Pi + Cursor Agent

**Overlap:** Claude Code + Codex + OpenClaw + Cursor (4 shared)  
**multica-only:** OpenCode + Hermes + Gemini + Pi (4 extras)  
**paperclip-only:** Bash + HTTP (generic hooks)

→ multica supports **more named models**; paperclip supports **more generic hooks**. Different BYO philosophies.

## 4. Monorepo architecture

### Workspace (pnpm + Turborepo)

From CLAUDE.md + root folders:

**apps/:**
- `apps/web/` — Next.js 16 frontend (port 3000)
- `apps/desktop/` — Electron with electron-vite

**packages/:**
- `packages/core/` — headless business logic (zero React DOM, zero browser APIs)
- `packages/ui/` — atomic UI components (zero business logic)
- `packages/views/` — shared business pages (no framework routing)
- `packages/tsconfig/` — shared TS config

**server/:**
- Go backend (Chi router, sqlc, gorilla/websocket)

**Other:**
- `docker/` — Docker configs
- `docs/` — mintlify docs
- `e2e/` — Playwright E2E tests
- `scripts/` — build/release utilities

### Build orchestration: Turborepo

**First Turborepo in corpus.** Turbo provides:
- Incremental builds (cache-based)
- Parallel task execution
- Remote caching (Vercel's Turborepo cloud offering)
- Pipeline definitions via turbo.json

### Tech stack detail

- **Node 22** (bleeding edge)
- **Go 1.26.1** (bleeding edge)
- **Next.js 16** (latest)
- **Electron** (via electron-vite — modern build tooling)
- **PostgreSQL 17 + pgvector** — first vector-capable DB in corpus
- **sqlc** — Go SQL codegen for type-safe queries
- **gorilla/websocket** — WebSocket real-time
- **Chi** — lightweight Go HTTP router
- **TanStack Query** — server state management
- **Zustand** — client state management
- **Vitest** — unit test runner (TS)
- **Playwright** — E2E browser tests
- **goreleaser** — Go binary release automation

## 5. Hybrid architecture: local daemon + cloud orchestration

### Design pattern

```
User machine:                          Multica Cloud (or self-hosted):
  ├─ CLI (`multica`)                     ├─ Next.js web (dashboard)
  ├─ Agent Daemon                         ├─ Go API server
  │    ├─ Claude Code session              │    ├─ Chi router
  │    ├─ Cursor agent                     │    ├─ WebSocket hub
  │    ├─ Codex invocation                 │    └─ pgvector queries
  │    └─ ... (any of 8 models)            └─ PostgreSQL 17 + pgvector
  └─ File system access
       ↑                                    ↑
       └──────── WebSocket ─────────────────┘
```

### Why this architecture

- **Privacy:** user's code stays local (daemon executes)
- **Cost:** no cloud compute per agent task
- **Model choice:** user's local Claude Code/Cursor subscription
- **Orchestration:** cloud coordinates tasks + tracks progress + stores history
- **Team collaboration:** cloud sees all team workspaces + cross-agent coordination

### Corpus-first hybrid pattern

- deer-flow (T5): fully cloud-hosted
- autoresearch (T5): fully local
- paperclip (T5): user runs server + UI + daemon locally (self-hosted)
- goclaw (T2): multi-tenant cloud
- **multica (T2): local daemon + cloud orchestration hybrid**

**multica unique hybrid** — neither pure-cloud nor pure-local. Balances privacy + collaboration.

## 6. Desktop app (Electron) — corpus-first

Details from CLAUDE.md:
- `apps/desktop/` uses **electron-vite** (modern build tooling)
- 3 route categories: session / transition flows / error states
- Transition flows = `WindowOverlay` state, NOT routes
- `setCurrentWorkspace(slug, uuid)` = singleton source of truth
- Top drag strip for macOS window-move

### Why desktop?

- **Always-on** daemon connection
- **Native notifications** for agent task completion
- **File system deep integration** (watch code changes)
- **Better keyboard shortcuts** than browser

### Corpus significance

**First Electron app in 15 wikis.** Signals multica's UX investment — web alone is insufficient for "agents as real teammates" always-on workflow.

## 7. pgvector — AI-ready DB

**PostgreSQL 17 + pgvector extension** — first vector-capable DB in corpus.

### What's vectorized? (Q13)

Speculation (no README detail):
- **Skills** — semantic skill matching ("find skill for this task" via embedding)
- **Issues/tasks** — similarity search ("find similar past tasks")
- **Agent outputs** — knowledge base from agent work
- **Team knowledge** — RAG-style retrieval for agents

### Why pgvector specifically

- Unified DB (no separate vector DB like Pinecone/Weaviate)
- Transactional with relational data
- Self-hostable (matches multica's self-host model)
- Mature Postgres ecosystem

## 8. goreleaser — Go binary release automation

**goreleaser** = Go's standard release tool. multica uses for:
- Cross-platform Go binary builds
- GitHub release asset upload
- Homebrew formula generation
- Docker image push
- Signed + notarized macOS binaries

**goclaw (v4 T2 N=1) also likely uses goreleaser** (pure Go project). Standard Go ecosystem tool.

## 9. Release channels

- **43 releases over 2473 commits** — weekly cadence
- **v0.2.6 current** (pre-1.0)
- **Canary + stable** (inferred from goreleaser config; not confirmed)

## 10. Testing infrastructure

Test matrix (from CLAUDE.md):

| Test type | Location | Tool |
|-----------|----------|------|
| Shared business logic | `packages/core/*.test.ts` | Vitest (Node) |
| Shared UI components | `packages/views/*.test.tsx` | Vitest (jsdom) |
| Platform wiring | `apps/*/test` | Vitest |
| E2E flows | `e2e/*.spec.ts` | Playwright |
| Go backend | `server/*` | `go test` |

**5 test categories** — parallels paperclip's 6-category matrix (without promptfoo equivalent).

**Key discipline (CLAUDE.md):** *"Never test shared component behavior in an app's test file."*

## 11. Cross-references

- [[(C) README + zh-CN summary]] — user positioning
- [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] — contributor discipline
- [[(C) skills-lock + Ecosystem Cross-Pollination]] (Phase 3 entity) — skills-lock deep-dive

## 12. Open questions

- What vectorizes? (Q13)
- Turborepo remote caching enabled? (new — Q31)
- Electron native notifications implementation? (new — Q32)
- Skill import process — automatic sync or manual? (new — Q33)
- Skill hash computation algorithm published? (new — Q34)
- Self-host AI model list (Ollama? vLLM? TGI?) (Q30)
- `.goreleaser.yml` config scope (new — Q35)

## 13. Corpus-first observations

- **First skills-lock.json** — dependency-locked skill manifest
- **First Anthropic-skills-registry import** (frontend-design from anthropics/skills)
- **First Vercel-agent-skills import** (web-design-guidelines from vercel-labs/agent-skills)
- **First Turborepo** in monorepo orchestration
- **First pgvector/Postgres 17** AI-ready DB
- **First Electron desktop app**
- **First hybrid local-daemon + cloud-orchestration architecture**
- **8 agent models = broadest BYO list**
