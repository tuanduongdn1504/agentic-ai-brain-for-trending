# Agent Dashboard / Agent OS — Gaps & Follow-ups

> **Topic:** [[_index|agent-dashboard-os]]
> **Source:** `../../raw/2026-05-13-agent-dashboard-agent-os-claude-code-observability.md` § Gaps

What the 6-video bundle did NOT cover. One speaker explicitly notes their walkthrough is an **"alpha version"** and that they are only **"scratching the surface"** of what production needs [Source 1].

---

## Gap 1: Cost governance dashboards

Multiple speakers highlight that running these systems can "burn a hole in your wallet" due to high API usage [Source 1, Source 2]. However:

- **No detailed framework** is provided for **token quotas**, budget alerts at a per-user level, or cost-optimization strategies for long-running agent threads [Source 1, Source 2]
- The bundle shows you the cost **per trace step** in LangSmith [Source 5] but stops short of building cost-aware dashboards

**Follow-up question:** How do mature teams build per-user token quotas, per-feature budget alerts, and cost-attribution dashboards for agent workloads?

**Follow-up search:** "LLM cost governance dashboard", "per-user token budget agentic", "OpenTelemetry cost attribution LLM"

---

## Gap 2: PII redaction and prompt-injection mitigation

While "Row Level Security" (RLS) is used to isolate user data [Source 1], and sandboxes are used for code execution [Source 2, Source 4], the bundle does **not** cover:

- **PII (Personally Identifiable Information) redaction in logs** — the trace tool sees everything; how do production teams scrub it? [Source 1]
- **Prompt injection** mitigation beyond basic firewalls [Source 1]

**Follow-up question:** What's the production-grade pattern for PII-safe agent traces, and what real-world prompt-injection defenses go beyond input sanitization?

**Follow-up search:** "LangSmith PII redaction", "agent trace pseudonymization", "prompt injection defense in depth 2026"

---

## Gap 3: Rigorous evaluation methodology — "golden datasets"

Tools like LangSmith are showcased for tracing [Source 1, Source 5], but the bundle lacks a comprehensive guide on:

- Building a **"golden dataset"** for benchmarking [Source 1]
- A formal **regression test suite** — one speaker admits manual testing becomes a "monumental task" as features grow [Source 1]
- **LLM-as-a-judge** evaluation — Daniel mentions **DeepEval** as a future topic but doesn't dive in [Source 1]

**Follow-up question:** How do mature teams construct golden datasets and automate scoring of agent responses for helpfulness, conciseness, and hallucinations?

**Follow-up search:** "DeepEval LLM judge", "agent regression test suite", "golden dataset construction RAG"

---

## Gap 4: UX for non-deterministic failures

The videos focus on successful tool calls but offer limited discussion on **defensive UX design**:

- How to **gracefully handle model timeouts** [Source 1]
- **Partial agent failures** in a multi-agent team [Source 1, Source 2]
- Explaining "thinking" states to non-technical users in a way that **builds trust** [Source 1]

**Follow-up question:** What UI/UX patterns exist for surfacing partial failures, retries, and "thinking" states in agent dashboards?

**Follow-up search:** "agent UI partial failure", "thinking state UX LLM", "non-deterministic UX patterns"

---

## Gap 5: Release management and database migrations

The sources largely demonstrate building on a single "main" Git branch for simplicity [Source 1]. They lack a detailed exploration of:

- **Release trains** for agent deployments [Source 1]
- Managing separate **dev/staging/production** environments [Source 1]
- Handling **database migrations** during automated deployments [Source 1]

**Follow-up question:** What does CI/CD look like for an agent OS — specifically, "Blue-Green" deployments for LLM apps where you test a new model version or prompt strategy against a subset of traffic before full rollout?

**Follow-up search:** "blue-green deployment LLM", "agent CI/CD pipeline", "prompt rollout strategy"

---

## Gap 6: Prompt versioning and registry management

Sources show prompts being edited in markdown or code files [Source 1, Source 2]. For production:

- **Prompt CMS** tools or LangSmith's prompt library for **version-controlling prompts independently** of application code [Source 5]
- The bundle doesn't walk through how this looks in practice

**Follow-up question:** How do production teams version prompts independently from app code, manage rollback, and run A/B tests on prompts?

**Follow-up search:** "LangSmith prompt registry", "prompt CMS production", "prompt versioning A/B"

---

## Gap 7: Sandbox resource limits

While E2B and Vercel Sandbox are mentioned for safety [Source 2, Source 4], the bundle doesn't address:

- **Hard compute limits (CPU/RAM/Network)** for agents [Source 2, Source 4]
- Preventing a "rogue agent" from consuming excessive cloud resources [Source 2]
- Catching agents stuck in **infinite loops** [Source 2]

**Follow-up question:** How are hard resource limits enforced inside E2B and Vercel Sandbox, and what monitoring/auto-kill patterns exist for runaway agents?

**Follow-up search:** "E2B resource limits", "Vercel Sandbox CPU memory", "agent kill switch infinite loop"

---

## Gap 8: Human-in-the-Loop (HITL) pause primitives

For high-stakes actions (the "order a laptop" example [Source 3]), there's no walkthrough of:

- **Interruptible agents** [Source 1]
- How to pause an agentic workflow to require **manual human approval** before final tool execution [Source 1]
- Where the approval UI lives in the dashboard

**Follow-up question:** What HITL patterns exist in production — specifically, the UX flow from "agent paused for approval" to "human approved, agent resumed"?

**Follow-up search:** "human in the loop agent pause", "LangGraph interrupt", "approval workflow LLM"

---

## Gap 9: Semantic caching for cost reduction

To mitigate the "wallet burn" mentioned by IndyDevDan [Source 2], the bundle doesn't cover:

- **Semantic caching** (e.g., Redis or GPTCache) [Source 1, Source 2]
- Storing previous LLM responses for similar queries to reduce redundant API calls and latency

**Follow-up question:** What's the production pattern for semantic-similarity cache lookup in front of an agent's LLM calls, and where does the cache surface in the dashboard?

**Follow-up search:** "GPTCache production", "semantic cache Redis LLM", "agent response cache hit rate"

---

## Gap 10: The "Chase AI / Claude Code dashboard" anchor

The autopilot topic prompt referenced an anchor video titled **"Claude Code Just Got a Dashboard"** (Chase AI) at `https://www.youtube.com/watch?v=7zxIeRWasbc`. **None of the 6 sources in the bundle are this video.** The bundle covers adjacent territory (LangSmith, Tmux, sandboxes, agentic RAG) but does **not** contain a direct walkthrough of a Claude-Code-specific dashboard product.

**Follow-up question:** What does the Claude Code-native dashboard (if one exists in May 2026) actually look like, and how does it compare to the LangSmith/OpenTelemetry/Tmux stack the bundle describes?

**Follow-up search:** Chase AI "Claude Code Just Got a Dashboard" walkthrough, Anthropic Claude Code official dashboard 2026, claudekit dashboard module — see [[../claudekit/_index]]

---

## Recommended follow-up topics for the next autopilot loop

Topics ranked by promised information density (high → low):

1. **Claude Code-native dashboard** (Chase AI anchor, plus any official Anthropic surface) — closes the biggest gap vs the topic title
2. **LLM cost governance dashboards** — explicit per-user quotas, budget alerts, cost attribution
3. **Golden datasets and LLM-as-a-judge (DeepEval)** — production evaluation methodology
4. **HITL pause patterns** — interruptible agents, approval UIs
5. **Semantic caching architectures** — GPTCache, Redis-based agent response cache
6. **Prompt registry / CMS** — LangSmith prompt library, prompt rollback, A/B testing
7. **PII redaction in agent traces** — production data-privacy patterns

Add these to `raw/topics-queue.md` for the next `/loop` or cron run.

---

## Key Takeaways

- **Cost governance, golden datasets, HITL, and prompt registry are the four biggest production gaps** the bundle leaves open [Source 1, Source 2]
- **PII redaction and prompt-injection mitigation** are mentioned but not solved — production deployment requires research beyond this bundle [Source 1]
- **The bundle's anchor video** (Chase AI's "Claude Code Just Got a Dashboard") **is not present in the sources** — biggest gap vs the topic title, queued for next loop
- **Sandbox resource limits** are assumed but not documented — open question for any team running E2B or Vercel Sandbox at scale [Source 2, Source 4]
- **DeepEval** is name-checked as a future topic but not explored — queue for follow-up [Source 1]
- 10 specific follow-up topics queued for the next autopilot run — see ranked list above
