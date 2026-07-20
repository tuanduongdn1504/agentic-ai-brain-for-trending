# hireui / Operator Relevance

## Bottom line
**Catalog defensively. Do NOT pilot the "free Claude" path against any real Anthropic account. Path A (free non-Claude routing) is interesting as a *cost-reduction pattern* to study — but it collides with the hireui candidate-LLM legibility ADR the moment candidate data or Claude-quality reasoning is involved.**

## Why it's on the radar
- The operator's goal set includes **Claude-API cost optimization** and there's a prior corpus pilot — [[harness-engineering/personal-repo-router-multimodel]] — that is *exactly* this idea (one gateway, many models, route by task/cost). OmniRoute is the productized, extreme version of that pattern.
- So the tool is worth **understanding as a reference architecture**, not adopting as-is.

## Hard stops (do not do)
1. **No Path C.** Never route a Claude Pro/Max subscription through OmniRoute to get "free Claude." Anthropic banned this (Jan/Feb 2026) and terminates accounts — see [[anthropic-oauth-ban-and-tos-risk]]. A ban would take out the operator's actual Claude access, which the whole workflow depends on.
2. **No Path B.** The AntiGravity/Kiro "free Claude" routes are expired and/or violate Google/AWS ToS — [[antigravity-kiro-and-the-free-claude-window]].
3. **No candidate data through free tiers.** Gemini/DeepSeek/OpenRouter free tiers **log and train on** inputs — a direct violation of the **[[external|Storm Bear: hireui candidate-LLM legibility ADR]]** (fixed, legible, audited, human-in-loop, residency-controlled; EU AI Act Annex III). Routing résumés/candidate PII through OmniRoute's free pool is categorically out.
4. **No unhardened deploy.** Default is HTTP + `CHANGEME` + no auth on a public port; it becomes a single store of all provider keys — [[security-and-privacy]].

## What's legitimately borrowable
- **The gateway-seam pattern itself:** one internal OpenAI-compatible endpoint in front of a vendor seam, with **paid API keys only**, routing rules, and cost caps. This is the *disciplined* version of what OmniRoute does — compose it with the operator's existing vendor-seam thinking ([[mosh-ai-powered-apps/_index]] Responses-API seam) rather than adopting OmniRoute.
- **Prompt compression as a cost lever** — the RTK/Caveman *idea* (compress prose/tool-chatter, preserve code/JSON byte-for-byte) is worth stealing for any high-volume LLM path, measured with your own eval harness, not the vendor's 89% ([[compression-rtk-caveman]]).
- **Quota-aware auto-fallback** across providers is a sound reliability pattern — but implement it on **paid, ToS-clean** providers.

## If ever piloted (narrow, non-candidate only)
- **Scope:** operator-side, throwaway, non-sensitive experimentation (e.g. a scratch coding task on free DeepSeek/Gemini) — **never** candidate-facing, never on hireui source with secrets.
- **Guardrails:** private-network-only (bind `127.0.0.1` / Tailscale), `REQUIRE_API_KEY=true`, TLS, **paid keys**, and a strict "no Path B/C" rule.
- **Value measured:** does free-tier routing meaningfully cut cost on *non-critical* work vs the honest baseline (Sonnet/Haiku on a paid key)? That's the only question worth answering — and t3 already gives the likely answer: yes for routine work, no for hard problems where Opus wins.

## Verdict
**AVOID for anything candidate-facing or account-risking; STUDY as a reference for the paid, hardened, ToS-clean version of a multi-provider cost-routing seam.** Claude stays the answer for hireui's real LLM features; the honest cost lever is model-tier choice (Haiku/Sonnet) on a paid key, not a free-tier proxy.

## Key Takeaways
- **Do not** run Path B/C or send candidate data through free tiers — it breaks the candidate-LLM ADR and risks an Anthropic ban.
- **Do** borrow the *disciplined* version: a paid, hardened, OpenAI-compatible gateway seam + compression + fallback.
- Cross-links: [[harness-engineering/personal-repo-router-multimodel]] · [[external|Storm Bear: hireui candidate-LLM legibility ADR]] · [[mosh-ai-powered-apps/_index]] · [[free-tokens-vs-free-claude-three-paths]]
