# (C) Phase-0.9 Verdict — v176 GLM-5 — GOAL-ALIGNED INCLUDE 3/4

**Subject:** `zai-org/GLM-5` (Zhipu AI) · **Date:** 2026-06-21 · **Routine:** LLM Wiki Routine v2.6
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4** — `(a) FAIL · (b) MODERATE · (c) STRONG · (d) STRONG`
**§31 tier-key:** (b) MODERATE+ → **GOAL-ALIGNED** (per operator direction). (a) does NOT key the tier.
**⚠️ Operator-directed scoping:** the operator chose "build it, argue (b) MODERATE." The stricter `(b) FAIL → OFF-GOAL CAPTURE` reading is equally defensible and is recorded as the operator-reviewable alternative (§ below).

---

## Criterion (a) — Storm Bear cultural-peer / identity axis → **FAIL (clean, no axis)**

- **Author = Zhipu AI** (`zai-org`, the Z.ai API-platform org) — a major Chinese frontier-model **corporate lab**.
- **Not Anthropic** → fails (a)-7 (Anthropic-only). A major commercial AI lab is not the *individual* cultural-peer axis.
- This is the **declared-non-Anthropic-institution** situation: matches **ByteDance v143**, **NVIDIA v169**, **Google v140**, and the immediately-prior **OpenBMB v175** (also a Chinese AI lab). A Chinese-origin/heritage inference is **NOT an (a)-rescue** (the v159→v175 discipline + standing recommendation (ii)).
- **Note (not a rescue):** logged as a Pattern #19 19a institutional-org portfolio data-point (Zhipu AI joins the corpus's Chinese-AI-lab set: OpenBMB v175 / ByteDance v143).

**Result: (a) FAILS, no axis minted.** Does not lower the tier — §31 keys on (b).

---

## Criterion (b) — goal-relevance → **MODERATE** (the tier-keying criterion; operator-directed)

Goal #1 = *"Master Claude and autonomous agents for software development."*

**The MODERATE case:**
1. GLM-5 is explicitly an **agentic-coding** model (*"From Vibe Coding to Agentic Engineering"*; hundreds of rounds / thousands of tool calls; 1M context) — the **engine class** of "autonomous agents for software development."
2. **Directly routable as a Claude Code / agent backend** (Z.ai OpenAI-compatible API) — the concrete **cc-switch v73** move.
3. **Benchmarks against Claude** (Terminal-Bench, Vending Bench, CC-Bench) — it maps the **competitive landscape** the goal lives in.

→ (b) MODERATE ⇒ GOAL-ALIGNED INCLUDE (§31 keys on (b) MODERATE+).

**⚠️ Flagged stretches (why this is a reach, and why OFF-GOAL is defensible):**
- It is **not Claude** — the goal centers Claude specifically; a rival base model is adjacent, not core.
- It is a **raw model, not applicable tooling/methodology** — nothing to pilot into the vault except "swap the backend."
- The **corpus substrate is tools-around-Claude, not competitor model weights** — every prior model-adjacent subject entered via a *tool* (DeepSeek-TUI v72 / cc-switch v73 / LLMs-from-scratch v74). A frontier-LLM-as-subject is at the edge of scope.

**→ The stricter reading `(b) FAIL → OFF-GOAL CAPTURE` (competitor model captured as corpus knowledge) is equally defensible.** Recorded GOAL-ALIGNED per operator direction; OFF-GOAL is the operator-reviewable alternative. §35 impact noted below for both readings.

---

## Criterion (c) — engineering substance → **STRONG** (in the model)

- Frontier-scale, architecturally novel **model**: 744B (40B active) MoE; **DeepSeek Sparse Attention**; **IndexShare** (−2.9× per-token FLOPs at 1M ctx); upgraded MTP speculative decoding (+20% acceptance); **slime** async RL infra; 28.5T-token pre-training; 1M context; `reasoning_effort` control; six deployment stacks.
- **Caveat:** the engineering weight lives in the *model*, not the *GitHub repo as an artifact* (the repo is a model card + deployment guides + tech-report pointer, minimal in-repo code). The *subject's* substance is unambiguous → STRONG.

---

## Criterion (d) — connectivity → **STRONG**

- **cc-switch v73** — a concrete, strong target for routing Claude Code to an alternative provider.
- **DeepSeek-TUI v72** — sibling Chinese-lab frontier-model ecosystem (tool wraps the model; GLM-5 is the model itself).
- **LLMs-from-scratch v74** — the "how an LLM works" educational counterpart to "a frontier LLM in the wild."
- **claude-api-cost-optimization thread** — open-weights near-frontier model as the cost/quality anchor.
- **Chinese-AI-lab cluster** — Zhipu AI alongside OpenBMB v175 / ByteDance v143 (#19 19a).
- **Competitive-landscape thread** — benchmarked vs Claude Opus 4.8 / 4.5.

---

## Pattern outcome — NO MINT (anti-inflation)

- **NO new top-level pattern** (max #85). **NO new §C standalone.** **Counts UNCHANGED 46/10; §C surface stays ≈33.**
- A single goal-adjacent frontier model does not warrant a minted capability class; §C vocab is tool/capability-shaped, and competitor models have only ever appeared as *backends referenced by tools*. Minting here = the inflation the routine fights (§28 clustering-first / count-discipline).
- **Recorded as a corpus-knowledge data-point** + an **audit-deferred tier-taxonomy question**: the corpus has no "model / inference substrate" tier; GLM-5 is plausibly the **first frontier general-purpose / agentic-coding LLM catalogued as the primary subject** (NOT the first model-subject — fish-speech, a TTS model, preceded; corrected from an initial over-claim via collision grep). Flagged for the overdue audit, NOT minted.

---

## Streak / ceiling / counts

- **Streak (v2.5 §32 forward-only):** GA:37 → **GA:38 · OG:11 [7 ov]** *(GOAL-ALIGNED per operator direction; NOT an override). If the operator elects the OFF-GOAL reading instead → `GA:37 · OG:12 [7 ov]`.*
- **§35 soft off-goal ceiling: CLEAR either way.** GA reading: window {v174 GA, v175 GA, **v176 GA**} = 0 OG. OFF-GOAL reading: window {v174 GA, v175 GA, **v176 OG**} = 1 OG ≤ 1 → still CLEAR (the v174/v175 GA pair gives headroom).
- **23 consecutive goal-aligned ships v153→v176** (under the GA reading).
- **Counts UNCHANGED: 46 confirmed patterns / 10 CONFIRMED Library-vocab.** §C surface stays ≈33 (no mint).

---

## Build method & verification (honest disclosure)

- **Verdict produced inline** (NOT the multi-agent workflow — the `feedback_wiki_verify_independently_check_collisions` memory documents that workflow confabulating corpus facts; independent verification is the load-bearing safeguard).
- **Independent verification performed:** 2× WebFetch (rendered repo page + raw README); collision grep over `_state/*.md` + `_patterns/*.md` for zhipu/GLM/Qwen/frontier-model/model-weights/fish-speech. The grep **corrected an over-claim**: GLM-5 is NOT the corpus's first *model-subject* (fish-speech, a TTS model, preceded it) — it is the first *frontier general-purpose LLM* subject.
- **inflation_check:** 0 mints, max top-level pattern stays #85, counts 46/10 unchanged, no §C surface change, no improper N-bumps.

---

## Honest non-claims

- (a) genuinely **FAILS** (Chinese corporate frontier-model lab, not Anthropic; no axis).
- (b) **MODERATE, operator-directed**; **OFF-GOAL is the defensible stricter reading**.
- **GOAL-ALIGNED per operator direction** (not an override; §35 clear under both readings).
- **NO mint** — not a new top-level pattern, not a new §C standalone.
- **NOT #52** (metrics page-stated, NOT API-verified; velocity unestablishable).
- **NOT #57** (benchmarks-vs-Claude = competition, not influence-citation).
- **NOT a coding agent/framework (T1)** — it is the model, not an agent built on one.
- Benchmark/architecture figures are **Zhipu's own published, unreplicated** numbers.
- **NO confirmed-count change (46/10).**
