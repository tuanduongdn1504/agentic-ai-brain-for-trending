# (C) Tier 1 5-way comparison — ECC vs Superpowers vs gstack vs GSD vs BMAD

> **Type:** Phase 4b — same-tier N-way comparison (extends v5 4-way to 5-way)
> **Scope:** All 5 currently-analyzed Tier 1 "Agent-as-assistant" frameworks
> **Sources:** 5 project wikis + taxonomy v4 (5-tier)
> **Status:** ✅ Published
> **Previous version:** `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md` (4-way, pre-BMAD)

---

## 0. Tier 1 membership (as of 2026-04-19)

| # | Framework | GitHub | Stars | Author | First wiki |
|---|-----------|--------|-------|--------|-----------|
| 1 | **ECC** (Everything Claude Code) | affaan-m/everything-claude-code | ~5K | Affaan (solo) | 2026-04-17 |
| 2 | **Superpowers** | obra/superpowers | ~5K | Jesse Vincent (solo) | 2026-04-18 |
| 3 | **gstack** | garrytan/gstack | ~5K | Garry Tan / YC (corporate) | 2026-04-18 |
| 4 | **GSD** (get-shit-done) | gsd-build/get-shit-done | ~8K | TÂCHES (solo) | 2026-04-18 |
| 5 | **BMAD** (BMAD-METHOD) | bmad-code-org/BMAD-METHOD | **45K** | BMad Code, LLC | 2026-04-19 |

**Tier 1 definition:** Agent-as-assistant — framework/toolkit that augments single human developer via AI agent personas/workflows, installed into IDE (Claude Code primary). Contrast with T2 (platform), T3 (education), T4 (bridge), T5 (application).

**Taxonomy reference:** `../../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`

---

## 1. Executive summary

- **BMAD dominates T1 reach** — 45K stars = 9× the others combined. But dominance ≠ superiority on every axis.
- **BMAD = most formalized (LLC, trademark, PR discipline, quality gate) + only T1 with VN + only T1 with marketplace**. Trade: breaking changes every major.
- **GSD = unique context-engineering spec framing** (context rot as the primary problem, 33 agents as solution).
- **Superpowers = most opinionated methodology** (Jesse's 7-stage workflow + TDD enforcement).
- **gstack = only YC/corporate-backed** — "virtual engineering team" framing, TypeScript core.
- **ECC = all-round Claude Code skills catalog** — broadest scope without narrow specialization.
- **No single winner.** Choice depends on user profile (solo dev / coach / VN speaker / methodology purist).

---

## 2. Multi-axis comparison (18 axes)

### Axis group A — Scale + community

| Axis | ECC | Superpowers | gstack | GSD | BMAD |
|------|-----|-------------|--------|-----|------|
| **1. Stars** | ~5K | ~5K | ~5K | ~8K | **45K** |
| **2. Forks** | ~500 | ~500 | ~500 | ~800 | **5,338** |
| **3. Author type** | Solo | Solo | Corporate (YC) | Solo | **LLC (commercial)** |
| **4. Community channels** | GitHub issues | GitHub issues | GitHub issues | $GSD token + community | **Discord + YouTube active** |

→ BMAD is outlier in reach + formalization. YC backing gave gstack credibility boost but not star advantage. Solo maintainers cluster at similar star count.

### Axis group B — Distribution + install

| Axis | ECC | Superpowers | gstack | GSD | BMAD |
|------|-----|-------------|--------|-----|------|
| **5. Install pattern** | git clone + setup | Plugin install | `npm install` | `npx get-shit-done-cc` | **`npx bmad-method install`** |
| **6. Distribution channel** | Git | Claude Code plugin | npm registry | npm registry | npm + marketplace |
| **7. Release cadence** | Irregular | Irregular | Regular | Regular | **Weekly stable + `@next` daily** |
| **8. Version discipline** | Semver | Semver | Semver | Semver | **Semver + trunk-based + quality gate** |

→ BMAD has most disciplined release ops. gstack + GSD + BMAD all `npx`-pattern (convergent).

### Axis group C — Agent architecture

| Axis | ECC | Superpowers | gstack | GSD | BMAD |
|------|-----|-------------|--------|-----|------|
| **9. Agent count** | Many small skills | ~10 patterns | ~15 specialist roles | **33 (growing)** | 12+ (shrinking per v6.3) |
| **10. Agent philosophy** | Many narrow | Few broad | Many specialized | Many hierarchical | **Fewer broader (consolidating)** |
| **11. Trajectory** | Stable | Stable | Stable | **Expanding** | **Contracting** |
| **12. Core language** | Markdown + samples | Markdown + bash | TypeScript | Markdown + TS workflow | **Markdown-pure core** |

→ **Major divergence:** BMAD + GSD opposite directions on agent count. BMAD consolidates (Barry/Quinn/Bob → Amelia). GSD adds (now 33). Different theses on cognitive load vs specialization.

### Axis group D — Novel primitives

| Axis | ECC | Superpowers | gstack | GSD | BMAD |
|------|-----|-------------|--------|-----|------|
| **13. Unique feature** | Breadth | 7-stage workflow + TDD | Virtual engineering team framing | Context rot spec | **Party Mode + Scale-Adaptive** |
| **14. Module system** | Skills catalog | Pattern library | Flat roles | Commands + agents | **5 modules + marketplace** |
| **15. Meta-tooling** | — | — | — | — | **BMB (builds more BMAD)** |

→ BMAD is only T1 with formal marketplace + meta-builder. Superpowers + GSD have stronger methodological opinions.

### Axis group E — Localization + accessibility

| Axis | ECC | Superpowers | gstack | GSD | BMAD |
|------|-----|-------------|--------|-----|------|
| **16. Non-EN docs** | ❌ | ❌ | ❌ | ❌ | **✅ VN + Czech (v6.3)** |
| **17. Doc depth** | Moderate | Moderate | Moderate | **Deep** (context spec) | Broad + cross-lang shallow |
| **18. Beginner onramp** | Self-directed | Jesse's walk-through | README | `/gsd-ingest-docs` | **`bmad-help` + VN README** |

→ BMAD is **only T1 option for VN users**. Translation quality ≠ native, but existence matters for Storm Bear operator context.

---

## 3. Six emergent 5-way patterns (extends v5's 6 patterns with BMAD data)

### Pattern 1 — Scale-reach correlation is non-linear

GSD (context rot) + BMAD (methodology) both hit scale via **distinctive framing**. ECC/Superpowers/gstack cluster at ~5K despite different strengths. **Framing that names a problem gets outsized reach.**

### Pattern 2 — Distribution convergence on `npx`

3 of 5 frameworks (gstack, GSD, BMAD) use `npx <package>` install. ECC + Superpowers use different patterns. **npm as distribution layer is winning T1.**

### Pattern 3 — Agent count ≠ quality — it's a philosophy fork

GSD (33, growing) vs BMAD (12+, shrinking) is **the most important T1 debate**. No empirical resolution. Both claim user benefit.

### Pattern 4 — Markdown-pure trend (convergent, Karpathy-adjacent)

BMAD pushes markdown-pure core hardest. ECC + Superpowers + GSD partially markdown. **Markdown as agent substrate = clear T1 winner pattern.** This mirrors Karpathy's autoresearch `program.md` skill pattern (T5).

### Pattern 5 — Commercial diversification spectrum

- Solo maintainer: ECC, Superpowers, GSD
- Corporate-backed: gstack (YC)
- LLC: BMAD

**BMAD is uniquely LLC-formalized** with trademark. Signals long-term commercial intent. Risk: commercial pivot (paid modules?) → open question Q6.

### Pattern 6 — Localization is rare; BMAD breaks the pattern

0 of 4 in v5 had non-EN. BMAD v6.3 added VN + Czech. **First signal T1 frameworks are extending to non-EN markets.** Question: will Superpowers/GSD/gstack follow?

### Pattern 7 (NEW — unique to 5-way) — Marketplace emergence at scale

BMAD's community module browser (v6.3) = first T1 marketplace. Predicted by Pattern 1 (BMAD's scale enables it). Other T1 may follow if their ecosystems mature.

---

## 4. Decision matrix — "which T1 for which profile?"

| User profile | Recommended | Why |
|--------------|-------------|-----|
| **VN-speaking developer/team** | **BMAD** | Only T1 with VN translation |
| **Solo developer, Claude Code native, wants broad skills** | **ECC** | All-round, no opinion overhead |
| **Methodology purist, TDD focused** | **Superpowers** | Jesse's 7-stage workflow is opinionated + proven |
| **Startup team (YC-style)** | **gstack** | Virtual engineering team framing fits |
| **Context-engineering focus** | **GSD** | Context rot spec is unique + deep |
| **Scrum coach / Agile methodology practitioner** | **BMAD** | 34+ Agile workflows + Party Mode |
| **Game developer** | **BMAD + BMGD** | Only T1 with game-dev module |
| **Wants marketplace + community modules** | **BMAD** | Only T1 with marketplace |
| **Wants stability, minimal churn** | **Superpowers** or **ECC** | Less churn than BMAD/GSD |
| **Wants corporate backing** | **gstack** (YC) or **BMAD** (LLC) | Only formalized entities |

**Multi-framework strategy (advanced):** Nothing prevents installing multiple. Example: **BMAD core for Agile workflows + GSD for context management + Superpowers methodology as reference.**

---

## 5. Churn + stability axis

| Framework | Major versions | Breaking-change pattern | Stability assessment |
|-----------|---------------|-------------------------|----------------------|
| ECC | 1 | None observed | High stability |
| Superpowers | Few | Rare | High stability |
| gstack | Few | Rare | High stability |
| GSD | Steady | Occasional | Medium stability |
| **BMAD** | **6 majors in 1 year** | **Every 1-2 majors** | **Low stability (high churn)** |

**Trade-off:** BMAD churns because evolution; ECC/Superpowers stable because small scope. **Production use of BMAD = budget migration time.**

---

## 6. Philosophical axis — "what is an agent?"

| Framework | Agent = |
|-----------|---------|
| ECC | Task-scoped skill |
| Superpowers | Methodology stage |
| gstack | Specialist role (like hiring team member) |
| GSD | Workflow coordinator |
| **BMAD** | **Named persona (human-named: Amelia, PM, Architect)** |

**BMAD's human-named personas = most anthropomorphic.** Critics: over-anthropomorphizing hides LLM mechanics. Defenders: human names reduce cognitive friction for non-technical users (PMs, designers).

---

## 7. T1 wiki cross-linking map

```
ECC ←→ Superpowers : methodology comparison
ECC ←→ gstack     : skills vs roles
ECC ←→ GSD        : breadth vs context-spec
ECC ←→ BMAD       : skills vs modules

Superpowers ←→ gstack : single-opinion vs specialist
Superpowers ←→ GSD    : TDD vs context-rot (methodology divergence)
Superpowers ←→ BMAD   : 7-stage vs 34+ workflows

gstack ←→ GSD  : YC corporate vs token-community
gstack ←→ BMAD : YC vs LLC (both formalized)

GSD ←→ BMAD : 33 agents vs 12+ consolidating (opposite philosophies) ⭐
```

**Key relationships:** GSD↔BMAD is the most informative T1 debate (agent count philosophy). gstack↔BMAD is the commercial formalization comparison.

---

## 8. What 5-way adds vs 4-way (meta-learning)

v5's 4-way (ECC/SP/gstack/GSD) identified 6 emergent patterns. Adding BMAD as 5th entrant revealed:

1. **Scale outlier exists in T1** — BMAD 9× others. Not assumed from 4-way data.
2. **Localization is possible in T1** — v5 concluded "T1 is EN-only". BMAD disproves.
3. **Marketplace emergence at scale** — new pattern #7, invisible in 4-way.
4. **Agent-count divergence** (BMAD vs GSD) — 4-way had GSD as outlier; 5-way shows BMAD is opposite outlier.
5. **Commercial formalization spectrum** — v5 saw YC as outlier; BMAD LLC adds new point, spectrum not binary.

**Meta:** **5-way > 4-way** for T1 because BMAD is genuinely different (commercial, VN, marketplace, scale). Adding a "similar" 5th entrant would have been less informative.

---

## 9. Open questions surfaced by 5-way

1. Will other T1 frameworks add non-EN translations in response to BMAD? (competitive localization pressure)
2. Will GSD or gstack add marketplace? (BMAD proves T1 marketplace viable)
3. Agent-count philosophy — is there empirical data on BMAD consolidation vs GSD expansion user outcomes?
4. Will BMAD's LLC introduce paid modules? (v6.3 marketplace is pre-commercial today)
5. Does BMAD's 45K stars = production adoption, or star-economics artifact?
6. VN community size — does any T1 have VN users today that BMAD would capture?

---

## 10. References

### Primary wiki sources (5 projects)

- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
- `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
- `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
- `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md`
- `../02 Wiki/(C) index.md` (BMAD, this project)

### Prior comparison documents

- `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md` — v5 baseline
- `../../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md` — 5-tier taxonomy

### Companion published guides (this project)

- [[(C) BMAD-METHOD - Huong dan cho nguoi moi]] — beginner guide bilingual

### Next scheduled update

- **When N=6 in T1:** add 6th T1 entrant. v11 does not close T1 — slot remains open.
- **When a T1 framework adds non-EN:** update Axis 16 (localization).
- **When empirical agent-count data emerges:** update Pattern 3 + §6 with resolved verdict.

---

**🐻 Storm Bear summary:** T1 is N=5 now. BMAD is the outlier: largest, most formal, only VN, most churn. For VN-operator context, BMAD is the clear starting point — pilot it, but don't bet production reliance until empirical assessment. Keep GSD in the toolkit for context engineering discipline.
