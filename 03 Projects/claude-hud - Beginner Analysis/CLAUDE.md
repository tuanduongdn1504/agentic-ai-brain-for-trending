# claude-hud - Beginner Analysis — Claude Context

**Project type:** LLM Wiki v35 (v2.1 routine, 4th v2.1-era execution)
**Subject:** `jarrodwatts/claude-hud`
**Tagline:** *"A Claude Code plugin that shows what's happening — context usage, active tools, running agents, and todo progress. Always visible below your input."*
**Status:** v1 in progress (2026-04-23)
**Operator:** Storm Bear (Cvtot, VN Scrum coach / software developer)

---

## Phase 0 probe (2026-04-23)

| Field | Value |
|-------|-------|
| Repo | `jarrodwatts/claude-hud` |
| Stars | **20,389** (~#15 in corpus) |
| Forks | 906 (4.4%) |
| Watchers (subscribers) | 32 |
| Open issues | **1** (very low — cleanly managed) |
| License | **MIT** |
| Primary lang | **TypeScript** (src/) + JavaScript (dist/) |
| Default branch | `main` |
| Created | 2026-01-02 (~3.7 months ago — **2nd-youngest in corpus** after awesome-design-md v25 at 3 weeks) |
| Pushed | 2026-04-22 (active, 1 day before wiki) |
| Latest version | v0.1.0 (package.json) / v0.0.12 (CHANGELOG last released 2026-04-04) |
| Topics | anthropic, claude, claude-code, cli, plugin, statusline, typescript |
| Size | 2,065 KB |
| Homepage | null (no dedicated site; blog jarrodwatts.com is author's, not project) |
| README langs | **EN + zh** (中文文档) — 2 languages |

## Author

- **Jarrod Watts** (jarrodwatts)
- **Sydney, Australia** — **1st Australian-authored framework in corpus** (observation, not registered as separate regional candidate per consolidation-forward discipline)
- Blog: jarrodwatts.com
- Twitter: @jarrodwatts
- GitHub since 2018-01-21 (~8 years)
- **144 public repos**, 1,075 followers, 28 following
- Company: none listed
- Bio: none (brand/behavior self-documents via blog + repos)

**Contributors observed in CHANGELOG credits:**
- @Tsopic — config system, layouts (#32)
- @melon-hub — Usage API, configure skill (#34)
- @r-firpo, @yansircc, @StephenJoshii — autocompact ideas (#30/#43/#49)

Effectively solo maintainer with PR contribution acknowledgements.

## 12-axis v2.1 classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant — 12TH T1 ENTRANT, but NEW SUB-CLASSIFICATION (display-layer plugin)** |
| **Archetype** | **Narrow-scope display-layer plugin (NEW T1 sub-variant)** — distinct from framework/methodology/skill-library mainstream of prior 11 T1 entrants |
| **Scale tier** | Medium (20K; ~5,500 stars/month over 3.7 months ≈ fast velocity, under awesome-design-md v25 but above claude-howto v32 early trajectory) |
| **Primary lang** | TypeScript (compiled to JS via tsc; `dist/` committed by CI post-merge) |
| **Packaging** | **Claude Code native `/plugin marketplace` — corpus-first at scale** (no npm publish; marketplace manifest only) |
| **Origin story** | Individual-author (Jarrod Watts) + rapid community contribution (2 named PR contributors + 3 idea contributors in CHANGELOG) |
| **Methodology** | No methodology — pure utility plugin; **scope-narrow** (statusline only) |
| **Governance** | **Medium-heavy** (CODE_OF_CONDUCT + CONTRIBUTING + SECURITY + SUPPORT + MAINTAINERS + TESTING + RELEASING — 7 governance files; unusual governance density for 3-month-old solo project) |
| **Agent/skill count** | 2 slash commands (`/claude-hud:setup` + `/claude-hud:configure`); 0 skills; 0 agents — single-purpose utility |
| **i18n** | EN + zh (2 languages; labels opt-in via `language: "zh"` config) |
| **Intellectual influence** | No explicit lineage cited. Uses Claude Code native statusline API (Anthropic-published primitive). |
| **Agent platforms** | **Claude Code only** (by design — native plugin) — NARROWEST platform count in corpus |

## Primitive-count probe (v2.1 Phase 0 informal discipline — INAUGURAL USE)

Per v2.1 Phase 5 informal discipline introduced session 41, counting distinct primitives from 4 signals:

| Signal | Source | Count |
|--------|--------|-------|
| 1. README TOC top-level sections | README.md | **~11** (Install / What is / What You See / How It Works / Configuration / Options / Usage Limits / Example Config / Display Examples / Troubleshooting / Requirements / Development / License / Star History) |
| 2. Repo folder structure top-level | GitHub contents | **6 dirs + 16 files** (.claude-plugin / .github / commands / dist / src / tests) |
| 3. CLAUDE.md / CLAUDE.README.md declared components | CLAUDE.README.md `<file_structure>` | **~16 source modules** (stdin / transcript / config-reader / config / git / types + 10 render/ modules) |
| 4. Slash commands exposed | commands/ dir | **2** (setup, configure) |
| 5. HUD output lines (product-level primitives) | README | **4 render lines** (project / context+usage merged / tools / agents / todos — line 2 merges context+usage; optional tools/agents/todos) |
| 6. Config options | README Options table | **~38 `display.*` + layout options** |

**Probed primitive-count summary:**
- **Product-level primitives:** ~4-5 (render lines)
- **User-level primitives:** 2 slash commands + ~38 config options
- **Source-level primitives:** ~16 modules

**Fits 4-entity format cleanly:** **YES** — the product is structurally narrow (single output surface = statusline). Entities distribute naturally as: (1) Core product (statusline renderer + data flow) / (2) Plugin distribution + marketplace mechanism / (3) Jarrod Watts author / (4) Storm Bear meta.

**Follow-up deep-dive wikis recommended:** None. Primitive-count is already well-contained. No compression concerns at 4-entity format.

**Operator decision recommended:** Accept as-is; no sequential deep-dive needed.

**Primitive-count flagging outcome:** **GREEN — 4-entity format is a natural fit.** This is the inaugural run of the v2.1 primitive-count check protocol, and on this (genuinely narrow) target the discipline correctly flags "no compression risk."

## v2.1 Phase 0.5 pattern pre-check results

### Un-stale check

- **#55 Korean Regional Archetype T1** (STALE) — Australian ≠ Korean, does NOT un-stale
- **#45 Dual-Licensing / #46 Duo-Founder / #52 Extreme-Viral-Velocity** — no evidence (single MIT, solo, fast-but-not-extreme growth)
- **Retired revivals** — #14 / #16 / #23 / #25 / #49 / #60 — none revive (no alignment-theory / no dependency-locking / no AI-disclosure / no personality-driven / no aggregator framing / no AutoGen-extension)

### Pattern strengthening (no status change)

- **#17 Ecosystem-Layer Organizations (CONFIRMED v15)** — Jarrod Watts has 144 public repos but only claude-hud is breakout scale. Is this a **solo-one-hit-flagship** variant (distinct from multi-publisher variant 1)? Observational; NOT registered as new variant (consolidation-forward — would need N=2 to register). Noted in wiki.
- **#18 Agent Runtime Standardization (CONFIRMED v15)** — claude-hud is a **plugin-layer primitive** for Claude Code's native statusline API. Reinforces the Claude-Code-native runtime standard. Not MCP-consumer like prior 9 data points, but EXTENSION-point consumer (statusline primitive). Strengthens Pattern #18 in a new direction.
- **#19 Intellectual Lineage Archetypes (CONFIRMED v20)** — **NO explicit lineage cited**. This is archetype 4 (no-lineage / tool-chain-only), consistent with GitNexus v33 archetype 4 precedent. 12th T1 datapoint for archetype 4.
- **#20 Solo-Scale Ceiling (CONFIRMED v21 refinement)** — NEW ROW "solo-Australian + narrow-utility-plugin + native-marketplace-distribution T1" (20K/3.7mo ≈ 5.4K/month). Validates that narrow scope + native distribution surface CAN scale to 20K+ in 3 months.
- **#27 Community-Viral Scale Path (CONFIRMED v21)** — **12th data point; native-plugin-marketplace-as-distribution sub-path**. Distinct from prior sub-paths (Reddit-viral / multi-channel-pedagogical / corporate-amplified / solo-organic-sustained). The `/plugin marketplace add` mechanism is itself the distribution channel.
- **#24 SECURITY.md (STALE or candidate)** — wait, #24 is already recorded at v32 as 4th T1 data point. claude-hud has SECURITY.md → 5th-6th T1 data point. Strengthening (would approach promotion threshold if not already past).
- **#51 Vibe-Coding Spectrum (CONFIRMED v29 audit)** — claude-hud is neutral on vibe axis (pure utility, no methodological stance). Not a new pole; no impact.
- **#73 Regional-Archetype-Registry T1 Meta-Pattern (CANDIDATE v34)** — Australian observation at N=1 Australia. **Not registered as 4th sub-variant at N=1** per consolidation-forward discipline. Noted for future un-staling or as observational. If a 2nd Australian T1 emerges, would graduate 73d to formal sub-variant (N=2 structurally-unambiguous).

### New candidate registration (budget ≤1-2 per ratio constraint)

**NONE — consolidation-forward discipline applied.**

Initial consideration: register #74 "Native-Plugin-Marketplace Distribution."

**Overlap pre-check against Pattern #59 (Claude Code Plugin Marketplace Native, CANDIDATE v27):**
- #59 formal statement: *"Framework uses Claude Code `/plugin marketplace add` as primary install channel."*
- claude-hud case: `/plugin marketplace add jarrodwatts/claude-hud` is the ONLY supported install path.
- **Overlap assessment:** **~100%** (same architectural pattern, same install surface). Far above 70% rejection threshold.

**Decision per v2.1 Phase 0.5 overlap protocol:** **Reject #74 registration; strengthen #59 to N=2 instead.**

**#59 Plugin Marketplace Native — STRENGTHENS to N=2 (promotion-candidate at next audit)**

Per #59's v27 registration: *"Required for promotion: 2+ framework using Claude Code plugin marketplace as primary install. Prediction: High — likely promotes quickly."* That prediction validates at v35 (2 wikis after candidate birth).

**Evidence (N=2 post-v35):**
1. **oh-my-claudecode v27** — `/plugin marketplace add github.com/Yeachan-Heo/oh-my-claudecode` primary, though sibling npm package `oh-my-claude-sisyphus@latest` exists (branding divergence Pattern #57 captures this).
2. **claude-hud v35** — `/plugin marketplace add jarrodwatts/claude-hud` is the ONLY install path. No npm publish despite TypeScript+package.json. **First pure-marketplace-only T1 in corpus.** Marketplace manifest auto-updates via version field in `plugin.json`.

Sub-variants emerge even at N=2:
- **59a Marketplace-with-sibling-npm** (OMC) — marketplace primary, npm companion
- **59b Marketplace-only** (claude-hud) — marketplace sole distribution surface

**Promotion-path:** Structurally-unambiguous-at-N=2 (Criterion 2 per v2.1). Should promote at next mini-audit.

**Net candidate count: +0** (no new candidates registered). Ratio stays 0.79:1 (no movement). **This is ratio-discipline text-book.**

### Counter-evidence observations

- **Pattern #22 AGENTS.md T1 absence** — claude-hud has CLAUDE.md + CLAUDE.README.md but NO AGENTS.md. Continues solo-T1-skips-AGENTS.md pattern (solo: claude-howto v32 ✗, OMC v27 ✓, codymaster v12 ✗, claude-hud v35 ✗). No refinement needed.
- **Pattern #12 Governance-Depth** — claude-hud has UNUSUALLY HEAVY governance for solo 3-month-old project (7 governance files: CODE_OF_CONDUCT / CONTRIBUTING / SECURITY / SUPPORT / MAINTAINERS / TESTING / RELEASING). Pattern #12 states governance-depth correlates with ORGANIZATION (not scale). **claude-hud is counter-evidence: heavy governance on solo small project.** Could be hypothesized as "solo-with-enterprise-aspiration" sub-variant or noise. **Noted for Phase 5 counter-evidence check.** Not registered as new candidate (N=1, consolidation-forward).

### Storm Bear meta-entity applicability (Phase 0.9)

**YES — include 4th entity as Storm Bear meta.** Reasons:
1. Claude Code statusline plugin directly usable in Storm Bear operator's daily workflow (Storm Bear vault IS Claude Code-driven; knowing context window health = immediately useful)
2. Native plugin marketplace discovery mechanism = worth understanding for operator's Claude Code fluency
3. Pattern #18 Agent Runtime Standardization — plugin system itself is the runtime standard being normalized
4. Low-install-friction, low-risk utility = HIGH pilot candidate
5. **24th consecutive Storm Bear meta-entity** (v10-v35)

## Phase 4b routing mode

**Primary:** **T1 sub-classification introduction — display-layer plugin genre emergence observation** (NOT T1 12-way).

**Rationale:** T1 at N=12 means full N-way comparison is unwieldy (prior analysis at v34 already flagged 11-way as edge of usability). Instead:

- **Frame as:** T1 sub-classification introduction — the PRIOR 11 T1 entrants are frameworks / methodologies / skill-libraries / tutorials / aggregators (broad-scope mental-model products). claude-hud is the **1st display-layer plugin** — narrow-scope, single-purpose, pure-utility, no methodology, no mental-model, no conceptual framework.
- **Propose axis:** T1 scope-breadth axis (broad-methodology ← mid-utility-library → narrow-display-primitive)
- **Observe emergence:** Display-layer / narrow-utility T1 plugins may be an **emerging sub-genre** catalyzed by Claude Code's native plugin marketplace primitive
- **Register observation:** If 2nd narrow-display-plugin T1 emerges at scale, formalize as sub-variant

~500-700 lines Phase 4b deliverable focusing on: (a) T1 scope axis taxonomy, (b) display-layer-plugin emergence hypothesis, (c) Pattern #18 extension-point-consumer variant, (d) native-plugin-marketplace distribution observation, (e) primitive-count flagging inaugural outcome, (f) Storm Bear pilot relevance.

## Scope and boundaries

- **In-scope:** 12th T1 entrant + display-layer plugin genre emergence + Pattern #18 / #20 / #27 strengthening + primitive-count inaugural flagging + pilot recommendation
- **Out-of-scope:** Full 38-config-option replication (reference table in README is self-sufficient), deep code archaeology of src/ modules (CLAUDE.README.md already covers this — cite rather than replicate), full T1 12-way comparison matrix

## Pilot ranking preview

**Very HIGH pilot relevance — NEW #2 after spec-kit (or potentially #1):**
- **Zero-friction install** (3 slash commands, 5 minutes)
- **Immediate ROI** for Storm Bear operator (context-window health visibility = prevents /compact surprises mid-work)
- MIT + solo bus-factor acceptable for this scope (if author goes dark, functionality still works standalone; fork-and-maintain cost low)
- Directly addresses a Storm Bear operator pain-point: mid-session context-budget blindness when deep in a long wiki build
- No Vietnamese needed (statusline is numeric/glyph-heavy, language-agnostic)
- Native Claude Code integration = no standalone install path, no external service dependency

**Caveats:**
- Solo bus factor (mitigated by low-scope + MIT)
- 3-month-old project — some churn in config surface still visible in CHANGELOG (6 released minor versions)
- Heavy governance overhead seems premature for project scope — yellow flag for potential over-engineering

## Cross-references (sibling wikis)

Primary peers (to cite in 02 Wiki + 03 Published):
- `../claude-code-best-practice - Beginner Analysis/` (v34) — most recent T1 peer, shares Claude-Code-native positioning
- `../claude-howto - Beginner Analysis/` (v32) — tutorial/guide T1 peer with Boris Cherny citation
- `../oh-my-claudecode - Beginner Analysis/` (v27) — 1st plugin-marketplace-native mention (Pattern #59 candidate origin)
- `../agency-agents - Beginner Analysis/` (v18) — prior narrow-T1 precedent (shell-first + 144-agent library)
- `../Everything Claude Code - Beginner Analysis/` (v1) — US T1 1st-in-corpus
- `../Superpowers - Beginner Analysis/` (v2) — Jesse Vincent US T1 methodology peer (contrast: broad-scope)
- `../spec-kit - Beginner Analysis/` (v17) — GitHub/Microsoft T1 methodology peer (contrast: broad-scope methodology + uv distribution)

## Next action (Phase 1)

Build `02 Wiki/(C) index.md` + `(C) log.md` + `01 Analysis/(C) open questions.md`, then proceed to Phase 2 (3 cluster summaries).

---

*(C) Claude-generated 2026-04-23 under routine v2.1 execution 4 (v35 fourth v2.1-era wiki after claude-howto v32 + GitNexus v33 + claude-code-best-practice v34).*
