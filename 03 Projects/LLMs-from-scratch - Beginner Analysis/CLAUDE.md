# LLMs-from-scratch (rasbt) — Project CLAUDE.md

📍 **Status:** Active wiki build — **v74** (2026-05-19)
📍 **Routine:** `05 Skills/llm-wiki-routine-v2.2.md`
📍 **Subject:** [github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
📍 **Book:** [Build a Large Language Model (From Scratch) — Manning, 2024](https://www.manning.com/books/build-a-large-language-model-from-scratch)
📍 **Author site:** [sebastianraschka.com](https://sebastianraschka.com)
📍 **Author blog:** [magazine.sebastianraschka.com (Ahead of AI)](https://magazine.sebastianraschka.com)

---

## Phase 0 outputs (verified 2026-05-19)

### Subject identity

- **Tagline (verbatim from GitHub):** *"Implement a ChatGPT-like LLM in PyTorch from scratch, step by step"*
- **README opener (verbatim):** *"This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code repository for the book Build a Large Language Model (From Scratch)."*
- **Book author intro (verbatim):** *"In Build a Large Language Model (From Scratch), you'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. In this book, I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples."*
- **Created:** 2023-07-23 → wiki build 2026-05-19 = **1,032 days old (~2 years 10 months)**
- **Book published:** 2024-09-12 (per CITATION.cff)
- **Author:** Sebastian Raschka (`rasbt`); **"AI Research Engineer working on LLMs"**; PhD academic-author-educator; 38K followers on GitHub; 149 public repos; blog "Ahead of AI" at magazine.sebastianraschka.com
- **Publisher:** Manning
- **ISBN:** 978-1633437166
- **License:** **Apache-2.0 WITH CUSTOM CARVE-OUT** — explicitly "Source form... explicitly excluding any books specific to this software and any related images" (Apache modified)
- **Homepage URL (verbatim from GitHub):** `https://amzn.to/4fqvn0D` (Amazon affiliate link to book — corpus-first homepage-as-affiliate-link)
- **Stats at v74 wiki build:** **95,135 stars / 14,569 forks / 786 watchers / 4 open issues / 1,051 commits** (since 2023-07-23); fork ratio 0.153 (15.3% — corpus-near-record alongside v65 17.8%)
- **Pinned at author level (6 repos):** LLMs-from-scratch (95.1K) + reasoning-from-scratch sequel (4.4K) + machine-learning-book (5.2K) + deeplearning-models (17.5K) + llm-architecture-gallery (1.2K) + mini-coding-agent (859) — **multi-book-portfolio shape**

### Subject classification (13-axis, v2.2 enhanced)

| Axis | Value |
|------|-------|
| **Tier** | **T3 Education — NEW sub-archetype "Educational-Book-Companion"** (corpus-first book-companion repo in v60+ corpus window; distinct from T3 course-tutorial v6 ai-agents-for-beginners / T3 educational-skill-collection v55 mattpocock / T3 single-skill-derivative v63 karpathy) |
| **Archetype** | solo-academic-author-educator (Sebastian Raschka; PhD; multi-book Manning portfolio; 38K GitHub followers; published "Machine Learning with PyTorch and Scikit-Learn" 2022 + "Build a Large Language Model From Scratch" 2024 + "Build a Reasoning Model From Scratch" sequel). **NEW Pattern #19 sub-mechanism 19e candidate "educator-multi-book-portfolio"** at solo-academic-author scale (distinct from 19a founder-personal-tool / 19b corporate-strategic / 19c community-collective / 19d corporate-observation-as-marketing). |
| **Scale tier** | **EXTREME-HIGH** (95K stars = top-tier corpus subject; among the highest-starred T3 subjects in corpus) |
| **Primary lang** | **Jupyter Notebook 74.7% + Python 25.3%** — corpus-second Jupyter-Notebook-primary subject after v36 pi-mono (which was Python-primary); FIRST corpus T3 subject with Jupyter-Notebook-primary language ratio |
| **Packaging tool** | `git clone --depth 1` + Manning ZIP download — **NO npm/cargo/Homebrew/etc.** — pedagogical reference implementation, not installable tool |
| **Origin story** | solo-academic-author-book-companion-project (companion to Manning book + Manning video course 17h15m + Manning Forum + GitHub Discussions); not corporate-strategic, not viral-MVP, not tool-multi-product |
| **Methodology** | **pedagogical step-by-step LLM implementation** — chapter-by-chapter Jupyter notebooks teaching: text-data → attention → GPT model → pretraining → finetuning (classification + instruction-following); appendix A PyTorch intro + appendix D training enhancements + appendix E LoRA |
| **Governance file count** | 4 explicit files (README + LICENSE.txt + CITATION.cff + CONTRIBUTING.md) — moderate; pedagogically-organized rather than tool-governance |
| **Agent/skill count** | N/A (educational artifact, not a tool) — 7 chapters + 5 appendices + extensive bonus folders (Llama/Qwen/Gemma implementations + BPE tokenizers + KV cache + LoRA + UI demos) |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | PyTorch (foundational framework dep) + Manning publisher (book metadata) + Ollama (in `ch07/ollama_evaluate.py` for instruction-tuning eval — NOT a corpus subject) + Llama/Qwen/Gemma model architecture families (in bonus folders) + Karpathy-style pedagogical lineage IMPLICIT (similar to nanoGPT educational approach but methodology-distinct) |
| **Agent platforms supported** | N/A — not an agent tool |
| **Living-Domain-Standards Tracking** | **YES — N+1 strengthening** at smaller scale than v71's 78a (5-layer multi-vendor synthesis); tracks LLM-model-architecture evolution: bonus folders for Llama/Qwen/Gemma implementations + appendix D training enhancements + appendix E LoRA = LDS evolution tracking via book updates |

### Velocity-screen + engagement-signal (v2.2 NEW)

| Metric | Value | Corpus context |
|--------|-------|---------------|
| Age | **1,032 days (~2 years 10 months / ~34 months)** | LONG-DURATION corpus subject; one of longest-sustained at significant rate |
| Stars | **95,135** | TOP-TIER corpus scale (among highest in corpus) |
| Forks | **14,569** | very high (fork-ratio 0.153 = 15.3% near-corpus-record) |
| Watchers (subscribers) | **786** | moderate |
| Open issues | 4 | exceptionally low for 95K-star repo |
| **`stars_per_day`** | **~92.2** | **LONG-SUSTAINED-MEDIUM** — BELOW v72-audit HIGH-NOT-EXTREME (150-300/d) but SUSTAINED over 1,032 days; **NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)"** |
| `fork_ratio` (forks/stars) | **0.153 (15.3%)** | very high — corpus-second after v65 claude-code-system-prompts 17.8%; high active-deployment intent (people fork to follow along with book) |
| `watchers_ratio` (subscribers/stars) | 0.0083 | low |
| `open_issues_ratio` | 0.00004 | extraordinarily low — pedagogical content stable, not tool with active bug surface |

**Velocity verdict:** **LONG-SUSTAINED-MEDIUM** at 92.2 stars/day for 1,032 days. NEW Pattern #52 sub-class candidate (60-150/d × 1000+d) distinct from v72-audit-registered HIGH-NOT-EXTREME (150-300/d) and EXTREME-VIRAL (>300/d). v75+ audit batch addition.

### Pattern Library pre-check (Phase 0.5 expanded v2.2)

- **NEW T3 sub-archetype candidate "Educational-Book-Companion":** **CORPUS-FIRST.** Book is the primary artifact; code is companion (Inverted vs. v6 ai-agents-for-beginners where course is primary and skills-as-tutorial; vs. v55 mattpocock where skill-collection IS the artifact). 7-chapter + 5-appendix Jupyter notebook structure mirrors book chapter-structure 1:1. **N=1 PROVISIONAL.** Phase 4b SECONDARY candidate (within-T3-archetype expansion).

- **NEW Pattern #45 Dual-Licensing sub-typology candidate 45d "Apache-2.0 with Book-Content-Exclusion-from-Source":** **CORPUS-FIRST.** License explicitly states *"Source form shall mean the preferred form for making modifications, explicitly excluding any books specific to this software and any related images, and includes but is not limited to software source code, documentation source (excluding books and images related to this software), and configuration files."* — Apache modified clause carving out copyrighted book + image content from open-source coverage. Structurally distinct from prior 45 sub-typologies: 45a Apache+commercial-shield (Unsloth v23) / 45b MIT+PolyForm-Shield (AutoGPT v59) / 45c MIT-wrapper+proprietary-binary-with-Acceptable-Use (CloakBrowser v69). 45d is INTRA-Apache modification (single license file with carve-out), not dual-file pattern. **N=1 PROVISIONAL.** → **Phase 4b PRIMARY: NEW Pattern #45 sub-typology 45d proposal-document** (SECOND formal sub-typology proposal-document in corpus history after v69's 45c).

- **NEW Pattern #19 sub-mechanism 19e candidate "educator-multi-book-portfolio":** Solo academic-author-educator portfolio: 4+ books + companion repos (LLMs-from-scratch + reasoning-from-scratch + machine-learning-book + deeplearning-models + llm-architecture-gallery). Distinct from sub-mechanism 19a founder-personal-tool-portfolio (Raschka's portfolio is BOOK-companions not tool-products). **N=1 PROVISIONAL** within Pattern #19. v75 stale-check.

- **NEW Pattern #52 Extreme-Viral-Velocity sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity":** 60-150/d × 1000+d. **CORPUS-FIRST** sustenance-over-3-years subject. Distinct from v72-audit HIGH-NOT-EXTREME (150-300/d × ≥30d) + EXTREME-VIRAL (>300/d × ≥30d). N=1 PROVISIONAL.

- **Pattern #78 Living-Domain-Standards N+1 strengthening:** Bonus folders for Llama/Qwen/Gemma model architectures + appendix D training enhancements + appendix E LoRA = LDS evolution tracking via book companion updates. Smaller scale than v71 agents-best-practices 78a 5-layer synthesis but distinct mechanism (book-companion-content-update vs single-skill-multi-vendor-synthesis).

- **Pattern #57 Cross-Wiki-Citation:** **WEAK** — README cites publisher Manning + Amazon (homepage) + Ollama (used in ch07 for instruction-tuning eval; not a corpus subject) + Llama/Qwen/Gemma (model architectures; not corpus subjects). No direct corpus-subject URL citation identified. Phase 0.9 (d) → FAIL.

- **NEW observational candidate OC-R "Affiliate-Link-As-Repository-Homepage":** GitHub `homepage` field = `https://amzn.to/4fqvn0D` (Amazon affiliate link to book). Corpus-first homepage-as-monetization-link; corpus-typical homepage is project-website or product-page. N=1 OBSERVATIONAL. v77 stale-check + v80 retire-check.

- **NEW observational candidate OC-S "Methodology-Influence-Node-Without-Operational-Tool":** Sebastian Raschka is a methodology-influence-node (foundational ML educator) but LLMs-from-scratch is NOT a vault-operational tool — Storm Bear uses LLMs (Claude Code) but doesn't need to build them from scratch. Corpus-pattern observation: Phase 0.9 (c) can STRONG PASS without (b) PASS. Sister to v63 Karpathy. N=2 candidate (Karpathy + Raschka). v75+ for N=3 evaluation. **N=2 EARLY-promotion-eligible at v75+ audit.**

### Storm Bear meta-entity Phase 0.9 STRICT (decision pre-registered)

**Verdict: 1/4 STRICT PASS = WEAK INCLUDE** (returns to WEAK after v73's STRONGEST; strength categorization continues to discriminate)

| Criterion | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| (a) Author archetype peer | ❌ **FAIL** | Sebastian Raschka is PhD-level academic ML educator/research-engineer; NOT developer+Scrum-coach archetype. Different field (ML academia + Manning publishing vs vault-Scrum-coaching). |
| (b) Operational tool for Scrum-coaching | ❌ **FAIL** | LLMs-from-scratch is educational book-companion reference for LEARNING LLM internals. Storm Bear's vault USES LLMs (Claude Code substrate) as black-box product; building LLMs from scratch is academic-pedagogical knowledge, not vault-operational tool. NOT a pilot candidate. |
| (c) Methodology-influence-node | ✅ **STRONG PASS** | **Sebastian Raschka is recognized ML methodology-influence-node** — PhD academic + multi-book Manning author + 38K-follower educator + "Ahead of AI" blog. **Sister to v63 Andrej Karpathy "corpus-foundation-individual" inheritance.** Vault's understanding of LLM substrates implicit-shaped by educators like Raschka. **STRONGEST methodology-influence-node candidate since v63 Karpathy** (Karpathy = corpus-foundation; Raschka = corpus-second-foundation-individual). |
| (d) In-corpus sibling reference | ❌ **FAIL** | README cites Manning publisher + Amazon (homepage) + PyTorch + Ollama (used in ch07/ollama_evaluate.py) + Llama/Qwen/Gemma. Ollama is NOT a corpus subject (per probe of v1-v73 entries). No corpus-subject URL citation identified. |

→ **WEAK INCLUDE (1/4)** — returns to WEAK after v73's STRONGEST INCLUDE. Strength categorization continues to discriminate empirically.

**Streak effect:** Post-v64-RESET window now 10 consecutive PASS:
- v65 STRONGEST 3/4 STRICT
- v66 STRONG 4/4 STRICT
- v67 MODERATE 2/4 STRICT
- v68 WEAK 1/4 STRICT
- v69 WEAK 1/4 STRICT
- v70 MODERATE 2/4 STRICT
- v71 MODERATE 2/4 STRICT
- v72 MODERATE 2/4 STRICT
- v73 STRONGEST 3-4/4 STRICT
- **v74 WEAK 1/4 STRICT — returns to WEAK after STRONGEST; strength-categorization spectrum re-expanded across STRONGEST→WEAK in 2 wikis**

18-instance Phase 0.9 post-amendment window v57-v74 = 16 PASS / 2 SKIP = **88.9% INCLUDE rate** (slight uptick from v73's 88.2%).

Strength categorization v65-v74: STRONGEST × 2 + STRONG × 1 + MODERATE × 4 + WEAK × 3 (MODERATE remains modal-status 4/10).

### Sibling detection

| Sibling | Relation | Why |
|---------|----------|-----|
| **v63 andrej-karpathy-skills** | **STRONGEST methodology-influence-node sibling** | Both academic-educator methodology-influence-nodes; Karpathy = corpus-foundation-individual (LLM Wiki pattern source; vault foundation); Raschka = corpus-second-foundation-individual at v74. Both Phase 0.9 (c) STRONG PASS. **N=2 OC-S evidence.** |
| v65 claude-code-system-prompts | fork-ratio sibling | 17.8% (v65) vs 15.3% (v74) = both top-tier active-deployment-intent fork-ratios |
| v6 ai-agents-for-beginners | T3 Education sibling | Both T3 Education; but v6 is course-tutorial (Microsoft corporate-org), v74 is book-companion (solo-academic-author) — different sub-archetypes |
| v55 mattpocock-skills | T3 Education sibling | Both T3 Education at solo-individual scale; but v55 is skill-collection-as-artifact, v74 is book-companion-where-code-supports-book |
| v23 Unsloth + v66 agentmemory + v64 claude-seo + v70 codegraph | Pattern #19 sub-archetype 19a sibling | All multi-product solo-individual portfolios; but v74 is multi-BOOK not multi-tool — NEW sub-mechanism 19e candidate |

### Tier placement decision

**T3 Education — NEW sub-archetype "Educational-Book-Companion"** — definitive. Rationale:
- Book is primary artifact (Manning publication + ISBN); code is companion (Apache-2.0 carve-out explicitly preserves book copyright)
- 7-chapter + 5-appendix structure mirrors book chapter-structure 1:1
- 17h15m Manning video course as second companion artifact
- Pedagogical step-by-step methodology (not tool-as-product)
- NOT T1 Augmentation (not installable as skill/tool)
- NOT T2 Service (no service surface)
- NOT T4 Bridge (no protocol/format-translation)
- NOT T5 Application (not user-facing application)

**Sub-archetype:** **Educational-Book-Companion** — NEW sub-archetype within T3; corpus-first in v60+ window. Phase 4b SECONDARY contribution.

### Phase 4b PRIMARY routing pre-registration

**PRIMARY:** **NEW Pattern #45 Dual-Licensing sub-typology 45d "Apache-2.0 with Book-Content-Exclusion-from-Source" registration proposal-document** — SECOND formal sub-typology proposal-document in corpus history (after v69's 45c). Apache-modified clause carving copyrighted book + image content out of open-source coverage; structurally distinct from prior 45a/b/c. All 3 sub-typology promotion criteria PASS with HIGH confidence. v75 stale-check + v80 retire-check. Formal sub-variant promotion at N=2 emergence.

**SECONDARY:**
- NEW T3 sub-archetype "Educational-Book-Companion" registration (within-T3-archetype expansion; N=1 PROVISIONAL)
- NEW Pattern #19 sub-mechanism 19e "educator-multi-book-portfolio" candidate (Raschka's 4+ pinned book-companion repos at solo-academic-author scale)
- NEW Pattern #52 sub-class candidate "LONG-SUSTAINED-MEDIUM-velocity (60-150/d × 1000+d)" — corpus-first sustained-3-year-at-significant-rate subject
- Pattern #78 N+1 LDS strengthening (model-architecture evolution tracking via bonus folders)
- NEW observational candidate OC-R "Affiliate-Link-As-Repository-Homepage" (Amazon affiliate URL as GitHub homepage)
- NEW observational candidate OC-S "Methodology-Influence-Node-Without-Operational-Tool" N=2 (Raschka + v63 Karpathy)

### Consolidation guard

**Pre-build state (post-v73 cc-switch wiki 2026-05-19):**
- 45 confirmed / 29 active / 0.644 ratio / 24 OCs
- Active count 29 = 1 below trigger threshold 30
- Ratio 0.644 well below 0.95 mini-audit trigger
- **PROCEED normally** — v74 contributes within-pattern strengthening + sub-typology proposal + sub-archetype expansion only

**v74 contribution to state:**
- 0 NEW top-level patterns
- ~2 NEW OC candidates (OC-R + OC-S; OC-S would be N=2 at registration with v63 Karpathy as second instance)
- NEW Pattern #45 sub-typology 45d via Phase 4b proposal-document
- NEW T3 sub-archetype "Educational-Book-Companion" registration
- Pattern #19 NEW sub-mechanism 19e candidate
- Pattern #52 NEW sub-class candidate
- Active count: stays at 29 (no new top-level patterns)
- Ratio: stays at 0.644 unchanged
- OC count: 24 → 26

---

## Cross-references

- **Routine:** [llm-wiki-routine-v2.2.md](../../05 Skills/llm-wiki-routine-v2.2.md)
- **Pattern Library:** [PATTERN_LIBRARY.md](../../PATTERN_LIBRARY.md)
- **v69 audit document:** [04 Reviews/(C) 2026-05-19 Pattern Library mini-audit ...md](../../04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE; LARGEST batch corpus-history; Pattern #83 N=5 PROMOTION + 23 other items).md)
- **Strongest methodology-influence sibling:** [v63 andrej-karpathy-skills](../andrej-karpathy-skills - Beginner Analysis/CLAUDE.md)
- **T3 Education siblings:** [v6 ai-agents-for-beginners](../ai-agents-for-beginners - Beginner Analysis/CLAUDE.md) + [v55 mattpocock-skills](../mattpocock-skills - Beginner Analysis/CLAUDE.md)
- **Pattern #19 sub-archetype 19a sibling:** [v23 Unsloth](../Unsloth - Beginner Analysis/CLAUDE.md) + [v70 codegraph](../codegraph - Beginner Analysis/CLAUDE.md)
- **v69 Pattern #45 sub-typology proposal precedent:** [v69 CloakBrowser](../CloakBrowser - Beginner Analysis/CLAUDE.md) (FIRST sub-typology proposal-document in corpus history)

---

## Phase status

- [x] Phase 0 — Pre-flight + probe complete
- [ ] Phase 1 — Scaffold (THIS COMMIT)
- [ ] Phase 2 — Source ingestion (3 clusters)
- [ ] Phase 3 — Entity pages (4 entities; Storm Bear meta WEAK INCLUDE 1/4)
- [ ] Phase 4a — Beginner bilingual guide (`03 Published/`)
- [ ] Phase 4b — Pattern #45 sub-typology 45d Apache-with-book-content-exclusion registration (`01 Analysis/`)
- [ ] Phase 5 — Iteration log + Pattern Library updates
- [ ] Phase 6 — Vault sync

Next: Phase 2 source ingestion — 3 clusters.
