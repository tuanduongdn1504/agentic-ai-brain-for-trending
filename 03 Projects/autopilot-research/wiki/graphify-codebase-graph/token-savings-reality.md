# The 71.5× claim — forensics

> **Source:** [[graphify-codebase-graph/_index]]. Adversarially verified (Workflow `wf_2f2a5052-7ac`). **Verdict: accurate-but-severely-misleading.** True for one specific benchmark; widely misrepresented as a general number.

## What "71.5×" actually measures

- The figure is **real and from the official repo** (`safishamsi/graphify` README): *"71.5× fewer tokens per query vs reading the raw files."*
- But it's **one specific benchmark**: a **52-file mixed corpus** = 3 Karpathy repositories + **5 research papers + 4 images**.
- **Baseline** = naively pasting raw files into prompts. **Graphify path** = querying the compact `graph.json` + `GRAPH_REPORT.md`.
- The README publishes **only the ratio**, not absolute before/after token counts, graph-construction cost, or the amortization period. So the 71.5× is, in the reviewers' words, "a black box."

## Why it doesn't generalize

The corpus is **cherry-picked in composition** — papers and images are *high-leverage compression targets*; real codebases are code-heavy, not mixed-media. Independent tests scatter wildly:

| Source | Result | Corpus |
|---|---|---|
| Official Graphify README | **71.5×** | 52-file mixed-media (Karpathy repos + 5 papers + 4 images) |
| stevescargall.com | ~79× | different/larger corpus (372K words) — built-in benchmark tool, not API-log validated |
| Exchangepedia (independent) | **7.3×** | a real (unnamed) Python codebase |
| Medium / browser-use (independent) | **~7-8% (≈1.07×)** | the browser-use project (113K vs 120K tokens) |
| roborhythms.com review | — | "the 71× headline does not survive contact with a normal-sized workday" |

**The variance between ~7% and 71.5× is structural (corpus-dependent), not measurement noise.** Note also: **no Anthropic / Claude Code team benchmark exists** — the 71.5× is the author's own measurement.

## Realistic expectations (by corpus size)

| Codebase | Expected per-query reduction |
|---|---|
| < 100 files | **1-3×** (possibly negative ROI — construction cost dominates) |
| 100-500 files | **5-15×** |
| 500+ files (mostly code) | **20-40×** |
| 52-file *mixed-media* (the benchmark) | 71.5× |

**Believe 2-8× on a normal repo.** The third-party blogs (skillbloomer, dev.to, gitpicks) repeated "71.5×"/"70×" as headlines with **no methodology or caveats** — marketing amplification, not science.

## The amortization trap

- The **first run costs tokens** (Pass 3 builds the graph). Savings only **compound on subsequent queries**.
- Rough math: if a build costs ~300-500K tokens and you save ~5K tokens/day, **payback is 60-100 days**, not hours. The browser-use ~7-8% result implies real payback is *months*, not queries.
- So Graphify is a bet on **a stable codebase you'll query repeatedly over a long time** — not a quick win on a one-off task or an actively-churning repo (which forces graph rebuilds).

## When it actually wins / loses

- ✅ **Wins:** large (500+ files) + stable + mixed-media (docs/papers/diagrams) + you'll run 100+ queries against the same snapshot + token cost is a real budget line.
- ❌ **Loses:** < ~200 files, one-off queries, code-only projects (no high-compression docs), or rapidly-changing code.

## The benchmark you should run (don't trust the headline)

1. Pick a representative project (200-1,000 files).
2. Measure **baseline**: run a typical query the normal way; read total tokens off the **Anthropic dashboard**.
3. Build the Graphify graph; run the **same** query; measure tokens (include the build cost).
4. Repeat over **one week, 10+ queries**.
5. Compare totals. **Expected: 2-8×, not 71.5×.**

> This ties directly to [[claude-api-cost-optimization/_index]] — Graphify is a *context-engineering* lever (load a compact graph instead of raw files), in the same family as prompt caching / programmatic tool calling / compaction. And point Pass 3 + queries at a local Ollama model → the only paid pass becomes **$0** ([[cowork-third-party-inference/_index]]).

## Key Takeaways

- 71.5× is **factually correct for a 52-file mixed-media best case** and **misleading as a general claim.**
- Independent real-world numbers: **7.3× (Python repo), ~7-8% (browser-use).** Plan for **2-8×.**
- Savings **scale with corpus size** and require **months of amortization** — it's a long-game bet on a stable repo.
- **No independent/Anthropic validation** of 71.5× exists; run your own dashboard-measured benchmark before believing any multiplier.
