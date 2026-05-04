# (C) Core Product — n8n Workflow Automation Platform

## What it is

**n8n** (pronounced "n-eight-n", short for "nodemation") is a fair-code workflow automation platform that combines:
- **Visual canvas building** (drag-and-drop low-code/no-code)
- **Custom code escape hatch** (TypeScript/JavaScript inline in nodes)
- **Self-host or cloud** (n8n.cloud managed SaaS commercial)
- **400+ integrations** with external services
- **Native AI capabilities** (6 agent types + 16 LLM providers + 11 vector stores + 8 memory backends)
- **Bidirectional MCP** (consume external MCP servers + expose self as MCP server)

## Architecture (high-level)

**Runtime layers:**

1. **Workflow engine** — TypeScript-based execution engine (Bun-compatible per ecosystem signal; not yet 100%-verified at v56 probe)
2. **Node library** — 400+ pre-built integration nodes (Slack, GitHub, Jira, Linear, Notion, Airtable, Google Sheets, etc.)
3. **AI agent layer** — 6 named agent node types orchestrating LLM calls + vector retrieval + memory
4. **Trigger layer** — webhooks, schedules, MCP Server Trigger, polling, HTTP requests
5. **Persistence** — workflow state + execution history + credentials (encrypted)

**Distribution surfaces (5+ confirmed at v56 probe):**

1. `npm install n8n` (CLI runtime — `npx n8n` runs locally on port 5678)
2. Docker `n8nio/n8n` (containerized self-host)
3. n8n.cloud managed SaaS (commercial subscription)
4. Self-host source build (clone + npm-build)
5. Docker Desktop (templated install)

## AI capabilities (Source 4 — verbatim from docs.n8n.io/advanced-ai)

### 6 AI Agent node types

| Agent Type | Use case |
|---|---|
| Conversational Agent | Multi-turn chat with memory |
| OpenAI Functions Agent | Structured function-calling via OpenAI native protocol |
| Plan and Execute Agent | High-level planner + low-level executor (LangChain pattern) |
| ReAct Agent | Reasoning + Acting interleaved (Yao et al. 2022 lineage) |
| SQL Agent | Natural language → SQL → DB execution |
| Tools Agent | Generic tool-calling abstraction |

### 16 native LLM providers

OpenAI / Anthropic / Google Gemini / Azure OpenAI / Cohere / Mistral Cloud / DeepSeek / Groq / Ollama / Google Vertex / Alibaba Cloud / Moonshot Kimi / Lemonade / OpenRouter / Vercel AI Gateway / xAI Grok

**Notable:** No LiteLLM dependency (unlike browser-use v41 which uses LiteLLM as universal-LLM-fork) — n8n integrates each provider natively. Pattern #28 native-multi-provider sub-axis 16th data point.

### 11 vector store integrations (corpus-first broadest)

Azure AI Search / Chroma / Milvus / MongoDB Atlas / PGVector / Pinecone / Qdrant / Redis / Supabase / Weaviate / Zep

### 8 memory backend types

Simple Memory (Buffer Window) / Chat Memory Manager / Motorhead / MongoDB Chat Memory / Redis Chat Memory / Postgres Chat Memory / Xata / Zep

### MCP support — BIDIRECTIONAL (corpus-first at T2)

**MCP Client node** — n8n consumes external MCP servers as additional tool-providers within workflows (Pattern #18 Layer 1 universal-protocol consumer)

**MCP Server Trigger node** — n8n exposes itself as MCP server for OTHER agents to consume (e.g., Claude Code can call n8n workflow as a tool via MCP) — corpus-first explicit MCP-server-trigger node naming

This bidirectional capability puts n8n in a unique architectural position: it's both a workflow-automation-PLATFORM and an MCP-tool-PROVIDER for other agents.

## Workflow execution model

1. **Trigger fires** — webhook / schedule / MCP server call / polling / manual
2. **Visual graph executes** — node-by-node, data flows along connections
3. **AI nodes orchestrate** — agent + LLM + vector + memory + tools
4. **External integrations execute** — 400+ services (REST APIs, OAuth flows, webhooks)
5. **Custom code fallback** — TypeScript node for arbitrary logic
6. **Persistence + history** — execution traces + workflow versions

## Scale + maturity signals

- **185,728 stars** at probe (3rd-largest in corpus after 2 outside-scope aggregators)
- **57,155 forks** (30.8% — high for T2 platform; suggests active fork-and-customize community)
- **1,580 open issues** (active triage churn typical of mature commercial platform)
- **Created 2019-06-22** — 7-year-mature (2nd-oldest subject in corpus)
- **Daily updates** (pushed 2026-04-27 today)
- **400+ integrations** (corpus-record breadth at T2)

## Repository structure (TypeScript monorepo signals)

- Default branch `master` (rare in corpus; legacy convention preserved)
- Repo size 476 MB (large)
- Topic mcp + mcp-client + mcp-server (deliberate MCP-positioning in repo metadata)

(Detailed monorepo package layout NOT enumerated per EXTREME primitive-count cite-not-replicate discipline; refer to repo directly for `packages/` breakdown.)

## Pattern Library implications

| Pattern | n8n contribution |
|---|---|
| #18 Agent Runtime Standardization | **STRONGEST T2 evidence in corpus** — bidirectional MCP at T2; Layer 0 horizontal-aggregation N=2 (gh-aw v48 + n8n v56) |
| #28 Multi-Provider AI Support | 16 native LLM providers (no LiteLLM); 16th-largest native multi-provider in corpus |
| #2 Distribution Evolution | 5+ surfaces (npm + Docker + cloud + self-host + Docker Desktop) |
| #69 Primitive-count taxonomy | 6th EXTREME-tier wiki subject |
| #27 Community-Viral | 185K stars / 7 years sustained-organic ≈ 71 stars/day (sustained-mature-organic sub-path) |

## Out-of-scope at v56

- 400+ integration enumeration (cite-not-replicate)
- Workflow execution engine internals (`packages/cli/` source dive)
- n8n.cloud-vs-self-host feature delta (deferred to Q4 OPEN-QUESTIONS)
- Bun runtime confirmation (ecosystem signal only at v56)
