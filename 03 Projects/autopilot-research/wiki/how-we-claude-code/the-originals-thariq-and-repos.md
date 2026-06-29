# The Originals — Thariq Shihipar, the Repos, and the Bitter Lesson

> The operator ask was *"double deep-dive into the original resource."* The workshop is downstream of four originals; this page is the map. Each was fetched from a primary source (blog, `gh api`, docs) — see [[how-we-claude-code/source-provenance]].

## 1. Thariq Shihipar — the HTML originator

- **Who:** Member of Technical Staff / engineer on the **Claude Code team at Anthropic** (confirmed via ChatPRD interview + GitHub profile). X: [@trq212](https://x.com/trq212). *(Arno pronounces it "Tariq/Tarik" in the talk; canonical spelling is **Thariq Shihipar**.)*
- **The blog:** *"Using Claude Code: The Unreasonable Effectiveness of HTML"* — [claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html). Arno: *"the talk that Tariq gave in San Francisco … he published that as a blog post called The Unreasonable Effectiveness of HTML files."* The intellectual origin of [[how-we-claude-code/pillar-2-html-specs-over-markdown]].
- **His three named workflows** (ChatPRD): (1) **brainstorming/planning with interactive HTML**; (2) **building throwaway micro-apps to edit your plan** ("micro-software on top of micro-software"); (3) **a "living design system in HTML"** (`design_system.html`) that travels with the code across sessions.
- **Philosophy:** an *"abundance mindset … developers can now afford to generate these throwaway tools"* + trust-based delegation (*"Hey Claude, I trust you here"*).

## 2. `ThariqS/html-effectiveness` — the companion gallery

- [github.com/ThariqS/html-effectiveness](https://github.com/ThariqS/html-effectiveness) (also mirrored as `anthropics/html-effectiveness`), Apache-2.0, **519★**, updated 2026-06-28. *"Sample code. Not maintained and not accepting contributions."*
- **Exactly 20 self-contained `.html` files** (`01`–`20` + `index.html`), no build tools, no dependencies, browser-native, fictional "Acme" sample data.
- **9 categories** on the companion site [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/): Exploration & Planning · Code Review & Understanding · Design · Prototyping · Illustrations & Diagrams · Decks · Research & Learning · Reports · Custom Editing Interfaces. *(The blog groups them more coarsely as ~5 use-case buckets; the companion site is the finer 9. Both counts verified — see provenance.)*
- Notable examples: `05` Living Design System (token swatches), `20` Prompt Tuner (live variable interpolation), `18` Triage board (drag-drop → export markdown), `07` Animation sandbox.
- Has spawned **7+ community derivative skills** (e.g. `prefer-html-output-skill`, `thariq-html-output-skills`, Cursor/Claude-Code ports).

## 3. `anthropics/cwc-workshops` — the workshop repo

- [github.com/anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) ("CW… workshops" = **C**laude **w**ith **C**ode workshops), **1,212★**, pushed 2026-06-26. Contains 9 workshop folders (agent-battle, eval-driven-agent-development, production-ready-agent, research-desk, …) — **`how-we-claude-code/`** is this one.
- Three phases: `phase-1-exploration/PROMPT.MD`, `phase-2-planning/PROMPT.MD`, and the full `phase-3-verify/` app. Deep-dived in [[how-we-claude-code/verification-framework-deep-dive]].

## 4. Richard Sutton — *The Bitter Lesson* (2019)

- Author **Richard S. Sutton** (father of reinforcement learning, U. Alberta), essay at incompleteideas.net, ~20K citations.
- **Thesis:** *"The general methods that leverage computation are ultimately the most effective, and by a large margin"* — breakthroughs come from compute + search + learning, **not** from human-encoded domain knowledge.
- Arno uses it as the philosophical backbone for [[how-we-claude-code/pillar-1-interview-and-bitter-lesson]] — see that page (and [[how-we-claude-code/caveats-and-when-not-to-use-html]]) for where the analogy is fair vs. over-stretched.

## Secondary corroboration (not originals, but useful)

- Thariq's own talk *"Why this Claude Code engineer uses HTML files as AI specs"* ([Qrpm7E80wQ0](https://www.youtube.com/watch?v=Qrpm7E80wQ0)).
- [ChatPRD "How I AI" interview](https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html) · [Lenny's Newsletter](https://www.lennysnewsletter.com/p/html-is-the-new-markdown-how-anthropic) · [Simon Willison](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/).

## Key Takeaways

- **One person (Thariq Shihipar) is the origin of pillars 1 & 2**; the cwc-workshops repo is the origin of pillar 3; Sutton is the philosophical frame.
- **20 HTML files / 9 categories** is exact and verifiable; the blog's own "5 categories" is a coarser grouping of the same work.
- *"Went viral / millions of views"* is **unverified** — the repo has hundreds of stars, not viral metrics. Treat as reported. (See [[how-we-claude-code/source-provenance]].)
