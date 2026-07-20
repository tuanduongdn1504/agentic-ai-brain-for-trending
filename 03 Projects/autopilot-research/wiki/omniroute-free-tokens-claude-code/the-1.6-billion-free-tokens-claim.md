# The "1.6 Billion Free Tokens" Claim

## Source
Anchor t1 [03:04, 13:15], t2 [00:56], t3 [06:33], t5; OmniRoute `FREE_TIERS.md`; Workflow verdicts `1.6b-claim`, `free-tokens-are-NOT-free-Claude`.

## The claim
Every video leads with a big number: DEVKIT AI says "**~2 billion free tokens/month**" and "**~1.6 billion**" from free providers; t2/t3/t5 repeat "~1.6B free tokens/month."

## Verdict: CORRECT-BUT-INCOMPLETE
The number is **real and honestly calculated** — but it is **100% non-Claude**, and the framing implies free Claude.

- OmniRoute's own [`FREE_TIERS.md`](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/reference/FREE_TIERS.md) documents **~1.54B recurring free tokens/month** (steady state) and **~2.15B in the first month** with one-time signup credits.
- It is **pool-deduplicated** (shared accounts counted once) and aggregated across **~40 separate free-tier pools**. Top contributors: **Mistral ~1.0B**, **llm7 ~150M**, **Gemini ~60M**, then Groq / SambaNova / Cerebras / Cloudflare-AI (~30M each) + dozens more.
- OmniRoute even *corrected its own figures down* on 2026-06-17 (Gemini 462M→60M, CloudflareAI 122M→30M) to stay honest — a point in the project's favour.
- **Zero of the 1.6B comes from Claude.** FREE_TIERS.md states plainly that Claude's absence "reflects that Anthropic doesn't offer a free-tier API." The anchor's own live demo confirms this: at [34:44] the model answering is **DeepSeek V4** ("this is from the open code side"), not Claude.

## Why the framing misleads
The video title *"Get 1.6 Billion Free Tokens **for Claude Code**"* is technically defensible only under one reading: **"free non-Claude models, accessed through the Claude Code client."** A viewer naturally hears "free Claude." Those are different products:
- ✅ Free tokens you can spend on **DeepSeek / Gemini / Mistral / Kimi / Nemotron** via the Claude Code CLI — real, and this is Path A.
- ❌ Free tokens on **Claude models** — not in the pool, and every route to "free Claude" is expired or banned (see [[free-tokens-vs-free-claude-three-paths]] and [[antigravity-kiro-and-the-free-claude-window]]).

## What the number is *not*
- **Not a personal entitlement you can burn on frontier work.** It is aggregate free-tier capacity, most of it on smaller/slower free models with per-provider rate limits and caps. t3 (the most honest source) says it straight: free tiers mean "slower models, tighter rate limits, and quality that swings" — and "on the truly hard problems, a top closed model like Opus still pulls clearly ahead."
- **Not stable.** Self-reported and moving: providers change free tiers constantly (e.g. **LongCat** was restructured May 2026 from a planned "50M tokens/day" to a **one-time 10M signup bonus**).

## Key Takeaways
- "**~1.6B free tokens/month**" is a **real, honest** OmniRoute figure — and **entirely non-Claude**.
- The "for Claude Code" framing invites the false read "free Claude." It means *the Claude Code client pointed at free non-Claude models*.
- Treat the number as **free low-to-mid-tier capacity with caps and rate limits**, useful for routine work — not frontier-Claude headroom.
- Related: [[free-tokens-vs-free-claude-three-paths]] · [[antigravity-kiro-and-the-free-claude-window]] · [[claims-scorecard]]
