# Trigger: user-invoked vs model-invoked (+ the superpowers comparison)

The talk's deepest axis, and the one that produced the most valuable verification nuance.

## The two invocation modes

- **You can always invoke any skill manually** — it sits on the filesystem; you type its name. The mode only controls whether the **model** can also fire it.
- **Model-invoked** (default): the skill's **`description` is loaded into the agent's context** so the agent can autonomously invoke it, and other skills can reach it.
- **User-invoked**: `disable-model-invocation: true` → the description is **stripped from the agent's context** entirely; only the user can invoke it (and no other skill can reach it).

Verified verbatim against Anthropic's Claude Code docs — see [[pocock-writing-great-skills/disable-model-invocation-mechanism]].

## The three costs (why neither wins)

- **Model-invoked pays context load** — each description "sits in the window every turn." 100 model-invoked skills = 100 descriptions in context on **every request**. (This is *descriptions*, not bodies; the body is lazy-loaded on invocation — see the caveat in [[pocock-writing-great-skills/caveats-and-corrections]] where a verify agent got this backwards.)
- **Model-invoked pays unpredictability** — "the model may just choose not to follow it, even if it's absolutely perfect for the task." That forces you to **eval your skills** to check they fire at the right time — "really nasty, a problem I prefer to avoid." (This is exactly why this vault maintains an evals harness — [[prompt-evaluation/_index]].)
- **User-invoked pays cognitive load** — zero context cost, but "*you* are the index that must remember it exists." The more user-invoked skills, the more the pilot must hold in their head.

Pocock's stance: he prefers **user-invoked / "full control"** — keep the agent's context small, avoid triggering-evals, and accept the cognitive load on himself. "I need to understand the skills really deeply to get the most use out."

## The comparison: mattpocock/skills vs obra/superpowers

Pocock frames his repo against the other giant skill set, **[obra/superpowers](https://github.com/obra/superpowers)** (Jesse Vincent / "obra"):

- **superpowers is primarily model-invoked** — "it gives the agent superpowers." ✅ **Confirmed**: its README says *"because the skills trigger automatically, you don't need to do anything special... The agent checks for relevant skills before any task. Mandatory workflows, not suggestions."* Its skills (brainstorming, test-driven-development, systematic-debugging, writing-plans) carry model-facing "Use when…" descriptions and no `disable-model-invocation` flag. **254,795★** (created 2025-10-09, MIT) — actually *larger* than `mattpocock/skills`.
- **mattpocock/skills is primarily user-invoked** — ✅ confirmed by a definitive count (main-loop `gh api` over all `SKILL.md`): **23 of 40 skills are user-invoked** (`disable-model-invocation: true`) vs 17 model-invoked (~58% user-invoked). Matt's "I prefer full control" is true both by **majority** and in **spirit**.

## The two-layer nuance (the workflow's best catch)

A refute-first verifier initially miscounted the repo as "50/50, not primarily user-invoked" and rated the comparison MISLEADING. A main-loop recount (23/17 of 40) **overturned** that — but the verifier surfaced a genuinely illuminating structural point worth keeping:

- `mattpocock/skills` is **two-layered**, not flatly user-invoked:
  - **User-invoked orchestration / entry points** — the skills *you* run: `grill-me`, `grill-with-docs`, `to-spec`, `to-tickets`, `implement`, `improve-codebase-architecture`, `triage`, `wayfinder`, `writing-great-skills`, `ask-matt`, `setup-matt-pocock-skills`, `teach`, …
  - **Model-invoked reusable patterns** — the skills *other skills reach*: `domain-modeling`, `tdd`, `code-review`, `grilling`, `research`, `prototype`, `codebase-design`, `diagnosing-bugs`, … These carry the "…or when another skill needs to…" reach clause.
- The design is literally what `writing-great-skills` prescribes: *"Pick model-invocation only when the agent must reach the skill on its own, **or another skill must**."* Example chain: user runs **`/grill-with-docs`** (user-invoked) → it *"runs a `/grilling` session, using the `/domain-modeling` skill"* (both model-invoked reusable patterns).
- So the accurate framing: **superpowers puts the AGENT in the driver's seat (automatic mandatory workflows); mattpocock puts the USER in the driver's seat (explicit slash-command orchestration that directs when the model-invoked patterns apply).** "Primarily user-invoked" captures the control-center truth; the model-invoked half is the *reusable substrate* the user-invoked half commands.

## Why it's the operator-relevant axis

- This vault's own skills are a mix: `autopilot-research-routine` and the `/loop autopilot research` entry point are effectively **user-invoked orchestration**; a future refactor could push shared sub-procedures (yt-search, notebooklm) into **model-invoked reusable patterns** reached by the routine — exactly the two-layer design.
- See [[pocock-writing-great-skills/hireui-and-vault-pilot]] for applying the Trigger axis to `05 Skills/` and hireui's operator-only skills (I-8).
