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

**Refactor:** Bulk state moved to `_state/` chapter files. Each chapter sized <35K tokens so agents can read individual chapters without thrashing. Root CLAUDE.md is a shim — ~7KB at the session-67 refactor, ~22KB now after v57-v71 state accumulation (v68 housekeeping 2026-05-14 compacted the Pattern Library state block + relocated the v61-v66 project block to `_state/03c`; v67 wiki 2026-05-18 renamed to v61-v67 + appended v67 entry; v68 zero wiki 2026-05-18 renamed to v61-v68 + appended v68 entry; v69 CloakBrowser wiki 2026-05-18 → 2026-05-19 renamed to v61-v69 + appended v69 entry; v70 codegraph wiki 2026-05-19 renamed to v61-v70 + appended v70 entry; **v71 agents-best-practices wiki 2026-05-19 renamed to v61-v71 + appended v71 entry**).

**Chapter index — `_state/` directory:**

| Chapter | Content | Size |
|---|---|---|
| `_state/01-skill-references.md` | 5 numbered skill references (LLM Wiki / Brain-setup / New-project / LLM Wiki Routine v2.1 / Pattern Library) — short stable skill definitions | 5KB |
| `_state/02-pattern-library-state-history.md` | Pattern Library state-block accumulation v21-v55 (every audit + post-wiki strengthening notes). v56-v66 Pattern Library narrative lives in `_patterns/05-recent-additions.md`. | 122KB |
| `_state/03c-projects-v61-v71.md` | Project entries v61-v71 (11 entries: cc-sdd / codex-plugin-cc / andrej-karpathy-skills / claude-seo / claude-code-system-prompts / agentmemory / opencode-antigravity-auth / zero (vercel-labs) / CloakBrowser (CloakHQ) / codegraph (colbymchenry) / **agents-best-practices (DenisSergeevitch)**) — **NEW at v68 housekeeping 2026-05-14** + **v67 + v68 entries appended 2026-05-18** + **v69 CloakBrowser entry appended 2026-05-19** + **v70 codegraph entry appended 2026-05-19** + **v71 agents-best-practices entry appended 2026-05-19** | ~40KB |
| `_state/03a-projects-v48-v60.md` | Project entries v48-v60 (13 entries: gh-aw / MiroFish / awesome-claude-skills / agent-skills-of-vercel / oh-my-openagent / learn-coding-agent / gsd-2 / automate-faceless-content / n8n / mattpocock-skills / OpenSpec / AutoGPT / free-claude-code) — **RENAMED at v68 housekeeping 2026-05-14** from `03a-projects-v48-v61.md`, which mislabeled the range (cc-sdd v61 was never in it). ⚠️ ~45K tokens — over the 35K-per-chapter discipline; split deferred to a future housekeeping cycle | 177KB |
| `_state/03b-projects-v42-v47.md` | Project entries v42-v47 (8 entries: ruflo / rowboat / magika / browser-use / claude-context / dive-into-llms / DeepTutor / bizos / aidevops) | 67KB |
| `_state/04-projects-v30-v39.md` | Project entries v30-v39 (10 entries: pi-mono / claude-hud / claude-code-best-practice / GitNexus / claude-howto / awesome-mcp-servers / OpenHands / LlamaFactory / system-prompts-leaks / fish-speech) | 140KB |
| `_state/05-projects-v1-v29.md` | Project entries v1-v29 (28 oldest entries: ECC v1 through crawl4ai v29 + foundational patterns) | 123KB |

**Reading discipline for agents:**
- Never read more than 1 chapter file in a single session — context-thrashing risk
- Use `awk` via Bash for surgical line-range extracts when full-chapter not needed
- Pattern Library specific entries: read `PATTERN_LIBRARY.md` chapter files (also refactored, see below)
- For wiki builds: read routine + 1 most-recent project chapter (03c) + WebFetch new subject — should fit in ~50-80K tokens

**Authoritative state pointer:** Chapter files are the authoritative state record. Root CLAUDE.md (this file) is the entry-point shim only. Updates go to chapter files; root only updated when adding new chapters or changing this index.


## Patterns đã verified work / Verified Patterns

See `_state/01-skill-references.md` for full descriptions of:
- **Pattern 1:** LLM Wiki pattern (Karpathy) — proven 2026-04-17
- **Pattern 2:** Brain-setup — proven 2026-04-17, v1 (5-round interview) superseded 2026-05-06 by v2 (4-phase incl. continuous-update + lazy-ADR; cross-port from mattpocock /grill-with-docs v57)
- **Pattern 3:** New project scaffolding (template-duplication + 6-question interview) — proven 2026-04-17
- **Pattern 4:** LLM Wiki Routine (autonomous orchestration) — proven 2026-04-18; v2.1 codified 2026-04-22; **v2.2 codified 2026-05-14 (current; supersedes v2.1)**. ⚠️ `_state/01-skill-references.md` skill #4 detail is still v2.1/v31-era — pending a content refresh
- **Pattern 5:** Pattern Library (cross-wiki synthesis) — codified 2026-04-19, current state in PATTERN_LIBRARY.md + history in `_state/02-pattern-library-state-history.md`

**Skill files at `05 Skills/`:** 9 skills total — see `05 Skills/SKILL_LOCK_POLICY.md` table for status + rationale.
- 6 IN-FLUX active
- 3 PUBLIC-ARCHIVED historical


## Current Pattern Library state (post-v71 agents-best-practices wiki 2026-05-19)

**Counts:** **44 confirmed** / **30 active** / 1 stale / 9 retired / 6 observation-tracks + **22 observational candidates** (was 21 pre-v71; +1 from v71 agents-best-practices: OC-O Agentic-Harness-Execution-Separation) = **107 full / 78 active-counting**. **Ratio 30:44 = 0.682:1 UNCHANGED** (within-pattern strengthening only at v71; no top-level state transitions).

**Latest activity (2026-05-19 session 73++):** **v71 agents-best-practices wiki shipped (SIXTH WIKI UNDER ROUTINE v2.2)** — DenisSergeevitch/agents-best-practices T1 Assistant Skill; provider-agnostic agentic framework synthesizing Anthropic + OpenAI patterns equally (821 stars at 4 days = 205.25 stars/day HIGH-velocity-NOT-EXTREME; Markdown-only; MIT; 15-reference-file architecture). **PRIMARY: Pattern #84 Cross-Vendor Ecosystem-Tolerance N=3 PROMOTION-ELIGIBLE + sub-typology 84c "Provider-Agnostic-By-Design" proposed** (84a v62 + 84b v65 + **84c v71** = all promotion criteria PASS; meta-archetype shift ecosystem-norm → author-design-choice; PROMOTE at v72+ formal audit). **NEW OC-O Agentic-Harness-Execution-Separation** (7-invariant loop; "model proposes, harness disposes" formalization). Pattern #78 N=3 STRONGEST 78a (triple-standard OWASP+NIST+MCP-spec + dual-vendor Anthropic 5 guides + OpenAI 5 guides). Pattern #83 83b within-pattern (harness-boundary-deficiency-disclosure). Pattern #21 within-pattern (8 principles + 7 loop invariants + L0-L4 autonomy levels + draft-commit pattern). Pattern #66 66d within-pattern (malicious skill packages threat; first skill-package-layer supply-chain evidence). 8 corpus-firsts at v71 (FIRST execution-separation formalization / FIRST 15-reference-file reference library / FIRST L0-L4 autonomy-level taxonomy / FIRST provider-agnostic dual-vendor unified framework / FIRST 15-category security threat model / FIRST draft-commit pattern formalization / FIRST OWASP+NIST+MCP-spec triple-standard / FIRST 12-tier context architecture taxonomy). Storm Bear MODERATE 2/4 (b+c). Prior 2026-05-19: **v70 codegraph wiki shipped (FIFTH WIKI UNDER ROUTINE v2.2)** — colbymchenry/codegraph T2 Service; **PRIMARY: Pattern #18 sub-mechanism B N=3 + protocol-variants formalization** (FIRST sub-mechanism formalization proposal-document = NEW 6th Phase 4b vehicle; FIRST 4-layer Pattern hierarchy); +4 OC (OC-K/L/M/N). Prior 2026-05-19: **v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE (24 items; Pattern #83 PROMOTED)**. Prior 2026-05-18→19: v69 CloakBrowser wiki. Prior 2026-05-18: v68 zero + v67 opencode ships. Prior 2026-05-14: v66 EARLY-OPERATOR-ELECTED mini-audit + routine v2.2 + v66 agentmemory wiki.

**Storm Bear meta-entity streak:** **7 consecutive PASS post-v64-RESET** (v65 STRONGEST + v66 STRONG 4/4 + v67 MODERATE 2/4 + v68 WEAK 1/4 + v69 WEAK 1/4 + v70 MODERATE 2/4 + **v71 MODERATE 2/4 — extends streak to 7; two consecutive MODERATEs**). **Strength categorization v65-v71: STRONGEST × 1 + STRONG × 1 + MODERATE × 3 + WEAK × 2** (MODERATE now modal-status). 15-instance Phase 0.9 post-amendment window v57-v71 = 13 PASS / 2 SKIP = **86.7% INCLUDE rate** (uptick from v70's 85.7%). v71 agents-best-practices contributes MODERATE 2/4 INCLUDE: (b) PASS operational-tool-for-vault (directly installable as Claude Code skill; hireui-harness agentic-harness design work) + (c) PASS methodology-influence (7-invariant loop + context tiers + planning mode + autonomy levels inform routine v2.2 design); (a) FAIL solo-eastern-european developer / (d) FAIL no explicit corpus-subject URL citation.

**Next audit triggers — v71 within-pattern strengthening only; trigger state unchanged:** active count 30 (maintained at trigger-threshold 5th-consecutive-wiki = corpus-record-condition EXTENDED); ratio 0.682 (buffer 0.268 below 0.95:1 mini-trigger; sub-0.95 zone preserved); v72 natural cadence (+1 wiki from v71). **v72 audit batch additions from v71:** Pattern #84 N=3 PROMOTION to CONFIRMED + sub-typology 84c formal registration + 84a/84b retroactive registration + Pattern #66 sub-mechanism 66d formal registration + OC-O stale-check + batch deferred from v70 (Pattern #18 sub-mechanism B promotion decision + B1/B2/B3 protocol-variants + OC-K/L/N stale-checks + OC-M N=3 evaluation + OC-E E1/E2 decision + Pattern #52 velocity-test batch + Pattern #45 45c stale-check + Tier-Taxonomy Review T6 + ~16 default stale-checks). **Routine v2.3 codification candidates accumulated (post-v71; unchanged from v70):** OVERDUE-NATURAL-CADENCE class formalization + sub-typology proposal-document discipline + NEW 6th Phase 4b vehicle (sub-mechanism formalization) + n-layer pattern hierarchy support (4-layer at v70) + protocol-variants-within-sub-mechanism as criterion 4 evidence + multi-surface saturation as Pattern #83 sub-archetype + audit batch >20-item splitting + sub-variant-without-top-level-promotion + dual-use subject framing + strength categorization threshold calibration + liability-framing axis.

**Where the detail lives:** per-version wiki-ship Pattern Library narrative + audit decisions → `_patterns/05-recent-additions.md` (authoritative; v71 strengthening block appended 2026-05-19). Pattern definitions → `PATTERN_LIBRARY.md` + `_patterns/` chapter files. State-block history v21-v55 → `_state/02-pattern-library-state-history.md`. Project entries → `_state/03a-projects-v48-v60.md` + `_state/03c-projects-v61-v71.md`. v66 audit document → `04 Reviews/(C) 2026-05-14 Pattern Library mini-audit post-v65 ...md`. **v69 OVERDUE-NATURAL-CADENCE audit document** → `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE; LARGEST batch corpus-history; Pattern #83 N=5 PROMOTION + 23 other items).md`. v67 Phase 4b proposal → `03 Projects/opencode-antigravity-auth - Beginner Analysis/01 Analysis/(C) Pattern-83 Honest-Deficiency-Disclosure N=3 promotion proposal.md`. v68 Phase 4b proposal → `03 Projects/zero - Beginner Analysis/01 Analysis/(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md`. v69 Phase 4b proposal → `03 Projects/CloakBrowser - Beginner Analysis/01 Analysis/(C) Pattern-45 sub-typology 45c wrapper-OSS + binary-proprietary-with-acceptable-use registration.md`. v70 Phase 4b proposal → `03 Projects/codegraph - Beginner Analysis/01 Analysis/(C) Pattern-18 sub-mechanism B one-binary-many-CLIENTS N=3 protocol-variants formalization.md`. **v71 Phase 4b proposal (Pattern #84 N=3 + sub-typology 84c)** → `03 Projects/agents-best-practices - Beginner Analysis/01 Analysis/(C) Pattern-84-cross-vendor-ecosystem-tolerance-N3-promotion-evaluation.md`. Pattern #83 confirmed entry → `_patterns/02b-confirmed-patterns-v42-plus.md` § "Promoted at v69 OVERDUE-NATURAL-CADENCE mini-audit (#83)". Routine v2.2 → `05 Skills/llm-wiki-routine-v2.2.md`.
For consolidated pilot ranking see `_state/pilot-ranking-2026-05-07.md` (post-v63 housekeeping; replaces scattered mentions).


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

**Current state:** **71-wiki corpus shipped + routine v2.2 codified + v66 EARLY-OPERATOR-ELECTED mini-audit + v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE + v66 agentmemory + v67 opencode-antigravity-auth + v68 zero (vercel-labs) + v69 CloakBrowser (CloakHQ) + v70 codegraph (colbymchenry) + v71 agents-best-practices (DenisSergeevitch) wikis shipped** (v1 ECC 2026-04-17 → **v71 agents-best-practices 2026-05-19 — SIXTH WIKI UNDER ROUTINE v2.2; Pattern #84 Cross-Vendor Ecosystem-Tolerance N=3 PROMOTION-ELIGIBLE + sub-typology 84c "Provider-Agnostic-By-Design" proposed; NEW OC-O Agentic-Harness-Execution-Separation; Pattern #78 N=3 STRONGEST 78a; 8 corpus-firsts; MODERATE-RELEVANCE vault pilot candidate**). Vault refactor session 67 + public-release session 68 + v57-v64 ships sessions 69-73+ + **pilot v3.2 hireui adversarial-review CANDIDATE-TO-COMPLETED lifecycle session 73 (2026-05-11 → 2026-05-13; FIRST FULLY-COMPLETED pilot in 64-wiki corpus history) + v65 + routine v2.2 + v66 EARLY audit + v66 agentmemory + v67 opencode-antigravity-auth + v68 zero + v69 CloakBrowser + v69 OVERDUE-NATURAL-CADENCE audit + v70 codegraph session 73++**. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v61 cc-sdd + v63 EARLY MINI-AUDIT + v62 codex-plugin-cc + v63 karpathy-skills + pilot v3.2 hireui + v64 claude-seo + v65 claude-code-system-prompts + routine v2.2 + v66 EARLY-OPERATOR-ELECTED mini-audit shipped session 71+ → 73++** (2026-05-07 to 2026-05-14; **10 deliverables in continuous arc** incl. the v66 agentmemory wiki). **v66 EARLY-OPERATOR-ELECTED mini-audit 2026-05-14 contributes**: **DUAL PRIMARY EXECUTION COMPLETE** — (1) Pattern #19 ecosystem-portfolio-builder PROMOTED N=4 (formal sub-archetype within already-CONFIRMED Pattern #19; 19a/19b/19c/19d sub-mechanisms registered) + (2) Pattern #78 Living-Domain-Standards Tracking ACCELERATED PROMOTION CANDIDATE→CONFIRMED with 78a + 78b sub-mechanisms (FASTEST PROMOTION ARC in 65-wiki corpus history at 2 wikis: v64 registration → v65 N=2 → v66 promotion); plus 5 NEW top-level candidates registered (#80 Tool-Level Adversarial Review N=2 + #81 Manifest-Drift N=1 + #82 Gamified-Curated N=1 + #83 Honest-Deficiency-Disclosure N=2 + #84 Cross-Vendor Ecosystem-Tolerance N=2); 3 within-pattern sub-variants registered (Pattern #21 21b continuous-extraction + Pattern #57 57c-product + Pattern #66 meta-supply-chain-awareness sub-category); 2 Library-vocabulary items formalized (#9 Cross-Pattern Coupled-Design N=5+ corpus-record + #10 1-wiki Rapid-Pattern-Evolution N=2); 1 deferral (Tier-Taxonomy Review T6 → v69); routine v2.2 first-audit validation PASSED no amendments. **State changes (audit)**: 42 → **43 confirmed** / 22 → **26 active** / 0.524 → **0.605 ratio**. **v66 agentmemory wiki then shipped same day** (FIRST wiki under v2.2): PRIMARY = NEW Pattern #85 Platform-Primitive Foundation N=1 + NEW Pattern #18 shared-backend-service sub-archetype + NEW observational candidate AI-Generated-Repo Artifact Contamination + Phase 0.9 4/4 STRICT PASS (FIRST 4/4 in post-amendment window); **post-wiki state 43 confirmed / 27 active / 0.628 ratio**. **Next:** v67/v68 stale-checks per default schedule (v68 adds Pattern #85 + Pattern #18 shared-backend sub-archetype); **v68 natural-cadence trigger** (+2 wikis from v66) OR active count ≥30 (3-candidate runway) OR ratio >0.95:1 mini (buffer 0.322); **v69 audit (~6mo+ window):** Pattern #52 sustained-velocity test (+ agentmemory) + Tier-Taxonomy Review T6 consideration; **routine v2.2 codification candidates RESET** (31 v60-v65 candidates codified at v2.2 2026-05-14; v2.3 target ~v75-v80 natural cadence with ~11 pre-v60 candidates deferred per honest disclosure); **pilot status: 1 pilot COMPLETED + 9 candidates pending** (v66 agentmemory added as highest-relevance pilot candidate — fenced-pilot recommended: scratch project → read-mostly vault → decision gate); Goal #2 progress made via first completed pilot lifecycle + agentmemory pilot-candidacy.


## Weekly Update

> **Last updated:** _2026-05-19 session 73++ — **v71 agents-best-practices wiki shipped (SIXTH WIKI UNDER ROUTINE v2.2)**. Phase 4b PRIMARY: **Pattern #84 Cross-Vendor Ecosystem-Tolerance N=3 PROMOTION-ELIGIBLE + sub-typology 84c "Provider-Agnostic-By-Design" proposed** (84a v62 Tool-tolerance + 84b v65 Usage-enforcement + 84c v71 Provider-Agnostic-By-Design; meta-archetype shift ecosystem-norm → author-design-choice; all promotion criteria PASS HIGH confidence; PROMOTE at v72+ formal audit). **NEW OC-O Agentic-Harness-Execution-Separation** registered (7-invariant agentic loop; "model proposes, harness disposes"). Pattern #78 N=3 STRONGEST 78a (triple-standard OWASP+NIST+MCP-spec + dual-vendor Anthropic 5 guides + OpenAI 5 guides). Pattern #83 83b within-pattern (harness-boundary-deficiency-disclosure; "prompt-only safety is insufficient"). Pattern #21 within-pattern (draft-commit pattern formalization — corpus-first). Pattern #66 66d within-pattern (malicious skill packages — first skill-package-layer supply-chain evidence). 8 corpus-firsts at v71. Storm Bear MODERATE 2/4 (b+c); streak extended to 7 consecutive PASS; 15-instance window 86.7% INCLUDE rate; MODERATE now modal-status (3/7 v65-v71). Routine v2.2 sixth-wiki validation clean. State-architecture: `_state/03c-projects-v61-v70.md` deleted → `_state/03c-projects-v61-v71.md` + v71 entry appended. Pattern Library state: 44 confirmed / 30 active / 0.682 ratio UNCHANGED (within-pattern strengthening only); OC count 21 → 22. Active count 30 maintained at trigger-threshold 5th-consecutive-wiki = corpus-record-condition EXTENDED. Earlier 2026-05-19: **v70 codegraph wiki shipped (FIFTH WIKI UNDER ROUTINE v2.2; FIRST sub-mechanism formalization proposal-document = NEW 6th Phase 4b vehicle; FIRST 4-layer Pattern hierarchy; +4 OC: OC-K/L/M/N)** + **v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE (24 items; Pattern #83 PROMOTED)** + v69 CloakBrowser wiki. Earlier 2026-05-18: v68 zero + v67 opencode ships. Earlier 2026-05-14: v66 EARLY-OPERATOR-ELECTED mini-audit + routine v2.2 + v66 agentmemory wiki._

- What's working: routine v2.2 operational end-to-end — **6 wikis shipped under v2.2 with no amendments needed**; v66 EARLY audit + v69 OVERDUE-NATURAL-CADENCE audit both executed cleanly (LARGEST audit batch in corpus history at v69 = 24 items disposed); **v71 agents-best-practices + v70 codegraph both produced clean Phase 4b promotion vehicles** without disrupting top-level state (44 confirmed / 30 active / 0.682 unchanged across both); **Phase 0.9 STRICT continues to discriminate empirically** — strength spectrum diversity maintained (STRONGEST / STRONG / MODERATE ×3 / WEAK ×2 over v65-v71); **Pattern #84 promotion-eligible after 3 wikis = sub-5-wiki promotion arc** (joins Pattern #78's FASTEST-PROMOTION record)
- What's not working: **`_state/03a-projects-v48-v60.md` is ~177KB / ~45K tokens — over the 35K-per-chapter discipline** (split deferred to housekeeping cycle); **GOALS.md shim planning sections are still v55/session-68-era** (need operator-involved re-narration); **`_state/01-skill-references.md` skill #4 is v2.1/v31-era** (routine description never updated); **active count 30 maintained at trigger-threshold 5th-consecutive-wiki** (corpus-record-condition; audit-velocity-control test case extended for 2nd consecutive wiki without audit); **9+ pilot candidates pending, only v3.2 deployed**
- What I'm sitting on / need to decide: (a) **commit the v70+v71 vault-sync working state** — uncommitted; (b) **execute pilots** — codegraph FIRST (read-only, reversible, lowest-risk), then agents-best-practices skill install (zero infrastructure, additive-only), then agentmemory THIRD; (c) **split `_state/03a-projects-v48-v60.md`** — oversize chapter state-architecture debt; (d) **GOALS.md shim re-narration** — planning sections need operator-involved pass; (e) next wiki build (v72) — **v72 audit is recommended BEFORE next wiki** (Pattern #84 promotion-eligible + active count at 5th-consecutive-trigger)
- What I'm feeling pulled toward: **commit vault-sync state, then run v72 audit before next wiki build.** Pattern #84 is promotion-eligible and the active-count has been at the trigger-threshold for 5 consecutive wikis. The audit batch is clearly defined (Pattern #84 promotion + sub-typology 84c formal registration + Pattern #66 66d sub-mechanism + all deferred v70 items).
- Any deadlines or time-sensitive things: **v72 audit batch** (from v71 + deferred v70 items): Pattern #84 PROMOTE to CONFIRMED + sub-typology 84c formal registration + Pattern #66 66d sub-mechanism registration + OC-O stale-check + Pattern #18 sub-mechanism B promotion decision (N=3 across B1+B2) + B1/B2/B3 formal registration + OC-K/L/N stale-checks + OC-M N=3 evaluation + OC-E E1/E2 decision + Pattern #52 velocity-test batch (~8 subjects) + Pattern #45 45c stale-check + Tier-Taxonomy Review T6 (ELEVATED, 2nd deferral) + ~16 default stale-checks. **Active count 30 at 5th-consecutive-trigger** — strongest audit-urgency signal in corpus history. **Routine v2.3 codification candidates post-v71 (unchanged from v70)**: 6th Phase 4b vehicle + n-layer hierarchy + protocol-variants as criterion 4 evidence + OVERDUE-NATURAL-CADENCE class + sub-typology discipline + multi-surface saturation + audit batch >20 splitting + dual-use framing + strength calibration + liability-framing axis.


## My Current Projects & Overviews

**Bulk content in `_state/` chapters (post-refactor session 67; restructured at v68 housekeeping 2026-05-14 + extended at v67 + v68 + v69 + v70 + v71 ships 2026-05-18 → 2026-05-19). Index by version range:**

- **v61-v71 (most recent):** `_state/03c-projects-v61-v71.md` — RENAMED at v71 ship 2026-05-19 from `03c-projects-v61-v70.md`; 11 entries (10 prior + agents-best-practices v71)
- **v48-v60:** `_state/03a-projects-v48-v60.md` — renamed at v68 housekeeping from `03a-projects-v48-v61.md` (range was mislabeled)
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest active projects** — full entries relocated to `_state/` chapter files at v68 housekeeping 2026-05-14 to keep this shim small. Most recent 11 (v61-v71) live in `_state/03c-projects-v61-v71.md`:

- **v71 agents-best-practices (DenisSergeevitch)** — T1 Assistant Skill; provider-agnostic agentic framework (8 principles + 7 loop invariants + L0-L4 autonomy levels + 15-reference-file architecture); PRIMARY = Pattern #84 N=3 PROMOTION-ELIGIBLE + sub-typology 84c "Provider-Agnostic-By-Design" proposed; NEW OC-O Agentic-Harness-Execution-Separation; Pattern #78 N=3 STRONGEST 78a; 8 corpus-firsts; sixth wiki under routine v2.2; **MODERATE-RELEVANCE vault pilot candidate** (skill install zero-risk; `skills attach DenisSergeevitch/agents-best-practices`)
- **v70 codegraph (colbymchenry)** — T2 Service; pre-indexed code knowledge graph for AI coding agents (MCP server + multi-agent installer); PRIMARY = Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" N=3 strengthening + protocol-variants formalization (B1 MCP variant N=2 + B2 CDP variant N=1) — **FIRST sub-mechanism formalization proposal-document in corpus history = NEW 6th Phase 4b promotion vehicle**; FIRST 4-layer Pattern hierarchy formalized; 6 corpus-firsts; fifth wiki under routine v2.2; **HIGH-RELEVANCE vault pilot candidate LOWER-risk than agentmemory** (read-only indexing, no vault state mutation, reversible via `codegraph uninit`)
- **v69 CloakBrowser (CloakHQ)** — T2 Service; CORPUS-FIRST purpose-built-for-stealth subject + CORPUS-FIRST anonymous-corporate-author; PRIMARY = Pattern #45 NEW sub-typology 45c "Artifact-Scope-Split with Acceptable-Use-Enumeration" (FIRST formal sub-typology proposal-document in corpus history); HIGH-velocity-NOT-EXTREME 172.7 stars/day at 86 days; 12 corpus-firsts; fourth wiki under routine v2.2
- **v68 zero (vercel-labs)** — PROVISIONAL T1 NEW sub-archetype #7 "programming-language-as-agent-substrate"; FIRST programming-language subject in corpus; PRIMARY = Pattern #86 N=1 registration + Pattern #87 Skill-As-Binary-Bootstrap; CORPUS 2nd-HIGHEST velocity 1,050 stars/day; 12 corpus-firsts; third wiki under routine v2.2
- **v67 opencode-antigravity-auth** — T4 Bridge OAuth-credential-plugin (Opencode ↔ Google Antigravity); PRIMARY = Pattern #83 Honest-Deficiency-Disclosure N=3 PROMOTION-ELIGIBLE; 9 corpus-firsts including CORPUS-RECORD-LOW fork_ratio 0.0001; second wiki under routine v2.2
- **v66 agentmemory** — T2 Service; first dedicated agent-memory-system in corpus; PRIMARY = NEW Pattern #85 Platform-Primitive Foundation; first wiki built under routine v2.2
- **v65 claude-code-system-prompts** — T1 reverse-engineering-reference-archive; DUAL PRIMARY (Pattern #78 N=2 + Storm Bear corpus-recursive)
- **v64 claude-seo** — T1 domain-vertical-skill-collection; PRIMARY = Pattern #19 N=3 promotion-eligible
- **v63 andrej-karpathy-skills** — T1 single-artifact; CORPUS-RECORD ~1,186 stars/day; Pattern #52 N=3
- **v62 codex-plugin-cc** — T4 Bridge; corpus-first cross-vendor cooperation
- **v61 cc-sdd** — T1 SDD framework; Pattern #21 un-stale; 10 corpus-firsts

Older ranges per the version-range index above. Pattern Library per-wiki narrative → `_patterns/05-recent-additions.md`.
