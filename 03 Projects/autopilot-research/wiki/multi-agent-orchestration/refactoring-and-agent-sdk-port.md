# Coordinator refactoring & porting to the Claude Agent SDK

> **Source:** ExamPro "Claude Architect: Multi-Agent Orchestration" (Andrew Brown, April 29 2026, 2h9m); Anthropic "Building Effective Agents"; Anthropic Claude Agent SDK Documentation; Anthropic Claude Code sub-agents Documentation

## REFACTORING: The Human-Ownership Lesson

The monolithic coordinator (a single `main.py` with everything inlined) works **only because it's held in memory**. It compiles, it runs—but it doesn't scale, isn't maintainable, and nobody can verify what it actually does without reading a 500-line function.

**The refactoring moves:**

- **Prompts:** system prompt and tool descriptions → separate Markdown files in `prompts/` directory; one file per agent role (coordinator prompt, spoke descriptions, routing rules)
- **Tool implementations:** each tool (`create_task`, `get_task_status`, `complete_task`) → its own `.py` file in `tools/`; tool JSON schemas → `tools.json` for reference or discovery
- **Shared utilities:** partition generation logic → `lib/partitions.py`; consistent logger → `lib/logger.py` (centralized formatting, timestamp handling, error handling)
- **Data structures:** input/output data → `data/` folder (JSON templates, partition schemas)
- **Logs:** structured JSONL output → `logs/` directory (parseable, timestamped, queryable)
- **Reports:** human-readable coverage report with timestamps → `reports/` directory (what did we screen? what gaps remain? score over time?)

**Code style for clarity:**

- **Stateless classes** with static methods (or module-level functions): no hidden state in `self`. Inputs and outputs are explicit, easy to mock/test. "The AI can write tests but that doesn't make them good or reliable tests"—you must know exactly what the code does.
- **Small functions instead of nested blocks:** break the big `run_coordinator()` loop into many small functions that **act as documentation**: `should_invoke_keyword_scanner()`, `aggregate_spoke_results()`, `check_coverage_sufficient()`. Each function name explains what it does; reading the code is reading the spec.

**Theme:** **technical ownership.** You are responsible for verifying the code does what you think it does, not trusting that it compiled. This discipline carries through to orchestration: a coordinator that cannot be audited is a coordinator you don't control.

---

## AGENT SDK PORT: The Payoff

Once the monolith is modular, porting to the Claude Agent SDK unlocks two major simplifications:

### 1. **@tool Decorator Replaces Manual JSON Schemas**

**Before (raw Anthropic SDK):**
```python
# Manual tool definition
tools_definitions = [
    {
        "name": "create_task",
        "description": "Create a new screening task...",
        "input_schema": {
            "type": "object",
            "properties": {
                "job_posting": {"type": "string"},
                "applicant_resume": {"type": "string"}
            },
            "required": ["job_posting", "applicant_resume"]
        }
    }
]

# Hand-rolled dispatch loop
while True:
    response = client.messages.create(
        model="claude-3-5-sonnet",
        tools=tools_definitions,
        messages=messages
    )
    for content_block in response.content:
        if content_block.type == "tool_use":
            # manually call the tool, add result to messages
```

**After (Claude Agent SDK):**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server, query, ClaudeAgentOptions

@tool("create_task", "Create a new screening task...", {"job_posting": str, "applicant_resume": str})
async def create_task(args) -> dict:
    job_posting, applicant_resume = args["job_posting"], args["applicant_resume"]
    # implementation
    return {"task_id": task_id, "subtasks": subtasks}

# Decorator captures name, description, input schema, handler. SDK infers schema from type hints.
# No manual JSON schemas. No hand-rolled dispatch loop.
```

**The `@tool` decorator can be applied inside a factory function** so it captures state via closures (the exact decorator-evaluation timing — definition-time vs. call-time — isn't documented in the SDK; the video author calls it "call time," which is his framing). This means:
- Tools can live separately in `tools/*.py` **and still bind coordinator state** (closure captures what the coordinator passes in)
- SDK handles the tool-call dispatch automatically

### 2. **create_sdk_mcp_server: In-Process MCP Bundling**

**The SDK creates an internal MCP server that runs inside your application**, not as a separate process:

```python
# Create tools via @tool decorator
server = create_sdk_mcp_server(
    name="coordinator-tools",
    version="1.0.0",
    tools=[create_task, get_task_status, complete_task]
)

# Pass the server to the query() async client
async for message in query(
    prompt="Analyze this job posting and resume...",
    options=ClaudeAgentOptions(
        mcp_servers={"coordinator": server}
    )
):
    # Claude autonomously invokes tools; SDK handles dispatch
```

**The hand-rolled while-True loop disappears.** Instead, you get `query()`, an async iterator that:
- Manages the agent loop internally
- Automatically invokes tools when Claude needs them
- Handles tool results and error recovery
- Returns messages as they arrive

### 3. **Async Client: AsyncAnthropic → SDK Client**

The raw Anthropic SDK uses:
```python
client = anthropic.AsyncAnthropic(api_key=...)
response = await client.messages.create(...)
```

The Claude Agent SDK replaces this with:
```python
async for message in query(prompt="...", options=ClaudeAgentOptions(...)):
    # Process each message as it arrives (streaming)
```

**Cleaner, more reactive, integrates loop control natively.**

---

## Key Insight from Andrew Brown

> "The tool-use call got easier and it's setting up an MCP server... clearly Anthropic is making that a priority."

The refactoring + SDK port demonstrates why:
1. **Ownership is clearer:** You can read the code and know what it does.
2. **Tool-use is declarative:** @tool decorator + internal MCP server remove boilerplate.
3. **Scaling is simpler:** Stateless classes and small functions compose without coupling.

This is the transition from "does it run?" to "can I control it?"

---

## Architecture: Hub-and-Spoke Coordinator

The refactored coordinator runs as a **hub**. Sub-agents (spokes) never communicate directly; all communication routes through the coordinator:

- **Coordinator owns:** task decomposition (break user query into subtasks), routing (which spoke handles what), context-sharing (a spoke only knows what the coordinator injects), result aggregation (combine spoke outputs into one answer), error handling (consistent retry/fallback logic), observability (single choke point for logging, tracing, audits)
- **Spokes are stateless:** execute one focused task, return results, no knowledge of other spokes or each other's intermediate steps

**Why hub-and-spoke works:**
- Observability: every message passes through the coordinator, so you can audit/trace everything
- Context isolation: spokes only see what they need (prevents information leakage, reduces token waste)
- Error recovery: coordinator can detect failures and retry/reroute (spokes don't need to know about failures elsewhere)

---

## Crosswalk to [[multi-agent-orchestration/agent-sdk-deep-dive]]

- @tool decorator and internal MCP server creation: see Agent SDK deep-dive for full API reference (Python `create_sdk_mcp_server` / TypeScript `createSdkMcpServer`)
- Subagent definitions (YAML frontmatter + Markdown prompt): see Claude Code sub-agents documentation and deep-dive for context isolation and tool allowlist/denylist
- Hooks for observability (PreToolUse, PostToolUse, Stop): detailed in Agent SDK docs; applied here via structured logging in refactored code
- Query async iterator and ClaudeAgentOptions: see Agent SDK API reference
- Session management and resume: relevant for persistence across coordinator restarts

---

## Key Takeaways

- **Refactoring for human ownership is non-negotiable:** a working system you don't understand is one you can't control. Break monoliths into prompts/, tools/, lib/, data/, logs/, reports/.

- **Stateless classes and small functions are documentation:** naming them well makes the code self-explanatory; this discipline forces you to think about what each piece does.

- **@tool decorator + internal MCP server simplify tool-use:** replacing manual JSON schemas and hand-rolled dispatch loops with declarative tool definitions and SDK-managed loops reduces boilerplate and cognitive load.

- **Closures let tools bind coordinator state:** tools can live in separate files (tools/*.py) and still capture the coordinator instance or configuration via closure, enabling modular code without sacrificing access to shared context.

- **Hub-and-spoke topology is the architectural contract:** the coordinator decomposes, routes, aggregates, and observes. Spokes execute focused tasks statelessly. No direct spoke-to-spoke communication. This contract enables auditing, error recovery, and scaling.

- **Real evaluation takes hours, not seconds:** the demo's coverage score went DOWN on iteration. "Just because it ran doesn't mean it's good." Automated tests are necessary but insufficient. Human judgment and datasets are required for production.

- **Observability is a refactoring target, not an afterthought:** move from print-statements to structured JSONL logging, error handling around critical calls (e.g., json.loads), request tracing (token counts, latency, request IDs), and human-readable reports. Productionize with container-per-agent + OpenTelemetry.