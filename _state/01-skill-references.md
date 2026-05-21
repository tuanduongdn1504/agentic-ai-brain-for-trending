## Patterns đã verified work / Verified Patterns

> Patterns đã được prove qua real project — Claude phải ưu tiên dùng thay vì re-derive từ đầu.

### 1. LLM Wiki pattern (Karpathy) — ✅ proven 2026-04-17

**Verified trong project:** `03 Projects/Everything Claude Code - Beginner Analysis/`

Build persistent knowledge wiki cho topic phức tạp, LLM maintain tất cả cross-references. Pattern generalize cho mọi topic có ≥5 sources + ≥3 months lifespan + clear ownership.

**Skill reference:** `05 Skills/llm-wiki-ingest.md` — codified 13-section entity page format + workflow 5 phases.

**Evidence:** 18 files deliverable trong 1 session (14 wiki + 1 published + 2 contribution docs + 1 iteration log). Knowledge compounds, cross-references emerge naturally, contradictions surface qua verification.

**Khi dùng:** user có topic phức tạp muốn build knowledge base; hỏi "dùng LLM Wiki pattern không?" thay vì treat như note thường.

### 2. Brain-setup interview (5 rounds) — ✅ proven 2026-04-17

Generate CLAUDE.md qua structured interview. File root này được sinh ra bằng skill này.

**Skill reference:** `05 Skills/brain-setup.md`

### 3. New project scaffolding — ✅ proven 2026-04-17

Template duplication + 6-question interview → project folder với CLAUDE.md + COMMANDS.md + numbered folders.

**Skill reference:** `05 Skills/new-project.md`

### 4. LLM Wiki Routine (autonomous orchestration) — ✅ proven 2026-04-18, **v2.2 codified 2026-05-14**

**Verified trong 81 projects** (v1-v81), **17 wikis under v2.2** (v66-v81 2026-05-14 → 2026-05-20) with zero amendments needed. Production-stable across **~25 distinct Phase 4b routing modes**.

Routine pattern = orchestration meta-skill. User input = 1 source URL. Routine autonomous handles toàn bộ 7 phases (Pre-flight → Scaffold → Sources → Entities → Beginner Guide → Phase 4b deliverable → Iteration log → Vault updates) trong ~75-180 min (velocity depends on subject complexity + corpus-firsts density; v81 = 75 min; v79 = 180 min).

**Skill references:**
- **`05 Skills/llm-wiki-routine-v2.2.md`** — **ACTIVE** (consolidated 2026-05-14 from ~31 codification candidates accumulated across v60-v65 wiki ships + v66 EARLY-OPERATOR-ELECTED mini-audit + completed pilot lifecycle v3.2 hireui adversarial-review)
- `05 Skills/llm-wiki-routine-v2.1.md` — v2.1 (superseded 2026-05-14; production-stable across v19-v65 corpus before supersession)
- `05 Skills/llm-wiki-routine-v2.md` — v2 (PUBLIC-ARCHIVED 2026-04-29; superseded 2026-04-22; retained for history)
- `05 Skills/llm-wiki-routine.md` — v1 (PUBLIC-ARCHIVED 2026-04-29; superseded 2026-04-19; retained for history)

**Evidence:** Pattern proven 81× across ~25 distinct Phase 4b routing modes. Shipped 81 wikis covering **5-tier taxonomy + outside-scope** (all 5 tiers multi-validated; T3 closed gap at v74 LLMs-from-scratch + NEW T3 sub-archetype "Educational-Book-Companion"). **17 wikis under v2.2 with zero amendments needed** = first-cycle validation clean. **Storm Bear meta-entity streak = 17 consecutive PASS post-v64-RESET** (NEW CORPUS-RECORD; 25-instance window 92.0% INCLUDE rate).

**v2.2 changes from v2.1 (2026-05-14):**
- **Phase 0.4 docs/ tree-listing** (v61 lesson) — explicit `docs/` directory tree fetch before individual files; avoids 404 silent-fail
- **Phase 0 velocity-screen automation** (v63 lesson) — auto-compute stars/day for ALL incoming subjects (not only viral-routing); catches Pattern #52 qualifications at ship-time
- **Engagement-signal sub-investigation** (v63 lesson) — capture watchers/stars + forks/stars ratios for ALL subjects; distinguishes drive-by-stars-dominant from active-deployment
- **13th classification axis "Living-Domain-Standards Tracking"** (v64 lesson) — Phase 0 axis: does subject codify external authoritative standards with versioned/deprecation-aware discipline?
- **Phase 0.9 SKIP entity slot reallocation** (v64 lesson) — when STRICT yields SKIP, reallocate 4th slot to Pattern Library implications; do not ship 3-entity wiki
- **Phase 4b PRIMARY routing discipline** (v64 lesson) — pre-register at Phase 0 classification, structure Phase 3 entity pages around PRIMARY deliverable
- **NEW Pattern candidate proposal-document discipline** (v64 lesson) — formal proposal at `01 Analysis/` for next-audit deliberation; 8 instances shipped under v2.2 (v74 + v75 + v76 + v77 + v78 + v79 + v80 + v81)
- **Source-celebrity-derivative-distillation criteria** (v63 lesson) — codify recognition: author ≠ source individual + explicit attribution + public observations as raw material + installable artifact packaging
- **Reference Claude Code's actual system prompts when codifying vault routines** (v65 lesson) — consult `claude-code-system-prompts` archive (v65 wiki subject) for ground-truth
- **Pre-Phase-6 fact-verification expanded** (v63 lesson) — verify Pattern Library evidence lists current to last 3-5 wikis
- **Pre-Phase-6 retroactive-correction-check** (v63 lesson) — formal mechanism to update prior wiki's register when retroactive correction caught
- **1-wiki rapid-evolution detection** (v65 lesson) — log meta-observation as Library-vocabulary candidate when N+1 wiki evolves N wiki's pattern
- **Cross-archetype N-counting as separate dimension from cross-tier** (v63 lesson) — Pattern #21 promotion via N=4 cross-archetype demonstrates counting dimension distinct from N=4 cross-tier
- **Un-stale 3-step arc** (v63 lesson) — lineage-test → independence-test → promotion sequence
- **Strengthen-over-discover discipline streak metric** (v63 lesson) — track ZERO-NEW-ACTIVE-CANDIDATES streak as health metric
- **Pattern #51 sub-pole "Anti-vibe-with-pragmatic-acknowledgment"** (v61+v63 counter-evidence narrowing scope)
- **EXTREME-VIRAL sub-archetype 3-axis discipline** (v63 lesson) — register sub-archetypes 52a/52b/52c alongside top-level Pattern #52
- **EARLY-OPERATOR-ELECTED mini-audit class** (v63 lesson) — 4th mini-audit class alongside CONSERVATIVE-DISCIPLINE / STRENGTHENING-DOMINANT / EXTENDED
- **Library-vocabulary item #9 cross-pattern coupled-design** (v60-v65 baseline; N=5+ at v65; CORPUS-RECORD 9-pattern at v78)
- **Library-vocabulary item #10 1-wiki rapid-pattern-evolution observational track** (v62→v63 Pattern #76 + v64→v65 Pattern #78 = N=2 TIED FASTEST cycles)
- **4 NEW anti-patterns added** — skip Phase 0 velocity-screen / defer NEW Pattern candidate proposal-document / skip Phase 0.9 SKIP entity slot reallocation / re-derive Claude Code prompt envelope from memory

**Routine v2.3 codification backlog (post-v81):** ~33 candidates accumulated across v66→v81 (target codification at ~v85-v90 natural cadence). Key items: sub-archetype proposal-document discipline as Phase 4b vehicle / corpus-recursive anchor revisitation policy / honest-self-review tightening pass post-Phase-6 (v81 first instance) / Storm Bear (a) axis 5-distinct-sub-criterion-calls (VN-located + VN-diaspora + VN-locale-inclusive + Chinese-handle-inferred + community-org PROBABLE-PASS) / criterion-stretching discipline (v81 criterion-4 within-instance-variation stretch lesson) / multi-skill-brand-portfolio Phase 0 distribution-axis sub-distinction / 8-pattern coupled-design as new corpus-record-condition.

**v2.1 changes from v2 (2026-04-22, historical):**
- 5 structural-promotion criteria (up from 2)
- 4 new Pattern Library mechanisms (OBSERVATION-TRACK sub-category / absorption-retirement / un-stale mechanism / counter-evidence-driven refinement)
- Audit cadence reform (mini at 0.95:1 / full at 1.05:1)
- Pre-registration overlap pre-check (>70% overlap → reject/consolidate)
- Consolidation-forward registration discipline
- Storm Bear meta-entity per-wiki evaluation (not blanket obligation)
- Supply-chain awareness protocol (Pattern #66)
- Fact-verification protocol
- Operator-facing backlog discipline
- Stream-timeout resume protocol
- Phase 4b routing modes expanded from 16 to ~25
- Ratio notation clarified (active/confirmed; lower is healthier)

**v2 changes from v1 (2026-04-19, historical):**
- 12-axis Phase 0 classification + 16-mode Phase 4b routing
- Consolidation guard + Pattern Library integration + Cross-wiki absence detection
- External URL resolution + Branch fallback + Storm Bear meta-entity feature
- BLOCKED_CONSOLIDATION status

**Khi dùng:** User nói "LLM wiki cho <URL>" → invoke v2.2 routine, autonomous execute. Consolidation guard (with v2.1 reformed cadence + v2.2 expansions) runs first.

**Meta-insight:** Routines compound differently than skills. Skill = knowledge. Routine = execution automation. v2.2 is the product of 81 wikis × ~31 v60+ codification candidates consolidated into operational protocol. Phase 4b PRIMARY proposal-document discipline (introduced at v64; matured across v74-v81 with 8 formal proposals shipped) is the highest-leverage v2.2 addition.

