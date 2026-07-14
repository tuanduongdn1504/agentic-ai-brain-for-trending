# Overview — the "teach" Skill video

## Source

Tự Học Cùng AI (VN community channel), "Hướng dẫn cài Skill 'teach' và tạo lộ trình học theo năng lực" (K3UXUOJ3ac0, 2026-06-28, 18:35). Full VN auto-caption transcript read in the main loop: `../../raw/2026-07-14-teach-skill-ai-tutor.md`.

## The pitch

In an information-overloaded world, self-directed learners without research/self-study skills need "a guide, a framework" for learning something properly. Generic courses teach everyone the same content; this Skill customizes lessons to the learner's own ability level, and gets more personalized the more you use it (more collected data → better-targeted lessons).

## The 6 core concepts

1. **Mission** — a written statement of *why* you want to learn this. Written by the user (or drafted by the AI on request). Every subsequent lesson is generated to stay aligned with this goal.
2. **Lesson** — the main AI-generated teaching content. Explicitly **not generated from nothing**: it draws on the Mission, the learner's accumulated learning history, provided Resources, and Notes (e.g., "explain in English" or "in Japanese"). This is described as the core of the Skill — it's what lets learning continue seamlessly across a brand-new chat thread, since all context lives in files, not the chat history.
3. **Reference** — condensed, packaged takeaways from a lesson, for later quick review (a cheat sheet).
4. **Learning Record** — tracks exercise results and Q&A during a lesson; the AI notes difficulty level and recurring mistakes, feeding this back in as input for generating the next lesson.
5. **Resource** — the input material the AI draws from. If the user provides none, the AI falls back on its own general knowledge; if the user supplies a book/notebook/link, that becomes the trusted grounding source.
6. **Note** — a preferences file: reading style, lesson length, language, tone (e.g., "teach me like a game").

## The 3-layer philosophy

1. **Knowledge** — the base layer: information drawn from the credible sources the learner supplies.
2. **Skill** — every lesson includes an exercise; the exercise's results become input data that shapes future lessons (can recall the prior lesson, adjust difficulty, change explanation style).
3. **Wisdom** — explicitly framed as **the layer AI cannot do for you**: the Skill recommends real-world groups/communities so the learner gets genuine practical application and "the deepest experience" with the material.

## The demo

1. Presenter downloads a zipped skill folder from their own Facebook group, unzips it.
2. Opens Codex CLI, navigates to the (hidden) `.codex` folder in the user's home directory, finds an existing `skill` subfolder, and copies the unzipped folder in. (See [[codex-skills-feature-verified]] for what's actually confirmed about this mechanism and path.)
3. Creates a new local project folder ("Học về tư duy hệ thống" — Learning systems thinking), opens it as a Codex project.
4. Invokes the skill with `$` + a plain-language request: `$teach giúp tôi học về tư duy hệ thống` ("...help me learn systems thinking"). Confirmed as a real Codex CLI invocation mechanism — see [[codex-skills-feature-verified]].
5. States they're using a free (not Pro/paid) ChatGPT account, with usage limits — see [[codex-free-tier-fact-check]] for the fact-check against current pricing.
6. Codex checks the project folder, finds no `mission` file yet, and prompts the presenter to state one. Presenter enters a short mission ("apply systems thinking to manage my team better...").
7. Lesson 1 is generated, sourced from **Donella Meadows** ("Thinking in Systems" + the "Leverage Points" concept) — see [[donella-meadows-source]] for the fact-check (captions garbled both the name and the concept).
8. Codex generates `mission`, `note`, and `resource` files visible in the project's file panel; Lesson 1 ("See team problems as feedback loops") includes core content, an exercise (~7 min), and a follow-up Reference cheat-sheet (causal-loop diagram, 4 components, 2 loop types).
9. Presenter demonstrates asking follow-up questions mid-lesson, ending the lesson explicitly ("kết thúc bài học 1"), then opening a **brand-new chat** and continuing to Lesson 2 — the system re-checks current progress from the saved files and picks up without losing context.

## Why the file-persistence mechanic matters

The "all state lives in files in the project folder, not the chat session" design is the same **files-as-memory** pattern already documented in this vault's [[../agent-memory-architecture/_index]] and [[../claude-code-memory-systems/_index]] topics — a low-tech, no-vector-DB approach to giving an agent continuity across sessions. Here it's applied to a tutoring use case rather than a coding-agent use case, but the mechanism (structured markdown files the agent re-reads at the start of each session) is identical in kind.

## See also

[[_index]] · [[codex-skills-feature-verified]] · [[matt-pocock-provenance]] · [[claims-scorecard]]
