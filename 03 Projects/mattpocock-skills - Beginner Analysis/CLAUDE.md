# mattpocock-skills - Beginner Analysis

> **Project type:** LLM Wiki v57 — Storm Bear corpus 57th wiki
> **Subject:** `mattpocock/skills` — Matt Pocock's "Skills For Real Engineers" — opinionated agent-skills collection
> **Date:** 2026-05-06 (session 69)
> **Tier:** T1 Assistant (skills bundle for Claude Code / Codex / agents — extends T1 N count)
> **Build mode:** Main-loop direct-write (per v56 lesson — avoid agent-thrash)
> **Storm Bear meta-entity:** ✅ INCLUDE (Phase 0.9 STRICT criteria PASS — see decision below)

---

## 12-axis classification

| Axis | Value |
|---|---|
| **Tier** | **T1 Assistant** (Claude Code / Codex / generic-agent skills bundle delivered as plugin) |
| **Archetype** | Solo-individual + commercial-educator (Matt Pocock — Total TypeScript founder + ex-Vercel + ex-Stately) + decades-of-engineering-experience-claim + skills-as-distillation-of-practice |
| **Scale tier** | **XX-Large 62,000 stars** (Top-10 in corpus; 5,300 forks; 478 watchers; 16 open issues; 66 commits = velocity-burst not slow-build) |
| **Primary lang** | Shell 100% (markdown skill files + shell installer; no TS source) |
| **Packaging** | `npx skills@latest add mattpocock/skills` (npm-package-as-installer + GitHub-as-source-of-truth) |
| **Origin story** | Solo-individual-author + extracted-from-personal-`.claude`-directory + commercial-educator-side-project + tagline "Straight from my .claude directory" |
| **Methodology** | Anti-vibe + pro-fundamentals + grilling-session pre-implementation + ubiquitous-language (DDD) + red-green-refactor TDD + tracer-bullet vertical slicing + deep-modules (Ousterhout) + lazy-ADR documentation |
| **Governance** | Light-Medium (CLAUDE.md = bucket-folder discipline + plugin.json declares 13 skills + README references mandatory + bucket README required + personal/in-progress/deprecated buckets explicitly hidden) |
| **Agent/skill count** | **13 active skills** (10 engineering + 3 productivity) + 4 misc + N hidden (personal/in-progress/deprecated) |
| **i18n** | EN-only |
| **Intellectual influence** | **5 explicit citations: Pragmatic Programmer (Hunt+Thomas) + Domain-Driven Design (Eric Evans) + Extreme Programming (Kent Beck) + A Philosophy Of Software Design (John Ousterhout) + GSD/BMAD/Spec-Kit as anti-pattern foils** |
| **Agent platforms** | Multi-platform-by-design (Claude Code primary + Codex + "any model" claim) — `npx skills add` installer abstracts agent target via interactive selection |

---

## Phase 0.5 overlap pre-check (12 candidate observations)

All 12 routed to within-pattern strengthening per consolidation-forward discipline; **0 new standalone candidates**.

1. **5 explicit methodology-book citations in README** → Pattern #57 sub-variant TBD or Pattern #19 archetype 4 strengthening (named-lineage-via-book-citation, distinct from individual-name-lineage like Karpathy/Lam)
2. **Explicit "GSD, BMAD, Spec-Kit" anti-pattern foils** → **Pattern #57 57c forward-citation-then-wiki structural data point — explicit multi-frontend in-corpus-reference; corpus-first multi-citation-of-prior-corpus-subjects in single README** (BMAD v11 + GSD v5/gsd-2 v54 + spec-kit v17 = 3 distinct prior corpus subjects cited as anti-pattern foils)
3. **3rd skills-collection repo at T1** → Pattern #18 horizontal-aggregation N=3 candidate (after awesome-claude-skills v50 + agent-skills-of-vercel v51) — but Matt's is **opinionated-curated-by-author** not aggregator-curated; sub-variant distinction
4. **MIT license** → Pattern #29 strengthening at standard-OSI sub-context (does NOT advance non-commercial-restriction-custom-license N=4)
5. **`npx skills add` installer pattern** → Pattern #2 distribution-evolution data point (CLI-installer-as-primary surface)
6. **Plugin manifest `.claude-plugin/plugin.json` declaring skills** → Pattern #22 governance-template strengthening (plugin manifest is emerging convention)
7. **62K stars in 66 commits** → Pattern #52 Extreme-Viral-Velocity un-stale candidate? **CHECK CAREFULLY** (extreme-burst velocity ratio: 62K stars / 66 commits ≈ 939 stars/commit; vs sustained-organic n8n 71 stars/day across 7 years)
8. **Solo-commercial-educator archetype** → Pattern #19 archetype 4 + Pattern #17 variant 1 strengthening (individual-multi-publisher with educator commercial brand — Total TypeScript)
9. **Bucket-folder discipline (engineering/productivity/misc/personal/in-progress/deprecated)** → Pattern #69 Primitive-count taxonomy LARGE-tier (~13 active + ~4 hidden = ~17 total directories; not EXTREME 7+ primitive-count yet — actually 6 directory categories with skills inside)
10. **CONTEXT.md domain-glossary primitive** → NEW within-pattern observation in Pattern #18 or Pattern #22 (domain-glossary-as-skill-required-input is novel signal but at N=1)
11. **Anti-vibe positioning ("real engineering, not vibe coding")** → Pattern #51 Vibe-Coding Spectrum anti-vibe pole strengthening
12. **`/grill-me` + `/grill-with-docs` interview-as-skill primitive** → Pattern #18 sub-observation — interview-pattern-as-deliverable structural data point (sister to brain-setup-style routines)

**0 NEW STANDALONE CANDIDATES.** **STREAK: 21-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES** (extending v56 20-streak — NEW LONGEST in corpus history).

## Un-stale check

- **#45 Dual-Licensing** — mattpocock/skills single MIT; does NOT un-stale. STAY STALE.
- **#52 Extreme-Viral-Velocity** — **CANDIDATE FOR UN-STALE.** 62K stars / 66 commits is structurally extreme-velocity. **BUT** — needs comparison against time-axis (when was repo created? unknown without commit-date probe). Conservative-discipline default: register observation but DO NOT trigger un-stale until time-axis verified at next mini-audit. **OBSERVATIONAL ONLY at v57; flag for v60 mini-audit re-evaluation.**
- **#72 PolyForm-Noncommercial** — MIT not PolyForm. STAY STALE.

2 of 3 un-stale checks NEGATIVE. 1 (#52) **OBSERVATIONAL FLAG for next mini-audit**, not direct un-stale.

## Phase 0.9 STRICT 4-criteria gate (session-66 amendment)

| Criterion | Verdict | Evidence |
|---|---|---|
| (a) Author archetype peer | ⚠️ PARTIAL | Matt Pocock = solo-individual-author (peer in solo dimension) + commercial-educator-with-Total-TypeScript-paid-course (peer in commercial-side-project dimension). NOT VN/Asian-diaspora; English location (Oxfordshire). Solo-side-project to commercial-revenue parallel structurally close to Storm Bear's solo Scrum-coaching practice. **DEFAULT FAIL on strict reading** but borderline. |
| (b) Operational tool for Scrum-coaching workflows | ✅ **PASS** | 13 skills directly deployable in Storm Bear's daily Claude Code workflows: `/grill-me` + `/grill-with-docs` for client-discovery sessions; `/tdd` for software-build practice; `/triage` for backlog management (Scrum-relevant); `/to-prd` + `/to-issues` for sprint-planning artifact generation; `/improve-codebase-architecture` for technical-debt audits. MIT license = no commercial-use barrier. |
| (c) Methodology-influence-node | ✅ **PASS** | README cites 5 named methodology sources directly applicable to vault routine v2.1 maintenance: Pragmatic Programmer (feedback loops + small steps) + DDD (ubiquitous language ↔ vault terminology discipline) + XP (Beck — invest in design every day) + Philosophy of Software Design (Ousterhout — deep modules ↔ skill-design discipline) + plus explicit anti-pattern positioning vs GSD/BMAD/Spec-Kit (corpus-internal methodology peers). 3 of 5 books are vault-relevant references. |
| (d) In-corpus reference | ✅ **PASS** | README explicitly cites BMAD + GSD + Spec-Kit as anti-pattern foils — **3 distinct prior corpus subjects cited in single README**. BMAD-METHOD v11 + GSD v5 / gsd-2 v54 + spec-kit v17. Pattern #57 57c forward-citation-then-wiki: corpus subject (BMAD/GSD/spec-kit) cited by later corpus subject (mattpocock/skills v57). Multi-citation distinct from prior 57c instances which were 1-to-1. |

**DECISION:** Criteria (b) + (c) + (d) **STRONGLY PASS** (3 of 4). **INCLUDE Storm Bear meta-entity legitimately under STRICT amendment.** Streak preserved at **40th consecutive Storm Bear meta-entity** (39 prior including v56 STRICT-1st + v57 STRICT-2nd at 3-criteria-pass — strongest STRICT-amendment Storm Bear meta-entity in corpus to date).

## Counter-evidence audit

- Pattern #57 57c forward-citation-then-wiki: STRENGTHENS strongly (multi-frontend citation in single README is structurally distinctive)
- Pattern #18 skills-collection at T1: STRENGTHENS but introduces **opinionated-curated-by-author** sub-variant distinction (vs aggregator-curated awesome-claude-skills v50 + plugin-manifest agent-skills-of-vercel v51)
- Pattern #51 Vibe-Coding Spectrum anti-vibe pole: STRENGTHENS (explicit "real engineering, not vibe coding" tagline)
- Pattern #19 archetype 4 individual-lineage: STRENGTHENS (5 named book-citations distinct from individual-name lineage like Karpathy)
- Pattern #29 MIT license: NEUTRAL-BASELINE (standard OSI; no narrowing)

## Velocity + scope notes

- 57th wiki built main-loop direct-write (post-v56 lesson applied: avoid agent thrash for high-primitive-count repos)
- Probe → write velocity ~30-40 min target
- Compressed-scope: 1 cluster summary + 4 entities + 1 beginner guide + 1 Phase 4b deliverable + 1 iteration log

## File index

- `00 INDEX.md` / `00 LOG.md` / `00 OPEN-QUESTIONS.md`
- `01 Sources/(C) Cluster — Combined source summary.md`
- `02 Entities/` — 4 entity pages
- `(C) 03 Beginner Guide.md` — bilingual VN+EN
- `(C) 04 Phase 4b — T1 multi-citation-of-prior-corpus-subjects + 3rd skills-collection sub-variant.md`
- `(C) 05 Iteration log v57.md`

## Pattern Library impact (post-v57)

- **Strongest Pattern #57 57c forward-citation-then-wiki evidence to date** (multi-frontend citation in single README; 3 distinct prior corpus subjects cited as anti-pattern foils) — promotion candidate for next mini-audit (potential 57c sub-variant 57c-multi-frontend or formal-statement extension)
- 3rd skills-collection at T1 → Pattern #18 horizontal-aggregation expanded; opinionated-curated-by-author sub-variant candidate (N=1 stale-flagged)
- **40th consecutive Storm Bear meta-entity** (3 of 4 STRICT criteria pass — strongest STRICT-amendment instance to date)
- **21-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak** (NEW LONGEST extends v56 20-streak)
- Pattern #52 OBSERVATIONAL flag for next mini-audit time-axis verification
- Pattern Library state post-v57: **39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = 74 full / 56 active. Ratio 17:39 = 0.436:1 PRESERVED 7TH CONSECUTIVE CYCLE** (largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 7 cycles — NEW LARGEST in corpus history maintained 7 cycles)

## v27 diagnostic HIGH bundle status

- Pre-v57: **v27 HIGH bundle 100% COMPLETE session 68 (2026-04-29)** per root CLAUDE.md
- Post-v57: vault-public-released; routine v2.1 STRICT Phase 0.9 amendment continues to apply

## References

- Routine: `05 Skills/llm-wiki-routine-v2.1.md`
- Style reference: `_state/03a-projects-v48-v55.md` (v55 + v56 entries)
- Recent additions: `_patterns/05-recent-additions.md`
- Sibling skills-collections: `03 Projects/awesome-claude-skills - Beginner Analysis/` (v50) + `03 Projects/agent-skills-of-vercel - Beginner Analysis/` (v51)
- Cited corpus subjects in mattpocock/skills README: `03 Projects/BMAD-METHOD - Beginner Analysis/` (v11) + `03 Projects/get-shit-done - Beginner Analysis/` (v5) + `03 Projects/gsd-2 - Beginner Analysis/` (v54) + spec-kit (v17 — folder name differs in `03 Projects/`)
