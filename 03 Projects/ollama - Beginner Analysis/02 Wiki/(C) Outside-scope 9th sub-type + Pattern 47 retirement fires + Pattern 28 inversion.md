# (C) Entity: Outside-scope 9th sub-type + Pattern #47 conditional retirement FIRES + Pattern #28 structural inversion + Pattern #18 Layer 0

> **Entity 3 of 4.** Primary pattern-implications entity. Documents the 3 structural events at v46: (1) 9th outside-scope sub-type formalization — LLM-inference-runtime; (2) Pattern #47 Vision-Based Browser Automation pre-registered conditional retirement trigger FIRES (corpus-first); (3) Pattern #28 Multi-Provider AI Support structural inversion observation (provider-being-consumed + multi-API-compat-as-runtime); (4) Pattern #18 Layer 0 runtime-bundled-launcher observation.

---

## 1. Summary of structural events at v46

4 structural events land in parallel:

1. **9th outside-scope sub-type formalized:** LLM-inference-runtime (Ollama) — distinct from 8 prior sub-types
2. **Pattern #47 conditional retirement trigger FIRES** — 1st pre-registered conditional retirement to actually fire in corpus history
3. **Pattern #28 structural inversion observation** — Ollama is the provider-being-consumed + implements 2 vendor-API-compat simultaneously (openai/ + anthropic/ subdirs)
4. **Pattern #18 Layer 0 runtime-bundled-launcher observation** — `ollama launch <runtime>` primitive at 170K-scale; potential 4-layer taxonomy extension at next audit

---

## 2. Outside-scope 9th sub-type: LLM-inference-runtime

### 2.1 7 test criteria (NEW formalization)

A repository fits the **LLM-inference-runtime** sub-type if it meets ALL 7 criteria:

1. **Runtime for running model weights at inference time.** Not training (rules out LlamaFactory v22 + Unsloth v23). Not producing weights (rules out fish-speech v20 foundation-model).
2. **Consumed BY agents as provider.** Structural inversion from typical Pattern #28 consumer-being-provider-abstracted framing.
3. **Local-first deployment model.** Single-machine install + daemon pattern (not cloud-only / SaaS-only).
4. **Multi-OS binary distribution.** macOS + Windows + Linux + Docker at minimum.
5. **Model registry + declarative model-packaging format.** E.g., Modelfile (Ollama), safetensors-with-config (others).
6. **Multi-provider-API-compat surface.** E.g., OpenAI-compat + Anthropic-compat subdirs simultaneously (OR at least one vendor-compat layer).
7. **Upstream integration with inference library.** E.g., llama.cpp integration + optional native backends (MLX / CUDA / ROCm / Metal).

### 2.2 Distinction from 8 prior outside-scope sub-types

| # | Sub-type | Founding wiki | Distinguishing vs LLM-inference-runtime |
|---|----------|---------------|------------------------------------------|
| 1 | education-aggregator | v8 build-your-own-x | Curated learning content (human-directed), not runtime |
| 2 | foundation-model | v20 fish-speech | **Produces weights**; Ollama consumes weights |
| 3 | prompt-leak-archive | v21 system-prompts-leaks | Archive/aggregation of extracted prompts; not runtime |
| 4 | training-infrastructure | v22 LlamaFactory + v23 Unsloth | **Trains weights**; Ollama runs inference only |
| 5 | design-template-aggregator | v25 awesome-design-md | Curated UI-template directory (absorbed into #68 v31 mini-audit); not runtime |
| 6 | MCP-server-aggregator | v31 awesome-mcp-servers | Curated MCP-server directory (absorbed into #68); not runtime |
| 7 | business-OS-as-product | v37 bizos (OT#74) | Domain-application product at cold-start; not LLM infrastructure |
| 8 | ML-security-classifier | v44 magika | File-type classifier; not LLM-serving runtime |
| **9** | **LLM-inference-runtime** | **v46 ollama** | **Runtime that SERVES LLMs at inference time; consumed BY agents** |

### 2.3 Outside-scope sub-type catalog as of v46

**10 total sub-types observed (9 distinct + 3 absorbed = 12 historical; 9 current distinct):**

Distinct + active:
1. education-aggregator → absorbed into #68 Awesome-List-Genre
2. foundation-model (fish-speech v20)
3. prompt-leak-archive (system-prompts-leaks v21)
4. training-infrastructure (LlamaFactory v22 + Unsloth v23 — N=2)
5. design-template-aggregator → absorbed into #68
6. MCP-server-aggregator → absorbed into #68
7. business-OS-as-product (bizos v37 — OT#74 observation-track)
8. ML-security-classifier (magika v44)
9. **LLM-inference-runtime (ollama v46)** NEW

### 2.4 Expected future observations

- Other LLM-inference runtimes: LMStudio, llama.cpp itself, text-generation-webui (Oobabooga), vLLM, llama-runner
- If N=2 arrives (e.g., LMStudio), could promote to named sub-type (analogous to training-infrastructure achieving N=2 at v23)
- Currently Ollama v46 is N=1 for this sub-type; stale-check at v51; retirement-check at v56

---

## 3. Pattern #47 conditional retirement trigger FIRES

### 3.1 Trigger preregistered at v42-deferred mini-audit (2026-04-24)

Per PATTERN_LIBRARY.md v42-deferred mini-audit documentation:

> "#47 Vision-Based Browser Automation (REFINED v29 + v41 + v42-deferred) | v24 | ✅ v42-deferred mini-audit refinement — formal statement upgraded to 3-point architectural spectrum (vision-primary Skyvern N=1 / hybrid browser-use N=1 / DOM-only crawl4ai N=1); stays CANDIDATE at N=1 vision-primary pole; **stale-check extension to v46 with pre-registered conditional retirement path** (if no 2nd vision-primary data point by v46, retire + replace with OBSERVATION-TRACK 'Browser-Agent Architectural-Approach 3-point spectrum') | v46 stale-check with conditional OBSERVATION-TRACK retirement"

### 3.2 Verification at v46

**Wikis v42 through v46 (5 wikis since trigger registration):**

| Wiki | Scope | Vision-primary browser agent? |
|------|-------|-------------------------------|
| v42 ruflo | T2 agent-as-service orchestration | NO — not browser agent |
| v43 rowboat | T5 personal-productivity-application | NO — not browser agent |
| v44 magika | Outside-scope ML-security-classifier | NO — not browser agent |
| v45 shannon | T5 AI-pentester | NO — not browser agent (uses DOM-based browser automation secondarily) |
| **v46 ollama** | **Outside-scope LLM-inference-runtime** | **NO — not browser agent at all** |

**Result: NO 2nd vision-primary data point arrived by v46.** Condition triggers retirement action at next mini-audit.

### 3.3 Retirement action (queued for next mini-audit)

At next mini-audit:
1. **Pattern #47 Vision-Based Browser Automation → RETIRED**
2. **Replace with OBSERVATION-TRACK** (sub-category introduced v29):
   - Name: "Browser-Agent Architectural-Approach 3-point spectrum"
   - Content: 3 distinct architectural approaches observed in corpus (vision-primary Skyvern N=1 / hybrid DOM+vision browser-use N=1 / DOM-only crawl4ai N=1)
   - Status: 🔍 OBSERVATION-TRACK (event-based; not architectural pattern with promotion path)
3. **Update N=1 stale-flag tracking table** — remove #47 entry; add OBSERVATION-TRACK entry

### 3.4 Structural significance (CORPUS-FIRST)

**This is the FIRST pre-registered conditional retirement trigger to actually fire in corpus history.**

Prior retirement paths:
- Stale-retirement (aged N=1 after 10+ wikis without evidence) — applied 4× at v27 audit
- Absorption-retirement (absorbed into superseding pattern) — applied 2× (v29 #60 absorbed into #17 variant 5; v31 #49 absorbed into #68)
- Confirmed-pattern absorption-retirement (v36 mini-audit absorbed #70 VN + #55 Korean into #73 Regional-Archetype-Registry)

**Pre-registered-conditional-retirement = NEW 4th retirement mechanism in corpus.**

**Governance precedent:** Pattern-library discipline acquired a new structural tool at v42-deferred mini-audit (conditional-retirement preregistration) and at v46 demonstrates the tool works as designed — triggers fire at preregistered condition without requiring operator memory of trigger.

### 3.5 Documentation for next mini-audit

Mini-audit document should include:
- Pattern #47 RETIRED status change
- OBSERVATION-TRACK "Browser-Agent Architectural-Approach 3-point spectrum" addition
- Structural-first commentary (first pre-registered conditional retirement fires)
- N=1 stale-flag tracking table update
- Post-audit ratio computation (retirement does NOT change ratio since RETIRED does not subtract from active-candidate count; it moves from candidate to retired — active-candidate count decreases by 1)

---

## 4. Pattern #28 Multi-Provider AI Support — STRUCTURAL INVERSION

### 4.1 Pattern #28 prior framing

Pattern #28 (CONFIRMED since v15; refined multiple times) has documented 11+ data points of frameworks adopting **multi-provider AI support** — consumer-side abstraction where framework X supports providers A, B, C, ...

**Recent data points:**
- ruflo v42: 6 providers with cost-based routing
- browser-use v41: 15+ native providers + LiteLLM (~115 total)
- DeepTutor v38: 27 LLM providers + 41 total integrations (corpus-most pre-v46)
- claude-context v40: 4 embedding + 2 vector DB + internal-env-switch sub-variant
- crawl4ai v29: LiteLLM via fork
- rowboat v43: 6 native + Vercel AI SDK + AI Gateway + Ollama + LM Studio

### 4.2 Structural inversion at v46

**Ollama is the PROVIDER being consumed by 11+ prior Pattern #28 wiki subjects.**

Evidence from README Libraries & SDKs section (lines 229-259):

| Pattern #28 prior consumer wiki | How it consumes Ollama |
|-------------------------------|------------------------|
| v29 crawl4ai (via unclecode-litellm fork) | LiteLLM treats Ollama as provider |
| v38 DeepTutor | Ollama listed in 27-provider + 41-integration catalog |
| v40 claude-context (Zilliz) | Ollama listed as embedding-provider option |
| v41 browser-use | Ollama native provider |
| v42 ruflo | Ollama integrated via BYO provider |
| v43 rowboat | Ollama named in README verbatim |
| **All 7 LangChain family integrations** | LangChain Python/JS/4j/Go/Rust/Dart/.NET all treat Ollama as provider |
| **Microsoft Semantic Kernel** | First-party Microsoft integration with Ollama connector |
| **Google Firebase Genkit** | First-party Google integration |
| **AWS Strands Agents** | First-party AWS integration |
| **Mozilla any-llm + any-agent** | First-party Mozilla integration |

**Plus:** Ollama itself implements **2 vendor-API-compat layers in parallel**:
- `openai/` subdir (5 files ~158 KB) — OpenAI Chat Completions API + Responses API
- `anthropic/` subdir (3 files ~83 KB) — Anthropic Messages API

This is **multi-API-compat-as-runtime** sub-pattern: any consumer expecting OpenAI SDK or Anthropic SDK can swap in Ollama without code changes (just change base URL + optional auth env var).

### 4.3 Within-Pattern-#28 observational framing (NOT new candidate)

**Consolidation-forward discipline applied (v2.1 Phase 0.6 mandatory pre-check):**

- Potential new candidate: "Provider-being-consumed runtime archetype"
- Overlap check: 100% overlap with Pattern #28 (just inverted direction)
- Decision: **Strengthen Pattern #28 with inversion sub-observation** — do NOT register standalone

Pattern #28 formulation-extension candidate at next mini-audit (optional; low priority):

> **Refined formulation:** Pattern #28 describes the multi-provider AI abstraction phenomenon from BOTH sides: (a) consumer side — frameworks adopt multiple provider support; (b) provider side — runtimes expose multi-API-compat layers to become universally-consumed. Ollama demonstrates provider-side: 2 vendor-API-compat (openai/ + anthropic/) + transparent local-cloud-split + first-party integrations from Microsoft + Google + AWS + Mozilla consuming it.

### 4.4 Strategic implication for corpus

Pattern #28 is **most-frequently-strengthened pattern** in corpus (11+ prior data points). v46 Ollama demonstrates **the provider side** of the ecosystem that 11+ prior consumers assume exists. Corpus now has both sides documented.

---

## 5. Pattern #18 Layer 0 observation — runtime-bundled-agent-launcher

### 5.1 Current Pattern #18 4-layer formulation (post-v42 + v36 refinements)

v42 Pattern #18 formal statement (most-refined state):
- **Layer 1 MCP universal** — Model Context Protocol adoption (OpenClaw + Hermes community-platform-scoped per v36 + ollama-MCP-Tier-1 per v45 shannon)
- **Layer 2 community-platform-scoped** — OpenClaw + Hermes ecosystem conventions
- **Layer 3 per-runtime** — individual runtime platform configs (Claude Code / Cursor / Windsurf / etc.)

Tool-count 3-tier distribution (v42 codification):
- Tier 1 basic 1-5 tools
- Tier 2 MCP-heavy 6-99 tools
- Tier 3 MCP-platform-scale 100+ tools (ruflo v42 313 tools corpus-first)

### 5.2 v46 Layer 0 observation

Ollama introduces `ollama launch <runtime>` — **runtime-bundled-agent-launcher primitive** below all existing Pattern #18 layers.

**Implementation:** 33 files in `cmd/launch/` subdirectory (~160 KB Go code + ~450 KB test code).

**10+ bundled runtimes:**

| Runtime | File size | Integration depth |
|---------|-----------|-------------------|
| OpenClaw | 27.4 KB | Heavy — install + config + daemon + onboarding UI |
| VS Code | 16.8 KB | Heavy — extension config |
| Hermes | 16.4 KB | Heavy |
| Pi (pi-mono v36) | 10.2 KB | Medium |
| Kimi | 8.5 KB | Medium |
| OpenCode | 6.2 KB | Medium |
| Droid | 5.0 KB | Medium |
| Codex | 3.6 KB | Light — config-injection only |
| Cline | 2.3 KB | Light |
| Claude Code | 1.9 KB | Light — env-var injection only |
| Copilot CLI | 1.7 KB | Light |

**Plus shared:** launch.go (29.2 KB core) + models.go (14.8 KB selector) + registry.go (11.5 KB runtime metadata) + selector_hooks.go (3.4 KB).

### 5.3 Layer 0 proposed formulation

**Layer 0 — runtime-bundled-agent-launcher:** LLM inference runtime ships `launch <runtime>` commands that bundle install + configuration + daemon-orchestration + connection for N agent runtimes at single infrastructure-runtime level.

Distinguishing features from Layer 1 (MCP):
- Not a protocol standardization — each launcher is bespoke integration
- Shipped as CLI commands in runtime binary (not separate daemon)
- Installation + configuration automated (e.g., `ollama launch openclaw` auto-installs OpenClaw via npm if not present, then configures gateway daemon, then opens TUI)

### 5.4 Pattern #18 formulation-extension candidate at next mini-audit

**Queued for next mini-audit consideration:**

Extend Pattern #18 formal statement to 4-layer taxonomy:
- **Layer 0 NEW — runtime-bundled-launcher** (ollama v46 N=1 observation at infrastructure-runtime scale)
- Layer 1 MCP universal
- Layer 2 community-platform-scoped
- Layer 3 per-runtime

**If N=2 arrives** (e.g., LMStudio ships similar bundled-launcher primitive in future wiki), Layer 0 formulation-extension confirmable under default ≥3-cross-tier or structural-N=2 criterion.

**At v46, this is OBSERVATION (not refinement)** — N=1 needs N=2 corroboration before formal-statement-update. Documented in strengthening data point category, not new-candidate registration (consolidation-forward discipline).

---

## 6. Pattern Library delta (Phase 5 direct updates preview)

Phase 5 will directly update PATTERN_LIBRARY.md with:

**Strengthenings (all within existing patterns; no status transitions at v46):**

| Pattern | Action |
|---------|--------|
| #17 variant 3 commercial-startup | +1 data point (Ollama, Inc. 170K-scale runtime-infrastructure + 130+ community-integration ecosystem) |
| #18 Agent Runtime Standardization | Layer 0 OBSERVATION (potential formulation-extension at next mini-audit if N=2 arrives) + Pattern #18 Tier 1 basic adoption by Ollama consumers observation |
| #19 archetype 4 tool-lineage | llama.cpp + Georgi Gerganov credit; fit |
| #22 AGENTS.md absence | Outside-scope runtime archetype consistent |
| #27 Community-Viral | 20+th observation; sustained-organic-infrastructure at ~5,150 stars/mo |
| #28 Multi-Provider AI Support | **STRUCTURAL INVERSION** observation within-pattern (provider-being-consumed + multi-API-compat-as-runtime) |
| #29 License-Category-Diversity | MIT strengthening |
| #2 Distribution Evolution | 13+ surface multi-OS observation |
| #12 Governance-Depth (refined 3-factor) | Commercial-runtime-infrastructure-stability sub-observation |
| #31 Open-Core Commercial Entity | **N=9 strengthening**; Pro-docs-depth 3/4; integration-driven upsell |
| #42 Academic-Published | Negative observational (practitioner-focused) |
| #44 Academic-Lab Affiliation | Negative observational (commercial-startup) |
| #47 Vision-Based Browser Automation | **CONDITIONAL RETIREMENT TRIGGER FIRES** (queued for next mini-audit retirement + OT replacement) |
| #48 Proprietary Anti-Bot Commercial Moat | Scope-distinct |
| #50 Commercial-Funnel Companion | **N=8 strengthening**; integration-driven-funnel sub-variant (NEW) |
| #52 Extreme-Viral-Velocity (stale) | Not un-staled (sustained-organic not extreme) |
| #57 Recursive Corpus Reference | **3rd data point + compound-2-wiki cross-corpus citation sub-variant** (NEW) |
| #58 Branding-Package Divergence | Negative (consistent `ollama` everywhere) |

**New candidates registered:** **0** (10-consecutive-wiki zero-registration streak extending v37-v45 9-streak — new corpus record)

**Outside-scope 9th sub-type catalog:** LLM-inference-runtime formally added.

## 7. Post-v46 Pattern Library state forecast

**Pre-v46:** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = **0.54:1 UNPRECEDENTED**.

**Post-v46 direct updates (before next mini-audit; no status transitions):**
- 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active
- Ratio 20:37 = **0.54:1 PRESERVED (10th consecutive wiki — NEW RECORD extending 9-streak v37-v45)**

**Post-next-mini-audit (if #47 retirement + OT replacement executed):**
- 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio 19:37 = **0.514:1 IMPROVED** (new all-time-low; first sub-0.55:1 ratio)

## 8. Storm Bear meta-implications

### 8.1 Corpus discipline signals

v46 demonstrates routine v2.1 discipline across 5 mechanisms simultaneously:

1. **Consolidation-forward discipline** — 0 new active candidates (10-streak extending record)
2. **Un-stale check** — all 4 stale candidates checked; negative
3. **Counter-evidence check** — Pattern #12 commercial-runtime-infrastructure-stability sub-observation (within refined formulation)
4. **Pre-registered conditional retirement trigger** — FIRES at v46 for Pattern #47 (new mechanism's first execution)
5. **Cross-corpus citation observation** — Pattern #57 3rd data point documented via third-party-unaware reference

### 8.2 Operator-facing backlog status

**v27 diagnostic HIGH bundle:**
- v46 = 18th consecutive wiki since v28 (when BLOCKING-RECOMMENDATION was first issued)
- 25+ sessions deferred
- Per routine v2.1 operator-facing backlog discipline: 5+ sessions = BLOCKING-RECOMMENDATION. **25+ sessions = threshold exceeded 5×.**

Pattern Library health at **0.54:1 UNPRECEDENTED** is NOT the bottleneck at v46. Operator-facing vault work is decisively next-highest-ROI.

**Recommended before v47:**
- Option A: **Mini-audit execute** (~30 min) — retires Pattern #47 + adds OBSERVATION-TRACK + updates N=1 stale-flag table; preserves corpus hygiene
- Option B: **v27 diagnostic HIGH bundle execute** (~6-8h) — unblocks 25+ sessions of deferred operator-facing vault actions
- Option C: **Continue v47** — wiki-building can extend 11-streak but operator backlog critical

### 8.3 Pattern #57 compound-cross-corpus citation meta-observation

Ollama's Pi integration doc third-party-unaware citing **v10 autoresearch + v36 pi-mono** validates that Storm Bear wiki-subject-selection is capturing the most-meaningful lineage nodes in the agent-runtime ecosystem.

This is **external validity signal** for corpus quality — 46 wikis in, 3rd-party maintainers independently reach for the same nodes Storm Bear selected for deep analysis (similar to v39 dive-into-llms cited LlamaFactory v22 wiki subject).

**46-wiki milestone implication:** Corpus has reached sufficient coverage that **third-party references to corpus wiki subjects appear independently in newly-arriving wikis at rate ≥1 per 5 wikis** (3 Pattern #57 data points across 46 wikis = ~6.5% base rate).

## 9. Cross-references

**Entities in this wiki:**
- `(C) Core product — ollama runtime + Modelfile.md`
- `(C) Commercial ecosystem + Pattern 31 N9 + Pattern 50 N8.md`
- `(C) Storm Bear meta — 35th consecutive.md`

**Cluster summaries:**
- `(C) README + positioning cluster summary.md`
- `(C) Architecture + 38-subdir cluster summary.md`
- `(C) Commercial + ecosystem cluster summary.md`

**Sibling wikis:**
- v8 build-your-own-x (1st outside-scope)
- v20 fish-speech (outside-scope foundation-model; produces weights)
- v22 LlamaFactory + v23 Unsloth (outside-scope training-infra; trains weights)
- v24 Skyvern (Pattern #47 founding vision-primary data point)
- v29 crawl4ai (Pattern #47 refinement via DOM-only counter-evidence)
- v36 pi-mono (cited in Ollama Pi integration docs)
- v37 bizos (outside-scope 7th sub-type)
- v41 browser-use (Pattern #47 3-point spectrum codification at v42-deferred mini-audit)
- v42 ruflo (v42-deferred mini-audit pre-registered #47 conditional retirement trigger)
- v44 magika (outside-scope 8th sub-type; most-recent precedent)
- v10 autoresearch-Karpathy (cited in Ollama Pi integration docs verbatim)

**Pattern Library:**
- PATTERN_LIBRARY.md
- `04 Reviews/(C) 2026-04-24 Pattern Library mini-audit post-v42 (v41 deferred actions).md` (pre-registered conditional retirement trigger source document)
