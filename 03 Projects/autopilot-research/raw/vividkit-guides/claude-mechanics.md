# Cơ chế Claude - Hiểu CLAUDE.md & Cấu hình | VividKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/claude-mechanics

> Extracted from: claude-mechanics.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



# Claude Mechanics

Hướng dẫn trực quan về cách Claude đọc instructions và ClaudeKit cấu hình project của bạn.

## CLAUDE.md là gì?

### Sách Công Thức cho Claude

Giống như sách công thức hướng dẫn đầu bếp, CLAUDE.md hướng dẫn Claude cách làm việc với project của bạn.

 Recipe Book tells Chef:

 1   Nguyên liệu nào dùng (tools, frameworks) 

 2   Cách chế biến (coding standards) 

 3   Quy tắc nhà bếp (những gì cần tránh) 

 CLAUDE.md tells Claude:

 1   Context project (tech stack, structure) 

 2   Coding standards (naming, patterns) 

 3   Workflows (cách plan, test, deploy) 

Lưu ý: Rules là guidance, không phải enforcement — Claude có thể bỏ sót. Nếu cần hành vi chắc chắn (auto-format, block nguy hiểm), dùng Hooks hoặc Permissions trong settings.json.

## Config Hierarchy

### Cách Config Files Xếp Chồng

Claude đọc config files theo 4 bước. Tất cả được concatenate (không override).

1

 Global user config  ` ~/.claude/CLAUDE.md `

Global user config — applies to all projects

2

 Project config (walk-up)  ` <project>/CLAUDE.md + CLAUDE.local.md `

Project config (walk-up from CWD to git root)

3

 Rules (user → project)  ` ~/.claude/rules/*.md → .claude/rules/*.md `

User rules first, then project rules (concatenated)

4

 Auto-memory  ` ~/.claude/projects/<project>/memory/MEMORY.md `

Auto-memory from past sessions (persistent)

Thứ tự: Global → Project → Rules → Memory

Tất cả files được concatenate — không override. File sau bổ sung thêm context, không thay thế.

#### Path-specific rules (nâng cao)

Đặt CLAUDE.md trong subfolder để rules chỉ apply khi Claude edit files trong folder đó. Hữu ích cho monorepo: frontend/backend có convention khác nhau.

``` bg-slate-100
project/
├── CLAUDE.md           # Áp dụng toàn project
├── frontend/
│   └── CLAUDE.md       # Chỉ load khi Claude edit trong frontend/
└── backend/
    └── CLAUDE.md       # Chỉ load khi Claude edit trong backend/
```

## `ck init` — Tạo những gì?

\$ ck init --kit engineer

Khi chạy ck init, ClaudeKit tải và cài đặt kit hoàn chỉnh vào project của bạn.

project/

  CLAUDE.md   Template (customize after) 

  AGENTS.md   Agent definitions 

  .gitignore 

  .repomixignore   Repomix ignore patterns 

  release-manifest.json   Kit version manifest 

  plans/   Plans directory 

  .opencode/   OpenCode compatibility 

  .claude/   ClaudeKit config 

  .ck.json   Kit metadata 

  settings.json   Claude Code settings 

  metadata.json   Deletion patterns 

  statusline.cjs   Statusline config 

  .env.example   Environment template 

  .mcp.json.example   MCP config template 

  agents/   14+ definitions 

  hooks/   22+ hooks 

  rules/   Workflow rules 

  skills/   90+ commands 

  scripts/   Utility scripts 

  schemas/   JSON schemas 

  output-styles/   Response formats 

  session-state/   Session tracking 

✓ Kit installed successfully

#### Common Flags:

` --kit engineer ` Kit nào để cài

` -g, --global ` Cài vào ~/.claude/ — áp dụng cho TẤT CẢ projects trên máy (thay vì chỉ project hiện tại)

` --fresh ` Reset CK files trong .claude/ (agents, skills, rules, hooks) + settings.json.\
• Project-mode: CLAUDE.md ở root được giữ.\
• Global-mode (-g): ~/.claude/CLAUDE.md bị replace.

## Config Kit vs Config Của Bạn

### Files ClaudeKit

Đừng sửa trực tiếp!

Do ClaudeKit quản lý

-    ` .claude/skills/* `
-    ` .claude/hooks/* `
-    ` .claude/agents/* `
-    ` .claude/settings.json `

### Files Của Bạn

Thoải mái chỉnh sửa!

Your customizations

-    ` CLAUDE.md (your additions) `
-    ` .claude/rules/* `
-    ` CLAUDE.local.md `
-    ` .env (gitignored) `

## Câu Hỏi Thường Gặp

 Q   ck init đã ghi đè CLAUDE.md của tôi!  

Mặc định, ck init merge configs và không ghi đè files hiện có. Chỉ có flag --fresh mới reset hoàn toàn.

 Q   Nên đặt custom rules ở đâu?  

Tạo files trong thư mục .claude/rules/. ClaudeKit sẽ không ghi đè những files này. Hoặc thêm vào CLAUDE.local.md cho preferences cá nhân (gitignored).

 Q   Khác biệt giữa global và local install là gì?  

ck init -g → ~/.claude/ (áp dụng cho TẤT CẢ projects). ck init → ./.claude/ (chỉ project này). Bắt đầu với local, chỉ dùng global cho preferences thực sự phổ quát.

 Q   Rules trong CLAUDE.md có tự động enforce không?  

Không. Rules chỉ là guidance — Claude cố gắng tuân thủ nhưng có thể bỏ sót. Muốn đảm bảo 100% (ví dụ: chặn lệnh nguy hiểm, auto-format trước commit), hãy dùng Hooks hoặc Permissions trong .claude/settings.json.

 Q   CLAUDE.md nên viết dài bao nhiêu?  

Dưới 200 dòng là lý tưởng. File càng ngắn và cụ thể, Claude càng dễ follow. Nội dung dài hơn nên tách vào .claude/rules/\*.md và link từ CLAUDE.md bằng @-references.

Vẫn còn thắc mắc? Xem hướng dẫn "[How ClaudeKit Works](/vi/guides/how-ck-works)" để hiểu rõ hơn về cách các skills và hooks hoạt động.

