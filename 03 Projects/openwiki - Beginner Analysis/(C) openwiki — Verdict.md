# (C) openwiki — Verdict (INLINE + hand-verified)

> **v195 · `langchain-ai/openwiki` · GOAL-ALIGNED INCLUDE 3/4 · 1 NEW §C standalone (N=1, corpus-first for the surface) · counts UNCHANGED 46/11 · Tier T2 Service.**
>
> Verdict produced **inline + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. A 6-agent read-only research workflow (`wf_9a67c696-fc0`; ~977K subagent-tokens; 73 tool-uses; **0 errors / 0 empty / all agents toolCalls>0** — the v191 zero-tool-call-confabulation lesson applied and held) did source-reading + upstream/landscape/security research ONLY. **Every corpus / collision / identity / tier claim below was verified BY HAND** (collision grep of `_state/` + `_patterns/` + `03 Projects/`; registry format + counts read directly from `_patterns/06`; identity + launch corroborated by my own WebSearch of the LangChain blog + X post; source hand-read at commit `58b4bd3`).

---

## Phase 0.9 STRICT (routine v2.6 §31 — the tier keys on (b), not (a))

### (a) FAIL — cleanly
LangChain, Inc. is a **declared-non-Anthropic institution** (a major US AI-infra company, ~$1.25B valuation), not Anthropic; (a)-7 is Anthropic-only. Matches the declared-non-Anthropic-institution line: Google v140 / ByteDance v143 / NVIDIA v169 / Zhipu-GLM-5 v176 / Microsoft-SkillOpt v178 / DeepSeek v186 / google-research v193. **FIRST `langchain-ai` ORG subject in the corpus** → a **#19 19a** returning-institution data-point (LangChain-the-*framework* appeared as a referenced dependency in claude-context v40; **Lance Martin (LangChain)** appeared as a Pattern #19 methodology-influence node in aidevops v47 — but no `langchain-ai` *org repo* has been a subject). No heritage rescue.

### (b) STRONG — keys the tier
This is dead-center on **Goal #1** and lands on **four live pilot threads at once**:
- It is an **autonomous documentation AGENT** built on **DeepAgents** (a Claude-Code-style harness) that produces the exact artifact class this vault studies — agent-consumable knowledge docs + **`AGENTS.md`/`CLAUDE.md`** instruction files.
- Claude is a **first-class provider** (native `ChatAnthropic` + via OpenRouter).
- It is a **productized, code-scoped version of THIS VAULT'S OWN founding pattern** — an LLM that incrementally writes + maintains a wiki (Karpathy LLM-Wiki). No prior corpus subject has been this close a mirror of the vault's own reason-for-being.
- Threads: **CC-memory-systems** (agent docs = an L-level knowledge layer), **#12/#22 AGENTS.md/CLAUDE.md** (it generates + maintains them), **loop-engineering v189** (the daily human-gated CI-PR update loop), **claude-api-cost-optimization** (multi-provider, defaults to cheap GLM 5.2 for the bulk pass).
- **Directly + safely pilotable** into BOTH the vault (borrow the doc-agent system-prompt discipline; run it on the vault's own code) AND **hireui** (run it on the monorepo → agent docs + `AGENTS.md`, feeding the GitNexus-first / Candidate-Detail context problem).

**STRONG-not-STRONGEST:** third-party + Claude is *one of several* providers (the out-of-box default is GLM 5.2, not Claude) + it is a *capability augmentation* (it writes docs) rather than the agent substrate itself. ⚠️ **Operator-reviewable:** the vault-parallel is uniquely strong here — a STRONGEST reading is defensible on the "it is literally a productized version of the vault's core pattern" ground. Held at STRONG per discipline; recorded.

### (c) STRONG — with honest caveats
A real, well-engineered documentation agent: DeepAgents `LocalShellBackend` + LangGraph `SqliteSaver` checkpointing (resumable threads) + a 5-provider abstraction with OpenRouter 5xx-fallback routing + git-evidence collection + a **content-snapshot SHA-256 no-op guard** (anti-CI-churn) + an Ink terminal UI + a genuinely sophisticated **~130-line system-prompt doctrine** + the `AGENTS.md`/`CLAUDE.md`-append feature + a scheduled-CI-PR example. **Caveats (foregrounded):** v0.0.1 / ~3 days old / 0 GitHub releases; **30 tracked files — a thin layer** whose hard agent-harness engineering is UPSTREAM in `deepagents` + LangGraph; **no test suite**; output quality proven only on its own small clean repo (no benchmarks vs Swimm/Komment/DeepWiki; multi-language coverage undocumented).

### (d) STRONG — dense connectivity
**Agent-code-context family** (§C#23 code-knowledge-graph graphify v16 / GitNexus v33 / codegraph v70 / codebase-memory-mcp v172 + claude-context v40 vector + **fff v194** lexical — OpenWiki = the *documentation-authoring* member of this family) + **AGENTS.md/#12/#22 thread** (aidevops v47 22c + the vault's own publishing strategy) + **loop-engineering v189** (scheduled human-gated CI loop) + **#84 84c** multi-provider + **GLM-5 v176** (the default model!) + **Lance Martin (LangChain)** (aidevops v47 influence node) + a genuine **meta-parallel to the vault's own LLM-Wiki pattern** (NOT a citation).

**Result: GOAL-ALIGNED INCLUDE 3/4** [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG].

---

## Collision check (BY HAND — decisive)

Grep over `_state/` + `_patterns/` + `03 Projects/` for: `openwiki` / `open-wiki` / `langchain` / `langsmith` / `deepwiki` / `agent documentation` / `AGENTS.md` / `documentation generator` / `auto-doc` / `autodoc` / `wiki for your codebase`:

- **`openwiki` / `open-wiki` / "wiki for your codebase" / "documentation generator" / "auto-doc" → ZERO hits.** No prior subject of this kind.
- **`langchain` →** appears only as (1) a *referenced framework/dependency* (claude-context v40 uses LangChain's char-splitter fallback), (2) **Lance Martin (LangChain)** as a Pattern #19 influence node (aidevops v47), (3) LangChain listed in ecosystem catalogs. **No `langchain-ai` ORG has ever been a subject → OpenWiki is the first.**
- **`langsmith` → ZERO hits.**
- **`deepwiki` →** appears only as an *external MCP/AI-docs integration* used by other subjects (claude-context v40 FAQ, claude-code-best-practice v34) — **a landscape peer, never a corpus subject.**
- **`agent documentation` / `AGENTS.md` →** Pattern #12 (corporate projects formalize agent docs) + Pattern #22 (AGENTS.md industry standard) + the vault's own publishing strategy. OpenWiki is the first subject that **auto-generates + maintains** these files (a facet of the mint, below).

**Boundary confirmation (hand-verified against `_patterns/06`):**
- **§C#23 "Pre-Indexed Read-Only Code Knowledge-Graph Queried via MCP"** (N=4: v16/v33/v70/v172, CONFIRMED Library-vocab #23) — INDEXES code into a **queryable graph/DB**. OpenWiki AUTHORS + maintains **human/agent-readable prose Markdown**. Different mechanism, different output.
- **v94 Understand-Anything** = a "multi-agent **codebase-knowledge-graph** tool" (adjacent to §C#23) — a knowledge graph, **not a prose-doc generator**. Distinct.
- **claude-context v40** = vector/embedding search. **fff v194** = lexical/fuzzy search. Neither authors docs.
- **book-to-skill v137 / SkillOpt v178** = author/optimize SKILLS, not codebase docs.

**Conclusion:** collision-clean; OpenWiki occupies an unrepresented surface.

---

## Pattern outcome

### 1 NEW §C standalone — N=1, CORPUS-FIRST for the surface

> **"Agent-First Codebase-Documentation Generator/Maintainer** — an autonomous agent/CLI that **authors and continuously maintains an agent-readable prose wiki inside your repo** and **wires it into the `AGENTS.md`/`CLAUDE.md` instruction files**, refreshed via a **git-diff-scoped, human-gated CI loop**; multi-provider, self-hosted."

**The defining CONJUNCTION** (no single facet is the claim; the intersection is): (an agent AUTHORS + MAINTAINS prose docs) × (agent-**FIRST** — docs built for future coding agents to consume) × (writes **INTO your repo** + updates the instruction files) × (continuous **git-diff-scoped maintenance** via a scheduled **human-gated CI PR** + a content-snapshot no-op guard) × (multi-provider, self-hosted CLI).

**Distinct** (mechanism + output) from every neighbor: §C#23 code-knowledge-graph (indexes → queries a graph) · claude-context v40 (vector) · fff v194 (lexical) · v94 Understand-Anything (knowledge graph) · book-to-skill v137 / SkillOpt v178 (skills).

**Scope honestly bounded: corpus-first for the surface, NOT world-first.** DeepWiki (Cognition/Devin, hosted SaaS), Context7 (Upstash MCP, public libs), Mintlify, Swimm (static-analysis-first), Komment (delta SaaS), GitBook AI all precede on *individual* axes. OpenWiki is differentiated on the **4-pillar conjunction** above (the research's "world-first at the intersection" claim = my "corpus-first for the surface, differentiated on the conjunction"). Mint at N=1 per the **fff v194 / serve-sim v183 / Agent-Reach v174 / camofox v179** precedent (mint the corpus-first-for-the-surface exemplar of a recurring world class the corpus doesn't yet represent).

**⚠️ NO-MINT alternative recorded, operator/audit-reviewable:** "a doc-*authoring* variant of the already-represented agent-code-context family (§C#23 + claude-context v40 + fff v194)." The mint stands on the **AUTHORS-PROSE-DOCS vs INDEXES/SEARCHES-CODE** mechanism/output boundary being load-bearing — the same kind of boundary that separated fff v194's lexical search from §C#23's graph. Either way, **counts UNCHANGED 46/11.**

§28 ≤2-new-standalones cap honored (1 mint).

### SECONDARY (NOT minted)

- **#19 19a** — first `langchain-ai` ORG subject (LangChain returning as an institution).
- **FIRST DeepAgents-built corpus subject** — a data-point on LangChain's `deepagents` harness ("open-source Claude Code alternative"). Audit-watch for N=2 (a non-corpus sibling, `langchain-ai/openshell-deepagent`, already exists). NOT a mint.
- **#12 / #22** — first subject that **auto-generates + maintains** `AGENTS.md`/`CLAUDE.md`. A facet **of** the §C mint, not a separate mint.
- **loop-engineering v189 cross-ref** — the daily CI-PR update loop + the content-snapshot no-op guard = a genuine L1/L2 unattended-loop instance (scheduled + git-diff-scoped + human-gated PR + anti-churn). Cross-ref, NOT a mint.
- **#84 84c** — multi-provider by design (5 providers; NO N-bump per v86; NOT the ponytail 14-platform mechanism).
- **GLM-5 v176 cross-ref** — the out-of-box default model is `z-ai/glm-5.2`. Data-point.
- **claude-api-cost-optimization** — defaults to cheap GLM 5.2 for a high-volume doc-writing task. **LV #20 Token-Economy QUALIFIED-ADJACENT** (no quantified benchmark → N stays 4).
- **#66 supply-chain / dual-use** — install BENIGN (first-party LangChain deps; no postinstall/curl-bash); **runtime MODERATE** (DeepAgents `LocalShellBackend` runs arbitrary shell — `virtualMode` sandboxes filesystem-tool *paths* but NOT the shell `execute` tool; writes to your repo; CI `contents: write` + secrets). Mitigated by the no-secret-reading prompt + secret-redaction + git-diff-reviewable, human-gated PRs.

### NON-claims

NOT **#52** (1.8k★/146 forks/0 releases page-stated §37.4; created-date not shown; ~3 days old → velocity **unestablishable**) · NOT **world-first** (DeepWiki + the doc-gen landscape precede) · NOT **#57** (a meta-*parallel* to the vault's LLM-Wiki pattern but it cites no corpus subject; the GLM-default + DeepWiki-peer are external; parallels/mentions ≠ recursion) · NOT **#18 B1-MCP** (a CLI + a CI job; it consumes no MCP and exposes no MCP) · NOT a new top-level pattern (**max stays #85**) · NOT §C#23 code-knowledge-graph (authors prose, doesn't index a graph).

---

## Tier

**T2 Service** — a self-hosted local **CLI documentation agent / developer tool**. Same family as **fff v194** ("library/tool for agents"), SkillSpector v169, SkillOpt v178, codebase-memory-mcp v172, agentmemory v66, codegraph v70. NOT T1 (not a skill/methodology *collection* — it's a running tool) and NOT T5 Agent-as-application (it's a narrow single-purpose doc agent, not an interactive coding agent like Kilo Code v177).

---

## Bookkeeping

- **Counts UNCHANGED: 46 confirmed top-level patterns / 11 CONFIRMED Library-vocab.**
- **§C live standalones 36 → 37** (+1, N=1); tracked PROVISIONAL surface ≈43 → **≈44**.
- **Streak: GA:55 → GA:56** (v195 is unambiguously goal-aligned — a real agent-documentation substrate on four live threads). **42 consecutive goal-aligned ships v153→v195.**
- **§35 CLEAR** — rolling-3 window {v193 GA, v194 GA, **v195 GA**} = 0 OG. (⚠️ the alt "v176/v186/v191/v193 OFF-GOAL-defensible" reading is unaffected — v195 is GA on any reading.)
- **inflation_check = discipline HELD:** 1 mint ≤2 cap; N=1 scoped honestly (corpus-first-for-surface, NOT world-first); NO-MINT alternative recorded reviewable; max #85; counts 46/11 unchanged; no double-count (§C standalone = capability; #12/#22 = a facet of it, not a separate N-bump; #84/#18 no bump); no N-bumps.

⚠️ **Ultracode note:** a workflow was used for read-only research (per the standing directive), but the verdict + every corpus claim were done **BY HAND**.
