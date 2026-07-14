# Codex CLI free-tier claim — fact-checked against current pricing

## The claim (as stated on-camera)

"Để sử dụng được Codex thì mọi người... hoàn toàn có thể sử dụng với cả tài khoản free. Hiện tại mình cũng đang sử dụng tài khoản free thôi, không phải là tài khoản Pro, không phải tài khoản trả phí." ("To use Codex... you can absolutely use it with a free account too. I'm currently using a free account myself, not Pro, not a paid account.") — with the caveat that heavy users should subscribe to a monthly plan.

## What current official pricing says

A main-loop `WebFetch` of `developers.openai.com/codex/pricing` (redirects to `learn.chatgpt.com/docs/pricing`, OpenAI's own docs domain — see [[source-provenance]] for how that redirect was confirmed) states plainly: **the Free plan does not include Codex CLI access.** The Free tier's description is "Explore Codex capabilities on quick coding tasks" with no CLI access; Codex CLI access begins at the **Go plan, $8/month**.

This directly conflicts with several third-party aggregator blogs (surfaced during the workflow's dive pass) that summarize Codex as "free on every plan including Free ($0/month)" — those summaries appear to conflate general ChatGPT-app-based Codex access (which may have a limited free trial surface) with the **CLI specifically**, which OpenAI's own pricing table gates behind Go or higher.

## How to read the contradiction with the video

Two explanations are plausible and not mutually exclusive:
1. **Policy tightened between the video's upload (2026-06-28) and this fact-check (2026-07-14).** A 2-3 week gap is enough time for a pricing-tier change, and OpenAI has iterated on Codex tiers rapidly through 2026.
2. **The presenter may have been using an API key (BYOK)** rather than ChatGPT-plan sign-in — Codex CLI supports both, and API-key billing is metered separately from the ChatGPT-plan tiers. If so, "free account" in the video may have meant "I'm not paying for a ChatGPT subscription," while still incurring (possibly negligible, given the demo's small scope) per-token API charges — a different claim than "the Free ChatGPT plan includes Codex CLI."

Either way, the video's specific framing — a $0/month ChatGPT plan unlocking Codex CLI with generous-enough limits for a demo — does not match current (2026-07-14) official pricing, which explicitly excludes Free from Codex CLI and starts CLI access at $8/month (Go).

## Verdict

**FALSE**, as a claim about current (2026-07-14) official Codex CLI pricing tiers. Flagged as a claim-vs-current-reality mismatch, not a deliberate misrepresentation — the presenter may simply be describing behavior true at time of filming, or conflating API-key access with a ChatGPT-plan tier. See [[claims-scorecard]].

## See also

[[_index]] · [[overview]] · [[claims-scorecard]] · [[source-provenance]]
