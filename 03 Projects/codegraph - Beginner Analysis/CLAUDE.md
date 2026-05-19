# codegraph (colbymchenry) — Project CLAUDE.md

📍 **Status:** Active wiki build — **v70** (2026-05-19)
📍 **Routine:** `05 Skills/llm-wiki-routine-v2.2.md`
📍 **Subject:** [github.com/colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
📍 **npm:** [@colbymchenry/codegraph](https://www.npmjs.com/package/@colbymchenry/codegraph)
📍 **Author site:** [colbymchenry.com](https://colbymchenry.com)

---

## Phase 0 outputs (verified 2026-05-19)

### Subject identity

- **Tagline (verbatim):** *"Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer tool calls, 100% local"*
- **One-line value claim (verbatim):** *"94% fewer tool calls · 77% faster exploration · 100% local"*
- **Created:** 2026-01-18 → wiki build 2026-05-19 = **121 days old (~4 months)**
- **Author:** Colby McHenry (`colbymchenry`; solo individual; *"15+ years of experience building software"*; website [colbymchenry.com](https://colbymchenry.com))
- **License:** MIT
- **Stats at v70 wiki build:** 5,062 stars / 352 forks / 21 watchers / 55 open issues / 37 open PRs / 28+ releases (latest v0.7.9 on 2026-05-18)
- **Pinned at author level:** codegraph + devpit + shopify-graphql-admin-mcp + saturday.shop + n8n-gcp-firebase + frontend-audit-skill (20 public repos total)

### Subject classification (13-axis, v2.2 enhanced)

| Axis | Value |
|------|-------|
| **Tier** | **T2 Service** — provides MCP server + CLI as installable Node binary; sibling to v66 agentmemory (T2 Service MCP server) and v29 crawl4ai (T2 Service) |
| **Archetype** | solo-individual-multi-product-portfolio (matches Pattern #19 founder-personal lineage sub-archetype 19a; 20 repos with pinned 6 distinct products) |
| **Scale tier** | medium (5K stars at 4-month age; ~42 stars/day moderate-high) |
| **Primary lang** | **TypeScript 95.4%** + JavaScript 4.4% + Shell 0.2% |
| **Packaging tool** | npm `@colbymchenry/codegraph` + `npx` interactive installer + multi-agent installer with `--target` flag for Claude Code / Cursor / Codex CLI / OpenCode |
| **Origin story** | solo-individual-domain-tool (code-knowledge-graph augmentation for AI coding agents); not corporate-strategic, not viral-MVP |
| **Methodology** | pre-indexed knowledge graph (tree-sitter parsers + SQLite FTS5 + symbol/edge extraction) as **alternative to runtime grep/find exploration** by AI agents |
| **Governance file count** | 4 governance docs (README + CLAUDE.md + CHANGELOG + LICENSE) — moderate |
| **Agent/skill count** | MCP server with search + context + impact + call-trace tools (specific tool count not enumerated in probe) + CLI subcommands |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | tree-sitter (Atom upstream) + better-sqlite3 / web-tree-sitter + no methodology lineage cited |
| **Agent platforms supported** | **4 platforms: Claude Code + Cursor + Codex CLI + OpenCode** (via shared MCP server with per-platform installer config) |
| **Living-Domain-Standards Tracking** | NO — codegraph establishes own code-graph schema rather than tracking external standards |

### Velocity-screen + engagement-signal (v2.2 NEW)

| Metric | Value | Corpus context |
|--------|-------|---------------|
| Age | **121 days (~4 months)** | mid-life-cycle |
| Stars | 5,062 | medium-tier |
| Forks | 352 | moderate |
| Watchers | 21 | very low |
| Subscribers | 21 | low |
| Open issues | 55 | low |
| Open PRs | 37 | active community contribution |
| **`stars_per_day`** | **~42** | **moderate-HIGH** but NOT Pattern #52 EXTREME-VIRAL (threshold >300/day in <90 days); SUSTAINED 4-month velocity at this rate is healthy-growth |
| `fork_ratio` (forks/stars) | 0.069 (7%) | moderate |
| `watchers_ratio` (watchers/stars) | 0.0042 | very low — drive-by-stars pattern (similar to recent corpus) |
| `open_issues_ratio` | 0.011 | low |
| `open_prs/total_engagement` | 37 open PRs visible | **higher-than-usual community contribution velocity** |

**Velocity verdict:** SUSTAINED-MODERATE-HIGH velocity (4-month at 42 stars/day; would meet Pattern #52 threshold for short-window subjects but is mid-life-cycle subject). NOT Pattern #52 trigger; STRENGTHENING data point for sustained-velocity-test batch at v70+ audit.

### Pattern Library pre-check (Phase 0.5 expanded v2.2)

- **Pattern #18 Cross-IDE-Coexistence (CONFIRMED) + sub-archetype shared-backend-service (REGISTERED v69 audit):** **STRONG strengthening + N=3 sub-mechanism B evidence.** Pattern #18 sub-archetype shared-backend-service was registered at v69 audit with sub-mechanism B "one-binary-many-CLIENTS via CDP" (v69 CloakBrowser). codegraph adds **MCP variant** N+1 evidence to sub-mechanism B (one-binary-many-CLIENTS via MCP); combined with v66 agentmemory MCP variant = **N=3 evidence for sub-mechanism B with 2 protocol-variants (MCP × 2 + CDP × 1)**. → **Phase 4b PRIMARY: Pattern #18 sub-mechanism B N=3 strengthening + protocol-variants formalization**

- **Pattern #57 Cross-Wiki-Citation strengthening:** STRONG. README + CLAUDE.md cite **Claude Code (vault substrate)** + **Codex (v62 corpus subject)** + **OpenCode (v67 corpus subject)** + Cursor (non-corpus). 2 corpus subjects + Claude Code substrate citation = **STRONG (d) PASS criterion**.

- **Pattern #66 meta-supply-chain-awareness (CONFIRMED) strengthening:** STRONG. "100% local. No data leaves your machine. No API keys. No external services. SQLite database only." Explicit supply-chain isolation claim. v70 strengthens corpus pattern of supply-chain-as-positioning.

- **OC-E Synchronicity-Discipline-As-Policy (v68 zero observational) potential N+1 evidence:** Codegraph CLAUDE.md mandates *"Three files must stay synchronized when updating MCP tool behavior: server-instructions.ts, instructions-template.ts, and .cursor/rules/codegraph.mdc"* — config-synchronicity-discipline. Distinct from v68 zero's behavioral-synchronicity (examples + docs + tests + contracts aligned with current behavior). **Sister observation OR N=2 evidence under broader OC-E formulation**; defer mechanism-distinction decision to v70+ audit.

- **Pattern #19 ecosystem-portfolio-builder (CONFIRMED N=4 at v66) strengthening:** colbymchenry has 20 public repos with 6 pinned distinct products. Matches Pattern #19 sub-archetype 19a founder-personal lineage (similar shape to v23 Unsloth + v66 agentmemory rohitg00 + v64 claude-seo AgriciDaniel). Pattern #19 N+1 strengthening but NOT new sub-archetype.

- **NEW observational candidate: Pre-Indexed-Context-Layer as agent augmentation strategy** — codegraph's product axis is *"pre-index once, query many times"* as alternative to runtime grep/find exploration by agents. Corpus-novel positioning vs default Claude Code exploration. N=1 OBSERVATIONAL.

- **NEW observational candidate: Quantitative-Benchmark-Marketing** — codegraph leads with *"94% fewer tool calls · 77% faster exploration"* as primary product positioning. v69 CloakBrowser also led with quantitative claims (0.9 reCAPTCHA score / 30+ detection sites). **N=2 evidence** for quantitative-claim-as-marketing-positioning OBSERVATIONAL.

- **NEW observational candidate: Multi-Agent-Installer-Pattern** — codegraph v0.7.7 introduces interactive multi-agent installer (`--target` flag for Claude Code / Cursor / Codex CLI / OpenCode). Corpus-novel installer pattern that auto-detects agent platform + writes per-platform config. N=1 OBSERVATIONAL.

- **NEW observational candidate: Corpus-rare AGENTS.md auto-generation** — codegraph installer creates `AGENTS.md` file in user's project with usage guidance (per v0.7.8 CHANGELOG). Corpus subjects mostly hand-write AGENTS.md; auto-generated AGENTS.md from tool installer is corpus-novel. N=1 OBSERVATIONAL.

### Storm Bear meta-entity Phase 0.9 STRICT (decision pre-registered)

**Verdict: 2/4 STRICT PASS = MODERATE INCLUDE** (breaks v68 + v69 WEAK modal-streak — strength categorization continues to discriminate)

| Criterion | Pass/Fail | Reasoning |
|----------|-----------|-----------|
| (a) Author archetype peer | ❌ **FAIL** | Colby McHenry is solo software-developer (15+ years experience); NOT explicit Scrum-coach archetype. Conservative call: software-developer-only peer is not the FULL (a) criterion (Storm Bear is developer + Scrum coach). |
| (b) Operational tool for Scrum-coaching | ✅ **PASS** | codegraph augments Claude Code (vault substrate) with pre-indexed code intelligence — directly vault-deployable for Storm Bear's vault maintenance + coding work. Similar to v66 agentmemory pilot-candidacy framing. |
| (c) Methodology-influence-node | ❌ **FAIL** | codegraph is tooling-influence not methodology-influence; vault routine v2.x not shaped by codegraph approach |
| (d) In-corpus sibling reference | ✅ **STRONG PASS** | README + CLAUDE.md explicitly cite **Claude Code (vault substrate; foundation product) + Codex (v62 corpus subject) + OpenCode (v67 corpus subject)** + Cursor — 2 corpus subjects + Claude Code substrate = STRONGER (d) than v69 (which had 2 corpus subjects only) |

→ **MODERATE INCLUDE (2/4)** — breaks v68 + v69 WEAK modal-streak. Strength categorization spectrum continues to discriminate empirically.

**Streak effect:** Post-v64-RESET window now 6 consecutive PASS:
- v65 STRONGEST 3/4 STRICT
- v66 STRONG 4/4 STRICT
- v67 MODERATE 2/4 STRICT
- v68 WEAK 1/4 STRICT
- v69 WEAK 1/4 STRICT
- **v70 MODERATE 2/4 STRICT — breaks 2-consecutive-WEAK; restores spectrum diversity**

14-instance Phase 0.9 post-amendment window v57-v70 = 12 PASS / 2 SKIP = **85.7% INCLUDE rate** (slight uptick from v69 84.6%).

### Sibling detection

| Sibling | Relation | Why |
|---------|----------|-----|
| **v66 agentmemory** | **STRONG STRUCTURAL sibling** | Same T2 Service shape; both MCP servers for multi-platform agent augmentation; both solo-individual portfolios; codegraph = code-graph-layer / agentmemory = memory-layer |
| v62 codex-plugin-cc | corpus-citation sibling | codegraph explicitly supports Codex CLI as installer target; v62 is corpus Codex plugin |
| v67 opencode-antigravity-auth | corpus-citation sibling + v69 audit sub-archetype sibling | codegraph installer auto-targets `opencode.jsonc` (per v0.7.8 CHANGELOG); v67 was Opencode-ecosystem corpus subject |
| v69 CloakBrowser | recent v2.2 wiki + Pattern #18 sub-mechanism B sibling | v69 CDP variant of one-binary-many-CLIENTS sub-mechanism; codegraph MCP variant |
| v23 Unsloth + v64 claude-seo | Pattern #19 sub-archetype 19a sibling | Solo-individual-multi-product-portfolio shape |

### Tier placement decision

**T2 Service** — definitive. Rationale:
- Provides MCP server + CLI as installable Node binary (T2 Service signature)
- Multi-platform via MCP (similar to agentmemory v66 T2 Service)
- NOT T1 Augmentation (not a skill collection)
- NOT T4 Bridge (not protocol translation; provides domain service)

**Sub-archetype:** **shared-backend-service Pattern #18 sub-archetype B (one-binary-many-CLIENTS via MCP)** — registered at v69 audit with sub-mechanism A (one-backend-many-IDENTITIES; v67) + B (one-binary-many-CLIENTS via CDP/MCP; v69 CloakBrowser CDP + v66 agentmemory MCP). codegraph adds MCP-variant N=3 evidence.

### Phase 4b PRIMARY routing pre-registration

**PRIMARY:** **Pattern #18 sub-archetype shared-backend-service sub-mechanism B N=3 strengthening** — codegraph MCP-variant + agentmemory MCP-variant + CloakBrowser CDP-variant = N=3 across 2 protocol-variants. Sub-mechanism B "one-binary-many-CLIENTS" formalized via 3 protocol-variants. Proposal-document at `01 Analysis/` registering protocol-variants formalization.

**SECONDARY:**
- OC-E Synchronicity-Discipline-As-Policy N+1 evidence (v68 zero + v70 codegraph; sub-mechanism distinction config-vs-behavioral)
- Pattern #57 strengthening (2 corpus subjects + Claude Code substrate cited in single subject)
- Pattern #66 strengthening (100% local + supply-chain-isolation claim)
- Pattern #19 N+1 strengthening (founder-personal-multi-product-portfolio shape)
- NEW observational candidate OC-K: Pre-Indexed-Context-Layer as agent augmentation strategy
- NEW observational candidate OC-L: Multi-Agent-Installer-Pattern (single tool, multiple agent targets)
- NEW observational candidate OC-M: Quantitative-Benchmark-Marketing (N=2 with v69 CloakBrowser)
- NEW observational candidate OC-N: Auto-generated AGENTS.md from tool installer

### Consolidation guard

**Pre-build state (post-v69 OVERDUE-NATURAL-CADENCE audit 2026-05-19):**
- 44 confirmed / 30 active / 0.682 ratio (audit just disposed 24-item batch)
- Active count 30 = AT trigger threshold
- Ratio 0.682 well below 0.95 mini-audit trigger
- **PROCEED normally** — v69 audit disposed overdue backlog; v70 wiki proceeds in healthy state

**v70 contribution to state:**
- 0 NEW top-level patterns (NEW observational candidates only)
- ~4 NEW OC candidates (OC-K + OC-L + OC-M + OC-N) — would push active count to 34 if all register
- Ratio impact: minor (0.682 → ~0.77 if 4 OCs register)
- Phase 4b PRIMARY (Pattern #18 strengthening) is within-pattern; no top-level promotion

---

## Cross-references

- **Routine:** [llm-wiki-routine-v2.2.md](../../05 Skills/llm-wiki-routine-v2.2.md)
- **Pattern Library:** [PATTERN_LIBRARY.md](../../PATTERN_LIBRARY.md)
- **v69 audit document:** [04 Reviews/(C) 2026-05-19 Pattern Library mini-audit ...md](../../04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE; LARGEST batch corpus-history; Pattern #83 N=5 PROMOTION + 23 other items).md)
- **Strongest structural sibling:** [v66 agentmemory](../agentmemory - Beginner Analysis/CLAUDE.md)
- **Pattern #18 sub-mechanism B sibling:** [v69 CloakBrowser](../CloakBrowser - Beginner Analysis/CLAUDE.md)
- **Corpus-citation siblings:** [v62 codex-plugin-cc](../codex-plugin-cc - Beginner Analysis/CLAUDE.md) + [v67 opencode-antigravity-auth](../opencode-antigravity-auth - Beginner Analysis/CLAUDE.md)
- **Pattern #19 19a archetype sibling:** [v23 Unsloth](../Unsloth - Beginner Analysis/CLAUDE.md) + [v64 claude-seo](../claude-seo - Beginner Analysis/CLAUDE.md)

---

## Phase status

- [x] Phase 0 — Pre-flight + probe complete
- [x] Phase 1 — Scaffold (project folder + CLAUDE.md + skeleton)
- [x] Phase 2 — Source ingestion (3 clusters complete)
- [x] Phase 3 — Entity pages (4 entities; Storm Bear meta MODERATE INCLUDE 2/4)
- [x] Phase 4a — Beginner bilingual guide (`03 Published/`)
- [x] Phase 4b — Pattern #18 sub-mechanism B N=3 strengthening + protocol-variants formalization (`01 Analysis/(C) Pattern-18 sub-mechanism B one-binary-many-CLIENTS N=3 protocol-variants formalization.md`)
- [x] Phase 5 — Iteration log + Pattern Library updates (header active-candidates + `_patterns/05-recent-additions.md` v70 strengthening block appended)
- [x] Phase 6 — Vault sync (03c renamed → v61-v70 + v70 entry appended + root CLAUDE.md + `_goals/02-version-log.md` v70 entry + PATTERN_LIBRARY.md state-block)

**Wiki BUILD COMPLETE 2026-05-19 session 73++.** Next: commit + push.
