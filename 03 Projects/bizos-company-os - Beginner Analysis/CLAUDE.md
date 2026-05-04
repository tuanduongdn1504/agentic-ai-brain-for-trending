# CLAUDE.md — bizos-company-os Beginner Analysis

> **Target:** `ungden/bizos-company-os` — Next.js 16 + Supabase business-OS ("Task → personal KPI → team KPI → company KPI → Financials"), 19 screens, by Alex Le / Titan Labs (VN).
> **Live demo:** https://bizos-company-os.vercel.app
> **Routine:** `llm-wiki-routine-v2.1` (this is v37 in Storm Bear corpus — 5th v2.1-era execution post-mini-audit + 26th consecutive Storm Bear meta-entity)
> **Shipped:** 2026-04-24

---

## 12-axis classification (Phase 0 output)

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE** — business-OS-as-product (7th outside-scope sub-type candidate; registered as OBSERVATION-TRACK not active candidate) |
| **Archetype** | Solo-VN-author business-application-at-cold-start (18 stars / 25 forks / 2 days old; 138% fork-to-star template-use ratio) |
| **Scale tier** | Cold-start (<5K) — smallest wiki-subject in corpus |
| **Primary lang** | TypeScript 90.5% + PLpgSQL 9.0% |
| **Packaging** | pnpm + Docker (multi-stage) + Vercel config + Railway config (4 deploy surfaces) |
| **Origin story** | Individual-author + cold-start (no community traction yet) |
| **Methodology** | **Domain methodology (KPI cascade)** — NOT agent methodology. Task → personal KPI → team KPI → company KPI → Financials chain. |
| **Governance** | **Light-minimal** — 2 files (AGENTS.md 327B + CLAUDE.md `@AGENTS.md` 11B pointer); **NO LICENSE file** (proprietary statement in README only) |
| **Agent/skill count** | **ZERO agents / zero skills** — 19 screens + 64 DB tables + 7 RBAC roles + 10 KPI operators + 5 bonus tiers |
| **i18n** | VN+EN bilingual first-class (626-entry dict; locale switcher in top bar); VN-primary README |
| **Intellectual influence** | None cited |
| **Agent platforms** | **ZERO** — no MCP / no agent primitives / AGENTS.md is 327B Next.js-agent-rules pointer only |

## Phase 0.5 Pattern pre-check

**Overlap pre-check outcomes (4 candidates considered, 0 registered):**
1. "Business-OS-as-product outside-scope sub-type 7" — considered; REJECTED standalone registration (single data point + cold-start + insufficient N). **Registered as OBSERVATION-TRACK only.**
2. "No-LICENSE-at-publish candidate" — overlaps with Pattern #29 License-Category-Diversity (confirmed). **Absorbed as sub-category strengthening of #29 (proprietary-by-default + no-LICENSE-file sub-variant).**
3. "Fork>Star template-use anomaly" — overlaps with Pattern #27 Community-Viral Scale Path (counter-evidence framing). **Registered as OBSERVATION-TRACK only.**
4. "Cold-start-snapshot methodological archetype" — methodological, not content. **Documented in iteration log, not registered.**

**Un-stale check (all NEGATIVE):**
- #45 Dual-Licensing — NEGATIVE (single-source proprietary)
- #46 Duo-Founder + Team — NEGATIVE (solo author)
- #52 Extreme-Viral-Velocity — NEGATIVE (18 stars, opposite of extreme-viral)
- Retired-revivals (#14/#16/#23/#25/#49/#55/#60/#70) — all NEGATIVE

**Counter-evidence observations (documented, not refining):**
- **Pattern #22 AGENTS.md industry standard** (confirmed) — bizos AGENTS.md is 327B Next.js-agent-rules pointer + CLAUDE.md is `@AGENTS.md` one-liner. Strengthens #22 adoption at outside-scope tier + documents **minimum-viable-AGENTS.md sub-variant** (327B contrast to pi-mono v36 182-line maximum). No formulation change.
- **Pattern #73 Regional-Archetype-Registry T1** (confirmed v36 as meta-pattern) — bizos is VN-authored but outside-scope (not T1). Pattern #73 is T1-scoped; bizos is **cross-tier VN observation** only. Does NOT strengthen 73b VN sub-variant (which is T1-only). Document observation for future cross-tier meta-pattern consideration IF 3+ cross-tier VN data points emerge.

**Consolidation-forward discipline:** Applied. Zero new active candidates registered.

## Phase 0.9 Primitive-count probe — YELLOW (2nd YELLOW in corpus)

**Primitive surface** (~150-180 distinct):
- 19 user-facing screens (`/dashboard` /org /departments /people /kpi /operations /compensation /projects /finance /reports /alerts /approvals /audit /okr /forecast /recruiting /knowledge /profile /settings /guide)
- 64 DB tables across 11 domain areas (org / rbac / KPI / operations / compensation / projects / finance / OKR / recruiting / knowledge / governance)
- 7 RBAC roles (ceo / cfo / hr_admin / dept_head / team_lead / employee / auditor)
- 10 KPI formula operators (sum / sub / mul / avg / weighted_avg / ratio / milestone / ref / const / manual)
- 5 bonus-tier thresholds + team/company multipliers
- 4 internal engines (formulaEngine / cascade / ruleEngine / queries-with-demo-fallback)
- 4 deploy surfaces (Vercel / Railway / Docker / local pnpm dev)
- 2 auth modes (Supabase / demo-no-env fallback)
- 626-entry i18n dict (VN+EN)
- 4 KPI status colors (green ≥100% / yellow 85-99% / red <85% / n/a)
- 19 mockup PNG designs + designer source

**Outcome: YELLOW** (3-4× GREEN baseline ~50-70 primitives). Consistent with v36 pi-mono YELLOW precedent.

**Scope-compression decisions (v2.1 informal discipline):**
- **4 entity allocation:**
  1. BIZOS core product — 19-screen shell + KPI cascade chain + demo-mode fallback (high-level, cites /guide for per-screen detail)
  2. Internal engines + data architecture — formulaEngine (10 ops) + cascade + ruleEngine (5 tiers) + 64 tables + 7-role RLS (combined technical entity)
  3. Alex Le + Titan Labs + VN solo-developer archetype
  4. Storm Bear meta (26th consecutive) — "VN solo-developer builds production business software with Claude Code" as operator-adjacent reference + business-OS-as-product outside-scope framing
- **Lossy compression accepted:** per-screen feature lists cite /guide instead of replicating; per-table schema details grouped into 11 domain areas; 626 dict entries summarized not enumerated.
- **Citation-not-replication:** AGENTS.md (327B), full install commands, screen walkthroughs cite upstream README + /guide page as primary sources.
- **Velocity overhead expected:** ~2h 30min-2h 40min (vs ~2h GREEN baseline), within YELLOW tolerance from v36 precedent.

## Phase 4b routing mode

**Primary:** `cold-start-outside-scope observation` + **`business-OS-as-product 7th outside-scope sub-type formalization (OBSERVATION-TRACK)`** + **`no-LICENSE-at-publish documentation`** (strengthens Pattern #29 License-Category-Diversity with absent-LICENSE sub-category)

**Secondary:** cross-tier VN observation (Pattern #73 does not extend to outside-scope; observation only)

**Novelty:** First cold-start-snapshot wiki (2-day-old repo at 18 stars) + first absent-LICENSE wiki in corpus + first business-domain-methodology (KPI-cascade) wiki

## Storm Bear meta-entity warranted?

**YES (26th consecutive).** Alex Le is a VN solo-developer peer archetype (Head of Product at Titan Labs; same region, adjacent craft to Storm Bear operator). Wiki demonstrates "VN solo-developer ships production business software built largely with Claude Code" as a direct-pilot reference case. The "Claude Code built this" positioning (inferred from .claude/launch.json + AGENTS.md + CLAUDE.md presence) establishes bizos-company-os as evidence for Storm Bear's own mission.

## Cross-references

**Sibling wikis cited by this wiki:**
- v36 pi-mono — primary reference (YELLOW precedent + solo-author-monorepo precedent)
- v34 claude-code-best-practice — Shayan Rais VN-adjacent regional + 82-tip aggregation
- v32 claude-howto — Luong Nguyen VN-diaspora T1 (comparison: VN T1 agent tutorial vs VN outside-scope business app)
- v12 codymaster — Tody Le VN-in-VN T1 (comparison: VN T1 agent framework vs VN outside-scope business app)
- v18 agency-agents — solo-enterprise-scale T1 contrast
- v29 crawl4ai — counter-evidence methodology precedent
- v21 system-prompts-leaks — ethical-framing ⚠️ precedent (absent-LICENSE analogous to unclear-license)
- Pattern Library current state: 34 confirmed + 23 active + 4 stale + 8 retired + 1 OT = 71 full / 57 active (ratio 0.68:1 post-v36 mini-audit)

---

*This file is the project-level context for the v37 wiki build. See `02 Wiki/(C) index.md` for phase tracking and `04 Reviews/(C) 2026-04-24 v37 build learnings.md` for iteration log.*
