# Langfuse deep-dive + harness-tool status check (LangGraph, LangChain, PydanticAI)

## Source

Deepening-pass-3 Workflow: `dive:langfuse` + `verify:langfuse` (refute-first) and `dive:harness-tools` + `verify:harness-tools` (refute-first). All verdicts below are the **verifier's** conclusion, not the dive's raw claim — where the two disagreed, the verifier's primary-source check wins (Rule 12). See [[source-provenance]] for token/tool-call counts.

## Langfuse — verified

**What it is:** an open-source LLM observability and AI-engineering platform (tracing + evaluation + prompt management). MIT-licensed, except the `ee/` (enterprise edition) folders in the GitHub repo.

**History:**
- Founded 2022 by Clemens, Max, and Marc Klingen (Marc = co-founder/CEO)
- Accepted into **Y Combinator W23**, November 2022
- **$4M seed round, September 2023** — investors **Lightspeed Venture Partners, La Famiglia, and Y Combinator** (a dive-agent draft had mis-added "General Catalyst" to this list; the refute-first verifier caught it against the official handbook — REFUTED, corrected here)
- Public launch as "Product Analytics for LLM Apps," July/August 2023
- **Acquired by ClickHouse, January 16, 2026** — Langfuse's own blog post states it "stays open source" post-acquisition. This is the one genuinely new fact this deepening pass surfaced; not previously in this corpus.

**Pricing:** Hobby / Core / Pro / Enterprise tiers (self-hosting is free at any tier); an optional Teams add-on at +$300/month unlocks SSO and fine-grained access control.

**Tracing/observability features (confirmed):** a traces → spans → sessions data model; token and cost tracking including input, output, and cache-read tokens; cost inference across OpenAI, Anthropic, **and Google Gemini** (not just the two the video implies).

**Eval features (confirmed):** LLM-as-judge with pre-built templates (official docs name Hallucination, Context-Relevance, Toxicity, and Helpfulness as examples — the docs do **not** publish an exhaustive template list, so don't cite a fixed count), datasets, experiments, and prompt versioning.

**Correction — a feature that is NOT yet shipped:** the dive's draft implied experiments can be pinned to a specific dataset *version* while a team keeps editing the live dataset. The verifier checked Langfuse's own experiments docs directly: **experiments always run against the latest dataset version at experiment time**, and the docs state version-pinning "will be added shortly" — i.e. it's on the roadmap, not live. Don't cite version-locked experiments as a current capability.

**vs. LangSmith:** Langfuse's own comparison page positions itself as the open-source alternative — self-hostable, and a more generous free tier (Langfuse: 50K events/month vs. LangSmith: 5K, per Langfuse's own numbers, which is a self-interested source and worth an independent re-check before quoting in anything customer-facing). For the LangSmith side of this comparison at genuine depth (evaluations, Deployments, Sandboxes, Context Hub, LLM Gateway, SmithDB internals), see the existing [[../agent-development-lifecycle/langchain-interrupt-26-anchor]] — that pass already has 150M+ traces/week and 6×–15× perf-gain figures from a LangChain-run keynote.

**Unverifiable (flagged, not asserted):** a claimed "100+ framework integrations" count — the official integrations page describes broad coverage but does not publish a number; user-segmentation feature details were not independently confirmed from the docs pages fetched.

## Harness tools — verified

**LangGraph** — actively maintained; v1.2.9 released 2026-07-10; ~37.2K GitHub stars. It has become **the orchestration runtime** for the LangChain ecosystem, replacing the now-deprecated `AgentExecutor`. LangChain now positions itself as the higher-level API layered on top of LangGraph's runtime.

> ⚠️ **Fabricated-date catch:** an earlier dive draft claimed "LangGraph reached general availability October 22, 2025." The refute-first verifier checked the GitHub releases API directly and found **zero releases in October 2025** — the earliest visible releases are from January 2026. This date is unverifiable at best, confabulated at worst. **Do not cite it.** This is the same stale/hallucinated-date failure mode this corpus has caught repeatedly in other topics (Rule 12 — the verify layer working as designed).

**LangChain** — still actively maintained; official docs confirm the "LangChain (high-level API) over LangGraph (runtime)" layered positioning.

**PydanticAI** — the video says "Pydantic," but the tool being described (an agent-building framework, not the base validation library) is almost certainly **PydanticAI**, a separate project by the Pydantic team.
- Launched **December 2, 2024** (confirmed via Simon Willison's contemporaneous blog post)
- v1.0 released **September 5, 2025** (a dive draft said Sept 4 — off by one day, corrected here)
- v2.0 released **June 23, 2026**; v2.9.0 around **July 10–11, 2026**
- ~18.5K GitHub stars, 281 releases — actively maintained, current as of this pass

**Unverifiable:** an "AgentExecutor migration deadline of December 2026" and LangGraph's exact open-PR/release counts could not be independently pinned down from the sources fetched — treat as approximate, not authoritative.

## Key Takeaways

- Langfuse is real, well-funded (YC W23 → $4M seed → ClickHouse acquisition Jan 2026), and open source (MIT core) — a legitimate open-source alternative to LangSmith, not a toy.
- Two corrections were caught by adversarial verification on this pass's own research, not on the video: a wrong investor name, and a not-yet-shipped dataset-versioning feature. Neither originated from the video — the video just said "LangFuse, LangSmith" as tool names with no further claims to verify.
- LangGraph/LangChain/PydanticAI are all real, current, and actively maintained as of mid-2026 — but a specific "October 2025 GA" date for LangGraph should be treated as unverified/likely wrong wherever it's encountered.
- "Pydantic" as a named agent-harness tool is corpus-shorthand for **PydanticAI** — flag this ambiguity if it recurs in future ingests rather than assuming which product is meant.
