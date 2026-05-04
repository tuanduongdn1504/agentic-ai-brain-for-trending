# (C) T1 10-way extension + VN-Regional-Archetype N=2 validation

> **Phase 4b deliverable** — claude-howto v32
> **Type:** T1 N-way extension + regional-archetype-N=2 validation (routing mode combination)
> **Length target:** 550-700 lines
> **Date:** 2026-04-22

---

## Part 1. T1 10-way extension context

### 1.1 History of T1 at Storm Bear

| v | Wiki | Scale | Archetype | Cumulative T1 N |
|---|------|-------|-----------|-----------------|
| v1 | everything-claude-code (affaan-m) | ~5K | US solo community | 1 |
| v2 | Superpowers (obra/Jesse Vincent) | ~8K | US solo (Jesse) | 2 |
| v3 | gstack (garrytan) | — | US founder-personal (YC) | 3 |
| v5 | get-shit-done (TÂCHES) | — | US community unattributed | 4 |
| v11 | BMAD-METHOD (BMad LLC) | 45K | US commercial LLC | 5 |
| v12 | codymaster (Tody Le) | 38 | **VN-in-VN solo** | 6 |
| v17 | spec-kit (GitHub) | 89.2K | US official corporate | 7 |
| v18 | agency-agents (msitarzewski) | 82.9K | US community-viral-Reddit | 8 |
| v27 | oh-my-claudecode (Yeachan Heo) | 30.4K | **Korean solo** | 9 |
| **v32** | **claude-howto (Luong Nguyen)** | **28.2K** | **VN-diaspora solo** | **10** |

T1 is the largest tier in Storm Bear corpus. 10 entrants across 5 archetypal dimensions:
- US-vs-non-US split: 7 US + 3 non-US (VN-in-VN + VN-diaspora + Korean)
- Solo-vs-organizational: 8 solo + 1 LLC + 1 official-corporate
- Scale distribution: 5 small-medium (<10K) + 2 medium-large (30-50K) + 3 large (70K+)
- Regional distribution: 7 US + 2 VN + 1 Korean (new at v32)

### 1.2 Why T1 keeps growing

T1 ("Agent-as-assistant" per Storm Bear tier taxonomy) is the broadest + most common tier because it matches the largest user-intent segment (individuals using Claude Code daily). Each new T1 entrant teaches something new about:
- **Intellectual lineage** (Pattern #19 archetypes) — individual-author (Karpathy, Lam, Cherny) / methodology / community-viral / research-paper-chain
- **Scale-author-location correlation** (Pattern #20 dictionary rows)
- **Regional archetype emergence** (Pattern #55 Korean + proposed Pattern #70 VN-Regional)
- **Governance file conventions** (Pattern #22 AGENTS.md, Pattern #24 SECURITY.md)

v32 adds a 10th entrant that crosses new structural axes: **regional-diaspora distinction** (VN-in-VN vs VN-diaspora). First time corpus has 2 entrants from same region with clearly different geographic+audience framings.

---

## Part 2. T1 10-way comparison (24 axes)

### 2.1 Identity + governance

| Axis | ECC v1 | SP v2 | gstack v3 | GSD v5 | BMAD v11 | codymaster v12 | spec-kit v17 | agency v18 | OMC v27 | **claude-howto v32** |
|------|--------|-------|-----------|--------|----------|----------------|--------------|-----------|---------|----------------------|
| **Scale** | ~5K | ~8K | — | — | 45K | 38 | 89.2K | 82.9K | 30.4K | **28.2K** |
| **Author/org** | affaan-m | Jesse V | Garry Tan | TÂCHES | BMad LLC | Tody Le | GitHub | msitarzewski | Yeachan | **Luong** |
| **Region/location** | US | US | US | US | US | VN-HCMC | US-Microsoft | US | Korea | **France (VN-diaspora)** |
| **License** | MIT | MIT | MIT | MIT | MIT | ISC | MIT | MIT | MIT | **MIT** |
| **Primary lang** | MD | MD+TS | Shell | MD | MD+JS | Python | Python | Shell | TS | **Python+MD** |
| **i18n README** | EN | EN | EN | EN | VN+EN | VN-primary | EN | EN+zh-CN | 7-lang | **EN+VN+CN+UK** |

### 2.2 Product + methodology

| Axis | ECC v1 | SP v2 | gstack v3 | GSD v5 | BMAD v11 | codymaster v12 | spec-kit v17 | agency v18 | OMC v27 | **claude-howto v32** |
|------|--------|-------|-----------|--------|----------|----------------|--------------|-----------|---------|----------------------|
| **Product type** | Feature framework | Methodology + skills | Virtual-team methodology | SDD methodology | BMM methodology | 79-skill product | Constitutional SDD | 144-personality agents | Multi-runtime orchestrator | **10-module tutorial** |
| **Core methodology** | Feature patterns | 7-stage TDD | Virtual eng team | SDD | BMM 12-agent | 5-tier memory | 9-article constitution | Agency metaphor | tmux multi-runtime | **Weekend pedagogy** |
| **Skill/component count** | ~30 | ~25 | — | — | 12-15 agents | 79 skills | 7 commands | 144 agents | 19 agents + 15 skills | **45 templates** |
| **Agent count** | — | — | — | — | 12 | — | — | 144 | 19 | **5** |
| **Distribution** | GitHub clone | GitHub clone | GitHub | GitHub | npm + GH | npm + docs | `uv tool install` | GitHub | npm + plugin | **git + EPUB** |
| **Pilot-relevance (Storm Bear)** | Medium | Medium | Medium | Low | HIGH (VN) | HIGH (VN peer) | **HIGH** (methodology) | Medium (consolidation risk) | HIGH (orchestration) | **HIGH** (self-onboarding) |

### 2.3 Intellectual lineage + governance depth

| Axis | ECC v1 | SP v2 | gstack v3 | GSD v5 | BMAD v11 | codymaster v12 | spec-kit v17 | agency v18 | OMC v27 | **claude-howto v32** |
|------|--------|-------|-----------|--------|----------|----------------|--------------|-----------|---------|----------------------|
| **Intellectual influence** | Karpathy | Karpathy | Karpathy | Karpathy | — | — (self-contained) | **John Lam** | Reddit thread | **Sup v2 + ECC v1** (recursive) | **Boris Cherny** |
| **Lineage archetype** | Individual | Individual | Individual | Individual | Self | Self | Individual | Community-viral | Multi-archetype-fusion | **Individual** |
| **SECURITY.md?** | — | — | — | — | — | — | ✅ | ✅ | — | **✅ (334 lines)** |
| **AGENTS.md?** | — | — | — | — | — | — | ✅ | ❌ | — | **❌** |
| **CONTRIBUTING.md?** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **✅ (381 lines)** |
| **CoC?** | — | — | — | — | ✅ | — | ✅ | ✅ | ✅ | **✅** |
| **Governance depth (1-5)** | 2 | 2 | 2 | 2 | 3 | 2 | **5** | 4 | 4 | **4** |

### 2.4 Cross-wiki standards adoption

| Axis | ECC v1 | SP v2 | gstack v3 | GSD v5 | BMAD v11 | codymaster v12 | spec-kit v17 | agency v18 | OMC v27 | **claude-howto v32** |
|------|--------|-------|-----------|--------|----------|----------------|--------------|-----------|---------|----------------------|
| **MCP adoption** | — | — | — | — | — | — | ✅ | ✅ | ✅ | **✅** |
| **OpenClaw ref?** | — | — | — | — | — | ✅ (doc) | — | ✅ (exec) | ✅ (runtime) | **—** |
| **Hermes ref?** | — | — | — | — | — | — | — | — | — | **—** |
| **Testing CI stack** | Minimal | Minimal | Minimal | Minimal | Minimal | Minimal | Extensive | Minimal | Medium | **Extensive (pytest+Ruff+Bandit+mypy)** |
| **Pre-commit hooks?** | — | — | — | — | — | — | ✅ | — | — | **✅ (5 checks)** |

### 2.5 Novel / corpus-first features

| Feature | Wiki introducing | Adopted by others in T1? |
|---------|------------------|--------------------------|
| **Interactive self-assessment quiz-as-slash-cmd** | **claude-howto v32** | N=1 (new) |
| **25-event hook taxonomy** | **claude-howto v32** | Largest at T1 |
| **3-scope CLAUDE.md variant system (named files)** | **claude-howto v32** | N=1 (new) |
| **EPUB offline ebook pipeline** | **claude-howto v32** | N=1 (new) |
| **Ukrainian README** | **claude-howto v32** | N=1 (new) |
| **Mermaid-syntax pre-commit hook** | **claude-howto v32** | N=1 (new) |
| **Multi-runtime tmux orchestration** | OMC v27 | N=1 |
| **144-agent library + personality design** | agency-agents v18 | N=1 |
| **9-article constitutional governance** | spec-kit v17 | N=1 |
| **Multi-archetype-fusion lineage (Pattern #19 new)** | OMC v27 | N=1 |
| **Boris Cherny citation** | **claude-howto v32** | N=1 (new lineage node) |
| **SkillsBench + 5-tier memory** | codymaster v12 | N=1 |
| **Community-viral Reddit-origin** | agency-agents v18 | N=1 |

claude-howto v32 introduces 6 of 13 novel T1 features. Highest novel-feature-introduction per T1 entrant since v18 agency-agents.

---

## Part 3. VN-Regional-Archetype T1 N=2 validation

### 3.1 Formal Pattern #70 proposal

**Pattern ID:** #70 (proposed)
**Name:** VN-Regional-Archetype T1
**Status at v32:** 🟡 CANDIDATE (with structurally-unambiguous-at-N=2 promotion-candidate flag)

**Formal statement:**
> VN-authored T1 framework with VN-language presence in governance (README port, tagline, or primary audience framing). Distinct from US-authored (ECC v1, Superpowers v2, gstack v3, GSD v5, BMAD v11, spec-kit v17, agency-agents v18), Korean-authored (OMC v27 — Pattern #55), and corporate-backed. Two sub-variants emerge at N=2:
>
> **Sub-variant 70a: VN-in-VN**
> - Author resident in Vietnam
> - VN-primary audience
> - VN-first or VN-only README
> - Tagline may be VN-language
> - Example: codymaster v12 (Tody Le, HCMC) — 38 stars, 79 skills, "Code Đi" tagline, product-authored
>
> **Sub-variant 70b: VN-diaspora**
> - Author resident in diaspora location (France / other)
> - Global audience with VN as courtesy port
> - EN-primary README with VN translation (typically <10% length of EN)
> - Tagline in English
> - Example: claude-howto v32 (Luong Nguyen, Paris) — 28.2K stars, 10 modules + 45 templates, "Master Claude Code in a Weekend" tagline, pedagogical

**Promotion path:** Both observations satisfy structurally-unambiguous-at-N=2 criterion (routine v2.1 criterion 2). Pattern #70 promotion-candidate for next mini-audit or full audit.

**Cross-reference:** Analogous to Pattern #55 Korean Regional Archetype T1 (N=1 OMC v27). If Korean reaches N=2 AND VN remains N=2 at future wiki, consider meta-pattern **#73 Regional-Archetype-Registry T1** (consolidation-forward, requires 3 regions with multi-observations). **Deferred pending 3rd region.**

### 3.2 VN-in-VN vs VN-diaspora structural comparison

| Axis | codymaster v12 (70a VN-in-VN) | claude-howto v32 (70b VN-diaspora) |
|------|-------------------------------|--------------------------------|
| **Author full name** | Tody Le | Luong NGUYEN |
| **GitHub handle** | tody-agent/codymaster | luongnv89 |
| **Location** | Ho Chi Minh City | Paris, France |
| **Diaspora?** | No (VN-in-VN) | Yes (France-based) |
| **Employer** | Head of Product at VN company (implied) | Montimage (French cybersecurity) |
| **Primary audience** | VN developers (direct) | Global developers |
| **README language priority** | VN-first | EN-first |
| **VN README length** | Primary/full | 73 lines = 8% of EN 878 lines |
| **Tagline** | "Code Đi" (VN) | "Master Claude Code in a Weekend" (EN) |
| **Time framing** | Open-ended ("vibe coding") | Weekend-specific |
| **Product type** | 79-skill product | 10-module tutorial |
| **Primary lang** | Python | Python + markdown |
| **Packaging** | npm (`@tody/codymaster-cli`) | Git clone + copy-paste |
| **Ecosystem** | tody-agent organization | luongnv89 individual with 116 repos |
| **Scale** | 38 stars | 28,186 stars (742× codymaster) |
| **Forks %** | 55% | 12.2% |
| **Medium blog?** | — | Yes (medium.com/@luongnv89) |
| **Content channels** | GitHub primary | GitHub + Medium + blog + 4-lang README + Twitter + EPUB |
| **Commercial model** | codymaster + tody-agent brand | Free OSS + closed commercial macOS apps (CUStats, TextWiz, separate feedback repos) |
| **Self-assessment** | — | **Interactive slash commands (corpus-first)** |
| **Lineage cited** | — (self-contained) | Boris Cherny (Anthropic) |

### 3.3 Scale-archetype correlation insight

Scale ceiling per sub-variant observed at v32:

| Sub-variant | Observed scale | Hypothesis |
|-------------|----------------|------------|
| 70a VN-in-VN (codymaster) | 38 | Smaller audience (VN-only) → smaller scale ceiling |
| 70b VN-diaspora (claude-howto) | 28,186 | Global audience access + multi-channel → larger scale ceiling |

**742× scale difference** — not proving one sub-variant "better", but demonstrating:
- **Audience reach matters** — VN-diaspora authors targeting global audience access VN-level audiences AND global audiences simultaneously
- **Language strategy matters** — EN-primary with VN port reaches both audiences; VN-primary mostly reaches VN only
- **Multi-channel distribution matters** — Luong's 7-channel approach + Medium blog amplify

**Strategic implication for corpus:** If VN-in-VN author adopts global-audience framing, hypothetically approach VN-diaspora scale. This is falsifiable at future VN T1 wiki.

### 3.4 Analog to Pattern #55 Korean Regional Archetype

**Pattern #55 (existing, N=1, OMC v27):**
- Yeachan Heo — Korean solo creator at Seoul (implied) + 5 Korean collaborators + Korean Ambassador Sigrid Jin + README.ko.md comprehensive
- Multi-runtime orchestration framework
- 30.4K stars in 3.5 months

**Structural parallel:** Both Pattern #55 (Korean) and proposed Pattern #70 (VN) describe:
1. Single regional language/cultural presence at T1
2. Solo authorship typical
3. Regional-community-viral growth
4. Distinct from US-dominant T1 baseline

**Structural differences:**
- Pattern #55 is Korean-in-Korea; no Korean-diaspora observation yet (would validate Korean-diaspora sub-variant like VN 70b)
- Pattern #70 has 2 sub-variants at registration (70a + 70b); Pattern #55 has only 70a-analog (Korean-in-Korea) at v32

**Prediction:** Korean-diaspora T1 author emergence would validate Pattern #55 structural expansion. VN-regional-archetype-registry and Korean-regional-archetype-registry both expected to mature with multi-sub-variant structure over next 5-10 wikis.

### 3.5 Meta-pattern deferred until N=3-region

Consolidation-forward candidate: **Pattern #73 Regional-Archetype-Registry T1** meta-pattern wrapping:
- Pattern #55 Korean (N=1)
- Pattern #70 VN (N=2 — 70a + 70b sub-variants)
- Future Pattern ?? (3rd region — CN? Latin America? Indian-diaspora? Eastern European?)

**Criterion per routine v2.1 meta-pattern-at-N=3-consolidation:** 3 observations across structurally-distinct sub-types.

**At v32 status:** 2 regions (Korean + VN) = insufficient for meta-pattern consolidation. **Explicit decision: register Pattern #70 as standalone candidate; defer meta-pattern until 3rd region emerges.** Absorption-retirement mechanism available (Pattern #55 + #70 could absorb into #73 when 3rd region appears and criterion cleared).

### 3.6 VN-Regional-Archetype ripple effects in corpus

At v32, VN is 20% of T1 corpus (2 of 10). This is:
- Largest non-US regional representation at T1
- Larger than Korean (1 of 10 = 10%)
- Approaches critical mass for regional-cluster observability

**Hypotheses for future wikis:**
1. **H1 (continuation):** 3rd VN T1 emerges within 5-10 wikis → Pattern #70 matures + strengthens meta-pattern
2. **H2 (Korean-diaspora):** Korean-diaspora T1 emerges → Pattern #55 gets 70b-analog sub-variant
3. **H3 (3rd region):** CN-solo-authored T1 OR Latin-America T1 emerges → meta-pattern #73 consolidation viable
4. **H4 (VN-cluster):** Storm Bear itself eventually publishes → corpus-adjacent 3rd VN T1 (but structurally outside corpus by ownership)

**Storm Bear strategic note:** If operator publishes Storm Bear vault as T1-like framework, VN regional cluster becomes N=3 and Pattern #70 meta-pattern-consolidation-candidate is triggered.

---

## Part 4. Pattern Library impact at v32

### 4.1 New candidates registered at v32

**Proposed #70 VN-Regional-Archetype T1:**
- Evidence: codymaster v12 + claude-howto v32
- Status: 🟡 CANDIDATE at N=2 structurally-unambiguous
- Promotion-recommendation: AT NEXT AUDIT (mini-audit or full audit) — conservative per routine v2.1 audit discipline (no mid-wiki promotion)
- Sub-variants: 70a VN-in-VN + 70b VN-diaspora

**Proposed #71 Interactive Self-Assessment Mechanism:**
- Evidence: claude-howto v32 (`/self-assessment` + `/lesson-quiz [topic]`)
- Status: 🟡 CANDIDATE N=1 stale-risk-flagged (per v2.1 routine)
- Required for promotion: 2nd framework with runtime interactive self-assessment embedded in product
- Stale-check: v37 (+5 wikis) / retire-check: v42 (+10 wikis)
- Prediction: Low-medium (educational-tech is niche)

### 4.2 Existing patterns strengthened at v32

| Pattern | Status | Evidence added at v32 |
|---------|--------|----------------------|
| #17 Ecosystem-Layer Organizations (variant 1) | ✅ confirmed | Luong's 15+ repo portfolio — 8th data point |
| #19 Intellectual Lineage Archetype 1 | ✅ confirmed | Boris Cherny = 3rd individual-author influence node (6 total touchpoints) |
| #20 Solo-Scale Ceiling dictionary | 🔄 reformulated | Add row: "Solo pedagogical-tutorial + ecosystem-portfolio" ~28K/5.5mo |
| #24 SECURITY.md T1 | ✅ confirmed | 4th T1 data point (334-line SECURITY.md) |
| #27 Community-Viral Scale Path | ✅ confirmed | 9th data point, new sub-path "VN-diaspora-pedagogical-multi-channel" |
| #55 Korean Regional Archetype T1 | 🟡 candidate | stale-check due at v32 — REMAINS N=1; stale-risk elevated but stay-as-candidate (analog #70 establishes family structure) |

### 4.3 Patterns NOT strengthened (notable absences/counter-evidence)

| Pattern | Status | Observation at v32 |
|---------|--------|--------------------|
| #22 AGENTS.md as Industry Standard | ✅ confirmed | **Absence** — claude-howto does NOT use AGENTS.md (2nd absence after agency-agents v18); narrows scope to meta-framework-specific |
| #23 AI-Disclosure Policy Emergence | ❌ RETIRED v27 audit | **No revival** — CONTRIBUTING.md lacks AI-disclosure despite Claude-Code focus; strengthens retirement rationale |
| #25 Personality-Driven Agent Design | ❌ RETIRED v27 audit | **No revival** — claude-howto's 5 subagents are role-based |
| #45 Dual-Licensing | ⏳ stale N=1 | No un-stale — claude-howto is single MIT |
| #46 Duo-Founder | ⏳ stale N=1 | No un-stale — solo author |
| #51 Vibe-Coding Spectrum | ✅ confirmed | Mixed signal — Luong has `vibe-coding` repo (pro) but claude-howto is structured-anti-vibe (con); observation noted, no new pole evidence |
| #57 Recursive Corpus Reference | 🟡 candidate N=1 | **No un-stale via citation** — claude-howto does not cite prior corpus items; stays N=1. Latent bridge via `unsloth-mlx` observed but structurally distinct from citation |

### 4.4 Ratio impact projection

**Post-v32 state (direct registration, no promotion):**
- 32 confirmed + 26 active + 4 stale + 6 retired + 1 observation-track = 69 full / 58 active
- Ratio 26:32 = **0.81:1** (still healthy — below 0.95:1 mini-audit trigger)

**If Pattern #70 promoted at next audit:**
- 33 confirmed + 25 active + 4 stale + 6 retired + 1 observation-track = 69 full / 58 active
- Ratio 25:33 = **0.76:1**

**Audit recommendation:** Mini-audit viable at next wiki (v33) if ratio approaches 0.95:1 OR if Pattern #70 promotion is time-sensitive. Otherwise routine mini-audit at +5 wikis (v37).

---

## Part 5. Storm Bear strategic implications

### 5.1 Corpus-application phase confirmation

v26 was strategic inflection ("5/5 tier validation structural milestone"). Since then (v26-v32), corpus has been in **application phase** — using accumulated patterns to evaluate new wikis. v32 validates:
- v2.1 discipline (overlap pre-check / un-stale / counter-evidence / consolidation-forward) — FIRST EXECUTION clean pass
- Phase 0.9 per-wiki meta-entity evaluation — YES for v32 (meta-relevance clear)
- v2.1 audit cadence reform — ratio projection 0.81:1 keeps buffer below mini-audit trigger

### 5.2 Operator-facing backlog escalation

Per v2.1 operator-facing backlog discipline:
- v16 "run graphify on Storm Bear vault" — deferred ~16 sessions → stale, but not BLOCKING
- **v27 diagnostic HIGH bundle — deferred 5+ sessions → BLOCKING-RECOMMENDATION tag applied**
- v32 NEW: claude-howto self-onboarding 13h weekend + optional 3-scope CLAUDE.md refactor

**Strategic recommendation in Phase 5 final report: v27 diagnostic HIGH bundle escalated to BLOCKING-RECOMMENDATION.**

### 5.3 Pilot ranking refresh at v32

| Rank | Wiki | Purpose | Effort |
|------|------|---------|--------|
| **1 (NEW)** | **claude-howto v32** | **Operator self-onboarding — meta-ROI** | **~13h weekend** |
| 2 | spec-kit v17 | Methodology for Scrum | — |
| 3 | OMC v27 | Multi-runtime orchestration | — |
| 4 | BMAD v11 | VN methodology at scale | — |
| 5 | markitdown v28 | Scrum doc ingestion | — |
| 6 | crawl4ai v29 | Web research utility | — |
| 7 | gws v13 | Google Workspace VN-enterprise | — |
| 8 | codymaster v12 | VN-peer observational | — |
| 9 | multica v15 | Linear-analog agent platform | — |
| 10 | graphify v16 | Vault graph extraction | — |
| 11 | agency-agents v18 | 144-agent library | — |

claude-howto at #1 because it is **the self-improvement investment that amplifies all other pilot effectiveness**. Operator completing 13h weekend → better-equipped to adopt spec-kit methodology, markitdown ingestion, crawl4ai research, etc.

### 5.4 Corpus health at v32

| Metric | Value | Status |
|--------|-------|--------|
| Wiki count | 32 | +1 at v32 |
| Tier distribution | T1=10 / T2=2 / T3=2 / T4=6 / T5=4 / outside-scope=8 | 5/5 validated |
| Velocity plateau | 27 consecutive wikis at ~2h (v6-v32) | Preserved |
| Pattern Library ratio | 0.81:1 (projected) | Healthy |
| v2.1 discipline | First execution clean | Validated |
| Operator-facing backlog | v27 diagnostic HIGH = 5+ sessions | **BLOCKING-RECOMMENDATION** |

---

## Part 6. Summary + next action

### 6.1 v32 meta-milestones

1. **T1 extends to N=10** (largest tier further extended)
2. **VN-Regional-Archetype T1 N=2** — proposed Pattern #70 (structurally-unambiguous-N=2 promotion-candidate)
3. **VN-diaspora sub-variant** distinct from VN-in-VN established structurally
4. **Pattern #19 archetype 1** — Boris Cherny 3rd influence node (6th touchpoint)
5. **Pattern #24 SECURITY.md** — 4th T1 data point
6. **Pattern #27** — 9th sub-path (VN-diaspora-pedagogical-multi-channel)
7. **First v2.1-era routine execution** — clean pass
8. **21st consecutive Storm Bear meta-entity** (per Phase 0.9 applicability)
9. **27 consecutive wikis at ~2h velocity plateau**
10. **10+ corpus-firsts at claude-howto v32**

### 6.2 Next action

**Strategic:** Before v33, execute v27 diagnostic HIGH bundle (BLOCKING-RECOMMENDATION; deferred 5+ sessions).

**Or alternatively:** If operator prefers skill-upgrade over diagnostic, start claude-howto Week 1 self-onboarding (3h Week 1 + sustained 13h over 5 weeks) — high-leverage investment that benefits all downstream work.

**Routine:** At v33, run mini-audit (ratio at 0.81:1, pattern #70 promotion-candidate ready, 2 new candidates since v31). Validate Pattern #70 promotion under structurally-unambiguous-at-N=2 criterion.

---

**(C) Generated 2026-04-22. Phase 4b deliverable for wiki v32 claude-howto.**
