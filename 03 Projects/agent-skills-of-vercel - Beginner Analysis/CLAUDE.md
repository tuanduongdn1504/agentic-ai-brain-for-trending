# (C) agent-skills-of-vercel — Project CLAUDE.md

> **51st LLM Wiki — first wiki post-corpus-half-century-milestone (v50).**
> Source: https://github.com/vercel-labs/agent-skills
> Routine: `05 Skills/llm-wiki-routine-v2.1.md`
> Built: 2026-04-25
> Storm Bear vault root: `/Users/Cvtot/KJ OS Template/`

---

## Phase 0: Pre-flight + 12-axis classification

### 0.1 Consolidation guard check

**Pre-v51 state (post-v50 4-action mini-audit, 2026-04-25):**
- 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio 18:38 = **0.474:1 — first sub-0.50:1 ratio in corpus history (held 0 cycles; v51 is first wiki post-mini-audit)**
- 0.476 buffer below 0.95:1 mini-audit trigger — **largest in corpus history**
- 14-consecutive-wiki zero-new-active-candidates streak (v37-v50)
- ⚠️ v27 diagnostic HIGH bundle backlog: **30 sessions deferred** (BLOCKING-RECOMMENDATION 6× threshold)

**Verdict:** PROCEED — library is unprecedented-healthy; ratio buffer 0.476 means v51 has runway. Default consolidation-forward (target: extend zero-streak to 15 wikis).

### 0.2 WebFetch-style probe (verified)

| Field | Value |
|-------|-------|
| Repo | `vercel-labs/agent-skills` |
| Description | "Vercel's official collection of agent skills" |
| Stars | 25,695 (#15 in corpus by scale) |
| Forks | 2,337 (9.1%) |
| Watchers | 25,695 (note: same as stars — possible API quirk) |
| Open issues | 131 |
| License (GitHub API) | **null** — no auto-detected LICENSE file at root |
| License (README §License) | **MIT** (claim only; no file at root) |
| Per-skill license | **4 of 7 skills declare `license: MIT` in YAML frontmatter; 3 do not** (corpus-first per-skill license metadata variation) |
| Primary lang | JavaScript |
| Default branch | main |
| Created | 2025-12-08 (~4.5 months — **2nd-youngest wiki subject in corpus** after bizos v37 cold-start) |
| Pushed | 2026-04-20 (5 days ago, active) |
| Repo size | ~10 MB |
| Topics | empty |
| Homepage | **https://skills.sh/vercel-labs/agent-skills** (skills.sh = third-party agent-skills registry, NOT Vercel-owned domain) |

**Owner:** Vercel Labs (`vercel-labs`) — Vercel Inc. ("Develop. Preview. Ship. Creators of Next.js."). 262 public repos, 5,980 followers, founded 2022-07-01 as a GitHub org under Vercel parent. Email support@vercel.com.

### 0.3 Branch resolution

main branch returned content cleanly. No fallback needed.

### 0.4 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant — corporate-narrow-skill-library sub-archetype.** Distinct from prior T1 entrants (methodology / aggregator / tutorial / display utility / multi-package monorepo). Not Pattern #68 awesome-list-genre (no curation of external skills — only Vercel-Engineering-built). |
| **Archetype** | **Ecosystem-scale commercial platform extension** (Pattern #17 variant 5 N=3 strengthening — joins HuggingFace v26 + Microsoft v6+v28). Vercel: >$10B private valuation (publicly reported 2024), Next.js + Vercel Cloud + AI SDK + v0 + multiple products, OSS + commercial tier, ~10 years mature (2015 founding). |
| **Scale tier** | Large (25.7K / 4.5 months ≈ 5,700 stars/month corporate-amplified-organic) |
| **Primary lang** | JavaScript (build tooling) — content is markdown SKILL.md + bash scripts. Skills target React / Next.js / React Native code. |
| **Packaging** | **`npx skills add vercel-labs/agent-skills`** (corpus-first third-party-registry-non-Anthropic install verb; via skills.sh / agentskills.io) + per-skill ZIP bundles + manual `cp -r skills/{name} ~/.claude/skills/` + paste-to-claude.ai |
| **Origin story** | Corporate-strategic — Vercel Engineering produces internal best-practice rules; packages as agent skills to amplify Vercel ecosystem (Next.js + Vercel Cloud + claimable-deployment funnel) |
| **Methodology** | None named (no SDD/BMM/TDD); rule-based agent-augmentation (40-100+ rules per skill) + claimable-deployment-as-agentic-pattern |
| **Governance file count** | **2 (LIGHT) — `AGENTS.md` + `CLAUDE.md` are byte-identical mirrors** (3,281 bytes each, both starting `# AGENTS.md`). Corpus-first 22d identical-mirror sub-variant. Plus README.md. No CONTRIBUTING / SECURITY / CODE_OF_CONDUCT / LICENSE / CITATION.cff. |
| **Agent/skill count** | **7 skills** (composition-patterns / deploy-to-vercel / react-best-practices / react-native-skills / react-view-transitions / vercel-cli-with-tokens / web-design-guidelines) |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | "Vercel Engineering" (corporate collective; Pattern #19 archetype 4 no-explicit-individual-lineage). No Karpathy / John Lam / research-paper-chain. |
| **Agent platforms supported** | Claude.ai + Claude Code + Cursor + Copilot (per AGENTS.md guidance). MCP **not adopted** (counter-evidence to Pattern #18 at corporate-official tier; observational). |

### 0.5 Cross-wiki pattern pre-check

**Strengthening (consolidation-forward — default):**

1. **Pattern #17 variant 5 ecosystem-scale commercial platform → N=3 strengthening** (HuggingFace v26 + Microsoft v6+v28 + **Vercel v51**). Variant already CONFIRMED at v29 audit under structural-N=2 criterion. Vercel v51 = 3rd structurally-criterial data point; reaches default ≥3-cross-tier criterion. Document as default-criterion strengthening; no status change needed (variant already confirmed).

2. **Pattern #57 Recursive Corpus Reference → 6th data point + 57c forward-citation-then-wiki sub-variant NEW.** v50 mini-audit promoted #57 to CONFIRMED with 2 sub-variants (57a direct citation N=4 / 57b aggregator-mediated multi-citation N=1). v51 = corpus-first **57c forward-citation-then-wiki**: vercel-labs/agent-skills was cited in **multica v15** wiki entry (Pattern Library line 2969 + CLAUDE.md row) as `"Vercel agent-skills import (first)"` — 36 wikis BEFORE the v51 wiki of vercel-labs/agent-skills itself. Distinct from 57a/b: subject was forward-cited in earlier wiki C (multica v15); later wiki D (v51) builds B's wiki. Register 57c at N=1 stale-flagged.

3. **Pattern #22 AGENTS.md → 22d identical-mirror sub-variant NEW.** Vercel ships `AGENTS.md` + `CLAUDE.md` as byte-identical 3,281-byte files (verified via `diff` — IDENTICAL). Distinct from existing sub-variants:
   - 22a: solo monolithic AGENTS.md (gh-aw v48 49.8KB)
   - 22b: minimum-viable shim (CLAUDE.md as tiny `@AGENTS.md` redirect alias; bizos v37 11B)
   - 22c: authoritative-with-shim 3-layer hierarchy (aidevops v47)
   - **22d NEW: identical-mirror full-content duplicated** (no canonical source; both files served independently)
   Register 22d as observational sub-variant at N=1 stale-flagged.

4. **Pattern #29 License-Category 29-absent-3 sub-context → N=2 strengthening.** v50 mini-audit registered 29-absent-3 (absent LICENSE + README-OSI-license-claim + per-skill-license-variation) at N=1 stale-flagged with awesome-claude-skills v50. **Vercel v51 = 2nd structural data point**: no LICENSE at root + README §License says "MIT" + 4 of 7 SKILL.md files declare `license: MIT` (per-skill variation). Promotes 29-absent-3 toward structural-N=2 criterion at next mini-audit. Strengthening.

5. **Pattern #59 Plugin Marketplace Native → `npx skills add` observational sub-variant NEW.** Distinct from 59a (marketplace+npm OMC v27) + 59b (marketplace-only claude-hud v35). New: **third-party non-Anthropic registry install verb** (`npx skills add <repo>` via skills.sh / agentskills.io). Observational within Pattern #59; do NOT register standalone.

6. **Pattern #50 Commercial-Funnel Companion → N=10+ data point** with 50a Standard funnel sub-variant (claim-URL terminus). vercel-deploy-claimable returns claim URL → `vercel.com/claim-deployment?code=...` for ownership transfer. Claim-URL-as-funnel-terminus is corpus-first explicit deployment-claim-mechanism within Pattern #50 50a sub-variant. Strengthening.

7. **Pattern #18 MCP → counter-evidence at corporate-official tier (observational).** Vercel skills do NOT use MCP — pure SKILL.md + bash scripts + Claude.ai/Code direct. Joins Layer-1-MCP-exclusion observations at T1-scale (pi-mono v36) + T5-scope (DeepTutor v38, ollama v46, MiroFish v49) + T1-scale (pi-mono v36) + corporate-official-tier (gh-aw v48 with MCP-Gateway). Vercel = T1-scale + corporate-official + MCP-absent-altogether. Observational only.

8. **Pattern #19 archetype 4 no-explicit-individual-lineage → strengthening at corporate-org level.** "Vercel Engineering" cited as collective — joins magika v44 "Google Research Anti-Abuse team" + gh-aw v48 GitHub corporate.

9. **Pattern #27 Community-Viral → corporate-amplified-organic sub-path strengthening.** 25.7K / 4.5 months = 5,700 stars/month. Lower than crawl4ai v29 (~3.3K/mo solo-organic-sustained) or markitdown v28 (~6.6K/mo at peak velocity); higher than typical T1 solo-publisher sub-path. Corporate-amplified amplifier confirmed.

10. **Pattern #2 Distribution Evolution → 4-surface install observation.** `npx skills add` + per-skill ZIP + manual cp + paste-to-claude.ai. Below corpus-max (magika v44 6+ channels); standard for T1.

**Un-stale check:** All 3 stale candidates negative for v51 (verified — no relevant signal).

### 0.6 Candidate overlap pre-check

Tested 9 potential standalone candidates; ALL routed to within-existing-pattern strengthening or sub-variant registration. **0 new active candidates.** Discipline preserved.

### 0.7 Sibling detection

Sibling wikis at outside-scope + T1 corporate-skill-library:
- **awesome-claude-skills v50** (outside-scope hybrid awesome-list+aggregator) — recently shipped; structurally distinct (Vercel = no curation, only Vercel-Engineering-authored)
- **claude-howto v32 / claude-code-best-practice v34 / claude-hud v35 / pi-mono v36 / aidevops v47** (T1 entrants) — structurally distinct sub-archetypes
- **markitdown v28** (T4 corporate-narrow-utility Microsoft) — closest corporate-narrow-tier-sibling (different tier but same archetype framing)

**Phase 4b routing mode:** Tier-within-variant extension + Pattern #17 variant 5 N=3 default-criterion strengthening + Pattern #22 22d sub-variant NEW + Pattern #57 57c sub-variant NEW + Pattern #29 29-absent-3 N=2 strengthening + multi-pattern-strengthening harvest.

### 0.8 Tier placement decision

**T1 Agent-as-assistant** (12th T1 entrant — verify exact count via vault CLAUDE.md state). Skills extend Claude/Cursor/Copilot capabilities directly — fits T1 definition (skills + extensions for AI coding assistants). NOT T4 (no bridge to external service; vercel-deploy-claimable is a deployment **action** within an agent assistant, not a bridge layer). NOT outside-scope (it IS a skill collection for agents, just narrow corporate-scoped).

### 0.9 Storm Bear meta-entity applicability check

**APPLICABLE — 40th consecutive Storm Bear meta-entity** (per v2.1 Phase 0.9 per-wiki applicability):
- **Direct vault relevance HIGH** for SKILL.md format reference (vault `05 Skills/` directory expansion)
- **AGENTS.md identical-mirror 22d adds 4th template** to vault CLAUDE.md refactor reference ensemble (spec-kit v17 + aidevops v47 22c + gh-aw v48 22a + Vercel v51 22d)
- **claimable-deployment workflow** (preview-URL + claim-URL bipartite) is interesting agentic primitive but not directly applicable to Storm Bear's Scrum-coach role
- **vercel-deploy-claimable as agentic-pattern**: "deploy from conversation, transfer ownership later" is novel ergonomics

**Frame as:** SKILL.md format template + 4th AGENTS.md template + observational Pattern #17 variant 5 N=3 reference.

### Primitive-count flagging (v2.1 informal discipline)

**Probed primitive-count:** 7 skills + 4 distribution surfaces + 2 governance files + 1 build package = ~14 primitives across 4 categories.

**Outcome: GREEN** — standard 4-entity format fits cleanly. Per-skill detail compressible via citation-not-replication (each SKILL.md cited not duplicated). No follow-up deep-dive wikis needed at v51.

**Velocity expected:** ~2h GREEN baseline.

---

## Phase 4b routing mode

**Primary mode:** Tier-within-variant extension (T1 12th entrant + corporate-narrow-skill-library sub-archetype) + **Pattern #17 variant 5 N=3 default-criterion strengthening** (HuggingFace + Microsoft + Vercel) + **Pattern #22 22d identical-mirror NEW sub-variant** + **Pattern #57 57c forward-citation-then-wiki NEW sub-variant** + **Pattern #29 29-absent-3 N=2 strengthening**.

**Secondary modes:** Cross-corpus citation (multica v15 cited Vercel agent-skills) + protocol-directory meta-reference (skills.sh / agentskills.io ecosystem observation) + counter-evidence-Pattern-#18 corporate-official-tier-MCP-absence.

---

## Cross-references

**Sibling wikis (≥3 mandatory):**
- `awesome-claude-skills v50` — corpus-half-century-milestone aggregator; structurally distinct (curation vs author-built)
- `markitdown v28` — Microsoft T4 corporate-narrow-utility (closest archetype-sibling at different tier)
- `aidevops v47` — Pattern #22 22c authoritative-with-shim (3rd of 4 AGENTS.md templates)
- `gh-aw v48` — Pattern #22 22a monolithic 49.8KB (1st of 4 AGENTS.md templates; corporate-official like Vercel)
- `multica v15` — **forward-citation source** (cited "Vercel agent-skills import (first)" 36 wikis pre-v51; Pattern #57 57c registration evidence)
- `oh-my-claudecode v27` — Pattern #59 59a marketplace+npm
- `claude-hud v35` — Pattern #59 59b marketplace-only
- `HuggingFace agents-course v26` — Pattern #17 variant 5 1st structural N=2 anchor
- `Microsoft markitdown v28` — Pattern #17 variant 5 2nd structural N=2 anchor (Vercel = N=3 default-criterion)

**Pattern Library entries referenced:**
- #17 variant 5 (N=3 strengthening — default-criterion close)
- #22 (22d identical-mirror NEW sub-variant)
- #57 (57c forward-citation-then-wiki NEW sub-variant)
- #29 (29-absent-3 N=2 strengthening)
- #50 (50a claim-URL-terminus observational)
- #59 (npx-skills-add observational sub-variant)
- #18 (counter-evidence corporate-official-tier; observational)
- #19 (archetype 4 strengthening)
- #27 (corporate-amplified-organic sub-path)
- #2 (4-surface install)

---

**End of project CLAUDE.md.**
