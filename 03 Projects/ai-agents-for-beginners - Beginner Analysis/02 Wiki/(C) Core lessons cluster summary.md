# (C) Core Lessons Cluster Summary — Lessons 01, 03, 05, 08

> Nguồn: Fetched via raw.githubusercontent.com 2026-04-18
> Coverage: 4 foundational concept lessons (agent types, design patterns, RAG, multi-agent)

## TL;DR

4 lessons form the **conceptual spine** của curriculum. Lesson 01 answers "what is an agent", Lesson 03 answers "how do we design one", Lesson 05 answers "how to get knowledge", Lesson 08 answers "how agents collaborate". Together = **agent fundamentals kit**. Every concept maps to Tier 1 sibling implementations at concrete level.

---

## Lesson 01: Intro to AI Agents and Agent Use Cases

### Definition
> "Systems that enable Large Language Models (LLMs) to perform actions by extending their capabilities by giving LLMs access to tools and knowledge."

4 core elements: **systems thinking, LLM capabilities, action performance, tool/knowledge access**.

### System Components

| Component | Role |
|-----------|------|
| **Environment** | Operational space (e.g., travel booking system) |
| **Sensors** | Information gathering detecting environment state |
| **Actuators** | Tools enabling agents to modify environment |

→ Classic agent theory (Russell+Norvig) applied to LLM era.

### 7 Agent Types

| Type | Mechanism | Use case |
|------|-----------|----------|
| Simple Reflex | Predefined rules | Rule-based automation |
| Model-Based Reflex | World modeling | State-aware tasks |
| Goal-Based | Plan creation | Task decomposition |
| Utility-Based | Preference weighting | Recommendation/ranking |
| Learning | Feedback-driven improvement | Self-improving agents |
| Hierarchical | Tiered delegation | Complex workflow orchestration |
| Multi-Agent | Independent/cooperative | Distributed problem-solving |

### When to use AI Agents

- Open-ended problems requiring dynamic planning
- Multi-step processes iterative tool use
- Continuous improvement via feedback

### Framework landscape (preview for Lesson 02)

- **Azure AI Agent Service** with open models (OpenAI, Mistral, Llama) + standardized OpenAPI 3.0 tools
- **AutoGen** — research-driven
- **Semantic Kernel** — production-ready

### Key takeaway L01

Agents = **LLM + tools + knowledge + goal-driven loop**. Not just chatbot. Understanding the 7 types = decision framework for which type fits problem.

---

## Lesson 03: Agentic Design Patterns

### Structure: 3 categories × 3 guidelines

**3 Pattern categories:**

1. **Agent (Space)** — Environmental design for physical/digital interaction
   - Focus: how agents connect people, operate across devices/platforms
2. **Agent (Time)** — Temporal design (past/present/future)
   - Focus: historical context, real-time nudging, adaptive evolution
3. **Agent (Core)** — Foundational elements
   - Focus: uncertainty management, trust establishment

**3 Implementation guidelines:**

- **Transparency** — disclose AI involvement + functionality
- **Control** — enable user customization + agency
- **Consistency** — maintain familiar multi-modal experience

### Pattern distinctiveness

| Pattern | Operational dimension |
|---------|----------------------|
| Space | Connectivity + accessibility across devices |
| Time | Contextual awareness + behavioral adaptation |
| Core | Transparency + control foundation |

### Design philosophy

> "Agents should broaden and scale human capacities while maintaining human control."

**Not replacing humans, connecting them.** Operate invisibly when appropriate while staying transparent + controllable.

### Code samples

- Python Agent Framework (Jupyter)
- .NET Agent Framework (Markdown docs)

### Key takeaway L03

**Space/Time/Core = mental scaffolding** for any agent design decision. Transparency/Control/Consistency = non-negotiable guardrails. Broader framework than pure "tool use" or "planning" patterns.

---

## Lesson 05: Agentic RAG

### Definition
> "A loop of iterative calls to the LLM, interspersed with tool or function calls."

Agent autonomously plans next steps while pulling information from external sources.

### Classic RAG vs Agentic RAG

| Axis | Classic RAG | Agentic RAG |
|------|-------------|-------------|
| **Flow** | Linear: retrieve → read → respond | Loop: plan → retrieve → assess → refine |
| **Decision** | Scripted pipeline | Autonomous self-direction |
| **State** | Stateless per query | State + memory across steps |
| **Tool use** | Single retrieval tool | Multiple retrieval methods, tool switching |

### 5-Step Iterative Loop

1. **Initial LLM Call** — present user objective
2. **Tool Selection** — model identifies needed info, invokes retrieval
3. **Assessment** — evaluate returned data sufficiency
4. **Refinement/Repeat** — adjust approach if needed
5. **Memory Maintenance** — track previous attempts to avoid repetition

### Capabilities

- **Self-Correction** — iterate failed queries, rewrite DB calls
- **Domain Autonomy** — operate dynamically within defined boundaries
- **Extended Workflows** — evolve strategies as new info surfaces

### Applications

- Compliance verification
- Complex database queries
- Multi-step tasks requiring repeated refinement + precision validation

### Key takeaway L05

**Agentic RAG ≠ better RAG.** It's RAG + loop + self-direction. Cost: more tokens, longer latency. Benefit: handles ambiguous/evolving queries classic RAG can't.

---

## Lesson 08: Multi-Agent Design Pattern

### When to use Multi-Agent

3 scenarios:

1. **Large workloads** — divided into smaller parallel tasks
2. **Complex tasks** — specialized subtasks (e.g., autonomous vehicle: navigation + obstacle detection + vehicle-to-vehicle comm)
3. **Diverse expertise** — specialists outperform generalists per domain

### Advantages over Single-Agent

- **Specialization** — each agent focused
- **Scalability** — add agents without overloading
- **Fault tolerance** — continues if individual fails

### Essential Building Blocks

- Agent Communication (protocols for sharing preferences/constraints)
- Coordination Mechanisms (unified goals)
- Agent Architecture (internal decision-making + learning)
- Visibility Tools (logging, monitoring, performance tracking)
- Orchestration Patterns (centralized/decentralized/hybrid)
- Human Integration (escalation + approval workflows)

### Common Orchestration Patterns

| Pattern | Mechanism |
|---------|-----------|
| **Group Chat** | Multiple agents exchange messages (centralized or peer-to-peer) |
| **Hand-off** | Sequential delegation based on predefined rules |
| **Collaborative Filtering** | Specialists contribute expertise to recommendations |

### Practical example: Refund Process

- **Process-specific agents:** customer, seller, payment, resolution, compliance
- **General-purpose agents:** shipping, notification, audit, security (serve multiple processes)

→ **Mixed architecture** (specialist + generalist).

### Key takeaway L08

Multi-agent = **design pattern, not silver bullet**. Requires thoughtful architecture around **communication, coordination, observability**. Simpler than it sounds: most systems = orchestrator + specialists + human escalation.

---

## Cross-lesson synthesis

### Concept → Implementation mapping to Tier 1/2 siblings

| Concept (L01-L08) | ECC | Superpowers | gstack | GSD | goclaw |
|-------------------|-----|-------------|--------|-----|--------|
| **Agent types** (L01) | Subagent categories | 7-stage agents | Specialist roles | 33 specialized agents | Agent teams per tenant |
| **Design patterns** (L03) | Skill format | Pattern library | Sprint pipeline | Meta-prompting | Platform patterns |
| **Agentic RAG** (L05) | Limited (skills lookup) | Search + doc ingest | Spec-driven search | `/gsd-ingest-docs` | Knowledge Vault (full Agentic RAG) |
| **Multi-agent** (L08) | Subagents concept | Subagent-driven | Specialist roles = multi-agent | 33 agents = multi-agent | Agent teams + orchestration |

→ **Every Tier 1/2 sibling implements subset of L01-L08 concepts.** Course = shared vocabulary.

### Cluster insight

**L01 teaches the WHAT, L03 teaches the HOW, L05 teaches the KNOWLEDGE, L08 teaches the COLLABORATION.**

Minimum learning path for siblings adoption:
- ECC/Superpowers users: L01 + L03 + L08 (basic)
- gstack/GSD power users: + L05 (RAG), + L07 (planning), + L09 (metacognition)
- goclaw deployers: + L08 full + L10 (production)

## Cross-references

- Sibling cluster summaries: none (first cluster summary pattern)
- Entity pages:
  - [[(C) Agent Design Patterns]] (draws from L01 + L03)
  - [[(C) Agentic RAG]] (draws from L05)
  - [[(C) Multi-Agent Systems]] (draws from L08)
- Main README: [[(C) README summary]]
