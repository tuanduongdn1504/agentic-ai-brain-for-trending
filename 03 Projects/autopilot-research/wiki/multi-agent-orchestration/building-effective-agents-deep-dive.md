# Original resource #1 — Anthropic "Building Effective Agents"

> **Source:** Anthropic Engineering Blog — https://www.anthropic.com/engineering/building-effective-agents

## Workflows vs Agents: Core Distinction

- **Workflows:** systems where LLMs and tools are orchestrated through **predefined code paths**; all steps, branching, and integration points are coded upfront
- **Agents:** systems where LLMs **dynamically direct their own processes and tool usage**, maintaining control over how they accomplish tasks; step count and exact path are not predetermined
- **Why it matters:** workflows are deterministic and cheaper (fewer tokens, predictable paths); agents are flexible but costlier and riskier (potential for compounding errors, unpredictable token use)
- **"Augmented LLM"** concept (video author's framing): an LLM with access to tools and a reasoning loop that can decide when and how to use them

## The Five Workflow Patterns

All five are **predefined patterns** — you choose which pattern fits your problem, code it, and the LLM operates within that constraint:

### 1. Prompt Chaining
- **What it is:** decomposes tasks into **sequential steps** where each LLM call processes the previous output; **programmatic checkpoints** between steps control flow
- **When to use:** tasks with clear sequential dependencies; predictable task breakdown; each step refines or builds on prior output
- **Example:** draft email → refine tone → check grammar → publish (each step processes and improves the prior)
- **Characteristic:** linear, deterministic, cheap relative to other patterns

### 2. Routing
- **What it is:** **classifies inputs** and **directs them to specialized followup tasks** (based on input type); enables separation of concerns and optimized prompts for distinct categories
- **When to use:** input space has discrete classes (e.g., user query is a bug report vs feature request vs support question); different classes need different processing
- **Example:** categorize incoming ticket as {bug, feature-request, support} → route to specialized agent/workflow per category
- **Characteristic:** gate-keeping step; low-cost classifier fronts multiple specialized pipelines

### 3. Parallelization — Two Variants
- **Sectioning:** break **independent subtasks into parallel execution** (each task is truly independent; results combine without conflict)
  - **When:** subtasks do not depend on each other's output; results can merge cleanly (e.g., research 3 independent markets in parallel, combine findings)
  - **Characteristic:** finish time is the slowest task, not the sum of all tasks
- **Voting:** run **identical tasks multiple times** for diverse outputs (or disagreement detection)
  - **When:** task is open-ended and you want multiple independent perspectives, or you want to measure agreement/confidence
  - **Characteristic:** expensive (N identical runs) but robust to single-point failures in reasoning

### 4. Orchestrator-Workers
- **What it is:** a **central LLM dynamically decomposes tasks** and **delegates to worker LLMs**; workers execute in isolation; orchestrator **synthesizes results** based on specific input (not predefined subtask structure)
- **When to use:** task decomposition must adapt to input; different inputs require different subsets/types of workers; complex problems requiring dynamic coordination
- **Example:** job-application screener — central orchestrator sees resume, decides to invoke keyword-scanner + red-flag-detector + deep-evaluator, aggregates scores into single recommendation
- **Characteristic:** orchestrator owns all decisions (what to decompose, who to delegate to, how to combine); workers are stateless; context isolation between workers
- **Key principle:** orchestrator is an LLM "doing the work" (making routing decisions); it's agent-like even though the overall system is structured as a workflow
- **Note:** video author emphasizes this pattern as hub-and-spoke — orchestrator at center; spokes (workers) never communicate directly; all info flows through center

### 5. Evaluator-Optimizer
- **What it is:** **one LLM generates responses** while **another provides evaluation and feedback** in **iterative loops**; generator runs, evaluator rates it, loop repeats until quality threshold met
- **When to use:** problem requires multiple refinement passes; evaluation criteria are clear (but not always automatable); iterative improvement beats single-pass
- **Example:** initial document draft → evaluate for completeness/clarity → identify gaps → rewrite → re-evaluate → accept or loop again (up to MAX iterations)
- **Characteristic:** expensive (multiple passes) but higher-quality final output; evaluator needs clear rubric or strong LLM judgment

## When (and When Not) to Use Agents

**Use agents when:**
- Problem is **open-ended** (step count cannot be predicted, fixed paths cannot be hardcoded)
- Task complexity varies with input; you cannot prescribe a single workflow upfront
- Problem requires the LLM to maintain control over its exploration path

**When NOT to use agents (simpler solutions often suffice):**
- **Optimized single LLM call with retrieval** — if the problem can be solved with context + one good prompt, don't add an agent loop
- **Any of the five workflow patterns above** — if your problem fits a predefined pattern, use it instead; agents are costlier, have higher latency, and risk compounding errors
- **Core principle:** maintain simplicity in agent design; start simple, add agentic behavior only if necessary

## Core Principles for Agent Design

From Anthropic's guidance (directly stated or demonstrated in the video build):

1. **Simplicity First** — don't architect for agent patterns if a workflow pattern solves the problem
2. **Transparency** — prioritize **explicit planning steps** in your agent's reasoning; don't hide decision-making in black-box loops
3. **Craft Agent-Computer Interfaces (ACI)** — thorough tool documentation, clear input/output schemas, and testing of tools are non-negotiable
   - Tools are how agents interact with the world; poorly designed tools lead to agent failures, misuse, or hallucinated tool calls
   - Invest in clear, example-rich tool documentation
4. **Human Judgment Required** — (video author's teaching stance, aligned to transparency principle) "just because it ran doesn't mean it's good"
   - Real evaluation takes hours with real data and human review
   - Automated metrics miss edge cases; you need human eyes on failures

## Crosswalk: Anthropic Patterns ↔ Video Architecture ↔ Related Concepts

| Anthropic Pattern | Video Term | Implementation | Use in Video |
|---|---|---|---|
| **Orchestrator-Workers** | Hub-and-Spoke Architecture | Central coordinator agent routes to N worker agents ("spokes"); workers never communicate directly; all results return to coordinator | Job-application screener: coordinator decomposes resume review into keyword-scan, deep-eval, red-flag-detect, score-aggregate spokes |
| **Routing** | Dynamic Selection | Model generates routing decision ON THE FLY based on case characteristics (e.g., "non-traditional background → check transferable skills"); never invoke agent unless it answers a real question | Screener coordinator decides which spokes to invoke based on resume signals; skips keyword-scan for obvious matches |
| **Parallelization — Sectioning** | Partition Planning | Carve scope so each worker owns a **distinct, non-overlapping slice**; separate PARTITION PLANNER (upstream, decides routing rules) from COORDINATOR (executor, invokes spokes per partition) | Research partitioning: planner reviews resume, decides "partition A: education background, partition B: work history, partition C: skills alignment"; coordinator invokes one screening per partition |
| **Evaluator-Optimizer** | Refinement Loop | Initial run → evaluate coverage → identify gaps → invoke agents **only** to fill identified gaps → repeat up to MAX iterations (3-4) | Screener: initial partitions → coverage evaluation → if gaps, re-run targeted spokes to cover missing areas → iterate until coverage sufficient or MAX reached |
| **Prompt Chaining** | Sequential Delegation | Task decomposition passes results forward linearly; one spoke completes, coordinator passes result to next spoke | Not primary in video, but coordinator's aggregation of sequential spoke results exhibits chaining within the orchestrator's logic |
| **Orchestrator-Workers** (agent pattern principles) | Coordinator Role | Orchestrator owns: decompose task, assess complexity, route to workers, aggregate results, error handling, observability; workers are **stateless**, no inter-worker knowledge | Coordinator owns task lifecycle (decompose resume → assess complexity → route to spokes → aggregate scores); spokes only execute, unaware of each other |
| **Agents vs Workflows** | When to Architect Hub-and-Spoke | Agents suit open-ended problems where step counts cannot be predicted; workflows (like hub-and-spoke) pre-define paths but within that path, orchestrator is agent-like (makes dynamic routing decisions) | Video builds a workflow (job screener) but coordinator exhibits agent-like behavior (dynamic selection); demonstrates the boundary is nuanced |
| **ACI (Agent-Computer Interface)** | Tool Design & SDK Simplification | Thorough tool documentation, clear schemas; Claude Agent SDK (@tool decorator + internal MCP server) abstracts away manual JSON tool schemas + hand-rolled dispatch loops | Video refactors from raw SDK (manual JSON schemas, hand-rolled dispatch) to Agent SDK (@tool decorator + create_sdk_mcp_server) — shows SDK as ACI automation |

**What the video SIMPLIFIES or RENAMES:**
- Anthropic's "Orchestrator-Workers" pattern = video's "Hub-and-Spoke Architecture" (same concept, different terminology; video emphasizes the topology of "no direct spoke-to-spoke communication")
- Anthropic's 5 workflow patterns are **formal definitions** in the source; video demonstrates 4 of them (chaining, routing, parallelization-sectioning, evaluator-optimizer) implicitly within the coordinator's logic, not as separate example workflows
- "Dynamic Routing" (video term) ≈ "Routing pattern" (Anthropic), but video shows routing as **on-the-fly model-generated decisions** rather than hard-coded classification
- Video's "Partition Planner" is a design pattern not formally named in Anthropic's source; it separates routing-rule generation from execution

## Common Pitfalls & Refinements Shown in Video

### Narrow Task Decomposition Problem
- **The trap:** decompose "Give me a comprehensive EV market analysis" narrowly as [sales trends, battery tech, manufacturers] → misses charging infrastructure, policy/subsidies, second-hand market, consumer sentiment, supply chains, grid capacity
- **Why it happens:** each sub-agent only sees its isolated context; none can flag what's missing; decomposition is too narrow upfront
- **Fixes shown:**
  1. **Decompose-time review:** add a tool that reviews the subtask breakdown **before delegating**, asking "what info is needed?" and expanding subtasks to cover gaps
  2. **Aggregate-time check:** before aggregating, ask "did we cover X, Y, Z?" and only submit if coverage is sufficient
- **Broader lesson:** narrow vs comprehensive decomposition is a **design discipline problem**, not an agent intelligence problem

### Context Isolation Double-Edged Sword
- **Benefit:** each worker has clean, focused context; reduced token waste; prevents hallucination of cross-worker knowledge
- **Cost:** workers cannot discover missing angles because they don't see the full picture
- **Solution:** coordinator is the "full-picture" agent; it controls what context each worker sees and can inject missing context or trigger additional spokes if needed

### Overlapping Work & Token Waste
- **The trap:** three research agents each given the same brief → three overlapping answers + wasted tokens
- **Fix:** partition scope so each agent owns a **non-overlapping slice** with a distinct purpose; one PARTITION PLANNER agent decides upfront what partitions exist, then COORDINATOR invokes exactly one screening per partition
- **Separation principle:** partition-planning (deciding routing rules) ≠ coordination (executing routes); keep them separate to avoid conflicting logic

## Observability & Productionization

### Centralized Coordinator as Observability Choke Point
- **Advantage:** coordinator sees every message, every tool call, every error; single point to log, trace, and audit
- **Implementation:**
  - Structured logging with timestamps, severity levels, request IDs
  - Persist all spoke inputs/outputs (scoped per partition)
  - Error handling around all tool calls (e.g., json.loads with try-catch)
  - Coverage evaluation gates before final submission
  - Exit-gate (force submit_final) to prevent infinite loops
- **Production readiness (mentioned but not fully built in video):**
  - Container per sub-agent (isolation, scaling, restarts)
  - OpenTelemetry for distributed tracing (metrics, latency, error rates across agents)
  - JSONL log format (parseable for log aggregation systems)
  - Persistent reports (timestamped, human-readable coverage audit trail)

### Video's Honest Weak Points (Pedagogical, Not Production)
- Initial observability: only print statements; no API tracing, token counts, latency tracking, request ID correlation
- Error handling: no try-catch around json.loads; spoke responses never persisted; no mid-run gap detection
- Coverage evaluation: refinement loop made score go **DOWN** (not UP) — realism check: "is it actually good?" requires hours of real evaluation with real data
- One-shot limitations: single-pass can miss gaps even with decompose-time + aggregate-time checks

## Key Takeaways

- **Workflows are predefined patterns; agents are open-ended.** Five workflow patterns cover most structured use cases — use them before resorting to full agent loops.
- **Hub-and-Spoke (Orchestrator-Workers) suits multi-step problems where you want coordination, context control, and observability.** Central orchestrator owns all routing, context injection, and aggregation.
- **Dynamic routing and partition planning are design disciplines, not agent intelligence features.** Model generates decisions, but you must architect the decomposition upfront and validate coverage.
- **Context isolation protects workers but requires the orchestrator to own the full picture.** Each worker is stateless; all complexity lives in the coordinator's logic and context management.
- **Tool design is ACI design.** Clear documentation, examples, and schema validation are non-negotiable; the Claude Agent SDK automates schema and dispatch, but YOU design the tool semantics.
- **Observability through centralization.** A single coordinator choke point enables structured logging, error handling, and audit trails; distributed architectures are harder to debug.
- **Start simple, add agentic behavior only if necessary.** Many problems that "look agentic" are actually well-solved by workflow patterns; measure twice, architect once.
- **Real evaluation takes human judgment and hours.** Automated metrics miss edge cases; your job is to define clear rubrics and spend the time validating, not just running the system.
