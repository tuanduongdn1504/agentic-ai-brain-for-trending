# Cluster 2 — Chapter Structure + Pedagogical Architecture

> Source ingestion 2/3 for v74 wiki build. Verbatim quotes where possible per "NEVER fabricate" discipline.

## Hardware requirements (verbatim)

> *"The code in the main chapters of this book is designed to run on conventional laptops within a reasonable timeframe and does not require specialized hardware... the code automatically utilizes GPUs if they are available."*

**Notable:** Pedagogical accessibility — designed to run on consumer laptops without GPU. This is **corpus-distinct** from prior ML educational subjects which often require GPU access.

## Chapter table (verbatim from README)

| Chapter Title | Main Code (for Quick Access) | All Code + Supplementary |
|---------------|------------------------------|--------------------------|
| Setup recommendations + "How to best read this book" | — | — |
| **Ch 1: Understanding Large Language Models** | No code | — |
| **Ch 2: Working with Text Data** | `ch02.ipynb` + `dataloader.ipynb` (summary) + `exercise-solutions.ipynb` | `./ch02` |
| **Ch 3: Coding Attention Mechanisms** | `ch03.ipynb` + `multihead-attention.ipynb` (summary) + `exercise-solutions.ipynb` | `./ch03` |
| **Ch 4: Implementing a GPT Model from Scratch** | `ch04.ipynb` + `gpt.py` (summary) + `exercise-solutions.ipynb` | `./ch04` |
| **Ch 5: Pretraining on Unlabeled Data** | `ch05.ipynb` + `gpt_train.py` (summary) + `gpt_generate.py` (summary) + `exercise-solutions.ipynb` | `./ch05` |
| **Ch 6: Finetuning for Text Classification** | `ch06.ipynb` + `gpt_class_finetune.py` + `exercise-solutions.ipynb` | `./ch06` |
| **Ch 7: Finetuning to Follow Instructions** | `ch07.ipynb` + `gpt_instruction_finetuning.py` (summary) + `ollama_evaluate.py` (summary) + `exercise-solutions.ipynb` | `./ch07` |
| **Appendix A: Introduction to PyTorch** | `code-part1.ipynb` + `code-part2.ipynb` + `DDP-script.py` + `exercise-solutions.ipynb` | `./appendix-A` |
| **Appendix B: References and Further Reading** | No code | `./appendix-B` |
| **Appendix C: Exercise Solutions** | list of exercise solutions | `./appendix-C` |
| **Appendix D: Adding Bells and Whistles to the Training Loop** | `appendix-D.ipynb` | `./appendix-D` |
| **Appendix E: Parameter-efficient Finetuning with LoRA** | `appendix-E.ipynb` | `./appendix-E` |

## Pedagogical progression (chapter-by-chapter)

The 7-chapter + 5-appendix structure implements **classic LLM-building pedagogy** as a single progressive sequence:

### Stage 1: Foundation (Ch 1-2)
- **Ch 1 — Understanding LLMs:** No code. Pure conceptual introduction.
- **Ch 2 — Working with Text Data:** First code chapter. Text → token → embedding pipeline. Dataloader pattern.

### Stage 2: Architecture (Ch 3-4)
- **Ch 3 — Coding Attention Mechanisms:** Single-head → multi-head attention from scratch. Mathematical core of transformers.
- **Ch 4 — Implementing a GPT Model from Scratch:** Full GPT architecture assembly. Attention + feedforward + positional encoding + LayerNorm.

### Stage 3: Training (Ch 5)
- **Ch 5 — Pretraining on Unlabeled Data:** Training loop. Cross-entropy loss. Generation. Loading pretrained GPT-2 weights.

### Stage 4: Adaptation (Ch 6-7)
- **Ch 6 — Finetuning for Text Classification:** Discriminative finetuning (spam classifier as example). Output head modification.
- **Ch 7 — Finetuning to Follow Instructions:** Instruction-tuning workflow. Includes Ollama-based evaluation + DPO bonus material.

### Stage 5: Reference (Appendices)
- **Appendix A — PyTorch Introduction:** Just-enough-PyTorch primer for readers without prior framework experience. DDP-script.py for distributed training.
- **Appendix B — References:** Pure reference material.
- **Appendix C — Exercise Solutions:** Consolidated exercise solutions.
- **Appendix D — Bells and Whistles:** Training loop enhancements (learning rate schedulers + hyperparameter tuning patterns).
- **Appendix E — LoRA:** Parameter-efficient finetuning bonus chapter.

## Pedagogy-supports-print-book signature

**Each main chapter ships 3 file types:**
1. **`chXX.ipynb`** — main chapter notebook (mirrors book chapter content)
2. **`gpt*.py` / `dataloader*.py` / etc.** — summary `.py` scripts (book's distilled code; same content but `.py` form)
3. **`exercise-solutions.ipynb`** — exercises + solutions

**Structure implications:**
- **1:1 chapter-to-folder mapping** — `ch02/`, `ch03/`, ..., `ch07/`
- **Sub-folder convention:** `01_main-chapter-code/` for primary book code + `02_bonus_*/` + `03_bonus_*/` etc. for bonus materials
- **Bonus folders accept community contributions** (per README contributing-policy carve-out)

This is **corpus-first** chapter-folder-structure-mirrors-book-toc convention. v74 introduces this as T3 sub-archetype "Educational-Book-Companion" structural signature.

## Bonus material structure (verbatim from README)

### Setup
- Python Setup Tips → `setup/01_optional-python-setup-preferences`
- Installing Python Packages and Libraries Used in This Book → `setup/02_installing-python-libraries`
- Docker Environment Setup Guide → `setup/03_optional-docker-environment`

### Chapter 2 — Working With Text Data (4 bonus folders)
- Byte Pair Encoding (BPE) Tokenizer From Scratch → `ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb`
- Comparing Various Byte Pair Encoding (BPE) Implementations → `ch02/02_bonus_bytepair-encoder`
- Understanding the Difference Between Embedding Layers and Linear Layers → `ch02/03_bonus_embedding-vs-matmul`
- Dataloader Intuition With Simple Numbers → `ch02/04_bonus_dataloader-intuition`

### Chapter 3 — Coding Attention Mechanisms (2 bonus folders)
- Comparing Efficient Multi-Head Attention Implementations
- Understanding PyTorch Buffers

### Chapter 4 — Implementing a GPT Model from Scratch (~7 bonus folders)
- FLOPs Analysis
- KV Cache
- Attention variants: Grouped-Query, Multi-Head Latent, Sliding Window, Gated DeltaNet, Cross-Layer KV Sharing
- Mixture-of-Experts (MoE)

### Chapter 5 — Pretraining on Unlabeled Data (~12 bonus folders) — **LARGEST bonus section**
- Alternative Weight Loading Methods
- Pretraining GPT on the Project Gutenberg Dataset
- Learning rate schedulers and hyperparameter tuning
- User interface for model interaction
- **Converting GPT to Llama**
- Memory-efficient Model Weight Loading
- Extending the Tiktoken BPE Tokenizer
- PyTorch performance optimization tips
- **LLM architectures supplements:** Llama 3.2, Qwen3, Gemma 3, Olmo 3, Tiny Aya, Qwen3.5, Gemma 4
- Integration examples with alternative LLMs

### Chapter 6 — Finetuning for Text Classification (3 bonus folders)
- Additional Experiments Finetuning Different Layers
- Finetuning Different Models on the 50k IMDb Dataset
- User interface for spam classifier

### Chapter 7 — Finetuning to Follow Instructions (5 bonus folders)
- Dataset utilities for near duplicates
- **Model evaluation via OpenAI API and Ollama** → `ch07/03_model-evaluation`
- Generating a Dataset for Instruction Finetuning
- **Direct Preference Optimization (DPO) for LLM Alignment** → `ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb`
- User interface for instruction-finetuned models

### Appendix E — LoRA
- Parameter-efficient Finetuning with LoRA (already counted as appendix-E.ipynb)

## Pattern #78 Living-Domain-Standards strengthening (N+1)

**LDS evolution-tracking via bonus folders:**

| LLM domain evolution | Tracked via bonus folder | Where |
|----------------------|--------------------------|-------|
| **Llama architecture** (Llama 3.2) | "Converting GPT to Llama" | ch05 bonus |
| **Qwen architecture** (Qwen3, Qwen3.5) | LLM architectures supplements | ch05 bonus |
| **Gemma architecture** (Gemma 3, Gemma 4) | LLM architectures supplements | ch05 bonus |
| **OLMo + Tiny Aya** | LLM architectures supplements | ch05 bonus |
| **MoE** (Mixture-of-Experts) | "Mixture-of-Experts (MoE)" | ch04 bonus |
| **GQA / MHL / Sliding Window / Gated DeltaNet / Cross-Layer KV** | Attention variants | ch04 bonus |
| **DPO** (Direct Preference Optimization) | "DPO for LLM Alignment" | ch07 bonus |
| **LoRA** (Parameter-efficient Finetuning) | Appendix E | dedicated |
| **KV Cache** | "KV Cache" | ch04 bonus |
| **BPE tokenizer** | "BPE Tokenizer From Scratch" | ch02 bonus |

**Mechanism:** Book code is print-pinned (Ch 1-7 main chapters cannot be extended); LDS evolution is captured via bonus-folder updates that DON'T break book-printed pages. This is **corpus-distinct LDS tracking mechanism** — the print-book constraint creates a separation between **main canonical book content (stable)** and **evolving bonus material (LDS frontier)**.

**Distinct from prior LDS patterns:**
- v64 claude-seo 78a multi-vendor-industry-domain-standards (8 SEO deprecation events tracked)
- v65 claude-code-system-prompts 78b single-vendor-product-internals-archive (Claude Code 176 version archive)
- v71 agents-best-practices 78a triple-standard synthesis (OWASP + NIST + MCP-spec + Anthropic-suite + OpenAI-suite at single-skill scale)
- v73 cc-switch 12-layer LDS integration (Tauri 2 + Rust 1.85+ + 7 agent runtimes + 50+ providers + multiple cloud-sync APIs)
- **v74 LLMs-from-scratch — book-content-stability + bonus-folder-LDS-evolution dual-layer** (NEW LDS tracking mechanism: print-stable-main + extensible-bonus)

## Companion artifacts (verbatim from README)

> *"[A 17-hour and 15-minute companion video course](https://www.manning.com/livevideo/master-and-build-large-language-models) where I code through each chapter of the book."*

> *"[Build A Reasoning Model (From Scratch)](https://mng.bz/lZ5B), while a standalone book, can be considered as a sequel to Build A Large Language Model (From Scratch)."*

**Companion artifact stack:**
1. **Manning book** (primary; ISBN 9781633437166; print + ebook; published 2024-09-12)
2. **GitHub repository** (companion code; Apache-modified license; this subject)
3. **Manning video course** (17h15m; companion-to-chapters; paid via Manning livevideo)
4. **Free 170-page PDF** "test yourself guide" (companion-via-Manning; mentioned in README)
5. **Sequel book** "Build a Reasoning Model (From Scratch)" + companion repo `rasbt/reasoning-from-scratch` (4.4K stars)

**Distinct corpus signature:** Book-with-companion-code is corpus-first archetype at v74. Prior T3 subjects shipped EITHER course-tutorial materials OR skill-collections OR single-skills — never book-companion-repo.

## CI/CD signal (cross-platform test discipline)

README ships **3 GitHub Actions badges** at chapter table opener:
- `Code tests Linux` via `basic-tests-linux-uv.yml`
- `Code tests Windows` via `basic-tests-windows-uv-pip.yml`
- `Code tests macOS` via `basic-tests-macos-uv.yml`

**Notable:**
- 3-OS CI test matrix at book-companion repo scale
- `uv` package manager used in Linux + macOS configs (modern Python tooling)
- `uv-pip` fallback for Windows
- **Pattern #66 Supply-Chain Awareness sub-mechanism candidate:** cross-OS-CI-tests-for-book-companion-code = supply-chain hygiene applied to educational artifact. Sister observation to Pattern #66 prior sub-mechanisms.

## Discussions + Community (verbatim from README)

> *"I welcome all sorts of feedback, best shared via the Manning Forum or GitHub Discussions."*

**Channels:**
1. **Manning Forum** — primary book-reader Q&A channel (publisher-hosted)
2. **GitHub Discussions** — repository-level Q&A (currently enabled)

**Notable:** **Dual-channel community discipline** — Manning Forum for book-content + GitHub Discussions for code-questions. Corpus-first dual-discussion-channel-split for educational artifact.

## Pedagogical pattern observations

### Solo-academic-author + multi-companion-artifact discipline

Raschka's distribution model:
- Book (Manning print + ebook)
- Code (GitHub Apache-modified)
- Video course (Manning livevideo paid)
- Free PDF supplement (Manning)
- Sequel book + sequel repo

This is **5-artifact-publication discipline** at solo-academic-author scale. Sister observation to Pattern #19 sub-mechanism 19a founder-personal-tool-portfolio but mechanism-distinct (BOOK-companions not tool-products).

### Print-book-constraint-as-architecture (NEW observational candidate)

The repository structure is **shaped by print-book constraints**:
1. Chapter 1-7 main code = print-pinned, contribution-locked
2. Bonus folders = print-unaffected, contribution-accepting
3. LDS evolution = constrained to bonus folders (LLM frontier tracked via bonus, not main)
4. License has explicit print-content-carve-out (Apache modified)
5. Distribution: git clone + Manning ZIP (not package-manager)

**OC-T candidate "Print-Book-Constraint-As-Architecture"** — book-companion repo structure is FORMALLY shaped by print-publishing constraints rather than software-architecture constraints. Corpus-first observation. N=1 OBSERVATIONAL.

This is **distinct mechanism** from prior pattern shape observations — most prior subjects' architectures are shaped by tool-use-case constraints; v74 is shaped by print-publishing-business constraints.
