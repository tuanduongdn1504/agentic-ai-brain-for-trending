# (C) Tier 1 "Agent-as-Assistant" 8-way Comparison — 8 T1 frameworks

> **Purpose:** Extend T1 validation to N=8 (largest tier). Test Pattern #9 Resolution D further. Document Pattern #20 MAJOR REVISION. Document Pattern #19 3-archetype refinement.
> **Parent:** [[(C) index]]
> **Entrants:**
> - ECC v1 (affaan-m — solo community)
> - Superpowers v2 (Jesse Vincent — solo community)
> - gstack v3 (Garry Tan — founder-personal YC)
> - GSD v5 (TÂCHES — community + SDD)
> - BMAD v11 (BMad Code LLC — formalized)
> - codymaster v12 (Tody Le — VN-authored solo)
> - spec-kit v17 (GitHub — corporate-official)
> - **agency-agents v18 (msitarzewski — solo-enterprise-scale + Reddit-viral-origin)**
> **Status:** ✅ Phase 4b deliverable, v18

---

## 1. Why this comparison

T1 "Agent-as-assistant" progression:
- v1: N=1
- v2: N=2
- v3: N=3
- v5: N=4
- v11: N=5 (closed)
- v12: N=6 (re-opened)
- v17: N=7 (+ first corporate)
- **v18: N=8 (+ first solo-enterprise-scale)**

**Each new T1 addition extends comparison.** v18 extends v17's 7-way to 8-way.

## 2. Summary table — 24-axis comparison

| # | Axis | ECC v1 | SP v2 | gstack v3 | GSD v5 | BMAD v11 | codymaster v12 | spec-kit v17 | **agency-agents v18** |
|---|------|--------|-------|-----------|--------|----------|----------------|--------------|------------------------|
| 1 | **Stars** | ~5K | ~8K | ~6K | ~6K | 45K | 38 | 89.2K | **82.9K** |
| 2 | **Forks** | low | low | low | low | 5.3K | 21 | 7.7K | **13.2K** |
| 3 | **License** | MIT | MIT | MIT | MIT | MIT | ISC | MIT | MIT |
| 4 | **Primary lang** | TS | TS | shell | shell | TS | TS | Python | **Shell 96.8%** |
| 5 | **Author/org** | affaan-m | Jesse Vincent | Garry Tan / YC | TÂCHES | BMad Code LLC | Tody Le | GitHub | **msitarzewski** |
| 6 | **Archetype** | Solo community | Solo community | Founder | Community | LLC | Solo VN | Corporate | **Solo-enterprise-scale** |
| 7 | **Scale tier** | Medium | Medium | Medium | Medium | Large | Small | X-Large | **X-Large** |
| 8 | **Methodology** | Feature | TDD 7-stage | Virtual team | SDD | BMM | 5-Tier Memory | SDD + 9 articles | **Personality-driven** |
| 9 | **Agent count** | ~12 | 7-stage | 1 team | — | 12+ | 79 | Constitution | **144** |
| 10 | **Marketplace** | ❌ | ❌ | ❌ | ❌ | Emerging | 79 embedded | 80+ @ scale | **144 built-in** |
| 11 | **Agent integrations** | 1 | ~3 | 1 | 14+ | Multi-IDE | 8+ | 30+ | **11** |
| 12 | **Governance depth** | Light | Medium (TDD) | Medium | Medium | High (BMM) | Medium | **Very High** (9 articles + AI-disclosure) | **Light (despite scale)** |
| 13 | **Governance files** | 1-2 | 1-2 | 1-2 | 1-2 | 2-3 | 2-3 | **6** | 5 |
| 14 | **Slash namespace** | — | — | — | `/gsd-*` | `/bmad-*` | — | `/speckit.*` | `@agency-*` |
| 15 | **Constitution concept** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** | ❌ |
| 16 | **Anti-vibe-coding** | implicit | TDD-first | discipline | SDD | methodology | embraces | **Formal explicit** | Personality-drives-purpose |
| 17 | **AI-disclosure policy** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** | ❌ |
| 18 | **i18n** | — | — | — | — | VN trans | VN authored | — | zh-CN CONTRIBUTING |
| 19 | **Intellectual lineage** | — | — | YC / Garry Tan | — | — | — | **John Lam** | **None (Reddit community)** |
| 20 | **Karpathy connection** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 21 | **OpenClaw/Hermes** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ OpenClaw | ❌ (corp opts out) | **✅ OpenClaw (5th wiki)** |
| 22 | **Packaging tool** | npm | npm | bash | bash | npm | npm | uv | **bash** |
| 23 | **Tagged releases** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (multi-version) | ✅ v0.7.3 | **❌ (main only)** |
| 24 | **Origin story** | — | TDD discipline | Virtual team thought experiment | — | — | VN AI-product lead | John Lam research | **Reddit thread → 50+ requests 12h** |

## 3. T1 8-archetype map (post-v18)

### 3-axis quadrant visualization

```
                         Scale tier
             Small         Medium         Large         X-Large
        ┌────────────┬────────────┬────────────┬────────────┐
Solo    │ codymaster │ ECC, SP,   │ graphify   │ agency-    │
comm    │ (VN, 38)   │ gstack, GSD│ (T4, 30K)  │ agents     │
        │            │ (5-10K)    │            │ (82.9K)    │
        ├────────────┼────────────┼────────────┼────────────┤
LLC     │            │            │ BMAD       │            │
        │            │            │ (45K)      │            │
        ├────────────┼────────────┼────────────┼────────────┤
Corp    │            │            │            │ spec-kit   │
        │            │            │            │ (89.2K)    │
        └────────────┴────────────┴────────────┴────────────┘
```

### Observations

- **8 archetypes in corpus T1** (3 org × 4 scale)
- **Solo dominates** — 4 of 4 scale columns have solo entrant
- **All 3 X-large cells filled** at v18 (solo + corp, LLC missing at X-large)
- **LLC only at Large** (BMAD 45K)
- **Corporate only at X-large** (spec-kit 89.2K)

### Pattern #9 Resolution D confirmed at T1 N=8

Multi-axial model validated. T1 bifurcates along organizational archetype (solo/LLC/corporate) × scale tier (small/medium/large/X-large) × methodology depth + other dimensions.

**8 archetypes of 12 possible (org × scale) = 67% density.**

## 4. Pattern #20 evolution — solo-scale ceiling

### Data points

| Framework | Tier | Archetype | Stars |
|-----------|------|-----------|-------|
| notebooklm-py v7 | T4 | Solo narrow | ~300 |
| ECC v1, SP v2, etc. | T1 | Solo medium | 5-10K |
| graphify v16 | T4 | Solo broad | 30K |
| **agency-agents v18** | **T1** | **Solo massive + Reddit-viral** | **82.9K** |

### Pattern #20 v18 formulation

> "**Solo-Scale Ceiling by Scope × Distribution × Timing × Community-Virality:**
> 
> - Narrow / low-distribution: 100-1000 stars
> - Medium / single-platform: 5-10K stars
> - Broad / multi-platform: 30K stars
> - **Massive + multi-platform + viral-timing: 80K+ stars**
> 
> Solo ceiling asymptotically approaches corporate ceiling (~90K) but slightly below due to resource limits (except when community-viral multiplier kicks in)."

### Ceiling model revision

**Prior ceiling ~30K (graphify v16) → new ceiling 80-90K (agency-agents v18).**

**Corporate advantage** over solo at X-large: ~7K stars (spec-kit 89 vs agency-agents 83). **Not large.**

### Pattern #20 promotion status

- v16: candidate (1 data point — graphify 30K)
- v18: **refined candidate** (2 data points — graphify + agency-agents)
- v19+: N≥3 needed for promotion to confirmed

## 5. Pattern #19 evolution — 3 lineage archetypes

### Pattern #19 history

| Version | Evidence | Refinement |
|---------|----------|------------|
| v16 | Karpathy 3 touchpoints | Candidate (clustering) |
| v17 | John Lam in spec-kit | 2nd influence node |
| **v18** | **No lineage in agency-agents** | **3 archetypes** |

### 3 archetypes formalized

1. **Individual-author lineage** (Karpathy, John Lam)
2. **Methodology-lineage** (SDD shared across GSD + spec-kit)
3. **Community-viral / no-lineage** (agency-agents Reddit origin)

### Corpus distribution (post-v18)

| Archetype | Count | Frameworks |
|-----------|-------|------------|
| Individual | 4 | vault + autoresearch + graphify + spec-kit |
| Methodology | 2 | GSD + spec-kit (SDD shared) |
| Community-viral | 1 | agency-agents |

### Implication

**Storm Bear vault's Karpathy-heavy framing is one of 3 archetypes, not universal.** Community-viral origin is viable alternative.

## 6. Pattern #18 evolution — OpenClaw at 5th wiki

### Full OpenClaw timeline

| Wiki | Version | Evidence |
|------|---------|----------|
| codymaster | v12 | 📄 Doc |
| paperclip | v14 | 🏗️ Arch |
| multica | v15 | 📄 Doc |
| graphify | v16 | 🛠️ Exec |
| **agency-agents** | **v18** | **🛠️ Exec** |

### Hermes timeline

| Wiki | Version | Evidence |
|------|---------|----------|
| paperclip | v14 | 🏗️ Arch |
| multica | v15 | 📄 Doc |
| graphify | v16 | 🛠️ Exec |
| agency-agents | v18 | **❌ (absent)** |

### Pattern #18 v17 refinement validated at v18

**Claim:** OpenClaw/Hermes standards are community-platform-specific.

**v18 evidence:**
- agency-agents (solo-community-style) → OpenClaw ✅
- spec-kit v17 (corporate) → OpenClaw ❌
- Pattern holds at 2-contrast, 5-positive-case level

### OpenClaw > Hermes within community-platform

- OpenClaw: 5 of 5 community-platform wikis (100%)
- Hermes: 3 of 5 community-platform wikis (60%)

**OpenClaw is the more-established standard.**

### Pattern #18 promotion candidate

- 12 observations across 5 wikis × execution + documentation
- Community-platform archetype confirmed
- **Could promote from candidate to confirmed at v19+**

## 7. Pattern #9 Resolution D at v18

### History

| Version | Tier | Pattern #9 status |
|---------|------|-------------------|
| v10 | T5 | Observation |
| v13 | T4 | Cross-tier confirmation |
| v14 | T5 | First test (paperclip) |
| v15 | T2 | Platform-tier homogeneity |
| v16 | T4 | Multi-axial Resolution D introduced |
| v17 | T1 | Resolution D generalized to T1 (N=7) |
| **v18** | **T1** | **Resolution D further validated (N=8, 8 archetypes)** |

### Resolution probabilities at v18

| Resolution | Post-v17 | Post-v18 |
|------------|----------|----------|
| A: Universal bifurcation (2-axis) | 25% | 20% |
| B: Invalidated | 10% | 10% |
| C: Tier-dependent | 15% | 10% |
| **D: Multi-axial within most tiers** | **50%** | **60%** |

**Resolution D strengthens at v18.** Could promote to confirmed at v19+ with N≥4 at T2 or T3 test.

## 8. Convergences (where all 8 T1 agree)

### Philosophical

- AI-assisted coding needs structure (all 8)
- Human-in-loop for policy (all 8)
- Docs/specs as artifacts (all 8)
- Git-integrated workflow (7 of 8; agency-agents no releases)
- Test-first or quality-first (7 of 8; ECC partial)

### Technical

- Multi-platform compatibility (6 of 8; gstack + ECC single-platform)
- Template-driven generation (all 8)
- MIT/permissive license (7 of 8; codymaster ISC)
- Config-file driven (7 of 8; agency-agents shell-scripts)

## 9. Divergences at T1 8-way

### Axis 1: Organizational archetype

8 archetypes observed (some quadrants empty).

### Axis 2: Methodology depth

- **Very High:** spec-kit (9 articles + AI-disclosure)
- **High:** BMAD (BMM)
- **Medium:** Superpowers (TDD), gstack (9-rule), GSD (SDD), codymaster (5-Tier)
- **Light:** ECC (feature), agency-agents (personality-driven)

### Axis 3: Primary product

- **Methodology:** spec-kit, BMAD, Superpowers, GSD
- **Agent library:** codymaster (79), agency-agents (144)
- **Framework tooling:** ECC, gstack

### Axis 4: Distribution strategy

- **Corporate-resource-enabled:** spec-kit (30+ platforms + 80+ extensions)
- **Multi-platform broad:** agency-agents (11 platforms + 144 built-in)
- **Multi-harness:** GSD (14+ harnesses)
- **Single-platform:** ECC, gstack

## 10. Storm Bear pilot ranking (v18 update)

| # | Framework | Priority | Rationale |
|---|-----------|----------|-----------|
| 1 | spec-kit | HIGH | Corporate stability + SDD + VN enterprise potential |
| 2 | BMAD | HIGH | VN translation + methodology + 45K scale |
| 3 | gws | HIGH | VN enterprise + Google + Apache (T4) |
| 4 | **agency-agents** 🆕 | **MEDIUM** | **144 agents ready + multi-tool; solo bus-factor** |
| 5 | codymaster | MEDIUM | VN peer-category |
| 6 | multica | MEDIUM | Linear-analog T2 team UX |
| 7 | graphify | HIGH (direct) | Vault applicability (run first) |

## 11. Emergent patterns at T1 8-way

### Pattern: Solo scales when scope × distribution × timing align

agency-agents (82.9K) + graphify (30K) + corporate spec-kit (89.2K) show solo can match corporate if:
- **Massive scope** (144 agents)
- **Multi-platform** (11+ installs)
- **Viral timing** (Reddit launch)

### Pattern: Personality-driven T1 is emerging

agency-agents' personality emphasis is unprecedented in T1. Pattern #25 candidate.

### Pattern: Shell-first minority persists

gstack v3 + agency-agents v18 = 2 shell-first T1 frameworks. Pattern #26 candidate.

### Pattern: Intellectual lineage diversifies

Karpathy 3 touchpoints (v10-v16) → broken at v17 (John Lam) → continued break at v18 (no lineage). Pattern #19 refining.

### Pattern: Governance-depth diverges by archetype

- Solo: light governance (even at 82.9K)
- LLC: medium
- Corporate: heavy (6 files + AI-disclosure)

Governance correlates with ORGANIZATION not SCALE.

## 12. Pattern library at v18

### New candidates at v18 (4)

- **#24 SECURITY.md as T1 standard** (graphify + spec-kit + agency-agents = 3 data points)
- **#25 Personality-Driven Agent Design** (agency-agents first-class)
- **#26 Shell-first T1** (gstack + agency-agents = 2 data points, minority pattern)
- **#27 Community-Viral Scale Path** (agency-agents Reddit → 80K+ without corporate)

### Refined at v18 (2)

- **#19** Intellectual Lineage → 3 archetypes
- **#20** Solo-Scale Ceiling → major revision (30K → 80K+)

### Library totals (post-v18)

- 12 confirmed (unchanged since v13)
- **15 candidates** (up from 11 at v17)
- **Total: 27**

**Candidates exceeded confirmed 15/12 — consolidation urgency unchanged + escalating.**

## 13. Next observation points

- **T3 second entrant** — ONLY remaining N=1 tier
- **Pattern #9 Resolution D N≥4 at T2 or T3** — would solidify universal multi-axial
- **Pattern #18 OpenClaw promotion** — 5 wikis confirms
- **Pattern #20 N=3 solo-massive** — ceiling model confirmation
- **Pattern #24 SECURITY.md N=4** — convention promotion
- **Corporate T1 N=2** (Google? AWS? Meta launch?) — corporate-T1 ceiling

## 14. Strategic recommendation at v18

**CONSOLIDATION URGENT.** 18 wikis + 27 candidates + 100+ action items = candidate-confirmation gap widening.

**Actions in order:**
1. Run graphify on Storm Bear vault (v16 pending — concrete, fast, high-leverage)
2. Pattern Library audit (promote confirmed, retire invalidated, apply formal criteria)
3. Routine v2 refactor (100+ action items overdue)
4. THEN evaluate next wiki (likely T3 second entrant for 5/5 closure)

## 15. References

- T1 7-way v17: `../../spec-kit - Beginner Analysis/03 Published/(C) Tier 1 7-way comparison.md`
- T1 6-way v12: `../../codymaster - Beginner Analysis/03 Published/(C) Tier 1 6-way comparison.md`
- T1 5-way v11, 4-way v5, 3-way v3 (earlier)
- Pattern #9/#18/#19/#20 history: root `GOALS.md`
- Parent: [[(C) index]]

---

**T1 at N=8 (largest). 8 archetypes. Pattern #9 Resolution D at 60% probability (leading). Pattern #19 3 archetypes. Pattern #20 MAJOR revision. Pattern #18 5th wiki. 4 new pattern candidates (#24-27). Pattern library now 27 total. Consolidation urgent.**
