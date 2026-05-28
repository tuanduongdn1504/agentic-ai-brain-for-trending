# Phase 0 + Phase 0.9 STRICT INCLUDE verdict — claude-mem v103

**Subject**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
**Date**: 2026-05-28
**Routine**: v2.3.1
**Verdict**: **STRONGEST INCLUDE 4/4** with (c) STRONGEST + (a)(b)(d) STRONG

---

## Phase 0: Tier classification

**Tier**: T2 Service / Memory-System sub-archetype (N=2 with v66 agentmemory)

claude-mem is a persistent memory-compression service: HTTP worker (port 37777) + SQLite FTS5 + Chroma vector DB + 5-lifecycle-hook architecture + `mem-search` skill + plugin distribution across Claude Code + Gemini CLI + OpenCode + OpenClaw. Service-shape distinct from T1 Assistant Skill or T3 Education.

**Sub-archetype**: Memory-System (v66 agentmemory anchor 2026-05-14; v103 claude-mem N=2 strengthening 2026-05-28; 37-wiki gap = unusually long N=1-to-N=2 latency in T2 sub-archetype layer).

---

## Phase 0.9: STRICT INCLUDE 4-criteria evaluation

### (a) Cultural-peer / Storm Bear-axis cluster — STRONG PASS

7-axis (a) taxonomy evaluation per routine v2.3.1 §25:

| Sub-axis | Evidence | Verdict |
|---|---|---|
| (a)-1 direct-author-peer | Alex Newman (US-inferred from English-only profile + no Vietnamese signal) | FAIL |
| (a)-2 native-language-fluency | No Vietnamese-language signal | FAIL |
| (a)-3 product-locale-inclusion | **Vietnamese (vi) locale in 30-locale mode set** (`plugin/modes/vi.md`) | **PASS** |
| (a)-4 community-org | Solo developer + 1,629 followers + 119 public repos | FAIL |
| (a)-5 multi-org-founder | Single-org solo | FAIL |
| (a)-6 cluster-extension | Location NULL on GitHub profile; no Asian-LOCATED signal | FAIL |
| (a)-7 foundational-vendor-direct-source | Not Anthropic-direct-org (Alex Newman individual) | FAIL |
| (a)-8 South-American-LOCATED | Location NULL; no signal | FAIL |

**(a)-3 strength evaluation**: Vietnamese is 1 of 30 locales = product-locale-inclusion PASS via routine v2.3.1 §24 (v78 ECC precedent + v99 cmux 21-locale precedent). v103 NEW CORPUS-RECORD-HIGH 30-locale breadth (exceeds v99 cmux 21-locale by ~43%).

**(a) verdict**: STRONG via single sub-axis support at (a)-3; STRONG not STRONGEST because single (a) sub-axis pass without cultural-peer + cluster-extension reinforcement. Comparable to v99 cmux verdict structure.

---

### (b) Cost-of-trial × functional-fit — STRONG PASS

**Cost-of-trial**: **LOW** (`npx claude-mem install` ~5 min reversible; uninstall via `npx claude-mem uninstall` + clear `~/.claude-mem/` state)

**Functional-fit**: **DIRECT** for Storm Bear's documented context-thrashing problem at session-pipe boundary
- Operator ships ~1-2 wikis/day under routine v2.3.1
- Session context regularly exceeds 100K tokens (per session-load notes in CLAUDE.md Weekly Update)
- claude-mem 10x token savings claim + 3-layer search workflow + progressive disclosure pattern = DIRECT mechanism-match to documented problem

**Existing-infrastructure-overlap**: HIGH (Claude Code daily usage + vault Markdown corpus at filesystem level)

**(b) verdict**: STRONG (LOW cost × DIRECT-applicability × HIGH overlap); STRONG not STRONGEST because memory-compression is a session-boundary utility not a single-action workflow primitive (cf. v100 Easydict 3-5-min brew install + reversible + workflow-directly-actionable).

---

### (c) Methodology-influence-node / corpus-novelty — STRONGEST PASS

**Methodology-novelty axes (multiple corpus-firsts)**:

1. **Pattern #85 Platform-Primitive Foundation N=2 STRENGTHENING after 37-wiki gap** (v66 agentmemory N=1 anchor + v103 N=2; 37-wiki gap is unusually long N=1→N=2 latency in T2 sub-archetype layer)
2. **CORPUS-RECORD-HIGH 30-locale mode system at single subject** (exceeds v99 cmux 21-locale prior record by ~43%)
3. **CORPUS-RECORD LLM-routing artifact density at single subject** (Library-vocab #12 post-CONFIRMED at N=5; v103 = `.agent/` + `.agents/` + `.claude/` + `.claude-plugin/` + `.codex-plugin/` + `.windsurf/` + `cursor-hooks/` + `WARP.md` + `CLAUDE.md` + `NOTICE` + `SECURITY.md` + `openclaw/SKILL.md` = 12-artifact presence at single subject = NEW CORPUS-RECORD challenging v99 cmux 8-in-product-skills baseline)
4. **CORPUS-FIRST `WARP.md` Warp-terminal LLM-routing artifact** in v60+ window (observational Library-vocab candidate)
5. **CORPUS-FIRST `cursor-hooks/` Cursor-specific top-level hooks directory** in v60+ window (observational Library-vocab candidate)
6. **CORPUS-FIRST `.codex-plugin/` Codex-plugin-as-top-level-artifact** in v60+ window (observational)
7. **CORPUS-FIRST `openclaw/` top-level integration directory** with own SKILL.md + install scripts + Dockerfile.e2e (CORPUS-FIRST harness-integration-as-top-level-package in v60+ window)
8. **CORPUS-FIRST hybrid SQLite FTS5 + Chroma vector DB at memory-system T2 Service scale** (architectural novelty; mem0/openmemory/supermemory cited as topic axis but not bundled = parallel-not-derivative observation)
9. **CORPUS-FIRST `.translation-cache.json` translation-caching artifact** at top-level for 30-locale mode system (corpus-novel)
10. **CORPUS-FIRST `@Claude_Memory` product-branded Twitter handle as account-level identity** at single-subject scope (corpus-novel observational; thedotmack's account literally branded as `@Claude_Memory`)
11. **Library-vocab #20 Token-Economy-Quantification N=4 STRENGTHENING** post-PROMOTION (CONFIRMED at v101 N=3; v103 = "10x token savings" claim at runtime+composition layer)
12. **Library-vocab #16 Engagement-Deficit-Extreme N+1 strengthening** at MEGA-scale 281× star-to-subscriber ratio (79,253 stars / 282 subscribers)

**(c) verdict**: STRONGEST — 12+ corpus-firsts at single subject + Pattern #85 N=2 STRENGTHENING after long-deferred gap + multiple post-PROMOTION strengthenings + CORPUS-RECORD-HIGH 30-locale + CORPUS-RECORD LLM-routing artifact density.

---

### (d) Corpus-recursive ties / methodology-influence chain — STRONG PASS

**Direct corpus-recursive ties**:

1. **Pattern #85 sub-archetype Memory-System** v66 agentmemory anchor + v103 = N=2 STRENGTHENING (cross-vendor implementers; structurally distinct memory-system designs)
2. **Pattern #57 sub-variant 57k Standards-Conformance-Layer Chain (7-implementer)** — chain extension v76 → v93 → v98 → v99 → v100 → v102 → **v103** = 7-implementer-in-9-calendar-days arc-velocity (continues unusually-fast standards-adoption arc); plugin/skills/ + openclaw/skills/ both present
3. **Pattern #57 sub-variant 57c-product 7+ corpus-subject citation density** (Claude Code v65 + Codex v62 + Gemini + OpenCode v67 + OpenClaw v82+v83 + Hermes v78 + Copilot)
4. **External memory-vertical citations** mem0 + openmemory + supermemory (NOT corpus subjects but observational lineage)
5. **Library-vocab #20 Token-Economy-Quantification N=4 STRENGTHENING** post-PROMOTION (CONFIRMED v101 with v87+v97+v98; v103 = N=4 with runtime-axis "10x token savings")

**(d) verdict**: STRONG — multiple corpus-recursive ties at sub-variant + sub-archetype + Library-vocab layers; STRONG not STRONGEST because corpus-recursive observations are post-PROMOTION strengthening + N=2 within already-registered Pattern #85, not new corpus-recursive event class.

---

## Overall verdict: STRONGEST INCLUDE 4/4

- (a) STRONG via (a)-3 PASS Vietnamese locale in 30-locale CORPUS-RECORD-HIGH set
- (b) STRONG LOW cost-of-trial × DIRECT functional-fit for documented context-thrashing problem
- (c) **STRONGEST** 12+ corpus-firsts + Pattern #85 N=2 STRENGTHENING + CORPUS-RECORD 30-locale + CORPUS-RECORD LLM-routing artifact density
- (d) STRONG corpus-recursive ties across Pattern #85 + Pattern #57 57k 7-implementer + Library-vocab #20 + #12 + #16

**Streak**: 35 PASS (v65-v83 + v85-v100 + v102 + v103) + 1 OVERRIDE (v84) = **"35+1*"** NEW CORPUS-RECORD = first 16-consecutive milestone post-v84 OVERRIDE
**INCLUDE rate**: 37-instance window v65-v103 = 36 PASS + 1 OVERRIDE = 97.3% (precise 97.30%; uptick from v102 97.22%)
**Strength categorization v65-v103**: STRONGEST × 16 + STRONG × 13 + MODERATE × 4 + WEAK × 5 + OVERRIDE × 1 (STRONGEST extends lead by 3 over STRONG)

---

## Phase 4b PRIMARY identification

**PRIMARY**: Pattern #85 Platform-Primitive Foundation **N=2 STRENGTHENING after 37-wiki gap** via Phase 4b vehicle #3 within-pattern strengthening proposal-document. v66 agentmemory anchor at routine v2.2 + v103 claude-mem N=2 under routine v2.3.1 = first N=2 evidence for Pattern #85 since registration; sub-archetype layer Memory-System now N=2 = pattern-strengthening-after-long-deferred-gap event.

**SECONDARY observations held at OC layer per cascade-discipline**:
- Pattern #57 sub-variant 57k 7-implementer chain extension (post-PROMOTION strengthening; not a registration event)
- CORPUS-RECORD 30-locale mode system at single subject
- CORPUS-RECORD LLM-routing artifact density at single subject
- 5 NEW Library-vocab candidates (WARP.md + cursor-hooks/ + `.codex-plugin/` + `openclaw/` integration-as-top-level-package + `.translation-cache.json` + `@Claude_Memory` product-branded handle)
- Library-vocab #20 Token-Economy-Quantification N=4 STRENGTHENING
- Library-vocab #16 Engagement-Deficit-Extreme MEGA-scale strengthening (281× ratio)
- mem0/openmemory/supermemory external memory-vertical citation observational track

---

## Honest dissent / caveats

- **(a) verdict could be argued WEAK-PASS rather than STRONG-PASS** because single sub-axis support at (a)-3 product-locale-inclusion is the structurally weakest (a) sub-axis (locale-presence binary not magnitude); cf. v99 cmux had identical structure and verdict was STRONG
- **(c) STRONGEST verdict load-bearing**: 12+ corpus-firsts pressure-test at v105 audit required; some claims (`.codex-plugin/`, `cursor-hooks/`, `WARP.md`, `@Claude_Memory` handle) are observational and may be downgraded if pressure-tested as ad-hoc-coined
- **(d) Pattern #57 57k 7-implementer chain**: v103 extends to N=5 post-PROMOTION at sub-variant layer; arc-velocity 7-implementer-in-9-calendar-days continues but does not accelerate further from v102 6-implementer-in-9 = arc-velocity stable not accelerating
- **Pattern #85 N=2 PRIMARY**: 37-wiki gap from v66 anchor is unusually long; v103 is first N=2 evidence in T2 Service Memory-System sub-archetype after no N=2 emergence through v76 → v85 → v90 → v95 → v100 → v101 audit cycles = long-deferred-strengthening event; v2.4 codification candidate: "N=1-to-N=2 Latency Tracking for sub-archetype-level Patterns"
- **Pattern #19 sub-mechanism candidate**: thedotmack profile (15-year-old account + product-branded Twitter handle + 119 public repos + solo-developer + MEGA-scale single project at 79K stars) does NOT cleanly fit existing Pattern #19 sub-mechanism taxonomy; NEW candidate "Solo-Developer-with-Product-Branded-Twitter-Handle at MEGA-scale" PROVISIONAL N=1 NOT REGISTERED at v103 to avoid worsening Pattern #19 graveyard (~10-11 candidates pending v105 CONSOLIDATION review)
- **Velocity at 293.5 stars/day for 270 days**: HIGH-NOT-EXTREME at upper-edge BUT approaches Multi-Month-Sustained EXTREME-VIRAL >300/d × 90+d threshold; if star-count continues current trajectory, v105 audit watch for sub-class boundary crossing
