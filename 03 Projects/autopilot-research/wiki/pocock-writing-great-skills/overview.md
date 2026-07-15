# Overview — Building Great Agent Skills: The Missing Manual

## Source

- Video: [`UNzCG3lw6O0`](https://www.youtube.com/watch?v=UNzCG3lw6O0) — Matt Pocock, *"Building Great Agent Skills: The Missing Manual"*, AI Engineer channel, 2026-06-29, 20:43.
- Raw transcript: `raw/2026-07-15-pocock-writing-great-skills.md`.

## What it is

- A **20-minute methodology talk**: how to write and audit **Agent Skills** (`SKILL.md` files) so they actually do what they promise.
- **Pre-recorded** for AI Engineer World's Fair 2026 (San Francisco); Pocock couldn't attend in person, so he "gave the talk I would have given in San Francisco" to camera.
- Not a product demo — a **shared rubric**. He explicitly frames the deliverable as *a checklist you can run against any skill*, and hands you the tool that runs it: the [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) skill.

## The framing: "skill hell"

- Developers keep inventing hells: **tutorial hell** (loops of half-learned tutorials) → **framework hell** (a new JS framework every 10 minutes) → now **skill hell**.
- Skill hell = thousands of freely-available skills, but **no shared rubric** to tell a good skill from a bad one, so people can't get the results the skills promise. True for individuals *and* organizations trying to turn SOPs into agent-runnable procedures.
- He names his own guilt: `mattpocock/skills` "is one of the most popular engineering skill sets out there," so he wants to help its users escape skill hell.

## The 4-part checklist (at a glance)

1. **Trigger** — how the skill is invoked. Decide **user-invoked** vs **model-invoked** (each has a real cost). → [[pocock-writing-great-skills/trigger-invocation-and-superpowers]]
2. **Structure** — the internal layout: **steps + reference**; keep `SKILL.md` minimal; hide branch-specific reference behind **context pointers**. → [[pocock-writing-great-skills/the-skill-checklist]]
3. **Steering** — getting the agent to actually do it: **leading words** + **legwork per step**. → [[pocock-writing-great-skills/steering-leading-words-and-legwork]]
4. **Pruning** — make it as small as possible: kill **duplication**, **sediment**, **no-ops**. → [[pocock-writing-great-skills/the-skill-checklist]]

Full framework detail: [[pocock-writing-great-skills/the-skill-checklist]].

## The honesty read

- **The highest-integrity content-rich talk in the corpus so far.** Scorecard: **13 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE / 0 FABRICATED** ([[pocock-writing-great-skills/claims-scorecard]]).
- Why so clean: it's a **domain authority describing his own repo + a documented mechanism**. Every claim about how skills work was verifiable against **Anthropic's own Claude Code docs** and the **live `mattpocock/skills` repo**.
- The single non-CONFIRMED item (CL5) is not an error but **evolution since recording**: the skill he demos as `2PRD` is now `to-spec` and has grown an issue-tracker-publish step.
- It sits at the honest end of the corpus honesty spectrum with [[github-copilot-cli-agents/_index]], [[local-ai-coding-agents/_index]] and [[codesistency-mobile-app-course/_index]] — and, being self-referential (his own tool, his own repo), is the least-hedged of them.

## Why this topic matters *here*

- This vault **runs on skills** — `05 Skills/` plus the project-local `autopilot-research/skills/` (`yt-pipeline`, `yt-search`, `notebooklm`, `autopilot-research-routine`, `bypass-403-escalation`). This talk is a **direct audit tool for the operator's own harness**, not just an external subject.
- It is the corpus' **4th Matt Pocock topic** and the first that is *about building the primitive* rather than using it: the WHY lives in [[pocock-software-fundamentals/_index]], the worldview in [[pocock-agentic-workflow/_index]], the pipeline in [[pocock-real-feature-build/_index]] — and the **skill-authoring craft** lives here.

## Next

See [[pocock-writing-great-skills/hireui-and-vault-pilot]] for the payload: running `writing-great-skills` over this vault's skills and hireui's skills.
