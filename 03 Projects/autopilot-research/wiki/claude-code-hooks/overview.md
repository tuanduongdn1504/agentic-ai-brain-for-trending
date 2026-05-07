# Claude Code Hooks — Overview

> **Topic:** [[_index|claude-code-hooks]]
> **Source:** `../../raw/2026-05-07-claude-code-hooks.md`

---

## What hooks are

Hooks are **event-driven shell commands** that run automatically inside the Claude Code lifecycle, similar in spirit to Git hooks. Each hook fires on a specific event (e.g. before a tool runs, after Claude finishes, when permission is requested) and executes a command you control [Source 1, Source 3].

They sit alongside `CLAUDE.md` (natural-language rules) and slash commands (manual triggers) as the third lever for shaping agent behaviour — but with one crucial difference: **deterministic execution**, no LLM judgement involved [Source 2, Source 5].

---

## The 9 lifecycle events

Sources consistently identify **9 trigger events** [Source 3]. The most-cited are:

- **`session start`** — fires when a CLI session opens. Common use: load business context / preferences before any prompt [Source 1, Source 2, Source 3, Source 5]
- **`session end`** — fires on session close. Common use: cleanup, log shipping
- **`pre-tool use`** — fires before any tool is invoked. Common use: block destructive commands, enforce CLI choice [Source 1, Source 2, Source 3, Source 4]
- **`post-tool use`** — fires after a tool finishes. Common use: lint/format the touched file [Source 2, Source 3]
- **`stop`** — fires when Claude finishes its turn. Common use: desktop notification chime [Source 1, Source 2, Source 3]
- **`permission request`** — fires when Claude asks user for permission. Common use: notify, log
- **`pre-compact`** — listed but **none of the 5 sources demonstrated a practical use case** [Source 3] — see `[[gaps-and-followups]]`

Two events are mentioned but not explicitly named in the bundle (`subagent stop`, `notification` are common Claude Code hook names — verify in official docs).

---

## Command hooks vs Prompt hooks

A core distinction across all 5 sources:

| | Command hook | Prompt hook |
|---|---|---|
| Execution | Pure shell script (no AI) | Evaluated by Claude (AI judgement) |
| Speed | Fast, sub-second | Adds significant latency [Source 2] |
| Use case | Notifications, formatting, CLI enforcement, hard blocks | Subjective rules ("does this match MECE structure?"), security guardrails |
| Cost | Free | Token-processing cost per fire |
| Recommendation | **Default choice** [Source 2, Source 3] | Use sparingly — see Joe Rhew's frustration in `[[expert-disagreements]]` |

---

## Where hooks live

Two locations:

1. **User level (global):** `settings.json` in the user's Claude Code config. Applies to every project [Source 1]
2. **Project level:** `settings.json` inside the project repo. Applies only to that project [Source 1]
3. **Plugin level:** when distributed as part of a Claude Code plugin, hooks are bundled in a `hooks.json` file [Source 1]

Both project-level and user-level hooks fire — they don't override each other unless you explicitly disable one.

---

## Configuration shape

Each hook is a JSON object specifying:
- The event it binds to
- A matcher (regex or pattern) for filtering when it should fire
- The command to execute

Sources don't show one canonical shape but consistently mention `settings.json` as the home and matchers as essential for keeping `pre-tool use` from firing on every tool call indiscriminately [Source 2].

> See `[[practical-takeaways]]` for the recommended way to **let Claude write the hook config for you** rather than editing `settings.json` by hand.

---

## Key Takeaways

- Hooks are **deterministic**, event-driven shell commands inside the Claude Code lifecycle [Source 1, Source 2, Source 3, Source 5]
- 9 lifecycle events; the most-used are `session start`, `pre-/post-tool use`, and `stop` [Source 3]
- Two flavours: **command hooks** (fast, deterministic) and **prompt hooks** (AI-evaluated, slow but flexible) — prefer command hooks [Source 2, Source 3]
- Live in `settings.json` at user level or project level (or `hooks.json` for plugins) [Source 1]
- `pre-compact` event exists but the bundle has no real-world example — research gap [[gaps-and-followups]]
