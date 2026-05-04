# ollama - Beginner Analysis — CLAUDE.md

> **Created:** 2026-04-24
> **Wiki #:** v46 (46th Storm Bear corpus wiki)
> **Routine:** `llm-wiki-routine-v2.1.md` (8th v2.1-era execution)
> **Source:** https://github.com/ollama/ollama
> **Status:** Phase 0-1 complete; executing Phases 2-6

---

## Positioning (verbatim)

> **Tagline:** "Start building with open models."
>
> **GitHub description:** "Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models."

**Integration bundling observed (README verbatim):**

> "You'll be prompted to run a model or connect Ollama to your existing agents or applications such as `Claude Code`, `OpenClaw`, `OpenCode`, `Codex`, `Copilot`, and more."

**Commercial tier (ollama.com/pricing verbatim):**
- **Pro**: $20/month (or $200/year) — "Run 3 cloud models at a time with 50x more cloud usage"
- **Max**: $100/month — "Run 10 cloud models at a time with 5x more usage than Pro"

## 12-axis classification (v2.1 Phase 0)

| Axis | Value |
|------|-------|
| **Tier** | **OUTSIDE-SCOPE — LLM-inference-runtime (9TH outside-scope sub-type candidate; NEW)** |
| **Archetype** | **Commercial-startup + open-core OSS runtime + high-adoption infrastructure** (MIT OSS + Ollama Cloud paid tier + 170K stars) |
| **Scale tier** | **X-large (170K stars)** — ≥#2 in corpus behind build-your-own-x 491K outside-scope + system-prompts-leaks 135K; **largest non-aggregator OSS project in corpus** |
| **Primary lang** | Go 64.7% + C 28.8% (llama.cpp backend) + TypeScript 3.5% + C++ 1.1% + Obj-C 0.5% + Shell 0.5% |
| **Packaging tool** | **5-channel multi-OS-binary**: curl installer (macOS+Linux) / PowerShell installer (Windows) / Docker Hub + Homebrew + Pacman + Nix + Helm + Flox + Guix (9+ third-party channels) + pip `ollama` (Python SDK) + npm `ollama` (JS SDK) |
| **Origin story** | Commercial-startup (Ollama, Inc.; ollama.com commercial entity) + open-core from day 1 + llama.cpp upstream lineage |
| **Methodology** | LLM-inference-runtime (local-first model serving) + Modelfile declarative format + dual-API-surface (OpenAI-compat + Anthropic-compat endpoints) |
| **Governance file count** | **Medium (3 files)** — README 18.7KB + CONTRIBUTING 3.6KB + SECURITY 1003B + LICENSE MIT + Dockerfile 9.8KB + CMakeLists.txt 15.2KB + .golangci.yaml; absent AGENTS.md / CLAUDE.md / CODE_OF_CONDUCT; explicit backwards-compat + new-feature discouragement discipline in CONTRIBUTING |
| **Agent/skill count** | N/A — not agent framework. Runtime exposes: 13+ REST API endpoints + 2 API-compat layers (OpenAI + Anthropic) + 10+ `ollama launch <runtime>` bundled integrations + Modelfile format + model registry. Consumed BY agents. |
| **i18n coverage** | EN-only (docs.ollama.com) |
| **Intellectual influence cited** | **llama.cpp + Georgi Gerganov** (founder credit in README "Supported backends"); NO individual-author AI-space lineage (no Karpathy / Lam / BMAD citations) |
| **Agent platforms supported** | **20 agent/runtime/IDE/chat integrations** documented first-class via `ollama launch` or dedicated mdx docs (Claude Code + OpenClaw + Hermes + OpenCode + Codex + Copilot CLI + Droid + Goose + Pi (pi-mono v36) + NemoClaw + Cline + Roo Code + VS Code + JetBrains + Xcode + Zed + Onyx + n8n + marimo) + 100+ community integrations via README directory |

## Scope classification rationale

**OUTSIDE-SCOPE per Storm Bear corpus definition:**
- Not primarily an agent framework
- Not extending Claude Code or agent platforms as consumer — instead, **Ollama IS the provider that agents consume** (structural inversion of Pattern #28)
- Primary use is runtime for running open-weight LLMs locally (inference-runtime distinct from foundation-model / training-infrastructure)
- **Decision: outside-scope LLM-inference-runtime 9th sub-type** (precedent: fish-speech v20 foundation-model, LlamaFactory v22 + Unsloth v23 training-infra, magika v44 ML-security-classifier)

**Distinct from 8 prior outside-scope sub-types:**
1. education-aggregator (build-your-own-x v8; absorbed into #68 at v31)
2. foundation-model (fish-speech v20) — **produces model weights** (Ollama consumes them)
3. prompt-leak-archive (system-prompts-leaks v21)
4. training-infrastructure (LlamaFactory v22 + Unsloth v23) — **trains model weights** (Ollama runs inference)
5. design-template-aggregator (awesome-design-md v25; absorbed into #68)
6. MCP-server-aggregator (awesome-mcp-servers v31; absorbed into #68)
7. business-OS-as-product (bizos v37 OT#74)
8. ML-security-classifier (magika v44)
9. **LLM-inference-runtime (ollama v46)** — NEW

**7-test criteria for LLM-inference-runtime sub-type (formalized in Phase 4b):**
1. Runtime for running model weights at inference time (not training, not producing weights)
2. Consumed BY agents as provider (structural inversion from typical Pattern #28 provider-being-consumed sub-observation)
3. Local-first deployment model (not cloud-only)
4. Multi-OS binary distribution (macOS + Windows + Linux + Docker)
5. Model registry + declarative model-packaging format (e.g., Modelfile)
6. Multi-provider-API-compat surface (OpenAI-compat + Anthropic-compat simultaneously)
7. Upstream integration with inference library (e.g., llama.cpp via MLX / CUDA / Metal backends)

## Phase 0.5 Pattern pre-check — MANDATORY

### 🔴 CRITICAL: Pattern #47 conditional retirement trigger FIRES at v46

Per v42-deferred mini-audit pre-registered conditional retirement trigger:
> "If no 2nd vision-primary data point by v46, retire Pattern #47 + replace with OBSERVATION-TRACK 'Browser-Agent Architectural-Approach 3-point spectrum'"

**v46 verification:**
- Is ollama vision-primary? **NO** (ollama is LLM runtime, not browser agent)
- Wikis v42-v45 (rowboat / magika / shannon) also NOT vision-primary browser agents
- **2nd vision-primary data point did NOT arrive by v46**
- **Conditional retirement trigger FIRES** — Pattern #47 → retire at next mini-audit + replace with OBSERVATION-TRACK

This is the **FIRST pre-registered conditional retirement trigger to actually fire in corpus history** (structural first). Documented here for next mini-audit action; no direct action at v46 wiki (audit handles retirement + OT registration).

### Strengthening / promotion candidates (no status changes at v46; documented for next audit)

1. **Pattern #17 variant 3 commercial-startup ecosystem** (CONFIRMED) → **data point** (Ollama, Inc. + ollama.com commercial entity + Ollama Cloud Pro/Max tiers + ollama-python + ollama-js + Discord + Reddit + Twitter). Strengthening — counts as 17th+ observation.
2. **Pattern #31 Open-Core Commercial Entity** (CONFIRMED N=8 after v45 shannon) → **N=9 strengthening** (Ollama MIT core + Ollama Cloud Pro $20/mo + Max $100/mo commercial tiers). 9 distinct commercial entity data points. Pro-docs-depth signal (per v45 formalization 0-4 axis): **3/4** (dedicated /pricing page + /cloud.mdx docs + account signin flow; no dedicated SHANNON-PRO.md-equivalent).
3. **Pattern #50 Commercial-Funnel Companion Platform** (CONFIRMED N=7 after v45) → **N=8 strengthening** (ollama.com + Ollama Cloud + /pricing + /search?c=cloud + account flow + Discord + Reddit + Twitter; 7-surface funnel). Ties rowboat v43 / ruflo v42 / shannon v45 for corpus-most-elaborate.
4. **Pattern #18 Agent Runtime Standardization** (CONFIRMED + 3-tier MCP formulation extended v42) → **MASSIVE strengthening at 170K-star scale**. Ollama ships `ollama launch <runtime>` for 10+ agent runtimes (Claude Code / OpenClaw / Hermes / OpenCode / Codex / Copilot CLI / Droid / Goose / Pi / NemoClaw) with dedicated `/docs/integrations/*.mdx` per runtime. Pattern #18 Layer 2 (OpenClaw + Hermes community-platform-scoped) validated at infrastructure-runtime scale. **`ollama launch <runtime>` as corpus-first runtime-bundled-agent-launcher primitive.**
5. **Pattern #28 Multi-Provider AI Support STRUCTURAL INVERSION observation** (CONFIRMED) — **Ollama is the PROVIDER being consumed by 11+ Pattern #28 prior wiki subjects** (LiteLLM / LangChain / LangChain4j / LangChainGo / Spring AI / Semantic Kernel / LlamaIndex / Haystack / Firebase Genkit / Portkey / Mozilla any-llm). Also inversely: **Ollama itself exposes OpenAI-compat + Anthropic-compat API-compatibility-layer subdirs** (`openai/` 5 files + `anthropic/` 3 files) — corpus-first 2-vendor-API-compat simultaneous-implementation. Within-Pattern-#28 observational sub-framing "provider-being-consumed" + "multi-API-compat-as-runtime".
6. **Pattern #2 Distribution Evolution** — **multi-OS-binary at 170K-scale** (corpus-first): macOS DMG + curl + Windows EXE + PowerShell + Linux curl + Docker + Homebrew + Pacman + Nix + Helm + Flox + Guix + pip (Python SDK) + npm (JS SDK) = 13+ distribution surfaces. Observational within #2.
7. **Pattern #22 AGENTS.md** — **absent** (consistent with outside-scope + runtime archetype). `.golangci.yaml` present as Go-native discipline file. Observational.
8. **Pattern #12 Governance-Depth (refined 3-factor v42)** — Ollama at 170K stars + commercial-startup + medium governance (3 files + backwards-compat-discouragement + CI discipline) → fits refined formulation correlating with maturity-ambition + maintainer-philosophy + scale-tier (not organization-size-as-predictor alone). Backwards-compat discipline explicit in CONTRIBUTING ("Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API) may not be accepted") = **commercial-runtime-infrastructure stability signal**.
9. **Pattern #29 License-Category-Diversity** — MIT strengthening (consistent with high-adoption OSS-runtime archetype).
10. **Pattern #19 Tool-lineage archetype 4 (no-individual-lineage)** — llama.cpp credit ("project founded by Georgi Gerganov") = tool-lineage, not individual-AI-space-author-lineage (no Karpathy / Lam / BMAD cited). Consistent with archetype 4. Meta-reference observation: Ollama integration docs cite **Pi (pi-mono v36)** and **pi-autoresearch (Karpathy autoresearch v10)** as integrations — **cross-corpus citation by third party** (Ollama's Pi integration docs reference Karpathy autoresearch verbatim). Pattern #57 Recursive Corpus Reference **new data point (3rd observation after v27 OMC + v30 OpenHands academic lineage chain)**.

### Potential un-stale — Pattern #52 Extreme-Viral-Velocity

- **Pattern #52** stale-flagged v31 (awesome-design-md 60K stars in 20 days baseline)
- Ollama scale: 170K stars / project age ~2.5 years (launched ~2023) ≈ 5,600 stars/month average. Not extreme-viral-velocity (≥1K/day) at sustained pace.
- **Decision:** NOT un-staling. Ollama represents sustained-organic-infrastructure-growth sub-path — observationally distinct from community-viral but NOT extreme-velocity.

### Observational / scope-respected patterns

11. **Pattern #47 Vision-Based Browser Automation** — **scope-distinct** (ollama not browser agent); FIRES conditional retirement trigger per above.
12. **Pattern #48 Proprietary Anti-Bot Commercial Moat** — scope-distinct (ollama not browser agent).
13. **Pattern #58 Branding-Package Divergence** — `ollama` package name consistent across GitHub + npm + pip + ollama.com + brew. No divergence. Observational-negative.
14. **Pattern #42 Academic-Published** — NO peer-reviewed publication cited; ollama is practitioner-focused (not research-paper-chain). Observational-negative.
15. **Pattern #44 Academic-Lab Affiliation** — NO academic-lab affiliation. Commercial-startup archetype. Observational-negative.

### Overlap pre-check

All observations route to within-existing-pattern strengthening or observational-negative. **0 new active candidates target** (10-consecutive-zero-registration streak goal v37-v46 extending 9-streak from v45).

### Un-stale check

- #45 Dual-Licensing — not applicable (single MIT; no dual-license architecture)
- #52 Extreme-Viral-Velocity — not applicable (sustained-organic, not extreme-velocity)
- #71 Interactive Self-Assessment — not applicable
- #72 PolyForm Noncommercial — not applicable (MIT)
- All negative. Disciplined.

## Phase 0.9 Primitive-count probe — EXPECTED RED

Estimated primitives from 4 signals:

1. **README TOC** — 14 top-level sections (Download / Get started / REST API / Python / JavaScript / Supported backends / Documentation / Community Integrations with 10 sub-categories including 100+ items)
2. **Repo folder structure** — **38 top-level subdirs** (anthropic/api/app/auth/cmd/convert/discover/docs/envconfig/format/fs/harmony/integration/internal/kvcache/llama/llm/logutil/manifest/middleware/ml/model/openai/parser/progress/readline/runner/sample/scripts/server/template/thinking/tokenizer/tools/types/version/x/) — **larger than browser-use v41 (17 subdirs) + ruflo v42 (~500 primitives EXTREME ecosystem)**
3. **Documented primitives from runtime domain:**
   - 13+ REST API endpoints (/api/generate, /api/chat, /api/create, /api/pull, /api/push, /api/list, /api/show, /api/copy, /api/delete, /api/embeddings, /api/ps, /api/version, /api/image-generation-experimental)
   - 2 API-compat layers (OpenAI `openai/` 5 files ~160KB / Anthropic `anthropic/` 3 files ~83KB)
   - 10+ `ollama launch <runtime>` integrations (cmd/launch/ 33 files including claude/cline/codex/copilot/droid/hermes/kimi/openclaw/opencode/pi/vscode)
   - Modelfile declarative format (parser/ + template/ subdirs)
   - Model registry + auth (manifest/ + auth/ + middleware/ + server/auth.go + download.go + cloud_proxy.go)
   - Multi-backend inference (llama/ llama.cpp integration + llm/ + ml/ + runner/ + harmony/ + thinking/ + tools/)
   - MLX version pinning (MLX_VERSION + MLX_C_VERSION files — Apple Silicon backend)
   - Quantization engine (server/quantization.go 11KB + tests 28.3KB)
   - 12+ Modelfile commands
   - 20+ CLI commands (cmd/cmd.go 62.2KB)
   - Cloud Proxy (server/cloud_proxy.go 14.5KB — Ollama Cloud tier integration)
4. **CMakeLists.txt** 15.2KB — C++ build config for native runtime (MLX + llama.cpp compilation)

**Estimated primitive count: ~250-400 (RED tier per v41 browser-use ~200 precedent; below ruflo v42 EXTREME ~500+)**

**Outcome: RED — 2nd RED in corpus** (v41 browser-use inaugural, v46 ollama 2nd).

**Compression decisions:**
- 4-entity format preserved
- Aggressive citation-not-replication (REST API endpoints cited to docs.ollama.com/api; Modelfile commands cited to docs.ollama.com/modelfile; community integration directory cited to README not enumerated)
- Lossy compression accepted for: per-CLI-flag enumeration / per-subdirectory architecture walkthrough / 100+ community integration enumeration
- **4 follow-up deep-dive wikis flagged:**
  1. Ollama REST API + Modelfile format deep-dive
  2. API-compatibility-layer architecture deep-dive (openai/ + anthropic/ implementation)
  3. `ollama launch <runtime>` integration protocol deep-dive (10+ bundled agent launchers)
  4. Multi-backend inference pipeline (MLX + llama.cpp) deep-dive
- Velocity tolerance: ~3h (RED +50% overhead vs ~2h GREEN baseline per v41 precedent)

## Storm Bear meta-entity applicability (Phase 0.9)

**Applicable = YES (35th consecutive).** Meta-entity warranted to:
- Document Storm Bear pilot relevance **LOW-MEDIUM** (privacy-sensitive Scrum coaching workflow pilot via local LLM + cost-optimization pilot)
- Formalize LLM-inference-runtime 9th outside-scope sub-type
- Pattern #47 conditional retirement trigger FIRES documentation (structural-first corpus event)
- Pattern #57 Recursive Corpus Reference 3rd data point (Ollama cites Pi v36 + pi-autoresearch-Karpathy-v10 verbatim — third-party-unaware cross-corpus citation like v39 dive-into-llms cited LlamaFactory v22)
- Ollama is commercial-runtime-infrastructure peer Storm Bear operator might evaluate for VN-client-data-privacy Scrum coaching workflows

## Phase 4b routing mode

**Primary:** Outside-scope 9th sub-type LLM-inference-runtime formalization + Pattern #47 conditional retirement trigger FIRES + Pattern #28 inversion observation + Pattern #18 runtime-bundled-agent-launcher strengthening.

**Secondary:** Pattern #57 Recursive Corpus Reference 3rd data point + Pattern #31 N=9 + Pattern #50 N=8 strengthening.

## Sibling references (mandatory Phase 2-4b cross-links)

- **v20 fish-speech** — outside-scope foundation-model precedent (produces weights; ollama consumes)
- **v22 LlamaFactory + v23 Unsloth** — outside-scope training-infrastructure precedent (trains weights; ollama runs inference)
- **v44 magika** — most-recent outside-scope precedent (ML-security-classifier 8th sub-type)
- **v8 build-your-own-x** — first outside-scope precedent
- **v37 bizos** — outside-scope business-OS-as-product (7th sub-type)
- **v10 autoresearch (Karpathy)** — cited by Ollama's Pi integration docs ("Inspired by Karpathy's autoresearch") — cross-corpus citation
- **v36 pi-mono (Mario Zechner)** — cited by Ollama's Pi integration docs as first-class integration
- **v27 oh-my-claudecode** — Pattern #57 Recursive Corpus Reference precedent
- **v41 browser-use** — Pattern #47 conditional-retirement-trigger predecessor + FIRST RED primitive-count precedent
- **v42 ruflo** — EXTREME primitive-count precedent (ollama v46 RED below EXTREME tier)
- **v45 shannon** — Pattern #31 N=8 immediate predecessor + Pattern #50 N=7 predecessor + pre-audit state baseline

## Final deliverables target

- 1 project CLAUDE.md (this file)
- 3 cluster summaries:
  1. README + positioning + multi-OS distribution + quick-start
  2. Architecture overview (38-subdir Go monorepo + inference pipeline + dual-API layers + model registry + Modelfile + `ollama launch` runtime-bundled-agent-launchers)
  3. Commercial structure (ollama.com + Ollama Cloud Pro/Max + Docker Hub + community ecosystem)
- 4 entity pages:
  1. Core product (ollama CLI + REST API + Modelfile + model registry + 10+ `ollama launch` bundled runtimes)
  2. Commercial + ecosystem (ollama.com + Ollama Cloud + 100+ community integrations + Pattern #31 N=9 + Pattern #50 N=8)
  3. Outside-scope 9th sub-type formal definition + Pattern #47 conditional retirement trigger FIRES + Pattern #28 inversion + Pattern #57 3rd data point
  4. 35th consecutive Storm Bear meta-entity (LLM-inference-runtime pilot relevance LOW-MEDIUM)
- 1 bilingual VN+EN beginner guide (~420-480 lines, 12-13 parts — install workflow + Modelfile basics + OpenAI/Anthropic-compat setup + 2-week eval roadmap + LOW-MEDIUM pilot framing)
- 1 Phase 4b primary deliverable (~650-750 lines): Outside-scope 9th sub-type + Pattern #47 conditional-retirement-fires + Pattern #28 inversion + Pattern #18 runtime-bundled-launcher strengthening
- 1 iteration log v46 with 13 sections
- 1 index + 1 log + 1 open-questions

## Cross-references

- Parent routine: `/Users/Cvtot/KJ OS Template/05 Skills/llm-wiki-routine-v2.1.md`
- Pattern register: `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md`
- Root CLAUDE: `/Users/Cvtot/KJ OS Template/CLAUDE.md`
- Root GOALS: `/Users/Cvtot/KJ OS Template/GOALS.md`
