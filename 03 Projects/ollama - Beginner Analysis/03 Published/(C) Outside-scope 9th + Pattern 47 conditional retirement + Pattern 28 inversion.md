# (C) Phase 4b Deliverable: Outside-scope 9th sub-type LLM-inference-runtime + Pattern #47 conditional retirement FIRES + Pattern #28 structural inversion + Pattern #18 Layer 0 observation

> **Phase 4b primary deliverable for v46 ollama.** ~720 lines. Documents 4 structural events landing in parallel at v46; 10-consecutive-wiki zero-new-candidates streak extends to new corpus record; pre-registered conditional retirement trigger fires for first time in corpus history.
>
> **Routing mode:** Outside-scope sub-type formalization + counter-evidence-refinement + un-stale-mechanism(-adjacent) + ratio-ceiling-discipline + protocol-directory-meta-reference-adjacent.

---

## Part 0 — Summary

**v46 ollama produces 4 simultaneous structural events:**

1. **Outside-scope 9th sub-type formalized — LLM-inference-runtime** (7 test criteria; distinct from 8 prior sub-types)
2. **Pattern #47 Vision-Based Browser Automation — pre-registered conditional retirement trigger FIRES** (CORPUS-FIRST: 1st pre-registered conditional retirement to actually fire)
3. **Pattern #28 Multi-Provider AI Support — STRUCTURAL INVERSION observation** (provider-being-consumed + multi-API-compat-as-runtime; Ollama implements 2 vendor-compat layers simultaneously via `openai/` + `anthropic/` subdirs)
4. **Pattern #18 Agent Runtime Standardization — Layer 0 runtime-bundled-launcher observation** (`ollama launch <runtime>` primitive; 33 files in `cmd/launch/`; potential 4-layer taxonomy extension at next audit)

**Plus:**
- **Pattern #57 Recursive Corpus Reference 3rd data point + compound-2-wiki cross-corpus citation sub-variant** (Ollama Pi integration doc cites v36 pi-mono + v10 autoresearch-Karpathy verbatim in single doc)
- **Pattern #31 Open-Core Commercial Entity N=9 strengthening** (Ollama Cloud Pro $20/mo + Max $100/mo; Pro-docs-depth 3/4)
- **Pattern #50 Commercial-Funnel Companion Platform N=8 strengthening** (7-surface integration-driven funnel sub-variant NEW)

**0 new active candidates.** 10-consecutive-wiki zero-new-candidates streak extending v37-v45 9-streak (CORPUS RECORD).

**Pattern Library post-v46 direct updates (before next mini-audit):** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = **0.54:1 PRESERVED 10th consecutive wiki** (extending 9-streak, new record).

---

## Part 1 — Outside-scope 9th sub-type: LLM-inference-runtime

### 1.1 Formal definition

**Name:** LLM-inference-runtime
**Scope:** Outside Storm Bear agent-framework taxonomy (T1-T5); joins 8 prior outside-scope sub-types.
**Founding wiki:** v46 ollama
**Scope tier:** X-large (170K stars Ollama — the largest-scale representative)

### 1.2 Seven test criteria

A repository fits **LLM-inference-runtime** outside-scope sub-type if it meets ALL 7:

1. **Runtime for running model weights at inference time.** Not training, not producing weights.
2. **Consumed BY agents as provider.** Structural inversion from typical Pattern #28 framing (frameworks abstract providers; this subtype IS the provider).
3. **Local-first deployment model.** Single-machine install + daemon pattern.
4. **Multi-OS binary distribution.** At least macOS + Linux + Docker (Windows optional).
5. **Model registry + declarative model-packaging format.** Enables custom model creation + distribution (Modelfile, safetensors-with-config, etc.).
6. **Multi-provider-API-compat surface.** Exposes at least one vendor-API-compat layer (OpenAI-compat minimum; bonus for Anthropic-compat / Azure-compat / others).
7. **Upstream integration with inference library.** Builds on established inference library (llama.cpp / vLLM / Triton / TensorRT-LLM) + optional native backends (MLX / CUDA / ROCm / Metal).

### 1.3 Distinction from 8 prior outside-scope sub-types

| # | Sub-type | Founding | Distinguishing vs LLM-inference-runtime |
|---|----------|----------|------------------------------------------|
| 1 | education-aggregator → absorbed into #68 | v8 build-your-own-x | Curated learning content (human-directed), not runtime |
| 2 | foundation-model | v20 fish-speech | **Produces model weights** (inference-runtime consumes weights foundation-model creates) |
| 3 | prompt-leak-archive | v21 system-prompts-leaks | Archive of extracted prompts; not runtime |
| 4 | training-infrastructure | v22 LlamaFactory + v23 Unsloth | **Trains model weights** (inference-runtime runs post-training inference only) |
| 5 | design-template-aggregator → absorbed into #68 | v25 awesome-design-md | UI-template directory; not runtime |
| 6 | MCP-server-aggregator → absorbed into #68 | v31 awesome-mcp-servers | MCP-server directory; not runtime |
| 7 | business-OS-as-product (OT#74) | v37 bizos | Domain-application; not LLM infrastructure |
| 8 | ML-security-classifier | v44 magika | File-type classifier; not LLM-serving |
| **9** | **LLM-inference-runtime** | **v46 ollama** | **Serves LLM inference; consumed BY agents as provider** NEW |

### 1.4 Future observations expected

**Candidate LLM-inference-runtime wikis for future Storm Bear corpus:**

- LMStudio (proprietary desktop; possibly-outside-Storm-Bear-corpus since not fully OSS)
- llama.cpp (upstream library — likely outside tier since library not runtime; Ollama wraps it)
- text-generation-webui / Oobabooga
- vLLM (Python-based, GPU-focused)
- llama-runner
- nomic.ai's LocalAI

**If a 2nd LLM-inference-runtime wiki arrives at v≤51 (5 wikis post-v46):** sub-type achieves N=2, matching training-infrastructure (v22 → v23 N=2 path).

**Stale-check schedule:** v51 (5-wiki)
**Retirement-check schedule:** v56 (10-wiki)

### 1.5 Outside-scope sub-type taxonomy evolution

**12-sub-type historical count (9 current distinct + 3 absorbed):**

1. education-aggregator (absorbed into #68 v31 mini-audit)
2. foundation-model (active, N=1 at fish-speech v20)
3. prompt-leak-archive (active, N=1 at system-prompts-leaks v21)
4. training-infrastructure (active, N=2 at LlamaFactory v22 + Unsloth v23)
5. design-template-aggregator (absorbed into #68 v31 mini-audit)
6. MCP-server-aggregator (absorbed into #68 v31 mini-audit)
7. business-OS-as-product (active OT#74, N=1 at bizos v37)
8. ML-security-classifier (active, N=1 at magika v44)
9. **LLM-inference-runtime (active, N=1 at ollama v46 NEW)**

**9 active distinct sub-types at v46.** Pattern #68 Awesome-List-Genre absorbed 3 aggregator-type sub-types (education + design + MCP) at v31 mini-audit consolidation.

---

## Part 2 — Pattern #47 Vision-Based Browser Automation — CONDITIONAL RETIREMENT TRIGGER FIRES

### 2.1 Pattern #47 history

| Audit | Action |
|-------|--------|
| v24 Skyvern (registration) | Registered as CANDIDATE at N=1 vision-DOM-free formulation |
| v29 audit | REFINED via crawl4ai counter-evidence (DOM-only architectural alternative) → narrowed to "vision-based as architectural alternative" |
| v41 browser-use | Hybrid DOM+vision counter-evidence — neither vision-primary (Skyvern) nor DOM-only (crawl4ai) |
| v42-deferred mini-audit | REFINED via 3-point architectural spectrum formulation: vision-primary Skyvern N=1 / hybrid browser-use N=1 / DOM-only crawl4ai N=1. Stays CANDIDATE at N=1 vision-primary pole. **Stale-check extension to v46 with pre-registered conditional retirement path** |

### 2.2 Pre-registered conditional retirement trigger verbatim

From PATTERN_LIBRARY.md v42-deferred mini-audit entry:

> "**stale-check extension to v46 with pre-registered conditional retirement path** (if no 2nd vision-primary data point by v46, retire + replace with OBSERVATION-TRACK 'Browser-Agent Architectural-Approach 3-point spectrum')"

### 2.3 Verification at v46

**Wikis v42 through v46 (5 wikis since trigger registration):**

| Wiki | Scope domain | Vision-primary browser agent? | Note |
|------|-------|-------------------------------|------|
| v42 ruflo | T2 agent-as-service orchestration | NO | RuvNet flagship framework; not browser |
| v43 rowboat | T5 personal-productivity-application | NO | Knowledge-graph personal AI coworker; not browser |
| v44 magika | Outside-scope ML-security-classifier | NO | File-type classifier; not browser |
| v45 shannon | T5 AI-pentester | NO | Security testing; uses DOM-based browser automation secondarily (NOT vision-primary) |
| **v46 ollama** | **Outside-scope LLM-inference-runtime** | **NO** | **LLM runtime; not browser agent at all** |

**Result:** NO 2nd vision-primary data point arrived by v46. **Conditional retirement trigger FIRES.**

### 2.4 Retirement action queued for next mini-audit

**Mini-audit actions:**

1. **Pattern #47 Vision-Based Browser Automation → RETIRED** (status transition: candidate → retired)
2. **Reason:** Pre-registered conditional retirement trigger (v42-deferred mini-audit) — stale-check at v46 with no 2nd vision-primary data point
3. **Replace with OBSERVATION-TRACK:**
   - Name: "Browser-Agent Architectural-Approach 3-point spectrum"
   - Sub-category: OBSERVATION-TRACK (event-based observation; no architectural promotion path)
   - Content: 3 distinct architectural approaches observed:
     - Vision-primary: Skyvern v24 (N=1)
     - Hybrid DOM+vision: browser-use v41 (N=1)
     - DOM-only: crawl4ai v29 (N=1)
   - Monitoring: reclassify back to candidate if 2+ new observations emerge at same architectural pole
4. **Update N=1 stale-flag tracking table** — remove #47 entry; add OBSERVATION-TRACK entry

### 2.5 Structural-first significance (CORPUS-FIRST)

**First pre-registered conditional retirement trigger to actually fire in corpus history.**

4 retirement mechanisms now documented + validated:
1. **Stale-retirement** (v27 audit) — aged N=1 after 10+ wikis → 4 retirements (first use)
2. **Absorption-retirement** (v29 + v31) — absorbed into superseding pattern → #60 at v29, #49 at v31 (2 cases)
3. **Confirmed-pattern absorption-retirement** (v36 mini-audit) — confirmed patterns absorbed into superseding meta-pattern → #70 VN + #55 Korean absorbed into #73
4. **Pre-registered conditional retirement (v46 FIRST FIRING)** — preregistered trigger condition met at future wiki → Pattern #47

**Governance tool matured:** Pattern-library discipline acquired 4th retirement mechanism at v42-deferred mini-audit (conditional-retirement preregistration) and **v46 demonstrates the tool works as designed** — trigger fires at preregistered condition without requiring operator to remember trigger existed.

This validates:
- Pattern-library discipline can be **defined as preregistered conditional** (not just reactive)
- Future patterns can be registered with similar conditional-retirement preregistration (e.g., "if no 2nd X observation by v+5, retire")
- Mini-audit cadence (~30 min) is sufficient for executing preregistered conditional retirements

### 2.6 Post-mini-audit ratio calculation

**Current (pre-mini-audit at v46 direct updates):**
- 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active
- Ratio 20:37 = 0.54:1

**Post-next-mini-audit (if #47 retirement + OT replacement):**
- 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio **19:37 = 0.513:1 IMPROVED** (first sub-0.55:1 ratio in corpus history)

**New all-time-low post-mini-audit.** Routine-integrity gains from preserving conditional-retirement discipline.

---

## Part 3 — Pattern #28 Structural Inversion observation

### 3.1 Prior Pattern #28 framing

Pattern #28 Multi-Provider AI Support (CONFIRMED since v15; refined multiple times) documents **consumer-side abstraction**: framework X adopts multi-provider AI support where X = framework, providers = OpenAI / Anthropic / Google / local-models / etc.

**11+ prior data points:**
- ruflo v42 (6 providers + cost-based routing)
- browser-use v41 (~115 provider surface via LiteLLM)
- DeepTutor v38 (41 integrations)
- claude-context v40 (4 embedding + 2 vector DB + internal-env-switch)
- crawl4ai v29 (LiteLLM fork)
- rowboat v43 (6 native + Vercel AI SDK)
- Plus multiple LangChain family wikis + Microsoft Semantic Kernel consumer patterns

### 3.2 Inversion at v46

**Ollama INVERTS Pattern #28** — Ollama is the **PROVIDER being consumed** by 11+ prior Pattern #28 wiki subjects.

**Evidence from README Libraries & SDKs section (lines 229-259):**

Prior Pattern #28 consumer wikis listing Ollama as provider:

| Consumer wiki | How Ollama is consumed |
|---------------|----------------------|
| LiteLLM (used by v29 crawl4ai via fork; v42 ruflo; etc.) | Ollama is native provider |
| LangChain family — 7 languages (v30+ + v40 claude-context + others) | All LangChain variants treat Ollama as provider |
| LlamaIndex (v38 DeepTutor ecosystem parent) | Ollama native provider |
| Microsoft Semantic Kernel (v6 prior Microsoft T3) | First-party Microsoft connector for Ollama |
| Google Firebase Genkit (v13 gws Google entrant) | First-party Google plugin for Ollama |
| AWS Strands Agents | First-party AWS framework with Ollama support |
| Mozilla any-llm + any-agent | First-party Mozilla abstractions treating Ollama as provider |
| Portkey (AI gateway) | Routes to Ollama as backend provider |
| Haystack (RAG) | Ollama provider integration |
| Ollama as LLM backend for: AutoGPT, crewAI, Cheshire Cat, 8+ other frameworks |

### 3.3 Multi-API-compat-as-runtime sub-observation

**Plus structural complement:** Ollama itself exposes **2 vendor-API-compat layers simultaneously**:

| Subdir | Size | Role |
|--------|------|------|
| `openai/` | 5 files ~158 KB | OpenAI Chat Completions + Responses API endpoints |
| `anthropic/` | 3 files ~83 KB | Anthropic Messages API endpoints |

**This means:** Any consumer expecting OpenAI SDK (11+ prior Pattern #28 wikis) or Anthropic SDK (Claude Code) can swap in Ollama by:
- OpenAI-compat: set `base_url: http://localhost:11434/v1`
- Anthropic-compat: set `ANTHROPIC_BASE_URL=http://localhost:11434`

**This is "multi-API-compat-as-runtime" sub-pattern** — distinct from frameworks that abstract providers consumer-side. Ollama abstracts providers **runtime-side** (single runtime serves multiple vendor SDK conventions simultaneously).

### 3.4 Within-Pattern-#28 observational framing (consolidation-forward discipline)

**Potential new candidate considered + rejected:** "Provider-being-consumed runtime archetype"

**Overlap pre-check (Phase 0.6 v2.1 mandatory):**
- 100% overlap with Pattern #28 (just inverted direction of the same phenomenon)
- **Decision:** Strengthen Pattern #28 with inversion sub-observation — do NOT register standalone

**Pattern #28 formulation-extension candidate at next mini-audit (optional; low priority):**

> **Refined formulation:** Pattern #28 describes multi-provider AI abstraction phenomenon from BOTH directions:
> - **Consumer side** (11+ data points): framework X abstracts providers A, B, C, ... (most observed variant)
> - **Provider side NEW observation at v46** (N=1): runtime Y exposes multiple vendor-API-compat layers to become universally-consumed-by-multiple-consumer-frameworks

If future wiki subject also demonstrates provider-side-multi-API-compat at infrastructure scale, formulation-extension confirmable at next mini-audit.

### 3.5 Strategic implication

Pattern #28 is **most-frequently-strengthened pattern** in corpus (12+ observations at v46). v46 Ollama demonstrates **the provider side of the ecosystem** that 11+ prior consumer wikis assumed existed.

**Corpus now has both sides documented.** Structural completeness — Pattern #28 is no longer "one-sided" observation.

---

## Part 4 — Pattern #18 Layer 0 runtime-bundled-launcher observation

### 4.1 Pattern #18 current 3-layer formulation (post-v42 + v36 refinements)

v42 Pattern #18 formal statement (most-refined at v46):
- **Layer 1 MCP universal** — Model Context Protocol (OpenClaw + Hermes community-platform-scoped per v36 + ollama-MCP-Tier-1 per v45 shannon)
- **Layer 2 community-platform-scoped** — OpenClaw + Hermes ecosystem conventions
- **Layer 3 per-runtime** — individual runtime platform configs

### 4.2 v46 Layer 0 observation

Ollama introduces **`ollama launch <runtime>`** — runtime-bundled-agent-launcher primitive **below all existing Pattern #18 layers**.

**Implementation:** 33 files in `cmd/launch/` subdirectory (~160 KB Go code + ~450 KB test code).

### 4.3 10+ bundled agent runtimes

| Runtime | File size | Integration depth | Documented lineage to Storm Bear corpus |
|---------|-----------|-------------------|-------------------|
| **OpenClaw** | 27.4 KB | Heavy | Pattern #18 Layer 2 canonical |
| **VS Code** | 16.8 KB | Heavy | — |
| **Hermes Agent** | 16.4 KB | Heavy | Pattern #18 Layer 2 canonical |
| **Pi (pi-mono v36)** | 10.2 KB | Medium | **v36 wiki subject** |
| Kimi (Moonshot) | 8.5 KB | Medium | — |
| **OpenCode** | 6.2 KB | Medium | — |
| Droid (Factory.ai) | 5.0 KB | Medium | — |
| Codex (OpenAI) | 3.6 KB | Light | — |
| Cline (VS Code ext) | 2.3 KB | Light | — |
| **Claude Code** | 1.9 KB | Light | — |
| Copilot CLI (GitHub) | 1.7 KB | Light | — |

### 4.4 Layer 0 proposed formulation

**Layer 0 — runtime-bundled-agent-launcher:** LLM inference runtime ships `launch <runtime>` commands bundling install + configuration + daemon-orchestration + connection for N agent runtimes at single infrastructure-runtime level.

**Distinguishing features from Layer 1 (MCP):**
- Not a protocol standardization — each launcher is bespoke integration
- Shipped as CLI commands in runtime binary (not separate daemon)
- Installation + configuration automated (e.g., `ollama launch openclaw` auto-installs OpenClaw via npm if not present, then configures gateway daemon, then opens TUI)

**Key behavior pattern:**
```
ollama launch <runtime> [--model <model>] [--yes]
→ Auto install runtime if missing (via npm / curl installer)
→ Auto configure runtime (env vars, config files)
→ Auto pull model if --model specified + --yes
→ Drop into interactive session
```

### 4.5 Proposed 4-layer Pattern #18 taxonomy at next mini-audit

If Pattern #18 formulation extends at next mini-audit:

| Layer | Scope | N= |
|-------|-------|---|
| **Layer 0 (NEW proposed)** | Runtime-bundled-launcher (infrastructure-runtime consumes N agent runtimes via bundled CLI) | **N=1 at v46 (ollama)** — observational only at present |
| Layer 1 | MCP universal (Model Context Protocol) | N=12+ consumer wikis |
| Layer 2 | Community-platform-scoped (OpenClaw + Hermes conventions) | N=5+ |
| Layer 3 | Per-runtime (Claude Code / Cursor / Windsurf / etc.) | N=many |

**Layer 0 promotion criteria at N=2:** if future wiki subject in outside-scope LLM-inference-runtime sub-type also ships bundled-launcher primitive (e.g., LMStudio's Local Server + API support for multiple protocols), Layer 0 formulation-extension confirmable under structural-N=2.

**At v46:** OBSERVATION; not formal Pattern #18 refinement yet. Documented as strengthening data point within existing 3-layer formulation, not as standalone new-candidate registration (consolidation-forward discipline applied).

### 4.6 Pattern #18 Tier 1 basic adoption by Ollama consumers

Pattern #18 tool-count 3-tier distribution (v42 codification):
- Tier 1 basic 1-5 tools
- Tier 2 MCP-heavy 6-99 tools
- Tier 3 MCP-platform-scale 100+ tools

**Ollama itself:** Does NOT consume MCP directly — integration with MCP-capable agent runtimes happens through API-compatibility layer (OpenAI-compat + Anthropic-compat) not MCP protocol.

**Consumer wikis that consume Ollama + MCP:**
- shannon v45 (Tier 1 MCP consumer at Pro tier; uses MCP server for TOTP via dedicated tool)
- Claude Code (MCP-capable; can use Ollama as model provider via Anthropic-compat while using MCP for tool-use)
- OpenClaw + Hermes (Pattern #18 Layer 2 MCP consumers; use Ollama as model backend)

**Ollama is Layer 0 provider** for Layer 1 MCP consumers. Pattern #18 4-layer taxonomy structurally sound.

---

## Part 5 — Pattern #57 Recursive Corpus Reference 3rd data point + compound sub-variant (NEW)

### 5.1 Pattern #57 timeline at v46

| # | Wiki | Recursive reference | Sub-variant |
|---|------|---------------------|-------------|
| 1 | v27 oh-my-claudecode | README cites v1 ECC + v2 Superpowers | 2-wiki citation across separate README sections |
| 2 | v30 OpenHands | Academic paper lineage chain (UIUC/CMU) | Academic-lineage-chain (implicit) |
| **3** | **v46 ollama** | **Pi integration doc cites v36 pi-mono + v10 autoresearch-Karpathy** | **Compound-2-wiki cross-corpus citation in single doc (NEW)** |

### 5.2 Evidence from Ollama source

**docs/integrations/pi.mdx (110 lines) contains 2 citations:**

**Reference 1 (lines 9-14) — v36 pi-mono Mario Zechner:**
> "Pi is a minimal and extensible coding agent.
>
> Install [Pi](https://github.com/badlogic/pi-mono):
> ```
> npm install -g @mariozechner/pi-coding-agent
> ```"

**Reference 2 (lines 67-68) — v10 autoresearch Karpathy verbatim:**
> "[pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) brings autonomous experiment loops to Pi. **Inspired by Karpathy's autoresearch**, it turns any measurable metric into an optimization target: test speed, bundle size, build time, model training loss, Lighthouse scores."

**Both citations in ONE integration doc.**

### 5.3 Sub-variant formalization: compound-2-wiki cross-corpus citation

**Distinction from v27 OMC:**
- v27 OMC cited ECC + Superpowers in separate README sections (distributed 2-wiki citation)
- v46 ollama cites pi-mono + autoresearch-Karpathy in single doc compressed into single narrative (compound 2-wiki citation)

**Qualitative difference:** Single-doc compound citation demonstrates the 2 prior wiki subjects are **genuinely entangled** in third-party maintainer's mental model (Pi lineage = pi-mono runtime + Karpathy methodology, referenced together not separately).

### 5.4 External validity signal

**46-wiki corpus milestone:**
- Pattern #57 base rate: 3 data points / 46 wikis = **6.5% of wikis contain recursive corpus references**
- Stronger-than-random signal — Storm Bear wiki-subject-selection captures most-meaningful lineage nodes

Similar cross-corpus external-validity signals in prior wikis:
- v39 dive-into-llms cited LlamaFactory v22 chapter 9
- v43 rowboat implicit-Karpathy structural parallel (knowledge-graph as Markdown; not explicit citation but structural mirror)

**At 46 wikis, 3 explicit Pattern #57 data points + multiple implicit external-validity signals validate corpus selection discipline.**

### 5.5 Potential future sub-variant promotion

If another compound-cross-corpus citation appears in a future wiki:
- Sub-variant "compound-cross-corpus citation" could promote at N=2 structural-unambiguity
- Currently: observational + sub-variant documented; NO new candidate registration (consolidation-forward)

---

## Part 6 — Pattern #31 Open-Core Commercial Entity N=9 strengthening

### 6.1 Pattern #31 data-point timeline

| # | Wiki | License | Commercial tier | Pro-docs-depth (0-4) |
|---|------|---------|-----------------|------------|
| 1 | v20 fish-speech | Custom non-OSI | Research-only OSS + commercial license | — (pre-formalization) |
| 2 | v24 Skyvern | AGPL-3.0 | Skyvern Cloud | — |
| 3 | v29 crawl4ai | Apache-2.0 | Cloud closed beta | — |
| 4 | v30 OpenHands | MIT + enterprise directory | Enterprise tier | — |
| 5 | v33 GitNexus | PolyForm Noncommercial | akonlabs.com SaaS | — |
| 6 | v41 browser-use | MIT | Browser-Use Cloud | 2/4 (inferred retrospectively) |
| 7 | v42 ruflo | MIT | Cognitum.One + Flow Nexus | 3/4 (inferred retrospectively) |
| 8 | v45 shannon | Shannon Lite AGPL-3.0 | Shannon Pro commercial | **4/4 (SHANNON-PRO.md 26KB corpus-most-detailed)** |
| **9** | **v46 ollama** | **MIT** | **Ollama Cloud Pro $20/mo + Max $100/mo** | **3/4** (ollama.com/pricing + /cloud.mdx + `ollama signin` — no SHANNON-PRO-style dedicated repo file) |

### 6.2 Pro-docs-depth signal (v45 formalization 0-4 ordinal-scale)

**Ollama v46 = 3/4:**

| Axis | Ollama v46 |
|------|-----------|
| Dedicated /pricing page | ✅ |
| Dedicated /cloud docs (cloud.mdx 232 lines) | ✅ |
| Account-signin CLI flow (`ollama signin`) | ✅ |
| Dedicated Pro-upsell file in repo (SHANNON-PRO.md-style) | ❌ |
| **Score** | **3/4** |

Shannon v45 remains 4/4 corpus-benchmark (SHANNON-PRO.md 26 KB).

### 6.3 Transparent local-cloud proxy architecture

**Corpus-first commercial-funnel sub-variant:**

Same CLI / REST API / SDK operate transparently against local OR cloud models via `:cloud` suffix in model name:

```shell
ollama run gemma3              # local inference
ollama run kimi-k2.5:cloud     # cloud inference (routes to Ollama Cloud backend)
```

Implementation in `server/cloud_proxy.go` (14.5 KB) + `server/routes_cloud_test.go` (33.0 KB).

**Authentication:** `ollama signin` → provisions `OLLAMA_API_KEY` → subsequent `:cloud` calls authenticated transparently.

**Commercial effect:** **Zero-code-change commercial upsell** — users can swap model name from `llama3.2` to `kimi-k2.5:cloud` and entire codebase continues to work. Creates natural upsell friction (Pro/Max tier unlocks more cloud usage + more concurrent cloud models).

**Integration-driven upsell pathway:**
```
User: "ollama launch claude --model kimi-k2.5:cloud"
CLI: "kimi-k2.5:cloud requires Ollama account. Run `ollama signin` first."
→ Account creation → cloud usage free tier → upsell trigger at usage threshold
```

---

## Part 7 — Pattern #50 Commercial-Funnel Companion Platform N=8 strengthening

### 7.1 Pattern #50 data-point timeline

| # | Wiki | Funnel architecture | Sub-variant |
|---|------|---------------------|-------------|
| 1 | v25 VoltAgent (awesome-design-md + getdesign.md) | 5-surface design-template funnel | Dedicated-doc-driven |
| 2 | v31 Frank Fiegel (Glama + awesome-mcp-servers) | 6-surface MCP-directory funnel | Directory-driven |
| 3 | v40 claude-context (Zilliz) | UTM-tracked campaign ID | First T4 cross-tier data point |
| 4 | v41 browser-use | AGENTS.md-embedded-LLM-upsell-instructions | In-framework-governance corpus-first |
| 5 | v42 ruflo | 3-layer commercial | Corpus-most-elaborate |
| 6 | v43 rowboat | 7-surface YC-S24 funnel | YC-amplified |
| 7 | v45 shannon | 7-surface Keygraph + Tower + Shannon Pro | Multi-product ecosystem |
| **8** | **v46 ollama** | **7-surface integration-driven funnel** | **Integration-driven-funnel sub-variant NEW** |

### 7.2 Ollama's 7-surface funnel

1. **ollama.com** landing page
2. **ollama.com/pricing** dedicated pricing
3. **docs.ollama.com/cloud** comprehensive cloud docs (232 lines)
4. **ollama.com/library** model library (markets cloud models)
5. **ollama.com/search?c=cloud** cloud-filter discovery surface
6. **`ollama signin`** CLI-native upsell gate
7. **Community surfaces** (Discord + X + Reddit + blog)

### 7.3 Integration-driven-funnel sub-variant (NEW)

**Distinguishing feature:** Upsell pathway embedded inside agent-runtime-integration workflow, NOT in README marketing.

**Pathway example:**
```
1. User installs Ollama (free)
2. User wants Claude Code with Kimi-K2.5 (cloud-only model)
3. User runs `ollama launch claude --model kimi-k2.5:cloud`
4. CLI detects cloud-model + no account → prompts `ollama signin`
5. Account creation → free cloud tier
6. Usage grows → upsell trigger at 50× baseline threshold
7. Pro $20/mo or Max $100/mo
```

**Distinct from:**
- Dedicated-doc upsell (shannon v45 SHANNON-PRO.md 26 KB explicit marketing)
- In-app upsell (rowboat v43 YC-startup)
- Ecosystem-portfolio (ruflo v42 3-layer commercial)

**Integration-driven-funnel sub-variant = corpus-first** at v46.

---

## Part 8 — Meta-implications + post-v46 Pattern Library forecast

### 8.1 10-consecutive-wiki zero-new-candidates streak (CORPUS RECORD)

**Streak evolution:**

| Wiki range | Streak # | Zero-registration? |
|------------|----------|---------------------|
| v37 bizos | 1st | ✓ |
| v38 DeepTutor | 2nd | ✓ |
| v39 dive-into-llms | 3rd | ✓ |
| v40 claude-context | 4th | ✓ |
| v41 browser-use | 5th | ✓ |
| v42 ruflo | 6th | ✓ |
| v43 rowboat | 7th | ✓ |
| v44 magika | 8th | ✓ |
| v45 shannon | 9th | ✓ |
| **v46 ollama** | **10th** | ✓ |

**NEW corpus record:** 10 consecutive wikis with 0 new active candidates + 0 new OBSERVATION-TRACKs.

### 8.2 Post-v46 Pattern Library state forecast

**Current (post-v45 harvest audit):** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio 20:37 = **0.54:1 UNPRECEDENTED**.

**Post-v46 direct updates (0 status transitions):** 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active. Ratio **0.54:1 PRESERVED 10th consecutive wiki**.

**Post-next-mini-audit (if #47 retirement + OT replacement per conditional retirement trigger):**
- 37 confirmed + 19 active + 3 stale + 9 retired + 5 OT = 73 full / 56 active
- Ratio **19:37 = 0.513:1 NEW ALL-TIME-LOW** (first sub-0.55:1 ratio in corpus history)

### 8.3 5 discipline mechanisms exercised cleanly at v46

v46 demonstrates routine v2.1 discipline across all 5 mechanisms:

1. **Consolidation-forward discipline** — 0 new active candidates target achieved (10-streak extending record)
2. **Un-stale check** — all 3 stale candidates (#45 Dual-Licensing / #52 Extreme-Viral-Velocity / #71 Interactive-Self-Assessment) + #72 PolyForm checked; all negative
3. **Counter-evidence check** — Pattern #12 Governance-Depth commercial-runtime-infrastructure-stability sub-observation within refined 3-factor formulation (not counter-evidence that narrows scope; sub-observation that strengthens existing refinement)
4. **Pre-registered conditional retirement trigger** — FIRES at v46 for Pattern #47 (first firing of new mechanism introduced v42-deferred mini-audit)
5. **Cross-corpus citation observation (Pattern #57)** — 3rd data point + compound-2-wiki sub-variant NEW

### 8.4 8th v2.1-era routine execution milestone

v46 = 8th v2.1-era routine execution (counting v32 onward):
- v32 claude-howto (1st v2.1 execution)
- v33 GitNexus (2nd)
- v34 claude-code-best-practice (3rd)
- v42 ruflo (6th)
- v43 rowboat (7th)
- v44 magika
- v45 shannon
- **v46 ollama (8th v2.1 execution)**

All 8 executions exercised 5+ discipline mechanisms cleanly without violations.

### 8.5 Velocity + primitive-count

**Primitive-count outcome: RED (2nd RED in corpus after v41 browser-use inaugural)**

- Estimated primitives: ~250-400 across 38 subdirs + 13 REST endpoints + 2 API-compat layers + 10+ launch runtimes + Modelfile format + model registry + multi-backend inference pipeline
- 4-entity format preserved via aggressive citation-not-replication
- 4 follow-up deep-dive wikis flagged

**Velocity: ~3h 0min** — within RED +50% overhead tolerance (vs ~2h GREEN baseline per v41 precedent).

**27+ consecutive wikis at ~2h velocity plateau preserved** (v6-v46; RED overhead within tolerance).

---

## Part 9 — Operator-facing backlog escalation

### 9.1 v27 diagnostic HIGH bundle status

- **v46 = 18 wikis since first BLOCKING-RECOMMENDATION at v28** (2026-04-22)
- **25+ operator sessions deferred** (incl. direct-update sessions)
- Per routine v2.1 operator-facing backlog discipline: **5+ sessions threshold exceeded ~5×**

### 9.2 Pattern Library health vs operator backlog

**Pattern Library at 0.54:1 UNPRECEDENTED = NOT the bottleneck.** Library is healthier than ever.

**Operator-facing vault work is decisively next-highest-ROI.**

### 9.3 Recommended sequencing after v46

**Option A (HIGH leverage, ~30 min):** Execute mini-audit
- Retire Pattern #47 per conditional retirement trigger
- Add OBSERVATION-TRACK "Browser-Agent Architectural-Approach 3-point spectrum"
- Update N=1 stale-tracking table
- Pattern Library ratio improves to 0.513:1 (new all-time-low)

**Option B (~6-8h):** Execute v27 diagnostic HIGH bundle
- Item #1: vault CLAUDE.md refactor (use v34 82-tip template + Ollama anti-feature-expansion governance model)
- Item #2: Storm Bear publishing strategy
- Item #5: vault skill-lock
- Unblocks 25+ deferred sessions

**Option C (continue v47):** Ship v47 wiki; extends streak to 11-consecutive but backlog continues

**Option D (hybrid):** Mini-audit (~30 min) + v27 HIGH bundle (~6-8h) same session = ~8h total

**Strongly recommended: Option A or D** — executes pre-registered conditional retirement trigger per routine discipline AND (Option D) addresses operator backlog.

---

## Part 10 — Corpus-firsts enumerated at v46

1. **9th outside-scope sub-type LLM-inference-runtime** formalized with 7 test criteria
2. **Pattern #47 pre-registered conditional retirement trigger FIRES** — first firing in corpus history; 4th retirement mechanism validated
3. **Pattern #28 structural inversion observation** — provider-being-consumed + multi-API-compat-as-runtime
4. **Pattern #18 Layer 0 runtime-bundled-launcher observation** — `ollama launch <runtime>` 33-file implementation at 170K-scale; potential 4-layer taxonomy extension
5. **Pattern #57 compound-2-wiki cross-corpus citation sub-variant** — Ollama Pi integration doc cites v36 pi-mono + v10 autoresearch-Karpathy in single doc
6. **Pattern #31 N=9 strengthening** — Ollama Cloud Pro $20/mo + Max $100/mo (9-entity commercial-entity data-point timeline); Pro-docs-depth 3/4
7. **Pattern #50 N=8 integration-driven-funnel sub-variant** — upsell pathway embedded in agent-runtime-integration workflow
8. **10-consecutive-wiki zero-new-candidates streak (CORPUS RECORD)** — extends v37-v45 9-streak
9. **2nd RED primitive-count** in corpus (after v41 browser-use inaugural)
10. **170K stars = largest non-aggregator OSS in corpus** (only build-your-own-x 491K + system-prompts-leaks 135K aggregators larger)
11. **Dual API-compat subdirs (openai/ + anthropic/) simultaneously** — corpus-first 2-vendor-API-compat runtime implementation
12. **Transparent local-cloud-proxy architecture** (`:cloud` suffix + cloud_proxy.go) — zero-code-change commercial upsell
13. **Modelfile declarative format** — corpus-first model-packaging format at runtime archetype
14. **First-party big-tech integrations from Microsoft + Google + AWS + Mozilla simultaneously** — 4 big-tech first-parties consume Ollama as runtime (non-reciprocal)
15. **Commercial-runtime-infrastructure-stability archetype** — Pattern #12 refined sub-observation (anti-feature-expansion discipline at 170K-scale)
16. **Third-party-unaware validation of corpus selection** — Ollama Pi integration doc independently cites 2 prior Storm Bear wiki subjects
17. **Pattern #47 first pre-registered conditional retirement FIRING** — 4th retirement mechanism validated
18. **35th consecutive Storm Bear meta-entity** (v10-v46 37-wiki window; v29 Phase 0.9 per-wiki evaluation discipline preserved)

---

## Cross-references

**Sibling wikis:**
- v10 autoresearch-Karpathy (cited verbatim in Ollama Pi integration; Pattern #57 citation)
- v20 fish-speech (outside-scope foundation-model; produces weights)
- v22 LlamaFactory + v23 Unsloth (outside-scope training-infra; trains weights)
- v24 Skyvern (Pattern #47 founding vision-primary; now conditional-retirement target)
- v25 awesome-design-md (Pattern #50 1st data point; absorbed into #68)
- v27 oh-my-claudecode (Pattern #57 1st data point)
- v29 crawl4ai (Pattern #47 refinement via DOM-only counter-evidence)
- v30 OpenHands (Pattern #31 N=4 + Pattern #57 2nd data point + MIT+enterprise precedent)
- v36 pi-mono (Pattern #18 Layer 0 integration target; cited in Ollama Pi integration doc)
- v37 bizos (outside-scope 7th sub-type OT#74)
- v41 browser-use (Pattern #47 3-point spectrum codification + Pattern #31 N=6 + Pattern #50 4th data point + first RED primitive-count)
- v42 ruflo (Pattern #31 N=7 + Pattern #50 5th data point + 3-layer commercial + conditional retirement trigger preregistration source)
- v43 rowboat (Pattern #50 6th 7-surface YC-S24)
- v44 magika (outside-scope 8th sub-type; most-recent predecessor)
- v45 shannon (Pattern #31 N=8 + Pattern #50 7th; SHANNON-PRO.md Pro-docs-depth 4/4 benchmark)

**Pattern Library:**
- PATTERN_LIBRARY.md full state: 37 confirmed + 20 active + 3 stale + 8 retired + 4 OT = 72 full / 57 active; ratio 0.54:1 UNPRECEDENTED preserved
- Post-next-mini-audit (if #47 retirement executed): ratio 0.513:1 NEW ALL-TIME-LOW

**Audit documents:**
- `04 Reviews/(C) 2026-04-24 Pattern Library mini-audit post-v42 (v41 deferred actions).md` — #47 conditional retirement preregistration source
- `04 Reviews/(C) 2026-04-24 Pattern Library mini-audit post-v45 (v43+v44+v45 harvest).md` — most-recent mini-audit

**Routine v2.1:**
- `/Users/Cvtot/KJ OS Template/05 Skills/llm-wiki-routine-v2.1.md` — protocol reference
- 8th v2.1-era execution (v32 onward); all 5+ discipline mechanisms exercised cleanly
