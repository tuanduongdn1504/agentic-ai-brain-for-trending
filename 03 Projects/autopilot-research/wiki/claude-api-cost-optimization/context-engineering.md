# Context Engineering (Tool Search · Programmatic Tool Calling · Compaction)

> Lever #2 in [[_index]]. *"The art and science of deciding what context to give Claude so the agent performs best."*
> The talk's discipline: **read the transcript** to see what the model actually sees — you're often sending far more than the task needs.

Agents fill the context window after a few turns because (a) all tool definitions are loaded up front and (b) raw tool results are dumped in whole. Three techniques fix this. All are real Anthropic features.

---

## 2a. Tool Search Tool

**Problem:** defining dozens–hundreds of tools means all their schemas sit in context, crowding out actual work. (Demo: one tool was 14K tokens, its result list 6.1K, another 9.3K.)

**Mechanism:** instead of loading every tool definition, pass a single *tool-search* tool. Mark heavy tools `defer_loading: true`. The model calls tool-search when it needs a capability; only the matched tool's definition is then loaded into context on demand. Discovered schemas are *appended* (not swapped), so the prompt cache is preserved.

**Apply:** include `tool_search_tool_bm25_20251119` (BM25) or `tool_search_tool_regex_20251119` (regex) in `tools`; mark deferred tools with `defer_loading: true`. (GA — confirmed via the bundled `claude-api` skill SDK references.)

**Claimed result:** Lovable cut token consumption ~10% AND improved model performance (less context clutter), then rolled it out to all users. *(Customer + 10% figure are speaker anecdote — not independently published; see [[source-provenance]].)*

---

## 2b. Programmatic Tool Calling

**Problem:** a tool returns a huge blob (e.g. Gong sales-call transcripts) but you only need a slice (overall sentiment), yet the whole blob lands in context.

**Mechanism:** Claude writes a small Python script (in the code-execution container) that calls the tools as functions, filters/aggregates the results with normal control flow, and returns **only the relevant subset** to the model. Intermediate results never enter Claude's context. Works because Claude is strong at writing code.

**Apply:** enable `code_execution_20260120`; define custom tools with `allowed_callers: ["code_execution_20260120"]`. (GA — confirmed first-party; free when used alongside web search/fetch, else ~$0.05/hr.) Anthropic reports performance gains with fewer input tokens on agentic-search benchmarks. *(Exact "+11% / −24%" figures were unverifiable in first-party text; the feature and direction are confirmed.)*

**Claimed result:** Quora applied it to HTML content — strip irrelevant markup, keep the core, improve model performance. *(Anecdote.)*

---

## 2c. Compaction

**Problem:** long autonomous runs hit the 1M-token context limit and stop.

**Mechanism:** near the limit, the API summarizes earlier context into a compaction block, drops unneeded turns, and continues — giving near-infinite *effective* context while keeping the model on-track.

**Apply:** beta header `compact-2026-01-12`; `context_management: {edits: [{type: "compact_20260112"}]}`. **Default trigger ~150K tokens, configurable (min 50K)** — the talk picked 400K for its demo. **Critical:** append the full `response.content` (not just text) each turn or you silently lose the compaction state. You write your own summarization prompt to steer what's kept. *(Claim "Hex used it + simplified their code" is anecdote.)*

**Sibling — Context Editing** (`clear_tool_uses_20250919` / `clear_thinking_20251015`): *prunes* stale tool results/thinking instead of summarizing. Use editing to drop dead weight; compaction to summarize when near the limit. Docs: `.../build-with-claude/context-editing`.

---

## Key Takeaways

- Three orthogonal context levers: **shrink tools** (search), **shrink results** (programmatic calling), **shrink history** (compaction/editing).
- Each is *intelligence-positive*: less junk context → better model performance, not just lower cost.
- The unifying habit: **read the transcript** and ask "is the model seeing only what this task needs?"

Related: [[prompt-caching]] (tool search preserves the cache by appending), [[advisor-strategy]] (next lever), [[demo-cost-progression]].
