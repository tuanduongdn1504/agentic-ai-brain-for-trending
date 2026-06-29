## [2026-06-20] ingest+compile | omnilogin-ai-coding

# (C) Autopilot Loop — 2026-06-20-13

> **Trigger:** manual (operator-submitted YouTube URL + "double deep-dive into the original resource" + "pilot methods for my apply")
> **Topic:** omnilogin-ai-coding
> **Started:** 2026-06-20
> **Ended:** 2026-06-20
> **Mode:** single-video ingest (path 5 yt-dlp) + originals deep-dive + adversarial-verify workflow + compile + pilot-methods

## Source

- Video: "Omnilogin AI Coding: Mô Tả Bằng Tiếng Việt, AI Tự Viết Kịch Bản Auto Login Gmail | Không Cần Code" — [ySEOr1q-Ve4](https://www.youtube.com/watch?v=ySEOr1q-Ve4)
- Channel: Omnilogin · 2026-04-23 · 10:26 · 1,349 views · Vietnamese
- Transcript: `yt-dlp --write-auto-subs vi` → `bin/vtt-to-md.py` (158 cue lines, 14 timestamped paragraphs). ffmpeg absent (warned, irrelevant — captions only).

## What it is

Vendor tutorial for **Omnilogin's "AI Coding" feature**: describe an automation in natural Vietnamese → LLM generates a complete **Script + config UI + Output pane**; BYO-model (provider type / base URL / API key / model + thinking toggle); demo model = **Kimi/Moonshot**; demo task = auto-login Gmail across antidetect-browser profiles, then scale across profiles concurrently. Omnilogin = antidetect browser (multi-account; affiliate/MMO/e-commerce).

## Deep-dive of originals (operator's "double deep-dive" ask)

Workflow `wf_1ac2a814-456` — 6 research facets, each piped through an adversarial verify stage. 24 agents, 334 tool calls, ~803K subagent tokens, ~4.6 min wall-clock.
1. Omnilogin product (antidetect browser, competitors, pricing, 3 automation surfaces)
2. AI Coding feature architecture (script/UI/output, BYOM, iterate-fix loop, scale-out)
3. Kimi/Moonshot model (K2.6→K2.7-Code, benchmarks, vs Claude) — meatiest
4. Kimi/Moonshot API (OpenAI-compat, base URLs, model strings, thinking param, pricing, $39-plan reality)
5. NL→script+self-config-UI pattern (generative UI / A2UI; vs Playwright codegen / RPA / browser agents)
6. BYO-model / OpenAI-compatible standard (Ollama/OpenRouter/LiteLLM; key-security)

## Verify corrections (Rule 12 fail-loud)

- "$39 plan required to use Kimi" → $39 = Allegretto *consumer* tier; **API is separate pay-as-you-go from the console** (kimi.com has 5 tiers, not 4 — "4" = paid only).
- "disable thinking" → real `thinking.type:"disabled"` on K2.5/K2.6; **K2.7-Code (Jun 2026, post-video) always thinks, errors if disabled**.
- circulating "K2.7-Code 60.4% SWE-bench Verified" → **REFUTED** (no independent SWE-bench; Moonshot-proprietary benchmarks only).
- "AI writes the complete script" (one-shot) → ~62% agentic task success; the iterate-fix loop is load-bearing.
- "agents generate their own config UI" → true but bounded to pre-approved component catalogs (A2UI/AG-UI).
- Omnilogin's "GoLogin trial-only" comparison → GoLogin has a permanent free plan (3 profiles).
- **Rule 7 conflict:** BYOM refuted by one agent (consumer marketing homepage hides config) vs confirmed by another (docs.omnilogin.net/en lists providers incl. OpenRouter/Custom) → **resolved CONFIRMED** (video shows fields + docs corroborate; homepage simplifies).

## ⚠️ Use-context flag

Demo's headline use (bulk automated Gmail login across antidetect profiles) conflicts with Google ToS. Wiki + pilot methods capture the **transferable engineering** (BYO-model, generative-UI, prompt discipline, verify loop, Kimi cost), **not** the account-farming use.

## Wiki articles created (10 files, NEW topic)

- wiki/omnilogin-ai-coding/_index.md (NEW)
- wiki/omnilogin-ai-coding/overview.md (NEW)
- wiki/omnilogin-ai-coding/omnilogin-product.md (NEW — original #1)
- wiki/omnilogin-ai-coding/ai-coding-feature.md (NEW — original #2)
- wiki/omnilogin-ai-coding/kimi-moonshot-deep-dive.md (NEW — original #3, meatiest)
- wiki/omnilogin-ai-coding/byo-model-openai-compatible.md (NEW — original #4)
- wiki/omnilogin-ai-coding/nl-to-automation-pattern.md (NEW — original #5)
- wiki/omnilogin-ai-coding/prompt-structure-discipline.md (NEW — original #6)
- wiki/omnilogin-ai-coding/video-to-original-crosswalk.md (NEW)
- wiki/omnilogin-ai-coding/source-provenance.md (NEW)
- wiki/_master-index.md (UPDATED — added omnilogin-ai-coding topic)
- raw/_inventory.md (UPDATED — +1 row)

## Pilot deliverable

- output/(C) 2026-06-20-omnilogin-ai-coding-pilot-methods.md — **16 ranked methods** (A cost/model-routing · B NL→script+UI pattern · C hireui Goal-#2 · D prompt/pipeline · E Scrum coaching) + skip-list + critic reframe.
- **Headline pilot:** A1 — a measured **Kimi-vs-Claude codegen bake-off** on the existing `evals/` harness (resolves cost + 3P-inference + eval-first in one pilot, produces a quality-per-dollar number). A2 — route via OpenRouter (scoped key). B5/C7 — the generate-script+config-UI pattern as a Claude Code skill → a hireui recruitment feature spec.

## Metric

- Cold-start NEW topic → primary gap (topic absent) closed; 10 articles + index + provenance + crosswalk. `gaps_closed_ratio` ≈ 1.0 for the topic; 6/6 originals deep-dived + verified.

## Stop reason

Single-topic manual request fully serviced (knowledge built + originals deep-dived + verified + pilot methods delivered).

## Suggested next action

Run **A1** this week: pay-as-you-go platform.kimi.ai key (NOT the $39 consumer plan) → wire Kimi K2.6 + Claude Sonnet into `evals/` over ~10 codegen tasks → quality-per-dollar table, via OpenRouter (A2) so the key is scoped. Operator can ask me to scaffold the bake-off in `sandbox/`. Per [[feedback_branch_wiki_ships_not_main]], this is on branch `autopilot-research` (already a working branch off main) — uncommitted; report for operator to commit/merge.
