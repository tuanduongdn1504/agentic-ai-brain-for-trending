# (C) T1 14-way + OpenCode-first sub-archetype + Pattern implications

**Entity type:** Tier-comparative + sub-archetype formalization
**Tier:** T1 Agent-as-assistant (largest tier in corpus extends to N=14)

## T1 14-way structural matrix

| # | Wiki | Author | Stars | Created | Sub-archetype | Runtime-primary | Domains |
|---|---|---|---|---|---|---|---|
| 1 | **ECC** v1 | affaan-m | ~7K | 2024-Q4 | Feature-framework | Claude Code | 1 (coding) |
| 2 | **Superpowers** v2 | obra (Jesse Vincent) | ~7K | 2025-Q1 | Methodology + 7-stage workflow | Claude Code | 1 (coding) |
| 3 | **gstack** v3 | garrytan (Garry Tan, YC) | ~6K | 2025-Q1 | Virtual engineering team | Claude Code | 1 (coding) |
| 4 | **GSD** v5 | gsd-build (TÂCHES) | ~5K | 2025-Q2 | SDD methodology + 14-harness support | Multi-runtime | 1 (coding) |
| 5 | **BMAD** v11 | bmad-code-org (LLC) | 45K | 2024-Q4 | BMM methodology + 12-15 agents + 5 modules | Multi-runtime | 1 (agile dev) |
| 6 | **codymaster** v12 | tody-agent (Tody Le, VN) | 38 | 2025-Q4 | 79-skill VN-authored memory-tier framework | Claude Code | 1 (coding) |
| 7 | **spec-kit** v17 | github (Microsoft official) | 89.2K | 2025-Q3 | Constitutional SDD + 9-article governance | Multi-runtime | 1 (coding) |
| 8 | **agency-agents** v18 | msitarzewski (solo) | 82.9K | 2025-Q1 | 144-personality-driven-agent agency | Multi-runtime | 12-14 (cross-domain breadth — Engineering / Marketing / Sales / Game / Spatial / etc.) |
| 9 | **OMC** v27 | Yeachan-Heo (Korean solo) | 30K | 2026-Q1 | 4-runtime orchestrator + 8-mode + 19-agent + plugin marketplace | Multi-runtime (4-way) | 1 (coding) |
| 10 | **claude-howto** v32 | luongnv89 (VN-diaspora) | 28K | 2025-Q4 | 10-tutorial-module + 45-template + interactive self-assessment | Claude Code | 1 (coding tutorial) |
| 11 | **claude-code-best-practice** v34 | shanraisshan (Pakistani) | 47K | 2025-Q4 | 82-tip aggregator + Anthropic-team-aggregator lineage | Claude Code | 1 (coding aggregator) |
| 12 | **claude-hud** v35 | jarrodwatts (Australian) | 20K | 2026-Q1 | Display-layer statusline plugin | Claude Code | 1 (display utility) |
| 13 | **pi-mono** v36 | badlogic (Mario Zechner, Austrian) | 38.9K | 2025-Q3 | Solo-monorepo-7-package + lockstep versioning | Standalone (Claude Code + Codex via skills) | 1 (coding agent) |
| 14 | **aidevops** v47 (THIS) | marcusquinn (Marcus Quinn, Jersey UK) | 212 | 2025-Q4 (Nov 9) | **OpenCode-first cross-domain multi-agent AI-DevOps platform** | **OpenCode-PRIMARY** | **13** (corpus-broadest tied with agency-agents) |

## T1 archetype distribution

| Archetype | Count |
|---|---|
| Solo-coding-methodology | 5 (ECC + SP + gstack + GSD + BMAD) |
| Solo-skill-library | 2 (codymaster + agency-agents) |
| Solo-tutorial-aggregator | 2 (claude-howto + claude-code-best-practice) |
| Corporate-official | 1 (spec-kit GitHub) |
| Solo-display-plugin | 1 (claude-hud) |
| Solo-multi-runtime-orchestrator | 1 (OMC) |
| Solo-monorepo-flagship | 1 (pi-mono) |
| **Solo-OpenCode-first-cross-domain-platform** | **1 (aidevops v47 NEW)** |

**T1 has 13 distinct sub-archetypes at N=14. aidevops establishes 13th sub-archetype.**

## Runtime-primary distribution

| Runtime-primary | Count |
|---|---|
| Claude Code primary | 8 (ECC / SP / gstack / codymaster / claude-howto / claude-code-best-practice / claude-hud / BMAD partial) |
| Multi-runtime balanced | 4 (spec-kit 30+ harnesses / agency-agents 11 / OMC 4-way / GSD 14-harness) |
| Standalone (own runtime, no MCP) | 1 (pi-mono) |
| **OpenCode-PRIMARY (Claude Code via redirect-shim)** | **1 (aidevops v47 NEW)** |

**aidevops v47 = first T1 entrant where Claude Code is explicitly secondary** (CLAUDE.md = 440B compatibility shim). All prior 13 entrants either Claude-Code-primary OR multi-runtime-balanced.

## Domain-coverage distribution

| Domain count | Examples |
|---|---|
| 1 (coding-only) | ECC / SP / gstack / GSD / BMAD / codymaster / spec-kit / claude-howto / claude-code-best-practice / claude-hud / OMC / pi-mono — 12 of 14 |
| 12-14 (cross-domain personality-driven) | agency-agents v18 |
| **13 (cross-domain functional-orchestrators)** | **aidevops v47 NEW** |

**Cross-domain breadth at T1:** agency-agents v18 (personality-driven roles: Whimsy Injector / Reality Checker / Reddit Community Builder) vs aidevops v47 (functional-domain orchestrators: SEO / Marketing / Legal / Health with deep tooling).

**Distinction:**
- **agency-agents** = WIDE personality-coverage with shallow per-agent tooling (each agent is a markdown role file)
- **aidevops** = WIDE functional-domain-coverage with DEEP per-agent tooling (each domain has dozens of subagents + helper scripts + service integrations + MCP filtering)

## OpenCode-first sub-archetype — formal definition

**7 test criteria for "OpenCode-first plugin (T1)" sub-archetype:**

1. ✅ README explicitly designates OpenCode as recommended/tested-first runtime
2. ✅ Framework code lives in OpenCode plugin format (`.opencode/` + `.agents/plugins/opencode-aidevops/`)
3. ✅ Claude Code support exists but explicitly secondary (redirect-shim or compatibility layer)
4. ✅ OpenCode native features (OAuth, plugin compaction hooks, server-mode attach, SDK) are first-class architectural primitives
5. ✅ User onboarding flow explicitly directs to OpenCode (`/onboarding` slash command in OpenCode)
6. ✅ Documentation throughout uses OpenCode as default examples (not Claude Code)
7. ✅ Auth pool integrates with OpenCode native OAuth (Anthropic / OpenAI / Cursor / Google) rather than Claude API key

**N=1 at v47 (aidevops only).** Future T1 wikis matching all 7 criteria → strengthen to N=2.

**Within Pattern #18 Agent Runtime Standardization — sub-observation NEW:** OpenCode-as-primary T1 ecosystem-diversity data point. Pattern #18 currently confirmed at N=multi-data-points; aidevops adds runtime-of-choice diversification observation.

## AGENTS.md-authoritative-with-CLAUDE.md-shim — 3-layer governance hierarchy

**Pattern #22 corpus state pre-v47:** All prior 46 wiki subjects had CLAUDE.md as primary or co-equal with AGENTS.md (when AGENTS.md existed). v37 bizos established 327B AGENTS.md minimum + 11B CLAUDE.md alias (`@AGENTS.md`).

**v47 establishes corpus-first AGENTS.md-AUTHORITATIVE-WITH-CLAUDE.md-AS-EXPLICIT-COMPATIBILITY-SHIM inversion:**

| Layer | File | Size | Audience | Purpose |
|---|---|---|---|---|
| **Layer 0 (shim)** | `CLAUDE.md` | 440B | Anthropic Claude Code tools | "See AGENTS.md for the authoritative AI assistant guidance. This file exists for compatibility with Claude Code and other Anthropic tools that look for CLAUDE.md." |
| **Layer 0 (shim)** | `AGENT.md` | 420B | Singular-AGENT.md tools | "See AGENTS.md... This file exists for compatibility with AI tools that look for AGENT.md (singular)." |
| **Layer 1 (dev-guide)** | `AGENTS.md` | 3,038B | Contributors + AI dev assistants | Two-AGENTS.md model + dev lifecycle + design principles + security + quality + self-assessment |
| **Layer 2 (user-guide)** | `.agents/AGENTS.md` | ~18,000B | End-users (deployed to `~/.aidevops/agents/AGENTS.md` by setup.sh) | Full operational guide |

**Pattern #22 formulation extension proposed at next mini-audit:** add 3-layer governance hierarchy as sub-variant within Pattern #22 (originally "AGENTS.md as Industry Standard"). Document AGENTS.md-authoritative-with-CLAUDE.md-shim sub-variant as CORPUS-FIRST at v47.

## Cross-provider verification — Pattern #28 NEW sub-axis

**Pattern #28 Multi-Provider AI Support corpus state pre-v47:** N=11+ data points across routing/abstraction styles. All prior data points framed as **routing** (which provider/model handles a request) or **abstraction** (uniform interface over providers).

**v47 introduces verification-not-routing as NEW sub-axis:**
- **Routing** (prior #28 data points) — Choose which provider serves request based on cost / speed / capability
- **Abstraction** (prior #28 data points) — Uniform API over multiple providers (LiteLLM-style)
- **Verification** (NEW v47 data point) — Use second provider's model to verify first provider's output for high-stakes operations (cross-correlated-hallucination defense)

**Mechanism (verbatim from README):**
> "Same-provider models share training data and failure modes. A Claude hallucination is unlikely to be reproduced by Gemini or GPT, and vice versa."

**Implementation:** `pre-edit-check.sh` screens against high-stakes taxonomy → for critical/high → `verify-operation-helper.sh` sends operation context to second model (different provider) → verifier independently assesses safety → on disagreement: blocked (critical) or warned (high) → all decisions logged for audit.

**Cost optimization:** Cheapest model tier (haiku-equivalent).

**Pattern #28 formulation extension proposal at next mini-audit:** Add "verification-not-routing" as 3rd sub-axis (alongside routing + abstraction). Document v47 aidevops as N=1 inaugural data point on verification-not-routing axis.

## EXTREME primitive-count tier — corpus-record observation

| Wiki | Primitive count | Tier rank |
|---|---|---|
| ruflo v42 | ~500+ | 1st EXTREME |
| **aidevops v47** | **~2,665+ (1,792 .md + 873 .sh)** | **2nd EXTREME — NEW CORPUS-RECORD (5× ruflo)** |

**Methodology corpus-record observation:**
- Primitive count = `find .agents/ -name '*.md' \| wc -l` + `find .agents/ -name '*.sh' \| wc -l`
- Combined: 2,665 files across the deployed agentic surface
- Higher-level primitives: 13 domains + 22 commands + 23 workflows + 79 tool families + 52 services + 7 bundles + 11 hooks + 20 MCPs + 30+ external services + 6 imported skills + 8 quality platforms

**Velocity tolerance applied:** EXTREME tier ~3h to ~3h 30min (within v2.1 informal discipline +50-75% overhead band).

**Scope-compression decisions documented in CLAUDE.md Phase 0.9:**
- 900+ subagents → cite `subagent-index.toon`; do NOT enumerate
- 52 services → enumerate categories only
- 30+ integrations → cite README §"Comprehensive Service Coverage"
- 22 commands + 23 workflows → enumerate top-level only
- 20 MCPs → reproduce table once, do NOT replicate per-MCP detail
- 5 follow-up deep-dive wikis flagged for v2.2

## Pattern #19 4th individual-influence-node — Lance Martin (LangChain)

**Pattern #19 archetype 2 methodology-lineage 4-individual-influence-node graph corpus-COMPLETE at v47:**

| # | Individual | Corpus touchpoints | First citation |
|---|---|---|---|
| 1 | **Andrej Karpathy** | 5+ (autoresearch v10 / LLM Wiki pattern foundation / graphify v16 / Ollama v46 cross-corpus / rowboat v43 implicit) | v10 |
| 2 | **John Lam (jflam)** | 1 (spec-kit v17 explicit) | v17 |
| 3 | **Anthropic team cluster** (Boris Cherny + Dex Horthy + Cat Wu) | 4+ (claude-howto v32 + claude-code-best-practice v34 + ECC v1 + SP v2) | v32 |
| 4 | **Lance Martin (LangChain)** ⬅️ NEW v47 | 1 (aidevops v47 16-pattern table) | v47 |

**aidevops v47 corpus-completes 4-individual-influence-node graph at Pattern #19 archetype 2.**

## Pattern #57 Recursive Corpus Reference — 4th data point

**Base rate update:**
| Wiki | Cross-corpus citation type | Subject |
|---|---|---|
| OMC v27 | Self-aware (cites prior corpus subjects ECC v1 + Superpowers v2) | First |
| dive-into-llms v39 | Third-party-unaware (chapter 9 cites LlamaFactory v22) | 2nd |
| Ollama v46 | Compound-2-wiki (Pi integration cites pi-mono v36 + Karpathy autoresearch v10) | 3rd |
| **aidevops v47** | **Third-party-unaware compound-2-wiki** (CREDITS.md cites VoltAgent v25 awesome-design-md MIT + Google Stitch DESIGN.md v25 referenced) | **4th** |

**Pre-v47 base rate:** 3/46 = 6.5%
**Post-v47 base rate:** 4/47 = **8.5%**

**External validity signal:** Marcus Quinn third-party-unaware that VoltAgent/awesome-design-md was Storm Bear v25 wiki subject (13-month delayed validation across 4 wikis). Strengthens Storm Bear wiki-subject-selection external-validity.

**Pattern #57 confirmed-tier strengthening; no formulation change needed.**

## Pattern Library impact summary

| Pattern | Action | Notes |
|---|---|---|
| **#18** Agent Runtime Standardization | Strengthening + sub-observation | OpenCode-as-primary T1 plugin (CORPUS-FIRST sub-observation NEW) |
| **#19** Intellectual Lineage archetype 2 | Strengthening | Lance Martin 4th individual-influence-node + multi-source methodology lineage strongest-evidence wiki |
| **#22** AGENTS.md Industry Standard | Formulation extension proposal | 3-layer governance hierarchy CORPUS-FIRST AGENTS.md-authoritative-with-CLAUDE.md-shim sub-variant |
| **#28** Multi-Provider AI Support | Formulation extension proposal | Cross-provider VERIFICATION-not-routing as NEW 3rd sub-axis (alongside routing + abstraction); 4-provider OAuth pool data point |
| **#57** Recursive Corpus Reference | 4th data point | CREDITS.md cites VoltAgent v25 + Google Stitch v25 referenced; base rate 4/47 = 8.5% |
| **#17** Ecosystem-Layer variant 1 | Strengthening | 18th data point (Marcus 20-repo solo-multi-publisher with prior 3.3K-star flagship) |
| **#20** Solo-Scale Ceiling | NEW T1 row | "Cold-start-with-mature-framework-surface (212 / 5.5mo / ~2,665 primitives + commercial-positioning)" |
| **#29** MIT | Strengthening | 39th MIT observation |
| **#12** Governance-Depth refined v42 3-factor | Strengthening (counter-evidence reinforcement) | 4th counter-evidence wiki philosophy-dominates-scale (claude-hud v35 + pi-mono v36 + ruflo v42 + aidevops v47); refined formulation HOLDS |
| **#51** Vibe-Coding Spectrum | Confirmed strengthening | Anti-vibe-pole "Sane vibe-coding through structure" data point + GitHub description "Vibe-Coding is easy. DevOps is hard." |
| **#2** Distribution Evolution | Strengthening | 5-surface npm/Bun/Homebrew/curl/manual + verified npm provenance |
| **#27** Community-Viral Scale Path | Counter-evidence observational | Cold-start-mature-surface; 38 stars/month NOT viral |

**Promotion candidates at next mini-audit:**
- **Pattern #22** formulation extension (3-layer governance hierarchy + AGENTS.md-authoritative-with-shim sub-variant)
- **Pattern #28** formulation extension (verification-not-routing as 3rd sub-axis)

**Total registrations: 0 new active candidates / 0 new OBSERVATION-TRACKs.**

## 11-streak zero-registration achieved (CORPUS-RECORD)

v37-v47 = **11 consecutive wikis with zero new active candidates.** Extends prior corpus-record streak v37-v46 (10 consecutive). Consolidation-forward discipline maturing to text-book at year 1.5 of v2.1 era.

## Cross-references

- See **(C) aidevops core product**
- See **(C) Marcus Quinn solo-individual ecosystem**
- See **(C) Storm Bear meta-entity v47 — 36th consecutive**
- See **(C) v47 Phase 4b — T1 14-way + OpenCode-first + AGENTS.md inversion + cross-provider-verification + EXTREME tier** (primary deliverable)

---

*(C) Generated by Claude — T1 14-way + OpenCode-first sub-archetype entity for v47 aidevops*
