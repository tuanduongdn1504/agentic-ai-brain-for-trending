# (C) Secondary curriculum (《大模型开发全流程》) + Huawei Ascend corporate-community partnership

> **Entity:** Dual-curriculum T3 secondary surface + national-hardware-ecosystem partnership + corporate-community educational co-development
> **Tier context:** T3 secondary distribution surface
> **Parent:** `[[(C) index]]`

---

## 1. Identity

**Product name:** 《大模型开发全流程》 — "Full LLM Development Process"

**English:** No official English name (no EN translation exists at time of observation)

**Launch:** 2025/06/06 (announced in dive-into-llms README update log)

**Hosting:** Huawei Ascend community portal — **https://www.hiascend.com/edu/growth/lm-development**

**Positioning per README:** 《大模型开发学习专区》 (literally "Large Model Development Learning Zone") at 昇腾社区 (Ascend community)

## 2. Product positioning (verbatim)

> 在《动手学大模型》原系列教程的基础上，我们联合华为开发了《大模型开发全流程》系列课程。本系列教程基于昇腾基础软硬件开发，覆盖PPT、实验手册、视频等教程形式。该教程分为初级、中级、高级系列，面向不同的大模型实践需求，旨在将前沿技术通过代码实践的方式，为相关研究者、开发者由浅入深地提供快速上手、应用昇腾已支持模型和全新模型迁移调优的全流程开发指南。

**Translation:** "Based on the original 《Dive into LLMs》 tutorial series, we collaborated with Huawei to develop the 《Full LLM Development Process》 course series. This series is built on Ascend foundational software + hardware, covering PPT, experiment manuals, videos, and other tutorial formats. The tutorial is divided into **initial / intermediate / advanced** tiers, targeting different LLM practice needs. Its goal is to transform frontier technology into code practice, providing researchers and developers with a full-process development guide — from shallow to deep — for quick onboarding, using Ascend-supported models, and migrating/tuning new models."

## 3. Dual-curriculum T3 architecture (corpus-first)

| Dimension | Primary 《动手学大模型》 (this repo) | Secondary 《大模型开发全流程》 (Ascend) |
|-----------|-------------------------------------|---------------------------------------|
| Hosting | GitHub (`Lordog/dive-into-llms`) | Huawei Ascend community (hiascend.com) |
| Accessibility | Global (GitHub-accessible + no paywall) | Requires Ascend-community-registration (likely free) |
| License signal | Absent-LICENSE | Platform ToS-governed |
| Hardware target | **NVIDIA A100/A800** (CUDA) | **Huawei Ascend NPU** (国产化) |
| Depth architecture | 11 chapters (topic-scoped) | 3-tier progression (初级/中级/高级) |
| Formats | README + PDF + Jupyter | **PPT + experiment manual + video + other** |
| Partnership | Pure academic (SJTU + NUS) | **Corporate-community** (+ Huawei Ascend) |
| Contributors | 11 | 19 (14 SJTU + 5 Huawei) |
| Maintenance | Active (73 commits, pushed 2026-04-15) | Unknown (external platform) |
| Cross-reference | Links TO secondary | Unknown reverse-link status |

**Corpus-first dual-curriculum T3 architecture** — no prior T3 entrant had 2 parallel hosted surfaces.

## 4. Huawei Ascend organizational positioning

### 4.1 Huawei Ascend (华为昇腾) identity

**华为昇腾** = Huawei's AI-accelerator hardware + software ecosystem division.

**Scope:**
- **Hardware:** Ascend NPUs (910B, 910C series)
- **Software stack:** MindSpore framework (Huawei's TensorFlow/PyTorch alternative) + CANN (Compute Architecture for Neural Networks; Huawei's CUDA alternative) + ModelZoo (pre-trained models)
- **Community:** hiascend.com — developer education + documentation + tutorials

**Strategic context:**
- Post-2022 US chip-export-restrictions on NVIDIA H100/A100 to CN catalyzed Ascend as NVIDIA-alternative for CN AI infrastructure
- National-level CN investment in Ascend for AI-infrastructure self-sufficiency
- Academic-partnership strategy to grow Ascend developer pool

### 4.2 Named Huawei Ascend contributors (from team 2 roster)

| Name | Likely role |
|------|-------------|
| **ZOMI** | AI educator (popular Bilibili creator); possibly ecosystem-growth lead |
| 谢乾 (Xie Qian) | Community team |
| 程黎明 (Cheng Liming) | Community team |
| 楼梨华 (Lou Lihua) | Community team |
| 焦泽昱 (Jiao Zeyu) | Community team |

**ZOMI note:** Independent AI-education creator on Bilibili (~1M+ follower scale in CN AI-education niche); likely Huawei community-ambassador or freelance partner (not full-time Huawei employee).

## 5. Partnership archetype (NEW corpus observation, N=1)

### 5.1 What it's NOT

- NOT open-core commercial-entity (Huawei ≠ open-sourcing the curriculum for commercial upsell; curriculum is public-welfare)
- NOT ecosystem-layer-individual (Huawei = corporation, not individual)
- NOT commercial-funnel companion (Huawei not monetizing tutorial users directly)
- NOT big-tech-curator (Huawei doesn't curate this; SJTU authors it)

### 5.2 What it IS

**National-hardware-vendor co-authoring educational content** as ecosystem-growth strategy:
- Huawei provides: hardware access + CANN/MindSpore expertise + hosting platform + 5 contributors
- SJTU provides: academic credibility + course-pedagogy expertise + 14 contributors + content ownership

**Mutual value:**
- Huawei: Ascend developer pool growth + academic credibility signal
- SJTU: Extended curriculum reach + hardware-sponsor partnership (possible research resources bonus)

### 5.3 Pattern #17 Ecosystem-Layer variant observation

**Pattern #17 (CONFIRMED v15, 5 variants at v29 audit + variant 5a at v38):**
- Variant 1: individual-led-dev (nextlevelbuilder)
- Variant 2: big-tech-curator (Anthropic / Vercel)
- Variant 3: commercial-startup-ecosystem (VoltAgent)
- Variant 4: solo-brand (safishamsi / penpax.ai)
- Variant 5: ecosystem-scale commercial platform (HuggingFace + Microsoft)
- Variant 5a: academic-lab ecosystem-portfolio (HKUDS; observational N=1)

**v39 proposes variant 6 observational (N=1):**
- **National-hardware-vendor with academic-co-author** (Huawei Ascend + SJTU BCMI)

**Not registered standalone** at N=1. If N=2 emerges (e.g., Tsinghua + Cambricon, or Rice U + Intel Gaudi), could formalize.

## 6. 国产化 (Nationalization / Domestic-Substitution) framing

### 6.1 Term analysis

**国产化 (guóchǎnhuà)** literally "nation-product-ization" — Chinese policy-framing term for domestic technology substitution:
- 国 (guó) = country / nation
- 产 (chǎn) = produce / product
- 化 (huà) = -ization / transformation

**Context:** Official CN policy framing for replacing foreign-dependency technology with domestic alternatives (semiconductors, OS, cloud, AI-accelerators, databases).

### 6.2 Corpus-first in Storm Bear wikis

- Prior CN-authored wikis (TrendRadar v19, fish-speech v20, LlamaFactory v22) = CN-ecosystem-native BUT did NOT use 国产化 framing explicitly
- **dive-into-llms v39 is first explicit 国产化 framing** — announces secondary curriculum AS national-substitution product

### 6.3 Implications for non-CN consumers

- **Academic study usability:** Secondary curriculum content will assume Ascend hardware + CANN/MindSpore; readers with only NVIDIA CUDA access will find parts inapplicable
- **Primary curriculum remains CUDA-based** — no dual-hardware claim; if you don't have Ascend, use primary curriculum only
- **Cultural awareness:** Understanding 国产化 framing is pedagogical context not hostile signal; parallels how Tsinghua + Alibaba curricula may reference Aliyun specifically

## 7. Tiered curriculum architecture (3-level progression)

| Tier | 中文 | Likely content scope |
|------|------|----------------------|
| 初级 | Initial / Beginner | Environment setup on Ascend + basic fine-tuning + small-model experiments |
| 中级 | Intermediate | Medium-scale training + CUDA → Ascend migration + distributed setup + MindSpore primitives |
| 高级 | Advanced | Full model lifecycle + production deployment + optimization + new-model-porting to Ascend |

**Pedagogical model distinct from all prior T3:**
- Microsoft v6 = 10 + 4 + 4 horizontal topic expansion
- HF v26 = 4-unit + bonus (self-contained framework units)
- **SJTU primary = 11-chapter topic-scoped (near-flat)**
- **SJTU secondary = 3-tier progression-scoped (vertical depth)**

### 7.1 Why progression-tier makes sense for Ascend content

- Hardware-migration content needs graduated difficulty (install → port small model → port large model)
- Developer-onboarding-funnel benefits from initial/intermediate/advanced self-selection
- Video format (new at T3) naturally suits sequential progression

## 8. New formats at secondary surface

Per verbatim: "覆盖PPT、实验手册和视频等教程形式"

| Format | Status at T3 |
|--------|--------------|
| PPT (slides) | Common (analog to primary curriculum PDFs) |
| 实验手册 (experiment manual) | Novel at T3 (step-by-step hands-on manual separate from README) |
| **视频 (video)** | **Corpus-first at T3** — Microsoft v6 has no dedicated video; HF v26 has YouTube embeds but not structural lessons |

**Video as first-class tutorial format at T3** = corpus-first observation. Reflects CN AI-education norms (Bilibili video-first pedagogy).

## 9. 2025/06/06 update context

Timing alignment:
- **5 months post-DeepSeek-R1** (Jan 2025 viral launch) — chapter 4 math-reasoning uses DeepSeek-R1 distillation
- **Peak reasoning-model era** industrially
- **Agent-era onset** — chapters 9 + 10 GUI Agent + Agent Safety added same batch
- **CN chip-self-sufficiency peak** push — Huawei Ascend 910C launched earlier 2025

**Bundled update:**
1. Secondary curriculum launch (new product)
2. Primary curriculum expansion (4 new topics: math / GUI agent / alignment / steganography)

**Inference:** SJTU BCMI coordinated major update batch to ship 2025/06 — both Huawei partnership launch AND content expansion timed together. Not serendipitous; orchestrated.

## 10. Storm Bear operator observation

### 10.1 Hardware-ecosystem partnership template

**Value for Storm Bear:** Template for how academic-partnership + hardware-vendor can amplify educational content reach. Not directly replicable (VN lacks national-AI-chip), but structural learning:

- **Hardware-sponsor = amplification layer** (Huawei provides reach + hosting)
- **Academic-author = credibility layer** (SJTU provides peer-reviewed rigor)
- **Bilateral value exchange** (sponsor gets developer pool; author gets reach)

**VN-analog for Storm Bear:** partnership with cloud providers (VNG Cloud / FPT Cloud) or agile-training bodies (Scrum Alliance VN chapter) for potential future Storm Bear educational content.

### 10.2 Video-first pedagogy observation

CN AI-education norms heavily favor Bilibili video-first. VN education norms (YouTube + written blogs) differ slightly but video-first works in VN too (per VN tech YouTube channels like "Phạm Huy Hoàng" growing at scale).

**Storm Bear practical:** If Storm Bear ships educational content eventually, video alongside written wiki may be necessary for VN market penetration (not optional). Resource investment caveat.

## 11. Practical non-access note

- **Secondary curriculum content not directly fetched** for this wiki (external platform; may require Ascend-community login)
- **What is known from README:** 3-tier structure + PPT + experiment manual + video formats + Ascend hardware target
- **What is not known:** Exact lesson count per tier, specific code samples, Huawei Ascend hardware requirements, dependency on MindSpore vs PyTorch-on-Ascend (PyTorch-on-Ascend does exist via torch_npu)

**For future follow-up:** Operator could register at hiascend.com/edu/growth/lm-development and capture secondary curriculum structure for Storm Bear observational coverage (currently deferred — primary curriculum has enough depth for v39 wiki).

## 12. Cross-references

- **Entity 1:** Core product 11-chapter curriculum (primary surface)
- **Entity 3:** SJTU BCMI + multi-institutional consortium + Pattern #44 N=4
- **Entity 4:** Storm Bear Vault meta
- **Cluster 2:** Secondary curriculum + Huawei Ascend detail

## 13. Patterns touched

- Pattern #17 Ecosystem-Layer Organizations — 12th data point (national-hardware-vendor-as-academic-co-author observational variant)
- Pattern #44 Academic-Lab Affiliation — multi-institutional-consortium sub-variant includes corporate-community partner (Huawei)
- Pattern #27 Community-Viral Scale Path — secondary curriculum likely amplifies primary 34K-star growth
- Pattern #19 Intellectual Lineage — academic-course-lineage extended via corporate-community co-authorship (hybrid observational)

## 14. Corpus-firsts enumerated from this entity

1. Dual-curriculum T3 architecture (GitHub + partner-platform)
2. National-hardware-ecosystem-substitution framing (国产化)
3. Huawei Ascend corporate-community educational partnership
4. Tiered curriculum architecture (初级/中级/高级 progression-scoped at T3)
5. Video as first-class tutorial format at T3 (new format)
6. Experiment-manual as separate-from-README deliverable at T3
7. Academic-hardware-vendor-community tri-partite partnership structure
8. ZOMI AI educator as corporate-community representative
