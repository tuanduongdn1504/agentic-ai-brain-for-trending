# open-design — Hướng dẫn cho người mới / Beginner's Guide / 入门指南

**Subject**: [`nexu-io/open-design`](https://github.com/nexu-io/open-design)
**Tagline (primary)**: *"An open, agent-native alternative to Claude Design / Figma"*
**License**: Apache-2.0 (with bundled-MIT components retained in-tree)
**Stars / Forks / Age**: 48,142 / 5,467 / 23 days (2026-05-21 fetch)

---

## 🇬🇧 English

### What is open-design?

`open-design` is the **open-source, local-first alternative to Anthropic's Claude Design** (released 2026-04-17, Opus 4.7). Where Claude Design is locked to Anthropic's model and Anthropic's skills, `open-design` lets you run the same artifact-first design loop with **any coding agent** (16 supported CLIs at v83 ship) and **any LLM provider** via BYOK ("Bring Your Own Key"). It's published by **nexu**, a 3-month-old indie org positioning itself as "the open-source stack for your AI coworker."

### What's in the box?

| Asset | Count |
|---|---|
| **Skills** (README claim) | 31 (27 prototype mode + 4 deck mode) |
| **Skills** (skills/ tree) | ~280+ subdirectories (sub-skills + variants + bundled third-party skills) |
| **Design systems** | 72 (2 hand-authored + 70 product systems: Anthropic, Apple, Cursor, Supabase, Figma, etc.) |
| **Visual directions** | 5 (Editorial Monocle + Modern Minimal + Tech Utility + Brutalist + Soft Warm) |
| **Media prompts** | 93 (43 image + 39 video Seedance + 11 HyperFrames) |
| **Supported coding agents** | 16 CLIs + BYOK proxy |
| **Locales** | 13 |

### The methodology (key claims)

- **"The prompt stack is the product"** — emphasis on composable layers
- **Junior + Senior designer dual-mode** — Junior workflow borrowed from `huashu-design`; Senior framing = "working filesystem + deterministic palette + checklist culture"
- **Anti-AI-slop machinery** — P0/P1/P2 gates (agent must pass P0 before emitting) + explicit forbidden-list ("invented metrics, generic emoji icons") + Honest-placeholders-over-fake-stats discipline
- **Five-dim critique**: Philosophy + Hierarchy + Detail + Function + Innovation
- **"We don't ship an agent. Yours is good enough"** — community-movement positioning

### How do I try it?

Four installation methods (pick one):

1. **Source install** (developers): `git clone` + `corepack enable` + `pnpm install` + `pnpm tools-dev run web` (needs Node 24 + pnpm 10.33.x)
2. **Docker**: `docker compose up -d` from the `deploy/` directory
3. **Desktop app**: Download prebuilt binary from `open-design.ai` or GitHub releases (Electron-packaged for macOS Apple Silicon, Intel x64, Windows x64; Linux AppImage in beta)
4. **Vercel-deploy**: Next.js-native cloud deploy if you want to host it yourself

### When should I use it?

✅ **Good fit**:
- You want artifact-first design output (HTML/CSS/SVG, not just Figma frames)
- You're already using a coding agent (Claude Code, Codex, Cursor, etc.) and want it to design too
- You don't want vendor lock-in (BYOK = use your own API keys at every layer)
- You have UI/branding/deck/media work in your next 30 days

❌ **Not a good fit**:
- You need pixel-perfect collaborative Figma replacement (this is agent-native, not designer-native)
- You don't have a coding agent in your workflow (one of the 16 is required)
- You expect a hosted SaaS — there's no paid tier; setup is on you (BYOK)

### Storm Bear verdict (vault-relevance check)

**STRONGEST INCLUDE 4/4** — methodology depth + 3-vector corpus-recursive citation (bundles taste-skill v81 + cites huashu-design v82 + alternative-to Anthropic Claude Design) + BYOK reduces tool-lock-in risk + Apache 2.0. **Conditional Tier-1 vault pilot** if Storm Bear has UI/design work planned in next 30-day window; if not, defer to taste-skill v81 (lighter footprint) first.

---

## 🇻🇳 Tiếng Việt

### `open-design` là gì?

`open-design` là **giải pháp thay thế mã nguồn mở, ưu tiên local cho Anthropic's Claude Design** (ra mắt 2026-04-17 với Opus 4.7). Trong khi Claude Design bị khóa vào model + skills của Anthropic, `open-design` cho phép bạn chạy cùng một vòng lặp design ưu tiên artifact với **bất kỳ coding agent nào** (16 CLI được hỗ trợ tại thời điểm v83) và **bất kỳ LLM provider nào** thông qua BYOK ("Bring Your Own Key" — mang khóa API của bạn). Sản phẩm do **nexu** phát hành — một org indie 3-tháng tuổi tự định vị là "open-source stack cho AI coworker của bạn."

### Có gì trong hộp?

| Asset | Số lượng |
|---|---|
| **Skills** (README claim) | 31 (27 prototype mode + 4 deck mode) |
| **Skills** (cây `skills/`) | ~280+ thư mục con (sub-skills + variants + bundled third-party skills) |
| **Design systems** | 72 (2 tự viết + 70 product systems: Anthropic, Apple, Cursor, Supabase, Figma, v.v.) |
| **Visual directions** | 5 (Editorial Monocle + Modern Minimal + Tech Utility + Brutalist + Soft Warm) |
| **Media prompts** | 93 (43 image + 39 video Seedance + 11 HyperFrames) |
| **Coding agents hỗ trợ** | 16 CLI + BYOK proxy |
| **Locales** | 13 (bao gồm English + 简体中文 + 日本語 + العربية + Türkçe + ... nhưng KHÔNG có tiếng Việt tại thời điểm v83 ship) |

### Methodology (các tuyên bố chính)

- **"The prompt stack is the product"** — nhấn mạnh vào composable layers
- **Junior + Senior designer dual-mode** — Junior workflow vay mượn từ `huashu-design`; Senior framing = "working filesystem + deterministic palette + checklist culture"
- **Anti-AI-slop machinery** — P0/P1/P2 gates (agent phải pass P0 trước khi emit) + danh sách forbidden tường minh ("invented metrics, generic emoji icons") + nguyên tắc Honest-placeholders-over-fake-stats
- **Five-dim critique**: Philosophy + Hierarchy + Detail + Function + Innovation
- **"We don't ship an agent. Yours is good enough"** — định vị community-movement

### Làm sao để thử?

Bốn phương pháp cài đặt (chọn một):

1. **Source install** (dev): `git clone` + `corepack enable` + `pnpm install` + `pnpm tools-dev run web` (cần Node 24 + pnpm 10.33.x)
2. **Docker**: `docker compose up -d` từ thư mục `deploy/`
3. **Desktop app**: Tải bản dựng sẵn từ `open-design.ai` hoặc GitHub releases (Electron — macOS Apple Silicon + Intel x64, Windows x64; Linux AppImage đang beta)
4. **Vercel-deploy**: Triển khai cloud bằng Next.js nếu bạn muốn tự host

### Khi nào nên dùng?

✅ **Phù hợp**:
- Bạn muốn output design ưu tiên artifact (HTML/CSS/SVG, không chỉ Figma frame)
- Bạn đã dùng coding agent (Claude Code, Codex, Cursor, v.v.) và muốn nó cũng design được
- Bạn không muốn lock-in vendor (BYOK = dùng API key của bạn ở mọi layer)
- Bạn có công việc UI/branding/deck/media trong 30 ngày tới

❌ **Không phù hợp**:
- Bạn cần Figma thay thế hoàn hảo pixel cho làm việc nhóm (cái này là agent-native, không phải designer-native)
- Bạn không có coding agent trong workflow (cần ít nhất 1 trong 16)
- Bạn mong đợi SaaS có host sẵn — không có paid tier; setup do bạn lo (BYOK)

### Storm Bear verdict (kiểm tra liên quan đến vault)

**STRONGEST INCLUDE 4/4** — chiều sâu methodology + 3-vector corpus-recursive citation (bundle taste-skill v81 + cite huashu-design v82 + alternative-to Anthropic Claude Design) + BYOK giảm risk tool-lock-in + Apache 2.0. **Tier-1 vault pilot có điều kiện** nếu Storm Bear có công việc UI/design dự kiến trong cửa sổ 30-ngày; nếu không, ưu tiên thử taste-skill v81 trước (footprint nhẹ hơn).

---

## 🇨🇳 中文

### `open-design` 是什么？

`open-design` 是 **Anthropic 的 Claude Design 的开源、本地优先的替代品**（Claude Design 于 2026-04-17 随 Opus 4.7 发布）。Claude Design 被锁定在 Anthropic 的模型和 skills 内，而 `open-design` 允许你用**任意 coding agent**（v83 时支持 16 个 CLI）和通过 BYOK（"Bring Your Own Key"，自带密钥）使用**任意 LLM 提供商**来运行相同的 artifact-first 设计循环。它由 **nexu** 发布，一个 3 个月大的 indie 组织，自我定位为"为你的 AI coworker 提供开源 stack"。

### 包内有什么？

| 资产 | 数量 |
|---|---|
| **Skills** (README 声明) | 31（27 prototype mode + 4 deck mode）|
| **Skills**（`skills/` 树）| ~280+ 子目录（sub-skills + variants + 捆绑的第三方 skills）|
| **Design systems** | 72（2 个手写 + 70 个产品系统：Anthropic、Apple、Cursor、Supabase、Figma 等）|
| **Visual directions** | 5（Editorial Monocle + Modern Minimal + Tech Utility + Brutalist + Soft Warm）|
| **Media prompts** | 93（43 image + 39 video Seedance + 11 HyperFrames）|
| **支持的 coding agents** | 16 个 CLI + BYOK 代理 |
| **语言** | 13（包括简体中文 + 繁體中文 + 日本語 + 한국어 等）|

### Methodology（核心主张）

- **"The prompt stack is the product"** — 强调可组合的 layers
- **Junior + Senior 设计师双模式** — Junior workflow 借鉴自 `huashu-design`；Senior framing = "working filesystem + deterministic palette + checklist culture"
- **Anti-AI-slop machinery** — P0/P1/P2 gates（agent 必须通过 P0 才能 emit）+ 显式的 forbidden 列表（"invented metrics, generic emoji icons"）+ Honest-placeholders-over-fake-stats 纪律
- **Five-dim critique**：Philosophy + Hierarchy + Detail + Function + Innovation
- **"We don't ship an agent. Yours is good enough"** — community-movement 定位

### 如何试用？

四种安装方式（任选一种）：

1. **Source install**（开发者）：`git clone` + `corepack enable` + `pnpm install` + `pnpm tools-dev run web`（需要 Node 24 + pnpm 10.33.x）
2. **Docker**：在 `deploy/` 目录运行 `docker compose up -d`
3. **Desktop app**：从 `open-design.ai` 或 GitHub releases 下载预构建二进制（Electron 打包：macOS Apple Silicon + Intel x64，Windows x64；Linux AppImage 测试中）
4. **Vercel-deploy**：使用 Next.js 部署到 cloud 自托管

### 什么时候用？

✅ **合适场景**：
- 你想要 artifact-first 设计输出（HTML/CSS/SVG，不只是 Figma frame）
- 你已经在用 coding agent（Claude Code、Codex、Cursor 等）并希望它也能做设计
- 你不想被 vendor lock-in（BYOK = 在每一层都用你自己的 API key）
- 你在未来 30 天有 UI/branding/deck/media 工作

❌ **不合适场景**：
- 你需要像素级完美的协作 Figma 替代品（这个是 agent-native，不是 designer-native）
- 你工作流中没有 coding agent（16 个里至少需要 1 个）
- 你期待托管 SaaS — 没有 paid tier；setup 需要你自己搞（BYOK）

### Storm Bear 评定（vault 相关性检查）

**STRONGEST INCLUDE 4/4** — methodology 深度 + 3-vector corpus-recursive citation（捆绑 taste-skill v81 + 引用 huashu-design v82 + alternative-to Anthropic Claude Design）+ BYOK 降低 tool-lock-in 风险 + Apache 2.0。**条件性 Tier-1 vault pilot**，前提是 Storm Bear 在 30 天窗口内有 UI/设计工作；如果没有，建议先试 taste-skill v81（footprint 更轻）。

---

## Sources

- Repository: <https://github.com/nexu-io/open-design>
- Product domain: <https://open-design.ai>
- Org domain: <https://nexu.io>
- README + GitHub API + skills/ tree fetched 2026-05-21

## Wiki cross-references

- Cluster 1: README positioning + Anti-AI-slop machinery + corpus-recursive citation lineage
- Cluster 2: 31-skill bundle + ~280-tree + corpus-recursive bundling
- Cluster 3: Distribution + 16-harness CORPUS-RECORD + BYOK + nexu org
- Entity 1: Core product (31-skill bundle with machinery)
- Entity 2: Distribution + 16-harness + BYOK
- Entity 3: Anti-Slop-Design-Curation observation track N=3 PROMOTION-LOCKED-IN
- Entity 4: Storm Bear meta + consolidated Pattern Library implications

🤖 Generated by Claude under routine `llm-wiki-routine-v2.2` (NINETEENTH execution).
