# The trajectory — the feature the bundle underrates

> Every source names this the #1 or #2 feature. It is also the only feature in the bundle that is **immediately portable as a design idea** without installing anything.

## What it is

An append-only, searchable record of everything the model saw and did in a session — exposed as a first-class tab in the UI, not a debug flag.

Better Stack: *"an append only log that records everything the model sees including system prompts, reasoning, and tool calls."*

What the sources report being able to inspect:

- **The full system prompt, verbatim** (Chase AI, Firecrawl, Cef)
- **The tool list actually presented to the model** (Firecrawl, Cef)
- **Context injections** — Firecrawl: *"two context values here, which is the value that gets given to the model by the harness itself"* (permissions info; available skills)
- **Reasoning / thinking steps**, per turn (Better Stack)
- **Every tool call and its result**
- **Per-turn token accounting** — Better Stack: *"this took 187 tokens. The reasoning was 94 of those tokens."*
- **Context-window breakdown by contributor** — Firecrawl: *"how much context has been used from the system prompt, the tools, and some of our messages"*
- **Session stats** — turns, average reasoning time, time-to-first-token
- **Live telemetry** — Chase AI: cache-hit %, input/output tokens, tokens-per-second. The VN source reads off his own run: **cache hit 95%, 141 tokens/sec, tool call 3.2s, input 206K tokens.**
- **Full session export to JSON** via download or an `export` slash command (Chase AI, Firecrawl)
- **Search across the whole trace**, and time-range selection (Cef, Better Stack)

## Why the sources rate it so highly

Cef: *"This, in my opinion, by itself is a very powerful feature and having access to so much information in such a convenient way is really cool."*

Firecrawl: *"this already is insanely useful when it comes to debugging agents."*

Chase AI states the comparative claim: *"this is like way more insight and way more visibility than a harness like Claude Code is going to give you. So, in the situations where you're having to do a lot of troubleshooting, like where is stuff actually going wrong? Well, this is where I can find it."*

And his overall verdict places it above the plugin system: *"that's the other big sell for this harness that I think it does better than anything else is the insights to what's actually going on under the hood."*

Firecrawl notes the design consequence in passing — the web-UI-first choice that CLI users dislike **exists because of this**: *"if you're an [opencode], a pi, or [Claude] code user like me, this may put you off, but there's a very good reason for this."* A trajectory viewer is hard to build in a terminal.

## What the bundle does not check

**No source verifies the trace is complete.** "Everything the model sees" is a strong claim; nobody diffs the trajectory against the actual wire request. Given that the harness itself injects context (permissions, skills) and that plugins can modify the agent loop, **a plugin could in principle inject context that the trajectory does not display** — and nothing in the bundle rules that out. Recorded as an open question, not a defect.

**No source connects it to cost.** The telemetry is right there (cache-hit %, per-turn tokens, tokens/sec) and no video draws a cost conclusion from it. That is the gap the vault's own observability work already fills — see [[claude-code-observability/_index]].

## The portable idea

**This is the takeaway to actually use.** The trajectory is an argument that *agent observability belongs in the primary UI, not behind a verbose flag*, and that the unit of observability is "what the model was shown" rather than "what the program logged."

The vault has been circling this: `claude-code-observability` covers the OTel/ccusage measurement layer; `prompt-evaluation` covers grading outputs. **Neither covers the "show me the exact context the model received, per turn, searchable" surface.** DSH's trajectory is the concrete existence proof that it is buildable and worth having, and it can be borrowed as a spec without running DSH at all.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/overview]] · [[deepseek-harness/hireui-relevance]] · [[claude-code-observability/_index]] · [[prompt-evaluation/_index]] · [[claude-api-cost-optimization/_index]] · [[wecommit-tokens-and-context-window/_index]]
