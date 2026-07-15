# The Skill Checklist — the 4-part framework

The core content of the talk. Four axes to write or audit any Agent Skill. In the published [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) skill these are the four **axes** of the `GLOSSARY.md`: **Invocation · Information Hierarchy · Steering · Pruning** (verified — the published skill maps 1:1 to the talk).

---

## 1. Trigger (Invocation) — 3:16

How the skill is invoked. **Every skill can always be invoked manually by the user** (`/skill-name`, or however the harness names it). The design decision is whether the *model* can also fire it:

- **Model-invoked** — the skill's `description` is loaded into the agent's context, so the agent can autonomously decide to invoke it (and other skills can reach it).
- **User-invoked** — set `disable-model-invocation: true`; the description is stripped from the agent's reach, so only the user can invoke it.

The trade-off (the heart of the talk):

| | Model-invoked | User-invoked |
|---|---|---|
| Firing | Agent *or* user | User only |
| Cost 1 | **Context load** — description sits in the window *every turn* (100 skills = 100 descriptions) | **Zero context load** |
| Cost 2 | **Unpredictability** — the model may *not* fire it even when perfect → you must **eval** your skills to check triggering | none of that class |
| Cost 3 | — | **Cognitive load** — *you* are the index that must remember it exists |

- **Neither is strictly better.** Model-invoked looks more flexible but pays in tokens + nondeterministic firing; user-invoked is deterministic + free but offloads the remembering onto the pilot.
- Pocock's own preference: **user-invoked, "full control"** — smaller agent context, no triggering evals, at the cost of his own cognitive load.
- Depth + the `mattpocock/skills` (user-invoked) vs `obra/superpowers` (model-invoked) comparison, and the two-layer nuance: [[pocock-writing-great-skills/trigger-invocation-and-superpowers]]. The exact field vs Anthropic's docs: [[pocock-writing-great-skills/disable-model-invocation-mechanism]].

---

## 2. Structure — 7:29

- A skill is built from **two units**: **steps** (the ordered procedure) and **reference** (supporting info). A skill can be all steps, all reference, or both. Thinking in these two units is the decomposition lever.
  - Example — `2PRD` (now `to-spec`): 3 steps (find relevant context → confirm test seams with the user, a human-in-the-loop checkpoint → write the PRD) + 2 references (what-is-a-test-seam, a PRD template).
- **Tip 3: make `SKILL.md` as small as possible.** Every skill = `description` + `SKILL.md` + branching reference. Small `SKILL.md` is easier to maintain, easier to audit, fewer words to think about, and **every word shaved is tokens shaved** off every use.
- **Branches → context pointers → external reference.** If reference material is only used on *one branch* of the skill, move it out of `SKILL.md` into a separate markdown file, reached by a **context pointer** ("if you need X, go to this file"). Pocock calls the pointed-to file an **external reference**.
  - `2PRD`/`to-spec` has **one branch** → all reference belongs in `SKILL.md`.
  - `domain-modeling` has **two-or-three branches** (update the `CONTEXT.md` glossary; create an ADR; or neither) → the ADR template + glossary template live *outside* `SKILL.md` (real files `ADR-FORMAT.md` + `CONTEXT-FORMAT.md`), pulled in only when that branch fires.

---

## 3. Steering — 11:54

The "main thing" of the talk — how to get the agent to actually do what the skill says. Two levers:

- **Leading words** — words that pack dense meaning into a small space. Put the leading word in the skill; the agent **repeats it back in its reasoning traces and output**, and because the word encodes the behaviour you want, that changes what it does.
  - Example: instead of "don't code layer-by-layer," use the leading word **"vertical slice"** — established dev terminology that triggers the model's priors. You can *verify it worked* by watching the reasoning traces say "we'll do this as a thin vertical slice."
  - English is "a pretty wide API"; look for stronger/more-consistent leading words, and agents are good at helping you find them.
- **Legwork per step** — agents under-invest effort on a step when they can *see the future goal*, so they rush to it. Fix: **split the process into separate skills so the agent sees one step at a time**, hiding the future step.
  - The canonical case: **plan mode**'s "ask clarifying questions → make a plan" always rushes the questions because the goal (a plan) is visible. Pocock's fix: a separate **`grill-with-docs`** skill (the interview) that runs *before* the planning skill (`2PRD`/`to-spec`) — the agent only sees the interview step, so it does the full legwork.
- Full detail + the Leitwort literary root: [[pocock-writing-great-skills/steering-leading-words-and-legwork]].

---

## 4. Pruning — 16:48

Keep the skill lean. Massive skills are a *symptom* of one of these failure modes:

- **Duplication** — every part of the skill should have a **single source of truth**; don't repeat reference material (the PRD template, "what is a test seam") across steps or files.
- **Sediment** — stale, irrelevant lines that accrete when many people edit a shared markdown and nobody feels brave enough to delete others' additions. Fix by looking at **structure** (move to the right branch, or kill it if stale). *(The published skill refines this: sediment is cured by pruning; **sprawl** — a too-long skill where every line is live — is cured by structure. The talk blends the two. See [[pocock-writing-great-skills/talk-vs-published-skill]].)*
- **No-ops** — lines that *look* like they do something but don't change the agent's behaviour (e.g. "write a long detailed commit message" — the agent would anyway). Common **when an agent writes your skill**. Find them with a **deletion test**: delete the line; if behaviour is unchanged, it was a no-op.
- "People ask how I get my skills so small — it's these techniques: deletion tests, compacting into leading words, no irrelevant material, no sediment."

---

## The full sweep (19:06)

> Trigger: is it firing at the right times? context-load or cognitive-load? · Structure: branches; steps + reference; branch-only material out of `SKILL.md` · Steering: condense into leading words + watch the traces; break down for legwork by hiding future phases · Pruning: a final pass for sediment, crud, and especially no-ops.

Get started by downloading the [`writing-great-skills`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) skill and running it over your own — or over community-authored — skills to check they're any good.
