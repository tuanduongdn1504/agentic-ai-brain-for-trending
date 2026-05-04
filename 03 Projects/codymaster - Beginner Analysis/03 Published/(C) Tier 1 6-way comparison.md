# (C) Tier 1 6-way comparison — ECC vs Superpowers vs gstack vs GSD vs BMAD vs codymaster

> **Type:** Phase 4b — same-tier N-way comparison (extends v11's 5-way to 6-way)
> **Scope:** All 6 currently-analyzed Tier 1 "Agent-as-assistant" frameworks
> **Status:** ✅ Published
> **Predecessor:** `../../BMAD-METHOD - Beginner Analysis/03 Published/(C) Tier 1 5-way comparison.md` (5-way, pre-codymaster)
> **T1 re-opening justification:** codymaster cleared "genuinely different" bar via 5 signals (VN-authored + 79 skills largest + 8+ platforms broadest + 6+ novel primitives deepest + SkillsBench empirical research first)

---

## 0. Tier 1 membership (as of 2026-04-19, v12)

| # | Framework | GitHub | Stars | Author | First wiki |
|---|-----------|--------|-------|--------|-----------|
| 1 | ECC (Everything Claude Code) | affaan-m/everything-claude-code | ~5K | Affaan (solo) | 2026-04-17 |
| 2 | Superpowers | obra/superpowers | ~5K | Jesse Vincent (solo) | 2026-04-18 |
| 3 | gstack | garrytan/gstack | ~5K | Garry Tan / YC (corporate) | 2026-04-18 |
| 4 | GSD (get-shit-done) | gsd-build/get-shit-done | ~8K | TÂCHES (solo) | 2026-04-18 |
| 5 | BMAD (BMAD-METHOD) | bmad-code-org/BMAD-METHOD | **45K** | BMad Code, LLC | 2026-04-19 |
| 6 | **codymaster** | **tody-agent/codymaster** | **38** | **Tody Le (VN solo)** | **2026-04-19** |

**T1 was formally closed at v11 (N=5).** codymaster re-opens because it clears the "genuinely different" bar (documented §9 below).

**Taxonomy reference:** `../../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`

---

## 1. Executive summary (6-way)

- **codymaster = scope outlier** — Full Lifecycle (Idea→Learn), 79 skills, 8+ platforms, 6+ novel primitives. Smallest community (38 stars) but deepest artifact.
- **BMAD = scale outlier** — 45K stars, LLC, marketplace, VN-translated.
- **GSD = framing outlier** — "context rot" as primary problem definition.
- **Superpowers = methodology outlier** — TDD + 7-stage workflow most opinionated.
- **gstack = backing outlier** — only YC corporate T1.
- **ECC = breadth outlier** — all-round Claude Code skills without narrow theme.
- **6 outliers on 6 different axes.** T1 at N=6 is genuinely diverse; no single archetype.

---

## 2. Multi-axis comparison (20 axes)

### Axis group A — Scale + community

| Axis | ECC | SP | gstack | GSD | BMAD | **codymaster** |
|------|-----|----|---------|-----|------|---------------|
| **1. Stars** | ~5K | ~5K | ~5K | ~8K | **45K** | **38 (smallest)** |
| **2. Forks** | ~500 | ~500 | ~500 | ~800 | 5,338 | 21 |
| **3. Community** | GH issues | GH issues | GH issues | $GSD token | **Discord + YouTube** | Global Discord |
| **4. Author type** | Solo US | Solo US | Corporate (YC) | Solo US | **LLC (US)** | **Solo VN** |

→ codymaster at 38 stars = order of magnitude smaller than any peer. Scale-inverse outlier to BMAD.

### Axis group B — Distribution + install

| Axis | ECC | SP | gstack | GSD | BMAD | **codymaster** |
|------|-----|----|---------|-----|------|---------------|
| **5. Install** | git + setup | Plugin | npm | npx | npx | **8+ channels (marketplace + npx + npm + slash)** |
| **6. Release cadence** | Irregular | Irregular | Regular | Regular | Weekly + `@next` | 11 tags, 120 commits |
| **7. License** | MIT | MIT | MIT | MIT | MIT | **ISC (outlier)** |
| **8. Platforms supported** | 1 | 1 | 1 | 14 | 4 | **8+** |

→ codymaster = broadest multi-platform distribution + only ISC license. Format + licensing outliers.

### Axis group C — Agent/skill architecture

| Axis | ECC | SP | gstack | GSD | BMAD | **codymaster** |
|------|-----|----|---------|-----|------|---------------|
| **9. Skill/agent count** | Many small | ~10 | ~15 | 33 | 46 (12+ agents+34+ workflows) | **79 (largest)** |
| **10. Naming philosophy** | Flat | Methodology | Specialist | Role-based | Human-named personas | **`cm-` prefixed functional** |
| **11. Runtime** | MD+code | MD+bash | TS | MD+TS | Pure MD + Node | **TS + SQLite + MD** |
| **12. Trajectory** | Stable | Stable | Stable | **Expanding (+)** | **Contracting (-)** | Growing (+ silently) |

→ codymaster has largest skill surface + most engineered runtime (TS + SQLite, not pure markdown).

### Axis group D — Novel primitives (depth)

| Axis | ECC | SP | gstack | GSD | BMAD | **codymaster** |
|------|-----|----|---------|-----|------|---------------|
| **13. Novel primitive count** | 0 | 1 (7-stage) | 0 | 1 (context rot spec) | 2 (Party Mode + Scale-Adaptive) | **6+ (5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench)** |
| **14. Memory architecture** | None | None | None | Context-rot concept | Scale-Adaptive depth | **5-Tier Memory + Ebbinghaus decay** |
| **15. Context engineering** | — | — | — | Conceptual | Auto-adapt | **Engineered: progressive L0/L1/L2 + cm:// URI + CodeGraph 95% compression + 200k budget** |
| **16. Empirical research** | — | — | — | — | — | **SkillsBench +18.6pp (only T1 with published benchmark)** |

→ codymaster is **deepest technical-primitive density in T1** by 3-4×. No peer comparable on brain architecture.

### Axis group E — Localization + accessibility

| Axis | ECC | SP | gstack | GSD | BMAD | **codymaster** |
|------|-----|----|---------|-----|------|---------------|
| **17. Non-EN docs** | ❌ | ❌ | ❌ | ❌ | ✅ VI+CS | **✅ VI+ZH+RU+KO+HI (6 langs)** |
| **18. Author origin** | US | US | US/YC | US | US-LLC | **VN** |
| **19. VN localization mode** | — | — | — | — | VN-translated | **VN-authored, EN-primary** |
| **20. Beginner onramp** | Self-directed | Jesse's guide | README | `/gsd-ingest-docs` | `bmad-help` + VN | **`cm how-it-work` + 6-lang README** |

→ codymaster adds **new localization axis (VN-authored vs VN-translated)** + **most multilingual docs** in T1.

---

## 3. Seven emergent patterns (extends v11's 7)

### Pattern 1 — Scale-reach correlation is non-linear (unchanged)

GSD (~8K) + BMAD (45K) got scale via distinctive framing. ECC/SP/gstack cluster at ~5K. **codymaster at 38 stars breaks the pattern entirely** — smallest community with deepest artifact. Inverse-correlation possible: depth and star-count are orthogonal, not correlated.

### Pattern 2 — Distribution convergence on npx/npm (reinforced)

4 of 6 use npx/npm. codymaster + gstack + GSD + BMAD all npm-distributed. **codymaster extends to 8+ platforms** — reinforces multi-distribution as T1 maturity signal.

### Pattern 3 — Agent count philosophy divergence (expanded)

| Framework | Direction | Count |
|-----------|-----------|-------|
| Superpowers | Few broad | ~10 |
| BMAD | Consolidating | 46 (shrinking Amelia absorbs) |
| gstack | Stable | ~15 |
| GSD | Expanding | 33 (growing) |
| ECC | Many small | Many |
| **codymaster** | **Expanding quietly** | **79** |

**codymaster aligns with GSD direction (expanding)** but reaches further (79 vs 33). The philosophy divide is real and persistent.

### Pattern 4 — Markdown-pure vs engineered-runtime (refined)

- **Pure markdown:** BMAD (strictest), Superpowers (mostly)
- **MD + TS:** GSD, gstack
- **MD + code + DB:** **codymaster** (SQLite backing, most engineered)

codymaster shifts the spectrum — **SQLite + better-sqlite3 dependency** is novel for T1. Peers treat skills as static documents; codymaster treats skills as DB-indexed artifacts.

### Pattern 5 — Commercial diversification spectrum (extended)

- Solo maintainer (US): ECC, Superpowers, GSD
- Solo maintainer (VN): **codymaster (NEW)**
- Corporate (YC): gstack
- LLC: BMAD

**codymaster adds non-US-solo point** to spectrum. Previous v11 spectrum = "formalization level"; v12 reveals "geographic origin" is another dimension.

### Pattern 6 — Localization is rare; BMAD started it, codymaster deepens (evolved)

- v5 (4-way): zero VN
- v11 (5-way): BMAD added VN → Pattern #6 invented
- **v12 (6-way):** codymaster adds 6-language coverage + VN-authored mode → **Pattern #6 split into sub-pattern**

**Sub-pattern 6a (translated):** BMAD mode — EN-origin + machine VN
**Sub-pattern 6b (authored):** codymaster mode — VN origin + EN-primary + machine VN

→ Pattern 6 is **evolving** at 6-way. Future: what's 6c (VN-primary)?

### Pattern 7 — Marketplace emergence at scale (unchanged)

BMAD's v6.3 marketplace remains unique. codymaster uses Claude plugin marketplace but doesn't publish its own. Pattern 7 holds with BMAD still sole example.

### Pattern 8 (NEW at 6-way) — Empirical research is rare

- 5 of 6 frameworks ship with no published benchmark
- **codymaster alone publishes SkillsBench +18.6pp**
- Even if methodology unverified, naming the number is unique

**Predicts:** as T1 matures, more frameworks will publish benchmarks. First-mover (codymaster) sets the bar, even at 38 stars.

---

## 4. Decision matrix — "which T1 for which profile?" (updated)

| User profile | v11 recommended | v12 update |
|--------------|----------------|-----------|
| **VN-speaking developer/team** | BMAD | **BMAD + codymaster** (both VN docs; codymaster adds peer-author proximity) |
| **VN product-lead, "can't code"** | — | **codymaster** (author profile match) |
| **Solo developer, Claude Code native, wants broad skills** | ECC | ECC |
| **Methodology purist, TDD focused** | Superpowers | Superpowers |
| **Startup team (YC-style)** | gstack | gstack |
| **Context-engineering focus** | GSD | GSD (conceptual) **or codymaster** (engineered) |
| **Scrum coach / Agile practitioner** | BMAD | **BMAD** (workflows) **+ codymaster** (cm-retro-cli, cm-sprint-bus) |
| **Game developer** | BMAD + BMGD | BMAD + BMGD |
| **Wants marketplace + community modules** | BMAD | BMAD |
| **Wants stability, minimal churn** | Superpowers or ECC | Superpowers or ECC |
| **Wants largest skill surface** | — | **codymaster (79)** |
| **Wants multi-platform** | GSD (14 harnesses) | **GSD or codymaster (8+)** |
| **Wants engineered brain (memory, context)** | — | **codymaster (5-Tier + Smart Spine + CodeGraph)** |
| **Wants empirical research backing** | — | **codymaster (SkillsBench only)** |
| **Wants VN author community proximity** | — | **codymaster (unique peer)** |
| **Wants non-code-writer workflow** | — | **codymaster ("can't code" author designed for this)** |

**New multi-framework strategy (advanced):**
- **Stack:** BMAD (workflows + VN translation) + codymaster (brain depth + VN author) + GSD (context rot discipline reference)
- **Install alongside, use per-task**

---

## 5. Churn + stability axis (updated)

| Framework | Major versions | Breaking-change pattern | Stability |
|-----------|---------------|-------------------------|-----------|
| ECC | 1 | None | High |
| Superpowers | Few | Rare | High |
| gstack | Few | Rare | High |
| GSD | Steady | Occasional | Medium |
| BMAD | 6 majors/year | Every 1-2 majors | **Low** |
| **codymaster** | **11 tags, 120 commits** | **Unknown** (no public changelog) | **Unknown** |

codymaster has release activity but unclear breaking-change discipline. 38-star community = no breaking-change complaints visible, not necessarily = no breaking changes.

---

## 6. Philosophical axis — "what is an agent?" (updated)

| Framework | Agent = |
|-----------|---------|
| ECC | Task-scoped skill |
| Superpowers | Methodology stage |
| gstack | Specialist role |
| GSD | Workflow coordinator |
| BMAD | Named persona |
| **codymaster** | **Self-healing executable unit** |

codymaster's agent = **living artifact that degrades and heals itself**. This is **new philosophy** in T1. No peer treats skills as organisms that need active maintenance.

---

## 7. T1 wiki cross-linking map (updated)

```
ECC ←→ Superpowers : methodology
ECC ←→ gstack     : skills vs roles
ECC ←→ GSD        : breadth vs context
ECC ←→ BMAD       : skills vs modules
ECC ←→ codymaster : skills count (many vs 79)

Superpowers ←→ BMAD : 7-stage vs 34+ workflows
Superpowers ←→ codymaster : methodology vs architecture

gstack ←→ BMAD : YC vs LLC formalization
gstack ←→ codymaster : engineering team vs SaaS team

GSD ←→ BMAD : 33 agents vs 12+ consolidating (key T1 debate v11)
GSD ←→ codymaster : context rot CONCEPT vs context-engineering SOLUTION ⭐

BMAD ←→ codymaster : VN-translated vs VN-authored ⭐ (key v12 debate)
```

**Two key v12 debates unlocked:**
1. **GSD ↔ codymaster** — concept vs implementation of context engineering
2. **BMAD ↔ codymaster** — VN-translated vs VN-authored localization

---

## 8. What 6-way adds vs 5-way (meta-learning)

v11's 5-way identified 7 emergent patterns. Adding codymaster as 6th entrant revealed:

1. **Scale-depth inverse correlation** — 38 stars + deepest primitives = Pattern 1 refined (scale ≠ quality)
2. **VN-authored vs VN-translated split** — Pattern 6 sub-categorized
3. **Empirical research emergence** — Pattern 8 invented (SkillsBench unique)
4. **Engineered-runtime extension of markdown-pure** — Pattern 4 refined
5. **Non-US-solo commercial point** — Pattern 5 extended (geographic dimension)

**Meta:** 6-way > 5-way for T1 **because codymaster is a SCOPE outlier**, not a scale outlier. BMAD (v11) was scale outlier. codymaster (v12) is scope outlier. Different axes of "genuinely different."

**Future additions:** next T1 entrant would need to be outlier on a NEW axis (not scale, not scope, not VN-authorship, not empirical research). Harder bar.

---

## 9. Re-opening justification — why codymaster cleared the "closed T1" bar

v11 formally closed T1 at N=5 with policy: "Future T1 additions must clear 'genuinely different' bar."

codymaster's 5 differentiating signals:

| Signal | Evidence | Peer comparison |
|--------|----------|-----------------|
| **1. VN-authored** | Tody Le + todyle.com + `tody-agent` handle | Only T1 with VN author |
| **2. 79 skills** | Folder count | Largest skill surface in T1 by 2× |
| **3. 8+ platforms** | Claude Desktop+Code+Cursor+Gemini+OpenCode+OpenClaw+Codex+Antigravity+npm | Broadest distribution in T1 |
| **4. 6+ novel primitives** | 5-Tier Memory + Smart Spine + CodeGraph + Self-Healing + Cloud Brain + SkillsBench | Deepest primitive density in T1 by 3× |
| **5. SkillsBench empirical research** | +18.6pp published | Only T1 with published benchmark |

**5 of 5 signals distinct from existing T1 peers.** Justifies re-opening.

**Precedent for routine v2:** "closure at N" is not permanent; re-opens when genuine outlier appears. Update routine v2 to document this policy.

---

## 10. Open questions surfaced by 6-way

1. Will other T1 frameworks publish benchmarks in response to SkillsBench? (empirical research competitive pressure)
2. Will any T1 framework author VN-primary (not just EN-primary with translation)?
3. codymaster's self-healing — will peers adopt if proven effective?
4. 5-Tier Memory architecture — will peers implement equivalents?
5. Multi-platform distribution — will BMAD/GSD expand beyond their current 4-14 platforms?
6. If codymaster scales to 1K-5K stars, does it break the scale-depth inverse correlation pattern?
7. Does codymaster's author actively respond to VN-community contributions?

---

## 11. References

### Primary wiki sources (6 projects)
- `../../Everything Claude Code - Beginner Analysis/02 Wiki/(C) index.md`
- `../../Superpowers - Beginner Analysis/02 Wiki/(C) index.md`
- `../../gstack - Beginner Analysis/02 Wiki/(C) index.md`
- `../../get-shit-done - Beginner Analysis/02 Wiki/(C) index.md`
- `../../BMAD-METHOD - Beginner Analysis/02 Wiki/(C) index.md`
- `../02 Wiki/(C) index.md` (codymaster, this project)

### Prior comparison documents
- `../../get-shit-done - Beginner Analysis/03 Published/(C) Tier 1 4-way comparison.md` — v5 baseline (pre-BMAD)
- `../../BMAD-METHOD - Beginner Analysis/03 Published/(C) Tier 1 5-way comparison.md` — v11 baseline (pre-codymaster)
- `../../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md` — 5-tier taxonomy

### Companion published guides
- [[(C) codymaster - Huong dan cho nguoi moi]] — VN-first beginner guide (first in corpus)

### Next scheduled update
- **If N=7 in T1:** add 7th entrant ONLY if clears a new outlier axis (not scale, not scope, not VN-authorship, not empirical research)
- **If codymaster reaches 1K+ stars:** revisit scale-depth inverse correlation
- **If any T1 framework adds empirical research:** Pattern 8 promoted to validated multi-entrant
- **If VN-primary framework appears:** Pattern 6c invented

---

**🐻 Storm Bear summary:** T1 at N=6. codymaster re-opened it with 5 distinct outlier signals. For VN-operator context: BMAD wins community + stability; codymaster wins author-proximity + depth. Run both in parallel pilot. Document which serves which workflow better — empirical answer > more wiki analysis.
