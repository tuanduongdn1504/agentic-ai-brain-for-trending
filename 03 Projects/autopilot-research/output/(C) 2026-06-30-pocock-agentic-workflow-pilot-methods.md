# (C) Pilot methods — applying Matt Pocock's agentic workflow to your flow

> **Source:** wiki topic [[pocock-agentic-workflow/_index]] — David Ondrej × Matt Pocock podcast (`nQwJVHCtDDY`) + adversarially-verified deep-dives of the originals (`wf_4562f245-5bc`).
> **Operator context:** software dev + Scrum coach; deployment target **hireui** (TalentAxis recruitment SaaS, React/TS web+mobile, **no LLM in product yet**, CONSTITUTION with **I-2 agent-\* branch policy** + **I-8 operator-only skill registry**, **Candidate Detail refactor** in flight); two L5 vaults (Storm Bear + autopilot-research).
> **Goal #2 = *actually deploy* these methods into a real working flow.** Ranked by that leverage.

---

## The headline (if you do ONE thing this week)

**Run a blank-slate harness reset + `grill-me`-as-plan-mode on the Candidate Detail refactor, and measure it.** It's the cheapest, most reversible Pocock move, it generates *real* Goal-#2 deployment evidence, and it **composes** with two things already in your queue: the **cc-sdd #1 pilot** (spec discipline) and the **how-we-claude-code agent-native verification harness** (the verify step). Pocock supplies the *operating posture* (harness-over-model, procedures-you-drive, queues-not-loops); cc-sdd supplies the *spec ritual*; how-we-claude-code supplies the *verification surface*. That triangle is your strongest "I deployed it" story.

---

## Ranking at a glance

| # | Method | Angle | Effort | Goal #2 |
|---|---|---|---|---|
| **P1** | Blank-slate harness reset (observe-then-layer) | hireui / personal | M | ★★★ |
| **P2** | `grill-me`-as-plan-mode gate before every agent-\* task | hireui | S | ★★★ |
| **P3** | Codebase-as-harness AX audit on Candidate Detail | hireui | M | ★★★ |
| **P4** | Fix the codebase *before* delegating (token-spend = architecture) | hireui | M | ★★★ |
| **P5** | Install `mattpocock/skills`, default to `disable-model-invocation` | personal / hireui | S | ★★★ |
| **P6** | `to-prd` → dependency-ordered task decomposition | hireui | S | ★★★ |
| **P7** | Queues-not-loops triage board for agent-\* PRs | hireui | M | ★★★ |
| **P8** | Self-improving nightly review cron ("buy a lock") | hireui / vault | M | ★★★ |
| **P9** | "Review the system, not just the code" maturity loop | hireui | S | ★★ |
| **P10** | Sand Castle spike — sandboxed AFK agent (gated) | hireui | L | ★★ |
| **P11** | Model discipline: lock Opus 4.8, don't chase launches | personal / hireui | S | ★★ |
| **P12** | `disable-model-invocation` context-leak audit | personal | S | ★★ |
| **P13** | Procedure-first skill curation (you're the driver) | personal | S | ★★ |
| **P14** | Wispr Flow dictation as a throughput skill | personal | S | ★ |
| **P15** | `teach` skill to close a real personal knowledge gap | personal | S | ★★ |
| **P16** | "Ask AI what to *remove*" backlog-hygiene ritual | hireui / Scrum | S | ★★ |
| **P17** | Strategic-vs-tactical as the new seniority axis | Scrum | S | ★★ |
| **P18** | DX = AX as a Definition-of-Ready lens | Scrum / hireui | S | ★★ |
| **P19** | "Enthusiasm beats experience" hiring/pairing frame | Scrum | M | ★ |
| **P20** | Stateful-vs-stateless audit of the 5 vault skills | vault | S | ★ |
| **P21** | Apply harness-over-model to the vault routine itself | vault | M | ★ |
| **P22** | Post-refactor agent runbook (compounding knowledge) | hireui | M | ★★ |
| **P23** | Define a Goal-#2 *quality* scorecard (not just speed) | hireui | S | ★★★ |

---

## Angle A — hireui Goal #2 (the deployment target)

### P1 — Blank-slate harness reset (observe → then layer back) ★★★ · M
**What:** On a fresh `agent-*` worktree, strip the agent bootstrap to bare metal — no skills, no MCPs, minimal/empty `CLAUDE.md` & `AGENTS.md`. Run a small Candidate Detail task and **observe what the agent does unaided.** Then layer back ONLY the 3–5 **procedures you deliberately choose** (P2/P5/P6).
**Why:** Matt's closing prescription. Most setups silently bloat the context window; you can't tune what you haven't observed. This is also the safest way to discover which of your *existing* harness pieces actually earn their context cost. Respects **I-8** (you own the registry) by construction.
**Caution:** don't nuke `main`'s config — do this on a throwaway `agent-*` branch/worktree per **I-2**.

### P2 — `grill-me`-as-plan-mode gate ★★★ · S
**What:** Install `grill-me` as a **user-invoked** procedure (`disable-model-invocation: true`). Before any agent-\* implementation, type `/grill-me` with your spec and let it adversarially interview you until you've reached "98% shared understanding" (David's framing). Lock the resulting plan before code.
**Why:** For Candidate Detail specifically, this is where you surface **design-token drift, layout-parity questions, and the 3-tabs/avatar-72px decisions** *before* the agent writes code — exactly the failure mode of that screen. Cheap, reversible, and it composes with cc-sdd's spec step rather than competing.

### P3 — Codebase-as-harness AX audit ★★★ · M
**What:** Before refactoring, measure the **Agent Experience** of the current Candidate Detail code: have an agent read `CandidateDetailScreen.tsx` + the Figma handoff and (a) estimate the refactor LOC, (b) flag every ambiguity (orphaned spacing/type tokens, navy `#1E2960`↔`#002D79`, accent `#E8743C`↔`#DC6803`, Inter↔Roboto drift). Then run a *tiny* spike (avatar-72px layout only) and compare actual tokens to the estimate. **Delta = your AX debt.**
**Why:** Matt: "your skills are the ceiling, and the codebase is the most-forgotten lever." A muddy spec makes *any* model burn tokens and ship low quality. This quantifies the debt and gives you a before/after Goal-#2 metric.

### P4 — Fix the codebase *before* delegating ★★★ · M
**What:** Use the P3 audit to ship **spec-hygiene PRs** first: reconcile Figma r2 ↔ mobile tokens, consolidate the color/spacing/type tokens, lock the verified timeline colors (`#ECFDF5`/`#FEF2F2`) and avatar size. *Then* branch `agent-*` for the real refactor.
**Why:** "Optimize token spend = have a codebase that's easier to change." Don't ask an agent to refactor on top of drifted tokens — clarify the target first. This is the ~10–20% strategic up-front investment (Ousterhout) that lets a cheaper model succeed later.

### P6 — `to-prd` → dependency-ordered task decomposition ★★★ · S
**What:** Run `/to-prd` on the locked Candidate Detail plan to produce a decomposed task list + acceptance criteria in **dependency order** (tokens → spacing → layout → copy → behavior), then feed tasks to agents one slice at a time.
**Why:** Tight scoping is the strategic-programming skill that makes delegation work. Thin, verifiable slices (run the full feedback loop after *each*) reduce agent churn and rework. *(Note: "tracer bullets" is a Pragmatic-Programmer concept Matt uses in his separate workshop, not this podcast — `to-prd` is the tool that operationalizes thin-slicing here.)*

### P7 — Queues-not-loops triage board ★★★ · M
**What:** A board with columns `Backlog → Triaged → Implementing → Ready-for-review → Spot-check → Merged`. Inbound work (incl. agent-\* PRs) lands in Backlog; you triage on **spec-clarity + context-cost + criticality**; only `agent-implement`-labelled items move forward. After auto-merging trivial fixes, **spot-check ~1-in-3.**
**Why:** Matt's "queues, not loops" — multiple agents pick scoped tasks off a queue; you stay the king prioritizing. Directly answers Goal-#2 deployment urgency with a *measured, controllable* rollout instead of a runaway loop.

### P8 — Self-improving nightly review cron ("buy a lock") ★★★ · M
**What:** A scheduled job (GitHub Actions `@cron`, or `/schedule` for the vault) that runs a `security-review`/`code-review` procedure over the last 24h of `agent-*` commits with a **cheap model**, a different slice of the repo each night; auto-flags high-confidence issues for you to approve.
**Why:** Matt's self-improving-systems principle — don't wait for a fancy model to catch bugs; build the loop that catches them with a cheap one. Pairs with your existing `/code-review` + `security-review` skills; the *cron* is the new part.

### P9 — "Review the system, not just the code" ★★ · S
**What:** When reviewing an agent PR, also write one line on **what the harness did well/badly** (Was the spec clear? Did it over-explore? Which skill misfired?). Feed that back into your skills/CLAUDE.md.
**Why:** Matt: review gives you *observability into your harness*, not just defect-gating. This is the feedback loop that makes P1's layered harness improve over time. Cross-link: [[claude-code-observability/_index]].

### P10 — Sand Castle spike (sandboxed AFK agent) ★★ · L · *gated*
**What:** On a **greenfield** hireui side-task (NOT the in-flight Candidate Detail refactor), try `@ai-hero/sandcastle` with a Docker provider + Claude Code to run one AFK agent, pull its commits back via the `branch` strategy, and review the PR.
**Why:** This is Matt's actual AFK substrate. Proves the parallel-agent pattern end-to-end.
**Cautions:** (1) **npm-security-check + install-snapshot** before installing (`@ai-hero/sandcastle`). (2) Its sandbox safety is *by-construction* (bind-mount blast radius), **not a certified guarantee** — never use the `no-sandbox` provider. (3) There is **no turnkey GitHub Action** — you replicate the pattern, you don't `uses:` it. (4) Defer until *after* the Candidate Detail refactor stabilizes (it has design decisions in flight that need HITL).

### P22 — Post-refactor agent runbook ★★ · M
**What:** After Candidate Detail ships, write `(C) candidate-detail-agent-runbook.md`: avatar/token/spacing conventions, acceptance-criteria template, Figma→code mapping, test structure. The next agent (or teammate) starts from this, not zero.
**Why:** Self-improving systems + the `teach`-skill ethos: each project teaches the next. Goal #2 is "methods that work *repeatedly*," and a runbook is how the knowledge compounds.

### P23 — Goal-#2 *quality* scorecard ★★★ · S
**What:** Define success for the refactor as **quality, not speed**: (1) zero design-token drift (Figma parity verified), (2) web/mobile identical data/behavior/copy (layout per device), (3) agent diffs are readable + pair-reviewable, (4) token spend measured + justified by scope.
**Why:** "If you ship low-quality code fast, Goal #2 fails." A scorecard makes the pilot *evidence* instead of vibes — and feeds P3's before/after AX numbers.

---

## Angle B — personal Claude Code harness hygiene

### P5 — Install `mattpocock/skills`, default to `disable-model-invocation` ★★★ · S
**What:** `npx skills@latest add mattpocock/skills`; select a small set (**grill-me, to-prd, to-issues, tdd, teach**); for each, set `disable-model-invocation: true` unless you genuinely want auto-trigger. Run `/setup-matt-pocock-skills` for issue/label config.
**Why:** The current gold-standard skills repo (150.8K★, MIT, 25 active skills). Defaulting to user-invoked keeps your context lean and the human driving — aligned with **I-8**.

### P11 — Model discipline: lock Opus 4.8, don't chase launches ★★ · S
**What:** Pin a stable model (Opus 4.8 medium, like Matt) for a month; only upgrade on *measured* cost/quality/speed wins. Document the decision.
**Why:** Matt waited ~a month on Opus 4.5 and isn't rushing Fable. Stability + measurement beats launch-week hype; supports Goal-#2 cost discipline. (You already have the measurement layer: `ccusage` + the OTel stack from [[claude-code-observability/_index]].)

### P12 — `disable-model-invocation` context-leak audit ★★ · S
**What:** Enumerate every skill the agent *can* auto-invoke; for each, decide "does it NEED to auto-trigger?" Default to **true** (manual); allow auto only for stateless, low-risk helpers.
**Why:** Every model-invokable skill leaks its description into context on every turn. This is the concrete hygiene behind P1's "layer back deliberately."

### P13 — Procedure-first skill curation ★★ · S
**What:** Audit your installed skills/plugins/MCPs and split them **procedure** (you invoke) vs **ability** (model invokes). Keep procedures; justify each ability or cut it.
**Why:** Matt keeps the steering wheel. Fewer abilities = less context leak + fewer auto-invocation surprises.

### P14 — Wispr Flow dictation ★ · S
**What:** Trial **Wispr Flow** (wisprflow.ai) for dictating specs/grill-me answers/PR descriptions.
**Why:** Matt calls dictation "overpowered" for developers — faster brain→tokens. Lowest-stakes experiment here; pure throughput.

### P15 — `teach` skill to close a real knowledge gap ★★ · S
**What:** In a scratch workspace, `/teach` yourself one real gap (e.g., the part of React Native layout or your mobile design system you're shakiest on), with a concrete *mission* tied to Candidate Detail.
**Why:** Dogfoods the stateful-skill pattern and the ZPD/retrieval-practice pedagogy — and directly raises the "your skills are the ceiling" ceiling on the work you're about to delegate.

---

## Angle C — autopilot-research + Storm Bear vaults

### P20 — Stateful-vs-stateless audit of your 5 project skills ★ · S
**What:** Classify `autopilot-research-routine` / `yt-pipeline` / `yt-search` / `notebooklm` / `bypass-403-escalation` as stateful (need local memory) vs stateless. Confirm the stateful ones (the routine's `_inventory.md`/loop-log) have clean state stores.
**Why:** Matt's stateful/stateless distinction is exactly the discipline that keeps the routine's coverage ledger honest (the silent-gap incident was a stateful-skill failure).

### P21 — Apply harness-over-model to the routine itself ★ · M
**What:** Treat the *vault routine* as a harness: where is it model-dependent vs structurally robust? (e.g., anchor-injection into the drain script so search doesn't miss operator-named URLs — already a known gap.) Improve the structure, not the prompt.
**Why:** "Queues not loops" already describes `topics-queue.md`; harness-over-model says invest in the *structure* of the routine. Low Goal-#2 weight, high meta-value.

*(P8's nightly review cron also applies to the vault as a `/schedule` lint/audit loop — see Angle A.)*

---

## Angle D — Scrum coaching

### P16 — "Ask AI what to *remove*" backlog hygiene ★★ · S
**What:** In backlog refinement, add a standing question: "what can we *delete* / simplify?" — and have AI propose removals, not additions.
**Why:** Matt: AI is bad at original ideas; you own the product. Counters the "1,000-feature VC app" failure mode. A clean Scrum-coaching ritual.

### P17 — Strategic-vs-tactical as the new seniority axis ★★ · S
**What:** Reframe team growth around **strategic** work (scoping, interfaces, tests, codebase legibility) since AI now does **tactical** (code-writing). Coach engineers to move up the strategic ladder; retire "tickets-closed" as the seniority signal.
**Why:** Ousterhout via Pocock — the durable framing for what human engineers are *for* in the agent era.

### P18 — DX = AX as a Definition-of-Ready lens ★★ · S
**What:** Add to your DoR: "if a human can't follow this spec, an agent will fail silently on it." Gate stories on spec clarity + acceptance criteria.
**Why:** Matt: DX and AX mirror each other. Makes "agent-ready" and "human-ready" the same bar — and improves both human handoffs and agent output.

### P19 — "Enthusiasm beats experience" pairing frame ★ · M
**What:** Pair an enthusiastic AI-native junior with an agent + a strategic senior reviewer; measure velocity/quality/morale; rotate.
**Why:** Matt's hiring take, reframed as a coaching experiment (and on-mission for a *recruitment* product). Lower Goal-#2 weight; high org-design value.

---

## Skip-list (what NOT to do — Pocock-derived + your CONSTITUTION)

- **Don't pilot `superpowers` (obra) first.** It defaults to **model-in-control auto-triggering**, which clashes with **I-8** (operator-owned registry). It's genuinely excellent and *more* popular than Matt's repo (241.7K★) — but start aligned with your governance; evaluate it deliberately later if you miss something specific (e.g., its `brainstorming`).
- **Don't go full Ralph/AFK on the in-flight Candidate Detail refactor.** It has live design decisions (Figma r2 parity) needing HITL. Ralph is **greenfield-only** by its author's own design.
- **Don't chase Fable** for hireui this month. Lock a stable model; upgrade on measured wins (P11).
- **Don't cargo-cult a giant skill stack.** Every model-invokable skill leaks context. Blank-slate (P1) then add deliberately.
- **Don't treat Sand Castle's sandbox as a certified security guarantee** or expect a turnkey GitHub Action — it's by-construction isolation + an internal-CI pattern to replicate.
- **Don't attribute workshop content to this video.** Smart Zone/100k, Brooks, tracer-bullets, 4-role architecture = the *separate AI-Engineer talk*, not this podcast.

## Critic's reframe (the honest "do this")

Most of these methods are *postures*, not deployments — and Goal #2 needs an actual deployment. So collapse the menu to a **two-week, evidence-producing sprint**:

1. **Week 1:** P1 (blank-slate on an `agent-*` worktree) → P3 (AX audit of Candidate Detail) → P4 (ship spec-hygiene PRs). Capture the P23 scorecard baseline.
2. **Week 2:** P2 (`grill-me` the locked plan) → P6 (`to-prd` decomposition) → implement 1–2 thin slices → P9 (review the system) → P23 (score it).
3. **Carry-forward:** P7 (triage board) + P8 (nightly review cron) become permanent; P10 (Sand Castle) waits for a greenfield task.

That sequence is the **smallest path to a real "I deployed Pocock's harness-first workflow on a production screen and here's the before/after" write-up** — file it in `04 Reviews/` (Storm Bear) as the Goal-#2 evidence, composing with the **cc-sdd #1** and **how-we-claude-code verification** pilots already queued.

> **Suggested next action:** start P1+P3 on a `agent-*` worktree of hireui this week, with the P23 scorecard open, and book a 2-week checkpoint to write the `04 Reviews/` Goal-#2 entry.
