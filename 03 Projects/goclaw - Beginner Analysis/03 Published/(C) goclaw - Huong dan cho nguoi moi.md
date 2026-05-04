# goclaw — Hướng dẫn cho người mới

> **For team / Cho team:** Đây là hướng dẫn tổng hợp để bắt đầu với **goclaw** — Multi-Tenant AI Agent Platform viết bằng Go. **Khác domain** với ECC/Superpowers/gstack (đây là platform/infrastructure, không phải Claude Code skills). Đọc 1 lần ~30 phút, đủ để deploy GoClaw Lite hoặc Standard + chạy agent đầu tiên.
>
> **Tác giả wiki:** Storm Bear, dựa trên `nextlevelbuilder/goclaw` (v3.x, CHANGELOG tới 2026).
> **Ngày:** 2026-04-18 | **Phiên bản:** v1
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)
> **Note:** goclaw có **official Vietnamese README** (`_readmes/README.vi.md`) — author bias VN/Asian market.

---

## 📋 Mục lục

1. [Tại sao đọc cái này](#tại-sao-đọc-cái-này)
2. [Part 1: goclaw là gì + positioning](#part-1-goclaw-là-gì--positioning)
3. [Part 2: 8 core features](#part-2-8-core-features)
4. [Part 3: Lite vs Standard edition](#part-3-lite-vs-standard-edition)
5. [Part 4: Setup roadmap 1 tuần](#part-4-setup-roadmap-1-tuần)
6. [Part 5: 3-Tier Memory + Knowledge Vault deep dive](#part-5-3-tier-memory--knowledge-vault-deep-dive)
7. [Part 6: Meta-relevance tới Storm Bear vault](#part-6-meta-relevance-tới-storm-bear-vault)
8. [Part 7: FAQ thường gặp](#part-7-faq-thường-gặp)
9. [Part 8: Resources & References](#part-8-resources--references)

---

## Tại sao đọc cái này

### Ai nên đọc / Who should read

- **Team lead / Ops engineer** cần deploy AI agent platform cho multiple users
- **Founder** muốn ship AI agent service tới end users (Zalo/Telegram/WhatsApp)
- **Solo founder** muốn personal AI agent without infrastructure (→ GoClaw Lite)
- **Storm Bear vault maintainer** muốn consider goclaw's Knowledge Vault as potential backend
- **Anyone** đã đọc 3 sibling guides (ECC/Superpowers/gstack) muốn hiểu platform-tier alternative

### Bạn sẽ có gì sau khi đọc / What you'll get

- Hiểu **positioning** của goclaw vs 3 siblings (agent-as-service vs agent-as-assistant)
- Biết **8 core features** (pipeline, memory, vault, multi-tenant, LLM providers, channels, security, teams)
- Hiểu **Lite vs Standard edition** — pick cho use case
- **Setup roadmap 1 tuần** từ zero → deploy Lite hoặc Standard + agent đầu tiên
- Hiểu **3-Tier Memory + Knowledge Vault** — potentially Storm Bear vault's backend

### Không phải là gì / What this is NOT

- ❌ Không phải tutorial cài Go / PostgreSQL / Docker từ đầu
- ❌ Không cover toàn bộ 20+ LLM providers chi tiết — xem docs.goclaw.sh
- ❌ Không cover 7 messaging channels setup (chỉ overview)
- ❌ Không cover advanced: custom tools, MCP bridge, scheduled cron

---

## Part 1: goclaw là gì + positioning

### TL;DR

**goclaw** là **Multi-Tenant AI Agent Platform** viết bằng **Go**, do `@nlb_io` (nextlevelbuilder) build. Single binary ~25MB, chạy trên $5 VPS, multi-tenant PostgreSQL, 20+ LLM providers, 7 messaging channels, MIT equivalent (CC BY-NC 4.0 — non-commercial).

**Vietnamese signal:** Zalo OA + Zalo Personal channels + official `README.vi.md` + language-matching agent behavior.

### Positioning critical

**goclaw operates on DIFFERENT architectural layer than ECC/Superpowers/gstack:**

| Layer | Purpose | Examples |
|-------|---------|----------|
| **Agent-as-assistant** (dev workflow) | Enhance Claude Code cho individual developers | ECC, Superpowers, gstack |
| **Agent-as-service** (end-user platform) | Multi-tenant AI agent service cho end users | **goclaw** |

→ **Không compete với 3 siblings.** Khác tier.

**Integration pattern:** goclaw có `Claude CLI` + `ACP` (Anthropic Console Proxy) + `Codex` là **LLM providers**. Nghĩa là goclaw có thể **invoke gstack/Superpowers/ECC skills trong backend** qua Claude Code session.

User story:
```
User message in Zalo
  → goclaw gateway
  → ACP provider (spawn Claude Code with gstack installed)
  → Claude Code runs /cso security audit
  → response → Zalo
```

### Khác ECC/Superpowers/gstack ở đâu

| Axis | ECC | Superpowers | gstack | **goclaw** |
|------|-----|-------------|--------|------------|
| Who uses | Individual dev | Individual dev | Individual dev | **End users (multi-tenant)** |
| Deployment | Local tool | Local tool | Local tool | **Self-hosted service** |
| Language | JS/TS | JS/TS | TS (Bun) | **Go** |
| Multi-user | ❌ | ❌ | `--team` shares repo | **✅ Full multi-tenant PG** |
| Channels | N/A | N/A | N/A | **7 (Telegram, Discord, Slack, Zalo x2, Feishu, WhatsApp)** |
| Memory | Manual hooks | Iteration logs | `/learn` skill | **3-tier auto (Working/Episodic/Semantic) + Knowledge Vault** |
| License | MIT | MIT | MIT | **CC BY-NC 4.0** (non-commercial) |

### Lịch sử ngắn

- Inspired by **OpenClaw** (cited trong README Acknowledgments)
- Author: **nextlevelbuilder** (`@nlb_io` on X), probably Vietnamese or Asian market
- Version: **v3.x** mainline + **lite-v1.x.x** desktop edition (parallel track)
- Aggressive development (no exact cadence verified)

---

## Part 2: 8 core features

### 1. 8-Stage Agent Pipeline

Internal execution loop per agent request:
```
context → history → prompt → think → act → observe → memory → summarize
```

Implementation: 7 Stage classes (ContextStage/ThinkStage/PruneStage/ToolStage/ObserveStage/CheckpointStage/FinalizeStage). Pluggable, always-on, max 20 iterations per request.

→ **Đọc sâu:** [[../02 Wiki/(C) 8-Stage Agent Pipeline]]

**Important:** Đây là **agent runtime loop**, không phải dev workflow (khác gstack's Sprint Pipeline + Superpowers's 7-Stage Workflow).

### 2. 4-Mode Prompt System

Full / Task / Minimal / None. Section gating + cache boundary optimization + per-session mode resolution.

### 3. 3-Tier Memory

```
Working (conversation) → Episodic (session summaries) → Semantic (knowledge graph)
```

Progressive loading: L0 auto-inject (always), L1/L2 on-demand.

Async consolidation workers (episodic/semantic/**dreaming**) promote lower tiers to higher.

→ **Đọc sâu:** [[../02 Wiki/(C) 3-Tier Memory + Knowledge Vault]]

### 4. Knowledge Vault

Document registry với:
- `[[wikilinks]]` bidirectional linking
- Hybrid search: BM25 (FTS) + pgvector (semantic)
- Filesystem sync (markdown files on disk + DB index)

→ **Đây là Karpathy's LLM Wiki pattern implemented as infrastructure.** Meta-relevant tới Storm Bear vault.

### 5. Multi-Tenant Architecture

- Per-tenant workspace (filesystem)
- Per-user context files
- AES-256-GCM encrypted API keys
- RBAC (admin / operator / viewer)
- Isolated sessions
- Per-tenant rate limiting
- Tenant-scope guards (`WHERE tenant_id = $N` mandatory)

→ **Đọc sâu:** [[../02 Wiki/(C) Multi-Tenant Architecture]]

### 6. 20+ LLM Providers

| Provider family | Examples |
|-----------------|----------|
| Anthropic native | Anthropic HTTP+SSE (prompt cache) |
| OpenAI-compatible | OpenAI, OpenRouter, DeepSeek, Groq, Mistral, xAI, MiniMax |
| Google | Gemini |
| Chinese | DashScope (Alibaba Qwen) |
| **Claude Code integration** | **Claude CLI (stdio+MCP), ACP, Codex** |

→ **Claude CLI + ACP = allows running gstack/Superpowers/ECC skills inside goclaw.**

### 7. 7 Messaging Channels

- Telegram (forum topics, STT, bot commands)
- Discord
- Slack
- **Zalo OA** (Vietnamese)
- **Zalo Personal** (Vietnamese)
- Feishu / Lark (streaming cards)
- WhatsApp (native via whatsmeow v3)

### 8. Agent Teams & Orchestration

Lead + Members + Task Board + Mailbox. 3 orchestration modes (auto/explicit/manual). 3 delegation modes (sync/async/bidirectional). `BatchQueue[T]` generic cho result aggregation.

→ **Đọc sâu:** [[../02 Wiki/(C) Agent Teams and Orchestration]]

### Plus: 30+ built-in tools + 5-layer defense security + self-evolution + event-driven architecture

---

## Part 3: Lite vs Standard edition

### GoClaw Lite (Desktop)

**Cho ai:** Solo founder, personal AI agent, không cần infrastructure.

**Stack:**
- Single native app (Wails v2 + React + Vite + Tailwind)
- SQLite database (zero setup)
- ~30MB
- Auto-update from GitHub Releases

**Install:**
```bash
# macOS
curl -fsSL https://raw.githubusercontent.com/nextlevelbuilder/goclaw/main/scripts/install-lite.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/nextlevelbuilder/goclaw/main/scripts/install-lite.ps1 | iex
```

**Limits:**
- Max 5 agents
- Max 1 team (5 members)
- Max 50 sessions
- No channels (chat only)
- No knowledge graph
- No RBAC / multi-tenant
- FTS5 text search (no pgvector)

### Standard (Server)

**Cho ai:** Team/org, multi-user, production, channel integrations.

**Stack:**
- Docker Compose hoặc binary
- PostgreSQL 18 + pgvector
- Web dashboard + HTTP API + WebSocket RPC
- Channels: Telegram/Discord/Slack/Zalo/Feishu/WhatsApp
- Desktop size: single binary ~25MB + PG container

**Install (Docker):**
```bash
git clone -b main https://github.com/nextlevelbuilder/goclaw.git && cd goclaw
chmod +x prepare-env.sh && ./prepare-env.sh
# Add at least one GOCLAW_*_API_KEY to .env
make up
# Dashboard: http://localhost:18790
```

**Optional services (WITH_* flags):**
- `WITH_BROWSER=1` — Headless Chrome
- `WITH_OTEL=1` — Jaeger tracing
- `WITH_SANDBOX=1` — Docker sandbox for untrusted code
- `WITH_TAILSCALE=1` — Private network
- `WITH_REDIS=1` — Redis cache

### Which to pick

| Use case | Lite | Standard |
|----------|------|----------|
| Solo founder, personal agent | ✅ | overkill |
| Storm Bear self-use | ✅ | |
| Team of 2-5 devs | | ✅ |
| Multi-tenant SaaS | | ✅ |
| Zalo/Telegram bot deploy | | ✅ |
| Development / testing | ✅ | ✅ |
| Air-gapped / no internet | ✅ | ✅ (self-host) |

→ **Start với Lite** nếu đơn lẻ. **Scale lên Standard** khi team > 1.

---

## Part 4: Setup roadmap 1 tuần

### Day 1: Pick edition + install

**Lite path (recommended for Storm Bear pilot):**
```bash
# macOS
curl -fsSL https://raw.githubusercontent.com/nextlevelbuilder/goclaw/main/scripts/install-lite.sh | bash

# Launch app (should auto-launch post-install)
```

**Standard path:**
```bash
git clone -b main https://github.com/nextlevelbuilder/goclaw.git && cd goclaw
chmod +x prepare-env.sh && ./prepare-env.sh
# Edit .env to add your Anthropic/OpenAI API key
make up
# Open http://localhost:18790
```

### Day 2: First agent

**Via onboarding wizard** (Lite hoặc Standard):
1. Pick provider (Anthropic / OpenAI / etc.)
2. Paste API key
3. Create first agent (vd: "Researcher")
4. Test chat

### Day 3: Knowledge Vault setup

Populate Knowledge Vault:
```bash
# Drop markdown files into vault directory
# Lite: ~/.goclaw/workspace/vault/
# Standard: /app/workspace/vault/ (inside Docker volume)
```

Files với `[[wikilinks]]` auto-indexed. Agent can query via `memory_search` tool.

**Storm Bear experiment:**
```bash
cp -r "/Users/Cvtot/KJ OS Template/03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/" \
      ~/.goclaw/workspace/vault/
# Restart goclaw
# Query agent: "What are hooks in Claude Code?"
# Agent should retrieve from ECC wiki via vault
```

### Day 4-5: Team setup (Standard only)

Create team via dashboard:
1. Admin → Teams → Create
2. Add lead agent (e.g., "CrewLead")
3. Add members (e.g., "Researcher", "Writer", "Reviewer")
4. Test team workflow:
   - User request → Lead creates tasks → Members claim → Results aggregated

### Day 6: Channel integration (Standard only)

**Telegram example:**
1. Create bot via BotFather
2. Admin → Channels → Add Telegram
3. Paste bot token
4. Restart
5. Message bot — routes to agent

### Day 7: Assess

**Success criteria:**
- ✅ Agent responds to chat
- ✅ Vault queries return relevant results (nếu populated)
- ✅ Team workflow produces aggregated output (Standard)
- ✅ Channel integration works (Standard)

**Decide:**
- Keep goclaw → rollout to team
- Blocker = CC BY-NC 4.0 license (commercial use?) → clarify
- Not fit → uninstall, try different approach

---

## Part 5: 3-Tier Memory + Knowledge Vault deep dive

### Why this matters cho Storm Bear

goclaw's memory + vault architecture = **Karpathy's LLM Wiki pattern implemented as infrastructure**.

Storm Bear vault hiện tại:
- File-based (Obsidian)
- Manual wiki maintenance
- Single user (you)
- `[[wikilinks]]` central

goclaw as potential backend:
- DB-backed với auto-consolidation
- Filesystem sync (retain file-based workflow)
- Multi-user capable
- `[[wikilinks]]` native

**Convergent implementations, complementary.**

### 3-tier memory model

```
┌────────────────────────────────────────┐
│ Tier 1: Working Memory                 │
│ • Current conversation                 │
│ • Recent messages, tool calls          │
│ • In-memory buffer                     │
└────────────────────────────────────────┘
          ↓ (consolidation on session end)
┌────────────────────────────────────────┐
│ Tier 2: Episodic Memory                │
│ • Past sessions as summaries           │
│ • Generated by episodic worker         │
│ • Searchable via memory_search         │
└────────────────────────────────────────┘
          ↓ (semantic + dreaming workers)
┌────────────────────────────────────────┐
│ Tier 3: Semantic Memory (KG)           │
│ • Extracted facts, entities, edges     │
│ • Knowledge graph                      │
│ • Queryable via knowledge_graph_search │
└────────────────────────────────────────┘
```

### Progressive loading L0/L1/L2

- **L0:** auto-inject top-N semantic results every request (free, cheap)
- **L1:** on-demand search (tool call, costs a bit)
- **L2:** deep KG traversal (expensive)

→ Balance cost vs recall.

### Knowledge Vault mechanics

**Storage dual-representation:**
- DB: BM25 index + embeddings (pgvector)
- Filesystem: markdown files (portable, git-friendly)

**Sync:** `internal/vault/` watches filesystem, updates DB indexes on change.

**Search hybrid:**
```
final_score = α * BM25_score + β * semantic_score
```

### Recipe: Import Storm Bear vault

**(Hypothetical — blocked by CC BY-NC 4.0 unless commercial clarified)**

```bash
# Assume Lite installed
cd ~/.goclaw/workspace/vault/

# Symlink or copy Storm Bear's 02 Wiki/ into vault
ln -s "/Users/Cvtot/KJ OS Template/03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki" "./ecc-wiki"
ln -s "/Users/Cvtot/KJ OS Template/03 Projects/Superpowers - Beginner Analysis/02 Wiki" "./superpowers-wiki"
ln -s "/Users/Cvtot/KJ OS Template/03 Projects/gstack - Beginner Analysis/02 Wiki" "./gstack-wiki"
ln -s "/Users/Cvtot/KJ OS Template/03 Projects/goclaw - Beginner Analysis/02 Wiki" "./goclaw-wiki"

# Restart goclaw
# Vault auto-indexes all 4 wiki folders
# [[wikilinks]] cross-project resolved

# Test:
# User: "Compare ECC hooks với Superpowers skills"
# Agent: retrieves from multiple wikis via hybrid search + synthesizes
```

→ **Potential outcome:** Storm Bear vault queryable via natural language agent, với auto-consolidation learning new patterns over time.

---

## Part 6: Meta-relevance tới Storm Bear vault

### Convergence với LLM Wiki pattern

Karpathy's LLM Wiki principle:
> "Instead of re-deriving knowledge từ RAG mỗi query, LLM incrementally builds maintained wiki — summaries, entity pages, cross-references, evolving synthesis."

Storm Bear vault implementation:
- Obsidian + manual curation
- 4 projects built via routine `llm-wiki-routine`
- Cross-project synthesis compounds

goclaw's Knowledge Vault:
- Multi-tenant infrastructure
- Auto-consolidation workers
- Same `[[wikilinks]]` syntax
- Hybrid search (BM25 + pgvector)

**Hypothetical migration paths:**

#### Path 1: Keep current, add goclaw-Lite as query layer

- Storm Bear vault stays file-based (Obsidian primary)
- Deploy goclaw Lite on Storm Bear's machine
- Symlink 4 projects' `02 Wiki/` into goclaw vault
- Use goclaw agents cho natural language queries over vault
- **Pro:** Keep current workflow. Add agent query capability.
- **Con:** Dual-source (Obsidian + goclaw DB). Potential drift.

#### Path 2: Full migration to goclaw Standard

- Deploy goclaw Standard (Docker + PostgreSQL)
- Import all vault content as starting corpus
- Team Storm Bear coaching operates via goclaw UI
- Obsidian becomes read-only mirror via FS sync
- **Pro:** Multi-user, production-grade, channels
- **Con:** CC BY-NC 4.0 license — commercial coaching = needs clarification
- **Con:** Infrastructure overhead

#### Path 3: Stay with current

- Storm Bear vault stays single-user file-based
- No goclaw integration
- **Pro:** Zero new dependency. Simple.
- **Con:** No multi-user. No natural language query capability.

### Storm Bear recommendation

**Pilot Path 1** (Lite as query layer) trong 1 tuần:
- Low commitment (just install Lite)
- Test if agent-vault interaction adds value
- If yes, consider Path 2 post-license-clarification
- If no, uninstall Lite, zero lost work

---

## Part 7: FAQ thường gặp

### Q1: goclaw replace Claude Code không?

Không. goclaw + Claude Code **work together** — goclaw can use Claude CLI + ACP làm providers. Means Claude Code + gstack skills run INSIDE goclaw.

### Q2: CC BY-NC 4.0 license — commercial work có OK không?

**Unclear without legal review.** Creative Commons Attribution-NonCommercial:
- Personal use: ✅
- Open-source contributions: ✅
- Internal tooling for non-profit: ✅
- Commercial SaaS using goclaw: likely ❌ requires separate license
- Coaching business: **gray area — consult lawyer**

Contact author (`@nlb_io`) for commercial licensing clarity.

### Q3: Go 1.26 + PG 18 + Docker — quá nặng cho solo?

Đó là vì sao **GoClaw Lite tồn tại**. Lite chỉ Wails + SQLite, 30MB app, zero infrastructure.

Standard (PG + Docker) cho team/production.

### Q4: Vietnamese market signal — confirmed author Vietnamese?

Tổng hợp signals:
- `_readmes/README.vi.md` official
- Zalo OA + Zalo Personal channels (Vietnamese messaging apps)
- `catalog_vi.go` i18n support
- Language-matching policy ("Always respond in user's language. If Vietnamese, respond Vietnamese.")

→ **Strong Vietnamese/Asian market signal.** Author likely VN or regional.

### Q5: Mix goclaw với 3 siblings OK?

**Different layers, should coexist:**
- Dev: use Claude Code + gstack (or Superpowers hoặc ECC) cho own dev work
- Deploy: use goclaw làm end-user agent platform
- Integration: goclaw's ACP provider spawns Claude Code sessions với gstack skills

### Q6: goclaw support Zalo — quan trọng cho VN market?

Có. Zalo là messaging app dominant ở VN. Bot via Zalo OA (official account) = reach VN users natively.

### Q7: Security posture enterprise-ready?

5-layer defense + AES-256-GCM + tenant-scope guards + RBAC + rate limiting + audit logs + Docker sandbox.

Enterprise-grade. Exceeds 3 siblings (dev-tool scope).

### Q8: GoClaw Lite vs Claude Desktop (Anthropic)?

Different:
- Claude Desktop = Anthropic's Claude UI
- GoClaw Lite = AI agent runtime với own agents, skills, memory, local-first

GoClaw Lite run local, not sending data to Anthropic beyond LLM calls (encrypted keys).

### Q9: Anthropic skill format compatibility?

Skills folder có docx/pdf/pptx/xlsx/skill-creator — looks like Anthropic official skill library ported.

**Hypothesis:** goclaw's `internal/skills/` loader reads SKILL.md format compatible với Anthropic. Potentially run gstack/Superpowers/ECC skills directly (not verified).

### Q10: Storm Bear should pilot goclaw?

**Yes, Lite edition, 1 week.** Low commitment, high learning signal.

Commercial-use question = resolve before Standard deployment for coaching business.

---

## Part 8: Resources & References

### Repo + docs

- **Repo:** https://github.com/nextlevelbuilder/goclaw
- **Docs:** https://docs.goclaw.sh
- **Twitter:** https://x.com/nlb_io
- **Vietnamese README:** `_readmes/README.vi.md`
- **OpenClaw (inspiration):** https://github.com/openclaw/openclaw

### Numbered docs in repo

- `docs/00-architecture-overview.md` — component diagram + module map
- `docs/01-agent-loop.md` — 8-stage pipeline detail
- `docs/02-providers.md` — 20+ LLM providers
- `docs/03-tools-system.md` — 30+ tools
- `docs/04-gateway-protocol.md` — WebSocket + HTTP API
- `docs/05-channels-messaging.md` — 7 channels
- `docs/06-store-data-model.md` — PostgreSQL schema
- `docs/07-bootstrap-skills-memory.md` — skills + memory init
- `docs/08-scheduling-cron.md` — scheduled tasks
- `docs/09-security.md` — 5-layer defense
- `docs/10-tracing-observability.md` — OTel export
- `docs/11-agent-teams.md` — team model deep
- `docs/12-extended-thinking.md` — Anthropic extended thinking
- `docs/13-ws-team-events.md` — WebSocket team events
- `docs/14-skills-runtime.md` — Docker runtime container
- `docs/15-core-skills-system.md` — 5-tier skill hierarchy
- `docs/16-skill-publishing.md` — skill publishing
- `docs/17-changelog.md` — full changelog
- `docs/18-http-api.md` — REST API reference
- `docs/19-websocket-rpc.md` — WebSocket RPC reference

### Wiki Storm Bear (đọc sâu)

- [[../02 Wiki/(C) README summary]]
- [[../02 Wiki/(C) CLAUDE.md + Architecture summary]]
- [[../02 Wiki/(C) Key Docs deep dive]]
- [[../02 Wiki/(C) 8-Stage Agent Pipeline]]
- [[../02 Wiki/(C) 3-Tier Memory + Knowledge Vault]]
- [[../02 Wiki/(C) Multi-Tenant Architecture]]
- [[../02 Wiki/(C) Agent Teams and Orchestration]]
- [[(C) Agent framework taxonomy]] — agent-as-assistant vs agent-as-service positioning

### Related ecosystem

- **OpenClaw:** https://github.com/openclaw/openclaw — cited inspiration, 247K stars (per gstack README)
- **Karpathy's LLM Wiki pattern:** the founding principle of Storm Bear vault
- **pgvector:** PostgreSQL extension for vector similarity
- **Wails v2:** Go + React desktop framework (used cho GoClaw Lite)

### License

- CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International)
- Allows: personal use, attribution, modification, sharing non-commercially
- Restricts: commercial use without separate license
- **Contact author for commercial terms**

### Khi gặp issue

- **Docker build fails:** `make reset` wipes volumes + rebuild
- **PG connection error:** verify `GOCLAW_*_API_KEY` in `.env`
- **Skills not discovered:** check Docker image variant (minimal vs full)
- **Port conflict:** configure `GOCLAW_PORT`
- **Lite SQLite corruption:** backup `~/.goclaw/data/`, restart (or reset)
- **Windows Node.js + Bun pipe bug:** not goclaw-specific, but if using gstack in parallel

---

## Closing thoughts — goclaw vị trí trong ecosystem

goclaw không compete với ECC/Superpowers/gstack — đó là **platform tier** vs **dev tool tier**. 

**Nếu bạn là:**
- **Dev cần enhance Claude Code:** pick ECC, Superpowers, hoặc gstack
- **Solo founder muốn personal AI agent:** GoClaw Lite
- **Team deploy AI service cho end users:** goclaw Standard
- **Storm Bear vault maintainer:** pilot Lite, assess Path 1 (vault query layer)

**goclaw unique strengths:**
1. Multi-tenant production platform
2. Vietnamese market support (Zalo x2)
3. 3-tier memory + Knowledge Vault = Karpathy pattern infrastructure
4. 20+ LLM providers including Claude CLI + ACP
5. 7 messaging channels
6. 5-layer enterprise security
7. Single Go binary portability
8. Self-evolution with guardrails
9. Agent teams first-class

**Blocker to watch:**
- CC BY-NC 4.0 license — commercial use clarity

→ **Next action cho Storm Bear:**
1. Install GoClaw Lite (30s, macOS/Windows)
2. Chat với first agent (5 min)
3. Drop 1 project's wiki into vault dir (10 min)
4. Test agent query via vault (15 min)
5. Assess: continue (→ Path 2 Standard) or stop (uninstall, stick with Obsidian)

---

> **Wiki maintained by Storm Bear.** goclaw = adjacent-domain LLM Wiki project (4th trong routine runs). Unique because operates on different architectural layer. Nếu fact sai hoặc outdated (aggressive dev), ping để fix.
