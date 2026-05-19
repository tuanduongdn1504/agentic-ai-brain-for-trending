# agent-skills-standard — Hướng dẫn cho người mới (VN + EN)

> **Subject:** [HoangNguyen0403/agent-skills-standard](https://github.com/HoangNguyen0403/agent-skills-standard) — "The portable SDLC standards layer for AI coding agents. Sync once, then work in your own runtime."
> **Tác giả / Author:** **Nguyen Huy Hoang** (Senior Software Engineer at VMO Holding; Hanoi, Việt Nam)
> **License:** Apache 2.0
> **Wiki version:** v76 — **CORPUS-FIRST chủ thể VN trong corpus v60+**

---

## 🇻🇳 Tiếng Việt

### agent-skills-standard là gì?

**agent-skills-standard** là một thư viện **chuẩn coding** (coding standards) cho 10+ AI coding agent — gồm Claude Code, Cursor, GitHub Copilot, Gemini, Windsurf, Trae, Kiro, Roo, Codex, và MCP. Tác giả là **anh Hoàng** (Nguyễn Huy Hoàng) — Senior Software Engineer ở VMO Holding tại Hà Nội.

Anh Hoàng giải bài toán: "Mỗi team có chuẩn code riêng. Nhưng AI agent không biết gì cả." Thay vì copy-paste rule vào từng prompt (tốn nhiều token), agent-skills-standard cài đặt **1 nguồn chuẩn duy nhất** và **CLI tự sinh ra format riêng cho từng AI agent**.

### Đặc điểm nổi bật

- **259 coding standards** sẵn dùng cho 20+ framework (Flutter, React, Next.js, Angular, NestJS, TypeScript, Go, Spring Boot, Android, iOS, Swift, Kotlin, Java, PHP, Laravel, Dart, databases, và các vai trò chuyên biệt)
- **Tiết kiệm 85% token** so với prompt engineering truyền thống
- Hỗ trợ **10+ AI agent** thông qua CLI sinh format gốc cho từng tool
- Có **MCP server tùy chọn** với chế độ "Transparent Interception" + audit log
- Hoàn toàn local-first: không telemetry, không gửi data lên cloud, không cần API key

### Tại sao dùng agent-skills-standard?

**Vấn đề:** AI tạo code không theo chuẩn team. Bạn phải nhắc đi nhắc lại trong mỗi prompt. Tốn nhiều token. Khó maintain.

**Giải pháp:** agent-skills-standard cho phép viết chuẩn code **một lần duy nhất** ở 1 nguồn canonical, rồi **CLI tự sinh format riêng** cho từng AI agent mà team bạn dùng.

### Cài đặt nhanh

```bash
# 1. Khởi tạo: detect tech stack của project
npx agent-skills-standard@latest init

# 2. Đồng bộ: phân phối skills vào folder của các AI agent
npx agent-skills-standard@latest sync
```

Lệnh `sync` sẽ:
- Đọc nguồn canonical `skills/`
- Sinh **format gốc** cho mỗi AI agent project bạn dùng:
  - Claude / Roo / OpenCode → Markdown commands
  - Cursor / Trae / Codex → skill folders với SKILL.md
  - Gemini → TOML command files
  - Copilot → prompt instruction files
  - MCP → tool definitions
- Đặt outputs vào folder riêng (`.claude/`, `.cursor/`, ...)

### Cơ chế 3 tầng (3-tier hierarchical lookup) — chìa khóa cho "85% fewer tokens"

Cách cũ: mỗi prompt load TẤT CẢ rules → tốn 3,600+ tokens

Cách của agent-skills-standard:

```
File edit / AI task
        ↓
[Tầng 1] AGENTS.md router (~20 dòng) — map extension → category index
        ↓
[Tầng 2] Category _INDEX.md (~10-15 dòng) — File Match / Keyword Match triggers
        ↓
[Tầng 3] SKILL.md (~500 tokens) — chỉ load KHI conditions match
```

Chỉ ~25 dòng được quét cho mỗi edit thay vì 3,600+ tokens. Chi phí giảm từ O(n) xuống O(1).

### Config file `.skillsrc`

```yaml
agents:
  - claude
  - cursor
  - copilot

exclusions:
  - flutter/getx     # không dùng GetX

custom_skill_paths:
  - ./team-rules/    # rules riêng của team

mcp:
  scope: project     # project | user | snippets-only | disabled
```

### MCP server (tùy chọn)

Nếu bật MCP scope:
- Server **Transparent Interception** — bắt request file đọc của agent
- **Auto-inject** rules liên quan vào output
- **Audit log** ghi rõ skills nào đã ảnh hưởng đến mỗi quyết định của AI
- "Lazy Loading" — skills không load tới khi cần
- Giảm thêm ~90% scouting tokens

### Bảo mật

- Skills chỉ là **text (Markdown/JSON)** — KHÔNG executable code, KHÔNG filesystem access, KHÔNG network requests
- CLI chỉ tải text
- **Không telemetry**
- **Local-first** — data project ở máy bạn
- Auto-scan prompt injection patterns
- Mỗi skill có `evals.json` validate AI tuân thủ

### Khi nào KHÔNG nên dùng?

- Team chưa có chuẩn code (đây là layer phân phối, không phải tạo chuẩn)
- Project chỉ dùng 1 AI agent và OK với prompt injection
- Cần binary/executable skills (đây là text-only)

### Vì sao quan trọng cho cộng đồng VN?

**Anh Hoàng là CHỦ THỂ VN đầu tiên trong corpus v60+ (45 wikis trở về trước)** — chứng minh dev VN có thể xây dựng tool OSS đạt scale corpus (496★ + 147 forks + 10+ harness adoption). Đây là tham chiếu trực tiếp cho cộng đồng dev VN muốn publish OSS standards layer.

### Thông tin nhanh

- 🌟 **496 stars** ở 124 ngày = 4.0 stars/ngày (sustained-low velocity)
- 🍴 **147 forks** = **fork ratio 0.296 CORPUS-RECORD-HIGH** (1.66× kỷ lục cũ v65 17.8%)
- ⚠️ **0 open issues** = engagement-deficit-extreme (community via forks/PRs)
- 📦 **10+ AI agents** hỗ trợ qua CLI-generated native formats
- 📚 **259 skills × 20+ frameworks** = CORPUS-RECORD codification density
- 🏗️ Tác giả **Nguyễn Huy Hoàng** — Senior SE tại VMO Holding, **Hà Nội**
- 📜 **Apache 2.0** (README ghi nhầm "MIT License" — Pattern Library Pattern #83 sub-mechanism 83f)

---

## 🇬🇧 English

### What is agent-skills-standard?

**agent-skills-standard** is a **portable SDLC standards layer** for 10+ AI coding agents — Claude Code, Cursor, GitHub Copilot, Gemini, Windsurf, Trae, Kiro, Roo, Codex, and MCP. Author: **Nguyen Huy Hoang** — Senior Software Engineer at VMO Holding, Hanoi, Vietnam.

Hoang solves a real problem: "Every team has coding standards. But AI agents don't know them." Instead of copy-pasting rules into every prompt (token-expensive, maintenance nightmare), agent-skills-standard maintains **a single canonical source** and **the CLI generates native formats for each AI agent**.

### Key features

- **259 ready-to-use coding standards** across 20+ frameworks (Flutter, React, Next.js, Angular, NestJS, TypeScript, Go, Spring Boot, Android, iOS, Swift, Kotlin, Java, PHP, Laravel, Dart, databases, and specialist roles)
- **85% fewer tokens** than traditional prompt engineering
- Supports **10+ AI agents** via CLI-generated native formats
- Optional **MCP server** with "Transparent Interception" + audit logs
- Fully **local-first**: no telemetry, no cloud data, no API key required

### Why use agent-skills-standard?

**Problem:** AI agents don't follow your team's standards. You repeat rules in every prompt. Tokens cost a lot. Maintenance is hard.

**Solution:** Write standards ONCE in a canonical source, then have **the CLI generate native formats** for whichever AI agents your team uses.

### Quick install

```bash
# 1. Initialize: detect project tech stack
npx agent-skills-standard@latest init

# 2. Sync: distribute skills to AI agent folders
npx agent-skills-standard@latest sync
```

The `sync` command:
- Reads canonical `skills/` source
- Generates **native formats** for each AI agent your project uses
- Places outputs into agent-specific directories (`.claude/`, `.cursor/`, etc.)

### 3-tier hierarchical lookup (the "85% fewer tokens" mechanism)

Traditional: every prompt loads ALL rules → 3,600+ tokens

agent-skills-standard:

```
File edit / agent task
        ↓
[Tier 1] AGENTS.md router (~20 lines) — extension → category index
        ↓
[Tier 2] Category _INDEX.md (~10-15 lines) — File Match / Keyword Match triggers
        ↓
[Tier 3] SKILL.md (~500 tokens) — loaded ONLY when conditions match
```

~25 lines scanned per edit instead of 3,600+ tokens. O(n) → O(1).

### `.skillsrc` config

```yaml
agents:
  - claude
  - cursor
  - copilot

exclusions:
  - flutter/getx     # we don't use GetX

custom_skill_paths:
  - ./team-rules/    # project-specific rules

mcp:
  scope: project     # project | user | snippets-only | disabled
```

### MCP server (optional)

If MCP scope is enabled:
- **Transparent Interception** — server intercepts agent file reads
- **Auto-injects** relevant skill rules into output
- **Audit logs** — shows which skills informed each AI decision
- "Lazy Loading" + "Token Filtering" (~90% scouting-token reduction)

### Security model

- Skills are **text only** (Markdown/JSON) — no executable code, no filesystem access, no network requests
- CLI downloads text only
- **Zero telemetry**
- **Local-first** — project data stays on your machine
- Prompt-injection scanning at sync time
- `evals.json` per skill for AI adherence validation

### When NOT to use

- Your team has no existing standards (this is a distribution layer, not a standards generator)
- Your project uses one AI agent only
- You need binary/executable skills (this is text-only)

### Why this matters to the corpus

**Hoang Nguyen is the CORPUS-FIRST VN-located solo developer in the v60+ window** (45-wiki gap since pilot v3.2 hireui). This is direct evidence that VN-located solo developers can produce corpus-scale subjects (496★, 147 forks, 10+ harness adoption). For developers in Vietnam considering OSS publication, agent-skills-standard is a structural blueprint.

### Fast facts

- 🌟 **496 stars** at 124 days = 4.0 stars/day (sustained-low velocity)
- 🍴 **147 forks** = **fork ratio 0.296 CORPUS-RECORD-HIGH** (1.66× v65 17.8% prior record)
- ⚠️ **0 open issues** = engagement-deficit-extreme corpus-record-low
- 📦 **10+ AI agents** supported via CLI-generated native formats
- 📚 **259 skills × 20+ frameworks** = CORPUS-RECORD codification density
- 🏗️ Author **Nguyen Huy Hoang** — Senior SE at VMO Holding, **Hanoi, Vietnam**
- 📜 **Apache 2.0** (README mistakenly declares "MIT License")

---

## Thông tin nguồn / Sources

- Repository: https://github.com/HoangNguyen0403/agent-skills-standard
- NPM: https://www.npmjs.com/package/agent-skills-standard
- Author: https://github.com/HoangNguyen0403
- Author location: Hanoi, Vietnam (VMO Holding)
