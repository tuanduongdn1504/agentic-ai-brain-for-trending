# Claude Code: what parallels, what doesn't

A direct, first-party-sourced comparison (Anthropic docs at `code.claude.com`/`platform.claude.com`, not memory) against everything Chris Noring demoed on the Copilot side.

## What genuinely parallels

| Copilot mechanism | Claude Code equivalent | Match quality |
|---|---|---|
| Agent Skills (`/skills`, folder + `SKILL.md`) | Agent Skills (`.claude/skills/<name>/SKILL.md`) | **Same open spec** (agentskills.io) — see [[agent-skills-shared-standard]] |
| Custom agents (`.github/agents/*.agent.md`) | Subagents (`.claude/agents/*.md`) | Same architectural shape (persona + tools + MCP + orchestration); Claude's config surface is richer (hooks, memory, background, isolation) — see [[custom-agents-vs-subagents]] |
| MCP servers (GitHub MCP, Playwright MCP) | MCP servers (same protocol, same Playwright MCP server) | **Identical** — MCP is vendor-neutral by design — see [[mcp-servers-in-copilot]] |

## What does not directly parallel

- **No native AGENTS.md support.** Claude Code reads `CLAUDE.md`; AGENTS.md is a large open community request (`anthropics/claude-code` issue #6235 and duplicates) with no shipped timeline as of mid-2026. See [[agents-md-guardrail]]. Not a gap that matters for hireui specifically, since hireui already standardizes on CLAUDE.md.
- **No single CLI command that maps 1:1 onto `/delegate`.** The closest Anthropic-side mechanisms:
  - **Routines with GitHub triggers** — Anthropic-managed cloud infrastructure; a saved Claude Code configuration (prompt + repos + connectors) that runs automatically. Supports scheduled, API, and **GitHub-event** triggers ("run automatically in response to repository events such as pull requests or releases"). This is real and lives on Anthropic-managed infrastructure so it keeps working with your laptop closed — genuinely comparable to `/delegate`'s "survives shutdown" property. The difference: Routines react to repo *events* (a PR opened, a release cut), not to an ad-hoc "assign this issue to an agent right now" action.
  - **Claude Tag** (real, launched 2026-06-23; see [[../claude-tag-multiplayer-agent/_index|claude-tag-multiplayer-agent]] for the full corpus treatment) — Slack-scoped: a team `@`-mentions Claude in a channel, Claude spawns a cloud session, and returns a PR option to the thread. This is the closest thing to "assign work, get a PR back" on the Claude side, but it's routed through Slack, not a GitHub issue-assignment button.
  - **Neither is literally "click assign-to-agent on a GitHub issue."** If hireui wants that exact interaction shape on the Claude side, the honest answer as of this research is: it doesn't exist yet as a first-party, issue-driven UI affordance the way Copilot's is. Routines-on-GitHub-events is the nearest workable substitute.

## Bottom line for hireui

Nothing here is a "Claude Code is behind" story except the missing issue-assign button — and even that has a working substitute (Routines w/ GitHub triggers). The skills and custom-agent constructs are equally mature on both sides, and MCP makes tool access a non-issue. The one thing worth actually testing on hireui's own repo: whether a **Routine with a GitHub-event trigger** can replicate the "open an issue, walk away, come back to a draft PR" workflow Chris demoed — that's a genuine, testable pilot (see the pilot-menu deliverable for this topic).

## See also
[[_index]] · [[copilot-cli-and-delegate]] · [[coding-agent-issue-to-pr]] · [[agents-md-guardrail]] · [[../claude-tag-multiplayer-agent/_index|claude-tag-multiplayer-agent]] · [[claims-scorecard]]
