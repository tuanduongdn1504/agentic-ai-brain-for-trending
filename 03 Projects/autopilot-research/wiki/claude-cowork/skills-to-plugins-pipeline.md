# Skills-to-plugins pipeline — codify-after-success

The recurring tactical practice: run a workflow manually, get it right, then have Claude **codify** the working flow into a reusable skill or plugin.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-4

## The pattern (corpus consensus N=3+)

1. **Operator runs a task manually** through Cowork — e.g., "organize this batch of invoices"
2. **The session succeeds** — the artifact looks right
3. **Operator asks Claude to codify** — "turn this process into a reusable skill"
4. **Claude writes a SKILL.md** capturing the working flow as a step-by-step
5. **Subsequent runs** invoke the skill rather than re-prompting from scratch

This is **rule extraction from worked examples** — a teaching loop where Cowork itself authors its future behavior.

## Speaker variations

### Bart Slodyczka — the canonical codifier

- Completes a pressing piece of work first (invoices, calendar review, etc.)
- Then tells Claude: **"turn this process into a reusable skill"**
- Treats successful sessions as **prompts for skill creation**, not just one-shot outputs

### Jack Roberts — the "handover test"

Has a sharper bar for what becomes a plugin vs. just a skill:

> **A task should become a plugin** if someone else could run the process **without asking questions**.

In other words: if the task is documentable enough that a stranger could execute it from the skill file alone, it's plugin-ready. If it still requires operator judgment, keep it as a one-off session.

This is a **handover-completeness criterion** — useful for deciding when to invest in plugin authoring vs. keeping the workflow ad hoc.

### Tech With Tim — the simplest framing

Skills are **essentially Markdown files** that provide a **step-by-step process** for Claude to follow. He uses skills like "search-for-flights" — repeatable workflow with consistent inputs.

## Skills vs Plugins

The corpus distinguishes (loosely):

| Concept | Format | Scope |
|---|---|---|
| **Skill** | Single `SKILL.md` | One workflow, one operator, fast to author |
| **Plugin** | Skill + supporting code/scripts/MCP wiring | Handover-ready, multi-step, multi-tool |

Some speakers (Tim) use "skill" for both. Anthropic-blessed terminology hasn't fully propagated.

## The composition with sandboxing + context

Skills live **inside the sandbox** ([[sandboxing-and-workspace-structure]]):

```
ClaudeWorkspace/
├── context/
├── projects/
└── skills/        ← codified workflows
    ├── organize-invoices.md
    ├── morning-brief.md
    └── ...
```

Context files (`context/*.md`) provide **WHO** Claude is; skills provide **WHAT** Claude does. Together they make scheduled tasks behave consistently across runs.

## Storm-Bear-vault analog

The same pattern operates at the vault level:

| Cowork layer | Vault analog |
|---|---|
| Operator codifies a successful workflow as `SKILL.md` | Storm Bear vault's `05 Skills/` curation cycle |
| "Handover test" before plugin promotion | LLM Wiki routine v2.2's promotion criteria from autopilot wiki → curated wiki |
| Skills sit alongside context files | Skills sit alongside `CLAUDE.md` in the vault |

This convergence — the **same codify-after-success workflow at three different scales (Cowork, vault, Storm Bear)** — is corpus-level evidence that the pattern is fundamental.

## Key Takeaways

- **Codify-after-success** is the dominant scaling pattern: don't write skills cold; write them from successful sessions
- **Jack Roberts's "handover test"** is the cleanest criterion for plugin-readiness — *can a stranger run this from the file alone?*
- **Tech With Tim's "skills are Markdown"** framing is the lowest-friction starting point — skill = a step-by-step file, nothing more
- **Skills + context files together** are what make Cowork's scheduled tasks reliable across runs
- The pattern is **scale-invariant** — same workflow operates in the autopilot wiki, Storm Bear curated vault, and vault skills

## Related

- [[overview]] — Cowork product positioning
- [[contextual-engineering]] — context files complement skills
- [[sandboxing-and-workspace-structure]] — skills live in the sandbox
- [[scheduling-and-the-app-open-constraint]] — Kenny Liao's cron plugin is itself a codified skill
- [[external|Storm Bear: 05 Skills/ curation cycle]]
- [[external|Storm Bear: agent-skills-standard (v76)]] — codifies the portable-skill format
