# Hub-and-spoke architecture & the coordinator role

> **Source:** ExamPro "Claude Architect: Multi-Agent Orchestration" — Andrew Brown / ExamPro (third-party course, [exampro.co/cca-f](https://www.exampro.co/cca-f)), [vRYBG_R8JAI](https://www.youtube.com/watch?v=vRYBG_R8JAI), 2026-04-29, 2h9m. Sections 1–3 of the video. **NOT first-party Anthropic.** Crosswalk: [[multi-agent-orchestration/building-effective-agents-deep-dive]] (Anthropic's orchestrator-workers pattern). See [[multi-agent-orchestration/source-provenance]].

## Hub-and-spoke definition

- **One coordinator agent at the center**; sub-agents (called "spokes") never communicate directly with each other.
- **All communication routes through the coordinator**, which owns:
  - Routing decisions (which spoke handles which task)
  - Context-sharing (each spoke only knows what the coordinator injects)
  - Error handling (single point to catch failures)
  - Observability (log every message, monitor state)
- **The coordinator is a choke point** — a design feature, not a bug. It forces all signal through one place, enabling tight control and audit trails.
- This is "at least one of the means" Claude Code sub-agents communicate (video author's framing); Anthropic's official term is **Orchestrator-Workers** pattern: central LLM dynamically decomposes tasks and delegates to workers, synthesizing results.

## Coordinator's four jobs

The coordinator must own:

1. **Task decomposition** — break the incoming query into subtasks.
2. **Delegation** — decide which spokes to invoke and what context/prompt to give them.
3. **Result aggregation** — combine spoke outputs into one coherent final response, resolving any conflicts.
4. **Routing (decide-who-by-complexity)** — assess the question's complexity and select the appropriate spokes.

## Coordinator routing rules

- **"Do not do the work yourself."** The coordinator orchestrates; it doesn't answer the query directly.
- **"Use your judgment."** The coordinator has discretion to route based on observed case characteristics:
  - **Simple factual question** → single spoke, no parallelization overhead.
  - **Multi-step research** → sequential delegation; pass earlier results forward as context.
  - **Independent subtasks** → parallel dispatch; all spokes run concurrently, results aggregated at the end.
- **Dynamic routing.** The model generates routing decisions on the fly based on the specific query. Example from video: "non-traditional background → check transferable skills; strong match → skip keyword scan." Never invoke a spoke unless it answers a real question.

## Basic implementation: The job-application screener

**Use case:** Screen job applications by decomposing into four independent screening angles.

- **Spokes (stateless worker agents):**
  - Keyword scanner — fast surface-level match (salary, location, keywords).
  - Deep evaluator — thorough assessment of skills, experience, trajectory.
  - Red-flag detector — identify disqualifying issues (gaps, incompatibilities, visa complications).
  - Score aggregator — synthesize outputs into a final decision and ranked score.

- **Coordinator tasks:**
  - Decompose incoming application into the four screening subtasks.
  - Delegate each to its spoke with the job posting + resume snippet scoped to that angle.
  - Aggregate the four responses into one final screening verdict.
  - Decide routing: if job is simple (junior-level) might skip deep eval; if high-complexity role, run all four.

- **Task tools (coordinator implements):**
  - `create_task(spoke_id, prompt, context)` — instantiate a subtask.
  - `get_task_status(task_id)` — poll completion.
  - `complete_task(task_id)` — finalize and retrieve result.

## Loop safety: MAX-STEPS cap and while-True idiom

- **while-True coordinator loop** with a **MAX-STEPS cap** (typically ~10, roughly 2× the expected ~5 steps) to catch runaway loops.
- If the coordinator tries to invoke more spokes than MAX-STEPS allows, the loop exits and forces a final aggregation.
- Prevents token waste and uncontrolled delegation chains.

## Key architectural invariants (from Anthropic's "Building Effective Agents")

- **Spokes have no knowledge of each other.** Context is isolated; each spoke only sees the coordinator's injected prompt and context.
- **Spokes are stateless.** Each invocation is independent; spokes don't maintain memory across calls.
- **Coordinator controls context boundaries.** The coordinator explicitly decides what information crosses between spokes and the outside world.
- **Result return is the only communication channel.** When a spoke finishes, it returns its result to the coordinator. There is no peer-to-peer spoke communication.

## Narrow decomposition pitfall (and fixes)

**Problem:** Decomposing "Give me a comprehensive EV market analysis" too narrowly (only sales figures, battery tech, manufacturers) silently misses critical dimensions: charging infrastructure, policy/subsidies, second-hand market, consumer sentiment, supply chains (lithium, cobalt), grid capacity. Each spoke only knows its isolated slice, so none flags the gaps.

**Fixes:**
1. **Decompose-time review tool** — before delegating, ask the coordinator: "What information is needed for a complete answer?" Add missing subtasks to the decomposition plan.
2. **Aggregate-time check** — before writing the final answer, verify: "Did we cover X? Y? Z?" Catch gaps before returning.

Video author notes: For the job-screener, "narrow vs better" is really one screening agent contextualized N ways, not three hard-coded agents (realization that parametrization beats proliferation).

## Crosswalk to Anthropic's patterns

| Video pattern | Anthropic "Building Effective Agents" |
|---|---|
| Coordinator decomposes + routes to spokes | **Orchestrator-Workers:** central LLM dynamically decomposes and delegates to workers |
| Dynamic routing (non-traditional background → check transferable skills) | **Routing:** classify inputs and direct to specialized followup tasks; separation of concerns |
| Partitioning independent screening subtasks | **Parallelization—Sectioning:** break independent subtasks into parallel execution |
| Sequential pass-forward of results | **Prompt Chaining:** decompose tasks into sequential steps; each LLM processes previous output |
| Spokes are stateless, no inter-spoke knowledge | **Orchestrator-Workers delegation:** workers execute isolated; only final result synthesized |

## Key Takeaways

- **Hub-and-spoke forces all communication through the coordinator**, eliminating silent failures from uncoordinated sub-agent work (spokes never talk directly).
- **The coordinator owns four responsibilities:** decomposition, delegation, aggregation, and routing complexity decisions. It does not do the actual work.
- **Routing is dynamic and case-dependent.** Use judgment to invoke only the spokes that answer real questions for this specific query (avoid waste).
- **Parallel vs. sequential is a routing choice, not a fixed design.** The coordinator decides on the fly based on subtask independence (parallel if independent; sequential if multi-step).
- **MAX-STEPS cap and while-True idiom prevent runaway loops.** Bind the coordinator loop to ~10 steps (2× expected normal count) to catch infinite delegation chains.
- **Spokes are stateless and context-isolated.** Each spoke only knows what the coordinator injects; there is no shared memory between spokes. This simplicity trades flexibility for predictability and auditability.
- **Narrow decomposition is a silent failure mode.** Without explicit "what information is needed?" reviews at decomposition time and "did we cover X?" checks at aggregation time, the coordinator can miss entire dimensions. Use safeguard tools to detect gaps.
- **This is Anthropic's Orchestrator-Workers pattern applied concretely.** The video demonstrates the hub-and-spoke topology; Anthropic's official architecture guide calls it "central LLM dynamically decomposes tasks and delegates to worker LLMs."
