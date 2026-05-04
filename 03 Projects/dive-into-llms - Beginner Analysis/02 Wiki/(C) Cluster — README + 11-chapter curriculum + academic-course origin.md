# (C) Cluster — README + 11-chapter curriculum + academic-course origin

> **Cluster:** User-facing README + 11-chapter curriculum structure + SJTU academic-course lineage
> **Parent:** `[[(C) index]]`
> **Sources:** Top-level README.md (111 lines) + per-chapter READMEs (11 files, 1.5-16.5 KB each) + project motivation section
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **Top-level README structure + project motivation + updates log**
2. **11-chapter curriculum taxonomy + per-chapter tripartite (README + PDF + Jupyter)**
3. **SJTU academic-course origin story (NIS8021 + NIS3353)**

## 2. README structure (111 lines)

| Section | Purpose |
|---------|---------|
| Badges | version v0.1.0 / Status-building / PRs-Welcome / stars / forks / issues |
| Navigation | 3 anchors: 项目动机 / 教程目录 / 贡献者列表 |
| 💡 Updates | 2025/06/06 entry announcing Huawei Ascend partnership + 4 new topics |
| 🎯 项目动机 (Project motivation) | SJTU course-handout origin + public-welfare (公益) framing |
| 📚 教程目录 (Curriculum TOC) | 11-row table: topic / blurb / [课件] [教程] [脚本] links |
| 🔥 Secondary curriculum | 《大模型开发全流程》 announcement + Huawei Ascend link |
| 🙏 免责声明 (Disclaimer) | Liability-limitation; implicit open-use-grant |
| 🤝 欢迎贡献 (Contributions welcome) | PR + issue open invitation |
| ❤️ 贡献者列表 (Contributor list) | 2 teams with named affiliations |
| 🌟 Star History | star-history.com chart embed |

**Corpus-first observations:**

- **Public-welfare (公益) framing** corpus-first — frames the project as Chinese-academic civic-good tradition rather than open-source ideology. Distinct from MIT/Apache-2.0 "permissive" framing.
- **Badge stack** conservative (5 badges; vs. corpus maximum ~15 in agency-agents v18). No CI / coverage / download-count badges — academic materials, not production software.
- **Dual-curriculum announcement in main README** — primary curriculum links to secondary-curriculum partner-platform. First corpus T3 with dual-surface distribution.
- **No demo / interactive widget / leaderboard** — pure educational-materials framing. Contrasts HF v26 Unit 4 leaderboard certification and Microsoft v6 lesson-demo embeds.

## 3. 11-chapter curriculum taxonomy

### 3.1 Per-chapter structure (33 primitives total)

Each chapter has **3 deliverables**:
1. `README.md` — tutorial walkthrough + code snippets + notes
2. `<topic>.pdf` — lecture slides (2-11 MB)
3. `<topic>.ipynb` — executable Jupyter notebook

**Total: 11 × 3 = 33 primary content primitives**, plus `assets/` folders (screenshots, diagrams) and chapter 11's `requirements.txt`.

### 3.2 Full 11-chapter inventory

| # | 中文 | Translation | Core tech | Notebook size |
|---|------|-------------|-----------|---------------|
| 1 | 微调与部署 | Fine-tuning + deployment | Transformers + Gradio Spaces + BERT | 11.7 KB |
| 2 | 提示学习与思维链 | Prompting + Chain-of-Thought | Qwen DashScope / Zhipu GLM / Baidu Wenxin / OpenAI | 17.2 KB |
| 3 | 知识编辑 | Knowledge editing | Model-editing methods (ROME, MEMIT-style) | 8.2 KB |
| 4 | 数学推理 | Math reasoning | DeepSeek-R1 distillation + SFT on DeepMath-103K → Qwen2.5-Math-1.5B | **73.7 KB** (largest) |
| 5 | 模型水印 | Watermarking | Text watermark embedding | 17.2 KB |
| 6 | 越狱攻击 | Jailbreak attacks | Security offense for safety research | 17.2 KB |
| 7 | 大模型隐写 | LLM steganography | Hidden-message encoding in LLM output | 17.2 KB |
| 8 | 多模态模型 | Multimodal models | MLLM reasoning + generation | 17.2 KB |
| 9 | GUI智能体 | GUI Agent | Qwen2-VL-7B + LLaMa-Factory + OS-Kairos dataset | 12.1 KB |
| 10 | 智能体安全 | Agent safety | Agent risk perception + safety testing | 12.6 KB |
| 11 | RLHF安全对齐 | RLHF alignment | PPO via TRL + GPT-2 + IMDB sentiment | **33.4 KB** |

### 3.3 4 topic clusters (derived)

| Cluster | Chapters | Pedagogical role |
|---------|----------|------------------|
| **Foundations** | 1-2 | Fine-tuning + Prompting as entry point |
| **Security-alignment** | 3, 5, 6, 10, 11 | Knowledge editing / watermark / jailbreak / agent safety / RLHF (largest cluster; reflects NIS3353 "AI Security Technology" course origin) |
| **Advanced-architectures** | 4, 7, 8 | Math reasoning / steganography / multimodal |
| **Agents** | 9, 10 | GUI Agent + Agent safety (newer topics added 2025/06) |

**Observation:** Security-alignment cluster is dominant (5 of 11 chapters). Mirrors academic origin — NIS3353 "AI Security Technology" is 1 of 2 source courses.

## 4. SJTU academic-course origin

### 4.1 Verbatim from README

> 《动手学大模型》系列编程实践教程，由上海交通大学《自然语言处理前沿技术》（NIS8021）、《人工智能安全技术》课程（NIS3353）讲义拓展而来（教师：张倬胜），旨在提供大模型相关的入门编程参考。本教程属公益性质、完全免费。

**Translation:** "The 《Dive into LLMs》 series hands-on-coding tutorial is expanded from SJTU's NIS8021 (Natural Language Processing Frontier Technology) and NIS3353 (AI Security Technology) course handouts (instructor: Zhang Zuosheng). This tutorial is public-welfare and completely free."

### 4.2 Academic-course lineage

**2 SJTU courses as origin:**
- **NIS8021 自然语言处理前沿技术** — NLP frontier technology (graduate-level)
- **NIS3353 人工智能安全技术** — AI Security Technology (undergraduate/graduate)

**Origin archetype: academic-course-lecture-notes → public tutorial**

This is a **corpus-first archetype** distinct from:
- **Big-tech-corporate T3** (Microsoft v6): Microsoft Developer Relations writes curriculum from scratch for strategic ecosystem-adoption
- **Commercial-ecosystem-platform T3** (HF v26): Hugging Face assembles named-instructor team to teach own platform + BYO frameworks

**SJTU archetype:** existing course handouts (already vetted by academic peer-review of SJTU curriculum committee) open-sourced as public-welfare extension.

### 4.3 Public-welfare (公益) positioning

Verbatim: "本教程属公益性质、完全免费" — "This tutorial is public-welfare, completely free."

**公益 (gōngyì) = public welfare / public good** — Chinese socio-cultural category for non-commercial civic contribution. Distinct from:
- Western "open source" (ideology: freedom + community-governed)
- Western "free as in beer" (no-cost but unclear rights)
- "Academic open materials" (MIT OCW style — institutionally-sponsored)

Public-welfare framing aligns with **absent-LICENSE decision** (see cluster 3): within Chinese academic-open tradition, explicit license may feel less culturally necessary because public-welfare framing implies liberal-use-with-attribution informally.

## 5. 2025/06/06 update expansion

Verbatim update log entries:
1. ✅ 上线国产化《大模型开发全流程》公益教程（含PPT、实验手册和视频），此处特别感谢华为昇腾社区的支持！
2. ✅ 在原系列编程实践教程的基础上进行内容更新，并增加了新的主题（数学推理、GUI Agent、大模型对齐、隐写术等）！

**Translation:**
1. Launched 《Full LLM Development Process》 national-ecosystem public-welfare tutorial (PPT + experiment manual + video), special thanks to Huawei Ascend community
2. Updated content of original programming-practice tutorial + added new topics (math reasoning / GUI Agent / LLM alignment / steganography)

**Evolution signals:**
- **国产化 (guóchǎnhuà) = "nationalization / domestic-substitution"** — frames Huawei Ascend curriculum as national-hardware-ecosystem alternative to NVIDIA-CUDA-dominated training
- **Timing:** June 2025 = peak DeepSeek-R1 viral moment (reasoning models). Chapter 4 (math reasoning) directly uses DeepSeek-R1 distillation; chapter timing aligns with ecosystem moment
- **New topics (4):** math reasoning / GUI Agent / alignment / steganography — all frontier topics of 2024-2025 LLM research

## 6. Cross-corpus citation (CORPUS-FIRST externally-originated)

**Discovery:** Chapter 9 GUI Agent tutorial (`documents/chapter9/README.md`) verbatim cites LLaMa-Factory:

> 本教程采用LLaMa-Factory对Qwen2-VL-7B进行有监督微调，因此先从[[Code](https://github.com/hiyouga/LLaMA-Factory/)]下载源码。

**Translation:** "This tutorial uses LLaMa-Factory to do supervised fine-tuning of Qwen2-VL-7B, so first download the source from [[Code]]."

**Corpus observation:** SJTU v39 externally cites hiyouga/LLaMA-Factory which is the subject of **v22 Storm Bear wiki** (outside-scope training-infrastructure; ACL 2024 peer-reviewed; first academic-lab affiliation in corpus).

**Type:** This is a **corpus-first EXTERNALLY-ORIGINATED cross-corpus citation** — distinct from v27 oh-my-claudecode citing v1 ECC + v2 Superpowers (SELF-citation within corpus / operator-aware). SJTU ≠ Storm Bear-aware; SJTU cites LLaMa-Factory because it's a useful ML tool; the corpus-alignment is serendipitous but validates that Storm Bear wiki subjects are genuinely useful upstream dependencies.

**Significance:**
- Confirms Storm Bear wiki subject selection has external validity (LLaMa-Factory is independently upstream-cited in SJTU curriculum)
- Establishes **2nd cross-corpus citation modality**: self-citation (v27) vs external-citation (v39); could justify new pattern candidate at higher N but currently N=1 external → documented as observation

## 7. Pedagogical register

Sample voice from chapter 6 blurb verbatim:
> 想要得到更好的安全，要先从学会攻击开始。让我们了解越狱攻击如何撬开大模型的嘴！

**Translation:** "To achieve better safety, start by learning to attack. Let's understand how jailbreak attacks pry open the mouth of large models!"

**Register characteristics:**
- **First-person-plural** (让我们 = "let's") — invitational pedagogy
- **Playful metaphors** (撬开...嘴 = "pry open ...mouth") — Chinese academic informal-serious blend
- **Question-hook openings** ("想...吗？" = "do you want to...?") — student-engagement
- **Security-ethics framing** — jailbreak-then-defend dual framing (chapters 6 + 10)

Contrast Microsoft v6 register (corporate-professional, neutral-tone, focus on Azure integration) and HF v26 register (instructional-casual, framework-agnostic, Unit-based progression).

## 8. Navigation to other clusters

- **Cluster 2:** Secondary curriculum + Huawei Ascend partnership (external-platform dual-curriculum)
- **Cluster 3:** Multi-institutional contributors + academic-lab governance (team structure + light-governance counter-evidence)

## 9. Patterns touched

- **Pattern #22 AGENTS.md T3-abstention** — dive-into-llms has NO AGENTS.md. 3rd T3-abstention observation.
- **Pattern #28 Multi-Provider AI Support pedagogical-level** — chapter 2 lists Qwen / Zhipu / Baidu Wenxin / Baichuan / OpenAI = pedagogy-level multi-provider awareness (7th observational data point).
- **Pattern #27 Community-Viral Scale Path** — 34K stars sustained ~60-90/day = CN-academic-amplified sub-path (15th data point).
- **Pattern #44 Academic-Lab Affiliation** — SJTU BCMI is 4th academic-lab; multi-institutional-consortium sub-variant observation.
- **Pattern #29 License-Category Diversity** — absent-LICENSE sub-category N=2 (bizos v37 + dive-into-llms v39).

## 10. Corpus-first signals from this cluster

1. CN-primary T3 (first at this tier)
2. Academic-course-lineage T3 sub-archetype (NIS8021 + NIS3353 → public tutorial)
3. PDF-slides-per-chapter T3 distribution (2-11 MB PDFs as first-class)
4. 公益 (public-welfare) positioning framing (first in corpus)
5. 国产化 (national-ecosystem-substitution) framing via Huawei Ascend (first in corpus)
6. Externally-originated cross-corpus citation (chapter 9 → LLaMa-Factory v22)
7. 2-course-handout academic origin (first in corpus at T3)
