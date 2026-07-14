# Sponsor fact-check: Nimbalyst (not "Nimble list")

## Name correction

The video's auto-generated captions mis-hear the sponsor's name throughout as **"Nimble list."** The real product is **Nimbalyst** ([nimbalyst.com](https://nimbalyst.com)), confirmed from the video description's actual sponsor link (`nimbalyst.com/?utm_source=youtube&utm_medium=sponsorship&utm_campaign=cole-medin-202607`). This is the same caption-garble failure mode flagged elsewhere in this corpus (e.g. School.com≠Skool in [[../google-ai-studio-github-import/_index]]) — always resolve a sponsor/product name against the description links, never the auto-captions alone.

## What checks out

- **Free + open source, MIT license, no signup for solo use** — confirmed. Desktop app (macOS/Windows/Linux) + mobile companion; GitHub repo public under MIT.
- **Plain markdown on disk** — confirmed. Nimbalyst's own docs: *"All content and metadata lives in plain markdown and standard files on your local filesystem"* — no proprietary format, plays well with Git.
- **Red/green diff viewer, agent manager (parallel Claude Code/Codex/OpenCode/GitHub Copilot sessions with worktree isolation), Kanban board, and a traversable dependency graph linking trackers→plans→diagrams→sessions→diffs→files** — all confirmed present as described.

## Where "100% local, no lock-in" oversells

**Verdict: CORRECT_BUT_INCOMPLETE**, and the same shape as this corpus's recurring "free tier" pattern (compare [[../google-ai-studio-github-import/pricing-privacy-data]] and [[../local-ai-coding-agents/_index]]'s "free" theater finding).

The "100% local, nothing to sign up for" framing is true for solo, individual use — but Nimbalyst's own marketing prominently features **real-time multiplayer editing and shared Kanban boards**, which run through a cloud sync server at `wss://sync.nimbalyst.com` (Cloudflare Workers + Durable Objects), plus a waitlisted "Nimbalyst for Teams" tier. The video's framing implies a purely local tool with zero cloud dependency anywhere in the product; that's only true if you never touch the collaboration features the product is built around.

## Takeaway

Not a false claim, not deceptive marketing on Nimbalyst's part (the cloud sync architecture is documented, not hidden) — just the familiar sponsor-read pattern where "100% local" quietly means "100% local for the free tier you'll actually use in the demo," and the team/collaboration tier this project is clearly built to sell runs through the cloud.
