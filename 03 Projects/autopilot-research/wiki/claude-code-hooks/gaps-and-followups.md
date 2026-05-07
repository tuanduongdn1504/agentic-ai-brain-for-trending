# Claude Code Hooks — Gaps & Follow-ups

> **Topic:** [[_index|claude-code-hooks]]
> **Source:** `../../raw/2026-05-07-claude-code-hooks.md` § Gaps

What the 5-video bundle did NOT cover. These are open questions for the next research cycle.

---

## Technical implementation gaps

### Non-bash languages

The bundle exclusively shows **bash scripts** (`.sh`) for command hooks [Source 4, Source 8 in raw, Source 12 in raw]. **Open question:** can hooks natively execute Python or Node.js scripts without a bash wrapper? What about `nu` / `fish` / non-default shells?

**Follow-up search:** "Claude Code hooks Python script", "Claude Code hooks node executable"

### Windows compatibility

All practical demos target macOS/Unix [Source 3, Source 11 in raw]. **Open question:** how do hooks function on Windows? `.bat` files? PowerShell? Different `settings.json` configuration?

**Follow-up search:** "Claude Code hooks Windows PowerShell", "Claude Code Windows hooks setup"

### Debugging hooks

**No source explained how to debug a failing hook.** Are there logs? How do you troubleshoot a hook that's silently failing to trigger?

**Follow-up search:** "Claude Code hook debug log", "Claude Code hooks not firing"

### Variable passing

Sources mention hooks fire on `write` / `edit` events [Source 2, Source 29 in raw], but **none explained how to pass metadata from the event into the script**. How does a `post-tool use` hook know *which* file was just edited so it can lint only that file?

**Follow-up search:** Claude Code hook environment variables (e.g. `$CLAUDE_FILE_PATH`), official reference docs

---

## Scaling and efficiency gaps

### Prompt-hook overhead

[Source 3] notes prompt hooks add latency, but **no source quantifies the token cost or the specific instruction-budget impact** vs equivalent inline rule.

**Follow-up search:** "Claude Code prompt hook tokens", measured benchmarks

### Race conditions on parallel hooks

[Source 4] mentions matching hooks run **in parallel**, but **the bundle doesn't address race conditions**: what happens if two parallel hooks try to modify the same file or hold a lock?

**Follow-up search:** "Claude Code hooks parallel race condition", "Claude Code hook locking"

### Performance limits

**No guidance on the maximum number of hooks** a project can support before performance degrades.

**Follow-up search:** stress-test write-ups, real-world large hook configs

---

## Tooling uncertainties

### "Hookify" plugin

[Source 1] mentions a tool called **Hookify** for analysing conversations to auto-create hooks — but the speaker admits "**it's actually a little unclear**... whether it's actually messing with `settings.json` or not. I haven't tried it yet" [Source 7 in raw].

**Follow-up search:** "Hookify Claude Code", explicit project page

### Plugin hook integration

Managing hooks within Claude Code plugins is described as "**difficult and tough to remember**" [Source 8 in raw]. **The bundle has no walkthrough on the structure or management of `hooks.json` for plugins.**

**Follow-up search:** "Claude Code plugin hooks.json", official plugin docs

---

## Behavioural / lifecycle gaps

### Pre-compact event

`pre-compact` is listed among the 9 events [Source 3, Source 33 in raw], but **no source provides a use case or example**. What's a real-world reason to hook into context compaction?

**Follow-up search:** "Claude Code pre-compact hook example", "Claude Code context compaction"

### Hook exit-code behaviour

What happens when a hook exits with non-zero? Does it stop the entire agentic loop or just emit a warning? [Source 38, Source 39 in raw — uncertain in bundle]

**Follow-up search:** official hook reference docs for exit-code handling

---

## Recommended follow-up topics for the next autopilot loop

Topics ranked by promised information density (high → low):

1. **Claude Code hooks Windows compatibility** — clear gap, focused topic
2. **Claude Code hook reference docs / environment variables** — core technical doc dive
3. **Claude Code plugin development with hooks** — emerging area, plugins are growing
4. **Hook performance / token cost benchmarks** — engineering measurement, useful for scaling
5. **Hookify and other hook-config-generators** — emerging tooling category

Add these to `raw/topics-queue.md` for the next `/loop` or cron run.

---

## Key Takeaways

- The bundle is **strong on what hooks are and basic use cases**, weak on **debugging, Windows, performance limits, and hook exit-code semantics**
- The `pre-compact` event is effectively undocumented in this bundle — surprising given how often context compaction matters
- Several plugin-related questions surfaced — this is a growing area worth a dedicated future bundle
- 5 follow-up topics queued for next autopilot run (see list above)
