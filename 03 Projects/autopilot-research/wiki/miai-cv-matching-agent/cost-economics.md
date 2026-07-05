# Cost Economics (verified arithmetic)

## Source

Dive `cost-economics` + refute-first verify (two arithmetic errors in the dive were caught and corrected by the verifier — corrected numbers below). OpenAI pricing verified: gpt-4o-mini $0.15/$0.60 per 1M in/out; text-embedding-3-small $0.02/1M.

## Demo-scale numbers (CONFIRMED)

- **Per-CV analysis ≈ $0.00134** (~0.13 cents): ~5,700 input tokens (system 500 + CV 1,200 + 5 JDs 4,000) + ~800 output tokens.
- **Ingestion is noise**: ~150 JDs × ~800 tokens × $0.02/1M ≈ **$0.0024 per crawl cycle**; weekly refresh ≈ $0.12/month.

## At SaaS scale (10K CVs/month, 500 jobs)

- LLM analysis: **≈ $13.35/month** (~99% of API spend).
- Embeddings: ≈ $0.12–0.42/month (<1%).
- Total API cost < $15/month — comparable to or below the hosting bill. Token-level optimization is marginal until ~50K+ analyses/month.

## Corrections the verify pass caught (Rule 12)

- Self-hosting embeddings (the video's cost tip: LM Studio/vLLM "để đỡ tốn tiền") saves ≈ **$0.12–0.13/month** at this scale vs a ~$250+/month GPU instance — **negative ROI ≈ 2,000:1**. The dive's "$0.44/month savings" was a transcription error. Verdict on the video's advice: **it targets the wrong cost line** — embeddings are <1% of spend; the LLM line is ~99%. (CONFIRMED)
- OpenAI Batch API saves **≈ $4.28/month** at 10K CVs (50% input discount; the dive's "$0.35" was another transcription error) — viable only for nightly re-matching due to 24h latency.
- The verifier's own Anthropic comparison used a stale model/pricing (Claude 3.5 Sonnet @ $3/1M) — superseded by the main-loop Claude math in [[claude-stack-port]] (Haiku 4.5 $1/$5: ≈$0.0097/CV raw, ≈$0.006 with caching, ≈$0.005 batched — ~4–7× gpt-4o-mini, still trivial in absolute terms).

## Levers that actually matter (in order)

1. **Prompt caching** on the JD/system context (both vendors; Anthropic reads at 0.1×).
2. **Batch API** for scheduled re-matching (both vendors 50%; Anthropic batches mostly complete <1h vs OpenAI's 24h window).
3. Model tiering: cheap model for scoring/explanations, expensive model only for premium deep-analysis.
4. NOT self-hosted embeddings at this scale.

## Key Takeaways

- The economics headline: this feature costs **tenths of a cent per candidate** — cost is not the barrier to shipping matching; quality and compliance are.
- Optimize the 99% line (LLM calls), not the 1% line (embeddings).
- The two dive arithmetic slips caught by refute-first verification are exactly why numbers get re-derived before publication.
- Cross-links: [[external|Storm Bear: claude-api-cost-optimization]] (vault's cost playbook), [[external|Storm Bear: mosh-ai-powered-apps]] (13× cost-lever framing).
