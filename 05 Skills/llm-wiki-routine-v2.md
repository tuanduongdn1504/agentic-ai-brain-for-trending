# Skill: LLM Wiki Routine v2 — PUBLIC-ARCHIVED (2026-04-29)

⚠️ **THIS SKILL IS SUPERSEDED.** Use the current version instead:
→ `05 Skills/llm-wiki-routine-v2.1.md`

This file is preserved as a historical record of skill evolution. DO NOT modify. DO NOT use in production. For current routine see `llm-wiki-routine-v2.1.md`. For evolution rationale see `05 Skills/SKILL_LOCK_POLICY.md`.

---

# Skill: LLM Wiki Routine v2 (historical)

> **Type:** Orchestration meta-skill (Routine pattern)
> **Version:** v2 — consolidated from 102+ action items accumulated across v3-v18 (16 wikis of learning)
> **Codified:** 2026-04-19 consolidation session
> **Supersedes:** `llm-wiki-routine.md` (v1) — v1 retained for historical reference
> **Parent skill:** `llm-wiki-ingest.md` (methodology)
> **Sibling refs:** `PATTERN_LIBRARY.md` (vault root — authoritative pattern register)

---

## What's new in v2 (vs v1)

v1 was codified after only 2 wikis (ECC + Superpowers). v2 incorporates learnings from 16 additional wikis (v3-v18) across all 5 taxonomy tiers.

### Major changes

1. **Phase 0 probe expanded** — new classification axes (archetype, lineage, methodology, governance) captured at probe time
2. **Pattern Library integration** — Phase 2+3+5 explicitly reference `PATTERN_LIBRARY.md`
3. **Cross-wiki absence detection** — presence AND absence of prior-wiki patterns captured
4. **External URL resolution** — Phase 2 fetches referenced catalogs/guides when counts/lists are external
5. **Branch resolution fallback** — Phase 0 retries common branches (main → master → v4 → dev) on 404
6. **Phase 4b routing expanded** — 16 distinct routing modes now documented (vs 3 in v1)
7. **Consolidation trigger** — routine blocks new wikis when candidate:confirmed > 2:1 or action-backlog > 100
8. **Storm Bear meta-entity** — now routine feature (9+ consecutive wikis at v18)

---

## Invocation (unchanged from v1)

User says: `"LLM wiki for <URL>"`, `"routine for <topic>"`, `"build wiki on <repo>"`.

→ Invoke immediately. No interview. No check-ins between phases.

**Do NOT invoke when:**
- Topic fails Phase 0 threshold
- User explicitly requests interview mode
- **NEW v2:** Consolidation state blocks new wikis (see §Consolidation guard below)

---

## Consolidation guard (NEW in v2)

**Before Phase 0, check consolidation state:**

```
IF (candidates_count / confirmed_count) > 2.0 OR action_backlog > 100:
    Block new wiki. Recommend:
      1. Run Pattern Library audit (PATTERN_LIBRARY.md)
      2. Refactor routine (this file)
      3. Execute pending vault actions (e.g., graphify-on-vault)
    User can override with explicit "proceed despite consolidation state"
```

**Reasoning:** v17 + v18 proved that candidate growth (3-4/wiki) outpaces confirmed-pattern growth without audits. Consolidation maintains library integrity.

**Override:** User can explicitly request wiki build despite state. Honor it, but note the trade-off in Phase 5 iteration log.

---

## 7-phase workflow (refined)

### Phase 0: Pre-flight + enhanced probe (15 min)

**0.1 Consolidation guard check** (v2 NEW) — see above.

**0.2 WebFetch-first probe** (v1 lesson, v2 confirmed):

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

**0.3 Branch resolution fallback** (v2 NEW):

```
IF raw.githubusercontent.com/<repo>/main/<file> returns 404:
    Try: master, v4, v3, dev (common alternatives)
    Log branch in iteration log
```

**0.4 Enhanced classification probe** (v2 NEW) — capture at probe time, don't defer to Phase 3:

| Axis | Values |
|------|--------|
| **Tier** | T1 assistant / T2 service / T3 education / T4 bridge / T5 application / outside-scope |
| **Archetype** | solo-community / solo-VN-authored / founder-personal / community / LLC / official-corporate / solo-enterprise-scale |
| **Scale tier** | small (<5K) / medium (5-20K) / large (20-60K) / X-large (>60K) |
| **Primary lang** | TS / JS / Python / Rust / Go / Shell / Ruby / etc. |
| **Packaging tool** | npm / pip / uv / cargo / shell / brew |
| **Origin story** | individual-author-lineage / methodology-lineage / community-viral / corporate-strategic / unknown |
| **Methodology** | named (SDD / BMM / TDD / XP / DDD) / feature-framework / persona-library / bridge / NONE |
| **Governance file count** | 0-2 (light) / 3-4 (medium) / 5-6 (heavy) |
| **Agent/skill count** | 1-10 / 11-30 / 31-100 / 100+ |
| **i18n coverage** | EN-only / VN / CN / JA / KO / CJK-trio / other |
| **Intellectual influence cited** | Karpathy / John Lam / Bostrom / none / other |
| **Agent platforms supported** | count (if applicable) |

**0.5 Cross-wiki pattern pre-check** (v2 NEW):

```
Check PATTERN_LIBRARY.md:
  - Does new framework fit existing confirmed patterns?
  - Does observation advance any candidate toward confirmation?
  - Is there a notable ABSENCE of prior-wiki patterns? (e.g., no OpenClaw, no Karpathy)
  - Do any cross-wiki standards (OpenClaw, Hermes, AGENTS.md) apply?
```

**0.6 Sibling detection** (v1, refined):

```bash
ls "/Users/Cvtot/KJ OS Template/03 Projects/" | grep "Beginner Analysis"
```

Enable Phase 4b routing decision based on:
- Same-tier peer (N-way comparison)
- Adjacent-tier peer (taxonomy extension)
- Different-domain (meta-reference or outside-scope)

**0.7 Tier placement decision** (v2 NEW — explicit):

```
Classify framework into tier with justification.
If ambiguous (could be T1 or T4), document both possibilities and pick primary.
Record in CLAUDE.md Positioning section.
```

**Outcome of Phase 0:**
- Probe complete with 12-axis classification
- Pattern Library pre-checked
- Tier placement decided
- Phase 4b routing mode identified
- Consolidation state verified

### Phase 1: Scaffold (10 min)

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

Note: v2 standardized folder names (03 Projects now uses "04 Reviews" for iteration logs vs earlier "07 Iteration Logs").

**1.2 CLAUDE.md template** — populate with:
- Repo stats (verbatim from Phase 0)
- 12-axis classification from Phase 0
- Tier placement + justification
- Cross-reference list (all N sibling wikis)
- Phase 4b routing decision preview
- Pattern tests (which patterns does this wiki test?)

**1.3 COMMANDS.md** — point to `llm-wiki-routine-v2` + cross-project references.

**1.4 Foundational wiki files:**
- `02 Wiki/(C) index.md` — phase tracking + sources/entities/published planning + cross-wiki siblings
- `02 Wiki/(C) log.md` — append-only timeline
- `01 Analysis/(C) open questions.md` — 20-30 questions

### Phase 2: Source ingestion (30-45 min)

**Target: 3 cluster summaries** (proven sweet spot v6-v18).

**Cluster strategy** (v2 formalized):

- **Cluster 1:** User-facing docs (README + translations + landing docs)
- **Cluster 2:** Contributor-facing docs (CLAUDE + AGENTS + CONTRIBUTING + SECURITY + etc.)
- **Cluster 3:** Technical/distribution (architecture + packaging + integrations)

**Per cluster:**
- Extract verbatim positioning / philosophy / key claims
- Document 8-12 corpus-first observations
- Check against Pattern Library — does cluster advance any candidate?
- Note ABSENCES (e.g., no Karpathy mention, no OpenClaw) as much as presences
- External URL resolution: if cluster references catalogs/guides hosted externally, fetch them

**Output per cluster:**
- `02 Wiki/(C) <cluster-name> cluster summary.md` (~15-section format)
- Update `(C) log.md` after each cluster
- Update `(C) index.md` Sources table

### Phase 3: Entity pages (40 min)

**Target: 4 entity pages** (v2 standard — up from v1's 3-5).

**Entity selection logic:**

1. **Core product entity** — what does this framework DO
2. **Distribution/ecosystem entity** — how is it delivered + integrated
3. **Novel pattern entity** — what's corpus-first OR pattern-relevant observation
4. **Tier meta + Storm Bear entity** — tier validation + strategic implications

**Format: 13-section canonical** (from `llm-wiki-ingest.md`):
1. Summary
2. Key claims
3. Evidence + sources
4. How it works
5. Worked example
6. Edges + failure modes
7. Related concepts
8. Cross-project comparison
9. Open questions
10. Decision log
11. Storm Bear relevance
12. References
13. Footer

**Cross-references MANDATORY:**
- Every entity references ≥3 sibling wikis
- Pattern Library entries referenced where applicable
- Novel observations tagged as Pattern candidates in PATTERN_LIBRARY.md update

**Storm Bear meta-entity** (v2 formalized) — consistent across 9+ consecutive wikis (v10-v18):
- 4th entity page = tier meta + Storm Bear strategic section
- Includes pilot ranking update, pattern audit notes, consolidation recommendations

### Phase 4a: Beginner bilingual guide (15 min)

**Output:** `03 Published/(C) <repo> - Huong dan cho nguoi moi.md`

**Template:** Parallel 18 prior wikis.

**Structure (10-13 parts):**
1. What is it? (bilingual)
2. Corpus-first signals
3. Tier placement
4. Installation
5. Core usage pattern
6. Novel concepts / key architectural choices
7. vs other corpus frameworks
8. Ethical framing (if autonomy-max tagline OR controversial positioning)
9. Storm Bear relevance (VN operator + Scrum coach fit)
10. 4-week learning roadmap
11. Tradeoffs + limitations
12. References + next action

**Length:** 400-700 lines. Bilingual (VN primary, EN technical).

### Phase 4b: Routing-dependent comparison/taxonomy (20-30 min)

**16 routing modes observed (v1-v18):**

| Mode | Trigger | Example |
|------|---------|---------|
| **Single-peer 2-way** | Same-tier N=2 → N=3 test | v14 T5 paperclip (3-way) |
| **N-way extension** | Same-tier + new entrant | v11 T1 5-way, v12 6-way, v17 7-way, v18 8-way |
| **Taxonomy adjacent** | New tier introduced | v6 T3 education, v7 T4 bridge, v9 T5 application |
| **Tier extension + refinement** | N=3 at established tier | v16 T4 3-way Resolution D |
| **Meta-reference** | Outside-scope wiki | v8 build-your-own-x |
| **Meta-peak** | Karpathy or other lineage touchpoint | v10 autoresearch |
| **Methodology convergence** | Same methodology across frameworks | v17 SDD GSD+spec-kit |
| **Lineage diversification** | New intellectual ancestor | v17 John Lam, v18 no-lineage |
| **Scale-anomaly** | Solo at enterprise-scale | v18 agency-agents |
| **Pattern-test** | First test of prior hypothesis | v14 Pattern #9 T5 test |
| **Platform-tier homogeneity** | T2 validation | v15 multica |
| **Pattern major revision** | Evidence requires formulation change | v18 Pattern #20 |
| **Corporate entrant** | First corporate-official at tier | v17 spec-kit |
| **Cross-wiki standard validation** | OpenClaw/Hermes/etc. confirmation | v18 OpenClaw 5th |
| **Storm Bear direct-action** | Vault applicability observed | v16 graphify |
| **Consolidation trigger** | Audit state exceeded | 2026-04-19 session (this) |

**Routing decision:**
- Review 16 modes — which applies primarily?
- Pick 1 primary mode, up to 2 secondary
- Output template driven by mode

**Output:** `03 Published/(C) <mode-specific-name>.md`

**Length:** 500-750 lines. Primary deliverable type.

### Phase 5: Iteration log (5 min)

**Output:** `04 Reviews/(C) YYYY-MM-DD v<N> build learnings.md`

**Structure (v2 standardized):**

1. **Milestones hit** (corpus-level + framework-specific)
2. **Phase breakdown** (duration per phase)
3. **What worked**
4. **What didn't work / friction** (minor + recurring)
5. **Routine v2 action items** (NEW at this version)
6. **Total action items accumulating**
7. **Meta-observations**
8. **Unique findings**
9. **Storm Bear vault impact**
10. **Next wiki candidates**
11. **Strategic decision point** (consolidation recommendation if applicable)

**Pattern Library update** (v2 NEW) — this phase updates `PATTERN_LIBRARY.md` directly:
- New candidates registered
- Existing candidates with new evidence noted
- Refinements applied (inline to pattern entry)

### Phase 6: Vault sync (5 min)

**Required updates:**

1. **Project `(C) index.md`** → all phases ✅
2. **Project `(C) log.md`** → append Phase 2-6 completion entry
3. **Root `CLAUDE.md`** → add project entry with:
   - Milestone summary
   - Deliverables list
   - Pattern tests applied
   - Storm Bear pilot ranking update
4. **Root `GOALS.md`** → append version log entry with:
   - Corpus-level milestones
   - Pattern Library changes (candidates added, confirmed promoted)
   - Next strategic options
5. **Root `PATTERN_LIBRARY.md`** (v2 NEW) → direct update with:
   - New candidates inline
   - Refinements to existing patterns
   - Promotion status (if applicable)

---

## Completion criteria (refined)

Routine reports DONE only when:

- [ ] Phase 0 complete with 12-axis classification
- [ ] Phase 1 scaffold (project + 8 subfolders + foundational files)
- [ ] Phase 2 = 3 cluster summaries
- [ ] Phase 3 = 4 entity pages (13-section format, cross-refs mandatory)
- [ ] Phase 4a beginner guide (400-700 lines, bilingual)
- [ ] Phase 4b routing-mode-specific deliverable (500-750 lines)
- [ ] Phase 5 iteration log + PATTERN_LIBRARY.md update
- [ ] Phase 6 vault sync (project index/log + root CLAUDE/GOALS/PATTERN_LIBRARY)
- [ ] Final report with deliverable counts + velocity + strategic recommendation

---

## Status protocol

Routine returns 1 of 5 statuses (v2 adds BLOCKED_CONSOLIDATION):

- **DONE** — all phases complete, no concerns
- **DONE_WITH_CONCERNS** — complete but issues flagged (e.g., inconsistent source docs)
- **BLOCKED** — can't self-resolve (URL inaccessible, license unclear)
- **NEEDS_CONTEXT** — need more info (ambiguous sibling detection, multiple Phase 4b candidates)
- **BLOCKED_CONSOLIDATION** (v2 NEW) — consolidation guard triggered; user must override or execute consolidation

---

## Defaults (evolved via 18 wikis)

| Default | Value | Evidence |
|---------|-------|----------|
| Bilingual | VN primary + EN technical | 18 wikis |
| Format | 13-section canonical | `llm-wiki-ingest.md` |
| Cluster summaries | 3 | v6-v18 |
| Entity pages | 4 | v10-v18 standardized |
| Beginner guide length | 400-700 lines | 16 wikis |
| Phase 4b deliverable | 500-750 lines | 10 wikis |
| Iteration log length | ~300-500 lines | 16 wikis |
| Velocity target | ~2 hours/wiki | v6-v18 plateau |
| Continuous execution | YES | 16 wikis |
| WebFetch-first | YES | v6+ lesson |
| Cross-wiki links | MANDATORY | 16 wikis |
| Pattern Library update | REQUIRED Phase 5 | v2 NEW |
| Storm Bear meta-entity | REQUIRED (4th entity) | v10-v18 |
| External URL fetching | When referenced | v2 NEW |
| Branch fallback | Main → master → v4 → dev | v2 NEW (v16 lesson) |

---

## Velocity targets (v2 refined)

| Repo size | Phase 2 | Phase 3 | Total | Wiki reference |
|-----------|---------|---------|-------|----------------|
| Small | 20-30 min | 30 min | ~1.5h | codymaster v12 |
| Medium | 30-45 min | 40 min | ~2h | **Plateau v6-v18** |
| Large | 45-60 min | 50-60 min | 2.5-3h | spec-kit v17, agency-agents v18 |
| Very large | 60-90 min | 60-90 min | 3-4h | paperclip v14 |

**Plateau observation:** 13 consecutive wikis (v6-v18) completed at ~2h. Velocity is routine-limited, not source-limited.

---

## Anti-patterns (v2 expanded)

❌ **Interview questions** — routine is autonomous by design
❌ **Skip Phase 5 iteration log** — log is how routine compounds
❌ **Skip vault sync (Phase 6)** — root files must stay current
❌ **Fabricate counts** — always verify with filesystem commands
❌ **Skip cross-project links** — unique vault value
❌ **Skip consolidation guard** (v2 NEW) — library integrity requires it
❌ **Skip Pattern Library update** (v2 NEW) — patterns drift otherwise
❌ **Skip absence detection** (v2 NEW) — absences as informative as presences
❌ **Over-promote patterns** (v2 NEW) — candidates require ≥3 observations across 2+ tiers
❌ **Silent assumption on tier placement** (v2 NEW) — document rationale
❌ **Force fit to existing patterns** (v2 NEW) — novel observations deserve new candidates

---

## Corpus-first observations tracker

When a new wiki reveals a corpus-first (something no prior wiki has shown), v2 routine:

1. Record in Phase 2 cluster summary as "corpus-first observation"
2. Reference in Phase 3 entity page
3. Consider as Pattern candidate in Phase 5 iteration log
4. Update PATTERN_LIBRARY.md if clear pattern emerges

**Current corpus-first tracker** (selected from v1-v18):
- First CJK-trio README: graphify v16
- First uv tool install: spec-kit v17
- First 9-article constitution at T1: spec-kit v17
- First solo-at-enterprise-scale: agency-agents v18
- First Reddit-viral origin: agency-agents v18
- First Game Development division: agency-agents v18
- First anti-vibe-coding stance: spec-kit v17
- First personality-driven agent design: agency-agents v18

---

## Consolidation protocol (NEW in v2)

When consolidation guard triggers, routine proposes one of:

1. **Run graphify on vault** — concrete, fast (~30-60 min), high-leverage
2. **Pattern Library audit** — apply criteria to candidates (~1-2h)
3. **Routine v2 refactor** — this file already executed 2026-04-19; update needed at 5+ new action items

**Format for consolidation proposal:**

```
⚠️ CONSOLIDATION GUARD TRIGGERED

State:
- Candidates: X / Confirmed: Y (ratio Z)
- Action backlog: N items

Recommended actions (in order):
1. [Cheapest / highest-leverage action]
2. [Audit action]
3. [Refactor action]

Override: User can reply "proceed despite consolidation" to build wiki anyway.
```

---

## Cross-references

- Parent skill: `llm-wiki-ingest.md`
- Pattern register: `PATTERN_LIBRARY.md` (vault root)
- v1 routine (superseded): `llm-wiki-routine.md`
- Sibling skills: `new-project.md`, `brain-setup.md`, `weekly-update.md`
- Evidence: 18 iteration logs across v1-v18 projects

---

## Version log

- **v1** (2026-04-18): First codification from 2 wikis (ECC + Superpowers).
- **v2** (2026-04-19): Consolidated from 102+ action items across v3-v18 (16 additional wikis).
  - Added: consolidation guard, 12-axis Phase 0 probe, 16-mode Phase 4b routing, absence detection, Pattern Library integration, branch fallback, external URL resolution, Storm Bear meta-entity as routine feature, new BLOCKED_CONSOLIDATION status.
  - Velocity: unchanged ~2h plateau proven at v6-v18.
