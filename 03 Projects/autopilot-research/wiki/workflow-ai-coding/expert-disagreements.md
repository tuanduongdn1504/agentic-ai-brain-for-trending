# Expert Disagreements

The speakers agree on the broad shape of the AI-coding workflow ([[core-patterns]]) but diverge sharply on specifics. Six axes of disagreement worth tracking.

## 1. Code value: "free" vs "expensive"

The deepest philosophical split.

- **Ryan Lopopolo (OpenAI):** "code is free" — AI can produce, refactor, delete code infinitely and patiently. Implementation isn't scarce. Code is a disposable build artifact, like compiler output.
- **Matt Pocock:** explicitly rejects this. **"Code is not cheap."** Bad code is more expensive than ever because it creates "software entropy" and lowers the ceiling of what an agent can accomplish in that codebase.

**Operational consequence:** Lopopolo's team will tolerate refactor-spam from agents (cheap to redo). Pocock's team will resist it (compounding entropy). Pick a side based on your codebase's longevity.

## 2. Specs-to-code vs active architecture

How much does the human touch the code editor?

- **Lopopolo (OpenAI):** advocates "harness" approach — humans steer at prompt level, agents execute the full job. Reportedly **banned his team from touching code editors** to force everything through models.
- **Pocock:** warns against the **"specs to code" movement**. Calls it **"vibe coding by another name"** — leads to garbage because developers lose handle on the code, which is their "battleground".

**Reconciliation:** maybe industry-vs-individual. OpenAI has institutional safety nets (reviewer agents, CI/CD); a solo dev doesn't and needs to stay close to the code.

## 3. Plan Mode vs Grill Me

How to achieve alignment before coding.

- **Boris (Anthropic) / default Claude Code workflow:** rely on **Plan Mode** for back-and-forth alignment.
- **Pocock:** dislikes Plan Mode — "extremely eager to create an asset rather than reaching deep understanding". Prefers his **Grill Me** skill that forces the AI to act as adversary and interview the developer until shared understanding is reached.

**Operational consequence:** Plan Mode is faster but converges on a plan even when the developer hasn't fully thought it through. Grill Me is slower but surfaces hidden assumptions.

## 4. Read or don't read AI outputs

Surprising contradiction even among high-automation advocates.

- **Lopopolo:** if you approve an AI-generated plan without reading it, you'll encode "instructions that you don't necessarily want followed" — wasted tokens and time downstream.
- **Pocock:** admits he **does NOT tend to read the resulting PRD** once shared understanding is reached via grilling. Reading the PRD only tests the AI's summarization ability, which is excellent already.

**Reconciliation:** depends on whether the alignment phase produced the document or the document produced the alignment. If you grilled-then-PRD, the PRD is a transcript and re-reading is wasteful. If the AI generated the plan first, you must read it.

## 5. Compacting vs clearing context

How to handle the "dumb zone" of long conversations.

- **Pocock:** **"Devs love compacting for some reason but I hate it."** Compacted history adds "sediment" that strains AI attention. Prefers the **"Guy from Memento"** strategy — clear context entirely, return to fresh system prompt.
- **Lopopolo:** points to **autocompaction** (specifically in newer models like GPT 5.4) as a fantastic feature that lets agents manage their own context efficiently over time.

**Operational consequence:** if your model has good autocompaction, trust it. If you're running older models or notice degradation, clear-and-restart beats compact.

## 6. Specialized vs universal agents

The Anthropic Skills team take.

- **Barry Zhang & Mahesh Murag (Anthropic):** "Don't build agents, build skills instead." Argue against domain-specific agents (Tax Agent, Legal Agent, etc.) and propose a universal general-purpose agent (Claude Code) that pulls skills (folders of markdown + scripts) only at runtime.

This isn't technically a disagreement with anyone in the bundle — none of the other speakers advocate for per-domain agents. But it's a contrarian-against-industry take: many vendors are still selling "X Agent for Y industry."

**Operational consequence:** for an individual operator, this is liberating — you don't need a custom agent for every workflow, just a growing library of skills. See [[../claude-code-hooks/_index|Claude Code hooks]] for the deterministic-event layer that complements this skills approach.

## How to use this list

When you read advice from any single AI-engineering thought leader, locate it on these 6 axes. The "best practice" they're advocating is shaped by their position on each axis. Disagreements are usually rooted in environment differences (institution vs solo, codebase age, model version), not absolute right/wrong.
