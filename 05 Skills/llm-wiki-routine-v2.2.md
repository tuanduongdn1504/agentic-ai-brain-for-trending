# Skill: LLM Wiki Routine v2.2

📍 **Status:** IN-FLUX (continues evolving — current version as of 2026-05-14)

> **Type:** Orchestration meta-skill (Routine pattern)
> **Version:** v2.2 — consolidated from ~31 codification candidates accumulated across v60-v65 (6 wikis + v63 EARLY mini-audit + 1 pilot lifecycle)
> **Codified:** 2026-05-14 (post-v65 wiki ship, pre-v66 audit-at-v65-trigger acceleration)
> **Supersedes:** `llm-wiki-routine-v2.1.md` (v2.1, codified 2026-04-22; session-66 amendment 2026-04-26 tightened Phase 0.9 STRICT)
> **Parent skill:** `llm-wiki-ingest.md` (methodology)
> **Sibling refs:** `PATTERN_LIBRARY.md` (vault root — authoritative pattern register)

---

## What's new in v2.2 (vs v2.1)

v2.1 was codified after 31 wikis with 1 amendment session (Phase 0.9 STRICT tightening at session 66 / v55). v2.2 incorporates ~31 codification candidates accumulated across v60+v61+v62+v63+v63-EARLY-mini-audit+v64+v65 wiki ships + 1 completed pilot lifecycle (BMAD+codex-adversarial-review v3.2 hireui 2026-05-13).

### Major additions (summary)

**Phase 0 expansions (4 items):**
1. **Phase 0.4 docs/ tree-listing** (v61 lesson) — Phase 0 probe explicitly lists `docs/` directory tree before fetching individual files; avoids 404 silent-fail when filenames differ from common conventions
2. **Phase 0 velocity-screen automation** (v63 lesson) — auto-compute stars/day-vs-threshold for ALL incoming wiki subjects (not only viral-routing); would have caught v62 codex-plugin-cc Pattern #52 qualification at v62 ship
3. **Engagement-signal sub-investigation discipline** (v63 lesson) — capture watchers/stars + forks/stars ratios for ALL subjects; helps distinguish drive-by-stars-dominant from active-deployment (v64 claude-seo 15.3% fork ratio + v65 claude-code-system-prompts 17.8% corpus-record were caught via this)
4. **Living-domain-standards-tracking as Phase 0 axis** (v64 lesson) — add 13th axis to classification: "Does subject codify external authoritative standards with versioned/deprecation-aware discipline?"

**Phase 0.9 discipline expansions (1 item):**
5. **Phase 0.9 SKIP entity slot reallocation discipline** (v64 lesson) — when STRICT yields SKIP, formally reallocate 4th entity slot to Pattern Library implications package (not leave at 3); v64 demonstrated with Entity 4 = multi-platform + Pattern Library implications

**Phase 1-3 expansions (2 items):**
6. **Phase 4b PRIMARY routing discipline** (v64 lesson) — when wiki ship has clear PRIMARY Pattern Library implication, structure Phase 3 entity pages around it as PRIMARY deliverable. Pre-register at Phase 0 classification, not retroactively at Phase 4
7. **Source-celebrity-derivative-distillation criteria** (v63 lesson) — codify recognition: (1) author ≠ source individual, (2) explicit source attribution with URL, (3) public observations as raw material, (4) installable artifact packaging

**Phase 4b expansions (2 items):**
8. **NEW Pattern candidate proposal-document discipline** (v64 lesson) — when Phase 4b generates NEW top-level candidate(s), draft formal proposal-document at `01 Analysis/` for next-audit deliberation (not just append to `_patterns/05-recent-additions.md`); v64 Pattern #19 N=3 proposal + v65 Pattern #78 N=2 proposal are exemplars
9. **Reference Claude Code's actual system prompts when designing vault routines** (v65 lesson) — discipline of consulting `claude-code-system-prompts` archive (v65 wiki subject) before codifying new vault practices; v65 provides ground-truth for understanding Claude Code's prompt envelope

**Phase 5-6 expansions (3 items):**
10. **Pre-Phase-6 fact-verification expanded** (v63 lesson) — verify Pattern Library evidence lists are current to last 3-5 wikis, not just numbered-pattern reference checking
11. **Pre-Phase-6 retroactive-correction-check** (v63 lesson) — when retroactive Pattern Library correction is caught (e.g., v63 catching v62 codex-plugin-cc Pattern #52 qualification gap), formal mechanism to update prior wiki's register
12. **1-wiki rapid-evolution detection discipline** (v65 lesson) — when N+1 wiki provides evidence to evolve N wiki's pattern registration, log meta-observation as Library-vocabulary candidate AND consider promotion-acceleration

**Pattern Library discipline expansions (5 items):**
13. **Cross-archetype N-counting as separate dimension from cross-tier** (v63 lesson) — Pattern #21 promotion via N=4 cross-archetype demonstrates counting dimension distinct from N=4 cross-tier; codify alongside criteria #1-#5
14. **Lineage-test → independence-test → promotion 3-step un-stale arc** (v63 lesson) — when un-stale candidate fails lineage-test (same lineage as existing evidence), evaluate independence-test on subsequent wikis; if satisfied, promote. v60→v61→v63 demonstrates
15. **Strengthen-over-discover discipline streak metric** (v63 lesson) — track ZERO-NEW-ACTIVE-CANDIDATES streak as Pattern Library health metric; longer streaks signal mature corpus + consolidation-forward discipline
16. **Anti-vibe-with-pragmatic-acknowledgment as Pattern #51 sub-pole** (v61+v63 lessons) — counter-evidence narrowing scope; explicit handling of pragmatic-acknowledgment positions in spectrum patterns
17. **EXTREME-VIRAL sub-archetype 3-axis discipline (Pattern #52)** (v63 lesson) — when N=3 cross-archetype reached for viral patterns, register sub-archetypes (52a/52b/52c) alongside top-level pattern; deliberate consolidation vs split at sustained-velocity test

**Audit class expansion (1 item):**
18. **EARLY-OPERATOR-ELECTED mini-audit class** (v63 lesson) — operator may elect mini-audit BEFORE natural-cadence trigger when high-impact promotion is ripe (e.g., LONGEST stale arc); codify as 4th mini-audit class alongside CONSERVATIVE-DISCIPLINE / STRENGTHENING-DOMINANT / EXTENDED

**Library-vocabulary expansion (2 items):**
19. **Library-vocabulary item #9: cross-pattern coupled-design correlations** (v60+v54 baseline; v65 strengthens to N=5+) — when multiple patterns co-occur at single wiki, log as cross-pattern coupled-design observation
20. **Library-vocabulary item #10: 1-wiki rapid-pattern-evolution observational track** (v62→v63 Pattern #76 + v64→v65 Pattern #78 = N=2 evidence; TIED FASTEST cycles in corpus history)

**Anti-patterns expanded (already in v2.1; v2.2 adds 4 NEW):**
21. **Skip Phase 0 velocity-screen** (v2.2 NEW) — auto-compute stars/day always; v62 codex-plugin-cc audit gap shows manual skipping causes pattern mis-classification
22. **Defer NEW Pattern candidate proposal-document** (v2.2 NEW) — drafting formal proposal at `01 Analysis/` is part of Phase 4b for NEW candidates; deferring loses audit-ready evidence package
23. **Skip Phase 0.9 SKIP entity slot reallocation** (v2.2 NEW) — when STRICT yields SKIP, reallocate 4th slot to Pattern Library implications; do not ship 3-entity wiki
24. **Re-derive Claude Code prompt envelope from memory when codifying vault routines** (v2.2 NEW) — consult `claude-code-system-prompts` archive (v65 wiki subject) for ground-truth

---

## Invocation (unchanged from v2.1)

User says: `"LLM wiki for <URL>"`, `"routine for <topic>"`, `"build wiki on <repo>"`.

→ Invoke immediately. No interview. No check-ins between phases.

**Do NOT invoke when:**
- Topic fails Phase 0 threshold
- User explicitly requests interview mode
- Consolidation state blocks new wikis (see §Consolidation guard below)

---

## Consolidation guard (v2.1 refined; v2.2 unchanged)

**Before Phase 0, check consolidation state:**

```
Compute ratio = active_candidates / confirmed_patterns

IF ratio > 2.0 OR action_backlog > 100:
    HARD BLOCK new wiki. Recommend (in priority order):
      1. Execute pending operator-facing vault actions (highest leverage)
      2. Run Pattern Library audit (full audit if ratio >1.05:1)
      3. Run mini-audit (if 0.95:1 < ratio ≤ 1.05:1)
      4. Refactor routine (if action_backlog > 100)
    User can override with explicit "proceed despite consolidation state"

ELIF ratio > 1.05:
    SOFT WARNING: full audit recommended; build proceeds if explicitly confirmed

ELIF ratio > 0.95:
    INFO: mini-audit available as option; build proceeds

ELSE (ratio ≤ 0.95):
    PROCEED normally
```

**Operator-facing backlog tracking (v2.1 → v2.2 unchanged):**

Routine tracks deferred vault actions (e.g., v27 diagnostic HIGH bundle, routine v2.2 codification candidates). At 5+ sessions of deferral:
- Escalate in recommendation with "BLOCKING-RECOMMENDATION" tag
- Do not hard-block, but be blunt in final report

**Override:** User can explicitly request wiki build despite state. Honor it, but note the trade-off in Phase 5 iteration log and escalate backlog in final recommendation.

---

## 7-phase workflow (v2.2 refined)

### Phase 0: Pre-flight + enhanced probe (15-20 min)

**0.1 Consolidation guard check** — see above.

**0.2 WebFetch-first probe** (v2 convention retained):

```
WebFetch: github.com/<owner>/<repo>
Extract:
  - Description/tagline verbatim
  - Stars / forks / watchers / open issues / commits / contributors
  - Primary language %
  - License
  - Latest release + date
  - Homepage URL
  - Top-level file list (README, CLAUDE.md, AGENTS.md, pyproject.toml, etc.)
  - Author/org attribution
  - First 300 lines of README summary
```

**0.3 Branch resolution fallback** (v2 retained):

```
IF raw.githubusercontent.com/<repo>/main/<file> returns 404:
    Try: master, v4, v3, dev (common alternatives)
    Log branch in iteration log
```

**0.4 Enhanced classification probe** — **13-axis** (v2.2 expanded from v2.1's 12-axis):

| Axis | Values |
|------|--------|
| **Tier** | T1 assistant / T2 service / T3 education / T4 bridge / T5 application / outside-scope |
| **Archetype** | solo-community / solo-VN-authored / solo-Korean (v27+) / solo-Japanese (v61+) / founder-personal / community / LLC / official-corporate / solo-enterprise-scale / academic-lab (v22+) / ecosystem-layer-individual-with-commercial-platform (v31+) / corporate-org-with-commercial-product (v65+) |
| **Scale tier** | small (<5K) / medium (5-20K) / large (20-60K) / X-large (60-100K) / XX-large (>100K) |
| **Primary lang** | TS / JS / Python / Rust / Go / Shell / markdown-only / etc. |
| **Packaging tool** | npm / pip / uv / cargo / shell / brew / markdown-only-directory |
| **Origin story** | individual-author-lineage / methodology-lineage / community-viral / corporate-strategic / academic-research / protocol-concurrent / unknown |
| **Methodology** | named (SDD / BMM / TDD / XP / DDD) / feature-framework / persona-library / bridge / aggregator-genre / NONE |
| **Governance file count** | 0-2 (light) / 3-4 (medium) / 5-6 (heavy) / 7+ (extensive) |
| **Agent/skill count** | 1-10 / 11-30 / 31-100 / 100+ / 1000+ (directory scale) |
| **i18n coverage** | EN-only / VN / CN / JA / KO / CJK-trio / 7-language-tier / other |
| **Intellectual influence cited** | Karpathy / John Lam / Bostrom / research-paper-chain / none / other |
| **Agent platforms supported** | count (if applicable) |
| **NEW v2.2: Living-Domain-Standards Tracking** | YES (codifies external authoritative standards with versioned/deprecation-aware discipline; v64 claude-seo / v65 claude-code-system-prompts) / NO / N/A |

**Phase 0.4 docs/ tree-listing (v2.2 NEW per v61 lesson):**

Before fetching individual files, list the `docs/` directory tree:

```
WebFetch: github.com/<owner>/<repo>/tree/main/docs
Capture: filenames + sub-directories
```

Reasoning: filename conventions vary (e.g., `ARCHITECTURE.md` vs `architecture.md` vs `01-architecture.md`); explicit listing avoids 404 silent-fail when fetching individual files.

**Phase 0 velocity-screen automation (v2.2 NEW per v63 lesson):**

Compute and record:

```
stars_per_day = stargazers_count / repo_age_days
fork_ratio = forks_count / stargazers_count
```

Auto-flag:
- `stars_per_day > 300` AND `repo_age_days <= 90` → **Pattern #52 EXTREME-VIRAL candidate; route to viral analysis**
- `fork_ratio > 0.15` → **HIGH active-deployment intent signal** (v64 claude-seo 0.153 / v65 claude-code-system-prompts 0.178)
- `stars_per_day < 1` AND `repo_age_days > 180` → **dormant/abandoned signal**

Engagement-signal sub-investigation (v2.2 NEW per v63 lesson): also capture `watchers / stars` and `open_issues / stars` ratios for ALL subjects — distinguishes drive-by-stars-dominant from active-deployment.

**0.5 Cross-wiki pattern pre-check** (v2.1 EXPANDED; v2.2 unchanged):

```
Check PATTERN_LIBRARY.md:
  - Does new framework fit existing confirmed patterns? (strengthening evidence)
  - Does observation advance any candidate toward confirmation? (flag for audit)
  - Is there notable ABSENCE of prior-wiki patterns? (counter-evidence signal)
  - Do any cross-wiki standards (OpenClaw/Hermes/MCP/AGENTS.md) apply?
  - Are any patterns currently STALE that this wiki might UN-STALE?
  - Could this observation serve as COUNTER-EVIDENCE refining an existing pattern?
  - Would any new candidate OVERLAP >70% with existing candidate? (pre-check)
  - Could this wiki provide N+1 evidence for a recently-registered N=1 candidate? (v2.2 NEW per 1-wiki rapid-evolution detection)
```

**0.6 Candidate overlap pre-check** (v2.1 retained):

Before registering any new candidate at Phase 5:
```
For each proposed new candidate:
  Check existing confirmed + candidate list for >70% overlap:
    - Same structural observation in different words
    - Sub-variant of confirmed pattern
    - Different framing of same phenomenon
  IF overlap:
    Choose: (a) strengthen existing pattern instead
            (b) register as variant-within-pattern (N=2 promotion possible)
            (c) register as meta-pattern consolidation (N=3 promotion possible)
            (d) reject registration
```

**0.7 Sibling detection** (v2 retained):

```bash
ls "/Users/Cvtot/KJ OS Template/03 Projects/" | grep "Beginner Analysis"
```

Enable Phase 4b routing decision based on:
- Same-tier peer (N-way comparison)
- Adjacent-tier peer (taxonomy extension)
- Different-domain (meta-reference or outside-scope)

**0.8 Tier placement decision + Phase 4b PRIMARY pre-registration (v2.2 NEW per v64 lesson):**

Classify framework into tier with justification. **Additionally, when Phase 0 evidence clearly indicates a PRIMARY Pattern Library implication (e.g., promotion-eligible candidate / N=2 strengthening for recent N=1 candidate / corpus-first observation), pre-register the Phase 4b PRIMARY routing mode at Phase 0.**

Example pre-registrations:
- v64 claude-seo: Phase 0 pre-registered Pattern #19 ecosystem-portfolio-builder N=3 PROMOTION as Phase 4b PRIMARY
- v65 claude-code-system-prompts: Phase 0 pre-registered Pattern #78 N=2 ACCELERATED PROMOTION as Phase 4b PRIMARY

**Discipline:** structure Phase 3 entity pages around the PRIMARY deliverable; do NOT retroactively recognize PRIMARY at Phase 4. The PRIMARY entity becomes the most-referenced cross-link target.

**0.9 Storm Bear meta-entity applicability check** (v2.1 STRICT 1-of-4; v2.2 retained + SKIP reallocation expanded):

**STRICT INCLUSION CHECK** — Storm Bear meta-entity included **if AND ONLY IF at least 1 of 4 criteria passes**. Disciplined-skip is default when 0/4.

```
4 inclusion criteria (binary pass/fail; verify with concrete evidence):

(a) Author archetype is structural peer to vault operator
    PASS: solo-VN / solo-Asian-diaspora / solo-engineer-coach / solo-product-lead-non-coder /
          solo-with-ecosystem-portfolio at scale comparable to Storm Bear vault publishing scenario
    FAIL: corporate / large-team / commercial-influencer-at-scale / pseudonymous /
          academic-only / domain-distant-author-archetype

(b) Subject is operational tool vault could deploy/use directly for Scrum-coaching workflows
    PASS: Scrum-applicable agent framework / VN-relevant productivity tool /
          knowledge-graph builder for Markdown vault / multi-runtime escape-hatch /
          ingestion utility for client docs / browser-agent for ticket scraping /
          v2.2 NEW: vault's PRIMARY operating substrate documentation (e.g., v65 Claude Code system prompts)
    FAIL: domain-mismatched / requires-infrastructure-vault-doesn't-have /
          blocked-by-license-for-commercial-Scrum-use

(c) Subject is methodology-influence-node for vault routine v2.1+ maintenance
    PASS: Karpathy / John Lam / Lance Martin / Boris Cherny / SDD / TDD / agentic-engineering /
          methodology-cited-by-other-corpus-frameworks /
          v2.2 NEW: product-level methodology-shaping (e.g., Claude Code prompt envelope shapes routine design)
    FAIL: no-methodology-lineage / personal-authority-claims-only /
          domain-irrelevant methodology

(d) Subject is in-corpus reference (cited by another corpus subject OR cites another corpus subject)
    PASS: explicit citation found via Pattern #57 sub-variant detection (57a/b/c/d) /
          sibling-product to existing corpus subject /
          successor-of or successor-by relationship to corpus subject /
          v2.2 NEW: documents THE most-corpus-cited product's internals (Pattern #57 57c-product
          STRONGEST instance; corpus-recursive at maximum depth)
    FAIL: no cross-corpus reference detected; subject standalone in corpus context

DECISION RULE:
  Sum of PASS criteria ≥ 1 → INCLUDE Storm Bear meta-entity (4th entity slot)
  Sum of PASS criteria = 0 → SKIP meta-entity; apply Phase 0.9 SKIP entity slot reallocation
```

**EXPLICIT REJECTION — non-criteria do NOT justify INCLUDE (unchanged from v2.1):**

❌ **"Cautionary-contrast" / "negation-as-lesson" / "what-not-to-do"** framings
❌ **"Storm Bear could theoretically learn X"** open-ended speculation
❌ **"Preserve consecutive-meta-entity streak"** as inclusion justification

**Phase 0.9 SKIP entity slot reallocation discipline (v2.2 NEW per v64 lesson):**

When 0/4 PASS → SKIP cleanly + **formally reallocate 4th entity slot to Pattern Library implications package**:

- Standard 4-entity structure (Entity 1-4) preserved
- Entity 4 content: Pattern Library implications + cross-pattern coupled-design observations + observational candidates + Library-vocabulary item additions
- Do NOT ship 3-entity wiki
- Do NOT scatter Pattern Library implications across clusters
- v64 demonstrated: Entity 4 = "multi-platform reach + Pattern Library implications package" (claude-seo)

**Storm Bear strength categorization (v2.2 NEW per v65 lesson):**

When 1+ PASS, also categorize INCLUDE strength:
- **WEAK INCLUDE (1/4 STRICT PASS)** — meets minimum bar
- **MODERATE INCLUDE (2/4 STRICT PASS)** — clear-but-bounded relevance
- **STRONG INCLUDE (3/4 STRICT PASS)** — substantial relevance (multiple criteria converge)
- **STRONGEST INCLUDE (4/4 STRICT PASS, or 3/4 STRICT + criterion (d) STRONGEST-IN-CORPUS-HISTORY)** — corpus-recursive maximum-depth observation

v65 example: 3/4 STRICT PASS with (d) STRONGEST-IN-CORPUS-HISTORY = **STRONGEST INCLUDE** in 10-instance window history. Log strength in iteration log + Phase 5 state changes.

**Outcome of Phase 0:**
- Probe complete with 13-axis classification (Living-Domain-Standards axis NEW v2.2)
- Pattern Library pre-checked (presence + absence + strengthening + un-stale + overlap + N+1-rapid-evolution)
- Tier placement decided
- Phase 4b PRIMARY routing mode pre-registered (NEW v2.2 discipline)
- Storm Bear meta-entity applicability decided + strength categorized
- Velocity-screen + engagement-signal computed (NEW v2.2)
- docs/ tree listed (NEW v2.2)
- Consolidation state verified

### Phase 1: Scaffold (10 min) — unchanged from v2.1

**1.1 Folder structure** (standardized v2):

```
<project>/
├── CLAUDE.md
├── COMMANDS.md
├── 00 Sources/     01 Analysis/
├── 02 Wiki/        03 Published/
├── 04 Reviews/     05 Skills/
├── 06 Archive/     07 Inbox/
```

**1.2 CLAUDE.md template** — populate with Phase 0 outputs + pattern-test preview + cross-reference list + **Phase 4b PRIMARY routing pre-registration** (v2.2 NEW).

**1.3 COMMANDS.md** — point to `llm-wiki-routine-v2.2` (this file) + cross-project references.

**1.4 Foundational wiki files:**
- `02 Wiki/(C) index.md` — phase tracking + sources/entities/published planning + cross-wiki siblings
- `02 Wiki/(C) log.md` — append-only timeline
- `01 Analysis/(C) open questions.md` — 20-30 questions

### Phase 2: Source ingestion (30-45 min) — refined v2.2

**Target: 3 cluster summaries** (proven sweet spot v6-v65 = 60 wikis).

**Cluster strategy** (v2 retained; v2.2 unchanged):
- **Cluster 1:** User-facing docs (README + translations + landing docs)
- **Cluster 2:** Contributor-facing docs (CLAUDE + AGENTS + CONTRIBUTING + SECURITY + etc.)
- **Cluster 3:** Technical/distribution (architecture + packaging + integrations) — for CHANGELOG-heavy subjects, this cluster may absorb the CHANGELOG-as-evidence content (per v64+v65 pattern)

**Per cluster (v2.1 + v2.2 additions):**
- Extract verbatim positioning / philosophy / key claims
- Document 8-12 corpus-first observations
- Check against Pattern Library — does cluster advance any candidate?
- Note ABSENCES as much as presences
- External URL resolution: if cluster references catalogs/guides hosted externally, fetch them
- Flag supply-chain risk if cluster documents untrusted-code ingestion
- Flag counter-evidence to existing patterns (not just confirming observations)
- **NEW v2.2: Flag Living-Domain-Standards evidence** — does cluster contain dated external-authority citations + deprecation-tracking + versioned absorption ledger?
- **NEW v2.2: Source-celebrity-derivative-distillation criteria check** — when subject distills public observations of a corpus-foundation individual/product, capture all 4 criteria: (1) author ≠ source, (2) explicit source attribution with URL, (3) public observations as raw material, (4) installable artifact packaging

**Output per cluster:**
- `02 Wiki/(C) <cluster-name> cluster summary.md` (~15-section format)
- Update `(C) log.md` after each cluster
- Update `(C) index.md` Sources table

### Phase 3: Entity pages (40 min) — refined v2.2

**Target: 4 entity pages** (v2 retained; v2.2 unchanged in count).

**Entity selection logic (v2.2 refined — Phase 4b PRIMARY-aware):**

1. **Core product entity** — what does this framework DO
2. **Distribution/ecosystem entity** — how is it delivered + integrated
3. **Novel pattern entity / Phase 4b PRIMARY entity (v2.2 NEW)** — when Phase 0 pre-registered a PRIMARY Pattern Library implication, this entity IS that PRIMARY deliverable (e.g., v64 Entity 2 = Pattern #19 N=3 / v65 Entity 2 = Pattern #78 N=2)
4. **Tier meta + Storm Bear entity (if Phase 0.9 PASS) OR Pattern Library implications package (if Phase 0.9 SKIP per reallocation discipline)**

**Format: 13-section canonical** (from `llm-wiki-ingest.md`) — unchanged.

**Cross-references MANDATORY:**
- Every entity references ≥3 sibling wikis
- Pattern Library entries referenced where applicable
- Novel observations tagged as Pattern candidates in PATTERN_LIBRARY.md update
- Counter-evidence observations tagged explicitly

**Storm Bear meta-entity (v2.2 — conditional + strength-categorized):**
- Apply STRICT 1-of-4 inclusion check from Phase 0.9
- When included: categorize strength (WEAK / MODERATE / STRONG / STRONGEST) per Phase 0.9 expansion
- When skipped: apply Phase 0.9 SKIP entity slot reallocation discipline — Entity 4 = Pattern Library implications package

### Phase 4a: Beginner bilingual guide (15 min) — unchanged from v2.1

**Output:** `03 Published/(C) <repo> - Huong dan cho nguoi moi.md`

**Structure (12-13 parts; v2.2 unchanged from v2.1):**
1. What is it? (bilingual)
2. Corpus-first signals
3. Tier placement
4. Installation
5. Core usage pattern
6. Novel concepts / key architectural choices
7. vs other corpus frameworks
8. Ethical framing (include if autonomy-max tagline OR controversial positioning OR supply-chain risk surface)
9. Storm Bear relevance (VN operator + Scrum coach fit)
10. 4-week learning roadmap
11. Tradeoffs + limitations
12. Caveats + safety notes (supply-chain awareness when applicable)
13. References + next action

**Length:** 400-700 lines. Bilingual (VN primary, EN technical).

### Phase 4b: Routing-dependent deliverable (20-30 min) — expanded v2.2

**~26 routing modes observed (v1-v65):**

Modes 1-25 from v2.1 retained. v2.2 adds:

| Mode | Trigger | Example |
|------|---------|---------|
| **NEW Pattern candidate proposal-document (v2.2)** | Phase 4b generates NEW top-level candidate | v64 Pattern #19 N=3 proposal / v65 Pattern #78 N=2 proposal |

**v2.2 NEW Pattern candidate proposal-document discipline:**

When Phase 4b generates a PROMOTION-ELIGIBLE candidate OR a NEW top-level candidate, **draft formal proposal-document at `01 Analysis/`** structured per audit criteria:

- Title: `(C) Pattern-NN <pattern-name> N=<count> promotion proposal.md`
- Sections: current status / N=<count> evidence (per-subject 3-criteria evaluation) / structural diversity table / promotion criteria evaluation (5 criteria) / recommended verdict / acceleration consideration if applicable / sub-taxonomy decision / audit checklist / evidence document cross-references
- Length: 200-400 lines (substantive but not exhaustive)
- Purpose: enables next-audit operator to deliberate efficiently without re-deriving evidence

Exemplars: `03 Projects/claude-seo - Beginner Analysis/01 Analysis/(C) Pattern-19 ecosystem-portfolio-builder N=3 promotion proposal.md` + `03 Projects/claude-code-system-prompts - Beginner Analysis/01 Analysis/(C) Pattern-78 Living-Domain-Standards Tracking N=2 promotion proposal.md`

**Routing decision:**
- Review modes — which applies primarily?
- Pick 1 primary mode (PRE-REGISTERED at Phase 0 per v2.2 discipline), up to 2 secondary
- Output template driven by mode

**Output:** `03 Published/(C) <mode-specific-name>.md` OR `01 Analysis/(C) Pattern-NN proposal.md` (when proposal-document discipline applies)

**Length:** 500-750 lines (Phase 4b primary deliverable) OR 200-400 lines (Phase 4b proposal-document).

### Phase 5: Iteration log + Pattern Library update (10-15 min) — expanded v2.2

**Output:** `04 Reviews/(C) YYYY-MM-DD v<N> build learnings.md` OR `01 Analysis/(C) iteration-log.md` (v64+ convention)

**Structure (v2.2 standardized):**

1. **Phase-by-phase log** (table format: phase / status / duration / notes)
2. **Key decisions made**
3. **Surprises + corrections**
4. **Pattern Library implications snapshot** (state table)
5. **v66/v67 audit agenda accumulated** (running queue of pre-registered items)
6. **Cross-wiki sibling decisions**
7. **Files written at v<N>**
8. **Velocity comment**
9. **What's notable about v<N>** — corpus-firsts + corpus-records

**Pre-Phase-6 fact-verification expanded (v2.2 per v63 lesson):**

Before Phase 6 vault sync, verify:

1. **Numbered-pattern references** (v2.1 baseline) — for each "#NN" pattern reference in wiki files, verify against PATTERN_LIBRARY.md (existence + correct name + accurate status)
2. **Pattern Library evidence lists** (v2.2 NEW) — verify evidence lists for confirmed/candidate patterns are CURRENT to last 3-5 wikis (not just internally-consistent)
3. **Streak counters** (v2.2 NEW) — verify Storm Bear meta-entity streak count + ZERO-NEW-ACTIVE-CANDIDATES streak count + INCLUDE rate window calculations
4. **Cross-reference link integrity** — verify all `[v<N> <subject>](../<path>)` links resolve to existing files

**Pre-Phase-6 retroactive-correction-check (v2.2 NEW per v63 lesson):**

Before Phase 6, check whether v<N> evidence retroactively corrects a prior wiki's Pattern Library register:

- v62→v63 example: codex-plugin-cc v62 qualified for Pattern #52 strengthening (~847 stars/day) but v62 wiki did NOT register; v63 wiki caught + corrected
- v64→v65 example: claude-seo v64 registered Pattern #78 N=1; v65 evidence makes N=1 stale-flag stale-by-N=2-evidence (1-wiki cycle)

Mechanism: log retroactive correction in iteration log + flag at next audit as gap-closure item.

**1-wiki rapid-evolution detection discipline (v2.2 NEW per v65 lesson):**

When v<N> provides evidence to evolve v<N-1>'s pattern registration (N+1 rapid evolution):

1. Log meta-observation as Library-vocabulary item #10 candidate
2. Consider promotion-acceleration: if N=2 evidence achieved at v<N-1>+1, consider accelerating promotion to next audit (vs default stale-check window)
3. Track as observational meta-pattern: "rapid-pattern-evolution observational track"

Documented cycles:
- v62→v63 Pattern #76 1-wiki counter-evidence cycle (2026-05-07/08)
- v64→v65 Pattern #78 1-wiki un-stale-via-N=2-evidence cycle (2026-05-13/14, TIED FASTEST)

**Engagement-signal sub-investigation discipline (v2.2 NEW per v63 lesson):**

Phase 5 records for EVERY subject (not only viral subjects):

- `stars_per_day`
- `fork_ratio` (forks/stars)
- `watchers_ratio` (watchers/stars)
- `open_issues_ratio` (open_issues/stars)

High fork_ratio (>0.15) signals active-deployment intent — v64 claude-seo 0.153 + v65 claude-code-system-prompts 0.178 = corpus-record back-to-back.

**Pattern Library update (v2.2 expanded discipline):**

Phase 5 directly updates `_patterns/03-active-candidates.md` + `_patterns/05-recent-additions.md`:

**Registration checks before adding candidate (v2.1 retained):**
- Overlap pre-check (Phase 0.6): >70% overlap → reject or consolidate
- Consolidation-forward discipline: if 2+ prior observations would be subsumed by proposed meta-pattern, register as meta-pattern
- N=1 stale-risk flagging: novel single-observation candidates flag at registration with "stale-risk-flagged" note

**Registration actions:**
- New candidate entry in Active Candidates section
- Update N=1 stale-tracking table with v+5 stale-check and v+10 retire-check
- Update count in Active Candidates section header
- Strengthen existing pattern evidence where applicable
- Un-stale check
- **NEW v2.2: 1-wiki rapid-evolution check** — does this v<N> provide N+1 evidence for v<N-1>'s newly-registered candidate? Flag for promotion acceleration

**Classification options (v2.1 + v2.2):**

| Status | When to assign |
|--------|---------------|
| 🟡 CANDIDATE | Default for 1-2 observations OR single-tier-confined |
| 🔍 OBSERVATION-TRACK | Event-based or episodic observation; not architectural pattern |
| Stale-risk-flagged at registration | N=1 candidate with one-off characteristics |
| **N+1 ACCELERATED (v2.2 NEW)** | Candidate received N+1 evidence within 1-wiki of registration; promotion-acceleration candidate at next audit |

### Phase 6: Vault sync (10 min) — refined v2.2

**Required updates:**

1. **Project `(C) index.md`** → all phases ✅
2. **Project `(C) log.md`** → append Phase 2-6 completion entry
3. **Root `CLAUDE.md`** → add project entry with milestones + deliverables + pattern tests + pilot ranking update
4. **Root `GOALS.md`** → append version log entry with corpus milestones + Pattern Library changes + next options
5. **Root `PATTERN_LIBRARY.md` / `_patterns/03-active-candidates.md` / `_patterns/05-recent-additions.md`** → direct update with new candidates + refinements + un-stale flags + promotion proposals + retroactive corrections (v2.2 NEW)

**Consistency check (v2.1 retained):**
- Counts across all vault files (PATTERN_LIBRARY / GOALS / CLAUDE / project-CLAUDE) must match
- Dates consistent
- Ratio computed correctly (active/confirmed; numerator:denominator label consistent)

**Reference Claude Code system prompts when designing vault routine changes (v2.2 NEW per v65 lesson):**

When Phase 6 routine-relevant updates are being made (e.g., updating routine v2.2 itself, brain-setup, weekly-update), consult v65 `claude-code-system-prompts` archive:

- `system-prompts/system-prompt-doing-tasks-software-engineering-focus.md` — Claude Code's stance on software-engineering tasks
- `system-prompts/system-prompt-memory-instructions.md` — Claude Code's memory file format expectations
- `system-prompts/system-prompt-tool-usage-task-management.md` — Claude Code's TodoWrite discipline
- `system-prompts/agent-prompt-managed-agents-onboarding-flow.md` — Anthropic's structured-onboarding model

Goal: ensure vault routine design aligns with Claude Code's prompt envelope rather than assumes against it.

---

## Mini-audit protocol (v2.2 expanded — 4 audit classes)

**Trigger conditions (v2.1 retained):**
- Ratio 0.95:1 - 1.05:1 (proactive, pre-trigger)
- Accumulated promotion-ready candidates (N=2 structurally-unambiguous across 2+ candidates)
- Operator request
- **v2.2 NEW: 1-wiki rapid-evolution detection** — when v<N> provides N+1 evidence within 1-wiki of v<N-1> registration, operator may elect promotion-acceleration at v<N+1> audit instead of awaiting natural cadence

**Scope (focused — not full audit):**
- Promotion review for specific candidates (not blanket review)
- Stale-flag retroactive application if threshold crossed
- Formulation extensions (not new patterns)
- Absorption-retirement when superseding pattern promotes
- 30-90 minute duration target (v2.2 widened upper bound from 60min v2.1 — recent audits trended 75-90min)

**Deliverables:**
- `04 Reviews/(C) YYYY-MM-DD Pattern Library mini-audit post-v<N>.md` (~300-600 lines)
- PATTERN_LIBRARY.md updates (promotions + retirements + extensions)
- GOALS.md session entry
- CLAUDE.md state block
- **v2.2 NEW: Updated 31-candidate routine v2.2/v2.3 codification candidates list**

**4 Mini-audit classes (v2.2 — was 3 in v2.1):**

1. **CONSERVATIVE-DISCIPLINE class (v2.1 baseline)** — focused; zero state transitions; mainly defer + register
2. **STRENGTHENING-DOMINANT class (v2.1 baseline)** — within-pattern strengthening focus; few promotions
3. **STRENGTHENING-DOMINANT EXTENDED class (v2.1 v60)** — wider scope than standard STRENGTHENING-DOMINANT; multi-pattern audit
4. **EARLY-OPERATOR-ELECTED class (v2.2 NEW per v63 lesson)** — operator elects mini-audit BEFORE natural-cadence trigger when high-impact promotion is ripe (e.g., LONGEST stale arc; v63 EARLY mini-audit at 2026-05-07 elected at ratio 0.452:1 vs 0.95:1 trigger threshold)

**Distinction from full audit:**
- Full audit: comprehensive scope, ~1-2h, reviews all candidates, introduces new criteria
- Mini-audit: targeted scope, ~30-90min, specific promotions + adjustments, no new criteria unless emergent from targeted review

**Acceleration audit pattern (v2.2 NEW per v65 trigger):**

When operator elects to run audit at +1 wiki (vs +2-3 wiki natural cadence), apply:
- Scope: PRIMARY items from recent wiki ship + DUAL-PRIMARY items if v<N-1> + v<N> both contributed PRIMARY-tier evidence
- Duration: aim for tight 60-90 min execution; defer non-PRIMARY items to natural-cadence audit
- Example: v66 audit at v65 trigger = Pattern #19 N=4 + Pattern #78 N=2 ACCELERATED PROMOTION as DUAL PRIMARY

---

## Audit cadence reform (v2.1 retained; v2.2 unchanged)

| Ratio zone | Trigger | Action |
|-----------|---------|--------|
| < 0.75:1 | Healthy | No action required |
| 0.75-0.95:1 | Healthy | Monitor; strengthen-over-discover discipline |
| 0.95:1 | Mini-audit zone | Lightweight rebalance (~30-90min); targeted promotions |
| 1.05:1 | Full audit trigger | Comprehensive review (~1-2h); systematic promotion + retirement |
| > 2.0:1 | Hard block | No new wikis until cleared |
| Action-backlog > 100 | Hard block | Routine refactor required |

**Operator-elected acceleration (v2.2):**

Operator may elect mini-audit BELOW the 0.95:1 trigger when:
- High-impact promotion is ripe (LONGEST stale arc / structural-diversity N=3+ / 1-wiki rapid-evolution N=2)
- DUAL-PRIMARY items accumulated (2+ PRIMARY-tier deliberations queued)
- Routine v2.x codification candidates exceed 30 accumulated

---

## 5 + 1 promotion-counting dimensions (v2.2 expanded — was 5 in v2.1)

Pattern Library CONFIRMED status can be achieved via 5 paths PLUS 1 NEW counting-dimension:

### 5 structural-promotion criteria (v2.1 retained)

| # | Criterion | Introduced | First use |
|---|-----------|-----------|-----------|
| 1 | Default: ≥3 observations across 2+ tiers | v1 baseline | Multiple |
| 2 | Structural-unambiguity-at-N=2 | v1 baseline | Multiple |
| 3 | Spectrum-pattern-at-N=2 | v29 audit | Pattern #51 Vibe-Coding |
| 4 | Variant-within-pattern-at-N=2 | v29 audit | Pattern #17 variant 5 |
| 5 | Meta-pattern-at-N=3-consolidation | v31 mini-audit | Pattern #68 Awesome-List-Genre |

### NEW counting-dimension (v2.2 per v63 lesson)

**Cross-archetype N-counting as separate dimension from cross-tier counting.**

When counting toward criterion #1 (≥3 cross-tier) or criterion #2 (structural-N=2), explicitly distinguish:

- **Cross-tier count**: number of distinct tiers (T1/T2/T3/T4/T5) where pattern observed
- **Cross-archetype count** (NEW v2.2): number of distinct author archetypes (solo-individual / solo-Japanese / corporate-org / academic-lab / etc.) where pattern observed

Pattern #21 SDD Methodology Emergence v63 promotion via N=4 cross-archetype (4 distinct organizational archetypes) demonstrated this counting dimension. Promotion may satisfy either or both counting dimensions; both should be evaluated at audit.

**v65 example**: Pattern #78 Living-Domain-Standards Tracking N=2 cross-archetype (solo-individual AgriciDaniel + corporate-org Piebald-AI) PLUS N=2 sub-mechanism (78a multi-vendor + 78b single-vendor-product-internals) — promotion satisfies criterion #2 structural-unambiguity-at-N=2 AND cross-archetype N=2 dimension.

---

## Library-vocabulary items (v2.2 expanded — 10 items)

Cross-pattern observations that don't fit existing patterns but capture corpus-level meta-observations.

### Item #1-#8 (pre-v2.2 baseline)

(Items #1-#8 retained from prior routine versions; brief mention; full text in `_patterns/05-recent-additions.md` archive.)

### Item #9: cross-pattern coupled-design correlations (v60 baseline; v2.2 strengthened)

When multiple patterns co-occur at single wiki, log as cross-pattern coupled-design observation.

**Evidence at v60 free-claude-code (N=4 baseline):** Pattern #57 polarity × Pattern #51 vibe × Pattern #19 archetype × tier — content-translation T4 sub-archetype

**Strengthening at v54 gsd-2 (N=3 3-pattern triple):** Pattern #57 × Pattern #58 × Pattern #18 — Pi-SDK-substrate triple

**Strengthening at v65 claude-code-system-prompts (CORPUS-RECORD N=5+):** Pattern #78 78b + Pattern #21 21b + Pattern #19 19d + Pattern #57 57c-product STRONGEST + Pattern #66 meta-supply-chain-awareness sub-category + NEW Pattern #79 — 5 patterns + 1 NEW candidate co-occurring at single wiki

**Disciplinary use:** when N=4+ patterns co-occur at single wiki, log as item #9 strengthening evidence at Phase 5; consider promoting cross-pattern coupled-design from observational to formal Pattern Library item if N≥3 at corpus-record scale.

### Item #10: 1-wiki rapid-pattern-evolution observational track (NEW v2.2 per v65 lesson)

When patterns register and immediately receive corpus evidence to evolve within 1-wiki, log as rapid-pattern-evolution observation.

**Evidence at v62→v63 (1-wiki counter-evidence cycle for Pattern #76):** Pattern #76 Adversarial Subagent Review Architecture registered v63 mini-audit 2026-05-07; codex-plugin-cc v62 wiki ship 2026-05-08 provided 1-wiki counter-evidence (1-day gap).

**Evidence at v64→v65 (1-wiki un-stale-via-N=2-evidence cycle for Pattern #78):** Pattern #78 Living-Domain-Standards Tracking registered v64 wiki ship 2026-05-13; claude-code-system-prompts v65 wiki ship 2026-05-13/14 provided 1-wiki N=2 evidence (0-1 day gap). **TIED FASTEST cycle in 64-wiki corpus history.**

**Disciplinary use:** when 1-wiki rapid-evolution detected at Phase 5, flag as item #10 strengthening evidence + consider promotion-acceleration at next audit (vs default stale-check window).

---

## Strengthen-over-discover discipline streak metric (NEW v2.2 per v63 lesson)

Track **ZERO-NEW-ACTIVE-CANDIDATES streak** as Pattern Library health metric.

**Definition:** count of consecutive wikis where Pattern Library candidate count stays unchanged (within-pattern strengthening only; no NEW top-level candidates registered).

**Healthy interpretation:** longer streaks signal mature corpus + consolidation-forward discipline. Most observations strengthen existing patterns rather than registering new ones.

**Broken streak interpretation:** when a wiki registers NEW candidates (e.g., 10 corpus-firsts at v61 cc-sdd / 2 NEW at v64 / 1 NEW at v65), the streak breaks legitimately if evidence justifies. Broken streaks at single-wiki points signal genuinely-novel evidence admittance is healthy outcome.

**Historical streaks:**
- v37-v60 = 24-streak (LONGEST in corpus pre-v61)
- v61 BROKE streak (10 corpus-firsts) — legitimate corpus-novelty
- v62 = back to streak (within-pattern only)
- v63 = within-pattern + retroactive correction (no NEW top-level)
- v64 BROKE streak (+2 NEW)
- v65 BROKE streak (+1 NEW)

**v2.2 codification:** Phase 5 must record streak status (preserved / broken / restarted) + categorize broken-streak as legitimate corpus-novelty vs over-registration concern.

---

## Source-celebrity-derivative-distillation criteria (NEW v2.2 per v63 lesson)

When subject distills public observations of a corpus-foundation individual or product, capture all 4 criteria:

1. **Author ≠ source individual/product** (distillation by third party)
2. **Explicit source attribution with URL** (not paraphrasing; verifiable citation)
3. **Public observations as raw material** (not private docs / not collaboration)
4. **Installable artifact packaging** (creates new artifact from observations)

**Evidence: v63 andrej-karpathy-skills** — forrestchang distills Karpathy's public X-tweet observations into installable `karpathy-guidelines` skill with explicit URL attribution.

**Disciplinary use:**
- Trigger Pattern #57 57c sub-variant detection (corpus-foundation-individual inheritance)
- Trigger Pattern #19 a4 sub-type registration (source-celebrity-derivative-distillation)
- Consider Pattern #52 EXTREME-VIRAL implication (source-celebrity derivatives often viral-velocity candidates)

---

## EXTREME-VIRAL sub-archetype 3-axis discipline (NEW v2.2 per v63 lesson, Pattern #52)

When N=3 cross-archetype reached for viral patterns, register sub-archetypes alongside top-level pattern.

**Pattern #52 N=3 sub-archetypes (registered v63):**
- **52a author-celebrity-driven** (N=1: mattpocock-skills v57)
- **52b corporate-celebrity-driven** (N=1: codex-plugin-cc v62 — retroactive correction)
- **52c source-celebrity-derivative** (N=1: andrej-karpathy-skills v63)

**Sustained-velocity criterion deferred to v69 audit (~6mo+ window):**
- All 3 sustain >100 stars/day at 6mo → promote to confirmed EXTREME-VIRAL pattern
- All 3 decay below <50 stars/day at 6mo → reformulate as EXTREME-VIRAL-BURST-AND-DECAY observational
- Mixed → split into sustained-vs-burst sub-variants

**Disciplinary use:** when Pattern #52 strengthening evidence appears (stars/day >300 in first 90 days), categorize sub-archetype + register at corresponding 52a/52b/52c slot.

---

## Anti-vibe-with-pragmatic-acknowledgment Pattern #51 sub-pole (NEW v2.2 per v61+v63 lessons)

Counter-evidence narrowing Pattern #51 Vibe-Coding Spectrum scope.

**Background:** Pattern #51 Vibe-Coding Spectrum was registered with 2-pole observation (anti-vibe at one end / max-vibe at other).

**v61 cc-sdd evidence:** gotalab anti-vibe with explicit pragmatic-acknowledgment — *"Yes, vibe-coding gets you to MVP fast. We acknowledge this."* — explicit acknowledgment of opposite pole's value PLUS critique of long-term cost.

**v63 evidence reinforces:** karpathy-skills NEUTRAL-with-anti-overengineering — narrower critique scope.

**v2.2 codification:**
- 51a anti-vibe with explicit-pragmatic-acknowledgment (v61 cc-sdd baseline)
- 51b NEUTRAL with anti-overengineering pole (v63 karpathy-skills)
- 51c anti-pattern-foil polarity (v57 mattpocock + v58 OpenSpec — N=2 distinct citing-subjects targeting v17 spec-kit)
- 51d positive-comparison-parallel polarity (v60 free-claude-code "...like OpenClaw")

**Disciplinary use:** when Pattern #51 strengthening evidence appears, categorize at corresponding sub-pole. v66+ audit deliberation: continue spectrum reformulation with sub-pole tracking.

---

## Lineage-test → independence-test → promotion 3-step un-stale arc (NEW v2.2 per v63 lesson)

When un-stale candidate fails lineage-test (same lineage as existing evidence), evaluate independence-test on subsequent wikis:

**Step 1 (lineage-test):** does N+1 evidence come from independent lineage vs existing N=1 evidence?
- If YES → criterion #2 structural-N=2 evaluation
- If NO → defer; await independence-test on later wiki

**Step 2 (independence-test):** does evidence from later wiki provide independent lineage?
- If YES → promotion candidate at next audit
- If NO → continue stale-flag; re-evaluate at next stale-check window

**Step 3 (promotion):** at audit, evaluate per 5 structural-promotion criteria + cross-archetype N-counting dimension

**v60→v61→v63 example:** Pattern #21 SDD Methodology Emergence
- v60 audit: REJECTED un-stale (lineage-test failed; spec-kit + cc-sdd shared lineage at Kiro IDE)
- v61 cc-sdd ship: REGISTERED but lineage-test still ambiguous
- v63 EARLY mini-audit: PROMOTED via N=4 cross-archetype (independence-test satisfied; 4 distinct organizational archetypes confirmed)

**Disciplinary use:** when un-stale event detected, explicitly run 3-step arc; document lineage-test result + independence-test status + promotion verdict.

---

## Absorption-retirement mechanism (v2.1 retained; v2.2 unchanged)

**Distinct from stale-retirement.**

**Trigger:** Candidate is subsumed by a superseding pattern (parent pattern promotes, variant-pattern promotes, or meta-pattern promotes).

**Mechanism:**
1. Move candidate formal-statement substance into superseding pattern as sub-observation
2. Mark original candidate "RETIRED (absorbed)" in Retired section
3. Keep historical record with "Revive if..." clause documenting what new evidence would re-justify standalone

---

## Un-stale mechanism (v2.1 retained; v2.2 expanded with 1-wiki acceleration variant)

**Purpose:** Re-activate stale candidates when 2nd observation appears.

**Standard flow (v2.1 retained):**
1. Stale-candidate (N=1 since 5+ wikis ago) gets 2nd observation in new wiki
2. Mark "✅ UN-STALED v<N>" in stale-tracking table
3. Move from STALE to active candidate with strengthened evidence
4. Typically flagged as promotion-candidate for next audit

**1-wiki acceleration variant (v2.2 NEW per v65 lesson):**
1. Candidate registered N=1 stale-flagged at v<N-1>
2. v<N> provides N=2 evidence within 1-wiki
3. Mark "✅ N+1 RAPID-EVOLUTION at v<N>" in stale-tracking table
4. Flag for promotion-acceleration at next audit (vs default stale-check at v<N-1+5>)
5. Cross-link to Library-vocabulary item #10 1-wiki rapid-pattern-evolution observational track

**v65 example:** Pattern #78 registered v64 → N=2 at v65 = 1-wiki acceleration. Acceleration recommendation at v66 audit (vs default v67 stale-check).

---

## Counter-evidence-driven refinement (v2.1 retained; v2.2 unchanged)

**Purpose:** Pattern formulation adjustment when counter-example demonstrates over-broad scope.

**Trigger:** New wiki provides structural counter-example to confirmed pattern formulation.

**Flow:**
1. Evaluate counter-evidence: does it invalidate pattern or narrow scope?
2. If invalidate: retire pattern
3. If narrow-scope: apply REFINED formulation preserving core observation at narrower scope

**Disciplinary use:** counter-evidence strengthens pattern by tightening scope, not just adding data points.

---

## OBSERVATION-TRACK sub-category (v29 audit — v2.1 codified; v2.2 unchanged)

**Purpose:** Retain episodic / event-based observations without forcing architectural-pattern framing.

**Criteria for reclassification:**
- Observation is event-based (specific incident response) not repeatable architectural choice
- Response pattern is reactive to external events, not structural framework-design decision
- Episodic nature doesn't fit N-observation promotion criteria

---

## Stream-timeout resume protocol (v2.1 retained; v2.2 unchanged)

**Scenario:** Delegated wiki builds to subagent may hit stream timeouts mid-execution.

**Resume flow:**
1. Check what files were created (Phase 1, 2, 3 output)
2. Read project `CLAUDE.md` + key entity files to understand prior agent's decisions
3. Spawn new agent with resume-prompt listing: completed work + remaining work + authoritative context files
4. Verify consistency across phases in final Phase 6 fact-verification check

---

## Completion criteria (refined v2.2)

Routine reports DONE only when:

- [ ] Phase 0 complete with 13-axis classification (v2.2 NEW Living-Domain-Standards axis) + overlap pre-check + un-stale check + 1-wiki rapid-evolution check + velocity-screen + engagement-signal computed + docs/ tree listed (v2.2 NEW) + Phase 4b PRIMARY pre-registered if applicable (v2.2 NEW)
- [ ] Phase 1 scaffold (project + 8 subfolders + foundational files; CLAUDE.md includes PRIMARY routing preview)
- [ ] Phase 2 = 3 cluster summaries (with counter-evidence + supply-chain flags + Living-Domain-Standards flag + source-celebrity-derivative-distillation criteria if applicable)
- [ ] Phase 3 = 4 entity pages (13-section format, cross-refs mandatory; meta-entity conditional with strength categorization v2.2 NEW; SKIP reallocation discipline v2.2 NEW)
- [ ] Phase 4a beginner guide (400-700 lines, bilingual, with ethical/supply-chain framing if applicable)
- [ ] Phase 4b routing-mode-specific deliverable (500-750 lines OR 200-400 lines proposal-document per v2.2 discipline)
- [ ] Phase 5 iteration log + PATTERN_LIBRARY.md update with overlap-pre-check + consolidation-forward discipline + retroactive-correction-check (v2.2 NEW) + 1-wiki rapid-evolution detection (v2.2 NEW) + strength-categorized meta-entity (v2.2 NEW) + engagement-signal recording (v2.2 NEW)
- [ ] Phase 6 vault sync (project index/log + root CLAUDE/GOALS/PATTERN_LIBRARY) + fact-verification expanded (v2.2 NEW: evidence list current 3-5 wikis + streak counters + cross-ref integrity) + consistency-check + reference Claude Code system prompts if routine-relevant updates (v2.2 NEW)
- [ ] Final report with deliverable counts + velocity + strategic recommendation + backlog escalation if applicable

---

## Status protocol (v2 retained; v2.2 unchanged)

Routine returns 1 of 5 statuses:

- **DONE** — all phases complete, no concerns
- **DONE_WITH_CONCERNS** — complete but issues flagged
- **BLOCKED** — can't self-resolve
- **NEEDS_CONTEXT** — need more info
- **BLOCKED_CONSOLIDATION** — consolidation guard triggered

---

## Defaults (evolved via 65 wikis)

| Default | Value | Evidence |
|---------|-------|----------|
| Bilingual | VN primary + EN technical | 65 wikis |
| Format | 13-section canonical | `llm-wiki-ingest.md` |
| Cluster summaries | 3 | v6-v65 |
| Entity pages | 4 | v10-v65 standardized |
| Beginner guide length | 400-700 lines | 60+ wikis |
| Phase 4b deliverable | 500-750 lines (standard) OR 200-400 lines (proposal-document v2.2 NEW) | v64-v65 |
| Iteration log length | ~300-500 lines | 60+ wikis |
| Velocity target | ~2 hours/wiki | v6-v65 plateau (60 wikis) |
| Continuous execution | YES | 60+ wikis |
| WebFetch-first | YES | v6+ lesson |
| Cross-wiki links | MANDATORY | 60+ wikis |
| Pattern Library update | REQUIRED Phase 5 | v2+ |
| Storm Bear meta-entity | STRICT 1-of-4 PASS REQUIRED (v2.1+); strength-categorized v2.2 | v56+ |
| External URL fetching | When referenced | v2+ |
| Branch fallback | Main → master → v4 → dev | v2+ |
| Overlap pre-check | REQUIRED Phase 0.6 | v28+ |
| Consolidation-forward discipline | ON | v31+ |
| Un-stale check | Phase 0.5 + Phase 5 | v30+ |
| Counter-evidence check | Phase 2 per cluster | v29+ |
| Fact-verification pre-Phase-6 | REQUIRED (v2.1 baseline + v2.2 EXPANDED evidence-list + streak-counter checks) | v31+ |
| **Velocity-screen automation (v2.2)** | REQUIRED Phase 0 | v63+ lesson |
| **docs/ tree-listing (v2.2)** | REQUIRED Phase 0.4 | v61 lesson |
| **Engagement-signal sub-investigation (v2.2)** | REQUIRED Phase 0 + Phase 5 | v63 lesson |
| **Phase 4b PRIMARY pre-registration (v2.2)** | REQUIRED at Phase 0 when applicable | v64 lesson |
| **NEW Pattern proposal-document (v2.2)** | REQUIRED at Phase 4b for NEW top-level candidates | v64-v65 lesson |
| **Phase 0.9 SKIP entity slot reallocation (v2.2)** | REQUIRED when STRICT yields SKIP | v64 lesson |
| **Pre-Phase-6 retroactive-correction-check (v2.2)** | REQUIRED | v63 lesson |
| **1-wiki rapid-evolution detection (v2.2)** | Phase 5 | v65 lesson |
| **Reference Claude Code system prompts when designing vault routine changes (v2.2)** | Recommended at Phase 6 routine-relevant updates | v65 lesson |

---

## Velocity targets (v2 retained; v2.2 widened for HIGH-density subjects)

| Repo size | Phase 2 | Phase 3 | Total | Wiki reference |
|-----------|---------|---------|-------|----------------|
| Small | 20-30 min | 30 min | ~1.5h | codymaster v12 |
| Medium | 30-45 min | 40 min | ~2h | **Plateau v6-v65** |
| Large | 45-60 min | 50-60 min | 2.5-3h | spec-kit v17, agency-agents v18, OpenHands v30 |
| Very large | 60-90 min | 60-90 min | 3-4h | paperclip v14 |
| **HIGH source-density (v2.2 NEW)** | 60-75 min | 60-75 min | ~2-2.5h | claude-seo v64 (~117 min), claude-code-system-prompts v65 (~130 min) |

**Plateau observation (v2.2 update):** 60 consecutive wikis (v6-v65) completed at ~2h. v64 + v65 demonstrate HIGH source-density extension (~2-2.5h acceptable when CHANGELOG >200KB / primitive-count >40 / DUAL PRIMARY Phase 4b).

---

## Anti-patterns (v2.2 expanded — was 18 in v2.1; v2.2 adds 5 NEW; total ~23)

❌ **Interview questions** — routine is autonomous by design
❌ **Skip Phase 5 iteration log** — log is how routine compounds
❌ **Skip vault sync (Phase 6)** — root files must stay current
❌ **Fabricate counts** — always verify with filesystem commands
❌ **Skip cross-project links** — unique vault value
❌ **Skip consolidation guard** — library integrity requires it
❌ **Skip Pattern Library update** — patterns drift otherwise
❌ **Skip absence detection** — absences as informative as presences
❌ **Over-promote patterns** — respect 5+1 promotion-counting dimensions (v2.2 expanded)
❌ **Silent assumption on tier placement** — document rationale
❌ **Force fit to existing patterns** — novel observations deserve candidates; counter-evidence deserves refinement
❌ **Skip overlap pre-check** — register new candidate only if <70% overlap with existing
❌ **Register standalone when consolidation-forward applies** — prefer meta-pattern if ≥2 prior observations would be subsumed
❌ **Ignore stale-candidates at Phase 0** — un-stale check is part of cross-wiki pattern pre-check
❌ **Re-use numbered-pattern references without fact-verification** — v31 showed #35 mislabel cascading
❌ **Defer operator-facing vault actions indefinitely** — backlog >5 sessions = escalate to BLOCKING-RECOMMENDATION
❌ **Register N=1 candidate without stale-risk evaluation** — one-off observations should flag at registration
❌ **Cautionary-contrast as Phase 0.9 inclusion criterion** — REJECTED at session 66; STRICT 1-of-4 hard requirement
❌ **Skip Phase 0 velocity-screen** (v2.2 NEW per v62 audit gap lesson) — auto-compute stars/day always; manual skipping causes pattern mis-classification (v62 codex-plugin-cc qualified Pattern #52 but v62 wiki did NOT register because viral-routing wasn't triggered)
❌ **Defer NEW Pattern candidate proposal-document** (v2.2 NEW per v64-v65 lesson) — drafting formal proposal at `01 Analysis/` is part of Phase 4b for NEW candidates; deferring loses audit-ready evidence package
❌ **Skip Phase 0.9 SKIP entity slot reallocation** (v2.2 NEW per v64 lesson) — when STRICT yields SKIP, reallocate 4th slot to Pattern Library implications; do not ship 3-entity wiki
❌ **Re-derive Claude Code prompt envelope from memory when codifying vault routines** (v2.2 NEW per v65 lesson) — consult `claude-code-system-prompts` archive (v65 wiki subject) for ground-truth
❌ **Skip retroactive-correction-check** (v2.2 NEW per v63 lesson) — when v<N> evidence retroactively corrects v<N-1>'s register, log + flag at next audit as gap-closure item

---

## Corpus-first observations tracker (v2.2 expanded — v60+ entries added)

**v2.1 baseline (v1-v31) retained.**

**v32-v55 additions (per `_state/02-pattern-library-state-history.md`):** various.

**v56-v65 corpus-firsts (v2.2 NEW):**
- First NEUTRAL Storm Bear Phase 0.9 SKIP: AutoGPT v59 (1st disciplined-skip in 41-streak history)
- First T4 api-protocol-translation-proxy: free-claude-code v60
- First T4 2-axis sub-taxonomy: free-claude-code v60 (content-transformation N=8 vs protocol-translation N=1)
- First positive-comparison-parallel Pattern #57 sub-variant: free-claude-code v60 ("...like OpenClaw")
- First cross-pattern coupled-design at N=4 (Library-vocabulary item #9): free-claude-code v60
- First Kiro IDE external-IDE-methodology lineage: cc-sdd v61
- First solo-Japanese T1 author: cc-sdd v61 (Pattern #55 Japan extension)
- First EARS-format explicit reference: cc-sdd v61
- First File Structure Plan primitive: cc-sdd v61
- First adversarial subagent review architecture at framework level: cc-sdd v61 (Pattern #76)
- First anti-vibe-with-pragmatic-acknowledgment positioning: cc-sdd v61
- First install-time-skill-format-translator (Pattern #18 Layer 2 v61): cc-sdd v61
- First cross-vendor cooperation observation (corporate-corporate): codex-plugin-cc v62 (OpenAI publishes plugin FOR Anthropic Claude Code)
- First 1-wiki counter-evidence cycle in corpus history (Pattern #76): v62→v63 (2026-05-07/08)
- First cross-vendor-bridge sub-archetype (Pattern #18 Layer 2 v62): codex-plugin-cc v62
- First corpus-record stars/day velocity (~1,186 stars/day): andrej-karpathy-skills v63
- First source-celebrity-derivative-distillation: andrej-karpathy-skills v63 (Pattern #19 a4 sub-type)
- First retroactive Pattern Library correction at audit: v63 catches v62 codex-plugin-cc Pattern #52 qualification gap
- First Pattern #21 SDD un-stale promotion via N=4 cross-archetype: v63 EARLY mini-audit
- First Pattern #19 ecosystem-portfolio-builder N=2 → N=3 → N=4 strengthening: v61 → v63 → v64 → v65
- First T1 domain-vertical-skill-collection: claude-seo v64 (Pattern #77 NEW)
- First Living-Domain-Standards Tracking N=1 + N=2: claude-seo v64 (78a) → claude-code-system-prompts v65 (78b) — TIED FASTEST 1-wiki un-stale cycle
- First 5-version-source atomic-bump CI discipline: claude-seo v64 (13 manifest-consistency assertions)
- First solo-author cross-vendor parallel-port: claude-seo + codex-seo v64 (Pattern #18 Layer 2 sub-archetype)
- First T1 reverse-engineering-reference-archive: claude-code-system-prompts v65 (Pattern #79 NEW)
- First STRONGEST 3-of-4 Storm Bear Phase 0.9 PASS with corpus-foundation-PRODUCT inheritance: claude-code-system-prompts v65 (criterion (d) STRONGEST IN CORPUS HISTORY)
- First Pattern #57 57c-product sub-variant (corpus-foundation-PRODUCT inheritance): claude-code-system-prompts v65
- First cross-pattern coupled-design at N=5+ (Library-vocabulary item #9 corpus-record): claude-code-system-prompts v65
- First TIED-FASTEST 1-wiki un-stale-via-N=2-evidence cycle (Pattern #78): v64→v65 (2026-05-13/14)
- First completed pilot lifecycle in corpus history: BMAD + codex adversarial-review v3.2 hireui (2026-05-11 → 2026-05-13)

---

## Cross-references

- Parent skill: `llm-wiki-ingest.md`
- Pattern register: `PATTERN_LIBRARY.md` (vault root) + chapters `_patterns/03-active-candidates.md` + `_patterns/04-confirmed-patterns.md` + `_patterns/05-recent-additions.md`
- v2.1 routine (superseded): `llm-wiki-routine-v2.1.md`
- v2 routine (historical): `llm-wiki-routine-v2.md`
- v1 routine (historical): `llm-wiki-routine.md`
- Sibling skills: `new-project.md`, `brain-setup.md`, `brain-setup-v2.md`, `weekly-update.md`, `(C) project-code-analysis-harness.md`
- Audit documents: `04 Reviews/` (multiple post-vNN audit documents)
- **NEW v2.2 reference:** v65 `claude-code-system-prompts` wiki — consult `02 Wiki/` cluster + entity files when designing vault routine changes (per Reference Claude Code system prompts discipline)
- Evidence: 65 iteration logs across v1-v65 projects + 1 completed pilot lifecycle document (BMAD + codex adversarial-review v3.2 hireui)

---

## Version log

- **v1** (2026-04-18): First codification from 2 wikis (ECC + Superpowers).
- **v2** (2026-04-19): Consolidated from 102+ action items across v3-v18 (16 additional wikis).
- **v2.1** (2026-04-22): Consolidated from ~205 cumulative action items across v19-v31 (13 additional wikis + v29 full audit + v30 direct updates + v31 mini-audit).
  - Pattern Library maturity: 5 structural-promotion criteria / OBSERVATION-TRACK / absorption-retirement / un-stale / counter-evidence-refinement
  - Discipline: audit cadence reform / mini-audit protocol / overlap pre-check / consolidation-forward / N=1 stale-risk-flagging / Storm Bear per-wiki evaluation / supply-chain awareness / fact-verification / operator-facing backlog / stream-timeout resume
  - Phase 4b routing: 16 → ~25 modes
- **v2.1 amendment session 66 (2026-04-26 post-v55):** Phase 0.9 STRICT 1-of-4 hard requirement; cautionary-contrast REJECTED as criterion; disciplined-skip is default when 0/4. 38-consecutive streak GRANDFATHERED.
- **v2.2** (2026-05-14): Consolidated from ~31 codification candidates accumulated across v60-v65 (6 wikis + v63 EARLY mini-audit + 1 completed pilot lifecycle).
  - **Phase 0 expansions (4):** docs/ tree-listing / velocity-screen automation / engagement-signal sub-investigation / Living-Domain-Standards as 13th axis
  - **Phase 0.9 expansions (1):** SKIP entity slot reallocation discipline + meta-entity strength categorization (WEAK/MODERATE/STRONG/STRONGEST)
  - **Phase 1-3 expansions (2):** Phase 4b PRIMARY pre-registration at Phase 0 / source-celebrity-derivative-distillation criteria
  - **Phase 4b expansions (2):** NEW Pattern proposal-document discipline (200-400 lines at `01 Analysis/`) / Reference Claude Code system prompts when designing routines
  - **Phase 5-6 expansions (3):** Pre-Phase-6 fact-verification expanded (evidence-lists + streak-counters + cross-ref integrity) / retroactive-correction-check / 1-wiki rapid-evolution detection
  - **Pattern Library discipline expansions (5):** Cross-archetype N-counting as 6th promotion dimension / Lineage-test → independence-test → promotion 3-step arc / Strengthen-over-discover streak metric / Anti-vibe Pattern #51 sub-pole / EXTREME-VIRAL Pattern #52 sub-archetype 3-axis
  - **Audit class expansion (1):** EARLY-OPERATOR-ELECTED 4th mini-audit class
  - **Library-vocabulary expansion (2):** Item #9 cross-pattern coupled-design (v60 baseline N=4 → v65 strengthening N=5+) / Item #10 1-wiki rapid-pattern-evolution observational track
  - **Anti-patterns expanded (5 NEW):** Skip velocity-screen / Defer NEW Pattern proposal-document / Skip Phase 0.9 SKIP reallocation / Re-derive Claude Code envelope from memory / Skip retroactive-correction-check
  - **Acceleration audit pattern:** Operator-elected mini-audit at +1 wiki vs +2-3 natural cadence (v65→v66 acceleration example)
  - **Honest disclosure:** ~11 of the claimed 31 codification candidates trace to pre-v60 state-history-chapter files not consolidated in this codification; remaining ~20 candidates from v60-v65 fully integrated. v2.3 will revisit pre-v60 backlog at next codification cycle (~v75-v80 natural cadence).
  - Velocity: unchanged ~2h plateau proven at v6-v65 (60 wikis) + HIGH source-density extension (~2-2.5h acceptable at v64+v65).

---

**v2.2 codified 2026-05-14. ~20 v60-v65 codification candidates integrated + 5 NEW anti-patterns + 1 NEW mini-audit class + 1 NEW promotion-counting dimension + 2 NEW Library-vocabulary items + 4 NEW Phase 0 sub-steps + 13th classification axis (Living-Domain-Standards). Consolidates v60-v65 learnings + 1 completed pilot lifecycle. Phase 0.9 STRICT 1-of-4 retained with strength categorization. Velocity plateau preserved across 60 consecutive wikis. Honest disclosure: ~11 pre-v60 candidates deferred to v2.3.**
