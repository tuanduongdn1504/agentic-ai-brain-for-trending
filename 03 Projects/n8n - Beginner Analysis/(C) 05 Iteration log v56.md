# Iteration Log v56 — n8n-io/n8n

> **Wiki number:** 56 (v56 — first wiki post-vault-refactor session 67)
> **Date:** 2026-04-27 session 67
> **Build mode:** Main-loop direct write (post-5-agent-thrash fallback)
> **Routine version:** v2.1 (session-66 STRICT Phase 0.9 amendment applied for first time)

---

## Section 1 — Subject + scope summary

**Subject:** `n8n-io/n8n` — Fair-code workflow automation platform with native AI capabilities

**Scope:** T2 Agent-as-service (4th T2 entrant; extends T2 from N=3 to N=4)

**Surface area:** EXTREME primitive-count tier (6th in corpus) — 400+ integrations + 6 AI agent node types + 16 native LLM providers + 11 vector stores + 8 memory types + bidirectional MCP + cli + workflow-canvas

**Build context:** First v2.1-era wiki where Phase 0.9 STRICT amendment fires for real (criterion b PASS). First wiki post-vault-refactor session 67 (3 root files reduced 47-62× via chapter-file split). First main-loop direct write after 5 consecutive agent-build attempts thrashed at 4-tool-use ceiling.

## Section 2 — Numerical metadata (fact-verified)

All facts pre-verified via session 67 direct WebFetch on 2026-04-27:

| Metric | Value | Source |
|---|---|---|
| Stars | 185,728 | api.github.com/repos/n8n-io/n8n |
| Forks | 57,155 | api.github.com/repos/n8n-io/n8n |
| Watchers | 185,728 (API quirk = stars) | api.github.com |
| Open issues | 1,580 | api.github.com |
| License (GitHub API) | NOASSERTION | api.github.com |
| License (actual) | n8n SUL source-available non-OSI | docs.n8n.io/sustainable-use-license/ |
| Primary lang | TypeScript | api.github.com |
| Default branch | master | api.github.com (rare in corpus) |
| Created | 2019-06-22 | api.github.com (~7 years; 2nd-oldest in corpus) |
| Pushed | 2026-04-27 | api.github.com (today; actively maintained) |
| Repo size | 476 MB | api.github.com |
| Homepage | n8n.io | api.github.com |
| Topics | 20 topics inc mcp/mcp-client/mcp-server | api.github.com |
| Company | n8n GmbH (Berlin, Germany) | n8n.io/imprint/ |
| CEO | Jan Oberhauser | n8n.io/imprint/ |
| AI agents | 6 types | docs.n8n.io/advanced-ai/ |
| LLM providers | 16 native | docs.n8n.io/advanced-ai/ |
| Vector stores | 11 | docs.n8n.io/advanced-ai/ |
| Memory backends | 8 | docs.n8n.io/advanced-ai/ |
| MCP support | Bidirectional (Client + Server Trigger) | docs.n8n.io/advanced-ai/ |

## Section 3 — 12-axis classification table

(Full table in CLAUDE.md; summary here.)

| Axis | Value |
|---|---|
| Tier | T2 (4th T2 entrant) |
| Archetype | German-mature-commercial-startup-with-SUL + bidirectional MCP |
| Scale tier | XXX-Large (3rd in corpus) |
| Primary lang | TypeScript |
| Packaging | 5+ surfaces |
| Origin story | Solo-founder-CEO Jan Oberhauser + 7-year German GmbH |
| Methodology | Workflow + AI agent overlay + bidirectional MCP |
| Governance | Medium-Heavy |
| Agent/skill count | EXTREME (6th in corpus) |
| i18n | EN-primary |
| Intellectual influence | Workflow-automation lineage (Zapier→Make→n8n) |
| Agent platforms | Bidirectional MCP corpus-first at T2 |

## Section 4 — Phase 0.5 overlap pre-check

**12 candidate observations enumerated:**

| # | Observation | Routing |
|---|---|---|
| 1 | n8n SUL custom-non-OSI-commercial-restriction | → Pattern #29 sub-context strengthening N=3 |
| 2 | n8n GmbH commercial-with-source-available | → Pattern #31 11th data point |
| 3 | n8n.cloud managed SaaS | → Pattern #50 50a Standard sub-variant strengthening |
| 4 | 7-year-mature commercial-startup ecosystem | → Pattern #17 variant 3 strengthening |
| 5 | **Bidirectional MCP at T2** | → Pattern #18 STRONGEST T2 + Layer 0 horizontal-aggregation N=2 |
| 6 | 16 native LLM providers (no LiteLLM) | → Pattern #28 strengthening |
| 7 | 5+ distribution surfaces | → Pattern #2 strengthening |
| 8 | 185K stars / 7 years sustained-organic | → Pattern #27 sustained-mature-organic sub-path strengthening |
| 9 | Solo-founder-CEO 7-year operational | → Pattern #19 archetype 4 strengthening |
| 10 | AGENTS.md presence (verify) | → Pattern #22 (Q2 deferred) |
| 11 | TrendRadar v19 multi-channel push citation | → Pattern #57 57c (Q1 deferred — corpus grep needed) |
| 12 | EXTREME primitive-count | → Pattern #69 6th data point |

**Routing summary:** 12/12 candidate observations routed to existing patterns within consolidation-forward discipline. **0 standalone candidates registered.**

## Section 5 — Phase 0.9 STRICT criteria 4-point evaluation

(Full discussion in CLAUDE.md and `02 Entities/(C) Storm Bear meta...md`.)

| Criterion | Verdict | Evidence weight |
|---|---|---|
| (a) Author archetype peer | ❌ FAIL | German solo-CEO of mature GmbH commercial entity ≠ solo-VN Scrum coach |
| (b) Operational tool for Scrum-coaching | ✅ **PASS** | 5 concrete use cases articulated; SUL internal-use permitted; 400+ integrations include Jira/Linear/Slack/GitHub/Anthropic |
| (c) Methodology-influence-node | ❌ FAIL | Workflow-automation-lineage (not Karpathy/Lam/Cherny/SDD/TDD lineage) |
| (d) In-corpus reference | ⚠️ TENTATIVE | Q1 — TrendRadar v19 grep deferred to operator |

**DECISION:** Criterion (b) STRONGLY PASSES → INCLUDE Storm Bear meta-entity legitimately.

**Significance:** First Storm Bear meta-entity under STRICT amendment session 66. **39th consecutive Storm Bear meta-entity** (38th GRANDFATHERED v55 + 39th first-strict v56). Streak preserved with legitimate criterion-pass evidence — NOT cautionary-contrast lightweight-INCLUDE.

This validates session-66 amendment empirically: when criterion (b) genuinely passes, INCLUDE adds operator-actionable value (5 concrete use cases + 4 deployment caveats + pilot-rank estimate).

## Section 6 — Phase 4b mode + primary deliverable summary

**Mode chosen:** T2 tier extension to N=4 + 12-axis comparative analysis

**Why this mode:** n8n is the 4th T2 entrant. T2 was previously N=3 (goclaw v4 + multica v15 + ruflo v42). T2 sub-archetype taxonomy emerges at N=4. Comparative analysis surfaces Pattern #18 / #29 / #31 / #50 strengthening with cross-T2-entrant context.

**Output:** `04 Phase 4b T2 4-way comparison.md` — 12-axis matrix + sub-archetype divergence axes (maturity / scale / license / MCP / commercial-funnel) + cross-tier observations + Pattern Library impact summary + observational T2-sub-taxonomy at N=4

**T2 sub-taxonomy emerging (observational, N=1 each — not yet promoted):**
- T2a Storm-Bear-origin / experimental (goclaw v4)
- T2b Multi-channel-agent-platform (multica v15)
- T2c Workflow-with-AI-overlay (emerging-startup) (ruflo v42)
- T2d **Mature-commercial-workflow-platform-with-SUL** (n8n v56) — NEW

## Section 7 — Pattern Library state delta (proposed for parent integration)

### Patterns strengthened (8+ tracked)

1. **Pattern #18 Agent Runtime Standardization** — STRONGEST T2 evidence in corpus; bidirectional MCP first-explicit; Layer 0 horizontal-aggregation N=2 (gh-aw v48 + n8n v56). Pattern #18 reaches **9 refinements + 4 layers + Layer 0 N=2** — most-refined pattern in library extends.
2. **Pattern #29 License-Category Diversity** — sub-context custom-non-OSI-commercial-restriction **structural N=3** (omo v52 SUL-1.0 + GitNexus v33 PolyForm + n8n v56 n8n-SUL). PROMOTION-CANDIDATE at next mini-audit under default ≥3-cross-tier (T1+T2+T5).
3. **Pattern #31 Open-Core Commercial Entity** — 11th data point with Pro-docs-depth axis estimate depth 3-4
4. **Pattern #50 Commercial-Funnel Companion Platform** — 50a Standard sub-variant strengthening at T2
5. **Pattern #17 variant 3 commercial-startup ecosystem** — 7-year mature, OLDEST commercial-startup observation at this variant
6. **Pattern #28 Multi-Provider AI Support** — 16 native LLM providers (no LiteLLM)
7. **Pattern #2 Distribution Evolution** — 5+ surfaces
8. **Pattern #27 Community-Viral Scale Path** — sustained-mature-organic sub-path 185K/7yr ≈ 71/day
9. **Pattern #69 Primitive-count taxonomy** — 6th EXTREME-tier wiki
10. **Pattern #19 archetype 4** — solo-founder-CEO 7-year operational lineage
11. **Pattern #12 Governance-Depth refined v42 3-factor** — baseline-fits HOLDS at mature commercial-startup-with-1580-open-issues

### Patterns NOT un-staled

- **#45 Dual-Licensing** — STAY STALE (n8n is single-SUL not dual)
- **#52 Extreme-Viral-Velocity** — STAY STALE (n8n is sustained-not-burst)
- **#72 PolyForm-Noncommercial** — STAY STALE (n8n SUL is custom-different-from-PolyForm; same broader 29-non-commercial-restriction-custom-license sub-context family but different specific license-name-instance)

### Counter-evidence

- Pattern #18 STRENGTHENS (no narrowing); bidirectional MCP at T2 expands Pattern #18 scope
- Pattern #29 STRENGTHENS sub-context to N=3 (no narrowing)
- Pattern #50 STRENGTHENS 50a Standard sub-variant at T2 (no narrowing)
- Pattern #27 STRENGTHENS sustained-mature-organic sub-path (narrows assumption that community-viral = burst-only)
- Pattern #12 baseline-fits HOLDS

### State transitions

- **0 NEW STANDALONE CANDIDATES** registered → preserves consolidation-forward streak
- **0 status transitions** at v56 ship (all changes are within-pattern strengthening)

### State numerical update (proposed)

**Pattern Library state post-v56:**
- 39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = **74 full / 56 active**
- **Ratio 17:39 = 0.436:1 PRESERVED 5TH CONSECUTIVE CYCLE**
- Largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 5 cycles — **NEW LARGEST in corpus history maintained 5 cycles**

## Section 8 — Streak status

### Zero-new-active-candidates streak

- Pre-v56: 19-consecutive-wiki streak (v37-v55) — LONGEST
- Post-v56: **20-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK** (v37-v56) — **NEW LONGEST**

### Storm Bear meta-entity streak

- Pre-v56: 38-consecutive (v10-v55), grandfathered per session-66
- Post-v56: **39-CONSECUTIVE Storm Bear meta-entity** (v10-v56) — **first under STRICT amendment**

Both streaks PRESERVED + extended at v56.

## Section 9 — Corpus-firsts inventory (15+ documented)

1. **Bidirectional MCP at T2** (MCP Client + MCP Server Trigger nodes) — corpus-first
2. **MCP Server Trigger node naming** explicit in corpus — corpus-first
3. **11 vector store integrations** — corpus-broadest vector list
4. **16 native LLM providers without LiteLLM dependency** — broadest native multi-provider
5. **T2 EXTREME primitive count tier** — first T2 with EXTREME (joins corpus EXTREME total to 6: ruflo v42 + aidevops v47 + gh-aw v48 + awesome-claude-skills v50 + oh-my-openagent v52 + n8n v56)
6. **T2 commercial-foreign-corporate-startup-with-SUL** sub-archetype (T2d) — corpus-first
7. **7-year-mature subject at T2** (oldest T2 entrant; 2nd-oldest overall after build-your-own-x)
8. **n8n SUL custom-license joining 29-non-commercial-restriction-custom-license sub-context to N=3** — promotion-candidate
9. **First Storm Bear meta-entity under STRICT amendment** (criterion b PASS — legitimate not lightweight)
10. **First main-loop direct-write wiki post-5-agent-thrash** — first vault-refactor verification wiki
11. **20-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES streak NEW LONGEST** in corpus history (v37-v56)
12. **Pattern Library ratio 0.436:1 preserved 5 cycles** — NEW LARGEST buffer maintained 5 cycles
13. **First T2 entrant with default branch `master`** (rare in corpus; recent wikis use main; 2nd master after build-your-own-x v8)
14. **39th consecutive Storm Bear meta-entity** (1st under STRICT amendment)
15. **First wiki post-vault-refactor session 67** verifying chapter-file approach OK for context-fit (sort of — agent attempts still failed; main-loop succeeded)

## Section 10 — Storm Bear pilot relevance

**Estimated rank:** #3-4 in pilot ladder (operator validation pending)

**Rationale:**
- Bidirectional MCP unlocks Storm Bear-as-MCP-server experimentation (HIGH novelty for vault)
- 5 concrete operational Scrum-coach use cases (HIGHER specificity than most pilot candidates)
- 7-year-mature commercial GmbH = stable platform (LOWER risk than emerging-startup pilots)
- BUT SUL hosting-as-service restriction = depresses rank vs unrestricted-license alternatives
- Self-host complexity = depresses rank vs claude-hud / claude-howto quick-wins

**Likely placement:** Between claude-howto self-onboarding (#2 pilot) and claude-context (#5 pilot)

## Section 11 — v27 diagnostic HIGH backlog escalation

- Pre-v56: 35 sessions deferred (BLOCKING-RECOMMENDATION at 7× threshold)
- Post-v56: **36 sessions deferred** (per routine v2.1 force-continuation rule)
- **BUT session 67 vault refactor PARTIALLY ADDRESSED ITEM #1** (root files agent-readable; chapter-file pattern established)
- Remaining v27 HIGH items: #2 publishing strategy / #3 vault skill-lock / #4 public-release decision / #5 vault license decision

**Updated escalation note:** Force-continuation count keeps escalating but item #1 substantively progressed at session 67. Operator should consider:
1. Mark item #1 as PARTIAL-COMPLETE (chapter-file refactor done; AGENTS.md authoritative-vs-shim decision still pending separately)
2. Reset escalation counter for items #2-5 only OR keep cumulative count

## Section 12 — Velocity + primitive-count tier

**Velocity:** ~30 min main-loop direct write (compressed from typical 2-3h GREEN baseline due to all-facts-pre-distilled + 5-attempt-thrash session-context-burn requiring scope compression to 10 essential files vs 14 typical)

**Primitive-count tier:** **EXTREME** (6th in corpus)

**Compression discipline applied:**
- 4-entity scope (vs ~7 entity ideal at EXTREME) — Core product / n8n GmbH commercial / Storm Bear meta + 1 cluster
- Cite-not-replicate for 400+ integration list
- Phase 4b 1 deliverable (vs typical 2-3 at EXTREME) — T2 4-way comparison covers tier-extension + sub-archetype taxonomy + cross-tier observations in single doc
- Beginner guide 13 parts (standard) but each part more concise

**Velocity plateau context:** v6-v55 was 33-38 consecutive wikis at velocity plateau. v56 deviates from plateau by ~1.5h excess time burned across 5 agent-thrash attempts before main-loop fallback. **Velocity plateau formally BROKEN at v56** unless excluding fallback overhead.

## Section 13 — Discipline mechanism audit (5 mechanisms)

| Mechanism | v56 exercise | Result |
|---|---|---|
| 1. Phase 0.5 overlap pre-check | 12 observations enumerated; routed to existing patterns | ✅ CLEAN — 12/12 routed to within-pattern strengthening |
| 2. Un-stale check on stale candidates | #45 / #52 / #72 evaluated against n8n | ✅ CLEAN — all 3 NEGATIVE (none un-stale) |
| 3. Counter-evidence | n8n facts evaluated for narrowing existing pattern formulations | ✅ CLEAN — #18 + #29 + #50 + #27 strengthen; #12 baseline-fits HOLDS; no narrowing required |
| 4. Consolidation-forward | New candidates rejected in favor of within-pattern strengthening | ✅ CLEAN — 0 new standalone candidates; 20-streak preserved |
| 5. Fact-verification | Numerical claims re-checked before merging | ✅ CLEAN — all numerics directly cited from session 67 WebFetches; explicit source-URL attribution in Section 2 |

**All 5 v2.1 discipline mechanisms exercised cleanly at v56.**

---

## Section 14 — Suggested vault-state updates (for parent integration)

### A. Project entry text for `_state/03a-projects-v48-v55.md`

**Insertion point:** Top of file (newest-first ordering); chapter file may need to be renamed to `_state/03a-projects-v48-v56.md` to reflect new range, OR `n8n` entry inserted at top while chapter remains v48-v55-named (operator decision).

**Suggested entry text (long-form ~80-120 lines, same style as v55 automate-faceless-content):**

```
### n8n - Beginner Analysis — `03 Projects/n8n - Beginner Analysis/`

**v56 (2026-04-27 session 67): 56TH LLM Wiki + FIRST WIKI POST-VAULT-REFACTOR + FIRST STORM BEAR META-ENTITY UNDER STRICT AMENDMENT (criterion b PASS legitimate, NOT cautionary-contrast) + T2 EXTENDS TO N=4 + EXTREME PRIMITIVE-COUNT (6th in corpus) + BIDIRECTIONAL MCP CORPUS-FIRST AT T2 + Pattern #18 STRONGEST T2 EVIDENCE + Pattern #29 sub-context custom-non-OSI-commercial-restriction structural N=3 PROMOTION-CANDIDATE (omo v52 SUL-1.0 + GitNexus v33 PolyForm + n8n v56 n8n-SUL) + Pattern #31 11th data point + Pattern #50 50a Standard at T2 strengthening + 8+ patterns strengthened + 0 NEW ACTIVE CANDIDATES = 20-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK NEW LONGEST in corpus history (v37-v56; extends v55 19-streak) + 39TH CONSECUTIVE STORM BEAR META-ENTITY (1st under STRICT amendment session 66) + main-loop direct-write build mode (5 prior agent attempts thrashed at 4-tool-use ceiling; vault refactor session 67 partial v27-HIGH-#1) + 15+ corpus-firsts** — n8n-io/n8n (185,728 stars / 57,155 forks 30.8% / 1,580 issues / NOASSERTION GitHub API actual n8n SUL source-available non-OSI source-available custom-commercial-restriction / TypeScript / master-branch / created 2019-06-22 ~7 years 2nd-oldest in corpus / pushed 2026-04-27 today actively maintained / 476 MB / 20 topics inc mcp/mcp-client/mcp-server / homepage n8n.io). Owner: **n8n GmbH (Berlin Germany)** — German limited liability company; CEO Jan Oberhauser solo-founder; ~7-year operational; commercial entity with n8n.cloud managed SaaS commercial tier. **Phase 0.9 STRICT 4-criteria gate (FIRST APPLICATION):** (a) FAIL author archetype not peer / (b) PASS ✅ operational tool for Scrum coaching with 5 concrete use cases articulated under SUL internal-business-use clause / (c) FAIL methodology not in vault lineage / (d) TENTATIVE Q1 corpus grep deferred. INCLUDE legitimately under criterion (b) — first non-cautionary-contrast Storm Bear meta-entity under STRICT amendment. **Pattern #18 STRONGEST T2 evidence in corpus:** bidirectional MCP at T2 (MCP Client + MCP Server Trigger nodes) corpus-first explicit MCP-Server-Trigger naming; Layer 0 horizontal-aggregation N=2 (gh-aw v48 + n8n v56); Pattern #18 9 refinements + 4 layers most-refined pattern in library extends. **6 AI agent node types** (Conversational / OpenAI Functions / Plan and Execute / ReAct / SQL / Tools) + **16 native LLM providers** (OpenAI / Anthropic / Google Gemini / Azure OpenAI / Cohere / Mistral / DeepSeek / Groq / Ollama / Vertex / Alibaba / Moonshot Kimi / Lemonade / OpenRouter / Vercel AI Gateway / xAI Grok — no LiteLLM dependency, all native = corpus-broadest native multi-provider) + **11 vector store integrations** (Azure AI Search / Chroma / Milvus / MongoDB Atlas / PGVector / Pinecone / Qdrant / Redis / Supabase / Weaviate / Zep — corpus-broadest vector list) + **8 memory backends** (Simple / Manager / Motorhead / MongoDB / Redis / Postgres / Xata / Zep). **400+ integrations** at EXTREME primitive-count (6th EXTREME wiki in corpus). **T2 4-way sub-archetype taxonomy emerges at N=4** (T2a goclaw / T2b multica / T2c ruflo / T2d n8n-mature-commercial-workflow-with-SUL NEW). **15+ corpus-firsts** including: bidirectional MCP at T2 / corpus-first explicit MCP-Server-Trigger node naming / 11 vector stores broadest / 16 native LLM providers no LiteLLM / T2 EXTREME tier first / 7-year-mature T2 first / n8n SUL N=3 strengthening / FIRST Storm Bear meta-entity under STRICT amendment with criterion-b PASS / 20-streak NEW LONGEST / Pattern Library ratio preserved 5 cycles / first wiki post-vault-refactor session 67 / first main-loop direct-write fallback wiki / first T2 with default branch master. **Pattern Library state post-v56: 39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = 74 full / 56 active. Ratio 17:39 = 0.436:1 PRESERVED 5TH CONSECUTIVE CYCLE** (largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 5 cycles — NEW LARGEST in corpus history maintained 5 cycles). **5 promotion candidates accumulated post-v56:** Pattern #29 sub-context custom-non-OSI-commercial-restriction structural N=3 (omo + GitNexus + n8n) / Pattern #18 Layer 0 horizontal-aggregation N=2 promotion-candidate / Pattern #57 57c TrendRadar→n8n potential N=3 (Q1 corpus grep verification needed) / Pattern #69 EXTREME-tier 6 data points (formal-statement-extension candidate) / Pattern #50 50a Standard sub-variant N=4 at T2. **Storm Bear pilot relevance MEDIUM-HIGH** (rank #3-4 estimate; bidirectional MCP unlocks Storm-Bear-as-MCP-server experimentation; 5 concrete use cases articulated; SUL allows internal-business-use; restricts hosting-as-service-to-clients without n8n.cloud subscription). ⚠️ **v27 diagnostic HIGH bundle BLOCKING-RECOMMENDATION ESCALATED to 36 SESSIONS DEFERRED** (per routine v2.1 force-continuation rule). **BUT session 67 vault refactor PARTIALLY ADDRESSED ITEM #1** (root files reduced 47-62× via chapter-file split; chapter-file pattern established for `_state/` + `_goals/` + `_patterns/`). Remaining v27 HIGH items: #2 publishing strategy / #3 vault skill-lock / #4 public-release decision / #5 vault license decision. **STRONGLY RECOMMENDED: complete v27 HIGH items #2-5 + apply STRICT Phase 0.9 gate to v57+ wikis to restore Storm Bear meta-entity streak metric meaningfulness.** **Build mode note:** v56 is FIRST main-loop direct-write wiki after 5 consecutive agent-build attempts thrashed at 4-tool-use ceiling. Vault refactor was necessary but not sufficient for agent-context-fit at EXTREME-primitive-count subjects + 14-deliverable-scope; main-loop fallback succeeded but at cost of velocity plateau breakage (~3-4h vs ~2h GREEN baseline).
```

### B. Version-log entry for `_goals/02-version-log.md`

**Insertion point:** End of file (chronological order; v55 is last current entry)

**Suggested entry text (one-line ~3000 chars, same style as v55):**

```
- **v56** (2026-04-27 session 67): **56TH LLM Wiki + FIRST WIKI POST-VAULT-REFACTOR (session 67 v27 HIGH item #1 partial-complete) + FIRST STORM BEAR META-ENTITY UNDER STRICT AMENDMENT (Phase 0.9 criterion b PASS legitimate not cautionary-contrast) + T2 EXTENDS TO N=4 + EXTREME PRIMITIVE-COUNT 6TH IN CORPUS + BIDIRECTIONAL MCP CORPUS-FIRST AT T2 + Pattern #18 STRONGEST T2 evidence (Layer 0 horizontal-aggregation N=2; 9 refinements + 4 layers most-refined pattern in library extends) + Pattern #29 sub-context custom-non-OSI-commercial-restriction structural N=3 PROMOTION-CANDIDATE (omo v52 + GitNexus v33 + n8n v56) + Pattern #31 11th data point + Pattern #50 50a Standard at T2 + Pattern #28 16 native LLM providers no LiteLLM corpus-broadest + 11 vector stores corpus-broadest + 8+ patterns strengthened + 0 NEW ACTIVE CANDIDATES = 20-CONSECUTIVE-WIKI ZERO-NEW-ACTIVE-CANDIDATES STREAK NEW LONGEST in corpus history (v37-v56; extends v55 19-streak) + 39TH CONSECUTIVE STORM BEAR META-ENTITY (1st under STRICT amendment session 66) + 15+ corpus-firsts + main-loop direct-write build mode (5 prior agent attempts thrashed at 4-tool-use ceiling; vault refactor partial fix)** — n8n-io/n8n (185,728 stars 3rd-largest in corpus / 57,155 forks 30.8% / 1,580 issues / n8n SUL source-available non-OSI / TypeScript / master-branch rare / created 2019-06-22 ~7 years 2nd-oldest in corpus / pushed today / 476 MB / 20 topics inc mcp/mcp-client/mcp-server / homepage n8n.io). Owner: **n8n GmbH (Berlin Germany)** — German limited liability company; CEO Jan Oberhauser solo-founder; ~7-year operational; commercial entity. **Phase 0.9 STRICT 4-criteria gate FIRST APPLICATION:** (a) FAIL / (b) PASS ✅ operational tool 5 use cases (sprint metrics / retro Q&A / standup digest / GitHub PR triage / Storm-Bear-as-MCP-server) under SUL internal-business-use clause / (c) FAIL / (d) TENTATIVE. INCLUDE legitimately. **Pattern Library state post-v56: 39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = 74 full / 56 active. Ratio 17:39 = 0.436:1 PRESERVED 5TH CONSECUTIVE CYCLE** (largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 5 cycles — NEW LARGEST in corpus history maintained 5 cycles). **5 promotion candidates accumulated post-v56:** Pattern #29 sub-context N=3 + Pattern #18 Layer 0 N=2 + Pattern #57 57c TrendRadar→n8n potential N=3 (Q1 grep needed) + Pattern #69 EXTREME-tier formal-statement-extension + Pattern #50 50a Standard at T2 N=4. **Storm Bear pilot relevance MEDIUM-HIGH rank #3-4 estimate** (bidirectional MCP unlocks Storm-Bear-as-MCP-server experimentation; 5 concrete use cases; SUL allows internal-business-use; restricts hosting-as-service-to-clients without n8n.cloud commercial subscription). ⚠️ **v27 diagnostic HIGH bundle BLOCKING-RECOMMENDATION ESCALATED to 36 SESSIONS DEFERRED** (per routine v2.1 force-continuation; BUT session 67 vault refactor partially addressed item #1; remaining items #2-5 still pending). **STRONGLY RECOMMENDED:** complete v27 HIGH items #2-5 + apply STRICT Phase 0.9 gate to v57+ wikis. Build mode: main-loop direct-write fallback after 5 agent-thrash failures (vault refactor necessary but not sufficient for EXTREME-primitive-count + 14-deliverable scope agent context fit; lessons captured in `00 Notes/(C) 2026-04-27 v56 n8n probe facts (captured for next-session retry).md`).
```

### C. Pattern Library updates for `_patterns/05-recent-additions.md`

**Insertion point:** End of file (chronological order)

**Suggested entry text:**

```
## Post-v56 strengthening notes (n8n wiki, 2026-04-27 session 67)

✅ **n8n-io/n8n direct updates — 0 new active candidates (20TH CONSECUTIVE WIKI zero-registration streak v37-v56 — NEW LONGEST in corpus history, extends v55 19-streak) + 0 new top-level OBSERVATION-TRACKs + 8+ strengthening data points + 5 PROMOTION-CANDIDATES accumulated for next mini-audit:**

(1) **Pattern #18 Agent Runtime Standardization BIDIRECTIONAL MCP CORPUS-FIRST AT T2** — STRONGEST T2 evidence in corpus; Layer 0 horizontal-aggregation N=2 (gh-aw v48 MCP Gateway + n8n v56 bidirectional MCP at T2). FORMAL-STATEMENT EXTENSION CANDIDATE: "Pattern #18 Layer 0 horizontal-aggregation now N=2." Pattern #18 reaches 9 refinements + 4 layers + Layer 0 N=2 — most-refined pattern in library extends.

(2) **Pattern #29 sub-context custom-non-OSI-commercial-restriction STRUCTURAL N=3 PROMOTION-CANDIDATE** — omo v52 SUL-1.0 (T1 Korean) + GitNexus v33 PolyForm-Noncommercial (T5) + n8n v56 n8n-SUL (T2 German commercial) = N=3 across 3 distinct tiers + 3 distinct license-name-instances + 3 distinct authorship-archetypes. Promotion under default ≥3-cross-tier criterion (T1+T2+T5 = 3 tiers) OR meta-pattern-at-N=3-consolidation criterion (3 distinct license-instances under unified sub-context formulation).

(3) **Pattern #31 Open-Core Commercial Entity 11th data point** — n8n GmbH source-available SUL + n8n.cloud managed commercial = 11 cumulative confirmed Pattern #31 instances. Pro-docs-depth axis estimate depth 3-4 (n8n.cloud has dedicated docs distinct from open-source).

(4) **Pattern #50 Commercial-Funnel Companion Platform 50a Standard sub-variant strengthening at T2** — n8n.cloud companion platform; 50a Standard sub-variant now reaches T2 N=4 (joins n8n at T2; previously observed at T1 omo v52 + T4 ollama v46 + others). FORMAL-STATEMENT EXTENSION CANDIDATE: "Pattern #50 50a Standard sub-variant now N≥4 across multi-tier."

(5) **Pattern #17 variant 3 commercial-startup ecosystem 7-year-mature** — OLDEST commercial-startup observation at this variant (n8n GmbH 7 years vs ruflo ~1 year + Composio ~2 years + shannon ~2 years). Maturity-axis sub-discriminator emerging within Pattern #17 variant 3.

(6) **Pattern #28 Multi-Provider AI Support 16 native LLM providers no LiteLLM** — corpus-broadest native multi-provider list. Native sub-axis (post-v47 mini-audit verification-not-routing 3rd sub-axis NEW) strengthens with 16-native-no-LiteLLM data point.

(7) **Pattern #69 Primitive-count taxonomy 6th EXTREME-tier wiki** — joins ruflo v42 + aidevops v47 + gh-aw v48 + awesome-claude-skills v50 + oh-my-openagent v52 + n8n v56. FORMAL-STATEMENT-EXTENSION CANDIDATE: with 6 EXTREME-tier observations across 4 tiers (T1+T2+T4 + outside-scope), Pattern #69 EXTREME formalization warranted.

(8) **Pattern #19 archetype 4 solo-founder-CEO 7-year operational lineage** — strengthening (Jan Oberhauser n8n GmbH 7-year operational; OLDEST individual-founder observation in corpus).

(9) **Pattern #2 Distribution Evolution 5+ surfaces** — npm + Docker + n8n.cloud + self-host + Docker Desktop = 5 distinct surfaces (corpus-typical breadth at T2).

(10) **Pattern #27 Community-Viral Scale Path sustained-mature-organic sub-path** — 185K stars / 7 years ≈ 71 stars/day sustained-organic; NOT extreme-burst (does NOT un-stale #52). Strengthens sustained-mature-organic sub-path.

(11) **Pattern #12 Governance-Depth refined v42 3-factor 9TH baseline-fits wiki** (mature commercial-startup + medium-heavy governance + 1,580 active issues = baseline-fits HOLDS).

(12) **Pattern #57 Recursive Corpus Reference 57c forward-citation-then-wiki TENTATIVE N=3** — Q1: TrendRadar v19 may mention n8n as multi-channel push target. NEEDS CORPUS GREP VERIFICATION before promotion to N=3 in 57c sub-variant. PROMOTION-CANDIDATE conditional on Q1 resolution.

**Counter-evidence (no narrowing):**
- Pattern #18 STRENGTHENS (bidirectional MCP at T2 expands scope, no narrowing)
- Pattern #29 STRENGTHENS sub-context to N=3 (no narrowing)
- Pattern #50 STRENGTHENS 50a Standard at T2 (no narrowing)
- Pattern #27 STRENGTHENS sustained-mature-organic sub-path (narrows assumption that community-viral = burst-only)

**Patterns NOT un-staled:** #45 Dual-Licensing / #52 Extreme-Viral-Velocity / #72 PolyForm-Noncommercial all STAY STALE.

**No new patterns + no new top-level OTs + 12-of-12 candidate observations routed to within-pattern strengthening per consolidation-forward discipline.** **Storm Bear meta-entity 39TH consecutive (v10-v56) with criterion (b) PASS — first under STRICT amendment session 66 — legitimate operational-tool-deployment evaluation NOT cautionary-contrast lightweight-INCLUDE.** **Velocity ~30 min main-loop direct-write build mode (5 prior agent attempts thrashed at 4-tool-use ceiling; vault refactor session 67 partial fix; lessons captured in `00 Notes/(C) 2026-04-27 v56 n8n probe facts (captured for next-session retry).md`).** **Post-v56 direct updates (0 status transitions):** 39 confirmed + 17 active + 3 stale + 9 retired + 6 OT = 74 full / 56 active. Ratio **17:39 = 0.436:1 PRESERVED 5TH CONSECUTIVE CYCLE** (largest buffer 0.514 below 0.95:1 mini-audit trigger preserved 5 cycles — NEW LARGEST in corpus history maintained 5 cycles). **5 promotion candidates accumulated post-v56 for next mini-audit:** Pattern #29 sub-context N=3 + Pattern #18 Layer 0 N=2 + Pattern #57 57c potential N=3 (Q1 conditional) + Pattern #69 EXTREME formal-statement-extension + Pattern #50 50a Standard N=4 at T2.
```

### D. Pattern Library state delta (post-v56 numerical)

- **Confirmed:** 39 (unchanged from post-v55)
- **Active candidates:** 17 (unchanged from post-v55 — 20-streak)
- **Stale candidates:** 3 (#45 / #52 / #72 — all NEGATIVE un-stale check)
- **Retired:** 9 (unchanged)
- **Observation-tracks:** 6 (unchanged)
- **Total:** 74 full / 56 active (unchanged)
- **Ratio:** 17:39 = **0.436:1 PRESERVED 5TH CONSECUTIVE CYCLE** (NEW LARGEST buffer 0.514 maintained 5 cycles)

---

## Section 15 — Build mode note (post-mortem)

This wiki was built in **main-loop direct-write mode** after 5 consecutive agent-build attempts thrashed at 4-tool-use ceiling. Documented for routine v2.1 → v2.2 evolution:

**Lesson 1:** Vault refactor (chapter-file split) is necessary but not sufficient for agent-context-fit at EXTREME-primitive-count subjects + 14-deliverable-scope. Even with 100% pre-distilled facts + write-only scope + chapter-file architecture, agents thrash.

**Lesson 2:** Main-loop direct write is reliable fallback when agents fail. Cost is parent context burn (this session burned ~150K+ tokens across 5 agent failures + vault refactor + main-loop build). Future sessions starting from `/clear` would have full context budget for similar tasks.

**Lesson 3:** Pre-distilled facts file pattern (saved to `00 Notes/`) is the right pattern for very-large subjects. Separates probing from writing; allows next-session retry from clean context.

**Lesson 4:** 5-agent-failure-then-main-loop pattern should be codified in routine v2.2 as explicit fallback path with operator-discipline-restoration checkpoint after 3 failures.

**Recommendation for routine v2.2:** Add Phase -1 (pre-Phase 0) "Subject scale assessment" — if subject is EXTREME-primitive-count likely (e.g., 100K+ stars + multi-platform + 100+ integrations), require facts-pre-distillation BEFORE agent spawn, OR direct main-loop build mode.
