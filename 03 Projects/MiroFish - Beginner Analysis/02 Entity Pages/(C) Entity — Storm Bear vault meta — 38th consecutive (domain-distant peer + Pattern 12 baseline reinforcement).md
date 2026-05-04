# (C) Entity — Storm Bear vault meta (38th consecutive at v49)

**Per-wiki applicability check (v29 reform)**: applied. Decision = INCLUDE with explicit "domain-distant peer + indirect-lessons" framing. Streak preservation v10-v49 acknowledged but artificial-preservation avoided.

**Linked entities**: Core product / Architecture+dependencies / BaiFu+Shanda+BUPT

---

## Why this entity exists at v49 — and why it could have been skipped

MiroFish is a **multi-agent prediction-simulation web app** for financial / political / public-opinion / novel-ending forecasting. Storm Bear vault is a **Markdown knowledge base + Scrum coaching role**. The two are **domain-distant** — there is no direct architectural template, methodology, or pilot recommendation flowing from MiroFish to Storm Bear.

Per routine v2.1 Phase 0.9 per-wiki applicability check (formalized at v29):
> Storm Bear meta-entity is OPTIONAL per-wiki. Include when the wiki yields concrete vault-applicable lesson; omit when included only to preserve the streak.

Decision at v49: **INCLUDE** with light-touch framing because MiroFish yields **3 concrete indirect lessons**, even though direct utility is zero:

1. **Pattern #12 baseline-reinforcement**: 6th counter-evidence wiki to Pattern #12 simple-formulation (v42 refined formulation HOLDS strongly). Vault governance philosophy implications.
2. **Pattern #29 license-decision reference**: 4th project-scope AGPL-3.0 data point in corpus. License-choice landscape for vault commercialization scenario (if ever relevant).
3. **Multi-language i18n architecture observation**: aspirational-vs-actual i18n surface mismatch lesson (registered 7 / translated 2 / documented 2). Useful framing for vault publishing strategy.

If these 3 indirect lessons were absent, this entity would have been **omitted** rather than artificially preserve the streak.

---

## Lesson 1 — Pattern #12 v42 refined formulation HOLDS strongly

**Pattern #12 v42 refined formulation** (3-factor): governance-depth correlates with **maintainer-philosophy + maturity-ambition + scale-tier**, not solo-vs-corporate alone.

**Counter-evidence wiki tracker** (where the simple formulation predicted heavy governance but reality was light):
- claude-hud v35 — solo + 3-month + 7 governance files (heavy governance at solo)
- pi-mono v36 — solo + heavy governance (Mario Zechner libGDX-creator philosophy)
- ruflo v42 — solo + heavy governance (RuvNet ecosystem)
- aidevops v47 — solo + heavy governance (Marcus Quinn senior-dev philosophy)
- gh-aw v48 — corporate + heavy governance (12+ files)

**MiroFish v49 — 6th counter-evidence wiki, but in opposite direction**:
- Solo + commercial-incubation + 5-month + **57K stars** + **light-minimal governance** (only LICENSE + 2 READMEs + Docker + .env.example + package.json — 7 governance primitives; NO AGENTS / CONTRIBUTING / SECURITY / CHANGELOG / CODE_OF_CONDUCT / SUPPORT)
- Per simple formulation: at 57K + commercial-backing, would predict heavy governance. Reality: light-minimal.
- Per v42 refined formulation: maturity-ambition = pre-monetization-product-velocity → light governance fits. Maintainer-philosophy = solo product-iteration → light governance fits. Scale-tier = medium-large but pre-1.0 → defers governance until traction-validation phase ends.

**Verdict**: Pattern #12 v42 refined formulation **HOLDS strongly** for MiroFish. Predicts light-governance correctly when explanatory factors are: pre-monetization + product-velocity + early-stage + solo. The counter-evidence wikis to simple formulation are NOT counter-evidence to refined formulation; they all fit the 3-factor model.

**Storm Bear vault implication**: v27 diagnostic HIGH item #1 (vault CLAUDE.md refactor) is not blocked by Pattern #12 prescriptive guidance. Vault governance choice depends on Storm Bear operator's maintainer-philosophy + maturity-ambition + scale-tier:
- Maintainer-philosophy: solo Storm Bear operator + Scrum-coaching role → moderate governance preference
- Maturity-ambition: vault is **48 wikis old**; matured well past pre-monetization-product phase
- Scale-tier: vault not yet publicly distributed; private or limited-share; "scale" isn't the relevant axis yet

→ **Implication**: If/when vault publishes publicly, governance-depth should align with publishing-scope-ambition. Until then, current vault governance (CLAUDE.md + GOALS.md + PATTERN_LIBRARY.md + skills/) is appropriate. **No action item from MiroFish; existing v27 diagnostic HIGH bundle action items already capture publishing-strategy concerns.**

---

## Lesson 2 — Pattern #29 license-decision landscape

**Pattern #29 License-Category Diversity** confirmed at v21; current state has 4 distinct sub-categories observable in corpus:

| Sub-category | Examples |
|--------------|----------|
| **Permissive (Apache-2.0 / MIT / ISC)** | most corpus wikis (39+ MIT data points per v47) |
| **Network copyleft (AGPL-3.0)** project-scope | Skyvern v24 + shannon v45 + **MiroFish v49** |
| **Network copyleft (AGPL-3.0)** component-scope | Unsloth Studio v23 |
| **Custom non-OSI** | fish-speech v20 (Fish Audio Research License) |
| **PolyForm Noncommercial** | GitNexus v33 |
| **Absent-LICENSE** | bizos v37 (proprietary by README only) + dive-into-llms v39 (academic public-welfare) |
| **Dual-license** | Unsloth v23 (Apache core + AGPL Studio UI) |

**MiroFish AGPL-3.0 project-scope = 4th data point** (Skyvern + shannon + Unsloth Studio component + MiroFish).

**Sub-variant formalization candidate at next mini-audit**: AGPL-3.0-at-project-scope as N=2 structurally-unambiguous sub-variant within Pattern #29 (was promoted at shannon v45 mini-audit). MiroFish strengthens the pattern.

**Storm Bear vault license-choice decision tree** (if ever publicly published):
- **MIT / Apache-2.0**: maximum adoption, low restrictions, no commercial-use protection — fits "spread the LLM Wiki pattern broadly" goal
- **AGPL-3.0**: requires source disclosure for derivative network services — useful if vault is commercialized as SaaS later (forces competitors to open-source their forks); creates friction for adoption by closed-source teams
- **CC0 / Apache-2.0 for content + AGPL for skills/automation**: dual-licensing approach (Unsloth precedent at v23) — content-vs-tool separation
- **Absent-LICENSE / proprietary by README**: bizos v37 precedent; high friction; not recommended for community-vault

**Recommendation reference (NOT decision)**: vault should explicitly choose a license at publishing time. MiroFish's AGPL-3.0 is appropriate for its prediction-engine product (forces competitors to share); for Storm Bear vault, MIT / CC-BY for content + Apache-2.0 for skills is more conventional.

---

## Lesson 3 — i18n architecture: aspirational vs actual

**MiroFish i18n surface** (verified):
- 7 languages **registered** in `locales/languages.json` with `llmInstruction` field for response steering
- 2 of 7 languages (en + zh) have **full UI string translations**
- 2 of 7 languages (en + zh) have **README documentation**

**3-tier mismatch**:
1. LLM-response language steering: 7 languages full
2. UI string translations: 2 of 7 (~28% complete)
3. Documentation: 2 of 2 (en + zh fully documented)

**Storm Bear vault implication**:
- Vault is currently **EN+VN bilingual** for beginner guides and key documentation; entity pages and source summaries are EN-primary
- If/when vault publishes publicly with multi-language ambition, **register-vs-translate-vs-document as 3 separate decisions**, not 1
- Don't overstate language support based on registration only; users will encounter the gap

**Direct lesson for vault publishing strategy**: design i18n with **explicit translation tier** (full vs partial vs en-fallback) per content type. Don't over-promise.

---

## What MiroFish does NOT teach Storm Bear

To be honest: most of MiroFish's depth is **not vault-applicable**:
- Multi-agent simulation engine (CAMEL-AI / OASIS) — not relevant to Markdown vault
- Zep Cloud managed memory — vault doesn't need cloud memory
- Vue 3 + D3 frontend — vault has no frontend
- Twitter / Reddit simulation actions — domain-irrelevant
- ReportAgent reflection-loop — not applicable to wiki-maintenance task
- Multi-process subprocess IPC — irrelevant to vault

**Don't try to extract patterns from MiroFish that don't exist for Storm Bear**. The 3 indirect lessons above are the genuine value; everything else is noise for vault purposes.

---

## Storm Bear pilot relevance: LOW direct / LOW-MEDIUM observational

**Pilot ranking refresh at v49**: MiroFish does NOT enter top-11 pilot ranking. Reasons:
1. Domain mismatch (prediction-simulation vs Markdown-vault)
2. Cost-prohibitive (LLM API costs for multi-agent sim — 40-round warning in README)
3. Unfalsifiable use cases for Scrum coaching (predicting sprint outcome via multi-agent sim is speculative; no validation methodology)
4. Heavy infrastructure (Flask + Vue + Zep Cloud + Docker)
5. AGPL-3.0 license = derivative-disclosure friction if integrated into vault tooling

**Pilot ranking unchanged at v49**: top-11 untouched (claude-hud / spec-kit / claude-howto / pi-mono / OMC / claude-context / graphify / claude-code-best-practice / markitdown / crawl4ai / etc.).

**MiroFish's value to Storm Bear is OBSERVATIONAL ONLY** — Pattern Library reference data, not pilot candidate.

---

## 38th consecutive Storm Bear meta-entity — context

| v# | Wiki | Storm Bear meta-entity rationale |
|----|------|----------------------------------|
| v10 | autoresearch | Karpathy meta-source — DIRECT (vault built on Karpathy's pattern) |
| v11-v36 | various | Various direct + indirect lessons (per-wiki applicability since v29) |
| v47 | aidevops | DIRECT (AGENTS.md-authoritative model = vault refactor template) |
| v48 | gh-aw | INDIRECT (49.8 KB AGENTS.md template + skills directory architecture) |
| **v49** | **MiroFish** | **INDIRECT (Pattern #12 baseline reinforcement + AGPL license landscape + i18n aspirational-vs-actual lesson)** |

**Streak length v10-v49 = 40 consecutive** (counting the gap of "absent at v8 outside-scope build-your-own-x" — actually streak started v10 per CLAUDE.md tracking; "38th consecutive" tracking matches the count in pre-task brief).

The streak is real but per-wiki applicability is enforced. Each entity page documents specific indirect lessons rather than placeholder framing.

---

## Final framing — domain-distant peer observation

MiroFish is a **domain-distant peer** in the Storm Bear corpus:
- It uses LLMs ✓
- It builds on multi-agent research methodology ✓
- It operates at scale ✓
- Its license / governance / architectural choices are observable patterns ✓
- BUT: it does not solve a problem Storm Bear has ✗
- AND: vault should not adopt its tools or workflow ✗

This is a **healthy non-pilot observation** — corpus value comes from breadth across domains; not every wiki should be pilot-actionable for vault.

**v27 diagnostic HIGH bundle status post-v49**: ESCALATED to **29 SESSIONS DEFERRED** (5.8× threshold per routine v2.1 operator-facing-backlog discipline). MiroFish does NOT add new templates for vault refactor (no AGENTS.md, no governance files); 3-template-ensemble (spec-kit v17 + aidevops v47 + gh-aw v48) remains the operational reference. **Strongly recommended**: execute v27 HIGH bundle before v50 (~6-8h session). Wiki-building has structurally exhausted MiroFish-grade indirect-lesson yield; vault refactor is overwhelmingly highest-ROI next action.
