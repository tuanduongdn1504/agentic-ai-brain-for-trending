# (C) Log — ai-agents-for-beginners Wiki

---

## [2026-04-18] setup | Phase 0+1 — Pre-flight + Scaffold (6th routine run)

- **Routine:** `05 Skills/llm-wiki-routine.md` v1 (6th auto-execution — **first different-domain**)
- **Phase 0 pre-flight:** ✅ PASSED
  - URL accessible (cvtot fork của microsoft/ai-agents-for-beginners)
  - **Clone FAILED** (3 attempts: default branch, `-b main`, `--filter=blob:none`) — git hangs after 17-27MB download, no checkout
  - **Pivoted to WebFetch** — raw.githubusercontent.com content acquisition
  - **Sibling detection: 5 projects** — 4 Tier 1 (ECC + Superpowers + gstack + GSD) + 1 Tier 2 (goclaw)
  - **Domain classification: NEW TIER** → Tier 3 "Agent-as-education" (different purpose than Tier 1 dev-tool-tier or Tier 2 platform-tier)
  - **Phase 4b routing = Tier 3 taxonomy expansion** (extends v4 2-tier model to 3-tier)

- **Phase 1 scaffold:**
  - Project folder duplicated từ template
  - 8 subfolders created
  - Source acquisition: WebFetch (not clone) — 8 lesson READMEs retrieved

- **Initial repo survey (via WebFetch README):**
  - Main README ~400+ lines structured: 10 lessons + 4 Coming Soon
  - 10 core lessons:
    1. Intro to AI Agents and Agent Use Cases
    2. Exploring AI Agentic Frameworks
    3. Understanding AI Agentic Design Patterns
    4. Tool Use Design Pattern
    5. Agentic RAG
    6. Building Trustworthy AI Agents
    7. Planning Design Pattern
    8. Multi-Agent Design Pattern
    9. Metacognition Design Pattern
    10. AI Agents in Production
  - Continuing lessons: 11 Agentic Protocols (MCP/A2A/NLWeb), 12 Context Engineering, 13 Agentic Memory, 14 MAF
  - Coming Soon (4): CUA, Scalable, Local, Securing
  - 50+ language translations (**Vietnamese included!** Unique of 6 projects to have native VN từ source)
  - Tech stack: Azure AI Foundry, GitHub Models, MAF, Azure AI Agent Service, Semantic Kernel, AutoGen
  - Community: Microsoft Foundry Discord
  - License: MIT (Microsoft trademark guidelines apply)

- **Unique findings:**
  - **Educational curriculum structure** — not a tool or framework, but a teaching resource
  - **Microsoft-authored** (well-resourced production-grade samples)
  - **Covers Tier 1/2 siblings' concepts at concept level** — e.g., Lesson 11 teaches MCP (which ECC/Superpowers/gstack USE); Lesson 12 teaches context engineering (which GSD SOLVES; which goclaw IMPLEMENTS); Lesson 08 teaches multi-agent (which gstack specialist roles EMBODY)
  - **Meta-relevance stronger than siblings** — this is **foundation layer** below the tool wiki layer
  - **Language accessibility** — VN translations suggest international scale
  - **Jupyter + .NET samples** — polyglot, learnability focus
  - **Coming Soon = curriculum in active evolution**

- **Source strategy:**
  1. Main README (already retrieved via WebFetch) — curriculum overview + tech stack + community
  2. Core lessons cluster: 01 (agent types) + 03 (design patterns) + 05 (Agentic RAG) + 08 (multi-agent) — already retrieved
  3. Frameworks + Protocols cluster: 02 (AutoGen/SK/Azure) + 11 (MCP/A2A/NLWeb) + 12 (context eng) + 14 (MAF) — already retrieved

- **Phase 0+1 status:** ✅ COMPLETE (scaffold + source retrieved via WebFetch; foundational files written)
- **Next:** Phase 2 source summaries

---

## [2026-04-18] ingest | Phase 2 — Source summaries (3 cluster files)

- **Source #1:** `(C) README summary.md` — curriculum overview (10 core + 4 continuing + 4 Coming Soon), tech stack (Azure AI Foundry + GitHub Models + SK + AutoGen + MAF), 50+ languages with native VN, Microsoft Foundry Discord, MIT license, related Microsoft Beginners courses suite
- **Source #2:** `(C) Core lessons cluster summary.md` — **NEW CLUSTER STRATEGY** (4 lessons 01+03+05+08 per file). L01 (7 agent types), L03 (3 design dimensions Space/Time/Core + 3 guidelines Transparency/Control/Consistency), L05 (Agentic RAG 5-step iterative loop), L08 (Multi-Agent orchestration patterns Group Chat/Hand-off/Collaborative Filtering). Concept → sibling implementation mapping included.
- **Source #3:** `(C) Frameworks + Protocols cluster summary.md` — 4 lessons 02+11+12+14. L02 (AutoGen/SK/Azure AI Agent Service), L11 (MCP/A2A/NLWeb tiered protocol ecosystem), L12 (context engineering 5 types + 4 failure modes), L14 (MAF = SK + AutoGen merger). Infrastructure readiness mapping + Microsoft ecosystem consolidation.
- **Key findings:**
  1. **Cluster strategy novel for education domain** — 8 lessons → 2 cluster summaries (not 8 individual)
  2. **WebFetch-first approach** when clone blocked (3 git clone attempts all failed — default branch, filter-blob, standard clone)
  3. **50+ language translations including Vietnamese** — unique in corpus (only goclaw also has VN)
  4. **Microsoft vendor bias** — AutoGen/SK/MAF emphasis, minimal LangChain/CrewAI
  5. **Protocol coverage unique** — only Tier 1/2/3 wiki to teach MCP/A2A/NLWeb at concept level (others USE MCP, don't TEACH)
- **Phase 2 status:** ✅ COMPLETE

---

## [2026-04-18] entities | Phase 3 — Entity pages (4 building blocks)

- **Entity #1:** `(C) Agent Design Patterns.md` — 7 agent types + 3 design dimensions + 3 guidelines; design decision matrix; examples (customer support agent, research assistant); sibling implementation table (all 5 siblings = Hierarchical at scaffolding); Storm Bear vault mapping (rules = implementation guidelines)
- **Entity #2:** `(C) Agentic RAG.md` — 5-step iterative loop; classic RAG vs Agentic RAG comparison; self-correction + domain autonomy + extended workflows capabilities; sibling comparison (goclaw = full Agentic RAG via Knowledge Vault); vault's `llm-wiki-ingest` skill ≈ Agentic RAG for wiki construction
- **Entity #3:** `(C) Multi-Agent Systems.md` — 3 scenarios + 3 orchestration patterns + refund process example (process-specific + general-purpose mix); metacognition adjacent concept (L09); sibling MAS implementation comparison (all 5 siblings implement some MAS form); vault as proto-MAS (Claude + specialized skills)
- **Entity #4:** `(C) Agentic Protocols (MCP + A2A + NLWeb).md` — 3 protocols detailed + tiered ecosystem; adoption patterns (MCP high, A2A medium, NLWeb low-emerging); sibling usage (all 5 = MCP users, none A2A/NLWeb); Storm Bear upgrade path (add MCP first for GitHub/filesystem)
- **Format compliance:** 13-section canonical format
- **Cross-references:** Each page links 5 sibling projects (4 Tier 1 + 1 Tier 2) + course concept sources
- **Phase 3 status:** ✅ COMPLETE

---

## [2026-04-18] publish | Phase 4 — Published guides (2 deliverables)

- **Phase 4a:** `03 Published/(C) AI Agents for Beginners - Huong dan cho nguoi moi.md` — bilingual beginner guide (~550 lines, 9 parts). Parts: intro, core concepts overview, key concepts deep dive, tech stack + setup, unique features (metacognition, protocol-awareness, MS ecosystem, VN translation), sibling comparison, 4-week roadmap, next steps, contribution opportunities. Different style vs siblings: **this IS a curriculum roadmap** (not teaching a tool).
- **Phase 4b:** `03 Published/(C) Agent framework taxonomy v2 - 3 tier.md` — **EXTENDS v4 taxonomy 2-tier → 3-tier** (~750 lines, 15-axis analysis, 7 personas). **Tier 3 "Agent-as-education" added.** 3 emergent patterns unique to 3-tier view: Purpose → Format correlation, Vendor consolidation increases with Tier, Learning progression is recursive not linear. Clean partition of 6 corpus items across 3 tiers.
- **Phase 4 status:** ✅ COMPLETE
- **Insight:** v6 Phase 4b = **taxonomy extension** (not new taxonomy + not N-way). Fourth Phase 4b output type.

---

## [2026-04-18] iterate | Phase 5 — Iteration log v6

- **Output:** `07 Iteration Logs/(C) 2026-04-18 v6 build learnings.md`
- **Velocity reduction** — first since v3 plateau (~2h vs ~2.5h baseline). Cause: cluster summary strategy saved writing time.
- **Key insights:**
  1. Routine handles 4 routing types now (same-domain + adjacent + same-tier + different-domain)
  2. 3-tier taxonomy stable across corpus
  3. Cluster summaries for education domain
  4. WebFetch as resilient fallback for clone-blocked repos
  5. Meta-relevance chain continues (L12 Context Engineering = GSD's context rot)
  6. Writing time dominates velocity, not comprehension
  7. 3-tier coverage = decision framework complete for current corpus
- **10+ action items** carryover to routine v2 (from v3-v6)
- **Recommendation:** Option A Storm Bear pilot (unchanged 4 consecutive rec) OR Option B routine v2 upgrade
- **Phase 5 status:** ✅ COMPLETE

---

## [2026-04-18] vault-sync | Phase 6 — Vault file updates

- Updated project `(C) index.md` — all phases ✅, deliverable tables populated
- Updated project `(C) log.md` — all phase entries appended
- Updated root `CLAUDE.md` — ai-agents-for-beginners project entry + 6-wiki milestone + 3-tier taxonomy note
- Updated `GOALS.md` — mark v6 shipped, 3-tier taxonomy established, version log append
- **Phase 6 status:** ✅ COMPLETE

---

## 🎉 v6 ALL PHASES COMPLETE

**6th auto-execution của routine successful.** First different-domain wiki shipped. 3-tier taxonomy established. Routine handles 4 routing modes.

**Routine v1 = production-stable across 6 runs** covering all domain routing types (same/adjacent/same-tier/different).

---

## [2026-04-18] post-ship retry | Background task retries — GitHub API probe succeeds

- **Context:** User requested retry of 3 failed background tasks from v6 build session (all git clone failures with RPC connection reset).
- **Retry strategies:**
  1. `git clone --depth=1 --single-branch -b main` (shallow clone) → still hanging
  2. `curl api.github.com/repos/cvtot/ai-agents-for-beginners` → ✅ **SUCCESS** (HTTP 200, 20 KB JSON)
  3. `curl codeload.github.com/.../tar.gz` (tarball) → truncated at 2.7 MB of 3.37 GB claimed — "unexpected end of file"

- **Root cause confirmed:** **Repo size = 3.4 GB** (fork), 3.7 GB (upstream). Network can't sustain transfer reliably. Clone failure is **infrastructure, not config**.

- **Findings from API probe (answers Open Question #1):**
  - Fork (`cvtot`): pushed 2026-01-12, size 3.4 GB, 0 stars, 0 forks, fork=true
  - Upstream (`microsoft`): pushed 2026-04-12, size 3.7 GB, **56,913 stars**, 19,718 forks
  - **Fork is 3 months stale vs upstream** — cvtot has not synced since January 2026
  - **Pure personal fork** (no stars/forks) — not a community maintenance or translation fork
  - Description confirmed: "12 Lessons to Get Started Building AI Agents" (fork README expanded to 14)
  - License MIT confirmed both fork + upstream

- **Wiki updates:**
  - `01 Analysis/(C) open questions.md` — Q1 marked RESOLVED với API findings
  - This log entry

- **Routine v2 action item added:**
  - **For large repos (>1 GB), skip clone entirely.** Use GitHub API for metadata + WebFetch for content. Add size check via API probe as Phase 0 step.

- **Status:** Retry productive. Wiki content unchanged (already shipped via WebFetch). Open question #1 resolved.

