# Entity 1 — LLMs-from-scratch product

> **What it is:** The official GitHub code repository for Sebastian Raschka's Manning-published book *Build a Large Language Model (From Scratch)* (2024). Apache-2.0 license modified to exclude print-book content + images from "Source form" definition.

## Definitional anchor (verbatim from repository README)

> *"This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code repository for the book Build a Large Language Model (From Scratch)."*

## What LLMs-from-scratch IS

A **book-companion repository** at v74. Three-artifact stack:

1. **Print + ebook book** (Manning 2024, ISBN 978-1633437166) — **PRIMARY ARTIFACT**
2. **GitHub repository** (Apache-modified; this subject) — **COMPANION CODE**
3. **Video course** (17h15m via Manning livevideo) — **COMPANION VIDEO**

The book is the primary artifact; the repository exists to support the book's pedagogical journey.

## What LLMs-from-scratch IS NOT

- ❌ NOT a tool (no installation; no service surface; no agent integration)
- ❌ NOT a vault pilot candidate (educational reference; not operational)
- ❌ NOT a frontier LLM training framework (pedagogical small-LLM education)
- ❌ NOT a production-grade implementation (designed for laptops; reasonable timeframes)
- ❌ NOT extendable in main chapters (print-book locks ch01-ch07 main code)

## Core structural properties

| Property | Value |
|----------|-------|
| **Tier** | **T3 Education — Educational-Book-Companion** (NEW corpus-first sub-archetype) |
| **License** | **Apache-2.0 MODIFIED** with book-content-carve-out (NEW Pattern #45 sub-typology 45d candidate) |
| **Primary language** | Jupyter Notebook 74.7% + Python 25.3% |
| **Hardware** | "designed to run on conventional laptops within a reasonable timeframe" |
| **Distribution** | `git clone --depth 1` + Manning ZIP (no package manager) |
| **Contribution policy** | Main chapter code = print-pinned, contribution-LOCKED; bonus folders = contribution-OPEN |
| **i18n** | EN-only |
| **CI/CD** | 3-OS test matrix (Linux + Windows + macOS via `uv` + `uv-pip`) |

## Scale + sustenance signals

| Metric | Value |
|--------|-------|
| **Stars** | **95,135** (top-tier corpus scale) |
| **Forks** | **14,569** (fork-ratio 15.3%; corpus-second after v65 17.8%) |
| **Open issues** | 4 (extraordinary low for 95K-star repo) |
| **Watchers (subscribers)** | 786 |
| **Commits** | 1,051 |
| **Age** | **1,032 days (~2.83 years / ~34 months)** |
| **Velocity** | **92.2 stars/day SUSTAINED** = NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM (60-150/d × 1000+d)" |

## Book metadata

| Field | Value |
|-------|-------|
| **Title** | Build A Large Language Model (From Scratch) |
| **Author** | Sebastian Raschka |
| **Publisher** | Manning |
| **ISBN** | 978-1633437166 |
| **Date released** | 2024-09-12 |
| **Sequel** | Build A Reasoning Model (From Scratch) — companion at `rasbt/reasoning-from-scratch` |

## Pedagogical architecture

**7 chapters + 5 appendices** organized into 5 pedagogical stages:

1. **Foundation (Ch 1-2):** Concepts + text data + tokenization + embedding
2. **Architecture (Ch 3-4):** Attention mechanisms + full GPT model assembly
3. **Training (Ch 5):** Pretraining loop + loss + generation + GPT-2 weight loading
4. **Adaptation (Ch 6-7):** Classification finetuning + instruction-tuning + DPO bonus
5. **Reference (Appendix A-E):** PyTorch primer + references + exercises + training-loop enhancements + LoRA

Each main chapter ships 3 file types:
- `chXX.ipynb` — full chapter notebook
- `XXXX.py` — summary `.py` script (book's distilled code)
- `exercise-solutions.ipynb` — exercises + solutions

## Bonus material structure

**12+ bonus folders** at chapter-folder convention `chXX/02_bonus_*/`. Covers:
- BPE tokenizers from scratch
- Attention variants (Grouped-Query, Multi-Head Latent, Sliding Window, Gated DeltaNet, Cross-Layer KV Sharing)
- Mixture-of-Experts
- KV Cache
- FLOPs Analysis
- Llama 3.2 / Qwen3 / Gemma 3 / OLMo 3 / Tiny Aya / Qwen3.5 / Gemma 4 architecture supplements
- Memory-efficient weight loading
- Project Gutenberg pretraining
- OpenAI API + Ollama evaluation
- Direct Preference Optimization (DPO)
- Spam classifier UI + instruction-finetuned-model UI
- Parameter-efficient finetuning (LoRA)

**Mechanism:** Print-book Ch 1-7 main code is **locked** (contributions cannot extend). Bonus folders are **open** (LDS evolution tracked here without breaking book-printed pages).

## License modification — verbatim Apache-2.0 carve-out

> **LICENSE.txt lines 26-30:** *""Source" form shall mean the preferred form for making modifications, **explicitly excluding any books specific to this software and any related images**, and includes but is not limited to software source code, documentation source (**excluding books and images related to this software**), and configuration files."*

**Effect:** Apache-2.0 covers code; book content + images remain Manning's print-publication copyright.

This is **corpus-first intra-Apache modification with book-content-carve-out** = NEW Pattern #45 sub-typology 45d candidate.

## Companion artifact stack (verbatim from README)

> *"[A 17-hour and 15-minute companion video course](https://www.manning.com/livevideo/master-and-build-large-language-models) where I code through each chapter of the book."*

> *"[Build A Reasoning Model (From Scratch)](https://mng.bz/lZ5B), while a standalone book, can be considered as a sequel to Build A Large Language Model (From Scratch)."*

5-artifact-publication discipline at solo academic-author-educator scale:
1. Manning print + ebook
2. GitHub Apache-modified repository
3. Manning livevideo 17h15m paid video course
4. Free 170-page PDF "test yourself guide" (per README)
5. Sequel book + sequel repo (`rasbt/reasoning-from-scratch`)

## Why LLMs-from-scratch matters at v74 corpus

**Pattern Library contributions:**

1. **PRIMARY: NEW Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source"** — corpus-first intra-Apache modification carving print-content out of open-source coverage. SECOND formal sub-typology proposal-document in corpus history after v69's 45c.

2. **NEW T3 sub-archetype "Educational-Book-Companion"** — corpus-first in v60+ window. Mechanism: book is primary artifact + chapter-folder-mirrors-book-TOC + print-book-constraint-shapes-architecture.

3. **NEW Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio"** — solo academic-author-educator + multi-book Manning/Packt + companion-repo per book.

4. **NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)"** — corpus-first multi-year-sustained-at-significant-rate subject.

5. **Pattern #78 LDS N+1 strengthening** — book-content-stability + bonus-folder-LDS-evolution dual-layer.

6. **OC-R "Affiliate-Link-As-Repository-Homepage"** — GitHub homepage URL = Amazon affiliate redirect.

7. **OC-S "Methodology-Influence-Node-Without-Operational-Tool" N=2** — v63 Karpathy + v74 Raschka sister-evidence.

8. **OC-T "Print-Book-Constraint-As-Architecture"** — repository structure shaped by print-publishing constraints.

## Cross-references

- **Author entity:** [Entity 2 — Sebastian Raschka archetype](./entity-2-raschka-archetype.md)
- **Phase 4b PRIMARY:** [Entity 3 — Pattern #45 sub-typology 45d](./entity-3-pattern-45-sub-typology-45d.md)
- **Storm Bear meta:** [Entity 4 — WEAK INCLUDE 1/4 rationale](./entity-4-storm-bear-meta.md)
- **Strongest methodology-influence sibling:** v63 andrej-karpathy-skills
- **Pattern #45 sub-typology predecessor:** v69 CloakBrowser 45c (FIRST sub-typology proposal-document)
