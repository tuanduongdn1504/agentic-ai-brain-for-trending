# Speed, pricing & local-hosting reality (corrected)

> The stream's incremental factual claims about speed, price, and self-hosting — corrected against independent sources. Source: [[vibe-coding-livestream-bridgemind]]. Verified via main-loop Opus WebSearch (OpenRouter / Artificial Analysis / Anthropic pricing / claude-api skill) + Workflow `wf_b9762e52-36b`.

## Speed — the streamer's K3 number is right; his Fable 5 number is wrong

- **K3 "~25–27 tok/s" at launch → CONFIRMED for what he was using.** OpenRouter early telemetry: **~26–28 tok/s, ~4s time-to-first-token**, "slower than Opus"; observers speculated speculative decoding wasn't yet enabled. His figure matches his provider exactly.
- **"Fable 5 runs at 38 tok/s on Anthropic" → likely WRONG.** Independent benchmarks (Artificial Analysis, OpenRouter) put Fable 5 at **~63–70 tok/s** — the "38" understates it by ~40%. *(This ~65 figure is a workflow finding not independently re-confirmed on Opus; treat the exact number as medium-confidence, but the direction — his 38 is too low — is safe.)*
- **The real story = launch-day serving immaturity, not architecture.** On the **official** Kimi API, Artificial Analysis measures K3 at **~62 tok/s** — near-parity with Fable 5's ~65. K3's slow OpenRouter throughput reflects incomplete serving optimization (Moonshot's custom vLLM KDA prefix-caching shipped alongside weights ~July 27; continuous batching / speculative decoding not yet tuned at launch), not a capability ceiling.
- **The KDA "fast decode" tension dissolves.** [[architecture|Kimi Delta Attention]]'s marketed **~6.3× faster decode / 75% smaller KV cache** applies specifically to **million-token-context decoding efficiency** — a different metric from fresh-request streaming throughput. Both can be true at once: efficient-per-token at long context, yet slow at launch on immature infra.

**Net:** K3 was genuinely slow *on OpenRouter at launch*, which is what the streamer saw and is fair to report — but he overstated the gap (Fable 5 is ~65, not 38) and the slowness is a maturity gap, not a permanent architectural weakness.

## Pricing — "5× increase" is inflated; "= Sonnet 5" needs an asterisk

- **The "5× price increase" is WRONG (~3.2–3.8× real).** Kimi K2.6 and K2.7 Code both list at **$0.95 in / $4.00 out** (262K ctx) at official launch pricing. K3 at **$3 / $15** is **~3.2× input / ~3.75× output** over that — a big jump to frontier tier, but **not 5×**. The streamer's cited "$0.72 / $3.50" baseline is a **discounted OpenRouter reseller rate**, not launch pricing; computing "5×" off the discounted number inflates the multiplier. *(His two on-stream figures for K2.7 output — "$3.50" and "$1" — are themselves inconsistent.)*
- **"$3/$15 = Sonnet 5" — accurate on sticker, with a timing asterisk.** Claude **Sonnet 5 standard = $3/$15** (per the claude-api reference) — so the parity claim holds at the standard rate. But Sonnet 5 is on **introductory $2/$10 through 2026-08-31**, i.e. **~33% cheaper than K3 right now**; parity only kicks in Sept 1. So "same price as Sonnet 5" is true *later*, not *today*.
- **His *conclusion* is directionally correct:** K3 is no longer a budget model — it's a frontier-tier price, "the end of super cheap Chinese AI" (a framing independent press echoes). See [[pricing-and-the-end-of-cheap-chinese-ai]]. He just got the arithmetic and the baseline wrong.

## Local hosting — not self-hostable; alternatives real; exact capex uncertain

- **CONFIRMED: 2.8T is not locally runnable by normal teams.** It needs data-center-class multi-GPU (the [[open-weights-reality|flagship article]] pegs it at **~650GB–1.7TB memory / 8–16 H100**). "You are not going to be running Kimi locally... you'd need a data center" is correct.
- **The "$3M" figure is a loose on-stream riff, likely overstated** — but treat precise counter-quotes with caution. The verification workflow proposed ~$150–200K (5× H200) or ~$28–37K (6–8 DGX Sparks); **this wiki does NOT adopt those precise numbers** — they rest on a shaky "700GB VRAM" assumption and conflict with the corpus's own 8–16 H100 figure. The robust, ship-able claim is simply: **not consumer-hostable; data-center hardware required; exact capex is uncertain and quantization changes the math.** See [[caveats-and-corrections-vibe-coding]].
- **Named local alternatives are REAL** (CONFIRMED on Hugging Face): **Qwen 3.6-27B** (already in-corpus, Apache-2.0), **Qwen 3.6-35B-A3B** (MoE, 35B total / ~3B active — the streamer said "35B"), **Gemma 4 31B**. His "as good as last year's frontier (~GPT-5 level)" is a fair rough framing.
- **Imminent shift:** K3 open weights land **~July 27**, after which quantized builds (llama.cpp / ollama / vLLM) will widen local options — a caveat the stream omits.

## <a id="hireui-as-a-dev-tool"></a>hireui: K3 as a *build tool* (distinct from the product ADR)

This video shows K3 as a **vibe-coding dev tool**, not a product-integrated model — a narrower question than the flagship [[hireui-translation]] (which ruled K3 **AVOID for any candidate-facing path**, and that ruling **stands unchanged**).

- **As a tool to *build* hireui: no compelling reason to adopt at launch.** K3's real edge is one-shot frontend/UI scaffolding, but against the operator's current stack (Claude Code + Sonnet/Opus) it's **slower on OpenRouter at launch, not self-hostable, cheaper only after Sept 1, and less integrated**. Sonnet 5 (currently $2/$10 intro) is the cheaper, faster, better-integrated baseline.
- **If ever piloted:** isolate to a **non-hireui throwaway** UI-scaffolding spike, measure K3 vs Sonnet 5 on identical tasks (cost/throughput/quality), and **explicitly reject the BridgeBench framing** for model selection (vendor conflict — see [[bridgemind-source-and-conflict-of-interest]]).
- **The two decisions are orthogonal:** adopting K3 as an IDE tool would *not* change the candidate-facing AVOID. Static candidate-matching logic stays on Claude behind the RATIFIED ADR regardless.

## Key Takeaways

- **Speed:** K3 ~26–28 tok/s at launch is real (OpenRouter); "Fable 5 = 38" is too low (~65); near-parity on official API; slowness = launch-day infra immaturity, not architecture.
- **Pricing:** ~3.2–3.8× over K2.6/K2.7's $0.95/$4, **not 5×**; "= Sonnet 5" true at standard rate but Sonnet 5 is 33% cheaper on intro pricing through Aug 31.
- **Local:** not consumer-hostable (confirmed); named Qwen/Gemma alternatives are real; exact capex is uncertain — the workflow's precise $ figures are **not adopted**; quantization arrives ~July 27.
- **hireui:** candidate-facing AVOID unchanged; as a *dev tool*, no compelling reason to switch from Claude at launch.
