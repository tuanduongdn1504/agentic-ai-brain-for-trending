# Contextual engineering — persistent `.md` "brain" files

How Cowork users keep Claude's memory consistent across scheduled sessions. Three distinct patterns emerge, plus an outlier automated approach.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-1 + §Outliers-5

## The shared problem

- Cowork sessions are stateless — each scheduled task runs without recall of prior runs (beyond what's in the conversation buffer)
- Speakers solve this by **persistent Markdown files** read at task start as context
- Anthropic ships **Global Instructions** as the official surface; speakers wrap their `.md` files via these

## Pattern A — Minimalist (Jack Roberts)

- Single `business brain.md` file as primary context repository
- Contains: business goals, target audience, mission, voice
- Pro: easy to author, one file to maintain
- Con: monolithic — risks "forgetfulness" as it grows (per Bart's critique)

## Pattern B — Specialist trio (Bart Slodyczka)

- Three separate files:
  - `about me.md` — personal priorities, who-am-I
  - `brand voice.md` — communication style, tone constraints
  - `working preferences.md` — procedural standards, how-I-work
- Pro: scopes context per concern; Claude can be told "for this task, load brand voice + working preferences only"
- Con: more authoring overhead; risk of inconsistency across files

## Pattern C — Stefan Wirth's strategic injection

- Local folders containing **strategy documents** and **roadmaps**
- Claude is given **read access** to these folders, not just static files
- Tasks reference the folders so Claude evaluates transcripts / outputs **against project visions**
- Adds his custom **"Context OS" MCP** to apply "lenses" (Stoic / Lean Startup / etc.) on top
- Pro: dynamic — strategy doc updates flow through automatically
- Con: requires careful folder discipline (see [[sandboxing-and-workspace-structure]])

## Pattern D — Kenny Liao's automated brain dump (the outlier)

- **Doesn't manually maintain** the context files at all
- Instead: nightly **scheduled task** parses a free-form notes file and **organizes** it into target context files (`identity`, `preferences`, `relationships`)
- The context system is itself a Cowork automation
- Pro: zero manual upkeep once the parser is built
- Con: trust the parser; debugging miscategorizations is harder than direct edits
- This is the **only** truly recursive use case in the corpus — a Cowork task that maintains its own future-task context

## Comparison table

| Pattern | Files | Maintenance | Cognitive overhead | Resilient to drift? |
|---|---|---|---|---|
| A — Minimalist | 1 | High (one big file) | Low | Poor (file grows unboundedly) |
| B — Specialist | 3 | Medium | Medium | Good (concerns separated) |
| C — Strategic injection | folders | Low (docs update naturally) | High (folder discipline) | Excellent |
| D — Automated brain-dump | many | None (Cowork rewrites) | Medium (debug parser) | Excellent (if parser is good) |

## Key Takeaways

- All Cowork power users converge on **persistent context files**, not in-session prompting
- The unsolved trade-off: **fewer files = more drift** vs. **more files = more authoring overhead**
- **Kenny Liao's brain-dump pattern is corpus-unique** — Cowork-task maintaining Cowork-task context; worth special attention as a self-bootstrapping pattern
- **Anthropic's Global Instructions** is the official surface but is barely mentioned in the corpus — speakers prefer file-based context they control
- This pattern is **identical to Storm Bear vault's CLAUDE.md librarian rules** (vault-level + per-project), validating the Anthropic blog "Skills explained" composition

## Related

- [[overview]] — Cowork product positioning
- [[skills-to-plugins-pipeline]] — context files often get codified into reusable skills
- [[../claude-md-12-rules/_index]] — same pattern at the Claude-Code/CLAUDE.md layer
- [[external|Storm Bear: CLAUDE.md librarian discipline]] — vault-level instance
