# Caveats & Corrections

> Method transparency + the specific corrections made during verification. Prime directive: don't repeat the same mistake twice — in either direction.

## Method + its limits
- **Bundle:** 7 videos (anchor + yt-search), captions via `yt-dlp` → `bin/vtt-to-md.py`, read directly (no NotebookLM). See [[source-provenance]].
- **Verification:** refute-first Workflow `wf_e3d4a558-e70` — 23 agents (7 digest + 14 adversarial cluster verifiers + synthesizer + completeness critic), ~1.42M tokens, 226 tool calls, 0 errors.
- ⚠️ **Model-override limitation (recurring corpus caveat):** per-agent model overrides are silently ignored — **all workflow agents ran on Haiku 4.5**. Therefore every load-bearing number/date was **re-verified in the main loop on Opus** (GitHub API + WebSearch), not taken on agent assertion.

## ⚠️ Two verifiers returned EMPTY — re-done main-loop
- `anthropic-tos-ban-risk` (verifier for the OAuth ban) and `without-anthropic-mechanism` (the t7/Bifrost mechanism) **completed without structured output** (2 of 23 agents empty).
- **Both were covered anyway:** the ToS-ban finding is independently established across 4 other verdicts *and* by the operator's own prior WebSearch (The Register / VentureBeat / MLQ / engineerscodex / KERSAI); the t7 mechanism was read directly from the transcript in the main loop. See [[anthropic-oauth-ban-and-tos-risk]] and [[cliproxyapi-lineage-and-the-gateway-ecosystem]]. No claim rests on an empty agent.

## Main-loop re-verifications (load-bearing, checked independently)
1. **"500+ contributors" → 257.** GitHub contributors API `Link` header: `per_page=1` last page = **257** named (289 incl. anonymous). Repo description's "500+" is inflated. ✓ agent was right.
2. **AntiGravity Claude removal (~May 2026).** WebSearch confirms Claude Sonnet/Opus 4.6 *were* in AntiGravity's selector, then "completely disappeared"; now API-key-only. This makes t6's July "free Claude via AntiGravity" **FALSE/expired**. ✓
   - ⚠️ **Honest nuance (do not over-claim):** t6 is a *live* July-16 demo that appears to show Claude working. We do **not** allege deliberate deception — plausible explanations are pre-removal footage, transitional availability, or stale/aliased model listings. The wiki claims only that the promise **doesn't hold as of July 2026**, not that FZ faked it.
3. **Kiro ToS prohibits proxy use.** Kiro FAQ: bans "use with OpenClaw and similar tools that leverage third-party harnesses"; AWS/Bedrock abuse-detection applies (extra on free tier). ✓ agent was right.

## Corrections applied to the videos' claims
- "Inspired by OpenRouter" → **TS port of CLIProxyAPI + fork of 9router** (README Acknowledgments). The anchor's "OpenRouter" was also an ASR artifact ("Nouter/Narrator/NRT").
- "17 routing strategies" → **18** (docs).
- Provider/model counts (236/256/300/344) → **version drift**; current 268+/500+. Not errors.
- OpenCode "160K stars" (t3) → **~187K** (understated).
- "Complete privacy" → local **only**; upstream free tiers log/train ([[security-and-privacy]]).

## Transcript hygiene (ASR garble normalized)
Auto-captions mangled key terms; normalized in analysis, never quoted as-is:
- "Nouter / Narrator / NRT / Naruto" = **OpenRouter**
- "Omni Round / Amiral / Omiro / Tiro" = **OmniRoute**
- "cloud code / clot / clout / Klout / CLUT" = **Claude Code / Claude Desktop**
- "Dis V4 / Dip V4 / Deep Sick" = **DeepSeek V4**
- "AGY / anti-gravity / Integrity" = **Google AntiGravity**
- "Byfrost / by frost" = **Bifrost**

## Rule-12 fail-loud notes
- The one **FALSE** verdict (t6 free-Claude-via-AntiGravity) rests on a provider-status change we verified by search; flagged with the "live demo may still appear to work" nuance rather than asserting fraud.
- Compression 89% is labeled **self-reported**, not proven (the critic argued it's closer to UNVERIFIABLE — noted in [[compression-rtk-caveman]]).
- Star/provider counts are **live-moving** (stars 20,307→20,322 within this session); cited with as-of dates.

## Key Takeaways
- All-Haiku workflow → **every load-bearing fact re-checked on Opus**; 2 empty verifiers fully compensated.
- Three independent re-verifications (contributors 257, AntiGravity removal, Kiro ToS) **upheld** the agents.
- The FALSE verdict is stated with a fairness nuance (expired promise, not proven deception).
- Related: [[claims-scorecard]] · [[source-provenance]]
