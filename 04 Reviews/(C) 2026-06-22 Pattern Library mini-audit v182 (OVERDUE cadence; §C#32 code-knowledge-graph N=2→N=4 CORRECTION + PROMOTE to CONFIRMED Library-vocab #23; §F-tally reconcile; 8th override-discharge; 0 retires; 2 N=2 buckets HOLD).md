# (C) Pattern Library mini-audit v182 — 2026-06-22

**Trigger:** OVERDUE natural cadence. Last audit = v167 (2026-06-16); the v167 doc set "next natural audit ~v171–v172." We are at **v181**, ~10 ships past due (v168–v181 all shipped without an audit). Run as a **dedicated audit session** (operator-elected, not bolted onto a ship), on branch `wiki/audit-v182` off `main` (= v181, 61ade7b). Window: **v168 → v181** + the accumulated deferred agenda.

**Discipline:** every collision / prior-instance / identity claim verified BY HAND (grep over `_state/*.md` + `_patterns/*.md`), per `feedback_wiki_verify_independently_check_collisions`. No subagent/workflow used for judgment. Count changes proposed for operator sign-off BEFORE any write; sign-off received 2026-06-22 (§C#32 → PROMOTE #23; both HOLD calls accepted).

---

## 0. Triggers (verified)

- **Count/ratio triggers NOT firing.** Active candidates ≈29, confirmed top-level patterns 46 → ratio ≈0.63 (well under the 0.95 trigger); active count 29 (just under the 30 trigger). The v168→v181 run is uniformly NO-MINT for top-level patterns ("max #85, counts unchanged").
- **This audit is cadence-driven** (overdue), not trigger-driven.
- ⚠️ **Maintenance flag:** `_patterns/03-active-candidates.md`'s header is frozen at a **v78 snapshot** (29 active / ratio 0.644 / 45 confirmed). Per-ship narrative moved to `_state/03c` + `_patterns/05` long ago, so the header is no longer the live tracker; a one-line "header frozen — see audit docs + registry" banner added at v182. Not load-bearing for this audit.

---

## 1. 🔴 HEADLINE — §C#32 code-knowledge-graph standalone was materially UNDER-COUNTED → CORRECTED N=2→N=4 → PROMOTED to CONFIRMED Library-vocab #23

**The error.** The v172 mint of "Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP" recorded **"N=2; codegraph v70 was the FIRST instance."** That is a **collision-miss** — the kind the verify-don't-confabulate discipline exists to catch. Surfaced by the cortex-hub v181 ship's own flag ("GitNexus v33 + graphify v16 PREDATE codegraph v70 — flagged, deferred").

**Verification (by hand, grep over `_state/04-projects-v30-v39.md` + `_state/05-projects-v1-v29.md`):**
- **graphify v16** — *"code → knowledge graph → Claude Code,"* and *"ships MCP server as first-class output → direct plug into Storm Bear Claude Code."* Graph-based code-knowledge-graph, MCP, for a coding agent. ✓
- **GitNexus v33** (`abhigyanpatwari/GitNexus`) — *"Indexes any codebase into a knowledge graph … exposes it through smart tools so AI agents never miss code"*; **16 MCP tools**; 5 agent platforms incl. Claude Code. Graph-based, MCP, for agents. ✓
- **The v33 entry's OWN text** already classified a *"CODE-INDEXING SUB-TAXONOMY … graphify v16 + GitNexus v33 graph-based + claude-context v40 vector-based … formal registration DEFERRED pending N=4."* The corpus recognized this family at v40 and deferred it pending N=4 — that condition is now MET by the graph instances.

**The correction.** §C#32 = **N=4**, anchored **graphify v16 → GitNexus v33 → codegraph v70 → codebase-memory-mcp v172**. Cross-author (4 distinct authors), multi-year (v16 → v172). codegraph v70 was **not** first; it was third, by 37–54 wikis.

**Scope discipline (anti-over-reach):** GRAPH-based only. **claude-context v40 is the VECTOR-based sibling** (embeddings/semantic search, not a knowledge graph) — a DISTINCT retrieval architecture, **NOT counted** in #23. Counting it would be the generalize-to-fit error.

**Possible 5th instance:** v94 Understand-Anything (codebase → knowledge graph) — **flagged, NOT asserted**; whether it is MCP-queried-by-agents needs a dedicated read. Firm claim stays N=4.

**No double-count:** cortex-hub v181 re-uses GitNexus v33 as a vendored dependency → adds NO new instance (N stays 4). The capability standalone (#23) and Pattern #18 B1-MCP (distribution structure) are different axes — both recorded, no double-count (the v140/v172 precedent).

**ACTION (signed off): PROMOTE to CONFIRMED Library-vocab #23.** Clears the routine §2 bar cleanly (N=4 cross-author + multi-year + a corpus-self-recognized recurring capability). **CONFIRMED Library-vocab 10 → 11.** Top-level patterns UNCHANGED (46). Recorded in `_patterns/06` §A (#23) + §C#32 marked PROMOTED-OUT (provenance retained) + §F count refreshed.

---

## 2. Judgment calls — both HOLD (signed off)

### 2a. Cited-to-Subject Elevation (§C, N=2) — HOLD at N=2
Kilo Code v177 is a candidate **3rd sub-flavor** (*cited-as-supported-harness*: it appeared only as a name in support matrices — ui-ux-pro-max v85 / agentmemory v66 / codebase-memory-mcp v172 / OpenSpec — before becoming a v177 subject). But a **support-matrix name-drop is a materially weaker kind of prior-appearance** than the existing two instances (v93 = cited as a *methodology source* the corpus then studied; v135 = vendored as a *code dependency* another subject adopted). If a passing mention counts, nearly every subject qualifies and the pattern loses meaning. → **HOLD at N=2** (the "don't generalize-the-definition-to-fit-the-3rd-instance" discipline — the v158/v162 caution). Kilo Code recorded as a **watched** candidate 3rd sub-flavor.

### 2b. Disclosed-indie-builder (a)-axis, now N=3 — KEEP operator-reviewable, do NOT register
Three disclosed solo indie builders FAILed (a) but disclosed more than a bare handle: Waishnav (v171 devspace) / Neo Reid (v174 Agent-Reach) / Jack Le (v181 cortex-hub). At N=3 the QUESTION is confirmed-recurring. But registering "disclosed solo indie developer building in public" as an (a) cultural-peer axis would **re-open the (a)-rescue channel** for future off-goal indie repos — the exact intake door standing rec (i)/(ii) is trying to NARROW. And all three were GOAL-ALIGNED via (b) STRONG anyway, so registering changes no past verdict. → **KEEP operator-reviewable, NOT registered.** Standing rec (ii) holds; the question is now logged at N=3 (was N=2 at v174).

---

## 3. Clean HOLDS / discharges (no count change)

- **Two deferred N=2 buckets HOLD** — no clean 3rd in v168–v181:
  - **Session-multiplexer species** (cmux v99 + AoE v162) — none of v168–v181 HOSTS human-driven agent sessions in panes. HOLD N=2.
  - **Multi-Vendor Orchestration Platform** (§C, Paseo v150 + ai-maestro v163) — PilotDeck v175 is its OWN runtime using model providers (not an orchestrator of third-party agents); cortex-hub v181's "Conductor" is EXPERIMENTAL scaffolding; Kilo Code v177's Orchestrator is a mode inside an IDE agent. None qualifies. HOLD N=2. PROMOTION-ELIGIBLE at a genuine N=3.
- **§39 / §28.3 auto-retire: ZERO retires.** The entire v132→v178 N=1 standalone cohort is **<30 days old** (the v126–v178 June burst). At 2026-06-22, the 30-day floor reaches back to 2026-05-23; the earliest unretired N=1 (Open Comparative Benchmark v132) is ≈2026-06-01. The 15-wiki ceiling is met for the older ones, but the rule requires BOTH ≥15 wikis AND ≥30 days. The 30-day floor protects every one — exactly the burst-cadence calibration §39 was adopted for. NO retires.
- **Override-review: DISCHARGED (8th time).** v153→v181 = **zero operator overrides** across 28 ships. The 2-in-20 / 3-in-30 override-frequency trigger is not firing. Lifetime overrides = 10 (last = v152). Common cause unchanged (intake-channel, not a Phase-0.9 criteria defect); no 4th governor, no criteria redesign.
- **§35 soft off-goal-rate ceiling: CLEAR.** 28 consecutive goal-aligned ships v153→v181 (under the GLM-5-GA reading). Rolling-3 window {v179 GA, v180 GA, v181 GA} = 0 OG.
  - *Open label (operator-settled):* GLM-5 v176 counts GA per operator direction; the defensible OFF-GOAL reading → GA:42·OG:12. Left as GA unless re-read.
- **Pattern #18 sub-archetype B / B1-MCP** — instance-strengthening only: agentmemory v66 / codegraph v70 / nature-skills v119 / supermemory v132 / google_workspace_mcp v140 / financial-services v141 / Scrapling v149 (N=7 at v151) + devspace v171 + codebase-memory-mcp v172 + **cortex-hub v181 (one endpoint, 6 clients) = N=10**. Confirmed sub-archetype since the v72 audit; the B1→own-sub-archetype split was DECLINED at v151. The stale "#18 sub-mechanism B promotion deferred" line is **confirmed struck** (no pending promotion). Tracked at the `02b` layer.
- **GLM-5 v176 "model / inference-substrate" tier (N=1): DEFER.** No new tier at N=1; revisit if a 2nd frontier-model-as-subject appears. (GLM-5 = first frontier-LLM subject; NOT first model-subject — fish-speech [TTS] preceded.)
- **Pattern #68 "(d) AI-engineering field-map" sub-type (v170):** within-pattern sub-flavor → recorded inside #68, **no count change**.

---

## 4. v168→v181 ship-window verification (the §C standalones filed this window)

All filed correctly in `_patterns/06` §C and consistent with their per-ship entries:
- v168 ponytail — Quantified Anti-Over-Engineering / Code-Minimalism Ruleset (N=1) ✓
- v169 SkillSpector — Defensive-Security Scanner for the Agent-Skills Ecosystem (N=1) ✓
- v171 devspace — Self-Hosted MCP Bridge (hosted-host → local coding agent) (N=1) ✓
- v172 codebase-memory-mcp — [the §C#32 row → now corrected to N=4 + PROMOTED to #23] ✓
- v173 claude-tap — Agent Protocol Inspector (N=1) ✓ (adjacency cross-ref to observability sub-archetype, NOT an instance — confirmed correct)
- v174 Agent-Reach — Multi-Platform Web/Social Read+Search Capability Layer (N=1) ✓
- v175 PilotDeck — Self-Contained Agent OS / WorkSpace Isolation + white-box memory (N=1) ✓
- v177 Kilo Code — Open-Source IDE-Embedded Multi-Model Coding-Agent Platform (N=1) ✓
- v178 SkillOpt — Text-Space Skill Optimizer (N=1) ✓
- v179 camofox-browser — Anti-Detect / Stealth Browser (N=2, anchors CloakBrowser v69) ✓
- v176 GLM-5, v180 telegram-assistant, v181 cortex-hub — NO MINT (corpus-knowledge / dependency data-points) ✓

inflation_check: discipline HELD across the window — every NO-MINT was a NO-MINT, the two N=2 re-anchors (codebase-memory-mcp v172, camofox v179) were filed at honest N=2 not N=1 over-claims, and the §28 ≤2-standalone cap was never breached.

---

## 5. State after v182

| Field | Before (v181) | After (v182) |
|---|---|---|
| Confirmed top-level patterns | 46 | **46 (unchanged)** |
| CONFIRMED Library-vocab | 10 | **11** (+#23 code-knowledge-graph) |
| Tracked clusters | 7 | 7 |
| Live §C standalones | 29 | **28** (−1 promoted-out to §A #23) |
| Tracked PROVISIONAL surface | ≈36 (7+29) | **≈35 (7+28)** |
| #18 B1-MCP instances | N≈9 | **N=10** (+cortex-hub) |
| Streak | GA:43 · OG:11 [7 ov] | **unchanged (audit ≠ ship)** |
| §35 ceiling | CLEAR | CLEAR |
| Routine | v2.6 CURRENT | v2.6 CURRENT (no change) |

**Shim counts to update: "46/10" → "46/11"; §C surface "≈36" → "≈35".**

---

## 6. Carry-forward / still-open (for the next audit ~v186+)

- **§C#23 possible 5th instance v94 Understand-Anything** — verify whether it is MCP-queried-by-agents; if yes, N=4→N=5 (does not change CONFIRMED status).
- **Standing recs (i)/(ii)** — off-goal-intake lever + (a)-rescue tightening — remain PENDING operator sign-off (held de-facto v159→v181). The disclosed-indie-builder (a) question is now logged at N=3.
- **Two N=2 buckets** (session-multiplexer, orchestration-platform) — promotion-eligible at a genuine N=3; still HOLD.
- **Cited-to-Subject Elevation** — Kilo Code recorded as a watched weak-3rd sub-flavor; revisit if a stronger 3rd appears.
- **`_patterns/03-active-candidates.md` header** — frozen at v78; refresh or formally supersede at a future housekeeping pass (banner added at v182).

**Audit clean: 0 fabrications propagated, 1 verified corpus-fact error corrected (§C#32 N=2→N=4), 1 promotion (#23), 0 retires, both HOLD calls signed off.**
