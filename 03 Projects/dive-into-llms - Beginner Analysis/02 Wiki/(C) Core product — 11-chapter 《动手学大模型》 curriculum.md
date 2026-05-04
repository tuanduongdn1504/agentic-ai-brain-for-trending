# (C) Core product — 11-chapter 《动手学大模型》 curriculum

> **Entity:** Primary curriculum product + 33 content primitives + 4 topic clusters + academic-course-lineage
> **Tier:** T3 Agent-as-education (3rd entrant)
> **Parent:** `[[(C) index]]`

---

## 1. Identity

**Product name:** 《动手学大模型》系列编程实践教程 — "Dive into LLMs Hands-on Coding Practice Tutorial Series"

**English transliteration:** "Dive into LLMs" (per repo slug `dive-into-llms`; echoing Aston Zhang's "Dive into Deep Learning" 《动手学深度学习》 title pattern — intentional naming heritage)

**Repository:** https://github.com/Lordog/dive-into-llms

**Status badge:** `Status-building` (ongoing curriculum; version v0.1.0)

## 2. Product positioning

### 2.1 Verbatim mission

> 《动手学大模型》系列编程实践教程，由上海交通大学《自然语言处理前沿技术》（NIS8021）、《人工智能安全技术》课程（NIS3353）讲义拓展而来，旨在提供大模型相关的入门编程参考。本教程属公益性质、完全免费。通过简单实践，帮助同学们快速入门大模型，更好地开展课程设计或学术研究。

**Translation:** "The 《Dive into LLMs》 hands-on coding tutorial series, expanded from SJTU's NIS8021 'NLP Frontier Technology' and NIS3353 'AI Security Technology' course handouts, aims to provide introductory programming reference for large language models. This tutorial is public-welfare and completely free. Through simple practice, it helps students quickly get started with LLMs and better pursue course design or academic research."

### 2.2 Target audience

- **Primary:** SJTU students taking NIS8021 / NIS3353 courses
- **Secondary:** Chinese-speaking graduate students + researchers + developers interested in hands-on LLM practice
- **Extended:** Global CN-reading audience (GitHub-accessible + no paywall)

**Audience-scope distinct from prior T3 entrants:**
- Microsoft v6 targeted beginner developers for Azure ecosystem adoption
- HF v26 targeted developers wanting to build agents with HF / LangGraph / LlamaIndex
- **SJTU v39 targets students + researchers for academic-entry-point** (course-assignment-compatible rigor, not framework-adoption)

## 3. Product architecture — 33 primitives

### 3.1 Per-chapter tripartite

Each of 11 chapters has **exactly 3 deliverables**:

1. **`README.md` (tutorial walkthrough)** — 1.5 KB (ch4, minimal) to 16.5 KB (ch11, maximal); narrative + code snippets + install steps + troubleshooting
2. **`<topic>.pdf` (lecture slides)** — 2.0 MB (ch11) to 10.9 MB (ch1); academic-style slides matching classroom delivery
3. **`<topic>.ipynb` (Jupyter notebook)** — 8.2 KB (ch3) to 73.7 KB (ch4); executable end-to-end code

**Consistency:** All 11 chapters follow this structure. No chapter deviates. Consistency is corpus-first T3 — Microsoft v6 = notebook+markdown-hybrid; HF v26 = MDX+Colab-link hybrid; neither as uniform.

### 3.2 PDF-slides-per-chapter as first-class

**PDF sizes and content heuristics:**

| Ch | PDF | Size | Likely content |
|----|-----|------|----------------|
| 1 | dive-into-llm.pdf | 10.9 MB | Broadest-scope intro (transformers overview + fine-tuning landscape) |
| 2 | dive-into-prompting.pdf | 8.4 MB | Prompting + CoT + reasoning landscape |
| 3 | dive_edit_0410.pdf | 3.2 MB | Knowledge editing methods |
| 4 | math.pdf | 4.1 MB | Math reasoning + distillation pipeline |
| 5 | watermark.pdf | unknown | Watermark method landscape |
| 6 | dive-Jailbreak.pdf | unknown | Jailbreak taxonomy |
| 7 | stega.pdf | unknown | Steganography theory + application |
| 8 | mllms.pdf | unknown | Multimodal LLM architectures |
| 9 | GUIagent.pdf | 6.4 MB | GUI agent research landscape |
| 10 | dive-into-safety.pdf | 7.7 MB | Agent safety frameworks |
| 11 | RLHF.pdf | 2.0 MB | PPO + RLHF canonical pipeline |

**PDF sizes suggest** pedagogical investment: intro chapters + agent-space chapters (1, 9, 10) have largest PDFs; security chapters (3, 11) are compact.

**First-class status:** PDF link appears FIRST in every TOC row (before README + notebook). Pedagogy assumes slides-first then hands-on.

### 3.3 Jupyter notebook sizes

Notebook complexity range: 8.2 KB (ch3 knowledge editing, smallest) → 73.7 KB (ch4 math reasoning, 9× larger).

**Chapter 4 (math reasoning) is disproportionately large** — 73.7 KB notebook reflects DeepSeek-R1 distillation pipeline complexity + DeepMath-103K dataset processing + SFT training loop + evaluation.

**Chapter 11 (RLHF) 2nd largest** — 33.4 KB reflects PPO implementation via TRL library + GPT-2 + BERT reward model + IMDB sentiment pipeline end-to-end.

## 4. 4 topic clusters

### 4.1 Cluster A: Foundations (chapters 1-2)

| Ch | Topic | Key tech |
|----|-------|----------|
| 1 | Fine-tuning + deployment | HuggingFace Transformers + Gradio Spaces + BERT classification |
| 2 | Prompting + CoT | Multi-provider API (Qwen DashScope + Zhipu + Baidu + OpenAI) + zero/few-shot + CoT |

**Pedagogical role:** Entry-points; readers can start here with minimal prerequisites.

### 4.2 Cluster B: Security-alignment (chapters 3, 5, 6, 10, 11)

| Ch | Topic | Key tech |
|----|-------|----------|
| 3 | Knowledge editing | Model-editing methods |
| 5 | Text watermarking | Embedding-level signal hiding |
| 6 | Jailbreak attacks | Offensive security for safety research |
| 10 | Agent safety | Agent risk perception |
| 11 | RLHF alignment | PPO via TRL + GPT-2 + BERT reward |

**Observation:** **5 of 11 chapters = security-alignment cluster** — dominant cluster. Mirrors NIS3353 "AI Security Technology" source course.

### 4.3 Cluster C: Advanced architectures (chapters 4, 7, 8)

| Ch | Topic | Key tech |
|----|-------|----------|
| 4 | Math reasoning | DeepSeek-R1 distillation → Qwen2.5-Math-1.5B SFT |
| 7 | LLM steganography | Covert information encoding in LLM outputs |
| 8 | Multimodal models | Visual + text reasoning + generation |

### 4.4 Cluster D: Agents (chapters 9-10)

| Ch | Topic | Key tech |
|----|-------|----------|
| 9 | GUI Agent | Qwen2-VL-7B + LLaMa-Factory + OS-Kairos adaptive HCI agent |
| 10 | Agent safety | Agent risk perception (paired with ch9) |

**Newest cluster** — added in 2025/06 expansion batch. Reflects agent-era frontier.

## 5. Cross-corpus citation (chapter 9 → LLaMa-Factory v22)

### 5.1 Verbatim quote (chapter 9 README)

> 本教程采用LLaMa-Factory对Qwen2-VL-7B进行有监督微调，因此先从[[Code](https://github.com/hiyouga/LLaMA-Factory/)]下载源码。

**Translation:** "This tutorial uses LLaMa-Factory to do supervised fine-tuning of Qwen2-VL-7B, so first download the source from [[Code]]."

### 5.2 Citation chain

1. **SJTU chapter 9** (curriculum T3) — uses LLaMa-Factory as fine-tuning backend
2. **LLaMa-Factory (hiyouga, Lab4AI)** (v22 Storm Bear wiki, outside-scope training-infra; ACL 2024)
3. **OS-Kairos** dataset (https://github.com/Wuzheng02/OS-Kairos) — Wu Zongru authored (listed in SJTU team contributors!)

**Finding:** Wu Zongru (吴宗儒) is **both** a SJTU dive-into-llms contributor AND the OS-Kairos dataset author. Chapter 9 is effectively Wu Zongru teaching fine-tuning using his own research dataset + LLaMa-Factory as backend.

**Pattern:** Academic-research-to-curriculum-integration — researchers teach what they build. Supports Pattern #32 Research-Paper-Chain Lineage at curriculum-level (research → teaching).

### 5.3 Corpus observation

First externally-originated cross-corpus citation in corpus:
- v27 oh-my-claudecode cited v1 ECC + v2 Superpowers = **self-aware / operator-aware citation** (Yeachan knew Storm Bear corpus subjects)
- **v39 dive-into-llms cites LlaMa-Factory v22 = third-party-unaware citation** (SJTU unaware of Storm Bear; cites LLaMa-Factory as genuinely-useful upstream tool)

**Significance:** External-citation validates Storm Bear wiki-subject-selection has real upstream-dependency signal. Not registered as pattern at N=1 but tracked as observation for future registration at N=2+.

## 6. Pedagogical workflow

### 6.1 Typical chapter consumption flow

1. **Read PDF slides first** (`<topic>.pdf`) — 5-15 minutes for concept overview
2. **Read README** (`README.md`) — 10-20 minutes for tutorial walkthrough
3. **Run Jupyter notebook** (`<topic>.ipynb`) — 30-60 minutes hands-on (depending on GPU availability)
4. **进阶练习 (advanced exercises)** sections at end of some chapters — optional self-directed extensions

### 6.2 Chapter 1 example workflow (from README)

1. Understand Transformers library (cite HF docs)
2. Install env (conda + pip; mention `https://pypi.tuna.tsinghua.edu.cn/simple` as CN mirror)
3. Download TextClassification dataset (Kaggle nlp-getting-started)
4. Use custom decoupled version OR integrated `run_classification.py`
5. Train BERT on fake-news classification task
6. Deploy via HF Gradio Spaces
7. Advanced exercises (other tasks / other models) + extended reading (arXiv LLM survey)

### 6.3 Chapter 9 example workflow (from README)

1. Read slides (GUI Agent landscape)
2. Read paper (OS-Kairos arXiv 2503.16465)
3. Download OS-Kairos dataset
4. Download Qwen2-VL-7B weights
5. Download LLaMa-Factory source (cross-corpus citation)
6. Preprocess OS-Kairos → sharegpt format
7. Configure LLaMa-Factory YAML
8. Run distributed SFT (requires 3× 80GB A100)
9. Run inference via `llamafactory-cli webchat`
10. Test on mobile screenshots with scored-action output

## 7. Hardware prerequisites

Per chapter probe:

| Ch | GPU requirement | Notes |
|----|-----------------|-------|
| 1 | Modest (BERT-base fine-tuning) | Single 8-16GB GPU workable |
| 2 | API-based | No local GPU; uses cloud APIs |
| 3 | Modest | Knowledge editing on small models |
| 4 | **High (≥40GB)** | Qwen2.5-Math-1.5B + DeepSeek-R1 distillation + vLLM |
| 5-8 | Variable | Assume medium-modest |
| 9 | **Very High (3× 80GB A100)** | Qwen2-VL-7B full SFT distributed training |
| 10 | Modest-Medium | Agent safety evaluation |
| 11 | Medium | RLHF on GPT-2 |

**Implication for self-study:** Chapters 4 + 9 require cloud-rental GPU or university-cluster access. Modest-GPU learners can complete 8 of 11 chapters comfortably.

## 8. Academic-course origin details

### 8.1 NIS8021 "Natural Language Processing Frontier Technology"

- Graduate-level course at SJTU
- Taught by Zhang Zuosheng (BCMI Lab)
- Covers NLP + LLM frontier (likely aligns with chapters 1, 2, 4, 8)

### 8.2 NIS3353 "AI Security Technology"

- Undergraduate or graduate course at SJTU
- Taught by Zhang Zuosheng + Liu Gongshen (senior InfoSec faculty)
- Covers AI security (likely aligns with chapters 3, 5, 6, 7, 10, 11)

**Attribution:** Curriculum is "expanded from course handouts" — this means original course slides + notes served as starting material. Public release is extension-for-public-welfare, not raw-course-handout-dump.

## 9. Pedagogical register samples

### Chapter 6 (jailbreak)
> 想要得到更好的安全，要先从学会攻击开始。让我们了解越狱攻击如何撬开大模型的嘴！
> "To achieve better safety, start by learning to attack. Let's understand how jailbreak attacks pry open the mouth of large models!"

### Chapter 7 (steganography)
> "看不见的墨水"！想让大模型在流畅回答的同时，悄悄携带只有"自己人"能识别的信息吗？大模型隐写告诉你！
> "'Invisible ink'! Want LLMs to fluently answer while secretly carrying information only 'insiders' can recognize? LLM steganography tells you!"

### Chapter 11 (RLHF)
> 基于PPO的RLHF实验指南：本教程"十分危险"，阅读后请检查你的大模型是否在冷笑。
> "PPO-based RLHF experiment guide: This tutorial is 'very dangerous.' After reading, please check if your LLM is sneering."

**Register characteristics:**
- Playful-serious blend
- Metaphorical (pry mouth / invisible ink / sneering)
- Question-hook openings
- Warning-with-humor (ch11 "dangerous" caveat)
- First-person-plural pedagogy

## 10. Cross-references

- **Entity 2:** Secondary curriculum + Huawei Ascend partnership (dual-curriculum architecture)
- **Entity 3:** SJTU BCMI + multi-institutional consortium + Pattern #44 N=4 (team + institution)
- **Entity 4:** Storm Bear Vault meta (operator relevance + self-learning viability)
- **Cluster 1:** README + 11-chapter + SJTU academic-course-origin (full content inventory)
- **v22 LlamaFactory:** chapter 9 cross-corpus citation target
- **v6 Microsoft:** T3 inaugural big-tech-corporate contrast
- **v26 HF agents-course:** T3 N=2 commercial-ecosystem-platform contrast

## 11. Patterns touched

- Pattern #27 Community-Viral Scale Path — 15th data point (CN-academic-amplified ~60-90/day)
- Pattern #44 Academic-Lab Affiliation — N=4 (multi-institutional-consortium sub-variant)
- Pattern #28 Multi-Provider AI Support — 7th observational (pedagogy-level)
- Pattern #22 AGENTS.md — 3rd T3-abstention observation
- Pattern #29 License-Category Diversity — absent-LICENSE sub-category N=2
- Pattern #12 Governance-Depth — counter-evidence observation
- Pattern #19 Intellectual Lineage — "lab-lead" variant of archetype 1 observational

## 12. Corpus-firsts enumerated from this entity

1. CN-primary T3 (34K stars)
2. Academic-course-lineage T3 sub-archetype (NIS8021+NIS3353)
3. PDF-slides-per-chapter T3 distribution (2-11 MB PDFs)
4. Absent-LICENSE T3 (2nd overall after v37 bizos)
5. Externally-originated cross-corpus citation (chapter 9 → LLaMa-Factory v22)
6. Playful-serious CN-academic pedagogical register
7. Tripartite per-chapter consistency (README + PDF + Jupyter uniform across 11)
8. SJTU institution first in corpus
