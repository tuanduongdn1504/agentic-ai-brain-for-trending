# Pilot methods — applying prompt-evaluation / grading to your workflow

> **Source knowledge:** [[prompt-evaluation/_index]] (Anthropic "Building with the Claude API" → Prompt Evaluations → Lesson 17 "Grading with AI"), deep-dived + adversarially verified (Workflow `wf_dd6c7095-c76`, 16 agents).
> **The one idea to apply:** turn "is this output any good?" into an **objective signal** (a 1–10 score or correct/incorrect) by writing a **grader** — code where you can, model where you need judgment, human to calibrate. Then **average it and trend it.**
> **The one technique that makes model graders work:** make the judge emit **reasoning + strengths/weaknesses BEFORE the score** (else you get clustered 6s).
> **Three surfaces in your flow this applies to:** (1) the **knowledge pipeline** (autopilot + Storm Bear wiki quality), (2) **hireui** real software (eval-first for its first AI feature), (3) **Claude Code skills/prompts**.

---

## ⭐ Critic's reframe — read this first

The deep-dive's completeness critic flagged that the obvious pilots (model-grade your articles) are **secondary**. Two higher-leverage moves:

1. **Fix ingest before grading output.** Your real, recurring pain is the **2026-05-14 anchor-miss** (4 of 6 bundles dropped operator-declared anchor URLs). A tiny **pre-ingest code grader** that halts the drain when picked videos overlap <50% with declared anchors prevents that recurring tonight — and it makes every downstream article-quality eval *easier* (good ingest → fewer hallucinations to catch). **XS, zero API cost, deterministic.** This is the critic's pick for **best first pilot**.
2. **Formalize Phase 0.9 STRICT as code, not an Opus call.** Your hand-rubric has been applied to 40+ wikis. Codifying its 4 criteria as a JSON-schema + scoring logic (a `.claude/` hook/skill) is higher-ROI and cheaper than model-grading it each time.

Also heed: **"presence ≠ correctness."** A regex that confirms `[[links]]` *exist* doesn't confirm they point to the *right* topics; a sentence citing `[Source 1]` can still draw an unsupported inference. Code graders gate structure; model/human graders gate substance. Don't oversell the cheap ones.

---

## The menu (ranked by ROI-per-effort)

### Tier 0 — prerequisites (do regardless of which pilot)

**M0 · Define criteria + a 20-case test set *(XS, ~30 min, free)*.** Pick ONE surface. Write down the **measurable** criteria upfront (Anthropic: "less than 0.1% flagged" not "safe"). Collect **20 cases drawn from real failures** (volume > polish). You cannot grade anything without this — it's step 1 of the cycle.

**M0.5 · Try the no-code on-ramp *(XS, ~20 min, ~free)*.** Open the **Anthropic Console → Evaluate** tab. Paste a prompt with `{{variables}}`, auto-generate test cases, grade 5-point, compare two prompt versions side-by-side. Internalize the loop before scripting anything.

---

### Angle A — Knowledge pipeline (autopilot-research + Storm Bear wiki)

**A1 · Pre-ingest anchor-validation code grader ⭐ (critic's #1) — ✅ SHIPPED 2026-06-16.**
*Refined during implementation:* the force-inclusion mechanism **already exists** in `bin/autopilot-drain.py` (added 2026-05-14), so the real unguarded gap wasn't "anchors get out-ranked" — it was that an **unreachable/age-restricted/region-blocked anchor is dropped *silently* at probe time** and the drain ingests anyway. So A1 became a **post-selection assertion that fails loud** (CLAUDE.md Rule 12), guarding the existing feature rather than reimplementing it.
- **What shipped:** `validate_anchors()` + `_video_id()` helpers in `bin/autopilot-drain.py`, wired into `drain_topic()` between selection and NotebookLM ingest. Emits an objective signal (`overlap` ratio + `PASS`/`WARN`/`FAIL`); on **FAIL (<50%)** in a real drain it **aborts before NotebookLM** with a fix-it message. Runs in `--dry-run` too (reports, no halt). Regression test: `evals/test_anchor_validation.py` (12 checks, exits non-zero on failure → CI-ready; no network/API cost).
- **Verified:** `python -m py_compile` clean; unit + offline integration tests green (dead anchor → FAIL → 0 NotebookLM calls; good anchor → PASS → proceeds).
- **Test it yourself today (zero API cost):** add an `Anchors:` block with one dead URL to a `topics-queue.md` topic and run `python bin/autopilot-drain.py --dry-run` — you'll see `anchor validation: FAIL` with the dropped URL listed. Or just run `python evals/test_anchor_validation.py`.

**A2 · Librarian-discipline code grader *(XS, ~30 min, free)*.**
20-line Python checking each compiled article for the 6 structural markers your CLAUDE.md requires: source-citation line, ≥2 `[[links]]`, a `## Key Takeaways`, parent `_index.md` updated, `_master-index.md` updated, no orphaned `Source N`.
- *Metric:* mean pass-ratio ≥0.83/article. *Caveat (critic):* checks **presence, not correctness** — best as a **pre-commit gate** on `autopilot-research/`, not a post-hoc report.

**A3 · `gaps_closed_ratio` quality companion *(XS, ~30 min, free)*.**
Add a deterministic **quality score** beside the existing quantity metric: citation-coverage (% sentences with a source), cross-link compliance, claim-density vs the NotebookLM source. Tracks whether the autopilot trades quality for quantity.
- *Caveat (critic):* density-parity can reward inflation — prefer **"count distinct claims; each must have a source."**

**A4 · Article-faithfulness model grader *(S, ~1h, ~$0.10–0.20/article)*.**
Opus judges each compiled article vs its NotebookLM source: faithfulness, hallucination list, scope-drift. Reasoning-first + Structured Outputs. Calibrate on a known-good (telegram-recipe-a) + known-bad (agent-dashboard-os anchor-miss) pair.
- *Caveat (critic):* "≤10% hallucination" is too loose for a **"NEVER fabricate"** vault — pair with A2's deterministic "every claim cited" check.

**A5 · Phase 0.9 STRICT rubric → code/hook (critic's #2) *(M, ~half-day)*.**
Codify the 4 criteria (structural-unambiguity / operational-deployability / methodology-influence / structural-peer) as explicit thresholds + JSON schema in a `.claude/` skill. Higher ROI than an Opus call; runs vault-wide. (If you do model-grade it, calibrate on harness-engineering = PASS vs ai-news-w19 = REWORK, ≥10 examples.)

**A6 · Human spot-check protocol *(XS, ~15 min/week, free)*.**
Every Friday, grade ONE random article on 3 questions (usable? better/worse than a sibling? what's missing?) into `04 Reviews/`. This is the **calibration oracle** for A2/A4 — and the gold standard the automated graders answer to.

---

### Angle B — hireui real software (eval-first, before the feature exists)

> ⚠️ hireui has **zero** Claude API usage today ([[project_hireui_no_llm_yet]] — verified 2026-06-15). So this is **build-it-right**, not retrofit. Apply hireui's CONSTITUTION (agent-* branches, operator-only skills, BMAD, GitNexus-first) when working there.

**B1 · Schema/format code grader for the first AI feature *(XS, ~30 min, free)*.**
For the likely first feature (resume↔JD match score), write the **output contract first**: `Ajv`/jsonschema validates `match_score ∈ [0,1]`, required fields, `confidence_bucket` enum, no timestamp (cache-kill detector). Pure code, gates output shape.
- *Metric:* 100% schema pass over 50 runs.

**B2 · Match-quality model grader (watermelon detector) *(S, ~1h, ~$0.10–0.20/run)*.**
LLM-as-judge reads resume + JD + the model's draft, **reasons then** scores 1–5: does the score match the bucket? Does the reason cite ≥2 concrete evidences? Is it a "watermelon" (green outside, red inside)? Opus judge, Structured Outputs.

**B3 · Golden test set + regression detector *(S, ~1h, ~$0.30–0.50/run)*.**
20 resume↔JD pairs across categories (perfect / near / weak / watermelon / over- & under-qualified) with **expected score ranges** from a recruiter. Baseline the metrics; fail if any drops >10%.

**B4 · CI regression gate *(L, multi-day, ~$7–10/mo)*.**
GitHub Actions on PRs touching AI routes: run B3, compare to baseline, **block merge** on regression. Add to hireui CLAUDE.md: "AI-route changes must pass the eval gate." (Needs `ANTHROPIC_API_KEY` secret + threshold calibration.)

**B5 · Weekly human review sampler *(XS, ~15 min/week, free)*.**
Recruiter reviews 5 random match decisions; track agreement %; <80% two weeks running → retrain. Catches silent drift both automated graders pass.

---

### Angle C — Claude Code skills & prompts (general dev flow)

**C1 · `yt-search` output-contract test *(XS, ~30 min, free)*.**
Code grader: does `yt-search` always return valid structured JSON (8 fields, integer counts, date format, valid YouTube URL, no dup IDs)? Run 20 queries; gate at ≥95% pass.
- *Caveat:* yt-dlp is non-deterministic — baseline over 3–5 runs.

**C2 · Wiki-article completeness rubric (reusable) *(S, ~1h, ~$0.30–0.50/audit)*.**
A copy-paste Python harness: `textstat` for readability + an Opus model grader (reasoning-first) scoring structure / cross-linking / citation / readability / no-fabrication 1–5. This is the **reusable eval harness** you drop into any project.

**C3 · CLAUDE.md 12-rule compliance checker *(M, ~half-day, ~$0.20–0.30/audit)*.**
Hybrid: code (radon cyclomatic-complexity for Rule 2, docstring coverage for Rules 1/4, raise/assert presence for Rule 12) + model grader for intent-level rules (Rule 4 goal-driven, Rule 9 tests-verify-intent). Pre-commit hook, gate ≥75%.

**C4 · Quality dashboard / feedback loop *(M, ~half-day, ~free)*.**
Aggregate C2 scores + coverage + cross-link health per compile cycle into a trend file; flag "LOW CONFIDENCE" cycles loud (Rule 12). Needs 4–6 weeks before thresholds mean anything.

**C5 · Micro-eval loop for skill iteration *(S, ~1h, ~$0.50–1.00/iteration)*.**
When a skill drifts: define criteria → 10 cases → grade → change ONE thing → re-run → accept only if ≥10-pt improvement. Cap 5 iterations/skill/week. The prompt-iteration loop, driven by an objective score.

---

## Recommended paths

- **If you want the highest-leverage, lowest-effort win that fixes a *real recurring bug*:** **M0 → A1** (anchor-validation, ~1h total). It stops the anchor-miss tonight and makes everything downstream easier. *This is my recommendation.*
- **If you want to learn the technique hands-on, low risk:** **M0.5 → A2 → A4 → A6** on the wiki pipeline — code-gate structure, model-grade faithfulness, human-calibrate weekly. A self-improving knowledge base.
- **If you want to advance Goal #2 (real software):** **M0 → B1 → B2 → B3** as the eval-first spec for hireui's first AI feature — so quality is measurable *before* the feature ships, not bolted on after.
- **If you want a reusable asset across every project:** **C2** (the drop-in harness) + **C5** (the iteration loop).

> **Why A1 over the others:** it's the only method that targets a **demonstrated, dated, recurring failure** in your own logs, costs nothing, is fully deterministic, and gates at the layer where the problem actually is. The model-graders are valuable but secondary — and the critic is right that good ingest shrinks the work they have to do.

## Next step

Pick a surface + a path above. I can implement the first pilot end-to-end in this session (A1 is ~30 min and self-contained). Full per-method implementation steps, success metrics, and starter code are in the workflow output (`wf_dd6c7095-c76`) and the wiki at [[prompt-evaluation/_index]].
