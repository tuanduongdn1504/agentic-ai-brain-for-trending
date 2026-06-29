# How We Claude Code — Workshop Overview

## Source

- **Entry point (operator-submitted):** Vietnamese dub "Workshop Anthropic | Hướng Dẫn Build App Có Verification Agent-Native" — [ATsbgIRA0Fw](https://www.youtube.com/watch?v=ATsbgIRA0Fw) (BizMate AI Official, 2026-06-25, 31:37). A faithful localization of the Anthropic original.
- **Original (authoritative):** **"How we Claude Code"** — [IlqJqcl8ONE](https://www.youtube.com/watch?v=IlqJqcl8ONE) (channel: Claude / Anthropic, 2026-05-23, 31:43, 50.8K views). Presenter **Arno**, member of Anthropic's **Applied AI** team ("architect"). Full English transcript in `raw/2026-06-29-how-we-claude-code-anthropic-workshop.md` (read in full).
- **Code:** [anthropics/cwc-workshops](https://github.com/anthropics/cwc-workshops) → `how-we-claude-code/` (1,212★).

## What it is

A live, code-along workshop showing **how Anthropic engineers actually use Claude Code** — not features in isolation, but a *way of working* tuned to the fact that **agents now run longer and burn more tokens, so the cost of a vague spec is higher than ever.** Arno's framing: *"If you're going to let your agent run for a longer period of time, then you can burn through a lot of tokens if it does the wrong thing. You want to avoid that ideally at the beginning."*

The whole talk is one argument: **front-load the human-verification you'd do later, into the spec — and make verification native to the artifact so the agent can do it for you.**

## The three pillars

1. **[[how-we-claude-code/pillar-1-interview-and-bitter-lesson|Let Claude interview you]]** — stop writing vague prompts ("make it better"); use the **Ask User Question** tool so Claude pulls the latent requirements *out* of you. Grounded in Sutton's *Bitter Lesson*: resist over-constraining an increasingly capable model.
2. **[[how-we-claude-code/pillar-2-html-specs-over-markdown|HTML specs over Markdown]]** — Markdown >~100–200 lines goes unread; **HTML** is denser, visual, and shareable. Generate **4 parallel design directions**, screenshot, feed back. Origin: **Thariq Shihipar's** blog *"The Unreasonable Effectiveness of HTML."*
3. **[[how-we-claude-code/pillar-3-agent-native-verification|Agent-native verification]]** — build verification *into* the artifact: components publish state to the DOM via `data-verify-*` attributes; one engine drives **three surfaces** (human dashboard / agent-in-browser / headless CI) and can **record runs as video clips**.

## The repo's three phases

| Phase | Folder | What it demonstrates | Example domain |
|---|---|---|---|
| 1 — Exploration | `phase-1-exploration/PROMPT.MD` | Claude interviews you via **AskUserQuestion** → a spec | **Bill-splitting app** |
| 2 — Planning | `phase-2-planning/PROMPT.MD` | Generate **4 HTML design directions** to compare | Bill-splitting app |
| 3 — Verify | `phase-3-verify/` (full Vite+React app) | The **agent-native verification framework** | **Todo app** (separate, self-contained) |

> ⚠️ **Correction vs. the video framing:** the bill-splitting app is only the phase 1–2 example. **Phase 3 — where the verification framework lives — is a separate React + Vite *Todo* app** (`src/features/todos/*`). See [[how-we-claude-code/source-provenance]].

## Closing recommendations from Arno

- **Use Auto Mode** (shift+Tab) always; it "makes it so much easier."
- **Set `/effort` to x-high** (or `max`); use **Fast Mode** (`/fast`) for quick spec iteration — "costs more, but great for iterating quickly on specs."
- **Use Opus 4.7, not Sonnet**, for this — its better vision model excels at frontend/screenshot feedback. *(At the talk date this was current; a **today** pilot should use **Opus 4.8** — [[how-we-claude-code/claude-code-primitives]].)*
- On token cost: *"Isn't an HTML spec more token inefficient? … the answer tends to be no … in the long term you iterate less if you have a good and rich HTML spec."* — though Thariq's own writing is more nuanced (HTML costs 2–4× tokens; see [[how-we-claude-code/caveats-and-when-not-to-use-html]]).

## Key Takeaways

- The unifying idea is **"agent-first"** — *"the remixing and new arrangement of primitives you're already familiar with … just to make it available to the agent first."*
- Longer agent runs raise the value of a **comprehensive spec verified up front** — the HTML file is the verification surface.
- Verification is **runtime observation at the rendered surface (the DOM), not static analysis or React-internal tests** — which is what makes it agent-drivable.
- None of the three pillars needs new tooling; they're a **discipline** on top of existing Claude Code primitives + a small React pattern.
- See [[how-we-claude-code/_index]] for the full article map and [[how-we-claude-code/source-provenance]] for what was independently verified vs. corrected.
