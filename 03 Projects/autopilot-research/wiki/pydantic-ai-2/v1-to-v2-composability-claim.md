# The "1.0 had no composability" claim — an overstatement

## The claim

Cole on 1.0: *"it really is just a hodgepodge of all the instructions and tools that we have for it. There's no organization and there's no composability. We can't take a subset of the capabilities out of this and easily add it into another agent. We have to redefine and recreate things."*

**Verdict: CORRECT_BUT_INCOMPLETE** — the diagnosis of *organization* is fair; the diagnosis of *composability* is an overstatement.

## What 1.0 actually had

Pydantic AI 1.0's own docs describe `Toolset`, explicitly designed for reuse:

> *"A toolset represents a collection of tools that can be registered with an agent in one go. They can be reused by different agents, swapped out at runtime or during testing, and composed in order to dynamically filter which tools are available, modify tool definitions, or change tool execution behavior."*
> — `pydantic.dev/docs/ai/tools-toolsets/toolsets/` (1.0-era documentation)

So toolset-level reuse across multiple `Agent` instances already existed before 2.0. What v2.0 actually changes, per the v2.0.0b1 changelog, is that four **previously-scattered constructor kwargs** — `instrument=`, `prepare_tools=`, `history_processors=`, `mcp_servers=` — get removed from `Agent()` and unified into the same capability primitive that already held instructions/tools/settings. The launch article's own framing supports this reading: *"The real leverage is in the layer around it... v2 consolidates this surrounding layer into a single primitive."*

## Why this distinction matters

Cole conflates two different problems: **scattered organization** (real — hooks, instrumentation, and history-processing lived in separate kwargs instead of one bundle) with **lack of composability** (overstated — toolsets were already reusable and swappable). The genuinely new thing in 2.0 is that *everything*, not just tools, now composes through one primitive — that's a real and worthwhile improvement, just not quite the "zero composability before" story the video tells.

## Cross-link

[[langchain-crewai-comparison]] — the adjacent competitive-framing claim, which has a similar shape: real underlying differences, oversold as unambiguous "leadership."
