# Skills: procedures vs abilities, and the context-leak problem

## Source

Matt's skills philosophy from [nQwJVHCtDDY](https://www.youtube.com/watch?v=nQwJVHCtDDY), verified against the primary source **[mattpocock/skills](https://github.com/mattpocock/skills)** (Shell, MIT, **150,757★**, pushed 2026-06-29) and the contrasting **[obra/superpowers](https://github.com/obra/superpowers)** (MIT, **241,675★**). See also [[../claude-skills/_index]] and [[../claude-code-skills-stack/_index]].

## Two kinds of skills

Matt's spoken distinction in the podcast:

- **Procedures** — skills *you* invoke yourself, to make the model behave a certain way. You're the driver: you type `/grill-me`, then `/to-prd`, then turn the PRD into issues. "I like to be the one in control. I don't want to delegate my thinking to the model."
- **Abilities** — skills the *model* reaches for on its own. Example: a "great React coding standards" ability the agent pulls in mid-task when it's about to write React, so it knows "don't use `useEffect`, use something else."

> **Terminology reconciliation (verified).** "Procedures / abilities" is **Matt's conversational vocabulary**. The **repo README codifies the same axis** as **User-invoked** vs **Model-invoked**: *"User-invoked skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. Model-invoked skills can be invoked by you **or** reached for automatically by the agent when the task fits; they hold the reusable discipline."* Same idea, two labels.

Matt's stated preference: **procedures**. He keeps the steering wheel because he knows his own skills and abilities and doesn't want to delegate the thinking.

## The context-leak problem → `disable-model-invocation`

This is the load-bearing technical insight:

- **Every model-invokable skill leaks its `description` into the context window** so the agent knows the skill exists. **100 abilities = 100 descriptions** burning context on every turn.
- You can suppress this with **`disable-model-invocation: true`** in a skill's frontmatter: the skill can then *only* be invoked by the user (typed), and its description is **not** leaked into context.
- **Verified in the repo:** `grill-me`, `to-prd`, and `teach` all set `disable-model-invocation: true`.

> ⚠️ **Correction.** In the podcast Matt cites *"my **engineering zoom-out** skill"* as his `disable-model-invocation` example. **No skill by that name exists in the public repo** (full enumeration of all 36 skill folders confirms it). Likely a misremembered/renamed/personal skill. The **mechanism he describes is real and verified** — it's just not attached to a skill called "engineering-zoom-out."

## Stateful vs stateless skills

- **Stateless** skills need no local memory of prior runs (most procedures: `grill-me`, `to-prd`).
- **Stateful** skills save state to the local filesystem so they "remember what you've done before." Matt's example is the **teach** skill — like a great teacher who remembers your prior lessons and your goal. (This is the same **file-system-as-memory** lineage as [[../claude-code-memory-systems/_index]] and the Ralph loop.)

## The teach skill (Matt's newest, and the demo in the video)

**Verified** at `skills/productivity/teach/SKILL.md` (added ~2026-05-27, moved to `productivity/` ~2026-06-08; `disable-model-invocation: true`).

- **What it does:** turns the agent into a **personalized tutor**. You state a *mission* (what you want to build / become) — not the subject — and it builds a curriculum on the fly, saving state into the workspace: **`MISSION.md`**, **learning records**, a **reference cheat-sheet**, and **lessons rendered as HTML** (richer than terminal text; reusable later).
- **Pedagogy encoded literally in the SKILL.md** (verified): the **Zone of Proximal Development**, the **Knowledge / Skills / Wisdom** trichotomy (*"Knowledge, captured from high-quality resources; Skills, acquired through interactive lessons; Wisdom, which comes from interacting with other learners"*), plus **retrieval practice, spacing, interleaving, desirable difficulty,** and fluency-vs-storage-strength. It uses **quizzes** ("unreasonably effective for storage strength") and points you to **primary sources** (e.g. the Pro Git book) at the end of a lesson.
- In the demo it teaches **git** to a "vibe coder," personalized to the local system (it checks whether git is installed, etc.). Matt says he taught himself to solve a **Rubik's cube** from memory with it.
- **Install:** `npx skills@latest add mattpocock/skills`, then choose the **teach** skill; works in **Claude Code or Codex**; invoke `/teach` inside a fresh workspace. (`/setup-matt-pocock-skills` configures issue-tracker/labels for the engineering skills.)

## grill-me — adversarial interviewer as plan-mode replacement

- **What it is:** *"A relentless interview to sharpen a plan or design."* It turns the agent into an **adversarial interviewer** that asks questions and surfaces ideas you hadn't considered until you reach a **shared understanding** — *before* any code is written. Matt uses it as a **replacement for plan mode**.
- **Verified:** exists at `skills/productivity/grill-me/`, `disable-model-invocation: true`. It is **very short** — it essentially **delegates to a `/grilling` skill** (the podcast's "literally four or five sentences" is roughly right in spirit; the file itself is ~3 lines). A companion **`grill-with-docs`** builds a project domain model. (This vault's **Brain-setup v2** was cross-ported from `/grill-with-docs`.)
- David's own version of this: *"don't say 'one-shot this app' — describe the vision, then say 'list the 10 most consequential decisions and interview me until you understand 98% of it.'"*

## The superpowers contrast (obra / Jesse Vincent)

Matt name-checks **superpowers** as "**probably the most popular skills repo out there**" — and the data backs him up: **obra/superpowers has 241,675★, ~60% more than his own 150,757★.**

- **superpowers takes the opposite *default*:** skills **trigger automatically** ("the agent checks for relevant skills before any task") — i.e., **model-in-control by default.** Matt prefers **user-in-control**.
- **Verified nuance (not truly "opposite"):** *both* systems support model-invocation. The difference is **defaults and granularity** — superpowers mandates auto-triggering; mattpocock/skills makes you opt in (`/setup-matt-pocock-skills`) and lets you disable it per-skill. More "different defaults, overlapping philosophy" than polar opposites.
- superpowers ships ~13+ skills (brainstorming, writing-plans, subagent-driven-development, TDD, requesting-code-review, using-git-worktrees, systematic-debugging…) across 11 agent platforms. Matt's closing advice: if, after a blank-slate reset, you *miss* something like superpowers' **brainstorming**, bring it back deliberately.

## Key Takeaways

- **Procedures (user-invoked) > abilities (model-invoked)** for Matt — keep the human driving. Repo terms: **User-invoked vs Model-invoked**.
- **Model-invokable skills leak their description into context;** `disable-model-invocation: true` stops the leak and locks a skill to manual use (verified on grill-me / to-prd / teach).
- **teach** is a *stateful* tutor skill encoding real learning science (ZPD, retrieval practice, spacing) and rendering HTML lessons — install via `npx skills@latest add mattpocock/skills`.
- **grill-me** = adversarial-interview plan-mode replacement; reach a shared understanding *before* coding.
- **superpowers (obra)** is the popular model-in-control counterpoint — genuinely *more* starred than Matt's repo; same tooling layer, opposite default.
