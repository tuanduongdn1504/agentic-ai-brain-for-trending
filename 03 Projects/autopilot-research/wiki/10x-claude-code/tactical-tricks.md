# Tactical Tricks — 10 specific configurations to adopt

Synthesized from 6 creators. Ranked by ease-of-adoption — the first 4 take <30 min total. The last 3 require infrastructure setup but pay back over months.

## Quick wins (do this today, <30 min total)

### 1. Enable a persistent status line
Surfaces the context-window % so you reset with `/clear` *before* hitting the "context rot" zone.
- **How:** `/status-line` or a custom prompt that echoes context %.
- **Sources:** Sean Kochel, Chase AI.
- **Why it matters:** without this you discover degradation only after the agent stops being useful — too late.

### 2. Create your first custom skill
Markdown SOP for one repeatable task you do often (Stripe checkout, code review template, OpenAPI spec generation).
- **How:** create `~/.claude/skills/<task-name>.md` with the SOP. Reference it by name.
- **Source:** Eric Tech (Claude Skills Explained).
- **Why it matters:** once Claude has the skill, "do an X" loads only the relevant SOP into context — saves tokens, ensures consistency.

### 3. Adopt git worktrees over branches for parallel work
Standard branches share the same working directory — multiple Claude instances clobber each other. Worktrees give each agent an isolated directory.
- **How:** `git worktree add ../proj-feature-A feature-A` then run Claude Code there.
- **Sources:** Sean Kochel, Chase AI, AI LABS.
- **Why it matters:** unlocks the parallel-agent patterns in [[../workflow-ai-coding/core-patterns|workflow-ai-coding § Infinite Parallelization]].

### 4. Use Plan Mode for any nontrivial task
Forces back-and-forth alignment before the agent starts editing.
- **How:** `/plan` at session start. Boris uses it in 80% of his sessions.
- **Sources:** Chase AI (mandatory), Boris Cherny (heavy user).
- **Caveat:** Boris predicts Plan Mode may disappear within ~1 month as models learn to enter it autonomously. Don't deeply couple your workflow to the literal `/plan` command — use the *pattern*. See [[creator-disagreements]] § 2.

## Architectural moves (do this in week 1)

### 5. Implement adversarial fact-checking agent pairs
One agent does the task; a second agent reviews the output for errors in real-time.
- **How:** spawn the second Claude in a parallel worktree with a "skeptical reviewer" system prompt. Pipe the first's output to it.
- **Sources:** AI LABS, Sean Kochel.
- **Why it matters:** catches hallucinations before they propagate into commits.

### 6. Write hooks with Exit Code 2 for path protection
Block the agent from modifying protected files (test directories, secrets, generated code, vendor folders).
- **How:** shell hook on `pre-tool-use` that returns exit code 2 (blocking error) when the agent targets a protected path.
- **Sources:** AI LABS.
- **Deep-dive:** [[../claude-code-hooks/_index|Claude Code hooks]] covers all 9 lifecycle events including this pattern.

### 7. Adopt the Karpathy LLM-wiki pattern for project knowledge
Structure raw project data as a markdown wiki with centralized indexes instead of letting Claude crawl scattered files.
- **How:** `wiki/_master-index.md` + topic folders + `[[wiki links]]`. Agent queries specific links rather than reading the whole tree.
- **Source:** Nate Herk (citing Andrej Karpathy).
- **Reported impact:** up to 95% drop in token usage vs unstructured project tree.
- **Meta-note:** this very autopilot-research wiki *is* an instance of this pattern.

## Advanced moves (do this in month 1+)

### 8. Enable experimental MCP CLI mode
Loads MCP tool schemas on demand via bash commands instead of keeping every connected tool's schema in memory permanently.
- **How:** set the experimental `MCPLI` flag.
- **Source:** AI LABS.
- **Why it matters:** prevents context bloat when you have many MCP servers connected. Each schema can be hundreds of tokens — having 20 connected tools adds up fast.

### 9. Build automated PR-watch loops
Polls a pull request every ~5 min, fetches lint/test logs, applies fixes until the PR passes.
- **How:** custom `ship-and-watch` slash command that wraps a polling loop with auto-fix.
- **Source:** Sean Kochel.
- **Why it matters:** turns "submit and forget" into a true autonomous loop. Pairs with [[../workflow-ai-coding/core-patterns|Ralph Wiggum loop]].

### 10. Give the agent visual feedback (Chrome / Vercel Agent Browser)
Lets the agent iterate on UI until it "looks right" — multimodal verification.
- **Standard:** `-chrome` flag → Chrome extension. (Sean Kochel, Boris Cherny.)
- **Context-efficient alternative:** Vercel's Agent Browser, which uses an accessibility tree to compress DOM down to 200-400 tokens. (AI LABS argues the standard Chrome extension blows up context.)
- **Trade-off:** see [[creator-disagreements]] § 4. Pick based on your context budget.

## Anti-patterns the creators warn against

- **Using Opus for trivial chores** — Chase AI: model-switch via `/model` for simple tasks. (Counter: Sean Kochel says use Opus for everything; see [[creator-disagreements]] § 1.)
- **Letting `claude.md` grow unbounded** — Boris and Sean both advocate "nuke and start fresh" when noise creeps in. (See [[claude-md-philosophy]].)
- **Skipping Plan Mode on complex tasks** — Chase AI calls this a top mistake.
- **Running with `--dangerously-skip-permissions` in production** — Chase AI flags it as fast but unsafe; [[gaps-production]] § VPC isolation.

## Adoption order

If you adopt only 3 things this month:

1. **#1 Status line** — highest ROI per minute of setup.
2. **#3 Git worktrees** — unlocks all parallel-agent patterns.
3. **#7 Wiki pattern for project knowledge** — compounds over time, biggest token-cost reduction.

The rest are valuable but more situational.
