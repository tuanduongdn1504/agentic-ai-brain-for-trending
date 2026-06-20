# (C) Phase-0.9 verdict — v173 claude-tap — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `liaohch3/claude-tap` — *"a local proxy and trace viewer for AI coding agents."*
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG. Tier: T2 Service.**
**Tier key (routine v2.5 §31):** the tier keys on **(b)** goal-relevance. (b) STRONG (MODERATE+) → **GOAL-ALIGNED INCLUDE**, regardless of the (a) FAIL.

---

## (a) FAIL — author cultural-peer axis

"liaohch3" is a **bare GitHub handle** with no disclosed individual identity, affiliation, or location. Not Anthropic (the only major-vendor carve-out, (a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only). The 9 contributor handles + the 8-language i18n hint at an East-Asian/Chinese-language origin, but a **name/heritage inference is NOT an (a)-rescue** (the v159→v172 discipline; held across v169/v170/v171/v172). **(a) FAILs cleanly; no rescue, no axis minted** — consistent with v168 ponytail (bare handle) and v172 DeusData (bare org).

## (b) STRONG — goal-relevance (the deciding axis)

Goal #1 = *"master Claude and autonomous agents for software development."*

claude-tap is the instrument for **seeing exactly how a coding agent works at the API/protocol level** — its real system prompt, its tool schemas, how context is assembled turn-over-turn, and its token/cost footprint. It is:

- **Claude-Code-first** (the default client).
- the **live-capture mechanism** behind the corpus's static prompt collections (v65 claude-code-system-prompts / system-prompts-leaks) — and exactly what its sibling project Phistory uses it for.
- directly on the **claude-api-cost-optimization** thread (token-usage breakdown: input/output/cache).
- directly on the **CC-memory-systems / understanding-agent-internals** thread (how context is built).
- **directly pilotable into the vault** (run the vault's own Claude Code through it).

Held at **STRONG (not STRONGEST):** third-party (not the vault's own work / not Anthropic substrate) and an **inspection/observational augmentation** — it lets you *understand* the agent, it doesn't make the agent more capable. STRONGEST is reserved for Anthropic core substrate or the agent itself.

## (c) STRONG — engineered substance

Python proxy + JS/HTML/CSS viewer; **dual reverse/forward proxy modes**; low-overhead SSE/WebSocket relay; auth-header redaction; **structural request diffing** with character-level highlighting; full-text search; token accounting; tool-schema inspector; HTML + JSON export; i18n (8 langs); **14 supported clients**; `pip`/`uv` install; **100+ releases** to v0.1.120; ~1.9k★/196 forks; 9 contributors. Not a prototype.

## (d) STRONG — pattern home

A clean **§C capability standalone** (CORPUS-FIRST, N=1 — "Agent Protocol Inspector") with an unambiguous home and a clear adjacency map (observability family / headroom v144 / relays v112-v117 / lazyagent v165). Nothing is forced. See `(C) PRIMARY — agent-protocol-inspector standalone N1.md`.

---

## Tier-tag (routine v2.5 §31)

**GOAL-ALIGNED INCLUDE.** (b) STRONG → the corpus's core. Counts toward the goal-aligned PASS streak: **GA:34 → GA:35.** §35 rolling-3-ship window {v171 GA, v172 GA, **v173 GA**} = 0 OG → CLEAR. **20 consecutive goal-aligned ships v153→v173.**

⚠️ **v169 cascade guard:** the v169 SkillSpector ship logged a shared-premise error ("(a) FAIL ⟹ OFF-GOAL") across its synthesis + verifiers + critic. That conflation is wrong — §31 keys the tier on **(b) only**, and v168 ponytail shipped GOAL-ALIGNED with exactly (a) FAIL · (b) STRONG. The v173 verification gave each of 3 lenses a distinct question precisely so they could not share that premise; the critic's `cascade_check` = "CASCADE RISK = ZERO."

## Verification

Verdict produced **inline**, then **adversarially verified by a 3-lens + critic workflow**:
- **Lens 1 (goal-relevance/tier):** CONFIRM — (b) STRONG, (a) FAIL, GOAL-ALIGNED correct, v169 cascade avoided.
- **Lens 2 (capability novelty/placement):** CONFIRM — genuinely novel; distinct from observability (no N-bump), headroom, relays, lazyagent; suggested the rename.
- **Lens 3 (secondary/non-claims):** CONFIRM — #84 84c scoped (not ponytail mechanism), NOT #18/#52/#57, #66 cross-ref.
- **Critic (anti-inflation):** `overall: AMEND` on ONE point — rename the §C standalone to lead with the protocol-layer distinction (incorporated). `inflation_check` = discipline HELD (mint warranted, N=1 correct, counts 46/10 unchanged, no double-count). `cascade_check` = ZERO.
