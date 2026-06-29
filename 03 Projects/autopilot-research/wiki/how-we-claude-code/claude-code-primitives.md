# Claude Code Primitives Referenced in the Workshop

> Verified against official docs (`code.claude.com/docs`, `platform.claude.com`) as of June 2026 — see [[how-we-claude-code/source-provenance]]. Most are confirmed from the workshop transcript itself.

| Primitive | What it does | Invocation | Status |
|---|---|---|---|
| **Auto Mode** | Permission mode where Claude auto-classifies/blocks risky tool calls and proceeds otherwise | **Shift+Tab** cycles modes (default → acceptEdits → plan → auto) | ✅ Confirmed. Arno: *"you need to be using auto mode … it makes it so much easier."* |
| **Fast Mode** | Faster **output generation** (same model), good for iterating on specs | `/fast` | ✅ Confirmed. *"costs more, but it's great for iterating quickly on specs."* |
| **`/effort`** | Adaptive **reasoning depth** (distinct from Fast Mode) | `/effort <level>`; levels: `low · medium · high(default) · xhigh · max` | ✅ Confirmed. Arno recommends **x-high** (or `max`). |
| **`/goal`** | Persistent autonomous loop toward a measurable completion condition; a fast model re-checks each turn | `/goal <condition>` | ✅ Confirmed (Claude Code v2.1.139, 2026-05-12). Arno mentions `/goal`. |
| **Ask User Question** | Claude presents interactive multiple-choice questions to interview *you* | reference the tool in your prompt (esp. plan mode) | ✅ Confirmed (v2.0.21+). The engine of [[how-we-claude-code/pillar-1-interview-and-bitter-lesson]]. |
| **Playwright MCP** | Browser automation via structured accessibility/DOM snapshots (~200–400 tokens), not pixels | `@playwright/mcp` in MCP config (~10 min setup) | ✅ Confirmed. Arno: *"I've already connected the Playwright MCP for this."* |
| **Storybook fixtures** | Component-isolation testing pattern the verify framework borrows from | community skills + `play()` tests | ⚠️ **Community pattern**, not a first-party-documented Claude Code feature. |

## Model recommendation (and the version drift)

- **Workshop (2026-05-23):** *"Try using **Opus 4.7** … it has a better vision model. That's where this really excels. If you use **Sonnet**, I wouldn't recommend that."* Opus 4.7 (April 2026) did ship "substantially better vision."
- **Today (June 2026):** the current top model is **Opus 4.8** (May 2026); **Fable 5** launched 2026-06-09. **A pilot run today should use Opus 4.8** (superset of 4.7's vision gains) + Fast Mode for spec iteration. *(Effort levels are available on Fable 5, Opus 4.8/4.7/4.6, Sonnet 4.6.)*

## Key Takeaways

- **Fast Mode (speed) ≠ `/effort` (reasoning depth)** — they're orthogonal knobs; the workshop uses both.
- **Auto Mode + `/effort x-high` + `/fast`** is Arno's default rig for this workflow; **Ask User Question** + **Playwright MCP** are the two tools that make pillars 1 & 3 work.
- Substitute **Opus 4.8** for the talk's "Opus 4.7" in any present-day pilot.
- Storybook is borrowed-from, not required — the verify framework is dependency-light TypeScript ([[how-we-claude-code/verification-framework-deep-dive]]).
- Cross-link: [[../claude-code-hooks/_index]], [[../10x-claude-code/_index]].
