# (C) v33 Build Learnings — GitNexus

> **Wiki 33** — Storm Bear corpus
> **Date:** 2026-04-23
> **Routine:** llm-wiki-routine-v2.1 (2nd v2.1-era execution)
> **Duration:** ~1.8 hours (within ~2h plateau)

---

## 1. Milestones hit

### Corpus-level milestones

- **33rd LLM Wiki** shipped
- **14th v2-era routine execution** (13 under v2, 2nd under v2.1)
- **T4 extends to N=7** — 2nd-largest tier continues (after T1 N=10)
- **Pattern #31 Open-Core Commercial Entity N=4** — structural validation across 4 orthogonal axes (scope / license / mechanism / entity)
- **Pattern #72 NEW candidate** — PolyForm Noncommercial Commercial-Gate License (N=1 stale-risk-flagged)
- **1st Indian-authored framework** in corpus (Abhigyan Patwari, Guwahati, Assam) — observation noted, not registered
- **22nd consecutive Storm Bear meta-entity** (per v2.1 Phase 0.9 per-wiki applicability)
- **28 consecutive wikis at ~2h velocity plateau** (v6-v33)
- **Pattern Library ratio 0.73:1 → 0.76:1** (post-v33; healthy; 0.19 buffer to mini-audit trigger)

### Framework-specific milestones (14 corpus-firsts)

1. 1st Indian-authored framework
2. 1st PolyForm Noncommercial 1.0.0 license
3. 1st CS-student author archetype
4. 1st LadybugDB embedded graph+vector DB
5. 1st browser-native knowledge-graph runtime (WASM tree-sitter + WASM LadybugDB + transformers.js + WebGPU)
6. 1st Sigstore-signed Docker deployment
7. 1st Kubernetes policy-controller admission-control documentation
8. 1st "nervous system for agent context" philosophy framing
9. 1st BM25 + semantic + RRF hybrid search in corpus
10. 1st anti-crypto disclaimer leading README
11. Most detailed 14-language capability matrix (type-annotation + constructor-inference per-language)
12. Most MCP tools per-project (16) in corpus
13. 1st bidirectional Claude Code hooks integration (PreToolUse + PostToolUse)
14. 1st cross-repo graph operations (5 group-tools primitive)

---

## 2. Phase breakdown

| Phase | Duration (est) | Notes |
|-------|---------------|-------|
| Phase 0 Pre-flight + probe | 15 min | WebFetch GitHub API + README + author profile + CONTRIBUTING + PolyForm license text |
| Phase 1 Scaffold | 5 min | Project folder + CLAUDE.md + index + log + open-questions |
| Phase 2 Source ingestion (3 clusters) | 25 min | README comprehensive fetch + CONTRIBUTING verification + SECURITY 404 confirmed + PolyForm text analysis |
| Phase 3 Entity pages (4) | 30 min | Core / MCP / Open-Core+PolyForm / Storm Bear meta |
| Phase 4a Beginner guide | 15 min | Bilingual VN+EN with PolyForm ethical framing |
| Phase 4b T4 7-way + Pattern #31 N=4 + Pattern #72 + regional observation | 20 min | Primary Phase 4b deliverable |
| Phase 5 Iteration log (this file) | 5 min | In progress |
| Phase 6 Vault sync + fact-verification | 5 min | Pending |
| **Total estimated** | **~1.8h** | **Within ~2h plateau** |

---

## 3. What worked

### Discipline mechanisms (v2.1 systematic exercise)

1. **Overlap pre-check** — Proposed Pattern #72 PolyForm distinguished from Pattern #29 (category-diversity descriptive) / Pattern #33 (custom-non-OSI) / Pattern #45 (dual-licensing) / Pattern #31 (parent pattern). Clean registration without overlap.

2. **Un-stale check** — All negative (5 checks: #45 / #46 / #52 / #55 / no retired revivals). Disciplined no-false-positives.

3. **Counter-evidence check** — Pattern #17 variant observation (single-flagship-with-commercial vs ecosystem-portfolio variants); Pattern #22 AGENTS.md T4 absence continuation. Noted for future audit; not forcing refinement in current wiki.

4. **Consolidation-forward discipline** — Indian regional observation NOT registered as pattern (cross-tier premature). Browser-native knowledge-graph runtime NOT registered (too niche, single observation). Only Pattern #72 registered. Conservative budget: 1 new candidate vs 2-3 budget.

5. **N=1 stale-risk-flagging** — Pattern #72 registered with stale-risk-flag. +5 trigger (v38) + +10 retirement (v43) documented.

### Velocity preservation

- 28 consecutive wikis at ~2h plateau. Routine v2.1 discipline mechanisms (overlap pre-check, un-stale check) add ~5 min Phase 0.5 time but save ~15 min Phase 5 (prevent registering-then-retracting candidates).
- Net velocity: neutral to positive.

### Template reuse

- CLAUDE.md template from claude-howto v32 (first v2.1-era) — structural elements directly reusable
- Phase 4b T4 N-way comparative structure from markitdown v28 (T4 5-way) + crawl4ai v29 (T4 6-way) — proven format
- Pattern #31 Open-Core analysis approach from OpenHands v30 (N=3 data point) — structural pattern-validation deliverable proven

### Fact verification

- Pattern #72 distinct from #29 + #33 + #45 verified by reading existing pattern statements
- Pattern #31 N=4 data points verified by cross-checking fish-speech v20 / Skyvern v24 / OpenHands v30 wiki files
- PolyForm license text verified via polyformproject.org direct fetch (not from README paraphrase)

---

## 4. What didn't work / friction

### Minor friction

1. **SECURITY.md 404** — had to verify absence explicitly; minor backtrack in Cluster 2 narrative to acknowledge inconsistency between sophisticated Sigstore supply-chain tooling vs absent vulnerability-disclosure documentation.

2. **"16 MCP tools" discrepancy** — README says 16 but only 12 explicitly named (7 per-repo + 5 group). "4 additional" implied (context / resources / prompts / skills). Documented as likely rounded/collective, not forcing specific-name enumeration.

3. **akonlabs.com not fully probed** — only referenced, not deep-fetched. Team size / pricing / funding not verifiable without commercial contact. Documented as "Unknown" in multiple places. Future wiki could deep-probe akonlabs if 2nd Indian-regional observation emerges.

4. **Indian regional observation — decision-friction** — consolidating cross-tier Indian observation with T1-specific Korean (#55) + VN (#70) patterns required careful framing. Decided against registration; wrote extensive Part 6 of Phase 4b deliverable to document rationale. Future meta-pattern #73 Regional-Archetype-Registry deferred appropriately.

### Recurring issues

1. **v27 diagnostic HIGH bundle backlog** — now deferred **9 sessions** (v28/v29/v30/v31/v31-mini/v32/v32-mini/v33). Applied BLOCKING-RECOMMENDATION tag in multiple places (CLAUDE.md / Entity 4 meta / Phase 4b Part 9). Operator action required.

---

## 5. Routine v2.1 action items (for next version v2.2 if emerges)

### NEW items from v33

1. **WebFetch schema-response fallback protocol** — initial probe returned JSON schema definitions instead of data when `curl`-style bash command tried to parse API. Resolution was switching to WebFetch tool with specific prompt. Document as Phase 0 bash-vs-WebFetch decision guideline.

2. **License-standardization vs custom distinction discipline** — when registering license-related candidates, explicit distinction between custom-written (fish-speech) vs standardized-family (PolyForm, AGPL, CC0) improves pattern granularity.

3. **Cross-tier regional observation non-registration protocol** — when regional pattern would be first cross-tier observation but established patterns (#55/#70) are tier-specific, explicitly defer to meta-pattern-consolidation. Document in narrative; do not inflate library.

4. **Commercial-entity maturity observation lens** — akonlabs.com (GitNexus) vs All Hands AI (OpenHands) vs 39 AI, INC (fish-speech) observation suggests commercial-entity MATURITY affects OSS governance depth. Could be candidate for meta-pattern at next audit if more data points emerge.

5. **T4 tier archetype-variant count tracking** — T4 now N=7 with 7 distinct variants. Document in Phase 0 tier-state note for next T4 wiki.

6. **Knowledge-graph tool proliferation observation** — corpus now has 2 knowledge-graph tools (graphify v16 + GitNexus v33) + 1 web-content-graph peer (crawl4ai v29). Could be emerging sub-genre at T4. Watch for 3rd observation as candidate trigger.

### Cumulative action items (running counter from v3)

- **~213 total cumulative action items** (205 cumulative through v31 + 8 new at v32 + 6 new at v33 = ~219 pre-claudehow refinement; estimate now at ~219)
- **Within v2.1 budget** (no hard-block threshold; action-backlog hard-block at >100 is about ROUTINE refactor urgency, not pattern actions)

---

## 6. Meta-observations

### Pattern Library maturity

- **33 confirmed + 25 active candidates + 5 stale + 6 retired + 1 observation-track = 70 full**
- **33 confirmed patterns** = substantial structural asset
- **Ratio 0.76:1** (0.19 buffer from 0.95:1 mini-audit trigger) = healthy
- Pattern identification + consolidation + discipline continue operating in balance
- **No urgent audit needed** at v33 — first wiki in several where no audit trigger approached

### Corpus state discipline

- **5/5 tier validation preserved** (v26 milestone intact)
- **T1: 10 / T2: 2 / T3: 2 / T4: 7 / T5: 5 / Outside-scope: 7** — diversity healthy
- **Post-v26 "corpus application phase"** continues — patterns applied, not just accumulated
- **v33 is 8th wiki post-tier-completion milestone** — pattern-strengthening dominant mode

### Routine v2.1 validation

- 2nd v2.1-era execution cleanly exercises all 5 discipline mechanisms
- v32 (claude-howto) set pattern for v2.1 discipline application
- v33 (GitNexus) reinforces the pattern — overlap pre-check + consolidation-forward are now habituated

### v27 diagnostic HIGH bundle escalation

- 9 sessions deferred as of v33
- BLOCKING-RECOMMENDATION status per v2.1 operator-facing backlog discipline
- Operator attention required before v34

---

## 7. Unique findings

### PolyForm Noncommercial 1.0.0 as mainstreaming signal

- Standardized non-OSI license family (polyformproject.org) gaining acceptance at 28.5K scale
- Signals OSS ecosystem maturing toward explicit commercial-gating strategies (not just custom legal writing like fish-speech research-license)
- May indicate PolyForm family adoption trajectory — watch for 2nd observation in next 5-10 wikis

### Pattern #31 Open-Core Commercial Entity structural robustness

- N=4 across 4 orthogonal axes = pattern is robustly CONFIRMED
- 4 license strategies (custom / AGPL / MIT+dir / PolyForm) well-characterize open-core economics
- Future data points will refine sub-taxonomies (not challenge pattern validity)

### Indian-at-T4 as cross-tier regional anchor

- 1st Indian-authored framework; at T4 not T1 (where #55 Korean + #70 VN established)
- Establishes that regional-archetype observation crosses tiers
- Meta-pattern #73 Regional-Archetype-Registry deferred waiting for (a) 2nd Indian observation OR (b) 3rd region with multi-entrant across tiers

### Tool-lineage archetype continuation

- GitNexus cites no individual-author lineage (unlike Karpathy / John Lam / Boris Cherny via claude-howto v32)
- Tree-sitter + LadybugDB + Graphology + transformers.js + Sigma.js + MCP = tool-only lineage
- Consistent with Pattern #19 archetype 4 (no-lineage observed at agency-agents v18)

### Bidirectional Claude Code hooks as architectural primitive

- 1st corpus framework USING hooks (not just teaching/documenting)
- PreToolUse + PostToolUse enables real-time graph accuracy
- Claude Code exclusive — differentiates from 4 other editor integrations

---

## 8. Corpus-firsts (14 new at v33)

1. Indian-authored framework
2. PolyForm Noncommercial 1.0.0 license
3. CS-student author archetype
4. LadybugDB embedded graph+vector DB
5. Browser-native knowledge-graph runtime
6. Sigstore-signed Docker deployment
7. Kubernetes policy-controller admission enforcement docs
8. "Nervous system for agent context" philosophy framing
9. BM25 + semantic + RRF hybrid search
10. Anti-crypto disclaimer leading README
11. Most-detailed 14-language capability matrix
12. 16 MCP tools per-project (corpus-most)
13. Bidirectional Claude Code hooks (PreToolUse + PostToolUse)
14. Cross-repo graph operations (5 group-tools primitive)

---

## 9. Storm Bear vault impact

### Observations

- Storm Bear meta-entity 22nd consecutive (v2.1 Phase 0.9 applicability assessed positive)
- GitNexus direct vault use = NOT a fit (code-only tree-sitter; not markdown-friendly)
- graphify v16 remains preferred vault knowledge-graph tool (MIT, markdown-friendly)
- Pattern #31 N=4 license strategies = operator learning asset if Storm Bear ever monetizes tooling

### Pilot ranking update

Post-v33 pilot ranking:
1. spec-kit v17
2. OMC v27
3. BMAD v11
4. markitdown v28
5. crawl4ai v29
6. graphify v16
7. gws v13
8. codymaster v12
9. multica v15
10. agency-agents v18
11. **GitNexus v33** (new; lowest due to markdown-vault mismatch + PolyForm commercial-gate)

### Operator decision tree for PolyForm usage

Documented in GitNexus Entity 3 + Entity 4 + Phase 4a guide:
- Personal exploration = free
- Paid Scrum consulting = commercial license required
- Email founders@akonlabs.com for commercial tier

---

## 10. Next wiki candidates

### Priority-ordered options

1. **HIGH — BLOCKING:** Execute v27 diagnostic HIGH bundle (9 sessions deferred; operator-facing backlog now at critical level)
2. **MEDIUM:** 2nd Indian framework observation (Bangalore/Hyderabad/Pune OSS; watch for emerging)
3. **MEDIUM:** 2nd PolyForm-family adoption (Pattern #72 un-stale trigger; any variant — Shield / Small Business / Strict etc.)
4. **MEDIUM:** Next Pattern #31 data point (5th would refine 4-axis taxonomy stability)
5. **LOW:** T4 or T1 wiki without strong pattern-validation purpose (corpus structurally complete)

### Strategic decision point

**v27 diagnostic HIGH bundle NOW CRITICAL.** 9 sessions deferred. BLOCKING-RECOMMENDATION tag per v2.1 operator-facing backlog discipline. Next session should prioritize execution over accumulating more wikis.

---

## 11. Scorecard

| Metric | Score | Evidence |
|--------|-------|----------|
| **Novelty** | 8/10 | 14 corpus-firsts; T4 7th archetype variant; PolyForm license introduction |
| **Pilot-relevance** | 3/10 | #11 pilot ranking — lowest; markdown-vault mismatch + commercial-gate |
| **Pattern-contribution** | 8/10 | Pattern #31 N=4 validation across 4 axes + Pattern #72 NEW + 6 strengthening |
| **Velocity** | 9/10 | 1.8h within plateau; all v2.1 disciplines exercised cleanly |
| **Quality** | 9/10 | 13 files created + PolyForm analysis deep + fact-verification implicit throughout |
| **Composite** | **~7.4/10** | Strong pattern-contribution + novelty; low pilot-relevance |

**Net assessment:** High pattern-contribution wiki. Low operator-pilot relevance by archetype (code-only + PolyForm gate). Appropriate balance for post-tier-completion corpus-application phase.

---

## 12. Fact-verification pre-Phase 6

### Pattern number references in wiki files — checking against PATTERN_LIBRARY.md

Patterns referenced in v33 wiki files:
- #8 Research-Benchmark (correct; CONFIRMED v5)
- #9 Multi-Axial Tier Bifurcation Resolution D (correct; CONFIRMED v16)
- #12 Governance Depth Correlates with Organization (correct; CONFIRMED v13)
- #17 Ecosystem-Layer Organizations (correct; CONFIRMED v15)
- #18 Agent Runtime Standardization (correct; CONFIRMED v15)
- #19 Intellectual Lineage (correct; CONFIRMED v18)
- #20 Solo-Scale Ceiling Dictionary (correct; CONFIRMED v21, reformulated)
- #22 AGENTS.md Industry Standard (correct; CONFIRMED v17)
- #23 AI-Disclosure Policy (correct; RETIRED v27 audit)
- #24 SECURITY.md T1 Standard (correct; CONFIRMED v18)
- #27 Community-Viral Scale Path (correct; CONFIRMED v21)
- #28 Multi-Provider AI Support (correct; CONFIRMED v25)
- #29 License-Category Diversity (correct; CONFIRMED v21)
- #31 Open-Core Commercial Entity (correct; CONFIRMED v24, N=3 at v30)
- #33 Non-OSI Custom License (correct; candidate)
- #42 Academic-Published Peer-Reviewed (correct; CONFIRMED v31 mini-audit)
- #44 Academic-Lab Affiliation (correct; CONFIRMED v31 mini-audit)
- #45 Dual-Licensing Strategy (correct; STALE v29)
- #46 Duo-Founder (correct; STALE v29)
- #50 Commercial-Funnel Companion Platform (correct; CONFIRMED v31 mini-audit)
- #52 Extreme-Viral-Velocity (correct; STALE v31 mini-audit)
- #55 Korean Regional Archetype T1 (correct; STALE-FLAGGED v32 mini-audit)
- #56 Multi-Runtime Orchestration (correct; candidate v27)
- #66 Supply-Chain Security Incident Response (correct; OBSERVATION-TRACK v29 audit)
- #69 Agent-PR Fast-Track Governance (correct; candidate v31)
- #70 VN-Regional-Archetype T1 (correct; CONFIRMED v32 mini-audit)
- #72 PolyForm Noncommercial Commercial-Gate License (NEW v33 registration)

**All references verified consistent with PATTERN_LIBRARY.md post-v32-mini-audit state.**

### Cross-wiki references verified

- graphify v16 ✓
- crawl4ai v29 ✓
- markitdown v28 ✓
- fish-speech v20 ✓
- Skyvern v24 ✓
- OpenHands v30 ✓
- claude-howto v32 ✓
- Everything Claude Code v1 ✓
- gws v13 ✓
- notebooklm-py v7 ✓
- TrendRadar v19 ✓
- awesome-mcp-servers v31 ✓
- oh-my-claudecode v27 ✓
- codymaster v12 ✓

**All sibling wiki references verified.**

### Counts verified

- 33 confirmed patterns pre-v33 (post-v32 mini-audit state) ✓
- 24 active candidates pre-v33 ✓
- 5 stale ✓
- 6 retired ✓
- 1 observation-track ✓
- 69 full total pre-v33 ✓
- 0.73:1 ratio pre-v33 ✓
- Post-v33 projection: 33 confirmed + 25 active + 5 stale + 6 retired + 1 OT = 70 full; 25:33 = 0.76:1 ✓

**All counts consistent.**

---

## 13. Summary

v33 GitNexus wiki: 13 new files created (1 CLAUDE.md + 1 index + 1 log + 1 open-questions + 3 clusters + 4 entities + 1 beginner guide + 1 Phase 4b + 1 iteration log = 13 files ✓).

Pattern Library: 1 new candidate (#72) + 1 new row Pattern #20 + 6 strengthening + 0 un-stale + 0 promotions.

Velocity: 1.8h (within plateau).

Discipline: all 5 v2.1 mechanisms exercised cleanly.

v27 diagnostic HIGH bundle: 9 sessions deferred; BLOCKING-RECOMMENDATION.

**Status: DONE_WITH_CONCERNS** (backlog escalation) — ready for Phase 6 vault sync.
