# SmithDB — purpose-built database for agent observability

> **Source:** Ankush Gola (LangChain co-founder/CTO) at LangChain Interrupt 2026, segment `[22:49]–[38:34]` of [the keynote](https://www.youtube.com/watch?v=jWy39wavbjY).
> **Raw:** `raw/2026-05-19-langchain-interrupt-26-adl-transcript.md` — see specifically segments at `[23:55]–[38:34]`
> **Sibling article:** [[langchain-interrupt-26-anchor]] for ADL framework + 6 product launches summary

This article focuses on the SmithDB architectural deep dive — the most technically detailed section of the Interrupt 2026 keynote. SmithDB is positioned as the foundational database underneath the entire LangSmith product, purpose-built for agent observability workloads.

---

## Why a purpose-built database

At `[24:13]–[25:33]` Ankush argues traditional data infrastructure fails on agent traces because of three workload characteristics:

| Characteristic | Why traditional DB fails |
|---|---|
| **Deeply nested traces** | Thousands to tens-of-thousands of intermediate steps per trace. SQL row-flatten or document-store nesting strategies hit query-plan complexity early. |
| **Large unbounded payloads** | P50: 6KB → 37KB over 2 years. **P99: 364KB → 12MB over 2 years.** Single customer sent 50TB on one day. Single trace observed: 8.1M tokens. Column-store cost models break above MB-scale per row. |
| **Multimodal** | Increasing share of voice + image content (customer support driving voice especially). Binary-blob-in-row + indexable-text-in-row hybrid is non-standard. |
| **Unique query patterns** | Top-K + time-window + text-search + metadata-filter combinations dominate. Few off-the-shelf DBs optimize for this mix. |

Volume data point: real LangSmith customer's **weekly trace volume now exceeds 150M** as agents enter production and new agents enter the picture.

> *"If you're using suboptimal infrastructure to handle agent observability workloads, you will experience slow queries and ingestion bottlenecks. You'll also experience rising infrastructure costs and complexity as you try to scale up."* — `[27:32]`

---

## Architecture

### Object-storage-backed compute/storage separation

`[29:46]–[30:21]`. Three architectural benefits:

1. **Cost** — object storage is "incredibly cheap" and "scales pretty much infinitely"
2. **Compute/storage separation** — elastically scale services without complex shuffling or sharding when scaling services up
3. **Self-host friendliness** — easy to set up where data residency requirements are strict

### Component layout

```
[ ingestion service ]──batch──▶[ object storage ]◀──scan──[ query service ]
        │                              ▲                       │
        ▼                              │                       ▼
[ in-memory + SSD buffer ]       [ Postgres meta store ]   [ SSD + memory cache ]
                                                               │
                                                  [ cluster manager (sticky routing) ]
                                                               │
                                                       [ compaction service ]
```

`[30:30]–[31:31]`. Concretely:

- **Cluster manager** — distributes load across servers + maintains **sticky routing** (cache utilization + batch-ingestion effectiveness)
- **Ingestion service** — batches raw trace data, durably stores to object storage, registers files in Postgres meta store
- **Query service** — figures out which files need scanning, downloads from object storage, scans; uses SSD caching + memory to minimize object-storage round trips
- **Compaction service** — shapes files for more optimal querying

---

## Access patterns optimized

`[31:31]–[33:30]`. SmithDB explicitly targets four agent-observability query shapes:

1. **Random access to individual traces/intermediate steps** — "Agent observability isn't just about asking what happened across millions of traces. It's also about asking what happened in this one particular agent execution." `[31:43]`
2. **Full-text search across trace text** — custom inverted index **layout specifically designed for object storage** `[32:35]`
3. **Time-windowed scan + multi-attribute filter** — metadata, tags, name, latency, other attributes
4. **Top-K with order-by + limit** — common in dashboard views

Reported performance: **6×–15× faster than the prior LangSmith infrastructure** across these workloads `[33:45]`.

---

## Stack choices

`[34:24]–[35:18]`. Built on two open-source foundations:

| Layer | Project | Why |
|---|---|---|
| Query engine | **Apache DataFusion** | Extensible Rust query engine |
| File format | **Vortex** | Extensible file format — allows custom encodings + custom chunking per column |

Custom additions on top:
- Indexing (esp. full-text search)
- Query planning
- Execution plans
- Storage layouts

Whole system written in **Rust**. This is corpus-first as a vendor-built agent-observability database; prior LangSmith was presumably Postgres/Clickhouse-class general-purpose stack.

---

## Three technical challenges and solutions

`[35:24]–[37:09]`. Ankush enumerates three specific problems and their solutions:

### Challenge 1 — Distributed spans

> *"In agent observability workloads, your spans are distributed. They come in different parts. And this is because agents run for long time horizons. And so you can have a start event that gets sent sometimes hours before your end event."* `[35:34]`

**Solution:** efficient finding-and-merging of distributed events at query time AND at compaction time.

This problem doesn't exist in traditional observability workloads (where spans are short-lived service-call durations). Long-horizon agent runs create dangling-start-event problem that compaction must reconcile.

### Challenge 2 — Top-K queries on object storage

> *"A lot of the queries within Lang Smith are top case style queries. So they contain an order by and limit. And a more naive query plan would essentially like find all the files that are in range and fan them out, scan them, do some type of merge and top K operation. This is actually like a little bit expensive on object storage, actually quite expensive on object storage."* `[36:04]`

**Solution:** **time-window-based approach encoded into custom execution plan** that feeds top-K queries within SmithDB.

The object-storage cost model penalizes high-fan-out scan patterns; bounded time-windows let the planner skip files outside the relevance window cheaply.

### Challenge 3 — Leading-edge ingestion latency

> *"In observability workloads, you often need to serve the most recently ingested data as fast as possible."* `[36:42]`

**Solution:** **buffer data in the ingestion service in memory + SSD even after durably flushed to object storage**, making it available to the query service to avoid downloading many small files for leading-edge queries.

Classic write-and-read-now problem — the durable flush wins on cost, but recent-data queries (the most common dashboard pattern) need the hot buffer to stay fast.

---

## The Amdahl's-law framing

`[37:19]–[37:45]`. Ankush positions SmithDB as solving the **agent-as-user-of-observability** problem, not just the human-as-user:

> *"Langsmith performance is not only important for human UX, but also agent UX. Increasingly, agents are not just the thing that are being observed by Langsmith, they are also the users of Langsmith."*

Jeff Dean quote `[37:38]`:
> *"As we get agent-based systems that are operating multiple times faster than a human, your tools can become like an Amdahl's law bottleneck."*

This is corpus-first explicit naming of the **Amdahl's law bottleneck applied to agent tooling**. Logical extension: as agents iterate faster than humans through the ADL flywheel (especially [[langchain-interrupt-26-anchor#Part 3 — LangSmith Engine|LangSmith Engine]]'s ambient-proactive agent pattern), any tool latency in the loop becomes the bottleneck on overall system throughput.

This reframes infrastructure-tier investment economics: a 6–15× DB speedup directly multiplies meta-agent throughput, not just human-dev productivity.

---

## Rollout status (as of 2026-05-19)

`[37:45]–[38:34]`:

- **Live now:** SmithDB serves core observability workloads across **all of US Cloud** on Langsmith. All interactions + tracing projects pages on smith.langchain.com powered by SmithDB.
- **Soon:** Rest of Langsmith UI to be backed by SmithDB; self-hosted SmithDB; global cloud traffic.
- **Early adopters:** Clay (Jeff), Vanta (Andy) — testimonials shown in keynote video.

---

## Open questions

1. **Does the 6–15× claim replicate?** All numbers are LangSmith-internal comparison vs prior LangSmith. Independent benchmark vs Clickhouse / Elastic / Datadog APM on agent-trace workloads would corroborate.
2. **Vortex adoption beyond SmithDB?** Vortex is a relatively new format; SmithDB is corpus-first user. Other agent-observability vendors (Helicone, Phoenix Arize, etc.) may follow.
3. **What's the cost-per-trace at 150M+/week scale?** Object storage is cheap, but query patterns (random access + full text + top-K) push compute. No public pricing yet.
4. **Will purpose-built agent-observability DB become the standard tier?** If yes, expect 2–3 competing OSS or vendor projects within 12 months. If no, traditional Clickhouse/Elastic remain dominant.
5. **What's the lower bound at which SmithDB beats off-the-shelf?** Workload below P99=1MB and < 10M traces/month may not justify a purpose-built DB; cutover threshold unstated.

---

## Cross-links

- [[langchain-interrupt-26-anchor]] — sibling article: ADL framework + 6 launches
- [[_index|agent-development-lifecycle]] — topic index
- [[external|agent-dashboard-os/_index]] — observability stack at user-facing layer; SmithDB sits underneath
- [[external|harness-engineering/research-roadmap]] — agent-observability infrastructure is a downstream research surface from harness-engineering anchor
