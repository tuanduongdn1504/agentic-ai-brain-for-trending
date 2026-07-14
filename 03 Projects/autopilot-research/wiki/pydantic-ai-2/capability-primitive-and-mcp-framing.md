# The capability primitive — and the MCP-framing error

## The definition (CONFIRMED)

Official Pydantic AI v2 launch article, verbatim: *"A capability bundles an agent's instructions, tools, lifecycle hooks, and model settings into a single, composable unit."* Cole's on-screen paraphrase matches this almost word-for-word. Independently cross-checked against the capabilities reference docs (`pydantic.dev/docs/ai/core-concepts/capabilities/`), which confirm the same four components and describe capabilities as "the primary extension point for Pydantic AI."

This is a real architectural consolidation, not a rename: pre-v2, an `Agent` took separate constructor kwargs for instrumentation (`instrument=`), tool prep (`prepare_tools=`), history processing (`history_processors=`), and MCP servers (`mcp_servers=`). v2.0 removes all of these from the `Agent()` constructor and routes them through capabilities instead (confirmed in the v2.0.0b1 changelog).

## Where the video overstates: "MCP servers are a subset of a capability"

**Verdict: MISLEADING.**

Cole's framing: *"it's also useful to think about capabilities as the layer above MCP servers... MCP servers are a subset of what you add into a capability."*

The actual architecture inverts this. Per the capabilities docs and the MCP overview page (`pydantic.dev/docs/ai/mcp/overview/`):

- Capabilities are the unifying wrapper that can *reference* an MCP server as one tool-source among several (alongside function tools, instructions, hooks, settings).
- MCP servers aren't "contained inside" a capability as a sub-component you select from; you *pass* an MCP server to the capability layer, you don't extract one *out of* a capability.
- You can also use `MCPToolset` directly via `toolsets=[...]` without going through a capability at all — meaning capabilities aren't even the sole access path to MCP.

So "capability wraps/manages MCP as one integration option" is accurate; "MCP servers are a subset of what you add into a capability" gets the containment relationship backwards. It's a small conceptual slip in an otherwise accurate explanation, not a factual error about what exists.

## Cross-link

This complements [[../harness-engineering/terminology]]'s discussion of how "harness" and adjacent architecture terms get used loosely across frameworks — Pydantic AI's capability/MCP relationship is another instance of a real mechanism described with an imprecise containment metaphor.
