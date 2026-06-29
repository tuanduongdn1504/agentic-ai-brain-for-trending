# Video → original crosswalk

Maps each claim/term in the video to its canonical original, the verification verdict, and what the video adds, simplifies, or omits. Verification: workflow `wf_1ac2a814-456` (24 agents). Full log: [source-provenance](source-provenance.md).

## Claim-by-claim

| Video says | Canonical original | Verdict | Note |
|---|---|---|---|
| "AI writes the whole automation script from a Vietnamese description" | Generative codegen ([nl-to-automation-pattern](nl-to-automation-pattern.md)) | **holds-with-correction** | Real agentic task success ~62%; the iterate-fix loop is required, not optional |
| Script + **UI code** + Output panes | Generative UI / A2UI / AG-UI ([nl-to-automation-pattern](nl-to-automation-pattern.md)) | **holds** | The UI-generation is the genuinely novel bit; bounded to component catalogs |
| BYO-model fields: provider type / base URL / API key / model | OpenAI-compatible config ([byo-model-openai-compatible](byo-model-openai-compatible.md)) | **confirmed** | Docs list ChatGPT/Claude/Gemini/DeepSeek/Grok/**OpenRouter**/Custom; homepage hides it |
| Demo model = **Kimi** | Moonshot AI ([kimi-moonshot-deep-dive](kimi-moonshot-deep-dive.md)) | **confirmed** | Video-era = K2.6; current coding flagship = K2.7-Code (Jun 2026) |
| Base URL for Kimi | `api.moonshot.ai/v1` (intl) / `.cn/v1` (China) | **confirmed** | Region-split; keys not interchangeable |
| **"disable thinking"** = faster + cheaper, less accurate | `thinking.type:"disabled"` | **partly-confirmed** | True on K2.5/K2.6; **K2.7-Code errors if disabled** (always thinks) |
| "Go to kimi.com, buy a plan (4 plans), I use the **$39** one" | kimi.com consumer tiers | **refuted/corrected** | 5 tiers (free + 4 paid); $39 = Allegretto **consumer** sub; **API is separate pay-as-you-go from the console** |
| (implied) Kimi is great for coding | Kimi benchmarks | **partly-confirmed** | K2.6 ties GPT-5.5 at 58.6% SWE-bench Pro; **K2.7-Code has no independent SWE-bench** — vendor numbers only; "60.4%" blog figure refuted |
| "No code, no drag-drop, no freelancer" | Three automation surfaces ([omnilogin-product](omnilogin-product.md)) | **holds** | AI Coding is one of three surfaces (no-code builder / SDK / AI) on a Puppeteer/Playwright/Selenium engine |
| Prompt should say what you HAVE / NEED / STEPS / UI / SAMPLE DATA | Spec-first prompting ([prompt-structure-discipline](prompt-structure-discipline.md)) | **holds** | Tight, teachable packaging of plan-first discipline |
| Run → check → ask AI to fix → re-run | Validation loop | **holds** | Standard harness verify-loop; load-bearing given ~62% draft accuracy |
| Author once → copy profile IDs → run N concurrently | Action Sync / batch ([omnilogin-product](omnilogin-product.md)) | **holds** | The generated config UI is what makes scaling = data entry |

## What the video ADDS (vs the bare originals)

- A **concrete, packaged** instance of generative-UI applied to browser automation (script + config form + output, in one screen).
- A clean **five-part prompt template** worth lifting verbatim.

## What the video SIMPLIFIES / GLOSSES

- Conflates **consumer subscription** with **API access** (the "$39 plan").
- Implies **one-shot generation**; reality is the **iterate-fix loop** (which it then shows anyway).
- Presents BYO-model as a Kimi-specific setup screen; it's the **universal OpenAI-compatible pattern**.

## What the video OMITS

- **Cost discipline at scale** — no token-cost math, no caching mention ([[claude-api-cost-optimization/_index]]).
- **Security** — pastes an API key into a closed-source app with no caveat ([byo-model-openai-compatible](byo-model-openai-compatible.md)).
- **ToS / legality** of bulk automated Gmail login across antidetect profiles.
- **When NOT to use AI** (the chef-vs-vending-machine judgment — [[ai-operating-system/_index]]).

## Cross-links

- [source-provenance](source-provenance.md) · [overview](overview.md) · [_index](_index.md)
