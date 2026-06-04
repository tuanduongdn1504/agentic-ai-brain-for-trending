# (C) Expensify/App — "New Expensify" (v152 wiki)

> **Status: OFF-GOAL CAPTURE** (STRICT Phase 0.9 = 0/4 → 10th operator override → `[ceiling-override]`, §35 re-breached). Corpus-knowledge of an out-of-scope subject, captured at explicit operator election. **Not a pilot.** See `01 Analysis/` for the verdict + Pattern-Library Phase 4b.

**Repo:** https://github.com/Expensify/App · **Owner:** Expensify, Inc. (US) · **License:** MIT
**Tagline:** *"Welcome to New Expensify: a complete re-imagination of financial collaboration, centered around chat."*

## What it is
The open-source codebase for **New Expensify** — Expensify's modern expense-management and financial-collaboration app, built around chat. One of the most-watched real-world examples of a **large-scale production React Native monorepo**: a `npm install` → `npm run web/ios/android` cross-platform app spanning web + iOS + Android from one TypeScript codebase.

It is **off goal #1** ("master Claude and autonomous agents for software development"): the product is finance/expense/chat. It is included as **corpus-knowledge via operator override**, with one genuinely interesting secondary thread (the internal Claude-Code adoption, below) recorded as an observation — not as goal-relevance.

## Architecture (the orthogonal-domain reference value)
- **HybridApp** — merges **NewDot** (the modern app) with **OldDot** (legacy mobile, via the `Mobile-Expensify` git submodule). Entry points span `src/App.tsx`, `src/Expensify.tsx`, `src/HybridAppHandler.tsx`; mobile builds must be initiated from `Mobile-Expensify`.
- **Onyx** (React Native Onyx) — offline-first **optimistic-update** state layer: queue-based requests, conflict resolution, offline by design.
- **React Compiler** (`babel-plugin-react-compiler`) — transparent auto-memoization of components/callbacks in the build pipeline.
- **Strict TypeScript discipline** — ESLint with an `eslint-seatbelt` grandfathered-violations mechanism; dual typecheck paths (`npm run typecheck-tsgo` fast/dev vs `npm run typecheck` tsc/CI gate); Prettier + lint mandatory pre-commit; CI rejects unformatted code.
- **Stack:** TypeScript 98.6%, React Navigation, Airship push, Mapbox, native Obj-C/Kotlin modules.

## The internal Claude-Code stack (observation — engineering exhaust, NOT the product)
This is the **richest internal Claude-Code adoption in the corpus to date**, and the only goal-#1-adjacent thing here worth *reading*:
- A **317-line `CLAUDE.md`** — a full operating manual for AI agents on the repo (architecture, build/test commands, coding standards, a **mandatory post-edit checklist**: *"ALWAYS run these steps after making code changes, before committing"* — Prettier → eslint → `typecheck-tsgo` → React-Compiler compliance).
- **`AGENTS.md`** — a one-line redirect: *"All repository guidelines and instructions have been consolidated into CLAUDE.md."*
- **`.mcp.json`** — MCP configuration (Pattern #18 B1).
- **Four named Claude-Code skills:**
  - `/agent-device` — drive the app on iOS/Android simulators or real devices for interactive testing, performance profiling, debugging.
  - `/playwright-app-testing` — browser-based testing/debugging after frontend changes.
  - `/react-native-best-practices` — FPS, FlashList, memoization, bundle size, startup, native modules, memory.
  - `/Sentry` — analyze crash data, spans, metrics.

By the **v122 discipline**, this is how the team *builds* the app, not what the app *is* — so it does not make Expensify a goal-#1 subject. But as a worked example of **operating Claude Code on a giant production RN monorepo**, the public `CLAUDE.md` + `/agent-device` skill are a legitimate *read* (not an install). It extends the corpus's "Claude-Code-as-internal-dev-exhaust" observation thread to N=4 (v122 + v128 + v142 + v152), v152 being the richest instance.

## Provenance (§37)
≈**4.9k★** / 3.9k forks / **263,873 commits** / **2,640 releases** / MIT / TypeScript 98.6%.
*Page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified (§37.4)**; this environment mocks the GitHub API.* Low stars vs an enormous commit count (commits ≫ stars, same shape as v151 hongbomiao) → **NOT a Pattern #52 claim.**

## Why it's here / why it's off-goal
- **Off goal #1:** the product is expense management + financial chat. Cataloguing or using Claude Code internally ≠ being agent tooling.
- **(a) FAIL:** Expensify is a US corporation — not a cultural-peer, not (a)-7 → no (a)-rescue → captured only via the **10th lifetime operator override**.
- **§35 RE-BREACHED:** window {v150 GA, v151 OG, v152 OG} = 2 OG → **v153 must be GOAL-ALIGNED.**
- **NO Pattern Library state change; ZERO mint** — off-goal = corpus-knowledge, not pattern-fuel.

## Not a pilot
A finance product, not a goal-#1 tool. The directly-useful, still-un-piloted goal-#1 subjects remain **v150 Paseo**, **v149 Scrapling**, and **v144 headroom**.
