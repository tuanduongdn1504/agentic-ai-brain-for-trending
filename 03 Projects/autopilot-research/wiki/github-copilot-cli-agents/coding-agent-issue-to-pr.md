# The coding agent: issue → sandbox → draft PR

## The claim (as made)

From a GitHub issue, you can "assign to agent"; the agent works in a sandbox ("most of our agents work in sandboxes, or all of them... they can't really break out of the sandbox and do a bunch of weird stuff"), then opens a draft PR requiring human review before merge. This is presented as GA, the second of two ways to scale (alongside CLI `/delegate`).

## Verified — real, and considerably older than the talk implies

- **GitHub Copilot coding agent reached GA on 2025-09-25** (`github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/`) — nearly ten months before this talk, not a brand-new feature. This is a **correction to the verification workflow's own output**: one verifier claimed a "July 2026" GA date backed by a press-release quote that a parallel dive agent could not locate anywhere in GitHub's changelog or newsroom. An independent main-loop check found the real GA changelog entry directly and confirms the September 2025 date; the "July 2026 press release" quote is treated as **likely confabulated** and is not used anywhere in this wiki. (See [[caveats-and-corrections]] for the full account — this is exactly the kind of cross-verifier contradiction the completeness-critic pass exists to catch.)
- **Multiple real entry points**, more than the talk's single "assign to agent" framing: assigning a GitHub issue, using the agents panel available on every GitHub page, or clicking "Delegate to coding agent" in VS Code — a nice direct echo of the CLI's `/delegate` naming.
- **Sandbox model confirmed at a high level**: Copilot coding agent runs in an isolated, ephemeral environment powered by GitHub Actions. GitHub's own phrasing: cloud/local sandboxes "provide isolated execution environments that let Copilot safely interact with code, tools, filesystem, and network resources." Exact network/secrets constraints were not independently pinned down to a specific doc page in this pass — treat the sandbox as real and isolated, but don't cite exact technical limits without checking current docs.
- **Draft-PR-then-review is the literal mechanism**, not just a "human in the loop" philosophy bolted on afterward — the agent structurally cannot merge its own work; a human has to act on the PR.
- **Enterprise/Business gate confirmed at the admin level**: Copilot Business/Enterprise administrators must enable coding agent from the Policies page before members can use it. Whether the *issue-assignment UI* specifically requires GitHub Enterprise (as opposed to just a paid Copilot plan) was not cleanly pinned down — the safer statement is "gated by admin policy on paid plans," not "Enterprise-only."

## Verdict

**CONFIRMED** (feature is real, GA, mechanically matches the demo) — with the GA date corrected to 2025-09-25 and the Enterprise-gate specificity softened. See [[claims-scorecard]], C4.

## See also
[[_index]] · [[copilot-cli-and-delegate]] · [[mcp-servers-in-copilot]] · [[claude-code-parity-and-gaps]] · [[caveats-and-corrections]] · [[claims-scorecard]]
