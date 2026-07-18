# (C) ui-skills — Deep Dive

> LLM Wiki **v218** · subject `ibelick/ui-skills` · built 2026-07-18 · **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` (no workflow / no subagent — the ~205K shim overflows subagent context → prompt-too-long, the v200→v217 self-throttle). Source hand-fetched (repo page + raw README + `package.json` + registry + two SKILL.md + the `ui-skills.com` skill index); identity + landscape by WebSearch; collision by sanity-anchored hand-grep.
>
> ⚠️ **NOT source-cloned** (flagged): the `ui-skills.com` site 403'd to WebFetch and the CLI `.ts` implementation (`bin/ui-skills.js` is only a `tsx` wrapper spawning an unfetched `.ts`) was not source-read → `start` behaviour is characterised from the README + the `ui-skills-root` skill, and the full 262-skill enumeration is from `src/data/registry.ts` (partial).

## One-line

**`ibelick/ui-skills` — "Skills for Design Engineers": a curated, categorized, multi-repo REGISTRY + CLI dispatcher of design-engineering agent skills (262 skills / 31 topics aggregated from many external repos) plus ~6 first-party anti-slop UI skills, so a coding agent (Codex / Cursor / Claude Code) pulls the right UI skill for the task on demand.**

## What it is (verified)

The rise of AI coding agents means UIs are generated faster than ever, and they trend toward "averaged-out slop" — the same fonts, gradient hero, rounded cards, layout drift, missing a11y. `ui-skills` attacks that by giving a coding agent a **discovery + fetch layer over design-engineering skills**:

- **A CLI** (`bin/ui-skills.js` → `tsx` → an unfetched `ui-skills.ts`), invoked via `npx`:
  - `npx ui-skills start` — prints the **`ui-skills-root` router-skill**, which teaches the agent to pick the right sub-skill for its task (verified from the site: *"shown by `npx ui-skills start` … for use when an agent in Codex, Cursor, or Claude Code has a clear UI goal"*).
  - `npx ui-skills categories` — list the 31 topic categories.
  - `npx ui-skills list --category motion` — list skills in a category.
  - `npx ui-skills get baseline-ui` — fetch a named skill's markdown.
- **A registry** (`src/data/registry.ts`): **262 skills across 31 topics**, each entry `{ slug, user, repo, rawUrl, githubUrl, name, description, topics }`. Most entries **point at skills hosted in OTHER GitHub repos** — this is a curated **aggregator**, not a monolithic single-author collection. AGENTS.md rule (verbatim): *"Do not add local `skills/*` files unless the repo actually hosts the skill markdown."*
- **~6 first-party skills** in `skills/` (hosted here): `baseline-ui`, `improve-ui`, `fixing-accessibility`, `fixing-metadata`, `fixing-motion-performance`, `ui-skills-root`.
- **An Astro website** (ui-skills.com) deployed on Cloudflare (`@astrojs/cloudflare` + `wrangler.jsonc`) — the human-browsable index of the registry.

**Topics (31, verified from the registry):** accessibility, motion, systems, visual, interaction, performance, craft, taste, typography, color, 3d, frontend, architecture, frameworks, testing, debugging, code-quality, tooling, video, nextjs, nuxt, vue, react-native, threejs, remotion, swiftui (+ others).

**Aggregated from (verified sample):** `MengTo/Skills` (design taste / visual / animation / gsap / threejs), `vercel-labs` (Next.js/React — the corpus's **v51** author), `antfu/skills` (Vue/Nuxt/tooling), `anthropics/skills` (Canvas/frontend-design), `pbakaus` (= the corpus's **impeccable v75** author), `mattpocock` (= the corpus's **v57** author), `shadcn` (improve / shadcn workflow), `wshobson` (WCAG audit), `emilkowalski`, `raphaelsalaja` (12 principles of animation), `0xdesign`, `Jane-xiaoer`, `cloudai-x`, etc.

### The first-party skills (representative quality)

**`baseline-ui`** (frontmatter: *"Quickly develop UI code by fixing spacing, hierarchy, typography, and small layout issues… when the interface needs a fast cleanup or polish pass"*; body: *"Enforces an opinionated UI baseline to prevent AI-generated interface slop"*). Two modes: `/baseline-ui` (apply constraints to the conversation) and `/baseline-ui <file>` (review a file → violations [quote the exact snippet] + why-it-matters + concrete fix). The constraint list is genuinely well-crafted, with real thresholds:

- **Stack** — Tailwind defaults; `motion/react` for JS animation; `tw-animate-css` for micro-animations; `cn` (`clsx` + `tailwind-merge`).
- **Components** — accessible primitives (`Base UI` / React Aria / Radix); reuse the project's primitives first; never mix primitive systems on one surface; `aria-label` on icon-only buttons; never rebuild keyboard/focus by hand.
- **Interaction** — `AlertDialog` for destructive actions; skeleton loaders; `h-dvh` not `h-screen`; respect `safe-area-inset`; errors next to the action; never block paste.
- **Animation** — never animate unless requested; compositor props only (`transform`/`opacity`); never animate layout props; `ease-out` on entrance; **≤200ms** interaction feedback; pause off-screen loops; respect `prefers-reduced-motion`.
- **Typography** — `text-balance` headings / `text-pretty` body; `tabular-nums` for data; `truncate`/`line-clamp` for dense UI; never touch `tracking-*` unless requested.
- **Layout / Performance / Design** — fixed `z-index` scale; `size-*` for squares; no `blur()`/`backdrop-filter` on large surfaces; no `will-change` outside an active animation; no `useEffect` for render-logic; **no gradients / no purple gradients / no glow-as-affordance**; one accent per view; empty states get one clear next action.

**`fixing-accessibility`** — a priority-ranked a11y punch-list (9 categories: accessible-names → keyboard → focus/dialogs → semantics → forms/errors → announcements → contrast → media/motion → tool-boundaries), with a "quick reference" of critical rules, common before/after fixes, and a **tool-boundaries** rule (*"prefer minimal, targeted fixes… do not refactor unrelated code… do not migrate UI libraries unless requested"*). Same `/skill` + `/skill <file>` review pattern.

These are textbook **anti-slop design skills** — opinionated, thresholded, review-mode-first, minimal-diff, exactly the Pattern #88 (anti-slop-curation) / hallmark v204 / taste-skill v81 shape, authored by someone who lives in this stack (Base UI, `motion/react`, Tailwind — ibelick's wheelhouse).

## Author (verified)

**ibelick = Julien Thibeaut** — a disclosed individual, Paris-based software/design engineer (~10 yr), runs **Interface Office** (a design-engineering studio helping AI startups build products). Notable OSS: **Zola** (open chat interface / OSS ChatGPT alternative), **prompt-kit** (building blocks for AI apps), **motion-primitives** (animated-UI kit). Widely-followed in the React/AI-UI space. **NOT Anthropic** (§41 — no name/heritage/notability/locale rescue; the disclosed-individual (a)-axis is answered NO). First `ibelick` / Julien-Thibeaut author in the corpus (#19 19a). The hallmark v204 (Hassan El Mghari / Together AI) / agent-skills v184 (Addy Osmani) situation — arguably the strongest disclosed *design-engineering* author yet.

## Facts

- License **MIT**; TypeScript 62.3% / Astro 33.1% / JS 3.3% / CSS 1.1% / Shell 0.2%.
- ~**4,700★ / 199 forks / 8 releases / v0.2.3** (2026-06-22) — **page-stated §37.4 → NOT a #52 (viral-velocity) claim** (the GitHub API is mocked in this environment). Trendshift **#20523** (a low ID → an established/known repo, not a fresh burst).
- Deps: astro 5 + @astrojs/cloudflare + @astrojs/react + @base-ui/react + motion + tailwind 4 + tsx + marked. (Base UI + `motion` = ibelick's own toolset.)
- Repo `AGENTS.md` governs the **website's** design conventions + how to maintain `src/data/registry.ts` — it is **not** an agent-harness routing file (no explicit Claude/Cursor/Codex mentions in it; the harness targets are named in the `ui-skills-root` skill instead).

## Corpus placement (hand-verified)

- **Design-skill cluster:** impeccable v75 / taste-skill v81 / huashu-design v82 / open-design v83 / ui-ux-pro-max v85 / hallmark v204 — the Pattern #88 anti-slop family. ui-skills' first-party skills sit squarely here.
- **Agent-skills ecosystem:** agent-skills-standard v76 / CodexKit v121 / karpathy v63 / mattpocock v57 / khazix v138 / agent-skills v184 / marketingskills v202.
- **Pattern #68 Awesome-List-Genre** (CONFIRMED at the v31 mini-audit): awesome-claude-skills v50 (a catalog of agent skills) / awesome-llm-apps v201 (a code-carrying gallery) / awesome-artificial-intelligence v170. ui-skills = a **machine-consumable, CLI-served, categorized** sub-variant of this — an "awesome-list of design-engineering skills + a CLI to fetch them."
- **Domain-Vertical-Skill-Collection** (CONFIRMED ≥6 verticals: SEO v64 / academic v90 / cybersecurity v98 / scientific-publishing v119 / finance v187 / marketing v202) — design-engineering would be a new vertical, but ui-skills is a **registry/router**, not a monolithic single-author install collection (the marketingskills v202 / ai-berkshire v187 shape) → an ADJACENCY, not a clean instance.
- **Cited-to-Subject Elevation:** `ui-skills.com` was already **cited as a design-methodology influence** in the **aidevops v47** wiki (Marcus Quinn's CREDITS.md design-md lineage, alongside Google Stitch DESIGN.md / VoltAgent-awesome-design-md / nothing-design-skill / shadcn/ui). It is now the subject itself — the Kilo Code v177 / v182-audit watched sub-flavor (audit bookkeeping, recorded-not-self-incremented).
- **Corpus-recursive aggregation:** the registry aggregates corpus subjects' skills (pbakaus/**impeccable v75**, **mattpocock v57**, **vercel-labs v51**, anthropics/skills) → the awesome-llm-apps v201 aggregator-mediated cross-ref, **NOT a #57 promotion** (aggregating others' skills ≠ citing an influence on itself).

## Landscape — NOT world-first (verified)

The agent-skills-for-frontend-design space is **crowded and populated**: Anthropic's own official **frontend-design** skill (~402K installs) is the baseline; **shadcn/ui** ships an official skill + an MCP server that searches/installs from registries; **skilld.dev** ("Curated skills for AI agents"), **aiuxplayground.com**, **aihero.dev**, **LazySkills**, **lobehub**, **agentskills.io** (`npx skills add`), **Cursor Directory**, **ClaudeSkills.wiki**, **awesome-claude-code-skills**, and the OpenCode community registry all populate it. The ecosystem grew from ~1 registry (Dec 2025) to ~8 major marketplaces by Q2 2026. ui-skills' distinctive contributions = (1) the **design-engineering vertical** scoping, (2) the **CLI + root-router-skill** progressive-disclosure mechanism, (3) ibelick's authorship/taste. But "a curated skill registry/marketplace + CLI" is not novel → corpus-first for the surface at best, **not a world-first**.

## Bottom line

A well-made, well-curated, well-authored **discovery + fetch layer for design-engineering agent skills**, plus a handful of genuinely high-quality first-party anti-slop UI skills. On-goal (Goal #1 agent-skills substrate + the design-skill cluster) and **directly, immediately pilotable into hireui's frontend** — the baseline-ui review mode is a ready-made, zero-risk anti-slop gate for the Candidate-Detail refactor. NO new pattern; it strengthens Pattern #68 (curated catalog, CLI-served sub-variant) + Pattern #88 (anti-slop design). See the Verdict + Pilot Methods Menu.
