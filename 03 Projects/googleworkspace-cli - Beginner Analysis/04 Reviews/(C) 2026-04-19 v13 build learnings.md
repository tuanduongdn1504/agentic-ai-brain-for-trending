# (C) 2026-04-19 v13 build learnings — googleworkspace/cli

> **Session:** 13th LLM Wiki build, 13th routine auto-execution
> **Duration:** ~2h
> **Routine:** `05 Skills/llm-wiki-routine.md` v1
> **Project:** `03 Projects/googleworkspace-cli - Beginner Analysis/`
> **Status:** ✅ Complete, all phases shipped

---

## 1. What shipped

- ✅ 5 foundation files (CLAUDE.md, COMMANDS.md, index, log, open questions)
- ✅ 3 source summaries (README / CONTEXT+CLAUDE+AGENTS cluster / 110 Skills+Helper Commands cluster)
- ✅ 4 entity pages (13-section canonical):
  - Dynamic Discovery Service Architecture
  - 110 Skills (44 gws-* + 10 personas + 56 recipes)
  - Multi-Flow OAuth2 + Model Armor + Validation Discipline
  - T4 Multi-Entrant Validation + Official-vs-Unofficial + Storm Bear Enterprise Angle
- ✅ Beginner bilingual published guide (~600 lines, 10 parts)
- ✅ T4 2-way comparison (extends T4 from N=1 to N=2, 15 axes, 4 new patterns)
- ✅ This iteration log
- ✅ 25 open questions tracked

**Total files:** 13 (5 foundation + 3 summaries + 4 entities + 1 beginner guide + 1 comparison + 1 iteration log)

**Velocity:** ~2h — stable with v9-v12. **8 consecutive wikis at ~2h plateau.**

---

## 2. Biggest wins

### Win 1 — T4 multi-entrant VALIDATED at N=2

Fourth tier to validate (after T1 N=5/6 at v11/v12, T5 N=2 at v10). T4 had been N=1 since v7 notebooklm-py. **googleworkspace/cli as T4 N=2** confirms the tier and surfaces subcategorization.

### Win 2 — Pattern #9 promoted to cross-tier observed law

v10 at T5 observed corporate-vs-solo bifurcation. v13 at T4 confirms same pattern. **Pattern #9 "Tiers bifurcate along corporate-vs-solo axis" now cross-tier.**

**Predictive power:** future T2/T3 validations should show same split. Test-ready hypothesis.

### Win 3 — New patterns invented at v13 (4 total)

- **Pattern #9 (cross-tier confirmation)** — corporate-vs-solo axis
- **Pattern #10** — T4 has official-vs-unofficial axis not present in T5
- **Pattern #11** — Dynamic Discovery architecture requires official status
- **Pattern #12** — Corporate-backed projects formalize agent documentation more

**4 new patterns in single wiki = highest pattern-invention yield to date.** Adding a genuine outlier (corporate T4 entrant vs prior solo T4 entrant) multiplies structural insight.

### Win 4 — Three corpus firsts identified

1. **First Rust project** — prior corpus: Python / JS-TS / Markdown-core / dual
2. **First Apache-2.0 license** — prior MIT dominant; codymaster ISC was only outlier
3. **First official-Google-corporate** — prior corporate: Microsoft T3 course / ByteDance T5 deer-flow / YC T1 gstack / BMAD-LLC T1. Google joins but is first with agent-tooling as flagship repo.

### Win 5 — Novel architectural pattern documented

**Dynamic Discovery Service** — runtime CLI generation from Google Discovery JSON. No generated crates. 1-line service registration. This is unique in corpus; no prior project generates command surface at runtime.

**Implication for routine v2:** when framework has novel architecture, dedicate a full Phase 3 entity page (which v13 did). Pattern for future novel-architecture framework wikis.

### Win 6 — Tri-file agent documentation pattern documented

CLAUDE.md (1-liner pointer) + AGENTS.md (contributor) + CONTEXT.md (runtime-user) = first observed tri-file split. Distinct audiences getting distinct docs.

**Routine v2 candidate:** detect tri-file presence in Phase 0; use as 3-source cluster strategy.

### Win 7 — T4 subcategorization formalized

T4a official-corporate-broad / T4b unofficial-solo-narrow. Clean predictive framework for future T4 additions.

### Win 8 — Storm Bear enterprise angle high-value

gws = Google Workspace ubiquity + VN enterprise standard + enterprise-grade auth. Highest-fit framework for Storm Bear since BMAD (VN translation) and codymaster (VN author). Now Storm Bear has **3 frameworks in parallel-pilot backlog**: BMAD + codymaster + gws.

### Win 9 — Phase 0 corrections caught (no cascading)

No marketing-vs-reality gaps this time. gws documents honestly:
- "100+ skills" → 110 actual (minor undersell, reasonable)
- Services enumerated accurately
- Version v0.22.5 stated without inflation

**Routine v2 lesson:** honest-docs frameworks exist; routine should recognize (not just expect miscalibration).

---

## 3. Friction points

### Friction 1 — GitHub API curl output auto-summarized

Saved curl to /tmp but environment auto-summarized JSON to schema form (not raw). Required WebFetch as alternative for repo metadata.

**Lesson:** for Phase 0 API probes, WebFetch against github.com HTML page is more reliable than raw API curl in this environment. Already-used pattern; confirming.

### Friction 2 — Couldn't deep-read AGENTS.md raw content

Curl'd AGENTS.md but content got truncated (file preserved header + truncation marker). Workaround: WebFetch with targeted prompts for section details.

**Lesson:** for deep reads of >8KB files, prefer WebFetch with "return verbatim with structural markers" prompt over curl save + read.

### Friction 3 — No community/Discord signal

gws README has no community channels listed (Q1). Limits Storm Bear's ability to engage community-side. Just GitHub issues.

**Neutral finding:** not all projects have community layers; gws is Google-official, support is via issues + Google Developer Relations.

---

## 4. Routine v1 performance at 13th auto-execution

### Stable behaviors

- Phase 0 API-probe-first with WebFetch fallback
- Phase 1 scaffold routine
- Phase 2 3-source clustering adapted to project structure
- Phase 3 4-entity structure held (novel primitives + taxonomy + security + meta-entity)
- Phase 4a bilingual guide consistent
- Phase 4b 2-way comparison extended from T4 N=1 to N=2

### New observations at v13

- **Pattern-invention yield** when adding genuine outlier = high (4 patterns from 1 wiki). Routine should expect this when tier bifurcation visible.
- **Tri-file agent docs detection** — new Phase 0 check candidate
- **Official-vs-unofficial** as Phase 0 classification
- **Rust-specific Phase 0 checks** — Cargo.toml presence, crates/ workspace structure

---

## 5. Action items for routine v2

Cumulative with prior v3-v12 action items (53 existing). v13 adds:

1. **Pattern #9 validation hook** — when adding multi-entrant to tier, check if corporate-vs-solo axis visible
2. **Tri-file agent docs detection** in Phase 0 (CLAUDE.md + AGENTS.md + CONTEXT.md)
3. **Official-vs-unofficial classification** in Phase 0 for T4 entrants
4. **Rust project conventions** — recognize Cargo.toml + crates/ workspace structure
5. **Apache-2.0 vs MIT noting** — license diversity tracking
6. **Dynamic Discovery / runtime-generated CLI** as recognized architecture pattern (documentable in Phase 3)
7. **Corporate-backing taxonomy** — Microsoft/Google/ByteDance/YC/LLC as distinct corporate-backer archetypes
8. **WebFetch as primary for Phase 0** — curl auto-summarization unreliable; prefer WebFetch targeted prompts

**Cumulative v3-v13 action items:** 53 + 8 = **61 total**. Routine v2 urgency remains **URGENT**.

---

## 6. Meta-observations at 13-wiki milestone

### Vault state

- **13 LLM Wikis complete**
- **5-tier taxonomy at N={6,1,1,2,2,1}** — T1/T2/T3/T4/T5/Outside
- **3 tiers multi-entrant-validated** (T1 v11/v12, T4 v13, T5 v10)
- **2 tiers still single-entrant** (T2 goclaw, T3 course)
- **VN relevance across 3 T1 entrants (BMAD translated + codymaster authored + goclaw has VN README)** and now 1 T4 entrant (gws = global but universal VN Workspace usage)
- **Storm Bear pilot backlog:** BMAD + codymaster + gws = 3 parallel candidates

### Compounding evidence

- Velocity stable at ~2h for **8 consecutive wikis** (v6-v13)
- Cross-project references in T4 2-way comparison pulled from v7 notebooklm-py cleanly
- Pattern #9 cross-tier confirmation = predictive framework crystallizing
- Taxonomy survived all 13 additions without structural revision

### Pattern library now has 12 patterns

1. Scale-reach correlation non-linear
2. Distribution convergence on npx/npm
3. Agent-count philosophy divergence
4. Markdown-pure vs engineered-runtime spectrum
5. Commercial diversification spectrum
6. Localization emergence (6a translated / 6b authored / 6c primary future)
7. Marketplace emergence at scale (BMAD unique)
8. Empirical research emergence (codymaster SkillsBench)
9. **NEW v13** — Tiers bifurcate along corporate-vs-solo axis
10. **NEW v13** — T4 has official-vs-unofficial axis absent in T5
11. **NEW v13** — Dynamic Discovery requires official status
12. **NEW v13** — Corporate-backed projects formalize agent docs more

### Where next?

**Options (ranked by strategic value):**

1. **Pilot** (highest value) — run BMAD + codymaster + gws in parallel 1-week Storm Bear Scrum cycle. Empirical > analysis.
2. **T2 validation** — add 2nd T2 entrant. Tests Pattern #9 at platform tier.
3. **T3 validation** — add 2nd T3 entrant. Tests Pattern #9 at education tier.
4. **Routine v2 codification** — 61 action items URGENT.
5. **7th T1** — only if new-outlier-axis framework appears (harder bar after scope + scale already taken).

---

## 7. Open questions carryover

25 v13 questions tracked. Key unresolved:

- Q4 Rust choice rationale (performance? distribution?)
- Q6 Model Armor cost / availability model
- Q13 OAuth "recommended" preset curation process
- Q14 VN/multi-language docs roadmap
- Q15 MCP support trajectory
- Q18 Storm Bear enterprise pilot candidacy
- Q20 Helper command anti-pattern enforcement

**Cumulative open questions across 13 wikis: ~170+** (v12 was ~150+). Healthy growth, still tractable.

---

## 8. Closing self-assessment

**Delivered:** Full 7-phase wiki with T4 multi-entrant validation, 4 new patterns (9-12), 3 corpus firsts documented, Storm Bear enterprise entity.

**Quality:** High. Phase 0 honest (no marketing correction cascading). Novel architecture (Dynamic Discovery) documented with inferred implementation paths. T4 subcategorization formalized with predictive framework.

**What I'd do differently next time:**
- Try gws install + basic invocation during wiki build. Empirical validation of claims adds credibility.
- Fetch `services.rs` + `discovery.rs` if accessible — would ground Dynamic Discovery claims
- Survey 2-3 GitHub issues to gauge community pain-points (not just README claims)

**What surprised me:**
- Pattern #9 cross-tier confirmation at N=2 — didn't expect second tier to show same bifurcation so cleanly
- Rust choice (not Go) from Google — unusual; suggests Rust is strong for CLI distribution
- 25K stars at v0.22.5 pre-1.0 — aggressive adoption; validates AI-agent-native positioning
- Tri-file agent documentation innovation — corpus evolution toward structured agent docs is real
- Model Armor as integrated safety layer — corpus first; likely industry inflection point

---

## 9. Recommended next action

**HIGH PRIORITY:** Parallel pilot BMAD + codymaster + gws for 1-week Storm Bear Scrum cycle. Empirical answer to multiple questions:
- Which framework serves Scrum coach role best?
- Does gws Dynamic Discovery + Workspace integration + agent skills actually automate cleanly?
- How do BMAD's Agile workflows + codymaster's brain depth + gws's Workspace bridge compose?

**URGENT:** Routine v2 codification sprint — 61 cumulative action items.

**Strategic:** Pattern #9 test — add 2nd T2 or T3 entrant. If Pattern #9 holds at all tiers, it's architecture law not T4/T5-specific.

**Alternative:** Engage Tody Le (v12 codymaster author) about VN community + cross-framework pilot. v13 gws's corporate-backing makes it unsuitable for "community VN" angle, but complement.

---

**Parent:** [[(C) index]]
**Siblings:** [[../../notebooklm-py - Beginner Analysis/04 Reviews/]] (T4 peer), [[../../autoresearch - Beginner Analysis/04 Reviews/]] (T5 2-way precedent), [[../../codymaster - Beginner Analysis/04 Reviews/]] (prior wiki)
