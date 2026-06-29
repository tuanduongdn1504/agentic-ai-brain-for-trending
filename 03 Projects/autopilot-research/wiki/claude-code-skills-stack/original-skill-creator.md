# Original Deep-Dive: Skill Creator (anthropics/skills)

## Source

- Repo: [github.com/anthropics/skills](https://github.com/anthropics/skills) → `skills/skill-creator/`.
- Verified (`gh api`, 2026-06-29): **156,362★**, 18,424 forks, language Python, created 2025-09-22, actively pushed. The official Anthropic Agent Skills repo (most skills Apache-2.0; document skills source-available).
- Anthropic blog: "Improving skill-creator: Test, measure, and refine Agent Skills" (2026-03-03 — "Skill Creator 2.0").

## What it is

The **genuinely first-party Anthropic** skill for *creating* and *iteratively improving* skills via evaluation. Eric's claim "created by Anthropic themselves" is **CONFIRMED**. (Note: this is the sibling of `mcp-builder`, which is Ben AI's #8 in the [[claude-skills/_index]] topic — both live in this same official repo.)

## How it works — the eval-driven loop

Four stages: **Create → Eval → Improve → Benchmark**.

- **Create:** scaffolds a `SKILL.md` (name, description/trigger, instructions, bundled resources) following progressive-disclosure best practices.
- **Eval:** you define test prompts + assertions; it runs the skill (and a no-skill baseline) and captures full transcripts.
- **Improve:** a **blind A/B `comparator`** agent compares versions; a `grader` scores against assertions; an `analyzer` proposes targeted fixes (including `description` optimization for better triggering).
- **Benchmark:** measures **pass rate / latency / token usage**; a browser **eval-viewer** displays results for human review.

## ⚠️ Corrections vs the draft

- The draft named four agents incl. an **"Executor"** — **PARTIAL**: the repo documents three (`grader`, `comparator`, `analyzer`); execution happens via spawned subagents but there is no agent literally named "Executor".
- Exact helper script names (`init_skill.py` / `run_eval.py`) are **UNVERIFIABLE** as cited; the repo references `scripts/aggregate_benchmark`, `scripts/grade_runs`, `run_loop.py`, `eval-viewer/generate_review.py`. Treat specific filenames as approximate.

## The meta-move (why this matters most)

Eric's headline use is **composition**: point Skill Creator at three SDD frameworks (Superpowers/GSD/G-Stack), enumerate each one's stages, and build a custom `build-feature` skill that selects the best stage from each + a ticket-classifier front door. The eval loop then *measures* whether the merged skill beats the components. This is the "build-your-own-harness, then prove it with evals" discipline.

## Operator relevance

- **autopilot vault:** formalize the still-fuzzy local skills (`yt-search`, `notebooklm`) into eval-backed SKILL.md files; benchmark the drain pipeline.
- **Storm Bear / routine v2.2:** the Create→Eval→Improve→Benchmark loop is a ready-made template for the long-pending routine-v2.2 codification (skill-authoring discipline).
- **prompt-evaluation cross-link:** the grader/comparator pattern *is* LLM-as-judge — compose with the operator's existing `evals/` harness (A1 anchor gate), don't rebuild it.

## Install safety

n/a — built-in / source-available from Anthropic. No third-party supply chain.

## Key Takeaways

- Confirmed first-party; the eval-driven improvement loop is the real value (not just scaffolding).
- 3 documented agents (grader/comparator/analyzer); "2.0" = the 2026-03-03 evals update.
- The transferable pattern is **compose-then-eval**, the cleanest on-ramp to the vault's routine-v2.2 skill-authoring goal.

## Related

[[claude-code-skills-stack/original-superpowers]] · [[claude-code-skills-stack/original-sdd-frameworks-gsd-gstack]] · [[prompt-evaluation/_index]] · [[claude-skills/_index]] · [[harness-engineering/_index]]
