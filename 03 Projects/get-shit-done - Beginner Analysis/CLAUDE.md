# get-shit-done - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`gsd-build/get-shit-done`](https://github.com/gsd-build/get-shit-done) — "meta-prompting, context engineering and spec-driven development system" cho 14+ AI coding harnesses. **Same tier** với ECC/Superpowers/gstack (Tier 1: agent-as-assistant). Mục tiêu: knowledge base + **4-way comparison Tier 1** (ECC vs Superpowers vs gstack vs GSD) để team chọn đúng tool.

## Claude's Role

Claude là wiki maintainer, **chạy bằng routine `llm-wiki-routine`** v1 (5th auto-execution — first project resuming same-domain comparison after v4 adjacent-domain taxonomy reframe):

- **Ingest sources** — README (927 lines), USER-GUIDE (1184 lines), docs/ARCHITECTURE + key docs
- **Cross-reference với 4 sibling wikis** — 3 Tier 1 (ECC/Superpowers/gstack) + 1 Tier 2 (goclaw)
- **4-way comparison Tier 1** — GSD slot trong Tier 1 mental model từ v4 taxonomy
- **Beginner roadmap** — adapt cho "context rot" focus (unique positioning của GSD)

**Prime directive:** Outcome = wiki + 4-way Tier 1 comparison + beginner roadmap. Nudge nếu drift.

## Process — routine `llm-wiki-routine` v1

7 phases. Continuous execution. Phase 4b = **4-way Tier 1 comparison** (same-domain routing, since v4 taxonomy established Tier 1 slot).

## Key People

- **Storm Bear** — owner, curator
- **Team** — audience
- **Cross-project:** 4 sibling wikis đã ship. This is 5th. Tier 1 slot now complete với 4 frameworks.

## Folder Structure

```
get-shit-done - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md
├── 00 Sources/            ← gsd repo clone (13MB, 396 .md)
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04-07/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ + 13-section format
- **Cross-reference 4 siblings MANDATORY** — especially 3 Tier 1 siblings cho comparison
- **Note: GSD doesn't have VN translation** (unlike goclaw) — 4 languages only (en/pt-BR/zh-CN/ja-JP/ko-KR)

## Positioning note

**GSD slot trong v4 taxonomy:**

| Tier | Frameworks |
|------|-----------|
| **Tier 1: Agent-as-assistant** | ECC, Superpowers, gstack, **GSD** |
| **Tier 2: Agent-as-service** | goclaw |

→ GSD is 4th entrant Tier 1. 4-way comparison unlocks "spectrum" insight.

## Unique positioning claims của GSD (từ Phase 0 survey)

- **"Solves context rot"** — specific problem framing (unique vs siblings)
- **14+ harnesses** — most supported (ECC 5, Superpowers 7, gstack 10, GSD 14)
- **$GSD Solana token** + "gsd_foundation" — crypto-backed (first of 5 projects)
- **Explicit competitors named:** "SpecKit, OpenSpec, Taskmaster"
- **npm installable:** `npx get-shit-done-cc@latest`
- **TypeScript-based** (has `sdk/`, `tests/`, `vitest.config.ts`)
- **33 agents folder / 21 in docs** — discrepancy worth noting

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — 5th LLM Wiki, 5th routine run, Tier 1 completion

### Expected milestones

- [x] Phase 0 Pre-flight (13MB, 396 .md, same-tier 4-way routing)
- [x] Phase 1 Setup
- [ ] Phase 2 Source ingestion — README + USER-GUIDE + ARCHITECTURE+COMMANDS+key docs
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **4-way Tier 1 comparison** (ECC vs Superpowers vs gstack vs GSD)
- [ ] Phase 5 Iteration log v5
- [ ] Phase 6 Vault file updates
