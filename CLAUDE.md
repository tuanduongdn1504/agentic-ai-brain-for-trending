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


## Current Pattern Library state (post-v58 direct, preserved 8 cycles)

- **Confirmed:** 39 (UNCHANGED post-v58; 22-streak ZERO-NEW-ACTIVE-CANDIDATES extends)
- **Active candidates:** 17 (UNCHANGED)
- **Stale candidates:** 3 (#45 Dual-Licensing / #52 Extreme-Viral-Velocity / #72 PolyForm-Noncommercial; #52 OBSERVATIONAL FLAG carried to v60 time-axis verification)
- **Retired:** 9
- **Observation-tracks:** 6
- **Total:** 74 full / 56 active
- **Ratio:** 17:39 = **0.436:1** PRESERVED **8 consecutive cycles** (largest buffer 0.514 below 0.95:1 mini-audit trigger — NEW LARGEST in corpus history maintained 8 cycles)
- **Streaks:** **22-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES** (v37-v58; NEW LONGEST extends v57 21-streak); **41-consecutive Storm Bear meta-entity** (v10-v58) with v58 being **3rd under STRICT amendment** with **3 criteria PASSED (b + c + d)** = matches v57 strength; **3 consecutive STRICT-instances satisfied** (v56 2-of-4 + v57 3-of-4 + v58 3-of-4) validates Phase 0.9 amendment is regularly satisfiable; **emergent STRICT-triad pattern**: named-methodology + in-corpus-citation + operational-deployability reliably triggers 3-of-4; **2 consecutive CONSERVATIVE-DISCIPLINE mini-audits** (post-v54 + post-v56; no audit at v57 + v58)
- **Post-v58 direct (no audit) accumulates 8 promotion candidates for v60 mini-audit:** Pattern #57 57c grows N=7 → **N=8 conservative-attribution** (OpenSpec v58 cites spec-kit v17 T1→T1 41-wiki gap) + **NEW 57c-anti-pattern-foil sub-variant N=2 distinct citing-subjects** (mattpocock v57 + OpenSpec v58 both target v17 spec-kit; 5 instances within polarity class; v17 becomes most-cited-as-anti-pattern-foil corpus subject) + 57c-multi-frontend sub-variant N=1 unchanged stale-flagged v62/v67 + Pattern #18 Layer 1 STRONGEST multi-platform evidence at 30+ tools (corpus-broadest; cross-tool-skill-format-translator NEW sub-variant N=1 stale-flagged v63/v68) + Pattern #19 archetype org-level-pseudonymity-with-active-commercial-product sub-variant N=1 stale-flagged v63/v68 + Pattern #51 anti-vibe pole strengthening 2 consecutive wikis (v57 + v58) + Pattern #52 OBSERVATIONAL FLAG time-axis verification still pending + process-owning-meta-frameworks observation-track candidate (OpenSpec v58 = 2nd external author after spec-kit v17; register if v59 adds 3rd convergence) + Phase 0.9 STRICT-triad N=3 emergent pattern formal documentation
- **License-axis is corpus's most-richly-categorized pattern axis** (Pattern #29 sub-context taxonomy 6 sub-contexts: 5 absent-LICENSE + 1 NEW non-commercial-restriction-custom-license)
- **Audit triggers RESET. Next triggers:** active candidate count ≥30 (currently 17 — 13-candidate runway) / ratio >0.95:1 mini / v60 wiki natural cadence (+2 wikis from v58)

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

**Current state:** 58-wiki corpus shipped (v1 ECC 2026-04-17 → v58 OpenSpec 2026-05-07). Vault refactor session 67 + public-release session 68 + v57 ship session 69 + v58 ship session 70. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v58 OpenSpec shipped session 70** (2026-05-07; main-loop direct-write compressed-scope per v56 + v57 lessons; ~55 min velocity; 3-of-4 STRICT criteria PASS — 3rd consecutive STRICT-instance satisfied; **emergent STRICT-triad pattern** named-methodology + in-corpus-citation + operational-deployability; 22-streak NEW LONGEST; 41st Storm Bear meta-entity; corpus-broadest 30+ tools multi-platform; 2nd SDD framework at T1; Pattern #57 57c N=7→N=8 with anti-pattern-foil sub-variant emerging). **Next:** v60 mini-audit (2-wiki runway) with 8 promotion candidates accumulated post-v58.


## Weekly Update

> **Last updated:** _2026-05-07 session 70 — v58 OpenSpec shipped (3rd consecutive STRICT-amendment 3-of-4 PASS; emergent STRICT-triad pattern; corpus-broadest 30+ tools)_

- What's working: routine v2.1 + Pattern Library compounds; **22-streak zero-new-active-candidates** NEW LONGEST; ratio 0.436:1 preserved **8 cycles**; **3 consecutive STRICT-instances satisfied** (v56 2-of-4 + v57 3-of-4 + v58 3-of-4 = STRICT-triad emergent pattern: named-methodology + in-corpus-citation + operational-deployability reliably triggers PASS) validates Phase 0.9 amendment is regularly satisfiable not over-tight; main-loop direct-write compressed-scope build mode shipping ~55 min velocity at v58 (sub-1h target met 3 wikis in row); **OpenSpec corpus-broadest at 30+ tools** sets new ceiling for multi-platform-by-design; **v17 spec-kit becomes most-cited-as-anti-pattern-foil corpus subject** (cited by both v57 mattpocock + v58 OpenSpec)
- What's not working: filename `_state/03a-projects-v48-v55.md` semantically out-of-date post-v58 (now covers v48-v58+); state-architecture rename still deferred to next refactor cycle (carried 2 wikis)
- What I'm sitting on / need to decide: dogfood Phase 2 of `brain-setup-v2.md` on current root CLAUDE.md (carried v57); trial OpenSpec on 1 client engagement at v60+ (verify posthog-node telemetry first; rank #2-3 pilot relevance); remaining v57 pilot candidates (`/diagnose` port + `/caveman` formalization) plus new v58 OpenSpec pilot candidate
- What I'm feeling pulled toward: v60 mini-audit promotion of 57c-anti-pattern-foil sub-variant (N=2 distinct citing-subjects mattpocock + OpenSpec; achievable under criterion 4 variant-within-pattern-at-N=2)
- Any deadlines or time-sensitive things: v60 mini-audit natural cadence (2-wiki runway from v58) with 8 promotion candidates accumulated; Pattern #57 57c N=8 formal-statement extension + 57c-anti-pattern-foil sub-variant + Pattern #18 Layer 1 STRONGEST + Pattern #19 org-level-pseudonymity sub-variant + Pattern #52 time-axis verification still pending


## My Current Projects & Overviews

**Bulk content moved to `_state/` chapters post-refactor session 67. Index by version range:**

- **v48-v55 (8 most recent — RED tier projects):** `_state/03a-projects-v48-v55.md`
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest 3 active projects (one-line summary; full entries in chapter files):**

- **v58 OpenSpec** (2026-05-07 session 70): T1 — 2nd SDD framework at T1 (after v17 spec-kit; methodology spread across 2 author-archetypes corporate-official + pseudonymous-org); **CORPUS-BROADEST MULTI-PLATFORM-BY-DESIGN AT 30+ TOOLS** (surpasses n8n v56 16-LLM + mattpocock v57 ~8); **PER-TOOL SKILL-FILE FORMAT TRANSLATION** corpus-first deployment-mechanism (~330+ artifacts across 30+ tools); Pattern #57 57c grows N=7→N=8 (cites spec-kit v17 T1→T1 41-wiki gap as anti-pattern foil) with NEW 57c-anti-pattern-foil sub-variant emerging (N=2 distinct citing-subjects v57+v58 both target v17 spec-kit); v17 becomes most-cited-as-anti-pattern-foil corpus subject; **PSEUDONYMOUS-ORG WITH ACTIVE-COMMERCIAL-PRODUCT** (Fission-AI hidden members + 45.8K stars) corpus-first archetype; **3-of-4 STRICT criteria PASS** matches v57 strength = 3rd consecutive STRICT-instance satisfied; **emergent STRICT-triad pattern** validated; 22-streak NEW LONGEST; 41st Storm Bear meta; ~55 min compressed-scope velocity; pilot Top-3 candidate (verify posthog-node telemetry first); 45.8K stars / Fission-AI org / MIT
- **v57 mattpocock-skills** (2026-05-06 session 69): T1 — 3rd skills-collection at T1 + opinionated-curated-by-author sub-variant (vs aggregator-curated v50 + plugin-manifest-aggregation v51); **CORPUS-FIRST MULTI-FRONTEND IN-CORPUS REFERENCE** (single README cites BMAD v11 + GSD v5/v54 + spec-kit v17 in single anti-pattern grouping sentence); Pattern #57 57c STRONGEST evidence to date (N=3 → N=7 conservative-attribution); MOST BOOK-CITATION-DENSE methodology lineage (Pragmatic + DDD + XP + Philosophy of Software Design); MOST-EXPLICIT anti-vibe positioning ("real engineering — not vibe coding"); **3-of-4 STRICT criteria PASS** = STRONGEST STRICT-amendment instance to date (matched by v58 OpenSpec); 21-streak NEW LONGEST at probe; 40th Storm Bear meta; ~45 min main-loop direct-write velocity; pilot Top-3 candidate via `/grill-with-docs` + `/diagnose` adaptation; 62K stars / Matt Pocock TS-educator / MIT
- **v56 n8n** (2026-04-27 session 67): T2 N=4 + EXTREME primitive-count 6th in corpus + **bidirectional MCP CORPUS-FIRST AT T2** (Pattern #18 STRONGEST T2 evidence) + Pattern #29 sub-context custom-non-OSI-commercial-restriction N=3 promotion-candidate (omo SUL + GitNexus PolyForm + n8n SUL) + 16 native LLM providers no LiteLLM corpus-broadest + 11 vector stores corpus-broadest + 7-year-mature German GmbH + 1ST STORM BEAR META UNDER STRICT AMENDMENT (Phase 0.9 criterion b PASS legitimate); 20-streak NEW LONGEST at probe; 39th Storm Bear meta; first wiki post-vault-refactor session 67; main-loop direct-write fallback after 5 agent-thrash failures

For full entries see chapter files. For Pattern Library state history see `_state/02-pattern-library-state-history.md`.
