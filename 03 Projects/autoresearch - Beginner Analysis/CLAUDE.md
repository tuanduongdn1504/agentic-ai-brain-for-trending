# autoresearch - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`karpathy/autoresearch`](https://github.com/karpathy/autoresearch) — Andrej Karpathy's autonomous ML research framework (AI agents overnight optimize model training on single GPU, ~100 experiments, `program.md` as agent skill). **74K stars, 10.8K forks.** **Tier 5 entrant #2 — validates multi-entrant claim for "Agent-as-application" tier** (after deer-flow v9). **Highest meta-relevance trong corpus** — Karpathy = source of LLM Wiki pattern Storm Bear vault is built upon.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** v1 (10th auto-execution — **T5 multi-entrant validation + Karpathy meta-reflection**):

- **Ingest sources via WebFetch** — README (8 KB), program.md (7 KB, the agent's skill), scripts cluster (prepare.py + train.py + analysis.ipynb)
- **Cross-reference với 9 sibling wikis** — T5 deer-flow is direct peer
- **Phase 4b = T5 2-way comparison + Karpathy meta-reflection** (validates T5 tier + honors pattern-source relationship)
- **Beginner roadmap** — different audience: ML researchers adopting autonomous research vs Scrum coach adopting autonomous workflows (deer-flow angle)

**Prime directive:** Outcome = wiki + T5 tier validation + honor Karpathy meta-relevance (his LLM Wiki pattern → Storm Bear vault → this wiki). Nudge nếu drift.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **T5 2-way comparison deer-flow vs autoresearch** (same-tier comparison, first time in T5) + **Karpathy meta-reflection** (similar spirit to v8 Storm Bear vault lessons).

## Key People

- **Andrej Karpathy** — original author (former OpenAI founding member, former Tesla AI director, **author of LLM Wiki pattern Storm Bear vault is based on**)
- **Cross-project:** 9 sibling wikis shipped. This is 10th = T5 second entrant + meta-relevance peak.
- **Storm Bear** — curator, operator

## Folder Structure

```
autoresearch - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← WebFetch-based (530 KB repo tiny; README + program.md + scripts)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 9 siblings MANDATORY** — especially T5 deer-flow (direct comparison peer)
- **Karpathy meta-relevance = critical theme** — honor Storm Bear's intellectual lineage
- **Note: Repo is MINIMAL** — just README + 4 scripts + 1 notebook + 1 image. Small surface but high impact (74K stars)

## Positioning note

**autoresearch trong v9 5-tier taxonomy:**

| Tier | Frameworks (n=10 now) |
|------|----------------------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD (4) |
| T2: Agent-as-service | goclaw (1) |
| T3: Agent-as-education | ai-agents-for-beginners (1) |
| T4: Agent-as-bridge | notebooklm-py (1) |
| **T5: Agent-as-application** | **deer-flow + autoresearch (2 ← MULTI-ENTRANT VALIDATED)** |
| Outside scope | build-your-own-x (1) |

→ **Tier 5 multi-entrant validated with N=2.** First multi-entrant tier (after T1 had 4 from v5).

### T5 2-way comparison preview

| Axis | deer-flow | autoresearch |
|------|-----------|--------------|
| **Specialization** | General-purpose harness | ML research specialist |
| **Form factor** | Full-stack app (Frontend + Backend) | Python scripts + Jupyter |
| **Task duration** | Minutes-hours | Overnight (~100 experiments) |
| **Orchestration** | LangGraph + sub-agents | Simple loop + git-based iteration |
| **Complexity** | High (4 services) | Low (5 files) |
| **Author** | ByteDance (corporate) | Karpathy (solo research) |
| **Maturity** | v2.0, 62K stars | Experimental, 74K stars |
| **License** | MIT | (to verify) |
| **User type** | Team / production | ML researcher / learner |

## Unique positioning claims của autoresearch

- **"AI agents running research automatically"** — autonomous research primitive
- **~100 experiments overnight** — research velocity
- **Single GPU (H100-tested)** — accessible ambition
- **5-min experiment budget** — fairness enforcement
- **val_bpb metric** — vocabulary-size-independent comparison
- **program.md = agent skill** — Markdown-based instructions, human-refined
- **Git-based experiment tracking** — commit → train → keep/revert → log
- **Karpathy's nanoGPT/nanochat lineage** — educational minimal philosophy
- **Extends Karpathy's LLM Wiki pattern meta-concept** — automation of research iteration = automation of knowledge iteration
- **Master branch (old style)** — like Karpathy's other projects (nanoGPT, makemore, llm.c)
- **74K stars** — Karpathy's standing as educator amplifies reach

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 10th LLM Wiki, 10th routine run, T5 multi-entrant validation + Karpathy meta-reflection

### Expected milestones

- [x] Phase 0 Pre-flight (API probe, 530 KB tiny, T5 entrant #2)
- [x] Phase 1 Setup — in progress
- [ ] Phase 2 Source ingestion — 3 summaries (README + program.md + Scripts cluster)
- [ ] Phase 3 Entity pages (4 — Program.md Agent Skill, 5-Min Experiment Loop, val_bpb Metric, Karpathy Meta-contribution)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **T5 2-way comparison deer-flow vs autoresearch + Karpathy meta-reflection**
- [ ] Phase 5 Iteration log v10
- [ ] Phase 6 Vault file updates
