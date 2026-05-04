# TrendRadar - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`sansan0/TrendRadar`](https://github.com/sansan0/TrendRadar) — **"⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts"**.

**52.1K stars (4th largest in corpus), 23.3K forks (highest forks-to-stars ratio 45%), GPL-3.0 (first GPL in corpus), v6.6.1, 228 commits master branch, 29 open issues, 8 PRs**. Python. **Author: sansan0 (solo maintainer, CN)** — **4th solo-at-enterprise-scale in corpus** (after agency-agents 82.9K, spec-kit 89.2K corporate, graphify 30K).

**Positioning:** *"告别无效刷屏，只看真正关心的新闻资讯"* — escape algorithmic control, consent-based information selection.

**Core product:** Multi-platform news aggregator + AI analysis + MCP server
- **11 CN news platforms** (Zhihu, Weibo, Baidu, Bilibili, Tencent, Phoenix, Toutiao, etc.)
- **AI analysis layer** via LiteLLM (DeepSeek, OpenAI, Gemini, Anthropic + 100+ providers)
- **9 push channels** (WeChat Work, Feishu, DingTalk, Telegram, Email, ntfy, Bark, Slack, generic webhook)
- **21+ MCP tools** + 4 MCP Resources (21+ categorized into Basic Queries / Intelligent Search / Advanced Analysis / RSS / System Management)
- **GitHub Actions scheduled** (default hourly cron)
- **Dual Docker images** (trendradar + trendradar-mcp)

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T4 Agent-as-bridge (primary) + T5 hybrid** — bridges 11 CN news platforms to agents via MCP; also standalone app |
| **Archetype** | Solo (sansan0) |
| **Scale tier** | X-Large (52.1K stars) |
| **Primary lang** | Python |
| **Packaging** | pip + Docker (two images) |
| **Origin story** | Community-viral / individual-solo (Pattern #19 no-lineage archetype) |
| **Methodology** | NONE (aggregation platform, not methodology framework) |
| **Governance files** | README + README-EN + README-MCP-FAQ + README-MCP-FAQ-EN (bilingual), LICENSE (TBD SECURITY/AGENTS) |
| **Agent/skill count** | 21+ MCP tools across 5 categories + 4 Resources |
| **i18n** | **Bilingual CN-primary + EN** (README-EN.md exists) — first corpus bilingual CN/EN at this scale |
| **Intellectual influence** | None cited |
| **Agent platforms** | MCP-compatible (Claude Desktop, Cursor, ChatGPT Desktop, Cherry Studio) |

**Tier placement rationale:** T4 bridge is primary because:
- MCP server (21+ tools) is the architectural interface for agent-consumer integration
- Bridges 11 external news platforms → agents (structurally parallel to gws v13 bridging Google Workspace services)
- Broad scope (11 platforms + RSS) without single-service narrowness (unlike notebooklm-py v7 single-service bridge)

Secondary T5 aspect: TrendRadar also runs standalone as scheduled autonomous trend-monitoring app. But MCP tooling is substantial enough to place T4 primary.

**Novel T4 quadrant:** TrendRadar occupies **solo-broad-external-platforms** — new to T4. Previous T4:
- T4a official-corporate-broad: gws v13 (Google Workspace 11+ services)
- T4b unofficial-solo-narrow: notebooklm-py v7 (NotebookLM single service)
- T4c unofficial-solo-broad-local: graphify v16 (local filesystem)
- **T4d (new v19): unofficial-solo-broad-external: TrendRadar v19 (11 CN news platforms)**

T4 extended to N=4 — Pattern #9 Resolution D further strengthened.

**Critical Pattern tests at v19:**

- **Pattern #18 (OpenClaw/Hermes) NEGATIVE EVIDENCE:** TrendRadar is solo-community-style (fits profile for OpenClaw/Hermes adoption per Pattern #18 community-platform-specific refinement) BUT does NOT mention OpenClaw/Hermes. Uses LiteLLM (100+ provider abstraction) + MCP directly. Possible refinements:
  - CN-ecosystem has different runtime standards
  - LiteLLM-agnostic design skips per-agent-runtime standards
  - Pattern #18 may be Western-community-platform-specific, not all community-platform
  - **Pattern #18 refinement candidate: regional-ecosystem-specific**

- **Pattern #19 (Intellectual lineage — 3 archetypes):** No Karpathy/Lam cited. 4th community-viral / no-lineage data point (after agency-agents v18). Strengthens 3-archetype model.

- **Pattern #20 (Solo-scale ceiling — revised):** 52.1K solo fits range 30K (graphify) → 82.9K (agency-agents). 4th solo-scale-ceiling data point. Formula validated.

- **Pattern #9 Resolution D (T4 multi-axial):** T4 at N=4 with new 4th quadrant (solo-broad-external-platforms). Resolution D strengthened further.

**NEW Pattern candidates at v19:**

- **#28 candidate: Multi-Provider AI Abstraction (LiteLLM pattern)** — TrendRadar first corpus framework using LiteLLM 100+ provider abstraction. Could predict future agent frameworks adopt provider-abstraction layers.
- **#29 candidate: GPL-3.0 in agent-space** — first GPL in corpus (prior: MIT / Apache-2.0 / ISC). Copyleft choice at 52K solo is distinctive.
- **#30 candidate: Regional-Ecosystem Runtime Standards** — hypothesis: agent runtime standards (like OpenClaw) may be regional/cultural, not universal. CN-ecosystem uses LiteLLM + MCP directly. Could refine Pattern #18 further.

**Novel elements at v19:**
1. **First GPL-3.0 in corpus** — copyleft at 52K scale
2. **First LiteLLM multi-provider abstraction** — 100+ providers via unified interface
3. **First 9-channel multi-push** — WeChat Work + Feishu + DingTalk are CN-first channels
4. **First CN news platform bridge** — 11 platforms, first CN-source-corpus T4 entrant
5. **First GitHub Actions scheduled execution** as primary deployment (cron-based)
6. **First 23.3K-fork ratio** (45% — highest in corpus; suggests high template-reuse)
7. **First 7-day check-in design** — activity-based resource fairness governance
8. **MCP 21+ tools across 4 Resources** — substantial MCP surface
9. **Jina AI Reader integration** — ecosystem cross-pollination signal
10. **Two Docker images** (trendradar + trendradar-mcp) — first separated-service Docker in corpus

**Phase 4b routing = T4 4-way extension comparison** (notebooklm-py v7 + gws v13 + graphify v16 + TrendRadar v19). Parallels T1 multi-way extension pattern (v11→v12→v17→v18). Documents Pattern #9 Resolution D strengthening + Pattern #18 potential regional refinement.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**19th auto-execution, first v2 routine execution, T4 extended to N=4**):

- **Ingest sources via WebFetch** — README.md + README-EN.md + README-MCP-FAQ.md + config files inferred from structure
- **Cross-reference với 18 sibling wikis** — especially T4 peers (notebooklm-py v7, gws v13, graphify v16) + solo-scale peers (agency-agents v18, graphify v16) + CN-language peers (deer-flow v9, multica v15)
- **Phase 4b = T4 4-way extension** — extends v16's 3-way; tests Pattern #9 Resolution D + Pattern #18 regional refinement + Pattern #20 ceiling validation
- **Beginner roadmap** — angle: VN users familiar with CN platforms (Zhihu, Bilibili, Weibo access common); Scrum coach use case: team trend-monitoring for specific industries/keywords

**Prime directive:** Outcome = wiki + T4 4-way comparison + document 4th T4 quadrant (solo-broad-external-platforms) + test Pattern #18 regional-ecosystem-specific hypothesis + register 3 new pattern candidates (#28-30).

## Process — routine `llm-wiki-routine-v2.md`

7 phases. First v2 routine execution. Phase 4b = **T4 4-way extension comparison**.

## Key People / Organization

- **sansan0** — solo creator/maintainer (CN individual)
- **wantcat (Docker Hub)** — possibly alias or associated account
- **Cherry Studio** — mentioned as integrated tool (CN AI app)
- **No VC/corp disclosed**
- **No intellectual lineage cited** (4th community-viral framework)
- **Cross-project:** 18 sibling wikis. This is 19th = T4 N=4 + Pattern #18 regional test.

## Folder Structure

```
TrendRadar - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00-07 folders
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 18 siblings MANDATORY** — especially T4 peers for 4-way
- **Pattern Library direct update** (v2 routine Phase 5)
- **Document Pattern #18 regional-ecosystem hypothesis** (negative evidence from CN-ecosystem framework)
- **Document 4th T4 quadrant** (solo-broad-external-platforms)

## Current Status

> **Last updated:** 2026-04-19
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 19th LLM Wiki, T4 extended to N=4

### Expected milestones

- [x] Phase 0 Pre-flight with v2 12-axis classification
- [ ] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 — README bilingual CN+EN / AI architecture + LiteLLM / MCP 21+ tools + Docker + deployment)
- [ ] Phase 3 Entity pages (4 — Core aggregation + AI layer / 21+ MCP Tools + Agent Ecosystem / Solo-at-52K CN + Pattern #19/#20/#18 evidence / T4 4-way + Pattern #9 Resolution D + Storm Bear meta)
- [ ] Phase 4a Beginner published guide bilingual
- [ ] Phase 4b **T4 4-way extension comparison** (notebooklm-py + gws + graphify + TrendRadar)
- [ ] Phase 5 Iteration log v19 + PATTERN_LIBRARY.md update
- [ ] Phase 6 Vault file updates
