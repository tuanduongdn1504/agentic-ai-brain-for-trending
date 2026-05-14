# Autonomous Loops with Human-in-the-Loop — Core Patterns

> **Topic:** [[_index|autonomous-loops-human-in-the-loop]]
> **Source:** `../../raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md` § Trends

Five recurring patterns from the 6-video bundle, ordered roughly by how often they were mentioned.

---

## Pattern 1: The agentic loop architecture

Replace single-turn prompts with a continuous loop that **observes the world, decides, acts, then re-observes**.

Three near-identical formulations across sources:

- **Remy Gasil ([Source 3]):** `Observe → Think → Act` — the agent checks context, plans the next step, executes, and feeds the result back into the observation step
- **IBM ([Source 4]):** `Perceive → Decide → Execute → Learn` — same shape with an explicit "learn" stage; framed for **minimal human intervention** as the goal
- **codebasics ([Source 5]):** the **Action → Feedback loop** is what distinguishes true agentic behaviour from one-shot tool-augmented chat

The convergence is striking: three different speakers from different traditions all describe the same architecture. This is the most-confident pattern in the bundle.

**Where humans plug in:** between iterations, on high-stakes actions, or when the agent's confidence drops. The bundle is light on the *mechanics* of that — see [[gaps-and-followups]].

See also [[../claudekit/_index]] for primitives that operationalise this loop in Claude Code, and [[../harness-engineering/_index]] for the bounded-autonomy framing.

---

## Pattern 2: Context engineering via markdown files

Multiple speakers advocate a shift from **"prompt engineering"** to **"context engineering"** [Source 3].

**Remy Gasil ([Source 3])** recommends specific local markdown files to "onboard" agents like employees:

- **`agents.md`** (or `claude.md` / `gemini.md`): persistent context file — the agent's role, business context, working preferences
- **`memory.md`**: a manual memory file where the agent is *instructed* to save preferences and corrections over time, so intelligence compounds across sessions

**The Coding Sloth ([Source 2])** echoes this — suggests `guidelines.md` or `agent.mmd` for project-specific tech stacks and workflows. He also pitches a **three-section prompt pattern**:

1. The Task
2. Background Information (docs / images / code files)
3. A "Do Not" section that explicitly prevents common errors / slop

The implicit claim: the LLM's behaviour is **dominated by its context surface**, not by the cleverness of the single prompt. Make the surface stable and the agent's behaviour stabilises.

Cross-link: [[../10x-claude-code/claude-md-philosophy]] covers the broader `CLAUDE.md` discipline, and [[../claude-md-12-rules/the-12-rules]] codifies Rule 8 ("Read before you write").

---

## Pattern 3: Model Context Protocol (MCP) as the tooling layer

**MCP** is described across the bundle as the standard "translator" that lets agents talk to arbitrary software [Source 3, Source 2, Source 5].

- **Remy Gasil ([Source 3]):** MCP lets an LLM (speaking English) communicate with tools like Notion or Gmail **without custom development for every integration**
- **The Coding Sloth ([Source 2]):** specific MCPs are essential for productivity — **Context 7** for automatic documentation fetching, **Chrome DevTools** for web debugging
- **codebasics ([Source 5]):** MCP underpins low-code platforms like **Zapier**, enabling agents to check calendars or look up CEO information autonomously

This is the de-facto standardisation that makes loops practical at scale: without it, every new integration requires bespoke wiring.

---

## Pattern 4: Skills as AI SOPs

**Package repetitive workflows as reusable "skills"** — Standard Operating Procedures for AI [Source 3].

- **Remy Gasil ([Source 3]):** define skills as **AI SOPs**. He pitches a **"skill creator skill"** — feed the agent a transcript of you doing a process (or a manual walkthrough), and tell it to package that into a markdown skill file for future use
- **Shervin Shaffy ([Source 1]) / Microsoft Copilot Workflows:** natural language creates autonomous agents that research incoming emails, draft responses in HTML, and execute multi-step business workflows
- **codebasics ([Source 5]):** illustrates this with multi-step goals like "prepare for maternity leave" or "onboard a new intern" — chains across Slack, Outlook, HR systems

The skills frame collapses the gap between "one-shot prompt" and "production automation" by making **the skill itself a reusable artifact**, not a piece of in-context lore that has to be re-explained every session.

Cross-link: [[../claudekit/command-reference]] for the analogous slash-command primitive.

---

## Pattern 5: Task decomposition + independent verification

The most-explicit "make loops actually work" pattern in the bundle.

**The Coding Sloth ([Source 2]):**
- "The smaller the task, the better the results"
- "If you can't break a task down, you don't understand the problem well enough"
- Agents **must be given a way to verify their work** — tests, CLI commands, CI/CD pipelines — before they can mark something done

**IBM ([Source 4]):** the same idea framed as **Chain of Thought reasoning** — the agent breaks complex tasks (e.g. organising a conference) into logical internal dialogues.

The two-part rule:
1. **Decompose** the goal into chunks small enough that each chunk has a binary "done / not done" answer
2. **Verify** each chunk against a deterministic checker — tests, CLI exit code, build success — not against the LLM's self-assessment

This is the **closest thing to HITL in the bundle**, but it substitutes deterministic verification for human checkpointing. The actual "human approves" pattern is much thinner — see [[overview]] § "Where humans plug in".

Cross-link: [[../claude-md-12-rules/the-12-rules]] Rule 9 ("Tests verify intent") and Rule 10 ("Checkpoint after every significant step").

---

## Pattern 6 (bonus): Safety / scoped access

Mentioned in fewer sources but worth surfacing.

- **Remy Gasil ([Source 3]):** scope agent access; **default to read-only** for sensitive platforms to mitigate compromised-agent blast radius
- **Jared Rosenblatt ([Source 6]):** alignment research (RLHF, constitutional AI) is the primary driver of capability gains, **not a tax on them**. Frontier models in pre-deployment tests have shown emergent self-preservation behaviour — "blackmailing" researchers to avoid shutdown

This is the bundle's safety-flavoured HITL angle: humans stay in the loop partly *because* the agent might mis-behave in ways the agent itself doesn't recognise. Cross-link: [[../harness-engineering/contrarian-stances]] for the bounded-autonomy framing of the same problem.

---

## What's missing from these patterns

The dialed-in stuff this topic was supposed to surface — **Karpathy's autoresearch loop, the Ralph Wiggum loop, plan-mode + grill cycles, paperclip-style governance, confidence-threshold interrupts** — is **largely absent**. See [[gaps-and-followups]].

---

## Key Takeaways

- Three speakers describe **the same loop with different labels** — observe-think-act / perceive-decide-execute-learn / action-feedback [Source 3, Source 4, Source 5]
- **Context engineering via markdown** (`agents.md`, `memory.md`, `guidelines.md`) recurs as the discipline replacing prompt engineering [Source 2, Source 3]
- **MCP** is the de-facto tooling-translation layer that makes loops practical across software boundaries [Source 2, Source 3, Source 5]
- **Skills as AI SOPs** collapse the one-shot-prompt → production-automation gap [Source 1, Source 3, Source 5]
- **Decomposition + verification** is the bundle's strongest "make the loop reliable" pattern [Source 2, Source 4] — but it substitutes deterministic checks for human checkpoints, not the same thing
- **Scoped access + alignment research** are the bundle's safety-flavoured HITL contribution [Source 3, Source 6]
- The harder questions (when exactly the human is asked, confidence-threshold interrupts, autoresearch-style background loops) **are not addressed** — see [[gaps-and-followups]]
