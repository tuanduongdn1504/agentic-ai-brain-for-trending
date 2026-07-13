# MCP servers inside Copilot

## The claim (as made)

During the `/delegate` demo, the agent is shown "using MCP servers, like Playwright, GitHub's MCP" while building the finance-tracker app.

## Verified — clean confirmation, all three parts

- **GitHub Copilot has broad, official MCP support** across VS Code, JetBrains IDEs, Xcode, Copilot CLI, the cloud/coding agent, and the GitHub app — both local and remote MCP servers. Rollout traces back to April 2025 alongside Agent Mode in VS Code.
- **GitHub's own MCP server is real**: [`github/github-mcp-server`](https://github.com/github/github-mcp-server), maintained by GitHub, hundreds of commits — lets an agent read repos/files, manage issues/PRs, inspect Actions runs, and review security findings.
- **Playwright MCP is real and Microsoft-maintained**: [`microsoft/playwright-mcp`](https://github.com/microsoft/playwright-mcp) — LLM-driven browser automation via accessibility snapshots rather than screenshots. Actively released (v0.0.78 dated 2026-07-09, two days before this talk). Documented as usable with GitHub Copilot agent in VS Code, and separately with Claude Desktop, Cursor, and Cline — genuinely cross-vendor.
- **Both servers are reportedly enabled by default** in Copilot's cloud-agent / code-review repository-level configuration — i.e. the demo wasn't showing an exotic setup, it's closer to the out-of-the-box experience.

## Verdict

**CONFIRMED**, no corrections needed. See [[claims-scorecard]], C5.

## Why this matters

MCP is the one piece of this stack that is *not* vendor-specific in any sense — it's the same protocol, the same Playwright MCP server, usable from Copilot, Claude Desktop, Cursor, or Cline. This is the strongest single point of genuine, protocol-level, cross-vendor interoperability in the entire talk — stronger even than the Agent Skills convergence, since here it's literally the *same running server process* that can serve multiple different agent clients.

## See also
[[_index]] · [[coding-agent-issue-to-pr]] · [[agent-skills-shared-standard]] · [[claims-scorecard]]
