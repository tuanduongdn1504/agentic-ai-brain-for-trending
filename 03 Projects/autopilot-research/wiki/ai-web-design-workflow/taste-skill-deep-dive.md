# Taste Skill — deep dive (the centerpiece original)

> **Repo:** [github.com/leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) · MIT · ~47.2K stars (2026-06-20) · JS/TS · actively developed (20 commits in 23 days, 2026-05-25 → 06-17; commits co-authored by Cursor + Claude Sonnet 4.6). Author **leonxlnx** is pseudonymous.
> **Tagline (verbatim):** *"Taste-Skill — gives your AI good taste. Stops the AI from generating boring, generic slop."*
> **One line:** it converts "generate something that looks OK" into "generate only what passes a **62-point mechanical anti-slop gate**." All facts below are **T1-confirmed** (fetched verbatim from the repo's SKILL.md files), independently by two research agents. See [[ai-web-design-workflow/source-provenance]].

---

## What it is

- A **design-discipline skill** (not a generator): a long, structured set of *mechanical, checkable* rules that an LLM coding agent loads and must obey when building/redesigning a web UI.
- It targets the specific, recurring ways LLM-generated front-ends look generic ("AI slop") and bans them by name.
- Ships as **Anthropic SKILL.md format** (raw markdown, **no YAML frontmatter**) — so it is portable across any skills-supporting agent.

## Install

```bash
# whole library (all variants)
npx skills add https://github.com/leonxlnx/taste-skill
# single variant only
npx skills add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend"
```

It also ships `.claude-plugin/plugin.json` → installable directly as a **Claude Code plugin**. Individual `SKILL.md` files can be copied into a project or pasted into any agent conversation. (Naming note: the core skill's folder is `skills/taste-skill/` but its metadata `name:` is `design-taste-frontend` — the project uses both interchangeably.)

## The 3 configuration dials

Every output is shaped by three 1–10 dials (baseline **8 / 6 / 4** for a premium landing page); a vibe→dial inference table maps words like "minimalist / playful / trust-first" to overrides:

| Dial | 1 ↔ 10 |
|---|---|
| **DESIGN_VARIANCE** | symmetry ↔ asymmetry |
| **MOTION_INTENSITY** | static ↔ choreographed |
| **VISUAL_DENSITY** | gallery/airy ↔ cockpit/packed |

## Step 0 — Brief Inference ("Design Read") before any code

> *"Before any code, state in one line: **'Reading this as: \<page kind\> for \<audience\>, with a \<vibe\> language, leaning toward \<design system or aesthetic family\>.'**"* — e.g. *"Reading this as: B2B SaaS landing for technical buyers, with a Linear-style minimalist language, leaning toward Tailwind utilities + Geist + restrained motion."* (Section 0.B)

This forces a shared read of the brief **before** the agent defaults to clichés.

## The mechanical rules (the actual anti-slop content)

These are the load-bearing, verbatim rules — the reason the skill works. They are the catalogue of "what makes LLM UI look generic," each turned into a binary check.

**Typography**
- **Em-dash (`—`) is COMPLETELY banned** everywhere (headlines, body, quotes, captions, buttons, alt text). *"The single most-violated LLM tell… There is no 'limited use' allowance. None."* (Section 9.G; pre-flight item) — the most distinctive rule in the whole skill.
- **No Inter as the default sans** — rotate Geist, Outfit, Cabinet Grotesk, Satoshi.
- **Serif discouraged** as default; only for genuinely editorial/luxury/heritage briefs with explicit justification. **Banned defaults:** Fraunces, Instrument_Serif. Don't reuse the same serif across consecutive projects.
- Emphasis via italic/bold of the *same* font, not serif+sans mixed in one headline; italic-descender clearance required.

**Layout**
- **Hero must fit the initial viewport:** headline ≤ 2 lines, subtext ≤ 20 words AND ≤ 4 lines, CTAs visible without scroll, top padding ≤ `pt-24` (6rem), hero stack ≤ 4 text elements.
- **No three-equal-column feature cards** ("the #1 LLM layout default") — use zig-zag / asymmetric grid / horizontal-scroll / masonry / Bento instead.
- **Bento grids have EXACTLY as many cells as content items** (zero empty cells); `grid-auto-flow: dense` with mathematically verified `col-span`/`row-span` interlocking.
- **Eyebrow restraint:** ≤ 1 eyebrow per 3 sections — mechanical check `count ≤ ceil(sectionCount/3)` ("the #1 violated rule in production tests").
- Premium-consumer **palette ban:** the warm beige+brass+oxblood+espresso default for cookware/wellness/luxury briefs is banned as the default reach; rotate to cold-luxury / forest / cobalt+cream / etc.

**Motion**
- **Motion code MUST be isolated in Client Components** (`'use client'`, memoized); Server Components render static layouts only.
- **`window.addEventListener('scroll', …)` is hard-banned** (jank-prone). Use Motion `useScroll()`, GSAP `ScrollTrigger`, `IntersectionObserver`, or CSS `animation-timeline: view()`. So are React-state scroll-progress and `requestAnimationFrame` loops touching React state.
- Animate `transform`/`opacity` only, never `top/left/width/height`.
- *"Motion only when motivated"* — every animation must answer "what does this communicate?" (hierarchy/feedback/state). *"GSAP everywhere is amateur."*
- **Reduced motion mandatory for MOTION_INTENSITY > 3** — `useReducedMotion()` / `@media (prefers-reduced-motion)`, degrade to static/instant (accessibility non-negotiable).

**Components / content / accessibility**
- **CTAs:** WCAG AA 4.5:1 contrast minimum, no wrapping at desktop, **no duplicate CTA intent** ("Get in touch" + "Contact us" both present = fail).
- **Icons:** official packages only (Phosphor, HugeIcons, Radix Icons, Tabler); Lucide only on explicit request; one family per project; never hand-roll SVG icon paths.
- **Real images required**, in priority order: (1) an image-generation tool if available, (2) real photography URLs or `picsum.photos/seed/{description}/{w}/{h}`, (3) explicit labeled placeholder slots. **Never** div-based fake screenshots, never pure-text minimalism, never hand-rolled decorative SVGs.
- **One design system per project** (never mix), chosen from **14** official systems available as packages: Material Web, Fluent UI, IBM Carbon, Shopify Polaris, Atlassian, GitHub Primer, GOV.UK, USWDS, Bootstrap, Tailwind, Radix, shadcn/ui, Native CSS/W3C, Apple Liquid Glass.
- Dark mode + accessible loading/error/empty states; Core Web Vitals plausibility.

## The 62-point Pre-Flight Check (the gate)

> *"If a single checkbox cannot be honestly ticked, the page is not done. Fix it before delivering."* (Section 14)

- **62 numbered checkboxes**, **all-or-nothing** — every box must pass before ship (em-dash count = 0, theme/color lock, button + form contrast, hero discipline, eyebrow count, split-header ban, zigzag cap, duplicate-CTA check, Bento cell-count, real images, dark mode, reduced motion, mobile collapse, no-AI-tells, one design system, …).
- ⚠️ **It is a *manual* mechanical checklist, not an automated linter.** The agent (or a verifying loop) reads each item and verifies by counting/inspecting — there is no shipped CLI/linter that runs the 62 checks for you. (Corrected: the draft's "73+ checkboxes" was wrong — it's **62**; and "15+ design systems" → **14**.)

## The 13 skill variants

The repo is a library, not one file:

| Variant | Role |
|---|---|
| **taste-skill** (`design-taste-frontend`) | Core, comprehensive, flexible/contextual (~87 KB SKILL.md) |
| **redesign-skill** | Audit + evolution of an *existing* site (~15 KB) — Scan → Diagnose (8 dims) → Fix |
| **gpt-tasteskill** | Strict, ChatGPT-optimized (~8 KB) — Python-RNG determinism + AIDA + 2-line iron rule |
| taste-skill-v1 | Backward-compat of the core |
| minimalist-skill | Editorial minimalist aesthetic (warm off-white #F7F6F3 + charcoal) |
| brutalist-skill | Industrial/Swiss brutalist (CRT scanlines, zero border-radius) |
| image-to-code-skill | Image-first pipeline (screenshot → UI code) |
| imagegen-frontend-web / -mobile | Section-image generation ("1 section = 1 horizontal image") |
| brandkit · soft-skill · stitch-skill · output-skill | Brand tokens / premium glass / Google-Stitch-compatible / output formatting |

### `redesign-skill` (the command the video uses)
- **Scan** (framework + styling integrity) → **Diagnose** (8 dimensions: typography, color, layout, interactivity, content, components, iconography, code quality) → **Fix** (7-step priority: **font swap → color cleanup → hover states → layout → component replacement → loading/error states → advanced interactivity**).
- Hard rule: *work within the existing stack — no framework migrations or library replacements without dependency verification*; never silently change URL slugs, nav labels, form-field names, logo, or legal copy. (Corrected: it does **not** use named "Greenfield/Preserve/Overhaul" modes — that was a draft error; it uses plain "How This Works" / "Design Audit" sections.)

### `gpt-tasteskill` (the stricter, ChatGPT-tuned variant)
- **Deterministic Python-RNG:** simulate `random.choice()` via prompt-character-count modulo to pick hero architecture, typography stack (Satoshi/Cabinet Grotesk/Outfit/Geist — *never Inter*), 3 component architectures, 2 GSAP paradigms — so the same prompt doesn't always produce the same template.
- **Mandatory `<design_plan>` block before any UI code** (verifies RNG picks, AIDA presence, hero width math, Bento density proof, label sweep, button contrast).
- **AIDA structure:** Navigation → Attention(Hero) → Interest(Bento) → Desire(GSAP Motion) → Action(CTA/Footer), `py-32 md:py-48` between sections.
- **2-line iron rule:** *"The H1 MUST NEVER exceed 2 to 3 lines. 4, 5, or 6 lines is a catastrophic failure."*

## Portability verdict — YES, it runs in Claude Code

- **Format:** Anthropic SKILL.md (raw markdown). **Installs in Claude Code** via `npx skills add …` or as a plugin (`.claude-plugin/plugin.json`).
- Also portable to **Cursor** (`.cursor/rules`), **ChatGPT** (paste into custom instructions), **Cline**, or any LLM context (raw paste). **Stack assumptions:** React/Next.js (Server Components default) + Tailwind v4 + Motion (`motion/react`) + GSAP/ScrollTrigger; the *principles* are framework-agnostic but the canonical code skeletons are React.
- **Token footprint:** the core SKILL.md is ~87 KB ≈ ~26K tokens if pasted whole — material if you inject it into every message; prefer the **on-demand skill** mechanism (progressive disclosure) over stuffing it into `CLAUDE.md`. See [[claude-api-cost-optimization/_index]].

## Honest caveats (what to weigh before adopting)

- **Pseudonymous author + no automated tests of all 13 variants** → maintenance/bus-factor risk. Mitigation: it's **MIT**, so you can fork and pin a known-good commit. (License covers redistribution; whether prompt-framing edits count as a "derivative" inside a proprietary product is unsettled — assume permissive, don't sell the skill itself.)
- **The 62-point gate is manual** — it's a discipline the agent self-checks, not a guaranteed linter. For a hard gate you'd wrap it in your own verification loop (or an [[prompt-evaluation/_index|eval]] / a [[claude-code-hooks/_index|hook]]).
- **Opinionated stack** (React/Tailwind/Motion/GSAP). If hireui's frontend is on a different stack, the *principles* transfer but the code skeletons won't drop in unchanged.

## Key takeaways

- The skill's value is a **named catalogue of LLM design tells** turned into **binary checks** — reusable as a design-QA rubric *independent of any tool*.
- It is **vendor-neutral and Claude-Code-native**; a Claude shop loses nothing by skipping the OpenAI stack.
- The most quotable, transferable rule: **ban the em-dash** — the #1 "this was written by an LLM" tell, applicable to *prose* as much as UI (cf. the Humanizer in [[claude-skills/the-eight-meta-skills]] and Wikipedia "Signs of AI writing").

## Cross-links

[[ai-web-design-workflow/the-redesign-workflow]] · [[ai-web-design-workflow/overview]] · [[claude-skills/original-anthropic-agent-skills]] (the SKILL.md format) · [[claude-skills/original-wikipedia-signs-of-ai-writing]] (the prose analog of "design tells") · [[harness-engineering/_index]] · [[claude-api-cost-optimization/_index]]
