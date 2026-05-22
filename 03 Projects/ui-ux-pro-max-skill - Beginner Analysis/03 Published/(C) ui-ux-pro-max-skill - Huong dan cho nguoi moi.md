# ui-ux-pro-max-skill — Hướng dẫn cho người mới / Beginner's Guide / 入门指南

**Subject**: [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
**Tagline**: *"An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms"*
**Owner**: nextlevelbuilder (Vietnam-located organization; `nextlevelbuilder.io`)
**Product domain**: `https://www.uupm.cc/`
**License**: MIT
**Stars / Forks / Age**: 81,352 / 8,375 / 174 days (Phase 0 fetch 2026-05-22)
**Velocity class**: Pattern #52 Multi-Month-Sustained EXTREME-VIRAL (~467/d × 174d) — **N=2 PROMOTION** evidence

---

## 🇬🇧 English

### What is ui-ux-pro-max-skill?

`ui-ux-pro-max-skill` is an **AI-powered design intelligence Claude skill** by Vietnamese organization **nextlevelbuilder**. It packages **669+ codified design-system elements** — 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, 99 UX guidelines, 161 reasoning rules, 13 stack templates — into an installable skill that works across **18 AI coding agents** (Claude, Cursor, Windsurf, Copilot, Kiro, Codex, Gemini, Trae, OpenCode + 9 more) via a single `npx uipro-cli init --ai {{platform}}` command.

The flagship feature is the **Design System Generator** — a 5-parallel-domain reasoning engine that takes your project requirements and outputs a complete design system (patterns + styles + colors + typography + effects + anti-patterns + checklists) in seconds.

### How does it work?

1. **Codified database**: CSV files in `src/ui-ux-pro-max/data/` contain canonical design knowledge (products, styles, colors, typography, charts, UX rules)
2. **Search engine**: BM25 + regex hybrid `scripts/core.py` (Python stdlib only, no external deps) ranks relevant entries
3. **Multi-domain reasoning**: 5 parallel search domains (product / style / typography / color / ux) feed into reasoning engine
4. **Stack-specific output**: 13 stack templates (`html-tailwind` default + React + Next + Vue + Nuxt + Svelte + SwiftUI + Flutter + React Native + Shadcn + Jetpack Compose + others) render results in your preferred framework
5. **Multi-symlink architecture**: `.claude/skills/` + `.factory/skills/` + `.shared/` symlinks → `src/ui-ux-pro-max/` single source of truth

### Install + use

```bash
# Global install via npm
npm install -g uipro-cli
uipro init --ai claude

# OR per-platform via npx (no install)
npx uipro-cli init --ai claude
npx uipro-cli init --ai cursor
npx uipro-cli init --ai windsurf
# ... 18 platform variants
```

### When should I use it?

✅ **Good fit**:
- You build UI/UX with a Claude-compatible AI agent (one of 18 supported platforms)
- You want a substantial design-system library at hand for SaaS / dashboard / portfolio / landing-page / mobile UI work
- You appreciate codified design intelligence (not just LLM-improvised CSS)
- You're comfortable with BM25-search-CLI workflow

❌ **Not a good fit**:
- You want a finished design (this is generation-assistance, not a polished deliverable)
- You don't use Claude Code or any of the 18 supported AI agents
- You want Figma-replacement (this is agent-native, not designer-native)

### Storm Bear verdict

**STRONGEST 4/4 INCLUDE** — clean Phase 0.9 PASS (post-v84 OVERRIDE; routine discipline restored). VN-located org = **direct cultural-peer to Storm Bear**. 669+ codified design elements + 18-platform install + `npx uipro-cli init --ai claude` one-command = **HIGH-RELEVANCE Tier-1 vault pilot CONDITIONAL IF UI work in 30-day window**. Pilot ranking position #5 (above v83 open-design at #6).

---

## 🇻🇳 Tiếng Việt

### `ui-ux-pro-max-skill` là gì?

`ui-ux-pro-max-skill` là **Claude skill design intelligence được hỗ trợ bởi AI** do tổ chức Việt Nam **nextlevelbuilder** phát triển. Nó đóng gói **669+ codified design-system elements** — 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, 99 UX guidelines, 161 reasoning rules, 13 stack templates — thành skill cài đặt được hoạt động trên **18 AI coding agents** (Claude, Cursor, Windsurf, Copilot, Kiro, Codex, Gemini, Trae, OpenCode + 9 cái khác) qua một lệnh duy nhất `npx uipro-cli init --ai {{platform}}`.

Flagship feature là **Design System Generator** — engine reasoning 5-parallel-domain nhận project requirements của bạn và output một complete design system (patterns + styles + colors + typography + effects + anti-patterns + checklists) trong vài giây.

### Hoạt động thế nào?

1. **Codified database**: CSV files trong `src/ui-ux-pro-max/data/` chứa kiến thức design canonical (products, styles, colors, typography, charts, UX rules)
2. **Search engine**: BM25 + regex hybrid `scripts/core.py` (chỉ Python stdlib, không external deps) xếp hạng entries liên quan
3. **Multi-domain reasoning**: 5 parallel search domains (product / style / typography / color / ux) feed vào reasoning engine
4. **Stack-specific output**: 13 stack templates render kết quả trong framework bạn chọn
5. **Multi-symlink architecture**: `.claude/skills/` + `.factory/skills/` + `.shared/` symlinks → `src/ui-ux-pro-max/` single source of truth

### Cài + dùng

```bash
# Global install qua npm
npm install -g uipro-cli
uipro init --ai claude

# HOẶC per-platform qua npx (không cần install)
npx uipro-cli init --ai claude
npx uipro-cli init --ai cursor
# ... 18 platform variants
```

### Khi nào nên dùng?

✅ **Phù hợp**:
- Bạn build UI/UX với Claude-compatible AI agent (1 trong 18 platform)
- Bạn muốn library design-system substantial cho SaaS / dashboard / portfolio / landing-page / mobile UI
- Bạn appreciate codified design intelligence (không chỉ LLM-improvised CSS)
- Bạn thoải mái với workflow BM25-search-CLI

❌ **Không phù hợp**:
- Bạn muốn finished design (đây là generation-assistance, không phải polished deliverable)
- Bạn không dùng Claude Code hoặc 1 trong 18 AI agent được hỗ trợ
- Bạn muốn Figma-replacement (đây là agent-native, không phải designer-native)

### Storm Bear verdict

**STRONGEST 4/4 INCLUDE** — clean Phase 0.9 PASS (post-v84 OVERRIDE; routine discipline được restore). VN-located org = **direct cultural-peer cho Storm Bear**. 669+ codified design elements + 18-platform install + `npx uipro-cli init --ai claude` one-command = **HIGH-RELEVANCE Tier-1 vault pilot CONDITIONAL NẾU có UI work trong 30-day window**. Pilot ranking position #5 (trên v83 open-design ở #6) — direct cultural-peer-org-bias multiplier + lower-cost-of-trial.

---

## 🇨🇳 中文

### `ui-ux-pro-max-skill` 是什么？

`ui-ux-pro-max-skill` 是越南组织 **nextlevelbuilder** 开发的 **AI 驱动的设计智能 Claude skill**。它将 **669+ codified design-system elements** — 67 个 UI styles、161 个 color palettes、57 个 font pairings、25 个 chart types、99 个 UX guidelines、161 个 reasoning rules、13 个 stack templates — 打包成可安装的 skill，通过单个 `npx uipro-cli init --ai {{platform}}` 命令在 **18 个 AI coding agents** 上工作（Claude、Cursor、Windsurf、Copilot、Kiro、Codex、Gemini、Trae、OpenCode + 9 个其他）。

旗舰功能是 **Design System Generator** — 一个 5-parallel-domain reasoning engine，接收你的 project requirements 并在几秒钟内输出完整的 design system（patterns + styles + colors + typography + effects + anti-patterns + checklists）。

### 工作原理？

1. **Codified database**：`src/ui-ux-pro-max/data/` 中的 CSV 文件包含规范的设计知识
2. **Search engine**：BM25 + regex 混合 `scripts/core.py`（仅 Python stdlib，无外部依赖）对相关条目进行排名
3. **Multi-domain reasoning**：5 个并行搜索域（product / style / typography / color / ux）输入到 reasoning engine
4. **Stack-specific output**：13 个 stack templates 在你选择的框架中渲染结果
5. **Multi-symlink architecture**：`.claude/skills/` + `.factory/skills/` + `.shared/` symlinks → `src/ui-ux-pro-max/` 单一可信源

### 安装 + 使用

```bash
# 通过 npm 全局安装
npm install -g uipro-cli
uipro init --ai claude

# 或通过 npx per-platform（无需安装）
npx uipro-cli init --ai claude
npx uipro-cli init --ai cursor
# ... 18 个 platform variants
```

### 何时使用？

✅ **合适场景**：
- 你使用 Claude 兼容的 AI agent（18 个平台之一）构建 UI/UX
- 你想要为 SaaS / dashboard / portfolio / landing-page / mobile UI 工作准备的大量设计系统库
- 你欣赏 codified design intelligence（不只是 LLM-improvised CSS）
- 你熟悉 BM25-search-CLI 工作流

❌ **不合适场景**：
- 你想要 finished design（这是 generation-assistance，不是 polished deliverable）
- 你不使用 Claude Code 或 18 个支持的 AI agent 中的任何一个
- 你想要 Figma-replacement（这是 agent-native，不是 designer-native）

### Storm Bear 评定

**STRONGEST 4/4 INCLUDE** — clean Phase 0.9 PASS（post-v84 OVERRIDE; routine discipline 已恢复）。VN-located org = Storm Bear 的**直接 cultural-peer**。669+ codified design elements + 18-platform install + `npx uipro-cli init --ai claude` one-command = **HIGH-RELEVANCE Tier-1 vault pilot 条件性（如果 30 天窗口内有 UI 工作）**。Pilot 排名 position #5（高于 v83 open-design 的 #6）— direct cultural-peer-org-bias multiplier + 较低的试用成本。

---

## Sources

- Repository: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill>
- Product domain: <https://www.uupm.cc/>
- Org domain: <https://nextlevelbuilder.io>
- README + CLAUDE.md + skill.json fetched 2026-05-22

🤖 Generated by Claude under routine `llm-wiki-routine-v2.2` (TWENTY-FIRST execution; FIRST under restored Phase 0.9 STRICT post-v84 OVERRIDE; v85 = clean PASS 4/4 STRONGEST).
