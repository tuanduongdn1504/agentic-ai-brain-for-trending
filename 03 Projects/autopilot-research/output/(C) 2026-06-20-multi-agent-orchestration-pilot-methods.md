# Pilot methods — applying multi-agent orchestration (Claude Architect) to your working flows

> **Source:** [[multi-agent-orchestration/_index]] — ExamPro "Claude Architect: Multi-Agent Orchestration" (Andrew Brown / ExamPro, [vRYBG_R8JAI](https://www.youtube.com/watch?v=vRYBG_R8JAI)) + deep-dives of the three Anthropic originals it's built on ([Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents), [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk/overview)). Verification log: [[multi-agent-orchestration/source-provenance]].
> **Date:** 2026-06-20.
> **Your working flows (from vault + memory):** (A) the **autopilot-research knowledge pipeline** (this vault — which *already* runs multi-agent Workflows + a coordinator-like 8-phase routine); (B) **hireui** — TalentAxis recruitment SaaS, your **Goal #2** build target (no LLM integration yet → build-it-right, not retrofit); (C) your **Claude Code harness / Workflow-authoring flow**; (D) **Scrum coaching / team practice**.
> **16 methods, ranked.** Each is grounded in a specific video pattern (or one of the Anthropic originals), with a concrete first step and a success signal.
>
> **The headline:** the video's worked example is a **job-application screener** — a near-1:1 analog for an agentic feature in **hireui**. That makes surface B the highest-value path from this knowledge to Goal #2.

---

## ▶ Start here (recommended sequence)

1. **This week, lowest friction:** **A2** — add a **decompose-time coverage list + aggregate-time coverage check** to your Workflow-authoring template (~30 min). You just watched *this* build need it: the research agents narrowly drifted (a fabricated "CCA-F exam" framing + a "Blobotomy" leak) and only the verify-pass caught it. That's the EV-market narrow-decomposition failure, live.
2. **Strategic Goal-#2 track:** **B6 → B10 → B7** — spec a **resume-screener agent for hireui** straight from the video's worked example, **eval-first** (write the judge before the feature), with the **partition-planner split**. A design doc, no code yet — the cleanest turn of this video into Goal-#2 progress.
3. **Ongoing habit:** **C15 + C14** — before you reach for a multi-agent Workflow, ask *"would a single well-prompted call + retrieval do?"* (Building Effective Agents' "start simple"), and *"never invoke a sub-agent unless it answers a real question"* (cost discipline; multi-agent burns ~15× the tokens of a chat).

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **A2** | Decompose-time + aggregate-time coverage gates in Workflows | A pipeline | **Low** (~30m) | **High** | Fixes the exact failure this build hit; reusable in every fan-out |
| **B6** | Spec a hireui resume-screener (design doc) | B hireui | Med (design) | **Very High** | The video *is* this feature; closest blueprint to Goal #2 |
| **B10** | Eval-first: judge + 20–50 cases before the feature | B hireui | Med | **Very High** | Video + research-system both: don't trust un-evaluated agents |
| **B7** | Partition-planner ↔ coordinator split for the screener | B hireui | Med | High | Prevents gaps *and* overlap; routing decided upstream |
| **C15** | "Would a single call do?" — start-simple gate | C harness | Low (heuristic) | **High** | The originals' core principle the video omits; saves whole Workflows |
| **A1** | Planner-vs-executor discipline in Workflow scripts | A pipeline | Low–Med | High | One place owns the work-list; stages stay "dumb" executors |
| **A4** | `evaluate_coverage` gate + iteration cap in the routine | A pipeline | Med | High | Turns `gaps_closed_ratio` into a real exit gate |
| **B8** | Coverage gates as fairness/compliance safeguards | B hireui | Design | **Very High** | A narrow screener silently dropping a dimension = legal risk |
| **C14** | "Never invoke unless it answers a real question" | C harness | Low | High | ~15× token discipline; scale effort to complexity |
| **A3** | Dynamic selection in yt-pipeline / drain | A pipeline | Low–Med | Med | Don't run the full fan-out for a small extend |
| **B9** | Refinement loop with a hard cap + `submit_final` gate | B hireui | Med | Med–High | But heed the caveat: iteration can make it *worse* |
| **C11** | Refactor skills/Workflow scripts for "ownership" | C harness | Low–Med | Med | Small functions as docs; you must be able to verify it |
| **C12** | Learn the `@tool` + in-process-MCP SDK shape | C harness | Low (read) | Med | The standalone-agent escape hatch from the Workflow tool |
| **A5** | JSONL trace + coverage report as the choke point | A pipeline | Low | Med | The loop-log *is* your observability choke point |
| **C13** | MAX-STEPS caps + forced exit gates by default | C harness | Low | Med | Runaway-loop guard in any loop you author |
| **D16** | Hub-and-spoke as a team-coordination lens | D coaching | Low | Med | Coordinator = lead/SM role; "spokes never talk directly" |

---

## A — Autopilot-research knowledge pipeline (this vault)

> This vault **already** runs multi-agent Workflows (this build was `wf_d77d2e85-2dc`, 24 agents) and a coordinator-like routine (`skills/(C) autopilot-research-routine.md`, 8 phases, `gaps_closed_ratio` metric). So these are refinements to a coordinator you already operate.

### A1 — Planner-vs-executor discipline in Workflow scripts
- **Video pattern:** the **partition-planner ↔ coordinator split** — one stage owns the routing *rules* and decides the work-list; downstream stages are "dumb" executors that don't re-decide. Routing in two places = "two places fighting" ([[multi-agent-orchestration/decomposition-and-partitioning]]).
- **Apply:** in your Workflow scripts, compute the work-list (files, channels, claims) in one scouting stage, then `pipeline()` over it — don't let later stages re-route.
- **First step:** in your next Workflow, add a comment marking the single "planner" step; assert every downstream `agent()` consumes its output rather than re-deciding scope.
- **Success signal:** no stage silently changes the set of items being processed mid-run.

### A2 — Decompose-time + aggregate-time coverage gates ⭐
- **Video pattern:** narrow decomposition silently drops whole dimensions (the EV-market example). Two safeguards: a **decompose-time** "what must be covered?" review, and an **aggregate-time** "did we cover X, Y, Z?" check ([[multi-agent-orchestration/decomposition-and-partitioning]]).
- **Apply:** before a research fan-out, have the workflow list the dimensions the topic *must* cover; after synthesis, gate on that list. This is the discipline that caught this very build's drift.
- **First step:** add two prompts to your Workflow template — a "coverage manifest" first agent and a final "coverage audit" agent that flags any manifest item missing or any claim not traceable to a source.
- **Success signal:** the audit agent catches ≥1 gap or unsupported claim on a real run (it just did — CCA-F + Blobotomy).

### A3 — Dynamic selection in the drain / yt-pipeline
- **Video pattern:** "never invoke an agent unless it answers a real question"; route by case, don't run the whole pipeline every time ([[multi-agent-orchestration/decomposition-and-partitioning]]).
- **Apply:** size the fan-out to the job — a cold-start topic warrants the full multi-source sweep; a small "extend topic X" does not.
- **First step:** in `bin/autopilot-drain.py` (or the routine's Phase 2), branch the source-count / agent-count on cold-start-vs-extend.
- **Success signal:** an "extend" run uses materially fewer agents/tokens than a cold-start.

### A4 — `evaluate_coverage` gate + iteration cap in the routine
- **Video pattern:** the **refinement loop** — run → `evaluate_coverage` → fill only the gaps → repeat to a MAX → `submit_final` only after coverage confirms ([[multi-agent-orchestration/refinement-and-observability]]).
- **Apply:** your routine already computes `gaps_closed_ratio`; make it a real *gate* (continue only if ratio < target AND iterations < cap), not just a logged number.
- **First step:** in Phase 6 (decide), encode the explicit MAX-cycle cap + the "stop when ratio ≥ target OR no new gaps for N cycles" exit (mostly already there — make the gate explicit and logged).
- **Success signal:** a loop-log shows the routine stopping on a *named* condition, not just running out of cycles.

### A5 — JSONL trace + coverage report as the observability choke point
- **Video pattern:** the coordinator is a **choke point** — log every message, emit structured (JSONL) traces, write a human-readable coverage report ([[multi-agent-orchestration/refinement-and-observability]]).
- **Apply:** treat the loop-log as that choke point; standardize a JSONL trace + a short coverage report per compile.
- **First step:** add a `## Coverage` block to the loop-log template (dimensions targeted vs. covered) and emit per-agent JSONL where Workflows allow.
- **Success signal:** you can answer "why did this compile underperform?" from the trace, not from re-running it.

---

## B — hireui (Goal #2, the real build target)

> hireui has **no LLM integration yet** (verified 2026-06-15). So these are **build-it-right specs**, not retrofits — same posture as the [[claude-api-cost-optimization/_index|cost-optimization]] + [[prompt-evaluation/_index|eval-first]] specs already in `hireui/_bmad-output/`. Follow hireui's own CONSTITUTION + BMAD harness when working there. **The video built a job-application screener — your domain exactly.**

### B6 — Spec a hireui resume-screener agent ⭐
- **Why:** the video's coordinator + spokes (keyword scanner, deep evaluator, red-flag detector, score aggregator) is a ready-made blueprint for a "screen this candidate against this req" feature ([[multi-agent-orchestration/hub-and-spoke-and-coordinator]]).
- **Apply:** write a 1-page design doc adapting the hub-and-spoke shape to hireui's data model.
- **First step:** create `hireui/_bmad-output/runbooks/resume-screener-agent-spec-2026-06-20.md` — coordinator + named screening spokes, what each spoke sees, how results aggregate into a ranked verdict. Cite [[multi-agent-orchestration/hub-and-spoke-and-coordinator]].
- **Success signal:** a reviewed design doc a future you could implement cold.

### B7 — Partition-planner ↔ coordinator split for the screener
- **Video pattern:** a **planner** decides which screening angles apply per req (junior vs senior vs non-traditional background), upstream; the **coordinator** executes one call per partition and doesn't invent angles ([[multi-agent-orchestration/decomposition-and-partitioning]]).
- **Apply:** model the screener as planner → coordinator so routing lives in one place; reqs of different seniority get different partition sets.
- **First step:** in B6's doc, add a "partition planner" section: inputs (req + resume), output (the partition set), and the rule that the coordinator runs exactly one call per partition.
- **Success signal:** the design has no routing logic duplicated between planner and executor.

### B8 — Coverage gates as fairness/compliance safeguards
- **Video pattern:** the EV-market narrow-decomposition failure = silently dropping a dimension. In a *hiring* screener that's not just incomplete — it's a fairness/legal exposure (e.g., ignoring transferable skills, employment-gap context, accommodations).
- **Apply:** make the decompose-time + aggregate-time coverage check (A2) a **named requirement** of the screener, tied to hireui's CONSTITUTION.
- **First step:** in B6's doc, add a "coverage contract" listing the dimensions every screen must address and an aggregate-time gate that blocks a verdict until they're covered.
- **Success signal:** a testable rule: "no screening verdict issues while any required dimension is uncovered."

### B9 — Refinement loop with a hard cap + `submit_final` gate
- **Video pattern:** evaluate-coverage → fill gaps → iterate to MAX → forced `submit_final` ([[multi-agent-orchestration/refinement-and-observability]]). **Caveat the video proved live:** iteration can make the score go *down* — so don't trust the loop without B10.
- **Apply:** allow a bounded refinement pass on a screen, but only land a verdict through an explicit exit gate.
- **First step:** in B6's doc, specify the MAX iterations + the `submit_final` gate + the rule "keep the best-scoring pass, not the last pass."
- **Success signal:** the design can't loop unbounded and can't ship a worse-than-earlier result.

### B10 — Eval-first: judge + 20–50 real cases before the feature ⭐
- **Source:** the research-system blog's eval rigor (LLM-as-judge on factual accuracy / completeness / source quality + human eval for the edge cases automation misses), and your own [[prompt-evaluation/_index]] pilot.
- **Apply:** this is your **eval-first Goal-#2 thread** made concrete — write the test before the feature. Build a judge for screening quality *and* fairness (no hallucinated credentials, consistent across comparable candidates).
- **First step:** 20–50 real (anonymized) screening cases + a multi-dimensional judge prompt in `hireui/evals/`, vetted with the prompt-evaluation 8-criteria rubric.
- **Success signal:** you could grade a candidate implementation on day one — and detect a fairness regression.

---

## C — Claude Code harness / Workflow-authoring flow

### C11 — Refactor skills + Workflow scripts for "technical ownership"
- **Video pattern:** the refactor-for-readability lesson — prompts in files, small functions that "act as documentation," stateless helpers; "the AI can write tests but that doesn't make them good tests" ([[multi-agent-orchestration/refactoring-and-agent-sdk-port]]).
- **Apply:** your Workflow scripts are getting large (this build's was ~250 lines). Extract the constants/specs, name the stages, keep each `agent()` prompt legible.
- **First step:** on your next Workflow, pull the big prompt strings into named consts and the article/spec lists into a single declarative block (this build already does — keep the pattern).
- **Success signal:** a teammate could read the script top-to-bottom and predict what each phase does.

### C12 — Learn the `@tool` + in-process-MCP SDK shape
- **Video pattern:** the port payoff — `@tool` decorator + `create_sdk_mcp_server` replace manual JSON schemas + a hand-rolled dispatch loop with an in-process MCP server ([[multi-agent-orchestration/agent-sdk-deep-dive]]).
- **Apply:** when a need outgrows the Workflow tool (a standalone, long-running, or deployed agent), this is the shape to reach for.
- **First step:** read [[multi-agent-orchestration/agent-sdk-deep-dive]] + skim the [Agent SDK docs](https://docs.claude.com/en/api/agent-sdk/overview); note the `query()` / `ClaudeAgentOptions` / `create_sdk_mcp_server` trio.
- **Success signal:** you can sketch a 1-tool SDK agent from memory.

### C13 — MAX-STEPS caps + forced exit gates by default
- **Video pattern:** the while-loop + MAX-STEPS cap (≈2× the expected steps) to catch runaway loops; a forced `submit_final` gate ([[multi-agent-orchestration/hub-and-spoke-and-coordinator]]).
- **Apply:** any loop you author (Ralph-loop, autopilot, a `while budget.remaining()` Workflow loop) gets an explicit cap + a defined exit.
- **First step:** audit your loop constructs for an unconditional `while True`; add a step cap + exit condition.
- **Success signal:** no loop in your tooling can run unbounded.

### C14 — "Never invoke a sub-agent unless it answers a real question"
- **Video pattern:** dynamic selection + the originals' cost framing — multi-agent uses ~15× the tokens of a chat; **scale effort to complexity** ([[multi-agent-orchestration/multi-agent-research-system-deep-dive]]; cross-ref [[claude-api-cost-optimization/_index]]).
- **Apply:** in Workflow design, drop any agent whose output won't change the conclusion; right-size the fan-out.
- **First step:** keep this one-line test next to your Workflow-authoring notes; apply it when you pick agent count.
- **Success signal:** you cut at least one speculative agent from a Workflow before running it.

### C15 — "Would a single call do?" — the start-simple gate ⭐
- **Source:** Building Effective Agents' core principle — *"simpler solutions like optimized single LLM calls with retrieval often suffice"*; use agents only for open-ended problems where steps can't be predicted ([[multi-agent-orchestration/building-effective-agents-deep-dive]]). This is the discipline the video *omits*.
- **Apply:** before authoring a multi-agent Workflow, explicitly check whether one well-prompted call (+ retrieval, + a schema) clears the bar.
- **First step:** add "start-simple check" as step 0 of your Workflow-authoring habit.
- **Success signal:** you solve at least one task with a single call that you'd previously have over-orchestrated.

---

## D — Scrum coaching / team practice

### D16 — Hub-and-spoke as a team-coordination lens
- **Video pattern:** the coordinator owns routing, context-sharing, error handling, and observability; **spokes never talk directly** ([[multi-agent-orchestration/hub-and-spoke-and-coordinator]]).
- **Apply:** a teaching frame for teams — the coordinator maps to a tech-lead / Scrum-master routing role; "spokes never talk directly" names the *anti-pattern* of undocumented side-channel coordination; and "narrow decomposition silently drops scope" is a sharp **story-slicing** lesson for sprint planning (a too-narrow breakdown ships silence, not an error).
- **First step:** in a retro or working-agreements session, use the choke-point vs. peer-to-peer contrast to surface where your team's coordination is invisible/unauditable.
- **Success signal:** the team names one place where work is routed informally (no choke point) and decides whether to make it visible.

---

## Cross-links

- [[multi-agent-orchestration/_index]] (source topic) · [[multi-agent-orchestration/video-to-original-crosswalk]] (the video↔original mapping) · [[multi-agent-orchestration/source-provenance]] (what's verified).
- Sibling pilots this composes with: [[prompt-evaluation/_index]] (B10's judge) · [[claude-api-cost-optimization/_index]] (C14's token discipline) · [[agentic-analytics-harness/_index]] (the "don't fragment knowledge across agents" lesson — Omni's, not this video's) · [[harness-engineering/_index]] (parent discipline) · [[claude-md-12-rules/_index]] (C11/C15).

## Suggested next action

Do **A2 this week** (~30 min — and you just saw why it matters: it's the safeguard that caught this build's own drift). Then open the **hireui Goal-#2 track** with **B6's design doc** (resume-screener, eval-first via B10, planner-split via B7) — the single highest-leverage turn of this video into product progress. Tell me which and I'll scaffold it: the A2 coverage-gate template into your Workflow-authoring notes, or the B6 screener spec straight into `hireui/_bmad-output/runbooks/`.
