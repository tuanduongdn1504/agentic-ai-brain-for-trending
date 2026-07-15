# (C) awesome-llm-apps — Verdict (LLM Wiki v201)

**Subject:** `Shubhamsaboo/awesome-llm-apps` — a multi-framework, multi-model gallery of ~129 full runnable LLM/agent/RAG/MCP apps. Apache-2.0; ~121k★ (page-stated §37.4). Author **Shubham Saboo** (AI DevRel/educator; Unwind AI; Tenstorrent/Google; **NOT Anthropic**). Source captured 2026-07-15.

## Phase 0.9 STRICT (routine v2.6 §31) — GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Reasoning |
|---|---|---|
| **(a) authorship / Anthropic tie** | **FAIL** | Shubham Saboo = a notable individual AI DevRel/educator/author (Tenstorrent Head-of-DevRel and/or Google Sr-AI-PM; ex-Unwind-AI; 3× AI author), **not Anthropic**; "notable author/educator" is **not a registered cultural-peer (a) axis** (the Addy Osmani v184 / Evan Bacon v183 situation — a disclosed prominent builder *reinforces-not-reopens* the disclosed-builder (a)-axis held operator-reviewable at N=3 per v182). #19 19a first `Shubhamsaboo` author. No (a)-rescue. |
| **(b) goal-relevance** | **STRONG (keys the tier)** | A huge library of **runnable Claude-supported agent / RAG / MCP / multi-agent / memory apps + an explicitly Claude-Code-first Agent-Skills sub-section (`npx skills add`) + framework crash courses** = dead-center on Goal #1 ("master Claude and autonomous agents for software development") as **learn-by-example + build-from-template** material, and **directly pilotable** (clone a RAG/MCP/multi-agent pattern → adapt into hireui). **STRONG-not-STRONGEST** because: (i) it's a third-party *learning/example collection* you borrow from, not the vault's own substrate; (ii) **Claude is one-of-many models and often not the default** — the gallery skews OpenAI/Gemini (4-app hand-sample = 0 Claude-default; 2/6 MCP agents support Claude), the Agent-Skills sub-section being the Claude-first exception; (iii) the hard engineering is upstream in the frameworks it demonstrates. Still clearly STRONG — arguably the strongest-relevance awesome-collection the corpus has had (contrast v170's MODERATE links-only field-map). GOAL-ALIGNED per §31 (keyed on (b), not (a)). |
| **(c) technical substance** | **STRONG (w/ honest caveats)** | ~129 full runnable apps across 15 categories, multi-framework (LangChain/LangGraph, CrewAI, Agno, AG2, OpenAI Agents SDK, Google ADK, browser-use, Firecrawl, EvoAgentX, Mem0, Streamlit, Chroma/Qdrant, Ollama), multi-model (7 providers), Apache-2.0, ~1,080 commits, weekly-updated, clean repo-level supply-chain. **Caveats:** each app = a thin, mostly-Streamlit-demo-grade wrapper (3–4 files) around a framework — the hard AI is upstream; quality/maintenance is uneven across contributor-sourced apps; 0 releases (collection-first); Streamlit-key-in-UI + opaque `npx skills add` governance are real trial risks; the Unwind AI newsletter is a funnel. |
| **(d) cross-references** | **STRONG** | Pattern #68 awesome-genre (v8/v25/v31/v50/v170) · v102 claude-cookbooks (the cookbook precedent) · the agentskills.io ecosystem (vercel-labs v51 `npx skills add` + agent-skills-standard v76 / anthropics-skills v93 / agent-skills v184) · MCP family · **it demonstrates corpus subjects `headroom` v144 + `browser-use` v41 as example content** (Pattern #57 57b-style aggregator-mediated) · education/learn-by-example cluster (v6/v39/v74/v191/v197) · agent-app shapes career-ops v200 / OpenMontage v188. |

**Verdict: GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG].**

## Pattern outcome: **NO MINT (primary)** — Pattern #68 (Awesome-List-Genre) instance-strengthening; §C-standalone MINT recorded as the operator/audit-reviewable ALTERNATIVE

**The central judgment (hand-made):** awesome-llm-apps is a **curated collection of runnable example apps** — an aggregation / learn-by-example / reference artifact, **not a tool or capability**. The corpus draws a consistent categorical line:

- **§C standalones are minted for tools/capabilities** — where *your* agent/workflow gains a new ability or *the agent IS the runtime* (fff v194 search library; openwiki v195 doc-authoring agent; page-agent v199 in-page GUI agent; career-ops v200 operational pipeline; agency-agents v185 persona library you install; loop-engineering v189 kit + CLIs you run).
- **Curated collections / cookbooks / galleries / curricula are NOT minted — they strengthen an existing genre/tier:** **v102 claude-cookbooks** (a recipe/example collection → NO §C, filed as a vendor cluster), **v170 awesome-artificial-intelligence** (Pattern #68 instance-strengthening, NO mint), **v50/v31/v25/v8** awesome-lists (Pattern #68), **v191/v196/v197** (education/domain, NO mint).

awesome-llm-apps is squarely in the second class: you **browse it and clone individual apps**; you do not "install awesome-llm-apps and gain a capability." It borrows the "awesome-" name and the curated-collection spirit of **Pattern #68 (CONFIRMED v31)** — and **Pattern #68 already carries a code-bundling form-factor sub-variant** (v50 awesome-claude-skills = "hybrid aggregator with bundled in-repo skills"). awesome-llm-apps extends that to a **fully-code-carrying / runnable-app-gallery form-factor sub-variant** → **clean Pattern #68 instance-strengthening** (the v170 handling), with strong **T3-Education learn-by-example** character (framework crash courses + reference apps).

**§C-standalone MINT — recorded, operator/audit-reviewable ALTERNATIVE:** "Curated Multi-Framework, Multi-Model Runnable LLM/Agent-Application Gallery (organized by capability category)" N=1, **corpus-first-for-surface + landscape-confirmed world-canonical/largest, NOT world-first**. This is a *genuinely defensible* alternative — the landscape research confirms no direct corpus precedent (v102 is single-vendor notebooks; Pattern #68 members are links-lists) and no direct world peer at this breadth — and it would follow the agency-agents-v185 / loop-engineering-v189 "mint the corpus-first world-class exemplar of a distinct recurring class" precedent. **It loses to NO-MINT** because awesome-llm-apps introduces a new **form-factor** (runnable apps) *within an existing genre* (curated collection), not a new **primitive** (v185's subagent-vs-skill was a real primitive boundary; career-ops v200 the-agent-IS-the-runtime was a real capability boundary) — and because the v102-cookbook / v170-awesome-list / curricula NO-MINT discipline is directly on point. **Either reading: counts UNCHANGED 46/11; §C surface UNCHANGED ≈47 (40 live standalones).** Flag both to the badly-overdue ~v192 audit.

### Secondary observations (NOT minted)
- **#19 19a** first `Shubhamsaboo` author (individual AI DevRel/educator).
- **Pattern #68 form-factor sub-variant** "runnable-full-app-carrying awesome-collection" (extends v50's code-bundling) — recorded within #68; whether it's a *named* sub-variant → the ~v192 audit.
- **agentskills.io ecosystem cross-ref** — the Agent-Skills sub-section uses `npx skills add` (vercel-labs v51 verb); Claude-Code-first + a claimed security+eval CI gate. Data-point, **NO N-bump**.
- **Pattern #57 57b-style aggregator-mediated data-point** — the gallery demonstrates corpus subjects `headroom` v144 + `browser-use` v41 as example content (the v50 shape; NOT a promotion, the subject demonstrates rather than cites-as-influence).
- **#84 84c ADJACENCY** — multi-model/multi-framework by design, but that's *pedagogical variety*, NOT provider-agnostic *distribution* → **NO N-bump**.
- **#22 AGENTS.md-absence** — genre-consistent (the 4/4 awesome-genre absence pattern); no AGENTS.md/contribution-section surfaced.
- **#50 companion-funnel family** — the Unwind AI newsletter tie-in ("new templates drop weekly, get them in your inbox"); data-point.
- **#66 supply-chain** — repo-level BENIGN (no curl|bash/postinstall/telemetry, Apache-2.0); per-app risks = Streamlit-key-in-UI + unpinned per-app deps + opaque `npx skills add` governance + typosquat-fork risk. Fence = scratch venv per app + `.env` keys + `npm-security-check` any skill + clone from the author URL only.

### NON-claims
NOT a new top-level pattern (max #85) · **NOT a §C mint** (the mint is the DECLINED alternative) · NOT #52 (121k★/0-releases page-stated §37.4; "55k" search-cache stale; "#1 trending / 1,300★-in-24h" search-stated → velocity unestablishable) · NOT #57 promotion (aggregator-mediated *demonstration*, not influence-citation) · NOT #18 B1-MCP (it *contains* MCP example apps; it is not itself an MCP server) · NOT corpus-first-as-a-mint · NOT Claude-centric (Claude one-of-many, OpenAI-leaning defaults).

## Counts / streak / §35
- Counts **UNCHANGED: 46 confirmed patterns / 11 CONFIRMED Library-vocab.** §C live standalones **UNCHANGED (40).** Tracked PROVISIONAL surface **UNCHANGED ≈47.**
- Streak **GA:61 → GA:62** (48 consecutive goal-aligned ships v153→v201; "49+3\*" frozen @v125).
- **§35 CLEAR** — rolling-3-ship window {v199 GA, v200 GA, **v201 GA**} = 0 OG. Override-frequency 2-in-20 / 3-in-30: v153→v201 = zero operator overrides.

## Tier
**Pattern #68 Awesome-List-Genre (code-carrying / runnable-app-gallery form-factor variant) × T3-Education learn-by-example reference gallery.** GOAL-ALIGNED (unlike the prior link-list #68 instances which were OUTSIDE-SCOPE, because (b) is STRONG here, not MODERATE).

## Confabulations / over-claims caught + corrected (all workflow agents ran on Haiku — elevated risk)
1. **Employer flip** — `web:identity` said "Google current / Tenstorrent prior"; my own hand-WebSearch said the reverse. Sources genuinely conflict (both org-charts exist). **Presented as ambiguous; the load-bearing NOT-Anthropic fact holds either way.**
2. **Stale "55k★"** (identity agent's reputation line) vs live **121k** (metrics agent + my WebFetch). **121k page-stated used.**
3. **"`npx skills add <url>` is non-standard / not agentskills.io"** (`src:agent-skills-mcp`) — Haiku over-interpretation. **Corrected:** it IS the agentskills.io ecosystem verb (vercel-labs v51), used with a GitHub URL.
4. **"Zero Claude in the whole repo"** (`src:sample-apps`) — a 4-app sample, over-generalized. **Scoped:** Claude is a *supported option, not the default*; the README + MCP section confirm some apps use Claude (e.g. `multi_mcp_agent_router` primary); the gallery skews OpenAI/Gemini.
5. **`src:frameworks-models` failed** ("prompt too long") — hand-covered the framework/model inventory from the README + sample apps.

**inflation_check = HELD** (0 mints; the corpus-first-for-surface §C mint DECLINED as the reviewable alternative per the v102/v170 discipline; max #85; counts 46/11 unchanged; no N-bumps on #84/#57/#68; §28 anti-inflation honored).
