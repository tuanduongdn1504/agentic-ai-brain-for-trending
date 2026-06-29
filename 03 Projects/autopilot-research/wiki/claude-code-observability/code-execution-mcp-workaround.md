# The MCP token-cost workaround — code execution

> **Source video:** "Claude Code + OpenTelemetry = Claude Command Center" by Mansel Scheffel (2026-04-22, 15:54) — [12:44] "code execution with MCP / programmatic tool calling"
> "There are ways around using MCP directly. We can use code execution...it deserves its own deep dive."

## Source

**Raw file:** `../../raw/2026-06-20-claude-code-otel-command-center.md`

**Original resources:**
- Anthropic Engineering: [Code execution with MCP: building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp)
- Anthropic Platform docs: [Tool Search Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)
- Anthropic Platform docs: [Programmatic Tool Calling (PTC)](https://platform.claude.com/cookbook/tool-use-programmatic-tool-calling-ptc)
- Claude Cookbook: [Programmatic tool calling examples](https://platform.claude.com/cookbook/)

---

## The problem: MCP token bloat

**MCP is token-hungry for two structural reasons:**

- **Upfront schema cost:** Tool definitions (JSON Schema with examples, error formats, descriptions) load into context before any tool execution begins. A typical multi-server MCP setup (GitHub + Slack + Sentry + Grafana + Splunk) costs **~55,000 tokens** just in tool definitions—*before the model does any work*.
- **Intermediate result feedback loop:** Every tool call returns results that flow back through the model context. When a skill chains multiple tool calls sequentially (search → read → update → confirm), each intermediate result adds tokens to the context. Complex workflows *pollute context* at every step.

⚠️ **Video claim:** The creator mentions Notion tools (update-pages, create-databases, search) show "high latency + error rates" at [12:44], but **does not cite specific latency/error numbers**. Community reports confirm MCP overhead is real, but published production Notion deployments with quantified latency are rare. Anthropic's engineering documentation uses hypothetical examples (Google Drive, Salesforce, Slack), not production Notion instances.

---

## The workaround: three mechanisms

### 1. Progressive disclosure (on-demand tool discovery)

Instead of loading all tool schemas upfront, load only the tools Claude needs for the task.

- **Tool search:** Query the MCP server's tool catalog (like a filesystem `ls` instead of `find`) with either:
  - **`tool_search_tool_regex_20251119`** — Python regex patterns (case-sensitive by default; use `(?i)` for case-insensitive matching)
  - **`tool_search_tool_bm25_20251119`** — Natural language queries (fuzzier, better for non-technical tool names)
- **Result:** Load only **3–5 most relevant tools** per query, not the entire 50+ tool catalog.
- **Token savings:** >85% reduction (55,000 tokens → ~8,000 tokens typical).

**Gotcha:** At least one tool must be non-deferred. If `defer_loading: true` on all tools, the search fails. The `tool_search_tool` itself must NOT be deferred.

### 2. Client-side filtering (data aggregation before context entry)

Claude writes code that *calls MCP tools as functions* (not direct model tool-use), aggregates/filters the results in the execution container, and returns only the distilled answer to the model context.

- **Code execution container:** Stateful environment that persists across multiple API calls within a session. Maintains access to MCP tool functions for direct invocation.
- **Workflow:** 
  1. Claude requests a tool (e.g., "search for Q")
  2. Code execution environment calls the tool, receives raw result (JSON)
  3. Code filters, transforms, and aggregates in-container (no context feedback)
  4. Only the summary returns to Claude's context (e.g., "found 3 results: A, B, C")
- **Token savings:** 98.7% reduction documented (150,000 tokens → 2,000 tokens in Anthropic's published example)
- **Real-world example:** Programmatic tool calling (PTC) reduces a typical multi-step workflow from 110,473 tokens to 15,919 tokens = **85.6% reduction**.

### 3. Single-step logic (code-based loops eliminate chained API calls)

Instead of looping: "call tool → get result → decide → call tool → get result → decide", Claude writes a loop in the execution container that runs entirely client-side.

- **Example:** Instead of 5 sequential API calls (search → read → read → update → confirm), Claude writes Python that opens the connection once, reads all results in-memory, filters, and updates—*all in one code block*.
- **Benefit:** Eliminates 4 unnecessary context round-trips + intermediate token bloat.

---

## Programmatic Tool Calling (PTC) configuration

When tools are configured for code execution, add the **`allowed_callers`** field to each tool definition:

```json
{
  "name": "search_tool",
  "description": "Search database",
  "allowed_callers": ["code_execution_20250825"]
}
```

**Two modes:**
- **`["code_execution_20250825"]`** — tool callable ONLY by code execution (PTC-only)
- **`["direct", "code_execution_20250825"]`** — tool callable by both model (direct tool-use) OR code execution (dual-mode)

**Recommendation:** Choose one mode clearly for each tool. Mixing both can confuse tool selection logic. Prefer `["code_execution_20250825"]` for workflows where you are intentionally moving to code-based execution; use `["direct", "code_execution_20250825"]` only if the tool must remain callable directly AND via code execution.

---

## Documented token savings (verified)

| Scenario | Traditional | Code Execution | Savings |
|---|---|---|---|
| **Multi-step workflow (Anthropic example)** | 150,000 tokens | 2,000 tokens | **98.7%** |
| **PTC real-world (cookbook)** | 110,473 tokens | 15,919 tokens | **85.6%** |
| **Input tokens (PTC variant)** | 771,000 tokens | 165,000 tokens | **78.5%** |
| **Tool search + defer_loading (typical)** | ~55,000 tokens | ~8,000 tokens | **>85%** |

---

## How this fixes MCP observability insights

⚠️ **Video context:** The creator observes high latency + error rates on certain MCP tools at [12:44] and defers explanation to "another video" — this article resolves that deferral.

The observability dashboard (from [[claude-code-opentelemetry]]) panels reveal:
- **MCP latency/error rate** — shows slowest tools
- **Token usage per MCP call** — shows bloat

Code execution *solves both* because:
1. **Latency reduction:** Sequential API calls collapse into single code execution → fewer network round-trips.
2. **Error rate reduction:** Client-side retry logic + filtering in-container → fewer model context loops that trigger error states.
3. **Token cost:** Filters bloat before results re-enter context.

---

## Limitations & gotchas

- **Code execution container not universal:** Available on Max/Pro plans (not all tiers). Enterprise may have different policies.
- **Tool search at capacity:** Max 10,000 tools in catalog. Regex patterns max 200 characters.
- **Regex variant (`tool_search_tool_regex_20251119`) is strict:** Python regex syntax, case-sensitive by default. Use `(?i)` flag for case-insensitive matching.
- **At least one tool must be non-deferred:** If all tools have `defer_loading: true`, tool search fails. Tool search itself must NOT be deferred.
- **Container state expires:** Track `container_id` across requests to persist state. Container expires after defined interval (check Anthropic docs for timeout specifics).
- **Notion deployment visibility:** The creator mentions Notion tools in the video, but Anthropic's engineering post uses *hypothetical* examples (Google Drive, Salesforce, Slack). Production Notion deployments with code execution have not been formally documented by Anthropic.

---

## Key takeaways

- **MCP bloat is structural:** ~55K tokens upfront + intermediate result feedback loop; compounds in workflows with chained tool calls.
- **Code execution trades context-height for code-complexity:** Write more code (Python loops), save tokens + latency.
- **Three mechanisms compose:** Progressive disclosure (tool search) + client-side filtering (code-based aggregation) + single-step logic (loops in-container) yield 85–98% token reduction.
- **Observability enables diagnosis:** The MCP latency/error-rate panels in [[mcp-and-skill-cost-metrics]] reveal which tools justify refactoring to code execution.
- **Requires explicit tool config:** Add `allowed_callers: ["code_execution_20250825"]` to enable PTC.
- **Sister to other cost levers:** This is Lever 2b of [[../claude-api-cost-optimization/_index]] — alongside tool-search (2a), defer-loading (2c), and cache hit rate (Lever 1).

---

## Related articles

- [[claude-code-opentelemetry]] — metrics + events that reveal MCP cost
- [[mcp-and-skill-cost-metrics]] — observability panels for latency/error-rate/token-spend
- [[../claude-api-cost-optimization/_index]] — full cost-reduction framework (Levers 1–5)
- [[../autonomous-loops-human-in-the-loop/_index]] — HITL approval pattern (complements code execution for safety)
- [[../claude-skills/_index]] — skill cost-per-run + performance tuning
