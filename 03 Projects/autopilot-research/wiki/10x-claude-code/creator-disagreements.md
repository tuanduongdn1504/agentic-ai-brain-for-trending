# Creator Disagreements

The 6 creators agree Claude Code is powerful but diverge on **model strategy**, **plan-mode lifespan**, **`claude.md` philosophy**, **browser strategy**, and **interface preference**. Five axes worth tracking.

## 1. Model strategy: Opus-everything vs model-switching

- **Sean Kochel — Opus maximalist:** use Opus for everything. Argues that arriving at a correct solution faster with Opus is ultimately cheaper than multiple iterations with a "dumber" model.
- **Chase AI — Efficiency pragmatist:** use `/model` to switch based on task complexity. Treats Opus 4.6 as a "nuclear bomb" not warranted for simple chores; recommends Sonnet or Haiku for the routine.

**Reconciliation:** Kochel's argument holds when failure costs are high (user-facing bugs, security-sensitive code). Chase's holds when tasks are bounded and verifiable (renaming, refactoring with test coverage). Pick per-task, not per-philosophy.

## 2. Plan Mode lifespan and necessity

- **Chase AI — Non-negotiable:** Plan Mode is a "must" — every single time you start a new project or feature.
- **Boris Cherny — Limited lifespan:** as the *creator* of Claude Code, predicts Plan Mode has ~1 month of relevance. The model is already learning to enter plan mode autonomously when it senses a complex task. The literal `/plan` command will become unnecessary.

**Reconciliation:** adopt the *pattern* (alignment before execution), not the *command*. The pattern is robust; the command is implementation detail. See [[../workflow-ai-coding/core-patterns|workflow-ai-coding § Planning-First]] for the broader frame.

## 3. `claude.md` philosophy: minimalism vs documentary

- **Boris Cherny — Minimalist:** his personal `claude.md` is **two lines**, focused only on PR automations.
- **Sean Kochel — Nuke-and-restart:** if the file becomes "noisy", delete it and start fresh rather than over-engineer.
- **AI LABS — Documentary:** uses `claude.md` as hub for a complex SOP system; recommends **`feature.json`**, `architecture.md`, `decision.md` (decision log), and PRD all as project artifacts.
- **Eric Tech — Skill-decomposed:** breaks the knowledge into separate `.md` skill files instead of one bloated `claude.md`.

**Reconciliation:** see [[claude-md-philosophy]] for the full deep-dive. Short version: minimalist works for solo devs on familiar codebases; documentary works for teams or unfamiliar codebases. Most operators eventually drift toward Eric Tech's skill-decomposed middle path.

## 4. Browser verification: standard Chrome vs Agent Browser

- **Sean Kochel + Boris Cherny — Standard Chrome extension (`-chrome`):** high-impact, simple to enable. Agent iterates on UI until it "looks good".
- **AI LABS — Vercel's Agent Browser:** Chrome extension is problematic because it loads the entire DOM into context, exhausting it. Vercel's Agent Browser uses accessibility tree to compress thousands of tokens of DOM data down to **200-400 tokens**.

**Reconciliation:** if your pages are simple and your context budget is generous, Chrome is fine. If pages are DOM-heavy (modern React apps with lots of components) or you're running long sessions, Agent Browser's compression matters.

## 5. Future of the interface: terminal vs GUI

- **Boris Cherny — Surprised the terminal stuck:** admits it's "unbelievable" the CLI became the ending point. Originally viewed it as cheap prototype; expected industry to move toward graphical IDEs quickly.
- **Chase AI — Beginner-friendly GUI:** suggests new users start with VS Code or Claude Code Desktop app — terminal is "intimidating" for non-technical users.

**Reconciliation:** terminal-first is current best practice for power users; GUI is on-ramp for beginners. Boris's surprise suggests the GUI vs CLI debate isn't settled — expect more GUI options soon.

## How to use these disagreements

When reading any single creator's "10x" advice, locate them on these 5 axes. Their advice is shaped by where they sit:

- A creator who optimizes for token cost (Chase AI) gives different advice than one who optimizes for solution-correctness-per-attempt (Kochel).
- A creator with a 200-line `claude.md` documents differently than one with 2 lines.
- A creator using Vercel Agent Browser doesn't talk about DOM-blowing-up-context the same way.

Pattern-match the *axis position* of the creator before adopting their tip wholesale.

See [[overview]] for the philosophical frame, [[tactical-tricks]] for the consensus moves where creators agree.
