# (C) Scripts cluster summary

> Nguồn: `prepare.py` (15 KB) + `train.py` (26 KB) + `analysis.ipynb` (8 KB) + `pyproject.toml` + `uv.lock`
> Purpose: Understand code infrastructure supporting autonomous research loop

## TL;DR

3 main scripts + dependencies. **`prepare.py` = fixed scaffolding** (data + tokenizer — agent can't touch). **`train.py` = agent's playground** (GPT model + optimizer + training loop — fully modifiable). **`analysis.ipynb` = human's tool** (post-hoc analysis Jupyter notebook). Dependency management via **uv** (Karpathy's preferred modern Python manager). Minimal, self-contained, single-GPU focused.

---

## Part 1 — prepare.py (15 KB, fixed scaffolding)

### Role
**Runtime preparation.** Agent CANNOT modify.

### Contents
- **Data download logic** — fetches training data
- **BPE tokenizer training** — vocab 8192 default
- **Constants + utilities** — shared between agent iterations
- **One-time setup** — runs once, produces reusable artifacts

### Why fixed?
- **Fairness:** Every experiment same data + tokenization
- **Efficiency:** Don't re-download dataset every run
- **Trust:** Prevent agent from "cheating" via different data prep
- **Baseline:** Comparison metric (val_bpb) makes sense only on same corpus

### Analogy to Storm Bear
prepare.py ≈ Storm Bear vault's **template folder** `(PROJECT TEMPLATE)/` — scaffolding that new projects inherit unchanged.

## Part 2 — train.py (26 KB, agent-modifiable)

### Role
**The experimental surface.** Agent's sole modification target.

### Contents (inferred từ README architecture)
- **GPT model implementation** — configurable depth, attention pattern
- **Optimizer** — Muon + AdamW hybrid (default; agent can change)
- **Training loop** — data loading, forward, backward, step
- **Evaluation integration** — calls validation at end, outputs val_bpb
- **Logging** — writes metrics for agent to read

### Configurable dimensions (from README)
- Model depth (default 8)
- Attention pattern (SSSL or L)
- Optimizer choice
- Vocabulary size (default 8192)
- Sequence length (default 1024)
- Batch size
- Total tokens trained

### Why this is the only modifiable file
- **Research happens here** — all hypotheses test via train.py
- **Clear scope** — agent can't break prepare.py accidentally
- **Budget respected** — train.py runs within 5-min budget

### Analogy to Storm Bear
train.py ≈ Storm Bear vault's **wiki pages** — where experimental thinking happens. Entity pages are "modifiable" vs index.md which is structural.

## Part 3 — analysis.ipynb (8 KB, human tool)

### Role
**Post-hoc human analysis.** Agent doesn't interact with.

### Contents
- Jupyter notebook reading results.tsv
- Visualizations (likely progress.png generated from this)
- Comparison across experiments
- Pattern detection in agent's experimental choices

### Purpose
**Human intelligence layer.** Agent runs 100 experiments; human analyzes trends + refines program.md.

### Human role in loop
1. Agent experiments overnight
2. Morning: human opens analysis.ipynb
3. Human sees patterns, identifies missed opportunities
4. Human refines program.md (maybe: "pay attention to X dimension we missed")
5. Next night: agent runs with updated instructions

### Analogy to Storm Bear
analysis.ipynb ≈ Storm Bear vault's **iteration logs** — retrospective human analysis of agent's work, feeding into next version.

## Part 4 — pyproject.toml + uv.lock (Python packaging)

### uv package manager
Karpathy consistently uses **uv** in recent projects. Modern Python tooling:
- Fast resolution (Rust-based)
- Reproducible lock files
- Cross-platform
- Replacing pip + venv for new projects

### Implications
- **Reproducibility:** uv.lock = exact dependency versions
- **Minimal deps:** pyproject shows Karpathy's minimal-philosophy applied
- **Setup:** `uv sync` gets everything going

### Analogy to Storm Bear
uv.lock ≈ Storm Bear vault's **`CLAUDE.md` file** — reproducible context that ensures consistent behavior.

## Part 5 — Role separation (trust architecture)

```
Fixed (human-maintained) ──────── prepare.py
                                  program.md
                                  pyproject.toml
                                  evaluation functions
                                  
Modifiable by agent ─────────────── train.py
                                    
Human analysis tools ────────────── analysis.ipynb
                                    results.tsv (written by agent)

Control plane ─────────────────── Git (branches, commits, reverts)
```

## Part 6 — Minimalism observation

### File count
- 1 README (positioning)
- 1 program.md (skill)
- 1 prepare.py (data)
- 1 train.py (experiment surface)
- 1 analysis.ipynb (human tool)
- 1 pyproject.toml (deps)
- 1 uv.lock (versions)
- 1 progress.png (visualization)
- **Total: 8 files** (including binaries)

### Comparison to sibling codebases

| Wiki | File count (approx) |
|------|---------------------|
| ECC (T1) | Thousands |
| Superpowers (T1) | Hundreds |
| gstack (T1) | ~100 |
| GSD (T1) | ~400 (396 .md alone) |
| goclaw (T2) | Thousands |
| course (T3) | ~50 |
| notebooklm-py (T4) | ~100 |
| deer-flow (T5) | ~100+ |
| build-your-own-x (outside) | 4 |
| **autoresearch (T5)** | **8** |

**autoresearch = 2nd smallest.** Only build-your-own-x smaller (single README).

### Karpathy's signature minimalism
- **llm.c** ~1000 lines C
- **makemore** ~500 lines Python
- **nanoGPT** < 500 lines
- **autoresearch** = same philosophy applied to research automation

## Part 7 — What's NOT included (implicit design choices)

### Missing
- ❌ **No test framework** — experiments are the tests
- ❌ **No CI** — human reviews results.tsv offline
- ❌ **No Docker** — bare Python + uv
- ❌ **No GUI** — terminal + Jupyter only
- ❌ **No multi-agent orchestration** — single agent
- ❌ **No cloud integration** — local single-GPU only
- ❌ **No cost tracking** — user responsible

### Why
Minimalism = educational value. Adding infrastructure = distracts from core idea.

## Part 8 — Development environment (implied)

### Requirements
- Python 3.10+
- uv (Karpathy's modern pip replacement)
- CUDA-capable NVIDIA GPU
- H100 recommended (tested)
- Single-node (no distributed)
- Terminal for monitoring
- Jupyter for analysis

### Absence of requirements
- No Docker
- No Node.js
- No frontend
- No database
- No orchestration layer

### Compared to deer-flow (T5 peer)
| Environment | deer-flow | autoresearch |
|-------------|-----------|--------------|
| **Python** | ✅ | ✅ |
| **Node.js** | ✅ (frontend) | ❌ |
| **Nginx** | ✅ | ❌ |
| **Docker** | Preferred | ❌ |
| **GPU** | Optional | **Required** |
| **Complexity** | High | Minimal |

→ **autoresearch = opposite complexity pole of deer-flow in T5 tier.**

## Part 9 — Reproducibility

### Enabled by
- uv.lock (exact deps)
- pyproject.toml (declared requirements)
- prepare.py (deterministic data prep)
- Fixed 5-min budget (time bound)

### Limited by
- GPU non-determinism (training variance across runs)
- Hardware differences (H100 vs A100 vs consumer GPU)
- LLM non-determinism (agent choices vary)

### Reproducibility tier
**Partial.** Environment reproducible; experiments not bitwise reproducible due to GPU + LLM variance.

## Part 10 — Cross-vault lessons

### Storm Bear could adopt

1. **uv for routine automation** — if Storm Bear ever builds Python tooling, uv = Karpathy-aligned
2. **Trust boundary clarity** — separate fixed (template) vs modifiable (wiki) vs analysis (logs) zones
3. **Minimal infrastructure** — resist over-engineering

### Storm Bear already has parallels

1. **Routine-as-skill** — `llm-wiki-routine.md` like program.md
2. **Template scaffolding** — `(PROJECT TEMPLATE)/` like prepare.py
3. **Iteration logs** — like analysis.ipynb workflow
4. **Git commits** — already used

## Cross-references

- Main positioning: [[(C) README summary]]
- Agent skill: [[(C) program.md agent skill summary]]
- Entity pages:
  - [[(C) 5-Minute Experiment Loop]] (scripts enable loop)
  - [[(C) val_bpb Metric + Evaluation Fairness]] (train.py produces)
  - [[(C) Karpathy's Meta-contribution to Storm Bear]] (synthesis)
- Sibling infra comparisons:
  - `../../deer-flow - Beginner Analysis/02 Wiki/(C) Architecture + Contributing cluster summary.md`
