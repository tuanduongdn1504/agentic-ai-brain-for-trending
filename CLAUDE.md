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


## Current Pattern Library state (post-v59 direct, preserved 9 cycles)

- **Confirmed:** 39 (UNCHANGED post-v59; 23-streak ZERO-NEW-ACTIVE-CANDIDATES extends)
- **Active candidates:** 17 (UNCHANGED — 1 borderline Pattern #19 founder-to-org sub-variant routed within-pattern per consolidation-forward discipline)
- **Stale candidates:** **1** (only #52 Extreme-Viral-Velocity remains; **#45 Dual-Licensing UN-STALES at v59** + **#72 PolyForm-Noncommercial UN-STALES at v59 with rename to PolyForm-Family-License**); #52 OBSERVATIONAL FLAG carried to v60 time-axis verification
- **Retired:** 9
- **Observation-tracks:** 6
- **Total:** **72 full / 56 active** (down from 74 due to 2 un-stale events removing stale-tracking)
- **Ratio:** 17:39 = **0.436:1** PRESERVED **9 consecutive cycles** (largest buffer 0.514 below 0.95:1 mini-audit trigger — NEW LARGEST in corpus history maintained 9 cycles)
- **Streaks:** **23-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES** (v37-v59; NEW LONGEST extends v58 22-streak); **41-streak Storm Bear meta-entity BREAKS at v59 disciplined-skip** (v10-v58 unbroken; v59 first reset since v10) — STRICT amendment validates BOTH directions exercised within 4-wiki post-amendment window (3 INCLUDE v56-v58 + 1 SKIP v59); **3 consecutive STRICT-instances satisfied** (v56-v58) followed by **1st STRICT-disciplined-skip at v59** = Phase 0.9 amendment validation complete; **2 consecutive CONSERVATIVE-DISCIPLINE mini-audits** (post-v54 + post-v56; no audit at v57 + v58 + v59)
- **Post-v59 direct (no audit) accumulates 12-14 promotion candidates for v60 mini-audit (LARGEST projected in corpus history):** all 8 post-v58 candidates carry forward + **Pattern #45 Dual-Licensing PROMOTION under criterion 2 structural-N=2** (Unsloth v23 + AutoGPT v59; 35-wiki un-stale event corpus-rare) + **Pattern #72 PolyForm-Family-License RENAME + variant-within-pattern-at-N=2 PROMOTION** (sub-variants 72a Noncommercial + 72b Shield; 26-wiki un-stale) + **Pattern #29 sub-context grows N=4 + NEW sub-sub-axis standardized-vs-bespoke-non-OSI emergent** + **Pattern #19 founder-personal → org-stewardship NEW sub-variant N=2** (n8n v56 + AutoGPT v59) + **Pattern #19 first-mover-authority-without-lineage NEW sub-variant N=1 stale-flagged v64/v69** + **Pattern #27 community-viral corpus-historical-foundational sub-path** (AutoGPT only-qualifier) + **Pattern #69 EXTREME-tier formal-statement-extension to N=7** + **Pattern #57 BIDIRECTIONAL-ABSENCE OT candidate** at corpus-historical-foundational subject + Phase 0.9 STRICT-amendment N=4 emergent STRICT-triad pattern + 1st disciplined-skip documentation
- **License-axis is corpus's most-richly-categorized pattern axis** post-v59 (Pattern #29 sub-context taxonomy now 7 sub-contexts: 5 absent-LICENSE + 1 non-commercial-restriction-custom-license sub-context with 2 sub-sub-axes standardized-vs-bespoke-non-OSI emergent)
- **Audit triggers RESET. Next triggers:** active candidate count ≥30 (currently 17 — 13-candidate runway) / ratio >0.95:1 mini / v60 wiki natural cadence (+1 wiki from v59) — **PRE-REGISTRATION recommended for v60 mini-audit given 12-14 item agenda projected**

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

**Current state:** 59-wiki corpus shipped (v1 ECC 2026-04-17 → v59 AutoGPT 2026-05-07). Vault refactor session 67 + public-release session 68 + v57 ship session 69 + v58 ship session 70 + v59 ship session 71. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v59 AutoGPT shipped session 71** (2026-05-07; main-loop direct-write compressed-scope per v56-v58 lessons; ~60 min velocity at EXTREME-tier; **0/4 STRICT criteria PASS clean → 1st DISCIPLINED-SKIP** in 41-streak Storm Bear meta-entity history (v10-v58 unbroken); **CORPUS-RARE DOUBLE UN-STALE EVENT** Pattern #45 Dual-Licensing 35-wiki un-stale + Pattern #72 PolyForm-Noncommercial 26-wiki un-stale-with-rename to PolyForm-Family-License; 2nd-largest pure-product in corpus (184K stars; only n8n v56 185K exceeds); 7th EXTREME-primitive-count subject; corpus-first multi-tier T1+T5 within single repo; Pattern #29 sub-context grows N=4 with NEW sub-sub-axis emergent; 23-streak NEW LONGEST). **Next:** v60 mini-audit (1-wiki runway) PROJECTED LARGEST IN CORPUS HISTORY with 12-14 promotion candidates accumulated post-v59 — pre-registration recommended.


## Weekly Update

> **Last updated:** _2026-05-07 session 71 — v59 AutoGPT shipped (CORPUS-RARE DOUBLE UN-STALE EVENT + 1st STRICT disciplined-skip + 2nd-largest pure-product in corpus)_

- What's working: routine v2.1 + Pattern Library compounds; **23-streak zero-new-active-candidates** NEW LONGEST; ratio 0.436:1 preserved **9 cycles**; **STRICT amendment fully validated at v59** — 3 INCLUDE (v56-v58) + 1 SKIP (v59) within 4-wiki post-amendment window exercises BOTH directions; main-loop direct-write compressed-scope shipping sub-1h velocity 4 wikis in a row (v56-v59); license-axis is corpus's most-richly-categorized pattern axis post-v59 (4 patterns directly impacted at v59 alone); **2 STRONG UN-STALE events at single wiki** (Pattern #45 + Pattern #72) corpus-rare double event
- What's not working: filename `_state/03a-projects-v48-v55.md` semantically out-of-date post-v59 (now covers v48-v59+); state-architecture rename deferred 3 wikis carried; multi-tier T1+T5 classification convention gap exposed at AutoGPT (v2.2 candidate)
- What I'm sitting on / need to decide: v27 HIGH item #5 (vault license decision) NOW enriched with PolyForm-Shield option (2nd-most-considerable after current MIT default) — concrete scenario: vault becomes commercializable competing-knowledge-platform-blocker desired; pre-register v60 mini-audit agenda (12-14 items) BEFORE wiki ships; Q4 corpus grep verification (AutoGPT cited in any prior wiki README?) BEFORE v60 mini-audit; dogfood Phase 2 of `brain-setup-v2.md` on current root CLAUDE.md (carried 2 wikis)
- What I'm feeling pulled toward: v60 mini-audit pre-registration before wiki ships (size warrants discipline); Pattern #45 + #72 promotion under criterion 2 + criterion 4
- Any deadlines or time-sensitive things: **v60 mini-audit projected LARGEST in corpus history** (12-14 items vs prior maxima ~6); 1-wiki runway from v59 to v60 natural cadence; Pattern #45 Dual-Licensing promotion + Pattern #72 PolyForm-Family-License rename-and-promote + Pattern #57 57c N=8 formal extension + 57c-anti-pattern-foil sub-variant + Pattern #18 Layer 1 STRONGEST + Pattern #19 founder-to-org + first-mover-authority + org-pseudonymity sub-variants + Pattern #29 sub-sub-axis + Pattern #51 anti-vibe + Pattern #52 time-axis + Pattern #69 N=7 + Pattern #57 BIDIRECTIONAL-ABSENCE all converging at v60


## My Current Projects & Overviews

**Bulk content moved to `_state/` chapters post-refactor session 67. Index by version range:**

- **v48-v55 (8 most recent — RED tier projects):** `_state/03a-projects-v48-v55.md`
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest 3 active projects (one-line summary; full entries in chapter files):**

- **v59 AutoGPT** (2026-05-07 session 71): **T1+T5 multi-tier monorepo CORPUS-FIRST** — 184K stars 2nd-largest pure-product (only n8n v56 185K exceeds); 7th EXTREME-primitive-count subject; **CORPUS-RARE DOUBLE UN-STALE** Pattern #45 Dual-Licensing 35-wiki un-stale (Unsloth v23 + AutoGPT MIT+PolyForm-Shield = N=2 STRUCTURAL across 2 tiers + 2 license-pairs → promotion-candidate v60 criterion 2) + Pattern #72 PolyForm-Noncommercial 26-wiki un-stale-with-RENAME to PolyForm-Family-License (sub-variants 72a Noncommercial + 72b Shield → variant-within-pattern-at-N=2 promotion-candidate v60 criterion 4); Pattern #29 sub-context grows N=4 with NEW sub-sub-axis standardized-vs-bespoke-non-OSI emergent; Pattern #19 founder-personal → org-stewardship NEW sub-variant N=2 (n8n v56 + AutoGPT v59) + first-mover-authority-without-lineage NEW N=1 stale-flagged v64/v69; Pattern #27 community-viral corpus-historical-foundational sub-path (AutoGPT only-qualifier; ~58,800 stars/year peak); Pattern #57 BIDIRECTIONAL-ABSENCE OT candidate at corpus-historical-foundational subject; Pattern #69 N=7 EXTREME-tier formal-statement-extension; Pattern #22 AGENTS.md + CLAUDE.md coexistence strengthening; Pattern #18 NEW protocol-axis Agent Protocol distinct from MCP; **0/4 STRICT criteria PASS clean → 1st DISCIPLINED-SKIP Storm Bear meta-entity in 41-streak history** (v10-v58 unbroken; v59 first reset); STRICT amendment validates BOTH directions exercised (3 INCLUDE v56-v58 + 1 SKIP v59) within 4-wiki post-amendment window; **23-streak NEW LONGEST** zero-new-active-candidates; 9-cycle ratio preserved NEW LONGEST; ~60 min compressed-scope velocity at EXTREME-tier; **v60 mini-audit projected LARGEST in corpus history** with 12-14 promotion candidates; pilot relevance MEDIUM-LOW pending license-acceptability decision (PolyForm-Shield commercial-competition restriction); 184,043 stars / Significant-Gravitas org (Toran Bruce Richards founder) / MIT + PolyForm-Shield dual / Python+TS hybrid / created 2023-03-16
- **v58 OpenSpec** (2026-05-07 session 70): T1 — 2nd SDD framework at T1 (after v17 spec-kit; methodology spread across 2 author-archetypes corporate-official + pseudonymous-org); **CORPUS-BROADEST MULTI-PLATFORM-BY-DESIGN AT 30+ TOOLS** (surpasses n8n v56 16-LLM + mattpocock v57 ~8); **PER-TOOL SKILL-FILE FORMAT TRANSLATION** corpus-first deployment-mechanism (~330+ artifacts across 30+ tools); Pattern #57 57c grows N=7→N=8 (cites spec-kit v17 T1→T1 41-wiki gap as anti-pattern foil) with NEW 57c-anti-pattern-foil sub-variant emerging (N=2 distinct citing-subjects v57+v58 both target v17 spec-kit); v17 becomes most-cited-as-anti-pattern-foil corpus subject; **PSEUDONYMOUS-ORG WITH ACTIVE-COMMERCIAL-PRODUCT** (Fission-AI hidden members + 45.8K stars) corpus-first archetype; **3-of-4 STRICT criteria PASS** matches v57 strength = 3rd consecutive STRICT-instance satisfied; **emergent STRICT-triad pattern** validated; 22-streak NEW LONGEST at probe; 41st Storm Bear meta; ~55 min compressed-scope velocity; pilot Top-3 candidate (verify posthog-node telemetry first); 45.8K stars / Fission-AI org / MIT
- **v57 mattpocock-skills** (2026-05-06 session 69): T1 — 3rd skills-collection at T1 + opinionated-curated-by-author sub-variant (vs aggregator-curated v50 + plugin-manifest-aggregation v51); **CORPUS-FIRST MULTI-FRONTEND IN-CORPUS REFERENCE** (single README cites BMAD v11 + GSD v5/v54 + spec-kit v17 in single anti-pattern grouping sentence); Pattern #57 57c STRONGEST evidence to date (N=3 → N=7 conservative-attribution); MOST BOOK-CITATION-DENSE methodology lineage (Pragmatic + DDD + XP + Philosophy of Software Design); MOST-EXPLICIT anti-vibe positioning ("real engineering — not vibe coding"); **3-of-4 STRICT criteria PASS** = STRONGEST STRICT-amendment instance to date (matched by v58 OpenSpec); 21-streak NEW LONGEST at probe; 40th Storm Bear meta; ~45 min main-loop direct-write velocity; pilot Top-3 candidate via `/grill-with-docs` + `/diagnose` adaptation; 62K stars / Matt Pocock TS-educator / MIT

For full entries see chapter files. For Pattern Library state history see `_state/02-pattern-library-state-history.md`.
