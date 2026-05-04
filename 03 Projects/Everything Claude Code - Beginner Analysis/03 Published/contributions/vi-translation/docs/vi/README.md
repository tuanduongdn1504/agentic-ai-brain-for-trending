# Everything Claude Code

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![npm ecc-universal](https://img.shields.io/npm/dw/ecc-universal?label=ecc-universal%20lượt%20tải%20hàng%20tuần&logo=npm)](https://www.npmjs.com/package/ecc-universal)
[![npm ecc-agentshield](https://img.shields.io/npm/dw/ecc-agentshield?label=ecc-agentshield%20lượt%20tải%20hàng%20tuần&logo=npm)](https://www.npmjs.com/package/ecc-agentshield)
[![GitHub App Install](https://img.shields.io/badge/GitHub%20App-150%20cài%20đặt-2ea44f?logo=github)](https://github.com/marketplace/ecc-tools)
[![License](https://img.shields.io/badge/giấy%20phép-MIT-blue.svg)](../../LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Perl](https://img.shields.io/badge/-Perl-39457E?logo=perl&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **140K+ sao** | **21K+ fork** | **170+ người đóng góp** | **12+ hệ sinh thái ngôn ngữ** | **Anthropic Hackathon Winner**

---

<div align="center">

**Ngôn ngữ / Language / 语言 / 語言**

[English](../../README.md) | [Português (Brasil)](../pt-BR/README.md) | [简体中文](../../README.zh-CN.md) | [繁體中文](../zh-TW/README.md) | [日本語](../ja-JP/README.md) | [한국어](../ko-KR/README.md) | [Türkçe](../tr/README.md) | [**Tiếng Việt**](README.md)

</div>

---

**Hệ thống tối ưu hiệu năng cho AI agent harness. Từ người thắng giải Anthropic hackathon.**

Không chỉ là configs. Một hệ thống hoàn chỉnh: skills, instincts, memory optimization, continuous learning, security scanning, và research-first development. Agents, skills, hooks, rules, và MCP configurations ở mức production-ready, tiến hóa qua hơn 10 tháng sử dụng hằng ngày khi xây dựng sản phẩm thực.

Hoạt động trên **Claude Code**, **Codex**, **Cursor**, **OpenCode**, **Gemini**, và các AI agent harness khác.

---

## Các hướng dẫn

Repo này chỉ chứa code thô. Các hướng dẫn giải thích mọi thứ.

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="../../assets/images/guides/shorthand-guide.png" alt="The Shorthand Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="../../assets/images/guides/longform-guide.png" alt="The Longform Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="../../assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>Shorthand Guide</b><br/>Cài đặt, nền tảng, triết lý. <b>Đọc cái này trước.</b></td>
<td align="center"><b>Longform Guide</b><br/>Token optimization, memory persistence, evals, parallelization.</td>
<td align="center"><b>Security Guide</b><br/>Attack vectors, sandboxing, sanitization, CVEs, AgentShield.</td>
</tr>
</table>

| Chủ đề | Bạn sẽ học được |
|--------|-----------------|
| Token Optimization | Chọn model, cắt system prompt, background processes |
| Memory Persistence | Hooks tự động save/load context qua các session |
| Continuous Learning | Tự extract pattern từ session thành skills tái dùng |
| Verification Loops | Checkpoint vs continuous evals, grader types, metric pass@k |
| Parallelization | Git worktrees, cascade method, khi nào scale instances |
| Subagent Orchestration | Context problem, iterative retrieval pattern |

---

## Có gì mới

### v1.10.0 — Surface Refresh, Operator Workflows, và ECC 2.0 Alpha (Th4 2026)

- **Dashboard GUI** — Desktop app mới dùng Tkinter (`ecc_dashboard.py` hoặc `npm run dashboard`) với dark/light theme toggle, tuỳ chỉnh font, và logo project trong header + taskbar.
- **Public surface đồng bộ với live repo** — metadata, catalog counts, plugin manifests, và docs install hiện khớp với OSS surface thực tế.
- **Mở rộng operator & outbound workflow** — `brand-voice`, `social-graph-ranker`, `connections-optimizer`, `customer-billing-ops`, `ecc-tools-cost-audit`, `google-workspace-ops`, `project-flow-ops`, và `workspace-surface-audit` hoàn thiện mảng operator.
- **Media & launch tooling** — `manim-video`, `remotion-video-creation`, và social publishing surface nâng cấp đưa technical explainers và launch content vào cùng hệ thống.
- **Framework & product surface mở rộng** — `nestjs-patterns`, Codex/OpenCode install surfaces phong phú hơn, packaging cross-harness đầy đủ giúp repo dùng được ngoài Claude Code.
- **ECC 2.0 alpha đã có trong tree** — prototype Rust control-plane trong `ecc2/` build được local, expose các command `dashboard`, `start`, `sessions`, `status`, `stop`, `resume`, và `daemon`. Dùng được ở alpha level, chưa phải general release.
- **Ecosystem hardening** — AgentShield, ECC Tools cost controls, billing portal, và website refreshes tiếp tục ship quanh core plugin thay vì drift thành silos riêng.

### v1.9.0 — Selective Install & Language Expansion (Th3 2026)

- **Selective install architecture** — Manifest-driven install pipeline với `install-plan.js` và `install-apply.js` cho targeted component installation. State store track những gì đã install và cho phép incremental updates.
- **6 agents mới** — `typescript-reviewer`, `pytorch-build-resolver`, `java-build-resolver`, `java-reviewer`, `kotlin-reviewer`, `kotlin-build-resolver` mở rộng language coverage lên 10 ngôn ngữ.
- **Skills mới** — `pytorch-patterns` cho deep learning workflows, `documentation-lookup` cho API reference research, `bun-runtime` và `nextjs-turbopack` cho modern JS toolchains, cộng 8 operational domain skills và `mcp-server-patterns`.
- **Session & state infrastructure** — SQLite state store với query CLI, session adapters cho structured recording, skill evolution foundation cho self-improving skills.
- **Orchestration overhaul** — Harness audit scoring deterministic, orchestration status và launcher compatibility hardened, observer loop prevention với 5-layer guard.
- **12 language ecosystems** — Rules mới cho Java, PHP, Perl, Kotlin/Android/KMP, C++, và Rust gia nhập cùng TypeScript, Python, Go, và common rules hiện có.

### v1.8.0 — Harness Performance System (Th3 2026)

- **Harness-first release** — ECC giờ được framed rõ ràng là agent harness performance system, không chỉ là config pack.
- **Hook reliability overhaul** — SessionStart root fallback, Stop-phase session summaries, và script-based hooks thay thế inline one-liners dễ vỡ.
- **Hook runtime controls** — `ECC_HOOK_PROFILE=minimal|standard|strict` và `ECC_DISABLED_HOOKS=...` cho runtime gating mà không cần edit hook files.
- **Commands harness mới** — `/harness-audit`, `/loop-start`, `/loop-status`, `/quality-gate`, `/model-route`.
- **NanoClaw v2** — model routing, skill hot-load, session branch/search/export/compact/metrics.
- **Cross-harness parity** — behavior tightened across Claude Code, Cursor, OpenCode, và Codex app/CLI.
- **997 internal tests passing** — full suite green sau hook/runtime refactor và compatibility updates.

[Xem changelog đầy đủ trong Releases](https://github.com/affaan-m/everything-claude-code/releases).

---

## Quick Start

Bắt đầu trong dưới 2 phút:

### Bước 1: Cài Plugin

```bash
# Add marketplace
/plugin marketplace add https://github.com/affaan-m/everything-claude-code

# Install plugin
/plugin install everything-claude-code@everything-claude-code
```

### Bước 2: Cài Rules (Bắt buộc)

> **Quan trọng:** Claude Code plugins không thể distribute `rules` tự động. Cài thủ công:

```bash
# Clone repo trước
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code

# Cài dependencies (chọn package manager)
npm install        # hoặc: pnpm install | yarn install | bun install

# macOS/Linux
./install.sh --profile full               # Khuyến nghị: cài full profile
./install.sh typescript                   # Hoặc chỉ ngôn ngữ cụ thể
# ./install.sh typescript python golang swift php
# ./install.sh --target cursor typescript
# ./install.sh --target antigravity typescript
```

```powershell
# Windows PowerShell
.\install.ps1 --profile full               # Khuyến nghị
.\install.ps1 typescript                   # Hoặc ngôn ngữ cụ thể

# npm-installed compatibility entrypoint cũng chạy cross-platform
npx ecc-install typescript
```

Cho hướng dẫn cài thủ công chi tiết, xem README trong folder `rules/`. Khi copy rules thủ công, copy cả directory (vd `rules/common` hoặc `rules/golang`), không copy file bên trong riêng lẻ, để relative references không bị break.

### Bước 3: Bắt đầu dùng

```bash
# Plugin install dùng namespaced form
/ecc:plan "Thêm user authentication"

# Manual install giữ slash form ngắn hơn:
# /plan "Thêm user authentication"

# Kiểm tra commands khả dụng
/plugin list everything-claude-code@everything-claude-code
```

**Vậy là xong!** Bạn đã có truy cập 48 agents, 183 skills, và 79 legacy command shims.

---

## Hỗ trợ cross-platform

Plugin hiện hỗ trợ đầy đủ **Windows, macOS, và Linux**, đi cùng với tích hợp chặt chẽ với các IDE lớn (Cursor, OpenCode, Antigravity) và CLI harnesses. Tất cả hooks và scripts đã được viết lại bằng Node.js để tương thích tối đa.

### Package Manager Detection

Plugin tự động phát hiện package manager ưa thích (npm, pnpm, yarn, hoặc bun) theo thứ tự ưu tiên:

1. **Environment variable**: `CLAUDE_PACKAGE_MANAGER`
2. **Project config**: `.claude/package-manager.json`
3. **package.json**: field `packageManager`
4. **Lock file**: phát hiện từ package-lock.json, yarn.lock, pnpm-lock.yaml, hoặc bun.lockb
5. **Global config**: `~/.claude/package-manager.json`
6. **Fallback**: package manager đầu tiên available

Để set package manager ưa thích:

```bash
# Qua environment variable
export CLAUDE_PACKAGE_MANAGER=pnpm

# Qua global config
node scripts/setup-package-manager.js --global pnpm

# Qua project config
node scripts/setup-package-manager.js --project bun

# Phát hiện setting hiện tại
node scripts/setup-package-manager.js --detect
```

Hoặc dùng command `/setup-pm` trong Claude Code.

### Hook Runtime Controls

Dùng runtime flags để tune độ nghiêm ngặt hoặc disable specific hooks tạm thời:

```bash
# Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard

# Hook IDs cần disable (cách nhau dấu phẩy)
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
```

---

## Có gì bên trong

Repo này là **Claude Code plugin** — cài trực tiếp hoặc copy components thủ công.

```
everything-claude-code/
|-- .claude-plugin/   # Plugin và marketplace manifests
|   |-- plugin.json         # Plugin metadata và component paths
|   |-- marketplace.json    # Marketplace catalog cho /plugin marketplace add
|
|-- agents/           # 48 specialized subagents để delegate
|   |-- planner.md           # Feature implementation planning
|   |-- architect.md         # System design decisions
|   |-- tdd-guide.md         # Test-driven development
|   |-- code-reviewer.md     # Quality và security review
|   |-- security-reviewer.md # Vulnerability analysis
|   |-- build-error-resolver.md
|   |-- e2e-runner.md        # Playwright E2E testing
|   |-- refactor-cleaner.md  # Dead code cleanup
|   |-- doc-updater.md       # Documentation sync
|   |-- docs-lookup.md       # Documentation/API lookup
|   |-- chief-of-staff.md    # Communication triage
|   |-- loop-operator.md     # Autonomous loop execution
|   |-- harness-optimizer.md # Harness config tuning
|   |-- và nhiều hơn (per-language reviewer/build-resolver)...
|
|-- skills/           # Workflow definitions và domain knowledge
|   |-- coding-standards/           # Language best practices
|   |-- backend-patterns/           # API, database, caching patterns
|   |-- frontend-patterns/          # React, Next.js patterns
|   |-- security-review/            # Security checklist
|   |-- tdd-workflow/               # TDD methodology
|   |-- continuous-learning/        # Legacy v1 Stop-hook pattern extraction
|   |-- continuous-learning-v2/     # Instinct-based learning với confidence scoring
|   |-- iterative-retrieval/        # Progressive context refinement cho subagents
|   |-- strategic-compact/          # Manual compaction suggestions
|   |-- verification-loop/          # Continuous verification
|   |-- django-patterns/            # Django patterns
|   |-- golang-patterns/            # Go idioms và best practices
|   |-- và 100+ skills khác...
|
|-- commands/         # Legacy slash-entry shims; ưu tiên dùng skills/
|   |-- tdd.md              # /tdd - Test-driven development
|   |-- plan.md             # /plan - Implementation planning
|   |-- e2e.md              # /e2e - E2E test generation
|   |-- code-review.md      # /code-review - Quality review
|   |-- build-fix.md        # /build-fix - Fix build errors
|   |-- và 70+ commands khác...
|
|-- rules/            # Always-follow guidelines (copy vào ~/.claude/rules/)
|   |-- README.md            # Structure overview và installation guide
|   |-- common/              # Language-agnostic principles
|   |   |-- coding-style.md    # Immutability, file organization
|   |   |-- git-workflow.md    # Commit format, PR process
|   |   |-- testing.md         # TDD, 80% coverage requirement
|   |   |-- performance.md     # Model selection, context management
|   |   |-- patterns.md        # Design patterns, skeleton projects
|   |   |-- hooks.md           # Hook architecture
|   |   |-- agents.md          # Khi nào delegate subagents
|   |   |-- security.md        # Mandatory security checks
|   |-- typescript/          # TypeScript/JavaScript specific
|   |-- python/              # Python specific
|   |-- golang/              # Go specific
|   |-- swift/               # Swift specific
|   |-- php/                 # PHP specific
|
|-- hooks/            # Trigger-based automations
|   |-- hooks.json                # Config của tất cả hooks
|   |-- memory-persistence/       # Session lifecycle hooks
|   |-- strategic-compact/        # Compaction suggestions
|
|-- scripts/          # Cross-platform Node.js scripts
|   |-- lib/                     # Shared utilities
|   |-- hooks/                   # Hook implementations
|   |-- setup-package-manager.js # Interactive PM setup
|
|-- mcp-configs/      # MCP server configurations
|   |-- mcp-servers.json    # GitHub, Supabase, Vercel, Railway, ...
|
|-- ecc_dashboard.py  # Desktop GUI dashboard (Tkinter)
|
|-- assets/           # Assets cho dashboard
|-- marketplace.json  # Self-hosted marketplace config
```

---

## Nên dùng agent nào?

Chưa biết bắt đầu từ đâu? Dùng quick reference này:

| Tôi muốn làm... | Dùng command | Agent được dùng |
|------------------|--------------|-----------------|
| Plan một feature mới | `/ecc:plan "Thêm auth"` | planner |
| Thiết kế system architecture | `/ecc:plan` + architect agent | architect |
| Viết code với test trước | `/tdd` | tdd-guide |
| Review code vừa viết | `/code-review` | code-reviewer |
| Fix build lỗi | `/build-fix` | build-error-resolver |
| Chạy end-to-end tests | `/e2e` | e2e-runner |
| Tìm security vulnerabilities | `/security-scan` | security-reviewer |
| Xoá dead code | `/refactor-clean` | refactor-cleaner |
| Update documentation | `/update-docs` | doc-updater |
| Review Go code | `/go-review` | go-reviewer |
| Review Python code | `/python-review` | python-reviewer |
| Review TypeScript code | `/ts-review` | typescript-reviewer |

### Common workflows

**Bắt đầu feature mới:**
```
/ecc:plan "Thêm user authentication với OAuth"
                                              → planner tạo implementation plan
/tdd                                          → tdd-guide enforce write-tests-first
/code-review                                  → code-reviewer check công việc
```

**Fix bug:**
```
/tdd                                          → tdd-guide: viết failing test reproduce bug
                                              → apply fix, verify test passes
/code-review                                  → code-reviewer: catch regressions
```

**Chuẩn bị lên production:**
```
/security-scan                                → security-reviewer: audit OWASP Top 10
/e2e                                          → e2e-runner: test critical user flows
/test-coverage                                → verify ≥80% coverage
```

---

## FAQ

<details>
<summary><b>Làm sao check agents/commands nào đang được cài?</b></summary>

```bash
/plugin list everything-claude-code@everything-claude-code
```

Hiện tất cả agents, commands, và skills khả dụng từ plugin.
</details>

<details>
<summary><b>Hooks không chạy / lỗi "Duplicate hooks file"</b></summary>

Đây là vấn đề phổ biến nhất. **ĐỪNG** thêm field `"hooks"` vào `.claude-plugin/plugin.json`. Claude Code v2.1+ tự động load `hooks/hooks.json` từ plugins đã cài. Khai báo thủ công gây lỗi duplicate detection. Xem [#29](https://github.com/affaan-m/everything-claude-code/issues/29), [#52](https://github.com/affaan-m/everything-claude-code/issues/52), [#103](https://github.com/affaan-m/everything-claude-code/issues/103).
</details>

<details>
<summary><b>Context window của tôi bị thu hẹp / Claude hết context</b></summary>

Quá nhiều MCP servers đang ăn context. Mỗi tool description của MCP chiếm tokens từ 200k window, có thể co xuống ~70k.

**Fix:** Disable MCPs không dùng per-project:
```json
// Trong .claude/settings.json của project
{
  "disabledMcpServers": ["supabase", "railway", "vercel"]
}
```

Giữ <10 MCPs enabled và <80 tools active.
</details>

<details>
<summary><b>Tôi có thể chỉ dùng một số components (vd chỉ agents)?</b></summary>

Được. Dùng Option 2 (manual install) và chỉ copy những gì cần:

```bash
# Chỉ agents
cp everything-claude-code/agents/*.md ~/.claude/agents/

# Chỉ rules
cp -r everything-claude-code/rules/common/* ~/.claude/rules/
```

Mỗi component hoàn toàn độc lập.
</details>

<details>
<summary><b>Có hoạt động với Cursor / OpenCode / Codex / Antigravity không?</b></summary>

Có. ECC là cross-platform:
- **Cursor**: pre-translated configs trong `.cursor/`. Xem section [Cursor IDE Support](../../README.md#cursor-ide-support).
- **OpenCode**: full plugin support trong `.opencode/`. Xem section [OpenCode Support](../../README.md#opencode-support).
- **Codex**: first-class support cho macOS app và CLI. Xem PR [#257](https://github.com/affaan-m/everything-claude-code/pull/257).
- **Antigravity**: tight-integrated install cho workflows, skills, và flattened rules trong `.agent/`.
- **Claude Code**: Native — đây là primary target.
</details>

<details>
<summary><b>Làm sao contribute skill hoặc agent mới?</b></summary>

Xem [CONTRIBUTING.md](../../CONTRIBUTING.md). Phiên bản ngắn:
1. Fork repo
2. Tạo skill trong `skills/your-skill-name/SKILL.md` (với YAML frontmatter)
3. Hoặc tạo agent trong `agents/your-agent.md`
4. Submit PR với description rõ ràng: làm gì, khi nào dùng
</details>

<details>
<summary><b>Security — có gì cần biết không?</b></summary>

**Có — phải đọc Security Guide trước khi chạy autonomous.**

2 CVE thật đã được published Feb 2026 (CVSS 8.7) liên quan Claude Code project config. Đọc `the-security-guide.md` để biết:
- 6 defense layers (sandboxing, sanitization, approval boundaries, observability, kill switches, memory discipline)
- 11-item minimum bar checklist
- AgentShield scanner: `npx ecc-agentshield scan`

Quy tắc vàng 1 câu: *"Never let the convenience layer outrun the isolation layer."*
</details>

---

## Running Tests

Plugin đi kèm test suite đầy đủ:

```bash
# Chạy tất cả tests
node tests/run-all.js

# Chạy từng file test riêng
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```

---

## Contributing

**Đóng góp được mong đợi và khuyến khích.**

Repo này được xây dựng như một community resource. Nếu bạn có:
- Agents hoặc skills hữu ích
- Hooks thông minh
- MCP configurations tốt hơn
- Rules cải tiến

Vui lòng đóng góp! Xem [CONTRIBUTING.md](../../CONTRIBUTING.md) để biết hướng dẫn.

### Ý tưởng đóng góp

- Skills theo ngôn ngữ (Rust, C#, Kotlin, Java) — Go, Python, Perl, Swift, và TypeScript đã có
- Configs theo framework (Rails, FastAPI) — Django, NestJS, Spring Boot, và Laravel đã có
- DevOps agents (Kubernetes, Terraform, AWS, Docker)
- Chiến lược testing (framework khác nhau, visual regression)
- Domain-specific knowledge (ML, data engineering, mobile)

---

## License

MIT — Dùng thoải mái, modify theo nhu cầu, contribute lại nếu có thể.

---

**Nếu repo này hữu ích cho bạn, hãy star nó. Đọc cả hai guides. Làm điều gì đó tuyệt vời.**
