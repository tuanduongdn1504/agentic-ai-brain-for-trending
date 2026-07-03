# PRD and issues pipeline — from conversation to queue

## Source

- Transcript `raw/2026-07-03-pocock-real-feature-build.md` · skills verified in [mattpocock/skills](https://github.com/mattpocock/skills) (`to-prd`, `to-issues`) + in-repo variant `.claude/skills/to-prd-project/SKILL.md` in course-video-manager.

## Step 1 — write the PRD (from the grilling transcript)

- **Input is the Q&A itself.** "The conversation we've just had is incredibly good fodder… I freaking love question-and-answer because it co-locates the question with the answer" — his attention-mechanics rationale for grilling-then-PRD rather than PRD-from-scratch.
- **Modules before prose.** The skill sketches the major modules and *surfaces them for review*: ghost-course schema/DB ops · materialization-cascade service (a new method on the course-write-service) · two new API routes · ghost-course UI · materialization modal · plans-deprecation.
- **Matt reviews the module list, not the document.** Two interventions:
  - Interface judgment: new `materializeCourseAndLesson` method vs a parameter on the existing `materializeGhost` — "I'm thinking about the interface more than the implementation… I think it should have a new method."
  - Scope cut: module 6 (plans deprecation) — "I do want to deprecate plans at some point, but not as part of this PRD."
- **Tests are decided at PRD time.** The skill asks *which modules do you want tests for* — answer: where harnesses already exist (course-write-service e2e). This produces "testing decisions" in the PRD → "more likely to follow TDD and create feedback loops as it's going."
- **The PRD is filed as a GitHub issue** (the parent). "Am I going to review this PRD? No… LLMs are really, really good at summarizing things. I'm going to accept it on faith." Structure: user stories + implementation decisions + testing decisions.
- In-repo variant `to-prd-project` adds orchestration hygiene: the PRD issue must **NOT** get the implement label (prevents Ralph picking up the parent as a work item).

## Step 2 — PRD → issues (slicing the queue)

- Because the PRD is already in context, slicing happens immediately, cheaply.
- Issues carry: link to parent PRD · what to build · acceptance criteria · **blocked-by relationships** · which parent user stories they address. "If the PRD is the destination, these are the journey."
- **Right-sizing is the human's judgment call:**
  - Too small = "we pay the cost of kicking up an entire agent" per trivial task (e.g. "hide publish/export UI on ghost courses").
  - Too big = loses coherence.
  - Live decision: "merge two and three together" → 4 slices (ghost-course creation / UI / direct delete / materialization cascade — the cascade "needs to live on its own").
- **Issues are NOT reviewed either:** "Absolutely not. I've already pre-reviewed them" (via the grilling + module pass).

## Why GitHub issues as the queue

- "This is what I do with all of my issues… because when we go to implement with an AFK agent, the agent pulls down all the GitHub issues, chooses one, and works on it." — the queue IS the interface between day shift and night shift ([[sandcastle-ralph-afk-loop]]).
- Blocking relationships give the harness a dependency graph — the verified current harness selects issues with **zero open blockers** (dependency-based selection).
- The same queue absorbs QA feedback later ([[qa-plan-and-feedback-loop]]) — one backlog, two producers (planning + QA), one consumer (Ralph).

## Key Takeaways

- **Grill → PRD → issues is a compression pipeline:** dialogue (rich, messy) → PRD (structured summary) → issues (executable slices). Human review effort is spent at the *start* (grilling) and on *module interfaces + slicing* — never on prose.
- The **module sketch is the review surface** — you can steer architecture without reading implementations.
- Decide **tests per module at PRD time**; it propagates TDD into every downstream issue.
- Slicing granularity is a first-class skill: agent-startup cost vs task coherence.
- Cross-links: [[grill-me-in-practice]] · [[ubiquitous-language-for-llms]] (module naming) · [[../pocock-agentic-workflow/afk-queues-not-loops]] (queue doctrine) · [[../claude-md-12-rules/_index]] (Rule 9: tests verify intent).
