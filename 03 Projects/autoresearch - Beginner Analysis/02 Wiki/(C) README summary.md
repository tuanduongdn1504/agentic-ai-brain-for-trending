# (C) README summary — autoresearch

> Nguồn: `README.md` (8 KB, fetched 2026-04-19)
> Repo: `karpathy/autoresearch`

## TL;DR

**autoresearch = Andrej Karpathy's autonomous ML research framework.** AI agents overnight optimize nanochat training on single GPU. Agent (Claude/Codex-like) reads `program.md`, modifies `train.py`, runs 5-min experiments, evaluates val_bpb, keeps/reverts, logs, repeats. **~100 experiments overnight.** Karpathy's vision of "frontier AI research conducted by automated agent swarms rather than human researchers." **74K stars, 10.8K forks.** Tier 5 "Agent-as-application" entrant #2 (validates multi-entrant with deer-flow).

## Positioning / framing

- **Title:** "Autoresearch: Autonomous AI-Driven Model Optimization"
- **Audience:** ML researchers + agentic AI enthusiasts
- **Philosophy:** Automation of research iteration (conceptual evolution from manual exploration)
- **Lineage:** Extends nanoGPT/nanochat (Karpathy's minimal educational ML infrastructure)
- **Vision:** Frontier AI research by automated agent swarms, overnight runs replacing human iteration

## The Research Problem

**Core challenge:** Discover optimal model architectures, hyperparameters, training strategies within **fixed computational budget** — without human intervention between iterations.

**Traditional approach:** Human researcher manually:
- Changes hyperparameter
- Runs experiment
- Analyzes result
- Iterates
- Sleeps between runs (wall clock lost)

**autoresearch approach:** Agent does all of above autonomously, including overnight.

## AI Agent Setup

**Single agent architecture.** Claude/Codex-class LLM operates:

- **Role:** Reads `program.md` for instructions, modifies `train.py`, executes experiments
- **Loop:** Edit code → train 5 min → evaluate val_bpb → retain OR discard → repeat
- **Cadence:** ~12 experiments/hour, ~100 overnight
- **Skill:** `program.md` provides "lightweight skill" — humans iteratively refine

### Agent ≠ Storm Bear Claude

- autoresearch agent = autonomous running Python, git commits, no human in loop
- Storm Bear Claude = routine execution in Claude Code session với Cvtot oversight

Different operational modes; similar concept (LLM + instructions + loop).

## File Architecture

| File | Role | Modifiable by agent? |
|------|------|----------------------|
| `prepare.py` (15 KB) | Fixed constants, data prep (downloads, BPE tokenizer), utilities | **❌ No** |
| `train.py` (26 KB) | GPT model + optimizer + training loop — **fair game** | **✅ Yes** |
| `program.md` (7 KB) | Human-editable baseline agent instructions | **Human-only** |
| `analysis.ipynb` (8 KB) | Human post-hoc analysis notebook | **Human-only** |
| `pyproject.toml` | Python dependencies | Read-only |
| `progress.png` (253 KB) | Visualization of progress | - |

**Clear trust delineation:**
- Agent modifies ONLY train.py
- Everything else = fixed scaffolding

## Nanochat Context

autoresearch = "simplified single-GPU implementation of nanochat" (Karpathy's earlier project).

**nanochat:** Karpathy's chatbot training framework emphasizing:
- Platform-wide support
- Flash Attention 3 kernel fallbacks
- Minimal educational code
- Self-contained training

autoresearch inherits philosophy, restricts to single-GPU, adds autonomous agent loop.

## Single-GPU Constraints & Methodology

### Fixed 5-minute wall-clock budget

**Why:**
- Experiments **comparable** despite architectural changes
- **Platform-specific optimization** — model adapts to compute available
- **~100 experiments** feasible overnight
- **Fairness** — no cheating với longer training

### val_bpb metric

**val_bpb = validation bits-per-byte**
- Vocabulary-size-independent
- Enables fair comparison across architectural variations (different vocab sizes can be compared)
- Lower = better

**Why not loss or perplexity?**
- Cross-vocabulary comparison impossible
- val_bpb normalizes

### Platform

- Single NVIDIA GPU (tested H100)
- Python 3.10+
- uv package manager
- No distributed training

## Automation Mechanism

```
1. Agent receives context từ program.md
2. Agent modifies train.py (model, optimizer, batch, architecture)
3. Agent commits change (git)
4. Agent executes training (5 min fixed)
5. Agent extracts val_bpb + memory from logs
6. Agent keeps (if improved) OR reverts (if not)
7. Agent logs to results.tsv (commit, metric, memory, status)
8. Agent repeats indefinitely
```

**Human role:** Review logs + iterate program.md instructions. Guide future behavior. Doesn't watch every run.

## Results & Findings

**README contains NO quantitative results.** Framework document, not research paper.

**Teaser:** Alludes to "10,205th generation codebase" — fictional or roadmap (unclear).

**Implication:** Karpathy publishing infrastructure for others to run. Findings community-driven.

## Architectural Details (train.py configurables)

| Parameter | Default | Agent can modify? |
|-----------|---------|-------------------|
| **Model depth** | 8 layers | ✅ |
| **Attention pattern** | SSSL (banded alternating) OR L (linear) | ✅ |
| **Optimizer** | Muon + AdamW hybrid | ✅ |
| **Vocabulary size** | 8192 | ✅ |
| **Sequence length** | 1024 | ✅ |
| **Batch size** | Variable | ✅ |
| **Total tokens** | Budget-bound | ✅ |

### For smaller devices

README provides guidance:
- Reduce depth to 4 layers
- Use TinyStories dataset
- Decrease sequence length to 256
- Lower batch size to 2^14 tokens

→ **Accessibility commitment** — not only H100 users can run.

## Relation to Karpathy's Work

### nanoGPT / nanochat lineage
- **Minimal code** — self-contained
- **Single-GPU** — accessible
- **Educational** — readable

### autoresearch evolution
- **Automation of iteration** — not just better training
- **Agent-driven** — LLM in the loop
- **Meta-research** — research ABOUT how to research

### Karpathy's broader impact
- **OpenAI founding member**
- **Tesla AI director (past)**
- **llm.c, makemore, tokenization videos** — teaching OSS
- **LLM Wiki pattern author** — **intellectual foundation of Storm Bear vault**

## Unique positioning vs 9 siblings

| Axis | autoresearch | Siblings comparison |
|------|--------------|---------------------|
| **Author stature** | Karpathy (foundational thinker) | Corporate / solo dev |
| **Domain** | ML research automation | Various (agent tooling, education, bridges) |
| **Form factor** | Python scripts | Apps / libraries / skills |
| **T5 specialization** | ML research specialist | deer-flow = general autonomous |
| **Star power** | 74K stars (2nd largest) | Various |
| **Meta-relevance to Storm Bear** | **PEAK** (LLM Wiki pattern author) | Lower |

## Meta-relevance to Storm Bear vault (PEAK)

### Karpathy = Storm Bear's intellectual lineage

Storm Bear root CLAUDE.md explicit:
> "following Karpathy's LLM Wiki pattern — instead of re-deriving knowledge from scratch on every query, the LLM incrementally builds and maintains a structured wiki"

**autoresearch = Karpathy's OTHER meta-pattern:** agents iterate research, not wikis.

**Parallel patterns:**

| Pattern | Storm Bear manifestation | autoresearch manifestation |
|---------|--------------------------|---------------------------|
| **LLM-maintained iteration** | Wiki pages | train.py experiments |
| **Human refines skill** | `llm-wiki-routine.md` | `program.md` |
| **Autonomous loop** | Routine phases 1-7 | Edit-train-eval-log loop |
| **Persistent artifact** | Obsidian vault | Git commit history |
| **Metric-driven keep/discard** | Entity page quality | val_bpb improvement |
| **Human-in-loop oversight** | Cvtot reviews published guides | Researcher reviews results.tsv |

→ **autoresearch :: research = Storm Bear :: knowledge.** Same meta-pattern, different domain.

### Cross-domain learning

**From autoresearch, Storm Bear could learn:**
1. **Git-based iteration tracking** — vault commits already do this; maybe formalize "experiment" concept per wiki
2. **Fixed-budget fairness** — time-bound each wiki build (routine already ~2h ceiling)
3. **Results.tsv** — structured experiment log; Storm Bear could add iteration log more uniformly
4. **Branch per campaign** — autoresearch uses `autoresearch/mar5` branch; Storm Bear could use branches for experimental vault versions

**From Storm Bear, autoresearch could adopt:**
1. **13-section entity page format** — structured knowledge representation
2. **Bilingual output** — VN + EN (autoresearch is EN-only, Karpathy's audience global)
3. **Published guide tier** — distinct from raw wiki, optimized for new audience

## Signals of quality / trust

- **74K stars** — Karpathy brand + genuine utility
- **Minimal codebase** — no over-engineering
- **Clear trust boundary** (prepare.py vs train.py)
- **Reproducible** (pyproject + uv.lock)
- **Educational philosophy** — Karpathy's commitment
- **Active development** — pushed 3 weeks ago

## Risks / watchouts

- **Autonomous agent modifying code** — sandbox responsibility on user
- **No quantitative results** — framework unproven as research tool (yet)
- **Cost unbounded** — overnight runs = LLM + GPU spend
- **Single-GPU only** — non-distributed; doesn't scale to frontier models
- **Experimental** — Karpathy may pivot or abandon
- **Non-deterministic training** — reproducibility challenges

## Open questions (→ `01 Analysis/(C) open questions.md`)

1. Quantitative results achieved?
2. Karpathy's intent (pedagogical vs serious?)
3. 10,205th-generation tease meaning
4. Hardware fairness beyond H100
5. Reproducibility discipline
6. Safety / sandbox
7. Agent choice benchmark
8. Storm Bear integration potential

## Sources list (for Phase 2 ingestion)

- README.md (this summary) — 8 KB
- program.md — the agent skill
- Scripts cluster (prepare.py + train.py + analysis.ipynb)

## Cross-references

- Sibling summaries (all 9):
  - 4 T1 agent-assistant
  - 1 T2 goclaw
  - 1 T3 course
  - 1 T4 notebooklm-py
  - 1 T5 deer-flow (**direct peer**)
  - 1 outside-scope build-your-own-x
- **Meta-lineage:**
  - Karpathy's LLM Wiki pattern = Storm Bear's foundational philosophy
  - Root vault `CLAUDE.md` — credits pattern explicitly
