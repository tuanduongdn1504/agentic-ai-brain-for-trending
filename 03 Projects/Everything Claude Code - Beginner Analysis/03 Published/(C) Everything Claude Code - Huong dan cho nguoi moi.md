# Everything Claude Code — Hướng dẫn cho người mới

> **For team / Cho team:** Đây là hướng dẫn tổng hợp để bắt đầu với **Claude Code** + **Everything Claude Code (ECC)**. Đọc 1 lần ~30 phút, đủ để setup và chạy production-ready workflow.
>
> **Tác giả wiki:** Storm Bear, dựa trên `affaan-m/everything-claude-code` (140K+ stars, Anthropic Hackathon Winner).
> **Ngày:** 2026-04-17 | **Phiên bản:** v1
> **Song ngữ:** Tiếng Việt (chính) + English (technical terms)

---

## 📋 Mục lục

1. [Tại sao đọc cái này](#tại-sao-đọc-cái-này)
2. [Part 1: Claude Code + ECC là gì](#part-1-claude-code--ecc-là-gì)
3. [Part 2: 7 Building Blocks](#part-2-7-building-blocks-của-claude-code)
4. [Part 3: Setup roadmap 4 tuần](#part-3-setup-roadmap-4-tuần)
5. [Part 4: Security minimum bar](#part-4-security-minimum-bar)
6. [Part 5: FAQ thường gặp](#part-5-faq-thường-gặp)
7. [Part 6: Resources & References](#part-6-resources--references)

---

## Tại sao đọc cái này

### Ai nên đọc / Who should read

- **Dev team** đang/sắp dùng Claude Code cho coding hằng ngày
- **Tech lead / Scrum Coach** cần standardize workflow AI agent cho team
- **Anyone** từng thử AI coding assistant (Cursor, Copilot) và muốn lên level production

### Bạn sẽ có gì sau khi đọc / What you'll get

- Hiểu **7 building blocks** của Claude Code (Skills, Commands, Hooks, Subagents, Rules, MCPs, Plugins)
- Biết khi nào dùng block nào, tránh overlap
- **Setup roadmap 4 tuần** concrete từ zero → productive
- **Security minimum bar** 11 điểm để không bị RCE / leak API key / data exfiltration
- Danh sách **resources** để đào sâu tiếp

### Không phải là gì / What this is NOT

- ❌ Không phải tutorial cài Claude Code từ đầu (xem docs chính thức)
- ❌ Không phải reference đầy đủ (xem wiki entity pages + official docs)
- ❌ Không cover advanced topics (custom MCP server build, agent eval harness, ECC 2.0 Rust prototype)

---

## Part 1: Claude Code + ECC là gì

### Claude Code

**Claude Code** là CLI tool của Anthropic — biến Claude thành coding agent có thể:
- Đọc/edit file trong codebase
- Chạy shell commands
- Trigger tests, builds, deploys
- Delegate task cho subagents
- Tích hợp với editor (Zed, VSCode, Cursor) và external services (GitHub, Supabase, Vercel…)

**Khác với ChatGPT / Copilot ở đâu:**
- **Agentic** — Claude tự quyết định action, không chỉ suggest
- **Persistent context** — CLAUDE.md + session files giữ context cross-session
- **Tool use** — call functions, read files, execute commands
- **Harness** — có hooks, subagents, rules, skills làm infrastructure

### Everything Claude Code (ECC)

**ECC** là một **plugin / configuration pack** cho Claude Code, do Affaan Mustafa (Anthropic Hackathon Winner) build qua 10+ tháng dùng hằng ngày.

**ECC không phải là Claude Code mới** — nó là **"performance optimization system for AI agent harnesses"** chồng lên Claude Code để:
- Chuẩn hoá workflow (TDD, code review, security scan)
- Tối ưu token & context window
- Continuous learning (Claude học từ session của bạn)
- Security scanning (AgentShield)
- Cross-harness support (Claude Code, Codex, Cursor, OpenCode, Gemini)

**Con số:**
- 48 specialized subagents
- 185 skills
- 79 commands (legacy, đang migrate sang skills)
- Hoạt động trên 12+ language ecosystems
- 140K+ GitHub stars, 170+ contributors

### ECC vs setup tự làm / ECC vs DIY

| | DIY Claude Code | + ECC |
|--|-----------------|-------|
| Setup time | Hàng tuần (trial + error) | 2-3 giờ (install + configure) |
| Skills tái dùng | Tự viết từ đầu | 185 có sẵn (TDD, review, testing per ngôn ngữ) |
| Security | Tự research | AgentShield + 11-item minimum bar có sẵn |
| Subagents | Tự viết | 48 agents có sẵn (planner, code-reviewer, build-resolver per ngôn ngữ) |
| Continuous learning | Không có | Có (instinct-based v2 với confidence scoring) |
| Team sharing | Khó | Plugin share qua marketplace |

**Kết luận:** Team mới dùng Claude Code → **dùng ECC sẽ tiết kiệm hàng tuần**. Sau quen, có thể fork/customize.

---

## Part 2: 7 Building Blocks của Claude Code

> Đây là mental model core. Hiểu 7 block này là hiểu Claude Code.

### Tổng quan / Overview

| # | Block | Mục đích 1 câu | Khi nào dùng |
|---|-------|----------------|--------------|
| 1 | **Skills** | Reusable workflow definitions ("cách làm") | Workflow lặp lại (TDD, code review) |
| 2 | **Commands** (legacy) | Slash-entry shims để gõ `/plan`, `/tdd` | Backward compat; tương lai migrate sang skill |
| 3 | **Hooks** | Event automation (PreToolUse, Stop, …) | Format on save, block bad commits, audit |
| 4 | **Subagents** | Scoped child Claude processes | Delegate task tốn exploration / cần model khác |
| 5 | **Rules / Memory** | Always-follow standards + persistent context | Security checklist, coding style, team conventions |
| 6 | **MCPs** | External service bridges (DB, GitHub, …) | Tương tác service ngoài với typed interface |
| 7 | **Plugins** | Distribution mechanism cho 4 block khác | Share workflow cross-team |

> **Nguyên tắc vàng (từ tác giả ECC):** *"Skills are the primary workflow surface. The real durable unit is the underlying skill."*

### Cách 7 block phối hợp / How they work together

```
User request
    ↓
Rules + CLAUDE.md inject context nền (always-on)
    ↓
Main Claude nhận request
    ↓
Hook PreToolUse fire (validate)
    ↓
Main Claude decide:
  - Invoke Skill? (reusable workflow)
  - Delegate Subagent? (scope hẹp)
  - Call MCP tool? (external service)
  - User gõ Command shortcut?
    ↓
Execute action (với Rules áp dụng)
    ↓
Hook PostToolUse fire (format/audit)
    ↓
Response trả về
    ↓
Hook Stop fire (session summary, pattern extraction)
    ↓
[Plugins bundle all of the above for distribution]
```

### Deep dive cho mỗi block

Mỗi block có **entity page riêng trong wiki** với comparison table, anatomy, recipes, anti-patterns. Nếu cần đi sâu, đọc theo thứ tự đề xuất:

| # | Entity page | Ưu tiên cho người mới |
|---|-------------|------------------------|
| 1 | [[(C) Skills]] | ⭐⭐⭐ **Đọc đầu tiên** — primary workflow surface |
| 2 | [[(C) Hooks]] | ⭐⭐⭐ Học tuần 1 — automation đơn giản |
| 3 | [[(C) Subagents]] | ⭐⭐ Học tuần 2 — khi có task phức tạp |
| 4 | [[(C) Rules and Memory]] | ⭐⭐⭐ Setup đầu tiên (CLAUDE.md cho project) |
| 5 | [[(C) MCPs]] | ⭐⭐ Học tuần 3 — cẩn thận security |
| 6 | [[(C) Plugins]] | ⭐ Học tuần 4 — distribution mechanism |
| 7 | [[(C) Commands]] | ⭐ Legacy — chỉ đọc khi cần maintain code cũ |

---

## Part 3: Setup roadmap 4 tuần

> **Cam kết đầu ra:** sau 4 tuần, bạn có setup Claude Code + ECC đủ để làm việc production với team.

### ✅ Tuần 1 — Foundation (5-7 giờ)

**Mục tiêu:** Cài Claude Code + viết CLAUDE.md đầu tiên + quen với 5 keyboard shortcut.

**Todos:**

1. **Cài Claude Code** — theo docs chính thức: [code.claude.com/docs](https://code.claude.com)
2. **Mở terminal split screen** — terminal bên trái (Claude Code), editor bên phải (VSCode/Cursor/Zed)
3. **Tạo `~/.claude/CLAUDE.md`** với 5-7 rule cá nhân, ví dụ:
   ```markdown
   # My Claude Context

   ## Who I Am
   [Tên, role, stack chính]

   ## Coding Style
   - No console.log in production
   - Use TypeScript strict mode
   - Parameterized queries only (no string concat SQL)

   ## Workflow
   - Always write tests first (TDD)
   - Use conventional commits
   - Ask before editing files > 200 lines
   ```
4. **Học 5 keyboard shortcut:**
   - `Ctrl+U` — xoá cả dòng
   - `!` — prefix cho bash command
   - `@` — search file
   - `/` — slash command
   - `Esc Esc` — interrupt Claude
5. **Thử 3 command cơ bản:**
   - `/compact` — manual context compaction
   - `/rewind` — quay về state cũ
   - `/statusline` — customize status bar

**Kết thúc tuần 1:** bạn có CLAUDE.md cá nhân và quen CLI.

### ✅ Tuần 2 — Skills & Subagents (6-8 giờ)

**Mục tiêu:** Cài ECC + dùng 3 skills + hiểu 1 subagent.

**Todos:**

1. **Cài ECC:**
   ```bash
   git clone https://github.com/affaan-m/everything-claude-code.git
   cd everything-claude-code
   npm install
   ./install.sh --profile full
   ./install.sh typescript   # hoặc ngôn ngữ stack của bạn
   ```

   > ⚠️ **Lưu ý:** Plugin install riêng KHÔNG copy rules. Dùng `install.sh` để install cả components + rules.

2. **Thử 3 skills:**
   - `/tdd Add user authentication` → xem workflow TDD end-to-end
   - `/refactor-clean` → cleanup dead code
   - `/code-review` → review recent changes

3. **Đọc 1 subagent file** (chọn 1):
   - `agents/planner.md` (6.9KB, có worked example)
   - `agents/code-reviewer.md` (8.6KB, confidence-based filtering)
   - `agents/harness-optimizer.md` (928B, minimal format)

   → Hiểu format frontmatter: `name`, `description`, `tools`, `model`.

4. **Delegate 1 task cho subagent** — vd: "Use the planner agent to design the new feature X"

5. **Đọc entity page [[(C) Skills]]** — hiểu lộ trình primary workflow surface.

**Kết thúc tuần 2:** bạn đã invoke 3 skills thật + 1 subagent.

### ✅ Tuần 3 — Hooks & MCPs (6-8 giờ)

**Mục tiêu:** Tạo hook đầu tiên + kết nối 3 MCP + audit context window.

**Todos:**

1. **Cài plugin `hookify`:**
   ```
   /plugin marketplace add https://github.com/claude-plugins-official
   /plugin install hookify@claude-plugins-official
   ```

2. **Tạo hook đầu tiên qua conversation:**
   ```
   /hookify Tạo hook: mỗi khi edit file .ts, chạy prettier --write và tsc --noEmit
   ```

3. **Enable 3 MCPs minimal (safe default):**
   ```json
   // ~/.claude.json
   {
     "mcpServers": {
       "context7": { ... },        // live docs lookup
       "sequential-thinking": { ... },  // chain-of-thought
       "memory": { ... }           // persistent memory
     }
   }
   ```

4. **Audit context:**
   ```
   /mcp          # list MCPs enabled
   /plugins      # scroll to MCP section, disable unused
   ```

5. **Áp dụng rule "context discipline"** từ tác giả ECC:
   - 20-30 MCPs configured OK
   - **Enable <10 MCPs per session**
   - Tổng tool active <80

6. **Đọc entity pages [[(C) Hooks]] và [[(C) MCPs]]** — đặc biệt section **security** của MCPs.

**Kết thúc tuần 3:** bạn có hook automation đang chạy + 3 MCPs healthy.

### ✅ Tuần 4 — Parallel & Advanced (4-6 giờ)

**Mục tiêu:** Parallel workflow + security audit + beginning continuous learning.

**Todos:**

1. **Thử `/fork` cho 2 task không overlap:**
   - Main chat: code changes
   - Fork: research / questions about codebase

2. **Tạo 1 git worktree cho parallel work:**
   ```bash
   git worktree add ../project-feature-a feature-a
   cd ../project-feature-a && claude
   ```

3. **Chạy security audit:**
   ```bash
   npx ecc-agentshield scan
   ```
   Xem output — có CRITICAL issue nào không? Fix theo recommendation.

4. **Enable continuous learning v2:**
   ```bash
   # Thêm observation hooks vào settings.json
   # Xem skills/continuous-learning-v2/SKILL.md cho full setup
   ```
   Sau đó chạy `/instinct-status` sau vài session để xem Claude học gì.

5. **Đọc [[(C) Longform Guide summary]]** — token optimization, memory persistence, sequential phases.

6. **Đọc [[(C) Security Guide summary]]** — 11-item minimum bar.

**Kết thúc tuần 4:** bạn có workflow production-ready + security baseline.

---

## Part 4: Security minimum bar

> Đây là **bắt buộc** nếu run Claude Code autonomously. Từ 2 real CVE Feb 2026 (CVSS 8.7), agent security không còn là theoretical.

### 🚨 Trước khi bắt đầu — hiểu threat model

**Lethal Trifecta** (Simon Willison framing):

```
Private data + Untrusted content + External communication = prompt injection
                                                           → data exfiltration thật
```

Nếu agent có cả 3 trong runtime → compromise.

**Ví dụ:**
- Agent đọc PDF từ email (untrusted) + có SSH key (private) + có internet (external) = attack vector
- Agent review PR lạ (untrusted) + có GitHub token personal (private) + push code (external) = supply chain attack

### ✅ 11-item Minimum Bar Checklist

Copy vào task của bạn, tick từng cái:

- [ ] **1. Separate agent identities** — đừng cho agent dùng Gmail/Slack/GitHub cá nhân; tạo `agent@yourdomain.com`, bot user, bot GitHub account
- [ ] **2. Short-lived scoped credentials** — token hạn dưới 30 ngày, scope đúng đủ
- [ ] **3. Untrusted work trong containers / devcontainers / VMs / sandbox**
- [ ] **4. Deny outbound network by default** (container `internal: true`)
- [ ] **5. Restrict reads từ secret paths** (`.ssh`, `.aws`, `.env`)
- [ ] **6. Sanitize files / HTML / screenshots / linked content** trước khi privileged agent thấy
- [ ] **7. Require approval** cho unsandboxed shell, egress, deployment, off-repo writes
- [ ] **8. Log tool calls, approvals, network attempts** (structured log JSON)
- [ ] **9. Process-group kill + heartbeat dead-man switch** (khi chạy autonomous loop)
- [ ] **10. Keep persistent memory narrow + disposable** (rotate sau untrusted runs)
- [ ] **11. Scan skills / hooks / MCP configs / agent descriptors** như supply chain artifact (`npx ecc-agentshield scan`)

### Quick wins — làm ngay được trong 15 phút

1. **Thêm deny list** vào `~/.claude/settings.json`:
   ```json
   {
     "permissions": {
       "deny": [
         "Read(~/.ssh/**)",
         "Read(~/.aws/**)",
         "Read(**/.env*)",
         "Write(~/.ssh/**)",
         "Bash(curl * | bash)",
         "Bash(ssh *)"
       ]
     }
   }
   ```

2. **Run AgentShield scan:**
   ```bash
   npx ecc-agentshield scan
   ```

3. **Disable MCPs không dùng:**
   ```bash
   /plugins  # scroll to MCP section, toggle off
   ```

### Nguyên tắc vàng 1 câu

> **"Never let the convenience layer outrun the isolation layer."** — Affaan Mustafa

Nghĩa là: mỗi lần bạn thêm convenience (MCP mới, plugin mới, auto-approve), phải cân bằng bằng isolation (sandbox, permission deny, audit log).

### Nếu thấy vấn đề security

1. **STOP immediately** — đừng continue
2. Dùng `security-reviewer` agent: "Use security-reviewer agent to analyze this"
3. Fix CRITICAL issues trước khi continue
4. **Rotate exposed secrets** ngay
5. Review codebase cho similar issues

### Đọc thêm / Deep dive

- [[(C) Security Guide summary]] — full 6 defense layers + CVE details
- [AgentShield repo](https://github.com/affaan-m/agentshield) — scanner ECC
- [Anthropic: Defending against prompt injection](https://www.anthropic.com/news/prompt-injection-defenses)

---

## Part 5: FAQ thường gặp

### Q: Claude Code có free không?

Claude Code là **tool của Anthropic** — miễn phí để download. Nhưng dùng **tốn API credit** (call Claude API backend).

**Cost ballpark (từ tác giả ECC):**
- Coding session 2 giờ với Sonnet: ~$2-5
- Deep architecture task với Opus: ~$5-15
- Với subagent + skill đúng (Haiku cho exploration, Sonnet default): cost giảm đáng kể

**Optimize cost:**
- Default Sonnet cho 90% tasks (đủ tốt)
- Upgrade Opus chỉ khi first attempt fail / 5+ files / architectural / security-critical
- Dùng Haiku cho exploration (tìm file, simple edit)

### Q: ECC có thay thế được IDE như VSCode không?

**Không.** ECC là plugin cho Claude Code (CLI), không phải IDE. Dùng song song với editor:
- **Claude Code (CLI + ECC)** — agent execute tasks
- **Editor (VSCode/Cursor/Zed)** — bạn review/edit files, track changes

**Setup khuyến nghị:** split screen, terminal bên trái + editor bên phải, auto-save enabled.

### Q: Tôi đã dùng Cursor / Copilot. Chuyển sang Claude Code có đáng không?

**Tuỳ use case:**

| | Cursor / Copilot | Claude Code |
|--|-----------------|-------------|
| **Best for** | Inline suggestions, autocomplete | Autonomous tasks, multi-step workflow |
| **Style** | "Assistant" | "Agent" |
| **Ưu** | Ít setup, tích hợp editor | Customizable deeply, production workflow |
| **Nhược** | Ít control trên workflow | Cost tốn hơn, learning curve steeper |

**Lời khuyên:** dùng **cả hai** — Cursor/Copilot cho autocomplete nhanh, Claude Code + ECC cho tasks tốn reasoning (TDD, refactor lớn, code review).

### Q: Team tôi có 5 người, share setup ECC như thế nào?

**2 approach:**

**A. Shared plugin (recommended):**
1. Fork `everything-claude-code` thành team repo
2. Customize `plugin.json` theo stack team
3. Team install: `/plugin marketplace add <team-repo-url>`

**B. Shared dotfiles:**
1. Push `~/.claude/CLAUDE.md` + `rules/` vào team Git repo
2. Team sync qua script (stow, chezmoi, custom bash)

Personal overrides: dùng `.claude.json.local` (gitignored).

### Q: Multi-* commands (`/multi-plan`, `/multi-execute`) không chạy?

**Đúng** — cần runtime riêng:
```bash
npx ccg-workflow
```

Runtime này cài dependencies bên ngoài ECC. Warn này có trong README ECC nhưng dễ miss.

### Q: Tôi có nên custom CLAUDE.md per project không?

**Có**, nhưng chỉ **delta** (cái khác user-level), không repeat.

**Ví dụ project CLAUDE.md:**
```markdown
# Project: UserMarkets SaaS

> This extends ~/.claude/CLAUDE.md with project-specifics.

## Stack
- Next.js 14 App Router + TypeScript
- Supabase (PostgreSQL + Auth)
- Stripe for billing

## Conventions
- Tests trong `__tests__/` co-located với source
- Use Zod cho mọi API validation
- Tailwind cho styling, no CSS modules

## Key Files
- `src/lib/db.ts` — Supabase client
- `src/app/api/` — API routes
- `src/components/` — React components

## Gotchas
- Stripe webhook MUST verify signature (file: `src/app/api/webhooks/stripe/route.ts`)
- User email trong `public.users.email` NOT `auth.users.email`
```

### Q: Context window bị đầy thì sao?

**Triệu chứng:** Claude chậm dần, hay quên đầu session, response quality giảm.

**Fix ngắn hạn (trong session):**
1. `/compact` — trigger context compaction thủ công
2. `/clear` — xoá conversation (giữ CLAUDE.md, rules, skills)
3. Disable MCPs không dùng: `/plugins` → toggle off

**Fix dài hạn:**
1. Audit MCPs enabled: `/mcp` — tác giả dùng 14 configured, chỉ 5-6 enabled per project
2. Giảm `hooks.json` entries không cần
3. Move rules ít dùng sang skills (lazy-load)
4. Dùng dynamic system prompt thay vì nhồi vào CLAUDE.md:
   ```bash
   claude --system-prompt "$(cat ~/.claude/contexts/review.md)"
   ```

### Q: Tôi contribute gì về ECC repo được không?

**Có!** Storm Bear wiki đã identify 4 contribution opportunities (nếu bạn muốn ship):

1. **Fix `rules/README.md`** — README ghi 8 common files nhưng thực tế 10 (thiếu `code-review.md`, `development-workflow.md`)
2. **Vietnamese translation** — ECC có 6 ngôn ngữ khác (pt-BR, zh-CN, zh-TW, ja-JP, ko-KR, tr), **chưa có VI**
3. **Verify `mgrep` benchmark** — claim "~50% token reduction vs grep" chưa public reproducible
4. **Update `plugin.json agents array`** — manifest có 38 agents, filesystem có 48 → 10 agents mới chưa add vào manifest

Gửi PR theo format `CONTRIBUTING.md`.

---

## Part 6: Resources & References

### 📚 Wiki pages (deep dive)

#### Source summaries (trinity guides)
- [[(C) README summary]] — ECC overview, install, naming convention
- [[(C) Shortform Guide summary]] — 7 building blocks foundation
- [[(C) Longform Guide summary]] — token economics, memory, parallelization
- [[(C) Security Guide summary]] — 6 defense layers, CVE details, AgentShield

#### Entity pages (7 building blocks)
- [[(C) Skills]] — primary workflow surface, 185 skills categorized
- [[(C) Hooks]] — 6 types, memory persistence, recipes
- [[(C) Subagents]] — 48 agents, sub-agent context problem, iterative retrieval
- [[(C) Rules and Memory]] — 15 rule dirs, CLAUDE.md patterns
- [[(C) MCPs]] — 27 pre-configured, OWASP MCP Top 10
- [[(C) Plugins]] — manifest anatomy, validator quirks
- [[(C) Commands]] — 79 legacy commands, migration paths

#### Analysis notes
- [[(C) README - open questions]] — câu hỏi mở + câu trả lời

### 🔗 External resources

#### ECC ecosystem
- [GitHub repo](https://github.com/affaan-m/everything-claude-code) — source
- [ecc.tools](https://ecc.tools) — marketplace + dashboard
- [AgentShield](https://github.com/affaan-m/agentshield) — security scanner
- Tác giả: [@affaanmustafa](https://x.com/affaanmustafa)

#### Anthropic official
- [Claude Code docs](https://code.claude.com/docs/)
- [Anthropic Academy](https://anthropic.skilljar.com)
- [Prompt injection defenses](https://www.anthropic.com/news/prompt-injection-defenses)

#### Security references (từ Security Guide)
- [CVE-2025-59536](https://nvd.nist.gov/vuln/detail/CVE-2025-59536) — Claude Code hook pre-trust execution
- [CVE-2026-21852](https://nvd.nist.gov/vuln/detail/CVE-2026-21852) — ANTHROPIC_BASE_URL override
- [Check Point Research](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
- [Simon Willison prompt injection series](https://simonwillison.net/series/prompt-injection/)
- OWASP MCP Top 10 (living project)

#### Community
- [Longform guide by Affaan](https://x.com/affaanmustafa/status/2014040193557471352)
- [Shortform guide](https://x.com/affaanmustafa/status/2012378465664745795)
- [Security guide](https://x.com/affaanmustafa/status/2033263813387223421)

---

## 🚀 Bước tiếp theo / Next Steps

### Sau khi đọc guide này

1. **Start setup ngay** — Tuần 1 chỉ 5-7 giờ, đừng để delay
2. **Share với 1 teammate** — đọc cùng, hỏi đáp song song
3. **Tạo GitHub issue trong team repo** — track progress 4 tuần
4. **Feedback cho wiki này** — gì chưa rõ, gì thiếu, ping Storm Bear

### Sau 4 tuần

1. Contribute lại cho ECC — 4 opportunities đã list
2. Viết skill riêng cho team — dùng `/skill-create` hoặc continuous-learning v2
3. Share learnings — viết blog post / talk internal
4. Đi sâu vào 1 advanced topic: token optimization / parallelization / autonomous loops

### Câu hỏi? Bug? Đề xuất?

Ping Storm Bear hoặc tạo issue trong team repo. Wiki này là **living document** — sẽ update theo feedback + ECC releases mới.

---

> **Version log:**
> - v1 (2026-04-17): First release. Dựa trên ECC v1.10.0. Bao gồm 7 building blocks + security minimum bar + 4-week roadmap.
> - *v1.1 sẽ: add section "Real-world team setup case study"; update khi ECC 2.0 stable release*

---

**🤖 Generated by Storm Bear wiki (Claude as wiki maintainer) dựa trên `affaan-m/everything-claude-code` — LLM Wiki pattern.**
