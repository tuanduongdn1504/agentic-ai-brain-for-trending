# (C) page-agent — Deep Dive (LLM Wiki v199)

> **Subject:** `alibaba/page-agent` — *"The GUI Agent Living in Your Webpage. One script gives any web page its own AI agent."*
> **Source-verified at commit `35ff6d4`** (2026-07-07), v1.11.0, MIT. Author **Simon** (`gaomeng1900` / X `@simonluvramen` / © "SimonLuvRamen") + **Alibaba Group Holding** (official `alibaba/` org repo).
> Built for LLM Wiki v199, 2026-07-08. Verdict + all corpus/collision/identity claims done **by hand** per `feedback_wiki_verify_independently_check_collisions`; a read-only 8-agent workflow (`wf_cf35685e-abb`, ~1.43M tok, 8/8 done / 0 errors / 1 empty) did **source-reading + upstream research ONLY**.

---

## 1. The one-sentence thesis

Every other web-agent in this vault drives a browser **from the outside** (browser-use v41, Skyvern v24, crawl4ai v29 — an external Python/Playwright process controlling a headless or remote browser, for a **developer or a coding agent**). page-agent inverts that: it is a **~50–100 KB client-side JavaScript library that a web-app owner drops into their own site** (`<script>` tag or `npm install`), which then gives **that site's end users** a natural-language agent that reads and drives the app's **own real DOM** — no browser extension, no Python, no headless browser, no backend, no screenshots.

> **The distinction the README itself draws:** *"`PageAgent` is designed for **client-side web enhancement**, not server-side automation."*

It is, in a phrase, **"browser-use, but living inside the page instead of driving it from outside"** — and it says so: the README credits browser-use as its foundation and the source literally tags the tool definitions `@note Adapted from browser-use`.

---

## 2. Identity, license, provenance (hand-verified)

| Field | Value |
|---|---|
| Repo | `github.com/alibaba/page-agent` (official Alibaba GitHub org) |
| Tagline | *"JavaScript in-page GUI agent. Control web interfaces with natural language."* / About: *"The GUI Agent Living in Your Webpage. One script gives any web page its own AI agent."* |
| License | **MIT** (© 2026 SimonLuvRamen + © 2026 Alibaba Group Holding Limited) |
| Author | **Simon** — GitHub `gaomeng1900`, X `@simonluvramen`, © "SimonLuvRamen"; an Alibaba engineer (this is an official Alibaba open-source project). *Fuller identity details unverified — the identity research agent returned empty; not relied upon.* |
| Languages | TypeScript 82.6% / JavaScript 11.8% / CSS 4.4% / HTML 1.2% |
| Version | **v1.11.0** (2026-07-03); **34 releases**; first commit **2025-09-23** ("Initial commit"), `feat: init` 2025-09-29 |
| Stars/forks | ~25k★ / ~2.1k forks (**page-stated §37.4 — NOT API-verified → NOT a Pattern #52 velocity claim**); Trendshift badge (repo 22551); HN discussion (item 47264138); MarkTechPost + author's Medium coverage |
| npm | `page-agent` (+ `@page-agent/core`, `@page-agent/mcp`, `@page-agent/llms`, `@page-agent/page-controller`, `@page-agent/ui`) |
| Files | 246 tracked; source-first npm-workspaces monorepo |
| Homepage / demo | https://alibaba.github.io/page-agent/ |

**Corpus-recursive provenance (load-bearing, source-verified):** the README carries a NOTICE-style credit —

> *"This project builds upon the excellent work of `browser-use`. … DOM processing components and prompt are derived from browser-use. Browser Use <github.com/browser-use/browser-use> Copyright (c) 2024 Gregor Zunic. Licensed under the MIT License."*

and `packages/core/src/tools/index.ts` opens with `@note Adapted from browser-use`, with the `scroll` tool tagged `@note Reference from browser-use`. **browser-use is corpus subject v41** (and the org that built v198 video-use). This is a genuine influence-derivation lineage (see §11).

---

## 3. Architecture — the 8-package monorepo

Clean, decoupled module boundaries (source-first workspaces; library `package.json` exports point at `src/*.ts` in dev, `dist/*.js` when published):

| Package | npm | Role | ~LOC (TS) |
|---|---|---|---|
| **core** | `@page-agent/core` | `PageAgentCore` — the **headless** ReAct agent loop, tools, prompts, config | 1,878 |
| **page-agent** | `page-agent` | Main entry: `PageAgent` extends `PageAgentCore` + built-in UI Panel + demo IIFE builds | 93 (thin) |
| **llms** | `@page-agent/llms` | OpenAI-compatible LLM client — retries, per-provider patching, token accounting | 1,503 |
| **page-controller** | `@page-agent/page-controller` | **DOM extraction + dehydration + action execution + SimulatorMask** — *no LLM dependency* | 2,226 |
| **ui** | `@page-agent/ui` | Panel + i18n, decoupled via a `PanelAgentAdapter` interface | 1,028 |
| **mcp** | `@page-agent/mcp` | **MCP server (Beta)** — lets an *external* agent client drive the in-page agent | (JS) |
| **extension** | — | Chrome extension (WXT + React) for **multi-page/multi-tab** tasks | 4,976 |
| **website** | `@page-agent/website` (private) | React docs + landing + dev playground | — |

The load-bearing separation: **`page-controller` has no LLM dependency** and **`llms` has no page dependency**. The agent brain (core) sits between them. That means the DOM engine is a reusable "give me the page as indexed text / click element N" library independent of any model, and the LLM client is a reusable OpenAI-compatible caller independent of the browser. This is why the same core runs in-page *and* inside the Chrome extension's `MultiPageAgent`.

---

## 4. The ReAct loop (`PageAgentCore.execute`) — source-verified

The loop, from the class doc-comment and `execute()`:

```
step:
  observe  → pageController.getBrowserState()  (refreshes the DOM tree)
  think    → LLM call:
               reflection (evaluate previous step / memory / next_goal)
             + action     (one tool from the tool set)
  act      → execute the chosen tool (by element index)
loop  (until `done`, maxSteps=40, or abort)
```

Design details that matter:

- **One "MacroTool" call per step.** All tools are merged into a *single* forced tool call named `AgentOutput` (`toolChoiceName: 'AgentOutput'`), whose schema is `{ evaluation_previous_goal, memory, next_goal, action: <union of every tool's schema> }`. The model reflects **and** picks exactly one action in one structured call. `description: "You MUST call this tool every step!"`
- **Two information streams, deliberately separated.** *History events* (steps, observations, user-takeovers) are **persistent and fed back into the LLM context** as `<agent_history>`. *Activity events* (thinking / executing / retrying / error) are **transient, UI-only, NOT in context** — so the model's reasoning isn't polluted by transient UI chatter. Errors are recorded in history for the panel but **excluded from LLM context** "to avoid polluting the agent's reasoning with transient errors."
- **System observations injected before each step:** URL-change detection (`Page navigated to → …`), accumulated-wait warning (`You have waited N seconds… DO NOT wait any longer`), and remaining-step warnings at 5-left and 2-left. (Loop-detection is an explicit `@todo`.)
- **Human-in-the-loop is first-class.** An `ask_user` tool (disabled unless you wire an `onAskUser` callback), and a `user_takeover` history event (`"User took over control and made changes to the page"`) so a human grabbing the wheel becomes part of the agent's memory.
- **Lifecycle hooks:** `onBeforeTask / onAfterTask / onBeforeStep / onAfterStep / onDispose` (all async, all `@experimental`).
- **Cancellation is threaded everywhere:** one `AbortController` reaches the LLM fetch, every tool (`ctx.signal`), and async callbacks; `signal.throwIfAborted()` is enforced *even if a tool ignored the signal and resolved normally*.
- **`maxSteps` default 40, `stepDelay` default 0.4s.** As of v1.10.0, `stop()` is async and a distinct `stopped` state exists; LLM-self-reported failure still ends as `completed` (status ≠ task-outcome).

**The system prompt** (`packages/core/src/prompts/system_prompt.md`, browser-use-derived) is a disciplined, honest agent contract:
- The indexed-element format is taught inline: `[index]<type>text</type>`, `\t` = DOM child, `*[index]` = newly-appeared element since last step.
- **Honesty over success theatre** (near-verbatim): *"It is ok to fail the task. … Trying too hard can be harmful. … User would rather you complete the task with a fail."*; *"Never assume an action succeeded just because it appears to be executed"*; captcha → tell the user, don't try to solve it.
- **Single-page-app constraint:** *"You can only handle single page app. Do not jump out of current page. Do not click on link if it will open in a new page."* (Multi-page is the extension's job — §7.)

---

## 5. The DOM engine — "dehydration" (the double-deep-dive core)

This is the heart, and the part **derived from browser-use** but reimplemented in-page. Source-verified in `packages/page-controller/src/`:

1. **Extraction.** `PageController.updateTree()` calls `dom.getFlatTree()` → `processElementsV2()` (in `dom/dom_tree/index.js`) recursively walks the live DOM, running `isInteractiveElement()` on every node.
2. **Interactivity test** (`isInteractiveElement()`, a multi-signal pipeline): blacklist/whitelist → CSS `cursor` against a set of interactive cursors → tag whitelist (`a, button, input, select, textarea, details, summary, label, option, li`) → ARIA role → **event-listener detection** (`getEventListeners()` with an `on*`-attribute fallback) → `contenteditable` → **scrollable** (`scrollHeight − clientHeight ≥ 4px`). Scrollable elements are automatically interactive.
3. **Indexing.** A global counter assigns each interactive element a **stable numeric index** (starting at 1). The map from index → real `HTMLElement` is the `selectorMap`. **No CSS selectors, no XPath** reach the LLM — just integers.
4. **Dehydration.** `flatTreeToString()` renders the tree to the token-lean text the LLM actually sees:
   - `[index]<tag>text</tag>` per interactive element; `\t` indentation encodes DOM parentage; pure-text nodes have no `[index]`.
   - **`*[index]`** marks elements that appeared *since the last step* (tracked via a `WeakMap` of prior element references) — so the model can reason about what its last action changed.
   - Scrollable containers embed `data-scrollable='left=…,top=…,right=…,bottom=…'` so the model knows scroll room in every direction and can scroll a *specific* container by index.
5. **Action execution, by index:**
   - **click** → `getElementByIndex()` → dispatches the **full W3C pointer sequence** (`pointerover → mouseover → pointerdown → mousedown → focus → pointerup → mouseup → click`) with pass-through hit-testing gates, so it behaves like a real user click (frameworks listening on any of those events fire correctly).
   - **input_text** → Plan A (synthetic `focus` + set value + dispatch `input`/`change`) for `input`/`textarea`; Plan B (`execCommand` selectAll/insertText) for `contenteditable`.
   - **scroll / scroll_horizontally** → `scrollBy()` on the target element or the window, returns the new position.
   - **select_dropdown_option** → matches option by *text*, sets value, dispatches `change`.

**Why this matters (and the honest caveat):** DOM-as-text (vs screenshot) means **no multimodal model, no vision cost, works with text-only and local LLMs, far fewer tokens than a screenshot** — the `claude-api-cost-optimization` argument. **But** (landscape-verified) this is **not a page-agent innovation**: browser-use, Stagehand, and Playwright-MCP have all converged on text/accessibility-tree representations. page-agent inherits the technique from browser-use; its *own* novelty is the **in-page delivery**, not the text-DOM.

**SimulatorMask** (`SimulatorMask.ts`) — the "the agent is driving" affordance: a full-screen fixed overlay that blocks user interaction during a run, with an **animated AI cursor** (ripple/fill/border layers, 20%-per-frame easing via `requestAnimationFrame`) that visibly glides to and clicks elements. Coordinated by `window`-dispatched events (`PageAgent::MovePointerTo`, `PageAgent::ClickPointer`, `PageAgent::EnablePassThrough`, `PageAgent::DisablePassThrough`). Opt-in via `enableMask: true`.

**Engine caveats (source-flagged):** no cross-origin iframe support (main document + same-origin frames only); `getEventListeners()` isn't available in every context (falls back to `on*` attributes); the 4px scroll threshold is arbitrary; bounding-rect / xpath caches can go stale if the page reflows without an `updateTree()`.

---

## 6. The LLM client (`@page-agent/llms`) — provider-quirk-hardened

An OpenAI-compatible caller built to survive the messy reality of "bring your own model, including weak local ones":

- **BYOK / OpenAI-compatible:** `LLMConfig = { baseURL, model, apiKey?, maxRetries?, transformRequestBody?, disableNamedToolChoice?, customFetch? }`. Anything speaking the OpenAI `/chat/completions` shape works — OpenAI, **Anthropic Claude**, Qwen (dashscope), DeepSeek, Gemini, GLM, MiniMax, OpenRouter, **Ollama** (`http://localhost:11434/v1`).
- **Tool-calling:** `tool_choice` defaults to `'required'` (must call *some* tool) or is forced by name (`{type:'function', function:{name:'AgentOutput'}}`). `disableNamedToolChoice` exists **for models that reject the named form** (e.g. DeepSeek) — a real-world quirk workaround.
- **Per-provider patching:** `modelPatch()` + `normalizeModelName()` apply provider-specific request tweaks (Qwen / DeepSeek / **Claude** / Gemini / GLM / MiniMax …) and convert OpenRouter's `reasoning_effort` format. `temperature` is **deprecated** ("many models reject it outright" — use `transformRequestBody`).
- **Retries:** `maxRetries` default **2** (3 attempts total), **fixed 100 ms backoff** (not exponential — a caveat under load). A typed `InvokeError` taxonomy splits **retryable** (`NETWORK_ERROR, RATE_LIMIT, SERVER_ERROR, NO_TOOL_CALL, INVALID_TOOL_ARGS, TOOL_EXECUTION_ERROR, INVALID_RESPONSE, INVALID_SCHEMA, UNKNOWN`) from **non-retryable** (`CONFIG_ERROR, AUTH_ERROR, CONTEXT_LENGTH, CONTENT_FILTER`); `AbortError` is never retried.
- **Token accounting** in every result: `promptTokens, completionTokens, totalTokens, cachedTokens (prompt-cache hits), reasoningTokens` — the client is token-economy aware.

**`autoFixer` / `normalizeResponse`** (`core/src/utils/autoFixer.ts`) is the resilience layer that makes weak/local models usable. It repairs ≥5 classes of malformed responses before parse: JSON emitted in `message.content` instead of `tool_calls`; the model returning the *action name* as the tool call instead of `AgentOutput`; args double-JSON-stringified; nested-function-call shapes; **missing `action` → falls back to `wait`**; and `validateAction()` coerces primitive inputs for single-field tools (`{click_element_by_index: 2}` → `{click_element_by_index: {index: 2}}`). This is the unglamorous glue that lets a 14B local model drive a real UI.

**Claude support is first-class and tested** (hand-read `CHANGELOG.md`, overriding the docs-SPA fetch which 404'd): v1.9.0 *"Claude Opus 4.8 support"*; v1.11.0 *"Rewrote per-model request patching for GPT, **Claude**, Qwen, Gemini, and DeepSeek."*

---

## 7. Multi-page (Chrome extension) + MCP server — source-verified

**Extension (WXT + React)** for tasks that span tabs:
- A `MultiPageAgent` + `TabsController` + `RemotePageController` orchestrate actions across tabs. Three extra tools are injected: **`open_new_tab` / `switch_to_tab` / `close_tab`**.
- **Stateless service worker + `chrome.storage.local` + a 1 s heartbeat** (a workaround for the side-panel unloading without cleanup). `onBeforeStep` runs `tabsController.syncTabs()` then `waitUntilTabLoaded()` so the agent sees current tab state.
- **Token-auth bridge:** a page can drive the extension only if the page's `localStorage['PageAgentExtUserAuthToken']` matches the extension's stored token (you copy it from the side panel). On match, the content script exposes `window.PAGE_AGENT_EXT.execute(task, config)` / `.stop()` to page JS via `postMessage`.

**MCP server (`@page-agent/mcp`, Beta)** — control the in-page agent from an *external* MCP client (Claude Desktop, Cursor, a coding agent):
- It is a **separate Node binary**, NOT bundled in the extension. It runs a local **HTTP + WebSocket `HubBridge`**; `launcher.html` pokes the extension (`chrome.runtime.sendMessage` to the extension ID) to open a hub tab that connects back over WebSocket.
- **Three MCP tools:** `execute_task(task)` / `get_status()` / `stop_task()`. External `config` (baseURL/apiKey/model/instructions) flows through the bridge and is merged into the hub's config.
- **A user-approval gate:** before executing an incoming hub task, the hub checks `window.confirm()` (or a cached `allowAllHubConnection` opt-in). Single-task-at-a-time throughout.

> Note the **direction** here: this MCP server does *not* augment a coding agent (the usual corpus B1-MCP shape — one server, many clients). It **exposes control of the in-page agent TO** external clients. An inversion worth flagging at audit; it is not a clean B1-MCP instance.

---

## 8. Configuration surface (source-verified)

`AgentConfig extends LLMConfig`:

| Option | Meaning |
|---|---|
| `language` | `'en-US' | 'zh-CN'` — swaps the system prompt's working-language line |
| `maxSteps` | default **40** |
| `stepDelay` | default **0.4 s** between steps |
| `customTools` | add or **delete** (`null`) tools per instance |
| `instructions.system` | injected `<system_instructions>` |
| `instructions.getPageInstructions(url)` | **per-URL instruction injection** — different guidance per route |
| `experimentalLlmsTxt` | fetch the site's `llms.txt` and inject it (cached, ≤1000 chars) |
| `experimentalScriptExecutionTool` | enables the `execute_javascript` tool — **OFF by default** |
| `transformPageContent(content)` | post-process the dehydrated page before it hits the LLM (redaction hook) |
| `customSystemPrompt` | replace the whole system prompt (`@experimental`, "may break agent behavior") |
| `onAskUser` | wire the `ask_user` human-in-loop tool |
| hooks | `onBeforeTask/onAfterTask/onBeforeStep/onAfterStep/onDispose` |
| `enableMask` | show the SimulatorMask + AI cursor |

The `execute_javascript`-off-by-default + the `transformPageContent` redaction hook + `getPageInstructions` per-route control are the three levers that make this **safely embeddable in a real product**.

---

## 9. Security & privacy (source-verified — the fence)

**Core posture is genuinely benign:** *"a **client-side only** tool with a 'Bring Your Own Key' (BYOK) architecture… does **not** collect or transmit any user data on its own… All data transmission occurs **only** between your browser and the LLM provider you configure."* No backend, no telemetry, MIT, open-source-auditable, `execute_javascript` off by default, extension config stored `chrome.storage.local` (no cloud sync, no analytics). `SECURITY.md` runs a proper private-vuln flow and prioritizes real boundary failures.

**But four real fence points for a production / hireui pilot:**
1. **The free demo/testing LLM proxy egresses page HTML to Alibaba Cloud *China*.** It's a convenience the maintainers bought (Function Compute + BaiLian Qwen), explicitly *"for technical evaluation only, must not be used in production,"* *"No Sensitive Data / PII,"* and *"servers located in Mainland China… if you are in a region with strict data localization laws (such as the EU/EEA), please do not use this API."* → **For anything real, use BYOK (your own Claude/OpenAI key or a local model), never the demo proxy.**
2. **HTML dehydration does NOT guarantee PII removal.** The extension docs: *"The HTML cleaning process… does not guarantee removal of sensitive information (e.g. visible text, form values, or personal data)."* → For a recruitment app (candidate PII), the dehydrated DOM sent to your LLM contains whatever is on screen. Use `transformPageContent` to redact, and choose a no-training provider.
3. **The `.env` API-key-inlined-in-IIFE footgun** (developer-guide): *"AK in your local `.env` will be inlined in the iife script. Be very careful when you distribute the script."* → Never ship a built demo bundle with a real key in it; the browser is a hostile place for secrets (real integrations should proxy the key server-side or use short-lived tokens).
4. **`execute_javascript`** (if you enable `experimentalScriptExecutionTool`) runs arbitrary JS in the page and *"may bypass some safe guards and data-masking mechanisms"* — leave it off unless you have a specific, sandboxed reason.

**Anti-AI-slop stance** (a nuanced one, source-verified `CONTRIBUTING.md`): *"Vibe coding is **NOT** allowed for the core lib or the extension!!! Vibe coding is **RECOMMENDED** when maintaining the demo, the website, the UI and tests."* + *"Bot or AI-generated pull requests without meaningful human involvement — We Don't Accept."* — a discipline that echoes this vault's own verify rule (AI where the blast radius is small; human judgment on the load-bearing core).

---

## 10. Maturity — honest read

**Strong:** 8-package decoupled monorepo; a well-engineered, honest ReAct loop; real provider-quirk hardening; 34 releases / semantic versioning / Keep-a-Changelog; steady cadence (v1.8.1 → v1.11.0 across ~10 weeks); a proper security policy; the transferable engineering (dehydration, MacroTool, autoFixer, the two-stream separation, the honesty-over-success prompt).

**Caveats:** unit tests exist **only in `@page-agent/llms`** (other packages "will follow incrementally"; E2E is a `packages/e2e/` **future** plan); **MCP server is Beta**; loop-detection is `@todo`; several tools are `@todo` (`send_keys`, `upload_file`, `extract_structured_data`); the single-page-app constraint (multi-page needs the extension); no cross-origin iframe support; the demo proxy is China-hosted; **no independent benchmark** — the "~90%+ accuracy" figure is promotional (a CoddyKit review), never measured against WebVoyager/etc. the way browser-use (89.1%) and Skyvern (85.85%) are.

---

## 11. Where it sits vs the corpus & the world

**Corpus browser/web cluster (all EXTERNAL developer tools):**
- **browser-use v41** — the **direct upstream** (page-agent's DOM+prompt are derived from it; `@note Adapted from browser-use`). External Python/Playwright→CDP automation for developers/coding-agents. *Complementary specialization, not competition* — browser-use drives from outside, page-agent lives inside.
- **Skyvern v24** — external browser automation (computer-vision + form-filling focus).
- **crawl4ai v29** — a crawler/scraper library.

**Corpus agent-capability §C standalones (the tier this joins):**
- **serve-sim v183** — agent perception+control of a *mobile/native simulator* (external, framebuffer).
- **Agent-Reach v174** — agent web/social *read+search* (content retrieval, not act).
- **camofox v179** — an *anti-detect stealth browser server* (external automation).
- **video-use v198** — edits a *static media artifact*.

page-agent is the **first corpus subject that is an in-page, embedded-by-the-site-owner, for-the-end-user GUI agent** — a genuinely new surface within the corpus.

**World landscape (honest — the space is populated):** the closest structural peer is **CopilotKit** (a broader in-page agentic-frontend framework with the AG-UI protocol, multi-surface, backend-agnostic — you *build* generative UI with it). Enterprise peers: **Microsoft Copilot Studio** Power Pages Agent API, **GitHub Copilot SDK**, **EmbedAI**. So page-agent is **corpus-first for the surface but NOT world-first**; its distinctive niche vs CopilotKit is *"drop one `<script>` in, drive the **existing** DOM, no app changes / no backend rewrite / no protocol to adopt."*

**The "structured-surface-not-raw-dump" perception thread** this vault has been tracking (browser-use v41's DOM-not-screenshot → codebase-memory-mcp v172's graph-not-file-reads → fff v194's resident-index → video-use v198's transcript-not-frames) gets another member: page-agent gives the LLM **an indexed DOM text map, not a screenshot** — the same "give the model a compact structured surface, not the raw bytes" move, applied in-page. (It inherits the technique from browser-use rather than inventing it.)

---

## 12. Five things worth stealing (preview of the Pilot Menu)

1. **The MacroTool pattern** — one forced structured tool call per step carrying *both* reflection and the chosen action. Clean, cheap, auditable.
2. **`autoFixer` / `normalizeResponse`** — repair malformed LLM tool-calls (JSON-in-content, double-stringified args, missing-action→wait) instead of failing the step. Makes weak/local models usable.
3. **The two-stream separation** — persistent History (in context) vs transient Activity (UI only), with transient errors kept *out* of the model's reasoning.
4. **DOM dehydration** — turn a rich structured surface into token-lean indexed text (`[index]<tag>text</tag>` + `*[new]` + `data-scrollable`) and let the model act by integer, never by selector.
5. **The honesty-over-success prompt + BYOK/no-backend/redaction-hook posture** — "it's ok to fail," "never assume success," `execute_javascript` off by default, `transformPageContent` redaction — the discipline that makes an autonomous UI agent safe to embed.

→ See **`(C) page-agent — Pilot Methods Menu.md`** for 24 concrete ways to apply this, and **`(C) page-agent — Verdict.md`** for the corpus placement.
