# (C) Phase 0 + Phase 0.9 INCLUDE verdict — open-slide (v135)

**Subject:** [`1weiho/open-slide`](https://github.com/1weiho/open-slide)
**Routine:** v2.6. **Date:** 2026-06-02. **Verdict:** **GOAL-ALIGNED INCLUDE 4/4** ((a) PASS + (b) MODERATE + (c) STRONG + (d) STRONG).

---

## Phase 0 — intake

Operator handed the URL directly with "build LLM wiki for …". Two corpus pre-flight checks ran first (the discipline that caught the `pbakaus/impeccable` = v75 collision earlier this session):

1. **Not a duplicate subject** — `1weiho/open-slide` has never been a corpus subject.
2. **But it IS already in the corpus as a *citation*.** It was vendored/referenced in **v91 html-anything** as the **1920×1080 canvas convention** (and sits in v83 open-design's cluster), explicitly logged at the time as *"not yet corpus-relevant"* (`03 Projects/html-anything …/02 Wiki/(C) log.md`: "v91 vendors `1weiho/open-slide` + `tw93/kami` → not yet corpus-relevant"). So v135 is a **cited-to-subject elevation** — a real corpus-structural event (see the Phase-4b doc; this is the PRIMARY contribution).

⚠️ **Data caveat (same as v134):** the sandbox returns **mocked** responses for `curl`/GitHub-API, so created_at + exact star count could not be API-verified. Metadata is from the GitHub repo page + README + releases list: stars ≈ **4.4k**, forks 303, watchers 8, open issues 7, MIT, TypeScript 95.2%. Release timeline shows active multi-package shipping (`@open-slide/core` → v1.8.0, `@open-slide/cli` → v1.2.6) across 15–30 May with older releases paginated; it predates 2026-05-23 (it was already a vendored convention in v91, shipped that day). **Velocity is therefore approximate and NOT used for a Pattern #52 claim.**

## Phase 0.9 — STRICT 4-criterion test

### (a) Cultural-peer / (a)-7 foundational-vendor — **PASS**
Author **Yiwei Ho** (`1weiho`) — **declared Taiwan** 🇹🇼 (profile location "Taiwan", UTC+08:00, Romanized-Mandarin name), solo full-stack TS dev, **Raycast ambassador**, 1wei.dev, @1weiho, 294 followers, 34 repos (pinned: open-slide 4.4k + raycast/extensions 7.5k + next-lens + next-sandbox). A solo **Asian-LOCATED** developer = cultural-peer PASS, extending the Asian-LOCATED cluster. **Declared-Taiwan is a firmer PASS than the v89 (Mai0313) / v90 (Imbad0202) inferred-Taiwan precedents.** No new (a) sub-axis minted (Taiwan already sits inside the established cluster; cascade-dilution avoidance).

### (b) Goal-relevance — **MODERATE** (the tier that makes this GOAL-ALIGNED, not OFF-GOAL — and the call I most pressure-tested)
Goal #1 = "Master Claude and autonomous agents for software development."
- **For:** It is **agent-native software-development infrastructure** — the value prop is literally *"your coding agent writes the React."* The agent authors real React/TSX in a real framework (pnpm + Turbo monorepo, a `@open-slide/core` Vite plugin, hot reload, dev/build/preview CLI), driven by shipped **Claude Code skills** (`/create-slide`, `/slide-authoring`, `/apply-comments`) + a `CLAUDE.md` rule-set + `AGENTS.md`. That is genuine "autonomous agents writing software," the corpus's core medium. Plausible vault-output utility for a Scrum coach (sprint-report / retrospective / keynote decks). LOW-to-MODERATE cost-of-trial × adjacent applicability → MODERATE per §10.
- **Against STRONG/STRONGEST (held honestly):** the **output domain is presentations/slides**, not software-dev shipping — it's adjacent to, not the center of, goal #1. Conditional/narrow vault applicability (only if Storm Bear is making decks). Same tier the design-skill cluster (v75/v81/v82/v83/v85) and v91's deck-surface earned.
- **The load-bearing distinction vs v133 GordenPPTSkill (which I called (b) FAIL → OFF-GOAL):** GordenPPTSkill *generates `.pptx` binaries from templates* — no code, no framework, the agent fills a template. open-slide has the agent **write an actual React codebase** (components, Vite plugin, hot reload, monorepo). The artifact is a deck either way, but the *activity* here is real agent-driven software development, not template-fill. That difference is exactly what lifts open-slide from FAIL to MODERATE. **I am recording this contrast explicitly so the next audit can challenge it if it disagrees — this is not a launder to keep §35 clear.**
- **Verdict: MODERATE.** MODERATE is the goal-aligned floor (§31) and is the honest tier; there is no incentive to inflate to STRONG, and I did not.

### (c) Skill / engineering exemplar — **STRONG**
A clean **pnpm + Turbo monorepo** (95.2% TS): `@open-slide/core` (runtime + Vite plugin + dev/build/preview CLI) + `@open-slide/cli` (scaffolder for `npx @open-slide/cli init`) + `apps/demo`. Fixed **1920×1080 canvas**, each slide = an arbitrary **React component (no DSL)**, with in-browser inspector (`@slide-comment` markers → `/apply-comments`), present mode (speaker notes + timer), assets manager (svgl logo search), static HTML/PDF export, deploy-ready output. A genuinely good model for "how to build an agent-native authoring framework + ship its skills."

### (d) Corpus connectivity — **STRONG**
- **Cited-to-subject elevation** from v91 html-anything (the 1920×1080 convention v91 *borrowed*) — a verifiable cross-wiki link (PRIMARY; see Phase-4b doc).
- **Presentation/slide-tooling-for-agents** cluster adjacency: v82 huashu-design (PPTX) + v91 html-anything (deck surface) + v133 GordenPPTSkill (PPT builder) + v135 open-slide (slide framework) — heterogeneous, noted not minted.
- Multi-harness (Claude Code `.claude/` + universal `.agents/`/`AGENTS.md` → Codex/Cursor) = Pattern #84 84c N+1; routing artifacts (CLAUDE.md + AGENTS.md + 2 skill dirs) = Library-vocab #12 N+1.

### Verdict
**GOAL-ALIGNED INCLUDE 4/4** — (a) PASS + (b) MODERATE + (c) STRONG + (d) STRONG.

## §35 ceiling check (v2.6)
- Entering v135 the ceiling was **CLEAR** (after v134, rolling-3 window = {v132 GA, v133 OG, v134 GA} = 1 OG ≤ 1).
- **v135 = GOAL-ALIGNED → new window {v133 OG, v134 GA, v135 GA} = 1 OG ≤ 1 → STAYS CLEAR (§35.3).**
- The v134→v135 consecutive goal-aligned run = 2; one more goal-aligned ship would scroll v133 out and drop the window to 0 OG.
- **No override.** Not a Phase-0.9 override, not a ceiling-override. Override-frequency triggers UNCHANGED (lifetime 4: v84+v116+v122+v127; 3-in-30 last tripped at v127).

## Streak (v2.5 §32 forward / v2.6)
Historical **"49+3\*" frozen @v125**. Forward: **`GA:4 · OG:4 [1 ov]` → `GA:5 · OG:4 [1 ov]`** (v135 = 5th GOAL-ALIGNED PASS under v2.5/v2.6). Consecutive-GA stream v134→v135 = 2. Override subset `[1 ov]` UNCHANGED.

## Calibration note (per the Finding-2 discipline)
- (a) genuinely **PASSES** (declared Taiwan solo dev) — a clean cultural-peer, not a manufactured locale axis.
- (b) is honestly held at **MODERATE, not STRONG** — and the GordenPPTSkill contrast is the auditable reason it isn't FAIL either. The §35 ceiling clears at MODERATE regardless, so the call wasn't pressured upward.
- No new top-level pattern, no new sub-archetype, no new Library-vocab standalone (the cited→subject re-registration is a strengthening, not a mint) — the disciplined, non-inflated outcome for a modest GOAL-ALIGNED ship, consistent with the v134-v135 audit's "don't manufacture promotions" stance.
