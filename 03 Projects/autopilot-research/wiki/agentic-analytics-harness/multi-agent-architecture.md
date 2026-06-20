# Multi-agent architecture: coordinator, sub-agent, and the two loops

## Source

First-party: [omni.co — Building Omni's architecture for agentic analytics](https://omni.co/blog/building-omnis-architecture-for-agentic-analytics). Talk-recap details (loops, iteration caps, "Blobotomy 1"): ai-heartland.com recap — flagged T2. See [[agentic-analytics-harness/source-provenance]].

## The shape of the system

- **Coordinator (main agent).** "Decides which tool to use next based on the question, the results, and what's already been tried." It goes *past a single query* and decides the next move — continue the analysis, compare datasets, investigate for the right matches, or summarize. It can **adapt mid-flight, retry when things break, or stop when it has something useful.** [T1]
- **Summarization sub-agent with its own context window.** Large query results would "clog up the context window of the main agent," so a dedicated sub-agent digests them and hands back a compact summary. [T1] This is the **one** place Omni kept a sub-agent — note the contrast with "Blobotomy 1" below.

### The two-loop structure [T2 — talk recap]

- **Outer loop:** **max 50 iterations**, with **checkpoint-based recovery** for fault tolerance (an iteration can fail without losing the whole run).
- **Inner loop:** **parallel tool invocation** across the available tools.
- Read as: *outer loop = "what should I do next, and have I done enough?"; inner loop = "fire the tools I need for this step, in parallel."*

## "Blobotomy 1" — the split-brain lesson [T2 — talk recap]

> "Blobotomy" is Omni's internal name for a major architectural surgery on Blobby (~5 total).

- **What they tried first:** separate concerns across agents — an **outer agent that planned** + a **separate sub-agent that generated queries.**
- **What broke:** **knowledge silos.** The outer agent knew *"what data exists"*; the inner agent knew *"what one query can retrieve."* Neither had the whole picture, so cross-boundary tasks produced **infinite loops** (each agent bouncing the problem to the other).
- **The fix:** **integrate query generation into the outer harness as a *tool*, not a separate agent.**
- **The principle:** **don't partition knowledge across agent boundaries — keep information and execution capability in the same layer.**
- **Why it generalizes:** multi-agent decomposition is fashionable, but splitting an agent along a *knowledge seam* (where each side needs the other's knowledge to act) creates coordination deadlock. Split along **context-isolation seams instead** (e.g. summarization, which only needs the result, not the plan) — which is exactly why the *summarization* sub-agent survived and the *query-writer* sub-agent didn't.

## Conversation memory: you rebuild it every turn [T1]

- The model has **no memory across turns.** "If you want a model to 'remember' what's already happened … you have to rebuild that memory yourself … **every. single. time.**"
- That means faithfully reconstructing **the full story**: who said what, which tools ran, what data came back, what changed.
- Omni built a **translator** that rewrites their internal conversation representation into "**exactly** what the AI backend expects."
- Demand for this came from real usage: customers using the **MCP Server** revealed appetite for *multi-step* analysis, which forced the memory rebuild.

## Key Takeaways

- **A coordinator + tool-calls beats a swarm of specialist agents** for this problem. Omni's only durable sub-agent is the **context-isolating summarizer**.
- **Decompose by context-isolation, not by knowledge.** If two agents each need the other's knowledge to act, merge them (Blobotomy 1).
- **Memory is your job, not the model's.** Plan to serialize/replay full conversation state through a translator into the exact shape the backend wants.
- **Bound the loop.** A hard iteration cap (50) + checkpoints stops runaway agents — the production version of the [[autonomous-loops-human-in-the-loop/_index|Ralph-loop]] budget discipline.
- Compare org-scale coding harnesses in [[harness-engineering/_index]]: same "humans steer, agents execute, harness enforces" thesis, applied to a customer feature.
