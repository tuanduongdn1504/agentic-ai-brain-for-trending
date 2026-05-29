# Sandboxing and workspace structure

The safety primitive every Cowork user implements. Tech With Tim's "Claude can't reverse its actions" warning is the load-bearing reason.

## Source

- Raw: [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md), §Trends-2

## The pattern (corpus consensus N=3+)

- Create a **dedicated folder** — variously called "Sandbox", "Claude Workspace", "Cowork Workspace"
- Grant Cowork **read/write access ONLY to that folder**
- Cowork's permission system enforces this — Tech With Tim explicitly notes Claude **cannot touch anything outside the folders the user explicitly allows**

## Why it matters

- **Tech With Tim's warning** is the critical primitive: **"Claude's actions cannot be easily reversed"**. There is no Cowork undo. Deletes are real. File overwrites are real. The sandbox is the only protection.
- Strongly recommended: **keep duplicates of important files** before allowing Cowork to operate on them

## Bart Slodyczka's standardized internal structure

Three subfolders inside the workspace:

```
ClaudeWorkspace/
├── context/      ← persistent .md brain files (see [[contextual-engineering]])
├── projects/     ← per-project working directories
└── output/       ← Cowork-generated artifacts
```

- **`context/`** — Claude reads from here; user writes (Pattern B trio: `about me.md` / `brand voice.md` / `working preferences.md`)
- **`projects/`** — bidirectional; per-project subdirectories isolate work
- **`output/`** — Claude writes; user reads (deliverables land here)

## What this composes with

- **Skills** ([[skills-to-plugins-pipeline]]) — sandbox-aware skills reference relative paths within the workspace
- **MCP servers** ([[mcp-connectors-landscape]]) — external connectors (Google Calendar, Notion) pull data INTO the sandbox; outputs land in `output/`
- **Scheduled tasks** ([[scheduling-and-the-app-open-constraint]]) — every scheduled task implicitly operates within the sandbox; non-sandbox writes need explicit permissions

## Compared to the Storm Bear vault

The autopilot-research project follows essentially the same pattern at a different scale:

| Cowork layer | Vault analog |
|---|---|
| `ClaudeWorkspace/` | `03 Projects/autopilot-research/` |
| `context/*.md` | `CLAUDE.md` + `03 Projects/<project>/CLAUDE.md` |
| Permission to read/write only this folder | Constitutional rule #1: "READ-ONLY outside scope" |
| Tech With Tim's irreversibility warning | The librarian rules forbidding silent edits |

This convergence is evidence the sandbox pattern is fundamental to safe agent operations, not Cowork-specific.

## Key Takeaways

- **No Cowork undo** — sandbox-or-suffer
- The recommended structure is **3 subfolders** (context / projects / output) — Bart's framing is the most actionable
- Sandboxing composes naturally with skills + MCP + scheduling — but each surface needs to respect the sandbox boundary explicitly
- The pattern is **identical in spirit** to Storm Bear's vault-level constitutional discipline; same problem, same answer
- **Keep file duplicates** before allowing Cowork to mutate anything important

## Gap (per [[production-readiness-gaps]])

- Corpus doesn't cover **sandbox escape detection** — what happens if a clever prompt induces Claude to ask for permissions it shouldn't have? No telemetry / no alerting in the YouTube layer.

## Related

- [[contextual-engineering]] — context files live IN the sandbox
- [[skills-to-plugins-pipeline]] — skills are sandbox-aware
- [[production-readiness-gaps]] — what enterprise needs that the sandbox alone doesn't provide
- [[external|Storm Bear: autopilot-research/CLAUDE.md scope clamp]]
