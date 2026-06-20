# Pilot methods — applying Omni's agentic-analytics-harness to your working flows

> **Source:** [[agentic-analytics-harness/_index]] — Omni's "Blobby" harness talk (Chris Merrick, Code with Claude London). Built by triangulation (video uncaptioned) — see [[agentic-analytics-harness/source-provenance]].
> **Date:** 2026-06-20.
> **Your working flows (from vault + memory):** (A) the **autopilot-research knowledge pipeline** (this vault — already piloting [[prompt-evaluation/_index|prompt-evaluation]]); (B) **hireui** — TalentAxis recruitment SaaS, your **Goal #2** build target (no LLM integration yet → build-it-right, not retrofit); (C) your **Claude Code harness / personal dev flow**; (D) **Scrum coaching / team practice**.
> **14 methods, ranked.** Each is grounded in a specific Omni finding, with a concrete first step and a success signal.

---

## ▶ Start here (recommended sequence)

1. **This week, lowest friction:** **M1** — fold Omni's **8-criteria benchmark-question rubric** into your live `evals/` harness (~30 min; directly extends the prompt-evaluation pilot you're already running).
2. **Strategic Goal-#2 track:** **M6 → M7 → M10** — spec a **"talk to your recruitment data" agent for hireui**, **semantic-layer-first** and **eval-first**, as a design doc. No code yet; this is the highest-value, lowest-risk way to turn this knowledge into Goal-#2 progress.
3. **Ongoing habit:** **M2** — weekly **session triage** of failed autopilot drains (read traces, root-cause, fix the query). It's Omni's #1 quality discipline, applied to your own pipeline.

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **M1** | 8-criteria benchmark-question rubric | A evals | **Low** (~30m) | High | Extends a live pilot; instant quality gate on eval sets |
| **M2** | Weekly "session triage" of failed drains | A pipeline | Low–Med | High | Omni's #1 eval discipline; observability-over-scorecards |
| **M6** | Spec a "Blobby-for-recruitment" agent (design doc) | B hireui | Med (design) | **Very High** | Closest published blueprint to your Goal #2 |
| **M7** | Build hireui's semantic layer FIRST | B hireui | Med | **Very High** | "The semantic layer is the moat" — do it before agent code |
| **M10** | Eval-first: judge benchmark before the feature | B hireui | Med | **Very High** | Ties hireui to your eval-first Goal-#2 thread |
| **M8** | Security-as-current-user invariant | B hireui | Design-time | **Very High** | PII/multi-tenant; cheap now, expensive later |
| **M3** | Observability-over-scorecards in the routine | A pipeline | Low | Med | Read the trace, not just `gaps_closed_ratio` |
| **M4** | High-quality error messages in `autopilot-drain.py` | A pipeline | Low–Med | Med–High | Omni's highest-ROI lever, applied to your tooling |
| **M9** | SQL-over-custom-format rule for hireui agent | B hireui | Design rule | High | Quantified 3–4→1 attempt win |
| **M11** | Error-recovery as a first-class component | B hireui | Design | High | The lever Omni says beats prompt tuning |
| **M12** | Model-native formats in your own skills | C harness | Low | Med | Fewer retries in your project-local skills |
| **M13** | Colocate context with definitions (CLAUDE.md) | C harness | Low | Med | Merrick's own analogy; you already do this well |
| **M14** | Don't fragment into too many sub-agents | C harness | Low (heuristic) | Med–High | "Blobotomy 1" — avoids a common multi-agent anti-pattern |
| **M5** | "Blobotomy" architecture-surgery log | D coaching | Low | Med | Team learning; = vault's "don't repeat mistakes twice" |

---

## A — Knowledge pipeline / evals (this vault)

### M1 — Adopt the 8-criteria benchmark-question rubric
- **Omni finding:** they score every eval *question* on 8 criteria — evaluability, coverage, realism, difficulty, non-redundancy, discriminative power, semantic clarity, data selectivity ([[agentic-analytics-harness/evals-and-error-recovery]]).
- **Apply:** add the 8-criteria checklist to your `evals/` harness; use it to audit the prompt-evaluation question set (and to vet new ones).
- **First step:** create `evals/benchmark-question-rubric.md` with the 8 criteria + a 1-line test each; run your current eval questions through it and flag any that fail ≥2 criteria.
- **Success signal:** you can point to ≥1 weak eval question the rubric caught (e.g. redundant or non-discriminative).

### M2 — Weekly "session triage" of failed drains
- **Omni finding:** daily analysis of **failed** user sessions, **trace-driven**, prioritized **over aggregate metrics**.
- **Apply:** your pipeline already flags `anchor-miss` / `low-signal` compiles (see `_master-index.md` ⚠️ entries). Triage them like Omni triages failed sessions.
- **First step:** a weekly 20-min pass — open the loop-log + raw bundle of each flagged compile, write a one-line root cause (bad query? recency filter? channel-cap?), and queue the fixed query for re-drain. The A1 anchor-validation gate in `bin/autopilot-drain.py` already automates part of this.
- **Success signal:** the ⚠️ anchor-miss topics (agent-dashboard-os, codex, claude-code-clones) get re-driven with corrected queries.

### M3 — Observability over scorecards in the routine
- **Omni finding:** "the eval number tells you *that* it failed; the trace tells you *why*." Merrick optimizes for the trace.
- **Apply:** when a compile's `gaps_closed_ratio` underperforms, don't just log it — **read the raw bundle + loop-log** before deciding the next action.
- **First step:** add a one-line note to the routine's Phase 6 (decide): "if ratio < target, read the trace before continuing." (Doc-only change in `skills/(C) autopilot-research-routine.md` — ask first, it's an existing skill file.)
- **Success signal:** a next-action recommendation that cites a trace observation, not just the metric.

### M4 — High-quality error messages in `autopilot-drain.py`
- **Omni finding:** authoring "what happened + how to fix" error messages was the **highest-ROI** quality lever — it beat prompt tuning.
- **Apply:** audit the drain script's failure paths (anchor-miss, 0-results, NotebookLM ask-fail) and rewrite each to state **cause + fix**.
- **First step:** grep `bin/autopilot-drain.py` for error/exit paths; for each, ensure the message names the cause and the corrective command.
- **Success signal:** next time a drain fails, the message alone tells you what to change.

---

## B — hireui (Goal #2, the real build target)

> hireui has **no LLM integration yet** (verified 2026-06-15). So these are **build-it-right specs**, not retrofits — same posture as the [[claude-api-cost-optimization/_index|cost-optimization]] spec already in `hireui/_bmad-output/runbooks/`. Follow hireui's own CONSTITUTION + BMAD harness when working there.

### M6 — Spec a "Blobby-for-recruitment" agent
- **Why:** Omni is the closest published blueprint to a "talk to your recruitment data" feature ("show me time-to-hire by department this quarter"). This is the most direct path from this video to Goal #2.
- **First step:** write a 1-page design doc in `hireui/_bmad-output/runbooks/` adapting Blobby's shape — **coordinator + one summarization sub-agent**, **SQL over DB views**, **semantic layer for recruitment metrics**, **eval-first acceptance**. Cite [[agentic-analytics-harness/multi-agent-architecture]].
- **Success signal:** a reviewed design doc that a future you could implement cold.

### M7 — Build hireui's semantic layer FIRST
- **Omni finding:** the semantic layer is the "intelligence backbone" / the moat — context colocated with data definitions, not a global prompt; ~175k-char budget; start minimal ([[agentic-analytics-harness/semantic-layer-as-context]]).
- **Apply:** before any agent code, define hireui's 5–10 core recruitment concepts ("active candidate," "time-to-hire," "pipeline stage," "offer-accept rate") with `ai_context` / `sample_values` / `synonyms` / `descriptions`.
- **First step:** a `semantic-layer.yaml` (or in-DB metadata) for those 5–10 metrics; seed from any existing schema/dbt-style definitions.
- **Success signal:** every metric the agent could be asked about has a colocated, human-readable definition.

### M8 — Security-as-current-user invariant
- **Omni finding:** the agent "can only ever run **as the current user**" — inherits existing permissions, never escalates.
- **Apply:** recruitment data is multi-tenant PII. Make this the #1 invariant of the design doc.
- **First step:** in M6's doc, write: "the agent executes queries under the requesting user's row-level permissions; never a service account; never cross-tenant." Aligns with hireui's CONSTITUTION.
- **Success signal:** a stated, testable permission boundary before any code exists.

### M9 — SQL-over-custom-format rule
- **Omni finding:** custom JSON DSL cost 3–4 attempts/query; **SQL (model-native) → 1 attempt** ([[agentic-analytics-harness/tool-design-and-sizing]]).
- **Apply:** the hireui agent should emit **SQL against read-only views**, not a bespoke query object.
- **First step:** note in M6's doc: "query tool emits SQL against curated read views; no custom query DSL." Define 2–3 starter views.
- **Success signal:** design avoids inventing a query format.

### M10 — Eval-first: judge benchmark before the feature
- **Omni finding:** LLM-as-judge + the 8-criteria benchmark; observability over scorecards.
- **Apply:** this is your **eval-first Goal-#2 thread** made concrete — write the test before the feature. Reuses M1's rubric.
- **First step:** 20–50 real recruitment questions (vetted with M1's rubric) + a judge prompt, as the feature's acceptance test, in `hireui/evals/`.
- **Success signal:** you could grade a candidate implementation on day one.

### M11 — Error-recovery as a first-class component
- **Omni finding:** teach recovery + retry budget + "what happened/how to fix" errors = the biggest quality win.
- **Apply:** spec it as a named component, not an afterthought.
- **First step:** in M6's doc, add an "error contract" section: retry budget, the "don't re-query unless filters changed" guardrail, and a structured error shape the agent can act on.
- **Success signal:** the design treats failure handling as a feature with its own acceptance criteria.

---

## C — Claude Code harness / personal dev flow

### M12 — Model-native formats in your own skills
- **Omni finding:** model-native > bespoke (3–4→1 attempt).
- **Apply:** when writing project-local skills / MCP tools, prefer SQL / standard JSON / markdown over invented formats.
- **First step:** scan `skills/` for any bespoke structured formats the model must be "taught"; note where a standard would cut retries.
- **Success signal:** at least one format simplification identified.

### M13 — Colocate context with definitions
- **Omni finding:** Merrick's analogy — `CLAUDE.md` = code context; semantic layer = data context, **near the definition, not global**.
- **Apply:** you already do this well (the vault's `_state/` chapter files; per-project CLAUDE.md). Carry it to hireui and any new project; cross-ref [[harness-engineering/anthropic-large-codebases-anchor|CLAUDE.md hierarchy]].
- **First step:** quick audit — is any CLAUDE.md carrying context that belongs next to a specific module/data instead?
- **Success signal:** context lives where the thing it describes lives.

### M14 — Don't fragment into too many sub-agents
- **Omni finding:** "Blobotomy 1" — splitting planner + query-writer into separate agents caused knowledge silos and infinite loops. Only the *context-isolating* summarizer sub-agent survived ([[agentic-analytics-harness/multi-agent-architecture]]).
- **Apply:** a heuristic for when you reach for a multi-agent Workflow or sub-agent: **"do these two need each other's knowledge to act?"** If yes → keep them one agent. Split only on **context-isolation** seams. (Also: bound long loops + checkpoint, like Omni's 50-iteration cap.)
- **First step:** keep this one-line test next to your Workflow-authoring notes.
- **Success signal:** you merge (or don't create) a sub-agent split that would have shared a knowledge seam.

---

## D — Scrum coaching / team practice

### M5 — The "Blobotomy" architecture-surgery log
- **Omni finding:** Omni names + documents major architectural surgeries ("Blobotomy" ×~5) as explicit learning artifacts.
- **Apply:** a lightweight ritual for hireui or any team you coach — when a big rewrite happens, capture it.
- **First step:** a one-paragraph template: **what we believed / what broke / what we changed / the principle.** Keep a running log.
- **Success signal:** the next "surgery" is logged — and the principle is reused, not re-learned. (This *is* the vault's prime directive: don't repeat the same mistake twice.)

---

## Cross-links

- [[agentic-analytics-harness/_index]] (source topic) · [[prompt-evaluation/_index]] (M1/M2/M10 build on it) · [[claude-api-cost-optimization/_index]] (M7/M11 caching levers) · [[harness-engineering/_index]] (parent discipline) · [[claude-md-12-rules/_index]] (M12/M13).

## Suggested next action

Do **M1 this week** (30 min, extends your live eval pilot). Then open the **hireui Goal-#2 track** by drafting **M6's design doc** (semantic-layer-first + eval-first). Tell me which and I'll scaffold it — and if you want the talk-specific numbers (45 tools / 50 iterations / Haiku→Sonnet) hardened, I can run an adversarial-verification Workflow like the last two ships.
