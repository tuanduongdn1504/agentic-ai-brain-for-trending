# (C) systemdesign42/system-design-academy — Phase 0 + Phase 0.9 STRICT verdict (v147)

**Subject:** `systemdesign42/system-design-academy` — https://github.com/systemdesign42/system-design-academy
**Date:** 2026-06-03 · **Routine:** v2.6 (§31 + §35 + §37)
**Verdict:** **GOAL-ALIGNED INCLUDE (borderline) — (a) FAIL · (b) MODERATE [low/borderline, flagged for audit challenge] · (c) WEAK-MODERATE · (d) MODERATE.**

---

## Phase 0 — scope gate
Borderline-in-scope as a **T3 Education** resource. A curated system-design educational index/newsletter that *includes* a substantive **AI Engineering** section (LLMs, RAG, **agents, multi-agent systems**). The agent/AI-systems content + the load-bearing relevance of system-design to building production agent systems puts it in scope as goal-aligned-borderline; the system-design-interview-prep core is off the agent-mastery center.

## Phase 0.9 STRICT — four axes

### (a) Cultural-peer / geographic — **FAIL**
- Owner `systemdesign42` — runs a popular system-design newsletter; **no identity/location disclosed** in-repo (confidence: none). Not an establishable cultural-peer, not (a)-7. No rescue, no axis minted.

### (b) Goal-relevance — **MODERATE (low/borderline)** — load-bearing, and honestly flagged
- **Why MODERATE-not-WEAK:** the subject explicitly covers **AI Engineering — LLMs, RAG, agents, multi-agent systems** as a named section (not me stretching — it's in the content), AND **system design is genuinely load-bearing for goal #1** ("autonomous agents *for software development*" at production scale needs distributed-systems / RAG-architecture / multi-agent-orchestration knowledge). For a Scrum coach/dev mastering agents, the AI-engineering + system-design-for-AI material directly serves the goal.
- **Why MODERATE-not-STRONG:** the subject's center of gravity is **system-design interview prep + architecture case studies** (Amazon/Netflix/Uber/Discord) — general SWE, not agent-mastery. The agent content is a **minority section** of a broad content index, and it's **educational links/case studies, NOT tooling** (no SKILL.md / `.claude/` / MCP / agent framework). This is meaningfully weaker on (b) than the agent-*focused* T3 subjects (v111 hello-agents, v113 ai-engineering-from-scratch, both STRONG).
- **⚠️ Recorded for audit challenge:** this is a genuine borderline call made while §35 was breached (creating an incentive to inflate). I held it at MODERATE on a principled line (substantive agent section + system-design load-bearing), NOT to satisfy §35 — and I flag it so the next audit can overturn it to WEAK/off-goal if it disagrees. (Same discipline as the v135 open-slide / v138 khazix (b)-MODERATE calls.)

### (c) Instructive engineering — **WEAK-MODERATE**
A well-curated educational *resource* (case studies + distributed-systems fundamentals + AI-engineering + white papers), but it's a **Markdown reference index / newsletter funnel, not code**. Instructive as a learning map; not instructive engineering.

### (d) Corpus connectivity — **MODERATE**
T3 Education sibling (v74 LLMs-from-scratch / v77 easy-vibe / v111 hello-agents / v113 ai-engineering-from-scratch); the AI-Engineering/multi-agent section connects to the agent-learning thread. Pattern #45 (CC BY-NC-ND restrictive license) + Pattern #82/#19-adjacent newsletter funnel.

---

## §35 — Soft Off-Goal-Rate Ceiling — SATISFIED, NOT FULLY CLEARED
- §35 was **BREACHED** after v146 (first ship-breach). §35.2 mandated **v147 be GOAL-ALIGNED** — **a goal-aligned (borderline-MODERATE) v147 SATISFIES that mandate** (NOT a 2nd ceiling-override).
- Rolling-3-ship window after v147 = **{v145 OG, v146 OG, v147 GA} = 2 OG → STILL BREACHED.** The ceiling **fully clears only when v148 is ALSO goal-aligned** (window would then be {v146 OG, v147 GA, v148 GA} = 1 OG ≤ 1). So **v148 must also be GOAL-ALIGNED.**

## Override accounting
v147 is NOT an override (it's a goal-aligned INCLUDE). Override-frequency triggers UNCHANGED (lifetime 8; 5-in-20). The §35 ceiling-override count is unchanged (v146 was the first and only `[ceiling-override]`).

## §37 — Fact-provenance
≈**25.3k★** / 3.2k forks / CC BY-NC-ND 4.0 / Markdown index (as of 2026-06, repo page — **stated, NOT API-verified §37.4**; env mocks the GitHub API). Velocity/age not established → **NOT a Pattern #52 claim**. Owner identity undisclosed.

## Streak (v2.6 §32)
GA:12 · OG:8 [5 ov] → **GA:13 · OG:8 [5 ov]** (v147 = 13th goal-aligned PASS; "49+3\*" frozen @v125). The `[ceiling-override]` flag is v146's only; v147 carries none.

## Honest non-claims
- (a) genuinely FAILS (undisclosed owner, not a cultural-peer, not (a)-7).
- (b) is **MODERATE not STRONG**, and a **borderline** MODERATE — flagged for audit to overturn to WEAK/off-goal if warranted. I did NOT inflate it to clear §35 (it doesn't even fully clear §35 — that needs v148).
- It's an **educational content-index/newsletter funnel, NOT tooling** — no SKILL.md/.claude/MCP.
- NOT a #52 claim. Phase 4b mints NOTHING (0 new standalones) — a borderline education resource, not a novel mechanism (the v124 "0 new standalones" discipline). NO Pattern Library state change.
