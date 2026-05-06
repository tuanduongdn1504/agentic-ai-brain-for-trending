# Entity 2 — Multi-citation README: BMAD + GSD + Spec-Kit anti-pattern foils

## 1. Identity

The **single most novel structural finding** in the v57 wiki: mattpocock/skills README cites 3 distinct prior Storm Bear corpus subjects in a single artifact, framed as "approaches that take away your control."

**Verbatim citation** (README paragraph 3):

> "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve."

This is **corpus-first multi-frontend in-corpus reference** — 3 prior wiki subjects cited in single sentence as anti-pattern positioning.

## 2. Pattern #57 57c forward-citation-then-wiki — strongest evidence to date

### Prior 57c instances (post-v56-mini-audit confirmed at N=3)

| Cited subject | Citing subject | Gap | Tier-pair |
|---|---|---|---|
| multica v15 | vercel-labs v51 | 36 wikis | T2 → outside-scope |
| OMC v27 | omo v52 | 25 wikis | T1 → T1 |
| Skyvern v24 | n8n v56 | 32 wikis | T1 → T2 |

### v57 NEW instances (3 simultaneous)

| Cited subject | Citing subject | Gap | Tier-pair |
|---|---|---|---|
| BMAD-METHOD v11 | mattpocock/skills v57 | 46 wikis | T1 → T1 |
| get-shit-done v5 + gsd-2 v54 (named "GSD") | mattpocock/skills v57 | 52 / 3 wikis | T1 → T1 |
| spec-kit v17 | mattpocock/skills v57 | 40 wikis | T1 → T1 |

### Multi-frontend extension significance

Prior 57c instances were 1-citing-subject ↔ 1-cited-subject pairs. v57 introduces:

- **Multi-frontend variant**: 1-citing-subject ↔ 3-cited-subjects in single sentence
- **Mean gap across 3 v57 instances**: (46 + 52 + 3 + 40) / 4 = 35.25 wikis (or 46/52/40 = 46 mean if treating GSD as v5)
- **Range across all 6 confirmed 57c instances**: 3-52 wikis
- **Corpus 57c total**: 6 instances (3 prior + 3 v57 new); promotion-candidate for **57c-multi-frontend sub-variant** at next mini-audit

### Promotion-candidate analysis at next mini-audit

**Option A — 57c-multi-frontend sub-variant (NEW within 57c)**
- Trigger: 1 instance at N=1 (mattpocock/skills v57 single occurrence)
- Stale-flag: register at N=1 with v62 / v67 cadence
- Conservative-discipline default

**Option B — formal-statement extension on 57c**
- "57c forward-citation-then-wiki now N=6 across T1 (4) + T2 (2) + outside-scope (1) tier-pairs"
- Strengthens existing 57c without new sub-variant

**Option C — register multi-citation as standalone candidate**
- REJECTED per consolidation-forward discipline: 57c sub-variant absorbs the observation cleanly

**Recommended path:** Option A (57c-multi-frontend sub-variant N=1 stale-flagged) + Option B (formal-statement extension) at next mini-audit — 2-action pattern matching post-v56 mini-audit conservative-discipline precedent.

## 3. Anti-pattern positioning structure

The 3 cited subjects are **classified by author as a single methodology-class** ("approaches like GSD, BMAD, and Spec-Kit"). Storm Bear corpus-internal classification of these subjects:

| Subject | Corpus tier | Corpus archetype | Author's grouping |
|---|---|---|---|
| **GSD v5** | T1 | Solo-individual (Mike) | "approach that owns the process" |
| **gsd-2 v54** | T1 | gsd-build org (8-repo monorepo + Pi-SDK substrate) | (same name "GSD" — author may not distinguish) |
| **BMAD-METHOD v11** | T1 | Methodology-feature-framework | "approach that owns the process" |
| **spec-kit v17** | T1 | Microsoft corporate-official + 9-article constitution | "approach that owns the process" |

**Ambiguity:** Author's "GSD" reference does not distinguish between gsd v5 (solo) and gsd-2 v54 (gsd-build org). Both are corpus subjects; v54 is more recent + more substantial. **Conservative attribution: "GSD" = both v5 and v54 jointly.**

## 4. Corpus implications of anti-pattern grouping

### Methodology-class signal

Author's grouping suggests a **"process-owning frameworks" meta-category** in agent-tooling space:

- GSD = task-tracker + opinionated workflow
- BMAD = methodology-feature-framework (Brain + Mind + Action + Decision → BMAD)
- spec-kit = 9-article-constitution-driven SDD

Mattpocock/skills positions itself as **anti-process-owning** — small + composable + author-controlled.

This grouping is **corpus-internal classification by external author**. Storm Bear corpus had not previously grouped these 3 subjects together; mattpocock/skills v57 introduces this classification as observation. Pattern Library could optionally formalize "process-owning-meta-frameworks" sub-category at future audit if 2+ external authors converge on similar grouping.

### Anti-pattern-as-positioning trend

This continues a corpus pattern where new subjects position against existing corpus subjects:
- v56 n8n positioned against Zapier/Make (non-corpus)
- v55 automate-faceless-content abandoned-author (negative-corpus-cautionary)
- **v57 mattpocock/skills positions explicitly against 3 prior corpus subjects**

Counter-pattern observation: corpus subjects are increasingly aware of (or cited by) other corpus subjects, suggesting the methodology-tooling space is consolidating into a discoverable cluster (which Storm Bear corpus reflects).

## 5. Storm Bear vault implications

### Citation-discoverability validates corpus selection

If 60K-star repo's author cited 3 of Storm Bear's prior 57 wiki subjects as the "process-owning" anti-pattern, Storm Bear's corpus selection is **validated as covering the canonical methodology-tooling cluster**. This is structurally similar to v27 OMC citing v1 + v2 corpus subjects.

### Vault-skill-coherence alignment

mattpocock/skills positions as anti-process-owning + small-composable-skills. Vault routine v2.1 is **also small-composable** (7-phase routine + 6 promotion criteria + sub-routines like mini-audit / brain-setup). This is structural alignment — vault is in the **same anti-process-owning camp** as mattpocock/skills, even though vault uses different specific skill primitives.

### Pattern #57 confirms corpus-self-aware status

Post-v57, Pattern #57 has 6 confirmed 57c instances + 4 prior 57a/b/d sub-variants. Recursive corpus reference is now **statistically common** in the corpus (~10% of wikis cite or are cited by another corpus subject). This validates Karpathy LLM Wiki pattern — the corpus is becoming **self-referentially coherent**, which is the design goal.

## 6. Pattern Library recommendation summary

| Action | Rationale |
|---|---|
| Register **57c-multi-frontend sub-variant N=1** stale-flagged v62 / v67 | Mattpocock/skills v57 is 1st multi-frontend 57c instance; flag for v62 review |
| Extend **57c formal-statement** to "N=6 across T1+T2+outside-scope tier-pairs" | Reflects 3 new v57 instances |
| Defer **process-owning-meta-frameworks meta-category** | Single external author grouping; needs 2nd author convergence (v60+ trigger) |
| Validate **corpus selection coverage** | 3 of 57 subjects cited by external 60K-star repo = strong selection signal |

## 7. Cross-wiki references (within entity)

- v15 multica / v51 vercel-labs / v27 OMC / v52 omo / v24 Skyvern / v56 n8n — prior 57c instances
- v11 BMAD-METHOD / v5 get-shit-done / v54 gsd-2 / v17 spec-kit — v57 NEW citations
- v50 awesome-claude-skills / v51 agent-skills-of-vercel — sibling skills-collections (NOT cited by mattpocock/skills; absence informative)

## 8. Open question for next mini-audit

**Q1.** Should "GSD" in mattpocock/skills README be attributed to v5 (original) or v54 (successor) for Pattern #57 57c counting? **Recommended resolution:** count as **both**, treating mattpocock/skills v57 as multi-citing 4 prior subjects (v5 + v11 + v17 + v54). This makes 57c v57 contribution = 4 instances within single README, the most multi-frontend any 57c-citing-subject has produced.

If resolution accepts v5+v54-as-distinct: 57c grows to N=7 confirmed (3 prior + 4 v57). 1st N≥7 sub-variant within Pattern #57 would warrant formal-statement extension to "57c is corpus-densest 57x sub-variant."
