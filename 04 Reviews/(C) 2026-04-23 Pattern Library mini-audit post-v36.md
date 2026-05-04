# (C) Pattern Library Mini-Audit Post-v36 (2026-04-23)

> **Trigger:** Operator-chosen Option 2 from Claude's post-v36 recommendation. Proactive mini-audit at 0.79:1 (below 0.95:1 trigger). Targeted scope: promote #69 + #73 + refine #18.
> **Pre-audit state:** 33 confirmed + 26 active + 5 stale + 6 retired + 1 observation-track = 71 full / 59 active. Ratio 26:33 = **0.79:1 (healthy pre-trigger)**.
> **Scope:** 3 requested actions + 1 bonus (#59 also N=2 structural at v35).
> **Audit goal:** Consolidate accumulated promotion-ready candidates from v31-v36 wikis under meta-pattern-at-N=3 + structural-N=2 + counter-evidence-refinement criteria. Strengthen library structure.

---

## Executive summary

### Actions taken (5 total — 3 requested + 2 bonus)

**Promotions (3):**
- **#69 Agent-PR Fast-Track Governance Protocol → CONFIRMED** under structural-N=2 criterion (v31 awesome-mcp-servers 69a `🤖🤖🤖` contributor-authored + v36 pi-mono 69b `lgtm`/`lgtmi` maintainer-authored). v31 prediction validated.
- **#73 Regional-Archetype-Registry T1 Meta-Pattern → CONFIRMED** under meta-pattern-at-N=3-consolidation criterion (Korean OMC v27 + VN codymaster/claude-howto + Pakistani claude-code-best-practice v34). 2nd meta-pattern promotion in corpus history (first was #68 at v31 mini-audit).
- **#59 Claude Code Plugin Marketplace Native → CONFIRMED** [BONUS] under structural-N=2 criterion (v27 oh-my-claudecode marketplace+npm companion + v35 claude-hud marketplace-only).

**Absorption-retirements (2):**
- **#70 VN-Regional-Archetype T1 → RETIRED (absorbed into #73)** — was CONFIRMED at v32 mini-audit; now sub-classification 73b within #73 meta-pattern. 3rd absorption-retirement in corpus.
- **#55 Korean Regional Archetype T1 → RETIRED (absorbed into #73)** — was STALE-CANDIDATE; absorbed as sub-classification 73a. First stale-to-retired-via-absorption pathway.

**Formulation extensions (1):**
- **Pattern #18 Agent Runtime Standardization — MCP-exclusion counter-evidence added** — extends v31-mini-audit formulation with 4th observation: T1-scale deliberate MCP rejection (pi-mono v36 at 38.9K stars, "MCP is overhyped" positioning). NOT a status change. 2nd counter-evidence-driven refinement of #18 (first was v31 mini-audit MCP-inclusion layer).

### Net state transitions

| Status | Pre-audit | Post-audit | Δ |
|--------|-----------|------------|---|
| Confirmed | 33 | **34** | +1 net (+3 promoted -2 absorbed) |
| Refined (subset of Confirmed) | 14 | **15** | +1 (#18 MCP-exclusion counter-evidence extension) |
| Active Candidate | 26 | **23** | -3 (all 3 promoted) |
| Stale | 5 | **4** | -1 (#55 absorbed) |
| Retired | 6 | **8** | +2 (#55, #70 absorbed) |
| Observation-track | 1 | **1** | 0 |
| **Active library total** | 59 | **57** | -2 |
| **Full library total** | 71 | **71** | 0 |

### Ratio resolution

- Pre-audit: 26:33 = **0.79:1**
- Post-audit: 23:34 = **0.68:1**

**Ratio drops 0.11 points** via 3 promotions + 2 absorption-retirements. Lowest ratio since v22 (post-LlamaFactory).

### Trigger status post-mini-audit

- Current rules: candidate count 23 < 25 ✓ / ratio 0.68:1 < 1:1 ✓ → no trigger
- Proposed cadence reform: ratio 0.68:1 < 0.95:1 ✓ → no mini-audit trigger / < 1.05:1 ✓ → no full audit trigger
- **Next trigger:** candidate count ≥25 OR v41 wiki OR ratio >0.95:1 (mini) / >1.05:1 (full)

---

## Phase A — Promotion review

### Promotion 1: #69 Agent-PR Fast-Track Governance Protocol → CONFIRMED

**Pre-audit status:** CANDIDATE since v31 awesome-mcp-servers (N=1 stale-risk-flagged at registration); STRENGTHENED v36 pi-mono to N=2 structurally-unambiguous.

**Evidence at N=2 with sub-variant diversity:**

| # | Wiki | Sub-variant | Authored-by | Mechanism | Trust-direction |
|---|------|-------------|-------------|-----------|-----------------|
| 69a | awesome-mcp-servers v31 | `🤖🤖🤖` title suffix | Contributor (agent-authored PRs) | Opt-in PR title marker | Contributor→maintainer disclosure |
| 69b | pi-mono v36 | `lgtm` / `lgtmi` | Maintainer (approval gating) | Explicit approval command in PR description | Maintainer→merge-gate authorization |

**Formal statement (promoted):**
> Frameworks with high contributor + agent activity adopt explicit agent-PR fast-track governance protocols — workflow-level primitives that route automated-agent-authored or agent-reviewed PRs distinctly from human-authored ones. Two structural sub-variants observed: **(a) contributor-side disclosure** (contributor marks PR as agent-authored via title/body marker like `🤖🤖🤖`; maintainer decides fast-track vs scrutiny); **(b) maintainer-side approval gating** (maintainer uses explicit approval command like `lgtm`/`lgtmi` signaling merge-readiness; disambiguates LGTM-as-vibe vs LGTM-as-authorization). Protocols emerge in high-throughput repos where ambient agent activity + PR volume create signal-to-noise problems for standard human-oriented governance. Distinct from Pattern #23 AI-Disclosure (retired v27 — passive compliance declaration); #69 is active-workflow-primitive.

**Cross-references:**
- **#23 AI-Disclosure Policy (RETIRED v27 audit):** Passive-declaration pattern; retired for lack of adoption. #69 is the active-workflow successor — adoption spreads where #23 didn't because it solves concrete throughput problem rather than compliance theater.
- **#7 Marketplace Emergence (confirmed):** Both are community-scale-governance patterns (plugin discovery / PR routing).
- **#12 Governance-Depth Correlation (confirmed):** Adoption of #69 correlates with high governance investment.

**Confidence:** Medium-High. N=2 at 2 distinct structural sub-variants (opt-in marker vs approval command). v31 prediction validated ("may spread as agent activity increases"). Further observations expected as ecosystem matures.

**Prediction:** N=3+ likely within v40-v45. Candidate observations: awesome-design-md v25 (if CONTRIBUTING updated), high-volume community-platform repos.

---

### Promotion 2: #73 Regional-Archetype-Registry T1 Meta-Pattern → CONFIRMED

**Pre-audit status:** CANDIDATE since v34 claude-code-best-practice (registered consolidation-forward at N=3; not standalone Pakistani registration).

**Evidence at N=3 across 3 distinct regions:**

| Sub-variant | Region | Wikis | Distinguishing features |
|-------------|--------|-------|-------------------------|
| **73a Korean** | Korea | oh-my-claudecode v27 (Yeachan Heo) | Korean README primary; Korean collaborators predominant; Korean OSS tradition |
| **73b VN** | Vietnam + VN-diaspora | codymaster v12 (Tody Le VN-in-VN) + claude-howto v32 (Luong Nguyen VN-diaspora Paris) | 2 sub-sub-variants: in-country vs diaspora; 742× scale divergence (38 vs 28K stars) |
| **73c Pakistani** | Pakistan | claude-code-best-practice v34 (Shayan Rais Karachi) | Claude Community Ambassador explicit; multi-channel content distribution |

**Formal statement (promoted as meta-pattern):**
> T1 Agent-as-assistant frameworks exhibit observable regional-archetype diversity distinct from US-anglophone default. Meta-pattern wraps 3 structurally-distinct sub-variants: Korean (73a), VN including VN-diaspora (73b), Pakistani (73c). Each regional sub-variant displays characteristic combinations of: (a) primary-language README prominence, (b) regional-collaborator clustering, (c) local OSS tradition inheritance, (d) audience-targeting + distribution-channel choices, (e) commercial-positioning vs community-positioning defaults. Meta-pattern absorbs prior #55 Korean + #70 VN as sub-classifications. Further regional sub-variants expected as T1 continues growth (Austrian observed v36 pi-mono as observational 73d; Indian observed v33 GitNexus at T4 but cross-tier framing deferred).

**Promotion rationale:** Meta-pattern-at-N=3-consolidation criterion (4th structural-promotion criterion introduced v31 mini-audit). Each sub-variant structurally distinct. N=3 at 3 distinct regions. Promotion saves fragmentation (3 separate regional candidates) into unified explanatory structure.

**Absorptions:**
- **#55 Korean Regional Archetype T1** (stale-candidate) → absorbed as 73a
- **#70 VN-Regional-Archetype T1** (confirmed at v32 mini-audit) → absorbed as 73b

**First stale-to-retired-via-absorption pathway** in corpus (#55). Prior stale-retirements (v27 audit) were all aging-out retirements; #55 retires via absorption into superseding meta-pattern. Demonstrates stale-candidates can still participate in meta-pattern consolidation.

**Cross-references:**
- **Pattern #17 Ecosystem-Layer Organizations (confirmed v15):** Regional-archetype is orthogonal axis; some regional authors are ecosystem-layer (Luong variant 1 8th data point); some are not.
- **Pattern #27 Community-Viral Scale Path (confirmed v21):** Regional sub-variants show distinct viral scale ceilings; Pakistani 73c at 47.4K sustained-viral highest regional-non-anglophone observation.
- **Pattern #20 Solo-Scale Ceiling (confirmed):** Regional archetype × scope × distribution interact to determine scale ceiling.
- **Pattern #68 Awesome-List-Genre Meta-Pattern (confirmed v31):** Sibling meta-pattern also at N=3. Both are consolidation-forward registrations.

**Confidence:** Medium-High. N=3 at 3 structurally-distinct regions. Further regional sub-variants welcome but not required.

**Prediction:** 4th regional sub-variant likely within v40-v50 as T1 continues growth. Austrian 73d observational at v36 pi-mono could promote to structural if 2nd Austrian observed. Indian observation at v33 GitNexus was T4 cross-tier — if 2nd Indian at T1 emerges, 73e Indian promotes.

**Meta-observation (corpus-level):**
This is the **2nd meta-pattern-at-N=3-consolidation promotion in corpus history** (first was #68 at v31 mini-audit). Meta-pattern promotion rate: ~2 per 6 wikis at current velocity. Library maturing into meta-structural layer.

---

### Promotion 3 (BONUS): #59 Claude Code Plugin Marketplace Native → CONFIRMED

**Pre-audit status:** CANDIDATE since v27 oh-my-claudecode (N=1); STRENGTHENS v35 claude-hud to N=2 structurally-unambiguous.

**Evidence at N=2 with sub-variant diversity:**

| # | Wiki | Sub-variant | Distribution model |
|---|------|-------------|--------------------|
| 59a | oh-my-claudecode v27 | Marketplace + npm companion | Plugin marketplace primary + `oh-my-claude-sisyphus@latest` npm package secondary |
| 59b | claude-hud v35 | Marketplace-only | Plugin marketplace exclusive; no alternative install path |

**Formal statement (promoted):**
> T1 Agent-as-assistant frameworks increasingly adopt Claude Code plugin marketplace as native primary install mechanism. Two structural sub-variants: **(a) marketplace + companion package manager** (marketplace primary + npm/pip secondary for alternative distribution); **(b) marketplace-only** (no alternative install path; plugin marketplace is the distribution surface). Pattern reflects Claude Code ecosystem maturity — marketplace as first-class Claude Code native distribution channel. Distinct from Pattern #7 Marketplace Emergence (confirmed v11 — general marketplace pattern; #59 is specifically Claude Code plugin marketplace at T1 tier).

**Cross-references:**
- **#7 Marketplace Emergence (confirmed v11):** Parent pattern; #59 is Claude-Code-specific sub-pattern at T1.
- **#2 Distribution Evolution (confirmed):** Related; #59 is current-state marker for Claude Code T1 distribution.

**Confidence:** Medium-High. N=2 at 2 structural sub-variants. Prediction: N=3+ likely within 5-10 wikis as Claude Code plugin marketplace matures.

---

## Phase B — Absorption-retirements

### ❌ #70 VN-Regional-Archetype T1 → RETIRED (absorbed into #73)

**Originally:** v32 claude-howto (promoted to CONFIRMED at v32 mini-audit under structural-N=2 criterion; 2 sub-variants 70a VN-in-VN + 70b VN-diaspora).

**Wikis since promotion:** 4 (v33-v36).

**Retirement rationale:** Absorbed into Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern at v36 mini-audit as sub-classification 73b VN. Retaining #70 as standalone confirmed pattern alongside #73 meta-pattern would fragment unified explanatory structure. #73 promotion under meta-pattern-at-N=3-consolidation criterion subsumes #70's observations formally.

**3rd absorption-retirement in corpus** (after #60 at v29 audit + #49 at v31 mini-audit). First confirmed-pattern absorption (prior 2 were candidate-absorption). Demonstrates confirmed patterns can retire via meta-pattern consolidation.

**Revive if:** Structural evidence emerges that VN-regional-archetype has properties distinct from #73 meta-pattern framing beyond sub-variants 70a/70b. Monitor.

---

### ❌ #55 Korean Regional Archetype T1 → RETIRED (absorbed into #73)

**Originally:** v27 oh-my-claudecode (N=1 stale-risk-flagged at registration); STALE-FLAGGED v32 mini-audit retroactive.

**Wikis since:** 9 (v28-v36).

**Retirement rationale:** Absorbed into Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern at v36 mini-audit as sub-classification 73a Korean. Meta-pattern now encompasses Korean-archetype observation as structural sub-variant.

**First stale-to-retired-via-absorption pathway in corpus.** Prior stale-retirements (v27 audit × 4 patterns) were all aging-out retirements — retired due to N=1 persistence past +10 threshold without evidence. #55 retires via absorption into superseding meta-pattern — new pathway demonstrates stale-candidates can participate in meta-pattern consolidation rather than just age out.

**Revive if:** Additional Korean-specific structural evidence emerges beyond what #73 captures. Monitor.

---

## Phase C — #18 formulation extension (MCP-exclusion counter-evidence)

### 🔄 #18 Agent Runtime Standardization — MCP-exclusion counter-evidence added (v36 mini-audit)

**Pre-audit status:** Confirmed since v15; refined multiple times (v17, v18, v19, v20 regional + archetype specificity; v31 mini-audit triple-layer MCP/OpenClaw/Hermes extension).

**Status change:** NONE (remains confirmed). Formal statement extended with 4th observation layer: MCP-exclusion counter-evidence.

**v36 counter-evidence:**
- pi-mono v36 at 38.9K stars T1-scale **deliberately rejects MCP** — explicit positioning in AGENTS.md + README: *"MCP is overhyped; LLM-native tool-calling + provider-direct integration is sufficient."*
- 1st T1-scale MCP-exclusion in corpus (prior MCP-exclusion observations were CN-ecosystem / foundation-model archetype specific)
- Mario Zechner's architectural choice is deliberate, not absence-by-omission

**Extended formal statement (v36):**
> Agent runtime standardization operates at 3 distinct layers (v31 mini-audit triple-layer formulation retained):
>
> **Layer 1 — Protocol layer (MCP, corpus-dominant 2024-2026):** Model Context Protocol as universal resource-access standard. 7+ corpus wikis adopt MCP. 85K-star directory (awesome-mcp-servers v31). **MCP transcends regional + archetype axes generally BUT has observable exceptions:**
>
> **Layer 1 exclusion observations (v36 extension):**
> - **CN-ecosystem exclusions** (N=2 pre-v36): TrendRadar v19 + fish-speech v20 skip MCP using parallel infrastructure (LiteLLM / Cherry Studio)
> - **Foundation-model exclusions** (N=1 pre-v36): fish-speech v20 skips MCP (foundation-model archetype specific)
> - **T1-scale deliberate rejection** (N=1 at v36): pi-mono v36 deliberately rejects MCP at 38.9K stars with explicit positioning *"MCP is overhyped; LLM-native tool-calling sufficient."*
> - **Pattern:** MCP adoption is overwhelmingly dominant (7/11 corpus T1 wikis) but NOT universal. Exclusions cluster around: (a) CN-ecosystem parallel infrastructure, (b) foundation-model archetype, (c) T1-scale deliberate-rejection (v36 new layer).
>
> **Layer 2 — Runtime identifier layer (OpenClaw + Hermes, Western-community-platform specific):** unchanged from v31 formulation.
>
> **Layer 3 — Agent-execution layer:** unchanged.
>
> Framework MCP adoption is best modeled as ~70-75% default with structured exclusion categories, not 100% universal.

**Significance:**
- 2nd counter-evidence-driven refinement of #18 (first was v31 mini-audit triple-layer extension)
- Formalizes MCP-adoption is not universal at T1-scale
- pi-mono v36 observation expands exclusion taxonomy: CN-ecosystem / foundation-model / **T1-scale-deliberate-rejection**
- Does NOT invalidate #18 (which is about standardization pattern observed) — refines scope
- Demonstrates counter-evidence mechanism (v29 audit introduction) continues maturing at scale

**Cross-references:**
- **Pattern #7 Marketplace Emergence (confirmed):** MCP server directory is marketplace-equivalent.
- **Pattern #28 Multi-Provider AI Support (confirmed v25 audit):** Related to #18 Layer 1; pi-mono v36 also strong #28 example (multi-provider-first architecture).
- **#59 Claude Code Plugin Marketplace Native (promoted this audit):** Layer-adjacent; plugin marketplace is T1-specific distribution surface.

---

## Phase D — Net state + meta-observations

### Full post-mini-audit state

- **Confirmed:** 34 patterns (net +1 after absorption)
- **Refined (subset of Confirmed):** 15 (was 14 + #18 MCP-exclusion extension)
- **Active Candidate:** 23
- **Stale:** 4 (was 5 - #55 absorbed)
- **Retired:** 8 (was 6 + #55 + #70 absorbed)
- **Observation-track:** 1 (#66 unchanged)
- **Full library total:** 71 (unchanged; promotion + absorption net zero)
- **Active library total:** 57 (was 59, -2)
- **Ratio:** 23:34 = **0.68:1** (lowest since v22; healthy)

### Structural firsts at v36 mini-audit

- **2nd meta-pattern-at-N=3-consolidation promotion** (#73; first was #68 at v31 mini-audit)
- **3rd absorption-retirement** in corpus (after #60 v29 + #49 v31 mini-audit)
- **First confirmed-pattern absorption** (#70 confirmed → retired via meta-pattern consolidation; prior absorptions were candidate→retired)
- **First stale-to-retired-via-absorption pathway** (#55 stale → retired via #73 absorption; prior stale-retirements were all aging-out)
- **2nd counter-evidence-driven refinement of #18** (first was v31 MCP-inclusion triple-layer; now v36 MCP-exclusion taxonomy)
- **First T1-scale deliberate MCP-rejection observation** (pi-mono v36)

### Meta-observations

**Strengthen-over-discover discipline operationalized across 5 wikis (v32 → v33 → v34 → v35 → v36):**
- v32: 2 new candidates (#70 + #71)
- v33: 1 new candidate (#72)
- v34: 1 new candidate (#73 consolidation-forward)
- v35: **0 new candidates** (overlap pre-check rejected #74)
- v36: **0 new candidates** (consolidation-forward rejected 5 proposed)

Candidate-registration rate declining: 2 → 1 → 1 → 0 → 0. Library saturating on architectural patterns. Meta-pattern consolidation at v31 + v36 suggests next natural refactor direction is meta-pattern-layer expansion.

**Meta-pattern promotion cadence:** 2 meta-patterns in 5 wikis (#68 at v31 + #73 at v36). Corpus is transitioning from candidate-accumulation phase to meta-pattern-consolidation phase.

**Action items for routine v2.2 (when natural cadence triggers):**
- Meta-pattern-at-N=3-consolidation criterion now validated 2×; codify as routine-v2.2 default (not just v2.1 introduction)
- Absorption-retirement mechanism now validated 3× (N=60 + #49 + #55 + #70); codify as routine-v2.2 default
- Counter-evidence-driven refinement of confirmed patterns now validated 3× (Patterns #47, #48 v29 audit + #18 v31 + v36 mini-audits); codify as routine-v2.2 default
- Pattern Library may need "meta-pattern registry" section if meta-pattern count ≥5

### Backlog status

**v27 diagnostic HIGH bundle:** 13 sessions deferred pre-audit; this audit didn't address it. Still pending post-audit.

**Operator-facing implication:** Pattern Library is now in its healthiest state since v22 (ratio 0.68:1). Structural consolidation round complete. Next operator action cycle should prioritize vault-diagnostic execution over further wiki growth.

---

## Audit closure

**All 5 actions executed** (3 requested + 2 bonus). Post-audit state applied to:
- `PATTERN_LIBRARY.md` — pending update (this audit authoritative)
- `GOALS.md` — pending update (session 44 entry)
- `CLAUDE.md` — pending update (post-v36-mini-audit state block)

**Next trigger:** candidate count ≥25 OR v41 wiki OR ratio >0.95:1 (mini) / >1.05:1 (full).

**Recommended next action:** v27 diagnostic HIGH bundle (13 sessions deferred; pattern-library health no longer bottleneck; operator-facing vault work is next-highest-ROI).

---

**v36 mini-audit shipped 2026-04-23. 3 promotions + 2 absorption-retirements + 1 formulation extension. Ratio 0.79:1 → 0.68:1. 2nd meta-pattern-at-N=3 promotion (#73) + 3rd absorption-retirement (#70 + #55) + 2nd counter-evidence-driven #18 refinement. Library transitions from candidate-accumulation to meta-pattern-consolidation phase.**
