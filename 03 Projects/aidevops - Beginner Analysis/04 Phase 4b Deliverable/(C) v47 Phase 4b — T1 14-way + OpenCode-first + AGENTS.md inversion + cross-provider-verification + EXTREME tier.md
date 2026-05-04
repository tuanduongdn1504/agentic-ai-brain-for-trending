# (C) v47 Phase 4b primary deliverable

**Target:** T1 14-way comparison + OpenCode-first sub-archetype + AGENTS.md-authoritative inversion + cross-provider-verification (Pattern #28 NEW sub-axis) + EXTREME primitive-count corpus-record + Pattern #19 4th individual-influence-node Lance Martin + Pattern #57 4th data point + 11-streak zero-registration extension

**Wiki:** v47 aidevops (`marcusquinn/aidevops`)

---

## Part 1 — T1 extension to N=14

### 1.1 14-way comparison matrix (compact)

| # | Wiki | Author | Stars | Sub-archetype | Runtime-primary | Domains | Primitives |
|---|---|---|---|---|---|---|---|
| 1 | ECC v1 | affaan-m | ~7K | Feature-framework | Claude Code | 1 | ~50 |
| 2 | Superpowers v2 | obra | ~7K | Methodology+7-stage | Claude Code | 1 | ~50 |
| 3 | gstack v3 | garrytan | ~6K | Virtual-eng-team | Claude Code | 1 | ~30 |
| 4 | GSD v5 | gsd-build | ~5K | SDD+14-harness | Multi-runtime | 1 | ~80 |
| 5 | BMAD v11 | bmad-code-org (LLC) | 45K | BMM+5-modules+12-15 agents | Multi-runtime | 1 | ~100 |
| 6 | codymaster v12 | tody-agent (VN) | 38 | 79-skill VN-authored | Claude Code | 1 | 79 |
| 7 | spec-kit v17 | github (Microsoft) | 89.2K | Constitutional SDD+9-article | Multi-runtime 30+ | 1 | ~80 |
| 8 | agency-agents v18 | msitarzewski | 82.9K | 144-personality-driven-agency | Multi-runtime 11 | 12-14 | 144 |
| 9 | OMC v27 | Yeachan-Heo (Korean) | 30K | 4-runtime-orchestrator+8-mode+19-agent+plugin marketplace | Multi-runtime (4-way) | 1 | ~50 |
| 10 | claude-howto v32 | luongnv89 (VN-diaspora) | 28K | 10-tutorial+45-template+self-assessment | Claude Code | 1 | ~70 |
| 11 | claude-code-best-practice v34 | shanraisshan (Pakistani) | 47K | 82-tip-aggregator+Anthropic-team-lineage | Claude Code | 1 | ~100 |
| 12 | claude-hud v35 | jarrodwatts (Australian) | 20K | Display-layer-statusline | Claude Code | 1 (display) | ~70 |
| 13 | pi-mono v36 | badlogic (Mario Zechner Austrian) | 38.9K | Solo-monorepo-7-package+lockstep | Standalone (no MCP) | 1 | ~150-200 |
| **14** | **aidevops v47** | **marcusquinn (Marcus Quinn UK)** | **212** | **OpenCode-first cross-domain multi-agent AI-DevOps platform** | **OpenCode-PRIMARY** | **13** | **~2,665+** |

### 1.2 Distribution observations

**Sub-archetype distribution:** 13 distinct sub-archetypes at N=14 (only 1 partial overlap: agency-agents v18 + aidevops v47 both cross-domain BUT different agent-type — personality-driven roles vs functional-domain orchestrators).

**Runtime-primary distribution:**
- Claude Code primary: 8/14 (57%)
- Multi-runtime balanced: 4/14 (29%)
- Standalone: 1/14 (7%) (pi-mono v36)
- **OpenCode-PRIMARY: 1/14 (7%) — aidevops v47 (CORPUS-FIRST)**

**Author origin distribution:**
- US: 7/14 (ECC / SP / gstack / GSD / agency-agents / claude-hud-Australian-but-US-style ... )
- UK / Channel Islands: **1/14 (aidevops Marcus Quinn Jersey)** — 1st Channel-Island-author T1
- VN: 2/14 (codymaster Tody Le + claude-howto luongnv89-diaspora)
- Korean: 1/14 (OMC Yeachan-Heo)
- Pakistani: 1/14 (claude-code-best-practice Shayan Rais)
- Australian: 1/14 (claude-hud Jarrod Watts)
- Austrian: 1/14 (pi-mono Mario Zechner)

**Pattern #73 Regional-Archetype-Registry observation:** No new regional sub-variant from aidevops (Channel Islands UK; English-language-cluster; not divergent from US T1 baseline). Pattern #73 sub-variant 73a Korean / 73b VN / 73c Pakistani unchanged.

**Scale tier distribution at T1:**
- 1K-10K: 4 (ECC / SP / gstack / GSD)
- 10K-50K: 5 (BMAD / OMC / claude-howto / claude-code-best-practice / claude-hud)
- 50K-90K: 3 (agency-agents / spec-kit / pi-mono)
- **Cold-start (<300 stars) with mature surface: 1 (aidevops v47 — NEW)**

aidevops v47 occupies novel scale-archetype intersection: cold-start stars but mature ~2,665+ primitive surface.

---

## Part 2 — OpenCode-first plugin sub-archetype formal definition

### 2.1 7 test criteria

A T1 framework qualifies as **"OpenCode-first plugin"** if it satisfies ALL 7 criteria:

1. **README explicit OpenCode-recommended** — Project README explicitly designates OpenCode as recommended/tested-first runtime
2. **OpenCode plugin format** — Framework code lives in `.opencode/` directory + `plugins/opencode-<name>/` structure
3. **Claude Code as secondary** — Claude Code support exists but explicitly secondary (redirect-shim or minimal compatibility layer)
4. **OpenCode-native architecture** — OpenCode features (OAuth pool, plugin compaction hooks, server-mode attach, SDK) are first-class architectural primitives
5. **Onboarding via OpenCode** — User onboarding flow explicitly directs to OpenCode (`/onboarding` slash command in OpenCode TUI)
6. **OpenCode-default examples** — Documentation throughout uses OpenCode as default examples
7. **Auth via OpenCode native OAuth** — Auth integrates with OpenCode native OAuth (Anthropic + OpenAI + Cursor + Google) rather than direct API key

### 2.2 v47 aidevops satisfies all 7 criteria

| # | Criterion | Evidence in aidevops |
|---|---|---|
| 1 | README OpenCode-recommended | `Recommended setup: OpenCode + Claude models` (cited 30+ times in README) |
| 2 | OpenCode plugin format | `.opencode/server/api-gateway.ts` + `.opencode/tool/parallel-quality.ts` + `.agents/plugins/opencode-aidevops/` compaction plugin |
| 3 | Claude Code secondary | `CLAUDE.md` 440B redirect-shim ("This file exists for compatibility with Claude Code...") |
| 4 | OpenCode-native architecture | OpenCode OAuth + `opencode serve` warm-server attach + `@opencode-ai/sdk` parallel dispatch + plugin compaction hooks (`tool.execute.before` / `tool.execute.after`) |
| 5 | Onboarding via OpenCode | "New users: Start OpenCode and type `/onboarding`" |
| 6 | OpenCode-default examples | All command examples + workflow walkthroughs use OpenCode TUI |
| 7 | Auth via OpenCode OAuth | `aidevops model-accounts-pool add anthropic\|openai\|cursor\|google` → OpenCode native OAuth |

**aidevops v47 = N=1 inaugural OpenCode-first plugin T1 sub-archetype.**

### 2.3 Pattern #18 sub-observation NEW

**Pattern #18 Agent Runtime Standardization corpus state pre-v47:** Confirmed; multiple data points across runtime-of-choice diversity (Claude Code primary majority + multi-runtime balanced minority + standalone pi-mono v36).

**v47 introduces NEW within-Pattern-#18 sub-observation: OpenCode-as-primary T1 plugin (N=1).** Documents runtime-of-choice diversification at T1 layer continuing to evolve (vs convergence on Claude Code).

**Future watch:** If 2nd OpenCode-first T1 framework appears → strengthen sub-observation to N=2.

---

## Part 3 — AGENTS.md-authoritative inversion + 3-layer governance hierarchy

### 3.1 Pattern #22 corpus state pre-v47

| Wiki | AGENTS.md presence | CLAUDE.md role | Hierarchy |
|---|---|---|---|
| Earlier T1 (ECC v1 / SP v2 / gstack v3 / GSD v5) | Mostly absent | Primary | CLAUDE.md only |
| BMAD v11 / spec-kit v17 / agency-agents v18 | Some | Primary or co-equal | Both files; CLAUDE.md ≥ AGENTS.md |
| codymaster v12 / claude-howto v32 / claude-code-best-practice v34 | Sometimes | Primary | CLAUDE.md primary, AGENTS.md supplementary |
| claude-hud v35 / pi-mono v36 | Yes | Primary | Both files; CLAUDE.md primary |
| OMC v27 | Yes | Co-equal | Both files; balanced |
| bizos v37 | 327B (minimum-viable) | 11B `@AGENTS.md` alias | AGENTS.md present, CLAUDE.md alias |
| ruflo v42 | 20.7KB | 38.9KB primary | CLAUDE.md primary at scale |

**v47 establishes corpus-first AGENTS.md-AUTHORITATIVE-WITH-CLAUDE.md+AGENT.md-REDIRECT-SHIMS inversion.**

### 3.2 v47 3-layer governance hierarchy

| Layer | File | Size | Audience | Verbatim purpose |
|---|---|---|---|---|
| **Layer 0 (shim)** | `CLAUDE.md` | 440B | Anthropic Claude Code tools | "See AGENTS.md for the authoritative AI assistant guidance. This file exists for compatibility with Claude Code..." |
| **Layer 0 (shim)** | `AGENT.md` | 420B | Singular-AGENT.md tools | "See AGENTS.md... This file exists for compatibility with AI tools that look for AGENT.md (singular)." |
| **Layer 1 (dev-guide)** | `AGENTS.md` (root) | 3,038B | Contributors + AI dev assistants | Quick-ref + Two-AGENTS.md model + dev lifecycle + design principles + security + quality + self-assessment |
| **Layer 2 (user-guide)** | `.agents/AGENTS.md` | ~18,000B | End-users (deployed to `~/.aidevops/agents/AGENTS.md` by setup.sh) | Full operational guide (runtime support / task lifecycle / model tiers / git workflow / agent routing / memory recall / security) |

### 3.3 Pattern #22 formulation extension proposal at next mini-audit

**Current Pattern #22 statement:** "AGENTS.md as Industry Standard — cross-framework convention (multica + gws + graphify + spec-kit all use AGENTS.md filename)."

**Proposed extension:**

> Add 3-layer governance hierarchy as sub-variant within Pattern #22:
> - Sub-variant 22a: AGENTS.md absent, CLAUDE.md primary (early T1 corpus)
> - Sub-variant 22b: AGENTS.md present, CLAUDE.md primary or co-equal (most T1 corpus)
> - Sub-variant 22c: AGENTS.md authoritative + CLAUDE.md/AGENT.md redirect-shims (NEW v47 — aidevops establishes 3-layer hierarchy: Layer 0 shims → Layer 1 dev-guide → Layer 2 user-guide deployed)
>
> **Document AGENTS.md-authoritative-with-CLAUDE.md-shim sub-variant 22c as CORPUS-FIRST at v47.**

**Promotion-readiness:** Single data point (N=1) at v47. Promotion-candidate if 2nd subject appears. Document sub-variant in next mini-audit even at N=1 (reflects observable corpus shift).

---

## Part 4 — Cross-provider verification (Pattern #28 NEW sub-axis)

### 4.1 Pattern #28 corpus state pre-v47

**Confirmed at multiple data points** (N=11+) across two prior sub-axes:

| Sub-axis | Description | Examples |
|---|---|---|
| **Routing** | Choose which provider/model based on cost/speed/capability per task | Pattern #28 confirmed wikis with cost-aware routing |
| **Abstraction** | Uniform API over multiple providers | LiteLLM (TrendRadar v19 / crawl4ai v29 fork) |

### 4.2 v47 introduces NEW 3rd sub-axis: VERIFICATION

**Aidevops cross-provider verification mechanism (verbatim from README §"Multi-Model Verification: Cross-Provider Safety"):**

> "High-stakes operations are verified by a second AI model from a different provider before execution. This catches single-model hallucinations before destructive operations cause irreversible damage."

**Risk taxonomy:**
| Risk | Examples | Action |
|---|---|---|
| Critical | `git push --force` to main, `DROP DATABASE`, production deploy | Blocked unless second model agrees |
| High | Force push feature branch, data migration, secret exposure | Warned, verification recommended |
| Medium | Bulk file deletion, config changes | Logged |
| Low | Normal edits, test runs | No verification |

**Mechanism:**
1. `pre-edit-check.sh` screens against high-stakes taxonomy
2. For critical/high → `verify-operation-helper.sh` sends operation context to second model (different provider than primary)
3. Verifier independently assesses safety
4. On disagreement: blocked (critical) or warned (high)
5. All decisions logged for audit

**Theoretical foundation:** *"Same-provider models share training data and failure modes. A Claude hallucination is unlikely to be reproduced by Gemini or GPT, and vice versa."*

**Cost optimization:** Cheapest model tier (haiku-equivalent). Marginal cost per check.

**Configuration:** `.agents/reference/high-stakes-operations.md`. Opt-out: `VERIFY_ENABLED=false` (not recommended).

### 4.3 Pattern #28 formulation extension proposal at next mini-audit

**Current Pattern #28 statement (rough):** Multi-Provider AI Support — frameworks support multiple AI providers via routing or abstraction.

**Proposed extension:**

> Pattern #28 has 3 sub-axes:
> - **Routing** (N=many): Choose provider per task based on cost/speed/capability (Pattern #28 majority data points)
> - **Abstraction** (N=few): Uniform API over multiple providers (LiteLLM / native multi-SDK)
> - **Verification** (N=1 NEW v47): Use second provider's model to verify first provider's output for high-stakes operations (cross-correlated-hallucination defense)
>
> v47 aidevops = N=1 inaugural data point on verification-not-routing axis. Document NEW sub-axis as CORPUS-FIRST.

**Promotion-readiness:** N=1 inaugural; document at next mini-audit. Future N=2 data point promotes verification sub-axis to confirmed-tier within Pattern #28.

### 4.4 4-provider OAuth pool data point

**Aidevops auth pool integrates with OpenCode native OAuth across 4 providers:**

| Provider | Auth method | Subscription tier |
|---|---|---|
| Anthropic | OpenCode native OAuth | Claude Pro / Max |
| OpenAI | OAuth | ChatGPT Plus / Pro |
| Cursor | Local IDE state read + gRPC proxy | Cursor Pro |
| Google | OAuth ADC bearer token | Google AI Pro / Ultra / Workspace |

**LRU rotation + per-provider cooldowns + auto-rotate on 429 + failure isolation (Google failure ≠ Anthropic failure).**

**CLI:** `aidevops model-accounts-pool [add|status|check|rotate|reset-cooldowns|list]`.

**Pattern #28 routing-axis data point:** subscription-rotation as cost-optimization mechanism (NEW within routing sub-axis: rotate-user-owned-subscriptions vs API-key-pay-per-token). Strengthening within Pattern #28; not separate observation.

---

## Part 5 — EXTREME primitive-count tier (NEW CORPUS-RECORD)

### 5.1 Primitive-count discipline (v2.1 informal §"Primitive-count flagging")

**Tiers (per v2.1 inception session 41):**
- **GREEN** baseline (~50-100 primitives) — standard 4-entity wikis
- **YELLOW** band (~120-200) — 25-33% velocity overhead
- **RED** band (~200-400) — 50-75% velocity overhead
- **EXTREME** tier (~500+) — 100%+ velocity overhead; aggressive citation-not-replication required

### 5.2 Corpus-record observation

| Wiki | Primitive count | Tier rank |
|---|---|---|
| ruflo v42 | ~500+ | 1st EXTREME |
| **aidevops v47** | **~2,665+ (1,792 .md + 873 .sh in `.agents/`)** | **2nd EXTREME — NEW CORPUS-RECORD; 5.3× ruflo** |

### 5.3 v47 primitive inventory

**Files in `.agents/`:**
- 1,792 markdown files (instructions + agent definitions + subagent specs + tool docs + reference material)
- 873 shell scripts (helpers + commands + hooks + automation)
- = **~2,665 primitive files** before counting JSON configs / YAML / source code in `.opencode/`

**Higher-level primitives:**
- 13 specialist domain agents
- 22 commands at `.agents/commands/` top-level
- 23 workflows at `.agents/workflows/`
- 79 tool families at `.agents/tools/`
- 52 service integrations at `.agents/services/`
- 7 project bundles at `.agents/bundles/`
- 11 git hooks at `.agents/hooks/`
- 20 MCP integrations
- 30+ external service integrations
- 6 imported skills (cloudflare-platform / heygen / remotion / video-prompt-design / animejs / caldav-calendar / proxmox-full)
- ~69 slash commands documented
- 8 external quality platforms (Codacy + CodeFactor + CodeRabbit + Sonar + Qlty + Bandit + secretlint + ShellCheck)
- 12+ root governance files (README/AGENTS/AGENT/CLAUDE/LICENSE/CONTRIBUTING/SECURITY/CODE_OF_CONDUCT/CHANGELOG/CREDITS/TODO/TERMS/MODELS/MODELS-PERFORMANCE/VERSION + 8 quality configs)

**Special-size files:**
- TODO.md = 1,031,375 bytes (1 MB) — corpus-largest task ledger
- CHANGELOG.md = 349,612 bytes (350 KB) — corpus-largest changelog
- README.md = 142,376 bytes (142 KB) — 2nd-largest README (after ruflo v42 280 KB)

### 5.4 Scope-compression decisions applied

**4-entity format preserved via aggressive citation-not-replication:**

| Primitive class | Compression strategy |
|---|---|
| 900+ subagents | Cite `subagent-index.toon` + per-domain directories; do NOT enumerate |
| 52 services | Enumerate categories only (Infrastructure / DNS / Git / AI / Security / Communications / Performance); cite `.agents/services/` |
| 30+ external integrations | Cite README §"Comprehensive Service Coverage"; reproduce category headings only |
| 22 commands + 23 workflows | Enumerate top-level only; cite `.agents/scripts/commands/` for per-command docs |
| 20 MCP integrations | Reproduce table from README §"MCP Integrations" once; do NOT replicate per-MCP detail |
| TODO.md 1 MB | Cite as task ledger; not summarized |
| CHANGELOG.md 350 KB | Cite latest version + corpus-relevant signals only |

**5 follow-up deep-dive wikis flagged for v2.2:**
1. **Pulse Supervisor Deep Dive** — autonomous orchestration architecture + 2-min cron + LLM-as-supervisor + struggle-ratio + circuit breaker
2. **13-Domain Specialist Agent Catalog** — per-domain workflow + subagent inventory + per-agent MCP filtering
3. **Mission Orchestration Architecture** — multi-day autonomous projects + milestone validation + budget tracking + Full vs POC modes
4. **Cross-Provider Verification Stack** — high-stakes operation taxonomy + multi-model safety + audit log + cost optimization
5. **TOON Format + Token-Efficient Serialization** — aidevops-originated format + 20-60% reduction analysis + adoption candidates

### 5.5 Velocity tolerance

**Measured velocity:** ~3h-3h 30min (within EXTREME tier +50-75% overhead band; ruflo v42 precedent ~3h 40min at +100% overhead).

**Plateau preserved:** v47 is **28th consecutive wiki at ~2-3.5h velocity plateau** (v6-v47).

---

## Part 6 — Pattern #19 4th individual-influence-node (Lance Martin / LangChain)

### 6.1 Pre-v47 Pattern #19 archetype 2 individual-influence-node graph

| # | Individual | Corpus touchpoints | First citation |
|---|---|---|---|
| 1 | **Andrej Karpathy** | 5+ (autoresearch v10 / LLM Wiki pattern foundation / graphify v16 inspired-by / Ollama v46 cross-corpus citation / rowboat v43 implicit) | v10 |
| 2 | **John Lam (jflam)** | 1 (spec-kit v17 explicit) | v17 |
| 3 | **Anthropic team cluster** (Boris Cherny + Dex Horthy + Cat Wu) | 4+ (claude-howto v32 + claude-code-best-practice v34 + ECC v1 + SP v2) | v32 |

### 6.2 v47 introduces 4th node: Lance Martin (LangChain)

**Aidevops README §"Agent Design Patterns" verbatim:**

> "aidevops implements proven agent design patterns identified by Lance Martin (LangChain)."

Source: x.com/RLanceMartin/status/2009683038272401719

**16-pattern documentation:** Each pattern mapped to aidevops implementation:

| Pattern | aidevops Implementation |
|---|---|
| Give Agents a Computer | `~/.aidevops/.agent-workspace/` + 873+ helper scripts |
| Multi-Layer Action Space | Per-agent MCP filtering (~12-20 tools each) |
| Knowledge Graph Routing | `subagent-index.toon` 900+ agents by domain/purpose/dependency |
| Progressive Disclosure | Subagent routing + YAML frontmatter + read-on-demand |
| Offload Context | `.agent-workspace/work/[project]/` for persistence |
| Cache Context | Stable instruction prefixes for prompt caching |
| Isolate Context | Sub-agents w/ separate windows + tool permissions |
| Multi-Agent Orchestration | TOON mailbox + agent registry + supervisor dispatch |
| Compaction Resilience | OpenCode plugin injects dynamic state at compaction |
| Ralph Loop | `/full-loop` + `full-loop-helper.sh` |
| Evolve Context | `/remember` + `/recall` w/ SQLite FTS5 + opt-in semantic search |
| Pattern Tracking | `/patterns` + `memory-helper.sh` |
| Token-Efficient Serialisation | TOON format (20-60% reduction) |
| Cost-Aware Routing | `model-routing.md` 7-tier + `/route` |
| Model Comparison | `/compare-models` + `/compare-models-free` |
| Response Scoring | `/score-responses` w/ structured criteria |

### 6.3 Pattern #19 corpus-COMPLETE 4-node graph at v47

**4-node individual-influence-node graph CORPUS-COMPLETE:**

| # | Individual | Domain | Stylistic signature |
|---|---|---|---|
| 1 | Andrej Karpathy | LLM research + education | "From scratch" pedagogical depth + Markdown LLM Wiki |
| 2 | John Lam (jflam) | SDD methodology | Constitutional governance + spec-driven |
| 3 | Anthropic team cluster | Claude Code platform | Engineering-team-aggregator best-practices |
| 4 | **Lance Martin (LangChain)** ⬅️ NEW v47 | Agent design patterns | 16-pattern catalog mapping LLM-agent architecture |

**Pattern #19 archetype 2 methodology-lineage** has 4 distinct individual-influence-node sources, all corpus-COMPLETE within their archetype style. **No new archetype likely without N=2-data-points-required-criterion data emerging.**

---

## Part 7 — Pattern #57 Recursive Corpus Reference 4th data point

### 7.1 Base rate update

**Pre-v47:** 3 cross-corpus citation data points / 46 wikis = 6.5% base rate.

**v47 contribution:** CREDITS.md §"Design Library (Brand Examples)" cites **VoltAgent/awesome-design-md (v25 wiki subject)** + **Google Stitch DESIGN.md** (v25 referenced).

**Verbatim CREDITS.md citation:**

> "VoltAgent/awesome-design-md (MIT License) — Curated collection of DESIGN.md files extracted from popular websites.
> Repository: https://github.com/VoltAgent/awesome-design-md
> 55 brand design system examples imported into `.agents/tools/design/library/brands/`
> Original preview HTML templates informed our parameterised preview template"

**Citation type:** Third-party-unaware compound-2-wiki (Marcus Quinn does NOT know v25 was Storm Bear wiki subject).

**Post-v47 base rate:** 4/47 = **8.5%**.

### 7.2 4-data-point base rate trajectory

| Wiki | Citation type | Subjects |
|---|---|---|
| OMC v27 | Self-aware (cites prior corpus subjects) | ECC v1 + Superpowers v2 |
| dive-into-llms v39 | Third-party-unaware | LlamaFactory v22 |
| Ollama v46 | Compound-2-wiki | pi-mono v36 + Karpathy autoresearch v10 |
| **aidevops v47** | **Third-party-unaware compound-2-wiki** | **VoltAgent/awesome-design-md v25 + Google Stitch v25 referenced** |

**Pattern #57 corpus-strengthening:** External-validity signal for Storm Bear wiki-subject-selection. v25 awesome-design-md (extreme-viral 60K stars in 20 days) chosen as wiki subject during the period when its design library was being adopted by another author. 13-month delayed validation pathway across 4 data points.

**Future watch:** TOON format adoption by other corpus subjects → aidevops becomes upstream node in cross-corpus citation graph (parallel to LlamaFactory v22 → dive-into-llms v39 chapter 9).

---

## Part 8 — 11-streak zero-registration milestone (CORPUS-RECORD)

### 8.1 Streak history

| Wiki | Active candidates registered | Streak length |
|---|---|---|
| v37 bizos | 0 | 1 |
| v38 DeepTutor | 0 | 2 |
| v39 dive-into-llms | 0 | 3 |
| v40 claude-context | 0 | 4 |
| v41 browser-use | 0 | 5 |
| v42 ruflo | 0 | 6 |
| v43 rowboat | 0 | 7 |
| v44 magika | 0 | 8 |
| v45 shannon | 0 | 9 |
| v46 Ollama | 0 | 10 |
| **v47 aidevops** | **0** | **11 (NEW CORPUS-RECORD)** |

**11 consecutive wikis with zero new active candidates.** Extends prior corpus-record streak v37-v46 (10 consecutive). Consolidation-forward discipline matures to text-book at year 1.5+ of v2.1 era.

### 8.2 v47 demonstrates discipline mechanism

**14+ candidate observations evaluated; ALL routed to within-existing-pattern strengthening:**

| Observation | Disposition |
|---|---|
| OpenCode-first plugin sub-archetype | Within-Pattern-#18 sub-observation NEW |
| AGENTS.md-authoritative-with-CLAUDE.md-shim | Within-Pattern-#22 formulation extension proposed |
| Cross-provider verification | Within-Pattern-#28 NEW sub-axis proposed |
| Lance Martin LangChain citation | Within-Pattern-#19 archetype 2 4th individual-influence-node |
| VoltAgent/awesome-design-md citation | Pattern #57 4th data point |
| 13-domain cross-domain coverage | T1 sub-archetype observation (not pattern) |
| 8-tool external quality stack | Pattern #12 governance-depth strengthening |
| 11 pre-push hooks | Within-Pattern-#12 strengthening |
| TOON format (aidevops-originated) | Future Pattern #57 watch (not registered) |
| 4-provider OAuth pool | Within-Pattern-#28 routing-axis data point |
| Voice Bridge ~6-8s | T1 first-class voice-input observation (not pattern) |
| Cisco Skill Scanner integration | Within-Pattern-#18 supply-chain security sub-observation |
| 30+ service integrations | Within-Pattern-#2 distribution surfaces |
| ~2,665 EXTREME primitive count | Methodology contribution (not pattern) |
| Cold-start-with-mature-surface (212 / 5.5mo) | Pattern #20 dictionary new T1 row |

**0 new active candidates registered. 0 new OBSERVATION-TRACKs registered.**

---

## Part 9 — Pattern Library impact summary (compact)

| Pattern | Action | Notes |
|---|---|---|
| **#18** Agent Runtime Standardization | Strengthening + sub-observation NEW | OpenCode-as-primary T1 plugin (CORPUS-FIRST sub-observation) |
| **#19** Intellectual Lineage archetype 2 | Strengthening | Lance Martin 4th individual-influence-node + multi-source methodology lineage strongest-evidence wiki |
| **#22** AGENTS.md Industry Standard | Formulation extension proposal | 3-layer governance hierarchy + AGENTS.md-authoritative-with-CLAUDE.md-shim sub-variant 22c CORPUS-FIRST |
| **#28** Multi-Provider AI Support | Formulation extension proposal | Cross-provider VERIFICATION-not-routing as 3rd sub-axis NEW; 4-provider OAuth pool routing-axis data point |
| **#57** Recursive Corpus Reference | 4th data point | CREDITS.md cites VoltAgent v25 + Google Stitch v25 referenced; base rate 4/47 = 8.5% |
| **#17** Ecosystem-Layer variant 1 | Strengthening | 18th data point (Marcus 20-repo solo-multi-publisher with prior 3.3K-star flagship) |
| **#20** Solo-Scale Ceiling | NEW T1 row | "Cold-start-with-mature-framework-surface (212 / 5.5mo / ~2,665 primitives)" |
| **#29** MIT | Strengthening | 39th MIT observation |
| **#12** Governance-Depth refined v42 3-factor | Strengthening (counter-evidence reinforcement) | 4th counter-evidence wiki philosophy-dominates-scale (claude-hud v35 + pi-mono v36 + ruflo v42 + aidevops v47); refined formulation HOLDS |
| **#51** Vibe-Coding Spectrum | Confirmed strengthening | Anti-vibe-pole structural-discipline data point |
| **#2** Distribution Evolution | Strengthening | 5-surface npm/Bun/Homebrew/curl/manual + verified npm provenance |
| **#27** Community-Viral Scale Path | Counter-evidence observational | Cold-start-mature-surface; 38 stars/month NOT viral |

**Promotion candidates at next mini-audit:**
1. **Pattern #22** formulation extension (3-layer governance hierarchy + AGENTS.md-authoritative sub-variant 22c)
2. **Pattern #28** formulation extension (verification-not-routing as 3rd sub-axis)

**Total registrations: 0 new active candidates / 0 new OBSERVATION-TRACKs.** 11-streak zero-registration extends.

---

## Part 10 — Strategic implications + recommendations

### 10.1 Corpus state post-v47 (forecast)

| Metric | Pre-v47 | Post-v47 |
|---|---|---|
| Confirmed patterns | 37 | 37 (unchanged) |
| Active candidates | 19 | 19 (unchanged — 11-streak preserved) |
| Stale candidates | 3 | 3 (unchanged) |
| Retired patterns | 9 | 9 (unchanged) |
| Observation-tracks | 5 | 5 (unchanged) |
| **Ratio (active:confirmed)** | **0.513:1** | **0.513:1 (PRESERVED 11th consecutive wiki)** |
| Buffer below 0.95:1 trigger | 0.437 | 0.437 (largest buffer in corpus history preserved) |

**11-streak ratio preservation = unprecedented.** Pattern Library health firmly NOT bottleneck.

### 10.2 Mini-audit candidates (NEXT mini-audit recommended)

**Patterns ready for promotion or formulation extension:**

1. **#22 formulation extension** (3-layer governance hierarchy + sub-variant 22c) — N=1 corpus-first; document at next mini-audit
2. **#28 formulation extension** (verification-not-routing as 3rd sub-axis) — N=1 corpus-first; document at next mini-audit

**Triggers (per v2.1):**
- Active candidate count: 19 (below 28 trigger; 9-candidate runway)
- Wiki-since-last-audit: v46 was last (1 wiki — well below 5-wiki natural-cadence trigger)
- Ratio: 0.513:1 (below 0.95:1 mini-audit / 1.05:1 full-audit triggers)

**Mini-audit recommended NOT triggered by formal v2.1 criteria but warranted to formalize Pattern #22 + #28 sub-variants while corpus-first observations are fresh.** Alternative: defer to natural-cadence mini-audit at v51 (5 wikis post-v46).

### 10.3 v27 diagnostic HIGH bundle status

**Sessions deferred:** v28 → v47 = **27 SESSIONS** (5.4× routine v2.1 operator-facing-backlog 5-session threshold).

**v47 reinforcement of urgency:**
- Aidevops AGENTS.md-authoritative + 3-layer model is **MOST DIRECT corpus template** for vault CLAUDE.md refactor (item #1)
- Aidevops 8-tool quality stack template for vault discipline (item #5 if Storm Bear publishes)
- Aidevops Lance Martin 16-pattern checklist provides skill audit framework

**Recommendation (12th consecutive force-continuation v36-v47):** STRONGLY RECOMMENDED to execute v27 diagnostic HIGH bundle before v48. Aidevops provides multiple direct-action templates. Estimated 6-8h session closes 2-4 of 5 items.

**Hybrid alternative:** v47 mini-audit (~30-45 min) → formalize Pattern #22 + #28 sub-variants → v27 HIGH bundle (~6-8h). Total: ~7-9h.

### 10.4 Storm Bear pilot ranking refresh

| # | Wiki | Storm Bear pilot value |
|---|---|---|
| 1 | claude-hud v35 | Display-utility direct adopt (5-min install) |
| 2 | spec-kit v17 | Methodology corporate-stable |
| 3 | claude-howto v32 | Tutorial / 4-week self-onboarding |
| 4 | OMC v27 | Multi-runtime + plugin marketplace |
| 5 | pi-mono v36 | Claude Code alternative |
| 6 | claude-code-best-practice v34 | 82-tip aggregator |
| **7** | **aidevops v47** **NEW** | **Pattern templates only (NOT framework adoption)** |
| 8 | rowboat v43 | Personal-productivity direct peer |
| 9 | claude-context v40 | Code-indexing pilot |
| 10 | graphify v16 | Code-indexing pilot |

aidevops v47 = **pilot rank #7** (above ruflo v42 commercial-bias-higher, agency-agents v18 no-commercial-layer; below 6 stronger pilots). Direct framework adoption NOT recommended; pattern-template-only adoption (AGENTS.md model + quality stack subset + Lance Martin checklist) HIGH leverage.

### 10.5 Future T1 watch points

**N=15+ T1 entrants might emerge from:**
1. **2nd OpenCode-first T1 plugin** → strengthens Pattern #18 OpenCode-primary sub-observation to N=2
2. **2nd AGENTS.md-authoritative-with-CLAUDE.md-shim T1** → promotes Pattern #22 sub-variant 22c at N=2
3. **2nd cross-provider-verification framework** → promotes Pattern #28 verification-not-routing sub-axis at N=2
4. **Cross-domain-personality-driven AND functional-orchestrator hybrid** → bridges agency-agents v18 + aidevops v47 sub-archetypes

**Corpus reaches N=14 at T1 = largest tier in Storm Bear corpus. T1 sub-archetype enumeration approaches saturation; next entrants must clear "genuinely different" bar (per v11 BMAD T1-closure precedent).**

---

## Part 11 — Closing observations

**v47 aidevops is the 47th wiki + 8th v2.1-era execution + 14th T1 entrant + corpus-record EXTREME primitive count + 11-streak zero-registration extension.**

**Most-distinctive corpus-firsts at v47:**
1. OpenCode-first T1 framework (CORPUS-FIRST)
2. AGENTS.md-authoritative-with-CLAUDE.md+AGENT.md-redirect-shims (CORPUS-FIRST 3-file inversion)
3. Cross-provider verification-not-routing (Pattern #28 NEW sub-axis)
4. EXTREME primitive-count corpus-record (~2,665+ vs ruflo ~500; 5×)
5. Lance Martin (LangChain) 4th individual-influence-node (Pattern #19 corpus-complete 4-node graph)
6. Pattern #57 4th data point (CREDITS.md cites v25 wiki subject; base rate 4/47 = 8.5%)
7. 11-streak zero-registration (CORPUS-RECORD; consolidation-forward discipline matures)

**Corpus state post-v47:** 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active. Ratio 19:37 = **0.513:1 PRESERVED 11th consecutive wiki** (largest buffer 0.437 below 0.95:1 mini-audit trigger preserved).

**Aidevops occupies novel corpus position:** cold-start-with-mature-framework-surface + commercial-positioning-without-paid-tier + OpenCode-first design. Future evolution likely involves either viral scale-up (rare for cold-start at month 5.5) OR sustained slow-growth as senior-dev-personal-platform.

---

*(C) Generated by Claude — Phase 4b primary deliverable for v47 aidevops*
