# The anti-vibe workflow (the actual product of the course)

The presenter states the workflow is the thing to learn, not the app. It maps almost exactly onto structured-development patterns already in the corpus ([[system-thinking-ai-coding]] design-before-prompt, [[jsm-practical-vibe-coding]], [[pocock-real-feature-build]] plan→build→QA).

## The loop, as taught

1. **Plan first — never code first.**
   - Open Claude Code in **Plan Mode**. Paste a project-agnostic "senior technical co-founder / product architect" prompt (linked in the video description) whose job is to **interview you**, not write code: *"I want us to be in complete alignment before writing any single line of code."*
   - Answer the multi-round Q&A (auth providers, backend shape, async strategy, ORM, rate limits, model choice, platforms in scope…). The point: *"minimize the guesswork from AI."*
   - Decide your **tech stack yourself** — *"I always want to have my tech stack determined by me, not by AI."* Leave everything else for the interview.
   - **Read the whole plan before accepting.** He rejects a risky item (hosting a durable Inngest endpoint on EAS at the start) and has Claude revise it to use the Inngest dev server instead — a concrete "push back on the plan" moment.
   - Save the approved plan to an uppercase **`PLAN.md`** as a phased to-do list; do NOT let Claude implement everything at once. Mark phases complete as they land, and periodically tell Claude to reconcile `PLAN.md` against what's actually built.

2. **Design with image models (before building UI).**
   - Generate each screen + a **design system** (typography, palette, components) with GPT image generation, using project-agnostic prompts (linked). Explore with *"generate a grid of 9 variations,"* pick one.
   - "Upscale" the chosen screen, extract background images ("generate this background, no text/logos, transparent"), drop everything into a `design/` folder as reference.

3. **Build feature-by-feature with a self-verify loop.** → see [[screenshot-verify-loop]].
   - Implement one screen; tell Claude to screenshot the simulator and compare to the design image, looping until "identical" (~80–90% realistic), then hand-tune values in code.

4. **Test manually, then run an AI code review.**
   - Hand-test the feature in the simulator.
   - Open a PR; **CodeRabbit** auto-reviews (summary, walkthrough, diagram, inline suggestions). Fix the **major** issues via Claude (using CodeRabbit's copy-paste "prompt for AI agents"), commit on the same branch. He explicitly skips minors "because this is a tutorial" but says fix them for real projects.

5. **Git discipline: branch per feature.**
   - First commit → straight to main. Thereafter: **feature branch → PR → CodeRabbit → fix-commits on the same branch → merge → pull to main.** Framed as *"the workflow you'd follow at a real company."*

6. **Loop until no features remain** → project done.

## The self-correcting `PLAN.md` habit

Recurring throughout: after building, he asks Claude *"check `PLAN.md` and mark anything we've implemented but forgot to check off."* At one point Claude finds six such items. This keeps a durable, human-readable source of truth for progress — the same instinct as a living spec.

## Environment conventions he sets

- **`AGENTS.md`** holds tech stack + conventions + hard rules (e.g. *"always use native tabs,"* *"never run the app yourself — I'm already running it in a separate terminal"*), with **`CLAUDE.md` referencing it**. (The verbal justification is partly wrong — see [[agents-md-vs-claude-md]].)
- **Skills**: install vendor skills (Clerk) so Claude follows official docs; they land in `.claude/skills/`.
- **Context7** MCP appended to prompts (*"use context7"*) to pull up-to-date library docs.
- **Permissions**: starts in ask-before-edits to learn, moves to auto-edit; mentions a bypass mode for hands-off editing.

## Why this matters for an operator

This is a clean, portable harness. The transferable parts for [[hireui-pilot-menu]]: the plan-mode interview + `PLAN.md`, the branch-per-feature + AI-review gate, and the screenshot-verify-loop for UI work.
