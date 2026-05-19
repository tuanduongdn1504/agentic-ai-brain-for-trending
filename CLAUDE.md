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

**Refactor:** Bulk state moved to `_state/` chapter files. Each chapter sized <35K tokens so agents can read individual chapters without thrashing. Root CLAUDE.md is a shim — ~7KB at the session-67 refactor, ~22KB now after v57-v69 state accumulation (v68 housekeeping 2026-05-14 compacted the Pattern Library state block + relocated the v61-v66 project block to `_state/03c`; v67 wiki 2026-05-18 renamed to v61-v67 + appended v67 entry; v68 zero wiki 2026-05-18 renamed to v61-v68 + appended v68 entry; v69 CloakBrowser wiki 2026-05-18 → 2026-05-19 renamed to v61-v69 + appended v69 entry).

**Chapter index — `_state/` directory:**

| Chapter | Content | Size |
|---|---|---|
| `_state/01-skill-references.md` | 5 numbered skill references (LLM Wiki / Brain-setup / New-project / LLM Wiki Routine v2.1 / Pattern Library) — short stable skill definitions | 5KB |
| `_state/02-pattern-library-state-history.md` | Pattern Library state-block accumulation v21-v55 (every audit + post-wiki strengthening notes). v56-v66 Pattern Library narrative lives in `_patterns/05-recent-additions.md`. | 122KB |
| `_state/03c-projects-v61-v69.md` | Project entries v61-v69 (9 entries: cc-sdd / codex-plugin-cc / andrej-karpathy-skills / claude-seo / claude-code-system-prompts / agentmemory / opencode-antigravity-auth / zero (vercel-labs) / **CloakBrowser (CloakHQ)**) — **NEW at v68 housekeeping 2026-05-14** + **v67 + v68 entries appended 2026-05-18** + **v69 CloakBrowser entry appended 2026-05-19** | ~28KB |
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


## Current Pattern Library state (post-v69 OVERDUE-NATURAL-CADENCE mini-audit 2026-05-19)

**Counts:** **44 confirmed** (was 43; **Pattern #83 PROMOTED at v69 OVERDUE-NATURAL-CADENCE mini-audit**) / **30 active** (was 32; -2 for Pattern #83 promotion-out + Pattern #45 sub-typology 45c absorbed into Pattern #45 confirmed entry) / 1 stale / 9 retired / 6 observation-tracks + 17 observational candidates = **103 full / 78 active-counting**. **Ratio 30:44 = 0.682:1** (buffer 0.268 below the 0.95:1 mini-audit trigger; post-promotion ratio drop of -0.062).

**Latest activity (2026-05-19):** **v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE — LARGEST single audit batch in corpus history (24 items; was 17 at v53)**. **Phase 4b PRIMARY (Phase A1): Pattern #83 Honest-Deficiency-Disclosure Discipline PROMOTED to CONFIRMED** under criterion #1 (≥3-cross-tier, N=5 v64+v65+v67+v68+v69) — **2nd PROMOTION-from-pre-eligible-state in corpus history** after Pattern #19 + #78 at v66 audit; 5 sub-mechanisms registered (83a security / 83b methodology / 83c legal-operational / 83d experimental-status / 83e license-axis-as-disclosure-surface); **multi-surface saturation sub-archetype emergent at N=2** (v67 + v69 both saturate 5+ surfaces). Phase A2: Pattern #45 sub-typology 45c registration CONFIRMED (OBSERVATIONAL N=1; FIRST sub-typology proposal-document promoted through audit channel in corpus history). Phase A3-A5: Pattern #84 84a/84b + Pattern #81 81a/81b + Pattern #18 shared-backend-service sub-archetype (sub-mechanisms A one-backend-many-IDENTITIES + B one-backend-many-CLIENTS) registered. Phase A6: Tier T6 DEFERRED to v75+; Pattern #86 PROVISIONAL T1 sub-archetype #7 retained. Phases B+C: 10 stale-checks + 13 OC dispositions completed; counter-evidence registered against OC-E synchronicity discipline (CloakBrowser README/CHANGELOG patch-count mismatch). **OVERDUE-NATURAL-CADENCE class is NEW 5th formal mini-audit class** (codify at routine v2.3). Prior 2026-05-18 → 2026-05-19: v69 CloakHQ/CloakBrowser wiki ship (CORPUS-FIRST purpose-built-for-stealth subject + anonymous-corporate-author; 12 corpus-firsts). Prior 2026-05-18: v68 vercel-labs/zero wiki ship (NEW Pattern #86 T1 sub-archetype #7) + v67 opencode-antigravity-auth wiki ship (Pattern #83 N=3 PROMOTION-ELIGIBLE proposal-document). Prior 2026-05-14: v66 EARLY-OPERATOR-ELECTED mini-audit + routine v2.2 codified + v66 agentmemory wiki.

**Storm Bear meta-entity streak:** **5 consecutive PASS post-v64-RESET** (v65 STRONGEST + v66 STRONG 4/4 + v67 MODERATE 2/4 + v68 WEAK 1/4 + **v69 WEAK 1/4 — SECOND consecutive WEAK in post-amendment window**). **Strength categorization spectrum continues with WEAK becoming modal category** (2 of 5 in v65-v69 window). 13-instance Phase 0.9 window v57-v69 = 11 PASS / 2 SKIP = **84.6% INCLUDE rate** (slight uptick from v68's 83.3%). v70-v75 evaluation: is WEAK modal-status coincidence or center-of-gravity calibration need?

**Next audit triggers — RESET POST-v69 OVERDUE-NATURAL-CADENCE AUDIT:** active count 30 (back AT trigger; was 32 pre-audit); ratio 0.682 (buffer 0.268 below 0.95:1 mini-trigger; sub-0.95 zone restored); v70 natural cadence (+1 wiki from v69). **v70 audit-not-blocking** post-audit-disposition (was ELEVATED to blocking-priority pre-audit). **v70+ audit agenda (deferred from v69):** Pattern #52 sustained-velocity-test batch (~7 subjects including v69 CloakBrowser sub-threshold-control case) + Pattern #83 sub-taxonomy formalization (83a-e split decision into formal sub-variants) + Tier-Taxonomy Review T6 (v75 if N=2 emerges; v75 downgrade to formal T1 sub-archetype if not) + Pattern #45 sub-typology 45c first-cycle stale-check + ~16 stale-check items per default schedule + Pattern #74/#75 v75-eval / Pattern #77/#79 v70-eval. **Routine v2.3 codification candidates accumulated:** OVERDUE-NATURAL-CADENCE class formalization + sub-typology proposal-document discipline + multi-surface saturation as Pattern #83 sub-archetype + audit batch >20-item splitting + sub-variant-without-top-level-promotion + dual-use subject framing + strength categorization threshold calibration (WEAK modal at v68+v69) + liability-framing axis.

**Where the detail lives:** per-version wiki-ship Pattern Library narrative + audit decisions → `_patterns/05-recent-additions.md` (authoritative). Pattern definitions → `PATTERN_LIBRARY.md` + `_patterns/` chapter files. State-block history v21-v55 → `_state/02-pattern-library-state-history.md`. Project entries → `_state/03a-projects-v48-v60.md` + `_state/03c-projects-v61-v69.md`. v66 audit document → `04 Reviews/(C) 2026-05-14 Pattern Library mini-audit post-v65 ...md`. **v69 OVERDUE-NATURAL-CADENCE audit document** → `04 Reviews/(C) 2026-05-19 Pattern Library mini-audit post-v66-v69 (OVERDUE-NATURAL-CADENCE; LARGEST batch corpus-history; Pattern #83 N=5 PROMOTION + 23 other items).md`. v67 Phase 4b proposal → `03 Projects/opencode-antigravity-auth - Beginner Analysis/01 Analysis/(C) Pattern-83 Honest-Deficiency-Disclosure N=3 promotion proposal.md`. v68 Phase 4b proposal → `03 Projects/zero - Beginner Analysis/01 Analysis/(C) T1-programming-language-as-agent-substrate NEW sub-archetype registration.md`. v69 Phase 4b proposal → `03 Projects/CloakBrowser - Beginner Analysis/01 Analysis/(C) Pattern-45 sub-typology 45c wrapper-OSS + binary-proprietary-with-acceptable-use registration.md`. Pattern #83 confirmed entry → `_patterns/02b-confirmed-patterns-v42-plus.md` § "Promoted at v69 OVERDUE-NATURAL-CADENCE mini-audit (#83)". Routine v2.2 → `05 Skills/llm-wiki-routine-v2.2.md`.
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

**Current state:** **69-wiki corpus shipped + routine v2.2 codified + v66 EARLY-OPERATOR-ELECTED mini-audit + v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE + v66 agentmemory + v67 opencode-antigravity-auth + v68 zero (vercel-labs) + v69 CloakBrowser (CloakHQ) wikis shipped** (v1 ECC 2026-04-17 → **v69 OVERDUE-NATURAL-CADENCE audit 2026-05-19 — LARGEST single audit batch in corpus history at 24 items; Pattern #83 PROMOTED to CONFIRMED at N=5 with 5 sub-mechanisms registered + multi-surface saturation sub-archetype emergent at N=2; Pattern #45 sub-typology 45c REGISTRATION CONFIRMED — FIRST formal sub-typology proposal-document promoted through audit channel in corpus history**). Vault refactor session 67 + public-release session 68 + v57-v64 ships sessions 69-73+ + **pilot v3.2 hireui adversarial-review CANDIDATE-TO-COMPLETED lifecycle session 73 (2026-05-11 → 2026-05-13; FIRST FULLY-COMPLETED pilot in 64-wiki corpus history) + v65 + routine v2.2 + v66 EARLY audit + v66 agentmemory + v67 opencode-antigravity-auth + v68 zero + v69 CloakBrowser + v69 OVERDUE-NATURAL-CADENCE audit session 73++**. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v61 cc-sdd + v63 EARLY MINI-AUDIT + v62 codex-plugin-cc + v63 karpathy-skills + pilot v3.2 hireui + v64 claude-seo + v65 claude-code-system-prompts + routine v2.2 + v66 EARLY-OPERATOR-ELECTED mini-audit shipped session 71+ → 73++** (2026-05-07 to 2026-05-14; **10 deliverables in continuous arc** incl. the v66 agentmemory wiki). **v66 EARLY-OPERATOR-ELECTED mini-audit 2026-05-14 contributes**: **DUAL PRIMARY EXECUTION COMPLETE** — (1) Pattern #19 ecosystem-portfolio-builder PROMOTED N=4 (formal sub-archetype within already-CONFIRMED Pattern #19; 19a/19b/19c/19d sub-mechanisms registered) + (2) Pattern #78 Living-Domain-Standards Tracking ACCELERATED PROMOTION CANDIDATE→CONFIRMED with 78a + 78b sub-mechanisms (FASTEST PROMOTION ARC in 65-wiki corpus history at 2 wikis: v64 registration → v65 N=2 → v66 promotion); plus 5 NEW top-level candidates registered (#80 Tool-Level Adversarial Review N=2 + #81 Manifest-Drift N=1 + #82 Gamified-Curated N=1 + #83 Honest-Deficiency-Disclosure N=2 + #84 Cross-Vendor Ecosystem-Tolerance N=2); 3 within-pattern sub-variants registered (Pattern #21 21b continuous-extraction + Pattern #57 57c-product + Pattern #66 meta-supply-chain-awareness sub-category); 2 Library-vocabulary items formalized (#9 Cross-Pattern Coupled-Design N=5+ corpus-record + #10 1-wiki Rapid-Pattern-Evolution N=2); 1 deferral (Tier-Taxonomy Review T6 → v69); routine v2.2 first-audit validation PASSED no amendments. **State changes (audit)**: 42 → **43 confirmed** / 22 → **26 active** / 0.524 → **0.605 ratio**. **v66 agentmemory wiki then shipped same day** (FIRST wiki under v2.2): PRIMARY = NEW Pattern #85 Platform-Primitive Foundation N=1 + NEW Pattern #18 shared-backend-service sub-archetype + NEW observational candidate AI-Generated-Repo Artifact Contamination + Phase 0.9 4/4 STRICT PASS (FIRST 4/4 in post-amendment window); **post-wiki state 43 confirmed / 27 active / 0.628 ratio**. **Next:** v67/v68 stale-checks per default schedule (v68 adds Pattern #85 + Pattern #18 shared-backend sub-archetype); **v68 natural-cadence trigger** (+2 wikis from v66) OR active count ≥30 (3-candidate runway) OR ratio >0.95:1 mini (buffer 0.322); **v69 audit (~6mo+ window):** Pattern #52 sustained-velocity test (+ agentmemory) + Tier-Taxonomy Review T6 consideration; **routine v2.2 codification candidates RESET** (31 v60-v65 candidates codified at v2.2 2026-05-14; v2.3 target ~v75-v80 natural cadence with ~11 pre-v60 candidates deferred per honest disclosure); **pilot status: 1 pilot COMPLETED + 9 candidates pending** (v66 agentmemory added as highest-relevance pilot candidate — fenced-pilot recommended: scratch project → read-mostly vault → decision gate); Goal #2 progress made via first completed pilot lifecycle + agentmemory pilot-candidacy.


## Weekly Update

> **Last updated:** _2026-05-19 session 73++ — **v69 OVERDUE-NATURAL-CADENCE mini-audit COMPLETE (LARGEST single audit batch in corpus history at 24 items; Pattern #83 PROMOTED to CONFIRMED) + v69 CloakHQ/CloakBrowser wiki shipped (FOURTH wiki under routine v2.2; build spans 2026-05-18 → 2026-05-19).** Phase 4b PRIMARY: Pattern #45 Dual-Licensing NEW sub-typology 45c "Artifact-Scope-Split with Acceptable-Use-Enumeration" registration (FIRST formal sub-typology proposal-document in corpus history; 4 distinguishing mechanisms: two-file artifact-scope split + Acceptable Use enumeration + bounded $100 liability cap + OEM/SaaS B2B carve-out; all 3 sub-typology promotion criteria PASS with HIGH confidence). 12 corpus-firsts including: **CORPUS-FIRST purpose-built-for-stealth subject** (vs prior corpus subjects with stealth-as-feature); **CORPUS-FIRST anonymous-corporate-author** (pm.me + no identity disclosure + dual-use); first two-separate-license-files at repo root; first artifact-scope-split licensing; first explicit Acceptable Use enumeration in license; first bounded fixed-dollar liability cap ($100); first explicit OEM/SaaS commercial-licensing carve-out; first 3-tier signature verification in single README (GPG + GitHub attestation + cosign); first 3-level upstream license attribution in license (Chromium → ungoogled-chromium → CloakHQ); first 28+ releases in 86-day window sustained 0.33 releases/day; first Pattern #45 sub-typology proposal-document at v2.2 era; first sub-typology proposal-document vehicle in corpus history. **HIGH-velocity-NOT-EXTREME 172.7 stars/day at 86 days** (below Pattern #52 >300 threshold — sub-threshold-control test case). +4 NEW observational candidates (OC-G Fork-as-Integration-Strategy + OC-H Anonymous-Corporate-Author for Dual-Use Tools + OC-I Detection-Evasion-As-Product-Axis + OC-J Acceptable-Use Enumeration as Risk-Mitigation Layer) + Pattern #83 N=5 consolidation (5-disclosure-surface saturation in single subject) + Pattern #66 strengthening (3-tier signature verification + 3-level upstream) + Pattern #57 strengthening (3-layer cross-corpus integration depth via browser-use v34 + crawl4ai v29) + Pattern #19 sister observation (corporate-anonymous-product-suite distinct archetype). Storm Bear meta-streak 5 consecutive PASS post-v64-RESET (v69 = SECOND consecutive WEAK 1/4); 13-instance window 84.6% INCLUDE rate; strength categorization WEAK becoming modal (2 of 5 in v65-v69). Routine v2.2 fourth-wiki validation clean + dual-use framing applied + sub-typology proposal-document discipline established. State-architecture: `_state/03c-projects-v61-v68.md` renamed → `_state/03c-projects-v61-v69.md` + v69 entry appended. Pattern Library state: 43 confirmed / 32 active / 0.744 ratio. **v69 audit batch ~24-25 items = NEW LARGEST in corpus history; 3rd-consecutive-wiki-past-active-count-trigger = corpus-record; v70 audit-before-wiki recommendation ELEVATED to blocking-priority.** Earlier 2026-05-18: v68 zero wiki ship (NEW Pattern #86 T1 sub-archetype #7) + v67 opencode-antigravity-auth wiki ship (Pattern #83 N=3 PROMOTION-ELIGIBLE). Earlier 2026-05-14: v68 housekeeping pass + v66 agentmemory wiki + v66 EARLY-OPERATOR-ELECTED mini-audit + routine v2.2 codification._

- What's working: routine v2.2 operational end-to-end — v66 EARLY audit (first audit under v2.2) + v66 agentmemory wiki (first wiki under v2.2) both clean; **DUAL PRIMARY execution clean at v66 audit** (Pattern #19 N=4 + Pattern #78 N=2 both PROMOTED); **Phase 0.9 STRICT produced the FIRST 4/4 PASS in the post-amendment window** at v66 (validates STRICT correctly INCLUDES when all 4 criteria genuinely converge); **DESIGN.md anomaly handled correctly** (verified 3 ways before treating as a finding — "NEVER fabricate" held under tooling pressure); **v68 housekeeping pass clean** — state-architecture restructure + 3 shim/chapter re-narrations (CLAUDE.md compaction / PATTERN_LIBRARY.md re-narration / `_goals/` chapter catch-up) executed without data loss, v60-era detail preserved-and-pointed-to rather than deleted; 11 deliverables in the 2026-05-07→2026-05-14 arc
- What's not working: **`_state/03a-projects-v48-v60.md` is ~177KB / ~45K tokens — over the 35K-per-chapter discipline** (the v68 rename fixed the misleading filename but not the oversize; a split into two chapters is the next housekeeping step); **GOALS.md shim planning sections are still v55/session-68-era** — the v68 pass caught up the `_goals/` data chapters + the shim's factual counts/pointers, but Current Position / Next Milestones / Timeline / Phase narratives / Reflections need a dedicated operator-involved re-narration; **`_state/01-skill-references.md` skill #4 is v2.1/v31-era** (routine description never updated past v31); **ratio at 0.628** (v60-v64 held sub-0.55; forecast back toward sub-0.55 by v70-v72 — see PATTERN_LIBRARY.md honest disclosure); **9 pilot candidates pending, only the one v3.2 deployed**
- What I'm sitting on / need to decide: (a) **commit the v68 housekeeping working state** — the renames + new `03c` + 3 shim/chapter re-narrations + GOALS catch-up are uncommitted; (b) **split `_state/03a-projects-v48-v60.md`** — the oversize chapter is the one remaining state-architecture debt; (c) **GOALS.md shim re-narration** — the planning sections need an operator-involved pass; (d) **execute a pilot** — agentmemory is the top candidate (fenced pilot: scratch project → read-mostly vault → decision gate), or the cc-sdd v61 + codex-plugin-cc v62 comparison-pilot; (e) next wiki build (v67)
- What I'm feeling pulled toward: **commit the housekeeping, then either the agentmemory pilot or the GOALS.md shim re-narration.** The v68 pass cleared the PATTERN_LIBRARY.md + GOALS-chapter + state-architecture drift; what's left is the `03a` split (mechanical) and the GOALS.md shim planning re-narration (needs operator judgment on goals/priorities). The **agentmemory fenced pilot** remains the most directly-vault-relevant subject in the recent corpus — the vault has *already hit* the failure mode agentmemory targets (the 584 KB CLAUDE.md refactor).
- Any deadlines or time-sensitive things: **v68 stale-checks** (~17-item batch — LARGEST in corpus history): Pattern #74 + #75 + #76 + #77 + #78 78a/78b + #79 + #80 + #81 + #82 + #83 **PROMOTION** + #84 **REFINEMENT (84a/84b decision)** + #85 + Pattern #18 shared-backend-service sub-archetype + **NEW from v67 wiki: OC-1 Adversarial-Detection-Tolerant Architecture + OC-2 Issue-As-Enforcement-Signal Pipeline + OC-3 Quota-Arbitrage-Across-Vendor-Internal-Surfaces + Library-vocabulary item #11 Engagement-Deficit-Extreme** + AI-Generated-Repo Artifact Contamination observational; **active candidate count REACHED 30 trigger at v67** (was 27 + 3 new = 30; mini-audit zone threshold met at active-count metric — ratio still 0.698 well below 0.95); **v69 audit (~6mo+ window)** Pattern #52 sustained-velocity test (now incl. agentmemory + opencode-antigravity-auth) + Pattern #83 sub-taxonomy decision (83a security / 83b methodology / 83c legal-operational) + Tier-Taxonomy Review T6; **routine v2.3 codification deferred to ~v75-v80**.


## My Current Projects & Overviews

**Bulk content in `_state/` chapters (post-refactor session 67; restructured at v68 housekeeping 2026-05-14 + extended at v67 + v68 + v69 ships 2026-05-18 → 2026-05-19). Index by version range:**

- **v61-v69 (most recent):** `_state/03c-projects-v61-v69.md` — RENAMED at v69 ship 2026-05-19 from `03c-projects-v61-v68.md`; 9 entries (8 prior + CloakBrowser v69)
- **v48-v60:** `_state/03a-projects-v48-v60.md` — renamed at v68 housekeeping from `03a-projects-v48-v61.md` (range was mislabeled)
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest active projects** — full entries relocated to `_state/` chapter files at v68 housekeeping 2026-05-14 to keep this shim small. Most recent 9 (v61-v69) live in `_state/03c-projects-v61-v69.md`:

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
