# (C) program.md agent skill summary

> Nguồn: `program.md` (7 KB, fetched 2026-04-19)
> Purpose: Understand the **agent's skill/instructions** — what Karpathy tells the autonomous agent to do

## TL;DR

`program.md` = **Markdown document** containing instructions for Claude/Codex-like agent. **~7 KB** — lightweight. Core objective: autonomously optimize val_bpb within 5-min training budget. Key constraints: only modify `train.py`, use git commits for tracking, continue indefinitely without asking human. **Direct parallel to Storm Bear's `llm-wiki-routine.md`** — both Markdown skills orchestrating autonomous agent loops.

## Core objective (from program.md)

> Autonomously optimize a machine learning model's validation bits-per-byte (val_bpb) metric through iterative experimentation within a fixed 5-minute training budget.

## Key capabilities granted

- **Code modification:** ONLY `train.py`. "Everything in train.py is fair game: model architecture, optimizer, hyperparameters, training loop, batch size, model size, etc."
- **Experimentation autonomy:** Continuous loop. No human approval between runs.
- **Git-based tracking:** Each iteration = commit; unsuccessful = revert.

## Workflow (from program.md)

### Setup phase
1. **Establish a branch** (e.g., `autoresearch/mar5`)
2. **Read in-scope files** (program.md, train.py, prepare.py)
3. **Verify data exists** (prepared by prepare.py)

### Experiment loop (forever)
1. **Modify code** (train.py hypothesis)
2. **Commit** (preserve state)
3. **Run training** (5 min fixed budget)
4. **Evaluate results** (extract val_bpb + memory)
5. **Keep** if improved, **revert** if not
6. **Log to `results.tsv`** (commit hash, performance, memory, status)

### Persistence
- Continue indefinitely without pausing
- Don't ask human for guidance mid-loop
- Human reviews logs offline

## Constraints (boundaries)

### What agent CANNOT do
- ❌ Modify `prepare.py`
- ❌ Install packages (environment fixed)
- ❌ Alter evaluation functions (metric integrity)
- ❌ Modify `program.md` itself
- ❌ Increase training budget beyond 5 min

### What agent should prefer
- ✅ VRAM increases **only for meaningful gains**
- ✅ Simplicity — code deletions yielding equal results preferred over complex optimizations
- ✅ Incremental hypotheses — small changes with clear rationale

## Agent's autonomy model

### Clear trust boundary

| Zone | Agent access | Rationale |
|------|--------------|-----------|
| `train.py` | Full modify | Where research happens |
| `prepare.py` | Read only | Ensures data + tokenizer stable |
| `program.md` | Read only | Human-curated skill |
| Evaluation | Read only | Prevent metric gaming |
| Environment | No install | Prevent dependency drift |
| Git | Full | Required for tracking |

### Operational autonomy

- **No approval gates** mid-loop
- **No escalation** to human unless critical failure
- **Indefinite runtime** — until human stops

**Implied risk model:** Failure = wasted compute (bounded by budget). No security risk (no internet, no package install).

## Workflow visualization

```
┌──────────────────────────────────┐
│ Setup (once per campaign)        │
│ - Create branch                  │
│ - Read files                     │
│ - Verify data                    │
└─────────┬────────────────────────┘
          │
          ▼
┌──────────────────────────────────┐
│ Loop (forever)                   │
│  ┌───────────┐                   │
│  │Modify code│                   │
│  │ (train.py)│                   │
│  └─────┬─────┘                   │
│        ▼                         │
│  ┌───────────┐                   │
│  │ Commit    │                   │
│  └─────┬─────┘                   │
│        ▼                         │
│  ┌───────────┐                   │
│  │  Train    │                   │
│  │ (5 min)   │                   │
│  └─────┬─────┘                   │
│        ▼                         │
│  ┌───────────┐                   │
│  │ Evaluate  │                   │
│  │ (val_bpb) │                   │
│  └─────┬─────┘                   │
│        ▼                         │
│  ┌─────────────────┐             │
│  │ Better?         │             │
│  ├─Yes──► Keep────┐│             │
│  └─No──► Revert──┐││             │
│                  │││             │
│  ┌───────────────▼▼▼┐            │
│  │ Log results.tsv   │            │
│  └─────┬─────────────┘            │
│        │                          │
│  back to top ◄─────────────────   │
└──────────────────────────────────┘
```

## Comparison to Storm Bear's `llm-wiki-routine.md`

Both = Markdown-based agent skills. Both = orchestrate autonomous loops.

| Aspect | autoresearch `program.md` | Storm Bear `llm-wiki-routine.md` |
|--------|--------------------------|----------------------------------|
| **Size** | ~7 KB | ~420 lines (larger) |
| **Target** | Research iteration loop | 7-phase wiki build |
| **Loop** | Infinite until human stops | One-shot per input URL |
| **Artifact** | Git commits + results.tsv | Wiki files in Obsidian |
| **Metric** | val_bpb | Wiki quality (implicit — 13-section compliance) |
| **Fairness** | 5-min training budget | ~2h session budget |
| **Human refine** | Yes (program.md iterated) | Yes (routine v2 upgrade planned) |
| **Skill format** | Markdown | Markdown |

### Key insight

**Both patterns identical at meta-level:**
- Human defines skill (Markdown)
- Agent follows skill (LLM)
- Loop executes task
- Keep/discard based on metric
- Human refines skill from results

**Storm Bear vault = direct descendant of Karpathy's thinking.** Storm Bear routine = Karpathy's pattern applied to knowledge management instead of ML research.

## Specific instructions observed

### Safety rails
- "Don't modify prepare.py"
- "Don't install packages"
- "VRAM increases only for meaningful gains"

### Preferences
- "Simplicity valued: code deletions yielding equal results preferred"
- Incremental改变 (small changes)

### Persistence
- "Continue indefinitely without pausing to ask the human for guidance"

## Iteration pattern for human

### Program.md evolution

Humans iterate program.md based on:
- Agent behaviors observed (missed opportunities, bad choices)
- Failure modes (crashes, infinite loops)
- New hypotheses to pursue
- Narrowing scope if agent wastes time

### Git log of program.md = meta-research history

**Speculation:** Karpathy's program.md commit history = rich study of how humans refine agent skills over time.

## Sections parallel to Storm Bear routine

### Setup phase ≈ Storm Bear Phase 0 (pre-flight)
Both: scaffold environment, verify prerequisites

### Experiment loop ≈ Storm Bear Phases 2-4 (sources + entities + publish)
Both: iterate creating artifacts

### Persistence ≈ Storm Bear Phase 6 (vault-sync)
Both: commit state before next iteration

### Log keeping ≈ Storm Bear iteration log
Both: track outcomes for future learning

## Trade-offs / Limitations of program.md approach

### Strengths
- **Markdown readable** — low barrier
- **Iteratively refined** — mistakes become instructions
- **Trust boundary clear** — explicit constraints
- **Self-contained** — skill + agent + code = minimal setup

### Weaknesses
- **Agent interpretability variance** — LLMs interpret instructions differently
- **Instructions drift** — as program.md grows, coherence risk
- **Git-based tracking** — fine for research, limits collaboration
- **No meta-monitoring** — agent doesn't self-assess whether instructions make sense

## Cross-references

- Main positioning: [[(C) README summary]]
- Related entities:
  - [[(C) Program.md as Agent Skill]] (entity page drawing from this)
  - [[(C) 5-Minute Experiment Loop]] (workflow primitive)
  - [[(C) Karpathy's Meta-contribution to Storm Bear]] (meta-synthesis)
- Storm Bear skill parallel:
  - `../../../05 Skills/llm-wiki-routine.md`
  - `../../../05 Skills/llm-wiki-ingest.md`
