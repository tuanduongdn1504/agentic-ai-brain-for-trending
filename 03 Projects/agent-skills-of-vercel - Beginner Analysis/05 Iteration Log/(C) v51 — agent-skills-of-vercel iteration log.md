# (C) v51 — agent-skills-of-vercel Iteration Log

**Built:** 2026-04-25 (session 61)
**Routine:** v2.1
**Wiki number:** 51 (first wiki post-corpus-half-century-milestone)
**Subject:** vercel-labs/agent-skills (25,695 stars / 4.5 months / MIT-claim / no LICENSE file)

---

## 1. Milestones hit

### Corpus-level

- ✅ **51st LLM wiki — first wiki post-corpus-half-century-milestone (v50)**
- ✅ **15-consecutive-wiki zero-new-active-candidates streak v37-v51** (NEW LONGEST in corpus history; extends v37-v50 14-streak)
- ✅ **8th v2.1-era routine execution post-v44 GREEN**; ratio 0.474:1 PRESERVED 1st post-mini-audit cycle
- ✅ **40th consecutive Storm Bear meta-entity** (v10-v51)
- ✅ **32 consecutive wikis at velocity plateau** (v6-v51; ~3h 30min within tolerance for multi-pattern harvest scope)
- ✅ **Pattern #17 variant 5 reaches N=3 default-criterion + dual-criterion-satisfaction** (HuggingFace + Microsoft + Vercel; analogous to Pattern #42 dual-criterion at v45)
- ✅ **Pattern Library hits 4-sub-variant taxonomy at #22** (22a/b/c/d) — most-elaborate sub-variant taxonomy in library
- ✅ **Pattern #57 reaches 3-sub-variant taxonomy** (57a/b/c)

### Framework-specific

- ✅ **T1 extends to N=15** with NEW corporate-narrow-skill-library sub-archetype (Vercel v51)
- ✅ **Pattern #22 22d identical-mirror sub-variant NEW** (corpus-first AGENTS.md = CLAUDE.md byte-identical mirror; N=1 stale-flagged)
- ✅ **Pattern #57 57c forward-citation-then-wiki sub-variant NEW** (multica v15 cited "Vercel agent-skills import (first)" 36 wikis pre-v51; first external validity signal of corpus-selection discipline)
- ✅ **Pattern #29 29-absent-3 N=2 strengthening** (awesome-claude-skills v50 + Vercel v51; promotion-candidate at next mini-audit under structural-N=2 criterion)
- ✅ **Pattern #50 50a most-explicit claim-URL-as-funnel-terminus observed** (vercel-deploy-claimable bipartite preview-URL + claim-URL output)
- ✅ **15 corpus-firsts documented** (see section 8)

---

## 2. Phase breakdown

| Phase | Duration | Notes |
|---|---|---|
| 0 Pre-flight | 25 min | 12-axis classification + Pattern Library pre-check + 9-candidate overlap pre-check (all routed to strengthening) + Storm Bear applicability + tier placement |
| 1 Scaffold | 10 min | 5 subfolders + foundational files |
| 2 Source ingestion | 45 min | 3 cluster summaries; SKILL.md content rich despite small repo |
| 3 Entity pages | 50 min | 4 entity pages with multi-pattern coverage; Pattern #17 variant 5 N=3 analysis + Storm Bear meta-entity 4-template ensemble |
| 4a Beginner guide | 25 min | Bilingual VN+EN, ~480 lines |
| 4b Phase 4b deliverable | 30 min | Multi-pattern strengthening harvest |
| 5 Iteration log | 15 min | This document |
| 6 Vault sync | 15 min | PATTERN_LIBRARY.md + CLAUDE.md + GOALS.md |
| **Total** | **~3h 35min** | Within ~3-4h tolerance for multi-pattern harvest scope |

---

## 3. What worked

- **Source already cloned** at `00 Source/agent-skills/` (1.2 MB) — no fetch overhead
- **Small repo, rich content** — 7 SKILL.md files (1,367 lines total) + AGENTS.md/CLAUDE.md identical-mirror discovery + per-skill license metadata variation
- **`diff` verification of 22d identical-mirror** — definitive proof (zero-output) before pattern registration
- **multica v15 forward-citation discovery via grep** — `/usr/bin/grep -in "Vercel agent-skills" CLAUDE.md` immediately surfaced line 2969 matching exact pattern
- **Pattern #17 variant 5 5-criteria check** — clean default-criterion satisfaction verification (Vercel meets all 5 unambiguously)
- **15-streak zero-registration discipline** — 9 candidate observations all routed to within-pattern strengthening or sub-variant registration without forced fragmentation

---

## 4. What didn't work / friction

### Minor friction

- **Shell init issue** — zsh alias `rtk` was broken throughout session; required workaround using `/bin/ls` / `/usr/bin/grep` / `/bin/mkdir` etc. with absolute paths. Slowed Phase 0 + Phase 1 by ~5 min.
- **Initial probe undercounted skills** — README lists 6 skills but 7 directories exist. `vercel-cli-with-tokens` is undocumented in README (companion to deploy-to-vercel). Probe now flags this discrepancy.
- **README label vs YAML name vs directory name divergence** — 3 different naming conventions per skill (e.g., `react-native-guidelines` README label / `react-native-skills` directory / `vercel-react-native-skills` YAML name). Required careful disambiguation in Cluster 1 + Entity 1.
- **Claude Code's `WebFetch` not used** — source already cloned, so `WebFetch` skipped. Phase 0.2 documented as "verified" rather than "fetched."

### Recurring friction (carry-forward)

- **v27 diagnostic HIGH bundle backlog** — escalated to **31 sessions deferred** post-v51 (BLOCKING-RECOMMENDATION 6.2× threshold; per v2.1 operator-facing-backlog discipline 5-session threshold). Not addressed at v51 — wiki is structurally cleaner than vault refactor.

---

## 5. Routine v2.1 → v2.2 action items (NEW from v51)

### NEW v51 action items (cumulative ~290+ across v3-v51)

1. **Sub-variant N-tracking discipline** — Pattern #57 now has 3 sub-variants with mixed N status (57a CONFIRMED N=4, 57b CONFIRMED N=1 stale-flagged, 57c NEW N=1 stale-flagged). Routine v2.2 should formalize sub-variant N-tracking table maintenance per pattern (analogous to N=1 stale-tracking table at top-level).

2. **AGENTS.md sub-variant probe protocol** — Routine v2.2 should add explicit `diff AGENTS.md CLAUDE.md` probe at Phase 0 to detect 22d identical-mirror cleanly. v51 caught this manually; future wikis with both files should automatically classify per 22a/b/c/d sub-variant.

3. **Forward-citation-then-wiki detection at Phase 0.5** — When pre-checking against PATTERN_LIBRARY.md, additional check: was current wiki subject CITED in any prior wiki entry as a dependency? Grep vault CLAUDE.md for `<repo-name>` would surface this. v51 caught multica v15 citation manually.

4. **Per-skill license metadata variation as Pattern #29 sub-context probe** — When wiki subject ships multiple skills/sub-modules, probe each for YAML `license:` field; flag variation as 29-absent-3 evidence. Generalizes to other multi-module wikis.

5. **Storm Bear pilot ranking refresh template** — Routine v2.2 could include "pilot ranking refresh" template in Phase 4a beginner guide (after each new wiki). v51 ranked 8 NEW (Vercel SKILL.md format adoption) but format not standardized.

6. **`npx skills add` third-party-registry discipline** — When wiki uses third-party non-Anthropic install registry, flag as Pattern #66 supply-chain awareness even if non-incident. Trust gradient: Anthropic-native > Vercel-published > random-publisher; routine should surface this gradient.

### Cumulative running counter

- v3 → v51: ~290+ cumulative action items (estimated, given v50 was at ~285)

---

## 6. Total action items running counter

**Updated cumulative: ~290+ action items (v3 through v51)**

Routine v2.1 → v2.2 refactor should be triggered when cumulative reaches threshold (proposed: 300 action items OR v60 wiki, whichever sooner).

---

## 7. Meta-observations

### Pattern Library health post-v51

- 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio 18:38 = **0.474:1 PRESERVED 1st post-v50-mini-audit cycle** (the unprecedented sub-0.50:1 ratio holds)
- 0.476 buffer below 0.95:1 mini-audit trigger PRESERVED — largest in corpus history
- 9 promotion-candidates accumulated (post-v50 mini-audit + v51): #29 AGPL-at-project-scope / #50 50b recruiting-funnel / #66 OT sub-categorization / #18 4-layer / #22 22c scope-narrowing / #47 retirement / **#22 22d (NEW)** / **#57 57c (NEW)** / **#29 29-absent-3 promotion (NEW)**

### Sub-variant taxonomy maturity

Post-v51, Pattern Library has multiple patterns with sub-variant taxonomies:
- **#17 variant 5 ecosystem-scale commercial platform** (CONFIRMED v29)
- **#22 AGENTS.md** — 4 sub-variants (22a/b/c/d)
- **#57 Recursive Corpus Reference** — 3 sub-variants (57a/b/c)
- **#29 License-Category Diversity** — 4 absent-LICENSE sub-contexts (29-absent-1/2/3 + AGPL sub-variant pending)
- **#50 Commercial-Funnel Companion** — 3 sub-variants (50a/b/c)

**Library reaches structural-maturity threshold predicted at v36 mini-audit** (confirmed-count 38 ≥ 2× active-candidate-count 18 = 36). Library shape is now "many CONFIRMED patterns with rich sub-variant taxonomies" rather than "many candidates seeking promotion."

### Forward-citation-then-wiki as external validity signal

multica v15 → Vercel v51 forward-citation pathway is **first observed corpus-selection-validation across ~36 wikis of separation**. Independent agent-ecosystem judgment (multica's skills-lock dependency manifest) retroactively validates Storm Bear's selection criteria (vault routine's choice of Vercel as v51 subject).

This signals corpus-selection discipline maturity. Storm Bear corpus is converging with broader agent-ecosystem judgment without explicit collaboration.

### Storm Bear meta-entity 40-streak

40 of 42 wikis (95%) post-v10 include Storm Bear meta-entity. Per-wiki applicability check at Phase 0.9 consistently PASS because most agent-framework wikis reveal vault-architectural lessons or pilot candidates.

---

## 8. Unique findings (corpus-firsts)

1. **AGENTS.md = CLAUDE.md byte-identical mirror (Pattern #22 22d sub-variant NEW)** — verified via `diff` zero-output; both 3,281 bytes, both starting `# AGENTS.md`
2. **Forward-citation-then-wiki (Pattern #57 57c sub-variant NEW)** — multica v15 cited "Vercel agent-skills import (first)" 36 wikis BEFORE v51; first external validity signal across 36-wiki separation
3. **Pattern #17 variant 5 N=3 default-criterion** — HuggingFace + Microsoft + Vercel; first variant within #17 to reach dual-criterion-satisfaction (structural-N=2 + default-3-cross-tier)
4. **Pattern #29 29-absent-3 N=2 strengthening** — awesome-claude-skills v50 + Vercel v51 = 2 wikis exhibiting 3-property signature (absent root LICENSE + README OSI claim + per-skill license metadata variation)
5. **`npx skills add <repo>` install verb** — corpus-first third-party non-Anthropic registry install (skills.sh / agentskills.io ecosystem)
6. **`argument-hint: <file-or-pattern>` YAML field** — corpus-first slash-command argument hint convention (web-design-guidelines)
7. **Per-rule prefix-namespace** — corpus-first per-rule taxonomy convention (composition-patterns: `architecture-` / `state-` / `patterns-` / `react19-`)
8. **Per-skill semver YAML metadata** — all 7 skills declare `metadata.version`; deploy-to-vercel at v3.0.0 (3 majors in 4.5 months); others at v1.0.0
9. **Build pipeline for rule-aggregator skill** — `packages/react-best-practices-build/` compiles per-rule MD files into consolidated SKILL.md (single-skill build pipeline)
10. **Claim-URL-as-funnel-terminus most-explicit observed** — vercel-deploy-claimable bipartite output (preview URL + claim URL); Pattern #50 50a most-elaborate observed instance
11. **Corporate-amplified-organic ~5,700 stars/month** — 25.7K / 4.5 months; mid-pack for corporate-amplified sub-path
12. **Per-skill license metadata variation** — 4 of 7 skills declare `license: MIT` in YAML; 3 do not (rule-aggregator skills declare; practical-script skills do not)
13. **Most-elaborate per-skill structure (composition-patterns)** — ships its own AGENTS.md + README + metadata.json + rules/ INSIDE skill directory
14. **README label vs YAML name vs directory name divergence** — 3 naming conventions per skill (`react-native-guidelines` / `react-native-skills` / `vercel-react-native-skills`)
15. **15-consecutive-wiki zero-new-active-candidates streak (v37-v51)** — NEW LONGEST in corpus history; extends v37-v50 14-streak

---

## 9. Storm Bear vault impact

### Direct utility (HIGH for SKILL.md format reference)

**Vercel SKILL.md format = most-direct corpus template for vault `05 Skills/` directory expansion.** Currently vault has 8 skills, all prose markdown, no YAML frontmatter, no trigger-phrase activation, no on-demand loading.

**NEW Storm Bear pilot #8:** Convert `llm-wiki-routine-v2.1.md` to Vercel-style SKILL.md format as proof-of-concept. Effort: 30-60 min. Compatibility: Claude Code natively reads YAML frontmatter.

**Pilot ranking refresh post-v51:**
1. rowboat v1 vault pilot (4 weeks)
2. claude-hud install (5 min)
3. spec-kit methodology (1-2 weeks)
4. claude-howto self-onboarding (13h weekend)
5. OMC multi-runtime (1 weekend)
6. pi-mono coding agent alt (2-4h)
7. aidevops AGENTS.md template (6-8h)
8. **Vercel SKILL.md format adoption (30-60 min single-skill / 3-4h full vault)** — NEW v51

### Direct utility (MEDIUM for AGENTS.md template)

**4-template AGENTS.md ensemble for vault CLAUDE.md refactor:**
- 22a monolithic (gh-aw v48 / spec-kit v17)
- 22c authoritative-with-shim (aidevops v47) — most-aligned with vault scaling needs
- **22d identical-mirror (Vercel v51) NEW** — NOT recommended for vault (no need for both files)

### v27 diagnostic HIGH bundle escalation

**31 sessions deferred post-v51** (5-session threshold per v2.1 operator-facing-backlog discipline; 6.2× overrun). Vercel v51 contributes:
- 4-template AGENTS.md ensemble for item #1 (vault CLAUDE.md refactor)
- SKILL.md format reference for `05 Skills/` directory expansion (related to item #1 but separable scope)

**STRONGLY RECOMMENDED:** Execute v27 diagnostic HIGH bundle before v52 (~6-8h session).

---

## 10. Next wiki candidates (strategic selection for pattern-strengthening)

### High-value next-wiki candidates

1. **2nd corporate-narrow-skill-library** (Cloudflare, AWS, Supabase, Stripe published a similar skill collection?) — would test Vercel sub-archetype at structural-N=2
2. **2nd 22d identical-mirror wiki** — would promote Pattern #22 22d to confirmed sub-variant
3. **2nd forward-citation-then-wiki opportunity** (any future v52+ wiki subject was cited in some prior v1-v51 wiki?) — would promote Pattern #57 57c to confirmed sub-variant
4. **3rd 29-absent-3 wiki** — would strengthen Pattern #29 29-absent-3 promotion-candidate (already at N=2 promotion-ready)
5. **Pattern #18 MCP corporate-official-tier observation enrichment** — wiki where corporate-official does adopt MCP-as-Layer-1 (counter to current Vercel + gh-aw observations)

### Strategic discipline

Default to **strengthen-over-discover** — prefer wikis that strengthen existing patterns rather than introduce many new candidates. Recent 15-streak v37-v51 demonstrates this discipline.

---

## 11. Strategic decision point (consolidation recommendation + backlog escalation)

### Pattern Library state

- **Library health: UNPRECEDENTED** — ratio 0.474:1 preserved post-v51 direct updates
- **Promotion candidates: 9 accumulated** (post-v50 mini-audit + v51)
- **Structural maturity threshold reached at v36 mini-audit; preserved through v51**

### Recommendations (priority order)

1. **PRIORITY 1 (BLOCKING-RECOMMENDATION ESCALATING):** Execute v27 diagnostic HIGH bundle before v52 — 31 sessions deferred (6.2× threshold). Vault CLAUDE.md refactor item #1 has 4-template ensemble post-v51. **STRONGLY RECOMMENDED 6-8h session.**
2. **PRIORITY 2:** Mini-audit at next operator-trigger to action 9 accumulated promotion-candidates (#22 22d / #57 57c / #29 29-absent-3 / #29 AGPL / #50 50b / #66 OT / #18 4-layer / #22 22c / #47 retirement). Estimated 30-60 min mini-audit.
3. **PRIORITY 3:** Optional Storm Bear pilot #8 — convert `llm-wiki-routine-v2.1.md` to Vercel-style SKILL.md format (30-60 min single-skill pilot).
4. **PRIORITY 4:** Continue wiki-building if no consolidation/pilot urgency. v52 candidate selection should bias toward strengthening (see section 10 high-value candidates).

### Override

Operator can override priority 1 by saying "proceed despite v27 backlog" — routine will continue. Honor with discipline notation in v52 iteration log.

---

## 12. Scorecard

| Dimension | Score | Notes |
|---|---|---|
| Novelty | 8/10 | 15 corpus-firsts; 2 NEW sub-variants registered (22d + 57c); Pattern #17 variant 5 N=3 milestone |
| Pilot-relevance for Storm Bear | 7/10 | HIGH SKILL.md format reference; MEDIUM 4-template AGENTS.md ensemble; LOW direct usage of React/Next.js skills |
| Pattern-contribution | 9/10 | 4 promotion-candidate strengthenings (#17 variant 5 N=3 / #22 22d NEW / #57 57c NEW / #29 29-absent-3 N=2 promotion-ready); 6 strengthening data points |
| Velocity | 7/10 | ~3h 35min — slightly above ~2h plateau due to multi-pattern harvest scope; within tolerance |
| Quality | 9/10 | All Phase 5 fact-verification clean; consolidation-forward discipline preserved 15-streak; cross-references mandatory met |

**Overall:** 8/10 — solid strengthening-and-sub-variant-harvest wiki; library reaches deeper maturity; vault ensemble enrichment.

---

## 13. Primitive-count check (v2.1 informal discipline)

- **Probed primitive-count:** ~13 across 4 categories (7 skills + 4 distribution surfaces + 2 governance files [AGENTS.md = CLAUDE.md identical-mirror = 1 content unit] + 1 build package)
- **Fits 4-entity format cleanly?** YES — GREEN tier
- **Follow-up deep-dive wikis recommended:** None at v51 — standard 4-entity format absorbed all primitives without compression
- **Operator decision:** Accept (no follow-up wikis needed)

**Velocity confirmation:** GREEN baseline ~2h held within tolerance (~3h 35min for multi-pattern harvest scope).

---

End of v51 iteration log.
