# Cluster 1 — README, Book Metadata + Apache-Modified License

> Source ingestion 1/3 for v74 wiki build. Verbatim quotes where possible per "NEVER fabricate" discipline.

## Subject identity (verbatim from GitHub repository surface)

- **Repository:** `rasbt/LLMs-from-scratch`
- **Tagline:** *"Implement a ChatGPT-like LLM in PyTorch from scratch, step by step"*
- **Homepage URL field:** `https://amzn.to/4fqvn0D` (Amazon affiliate redirect to Manning book on Amazon — **corpus-first GitHub-homepage-as-affiliate-link**)
- **Created:** 2023-07-23T18:15:57Z → 2026-05-19 = **1,032 days**
- **Stars / forks / watchers (subscribers) / open issues:** 95,135 / 14,569 / 786 / 4
- **Commits:** 1,051 total
- **Primary language ratio:** Jupyter Notebook 74.7% + Python 25.3%
- **GitHub topics:** `ai`, `artificial-intelligence`, `chatbot`, `chatgpt`, `deep-learning`, `from-scratch`, `generative-ai`, `gpt`, `language-model`, `large-language-models`, `llm`, `machine-learning`, `neural-networks`, `python`, `pytorch`, `transformers`
- **License field:** "NOASSERTION" (GitHub fails to auto-classify; actual license is Apache-2.0 modified with carve-out clauses — see § License axis below)

## Book metadata (from CITATION.cff verbatim)

```yaml
cff-version: 1.2.0
message: "If you use this book or its accompanying code, please cite it as follows."
title: "Build A Large Language Model (From Scratch), Published by Manning, ISBN 978-1633437166"
abstract: "This book provides a comprehensive, step-by-step guide to implementing a ChatGPT-like large language model from scratch in PyTorch."
date-released: 2024-09-12
authors:
  - family-names: "Raschka"
    given-names: "Sebastian"
license: "Apache-2.0"
url: "https://www.manning.com/books/build-a-large-language-model-from-scratch"
repository-code: "https://github.com/rasbt/LLMs-from-scratch"
```

**Notable:** CITATION.cff declares `license: "Apache-2.0"` but the actual LICENSE.txt is **Apache-2.0 MODIFIED** with carve-out clauses (see below). CITATION.cff's "Apache-2.0" assertion is incorrect at the structural level — the modification is material enough that "NOASSERTION" from GitHub is the more accurate classification.

## README opener (verbatim)

> *"This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code repository for the book [Build a Large Language Model (From Scratch)](https://amzn.to/4fqvn0D)."*

> *"In [Build a Large Language Model (From Scratch)](http://mng.bz/orYv), you'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. In this book, I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples."*

> *"The method described in this book for training and developing your own small-but-functional model for educational purposes mirrors the approach used in creating large-scale foundational models such as those behind ChatGPT. In addition, this book includes code for loading the weights of larger pretrained models for finetuning."*

## Book primary-artifact framing (verbatim)

The README's links list places book + Manning + Amazon **before** the GitHub source code link:

> *"- Link to the official [source code repository](https://github.com/rasbt/LLMs-from-scratch)*
> *- [Link to the book at Manning (the publisher's website)](http://mng.bz/orYv)*
> *- [Link to the book page on Amazon.com](https://www.amazon.com/gp/product/1633437167)*
> *- ISBN 9781633437166"*

The book cover image is displayed prominently above this list. **Implication:** Book = primary artifact; repository = companion code. This is structurally distinct from corpus tool subjects where the repository IS the artifact.

## Apache-2.0 MODIFIED — verbatim carve-out clause

> **LICENSE.txt lines 26-30 verbatim:**
>
> *""Source" form shall mean the preferred form for making modifications, **explicitly excluding any books specific to this software and any related images**, and includes but is not limited to software source code, documentation source (**excluding books and images related to this software**), and configuration files."*

**Mechanism:** Apache-2.0 license redefines "Source form" to EXCLUDE:
1. Books specific to this software (i.e., the Manning book "Build a Large Language Model From Scratch")
2. Related images (book cover + chapter diagrams + figures)
3. Documentation source for those books and images

**Effect:** The code is Apache-2.0 licensed. The BOOK and BOOK IMAGES are NOT covered by the Apache-2.0 license — they remain under Manning's copyright. This protects Manning's publication rights while keeping the implementation code open-source.

**Comparison to Pattern #45 prior sub-typologies:**

| Sub-typology | Mechanism | Subjects |
|--------------|-----------|----------|
| **45a Apache + commercial shield** | Tier-based: free-tier code Apache + commercial-tier non-Apache | Unsloth v23 |
| **45b MIT + PolyForm-Shield** | PolyForm-Noncommercial wraps MIT codebase for non-commercial users | AutoGPT v59 |
| **45c MIT-wrapper + Proprietary-Binary** | Artifact-scope split: wrapper MIT + binary proprietary with Acceptable Use | CloakBrowser v69 |
| **45d Apache-modified (NEW v74 candidate)** | INTRA-Apache carve-out: code Apache-2.0 but books + images explicitly excluded | LLMs-from-scratch v74 |

**Structural distinction of 45d:**
- **Single license file** (not dual-file split like 45c)
- **Carve-out by content-type** (not by artifact-scope or commercial-tier)
- **Print-publishing copyright preservation** (specific to book-companion-repo archetype)
- **Apache-2.0 BASE preserved** (modified only at "Source form" definition)

This is **CORPUS-FIRST** book-content-carve-out within an Apache-2.0 license. v74 Phase 4b PRIMARY proposal-document registers 45d as new sub-typology.

## Repository acquisition methods (verbatim)

> *"To download a copy of this repository, click on the [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) button or execute the following command in your terminal:"*
>
> *"```bash"*
> *"git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git"*
> *"```"*

> *"(If you downloaded the code bundle from the Manning website, please consider visiting the official code repository on GitHub at [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) for the latest updates.)"*

**Notable:** No npm, no Homebrew, no Cargo, no Docker as primary distribution. This is **corpus-rare** distribution model: `git clone` + Manning ZIP only. Reinforces book-companion archetype (vs tool subjects which ship via package managers).

## Contributing policy (verbatim)

> *"Please note that since this repository contains the code corresponding to a print book, I currently cannot accept contributions that would extend the contents of the main chapter code."*

**Notable:** **CORPUS-FIRST print-book-locked-content contributing policy** — main chapter code is print-pinned to the book's printed pages and CANNOT accept extensions. Bonus material (separately structured) CAN accept contributions. This is a meta-pattern observation: print-publishing constraints shape code repository contribution-acceptance policy.

Counter-evidence to Pattern #80 Tool-Level Adversarial Review (CANDIDATE) — Raschka's repo is NOT structured for adversarial review or PR-based contribution flow; it's structured for solo-author print-publication preservation.

## Repository age + sustenance signals

| Metric | Value | Corpus context |
|--------|-------|---------------|
| **Age at wiki build** | **1,032 days (~2.83 years / ~34 months)** | LONGEST-DURATION at significant rate in v60+ corpus window |
| **Average stars/day** | **~92.2/day** | LONG-SUSTAINED-MEDIUM (below v72-audit HIGH-NOT-EXTREME 150-300/d threshold) |
| **Sustenance ratio** | 3.4× longer than v73 cc-switch (289d) | corpus-leading multi-year sustenance |
| **Fork ratio** | **15.3%** (14,569 / 95,135) | corpus-second after v65 17.8% — top-tier active-deployment intent |
| **Open issues ratio** | 0.00004 | extraordinarily low for 95K-star repo — pedagogical content stable |

**Velocity classification:** **NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)"** — distinct from existing v72-audit-registered sub-classes:
- EXTREME-VIRAL (>300/d × ≥30d) — v63 karpathy 1,186/d / v68 zero 1,050/d / v62 codex-plugin-cc 847/d
- HIGH-NOT-EXTREME (150-300/d × ≥30d) — v69 CloakBrowser 172.7/d × 86d / v72 DeepSeek-TUI 267.6/d × 120d / v73 cc-switch 259.6/d × 289d
- **LONG-SUSTAINED-MEDIUM (60-150/d × 1000+d) ← NEW v74 candidate** — v74 LLMs-from-scratch 92.2/d × 1032d

**Cross-archetype:** Educational-book-companion (solo academic-author-educator) — distinct mechanism from corpus prior multi-year-sustenance subjects.

## Author identity (Sebastian Raschka)

- **GitHub:** `rasbt` — 38,000 followers / following 41 / 149 public repos
- **Self-described role:** "AI Research Engineer working on LLMs"
- **Website:** sebastianraschka.com
- **Blog:** "Ahead of AI" magazine.sebastianraschka.com
- **Social:** Twitter @rasbt, YouTube @SebastianRaschka, LinkedIn in/sebastianraschka
- **Organization affiliations:** conda-forge, psa-lab, iPRoBe-lab, Raschka-research-group, BioPandas
- **GitHub achievements:** Pull Shark ×4, Galaxy Brain ×4, Public Sponsor, Mars 2020 Contributor, Arctic Code Vault Contributor

**Pinned repos (6) — multi-book-portfolio shape:**

| # | Repo | Stars | Description |
|---|------|-------|-------------|
| 1 | **LLMs-from-scratch** | **95.1K** | "Implement a ChatGPT-like LLM in PyTorch from scratch" (THIS subject) |
| 2 | **reasoning-from-scratch** | 4.4K | "Implement a reasoning LLM in PyTorch from scratch" (SEQUEL book) |
| 3 | **machine-learning-book** | 5.2K | Code for *Machine Learning with PyTorch and Scikit-Learn* (Packt 2022) |
| 4 | **deeplearning-models** | 17.5K | "A collection of various deep learning architectures" |
| 5 | **llm-architecture-gallery** | 1.2K | (LLM-architecture-reference) |
| 6 | **mini-coding-agent** | 859 | "Minimal and readable coding agent harness" |

**Total pinned star count:** 95.1K + 4.4K + 5.2K + 17.5K + 1.2K + 0.9K ≈ **124.3K stars** across 6 pinned book-companion + tutorial repos at solo academic-author-educator scale.

**Pattern #19 sub-mechanism candidate 19e "educator-multi-book-portfolio":**
- Distinct from sub-mechanism 19a founder-personal-tool-portfolio (Raschka's portfolio is BOOKS not tools)
- Distinct from sub-mechanism 19b corporate-strategic (Raschka is solo academic-author)
- Distinct from sub-mechanism 19c community-collective (Raschka is solo single-author)
- Distinct from sub-mechanism 19d corporate-observation-as-marketing (Raschka is publishing-business not corporate-observation)
- **N=1 PROVISIONAL** within Pattern #19 (CONFIRMED at v66 audit)
- v75 stale-check + v80 retire-check

## Methodology-influence-node positioning (Storm Bear Phase 0.9 (c) STRONG PASS rationale)

**Sebastian Raschka is a recognized ML methodology-influence-node:**

1. **Academic credentialing:** PhD in Statistics (Michigan State); former Assistant Professor at UW-Madison; current AI Research Engineer
2. **Multi-book Manning + Packt authorship:**
   - "Python Machine Learning" (2015, Packt) + 3rd edition (2019)
   - "Machine Learning with PyTorch and Scikit-Learn" (2022, Packt)
   - "Build a Large Language Model (From Scratch)" (2024, Manning) — THIS subject's companion
   - "Build a Reasoning Model (From Scratch)" (sequel; in-progress)
3. **Educational reach:**
   - 38K GitHub followers + extensive Twitter/X presence
   - "Ahead of AI" blog (Substack-style magazine.sebastianraschka.com)
   - YouTube channel @SebastianRaschka
   - Manning video course 17h15m companion to THIS book
4. **Open-source influence:** mlxtend library + multiple research-tool repos at Raschka-research-group org
5. **Foundational pedagogical positioning:** "Build LLMs from scratch" is a foundational pedagogical category alongside Karpathy's nanoGPT lineage — both teach LLM internals via educational implementation

**Corpus comparison:** Raschka = **corpus-second-foundation-individual** at v74 (after v63 Karpathy = corpus-foundation-individual). Both Phase 0.9 (c) STRONG PASS based on methodology-influence-node status without operational-tool requirement.

**OC-S candidate "Methodology-Influence-Node-Without-Operational-Tool":**
- N=1: v63 Andrej Karpathy (skill-derivative at karpathy-skills v63; Karpathy himself = corpus-foundation)
- **N=2: v74 Sebastian Raschka (LLMs-from-scratch + reasoning-from-scratch + multi-book portfolio = corpus-second-foundation-individual)**
- N=2 EARLY-promotion-eligible at v75+ audit
- Mechanism: Phase 0.9 (c) STRONG PASS valid without (b) PASS — pure methodology-influence without vault-operational-deployability

## Notable observational candidates registered

### OC-R "Affiliate-Link-As-Repository-Homepage" (NEW v74)

GitHub `homepage` field = `https://amzn.to/4fqvn0D` (Amazon affiliate redirect URL).

**Corpus-typical homepage:** project website (e.g., codegraph.dev / sebastianraschka.com) or product page (e.g., manning.com/books/...).

**v74 corpus-first:** Amazon affiliate link as homepage URL = monetization-via-book-purchase-redirect.

N=1 OBSERVATIONAL. v77 stale-check + v80 retire-check.

### OC-S "Methodology-Influence-Node-Without-Operational-Tool" (N=2 with v63 Karpathy sister)

See § Methodology-influence-node positioning above. Pre-eligible for v75+ audit.

## Source-ingestion note: print-book-as-primary-source-of-truth

**The repository itself states (verbatim):**
> *"this repository contains the code corresponding to a print book"*

The print book (Manning 2024) is the **primary source of truth**. Repository updates can extend bonus materials but cannot extend main chapter code (book-pinned). This shapes:
1. Contribution policy (PRs accepted only for bonus folders)
2. Source ingestion approach (book content unavailable to wiki; only README + LICENSE + CITATION + bonus-folder structure + chapter notebook structure available)
3. Knowledge-base scope (wiki documents the REPOSITORY structure + book-companion archetype, NOT the book content)

Per "NEVER fabricate" discipline, the wiki:
- ✅ Documents repository structure, license terms, README content, bonus materials, author identity
- ❌ Does NOT attempt to summarize book content beyond what README quotes verbatim
- ❌ Does NOT claim methodology-correctness or technical-accuracy of book content (operator has not read the book; cannot verify)
