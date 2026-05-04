# deer-flow - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow) — **"SuperAgent harness"** (62K stars, ByteDance, v2.0) cho long-horizon autonomous tasks (minutes to hours). Architecture: Sandbox + Memory + Skills + Sub-agents + Message Gateway. Self-hosted Python + Next.js app với LangGraph orchestration. **Proposes new Tier 5 "Agent-as-application"** — extends 4-tier taxonomy vì deer-flow không fit T1-T4. First standalone autonomous agent harness in Storm Bear corpus.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** v1 (9th auto-execution — **third different-domain**, Tier 5 proposal):

- **Ingest sources via WebFetch** — README (38 KB), Install.md, CONTRIBUTING.md
- **Cross-reference với 8 sibling wikis** — 4 T1 + 1 T2 + 1 T3 + 1 T4 + 1 outside-scope
- **Phase 4b = Tier 5 proposal** — extends v7 4-tier → v9 5-tier với "Agent-as-application"
- **Beginner roadmap** — different angle: "when to run standalone agent vs plug into Claude Code"

**Prime directive:** Outcome = wiki + 5-tier taxonomy proposal + beginner guide positioning standalone autonomous agent apps in Storm Bear ecosystem. Nudge nếu drift.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **Tier 5 "Agent-as-application" proposal** (new tier, extends taxonomy, 8th distinct Phase 4b routing mode).

## Key People

- **ByteDance** — original author (TikTok parent company, strong OSS record)
- **DeerFlow team** — active development (pushed today 2026-04-18)
- **Cross-project:** 8 sibling wikis shipped. This is 9th = 3rd different-domain.
- **Storm Bear** — curator, operator

## Folder Structure

```
deer-flow - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← WebFetch-based (32 MB repo manageable but WebFetch faster for docs)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 8 siblings MANDATORY** — especially T1 tools (plug-in complement) + T2 goclaw (platform comparison)
- **Note: NO Vietnamese README** despite 5-language support (fr/ja/ru/zh/en) — contribution opportunity
- **Note: Agent autonomy comparable to Devin/AutoGPT/OpenHands class** — not Claude Code class

## Positioning note

**deer-flow slot trong proposed v9 5-tier taxonomy:**

| Tier | Frameworks (n=9 now) | Purpose | Verb |
|------|---------------------|---------|------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD (4) | Use in Claude Code | Use |
| T2: Agent-as-service | goclaw (1) | Deploy multi-tenant | Deploy |
| T3: Agent-as-education | course (1) | Learn concepts | Learn |
| T4: Agent-as-bridge | notebooklm-py (1) | Integrate external | Integrate |
| **T5: Agent-as-application** (NEW v9) | **deer-flow (1)** | **Run standalone autonomous** | **Run** |
| Outside scope | build-your-own-x (1) | General programming | — |

→ **First T5 entrant.** Standalone autonomous agent harness = distinct from other tiers.

**Comparison to similar class:**
- **Devin** (Cognition AI) — closed-source; deer-flow = open OSS alternative
- **AutoGPT** — older era; deer-flow = newer architecture with LangGraph
- **OpenHands** — parallel OSS; deer-flow = different lineage (ByteDance)
- **CrewAI** — multi-agent framework; deer-flow = application layer atop orchestrator

## Unique positioning claims của deer-flow (từ Phase 0 probe + README)

- **"SuperAgent harness"** — self-framing (unique vs siblings)
- **Long-horizon** — tasks "minutes to hours" (vs Claude Code's interactive short tasks)
- **Full-stack app** — Frontend (Next.js) + Backend (Python) + Nginx reverse proxy
- **LangGraph orchestration** — graph-based agent flow (popular agent framework)
- **Progressive skill loading** — skills load when needed (context-conservation)
- **Multi-channel integration** — Telegram, Slack, Feishu, WeChat, WeCom (real IM usage)
- **Complementary vs Claude Code** — explicit positioning: can invoke each other via OAuth/skill
- **Self-hosted** — local trusted-network deployment recommended
- **62K stars** — 2nd largest in corpus (behind build-your-own-x 491K meta-reference)
- **ByteDance backing** — large company sustainability
- **#1 GitHub Trending after v2.0** — February 2026 launch milestone
- **Rebuilt from scratch v2** — no shared code with v1

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 9th LLM Wiki, 9th routine run, third different-domain với Tier 5 proposal

### Expected milestones

- [x] Phase 0 Pre-flight (API probe PASSED, 32MB moderate, Tier 5 "Agent-as-application" proposal)
- [x] Phase 1 Setup — in progress
- [ ] Phase 2 Source ingestion — 3 summaries (README + Install + Contributing/architecture)
- [ ] Phase 3 Entity pages (4 — Harness Architecture, Skill System, Sub-Agent System, Message Gateway)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **Tier 5 proposal — 5-tier taxonomy extension**
- [ ] Phase 5 Iteration log v9
- [ ] Phase 6 Vault file updates
