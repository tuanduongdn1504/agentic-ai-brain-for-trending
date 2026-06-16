# Pilot methods — applying Claude API cost optimization to your workflow

> **Source knowledge:** [[claude-api-cost-optimization/_index]] (Punit/Puneet Shah, Code with Claude London).
> **Goal:** turn the four levers (caching → context engineering → advisor) into something running in *your* stack.
> **Where it applies:** the levers are about **metered Anthropic API spend**. Your Claude Code / Cowork usage is mostly subscription (not directly metered).
> **⚠️ Correction (verified 2026-06-15):** hireui was assumed to have live Claude API calls (resume parsing / JD gen / candidate matching) — it does **not**. A full scan (`package.json` deps + `src`/`apps`/`packages` source + env vars) found **zero LLM integration** in hireui's product code; the only "anthropic/claude" strings are in its agent-harness tooling. So there is currently **no API path in hireui to retrofit caching onto.** The levers still apply to hireui — but as a **build-it-right spec for its first AI feature** (M6-as-spec), not a retrofit (M1). For an *existing* metered target, you'd need a product/service that actually calls the Anthropic API today (none found locally). Otherwise the live "apply" path is **M5 (sandbox replication)**.

## Current pricing anchor (per MTok, from the bundled `claude-api` skill, 2026)

| Model | Input | Output | Cached input (≈0.1×) |
|---|---|---|---|
| Opus 4.8 | $5 | $25 | $0.50 |
| Sonnet 4.6 | $3 | $15 | $0.30 |
| Haiku 4.5 | $1 | $5 | $0.10 |

---

## The methods (ranked by ROI-per-effort)

### M0 — Measure-first baseline *(prerequisite; ~30 min)*
You can't optimize what you haven't looked at (the talk's core discipline). Before changing anything:
- Open `console.anthropic.com` → analytics: record current **prompt-cache hit rate** + spend per workload. Use the new **cache-miss-reason** view.
- Add a tiny logger around your `messages.create()` calls that prints `usage.input_tokens / cache_read_input_tokens / cache_creation_input_tokens / output_tokens` per call.
- **Deliverable:** a one-screen "before" snapshot. Everything else is measured against it.
- **Risk:** none. **Do this regardless of which method you pick next.**

### M1 — Prompt-caching pilot in hireui *(~1h; highest ROI)*
The talk's "if you do one thing." In hireui's hottest API path (whatever re-sends a big stable prefix — system prompt, rubric, JD template, candidate schema):
1. Freeze the prefix: move any timestamp / per-request ID / unsorted JSON **out of the system prompt**.
2. Add one-line auto-caching: `cache_control: {"type": "ephemeral"}` on the request (or a manual breakpoint on the last stable block).
3. Verify `cache_read_input_tokens > 0` on the 2nd+ call; target >80% hit rate.
- **Expected payoff:** up to 90% off the cached portion of input + rate-limit headroom. The talk halved cost at just 58% hit rate.
- **Risk:** ~zero — caching does not change output (byte-identical). Reversible in one line.

### M2 — Claude API skill audit pass *(~30–60 min)*
The talk's "Claude API skill" = the `claude-api` skill bundled in Claude Code (the one used to verify this wiki). In any repo that calls the Anthropic API, ask Claude Code: *"audit my prompt-caching — trace the prompt assembly path, find silent invalidators, place breakpoints."* It runs the placement-pattern + silent-invalidator checklist for you.
- **Expected payoff:** finds the invalidators M1 might miss (tool reordering, model switches, non-deterministic serialization).
- **Risk:** none (read/advise). Good companion to M1.

### M3 — Advisor / model-tiering pilot *(~1–2h; biggest structural saving)*
Find an "Opus-everywhere" path in hireui that's mostly routine with occasional hard calls (e.g. candidate-fit scoring where most are clear-cut but edge cases need judgment). Convert it:
```json
// request model: claude-sonnet-4-6  (or claude-haiku-4-5)
"tools": [{ "type": "advisor_20260301", "name": "advisor", "model": "claude-opus-4-8" }]
// beta header: advisor-tool-2026-03-01
```
- **Expected payoff:** ~64–85% input-cost cut on that path (80% Haiku + 20% Opus-advisor ≈ $1.80/MTok vs $5 all-Opus); intelligence preserved on the hard cases (the "watermelon" catch).
- **Risk:** medium — needs a quality check (does the executor escalate enough?). Pilot on a non-critical path first; compare advisor-on vs all-Opus on a sample.

### M4 — Context-engineering pilot for an agentic loop *(~2–4h)*
If hireui has a tool-heavy agent (many tools and/or huge tool results):
- **Tool Search** (`tool_search_tool_bm25_20251119` + `defer_loading: true`) if you define many tools.
- **Programmatic Tool Calling** (`code_execution_20260120` + `allowed_callers`) if a tool returns big blobs you only need a slice of (e.g. parsing a full CV when you need 5 fields).
- **Compaction** (`compact-2026-01-12`) if any session runs long.
- **Expected payoff:** cost *and* quality (less junk context → better model performance).
- **Risk:** medium — more moving parts; do M1 first so caching is already in place.

### M5 — Sandbox "HeroCorp" replication *(~half day; learn-by-doing)*
Build a throwaway dashboard agent in a sandbox vault project and reproduce the talk's arc (baseline → cache → context-engineer → advisor), logging cost at each stage. Internalize the method on safe ground before touching the product.
- **Expected payoff:** confidence + a reusable reference implementation; write-up to `04 Reviews/`.
- **Risk:** none (sandbox). Best if you want to understand before deploying.

### M6 — Cost-discipline guardrail *(~1–2h; makes it stick)*
Make the win durable instead of one-off:
- A `CLAUDE.md`/constitution rule for hireui: "API calls must use prompt caching; system prompt must be timestamp-free."
- A hook or test that **fails loud** if cache-hit-rate on a smoke call drops to 0 (catches a future timestamp regression).
- **Ties to** the vault's "Cost-Discipline Enforcement Primitive" observation-track — this would be the first product→wiki contribution made concrete.
- **Risk:** low. Best paired with M1 (guard what you just won).

### M7 — Promote to Storm Bear curated wiki *(meta; operator decision)*
This topic is strong first-party evidence for the Cost-Discipline Enforcement Primitive OT. Candidate for the slow-track LLM Wiki at the next mini-audit. Not a "workflow" pilot, but the knowledge-management next step.

---

## Recommended path

**M0 → M1 → M3** on hireui, with **M6** to lock it in. M0 (30 min) gives the baseline; M1 (1h, zero-risk) banks the caching win; M3 (1–2h) is the big structural saving once you've proven measurement works; M6 keeps it from regressing. M2 folds into M1; M4 only if there's a tool-heavy loop; M5 if you want to learn before deploying.

> ⚠️ Apply ITS rules when working in `/Users/Cvtot/monorepo/hireui` (CONSTITUTION: agent-* branch policy, operator-only skill registry, GitNexus-first, BMAD harness, `.pilot-log`).
