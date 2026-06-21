# (C) v179 camofox-browser — Verdict & Collision-Check Record

**Subject:** `jo-inc/camofox-browser` (npm `@askjo/camofox-browser`) · v1.11.2 · MIT · © 2025 **Jo, Inc** (askjo.ai)
**Ship date:** 2026-06-22 · **Routine:** LLM Wiki Routine v2.6 (Phase 0.9 STRICT; §31 tier keyed on (b))
**Method:** built **inline** (NOT the 3-lens+critic multi-agent workflow — per vault memory `feedback_wiki_verify_independently_check_collisions`, that workflow confabulates corpus facts; this verdict was verified by hand: re-clone at `ce3a3b0` + source greps + collision grep over `_state/*.md` + `_patterns/*.md` + `03 Projects/`).

---

## Phase 0.9 STRICT — GOAL-ALIGNED INCLUDE 3/4

### (a) FAIL — clean
Author = **Jo, Inc** (askjo.ai), a consumer-AI-agent **company**, not Anthropic. (a)-7 is Anthropic-only; "a startup building a personal AI agent" is not the individual cultural-peer axis. **Declared-non-Anthropic-institution** — matches Kilo AI v177 / NVIDIA v169 / DeusData v172 / CloakHQ v69. No heritage rescue (the v159→v178 discipline; standing rec (ii)). **First Jo-Inc author in the corpus → a #19 19a institutional data-point** (NOT a new (a) axis).

### (b) STRONG — keys the tier
camofox-browser is an **anti-detection browser-automation server *for AI agents*** — a REST API + an OpenClaw agent-plugin (11 tools) + **token-efficient accessibility snapshots with stable element refs** that give a coding/automation agent a stealthy browser it can actually drive. That is dead-center agent-autonomy substrate (Goal #1). It is **directly pilotable** into the vault's own Claude Code (give it a browser for one real web task) and into hireui automation.
**STRONG-not-STRONGEST** because: third-party; the *native* plugin targets **OpenClaw** (Claude/Claude Code consume via the agent-agnostic REST API, not a first-class Claude integration); and it is **capability-augmentation** (extends an agent's reach) rather than Claude/Anthropic substrate. Calibrates to **Agent-Reach v174 (b) STRONG** (web-reach capability layer) — same shape, different verb (act-on-a-browser vs read+search). A clear tier above **GLM-5 v176 (b) MODERATE** (raw model, nothing to pilot but swap a backend).

### (c) STRONG
`server.js` = 6,133 lines; **23 `lib/` modules**; **3 sub-plugins** (persistence/vnc/youtube) on an internal event bus; a **Cloudflare Worker** telemetry sink; **37 REST routes**; **11 agent tools**; Prometheus (`prom-client`) + Sentry observability; Docker/Railway/Fly deploy; OpenAPI generation; Jest unit/e2e/live/plugin suites; per-user session isolation; proxy+GeoIP; lazy/idle self-healing lifecycle (mem-threshold restarts). Substantial real engineering.
**Honest caveat:** the *hard* fingerprint-spoofing lives **upstream in Camoufox/Firefox (C++)**, not in this repo — camofox is the orchestration/service/agent-surface layer on top. Single-vendor, actively-versioned (v1.11.2).

### (d) STRONG
Anti-detect-browser sibling **CloakBrowser v69** (the N=1 of the species) + agent-browser-automation **browser-use v34 / Skyvern v24** + web-capability **Agent-Reach v174 / crawl4ai v29** + scraping **Scrapling v149** (LV #21). Pattern cross-refs: #18 (agent-tool server), #66 (supply-chain/dual-use), #84 84c (agent-agnostic surface), #19 19a (new org).

**Verdict: GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG].**

---

## Collision check (the load-bearing step)

Hand-grep over `_state/*.md`, `_patterns/*.md`, `03 Projects/` for: `CloakBrowser`, `Camoufox`, `anti-detect`, `anti-detection`, `fingerprint`, `stealth`, `browser-use`, `crawl4ai`, `Skyvern`, `accessibility snapshot`, `Playwright`, `jo-inc`.

**Findings:**
1. **CloakBrowser v69 (`CloakHQ/CloakBrowser`)** = the corpus's **"CORPUS-FIRST purpose-built-for-stealth subject"** (per its `_state/03c` entry, explicitly "vs browser-use v34 / crawl4ai v29 / Skyvern v24 which treat stealth as one feature among many"). It is a **Chromium / ungoogled-chromium** stealth browser delivered as a **Python/JS SDK + Playwright drop-in** (CDP — the codegraph v70 entry registers CloakBrowser as its B2-CDP variant). Anonymous author CloakHQ; dual-licensed.
   → **camofox-browser is NOT corpus-first stealth-browser. CloakBrowser v69 holds priority. camofox = N=2 of the anti-detect-browser species.**
2. **Library-vocab registry (`_patterns/06`) check:** grep for `stealth | anti-detect | CloakBrowser | Camoufox | detection-evas | undetectable` returns **only the Agent-Reach v174 row** (line 82 — matches because its *DISTINCT-from* text mentions "undetectable scraping"). **There is NO dedicated stealth/anti-detect-browser standalone registered.** CloakBrowser v69's stealth-browser observation was a **v2.x phantom-count casualty** (it generated OC-G…OC-J + Pattern #45 45c but no registered §C standalone) — **exactly the codegraph v70 → codebase-memory-mcp v172 situation** (first instance's observation never made it into the registry).
3. `jo-inc` / `Jo, Inc` / `@askjo` — no prior corpus subject. **First Jo-Inc author.**

---

## Pattern outcome — 1 NEW §C standalone at **N=2** (NOT corpus-first)

**MINT: §C Library-vocab standalone "Anti-Detect / Stealth Browser — a purpose-built fingerprint-spoofing browser delivered for automation"**, filed at **N=2**, anchoring:
- **N=1 CloakBrowser v69** (`CloakHQ`) — Chromium/ungoogled-chromium; **SDK + Playwright drop-in (CDP)**; anonymous corporate; dual-licensed. *(Un-registered priority — credited here.)*
- **N=2 camofox-browser v179** (`Jo, Inc`) — Camoufox/Firefox; **REST-API server + OpenClaw agent-plugin + token-efficient accessibility snapshots** for AI agents.

**Why mint, and why N=2 (the v172 precedent, exactly):** the species is real (2 cross-author instances) but was never registered (phantom-count casualty). Per §28 clean-2nd-instance discipline + the **codebase-memory-mcp v172** precedent ("MINT a NEW §C standalone at N=2 to credit the un-registered first instance's priority" — *not* "re-register"), this is a new registry row at N=2, **not** a corpus-first N=1 claim.

**camofox's distinguishing facet (recorded, NOT separately minted):** the **agent-facing-server delivery** — REST API + agent plugin + LLM-token-efficient accessibility snapshots with stable refs — vs CloakBrowser's **SDK/library delivery**. Plus a **different browser engine** (Firefox/Camoufox vs Chromium/ungoogled). These are *within-species* variations + an **adjacency cross-reference** to the agent-capability-layer cluster (Agent-Reach v174 web-reach / browser-use v34 automation). Minting a *separate* N=1 standalone for "anti-detect browser **as agent server**" would be the **"draw-the-circle-to-make-it-first"** over-claim the routine fights → declined.

### SECONDARY (NOT minted)
- **#18 agent-tool-server adjacency** — one backend exposed to agent clients via **REST + an OpenClaw plugin**. ⚠️ **NOT a #18 B1-MCP instance** (it is not an MCP server). Audit-bookkeeping adjacency only.
- **#84 84c provider-agnostic** — REST surface is agent-agnostic; native plugin is OpenClaw-specific. Scoped observation, **NO N-bump** (v86 rule).
- **#66 supply-chain / dual-use** — `postinstall` + `npx camoufox-js fetch` pulls a browser binary at install; bearer-token (`CAMOFOX_ACCESS_KEY`) + cookie-import gating (`CAMOFOX_API_KEY`) + opt-out telemetry; anti-detection = dual-use (account-ban/ToS risk). Cross-reference + pilot fence.
- **#19 19a** — first Jo, Inc author (institutional data-point).
- **Library-vocab #20 Token-Economy** — snapshot windowing (`MAX_SNAPSHOT_CHARS 80000 ≈ 20K tok`, refs-not-HTML) is *thematically* token-economy but carries **no quantified headline benchmark** → **adjacency only, N stays 4** (the v168/v172/v175 deferral posture).

### NON-claims
- **NOT corpus-first stealth-browser** (CloakBrowser v69 precedes).
- **NOT a new top-level pattern** (max stays #85).
- **NOT #52** — stars/forks page-stated only; §37.4 mocks the GitHub API → velocity unestablishable (no star figure asserted).
- **NOT #57** — "stands on the shoulders of Camoufox" = an upstream-dependency credit; Camoufox is not a corpus subject; cites no corpus subjects as influences. *Mentions ≠ recursion.*
- **NOT #18 B1-MCP** (REST + OpenClaw plugin, not MCP).
- **NOT Library-vocab #21 Scrapling** (that's a scraping *library* + tooling-authoring chain; this is a browser *server*).

---

## Counts & streak

- **Top-level / CONFIRMED-vocab counts: UNCHANGED 46 / 10.**
- **§C Library-vocab surface: ≈35 → ≈36** (+1 standalone, filed at N=2).
- **Streak: `GA:40 → GA:41 · OG:11 [7 ov]`** (GA reading; under the operator's defensible OFF-GOAL-v176 reading → `GA:40 · OG:12`).
- **§35 soft off-goal ceiling: CLEAR** — rolling-3 window {v177 GA, v178 GA, **v179 GA**} = 0 OFF-GOAL ≤ 1.
- **26 consecutive goal-aligned ships v153 → v179** (GA reading).
- **inflation_check:** discipline HELD — 1 mint (≤2 cap), filed at the honest N=2 (not an N=1 over-claim), max top-level #85, counts 46/10 unchanged, no double-count (the standalone = *capability species*; #18 adjacency = *distribution structure* — different axes, the v140/v171/v172 precedent).

**Tier: T2 Service** (self-hosted browser-automation server; same tier as CloakBrowser v69 / agentmemory v66 / codegraph v70).

---

## PILOT

**On-goal and genuinely pilotable** — give the vault's own Claude Code (or hireui automation) a stealthy browser via the REST API for one real web task. But it is a **heavier, higher-risk** candidate than the read-only pilots:
- dual-use anti-detection (account-ban/ToS risk — like Agent-Reach v174);
- `postinstall` downloads a browser binary;
- the server drives a real browser and can **import cookies** + **run arbitrary JS in pages** (`camofox_evaluate`).

**Fence:** `install-snapshot` + `npm-security-check @askjo/camofox-browser` (postinstall + binary fetch) + run **LOCAL-ONLY with `CAMOFOX_ACCESS_KEY` set** + scratch automation target + **disposable accounts** for any logged-in site + `CAMOFOX_CRASH_REPORT_ENABLED=false` + pin v1.11.2.

**Pilot ladder placement:** behind the read-only **SkillSpector v169** (first) and **claude-tap v173** (second); **comparable footprint to Agent-Reach v174** (capability gain + account-ban risk + heavy install). PILOT lever still stands (zero piloted).
