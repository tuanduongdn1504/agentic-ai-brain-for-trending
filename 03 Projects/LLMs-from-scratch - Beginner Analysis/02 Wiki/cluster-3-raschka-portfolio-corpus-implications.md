# Cluster 3 — Raschka Portfolio + Corpus Implications + Sister Repos

> Source ingestion 3/3 for v74 wiki build. Verbatim quotes where possible per "NEVER fabricate" discipline.

## Raschka multi-book-portfolio (Pattern #19 sub-mechanism 19e candidate)

### 6 pinned repos at solo-academic-author scale

| # | Repository | Stars | Description (verbatim from GitHub pinned section) |
|---|------------|-------|---------------------------------------------------|
| 1 | **LLMs-from-scratch** (THIS subject v74) | **95.1K** | "Implement a ChatGPT-like LLM in PyTorch from scratch" |
| 2 | **reasoning-from-scratch** | 4.4K | "Implement a reasoning LLM in PyTorch from scratch" |
| 3 | **machine-learning-book** | 5.2K | Code for *Machine Learning with PyTorch and Scikit-Learn* (Packt 2022) |
| 4 | **deeplearning-models** | 17.5K | "A collection of various deep learning architectures" |
| 5 | **llm-architecture-gallery** | 1.2K | (architecture-reference catalog) |
| 6 | **mini-coding-agent** | 859 | "Minimal and readable coding agent harness" |

**Combined pinned-stars:** 95.1K + 4.4K + 5.2K + 17.5K + 1.2K + 0.9K ≈ **124.3K** across 6 pinned book-companion + tutorial repos

**Total Raschka public repos:** 149 (per GitHub profile probe)

### Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio" formal candidate

| Property | Value | Distinguishing |
|----------|-------|----------------|
| **Primary artifact type** | Books (multi-publisher: Manning + Packt) | vs 19a tool-products / vs 19b corporate-strategic / vs 19c community-collective / vs 19d corporate-observation-as-marketing |
| **Author identity** | Solo academic-author-educator (PhD + Research Engineer) | vs 19a solo-engineer / vs 19b corporate-org / vs 19c community-led |
| **Distribution model** | git clone + Manning/Packt ZIP (no package-manager) | vs 19a npm/cargo/Homebrew |
| **Revenue model** | Book sales + paid video course + free repo | vs 19a free-OSS-with-commercial-shield / vs 19b corporate-strategic-platform |
| **Time horizon** | Multi-year per book (Raschka's portfolio spans 2015→2024+) | vs viral-velocity-MVP-portfolio |
| **Methodology alignment** | All books share "from scratch" pedagogical methodology | mechanism-distinct from prior 19 sub-mechanisms |

**N=1 PROVISIONAL within Pattern #19 (CONFIRMED at v66 audit).** v75 stale-check + v80 retire-check.

**Forward observation:** v75+ corpus may identify second educator-multi-book-portfolio (e.g., Chip Huyen / Aurélien Géron / Lewis Tunstall / etc.) → N=2 promotion-eligible.

## Sister-repo: `rasbt/reasoning-from-scratch`

The sequel book's companion repo (`rasbt/reasoning-from-scratch`, 4.4K stars). Per README of THIS subject:

> *"Build A Reasoning Model (From Scratch), while a standalone book, can be considered as a sequel to Build A Large Language Model (From Scratch)."*

**Implications:**
1. Raschka explicitly extends multi-book-portfolio: LLMs-from-scratch (2024) → reasoning-from-scratch (in-progress)
2. Sequel book = SECOND data point for sub-mechanism 19e (Raschka-specific)
3. Reasoning-from-scratch repo is likely shaped by SAME conventions:
   - Apache-modified license with book-content-carve-out (probable; needs verification at v75+ if reasoning-from-scratch ever wiki'd)
   - Chapter-folder-mirrors-book-TOC structure
   - Print-book-locked-main + extensible-bonus split

**v75+ sister-wiki candidate:** `rasbt/reasoning-from-scratch` is N=2 confirming case for v74's NEW sub-typology 45d + NEW T3 sub-archetype "Educational-Book-Companion" + sub-mechanism 19e. If/when it reaches v75+-eligible-scale, it would provide structural N=2 evidence for all 3 v74 candidates.

## Sister-repo: `rasbt/machine-learning-book`

Companion to "Machine Learning with PyTorch and Scikit-Learn" (Packt 2022; 5.2K stars).

**Implications:**
1. Raschka's book-companion-repo discipline pre-dates LLMs-from-scratch (2024) — established pattern from 2022 Packt book
2. **Cross-publisher portfolio:** Packt + Manning + future = multi-publisher book-companion-repo discipline at solo-academic-author scale
3. License model likely Apache-2.0 base (needs verification for whether it has same book-content-carve-out as LLMs-from-scratch)

## Sister-repo: `rasbt/deeplearning-models`

17.5K stars. "A collection of various deep learning architectures." NOT a book companion — distinct archetype.

**Implications:**
1. Raschka's portfolio is NOT exclusively book-companion — includes reference-catalog repos
2. `deeplearning-models` = T3 educational-architecture-reference (not book-companion)
3. Raschka's multi-archetype portfolio: book-companion (3 repos: LLMs-from-scratch + reasoning-from-scratch + machine-learning-book) + reference-catalog (deeplearning-models + llm-architecture-gallery) + agent-tool (mini-coding-agent)

**Pattern #19 sub-mechanism 19e formal definition refinement:** Sub-mechanism 19e is "educator-multi-book-portfolio" — the BOOK-companion subset of Raschka's portfolio (3 of 6 pinned). The reference-catalog + agent-tool repos are sister contributions but mechanism-distinct.

## Sister-repo: `rasbt/mini-coding-agent`

859 stars. "Minimal and readable coding agent harness."

**Implications:**
1. Raschka is engaging with coding-agent harness design (cross-domain from pure pedagogy)
2. Potential corpus-citation candidate for future agentic-harness corpus subjects
3. Aligns with v71 agents-best-practices (DenisSergeevitch) corpus-already-noted agentic-harness governance interest

**Cross-corpus implication:** Pattern #57 Cross-Wiki-Citation candidate at v75+ if any future corpus subject cites Raschka's mini-coding-agent as influence or sister.

## Pattern Library implications summary

### Phase 4b PRIMARY contribution

**NEW Pattern #45 sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" registration proposal-document:**

- **Mechanism:** LICENSE.txt redefines Apache-2.0 "Source form" to explicitly exclude books + related images + book-documentation-source. Code is Apache-2.0; book copyright preserved separately.
- **Verbatim license clause (LICENSE.txt lines 26-30):** *""Source" form shall mean the preferred form for making modifications, explicitly excluding any books specific to this software and any related images, and includes but is not limited to software source code, documentation source (excluding books and images related to this software), and configuration files."*
- **Structural distinction from prior 45 sub-typologies:**
  - 45a Unsloth (Apache + commercial-shield via tier)
  - 45b AutoGPT (MIT + PolyForm-Shield wrapping)
  - 45c CloakBrowser (MIT-wrapper + proprietary-binary artifact-scope split)
  - **45d LLMs-from-scratch (Apache-modified intra-license carve-out)** ← NEW
- **Promotion criteria evaluation:**
  - ✅ Criterion 1 (sub-typology proposal at N=1 with HIGH structural distinction): PASS — corpus-first intra-Apache modification
  - ✅ Criterion 3 (mechanism-distinct from prior sub-typologies): PASS — single-license-file-with-carve-out vs prior dual-file/tier-based approaches
  - ✅ Criterion 4 (sub-typology-within-pattern threshold): PASS — Pattern #45 CONFIRMED at v60 audit, sub-typology threshold satisfied
- **Confidence verdict:** HIGH
- **v75 stale-check + v80 retire-check.** Formal sub-variant promotion at N=2 emergence.
- **SECOND formal sub-typology proposal-document in corpus history** after v69's 45c.

### Phase 4b SECONDARY contributions

**1. NEW T3 sub-archetype "Educational-Book-Companion" registration:**
- Mechanism: Book is primary artifact + code is companion + chapter-folder-mirrors-book-TOC + print-book-constraint-shapes-repository-architecture
- Distinct from prior T3 sub-archetypes: course-tutorial v6 / educational-skill-collection v55 / single-skill-derivative v63
- N=1 PROVISIONAL; v75 stale-check
- Forward N=2 candidate: rasbt/machine-learning-book + future reasoning-from-scratch wiki

**2. NEW Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio" candidate:**
- Mechanism: solo academic-author-educator + multi-book Manning/Packt + companion-repo per book + book-as-primary-artifact
- Distinct from sub-mechanisms 19a/b/c/d (tool-portfolio / corporate / community / observation)
- N=1 PROVISIONAL; v75 stale-check
- Forward N=2 candidate: other educator-multi-book authors

**3. NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)":**
- Mechanism: medium-velocity sustained over multi-year time horizon (1,000+ days)
- Distinct from v72-audit sub-classes EXTREME-VIRAL (>300/d × ≥30d) + HIGH-NOT-EXTREME (150-300/d × ≥30d)
- N=1 PROVISIONAL at v74
- Sister case to v72-audit's HIGH-NOT-EXTREME but at lower velocity + longer sustenance horizon

### Within-pattern strengthenings (no state changes)

**1. Pattern #78 Living-Domain-Standards N+1 strengthening:**
- Mechanism: book-content-stability + bonus-folder-LDS-evolution dual-layer
- Tracks LLM frontier via bonus folders: Llama/Qwen/Gemma model architectures + MoE + Attention variants + KV cache + DPO + LoRA
- Distinct LDS-tracking mechanism vs prior 78a (multi-vendor synthesis) + 78b (vendor-internals-archive)
- Sub-mechanism candidate: "Book-Companion-LDS-via-Bonus-Folders"

**2. Pattern #66 Supply-Chain Awareness within-pattern observation:**
- 3-OS CI test matrix (Linux + Windows + macOS) at book-companion-repo scale
- `uv` modern Python tooling + `uv-pip` Windows fallback
- Sister observation to Pattern #66 prior sub-mechanisms

**3. Pattern #19 N+1 strengthening (top-level):**
- Pattern #19 ecosystem-portfolio-builder N+1 at Raschka portfolio (6 pinned repos + 149 total)
- Currently sub-archetype 19a founder-personal-tool-portfolio at N=5 → v74 contributes NEW sub-mechanism 19e candidate

## Observational candidates registered at v74

### OC-R "Affiliate-Link-As-Repository-Homepage" (NEW v74)
- GitHub `homepage` field = `https://amzn.to/4fqvn0D` (Amazon affiliate link to book)
- Corpus-first homepage-as-affiliate-link
- N=1 OBSERVATIONAL
- v77 stale-check + v80 retire-check

### OC-S "Methodology-Influence-Node-Without-Operational-Tool" (N=2 at registration)
- v63 Andrej Karpathy (corpus-foundation-individual) + v74 Sebastian Raschka (corpus-second-foundation-individual)
- Phase 0.9 (c) STRONG PASS valid without (b) PASS — pure methodology-influence-node mechanism
- N=2 EARLY-promotion-eligible at v75+ audit
- v75+ stale-check + v80 retire-check

### OC-T "Print-Book-Constraint-As-Architecture" (NEW v74)
- Repository structure shaped by print-publishing constraints rather than software-architecture constraints
- 5 manifestations: (1) main-chapter print-pinned-content-locked + (2) bonus-folders contribution-accepting + (3) LDS evolution constrained to bonus + (4) license carve-out for print content + (5) distribution via git-clone + publisher-ZIP
- Corpus-first observation
- N=1 OBSERVATIONAL
- v77 stale-check + v80 retire-check

## Pattern #57 Cross-Wiki-Citation assessment

**README + repository content cite:**
- ✅ Manning (publisher; not a corpus subject)
- ✅ Amazon (affiliate redirect; not a corpus subject)
- ✅ PyTorch (foundational framework; not a corpus subject)
- ✅ Ollama (used in ch07/03_model-evaluation + ch07/04_preference-tuning-with-dpo; NOT a corpus subject — verified against v1-v73 entries)
- ✅ Llama / Qwen / Gemma (model architecture families; not corpus subjects)
- ❌ NO direct corpus-subject URL citation identified

**Verdict:** Pattern #57 (d) Phase 0.9 criterion = **FAIL**. Subject does not anchor to corpus subjects in its primary surface.

**Notable counter-example to Pattern #57:** v74 is a STRONG (c) methodology-influence-node subject WITHOUT (d) corpus-citation. This is precisely the OC-S "Methodology-Influence-Node-Without-Operational-Tool" pattern observation — pure methodology-influence can ground Phase 0.9 (c) without requiring (d) corpus-anchoring or (b) operational-tool-deployability.

## Pilot candidacy assessment

**Phase 0.9 (b) FAIL — LLMs-from-scratch is NOT a vault pilot candidate.**

Reasoning:
- Educational reference for LEARNING LLM internals
- Storm Bear's vault USES LLMs (Claude Code substrate) as black-box product
- Building LLMs from scratch is academic-pedagogical knowledge, not vault-operational tool
- No installable artifact (git clone + Jupyter notebooks; pedagogical-only)
- No pilot deployment surface

**Pilot-ranking update at v74:** Unchanged from post-v73 — cc-switch remains #1 + codegraph #2 + agents-best-practices skill #3 + agentmemory #4 + DeepSeek-TUI #5. v74 LLMs-from-scratch is **NOT-PILOT** — added to corpus as methodology-influence-node + Phase 4b proposal-document subject, not as pilot candidate.

**Forward implication:** Future v75+ may identify operational LLM-building toolkits (e.g., HuggingFace transformers tutorials) that would be both methodology-influence AND vault-operational. v74 establishes the **methodology-only** pattern as distinct corpus archetype.

## Cross-pattern coupled-design observation

v74 exhibits NEW corpus coupling:
- Pattern #45 sub-typology 45d (Apache-modified for book-content) × Pattern #19 sub-mechanism 19e (educator-multi-book-portfolio) × NEW T3 sub-archetype (Educational-Book-Companion) × Pattern #52 NEW sub-class (LONG-SUSTAINED-MEDIUM-velocity)

**4-pattern coupled-design** at single wiki subject. Sister to v60 (4-pattern), v65 (5+-pattern corpus-record), v73 (multiple sub-mechanism candidates).

Library-vocabulary item #9 Cross-Pattern Coupled-Design strengthening: v74 is N+1 4-pattern correlation observation.

**Distinguishing v74 coupling:** All 4 patterns are TIED to the educational-book-companion archetype constraint — license shaped by print-content + portfolio shaped by multi-book authorship + tier shaped by book-as-primary-artifact + velocity shaped by multi-year-book-sustenance. **Tight cross-pattern correlation around single archetype constraint** = NEW cross-pattern coupling sub-mechanism candidate.

## Source-ingestion verification

All quotes in this cluster verified against:
- GitHub repository surface (WebFetch of github.com/rasbt/LLMs-from-scratch)
- GitHub API (`api.github.com/repos/rasbt/LLMs-from-scratch`)
- raw.githubusercontent.com README + LICENSE.txt + CITATION.cff
- GitHub profile probe (github.com/rasbt)

No book content extracted (book is print-published copyright Manning; not within wiki scope).
No bonus-folder code probed (only folder structure + descriptions per README).

Verified 2026-05-19 build session.
