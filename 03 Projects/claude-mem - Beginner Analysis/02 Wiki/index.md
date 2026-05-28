# thedotmack/claude-mem — Wiki index (v103)

**Subject**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
**Description**: "Persistent Context Across Sessions for Every Agent — Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions."
**Wiki built**: 2026-05-28 (routine v2.3.1)
**Tier**: T2 Service / Memory-System sub-archetype (N=2 with v66 agentmemory)
**Phase 0.9 verdict**: STRONGEST INCLUDE 4/4 with (c) STRONGEST + (a)(b)(d) STRONG

---

## Quick facts (verified GitHub API 2026-05-28)

- **Owner**: thedotmack = **Alex Newman** (15-year GitHub account 2011-03-22; 1,629 followers; 119 public repos; Twitter `@Claude_Memory` = product-branded handle CORPUS-NOVEL observational)
- **Created**: 2025-08-31 (~270 days at fetch; ~9 months)
- **Last push**: 2026-05-28 (today; actively maintained)
- **Stars**: 79,253 (~293.5/d HIGH-NOT-EXTREME upper-edge; approaches but below EXTREME-VIRAL >300/d threshold)
- **Forks**: 6,808 (fork ratio 0.086 active-deployment)
- **Watchers** (subscribers): 282 (Library-vocab #16 Engagement-Deficit-Extreme MEGA-scale strengthening = 281× star-to-subscriber ratio)
- **Open issues**: 121
- **License**: Apache 2.0
- **Primary language**: TypeScript
- **Default branch**: main
- **Homepage**: claude-mem.ai (custom domain at .ai TLD)
- **Discussions**: ENABLED
- **Topics (20-axis)**: ai + ai-agents + ai-memory + anthropic + artificial-intelligence + chromadb + claude + claude-agent-sdk + claude-agents + claude-code + claude-code-plugin + claude-skills + embeddings + long-term-memory + mem0 + memory-engine + openmemory + rag + sqlite + supermemory

---

## Architecture (per README)

**Core mechanism**: Persistent memory compression for AI agents — automatically preserves context between sessions, captures tool usage observations, generates semantic summaries, retrieves relevant context for future interactions.

**5-lifecycle-hook architecture**:
1. SessionStart
2. UserPromptSubmit
3. PostToolUse
4. Stop
5. SessionEnd

**Persistence + retrieval stack**:
- HTTP worker service on port 37777 + web UI
- SQLite database with FTS5 full-text search
- Chroma vector database for hybrid semantic/keyword search
- `mem-search` skill for natural-language queries

**Token efficiency claim**: "~10x token savings by filtering before fetching details" via 3-layer search workflow (index → timeline → full details).

**30-locale mode system** (CORPUS-RECORD-HIGH at v103; exceeds v99 cmux 21-locale by ~43%): Arabic + Bengali + Chill specialized + Czech + Danish + German + Greek + Spanish + Finnish + French + Hebrew + Hindi + Hungarian + Indonesian + Italian + Japanese + Korean + Dutch + Norwegian + Polish + Portuguese-BR + Romanian + Russian + Swedish + Thai + Turkish + Ukrainian + Urdu + **Vietnamese (vi)** + Chinese (zh) + specialized modes (code + email investigation + law study + meme tokens).

**Beta channel**: "Endless Mode" (biomimetic memory architecture).

---

## Top-level repo structure (CORPUS-RECORD LLM-routing artifact density)

| Artifact | Type | Notes |
|---|---|---|
| `.agent/` | Dir | LLM-routing artifact |
| `.agents/` | Dir | LLM-routing artifact (plural form distinct from `.agent/`) |
| `.claude/` | Dir | Claude Code config (commands + plans + reports + settings.json) |
| `.claude-plugin/` | Dir | Claude Code plugin manifest |
| `.codex-plugin/` | Dir | **CORPUS-FIRST Codex-plugin-as-top-level-artifact** in v60+ window |
| `.windsurf/` | Dir | Windsurf integration |
| `cursor-hooks/` | Dir | **CORPUS-FIRST Cursor-specific top-level hooks directory** in v60+ window |
| `WARP.md` | File | **CORPUS-FIRST Warp-terminal LLM-routing artifact** in v60+ window |
| `CLAUDE.md` | File | Project-CLAUDE.md routing |
| `NOTICE` | File | Apache-2.0 NOTICE attribution |
| `SECURITY.md` | File | Security policy |
| `openclaw/` | Dir | **CORPUS-FIRST harness-integration-as-top-level-package** in v60+ window (own SKILL.md + install scripts + Dockerfile.e2e + e2e tests + package.json) |
| `plugin/skills/` | Dir | 7th implementer in agentskills.io standard chain |
| `openclaw/skills/` | Dir | Secondary skills directory at OpenClaw integration scope |
| `evals/` | Dir | Evaluation infrastructure |
| `docker/` + `Dockerfile.test-installer` + `docker-compose.yml` + `docker-compose.e2e.yml` | Multi-Docker discipline | Test-installer + E2E + main compose |
| `install/` | Dir | Dedicated install scripts |
| `ragtime/` | Dir | RAG-related subsystem |
| `.translation-cache.json` | File | **CORPUS-FIRST translation-caching artifact** for 30-locale mode system |
| `bunfig.toml` | File | Bun config (corpus-extension after v84 Bun-primary OVERRIDE-retired at v96) |
| `transcript-watch.example.json` | File | Example config for transcript-watching |
| `cursor-hooks/` | Dir | Cursor-specific hooks |

**Library-vocab #12 LLM-routing artifacts**: post-CONFIRMED at v86 N=5 (NOTICE+HARNESSES+AGENTS+llms.txt+skill.json baseline); claude-mem = `.agent/` + `.agents/` + `.claude/` + `.claude-plugin/` + `.codex-plugin/` + `.windsurf/` + `cursor-hooks/` + `WARP.md` + `CLAUDE.md` + `NOTICE` + `SECURITY.md` + `openclaw/SKILL.md` + `plugin/skills/` + `openclaw/skills/` = **14-artifact presence at single subject = NEW CORPUS-RECORD** (challenges v99 cmux 8-in-product-skills baseline + v85 ui-ux-pro-max 18-platform-skill.json prior records at LLM-routing layer).

---

## Pattern #57 sub-variant 57k Standards-Conformance-Layer Chain — 7-implementer extension

Agentskills.io standard chain post-PROMOTION at v101 (N=3 with 5-implementer); v102 extended to N=4 STRONGER with 6-implementer; **v103 = N=5 STRONGEST post-PROMOTION with 7-implementer chain extension**:

| # | Wiki | Date | Subject | Vertical |
|---|---|---|---|---|
| 1 | v76 | 2026-05-19 | HoangNguyen0403/agent-skills-standard (anchor) | Standards-meta |
| 2 | v93 | 2026-05-23 | anthropics/skills (authoritative reference) | Foundational-vendor reference |
| 3 | v98 | 2026-05-25 | mukul975/Anthropic-Cybersecurity-Skills | Cybersecurity-vertical |
| 4 | v99 | 2026-05-27 | manaflow-ai/cmux | Native-terminal-multiplexer-vertical |
| 5 | v100 | 2026-05-27 | tisfeng/Easydict | Translation-utility-vertical |
| 6 | v102 | 2026-05-28 | anthropics/claude-cookbooks | Foundational-vendor reference cookbook |
| **7** | **v103** | **2026-05-28** | **thedotmack/claude-mem** | **Memory-system-vertical** |

**Arc-velocity**: 7-implementer-in-9-calendar-days (v76 2026-05-19 → v103 2026-05-28 = 9 days; arc-velocity stable not accelerating from v102 6-implementer-in-9).

**v103 conformance evidence**: `plugin/skills/` + `openclaw/skills/` + `openclaw/SKILL.md` = explicit dual-skills-directory at distribution + integration scopes.

---

## Phase 4b PRIMARY: Pattern #85 Platform-Primitive Foundation N=2 STRENGTHENING after 37-wiki gap

See: [Phase 4b PRIMARY proposal-document](../01%20Analysis/(C)%20Pattern-85-N2-STRENGTHENING-after-37-wiki-gap.md)

**Summary**: v66 agentmemory (anchor at routine v2.2 ship 2026-05-14) + **v103 claude-mem N=2 STRENGTHENING** (routine v2.3.1 ship 2026-05-28) = first N=2 STRENGTHENING evidence for Pattern #85 after 37-wiki gap = unusually long N=1→N=2 latency in T2 Service Memory-System sub-archetype = long-deferred-strengthening event worth flagging for v2.4 codification (N=1-to-N=2 latency tracking discipline).

---

## Phase 4b SECONDARY observations (held at OC layer per cascade-discipline)

1. **CORPUS-RECORD-HIGH 30-locale mode system at single subject** (exceeds v99 cmux 21-locale by ~43%) — Library-vocab PROVISIONAL N=1
2. **CORPUS-RECORD 14-LLM-routing-artifact density at single subject** (Library-vocab #12 post-CONFIRMED N=5; claude-mem N=14 = NEW CORPUS-RECORD at single-subject artifact-count)
3. **CORPUS-FIRST `WARP.md` Warp-terminal LLM-routing artifact** in v60+ window — Library-vocab PROVISIONAL N=1
4. **CORPUS-FIRST `cursor-hooks/` Cursor-specific top-level hooks directory** in v60+ window — Library-vocab PROVISIONAL N=1
5. **CORPUS-FIRST `.codex-plugin/` Codex-plugin-as-top-level-artifact** — Library-vocab PROVISIONAL N=1
6. **CORPUS-FIRST `openclaw/` harness-integration-as-top-level-package** with own SKILL.md + install scripts + Dockerfile.e2e — Library-vocab PROVISIONAL N=1
7. **CORPUS-FIRST `.translation-cache.json` translation-caching artifact** for 30-locale mode system — Library-vocab PROVISIONAL N=1
8. **CORPUS-FIRST `@Claude_Memory` product-branded Twitter handle as account-level identity** at single-subject scope — Library-vocab PROVISIONAL N=1 (observational; Pattern #19 sub-mechanism candidate at solo-developer-product-branded-account axis NOT REGISTERED per Pattern #19 graveyard pressure)
9. **Library-vocab #20 Token-Economy-Quantification N=4 STRENGTHENING** post-PROMOTION (CONFIRMED v101 N=3 with v87+v97+v98; v103 adds runtime-axis "10x token savings")
10. **Library-vocab #16 Engagement-Deficit-Extreme MEGA-scale strengthening** at 281× star-to-subscriber ratio
11. **Pattern #57 sub-variant 57k N=5 STRONGEST post-PROMOTION** via 7-implementer chain extension (see chain table above)
12. **External memory-vertical citations** (topics: mem0 + openmemory + supermemory; NOT corpus subjects but observational lineage at memory-vertical layer; v103 = parallel-not-derivative observation)
13. **Possible Pattern #52 sub-class boundary watch** at 293.5/d HIGH-NOT-EXTREME upper-edge approaching EXTREME-VIRAL >300/d threshold; v105+ trajectory watch

---

## Pilot recommendation

**Tier**: HIGH-RELEVANCE pilot Tier-1 actionable
**Cost-of-trial**: **LOW** (`npx claude-mem install` ~5 min reversible; uninstall via `npx claude-mem uninstall` + clear `~/.claude-mem/`)
**Reversibility**: STRONG (npm uninstall pattern + state directory clear)
**Direct-applicability**: **DIRECT** for Storm Bear's documented context-thrashing problem at session-pipe boundary (routine v2.3.1 at 100+ wikis in 6 months; sessions regularly exceed 100K tokens)

**Pilot ranking insertion at position #2 NEW** (between Understand-Anything v94 #1 and claude-plugins-official v95 #2 → #3; mechanism-match for documented problem):
1. Understand-Anything v94 (DIRECT vault-utility methodology-influence at corpus-structure layer)
2. **claude-mem v103 NEW** (DIRECT vault-utility memory-compression for session context; addresses documented context-thrashing)
3. claude-plugins-official v95 (MINIMUM cost-of-trial; already-installed-by-default) — DISPLACED
4. distill v97 (CLI-pipe compression utility) — DISPLACED
5. cmux v99 (DIRECT multi-session AI-agent orchestration) — DISPLACED
6. Easydict v100 (Vietnamese ↔ English translation utility) — DISPLACED
7. claude-cookbooks v102 (canonical Anthropic-authoritative cookbook patterns) — DISPLACED
8. Anthropic-Cybersecurity-Skills v98 (methodology-extraction read-only) — DISPLACED

**Recommended pilot trial path** (~10-15 min hands-on):
- `npx claude-mem install` (~3-5 min; auto-installs Claude Code plugin)
- Verify HTTP worker on port 37777
- Run 2-3 sample Claude Code sessions
- Verify memory persistence + retrieval via `mem-search` skill
- Compare token-usage profile vs baseline (10x savings claim verification)
- Reversible: `npx claude-mem uninstall` + `rm -rf ~/.claude-mem/`

**Methodology-influence Tier-1-special multi-track position UNCHANGED** at #5 (v102 last entry; v103 is workflow-pilot not methodology-influence-special since v103 uses corpus methodology rather than redefining methodology-direction).

---

## Storm Bear streak (post-v103 ship)

**35 PASS (v65-v83 + v85-v100 + v102 + v103) + 1 OVERRIDE (v84) = "35+1*"** NEW CORPUS-RECORD = first 16-consecutive milestone post-v84 OVERRIDE (extends v102's 15-consecutive milestone by 1)

**37-instance window v65-v103** = 36 PASS + 1 OVERRIDE = **97.3% INCLUDE rate** (uptick from v102's 97.22%)

**Strength categorization v65-v103**: STRONGEST × 16 + STRONG × 13 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONGEST extends lead by 3 over STRONG)

**Override-frequency**: 1-in-37 well below v2.3 redesign trigger thresholds (2-in-20 / 3-in-30)

---

## State summary post-v103 ship

- **Pattern Library**: 46 confirmed / ~25 active / 0.543 ratio UNCHANGED (Pattern #85 N=2 STRENGTHENING is sub-archetype/strengthening event, not new top-level Pattern)
- **Library-vocab CONFIRMED**: 7 UNCHANGED
- **Library-vocab PROVISIONAL**: ~83 → ~90 (+7 from v103 inventoried per cascade-discipline)
- **v105 audit batch projection**: ~6-8 from v102 + ~8-10 from v103 + carryovers = ~25-30-item batch projected HEALTHY post-promotion-cycle baseline (well below v96's 71-item CORPUS-RECORD)
- **Routine v2.3.1 sixth-execution validation CLEAN** = framework holds at 6-of-6 executions post-codification 2026-05-25 = framework-stability strong signal extending 5-of-5 from v102
