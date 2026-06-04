# (C) Expensify/App ("New Expensify") — Phase 0 + Phase 0.9 STRICT verdict (v152)

**Subject:** `Expensify/App` — https://github.com/Expensify/App
**Date:** 2026-06-04 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **STRICT Phase 0.9 = 0/4 → SKIP → 10th lifetime operator OVERRIDE → OFF-GOAL CAPTURE via the override channel** — (a) FAIL · (b) FAIL · (c) WEAK/MODERATE · (d) WEAK/MODERATE. **Built at explicit operator election** (AskUserQuestion → "Ship as OFF-GOAL via override") after the 0/4 verdict + §35 re-breach were put on the record. **Not laundered.**

---

## Phase 0 — scope gate
**Off-goal.** New Expensify = *"a complete re-imagination of financial collaboration, centered around chat"* — Expensify Inc.'s open-source **expense-management + financial-collaboration super-app**. The *subject* is a finance/expense/chat product. Goal #1 is "master Claude and autonomous agents for software development" — this is not an agent/Claude *product*.

The complication (and it's a real one): the repo carries a **substantial internal Claude-Code stack** — a **317-line `CLAUDE.md`** operating manual, an `AGENTS.md` that redirects to it, a `.mcp.json` (MCP), and **four named Claude-Code skills**: `/agent-device` (drive iOS/Android simulators/real devices for interactive testing, profiling, debugging), `/playwright-app-testing` (browser testing after frontend changes), `/react-native-best-practices` (FPS/FlashList/memoization/bundle/startup guidance), `/Sentry` (crash/span/metric analysis). This is the **richest** internal-Claude-Code adoption seen in the corpus to date.

But per the **v122 dograh discipline** (restated v128 Echo Loop, v142 OrcaSlicer): a `.claude/`/`AGENTS.md`/`CLAUDE.md` presence is the team's **engineering exhaust, not the repo's product**, and does **not** flip an off-goal product to goal-aligned — "a huge fraction of repos now ship a CLAUDE.md; counting that as corpus-relevance would blow scope open." So as a **subject**, this is off-goal, with the internal-tooling thread logged as an observation (the richest member of that N=4 cluster).

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
Owner is **Expensify, Inc.**, a US corporation. Not a cultural-peer; not a Foundational-Vendor-Direct-Source ((a)-7 is for vault-substrate vendors — Anthropic-tier — which Expensify is not). **No (a)-rescue available** → the only intake door for this off-goal subject is an **operator OVERRIDE**. No axis minted from a corporate org (the v139/v142/v145 discipline).

### (b) Goal-relevance — **FAIL** (load-bearing)
The product is finance/expense/chat — off goal #1. The internal Claude-Code stack is real and substantial, but it's how the team *builds* the app, not what the app *is* (the v122 line). Clean FAIL on the subject axis.

- **Defensible (b)-MODERATE reading, declined:** one could treat the subject as "*how a 263k-commit production engineering org operationalizes Claude Code + MCP + a custom device-driving test skill at scale*," which is genuinely studyable for goal #1 — arguably the strongest such public example in the corpus. The v147 system-design-academy precedent held a borderline (b)-MODERATE when agent content was a substantive *section*. **Declined here** because (1) v147's agent content was part of what the subject *offers a reader*, whereas Expensify's agent tooling is its internal *build process* (the v122 distinction), and (2) inflating (b) to clear §35 is exactly the move §35 exists to discourage. Recorded for the audit to challenge; **not** the basis of this ship (operator elected the override, not this reading).

### (c) Instructive engineering — **WEAK/MODERATE**
A famously large, high-quality production React Native monorepo — HybridApp (NewDot + OldDot), Onyx offline-first optimistic state, React Compiler auto-memoization, strict-TS/Prettier/eslint pre-commit discipline. Genuinely instructive *as an RN-at-scale reference*, but orthogonal to goal #1. WEAK→MODERATE.

### (d) Corpus connectivity — **WEAK/MODERATE**
Connects via the **Claude-Code-as-internal-dev-exhaust thread** (v122 dograh + v128 + v142 → **N=4**, v152 the richest) + Pattern #18 **B1 MCP** (`.mcp.json`) + Pattern #84 (multi-skill internal tooling). Not a goal-#1 product cluster. WEAK→MODERATE.

---

## Override / channel call
STRICT 0/4 clear PASS → **SKIP**. (a) FAILs, so there is **no (a)-rescue** door (contrast v151 hongbomiao, which had a registered-heritage (a)-rescue). The subject was captured at **explicit operator election** → **10th lifetime operator OVERRIDE** (v84+v116+v122+v127+v139+v142+v145+v146+v148+v152), **7th forward** under v2.5/v2.6. Same shape as v146 OpenCut / v148 goose (0/4 SKIP overrides that were also `[ceiling-override]`s).

## §35 — Soft Off-Goal-Rate Ceiling — **RE-BREACHED**
- Rolling-3-ship window after v152 = **{v150 GA, v151 OG, v152 OG} = 2 OG > 1 → BREACH.**
- v152 carries the corpus's **3rd logged `[ceiling-override]`** (after v146 first-ever, v148 second).
- **v153 MUST be GOAL-ALIGNED** (§35.2). Full clearance needs **v153 AND v154 both GA** (to scroll both v151 and v152 out of the window).
- ⚠️ **Override-frequency: 7-in-20** (v127+v139+v142+v145+v146+v148+v152) + far past 3-in-30 → next audit **RE-MANDATED** (already overdue; common-cause re-confirmed 5× now — intake-channel off-goal capture, the lever is upstream subject-selection, not a criteria defect).

## §37 — Fact-provenance
≈**4.9k★** / 3.9k forks / **263,873 commits** / **2,640 releases** / MIT / TypeScript 98.6% (+ JS 0.6%, Obj-C, Kotlin) (page-stated as of 2026-06 via WebFetch of the rendered repo — **NOT independently API-verified §37.4**; env mocks the GitHub API). Low stars vs an enormous commit count (commits ≫ stars, same shape as v151 hongbomiao) → **NOT a Pattern #52 claim.** Owner Expensify, Inc. (US).

## Streak (v2.6 §32)
GA:15 · OG:10 [6 ov] → **GA:15 · OG:11 [7 ov]** (OG +1; **GA UNCHANGED** — off-goal does not advance the goal-aligned streak; **override** → override-subset [6 ov]→[7 ov]; **lifetime overrides 9 → 10**; "49+3\*" frozen @v125).

## Pattern Library — NO state change, NO mint (§28)
**ZERO new Library-vocab; registry 06 NOT moved; NO sub-archetype; NO new top-level Pattern** (off-goal = corpus-knowledge not pattern-fuel — the v128/v129/v133/v146/v148 discipline). See `(C) Pattern-Library-Phase-4b.md` for the observations.

## Not a pilot
A finance/expense product. Nothing to install/trial for goal #1. The only goal-#1-adjacent *read* is the public 317-line `CLAUDE.md` as a worked example of operating Claude Code on a giant RN monorepo. The actual goal-#1 pilots remain **v150 Paseo + v149 Scrapling + v144 headroom** (all un-piloted).

## Honest non-claims
- (b) genuinely FAILS — off goal #1; the internal Claude-Code stack does **not** flip it (v122 discipline). Not laundered.
- A (b)-MODERATE GOAL-ALIGNED reading was *defensible* and *declined* — not used to clear §35.
- (a) FAILS — US corporation, no (a)-rescue, no axis minted.
- NOT a #52 claim (low stars vs commits; metrics not API-verified).
- 10th lifetime operator override / 7-in-20 forward; 3rd `[ceiling-override]`; §35 re-breached.
- ZERO mint; NO new pattern/sub-archetype/standalone; NO confirmed-count change (46/9).
