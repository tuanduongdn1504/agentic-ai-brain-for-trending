# (C) README Summary — Everything Claude Code

> **Source:** `00 Sources/everything-claude-code/README.md`
> **Repo:** https://github.com/affaan-m/everything-claude-code
> **Ingested:** 2026-04-17
> **Coverage:** Đọc kỹ lines 1–600; lines 600–end chưa ingest đầy đủ.

---

## TL;DR

**VI:** ECC (Everything Claude Code) là một bộ "system" tối ưu hiệu năng cho AI coding agent — không chỉ là configs. Gồm **48 agents, 183 skills, 79 legacy commands**, hoạt động trên Claude Code, Codex, Cursor, OpenCode, Gemini và các harness khác. Tác giả là người thắng giải Anthropic Hackathon. Repo đã có 140K+ stars, 21K+ forks, 170+ contributors.

**EN:** ECC is a performance optimization system for AI coding agents — not just configs. It bundles **48 agents, 183 skills, 79 legacy commands**, working across Claude Code, Codex, Cursor, OpenCode, Gemini and other harnesses. Built by an Anthropic Hackathon winner. 140K+ stars, 21K+ forks, 170+ contributors.

---

## Vì sao tồn tại / Why it exists

Mục tiêu là biến một AI coding agent (như Claude Code) từ chatbot generic → thành một hệ thống production-grade, có:

1. **Token optimization** — chọn model phù hợp, cắt prompt thừa, đẩy bớt việc sang background
2. **Memory persistence** — hooks để lưu/load context giữa các session (agent "nhớ" được)
3. **Continuous learning** — tự extract pattern từ session thành reusable skills
4. **Verification loops** — checkpoint vs continuous evals, grader types, pass@k metrics
5. **Parallelization** — git worktrees, cascade method, scale instances
6. **Subagent orchestration** — giải quyết "context problem" bằng iterative retrieval pattern

> Ai đến từ "vibe coding" với Claude Code mà thấy bị giới hạn bởi context, hay làm sai, hay quên — đây là toolkit để fix những vấn đề đó.

---

## Ba tài liệu hướng dẫn chính / The Three Guides

Repo "chỉ chứa code thô" — phần giải thích nằm trong 3 guides:

| Guide | Nội dung | File trong repo |
|-------|----------|-----------------|
| **Shorthand Guide** | Setup, foundations, philosophy. **Đọc cái này TRƯỚC.** | `the-shortform-guide.md` (15.9 KB) |
| **Longform Guide** | Token optimization, memory persistence, evals, parallelization | `the-longform-guide.md` (14.8 KB) |
| **Security Guide** | Attack vectors, sandboxing, sanitization, CVEs, AgentShield | `the-security-guide.md` (27.9 KB) |

---

## Cấu trúc repo / Repo Structure

```
everything-claude-code/
├── .claude-plugin/   # Plugin & marketplace manifests
├── agents/           # 36+ specialized subagents (planner, code-reviewer, tdd-guide…)
├── skills/           # Workflow definitions & domain knowledge (chính, ưu tiên dùng)
├── commands/         # Legacy slash-command shims (đang được migrate sang skills/)
├── rules/            # Always-follow guidelines (copy thủ công vào ~/.claude/rules/)
├── hooks/            # Trigger-based automations (PreToolUse, PostToolUse, Stop…)
├── scripts/          # Cross-platform Node.js utilities cho hooks/setup
├── contexts/         # Dynamic system prompt injection (dev/review/research modes)
├── examples/         # Real-world CLAUDE.md (Next.js, Go, Django, Laravel, Rust…)
├── mcp-configs/      # MCP server configs (GitHub, Supabase, Vercel, Railway…)
├── tests/            # Test suite (997+ tests)
├── ecc_dashboard.py  # Tkinter desktop GUI để explore components
└── README.md         # File này
```

---

## Cài đặt / Installation

### Cách 1: Plugin (nhanh)

```bash
# Trong Claude Code:
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install everything-claude-code@everything-claude-code
```

### Cách 2: Manual (đáng tin cậy hơn)

```bash
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code
npm install        # hoặc pnpm/yarn/bun

# macOS/Linux
./install.sh --profile full                    # tất cả
./install.sh typescript python golang          # chỉ ngôn ngữ cần

# Windows
.\install.ps1 --profile full
```

> ⚠️ **Lưu ý:** Plugin install KHÔNG tự copy `rules/` — phải làm thủ công.
> ⚠️ **Note:** Plugin install does NOT auto-copy `rules/` — must do manually.

### Naming convention (dễ nhầm / easy to confuse)

| Surface | Identifier |
|---------|-----------|
| GitHub repo | `affaan-m/everything-claude-code` |
| Plugin install | `everything-claude-code@everything-claude-code` |
| npm package | `ecc-universal` |

---

## Concepts trọng yếu (cần entity page riêng) / Key concepts needing their own pages

> Đây là TODO list cho các lần ingest tiếp theo. Mỗi item nên thành 1 entity page trong wiki.

- [ ] **Agents** — subagent là gì, khi nào dùng, format `name/description/tools/model`
- [ ] **Skills** — workflow definitions, format `When to Use / How It Works / Examples`
- [ ] **Commands (legacy)** — slash commands, đang migrate sang skills
- [ ] **Hooks** — `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart`, hook profiles (`minimal/standard/strict`)
- [ ] **Rules** — always-follow guidelines, structure `common/ + <language>/`
- [ ] **Contexts** — dynamic prompt injection (`dev`/`review`/`research`)
- [ ] **MCP Configs** — Model Context Protocol server setup
- [ ] **Continuous Learning v1 vs v2** — Stop-hook pattern vs instinct-based với confidence scoring
- [ ] **Iterative Retrieval** — pattern giải quyết context problem cho subagents
- [ ] **Verification Loop / Eval Harness** — pass@k, grader types, checkpoint vs continuous
- [ ] **Strategic Compact** — manual compaction để giữ session khỏe
- [ ] **NanoClaw v2** — model routing, skill hot-load, session branch/search/export
- [ ] **AgentShield** — security scanner cho Claude Code config
- [ ] **Skill Creator** — sinh skill từ git history (local hoặc GitHub App)
- [ ] **PM2 + multi-* commands** — multi-agent orchestration (cần `ccg-workflow` runtime riêng)
- [ ] **ECC 2.0 alpha** — Rust control-plane prototype trong `ecc2/`
- [ ] **Hook Runtime Controls** — `ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS`
- [ ] **Package Manager Detection** — priority chain để chọn npm/pnpm/yarn/bun

---

## Lộ trình đọc cho người mới / Beginner reading order (proposed)

> Dự kiến — sẽ refine sau khi đọc 3 guides.

1. **`the-shortform-guide.md`** (15.9KB) — bắt buộc, đọc đầu tiên
2. **`README.md` phần "Quick Start"** (đã summary ở trên) — cài plugin + 1-2 skill cơ bản
3. **`examples/CLAUDE.md`** + **`examples/user-CLAUDE.md`** — xem 1 config thực tế
4. **`rules/common/*.md`** — coding-style, git-workflow, testing, security
5. **`the-longform-guide.md`** (14.8KB) — sau khi quen, học token optimization & memory persistence
6. **`skills/`** — chọn 3-5 skill liên quan stack của mình, đọc kỹ
7. **`the-security-guide.md`** (27.9KB) — trước khi dùng cho production code

---

## Cross-references

- [[(C) index]] — main catalog
- [[(C) log]] — activity log
- [[../01 Analysis/(C) README - open questions]] — open questions từ lần ingest này

## Citations

- README.md, lines 1–600 (full file 67KB, một phần chưa đọc kỹ)
- Repo CLAUDE.md (auto-loaded khi đọc): tóm tắt architecture & tests
