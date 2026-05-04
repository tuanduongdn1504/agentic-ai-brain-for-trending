# gstack - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ hướng dẫn người mới về [`garrytan/gstack`](https://github.com/garrytan/gstack) — Garry Tan (YC President & CEO) framework biến Claude Code thành "virtual engineering team" với 23 specialists + 8 power tools, tất cả là slash commands. Mục tiêu: knowledge base + **comparison guide 3-way ECC vs Superpowers vs gstack** để team chọn đúng tool.

## Claude's Role

Claude là wiki maintainer cho project này, **chạy bằng routine `llm-wiki-routine`** từ vault (proven trong 2 projects trước):

- **Ingest sources** — README + CLAUDE.md + ETHOS + ARCHITECTURE + CHANGELOG (skim-first cho file >20KB)
- **Cross-reference với ECC + Superpowers wikis** — đây là project thứ 3 trong cùng domain (AI coding agent frameworks), value cross-project synthesis cao
- **Comparison guide 3-way** — output đặc biệt: ECC vs Superpowers vs gstack (3-way decision matrix unique cho Storm Bear vault)
- **Beginner roadmap** — tương tự 2 project trước nhưng adapt cho gstack's CEO-first workflow

**Prime directive:** Nếu drift, nudge: "Outcome là wiki + comparison 3-way + beginner roadmap. Quay lại nếu drift."

## Process — chạy bằng routine `llm-wiki-routine`

7 phases (Phase 0 → Phase 6) per `05 Skills/llm-wiki-routine.md`. Continuous execution mode.

## Key People

- **Storm Bear** — owner, curator
- **Team** — audience cho material publish
- **Cross-project context:** Wiki ECC (v1, 2026-04-17) + Wiki Superpowers (v2, 2026-04-18) đã ship — leverage cho 3-way comparison

## Folder Structure

```
gstack - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md            ← Routine reference
├── 00 Sources/            ← gstack repo clone
├── 01 Analysis/           ← Working notes
├── 02 Wiki/               ← Entity/concept pages song ngữ
├── 03 Published/          ← Beginner guide + 3-way comparison
├── 04 System/
├── 05 Skills/
├── 06 Attachments/
└── 07 Iteration Logs/     ← v3 build learnings
```

## Rules & Conventions

- **`(C)` prefix** — Files Claude tạo
- **Editing rule** — Xin phép trước khi edit non-`(C)` files
- **Song ngữ Việt–Anh** — Wiki + published bilingual
- **Source fidelity** — Cite commit hash + line numbers
- **Beginner-first** — Technical term giải thích lần đầu xuất hiện
- **Cross-reference 2 sibling wikis** — ECC + Superpowers analogs MANDATORY
- **13-section format** từ `05 Skills/llm-wiki-ingest.md`

## Comparison axis — gstack vs siblings

Đây là deliverable đặc biệt — **3-way decision matrix:**

| Axis | ECC | Superpowers | gstack |
|------|-----|-------------|--------|
| Author | Affaan Mustafa | Jesse Vincent (obra) | Garry Tan (YC President) |
| Stars | 140K+ | TBD | TBD verify |
| Approach | Performance optimization | Methodology framework | "Virtual engineering team" / role-based |
| Scope | 185 skills + 48 agents + 79 commands | 14 skills + 1 agent | 23 specialists + 8 power tools (slash commands) |
| Workflow | Sequential phases (flexible) | 7-stage hard-gated | CEO → eng → designer → reviewer → QA → security → release pipeline |
| TDD | Skill-based | Iron Law mandatory | Built into review/qa commands |
| Cross-harness | 5 harnesses | 7 harnesses | TBD verify (Codex folder exists) |
| Distribution | Plugin + manual | Marketplace + git URL | TBD |
| Best for | Broad capability | Discipline + production | Solo founder velocity (600K LOC/60 days claim) |

→ Final 3-way comparison guide sẽ fill bảng này.

## Current Status

> **Last updated:** 2026-04-18
> **Status:** 🟡 Routine auto-execute IN PROGRESS — first run của routine `llm-wiki-routine`

### Expected milestones

- [x] Phase 0 Pre-flight (URL accessible, threshold passed, sibling detected → Phase 4b enabled)
- [x] Phase 1 Setup (3-5 phút)
- [ ] Phase 2 Source ingestion — README + CLAUDE.md + ETHOS+ARCHITECTURE+CHANGELOG
- [ ] Phase 3 Entity pages — 4 building blocks
- [ ] Phase 4a Beginner published guide
- [ ] Phase 4b **3-way comparison guide ECC vs Superpowers vs gstack** (special deliverable)
- [ ] Phase 5 Iteration log v3 — verify routine hoạt động
- [ ] Phase 6 Vault file updates

**Total estimate:** 3-4 hours per routine velocity targets (medium repo size).
