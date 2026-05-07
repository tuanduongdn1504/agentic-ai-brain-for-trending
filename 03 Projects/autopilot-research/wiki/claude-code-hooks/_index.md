# Claude Code Hooks

> **Topic:** Claude Code's deterministic event-driven shell command system
> **First compiled:** 2026-05-07 (autopilot loop run 13)
> **Source bundle:** `../../raw/2026-05-07-claude-code-hooks.md` (5 YouTube videos via NotebookLM)
> **Maintained by:** Claude Code librarian per `../../CLAUDE.md`

---

## What this is

Claude Code hooks let you run **deterministic shell commands** on specific lifecycle events (session start/end, pre/post tool use, stop, permission request, etc.) — like Git hooks but inside the agent loop. They sit between manual prompting and full autonomy: you preserve the LLM's "instruction budget" by enforcing rules deterministically rather than relying on the model to remember them.

---

## Articles in this topic

| Article | What it covers |
|---|---|
| [[overview]] | What hooks are, the 9 trigger events, command-vs-prompt hook split, where they live in `settings.json` |
| [[core-patterns]] | Deterministic automation, instruction-budget preservation, common use cases (notifications, CLI enforcement, code quality) |
| [[expert-disagreements]] | Productivity vs latency conflict (Joe Rhew vs others), minimalist-vs-essential view, AI-driven-vs-pure-deterministic debate |
| [[practical-takeaways]] | 7 actionable rules for adopting hooks |
| [[gaps-and-followups]] | What current sources don't cover — Windows compat, debugging, non-bash languages, prompt-hook token cost, parallel-hook race conditions |

---

## Source citations (within this topic)

| Source # | Channel | Title | URL |
|---|---|---|---|
| 1 | AI Terminal | Hooks Deep Dive: All 9 Events & Practical Examples | https://www.youtube.com/watch?v=ENNZEqvodgY |
| 2 | Code Playbook | Claude Code Course 11 - Hooks | https://www.youtube.com/watch?v=bOewYZvpiNo |
| 3 | Joe Rhew | Claude Code Hooks: Get Notified When Tasks Finish | https://www.youtube.com/watch?v=G9OBGn0h6LE |
| 4 | Matt Pocock | How to actually force Claude Code to use the right CLI (don't use CLAUDE.md) | https://www.youtube.com/watch?v=3CSi8QAoN-s |
| 5 | Simon Scrapes | Master 80% of Claude Code. Just Learn These 15 Things. | https://www.youtube.com/watch?v=0qqV4yv-Hss |

> Source numbers above match the inline `[Source N]` citations within each article.

---

## Related topics

(none yet — this is the first topic in this autopilot wiki)

Future cross-links to consider when more topics land:
- `[[external|Storm Bear: Claude Code best practices]]` (existing curated wiki at `../../../claude-code-best-practice - Beginner Analysis/`)
- `[[external|Storm Bear: superpowers]]` (existing curated wiki for the multi-skill Claude framework)
