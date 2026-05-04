# (C) Frameworks + Protocols Cluster Summary — Lessons 02, 11, 12, 14

> Nguồn: Fetched via raw.githubusercontent.com 2026-04-18
> Coverage: 4 infrastructure/framework lessons (frameworks landscape, protocols, context engineering, MAF)

## TL;DR

4 lessons form the **infrastructure spine** của curriculum. Lesson 02 answers "which tool", Lesson 11 answers "which protocol", Lesson 12 answers "how to manage info flow", Lesson 14 answers "Microsoft's consolidation". Together = **production-readiness kit**. Critical for Tier 2 platform deployment (goclaw territory) + Tier 1 advanced use.

---

## Lesson 02: Exploring AI Agentic Frameworks

### 3 Frameworks covered

| Framework | Focus | Design | Strength |
|-----------|-------|--------|----------|
| **AutoGen** | Event-driven, distributed multi-agent | Actor model + async messaging | Experimentation, sophisticated prototyping |
| **Semantic Kernel** | Enterprise production apps | Modular connectors + plugins | Single/multi-agent + LLM abstraction |
| **Azure AI Agent Service** | Cloud deployment | Platform service integrated với Foundry | Enterprise security, Bing Search, Azure Functions |

### When to use which

- **AutoGen** — rapid experimentation, code generation, data analysis
- **Semantic Kernel** — production apps with modular reusable components
- **Azure AI Agent Service** — enterprise needing Azure ecosystem integration

### Integration strategy

> "Build in Semantic Kernel, deploy via Azure AI Agent Service for optimal enterprise implementation."

→ **Hybrid path** recommended, not single-framework.

### Code samples

- Python: Semantic Kernel auto-function-calling
- AutoGen: Multi-agent collaboration via GroupChatManager
- Azure AI Agent Service: thread-based conversation management

### Key takeaway L02

Framework choice = **function of deployment target + experimentation maturity**. Not a "best" framework; **best fit for context**. Microsoft pushes hybrid SK-to-Azure pipeline for enterprise.

---

## Lesson 11: Agentic Protocols (MCP, A2A, NLWeb)

### 3 Protocols, 3 relations

| Protocol | Connects | Origin | Purpose |
|----------|----------|--------|---------|
| **MCP (Model Context Protocol)** | LLM ↔ tools | Anthropic | Standardized tool/resource/prompt access |
| **A2A (Agent-to-Agent)** | Agent ↔ agent | Google | Cross-vendor agent collaboration |
| **NLWeb (Natural Language Web)** | Agent ↔ website | Microsoft | Website-level AI accessibility |

### MCP detail

Client-server architecture. Hosts (LLM apps) connect to servers exposing 3 capabilities:
- **Tools** — discrete functions agents can invoke
- **Resources** — read-only data items
- **Prompts** — predefined templates

### A2A detail

Different AI agents communicate across organizations + tech stacks. Each runs own LLM + internal tools. Built-in authentication. Enables **cross-vendor collaboration** unlike MCP's intra-stack focus.

### NLWeb detail

Transforms websites → AI-accessible systems:
- Processes NL questions through embedding models + vector DBs
- Simultaneously functions as MCP server (AI agents can query website directly)
- **Dual role:** natural language interface for humans + machine interface for agents

### Tiered ecosystem

> "MCP connects agents to tools, A2A connects agents to each other, NLWeb makes web content agent-accessible."

| Layer | Protocol | Example |
|-------|----------|---------|
| **Tools** | MCP | Claude Desktop connects to filesystem MCP server |
| **Peers** | A2A | Agent A (vendor X) calls Agent B (vendor Y) via A2A |
| **Web** | NLWeb | AI agent queries Microsoft Learn via NLWeb |

### Why protocols matter

- **MCP** — eliminates static API coding, seamless model switching
- **A2A** — enables multi-vendor systems with built-in auth
- **NLWeb** — grounds AI in web content, prevents hallucinations

### Key takeaway L11

3 protocols = **tiered infrastructure** for agentic ecosystem. MCP widely adopted (Claude Code uses heavily). A2A emerging. NLWeb very new. **Knowing protocols = knowing what agents CAN connect to**.

---

## Lesson 12: Context Engineering for AI Agents

### Definition

> "Managing dynamic information flow to ensure AI agents have appropriate data for task completion."

**vs Prompt Engineering:**

| Axis | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| **Scope** | Static instructions | Dynamic info flow |
| **Duration** | Single prompt | Agent lifecycle |
| **Management** | Write-once | Continuous update |

### 5 Types of Context

1. **Instructions** — rules, prompts, examples, tool descriptions
2. **Knowledge** — facts, DB retrievals, accumulated memories
3. **Tools** — external functions, APIs, feedback results
4. **Conversation History** — ongoing user dialogue
5. **User Preferences** — learned likes/dislikes

### Management Strategies

- Agent scratchpads (single-session notes)
- Long-term memories (cross-session storage)
- Context compression via summarization
- Multi-agent systems with shared context
- Sandbox environments for heavy processing
- Runtime state objects for subtask management

### 4 Common Failures

| Failure | Issue | Fix |
|---------|-------|-----|
| **Poisoning** | Hallucinations repeated in context | Validate data, quarantine errors |
| **Distraction** | History overshadows training knowledge | Summarize periodically |
| **Confusion** | Too many tools overwhelm model | RAG for selective tool loading |
| **Clash** | Conflicting info persists | Prune outdated data, use scratchpads |

### Practical Example

Context-engineered Paris booking agent:
- Checks calendars
- Recalls preferences
- Responds: *"I see you're free the first week of October. Shall I look for direct flights..."*

vs prompt-only agent: *"When would you like to go?"*

→ **Context engineering transforms UX.**

### Key takeaway L12

Context engineering = **discipline**, not technique. 5 types × 4 failures = 20 risk vectors. **GSD's "context rot solution"** operationalizes this lesson. Tier 1 siblings ALL struggle với này; GSD explicitly targets.

---

## Lesson 14: Microsoft Agent Framework (MAF)

### What is MAF

> "Builds on top of the experience and learnings from Semantic Kernel and AutoGen."

**MAF = merger/evolution of SK + AutoGen learnings.** Production-ready platform for enterprise agent deployment.

### Key Features

**Orchestration:**
- Sequential workflows (step-by-step)
- Concurrent execution (parallel)
- Group chat (collaborative)
- Handoff (between agents)
- Manager-based coordination (dynamic task lists)

**Production:**
- **Observability** — OpenTelemetry + Azure AI Foundry dashboards
- **Security** — native Azure hosting, RBAC, content safety
- **Durability** — pausable/resumable workflows, error recovery
- **Control** — human-in-the-loop approval workflows

**Interoperability:**
- Cloud-agnostic (containers, on-prem, multi-cloud)
- Provider-agnostic (Azure OpenAI, OpenAI, others)
- Open standards (A2A, MCP)
- Integrations (Microsoft Fabric, Pinecone, mem0)

### Differentiation vs SK and AutoGen

| Aspect | MAF | Semantic Kernel | AutoGen |
|--------|-----|-----------------|---------|
| **Agent Creation** | Direct provider extensions | Requires Kernel instance | Different approach |
| **Tool Registration** | During agent creation | Registered to Kernel | FunctionTool wrapper |
| **Threading** | Automatic | Manual | N/A |
| **Multi-turn Support** | Default | N/A | Requires config |
| **Orchestration** | Graph-based workflows | N/A | Event-driven teams |

### Core Concepts

- **Agents** — customizable instructions, multiple LLM providers, flexible tool integration
- **Workflows** — compose executors (AI agents or custom logic) via edges: direct, conditional, switch-case, fan-out, fan-in
- **Memory Systems** — in-memory threads, persistent message stores, external memory (mem0)
- **Middleware** — logging, monitoring at function + chat interaction levels

### Strategic position

**MAF = Microsoft's unified agent platform bet.** SK maintained but MAF forward path. Enterprise cloud-first but cloud-agnostic deployment possible.

### Key takeaway L14

MAF = **Microsoft's AutoGen+SK consolidation**. Signals: Microsoft unifying fragmented agent tooling. Enterprise teams evaluating SK should plan MAF migration. Non-Microsoft teams can still use (provider-agnostic) but main benefit = Azure integration.

---

## Cross-lesson synthesis

### Infrastructure readiness mapping

| Production concern | Lesson | Sibling who addresses |
|--------------------|--------|----------------------|
| Framework choice | L02 | All (meta) |
| Protocol use | L11 | ECC, Superpowers (MCP users) |
| Context management | L12 | GSD (explicit), all (implicit) |
| Microsoft ecosystem deployment | L14 | goclaw (comparable, but Go-based) |

### Frameworks → Tier mapping

**Tier 1 siblings ≈ Semantic Kernel role** — tool used by individual dev
**Tier 2 goclaw ≈ Azure AI Agent Service role** — platform deploying for multiple tenants
**Tier 3 this course** — teaches the concepts underlying both tiers

### MAF vs goclaw (cross-tier)

| Axis | MAF | goclaw |
|------|-----|--------|
| **Language** | C# / Python | Go |
| **Cloud** | Azure-first | Cloud-agnostic |
| **Scale target** | Enterprise Microsoft | Multi-tenant platform |
| **Licensing** | MIT (open) | CC BY-NC (non-commercial) |
| **Openness** | Open + Microsoft-supported | OSS solo |

→ Different target profiles. MAF for Microsoft-committed enterprises; goclaw for OSS/polyglot environments.

### Context engineering convergence

**L12 "context engineering"** ≈ **GSD's "context rot solution"** ≈ **vault's `llm-wiki-ingest` skill**.

3 implementations, same concept:
- Microsoft course: teaches 5 types + 4 failures
- GSD: implements via XML prompts + size budgets + fresh subagent context
- Storm Bear vault: implements via 13-section entity format + cross-references

→ **Meta-convergence chain continues** (v4 goclaw Knowledge Vault, v5 GSD `/gsd-ingest-docs`, v6 L12 context engineering).

## Cross-references

- Main README: [[(C) README summary]]
- Core lessons cluster: [[(C) Core lessons cluster summary]]
- Entity pages:
  - [[(C) Agentic Protocols (MCP + A2A + NLWeb)]] (draws from L11)
  - Plus L02/L12/L14 content feeds comparison guides
- Sibling cross-refs:
  - GSD's Context Rot Solution: `../../get-shit-done - Beginner Analysis/02 Wiki/(C) Context Rot Solution.md`
  - goclaw's Knowledge Vault: `../../goclaw - Beginner Analysis/02 Wiki/(C) 3-Tier Memory + Knowledge Vault.md`
