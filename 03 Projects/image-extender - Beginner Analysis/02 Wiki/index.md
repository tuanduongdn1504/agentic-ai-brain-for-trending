# image-extender — wiki (v139)

> **(C) AI-generated wiki page.** Subject: [`boona13/image-extender`](https://github.com/boona13/image-extender). Built 2026-06-02 under LLM Wiki Routine v2.6.
> ⚠️ **Out-of-corpus-scope subject** — built as the **5th lifetime operator OVERRIDE** (STRICT Phase 0.9 = 0/4 SKIP). Recorded as an OFF-GOAL CAPTURE, not laundered into an INCLUDE.
> ⚠️ Metadata caveat (§37): sandbox mocks the GitHub API (it errored outright on the first attempt) — figures are from the repo page + a gh-api mock, **not API-verified**.

## Identity

| Field | Value |
|---|---|
| Repo | `boona13/image-extender` |
| Tagline | **"Seamlessly extend any image in any direction with AI — then build whole 2D game art sets."** |
| Author | **Ibrahim Boona** (`boona13`) — inferred North-African/Middle-Eastern, **undeclared** location (also built `mykonos-island-voxels` ~784★) |
| Tier | **T5 Application** (standalone creative-tech web app) — **out-of-corpus-scope** |
| License | MIT |
| Language | TypeScript 99% (Next.js 14 + React 18 + Tailwind) |
| Stars | ≈ **586** (repo page) / mock 597 / ~63–65 forks / 5 commits / no releases — *stated, NOT API-verified* (§37.4) |
| Created | ~**2026-05-26** (~1 week) — *NOT API-verified*; ~84★/day if accurate, **no #52 claim** |
| Verdict | **STRICT 0/4 SKIP → operator OVERRIDE** ((a) FAIL + (b) FAIL + (c) WEAK + (d) WEAK/FAIL) |

## What it is

A standalone web app for **AI image outpainting + 2D game-art generation**, powered by **Google Gemini via OpenRouter** (BYOK). Five studios:

1. **Extender** — outpaint images in any direction, best-of-3 seam-quality selection.
2. **Parallax Studio** — multi-layer game backgrounds (Sky/Far/Mid/Near).
3. **Tile Studio** — 13-tile autotile sets for 2D platformers.
4. **Sprite Studio** — character animation sheets (5 body plans).
5. **Props Studio** — transparent decoration-sprite library.

Pipeline: expand canvas → call Gemini for outpainting → pre-correct color drift → **Poisson-blend** (gradient-domain) to hide the seam → generate 3 candidates sorted by seam quality. Props use a two-call **"art-director → painter"** pattern; sprites get deterministic post-processing. `npm install && npm run dev` → localhost:3000; ~$0.03 per extension.

```bash
git clone https://github.com/boona13/image-extender.git && cd image-extender && npm install && npm run dev
```

## Why it's out of scope (and here anyway)

Goal #1 = "Master Claude and autonomous agents for software development." image-extender has **no Claude, Claude Code, MCP, Anthropic, agentskills.io, or agent-framework surface** — Gemini is used purely as an image API. It is a genuinely well-built creative-tech tool in an **orthogonal domain**.

- **(a) FAIL** — Ibrahim Boona, inferred North-African/ME (undeclared); not a registered cultural-peer axis, no (a)-rescue, no new axis minted (v97→v115 anti-pattern).
- **(b) FAIL** — image-outpainting / 2D-game-art app, off goal #1.
- **(c) WEAK** — excellent Poisson-blend + art-director→painter engineering, orthogonal field.
- **(d) WEAK/FAIL** — no agentskills.io chain / Claude adjacency; only thin OpenRouter-multi-model + creative-tech-cluster (v84/v116) threads.

→ **operator OVERRIDE** (elected, eyes-open) = **5th lifetime** (v84 image-blaster + v116 Sana + v122 dograh + v127 developer-portfolios + v139).

## Pattern Library contribution (Phase 4b)

- **NONE minted.** NO Pattern Library state change (46 confirmed / 8 Library-vocab CONFIRMED). **ZERO new Library-vocab (§28; registry NOT moved).** NO sub-archetype, NO top-level pattern. Off-goal captures are corpus-knowledge, not pattern-fuel.
- **Observations only:** creative-tech/image-gen-via-override cluster (**v84 + v116 + v139 = 3 of 5 lifetime overrides are creative-tech/image** — the audit-relevant meta-signal) · OpenRouter multi-model BYOK (Pattern #18/#8 adjacency, thin) · art-director→painter two-call orchestration · Pattern #82 quantitative-marketing (mild) · Pattern #66 BYOK-localStorage (thin).

## §35 / streak / override

- **§35 STAYS CLEAR** — window {v137 GA, v138 GA, v139 OG} = 1 OG ≤ 1 (v137/v138 GA buffer absorbs it). ⚠️ a 2nd off-goal at v140 re-breaches → **v140 should be GOAL-ALIGNED**.
- ⚠️ **Override-frequency RE-TRIPS: 3-in-20 (v122+v127+v139) + 3-in-30** → **next audit re-mandated** (systematic-miss review, already overdue ~v139–v140).
- **Streak:** `GA:8 · OG:4 [1 ov]` → **`GA:8 · OG:5 [2 ov]`** ("49+3\*" frozen @v125). GA unchanged (the v131→v138 8-ship goal-aligned run is **broken** here); OG +1; forward override subset [1 ov]→[2 ov].

## Pilot note

**NOT a pilot.** Creative-tech/game-art domain, orthogonal to Scrum/software-dev — corpus-knowledge-of-an-outlier (joins v84/v116/v122/v127). If you ever need 2D game art it's a nice BYOK tool, but it does not advance goal #1 and does not join any vault stack. The directly-useful goal-#1 moves remain the still-un-piloted **v137 book-to-skill** + **v138 neat-freak**.
