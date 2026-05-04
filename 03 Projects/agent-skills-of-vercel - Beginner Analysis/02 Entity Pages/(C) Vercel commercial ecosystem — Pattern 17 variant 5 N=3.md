# (C) Entity Page — Vercel Commercial Ecosystem (Pattern #17 variant 5 N=3)

**Type:** Pattern + commercial ecosystem entity
**Source:** Vercel public information + repo positioning + claimable-deployment workflow analysis
**Cross-refs:** HuggingFace agents-course v26 (Pattern #17 variant 5 1st structural-N=2 anchor) / Microsoft markitdown v28 (Pattern #17 variant 5 2nd structural-N=2 anchor) / awesome-claude-skills v50 (composio-skills commercial-platform-bundled) / rowboat v43 (Pattern #50 6th data point Vercel AI SDK consumer; Vercel as upstream provider) / DeepTutor v38 (Pattern #28 native-SDK-routing observation) / pi-mono v36 (T1 multi-package monorepo)

---

## 1. Pattern #17 variant 5 ecosystem-scale commercial platform — N=3 default-criterion

**Variant 5 was promoted to confirmed at v29 audit** under structural-unambiguity-at-N=2 criterion (HuggingFace v26 + Microsoft v6+v28 = 2 structurally-criterial data points).

**Vercel v51 = 3rd structural data point**, reaching the **default ≥3-observations-across-2+-tiers criterion** (the original baseline criterion).

### Variant 5 criteria (formalized v29 audit)

A wiki subject qualifies as Pattern #17 variant 5 ecosystem-scale commercial platform if it meets all 5 criteria:

| # | Criterion | HuggingFace v26 | Microsoft v6+v28 | **Vercel v51** |
|---|---|---|---|---|
| 1 | **>$1B valuation** | ✅ ~$4.5B (2023) | ✅ ~$3T public market cap | ✅ **~$3.25B (2024 Series E)** |
| 2 | **Multiple products** | ✅ Hub + Transformers + Datasets + Spaces + smolagents + Inference + Learn + multiple courses + libraries (14+) | ✅ Microsoft 365 + Azure + GitHub + Copilot + AutoGen + AI Studio + many | ✅ **Next.js + Vercel Cloud + AI SDK + v0.dev + Vercel Toolbar + Edge Functions + Marketplace + Storage (8+)** |
| 3 | **OSS** | ✅ Hub OSS + Transformers Apache-2.0 + Datasets Apache-2.0 + many | ✅ AutoGen MIT + markitdown MIT + many | ✅ **Next.js MIT + AI SDK MIT + many; vercel-labs/agent-skills MIT-claim (this wiki)** |
| 4 | **Commercial tier** | ✅ HF Pro + HF Enterprise + Inference Endpoints + Spaces upgrades | ✅ Azure paid + Microsoft 365 + GitHub Copilot + AI Studio paid | ✅ **Vercel Pro + Vercel Enterprise + Vercel Hobby (free) → Pro paid; AI SDK is free; v0.dev paid above free tier** |
| 5 | **>10 years mature** | ✅ founded 2016 (~10 years) | ✅ founded 1975 (~50 years) | ✅ **founded 2015 (~10 years)** |

**Verdict:** Vercel v51 satisfies all 5 criteria. **N=3 default-criterion strengthening achieved.**

### Default-criterion vs structural-N=2

- **Default ≥3-cross-tier criterion:** Variant 5 was already confirmed under structural-N=2 criterion at v29 audit. Reaching N=3 default-criterion is **strengthening** (variant becomes "confirmed under both criteria" — analogous to Pattern #42 which reached dual-criterion-satisfaction at v45).
- **No new promotion needed** — variant 5 already CONFIRMED. Vercel v51 = strengthening data point.

### Cross-tier coverage at variant 5 (post-v51)

| Wiki | Tier | Org | Anchor product |
|---|---|---|---|
| Microsoft v6 | T3 (Education) | Microsoft | ai-agents-for-beginners |
| HuggingFace v26 | T3 (Education) | HuggingFace | agents-course |
| Microsoft v28 | T4 (Bridge) | Microsoft | markitdown |
| **Vercel v51** | **T1 (Assistant)** | **Vercel** | **agent-skills** |

**4 wikis × 3 tiers** post-v51. Variant 5 spans T1 + T3 + T4 — broadens default-cross-tier coverage from 2 tiers (post-v29) to 3 tiers (post-v51). Multi-tier coverage strengthens default-criterion satisfaction.

## 2. Vercel ecosystem inventory

| Product | Type | License | Maturity |
|---|---|---|---|
| **Next.js** | OSS framework | MIT | Founding flagship 2016 |
| **Vercel Cloud** | Commercial PaaS | Proprietary | Original product 2015 |
| **AI SDK** (`@vercel/ai`) | OSS SDK for LLM apps | Apache-2.0 | Active, multi-provider |
| **v0.dev** | AI generative UI | Commercial (free tier) | Released 2023 |
| **Vercel Toolbar** | OSS dev-tool | MIT | Vercel-distributed |
| **Vercel Marketplace** | Integration marketplace | Commercial | Native to Vercel Cloud |
| **Vercel Storage** | Database/blob/edge config | Commercial | Postgres + KV + Blob + Edge Config |
| **Edge Functions** | Compute primitive | Commercial | Vercel Cloud component |
| **vercel-labs/agent-skills** | OSS skill collection | MIT-claim | This wiki — 4.5 months old |

**Pattern #17 variant 5 anchor: 8+ products across OSS + commercial + multiple-domains** (frameworks + cloud + AI + UI generation + dev tools + databases). Strongest single-org-ecosystem evidence for variant 5 since Microsoft v28.

## 3. Commercial-funnel mapping (Pattern #50)

### vercel-deploy-claimable workflow → claim-URL-as-funnel-terminus

**Bipartite output (verbatim):**
```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...
```

**Funnel mechanics:**
1. Agent deploys to ephemeral Vercel-hosted preview (no user auth needed)
2. Returns preview URL (live site for user to inspect)
3. Returns claim URL (point of conversion to Vercel account ownership)
4. User visits claim URL → authenticates / signs up for Vercel account → deployment ownership transfers
5. **User now in Vercel commercial funnel** (Pro tier upsell, Enterprise pitch, Edge Functions usage charges, etc.)

**Pattern #50 50a sub-variant data point:** Most-explicit claim-URL-as-funnel-terminus observed in corpus. Joins:
- VoltAgent + getdesign.md v25 (commercial-funnel-via-companion-platform)
- ruflo v42 (Cognitum.One + Flow Nexus 7-surface funnel)
- rowboat v43 (Rowboat Labs YC-S24 7-surface funnel)
- ollama v46 (integration-driven-funnel via `ollama launch`)
- shannon v45 (Tower managed vCISO + SHANNON-PRO.md 26KB — most-detailed Pro-tier docs)
- aidevops v47 (commercial positioning at aidevops.sh)

**Distinction:** vercel-deploy-claimable is the most-explicit deployment-claim-mechanism observed. Other wikis have funnel companion platforms but none surface the claim mechanism as cleanly in agent-output.

## 4. AI SDK as upstream-provider observation

**rowboat v43** consumes Vercel AI SDK as a multi-provider abstraction layer (Pattern #28 11th data point at v43). Vercel as upstream-provider in the corpus: rowboat v43 + multiple other wikis use `@vercel/ai`.

**Vercel v51 wiki adds Vercel as direct-subject** (not just upstream-cited). Provides ecosystem framing context for prior Vercel AI SDK observations.

## 5. Pattern #57 57c forward-citation-then-wiki (corpus-first)

**multica v15** wiki entry in vault CLAUDE.md row 2969 (verified via grep):

> *"Tech stack — 8 corpus-firsts: Next.js 16 web + Electron desktop (first in corpus) + Go backend (Chi + sqlc + gorilla/websocket) + PostgreSQL 17 + pgvector (first vector-capable DB) + Turborepo (first monorepo orchestrator) + pnpm + skills-lock.json (first dependency-locked skill manifest) + Anthropic skills registry import (first) + **Vercel agent-skills import (first)** + hybrid local-daemon + cloud-orchestration..."*

multica v15 (built 2026-04-19) cited `vercel-labs/agent-skills` as a dependency import in its skills-lock.json — **36 wikis BEFORE v51 wiki of vercel-labs/agent-skills itself.**

**This is corpus-first forward-citation-then-wiki sub-variant of Pattern #57.**

### Pattern #57 sub-variant structure (post-v51 if registered)

| Sub-variant | Mechanism | Examples |
|---|---|---|
| **57a Direct citation** (CONFIRMED v50; N=4) | Subject A's repo cites subject B (current-or-past wiki subject) | bizos v37 cites multiple / aidevops v47 CREDITS.md cites VoltAgent v25 / shannon v45 cites pi-mono v36 / oh-my-claudecode v27 cites ECC v1 + Superpowers v2 |
| **57b Aggregator-mediated multi-citation** (CONFIRMED v50; N=1 stale-flagged) | Aggregator curates lists where subject B appears; awesome-list-genre form-factor | awesome-claude-skills v50 lists multiple corpus subjects |
| **57c NEW: Forward-citation-then-wiki** | Subject B cited in earlier wiki C; later wiki D builds B's wiki | **multica v15 cited "Vercel agent-skills" → v51 builds Vercel wiki (36-wiki gap)** |

**N=1 at v51, stale-flagged at registration. +5 v56 / +10 v61 review cadence.**

**Mechanistically distinct from 57a:** In 57a, the citation flows FROM the current wiki subject to a prior subject (intra-wiki authorial intent). In 57c, the citation flow is REVERSE: a prior wiki cited the current subject as a dependency, and the current wiki is built only later. The corpus-selection-discipline retroactively validates earlier wikis' choices.

**Mechanistically distinct from 57b:** 57b is aggregator-mediated; 57c is direct dependency-citation in a non-aggregator wiki (multica is T2 platform, not an aggregator).

**Significance:** External validity signal for Storm Bear corpus-selection discipline. multica v15 author selected vercel-labs/agent-skills as a notable dependency 36 wikis before vault routine v2.1 selected it as a wiki subject. Independent validation of selection criteria.

## 6. AGENTS.md identical-mirror as 4th template (vault refactor reference ensemble)

**Vault CLAUDE.md refactor (v27 diagnostic HIGH item #1)** has been deferred 30 sessions. Vercel v51 adds a 4th reference template:

| Template | Source | Sub-variant | Storm Bear relevance |
|---|---|---|---|
| **22a Monolithic single-source** | gh-aw v48 (49.8KB AGENTS.md) | Solo monolithic | Heavy-governance corporate-official template |
| **22c Authoritative-with-shim 3-layer** | aidevops v47 (Layer 0 shims + Layer 1 root + Layer 2 .agents/) | Hierarchical multi-file | Most-direct refactor template if vault scales to layered architecture |
| **22a Monolithic at scale** (also) | spec-kit v17 | Constitutional governance + 9-articles | Methodology + governance reference |
| **22d NEW Identical-mirror** | **Vercel v51** | Full content duplicated in BOTH AGENTS.md + CLAUDE.md | **Zero-divergence-risk template; storage cost 2× but no drift** |

**4-template ensemble for vault CLAUDE.md refactor decision:**
- If operator wants single source of truth → 22a monolithic (gh-aw v48 / spec-kit v17)
- If operator wants hierarchical scaling → 22c authoritative-with-shim (aidevops v47)
- If operator wants both files identical with zero drift → **22d identical-mirror (Vercel v51)**

**v51 contribution to v27 diagnostic HIGH item #1:** New template option added. Not a single-template recommendation; provides choice across architectures.

## 7. Pattern Library impact (this entity contributes)

| Pattern | Action |
|---|---|
| #17 variant 5 | N=3 default-criterion strengthening (HuggingFace + Microsoft + Vercel — 4 wikis × 3 tiers) |
| #50 50a claim-URL-as-funnel-terminus | Most-explicit observed corpus instance; observational |
| #57 57c forward-citation-then-wiki | NEW sub-variant N=1 stale-flagged at registration |
| #22 22d identical-mirror | NEW sub-variant N=1 stale-flagged at registration; 4th template added to vault refactor reference ensemble |
| #28 multi-provider via Vercel AI SDK | Strengthens prior-wiki Vercel-AI-SDK consumption observations (Vercel as upstream-provider; rowboat v43 + others) |

## 8. Strategic Storm Bear vault implications

**For v27 diagnostic HIGH bundle (deferred 30 sessions, BLOCKING-RECOMMENDATION 6× threshold):**

Item #1 (vault CLAUDE.md refactor) now has **4-template ensemble** to choose from. This reduces decision overhead — operator can pick template based on architectural preference rather than building from scratch.

**Concrete recommendation order (v51 update):**
1. **Choose template:** 22a monolithic / 22c authoritative-with-shim / 22d identical-mirror
2. **Reference SKILL.md format spec from Vercel** for vault `05 Skills/` expansion (YAML frontmatter convention)
3. **Adopt 500-line cap + on-demand loading semantics** for vault skills

**For v27 diagnostic HIGH item #2** (Storm Bear publishing strategy): Vercel commercial-funnel via claim-URL provides reference for "agent-deployed asset → ownership transfer" if vault ever publishes to public asset.

End of entity page.
