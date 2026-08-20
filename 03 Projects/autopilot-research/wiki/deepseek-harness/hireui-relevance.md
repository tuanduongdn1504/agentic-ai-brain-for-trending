# hireui relevance

> Target: `/Users/Cvtot/monorepo/hireui` — the TalentAxis recruitment SaaS that is the Goal #2 pilot target. Standing constraint: the **candidate-LLM legibility ADR** (any hireui LLM path touching a candidate must be fixed + legible + audited + human-in-loop + eval-gated, per EU AI Act).

## Verdict: take one idea, install nothing

**DSH is not a hireui candidate and this page does not argue for one.** Developer preview; plugins get full shell and filesystem access; DeepSeek's own docs disclaim the sandbox as a security boundary; no eval harness anywhere in the stack; closed to external PRs so there is no upstream recourse. Any of those alone disqualifies it from a codebase that processes candidate PII.

**What transfers is the trajectory.**

## The one thing worth building: a trajectory for hireui's LLM calls

The ADR requires that a candidate-facing LLM decision be **legible and audited**. hireui has **no LLM integration yet** (verified 2026-06-15: zero Claude API usage in product code), which means this is a build-it-right opportunity rather than a retrofit — the same framing that made the ADR worth ratifying before any code existed.

DSH's trajectory is an existence proof of the right shape for that audit surface. What it exposes per turn:

- the **exact system prompt** the model received
- the **tool list** actually presented
- **context injections made by the harness itself** — the ones the application added, not the user
- reasoning, every tool call and result
- per-turn token accounting and context-window attribution by contributor
- full **JSON export** of the session
- searchable, time-range-selectable

**Map that onto the ADR's "answerability record" requirement and it is nearly a spec.** For a Match-Explain feature, the audited artifact should be: *this candidate, this job, this exact prompt, these retrieved fields, this output, this reviewer, this verdict* — recoverable months later for a regulator or a rejected candidate.

The vault has been circling this shape from three directions and none of them cover it:

- `claude-code-observability` — the OTel/ccusage **cost** measurement layer
- `prompt-evaluation` — **grading outputs**, and the `evals/` harness whose anchor-validation gate is already shipped in `bin/autopilot-drain.py`
- the legibility ADR — the **requirement**

**DSH's trajectory is the missing middle: the per-call context record.** It is borrowable as a design without running DSH, which is exactly the kind of zero-install port the vault keeps identifying and not executing.

## Concrete next action, ~2 hours, zero install

Before hireui's first LLM call ships, write `hireui/docs/adr/llm-trajectory-record.md` specifying the persisted record for every candidate-touching LLM call: prompt (system + user, verbatim), model + version, all injected context with its provenance, tool calls, raw output, token counts, reviewer identity, and final human verdict. Then make it a **required** field-set — not a logging nice-to-have — so that a call which cannot produce the record cannot ship.

This is the same shape as the strongest primitive the vault has borrowed recently: **a code-enforced gate where the artifact cannot exist without its evidence** (v248's report gate — no finding without a required PoC). Apply it here as: **no candidate-facing LLM output without a complete trajectory record.**

## What explicitly does not transfer

- **The plugin architecture.** hireui needs fewer arbitrary-code extension points, not more. Full-shell-access plugins in a PII codebase is the inverse of the ADR.
- **Creator mode / self-modifying anything.** The ADR requires *fixed* logic on candidate paths. A system that rewrites its own agent loop cannot satisfy "fixed + audited."
- **The DSH model provider.** Unrelated to the harness question; hireui's model choice stays a Claude decision (Haiku 4.5 for Match-Explain per the existing plan).
- **`dsh-market` / any community plugin.** Never wire candidate data through a catalogue-sourced plugin. The catalogue is a ~16% sample of an 8,874-repo topic with no effect review at any stage.

## The pilot-worthy question (not a hireui pilot)

The bundle leaves one cheap, security-relevant experiment on the table: **did rc.6 → rc.7 relax the out-of-workspace write policy from hard-refuse to prompt-and-allow?** The VN source proposed it and half-retracted it; v242's source diff says rc.6→rc.7 was version strings only.

Settling it costs ~30 minutes in a throwaway VM (never on hireui, never on the vault host): install both, attempt an out-of-workspace write at workspace-write tier, diff the behaviour. **It is worth settling because the answer discriminates between two vault rules** — if the sandbox did change with zero code delta, then v242's D24 needs the plugin-pinning corollary *and* a behaviour-vs-diff corollary. That is a genuine sharpening of vault method, obtainable from a tool we have already decided not to adopt.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/trajectory-and-observability]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/install-and-operational-reality]] · [[claude-code-observability/_index]] · [[prompt-evaluation/_index]] · [[api-security-7-techniques/_index]] · [[miai-cv-matching-agent/_index]] · [[agent-memory-architecture/_index]]
