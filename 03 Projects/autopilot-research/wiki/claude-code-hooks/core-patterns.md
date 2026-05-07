# Claude Code Hooks — Core Patterns

> **Topic:** [[_index|claude-code-hooks]]
> **Source:** `../../raw/2026-05-07-claude-code-hooks.md` § Trends

---

## Pattern 1: Deterministic automation

Hooks are **deterministic** — they run automatically and consistently based on specific events without the "probabilistic" nature of an LLM [Source 2, Source 3, Source 5]. This is the headline differentiator vs putting rules in `CLAUDE.md`, where the model decides whether to follow the rule on each turn.

For any rule you want enforced **every time without fail**, hooks are the answer.

---

## Pattern 2: Preserving "instruction budget"

Multiple sources emphasise that moving instructions out of `CLAUDE.md` and into hooks **saves the LLM's instruction budget** [Source 4, Source 5].

The argument:
- Every line in `CLAUDE.md` consumes context window
- Trivial workflow constraints ("use pnpm not npm", "format with Prettier", "don't commit `.env`") don't need LLM reasoning
- By enforcing those deterministically through hooks, you free the model to focus on the complex reasoning that actually requires judgement

Matt Pocock takes this furthest, advocating to **"almost always" delete `CLAUDE.md` and replace its rules with hooks** [Source 4]. See `[[expert-disagreements]]` for the counter-position.

---

## Pattern 3: Common use cases

The 5 sources cluster around four high-frequency use cases:

### Notifications

Desktop alert, system sound (chime, meow, custom), or push notification when:
- Claude finishes a long task (`stop` event)
- Claude needs permission to proceed (`permission request` event)

Cited by [Source 1, Source 2, Source 3, Source 5] as the single most popular hook. Lets you multitask while Claude works.

### CLI / tool enforcement

Force Claude to use specific tools:
- `pnpm` instead of `npm` [Source 4]
- A custom internal CLI that Claude wouldn't know about
- Project-specific build / test runners

Pre-tool-use hook intercepts the command, rewrites or blocks it, returns success or failure to Claude.

### Destructive command blocking

Same `pre-tool use` event, used defensively:
- Block `git push --force` to protected branches
- Block `rm -rf` outside project root
- Block deletion of `.env` files
- Block direct database mutations [Source 4]

### Code quality automation

`post-tool use` event, fires after Claude edits a file:
- Run linter (ESLint, Ruff, etc.)
- Run formatter (Prettier, gofmt, black)
- Run focused tests on the touched file
- Type-check with `tsc --noEmit`

[Source 2, Source 3] both demonstrate ESLint + Prettier on save.

---

## Pattern 4: Let Claude write the hook for you

Across [Source 1, Source 4, Source 5], the most-mentioned approach for **creating** hooks is to **not edit `settings.json` by hand**. Instead:

1. **Provide the documentation URL** — feed Claude the official hooks docs URL, ask it to read and produce a config [Source 1]
2. **Convert existing rules** — point Claude at your current `CLAUDE.md` and ask it to extract deterministic-enforceable rules into hook scripts + `settings.json` entries [Source 4]
3. **Use Claude for hook logic refinement** — when the hook needs nontrivial logic (e.g. "MECE directory check — block creating overlapping folders"), let Claude reason through the bash, then commit the result [Source 2]

This pattern uses the LLM as a *compiler* from natural language → deterministic bash, then captures the output so the runtime path is hook-only (no LLM in the inner loop).

---

## Pattern 5: Filtering and routing

Broad triggers like `pre-tool use` fire on **every tool call**. Without filtering, your hook runs hundreds of times per session.

The sources recommend a **routing pattern** [Source 2]:

```
pre-tool use hook → script that checks:
  ├─ Is this a `bash` command?
  │  ├─ Yes → check command pattern (regex match `git push|rm -rf`?)
  │  │  ├─ Match → block / log / alert
  │  │  └─ No match → allow silently
  │  └─ No → allow silently
```

The script returns 0 (allow) or non-zero (block) plus stdout for Claude to see.

[Source 2] notes this filtering layer becomes essential as hook count grows — without it, hooks add measurable latency and "muddy" the agent's perception of what's allowed.

---

## Key Takeaways

- **Determinism is the value prop** — anything you want to enforce 100% of the time goes here, not in `CLAUDE.md` [Source 4, Source 5]
- **Top 4 use cases:** notifications, CLI enforcement, destructive-command blocking, code quality automation [Source 1-5]
- **Don't write hooks by hand** — let Claude convert your existing rules into hook configs [Source 1, Source 4, Source 5]
- **Filter aggressively** — broad events like `pre-tool use` need a routing/matcher layer or they bloat every interaction [Source 2]
