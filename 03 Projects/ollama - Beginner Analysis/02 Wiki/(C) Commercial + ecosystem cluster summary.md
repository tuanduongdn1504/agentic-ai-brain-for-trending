# (C) ollama — Commercial + ecosystem cluster summary

> **Source cluster 3 of 3.** Maps ollama.com commercial entity, Ollama Cloud Pro/Max pricing, 7-surface commercial-funnel, 130+ community-integration ecosystem, governance surface, and 3rd-party-unaware cross-corpus citation evidence.

---

## 1. Commercial entity: ollama.com

**Primary surface:** https://ollama.com
**Repo owner:** ollama (GitHub org) → likely Ollama, Inc. (commercial entity; founders not publicly cited in README or landing page)
**Security contact:** hello@ollama.com (SECURITY.md line 7)
**Community surfaces (README lines 46-50):**
- Discord: discord.gg/ollama
- X (Twitter): x.com/ollama
- Reddit: reddit.com/r/ollama

**Docker Hub:** hub.docker.com/r/ollama/ollama (official image)

## 2. Ollama Cloud + pricing tiers

**docs/cloud.mdx (4.4 KB) documents:**

> "Ollama's cloud models are a new kind of model in Ollama that can run without a powerful GPU. Instead, cloud models are automatically offloaded to Ollama's cloud service while offering the same capabilities as local models, making it possible to keep using your local tools while running larger models that wouldn't fit on a personal computer."

**Cloud models (as of v46 2026-04-24):**
- `kimi-k2.5:cloud`
- `glm-5:cloud`
- `glm-5.1:cloud`
- `qwen3.5:cloud`
- `minimax-m2.7:cloud`

**Pricing (ollama.com/pricing):**

| Tier | Price | Included |
|------|-------|----------|
| Free (with account) | $0 | Basic cloud models + local runtime |
| **Pro** | **$20/mo** (or $200/yr) | "Run 3 cloud models at a time with 50x more cloud usage" |
| **Max** | **$100/mo** | "Run 10 cloud models at a time with 5x more usage than Pro" |

**Account flow:**
```shell
ollama signin
```
→ Routes to ollama.com account auth → cloud API key provisioning → transparent routing via `:cloud` suffix in model names.

**Ollama Cloud architecture (inferred from `server/cloud_proxy.go` 14.5 KB + routes_cloud_test.go 33.0 KB):**
- Local Ollama daemon acts as transparent proxy
- `:cloud` suffix triggers forwarding to Ollama Cloud backend via `OLLAMA_API_KEY` env
- Same REST API / CLI / SDK works for local + cloud — **zero-code-change commercial upsell.**

**Pattern #31 Open-Core Commercial Entity N=9 strengthening (after v45 shannon N=8 baseline):**

9-entity data-point ledger (confirmed + strengthened patterns):
1. fish-speech v20 (custom non-OSI)
2. Skyvern v24 (AGPL-3.0 + commercial cloud)
3. OpenHands v30 (MIT + enterprise directory)
4. crawl4ai v29 (Apache-2.0 OSS + cloud coming)
5. GitNexus v33 (PolyForm Noncommercial)
6. browser-use v41 (MIT + Browser-Use Cloud)
7. ruflo v42 (MIT + Cognitum.One + Flow Nexus)
8. shannon v45 (Shannon Lite AGPL-3.0 + Shannon Pro commercial)
9. **ollama v46 (MIT + Ollama Cloud Pro $20/mo + Max $100/mo)** NEW

**Pro-docs-depth signal (v45 formalization 0-4 ordinal-scale):**

| Element | Present? | Score contribution |
|---------|---------|-------------------|
| Dedicated /pricing page | ✅ | 1 |
| Dedicated /cloud docs (cloud.mdx 232 lines) | ✅ | 1 |
| Account-signin + env-var flow | ✅ | 1 |
| Dedicated Pro-upsell file in repo (SHANNON-PRO.md-equivalent) | ❌ | 0 |

**Depth = 3/4.** Shannon v45 remains 4/4 reference (SHANNON-PRO.md 26 KB most-detailed Pro-tier doc in corpus). Ollama v46 at 3/4 because README does not embed explicit Pro-upsell language — Pro tier discovered via ollama.com/pricing + /cloud docs instead.

## 3. 7-surface commercial-funnel (Pattern #50 N=8 strengthening)

Ollama's commercial-funnel surfaces:

1. **ollama.com** landing page
2. **ollama.com/pricing** dedicated pricing
3. **docs.ollama.com/cloud** comprehensive cloud docs
4. **ollama.com/library** model library (marketing for cloud models via `:cloud` suffix)
5. **ollama.com/search?c=cloud** filtered search for cloud models
6. **`ollama signin`** CLI-native upsell path
7. **Discord + X + Reddit + blog** community surfaces

**Pattern #50 N=8 strengthening.** Joins v42 ruflo (corpus-most-elaborate 7-layer + 3-layer commercial) / v43 rowboat (7-surface YC-funnel) / v45 shannon (7-surface Keygraph/Tower funnel). **Ollama's integration-driven commercial funnel sub-variant:** upsell path is embedded inside agent-runtime integrations (e.g., `ollama launch claude --model kimi-k2.5:cloud` auto-prompts `ollama signin` → account creation → $20/mo upsell cascade). Distinct from in-app upsell (Rowboat v43) or dedicated-doc upsell (shannon v45).

## 4. 130+ community-integration ecosystem (Pattern #17 variant 3 strengthening)

README lines 152-357 = **~60% of README line count** = community-integration directory:

**13 sub-category directories:**

| Category | Count |
|---------|-------|
| Chat Interfaces / Web | 16 |
| Chat Interfaces / Desktop | 23 |
| Chat Interfaces / Mobile | 7+ |
| Code Editors & Development | 16 |
| Libraries & SDKs | ~30 |
| Frameworks & Agents | 8 |
| RAG & Knowledge Bases | 9 |
| Bots & Messaging | 5 |
| Terminal & CLI | 11 |
| Productivity & Apps | 16 |
| Observability & Monitoring | 6 |
| Database & Embeddings | 4 |
| Infrastructure & Deployment | 7 |

**Total ≈ 130+ integration projects.** One of the deepest directly-maintained community-integration directories at 170K-scale.

**Ecosystem maturity signal:**
- **LiteLLM** (unified 100+ LLM provider abstraction; also in ruflo v42) treats Ollama as first-class provider
- **LangChain** + LangChainJS + LangChainGo + LangChain4j + LangChainRust + LangChainDart + LangChain for .NET = 7 LangChain family integrations. Deepest corpus LangChain family coverage.
- **LlamaIndex** + LlamaIndexTS = 2 LlamaIndex integrations
- **Microsoft Semantic Kernel** — first-party Microsoft integration (no Microsoft involvement observed in Ollama itself; Microsoft plugs Ollama into Semantic Kernel Ollama connector)
- **Firebase Genkit** — Google-first-party integration (Google plugs Ollama into Genkit; no Google involvement in Ollama)
- **Mozilla any-llm + any-agent** — Mozilla first-party abstractions treating Ollama as provider
- **AWS Strands Agents** — AWS first-party agent framework with Ollama support
- **Portkey** — AI gateway treating Ollama as provider
- **AutoGPT + crewAI** — agentic frameworks with Ollama support

**Pattern #17 Ecosystem-Layer variant 3 commercial-startup ecosystem-portfolio strengthening** — Ollama, Inc. at center of 130+ community-integration ecosystem. Structurally similar to VoltAgent v25 (awesome-design-md aggregator + voltagent framework + getdesign.md commercial) and Rowboat Labs v43 (4-OSS-surface + YC-S24 + 7-surface funnel) but **at infrastructure-runtime scale rather than framework scale** — Ollama provides the runtime, integrations provide higher-layer consumers.

## 5. Cross-corpus citations (Pattern #57 Recursive Corpus Reference 3rd data point)

**Evidence in docs/integrations/pi.mdx (lines 65-80):**

> "### Autoresearch with `pi-autoresearch`
>
> [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) brings autonomous experiment loops to Pi. **Inspired by Karpathy's autoresearch**, it turns any measurable metric into an optimization target: test speed, bundle size, build time, model training loss, Lighthouse scores."

Also lines 5-38 document Pi (pi-mono v36) as first-class integration:
> "Pi is a minimal and extensible coding agent."
> + `npm install -g @mariozechner/pi-coding-agent`
> + `ollama launch pi`

**Both v10 Karpathy autoresearch + v36 pi-mono Mario Zechner are named in single Ollama integration doc by third-party unaware of Storm Bear corpus.** This is the 3rd Pattern #57 data point:

**Pattern #57 timeline:**
1. **v27 oh-my-claudecode** — OMC README cites **v1 ECC + v2 Superpowers** as inspirations (first recursive-corpus-reference in corpus)
2. **v30 OpenHands** — academic paper lineage chain cites UIUC/CMU papers (implicit lineage citation)
3. **v46 ollama** — Pi integration doc cites **Pi (v36) + pi-autoresearch-Karpathy (v10)** (compound-2-wiki cross-corpus citation in single doc)

**Sub-variant at v46 — compound-cross-corpus citation (NEW):** single doc cites 2 prior corpus wikis (not just 1). Structurally distinct from OMC v27 (also 2 citations but across separate pinned repos).

This is **third-party-unaware validation** that Storm Bear wiki-subject-selection is capturing the most-influential nodes in the agent-runtime ecosystem — Ollama engineers writing integration docs independently cite Karpathy autoresearch (v10) and Pi pi-mono (v36) as the most-meaningful prior artifacts in Pi's lineage.

## 6. Governance surface

**3 governance files (analyzed in cluster 2):**

- `README.md` 18.7 KB — 40% user-facing + 60% community-integrations directory
- `CONTRIBUTING.md` 3.6 KB — explicit backwards-compat + anti-feature-expansion + package-prefixed commit + tests-required discipline
- `SECURITY.md` 1003 B — responsible disclosure to hello@ollama.com

**Notable absences:**
- **No AGENTS.md** — consistent outside-scope runtime archetype (Pattern #22 absence)
- **No CLAUDE.md** — absent despite Claude Code being first-class integration via `ollama launch claude`
- **No CODE_OF_CONDUCT.md**
- **No MAINTAINERS.md / GOVERNANCE.md** — team opaque
- **No public roadmap / RFC / discussion process documented**
- **No CITATION.cff** (contrast magika v44 corpus-first CITATION.cff)

**Governance-depth at 170K stars:** Medium-light + high-discipline — distinct from LlamaFactory v22 academic-lab (medium-heavy with CITATION.cff + academic-lineage). Correlates with commercial-runtime-infrastructure-stability archetype (stable API is product; governance overhead would slow core discipline).

**Pattern #12 refined 3-factor formulation fit:**
- Maturity-ambition: HIGH (backwards-compat discipline + anti-feature-expansion)
- Maintainer-philosophy: commercial-runtime-infrastructure-stability + lean-governance
- Scale-tier: X-large (170K)

Reinforces v42 refinement (not "solo vs corporate predicts governance-depth" but "maturity-ambition + maintainer-philosophy + scale-tier" predicts it).

## 7. Pattern #18 MCP observation (light-consumer)

Ollama does **not** ship explicit MCP server or MCP client integration in README. `docs/integrations/` catalogs 20 runtime integrations but none are MCP-specific.

**Tier classification per v42 Pattern #18 3-tier tool-count formulation:**
- Tier 1 basic 1-5 tools: N/A (runtime doesn't expose MCP tools)
- Tier 2 MCP-heavy 6-99 tools: N/A
- Tier 3 MCP-platform-scale 100+ tools: N/A

**Ollama is a Pattern #18 Layer 0 provider** (runtime-bundled-launcher) not a Layer 1 MCP consumer. Ollama does not consume MCP directly; integration with MCP-capable agent runtimes (Claude Code / OpenClaw / Hermes / Pi) happens through **API-compatibility layer** (OpenAI-compat + Anthropic-compat) not MCP protocol.

**Observation for next audit:** Pattern #18 may extend to 4-layer taxonomy:
- **Layer 0 NEW — runtime-bundled-launcher** (ollama v46; first observation)
- Layer 1 MCP universal
- Layer 2 community-platform-scoped
- Layer 3 per-runtime

Pattern #18 formulation-extension candidate at next mini-audit if Layer 0 observation validates at N=2 (e.g., if future wiki subject in outside-scope runtime archetype also ships bundled launchers).

## 8. Pattern #27 Community-Viral Scale Path data point

**Ollama scale math:**
- 170,000 stars
- Project launched ~July 2023
- Current date 2026-04-24 → ~2.75 years age
- Average: ~5,150 stars/month sustained

**Not extreme-viral** (Pattern #52 criteria: ≥1K stars/day at sustained pace). Ollama did not ship at that velocity.

**Sub-path classification:** **Sustained-organic-infrastructure-growth** — similar to shannon v45 steady organic-commercial growth (2.5K stars/mo) and OpenHands v30 corporate-academic-amplified (~2,867/mo) but at higher absolute scale due to infrastructure-runtime being universally-needed (anyone running open-weight LLMs locally → potential Ollama user).

**Data point strengthening within-#27:** Ollama is 20+th observation. Sub-path documented.

## 9. Ecosystem signals + Storm Bear peer archetypes

**Commercial peers in corpus at infrastructure-scale:**

| Peer wiki | Scale | Commercial tier |
|-----------|-------|-----------------|
| Ollama v46 | 170K | Cloud Pro $20 + Max $100 |
| OpenHands v30 | 72K | Enterprise directory (MIT core + separate-license enterprise) |
| browser-use v41 | 89K | Browser-Use Cloud |
| crawl4ai v29 | 64K | Cloud closed beta |
| ruflo v42 | 33K | Cognitum.One + Flow Nexus |
| markitdown v28 | 114K | No explicit commercial tier (Microsoft strategic OSS) |
| shannon v45 | 40K | Shannon Pro |

**Ollama is largest commercial-runtime-infrastructure archetype in corpus** (beats browser-use, OpenHands, markitdown).

**Commercial-funnel discipline evolution (Pattern #50 N=8 observation timeline):**

1. **Dedicated-doc-driven** (shannon v45 SHANNON-PRO.md 26 KB; Pro-docs-depth 4/4)
2. **In-app upsell** (rowboat v43 YC-startup; Pro-docs-depth N/A until commercial launch)
3. **Integration-driven** (ollama v46; Pro-docs-depth 3/4 — Pro tier discovered through integration workflow, not README marketing)
4. **Ecosystem-portfolio multi-layer** (ruflo v42; 3-layer commercial structure)

Ollama's integration-driven-commercial-funnel is corpus-first sub-variant.

## 10. Pattern delta summary from this cluster

| Pattern | Delta |
|---------|-------|
| #17 variant 3 commercial-startup | 170K-scale ecosystem-portfolio strengthening (130+ community integrations) |
| #27 Community-Viral Scale Path | 20+th observation; sustained-organic-infrastructure-growth sub-path |
| #31 Open-Core Commercial Entity | **N=9 strengthening**; Pro-docs-depth 3/4; transparent local-cloud-proxy sub-variant |
| #50 Commercial-Funnel Companion Platform | **N=8 strengthening**; integration-driven-funnel sub-variant (NEW) |
| #52 Extreme-Viral-Velocity (stale) | Not un-staled (sustained-organic, not extreme) |
| #57 Recursive Corpus Reference | **3rd data point**; compound-2-wiki cross-corpus citation sub-variant (NEW) |
| #18 Layer 0 | Runtime-bundled-launcher observation; potential 4-layer taxonomy extension candidate |

## 11. Corpus-firsts enumerated from this cluster

1. **170K-star non-aggregator OSS project** (corpus largest)
2. **Ollama Cloud Pro $20 + Max $100 integration-driven-funnel** (Pro-docs-depth 3/4 sub-variant)
3. **Transparent local-cloud-proxy architecture** with `:cloud` suffix (zero-code-change upsell)
4. **130+ community-integration directory** (60% of README line count; 13 sub-categories)
5. **Compound-2-wiki cross-corpus citation** (Pi integration doc cites pi-mono v36 + Karpathy autoresearch v10 simultaneously)
6. **Pattern #18 Layer 0 runtime-bundled-launcher** — infrastructure-scale implementation of `ollama launch <runtime>` for 10+ agent runtimes
7. **Anti-feature-expansion CONTRIBUTING discipline at 170K stars** — commercial-runtime-infrastructure-stability governance
8. **First-party ecosystem integrations from Microsoft + Google + AWS + Mozilla simultaneously** (Semantic Kernel + Firebase Genkit + Strands Agents + any-llm) — 4 big-tech first-parties integrate Ollama; Ollama does not reciprocally integrate their runtimes (distinguishes ollama from Pattern #17 variant 2 big-tech-curator archetype)
9. **Third-party-unaware validation of corpus-selection** (Ollama Pi integration doc independently cites 2 Storm Bear wiki subjects)
10. **Commercial-runtime-infrastructure-stability archetype** as new Pattern #12 refined sub-observation
