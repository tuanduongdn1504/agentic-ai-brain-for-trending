# (C) v180 — Verdict + Collision Record

**Subject:** `badpaybad/a.i-assistant-chatbot-telegram-serverles` · author **Nguyen Phan Du** (`badpaybad`, commits `dunp`) · MIT · 6★/2 forks · source-verified at commit `4070f21`.
**Date:** 2026-06-22 · **Routine:** LLM Wiki Routine v2.6 · **Verification:** produced **inline** + verified by hand (clone + source greps; collision grep over `_state/` + `_patterns/`; 1× WebSearch author identity) per `feedback_wiki_verify_independently_check_collisions` (the multi-agent workflow confabulates corpus facts — not used).

---

## Verdict: GOAL-ALIGNED INCLUDE 3/4 · NO MINT · counts 46/10 UNCHANGED

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** Anthropic / cultural-peer | **FAIL** | Author = an individual Vietnamese developer (Nguyen Phan Du), not Anthropic ((a)-7 is Anthropic-only). **Disclosed indie builder** (named, ~150 repos) → the **v171 devspace / v174 Agent-Reach situation**, NOT a bare handle. ⚠️ **Operator-reviewable:** the Vietnamese-first README + the operator's own VN locale touch the **v78 "(a) PASS via product-locale-inclusion"** precedent — but the **v159→v179 strict discipline (standing rec ii)** says do **not** (a)-rescue on a locale/heritage inference. Logged operator-reviewable, **NOT relied upon**; the tier keys on (b) regardless (§31). |
| **(b)** Goal-relevance (keys the tier) | **MODERATE** | It **is** an autonomous-agent framework for personal/dev tasks (CLI exec, browser/GUI automation, a code skill, a spec-first dev methodology, tool-calls, FAISS memory) = dead-center on Goal #1's *class*. Held **below STRONG** by: **Gemini-bound** implementation (not Claude; local path = a gemma4 gemini-compat server, not Claude); **messy/personal/early** (6★, single author, kitchen-sink, `todo` stubs); **low pilotability** into the vault (Ubuntu + Telegram + Gemini-protocol). Calibrates **at/just-above GLM-5 v176's (b) MODERATE** — GLM-5 = a raw competitor model; this = a full competitor-LLM agent *framework* (a notch more applicable, still not Claude-centric). **(b) MODERATE+ → GOAL-ALIGNED** under §31. |
| **(c)** Engineering substance | **MODERATE** | A real, working core: FastAPI webhook server + Cloudflare-tunnel bootstrap + dynamic skill orchestration + FAISS long-term memory (gemini/fasttext embeddings) + SQLite + rolling summarization + Telegram/Discord/Telethon transports + a local Gemma-4 gemini-compatible server + cli/browser/jira/drive skills. **Honest caveats:** headline 20K-Py/435K-JS totals are **inflated by the vendored `TreeOfThought/` sub-project** (~431K JS, a separate face-recognition full-stack app) + `cnc`/`games`/`cameraip` — the **actual core ≈ 8.2K Py**; the `gemini_dynamic` tool-call loop is a `todo` stub; "multi-LLM" is Gemini-protocol + API-compat, not an abstraction; 6★. |
| **(d)** Cross-references / pattern fit | **STRONG** | Rich: self-contained-agent family (OpenHuman v118 / PilotDeck v175 / AutoGPT / ECC v1 / OpenHands v30); spec-first methodology (cc-sdd v61 / spec-kit v17 / OpenSpec / bundled BMAD); #84 84c rule-file copies; #12 LLM-routing artifacts; #66 dual-use; vector-memory (agentmemory v66 / supermemory v132); browser/scrape (browser-use v34 / crawl4ai v29); group-aggregation + telegram-push (TrendRadar). |

---

## Pattern outcome: NO MINT (the GLM-5 v176 / camofox-declined-mint discipline)

**No new top-level pattern (max #85). No new §C standalone. Counts UNCHANGED 46/10. §C surface stays ≈36.**

The candidate corpus-first facet was: **"a consumer chat app (Telegram) as the *complete* control surface for a self-hosted, serverless personal PC agent."** Why it is **recorded as a DEFERRED candidate axis, not minted at N=1:**

1. **Weak substance for a corpus-first anchor.** Minting CORPUS-FIRST on a **6★, single-author, Gemini-bound, kitchen-sink** repo would be inflation. The Kilo-Code-v177 precedent (mint N=1 for a recurring world-class) applies to *the major exemplar of a class* — this is a **minor, weak instance** of the class, not its exemplar.
2. **The distinctive facet is a delivery/UI choice, not a new capability.** The agent capabilities (CLI exec, browser automation, skills, memory) all have corpus precedent; "fronted by Telegram, serverless via tunnel" is a *packaging* choice. Minting on packaging is the **"draw the circle to make it first"** move the routine explicitly declines (cf. camofox v179's *declined* separate "anti-detect browser AS agent server" mint).
3. **Heavy family overlap.** It sits squarely in the **self-contained-agentic-framework/assistant** family (OpenHuman v118 "general agentic desktop assistant"; PilotDeck v175 §C#83 self-contained agent OS; AutoGPT). The frontend differs; the *kind* does not.
4. **The world-class is real but unrepresented by a strong instance.** WebSearch confirms the "self-hosted personal AI agent fronted by a consumer chat app, runs on your own machine" class recurs (QwenPaw [agentscope-ai], opencode-telegram-bot, AI-Telegram-Assistant) — **none are corpus subjects.** Disciplined call: **record the axis as a watch/DEFERRED candidate**; mint if/when a *stronger, cleaner* instance ships (then this becomes a credited prior data-point), per §28 anti-inflation + the §35 ceiling.

**Recorded as:** a **corpus-knowledge data-point** in the self-contained-agentic-framework family + a **DEFERRED candidate axis** ("consumer-chat-app-as-complete-agent-frontend / serverless-PC personal agent"), promotion-eligible on a cleaner 2nd/exemplar instance.

### SECONDARY (NOT minted)
- **#19 19a** — first **Nguyen Phan Du / badpaybad** author; thin institutional/portfolio data-point.
- **#84 84c** — the 4 byte-identical `.clinerules`/`.cursorrules`/`.geminirules`/`.windsurfrules` = a small **84c.1 drift-(un)validated repo-copies** data-point (**4 copies, not 14**; no drift-checker — weaker than ponytail v168's hybrid; **NO N-bump**).
- **#12 LLM-routing artifacts** — rule files + skill `readme.md`/`system_instruction.md` + `.agent/tot-dev.md` = a routing-artifacts instance (NO N-bump).
- **#66 supply-chain / dual-use** — NL→bash exec, Telethon group ingestion, GUI/browser automation, public tunnel, plaintext `config.py` secrets (see wiki §7). A genuine attack/abuse surface; pilot fence required.
- **Spec-first methodology cross-ref** — `tot-dev` (`whattodo.md → howtodo.md → code`) + bundled BMAD = cross-ref to cc-sdd v61 / spec-kit v17 / OpenSpec (NOT a new instance; recorded).
- **Skill-as-self-generating-prompt** — several skills' `.md` is a meta-prompt that generates the skill `.py` (N=1 feature; interesting; recorded, not minted).
- **Local-LLM-via-API-compatibility** — `gemma4/` re-implements Gemini `v1beta` so the gemini client runs local (a feature, not a pattern).

### NON-claims (explicitly)
- **NOT** corpus-first as a Telegram/agent subject — but **no prior telegram-fronted agent subject exists** (tight grep empty); the NO-MINT is on *substance + packaging-not-capability*, not on a collision.
- **NOT #52** (6★/2 forks page-stated, §37.4 → velocity unestablishable; also: tiny).
- **NOT #57** (bundles BMAD / references cline/cursor/gemini/windsurf harnesses as *rule-file targets*, cites no corpus subjects as influences; mentions ≠ recursion).
- **NOT #18 B1-MCP** (not an MCP server; FastAPI webhook + skills).
- **NOT** an N=2 of any existing §C standalone (OpenHuman anchors no standalone; PilotDeck §C#83 is a different organizing primitive — WorkSpace isolation + white-box memory; this has neither).

---

## Collision record (independent grep — `feedback_wiki_verify_independently_check_collisions`)

| Check | Method | Result |
|---|---|---|
| Prior telegram-**fronted agent** subject? | tight grep `_state/03c,05` + `_patterns/06` for "telegram as / chat-app-as / telegram-controlled / via telegram chat" | **EMPTY** — none. (Telegram appears only as a *push channel* in other subjects, e.g. TrendRadar's 9 channels.) |
| §C standalone for self-contained framework / agent-OS / telegram? | read full §C registry (`_patterns/06`, §A+§C, all 86 entries) | Closest = **#83 PilotDeck** (WorkSpace isolation + white-box memory — different primitive) + OpenHuman v118 (anchors **no** standalone). No telegram/serverless-PC-agent standalone. |
| ECC v1 collision? | grep `_state/05` | ECC v1 = a **feature-framework methodology** (T1 methodology battlefield), not a telegram agent. No collision. |
| Author identity | WebSearch | **badpaybad = Nguyen Phan Du**, Vietnamese developer, ~150 repos — disclosed indie builder (not a bare handle). |
| Is the chat-app-frontend class a real world-pattern? | WebSearch | **Yes** (QwenPaw / opencode-telegram-bot / AI-Telegram-Assistant) — recurring, none in corpus → supports "DEFERRED axis," not a 6★ corpus-first mint. |

**inflation_check:** discipline HELD — 0 mints, max pattern #85, counts 46/10 unchanged, no §C surface change, no double-count, no generalize-to-fit. Tier **T2 Service** (self-hosted personal agent framework; same tier as PilotDeck v175 / OpenHuman-family).

---

## Streak & ceiling
- **GOAL-ALIGNED (GA)** → streak **GA:41 → GA:42** (`GA:42 · OG:11 [7 ov]`; under the GLM-5-v176-OFF-GOAL reading → GA:41·OG:12).
- **§35 CLEAR** — rolling-3 window {v178 GA, v179 GA, **v180 GA**} = 0 OFF-GOAL ≤ 1.
- **27 consecutive goal-aligned ships v153→v180** (GA reading).

## Pilot note
On-goal *class* but a **poor pilot target**: Ubuntu-only, Gemini-bound, NL→bash exec, reads all your Telegram groups, kitchen-sink. Far below the clean read-only pilots (SkillSpector v169 / claude-tap v173). If ever piloted: scratch VM + throwaway bot/key + local gemma4 + never a real account. Recorded; not recommended ahead of the existing ladder.
