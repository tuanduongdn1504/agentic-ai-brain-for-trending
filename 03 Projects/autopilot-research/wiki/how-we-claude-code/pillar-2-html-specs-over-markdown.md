# Pillar 2 — HTML Specs Over Markdown

## Source

Workshop (~10:00–12:30, 15:30–17:45) + **Thariq Shihipar**, *"Using Claude Code: The Unreasonable Effectiveness of HTML"* — [claude.com/blog](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html) (companion: [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/) + [github.com/ThariqS/html-effectiveness](https://github.com/ThariqS/html-effectiveness), Apache-2.0, 519★). Corroborated via ChatPRD interview + Simon Willison. See [[how-we-claude-code/the-originals-thariq-and-repos]].

## The thesis

A colleague of Arno's: *"The Markdown file is the lingua franca of the AI-native software development life cycle."* Arno calls it poetic — *but the format is getting constrained.* Markdown specs grow past **~100–200 lines and nobody reads them** ("certainly unlikely that your colleagues are going to read them"). **HTML condenses more information and is more ergonomic to engage with** before the agent starts building.

Thariq's five claimed advantages of HTML output:
1. **Information density** (tables, mockups, diagrams inline)
2. **Visual clarity / organization** (tabs, links, responsive layout)
3. **Ease of sharing** (a browser link, mobile-responsive)
4. **Two-way interactivity** (sliders, toggles, export buttons → feed results back to Claude)
5. **Data ingestion** (pull from files, MCPs like Slack/Linear, git logs)

> *"I have honestly stopped using Markdown altogether for almost everything, but I'm probably far on the HTML maximalist side of things."* — Thariq

## Techniques demonstrated / documented

- **Generate 4 design directions in parallel.** Arno's prompt (in the repo): *"Give me a few different directions, four different design directions, explore them, generate them as HTML"* → e.g. one **Brutalist**, one **Tokyo FinTech**. Click through, compare aesthetics.
- **Screenshot → feedback loop.** *"Especially when you're doing front-end, it's really hard to articulate 'the thing is slightly off' … it's easier for Opus 4.7 (better vision model) to extract from you what the problem is."* Take a screenshot of the rendered HTML, paste it back.
- **Export buttons** ("Copy as JSON / Markdown / diff") so a UI edit flows back into Claude as a spec.
- **Live-preview editors / micro-apps** — disposable single-purpose UIs (a draggable prioritizer, a prompt tuner) generated to *edit the plan*, then thrown away.
- **`design_system.html`** — a portable design-token file Claude references across sessions for visual consistency.

## On token cost

- Arno (workshop): *"Isn't an HTML spec more token inefficient? … the answer tends to be no … in the long term you iterate less if you have a good and rich HTML spec."*
- Thariq (blog): HTML *does* cost more tokens, **but** *"the 1 million context window in Opus 4.7 renders this negligible. The trade-off favors expressiveness and user engagement over raw token economy."*
- ⚠️ Independent reporting puts the overhead at **2–4× Markdown's tokens**, and notes only ~1% of Thariq's generated tokens reach production (the rest is scaffolding). The "no" is a *long-run-iterations* argument, not a per-document one. See [[how-we-claude-code/caveats-and-when-not-to-use-html]].

## Key Takeaways

- **Markdown over ~100–200 lines goes unread → use HTML for rich, sharable, interactive specs.**
- The highest-leverage moves: **4 parallel design directions** + **screenshot feedback** (needs a strong vision model — Opus 4.7/4.8).
- HTML's superpower is **two-way interaction** (export buttons, micro-apps) that round-trips edits back to Claude.
- Token cost is real (2–4×); justified *only* when richer specs cut total iterations — not a blanket "always HTML." Critically: **this vault's own Markdown wiki is exactly a case where Markdown wins** (greppable, diffable, RAG-friendly) — see caveats.
- Cross-link: [[../ai-web-design-workflow/_index]] (design generation + anti-slop), [[../prompt-evaluation/_index]] (spec verification).
