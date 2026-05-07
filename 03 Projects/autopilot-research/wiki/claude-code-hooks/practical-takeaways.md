# Claude Code Hooks — Practical Takeaways

> **Topic:** [[_index|claude-code-hooks]]
> **Source:** `../../raw/2026-05-07-claude-code-hooks.md` § Key Takeaways

7 actionable rules distilled from the 5-video bundle. Listed roughly by order of safest-to-adopt-first.

---

## 1. Get the notification hook running first

Configure the **`stop` event** to trigger a desktop notification or audio chime so you can multi-task while Claude works [Source 1, Source 5]. Same pattern works for `permission request` events.

This is the lowest-risk, highest-frequency-of-payoff hook. It's nearly universal across the 5 sources. Adopt this even if you adopt nothing else.

---

## 2. Use `session start` to force-load context

Force-load specific business context or memory files reliably **every time** the CLI opens, rather than relying on Claude's subjective judgement of when to read a reference file [Source 5].

Example: a `session start` hook that runs `cat docs/architecture-overview.md` and pipes into the conversation. Now Claude always has that context, no `CLAUDE.md` reminder needed.

---

## 3. Prioritise command hooks over prompt hooks

Default to deterministic command hooks (pure bash). Reach for prompt hooks only when the rule genuinely needs LLM judgement, and **measure latency** before keeping them [Source 2, Source 3].

This is the lesson from Joe Rhew's frustration story (see `[[expert-disagreements]]`). If a hook is making your CLI feel sluggish, it's almost certainly a prompt hook.

---

## 4. Implement filtering / routing for broad triggers

For broad events like `pre-tool use`, route them through a script that **checks for specific command patterns** before doing real work [Source 2].

Anti-pattern: hook fires on every tool call, runs heavy logic regardless.
Pattern: hook fires on every tool call, immediately checks `is this a bash command? does it match a known dangerous pattern?` and short-circuits if not.

---

## 5. Enforce project guardrails (block destructive commands)

Use hooks to programmatically block destructive operations [Source 4]:
- `git push --force` to protected branches
- `rm -rf` outside scoped paths
- Direct `.env` deletion / overwrite
- Production database mutations

The hook returns non-zero, Claude sees the block and explains the failure. Defensive layer that doesn't depend on the model remembering the rule.

---

## 6. Auto-redirect to preferred tools

Same `pre-tool use` event, used for tool-substitution rather than blocking [Source 4]:
- Intercept `npm install`, rewrite to `pnpm install`
- Intercept `docker build`, rewrite to your project-specific build script
- Intercept default test runner, rewrite to your custom invocation

This is **less brittle than a `CLAUDE.md` rule** because the model can't forget to apply it.

---

## 7. Let Claude write the hook config for you

The single most-mentioned process tip across [Source 1, Source 4, Source 5]:

1. Open the official hooks docs URL in Claude
2. Either: paste your existing `CLAUDE.md` rules, or describe in natural language what you want enforced
3. Ask Claude to produce: the bash script(s) + the `settings.json` entries
4. Review, tweak, commit

This works because the *runtime* path is hook-only (no LLM). The LLM is just a **compiler** at config-creation time, then steps out of the loop.

---

## Adoption order I'd suggest (synthesis, not from sources)

1. Notification on `stop` (rule #1) — 5 minutes, instant payoff
2. `session start` for project-specific context (rule #2) — 15 minutes
3. Code-quality `post-tool use` (formatter + linter on save) — 30 minutes, big quality-of-life win
4. Defensive `pre-tool use` for destructive commands (rules #4 + #5) — 1 hour, do this with filtering from day 1
5. Tool-redirect rewrites (rule #6) — only after the first 4 are stable

Defer rule #7 (Matt Pocock's "delete `CLAUDE.md` entirely") until you've felt real friction with `CLAUDE.md`. It's an aggressive move that pays off only at scale.

---

## Key Takeaways

- Start with **notifications** [Source 1, Source 5] — universal payoff, no risk
- **Session-start hooks** beat trusting the model to read context files [Source 5]
- Default to **command hooks**; measure latency before adopting prompt hooks [Source 2, Source 3]
- **Filter / route** broad events to keep latency tame [Source 2]
- Use hooks defensively (block destructive commands) and offensively (rewrite to preferred tools) — both via `pre-tool use` [Source 4]
- **Let Claude generate the config**, don't hand-edit `settings.json` [Source 1, Source 4, Source 5]
