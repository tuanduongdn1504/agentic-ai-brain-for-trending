# Theo on cost, speed & how to use K3 (N=3)

> Theo's pricing read **corroborates the corpus** ($3/$15 = Sonnet-tier, not cheap; verbosity eats the discount), adds **real single-practitioner cost numbers**, and clears up the **confusing access story** (weights not out; OpenCode / CLI-proxy, not native Claude Code).

## Pricing — corroborates the corpus, no "5×" error

- **$0.30 cache-hit / $3 per M in / $15 per M out** [09:30] — *independently CONFIRMED* against Moonshot pricing.
- Theo frames it as **"roughly Sonnet-level priced"** — the same conclusion as the corpus's [[pricing-and-the-end-of-cheap-chinese-ai]] ("$3/$15 = frontier-tier = Sonnet 5") and the widely-quoted framing "Opus-4.8-class at Sonnet-5 pricing." **Notably, Theo does *not* repeat the N=2 BridgeMind "5× price increase" error.**
- He states the catch the corpus flagged as scorecard #17: **$15-out "is not cheap," and K3 uses ~2× the tokens of GPT-5.6 Sol**, which *cancels* the nominal discount [24:43]. CONFIRMED / CORROBORATES.

## Real cost — new, but single-practitioner (OPINION)

- **~$63 for a full day of heavy work** [39:14] — versus his self-reported **~$1,000/day on OpenAI models** and **~$300–400/day on Fable**. Verdict **OPINION** (his own API accounting; not independently checkable) but a useful order-of-magnitude: *work-per-dollar is good, but the $15-out + 2× verbosity keep it from being a blow-out saving.*
- **Subscription tiers ≈ $20 / $40 / $100 / $200** [38:03–38:32]. He burned the $40 tier's 5-hour window in ~30 minutes of early testing, upgraded to $200, and then "borderline abusive usage" didn't pass 50% of a 5-hour window — so the top tier is generous. (The Haiku verifiers attached tier *names* and exact `$19/$39/$99/$199` figures; those are secondary-source enrichment, not Theo's on-camera words — treat the round numbers as his.)

## Speed — a measurement-context conflict, reconciled

- **Theo: ~20 TPS out, "less than half of what we see from other labs"** [35:26], and reasoning runs on **max effort only** (no low/high modes at launch), so "it feels slow."
- **Apparent conflict:** Artificial Analysis publishes **~62 tok/s** for K3. The completeness critic flagged this 3× gap as needing resolution.
- **Reconciliation:** these measure different things, and the **corpus already contains both poles** — [[speed-pricing-and-local-reality]] records "26–28 launch / 62 official." Theo's ~20 TPS is an **end-to-end, harness-measured** rate (OpenCode + a CLI proxy routing into Claude Code, with routing/launch overhead); AA's 62 is **raw API** under ideal conditions. So Theo's number is a *third* consistent data point: **effective throughput in a real harness at launch is far below the headline 62.** Marked **UNVERIFIABLE as a raw-speed claim / CONFLICTS with the raw-API figure**, reconciled by measurement context — not asserted as K3's true speed.

## How to actually use it — the access story

At video time (2026-07-17), the weights weren't out (**promised July 27**), so the *only* paths are hosted:

1. **`kimi.com` subscription** ($20–$200 tiers) — but subscriptions **do NOT grant the full 1M context** (this is what cut off Theo's ping.gg run mid-migration; CONFIRMED — full 1M is gated to higher API tiers). 
2. **`platform.kimi.ai` API** — pay-as-you-go; Theo accidentally spent ~$100 here before realizing he already had a sub.
3. **Not natively in Claude Code or Codex** ("wink") [29:48–30:16] — CONFIRMED. Theo's workarounds: **OpenCode** as the harness (bring the Kimi API key), and a **CLI proxy** that routes `/model kimi-k3` *into* Claude Code alongside Claude and Codex — the "route a non-native model into your existing harness" pattern (the same class of tool as the CLIProxyAPI/OmniRoute proxies covered in the Storm Bear main vault, not yet a topic in this autopilot worktree).

US-based labs also expose their models on Bedrock/GCP/Azure; **Moonshot does not** — reinforcing the residency point below.

## Residency footnote (matters for hireui)

Theo says inference goes "through Chinese servers." **Verified nuance:** the international API is operated by **MOONSHOT AI PTE. LTD. (Singapore)** with servers in Singapore — so "literally Chinese servers" is *imprecise*. **But it does not rescue the residency concern**, and arguably worsens it: Kimi's [privacy policy](https://platform.kimi.ai/docs/agreement/userprivacy) says **inputs *and* outputs may be used to train/improve the models by default** (opt-out requires negotiating an enterprise arrangement), data may be transferred outside your country, and the parent is Beijing-based. See [[hireui-translation]].

## Key Takeaways

- **Pricing verdict corroborated:** $3/$15 = Sonnet-tier, and ~2× verbosity eats the discount — Theo agrees, and avoids the N=2 "5×" error.
- **~$63/day** heavy use is his real number (OPINION) — good work-per-dollar, not a blow-out saving.
- **Speed 20 vs 62 TPS is a harness-vs-raw-API artifact**, consistent with the corpus's "26–28 launch / 62 official."
- **Access is fiddly:** hosted-only until July 27, subscriptions cap context, and it's OpenCode / CLI-proxy — not native Claude Code.
- **Singapore, not literally China — but trains on your I/O by default**, so still AVOID for candidate data.
