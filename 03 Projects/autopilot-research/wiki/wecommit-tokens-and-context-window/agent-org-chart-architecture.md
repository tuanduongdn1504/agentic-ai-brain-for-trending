# The Agent Org-Chart Architecture

> **Source:** [`4PKT7vFo334`](https://www.youtube.com/watch?v=4PKT7vFo334) [50:32]–[57:48] — his live demo of the system he says runs his own company.
> ⚠️ **This section was almost lost.** The automated extraction returned only pricing points for this 59-minute video and missed the architecture entirely; the completeness critic caught the gap and it was recovered by reading the transcript directly. See [[caveats-and-corrections]].

## The premise

His diagnosis of where operating time actually goes ([50:59]): **aggregating information from many different sources** before you can decide anything — email, metrics, channel data. So the design goal is *one place*:

1. **All decision inputs converge on one interface.**
2. **All agents are commanded from that same interface.**

> *"Giống như là chúng ta điều hành công ty qua một cái giao diện duy nhất"* — running the company through a single interface.

He explicitly warns against the alternative: *"Bạn đừng dùng lẻ tẻ"* — don't run them piecemeal, scattered across separate tools.

## The hierarchy

A three-level org chart, staffed by agents:

```
CEO agent                    ← you give work to this one only
├── Marketing department
│   ├── YouTube channel manager   (analyse content, reply to comments,
│   │                              mine comments for insight, propose topics)
│   ├── LinkedIn Writer           (40–60min video → LinkedIn post)
│   └── Image designer            (art for that post)
├── Sales department              (sales checks)
├── Customer care                 (dedicated agent)
└── Operations                    (its own agents)
```

## The two mechanics that make it work

**1. Semantic routing, not rule-based dispatch** ([53:17]–[53:45]). He issues work to the **CEO agent only**. It reads the request, understands the intent, decides which department owns it, and delegates down. His demo: *"hãy trả lời các bình luận video mới nhất của tôi"* → CEO → marketing → YouTube-manager agent. No routing table; the routing *is* the comprehension.

**2. Ordered hand-offs inside a department, concurrency across them** ([54:13]–[54:39]). "Turn my latest video into a LinkedIn post, then generate a matching image" is **two staff in sequence** — LinkedIn Writer first, image designer second, because the second consumes the first's output. Meanwhile he fires an unrelated request (check community activity on Circle) which routes to a **different department in parallel**.

So: **sequential within a dependency chain, parallel across independent ones** — the same shape as a well-built workflow, expressed as an org chart.

## The dashboard layer

- Freely reconfigurable by current priority ([51:53]): push marketing panels to the top this month, swap to sales later.
- Gives him an **overview of every agent's activity** in one view ([51:26]).
- Surfaces metrics **beyond the vendor's own console** ([55:33]): which recent videos performed, which topics to do next, which time slot to publish — *"nhiều thông tin hơn mà ở trong YouTube Studio không có."*
- Includes a **"radar thị trường"** (market radar) panel ([56:00]).

## Honest disclosure, and its cost to verifiability

He states **twice** ([50:32], [52:20]) that sensitive agents and sensitive data were removed from the dashboard before filming, while insisting the architectural value is unaffected.

That is commendable disclosure. It also means **the demo is partial and the system cannot be independently verified** — we see the parts he chose to show. Treat this as a described architecture, not an audited one. No repo, no code, and no product name is given for the dashboard.

## Why this belongs in a tokens topic

It looks like a detour from tokenization, but it is the payoff. His whole cost argument ([[dont-swap-models]]) is that the variables that matter are **how much work you send and how many calls you make**. An org chart with semantic routing is a mechanism for controlling exactly those two: each agent gets a narrow brief (less context per call) and the CEO layer prevents you from broadcasting every task to everything.

## Cross-links

- [[dont-swap-models]] — the cost thesis this architecture serves
- [[multi-agent-orchestration/_index]] — the corpus' orchestration treatment (hub-and-spoke, stateless workers)
- [[four-rules-for-token-discipline]] — rule 4's partition-by-strength, applied at org scale
- [[agent-forgetfulness-and-vendor-memory]] — the memory problem this architecture inherits
- [[caveats-and-corrections]]
