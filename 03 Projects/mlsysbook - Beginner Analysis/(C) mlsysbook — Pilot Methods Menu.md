# (C) mlsysbook — Pilot Methods Menu (v197)

**24 ways to apply MLSysBook to your working flow.** Blunt framing: MLSysBook is a **knowledge subject** — the payoff is *mental models + a few borrowable disciplines*, not installable tooling. But it is unusually well-aimed at you: you're a **software engineer** about to ship **hireui's first LLM feature**, and you're a **Scrum coach who hires** — and this book's serving/eval/responsible-AI/**recruitment-bias** content lands straight on both. Everything here is free (CC-BY-NC-SA to read; MIT/Apache/AGPL components) and mostly **zero-install**.

**⭐ One-thing path: A1 → B7 → D14.** Read the 5-chapter "what an LLM feature really is" spine → steal the responsible-AI-for-hiring checklist into a hireui **fairness gate ADR** → build it into the CandidateDetail/Match-Explain feature on an `agent-*` branch. That's a real Goal-#2 artifact from a book, requiring nothing installed.

**Fence (applies throughout):** it's a textbook — the only "install" risks are the *optional* components. If you run TinyTorch/MLSys·im/labs: `install-snapshot` first + scratch venv/Codespaces. **Never** clone-and-build the whole repo (image/PDF-heavy — use the blobless clone or read online at mlsysbook.ai). SocratiQ + StaffML are AGPL/CC-BY-NC — read-only fine, don't productize into hireui. hireui work follows its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first); **hireui has no LLM spend yet → build-it-right, design-only, don't retrofit.**

---

## A — Read & learn (zero risk, highest knowledge ROI)

**A1. The "what an LLM feature really is" spine (~4–6 h).** Read, in order, Vol I: **Introduction → ML Systems → Model Serving → Benchmarking → Responsible Engineering**. This is the minimum to internalize: constraints-drive-architecture, the 5–95 rule, silent-failure/drift, Little's-Law headroom, Goodhart's-Law-in-benchmarks, and the fairness-Pareto-frontier. Everything else in this menu assumes this spine. *(The AI-For-Beginners v191 "A3 what-Claude-is-made-of spine" move, one systems-layer up.)*

**A2. Personal gap-map.** Skim the two volume tables of contents; mark each chapter Solid / Fuzzy / New. Your likely New: KV-cache serving physics, MFU/roofline, distributed-training MTBF, differential privacy, sustainability/carbon. Your likely Solid: MLOps principles, the SDLC framing. This tells you exactly what to read deeply for hireui.

**A3. The quantitative-laws flashcard set.** From the Deep Dive §2.2, make ~10 flashcards you can actually recall in a design meeting: Iron Law (`T=O/(R·η)`), memory wall (bit-movement 100–10⁶× compute), Amdahl ceiling, Adam 6× memory, **KV-cache ≈ 128 KB/token for Llama-3-8B → 16.8 GB at 128k**, INT8-only-4×-on-Tensor-Cores, Little's-Law-70%-headroom, serving-dominates-training-100–1000×. These are the napkin math that make you sound like a staff engineer.

**A4. Read the recruitment-bias case studies as a hireui pre-mortem.** Vol I Responsible Engineering + Vol II Responsible AI: the **Amazon "women's" résumé penalty**, **COMPAS calibration-vs-equalized-odds**, **Obermeyer cost-as-proxy**, and **proxy-variable entanglement** (ZIP / name / college / career gaps reconstruct protected attributes). Read them asking "which of these would hireui reproduce?" — this is the single most directly-relevant reading in the book for your product.

---

## B — Borrow disciplines into your own work (zero-install)

**B5. The D·A·M design checklist.** For every hireui LLM feature, write a one-pager splitting the design into **Data** (where it comes from, quality/freshness/consent), **Algorithm** (the frozen model + prompt), **Machine** (latency/memory/cost budget). Forces co-design instead of "pick a model, bolt it on." (This is how the whole book reasons.)

**B6. Constraint-propagation-backward rule.** Adopt as a team norm: **no LLM-feature ticket starts without its deployment constraints written first** (latency SLO, max output tokens, $/request ceiling, privacy tier). The book's "exponential cost escalation" is the argument — a constraint found at launch costs orders of magnitude more than one found at day 1. Bake it into your Definition-of-Ready. *(Composes with the system-thinking pilot's 3-golden-questions gate.)*

**B7. ⭐ The responsible-AI-for-hiring gate (highest Goal-#2 ROraw).** Convert the recruitment-bias content into a hireui **Fairness Gate spec** (an ADR): (1) never rely on removing protected attributes — proxies reconstruct them; (2) **disaggregated per-group outcome monitoring** is the only real defense; (3) pick your fairness metric explicitly (calibration vs. equalized-odds — you can't have both, COMPAS proves it); (4) budget the accuracy tax (~4pp) and document it. This is a *real hireui feature spec* derived from a textbook. *(Composes with the miai-cv-matching "assistive-not-decisional" + EU-AI-Act pins already in your memory.)*

**B8. The verify/gray-zone gate for LLM outputs.** Steal the StaffML/edge-chapter pattern: emit an LLM summary only if `confidence > 0.85`; **human-review if < 0.75**; log the 0.75–0.85 gray zone for audit. This is the book's answer to silent degradation — and it composes with your v189 loop-verifier + SkillSpector-class read-only gating.

---

## C — Scratch trials (low-risk, hands-on, off the critical path)

**C9. MLSys·im napkin-math trial.** `pip install` MLSys·im in a scratch venv (Apache-2.0) and reproduce the KV-cache-at-128k calc + a serving-cost estimate for *your* hireui traffic assumptions (1M requests/mo × $/1k-tokens). 30 minutes → a real cost number for the roadmap. *(The simulator is the safest, most directly-useful component.)*

**C10. Run one Lab.** Open Lab 00 (Marimo notebook, browser or Codespaces) — change a parameter, watch a trade-off break. Pick the serving or compression lab. Builds intuition the flashcards can't.

**C11. TinyTorch, one module.** In a scratch clone (MIT-licensed), do the first TinyTorch module (build a tensor/autograd primitive by hand). Don't do all 20 — one module is enough to make "the model is 5% of the system" viscerally true. Off-goal but genuinely clarifying if you've never built a framework internal.

**C12. Read SocratiQ's provider-fallback code as a reference implementation.** `socratiq/src_shadow/configs/env_configs.js` + `client.config.js` + `js/libs/agents/`. It's a working, production **8-provider fallback + keys-server-side-in-a-Cloudflare-Worker** design. Read it as a concrete answer to "how do I structure a vendor-agnostic LLM client without leaking keys" — pairs with your meetily-v196 vendor-seam study.

---

## D — hireui / Goal-#2 (the real payoff — per its CONSTITUTION)

**D13. Serving-cost + KV-cache budget for hireui's first LLM feature.** Before writing code: compute the KV-cache + weight memory for your chosen model (Haiku vs Sonnet), the per-request token budget, and the $/month at projected volume (the "serving dominates training 100–1000×" fact means this number, not training, is your economics). Put it in the feature's design doc as a hard SLO. *(Composes with the CC-observability/ccusage cost thread + the mosh vendor-seam.)*

**D14. ⭐ Build the Fairness Gate (B7) into CandidateDetail / Match-Explain.** On an `agent-*` branch, add: disaggregated eval on a labeled holdout (per candidate-background cluster + per hiring-manager cohort), a hard release gate (no protected-group quality drop > 2pp), and an ADR documenting the calibration-vs-equalized-odds choice. **This is the sharpest, most defensible Goal-#2 artifact in this whole ship** — a recruitment product implementing the book's recruitment-bias lessons. *(Composes with miai-cv-matching's recruiter-labeled evals + assistive-not-decisional framing.)*

**D15. Statistical telemetry from day one.** Instrument the LLM feature for **silent-drift** signals, not just errors: summary-length drift, latency p99, recruiter corrections/rejections, per-segment quality. The book's core operational lesson — traditional monitoring can't see accuracy degradation. Wire it into the prompt-eval harness you already have.

**D16. The vendor-seam + provider-fallback (SocratiQ + meetily pattern).** Design hireui's LLM client as: one OpenAI-compatible path + a Claude-specific shape + a local/cheap fallback (Haiku for cost, an open model for privacy-tier candidates). SocratiQ's Cloudflare-Worker-holds-keys design + meetily's `generate_summary()` = your two reference implementations. *(Directly advances the mosh-ai A2-seam thread.)*

---

## E — Personal & team (Scrum-coach leverage)

**E17. ⭐ StaffML as your own + your team's systems-fluency drill.** Use the StaffML vault (free, mlsysbook.ai/staffml) to drill the Cloud/Edge/Mobile/TinyML tracks. The **napkin-math + common-mistake** structure of each question is exactly the reasoning you want in design reviews. Do the "GPU Memory Hierarchy" chain (L1→L6, including the coding-agent memory-architecture question — your CC-memory thread).

**E18. Steal the StaffML question TEMPLATE for hireui's own technical-interview bank.** The `scenario → question → realistic_solution + common_mistake(Pitfall/Rationale/Consequence) + napkin_math(Assumptions/Calc/Conclusion)` + Bloom-level + competency-area taxonomy is a **reusable, physics-grounded assessment format**. Build a small hireui engineering-interview question set in this exact shape — a real recruitment-product asset. (Bloom L1-Recall → L6-Architect is a ready-made seniority rubric.)

**E19. A 3-session team "AI Engineering" literacy workshop.** Session 1: constraints-drive-architecture + the 5–95 rule + silent failure. Session 2: the quantitative laws (KV-cache, serving-cost-dominance, Little's-Law-headroom) with a live MLSys·im demo. Session 3: responsible-AI-for-hiring (the case studies + your Fairness Gate). Scrum-coach leverage: turns the whole team fluent in *why* the LLM feature is built the way it is.

**E20. The AI Engineering Blueprint as a hiring/leveling rubric.** Skim the Instructor Hub's competency framework + StaffML's Bloom-mapped mastery levels ("owns a task → owns a component → owns a system → owns the architecture → owns the org"). It's a ready-made **seniority ladder for ML-systems roles** — directly usable in hireui's own role definitions and in your Scrum-coaching of engineering growth.

---

## F — Vault-meta (compounding the knowledge base)

**F21. ⭐ Steal design-grammar's formalism into the Pattern Library.** MLSysBook's `design-grammar` (5 Roles × 8 Layers × **90 primitives with `composition_links` + rewrite-rules.yml**; loop = *"naive system + binding constraint → rewrite rule → feasible system"*) is a **near-exact mirror of this vault's own method**. Borrow: (1) the `composition_links` idea (make patterns explicitly compose), (2) the "primitive + constraint → rewrite" framing for Library-vocab entries, (3) the periodic-table visualization. This is the deepest vault cross-ref in the ship.

**F22. Adopt the AI-generated-corpus provenance trail.** StaffML questions carry `validation_model` / `math_model` / `human_reviewed:not-reviewed` fields — a machine-readable QA audit trail for AI-generated content. Consider a lightweight version for `(C)`-prefixed vault artifacts (which model wrote it, whether a human verified it) — reinforces the inflation-check discipline.

**F23. The "textbook as agent-maintained repo" data-point.** Log MLSysBook's `binder` CI (domain-specific validation: math consistency, notation, dead-code, percent-in-prose) + Claude/Codex worktree audit workflow as a #12 / agent-maintenance reference — a template for how the vault itself could gate its own consistency (e.g., a "shim-doesn't-exceed-N-tokens" check, given the standing shim-size flag).

**F24. The agent-code-context vs. ML-systems-knowledge synthesis.** File the observation: MLSysBook (v197) is the corpus's ML-systems-*knowledge* subject; it complements — doesn't overlap — the agent-*tooling* subjects. Its SocratiQ (embedded multi-agent tutor + provider-fallback) is a genuine agent-system data-point worth watching if a *standalone* embedded-AI-tutor subject recurs (DeepTutor v38 = the prior; a 3rd would be worth a mint review).

---

### Method ladder summary
- **Fastest value:** A1 (spine) → A3 (flashcards) → E17 (StaffML drill).
- **Sharpest Goal-#2:** A4 → B7 → **D14** (Fairness Gate in CandidateDetail) — a real hireui feature from a textbook.
- **Deepest vault payoff:** F21 (design-grammar → Pattern Library).
- **Team leverage:** E19 (workshop) + E20 (seniority rubric).
- **Zero-install throughout;** the only optional installs (MLSys·im C9, TinyTorch C11, Labs C10) are scratch-venv/Codespaces only.
