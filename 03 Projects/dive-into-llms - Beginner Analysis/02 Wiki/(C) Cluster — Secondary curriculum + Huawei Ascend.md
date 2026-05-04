# (C) Cluster — Secondary curriculum (《大模型开发全流程》) + Huawei Ascend corporate-community partnership

> **Cluster:** Dual-curriculum T3 architecture + national-hardware-ecosystem-substitution partnership + 2025/06 evolution
> **Parent:** `[[(C) index]]`
> **Sources:** README section "🔥 新上线：国产化《大模型开发全流程》" + Huawei Ascend community reference (https://www.hiascend.com/edu/growth/lm-development) + contributor team 2 roster
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Secondary curriculum launch (《大模型开发全流程》) as dual-surface distribution**
2. **Huawei Ascend corporate-community educational partnership (corpus-first)**
3. **Tiered curriculum architecture (initial / intermediate / advanced)**

## 2. Secondary curriculum identity

### 2.1 Verbatim positioning

> 在《动手学大模型》原系列教程的基础上，我们联合华为开发了《大模型开发全流程》系列课程。本系列教程基于昇腾基础软硬件开发，覆盖PPT、实验手册、视频等教程形式。该教程分为初级、中级、高级系列，面向不同的大模型实践需求，旨在将前沿技术通过代码实践的方式，为相关研究者、开发者由浅入深地提供快速上手、应用昇腾已支持模型和全新模型迁移调优的全流程开发指南。

**Translation:** "Based on the original 《Dive into LLMs》 tutorial series, we collaborated with Huawei to develop the 《Full LLM Development Process》 course series. This series is built on Ascend foundational software + hardware, covering PPT, experiment manuals, videos, and other tutorial formats. The tutorial is divided into **initial / intermediate / advanced** tiers, targeting different LLM practice needs. Its goal is to transform frontier technology into code practice, providing researchers and developers with a full-process development guide — from shallow to deep — for quick onboarding, using Ascend-supported models, and migrating/tuning new models."

### 2.2 Surface characteristics

**Primary surface (this repo):** `Lordog/dive-into-llms` on GitHub — 11 chapters + Jupyter + PDF + CN-markdown

**Secondary surface (off-repo):** Huawei Ascend community at **https://www.hiascend.com/edu/growth/lm-development** (link in README as "👉《大模型开发学习专区》@ 昇腾社区 👈")

### 2.3 Dual-curriculum T3 architecture (corpus-first)

| Dimension | Primary 《动手学大模型》 | Secondary 《大模型开发全流程》 |
|-----------|------------------------|-------------------------------|
| Hosting platform | GitHub | Huawei Ascend community (hiascend.com) |
| License signal | Absent-LICENSE | Unknown (external platform) |
| Hardware target | NVIDIA A100/A800 (CUDA) | **Ascend (昇腾) NPU** |
| Content depth | 11 chapters + 33 primitives | Tiered (initial/intermediate/advanced) |
| Formats | README + PDF + Jupyter | **PPT + experiment manuals + videos** |
| Purpose | Foundational LLM techniques | Full development lifecycle (migration + tuning + deployment) |
| Partnership | None (pure academic) | Corporate-community (Huawei) |

**Corpus-first dual-curriculum T3** — no prior T3 entrant had 2 parallel surfaces with differentiated hosting/hardware/formats.

## 3. Huawei Ascend corporate-community partnership (corpus-first observation)

### 3.1 Organization identity

**Huawei Ascend (华为昇腾)** — Huawei's AI-hardware ecosystem division, established to compete with NVIDIA in the AI-accelerator market.

**Community URL:** https://www.hiascend.com/ with `edu/` subfolder dedicated to tutorials + learning paths.

**Named contributors from Huawei team (README):**
- **ZOMI** — likely ZOMI AI educator (popular CN AI-content creator on Bilibili)
- 谢乾 (Xie Qian)
- 程黎明 (Cheng Liming)
- 楼梨华 (Lou Lihua)
- 焦泽昱 (Jiao Zeyu)

### 3.2 Partnership archetype (NEW corpus observation)

**Pattern #17 Ecosystem-Layer variant observation:**

Huawei here is NOT:
- An ecosystem-layer individual (Pattern #17 variant 1: nextlevelbuilder)
- A big-tech curator (Pattern #17 variant 2: Anthropic / Vercel)
- A commercial-startup ecosystem (Pattern #17 variant 3: VoltAgent)
- An ecosystem-scale commercial platform (Pattern #17 variant 5: HuggingFace + Microsoft)

Instead: **Corporate hardware-community partner embedded as educational co-developer** — Huawei Ascend provides hardware + curriculum development resources, SJTU provides academic credibility + pedagogy. Bilateral value exchange.

**Novel variant candidate (N=1 observational):**
- **Ascend Ecosystem-Growth Strategy** — national-hardware-vendor co-authoring educational content to drive hardware adoption (compare to NVIDIA Deep Learning Institute or AMD ROCm tutorials)
- **If N=2 emerges** (e.g., another national-hardware vendor partnering with academic lab), could formalize as Pattern #17 variant 6: "national-hardware-vendor-with-academic-co-author"

### 3.3 国产化 (Nationalization / Domestic-Substitution) framing

Verbatim: "国产化《大模型开发全流程》" — "Nationalized 《Full LLM Development Process》"

**国产化 (guóchǎnhuà)** = "domestic-substitution / nationalization" — Chinese policy-framing for replacing foreign technology dependencies with domestic alternatives.

**Context:** Post-2022 US chip export restrictions on NVIDIA H100/A100 to China catalyzed Huawei Ascend growth as NVIDIA-alternative. Academic curriculum in Ascend-ecosystem aligns with national policy + industrial self-sufficiency.

**First corpus wiki with explicit nationalization framing** — prior CN-authored corpus wikis (TrendRadar v19 / fish-speech v20 / LlamaFactory v22) presented as CN-ecosystem-native but without explicit 国产化 positioning.

## 4. Tiered curriculum architecture

Per README: "该教程分为初级、中级、高级系列" — "divided into initial, intermediate, advanced tiers"

| Tier | Chinese | Likely target |
|------|---------|---------------|
| 初级 | Initial / Beginner | Environment setup + basic fine-tuning on Ascend + small-model experiments |
| 中级 | Intermediate | Medium-scale training + migration from CUDA to Ascend + distributed setup |
| 高级 | Advanced | Full model development lifecycle + production deployment + optimization |

**Pedagogical progression archetype** distinct from:
- **Microsoft v6:** 10-lesson + 4 continuing + 4 coming-soon (horizontal topic expansion)
- **HF v26:** 4-unit + bonus (unit = self-contained module with framework focus)
- **SJTU primary:** 11-chapter (topic-scoped; near-flat structure)
- **SJTU secondary:** 3-tier (progression-scoped; vertical depth)

### 4.1 Four resources per tier

Per README: "覆盖PPT、实验手册和视频等教程形式" — "covering PPT, experiment manuals, videos, and other tutorial formats"

- **PPT** — lecture slides (analogous to primary curriculum's per-chapter PDFs)
- **实验手册 (experiment manual)** — step-by-step hands-on guides
- **视频 (video)** — recorded instruction (NEW at T3 — primary curriculum has no video)
- **+ 其他 (other)** — unspecified

Video addition at secondary surface is corpus-first for T3 (Microsoft v6 + HF v26 both text-primary; HF v26 has YouTube embed but not as structural tutorial component).

## 5. 2025/06/06 update significance

### 5.1 Timing alignment with ecosystem

- **June 2025** = 5 months after DeepSeek-R1 launch (Jan 2025) + peak viral moment
- **Chapter 4 math reasoning** directly uses DeepSeek-R1 distillation → Qwen2.5-Math-1.5B
- **Chapter 9 GUI Agent** added in 2025/06 expansion batch — first agent-space chapter
- **Chapter 10 Agent Safety** — paired with ch9, also agent-space

**Inference:** SJTU BCMI Lab monitored 2024-2025 ecosystem evolution and expanded curriculum to match. Not a one-time curriculum drop; actively maintained.

### 5.2 Pedagogical rebalancing

Original (pre-2025/06) curriculum likely emphasized:
- Fine-tuning + prompting + knowledge editing + watermark + jailbreak + multimodal + RLHF (7 chapters)

2025/06 expansion added:
- Math reasoning / GUI Agent / Agent safety / Steganography (4 new topics)

**Net effect:** Curriculum evolved from **general LLM techniques** (pre-2025/06) to **LLM + agent-era + reasoning-era** (post-2025/06) — matching industry 2024-2025 frontier.

## 6. Dual-attribution implications

### 6.1 Credit allocation

**Primary curriculum (《动手学大模型》)** contributor team:
- SJTU: 10 faculty/students (Zhang Zuosheng, Yuan Tongxin = Lordog, Ma Xinbei, He Zhiwei, Du Wei, Zhao Haodong, Wu Zongru, Wu Zheng, Dong Lingzhong, Zhang Yulong)
- NUS: Fei Hao (费豪)

**Secondary curriculum (《大模型开发全流程》)** contributor team:
- SJTU: Zhang Zuosheng, Liu Gongshen, Chen Xingyu, Cheng Pengzhou, Dong Lingzhong, He Zhiwei, Ju Tianjie, Ma Xinbei, Wu Zheng, Wu Zongru, Yan Zihe, Yao Yao, Yuan Tongxin, Zhao Haodong (14 SJTU contributors — expanded from primary's 10)
- Huawei Ascend: ZOMI, Xie Qian, Cheng Liming, Lou Lihua, Jiao Zeyu (5 Huawei contributors)

**Overlap:** 8 of 10 primary contributors also in secondary (Zhang Zuosheng, Yuan Tongxin, Ma Xinbei, He Zhiwei, Wu Zongru, Wu Zheng, Dong Lingzhong, Zhao Haodong). **Core team carry-over ~80%** between primary and secondary.

### 6.2 Institutional evolution signals

- **SJTU team expansion** — 10 → 14 contributors suggests BCMI Lab investment grew between primary (original) and secondary (2025/06)
- **NUS drops out of secondary** — Fei Hao contributes only to primary; absent from Huawei-partnered secondary (possible geographic/institutional boundary)
- **Liu Gongshen (刘功申)** joins as 2nd SJTU senior — InfoSec Directory page at `infosec.sjtu.edu.cn/DirectoryDetail.aspx?id=75`; likely AI-security faculty bringing course NIS3353 expertise

## 7. Storm Bear operator observation

### 7.1 Dual-curriculum as strategic template

**Primary + Secondary pattern** offers Storm Bear a template:
- **Primary (public, open):** Vault wiki → eventual public release (compare to SJTU GitHub materials)
- **Secondary (partner platform):** Commercial / educational-partner venue (compare to Huawei Ascend)

**For VN Scrum coaching:**
- Storm Bear vault = analog to primary (self-maintained GitHub + Obsidian + free)
- Partnership option = VN university Scrum coursework OR commercial training partner (Agile VN certification body) = analog to secondary

**Caveat:** Feasibility depends on Storm Bear building reputational capital to attract institutional partner. Currently vault is pre-public.

### 7.2 Hardware-ecosystem observation

**Huawei Ascend nationalization** shows how hardware-vendor partnerships amplify academic content reach in constrained geographic-regulatory contexts. For VN (no national AI chip), analog partnerships would be with cloud providers (VNG Cloud / FPT Cloud) or hardware integrators.

**Low priority for Storm Bear operator** — VN regulatory-hardware context differs from CN; direct replication not applicable.

## 8. Patterns touched

- **Pattern #17 Ecosystem-Layer** — 12th data point (Huawei Ascend corporate-community-as-educational-partner observational variant; not registered as new variant due to N=1)
- **Pattern #31 Open-Core Commercial Entity** — N/A; Huawei is not open-core commercial entity for this educational product; rejected overlap
- **Pattern #44 Academic-Lab Affiliation** — N=4 with multi-institutional-consortium sub-variant (SJTU + NUS + Huawei academic-industry consortium)
- **Pattern #27 Community-Viral Scale Path** — secondary curriculum distribution extends reach beyond GitHub 34K; may contribute to star-growth velocity

## 9. Corpus-first signals from this cluster

1. Dual-curriculum T3 architecture (GitHub + partner-platform)
2. National-hardware-ecosystem-substitution framing (国产化)
3. Huawei Ascend corporate-community educational partnership
4. Tiered curriculum architecture (初级/中级/高级 progression-scoped)
5. Video as first-class tutorial format at T3
6. Academic-industry consortium with 80% contributor overlap between primary/secondary curricula
7. ZOMI AI educator as corporate-community representative

## 10. Navigation to other clusters

- **Cluster 1:** README + 11-chapter primary curriculum + SJTU academic-course origin
- **Cluster 3:** Multi-institutional contributors + academic-lab governance (Pattern #44 N=4)
