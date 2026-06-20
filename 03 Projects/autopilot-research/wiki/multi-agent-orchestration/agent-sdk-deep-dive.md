# Original resource #3 — the Claude Agent SDK

> **Source:** Anthropic Claude Agent SDK docs (`https://code.claude.com/docs/en/agent-sdk/`) + ExamPro "Claude Architect: Multi-Agent Orchestration" video (Andrew Brown, April 29, 2026, 2h9m)
> **Kind:** Original deep-dive — SDK primitives + video demonstration + primary-source verification

## What the Agent SDK is (renamed from Claude Code SDK)

- Official Python + TypeScript library from Anthropic that gives programmers **the same tools, agent loop, and context management that power Claude Code, programmable in your own codebase.**
- Replaces the raw `anthropic` Client SDK's manual tool-use loop with **automatic autonomous tool handling.**
- Supports Python 3.10+ and TypeScript. **Ruby is not supported** (confirmed in docs; video author wishes for it).
- Built atop the Claude API (same models, same pricing) but abstracts away the hand-rolled tool-dispatch machinery.

## The gather-context / take-action / verify-work loop

- **Gather context:** agent collects relevant files, executes queries, builds understanding of the problem.
- **Take action:** agent invokes tools to move toward the goal (read, write, execute, search, analyze).
- **Verify work:** agent checks outputs, detects errors, iterates until satisfied or reaches a stop condition.
- This loop **runs autonomously inside the SDK** — Claude handles tool calls without you manually parsing JSON or routing to functions.

## Primitives: tools, decorators, in-process MCP servers

### @tool decorator (Python) / tool() helper (TypeScript)

- Defines a custom function as a tool Claude can invoke.
- Python: `@tool('name', 'description', {'param': type, ...}, annotations=ToolAnnotations(...))`
- TypeScript: `tool('name', 'description', zod_schema, async_handler, {annotations})`
- **The `@tool` decorator can be applied inside a factory function**, so tools bind state via closures and live in separate files while still capturing coordinator state. (The exact decorator-evaluation timing is **not explicitly documented** in the SDK docs; the closure-via-factory mechanism is the load-bearing part. The video author frames it as "runs at call time" — treat that as his interpretation, not a documented guarantee.)
- Tool handlers are **async functions returning a dict with `content` (required array of blocks: text, image, audio, resource, resource_link) and optional `structuredContent` (JSON) + `isError` (bool).**

### create_sdk_mcp_server (Python) / createSdkMcpServer (TypeScript)

- **In-process MCP server** — runs inside your application, not as a separate process.
- **Replaces manual JSON tool schemas + tool-dispatch loops** with a single abstraction.
- Input: array of @tool-decorated functions. Output: an MCP server object that bundles them.
- Pass the server to `query()` via `mcp_servers` (Python) or `mcpServers` (TypeScript).
- **Confirmed:** SDK docs explicitly contrast Client SDK (you implement loop manually) vs Agent SDK (Claude handles tools autonomously). In-process MCP server is the mechanism.
- **Video author framing:** "the tool-use call got easier and it's setting up an MCP server... clearly Anthropic is making that a priority."

### ClaudeSDKClient + ClaudeAgentOptions + query()

- **ClaudeSDKClient:** async client (replaces `anthropic.AsyncAnthropic` from raw SDK) — configured via `ClaudeAgentOptions`.
- **ClaudeAgentOptions:** configuration object controlling:
  - `allowed_tools` (pre-approved tools) / `disallowed_tools` (scoped rules).
  - `mcp_servers` — which MCP servers to attach.
  - `agents` (subagent definitions).
  - `permission_mode` (acceptEdits, bypassPermissions, dontAsk).
  - `hooks` (PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit) for observability.
  - `resume` (session ID to resume past conversations).
- **query():** main agent loop as an **async iterator**. Python: `async for message in query(prompt='...', options=ClaudeAgentOptions(...))`. TypeScript: `for await (const message of query({...}))`. Returns messages as the agent thinks and acts.

## Subagents + orchestration

### What subagents are

- **Separate agent instances** your main agent can spawn to handle focused subtasks.
- Each subagent runs in its **own fresh context window** with a **custom system prompt, specific tool access, and independent permissions.**
- **Intermediate tool calls and results stay inside the subagent** — only the final message returns to the parent.
- **Context is isolated:** subagent does NOT see parent conversation history, previously read files, or other subagent outputs.

### Communication pattern (confirmed: hub-and-spoke, no direct spoke-to-spoke communication)

- **The only channel from parent to subagent is the Agent tool's prompt string** — include any file paths, error messages, or decisions the subagent needs directly in that prompt.
- When subagent completes, its result returns to the delegating agent (the parent). **Only the top-level subagent's summary returns to main conversation in nested scenarios.**
- **Documentation does NOT describe direct peer-to-peer communication between subagents.** All patterns route through delegation and result return. (Video's claim: "hub-and-spoke with spokes never talking directly" — matches documentation.)

### Subagent definition

- Markdown file with **YAML frontmatter + markdown body** (in Claude Code; SDK has programmatic AgentDefinition).
- Frontmatter fields: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `hooks`, memory, background, isolation, color.
- Markdown body becomes the **custom system prompt** (not the full Claude Code system prompt).
- **Automatic invocation:** Claude automatically decides when to invoke subagents based on the task and each subagent's description.
- **Explicit invocation:** name them via Agent tool or @-mention syntax.

### Nested subagents + depth limit

- Subagents can spawn nested subagents (recent Claude Code versions), with a documented depth limit before the Agent tool becomes unavailable. (Exact version + depth number drawn from the research fetch and **not re-verified** here — check current docs before relying on them.)
- Each invocation creates a new instance with fresh context; resumed subagents retain full conversation history.

## Hooks for observability

- **PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit** — run at key points in the agent lifecycle via callback functions.
- Example use case: PostToolUse hook logs file changes to an audit trail, catching what the agent modified and when.

## Sessions + resumption

- **Sessions maintain context across multiple exchanges** — conversation history persists.
- Capture `session_id` from one run and use it to resume with full conversation history in the next run.
- Transcripts are cleaned up based on `cleanupPeriodDays` setting (default: 30 days).

## Built-in tools

- Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion.
- Tool naming pattern for MCP tools: `mcp__<server_name>__<tool_name>`.
- **Tool search is enabled by default** — loads tools on demand to preserve context window.

## Language support

- **Python (3.10+) and TypeScript.** Ruby is NOT supported. (Video author correctly states this; docs confirm.)

## Video demonstration: hub-and-spoke coordinator + refactoring + SDK porting

### Architecture overview (Andrew Brown's build)

- **Coordinator** (main agent): owns task decomposition, routing, context-sharing, error handling, observability.
- **Spokes** (worker subagents): stateless execution. Each knows only what coordinator injects. **No direct inter-spoke communication.**
- Use case: **job-application screener** with spokes for keyword scanning, deep evaluation, red-flag detection, score aggregation.

### Key patterns demonstrated

**1. Task decomposition + delegation:**
- Coordinator breaks complex queries into subtasks.
- Routes to appropriate spoke based on case characteristics.
- Aggregates results into coherent response.

**2. Narrow decomposition problem (and fix):**
- ❌ Decomposing "EV market analysis" into only sales/battery/manufacturers misses charging infra, policy, sentiment, supply chains, grid capacity.
- ✅ Fix 1: decompose-time review tool (coordinator asks "what info is needed?" before delegating).
- ✅ Fix 2: aggregate-time check ("before writing the answer, did you cover X?").
- Realization: specificity and scope-clarity at delegation time prevent gaps. (Matches Anthropic research system: "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information.")

**3. Dynamic routing:**
- Model generates routing **on-the-fly** based on case characteristics (e.g., "non-traditional background → check transferable skills").
- Never invoke a spoke unless it answers a real question (avoids wasted tokens).
- Can add a tool to validate routing quality.
- Hybrid (some coordinator-driven code logic, some model-generated routing) is acceptable — "there are no rules here."

**4. Partitioning to avoid overlapping work:**
- Three research agents given the same brief → overlapping answers + wasted tokens.
- Carve scope so each spoke owns a **distinct non-overlapping slice** (partition).
- Generate a JSON partition structure (agent + scope + cover + exclude).
- **Separation:** PARTITION PLANNER (sees the input, owns routing rules, decides which partitions to create) vs COORDINATOR (dumb executor: invoke exactly one screening per partition).
- Putting routing logic in both places = two places fighting — consolidate routing upstream.

**5. Refinement loop (evaluator-optimizer pattern):**
- Initial run → call evaluate_coverage tool → if coverage insufficient, invoke spokes to **fill identified gaps** → repeat up to MAX (3-4 iterations) → submit_final only after evaluation confirms coverage.
- ⚠️ **Realism check:** in the demo, coverage score actually went DOWN across iterations. Andrew flags: "is it good? needs real datasets + hours of eval. No magic here."

**6. Observability (centralized coordinator as choke point):**
- Initial demo: weak observability (only print statements, no error handling around json.loads, no API tracing/token counts/latency/request IDs, spoke responses never persisted).
- Refactored toward: structured logging w/ timestamps + levels, error handling, persist spoke inputs/outputs scoped per partition, evaluate_coverage gate, force submit_final exit gate.
- Productionize later with: containers per sub-agent + OpenTelemetry.

### Coordinator refactoring for human readability

- **Prompts → markdown files** in `prompts/` folder.
- **Each tool → separate .py file** in `tools/` + `tools.json` schemas.
- **Partition generation → lib/partitions.py**.
- **Consistent logger → lib/logger.py**.
- **Prefer stateless classes** (with static methods) so inputs/outputs are easy to mock/test.
- **Break big run-coordinator loop into many small functions** that "act as documentation" (if/else blocks → function calls).
- **Data → data/ folder; JSONL logs → logs/ dir; timestamped human-readable coverage report → reports/.**
- Theme: **technical ownership** — you must know exactly what the code does. "The AI can write tests but that doesn't make them good/reliable tests."

### Agent SDK porting (tool-use simplification)

- **Before (raw Anthropic SDK):** manual JSON tool schemas + hand-rolled tool dispatch loop + error handling.
- **After (Claude Agent SDK):** 
  - @tool decorator on each function.
  - create_sdk_mcp_server wraps tools into an in-process MCP server.
  - Tools can live in `tools/` separately while still binding coordinator state via closures (decorator factory pattern).
  - Async client (anthropic.AsyncAnthropic) → SDK client with query() async iterator.
- **Claim verified:** SDK docs explicitly show @tool + create_sdk_mcp_server replacing manual JSON schemas + dispatch.
- **Author framing:** "the tool-use call got easier and it's setting up an MCP server... clearly Anthropic is making that a priority."

## Crosswalk: SDK primitives ↔ video usage

| Primitive | Video usage |
|---|---|
| `@tool` decorator | Each coordinator tool (create_task, get_task_status, etc.) + partition planner tools |
| `create_sdk_mcp_server` | Wraps all tools into server; pass to query() |
| `query()` async iterator | Main coordinator loop (`async for message in query(...)`) |
| `ClaudeAgentOptions` | Configure allowed_tools, hooks, permission_mode, subagents |
| Subagent (Agent tool) | Each spoke (keyword scanner, deep evaluator, red-flag detector) |
| Hooks (PostToolUse, etc.) | Observability: structured logging, audit trails |
| Sessions | Resume capability across runs (not explicitly shown in video, but SDK supports it) |

## Confirmed vs. author framing

✅ **Confirmed in source docs:**
- @tool decorator + create_sdk_mcp_server replace manual JSON schemas + dispatch loop.
- In-process MCP server runs inside the application (not separate process).
- Subagent context is isolated; only final message returns to parent.
- Hub-and-spoke communication pattern (no direct spoke-to-spoke).
- Python 3.10+ and TypeScript supported; Ruby not supported.
- Tool handlers return dict with `content` (required) + optional `structuredContent` + `isError`.
- Hooks provide observability callbacks at key lifecycle points.

⚠️ **Author framing (not explicitly confirmed in source docs):**
- Decorator runs at call time capturing state via closures — docs show factory pattern but don't detail decorator timing.
- Coordinator framing as a "dumb executor" vs partition planner as upstream router — SDK supports both patterns but doesn't use this terminology.
- MAX-STEPS cap at ~10 (2× expected ~5) as runaway loop guard — docs don't specify recommended loop caps or turning limits.
- Coverage score going DOWN across iterations — anecdotal from the demo, not a source claim.

## Claim about spokes never talking directly to each other

**Verified in Claude Code subagents docs:**
- "Each subagent runs in its own context window" with "isolated context."
- "Subagents work within a single session" — all communication via delegation + result return.
- Subagents work within a single session — all communication is via delegation + result return.
- The docs describe **no** direct peer-to-peer channel between hub-and-spoke spokes. (Separate parallel-session "team" mechanisms, where they exist, are out of scope here and unverified in this build.)
- **Conclusion:** video's "spokes never talk directly" claim is consistent with documentation.

## Key Takeaways

- The Agent SDK automates the tool-use loop that the raw Anthropic SDK forces you to hand-code — @tool decorator + in-process MCP server replace manual JSON schemas + dispatch.
- Hub-and-spoke coordinator architecture centralizes routing, context-sharing, error handling, and observability — the coordinator is the single choke point, enabling visibility and control.
- Subagents are context-isolated instances that return results to the parent; all communication flows through the coordinator's delegation mechanism (no direct spoke-to-spoke communication).
- Narrow task decomposition (and missing coverage) is a failure mode — fix it with scope-clarity at delegation time + coverage evaluation tools + refinement loops to fill identified gaps.
- Dynamic routing on-the-fly (model decides which spoke to invoke based on case) beats hard-coded paths for complex, variable workloads.
- Partition planning as a separate upstream concern (deciding WHICH partitions to create) prevents both duplication and gaps when multiple spokes might overlap.
- Observability through a centralized coordinator is cheap and powerful — every message passes through, enabling structured logging, error handling, and audit trails.
- Technical ownership requires readable code structure: prompts in files, tools in separate files, small functions as documentation, JSONL logs — "just because it ran doesn't mean it's good."
- Real evaluation of multi-agent systems takes hours and real datasets; simulations (even with falling coverage scores) are pedagogical, not proof of production readiness.
- Model tier and orchestration clarity matter more for performance gains than raw token budget — Anthropic's production research system (Opus lead + Sonnet subagents) outperformed single-agent Opus by 90.2% on internal research eval.
