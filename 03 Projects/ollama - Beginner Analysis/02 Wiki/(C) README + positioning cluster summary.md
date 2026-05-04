# (C) ollama — README + positioning cluster summary

> **Source cluster 1 of 3.** Maps the user-facing README (18.7 KB), the ollama.com landing + /pricing + /cloud.mdx commercial surface, and the 100+-item community integrations directory that occupies ~60% of README line count.

---

## 1. Verbatim positioning

**GitHub repo description:**
> "Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models."

**README tagline (line 9):**
> "Start building with open models."

**ollama.com landing:**
> "the easiest way to build with open models"

**Ollama Cloud pitch (docs/cloud.mdx line 7, verbatim):**
> "Ollama's cloud models are a new kind of model in Ollama that can run without a powerful GPU. Instead, cloud models are automatically offloaded to Ollama's cloud service while offering the same capabilities as local models, making it possible to keep using your local tools while running larger models that wouldn't fit on a personal computer."

**Philosophy (CONTRIBUTING.md line 22-25):**
> "Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API) [may not be accepted] / Changes that add significant friction to the user experience [may not be accepted] / Changes that create a large future maintenance burden for maintainers and contributors [may not be accepted]."

This is **commercial-runtime-infrastructure-stability discipline** — distinct tone from feature-rich agent-framework wikis (BMAD v11 / spec-kit v17 / ruflo v42). Maps to Pattern #12 Governance-Depth refined 3-factor formulation (maintainer-philosophy + maturity-ambition + scale-tier).

## 2. Scale + project metadata (WebFetch 2026-04-24)

| Axis | Value | Corpus ranking |
|------|-------|---------------|
| Stars | **170,000** | **#2 in corpus** behind build-your-own-x 491K (outside-scope meta-reference); largest non-aggregator OSS project in corpus (surpasses system-prompts-leaks v21 135K meta-reference) |
| Forks | 15,800 | 9.3% fork-to-star ratio — mid-range |
| Watchers | 955 | High absolute count |
| Open issues | 2,200 | High absolute (matched by very-large-scale projects) |
| Commits | 5,344 | Active |
| License | MIT | Permissive |
| Primary lang | Go 64.7% + C 28.8% + TS 3.5% + C++ 1.1% + Obj-C 0.5% + Shell 0.5% | **First multi-language runtime at X-large scale** |
| Latest release | v0.21.2 (2026-04-23) | Shipped yesterday = active |
| Homepage | ollama.com | Commercial entity site |
| GitHub description | See §1 | Cites 7 specific model families by name |

**Scale classification: X-large (60K-200K)** — fits between OpenHands v30 (72K) and system-prompts-leaks v21 (135K outside-scope).

## 3. Multi-OS distribution surface (Pattern #2 strengthening)

**README Download section (lines 13-44) enumerates 5 official install channels + Libraries section:**

| OS | Install | Artifact |
|----|---------|---------|
| macOS | `curl -fsSL https://ollama.com/install.sh \| sh` | Ollama.dmg binary |
| Windows | `irm https://ollama.com/install.ps1 \| iex` | OllamaSetup.exe binary |
| Linux | `curl -fsSL https://ollama.com/install.sh \| sh` | Manual install docs |
| Docker | Docker Hub `ollama/ollama` | Official image |
| npm | `npm i ollama` (ollama-js SDK) | — |
| pip | `pip install ollama` (ollama-python SDK) | — |

**+ 9 package-manager channels (README lines 349-357):**
- Pacman (Arch Linux)
- Homebrew (macOS)
- Nix
- Helm Chart (Kubernetes)
- Gentoo
- Flox
- Guix channel

**→ 13+ distribution surfaces at 170K-scale.** Corpus-first **multi-OS-native-binary-at-infrastructure-scale** observation. Strengthening-within-Pattern-#2 (not new candidate; distribution-evolution pattern observation).

## 4. Runtime-bundled-agent-launcher primitive (Pattern #18 MASSIVE strengthening)

**README lines 53-76:** `ollama launch <runtime>` one-command spawning of integrated coding agents or personal-AI-assistants.

Documented first-class integrations (README + docs/integrations/*.mdx 20 files):

**Coding Agents (7):**
- `ollama launch claude` → Claude Code with Anthropic-compat API (`ANTHROPIC_BASE_URL=http://localhost:11434`)
- `ollama launch codex` → OpenAI Codex with OpenAI-compat API
- `ollama launch copilot` → GitHub Copilot CLI
- `ollama launch droid` → Factory.ai Droid
- `ollama launch goose` → Block Goose
- `ollama launch opencode` → OpenCode
- `ollama launch pi` → **Pi (pi-mono v36 Mario Zechner)** — CORPUS-FIRST cross-runtime integration

**AI Assistants (2):**
- `ollama launch openclaw` → OpenClaw (WhatsApp/Telegram/Slack/Discord/iMessage bridge)
- `ollama launch hermes` → Hermes Agent

**IDEs/Editors (6):**
- VS Code, Cline, Roo Code, JetBrains, Xcode, Zed

**Notebooks + automation (2):**
- marimo, n8n

**Chat/RAG (1):**
- Onyx

**cmd/launch/ subdirectory file sizes** (scope signal):

| Runtime | `cmd/launch/<name>.go` size |
|---------|----------------------------|
| openclaw | 27.4 KB |
| vscode | 16.8 KB |
| hermes | 16.4 KB |
| launch (core) | 29.2 KB |
| droid | 5.0 KB |
| cline | 2.3 KB |
| codex | 3.6 KB |
| copilot | 1.7 KB |
| pi | 10.2 KB |
| claude | 1.9 KB |
| opencode | 6.2 KB |
| kimi | 8.5 KB |
| models | 14.8 KB |
| registry | 11.5 KB |

Total: ~160 KB Go code + massive test files (`_test.go` typically 2-3× larger) across 33 files in `cmd/launch/`.

**Pattern #18 Agent Runtime Standardization Layer-0 observation:** Ollama introduces a new layer below Layer 1 MCP — **runtime-bundled-agent-launcher Layer 0** where the inference runtime itself ships `launch <runtime>` commands for 10+ agent runtimes. MASSIVE corpus strengthening at 170K-star scale; Pattern #18 formulation may extend at next audit to 4-layer taxonomy (Layer 0 runtime-bundled-launcher / Layer 1 MCP / Layer 2 community-platform-scoped / Layer 3 per-runtime).

## 5. REST API + dual API-compatibility layer (Pattern #28 STRUCTURAL INVERSION observation)

**Native REST API (README lines 90-105 + docs/api.md):**

13+ endpoints:
- POST /api/generate (completion)
- POST /api/chat (chat completion)
- POST /api/create (create model from Modelfile)
- GET /api/tags (list local models)
- POST /api/show (show model info)
- POST /api/copy (copy model)
- DELETE /api/delete (delete model)
- POST /api/pull (pull from registry)
- POST /api/push (push to registry)
- POST /api/embeddings (generate embeddings)
- GET /api/ps (list running models)
- GET /api/version
- POST /api/image-generation (experimental)

Default bind: `http://localhost:11434`.

**Dual API-compat subdirs (CORPUS-FIRST structural observation):**

- `openai/` — 5 files ~158 KB total (openai.go 26.2KB + responses.go 41.1KB + openai_test.go 21.3KB + responses_test.go 65.7KB + openai_encoding_format_test.go 3.9KB) — **OpenAI-compatible API endpoints**
- `anthropic/` — 3 files ~83 KB total (anthropic.go 31.9KB + anthropic_test.go 42.7KB + trace.go 9.3KB) — **Anthropic-compatible API endpoints**

**This is a structural inversion of Pattern #28 Multi-Provider AI Support:**

Prior Pattern #28 framing: Framework X supports providers A, B, C, ... (consumer-side abstraction). 11 prior corpus wikis documented this pattern (ruflo v42 / browser-use v41 / DeepTutor v38 / claude-context v40 / etc.).

**Ollama inverts:**
1. Ollama IS the provider consumed by 11+ prior Pattern #28 wikis (LiteLLM / LangChain / LangChain4j / Spring AI / Semantic Kernel / LlamaIndex / Haystack / Firebase Genkit / Portkey / Mozilla any-llm / pi-mono pi-ai) per README Libraries & SDKs section (lines 229-259).
2. Ollama itself exposes **2 vendor-API-compat layers simultaneously** (OpenAI-compat + Anthropic-compat) so consumers that expect OpenAI or Anthropic SDK can swap in Ollama by changing base URL. This is a **multi-API-compat-as-runtime** sub-pattern corpus-first.

Concrete evidence: Claude Code integration (docs/integrations/claude-code.mdx lines 113-121) uses Anthropic-compat:
```shell
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434
```

And typical OpenAI-compat SDK consumers (pi-mono via `api: "openai-completions"` + `baseUrl: http://localhost:11434/v1`; docs/integrations/pi.mdx lines 86-99) use OpenAI-compat.

**Within-Pattern-#28 observational framing:** "provider-being-consumed" + "multi-API-compat-as-runtime." Documented as strengthening; no new candidate (consolidation-forward discipline).

## 6. Community integrations directory (README lines 152-357, Pattern #17/#27 strengthening)

README is ~60% community-integrations directory — 100+ projects across 11 categories:

| Category | Count (representative) | Notable items |
|---------|------------------------|----------------|
| Chat Interfaces (Web) | 16 | Open WebUI, Onyx, LibreChat, Lobe Chat, NextChat, Perplexica, big-AGI, Chatbox |
| Desktop clients | 23 | Dify.AI, AnythingLLM, Cherry Studio, Alpaca, Enchanted, Msty, Witsy |
| Mobile | 7+ | SwiftChat, Enchanted, Maid, Ollama App, Reins, ConfiChat |
| Code Editors & Dev | 16 | Cline, Continue, Void, twinny, gptel, Ollama Copilot, Obsidian Local GPT, VT Code, QodeAssist, AI Toolkit for VS Code, Open Interpreter |
| Libraries & SDKs | **~30** | **LiteLLM, Semantic Kernel, LangChain4j, LangChainGo, Spring AI, LangChain / LangChainJS, ruby_llm, any-llm (Mozilla), OllamaSharp, LangChainRust, LangChainDart, Agents-Flex, Elixir LangChain, Ollama-rs, LangChain .NET, chromem-go, LlmTornado, Ollama4j, ollama-laravel, ollama-swift, LlamaIndex / LlamaIndexTS, Haystack, Firebase Genkit, Ollama-hpp, PromptingTools.jl, rollama, Portkey, Testcontainers, LLPhant** |
| Frameworks & Agents | 8 | AutoGPT, crewAI, Strands Agents (AWS), Cheshire Cat, any-agent (Mozilla), Stakpak, Hexabot, Neuro SAN (Cognizant) |
| RAG & Knowledge | 9 | RAGFlow, R2R, MaxKB, Minima, Chipper, ARGO, Archyve, Casibase, BrainSoup |
| Bots & Messaging | 5 | LangBot, AstrBot, Discord-Ollama, Ollama Telegram, LLM Telegram |
| Terminal & CLI | 11 | aichat, oterm, gollama, tlm, tenere, ParLlama, llm-ollama, ShellOracle, LLM-X, cmdh, VT |
| Productivity & Apps | 16 | AppFlowy, Screenpipe, Vibe, Page Assist, NativeMind, Ollama Fortress, 1Panel, Writeopia, QA-Pilot, Raycast, Painting Droid, Serene Pub, Mayan EDMS, TagSpaces |
| Observability | 6 | Opik, OpenLIT, Lunary, Langfuse, HoneyHive, MLflow Tracing |
| Database & Embeddings | 4 | pgai (TimescaleDB), MindsDB, chromem-go, Kangaroo |
| Infrastructure | 3 | Google Cloud, Fly.io, Koyeb, Harbor |

Total: **~130+ items** across 13 sub-categories.

**Pattern #17 Ecosystem-Layer Organizations strengthening:** Ollama, Inc. + ollama.com commercial entity sits atop an ecosystem-layer where 130+ community integrations consume the runtime. Not a new variant — consistent with variant 3 commercial-startup ecosystem-portfolio-strategy (ruflo v42 / Rowboat Labs v43 / Zilliz v40 / VoltAgent v25 precedents).

**Pattern #27 Community-Viral Scale Path strengthening:** 170K stars / ~2.5-year project age (Ollama announced July 2023) ≈ 5,600 stars/month sustained-organic-infrastructure-growth sub-path. Not extreme-viral (Pattern #52 criteria not met — ollama did NOT ship 1K+ stars/day at sustained pace). Joins shannon v45 (2.5K/mo organic-commercial) and OpenHands v30 (~2,867/mo corporate-academic-amplified) in sustained-growth tier.

## 7. Supported backend + intellectual lineage (Pattern #19 archetype 4)

**README line 143 verbatim:**
> "[llama.cpp](https://github.com/ggml-org/llama.cpp) project founded by Georgi Gerganov."

Only supported backend explicitly named. No individual-author AI-space lineage cited (no Karpathy / Lam / Anthropic team / Boris Cherny mentions).

**Pattern #19 Intellectual Lineage archetype 4 (tool-lineage no-individual-author):** Ollama fits cleanly — technical foundation credited to llama.cpp + Georgi Gerganov upstream without adopting individual-author intellectual positioning. Consistent with other outside-scope-runtime archetypes.

**However:** Ollama's Pi integration docs (docs/integrations/pi.mdx lines 65-80) cite **"Karpathy's autoresearch"** verbatim:

> "[pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) brings autonomous experiment loops to Pi. Inspired by Karpathy's autoresearch, it turns any measurable metric into an optimization target..."

**Pattern #57 Recursive Corpus Reference 3rd data point (CORPUS-FIRST compound cross-corpus citation):** Ollama cites BOTH **Pi (pi-mono v36 Mario Zechner)** AND **Karpathy's autoresearch (v10)** — 2 prior corpus wiki subjects referenced in one integration document by a third party unaware of Storm Bear corpus. This is the 3rd Pattern #57 data point (after v27 OMC cited v1 ECC + v2 Superpowers; v30 OpenHands cited academic lineage). Distinct sub-variant: **compound-2-wiki cross-corpus citation in single doc**.

## 8. Context-length + cloud-model mechanics

**docs/integrations/claude-code.mdx line 135:**
> "Note: Claude Code requires a large context window. We recommend at least 64k tokens. See the [context length documentation](/context-length) for how to adjust context length in Ollama."

**docs/cloud.mdx:** Cloud models run on Ollama datacenter GPUs; accessed via `ollama signin` + `:cloud` suffix in model names (e.g., `kimi-k2.5:cloud`, `glm-5:cloud`, `qwen3.5:cloud`, `minimax-m2.7:cloud`). Local and cloud models share same CLI / API surface — **transparent local-cloud-split with no code change required** = commercial hook.

Ollama Cloud pricing (ollama.com/pricing):

| Tier | Price | Spec |
|------|-------|------|
| Free (account) | $0 | Basic cloud included free with account |
| Pro | $20/mo or $200/yr | "Run 3 cloud models at a time with 50x more cloud usage" |
| Max | $100/mo | "Run 10 cloud models at a time with 5x more usage than Pro" |

**Pattern #31 Open-Core Commercial Entity N=9 strengthening** (after v45 shannon N=8 baseline). Pro-docs-depth signal (per v45 0-4 axis):
- ollama.com/pricing dedicated page: ✅
- docs/cloud.mdx dedicated doc: ✅ (232 lines)
- account signin flow: ✅
- dedicated SHANNON-PRO.md-style upsell file: ❌

**Depth = 3/4** (vs shannon v45 4/4 with SHANNON-PRO.md 26KB).

## 9. Notable absences

- **No AGENTS.md** — consistent with outside-scope runtime archetype (Pattern #22 absence observation; runtime doesn't need "how to use this framework with agents" since runtime IS the thing agents connect to).
- **No CLAUDE.md** — absent despite first-class Claude Code integration via `ollama launch claude`.
- **No CODE_OF_CONDUCT.md.**
- **No MAINTAINERS.md / GOVERNANCE.md** — team opaque to public.
- **No peer-reviewed paper** — practitioner-focused (Pattern #42 negative observational).
- **No academic-lab affiliation** — commercial-startup archetype (Pattern #44 negative observational).
- **No branding-package divergence** — `ollama` is consistent across GitHub repo + npm package + pip package + ollama.com + Homebrew formula (Pattern #58 negative observational).
- **EN-only** — docs.ollama.com has no non-EN localization (notable at 170K-scale — contrasts ruflo v42 / DeepTutor v38 / LlamaFactory v22 CJK-variant i18n).

## 10. Corpus-firsts enumerated from this cluster

1. **LLM-inference-runtime** as 9th outside-scope sub-type (formalized Phase 4b)
2. **Multi-OS-native-binary distribution at 170K-scale** — 5 OS channels + 9 package managers (13+ total surfaces)
3. **Dual API-compatibility layer simultaneously** (`openai/` + `anthropic/` subdirs) — corpus-first 2-vendor-API-compat implementation
4. **`ollama launch <runtime>` runtime-bundled-agent-launcher primitive** — 10+ bundled agent runtimes at infrastructure-runtime level; potential Pattern #18 Layer 0 extension
5. **Pattern #28 structural inversion** — provider-being-consumed-by-agents (11+ prior Pattern #28 wikis consume Ollama)
6. **Pattern #57 compound-cross-corpus citation** — single integration doc (Pi) cites 2 prior corpus wiki subjects (pi-mono v36 + autoresearch-Karpathy v10)
7. **Commercial-runtime-infrastructure-stability discipline in CONTRIBUTING** — explicit backwards-compat-preservation + new-feature-discouragement
8. **Ollama Cloud transparent local-cloud-split with `:cloud` suffix** — zero-code-change commercial upsell pathway
9. **Third-party runtime integration docs directory at 20 files** — docs/integrations/*.mdx each dedicated to one consumer runtime (Claude Code 136 lines, Pi 110 lines, OpenClaw 96 lines, etc.)
10. **Largest non-aggregator OSS project in Storm Bear corpus** (170K stars — only build-your-own-x 491K outside-scope meta-reference and system-prompts-leaks 135K outside-scope are larger; both aggregators)

## 11. Pattern delta summary

| Pattern | Delta |
|---------|-------|
| #17 variant 3 commercial-startup | Data point strengthening (Ollama, Inc. + ollama.com + Ollama Cloud + 130+ ecosystem) |
| #18 Agent Runtime Standardization | **MASSIVE** strengthening — Layer 0 runtime-bundled-launcher observation; potential 4-layer taxonomy extension |
| #19 archetype 4 tool-lineage no-individual | Fit (llama.cpp credit only) |
| #22 AGENTS.md | Absent (consistent outside-scope) |
| #27 Community-Viral | 20+th observation; sustained-organic-infrastructure sub-path |
| #28 Multi-Provider AI Support | **STRUCTURAL INVERSION** observation — provider-being-consumed + multi-API-compat-as-runtime |
| #29 License-Category-Diversity | MIT strengthening |
| #2 Distribution Evolution | 13+ surface multi-OS observation |
| #12 Governance-Depth (refined) | Commercial-runtime-infrastructure-stability sub-observation |
| #31 Open-Core Commercial Entity | **N=9 strengthening** (Pro $20/mo + Max $100/mo); Pro-docs-depth = 3/4 |
| #42 Academic-Published | Absent (practitioner-focused) |
| #44 Academic-Lab Affiliation | Absent (commercial-startup) |
| #47 Vision-Based Browser Automation | **CONDITIONAL RETIREMENT TRIGGER FIRES** (scope-distinct; no vision-primary at v46) |
| #48 Proprietary Anti-Bot Commercial Moat | Scope-distinct |
| #50 Commercial-Funnel Companion Platform | **N=8 strengthening** (7-surface funnel) |
| #52 Extreme-Viral-Velocity (stale) | Not un-staled (sustained-organic, not extreme) |
| #57 Recursive Corpus Reference | **3rd data point** + compound-2-wiki sub-variant (NEW) |
| #58 Branding-Package Divergence | Negative (consistent `ollama` everywhere) |

**New active candidates target:** 0 (10-consecutive-wiki zero-registration extending v37-v45 9-streak).
