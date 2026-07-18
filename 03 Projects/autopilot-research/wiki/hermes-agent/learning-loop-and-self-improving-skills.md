# Hermes Agent — The Learning Loop & Self-Improving Skills

## Source
`raw/2026-07-18-hermes-agent/` (esp. t1 Phan Dong Giang, t4 Sean's AI Stories, t8 AI LABS) + official docs. Verified via `wf_06a79485-687`.

## The core differentiator (as marketed)
- Hermes' headline claim is a **built-in "learning loop"** — it doesn't just execute tasks, it *gets better at your work over time*:
  1. **Curated memory** — remembers your habits, preferences, projects across sessions.
  2. **Autonomous skill creation** — when it solves a hard/repeated task, it packages the process into a reusable **skill** so it never re-derives it.
  3. **Skill self-improvement** — skills are meant to refine with repeated use.
- The `/learn` command + agentskills.io-compatible skill files are the surface for this. Skills are searchable and shareable.
- **Four documented ways to build a skill** (t1): (1) install from the Skill Hub library; (2) ask it to do a task, then have it package that as a skill; (3) ask it to author a skill from scratch; (4) let it auto-build skills that match your recurring workflows.

## ⚠️ The maturity contradiction (surfaced, not averaged — Rule 7)
- **The most credible technical reviewer, Sean's AI Stories (balanced, non-promotional), contradicts the marketing on camera:**
  - *"I don't think it self-triggered self-learning skills yet. It only triggered learning the memory."* — i.e. the observed behavior was **memory updates**, not autonomous *skill* generation/improvement.
  - He notes Hermes **lacks LLM-ops / eval systems** (no LangSmith/Langfuse-style evaluation of whether a "self-improved" skill is actually better).
  - He wanted it to *proactively offer to save a skill* after a difficult iterative task — a **stated missing feature**.
- **Reconciliation:** the fact-check confirms Hermes *does* accumulate memory and *can* create reusable skills (X3/X4 CONFIRMED). What is **contested/unverified** is whether skills autonomously improve in *quality* (a fitness/eval loop) vs. simply being saved and recalled. Treat "self-improving skills" as **"skills that are saved and reused, with autonomous quality-evolution unproven."**

## Other unverified mechanism claims (do NOT assert as fact)
- **"Every-10-turn background fact-checking prevents hallucination"** (NetworkChuck) — not in official docs or other sources; UNVERIFIED.
- The anchor's *"work → think → check → improve" circle* framing of the loop is **MISLEADING** ([[claims-scorecard]] X5): the docs describe continuous autonomous skill creation + memory curation + user modeling, **not** a discrete 4-phase evaluation cycle. The presenter invented the procedural framing.
- A **cron-driven skill bug was shown live** (t4): a "send a joke every minute for 10 minutes" job fired only 2 of 10 times; Sean flagged the scheduler doesn't update results unless explicitly asked.

## Key Takeaways
- The learning loop is Hermes' genuine conceptual differentiator vs a plain chatbot or a static-skill agent — and it *is* real at the **memory + skill-save-and-reuse** layer.
- **Autonomous skill-quality self-improvement is the weakest-evidenced part of the pitch** — the credible reviewer saw memory-learning only, and there's no eval system to measure "improvement."
- Distinguish **memory accumulation** (common to many agents) from **autonomous skill creation** (Hermes' sharper claim). The "only agent with a learning loop" line is FALSE ([[hermes-vs-openclaw]] — OpenClaw also has memory + skills).
- See [[agent-memory-architecture|agent-memory-architecture]] for the general memory-taxonomy this maps onto (procedural = skills, semantic/episodic = memory) and [[harness-engineering|harness-engineering]] for the loop framing.
