# NEW deep-dive: Impeccable (`pbakaus/impeccable`)

> The rival anti-slop design system — and the most-misreported claim in the video.

## Verified facts (gh api, 2026-06-29)

- **Repo:** `pbakaus/impeccable` · **42,154★** · **Apache-2.0** · JavaScript · created **2025-11-16** · pushed 2026-06-29 (daily-active) · not archived.
- **Description:** *"The design language that makes your AI harness better at design."*
- **Author:** **Paul Bakaus** (`pbakaus`) — Creative Technologist at Google; **creator of jQuery UI**, Google for Creators, Spotter Studio. A credible, senior author (this is *not* a throwaway repo).
- **Website:** [impeccable.style](https://impeccable.style) (live).

## What it is

A design-guidance system + CLI for AI coding agents that improves frontend quality through three layers:
1. **23 specialized design commands** — `craft`, `shape`, `init`, `document`, `extract`, `audit`, `critique`, `polish`, `bolder`, `quieter`, `distill`, `harden`, `onboard`, `optimize`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`, `adapt`, `clarify`, `live`. (The skeptic counted exactly **23** files in `skill/reference/` — matching the video's "23"; an earlier draft's "26" was wrong.)
2. **44 deterministic detector rules** — mechanical anti-pattern detection (overused fonts, contrast issues, outdated easing). **No LLM and no API key** required for the detection layer — it runs locally.
3. **A live visual editor** — pick any DOM element on your running dev server, request a change in natural language, and see **three production-ready variants swap in via HMR** before it writes the change back to source as a reviewable diff.

It supports Claude Code, Cursor, GitHub Copilot, plus AWS Bedrock / Google Vertex, and frameworks Vite / Next.js / SvelteKit / Astro / Nuxt / static HTML. It can **export a `DESIGN.md` in Google-Stitch format** — directly composable with [[claude-code-plugins-stack/already-deep-dived-crosswalk|Awesome Design MD]].

## How it works

- `npx impeccable install` (or copy the `.github/` folder) → `npx impeccable init` to set design context (product, audience, brand voice).
- Then invoke `/impeccable <command>` in your harness: `/impeccable craft <target>`, `/impeccable audit`, `/impeccable live`.
- The detector rules run locally and deterministically; the command layer generates guidance or variants; `live` runs a dev-server hook for visual iteration.

## The load-bearing claim — REFUTED

> Chase: *"a couple days ago, Impeccable became a built-in layer for everybody who uses the GitHub Copilot app... GitHub themselves saw this... and made it native to their AI tool."*

**This is false on three counts** (verified against the repo history, release notes, and GitHub's own Copilot docs):

1. **Direction is backwards.** *Impeccable* added **Copilot hook support** (PR #279 "Add GitHub Copilot hook support," merged **2026-06-20**; PR #280 gave Copilot equal prominence). GitHub did **not** integrate Impeccable into Copilot. A "Make Copilot built-in note" commit (2026-06-22) refers to Impeccable pre-bundling Copilot support, not the reverse.
2. **Users still install + enable it.** Release notes for `skill-v3.8.0` (2026-06-21): *"Installing the skill adds a `.github/hooks/impeccable.json`."* Copilot-app users skip the install step but must still **enable it under Settings → Experimental**. This is *pre-bundled support*, not GitHub making it native.
3. **GitHub's docs are silent.** `docs.github.com/en/copilot` contains **zero** mentions of Impeccable.

**Two more corrections:**
- The live visual editor is **alpha**, not "beta" — the docs explicitly say *"Status: alpha. Live Mode works end-to-end and is ready to try, but it still needs more testing against real-world repos and framework configs."*
- The website homepage shows ~12 commands with before/afters, not "every command" — the full reference is at `/docs`.

## Impeccable vs Taste Skill (the design anti-slop rivalry)

Both fight "AI slop"; they're genuinely different:

| | Impeccable | Taste Skill ([[ai-web-design-workflow/_index]]) |
|---|---|---|
| Core | 23 commands + 44 **deterministic** detector rules | 3 dials + brief-inference + a pre-flight gate |
| Differentiator | **live visual editor** (alpha) — click the rendered element, see variants live | portability + opinionated rules (em-dash ban) |
| LLM needed for detection? | **No** (44 rules run locally) | gate is checklist-based |
| Author | Paul Bakaus (jQuery UI, Google) | leonxlnx (solo) |
| Stars | 42.2K | 52.9K |

The live editor is the real reason to try Impeccable *in addition to* the Taste Skill you already surfaced — it's a fundamentally different interaction (visual, on the rendered DOM) than instruction-only skills.

## Operator relevance

Medium-high but **deferred-conditional**. The natural home is the hireui **Candidate-Detail refactor spike** (React/Next.js + Tailwind) once it reaches design-iteration phase: `/impeccable audit` to catch anti-patterns + `/impeccable live` to iterate visually against the Figma source-of-truth. Best framed as a **comparison-pilot layered on top of the Taste Skill** — measure each on the same screen (the live editor is the variable to test). Install per hireui I-8 operator-registry + I-2 agent-branch governance. **Don't reach for it reflexively** — you already have a design lever (Taste Skill); the question Impeccable answers is "do I want a visual on-DOM editor too?"

## Cross-links

- [[ai-web-design-workflow/_index]] — the Taste Skill (its rival); the anti-slop framing
- [[claude-code-plugins-stack/already-deep-dived-crosswalk]] — Awesome Design MD (composes via `DESIGN.md` export)
- [[claude-code-skills-stack/_index]] — Eric Tech's design-skill picks (UI UX Pro Max etc.)
- [[claude-code-plugins-stack/source-provenance]] — the Copilot-claim refutation ledger
