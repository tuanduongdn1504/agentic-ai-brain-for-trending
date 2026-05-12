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
| `_state/03a-projects-v48-v61.md` | Project entries v48-v61 (recent ships: gh-aw / aidevops / shannon / ollama / MiroFish / awesome-claude-skills / vercel-labs / oh-my-openagent / learn-coding-agent / gsd-2 / automate-faceless-content / n8n / mattpocock-skills / OpenSpec / AutoGPT / free-claude-code / cc-sdd) — RENAMED at v63 housekeeping (2026-05-07; was `03a-projects-v48-v55.md` semantically out-of-date since v56) | ~140KB |
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


## Current Pattern Library state (post-v63 andrej-karpathy-skills 2026-05-09 — Pattern #52 N=1→N=3 retroactive cross-archetype strengthening)

- **Confirmed:** **42** (was 41; **+1 promotion at v63 EARLY mini-audit**: Pattern #21 SDD Methodology Emergence under criterion #2 structural-unambiguity-at-N=2; **LONGEST stale-to-promotion arc in corpus history at 36 wikis** v25→v63; **1st un-stale-via-independence-test promotion** in corpus)
- **Active candidates:** **19** (was 17; -1 Pattern #21 promoted + 3 NEW top-level candidates registered N=1 stale-flagged: **Pattern #74 EARS-Format Requirements** + **Pattern #75 External-IDE-Methodology Lineage Type** + **Pattern #76 Adversarial Subagent Review Architecture at Framework Level** = net +2)
- **Stale candidates:** **1** (Pattern #52 Extreme-Viral-Velocity OBSERVATIONAL FLAG preserved at ~93 days mattpocock/skills age = barely past 90d threshold but in 90d<x<12mo "preserve flag" band per v60 pre-registered Item 12 decision-criteria; re-evaluate at v66 ~6mo age. **Pattern #21 LEFT stale via promotion at v63 audit.**)
- **Retired:** 9
- **Observation-tracks:** 6
- **Total:** **75 full / 61 active**
- **Ratio:** 19:42 = **0.452:1** — preserves LARGEST sub-0.475 zone in corpus history; buffer **0.498** below 0.95:1 mini-trigger (slight +0.037 from v60 0.415:1 baseline due to 3 NEW candidate registrations; still very healthy + ratio-trigger remains unlikely soon)
- **Streaks post-v63:** ZERO-NEW-ACTIVE-CANDIDATES streak still BROKEN at v63 audit; v62 wiki adds 4 candidates queued for v66 + v63 wiki adds only within-pattern strengthenings (NO new top-level candidates at v63 ship); **Storm Bear meta-entity streak post-v59-RESTART at 4** (v60 PASS + v61 PASS + v62 PASS + **v63 PASS** — 4 consecutive); **8-instance Phase 0.9 post-amendment window**: v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS / **v63 PASS** = **7 PASS / 1 SKIP = 87.5% INCLUDE rate** (criterion (d) STRONGEST instance at v63 — Karpathy corpus-foundation derivative-distillation); **4 mini-audit classes invoked since v54** (CONSERVATIVE-DISCIPLINE × 2 / STRENGTHENING-DOMINANT EXTENDED at v60 / EARLY-OPERATOR-ELECTED at v63)
- **v63 andrej-karpathy-skills wiki ship — CORPUS-RECORD ~1,186 stars/day velocity at observation** (3.2× mattpocock baseline) + **Pattern #52 N=1 → N=3 retroactive cross-archetype strengthening** (mattpocock author-celebrity v57 + codex-plugin-cc corporate-celebrity v62 RETROACTIVE + andrej-karpathy-skills source-celebrity-derivative v63) + **v62 audit gap caught** (codex-plugin-cc ~847 stars/day qualified for Pattern #52 strengthening but v62 wiki did NOT register; retroactive correction at v63 = sister to v61 catch of OpenSpec v58 missing from Pattern #21 evidence list) + **CORPUS-FIRST source-celebrity-derivative-distillation observation** (Pattern #19 a4 NEW sub-type N=1 stale-flagged: solo-engineer distills public-figure observations with explicit attribution) + **Pattern #19 ecosystem-portfolio-builder N=2 strengthening** (gotalab v61 + forrestchang v63) + **Pattern #18 Layer 2 multi-platform-single-skill-manual-sync NEW sub-axis** (4th sub-archetype at Layer 2; Claude Code + Cursor at single-skill scale via parallel manual-sync) + **Pattern #57 57c-strongest instance** (Karpathy = corpus-foundation-individual; LLM Wiki pattern → vault foundation; v63 = direct derivative of corpus-foundation-individual public observations) + **8 corpus-firsts at v63** including Pattern #51 NEUTRAL-with-anti-overengineering pole observation
- **v62 codex-plugin-cc wiki ship — corpus-first cross-vendor cooperation observation** (OpenAI publishes Apache-2.0 plugin FOR Anthropic Claude Code rival platform; unprecedented in 61 prior wikis) + **CORPUS-FIRST 1-wiki counter-evidence cycle** (Pattern #76 registered v63 mini-audit 2026-05-07; codex-plugin-cc counter-evidence v62 2026-05-08 = 1-day/1-wiki gap; FASTEST counter-evidence cycle in corpus history vs prior longest 5-wiki at v29) + **Stratum A vs Stratum B implementation-strata distinction** (cc-sdd architectural role-separation vs codex-plugin-cc prompt-framing variant within same review function — 2 fundamentally distinct mechanism strata) + **Pattern #18 Layer 2 sub-archetype 3rd axis** (cross-vendor-platform-bridge-as-plugin; total Layer 2 = api-protocol-translation-proxy v60 + install-time-skill-format-translator v61 + cross-vendor-bridge v62 = 3 sub-archetypes at N=1 each) + **Pattern #19 corporate-strategic archetype N=2 cross-org structural** (Microsoft + OpenAI distinct organizational entities) + 4 NEW candidate registrations queued for v66 mini-audit (sister to Pattern #76 prompt-framing variant + NEW Pattern #77 Cross-Vendor Cooperative Plugin Publication + NEW Background-Task-Lifecycle-Primitive-Set + Pattern #18 Layer 2 cross-vendor-bridge sub-archetype)
- **Post-v63 audit within-pattern strengthenings (3 — within already-CONFIRMED patterns; do NOT add to active-candidate count):** Pattern #18 Layer 2 install-time-per-platform-skill-format-translator sub-archetype N=1 stale-flagged v66/v71 (cc-sdd v61; distinct from runtime API protocol translation v60 + per-tool format translation v58 — overlap pre-check passed <70%; Pattern #18 refinements stay 11) + Pattern #19 first-mover-authority-without-lineage NEW ecosystem-portfolio-builder sub-type N=1 stale-flagged v66/v71 (gotalab 4-product portfolio cc-sdd + skillport + uxaudit + claude-code-marimo) + Pattern #73 73d Japanese sub-variant N=1 stale-flagged v66/v71 (gotalab solo-Japanese; 4-region distribution now Korean 73a + VN 73b + Pakistani 73c + **Japanese 73d NEW**)
- **v63 audit decisions (13 items): 1 PROMOTION (Pattern #21) + 3 NEW top-level candidates (#74 EARS / #75 External-IDE-lineage / #76 Adversarial-review) + 3 within-pattern strengthenings + 1 fact-verification correction (Pattern #21 evidence list OpenSpec v58 added; closes v58→v60 audit gap caught at v61 wiki ship) + 1 stale-flag preserved (Pattern #52) + 2 stale-check decisions (Pattern #18 cross-tool-skill-format-translator stays stale + Pattern #57 57c-positive-comparison-parallel no-action at v63) + 2 deferrals (Pattern #51 spectrum reformulation to v66 + Process-owning-meta-frameworks OT)**
- **10 corpus-firsts at v61** (most-prolific corpus-first contribution since v18 agency-agents): Kiro IDE external-IDE-methodology lineage / solo-Japanese T1 author / EARS-format explicit reference / File Structure Plan primitive / P-wave parallel-execution annotation / brief.md discovery routing artifact / adversarial subagent review architecture / anti-vibe-with-pragmatic-acknowledgment positioning / agent-platform-format-translation-installer mechanism / architecture-as-foundation explicit acknowledgment
- **Audit triggers RESET post-v63 EARLY MINI-AUDIT.** Next triggers: active candidate count ≥30 (currently 19 — 11-candidate runway PRESERVED at v63 ship) / ratio >0.95:1 mini (currently 0.452:1; buffer 0.498 — ratio-trigger unlikely soon) / **v66 wiki natural cadence (+3 wikis from v63)** with **expanded carry-forward**: 9 from v63 EARLY mini-audit + Pattern #52 N=3 sub-archetype 3-axis (52a/52b/52c) deliberation + Pattern #19 a4 derivative-distillation stale-check + Pattern #19 ecosystem-portfolio-builder N=2 promotion deliberation + Pattern #18 multi-platform-single-skill-manual-sync stale-check + v62 audit gap closure documentation = **expanded ~14 carry-forward items**. **v69 audit (~6mo+ window):** Pattern #52 sustained-velocity test for all 3 N=3 subjects (mattpocock + codex-plugin-cc + karpathy-skills). **Audit results:** `04 Reviews/(C) 2026-05-07 Pattern Library mini-audit post-v61 (early-elected; 1 promotion + 3 NEW candidates + 6 within-pattern decisions).md` — 13-item EARLY-OPERATOR-ELECTED audit; ~75 min duration; **routine v2.2 codification URGENT at v65 window — 25 candidates accumulated v60+v61+v62+v63** (5 new at v63: Phase 0 velocity-screen automation / source-celebrity-derivative-distillation criteria / EXTREME-VIRAL sub-archetype 3-axis discipline / engagement-signal sub-investigation / pre-Phase-6 retroactive-correction-check)

For state-block history v21-v55 see `_state/02-pattern-library-state-history.md`.
For pattern definitions see `PATTERN_LIBRARY.md` (refactored — chapter files in `_patterns/`).
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

**Current state:** 63-wiki corpus shipped (v1 ECC 2026-04-17 → v63 andrej-karpathy-skills 2026-05-09). Vault refactor session 67 + public-release session 68 + v57 ship session 69 + v58 ship session 70 + v59 ship session 71 + v60 ship session 71+ + v61 ship + v63 EARLY mini-audit session 71+ + v62 ship session 72 + v63 andrej-karpathy-skills wiki ship session 73. v27 diagnostic HIGH bundle 100% COMPLETE session 68.

**Plan:** **v61 cc-sdd + v63 EARLY MINI-AUDIT + v62 codex-plugin-cc + v63 andrej-karpathy-skills shipped session 71+ → 73** (2026-05-07 to 2026-05-09; 4 deliverables in continuous arc). **v63 wiki ship resolves user-elected path 'build wiki BEFORE deciding substitution question'**; CORPUS-RECORD ~1,186 stars/day velocity + Pattern #52 N=1 → N=3 retroactive cross-archetype strengthening + v62 audit gap caught + answers user's substitution question (mattpocock + karpathy combo CANNOT replace cc-sdd — different categories: behavioral-overlay vs methodology-harness). **Next:** v66 wiki natural cadence mini-audit (+3 wikis from v63; **expanded ~14-item agenda** incl 9 v63 carry-forward + 5 v63 wiki-ship items); v69 audit (~6mo+) for Pattern #52 sustained-velocity test; **routine v2.2 codification URGENT at v65 window** (25 candidates accumulated v60+v61+v62+v63); **pilot deployment URGENCY FURTHER ESCALATING** — **9 ranked pilots accumulated / 0 deployed** (added andrej-karpathy-skills #3.5 Tier-2); Goal #2 only resolves via actual pilot deployment (cc-sdd #1 + codex-plugin-cc #1.5 comparison-pilot recommended Week 1-2; karpathy-skills Week 3+ stack-layer test).


## Weekly Update

> **Last updated:** _2026-05-09 session 73 — v63 andrej-karpathy-skills wiki shipped (CORPUS-RECORD ~1,186 stars/day velocity 3.2× mattpocock baseline; Pattern #52 N=1→N=3 retroactive cross-archetype strengthening; v62 audit gap caught & corrected; Pattern #19 a4 derivative-distillation NEW sub-type N=1; Pattern #18 Layer 2 multi-platform-single-skill-manual-sync NEW sub-axis N=1; substitution question answered cleanly — combo CANNOT replace cc-sdd, different categories)_

- What's working: routine v2.1 + Pattern Library compounds; **v63 andrej-karpathy-skills wiki shipped cleanly** as derivative-distillation of corpus-foundation-individual Karpathy public observations (Pattern #57 57c-strongest instance); Pattern #52 EXTREME-VIRAL-VELOCITY OBSERVATIONAL FLAG strengthens N=1→N=3 cross-archetype (mattpocock author-celebrity + codex-plugin-cc corporate-celebrity RETROACTIVE + karpathy-skills source-celebrity-derivative); v62 audit gap caught (codex-plugin-cc ~847 stars/day qualified for Pattern #52 but v62 wiki did NOT register) = 2nd consecutive audit-gap-caught-at-next-wiki cycle (sister to v61 catching v58→v60 gap); **8-instance Phase 0.9 post-amendment window 87.5% INCLUDE rate** validates STRICT calibration healthy; 4-consecutive Storm Bear meta-streak post-v60-RESTART; substitution question answered cleanly via category distinction (behavioral-overlay vs methodology-harness)
- What's not working: filename `_state/03a-projects-v48-v55.md` still out-of-date post-v61 (now covers v48-v62+); state-architecture rename deferred to next refactor cycle; **pilot deferral imbalance ESCALATES at v63** — 9 ranked pilots / 0 deployed (added karpathy-skills #3.5 Tier-2); 2-wiki STRONG RECOMMENDATION (pause wiki + execute Tier-1 pilot bundle) NOT executed (wiki-build elected over pilot at v62→v63); Goal #2 progress stalled; routine v2.2 codification candidates accumulated to **25 — codification URGENT at v65 window**
- What I'm sitting on / need to decide: **THREE HIGH-OPERATIONAL pilot candidates ranked Tier-1** (cc-sdd v61 #1 / codex-plugin-cc v62 #1.5 / free-claude-code v60 #2); **karpathy-skills v63 ranks Tier-2 #3.5** (orthogonal behavioral-overlay layer; ~2-min setup; Week 3+ stack-layer test recommended). User's substitution question (mattpocock + karpathy combo to replace cc-sdd) ANSWERED: **NO** — different categories (behavioral-overlay + skills-collection vs methodology-workflow-harness); combo can complement cc-sdd as orthogonal layer, cannot substitute methodology phases (spec/plan/tasks/impl + adversarial review + EARS-format + FSP + P-wave annotation + brief.md routing). Strategic decision: continue pause wiki + execute Tier-1 pilot bundle? OR continue wiki builds with v64 candidate? Routine v2.2 codification 25 candidates = codify at v65 window (was v65-v70; now v65 minimum given urgency)
- What I'm feeling pulled toward: **Tier-1 pilot bundle execution Week 1-2** — cc-sdd v61 + codex-plugin-cc v62 comparison-pilot (apple-to-apple Pattern #76 architectural-vs-prompt-framing empirical evaluation) → karpathy-skills v63 stack-layer test Week 3+ (orthogonal behavioral-overlay) → write-up in `04 Reviews/` → resume wiki builds with fresh pilot evidence informing v66/v69 audit decisions
- Any deadlines or time-sensitive things: **v66 mini-audit natural cadence (+3 wikis from v63) — expanded ~14-item agenda** (9 v63 EARLY mini-audit carry-forward + 5 v63 wiki-ship items: Pattern #52 N=3 sub-archetype 3-axis deliberation / Pattern #19 a4 derivative-distillation stale-check / Pattern #19 ecosystem-portfolio-builder N=2 promotion / Pattern #18 multi-platform-single-skill-manual-sync stale-check / v62 audit gap closure documentation); **v69 audit (~6mo+ window)** for Pattern #52 sustained-velocity test; **routine v2.2 codification URGENT at v65 window** (25 candidates); **Pattern #52 sustained-velocity earliest test** for mattpocock ~early August 2026 / karpathy-skills ~late July 2026 / codex-plugin-cc ~mid October 2026


## My Current Projects & Overviews

**Bulk content moved to `_state/` chapters post-refactor session 67. Index by version range:**

- **v48-v61 (most recent — RED tier projects):** `_state/03a-projects-v48-v61.md` (renamed at v63 housekeeping 2026-05-07)
- **v42-v47 (8 mid-recent):** `_state/03b-projects-v42-v47.md`
- **v30-v39 (10 mid):** `_state/04-projects-v30-v39.md`
- **v1-v29 (28 oldest):** `_state/05-projects-v1-v29.md`

**Latest 3 active projects (one-line summary; full entries in chapter files):**

- **v63 andrej-karpathy-skills** (2026-05-09 session 73): T1 Augmentation single-skill behavioral-guidelines artifact — **CORPUS-RECORD ~1,186 stars/day velocity at observation** (121,227 stars / 102 days; **3.2× mattpocock baseline**); **Pattern #52 EXTREME-VIRAL-VELOCITY N=1 → N=3 retroactive cross-archetype strengthening** (mattpocock author-celebrity v57 + codex-plugin-cc corporate-celebrity v62 RETROACTIVE + andrej-karpathy-skills source-celebrity-derivative v63); **CORPUS-FIRST source-celebrity-derivative-distillation observation** = Pattern #19 a4 NEW sub-type N=1 stale-flagged (solo-engineer forrestchang distills corpus-foundation-individual Karpathy X-tweet observations into installable artifact with explicit attribution); **v62 audit gap caught & corrected** (codex-plugin-cc ~847 stars/day qualified for Pattern #52 but v62 wiki did NOT register; sister to v61 catching v58→v60 gap); **Pattern #19 ecosystem-portfolio-builder N=2 sub-type strengthening** (forrestchang karpathy-skills + Multica = sister to gotalab v61 4-product portfolio); **Pattern #18 Layer 2 multi-platform-single-skill-manual-sync NEW sub-axis N=1** (Claude Code + Cursor at single-skill scale via parallel manual-sync; 4th sub-archetype at Layer 2); **Pattern #57 57c-strongest corpus-foundation-individual inheritance instance** (Karpathy = most-corpus-cited individual; LLM Wiki pattern → Storm Bear vault foundation; v63 = direct derivative); **Storm Bear meta-streak advances to 4 post-v60-RESTART** (Phase 0.9 STRICT 3-of-4 PASS — (a) solo-individual not archetype-peer FAIL but (b) operational-deployable + (c) methodology-influence + (d) STRONGEST corpus-foundation-individual inheritance); **8-instance window 87.5% INCLUDE rate**; **8 corpus-firsts at v63**; **substitution question ANSWERED** (mattpocock + karpathy combo CANNOT replace cc-sdd — behavioral-overlay-collection vs methodology-workflow-harness; combo complements cc-sdd as orthogonal layer); ~85-90 min main-loop direct-write velocity; **Storm Bear pilot ranking #3.5 NEW Tier-2** (after free-claude-code v60 #2 / before n8n v56 Tier-2; Week 3+ stack-layer test); 121,227 stars / forrestchang solo-engineer + Multica founder / Markdown only / MIT / 2 platforms (Claude Code + Cursor) / EN+ZH bilingual / 1 skill `karpathy-guidelines` / 4 principles distilled from Karpathy X tweet; **v66 mini-audit pre-registered with 5 v63-action-items** (Pattern #52 N=3 sub-archetype 3-axis deliberation / Pattern #19 a4 stale-check / Pattern #19 ecosystem-portfolio-builder N=2 promotion / Pattern #18 multi-platform-single-skill-manual-sync stale-check / v62 audit gap closure)
- **v62 codex-plugin-cc** (2026-05-08 session 72): T4 Bridge — **CORPUS-FIRST cross-vendor cooperation observation** (OpenAI publishes Apache-2.0 plugin FOR Anthropic Claude Code rival platform; unprecedented in 61 prior wikis); **CORPUS-FIRST 1-wiki counter-evidence cycle** to Pattern #76 (registered v63 audit 2026-05-07; counter-evidence v62 2026-05-08 = 1-day gap; FASTEST in corpus vs prior 5-wiki); **Stratum A vs Stratum B implementation-strata distinction** (cc-sdd v61 architectural role-separation = Pattern #76 N=1 baseline; codex-plugin-cc v62 prompt-framing variant within same review function = NEW sister candidate); **Pattern #18 Layer 2 3rd sub-archetype cross-vendor-platform-bridge-as-plugin** (post v60 api-protocol-translation-proxy + v61 install-time-skill-format-translator); **Pattern #19 corporate-strategic archetype N=2 cross-org structural** (Microsoft + OpenAI distinct orgs); **Storm Bear meta-streak advances to 3** (3-of-4 Phase 0.9 PASS with (a) corporate-org FAIL but (b)(c)(d) clean — 86% 7-instance INCLUDE rate); 4 NEW candidates queued for v66 mini-audit (sister to #76 + Pattern #77 Cross-Vendor Cooperation + Background-Task-Lifecycle + Pattern #18 Layer 2 sub-archetype); **pilot ranking #1.5 NEW** (post-cc-sdd v61 #1, before free-claude-code v60 #2 — best as comparison-pilot to cc-sdd for Pattern #76 architectural-vs-prompt-framing empirical evaluation); 17.8K stars / 26 commits (extreme density 684 stars-per-commit signaling viral attention) / Apache-2.0 / JavaScript 100% / OpenAI corporate / Claude Code single-host / 7 slash commands organized 3 ways (review + delegate + 4-command background-lifecycle) / 6-primitive plugin architecture (agents + commands + hooks + prompts + schemas + skills) / EN-only / ChatGPT subscription required gate
- **v61 cc-sdd** (2026-05-07 session 71+): T1 — **3rd-4th independent SDD framework** (after v5 GSD + v17 spec-kit + v54 gsd-2 + v58 OpenSpec); **Pattern #21 SDD Methodology Emergence un-stale evidence resolves v60 audit lineage-rejection** (cc-sdd = independent organization gotalab + independent author + independent intellectual lineage Kiro IDE — **corpus-first external-IDE-methodology lineage**); **CORPUS-FIRST solo-Japanese T1 author** (Pattern #55 Japan extension — 4th regional archetype after VN/CN/Korean); **10 corpus-firsts at v61** (most-prolific since v18 agency-agents): Kiro IDE lineage / solo-Japanese / EARS-format / FSP primitive / P-wave annotation / brief.md routing / **adversarial subagent review architecture at framework level** / **anti-vibe-with-pragmatic-acknowledgment positioning** (Pattern #51 nuance — 2nd consecutive narrowing post-v60) / **agent-platform-format-translation-installer** (Pattern #18 Layer 2 sub-archetype N=1 install-time vs v60 runtime + v58 per-tool format) / architecture-as-foundation explicit acknowledgment; **Storm Bear meta-streak advances to 2 post-v60-RESTART** (Phase 0.9 STRICT 3-of-4 PASS — (a) solo-Japanese borderline + (b) operational-deployability strong + (c) methodology-influence-node + (d) PARTIAL via structural-peer); 6-instance window 83% INCLUDE rate; 25-streak NEW LONGEST; **Storm Bear pilot ranking NEW HIGH-OPERATIONAL #3-tier** (joins free-claude-code v60 — orthogonal layers proxy-vs-methodology; both viable simultaneous pilots ~1h setup + 1-week measurement); ~110-125 min main-loop direct-write velocity (above v60's ~60 min compressed-scope but appropriate for Pattern-Library-heavy wiki); **v63 mini-audit pre-registered with 7 v61-action-items** (Pattern #21 un-stale + promotion / Pattern #18 Layer 2 sub-archetype registration / Pattern #51 spectrum reformulation / Pattern #55 East-Asian-meta-archetype consolidation / Pattern #19 ecosystem-portfolio sub-type / 7 routine v2.2 codifications); 3.3K stars / gotalab solo-Japanese / TypeScript 99.6% / MIT / 8 platforms (2 stable + 5 beta + 1 experimental) / 13 languages
- **v60 free-claude-code** (2026-05-07 session 71+): T4 9th archetype **api-protocol-translation-proxy CORPUS-FIRST** (distinct mechanism from prior 8 content-transformation T4 entrants — translates Anthropic Messages API ↔ 6 upstream provider protocols); **Pattern #57 57c polarity sub-variant CORPUS-FIRST positive-comparison-parallel** (tagline "...like OpenClaw"; sister to anti-pattern-foil v57+v58); **cross-pattern coupled-design CORPUS-FIRST at N=4** (P57 polarity × P51 vibe × P19 archetype × tier — library-vocabulary item #9 candidate); **CORPUS-FIRST T4 2-axis sub-taxonomy** (content-transformation N=8 vs protocol-translation N=1); 24-streak; **Storm Bear meta-streak RESTART at 1**; **Pattern #51 anti-vibe pole streak BREAKS** at v60 (2-consecutive-NEUTRAL counter-evidence narrows scope to commercial-educator T1 archetype-correlated); 22c sub-variant NEW corpus-first AGENTS↔CLAUDE explicit-sync-comment-header; Pattern #28 per-Claude-tier-routing NEW sub-variant N=1; 5th consecutive sub-1h direct-write ship; **Storm Bear pilot ranking #3-tier HIGH-OPERATIONAL** (cost-reduction proxy; 4-plugin Claude-Code augmentation stack composability); v60 mini-audit ARMED at natural cadence; 22.1K stars / Alishahryar1 solo-individual / Python 100% / MIT
- **v59 AutoGPT** (2026-05-07 session 71): **T1+T5 multi-tier monorepo CORPUS-FIRST** — 184K stars 2nd-largest pure-product; 7th EXTREME-primitive-count subject; **CORPUS-RARE DOUBLE UN-STALE** Pattern #45 Dual-Licensing 35-wiki un-stale + Pattern #72 PolyForm-Family-License 26-wiki un-stale-with-RENAME (sub-variants 72a Noncommercial + 72b Shield); Pattern #29 sub-context grows N=4 with NEW sub-sub-axis standardized-vs-bespoke-non-OSI emergent; Pattern #19 founder-personal → org-stewardship NEW sub-variant N=2 + first-mover-authority-without-lineage NEW N=1; Pattern #27 community-viral corpus-historical-foundational sub-path (AutoGPT only-qualifier); Pattern #57 BIDIRECTIONAL-ABSENCE OT candidate (REJECTED at v60 audit via 3rd corpus-history fact-verification correction); **0/4 STRICT criteria PASS clean → 1st DISCIPLINED-SKIP Storm Bear meta-entity in 41-streak history**; 23-streak; ~60 min compressed-scope velocity; pilot relevance MEDIUM-LOW pending license-acceptability decision; 184,043 stars / Significant-Gravitas org / MIT + PolyForm-Shield dual / Python+TS hybrid

For full entries see chapter files. For Pattern Library state history see `_state/02-pattern-library-state-history.md`.
