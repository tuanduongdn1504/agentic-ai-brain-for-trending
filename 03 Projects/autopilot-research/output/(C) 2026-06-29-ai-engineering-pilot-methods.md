# Chip Huyen's *AI Engineering*: Ranked Pilot Methods for Storm Bear

> **Source:** Anas Riad — "AI Engineering in 41 Minutes: From Demo to Production" ([geQqpO_AFMo](https://www.youtube.com/watch?v=geQqpO_AFMo), 2026-06-17, 41:54, 17.4K views), a chapter-walkthrough of the **original**: Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, Dec 2024, 534pp, 10 chapters; repo [chiphuyen/aie-book](https://github.com/chiphuyen/aie-book) 16.3K★).
> **Date:** 2026-06-29. **Operator:** Storm Bear (Karpathy LLM-Wiki maintainer ×2 vaults + `~/.claude` memory + Scrum coach + **hireui/TalentAxis = Goal #2**).
> **Verification:** deep-dive + adversarial Workflow `wf_508f1c32-b7b` (15 agents) + primary-source fetch of Huyen's chapter-summaries/ToC. Ledger: [source-provenance](../wiki/ai-engineering/source-provenance.md). Companion wiki: [ai-engineering](../wiki/ai-engineering/_index.md) (11 files).

---

## Headline Insight

**This is the bullseye topic for Goal #2 — and the timing is perfect.** The book's entire thesis is *demo → production*. **hireui has zero LLM integration today** (verified) — which means its first AI feature isn't a retrofit, it's a **clean demo→production project you can do *by the book*, literally.** Most "add AI" attempts die as demos because teams do the fun 60% (a clever prompt, maybe RAG) and skip the boring 40% that the video *also* skips: **evaluation pipelines, guardrails + PII handling, cost/latency, monitoring, feedback loops** (Ch.3–4, 9–10).

So the value to you is **a build-it-right blueprint that slots straight onto threads you're already running.** The book is the conceptual parent of four of your existing pilots: [[prompt-evaluation]] *is* Ch.3–4 operationalized; [[claude-api-cost-optimization]] *is* Ch.9 + Ch.10-router/cache at the app layer; [[cowork-third-party-inference]] *is* Ch.4 host-vs-API for candidate PII; [[multi-agent-orchestration]] *is* Ch.6 agents. **You don't need new tooling — you need to sequence the disciplines you already have around one real hireui feature, eval-first.**

The single highest-leverage move (A1 below): **before writing a line of hireui LLM code, run the Ch.3–4 eval-first step** — define success criteria + build a small private eval set from real recruitment examples — and **design the Ch.10 5-layer architecture as the spec.** That converts "we want an AI screening feature" from a demo into an engineered system, and it's the missing measurement that turns your "N pilots / 0 deployed" into actual Goal #2 evidence.

Two cautions before you spend a minute: **don't fine-tune** anything for a first feature (Ch.7: prompt+RAG win; "getting data for finetuning is hard"), and **the video is a third-party summary, not gospel** — for evaluation, cost, and architecture, read the book chapters (free summaries in the repo), not the 41 minutes.

---

## ▶ Start Here (3-Step Sequence)

1. **Week 1 — Pick ONE hireui AI feature and write its eval *first* (A1 + A2).** Choose the smallest real one (e.g. "rank candidates against a job description" or "summarize a CV into a structured profile"). Before any prompt: write the **success criteria** (Ch.4: quality, safety, cost, latency) and **10–30 graded examples from real recruitment data** into your existing `evals/` harness. **Measure:** you have a private eval set + a baseline score *before* building — the thing 90% of teams never do.

2. **Week 2 — Build the feature prompt→RAG, run it through the eval, and add the two non-negotiable guardrails (A3 + A5).** Prompt-engineer it (Ch.5 5-part anatomy), add RAG over your job/candidate corpus only if it needs facts it lacks (Ch.6), and add **PII guardrails + output validation** (Ch.5/Ch.10-step2). Run every version through the Week-1 eval. **Measure:** score trend across prompt versions; zero PII leaks in output checks; mergeable PR under hireui I-2/BMAD.

3. **Week 3 — Make it productiony: cost + observability + a feedback hook (A4 + A7 + A8).** Add prompt caching + a cheap/strong model split (Ch.10 steps 3–4, composes with [[claude-api-cost-optimization]]), wire `ccusage`/OTel observability ([[claude-code-observability]]), and design one **feedback capture** (recruiter thumbs-up/down on a ranking) per Ch.10. **Measure:** cost-per-call, cache-hit-rate, and a feedback signal you can fold back into the eval set. *This is the demo→production arc, evidenced.*

---

## Ranked Methods Table

| Rank | Method | Flow | Effort | Value | First Step | Success Signal |
|------|--------|------|--------|-------|-----------|-----------------|
| 1 | **Eval-first: define success criteria + private eval set BEFORE building hireui's first AI feature** | A | Med | ⭐High | Write Ch.4 criteria (quality/safety/cost/latency) + 10–30 graded real examples into `evals/` | A baseline score exists before any prompt is written |
| 2 | **Design the Ch.10 5-layer architecture as the hireui build spec** | A | Med | ⭐High | Sketch context→guardrails→router→caches→agents for the feature; put in BMAD `_bmad-output/` | A reviewed spec that names every production layer, not a notebook demo |
| 3 | **Prompt→RAG (NOT finetune) for the first feature** | A | Med | High | Build with Ch.5 prompt anatomy; add RAG over job/candidate corpus only if needed | Feature works on prompt+RAG; finetuning consciously deferred |
| 4 | **PII guardrails + output validation on candidate data** | A | Med | ⭐High | Add input/output checks + schema validation (Ch.5/Ch.10-step2) on the PII path | 0 PII leaks in output checks; injection-resistant; feeds CONSTITUTION |
| 5 | **AI-as-judge to grade candidate-screening output** | A/B | Med | High | Build a rubric judge (reasoning-before-score) for ranking quality; reuse `evals/` | Judge scores correlate with recruiter judgment on a held-out set |
| 6 | **Formalize the vault's adversarial-verify workflows as Ch.3 AI-as-judge** | B | Low | High | Document judge selection + the bias/limitations checklist into the routine | Verify workflows cite Ch.3 limits; fewer confabulation slips |
| 7 | **Host-vs-API 7-factor decision for candidate PII (BYOM/sovereignty)** | A | Med | High | Run Ch.4's 7 factors (privacy/lineage/perf/functionality/control/cost/compliance) | A documented model-hosting decision; ties to [[cowork-third-party-inference]] |
| 8 | **Cost layer: prompt caching + cheap/strong model router (Ch.9 + Ch.10 step3–4)** | A | Med | High | Add caching + Sonnet-default/Opus-advisor split; measure with `ccusage` | Cost-per-call + cache-hit-rate measured; composes w/ [[claude-api-cost-optimization]] |
| 9 | **Observability from day 1 on the hireui feature** | A | Low | High | Wire OTel/JSONL + a quality/cost/latency panel ([[claude-code-observability]]) | Live cost+latency+error panel before launch, not after |
| 10 | **Feedback flywheel: design one feedback capture (Ch.10)** | A | Low | High | Add recruiter thumbs/edit capture; route signals into the eval set | Feedback signal collected + folded back into eval cases |
| 11 | **Treat the wiki as a RAG system; apply Ch.6 retrieval-optimization** | B | Low | Med | Audit `_master-index`→topic→article retrieval; add metadata/cross-link "re-ranking" | Faster, more precise drill-down; fewer missed cross-links |
| 12 | **Dataset engineering (Ch.8) = your source-ingestion discipline** | B | Low | Med | Map curation>volume + dedupe/clean/filter onto `raw/_inventory.md` coverage rules | Ingestion rubric cites Ch.8; no low-quality sources compiled |
| 13 | **Hallucination guards (Ch.2) for the confabulation problem you hit** | B | Low | High | Add "if unsure, say so + cite source" + grounding checks to the verify step | Fewer invented collisions/facts in wiki ships (your known failure mode) |
| 14 | **Eval pipeline (Ch.4) to grade wiki/Storm-Bear ship quality** | B | Med | Med | Score each ship on a rubric (coverage, citation, cross-link, confabulation) | A per-ship quality number you can trend |
| 15 | **Model-selection discipline: build a private eval set, ignore leaderboards** | C | Low | High | For your own Claude/Codex/Kimi choices, benchmark on `evals/`, not Arena | Model picks justified by your data (composes w/ [[omnilogin-ai-coding]] bake-off) |
| 16 | **Read the book as a structured plan using the free chapter summaries** | C | Low | High | Read repo `chapter-summaries.md`; deep-read Ch.3,4,10 (the skipped/production half) | Ch.3/4/10 read; gaps the video left are closed |
| 17 | **Sampling discipline for reproducible evals (Ch.2)** | C | Low | Med | Pin temperature + document temp-0≠determinism in `evals/` runs | Eval runs are as reproducible as the API allows; variance understood |
| 18 | **Order-of-operations as a personal/team decision checklist** | C/D | Low | Med | Adopt prompt→RAG→agents→finetune as the default escalation ladder | Every AI task starts at the cheapest lever; finetune is justified, not reflexive |
| 19 | **Teach the AI-engineering lifecycle + demo≠production gap (Scrum)** | D | Low | High | Run a workshop on the 7-step lifecycle + the demo-vs-prod table | Team can name the production gaps a demo hides |
| 20 | **"Eval-first" as a Definition of Done for AI features** | D | Low | High | Add "has success criteria + eval set + guardrails" to DoD for AI stories | No AI story is "done" without an eval — eliminates demo-ware |
| 21 | **AI-engineering-vs-ML-engineering framing for stakeholders** | D | Low | Med | Use the distinction to set expectations (adapt models ≠ train models) | Stakeholders stop asking to "train our own model" reflexively |

---

## Detailed Methods by Flow

### **Flow A — hireui Goal #2 (the bullseye: a real demo→production project)**

> Execute hireui-rooted (GitNexus + Figma MCP + I-8 operator-installs + I-2 agent-* branch + BMAD + `.pilot-log`). hireui has **no LLM yet** → this is a *build-it-right spec*, not a retrofit (see [[claude-api-cost-optimization]] note).

**A1. Eval-first — define success criteria + a private eval set before you build.** The book's #1 lesson (Ch.4, verbatim): *"Not having a reliable evaluation pipeline is one of the biggest blockers to AI adoption."* Pick the smallest real feature (candidate↔job ranking, or CV→structured-profile). Before any prompt: write success criteria across **quality / safety / cost / latency** and capture **10–30 graded examples from real recruitment data** into your `evals/` harness (the A1 anchor gate you already shipped — don't rebuild it). **Success:** a baseline score exists *before* a prompt is written. *This is the move that converts Goal #2 from vibes to evidence.*

**A2. Design the Ch.10 5-layer architecture as the build spec.** Sketch the production system before coding: **(1) Enhance Context** (RAG over jobs/candidates) → **(2) Guardrails** (PII + injection + schema) → **(3) Model Router/Gateway** (cheap model default, strong on hard cases; centralize keys/limits/fallbacks) → **(4) Caches** (prompt cache for repeated job descriptions) → **(5) Agent patterns** (only if multi-step). Drop it in `hireui/_bmad-output/`. **Success:** a reviewed spec that names every production layer — not a one-off notebook.

**A3. Prompt → RAG, NOT finetune.** Build with the Ch.5 5-part prompt (role/task/context/examples/output-format) and add RAG (Ch.6) only when the model needs facts it lacks (your job DB, candidate records). **Do not finetune** — Ch.7 is explicit that prompt+RAG should be exhausted first and "getting data for finetuning is hard." **Success:** the feature works on prompt+RAG; finetuning is a documented, deferred decision.

**A4. Cost layer — caching + model routing.** Apply Ch.9/Ch.10: **prompt caching** (repeated system prompt + job descriptions bill ~0.1× on hits), and a **Sonnet-default / Opus-advisor** split for hard cases. This is your [[claude-api-cost-optimization]] pilot, now with a real workload. **Success:** cost-per-call + cache-hit-rate measured via `ccusage` ([[claude-code-observability]]).

**A5. PII guardrails + output validation.** Candidate data is sensitive. Add Ch.5/Ch.10-step2 guardrails: input checks, **treat retrieved candidate content as untrusted** (injection surface), schema-validate outputs, and an escalation/human-review path for low-confidence rankings. **Success:** zero PII leaks in output checks; a findings list that feeds the hireui CONSTITUTION. (Pair with the G-Stack `/cso` audit from [[claude-code-skills-stack]].)

**A6. AI-as-judge to grade screening quality.** Build a rubric judge (reasoning-before-score, per [[prompt-evaluation]]) that scores candidate-ranking output against recruiter expectations. Beware the Ch.3 judge biases. **Success:** judge scores correlate with recruiter judgment on a held-out set → you can iterate prompts against a number.

**A7. Host-vs-API 7-factor decision (data sovereignty).** Run Ch.4's seven factors (data privacy, lineage, performance, functionality, control, cost, compliance) on candidate PII. This is the formal version of the [[cowork-third-party-inference]] BYOM question. **Success:** a documented hosting decision (managed API vs gateway+local) defensible to a future customer's security review.

**A8. Observability + feedback flywheel from day 1.** Wire OTel/JSONL + a quality/cost/latency panel ([[claude-code-observability]]); design **one** Ch.10 feedback capture (recruiter thumbs/edit on a ranking) and route it back into the A1 eval set. **Success:** a live panel before launch + a feedback signal that grows your eval set (the data flywheel).

---

### **Flow B — autopilot-research + Storm Bear Vaults (the wiki *is* an AI system)**

**B1. Formalize your adversarial-verify workflows as Ch.3 "AI-as-judge."** Your verify workflows (this one included) *are* LLM-as-judge. Ch.3 names their limits — bias, inconsistency, model-specific preference, and *"scores need to be interpreted in the context of what judges are being used."* Document a judge-selection + limitations checklist into the routine. **Success:** verify steps cite Ch.3 limits; fewer confabulation slips (your known failure — see your memory note on invented collisions).

**B2. Hallucination guards (Ch.2) for the confabulation problem.** The book's hallucination causes (knowledge gap, probabilistic pattern-completion, weak grounding) describe exactly the failure where a lens invented a "v142 collision." Add explicit grounding + "if unsure, say so + cite" to the verify lens prompts. **Success:** measurably fewer fabricated corpus facts in ships.

**B3. Dataset engineering (Ch.8) = source-ingestion discipline.** "Quality > quantity", diversity, dedupe/clean/filter — map onto `raw/_inventory.md` coverage rules. Treat compiling a source into the wiki like adding to a training set: curate, don't dump. **Success:** an ingestion rubric citing Ch.8; low-quality sources rejected at intake.

**B4. RAG retrieval-optimization (Ch.6) for the wiki itself.** The wiki is a hand-curated RAG (retrieve via `_master-index`→topic→article → synthesize → answer). Apply re-ranking (cross-link density), metadata (front-matter), and query-rewriting thinking to your `query:` verb. **Success:** faster, more precise drill-down; fewer missed cross-links. (Sibling to [[claude-code-memory-systems]] L5 + [[graphify-codebase-graph]].)

**B5. Eval pipeline (Ch.4) to grade ship quality.** Score each wiki/Storm-Bear ship on a rubric (coverage, citation discipline, cross-link integrity, confabulation rate). **Success:** a per-ship quality number you can trend across topics — a feedback loop on your *own* knowledge work.

---

### **Flow C — Personal Claude Code harness / prompt-eval pilot**

**C1. Read the book as a structured plan (free chapter summaries).** Use the repo `chapter-summaries.md` + the [ai-engineering wiki](../wiki/ai-engineering/_index.md). **Deep-read the chapters the video skipped: Ch.3, Ch.4, Ch.10** — they're the production half and the ones most relevant to you. **Success:** the eval + architecture + feedback gaps closed.

**C2. Ch.3–4 deepen the prompt-eval pilot you're already running.** Your [[prompt-evaluation]] work *is* Ch.3–4 operationalized. Fold in the book's extras: comparative/ranking eval, the "evaluate every component" rule, and the 3-step pipeline-design method. **Success:** your eval discipline gains the conceptual scaffolding (and citations) it was missing.

**C3. Model-selection discipline (Ch.4) for your own model choices.** When choosing Claude vs Codex vs Kimi (see [[omnilogin-ai-coding]] bake-off), **build a private eval set and benchmark on your data — ignore leaderboards.** **Success:** model picks justified by *your* tasks, not Arena rank.

**C4. Sampling discipline (Ch.2) + the order-of-operations checklist.** Pin temperature for reproducible eval runs (and document temp-0≠determinism); adopt **prompt→RAG→agents→finetune** as your default escalation ladder for any AI task. **Success:** reproducible evals + every task starts at the cheapest lever.

---

### **Flow D — Scrum Coaching / Teaching Teams**

**D1. Teach the AI-engineering lifecycle + the demo≠production gap.** The 7-step lifecycle and the demo-vs-production table are a ready-made workshop. **Success:** the team can name the production gaps a demo hides (eval, guardrails, cost, monitoring, feedback).

**D2. "Eval-first" as a Definition of Done for AI features.** Add to your DoD: an AI story isn't "done" without **success criteria + an eval set + guardrails**. This is the single most effective anti-demo-ware policy. **Success:** no AI story ships as an unmeasured demo.

**D3. AI-engineering-vs-ML-engineering for stakeholder expectations.** Use the distinction (adapt foundation models ≠ train models from scratch) to stop the reflexive "let's train our own model" ask and set realistic scope. **Success:** stakeholders frame AI work as adaptation + evaluation, not a research project.

---

## What to Consciously SKIP (and Why)

- **Don't fine-tune for hireui's first feature.** Ch.7 is explicit: exhaust prompt + RAG first; "getting data for finetuning is hard." Revisit only if a *measured* eval shows a domain gap nothing cheaper closes.
- **Don't treat the 41-minute video as the source.** It's a faithful but partial third-party summary that **skips Ch.7–10** (the production half) and simplifies evaluation. For eval/cost/architecture, read the book chapters (free summaries in the repo). The creator (Anas Riad) is a credible educator, **not** Chip Huyen and not official O'Reilly content.
- **Don't cite `huyenchip.com/ai-engineering`** — it 404s. The companion is the **GitHub repo** + `huyenchip.com/books/` (see [source-provenance](../wiki/ai-engineering/source-provenance.md)).
- **Don't build a multi-agent system for the first feature.** Ch.6: don't default to agents — "the more automated the agent becomes, the more catastrophic its failures." Single-step RAG + a good prompt is the right first shape; agents come later (and then see [[multi-agent-orchestration]]).
- **Don't add new tooling reflexively.** Your existing pilots (`evals/`, cost-optimization, observability, cowork-3P) already implement Ch.3/4/9/10 at the app layer — *sequence them*, don't re-buy them.

---

## Critic's Reframe

The honest read: this topic adds **almost no new tools** to your stack — and that's the point. You've spent weeks accumulating the *components* of AI engineering as separate pilots (prompt-eval = Ch.3–4, cost-optimization = Ch.9/Ch.10, cowork-3P = Ch.4 hosting, multi-agent = Ch.6, memory/RAG = Ch.6). Chip Huyen's book is the **assembly diagram** that says how they compose into one production system and **in what order** (eval-first; prompt→RAG→agents→finetune; the 5-layer architecture). The video gave you the fun half and stopped exactly where the engineering starts.

For you specifically, the trap is the same one you've named yourself: **"N ranked pilots, 0 deployed."** This topic's job is to break that — not by adding pilot #N+1, but by giving you the **one sequence to actually ship a feature**: pick a small hireui AI feature, write its eval first, design the 5-layer spec, build prompt→RAG, add PII guardrails + caching + observability, capture feedback. That arc *is* demo→production, it touches five disciplines you already track, and it produces the Goal #2 evidence (a measured, shipped feature) you keep deferring. Everything else here — teaching it, applying Ch.8 to your ingestion, formalizing Ch.3 in your verify workflows — is high-value reinforcement of disciplines you already run. The book's gift is **order and completeness**, not novelty.

---

## Cross-Links to Sibling Wiki Topics

- **[prompt-evaluation](../wiki/prompt-evaluation/)** — Ch.3–4 operationalized (Anthropic grading course); your active pilot.
- **[claude-api-cost-optimization](../wiki/claude-api-cost-optimization/)** — Ch.9 + Ch.10 router/cache at the app layer (caching, advisor, context-eng).
- **[cowork-third-party-inference](../wiki/cowork-third-party-inference/)** — Ch.4 host-vs-API / BYOM for candidate-PII sovereignty.
- **[multi-agent-orchestration](../wiki/multi-agent-orchestration/)** — Ch.6 agents at system scale (the Anthropic agent originals); the job-screener ≈ a hireui feature.
- **[claude-code-memory-systems](../wiki/claude-code-memory-systems/)** — Ch.6 memory + RAG-as-memory; the Karpathy LLM-Wiki lineage (this vault).
- **[agentic-analytics-harness](../wiki/agentic-analytics-harness/)** — a real production foundation-model harness living these exact lessons (eval, error-recovery, observability).
- **[claude-code-observability](../wiki/claude-code-observability/)** — Ch.10 monitoring in practice (OTel/JSONL/`ccusage`).
- **[claude-code-skills-stack](../wiki/claude-code-skills-stack/)** — G-Stack `/cso` security audit pairs with A5 PII guardrails.
- **[omnilogin-ai-coding](../wiki/omnilogin-ai-coding/)** — Ch.4 model-selection bake-off (Kimi vs Claude on `evals/`).

---

## Suggested Next Action

**This week:** A1 — pick the smallest real hireui AI feature and **write its eval first** (success criteria + 10–30 graded real examples into `evals/`). **Report:** the criteria + the baseline score before any prompt exists.

**Week 2:** A2 + A3 + A5 — design the Ch.10 5-layer spec, build it prompt→RAG, add PII/output guardrails; run every version through the Week-1 eval. **Report:** score trend across versions + a clean PR under I-2/BMAD.

**Week 3:** A4 + A8 — caching + model routing + observability + one feedback capture. **Report:** cost-per-call, cache-hit-rate, and the first feedback signal folded back into the eval set.

**Decision to tee up:** after Week 3 you'll have hireui's **first shipped, measured, production-shaped AI feature** — the concrete Goal #2 evidence that converts "N pilots / 0 deployed" into "1 deployed, by the book." And a parallel low-effort win any time: read Ch.3, 4, 10 from the free repo summaries (C1) to close the gaps the video left.

---

**File prepared for Storm Bear's vault. The topic adds order + completeness, not new tools — the win is sequencing the disciplines you already track around one real hireui feature, eval-first.**
