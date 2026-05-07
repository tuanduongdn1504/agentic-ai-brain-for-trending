# Storm Bear — Claude Context File

This vault is a personal knowledge base and operating system for Storm Bear, built on the LLM Wiki pattern.


## Who I Am & My Purpose

I'm a software developer and Scrum Coach. I build software and help teams ship.

My purpose is building a persistent, compounding knowledge base following Karpathy's LLM Wiki pattern. The idea: instead of re-deriving knowledge from scratch on every query, the LLM incrementally builds and maintains a structured wiki — summaries, entity pages, cross-references, evolving synthesis. I curate sources, direct analysis, and ask the right questions. The LLM handles all the grunt work. Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.


## Claude's Purpose in This Level

At the vault level, Claude is primarily the wiki maintainer and knowledge architect:

- **Ingest sources** — read new sources, extract key information, write summary pages, update the index, update entity/concept pages across the wiki, append to the log
- **Maintain cross-references** — keep links between pages current, flag contradictions, note where new data challenges old claims
- **Answer queries** — search the wiki, synthesize answers with citations, and file valuable answers back into the wiki as new pages
- **Lint the wiki** — periodically check for contradictions, stale claims, orphan pages, missing cross-references, data gaps
- **Strategic thinking** — help with planning, accountability, brainstorming, and decision-making when called on

The prime directive: don't repeat the same mistake twice.


## Claude's Rules & Boundaries

- **Blunt and direct** — challenge me, don't sugarcoat, call me out when I'm wrong
- **Always end with a suggested next action** — every response should close with what to do next
- **Prefix AI-generated files with `(C)`** — so it's clear what Claude wrote vs. what I wrote
- **Ask before editing existing notes** — never modify my files without permission
- **NEVER fabricate information** — if you don't know, say so. No making things up.
- **NEVER make silent assumptions** — if something is unclear, ask. Don't fill in the blanks and hope I won't notice.


## Vault State Architecture (refactored 2026-04-27 session 67)

**Why this exists:** Pre-refactor CLAUDE.md was 584KB / ~146K tokens — too large for any agent to read without context-thrashing. Three consecutive v56 wiki-build attempts failed at the 4-tool-use mark because agents couldn't fit even one vault file in context. This validated routine v2.1 operator-facing-backlog discipline (35 sessions deferred = 7× threshold) empirically as an INFRASTRUCTURE BLOCK, not a soft warning.

**Refactor:** Bulk state moved to `_state/` chapter files. Each chapter sized <35K tokens so agents can read individual chapters without thrashing. Root CLAUDE.md is now a small shim (~7KB).

**Chapter index — `_state/` directory:**

| Chapter | Content | Size |
|---|---|---|
| `_state/01-skill-references.md` | 5 numbered skill references (LLM Wiki / Brain-setup / New-project / LLM Wiki Routine v2.1 / Pattern Library) — short stable skill definitions | 5KB |
| `_state/02-pattern-library-state-history.md` | Pattern Library state-block accumulation v21-v55 (every audit + post-wiki strengthening notes) | 122KB |
| `_state/03a-projects-v48-v55.md` | Project entries v48-v55 (8 most recent: gh-aw / aidevops / shannon / ollama / MiroFish / awesome-claude-skills / vercel-labs / oh-my-openagent / learn-coding-agent / gsd-2 / automate-faceless-content) | 124KB |
| `_state/03b-projects-v42-v47.md` | Project entries v42-v47 (8 entries: ruflo / rowboat / magika / browser-use / claude-context / dive-into-llms / DeepTutor / bizos / aidevops) | 67KB |
| `_state/04-projects-v30-v39.md` | Project entries v30-v39 (10 entries: pi-mono / claude-hud / claude-code-best-practice / GitNexus / claude-howto / awesome-mcp-servers / OpenHands / LlamaFactory / system-prompts-leaks / fish-speech) | 140KB |
| `_state/05-projects-v1-v29.md` | Project entries v1-v29 (28 oldest entries: ECC v1 through crawl4ai v29 + foundational patterns) | 123KB |

**Reading discipline for agents:**
- Never read more than 1 chapter file in a single session — context-thrashing risk
- Use `awk` via Bash for surgical line-range extracts when full-chapter not needed
- Pattern Library specific entries: read `PATTERN_LIBRARY.md` chapter files (also refactored, see below)
- For wiki builds: read routine + 1 most-recent project chapter (03a) + WebFetch new subject — should fit in ~50-80K tokens

**Authoritative state pointer:** Chapter files are the authoritative state record. Root CLAUDE.md (this file) is the entry-point shim only. Updates go to chapter files; root only updated when adding new chapters or changing this index.


## Patterns đã verified work / Verified Patterns

See `_state/01-skill-references.md` for full descriptions of:
- **Pattern 1:** LLM Wiki pattern (Karpathy) — proven 2026-04-17
- **Pattern 2:** Brain-setup — proven 2026-04-17, v1 (5-round interview) superseded 2026-05-06 by v2 (4-phase incl. continuous-update + lazy-ADR; cross-port from mattpocock /grill-with-docs v57)
- **Pattern 3:** New project scaffolding (template-duplication + 6-question interview) — proven 2026-04-17
- **Pattern 4:** LLM Wiki Routine v2.1 (autonomous orchestration) — proven 2026-04-18, v2.1 codified 2026-04-22, session-66 Phase 0.9 STRICT-tightening 2026-04-26
- **Pattern 5:** Pattern Library (cross-wiki synthesis) — codified 2026-04-19, current state in PATTERN_LIBRARY.md + history in `_state/02-pattern-library-state-history.md`

**Skill files at `05 Skills/`:** 9 skills total — see `05 Skills/SKILL_LOCK_POLICY.md` table for status + rationale.
- 6 IN-FLUX active
- 3 PUBLIC-ARCHIVED historical


## Current Pattern Library state (post-v60 EXTENDED MINI-AUDIT 2026-05-07 session 70)

- **Confirmed:** **41** (was 39; +2 promotions at v60 audit: Pattern #45 Dual-Licensing under criterion 2 + Pattern #72 PolyForm-Family-License RENAME under criterion 4)
- **Active candidates:** 17 (UNCHANGED post-audit)
- **Stale candidates:** **1** (only #52 Extreme-Viral-Velocity OBSERVATIONAL FLAG preserved per pre-registered Item 12; mattpocock/skills first-commit 2026-02-03 → ~3 months at v60 falls in 90d<x<12mo "preserve flag" band; re-evaluate v63)
- **Retired:** 9
- **Observation-tracks:** 6 (Pattern #57 BIDIRECTIONAL-ABSENCE OT REJECTED via 3rd audit-layer fact-verification — corpus-grep falsified v59 absence claim with 53 files / 17+ wikis citing AutoGPT)
- **Total:** **74 full / 58 active**
- **Ratio:** 17:41 = **0.415:1** — NEW LARGEST in corpus history (post-audit drop from 0.436:1); buffer **0.535** below 0.95:1 mini-trigger — NEW LARGEST in corpus history
- **Streaks:** **24-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES** (v37-v60; NEW LONGEST extends v59 23-streak); **Storm Bear meta-entity streak RESTART at 1** post-v59 41-streak break (v60 free-claude-code 2-of-4 PASS INCLUDE — Phase 0.9 STRICT criterion (b) operational-deployability + (d) in-corpus-citation via OpenClaw tagline reference); **5-instance Phase 0.9 post-amendment window with both directions exercised**: v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS = 80% INCLUDE rate validates STRICT amendment is regularly satisfiable AND disciplined-skip works as designed; **2 consecutive CONSERVATIVE-DISCIPLINE mini-audits** (post-v54 + post-v56; no audit at v57-v60); **v60 mini-audit ARMED at natural cadence** per pre-registered 14-item agenda
- **Post-v60 direct strengthening (no audit at v60 ship — pre-registered audit at user's chosen time):** Pattern #57 57c grows to **N=9 conservative-attribution** with NEW polarity sub-variant **57c-positive-comparison-parallel** at v60 (free-claude-code tagline cites OpenClaw via positive parallel; sister to anti-pattern-foil v57+v58; routes within Pattern #57 family) + Pattern #18 NEW Layer 2 sub-archetype **api-protocol-translation-proxy** at T4 N=1 (corpus-first T4 9th archetype; observational within Layer 2) + Pattern #28 NEW per-Claude-tier-routing sub-variant N=1 + Pattern #22 22c NEW corpus-first AGENTS↔CLAUDE explicit-sync-comment-header at v60 + Pattern #19 first-mover-authority-without-lineage strengthens N=1 → N=2 with utility-tool sub-type + Pattern #51 anti-vibe pole streak BREAKS at v60 (2-consecutive-NEUTRAL counter-evidence narrows scope to commercial-educator T1 archetype-correlated) + NEW corpus-first cross-pattern coupled-design at N=4 (P57 polarity × P51 vibe × P19 archetype × tier; library-vocabulary item #9 candidate) + NEW corpus-first T4 2-axis sub-taxonomy (content-transformation N=8 vs protocol-translation N=1)
- **License-axis taxonomy** unchanged at v60 (free-claude-code MIT-only); 7 sub-contexts post-v59 maintained
- **Audit triggers RESET post-v60 EXTENDED MINI-AUDIT.** Next triggers: active candidate count ≥30 (currently 17 — 13-candidate runway) / ratio >0.95:1 mini (currently 0.415:1; ratio-trigger unlikely soon at NEW LARGEST 0.535 buffer) / v63 wiki natural cadence (+3 wikis from v60). **Audit results:** `_state/v60-mini-audit-results-2026-05-07.md` — 14-item LARGEST mini-audit in corpus history; 1st EXTENDED MINI-AUDIT classification; 1st STRENGTHENING-DOMINANT class; 2 promotions + 1 RENAME + 2 sub-variant promotions + 1 sub-sub-axis formalization + 5 formal-statement extensions + 1 OT rejection via fact-verification (3rd in corpus history; LARGEST falsification scope)

For state-block history v21-v55 see `_state/02-pattern-library-state-history.md`.
For pattern definitions see `PATTERN_LIBRARY.md` (refactored — chapter files in `_patterns/`).


## Folder Structure

```
Storm Bear/
├── CLAUDE.md              ← You are here (small shim post-refactor session 67)
├── GOALS.md               ← Goals shim post-refactor (chapters in _goals/)
├── PATTERN_LIBRARY.md     ← Pattern Library shim post-refactor (chapters in _patterns/)
├── _state/                ← CLAUDE.md chapter files (post-refactor session 67)
├── _patterns/             ← PATTERN_LIBRARY.md chapter files (post-refactor session 67)
├── _goals/                ← GOALS.md chapter files (post-refactor session 67)
├── 00 Notes/              ← General notes and raw sources
├── 01 Journals/           ← Journal entries
├── 02 Chess Moves (Long-Term Planning)/ ← Strategic thinking sessions
├── 03 Projects/           ← Project folders, each with its own CLAUDE.md
├── 04 Reviews/            ← Weekly and periodic reviews
└── 05 Skills/             ← Claude skill definitions
```


## My Strengths & Weaknesses

_Not provided. To be filled in when ready._


## My Goals & Current Progress

**Main goal:** Master Claude and autonomous agents for software development.

**Current state:** 60-wiki corpus shipped (v1 ECC 2026-04-17 → v60 free-claude-code 2026-05-07). Vault refactor session 67 + public-release session 68 + v57 ship session 69 + v58 ship session 70 + v59 ship session 71 + v60 ship session 71+ continuation. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v60 free-claude-code shipped session 71+** (2026-05-07; main-loop direct-write compressed-scope per v56-v59 lessons; ~60 min velocity = 5th consecutive sub-1h ship = velocity-plateau-2 confirmed). **v60 EXTENDED MINI-AUDIT executed session 70** (2026-05-07; LARGEST mini-audit in corpus history with 14 items; 1st EXTENDED MINI-AUDIT classification; 1st STRENGTHENING-DOMINANT class; 2 promotions Pattern #45 + Pattern #72 RENAME; 2 sub-variant promotions; 1 sub-sub-axis formalization; 5 formal-statement extensions; 1 OT rejection via 3rd audit-layer fact-verification — corpus-grep falsified v59 BIDIRECTIONAL-ABSENCE claim). **Next:** v63 mini-audit natural cadence (+3 wikis from v60) with 6 carry-forward items; Pattern #52 OBSERVATIONAL FLAG re-evaluation (~6mo mattpocock/skills age at v63); routine v2.2 codification (7 candidates accumulated).


## Weekly Update

> **Last updated:** _2026-05-07 session 70 — v60 EXTENDED MINI-AUDIT executed (LARGEST mini-audit in corpus history; +2 promotions; 1st RENAME-on-promotion; 3rd audit-layer fact-verification correction; ratio 0.415:1 NEW LARGEST buffer 0.535)_

- What's working: routine v2.1 + Pattern Library compounds; **v60 EXTENDED MINI-AUDIT executed cleanly** — 14 items in single session = LARGEST in corpus history (2.3× prior max); pre-registered LOCKED-vs-OPEN protocol validated; 4 pre-step probes resolved 3 OPEN items; Pattern #45 + Pattern #72 promoted (1st RENAME-on-promotion); audit-layer fact-verification protocol caught v59 BIDIRECTIONAL-ABSENCE overstatement (53 files / 17+ wikis cite AutoGPT — Skyvern v24 explicit lineage citation); ratio 0.415:1 NEW LARGEST in corpus history with 0.535 buffer
- What's not working: filename `_state/03a-projects-v48-v55.md` still out-of-date post-v60 (now covers v48-v60+); state-architecture rename deferred to next refactor cycle; v59 wiki BIDIRECTIONAL-ABSENCE claim required falsification at v60 audit (3rd fact-verification correction in corpus suggests routine v2.2 candidate: pre-step required for any "first-of-kind" or "absence" claim before commit)
- What I'm sitting on / need to decide: **free-claude-code pilot deployment** — Storm Bear pilot ranking #3 HIGH-OPERATIONAL (cost-reduction proxy for active Claude-Code workflow; ~1h setup + 1-week measurement + write-up); v27 HIGH item #5 (vault license decision) — now ENRICHED post-v60 audit with PolyForm-Family-License sub-variants 72a + 72b structurally available as alternative considerations; routine v2.2 codification (Phase 0.9 STRICT-triad pattern + EXTENDED MINI-AUDIT classification + pre-step audit protocol + 7 v2.2 candidates accumulated)
- What I'm feeling pulled toward: pilot free-claude-code this week — 1 wiki build through proxy; routine v2.2 codification of EXTENDED MINI-AUDIT + STRICT-triad as next next major skill update
- Any deadlines or time-sensitive things: v63 mini-audit natural cadence (+3 wikis from v60) — 6 carry-forward items including Pattern #52 OBSERVATIONAL FLAG re-evaluation at ~6mo mattpocock/skills age; Pattern #57 57c-positive-comparison-parallel sister sub-variant stale-check v65/v70


## My Current Projects & Overviews

**Bulk content moved to `_state/` chapters post-refactor session 67. Index by version range:**

- **v48-v55 (8 most recent — RED tier projects):** `_state/03a-projects-v48-v55.md`
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest 3 active projects (one-line summary; full entries in chapter files):**

- **v60 free-claude-code** (2026-05-07 session 71+): T4 9th archetype **api-protocol-translation-proxy CORPUS-FIRST** (distinct mechanism from prior 8 content-transformation T4 entrants — translates Anthropic Messages API ↔ 6 upstream provider protocols); **Pattern #57 57c polarity sub-variant CORPUS-FIRST positive-comparison-parallel** (tagline "...like OpenClaw"; sister to anti-pattern-foil v57+v58); **cross-pattern coupled-design CORPUS-FIRST at N=4** (P57 polarity × P51 vibe × P19 archetype × tier — library-vocabulary item #9 candidate); **CORPUS-FIRST T4 2-axis sub-taxonomy** (content-transformation N=8 vs protocol-translation N=1); 24-streak NEW LONGEST; **Storm Bear meta-streak RESTART at 1** (Phase 0.9 STRICT 2-of-4 PASS — (b) operational-deployability + (d) in-corpus-citation; 5-instance window 80% INCLUDE rate validates STRICT amendment regularly satisfiable); **Pattern #51 anti-vibe pole streak BREAKS** at v60 (2-consecutive-NEUTRAL counter-evidence narrows scope to commercial-educator T1 archetype-correlated; pole observational-only); 22c sub-variant NEW corpus-first AGENTS↔CLAUDE explicit-sync-comment-header; Pattern #28 per-Claude-tier-routing NEW sub-variant N=1; 5th consecutive sub-1h direct-write ship = **velocity-plateau-2 confirmed**; **Storm Bear pilot ranking NEW #3** (HIGH-OPERATIONAL cost-reduction utility for active vault Claude-Code workflow; 4-plugin Claude-Code augmentation stack composability with claude-hud + claude-context + claude-howto = zero-conflict orthogonal-layer composition; ~1h setup + 1-week measurement pilot); v60 mini-audit ARMED at natural cadence per pre-registered 14-item agenda; 3 OPEN audit items resolved by v60 evidence; 22.1K stars / Alishahryar1 solo-individual / Python 100% / MIT
- **v59 AutoGPT** (2026-05-07 session 71): **T1+T5 multi-tier monorepo CORPUS-FIRST** — 184K stars 2nd-largest pure-product; 7th EXTREME-primitive-count subject; **CORPUS-RARE DOUBLE UN-STALE** Pattern #45 Dual-Licensing 35-wiki un-stale + Pattern #72 PolyForm-Family-License 26-wiki un-stale-with-RENAME (sub-variants 72a Noncommercial + 72b Shield); Pattern #29 sub-context grows N=4 with NEW sub-sub-axis standardized-vs-bespoke-non-OSI emergent; Pattern #19 founder-personal → org-stewardship NEW sub-variant N=2 + first-mover-authority-without-lineage NEW N=1; Pattern #27 community-viral corpus-historical-foundational sub-path (AutoGPT only-qualifier); Pattern #57 BIDIRECTIONAL-ABSENCE OT candidate; **0/4 STRICT criteria PASS clean → 1st DISCIPLINED-SKIP Storm Bear meta-entity in 41-streak history**; 23-streak NEW LONGEST at probe; ~60 min compressed-scope velocity; pilot relevance MEDIUM-LOW pending license-acceptability decision; 184,043 stars / Significant-Gravitas org / MIT + PolyForm-Shield dual / Python+TS hybrid
- **v58 OpenSpec** (2026-05-07 session 70): T1 — 2nd SDD framework at T1 (after v17 spec-kit); **CORPUS-BROADEST MULTI-PLATFORM-BY-DESIGN AT 30+ TOOLS** (surpasses n8n v56 16-LLM + mattpocock v57 ~8); **PER-TOOL SKILL-FILE FORMAT TRANSLATION** corpus-first deployment-mechanism (~330+ artifacts); Pattern #57 57c-anti-pattern-foil sub-variant emerging (N=2 distinct citing-subjects v57+v58 both target v17 spec-kit); **PSEUDONYMOUS-ORG WITH ACTIVE-COMMERCIAL-PRODUCT** (Fission-AI hidden members) corpus-first archetype; **3-of-4 STRICT criteria PASS**; 22-streak NEW LONGEST at probe; ~55 min compressed-scope velocity; 45.8K stars / Fission-AI org / MIT

For full entries see chapter files. For Pattern Library state history see `_state/02-pattern-library-state-history.md`.
