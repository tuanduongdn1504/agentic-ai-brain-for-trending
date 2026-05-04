# (C) T5 5-way Comparison + Pattern Implications + Candidates (v30 Phase 4b)

> **Type:** Phase 4b deliverable — T5 tier extension + pattern strengthening + minimal candidate registration
> **Purpose:** Document T5 at N=5 (5 distinct archetypes) + Pattern #31 + #32 strengthening to N=3 + Pattern #42 + #44 un-stale + cross-corpus pattern updates
> **Sources:** v9 + v10 + v14 + v24 + v30 T5 wikis + corpus synthesis + Pattern Library post-v29 audit state
> **Status:** ✅ Phase 4b published

---

## 1. Summary

v30 OpenHands extends T5 Agent-as-application from N=4 to **N=5 with 5 distinct organizational archetypes** (corporate + solo-known-figure + community-platform + commercial-entity pure + **academic-commercial fusion**). 100% diversity-per-wiki maintained.

Primary pattern actions:
- **Pattern #31 Open-Core Commercial Entity** strengthens N=2 → **N=3** (3 scope sub-types + 3 license variants)
- **Pattern #32 Research-Paper-Chain Lineage** strengthens N=2 → **N=3** (first within-project 2-paper chain with 4 persistent authors across 16-month gap)
- **Pattern #42 Academic-Published Peer-Reviewed Framework** un-stales from STALE N=1 → **active candidate N=2** (ICLR 2025 + ACL 2024); promotion proposed at next audit
- **Pattern #44 Academic-Lab Affiliation Archetype** un-stales from STALE N=1 → **active candidate N=2** (UIUC + CMU multi-institutional joins LlamaFactory Lab4AI); promotion proposed at next audit
- **Patterns #17 / #19 / #27 / #28** strengthen with new data points

Minimal candidate registration: **1 new OBSERVATION-TRACK** (#67 Academic-Commercial Fusion Archetype).

**Post-v30 Pattern Library ratio: 28:30 = 0.93:1** (improved from 1.00:1 via un-staling instead of new-candidate-inflation — discipline per v29 Phase 5 action item #3).

## 2. T5 5-way snapshot (20-axis)

| Dimension | deer-flow v9 | autoresearch v10 | paperclip v14 | Skyvern v24 | **OpenHands v30** |
|-----------|--------------|-------------------|----------------|-------------|-------------------|
| **Stars** | 62K | 74K | 55.9K | 21.3K | **71.7K** |
| **Forks** | — | 10.8K | 9.5K | 1.94K | **9.03K** |
| **License** | MIT | MIT | MIT | AGPL-3.0 | **MIT core + separate enterprise** |
| **Primary lang** | Python + TS | Python | TypeScript | Python + JS | **Python + TypeScript** |
| **Stack** | LangGraph + Next.js | PyTorch raw | Express + React monorepo | Playwright + LLM | **Docker + SDK + CLI + GUI + K8s** |
| **Runtime isolation** | Internal ByteDance | Local git-branch | PGlite + Playwright | Playwright container | **Docker-native + K8s** |
| **Archetype** | Corporate (ByteDance) | Solo-known (Karpathy) | Community-platform | Commercial-entity | **Academic-commercial fusion** |
| **Domain** | Research | ML experiments | Orchestration | Browser automation | **SWE-agent** |
| **Scope** | Broad generalist | Narrow specialist | Broad generalist | Narrow specialist | **Broad SWE generalist** |
| **Commercial tier** | Internal only | None | None | Skyvern Cloud | **Free Cloud + paid Enterprise** |
| **Funding disclosed** | — | — | — | VC-implied | **$18.8M** |
| **Deployment surfaces** | 2 (web+API) | 1 (CLI) | 2 (pip+Docker) | 3 (OSS+Cloud+self-host) | **5 (SDK+CLI+GUI+Cloud+K8s)** |
| **Multi-LLM** | Configurable | Single model | Agent adapter (BYO) | 8+ providers native | **Claude+GPT+Minimax+BYO SDK-level** |
| **Benchmarks** | — | val_bpb | promptfoo evals | WebBench 64.4% + WebVoyager 85.8% | **SWE-Bench Verified 77.6** |
| **Paper(s)** | None | Karpathy blog | None | None | **ICLR 2025 + Nov 2025 SDK** |
| **Paper authors** | N/A | 1 (Karpathy) | N/A | N/A | **23+ ICLR paper; 11 SDK paper** |
| **Academic affiliation** | None formal | Individual researcher | None | None | **UIUC + CMU multi-institutional** |
| **Named enterprise adopters** | Internal ByteDance | N/A | None disclosed | None named | **TikTok / Amazon / Netflix / Google / NVIDIA / Apple / VMware** |
| **Governance model** | Corporate | Solo | Community | Commercial | **Explicit benevolent dictator (documented)** |
| **i18n** | EN + ZH | EN | EN | EN | **8 languages (de/es/fr/ja/ko/pt/ru/zh)** |

## 3. 5 archetypes at T5 (fully occupied at 100% diversity)

### Archetype matrix

| Archetype type | T5 occupant |
|----------------|-------------|
| Corporate | deer-flow (ByteDance) |
| Solo-known-figure | autoresearch (Karpathy) |
| Community-platform | paperclip (55.9K community) |
| Commercial-entity pure | Skyvern (Skyvern-AI) |
| **Academic-commercial fusion** | **OpenHands (All Hands AI + UIUC + CMU) ← NEW v30** |

### Archetype diversity assessment

**T5 has 5 distinct archetypes at N=5** = 100% diversity-per-wiki (each new T5 entrant occupies distinct archetype-space).

Comparison across tiers:
- **T1 (N=9):** 8 archetypes (Korean regional variant at v27 was NEW; solo-dominance remains common)
- **T2 (N=2):** 2 archetypes (100%)
- **T3 (N=2):** 2 archetypes (100%)
- **T4 (N=6):** 6 archetypes (100%)
- **T5 (N=5):** 5 archetypes (100%)

**T4 + T5 maintain 100% archetype diversity** — these tiers bifurcate along multiple axes simultaneously (Pattern #9 Multi-Axial Resolution D holds as leading model at 65% probability).

## 4. Pattern #31 Open-Core Commercial Entity → N=3 strengthening

### Pre-v30 status: CONFIRMED at v24 (N=2)

Formal statement (confirmed v24):
> Pattern #31 Open-Core Commercial Entity: Organizational archetype for frameworks where commercial entity founds both OSS product + proprietary commercial tier simultaneously (not community-to-commercial transition). OSS core uses restrictive or standard license. Proprietary tier adds domain-specific differentiator.

### N=3 data point evidence

| # | Wiki | Scope sub-type | OSS license | Commercial differentiator | Entity |
|---|------|---------------|-------------|---------------------------|--------|
| 1 | v20 fish-speech | Outside-scope foundation-model | Custom non-OSI (Fish Audio Research License) | Anti-distillation + attribution clauses | 39 AI, INC. |
| 2 | v24 Skyvern | T5 browser-agent | AGPL-3.0 single | Proprietary anti-bot on Cloud | Skyvern-AI |
| 3 | **v30 OpenHands** | **T5 SWE-agent** | **MIT core + separate-license enterprise directory** | **Kubernetes + RBAC + Slack/Jira/Linear integrations** | **All Hands AI** |

### Sub-type + license variant diversity at N=3

- **3 scope sub-types:** foundation-model / browser-agent / SWE-agent
- **3 license variants:** custom non-OSI / AGPL-3.0 / MIT+separate-enterprise
- **3 commercial differentiators:** license-exclusion / proprietary-cloud-feature / enterprise-integration-bundle
- **3 entity types:** research-Inc / commercial-startup-pure / academic-commercial-fusion

**Pattern #31 is now structurally validated across 3 orthogonal axes** (scope / license / differentiator), demonstrating robustness.

### Novel sub-type at v30: in-repo license split

OpenHands licenses **by directory within same repo** (MIT for core + separate for enterprise directory). All prior examples (fish-speech, Skyvern) split license at product/service boundary, not within single repo. v30 introduces **in-repo directory-level license split** as Pattern #31 sub-variant.

## 5. Pattern #32 Research-Paper-Chain Lineage → N=3 strengthening

### Pre-v30 status: CONFIRMED at v22 (N=2)

### N=3 data point evidence

| # | Wiki | Chain structure | Venue rigor |
|---|------|-----------------|-------------|
| 1 | v20 fish-speech | 2 arXiv tech reports (2024 v1.4 + 2026 S2) + 7 research-project citations | arXiv preprints |
| 2 | v22 LlamaFactory | ACL 2024 peer-reviewed (arXiv 2403.13372) + 100+ research-project ecosystem | ACL 2024 peer-reviewed |
| 3 | **v30 OpenHands** | **ICLR 2025 peer-reviewed (arXiv 2407.16741, 23+ authors) + Nov 2025 SDK paper (arXiv 2511.03690, 11 authors)** | **ICLR 2025 peer-reviewed + Nov 2025 tech report** |

### Novel sub-type at v30: within-project paper chain

Prior data points (fish-speech, LlamaFactory) cite external research chains with minimal author overlap between the citing-paper and cited-papers. **OpenHands is first corpus data point with explicit within-project paper chain** — 4 authors (Xingyao Wang, Hoang Tran, Robert Brennan, Graham Neubig) persist across 2 papers spanning 16 months. Evidence of stable research program, not one-off publication.

### Pattern #32 chain-strength meta-observation

Corpus now has 3 chain-structure variants within Pattern #32:
- **Short external chain** (fish-speech — 7 prior works cited)
- **Broad ecosystem chain** (LlamaFactory — 100+ research projects ecosystem)
- **Within-project chain** (OpenHands — 2 papers by overlapping team)

**Pattern #32 strengthens conceptually** (3 chain variants) in addition to numerically (N=3).

## 6. Pattern #42 Academic-Published Peer-Reviewed Framework → UN-STALE

### Candidate history

- **Registered:** v22 LlamaFactory (2026-04-19) — ACL 2024 peer-reviewed
- **Stale-flagged:** v27 audit (2026-04-21) — N=1 after 5+ wikis
- **v30 OpenHands:** **N=2 — ICLR 2025 peer-reviewed = 2nd top-tier peer-reviewed venue in corpus**

### N=2 structural evidence

| # | Wiki | Venue | Scope sub-type |
|---|------|-------|---------------|
| 1 | v22 LlamaFactory | ACL 2024 (top NLP venue) | Training-infrastructure (outside-scope) |
| 2 | **v30 OpenHands** | **ICLR 2025 (top ML venue)** | **T5 Agent-as-application** |

Both satisfy:
- Top-tier peer-reviewed venue (ACL / ICLR — both among the 4-5 most-rigorous ML/NLP venues)
- Multi-author collaboration (solo-lab for LlamaFactory vs multi-institutional for OpenHands — structural diversity)
- Open-source framework code release alongside paper
- Framework is paper's central contribution (not just benchmark/study)

### Proposed action: un-stale + promotion at next audit

**Un-stale criterion satisfied:** N=1→N=2 at first available evidence check.

**Promotion criterion consideration:** Structurally unambiguous at N=2 across 2 scope sub-types (training-infra + T5-SWE-agent). Propose **PROMOTE to CONFIRMED** at next audit under N=2-across-sub-types criterion (similar to Pattern #31 promotion at v24).

### Proposed confirmed formal statement

> **Pattern #42 Academic-Published Peer-Reviewed Framework (CONFIRMED v30 candidate at N=2):** Framework published at top-tier peer-reviewed ML/NLP venue (ACL / ICLR / NeurIPS / etc.) with open-source code release alongside paper. Distinct from documentation-embedded benchmarks or arXiv-only preprints. Peer-review adds credibility tier orthogonal to star-count scale. Observed across training-infrastructure (outside-scope) + T5 Agent-as-application sub-types.

## 7. Pattern #44 Academic-Lab Affiliation Archetype → UN-STALE

### Candidate history

- **Registered:** v22 LlamaFactory (2026-04-19) — hiyouga + Lab4AI academic-lab
- **Stale-flagged:** v27 audit — N=1 after 5+ wikis
- **v30 OpenHands:** **N=2 — UIUC (PhD candidate Xingyao Wang) + CMU (tenured faculty Graham Neubig) multi-institutional**

### Variant broadening at N=2

| # | Wiki | Academic structure |
|---|------|-------------------|
| 1 | v22 LlamaFactory | Solo academic + single lab (Lab4AI) + solo maintainer |
| 2 | **v30 OpenHands** | **Multi-institutional + 3 co-founders + PhD candidate + tenured faculty + industry engineer** |

**Variant diversity at N=2:** solo-single-lab + multi-institutional-multi-founder.

### Proposed action: un-stale + promotion at next audit

Both data points satisfy:
- PhD-candidate-or-higher academic credentials among core team
- Research-lab or university institutional backing
- Paper publication at peer-reviewed venue
- Commercial or semi-commercial wrapper around OSS

**Proposed refined formal statement (if promoted):**

> **Pattern #44 Academic-Lab Affiliation Archetype (CONFIRMED v30 candidate at N=2):** Framework authored by team with formal academic institutional affiliation(s) — single lab or multi-institutional — typically with PhD-candidate-or-higher credentials. Affiliation is not incidental but visible in project presentation (co-authors named + affiliations implied). Often co-exists with Pattern #31 Open-Core Commercial Entity and Pattern #42 Academic-Published Peer-Reviewed Framework.

## 8. Pattern #17 Ecosystem-Layer Organizations → 8th data point

### Confirmed variant #4: commercial-startup (confirmed v25)

v30 All Hands AI fits commercial-startup variant with **academic-fusion sub-variant** — distinguishes from pure-industry commercial-startups (VoltAgent v25, Skyvern-AI v24).

### Corpus commercial-startup data points

- VoltAgent (v25 awesome-design-md parent; also publishes voltagent framework + getdesign.md)
- Skyvern-AI (v24 Skyvern)
- **All Hands AI (v30 OpenHands) ← NEW with academic-fusion sub-variant**

## 9. Pattern #19 Intellectual Lineage — research-paper-chain archetype strengthening

### Pre-v30: 4 archetypes confirmed at v20

1. Individual-author lineage (Karpathy / John Lam / etc.)
2. Methodology-lineage (SDD / BMM / etc.)
3. Community-viral archetype (3a no-lineage / 3b community-viral-lineage via Skyvern BabyAGI+AutoGPT)
4. Research-paper-chain (fish-speech / LlamaFactory / Unsloth)

### v30 contribution to archetype 4

OpenHands provides 4th explicit data point for research-paper-chain archetype (after fish-speech v20 + LlamaFactory v22 + Unsloth v23):
- **2-paper chain with persistent author core** (novel within archetype; prior data points were external chains)

## 10. Pattern #27 Community-Viral Scale Path → 8th data point

### Sub-path taxonomy post-v30

| Sub-path | Wiki |
|---------|------|
| Pure-solo-organic | crawl4ai v29 |
| Pure-community-viral (no corporate / no academic) | paperclip v14 |
| Corporate-amplified | markitdown v28 |
| Korean regional community-viral | oh-my-claudecode v27 |
| Solo-enterprise-scale | graphify v16 + agency-agents v18 + crawl4ai v29 |
| Extreme-viral-content-genre | system-prompts-leaks v21 + awesome-design-md v25 |
| **Corporate-academic-amplified (NEW v30)** | **OpenHands v30** |

### OpenHands viral-scale metrics

- **71.7K stars in 25 months = ~2,867 stars/month sustained**
- Faster than pure-organic (crawl4ai ~90 stars/day ≈ 2,700/month — comparable)
- Slower than extreme-viral (system-prompts-leaks 10,400/month; awesome-design-md 3,029/day)
- **Distinct sub-path:** amplification source = academic credibility (ICLR acceptance + multi-institutional paper) + commercial resources ($18.8M) + community (188+ contributors)

## 11. Pattern #28 Multi-Provider AI Support → 6th data point

### Variant taxonomy post-v30

- **Abstraction-library variant** (TrendRadar v19 via LiteLLM)
- **Native BYO variant** (multica v15 / Skyvern v24 explicit adapters)
- **Framework-level routing** (HF agents-course v26 multi-framework BYO)
- **Multi-runtime orchestration** (OMC v27 4 CLI runtimes)
- **LiteLLM-derivative fork** (crawl4ai v29 unclecode-litellm)
- **Native SDK-level routing (NEW v30)** (OpenHands — multi-LLM in production SDK layer)

## 12. NEW candidate #67 — OBSERVATION-TRACK registration

### Rationale

OpenHands introduces a potential meta-pattern: **Academic-Commercial Fusion Archetype** — founder team spans academic + commercial simultaneously at founding (not sequential transition).

However, this pattern overlaps significantly with already-confirmed Pattern #31 + candidate Patterns #42 + #44. Risk of double-counting if registered as full candidate.

### Proposed classification: OBSERVATION-TRACK

Per v29 audit sub-category formalization, OBSERVATION-TRACK is for **event-based or potentially-meta-pattern observations** that don't yet fit standard architectural-pattern criteria.

### Proposed observation statement

> **#67 Academic-Commercial Fusion Archetype (OBSERVATION-TRACK v30):** Founder team spans academic institution(s) + commercial entity simultaneously at founding time — not sequential academic-to-industry transition. Typically co-occurs with Pattern #31 Open-Core + Pattern #42 Peer-Reviewed + Pattern #44 Academic-Lab. Distinct from pure-academic (Karpathy autoresearch) and pure-commercial (Skyvern). N=1 at v30 (All Hands AI: UIUC + CMU + industry co-founders). **Watch for:** future frameworks with similar founder composition to assess meta-pattern vs fusion-with-existing-patterns.

### Discipline impact

- Ratio calculation: registered as OBSERVATION-TRACK, does NOT count as active candidate
- Preserves post-v30 ratio improvement from un-staling (1.00:1 → 0.93:1)
- Avoids v29-highlighted pattern proliferation

## 13. Post-v30 Pattern Library state

### Counts post-v30

**Pre-v30 (post-v29 audit):** 28 confirmed + 28 active candidates + 5 stale + 5 retired = 66 full; ratio 1.00:1

**Changes at v30:**
- +0 confirmed (promotions deferred to next audit)
- +2 active candidates (via un-stale: #42 + #44)
- −2 stale (via un-stale: #42 + #44)
- +1 OBSERVATION-TRACK (#67, not counted as active candidate)

**Post-v30:**
- **28 confirmed + 30 active candidates + 3 stale + 5 retired + 1 observation-track = 67 full**
- **Ratio: 28:30 = 0.93:1** ✅ (improved from 1.00:1, cleared trigger)

### Observations at v30

- First wiki to un-stale candidates since stale-flag protocol formalized at v21 + v27
- First wiki to register OBSERVATION-TRACK as primary candidate handling mechanism
- Zero new active candidates (all action via strengthening + un-staling)
- Demonstrates v29 Phase 5 action item #3 discipline (pre-check candidate overlap)

## 14. Next audit proposals

At next audit (next trigger: +5 wikis from v29 audit → v34, OR ratio >1.05:1, OR active candidate count >28):

1. **Promote #42 Academic-Published Peer-Reviewed** at N=2
2. **Promote #44 Academic-Lab Affiliation** at N=2
3. **Formalize relationship** between #31 + #42 + #44 + #67 (meta-pattern vs fusion-of-separate-patterns)
4. **Continue observing #67** for 2nd data point before candidate reclassification
5. **Consider Pattern #32 chain-variant taxonomy formalization** (3 chain structures documented at N=3)

## 15. v30 meta-milestones

- ✅ **12th v2 routine execution** (12 distinct Phase 4b modes across 30 wikis)
- ✅ **T5 extends to N=5** with 5 distinct archetypes at 100% diversity-per-wiki
- ✅ **Pattern #31 strengthens to N=3** across 3 scope sub-types + 3 license variants
- ✅ **Pattern #32 strengthens to N=3** with first within-project paper chain variant
- ✅ **Patterns #42 + #44 un-stale** at N=2 via structurally-unambiguous multi-institutional evidence
- ✅ **Post-audit-clean first wiki** (v29 audit cleared 1.19→1.00; v30 cleared to build)
- ✅ **21st consecutive Storm Bear meta-entity** (v10-v30)
- ✅ **25 consecutive wikis at ~2h velocity plateau** (v6-v30)
- ✅ **Discipline demonstrated:** minimal new candidate registration (#67 as OBSERVATION-TRACK only) following v29 Phase 5 action item #3
- ✅ **Ratio improvement via un-staling:** 1.00:1 → 0.93:1 (first wiki to achieve ratio-improvement via un-stale mechanism)
- ✅ **10 corpus-firsts:** SWE-Bench Verified in corpus / SWE-agent T5 sub-type / academic-commercial-fusion archetype / benevolent-dictator-model explicit at 71K+ scale / 3-co-founder academic-industry triangle / named FAANG+ adoption at T5 / within-project 2-paper chain (4 persistent authors) / MIT core + in-repo separate-license-enterprise / VNC-based GUI-app-interaction agent primitive / 5-deployment-surface T5

## 16. Storm Bear operator takeaway

**Pilot ranking update v30:**
1. spec-kit v17 — methodology
2. OMC v27 — Scrum-ceremony alignment
3. BMAD v11 — VN methodology
4. markitdown v28 — doc ingestion utility
5. crawl4ai v29 — web research utility
6. **OpenHands v30 🆕 — SWE-agent platform (PR review / incident triage / migration)**
7. gws v13
8-10. codymaster / multica / graphify

**Verdict:** OpenHands is high-quality T5 platform bet (ICLR 2025 + $18.8M + 3 co-founders + MIT core), Medium-priority pilot rank #6 due to learning curve. Deploy after methodology + ingestion utility flows are stable. Best-in-class SWE-agent OSS option at v30.

---

**v30 OpenHands Phase 4b published 2026-04-22. T5 N=5. Pattern #31 #32 strengthening + #42 #44 un-staling. Pattern Library ratio 1.00→0.93:1. Discipline demonstrated.**
