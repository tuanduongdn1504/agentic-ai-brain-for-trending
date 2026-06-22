# (C) v181 cortex-hub — Verdict & Collision-Check Record

**Subject:** `lktiep/cortex-hub` — Self-hosted AI Agent Memory + Code Intelligence Platform · v0.7.0 · MIT · author **Jack Le** (`lktiep`, jackle.dev).
**Ship:** v181 · **Date:** 2026-06-22 · **Verified at commit:** `27d5d23` (default branch `master`, 2026-06-15).
**Build method:** Verdict produced **INLINE** (NOT the multi-agent workflow) per `feedback_wiki_verify_independently_check_collisions`. Source-verification of the clone was delegated to one read-only Explore agent (safe, factual — no corpus-fact judgment); all collision / identity / prior-instance claims were verified **by hand** (grep over `_state/` + `_patterns/` + a project-folder listing; WebSearch to confirm the npm-package identity + license; 2× WebFetch repo/profile).

---

## 1. Verdict

**GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG. Tier T2 Service. NO MINT.** Counts UNCHANGED **46/10**; §C surface unchanged (no new standalone). Streak `GA:42 · OG:11 [7 ov]` → **`GA:43 · OG:11 [7 ov]`** (OFF-GOAL-v176 reading → `GA:42 · OG:12`). §35 rolling-3-ship window {v179 GA, v180 GA, **v181 GA**} = 0 OG → **CLEAR**. **28 consecutive goal-aligned ships v153→v181** (GA reading).

### (a) FAILS cleanly — disclosed indie builder, not a registered axis
**Jack Le** (`lktiep`, site **jackle.dev**, 21 public repos, 6 followers; cortex-hub is the sole pinned repo). A **disclosed individual indie developer** — not Anthropic ((a)-7 is Anthropic-only), and "solo indie builder building in public" is not a registered (a) cultural-peer axis. This is the **v171 devspace / v174 Agent-Reach** situation (disclosed indie, NOT a bare handle), not the v172/v173 bare-handle situation. Per the v171 precedent + standing rec (ii), the "indie-builder axis" is **operator-reviewable, NOT minted** → clean FAIL, no axis. A Vietnamese-name inference ("lktiep" ≈ Lê … Tiệp; the operator is VN) is likewise **NOT** an (a)-rescue (the v159→v180 discipline + the explicit v180 handling of the v78 product-locale precedent). First Jack-Le author → a **#19 19a** data-point. ⚠️ **3rd instance** (after v171 + v174) of the disclosed-indie-builder (a) question for a software-developer operator → reinforces, does not resolve, the open rec-(ii) item (now N=3).

### (b) STRONG — keys the tier
cortex-hub **is MCP infrastructure for AI coding agents** — a self-hosted backend giving Claude Code (first among supported agents) + 5 others persistent memory, code intelligence, shared knowledge, quality gates, and an experimental cross-IDE orchestration layer = **dead-center on Goal #1**. It lands on **three** live pilot threads at once — **CC-memory-systems** (mem9 + temporal knowledge base), **multi-agent-orchestration** (Conductor cross-IDE task delegation), **claude-api-cost-optimization** (CLIProxy gateway + quality gates) — and is **directly pilotable into the vault and into hireui** (whose CONSTITUTION is "GitNexus-first" — and cortex-hub *is* a GitNexus-wrapping shared hub). STRONG-not-STRONGEST because: third-party + **augmentation** (it augments existing agents, isn't Anthropic substrate); Claude is one of six supported agents; and it is a **thin orchestration layer over third-party engines** (§4.2/4.5 of the wiki). Calibrates to agentmemory v66 / codebase-memory-mcp v172 / devspace v171 (b) STRONG. *(Operator-reviewable: arguably among the strongest (b)'s in the recent run — three pilot threads + the hireui/GitNexus tie-in — recorded, not used to inflate the grade.)*

### (c) STRONG (with honest caveats; a MODERATE reading is defensible)
**Real original surface:** a working MCP server (18 tools); **mem9**, a home-grown embedding + memory engine (Xenova-local default / Gemini fallback, Qdrant store, branch→project→agent hierarchical recall); a SQLite temporal knowledge base (6 hall types, `validFrom`/`asOf`); a recipe-learning system; 4-dimension quality gates; the Conductor scaffolding (agent registry + WebSocket + task lifecycle + dashboard page); a Next.js 15 / React 19 dashboard (13 pages, static export); a 6-agent MCP-config installer; a 5-service Docker compose; Cloudflare-tunnel deploy. **Caveats foregrounded:** two of the three headline capabilities are **vendored third-party black boxes** (GitNexus = the npm `gitnexus` package = corpus v33; CLIProxy = `eceasy/cli-proxy-api`) → cortex-hub is, in the source-reader's words, "a thin orchestration layer"; the README **inflates** the tool count (24 → 18); Conductor is **experimental**; tests are **minimal** (~2 files); it is **v0.7.0 pre-GA**. STRONG for the breadth of original orchestration + the memory/knowledge/quality/dashboard surfaces being genuinely cortex-hub's own; a MODERATE reading (given the vendored engines + near-zero tests) is defensible — recorded honestly. (Mirrors camofox v179's "(c) STRONG, but the hard part is upstream.")

### (d) STRONG
Dense, unambiguous family + adjacency map (§3 below). Clear home (augment-backend MCP-server family), clear distinctions from the runtimes/bridges/orchestration-platforms, and a striking corpus-recursive-dependency cross-reference.

---

## 2. Pattern outcome — NO MINT (the v179/v180 packaging-discipline)

**No new top-level pattern (max stays #85). No new §C standalone. Counts UNCHANGED 46/10. §C surface unchanged.**

A candidate corpus-first facet exists — **"a single self-hosted MCP hub that UNIFIES multiple agent-infrastructure capabilities (memory + code-intel + temporal knowledge + recipe-learning + LLM gateway + quality gates) shared across many existing coding agents"** — and the §C registry confirms **no existing standalone** covers it (the corpus has point-solutions and agent-runtimes, not a unified augment-hub). So a mint *would* be corpus-first as a class. It is **DECLINED**, recorded as a **DEFERRED watch axis**, for four reasons (the v180 telegram template, applied):

1. **Weak/early anchor for a corpus-first class.** cortex-hub is a **thin orchestration layer wrapping third-party engines** — two of three headline capabilities are vendored (GitNexus = a corpus subject's npm package; CLIProxy = `eceasy/cli-proxy-api`); only `mem9` is original. README inflates the tool count; Conductor is experimental; 57★, single-author, v0.7.0 pre-GA, ~2 test files. The Kilo-Code-v177 "mint N=1 to credit a recurring world-class" precedent applies to **the major exemplar** of a class — this is an **early/weak instance**, not the exemplar.
2. **Packaging-not-capability.** The distinctive move is **integration/unification of existing MCP capabilities behind one endpoint** — a delivery/packaging choice, not a new capability. Every component capability has corpus precedent (memory → agentmemory v66; code-graph → codegraph v70 / codebase-memory-mcp v172; gateway → cc-switch v73). This is exactly the "draw-the-circle-to-make-it-first" move the routine declines (cf. camofox v179's *declined* separate "anti-detect browser AS agent server" mint).
3. **Heavy family overlap.** The augment-backend MCP family (agentmemory v66 / supermemory v132 / codegraph v70 / codebase-memory-mcp v172 §C#32) + the self-contained-platform family (PilotDeck v175 §C#35 / OpenHuman v118) + the orchestration-platform standalone (§C#23) already surround this region.
4. **The class recurs but is unrepresented by a strong corpus instance.** "Unified agent-memory/context/infra hub" is a real emerging product category (the commercial mem0 / Letta / Pieces space) — none in corpus. Mint on a cleaner exemplar later; cortex-hub becomes a credited prior data-point (§28 anti-inflation + §35).

### What IS recorded (secondary, NOT minted)

- **Corpus-recursive DEPENDENCY (headline cross-reference, NOT a #57).** cortex-hub bundles + sed-patches the corpus's **own v33 subject GitNexus** (`abhigyanpatwari/GitNexus`, npm `gitnexus`, PolyForm-Noncommercial 1.0.0, ~36.8k weekly downloads) as its code-intelligence engine, **uncredited**, inside an **MIT** repo. This is a genuine "corpus subject embedded as a load-bearing runtime dependency of a later corpus subject" data-point — **stronger than a mention** but **NOT a Pattern #57 influence-citation** (there is *no acknowledgment at all* — silent incorporation, the opposite of the PilotDeck v175 "thanks to pioneers" case). Recorded as a notable cross-reference; whether "corpus-subject-as-dependency-of-corpus-subject" is a trackable thing is deferred to audit (N=1 curiosity).
- **License/attribution flag (#66 supply-chain).** PolyForm-Noncommercial GitNexus inside an MIT "use across all your agents" repo, uncredited → a real concern for any **commercial** self-hoster (the operator's Scrum-coaching / SaaS context). Plus: `curl|bash` install writing MCP configs + git hooks + a global skill into `~/.claude` across 6 agents; 5-service Docker compose; Cloudflare tunnel; Bearer-token auth.
- **Pattern #18 sub-archetype B / B1-MCP instance-strengthening.** One MCP endpoint, 6 agent clients auto-configured by `install.sh` = a clean B1-MCP instance (the agentmemory v66 / codegraph v70 / devspace v171 / codebase-memory-mcp v172 lineage). Per v151/v172, B1-MCP was reconciled to N=7 at v151 (+devspace v171 +codebase-memory-mcp v172 = N≈9); +cortex-hub v181 = **N≈10** (exact tally = audit bookkeeping per the v151 "filing-is-an-act" note). The standalone-vs-#18-B1 axes are distinct (capability vs distribution structure) → no double-count (the v140/v171/v172 precedent). A B1→own-sub-archetype split was DECLINED at v151 → pure instance-strengthening, NOT a pending promotion.
- **§C#32 audit-reconciliation note (do NOT act unilaterally).** cortex-hub's code-graph = GitNexus v33 re-used via dependency → it does **not** add a clean new cross-author instance to §C#32 ("Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP," N=2: codegraph v70 + codebase-memory-mcp v172). It *surfaces* that **GitNexus v33 (16 MCP tools, AST→graph→MCP) and graphify v16 actually PREDATE codegraph v70** as members of that family — the §C#32 "first instance = codegraph v70" framing may need revisiting at audit. Flagged, deferred.
- **Library-vocab #20 Token-Economy QUALIFIED-ADJACENT.** The MemPalace benchmark comparison (R@5 96.0% / ~10ms embedding / $0-cost) is page-stated + unreplicated → **N stays 4** (the v168/v172/v175 precedent).
- **#19 19a** first Jack-Le author data-point. **#12 LLM-routing-artifacts** INCIDENTAL cross-ref (ships CLAUDE.md + AGENTS.md + .cursorrules; NO N-bump). **Recipe/knowledge credits** to MemPalace + HKUDS/OpenSpace (NON-corpus projects → NOT #57).

### NON-claims
- **NOT corpus-first** as "code knowledge-graph MCP" (codegraph v70 / codebase-memory-mcp v172 precede; and cortex-hub *re-uses* GitNexus v33, doesn't add a new instance).
- **NOT a new top-level pattern** (max #85; the #86/#88 rejection at v168/v169).
- **NOT #52** (57★/17 forks/2 releases/v0.7.0 page-stated, NOT API-verified §37.4 → velocity unestablishable).
- **NOT #57** (credits MemPalace + HKUDS/OpenSpace = NON-corpus; the GitNexus link is *uncredited dependency-incorporation*, not influence-citation; mentions/dependency ≠ recursion).
- **NOT §C#35 PilotDeck** (cortex-hub is an augment-backend, not its own agent-OS runtime). **NOT §C#31 devspace** (augments existing local agents; doesn't manufacture one from a hosted host). **NOT §C#23 orchestration platform** (Conductor is experimental, not the core; doesn't orchestrate multiple third-party agents as units). **NOT §C#32 N=3** (re-uses the v33 instance via dependency).

---

## 3. Family & adjacency map

| Relationship | Corpus subject | How cortex-hub relates |
|---|---|---|
| **Bundled dependency (corpus-recursive)** | **GitNexus v33** (`abhigyanpatwari`) | cortex-hub's code-intel engine IS the npm `gitnexus` package = GitNexus v33, installed + sed-patched, uncredited; PolyForm-vs-MIT license tension |
| Same capability class (code-graph MCP) | codegraph v70 / **codebase-memory-mcp v172 §C#32** / graphify v16 | cortex-hub re-uses GitNexus (this family) rather than adding a clean new instance |
| Same capability class (memory MCP) | agentmemory v66 / supermemory v132 | mem9 is cortex-hub's own (Xenova + Qdrant); not a wrapper of these |
| Same capability class (provider gateway) | cc-switch v73 / relay v112/v117 | CLIProxy = `eceasy/cli-proxy-api` (third-party) |
| Family (self-contained platform) — DISTINCT | PilotDeck v175 §C#35 / OpenHuman v118 | those ARE agent runtimes; cortex-hub augments existing third-party agents |
| Direction-contrast — DISTINCT | devspace v171 §C#31 | devspace manufactures a local agent from a hosted host; cortex-hub augments local agents |
| Adjacency (experimental) | Paseo v150 / ai-maestro v163 §C#23 | Conductor ≈ cross-IDE task delegation, but WIP, not the core |
| Distribution structure | Pattern #18 B1-MCP | one endpoint, 6 clients auto-configured → instance-strengthening N≈10 |

---

## 4. Verification log (per `feedback_wiki_verify_independently_check_collisions`)

1. **Clone + source-read** at `27d5d23` (read-only Explore agent): MCP tool count (18 registered vs README's 24); GitNexus = external npm `gitnexus@latest`, sed-patched (`infra/Dockerfile.gitnexus`); mem9 = own (Xenova + Qdrant, no mem0/agentmemory/supermemory deps); CLIProxy = `eceasy/cli-proxy-api`; 6 hall types; 4 quality dims; Conductor experimental; install.sh = config-writer (not binary downloader); 6 agents; ships CLAUDE.md + AGENTS.md + .cursorrules; no acknowledgments section; ~2 test files; zero TODO markers.
2. **Identity verified by hand:** the npm `gitnexus` package = `abhigyanpatwari/GitNexus` (corpus v33), **PolyForm-Noncommercial 1.0.0**, ~36.8k weekly downloads (WebSearch). The shared component name was **NOT** assumed to be the corpus subject until this was confirmed.
3. **Author verified by hand:** Jack Le / `lktiep` / jackle.dev / 21 repos (WebFetch of the GitHub profile) → disclosed indie builder, (a) FAIL, no rescue.
4. **Collision grep by hand** over `_state/` + `_patterns/` + a `03 Projects/` folder listing: confirmed the prior corpus "GitNexus" is `abhigyanpatwari/GitNexus` v33 (a *different author* from cortex-hub's lktiep); read the full §C standalone registry (#10–#38) → confirmed **no existing "unified multi-capability agent-infra hub" standalone** (so a mint would be corpus-first) and confirmed §C#32 is the code-graph standalone cortex-hub re-uses-not-adds-to.
5. **README quotes** captured verbatim (tagline, isolation thesis, MemPalace benchmark, HKUDS/OpenSpace recipe credit, `curl|bash` install, Conductor-experimental statement) via raw-`master` WebFetch.
6. **inflation_check = discipline HELD:** 0 mints (NO MINT verdict), max #85, counts 46/10 unchanged, no §C surface change, no improper N-bumps (the §C#32 N stays 2; #20 N stays 4), no double-count. The doc-vs-code inflation ("24 tools") was caught + documented as the code-verified 18.

---

## 5. Pilot note

**Highest *relevance* of the recent run, but among the heaviest *footprint* + a unique license wrinkle** → NOT the first pilot. Relevance is high: it lands on three pilot threads (memory / orchestration / cost) and directly mirrors hireui's "GitNexus-first" setup. But: 5-service Docker compose (Qdrant + gitnexus + CLIProxy + dashboard-api + hub-mcp); `curl|bash` installer writing configs/hooks/skill into `~/.claude` across 6 agents; Cloudflare tunnel; v0.7.0 pre-GA; **and the GitNexus PolyForm-Noncommercial dependency** (a real license question for commercial use). **Fence:** install-snapshot + read `install.sh` before any `curl|bash` (prefer manual Docker-compose) + scratch project first + configure a **single agent (Claude Code only)**, not all 6 + **resolve the GitNexus PolyForm-Noncommercial license before any commercial use** + pin v0.7.0. **Ladder placement:** behind the read-only candidates — SkillSpector v169 (lowest-risk) → claude-tap v173 (value-per-risk) → Agent-Reach v174 (capability) → codebase-memory-mcp v172 → comparable weight to PilotDeck v175 / devspace v171 (heavy self-hosted platforms), **with the added license caveat**. PILOT lever still formally stands (zero piloted).

---
*Verdict produced inline. Source-verification delegated to one read-only Explore agent; all corpus-fact, collision, identity, and license claims verified by hand (grep + WebSearch + WebFetch). No multi-agent verdict workflow was used (per the vault memory).*
