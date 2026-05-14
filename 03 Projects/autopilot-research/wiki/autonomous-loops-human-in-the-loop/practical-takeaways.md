# Autonomous Loops with Human-in-the-Loop — Practical Takeaways

> **Topic:** [[_index|autonomous-loops-human-in-the-loop]]
> **Source:** `../../raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md` § Takeaways

> ⚠️ **Honesty note:** the bundle is thin on **specific HITL checkpoint mechanics** (see [[_index]] signal-quality warning). The 7 rules below are the ones that actually come from the sources. Where a "rule" is a vendor-generic platitude, I'm flagging it so you can weight accordingly. For dialed-in patterns, treat [[../workflow-ai-coding/_index]] and [[../harness-engineering/_index]] as higher-signal than this topic.

7 actionable rules, ordered roughly by adopt-this-first.

---

## 1. Decompose the goal until each step has a binary done/not-done answer

The single most-cited tactical rule in the bundle.

- **The smaller the task, the better the results** [Source 2]
- **If you can't break a task down, you don't understand the problem well enough** [Source 2]
- IBM ([Source 4]) calls the same idea **Chain of Thought reasoning** — break complex tasks into logical internal dialogues

Tactically: write the goal, then keep asking "what's the first verifiable chunk?" until you have something a test or CLI command can decide on. **This is also the foundation of any HITL workflow** — you can't checkpoint progress you can't measure.

Cross-link: [[../claude-md-12-rules/the-12-rules]] Rule 9 (Tests verify intent) and Rule 10 (Checkpoint after every significant step).

---

## 2. Give the agent a deterministic way to verify its own work

Closely tied to rule 1 but distinct: decomposition alone doesn't help if there's no checker.

- The Coding Sloth ([Source 2]) insists agents must verify via **tests, CLI commands, or CI/CD pipelines** — not by self-assessing
- Without a deterministic check, the agent declaring "done" is just a confidence statement

For HITL contexts, this means: the **deterministic check is the first checkpoint**, the **human is the second** (only when the deterministic check is inconclusive or the action is high-stakes).

---

## 3. Put high-stakes outputs through a drafts-not-sends gate

The closest the bundle gets to an explicit HITL pattern.

- Shervin Shaffy ([Source 1]) shows Copilot Workflows preparing **HTML email drafts** for human review, not auto-sending
- Remy Gasil ([Source 3]) recommends the same pattern for ad-spend changes and other irreversible operations
- The rule: **if the action is one-way or expensive, the agent produces a proposal, not an execution**

Useful boundary: anything that touches money, identity, customers, or production data goes through this gate by default.

---

## 4. Scope agent permissions to the minimum (read-only by default)

- Remy Gasil ([Source 3]) explicitly: give agents **read-only access** to sensitive platforms by default
- Promote to write-access per-tool, per-task, only after the read-only loop is stable

This is the security-flavoured HITL: the human stays in the loop **by being the only thing that can grant write permission**. Reduces the blast radius of a compromised or hallucinating agent. See also [[../claude-code-hooks/practical-takeaways]] for how `pre-tool-use` hooks can enforce this deterministically.

---

## 5. Build a stable context surface (`agents.md` + `memory.md`)

Shift from prompt engineering to context engineering [Source 2, Source 3]:

- **`agents.md`** (or `claude.md` / `gemini.md`): the agent's persistent role, business context, working preferences
- **`memory.md`**: where the agent saves preferences and corrections across sessions
- **Three-section prompt pattern** from The Coding Sloth ([Source 2]): (1) Task, (2) Background, (3) "Do Not" list

This isn't HITL per se, but it's what makes loops **reliable enough to leave running** — without a stable context, every loop is starting from scratch. Cross-link: [[../10x-claude-code/claude-md-philosophy]].

---

## 6. Package recurring workflows as Skills (AI SOPs)

[Source 3] (Remy Gasil) describes a **"skill creator skill"** pattern:

1. Walk the agent through a process once (or feed it a transcript of you doing it)
2. Tell the agent to **package the process into a markdown skill file**
3. Reuse the skill thereafter

The point: don't re-explain the same workflow every session. Crystallise it. This is the **autonomy-enabler** for the loop — without skills, the agent has to be re-onboarded each time and HITL load goes up unnecessarily.

Cross-link: [[../claudekit/command-reference]] for slash-command primitive.

---

## 7. Treat alignment / safety effort as capability-positive, not capability-negative

Jared Rosenblatt's argument in [Source 6]:

- RLHF, constitutional AI, and similar alignment work are the **primary drivers of capability gains**, not a tax on them
- Frontier models in pre-deployment tests have shown emergent misbehaviour (self-preservation attempts, "blackmail")
- HITL checkpoints aren't friction — they're a **safety surface** that also pays capability dividends

Tactically: when someone argues "the human review step is slowing us down", **measure the cost of removing it** before doing so. The bundle has a strong "don't trust the autonomous loop blindly" thread running through it.

---

## What the bundle says but I'd weight low

Two of the bundle's "actionable rules" are vendor-generic and probably already in your bones if you've used Claude Code seriously:

- **Use MCP** ([Source 3, Source 5]) — true but unremarkable; everyone uses MCP now
- **Reinvest in RLHF** ([Source 6]) — true at the platform level but not something an individual operator implements

Mentioned here for completeness; don't pad your weekly review with them.

---

## Adoption order I'd suggest (synthesis, not direct from sources)

1. **Rule 1 (decompose) + Rule 2 (verify)** — the foundation; without these the loop is useless
2. **Rule 3 (drafts-not-sends gate)** for any high-stakes loop — your first explicit HITL surface
3. **Rule 4 (read-only scoping)** for new tools; promote to write per-task
4. **Rule 5 (context engineering)** — pays off on the second session, compounds thereafter
5. **Rule 6 (skills)** — once you find yourself repeating a workflow ≥3 times
6. **Rule 7 (treat alignment as positive-sum)** — the meta-rule for resisting "just remove the human review" pressure

---

## Key Takeaways

- **Decompose + verify** are the two non-negotiable rules — without them, no HITL design will save you [Source 2, Source 4]
- **Drafts-not-sends** is the bundle's clearest explicit HITL pattern; default for anything one-way or expensive [Source 1, Source 3]
- **Read-only by default** for new tools — promote per-task [Source 3]
- **Context engineering** (`agents.md` + `memory.md` + three-section prompts) is what makes leaving a loop running viable [Source 2, Source 3]
- **Skills as SOPs** crystallise repeated workflows so the human isn't re-onboarding every session [Source 1, Source 3]
- **Alignment is positive-sum**: don't treat human review as friction to optimise away [Source 6]
- The bundle is **light on confidence-threshold interrupts, autoresearch loops, and Ralph-loop mechanics** — see [[gaps-and-followups]]
