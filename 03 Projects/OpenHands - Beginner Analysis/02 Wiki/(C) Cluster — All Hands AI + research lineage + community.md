# (C) Cluster — All Hands AI + research lineage + community

> **Wiki:** v30 OpenHands
> **Cluster:** Organizational archetype + 2-paper research chain + governance + community structure
> **Source density:** High — COMMUNITY.md + ICLR 2025 paper + SDK Nov 2025 paper + openhands.dev company page
> **Status:** Cluster summary complete

---

## 1. Summary

OpenHands is structured as an **academic-commercial fusion** distinct from every prior Storm Bear corpus entry. Three named co-founders span academic and industry:

- **Xingyao Wang** — UIUC PhD candidate, SWE-bench research contributor
- **Graham Neubig** — CMU Professor (tenured faculty)
- **Robert Brennan** — software engineer

The **commercial wrapper is All Hands AI** ($18.8M funding disclosed on openhands.dev). The **academic anchor is the research-paper-chain** — two peer-reviewed papers (ICLR 2025 + arXiv Nov 2025) with 23+ co-authors across multiple institutions. The community operates under **benevolent dictator model** with High Openness + High Agency values (COMMUNITY.md).

This cluster documents why OpenHands satisfies multiple pattern-promotion criteria simultaneously: Pattern #31 Open-Core Commercial Entity (3rd data point), Pattern #32 Research-Paper-Chain Lineage (3rd data point), Pattern #42 Academic-Published Peer-Reviewed Framework (N=2 un-stale), Pattern #44 Academic-Lab Affiliation Archetype (N=2 un-stale), Pattern #17 Ecosystem-Layer Organizations (8th data point + new archetype variant).

## 2. Sources in cluster

| Source | Type | Key content |
|--------|------|-------------|
| COMMUNITY.md | Governance doc | 3 founders named + benevolent-dictator model + core values |
| arXiv 2407.16741 | ICLR 2025 peer-reviewed paper | 23+ co-authors + OpenDevin→OpenHands rebrand statement |
| arXiv 2511.03690 | Nov 2025 follow-up paper | 11 co-authors SDK paper + production focus |
| openhands.dev product+company page | Company presence | $18.8M funding + mission + enterprise positioning |
| GitHub repo | Structural data | 71.7K stars + 101 releases + 2.1K contributions + 188+ contributors (from paper) |

## 3. Organizational archetype — academic-commercial fusion

### Founder composition

| Founder | Primary affiliation | Academic credentials | Commercial role |
|---------|--------------------|--------------------|-----------------|
| **Xingyao Wang** | UIUC (PhD candidate) | SWE-bench research contributor | Co-founder + likely CTO/Research lead |
| **Graham Neubig** | CMU (Professor, tenured) | Multiple first-tier NLP publications | Co-founder + Research advisor |
| **Robert Brennan** | Software engineering industry | — | Co-founder + Engineering lead |

### Pattern #44 Academic-Lab Affiliation — N=2 validation

**Prior at v22 LlamaFactory:** Hiyouga + Lab4AI academic-lab affiliation (N=1, STALE-CANDIDATE flagged at v27 audit)

**At v30 OpenHands:** Multi-institutional (UIUC PhD candidate + CMU tenured faculty) + All Hands AI commercial wrapper

**Structural commonalities at N=2:**
- Academic PhD-level or faculty-level affiliation(s)
- Research-lab or university institutional backing
- Published paper(s) at top-tier venue (ACL 2024 for LlamaFactory / ICLR 2025 for OpenHands)
- Commercial or semi-commercial wrapper around OSS

**Structural differences (enriching pattern):**
- LlamaFactory: single academic-lab + solo maintainer + ACL 2024 (peer-reviewed)
- OpenHands: multi-institutional + 3 co-founders + ICLR 2025 (peer-reviewed) + **additional commercial entity**

**Recommendation: Pattern #44 UN-STALE + promote to CONFIRMED at next audit** under **N=2 multi-institutional criterion**. Structurally unambiguous across 2 sub-types (solo-academic-lab vs multi-institutional-fusion).

### Pattern #31 Open-Core Commercial Entity — 3rd data point strengthening

**Confirmed at v24 Skyvern (N=2):**
- v20 fish-speech: 39 AI INC + custom research-license + commercial paid tier
- v24 Skyvern: Skyvern-AI + AGPL-3.0 + Skyvern Cloud anti-bot proprietary

**v30 OpenHands satisfies all 4 criteria:**
1. ✅ **Commercial entity founded around product** — All Hands AI incorporated around OpenHands (not community-to-commercial transition)
2. ✅ **OSS core with restrictive/standard license** — MIT for core (with separate enterprise dir licensing)
3. ✅ **Proprietary commercial tier with domain-specific differentiator** — Enterprise Kubernetes + RBAC + Slack/Jira/Linear integrations + multi-user collaboration
4. ✅ **OSS as lead-gen + credibility + commercial tier as revenue** — explicit structure

**Data point count: N=3** (fish-speech v20 + Skyvern v24 + OpenHands v30).

**Sub-type diversity within Pattern #31:**
- v20 fish-speech: foundation-model sub-type (outside-scope)
- v24 Skyvern: T5 browser-agent sub-type
- **v30 OpenHands: T5 SWE-agent sub-type (NEW within Pattern #31)**

Pattern #31 now has **3 distinct sub-types + 3 license variants** (custom non-OSI / AGPL-3.0 / MIT + separate enterprise) — spans scope categories with implementation diversity.

## 4. Research lineage — 2-paper chain with 23+ authors

### Paper 1: ICLR 2025 — OpenHands Platform (arXiv 2407.16741)

**Title:** *"OpenHands: An Open Platform for AI Software Developers as Generalist Agents"* (f.k.a. OpenDevin)

**Submission date:** July 23, 2024

**Venue:** ICLR 2025 (peer-reviewed acceptance)

**Authors (23+):** Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, Graham Neubig

**Contribution:** Platform architecture + agent loop + sandboxed execution + multi-agent coordination + benchmark harness. Evaluated across software engineering + web browsing tasks.

### Paper 2: arXiv Nov 2025 — SDK Redesign (arXiv 2511.03690)

**Title:** *"The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents"*

**Submission date:** November 5, 2025

**Status:** Tech report / preprint (peer-review status pending verification)

**Authors (11):** Xingyao Wang, Simon Rosenberg, Juan Michelini, Calvin Smith, Hoang Tran, Engel Nyst, Rohit Malhotra, Xuhui Zhou, Valerie Chen, Robert Brennan, Graham Neubig

**Contribution:** SDK redesign emphasizing flexibility + security + user interaction. Production-grade features: sandboxed execution + lifecycle control + model-agnostic routing + security analysis + REST/WebSocket + multi-interface (VS Code + VNC + CLI).

### Pattern #32 Research-Paper-Chain Lineage — N=3

**Confirmed at v22 LlamaFactory (N=2):**
- v20 fish-speech: 2 arXiv preprints (2024 v1.4 + 2026 S2 tech report)
- v22 LlamaFactory: ACL 2024 peer-reviewed + multi-citation (PEFT/TRL/QLoRA/FastChat)

**v30 OpenHands:** ICLR 2025 peer-reviewed + Nov 2025 follow-up tech report + 100+ references likely (paper unverified here, implied from ICLR acceptance + 23 authors spanning institutions)

**Pattern #32 strengthens from N=2 to N=3.** 3 distinct sub-types (TTS / training-infra / SWE-agent) with consistent structural pattern: **multi-paper chain with author overlap across papers**.

### Pattern #42 Academic-Published Peer-Reviewed Framework — N=2 un-stale

**Prior at v22 LlamaFactory (N=1, flagged STALE at v27 audit):**
- ACL 2024 acceptance (top-tier NLP venue)

**At v30 OpenHands:**
- ICLR 2025 acceptance (top-tier ML venue)

**Structural commonalities:**
- Top-tier ML/NLP conference venue
- Peer-reviewed acceptance
- Multi-author collaboration spanning institutions
- Open-source framework (not pure-research demo)

**Recommendation: Pattern #42 UN-STALE + propose PROMOTE to CONFIRMED at next audit** — N=2 structurally unambiguous across 2 sub-types (training-infrastructure ACL + T5 SWE-agent ICLR).

### Pattern #19 Intellectual Lineage — research-paper-chain archetype

**Archetype 4 of 4 (confirmed at v20):** research-paper-chain (vs individual-author / methodology / community-viral)

**Corpus data points:**
- v20 fish-speech: 7 prior research citations (VITS2 / Bert-VITS2 / GPT VITS / MQTTS / GPT Fast / GPT-SoVITS / Qwen3)
- v22 LlamaFactory: 100+ research projects chain (PEFT / TRL / QLoRA / FastChat + ecosystem)
- v23 Unsloth: Triton + HuggingFace + DeepSpeed ecosystem (narrower than LlamaFactory)
- **v30 OpenHands: 2-paper chain with 23+ + 11 authors spanning UIUC + CMU + multi-institutional**

**Pattern #19 research-paper-chain archetype 4th explicit data point (6th if counting v24 Skyvern BabyAGI/AutoGPT community-viral lineage sub-archetype 3b).**

## 5. Community governance — benevolent dictator model

### Core values (COMMUNITY.md verbatim)

- **High Openness:** *"We welcome anyone and everyone into our community by default."*
- **High Agency:** *"Members are encouraged to contribute through PRs, events, feedback, or questions."*

### Governance structure

- **Benevolent dictator model** (explicit in COMMUNITY.md) — not foundation-governed, not corporate-committee
- **Transparent planning** — *"our plans, our work, our successes, and our failures are all public record"*
- **Slack primary channel** — dub.sh/openhands invite link
- **Academic + engineering + enthusiast community** — *"engineers, academics, and enthusiasts reimagining software development"*

### Corpus comparison

| Framework | Governance model |
|-----------|------------------|
| v11 BMAD | Commercial LLC + community contributions |
| v13 gws | Official corporate (Google) |
| v17 spec-kit | Official corporate (GitHub/Microsoft) + 9-article constitution |
| v22 LlamaFactory | Solo maintainer + academic-lab affiliation |
| v27 oh-my-claudecode | Solo maintainer + multi-runtime ambassador network |
| **v30 OpenHands** | **Benevolent dictator + 3 co-founders + commercial entity + academic anchors** |

**v30 novelty:** First benevolent-dictator-model explicit in corpus (gws/spec-kit have formal governance docs; BMAD is LLC; solo maintainers are implicit benevolent-dictator). OpenHands is first **formally documented BDM at scale** (71.7K stars).

## 6. Adoption + maturity signals

### Scale + growth

- **71.7K stars** in 25 months = ~2,867 stars/month sustained (Pattern #27 8th data point: corporate-academic-amplified)
- **9,030 forks** (12.6% ratio — high engagement; corpus avg ~8-10%)
- **101 releases** (active velocity; corpus max was previously v21 system-prompts-leaks 135K stars / 13 months viral)
- **2.1K contributions from 188+ contributors** (ICLR paper cite)
- **315 MB repo size** (largest T5 in corpus by 2×+ — reflects production-grade codebase)

### Enterprise adoption claim

**Named in README:** TikTok, VMware, Amazon, Netflix, Google, NVIDIA, Apple

**Structural significance:** First T5 wiki with named FAANG+ enterprise adoption. Skyvern v24 had no named enterprise users; paperclip v14 had no disclosed customers; deer-flow v9 has implicit ByteDance internal use only.

**Caveat:** Marketing claim; scale and depth of adoption unverified.

## 7. Cluster synthesis

### Academic-commercial fusion as corpus-first archetype

OpenHands occupies a structural position no prior Storm Bear wiki has:

| Dimension | Pure academic (Karpathy autoresearch) | Pure commercial (Skyvern) | **OpenHands fusion** |
|-----------|---------------------------------------|--------------------------|---------------------|
| Founder pool | Solo academic | Pure industry (founders@skyvern.com) | **3 co-founders: 1 PhD candidate + 1 tenured faculty + 1 industry** |
| Funding | None disclosed (Karpathy personal) | VC implied (not disclosed specifically) | **$18.8M disclosed** |
| Research venue | Blog post | None | **ICLR 2025 + arXiv Nov 2025** |
| Author count | 1 (Karpathy) | Unnamed ("founders@") | **23+ paper co-authors** |
| OSS license | MIT | AGPL-3.0 | **MIT + separate enterprise** |
| Scale | 74K stars | 21K stars | **71.7K stars** |

**The fusion unlocks:**
- **Academic credibility** (ICLR acceptance + multi-institutional authors) without ivory-tower isolation
- **Commercial scalability** (All Hands AI entity + enterprise tier + $18.8M funding) without VC-captured positioning
- **Community leverage** (188+ contributors + benevolent dictator) without foundation-governance overhead

### Pattern implications consolidated

| Pattern | Pre-v30 status | v30 action | Post-v30 status |
|---------|---------------|-----------|----------------|
| #17 Ecosystem-Layer Orgs | Confirmed (v15, 7 data points) | 8th data point (commercial-startup with academic-fusion variant) | Confirmed, 8 data points |
| #19 Intellectual Lineage | Confirmed (v20, 4 archetypes) | Research-paper-chain archetype 4th data point | Confirmed, strengthened |
| #27 Community-Viral Scale | Confirmed (v21, 7 data points at v29) | 8th data point (corporate-academic-amplified sub-path) | Confirmed, 8 data points |
| #28 Multi-Provider AI Support | Confirmed (v25, 5 data points at v29) | 6th data point (native-SDK-routing variant) | Confirmed, 6 data points |
| #31 Open-Core Commercial Entity | Confirmed (v24, N=2) | N=3 (OpenHands satisfies all 4 criteria + SWE-agent sub-type) | **Confirmed, N=3** |
| #32 Research-Paper-Chain Lineage | Confirmed (v22, N=2) | N=3 (ICLR 2025 + Nov 2025 SDK paper) | **Confirmed, N=3** |
| #42 Academic-Published Peer-Reviewed | STALE-CANDIDATE (v27 flagged) | N=2 un-stale (ICLR 2025 = 2nd peer-reviewed venue) | **Un-stale, promotion proposed** |
| #44 Academic-Lab Affiliation | STALE-CANDIDATE (v27 flagged) | N=2 un-stale (UIUC + CMU multi-institutional) | **Un-stale, promotion proposed** |

**New candidates proposed at v30 (discipline: minimal):**

- **#67 Academic-Commercial Fusion Archetype** — observation-track initially; may overlap with promoted #31 + #42 + #44

**v30 contribution summary:** OpenHands is a **pattern-strengthening wiki** more than a pattern-discovering wiki. Its value in the corpus is validating existing candidates (#42, #44) and strengthening confirmed patterns (#31, #32) through structural unambiguity at N=2+.
