# Overview — Omni's Blobby: the best agentic analytics harness

## Source

- **Video:** [Building the best agentic analytics harness: Powered by Claude, built with Claude Code](https://www.youtube.com/watch?v=K4-flzsPraE) — Claude (Anthropic) channel, 2026-05-21, 26:46.
- **Speaker:** Chris Merrick, Cofounder & CTO, **Omni** (BI/analytics platform). Talk given at **Code with Claude: Extended London**, 2026-05-20 (Founder stage, 11:30 AM).
- **Companion first-party:** [omni.co — Building Omni's architecture for agentic analytics](https://omni.co/blog/building-omnis-architecture-for-agentic-analytics) + [omni.co — Improving AI quality with context](https://omni.co/blog/improving-ai-quality-with-context).
- ⚠️ Video is **uncaptioned**; this is triangulated, not transcribed → [[agentic-analytics-harness/source-provenance]]. Raw: `raw/(C) 2026-06-20-omni-agentic-analytics-harness.md`.

## What it is

- **Omni** = an analytics/BI platform. **Blobby** = its embedded **agentic analytics assistant** — you ask a business question in natural language; Blobby plans, writes SQL, runs it, validates, summarizes, and can build dashboards.
- It is a **harness**, in exactly the [[harness-engineering/_index|harness-engineering]] sense: the model supplies intelligence; the *harness* (tools, semantic layer, loops, validation, error recovery, evals) supplies **control**.
- The corpus angle: every prior harness article was about **coding** agents. **Blobby is the first *product* harness** — a customer-facing feature, not a dev workflow. The same principles transfer.

## The numbers (one table)

| Metric | Value | Tier |
|---|---|---|
| Platform code written with Claude Code | **99%** | T1 (Anthropic desc) |
| Production token consumption | **103.3B / month** (Apr 2026), up from **1.2B/month** (Aug 2025) | T2 recap, 103.3B cross-confirmed |
| Engineering team | **~30 engineers** | T2 recap |
| Time to production | **18 months** | T2 recap |
| Tool portfolio | **4 core tool types** (first-party) → **45 tools** (matured) | T1 / T2 — see [[agentic-analytics-harness/tool-design-and-sizing]] |
| Outer-loop iteration cap | **50** with checkpoint recovery | T2 recap |
| Major architectural rewrites ("Blobotomy") | **~5** | T2 recap |
| Semantic-context budget | **~200k chars total, ~175k for semantic layer** | T1 (Omni blog) |
| Model hosting | AWS Bedrock-hosted Claude (Haiku→Sonnet migration) | T1 / T2 |

## Five engineer-applicable principles

1. **Colocate context with its definitions.** Business context lives *in the semantic layer next to the data*, not in a giant global prompt. (Analogy Merrick draws: `CLAUDE.md` stores *code* context; the semantic layer stores *data* context.) → [[agentic-analytics-harness/semantic-layer-as-context]]
2. **Invest heavily in error messages.** High-quality errors ("what happened" + "how to fix") + retry budget + taught recovery strategies = the **highest-ROI** quality lever they found. → [[agentic-analytics-harness/evals-and-error-recovery]]
3. **Don't fragment knowledge across agent boundaries.** Splitting "planner" and "query-writer" into separate agents created silos and infinite loops. Keep information + execution in the same layer. → [[agentic-analytics-harness/multi-agent-architecture]]
4. **Use model-native formats.** Teaching Claude a custom JSON query DSL cost 3–4 attempts/query; switching to **SQL (which Claude already knows)** cut it to **1 attempt**. → [[agentic-analytics-harness/tool-design-and-sizing]]
5. **Prioritize trace observability.** Reading raw traces ("why did *this* fail") beats staring at aggregate scorecards. → [[agentic-analytics-harness/evals-and-error-recovery]]

## Five production lessons (Omni's own framing)

1. **Demo ≠ production.** "Text-to-SQL looks cool in a demo, but rarely makes the jump to production."
2. **AI optimism is a risk.** "LLMs are optimistic. Even when you leave out crucial context, they'll still try to help" — so they answer *confidently wrong*. The harness must catch this.
3. **Foundations first.** "Maniacally focused on quality before we even decided to evolve our AI assistant."
4. **Security is non-negotiable.** The agent "can only ever run **as the current user**" — it inherits Omni's existing permissions, never escalates.
5. **Trust over cleverness.** "We chose the hard path because it's the only way to engineer a system that respects your permissions and definitions at every step."

## Key Takeaways

- The headline isn't "AI writes SQL" — it's that **a disciplined harness around a general model beat purpose-built text-to-SQL** for production analytics.
- **The semantic layer is the moat.** Generic LLM + business-context-in-the-semantic-layer = "AI-native platform"; that colocated context is what makes answers trustworthy.
- **Error recovery, not prompt-wording, was the biggest quality win** — a counter-intuitive, transferable finding.
- **Cost discipline is structural:** they rely on prompt caching and never dump full result sets into context (summarize first). Same levers as [[claude-api-cost-optimization/_index]], proven at 100B-tokens/month scale.
- **Dogfooding compounds:** the CTO lives in Claude Code daily, so he could "design a good harness for Blobby." Toolmakers as primary users.
- For the operator's **Goal #2 (build software with these tools)**, Blobby is the closest published blueprint to a "talk-to-your-data" feature — directly relevant to **hireui** (external repo: TalentAxis recruitment SaaS). See `output/(C) 2026-06-20-agentic-analytics-harness-pilot-methods.md`.
