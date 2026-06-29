# Pilot methods — applying the Omnilogin AI Coding / Kimi knowledge to your working flows

> **Source:** [[omnilogin-ai-coding/_index]] — Omnilogin "AI Coding" video ([ySEOr1q-Ve4](https://www.youtube.com/watch?v=ySEOr1q-Ve4)) + deep-dives of the originals ([Omnilogin](https://www.omnilogin.net), [Kimi/Moonshot](https://platform.kimi.ai/docs), the [OpenAI-compatible BYO-model standard](https://platform.kimi.ai/docs/api/overview), [generative-UI / A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)). Verification: [[omnilogin-ai-coding/source-provenance]] (workflow `wf_1ac2a814-456`, 24 agents).
> **Date:** 2026-06-20.
> **Your flows:** **(A)** cost & model-routing (your active [[claude-api-cost-optimization/_index]] + [[cowork-third-party-inference/_index]] threads) · **(B)** the NL→script+config-UI pattern (a Claude Code skill) · **(C)** **hireui** — Goal-#2 SaaS (no LLM yet → build-it-right) · **(D)** prompt discipline + the autopilot pipeline · **(E)** Scrum coaching / citizen automation.
> **16 methods, ranked.** Each has the source pattern, a concrete first step, and a success signal.
>
> **The headline:** the video is a *sales demo for an antidetect browser*, but strip the product and three first-class engineering patterns fall out — **(1) BYO-model over an OpenAI-compatible base URL** (Kimi is just one more provider; this is your existing cost + 3P-inference lever), **(2) "generate the script *and* its config UI"** (= 2026 generative-UI; the shape of a hireui recruitment feature), **(3) the spec-first prompt + iterate-fix verify loop** (the real moat — which you already practice). **Don't adopt Omnilogin. Adopt its architecture in your own Claude-native stack**, where you own the keys, the routing, and the data.

---

## ▶ Start here (recommended sequence)

1. **This week, highest leverage, produces a number:** **A1** — a **Kimi-vs-Claude codegen bake-off** using your existing `evals/` harness. Add Kimi (`api.moonshot.ai/v1`, OpenAI-compatible) as a provider, run ~10 real codegen tasks, score quality *and* cost. This single pilot resolves three open threads at once (cost / 3P-inference / eval-first) and gives you a defensible "is the 5–8× cheaper model good enough for *my* tasks?" answer — instead of trusting unaudited vendor benchmarks.
2. **Alongside it, the secure plumbing:** **A2** — route through **OpenRouter** (one scoped, rotatable key) instead of pasting raw provider keys into anything. This is the security fix the video skips.
3. **The keeper idea, as a reusable skill:** **B5** — make *"generate the script + its config UI + sample data"* a Claude Code skill, encoding the **HAVE/NEED/STEPS/UI/SAMPLE-DATA** template. Then **C7** turns that exact shape into a hireui recruitment-automation feature spec (Goal #2).

---

## Ranked table

| # | Method | Flow | Effort | Value | Why it ranks here |
|---|---|---|---|---|---|
| **A1** | Kimi-vs-Claude codegen **bake-off** on your `evals/` harness | A cost | **Med** | **High** | Resolves cost + 3P-inference + eval-first in one measured pilot; produces a real number |
| **A2** | Route models via **OpenRouter** (scoped key), not raw keys | A cost | Low | **High** | The security fix the video skips; one key, many models, rotatable |
| **B5** | "Generate script **+ config UI + sample data**" as a Claude Code skill | B pattern | Med | **High** | The genuinely-novel keeper; turns one-off scripts into re-runnable tools |
| **C7** | Spec a hireui **"describe screening step → generated automation + form"** feature | C hireui | Med | **High** | Goal #2; = this pattern + [[multi-agent-orchestration/_index]] job-screener; build-it-right (no LLM yet) |
| **C8** | BYO-model + **local-Ollama-for-PII** as hireui architecture | C hireui | Med | **High** | Candidate-PII sovereignty; ties [[cowork-third-party-inference/_index]] |
| **A3** | Cross-provider **prompt caching** (Kimi cache ~$0.10–0.16/M) | A cost | Low | Med–High | Same lever as your cost topic, now provider-agnostic |
| **B6** | The **iterate-fix verify loop** as the codegen acceptance gate | B pattern | Low | Med–High | ~62% draft accuracy → the loop is load-bearing, not optional |
| **D11** | Adopt **HAVE/NEED/STEPS/UI/SAMPLE-DATA** as a codegen prompt template | D prompt | Low | Med–High | Cheap, teachable, lifts first-shot quality everywhere |
| **A4** | Conscious **thinking-vs-no-thinking** tier rule (K2.6 vs K2.7-Code) | A cost | Low | Med | Deliberate speed/cost/accuracy routing per task |
| **D12** | **Model-tier the autopilot pipeline** (cheap Kimi for compile, Claude for synthesis) | D pipeline | Med | Med | Cuts pipeline cost on the mechanical steps |
| **C9** | **ToS-safe** recruitment browser automation (official APIs/consented only) | C hireui | Low | Med | Keeps Goal #2 on the right side of platform terms |
| **C10** | **Local-first + opt-in-cloud** candidate-data posture | C hireui | Low (note) | Med | Borrow Omnilogin's defensible privacy default |
| **E13** | "Describe → AI builds it, no code" as **citizen-automation** enablement | E coaching | Med | Med | + chef-vs-vending-machine judgment for teams |
| **E14** | Teach the **BYO-model mental model** (base URL + key + model = swap any brain) | E coaching | Low | Med | Model choice = config + cost lever + data-trust decision |
| **E15** | Teach **spec-first + verify-loop** is the moat, not the model | E coaching | Low | Med | The real lesson under the demo |
| **E16** | Teach **"own your keys"** security literacy | E coaching | Low | Med | Don't paste secrets into closed apps; scope + rotate |

---

## A — Cost & model routing (your active threads)

> The video's "add a model" screen is the universal **OpenAI-compatible BYO-model** form ([[omnilogin-ai-coding/byo-model-openai-compatible]]). Kimi is one provider behind a base URL. This is the same lever as your [[cowork-third-party-inference/_index]] (swap the model under the harness) and [[claude-api-cost-optimization/_index]] (cut the bill) work — now with a concrete, ~5–8×-cheaper candidate to *measure*.

### A1 — Kimi-vs-Claude codegen bake-off on your `evals/` harness ⭐
- **Pattern:** BYO-model swap ([[omnilogin-ai-coding/kimi-moonshot-deep-dive]]) + your eval-first discipline ([[prompt-evaluation/_index]]). Kimi is OpenAI-compatible (`base_url=https://api.moonshot.ai/v1`), so it's a one-line provider change.
- **Apply:** don't trust the vendor numbers (K2.7-Code has **no independent SWE-bench**; "60.4%" is a refuted blog figure). Measure on *your* codegen tasks.
- **First step:** get a **platform.kimi.ai API key** (pay-as-you-go from the console — **not** the $39 consumer plan); pick ~10 representative codegen tasks; run **Kimi K2.6** and **Claude Sonnet** through your `evals/` harness, scoring quality + recording $/task.
- **Success signal:** a **quality-per-dollar table** for your own tasks → a defensible decision (use Kimi as a cheap tier / fallback / not at all). Note the practitioner caveat: Kimi tends to over-refactor; your eval will catch it if so.

### A2 — Route via OpenRouter (scoped key), not raw keys ⭐
- **Pattern:** the BYO-model security angle ([[omnilogin-ai-coding/byo-model-openai-compatible]]) — handing any app a raw provider key = full spend authority + read access. OpenRouter (`openrouter.ai/api/v1`) gives one scoped, rotatable key over hundreds of models.
- **Apply:** put a gateway between you and providers so swapping models is config and keys are disposable.
- **First step:** create an OpenRouter key with a spend cap; point your sandbox / `claude-cost-arc` at `openrouter.ai/api/v1`; run the A1 bake-off through it (Kimi + 1–2 others).
- **Success signal:** model swap = a string change; a leaked key costs ≤ the cap and is rotated in seconds.

### A3 — Cross-provider prompt caching
- **Pattern:** Kimi cache-hit input ~$0.10–0.16/M (≈80% off) — same lever as [[claude-api-cost-optimization/_index]], provider-agnostic.
- **Apply:** in any repeated-system-prompt workflow, cache the stable prefix.
- **First step:** in the A1 bake-off, enable caching on the shared system prompt; measure cached vs uncached cost.
- **Success signal:** cached input bills ~80% less; the saving holds across providers.

### A4 — Conscious thinking-vs-no-thinking tier rule
- **Pattern:** `thinking.type:"disabled"` trades accuracy for speed+cost — **works on K2.6, errors on K2.7-Code** ([[omnilogin-ai-coding/kimi-moonshot-deep-dive]]).
- **Apply:** route cheap/mechanical tasks to a no-thinking (or cheaper) tier; reserve full reasoning for hard ones — the model-for-judgment-only discipline ([[claude-md-12-rules/_index]] Rule 5).
- **First step:** write a 3-line routing rule (which task classes get thinking on/off / which model).
- **Success signal:** you choose reasoning depth per task on purpose, not by default.

---

## B — The NL→script+config-UI pattern (a Claude Code skill)

> The genuinely novel bit isn't "AI writes code" — it's that the agent emits the **script + a config UI + sample data**, making the artifact a re-runnable tool ([[omnilogin-ai-coding/nl-to-automation-pattern]]). That's 2026 generative-UI (A2UI/AG-UI).

### B5 — "Generate script + config UI + sample data" as a skill ⭐
- **Pattern:** generative UI + the five-part prompt ([[omnilogin-ai-coding/prompt-structure-discipline]]).
- **Apply:** when Claude builds you a one-off automation/script, have it *also* emit a tiny parameterized runner (CLI flags / a small form) + sample data — so future-you (or a non-coder) re-runs it by changing inputs, not editing code.
- **First step:** use `anthropic-skills:skill-creator` to make a `gen-runnable-automation` skill encoding HAVE/NEED/STEPS/UI/SAMPLE-DATA + "emit a config surface + sample data + a verify step."
- **Success signal:** a script you generated weeks ago is re-runnable on new inputs via its form/flags, untouched.

### B6 — Iterate-fix verify loop as the codegen acceptance gate
- **Pattern:** the video's run→check→fix-in-chat loop ([[omnilogin-ai-coding/ai-coding-feature]]); harness validation loops ([[harness-engineering/_index]]); Rule 9 ([[claude-md-12-rules/_index]]).
- **Apply:** treat generated automation as a **draft** (~62% correct) until it runs clean on a *fresh* input; bugs go back to the model with the error.
- **First step:** add "generated automation is not 'done' until it runs clean on a held-out input" to your codegen checklist / the B5 skill.
- **Success signal:** nothing generated is accepted without a clean verify run on unseen data.

---

## C — hireui (Goal #2, the real build target)

> hireui has its own CONSTITUTION (agent-* branch policy, operator-only skill registry, GitNexus-first) + BMAD + `.pilot-log`, and **no LLM integration yet** — so this is **build-it-right**, not retrofit. Follow hireui's rules, not the vault's.

### C7 — Spec the "describe screening step → generated automation + form" feature ⭐
- **Pattern:** the NL→script+config-UI pattern ([[omnilogin-ai-coding/nl-to-automation-pattern]]) = a recruiter-operable version of [[multi-agent-orchestration/_index]]'s job-application-screener.
- **Apply:** a recruiter describes a screening/outreach step in plain language → hireui generates a **parameterized, re-runnable automation + its config form** (source, criteria, output). Decouple agent reasoning from UI (testable/portable); semantic intent replaces hard-coded rules (adapts to new job specs without redeploy).
- **First step:** write a one-page feature spec in hireui's `_bmad-output` (respecting its CONSTITUTION), citing this wiki + the multi-agent job-screener; mark the model layer as BYO (→ C8).
- **Success signal:** a spec a recruiter could operate and an engineer could build, with a verify-loop gate baked in.

### C8 — BYO-model + local-Ollama-for-PII as hireui architecture ⭐
- **Pattern:** OpenAI-compatible provider abstraction ([[omnilogin-ai-coding/byo-model-openai-compatible]]) + data-sovereignty ([[cowork-third-party-inference/_index]]).
- **Apply:** route hireui's (future) LLM calls through a swappable layer (LiteLLM / your own gateway) — **Claude for quality, OpenRouter for cost, local Ollama for candidate-PII** flows that shouldn't leave your infra.
- **First step:** add a provider-abstraction note to hireui's runbooks (alongside the existing `claude-api-cost-optimization-spec`): never hardcode a vendor; PII flows default to local; keys are scoped per component.
- **Success signal:** hireui's first LLM feature ships behind a swappable, key-scoped layer — not a hardcoded vendor SDK.

### C9 — ToS-safe recruitment browser automation
- **Pattern:** Omnilogin runs on Puppeteer/Playwright/Selenium ([[omnilogin-ai-coding/omnilogin-product]]) — but the demo's bulk-Gmail use violates ToS. The *runtime* is fine; the *use* must be sanctioned.
- **Apply:** for recruitment automation, use **official APIs / candidate-consented imports / your own ATS** — not at-scale scraping of LinkedIn etc.
- **First step:** enumerate which hireui automations are ToS-safe (own data, consented flows) vs not, before any build.
- **Success signal:** a sanctioned-automation allowlist exists; no feature depends on a ToS-violating data source.

### C10 — Local-first + opt-in-cloud candidate-data posture
- **Pattern:** Omnilogin's local-first + optional encrypted backup default ([[omnilogin-ai-coding/omnilogin-product]]).
- **Apply:** for sensitive candidate data, default to your-DB + encrypted opt-in sync rather than third-party-cloud-only — a defensible privacy stance for a recruitment SaaS.
- **First step:** record the posture in hireui's data-architecture docs as an explicit decision.
- **Success signal:** PII handling is a documented choice, not an accident of which SaaS you wired in first.

---

## D — Prompt discipline + the autopilot pipeline

### D11 — Adopt HAVE / NEED / STEPS / UI / SAMPLE-DATA as a codegen prompt template
- **Pattern:** the presenter's five-part prompt ([[omnilogin-ai-coding/prompt-structure-discipline]]) — spec-before-generation; the non-obvious wins are *ask for the config UI* + *give sample data*.
- **Apply:** drop it in front of any "generate an automation/script" task.
- **First step:** add the 5-line template to your prompt library (and the B5 skill).
- **Success signal:** first-shot codegen needs fewer fix rounds.

### D12 — Model-tier the autopilot pipeline
- **Pattern:** cheap model for mechanical work, strong model for judgment ([[claude-md-12-rules/_index]] Rule 5; [[claude-api-cost-optimization/_index]] advisor strategy).
- **Apply:** route a mechanical pipeline phase (e.g., raw→draft compile) through Kimi/OpenRouter; keep Claude for synthesis/audit.
- **First step:** in a sandbox, run one `yt-pipeline`/compile phase through Kimi; eval the output vs the Claude baseline.
- **Success signal:** pipeline cost drops on the cheaped step with no quality regression (verified, not assumed).

---

## E — Scrum coaching / citizen automation

### E13 — "Describe → AI builds it, no code" as citizen-automation enablement
- **Pattern:** the whole demo's promise, plus the **chef-vs-vending-machine** judgment ([[ai-operating-system/_index]]) — when AI vs plain automation.
- **Apply:** show a team how a non-engineer can ship a small automation *with a verify loop*, and where that's the wrong tool.
- **First step:** a one-pager / live demo for one team using a real (ToS-safe) task.
- **Success signal:** a non-engineer ships a small automation and knows when *not* to.

### E14 — Teach the BYO-model mental model
- **Pattern:** base URL + key + model = swap any brain ([[omnilogin-ai-coding/byo-model-openai-compatible]]).
- **Apply:** the most freeing concept for teams — model choice is a config string, a cost lever, *and* a data-trust decision.
- **First step:** one slide: same code, three providers (Claude / OpenRouter / local Ollama).
- **Success signal:** the team reasons about model choice instead of treating it as fixed.

### E15 — Teach "the moat is spec-first + the verify loop, not the model"
- **Pattern:** what actually made the demo work wasn't Kimi — it was the HAVE/NEED/STEPS prompt + the run→check→fix loop ([[omnilogin-ai-coding/overview]]).
- **Apply:** use the video as a case study against one-shot-magic expectations.
- **First step:** a 10-min teardown: "spot the two things that made this work."
- **Success signal:** people stop expecting one-shot results and start writing specs + verifying.

### E16 — Teach "own your keys" security literacy
- **Pattern:** the video pastes a raw API key into a closed app with no caveat ([[omnilogin-ai-coding/byo-model-openai-compatible]]).
- **Apply:** scope keys per component, store in env, rotate on compromise, prefer a gateway over pasting master keys into binaries.
- **First step:** add the "never paste a master key into a third-party app" rule to your team's AI-usage guide.
- **Success signal:** keys in use are scoped + rotatable, not master keys in someone else's app.

---

## What to consciously SKIP (and why) — the discipline half

- **Omnilogin itself + the antidetect/bulk-account use case** — orthogonal to your domain and ToS-fraught. Take the architecture, not the product.
- **The "$39 consumer plan to use Kimi" framing** — API is **pay-as-you-go from the console**, separate from the consumer subscription. Don't buy the consumer tier for API access.
- **Trusting Kimi's coding benchmarks** — K2.7-Code has *no* independent SWE-bench; pilot on *your* eval set (A1) before believing any number.
- **Pasting raw provider keys into closed apps** — use a scoped OpenRouter/gateway key (A2). This is the one anti-pattern in the video.
- **Defaulting to Kimi over Claude** — the cost win is real but instruction-following is reportedly weaker and context is smaller (256K vs ~1M). It's a *tier/fallback*, decided by A1 — not a swap.
- **Expecting one-shot generation** — ~62% draft accuracy; the verify loop is mandatory (B6).

## Critic's reframe (the contrarian read)

A skeptic would say: *this is a low-view vendor ad for an account-farming tool — why mine it at all?* Fair. But the reason it's worth your time is that it shows, in one 10-minute screen recording, the **commoditization of three things you're already investing in**: model-swapping (BYO-model is now a default UI affordance, not a hack), agent-generated UIs (the artifact is becoming a *tool*, not a snippet), and the spec+verify discipline (even a marketing demo can't escape the fix loop). The sharpest takeaway is **inversion**: the model is the *commodity* (Kimi at 5–8× less, one base-URL away), and the **durable value is the harness around it** — your eval set, your gateway, your prompt template, your verify loop, your data posture. That's exactly the [[harness-engineering/_index]] thesis. So the move isn't "use Kimi" — it's *"prove, with A1, whether the cheap model clears your bar, behind plumbing you own (A2/C8), driven by discipline you already have (B6/D11)."* If Kimi clears the bar, you've cut a cost; if it doesn't, you've got evidence — either way the harness wins.

## Cross-links

- [[omnilogin-ai-coding/_index]] (source topic) · [[omnilogin-ai-coding/overview]] · [[omnilogin-ai-coding/source-provenance]] (what's verified).
- Composes with: [[cowork-third-party-inference/_index]] (swap the model under the Claude harness — first-party) · [[claude-api-cost-optimization/_index]] (the cost lever + advisor tiering) · [[prompt-evaluation/_index]] (the bake-off harness) · [[multi-agent-orchestration/_index]] (the job-screener C7 fronts) · [[harness-engineering/_index]] (own-the-harness thesis) · [[self-hosted-devops-oss/_index]] (own-your-keys/secrets).

## Suggested next action

Do **A1 this week** — get a pay-as-you-go **platform.kimi.ai** API key (not the $39 consumer plan), wire **Kimi K2.6** + **Claude Sonnet** into your `evals/` harness over ~10 real codegen tasks, and produce a **quality-per-dollar table**. Run it through **OpenRouter** (A2) so the key is scoped from day one. Say the word and I'll **scaffold the bake-off** in `sandbox/` — provider config, the task set, and the eval-scoring wrapper — so you just drop in keys and run.
