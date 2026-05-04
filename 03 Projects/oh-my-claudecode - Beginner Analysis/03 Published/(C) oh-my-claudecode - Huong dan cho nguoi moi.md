# (C) oh-my-claudecode — Hướng dẫn cho người mới / Beginner's Guide

> **Project:** [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
> **Tagline:** *"Teams-first Multi-agent orchestration for Claude Code. Zero learning curve."*
> **Audience:** Claude Code user muốn multi-agent orchestration không phải học lệnh
> **Language:** Bilingual VN/EN
> **Complexity:** Medium — setup đơn giản, nhưng 8 modes + 19 agents + 15+ skills cần thời gian làm quen

---

## 1. OMC là gì? / What is OMC?

**VN:** oh-my-claudecode (viết tắt **OMC**) là framework multi-agent orchestration cho Claude Code, được tạo bởi **Yeachan Heo** (lập trình viên solo người Hàn Quốc). Mục tiêu: cho phép user sử dụng Claude Code với nhiều agents chuyên biệt phối hợp cùng nhau — mà không cần học lệnh mới. Slogan: *"Don't learn Claude Code. Just use OMC."* (Đừng học Claude Code. Chỉ cần dùng OMC.)

**EN:** oh-my-claudecode (OMC) is a multi-agent orchestration framework for Claude Code by **Yeachan Heo** (Korean solo developer). Goal: let users coordinate specialized agents without memorizing commands. Marketing angle: **7-language README** (en + ko + zh + ja + es + **vi** + pt) — ties fish-speech for broadest i18n in Storm Bear corpus.

**Key stats:**
- **30,366 GitHub stars** (3.5 months old — viral tier)
- **MIT license**
- **TypeScript**
- **npm:** `oh-my-claude-sisyphus@latest` (lưu ý: branding tên khác với npm package name)
- **Homepage:** oh-my-claudecode.dev
- **Discord:** discord.gg/PUwSMR9XNk

## 2. 8 orchestration modes (sân chơi chính)

| Mode | Mô tả | Khi nào dùng |
|------|-------|-------------|
| **Team (canonical)** | Pipeline 5-stage: plan → prd → exec → verify → fix | Work phối hợp nhiều agents trên task list chung |
| **omc team (CLI)** | tmux workers — spawn real `claude`/`codex`/`gemini`/`cursor-agent` processes | Codex/Gemini/Cursor CLI tasks |
| **CCG** | Tri-model synthesis (Codex + Gemini + Claude) | Backend + UI mixed work |
| **Autopilot** | Single agent thực hiện end-to-end | Feature nhỏ, ít nghi thức |
| **Ultrawork** | Max parallelism (không có team coordination) | Burst fixes / refactors |
| **Ralph** | Persistent verify/fix loops (bao gồm Ultrawork) | Task PHẢI hoàn thành — không được half-done |
| **Pipeline** | Sequential staged | Multi-step transformations đúng thứ tự |
| **Ultrapilot (legacy)** | Alias deprecated | Workflow cũ |

## 3. Cài đặt / Installation

### Bước 1: Install (Claude Code user — recommended)

**Marketplace-first (2 lệnh, nhập **từng lệnh một** — không paste cả 2):**

```bash
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
```

Sau đó:

```bash
/plugin install oh-my-claudecode
```

### Bước 2: Install (npm — nếu cần CLI tools)

```bash
npm i -g oh-my-claude-sisyphus@latest
```

⚠️ **Chú ý:** Package name là `oh-my-claude-sisyphus`, KHÔNG phải `oh-my-claudecode`. Đây là branding divergence document trong README.

### Bước 3: Setup

```bash
# Trong Claude Code / OMC session
/setup
/omc-setup

# Từ terminal
omc setup
```

### Bước 4: Thử chạy

```bash
# Trong session
/autopilot "build a REST API for managing tasks"

# Natural-language shortcut
autopilot: build a REST API for managing tasks
```

## 4. 19 Specialized Agents / Các agent chuyên biệt

OMC có 19 agents, mỗi agent mapped với AI model phù hợp (haiku/sonnet/opus):

| Agent | Model | Vai trò (VN) |
|-------|-------|-------------|
| explore | haiku | Tìm code nhanh, map symbols |
| analyst | opus | Làm rõ requirements, acceptance criteria |
| planner | opus | Lập kế hoạch task |
| architect | opus | Thiết kế kiến trúc hệ thống |
| debugger | sonnet | Chẩn đoán root cause |
| executor | sonnet | **Default** cho code changes |
| verifier | sonnet | Verify completion bằng evidence |
| tracer | sonnet | Evidence-driven tracing |
| security-reviewer | sonnet | Review bảo mật |
| code-reviewer | opus | Approval pass (KHÔNG tự approve) |
| test-engineer | sonnet | Chiến lược + code tests |
| designer | sonnet | UI/UX design |
| writer | haiku | Viết nội dung |
| qa-tester | sonnet | QA |
| scientist | sonnet | Experimental / ML |
| document-specialist | sonnet | Consult docs (Context Hub) |
| git-master | sonnet | Git operations |
| code-simplifier | opus | Refactor theo deletion-first |
| critic | opus | Critique độc lập |

**Smart model routing** tiết kiệm **30-50% tokens** (README claim).

## 5. Team Pipeline (workflow canonical)

```
team-plan → team-prd → team-exec → team-verify → team-fix (loop)
```

Example:
```bash
/team 3:executor "fix all TypeScript errors"
```

→ Spawn 3 executor agents đồng thời.

**Bật native teams** trong `~/.claude/settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

## 6. tmux CLI Workers (multi-runtime)

OMC có thể spawn real processes:

```bash
omc team 2:codex "review auth module for security issues"
omc team 2:gemini "redesign UI for accessibility"
omc team 1:claude "implement payment flow"
omc team status auth-review
omc team shutdown auth-review
```

**4 native runtimes supported:** Claude + Codex + Gemini + Cursor-agent (v4.13.1+).

**Platform tmux support:**
- macOS: `brew install tmux`
- Ubuntu: `sudo apt install tmux`
- **Windows native: psmux** — `winget install psmux` (không cần WSL!)

## 7. Skill learning + auto-inject

OMC có 2 scope for custom skills:

| | Project | User |
|---|---------|------|
| Path | `.omc/skills/` | `~/.omc/skills/` |
| Share | Team (versioned) | All your projects |
| Priority | Higher | Lower fallback |

**Auto-learn:** `/learner` tự extract patterns từ session.
**Auto-inject:** Skills phù hợp tự load vào context.

Example skill file:
```yaml
---
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
---
Wrap handler at server.py:42 in try/except ClientDisconnectedError...
```

**Manage:** `/skill list | add | remove | edit | search`

## 8. 5 Inspirational sources / 5 nguồn cảm hứng

Yeachan ghi rõ 5 nguồn ảnh hưởng (điều hiếm — hầu hết framework không ghi):

1. **oh-my-opencode** (code-yeongyu) — naming convention (Hàn Quốc)
2. **claude-hud** (ryanjoachim) — HUD statusline
3. **Superpowers** (obra / Jesse Vincent) — **Storm Bear v2 corpus**
4. **everything-claude-code** (affaan-m) — **Storm Bear v1 corpus**
5. **Ouroboros** (Q00) — persistent loops

⚠️ **ĐẶC BIỆT:** 2 trong 5 nguồn là corpus items của Storm Bear. Đây là **lần đầu Storm Bear corpus được cite bởi wiki subject**. Meta-validation: v1 + v2 đã được chọn đúng.

## 9. Lộ trình 4 tuần cho beginner / 4-week roadmap

### Tuần 1: Cài đặt + làm quen

- Install OMC via plugin marketplace (bước 1 + 2)
- Run `/setup` + `/omc-setup`
- Đọc README + CLAUDE.md + AGENTS.md
- Thử `/autopilot "simple task"` x 3 lần
- Enable native teams trong `~/.claude/settings.json`

### Tuần 2: Team mode + pipeline

- Thử `/team 2:executor "fix all linter warnings"`
- Quan sát pipeline `plan → prd → exec → verify → fix`
- Dùng `/deep-interview` cho requirements rõ ràng
- Setup HUD statusline
- Cài Codex CLI + Gemini CLI (optional)

### Tuần 3: Multi-runtime + CCG

- Cài tmux (macOS/Linux) hoặc psmux (Windows)
- Thử `omc team 2:codex "review this PR"`
- Thử `/ccg` cho architectural decisions
- Experiment với Ralph mode cho tasks phải hoàn thành

### Tuần 4: Custom skills + workflow mature

- Dùng `/learner` extract skills từ sessions
- Viết 1-2 custom skills in `.omc/skills/`
- Setup notification tags (Discord/Telegram/Slack)
- Setup OpenClaw integration (advanced)
- Sponsor nếu OMC giúp workflow (GitHub Sponsors)

## 10. Storm Bear use cases / Ứng dụng cho Storm Bear

**Storm Bear operator = Scrum coach + developer.** OMC áp dụng CAO:

### Scrum ceremony alignment

OMC Team pipeline map 1:1 với Scrum ceremonies:

| OMC stage | Scrum ceremony |
|-----------|----------------|
| team-plan | Sprint Planning |
| team-prd | Story Definition |
| team-exec | Sprint Execution |
| team-verify | Sprint Review |
| team-fix | Retrospective feedback |

### Cross-validation cho architecture

`/ccg` tri-model advisor (Codex + Gemini + Claude) = cross-check quyết định kiến trúc. Reduce "solo Claude blind spots."

### Scrum-coaching agent prototype

OMC + custom skills = foundation cho Vietnamese Scrum-coaching agent:
- `/learner` extract Scrum-specific patterns
- `.omc/skills/scrum-retrospective-facilitator.md` — custom skill
- `/deep-interview` = Socratic coaching pattern

## 11. Lưu ý quan trọng / Important notes

### ✅ Ưu điểm / Pros

- ✅ **Install dễ** qua Claude Code plugin marketplace
- ✅ **MIT license** — commercial use OK
- ✅ **Multi-runtime** — không bị lock-in Claude Code
- ✅ **7-language README** gồm tiếng Việt
- ✅ **Active development** — push daily (commits hôm nay!)
- ✅ **Zero open issues** — triage nhanh hoặc cộng đồng active
- ✅ **Scrum coaching alignment** — pipeline mirrors ceremony flow

### ⚠️ Điểm cần cân nhắc / Caveats

- ⚠️ **Solo author** — Yeachan Heo một mình lead; bus-factor cao
- ⚠️ **Korean-primacy** — governance Hàn Quốc; VN docs translated, không phải native design
- ⚠️ **Branding divergence** — `oh-my-claudecode` repo vs `oh-my-claude-sisyphus` npm (dễ confuse)
- ⚠️ **tmux required** cho CLI mode — thêm dep
- ⚠️ **Complex surface** — 8 modes + 19 agents + 15+ skills dù claim "zero learning curve"
- ⚠️ **Velocity sustainability unclear** — 289 stars/day 3.5 tháng có thể giảm
- ⚠️ **Codex/Gemini CLIs** cần cài thêm nếu dùng multi-runtime

### 🆚 So sánh với các T1 frameworks khác

| Framework | Focus | Stars | Archetype |
|-----------|-------|-------|-----------|
| spec-kit v17 | SDD corporate | 89.2K | Official-corporate (GitHub) |
| agency-agents v18 | 144 personality agents | 82.9K | Solo-community-viral |
| BMAD v11 | Methodology + 12 agents | 45K | Formalized-LLC |
| **OMC v27** | **8-mode multi-runtime** | **30.4K** | **Solo-Korean-multi-runtime** |
| codymaster v12 | VN 79 skills | 38 | Solo-VN |

**Verdict cho Storm Bear:** OMC ranking #2 trong pilot priority (sau spec-kit), vì:
1. Team-pipeline Scrum-ceremony alignment HIGH
2. Multi-runtime cross-validation cho architecture
3. MIT + plugin marketplace + Claude Code native = low friction
4. Caveats: solo bus-factor, Korean primacy

## 12. Next steps

1. ✅ Read through README + this guide
2. 🔲 Install OMC via plugin marketplace
3. 🔲 Run `/setup` + first `/autopilot` test
4. 🔲 Try `/team 2:executor "simple task"` to experience pipeline
5. 🔲 Join Discord: discord.gg/PUwSMR9XNk
6. 🔲 Sponsor Yeachan nếu thấy value: github.com/sponsors/Yeachan-Heo
7. 🔲 Consider Scrum-coaching skill extraction experiment (advanced)

## 13. References / Tham khảo

- [GitHub: Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
- [Homepage](https://oh-my-claudecode.dev)
- [Documentation](https://yeachan-heo.github.io/oh-my-claudecode-website)
- [CLI Reference](https://yeachan-heo.github.io/oh-my-claudecode-website/docs.html#cli-reference)
- [Discord](https://discord.gg/PUwSMR9XNk)
- [Sibling: oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
- [GitHub Sponsors](https://github.com/sponsors/Yeachan-Heo)

**Storm Bear wiki cross-refs:**
- [[(C) Team Mode 5-Stage Pipeline + 4-Runtime tmux Orchestration]]
- [[(C) Yeachan Heo Korean Solo Archetype + oh-my-codex Ecosystem-Layer]]
- [[(C) 5-Source Multi-Lineage + Recursive Corpus Reference + Pattern 57 Candidate]]
- [[(C) T1 Extends to N=9 + 5 New Candidates + Storm Bear]]

---

**OMC v27 = T1 framework #9 trong Storm Bear corpus. Tiếng Việt được hỗ trợ native trong README. Storm Bear operator pilot priority #2 (sau spec-kit). Test drive 1 tuần trước khi cam kết vào workflow.**
