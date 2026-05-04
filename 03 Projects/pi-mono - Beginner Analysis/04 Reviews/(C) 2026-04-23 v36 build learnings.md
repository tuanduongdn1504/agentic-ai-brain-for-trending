# v36 Build Learnings — badlogic/pi-mono

**Wiki:** 36th LLM Wiki in Storm Bear corpus.
**Routine:** v2.1 execution 5 (5th v2.1-era run after claude-howto v32 / GitNexus v33 / claude-code-best-practice v34 / claude-hud v35).
**Date:** 2026-04-23
**Velocity:** ~2h 40min (YELLOW-flag overhead, within expectation; plateau preserved at 31 consecutive wikis at ~2h v6-v36).

---

## 1. What worked

- **Consolidation-forward discipline rejected 5 candidates.** Initial Phase 0.5 enumeration had 5 potential new candidates (multi-tier monorepo / Austrian regional / MCP-exclusion / `lgtm`-gate / lockstep-versioning). Discipline: 0 registered standalone. All 5 routed to strengthening existing patterns (#17 11th data point / #73 4th sub-variant / #18 counter-evidence / #69 N=2 promotion / Mario entity author-archetype). **Net new candidates at v36: 0.** Ratio preserved at 0.79:1.

- **Pattern #69 promotion-candidate triggered cleanly.** v31 registration predicted "High — likely promotes quickly." Prediction validated at v36 (+5 wikis). 69a `🤖🤖🤖` contributor-authored + 69b `lgtm`/`lgtmi` maintainer-authored = structurally-distinct sub-variants at author-side + trigger-moment + purpose axes. Criterion 2 (structurally-unambiguous-N=2) met. Promotion-candidate written into Phase 4b deliverable.

- **Primitive-count flagging 2nd run produced first YELLOW.** v35 was inaugural GREEN on narrow target (claude-hud). v36 on pi-mono primitive surface ~3-4× denser → YELLOW correctly flagged. Scope-compression decisions documented in CLAUDE.md Phase 0.9 (entity allocation, lossy-compression accepted, citing-vs-replicating policy). Discipline scaled from GREEN to YELLOW without breaking.

- **T1 N=13 sub-classification framing avoided the 13-way matrix pitfall.** Similar decision as v35 (T1 N=12 avoided matrix): at v36 chose sub-archetype introduction ("monorepo-under-single-flagship") rather than 13-way comparison. Deliverable focused at ~600 lines on a few high-value axes (sub-archetype / #69 promotion / #18 counter-evidence / #27 sub-path / primitive-count precedent).

- **Pattern #18 MCP-exclusion counter-evidence documented with discipline.** Resisted the urge to immediately refine Pattern #18 at N=1 counter-evidence; logged as observational with explicit N=2-trigger condition. Consistent with v2.1 discipline "counter-evidence at N=1 is watch, not refine."

- **Mario's libGDX founder-equity observation NOT registered as standalone.** Tempting pattern ("cross-domain founder-equity" as Pattern #27 sub-path), but N=1 Mario. Filed in Mario's entity page + noted in Phase 4b Part 4 for future N=2 watch. Consolidation-forward applied.

- **Bash tool workflow stayed clean.** Used WebFetch with targeted prompts consistently (no retry of v35's python3 failure). Probe phase efficient — ~20 min total despite 12-file source surface.

## 2. What didn't work / friction

- **Initial bash curl attempts showed schema-view not raw-view.** Three `curl | head` calls returned JSON schema descriptions instead of actual JSON content. Not a blocker (WebFetch recovered), but suggests the Bash harness/sandbox is transforming some outputs unpredictably. For routine v2.2: prefer WebFetch over `curl | parse` for JSON; use bash only for file I/O.

- **Primitive-count YELLOW classification took one manual iteration to finalize.** Initial instinct was to push for RED (single-wiki-insufficient). After reflecting on "can 4 entities cover this with lossy-compression preserving key architectural insight?" the answer was yes. YELLOW was correct. Discipline: YELLOW is the "most wikis" classification; RED should be reserved for genuinely-split-required cases (pi-mono is NOT one of those).

- **Fact-verification pre-Phase-6** — checking Pattern Library state against planned references took extra time. PATTERN_LIBRARY.md at 2050 lines is unwieldy for manual cross-check. Proposed: automated fact-verification script that validates Pattern # references in wiki output against PATTERN_LIBRARY canonical state. Note for routine v2.2.

- **Some package-level detail in pi-mono (pi-pods, pi-mom, pi-tui, pi-web-ui) is NOT deeply covered in this wiki.** This is by-design per YELLOW compression decision, but future readers may want those details. Mitigated via "cited rather than replicated" with direct README links + brief summary paragraphs inside Mario's entity page. Acceptable trade-off but documented for transparency.

## 3. Routine v2.1 mechanisms exercised at v36

| v2.1 mechanism | Status | Outcome |
|----------------|--------|---------|
| Phase 0 12-axis classification | ✅ | Full matrix populated; NEW observation axis "multi-tier-monorepo-under-single-flagship" |
| Phase 0.5 overlap pre-check | ✅ | **5 candidates considered; 0 registered standalone; 5 routed to strengthening** — text-book |
| Phase 0.5 un-stale check | ✅ | 0 un-stales (#52/#55/#45/#46 verified no match) |
| Phase 0.5 counter-evidence check | ✅ | Pattern #18 MCP-exclusion + Pattern #12 solo-heavy-governance + Pattern #22 AGENTS.md-at-solo-T1 noted |
| Phase 0.5 consolidation-forward discipline | ✅ | Austrian → strengthen #73 4th sub-variant; monorepo → strengthen #17; not-standalone |
| Phase 0.5 N=1 stale-risk flagging | ✅ (N/A — no N=1 candidates registered) |
| Phase 0.9 Storm Bear meta-entity per-wiki evaluation | ✅ | YES include; 25th consecutive (v10-v36) |
| Phase 5 fact-verification pre-Phase-6 | ✅ | Pattern Library state cross-checked; 3 pattern-# references validated in Phase 4b deliverable |
| Phase 5 PRIMITIVE-COUNT FLAGGING (2nd run, first YELLOW) | ✅ | YELLOW — 4-entity format with deliberate scope compression; precedent for future YELLOW-flagged wikis established |
| Operator-facing backlog discipline | ⚠️⚠️ | **v27 diagnostic HIGH bundle deferred 13 sessions** (v28/v29/v30/v31/v31-mini/v32/v32-mini/v33/v34/v34-action/v35/v36 + next) — **BLOCKING-RECOMMENDATION** escalated again |
| Pattern #69 promotion-path exercised | ✅ | First v2.1-era N=1 → N=2 structurally-unambiguous promotion-candidate (promotion at next mini-audit) |

## 4. Pattern Library delta at v36

### Strengthening (6 patterns, 0 status change)

| Pattern | Action |
|---------|--------|
| **#17 Ecosystem-Layer Organizations** | 11th data point; observational solo-flagship-with-monorepo-scope sub-variant (not registered pending N=2) |
| **#18 Agent Runtime Standardization** | **First T1-scale MCP-exclusion counter-evidence**; observational N=1 |
| **#19 Intellectual Lineage Archetypes** | Archetype 4 (no-lineage) 13th T1 data point |
| **#20 Solo-Scale Ceiling** | NEW ROW "solo-Austrian + monorepo + libGDX-founder-equity T1" (38.9K/8.5mo) |
| **#22 AGENTS.md as Industry Standard** | 5th+ T1 data point; AGENTS.md-at-solo-T1 refinement direction |
| **#27 Community-Viral Scale Path** | 13th data point; NEW SUB-PATH cross-domain-founder-equity observational N=1 |

### Promotion-candidate (1 pattern)

| Pattern | Current | Proposed |
|---------|---------|----------|
| **#69 Agent-PR Fast-Track Governance Protocol** (CANDIDATE v31, stale-risk flagged) | N=1 | **N=2 structurally-unambiguous via pi-mono 69b `lgtm`/`lgtmi` sub-variant. PROMOTE at next mini-audit.** |

### Observation-track additions (1 pattern)

| Pattern | Addition |
|---------|----------|
| **#73 Regional-Archetype-Registry T1 Meta-Pattern** | 4th sub-variant 73d Austrian (observational N=1-in-registry; #73 itself separately promotion-ready from v34) |

### Counter-evidence watch (2 patterns)

| Pattern | State |
|---------|-------|
| **#12 Governance-Depth Correlation** | N=2 counter-evidence (solo-heavy-governance: pi-mono + claude-hud v35). **If N=3, refinement proposed: "governance-depth correlates with maintainer-philosophy more than organization-size."** |
| **#28 Multi-Provider AI Support** | **Refinement candidate** — "native-built-in multi-provider at T1-coding-agent scope" sub-variant; defer to mini-audit |

### Retirement decisions overdue (2 patterns)

- **#45 Dual-Licensing Strategy** — stale since v29 audit; +10-threshold passed at v33; **STILL not retired at v36**. Backlog.
- **#46 Duo-Founder + Team** — stale since v29 audit; +10-threshold passed at v33; **STILL not retired at v36**. Backlog.

### Ratio post-v36

**Unchanged from post-v35:** 33 confirmed + 26 active candidates + 5 stale + 6 retired + 1 OT = 71 full / 59 active; **ratio 26:33 = 0.79:1**.

**0.16 buffer below 0.95:1 mini-audit trigger.**

## 5. Velocity analysis

| Wiki | Phase 4b routing | Primitive-count | Time |
|------|------------------|-----------------|------|
| v32 claude-howto | T1 10-way + VN-archetype | — (pre-discipline) | ~2h |
| v33 GitNexus | T4 7-way + Pattern #31 N=4 | — (pre-discipline) | ~2h |
| v34 claude-code-best-practice | T1 11-way + Pakistani | — (informal discipline begins) | ~2h |
| v35 claude-hud | T1 narrow sub-archetype + #59 N=2 | GREEN | ~2h (inaugural) |
| **v36 pi-mono** | T1 monorepo-sub-archetype + #69 N=2 | **YELLOW** | **~2h 40min** |

**YELLOW overhead:** ~20-30% over GREEN baseline (expected; scope-compression documentation tax). 31 consecutive wikis at ~2h plateau preserved (v6-v36).

## 6. Strategic decision points at v36

### 6.1 v27 diagnostic HIGH bundle

**Deferred 13 sessions** at v36. Per v2.1 operator-facing backlog discipline, this is now BLOCKING-RECOMMENDATION at 3rd consecutive escalation. Options for operator:

**Option A:** Pause v37 wiki production; execute v27 diagnostic HIGH bundle (estimated 1-2 hours depending on bundle scope)
**Option B:** Continue wiki-building; accept discipline debt accrual indefinitely (recommended only if operator has explicit reason to defer)
**Option C:** Operator-review + dismiss bundle (if no longer relevant after 13 sessions)

### 6.2 Proactive mini-audit opportunity

Ratio 0.79:1 is healthy (0.16 buffer below trigger). **Proactive mini-audit is low-ratio-cost and high-value:**
- Promote #69 (structurally-unambiguous-N=2) — ratio change 26:33 → 25:34 = 0.735:1 improvement
- Promote #73 meta-pattern-at-N=3-consolidation if operator willing (would absorb candidates, drop ratio)
- Refine #28 native-built-in sub-variant formulation
- Execute overdue retirement of #45 + #46
- Document Pattern #18 MCP-exclusion watch formally

Estimated mini-audit time: ~45-60 min.

### 6.3 pi-mono pilot evaluation for Storm Bear operator

pi-coding-agent at Storm Bear operator pilot rank #3 (NEW at v36). Recommended evaluation: 2-4 hours hands-on (documented in beginner guide Part 8). **Not urgent — secondary runtime preparedness, not primary-runtime switch.**

## 7. Corpus-wide observations at v36

### 7.1 T1 tier state

T1 at N=13 post-v36. Largest tier in corpus. Archetypes increasingly diverse:
- Broad-methodology: ECC v1 / SP v2 / gstack v3 / GSD v5 / BMAD v11 / spec-kit v17 / codymaster v12
- Mid-skill-library: agency-agents v18 / OMC v27
- Tutorial-guide: claude-howto v32 (VN-diaspora) / claude-code-best-practice v34 (Pakistani) / Everything Claude Code v1 (US)
- Narrow-display-plugin: claude-hud v35 (Australian)
- **Solo-monorepo-flagship: pi-mono v36 🆕 (Austrian)**

T1 N=13 is now "methodology battlefield" evolving into "archetype-diversity laboratory."

### 7.2 Regional archetype registry (#73) at 4 sub-variants

- 73a Korean (OMC v27) — stale-flagged v32
- 73b VN (codymaster v12 + claude-howto v32) — promoted v32 mini-audit
- 73c Pakistani (claude-code-best-practice v34) — candidate
- **73d Austrian (pi-mono v36) — new at v36**

**Pattern #73 meta-pattern itself at N=3+ regional sub-variants** → structurally ready for promotion under meta-pattern-at-N=3-consolidation criterion (proposed at v34, still deferred).

### 7.3 Solo-author-at-enterprise-scale observations

| Author | Scale | Archetype |
|--------|-------|-----------|
| msitarzewski (agency-agents) | 82.9K | Solo + 144-agent library + Reddit-viral |
| unclecode (crawl4ai) | 64K | Solo + T4 enterprise-scale-web-utility + LiteLLM |
| **Mario Zechner (pi-mono)** | **38.9K** | **Solo + 7-package monorepo + libGDX-founder-equity (NEW)** |
| safishamsi (graphify + AkonLabs) | 30K | Solo + commercial entity + knowledge-graph |
| Jarrod Watts (claude-hud) | 20K | Solo + narrow display-plugin + one-hit-flagship |
| Luong Nguyen (claude-howto) | 28K | Solo + tutorial + VN-diaspora |

Solo-at-enterprise-scale pattern has 6+ instances now. Pattern #20 Solo-Scale Ceiling continues to get validated data points. Ceiling breached multiple times without corporate backing.

### 7.4 Pattern #18 MCP-exclusion watch

Event-based observation to track:
- pi-mono v36 — first T1-scale MCP-exclusion counter-evidence
- claude-hud v35 — narrow plugin; extension-point-consumer, not MCP (tangential)

If T1 MCP-exclusion N=2 emerges within 5 wikis, refine Pattern #18 to explicit "MCP-optional layer-1 standard" framing. Otherwise observational.

---

## 8. Fact-verification pre-Phase-6

Cross-checked Pattern # references in v36 deliverables:

- Pattern #17 current state (CONFIRMED v15, REFINED v25) ✅ matches PATTERN_LIBRARY post-v25 audit entry
- Pattern #18 current state (CONFIRMED v15, REFINED v17 + v31) ✅ matches PATTERN_LIBRARY post-v31 mini-audit triple-layer formulation
- Pattern #19 archetype 4 no-lineage ✅ validated (fish-speech v20 research-paper-chain was archetype 4 introduction; extended in later wikis)
- Pattern #20 solo-scale formal statement ✅ observational-archetype-dictionary per v21 audit reformulation
- Pattern #22 AGENTS.md CANDIDATE v17 status ✅ validated (still CANDIDATE, no promotion yet)
- Pattern #27 CONFIRMED v21 status ✅ validated
- Pattern #28 CONFIRMED v25 audit N=6+ data points ✅ validated
- Pattern #59 Plugin Marketplace Native CONFIRMED-candidate (v35 strengthen to N=2) — pi-mono does NOT use marketplace (npm only) — fact check: pi-mono is not a Claude Code plugin so N/A ✅
- Pattern #69 CANDIDATE v31 N=1 stale-risk ✅ validated
- Pattern #73 CANDIDATE v34 3 sub-variants ✅ validated (73a + 73b + 73c); v36 adds 73d

**Clean. 0 fact errors pre-Phase-6.**

---

## 9. Open items for operator attention (carryover + new)

1. **v27 diagnostic HIGH bundle BLOCKING-RECOMMENDATION** — 13 sessions deferred; escalated again at v36
2. **Proactive mini-audit opportunity** — Pattern #69 promotion + Pattern #73 promotion + Pattern #28 refinement + retirements (#45/#46) — ~45-60 min if executed
3. **Pi-mono pilot evaluation** — 2-4h Storm Bear operator pilot recommended (secondary-runtime preparedness)
4. **Routine v2.2 refactor** — cumulative ~225+ action items post-v36; refactor candidacy status
5. **Pattern Library growth** — post-v36 at 71-total-items, 59-active; consider documentation-restructuring if approaches 100

---

## 10. v36 corpus-firsts

- **1st Austrian-authored framework in corpus** (Mario Zechner)
- **1st explicit T1-scale MCP-exclusion** (pi-mono deliberate design)
- **1st T1 monorepo-under-single-flagship observational sub-archetype** (7-package coordinated release)
- **1st `lgtm`/`lgtmi` maintainer-authored approval-keyword protocol** (sub-variant 69b)
- **1st cross-domain-founder-equity observation** (Mario's libGDX → pi-mono transition; N=1 observational)
- **1st explicit OSS-session-data-donation flywheel** (pi-share-hf → HF dataset)
- **1st lockstep-monorepo with 200+ releases in 8.5 months** (single-author-specific quirk; noted not patterned)
- **1st CRITICAL Git Rules for Parallel Agents** explicitly codified in AGENTS.md
- **1st first YELLOW primitive-count flagging outcome** (v35 was inaugural GREEN)
- **1st pi-ai 20+-provider unified LLM API at T1-coding-agent scope** (distinct from LiteLLM pure-abstraction; Pattern #28 refinement candidate)

---

## 11. v2.1 routine maturation state

5 v2.1-era executions complete:
1. **v32 claude-howto** — inaugural v2.1 discipline test
2. **v33 GitNexus** — consolidation discipline on T4 extension
3. **v34 claude-code-best-practice** — T1 11th entrant
4. **v35 claude-hud** — primitive-count flagging inaugural (GREEN) + #59 N=2 strengthening
5. **v36 pi-mono 🆕** — primitive-count YELLOW first + #69 N=2 promotion-candidate + MCP-exclusion counter-evidence

**Routine v2.1 is production-stable across 5 executions with 5 distinct Phase 4b modes:**
- VN-Regional N=2 promotion (v32)
- T4 N=4 structural validation + PolyForm register (v33)
- T1 11-way meta-reference (v34)
- T1 narrow sub-archetype + marketplace-plugin-native N=2 (v35)
- T1 monorepo sub-archetype + MCP-exclusion counter-evidence + #69 N=2 promotion (v36)

Velocity plateau preserved: ~2h on GREEN, ~2h 40min on YELLOW. No RED yet (reserved for genuine compression-failure).

---

## 12. Recommendation for v37 and beyond

**At v36:** operator has 3 natural next-moves:

**Option A (resolve backlog):** v27 diagnostic HIGH bundle execution. Pause wikis. Return to wikis with clean backlog.

**Option B (consolidate):** Proactive mini-audit. Low ratio cost (0.79:1 healthy). Promote #69 + #73, refine #28, retire #45 + #46. Return to wikis with improved library.

**Option C (continue):** v37 new wiki. Target selection TBD; candidates include T5 (only 5 T5 entrants, smallest validated tier) or another T3 (T3 has 2 entrants — potential for #53 Multi-Framework BYO promotion if T3 3rd observation).

**Recommended sequence:** Option B first (45-60 min) → Option A if time permits → Option C for v37.

**Do NOT recommend:** Continuing wiki production without either audit or backlog clearance for >2 more sessions (accumulating discipline debt compounds).

---

## 13. Primitive-count flagging 2nd run detailed analysis (v2.1 informal discipline)

Per v2.1 Phase 5 informal discipline introduced at session 41 (v34) + validated at v35 (GREEN inaugural), v36 is the **2nd execution** and **first YELLOW outcome**.

### 13.1 Probe execution summary

**Probe signals (6 applied):**

| Signal | Source | Count |
|--------|--------|-------|
| 1 | Root README sections | ~6 |
| 2 | Top-level repo structure | 6 dirs + 12 files |
| 3 | Monorepo packages | **7** |
| 4 | Coding-agent user surface (flags + slash + keys + tools + resources + settings) | **~110** |
| 5 | pi-ai providers | **20+** |
| 6 | Other packages' primitives | **~30+** |

**Aggregate primitive surface:** ~150-200 distinct primitives across the monorepo.

### 13.2 Density comparison with v35 (inaugural GREEN)

| Wiki | Primitive-count signal | Density | Flag |
|------|------------------------|---------|------|
| **v35 claude-hud** | ~11 README sections + ~38 config options + 2 slash commands + 4 render lines + 16 source modules | ~70 distinct primitives | **GREEN** |
| **v36 pi-mono** | ~150-200 distinct primitives (3-4× denser) | Dense | **YELLOW** |

### 13.3 Classification thresholds (empirical, 2 data points)

- **GREEN:** <100 distinct primitives (claude-hud at ~70)
- **YELLOW:** 100-300 distinct primitives (pi-mono at ~150-200)
- **RED:** >300 distinct primitives (not observed yet; reserved for genuine single-wiki-insufficient cases)

**Caveat:** Thresholds are informal / N=2 data points. Calibrate further with future wikis.

### 13.4 Scope-compression discipline applied

**YELLOW compression decisions (from CLAUDE.md Phase 0.9):**

- **4 entities with deliberate allocation:**
  1. pi-coding-agent (flagship product — primary entity)
  2. pi-ai + pi-agent-core **COMBINED** (foundation libraries — save 1 entity slot)
  3. Mario Zechner (author + ecosystem portfolio — absorbs pi-pods + pi-mom + pi-tui + pi-web-ui as brief mentions)
  4. Storm Bear meta-entity (per v2.1 Phase 0.9)

- **Lossy compression:** pi-pods / pi-mom / pi-tui / pi-web-ui do NOT get dedicated entities
- **Citing rather than replicating:** Full 25-flag + 20-slash-command + 15-keybinding + 38-setting + 20+-provider enumerations are CITED to upstream READMEs rather than duplicated

### 13.5 Velocity impact validation

- v35 GREEN: ~2h
- v36 YELLOW: ~2h 40min (expected 20-30% overhead; measured within range)

**YELLOW overhead ≈ 20-30%.** Acceptable trade-off for preserved wiki quality. Documents compression decisions for transparency.

### 13.6 Future deep-dive triggers identified

If pattern-library pressure makes these relevant:

1. **pi-ai standalone wiki** — if Pattern #28 Multi-Provider AI Support warrants native-built-in-at-T1-coding-agent sub-variant refinement at mini-audit
2. **pi-pods standalone wiki** — if GPU-inference-infra archetype emerges at N≥2

Both are deferred to future; not triggered at v36.

### 13.7 Precedent for future YELLOW-flagged wikis

**v36 precedent established:** YELLOW should explicitly document:
1. Primitive-count probe data (count + signals)
2. Density-comparison with GREEN baseline wikis
3. Compression decisions (entity allocation + lossy-compression scope + citation-not-replication scope)
4. Future deep-dive triggers
5. Velocity overhead measured

Future YELLOW wikis should follow the same template for consistency + cross-comparison.

### 13.8 Open research questions for flagging discipline

1. **Does YELLOW overhead scale linearly with primitive count?** 2 data points (GREEN ~70 / YELLOW ~175) = 2.5× density, 20-30% overhead. If 350-primitive-surface wiki emerges (near RED threshold), is overhead ~40-50%? Worth tracking.
2. **What's the RED threshold precisely?** Reserved for cases where 4-entity format cannot preserve architectural insight without critical loss. Not yet observed empirically.
3. **Is primitive-count the right complexity metric?** Could substitute "conceptual-distinct-axis count" (e.g., pi-mono has ~5 orthogonal axes: coding-agent / LLM-abstraction / agent-runtime / TUI / web-UI / Slack / GPU-infra). Alternative framing to explore.

---

*(C) Claude-generated 2026-04-23 per routine v2.1 execution 5.*
