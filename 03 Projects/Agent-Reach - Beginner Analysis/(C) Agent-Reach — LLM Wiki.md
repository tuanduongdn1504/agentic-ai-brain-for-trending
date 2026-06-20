# (C) Agent-Reach — LLM Wiki (v174)

> **Ship:** v174 · 2026-06-20 · branch `wiki/v174-agent-reach` off `wiki/v173-claude-tap` (based at `4085da9` = v173, which is itself unmerged — branching off `main` would orphan the v168→v173 cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** **1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1)** — *"Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents (one unified install bundling per-platform readers/searchers behind ordered primary+fallback backends that auto-switch on failure; zero-paid-API posture)."* The corpus's first **federated** read+search capability layer that gives a coding agent reach across many heterogeneous external platforms (open web · social · video · code-host · RSS · finance · podcast · semantic-search) through one install, with per-platform primary+fallback backends that auto-switch on failure. Secondary scoped observations only (#84 84c provider-agnostic · #66 privacy cross-ref · #19 19a indie-builder portfolio · #12 incidental routing-artifacts). NO new top-level pattern (max stays **#85**). Counts UNCHANGED (**46 / 10**); tracked PROVISIONAL §C surface ≈31 → ≈32 (+1 standalone).
> **Tier:** **T2 Service** (a self-hosted local CLI capability-layer you install + run alongside your agent; consistent with v171 devspace / v172 codebase-memory-mcp / v173 claude-tap).
> ✅ **On the goal-#1 substrate core** — fourth consecutive core-substrate ship after v171 devspace + v172 codebase-memory-mcp + v173 claude-tap. Agent-Reach is dead-center on *"master Claude and autonomous agents for software development"*: it gives a coding agent a **genuinely new capability** — the ability to actually read and search the live internet (Twitter, Reddit, YouTube, GitHub, B站, Xiaohongshu, LinkedIn, RSS, semantic search…) without paid APIs — packaged as *"a capability layer, not just another tool."*
>
> ⚠️ **(a) FAIL is genuine, but this is NOT a bare-handle case.** The author discloses an indie-builder identity (display "Pnant Panniantong", bio name **"Neo Reid"**, *"Solo founder. All employees are AI."*, X **@Neo_Reidlab**, sibling project **xfetch**) — like **v171 devspace** (Waishnav), unlike **v173 claude-tap** / **v172 DeusData** (genuinely bare). Per the v171 precedent + standing recommendation (ii), the "solo indie builder building in public" angle is **operator-reviewable + NOT a registered (a) rescue** → clean FAIL under the current rule, no axis minted. This is the **2nd instance** (after v171) of that open question for a software-developer operator — it reinforces the v171 recommendation, it does not resolve it. See §5.
>
> 🔬 **Verdict adversarially verified** (3 distinct lenses + an anti-inflation critic — the v172/v173 model; each lens a different question to avoid the v169 shared-premise cascade). **All 3 lenses CONFIRM the core verdict; cascade risk = ZERO (all three independently keyed the tier on (b), not (a)); inflation_check = discipline HELD.** The critic returned `overall: AMEND` on three documentation points — two incorporated ((a) identity framing; #12 incidental scoping), **one DISMISSED as a confabulation**: a verifier alleged a corpus-collision with "v142 claude-web-research," but independent grep confirmed **no such subject exists** (v142 = OrcaSlicer-bambulab, a 3D-printing slicer) → the fabrication was not propagated, and CORPUS-FIRST N=1 was re-confirmed by the dedicated collision lens's real grep **and** my own. See §6 + §8.

---

## 1. What it is

`Panniantong/Agent-Reach` — description, verbatim:

> *"Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees."*

and the Chinese tagline:

> *"给你的 AI Agent 一键装上互联网能力"* (give your AI Agent one-click internet capabilities)

The design thesis, verbatim — and the key to the whole pattern:

> *"能力层（capability layer），不是又一个工具"* — **a capability layer, not just another tool.**

The problem it names: AI coding agents can write code, edit docs, and manage projects — *"但你让它去网上找点东西，它就抓瞎了"* (but ask it to find something on the web and it's blind). Concretely, an agent on its own can't: pull YouTube subtitles, search Twitter without a paid API, read Reddit (403 blocks), read Xiaohongshu without login, download from B站 (yt-dlp blocked), do semantic web search, parse raw HTML meaningfully, or manage per-platform authentication.

Agent-Reach is the layer that fixes all of that at once. You don't install it yourself — you tell **the agent** a one-liner, and the agent installs and configures it autonomously:

```
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```
(The agent runs `pip install`, detects the environment, and configures MCP. Update analogously via `docs/update.md`.)

It is written in **Python (95%) / Shell (5%)**, licensed **MIT**, latest **v1.5.0** (2026-06-11), 7 releases. Credentials never leave the machine:

> *"Cookie、tokens 永不外传"* — cookies/tokens are never transmitted; stored locally at `~/.agent-reach/config.yaml` with `600` permissions.

**Why this matters for the vault.** This is the missing *reach* organ for a coding agent. The vault's own Claude Code can already read/write code and run tools — Agent-Reach is what lets it actually go read a GitHub issue thread, pull a YouTube talk's transcript, search Twitter/Reddit for prior art, or run a semantic web search — for free, without the operator wiring up a dozen API keys. That is squarely on goal #1 and directly pilotable.

## 2. The 13 platforms + their backends

Each platform is served by an **ordered list of backends** (a primary plus fallbacks). The defining design choice is that *which* backend is used can change without the agent's caller noticing.

| Platform | Primary backend | Fallback | Notes |
|---|---|---|---|
| **Web** | Jina Reader | — | no config; clean HTML→markdown reading |
| **YouTube** | yt-dlp | — | subtitle extraction + search |
| **RSS/Atom** | feedparser | — | no config |
| **Web Search** | Exa (via `mcporter`) | — | **free, MCP-based, no API key** |
| **GitHub** | `gh` CLI | — | auth required for private repos |
| **Twitter/X** | `twitter-cli` (cookie) | OpenCLI | cookie-based, no paid API |
| **B站 (Bilibili)** | `bili-cli` | OpenCLI / search API | *yt-dlp retired — 风控/blocked* |
| **Reddit** | OpenCLI (desktop) | `rdt-cli` | cookie/login required (no anon access) |
| **Xiaohongshu (小红书)** | OpenCLI (desktop) | `xiaohongshu-mcp` / `xhs-cli` | browser login-state reuse |
| **LinkedIn** | `linkedin-scraper-mcp` | Jina Reader | public page access |
| **V2EX** | native API | — | no config |
| **雪球 (Xueqiu)** | native API | — | stock data / search / rankings |
| **小宇宙 Podcast** | Whisper transcription | — | free key required |

The spread is the point: **open web + social + video + code-host + RSS + finance + podcast + semantic-search**, all behind one install — Chinese-internet platforms (B站/小红书/V2EX/雪球/小宇宙) alongside Western ones (Twitter/Reddit/YouTube/LinkedIn/GitHub).

## 3. How it works (the architecture that earns the standalone)

- **Ordered primary+fallback backends per platform.** A fallback is *list reordering, not code rewriting* — the layer keeps an ordered list and promotes a working backend when the primary breaks.
- **Real-time functional detection.** It checks whether a backend actually *works right now*, not merely whether the command exists. Damaged pathways receive repair instructions.
- **Auto-switch on failure, zero user intervention.** Concrete 2026-06 example from the README: yt-dlp got blocked on B站 (风控) → the layer automatically switched to `bili-cli`, with no user action. The durability thesis: *"接入方式会换代，你不用操心"* (access methods will change over time; you don't have to manage it).
- **Health diagnostics.** `agent-reach doctor` reports, in one command: which channels are active, the current backend for each platform, which are functional vs broken, and remediation steps.
- **Zero mandatory API fees.** Every backend is an open-source tool or a free method (Jina Reader, yt-dlp, cookie-based CLIs, Exa-via-MCP without a key). Optional: a ~$1/month residential proxy for geo-blocked access (China-mainland → Reddit/Twitter); local machines need none.

**Supported agents:** Claude Code ✓ · OpenClaw ✓ (needs `tools.profile: "coding"`) · Cursor ✓ · Windsurf ✓ · **any agent that can run shell commands** (LLM-agnostic).

**Integrations:** `mcporter` (MCP-based Exa, no key) · **BrowserAct** (recommended for forms / multi-session / automated login) · **Tencent Cloud OpenClaw** partnership (official distribution channel) · **AtomGit** mirror (China-optimized git access). Auto-installed deps: `twitter-cli`, `bili-cli`, `rdt-cli`, `yt-dlp`, `feedparser`, Node.js, `gh` CLI, `mcporter`, plus the `agent-reach` Python package.

## 4. The distinctive contribution (why it mints a §C standalone — CORPUS-FIRST)

The corpus has plenty of web tools — but none with Agent-Reach's shape. The defining combination is **(federation × capability-layer-for-agents × ordered-fallback-routing × zero-paid-API)**:

| Subject | What it is | Why it is NOT Agent-Reach |
|---|---|---|
| **crawl4ai** (v29) | a single LLM-friendly web crawler/scraper library | no per-platform readers (no Twitter/Reddit/YouTube handlers), no ordered fallback lists, no auto-switch — one crawler, not a federation |
| **browser-use** (v42–v47 era) | browser *automation* for agents (fill forms, click) | drives a browser to *act*; Agent-Reach *reads/searches content* — complementary, opposite job |
| **Scrapling** (v149) | undetectable web-scraping *library* + official agent-tooling (Library-vocab #21) | the *authoring* chain (a library that ships its own skills); Agent-Reach *integrates pre-existing tools* under unified orchestration — different layer |
| **google_workspace_mcp** (v140) | MCP server giving an agent reach into **one vendor's** productivity suite | single vendor (Google); Agent-Reach federates **13 heterogeneous** platforms with fallback routing |
| Jina Reader / Exa | individual backend providers | **components Agent-Reach incorporates**, not competitors — Agent-Reach is the orchestrator above them |

So Agent-Reach is the corpus's **first multi-platform federated read+search capability layer for coding agents**: a single install that gives an agent reach across many heterogeneous external platforms, with each platform's access abstracted behind an ordered, auto-switching backend list, on a zero-paid-API posture, framed explicitly as *"a capability layer, not just another tool."*

**Standalone (the capability):**

> **"Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents (one unified install bundling per-platform readers/searchers behind ordered primary+fallback backends that auto-switch on failure; zero-paid-API posture)."** **CORPUS-FIRST, N=1.** Anchor: **Agent-Reach v174**. PROMOTION-ELIGIBLE at N=2 (a 2nd multi-platform federated read+search capability layer for agents). Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).

The fact that it supports **4+ agents** (and any shell agent) is a separate axis — provider-agnostic distribution, a scoped **#84 84c** observation (§6), no double-count.

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL — but not a bare handle.** The author `Panniantong` (display **"Pnant Panniantong"**) discloses an indie-builder identity: bio name **"Neo Reid"**, since 2020, *"Solo founder. All employees are AI."*, motto *"Ship it. Open-source it. Move on."*, focus *"AI agents that actually do things"*, public **X @Neo_Reidlab**, sibling project **xfetch** (a Twitter CLI scraper). This is **not Anthropic** (the only major-vendor carve-out, (a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only), and "solo indie builder building in public" is **not a registered (a) cultural-peer axis**. It is the **v171 devspace** situation (disclosed indie founder), not the **v173 / v172** bare-handle situation. Per the v171 precedent + standing recommendation (ii), the "indie-builder axis" is logged **operator-reviewable, NOT minted** as a rescue → **clean (a) FAIL, no axis.** ⚠️ This is the **2nd instance** of that exact open question (after v171) for a software-developer operator — recorded as reinforcing the v171 recommendation, not resolving it.
- **(b) STRONG.** Goal #1 = *"master Claude and autonomous agents for software development."* Agent-Reach gives a coding agent a **genuinely new capability** — federated read+search reach across the open web, social, video, code-hosts, RSS, finance, and semantic search — which is core to agent autonomy (an agent that can't read the web is half-blind). It is **Claude-Code-first** among the supported agents and **directly pilotable into the vault** (free multi-platform web research for the vault's own Claude Code). Held at **STRONG (not STRONGEST)** because it is third-party **bundler architecture** (it routes to existing OSS tools; it does not invent retrieval) and a **capability-augmentation** layer — it extends what the agent can reach, it is not the agent itself / not Anthropic core substrate. STRONGEST is reserved for Anthropic core substrate or the agent itself.
- **(c) STRONG.** A real, substantial surface: a Python capability layer; 13-platform federated readers/searchers; **ordered primary+fallback backend routing with real-time functional detection + auto-switch**; `agent-reach doctor` diagnostics; MCP integration (Exa via `mcporter`); credential security (`600`-perm local storage, no-upload, `--safe` / `--dry-run` modes, clean uninstall); **agent-driven self-install**; bundles ~9 backend tools; 7 releases to v1.5.0. Not a prototype.
- **(d) STRONG.** A clean **§C capability standalone** (CORPUS-FIRST, N=1) with an unambiguous home and a clear adjacency map (crawl4ai / browser-use / Scrapling / google_workspace_mcp / Jina+Exa). Nothing is forced.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is **STRONG** (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s FAIL does **not** make a (b)-STRONG subject off-goal — that was the v169 cascade error; the v174 verification gave each lens a distinct question so they could not share that false premise. **Tier: T2 Service.**

## 6. Pattern Library outcome

**PRIMARY — 1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1):**

> **"Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents (one unified install bundling per-platform readers/searchers behind ordered primary+fallback backends that auto-switch on failure; zero-paid-API posture)."**
> Anchor: **Agent-Reach v174** (`Panniantong` / Neo Reid). The corpus's first federated multi-platform read+search capability layer for coding agents. **§28: 1 new standalone (≤2 cap honored). PROMOTION-ELIGIBLE at N=2.** Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).

Distinct from crawl4ai v29 (single crawler library), browser-use (browser automation), Scrapling v149 (scraping library + authoring chain), google_workspace_mcp v140 (single-vendor MCP), and Jina/Exa (components it incorporates) — see §4. **CORPUS-FIRST confirmed by the dedicated collision lens's real grep AND an independent grep** (§8). The standalone is the **capability**; the multi-agent support is a separate axis (below) → no double-count.

**SECONDARY observations (NOT minted):**

- **Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation (NO N-bump).** Agent-Reach is LLM-agnostic and works with Claude Code / OpenClaw / Cursor / Windsurf + any shell-capable agent. This is a **scoped note, not an N-bump** (the v86 discipline). ⚠️ Explicitly **NOT** the v168 ponytail "14-platform **native-rule-file** distribution/generation" mechanism (the v169 contamination — do not repeat it): Agent-Reach is a shared capability layer that *many agents consume*; it distributes *nothing into* each client's native rule format. It is a tool agents call, not a tool that writes itself into agents.
- **Pattern #66 (privacy / security-conscious design) — cross-reference.** Local-only credential storage (`~/.agent-reach/config.yaml`, `600` perms) + no-upload of cookies/tokens + open-source backends + `--safe` / `--dry-run` modes + a clean uninstall + an explicit *"use disposable accounts (封号风险)"* warning = a privacy-conscious posture for a tool that, by construction, handles platform cookies/credentials. Cross-referenced, **not** an N-bump of #66.
- **Pattern #19 sub-archetype 19a (founder/portfolio) — indie-builder data-point.** Unlike the recent bare-handle authors, `Panniantong` / **Neo Reid** discloses a solo-founder/indie-builder identity + a small public portfolio (Agent-Reach + `xfetch`); a data-point of a CONFIRMED pattern, no new sub-mechanism.
- **Pattern #12 (LLM-routing artifacts) — INCIDENTAL scoped cross-ref (NO N-bump).** The install writes **skill files + MCP settings** into the agent (per the uninstall, which "removes config, skill files, MCP settings") — i.e. it emits LLM-routing artifacts. But this is a **side-effect of capability exposure**, not the core pattern (the core is federated read-search across 13 platforms behind auto-switching *data-access* backends). #12 is already CONFIRMED N=5+; this is a scoped note, not an N-bump.
- **Adjacencies noted (NOT members):** the **multi-backend failover** is **data-access routing** (yt-dlp→bili-cli for a B站 blockade), distinct from Pattern #18 #8 *Multi-Source LLM Aggregator* (which fails over among **inference providers** — a different layer). The **zero-paid-API** posture is **data-access economics**, distinct from **LV-C2** *Cost/Capacity Economics of Free-or-Cheap Inference* (which is about **inference** cost). Both are recorded as distinct, not as members.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Max confirmed stays **#85**; the capability lives at the §C-standalone tier per §28 (the same anti-inflation that rejected #86/#88 at v168).
- **NOT Pattern #52 (viral velocity).** **35.2k★ / 2.8k forks / v1.5.0 / 7 releases** are **page-stated, NOT API-verified** (§37.4 — this sandbox mocks the GitHub API). **No API-verified creation date → velocity unestablishable → explicitly not a #52 claim.** (The 35.2k★ figure is notably high and worth flagging, but it cannot ground a velocity claim.)
- **NOT Pattern #57 (corpus-recursion).** The supported-agent list includes corpus subjects (Claude Code, OpenClaw ~ v164 oc-claw, Cursor, Windsurf) — but it lists them as **clients it provisions**, not as **source material / influences it cites.** Mentions ≠ recursion (the v171/v172/v173 discipline).
- **NOT Pattern #18 B1-MCP.** Agent-Reach is a **CLI capability-aggregator** that *uses* MCP for some backends (Exa via `mcporter`); it is **not a single MCP server distributed to many MCP clients.** The multi-client support is the #84 84c axis above.
- **NOT a re-classification / new tier.** A clean §C capability standalone + scoped secondary notes — nothing more.

**Counts UNCHANGED: 46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL §C surface ≈31 → **≈32** (+1 standalone N=1).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** **35.2k★ / 2.8k forks / 7 releases / 290 commits / 37 open issues / 38 open PRs**, latest **v1.5.0 (2026-06-11)** *(as of 2026-06-20 page render, github.com/Panniantong/Agent-Reach — confidence: stated, NOT API-verified)*. **MIT** license. Languages **Python 95% / Shell 5%** (page-stated).
- **No API-verified creation date** → age & velocity **unestablishable** → **explicitly NOT a Pattern #52 claim** (notwithstanding the high page-stated star count).
- **Author identity (verified by direct WebFetch of the GitHub profile, confidence: stated):** display name "Pnant Panniantong"; bio name **"Neo Reid"**; *"Solo founder. All employees are AI."*; motto *"Ship it. Open-source it. Move on."*; focus *"AI agents that actually do things"*; X **@Neo_Reidlab**; sibling repo **xfetch** (Twitter CLI scraper). Affiliation/location **not shown**. Chinese-language origin is an inference from the WeChat-group reference + Chinese-platform focus (confidence: speculation) and is **immaterial** to the (a) FAIL.
- **README contents** (the 13-platform table, the per-platform backends, the ordered-fallback/auto-switch mechanism, `agent-reach doctor`, the security model, the verbatim quotes, the integrations) are page-verified from the rendered README + repo page at ship time. Performance/durability characterizations are vendor-stated, not independently reproduced.

## 8. Streak / state / verification

- **Streak:** `GA:35 · OG:11 [7 ov]` → **`GA:36 · OG:11 [7 ov]`** (36th GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v172 GA, v173 GA, **v174 GA**} = **0 OG → STAYS CLEAR.** No ceiling-override needed or taken.
- **21 consecutive goal-aligned ships v153→v174.** v168/v169/v170 varied the domain; v171/v172/v173 returned to + stayed on the goal-#1 substrate core; **v174 stays on the core** — an agent *capability-augmentation* layer (giving agents web reach), a distinct shape from the v171 (manufacture-an-agent bridge) / v172 (read-only code graph) / v173 (protocol inspection) substrate ships.
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Max pattern #85. PROVISIONAL §C surface ≈31 → ≈32.
- **Override-frequency triggers (2-in-20 / 3-in-30):** v153→v174 = **zero** operator overrides (clean).
- **Build note — verdict produced inline, then adversarially verified by a 3-lens + critic workflow** (each lens a distinct question — goal-relevance/tier/identity · capability-novelty/corpus-collision · secondary/non-claims — to avoid the v169 shared-premise cascade):
  - **Lens 1 (goal-relevance/tier/identity): AMEND** — confirmed (b) STRONG keys the verdict, (a) FAIL, T2 Service, streak math; raised two amendments: (1) the (a) identity should note the disclosed indie-builder identity (matches v171), (2) verify CORPUS-FIRST against "v142 claude-web-research."
  - **Lens 2 (capability-novelty/corpus-collision): CONFIRM** (high) — real grep over the project chapters + registry; no collision; CORPUS-FIRST N=1 justified; distinct from crawl4ai / browser-use / Scrapling / google_workspace_mcp / Jina+Exa.
  - **Lens 3 (secondary/non-claims): CONFIRM** (high) — all four secondaries correctly scoped; all four non-claims correct; recommended upgrading #12 to a *confirmed-incidental* scoped note.
  - **Critic (anti-inflation): `overall: AMEND`** — `cascade_check` = ZERO (all three independently keyed the tier on (b)); `inflation_check` = discipline HELD (1 mint ≤2 cap, N=1 correct, max #85, no improper N-bumps, counts 46/10 unchanged); three amendments to incorporate.
  - **Disposition of the amendments:** (1) (a) identity framing → **INCORPORATED** (independently verified — author discloses indie-builder identity; v171 treatment). (3) #12 incidental scoping → **INCORPORATED**. (2) "v142 claude-web-research" collision → **DISMISSED as a confabulation**: independent grep found **no** "web-research/claude-web" subject anywhere in the corpus, and v142 = **OrcaSlicer-bambulab** (a 3D-printing slicer, T5 out-of-scope). The critic's "resolution" of this concern ("v142 provides single-platform web-search via Exa") was itself invented; neither Lens 1 nor the critic actually read the file. The fabrication was not propagated; CORPUS-FIRST stands on Lens 2's real grep + the independent grep. (Recorded honestly — this is the "verify before recommending; never propagate fabrications" discipline doing its job.)

## 9. Pilot note

Agent-Reach is a **strong, directly-on-goal capability pilot** — distinct in kind from the inspection/memory/bridge pilots ahead of it on the ladder.

- **Why high-value & on-thread:** it gives the vault's own Claude Code (and any agent) the ability to *actually read and search the live internet* — pull a GitHub thread, a YouTube transcript, a Twitter/Reddit search, or a semantic web search — for free, without the operator wiring up a dozen API keys. That is a genuine capability the agent does not otherwise have, and it pairs naturally with the operator's research/autopilot workflows.
- **Risk profile — lower than devspace, but the heaviest install footprint + the only one with account-ban risk:** no remote tunnel / no remote execute (unlike devspace v171); no compiled-binary `curl|bash` (the install is `pip` + agent-driven); credentials are local-only (`600` perms) and never uploaded. **BUT** it installs **~9 backend CLIs + Node.js + the `gh` CLI + `mcporter`**, writes **skill files + MCP config** into the agent, and — for cookie-based platforms (Twitter/Reddit/Xiaohongshu) — handles your **session cookies** and explicitly **warns of account-ban risk (封号风险)**. That is a materially bigger footprint than the read-only/inspection tools.
- **Pilot fence (if attempted):**
  1. `install-snapshot` first; inspect the `agent-reach` PyPI package; **`npm-security-check`** the npm-distributed backend CLIs before they're pulled in.
  2. **Use disposable/throwaway accounts** for any cookie-based platform — never a primary Twitter/Reddit/Xiaohongshu account (the README says so for a reason).
  3. Verify the `600` permissions on `~/.agent-reach/config.yaml`; confirm no-upload.
  4. **Local-only** — skip the optional residential proxy.
  5. Run `--safe` / `--dry-run` first to see exactly what gets installed/configured; pin **v1.5.0**.
- **Ranking (updated):** the on-goal pilot ladder is now five rungs. **(1) SkillSpector v169** stays the lowest-risk *first* pilot (read-only, free). **(2) claude-tap v173** is the highest *value-per-risk* (local, pip, auto-redacting, code-read-only; on the cost + memory threads). **(3) Agent-Reach v174** is the strongest *capability* pilot (it adds a new ability rather than observing one) but sits behind a heavier fence — many backend CLIs + cookie/ban-risk — so pilot it after a low-risk loop-prover. **(4) codebase-memory-mcp v172** (read-only, but a compiled-binary `curl|bash` + 11-agent auto-config). **(5) devspace v171** (highest value + highest risk: remote read/write/execute/git via tunnel). The PILOT lever still formally stands (zero piloted).

## Suggested next action

Review + merge the `wiki/v174-agent-reach` branch (based on v173/`4085da9`, itself unmerged — merging v174 brings the v168→v174 cumulative state along). Then, on the standing PILOT lever, Agent-Reach is a strong *capability* rung: after a low-risk loop-prover (SkillSpector `--no-llm` over `05 Skills/`, then a throwaway Claude Code session through claude-tap), consider a fenced Agent-Reach pilot — **install in a scratch project with `--safe`/`--dry-run`, give the vault's Claude Code web reach for one real research task, using a disposable account for any cookie platform** — and watch whether free multi-platform reach changes the autopilot/research loop.
