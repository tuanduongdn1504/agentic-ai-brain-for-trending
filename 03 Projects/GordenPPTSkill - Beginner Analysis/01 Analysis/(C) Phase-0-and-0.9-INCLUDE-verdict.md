# (C) GordenPPTSkill — Phase 0 + Phase 0.9 verdict (v133)

**Subject:** `GordenSun/GordenPPTSkill` — an agentskills.io PPT-builder skill.
**Date:** 2026-06-01. **Routine:** v2.6. **Verdict:** **WEAK INCLUDE → OFF-GOAL CAPTURE via (a)-rescue** (v2.5 §31). Built at explicit operator election ("build it anyway", after being flagged off-goal).

---

## Phase 0 — scope / decision gate

A Claude/AI **`SKILL.md` skill** (agentskills.io standard) → in the corpus's *skill* domain by format. But its *purpose* is **PowerPoint-deck generation** — a content/design-productivity vertical, not software development / autonomous agents. Flagged off-goal at intake; operator elected to build it anyway. Proceed to Phase 0.9 with the off-goal flag.

**Metadata (verified, gh API + raw SKILL.md/INDEX 2026-06-01):** 1,311★ / 120 forks / created 2026-05-27 / pushed 2026-06-01 (**~5 days**) → ~262★/day (sharp nascent pulse, far too young to confirm Pattern #52). License "Other" / non-commercial ("禁止任何商业用途"). Python (scripts) + 19 PPTX template binaries. `SKILL.md` name `gorden-ppt-skill`. Author **Gorden Sun** (@Gorden_Sun; location undeclared; account 2013, 56 repos) — inferred China-Mainland.

---

## Phase 0.9 — STRICT INCLUDE/SKIP (4 criteria)

### (a) cultural-peer / (a)-7 — **PASS (inferred China-Mainland)**
Chinese-primary README, 19 China-scenario templates (incl. 党政红 patriotic-education, 思政课件 ideological courseware, 述职竞聘 job-defense), Chinese author name. Inference-tolerant (§8). China-cluster N+1 (v82/v94/v100/v117/v123/v128/v129 + v133). This is the criterion the include rests on — the (a)-rescue channel.

### (b) goal-relevance — **FAIL**
Goal #1 = "Master Claude and autonomous agents for software development." GordenPPTSkill **generates presentations.** It has zero software-development / agent-building / vault utility. Being a *Claude skill* is a format/connectivity fact (d), not goal-relevance; being a *well-structured* skill is an exemplar fact (c), not goal-relevance. The subject's *purpose* is off goal #1 → **(b) FAILs.** (Same shape as the design-skill cluster's weak-(b) members — v75/v81/v82/v83/v85/v105 — now made explicit under v2.5's strict (b) test.)

### (c) instructive-exemplar — **MODERATE**
A competently-built agentskills.io skill: clean `SKILL.md` + 5 references (workflow, pptx-edit-schema, chart-editing, custom-template-workflow, original-design-guide) + 6 scripts (build_pptx, apply_update, check_update, build_manifest, compute_capacity, render_slides) + manifest.json + per-template {detail.json, intro.md, preview.png}. Genuinely interesting mechanics: non-destructive text-only editing, text-box **capacity/overflow detection**, same-level-title **font-size consistency** checks, and a **self-update-on-first-use** step. A mild skill-structure exemplar — but the domain (PPT-gen) is off corpus-core, so MODERATE not STRONG.

### (d) corpus-connectivity — **MODERATE–STRONG**
agentskills.io 57k chain implementer + **design/content-skill cluster** adjacency (esp. v82 huashu-design's PPTX export + v105 guizang social-card design-skill) + `NOTICE.md` attribution (cf. v75 impeccable) + Pattern #45 non-commercial-license sub-typology + China-Mainland cluster.

---

## Verdict

| Criterion | Call | Note |
|---|---|---|
| (a) cultural-peer / (a)-7 | **PASS** | inferred China-Mainland; the (a)-rescue channel |
| (b) goal-relevance | **FAIL** | PPT-deck generator; off goal #1 (not software-dev/agents) |
| (c) instructive | **MODERATE** | competent skill-structure exemplar; off-core domain |
| (d) connectivity | **MODERATE–STRONG** | agentskills.io chain + design-skill cluster + NOTICE.md + #45 |

**→ WEAK INCLUDE → OFF-GOAL CAPTURE via the (a)-rescue channel** (v2.5 §31: (b) FAILs → NOT goal-aligned; (a) PASSes → captured via (a)-rescue, NOT an override). **The 5th (a)-rescue off-goal capture** (v80 + v123 + v128 + v129 + v133).

---

## §35 soft off-goal-rate ceiling — analysis (STAYS CLEAR)

- **Entering this ship the ceiling was CLEAR** (v132 cleared it; window after v132 = {v129 OG, v131 GA, v132 GA} = 1 OG).
- **v133 = OFF-GOAL CAPTURE** → new rolling-3-ship window = {v131 GA, v132 GA, **v133 OG**} = **1 OG ≤ 1 → STILL CLEAR** (does NOT breach — the two prior goal-aligned ships buffer this single off-goal capture). So there is no §35 violation and no `[ceiling-override]` needed.
- **But** — honestly: this **resumes off-goal intake** after the v131/v132 goal-aligned run. (a)-rescue off-goal capture is now **N=5**; the v2.5 off-goal-capture rate across all 7 v2.5/v2.6 ships is now **4-of-7** (OG: v127/v128/v129/v133; GA: v126/v131/v132). One more off-goal ship next would **re-breach** the ceiling (window would become {v132 GA, v133 OG, v134 OG} = 2 OG) — so v134, if it ships, should be goal-aligned to stay clear.
- **Override-frequency triggers:** UNCHANGED (v133 is not an override; (a)-rescue clears the gate on (a)).

## Streak (v2.5 §32 forward / carried under v2.6)

Historical **"49+3\*" FROZEN @v125**. Forward: **`GA:3 · OG:3 [1 ov]` → `GA:3 · OG:4 [1 ov]`** — v133 = the **4th OFF-GOAL CAPTURE** under v2.5/v2.6 (via (a)-rescue, not an override → OG +1, `[1 ov]` UNCHANGED, no trigger trip). The 2-ship consecutive-GA stream (v131→v132) is broken.

## Honest summary

A clean, real agentskills.io skill — but a PowerPoint-deck generator, which is **off goal #1**. I tagged it honestly as an OFF-GOAL CAPTURE (b-FAIL) entering via (a)-rescue, the 5th such, rather than laundering the "it's a Claude skill" connectivity into goal-relevance. Built at the operator's explicit election after the off-goal nature + un-piloted goal-aligned backlog were surfaced. The ceiling stays clear (the v131/v132 buffer), but the off-goal-capture rate (4-of-7 under v2.5) and (a)-rescue N=5 are the live signals — exactly what the v125/v130 audits flagged. No pattern/Library-vocab minted (off-goal captures aren't pattern-fuel).
