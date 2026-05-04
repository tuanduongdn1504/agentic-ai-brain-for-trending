# ai-agents-for-beginners - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`cvtot/ai-agents-for-beginners`](https://github.com/cvtot/ai-agents-for-beginners) (fork của `microsoft/ai-agents-for-beginners`) — **10-lesson course** (+ 4 Coming Soon) dạy AI Agents fundamentals, design patterns, Microsoft ecosystem (Azure AI Foundry, Semantic Kernel, AutoGen, MAF). **New Tier 3** (Agent-as-education) — khác Tier 1 (dev-tool) và Tier 2 (platform) từ v4 taxonomy. Mục tiêu: knowledge base + **Tier 3 addition to taxonomy** + beginner guide map education-content vs tool-content.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** v1 (6th auto-execution — first **different-domain** project, testing routine's outer generalization beyond agent-framework tooling):

- **Ingest sources** — Main README + 7 lesson READMEs (Intro, Agentic Frameworks, Design Patterns, Agentic RAG, Multi-Agent, Agentic Protocols, Context Engineering, MAF)
- **Cross-reference với 5 sibling wikis** — 4 Tier 1 (ECC/Superpowers/gstack/GSD) + 1 Tier 2 (goclaw)
- **Phase 4b = Tier 3 taxonomy expansion** — extend v4 2-tier model → 3-tier model (education tier added)
- **Beginner roadmap** — different style: this IS a roadmap (vs siblings teach tools). Cross-reference: course = source material cho siblings

**Prime directive:** Outcome = wiki + 3-tier taxonomy upgrade + beginner guide clarifying "learn concepts (ai-agents-for-beginners) vs learn tooling (siblings)". Nudge nếu drift.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **Tier 3 taxonomy expansion** (different-domain routing — first "outside-dev-tooling-domain" project).

## Key People

- **Storm Bear** — owner, curator
- **Team** — audience
- **Cross-project:** 5 sibling wikis đã ship. This is 6th. First **different-domain** sibling.
- **Original author:** Microsoft (course team); repo = cvtot fork

## Folder Structure

```
ai-agents-for-beginners - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← WebFetch-based (clone blocked; content via raw.githubusercontent.com)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 5 siblings MANDATORY** — especially vì đây là different-domain pivot
- **Note: Source acquisition via WebFetch** (clone blocked; fetch lesson READMEs individually)
- **Note: Vietnamese translation exists** (via README translations folder — 50+ languages claim)

## Positioning note

**ai-agents-for-beginners slot trong v4+v6 taxonomy:**

| Tier | Frameworks | Purpose |
|------|-----------|---------|
| **Tier 1: Agent-as-assistant** | ECC, Superpowers, gstack, GSD | Dev tool use daily |
| **Tier 2: Agent-as-service** | goclaw | Platform deploy |
| **Tier 3: Agent-as-education** (**NEW v6**) | ai-agents-for-beginners | Learn concepts first |

→ **First Tier 3 entrant.** Distinct purpose: teach fundamentals before tool adoption. Complementary, not competitive với Tier 1/2.

## Unique positioning claims của ai-agents-for-beginners (từ Phase 0 survey)

- **"AI Agents for Beginners"** — explicitly educational framing (unique vs siblings)
- **10 core lessons + 4 Coming Soon** — structured curriculum (weeks, not reference docs)
- **Microsoft-authored** (well-resourced, production-grade sample code)
- **Azure ecosystem focus** — Azure AI Foundry, Semantic Kernel, AutoGen, MAF
- **GitHub Models integration** — free inference endpoint cho learners
- **50+ language translations** — including Vietnamese (unique of 6 projects that has VN from source)
- **Jupyter notebook samples** — learnability over production-optimization
- **Protocol-aware** — covers MCP, A2A, NLWeb (Tier 0 infrastructure topics)
- **License MIT** — same như most siblings
- **Discord community** via Microsoft Foundry server

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 6th LLM Wiki, 6th routine run, first different-domain

### Expected milestones

- [x] Phase 0 Pre-flight (WebFetch-based, Tier 3 classification)
- [x] Phase 1 Setup — in progress
- [ ] Phase 2 Source ingestion — 3 summaries (Main README + 4 lesson cluster + MAF/Protocols cluster)
- [ ] Phase 3 Entity pages (4 — Agent Design Patterns, Agentic RAG, Multi-Agent Systems, Agentic Protocols)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **Tier 3 taxonomy expansion** (3-tier model: education + assistant + service)
- [ ] Phase 5 Iteration log v6
- [ ] Phase 6 Vault file updates
