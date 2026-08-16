# (C) CoreOfPotato — Verdict + Pattern Outcome

> **v231** · `hwahao/CoreOfPotato` · 2026-08-16 · operator-requested
> Verdict produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — no workflow, no subagent (the ~205K shim overflows every subagent >200K → prompt-too-long; the v200→v230 self-throttle).

---

## Tier: **GOAL-ALIGNED INCLUDE 3/4**

### (a) Anthropic-affiliated — **FAIL**
`hwahao` is a disclosed individual (bio + Hanoi, Viet Nam), not Anthropic, no company, no notability signal. **§41**: (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source — no name, heritage, locale or notability inference.

⚠️ Explicitly recorded and **not** relied upon: the subject is Vietnamese-authored and reached the operator through a Vietnamese Facebook channel, and the operator is VN-located. Under the superseded v78-ECC product-locale precedent that once looked like an (a) angle; under the v159→v230 discipline it is **not** an (a)-rescue. Clean FAIL. → **#19 19a**, first `hwahao` author.

### (b) Goal-relevance — **MODERATE** (keys the tier)
**For:** it is LLM-access-gateway infrastructure, the corpus's densest tooling thread (cc-switch v73 · freellmapi v112 · CodexPlusPlus v117 · ai-switcher v153 · opencode-antigravity-auth v67 · CLIProxyAPI v207 · OmniRoute v208). It sits on the live **claude-api-cost-optimization** thread as the free-tier-harvesting pole. Its shipped `caller_map` registers exactly two clients — **OpenClaw** and **OpenCode** — so the intended consumers are *coding agents*, which is Goal #1's neighbourhood. And it is a **genuine corpus-recursive build on CloakBrowser v69**.

**Held below STRONG by four things:** **Claude appears nowhere** (drivers are `chatgpt.py` / `gemini.py` / `grok.py`; no `claude.py`) — neither as a target model nor a named client; the artifact is **tiny and stale** (~16★, 7 commits, no activity since 2026-06-09); the hard parts are **all upstream** (stealth = CloakBrowser v69, automation = Playwright, the models = the vendors'); and **there is nothing safely pilotable** — the flagship use is ToS-violating and account-ban-risking.

Calibration: clearly below v207 CLIProxyAPI / v208 OmniRoute **(b) STRONG** (flagship scale, Claude among the wrapped providers, a load-bearing dependency of corpus subject v181); sitting at or just above **v180's (b) MODERATE** (a real system in a goal-relevant class, but tiny, personal, and pointed at non-Claude models). **MODERATE+ → GOAL-ALIGNED per §31.** Gray-zone ≠ off-goal (the opencode-antigravity-auth v67 / camofox v179 / Strix v190 / CLIProxyAPI v207 precedent). §40 not needed.

⚠️ **Both neighbours recorded reviewable.** **STRONG** is arguable on the coding-agent-client + corpus-recursive-dependency + live-cost-thread grounds. **OFF-GOAL CAPTURE** is arguable on Claude-absence + nothing-pilotable + ToS-violation. Recorded **MODERATE primary on the merits**; under the OFF-GOAL reading the streak becomes `GA:88 · OG:14` and §35 stays CLEAR (1 OG ≤ 1).

### (c) Substance — **MODERATE**
**Real:** a working aiohttp gateway with a source-verified `/v1/chat/completions` + genuine SSE streaming; a `BaseDriver` registry with three drivers; per-platform worker pools; a composite `nav_key` session-multiplexing scheme with three URL-cache strategies; a `/hub` dashboard; `/api/*` admin surface with log export/retention; a load-test harness; real CI (`ci.yml` — Python 3.9, ruff, playwright, pytest); DISCLAIMER, CONTRIBUTING, EASY_START, Keep-a-Changelog.

**Caveats, foregrounded:** **7 commits in 4 days, 4 of them `fix(ci)`**; ~16★/3 forks; v1.0.1; stale since June; **2 public repos by a self-described non-coder** → almost certainly AI-generated, with a verified tell (**the CHANGELOG's v1.0.0 entry says "Open-source release of CoreNexus"**, re-fetched with a targeted yes/no-and-quote to exclude a summarizer artifact); a thin orchestration layer over third-party engines; completion detection is a **text-stability heuristic** (`stable_count >= 8`, ~2 s), brittle by construction; CI is single-Python-version; **⚠️ NOT source-cloned**.

### (d) Connectivity — **STRONG**
LLM-access-tooling family (v73/v112/v117/v153/v67/v207/v208) · the stealth-browser §C standalone (**v69 as a dependency**, v179 camofox) · browser automation (browser-use v41 / Skyvern v24 / crawl4ai v29 / page-agent v199) · **Pattern #18 #8** Multi-Source LLM Aggregator · **LV-C2** cost economics · **#66** dual-use/ToS · the api-security/BOLA pilot thread · the vendor-seam thread (meetily v196 / AIRI v210 / lobehub v222).

---

## Pattern outcome: **NO MINT**

**Counts UNCHANGED 46/11. §C live standalones 47 unchanged. §C surface unchanged. No new top-level pattern (max #85).**

### The candidate class, and why it is declined
The tempting mint is an N=1 §C standalone:

> *"Self-Hosted Gateway that Browser-Automates Free Consumer Web-Chat UIs Behind an Anti-Detect Browser and Re-Exposes Them as an OpenAI-Compatible API (with per-conversation session multiplexing)."*

It is genuinely **corpus-first for that surface** — collision grep is clean, and no existing §C row covers *scraping a consumer chat UI into an API*. **DECLINED** on three grounds:

1. **Not world-first, and not close.** `gpt4free` / `g4f` is the world-canonical flagship of exactly this class — reverse-engineered free-provider aggregation *including* browser automation — and precedes CoreOfPotato by years, with `gpt4free` and `free-ai` GitHub topics behind it. (`gpt4free` already appears in the corpus, but only as one of 13 providers in another subject's config — a landscape mention, never a subject.)
2. **The anchor is weak and early.** ~16★, 3 forks, **7 commits over 4 days**, stale two months, 2 public repos by a self-described non-coder, a thin orchestration layer wrapping CloakBrowser v69 + Playwright + the vendors' own UIs. The **cortex-hub v181 precedent is directly on point** (a would-be corpus-first class declined because the anchor was a weak, early, thin wrapper over third-party engines), reinforced by **a.i-assistant-chatbot-telegram v180** (weak-substance anchor + packaging-not-capability). The Kilo-Code v177 "mint the exemplar at N=1" precedent applies to a class's *major* exemplar — this is a minor instance of a class whose exemplar is elsewhere.
3. **§28 anti-inflation.** Minting a corpus-first row on a 16★ 7-commit repo for a genre this populated is exactly the phantom-count inflation the routine exists to prevent.

**Recorded instead:** a corpus-knowledge data-point + a **DEFERRED watch axis** — *"gateway that browser-automates consumer web-chat UIs behind an anti-detect browser and re-exposes them as an OpenAI-compatible API (free-tier harvesting, as distinct from OAuth-subscription re-exposure)."* If the class earns a mint later it should be minted on a clean exemplar (gpt4free being the obvious candidate), with CoreOfPotato credited as the prior data-point. The N=1 mint is recorded as the **operator/audit-reviewable alternative**.

### Two boundaries that had to be held (both easy to over-claim)

**⚠️ NOT a clean N=3 of the v207 §C standalone.** That row is titled and scoped *"Self-Hosted Multi-Provider API Gateway that Re-Exposes **CLI-Tool OAuth Subscriptions** as OpenAI/Gemini/Claude/Codex-Compatible Endpoints"* (N=2: CLIProxyAPI v207 + OmniRoute v208, promotion **deferred pending a fully-independent non-port 3rd instance**). CoreOfPotato re-exposes **free consumer web-UI sessions driven through a stealth browser** — a *different source mechanism*, not a different implementation of the same one. **The v207 promotion trigger is therefore NOT satisfied**, and it would have been easy and wrong to say it was (the geti-v213-is-not-a-clean-v192-N=3 discipline).
→ *Reviewable alternative for the audit:* generalize the row to *"re-exposes a non-API consumer entitlement as an OpenAI-compatible endpoint"*, under which CoreOfPotato **would** be an independent, non-port 3rd instance on a new sub-mechanism and **would** fire the promotion. Recorded, **not** self-executed — a headline-count-changing promotion is an audit act.

**⚠️ NOT an instance of the stealth-browser §C standalone** (v69 CloakBrowser + v179 camofox, N=2). CoreOfPotato **consumes** that class; it is not a member of it. No N-bump.

---

## SECONDARY (recorded, NOT minted)

- **Pattern #57 — GENUINE corpus-recursive dependency.** Depends on and **openly credits CloakBrowser = corpus subject v69** (`requirements.txt: cloakbrowser>=0.3.31`; `setup_cloak.py` pip-installs it and calls `ensure_binary()`; the v1.0.0 CHANGELOG credits *"Complete integration with CloakBrowser"*). Identity verified independently via PyPI/landscape research → **CloakHQ**, matching v69's recorded engine and Python-SDK/Playwright-drop-in delivery. Stronger than cortex-hub v181's *silent* GitNexus v33 bundling; the page-agent v199 / OmniRoute v208 credited-dependency shape. N-tally = audit bookkeeping.
- **Pattern #18 sub-mechanism #8 (Multi-Source LLM Aggregator)** — instance-strengthening; recorded, not self-incremented.
- **LV-C2 cost economics** — the corpus's LLM-access economics now spans config-switching (v73), free-tier stacking (v112), reseller relay (v117), multi-account rotation (v153), OAuth bridging (v67), subscription re-exposure (v207/v208) and now **web-UI harvesting (v231)**. The DEFERRED subscription-arbitrage watch axis gains a web-UI-harvesting sub-variant.
- **"AI-Generated-Repo Artifact Contamination"** — the observational candidate registered at **v69** and never carried into the pattern registry (a v2.4 phantom-count casualty, like the stealth-browser axis itself). CoreOfPotato is a textbook instance (`CoreNexus` in the changelog; "no coding skills" bio; 7 commits in 4 days; 4/7 `fix(ci)`). ⚠️ Pleasing recursion: the candidate was born at v69, which is also this subject's dependency. Cross-reference only — the audit may resurrect it.
- **#66 supply-chain / ToS / dual-use** — the sharpest section: a black-box precompiled Chromium from an anonymous vendor; **ships `require_auth: false` + `cors_origins: ["*"]` + a placeholder admin token, with `require_admin` allowing access when no token is configured** (source-verified) while holding live authenticated sessions to your personal AI accounts; browser profiles (session cookies) persisted to `./data/browser_profiles`; and an evade-the-bot-protection premise the project's own DISCLAIMER concedes carries **account-ban risk**.
- **#19 19a** — first `hwahao` author; also the corpus's **first subject authored by a self-described non-coder** (an author-profile data-point, not a mint).

## NON-claims
NOT **#52** (~16★/3 forks page-stated §37.4; stale) · NOT **world-first** (gpt4free/g4f + a populated genre precede) · NOT corpus-first *as a mintable class* (declined) · NOT **#18 B1-MCP** (ships no MCP server) · NOT a clean **N=3 of the v207 row** · NOT an instance of the **v69/v179 stealth-browser row** (a consumer) · NOT **#12/#22** (no `AGENTS.md` / `CLAUDE.md` at root) · NOT Claude-supporting · NOT a new top-level pattern (max #85) · NOT source-cloned (flagged).

## Tier
**T2 Service** — self-hosted local gateway; the CLIProxyAPI v207 / OmniRoute v208 / freellmapi v112 family.

## Streak
v230 **GA:88** → **`GA:89 · OG:13 [7 ov]`** — **12 consecutive goal-aligned ships** since the v219 OFF-GOAL break.
**§35 CLEAR**: window {v229 GA, v230 GA, **v231 GA**} = 0 OG. *(Under the reviewable OFF-GOAL reading: `GA:88 · OG:14`, window = 1 OG ≤ 1 → still CLEAR.)*

## Verification log
Source hand-fetched (repo page · raw README · CHANGELOG ×2 · DISCLAIMER · EASY_START · requirements.txt · setup_cloak.py · config.example.json · core tree · core/drivers tree · core/server.py · core/routes.py · core/drivers/grok.py · .github/workflows/ci.yml · commit list · author profile). Identity + landscape + the CloakBrowser↔CloakHQ link by independent WebSearch. **Collision by sanity-anchored hand-grep: 0 hits for `CoreOfPotato`/`hwahao`/`NaModu` in BOTH authoritative state files, while the `CLIProxyAPI` anchor hit 23/11 → grep works → collision-clean.** The v207 §C row and the v69/v179 stealth row were read verbatim from `_patterns/06` to establish the two boundaries above.

**Two errors caught by hand:** (1) `core/routes.py` has no `/v1/chat/completions` — I checked `server.py` before reporting a discrepancy, and there is none (the v193 false-drift lesson); (2) `config.example.json` has no stealth/cloak key — resolved by hand to `browser.executable_path`, which *is* the cloak hook, rather than reported as an inconsistency. **One real drift confirmed** (`CoreNexus`) only after a targeted re-fetch designed to exclude a summarizer artifact.

**inflation_check HELD:** 0 mints; the N=1 §C mint DECLINED per §28 + the cortex-hub v181 / v180 weak-anchor precedent and recorded as the reviewable alternative; the v207 N=3 and v69/v179 N-bump both explicitly declined; counts 46/11 unchanged; max #85; no double-count; #57 and #18 #8 recorded, not self-incremented.
