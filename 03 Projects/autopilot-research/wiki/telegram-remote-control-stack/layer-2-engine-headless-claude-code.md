# Layer 2 — Engine (headless Claude Code SDK + Ralph loop)

The execution layer. Where Telegram messages from [[layer-1-interface-telegram]] actually run. Three patterns: warm-session, cold-headless, and Ralph-loop autonomous.

## Headless Claude Code: the foundation

Headless mode = Claude Code without an interactive terminal UI. Triggered via:
- `claude --channels <plugin>` — listener mode for messaging integrations (warm session)
- `claude -p "<prompt>"` — one-shot prompt mode (cold session)
- Programmatic SDK invocation (per Anthropic docs, evolving)

Three speakers in the bundle approach this differently:

### Cold-headless approach (Lee, Cursor VP)
Lee's philosophy: **start a new chat for every discrete task**. He warns that once context reaches 80-90%, model quality drops significantly. So: small tasks, fresh sessions.

This works well when:
- Each Telegram message is independent (no thread continuity needed)
- You want predictable token cost per message
- Tasks are bounded (30-75 line changes per Lee's heuristic)

Implementation: Telegram bot subprocess-spawns `claude -p` per message.

### Warm-session approach (Developers Digest)
Counterpoint: keep ONE `claude --channels` process running. Each Telegram message is a new turn in the SAME conversation. Larger context, faster response, continuity across messages.

This works well when:
- Multi-step tasks span multiple messages
- You're iterating on a single problem ("now also add tests", "and now refactor X")
- Context window is large enough that you don't hit the dumb zone often

The trade-off is real: warm sessions accumulate sediment (per Pocock in [[../workflow-ai-coding/expert-disagreements|workflow-ai-coding]]). Plan for periodic clears.

### Hybrid: warm with explicit reset
The pragmatic default: warm session, but expose `/clear` as a Telegram command. Operator clears manually when context degrades. Best of both worlds.

## The Ralph loop — autonomous validation

The Ralph loop (named after the Simpsons character for his determination) is the **flagship pattern** for autonomous Claude Code from the bundle. Developers Digest gives the deepest treatment.

### Mechanism
1. Operator sends task to Telegram bot ("implement feature X with tests passing").
2. Claude implements the code.
3. Claude triggers a **Stop Hook** (deterministic shell script) that fires when Claude says "done".
4. Stop Hook runs the test suite.
5. **If tests fail:** test output is fed back into Claude's context, with instruction "fix this and continue".
6. Claude attempts fix → loop back to step 3.
7. **If tests pass:** Stop Hook reports success to Telegram; Claude exits the loop.

This loop can run for **hours** unattended. Operator gets a Telegram notification when done.

### Why "Ralph"
Ralph Wiggum, who is "determined" — the loop just won't stop until it succeeds. Not technically deep, but the name stuck.

### Stop Hooks (the deterministic spine)
Stop Hooks are part of Claude Code's hook system — see [[../claude-code-hooks/_index|Claude Code hooks]] for the 9-event lifecycle. The relevant pattern here:
- `Stop` event fires when Claude finishes a turn
- Hook script can execute arbitrary shell (run tests, lint, build)
- Hook **exit code 2** is "blocking error" — feeds output back into Claude
- Hook **exit code 0** is "OK" — Claude finishes for real

The Ralph loop is essentially "Stop Hook with exit code 2 that runs tests and feeds failures back".

### Safety: max_iterations
Developers Digest's most important warning: **autonomous loops MUST cap iterations.** Without `max_iterations`, a Ralph loop on a fundamentally broken test can:
- Burn 1000s of tokens trying the same wrong fix
- Recursively damage code
- Hit your Anthropic API rate limit

Implementation: a counter in the Stop Hook script. After N iterations, exit code 0 regardless of test result, with a message to the operator: "I gave up after N tries; please review."

### Iterative checkpointing
Long-running tasks should write a `task.md` or `to-do.md` file. Claude is instructed to:
- Check off items as it completes them
- Run validation (Playwright for UI, unit tests for logic) after EACH item
- Stop on failure rather than building on broken state

This prevents catastrophic-failure-cascade — where bug at step 1 propagates through 12 dependent changes.

## Persistent memory — `agents.md` / `claude.md`

For multi-day work, the bundle converges on:
- **Project memory:** `agents.md` or `claude.md` in the project root (tech stack, conventions, lessons-learned).
- **Session memory:** `progress.txt` updated by the Ralph loop tracking what was learned.

Boris Cherny (cited in [[../10x-claude-code/claude-md-philosophy|10x-claude-code § claude.md philosophy]]) keeps his personal `claude.md` to **2 lines**. Documentary teams keep multiple files.

For Telegram-driven workflows, the key adaptation: the bot may have access to the project memory but **the human can no longer easily eyeball it**. Add a Telegram command:
```
/show claude.md      # bot dumps the file content
/edit claude.md      # bot starts an edit session (line-by-line)
```

Without these affordances, your `claude.md` rots silently.

## Skills — runtime-loaded SOPs

Simon Scrapes' contribution from the bundle: **Claude Code Skills** are markdown SOP files loaded into context only when the agent decides to use them. Pattern:
- YAML front matter = summary (always loaded)
- Body = full instructions (loaded only when invoked)
- Reference files in same folder = loaded only when full skill is invoked

This is **progressive disclosure**. Solves the "noisy menu" problem where 1000 generic skills cannibalize each other for attention.

Simon's contrarian claim: **20-30 well-built skills outperform 1000 generic skills**. In a Telegram-driven workflow, you want skills tightly aligned to common phone-issued commands ("/deploy staging", "/run-tests", "/triage-error <id>") so the bot consistently reaches for the right SOP.

## Cold vs warm vs Ralph — when to use each

| Pattern | Latency | Token cost | Continuity | Best for |
|---|---|---|---|---|
| **Cold** (`claude -p`) | high (subprocess startup) | predictable per-msg | none | one-off independent tasks |
| **Warm** (`claude --channels`) | low | grows over time | excellent | multi-message conversations |
| **Ralph loop** | n/a (autonomous) | high (many iterations) | within-loop | self-validating tasks ("make tests pass") |

A mature setup runs ALL THREE depending on Telegram command:
- `/quick <task>` → cold
- `/work <task>` → warm session
- `/autonomous <task> <validation>` → Ralph loop

## Cross-references

- [[layer-1-interface-telegram]] — the bot pattern that triggers this layer
- [[layer-3-mcp-integration]] — how Claude reaches external tools during execution
- [[../claude-code-hooks/_index|Claude Code hooks]] — Stop Hooks and the 9 lifecycle events
- [[../workflow-ai-coding/core-patterns|workflow-ai-coding § Autonomous Loop]] — strategic frame for Ralph
- [[../workflow-ai-coding/expert-disagreements|workflow-ai-coding § compact vs clear]] — managing context in warm sessions
