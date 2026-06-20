# Tool design and sizing

## Source

First-party: [omni.co — Building Omni's architecture for agentic analytics](https://omni.co/blog/building-omnis-architecture-for-agentic-analytics). Talk-recap (45-tool portfolio, "Blobotomy 2", per-query attempt counts): T2 — see [[agentic-analytics-harness/source-provenance]]. "Design and size their tools" is named explicitly in Anthropic's video description [T1].

## The 4 core tools (first-party) [T1]

Omni's blog describes the system around **four core tool types**:

1. **Topic picker + query tool** — inspects metadata across **Topics** (the semantic-layer unit), makes an *informed choice* about which Topic to use, then generates SQL. Picking the right Topic *before* writing SQL is the first correctness gate.
2. **Field values tool** — fetches the list of **valid field values** so the agent can "adjust to find the correct match." (e.g. user says "Europe" → tool returns `["EMEA","NAM","APAC"]` → agent maps to `EMEA`.) This is **typo/fuzzy resilience as a tool**, not a prompt instruction.
3. **Summarization tool** — the context-isolating sub-agent (see [[agentic-analytics-harness/multi-agent-architecture]]).
4. **Query execution** — runs the SQL.

## The 45-tool portfolio (matured) [T2 — talk recap]

The talk recap cites a **45-tool** portfolio covering query generation, **dashboard creation**, **visualization**, **validation**, and **data modeling**.

> **Reconciliation (Rule 7 — surfaced, not blended):** "4 core tools" (blog, ~Aug 2025) and "45 tools" (talk, May 2026) are **not a contradiction** — they are different *granularity* at different *times*. The blog names the 4 load-bearing tool *categories*; the talk reports the full matured count after 18 months. Treat **4 as the conceptual skeleton** and **45 as the production reality.** Exact count is single-source.

## "Blobotomy 2" — SQL over a custom format [T2 — talk recap]

- **What they had:** a **proprietary JSON query format** the model had to be taught.
- **The insight:** teaching Claude a *novel* syntax imposes unnecessary **cognitive load** — the model spends capability learning your DSL instead of solving the problem.
- **The switch:** generate **SQL**, which **Claude already knows from training.**
- **The payoff:** **"3–4 attempts needed per query → 1 attempt"** after the transition.
- **Bonus alignment:** the specific SQL Claude favors (**CTEs**) matched Omni's parser strengths, compounding the gain.
- **Principle:** **leverage the model's existing knowledge; prefer model-native formats over bespoke ones.**

## The data-format constraint [T1]

- SQL results come back in **Arrow format with non-serializable types.**
- They **must be transformed into CSVs** before being re-introduced into the conversation (the model can't consume Arrow's non-serializable types directly).
- And you **never dump full result sets** into context anyway — too expensive, and it **breaks prompt caching** (see [[agentic-analytics-harness/evals-and-error-recovery]] + [[claude-api-cost-optimization/_index]]). Summarize first.

## Sizing principles (synthesized)

- **Size a tool to a decision the agent actually makes.** "Pick a Topic," "resolve a field value," "summarize a big result" are each a discrete decision → each its own tool.
- **A tool can encode a correctness gate** (Topic-pick-before-SQL; valid-value lookup) that you'd otherwise hope the prompt enforces.
- **Prefer formats the model already speaks** (SQL, standard JSON) — a custom format is a hidden tax measured in retries.
- **Keep result payloads small** — transform (Arrow→CSV), cap, and summarize before re-entry, to protect both context budget and prompt caching.

## Key Takeaways

- **Model-native > bespoke** is the single most quantified lesson in the talk (**3–4 → 1 attempt**). If you're inventing a DSL for an agent, check whether the model already knows a standard equivalent.
- **Tools are where you put correctness**, not just capability — field-value lookup and Topic-picking are *guardrails shaped like tools*.
- **"4 core / 45 total"** — start with a small, conceptually-clean tool set and let it grow with evidence; don't ship 45 on day one.
- **Plan for serialization** at the data boundary (Arrow→CSV) and for **caching-safe** payload sizes from the start.
