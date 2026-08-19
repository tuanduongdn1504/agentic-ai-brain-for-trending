# Prompt Caching (as taught)

> **Source:** anchor [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) [19:01]–[20:49].

## What he teaches

1. **What caching is** ([19:01]): content from earlier turns is stored on Anthropic's server so that next time you call, it costs less. *"Tiền sẽ khác, tiền bé hơn"* — the price is different, smaller.
2. **Cheaper is not free** ([19:27]): *"tiền bé hơn không có nghĩa là không tốn tiền."*
3. **Caches expire** ([19:27]): leave it too long without interacting and the cache lapses; then the whole history is read again and you pay for it. Every vendor — OpenAI, Anthropic — has its own expiry rules, and expiry affects both **cost** and **processing time**.
4. **He reads the real pricing table on screen** ([19:55]–[20:22]), correctly separating input price from the **cache write** column, and noting the default window is short (5 minutes) with a longer 1-hour option that costs more.
5. **Output is ~5× input** ([20:49]), so the highest-leverage output move is to demand terse answers — and, for a Vietnamese speaker, to consider answering in English.

## Verified against first-party docs

His numbers are **exactly right**, which makes this one of the most accurate passages in the bundle:

| His claim | First-party | Verdict |
|---|---|---|
| Cache **write**, 5-minute TTL = $6.25 / 1M (on a $5 input model) | **1.25× base input** = $6.25 | ✅ CONFIRMED |
| Cache **write**, 1-hour TTL = $10 / 1M | **2× base input** = $10 | ✅ CONFIRMED |
| Reuse costs less than full price | Cache reads ≈ **0.1× base input** | ✅ CONFIRMED (direction) |
| Output ≈ 5× input | $10→$50, $5→$25, $2→$10, $1→$5 — **exactly 5× across the entire Claude lineup** | ✅ CONFIRMED |
| Expiry forces a full re-read that costs money | A lapsed cache means a fresh **write** at 1.25×–2× | ✅ CONFIRMED (understated if anything) |

## ⭐ The gap: he under-sells the thing he is recommending

He never states the **cache-read discount**. Reads bill at **~0.1× base input — about 90% off**. That single number is the reason caching is the highest-leverage cost lever available, and the corpus already carries it as the headline of an Anthropic Platform-team talk: *"if you remember one thing, remember prompt caching"* ([[claude-api-cost-optimization/prompt-caching]]).

Because he quotes only the *write* premium (1.25×/2×) and never the *read* discount (0.1×), a viewer could reasonably come away thinking caching is a **surcharge** rather than a ~90% saving. The break-even is fast:

- **5-minute TTL:** 2 requests break even — 1.25× + 0.1× = 1.35× versus 2× uncached
- **1-hour TTL:** 3 requests break even — 2× + 0.2× = 2.2× versus 3× uncached

## What he omits that will bite in production

- **Prefix matching is byte-exact.** Any change anywhere in the prefix invalidates everything after it. Render order is `tools` → `system` → `messages`; keep stable content first and volatile content (timestamps, per-request ids) last. **A timestamp in the system prompt is the classic silent cache killer.**
- **There is a minimum cacheable prefix** (~1024 tokens). Shorter prefixes silently do not cache at all.
- **Verify, don't assume:** check `usage.cache_read_input_tokens`. If it is zero across repeated identical-prefix requests, something is invalidating the prefix.

## Cross-links

- [[claude-pricing-ladder]] — the price table he is reading from
- [[statelessness-and-context-cost]] — why caching matters at all
- [[claude-api-cost-optimization/prompt-caching]] — the deeper first-party treatment (and the ~90% headline)
- [[claude-code-observability/cost-cache-token-metrics]] — measuring cache hit rate in practice
- [[claims-scorecard]]
