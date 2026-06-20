# (C) claude-tap — LLM Wiki (v173)

> **Ship:** v173 · 2026-06-20 · branch `wiki/v173-claude-tap` off `wiki/v172-codebase-memory-mcp` (based at `1bf025c` = v172, which is itself unmerged — branching off `main` would orphan the v168→v172 cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** **1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1)** — *"Agent Protocol Inspector (local man-in-the-middle capture + trace-viewer of an AI coding agent's live API traffic, for debugging)."* The corpus's first wire-level man-in-the-middle proxy that **records + renders an agent's live API request/response payloads for inspection/debugging** (system prompts, tool schemas, conversation, SSE streams, token usage; structural request diffs; self-contained HTML viewer; 100% local). Distinct from the observability sub-archetype (different layer/object/purpose → adjacency cross-reference, **NOT** an instance, **NO** N-bump). Secondary scoped observations only (#84 84c provider-agnostic · #66 privacy cross-ref · #19 19a). NO new top-level pattern (max stays **#85**). Counts UNCHANGED (**46 / 10**); tracked PROVISIONAL §C surface ≈30 → ≈31 (+1 standalone).
> **Tier:** **T2 Service** (a self-hosted local developer tool you install + run alongside your agent; kin in *spirit* to the observability/metering tools v89/v109/v157 but a distinct wire-inspection shape).
> ✅ **On the goal-#1 substrate core** — third consecutive core-substrate ship after v171 devspace + v172 codebase-memory-mcp. claude-tap is dead-center on *"master Claude and autonomous agents for software development"*: it is the tool that lets you **see exactly what Claude Code (and 13 other agents) actually send to and receive from the model** — the system prompt, the tool schemas, the context, the token usage — at the protocol level.
>
> ⚠️ **(a) FAIL is genuine, not a downgrade.** "liaohch3" is a bare GitHub handle with no disclosed identity — not Anthropic, not a registered cultural-peer (a)-axis; a name/heritage guess is **not** an (a)-rescue (the v159→v172 discipline). The tier keys on **(b)**, which is STRONG → GOAL-ALIGNED regardless. The v169 cascade error ("(a) FAIL → OFF-GOAL") is explicitly guarded against. See §5.
>
> 🔬 **Verdict adversarially verified** (3 distinct lenses + an anti-inflation critic; the v172 model — each lens a different question to avoid the v169 shared-premise cascade). **All 3 lenses CONFIRMED (high confidence); cascade risk = zero (all three independently keyed the tier on (b), not (a)). The critic returned ONE AMEND only: rename the §C standalone to lead with the protocol-layer distinction (incorporated — the name below). Everything else CONFIRMED** — GOAL-ALIGNED INCLUDE 3/4, T2 Service, N=1 corpus-first, counts 46/10 unchanged, no double-count.

---

## 1. What it is

`liaohch3/claude-tap` — description, verbatim:

> *"a local proxy and trace viewer for AI coding agents"*

and the repo's one-line pitch:

> *"Intercept and inspect Coding Agent API traffic from Claude Code, Codex CLI, Gemini CLI, Cursor CLI, OpenCode, Kimi/Kimi Code, Pi, and Hermes in a local trace viewer."*

You **run your coding-agent CLI *through* claude-tap.** It sits in the middle as a proxy, forwards the traffic to the model provider unchanged, and **records every request/response pair** along the way — then renders them in a browser-based trace viewer. The README's framing of what you get to see:

> *"inspect the real API traffic and agent context: system prompts, conversation history, tool schemas, tool calls, streaming responses, token usage, and request diffs"*

The headline use is **debugging by evidence**, not monitoring:

> *"Debug behavior with evidence: compare adjacent requests and pinpoint which prompt, message, tool, or parameter changed."*

It is written in **Python (82.4%)** with a **JS/HTML/CSS (9.7% / 4.5% / 2.6%)** viewer, licensed **MIT**, latest **v0.1.120** (2026-06-18), with **100+ releases** and 9 contributors. Traces never leave the machine:

> *"Keep traces on your machine: no hosted dashboard is required, and common auth headers are redacted before recording."*

**Why this matters for the vault.** This is, in effect, *Charles Proxy / mitmproxy for coding agents* — the missing instrument for seeing what an agent like Claude Code actually does under the hood: the real system prompt it runs, the exact tool schemas it advertises, how the conversation is assembled turn-over-turn, and where the tokens (and money) go. That is squarely on goal #1 and directly on two of the operator's live pilot threads (claude-api-cost-optimization; CC-memory-systems / understanding agent internals).

## 2. What it captures + the viewer

**Captured per run** (the agent's real wire traffic): system prompts · conversation history · tool schemas (definitions) · tool calls + tool results · reconstructed streaming responses · token usage (input / output / cache) · request diffs.

**The viewer** (self-contained, local):

| Feature | What it does |
|---|---|
| **Structural diff** | *"compare consecutive requests to see exactly what changed: new/removed messages, system prompt diffs, character-level inline highlighting"* |
| **Full-text search** | search across messages, tools, and prompts |
| **Path filter** | filter by API endpoint |
| **Token-usage breakdown** | input / output / cache accounting |
| **Tool inspector** | tool definitions with parameter schemas |
| **Live viewer** | browser viewer on by default during a run |
| **Export** | a **self-contained HTML viewer** for review/archiving, or a **compact JSON/JSONL trace bundle** ("Share one portable artifact"); regenerate the HTML viewer from JSONL |
| **Polish** | dark/light themes · iframe embed mode · i18n (8 languages) |

The structural-diff-between-consecutive-requests feature is the distinctive one: it turns "the agent behaved differently" into "*this* message / system-prompt line / tool / parameter is what changed," with character-level highlighting.

## 3. How it works (architecture)

- **Proxy modes — reverse *or* forward, per client.** *Reverse* mode points base-URL-aware clients at the proxy (set the client's base URL to claude-tap). *Forward* mode uses proxy / CA-cert environment variables for clients that have no base-URL setting. This dual mode is what lets one tool tap 14 heterogeneous CLIs.
- **Low-overhead streaming.** *"SSE and WebSocket streams are forwarded as chunks/messages arrive with low proxy overhead"* — it does not buffer the whole response; it relays the stream and records it.
- **Local recording.** Each run writes a local trace session (JSONL); the viewer is generated on exit (or live during the run). No upload, no hosted backend.
- **Auth-header redaction.** Common auth headers are redacted **before** recording — so the stored/exported trace doesn't carry your API keys.

**Install / use.**
```
uv tool install claude-tap      # or: pip install claude-tap   (Python 3.11+)
claude-tap                      # defaults to Claude Code, live browser viewer
claude-tap --tap-client codex -- --model codex-mini-latest   # tap a different client; downstream flags after --
```
`--tap-client` selects the client to launch / listen to. Recognized client codes (14): `claude, agy, codex, codexapp, gemini, kimi, kimi-code, opencode, openclaw, pi, hermes, cursor, qoder, codebuddy` (`agy` = Antigravity).

## 4. The distinctive contribution (why it mints a §C standalone — CORPUS-FIRST)

The corpus has many tools that **watch an agent**, and a few that **sit in the traffic path** — but none that does what claude-tap does:

| Subject | What it does to the agent | Layer | Why it is NOT this |
|---|---|---|---|
| Observability sub-archetype — metering (v89 VibeCodingTracker, v109 cclog-cli, v157 ClaudeBar, v158 ai-token-monitor, v165 lazyagent) | reads usage **logs / session files**, displays **numbers/metrics** | logs/files | reports *how much*, not *what was sent on the wire* |
| Observability sub-archetype — ambient/affective (v154 agentpet, v155 openpets, v156, v164 oc-claw, v166) | reactive pet/avatar of **aggregate run-state** | hooks/state | shows *status*, not the protocol |
| Observability sub-archetype — attention (v160 ping-island) | routes **approval interrupts** | hooks | not capture |
| **headroom** (v144) | **intercepts the read-path** to **COMPRESS** what the agent reads pre-LLM (reversible CCR) | wire/proxy (one surface) | same place on the wire, **opposite purpose** — transform/shrink, not observe/record |
| **CodexPlusPlus / relay economy** (v117, LV-C2) | a proxy/relay that **REDIRECTS** traffic to alternate/cheaper endpoints | wire | redirect for cost, not inspect |
| **codebase-memory-mcp / codegraph** (v172 / v70) | MCP server the agent **queries** for code facts | MCP | augments the agent, doesn't observe its traffic |
| **claude-tap** (v173) | **records + renders the live API request/response payloads for inspection/debugging** | **wire/proxy** | — |

So claude-tap is the corpus's **first protocol-inspection proxy / trace-viewer**: a man-in-the-middle that **records the agent's actual API payloads and renders them for debugging** — at the **network-wire layer** (not logs/state/hooks), with the **raw protocol** as its object (system prompts, tool schemas, SSE streams — not metrics or run-state), for the **purpose of debugging/reverse-engineering** the agent's real behavior (not usage monitoring, not compression, not relay).

It does *touch* the observability family (you are, broadly, "watching the agent"), but classing it as an instance of the observability sub-archetype would be the **"generalize-the-definition-to-fit" error** the audits repeatedly warn against — it differs on all three axes (layer / object / purpose). It is recorded as an **adjacency cross-reference** to that sub-archetype, **not an instance**, so it does **not** bump the sub-archetype's N.

It is also genuinely distinct from the two nearest wire-layer neighbors: **headroom v144** sits in the same proxy position but **transforms** (compresses) rather than **records/inspects**; the **relay/reseller proxies** (v112 / v117) **redirect** for cost rather than **capture for inspection**.

**Standalone (the capability):**

> **"Agent Protocol Inspector (local man-in-the-middle capture + trace-viewer of an AI coding agent's live API traffic, for debugging)"** — records + renders live request/response payloads (system prompts / tool schemas / conversation / SSE / token-usage) for debugging; structural request diffs; self-contained HTML viewer; 100% local. *(Drafted as "API-Traffic Interceptor / Trace-Viewer (protocol-inspection proxy)"; renamed on the v173 critic AMEND to lead with the protocol-layer distinction — kept as a search alias.)* **CORPUS-FIRST, N=1.** PROMOTION-ELIGIBLE at N=2 (a 2nd protocol-inspection/trace-viewer proxy for coding agents). Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).

The fact that it taps **14 clients** is a separate axis (provider-agnostic distribution) handled as a scoped #84 84c observation (§6) — no double-count.

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** The author is **"liaohch3"** — a bare GitHub handle with **no disclosed individual identity, affiliation, or location.** It is not Anthropic and not any registered cultural-peer (a)-axis; the only major-vendor carve-out, **(a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only.** The contributor handles and the 8-language i18n hint at an East-Asian/Chinese-language origin, but a **name/heritage inference is explicitly NOT an (a)-rescue** (the v159→v172 discipline — held across v169/v170/v171/v172). **(a) FAILs cleanly; no rescue, no axis minted** — consistent with v168 ponytail (bare handle) and v172 DeusData (bare org).
- **(b) STRONG.** Goal #1 = *"master Claude and autonomous agents for software development."* claude-tap is the instrument for **seeing exactly how a coding agent actually works at the API/protocol level** — its real system prompt, its tool schemas, how it assembles context, and its token/cost footprint. It is **Claude-Code-first** (the default client), it directly serves **understanding agent internals** (cf. the v65 claude-code-system-prompts work + the system-prompts-leaks corpus subject — claude-tap is the *live-capture mechanism* those static collections lack), and its **token-usage breakdown** lands directly on the operator's **claude-api-cost-optimization** thread. It is **directly pilotable into the vault** (run the vault's own Claude Code sessions through it to see the real prompt/context/tool/token picture). Held at **STRONG (not STRONGEST)** because it is third-party (not the vault's own work / not an Anthropic substrate) and is an **inspection/observational augmentation** — it lets you *understand* the agent, it doesn't make the agent more capable. STRONGEST is reserved for Anthropic core substrate or the agent itself.
- **(c) STRONG.** A mature, real surface: a Python proxy + JS/HTML/CSS trace viewer; **dual reverse/forward proxy modes**; low-overhead SSE/WebSocket relay; auth-header redaction; **structural request diffing** with character-level highlighting; full-text search; token accounting; tool-schema inspector; HTML + JSON export; i18n (8 langs); **14 supported clients**; `pip`/`uv` install; **100+ releases** to v0.1.120; ~1.9k★/196 forks; 9 contributors. Not a prototype.
- **(d) STRONG.** A clean **§C capability standalone** (the protocol-inspection-proxy capability, CORPUS-FIRST N=1) with an unambiguous home and a clear adjacency map (observability family / headroom / relays). Nothing is forced.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is **STRONG** (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s FAIL does **not** make a (b)-STRONG subject off-goal — that was the v169 cascade error; the v173 verification gives each lens a distinct question precisely so they cannot share that false premise.

## 6. Pattern Library outcome

**PRIMARY — 1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1):**

> **"Agent Protocol Inspector (local man-in-the-middle capture + trace-viewer of an AI coding agent's live API traffic, for debugging)."**
> *(Renamed on the v173 critic AMEND from the drafted "API-Traffic Interceptor / Trace-Viewer (protocol-inspection proxy) for AI Coding Agents" — the new name leads with the protocol-layer distinction that justifies the mint over an observability-instance reading; the old name is retained as a search alias.)*
> Anchor: **claude-tap v173** (`liaohch3`). The corpus's first wire-level man-in-the-middle proxy that records + renders an agent's live API request/response payloads for inspection/debugging. **§28: 1 new standalone (≤2 cap honored). PROMOTION-ELIGIBLE at N=2** (a genuine 2nd protocol-inspection/trace-viewer proxy for coding agents). Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).

Distinct from the **observability sub-archetype** (adjacency cross-reference, **NO N-bump** — different layer/object/purpose; classing it as an instance would be the "generalize-to-fit" error) and from the wire-layer neighbors **headroom v144** (compresses) and the **relay/reseller proxies v112/v117** (redirect for cost). The standalone is the **capability**; the 14-client reach is a separate axis (below) → no double-count.

**SECONDARY observations (NOT minted):**

- **Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation (NO N-bump).** One proxy taps **14 heterogeneous agent CLIs** via dual reverse/forward modes. This is provider-agnostic by design — but it is a **scoped note, not an N-bump** (the v86 discipline: a single new count-increment / "most clients yet" is not by itself a CORPUS-RECORD mint). ⚠️ Explicitly **NOT** the ponytail "14-platform **native-rule-file** distribution" mechanism (the v169 contamination — do not repeat it): claude-tap distributes *nothing into* the clients; it is **one proxy that taps many CLIs**, a different mechanism. Also **NOT** Pattern #18 B1-MCP — claude-tap is a **proxy you run the CLI through, not an MCP server**, so the one-server-many-MCP-clients pattern does not apply.
- **Pattern #66 (supply-chain / security-conscious / privacy design) — cross-reference.** *"Keep traces on your machine"* + auth-header auto-redaction before recording + no hosted dashboard = a privacy-conscious posture for a tool that, by construction, sits in your API key path. Cross-referenced, **not** an N-bump of #66.
- **Pattern #19 sub-archetype 19a (founder/portfolio) — minimal data-point.** "liaohch3" is a bare handle with no disclosed individual or visible portfolio; a thin data-point of a CONFIRMED pattern, no new sub-mechanism.
- **LV-C4 (cadence micro-signal) — page-stated note only.** 100+ releases to v0.1.120 is a high release cadence, but the counts are page-stated, not API-verified (§37.4); logged as a cadence note, not advanced.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Max confirmed stays **#85**; the capability lives at the §C-standalone tier per §28 (the same anti-inflation that rejected #86/#88 at v168).
- **NOT an instance of the observability sub-archetype** (it does not READ+DISPLAY agent state/usage; it RECORDS+INSPECTS the wire protocol) — adjacency cross-reference only, NO N-bump.
- **NOT Pattern #52 (viral velocity).** ≈**1.9k★ / 196 forks / 100+ releases** (v0.1.120, 2026-06-18) are **page-stated, NOT API-verified** (§37.4 — this sandbox mocks the GitHub API). **No API-verified creation date → velocity unestablishable → explicitly not a #52 claim.**
- **NOT Pattern #57 (corpus-recursion).** The 14-client list includes corpus subjects (Claude Code, Codex, Gemini CLI, OpenCode ~ v67, OpenClaw ~ v164 oc-claw, Pi ~ pi-mono) — but it lists them as **clients it taps**, not as **source material / influences it cites.** Mentions ≠ recursion (the v171/v172 discipline). The **Phistory** relationship is a **downstream dependent** (Phistory uses claude-tap's export), not an upstream influence — also not #57.
- **NOT Pattern #18 B1-MCP** (proxy, not MCP server) and **NOT** the ponytail #84 "14-platform rule-file distribution" mechanism (different mechanism — taps clients, distributes nothing).
- **NOT a re-classification / new tier.** A clean §C capability standalone + scoped secondary notes — nothing more.

**Counts UNCHANGED: 46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL §C surface ≈30 → **≈31** (+1 standalone N=1).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** ≈**1.9k★ / 196 forks / 100+ releases** *(as of 2026-06-20 page render, github.com/liaohch3/claude-tap — confidence: stated, NOT API-verified)*. **MIT** license. Languages **Python 82.4% / JS 9.7% / HTML 4.5% / CSS 2.6% / Shell 0.8%** (page-stated). Latest release **v0.1.120, 2026-06-18** (page-stated).
- **No API-verified creation date** → age & velocity **unestablishable** → **explicitly NOT a Pattern #52 claim.**
- **Author identity:** "liaohch3" — a bare GitHub handle. **No disclosed individual, no stated affiliation/location** (confidence: stated — the *absence* of identity is what the repo page shows). East-Asian/Chinese-language origin is an **inference** from contributor handles + i18n (confidence: speculation) and is **immaterial** to the (a) FAIL (a bare handle FAILs (a) regardless; a heritage guess is not an (a)-rescue).
- **README contents** (§2 capture surface + viewer features, §3 proxy modes / streaming / redaction, the verbatim quotes, the 14-client list, the Phistory relationship) are page-verified from the rendered README + repo page at ship time. Performance characterizations ("low overhead") are vendor-stated, not independently reproduced.

## 8. Streak / state

- **Streak:** `GA:34 · OG:11 [7 ov]` → **`GA:35 · OG:11 [7 ov]`** (35th GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v171 GA, v172 GA, **v173 GA**} = **0 OG → STAYS CLEAR.** No ceiling-override needed or taken.
- **20 consecutive goal-aligned ships v153→v173.** v168/v169/v170 varied the domain off the v153→v166 operating/monitoring niche; **v171/v172 returned to the goal-#1 substrate core** (MCP infra), and **v173 stays on the core** — an agent-internals inspection tool (a distinct *protocol-inspection* shape, not the v153→v166 usage-monitoring niche).
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Max pattern #85. PROVISIONAL §C surface ≈30 → ≈31.
- **Override-frequency triggers (2-in-20 / 3-in-30):** v153→v173 = **zero** operator overrides (clean).
- **Build note:** verdict produced **inline**, then **adversarially verified by a 3-lens + critic workflow** (each lens a distinct question — goal-relevance/tier · capability-novelty/placement · secondary-claims/non-claims — to avoid the v169 shared-premise cascade). **Result: all 3 lenses CONFIRM (high confidence); the critic's `cascade_check` = "CASCADE RISK = ZERO" (all three independently keyed the tier on (b), not (a)); `inflation_check` = discipline HELD (mint warranted, N=1 correct, counts 46/10 unchanged, no double-count). The critic returned `overall: AMEND` on ONE point only — rename the §C standalone to lead with the protocol-layer distinction — incorporated above.** The critic's final verdict line restates: GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG; T2 Service; streak GA:34→GA:35; §35 clear; 20 consecutive goal-aligned ships v153→v173.

## 9. Pilot note

claude-tap is one of the **strongest and lowest-risk pilot candidates the corpus has surfaced** — arguably the best on-thread / risk ratio to date.

- **Why high-value & on-thread:** running the vault's own Claude Code sessions through claude-tap shows the **real system prompt, the real tool schemas, the real context assembly, and the real token/cache breakdown** of the operator's own agent work. That lands directly on **two live pilot threads at once**: **claude-api-cost-optimization** (the token-usage breakdown is exactly the metering the hireui cost spec wants) and **CC-memory-systems / understanding-agent-internals** (seeing how context is actually built per turn). It is also useful for the **multi-agent-orchestration** thread (inspect what each agent sends) and pairs naturally with the v65 claude-code-system-prompts work (claude-tap is the live-capture mechanism behind those static prompt collections — exactly what Phistory does with it).
- **Why low-risk:** it is **100% local** (no hosted dashboard, no upload), it **auto-redacts auth headers before recording** (exported traces don't carry your keys), it is **read-only with respect to your code** (it inspects traffic, it doesn't write files or execute), and it installs as a plain **Python package** (`pip`/`uv`) — no compiled-binary `curl|bash` (v172) and no remote read/write/execute bridge (v171).
- **The one real caveat:** it is a **man-in-the-middle proxy** — by design it sits in your API request path and *sees* your traffic (including auth, pre-redaction). That is a smaller blast radius than devspace's execute-bridge or a system-wide compiled binary, but it is not nothing: a proxy in the key path warrants the usual care.
- **Pilot fence (if attempted):**
  1. `install-snapshot` first; run **npm-security-check**'s PyPI analogue / inspect the package before `pip install` (single-author handle, but MIT + 100+ releases + 9 contributors are reassuring signals).
  2. Pilot against a **scratch project / a single throwaway Claude Code session** first, not the vault, to see what a trace contains.
  3. Confirm the **auth-header redaction** actually scrubbed the exported trace before sharing any artifact.
  4. Pin **v0.1.120**.
- **Ranking (updated):** **SkillSpector (v169) remains the lowest-risk *first* pilot** (read-only Python scanner, no request-path involvement). **claude-tap (v173) is the highest *value-per-risk* pilot** — low-risk (local, pip-installed, auto-redacting, code-read-only) *and* directly on the cost + memory threads — strong candidate for the **second** pilot, ahead of codebase-memory-mcp v172 (heavier compiled-binary install) and well ahead of devspace v171 (highest value + highest risk). The PILOT lever still formally stands (zero piloted).

## Suggested next action

Review + merge the `wiki/v173-claude-tap` branch (based on v172/`1bf025c`, itself unmerged — merging v173 brings the v168→v173 cumulative state along). Then the highest-value open move is the **standing PILOT lever**, and claude-tap is now the cleanest second rung on it: pilot **SkillSpector `--no-llm` over `05 Skills/`** first (lowest-risk loop-proof), then **run a throwaway Claude Code session through claude-tap** to capture the vault agent's real system prompt + tool schemas + token breakdown (directly on the cost + memory threads, behind the §9 fence), keeping **codebase-memory-mcp** and **devspace LOCAL-ONLY** as the heavier-install / higher-risk follow-ups.
