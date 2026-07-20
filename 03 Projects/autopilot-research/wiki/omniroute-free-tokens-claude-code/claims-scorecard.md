# Claims Scorecard

## Source
Refute-first Workflow `wf_e3d4a558-e70` (7 digest + 14 cluster verifiers + synth + critic; 2 verifiers returned empty and were re-done main-loop — see [[caveats-and-corrections]]) + 3 main-loop (Opus) re-verifications of load-bearing date/number claims.

## Verdict counts (12 clusters)
**0 CONFIRMED · 9 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 FALSE · 0 UNVERIFIABLE · 0 FABRICATED**

Profile: a **hype bundle** — the numbers survive scrutiny, but every video omits the ToS/security/provider-caveat context. Nothing rated cleanly CONFIRMED because each headline claim is technically-true-but-materially-incomplete.

## The table

| # | Claim (as pitched) | Verdict | Corrected / completed |
|---|---|---|---|
| 1 | "~1.6–2B free tokens/month" | **CORRECT-BUT-INCOMPLETE** | Real (OmniRoute `FREE_TIERS.md`: ~1.54B recurring / ~2.15B first month). **100% non-Claude** (Mistral 1B, llm7 150M, Gemini 60M…). Self-reported, shifting. |
| 2 | "free tokens **for Claude Code**" | **CORRECT-BUT-INCOMPLETE** | Only means "free **non-Claude** models via the Claude Code client." Anchor demo served **DeepSeek V4**. No free Claude in the pool. |
| 3 | Providers/models ("~300 / 256 / 344") | **CORRECT-BUT-INCOMPLETE** | Version drift, not error. Current: **268+ providers / 500+ models**. |
| 4 | "inspired by OpenRouter" | **MISLEADING** | Actually a **TS port of CLIProxyAPI** + fork of **9router**; inherits OAuth-reuse. Speaker confused OpenRouter (a marketplace) with the software lineage. |
| 5 | "RTK+Caveman saves 15–95% (~89%)" | **CORRECT-BUT-INCOMPLETE** | Real range + preservation of code/URLs/JSON, but **self-reported, not independently benchmarked**. |
| 6 | MIT · ~20K★ · "500+ contributors" · Brazilian author | **CORRECT-BUT-INCOMPLETE** | MIT ✓, ~20.3K★ ✓, Diego Souza (São Paulo) ✓. **"500+ contributors" is inflated → 257 named** (289 incl. anonymous). |
| 7 | "replaces Claude Code / OpenRouter" | **CORRECT-BUT-INCOMPLETE** | Conditional: replaces CC for **routine model-agnostic** work only. Opus still wins hard problems; free Claude requires a paid key. OpenCode ★ understated (160K→~187K). |
| 8 | "90+ free-forever providers, no card" | **MISLEADING** | Most carry caps/rate-limits/KYC or are one-time. **Kiro ToS prohibits proxy use**; Qoder has no free tier; Pollinations rate-limited; **LongCat restructured May 2026** to a one-time 10M bonus. |
| 9 | VPS setup is fine as shown | **CORRECT-BUT-INCOMPLETE** | Defaults are **unsecured** (HTTP, `CHANGEME`, `REQUIRE_API_KEY=false`, insecure cookies); walkthroughs omit hardening. |
| 10 | 17 routing strategies / quota-aware auto-fallback | **CORRECT-BUT-INCOMPLETE** | **18** strategies; fallback real but quota-awareness **buggy** (GitHub #7387, 2026-07-16→17). "8ms failover" unverifiable. |
| 11 | "Claude Desktop is now FREE — ALL Claude models" (t6, via AntiGravity) | **FALSE** | AntiGravity's free Claude was **removed ~May 2026** (now API-key-only). July-dated "free Claude via AntiGravity" doesn't hold. |
| 12 | "everything stays local / complete privacy" | **CORRECT-BUT-INCOMPLETE** | OmniRoute's *own* storage is local/encrypted, but prompts go **upstream** to free tiers that **log/train** (Gemini, DeepSeek, OpenRouter's own warning). |

## Cross-cutting omissions (in every video)
- Anthropic's **Jan/Feb 2026 OAuth ban** (OpenClaw/OpenCode/Roo/Goose blocked) — [[anthropic-oauth-ban-and-tos-risk]].
- **AntiGravity Claude removal** (~May 2026) and **Kiro's proxy prohibition** — [[antigravity-kiro-and-the-free-claude-window]].
- **VPS hardening** and **upstream data-training** — [[security-and-privacy]].
- The **Path A / B / C** distinction — [[free-tokens-vs-free-claude-three-paths]].

## Key Takeaways
- **9/12 "correct-but-incomplete," 2 misleading, 1 false, 0 confirmed** — trustworthy mechanism, systematically incomplete framing.
- The single **FALSE** is the "free Claude via AntiGravity" claim (expired ~May 2026).
- Every material risk (ToS ban, security, provider caveats) is an **omission**, not an outright lie — which is exactly why the bundle is persuasive.
- Related: [[caveats-and-corrections]] · [[overview]]
