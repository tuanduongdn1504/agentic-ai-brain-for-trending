# (C) gemini-web2api — Verdict + Pattern Outcome

**Wiki v232 · 2026-08-17 · `Sophomoresty/gemini-web2api`**
*Routine v2.7. Verdict produced INLINE + fully hand-verified per `feedback_wiki_verify_independently_check_collisions` — no workflow, no subagent (the ~1.09 MB shim overflows every subagent >200K; the v200→v231 self-throttle).*

---

## Headline

> **GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · **(b) MODERATE keys the tier** ⚠️ STRONG + OFF-GOAL both reviewable · (c) MODERATE ⚠️ STRONG-reviewable · (d) STRONG
>
> **1 NEW §C standalone at N=2**, crediting v231 CoreOfPotato's un-registered priority.
> **Counts UNCHANGED 46 top-level / 11 CONFIRMED.** §C live standalones **47 → 48**; tracked surface **≈54 → ≈55**.
> **Streak `GA:90 · OG:13 [7 ov]`** (13 consecutive GA post the v219 OG break). **§35 CLEAR.**
> **Tier T2 Service.** **PILOT: ⚠️ pilot-AVOID — read-only payoff.**

---

## 1. Four-criteria scoring

### (a) FAIL — §41

Author **Sophomoresty (靝悠Sol)** is a disclosed individual — per their own verbatim bio, an undergraduate (SCU = **Sichuan University**, based in Shanghai/Fudan) who *"somehow ended up doing AI-powered reverse engineering."* **Not Anthropic.** No declared affiliation, no registered (a)-7 vendor-direct source.

No rescue is taken on name, heritage, locale, or notability (§41). The disclosed-individual (a)-axis remains **answered NO** and unregistered per the v212 audit (rec-ii). **#19 19a** — first `Sophomoresty` author in the corpus.

### (b) MODERATE — keys the tier ⚠️ *both neighbours reviewable*

**FOR MODERATE+ (→ GOAL-ALIGNED per §31; no §40 needed):**

1. **LLM-access-gateway infrastructure is the corpus's densest tooling thread** — `opencode-antigravity-auth` v67, `cc-switch` v73, `freellmapi` v112, `CodexPlusPlus` v117, `ai-switcher` v153, `CLIProxyAPI` v207, `OmniRoute` v208, `CoreOfPotato` v231. This is squarely inside it.
2. **The intended clients include coding agents** — `/v1/responses` exists for **Codex CLI**, `/v1beta/models` for **Gemini CLI**.
3. **It sits on the live `claude-api-cost-optimization` thread**, at its free-tier-harvesting pole.
4. **It is a genuinely instructive protocol-RE artifact** — ~350 stdlib lines that reconstruct Google's own web auth and speak its private RPC.
5. **The sharpest on-goal payoff: a second, independent, source-verified instance of the same broken-authentication triad** (bind-all-interfaces + wildcard CORS + fail-open auth) on a local service holding live AI-account credentials. Two independent projects, same class, same defect shape ⇒ a *confirmed recurring* anti-pattern, directly red-teamable against hireui.

**HELD BELOW STRONG:**

- **Claude appears nowhere in the subject.** Gemini only.
- **Single-vendor** — narrower than v231's three.
- **Nothing is safely pilotable** (ToS-gray by construction).
- **The hard parts are Google's** — the model, and the protocol it merely re-implements.

Calibration: at/just-above **v180's (b) MODERATE**, level with **v231's**, clearly below **v207/v208 (b) STRONG**. Gray-zone ≠ off-goal (the v67 / v179 / v190 / v207 / v208 precedent).

⚠️ **STRONG reviewable** — the landscape finding that the identical technique already targets **claude.ai** (`cyberanrhy/gemini-claude-web2api`, §9.1 of the Deep Dive) makes this class an active abuse vector against Anthropic's own consumer product, and the security finding is unusually transferable. *Held at MODERATE because (b) scores the SUBJECT, and the Claude-targeting sibling is not a property of this subject.*

⚠️ **OFF-GOAL reviewable** — Claude-absent, ToS-violating, nothing pilotable → `GA:89 · OG:14`, and **§35 would still be CLEAR** (1 OG in the rolling-3 window ≤ 1).

### (c) MODERATE ⚠️ STRONG-reviewable

**FOR:** a real, working, genuinely non-trivial artifact — `SAPISIDHASH` reconstruction, `wrb.fr` batchexecute parsing, three API-shape translations, tool calling, streaming, multimodal, **all on the Python standard library** (`httpx` optional); ~2.7k★ / 6 contributors / 59 commits; an 8-module package *and* a 1,108-line self-contained script; Docker + Cloudflare Worker + a purpose-built browser extension; a `tests/` directory; Trendshift-tracked twice.

**AGAINST (why it lands at MODERATE):**

- **No releases published** — v1.1.0 lives only in `pyproject.toml`.
- **CI is `docker.yml` only** — the tests exist but are **not gated** (the geti v213 "CI build-only" shape).
- **No `__Secure-1PSIDTS` rotation** — materially behind the mature upstream `HanaokaYuzu/Gemini-API`, which rotates every ~9 minutes because Google expires it fast.
- **A hardcoded Google build ID** (`boq_assistant-bard-web-server_20260716.08_p0`) — fragile by construction.
- **Two implementations of the same protocol in one repo** (single file + package), provenance between them unstated → drift risk.
- **NOT source-cloned** (hand-fetched file-by-file; the v200→v231 self-throttle).

Recorded at MODERATE deliberately: the corpus reserves (c) STRONG for depth **plus maturity**, and the maturity half is conspicuously thin. The operator may flip it — (c) does not key the tier.

### (d) STRONG

Dense, live cross-references: **v231 CoreOfPotato** (the direct N=2 partner, opposite mechanism) · **v207 CLIProxyAPI** + **v208 OmniRoute** (the sibling OAuth-subscription class; and OmniRoute has *shipped* a `gemini-web` provider) · v67 / v73 / v112 / v117 / v153 (the LLM-access-tooling family) · **LV-C2** cost economics · the anti-detect thread v69 / v179 (header-level only) · `#66` dual-use/ToS · the `claude-api-cost-optimization` pilot thread · hireui's API-security / BOLA thread.

---

## 2. Collision check — CLEAN

Sanity-anchored hand-grep over both authoritative state files (`_state/03c-projects-v61-v183.md`, `_patterns/06-library-vocab-registry.md`):

| Term | `_patterns/06` | `_state/03c` |
|---|---|---|
| `CoreOfPotato` *(anchor)* | 1 | 1 |
| `CLIProxyAPI` *(anchor)* | 12 | 24 |
| `gpt4free` *(anchor)* | 1 | 2 |
| **`gemini-web2api`** | **0** | **0** |
| **`web2api`** | **0** | **0** |
| **`Sophomoresty`** | **0** | **0** |
| `gemini-webapi` / `HanaokaYuzu` | 0 | 0 |

Three anchors hit ⇒ the grep works ⇒ the empty subject rows are trustworthy. **Collision-clean.** First `Sophomoresty` author; first appearance of this specific project or its upstream library family in the corpus.

---

## 3. PATTERN OUTCOME — 1 NEW §C standalone at N=2

> **"Self-Hosted Gateway that Harvests a Free Consumer AI Web-Chat Entitlement and Re-Exposes It as an OpenAI-Compatible API"**
>
> **N=2** — v231 CoreOfPotato (`hwahao`) + **v232 gemini-web2api** (`Sophomoresty`)
>
> **NOT corpus-first** (v231 holds priority) · **NOT world-first** (gpt4free / HanaokaYuzu / a saturated ecosystem)

### 3.1 Why mint now, when v231 declined eight days ago

v231 declined on **two** grounds. One survives; one is discharged.

**Ground (1) — "NOT world-first, and not close."** Still true. But **not independently disqualifying under this corpus's own precedent**: `CLIProxyAPI` v207, `OfficeCLI` v206 and `grok-build` v215 were each minted explicitly *"corpus-first for the surface, NOT world-first"*, and `Firecrawl` v214 was minted while being **neither** corpus-first nor world-first. Not-world-first has never, on its own, blocked a §C row.

**Ground (2) — "weak + early anchor"** (the cortex-hub v181 precedent: 16★, 7 commits, 4 days, stale, thin orchestration layer). **This is now discharged.**

| | v231 CoreOfPotato | **v232 gemini-web2api** |
|---|---|---|
| Stars | ~16 | **~2.7k** |
| Commits | 7 (4 of them `fix(ci)`) | **59** |
| Contributors | 1 | **6** |
| Lifespan | 4 days, then stale ~2 months | maintained; Trendshift-tracked twice |
| Substance | thin wrapper over CloakBrowser + Playwright | **own protocol implementation, zero required deps** |
| Provenance | almost certainly vibe-coded (verified drift tell) | independent RE; drift check came back **clean** |

**And v231 said so itself**, verbatim in its own ship record: *"mint later on a clean exemplar (gpt4free), crediting v231 as the prior data-point."* v232 is a materially cleaner exemplar.

### 3.2 The precedent this follows

Four prior ships used exactly this move — **mint the species row at N=2, crediting an un-registered first instance**:

- **camofox-browser v179** → credited `CloakBrowser` v69
- **codebase-memory-mcp v172** → credited `codegraph` v70
- **Strix v190** → credited `shannon` v45
- **Firecrawl v214** → credited `crawl4ai` v29

v232 is the same shape, and stronger than most of them on one axis: the two instances are **cross-author, cross-language, cross-vendor-target, and cross-*mechanism***.

### 3.3 Why the two instances are one species and not two

They harvest the **same kind of entitlement** (a free consumer AI web-chat session) and produce the **same artifact** (a local OpenAI-compatible endpoint). They differ only in *how* they reach it:

- **v231:** drive the real UI in an anti-detect browser and scrape the DOM.
- **v232:** skip the UI entirely, speak the private RPC directly with a reconstructed auth header.

That is **within-species variation on the access vector** — the camofox v179 "don't draw the circle around the delivery form" discipline. Minting two rows here would be the over-claim.

### 3.4 ⚠️ TWO reviewable alternatives — recorded, NOT self-executed

**(A) NO MINT.** *"Keep v231's DEFERRED watch axis. The class is a saturated fork ecosystem whose canonical exemplar (gpt4free, or `HanaokaYuzu/Gemini-API`) is still not a corpus subject; §28 says wait for the flagship."* Defensible. **Loses** to the four-precedent N=2-crediting-priority move, and to the observation that waiting has already produced two instances without a flagship arriving.

**(B) GENERALISE THE v207 ROW INSTEAD.** Restate v207's row from *"re-exposes **CLI-Tool OAuth Subscriptions**"* to *"re-exposes a **non-API consumer entitlement**"*, absorbing v231 + v232 as instances.

⚠️ **This is precisely the alternative v231 flagged to the audit and explicitly did not self-execute, and I hold the same line — for a concrete reason.** The v207 row is **PROMOTION-ELIGIBLE at a non-port N=3**. Generalising it would sweep v231 and v232 in as instances #3 and #4 and thereby **silently fire a promotion-to-CONFIRMED trigger**, changing the headline counts. **A promotion is an audit act.** Recorded prominently, not executed.

### 3.5 ⚠️ BOUNDARIES HELD (each easy to over-claim)

1. **NOT an N=3 of the v207 §C row.** That row is scoped to *"CLI-Tool OAuth Subscriptions."* v232 harvests a **free consumer web-UI entitlement** — a different source mechanism. **The v207 promotion trigger is NOT fired.** (Same boundary v231 held; the geti-v213-is-not-a-v192-N=3 discipline.)
2. **NOT an instance of the stealth/anti-detect browser row** (v69 + v179, N=2). v232 does header/User-Agent/Referer mimicry only — no patched browser, no fingerprint spoofing. It is not even a *consumer* of that class, unlike v231. **No N-bump.**
3. **NOT a Pattern #18 #8 (Multi-Source LLM Aggregator) instance.** v232 is **single-source** (Gemini only). v231 was multi-source; this is not. Recorded as a non-claim.
4. **NOT world-first.** Named peers: `gpt4free`, `HanaokaYuzu/Gemini-API` (~3k★, the mature upstream, and it rotates tokens where v232 does not), `Nativu5/Gemini-FastAPI` (646★), `ntthanh2603/gemini-web-to-api` (193★), `XxxXTeam/geminiweb2api` (54★), `n0madic/go-gemini-web2api`, same-name forks `cyberanrhy/` and `one880808/`, a JS/Workers port, and the `gemini-proxy` GitHub topic.

### 3.6 Bookkeeping

- Counts **UNCHANGED**: 46 top-level patterns / 11 CONFIRMED Library-vocab.
- §C live standalones **47 → 48**; tracked PROVISIONAL surface **≈54 → ≈55**.
- §28 ≤2-mints cap honored (**1** mint).
- **PROMOTION-ELIGIBLE at a genuinely-independent N=3.** Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).
- ⚠️ **Flagged to the badly-overdue audit** (last audit v212; v213–v232 all shipped since).

---

## 4. SECONDARY observations — recorded, NOT minted

- **`#19` 19a** — first `Sophomoresty` author; and a coherent **"entitlement-circumvention builder" portfolio archetype** (paywall bypass across 936 sites · DRM'd music decryption · 90+ educational-platform video downloading · free Google-AI-Mode search as an MCP server · free Gemini as an API). ⚠️ `gemini-search-mcp` applies the same move to **search, delivered as MCP** — an adjacency only; **v232 ships no MCP server**.
- **LV-C2 (LLM-access economics)** — the ledger now reads: config-switch v73 · free-tier-stack v112 · reseller-relay v117 · multi-account-rotate v153 · OAuth-bridge v67 · subscription-re-exposure v207 + v208 · **web-UI harvesting v231 (UI-automation) + v232 (protocol-RE)**. The subscription-arbitrage watch axis gains a second, mechanically distinct sub-variant.
- **⚠️ The class already targets Claude** — `cyberanrhy/gemini-claude-web2api` (*"proxy for Gemini **and Claude** Web APIs. Free AI access via cookie auth"*) applies this identical technique to **claude.ai**. Recorded as a **DEFERRED watch axis** and as the strongest reason this class warrants the vault's attention. **NOT a property of v232.**
- **⚠️ A corpus subject already productised this class** — OmniRoute (**v208**) issue **#2378** requested a `gemini-web` provider *"similar to existing `chatgpt-web`, `grok-web`, and `copilot-web`"*, closed by **PR #2380**. Four web-UI-harvesting providers now ship inside a corpus subject. The issue cites four other projects and **not** this subject ⇒ a **landscape** link, **NOT `#57`**.
- **`#83` honest-disclosure — NEGATIVE data-point.** No ToS / legal / account-ban disclaimer in either README, on a tool that is ToS-gray by construction. (Credential-hygiene warnings *do* appear in the extension and Cloudflare READMEs.) **Weaker disclosure than v231**, which shipped a DISCLAIMER conceding ban risk.
- **"AI-Generated-Repo Artifact Contamination"** (the v69-era candidate v231 instantiated) — **checked and came back CLEAN here**. The "Zero auth" / "Zero cost" tagline split is a genuine dual-phrasing across two locations, both accurate. Recorded as the **negative control** for that candidate axis.
- **Anti-detect technique cross-ref** — header/UA/Referer/Origin mimicry + `X-Same-Domain: 1`, plus the Cloudflare Worker's stated browser-fingerprint rotation. Cross-ref to v69 / v179 only. **NO N-bump.**
- **`#66` — the sharpest section.** Install **BENIGN** (stdlib + optional `httpx`; no `curl|bash`, no compiled binary, no postinstall, no telemetry — materially safer than v231's black-box Chromium). Runtime is the concern: **`host: 0.0.0.0`** + **unconditional `Access-Control-Allow-Origin: *`** + **`if not keys: return True`** (auth fails open, and the zero-key mode is *advertised*) + a hardcoded `"api_keys": ["sk-gemini"]` default credential + `log_requests: true` (prompts to local logs) + a browser extension that extracts live Google session material + a Cloudflare path that stores your Google cookies as third-party edge env vars.

---

## 5. NON-claims

**NOT** `#52` (~2.7k★ / ~607–627 forks / 59 commits page-stated §37.4; **no releases published**; ⚠️ Trendshift lists it as "#7 **JavaScript** Repo of the Day" despite Python primary — a categorisation oddity → velocity unestablishable) · **NOT** `#57` (credits linux.do and "the open-source API proxy ecosystem" — no corpus subjects; and it does **not** wrap `HanaokaYuzu/Gemini-API`, confirmed by zero declared dependencies) · **NOT** `#18` B1-MCP (ships no MCP server) · **NOT** `#18` #8 (single-source) · **NOT** world-first · **NOT** corpus-first (v231 holds priority) · **NOT** a v207 N=3 · **NOT** a v69/v179 stealth-browser instance · **NOT** a new top-level pattern (max #85) · **NOT** source-cloned.

---

## 6. Tier & streak

**Tier T2 Service** — self-hosted local gateway service (the `CLIProxyAPI` v207 / `OmniRoute` v208 / `CoreOfPotato` v231 / `freellmapi` v112 family).

**Streak:** v231 `GA:89` → **`GA:90 · OG:13 [7 ov]`** — **13 consecutive GA** since the v219 OG break.
**§35 CLEAR** — rolling-3 window {v230 GA, v231 GA, **v232 GA**} = 0 OG.
*(Under the reviewable OFF-GOAL reading: `GA:89 · OG:14`, window = 1 OG ≤ 1 → still CLEAR.)*

**inflation_check HELD** — 1 mint (≤2 cap); filed at an honest **N=2**, not an N=1 over-claim; both reviewable alternatives recorded; three boundaries held; counts 46/11 unchanged; max top-level pattern still #85; no improper N-bumps (#18 #8 declined, stealth-browser declined, MCP declined).

---

## 7. Verification record

Produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions`. **No workflow, no subagent** (the ~1.09 MB shim overflows every subagent >200K → prompt-too-long; the v200→v231 self-throttle).

- **Source hand-fetched:** repo page · `README.md` · `README_CN.md` · `pyproject.toml` · `config.example.json` · `gemini_web2api/gemini.py` · `gemini_web2api/server.py` · `gemini_web2api.py` · package / extension / cloudflare / workflows trees · releases page · Trendshift · author profile.
- **Independent verification by WebSearch:** author identity · the landscape and world-first denial · the OmniRoute-v208 link (fetched the issue directly).
- **Collision:** sanity-anchored hand-grep, three anchors hitting (§2).
- **Boundary rows read verbatim** from `_patterns/06` — the v207 §C row (line 100) and the v212-audit §F entry (line 236), to establish the not-an-N=3 boundary and the promotion-trigger risk in alternative (B).

**Three errors caught by hand:**

1. An author characterisation of *"reverse engineer and penetration tester… offensive security tool developer"* — **not supported** by the verbatim bio. Discarded.
2. "SCU" read as **Santa Clara University** — in context (Shanghai, FDU = Fudan, Chinese-language repos) it is **Sichuan University**. Corrected.
3. A tagline discrepancy ("Zero auth" vs "Zero cost") that looked like the v231 drift tell — **re-checked and resolved clean**: two real strings in two locations, both accurate.

---

## 8. Verdict in one paragraph

**gemini-web2api is a small, genuinely clever, independent piece of protocol reverse-engineering that turns Google's private Gemini web RPC into a free OpenAI-compatible endpoint — and it ships binding to every interface, with wildcard CORS, and an auth check that fails open.** It is materially better built than the corpus's previous instance of this class and materially less mature than the class's actual flagship. It earns its place for three read-only reasons: it is the **second independent instance** of the web-UI-harvesting species, on a **completely different access vector**, which makes that species real; it is the **second independent specimen of the same broken-authentication triad**, which turns a one-off observation into a red-team check worth running against hireui; and the class it belongs to demonstrably **already targets claude.ai**. Do not run it against anything you care about.
