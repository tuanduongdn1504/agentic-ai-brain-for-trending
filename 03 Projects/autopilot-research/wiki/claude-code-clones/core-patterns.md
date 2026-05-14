# Claude Code Clones — Core Patterns

> **Topic:** [[_index|claude-code-clones]]
> **Source:** `../../raw/2026-05-13-open-source-claude-design-clones-alternative-agent.md` § Trends

Recurring techniques across the named clones, and across the broader "Claude design" pattern. These are the primitives clones either replicate, diverge on, or skip.

---

## Pattern 1: Terminal-first agent over IDE-extension

The headline design-choice that defines this whole class.

- Move the agent **one layer up in the stack** — out of the IDE editor and into the terminal as the primary interface [Source 3]
- The repo root becomes the unit of context; the agent has filesystem + bash + git as its native tools rather than only the editor buffer
- Caleb explicitly identifies this as the "complete change in workflow" that differentiates Claude Code (and its clones / antecedents like Aider) from IDE forks like Cursor or Windsurf [Source 3]

**Clones that replicate:** OpenClaw, OpenCode, Aider (each in some form).
**Clones that diverge:** none in this bundle — the bundle is selection-biased toward terminal clones.

---

## Pattern 2: Dynamic prompt sandwich

The architectural revelation from Fireship's analysis of the leaked Claude Code source [Source 2].

- Claude Code is **not "alien super intelligence"** — it's a complex orchestration of hard-coded instruction strings glued together with TypeScript at runtime [Source 2]
- Hard-coded strings tell the model to "be a good boy", follow safety guardrails, adopt a persona, and respect tool constraints [Source 2]
- The prompt is composed dynamically per turn from these fragments — hence "sandwich"

**Why this matters for clones:** once the technique is public, replicating it is straightforward engineering work. The leak demystified the architecture. Forks like OpenClaw started here [Source 2].

**Falsifier:** Fireship dismisses this as "prompt spaghetti" [Source 2]; Caleb takes a more reverent view [Source 3] — see [[expert-disagreements]].

---

## Pattern 3: The bash tool as load-bearing primitive

The single most-cited specific technical discovery from the leak [Source 2].

- A ~1,000-line file dedicated to letting the LLM **reliably parse and execute terminal commands** [Source 2]
- This is the primitive that lets a Claude-style agent actually do work in a repo — read files, run tests, commit, deploy
- Clones that replicate the bash tool reliably "work"; clones that approximate it loosely fail in subtle ways (the bundle implies this without measuring it)

**Implication for clones:** the bash tool is where engineering effort concentrates. The prompt sandwich is the orchestration; the bash tool is the actuator.

---

## Pattern 4: Tribal-knowledge text files (claude.md / skills.md / code.md)

A pattern Claude Code popularised that every named clone seems to adopt.

- A markdown file at repo root encodes project-specific rules the agent should always respect [Source 3, Source 5]
- Caleb frames this as **"pulling tribal knowledge out of developers' minds and into a well-defined document"** [Source 3]
- Hasan adds `code.md` as a place for prompt-level rules so you don't repeat instructions per session [Source 5]

**Why clones replicate this:** it's a cheap, high-leverage convention. No special tooling required — just a convention the agent reads on session start. Cost-of-replication is near zero.

---

## Pattern 5: Hive Mind / shared memory across agents

Higher-end pattern from Mark Kashef's setup [Source 1].

- A unified memory state — typically a local SQLite database — that **every specialised agent reads and writes** [Source 1]
- Lets a "council of agents" (triage + ops + research + communications) track each other's completed work [Source 1]
- Mark layers this with semantic memory (vector-based) and episodic memory (older conversations "decay" over time) [Source 1]
- Gemini 1.5 Flash is used as a cheap "washing machine" to categorise long chat histories into facts/preferences [Source 1]

**Relevance to clones:** clones that target the multi-agent / agentic-system space (rather than single-turn coding) need this memory layer. The bundle doesn't say which clones ship it natively — it's mostly built bespoke on top.

---

## Pattern 6: Agent SDK as bridge (the anti-clone)

The pattern Mark Kashef advocates as a **replacement** for clones [Source 1, Source 4].

- Use the official **Anthropic Agent SDK** to run Claude Code's brain from any interface — Telegram, Slack, Discord [Source 1]
- Keeps the user on a legitimate Anthropic subscription (no "barely legal" subscription smuggling) [Source 1]
- Mark explicitly cites Boris Cherny (creator of Claude Code) as having confirmed this is "fair game" for personal local tools [Source 1]
- Replaces both OpenClaw and Hermes in Mark's stack [Source 1]

**Why this matters as a "pattern":** it's the **anti-clone** — the legitimate path that makes clones less necessary. Any analysis of clones has to weigh whether Agent SDK bridging solves the same problem with less risk.

---

## Pattern 7: Subscription-cost optimisation

The pragmatic motivation behind much of the clone interest [Source 3, Source 5].

- Many users prefer Claude Code (or a clone) because it can leverage their **existing Anthropic subscription** rather than paying per-API-call [Source 3]
- Hasan demonstrates routing Claude Code to **OpenRouter** and using free models like Minimax M2.5 for simpler tasks [Source 5]
- Anthropic has **banned third-party apps** from tapping subsidised subscription pricing [Source 3] — which limits which clones can legally use this trick
- The Agent SDK path keeps you legitimate; the OpenClaw / Hermes path is "gray area" [Source 1, Source 3]

**Implication:** cost is the prime mover for clone adoption. If Anthropic ever subsidises programmatic use the way they subsidise the Pro UI, much of the clone landscape evaporates.

---

## Pattern 8: Council of agents / triage architecture

Higher-end architectural pattern [Source 1].

- A primary **triage agent** delegates incoming work to specialised sub-agents (ops, research, communications, code) [Source 1]
- Specialised agents share the Hive Mind memory layer (Pattern 5) so each knows the others' state [Source 1]
- The user interacts with the triage agent; specialisation is invisible from the outside

**Relevance to clones:** this is mostly an **application-layer pattern built on top of** Claude Code or a clone — it's not in the agent CLI itself. But clones that expose enough hooks for sub-agent orchestration enable this; clones that don't, foreclose it.

---

## Where clones diverge from Claude Code

The bundle is thin here, but the implicit divergences:

- **OpenClaw** is leak-derived — inherits the prompt sandwich and bash tool [Source 2]. Long-term divergence depends on whether Anthropic keeps shipping updates that OpenClaw can't track
- **OpenCode** is a parallel independent implementation [Source 2, Source 3] — likely differs at the prompt-orchestration level rather than the bash-primitive level
- **Aider** predates Claude Code and was the originator of much of this pattern [Source 3]. Diverges in that it doesn't replicate Claude Code; Claude Code is downstream of Aider's terminal-first thesis
- **Hermes** — bundle says almost nothing concrete about its architecture beyond "great vibe coder for prototypes" [Source 6]

---

## Key Takeaways

- **Terminal-first** is the defining design choice — clones differentiate from Cursor/Windsurf IDE forks here [Source 3]
- **The bash tool is load-bearing** — a ~1,000-line primitive identified in the leak as the technical core [Source 2]
- **Dynamic prompt sandwich** is the orchestration architecture, demystified by the leak; "prompt spaghetti" [Source 2]
- **Tribal-knowledge files** (`claude.md` / `skills.md` / `code.md`) are cheap, high-leverage; nearly universal [Source 3, Source 5]
- **Agent SDK bridging is the anti-clone** — the legitimate alternative that two of the bundle's videos endorse [Source 1, Source 4]
- **Subscription cost is the prime mover** for clone interest; Anthropic's crackdown narrows the value [Source 1, Source 3]
- The bundle is **thin on clone-internal architectural divergence** — see [[gaps-and-followups]]
