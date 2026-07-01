# (C) DeepSpec / DSpark — Pilot Methods Menu (v186)

> **Prefix `(C)` = Claude-generated.** Companion to `(C) DeepSpec — Deep Dive + Verdict.md`.
> **Read this first — the blunt truth:** DeepSpec is a **knowledge** subject, not a "install-it-into-your-Claude-workflow" subject. Its released draft-model checkpoints only accelerate **open-weight** models (Qwen3 / Gemma4). **Claude is closed-weight — you cannot swap a draft model into it**, and there is no user-facing speculative-decoding lever on the Claude API. So the *best* way to "apply" this is (1) **conceptually** — it makes you a smarter operator of the tools you already pay for — and (2) a **conditional self-host path** if you ever run an open model yourself. Full production DSpark isn't even reproducible from the open repo (the hardware-aware scheduler / Algorithm 1 isn't in it — see §4 of the Deep Dive).
>
> **The honest top-3:** **A1** (read the paper as an inference-cost primer) → **A4/B6** (map the levers onto your live `claude-api-cost-optimization` thread — the only truly on-goal application) → **C12** (free, no-GPU hand-trace to *feel* the mechanism). Everything with a GPU is optional curiosity; everything that trains is heavy and only makes sense if you self-host.

Each method is tagged **[effort]** / **[cost/risk]** / **what it proves**.

---

## Group A — Zero-cost conceptual (read-only; the real value)

**A1. Read the DSpark paper as an "how LLM inference gets fast" primer.** [30–45 min] [free] — Internalize the mental model **L = (T_draft + T_verify)/τ** and the three levers (draft cheaper / draft better / verify smarter). *Proves:* you now understand what every "2–3× faster inference" claim (Groq, Together, Fireworks, vLLM, DeepSeek V4) is actually doing. This is the single highest-ROI action.

**A2. Add a "speculative decoding / inference acceleration" concept note to the vault.** [30 min] [free] — One page under `00 Notes/` (or as an `05 Skills/` reference), cross-linking GLM-5 v176, DeepSeek-TUI v72, LLMs-from-scratch v74. *Proves:* the vault now has a substrate-layer reference it was missing (fills the gap this ship's (d)-cluster exposed).

**A3. Write the "three latency levers → decisions I actually make" one-pager.** [20 min] [free] — Map *draft cheaper / draft better / verify smarter* onto the choices you control: **model tier** (Opus 4.8 vs Sonnet 4.6 vs Haiku 4.5), **prompt caching**, **Batch API**, **Fast Mode**. *Proves:* turns theory into a decision checklist.

**A4. Map DSpark's ideas onto the `claude-api-cost-optimization` pilot thread. ⭐** [45 min] [free] — The load-bearing on-goal application. You can't do spec-decoding on Claude, but the *analogy* is exact:
  - "cheaper verify" ↔ **prompt caching** (cached reads ≈ 0.1× input price; ~90% savings on the cached prefix) + **Batch API** (50% off, non-latency-sensitive).
  - "faster generation" ↔ **Fast Mode** (Opus 4.8/4.7, up to ~2.5× output tok/s, premium price) — the closest user-facing lever to what a draft model buys.
  - "confidence-scheduled verification" ↔ *only spend expensive compute where payoff is likely* — the same logic as routing cheap tasks to Haiku and hard ones to Opus.
  *Proves:* concrete cost levers for hireui's future LLM features. (Model IDs/pricing/caching facts sourced from the `claude-api` reference.)

---

## Group B — Cost/latency-thread application (Claude-side, honest)

**B5. Audit hireui's LLM-integration spec for the levers you CAN pull.** [1–2 h] [free] — hireui has **no LLM yet** (`project_hireui_no_llm_yet`), so bake the levers in at design time: caching for repeated prompts (resume schema, JD templates), Batch API for bulk candidate scoring, tier-routing (Haiku for classification, Opus for reasoning). *Proves:* Goal #2 — a cost-right build-it spec, informed by *why* inference is expensive.

**B6. Borrow DSpark's benchmark honesty into the vault's `evals/` harness. ⭐** [1 h] [free] — DSpark's README says *"align your setup with the training settings or the comparison is not meaningful,"* and the paper reports **position-wise** conditional acceptance, not just a headline average. Port that discipline: every eval states its exact setup + reports a distribution, not one number. *Proves:* strengthens the prompt-evaluation pilot thread + the routine's §37 fact-provenance rules.

**B7. Build a tiny "tok/s + $/1M" cost model for coding-agent backends.** [1 h] [free] — A spreadsheet/notebook comparing Claude (Opus/Sonnet/Haiku, with/without caching) vs an open model + speculative decoding (2–6× cheaper *self-hosted* inference). *Proves:* a data-driven input to the **cc-switch v73** backend-routing decision (when is a self-hosted open model + spec-decoding actually cheaper than the Claude API for a given task?).

**B8. Adopt "confidence-scheduled verification" as an anti-inflation analogy.** [20 min] [free] — DSpark verifies only high-survival tokens and prunes the rest; the routine's `inflation_check` mints only high-confidence patterns and prunes the rest. Same shape. *Proves:* a clean articulation of the vault's own discipline (meta-methodology borrow).

---

## Group C — Hands-on local experiment (rented GPU; learning-only, NOT production)

> These need a cloud GPU (~1–2 h rental, a few $). None touch your machine or Claude. **install-snapshot + npm/pip hygiene not needed** (remote box), but pin the commit (`afdfa7c`) and use a throwaway instance.

**C9. Run DeepSpec's EVAL with a *released* checkpoint (no training).** [2–3 h] [~$5–15 GPU] — On a rented single GPU, `bash scripts/eval/eval.sh` pointing `draft_name_or_path` at e.g. `deepseek-ai/eagle3_qwen3_4b_ttt7` and `target_name_or_path` at `Qwen/Qwen3-4B`. *Proves:* you *see* accepted-length τ per benchmark — the abstraction becomes a number.

**C10. Serve Qwen3-4B + a draft via SGLang and measure the speedup.** [2–3 h] [~$10–20 GPU] — `python -m sglang.launch_server --model Qwen/Qwen3-4B --speculative-algorithm EAGLE3 --speculative-draft-model-path <hf-checkpoint> --speculative-num-steps 3 ...`, then benchmark tok/s vs no-draft. *Proves:* the real-world 2–6× latency win, felt end-to-end. (SGLang/vLLM are the standard consumers of these checkpoints.)

**C11. Compare DSpark vs DFlash vs Eagle3 on one benchmark.** [3 h] [~$15 GPU] — Reproduce a slice of the paper's Table 1 on Qwen3-4B. *Proves:* the parallel-vs-autoregressive-vs-semi-autoregressive tradeoff, empirically — the core insight of the paper.

**C12. Hand-trace one decoding round on paper (NO GPU). ⭐** [30 min] [free] — Read `markov_head.py` + `draft_ops.py` + paper Fig. 1 and trace: anchor D → parallel backbone → base logits → Markov head adds bias → sample E,F,G,H → confidence prunes H → target verifies E✓ F✓ G✗ → bonus G*. *Proves:* you understand the mechanism at the tensor level, for free — the best cost/insight ratio in Group C.

---

## Group D — Conditional self-host path (ONLY if you ever run an open model)

> This is where DeepSpec's checkpoints become *directly* usable — but only when you self-host an open-weight LLM. Fences: MIT (safe) but heavy; verify the target-model license (Qwen3/Gemma4 have their own terms); pin `afdfa7c`.

**D13. Cheap self-hosted feature for hireui.** [days] [infra $] — If hireui ever needs a bulk, latency-tolerant, cost-sensitive LLM feature (resume parsing, JD↔candidate matching at scale) where Claude-API cost doesn't pencil out, serve **Qwen3 + a released DSpark/EAGLE3 draft** via SGLang/vLLM for **2–6× cheaper** inference. DeepSpec's checkpoints are the drop-in accelerator. *Proves:* a concrete Goal-#2 cost path — but only if/when self-hosting is on the table.

**D14. Speed up a local open coding-agent.** [1 day] [GPU] — For a self-hosted open backend behind **cc-switch v73** (or DeepSeek-TUI v72's DeepSeek-V4 target), enable speculative decoding to cut latency. *Proves:* the "make my local agent faster" lever.

**D15. Fine-tune a domain draft model (the full, heaviest path).** [weeks] [8 GPU + ≥38 TB] — The README explicitly recommends re-fine-tuning the draft for domain-specific use. This is the complete DeepSpec training pipeline (data-gen via SGLang → 38 TB target cache → FSDP training). *Proves:* end-to-end mastery — but this is a research-scale commitment, **not recommended** unless self-hosting at scale is a real goal.

---

## Group E — Vault-methodology borrows (meta)

**E16. Borrow "semi-autoregressive" as an orchestration analogy. ⭐** [20 min] [free] — DSpark = heavy **parallel backbone** + **lightweight sequential correction head**. That is *exactly* this vault's own ship shape: a **read-only fan-out workflow** (parallel backbone) + an **inline hand-verified verdict** (sequential correction). Document the parallel in the routine notes. *Proves:* a crisp mental model for why the vault's build pattern works.

**E17. Fold "align your setup or the comparison is meaningless" into §37.** [15 min] [free] — Add DSpark's caveat as a named exemplar in the routine's benchmark-provenance / #52-velocity rules. *Proves:* reinforces the fact-provenance discipline with an external authority.

**E18. Add DeepSpec to the "understand the substrate" reading list.** [5 min] [free] — Alongside LLMs-from-scratch v74, as the canonical *inference-acceleration* reference (v74 covers *training* the model; DeepSpec covers *serving* it fast). *Proves:* completes the substrate-literacy pair.

---

## Group F — Corpus / wiki maintenance (the meta-pilot)

**F19. File the "model / inference-substrate" tier question for the next audit.** [10 min] [free] — Now **N=2** (GLM-5 v176 frontier-model + DeepSpec inference-accel-framework). Decide at audit whether to create the tier or keep deferring. *Proves:* keeps the anti-inflation bookkeeping honest.

**F20. Cross-link the DeepSeek cluster.** [15 min] [free] — A reference note tying DeepSeek-TUI v72 / GLM-5 v176 (Zhipu, adjacent) / DeepSpec v186 into a "Chinese-frontier-lab / model-substrate" map. *Proves:* the corpus's competitive-landscape picture is navigable.

---

## Recommended ladder

1. **A1** — read the paper (30–45 min, free). Non-negotiable; everything else builds on it.
2. **A4 + B6** — map the levers onto the live cost-optimization thread + borrow the benchmark honesty (free, on-goal, Goal-#2-relevant).
3. **C12 + E16** — free hand-trace + the orchestration-analogy borrow (feel the mechanism; sharpen the vault's own method).
4. **B5 / B7** — bake the levers into hireui's future LLM spec + build the cost model (Goal #2, still free).
5. *(Optional, if curious)* **C9 → C10** — rent a GPU, see τ, measure the speedup.
6. *(Only if self-hosting)* **D13** — the one path where the checkpoints become directly useful.

**What NOT to do:** don't try to "apply DeepSpec to Claude" (impossible — closed weights, no user-facing lever); don't run D15 (38 TB training) as a learning exercise; don't cite DSpark's 60–85% online numbers as verified (they're DeepSeek's own, unreplicated).

**PILOT lever status:** the standing vault PILOT lever (zero of the recent read-only candidates piloted — SkillSpector v169 → claude-tap v173 → Agent-Reach v174 → codebase-memory-mcp v172 → devspace v171 ladder) is **unaffected** — DeepSpec is not a pilotable agent tool, it's substrate knowledge. If you want a *pilotable* on-goal action this session, the strongest is still **agent-skills v184 M1→M9** (free Claude-Code plugin, five operator threads) or the read-only ladder above. DeepSpec's contribution is making you smarter about *why* those tools cost what they cost.
