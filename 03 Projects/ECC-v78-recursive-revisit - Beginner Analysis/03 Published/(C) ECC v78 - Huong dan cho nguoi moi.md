# (C) ECC v78 — Hướng dẫn cho người mới / Beginner Guide

**Subject:** affaan-m/ECC — "The harness-native operator system for agentic work. From an Anthropic hackathon winner."
**Repo:** https://github.com/affaan-m/ECC
**Homepage / Pro:** https://ecc.tools
**License:** MIT (OSS free forever) + ECC Pro $19/seat/mo

---

## 🇻🇳 Tiếng Việt

### ECC là gì?

ECC là một **operator system đa-harness** miễn phí MIT cho công việc agentic AI. Tác giả **Affaan Mustafa** (Anthropic Hackathon Winner) đã build ECC qua 10+ tháng dùng hằng ngày — production-ready agents + skills + hooks + commands + MCP configs cho **Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, GitHub Copilot** và nhiều harness khác.

> "Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development."

ECC có **README tiếng Việt** ở `docs/vi-VN/README.md` — đây là 1 trong 10+ ngôn ngữ hỗ trợ.

### Quy mô (xác minh GitHub API 2026-05-20)

| Chỉ số | Giá trị |
|--------|---------|
| Stars | **187,238** (kỷ lục corpus về velocity) |
| Forks | 28,997 |
| Open issues | 1 |
| Tuổi repo | 122 ngày (tạo 2026-01-18) |
| Last push | 2026-05-20 (active hôm nay) |
| Velocity | **1,535 stars/ngày** kỷ lục corpus |
| Contributors | 170+ |

### 5 nguyên tắc cốt lõi (từ CLAUDE.md)

1. **Agent-First** — Giao việc cho specialized agents
2. **Test-Driven** — Test trước implementation; 80%+ coverage bắt buộc
3. **Security-First** — Không bao giờ妥协 về security; validate mọi input
4. **Immutability** — Luôn tạo object mới, không mutate
5. **Plan Before Execute** — Plan trước khi viết code phức tạp

Cộng thêm **Prompt Defense Baseline** ngay trong CLAUDE.md (corpus-first explicit prompt-injection-defense).

### Kiến trúc tổng thể

- **60 specialized agents** (planner, architect, tdd-guide, code-reviewer, security-reviewer, build-resolver, python-reviewer, go-reviewer, django-reviewer, kotlin-reviewer, etc.)
- **232 codified skills** (workflow definitions)
- **75 slash commands** (`/tdd` `/plan` `/e2e` `/code-review` `/build-fix` `/learn` `/skill-create`)
- **75 legacy command shims** (backward-compat cho renames)
- **11+ harness directories** trong repo (.claude/.codex/.cursor/.opencode/.gemini/.kiro/.trae/.qwen/.zed/.codebuddy/.agents)
- **manifests/** + **schemas/** + **research/** + **contexts/** (6-layer LDS — kỷ lục corpus về codification density)

### Mô hình kinh tế 2-tầng (corpus-first)

| Kênh | Giá | Phù hợp |
|------|-----|---------|
| **git clone** | free MIT | Đọc source, full repo |
| **npm `ecc-universal`** | free | Cross-harness installer |
| **npm `ecc-agentshield`** | free | Skill scan security |
| **GitHub App `ecc-tools`** | freemium | PR audit (150+ installs) |
| **ECC Pro** | **$19/seat/tháng** | Private repos + Pro features |
| **GitHub Sponsors** | $5+/tháng | Hỗ trợ maintainer |

Triết lý: **"OSS stays free forever. Pro funds the maintainer."**

### Cách bắt đầu

1. Vào https://github.com/affaan-m/ECC
2. Đọc README tiếng Việt ở `docs/vi-VN/README.md`
3. Chọn kênh phân phối:
   - **Vibe đầy đủ:** `git clone` + đọc CLAUDE.md + AGENTS.md
   - **Cài nhanh:** `npm install -g ecc-universal`
   - **Chỉ security:** `npm install -g ecc-agentshield`
   - **Hosted PR audits:** install ECC GitHub App
4. Chọn 1 agent để thử trước — `planner` hoặc `tdd-guide` là điểm khởi đầu phổ biến
5. Adopt 5-nguyên-tắc workflow

### Khi nào KHÔNG nên dùng ECC

- Bạn cần single-harness simplicity (ECC opinionated multi-harness; 60 agents là surface cao cho người mới)
- Bạn muốn tránh SaaS dependency (Pro tier có thể tạo funding-path mong muốn không có)
- Bạn thích build skills từ đầu (ECC 232 skills là batteries-included)
- Bạn chưa có 5-nguyên-tắc discipline cho daily workflow

---

## 🇬🇧 English

### What is ECC?

ECC is a **multi-harness operator system** for AI-assisted software development, MIT-licensed, built by **Affaan Mustafa** (Anthropic Hackathon Winner) over 10+ months of intensive daily use. Production-ready **agents + skills + hooks + commands + MCP configurations** across **Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, GitHub Copilot** and more.

> "Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development."

ECC ships a Vietnamese README at `docs/vi-VN/README.md` as 1 of 10+ supported locales.

### Scale (verified GitHub API 2026-05-20)

| Metric | Value |
|--------|-------|
| Stars | **187,238** (CORPUS-RECORD velocity) |
| Forks | 28,997 |
| Open issues | 1 |
| Repo age | 122 days (created 2026-01-18) |
| Last push | 2026-05-20 (active today) |
| Velocity | **1,535 stars/day** corpus-record |
| Contributors | 170+ |

### 5 core principles (from CLAUDE.md)

1. **Agent-First** — Delegate to specialized agents
2. **Test-Driven** — Tests before implementation; 80%+ coverage required
3. **Security-First** — Never compromise on security; validate all inputs
4. **Immutability** — Always create new objects, never mutate
5. **Plan Before Execute** — Plan complex features before code

Plus **Prompt Defense Baseline** in CLAUDE.md (CORPUS-FIRST explicit prompt-injection-defense at project scope).

### Architecture summary

- **60 specialized agents** (planner, architect, tdd-guide, code-reviewer, security-reviewer, build-resolver, language-specialists)
- **232 codified skills**
- **75 slash commands** + **75 legacy command shims**
- **11+ harness directories** in repo (.claude, .codex, .cursor, .opencode, .gemini, .kiro, .trae, .qwen, .zed, .codebuddy, .agents)
- **6-layer LDS surface** (manifests/ + schemas/ + research/ + contexts/ + skills/ + agents/) — CORPUS-RECORD codification density

### Dual-tier economic model (corpus-first)

| Channel | Cost | Best for |
|---------|------|----------|
| **git clone** | free MIT | Reading source |
| **npm `ecc-universal`** | free | Cross-harness installer |
| **npm `ecc-agentshield`** | free | Security skill collection |
| **GitHub App `ecc-tools`** | freemium | Hosted PR audits (150+ installs) |
| **ECC Pro** | **$19/seat/mo** | Private repos + Pro features |
| **GitHub Sponsors** | $5+/mo | Fund maintainer |

Philosophy: **"OSS stays free forever. Pro funds the maintainer."**

### How to start

1. Visit https://github.com/affaan-m/ECC
2. Read language-appropriate README — Vietnamese at `docs/vi-VN/README.md`
3. Choose distribution channel
4. Pick a single agent to evaluate first (`planner` or `tdd-guide` are common)
5. Adopt 5-principle workflow

### When NOT to adopt ECC

- You need single-harness simplicity (60 agents is high cognitive surface)
- You want to avoid SaaS dependency (Pro tier creates funding-path)
- You prefer building skills from scratch (ECC 232 skills are batteries-included)
- You don't have 5-principle discipline yet

---

## v1 → v78 corpus-recursive delta

If you read the v1 wiki (2026-04-17), the meta-architecture has substantially shifted:

| Axis | v1 (89 days old) | v78 (122 days old) |
|------|-------------------|----------------------|
| Repo name | `everything-claude-code` | `ECC` (renamed) |
| Harness scope | Claude-Code-only | 7+ harnesses, 11+ dirs |
| Skills count | small documented set | 232 codified |
| Agents count | subagents only | 60 specialized agents |
| Economic model | OSS-only | OSS + ECC Pro $19/seat/mo + Sponsors |
| Version | unversioned | v2.0.0-rc.1 Hermes |
| Locales | EN-primary | 10+ including Vietnamese |
| Hackathon status | unmentioned | **Anthropic Hackathon Winner** |

---

## Vault-context notes (Storm Bear)

- v78 is CORPUS-FIRST corpus-recursive anchor revisitation (v1 → v78 at 33-day delta)
- HIGH-RELEVANCE vault pilot candidate position #3 (fenced-scope: skill subset rather than full operator-system install)
- Pilot ranking post-v78: cc-switch #1 + agent-skills-standard #2 + **ECC NEW v78 #3** + codegraph #4 + agents-best-practices #5 + agentmemory #6
- Vietnamese-locale README presence = direct Storm Bear cultural-peer-locale evidence (CORPUS-FIRST Phase 0.9 (a) axis-call via product-locale-inclusion)
- Velocity 1,535/d = CORPUS-RECORD sustained EXTREME-VIRAL

**Build:** v78 wiki 2026-05-20 (fourteenth wiki under routine v2.2; corpus-recursive revisit of v1 anchor)
