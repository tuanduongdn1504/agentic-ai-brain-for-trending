# goclaw - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`nextlevelbuilder/goclaw`](https://github.com/nextlevelbuilder/goclaw) — **Multi-Tenant AI Agent Platform** built in Go. **Adjacent domain** vs 3 siblings (ECC/Superpowers/gstack là Claude Code skill frameworks; goclaw là agent platform/infrastructure). Mục tiêu: knowledge base + **taxonomy guide** positioning goclaw vs siblings as different architectural layer.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** (4th auto-execution):

- **Ingest sources** — README + CLAUDE.md + key docs (00-architecture, 01-agent-loop, 14-skills-runtime)
- **Cross-reference với 3 sibling wikis** — nhưng **reframe as taxonomy** (agent-as-assistant vs agent-as-service) chứ không forced 4-way comparison
- **Meta-relevance to Storm Bear vault:** goclaw's "Knowledge Vault với wikilinks + hybrid search" = Karpathy's LLM Wiki pattern **as infrastructure**. Worth deep-note.
- **Beginner roadmap** — adapt cho ops/platform audience (khác dev audience của 3 siblings)

**Prime directive:** Nếu drift, nudge: "Outcome = wiki + taxonomy guide. Quay lại nếu drift."

## Process — routine `llm-wiki-routine` v1

7 phases (Phase 0 → Phase 6). Continuous execution mode.

**Phase 4b reframed:** Agent framework taxonomy (not 4-way comparison — goclaw operates on different layer than 3 siblings).

## Key People

- **Storm Bear** — owner, curator
- **Team** — audience cho material publish
- **Cross-project context:** 3 sibling wikis shipped (ECC v1 + Superpowers v2 + gstack v3) → taxonomy guide leverages all 3

## Folder Structure

```
goclaw - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md            ← Routine reference
├── 00 Sources/            ← goclaw repo clone
├── 01 Analysis/           ← Working notes
├── 02 Wiki/               ← Entity pages song ngữ
├── 03 Published/          ← Beginner guide + taxonomy guide
├── 04 System/             ← (empty)
├── 05 Skills/             ← (empty)
├── 06 Attachments/
└── 07 Iteration Logs/     ← v4 build learnings
```

## Rules & Conventions

- **`(C)` prefix** — Files Claude tạo
- **Editing rule** — Xin phép trước khi edit non-`(C)` files
- **Song ngữ Việt–Anh** — Wiki + published bilingual
- **Source fidelity** — Cite file + line numbers
- **Cross-reference 3 siblings MANDATORY** — but mark layer difference explicitly
- **13-section format** từ `05 Skills/llm-wiki-ingest.md`
- **Vietnamese README note** — goclaw có `_readmes/README.vi.md` official → reference trong bilingual translation

## Positioning note

**Key framing cho tất cả deliverables:**

| Layer | Framework | What they enhance |
|-------|-----------|-------------------|
| **Agent-as-assistant** (dev workflow enhancement) | ECC, Superpowers, gstack | Claude Code → more capable coding agent |
| **Agent-as-service** (end-user platform) | **goclaw** | Multi-tenant AI agent platform for end users |

→ goclaw KHÔNG replace 3 siblings, KHÔNG compete. Different architectural tier.

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 4th LLM Wiki project, 4th auto-execution của routine

### Expected milestones

- [x] Phase 0 Pre-flight (URL accessible, threshold 42MB/117.md, adjacent domain detected)
- [x] Phase 1 Setup
- [ ] Phase 2 Source ingestion — README + CLAUDE.md + key architecture docs
- [ ] Phase 3 Entity pages — 4 building blocks
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **Agent framework taxonomy guide** (reframed — not 4-way comparison)
- [ ] Phase 5 Iteration log v4
- [ ] Phase 6 Vault file updates

**Total estimate:** 3-4 hours (large repo, adjacent domain requires reframing energy).
