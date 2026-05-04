# (C) oh-my-openagent — Project CLAUDE.md

> **Wiki version:** v52 (Storm Bear corpus 52nd LLM wiki)
> **Routine:** `05 Skills/llm-wiki-routine-v2.1.md` — 9th v2.1-era execution
> **Built:** 2026-04-25 → 2026-04-26
> **Source:** https://github.com/code-yeongyu/oh-my-openagent (default branch `dev`; renamed from `oh-my-opencode`)
> **Cloned:** `00 Source/oh-my-openagent/` (~30 MB, 1,766 TS files, 377k LOC, commit 2892ca4a on `dev`)

## Phase 0 verbatim probe

| Field | Value |
|-------|-------|
| Repo | code-yeongyu/oh-my-openagent (renamed; npm package still `oh-my-opencode`) |
| Description | "omo; the best agent harness - previously oh-my-opencode" |
| Stars | 54,135 (#9-ish in corpus, between MiroFish v49 57.3K and ruflo v42 33K) |
| Forks | 4,394 (8.1%) |
| Watchers | 54,135 (likely API quirk = stars; verify) |
| Open issues | 651 (HIGH community contribution churn) |
| License (GitHub) | NOASSERTION / "Other" |
| License (file) | **SUL-1.0 — Sustainable Use License Version 1.0** (custom non-OSI; non-commercial-restriction) |
| Primary lang | TypeScript (1,766 TS files; Bun-built) |
| Default branch | **`dev`** (NOT `main`/`master` — corpus-first `dev` default) |
| Created | 2025-12-03 (~4.7 months) |
| Pushed | 2026-04-25 (today, actively maintained) |
| Latest version | 3.17.5 (mature; many 3.x releases) |
| Repo size | ~59 MB raw / ~30 MB extracted |
| Homepage | https://ohmyopenagent.com/ |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, **claude-skills**, cursor, gemini, ide, openai, **opencode**, orchestration, tui, typescript |
| Author | YeonGyu-Kim (`code-yeongyu`) — Seoul, Korea; Sionic AI affiliation; bio "Hacker."; 133 public repos; 2,956 followers |
| Org affiliation | Sionic AI (`@sionic-ai`) — Korean AI startup, sionic.ai; 57 public repos |
| Adjacent venture | Sisyphus Labs (sisyphuslabs.ai) — *"Sisyphus is the agent that codes like your team"* + waitlist for "fully productized version of Sisyphus" |
| Discord | discord.gg/PUwSMR9XNk (LeaksLab? — actually own Discord; 1.4K members) |
| Twitter | @justsisyphus (proxy account; primary @q_yeon_gyu_kim suspended) |
| Telemetry | PostHog with hashed installation ID; opt-out via `OMO_SEND_ANONYMOUS_TELEMETRY=0` or `OMO_DISABLE_POSTHOG=1` |

## Tier classification (Phase 0.8)

**T1 Agent-as-assistant — 16TH T1 ENTRANT** (extends T1 from N=15 post-v51 Vercel).

Sub-archetype: **solo-Korean-Seoul + Sionic-AI-affiliated + customized-OpenClaw-fork-harness + multi-runtime-orchestration + commercial-incubation-via-sisyphuslabs.ai + EXTREME-primitive-count**.

Distinct from prior 15 T1 entrants. Closest peer: **OMC v27 Yeachan Heo** (also Korean Seoul, also OpenClaw-based, also `oh-my-*` naming, also Sisyphus mythology).

Justification:
- Plugin entry point + interactive coding harness installed against OpenCode runtime → user-facing assistant
- Not service (no daemon-as-managed-platform like multica v15 / ruflo v42 T2)
- Not bridge (not a connector between systems like notebooklm-py v7)
- Not application (not standalone autonomous loop like Skyvern v24 / shannon v45)
- Not education (not pedagogical curriculum like dive-into-llms v39)
- Not outside-scope (not aggregator or training-infra)

T1 with **EXTREME primitive surface** (1,766 TS files / 26 tools / 11 named agents / 52 hooks / 19 features / 11 platform binaries / 3-tier MCP / 5-language docs / 14 overridable agent fields / 8 hook tiers).

## v2.1 Routine 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant — 16th T1 entrant + solo-Korean-Seoul-OpenClaw-fork-harness sub-archetype** |
| **Archetype** | Solo-Korean-Seoul + Sionic-AI-employed + Sisyphus-Labs-incubation + customized-OpenClaw-fork; sibling of OMC v27 Yeachan Heo |
| **Scale tier** | Large (54K / ~4.7 months ≈ ~11.5K stars/month — sustained-community-viral; 2nd Korean Seoul T1 in corpus joins OMC ~298 stars/day) |
| **Primary lang** | TypeScript (Bun runtime; bunx CLI) |
| **Packaging** | npm (`oh-my-opencode` preserved + `oh-my-openagent` dual alias) + 11-platform Bun-compiled binaries (darwin/linux/windows × x64/arm64 × baseline/musl variants) |
| **Origin story** | Solo Korean dev → renamed `oh-my-opencode` → `oh-my-openagent` mid-2026 to broaden multi-runtime targeting; Sionic AI employment + Sisyphus Labs commercial incubation parallel |
| **Methodology** | Greek-mythology specialist agents + IntentGate classifier + Hashline LINE#ID edit-tool (corpus-first hash-anchored edit at T1) + ralph loop + ultrawork command + multi-runtime category-based model routing |
| **Governance** | 5 governance files (AGENTS.md auto-generated via /init-deep + CLA.md + CONTRIBUTING.md + LICENSE.md SUL-1.0 + README × 5 langs) — MEDIUM-HEAVY at solo-T1; counter-evidence reinforcement to Pattern #12 v42 refined formulation (7th counter-evidence wiki) |
| **Agent/skill count** | **EXTREME** — 26 tools / 11 named agents / 52 hooks / 19 features / 3-tier MCP (~3 built-in + .mcp.json + skill-embedded) / 8 categories (visual-engineering / deep / quick / ultrabrain / + 4 more) / 11 platform binaries / 14 overridable agent fields × 21 fields each / Built-in skills (playwright / git-master / frontend-ui-ux / + custom) |
| **i18n** | **5 languages** (en + ko + ja + zh-cn + ru) — corpus-first inclusion of Russian at T1; ties browser-use v41 6-lang and matches OMC v27 7-lang at T1 sustained Korean-author multi-lang norm |
| **Intellectual influence** | Multi-source (corpus-first explicit cluster): **oh-my-pi** (Hashline edit tool source + The Harness Problem blog by Can Bölük) + **OpenCode** runtime (forks/extends) + **OpenClaw** (deep customized fork; prior corpus presence in OMC v27 / multica v15 / paperclip v14 / graphify v16 / agency-agents v18) + named tribute @thdxr (X.com post about Anthropic blocking OpenCode) |
| **Agent platforms** | OpenCode primary + Claude Code compatibility layer (hooks/commands/skills/MCPs/plugins reused) + multi-runtime model routing (Claude Opus 4.7 + Kimi K2.5 + GLM 5 + GPT-5.4 + Minimax + Gemini) |

## Phase 0.5 Cross-wiki pattern pre-check

**Library state pre-v52** (per PATTERN_LIBRARY.md): 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. **Ratio 18:38 = 0.474:1 PRESERVED** (largest buffer 0.476 below 0.95:1 mini-audit trigger). 15-consecutive-wiki zero-registration streak v37-v51.

### Hypotheses tested (consolidation-forward priority)

1. **Pattern #57 57c forward-citation-then-wiki sub-variant — STRENGTHENING TO N=2 STRUCTURAL** ✅
   - 57c registered v51 N=1 (multica v15 cited "Vercel agent-skills import (first)" → v51 wiki of vercel-labs/agent-skills, 36-wiki gap)
   - **omo v52: OMC v27 wiki entry cited "oh-my-opencode" as 1 of 5 inspirational sources; v52 = wiki of oh-my-opencode/oh-my-openagent (renamed), 25-wiki gap (v27 → v52)**
   - **Result:** 57c reaches **N=2 structural** at v52 — promotion-candidate at next mini-audit under structural-N=2 criterion (criterion #2). Sub-variant promotion analogous to Pattern #58 promotion at v42 mini-audit.

2. **Pattern #57 57a Direct citation strengthening N=5** ✅
   - omo's `docs/superpowers/` subdirectory (with `plans/` + `specs/`) directly references **obra/superpowers (Storm Bear v2 wiki subject)** as integrated skill-system component
   - 57a was N=4 pre-v52; reaches **N=5** at v52
   - Strengthening (no status change; already CONFIRMED v50 mini-audit)

3. **Pattern #73 73a Korean-Regional-Archetype T1 strengthening** ✅
   - 73a Korean T1: OMC v27 (Yeachan Heo, Seoul) + omo v52 (YeonGyu-Kim, Seoul Sionic AI) = N=2 Korean-Seoul-T1 within 73a
   - Sub-observations (within-pattern, NOT new candidates per consolidation-forward discipline):
     - **Korean-`oh-my-*`-naming-convention**: oh-my-claudecode (Yeachan v27) + oh-my-codex (Yeachan sibling) + oh-my-opencode→oh-my-openagent (YeonGyu v52) → ≥3 explicit `oh-my-*` repos by 2 Korean Seoul authors
     - **Korean-Sisyphus-mythology-naming**: oh-my-claude-sisyphus (OMC v27 npm name) + Sisyphus + Sisyphus Labs (omo v52) — both Korean projects reference Sisyphus mythology
     - **Korean-OpenClaw-fork-extension**: both fork OpenClaw runtime
   - Strengthening evidence within Pattern #73; sub-observations documented but NOT registered standalone (consolidation-forward).

4. **Pattern #58 Branding-Package Divergence — N=5 STRENGTHENING + NEW SUB-VARIANT 58c**
   - 58a: rename-without-npm-rename (OMC v27)
   - 58b: rebrand-with-transitional-preserve (ruflo v42)
   - **58c NEW v52: rebrand-repo-keep-npm-package + dual-bin-alias** — repo `oh-my-opencode` → `oh-my-openagent` but `package.json.name` still `oh-my-opencode` + dual-bin alias both `oh-my-opencode` AND `oh-my-openagent` shell to same `bin/oh-my-opencode.js`
   - N=1 stale-flagged at registration (v52 → v57 stale-check / v62 retire-check); promotion-ready at N=2 structural
   - **Sub-variant within already-CONFIRMED #58 (PROMOTED v42 mini-audit)** — analogous to v51 Pattern #22 22d sub-variant registration

5. **Pattern #29 License-Category Diversity — NEW custom-non-OSI-non-commercial-restriction sub-context**
   - SUL-1.0 (Sustainable Use License Version 1.0) — custom non-OSI license restricting commercial use to "internal business purposes" + "distribute free of charge for non-commercial purposes"
   - Family-similar to PolyForm Noncommercial (GitNexus v33 Pattern #72) but distinct license text/family
   - **Decision:** Strengthen Pattern #29 with NEW sub-context "custom-non-OSI-non-commercial-restriction" (N=2 with PolyForm GitNexus v33). Do NOT generalize Pattern #72 (different license families with different specific terms).
   - Promotion-candidate at next mini-audit under structural-N=2 if formalized

6. **Pattern #28 Multi-Provider AI Support strengthening** ✅
   - 6+ providers with explicit role-specialization: Claude Opus 4.7 (orchestration) / Kimi K2.5 + GLM 5 (orchestration alt) / GPT-5.4 (deep work) / Minimax (speed) / Gemini (creativity)
   - **Category-based routing** (visual-engineering / deep / quick / ultrabrain) instead of agent-picks-model — distinct from prior native-provider routing
   - 14th+ data point at #28 (post-v51 was 13th+)

7. **Pattern #50 Commercial-Funnel Companion strengthening — sisyphuslabs.ai sub-variant**
   - Multi-channel funnel: ohmyopenagent.com (homepage) + sisyphuslabs.ai (commercial incubation waitlist for "fully productized Sisyphus") + Sionic AI parent + Discord + npm packages + GitHub releases
   - Sub-variant **50d** observation: **incubation-waitlist-as-funnel-terminus** — separate commercial entity (Sisyphus Labs) with explicit "Join the waitlist" entrypoint embedded in OSS README; mechanism-distinct from 50a standard funnel / 50b recruiting / 50c bundled-product
   - **Decision:** Document as observational sub-variant within Pattern #50 (already CONFIRMED v31 mini-audit + REFINED v50 mini-audit with 3-sub-variant taxonomy). Register sub-variant 50d N=1 stale-flagged at v52 (v57 / v62 cadence). N=10+ data point overall for #50.

8. **Pattern #2 Distribution Evolution corpus-record at T1**
   - 11-platform Bun-compiled binary distribution (darwin × {arm64, x64, x64-baseline} + linux × {arm64, arm64-musl, x64, x64-baseline, x64-musl, x64-musl-baseline} + windows × {x64, x64-baseline}) + npm dual-bin + bunx + curl install
   - Most-platform-binary distribution at T1 in corpus (extends prior ollama v46 13+ surfaces but ollama is outside-scope)
   - Strengthening only (no new pattern)

9. **Pattern #18 MCP — 3-tier MCP system observation strengthening**
   - 3 tiers: built-in (Exa/Tavily websearch + context7 + grep_app) + Claude Code `.mcp.json` (`${VAR}` env expansion) + skill-embedded SKILL.md YAML (per-session stdio + HTTP)
   - **Counter-evidence to "MCP-as-flat-protocol"** — omo treats MCP as 3-tier scoping mechanism; observational Layer-2 strengthening within Pattern #18
   - **Pattern #18 OpenCode-primary observation strengthening** (registered v47 N=1 stale-risk-flagged) — omo IS OpenCode-primary (plugin extends OpenCode runtime); reaches **N=2** at v52 → un-stale + promotion-candidate at next mini-audit under structural-N=2

10. **Pattern #17 variant 1 solo-individual-publisher strengthening** ✅
    - YeonGyu-Kim solo + 133 public repos + Sionic AI employment + Sisyphus Labs separate commercial venture = solo-with-multiple-affiliations sub-observation
    - 19th+ data point for variant 1; observational only

11. **Pattern #19 archetype 2 methodology-lineage NEW influence node Can Bölük**
    - Hashline edit tool inspired by **oh-my-pi** (github.com/can1357/oh-my-pi) + cited blog **"The Harness Problem"** by Can Bölük (blog.can.ac/2026/02/12)
    - Corpus-first explicit Can Bölük citation as influence node within archetype 2 methodology-lineage
    - Joins Karpathy + Lance Martin + Anthropic-team-cluster + (others) as named influence nodes
    - Observational strengthening; not registered standalone (consolidation-forward)

12. **Pattern #27 Community-Viral strengthening**
    - 54K stars / ~4.7 months ≈ ~11.5K stars/month sustained-community-viral
    - Korean-Seoul-amplified sub-path (joins OMC v27 ~298 stars/day Korean sub-path)
    - 2nd-fastest viral velocity at T1 (after agency-agents v18) — but slower than awesome-design-md v25 ~3,000/day extreme-velocity outside-scope
    - Strengthening only

13. **Pattern #12 Governance-Depth refined-formulation 7TH COUNTER-EVIDENCE WIKI**
    - Solo-heavy-governance: AGENTS.md auto-generated 173-line + CLA.md + CONTRIBUTING.md (49+ lines including English-language-policy section) + LICENSE.md SUL-1.0 + README × 5 langs + manifesto.md + privacy/ToS legal docs
    - At solo-Korean-T1 = 7th counter-evidence wiki to v42 refined formulation (governance correlates with maturity-ambition + maintainer-philosophy + scale-tier, NOT solo-vs-corporate alone)
    - Refined formulation HOLDS strongly at N=7 counter-evidence

14. **Adversarial-Anthropic-positioning corpus-first explicit subject README claim**
    - README verbatim: *"Anthropic blocked OpenCode because of us. Yes this is true."* (links to X.com @thdxr post)
    - Continues: *"Claude Code's a nice prison, but it's still a prison. We don't do lock-in here. We ride every model."*
    - **Decision:** Document as observational subject-claim with verifiability caveat. Do NOT register standalone candidate. Possible overlap with retired Pattern #13 Autonomy-Framing OR within #51 Vibe-Coding Spectrum framing-axis (anti-lock-in pole).
    - Observation-only; flag in Phase 4b for future N=2 watch (would another framework explicitly position against a runtime?)

15. **Greek-mythology persona-design corpus-first cluster at T1**
    - 11 named agents: Sisyphus / Hephaestus / Prometheus / Oracle / Librarian / Atlas / Metis / Momus / Multimodal-Looker / Sisyphus-Junior + Explore
    - Corpus-first heavy Greek-mythology-cluster persona-design at T1 (prior personas in corpus: agency-agents v18 144 personalities like Whimsy Injector / Reality Checker — but those are descriptive role names, not unified mythology cluster)
    - Pattern #25 Personality-Driven Agent Design retired v27 — do NOT re-register; observation only (event-based aesthetic choice, not architectural)

### Overlap pre-check decisions

| Candidate hypothesis | Decision | Reasoning |
|---|---|---|
| Korean-`oh-my-*`-naming standalone candidate | REJECT (consolidation-forward) | Within Pattern #73 73a sub-observation; N=2 ≥3 explicit oh-my-* repos but mechanism is naming-convention not architectural |
| Korean-Sisyphus-mythology standalone candidate | REJECT (consolidation-forward) | Within Pattern #73 73a sub-observation; aesthetic/cultural rather than architectural pattern |
| Adversarial-Anthropic-positioning standalone candidate | REJECT (event-based observational) | Subject-claim N=1; possibly overlaps retired #13 Autonomy-Framing; observational only |
| Greek-mythology persona-cluster standalone candidate | REJECT (event-based aesthetic; #25 already retired) | Pattern #25 Personality-Driven retired v27; same retirement reasoning applies |
| 11-platform-binary distribution standalone | REJECT (within Pattern #2) | Strengthening only at N=11+ |
| SUL-1.0 license standalone | REJECT (within Pattern #29 sub-context) | Strengthen #29 with custom-non-OSI-non-commercial-restriction sub-context (joins Pattern #72 PolyForm; N=2 sub-context) |
| Multi-runtime category-based model routing standalone | REJECT (within Pattern #28) | Sub-axis observation within Pattern #28 multi-provider; does not justify new pattern |
| OpenClaw deep-fork extension archetype standalone | REJECT (within Pattern #18 OpenCode-primary observation) | Strengthens existing #18 sub-observation to N=2 promotion-candidate |

**Result: 0 new active candidates registered. 16-CONSECUTIVE-WIKI ZERO-REGISTRATION STREAK ACHIEVED (v37-v52)** — extends v51 15-streak; NEW LONGEST in corpus history.

## Phase 0.6 Stale candidate un-stale check

| Stale candidate | Pre-v52 status | omo v52 evidence | Decision |
|---|---|---|---|
| #45 Dual-Licensing | STALE since v28 | None (omo single SUL-1.0) | Stays stale |
| #52 Extreme-Viral-Velocity | STALE since v28 | None (~11.5K/month sub-extreme) | Stays stale |
| 3rd stale | STALE | None | Stays stale |

No un-stale triggered.

## Phase 0.9 Storm Bear meta-entity applicability check

PASS criteria check:
- **Direct pilot candidate?** MEDIUM-LOW — SUL-1.0 license blocks Storm Bear commercial Scrum coaching deployment; pilot-eval-only (personal/internal use)
- **Observational value?** HIGH — Korean ecosystem peer of OMC v27 + Pattern #57 57c N=2 promotion-candidate + Pattern #18 OpenCode-primary N=2 + 4-template AGENTS.md ensemble extension consideration + multi-runtime category-routing template
- **Meta-entity warranted?** YES — 2nd Korean-Seoul T1 in corpus + corpus-internal-recursion (omo cites obra/superpowers v2) + license-blocked-commercial caveat warrants vault-architectural lesson
- **Or utility library with no vault-level implication?** NO — has vault-architectural relevance (multi-runtime escape-hatch + skill-format reference)

**Decision:** Storm Bear meta-entity APPLICABLE — **41st consecutive Storm Bear meta-entity (v10-v52)**. Frame as "Korean ecosystem peer + multi-runtime escape hatch + license-blocked-commercial pilot caveat + Pattern #57 corpus-touches-its-own-citation observation".

## Primitive-count flagging (Phase 0.9 → Phase 5)

**Probed primitive-count: ~150-300 across 14 categories** (per AGENTS.md inventory):
- 26 tools (across 17 directories)
- 11 named agents
- 52 hooks across 5 tiers (Session 24 / Tool-Guard 14 / Transform 5 / Continuation 7 / Skill 2)
- 19 features
- 3-tier MCP (built-in + Claude Code .mcp.json + skill-embedded)
- 8 categories (visual-engineering / deep / quick / ultrabrain / + 4 more) with category-model-routing
- 11 platform binaries
- 14 overridable agent fields × 21 fields each
- 5-language docs
- Built-in skills (playwright / git-master / frontend-ui-ux / + custom)
- 7 GitHub Actions workflows (ci / publish / publish-platform / sisyphus-agent / refresh-model-capabilities / cla / lint-workflows)
- 32 Zod config schema files
- 1,766 TS source files / 377K LOC / 104 barrel index.ts
- Built-in commands (ultrawork / ultrawork-loop / start-work / init-deep / + others)

**Primitive-count tier: EXTREME** (consistent with ruflo v42 ~500 / aidevops v47 ~2,665 / awesome-claude-skills v50 EXTREME / shannon v45 YELLOW). 4-entity format with aggressive citation-not-replication required.

**Compression strategy adopted:**
- 4-entity allocation (Core product + Architecture+Distribution / OpenCode-Bun-platform-binaries / Korean ecosystem + Sisyphus Labs commercial + Pattern implications / 41st Storm Bear meta)
- Lossy compression accepted: per-tool details cite AGENTS.md WHERE TO LOOK table; per-hook details cite docs/reference/features.md; per-agent personality details cite README §Discipline Agents
- Citation-not-replication for: 26 tools enumeration / 52 hook breakdown / 19 features / per-platform-binary detail / Zod schema field detail / 1,766 TS file structure
- 5+ follow-up deep-dive wikis flagged for v2.2 consideration (Greek-mythology agent catalog / 26-tool catalog / 52-hook lifecycle / 11-platform-binary build pipeline / 3-tier MCP system architecture)

**Velocity expected:** ~3h-3h 30min (within EXTREME +50-75% tolerance band; v45 shannon YELLOW ~2h 30min / v42 ruflo EXTREME ~3h 40min / v47 aidevops EXTREME ~3h-3h 30min precedents).

## Cross-wiki references

**Direct corpus connections:**
- **OMC v27 Yeachan Heo** — Korean Seoul T1 ecosystem peer (Pattern #73 73a strengthening); cited "oh-my-opencode" as 1 of 5 inspirational sources (Pattern #57 57c N=2 promotion-candidate)
- **obra/superpowers v2 (Jesse Vincent)** — omo's `docs/superpowers/` subdir directly cites/integrates (Pattern #57 57a 5th data point)
- **paperclip v14** — autonomy-max framing comparison (paperclip "zero-human companies" vs omo manifesto "Human In The Loop = BOTTLENECK")
- **GitNexus v33 (Pattern #72 PolyForm Noncommercial)** — non-commercial-restriction custom license sibling for Pattern #29 sub-context formalization
- **vercel-labs/agent-skills v51** — most-recent T1 entrant + Pattern #57 57c sibling (v51 was 57c N=1; omo v52 is 57c N=2)
- **aidevops v47 / pi-mono v36 / claude-hud v35** — recent T1 sub-archetype peers (3-layer governance hierarchy 22c / multi-package monorepo / display utility)
- **graphify v16 / agency-agents v18 / multica v15 / paperclip v14** — prior OpenClaw-corpus-presence observations (Pattern #18 OpenCode-primary observation strengthens to N=2 with omo)

## v2.1 routine deviations / observations

- **Default branch `dev`** (not `main`/`master`) — first explicit `dev` default in T1 corpus; Phase 0 branch-fallback resolved cleanly per routine v2.1 §0.3
- **Subject-claim verification:** "Anthropic blocked OpenCode because of us" — flagged as subject-claim per README with caveat (verifiable via X.com @thdxr post link but third-party assertion); document with caveat in beginner guide ethical framing
- **Sisyphus Labs vs Sionic AI relationship:** Sisyphus Labs (sisyphuslabs.ai) appears separate venture from Sionic AI parent company — Sionic AI is YeonGyu's day-job employer; Sisyphus Labs is the omo-incubation commercial entity for "fully productized Sisyphus" waitlist. Treat as parallel commercial structures (similar to Composio Inc. parent of awesome-claude-skills v50)

## Pattern Library delta forecast

- **0 new active candidates** (consolidation-forward; 16-streak NEW LONGEST extends v51 15-streak)
- **2 NEW sub-variant registrations within existing patterns:**
  - Pattern #58 sub-variant 58c rebrand-repo-keep-npm-package + dual-bin-alias (N=1 stale-flagged v52 → v57/v62)
  - Pattern #50 sub-variant 50d incubation-waitlist-as-funnel-terminus (N=1 stale-flagged v52 → v57/v62)
- **Pattern #57 57c N=2 STRUCTURAL PROMOTION-CANDIDATE** at next mini-audit (joins v51 multica-citation; structural-N=2 criterion now met)
- **Pattern #18 OpenCode-primary observation N=2** un-stale + promotion-candidate at next mini-audit (registered v47 N=1; omo v52 = 2nd data point)
- **Pattern #29 NEW sub-context** custom-non-OSI-non-commercial-restriction (N=2 with PolyForm GitNexus v33) — promotion-candidate at next mini-audit
- **Pattern Library state forecast:** 38 confirmed + 18 active + 3 stale + 9 retired + 5 OT = unchanged structurally; ratio **18:38 = 0.474:1 PRESERVED 2nd post-v50-mini-audit cycle** (largest buffer 0.476 below 0.95:1 mini-audit trigger preserved)
- **10+ promotion candidates accumulated post-v52** (cumulative across v45-v52): #57 57c structural-N=2 + #18 OpenCode-primary structural-N=2 + #29 SUL-1.0 sub-context + carry-forward 9 from post-v51 — mini-audit warranted at next operator-trigger

## Phase 4b routing mode

**Primary mode: Pattern-test + within-variant strengthening + cross-corpus citation**
- Pattern #57 57c structural-N=2 promotion-candidate test (v51 + v52 = N=2 across 25-wiki gap)
- Pattern #73 73a Korean N=2 strengthening with sub-observations
- Pattern #58 58c sub-variant registration + #50 50d sub-variant registration
- Pattern #29 SUL-1.0 sub-context + Pattern #18 OpenCode-primary N=2

Secondary modes:
- Cross-corpus citation (omo cites obra/superpowers + cites v27 in reverse — meta-recursion)
- Counter-evidence-driven refinement (Pattern #12 7th counter-evidence wiki)
- Adversarial-positioning observational documentation (subject-claim caveat)

## Quality assertions

- All counts verified against source repo files (package.json + LICENSE.md + AGENTS.md + README.md + 5-lang README files + src/ directory listing + docs/ directory listing)
- License = SUL-1.0 confirmed via LICENSE.md text (Sustainable Use License Version 1.0; non-commercial-restriction)
- Adversarial-Anthropic claim flagged as subject-claim with caveat (verifiable via X.com link only; third-party assertion)
- 11-platform binary count verified via package.json optionalDependencies array
- 5-language README count verified via /bin/ls (en + ko + ja + zh-cn + ru)
- Default branch `dev` confirmed via AGENTS.md "Branch: dev" header
- Korean Seoul + Sionic AI affiliation confirmed via GitHub profile metadata (probe metadata) + Sisyphus Labs cited as separate venture in README

---

**Project status:** Phase 0 complete with full 12-axis classification + Pattern Library pre-check + 16-streak zero-registration achieved + EXTREME primitive-count tier + Storm Bear meta-entity applicability PASS + 41st consecutive meta-entity confirmed. Proceeding to Phase 1-6 deliverables.
