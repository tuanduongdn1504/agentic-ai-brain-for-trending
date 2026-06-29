# Agents, Tools, Permissions & Memory (Ch. 6, part 2)

## Source

Video sections "From RAG to Agents" → end + Huyen *AI Engineering* Ch.6 (RAG and Agents → Agents, Tools, Planning, Failure Modes, Memory). See [[overview]], [[rag]], [[source-provenance]].

## RAG vs agents

- **RAG** retrieves info to answer a query in a grounded way — **single-step**: retrieve + generate.
- **Agents go further**: they can **plan, use tools, hold memory, and take multiple steps.** Given a task, an agent can plan → call tools → observe results → decide next steps → produce a final answer.
- **Don't default to agents.** Ask: are we just answering queries from a grounded source (→ RAG), or do we need actions/tools/memory/reasoning (→ agent)? *Agents extend RAG by adding planning + tool use* — you can have RAG *inside* an agent.

| | RAG | Agents |
|---|---|---|
| Pattern | retrieve → generate | plan → act → observe → iterate |
| Steps | single-step | multi-step |
| Best for | grounded answering | multi-step tasks + actions |

## Agent system design — the plan-act-observe loop

`User goal` → **Planning & reasoning** (understand the task) → **Tool selection** (pick relevant tools) → **Call the tool** (e.g. via MCP) → **Observe the result** → **Update memory** → **Next action**: if there's enough context → answer; else → loop back to planning. With a **human-in-the-loop handoff** when configured.

> **"Think about agents as workflows with feedback, not just one model call."** You design each step — that's where the intelligence comes from. They're *intelligent workflows*, not magic.

## Tools & permissions (least privilege)

- **Tools make agents useful** — without a search tool it can't search; without DB access it can't query; without an API it can't reach it. Examples: search, database, code execution, external APIs (often via MCP).
- **But permissions keep them safe.** Huyen's law (Ch.6, verbatim): *"The more tools you give a model, the more capabilities the model has,"* but *"the more automated the agent becomes, the more catastrophic its failures."*
- **Controls:** allow-lists (what it can/can't do), scope, **rate limits**, thresholds/stop conditions, **approval gates**, **audit logs**.
- **Least privilege:** "give the agent only the tools and access it truly needs." And **prefer narrow agents** — one agent per job. "You don't want an agent with 25 tools doing 15 tasks — it's confusing, memory blows up, results get weak." (This is the *context-isolation* principle echoed in [[../multi-agent-orchestration/_index]] and [[../agentic-analytics-harness/_index]].)

> Useful agents need tools; **safe agents need strict permissions.**

## Memory (Ch.6 "Memory")

Memory keeps agents coherent across longer tasks. Huyen: memory systems "manage information exceeding context-window limits." Four kinds (the video's breakdown):

1. **Short-term context** — recent messages / immediate conversation.
2. **Task state** — current goal, progress, intermediate results.
3. **Long-term memory** — stored knowledge, preferences, facts over time.
4. **Interaction history** — past interactions + decisions, for continuity.

**Risks:** **stale memory**, **privacy issues**, and **growing context cost** — "if you've used Claude you've hit context limits." Unbounded memory means every small request drags a huge history → slow + expensive + privacy-leaky.

> **Discipline: "store only what helps the task and forget what is not needed."** Refresh/clean memory; expire old history. (This is exactly the context-rot / memory-hygiene theme in [[../claude-code-memory-systems/_index]].)

## Agent failure modes & evaluation (Ch.6, video glosses)

Ch.6 explicitly covers **agent failure modes and evaluation** — agents fail in *compounding* ways (a bad plan or a wrong tool call cascades). Agent eval therefore measures the **trajectory** (did it take sensible steps?) as well as the **final answer** — see [[evaluation]] and the trajectory-vs-outcome framing in [[../prompt-evaluation/_index]].

## Key Takeaways

- **RAG = single-step grounded answering; agents = multi-step plan-act-observe loops** with tools + memory. Don't reach for agents unless the task needs actions/multi-step reasoning.
- **Agents are designed workflows with feedback**, not a single clever model call.
- **Tools = capability, permissions = safety.** Apply least privilege, allow-lists, rate limits, approval gates, audit logs — and **prefer narrow, single-purpose agents.**
- More automation = more catastrophic failures; design for the failure, not just the happy path.
- **Memory must be curated** (short-term / task-state / long-term / history) — unbounded memory means cost, staleness, and privacy risk.

## Cross-links

- [[rag]] (agents extend RAG) · [[prompt-engineering-and-guardrails]] (tool allow-lists / injection) · [[evaluation]] (agent eval = trajectory + outcome) · [[production-architecture-and-feedback]] (Ch.10 "Add Agent Patterns")
- [[../multi-agent-orchestration/_index]] — coordinator/sub-agent patterns, narrow-decomposition, the Anthropic agent originals
- [[../claude-code-memory-systems/_index]] — the 6-level memory taxonomy (this section ≈ its conceptual core)
- [[../agentic-analytics-harness/_index]] — production agent harness lessons (tool sizing, don't-fragment-knowledge, error-recovery)
