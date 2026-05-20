# LangChain Interrupt 2026 — Agent Development Lifecycle anchor

> **Source:** [The Agent Development Lifecycle: Build, Test, Deploy, Monitor | Interrupt 26](https://www.youtube.com/watch?v=jWy39wavbjY) — Harrison Chase (LangChain co-founder/CEO) + Ankush Gola (LangChain co-founder/CTO), 44:58, uploaded 2026-05-19, ~1.9K views as of 2026-05-20.
> **Raw:** `raw/2026-05-19-langchain-interrupt-26-adl-transcript.md` (905 caption segments, ~7.7K words; clean VTT)
> **Compiled:** 2026-05-20
> **Status:** N=1 single-source anchor for new topic [[_index|agent-development-lifecycle]]

This is LangChain's second annual Interrupt conference keynote. Last year framed building agents as hard; this year frames the discipline that companies have figured out to do it reliably: **the Agent Development Lifecycle (ADL)** — a 4-phase loop parallel to but distinct from SDLC.

The keynote is structured around 6 product launches positioned as tools for each ADL phase, plus a 15-min architectural deep dive from CTO Ankush Gola on **SmithDB** (see sibling article [[smithdb-architecture]]).

---

## The framing claim: why agents need their own lifecycle

At `[02:36]–[03:39]` Harrison argues agents differ from software along two axes:

1. **Input space is infinite.** Natural language has unbounded dimensions; multimodal inputs (images, video, audio) compound this. "The input space to agents is really, really large."
2. **Output is non-deterministic and prompt-fragile.** "LLMs are non-deterministic, and even if they were deterministic, they're still really sensitive to small changes in the prompt."

Combined → "you end up with an overall agentic system that's really hard to predict how it's going to do before you actually launch it." Conclusion at `[03:41]`: *"The teams that have figured out how to build agents reliably, they ship early and then they iterate quickly."*

This positions the ADL as **the iteration-flywheel framework** — not a waterfall lifecycle but a continuous loop. The 4 phases are Build → Test → Deploy → Monitor, with **traces sitting at the center**.

---

## Phase 1 — Build

### The core agent definition

At `[06:09]–[06:34]` Harrison gives the cleanest definition of "agent" so far in the corpus:

> *"It's an LLM running in a loop calling tools. There's a bunch of stuff that can happen around that loop. There's a bunch of specific tools you can add in. But when people talk about agents, this is essentially what they're talking about."*

This is consistent with [[external|harness-engineering/tejas-kumar-anchor|Tejas Kumar's 5-component decomposition]] (where the agent loop is component 5 of 6) — both place the loop as the core but explicitly distinguish "agent = loop" from "harness = stuff around the loop".

### Deep Agents = an agent harness (cross-anchor terminology adoption)

At `[06:35]–[08:09]` Harrison defines Deep Agents — LangChain's flagship — explicitly as an **agent harness**:

> *"Deep agents is an agent harness. And it basically adds more batteries-included things. It supercharges this loop."*

What Deep Agents adds to the agent loop:
- **Execution environment** — spectrum from sandbox (full code exec) to virtual file system (database exposed as filesystem; "LLMs are great at reading and writing files, so you can kind of trick it into having this kind of mock execution environment" `[07:25]`)
- **Context management** — skills, memory, summarization, context offloading, prompt caching ("built into the harness, automatically" `[08:07]`)
- **Steering / HITL controls** — "they're long horizon agents, but that doesn't mean they're fully autonomous"
- **Delegation** — sub-agents, planning agents, task agents; harness specifies communication

This is **the first observed instance** of a major framework vendor (LangChain) adopting Tejas Kumar's "agent harness" framing terminology end-to-end. Compare against [[external|harness-engineering/terminology|harness-engineering/terminology]] where the term was established via Lopopolo (org-scale) — here it's productized at a sibling abstraction level. Strong corroboration signal for the Tejas anchor's promotion criteria.

### Deep Agents 0.6 launch — 3 trend-driven features

At `[09:03]–[12:24]` Harrison ties 3 product additions to 3 industry trends:

| Trend | Product addition |
|---|---|
| **Rise of open models** (DeepSeek V4 "just launched last week, as performant on certain tasks as frontier models" `[09:19]`; frontier costs rising) | Native support for GLM5, DeepSeek, Nemotron; integrations with Fireworks, Base10, NVIDIA; `deep agents code` open-source coding agent example "really, really good for open source models" |
| **Execution environment attention** (virtual FS one extreme, full sandbox other) | **CodeInterpreter** middle ground using QuickJS (JavaScript runtime subset; can write/exec code, manipulate data files, read/write filesystem, but no Docker; lightweight + multi-tenant deployable, doesn't require separate sandbox per agent) |
| **Delightful UIs still hard** (agents emit text, tool calls, images, reasoning, sub-agents — complex event streams) | New streaming protocol + 4 frontend SDKs + partnerships with **CoPilotKit, Assistant UI, Vercel** |

The DeepSeek V4 callout is **time-sensitive corpus evidence** — a frontier-competitive open model launched within ~1 week of the conference, suggesting the open-model trend is accelerating. See [[recommended-trending-topics|trending topics]] in this article's tail.

---

## Phase 2 — Test

At `[12:40]–[13:33]` Harrison summarizes LangSmith evaluations (2 years of building):

- Build datasets (reference inputs/outputs OR criteria for scoring)
- Define metrics (correctness, hallucinations, use-case-specific)
- Run agent over datasets, score on metrics, create experiments
- Use experiments for **hill-climbing** (improvement) OR **regression prevention** (stability)

No new launches in this phase from the keynote — but Harrison notes more announcements coming later (which become LangSmith Engine + SmithDB).

This phase aligns with [[external|harness-engineering/core-claims|Lopopolo's claim about test-driven harness work]] but is more granular: datasets + metrics + experiments as explicit primitives rather than just "tests run in CI".

---

## Phase 3 — Deploy

At `[13:37]–[14:08]` Harrison identifies 4 production challenges that emerge after local development:

1. Single user → many users (env vars, memory must be per-user)
2. Open access → auth-controlled access
3. Local crash recovery → durable execution at scale

Existing solution: **LangSmith Deployments** (launched ~1 year ago). 30 API endpoints (streaming, HITL, auth, etc.). "Single standard deployment pattern." 100M+ agent runs served. Customers: **Workday, Cisco, Etsy, Podium, ByteDance.**

### New launch 1: LangSmith Sandboxes (generally available)

`[15:01]–[16:07]`. Execution environments as a service.

- **Spin up in <1 second**
- Persistence across interactions
- Snapshots and forks
- **Auth proxy outside sandbox** — keeps API keys hidden from the LLM. "If you wanna give the LLM the ability to use something that requires an API key, you don't actually want it to see that API key because then it could get prompt injected and leaked it. And so we have an off proxy that sits outside the sandbox and basically intercepts traffic and inserts that in." `[15:25]`
- Framework-agnostic (works with Deep Agents OR without; testing, RL, production agents)
- Used by Monday (AI sidekick)

The **auth proxy pattern** is corpus-first as a discrete primitive — Tejas Kumar's [[external|harness-engineering/tejas-kumar-anchor|loginHandler]] demonstrated the principle (harness has secrets, agent doesn't); LangChain has formalized it into a productized middleware layer. Two independent corroborations of the same architectural stance within 2 days (Tejas 2026-05-17, Harrison 2026-05-19).

### New launch 2: LangSmith Context Hub

`[16:07]–[18:42]`. **Karpathy LLM Wiki gets explicit corporate productization.**

- Stores `agents.md` files, skills, **LLM wikis** ("this thing that Karpathy did where he basically ran an LLM and had it generate wikis, which are condensed knowledge in markdown files. We think that's gonna become a more and more common pattern" `[17:23]`)
- Versioning, tags, comments
- Pull-down to local CLI, deep agents (as virtual file system), or any agent harness

Harrison positions Context Hub as a **first stab at memory**, framed as open:
- `agents.md` and skills are open standards (open foundations)
- Memory should not be locked into LLM, framework, or platform
- Working with **Redis, Elastic, Mongo, Pinecone** to push **open memory standard for agents**

This is a corpus-first observation of major framework vendor explicitly building product on Karpathy's LLM Wiki pattern. **Critical Storm Bear cross-link:** the LLM Wiki pattern is the foundational pattern of [[external|harness-engineering/_index]]'s sibling research thread — Harrison naming it directly elevates it from personal-discipline pattern to ecosystem load-bearing. Worth flagging for Pattern Library mini-audit candidate registration.

---

## Phase 4 — Monitor

`[18:42]–[19:17]` (brief — main coverage deferred to SmithDB section)

- Tracing (every step, inputs, outputs)
- Dashboards (cost, latency over time)
- Online evals (LLM-as-judge or code over traces; capture or attach user feedback)

---

## Governance overlay

At `[19:24]–[21:04]` Harrison frames a 5th cross-cutting concern: **governance at scale**. "When you do it for 10 or 100 agents, that's when you really need to think about governance."

Two specific concerns:
1. **Cost** — surprise bills, per-agent / per-user spending visibility
2. **Data exposure** — LLMs are great with data but shouldn't access every source

### New launch 3: LangSmith LLM Gateway (beta)

- Sits between agents and LLM calls
- Spend limits + total visibility
- Guardrails for PII detection + secret detection
- Integrates with coding agents (notably the most popular agent class)
- Works with all LLM providers LangChain supports
- Auto-traced to LangSmith

This addresses the [[external|harness-engineering/core-claims|Lopopolo $2-3K/day token cost claim]] from the consumer side — orgs scaling agents need budget caps, not just inference.

---

## The integration story: Managed Deep Agents

`[21:18]–[22:49]`. **New launch 4: Managed Deep Agents (private preview)** — a single API combining everything.

Architecture:
- **Harness:** Deep Agents
- **Runtime:** LangSmith Deployments
- **Models:** OpenAI, Anthropic, Fireworks, Base10 (open + closed)
- **Memory / instructions:** Context Hub (versioned, trackable)
- **Execution environment:** LangSmith Sandboxes (separated from agent runtime)
- **Tools:** MCP (directly or via Arcade-like MCP server providers)
- **Streaming:** new protocol, CoPilotKit / Assistant UI / Vercel compatible

This positioning makes Deep Agents the harness + LangSmith the platform-around-the-harness — analogous to Claude Code (harness) + Anthropic's broader infra. Compare against [[external|harness-engineering/symphony-architecture|Lopopolo's Symphony]] which keeps the harness internal to OpenAI but exposes only the outcome.

---

## Part 2: SmithDB

`[22:49]–[38:34]` is Ankush Gola's deep dive on SmithDB. Covered in detail at [[smithdb-architecture]]. Headline metrics for the anchor record:

- **150M+ traces/week** at one Langsmith customer
- **50TB on a single day** sent by one customer
- **P50 payload growth:** 6KB → 37KB over the past 2 years
- **P99 payload growth:** 364KB → **12MB** over the past 2 years
- **Sample LangChain go-to-market agent trace:** 8.1 million tokens encoded in a single trace `[27:14]`
- **SmithDB perf gain:** 6×–15× faster than prior LangSmith infrastructure
- **Stack:** Rust + Apache DataFusion (extensible query engine) + Vortex (extensible file format) + custom indexing/query-planning/storage
- **Storage model:** object-storage-backed compute/storage separation
- **Early adopters:** Clay, Vanta

Jeff Dean quote (`[37:38]`):
> *"As we get agent-based systems that are operating multiple times faster than a human, your tools can become like an Amdahl's law bottleneck."*

This positions agent observability as **the next infrastructure-scaling frontier** — purpose-built database infrastructure for trace workloads is now economically necessary at scale.

---

## Part 3: LangSmith Engine

`[39:00]–[43:36]`. **New launch 5: LangSmith Engine (public beta)** — an "ambient, proactive, action-taking agent."

Harrison reframes the still-hard parts of the ADL flywheel:
- Finding issues among millions of traces — hard
- Understanding issues in long traces — hard
- Fixing issues (change prompt? code? tools?) — hard
- Avoiding regression repetition — hard ("whack-a-mole")

LangSmith Engine sits on top of traces, runs on a schedule, and:
- Detects issues, assigns priority, backs evidence with traces
- Suggests **code changes** (via GitHub integration)
- Suggests **data points to add to datasets** (regression prevention)
- Suggests **prompt/context changes** (via Prompt Hub / Context Hub)
- Suggests **online evals to add** (track issue over time)

This is a **meta-agent for the ADL flywheel** — "you build an agent to help you with the things that are hard and important that you don't want to do." It collapses the 4 phases into a continuously-tightening loop with a proactive agent driving each spoke.

---

## Where this anchor converges with prior corpus anchors

| Prior anchor | Convergence point |
|---|---|
| [[external|harness-engineering/anchor-bundle-overview\|Lopopolo (org-scale)]] | Same observation that agent work requires new tooling categories distinct from SDLC; same "iterate quickly" stance; same emphasis on harness as integrating layer |
| [[external|harness-engineering/tejas-kumar-anchor\|Tejas Kumar (definitional)]] | Direct adoption of "agent harness" terminology; auth-proxy / harness-holds-secrets pattern; explicit 5+ component decomposition (Deep Agents has execution env + context mgmt + steering + delegation, equivalent to Tejas's 5–6 components) |
| [[external|harness-engineering/personal-repo-overview\|Tù Bà Khuỳm (individual-scale)]] | `agents.md` + skills + LLM Wiki as memory layer — all individual-scale primitives now productized as Context Hub |
| [[external|agent-dashboard-os/_index\|agent-dashboard-os]] | LangSmith Observability is the dashboard stack; SmithDB is the data-tier underneath |
| [[external|claude-md-12-rules/_index\|claude-md-12-rules]] | `agents.md` as open standard, working with Redis/Elastic/Mongo/Pinecone — elevates `agents.md` from personal-discipline file to ecosystem-level open format |

## Where this anchor diverges

- **Vendor-platform integration vs vendor-neutral tooling.** ADL framework is platform-agnostic in framing but the launches are all LangChain ecosystem. Compare to [[external|harness-engineering/contrarian-stances|Lopopolo's stance against vendor-lock-in tools]] — Harrison threads the needle by emphasizing open standards (agents.md, MCP, memory partners) while productizing a single API.
- **Cheap-model-+-good-harness positioning.** Both Tejas (`[17:53]`) and LangChain (DeepSeek/GLM5/Nemotron support, deep-agents-code open-source coding agent) endorse open/cheap models. Lopopolo's [[external|harness-engineering/core-claims|claims #6 & #8]] (frontier-grade-model + 1B-token-day) operate at a different scale point. The cheap-+-harness camp is growing across multiple 2026-Q2 sources.
- **HITL framing.** Harrison treats HITL as "steering control built into the harness" — load-bearing primitive. [[external|autonomous-loops-human-in-the-loop/_index]] frames it as a discipline / posture. Different abstraction levels of the same concern.

---

## Open questions surfaced

1. **Does SmithDB's 6–15× performance gain replicate outside LangSmith workloads?** All metrics are LangSmith-internal. Independent benchmark would corroborate.
2. **Is the auth-proxy pattern (secrets outside agent) becoming the new default for production-scale harnesses?** Two corpus sources within 2 days; worth tracking for 3rd corroborator.
3. **Will Karpathy's LLM Wiki pattern become a vendor-supported primitive across multiple frameworks (not just LangChain Context Hub)?** First major-vendor productization observed; second/third independent adoption would confirm trend.
4. **How does Managed Deep Agents compete with Claude Code + Anthropic infrastructure?** Both are harness+platform stacks; head-to-head comparison absent in corpus.
5. **Will Apache DataFusion + Vortex become standard for observability databases?** SmithDB is corpus-first user; other agent-observability vendors (Helicone, Phoenix, etc.) may adopt or compete.
6. **What's the saturation point for ambient meta-agents (LangSmith Engine pattern)?** When does an agent-helping-build-agents loop hit diminishing returns? Lopopolo's [[external|harness-engineering/contrarian-stances|skepticism toward "review by another agent"]] is partially relevant.

---

## Recommended trending topics (from this ingest's signal)

See parent topic [[_index|agent-development-lifecycle]] for placement notes. These emerge directly from this talk as worth-investigating next:

1. **DeepSeek V4 launch + open coding-model 2026 landscape** — Harrison cites V4 as "just last week" and frontier-competitive `[09:19]`; GLM5 + Nemotron + Qwen / GPT-OSS (from Tejas talk) all 2026 entrants. **Why now:** 3 independent 2026-Q2 talks endorse cheap-model-+-harness pattern.
2. **agents.md / Open Memory Standard ecosystem** — Redis + Elastic + Mongo + Pinecone partnering with LangChain. **Why now:** corpus-first observation of multi-vendor open-standard-for-memory effort.
3. **Auth-proxy pattern for agent secret isolation** — Tejas demonstrated principle 2026-05-17, LangChain productized 2026-05-19. **Why now:** 2 independent sources, 2 days apart — pattern emerging as default.
4. **Karpathy LLM Wiki gets vendor productization (Context Hub)** — first major-framework explicit adoption. **Why now:** validates Storm Bear's core vault pattern at industry-vendor level; if 2 more vendors adopt, becomes a Pattern Library promotion candidate.
5. **SmithDB-class purpose-built infrastructure for agent observability** — `Apache DataFusion + Vortex + Rust` stack pattern. **Why now:** 6–15× perf gain claim + Jeff Dean Amdahl's-law framing suggests this becomes standard infrastructure tier.

---

## Cross-links

- [[_index|agent-development-lifecycle index]] — topic-level navigation
- [[smithdb-architecture]] — SmithDB technical deep dive sibling article
- [[external|harness-engineering/tejas-kumar-anchor]] — 5-component harness decomposition (terminology cross-adoption observed here)
- [[external|harness-engineering/anchor-bundle-overview]] — Lopopolo's org-scale framing (ADL is the consumer-side toolchain version)
- [[external|harness-engineering/personal-repo-overview]] — individual-scale primitives now productized in Context Hub
- [[external|agent-dashboard-os/_index]] — LangSmith Observability stack sits in this topic; SmithDB extends it underneath
- [[external|claude-md-12-rules/_index]] — agents.md elevated to ecosystem open standard
- [[external|autonomous-loops-human-in-the-loop/_index]] — ADL flywheel + LangSmith Engine meta-agent pattern
