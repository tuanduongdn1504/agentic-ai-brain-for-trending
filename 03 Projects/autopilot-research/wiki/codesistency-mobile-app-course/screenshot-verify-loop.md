# The screenshot-verify loop (distinctive technique)

The single most portable technique in the course. It's an **agent-native visual verification loop**: the agent checks its own UI work against the target design instead of the human eyeballing every iteration.

## The loop

1. Give Claude the reference design image (upscaled screen from the GPT-image design step) via `@filename`.
2. Prompt Claude to **implement the screen**, then **take a screenshot from the running iOS simulator, compare it to the design image, and keep iterating until the two are identical.** (The exact loop prompt is linked in the video description.)
3. Claude runs the loop autonomously — it screenshots, critiques *itself* ("the button backgrounds and layout are missing"; "the text wraps to three lines, should be two"), edits, re-screenshots.
4. When close enough, stop and **hand-tune specific values in code** (e.g. he sets an image width to `58`, adjusts icon size to `22`).

## Honest expectations (the presenter's own framing)

- *"Most of the time it's not going to be 100% identical — it's AI. I'd say it's mostly around 80 or 90%."* Then you jump into code for the last mile.
- He deliberately doesn't over-polish in the tutorial: *"I don't want to waste two more hours making this auth screen look better — I'm just showing you the workflow."*

## Preconditions that make it work

- A **running simulator** the agent can screenshot (iOS on Mac; Android on Windows). He runs the app himself in a separate terminal and tells Claude via `AGENTS.md` to **never start the app** (avoids duplicate sessions).
- **Reference images** produced up front in the design step, stored in `design/`.
- Enough permission latitude (auto-edit) that the agent can iterate without a prompt per file.

## Why it's a genuine contribution

Most tutorials show "prompt → accept → move on." This closes a feedback loop the model can run itself: the design image is a **checkable success criterion** (Rule 4 goal-driven execution, in this vault's terms). It's the UI analog of "tests verify intent" — the screenshot-vs-design comparison is the test.

Related in corpus:
- [[how-we-claude-code]] — Anthropic's "agent-native verify" phase (agent checks its own work).
- [[ai-web-design-workflow]] — design-as-gate (Taste Skill 62-point anti-slop check).
- [[jasonlee-claude-mobile-app]] — design-handoff, but without the self-verify loop.

## Caveats

- Screenshot-compare is only as good as the reference. It converges UI *appearance*, not behavior or accessibility.
- It costs tokens (multiple screenshot+edit rounds per screen). Fine for a handful of screens; budget accordingly for a large app.
- Requires the agent to have a working screenshot tool wired to the simulator — not automatic in every setup.
