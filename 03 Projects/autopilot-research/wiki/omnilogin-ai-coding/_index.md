# omnilogin-ai-coding

> **Topic index.** Maintained per `../../CLAUDE.md` librarian rules.
> **Source:** Omnilogin channel video "Omnilogin AI Coding: Mô Tả Bằng Tiếng Việt, AI Tự Viết Kịch Bản Auto Login Gmail | Không Cần Code" ([ySEOr1q-Ve4](https://www.youtube.com/watch?v=ySEOr1q-Ve4), 2026-04-23, 10:26, Vietnamese, 1,349 views) — a vendor tutorial. Raw: [2026-06-20-omnilogin-ai-coding.md](../../raw/2026-06-20-omnilogin-ai-coding.md).
> **Compiled:** 2026-06-20 (path 5 yt-dlp transcript + direct primary-source fetch + adversarial verification workflow `wf_1ac2a814-456`, 24 agents).

## What this topic is

A Vietnamese vendor demo of **Omnilogin's "AI Coding" feature** — describe an automation task in plain language, an LLM writes the **complete script + a config UI + an output pane**, no coding required (demo: auto-login Gmail across antidetect-browser profiles, using **Kimi / Moonshot AI** as the model via a bring-your-own-model API config).

Per the operator's **"double deep-dive into the original resource"** ask, this topic does **not** stop at the video. It deep-dives the originals the demo stands on:

1. **Omnilogin** — the antidetect browser itself ([omnilogin-product](omnilogin-product.md))
2. **The AI Coding feature** — how generation + the script/UI/output panes + the iterate-fix loop actually work ([ai-coding-feature](ai-coding-feature.md))
3. **Kimi / Moonshot AI** — the model line, OpenAI-compatible API, pricing, the "disable thinking" parameter ([kimi-moonshot-deep-dive](kimi-moonshot-deep-dive.md)) — *the meatiest original*
4. **The BYO-model / OpenAI-compatible standard** the config fields come from ([byo-model-openai-compatible](byo-model-openai-compatible.md))
5. **The "NL → script + self-config UI + output" pattern** itself, vs Playwright codegen / RPA / browser agents ([nl-to-automation-pattern](nl-to-automation-pattern.md))
6. **The prompt-structure discipline** the presenter teaches ([prompt-structure-discipline](prompt-structure-discipline.md))

## ⚠️ Use-context flag

The demo's headline use case — **bulk automated Gmail login across many antidetect profiles** — sits in the multi-account / "MMO" space that commonly conflicts with platform Terms of Service (Google prohibits automated/bulk account access). This wiki captures the **transferable engineering** (generation pattern, BYO-model config, Kimi cost angle, prompt discipline, verify loop), **not** the bulk-account-farming use case. The pilot methods are scoped accordingly.

## Articles

- [overview](overview.md) — the whole thing in one page + the decision lens
- [omnilogin-product](omnilogin-product.md) — **original #1**: antidetect browser, competitors, pricing, automation surfaces
- [ai-coding-feature](ai-coding-feature.md) — **original #2**: the AI Coding architecture (script/UI/output, BYOM, iterate-fix loop, scale-out)
- [kimi-moonshot-deep-dive](kimi-moonshot-deep-dive.md) — **original #3**: Kimi K2.6→K2.7-code, OpenAI-compat API, base URLs, pricing, the thinking toggle, vs Claude
- [byo-model-openai-compatible](byo-model-openai-compatible.md) — **original #4**: why every app exposes `base URL + key + model`; OpenRouter/Ollama/LiteLLM; the security angle
- [nl-to-automation-pattern](nl-to-automation-pattern.md) — **original #5**: generative UI / A2UI / AG-UI; vs Playwright codegen / classic RPA / Skyvern-Browser-Use-Stagehand; what's genuinely novel
- [prompt-structure-discipline](prompt-structure-discipline.md) — **original #6**: the HAVE / NEED / STEPS / UI / SAMPLE-DATA template
- [video-to-original-crosswalk](video-to-original-crosswalk.md) — every video claim → canonical original → verification verdict → what the video adds/omits
- [source-provenance](source-provenance.md) — verification log, conflicts resolved, video-only claims flagged

## Pilot methods

`output/(C) 2026-06-20-omnilogin-ai-coding-pilot-methods.md` — **16 ranked methods** across cost/model-routing · the NL→script+UI pattern · hireui Goal #2 · prompt discipline · Scrum coaching, plus a skip-list and a critic's reframe.

## Cross-links

- [[cowork-third-party-inference/_index]] — sister topic: the same BYO-model / OpenAI-compatible lever, first-party (Cowork on 3P + Ollama + OpenRouter). Kimi is just one more provider behind a base URL.
- [[claude-api-cost-optimization/_index]] — Kimi's ~5–8× cheaper tokens + prompt-caching = the same cost discipline, cross-provider.
- [[prompt-evaluation/_index]] — the eval harness to actually compare Kimi vs Claude on *your* codegen tasks before trusting vendor benchmarks.
- [[multi-agent-orchestration/_index]] — the video's job-screener-shaped demo ≈ a hireui recruitment-agent feature.
- [[graphify-codebase-graph/_index]] / [[claude-code-clones/_index]] — OpenCode/Playwright codegen lineage of "generate automation from a description."
- [[self-hosted-devops-oss/_index]] — local/private inference + own-your-keys ethos.
