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
- **Pattern 2:** Brain-setup interview (5 rounds) — proven 2026-04-17
- **Pattern 3:** New project scaffolding — proven 2026-04-17
- **Pattern 4:** LLM Wiki Routine v2.1 (autonomous orchestration) — proven 2026-04-18, v2.1 codified 2026-04-22, session-66 Phase 0.9 STRICT-tightening 2026-04-26
- **Pattern 5:** Pattern Library (cross-wiki synthesis) — codified 2026-04-19, current state in PATTERN_LIBRARY.md + history in `_state/02-pattern-library-state-history.md`

**Skill files at `05 Skills/`:**
- `llm-wiki-routine-v2.1.md` (current; tightened session 66)
- `llm-wiki-routine-v2.md` (superseded 2026-04-22)
- `llm-wiki-routine.md` (v1; superseded 2026-04-19)
- `brain-setup.md`
- `new-project.md`


## Current Pattern Library state (post-v56-mini-audit, preserved 6 cycles)

- **Confirmed:** 39 (UNCHANGED post-mini-audit; 2nd CONSERVATIVE-DISCIPLINE audit in corpus history)
- **Active candidates:** 17
- **Stale candidates:** 3 (#45 Dual-Licensing / #52 Extreme-Viral-Velocity / #72 PolyForm-Noncommercial)
- **Retired:** 9
- **Observation-tracks:** 6
- **Total:** 74 full / 56 active
- **Ratio:** 17:39 = **0.436:1** PRESERVED **6 consecutive cycles** (largest buffer 0.514 below 0.95:1 mini-audit trigger — NEW LARGEST in corpus history maintained 6 cycles)
- **Streaks:** **20-consecutive-wiki ZERO-NEW-ACTIVE-CANDIDATES** (v37-v56; LONGEST); **39-consecutive Storm Bear meta-entity** (v10-v56) with v56 being **1st under STRICT amendment** with **2 criteria PASSED (b + d)** post-audit Q1-resolution (Skyvern v24→n8n v56 32-wiki gap = criterion d evidence); **2 consecutive CONSERVATIVE-DISCIPLINE mini-audits** (post-v54 + post-v56)
- **Post-v56 mini-audit (session 67) executed 5 actions:** Pattern #29 NEW formal sub-context "29-non-commercial-restriction-custom-license" (omo SUL-1.0 + GitNexus PolyForm + n8n SUL = N=3 across T1+T2+T5; default ≥3-cross-tier criterion satisfied) + Pattern #18 Layer 0 horizontal-aggregation 0b STRUCTURAL N=2 within already-confirmed (Pattern #18 reaches **10th refinement** — most-refined pattern in library extends) + Pattern #57 57c forward-citation-then-wiki N=3 formal-statement extension (Skyvern v24→n8n v56 32-wiki gap NEW; mean gap 31 wikis; range 25-36) + Pattern #69 EXTREME 4-tier-coverage formal-statement extension + Pattern #50 50a Standard 4-tier-coverage formal-statement extension
- **License-axis is corpus's most-richly-categorized pattern axis** (Pattern #29 sub-context taxonomy 6 sub-contexts: 5 absent-LICENSE + 1 NEW non-commercial-restriction-custom-license)
- **Audit triggers RESET. Next triggers:** active candidate count ≥30 (currently 17 — 13-candidate runway) / ratio >0.95:1 mini / v60 wiki natural cadence (+4 wikis from v56)

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

**Current state:** 55-wiki corpus shipped (v1 ECC 2026-04-17 → v55 automate-faceless-content 2026-04-26). Vault refactor session 67 (2026-04-27) unblocks v56+ agent builds. v27 diagnostic HIGH bundle item #1 (vault CLAUDE.md refactor) executed via this session.

**Plan:** v56 n8n shipped session 67 (main-loop direct-write fallback). Post-v56 mini-audit executed (2nd CONSERVATIVE-DISCIPLINE; ZERO state transitions). **v27 HIGH bundle 100% COMPLETE session 68** (2026-04-29) — license decision (MIT) + public-release decision (whole-vault NOW GitHub+Anthropic single-repo Q5=G full audit) + publishing strategy (22c AGENTS.md + bilingual README) + skill-lock policy (v1+v2 PUBLIC-ARCHIVED; v2.1+brain-setup+new-project IN-FLUX); 36-session backlog resolved. **Pre-launch execution remaining (~30-60 min):** anti-leak grep + (C) prefix audit + apply skill-lock headers + `gh repo create --public` (recommended name `agentic-ai-second-brain`) + add 11 topics + submit 3 skills to Anthropic skills marketplace.


## Weekly Update

> **Last updated:** _2026-04-27 session 67 — vault refactor day_

- What's working: routine v2.1 + Pattern Library compounds; 19-streak zero-new-active-candidates discipline holding; ratio 0.436:1 unprecedented health preserved 4 cycles
- What's not working: vault state files grew to 400-600KB each → empirically blocked v56 agent builds 3× → infrastructure failure
- What I'm sitting on / need to decide: confirm refactor works (test agent on n8n v56) + decide whether to similarly refactor PATTERN_LIBRARY.md and GOALS.md or wait for next failure
- What I'm feeling pulled toward: ship v56 once refactor verified
- Any deadlines or time-sensitive things: routine v2.1 stale-check windows (#45 / #52 / #72 stale candidates; #57b / #50c / #29-absent-3 N=1 sub-variants synchronized v55/v60)


## My Current Projects & Overviews

**Bulk content moved to `_state/` chapters post-refactor session 67. Index by version range:**

- **v48-v55 (8 most recent — RED tier projects):** `_state/03a-projects-v48-v55.md`
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest 3 active projects (one-line summary; full entries in chapter files):**

- **v56 n8n** (2026-04-27 session 67): T2 N=4 + EXTREME primitive-count 6th in corpus + **bidirectional MCP CORPUS-FIRST AT T2** (Pattern #18 STRONGEST T2 evidence) + Pattern #29 sub-context custom-non-OSI-commercial-restriction N=3 promotion-candidate (omo SUL + GitNexus PolyForm + n8n SUL) + 16 native LLM providers no LiteLLM corpus-broadest + 11 vector stores corpus-broadest + 7-year-mature German GmbH + 1ST STORM BEAR META UNDER STRICT AMENDMENT (Phase 0.9 criterion b PASS legitimate); 20-streak NEW LONGEST; 39th Storm Bear meta; first wiki post-vault-refactor session 67; main-loop direct-write fallback after 5 agent-thrash failures
- **v55 automate-faceless-content** (2026-04-26 session 65): OUTSIDE-SCOPE 10th candidate sub-type content-creation-automation-tutorial; Pattern #29 sub-context 29-absent-5 candidate + Pattern #50 sub-variant 50e candidate; 19-streak; 38th Storm Bear meta GRANDFATHERED (last lightweight-INCLUDE under old criteria; session-66 STRICT amendment applies v56+)
- **v54 gsd-2** (2026-04-26 session 65): T1 N=15 (absolute N=17); Pattern #57 STRONGEST evidence in corpus (4 pi-* packages with verbatim "vendored from pi-mono" machine-readable Pattern #57 sub-variant 57d candidate); Pattern #58 NEW sub-variant 58e successor-repo-not-rename; Pattern #21 SDD un-stale candidate; 18-streak; 37th Storm Bear meta

For full entries see chapter files. For Pattern Library state history see `_state/02-pattern-library-state-history.md`.
