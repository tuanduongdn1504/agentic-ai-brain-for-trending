# (C) 5-Minute Experiment Loop

> Entity page — Workflow primitive
> Sources: README automation mechanism + program.md workflow
> Format: 13-section canonical

## 1. What is it / Nó là gì

**5-Minute Experiment Loop** = autoresearch's core operational primitive. Each iteration: **edit train.py → commit → train 5 min → evaluate val_bpb → keep or revert → log**. Fixed 5-min wall-clock budget. ~12 iterations/hour. ~100 overnight. Enables comparative research velocity previously impossible manually.

## 2. Why it matters / Sao quan trọng

### Fairness enforcement

**Problem:** Without time limit, agent could game results:
- Train longer = always better val_bpb
- Agent learns "just increase epochs"
- No meaningful architectural insight

**Solution:** Fixed 5-min budget.
- Architecture wins on **efficiency**, not duration
- Novel optimizers + attention patterns + batch sizing compete fairly
- Overnight = 100 hypotheses at same footing

### Velocity enablement

Traditional ML research:
- Morning: propose hypothesis
- Day: implement + debug
- Evening: launch training
- Night: wait hours
- Next day: check result
- **~1 experiment/day**

autoresearch:
- Night: agent runs 100 experiments
- Morning: human reviews
- **~100 experiments/night = 100x velocity**

### Comparability invariant

Because every experiment = 5 min, **val_bpb directly comparable**. No normalization needed. Clean leaderboard.

## 3. Loop detailed (from program.md)

```
┌─ LOOP (continuous) ─┐
│                      │
│  1. Modify train.py  │
│     - New hypothesis │
│     - Small change   │
│                      │
│  2. Commit (git)     │
│     - Experiment ID  │
│     - Changelog msg  │
│                      │
│  3. Run training     │
│     - 5 min wall     │
│     - Fixed budget   │
│                      │
│  4. Evaluate         │
│     - val_bpb metric │
│     - Memory usage   │
│                      │
│  5. Decision         │
│     - Better? Keep   │
│     - Worse? Revert  │
│                      │
│  6. Log results.tsv  │
│     - Hash + metric  │
│     - Memory + status│
│                      │
│  └─ back to 1 ──────┘
```

## 4. 5-minute budget decisions

### Why 5 minutes?

**Trade-offs:**
- **Too short (<1 min):** Training doesn't reach meaningful loss; results noisy
- **Too long (>15 min):** Few experiments per night; comparability harder
- **Sweet spot 5 min:** ~100 exp/night, reasonable training signal

### Hardware adaptation

5-min budget on H100 = different token count than 5 min on A100 or consumer GPU.

**Karpathy's insight:** Let model adapt to hardware. Budget = wall-clock, not token count.

**Result:** Research insights transfer across hardware (architectural, not compute-specific).

### Comparison to training literature

Typical ML papers: ~hours to weeks per experiment.
autoresearch: ~minutes.

Different research scope:
- Papers: Deep insights, slow iteration
- autoresearch: Breadth exploration, fast iteration

**Both valid.** Different stages of research pipeline.

## 5. Agent decision protocol

### Keep vs revert rule

Binary: **val_bpb improved?** Keep. Else revert.

**Simplicity benefits:**
- Clear signal, no ambiguity
- No complex multi-objective weighting
- Agent spends no time deliberating

**Risks:**
- Overfits to val_bpb (but that's the defined objective)
- Doesn't value memory unless prompted
- Ignores training stability (unless crashes prevent completion)

### Memory consideration

program.md says: "VRAM increases acceptable only for meaningful gains."

**Implication:** agent biased toward same-memory-or-lower changes. Memory explosion = discard even if val_bpb improved marginally.

### Simplicity preference

"Code deletions yielding equal results are preferred over complex optimizations."

**Implication:** agent biased toward **Occam's razor**. Simpler train.py over complex. Matches Karpathy's philosophy.

## 6. Results.tsv structure (inferred)

```tsv
commit_hash    val_bpb    memory_gb    status       description
abc123def      0.823      12.4         KEPT         "Added RoPE"
def456abc      0.835      14.2         REVERTED     "Tried 12-layer"
...
```

### Why TSV not JSON
- Karpathy minimalism
- Easy grep + awk
- Jupyter reads natively
- Commit-diffable

## 7. Comparison to sibling iteration patterns

### T1 workflows (Claude Code plug-ins)
- ECC, Superpowers, gstack, GSD = human iterates per prompt
- No autonomous loop
- ~1 iteration / minute (human-paced)

### T2 goclaw
- Platform serves agents for users
- Iteration per-user, not meta-research

### T3 course
- N/A (learning resource)

### T4 notebooklm-py
- Per-call invocation
- No autonomous loop

### T5 deer-flow
- Long-horizon autonomous (minutes-hours per task)
- Single task, not iteration-loop
- Can repeat tasks but not built-for-iteration

### **T5 autoresearch**
- **Autonomous continuous loop**
- **~12 iterations/hour**
- **Optimization-focused**

→ **autoresearch uniquely targets iteration velocity.** deer-flow runs 1 big task; autoresearch runs 100 small tasks.

## 8. Comparison to Storm Bear routine

### Storm Bear routine
- 1 wiki per ~2 hours
- 7 phases sequential
- Non-iterative (one-shot)
- Quality > velocity

### autoresearch loop
- 100 experiments per night
- 6 steps per iteration
- Iterative (thousands possible)
- Velocity > quality (iteration provides quality via selection)

**Different optimization targets.** Both valid for respective domains (knowledge = quality, ML research = breadth).

### Possible hybrid

Could Storm Bear routine become iterative?
- Hypothesis: improved routine v2
- Run routine on test wiki
- Evaluate output quality
- Keep v2 if better, else revert
- 10 routine v2 variants tested over weekend?

**Possible but expensive** (each test = ~2h, ~$2 LLM spend). autoresearch's 5-min per iteration = 25x cheaper.

## 9. Trade-offs / Limitations

### Strengths
- **Velocity enabler** — 100x human researcher
- **Fair comparison** — fixed budget = honest metrics
- **Minimal state** — each iteration independent
- **Git-traceable** — full history

### Weaknesses
- **Budget gaming impossible** — but agent may optimize FOR 5-min specifically (overfitting to budget)
- **No deep runs** — important long-tail experiments miss (e.g., 20-min experiments revealing late instability)
- **Overfits to single metric** — val_bpb narrow; generalization ignored
- **Per-iteration cost** — agent LLM call per iteration, adds up
- **Short-memory** — agent may rediscover same bad ideas
- **No cross-experiment learning** — unless program.md updated, each iteration naive

## 10. Common pitfalls

1. **Agent exploits budget loophole** — e.g., skips validation to spend more on training
2. **Metric gaming** — finds train-time-only wins (not robust)
3. **Premature termination** — agent gives up on hypothesis mid-execution
4. **Irreversible mistakes** — somehow destroys state despite git; rare but possible
5. **Cost blowout** — 100 iterations × LLM call = non-trivial spend
6. **Silent failure mode** — training crashes, logs empty, counts as "reverted"; wasted budget
7. **Commit pollution** — 100 commits/night in main branch clutter

## 11. When NOT to use this pattern

- **Research needs deep runs** — <5 min insufficient for some questions
- **Non-ML domains** — pattern assumes training metric; other fields have different evaluation
- **Small budget** — 100 iterations × GPU = expensive cloud bills
- **Human-in-loop preferred** — some research requires judgment-intensive intermediate steps
- **Reproducibility-critical** — non-determinism creates noise

## 12. Storm Bear vault relevance

### Direct relevance

**Low-medium.** Storm Bear is knowledge domain, not ML. But:

### Meta-pattern Storm Bear could apply

**"Fixed budget per iteration" principle:**
- Storm Bear routine ~2h per wiki = budget
- Fairness: all wikis get same time
- Enables comparison: routine v1 vs v2 quality tested fairly

**"Keep/revert based on metric" principle:**
- Storm Bear doesn't have this explicit
- Could add: wiki output compared against 13-section compliance score
- Revert-to-v1 if v2 lower quality

### If Storm Bear routine becomes iterative

Could test routine v2 changes on corpus:
- Hypothesis: "change X improves routine"
- Run on test wikis (maybe rebuild 3 existing)
- Compare quality metrics
- Keep or revert

**But expensive.** autoresearch's 5-min luxury not available.

## 13. References / Nguồn

- Source: [[(C) README summary]] (automation mechanism) + [[(C) program.md agent skill summary]] (workflow)
- Related entities:
  - [[(C) Program.md as Agent Skill]] (skill orchestrates loop)
  - [[(C) val_bpb Metric + Evaluation Fairness]] (metric enables keep/revert)
  - [[(C) Karpathy's Meta-contribution to Storm Bear]] (pattern lineage)
- Sibling workflow patterns:
  - `../../deer-flow - Beginner Analysis/02 Wiki/(C) Sub-Agent System (Parallel Fan-out).md` (different pattern: parallel decompose)
