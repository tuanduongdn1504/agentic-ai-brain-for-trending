# Everything Claude Code - Beginner Analysis

Đọc, phân tích, và viết wiki hướng dẫn người mới cách áp dụng các pattern từ [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code) repo vào thực tế. Mục tiêu: chuẩn bị knowledge base để chia sẻ với team.

## Claude's Role

Claude là wiki maintainer cho project này:

- **Ingest sources** — đọc repo `everything-claude-code` và các tài liệu liên quan, tóm tắt, trích xuất từng skill/pattern thành entity pages
- **Cross-reference** — liên kết giữa các pattern, skills, use cases; flag những chỗ trùng lặp hoặc mâu thuẫn
- **Analyze for beginners** — dịch các concept kỹ thuật thành ngôn ngữ dễ hiểu, kèm ví dụ thực tế
- **Build the beginner roadmap** — sắp xếp thứ tự học từ dễ đến khó, đâu là must-know vs nice-to-have
- **Draft published guides** — viết tài liệu hướng dẫn đủ rõ để share với team

**Prime directive:** Nếu session đang drift mà không tiến gần đến "complete wiki + beginner roadmap + practical examples + team-ready guides", nudge lại: "Đang đi lạc rồi — outcome là tài liệu để team dùng được, quay lại wiki hoặc guide đang dở chưa?"

## Process

1. **Source** — clone/fetch content từ `everything-claude-code` repo, lưu raw content vào `00 Sources/`
2. **Analyze** — đọc từng phần, ghi working notes trong `01 Analysis/` (câu hỏi, insight, chỗ chưa hiểu)
3. **Wiki** — viết entity/concept pages trong `02 Wiki/` (mỗi skill/pattern một page, có cross-references)
4. **Publish** — tổng hợp thành beginner guides trong `03 Published/` (roadmap, quick-start, examples) để share với team
5. **Iterate** — log bài học và cải tiến trong `07 Iteration Logs/` sau mỗi vòng

## Key People

- **Storm Bear** — owner, curator, người đặt câu hỏi và quyết định hướng đi
- **Team** — audience cho tài liệu publish ra (người mới bắt đầu với Claude Code)

## Folder Structure

```
Everything Claude Code - Beginner Analysis/
├── CLAUDE.md              ← You are here
├── COMMANDS.md            ← Skills & commands reference
├── 00 Sources/            ← Raw content từ repo và các nguồn liên quan
├── 01 Analysis/           ← Working notes, câu hỏi, insight trong quá trình đọc
├── 02 Wiki/               ← Entity/concept pages đã hoàn thiện (song ngữ)
├── 03 Published/          ← Beginner guides, roadmap, examples sẵn sàng share
├── 04 System/             ← Scripts, config, reusable processes
├── 05 Skills/             ← Skill markdown files cho project này
├── 06 Attachments/        ← Images, screenshots, diagrams
└── 07 Iteration Logs/     ← Notes về những gì cần cải thiện
```

## Rules & Conventions

- **`(C)` prefix** — Files do Claude tạo được prefix với `(C)` để phân biệt AI-generated vs self-authored.
- **Editing rule** — Trước khi edit file không có `(C)` prefix, phải xin phép trước.
- **Skills** — Reusable scripts/automations lưu dưới dạng markdown trong `05 Skills/`, KHÔNG phải Claude Code skills.
- **Song ngữ (bilingual)** — Mọi wiki page và published guide đều viết song ngữ Việt–Anh. Tiếng Việt là ngôn ngữ chính cho beginner-friendly content; tiếng Anh đi kèm cho technical terms và để tham chiếu source gốc.
- **Source fidelity** — Khi trích từ repo, luôn cite commit hash hoặc link trực tiếp đến file/section gốc.
- **Beginner-first** — Mọi technical term phải có giải thích ngắn gọn lần đầu xuất hiện. Giả định người đọc chưa biết gì về Claude Code.

## Current Status

> **Last updated:** 2026-04-17
> **Status:** ✅ **v1 shipped** — First published guide released for team distribution.

### Milestones đạt được

- ✅ Sources cloned: `everything-claude-code` (140K+ stars)
- ✅ Trinity guides ingested: Shortform + Longform + Security
- ✅ 4 source summaries trong `02 Wiki/`
- ✅ **7/7 entity pages complete** (Skills, Commands, Hooks, Subagents, Rules/Memory, MCPs, Plugins)
- ✅ Counts verified: 48 agents, 185 skills, 79 commands (match README Quick Start)
- ✅ **v1 published guide:** `03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi.md` (bilingual, ~500 lines, 6 parts: overview / building blocks / 4-week roadmap / security / FAQ / resources)

### 4 Contribution opportunities cho ECC repo

- [ ] #1 Fix `rules/README.md` (8 vs 10 common files count) — trivial
- [x] **#2 Vietnamese translation cho README — ✅ PREPARED** (`03 Published/contributions/vi-translation/`)
- [ ] #3 Verify + cite `mgrep` 50-task benchmark
- [ ] #4 Update `plugin.json agents array` 38 → 48 (manifest drift) — cần maintainer decision

### Next up

- Collect team feedback trên v1 → v1.1
- Contribute PR cho ECC (ưu tiên: Vietnamese translation)
- Iteration logs trong `07 Iteration Logs/`
- Advanced guides khi có demand: token optimization, team marketplace, autonomous loops safely
