# Custom agents (Copilot) vs. subagents (Claude Code)

## The claim (as made)

Custom agents are "when we feel like the skill isn't enough... you have a persona... an agent can use n number of skills... it's able to use MCP servers... it's more of an orchestrator... has a front matter, it has instructions." Location: `.github/agents/`, filename must end `.agent`. Frontmatter shown in the demo: name/description (like a skill) plus **argument hints** and a **`tools`** field ("the agent can read, it can search the web, it can create to-do lists, and much more").

## Verified: location, hierarchy, and most of the frontmatter

- **Location confirmed**, with more nuance than the talk gives: repo-level agents live at `.github/agents/<name>.agent.md`; org-level at `agents/<name>.agent.md` in a `.github`/`.github-private` repo; enterprise-level the same pattern one level up. Filenames are restricted to letters/digits/`.`/`-`/`_`.
- **The skill-vs-agent hierarchy is GitHub's own official framing, not just Chris's mental model.** Per GitHub's docs: skills are "opt-in... agents receive no skills by default... sub-agents do not inherit skills from the parent." Custom agents are the orchestrators — they can delegate to sub-agents with their own system prompts and tool restrictions, and a "lead agent" pattern (e.g. `architect.agent.md`) can auto-delegate and review outputs.
- **Frontmatter fields confirmed as real and documented**: required `description`; optional `name`, `target` (`vscode` or `github-copilot`), `tools` (allowlist; defaults to all if omitted), `model`, `disable-model-invocation`, `user-invocable`, `mcp-servers` (GitHub.com only), `metadata` (GitHub.com only).
- **GA status is split by surface**: GitHub.com cloud-agent custom agents are GA for all paid Copilot plans (confirmed via the Copilot SDK GA announcement, 2026-06-02). IDE-side custom agents (JetBrains, Eclipse, Xcode) are still public preview as of mid-2026.

## One caveat, held loosely

GitHub's own reference docs (`docs.github.com/en/copilot/reference/custom-agents-configuration`) reportedly flag the `argument-hint` frontmatter field as **unsupported / regressed** as of early 2026, tied to a specific GitHub issue number found by the verification workflow. That specific issue number and date are **not independently re-confirmed by the main loop** and are held as *plausible-but-unverified* rather than fact (per this project's discard-as-garble / quarantine-unverified-specifics discipline — see [[caveats-and-corrections]]). The safe takeaway: don't rely on `argument-hint` working without testing it yourself against the current Copilot CLI version; everything else in the frontmatter table above is independently well-documented and stable.

## Side-by-side: Copilot custom agent vs. Claude Code subagent

| Aspect | GitHub Copilot custom agent | Claude Code subagent |
|---|---|---|
| File location | `.github/agents/<name>.agent.md` (repo) | `.claude/agents/<name>.md` (project) or `~/.claude/agents/<name>.md` (personal) |
| Required frontmatter | `description` | `name`, `description` |
| Tool restriction | `tools:` allowlist (optional, defaults to all) | `tools:` field |
| Model override | `model:` field | `model:` field |
| MCP access | `mcp-servers:` (GitHub.com only) | `mcpServers` field |
| Skill access | `skills:` — full skill content eagerly injected at startup | invokes `.claude/skills/` skills like the main agent |
| Orchestration | can delegate to sub-agents; "lead agent" pattern | subagents are invoked by the main agent or each other |
| Extra fields | `disable-model-invocation`, `user-invocable`, `metadata`, `target` | `permissionMode`, `maxTurns`, `hooks`, `memory`, `background`, `effort`, `isolation`, `color` — a notably richer set |

**Read:** the two constructs are architecturally the same shape (persona + tool constraint + orchestration + optional MCP), confirmed independently against both vendors' own docs — not just Chris's own mental model. Claude Code's version currently exposes more configuration surface (hooks, memory, background execution, isolation) than Copilot's documented fields.

## See also
[[_index]] · [[agent-skills-shared-standard]] · [[claude-code-parity-and-gaps]] · [[claims-scorecard]]
