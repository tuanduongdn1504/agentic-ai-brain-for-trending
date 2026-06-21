# (C) GLM-5 — LLM Wiki

> **Subject:** `zai-org/GLM-5` · **Wiki ship:** v176 · **Date:** 2026-06-21
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — `(a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG` *(GOAL-ALIGNED per operator direction; the stricter `(b) FAIL → OFF-GOAL CAPTURE` reading is the recorded operator-reviewable alternative — see §6)*
> **One-line:** Zhipu AI's open-weights **frontier agentic-coding LLM family** (GLM-5 / 5.1 / 5.2) — a 744B-parameter (40B-active) Mixture-of-Experts model with a 1M-token context, pitched at *"complex systems engineering and long-horizon agentic tasks"* and benchmarked head-to-head against Claude Opus. It is a **competitor base model**, not Claude/Anthropic tooling — relevant to the vault as the *engine* an autonomous coding agent runs on (and as a routable Claude-Code backend).

---

## 1. What it is (for a beginner)

GLM-5 is **a large language model** — the kind of thing Claude itself is — published by **Zhipu AI** (the `zai-org` GitHub org, the company behind the **Z.ai** API platform). It is *not* a tool you install, a skill, or an agent framework. It is the **model weights + the recipe to run them**, with a model card, benchmark tables, deployment guides, and a technical report (arXiv:2602.15763).

The repo's tagline is **"GLM-5: From Vibe Coding to Agentic Engineering"** — the explicit pitch is that this model is built to *do software engineering autonomously over long horizons*, not just autocomplete snippets. Zhipu's framing: it *"breaks complex problems down, runs experiments, reads results, and identifies blockers,"* sustaining *"optimization over hundreds of rounds and thousands of tool calls."*

It is **open-weights** (downloadable from Hugging Face and ModelScope in BF16 and FP8) and runnable locally on the usual frontier-model stacks (SGLang, vLLM, Hugging Face Transformers, KTransformers, Unsloth, Ascend NPU) or via the hosted **Z.ai API** (OpenAI-compatible).

**Why a competitor model is in this vault at all:** the vault's Goal #1 is *"Master Claude and autonomous agents for software development."* GLM-5 is a *rival* to Claude — but it is also (a) the *engine class* that powers autonomous coding agents, and (b) a model you can actually point Claude Code (or an OpenAI-compatible agent) at as a backend, exactly the move catalogued in **cc-switch v73** (route Claude Code to 9 alternative providers). So it earns a wiki entry as a **competitive-landscape / substrate-alternative reference** — held at MODERATE relevance, *not* as Claude/Anthropic core substrate. See §6 for the honest scoping.

---

## 2. The model family (verbatim-anchored)

| Model | Parameters | Context | Precision | Role |
|---|---|---|---|---|
| **GLM-5.2** | 744B (40B active) | **1M tokens** | BF16 / FP8 | *"our latest flagship model for long-horizon tasks"* — adds `reasoning_effort` effort levels |
| **GLM-5.1** | 744B (40B active) | (not specified) | BF16 / FP8 | *"agentic engineering, with significantly stronger coding capabilities than its predecessor"*; SOTA on SWE-Bench Pro |
| **GLM-5** | 744B (40B active) | long-context | BF16 / FP8 | the family base; pre-training scaled **23T → 28.5T tokens** vs GLM-4.5 |

So the repo named `GLM-5` actually hosts a **family** (5 → 5.1 → 5.2), with 5.2 the current flagship.

---

## 3. Architecture & engineering (what makes the (c) STRONG)

The engineering substance lives in the **model**, not in the repo's code (the repo is mostly a model card + deployment guides + a tech-report pointer). The model is frontier-scale and architecturally novel:

- **Mixture-of-Experts** — 744B total / **40B active** per token (sparse activation = frontier capacity at a fraction of the per-token compute).
- **DeepSeek Sparse Attention (DSA)** — *"largely reducing deployment cost while preserving long-context capacity"* (the mechanism that makes a 1M-token context economically deployable).
- **IndexShare** — reuses *"the same indexer across every four sparse attention layers, reducing per-token FLOPs by 2.9× at a 1M context length."*
- **Speculative decoding** — upgraded MTP layer, *"increasing the acceptance length by up to 20%."*
- **slime** — *"a novel asynchronous RL infrastructure"* developed for post-training efficiency.
- **`reasoning_effort` control** (`max` default / `high`) on GLM-5.2; thinking can be disabled with `enable_thinking=false`.

This is serious, frontier-lab engineering. The caveat for (c) is only that the *GitHub repo as an artifact* is a model-card/deployment hub, not a large codebase — but the *subject's* engineering weight is unambiguous.

---

## 4. Benchmarks — and the Claude comparison (page-stated)

These are **Zhipu's own published numbers** (page-stated; treat as vendor benchmarks, not independently replicated):

| Benchmark | GLM-5.2 | GLM-5.1 | Claude reference |
|---|---|---|---|
| **Terminal-Bench 2.1** (coding) | **81.0** | 62.0 | **Claude Opus 4.8: 85.0** |
| **SWE-Bench Pro** (coding) | **62.1** | 58.4 (SOTA) | — |
| **Vending Bench 2** (long-horizon ops) | — | — | GLM-5 **$4,432**, *"approaches Claude Opus 4.5"* |
| **CC-Bench-V2** (frontend/backend/long-horizon) | — | — | GLM-5 *"narrows the gap to Claude Opus 4.5"* |

The honest read: GLM-5.2 is a **near-frontier coding model that trails Claude Opus 4.8 on the headline coding bench (81.0 vs 85.0)** but closes much of the gap — and explicitly positions itself *against Claude* on agentic/coding/long-horizon work. For a vault whose goal is mastering Claude + autonomous agents, that competitive positioning is the relevant signal: it maps where Claude sits relative to the strongest open-weights challenger.

---

## 5. How you'd actually use it (the goal-relevant path)

1. **As a Claude Code / agent backend** — Z.ai exposes an OpenAI-compatible API; you can route a coding agent at GLM-5 instead of (or alongside) Claude. This is the **cc-switch v73** move; GLM-5 is a concrete, strong target for it.
2. **Self-hosted** — download weights from HF/ModelScope, serve with SGLang/vLLM. 744B (40B active) is heavy but the DSA/IndexShare work is specifically about making the 1M-context deployment affordable.
3. **As a cost/quality reference point** — on the **claude-api-cost-optimization** thread, an open-weights near-frontier model is the natural "what does the cheaper alternative cost/score" anchor.

---

## 6. Honest scoping — why MODERATE, not STRONG, and why OFF-GOAL is defensible

The operator directed this build to **argue (b) MODERATE → GOAL-ALIGNED**. Here is the case and the flagged stretches:

**The MODERATE case:** (1) GLM-5 is explicitly an *agentic-coding* model — the engine class of "autonomous agents for software development." (2) It is directly routable as a Claude Code backend (cc-switch v73 lineage; OpenAI-compatible). (3) It benchmarks *against Claude*, so it maps the competitive landscape the goal lives in. Per routine §31, (b) MODERATE+ keys the tier to **GOAL-ALIGNED**.

**The flagged stretches (where this is a reach):**
- **It is not Claude.** Goal #1 centers *Claude* specifically; a rival base model is adjacent, not core.
- **It is a raw model, not applicable tooling/methodology.** The operator cannot "use" GLM-5 the way they use a skill, an MCP server, or a pattern — there is nothing to pilot into the vault except "swap the backend."
- **The corpus substrate is tools-around-Claude, not competitor model weights.** Every prior model-adjacent subject entered via a *tool* (DeepSeek-TUI v72 / cc-switch v73 / LLMs-from-scratch v74). GLM-5 as a *frontier-LLM-subject* is at the edge of scope.

**Therefore the stricter, equally-defensible reading is `(b) FAIL → OFF-GOAL CAPTURE`** (a competitor model captured as corpus knowledge, not goal-aligned substrate). I am recording GOAL-ALIGNED **per operator direction**, with OFF-GOAL logged as the operator-reviewable alternative. Either way it is INCLUDE; the only thing that changes is whether the streak counts it goal-aligned.

---

## 7. Pattern outcome — NO mint (anti-inflation)

- **NO new top-level pattern** (max stays #85).
- **NO new §C Library-vocab standalone.** A single goal-adjacent frontier model does not warrant a minted capability class; the §C vocab is tool/capability-shaped, and competitor models have only ever appeared as *backends referenced by tools*. Minting here is exactly the inflation the routine fights (§28 clustering-first / count-discipline). **Counts UNCHANGED 46/10.**
- **Recorded as a corpus-knowledge data-point** (competitive-landscape / substrate-alternative reference) + an **audit-deferred tier-taxonomy question**: *the corpus has no "model / inference substrate" tier* — GLM-5 is plausibly the **first frontier general-purpose / agentic-coding LLM catalogued as the primary subject** (NOT the first model-subject — fish-speech, a TTS model, preceded it; the distinction is "frontier general-purpose LLM"). Whether that warrants a new tier category is flagged for the (already overdue) audit, **not minted now**.

**Secondary cross-references (NOT minted):**
- **cc-switch v73** — GLM-5 is a concrete, strong target for the "route Claude Code to an alternative provider" move (Z.ai / OpenAI-compatible).
- **DeepSeek-TUI v72** — sibling Chinese-lab frontier-model ecosystem (that subject's *tool* wraps DeepSeek V4 models; GLM-5 is the model itself).
- **Pattern #19 19a institutional-org portfolio data-point** — Zhipu AI / `zai-org` = another major Chinese AI lab subject, alongside OpenBMB v175 and ByteDance v143.
- **claude-api-cost-optimization thread** — open-weights near-frontier model as the cost/quality anchor.
- **LV-C2 / data-access economics adjacency** — open-weights + self-hostable is an inference-economics data-point (adjacent, not a member).

**Non-claims:**
- **NOT Pattern #52** (viral velocity) — 4.9k★ / 509 forks / 0 releases are **page-stated, NOT API-verified** (§37.4 mocks the GitHub API) → velocity unestablishable.
- **NOT Pattern #57** (corpus-recursive) — benchmarking *against* Claude Opus is a competitive comparison, **not** an influence-citation of a corpus subject.
- **NOT a coding agent/framework (T1)** — it is the *model*, not an agent built on one (the DeepSeek-TUI v72 distinction).

---

## 8. Provenance & verification (§37)

- **Facts** verified by 2× WebFetch (the rendered repo page + the raw README) on 2026-06-21.
- **Page-stated, NOT API-verified (§37.4):** 4.9k★ / 509 forks / 0 releases; **License: Apache-2.0** per the repo-page sidebar (the README does not restate it — treat as page-stated, not independently reconfirmed); primary language not prominently stated (model-card/deployment-hub repo). **No API-verified creation date → velocity unestablishable → explicitly NOT a #52 claim.**
- **Benchmark + architecture figures** are **Zhipu's own published numbers** (vendor-stated, not independently replicated).
- **Author identity:** `zai-org` = **Zhipu AI** (the Z.ai API platform org) — a major Chinese frontier-model lab; declared, not inferred.
- **Build method:** verdict produced **inline** (not the multi-agent workflow — per the `feedback_wiki_verify_independently_check_collisions` memory, that workflow has confabulated corpus facts; independent verification is load-bearing and was done by hand: collision grep over `_state/`+`_patterns/` corrected an over-claim — "first model-subject" → "first *frontier-LLM*-subject," since fish-speech preceded as a TTS-model subject).
