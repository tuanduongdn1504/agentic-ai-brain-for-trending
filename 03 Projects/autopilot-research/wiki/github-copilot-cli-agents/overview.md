# Overview — the talk, act by act

## Setup

Chris Noring opens with a show-of-hands: who's still coding "like normal"? Almost no hands. His framing: developers haven't lost their jobs, their "center of gravity has moved" — from 100%-on-keyboard implementers to system designers who scale themselves through agents. He's explicit that this is *his own mental model*, not gospel ("you might tell me, 'Hey, Chris, you're wrong,' and that's completely fine").

He namechecks Claude directly and warmly: "we are very good friends of Claude... Anthropic, good stuff" — roughly half the room raises hands for Claude, half for Copilot. The talk is deliberately vendor-agnostic in its framing even though the demos are Copilot-specific.

## Act 1 — CLI as the new entry point

Noring proposes starting work in a CLI (GitHub Copilot CLI, or Claude Code if that's your tool) rather than opening an editor first — a genuinely "weird idea" by his own admission, since editors used to be the developer's first touchpoint. Rationale:
- The CLI is good for issue/PR triage without opening a UI ("close 15 issues without even seeing the user interface")
- Agentic tools mean you're writing prompts, not Java/JavaScript/Python, most of the day ("Build me an app. Add this new feature. Or fix this.")
- The editor becomes the **second** stop — for the ~5% of hands-on work he still does after 20 years, mostly fine adjustments

## Act 2 — three guardrails (the editor as "control board")

Without guardrails, he says, agentic work is "mayhem... chaos," and he uses the community term for the failure mode: **"AI slop"** (auto-captions mis-transcribe this as "AI slope" throughout — a straightforward ASR/caption error, not a real term; see [[caveats-and-corrections]]).

1. **AGENTS.md** — "the absolute bare minimum." A repo-root file stating intent, architecture, constraints, and dos/don'ts (e.g. "never change the architecture unless I tell you"). Demoed on a small finance-tracker repo. See [[agents-md-guardrail]].
2. **Skills** — for tasks that are repeatable and must happen "in a certain order" without improvisation. Explicitly cross-referenced to Claude: "if you're on Claude... you usually have dot Claude slash skills... folders, one folder for each skill, and then you have a skill.md." See [[agent-skills-shared-standard]].
3. **Custom agents** — for when a skill "can't orchestrate itself with others." A custom agent has a persona (e.g. "researcher," "security expert," "back-end"), a `tools:` allowlist, and can use MCP servers. Demoed as a research-only agent constrained from editing files. See [[custom-agents-vs-subagents]].

## Act 3 — scale (delegate)

Two "modalities," both invoking the same underlying agent:
- **From the CLI:** `/delegate "Create a finance app that tracks my spending..."` — commits any local changes to a branch, opens a draft PR, and the agent works in the background (using MCP servers like Playwright and GitHub's own MCP) while Noring "sips coffee."
- **From the GitHub issue UI:** write an issue, click assign-to-agent, walk away; the agent works in a sandbox and comes back with a draft PR.

Both land in the same place: **a draft PR that requires human review to merge.** This is his "human in the loop" framing — not a philosophical add-on but the literal mechanical gate of how the feature works (see [[coding-agent-issue-to-pr]]).

## Closing framing

"20 times more code... could be 20 times more slop, and we don't want that" — the guardrails exist to make delegation safe, not to replace developers. Landing line: "we want the engineering brain, so please stay in this industry."

## What's genuinely useful here vs. rhetorical color

| Load-bearing (fact-checked) | Rhetorical color (not fact-checkable) |
|---|---|
| AGENTS.md, Agent Skills, custom agents, `/delegate`, issue-assign, MCP servers | "10x/20x/100x developer" (his own aspirational framing, not a GitHub benchmark) |
| "human in the loop" = draft-PR review gate (mechanically true) | axe-vs-chainsaw metaphor (rhetorical) |
| Skills = shared open standard across vendors | "half the room uses Claude" (unverifiable anecdote, plausible) |

See [[claims-scorecard]] for the graded version of the left column.
