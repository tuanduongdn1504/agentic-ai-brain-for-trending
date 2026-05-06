# Skill: LLM Wiki Routine v2.1

📍 **Status:** IN-FLUX (continues evolving — current version as of 2026-05-06)

> **Type:** Orchestration meta-skill (Routine pattern)
> **Version:** v2.1 — consolidated from ~205 cumulative action items across v3-v31 (29 wikis + 2 full audits + 1 mini-audit of learning)
> **Codified:** 2026-04-22 (post-v31 mini-audit consolidation session)
> **Supersedes:** `llm-wiki-routine-v2.md` (v2) — v2 retained for historical reference
> **Parent skill:** `llm-wiki-ingest.md` (methodology)
> **Sibling refs:** `PATTERN_LIBRARY.md` (vault root — authoritative pattern register)

---

## What's new in v2.1 (vs v2)

v2 was codified after 18 wikis (102+ action items). v2.1 incorporates learnings from 13 additional wikis (v19-v31) + v29 full audit + v30 direct updates + v31 mini-audit.

### Major additions (summary)

1. **5 structural-promotion criteria** for Pattern Library (up from 2 in v2): default ≥3-cross-tier / structural-N=2 / spectrum-pattern-N=2 / variant-within-pattern-N=2 / **meta-pattern-at-N=3-consolidation**
2. **OBSERVATION-TRACK sub-category** — event-based observations retained for monitoring but not architectural promotion
3. **Absorption-retirement mechanism** — retire candidate via absorption into superseding pattern (vs staleness-retirement only)
4. **UN-STALE mechanism** — stale candidates unstale when 2nd observation appears
5. **Audit cadence reform** — mini-audit at 0.95:1 / full audit at 1.05:1 (replaces v2's >1:1 trigger)
6. **Pre-registration overlap pre-check** — reject new candidate if >70% overlap with existing
7. **Consolidation-forward registration discipline** — register meta-pattern not standalone when ≥2 prior observations would be subsumed
8. **N=1 stale-risk-flagging at registration** — novel single-observation candidates flag themselves
9. **Event-based vs architectural pattern distinction** — reclassify as OBSERVATION-TRACK when episodic
10. **Counter-evidence-driven refinement** — counter-example narrows pattern scope (not invalidation)
11. **Storm Bear meta-entity per-wiki evaluation** — not blanket obligation; assess applicability (**TIGHTENED at session 66 post-v55**: STRICT 1-of-4 hard requirement; cautionary-contrast REJECTED as criterion; disciplined-skip is default when 0/4 — see Phase 0.9)
12. **Supply-chain awareness protocol** — flag transitive trust-boundary risks
13. **Fact-verification protocol** — re-check numbered-pattern references before Phase 6
14. **Ratio notation clarification** — ratio = active/confirmed; lower is healthier (fewer pending candidates)
15. **Stream-timeout resume protocol** — delegated builds can resume from partial completion
16. **Phase 4b routing expanded to ~25 modes** (up from 16 in v2)
17. **Mini-audit protocol** formalized as reusable routine
18. **Operator-facing backlog discipline** — track deferred vault actions; escalate at N-session threshold

---

## Invocation (unchanged from v2)

User says: `"LLM wiki for <URL>"`, `"routine for <topic>"`, `"build wiki on <repo>"`.

→ Invoke immediately. No interview. No check-ins between phases.

**Do NOT invoke when:**
- Topic fails Phase 0 threshold
- User explicitly requests interview mode
- Consolidation state blocks new wikis (see §Consolidation guard below)

---

## Consolidation guard (v2.1 refined)

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

**Operator-facing backlog tracking (v2.1 NEW):**

Routine tracks deferred vault actions (e.g., v27 diagnostic HIGH bundle). At 5+ sessions of deferral:
- Escalate in recommendation with "BLOCKING-RECOMMENDATION" tag
- Do not hard-block, but be blunt in final report

**Reasoning:** v28-v31 proved that candidate accumulation (3-5/wiki) outpaces audit consolidation (4 items/audit) without intervention. Audit cadence reform + backlog tracking maintains library integrity + operator execution discipline.

**Override:** User can explicitly request wiki build despite state. Honor it, but note the trade-off in Phase 5 iteration log and escalate backlog in final recommendation.

---

## 7-phase workflow (v2.1 refined)

### Phase 0: Pre-flight + enhanced probe (15 min)

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

**0.4 Enhanced classification probe** — 12-axis (v2 retained):

| Axis | Values |
|------|--------|
| **Tier** | T1 assistant / T2 service / T3 education / T4 bridge / T5 application / outside-scope |
| **Archetype** | solo-community / solo-VN-authored / solo-Korean (v27+) / founder-personal / community / LLC / official-corporate / solo-enterprise-scale / academic-lab (v22+) / ecosystem-layer-individual-with-commercial-platform (v31+) |
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

**0.5 Cross-wiki pattern pre-check** (v2.1 EXPANDED):

```
Check PATTERN_LIBRARY.md:
  - Does new framework fit existing confirmed patterns? (strengthening evidence)
  - Does observation advance any candidate toward confirmation? (flag for audit)
  - Is there notable ABSENCE of prior-wiki patterns? (counter-evidence signal)
  - Do any cross-wiki standards (OpenClaw/Hermes/MCP/AGENTS.md) apply?
  - Are any patterns currently STALE that this wiki might UN-STALE? (v2.1 NEW)
  - Could this observation serve as COUNTER-EVIDENCE refining an existing pattern? (v2.1 NEW)
  - Would any new candidate OVERLAP >70% with existing candidate? (v2.1 NEW pre-check)
```

**0.6 Candidate overlap pre-check** (v2.1 NEW):

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

**0.8 Tier placement decision** (v2 retained — explicit):

Classify framework into tier with justification. If ambiguous (could be T1 or T4), document both possibilities and pick primary. Record in CLAUDE.md Positioning section.

**0.9 Storm Bear meta-entity applicability check** (v2.1 NEW; **TIGHTENED at session 66 post-v55 per Option A discipline-restoration**):

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
          ingestion utility for client docs / browser-agent for ticket scraping
    FAIL: domain-mismatched (content-marketing / faceless-content / business-OS / ML-training-infra) /
          requires-infrastructure-vault-doesn't-have / blocked-by-license-for-commercial-Scrum-use

(c) Subject is methodology-influence-node for vault routine v2.1 maintenance
    PASS: Karpathy / John Lam / Lance Martin / Boris Cherny / SDD / TDD / agentic-engineering /
          methodology-cited-by-other-corpus-frameworks
    FAIL: no-methodology-lineage / personal-authority-claims-only ("OG AI Wizard") /
          domain-irrelevant methodology

(d) Subject is in-corpus reference (cited by another corpus subject OR cites another corpus subject)
    PASS: explicit citation found via Pattern #57 sub-variant detection (57a/b/c/d) /
          sibling-product to existing corpus subject /
          successor-of or successor-by relationship to corpus subject
    FAIL: no cross-corpus reference detected; subject standalone in corpus context

DECISION RULE:
  Sum of PASS criteria ≥ 1 → INCLUDE Storm Bear meta-entity (4th entity slot)
  Sum of PASS criteria = 0 → SKIP meta-entity; substitute alternative 4th entity per Phase 3
```

**EXPLICIT REJECTION — non-criteria do NOT justify INCLUDE:**

❌ **"Cautionary-contrast" / "negation-as-lesson" / "what-not-to-do"** framings (e.g., "abandoned-author-no-LICENSE is cautionary template for vault publishing" / "OG AI Wizard personal-authority is contrast for vault honest-self-presentation"). These are post-hoc rationalizations to preserve streak metric. If genuinely useful as cautionary lesson, document in `04 Reviews/` as separate review note — do NOT conflate with structural Storm Bear meta-entity.

❌ **"Storm Bear could theoretically learn X"** open-ended speculation. Phase 0.9 requires concrete evidence (specific author archetype + specific operational use + named methodology lineage + verifiable in-corpus reference).

❌ **"Preserve consecutive-meta-entity streak"** as inclusion justification. Streak length is downstream metric, NOT inclusion target. Goodhart's law: optimizing for streak length corrupts Phase 0.9 signal-value.

**Disciplined-skip is feature, not bug.** When 0/4 criteria pass:
1. Document the skip in CLAUDE.md (NOT a routine violation; correct application of Phase 0.9)
2. Substitute 4th entity slot with alternative (specific pattern-test entity / secondary architecture entity / domain-specific deep-dive)
3. Note skip explicitly in iteration log as "Phase 0.9 disciplined-skip; 0/4 criteria passed"
4. Streak counter: SKIP breaks consecutive-meta-entity streak; reset to 0; honest signal restored

**Tightening history:**
- v10-v28: blanket-obligation (auto-include for every wiki)
- v29-v54: discretionary per-wiki check ("if wiki reveals vault-architectural lesson" — too loose)
- v55: lightweight-INCLUDE via cautionary-contrast despite 4/4 FAIL — Phase 0.9 violation acknowledged at session 66
- **v56+: STRICT 1-of-4 hard requirement; cautionary-contrast REJECTED as criterion** (this section)

**Streak counter handling at session 66 tightening event:**
- 38-consecutive Storm Bear meta-entity streak (v10-v55) GRANDFATHERED — preserved as historical record per Option A2 grandfather-then-tighten-prospectively
- Streak metric semantic shift: pre-v55 era used loose criteria; post-v55 era uses strict criteria
- Going forward: only strict-criteria-passing wikis count toward future streak metrics
- v56 onwards: if 0/4 → SKIP cleanly + restart streak from next strict-criteria-passing wiki

**Outcome of Phase 0:**
- Probe complete with 12-axis classification
- Pattern Library pre-checked (presence + absence + strengthening + un-stale + overlap)
- Tier placement decided
- Phase 4b routing mode identified
- Storm Bear meta-entity applicability decided
- Consolidation state verified

### Phase 1: Scaffold (10 min) — unchanged

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

**1.2 CLAUDE.md template** — populate with Phase 0 outputs + pattern-test preview + cross-reference list.

**1.3 COMMANDS.md** — point to `llm-wiki-routine-v2.1` (this file) + cross-project references.

**1.4 Foundational wiki files:**
- `02 Wiki/(C) index.md` — phase tracking + sources/entities/published planning + cross-wiki siblings
- `02 Wiki/(C) log.md` — append-only timeline
- `01 Analysis/(C) open questions.md` — 20-30 questions

### Phase 2: Source ingestion (30-45 min) — refined v2.1

**Target: 3 cluster summaries** (proven sweet spot v6-v31).

**Cluster strategy** (v2 retained):
- **Cluster 1:** User-facing docs (README + translations + landing docs)
- **Cluster 2:** Contributor-facing docs (CLAUDE + AGENTS + CONTRIBUTING + SECURITY + etc.)
- **Cluster 3:** Technical/distribution (architecture + packaging + integrations)

**Per cluster (v2.1 additions):**
- Extract verbatim positioning / philosophy / key claims
- Document 8-12 corpus-first observations
- Check against Pattern Library — does cluster advance any candidate?
- Note ABSENCES (e.g., no Karpathy mention, no OpenClaw) as much as presences
- External URL resolution: if cluster references catalogs/guides hosted externally, fetch them
- **NEW v2.1: Flag supply-chain risk** if cluster documents untrusted-code ingestion (MCP servers, plugins, third-party agents) — link to Pattern #66 OBSERVATION-TRACK
- **NEW v2.1: Flag counter-evidence** to existing patterns (not just confirming observations)

**Output per cluster:**
- `02 Wiki/(C) <cluster-name> cluster summary.md` (~15-section format)
- Update `(C) log.md` after each cluster
- Update `(C) index.md` Sources table

### Phase 3: Entity pages (40 min) — refined v2.1

**Target: 4 entity pages** (v2 retained).

**Entity selection logic (v2.1 refined):**

1. **Core product entity** — what does this framework DO
2. **Distribution/ecosystem entity** — how is it delivered + integrated
3. **Novel pattern entity** — what's corpus-first OR pattern-relevant observation (include counter-evidence patterns too)
4. **Tier meta + Storm Bear entity** (if applicable per Phase 0.9; otherwise substitute with alternative 4th entity)

**Format: 13-section canonical** (from `llm-wiki-ingest.md`) — unchanged.

**Cross-references MANDATORY:**
- Every entity references ≥3 sibling wikis
- Pattern Library entries referenced where applicable
- Novel observations tagged as Pattern candidates in PATTERN_LIBRARY.md update
- **NEW v2.1: Counter-evidence observations tagged explicitly** (v29 introduced #47, #48 refinement via counter-evidence)

**Storm Bear meta-entity (v2.1 refined — conditional; STRICT criteria post-v55 tightening session 66):**
- Apply STRICT 1-of-4 inclusion check from Phase 0.9 (cautionary-contrast REJECTED as criterion)
- When included (≥1/4 PASS): 4th entity = tier meta + Storm Bear strategic section with pilot ranking update + pattern audit notes + consolidation recommendations
- When skipped (0/4 PASS): 4th entity = alternative (e.g., specific pattern-test entity / secondary architecture entity / domain-specific deep-dive); document skip explicitly in CLAUDE.md + iteration log per Phase 0.9 protocol

### Phase 4a: Beginner bilingual guide (15 min) — refined v2.1

**Output:** `03 Published/(C) <repo> - Huong dan cho nguoi moi.md`

**Structure (12-13 parts):**
1. What is it? (bilingual)
2. Corpus-first signals
3. Tier placement
4. Installation
5. Core usage pattern
6. Novel concepts / key architectural choices
7. vs other corpus frameworks
8. **Ethical framing (v2 retained + v2.1 expanded)** — include if autonomy-max tagline OR controversial positioning OR **supply-chain risk surface** (v2.1 NEW; e.g., aggregator-directories or untrusted-plugin frameworks)
9. Storm Bear relevance (VN operator + Scrum coach fit)
10. 4-week learning roadmap
11. Tradeoffs + limitations
12. **Caveats + safety notes** (v2.1 NEW emphasis on supply-chain awareness when applicable)
13. References + next action

**Length:** 400-700 lines. Bilingual (VN primary, EN technical).

### Phase 4b: Routing-dependent deliverable (20-30 min) — expanded v2.1

**~25 routing modes observed (v1-v31):**

| Mode | Trigger | Example |
|------|---------|---------|
| Single-peer 2-way | Same-tier N=2 → N=3 test | v14 T5 paperclip (3-way) |
| N-way extension | Same-tier + new entrant | v11 T1 5-way → v18 8-way → v27 9-way |
| Taxonomy adjacent | New tier introduced | v6 T3 / v7 T4 / v9 T5 |
| Tier extension + refinement | N=3+ at established tier | v16 T4 3-way Resolution D |
| Meta-reference | Outside-scope wiki | v8 build-your-own-x |
| Meta-peak | Karpathy/lineage touchpoint | v10 autoresearch |
| Methodology convergence | Same methodology across frameworks | v17 SDD GSD+spec-kit |
| Lineage diversification | New intellectual ancestor | v17 John Lam, v18 no-lineage, v20 research-paper-chain |
| Scale-anomaly | Solo at enterprise-scale | v18 agency-agents, v29 crawl4ai |
| Pattern-test | First test of prior hypothesis | v14 Pattern #9 T5 test |
| Platform-tier homogeneity | T2 validation | v15 multica |
| Pattern major revision | Evidence requires formulation change | v18 Pattern #20 |
| Corporate entrant | First corporate-official at tier | v17 spec-kit |
| Cross-wiki standard validation | OpenClaw/Hermes/MCP confirmation | v18 OpenClaw 5th |
| Storm Bear direct-action | Vault applicability observed | v16 graphify |
| Consolidation trigger | Audit state exceeded | v29 audit session |
| **Tier-completion milestone** (v2.1 NEW) | All tiers multi-entrant | v26 T3 N=2 → 5/5 milestone |
| **Pattern refinement via counter-evidence** (v2.1 NEW) | Counter-example narrows scope | v29 #47, #48 via crawl4ai |
| **Un-stale mechanism** (v2.1 NEW) | Stale candidate gets 2nd data point | v30 #42, #44 via OpenHands |
| **Meta-pattern consolidation** (v2.1 NEW) | 3+ candidates collapse to meta-pattern | v31 mini-audit #68 wraps #49 + ... |
| **Tier within-variant extension** (v2.1 NEW) | Existing tier adds new archetype variant | v27 T1 Korean, v29 T4 solo-enterprise-scale |
| **Ratio ceiling observation** (v2.1 NEW) | Pattern Library ratio exceeds consolidation rate | v28, v29 pre-audit |
| **Regional bifurcation** (v2.1 NEW) | Corpus observable in distinct regional ecosystems | v19 TrendRadar CN vs Western |
| **Cross-corpus citation** (v2.1 NEW) | Wiki subject cites prior Storm Bear wiki | v27 OMC cites v1 + v2 |
| **Protocol-directory meta-reference** (v2.1 NEW) | Wiki is directory of ecosystem standard | v31 awesome-mcp-servers |

**Routing decision:**
- Review modes — which applies primarily?
- Pick 1 primary mode, up to 2 secondary
- Output template driven by mode

**Output:** `03 Published/(C) <mode-specific-name>.md`

**Length:** 500-750 lines. Primary deliverable type.

### Phase 5: Iteration log + Pattern Library update (10 min) — expanded v2.1

**Output:** `04 Reviews/(C) YYYY-MM-DD v<N> build learnings.md`

**Structure (v2.1 standardized):**

1. **Milestones hit** (corpus-level + framework-specific)
2. **Phase breakdown** (duration per phase)
3. **What worked**
4. **What didn't work / friction** (minor + recurring)
5. **Routine v2.1 action items** (NEW items for next version)
6. **Total action items accumulating** (running counter)
7. **Meta-observations**
8. **Unique findings** (corpus-firsts)
9. **Storm Bear vault impact** (if Storm Bear meta-entity included)
10. **Next wiki candidates** (strategic selection for pattern-strengthening)
11. **Strategic decision point** (consolidation recommendation if applicable + backlog escalation)
12. **Scorecard** (novelty / pilot-relevance / pattern-contribution / velocity / quality)
13. **Primitive-count check** (v2.1 informal discipline — see Primitive-count flagging section below)

**Primitive-count flagging (v2.1 informal discipline — added 2026-04-23)**

**Purpose:** Flag when a wiki's source repo has more distinct primitives than 4-entity format can cleanly accommodate. Recommendation-only — does NOT trigger variable entity count (that proposal deferred to routine v2.2 at natural cadence ~v45-v50).

**Probe (run at Phase 0, report at Phase 5):**

Count distinct primitive-types from 4 signals:
1. README TOC top-level sections
2. Repo folder structure top-level (`/commands/` `/hooks/` `/mcps/` etc.)
3. AGENTS.md / CLAUDE.md declared components
4. Documentation site top-level pages

**Primitive-count threshold:**
- ≤4 primitives: no action (standard 4-entity fit)
- 5-6 primitives: Phase 5 iteration log flags "primitive-count > 4; consider 1 follow-up deep-dive wiki"
- 7+ primitives: Phase 5 iteration log flags "primitive-count ≥ 7; consider N-4 follow-up deep-dive wikis" (where N = primitive count)

**Iteration log section 13 template:**

```
### Primitive-count check (v2.1 informal discipline)

- **Probed primitive-count:** N
- **Fits 4-entity format cleanly?** Yes / Partial / No
- **Follow-up deep-dive wikis recommended:** [list primitives that got compressed]
- **Operator decision:** [defer / ship sequentially / accept compression]
```

**Reasoning for informal discipline:**

ECC v1 had 7 Claude Code primitives compressed into 7 separate wiki pages (outlier). All 33 subsequent wikis ship with standard 4-entity format, some compressing primitives. Rather than rebuild routine to handle variable counts (routine v2.2 proposal), informal flag lets operator decide per-wiki whether follow-up deep-dive wikis justified. Preserves structural comparability + 2h velocity + Pattern Library coordinates while surfacing compression honestly.

**Historical candidates for follow-up deep-dive wikis (retroactive):**
- ECC v1: could spawn `ECC - Commands Deep Dive` / `ECC - Hooks Deep Dive` / `ECC - MCPs Deep Dive` / etc.
- Any complex framework where primitive-count probe would have returned ≥5

**Not retrofitted** — 33 existing wikis stay valid. Informal discipline applies forward from v35+.

**Pattern Library update (v2.1 expanded discipline):**

Phase 5 directly updates `PATTERN_LIBRARY.md`:

**Registration checks before adding candidate:**
- Overlap pre-check (Phase 0.6): >70% overlap → reject or consolidate
- Consolidation-forward discipline: if 2+ prior observations would be subsumed by proposed meta-pattern, register as meta-pattern (not 3rd standalone)
- N=1 stale-risk flagging: novel single-observation candidates flag at registration with "stale-risk-flagged" note

**Registration actions:**
- New candidate entry in Active Candidates section
- Update N=1 stale-tracking table with v+5 stale-check and v+10 retire-check
- Update count in Active Candidates section header
- Strengthen existing pattern evidence where applicable
- **NEW v2.1: Un-stale check** — does any STALE-CANDIDATE now have 2nd data point from this wiki? If yes, un-stale with audit recommendation

**Classification options (v2.1 expanded):**

| Status | When to assign |
|--------|---------------|
| 🟡 CANDIDATE | Default for 1-2 observations OR single-tier-confined |
| 🔍 OBSERVATION-TRACK (v29 NEW) | Event-based or episodic observation; not architectural pattern |
| Stale-risk-flagged at registration (v2.1 NEW) | N=1 candidate with one-off characteristics (not yet stale, but likely) |

### Phase 6: Vault sync (10 min) — refined v2.1

**Required updates:**

1. **Project `(C) index.md`** → all phases ✅
2. **Project `(C) log.md`** → append Phase 2-6 completion entry
3. **Root `CLAUDE.md`** → add project entry with milestones + deliverables + pattern tests + pilot ranking update
4. **Root `GOALS.md`** → append version log entry with corpus milestones + Pattern Library changes + next options
5. **Root `PATTERN_LIBRARY.md`** → direct update with new candidates + refinements + un-stale flags + promotion proposals

**Fact-verification protocol (v2.1 NEW):**

Before Phase 6 completion, re-check all numbered-pattern references in wiki files:
```
For each "#NN" pattern reference in wiki files:
  Verify against PATTERN_LIBRARY.md:
    - Does #NN exist?
    - Is the referenced name correct?
    - Is the referenced status accurate?
IF mismatch:
  Document in mini-audit or correct inline
  Historical wiki files may remain unchanged if correction documented
```

Lesson from v31: Pattern Implications file mislabeled #35 as "Education-Aggregator" (actual #35 = Foundation-Model-as-Product). Caught at v31 mini-audit post-hoc. Pre-Phase-6 check prevents.

**Consistency check (v2.1 NEW):**
- Counts across all vault files (PATTERN_LIBRARY / GOALS / CLAUDE / project-CLAUDE) must match
- Dates consistent
- Ratio computed correctly (active/confirmed; numerator:denominator label consistent)

---

## Mini-audit protocol (NEW in v2.1)

**Trigger conditions:**
- Ratio 0.95:1 - 1.05:1 (proactive, pre-trigger)
- Accumulated promotion-ready candidates (N=2 structurally-unambiguous across 2+ candidates)
- Operator request

**Scope (focused — not full audit):**
- Promotion review for specific candidates (not blanket review)
- Stale-flag retroactive application if threshold crossed
- Formulation extensions (not new patterns)
- Absorption-retirement when superseding pattern promotes
- 30-60 minute duration target

**Deliverables:**
- `04 Reviews/(C) YYYY-MM-DD Pattern Library mini-audit post-v<N>.md` (~300-600 lines)
- PATTERN_LIBRARY.md updates (promotions + retirements + extensions)
- GOALS.md session entry
- CLAUDE.md state block

**Distinction from full audit:**
- Full audit: comprehensive scope, ~1-2h, reviews all candidates, introduces new criteria
- Mini-audit: targeted scope, ~30-60min, specific promotions + adjustments, no new criteria unless emergent from targeted review

**Validated at v31 mini-audit** — 4 promotions + 1 absorption-retirement + 1 stale-flag + 1 formulation extension + 1 new criterion (meta-pattern-at-N=3-consolidation) executed in single session. Ratio 1.07:1 → 0.75:1 (biggest single-audit drop in corpus).

---

## Audit cadence reform (v2.1 — replaces v2 >1:1 trigger)

| Ratio zone | Trigger | Action |
|-----------|---------|--------|
| < 0.75:1 | Healthy | No action required |
| 0.75-0.95:1 | Healthy | Monitor; strengthen-over-discover discipline |
| 0.95:1 | Mini-audit zone | Lightweight rebalance (~30-60min); targeted promotions |
| 1.05:1 | Full audit trigger | Comprehensive review (~1-2h); systematic promotion + retirement |
| > 2.0:1 | Hard block | No new wikis until cleared |
| Action-backlog > 100 | Hard block | Routine refactor required |

**Historical data:**
- v25 audit: 1.00:1 → 0.74:1 (full audit, pre-reform trigger)
- v27 audit: 1.00:1 → 0.93:1 (full audit, retire-only)
- v29 audit: 1.19:1 → 1.00:1 (full audit, first proactive promotions)
- v31 mini-audit: 1.07:1 → 0.75:1 (first mini-audit; validates cadence reform)

---

## 5 structural-promotion criteria (v2.1 consolidated)

Pattern Library CONFIRMED status can be achieved via 5 paths:

| # | Criterion | Introduced | First use |
|---|-----------|-----------|-----------|
| 1 | Default: ≥3 observations across 2+ tiers | v1 baseline | Multiple |
| 2 | Structural-unambiguity-at-N=2 | v1 baseline | Multiple |
| 3 | Spectrum-pattern-at-N=2 | v29 audit | Pattern #51 Vibe-Coding |
| 4 | Variant-within-pattern-at-N=2 | v29 audit | Pattern #17 variant 5 |
| 5 | Meta-pattern-at-N=3-consolidation | v31 mini-audit | Pattern #68 Awesome-List-Genre |

**Criterion descriptions:**

**Default (1):** Pattern observed in ≥3 wikis spanning ≥2 different taxonomy tiers. Confidence derives from breadth + frequency.

**Structural-unambiguity-at-N=2 (2):** Pattern observed in 2 wikis where each observation is structurally criterial (not ambiguous). Confidence derives from clarity of structural definition.

**Spectrum-pattern-at-N=2 (3):** Spectrum-type pattern with observable poles can promote at N=2 via 2-distinct-pole observations. Each pole = structural demonstration of the spectrum axis (analogous to 2 opposing points defining a line).

**Variant-within-pattern-at-N=2 (4):** Sub-variant within an already-confirmed pattern can promote at structurally-unambiguous N=2. Separate promotion track from the parent pattern. Example: Pattern #17 variant 5 ecosystem-scale commercial platform promoted at HuggingFace + Microsoft.

**Meta-pattern-at-N=3-consolidation (5):** Meta-pattern wrapping 2+ prior observations across structurally-distinct sub-types can promote at N=3 if: (a) the sub-type axis is criterially clean, (b) each sub-type has ≥1 observation, (c) promotion saves fragmentation by consolidating multiple candidates into unified explanatory structure. Absorbs sub-candidates as sub-type classifications (absorption-retirement).

---

## Absorption-retirement mechanism (v2.1 formalized)

**Distinct from stale-retirement** (first applied v27 audit to 4 aged N=1 candidates).

**Trigger:** Candidate is subsumed by a superseding pattern (parent pattern promotes, variant-pattern promotes, or meta-pattern promotes).

**Mechanism:**
1. Move candidate formal-statement substance into superseding pattern as sub-observation
2. Mark original candidate "RETIRED (absorbed)" in Retired section
3. Keep historical record with "Revive if..." clause documenting what new evidence would re-justify standalone

**Cases observed:**
- v29 audit: #60 AutoGen-Extension → absorbed into Pattern #17 variant 5 promotion
- v31 mini-audit: #49 Design-Template-Aggregator → absorbed into #68 Awesome-List-Genre meta-pattern

**Benefit:** Prevents fragmentation when structural consolidation emerges naturally.

---

## Un-stale mechanism (v2.1 formalized)

**Purpose:** Re-activate stale candidates when 2nd observation appears.

**Flow:**
1. Stale-candidate (N=1 since 5+ wikis ago) gets 2nd observation in new wiki
2. Mark "✅ UN-STALED v<N>" in stale-tracking table
3. Move from STALE to active candidate with strengthened evidence
4. Typically flagged as promotion-candidate for next audit

**Cases observed:**
- v30 OpenHands un-staled #42 Academic-Published + #44 Academic-Lab Affiliation (both N=1 since v22 → N=2 at v30)
- Both promoted at v31 mini-audit under structural-unambiguity-at-N=2

**Significance:** First ratio-improvement mechanism via existing-candidate re-activation (not just retirement or promotion of new observations). v30 direct updates leveraged this to demonstrate corpus discipline.

---

## Counter-evidence-driven refinement (v2.1 formalized)

**Purpose:** Pattern formulation adjustment when counter-example demonstrates over-broad scope.

**Trigger:** New wiki provides structural counter-example to confirmed pattern formulation.

**Flow:**
1. Evaluate counter-evidence: does it invalidate pattern or narrow scope?
2. If invalidate: retire pattern
3. If narrow-scope: apply REFINED formulation preserving core observation at narrower scope

**Cases observed:**
- v29 audit: #47 Vision-Based Browser Automation narrowed from "vision-DOM-free" to "vision-based as architectural alternative" (crawl4ai DOM-based counter-evidence)
- v29 audit: #48 Proprietary Anti-Bot Commercial Moat narrowed from "anti-bot moat" to "proprietary-commercial-gated anti-bot specifically" (crawl4ai OSS anti-bot counter-evidence)

**Discipline:** Counter-evidence strengthens pattern by tightening scope, not just adding data points. Framing: "pattern is specifically about X, not the broader Y."

---

## OBSERVATION-TRACK sub-category (v29 audit — v2.1 codified)

**Purpose:** Retain episodic / event-based observations without forcing architectural-pattern framing.

**Criteria for reclassification:**
- Observation is event-based (specific incident response) not repeatable architectural choice
- Response pattern is reactive to external events, not structural framework-design decision
- Episodic nature doesn't fit N-observation promotion criteria

**Tracking:**
- OBSERVATION-TRACK candidates have own sub-section in PATTERN_LIBRARY.md
- Retained for monitoring but not tracked for architectural promotion
- May reclassify back to architectural candidate if structural pattern emerges from 2+ incidents

**Cases observed:**
- #66 Supply-Chain Security Incident Response — reclassified at v29 audit (crawl4ai supply-chain incident is event-based)
- #67 Academic-Commercial Fusion Archetype — registered directly as OBSERVATION-TRACK at v30 (discipline application)

---

## Stream-timeout resume protocol (v2.1 NEW)

**Scenario:** Delegated wiki builds to subagent may hit stream timeouts mid-execution.

**Detection:** Agent returns "Stream idle timeout" or "Error" with partial tool_use count.

**Resume flow:**
1. Check what files were created (Phase 1, 2, 3 output)
2. Read project `CLAUDE.md` + key entity files to understand prior agent's decisions (classification, new candidates, pattern observations)
3. Spawn new agent with resume-prompt listing: completed work (don't redo) + remaining work (Phase 4a, 4b, 5, 6 typically) + authoritative context files
4. Verify consistency across phases in final Phase 6 fact-verification check

**Validated at v31:** Prior agent completed Phase 1-3 before timeout; resume agent completed Phase 4a-6 cleanly. Pattern preserved across 13 files + 3 vault updates.

---

## Completion criteria (refined v2.1)

Routine reports DONE only when:

- [ ] Phase 0 complete with 12-axis classification + overlap pre-check + un-stale check
- [ ] Phase 1 scaffold (project + 8 subfolders + foundational files)
- [ ] Phase 2 = 3 cluster summaries (with counter-evidence + supply-chain flags if applicable)
- [ ] Phase 3 = 4 entity pages (13-section format, cross-refs mandatory; meta-entity conditional)
- [ ] Phase 4a beginner guide (400-700 lines, bilingual, with ethical/supply-chain framing if applicable)
- [ ] Phase 4b routing-mode-specific deliverable (500-750 lines)
- [ ] Phase 5 iteration log + PATTERN_LIBRARY.md update with overlap-pre-check + consolidation-forward discipline
- [ ] Phase 6 vault sync (project index/log + root CLAUDE/GOALS/PATTERN_LIBRARY) + fact-verification + consistency-check
- [ ] Final report with deliverable counts + velocity + strategic recommendation + backlog escalation if applicable

---

## Status protocol (v2 retained)

Routine returns 1 of 5 statuses:

- **DONE** — all phases complete, no concerns
- **DONE_WITH_CONCERNS** — complete but issues flagged (e.g., inconsistent source docs)
- **BLOCKED** — can't self-resolve (URL inaccessible, license unclear)
- **NEEDS_CONTEXT** — need more info (ambiguous sibling detection, multiple Phase 4b candidates)
- **BLOCKED_CONSOLIDATION** — consolidation guard triggered; user must override or execute consolidation

---

## Defaults (evolved via 31 wikis)

| Default | Value | Evidence |
|---------|-------|----------|
| Bilingual | VN primary + EN technical | 31 wikis |
| Format | 13-section canonical | `llm-wiki-ingest.md` |
| Cluster summaries | 3 | v6-v31 |
| Entity pages | 4 | v10-v31 standardized |
| Beginner guide length | 400-700 lines | 29 wikis |
| Phase 4b deliverable | 500-750 lines | 23 wikis |
| Iteration log length | ~300-500 lines | 29 wikis |
| Velocity target | ~2 hours/wiki | v6-v31 plateau (26 wikis) |
| Continuous execution | YES | 29 wikis |
| WebFetch-first | YES | v6+ lesson |
| Cross-wiki links | MANDATORY | 29 wikis |
| Pattern Library update | REQUIRED Phase 5 | v2+ |
| Storm Bear meta-entity | PER-WIKI evaluation (v29+) | v10-v31 mostly included |
| External URL fetching | When referenced | v2+ |
| Branch fallback | Main → master → v4 → dev | v2+ |
| Overlap pre-check | REQUIRED Phase 0.6 (v2.1 NEW) | v28+ lesson |
| Consolidation-forward discipline | ON (v2.1 NEW) | v31 demonstrated |
| Un-stale check | Phase 0.5 + Phase 5 (v2.1 NEW) | v30 lesson |
| Counter-evidence check | Phase 2 per cluster (v2.1 NEW) | v29 lesson |
| Fact-verification pre-Phase-6 | REQUIRED (v2.1 NEW) | v31 lesson |

---

## Velocity targets (v2 retained)

| Repo size | Phase 2 | Phase 3 | Total | Wiki reference |
|-----------|---------|---------|-------|----------------|
| Small | 20-30 min | 30 min | ~1.5h | codymaster v12 |
| Medium | 30-45 min | 40 min | ~2h | **Plateau v6-v31** |
| Large | 45-60 min | 50-60 min | 2.5-3h | spec-kit v17, agency-agents v18, OpenHands v30 |
| Very large | 60-90 min | 60-90 min | 3-4h | paperclip v14 |

**Plateau observation:** 26 consecutive wikis (v6-v31) completed at ~2h. Velocity is routine-limited, not source-limited.

---

## Anti-patterns (v2.1 expanded)

❌ **Interview questions** — routine is autonomous by design
❌ **Skip Phase 5 iteration log** — log is how routine compounds
❌ **Skip vault sync (Phase 6)** — root files must stay current
❌ **Fabricate counts** — always verify with filesystem commands
❌ **Skip cross-project links** — unique vault value
❌ **Skip consolidation guard** — library integrity requires it
❌ **Skip Pattern Library update** — patterns drift otherwise
❌ **Skip absence detection** — absences as informative as presences
❌ **Over-promote patterns** — respect 5 structural-promotion criteria
❌ **Silent assumption on tier placement** — document rationale
❌ **Force fit to existing patterns** — novel observations deserve candidates; counter-evidence deserves refinement
❌ **Skip overlap pre-check** (v2.1 NEW) — register new candidate only if <70% overlap with existing
❌ **Register standalone when consolidation-forward applies** (v2.1 NEW) — prefer meta-pattern if ≥2 prior observations would be subsumed
❌ **Ignore stale-candidates at Phase 0** (v2.1 NEW) — un-stale check is part of cross-wiki pattern pre-check
❌ **Re-use numbered-pattern references without fact-verification** (v2.1 NEW) — v31 showed #35 mislabel cascading through Pattern Implications wiki
❌ **Defer operator-facing vault actions indefinitely** (v2.1 NEW) — backlog >5 sessions = escalate to BLOCKING-RECOMMENDATION
❌ **Register N=1 candidate without stale-risk evaluation** (v2.1 NEW) — one-off observations should flag at registration

---

## Corpus-first observations tracker (v2.1 expanded)

**Current corpus-first tracker** (selected from v1-v31):
- First CJK-trio README: graphify v16
- First 9-article constitution at T1: spec-kit v17
- First solo-at-enterprise-scale: agency-agents v18
- First non-OSI license: fish-speech v20
- First pseudonymous author: system-prompts-leaks v21
- First ACL 2024 peer-reviewed: LlamaFactory v22
- First dual-licensing: Unsloth v23
- First vision-based browser automation (refined v29): Skyvern v24
- First design-template-aggregator (absorbed v31): awesome-design-md v25
- First 5/5 tier validation: HF agents-course v26
- First recursive corpus reference: OMC v27
- First Microsoft 2nd entrant (T3+T4): markitdown v28
- First solo-enterprise-scale 3rd data point: crawl4ai v29
- First supply-chain incident response: crawl4ai v29 (observation-track)
- First 4-layer T5 academic-commercial fusion: OpenHands v30
- First meta-pattern consolidation promoted at N=3: #68 Awesome-List-Genre (v31 mini-audit)
- First proactive below-trigger mini-audit: v31 mini-audit session

---

## Cross-references

- Parent skill: `llm-wiki-ingest.md`
- Pattern register: `PATTERN_LIBRARY.md` (vault root)
- v2 routine (superseded): `llm-wiki-routine-v2.md`
- v1 routine (historical): `llm-wiki-routine.md`
- Sibling skills: `new-project.md`, `brain-setup.md`, `weekly-update.md`
- Audit documents:
  - `04 Reviews/(C) 2026-04-22 Pattern Library audit post-v29.md` (full audit)
  - `04 Reviews/(C) 2026-04-22 Pattern Library mini-audit post-v31.md` (first mini-audit)
  - `04 Reviews/(C) 2026-04-21 Pattern Library audit post-v27.md` (first retirements)
  - `04 Reviews/(C) 2026-04-20 Pattern Library audit post-v25.md` (reset baseline)
- Diagnostic documents:
  - `04 Reviews/(C) 2026-04-21 Storm Bear vault diagnostic — applying 27 confirmed patterns.md` (v27)
- Evidence: 31 iteration logs across v1-v31 projects

---

## Version log

- **v1** (2026-04-18): First codification from 2 wikis (ECC + Superpowers).
- **v2** (2026-04-19): Consolidated from 102+ action items across v3-v18 (16 additional wikis).
  - Added: consolidation guard, 12-axis Phase 0 probe, 16-mode Phase 4b routing, absence detection, Pattern Library integration, branch fallback, external URL resolution, Storm Bear meta-entity as routine feature, BLOCKED_CONSOLIDATION status.
  - Velocity: unchanged ~2h plateau proven at v6-v18.
- **v2.1** (2026-04-22): Consolidated from ~205 cumulative action items across v19-v31 (13 additional wikis + v29 full audit + v30 direct updates + v31 mini-audit).
  - **Pattern Library maturity additions:**
    - 5 structural-promotion criteria (up from 2): default ≥3-cross-tier / structural-N=2 / spectrum-N=2 / variant-within-pattern-N=2 / meta-pattern-at-N=3-consolidation
    - OBSERVATION-TRACK sub-category (event-based observations)
    - Absorption-retirement mechanism (retire via absorption into superseding pattern)
    - Un-stale mechanism (stale candidates reactivate on 2nd observation)
    - Counter-evidence-driven refinement (narrow scope via counter-example)
  - **Discipline additions:**
    - Audit cadence reform (mini-audit at 0.95:1 / full at 1.05:1)
    - Mini-audit protocol codified as reusable routine
    - Pre-registration overlap pre-check (>70% overlap → reject/consolidate)
    - Consolidation-forward registration discipline
    - N=1 stale-risk-flagging at registration
    - Storm Bear meta-entity per-wiki evaluation (not blanket obligation)
    - Supply-chain awareness protocol (transitive trust-boundary risks)
    - Fact-verification protocol (pre-Phase-6 numbered-pattern re-check)
    - Operator-facing backlog discipline (escalate at 5+ sessions deferral)
    - Stream-timeout resume protocol (delegated builds)
  - **Phase 4b routing modes:** expanded from 16 to ~25 (added: tier-completion-milestone / counter-evidence-refinement / un-stale-mechanism / meta-pattern-consolidation / tier-within-variant-extension / ratio-ceiling / regional-bifurcation / cross-corpus-citation / protocol-directory-meta-reference)
  - **Ratio notation clarification:** ratio = active/confirmed; lower is healthier
  - Velocity: unchanged ~2h plateau proven at v6-v31 (26 consecutive wikis).

- **v2.1 amendment session 66 (2026-04-26 post-v55):** Phase 0.9 Storm Bear meta-entity inclusion check **TIGHTENED to STRICT 1-of-4 hard requirement**. Cautionary-contrast / negation-as-lesson / what-not-to-do framings **REJECTED as inclusion criteria** per Option A discipline-restoration. Trigger: v55 automate-faceless-content agent reported 4/4 FAIL but chose lightweight-INCLUDE via cautionary-contrast framing — Phase 0.9 violation acknowledged. Disciplined-skip is default when 0/4 PASS. Streak counter handling: 38-consecutive Storm Bear meta-entity (v10-v55) GRANDFATHERED per Option A2; strict criteria enforced from v56+. Goodhart's law correction: streak length is downstream metric, NOT inclusion target. Sub-promotion to v2.2 candidate at next routine-version refactor (~v60-v75 natural cadence).

---

**v2.1 codified 2026-04-22. 5 structural-promotion criteria + 4 new mechanisms (absorption-retirement / un-stale / counter-evidence-refinement / OBSERVATION-TRACK) + audit cadence reform + mini-audit protocol + 10 discipline refinements + ~25 Phase 4b routing modes + Phase 0.9 STRICT 1-of-4 inclusion check (session 66 amendment). Consolidates v19-v31 learnings + v29 audit + v30 direct updates + v31 mini-audit + v55 Phase 0.9 tightening. Velocity plateau preserved across 50+ consecutive wikis.**
