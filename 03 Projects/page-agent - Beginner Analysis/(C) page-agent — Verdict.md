# (C) page-agent — Verdict (LLM Wiki v199)

**Subject:** `alibaba/page-agent` — an in-page, client-side-JavaScript GUI agent a web-app owner embeds so their end users can drive the app by natural language. MIT; v1.11.0; source-verified at `35ff6d4`; author Simon (`gaomeng1900`) + Alibaba Group Holding.

**Ship date:** 2026-07-08 · **Branch:** `wiki/v199-page-agent` off the v198 tip.

---

## Verdict: GOAL-ALIGNED INCLUDE 3/4

| Criterion | Call | Why |
|---|---|---|
| **(a) Anthropic-adjacency / cultural-peer** | **FAIL** | `alibaba/page-agent`, author Simon (`gaomeng1900` / SimonLuvRamen) + Alibaba Group Holding — **not Anthropic**. First `alibaba/` **org** subject (Qwen/dashscope has appeared only as a *backend* in prior wikis, never as a repo subject) → a **#19 19a** institutional data-point, not a new (a) axis. No heritage rescue. |
| **(b) Goal-relevance** | **STRONG** (keys the tier) | It **is** an autonomous GUI agent (Goal #1's "autonomous agents" core), it **ships an MCP server**, its LLM client treats **Claude as first-class** (Opus 4.8 support + per-model patching), and it is **directly + sharply pilotable into hireui** — a recruitment SaaS web app, exactly page-agent's stated use case ("ship an AI copilot in your product in lines of code, no backend rewrite"). Arguably the **sharpest Goal-#2 *product*-pilot in the corpus since serve-sim v183**. STRONG-not-STRONGEST = third-party + LLM-agnostic (Qwen-default, Claude one of many) + the domain is end-user web-app enhancement, not software-dev tooling. ⚠️ **MODERATE-on-domain reading recorded operator-reviewable** (the OpenMontage v188 / meetily v196 precedent: it's an end-user product agent, not coding-agent / agent-dev infra). Either reading → GOAL-ALIGNED per §31 (keys on (b) MODERATE+, not (a)). |
| **(c) Substance / engineering** | **STRONG** | 8-package decoupled monorepo (headless core / LLM client / DOM controller / UI / MCP / extension); a well-engineered honest ReAct loop (MacroTool single-call-per-step, persistent-vs-transient streams, observations, user-takeover, lifecycle hooks, per-URL instructions + `llms.txt` fetch, `execute_javascript` off-by-default); real DOM dehydration engine + SimulatorMask; provider-quirk-hardened OpenAI-compatible client + `autoFixer`; BYO-LLM incl. local; Chrome extension multi-tab + MCP server (Beta); 34 releases / v1.11.0. **Caveats:** tests only in `@page-agent/llms`; MCP Beta; loop-detection + several tools `@todo`; single-page-app core; no cross-origin iframes; no independent benchmark (the "~90%" figure is promotional). |
| **(d) Cross-references** | **STRONG** | Direct upstream **browser-use v41** (DOM+prompt derived — the genuine #57); external-automation cluster Skyvern v24 / crawl4ai v29; agent-capability §C standalones serve-sim v183 / Agent-Reach v174 / camofox v179 / video-use v198; the "structured-surface-not-raw-dump" perception thread (browser-use v41 / codebase-memory-mcp v172 / fff v194 / video-use v198); threads: multi-agent-orchestration, claude-api-cost-optimization (text-DOM = no vision cost), #18 B1-MCP, #84 84c LLM-agnostic, #12 CLAUDE.md+AGENTS.md; hireui (Goal #2). |

---

## Pattern outcome: 1 NEW §C standalone at N=1 (CORPUS-FIRST for the surface, NOT world-first)

**"In-Page / Embedded End-User GUI Agent"** — *a client-side JavaScript library a **web-app owner** drops into their **own** site (one `<script>` / `npm install`, no extension / no headless browser / no Python / no backend) to give that site's **END USERS** a natural-language agent that reads and drives the app's **own real DOM** via text dehydration (no screenshots), BYOK.*

**The defining conjunction:**
- **In-page / client-side JS** — the agent *lives in* the target page, it does not drive it from outside.
- **Embedded BY the site owner FOR that site's end users** — not a developer/coding-agent automating an arbitrary browser.
- **Drives the app's OWN real DOM** via text dehydration (`[index]<tag>text</tag>`), no screenshots/multimodal.
- **Zero external infrastructure / BYOK** — no headless browser, no Python, no backend.

**DISTINCT from** every prior corpus browser/web subject, which are **external developer tools**:
- browser-use v41 / Skyvern v24 — external Playwright/CDP automation for developers/agents ("server-side automation"); page-agent is explicitly *"client-side web enhancement, not server-side automation"* — **and derives from browser-use** (the upstream, not the same surface).
- crawl4ai v29 — a crawler library.
- serve-sim v183 §C — agent perception+control of a *mobile/native simulator* (external framebuffer).
- Agent-Reach v174 §C — web/social *read+search* (retrieve content, not act on the app's UI).
- camofox v179 §C — an *anti-detect stealth browser server* (external automation).
- video-use v198 §C — operates on a *static media artifact*.

**Scope honestly bounded — CORPUS-FIRST for the surface, NOT world-first.** The in-page embedded-copilot space is **commercially populated**: the closest structural peer is **CopilotKit** (a broader in-page agentic-frontend framework + AG-UI protocol, multi-surface, backend-agnostic), plus **Microsoft Copilot Studio** Power Pages Agent API, **GitHub Copilot SDK**, **EmbedAI**. page-agent's niche vs CopilotKit: *drop one `<script>` in, drive the **existing** DOM, no app changes / no protocol to adopt.* Its "text-DOM-not-screenshots" is **NOT** a novel advantage (browser-use / Stagehand / Playwright-MCP have all converged on it); its **own** distinctive is the in-page pure-JS delivery.

**⚠️ NO-MINT alternative recorded operator/audit-reviewable** (the camofox v179 / ai-berkshire v187 / video-use v198 discipline): *"page-agent is a browser-agent variant within the represented external-browser-automation family (browser-use v41 / Skyvern v24); the in-page delivery is a packaging/deployment choice, not a new capability → file as instance-strengthening, no fresh standalone."* **Leaned MINT** because the WHO (site owner) + FOR-WHOM (that site's end users) + WHERE (in-page, no external driver) is a genuinely different task boundary + deployment model from external developer automation — the same edit-vs-produce boundary logic that carried video-use v198 and the web-vs-mobile boundary that carried serve-sim v183. §28 ≤2-new-standalones cap honored (1 mint). Either reading → **counts UNCHANGED 46/11**.

Mint at N=1 per the serve-sim v183 / fff v194 / openwiki v195 / video-use v198 precedent (strong real anchor — official Alibaba org, 25k★ page-stated, production TS monorepo, 34 releases, no *corpus* peer on the surface). **PROMOTION-ELIGIBLE at N=2** (a genuine 2nd in-page embedded end-user GUI-agent library analyzed as a primary subject — CopilotKit itself would qualify if it becomes a subject); time-aware stale-watch ≥15 wikis AND ≥30 days (§39).

---

## SECONDARY (recorded, NOT minted)

- **#57 corpus-recursive influence-citation — GENUINE.** page-agent v199 explicitly **derives its DOM-processing components + system prompt FROM browser-use v41** (a corpus subject), with an open NOTICE-style credit (© Gregor Zunic) + source-verified `@note Adapted from browser-use` headers. This is a real recursion (a corpus subject citing/deriving-from *another* corpus subject as influence) — **stronger** than the recent "mentions ≠ recursion" client-only cases (v172/v173/v174) and cleaner than v181 cortex-hub's *silent* GitNexus-v33 bundling. **⚠️ Distinguish from v198:** video-use v198's browser-use tie was a *self-reference* (same org) explicitly logged NOT-#57; **v199 is a different author (Alibaba/Simon) deriving from browser-use = a genuine #57.** So browser-use v41 collects, within two ships, a self-reference (v198) and a genuine forward-citation (v199). Whether this is a #57 promotion data-point = **audit bookkeeping** (N of #57 not self-incremented here).
- **#19 19a — first `alibaba/` org subject.** Institutional data-point (Qwen/dashscope was a prior backend, never a repo subject). Not a new (a) axis.
- **#18 B1-MCP — ADJACENCY, direction-inverted, NO N-bump.** Ships `@page-agent/mcp` (Beta) but it **exposes control of the in-page agent TO external clients**, the *opposite* direction of the canonical B1-MCP (one server augmenting many coding agents). Recorded as an adjacency data-point + an audit flag; **not** a clean B1-MCP instance.
- **#84 84c LLM-agnostic** — BYO-LLM incl. local (Ollama/dashscope/OpenRouter/OpenAI-compatible; Claude among supported + tested). NOT the ponytail v168 14-platform native-rule-file mechanism → **NO N-bump** (per v86).
- **#12 LLM-routing-artifacts** — ships `CLAUDE.md` (`@AGENTS.md` alias) + `AGENTS.md` + per-package `AGENTS.md`. Incidental → **NO N-bump**.
- **LV #20 Token-Economy-Quantification — QUALIFIED-ADJACENT.** DOM-as-text = "no multi-modal LLMs" is a real token/cost argument (cheaper than screenshot computer-use) + the client tracks `cachedTokens`/`reasoningTokens`; but **no quantified benchmark** → **N stays 4**, bump DEFERRED (per v168/v172/v194).
- **#66 supply-chain — BENIGN install / MODERATE data-privacy.** Install clean (npm/CDN, MIT, client-side, BYOK, no backend, no telemetry, `execute_javascript` off-by-default, open-source-auditable, proper `SECURITY.md`). The fence: the **free demo proxy egresses page HTML to Alibaba Cloud *China*** (tech-eval only, no-PII, EU-do-not-use → use BYOK for anything real); **HTML dehydration does NOT guarantee PII removal** (recruiter/candidate data = a real fence → use `transformPageContent` redaction + a no-training provider); the **`.env`-AK-inlined-in-IIFE footgun**; `execute_javascript` runs arbitrary in-page JS if enabled.
- **Anti-AI-slop contribution stance** — *"Vibe coding NOT allowed for the core lib or the extension; RECOMMENDED for demo/website/UI/tests"* + no unmotivated bot PRs. Echoes the vault's own verify discipline. Recorded, not minted.

## NON-claims

- **NOT #52** — 25k★ / Trendshift / HN are page-stated (§37.4) → velocity unestablishable.
- **NOT corpus-first browser-agent** — browser-use v41 / Skyvern v24 precede; the claim is scoped to the **in-page embedded end-user** surface.
- **NOT world-first** — CopilotKit / EmbedAI / Copilot Studio / GitHub Copilot SDK precede/compete.
- **NOT #18 B1-MCP** in the strict sense (Beta + inverted direction — adjacency only).
- **NOT a new top-level pattern** (max #85).
- **NOT novel for text-DOM-not-screenshots** — industry-converged; inherited from browser-use.

---

## Tier & counts

**Tier: T2 Service** (embeddable client-side capability layer / SDK for the browser — the browser-capability family with browser-use v41 / crawl4ai v29 / camofox v179 / Agent-Reach v174; minor library-vs-service classification nuance flagged for audit).

- Counts **UNCHANGED 46/11**.
- §C live standalones **38 → 39**; tracked PROVISIONAL surface **≈45 → ≈46**.
- Streak **GA:59 → GA:60**; **46 consecutive goal-aligned ships v153→v199.**
- **§35 CLEAR** — rolling-3 window {v197 GA, v198 GA, **v199 GA**} = 0 OG.
- Lifetime operator overrides = 10; v153→v199 = **zero** overrides.

## Verification note (`feedback_wiki_verify_independently_check_collisions`)

Verdict produced **INLINE + hand-verified**. A read-only 8-agent workflow (`wf_cf35685e-abb`, ~1.43M subagent-tokens, 117 tool-uses, **8/8 done / 0 errors / 1 empty**) did **source-reading + upstream research ONLY**. ALL corpus/collision/identity/mint claims verified **BY HAND**:
- **Collision grep clean** — no prior `page-agent` / in-page / embedded-GUI-agent / Simon / `gaomeng1900` subject anywhere (`_state/` + `_patterns/` + `03 Projects/`).
- **browser-use = v41** (authoritative — the serve-sim v183 entry explicitly corrects the earlier v34 miscache); Skyvern v24, crawl4ai v29 confirmed.
- **No prior `alibaba/` org subject** (Qwen/dashscope was a backend only).
- **No existing in-page/embedded end-user GUI-agent §C standalone** (registry read).
- **I hand-read** README, CLAUDE.md, AGENTS.md, `system_prompt.md`, `tools/index.ts`, `PageAgentCore.ts`, `llms/types.ts`, `terms-and-privacy.md`, `CHANGELOG.md`, developer-guide — and the workflow's DOM-engine / LLM-client / extension-MCP / config claims cross-matched my hand-reads (real line numbers → real tool calls).
- **Confabulations caught + corrected:** (1) the 1 **empty** agent = the identity researcher (StructuredOutput not returned) → identity covered by hand from the repo (Simon / gaomeng1900 / Alibaba org; no over-claim about Simon's other work). (2) the docs-models agent reported *"Claude NOT mentioned"* — this is a **SPA-404 fetch artifact** (the docs site is a dynamic SPA that returned 404 for `/docs/features/models`), **NOT ground truth**: the hand-read `CHANGELOG.md` explicitly ships "Claude Opus 4.8 support" + per-model Claude patching, so Claude support is CONFIRMED and the negative finding was overridden.

`inflation_check` = discipline HELD (1 mint ≤2 cap; N=1 scoped corpus-first-not-world-first with CopilotKit credited; NO-MINT alt recorded; counts 46/11 unchanged; no N-bumps on #18/#84/#12/#20; #57 recorded not self-incremented).
