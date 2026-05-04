# Superpowers - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ hướng dẫn người mới về [`obra/superpowers`](https://github.com/obra/superpowers) framework — methodology + skills library cho AI coding agents do Jesse Vincent (`obra`) build. Mục tiêu: chuẩn bị knowledge base + **comparison guide với ECC** để team chọn đúng tool.

## Claude's Role

Claude là wiki maintainer cho project này, **áp dụng skill `llm-wiki-ingest` từ vault** (proven trong project ECC):

- **Ingest sources** — đọc repo `superpowers` + related docs, tóm tắt, trích xuất entity pages cho 7-stage workflow + skills library + subagent patterns
- **Cross-reference với ECC wiki** — đây là value-add unique vì Storm Bear đã có ECC analysis. Mỗi concept trong superpowers nếu có analog trong ECC, link cross-project.
- **Comparison guide** — output đặc biệt: `ECC vs Superpowers` để team biết chọn cái nào theo use case
- **Beginner roadmap** — tương tự ECC project nhưng adapt cho superpowers methodology
- **Test pattern generalization** — đây là **Phase 2 target #5** trong GOALS.md ("Apply LLM Wiki pattern cho 1 project không phải ECC"). Verify skill generalize hay cần tuning.

**Prime directive:** Nếu session đang drift mà không tiến gần "complete wiki + comparison guide ECC vs Superpowers + beginner roadmap + team-ready material", nudge lại: "Đang đi lạc rồi — outcome là material để team chọn đúng tool, quay lại wiki/comparison đang dở chưa?"

## Process — theo skill `llm-wiki-ingest` (5 phases)

1. **Phase 1 Setup** — clone `superpowers` vào `00 Sources/`, tạo `02 Wiki/(C) index.md` + `(C) log.md` + `01 Analysis/(C) open questions.md` ngay
2. **Phase 2 Source ingestion** — README → main docs → key SKILL.md files (target 2-3 source summaries trước entity pages)
3. **Phase 3 Entity pages** — 13-section canonical format cho building blocks chính (7-stage workflow, skills, subagents, TDD enforcement, etc.)
4. **Phase 4 Published guide** — bilingual beginner guide + **comparison guide ECC vs Superpowers** (unique deliverable)
5. **Phase 5 Iteration log** — capture learnings để compare với ECC v1 baseline (verify skill compound)

## Key People

- **Storm Bear** — owner, curator, người đặt câu hỏi và quyết định hướng đi
- **Team** — audience cho material publish ra (cùng team với ECC project)
- **Cross-project context:** Wiki ECC đã ship trong `03 Projects/Everything Claude Code - Beginner Analysis/` — leverage cho comparison

## Folder Structure

```
Superpowers - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md            ← Skills & commands reference
├── 00 Sources/            ← Raw repo clone + related docs
├── 01 Analysis/           ← Working notes, câu hỏi, comparison drafts
├── 02 Wiki/               ← Entity/concept pages song ngữ (theo 13-section format)
├── 03 Published/          ← Beginner guide + ECC vs Superpowers comparison
├── 04 System/             ← Scripts, config, reusable processes
├── 05 Skills/             ← Project-specific skills (nếu sinh ra)
├── 06 Attachments/        ← Images, screenshots, diagrams
└── 07 Iteration Logs/     ← Notes về cải thiện + so sánh với ECC v1
```

## Rules & Conventions

- **`(C)` prefix** — Files do Claude tạo prefix `(C)` (theo vault rule)
- **Editing rule** — Trước khi edit file không có `(C)` prefix, xin phép trước
- **Skills folder** — Reusable scripts/automations dưới dạng markdown trong `05 Skills/` (KHÔNG phải Claude Code skills)
- **Song ngữ Việt–Anh** — Wiki + published guide bilingual; tiếng Việt chính, English cho technical terms
- **Source fidelity** — Trích từ repo → cite commit hash hoặc link trực tiếp
- **Beginner-first** — Technical term có giải thích lần đầu xuất hiện
- **Cross-reference ECC wiki** — Khi concept có analog trong ECC, link sang `03 Projects/Everything Claude Code - Beginner Analysis/02 Wiki/` (cross-project knowledge graph)
- **Apply 13-section entity format** từ `05 Skills/llm-wiki-ingest.md` — không re-design format, dùng proven baseline

## Comparison axis — ECC vs Superpowers

Đây là deliverable đặc biệt. Khi build wiki, track theo các axis:

| Axis | ECC | Superpowers |
|------|-----|-------------|
| Author | Affaan Mustafa | Jesse Vincent (obra) |
| Stars | 140K+ (verified) | TBD verify |
| Approach | Performance optimization system | Methodology + structured workflow |
| Scope | 48 agents + 185 skills + 79 commands | TBD |
| Workflow style | TBD vs 7-stage | 7-stage explicit |
| TDD | Skill-based (tdd-workflow) | Built-in enforcement |
| Subagent | 48 specialized | TBD |
| Cross-harness | Claude/Codex/Cursor/OpenCode/Gemini | Claude/Cursor/Codex/Gemini/Copilot |
| Security | AgentShield + 11-item bar | TBD |
| Distribution | Plugin + manual install | Claude marketplace |
| Best for | TBD use cases | TBD use cases |

→ Final published comparison guide sẽ fill bảng này.

## Current Status

> **Last updated:** 2026-04-18
> **Status:** Just created — ready cho Phase 1 setup. **Second LLM Wiki project** of Storm Bear vault — testing skill `llm-wiki-ingest` generalization.

### Expected milestones (theo iteration log v1 baseline)

- [ ] Phase 1 Setup (5-10 phút)
- [ ] Phase 2 Source ingestion — main README + key docs (~3 sources, 45-60 phút)
- [ ] Phase 3 Entity pages — 4-7 building blocks (2-3 hours)
- [ ] Phase 4a Published beginner guide (30-40 phút)
- [ ] Phase 4b **Published comparison guide ECC vs Superpowers** (40-50 phút, deliverable đặc biệt)
- [ ] Phase 5 Iteration log v2 (15-20 phút) — compare với ECC v1 patterns

**Total estimate:** ~5-7 hours (theo data từ ECC v1; có thể faster vì pattern proven)

<!-- TODO: Update khi tiến độ tăng -->
