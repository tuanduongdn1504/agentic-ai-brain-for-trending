# (C) README Summary

> **Source:** `00 Sources/goclaw/README.md` (338 lines, ~14KB)
> **Ingested:** 2026-04-18
> **Coverage:** Full file
> **Routine context:** Source #1 of 3 cho goclaw project (Phase 2, 4th auto-execution)

---

## TL;DR

**VI:** goclaw là **Multi-Tenant AI Agent Platform** viết bằng **Go** — multi-agent gateway với 20+ LLM providers, 7 messaging channels, multi-tenant PostgreSQL, single 25MB binary, deploy được trên $5 VPS. **Different domain** so với 3 siblings (ECC/Superpowers/gstack): đây là **infrastructure/platform layer** cho end-user AI agents, không phải skills framework cho Claude Code devs.

**EN:** goclaw is a Multi-Tenant AI Agent Platform written in Go — multi-agent gateway with 20+ LLM providers, 7 messaging channels, PostgreSQL, single 25MB binary, runs on $5 VPS. Different architectural layer vs 3 siblings (platform vs dev-skill framework).

**Meta-insight cho Storm Bear:** goclaw có "Knowledge Vault" built-in với `[[wikilinks]]` + hybrid search (BM25 FTS + pgvector semantic) + filesystem sync. **Đây là Karpathy's LLM Wiki pattern implemented as infrastructure** — potentially the actual backend Storm Bear vault could use at scale.

---

## Domain positioning

**Critical framing** (repeat across all wiki docs):

| Tier | Purpose | Examples |
|------|---------|----------|
| **Agent-as-assistant** (dev workflow) | Enhance Claude Code for individual developers | ECC, Superpowers, **gstack** |
| **Agent-as-service** (end-user platform) | Multi-tenant AI agent service for end users | **goclaw** |

→ goclaw KHÔNG compete với 3 siblings. Different layer.

**Overlap point:** goclaw can **invoke** Claude CLI / Codex / ACP as **LLM providers** — meaning goclaw có thể chạy gstack skills as backend if wired up. **Potential integration pattern, not competition.**

---

## Tác giả + background

**nextlevelbuilder** (Twitter: `@nlb_io`)
- Hosts docs at `docs.goclaw.sh`
- Origin: "GoClaw was originally inspired by the [OpenClaw](https://github.com/openclaw/openclaw) project architecture" (cited in Acknowledgments)
- Vietnamese signal: `_readmes/README.vi.md` exists; Zalo OA + Zalo Personal channels (Vietnamese messaging app) supported

→ **Probable Vietnamese or Asian market origin.** Unique positioning across 4 projects.

---

## Cốt lõi: 8 core features

### 1. 8-Stage Agent Pipeline
```
context → history → prompt → think → act → observe → memory → summarize
```
Pluggable stages, always-on execution.

**Implementation note (cross-reference với 01-agent-loop.md):**
- "V2 monolithic" legacy path (default)
- "V3 pipeline" enabled via feature flag
- Actual Go Stage classes: ContextStage / ThinkStage / PruneStage / ToolStage / ObserveStage / CheckpointStage / FinalizeStage
- Marketing "8 stages" = conceptual breakdown; implementation = 7 Stage classes

### 2. 4-Mode Prompt System

Full / Task / Minimal / None. Section gating + cache boundary optimization + per-session mode resolution.

### 3. 3-Tier Memory

```
Working (conversation) → Episodic (session summaries) → Semantic (knowledge graph)
```

Progressive loading **L0/L1/L2** (L0 auto-injected).

### 4. Knowledge Vault

- Document registry với `[[wikilinks]]` bidirectional linking
- Hybrid search: FTS (BM25) + semantic (pgvector)
- Filesystem sync

→ **Direct Karpathy LLM Wiki pattern implementation.**

### 5. Agent Teams & Orchestration

- Shared task boards (Kanban)
- Inter-agent delegation: sync / async / bidirectional
- 3 orchestration modes: auto / explicit / manual

### 6. Self-Evolution

3-stage guardrailed pipeline:
```
metrics → suggestions → auto-adapt
```

Agents can refine communication style + domain expertise (CAPABILITIES.md) — **but never change identity, name, or core purpose.**

### 7. Multi-Tenant PostgreSQL

- Per-user workspaces
- Per-user context files
- Encrypted API keys (AES-256-GCM)
- RBAC (admin / operator / viewer)
- Isolated sessions

### 8. Single Binary Go

- ~25 MB static binary
- No Node.js runtime
- <1s startup
- Runs on $5 VPS

---

## 20+ LLM Providers

**Native integrations:**
- Anthropic (native HTTP+SSE with prompt caching)
- OpenAI, OpenRouter, Groq, DeepSeek
- Gemini, Mistral, xAI, MiniMax, DashScope
- **Claude CLI** (stdio+MCP bridge) ← important cross-project
- **Codex** (OpenAI) ← important cross-project
- **ACP** (Anthropic Console Proxy — Claude Code, Codex, Gemini CLI as JSON-RPC 2.0 stdio)
- Any OpenAI-compatible endpoint

**Cross-project insight:** goclaw can use Claude Code (via ACP/Claude CLI provider) as backend. Meaning:
- User's message in Zalo → goclaw → ACP provider → Claude Code with gstack skills installed → response back to Zalo

→ **goclaw = infrastructure; gstack = skills library; siblings can layer.**

---

## 7 Messaging Channels

| Channel | Notes |
|---------|-------|
| Telegram | Forum topics, STT, bot commands |
| Discord | Full bot |
| Slack | Full integration |
| **Zalo OA** | ⚠️ Vietnamese market |
| **Zalo Personal** | ⚠️ Vietnamese market |
| Feishu/Lark | Streaming cards, media |
| WhatsApp | Native via whatsmeow (v3), no WhatsApp API |

→ **Zalo x2 support = strong Vietnamese market signal.**

---

## Production Security

- **5-layer permission system**
- Rate limiting
- Prompt injection detection
- SSRF protection
- AES-256-GCM encryption for API keys
- Shell deny patterns
- Path traversal prevention
- Input guard (detection-only)

→ **Enterprise-grade posture.** Exceeds 3 siblings (which are dev-tool scope).

---

## Desktop Edition "GoClaw Lite"

Native desktop app cho local AI agents (no Docker, no PostgreSQL, no infrastructure):

**Stack:**
- Wails v2 + React v19 + Vite 6 + Tailwind 4
- SQLite database (zero setup)
- Single native app ~30MB
- Build tag: `//go:build sqliteonly`

**Limits cho Lite:**
- Max 5 agents
- Max 1 team (5 members)
- FTS5 text search (no pgvector)
- No channels (only chat)
- No knowledge graph
- No RBAC / multi-tenant

**Install:**
```bash
# macOS
curl -fsSL https://raw.githubusercontent.com/nextlevelbuilder/goclaw/main/scripts/install-lite.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/nextlevelbuilder/goclaw/main/scripts/install-lite.ps1 | iex
```

→ **Use case cho solo founder (Storm Bear persona):** GoClaw Lite = personal AI agent without infrastructure overhead.

---

## 30+ Built-in Tools (8 categories)

| Category | Example tools |
|----------|---------------|
| **Filesystem** | read_file, write_file, edit_file, search, glob |
| **Runtime** | exec (shell), browser (automation) |
| **Web** | web_search (Brave/DDG), web_fetch |
| **Memory** | memory_search, memory_get, knowledge_graph_search |
| **Media** | create_image/audio/video, TTS |
| **Skills** | skill_search (BM25+semantic), use_skill, skill_manage |
| **Teams** | team_tasks, spawn, delegate, message |
| **Automation** | cron, heartbeat, session management |

→ **Anthropic-compatible skill system** built-in.

---

## Quick Start (low-friction path)

```bash
git clone -b main https://github.com/nextlevelbuilder/goclaw.git && cd goclaw
make build
./goclaw onboard        # Interactive setup wizard
source .env.local && ./goclaw
```

Or Docker:
```bash
chmod +x prepare-env.sh && ./prepare-env.sh
# Add at least one GOCLAW_*_API_KEY to .env, then:
make up

# Dashboard: http://localhost:18790
```

### Optional services via WITH_* flags

| Flag | Service |
|------|---------|
| `WITH_BROWSER=1` | Headless Chrome |
| `WITH_OTEL=1` | Jaeger tracing UI |
| `WITH_SANDBOX=1` | Docker code sandbox |
| `WITH_TAILSCALE=1` | Tailscale private network |
| `WITH_REDIS=1` | Redis cache |

---

## License + model

- **License:** CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0)
- **Implication:** Commercial use requires separate license. Non-commercial = OK (personal, learning, open-source)
- **Different from 3 siblings:** ECC + Superpowers + gstack = MIT (permissive). goclaw = stricter.

→ **For Storm Bear's Scrum coaching work** — need to verify if coaching/consulting counts as commercial under CC BY-NC 4.0. Potential blocker for business use.

---

## Cross-connection to sibling projects

| Aspect | ECC | Superpowers | gstack | **goclaw** |
|--------|-----|-------------|--------|--------|
| Layer | Dev assistant | Dev assistant | Dev assistant | **Platform/service** |
| Language | JS/TS | JS/TS | TS (Bun) | **Go** |
| Runtime | Claude Code | Claude Code | Claude Code | **Standalone gateway** |
| License | MIT | MIT | MIT | **CC BY-NC 4.0** |
| Dev OR end user | Dev | Dev | Dev | **End user** (multi-tenant) |
| Channel integrations | None | None | Browser | **7 messaging channels** |
| Memory system | Via hooks | Via skills | Via `/learn` skill | **3-tier built-in** |
| Multi-tenant | ❌ | ❌ | ❌ | **✅ Full multi-tenant PostgreSQL** |
| Uses Claude Code as provider | N/A (is Claude Code ext) | N/A | N/A | **✅ Via ACP/Claude CLI provider** |

→ **Integration pattern identified:** goclaw can host gstack/Superpowers/ECC skills **as backend** via Claude Code provider.

---

## Meta-relevance to Storm Bear vault

Storm Bear vault = Karpathy's LLM Wiki pattern implemented as Obsidian vault + Claude.

goclaw = Karpathy's LLM Wiki pattern implemented as **infrastructure**:
- Knowledge Vault module (`internal/vault/`)
- `[[wikilinks]]` native syntax
- Hybrid search (BM25 + pgvector)
- Filesystem sync
- L0 auto-injection (L0 = "most relevant context, always injected")

**Implication cho Storm Bear:**
- **Current:** vault = 1 user (me) + manual wiki maintenance
- **Potential:** deploy goclaw, import vault as Knowledge Vault → multi-tenant wiki with search + agent access
- **Scale path:** Storm Bear's coaching team could have shared vault via goclaw's multi-tenant model
- **Caveat:** CC BY-NC 4.0 license = commercial use needs clarification

---

## Open questions resolved

- ✅ Q5: Claude CLI + Codex + ACP are providers in goclaw → **Integration possible (gstack skills as backend via ACP)**
- ✅ Q9: GoClaw Lite use case cho solo founder → personal AI agents without infrastructure overhead
- ✅ Q10: Zalo x2 channels + Vietnamese README → **Vietnamese market signal confirmed**
- ✅ Q11: Vietnamese translation official → author bias toward VN/Asian market

## Open questions raised

- ⏸ CC BY-NC 4.0 commercial usage clarification (Storm Bear coaching = commercial?)
- ⏸ Skills Runtime (`internal/skills/`) format vs ECC/Superpowers/gstack SKILL.md — importable?
- ⏸ Self-Evolution guardrails exact scope (what can't be auto-adapted?)
- ⏸ Knowledge Vault query/search API — usable outside goclaw as library?
- ⏸ Desktop edition vs Server edition — use case split cho Storm Bear team?

---

## Cross-references

- [[(C) CLAUDE.md + Architecture summary]]
- [[(C) Key Docs deep dive]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) README summary.md`
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) README summary.md`
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) README summary.md`

## Citations

- `00 Sources/goclaw/README.md` (full file, 338 lines)
- OpenClaw acknowledgment: line 324
- License: line 328
- Karpathy LLM Wiki pattern = implicit in "Knowledge Vault với wikilinks" description (line 246-252)
