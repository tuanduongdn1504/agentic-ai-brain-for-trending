# Builder–Orchestrator–Executor — Mani Kanasani's framework

The corpus's strongest organizing taxonomy. Adopt with confidence as a default architecture for any multi-tool AIOS.

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Trends-5

## The three-role separation

Mani Kanasani's framework partitions an AIOS into three distinct functional layers:

| Role | Purpose | Example tools |
|---|---|---|
| **Builder** | Construct platforms / one-time scaffolding | Cloud Code · Lovable · Bolt |
| **Orchestrator** | Coordinate workflows / manage agent fleet | **OpenClaw** (Mani's primary), Cowork |
| **Executor** | Specialized agents that do specific tasks | Research agent · email agent · voice agent · meeting-intelligence agent |

Each layer has a different lifespan and a different optimization goal:
- **Builder is short-lived** — used during initial setup, then mostly idle
- **Orchestrator is always-on** — long-running, manages agent dispatch
- **Executors are task-scoped** — spun up per workflow, completed and torn down

## Why this matters

The corpus consensus (across all 6 sources, even Ross Mike implicitly) is that **specialization beats generalization** for AI agents. A single mega-agent trying to do everything underperforms a small fleet of focused agents because:

1. **Context budgets** per agent stay small → less context rot
2. **Skill scoping** per agent stays narrow → clearer behavior
3. **Failures localize** → easier debugging
4. **Sub-agent parallelism** unlocks (orchestrator dispatches multiple executors in parallel)

## Autopilot loops + Kanban orchestration

Both **Mani Kanasani** and **Simon Scrapes** advocate for **autonomous loops** running on a Kanban board:

```
                       Kanban Board
   ┌──────────┬─────────┬──────────┬──────────┐
   │  To Do   │  Doing  │  Review  │   Done   │
   ├──────────┼─────────┼──────────┼──────────┤
   │ task A   │ task C  │ task B   │ task D   │
   │ task E   │         │          │          │
   └──────────┴─────────┴──────────┴──────────┘
        ▲          ▲         ▲          ▲
        │          │         │          │
   [Orchestrator decides which agent picks up next]
        │          │
        ▼          ▼
   ┌──────────────────┐
   │ Executor agents  │
   │  - research      │
   │  - email         │
   │  - voice         │
   │  - meeting-intel │
   └──────────────────┘
```

Tasks move through stages **without human supervision**. The orchestrator decides which executor handles each task; executors update the board on completion.

Implementation: Mani Kanasani specifically mentions **Superbase** as the shared-state store.

## Remy Gaskell's "Observe-Think-Act" loop

The cognitive primitive each executor agent runs:

1. **Observe** — read inputs / pull from connectors / check Kanban board state
2. **Think** — reason about next step / select skill / decide tool calls
3. **Act** — execute the tool call / write to memory / update board

Compared to simple chatbot:
- Chatbot is **respond-only** — single turn, no agency
- Observe-Think-Act is **looping** — repeated until goal is reached

This is the same pattern as [[../autonomous-loops-human-in-the-loop/_index]] but tightened to a single cognitive cycle.

## Mani Kanasani's chef-vs-vending-machine analogy

The corpus's sharpest framing of automation-vs-agency:

| Automation | Agency |
|---|---|
| **Vending machine** — fixed output for fixed input | **Chef** — takes custom orders, makes decisions mid-process |
| Workflows / Zapier / IFTTT | AI agents on Observe-Think-Act loops |
| Predictable | Adaptive |
| Easy to test | Harder to test (eval suites needed) |

Implication: when designing an AIOS workflow, **explicitly choose** which steps need the chef vs which need the vending machine. Don't agentify what can be reliably automated.

## Composing with vault patterns

The autopilot-research project IS this pattern:

| AIOS layer | Vault instance |
|---|---|
| **Builder** | Initial project scaffolding (`(PROJECT TEMPLATE)/` clone) |
| **Orchestrator** | `bin/autopilot-drain.py` + launchd UserAgent for cron |
| **Executors** | yt-search agent, NotebookLM ingest agent, compile-by-Claude in Claude Code session |
| **Kanban board** | `raw/topics-queue.md` (pending vs completed) |
| **Observe-Think-Act** | Claude Code session reading raw + writing wiki + updating master-index |

This convergence is corpus-level evidence that the Builder-Orchestrator-Executor pattern is the **right primitive** for autonomous knowledge work — vault arrived at it independently via Karpathy/paperclip inspiration; Mani Kanasani arrived at it via OpenClaw practice.

## Security posture for this architecture

Two distinct schools (covered in detail at [[security-philosophies-and-sandboxing]]):

- **Conservative access** (Ross Mike) — each executor gets minimum permissions; prefer read-only
- **Infrastructure-led security** (Mani Kanasani) — sandbox the orchestrator + executors via NemoClaw; don't rely on prompt-level safety

For high-stakes executors (email-sender / payment-mover), infrastructure-led is the more defensible posture.

## When NOT to use this pattern

The Builder-Orchestrator-Executor split adds complexity. Skip it if:

- You're running a **single agent on a single task** — no orchestration needed
- Your workflow is **fully deterministic** — use plain automation (vending machine), not AI
- **Context fits comfortably** in one agent's window — multi-agent split doesn't help
- You're **prototyping** — start single-agent, split into roles only when you hit a bottleneck

## Key Takeaways

- **Builder–Orchestrator–Executor is the corpus's strongest organizing taxonomy** — adopt as the default for non-trivial AIOS
- **Specialization beats generalization** — every speaker converges on this even when phrasing differs
- **Kanban-driven autonomous loops** (Mani + Simon) are the orchestration default
- **Observe-Think-Act** (Remy Gaskell) is the per-executor cognitive primitive
- **Chef-vs-vending-machine** (Mani) is the sharpest framing for *when* to use AI vs plain automation
- **The vault's autopilot-research project IS this pattern** — independent convergence validates the architecture

## Related

- [[overview]] — AIOS framing
- [[skills-architecture-progressive-disclosure]] — how executors invoke capabilities
- [[security-philosophies-and-sandboxing]] — security posture for each role
- [[../autonomous-loops-human-in-the-loop/_index]] — sister topic on the loop pattern
- [[../harness-engineering/_index]] — org-scale variant
