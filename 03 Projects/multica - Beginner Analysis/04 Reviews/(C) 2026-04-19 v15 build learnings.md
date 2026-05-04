# (C) v15 multica — build learnings + routine v2 action items

> **Date:** 2026-04-19
> **Wiki:** multica (15th LLM Wiki in corpus)
> **Routine:** `llm-wiki-routine` v1 (15th auto-execution)
> **Duration:** ~2h (within velocity plateau v6-v15)
> **Parent:** [[(C) index]]

---

## 1. Milestones hit at v15

### Corpus-level milestones

- ✅ **T2 multi-entrant validated** (N=2: goclaw v4 + multica v15)
- ✅ **4/5 tiers multi-entrant-validated** (only T3 remains single-entrant)
- ✅ **Pattern #9 refined to tier-dependent** — platform-tier homogeneity hypothesis
- ✅ **3 new Pattern candidates registered** (#16 skill-lock, #17 ecosystem-layer orgs, #18 agent-runtime standardization)
- ✅ **Cross-wiki ecosystem signal detected** — OpenClaw in 3 wikis, Hermes in 2, nextlevelbuilder contributes cross-project
- ✅ **Velocity plateau 10 consecutive wikis** (~2h/wiki v6-v15)
- ✅ **15 wiki milestone** — significant corpus mass for pattern mining

### multica-specific corpus-firsts

- First **Electron desktop app**
- First **skills-lock.json** (dependency-locked skill manifest)
- First **pgvector/Postgres 17** (vector-capable DB)
- First **Turborepo** (monorepo orchestration)
- First **Anthropic skills registry** import
- First **Vercel agent-skills** import
- First **hybrid local-daemon + cloud-orchestration** architecture
- Broadest BYO-agent list (8 models)

## 2. Phase breakdown (~2h total)

| Phase | Duration | Notes |
|-------|----------|-------|
| 0: Pre-flight API probe | ~15 min | WebFetch README + README.zh-CN + metadata; verified 16.2K stars |
| 1: Scaffold | ~10 min | CLAUDE.md + COMMANDS.md + index + log + open questions |
| 2: Source summaries (3) | ~35 min | README cluster + CLAUDE+AGENTS+CONTRIBUTING cluster + Skills+Architecture+skills-lock cluster |
| 3: Entity pages (4) | ~40 min | Linear-Analog + Electron + skills-lock + T2-Pattern9-Storm-Bear |
| 4a: Beginner guide | ~15 min | Bilingual VN/EN, 12 parts |
| 4b: T2 2-way comparison | ~20 min | 20-axis compare + Pattern #9 refinement formal statement |
| 5: Iteration log | ~5 min | This file |
| 6: Vault sync | ~5 min | Root CLAUDE.md + GOALS.md |

## 3. What worked

### Routine execution

- **WebFetch-first** continued to serve cleanly for large docs (21KB CLAUDE.md, 11KB CLI_AND_DAEMON)
- **Cluster summary strategy** — 3 clusters covered 10+ source files cleanly
- **Cross-wiki reference proactive** — detected OpenClaw/Hermes/nextlevelbuilder before Phase 4b, seeded into entity pages
- **Pattern #9 test discipline maintained** — 7-criteria fit check explicit for both T2 entrants
- **13-section canonical format** — applied to all 4 entities without format iteration

### Unique value added

- **Ecosystem-layer observation** (nextlevelbuilder cross-project) = novel corpus insight unlocked at v15
- **Pattern #16 (skills-lock) registered** = first-mover pattern capture
- **Pattern #17 (ecosystem-layer orgs) registered** = meta-observation about org archetypes
- **Pattern #18 (agent-runtime standardization) registered** = cross-wiki convergence pattern
- **Pattern #9 refinement formal** = tier-dependent resolution with 55% probability

## 4. What didn't work / friction

### Minor friction

- **skills-lock.json not directly accessible at first** — had to WebFetch raw content; small overhead
- **Electron + Next.js + Go + pgvector stack breadth** — required careful pacing in cluster summary to avoid stack-dump
- **"10 hires won't be human" tagline** — took careful handling to contextualize ethically without dismissing tool utility

### Recurring friction from v11-v14

- **Still no automated cross-wiki search tool** — detected OpenClaw/Hermes/nextlevelbuilder manually by remembering prior wikis
- **No automated Pattern library update** — still manual tracking in GOALS.md version log
- **No automated entity-page template** — still writing 13 sections from memory each time

## 5. Routine v2 action items (new at v15)

### A. Cross-wiki search tool (ESCALATED — was urgent at v13, now CRITICAL)

**Need:** Grep-like search across all 15 project wikis for pattern detection.

**Action:** Build `llm-wiki-grep` skill that searches across `03 Projects/*/02 Wiki/` and surfaces matches with citations. Would have automated OpenClaw/Hermes/nextlevelbuilder detection.

### B. Pattern library auto-update hook

**Need:** When new Pattern candidate registered in iteration log, propagate to GOALS.md + root CLAUDE.md automatically.

**Action:** Add Phase 6 substep that parses iteration log `### New candidates` section and updates Pattern Library entries.

### C. Entity page template scaffolding

**Need:** Fresh entity pages should start from template with 13-section headers pre-filled.

**Action:** Add `05 Skills/llm-wiki-entity-template.md` as ingestion artifact to be copied.

### D. Skills-lock pattern for Storm Bear vault (NEW)

**Need:** Storm Bear vault own skills/templates/cross-project references could benefit from skills-lock.json pattern.

**Action:** Evaluate `skills-lock.json` at Storm Bear root. Lock `llm-wiki-ingest` + `llm-wiki-routine` + `brain-setup` + `new-project` versions with SHA-256 integrity.

### E. Ecosystem-layer tracking (NEW)

**Need:** Track which orgs publish across multiple corpus projects (ecosystem-layer detection).

**Action:** Add section to root `GOALS.md` → "Ecosystem-layer orgs observed" with nextlevelbuilder (goclaw + multica contributor) + others as detected.

### F. Runtime-standard tracking (NEW)

**Need:** Track de facto agent-runtime names appearing across frameworks.

**Action:** Add section to root `GOALS.md` → "Agent runtime standards observed" with OpenClaw (3 wikis), Hermes (2 wikis), etc.

### G. Autonomy-framing index (NEW)

**Need:** Corpus now has 3+ autonomy-maximum framings (paperclip "zero-human", multica "10 hires won't be human", deer-flow SuperAgent). Should track as formal pattern axis.

**Action:** Add Autonomy-framing Spectrum entity at vault root; each new wiki scores on spectrum.

### H. Desktop-app precedent flag (NEW)

**Need:** multica first Electron in corpus. Future wikis with desktop apps should reference this precedent.

**Action:** Add flag in Phase 0 API probe: "Does project have native desktop app?" → if yes, cross-reference multica architecture entity.

## 6. Total action items accumulating

- v3-v14 cumulative: 60+ items
- v15 additions: 8 items (A-H above)
- **Total routine v2 backlog: 68+ items**

**Status escalation:** Routine v2 upgrade URGENT → **CRITICAL** at v15. Consider pausing new wikis to execute routine v2 refactor.

## 7. Meta-observations at 15-wiki milestone

### Corpus mass sufficient for structural inference

15 wikis across 5 tiers with multi-entrant validation in 4 tiers gives **statistical body** for structural claims:

- Pattern #9 (bifurcation) now refineable based on tier
- Autonomy-framing spectrum stable with 3+ data points
- Ecosystem-layer orgs detectable cross-wiki
- Runtime-standards emerging detectable cross-wiki
- Community-platform archetype confirmed homogeneous at T2

### Pattern diversity stabilizing

Pattern library at 15 wikis:
- **12 confirmed** patterns
- **6 candidates** (was 3 pre-v15; +3 from v15)
- Most patterns mineable at N≥2 in a tier

**Insight:** Wiki corpus is entering phase where new wikis **validate existing patterns** more than **discover new ones**. Pattern discovery rate will slow; validation rate accelerates.

### Compounding evidence at v15

- Routine execution stable across 5 tiers + outside-scope
- Velocity plateau proves pattern mature
- Cross-wiki citations dense (15 × 14/2 = 105 possible pairs, ~50 used)
- Entity-page compounding observed (new entities reference 5+ prior wikis)

### Karpathy meta-cycle continues

multica's skills-lock + Anthropic skill-registry import = Anthropic publishes official skill registry. This validates Karpathy's LLM Wiki philosophy ripples outward — Anthropic itself now curates agent-skill knowledge.

## 8. v15-specific unique findings worth preserving

1. **OpenClaw emerging runtime standard** — 3 wikis mention it
2. **Hermes name reuse** — 2 wikis mention it (possibly Nous Research Hermes)
3. **nextlevelbuilder ecosystem-layer** — publishes goclaw + contributes ui-ux-pro-max-skill
4. **Anthropic has `anthropics/skills` repo** — official skill registry
5. **Vercel has `vercel-labs/agent-skills` repo** — agent-skills investment
6. **shadcn skill present in multica** — UI components as skill (novel framing)
7. **Linear-analog UX** emerging as agent-platform paradigm
8. **Electron + pgvector + Turborepo combination** — tech stack novelty
9. **skills-lock.json format version 1** — evolution anticipated
10. **Multi-workspace vs multi-tenant** — architectural vocabulary divergence between goclaw + multica

## 9. Storm Bear vault impact

### Immediate (actionable after v15)

- Update root `GOALS.md` with Pattern #9 refinement + 3 new candidates
- Update root `CLAUDE.md` with multica project entry
- Flag routine v2 as CRITICAL in next weekly review

### Medium-term (within 2 weeks)

- Evaluate skills-lock.json for Storm Bear vault own skills
- Document ecosystem-layer orgs list (nextlevelbuilder + future)
- Document agent-runtime-standards list (OpenClaw + Hermes + future)

### Long-term (within 1 month)

- Execute routine v2 refactor (68+ action items)
- Reconsider T3 multi-entrant strategy (only tier remaining)
- Pilot multica and/or goclaw personally

## 10. Next wiki candidates

Criteria for 16th wiki:
- **Would validate existing patterns** (prefer) OR
- **Would add novel dimension** (Pattern #19+ candidate)

Candidates on backlog:
- More T3 candidates (agent-as-education — only tier at N=1)
- 3rd T2 entrant (would test Pattern #9 refinement strongly)
- Non-English-region agent platforms (beyond CN/VN)
- Enterprise-first platform (contrast with community-platform T2 homogeneity)

## 11. References

- Parent: [[(C) index]]
- Prior iteration log: `../../paperclip - Beginner Analysis/04 Reviews/(C) 2026-04-19 v14 build learnings.md`
- Published: `../03 Published/(C) multica - Huong dan cho nguoi moi.md` + `(C) Tier 2 2-way comparison.md`
- Root GOALS.md version log entry: pending v15 append

---

**v15 complete. Pattern #9 refined. 3 new pattern candidates. 4/5 tiers validated. Routine v2 upgrade CRITICAL. Next wiki: choose by pattern-validation vs pattern-discovery tradeoff.**
