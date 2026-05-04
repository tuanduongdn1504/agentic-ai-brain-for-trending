# (C) Entity: Commercial ecosystem — Ollama Cloud + 130+ integrations + Pattern #31 N=9 + Pattern #50 N=8

> **Entity 2 of 4.** Maps commercial structure (ollama.com + Pro/Max tiers + transparent proxy architecture), 130+ community ecosystem, cross-corpus-citation Pattern #57 evidence, and Pattern #31/#50 strengthening details.

---

## 1. Identity

- **Commercial entity:** Ollama, Inc. (inferred from ollama.com + hello@ollama.com contact; founders not publicly credited in README)
- **Primary site:** ollama.com
- **Pricing page:** ollama.com/pricing
- **Docs:** docs.ollama.com
- **Model registry:** ollama.com/library
- **Cloud filter:** ollama.com/search?c=cloud
- **Account auth:** via `ollama signin` CLI command

## 2. Ollama Cloud tier architecture

**Transparent local-cloud-split:**

Same CLI / REST API / SDK operate against **local models** (no `:cloud` suffix) OR **cloud models** (`:cloud` suffix in model name). Example:

```shell
ollama run gemma3              # local
ollama run kimi-k2.5:cloud     # cloud (routes through ollama.com backend)
```

Implementation: `server/cloud_proxy.go` (14.5 KB) + `server/routes_cloud_test.go` (33.0 KB).

**Authentication flow:**

```shell
ollama signin
# → routes to ollama.com account auth
# → provisions OLLAMA_API_KEY (env var)
# → subsequent :cloud model calls authenticated transparently
```

**Cloud model catalog (as of 2026-04-24):**

- `kimi-k2.5:cloud` (Moonshot; multimodal reasoning with subagents)
- `glm-5:cloud` + `glm-5.1:cloud` (Zhipu; reasoning + code)
- `qwen3.5:cloud` (Alibaba; reasoning + coding + vision)
- `minimax-m2.7:cloud` (MiniMax; fast coding)
- `glm-4.7-flash` (Zhipu flash variant)

Local models have same catalog reach — any open-weight GGUF model can run locally via `ollama pull`.

## 3. Pricing tiers (ollama.com/pricing)

| Tier | Price | Spec (verbatim from ollama.com) |
|------|-------|---------------------------------|
| Free with account | $0 | Basic cloud included free with Ollama accounts |
| **Pro** | **$20/month** or $200/year | "Run 3 cloud models at a time with 50x more cloud usage" |
| **Max** | **$100/month** | "Run 10 cloud models at a time with 5x more usage than Pro" |

Enterprise tier not explicitly documented on public pricing page.

## 4. Pattern #31 N=9 strengthening (Open-Core Commercial Entity)

**Timeline of Pattern #31 data points** (ordered by wiki number):

| # | Wiki | License | Commercial tier |
|---|------|---------|-----------------|
| 1 | v20 fish-speech | Custom non-OSI | Research-only OSS + commercial license gate |
| 2 | v24 Skyvern | AGPL-3.0 | Skyvern Cloud proprietary tier |
| 3 | v29 crawl4ai | Apache-2.0 | Cloud closed beta |
| 4 | v30 OpenHands | MIT core + separate-license enterprise directory | `enterprise/` directory separate license |
| 5 | v33 GitNexus | PolyForm Noncommercial | akonlabs.com SaaS |
| 6 | v41 browser-use | MIT | Browser-Use Cloud |
| 7 | v42 ruflo | MIT | Cognitum.One + Flow Nexus |
| 8 | v45 shannon | Shannon Lite AGPL-3.0 | Shannon Pro commercial tier |
| **9** | **v46 ollama** | **MIT** | **Ollama Cloud Pro $20/mo + Max $100/mo** NEW |

**9 distinct commercial-entity data points** across **6 different license strategies** (custom non-OSI / AGPL-3.0 / Apache-2.0 / MIT + enterprise directory / PolyForm Noncommercial / MIT / MIT multi-product / Shannon Lite AGPL / MIT with cloud upsell). Pattern #31 continues to demonstrate **commercial-gating is license-independent** (v42-deferred mini-audit lesson about #48 applies here too).

**Pro-docs-depth ordinal signal (v45 formalization 0-4):**

| Axis | Ollama v46 | Shannon v45 (benchmark 4/4) |
|------|-----------|------------------------------|
| Dedicated /pricing page | ✅ | ✅ |
| Dedicated /cloud docs | ✅ (cloud.mdx 232 lines) | ✅ (docs) |
| Account-signin CLI flow | ✅ | ✅ |
| Dedicated Pro-upsell file in repo (SHANNON-PRO.md-style) | ❌ | ✅ (26 KB most-detailed in corpus) |
| **Score** | **3/4** | 4/4 |

Depth = 3/4. Upsell happens through integration workflow (`ollama signin` prompted during `ollama launch claude --model kimi-k2.5:cloud`) rather than dedicated README marketing section.

## 5. Pattern #50 N=8 strengthening (Commercial-Funnel Companion Platform)

**7-surface commercial funnel:**

1. ollama.com landing (primary brand surface)
2. ollama.com/pricing (dedicated pricing page)
3. docs.ollama.com/cloud (cloud.mdx 232 lines)
4. ollama.com/library (model library; markets cloud models alongside local)
5. ollama.com/search?c=cloud (cloud-filter discovery surface)
6. `ollama signin` (CLI-native upsell gate)
7. Community (Discord + X + Reddit + blog)

**Pattern #50 data-point timeline:**

| # | Wiki | Funnel surfaces |
|---|------|------------------|
| 1 | v25 VoltAgent / awesome-design-md / getdesign.md | 5-surface design-template funnel |
| 2 | v31 Frank Fiegel / Glama / awesome-mcp-servers | 6-surface MCP-directory funnel |
| 3 | v40 claude-context (Zilliz) | First T4 cross-tier data point — UTM-tracked campaign ID |
| 4 | v41 browser-use | AGENTS.md-embedded-LLM-upsell-instructions (corpus-first) |
| 5 | v42 ruflo | 3-layer commercial corpus-most-elaborate |
| 6 | v43 rowboat | 7-surface YC-S24 funnel |
| 7 | v45 shannon | 7-surface Keygraph + Tower managed vCISO + Shannon Pro funnel |
| **8** | **v46 ollama** | **7-surface integration-driven funnel** NEW |

**Ollama's integration-driven-funnel sub-variant:**

Upsell pathway embedded inside agent-runtime-integration workflow:
- User installs Ollama + wants to use Claude Code with Kimi-K2.5
- Runs `ollama launch claude --model kimi-k2.5:cloud`
- CLI prompts `ollama signin` (account creation)
- Account provisioning → Pro-tier upsell for higher cloud usage
- `$20/mo` threshold triggered at 50× baseline usage

This is **corpus-first integration-driven-commercial-funnel sub-variant** distinct from:
- Dedicated-doc-driven (shannon v45 SHANNON-PRO.md)
- In-app upsell (rowboat v43)
- Ecosystem-portfolio multi-layer (ruflo v42)

## 6. 130+ community-integration directory (Pattern #17 variant 3 strengthening)

README lines 152-357 = **~60% of README line count** dedicated to community-integration directory.

**13 sub-category breakdown:**

| Category | Projects | Representative examples |
|---------|----------|------------------------|
| Chat Interfaces / Web | 16 | Open WebUI, Onyx, LibreChat, Lobe Chat, NextChat, Perplexica, big-AGI, Chatbox |
| Chat Interfaces / Desktop | 23 | Dify.AI, AnythingLLM, Cherry Studio, Alpaca, Enchanted, Msty, Witsy, BoltAI, IntelliBar |
| Chat Interfaces / Mobile | 7+ | SwiftChat, Enchanted, Maid, Ollama App, Reins, ConfiChat |
| Code Editors & Development | 16 | Cline, Continue, Void, twinny, gptel (Emacs), Ollama Copilot, Obsidian Local GPT, VT Code, QodeAssist, AI Toolkit for VS Code (Microsoft), Open Interpreter |
| Libraries & SDKs | ~30 | **LiteLLM, LangChain (Python+JS+4j+Go+Rust+Dart+.NET), LlamaIndex (Python+TS), Microsoft Semantic Kernel, Haystack, Firebase Genkit (Google), Mozilla any-llm, ruby_llm, OllamaSharp (.NET), Ollama-rs, Ollama4j, ollama-laravel, ollama-swift, chromem-go, Portkey, Testcontainers, LLPhant (PHP), PromptingTools.jl (Julia), rollama (R)** |
| Frameworks & Agents | 8 | AutoGPT, crewAI, AWS Strands Agents, Cheshire Cat, Mozilla any-agent, Stakpak, Hexabot, Cognizant Neuro SAN |
| RAG & Knowledge | 9 | RAGFlow, R2R, MaxKB, Minima, Chipper, ARGO, Archyve, Casibase, BrainSoup |
| Bots & Messaging | 5 | LangBot, AstrBot, Discord-Ollama, Ollama Telegram, LLM Telegram |
| Terminal & CLI | 11 | aichat, oterm, gollama, tlm, tenere, ParLlama, llm-ollama (Datasette), ShellOracle, LLM-X, cmdh, VT |
| Productivity & Apps | 16 | AppFlowy, Screenpipe, Vibe, Page Assist, NativeMind, Ollama Fortress (security proxy), 1Panel, Writeopia, QA-Pilot, Raycast, Painting Droid, Serene Pub, Mayan EDMS, TagSpaces |
| Observability & Monitoring | 6 | Opik (Comet), OpenLIT, Lunary, Langfuse, HoneyHive, MLflow Tracing |
| Database & Embeddings | 4 | pgai (Timescale), MindsDB, chromem-go, Kangaroo |
| Infrastructure & Deployment | 7 | Google Cloud, Fly.io, Koyeb, Harbor + 7 package managers |

**Total ≈ 130+ integration projects documented directly in README.**

**Pattern #17 variant 3 commercial-startup ecosystem-portfolio strengthening:**

Ollama, Inc. at center of 130+ community-integration ecosystem. Structurally similar to:
- VoltAgent v25 (awesome-design-md aggregator + voltagent framework + getdesign.md commercial)
- Rowboat Labs v43 (4-OSS-surface + YC-S24 + 7-surface funnel)
- Zilliz v40 (commercial-ecosystem-startup + 7-repo portfolio)
- ruflo v42 (solo-flagship-with-commercial + multi-package ecosystem)

**Distinguishing feature:** At infrastructure-runtime scale (170K stars) with first-party integrations from **Microsoft (Semantic Kernel + AI Toolkit for VS Code) + Google (Firebase Genkit + Google Cloud) + AWS (Strands Agents) + Mozilla (any-llm + any-agent) simultaneously**. 4 big-tech first-parties consume Ollama without Ollama reciprocally integrating them — distinguishes Ollama from Pattern #17 variant 2 big-tech-curator archetype (Microsoft v6+v28+v34 + Google v13+v44 = organizations curating frameworks, not being curated-by-external-frameworks).

Ollama's archetype: **runtime-being-consumed-by-big-tech-first-parties** = new structural sub-observation within Pattern #17 variant 3.

## 7. Pattern #57 Recursive Corpus Reference 3rd data point + compound sub-variant

**Timeline:**

| # | Wiki | Recursive reference type | Sub-variant |
|---|------|--------------------------|-------------|
| 1 | v27 oh-my-claudecode | OMC README cites v1 ECC + v2 Superpowers as inspirations | 2-wiki citation across separate sections |
| 2 | v30 OpenHands | Academic paper lineage chain cites UIUC/CMU prior papers | Academic-lineage-chain-implicit |
| **3** | **v46 ollama** | **Ollama Pi integration doc cites v36 pi-mono + v10 Karpathy autoresearch in single doc** | **Compound-2-wiki cross-corpus citation** NEW |

**Evidence in docs/integrations/pi.mdx:**

Lines 5-38 document Pi (pi-mono v36) as first-class integration:
> "Pi is a minimal and extensible coding agent. / Install Pi: npm install -g @mariozechner/pi-coding-agent / ollama launch pi"

Lines 65-80 cite Karpathy autoresearch (v10) verbatim:
> "[pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) brings autonomous experiment loops to Pi. **Inspired by Karpathy's autoresearch**, it turns any measurable metric into an optimization target..."

**Both citations appear in ONE doc (pi.mdx 110 lines).** Neither cited via explicit Storm-Bear-corpus knowledge — third-party-unaware validation that Storm Bear wiki-subject-selection captures meaningful ecosystem nodes.

**Structural observation:** Compound-cross-corpus citation is **qualitatively different** from v27 OMC citation (which cited ECC + Superpowers separately in different README sections). v46 ollama's Pi integration compresses 2 wiki references into single narrative — demonstrates Pi's lineage is genuinely entangled with both Karpathy (autoresearch methodology) + Mario Zechner (pi-mono runtime) in Ollama's maintainer-mental-model.

## 8. Governance surface

**3 governance files:**

- README.md 18.7 KB (40% user-facing / 60% community-integrations directory)
- CONTRIBUTING.md 3.6 KB — **explicit anti-feature-expansion discipline**
- SECURITY.md 1003 B — hello@ollama.com disclosure

**CONTRIBUTING notable claims (verbatim lines 22-25):**

> "**Issues that may not be accepted:**
> - Changes that break backwards compatibility in Ollama's API (including the OpenAI-compatible API)
> - Changes that add significant friction to the user experience
> - Changes that create a large future maintenance burden for maintainers and contributors"

Plus: "New features: new features (e.g. API fields, environment variables) add surface area to Ollama and make it harder to maintain in the long run as they cannot be removed without potentially breaking users in the future."

**Commit-message convention (lines 52-74):**
- `<package>: <short description>` format
- Lowercase "This changes Ollama to..." continuation
- Good: `llm/backend/mlx: support the llama architecture`
- Bad: `feat: add more emoji` (conventional-commits prefixes explicitly rejected)

**Absent governance:**
- No AGENTS.md (Pattern #22 absence at outside-scope runtime archetype)
- No CLAUDE.md
- No CODE_OF_CONDUCT.md
- No MAINTAINERS.md / GOVERNANCE.md (team opaque)
- No public roadmap / RFC process
- No CITATION.cff

**Pattern #12 Governance-Depth refined 3-factor formulation fit:**
- Maturity-ambition: HIGH (backwards-compat + anti-feature-expansion discipline)
- Maintainer-philosophy: commercial-runtime-infrastructure-stability + lean-governance
- Scale-tier: X-large (170K)

Medium-light governance at X-large scale with strong discipline-focus. Reinforces v42 refinement; adds **"commercial-runtime-infrastructure-stability"** as new Pattern #12 sub-observation (within refined-formulation framing).

## 9. Pattern delta from this entity

| Pattern | Delta |
|---------|-------|
| #17 variant 3 commercial-startup | 170K-scale strengthening + runtime-being-consumed-by-big-tech-first-parties sub-observation |
| #27 Community-Viral | 20+th observation; sustained-organic-infrastructure-growth at ~5,150 stars/mo |
| #29 License-Category-Diversity | MIT strengthening |
| #31 Open-Core Commercial Entity | **N=9 strengthening**; Pro-docs-depth 3/4; integration-driven-funnel |
| #50 Commercial-Funnel Companion | **N=8 strengthening**; integration-driven-funnel sub-variant (NEW) |
| #57 Recursive Corpus Reference | **3rd data point + compound-2-wiki cross-corpus citation sub-variant (NEW)** |
| #12 Governance-Depth (refined) | Commercial-runtime-infrastructure-stability sub-observation |

## 10. Storm Bear observational relevance

For Storm Bear operator:
- **Integration-driven-funnel** is effective commercial sub-variant Storm Bear could study if ever building commercial offering from Scrum-coach tooling (embed upsell in workflow, not README marketing).
- **Anti-feature-expansion governance** at 170K stars is powerful discipline model — every added CLI flag / API field is forever maintenance cost. Storm Bear vault CLAUDE.md refactor (v27 diagnostic HIGH bundle) could adopt similar discipline.
- **130+ community-ecosystem observation** demonstrates runtime-infrastructure advantage: building the foundational layer means others build downstream (Storm Bear is above-LLM-runtime layer; unlikely to reach similar ecosystem).

## 11. Cross-references

**Entities in this wiki:**
- `(C) Core product — ollama runtime + Modelfile.md`
- `(C) Outside-scope 9th sub-type + Pattern 47 retirement fires + Pattern 28 inversion.md`
- `(C) Storm Bear meta — 35th consecutive.md`

**Cluster summaries:**
- `(C) README + positioning cluster summary.md`
- `(C) Architecture + 38-subdir cluster summary.md`
- `(C) Commercial + ecosystem cluster summary.md` (source for this entity)

**Sibling wikis:**
- v45 shannon (Pattern #31 N=8 + Pattern #50 N=7 immediate predecessor; SHANNON-PRO.md Pro-docs-depth 4/4 benchmark)
- v43 rowboat (Pattern #50 7-surface YC-S24 predecessor)
- v42 ruflo (Pattern #31 N=7 + 3-layer commercial predecessor)
- v41 browser-use (Pattern #31 N=6 + Pattern #50 4-data-point precedent)
- v30 OpenHands (Pattern #31 N=4 + MIT+enterprise-directory precedent)
- v25 awesome-design-md / VoltAgent (Pattern #50 1st data point)
- v27 OMC + v30 OpenHands (Pattern #57 data points 1 + 2)
- v36 pi-mono (cited by Ollama Pi integration docs)
- v10 autoresearch-Karpathy (cited by Ollama Pi integration docs verbatim)
