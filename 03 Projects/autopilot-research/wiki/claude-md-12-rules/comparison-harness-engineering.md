# 12 rules vs harness engineering — axis-by-axis comparison

> Mnilax's 12 rules (individual-developer Claude Code, May 2026) vs Lopopolo's harness engineering (OpenAI internal stack, Apr 2026). Both target the same era of Claude Code maturity but optimize for **different scales** (individual codebase vs 7-engineer OpenAI Frontier team) and **different cost profiles** (token-budget-conscious vs token-billionaire). This comparison surfaces where they agree, conflict, and what to keep when both can't coexist.

## Scale + cost-profile context

| Dimension | Mnilax 12-rule | Lopopolo harness engineering |
|---|---|---|
| Target user | Individual developer + small team | 7-engineer team at OpenAI |
| Token cost profile | Budgets matter (Rule 6: 4K/task, 30K/session) | $2-3K/day / "token billionaire" |
| Codebase scale | Single-repo or modest monorepo | 1M+ LOC, 750 packages, 1,500 PRs over 5 months |
| Reviewer count | Solo / standard PR | "Dark Factory" — zero human pre-merge review |
| Pipeline complexity | Single Claude Code session at a time | Multi-agent (Codex + Aardvark) + Symphony orchestration |

The systems are **different rungs of the same ladder**. The 12 rules optimize the individual rung (one developer + Claude); harness engineering optimizes the org rung (team + agent fleet). Trying to apply Lopopolo's posture without his scale produces over-engineering; trying to scale 12 rules without harness infrastructure produces drift.

## Agreement axes (8 — high-confidence overlap)

### 1. Read before write / agent-legibility

- **Mnilax Rule 8:** "Before adding code... read exports, immediate callers, shared utilities. 'Looks orthogonal' is the most dangerous phrase."
- **Lopopolo:** [[external|harness-engineering/terminology#agent-legibility|Agent-legibility]] — repo structured so models can parse intent, [[external|harness-engineering/blog-talk-evolution#high-leverage-missing-from-talk-content|Layered architecture]] (Types → Config → Repo → Service → Runtime → UI) enforces read-order

**Convergence:** both insist agents must consume existing structure before producing new code. Mnilax codifies as imperative; Lopopolo codifies via architecture.

### 2. Model for judgment only, deterministic code for everything else

- **Mnilax Rule 5:** "Use Claude for: classification, drafting, summarization. Do NOT for: routing, retries, deterministic transforms. If code can answer, code answers."
- **Lopopolo:** consistently positions Claude/Codex as **execution layer**, with deterministic guardrails (CI, lint, hooks, Skills) handling structure. Code IS code; agents do creative work.

**Convergence:** identical philosophy.

### 3. Fail loud / observability over hidden success

- **Mnilax Rule 12:** "If you can't be sure something worked, say so. 'Completed' is wrong if anything was skipped silently."
- **Lopopolo:** heavy emphasis on observability (Prometheus, Grafana, OpenTelemetry per [[external|harness-engineering/cited-references]]); blog mentions agents author dashboards in response to outages

**Convergence:** Mnilax codifies the agent behavior, Lopopolo codifies the infrastructure that makes silent failure detectable. Complementary, not redundant.

### 4. Convention beats novelty within a codebase

- **Mnilax Rule 11:** "Conformance > taste inside the codebase. Disagreement is a separate conversation."
- **Lopopolo:** specifies hard architectural rules (Layers, AGENTS.md as table-of-contents, isolated packages). Convention is enforced by repo structure not just preference.

**Convergence:** both reject "Claude's preferred style" as a decision input. Mnilax via rule, Lopopolo via architecture.

### 5. Tests verify intent

- **Mnilax Rule 9:** "Tests must encode WHY behavior matters, not just WHAT. A test that can't fail when business logic changes is wrong."
- **Lopopolo:** explicit emphasis on testing as semantic verification — agent records bug-repro video, then fix-confirmation video, as part of PR artifact

**Convergence:** both reject shallow-pass tests. Lopopolo's video-evidence is a stronger form of "intent" verification than Mnilax's abstract rule.

### 6. Multi-step work needs structure

- **Mnilax Rule 10:** "Checkpoint after every significant step. Don't continue from a state you can't describe back."
- **Lopopolo:** Symphony architecture enforces this via durable execution + claim management; Ralph Loop is the iteration primitive

**Convergence:** identical problem (multi-step drift), different solution (imperative discipline vs infrastructure pattern).

### 7. Push back when simpler exists

- **Mnilax Rule 1:** "Push back when a simpler approach exists."
- **Lopopolo:** the blog's "Map, not Manual" philosophy — `AGENTS.md` ~100 lines NOT 1,000-page instruction manual; "giant files crowd out the task and rot instantly"

**Convergence:** both anti-elaboration. Mnilax for code, Lopopolo for prompt/context.

### 8. Surface uncertainty explicitly

- **Mnilax Rule 1:** "State assumptions explicitly. If uncertain, ask rather than guess."
- **Lopopolo:** [[external|harness-engineering/open-questions]] documents his own hedges explicitly — "I have not quite figured out how to use Spark yet", "TBD we have not figured this out"

**Convergence:** both treat surfaced uncertainty as virtue. Lopopolo demonstrates it; Mnilax codifies it.

## Conflict axes (4 — choose-one decisions)

### 1. Code as burden (Mnilax) vs code is free (Lopopolo)

- **Mnilax Rule 2:** "Minimum code that solves the problem. No speculative features."
- **Mnilax Rule 3:** "Touch only what you must. Clean up only your own mess. Don't refactor what isn't broken."
- **Lopopolo:** "**Code is free**... infinitely parallel... ability to produce, maintain, refactor, and delete code is no longer a forcing function." Concrete example: agents reimplemented `map-with-concurrency` instead of using `p-limit` to fit internal OTEL

**Tension:** direct opposition. Mnilax says don't reimplement; Lopopolo says reimplementing IS the optimization at scale.

**Resolution rule for personal harness:**
- At individual / small-team scale → Mnilax wins. Code IS burden because YOU maintain it.
- At Lopopolo's scale (multiple agents per repo, $2-3K/day token throughput, no human edits) → code being "free" only holds because agents maintain it
- **Use Mnilax default; consider Lopopolo's stance only when your maintenance is also fully agent-driven**

### 2. Token budgets (Mnilax) vs token billionaire (Lopopolo)

- **Mnilax Rule 6:** "Per-task: 4,000 tokens. Per-session: 30,000 tokens. If approaching budget, summarize and start fresh."
- **Lopopolo:** "borderline negligent" not to operate at ~$2-3K/day token throughput

**Tension:** opposite optimization targets.

**Resolution rule:**
- Default to Mnilax — budgets force discipline and surface drift early
- Lopopolo's posture works only when you have **multi-agent orchestration** (Symphony) and **observability** to spot when an agent loop is wasteful before it burns the budget
- **Most personal harnesses don't have either** → Mnilax holds

### 3. Surface conflicts (Mnilax) vs trash and rebuild (Lopopolo)

- **Mnilax Rule 7:** "If two patterns contradict, pick one (more recent/more tested), explain why, flag the other for cleanup."
- **Lopopolo:** Symphony "can trash and rebuild entire worktrees from scratch if implementation fails to meet spec"

**Tension:** Mnilax is incremental + conservative; Lopopolo is throw-away + maximalist.

**Resolution rule:** depends on whether you can ALWAYS rebuild. If your test suite isn't comprehensive enough to verify a rebuilt implementation, Mnilax's incremental conflict-resolution is safer.

### 4. Convention conformance vs Symphony's "agent-legible" rewrite

- **Mnilax Rule 11:** "Match codebase conventions even if you disagree. Don't fork silently."
- **Lopopolo (implicit):** **changing the architecture** of a codebase to be more agent-legible (the 750-package hyper-modular structure) IS the right move when humans aren't the primary reader

**Tension:** Mnilax assumes humans-are-readers context; Lopopolo's stance reverses the assumption.

**Resolution rule:** if humans still review or onboard via this codebase, Mnilax wins. If the codebase is genuinely "Dark Factory" with no human direct readership, Lopopolo's restructuring becomes valid.

## What to keep when both can't coexist (decision rules for personal harness)

Adapting both to a single individual-developer setup:

| Decision | Default to | Reason |
|---|---|---|
| "Should I write more code or less?" | **Mnilax Rule 2 + 3** (less) | You maintain it personally |
| "Should I touch unrelated code?" | **Mnilax Rule 3** (no) | Same as above |
| "Should I budget tokens?" | **Mnilax Rule 6** (yes) | Cost discipline + drift detection |
| "Should I use Claude for X?" | **Both agree** (Rule 5 + Lopopolo) | Judgment only |
| "Should I write tests that verify intent?" | **Both agree** (Rule 9 + Lopopolo) | Adopt strictest version (Lopopolo's video-evidence if applicable) |
| "Should I read code before writing?" | **Both agree** (Rule 8 + agent-legibility) | Strongest possible adoption |
| "Should I checkpoint?" | **Mnilax Rule 10** (yes) | Lopopolo has Symphony infra; you don't |
| "Should I match conventions?" | **Mnilax Rule 11** | You're operating at his "humans review" rung |
| "Should I fail loud?" | **Both agree** (Rule 12 + observability) | Adopt Lopopolo's infra discipline if scaling up |

**Compound posture (recommended for individual / small team):**
- Adopt all 12 Mnilax rules as the **floor**
- Layer Lopopolo's specific practices that don't conflict: video-evidence tests (Rule 9 amp), agent-legible architecture (Rule 8 amp), observability infrastructure (Rule 12 amp)
- Defer Lopopolo's scale-dependent practices (Token Billionaire spend rate, Trash-and-Rebuild, 750-package decomposition) until you have his support infrastructure

## Cross-link maintenance

When future ingests touch either system:
- **New Lopopolo claim** that adds to comparison → append to relevant agreement / conflict axis
- **Independent verification of Mnilax's 41% → 3% claim** → reference here AND in [[the-12-rules#the-numbers]]
- **Third system to compare** (e.g., from vividkit.dev claudekit ingest) → create new `comparison-claudekit.md` rather than expanding this article

## Key Takeaways

- **Mnilax 12 + Lopopolo harness target different scales**, not different methodologies. Most personal harnesses operate at Mnilax's scale.
- **8 of 12 rules have Lopopolo's harness as amplifier** — same goal, Lopopolo solves via infrastructure where Mnilax solves via discipline
- **4 hard conflicts** — code as burden vs free, token budgets vs unlimited, incremental vs trash-rebuild, convention conformance vs agent-legible restructuring. Default to Mnilax for individual scale; consider Lopopolo only when his infrastructure preconditions are met.
- **Recommended compound posture:** all 12 Mnilax + Lopopolo's non-conflicting amplifiers (video-evidence tests, observability, agent-legible architecture)
- **The two systems are evolutionary, not competing** — Mnilax addresses individual-rung failures; harness engineering addresses org-rung failures. Move up rungs as your infrastructure can support it.
