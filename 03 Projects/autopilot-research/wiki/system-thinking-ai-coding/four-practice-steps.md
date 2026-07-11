# The 4 practice steps (deliberate training of the "brain muscle")

## Source

[`raw/2026-07-07-system-thinking-ai-coding.md`](../../raw/2026-07-07-system-thinking-ai-coding.md) [00:33:44]–[00:39:42]. Framed as deliberate practice — "system thinking is a *brain* muscle, not an arm muscle" — that you can train even without a real-world job/environment. See [[overview]].

## Step 1 — Design *before* you prompt

- Pen + paper (or iPad). **Draw boxes = components, arrows = data flow.** Mark where **state** lives, where **errors** can occur, where you can **decouple**.
- Rule: **"If you can't draw it on paper, you don't really understand it — and the AI will invent the parts you didn't draw."**
- Backend version: **draw/understand the ERD (entity-relationship diagram) first.** ERD → API → specification. Skip it and "it's all guesswork that will eventually collapse — fine when small, dies as it grows / gets users."
- Discipline point: once you start prompting you've *already* borrowed the AI's plan; do your own thinking *first*.

## Step 2 — Use **spec as scaffolding** (specification-driven)

- Write **WHAT and WHY before HOW.** The "how" question comes later and doesn't matter yet.
- A short spec defines: **the problem, the constraints, the trade-offs, the definition of success, and the error scenarios you must be able to test.**
- This is "the safest skeleton for working with coding agents" — it lets the agent dodge the traps you've already named.
- Corpus tie-in: this is the same idea as spec-driven development — [[jsm-six-file-context]] (feature-specs), Storm Bear's cc-sdd / OpenSpec / GSD (external), and "the plan is a checkable artifact" in [[elicit-verifiable-agent-dsl]].

## Step 3 — "Case-study when it breaks" (the chaos-delete drill)

- Pick any file/function/component and **(mentally) delete it: how badly does the system break? What breaks?** You'll learn each part's real role, position, and contribution.
- If the answer is **"I don't know," that is a cognitive hole** — you don't understand your own system.
- Governing maxim (Cao Cao / Tào Tháo): **"use but don't fully trust."** Use the AI, but stay in control; **always test** ("luôn thử").
- This is [[three-golden-questions]] Q3 turned into a *repeatable exercise*.

## Step 4 — Reverse code review (argue *back* with the AI)

- On important PRs, **don't merge fast.** Make the AI **explain each step**: *why did you write it this way? did you weigh the risk? is it extensible? what's the trade-off?*
- **Best form:** make the AI **write the docs (and tests) for the whole project** — what each component does, why this tech/design-pattern was chosen — then **you review, edit, and validate the docs**, and ask back. He calls this his "learning process" with students starting from a blank slate.
- Anchored by the [[compiler-vs-llm]] point: the LLM is an *infinitely-patient teacher you must continuously verify* (ask the same question 10 times → 10 different answers). It is not a compiler.

## The meta-rule wrapping all four

- **Slow down on purpose.** AI lets you go fast; the practice is to deliberately go slow — investigate, force explanations, and occasionally re-code something *from memory* to keep the muscle alive. "That's how I survived this game."

## Key Takeaways

- **Draw it → Spec it → Chaos-delete it → Argue it back.** Four rituals that force the *theory* (see [[naur-programming-as-theory-building]]) back into the human even when the AI wrote the code.
- Steps 1–2 are pre-generation (build the theory first); Steps 3–4 are post-generation (recover the theory from AI output).
- Every step is a low-cost habit with no new tooling — which is exactly why it's the highest-leverage thing to pilot. See the pilot methods deliverable.
- Reverse-review + "make the AI write the docs then validate them" is the sharpest transferable technique; it also cross-links to review-layer value seen in [[jsm-practical-vibe-coding]] and [[pocock-real-feature-build]].
