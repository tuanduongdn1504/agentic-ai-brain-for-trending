# (C) Harness-Design Pre-Flight — "Complicated vs Complex?" (Cynefin)

> **Source:** the one immediately usable idea from [[../wiki/adaptive-engineering-beyond-harness/_index]] (Rajiv Chandegra, *"Beyond the Harness"*, AI Engineer Europe 2026). The talk borrows this from **Dave Snowden's Cynefin framework** (1999) — which the talk itself never names (see [[../wiki/adaptive-engineering-beyond-harness/caveats-and-corrections]]).
> **Status:** reusable decision aid for the vault's harness/agent work AND for hireui LLM-feature design. Zero-cost, zero-install.
> **Created:** 2026-07-15

## Why this exists

The "Beyond the Harness" talk argues that **the most expensive mistake in modern engineering is treating a complex problem like a complicated one.** A *fixed harness* (plan → spec → build → verify) is the **right** tool for **complicated** problems and the **wrong** tool for **complex** ones. So before you design a harness or build an agentic feature, spend 5 minutes classifying the problem. The payoff for this vault + hireui is the opposite of what the talk intends: **almost everything the operator does is *complicated*, which means the current deliberate-harness approach is correct** — this pre-flight *validates* it, and flags the rare exceptions.

## The distinction (only two domains matter here)

| | **Complicated** | **Complex** |
|---|---|---|
| Example | jumbo jet, clock, a CRUD feature, a CI pipeline | a flock, a market, a multi-team org, a live hiring market |
| Cause→effect | knowable by an expert (may need analysis) | only visible in retrospect; parts adapt to each other |
| Right method | **analyze → plan → predict → execute** (good practice) | **probe → sense → respond** (safe-to-fail experiments) |
| Right harness | **fixed** — spec-driven, deterministic gates, verify loop | **adaptive** — constraints + observation, amplify what works |
| Failure if mis-typed | over-engineering; slow but safe | **brittle** — you plan for a world that keeps moving |

*(Cynefin has 5 domains — Clear/Obvious, Complicated, Complex, Chaotic, Disorder. For engineering-task classification the Complicated↔Complex boundary is the load-bearing one; Chaotic = incident/outage "act first", and Clear = trivial/best-practice.)*

## The 4 diagnostic questions

Ask these before building. **Any two "yes" answers on the right → treat it as complex.**

1. **Decomposition** — Can I break this into parts, solve each, and reassemble a correct whole? *(Yes → complicated. No, the parts interact → complex.)*
2. **Repeatability** — Will the same inputs reliably produce the same good output? *(Yes → complicated. Depends on other agents/humans reacting → complex.)*
3. **Expert-knowability** — Could a domain expert, given time, specify the right answer up front? *(Yes → complicated. Only discoverable by trying → complex.)*
4. **Stability** — Will the problem hold still long enough for a plan to stay valid? *(Yes → complicated. It shifts as I work → complex.)*

## Worked classification — the operator's actual work

### hireui (the product) — **all complicated** → keep the fixed harness

| Work item | Classification | → Harness |
|---|---|---|
| Candidate-Detail refactor (drifted tokens, r1→r2 migration) | **Complicated** — knowable, decomposable, stable spec | Fixed: Figma SoT + locked plan paths + verify loop. *(Already the plan.)* |
| Match-Explain (first LLM feature: CV↔job) | **Complicated** — a scoped scoring/explanation task with a definable rubric | Fixed: Haiku structured outputs, recruiter-labeled evals, Mosh A2 seam. **NOT** an emergent multi-agent thing. |
| CV parsing / OCR ingestion | **Complicated** — deterministic-ish extraction w/ measurable accuracy | Fixed: accuracy eval gate before ship. |
| API-security hardening (BOLA/authorization, CORS, CSP) | **Complicated** — known checklist (OWASP API Top 10) | Fixed: audit → fix → test. |
| Docker/CI-CD deploy layer | **Complicated** — well-understood ops | Fixed: pipeline + gates. |

**Verdict:** every current + near-term hireui work item is **complicated**. The disciplined, spec-first, verify-gated approach is the *right* tool — the talk's own framework says so. Do **not** reach for emergent/adaptive orchestration here.

### The vault (autopilot-research) — **complicated** → the fixed routine is correct

| Work item | Classification | → Harness |
|---|---|---|
| Wiki compile (raw → articles → scorecard) | **Complicated** — a repeatable pipeline | Fixed: the 8-phase Loop Routine v2.1 (constitutional, metric-bounded). Correct as-is. |
| Adversarial verification of claims | **Complicated** — decomposable per-claim | Fixed: fan-out fact-checkers + critic. Correct as-is. |

**Verdict:** the routine's "NEVER recurse / scope-clamp / metric-bounded" constraints are the right call for a complicated problem. Do **not** relax them in the name of "emergence."

### The genuinely *complex* cases (where probe-sense-respond wins)

These are **not** software-build tasks — they're the social/organizational ones from the operator's Scrum-coaching hat:

- **Multi-team org dynamics / adopting a new process across teams** — parts (people) adapt to each other; you can't spec the outcome. → run small safe-to-fail experiments, sense, amplify.
- **A live hiring market's behavior** (what candidates/employers actually do in response to a feature) — emergent, shifting. → probe with A/B and instrumented rollout, don't over-plan.
- **Team-level "what agentic workflow should we standardize on?"** — depends on how the team reacts. → pilot, observe, don't mandate up front.

For these, the talk's *question* is genuinely useful even though its *answer* (build an emergent orchestrator) is not what you'd do.

## How to use it

1. **Add one line to the harness/feature design checklist** (vault harness-engineering thread + any hireui feature-spec template):
   > *"Pre-flight: is this **complicated** (knowable, decomposable, stable → fixed harness: plan/spec/verify) or **complex** (parts adapt, shifts as you work → probe/sense/respond)? Don't treat complex as complicated. Almost all build work is complicated."*
2. When something *feels* like it needs a swarm of agents, run the 4 questions first — it's almost always a complicated task wearing a scary costume.
3. Reserve "adaptive / probe-sense-respond" for the org/market/social cases, and even there, keep candidate-impacting decisions legible (see the companion ADR).

## Key takeaway

The most valuable thing "Beyond the Harness" gives the operator is **a validation, not a redirection**: run the pre-flight and your current fixed-harness discipline comes out *right* for essentially all of hireui + the vault. Adopt the **question**; you already have the correct **answer**.
