# notebooklm-py - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`teng-lin/notebooklm-py`](https://github.com/teng-lin/notebooklm-py) — **unofficial Python API + CLI + agentic skill** cho Google NotebookLM. Full programmatic access gồm features mà web UI không expose. **New Tier 4 candidate** (Agent-as-bridge/connector) — khác Tier 1/2/3 từ v6 taxonomy. Mục tiêu: knowledge base + Tier 4 proposal + beginner guide position trong Storm Bear vault.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** v1 (7th auto-execution — second **different-domain** project, testing routine vs bridge/connector library):

- **Ingest sources via WebFetch** — README, SKILL.md (26KB), CLAUDE.md, CHANGELOG, AGENTS.md
- **Cross-reference với 6 sibling wikis** — 4 Tier 1 + 1 Tier 2 + 1 Tier 3
- **Phase 4b = Tier 4 proposal** — Agent-as-bridge/connector tier (extends 3-tier → 4-tier OR cross-cutting axis)
- **Beginner roadmap** — style khác: not "pick tool to use daily", is "know when to wire external service into Tier 1 workflow"

**Prime directive:** Outcome = wiki + Tier 4 taxonomy update + beginner guide explaining NotebookLM + notebooklm-py + when to integrate. Nudge nếu drift.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **Tier 4 proposal + cross-tier positioning** (different-domain routing, second time after v6).

## Key People

- **Storm Bear** — owner, curator
- **Team** — audience (researchers, Scrum coaches, knowledge workers who use NotebookLM)
- **Cross-project:** 6 sibling wikis shipped. This is 7th. Second **different-domain** after v6 course.
- **Original author:** teng-lin (solo maintainer, active development)

## Folder Structure

```
notebooklm-py - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← WebFetch-based (size-aware decision per routine v2 rule)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 6 siblings MANDATORY** — especially vì đây là second different-domain pivot
- **Note:** Source acquisition via WebFetch (repo small 26MB but skipping clone faster for doc-only build)
- **Note:** Repo has `CLAUDE.md` and `AGENTS.md` of its own — referenced but NOT copied (respecting upstream ownership)

## Positioning note

**notebooklm-py slot trong v6 3-tier + proposed v7 4-tier:**

| Tier | Frameworks | Purpose |
|------|-----------|---------|
| **Tier 1: Agent-as-assistant** | ECC, Superpowers, gstack, GSD | Dev tool use daily |
| **Tier 2: Agent-as-service** | goclaw | Platform deploy |
| **Tier 3: Agent-as-education** | ai-agents-for-beginners | Learn concepts first |
| **Tier 4: Agent-as-bridge (NEW v7)** | notebooklm-py | Connect agent to external service |

→ **First Tier 4 entrant.** Different purpose from other 3 tiers. Agents USE this library; library doesn't BE the agent.

## Unique positioning claims của notebooklm-py (từ Phase 0 probe)

- **"Unofficial Python API and agentic skill for Google NotebookLM"** — clear framing
- **"Features web UI doesn't expose"** — unique value proposition
- **Python API + CLI + Skill** — 3-way integration (not just library)
- **11,043 stars** — significant community traction
- **MIT License** — permissive
- **Active development** — pushed 2026-04-17 (1 day stale), v0.3.4 released 2026-03-12
- **1-2 week release cadence** — healthy maintenance
- **Python 3.10-3.14 support** — forward-compatible
- **4-layer architecture** — CLI → Client → Core → RPC (clean separation)
- **Undocumented Google RPC APIs** — fragility risk (stability policy documented)
- **Explicit agent compatibility** — Claude Code, Codex, OpenClaw (named)

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 7th LLM Wiki, 7th routine run, second different-domain (bridge/connector)

### Expected milestones

- [x] Phase 0 Pre-flight (API probe succeeded, 26MB manageable, Tier 4 classification)
- [x] Phase 1 Setup — in progress
- [ ] Phase 2 Source ingestion — 3 summaries (README + SKILL + CHANGELOG/AGENTS/CLAUDE cluster)
- [ ] Phase 3 Entity pages (4 — CLI Surface, Python API, Skill Integration, Web-UI-Exclusive Capabilities)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **Tier 4 proposal + cross-tier positioning**
- [ ] Phase 5 Iteration log v7
- [ ] Phase 6 Vault file updates
