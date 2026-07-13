# GitHub Copilot CLI and `/delegate`

## The claim (as made)

GitHub Copilot CLI is a real terminal product usable as a coding-agent entry point (parallel to Claude Code CLI). It has a `/delegate` command that "sends this session to GitHub" — creates a background coding-agent job and a draft PR, running in a sandbox, while the developer keeps working elsewhere.

## Verified — clean confirmation

- **GitHub Copilot CLI is real and GA.** Public preview began 2025-09-25; GA announced 2026-02-25 (`github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/`). Under active development — latest release (v1.0.70) dated 2026-07-10, one day before this talk.
- **`/delegate` is a real, documented slash command**, exactly as demoed (`docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca`): *"Running the `/delegate TASK-DESCRIPTION` slash command from GitHub Copilot CLI will commit any unstaged changes to a new branch. After that, Copilot coding agent will open a draft pull request, make changes in the background, and then request a review from you."*
- **The mechanic is precisely "hand off to the cloud so it survives a laptop shutdown."** Copilot CLI's own docs distinguish two autonomy modes: **autopilot mode** (runs locally, in your terminal session) and **`/delegate`** (runs remotely on GitHub's infrastructure — "continue running even if you shut down your local machine"). Both invoke the same underlying "Copilot coding agent" capability; the difference is purely *where* it executes.
- **Copilot CLI supports a genuinely large slash-command surface** beyond `/delegate`: `/every` and `/after` (scheduling), `/agent` (select a custom agent), `/usage` (token/cost tracking), `/diff` and `/review` (inspect changes), `/mcp add` (configure MCP servers), `/sandbox`, `/context`, `/compact`, and more. This is a mature CLI, not a thin wrapper.

## Verdict

**CONFIRMED**, no corrections needed — one of the cleanest claims in the whole talk (see [[claims-scorecard]], C1).

## The Claude-side parallel

Claude Code CLI has its own local-autonomy modes but does not currently have a single named command that maps 1:1 onto `/delegate`'s specific "hand off to a persistent cloud job that survives a local shutdown, and comes back as a draft PR" behavior. The closest analogues — Routines with GitHub triggers, and Claude Tag — are event-triggered or Slack-scoped rather than an ad-hoc CLI command. See [[claude-code-parity-and-gaps]] for the full comparison.

## See also
[[_index]] · [[coding-agent-issue-to-pr]] · [[claude-code-parity-and-gaps]] · [[claims-scorecard]]
