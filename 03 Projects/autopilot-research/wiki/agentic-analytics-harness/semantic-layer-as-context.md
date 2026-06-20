# The semantic layer as context: colocating data context with its definitions

## Source

First-party: [omni.co — Improving AI quality with context](https://omni.co/blog/improving-ai-quality-with-context) + [omni.co — Building Omni's architecture for agentic analytics](https://omni.co/blog/building-omnis-architecture-for-agentic-analytics). All T1 except where noted.

## The core idea

- The **semantic layer** is Blobby's **"intelligence backbone."** It "enforces governance, context, and business logic **by design**."
- It teaches the AI **your specific business language** — your metrics, definitions, logic — so the agent **already knows** what "active customer" means, which fields drive revenue, and **who's allowed to see what.**
- The load-bearing distinction vs a generic LLM: **context is stored *in the semantic layer*, not in a global prompt.** "Since Omni's AI is built on top of that semantic layer, it doesn't have to guess. It uses the **same trusted logic** that powers every query, report, and dashboard."
- It's **human-visible too** — users can debug or improve the logic. The context that steers the AI is the same artifact humans read.
- Merrick's analogy: **`CLAUDE.md` stores *code* context; the semantic layer stores *data* context — near the definition, not globally.** (This is principle #1 — *colocate context with definitions* — see [[agentic-analytics-harness/overview]].)

## The metadata fields [T1]

Context attaches to fields/Topics via:

| Field | Purpose |
|---|---|
| `ai_context` | Explicit instructions for the AI ("use this Topic to answer sales/revenue questions"). Keep **short and direct.** |
| `sample_values` | Concrete examples of a field's values. |
| `synonyms` | Alternative names users might say for a field. |
| `descriptions` | Plain clarifications of meaning/usage. |

> The talk recap [T2] frames a near-identical set as `ai_context` / `sample_queries` / `all_values` (enumerate valid values like `["EMEA","NAM","APAC"]` for fuzzy matching) / feedback loop. Same idea, slightly different field names between blog and recap — treat the **blog's names as canonical.**

## Three injection levels [T1]

Context is layered from global → specific:

1. **Model-level** — global behavior + "house rules": default assumptions, metric definitions, response style.
2. **Topic-level** — domain-specific facts, field preferences, default filters, example questions.
3. **View / field-level** — fine-tuning individual field interpretations.

## The budget [T1]

- The model handles **~200,000 characters total.**
- **~175,000** of that is allocated to **semantic-layer context.**
- Implication: context is **finite and must be curated** — you can't inject everything, so colocation + brevity ("short and direct") are economic necessities, not style preferences.

## The feedback loop [T1]

- **Read what users actually ask Blobby** via **Analytics > AI usage dashboard** to spot trends and gaps.
- **Refine definitions over time** from real sessions (this connects to *session triage* in [[agentic-analytics-harness/evals-and-error-recovery]]).
- **Seed initial context from `dbt` metadata** — don't start from scratch.
- Guidance: **start minimal** — "even a small amount of context is better than nothing"; begin with model-level + a few key Topics, then build.

## Key Takeaways

- **Put context where the thing it describes lives.** Data context → semantic layer; code context → `CLAUDE.md`/module docs. A global prompt that knows everything about everything doesn't scale (200k-char ceiling).
- **Context is a curated, budgeted asset (~175k chars).** "Short and direct," layered model→topic→field.
- **Enumerated valid values are a quality lever**, not metadata bureaucracy — they enable fuzzy matching and typo resilience *deterministically*.
- **Close the loop:** mine real user questions → refine context → measure again. The semantic layer is a living artifact.
- This is the [[claude-md-12-rules/_index|read-before-write / context-discipline]] philosophy, expressed as a *product* data layer.
