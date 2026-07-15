# pocock-writing-great-skills

> **Topic index.** Matt Pocock's **AI Engineer World's Fair 2026** talk *"Building Great Agent Skills: The Missing Manual"* — a **4-part checklist for writing/auditing Agent Skills** (Trigger → Structure → Steering → Pruning), encoded in a real, downloadable skill. The corpus' **4th dedicated Matt Pocock topic** and its **first how-to-*build*-skills manual** — a meta-tool for this vault's own skill layer. Verified claim-by-claim: **the cleanest content-rich talk in the corpus so far.**

**Source:** AI Engineer (`@aiDotEngineer`), *"Building Great Agent Skills: The Missing Manual"* — [`UNzCG3lw6O0`](https://www.youtube.com/watch?v=UNzCG3lw6O0), uploaded **2026-06-29** (opening day of AI Engineer World's Fair 2026), 20:43, English, ~102.8K views at ingest. **Pre-recorded/remote** — Pocock couldn't attend in person ("family matters intruded") and recorded "the talk I would have given in San Francisco."
**Raw:** `raw/2026-07-15-pocock-writing-great-skills.md` (full EN transcript, read in full in the main loop).
**Compiled:** 2026-07-15 (path 5 yt-dlp; verified via Workflow `wf_d267ed85-320` — 20 agents = 5 dives + 14 refute-first verifiers + 1 completeness critic; ~833K tokens, 245 tool calls, 0 errors, 0 empty; all Haiku 4.5 — reconciled against ~12 Opus main-loop `gh api`/WebFetch/WebSearch anchors + the full transcript, yielding **5 Rule-12 main-loop overrides**).

---

## The one-paragraph version

Pocock's thesis: we've entered **"skill hell"** — thousands of freely-available Agent Skills, no shared rubric for telling a good one from a bad one. His fix is a **skill checklist** with four axes: (1) **Trigger** — decide **user-invoked** (`disable-model-invocation: true`, zero context load, you must remember it) vs **model-invoked** (description sits in context every turn = *context load*, and the model may not fire it = *unpredictability* → you end up eval-ing your skills); (2) **Structure** — a skill is **steps + reference**; keep `SKILL.md` as small as possible and push branch-specific reference behind a **context pointer** into an **external reference** file; (3) **Steering** — use **leading words** (dense-meaning terms the agent echoes in its reasoning traces, e.g. "vertical slice"), and **increase legwork per step** by splitting a process into separate skills so the agent sees one step at a time (his `grill-with-docs` → `to-spec` split); (4) **Pruning** — single source of truth (kill **duplication**), remove **sediment** (stale accreted crud), and delete **no-ops** (lines the model already obeys) via a **deletion test**. He encoded the whole checklist into a real skill, [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md), in his **170.6K★** [`mattpocock/skills`](https://github.com/mattpocock/skills) repo — the Storm Bear vault's own **Pattern #52**. **Verification finding:** every mechanism checks out against Anthropic's own Claude Code docs and the live repo; the only correction is *evolution since recording* — the published skill has grown a richer vocabulary than the talk, and the demo's `2PRD` skill is now `to-spec`.

## Articles

- [[pocock-writing-great-skills/overview]] — what the talk is, "skill hell," the 4-part checklist at a glance, the honesty read
- [[pocock-writing-great-skills/the-skill-checklist]] — the framework in depth: Trigger / Structure / Steering / Pruning
- [[pocock-writing-great-skills/trigger-invocation-and-superpowers]] — **user-invoked vs model-invoked**, context-load vs cognitive-load vs unpredictability, and the `mattpocock/skills` (user-invoked) vs `obra/superpowers` (model-invoked) comparison — incl. the **two-layer nuance** (23/40 user-invoked; model-invoked skills are the reusable substrate)
- [[pocock-writing-great-skills/disable-model-invocation-mechanism]] — the mechanism vs **Anthropic's own docs**: `disable-model-invocation` is a **real, official Claude Code field** but a **Claude-Code extension**, *not* part of the portable [agentskills.io](https://agentskills.io) open standard
- [[pocock-writing-great-skills/steering-leading-words-and-legwork]] — **leading words** (Leitwort), the "vertical slice" example, reasoning-trace verification; **legwork** and the plan-mode/`grill-with-docs` split
- [[pocock-writing-great-skills/talk-vs-published-skill]] — the `writing-great-skills` skill has **evolved past the talk** (GLOSSARY's 4 axes, "predictability" root virtue, router skill, information hierarchy, completion criterion); `2PRD`→`to-spec`; the sediment-vs-sprawl refinement
- [[pocock-writing-great-skills/claims-scorecard]] — the 14-claim scorecard (**13 CONFIRMED / 1 CORRECT-BUT-INCOMPLETE / 0 MISLEADING / 0 FALSE / 0 FABRICATED**)
- [[pocock-writing-great-skills/caveats-and-corrections]] — caption garbles (Leitwort, "Air Engineer", "papago"), the **5 Rule-12 overrides** of the workflow's own Haiku agents, the forward-looking "AI coding crash course", superpowers-is-bigger
- [[pocock-writing-great-skills/hireui-and-vault-pilot]] — **the payload: run `writing-great-skills` over this vault's own skills + hireui's skills** — this is the corpus' first source that is a direct audit tool for the operator's own harness
- [[pocock-writing-great-skills/source-provenance]] — video, speaker, event, channel, methodology, all source URLs

## Cross-links

- [[pocock-software-fundamentals/_index]] — **sibling Pocock topic (the WHY)**; this is the HOW-to-build-the-skills that carry that theory. Both cite the same repo; software-fundamentals demoed `grill-me`/`domain-modeling`/`tdd`/`improve-codebase-architecture` on stage — this talk explains *how those skills are built*
- [[pocock-agentic-workflow/_index]] — sibling Pocock topic (the worldview: harness > model, procedures-vs-abilities, queues-not-loops); "leading words" + "legwork" are the skill-level mechanics under that worldview
- [[pocock-real-feature-build/_index]] — sibling Pocock topic (the end-to-end pipeline); `grill-with-docs`→`to-spec` is that pipeline's front half
- [[teach-skill-ai-tutor/_index]] — Pocock's `teach` skill redistributed unattributed; **same repo**, a real user-invoked skill (`disable-model-invocation: true` confirmed here)
- [[claude-skills/_index]] — the Process-Interviewer / grill-me lineage
- [[claude-code-skills-stack/_index]] — skills composition/stacking
- [[github-copilot-cli-agents/agent-skills-shared-standard]] + [[teach-skill-ai-tutor/codex-skills-feature-verified]] + [[pydantic-ai-2/progressive-disclosure-and-skills-lineage]] — **the corpus' [agentskills.io](https://agentskills.io) thread**; this topic adds the sharpest data point yet: the *open standard* is 6 fields, and `disable-model-invocation` is a Claude-Code-only extension
- [[how-we-claude-code/_index]] — Anthropic's own "interview-first" workflow; the `grill-with-docs` legwork split is the same instinct
- [[system-thinking-ai-coding/_index]] — design-before-prompt; "leading words" are the prompt-level lever
- [[prompt-evaluation/_index]] — Pocock's "model-invoked skills force you to *eval* your skills to check they fire" = the exact reason this vault has an evals harness
- **[[external|Storm Bear: Pattern Library #52 — Extreme-Viral-Velocity]]** — `mattpocock/skills` is the vault's tracked Pattern #52 (170,613★ at ingest, up from 169,558 the day before)

**hireui + vault pilot deliverable:** `output/(C) 2026-07-15-pocock-writing-great-skills-pilot-methods.md`
