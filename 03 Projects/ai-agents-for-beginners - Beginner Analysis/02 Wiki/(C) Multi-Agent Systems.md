# (C) Multi-Agent Systems

> Entity page — Architecture concept
> Sources: Lesson 08 (multi-agent) + Lesson 09 (metacognition, adjacent)
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Multi-Agent System (MAS)** = architecture where **multiple agents work together** toward common goal. Each agent has specialization (task, domain, role). Coordination via **communication protocols + orchestration patterns**.

**Simple rule of thumb:** If one agent does everything = single-agent. If decomposed to 2+ specialists coordinating = multi-agent.

## 2. Why it matters / Sao quan trọng

Single-agent limitations:
- **Context window** — one agent can't hold unbounded context
- **Specialization** — generalist weaker than specialist per domain
- **Scale** — serial execution bottleneck
- **Fault tolerance** — single point of failure

Multi-agent addresses via: **parallelism + specialization + redundancy**.

## 3. When to use Multi-Agent (3 scenarios)

1. **Large workloads** — divide into smaller parallel tasks (e.g., research 50 papers → 5 agents × 10 papers)
2. **Complex tasks** — specialized subtasks (e.g., autonomous vehicle = navigation + obstacle detection + V2V communication)
3. **Diverse expertise** — specialists outperform generalists per domain

## 4. Advantages over Single-Agent

| Advantage | Explanation |
|-----------|-------------|
| **Specialization** | Each agent focused on specific task |
| **Scalability** | Add agents as needs grow, no overloading |
| **Fault tolerance** | Individual failure doesn't crash system |
| **Parallelism** | Concurrent execution possible |

## 5. Essential Building Blocks

- **Agent Communication** — protocols for sharing preferences/constraints
- **Coordination Mechanisms** — ensure agents work toward unified goal
- **Agent Architecture** — internal decision-making + learning structures
- **Visibility Tools** — logging, monitoring, performance tracking
- **Orchestration Patterns** — centralized / decentralized / hybrid
- **Human Integration** — escalation points + approval workflows

## 6. Common Orchestration Patterns

### Group Chat
- Multiple agents exchange messages
- Centralized (manager routes) or peer-to-peer (agents discuss directly)
- Use case: Brainstorming, design reviews

### Hand-off
- Sequential task delegation based on predefined rules
- Agent A finishes → passes to Agent B
- Use case: Customer support triage → specialist

### Collaborative Filtering
- Multiple specialists contribute expertise
- Outputs combined for final recommendation
- Use case: Multi-dimensional scoring (price + safety + speed)

## 7. Practical Example: Refund Process

### Process-specific agents
- Customer (handles customer requests)
- Seller (handles seller-side)
- Payment (handles refund execution)
- Resolution (handles escalation logic)
- Compliance (handles regulatory checks)

### General-purpose agents
- Shipping (cross-process)
- Notification (cross-process)
- Audit (cross-process)
- Security (cross-process)

→ **Mixed architecture** = specialists + shared utilities. Pattern generalizes.

## 8. Adjacent concept: Metacognition (Lesson 09)

Multi-agent systems benefit from **metacognition agents** — agents that reflect on:
- Which agent should handle this task?
- Am I the right specialist?
- Should I escalate?

→ Metacognition = **orchestration intelligence layer**. Not always needed, but unlocks adaptive MAS.

## 9. Trade-offs / Limitations

- **Coordination overhead** — N agents = N² communication possible
- **Consistency challenges** — agents may disagree or repeat work
- **Debugging complexity** — emergent behavior hard to trace
- **Cost multiplier** — each agent = LLM call; MAS = N× cost
- **Latency amplification** — sequential handoff adds per-step latency

## 10. Comparison to sibling implementations

| Sibling | MAS implementation | Orchestration |
|---------|-------------------|---------------|
| **ECC** | Subagents concept, light | Hand-off primarily |
| **Superpowers** | Subagent-driven development | Hand-off + Group chat (7-stage) |
| **gstack** | Specialist roles (Sprint Pipeline) | Hand-off (pipeline stages) |
| **GSD** | 33 specialized agents | Group chat + Hand-off + Planning Agent Coordination |
| **goclaw** | Agent teams per tenant | Platform orchestration, multi-tenant |

**Observation patterns:**
- **Hand-off** = universal (all 5 siblings use)
- **Group chat** = GSD + Superpowers (planning phase)
- **Collaborative filtering** = rarely used explicitly

## 11. Common pitfalls

1. **Too many agents** — 50 specialists when 5 suffice. Coordination overhead kills gains.
2. **No coordinator** — decentralized MAS hard to steer. Usually need manager agent.
3. **Agent overlap** — 2 agents can both handle task = conflict or redundant work.
4. **Missing termination** — agents keep working indefinitely. Budget blown.
5. **Opaque communication** — no logging = impossible to debug emergent behavior.

## 12. When NOT to use Multi-Agent

- **Simple single-step task** — single agent sufficient
- **Latency-critical** — coordination adds latency
- **Budget-constrained** — MAS cost multiplier prohibitive
- **Prototype stage** — start single, add agents as needed
- **Unclear decomposition** — if tasks don't cleanly split, single agent with good prompting wins

## 13. Storm Bear vault relevance + References

**Vault itself = proto-multi-agent:**

| Agent (in vault) | Role |
|------------------|------|
| Claude (wiki maintainer) | Main agent |
| `llm-wiki-ingest` skill | Specialized sub-agent (knowledge construction) |
| `llm-wiki-routine` skill | Orchestrator (routine pattern) |
| `brain-setup` skill | Specialized sub-agent (vault init) |
| `new-project` skill | Specialized sub-agent (scaffolding) |

**Orchestration:** Hand-off pattern (routine → ingest skill → etc.). Group chat absent. Collaborative filtering absent.

→ **Vault = minimal MAS.** Could evolve toward Group Chat (multi-Claude instances reviewing each other) or Collaborative Filtering (vote on entity page content).

## References

- Source: [[(C) Core lessons cluster summary]] (lesson 08)
- Related entities: [[(C) Agent Design Patterns]], [[(C) Agentic RAG]]
- Sibling MAS implementations:
  - `../../get-shit-done - Beginner Analysis/02 Wiki/(C) 33 Specialized Agents + Commands.md`
  - `../../gstack - Beginner Analysis/02 Wiki/(C) Specialist Roles.md`
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Agent Teams.md`
  - `../../Superpowers - Beginner Analysis/02 Wiki/(C) Subagent-Driven Development.md`
