# Claude Cowork — overview

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md) (NotebookLM `f851b538-c0cb-405f-9a8b-c46837464930`)
- Anchor video: [Duy Luân Dễ Thương — Cách hẹn giờ để AI tự chạy task cho bạn](https://www.youtube.com/watch?v=zxdI5bWcnGs)

## What it is (synthesized)

- Anthropic-shipped **desktop application** built on top of Claude
- Combines four primitives: **scheduled tasks** + **skills** (Markdown files defining workflows) + **MCP servers / Connectors** (Google / Notion / Linear / Playwright / etc.) + **sub-agents** (parallel execution)
- Positioned as the **non-technical-user** layer above Claude Code (which is the CLI for developers)
- Requires **paid Claude subscription** + (in standard mode) **computer on + desktop app open** for scheduled tasks to fire

## The three-mode taxonomy (where speakers disagree)

Three speakers offer three definitions of how Chat / Code / Cowork relate:

| Speaker | Axis | Definition |
|---|---|---|
| Tech With Tim | User skill level | Cowork = beginners (non-CLI), Code = power users (CLI) |
| Bart Slodyczka | Professional role | Chat = assistant, Code = developer, Cowork = "employee" (multi-step task completer) |
| Jack Roberts | Product history | Cowork = rebrand of earlier Claude Code packaging; same engine, stripped slash commands + non-technical UI |

→ The disagreement is itself evidence: Anthropic's product positioning is still settling. None of the speakers cite an official Anthropic taxonomy.

### Taxonomy refinement from 2026-05-30 follow-up drain

**Eliot Prince** ([Claude Cowork Plugins Explained, 135K views](https://www.youtube.com/watch?v=1GZYNyuL6Lg)) adds a brain-vs-hands framing that complements the 3-mode taxonomy:

- **LLM as "brain"** — the reasoning engine; what Chat exposes
- **Skills + Plugins as "hands"** — the action surfaces; what Cowork adds on top of the brain

Under this framing, Cowork is **not** a competitor to Code — it's a **higher-level packaging** that exposes Skills + Plugins + Connectors above Code's primitives, while still using the same underlying brain. Compatible with Jack Roberts's "rebrand" framing.

The Prince framing is corpus-first and resolves some of the 3-way disagreement: Code and Cowork share the brain; they differ in what hands are pre-built.

See [[skills-vs-plugins-hierarchy]] for the two-tier hierarchy within "hands" (Skills = single-task recipes; Plugins = job-function bundles).

## Pricing posture

- **Subscription required** to use Cowork at all (no free tier mentioned in any of the 6 sources)
- **Jack Roberts** reframes the **$200/month Max plan** as a **"salary headcount"** for an AI employee, not a software cost — distinct mental-model vs. the "save credits" framing from Kenny Liao / Tech With Tim / Stefan Wirth

## Key Takeaways

- Cowork is a **scheduling-first** product: the unlock vs. plain Claude Chat is autonomy on a clock
- It is **NOT a developer tool** — that's Claude Code's job; Cowork strips the CLI/slash-command interface
- The "AI employee" framing recurs across 3+ speakers and looks like Anthropic's intended positioning
- The hardware constraint (app must be open) is the most-cited limitation across the corpus — see [[scheduling-and-the-app-open-constraint]]
- Anthropic has not standardized the Cowork-vs-Code-vs-Chat distinction in public marketing; expect this to clarify in coming months

## Related

- [[contextual-engineering]] — Cowork's primary configuration surface is `.md` context files
- [[sandboxing-and-workspace-structure]] — the safety primitive every Cowork user needs
- [[mcp-connectors-landscape]] — Cowork's "what tools" surface
- [[skills-to-plugins-pipeline]] — Cowork's reusable-automation unit
