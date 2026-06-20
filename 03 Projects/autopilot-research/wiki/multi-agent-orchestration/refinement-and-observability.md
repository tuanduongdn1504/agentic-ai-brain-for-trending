# Refinement loops & observability

> **Source:** "Claude Architect: Multi-Agent Orchestration" (ExamPro, Andrew Brown, 2026-04-29); sections 7–8. Crosswalks to Anthropic "Building Effective Agents" (evaluator-optimizer pattern) and "Multi-agent research system" (observability, tracing, production engineering).

## Refinement loops: from one-shot to iterative

- **One-shot problem:** Initial coordinator invocation completes and submits. If coverage is incomplete (e.g., narrow decomposition misses critical angles), there's no mechanism to detect or repair gaps before returning the result.
- **Refinement pattern:** Run initial partitions → invoke an `evaluate_coverage` tool → identify missing angles → invoke only the screening agents needed to fill those gaps → repeat up to a max (3–4) iterations → submit_final only after coverage evaluation confirms sufficient coverage.
- **This IS the evaluator-optimizer pattern** from "Building Effective Agents" — one subsystem generates responses; another evaluates and provides feedback; loop iterates until satisfaction criteria met.
- **Critical caveat:** in the demo, the coverage score actually went DOWN across iterations. Andrew flags that "is it good?" requires real datasets + hours of eval. Pedagogical emphasis: "no magic here; don't trust one-shot coverage metrics; real evaluation takes discipline."

### Evaluate_coverage tool design

- Takes the current results (say, multiple resume screenings) as input.
- Returns a structured evaluation: `{coverage_score: float, gaps: [list of missing angles], recommendations: [list of targeted follow-ups]}`.
- Comparison to "Building Effective Agents": the evaluator subsystem in the evaluator-optimizer pattern must be domain-specific and callable repeatedly; `evaluate_coverage` is one concrete realization.
- Honest output: if score went down, report it. The pattern survives bad luck; silencing the signal does not.

### Loop safeguards

- **MAX iterations cap (3–4):** prevents runaway loops and budget explosion. In the demo, MAX-STEPS on the coordinator itself ≈10 (roughly 2× the expected ~5 steps) — a separate guard.
- **Coverage gate before submit_final:** Don't declare victory until the evaluation confirms coverage is sufficient. Moves the quality bar from "did it run?" to "does it cover what we care about?"

### Connection to "Building Effective Agents"

- **Evaluator-Optimizer pattern definition:** "One LLM generates responses while another provides evaluation and feedback in iterative loops."
- **Wide-then-narrow strategy:** Start broad, evaluate landscape, progressively narrow. Refinement loop embodies this: initial broad partition → evaluate what's missing → narrow follow-up passes → converge.

---

## Observability: the coordinator as a choke point

- **Architectural advantage:** Centralized coordinator owns every message, tool invocation, and result aggregation. It is the single point where you can observe the entire system's behavior, catch errors consistently, and control what context crosses into and out of isolated sub-agents.
- **Decentralized alternative:** If spokes can invoke each other directly, you lose observability (can't see all paths), error handling is fragmented (different spokes have different error strategies), and context boundaries become diffuse.
- **Honest audit of the initial demo build:**
  - Only print statements (not structured logs).
  - No error handling around json.loads (would crash if response is malformed).
  - No API tracing (token counts, latency, request IDs).
  - Spoke responses never persisted to disk.
  - Every spoke receives the full job posting, regardless of partition.
  - Spokes cannot reject out-of-scope questions.
  - No mid-run gap detection (coverage check only at the end).
  - Single-pass results submitted without refinement loop.

### Refactoring for production-grade observability

- **Structured, timestamped logging** with levels (DEBUG, INFO, WARN, ERROR) — replaces print statements.
- **Error handling:** Wrap dangerous calls (json.loads, API calls) in try-catch; return structured error objects so the coordinator can decide next steps, not crash.
- **Persist scoped spoke I/O:** Save each spoke's input and output separately (keyed by partition ID). Enables debugging, auditing, replay.
- **Coverage gate:** The `evaluate_coverage` tool fires before loop iteration; if score is still low, flag it explicitly (don't silently continue).
- **Forced exit gate:** A `submit_final` tool that the coordinator MUST invoke (not just return) — ensures final state is logged and audit trail is complete.
- **Structured logging format: JSONL** (newline-delimited JSON) — machine-readable, parseable for analytics, no ambiguity about multi-line logs.
- **Timestamped human-readable coverage report:** Generate a summary to `reports/` at the end of the run (for human review + debugging).

### Code organization for observability

The refactored coordinator architecture (from section 9):

```
prompts/                    — system prompts as markdown files (one per role)
tools/                      — each tool in its own .py file
tools.json                  — tool schemas (JSON)
lib/
  ├── partitions.py         — partition generation logic
  └── logger.py             — centralized logging setup
data/                       — input data (e.g., job postings, resumes)
logs/                       — JSONL logs (one per run)
reports/                    — human-readable summaries
tools.py                    — entrypoint importing all tools
main.py                     — main coordinator loop (thin, reads prompts from prompts/)
```

**Theme:** Technical ownership — you must know exactly what the code does. Small, documented functions act as self-documenting code. Stateless classes (static methods) make inputs/outputs explicit and testable. JSONL logs enable post-hoc analysis without relying on print-grep archaeology.

---

## Connection to "Building Effective Agents"

- **Orchestrator-workers pattern:** The source defines a central LLM that "dynamically decomposes tasks and delegates to worker LLMs, synthesizing results." The coordinator is the orchestrator; spokes are workers. Centralization enables the observability described here.
- **Core principles:** The source emphasizes "maintain simplicity" and "prioritize transparency through explicit planning steps." Structured logging + error handling + JSONL output embody transparency; the coordinator's control flow is explicit and auditable.
- **Tool documentation & testing:** The source advises "craft agent-computer interfaces via thorough tool documentation and testing." Each tool (create_task, evaluate_coverage, submit_final, etc.) needs clear contracts; JSONL logs provide a test harness for post-run analysis.

---

## Production deployment: containers + OpenTelemetry

- **Container per sub-agent:** Each spoke (keyword scanner, deep evaluator, red-flag detector, aggregator) runs in its own container with isolated filesystem, environment, and resource limits. The coordinator orchestrates the containers and collects their logs to a central store.
- **OpenTelemetry as a second observability layer:** Beyond application-level JSONL logs, OpenTelemetry (OTel) instruments the coordinator's LLM calls (token counts, model routing decisions, tool-use latencies, subagent invocation patterns). Feeds into a metrics backend (Prometheus, Datadog, etc.) for real-time dashboards and alerting.
- **Compared to the Anthropic sources:** **"rainbow deployments"** (gradual traffic shift between versions) is a production pattern from **"How we built our multi-agent research system"** — *not* from "Building Effective Agents" (which focuses on transparency + agent-computer-interface craft). Structured observability is the prerequisite for that kind of safe rollout — you must see decision patterns and error rates before shifting traffic. (The "observability-is-a-prerequisite" link is a sound inference, not a verbatim source claim.)

### Lightweight planning aid (section 8 addendum)

- **README with task checklist:** The coordinator can maintain a simple markdown checklist (e.g., "[ ] decompose task, [ ] create partitions, [ ] invoke keyword scanner, [ ] invoke deep evaluator, [x] evaluate coverage, [ ] refine gaps, [ ] submit final"). Claude checks off items as the loop progresses. "Not exactly spec-driven development, but a lightweight planning artifact."

---

## Comparison to "multi-agent research system" (Anthropic blog)

- **Observability patterns align:** Anthropic's research system monitors "decision patterns and interaction structures (without accessing conversation contents)" — a similar principle to the coordinator logging tool invocations and results. The source notes "monitoring without content access" as a privacy-preserving observability pattern.
- **Separation of concerns:** Anthropic scales effort by query complexity — 1 agent for simple fact-finding, 10+ for complex research. The video's partition planner / coordinator separation is a similar scaling principle applied at the choreography layer.
- **Task description specificity:** The source emphasizes "each subagent receives specific research tasks with distinct purposes. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information." The video's early EV-market mistake (narrow decomposition) is the same failure mode; the fix (decompose-time review + aggregate-time check) prevents it.

---

## SDK & tooling updates (section 9-10 summary)

- **Manual tool-use to @tool decorator:** The initial coordinator used hand-rolled Anthropic SDK with manual JSON schemas and a while-True tool-use loop. Porting to Claude Agent SDK replaced this with `@tool` decorators (define tool signature + handler inline) and `create_sdk_mcp_server` (bundles tools into an in-process MCP server).
- **Why it matters for observability:** The @tool decorator + SDK client handle tool schema validation + dispatch automatically. The coordinator code shrinks; error handling is more consistent; hooks (PreToolUse, PostToolUse) attach observability instrumentation at a defined attachment point.
- **MCP server runs inside the application** (not as a separate process) — no IPC latency, easier to test, all logging goes to the same output stream.

### Quote from the video

> "The tool-use call got easier and it's setting up an MCP server… clearly Anthropic is making that a priority." (Andrew Brown on SDK porting experience.)

---

## Key Takeaways

- **Refinement loops are the evaluator-optimizer pattern in practice:** one subsystem (spokes) generates results; another (evaluate_coverage tool) evaluates coverage; coordinator iterates until satisfied or MAX iterations reached.
- **Honest feedback loops matter:** in the demo, coverage score went DOWN — that's the signal; don't ignore it. Real evaluation requires datasets + hours.
- **Centralized coordinators enable observability:** all messages, all errors, all context boundaries flow through one point. Decentralized architectures lose observability.
- **Weak observability (print-only, no error handling, no tracing, no persisted I/O) is the default — refactor it away:** structured logging + error handling + JSONL output + scoped I/O + coverage gates + forced exit gates.
- **Modular code architecture (prompts/ tools/ lib/ logs/ reports/) mirrors observability discipline:** small functions, clear I/O contracts, stateless classes, JSONL logs enable human understanding and post-hoc debugging.
- **Production observability stacks:** add containerization (per-agent isolation) + OpenTelemetry (metrics/traces) on top of application-level JSONL logging — enables safe deployments and real-time dashboards.
- **The SDK makes observability instrumentation easier:** @tool decorators + hooks (PreToolUse, PostToolUse) + in-process MCP server provide defined attachment points for logging + error handling + tracing.