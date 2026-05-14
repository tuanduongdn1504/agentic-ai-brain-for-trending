# Autonomous Loops with Human-in-the-Loop — Gaps & Follow-ups

> **Topic:** [[_index|autonomous-loops-human-in-the-loop]]
> **Source:** `../../raw/2026-05-13-auto-loop-goals-with-human-in-the-loop.md` § Gaps

> ⚠️ **READ THIS FIRST — signal-quality warning.** The auto-selection rubric for this bundle had to **relax the recency filter** to fill 6 slots, which pulled in generic 2025 explainer videos (IBM, codebasics, CNN) instead of the dialed-in content the topic was supposed to surface (Karpathy autoresearch, Ralph Wiggum loop, plan-mode + grill cycles, paperclip governance, confidence-threshold interrupts). **Treat this topic as a thin first pass and re-run with a tighter query before relying on it.**

---

## What the bundle actually delivered

Looking at the 6 sources honestly:

| Source | Channel | What it actually covers | Signal for this topic |
|---|---|---|---|
| 1 | Collaboration Simplified | Microsoft Copilot Workflows tutorial | Medium — drafts-not-sends demo |
| 2 | The Coding Sloth | "500 hours with AI coding" generalist | Medium — decomposition + verification rules |
| 3 | Greg Isenberg / Remy Gasil | Building AI agents full course | **Highest** — observe-think-act, context engineering, scoped access |
| 4 | IBM Technology | Generative vs Agentic AI explainer | Low — vendor-flavoured definitions |
| 5 | codebasics | "What is Agentic AI" explainer | Low — vendor-flavoured definitions |
| 6 | CNN | AI emergent behaviour / alignment journalism | Medium — safety framing of HITL, but not mechanics |

**Two sources (1 and 3) actually engage with HITL mechanics. Three sources (4, 5, partially 1) are explainers. One source (6) is journalism.** This is the recency-filter relaxation showing up in the output.

---

## What the topic was supposed to surface but didn't

The topic title "Auto-Loop Goals with Human-in-the-Loop" and the query `autonomous agent goal driven loop human in the loop self correcting Claude 2026` were aimed at the dialed-in genre. None of the following — which are the actual canonical references — appear in the bundle:

### Karpathy autoresearch loop

- Karpathy's framing of LLMs as **research-process executors** that maintain incrementally-compounding state
- The "wiki-as-codebase, LLM-as-programmer" pattern (the foundation of this autopilot-research vault itself)
- The discipline of **continuous-summary** + **lazy-ADR** + **structured-state-update** that distinguishes autoresearch from chat
- **None of the 6 sources mention this by name or by pattern.**

### Ralph Wiggum loop

- The Ralph loop: agent runs **autonomously on a single goal with periodic checkpoint-and-resume**, named after the "I'm going to keep doing this" character
- The pattern of operator returning to a converged-state rather than a half-state
- **None of the 6 sources mention this.** Existing coverage lives in [[../workflow-ai-coding/_index]].

### Plan-mode + grill cycles

- Claude Code's `/plan` mode as an **explicit HITL checkpoint surface**
- The "grill the docs" pattern — adversarial questioning of a plan before execution
- **Not addressed** by any source.

### Paperclip-style governance

- Bounded-autonomy patterns from the harness-engineering literature (Lopopolo et al.)
- Explicit budget caps, blast-radius limits, escalation triggers
- The CNN source ([Source 6]) **gestures at the safety angle but doesn't describe governance mechanics**

### Confidence-threshold interrupts

- Interrupt-based agents that pause and wait for human OK when confidence drops below a threshold for a high-risk action
- **Explicitly flagged as a gap in the raw bundle's own gaps section (§ "Follow-up topics #6")** — the bundle knows it didn't cover this

### Specific to autonomous orchestration

- **No source covers:** Claude Code `--dangerously-skip-permissions` discipline, the cron / loop / schedule primitives, the autopilot-research routine v2.1, or any specific harness's HITL surface
- The bundle is **vendor-neutral and platform-generic**, which is precisely the wrong fit for an autopilot wiki

---

## Other gaps the raw bundle itself identified

From the raw bundle's own § Gaps (these are gaps in the *source content* even on its own terms):

### Cost management / token budgeting

- Multi-turn loops and Chain of Thought reasoning have **exponential cost** in production
- A single user request can trigger dozens of expensive frontier-model calls
- **No source quantified this**

### Observability and tracing

- Production loops need distributed tracing
- If an agent fails on step 7 of 10, you need to log state + tool output + LLM reasoning for that specific execution
- Remy Gasil shows local "thinking process" UI [Source 3] but no production-scale answer

### Concurrency / state at scale

- Examples are 1-user / 1-agent
- `memory.md` doesn't scale to 1000 concurrent users / millions of preferences
- No coverage of database-backed memory at production scale

### Tool-call hallucinations and guardrails

- Agents can hallucinate **non-existent tool calls** in production
- Sources lack a framework for intercepting and validating agent outputs before destructive actions execute
- The Coding Sloth's "verification via tests" [Source 2] is a partial answer but not complete

### RBAC for production agents

- Remy Gasil's "read-only access" [Source 3] is the only access-control discussion
- Production agents need role-based access — e.g., HR agent must verify the *asker's* clearance, not just have HR-API access

---

## Follow-up topics for the next autopilot loop

Ranked by expected information density for **this specific topic**:

### Tier 1 — re-run the same topic with a tighter query

**Recommended new query:**
```
Karpathy autoresearch Ralph loop human checkpoint goal driven Claude Code plan mode grill
```

Constrain to:
- **Recency filter: tight (≤ 6 months)** — do not relax this
- Channels: prefer Karpathy, harness-engineering creators, Claude Code-specific channels over IBM / CNN / vendor explainers
- Exclude: generic "What is Agentic AI" explainer videos

### Tier 2 — adjacent topics worth their own bundle

1. **Production observability for agentic loops** — LangSmith, Arize Phoenix, OpenTelemetry for AI
2. **LLM evaluation frameworks for agent reliability** — RAGAS, Promptfoo, "golden dataset" testing
3. **Output guardrails** — NeMo Guardrails, Guardrails AI, schema-validation layers
4. **Multi-agent orchestration** — AutoGen, CrewAI, LangGraph (the bundle gestures at sub-agents but doesn't go deep)
5. **Vector-db-backed long-term agent memory** — Pinecone, Weaviate, Milvus as scaling answer when `memory.md` outgrows itself
6. **Confidence-threshold HITL patterns** — interrupt-based UI/UX for when the agent should ask vs act

### Tier 3 — pre-existing wiki coverage worth re-reading

Before re-running the autopilot, **read these existing topics in this wiki** — they cover what this bundle missed:

- [[../workflow-ai-coding/_index]] — Ralph loop, planning-first patterns
- [[../harness-engineering/_index]] — bounded autonomy, Lopopolo framing
- [[../claude-md-12-rules/_index]] — Rule 4 (goal-driven), Rule 10 (checkpoint discipline)
- [[../claudekit/_index]] — workflow primitives
- [[../claude-code-hooks/_index]] — `pre-tool-use` as a deterministic HITL substitute
- [[../10x-claude-code/_index]] — productivity patterns when loops actually work

These four/five topics together probably **cover 80% of what the present bundle was supposed to but didn't**.

---

## What to do with this topic going forward

Pragmatic options:

1. **Mark this topic provisional** — leave it in place but link the re-run output here when it lands
2. **Re-run before action** — don't act on these takeaways operationally until the tighter-query re-run is in
3. **Use this as a control** — when the re-run lands, diff the two topics; the differences are exactly what the recency filter was hiding

The librarian routine should probably add a **post-condition check** to the auto-selection: if the recency filter is relaxed, **flag the resulting bundle as provisional** in the topic frontmatter automatically.

---

## Key Takeaways

- The bundle is **provisional** — the recency filter relaxation pulled in generic explainer content over dialed-in autoresearch / Ralph-loop / HITL-mechanics content
- **Two of six sources** (Remy Gasil [Source 3], Microsoft / Shervin Shaffy [Source 1]) actually engage with loop mechanics; the rest are explainers, journalism, or vendor positioning
- **Karpathy autoresearch, Ralph loop, plan-mode + grill cycles, paperclip governance, confidence-threshold interrupts** — all explicitly absent
- **Re-run query recommended:** `Karpathy autoresearch Ralph loop human checkpoint goal driven Claude Code plan mode grill` with a tight (≤ 6 months) recency filter and explainer-channel exclusion
- Production gaps the bundle didn't even pretend to cover: cost / observability / concurrency / RBAC / tool-call guardrails — each merits its own future topic
- **Existing wiki topics** ([[../workflow-ai-coding/_index]], [[../harness-engineering/_index]], [[../claude-md-12-rules/_index]]) likely cover more of the intended ground than this bundle does — read those first
- **Routine improvement suggestion:** auto-flag any bundle where the recency filter had to be relaxed as `provisional: true` in topic frontmatter
