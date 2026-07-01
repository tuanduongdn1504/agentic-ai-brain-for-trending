# Open Design vs Claude Design (open vs closed)

## Source

[Claude Design announcement](https://www.anthropic.com/news/claude-design-anthropic-labs) (Anthropic, verified via WebFetch + TechCrunch/VentureBeat/DataCamp, 2026-07-01) vs `nexu-io/open-design` README. Workflow `wf_4a91a8b2-2bb` agent `claude-design-product`.

## Claude Design is real (the load-bearing fact)

The whole "alternative to" framing depends on Claude Design existing — and it does. **Verified:**

- **Introducing Claude Design by Anthropic Labs**, launched **2026-04-17** ([anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)).
- *"A new Anthropic Labs product that lets you collaborate with Claude to create polished visual work like designs, prototypes, slides, one-pagers, and more."*
- **Research preview**, powered by **Claude Opus 4.7** (Anthropic's "most capable vision model").
- **Cloud-only**, accessed at **claude.ai/design**. **Subscription-gated:** included for **Pro / Max / Team / Enterprise**, using your plan's limits (no separate checkout).
- **Reads your codebase + Figma files** to auto-extract a design system and apply it to new projects; hands off to **Claude Code** for development.
- Market signal: **Figma stock fell ~7%** and Adobe ~1.5% on launch day (per TechCrunch/VentureBeat) — the market read it as a serious Figma challenger.

> ⚠️ The workflow's synthesis critic flagged "Claude Design existence unverified" as its #1 concern. That flag is **overridden** — a direct fetch of the Anthropic announcement + three independent outlets confirm it. This is a recurring pattern in this vault (verifiers declaring real things unverifiable because *they* couldn't reach the source); see [[open-design/source-provenance]].

## The comparison

| Dimension | **Claude Design** (Anthropic) | **Open Design** (nexu-io) |
|---|---|---|
| Source | Closed | **Open (Apache-2.0)** |
| Where it runs | Cloud (claude.ai/design) | **Local-first** (127.0.0.1 daemon, desktop app) |
| Model | Locked to **Opus 4.7** | **Any agent on your PATH** (Claude Code / Codex / Cursor / Gemini / Copilot / …) or BYOK proxy |
| Cost | Bundled in Pro/Max/Team/Enterprise subscription | **Free tool; you pay only your own API/agent usage (BYOK)** |
| Data | Anthropic cloud | **Stays in your project directory** |
| Design system | Auto-extracted from codebase/Figma; Anthropic-hosted | **Portable `DESIGN.md`** in your repo (version-controlled) |
| Extensibility | Anthropic's surface | **`SKILL.md` skills + plugins** you can add/fork |
| Maturity | Anthropic-backed, but research preview | **~2 months old**, viral (73K★), pre-1.0 |
| Handoff | → Claude Code | → your CLI directly (it *is* your CLI) |
| Outputs | designs, prototypes, slides, one-pagers | prototypes, dashboards, decks, images, video, HyperFrames → HTML/PDF/PPTX/MP4 |

## The honest "when to use which"

- **Claude Design** wins on: polish, zero setup, first-party reliability, tight Figma/codebase extraction, and it's *already included* if you have a Max/Team/Enterprise plan. It's the safe, cloud-convenient, designer/PM-friendly choice.
- **Open Design** wins on: **no vendor lock-in** (swap agents), **local-first / data-stays-home** (matters for a recruitment SaaS's sensitive data), **model-agnostic cost control** (BYOK, pick a cheaper model per task), and **hackability** (fork skills, own the `DESIGN.md`). It's the developer/harness-first choice — and the one aligned with hireui's **GitNexus-first + I-8 operator-owned + agent-`*`-branch** constraints.
- **They're not exclusive.** You can design in Claude Design (or import its `.zip` export) and continue locally in Open Design on your own agent — the video does exactly this.

For hireui specifically, Open Design's **local-first + BYOA + portable-`DESIGN.md`** profile is the better *architectural* fit; Claude Design is the better *convenience* option if you're already on a qualifying plan and don't need self-hosting. Pilot guidance: `output/(C) 2026-07-01-open-design-pilot-methods.md` (H1, H6).

## Key Takeaways

- **Claude Design is a genuine Anthropic Labs product** (2026-04-17, Opus 4.7, cloud-only, Pro/Max/Team/Enterprise) — the premise holds; the critic's "unverified" flag is overridden by primary sources.
- Open Design's differentiators are **open-source, local-first, model-agnostic (BYOA/BYOK), and portable `DESIGN.md`** — vs Claude Design's polished-but-closed, cloud-only, Opus-locked, subscription model.
- **Neither dominates:** Claude Design = convenience + polish + already-in-your-plan; Open Design = control + privacy + hackability + cost. They interoperate via `.zip` import.
- For **hireui**, Open Design's profile fits the CONSTITUTION (local, operator-owned, agent-branch) better; Claude Design is the low-effort fallback if you're already subscribed.
