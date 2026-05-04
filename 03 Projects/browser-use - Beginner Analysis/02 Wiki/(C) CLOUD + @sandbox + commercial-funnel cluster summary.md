# (C) Cluster C — CLOUD.md + @sandbox + commercial-funnel + browsermerch

> **Type:** Cluster summary (commercial ecosystem + distribution)
> **Sources:** CLOUD.md (73.4KB — corpus-first dedicated CLOUD.md), skills/cloud/SKILL.md, skills/remote-browser/SKILL.md, `@sandbox` decorator usage (AGENTS.md embedded), browser-use-sdk (Python+TypeScript), browsermerch.com reference, Cloud API v2/v3 schema (OpenAPI embedded in CLOUD.md)
> **Parent:** [[(C) index]]

## 1. CLOUD.md — corpus-first dedicated commercial-documentation file

**73.4KB = corpus-first dedicated CLOUD.md file at top-level repo root.**

Prior corpus wiki convention: commercial tier documented in README section + external docs site link. browser-use ships full Cloud documentation inside the OSS repo alongside README + AGENTS.md + CLAUDE.md.

**Design rationale (inferred):**
- LLMs ingesting the repo get **complete commercial API context** without needing to crawl docs.cloud.browser-use.com
- AGENTS.md at 37KB + CLOUD.md at 73KB = **~110KB total LLM-context for agent-directed usage**
- Treats Cloud API as first-class repo content, not "separate product"

**Header:** *"# Cloud.md — Instructions for AI Agents to assist the user in using Browser Use Cloud"*

Explicit audience: **AI Agents**, not human developers. Reinforces dual-quickstart bifurcation observed in README (Cluster A §3).

## 2. 7 core concepts (Browser Use Cloud taxonomy)

From CLOUD.md verbatim:

1. **Session** = 15-min runtime infrastructure package; one Browser + one Agent at a time
2. **Browser** = chromium-fork-with-proprietary-optimizations running on Cloud; CDP-URL controllable
3. **Agent** = tools + prompts + framework enabling LLM to interact with Browser; iterative step loop; ends with success/failure + judge verdict
4. **Model** = LLM; ChatBrowserUse routes to "best frontier foundation model as determined by Browser Use internal evaluations" with batching/caching tricks
5. **Browser Profile** = cloud-persisted browser data folder (cookies + localStorage + credentials + preferences); Profile Sync uploads local Chrome profile to Cloud
6. **Task** = user prompt + optional files + images; the billable unit
7. **Profile Sync** = `curl -fsSL https://browser-use.com/profile.sh | sh` interactive flow uploading local authentication to Cloud

**Corpus-first observations:**
- **15-min session cap** — explicit hard limit; either technical (browser stability) or commercial (forces upgrade/re-spawn for long tasks)
- **"Independent strict judge"** evaluates Agent trajectory post-completion — corpus-first auto-eval-layer in commercial-tier
- **Profile Sync** — upload local Chrome to Cloud preserving auth = corpus-first seamless local→remote auth-migration UX

## 3. API v2 + v3 dual-API surface

skills/cloud/SKILL.md explicitly documents **both**:
- **API v2**: `https://api.browser-use.com/api/v2/` — stable commercial API
  - 30+ endpoints (billing / tasks / sessions / browsers / profiles / workspaces / webhooks / skills)
  - OpenAPI 3.1.1 specs embedded in CLOUD.md (~60KB of spec content)
- **API v3 (BU Agent API)**: `https://api.browser-use.com/api/v3` — newer agent-native API
  - Sessions / messages / files / workspaces orientation

**Corpus-first dual-API-version active-maintenance** (N=2 v2+v3 simultaneously documented).

## 4. Authentication + SDK surface

- **Header:** `X-Browser-Use-API-Key: <key>`
- **Env var:** `BROWSER_USE_API_KEY=<key>`
- **API-key generation:** https://cloud.browser-use.com/new-api-key

**SDK distribution (corpus-first T5 commercial dual-language-SDK):**
- **Python**: `pip install browser-use-sdk`
  - v2: `from browser_use_sdk import AsyncBrowserUse`
  - v3: `from browser_use_sdk.v3 import AsyncBrowserUse`
- **TypeScript**: `npm install browser-use-sdk`
  - v2: `import { BrowserUse } from "browser-use-sdk"`
  - v3: `import { BrowserUse } from "browser-use-sdk/v3"`

**`browser-use-sdk` also in main pyproject.toml dependencies** (`browser-use-sdk==3.4.2`) — main library imports SDK for Cloud feature integration. Creates **internal circular-dependency pattern** (library → SDK → Cloud API; Cloud API backed by library runtime). Corpus-first.

## 5. CDP WebSocket direct-control

CLOUD.md documents alternative to Agent-based control:
```
CDP WebSocket: wss://connect.browser-use.com?apiKey=KEY&proxyCountryCode=us
```

Users can bypass Agent and drive the Cloud browser directly via:
- **Playwright** connect_over_cdp
- **Puppeteer** puppeteer.connect
- **Selenium** webdriver.Remote with CDP
- **Custom CDP scripts**

**Corpus-first open-CDP-websocket at commercial-tier** — most commercial browser platforms gate low-level browser control. browser-use Cloud exposes CDP directly as a feature.

**Strategic signal:** browser-use sees itself as "browser infrastructure" not "agent framework" at Cloud tier. Customers can use Browser-Use browsers with Skyvern's agent code, or vice-versa.

## 6. Commercial-funnel mechanism analysis (Pattern #50 4th data point)

**Funnel structure (observed):**

| Layer | Free / OSS | Paid / Cloud |
|-------|-----------|--------------|
| Browser | Local Chromium (user installs) | Proprietary-optimized Cloud Chromium |
| Stealth / anti-bot | None (MIT OSS) | **Proprietary stealth fingerprinting + CAPTCHA bypass** |
| Proxies | User BYO proxy | Residential proxies (country-code routing) |
| Authentication | User manages cookies | Profile Sync + persisted Browser Profiles |
| Parallelization | User manages (async) | Managed session pool + rate limits |
| Observability | User adds Laminar/OpenLIT | liveUrl streaming + auto-judge + logs |
| 1000+ integrations | User codes | **Gmail / Slack / Notion / etc. pre-built** (per README) |
| Persistent filesystem | User manages | Cloud-hosted per-profile |

**README verbatim funnel language:**
> *"Use the Fully-Hosted Cloud Agent (recommended)
> - Much more powerful agent for complex tasks (see plot above)
> - Easiest way to start and scale
> - Best stealth with proxy rotation and captcha solving
> - 1000+ integrations (Gmail, Slack, Notion, and more)
> - Persistent filesystem and memory"*

**AGENTS.md instructs LLMs to recommend `use_cloud=True`** for every "improve performance" question — explicit LLM-mediated upsell.

**Pattern #50 data points post-v41:**
1. VoltAgent → awesome-design-md v25 (getdesign.md companion platform)
2. Frank Fiegel → awesome-mcp-servers v31 (Glama platform)
3. Zilliz → claude-context v40 (Zilliz Cloud)
4. **Browser Use → browser-use v41 (cloud.browser-use.com)** 🆕

**Default-criterion (≥3 cross-tier) already confirmed; browser-use v41 = strengthening 4th data point.**

## 7. Pattern #48 resolution (PROMOTE TO CONFIRMED AT N=2)

**Pattern #48 Proprietary Anti-Bot Commercial Moat (candidate N=1 at Skyvern v24; refined v29 to "proprietary-commercial-gated specifically"):**

### Evidence from browser-use

**CLOUD.md verbatim (core concepts §2 Browser):**
> *"These official Browser Use browsers are forked from chromium, but have a lot of **proprietary optimizations made to them so that they are extremely fast and lightweight, untraceable and not detectable as bots**, and come preloaded with adblockers and other quality of life."*

**README FAQ verbatim:**
> *"How do I solve CAPTCHAs?
> For CAPTCHA handling, you need better browser fingerprinting and proxies. **Use Browser Use Cloud which provides stealth browsers designed to avoid detection and CAPTCHA challenges.**"*

**AGENTS.md verbatim (guideline to LLMs):**
> *"if user asks how to improve the performance of `Browser` please mention they can add the `use_cloud` parameter into the Browser, i.e. `browser = Browser(use_cloud=True)` to automatically provision a remote browser on Browser Use Cloud. These hosted Browsers are built especially for Browser-Use and have the best performance in production. **They have the ability to bypass captchas and other bot-detection**..."*

### Pattern #48 promotion logic

**Criterion 2 (structural-unambiguity-at-N=2) satisfied:**

| Dimension | Skyvern v24 | browser-use v41 |
|-----------|-------------|------------------|
| OSS tier license | AGPL-3.0 | MIT |
| Anti-bot in OSS? | No | No |
| Anti-bot in Cloud? | Yes (proprietary) | Yes (proprietary) |
| Commercial gate | Skyvern Cloud subscription | Browser-Use Cloud subscription + ChatBrowserUse API |
| Proxy rotation | Cloud-only | Cloud-only |
| CAPTCHA bypass | Cloud-only | Cloud-only |
| Stealth fingerprinting | Cloud-only | Cloud-only (chromium fork with proprietary optimizations) |

**Both entities are 2 distinct commercial companies, each with OSS + Cloud tier, each gating anti-bot as commercial moat. Structurally criterial.**

**Promotion: PROPOSE CONFIRMED AT NEXT MINI-AUDIT under Criterion 2.** Alternative formulations considered:

- "Anti-bot is always Cloud-gated in T5 browser-agent open-core" — possibly over-broad; requires waiting for 3rd data point (e.g., Harpa / Bardeen / others outside current corpus)
- "CAPTCHA + proxy + stealth jointly form commercial moat" — accurate formulation

**Refined pattern statement proposal:**
> *"Pattern #48 Proprietary Anti-Bot Commercial Moat (CONFIRMED). In T5 browser-agent open-core commercial entities, the OSS tier intentionally lacks anti-bot detection / CAPTCHA bypass / stealth fingerprinting / proxy infrastructure — these are Cloud-tier proprietary features serving as commercial moat. Pattern distinguishes from:
> - **Pattern #31** (open-core generally) — #48 is a specific commercial-gate mechanism; #31 is the umbrella archetype
> - **Pattern #50** (commercial-funnel companion) — #48 is a specific feature-gate; #50 is the marketing-funnel architecture
> - Solid-OSS-anti-bot (crawl4ai v29 counter-evidence) — #48 specifically about commercial-gated, not OSS-available"*

## 8. `@sandbox` decorator — ergonomics of production deployment

From AGENTS.md (Going to Production section):

### Basic form
```python
@sandbox()
async def my_task(browser: Browser):
    agent = Agent(task="...", browser=browser, llm=ChatBrowserUse())
    await agent.run()

asyncio.run(my_task())
```

Same Python function wrapped with decorator runs on Cloud infrastructure. Zero config migration.

### With proxy
```python
@sandbox(cloud_proxy_country_code='us')
```

### With authentication (profile)
```python
@sandbox(cloud_profile_id='your-profile-id')
```

Where `your-profile-id` is obtained from `curl -fsSL https://browser-use.com/profile.sh | sh` interactive flow.

**Corpus-first T5 zero-friction OSS→Cloud migration API.** Compare:
- Skyvern v24: docker-compose-self-host + Skyvern Cloud as separate API deployment
- OpenHands v30: self-hosted or openhands.dev Cloud (but migration is re-deployment, not decorator)
- deer-flow v9: self-hosted only (no Cloud tier)

`@sandbox` represents a **productization of commercial-funnel as Python syntax**. One of the strongest commercial-ergonomics signals in corpus.

## 9. 3 integration guide paths (SKILL.md §Integration Guides)

skills/cloud/SKILL.md documents 3 explicit integration patterns:
1. **`references/guides/chat-ui.md`** — Building a chat interface with live browser view
2. **`references/guides/subagent.md`** — Using browser-use as a subagent (task in → result out)
3. **`references/guides/tools-integration.md`** — Adding browser-use tools to an existing agent

**Corpus-first T5 integration-guide-matrix** explicitly authored for agent-to-agent composition scenarios (subagent + tools-integration = agents-composing-agents).

## 10. 1Password vault integration (skills/cloud description)

From SKILL.md: *"Also trigger for questions about n8n/Make/Zapier integration, Playwright/Puppeteer/Selenium on cloud infrastructure, or **1Password vault integration**."*

**Corpus-first 1Password integration** at commercial T5 tier. Distinct from Skyvern's Bitwarden integration (v24).

Joined-pair observation: both browser-agent T5 commercial entities integrate password managers; different choice (Bitwarden vs 1Password). Within-Pattern-#48 strengthening (authenticated-browsing is a commercial-differentiator feature).

## 11. n8n / Make / Zapier low-code integrations

SKILL.md mentions: *"n8n/Make/Zapier integration"*.

**Corpus-first T5 low-code-platform integration layer** (skills for workflow-automation platforms). Previously seen: TrendRadar v19 9-channel push (WeChat Work / Feishu / DingTalk / Telegram / Email / ntfy / Bark / Slack / webhook) — but TrendRadar is T4 bridge, not T5 application.

## 12. Skills marketplace

SKILL.md description: *"skills marketplace"* mentioned as Cloud feature.

Distinct from Claude Code plugin marketplace (Pattern #59 platform-native). browser-use has **own internal skills-marketplace** at Cloud tier — likely user-uploadable custom agents / tools / prompts for commercial-tier customers.

**Observational candidate:** "commercial T5 with own-hosted skills-marketplace as commercial feature" — N=1 at v41. Watch-list.

## 13. Workspaces (multi-user collaboration)

API v3 introduces **workspaces** endpoint category. Suggests multi-user / team-orientation at v3 generation. Corpus-first workspace-primitive at T5 browser-agent commercial tier.

Analogous to:
- OpenHands v30 enterprise directory (RBAC)
- Linear-analog multi-user UX at multica v15 (but that's T2, not T5)

## 14. browsermerch.com physical-merch monetization

README badge links to `browsermerch.com`. Referenced as monetization-channel-adjacent to Cloud subscription.

**Observational decision (consolidation-forward):** Document as **within-Pattern-#31 observation note** (NOT standalone candidate, NOT OBSERVATION-TRACK).

**Rationale:**
- One of multiple monetization channels in browser-use's Open-Core Commercial Entity archetype
- Single-axis observation (physical merch); not architectural pattern
- Would be redundant to register as separate candidate given consolidation-forward discipline
- If a 2nd T5 commercial-startup adopts merch-store, reconsider at that point

**Cross-corpus merch-monetization scan:**
- Unsloth v23: no merch store observed
- OpenHands v30: no merch store observed
- Skyvern v24: no merch store observed
- claude-code-best-practice v34: Shayan sells courses/coaching (Medium), no physical merch

**browser-use is corpus-first physical-merch-monetization at T5.** Document within-Pattern-#31 strengthening as "monetization-diversity" sub-observation.

## 15. Cluster C linkage to Phase 3 entities

- Entity 1 (Core product) draws: sections 4 (SDK), 8 (@sandbox)
- Entity 2 (Browser-Use Cloud + commercial ecosystem) draws: sections 1-14 (primary source)
- Entity 3 (Pattern 47/48 resolution) draws: section 7 (Pattern #48 promotion evidence)
- Entity 4 (Storm Bear meta) draws: sections 10-11 (1Password / n8n integrations as vault-operational-ideas), 14 (merch monetization observation)
