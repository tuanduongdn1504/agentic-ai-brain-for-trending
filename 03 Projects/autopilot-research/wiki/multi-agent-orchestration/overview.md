# Multi-agent orchestration — overview

> **Source:** ExamPro "Claude Architect: Multi-Agent Orchestration" — Andrew Brown / ExamPro (third-party paid course, [exampro.co/cca-f](https://www.exampro.co/cca-f)), [vRYBG_R8JAI](https://www.youtube.com/watch?v=vRYBG_R8JAI), 2026-04-29, 2h9m (~57K views at capture). **NOT first-party Anthropic.** Built LIVE in Python using the Anthropic SDK, then ported to the Claude Agent SDK. Pedagogical vibe-build: "just because it ran doesn't mean it's good"; real evaluation takes hours. See [[multi-agent-orchestration/source-provenance]] for what's verified vs. third-party framing.

## What is this source?

This is a **third-party teaching video**, not first-party Anthropic documentation. Andrew Brown (founder of ExamPro, a third-party training platform) walks through multi-agent orchestration patterns in real time, building a job-application screener with a central coordinator agent and isolated worker spokes. The architecture is grounded in Anthropic's published patterns, and the video ported the final code to the Claude Agent SDK to show production tooling. (The course is marketed at `exampro.co/cca-f`; whether ExamPro's "Claude Architect" branding maps to any official Anthropic certification is **unconfirmed** — see [[multi-agent-orchestration/source-provenance]].)

## Source lineage & origin

The patterns Andrew teaches originate in **three Anthropic deep dives**:

1. **[Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)** — defines Orchestrator-Workers, Evaluator-Optimizer, Routing, Parallelization, and when to use workflows vs agents. Deep-dived in [[multi-agent-orchestration/building-effective-agents-deep-dive]].
2. **[How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)** — Anthropic's production multi-agent system with Opus lead + Sonnet subagents; covers token economics, failure modes, observability, and scaling rules. Deep-dived in [[multi-agent-orchestration/multi-agent-research-system-deep-dive]].
3. **[Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)** — official SDK tooling: `@tool` decorator, `create_sdk_mcp_server`, in-process MCP, subagent definitions, hooks. Deep-dived in [[multi-agent-orchestration/agent-sdk-deep-dive]].

The explicit video↔source mapping lives in [[multi-agent-orchestration/video-to-original-crosswalk]].

The video re-teaches these patterns in concrete code with a single use case (job screener), then demonstrates the SDK primitives. It is pedagogical, not production-ready; Andrew explicitly notes observability gaps, coverage scores going backward, and that real evaluation requires hours of work.

## The core model: hub-and-spoke architecture

**One coordinator agent sits at the center.** Spokes (worker sub-agents) never communicate directly—all routing, context-sharing, and error handling flows through the coordinator:

- **Coordinator owns:** task decomposition (break complex query into subtasks), routing (which agents to invoke and when), result aggregation (combine outputs into one coherent response), and observability (single choke point for logging/errors).
- **Spokes own:** execution only. Stateless. They only see what the coordinator injects. No direct peer knowledge.
- **Communication topology:** coordinator ↔ spoke; never spoke ↔ spoke.

This contrasts with decentralized or peer-to-peer designs where agents negotiate directly. Hub-and-spoke trades flexibility for visibility and control.

## The 9-step arc

The video walks through a progression of refinements:

### 1. **Coordinator role & task lifecycle**

Coordinator prompt rules: "Do not do the work yourself." Decide routing based on query complexity—simple factual → single agent; multi-step → sequential pass-forward; independent subtasks → parallel invoke. Build a while-True loop with a MAX-STEPS cap (~10 = 2× expected ~5 steps) to catch runaway loops.

### 2. **Basic coordinator implementation**

Skeleton: `create_task`, `get_task_status`, `complete_task` tools. Use case: job-application screener with spokes for keyword scanning, deep evaluation, red-flag detection, score aggregation. Coordinator decomposes the resume, routes to the appropriate spoke, aggregates results.

### 3. **Narrow task decomposition — failure & fix**

The EV-market example: decompose "comprehensive EV market analysis" into only [sales, battery tech, manufacturers], silently miss charging infra, policy/subsidies, sentiment, supply chains, grid capacity. Each spoke works isolated; none can flag gaps.

**Fix:** Two safeguards. (a) At decompose-time, give the coordinator a tool to review the subtask breakdown—ask "what info is needed?"—before delegating. (b) At aggregate-time, check "before finalizing, did you cover X?"

**Realization:** the screener pattern generalizes to: one screening agent contextualized N ways, not N hard-coded agents.

### 4. **Dynamic selection**

Do not run the full spoke pipeline for every query (wastes tokens). Tell the coordinator to route based on case. "Never invoke a screening agent unless it answers a real question." Model generates routing **on the fly** (e.g., "non-traditional background → check transferable skills"). Hybrid (some coordinator-driven logic, some code-driven) is fine.

### 5. **Partitioning research**

Three research agents given the same brief → three overlapping answers + wasted tokens. Carve scope so each agent owns a distinct **non-overlapping** slice. Generate a JSON partition structure (agent + scope + cover + exclude).

**Andrew's architectural choice (the video's own elaboration, not an Anthropic-named pattern):** separate a PARTITION PLANNER (sees the input, owns routing rules, decides which partitions exist) from the COORDINATOR (dumb executor: invoke exactly one screening call per partition, don't invent extra angles). Putting routing in both = two places fighting.

### 6. **Refinement loop — evaluator-optimizer pattern**

One-shot runs are incomplete. Add a loop: run initial partitions → call `evaluate_coverage` tool → if insufficient, invoke agents only on identified gaps → repeat up to MAX (3-4 iterations) → `submit_final` only after evaluation confirms coverage.

**Reality check:** in the demo, the coverage score actually went DOWN across iterations. Andrew flags: "Is it good? Unknown—needs real datasets and hours of eval." No magic here.

### 7. **Observability — the centralized choke point**

The coordinator is the single choke point: it can observe every message, catch errors consistently, and control what context crosses boundaries (vs decentralized agents you can't observe).

Audit of the built system showed weak observability: only print statements, no error handling around JSON parsing, no API tracing/token counts/latency/request IDs, spoke responses never persisted, every spoke gets full context regardless of partition, spokes can't reject out-of-scope questions, single-pass can't detect gaps until submit.

**Refactoring fixes:** structured logging with timestamps + levels, try-catch error handling, persist spoke inputs/outputs scoped per partition, `evaluate_coverage` gate before submit, force `submit_final` exit gate. Later: containerize each sub-agent + OpenTelemetry tracing.

### 8. **Coordinator refactoring — code structure for ownership**

The monolithic main.py "is not good code." Refactor for human readability:

- Prompts → markdown files in `prompts/` folder
- Each tool → its own `.py` file in `tools/` + `tools.json` schemas
- Partition generation → `lib/partitions.py`
- Logger → `lib/logger.py`
- Prefer **stateless classes** (static methods) so inputs/outputs are mock-testable
- Break the big run-coordinator loop into many small **functions that act as documentation** (if/else → function calls)
- Data → `data/` folder; JSONL logs → `logs/`; human-readable coverage report → `reports/` with timestamp
- **Theme:** technical ownership—you must know exactly what the code does.

### 9. **Claude Agent SDK porting**

Port the raw Anthropic SDK coordinator to the Claude Agent SDK. Result: tool-use gets much simpler.

**Before:** manually define JSON schemas for each tool, hand-roll tool dispatch loop, parse responses.

**After:** `@tool` decorator on each function, bundle into an in-process MCP server via `create_sdk_mcp_server`. Decorator runs at call time, so tools can bind state via closures (tools/ files capture coordinator state while staying modular). Tools live in separate files, unified via decorator + MCP server.

Andrew observes: "the tool-use call got easier and it's setting up an MCP server... clearly Anthropic is making that a priority."

**Optional vision:** coordinator could route sub-agents to different models, or let the model pick the best model.

## Read next (this topic)

Video-knowledge articles:

- [[multi-agent-orchestration/hub-and-spoke-and-coordinator]] — the architecture + the coordinator's 4 jobs + basic build (sections 1–3)
- [[multi-agent-orchestration/decomposition-and-partitioning]] — narrow decomposition, dynamic selection, research partitioning (sections 4–6)
- [[multi-agent-orchestration/refinement-and-observability]] — refinement loop + observability choke point (sections 7–8)
- [[multi-agent-orchestration/refactoring-and-agent-sdk-port]] — code-for-ownership refactor + the Agent SDK port (sections 9–10)

Original-source deep-dives + the bridge:

- [[multi-agent-orchestration/building-effective-agents-deep-dive]] — Anthropic's pattern taxonomy (the source for the workflow patterns)
- [[multi-agent-orchestration/multi-agent-research-system-deep-dive]] — Anthropic's production orchestrator-worker system
- [[multi-agent-orchestration/agent-sdk-deep-dive]] — the Claude Agent SDK (the porting target)
- [[multi-agent-orchestration/video-to-original-crosswalk]] — the master video-term ↔ Anthropic-pattern mapping
- [[multi-agent-orchestration/source-provenance]] — verification log + what's third-party vs. confirmed

Sibling topics: [[harness-engineering/_index]] · [[prompt-evaluation/_index]] · [[claude-api-cost-optimization/_index]] · [[agentic-analytics-harness/_index]] · [[claude-md-12-rules/_index]]

## Pedagogical caveats

The video deliberately skips production rigor:

- No real datasets; no automated tests
- Observability weak initially (print statements, no API tracing)
- Refinement loop coverage score went DOWN—indicates "is it actually good?" requires hours of work
- Job screener is a teaching vehicle, not a deployed system
- Code is admittedly messy mid-build (the vibe-build style prioritizes narrative clarity over polish)

Andrew's repeated framing: **"Just because it ran doesn't mean it's good."** Human judgment and rigorous evaluation are mandatory.

---

## Key Takeaways

- **Hub-and-spoke architecture** isolates sub-agents and gives the coordinator visibility and control over all task decomposition, routing, result aggregation, and error handling. Spokes never talk directly.

- **Task decomposition narrowness is a failure mode.** Narrow decomposition can silently miss entire problem dimensions (e.g., EV market missing charging infra, policy, sentiment). Use decompose-time review tools + aggregate-time coverage checks to catch gaps.

- **Dynamic routing beats static pipelines.** Let the model decide which agents to invoke on-the-fly based on query characteristics. Don't waste tokens running full pipelines for simple queries. "Never invoke an agent unless it answers a real question."

- **Partition planners upstream of coordinators.** Separate the logic that decides "which agents exist and who owns what scope" from the logic that executes partition assignments. Prevents routing from being two places fighting.

- **Refinement loops + evaluator-optimizer pattern enable completeness.** Initial one-shot runs leave gaps. Loop: run → evaluate coverage → fill identified gaps → repeat (MAX 3-4). Coverage scores can go backward; real eval requires hours, not heuristics.

- **Observability comes from centralization.** Hub-and-spoke's single choke point (the coordinator) can log every message, catch errors consistently, and control context boundaries. This is a feature, not a limitation—decentralized designs can't observe failure patterns uniformly.

- **Code structure reflects ownership.** Refactoring for readability (prompts in files, tools in separate .py files, small functions as documentation, stateless classes) isn't polish—it's how you maintain technical accountability. The AI can write code; you must be able to verify it.

- **Claude Agent SDK simplifies tool-use.** The `@tool` decorator + in-process MCP server (`create_sdk_mcp_server`) replaces manual JSON schema + dispatch loop. Tools stay modular (separate files) while binding coordinator state via closures. Anthropic is prioritizing this as a core capability.