# Original #2 — The AI Coding feature (architecture)

## Source

The video itself (primary — it shows every screen), corroborated by [docs.omnilogin.net/en](https://docs.omnilogin.net/en) (model-provider list) and omnilogin.net feature pages. Workflow `wf_1ac2a814-456` facet 2 + verifications.

> **Conflict resolved (Rule 7):** one research agent *refuted* "AI Coding is BYO-model," because the **consumer marketing homepage** only says "describe what you need, the AI handles the rest" — the technical config is abstracted away. But the **video demonstrates the config fields directly**, and **docs.omnilogin.net/en explicitly lists the supported providers** (ChatGPT, Claude via Anthropic API incl. Opus 4, Gemini, DeepSeek, Grok, **OpenRouter**, **Custom AI**). → **BYO-model is confirmed.** The homepage simplifies; the docs + video are authoritative. (Logged in [source-provenance](source-provenance.md).)

## The interface (what's on screen)

Open Omnilogin → **Quy trình (Workflows)** → **AI Coding** → new process. Layout:

- **Left:** a **chat box** to talk to the AI (the iterate channel)
- **Bottom:** the **prompt input** box
- **Right pane, three tabs:**
  - **Script** — the generated automation code
  - **UI code** — a generated **config UI** (e.g., a textarea to paste the account list + sample data) so the script can be run with different inputs by a non-coder
  - **Output** — run results

The **UI code tab is the distinctive bit.** Most "AI writes code" tools stop at the Script. Here the agent also emits a small parameterized front-end for its own script — so the deliverable is a *re-runnable mini-app*, not just a code snippet. (This is the 2026 "generative UI" idea — see [nl-to-automation-pattern](nl-to-automation-pattern.md).)

## Bring-your-own-model config

Settings → Model → add a model. Fields:

| Field | Meaning |
|---|---|
| `provider type` | which provider family (ChatGPT / Claude / Gemini / DeepSeek / Grok / OpenRouter / Custom) |
| `provider name` | any nickname |
| `Base URL` | the endpoint to call (e.g., `https://api.moonshot.ai/v1` for Kimi) |
| `API key` | the access key |
| `model` | the **exact** model-name string (e.g., `kimi-k2.6`) |
| `disable thinking` *(Kimi)* | toggle: ON = faster + cheaper, accuracy may drop |

These fields are the **OpenAI-compatible BYO-model pattern** — see [byo-model-openai-compatible](byo-model-openai-compatible.md). The demo wires up **Kimi** (Base URL + a console API key + model name + the disable-thinking toggle).

## The generation + iterate-fix loop (the real workflow)

1. **Attach a profile** for the AI to use (e.g., profile 183) — generation is tested against a real browser session.
2. **Write the prompt** (see [prompt-structure-discipline](prompt-structure-discipline.md)) → Enter.
3. AI **plans, then generates** Script + UI code (the demo fast-forwards a multi-minute generation).
4. **Accept** the Script tab; **Accept** the UI code tab → saved.
5. **Verify:** clear the profile's data, re-run, check for errors. **If errors remain, ask the AI to fix in chat** — loop until clean.
6. Re-enter sample data → run → confirm success.

This is a **human-in-the-loop verify loop**, not one-shot generation — which matches reality: independent data puts agentic task success around ~62%, not 100% ([nl-to-automation-pattern](nl-to-automation-pattern.md)). The loop *is* the product, not a flaw.

## Scale-out (author once, run on N)

- Group management → create group "Gmail" → quick-create 2 profiles in it.
- Select all → bulk utility → **copy profile IDs** → paste into the generated input UI.
- Paste the account data → save.
- Set **concurrency** (e.g., 2 simultaneous), select profiles **by group** → **Run** → both complete.

The generated UI is what makes this clean: the script was authored once, and the **config form** is where per-run inputs (profile IDs, account list) get supplied — so scaling is data entry, not re-coding.

## Key takeaways

- The artifact is a **triple**: code + a parameterized config UI + an output view. The UI is what turns a script into a re-runnable tool for non-coders.
- It's **BYO-model over OpenAI-compatible endpoints** — confirmed by docs (providers incl. OpenRouter + Custom) and the on-screen fields, despite the marketing homepage abstracting it away.
- The workflow is **generate → accept → verify → fix-in-chat → scale**, a classic validation loop. The model writes the draft; the human gates correctness.
- Generation is tested **against a real attached browser profile**, not in the abstract — grounding the codegen in a live target.

## Cross-links

- [kimi-moonshot-deep-dive](kimi-moonshot-deep-dive.md) — the model behind the Base URL
- [byo-model-openai-compatible](byo-model-openai-compatible.md) — why these exact config fields
- [nl-to-automation-pattern](nl-to-automation-pattern.md) — the "self-config UI" as generative UI; comparison to Playwright codegen / RPA / browser agents
- [prompt-structure-discipline](prompt-structure-discipline.md) — the prompt that drives step 2
- [[harness-engineering/_index]] — the verify-loop as harness discipline
