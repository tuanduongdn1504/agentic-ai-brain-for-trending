# "Don't Swap Models — Change Two Variables"

> **Source:** [`4PKT7vFo334`](https://www.youtube.com/watch?v=4PKT7vFo334) [50:04]. One passage, and the sharpest cost claim in the bundle.

## The claim

> *"Không phải suốt ngày đi đổi cái con này đang từ Opus để chuyển sang OpenAI để dùng mô hình khác rồi Kimi. Đừng làm như vậy. Vì bởi vì bạn chỉ cần thay đổi hai cái biến số là **khối lượng công việc** và **số lần gọi** là bạn đã giảm tụt hết [chi phí] rồi."*

Paraphrased: **stop rotating vendors** — Opus → OpenAI → Kimi → whatever is cheapest this week. You only need to change two variables:

1. **The amount of work you send** (workload per call)
2. **The number of calls you make**

…and cost drops sharply. His accompanying point ([50:04]) is that the real work is **iterating on quality** — making the thing answer better and run smoother — not shopping for models.

## Why this is worth recording

It is a **counter-position to an entire band of the corpus.** The vault carries a cluster of subjects whose whole premise is *route to a cheaper or free upstream provider*: [[omniroute-free-tokens-claude-code/_index]] and the API-gateway / free-tier-harvester family. Those optimise the **price per token**. He argues the leverage is in **token volume and call count** instead — the numerator, not the unit price.

Both can be true, and they are not symmetric in risk:

| Lever | Ceiling | Risk |
|---|---|---|
| Cheaper vendor / gateway routing | Bounded by the price gap; can be large | ToS exposure, account bans, quality drift, a dependency you don't control |
| Less work per call, fewer calls | Compounds with caching and context engineering | Requires actual design work |

His lever is the one that survives a vendor changing its mind. It also aligns with the corpus' **harness-over-model** thesis ([[pocock-agentic-workflow/_index]]: the harness matters more than the model) and with the operator's own experience that cost discipline is a design property, not a procurement one.

## The mechanism, spelled out

He does not connect them explicitly, but "reduce workload and call count" is precisely what the rest of the bundle operationalises:

- **Less work per call** → [[four-rules-for-token-discipline]] rule 3 (send the schema, not the dataset; drop unneeded columns) and rule 2 (terse output, English when acceptable)
- **Fewer calls** → [[agent-org-chart-architecture]] (semantic routing sends a task to one specialist instead of broadcasting) and caching, which makes repeat calls cheap instead of merely fewer ([[prompt-caching-as-taught]])
- **Both** → the accuracy/cost convergence: *"chính xác và đỡ tốn tiền nó đi liền với nhau"*

## The caveat

Model choice is **not** irrelevant — his own pricing ladder shows a **10× input spread** between Haiku ($1) and Fable 5 ($10) ([[claude-pricing-ladder]]), and the corpus documents model-tiering as a real lever (cheap executor + expensive advisor, [[claude-api-cost-optimization/advisor-strategy]]). His argument is better read as *"stop **churning** vendors in search of a discount"* than *"tier selection doesn't matter"*. Picking the right tier once is design; rotating providers weekly is thrash.

## Cross-links

- [[claude-pricing-ladder]] — the 10× tier spread that qualifies this
- [[four-rules-for-token-discipline]] · [[agent-org-chart-architecture]] — where the two variables get controlled
- [[omniroute-free-tokens-claude-code/_index]] — the corpus' counter-pole (route to cheaper upstreams)
- [[pocock-agentic-workflow/_index]] — harness > model
- [[claude-api-cost-optimization/advisor-strategy]] — tiering done deliberately
