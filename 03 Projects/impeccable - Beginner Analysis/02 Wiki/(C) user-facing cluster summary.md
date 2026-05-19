# (C) Cluster: User-facing — what impeccable does + how to use it

## In one sentence

Impeccable is an Apache-2.0 Claude/Cursor/etc. skill that gives AI coding assistants a structured design vocabulary so AI-generated UIs stop looking AI-generated — invoked via `/impeccable <command> [target]` across 14 supported AI harnesses.

## Who it's for

PRODUCT.md is specific: the target user is the **developer-designer pair using AI coding tools who already knows the problem** — they arrive via GitHub or word-of-mouth, recognize AI output reads as "AI-made" (dark mode, purple-to-blue gradients, glassmorphism, cards-in-cards), and want practical guidance not education.

Not the target: someone seeking a tutorial on web design fundamentals.

## What you get when you install it

**One skill (`/impeccable`) with 23 sub-commands organized in 6 category-color-tints** (Create magenta / Evaluate purple / Refine blue / Simplify amber / Harden green / System gray). The skill loads two context files (`PRODUCT.md` required, `DESIGN.md` recommended) before any command runs.

**Anchor commands:**

| Command | What it does |
|---------|--------------|
| `/impeccable shape` | Plan UX/UI before coding (PRE-build) |
| `/impeccable craft` | End-to-end feature build (BUILD) |
| `/impeccable teach` | Set up PRODUCT.md + DESIGN.md (PRE-skill bootstrap) |
| `/impeccable document` | Generate DESIGN.md from existing code |
| `/impeccable critique` | UX design review with scoring (EVAL) |
| `/impeccable audit` | A11y + performance + responsiveness (EVAL) |
| `/impeccable bolder` / `quieter` / `distill` | Amplify / tone down / simplify (REFINE) |
| `/impeccable animate` / `colorize` / `typeset` / `layout` | Add motion / color / typography / spacing (ENHANCE) |
| `/impeccable live` | Browser-based visual variant generation |
| `/impeccable polish` | Final shipping readiness (corpus-first "polish command" formalization) |

Plus **27 deterministic anti-pattern rules** with a standalone CLI detector — `npx impeccable detect <path-or-URL>` works without an API key and scans for the banned moves: pure black/white, left-border color stripes, gradient text, dark-mode-by-default, glassmorphism, second accent colors, bounce easing, layout animation, nested cards, identical card grids, hero-metric templates, hedging copy, non-standard spacing tokens, and ~15 others.

## How invocation works

`/impeccable <command> [target]` — first word matches a command, the skill loads the matching reference file, then executes against the target.

`/impeccable critique blog` → loads `reference/critique.md` + executes scored UX review on the `blog` route.

No argument → command menu + user-intent question. Generic call without command → setup + shared design laws + register-appropriate (brand vs product) reference.

If `PRODUCT.md` is missing, the skill runs `/impeccable teach` first — boot-strap before work.

## Shared design laws (loaded for every command)

Every command sits on top of these:

- **Color**: OKLCH only; avoid pure black/white; pick a strategy on the Restrained-→-Drenched spectrum
- **Theme**: choose dark/light based on a physical scene the interface evokes, not category defaults
- **Typography**: cap body at 65–75 characters per line; use weight + scale for hierarchy
- **Layout**: vary spacing for rhythm; **no nested cards**
- **Motion**: ease out exponentially (`cubic-bezier(0.16, 1, 0.3, 1)`); **never animate layout properties**
- **Absolute bans** (5): no side-stripe borders, no gradient text, no default glassmorphism, no hero-metric templates, no modals as the first thought

The skill calls this the **AI slop test**: if output obviously reads as AI-generated, the skill failed its job.

## Editorial voice (STYLE.md)

STYLE.md treats copy as a first-class deliverable. It enforces:

- Open with the reader's wrong belief, your strongest claim, or the example — never throat-clearing
- Take a stance someone could genuinely disagree with
- Concrete details over adjectives: "54 KB" beats "lightweight"
- Vary sentence rhythm: long, long, short
- Active voice dominates
- **Denylist** (build-validator-enforced): load-bearing / highest-leverage / biggest unlock / seamless / robust / elevate / empower / delve / underscore / tapestry / in today's / whether you're / let's dive in / in summary / in conclusion / em-dashes

Final test: read aloud, swap your brand for a competitor's, ask if anything became false. If not, rewrite.

## Where to get it

- Bundle download from `https://impeccable.style`
- Copy from `pbakaus/impeccable` GitHub repo into your project's harness directory (`.claude/skills/impeccable/`, `.cursor/skills/impeccable/`, etc.)
- CLI: `npx impeccable detect <path>` runs the 27-rule anti-pattern scanner standalone

## Reading order

If you only read three files: **PRODUCT.md** (philosophy + target user) → **DESIGN.md** (the 7 design domains + 27 anti-patterns) → **STYLE.md** (editorial discipline). Everything else (AGENTS.md / HARNESSES.md / NOTICE.md / DEVELOP.md / CLAUDE.md) is contributor-facing.
