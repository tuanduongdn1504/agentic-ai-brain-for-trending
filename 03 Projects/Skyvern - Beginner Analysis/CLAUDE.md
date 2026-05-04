# Skyvern - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`Skyvern-AI/skyvern`](https://github.com/Skyvern-AI/skyvern) — **"Automate browser based workflows with AI"**.

**21,281 stars (#11 in corpus), 1,944 forks (9.1%), AGPL-3.0 (2nd AGPL in corpus after Unsloth Studio v23), Python, main-branch, 149 open issues, created 2024-02-28, pushed 2026-04-20**. Organization: **Skyvern-AI** (commercial company, Skyvern Cloud managed product at skyvern.com). Authors: unnamed in README; contact `founders@skyvern.com` (plural — suggests duo or small team).

**Scope status: T5 Agent-as-application (4TH T5 entrant) — browser-automation specialization.**

**Positioning:** *"Automate Browser-based workflows using LLMs and Computer Vision."* Skyvern extends Playwright with vision + LLM to do browser tasks without brittle XPath selectors.

**Core product:**
- **4 AI page commands** — act / extract / validate / prompt
- **Workflow builder** — loops, data extraction, validation, HTTP, file parsing, email
- **2FA support** — TOTP / email / SMS; Bitwarden password manager integration
- **Livestreaming + form filling + file download** — browser automation primitives
- **Multi-LLM support** — OpenAI + Anthropic + Bedrock + Gemini + 10+ providers
- **Tech stack:** Python 3.11+ / Node.js / Playwright / Docker / Docker Compose
- **Benchmarks:** 85.8% WebVoyager + 64.4% WebBench ("best-in-class on WRITE tasks")
- **Cloud + self-hosted:** OSS local via pip/Docker + Skyvern Cloud managed (anti-bot measures proprietary)

**Intellectual lineage:** *"Inspired by Task-Driven autonomous agent design from BabyAGI and AutoGPT."* → Pattern #19 community-viral archetype data point.

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application (4th entrant)** |
| **Archetype** | **Commercial-entity + team** (Skyvern-AI LLC/Inc, Skyvern Cloud) — matches existing commercial archetype |
| **Scale tier** | Medium-large (21.3K stars — #11 in corpus) |
| **Primary lang** | Python + Node.js |
| **Packaging** | pip + Docker Compose + Cloud (managed) |
| **Origin story** | Founded 2024-02, commercial from day 1 (Skyvern Cloud managed product) |
| **Methodology** | Task-driven autonomous agent (BabyAGI / AutoGPT lineage) + vision-based DOM-free browser |
| **Governance files** | README + LICENSE (AGPL-3.0) + Docker Compose |
| **Agent/skill count** | 4 AI page commands + workflow builder blocks |
| **i18n** | English-only |
| **Intellectual influence** | **BabyAGI + AutoGPT (community-viral lineage)** + Playwright framework |
| **Agent platforms** | Self-hosted OSS + Skyvern Cloud (proprietary) |

**Tier placement rationale:** T5 Agent-as-application — produces autonomous browser-workflow execution (not training, not orchestrating other agents). Specializes at browser-automation domain.

**Pattern validation analysis at v24:**

### Patterns that test at v24

- **#31 Open-Core Commercial Entity (candidate N=1 at v20)** — Skyvern is **2nd observation** (fish-speech v20 + Skyvern v24). Both have OSS core + proprietary commercial tier. **COULD PROMOTE to CONFIRMED at N=2** (structurally unambiguous across 2 sub-types: foundation-model + T5-browser-agent).
- **#45 Dual-Licensing Strategy (candidate N=1 at v23)** — Skyvern is NOT dual-license (single AGPL-3.0 for OSS repo; proprietary cloud is separate, not dual-licensed component). **STAYS candidate N=1.** Distinction from Pattern #31 clarified.
- **#29 License-Category Diversity (confirmed v21)** — +1 data point (Skyvern AGPL-3.0, 2nd AGPL in corpus). Non-permissive now N=5 (2 GPL + 2 AGPL + 1 custom).
- **#8 Research-Benchmark** — WebBench 64.4% + WebVoyager 85.8% = empirical evaluation data point (7th in corpus).
- **#19 Intellectual Lineage — community-viral archetype** — Skyvern cites BabyAGI + AutoGPT (both community-viral OSS agents). Strengthens community-viral archetype (prior: agency-agents v18 Reddit-viral + TrendRadar v19 no-lineage).

### T5 tier extension

- v9 deer-flow (research agent, corporate ByteDance)
- v10 autoresearch (ML research, Karpathy solo)
- v14 paperclip (orchestration, community-platform)
- **v24 Skyvern (browser automation, commercial-entity)** ← NEW

**T5 at N=4 after v24.** Archetype diversity: corporate + solo + community-platform + **commercial-entity**. 4 distinct archetypes at T5.

### NEW Pattern candidates at v24 (speculative)

- **#47 candidate: Vision-DOM-Free Browser Automation** — novel approach (vision + LLM vs XPath/selector-based). Distinct from Puppeteer/Playwright-only or Selenium. Sub-pattern within T5 application-specific-methodology.
- **#48 candidate: Proprietary-Anti-Bot Commercial Moat** — OSS core + proprietary anti-bot as commercial differentiator. Could overlap with Pattern #31 (open-core); may be sub-type.

### Novel elements at v24

1. **2nd AGPL-3.0** in corpus
2. **Browser-automation T5 specialization** — first in corpus (deer-flow=research, autoresearch=ML, paperclip=orchestration)
3. **WebBench + WebVoyager benchmarks** — first browser-automation benchmarks in corpus
4. **Vision + LLM DOM-free approach** — novel methodology
5. **Proprietary anti-bot as commercial moat** — first in corpus
6. **Commercial-from-day-1 entity** — Skyvern-AI founded with Skyvern Cloud product
7. **Plural "founders@skyvern.com"** — suggests duo or small team (test Pattern #46 potentially)
8. **Task-Driven autonomous agent** — BabyAGI/AutoGPT lineage = community-viral Pattern #19 data point
9. **4 AI page commands** (act/extract/validate/prompt) — novel abstraction
10. **10+ LLM provider support** — Pattern #28 (LiteLLM) data point check

**Phase 4b routing = T5 tier extension deliverable** — 4-way comparison of T5 entrants (deer-flow + autoresearch + paperclip + Skyvern). Documents T5 archetype diversity maturing + Pattern #31 promotion.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**24th auto-execution, 6th v2 routine execution**):

- **Ingest sources via WebFetch** — README + docs.skyvern.com
- **Cross-reference với 23 sibling wikis** — primarily T5 peers (deer-flow v9 + autoresearch v10 + paperclip v14) + open-core peer (fish-speech v20) + AGPL peer (Unsloth v23)
- **Phase 4b = T5 tier extension 4-way comparison**
- **Beginner roadmap angle** — developers wanting to automate browser tasks (Storm Bear operator: Jira/Linear/retrospective data collection possible use)

**Prime directive:** Outcome = wiki + Pattern #31 PROMOTION to N=2 + #29 strengthening + T5 archetype diversity documentation + clarify #45 vs #31 distinction.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 6th v2 routine execution. Phase 4b = T5 4-way comparison deliverable.

## Key People / Organization

- **Skyvern-AI** — commercial organization (LLC/Inc unclear)
- **"founders@skyvern.com"** — plural (duo or small team)
- **Skyvern Cloud** — managed commercial product at skyvern.com
- **Community:** Discord + Twitter @skyvernai + LinkedIn + GitHub issues
- **Cross-project:** 23 sibling wikis. This is 24th = T5 tier extension + Pattern #31 promotion.

## Folder Structure

```
Skyvern - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── 00-04 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 23 siblings MANDATORY** — especially T5 peers (v9, v10, v14) + open-core peer (v20) + AGPL peer (v23)
- **Pattern Library direct update** (v2 routine Phase 5) — promote #31 + strengthen #29 + #19 + #8 + clarify #45 scope

## Current Status

> **Last updated:** 2026-04-20
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 24th LLM Wiki, 6th v2 execution, T5 4th entrant, Pattern #31 promotion candidate

### Expected milestones

- [x] Phase 0 Pre-flight with v2 12-axis classification
- [ ] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 clusters)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **T5 4-way comparison deliverable**
- [ ] Phase 5 Iteration log v24 + PATTERN_LIBRARY.md update
- [ ] Phase 6 Vault file updates
