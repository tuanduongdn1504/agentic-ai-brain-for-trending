# (C) Phase 4b — Pattern Library contribution — open-slide (v135)

**Subject:** `1weiho/open-slide` · **Routine v2.6** · 2026-06-02
**PRIMARY:** Library-vocab **"Cited-to-Subject Elevation" → N=2** (re-registration on a genuine 2nd instance; v93 anchor + v135).
**State change at ship:** NONE (46 confirmed / 8 Library-vocab CONFIRMED unchanged). No top-level pattern, no sub-archetype, no new standalone minted.

---

## PRIMARY — Cited-to-Subject Elevation → N=2 (re-registration / strengthening)

### The event
open-slide was previously present in the corpus **only as a citation**: v91 html-anything **vendored its 1920×1080 canvas convention** and logged it as *"not yet corpus-relevant"* (verifiable: `03 Projects/html-anything - Beginner Analysis/02 Wiki/(C) log.md` + `(C) cluster-1-…md` + `(C) cluster-2-…md`). At v135 it is promoted to a **first-class subject**. That is a clean instance of the corpus event-class **"a subject first appears as a cited/vendored reference, then is later elevated to its own wiki."**

### Why this is a re-registration (not a new mint)
- v93 anthropics/skills minted **"Retrospective-Promotion-from-Cited-to-Subject"** as a PROVISIONAL N=1 Library-vocab item (2026-05-25).
- Per routine §28 auto-retire (N=1 standalone retires ~15 wikis without a 2nd instance), v93+15 ≈ v108 — so the item has almost certainly auto-retired by v135. §28 explicitly permits **re-registration on a genuine 2nd instance.**
- open-slide is that genuine 2nd instance → I **re-register the item as N=2** under the broader label **"Cited-to-Subject Elevation."** Promotion-eligible toward CONFIRMED at N=3.

### Honest sub-flavor distinction (recorded, not laundered)
- **v93** flavor: a subject **cited as a methodology source** (anthropics/skills was referenced for the agentskills.io standard) then became the subject.
- **v135** flavor: a subject **vendored as a dependency / borrowed convention** (the 1920×1080 canvas v91 adopted) then became the subject.
- Same family (cited → subject), slightly different sub-flavor (methodology-citation vs dependency-vendoring). I register the **broad** family at N=2 and note the two sub-flavors; whether they're one class or two is an N=3 question for a future audit. **No unilateral promotion.**

## SECONDARY (observations — §28-disciplined; instance notes, not mints)

1. **Pattern #84 84c "multi-harness / provider-agnostic" — N+1** (CONFIRMED). Ships `.claude/skills` (Claude Code) + universal `.agents/skills` + `AGENTS.md` (Codex/Cursor); README names Claude Code + Codex + Cursor. **Modest** multi-harness (no GEMINI.md, no per-harness config beyond `.claude/` + universal `AGENTS.md`) — instance noted, not re-minted, and not inflated to a large harness-count claim.
2. **Library-vocab #12 LLM-routing artifacts — N+1** (CONFIRMED). `CLAUDE.md` + `AGENTS.md` + `.claude/skills` + `.agents/skills` = 4 routing artifacts at root.
3. **Presentation/slide-tooling-for-agents cluster — OBSERVATION ONLY (NOT minted).** v82 huashu-design (design/PPTX) + v91 html-anything (deck = 1 of 9 surfaces) + v133 GordenPPTSkill (PPT-builder skill) + v135 open-slide (React slide framework). The members are **heterogeneous** (design-language vs file-emitter vs multi-surface vs framework) — minting a "slide-tooling-for-agents" sub-archetype at this stage would be exactly the anti-pattern the v125/v128/v129/v134-v135 discipline warns against. Logged as adjacency, not a new tier sub-archetype.
4. **Convention-propagation-between-corpus-subjects — OBSERVATION (NOT minted).** The 1920×1080 fixed-canvas + React-component-per-slide convention **propagated to another corpus subject** (v91 adopted it). A mini cross-wiki influence signal — interesting, but narrow and product-specific. Noted; **no standalone filed** (keeps the §28 new-standalone count at 0 this ship).
5. **Pattern #82 quantitative-marketing — mild.** "The slide framework built for agents", 4.4k★, "built for agents" framing. Present but thin; instance note only.

## Honest non-claims
- **NO Pattern Library state change at ship** (46 confirmed / 8 Library-vocab CONFIRMED unchanged).
- **PRIMARY is a re-registration/strengthening (N=2), NOT a promotion.** The cited→subject class advances toward CONFIRMED only at a genuine N=3.
- **NOT an agentskills.io 57k implementer.** It ships its own scaffolder (`npx @open-slide/cli init`) + `.claude/skills`; there is no evidence of `npx skills add` / agentskills.io registration. (Conceptually a framework-bundled-skills model, like v114/v126 vendor-skills but for the framework's own use, not a 57k chain node.)
- **NOT a Pattern #52 promotion** — created_at not API-verifiable in this sandbox; velocity approximate (~4.4k★ over an unverified window). Recorded as a positive-but-unquantified signal, not a sub-class claim.
- **(b) MODERATE, not STRONG/STRONGEST** — presentation domain, conditional applicability (see verdict doc + GordenPPTSkill contrast).
- **ZERO new Library-vocab standalones minted** (§28 ≤2 cap; used 0). **NO new tier sub-archetype.** **NO new top-level pattern.**

## What a future audit should carry from v135
1. **"Cited-to-Subject Elevation" N=2** (v93 + v135) — watch for an N=3 to promote, and decide whether the methodology-citation vs dependency-vendoring sub-flavors are one class or two.
2. The presentation/slide-tooling-for-agents cluster (v82+v91+v133+v135) — re-assess only if a genuinely homogeneous 2nd framework appears (don't mint on the heterogeneous current set).
