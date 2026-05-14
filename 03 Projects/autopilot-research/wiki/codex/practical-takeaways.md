# Codex — Practical Takeaways

> **Topic:** [[_index|codex]]
> **Source:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` § Takeaways

10 actionable rules distilled from the 6-video bundle. Listed roughly in order of safest-to-adopt-first. Adopt them whether your default builder is Codex or Claude Code — most apply to both.

---

## 1. Create a memory file at the project root (`agents.md` or `claude.md`)

Drop an **`agents.md`** (Codex) or **`claude.md`** (Claude Code) file in the project root [Source 1, Source 4, Source 5]. Treat it as an **onboarding document**: project architecture, conventions, "do this, don't do that" rules.

Teacher's Tech calls this the **"single most important thing"** to set up [Source 4]. Mosh agrees [Source 5]. This is the lowest-effort, highest-leverage configuration in the bundle.

Start with: tech stack, directory map, one-line description of each major module, "never touch these files / patterns" list.

---

## 2. Toggle into Planning Mode before every multi-step task

Use **Planning Mode (Shift+Tab in Claude Code; equivalent in Codex)** before any task that touches more than one file [Source 1, Source 3, Source 4, Source 5].

- Agent drafts a todo list / plan
- You review and edit
- Only then does the agent touch code

Mosh and Teacher's Tech both flag this as the single biggest defense against "agent goes down the wrong path" [Source 4, Source 5]. It's free, fast, and cheap to redirect at plan time vs after the agent has half-written code across five files.

---

## 3. Use Codex as adversarial reviewer for Claude's output

Adopt Jack Roberts' core insight: **Claude is a poor self-evaluator** — wire in **Codex (or GPT-5.5) as the adversarial reviewer** [Source 2, Source 6].

The pattern:
1. Claude writes the code
2. Codex receives the diff with a system prompt instructed to be **skeptical**
3. Codex flags bugs, refuses mediocre work, suggests improvements
4. You decide whether to send it back to Claude with the feedback

This is the **single strongest argument for keeping Codex installed** even if Claude Code is your daily driver [Source 6].

---

## 4. Isolate parallel agent threads with git worktrees

When running multiple Codex/Claude tasks simultaneously, use **`git worktree add`** to separate each thread into its own folder and branch [Source 1, Source 3].

Without this: agents clobber each other's changes.
With this: 10+ parallel agents run safely, you merge the good results, discard the bad.

Keith AI and Riley Brown both demo this heavily [Source 1, Source 3]. Adopt it the moment you're running more than 2 agents at once.

---

## 5. Use voice input (Whisper Flow or built-in dictation)

Three of the six speakers (Riley Brown, Keith AI, Mosh) all use voice input [Source 1, Source 3, Source 5].

- Speaking is **2-3× faster than typing** [Source 3]
- Once you're orchestrating 3+ parallel agents, typing becomes the bottleneck
- Whisper Flow is the most-cited tool; OS built-in dictation works as a fallback

This is the operational glue that makes multitasking viable.

---

## 6. Actively manage context — `/compact` and `/clear`

Don't let context windows fill up. Run **`/compact`** to summarize the conversation, or **`/clear`** to start fresh with a summary file [Source 5].

Why: a full context window causes **"context anxiety"** — the model rushes to finish before running out of room — and **costs more per request** while producing **lower-quality output** [Source 2, Source 5].

Rule of thumb: compact when you're past 50% of context. Clear when switching to an unrelated task within the same session.

---

## 7. Run automated maintenance loops on `agents.md` / `claude.md`

Keith AI's pattern: a **cron-scheduled "upskill" automation** that runs nightly or weekly [Source 1]. The skill:
- Analyzes recent agent interactions
- Detects misunderstandings between you and the agent
- **Automatically updates `agents.md`** with the resolution

Result: the memory file evolves and gets sharper without manual maintenance.

This pattern composes naturally with `/loop` and `/schedule` from `../../CLAUDE.md` — you can run it as an autopilot routine.

---

## 8. Build modular workflow / skill recipes (not one-off prompts)

Both Riley Brown and Teacher's Tech argue that **plain-English workflow files** outperform sloppy one-off prompts [Source 3, Source 4].

- Describe the repeatable process step-by-step in markdown
- Save as a skill
- Invoke by reference rather than rewriting the prompt every time

This gives the agent a clear reason-and-adapt framework rather than asking it to guess what you meant [Source 4].

This mirrors the `05 Skills/` pattern in the Storm Bear vault and the `skills/` directories in autopilot-research projects.

---

## 9. Decide your "vibe coding vs real engineering" posture explicitly

The bundle splits sharply on this (see [[expert-disagreements]] Conflict 3). Pick a posture and stick to it for a given project:

**Vibe-coding posture (Riley Brown, Keith AI):**
- Full-access permissions
- 10+ parallel agents
- Multitasker mindset, agent "cooks" while you do other work
- Best for: prototypes, side projects, exploratory work

**Real-engineering posture (Mosh, Teacher's Tech):**
- Sandbox mode, review every change
- One or two agents at most
- Carpenter mindset, you are the craftsman, AI is the power saw
- Best for: production systems, regulated environments, team codebases

Mismatched postures within a team are a faster route to friction than any technical problem [Source 3, Source 5].

---

## 10. Maintain real-engineering oversight, even in vibe mode

The single rule both camps actually agree on, just phrased differently [Source 4, Source 5]:

- Mosh: **never allow agents to one-shot entire applications without reviewing every line** and backing changes with **automated tests** [Source 5]
- Teacher's Tech: AI handles the mechanical parts, you handle the architecture [Source 4]
- Even Riley Brown's "let it cook" full-access workflow ends in **review and merge from worktree** — he just shifts when the review happens [Source 3]

The most aggressive vibe-coder in the bundle still reviews work before merging. Don't skip the merge review — that's the point at which "AI does the work" becomes "I shipped good code".

---

## Adoption order I'd suggest (synthesis, not from sources)

1. **Memory file** (rule #1) — 30 minutes, instant payoff
2. **Planning Mode** (rule #2) — zero setup, just toggle Shift+Tab
3. **Voice input** (rule #5) — 15 minutes setup, multiplies your operator speed
4. **Git worktrees** (rule #4) — first time you want a second agent running
5. **`/compact` and `/clear` discipline** (rule #6) — habit, no install
6. **Codex as adversarial reviewer** (rule #3) — install Codex, define a "review this diff" skill
7. **Skill / workflow recipes** (rule #8) — once you notice yourself repeating prompts
8. **Cron-scheduled memory-file maintenance** (rule #7) — once your `agents.md` is stable
9. **Posture decision** (rule #9) — pick a default, document it in the memory file
10. **Oversight discipline** (rule #10) — this is the meta-rule, never stop doing it

---

## Key Takeaways

- **Memory file at project root** is the single highest-leverage setup [Source 4]
- **Planning Mode every multi-step task** — free and prevents the most common failure mode [Source 4, Source 5]
- **Codex as adversarial reviewer** is the primary reason to keep Codex installed alongside Claude Code [Source 6]
- **Git worktrees are non-negotiable** the moment you run more than 2 parallel agents [Source 1, Source 3]
- **Voice input** is operational infrastructure, not a luxury [Source 1, Source 3, Source 5]
- **Context management discipline** (compact / clear) directly affects quality and cost [Source 5]
- **Pick a posture** — vibe vs real-engineering — and make it explicit to collaborators [Source 3, Source 5]
- **Always review at merge** — even the most aggressive vibe-coder in the bundle does this [Source 3, Source 5]
