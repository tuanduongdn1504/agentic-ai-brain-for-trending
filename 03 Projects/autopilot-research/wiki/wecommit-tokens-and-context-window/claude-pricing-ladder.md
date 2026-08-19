# The Claude Pricing Ladder (as taught)

> **Source:** [`4PKT7vFo334`](https://www.youtube.com/watch?v=4PKT7vFo334) [13:11]–[14:32], reading Anthropic's live pricing page on screen.
> ⚠️ **This article corrects a fabrication introduced by this project's own extraction pipeline, not by the source.** See [[caveats-and-corrections]] §Extraction errors.

## His teaching device: an education ladder

He maps the model tiers onto school levels — a genuinely good mnemonic for a non-technical audience:

| His label | Model | Input $/1M | Output $/1M |
|---|---|---|---|
| **Tiến sĩ** — PhD | **Claude Fable 5** | $10 | $50 |
| **Thạc sĩ** — master's | **Claude Opus 5** | $5 | $25 |
| **Sinh viên đại học** — university student | **Claude Sonnet 5** | $2 | $10 |
| **Cấp ba** — high school | **Claude Haiku** | $1 | ($5) |

His arithmetic as narrated: the top tier is $10 in / $50 out; Opus 5 is *"rẻ một nửa"* (half price) at $5 / $25; Sonnet 5 halves again to $2 / $10; the bottom tier drops to $1.

## Verified against first-party pricing

| His figure | Authoritative | Verdict |
|---|---|---|
| Fable 5 — $10 / $50 | $10.00 / $50.00 | ✅ **exact** |
| Opus 5 — $5 / $25 | $5.00 / $25.00 | ✅ **exact** |
| Haiku — $1 input | $1.00 (output $5.00) | ✅ **exact** |
| Sonnet 5 — $2 / $10 | **$3.00 / $15.00 standard.** $2 / $10 is *introductory* pricing, valid **through 2026-08-31** | ⚠️ **correct when filmed, expires imminently** |
| Output ≈ 5× input | Holds exactly at every tier | ✅ **exact** |

**His pricing table is one of the most accurate things in the bundle.** All four tiers check out.

## ⏰ The one time-sensitive correction

Video published **2026-08-02**. Sonnet 5's $2 / $10 was live then, but it is **introductory pricing that ends 2026-08-31**, after which Sonnet 5 returns to **$3 / $15**.

> **Anyone applying his Sonnet 5 numbers after 2026-08-31 will underestimate cost by 50%.** With this topic compiled 2026-08-19, that is **12 days away.** If you are building a cost model off this video, this is the line to change.

Note also that the $10/$50 figure is shared: it is Fable 5's standard rate *and* Claude Opus 5's **fast-mode** rate. He is reading the Fable 5 row — he explicitly places Fable above Opus on the ladder — but the coincidence is worth knowing if you re-derive his numbers and land on a different row.

## What the ladder is actually for

The ladder exists to support his real argument, made at [50:04] and developed in [[dont-swap-models]]: **once you can see that price scales predictably by tier, the interesting variables are not which vendor you use but how much work you send and how many times you call.** The table is the setup; the punchline is workload discipline.

## Cross-links

- [[dont-swap-models]] — the argument this table is built to support
- [[prompt-caching-as-taught]] — the cache columns on the same pricing page
- [[claude-api-cost-optimization/_index]] — the model-tiering / advisor-strategy treatment
- [[caveats-and-corrections]] · [[claims-scorecard]]
