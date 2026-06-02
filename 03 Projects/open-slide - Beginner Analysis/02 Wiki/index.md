# open-slide — wiki (v135)

> **(C) AI-generated wiki page.** Subject: [`1weiho/open-slide`](https://github.com/1weiho/open-slide). Built 2026-06-02 under LLM Wiki Routine v2.6.
> ⚠️ Metadata caveat: this sandbox mocks the GitHub API, so created_at + exact star count are **not API-verified** — figures below are from the repo page / README / releases list and flagged where approximate.

## Identity

| Field | Value |
|---|---|
| Repo | `1weiho/open-slide` |
| Tagline | **"The slide framework built for agents."** |
| Author | **Yiwei Ho** (`1weiho`) — declared **Taiwan** 🇹🇼, solo full-stack TS dev, Raycast ambassador; 1wei.dev, @1weiho |
| Tier | **T2 Service** (agent-native React framework + CLI) with bundled **T1 agent skills** |
| License | MIT |
| Language | TypeScript 95.2% |
| Stars | ≈ 4.4k (303 forks / 8 watchers / 7 open issues) — *unverified* |
| Releases | active multi-package: `@open-slide/core` → v1.8.0, `@open-slide/cli` → v1.2.6 (15–30 May window + older paginated) |
| Verdict | **GOAL-ALIGNED INCLUDE 4/4** — (a) PASS + (b) MODERATE + (c) STRONG + (d) STRONG |

## What it is

A presentation framework **optimized for AI coding agents**: you describe a deck in natural language, your coding agent **writes the React**, and open-slide handles the canvas, scaling, navigation, hot reload, and present mode so the agent focuses on content.

- **Fixed 1920×1080 canvas**; each slide is an arbitrary **React component (no DSL)**.
- **pnpm + Turbo monorepo**: `@open-slide/core` (runtime + Vite plugin + dev/build/preview CLI) · `@open-slide/cli` (scaffolder, `npx @open-slide/cli init`) · `apps/demo`.
- **Shipped agent skills**: `/create-slide` (scaffold a deck end-to-end with scoping questions) · `/slide-authoring` (1920×1080 / typography / color / layout reference) · `/apply-comments` (apply pending `@slide-comment` edits).
- **In-browser inspector** (click-to-comment `@slide-comment` markers) · **present mode** (speaker notes + timer) · **assets manager** (svgl logo search) · **static HTML/PDF export** · deploy-ready (Vercel/Cloudflare Pages).
- **Harness surfaces**: `.claude/skills` (Claude Code) + universal `.agents/skills` + `CLAUDE.md` + `AGENTS.md` (Codex/Cursor). No `GEMINI.md`.

```bash
npx @open-slide/cli init my-slide
cd my-slide
pnpm dev
```

## Why it's in the corpus

- **(a)** Yiwei Ho — declared-Taiwan solo dev = cultural-peer PASS (Asian-LOCATED cluster; firmer than the v89/v90 inferred-Taiwan precedents).
- **(b)** MODERATE — agent-native React-framework tooling (the agent writes real code) in the **presentation domain**. Distinguished from v133 GordenPPTSkill (b)-FAIL: GordenPPTSkill fills templates → `.pptx` binaries (no code); open-slide has the agent write an actual React codebase. Conditional vault utility (Scrum/keynote decks). → GOAL-ALIGNED tier, not OFF-GOAL.
- **(c)** STRONG — clean monorepo + Vite-plugin runtime + CLI scaffolder + 3 shipped skills + inspector/present/export = a good agent-native-framework exemplar.
- **(d)** STRONG — **cited-to-subject elevation** (v91 html-anything borrowed its 1920×1080 canvas convention and logged it "not yet corpus-relevant"; now a subject) + presentation-tooling cluster adjacency (v82/v91/v133) + Pattern #84 multi-harness + Library-vocab #12 routing artifacts.

## Pattern Library contribution (Phase 4b)

- **PRIMARY:** Library-vocab **"Cited-to-Subject Elevation" → N=2** (v93 anthropics/skills anchor + v135) — re-registration on a genuine 2nd instance; promotion-eligible at N=3. *(Sub-flavors: v93 methodology-citation vs v135 dependency-vendoring — one-class-vs-two is a future-audit call.)*
- **SECONDARY (instance notes, not mints):** Pattern #84 84c multi-harness N+1 (modest: Claude + universal AGENTS.md) · Library-vocab #12 routing artifacts N+1 (CLAUDE.md + AGENTS.md + 2 skill dirs) · presentation/slide-tooling-for-agents cluster (v82+v91+v133+v135, **heterogeneous → observation only, NOT minted**) · convention-propagation-between-corpus-subjects (observation) · Pattern #82 quantitative-marketing (mild).
- **State change: NONE.** No top-level pattern, no sub-archetype, no new standalone (§28 new-standalone count = 0). NOT a Pattern #52 promotion (velocity unverified). NOT an agentskills.io 57k implementer.

## §35 / streak

- §35 ceiling **STAYS CLEAR** — window {v133 OG, v134 GA, v135 GA} = 1 OG ≤ 1. No override.
- Streak: **`GA:4 · OG:4 [1 ov]` → `GA:5 · OG:4 [1 ov]`** ("49+3\*" frozen @v125). v135 = 5th GOAL-ALIGNED PASS; consecutive-GA run v134→v135 = 2.

## Pilot note

**CONDITIONAL pilot** — like the design-skill cluster. If Storm Bear has a deck to build in a ~30-day window (sprint report, retrospective, keynote), a reversible trial is cheap: `npx @open-slide/cli init` on a scratch dir, drive `/create-slide` with Claude Code, `pnpm dev`, throw it away after. It is **not** a daily-driver vault tool (presentation domain, not core software-dev), and it does **not** join the operational Claude-Code-adjacent stack. Lower-friction than installing anything into the vault itself (it scaffolds a separate project). The genuinely interesting study angle: how it ships `/create-slide` + `/slide-authoring` + `CLAUDE.md` authoring rules — a clean model to **borrow by hand** when you next author a Claude skill that drives a framework.
