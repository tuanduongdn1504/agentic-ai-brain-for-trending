# (C) Yeachan Heo Korean Solo Archetype + oh-my-codex Ecosystem-Layer

> **Type:** Entity — organizational + regional
> **Parent:** [[(C) index]]
> **Sources:** README maintainers + ambassadors + top collaborators + sibling repo reference
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

Yeachan Heo operates as **Korean solo-led creator** of oh-my-claudecode (30K stars, 3.5 months) + sibling product `oh-my-codex`. **First Korean-authored T1 framework in Storm Bear corpus** (Pattern #55 candidate) and **7th Pattern #17 data point with new 5th archetype variant** (individual-multi-runtime-publisher).

## 2. Yeachan Heo personal profile

- **GitHub:** [@Yeachan-Heo](https://github.com/Yeachan-Heo)
- **Role:** Creator & Lead (solo)
- **Nationality inferred:** Korean (name conventions + Korean collaborator cluster + Korean README)
- **Public presence:** GitHub Sponsors active + Discord owner
- **Sibling project:** `oh-my-codex` (parallel for OpenAI Codex CLI)

## 3. Korean team composition

### Core roster
| Role | Person | Evidence |
|------|--------|----------|
| Creator & Lead | Yeachan Heo | Solo |
| Ambassador | Sigrid Jin (@sigridjineth) | Korean name |
| Document Specialist | devswha (@devswha) | Likely Korean |
| Top Collaborator | JunghwanNA (@shaun0927) — 65 commits | Korean |
| Top Collaborator | riftzen-bit (@riftzen-bit) — 52 commits | Likely Korean |
| Top Collaborator | Seunggwan Song (@Nathan-Song) — 20 commits | Korean |
| Top Collaborator | BLUE (@blue-int) — 20 commits | Ambiguous |
| Top Collaborator | Junho Yeo (@junhoyeo) — 15 commits | Korean |

**Korean saturation:** ~7 of 8 named accounts plausibly Korean. Core governance = Korean.

### Featured contributors ecosystem (from README)

Top 11 personal non-fork repos from 100+ star OMC contributors: **6 of 11** appear Korean-origin (Yeachan-Heo, junhoyeo, psmux, jcwleo, MeroZemory, HaD0Yun). Korean ecosystem-promotion observable.

## 4. Pattern #55 Korean Regional Archetype T1 (NEW candidate)

**Definition:** Korean-authored T1 framework in Storm Bear corpus.

**Prior T1 regional archetypes (post-v18):**
- **US corporate:** spec-kit v17 (GitHub/Microsoft), ECC v1, Superpowers v2, gstack v3
- **US LLC:** BMAD v11
- **US community:** GSD v5
- **VN solo:** codymaster v12 (Tody Le)
- **Unattributed solo:** agency-agents v18 (msitarzewski)

**v27 adds Korean solo archetype** — **5th distinct regional archetype at T1**.

### Regional archetype comparison

| Archetype | Count | Examples |
|-----------|-------|----------|
| US corporate | 4 | gstack (YC), spec-kit (GitHub), ECC + Superpowers (US solo) |
| US LLC | 1 | BMAD |
| US community | 1 | GSD |
| VN solo | 1 | codymaster |
| Unattributed solo | 1 | agency-agents |
| **Korean solo (NEW)** | **1** | **oh-my-claudecode v27** |

Pattern #55 candidate (N=1). Validates/strengthens if 2nd Korean T1 arrives.

## 5. Pattern #17 Ecosystem-Layer 5th archetype variant (individual-multi-runtime-publisher)

### Current Pattern #17 state (post-v26)

6 data points across 4 archetype variants:

| # | Organization/Individual | Archetype variant | Reference |
|---|------------------------|-------------------|-----------|
| 1 | nextlevelbuilder | Individual-led-dev | goclaw v4 + multica contribution |
| 2 | Anthropic | Big-tech curator | anthropics/skills |
| 3 | Vercel | Big-tech curator | vercel-labs/agent-skills |
| 4 | safishamsi / penpax.ai | Individual-led dev solo-brand | graphify v16 + Penpax |
| 5 | VoltAgent | Commercial-startup ecosystem | awesome-design-md v25 |
| 6 | HuggingFace | Ecosystem-scale commercial platform | HF agents-course v26 |

### v27 adds 7th data point + 5th variant

| # | Org/Individual | Archetype variant | Reference |
|---|---------------|-------------------|-----------|
| 7 | **Yeachan Heo** | **Individual-multi-runtime-publisher (NEW)** | **oh-my-claudecode + oh-my-codex** |

### Distinction from nextlevelbuilder (variant #1)

| Dimension | nextlevelbuilder | Yeachan Heo |
|-----------|-----------------|-------------|
| Product pattern | One anchor product + contributions to others | **Multiple parallel products, each runtime-specialized** |
| Ecosystem focus | Individual developer | Individual multi-CLI orchestrator |
| Cross-org activity | Contributes to other ecosystems (multica) | Publishes own parallel products (oh-my-codex) |
| Runtime breadth | Single-runtime (Go) | **Multi-runtime (Claude + Codex; separate repos)** |
| Sibling model | N/A | **Explicit "for Codex users" cross-promotion** |

**Yeachan archetype is distinct** — runtime-specialized parallel publishing with cross-promotion between siblings.

## 6. oh-my-codex sibling product

From OMC README row 1:

> **For Codex users:** Check out [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) — the same orchestration experience for OpenAI Codex CLI.

**Structural implications:**
- Same core orchestration concepts ported per-runtime
- Reduces user confusion (Claude users → OMC; Codex users → oh-my-codex; OMC CLI can still spawn Codex workers)
- **Maintenance cost:** 2× (parallel codebases)
- **Ecosystem leverage:** 2× reach (Claude + Codex communities)

**Yeachan's ecosystem bet:** user runtime-native tools dominate product ergonomics; runtime-specific products beat runtime-agnostic platforms for solo-maintainer reach.

## 7. Solo-at-enterprise-scale velocity

### Comparison with prior solo-scale data points

| Framework | Stars | Age (days) | Stars/day | Archetype |
|-----------|-------|-----------|-----------|-----------|
| graphify v16 | 30,000 | ~1,095 (3 yr) | ~27 | Solo broad-scope |
| agency-agents v18 | 82,900 | ~365 (1 yr est) | ~227 | Solo community-viral |
| **oh-my-claudecode v27** | **30,366** | **102** | **~298** | **Solo Korean multi-runtime** |

**oh-my-claudecode velocity exceeds agency-agents by ~31%.** Supports Pattern #20 solo-scale-ceiling revision — ceiling rises rapidly when:
1. Framework answers unmet need (multi-runtime orchestration)
2. Inspiration lineage explicit (5 sources)
3. Runtime community active (Claude Code user base growing)
4. Install friction low (plugin marketplace native)

**Pattern #20 revision candidate:** solo-scale ceiling may not have fixed absolute limit; velocity × scope × community-fit → emergent scale.

## 8. Korean ecosystem signals in repo structure

- `.clawhip/` directory — Korean-origin naming (clawhip = OpenClaw + whip? Unresolved etymology)
- `.codex/` file — Codex config file
- `.claude-plugin/` directory — Claude plugin manifest
- Korean README (`README.ko.md`)
- Ambassador program with Korean first-name (Sigrid Jin)
- GitHub Sponsors set up (typical Korean OSS monetization pattern)

## 9. Community-virality without US-based Reddit path

**Distinct from agency-agents v18** (Reddit-viral via msitarzewski, 82.9K stars via community path) — oh-my-claudecode reached 30K through:
- Korean Dev community virality (Korean tech scene early adoption)
- English-first README with 7 translations
- Multi-runtime value prop (broad Claude Code user appeal)
- Explicit recursive citation (borrowed credibility from Superpowers + ECC)

Pattern #27 Community-Viral Scale Path — **Korean-origin sub-path**. Distinct from US-Reddit (agency-agents) and CN-WeChat (TrendRadar v19). Adds regional community-virality diversity.

## 10. Sponsor + donation monetization

GitHub Sponsors page active. Pitch from README:
- Keep development active
- Priority support for sponsors
- Influence roadmap & features
- Help maintain free & open source

**Model:** Pure-OSS-with-GitHub-Sponsors (no LLC, no commercial derivative, no open-core tier). Distinct from:
- BMAD v11 formalized LLC
- fish-speech v20 / Skyvern v24 open-core
- awesome-design-md v25 commercial-funnel (VoltAgent getdesign.md)
- Unsloth v23 dual-license

**Yeachan donation-only model** — closer to Karpathy autoresearch (no monetization) + paperclip v14 (no VC disclosed) economic philosophy.

## 11. Related concepts

- [[(C) Cluster — Ecosystem + multi-lineage + Korean authorship]]
- [[(C) 5-Source Multi-Lineage + Recursive Corpus Reference + Pattern 57 Candidate]]
- Pattern #17 Ecosystem-Layer Organizations (confirmed v15; 7th data point at v27 with 5th variant)
- Pattern #20 Solo-Scale Ceiling (revision candidate at v27 for velocity factor)
- Pattern #27 Community-Viral Scale Path (confirmed v21; 5th data point at v27 Korean-sub-path)
- Pattern #55 Korean Regional Archetype T1 (NEW candidate at v27)

## 12. References

- README.md Core Maintainers + Ambassadors + Document Specialists + Top Collaborators sections
- README.md Featured by OmC Contributors section
- oh-my-codex GitHub link (Yeachan-Heo/oh-my-codex)

## 13. Edges + limitations

- **Single-point-of-failure** — if Yeachan unavailable, governance collapses to ambassador (N=1) + doc specialist (N=1); top collaborator (JunghwanNA 65 commits) could backfill but role uncertain
- **Korean-language primacy risk** — VN/EN docs translated but design decisions Korean-first; i18n cohesion depends on ambassador quality
- **oh-my-codex split-attention** — 2× maintenance cost; Codex market smaller than Claude Code; may under-invest if Claude momentum accelerates
- **Velocity unsustainable?** — 289 stars/day over 3.5 months = ~105K projected annual rate if sustained; real-world deceleration expected
- **Korean archetype uniqueness** — may not generalize if Korean-solo-led T1 remains N=1 long-term

---

**Yeachan Heo = first Korean-authored T1 in Storm Bear corpus. 7th Pattern #17 data point with new 5th archetype variant (individual-multi-runtime-publisher). Pattern #55 Korean Regional Archetype candidate registered. Solo-at-enterprise-scale velocity (~298 stars/day) challenges prior ceilings (agency-agents ~227).**
