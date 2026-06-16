# Advisor Strategy (cheap executor + expensive advisor)

> Lever #3 in [[_index]]. The Pareto-optimal way to cut cost while preserving intelligence.
> **It's a real first-party tool**, not just a pattern: `advisor_20260301` (beta header `advisor-tool-2026-03-01`) — confirmed via the bundled `claude-api` skill (`shared/tool-use-concepts.md` §Advisor).

## Mechanism

Run the agent loop on a **cheaper executor model** (Sonnet or Haiku). Give it an **advisor tool** backed by a **more capable model** (Opus). The executor handles routine "shapes" itself; when it hits something unusual it can't confidently resolve, it calls the advisor for guidance/review, then integrates the advice. The advisor runs its own API call — you don't orchestrate it manually.

**Analogy from the talk:** a junior engineer paired with a senior. The junior does the work; with the senior's review/architecture guidance they reach near-senior results at junior cost.

## The "watermelon" example (why the advisor earns its keep)

In the demo, Sonnet reviewed a contract-renewal transcript (Metropolis, the biggest client) and reported it on track — *green outside*. The Opus advisor looked harder and caught the real risk — *red inside* ("watermelon"): the mayor specifically wanted a superhero who wasn't available on the event date, so the renewal would actually fail. **Opus overrode Sonnet's optimistic read and flagged the error.** That catch is the value: cheap model for throughput, expensive model for the judgment calls that matter.

## Why it's Pareto-optimal

- **Hard/complex tasks:** advisor is consulted → better architecture/decisions (talk cites Bolt). *(Customer claim = anecdote.)*
- **Simple tasks:** advisor is *not* called → no extra cost.
- Net: you move down the cost curve without moving down the intelligence curve.

**Magnitude:** Anthropic's advisor strategy reportedly cuts cost ~**85%** (Haiku executor + Opus advisor vs Sonnet-for-everything) — corroborated by InfoQ's Code with Claude coverage (per research workflow; shipped ~2026-04-09).

## How to apply (3 options, easiest first)

1. **Official advisor tool (recommended):**
   ```json
   { "type": "advisor_20260301", "name": "advisor", "model": "claude-opus-4-8" }
   ```
   …on a request whose top-level `model` is `claude-sonnet-4-6` (or `claude-haiku-4-5`). Beta header `advisor-tool-2026-03-01`.
2. **Managed Agents multiagent:** a coordinator on a cheap model with subagents on Opus for hard sub-tasks.
3. **Manual escalation loop:** run executor; on low-confidence/complexity signals, re-run the turn on Opus and take its answer.

## Pricing math (current, per MTok — from the `claude-api` skill)

| Model | Input | Output |
|---|---|---|
| Opus 4.8 | $5 | $25 |
| Sonnet 4.6 | $3 | $15 |
| Haiku 4.5 | $1 | $5 |

Blended input cost ≈ `routine% × executor + escalation% × advisor`. E.g. **80% Haiku + 20% Opus-advisor ≈ $1.80/MTok vs $5 all-Opus (~64% off)**; Haiku-vs-Sonnet-everything is the ~85% headline. Tune the escalation rate to your task mix.

## Key Takeaways

- Don't run everything on Opus. Run the loop cheap; escalate the hard shapes.
- The advisor tool makes this a one-tool config change, not a custom router.
- The "watermelon" failure mode (cheap model says fine, expensive model catches the real problem) is exactly what the advisor exists to catch.

Related: [[demo-cost-progression]] (final lever in the arc), [[_index]].
