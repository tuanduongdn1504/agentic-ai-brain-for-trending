# (C) CLIProxyAPI — Verdict

> **Wiki v207** · 2026-07-16 · `router-for-me/CLIProxyAPI` · operator-requested.
> Verdict produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions`. **No workflow relied on** (the ~205K shim overflows subagent context → prompt-too-long, the v200/v202/v204/v205/v206 self-throttle precedent). Source hand-fetched (repo page + README + help.router-for.me + a setup guide); identity + landscape + ToS by WebSearch; **collision + the eceasy↔cortex-hub link by hand-grep of `_state/`+`_patterns/`**.

---

## Verdict line

**GOAL-ALIGNED INCLUDE 3/4 · [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG] · Tier T2 Service · 1 NEW §C standalone at N=1 (CORPUS-FIRST for the surface, NOT world-first) · counts UNCHANGED 46/11.**

⚠️ **On-goal as a KNOWLEDGE/landscape subject, but pilot-AVOID for Claude** (ToS-violating + Anthropic-blocked since April 2026 + account-ban risk).

---

## The four criteria

### (a) FAIL — cleanly
`router-for-me` / "Router-For.ME" is a **bare org** (footer "Copyright © 2025-present Router-For.ME"; no disclosed individual/company), **not Anthropic**. §41 keys (a) on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source only — no name/heritage/locale/notability inference, and there is no disclosed individual to even consider. The **DeusData v172 / Jo-Inc v179 / iOfficeAI v206 bare-org** situation. → **#19 19a first `router-for-me` author** (an institutional-portfolio data-point, not a new axis).

### (b) STRONG — keys the tier (⚠️ ToS-gray → pilot-AVOID-for-Claude, recorded)
CLIProxyAPI is **mature, canonical LLM-access / provider-routing infrastructure** sitting on the *exact* substrate the vault has repeatedly studied — cc-switch v73 / freellmapi v112 / CodexPlusPlus v117 / ai-switcher v153 are all corpus subjects in this neighborhood — and it is **dead-center on the operator's live `claude-api-cost-optimization` pilot thread**. It was also a **load-bearing dependency of cortex-hub v181** (§5 of the Deep Dive). Studying it teaches the LLM-gateway landscape *and* the subscription-vs-API ToS boundary, which is directly relevant to hireui (which will consume LLM APIs).

**STRONG-not-STRONGEST** because: third-party gray-zone infra (not Anthropic substrate); Claude is one of several wrapped providers; **and its flagship value-prop (free Claude via API) is ToS-violating, Anthropic-blocked (April 4 2026), and account-ban-risk.** The gray-zone does NOT make it off-goal — the corpus routinely includes dual-use/gray-zone subjects (opencode-antigravity-auth v67 OAuth bridge / CloakBrowser v69 / camofox v179 / Strix v190). It makes it a **fenced, pilot-AVOID-for-Claude** subject. GOAL-ALIGNED per §31 (keys on (b) STRONG).

### (c) STRONG — with honest caveats
Go 100% · MIT · ~42.4k★ · **761 releases** (extraordinary velocity) · v7.2.80 · multi-provider OAuth + full multi-protocol endpoint compatibility + multi-account load-balancing + Go SDK + Management API + a whole ecosystem (EasyCLI Tauri GUI + Management-Center WebUI + 20+ community projects + adopted as cortex-hub v181's gateway). **Caveats foregrounded:** (1) **NOT source-cloned** — internal Go architecture documented-not-inspected; (2) star count page-stated §37.4 (42.4k vs 42.2k across sources → **not #52**); (3) the **ToS gray-zone / account-ban risk**; (4) the docs' own "model name ≠ backend" alias footgun; (5) OAuth-credential storage format/encryption undocumented; (6) no prominent legal/ToS disclaimer surfaced (unlike v67's CAUTION block — noted, not asserted-absent).

### (d) STRONG
cc-switch v73 (LV#22 8a) + freellmapi v112 (LV-C2) + CodexPlusPlus v117 (LV-C2 + LV#22 8b) + ai-switcher v153 (§C + LV#22 8c) + **opencode-antigravity-auth v67** (closest cousin — single-provider OAuth-credential bridge, Pattern #83 83c, T4) + Pattern #18 #8 (Multi-Source LLM Aggregator) + the claude-api-cost-optimization pilot thread + **cortex-hub v181** (bundled it) + EasyCLI (its own Tauri GUI). Dense.

---

## Pattern outcome — 1 NEW §C standalone at N=1

**MINT: "Self-Hosted Multi-Provider API Gateway that Re-Exposes CLI-Tool OAuth Subscriptions as OpenAI/Gemini/Claude/Codex-Compatible Endpoints"** — N=1.

**Scope: CORPUS-FIRST for the multi-provider-subscription-gateway surface, NOT world-first.** The class is populated (`aryan877/claude-proxy` peer + `CliRelay`/`kur4ge`/`ben-vargas/ai-cli-proxy-api` forks/downstreams); CLIProxyAPI is the **world-canonical, most-forked flagship** (the Kilo-Code v177 / awesome-llm-apps v201 precedent). Mint at N=1 per the serve-sim v183 / fff v194 / page-agent v199 / career-ops v200 / OfficeCLI v206 precedent (canonical-flagship-of-a-real-class + corpus dependency + a genuinely distinct capability) AND the **ai-switcher v153 neighborhood precedent** (ai-switcher got its own N=1 §C standalone distinct from cc-switch/CodexPlusPlus because its *capability* was distinct — same logic here).

**DISTINCT from:** cc-switch v73 (config-switcher, points a client elsewhere — no gateway) · freellmapi v112 (free-tier stacking — no subscription-OAuth) · CodexPlusPlus v117 (reseller relays — sells API access; CLIProxyAPI uses *your own* subscriptions) · ai-switcher v153 (multi-account rotation — no unified API front) · Pattern #18 #8 (generic provider aggregator — CLIProxyAPI *is* an instance, but subscription-OAuth-source + unified-multi-protocol-front is the distinctive) · opencode-antigravity-auth v67 (single-provider OAuth-credential *bridge plugin*, T4 — same core OAuth-reverse-engineering idea, different shape/scope/tier).

### ⚠️ Two boundary/NO-MINT alternatives recorded operator/audit-reviewable
1. **N=2-not-N=1:** if "reverse-engineer a CLI-tool's OAuth to use its subscription programmatically" is read as the class, **opencode-antigravity-auth v67** (single-provider bridge) is the un-registered N=1 and CLIProxyAPI is N=2 (the camofox v179 / codebase-memory-mcp v172 / Strix v190 clean-2nd-instance precedent). **I lean N=1-for-the-gateway-surface** (v67 = a single-provider bridge *plugin* T4; v207 = a multi-provider API-gateway *service* T2 — distinct shape/scale/tier), but flag it.
2. **NO-MINT:** it's simply an instance of Pattern #18 #8 (Multi-Source LLM Aggregator) + LV-C2 economics, with subscription-OAuth as a source-variant (the camofox v179 "don't-draw-the-circle" reading). **I lean MINT** (canonical flagship + corpus dependency + distinct source/mechanism/ToS-profile), but record it.

**Either reading → counts UNCHANGED 46/11.**

---

## Secondary (NOT minted)
- **#19 19a** first `router-for-me` author.
- **Corpus-recursive DEPENDENCY cross-ref** — cortex-hub v181 bundled `eceasy/cli-proxy-api` as its gateway (v181 bundled TWO now-corpus subjects: GitNexus v33 + CLIProxyAPI v207). **NOT #57** (silent bundling, not an influence-citation; and the direction is earlier-ship-bundled-this).
- **Pattern #18 #8 (Multi-Source LLM Aggregator) instance-strengthening** — CLIProxyAPI routes/aggregates providers (N = audit bookkeeping, recorded not self-incremented).
- **LV-C2 (Cost / Capacity Economics) cross-ref** — subscription-arbitrage as a cost-economics sub-theme, a DEFERRED watch axis alongside relay-reseller (v117) + free-tier-stacking (v112).
- **opencode-antigravity-auth v67 OAuth-reverse-engineering cousin** — see boundary alt #1.
- **EasyCLI = Router-For.ME's Tauri desktop GUI for the proxy** → **LV#22 (Tauri Management-GUI) ADJACENCY** (manages a *proxy*, not "another coding agent" directly → NO N-bump; the agency-agents v185 Tauri-adjacency discipline).
- **#66 supply-chain / ToS / DUAL-USE (load-bearing):** core mechanism ToS-violating for Claude (Jan-2026 enforcement + April-2026 block + account-ban risk); Docker `curl`/compose install; captures + persists subscription OAuth tokens (credential-sensitive); no prominent disclaimer surfaced.

## Non-claims
- **NOT #18 B1-MCP** — a REST API gateway; ships NO MCP server (a downstream community project wraps it).
- **NOT #52** — metrics page-stated §37.4.
- **NOT #57** — bundled-by-v181 = dependency not citation; cites no corpus subjects as influences.
- **NOT world-first** — populated class.
- **NOT a new top-level pattern** — max stays #85.
- **NOT source-verified at the Go level** — flagged.

---

## inflation_check — HELD
1 mint (≤2 cap honored); N=1 scoped corpus-first-**for-surface**-NOT-world-first with the landscape credited + both boundary alternatives recorded; counts UNCHANGED 46/11; max #85; no double-count (#18 #8 aggregator vs the §C standalone are different axes); no N-bumps on #18/#84/LV#22/LV-C2 (all recorded-not-self-incremented). The corpus-recursive-dependency finding was **hand-verified** (the `eceasy/cli-proxy-api` ↔ cortex-hub v181 link), not confabulated.

---

## Streak / §35
- §C live standalones **41 → 42**; tracked PROVISIONAL surface **≈48 → ≈49**.
- Streak **GA:66 → GA:67** (53 consecutive goal-aligned ships v153→v207).
- §35 CLEAR — window {v205 GA, v206 GA, **v207 GA**} = 0 OG (v203 = audit, excluded).

---

## PILOT (one-line)
On-goal as a **landscape/knowledge** subject + directly relevant to the cost-optimization thread, but **pilot-AVOID for Claude** (ToS violation + Anthropic block + ban risk). Value = read/learn the LLM-gateway landscape + the ToS boundary (zero risk) + understand the cortex-hub v181 dependency you already catalogued; the one genuinely on-goal borrow = its multi-protocol provider-routing **architecture** as a reference for hireui's future vendor-seam (with **official API keys**, never subscription-OAuth). Full 24-method menu in `(C) CLIProxyAPI — Pilot Methods Menu.md`.
