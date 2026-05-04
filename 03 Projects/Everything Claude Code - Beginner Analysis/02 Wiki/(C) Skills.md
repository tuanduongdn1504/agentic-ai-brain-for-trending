# (C) Skills — Entity Page

> **Type:** Building block #1 (foundation) — "primary workflow surface" theo lời tác giả
> **Status:** Third entity page (format đã ổn định)
> **Sources:** 5 — README, shortform, longform, `tdd-workflow/SKILL.md`, `continuous-learning-v2/SKILL.md`
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** Skills là **workflow definitions tái dùng**, viết bằng markdown với YAML frontmatter — đóng gói "khi nào dùng + cách làm + ví dụ" thành 1 unit Claude có thể auto-load (theo description) hoặc user gọi tay (`/skill-name`). Đây là **đơn vị bền vững nhất** của Claude Code, ưu tiên hơn commands.

**EN:** Skills are **reusable workflow definitions** in markdown with YAML frontmatter — packaging "when to use + how to do + examples" into a unit Claude can auto-load (via description) or user invokes manually (`/skill-name`). They are the **durable unit** of Claude Code, prioritized over commands.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng skill khi:
- Workflow **lặp lại nhiều lần** với cùng pattern (TDD, code review, security audit)
- Cần **structure rõ** mà Claude phải follow (vd "viết test trước, run test, implement, refactor")
- Cần **share** workflow với team hoặc các project khác
- Cần **auto-load** dựa trên context (vd skill `python-patterns` auto fire khi edit `.py`)
- Cần **kết hợp** nhiều bước thành 1 invoke (vd `/tdd` = write tests → run → implement → verify)

### ❌ KHÔNG dùng skill khi:
- Logic chỉ là enforce/format, không cần reasoning → **hook**
- Một lần (one-off task) → chạy thẳng, không tạo skill
- Cần delegate task tốn nhiều exploration với scope/model riêng → **subagent**
- Workflow thay đổi mỗi lần → skill mất giá trị nếu không reusable

---

## Skill vs Hook vs Subagent vs Command (chọn cái nào?)

| Tiêu chí | Hook | **Skill** | Subagent | Command (legacy) |
|----------|------|-----------|----------|------------------|
| **Trigger** | Event tự động | User invoke `/skill` hoặc auto via description | Orchestrator delegate | User gõ `/cmd` |
| **Reasoning** | ❌ | ✅ Workflow + structure | ✅ Full Claude inference | ✅ Markdown prompt |
| **Latency** | <200ms | Trung bình | Chậm nhất | Trung bình |
| **Reusable cross-project** | Khó (config riêng) | ✅ Dễ (share folder) | ✅ Dễ | ✅ Dễ |
| **Cost** | ~0 token | Token main session | Token RIÊNG | Token main session |
| **Status trong ECC** | Stable | ✅ **Primary surface** | Stable | ⚠️ Legacy, đang migrate sang skill |
| **Use case** | Format on save, audit | Reusable workflow (TDD, review) | Delegate exploration | Slash-entry shim |

> **Quy tắc quyết định / Decision rule:**
> - Cần **enforce / automate** không reasoning → **Hook**
> - Cần **reusable workflow** với reasoning → **Skill** (ưu tiên cao nhất)
> - Cần **delegate task tốn context** → **Subagent**
> - Có command cũ (`/tdd`, `/plan`) → vẫn work, nhưng logic thực nằm trong skill underlying

---

## ECC ship 185 skills — phân loại / 185 skills categorized

> Số liệu verified bằng `ls -d skills/*/ | wc -l` (2026-04-17) = **185 skills**. README Quick Start ghi 183 (≈ chính xác). Changelog v1.10.0 ghi 156 (outdated).

### Theo domain / By domain

| Domain | Ví dụ |
|--------|-------|
| **Language patterns** | `python-patterns`, `golang-patterns`, `cpp-coding-standards`, `perl-patterns`, `swift-concurrency-6-2`, `compose-multiplatform-patterns`, `nestjs-patterns`, `pytorch-patterns` |
| **Framework / stack** | `django-patterns`, `laravel-patterns`, `springboot-patterns`, `nextjs-turbopack`, `bun-runtime`, `frontend-patterns`, `backend-patterns` |
| **Testing** | `tdd-workflow`, `e2e-testing`, `python-testing`, `golang-testing`, `cpp-testing`, `springboot-tdd`, `django-tdd`, `laravel-tdd`, `perl-testing` |
| **Security** | `security-review`, `security-scan`, `django-security`, `laravel-security`, `springboot-security`, `perl-security` |
| **Verification** | `verification-loop`, `eval-harness`, `agent-eval`, `django-verification`, `laravel-verification`, `springboot-verification` |
| **Workflow / meta** | `continuous-learning`, `continuous-learning-v2`, `iterative-retrieval`, `strategic-compact`, `autonomous-loops`, `search-first`, `skill-stocktake`, `configure-ecc` |
| **Code quality** | `coding-standards`, `code-tour`, `codebase-onboarding`, `architecture-decision-records`, `plankton-code-quality` |
| **Patterns specific** | `content-hash-cache-pattern`, `cost-aware-llm-pipeline`, `regex-vs-llm-structured-text`, `swift-actor-persistence`, `swift-protocol-di-testing` |
| **Infrastructure** | `database-migrations`, `api-design`, `docker-patterns`, `deployment-patterns`, `mcp-server-patterns` |
| **Business / content** | `article-writing`, `content-engine`, `market-research`, `investor-materials`, `investor-outreach`, `brand-voice` |
| **Operator** | `customer-billing-ops`, `connections-optimizer`, `google-workspace-ops`, `project-flow-ops`, `workspace-surface-audit`, `automation-audit-ops` |
| **Media** | `manim-video`, `remotion-video-creation`, `frontend-slides`, `videodb` |

> **Insight:** ECC đi từ "code quality core" (ban đầu) → expand sang business/operator/media (gần đây). Phù hợp với positioning "production-grade system" thay vì "code helper".

---

## Anatomy: Một skill trông như thế nào / What a skill looks like

### Single-file skill (đơn giản)

```markdown
---
name: tdd-workflow
description: Use this skill when writing new features, fixing bugs, or
             refactoring code. Enforces test-driven development with 80%+
             coverage including unit, integration, and E2E tests.
origin: ECC                    # optional: ECC | community | personal
---

# Test-Driven Development Workflow

[Intro 1-2 sentence]

## When to Activate
- Writing new features
- Fixing bugs
- Refactoring existing code
...

## Core Principles
### 1. Tests BEFORE Code
ALWAYS write tests first...

## Workflow Steps
### Step 1: ...
### Step 2: ...

## Examples
[concrete code examples]

## Best Practices
[checklist]
```

### Multi-file skill (phức tạp)

Khi skill cần code script, agent, hoặc hook đi kèm — folder structure:

```
continuous-learning-v2/
├── SKILL.md          ← Document chính (có frontmatter)
├── config.json       ← Config riêng cho skill
├── agents/           ← Subagent skill này invoke
├── hooks/            ← Hook script skill này cài
└── scripts/          ← Helper scripts (Python, Node)
```

### Frontmatter fields

| Field | Bắt buộc | Ý nghĩa |
|-------|----------|---------|
| `name` | ✅ | Định danh skill, lowercase + hyphen (`tdd-workflow`) |
| `description` | ✅ | **Quyết định khi Claude auto-load.** Cụm như "Use this skill when X" trigger mạnh. |
| `origin` | ❌ | `ECC` / `community` / `personal` — phân loại nguồn |
| `version` | ❌ | Semver, hữu ích khi skill có breaking changes (vd `continuous-learning-v2` v2.1.0) |

### Body sections convention (3 mục bắt buộc theo CONTRIBUTING.md ECC)

1. **When to Use / When to Activate** — điều kiện trigger
2. **How It Works / Workflow Steps** — pipeline cụ thể
3. **Examples** — concrete code/output examples

> Ngoài 3 mục trên, skill có thể thêm: Core Principles, Best Practices, Anti-patterns, Configuration, Commands, Related, v.v.

---

## Cơ chế / How It Works

```
User intent
    ↓
Claude detect trigger:
  - User gõ /skill-name             → explicit invoke
  - Description match context       → auto-load
  - Hook fire skill                 → triggered
    ↓
Skill SKILL.md được inject vào context
    ↓
Claude follow workflow trong skill body
    ↓
Nếu multi-file: skill có thể gọi script, spawn subagent, etc.
    ↓
Output trả về cùng conversation (khác subagent — không return summary riêng)
```

### Skill placement policy

| Location | Mục đích |
|----------|----------|
| `skills/` (trong repo) | **Curated** skills, ECC ship hoặc team-shared |
| `~/.claude/skills/` | **Generated** (auto-learned) hoặc **imported** từ user khác |

> Tách biệt để generated skill không pollute curated set. Xem `docs/SKILL-PLACEMENT-POLICY.md` trong repo.

---

## Configuration & Discovery

### Liệt kê skills enabled

```bash
/plugin list everything-claude-code@everything-claude-code
```

### Disable skill (nếu noise)

Skill không có env var như `ECC_HOOK_PROFILE`. Cách disable:
1. Xoá file SKILL.md khỏi `~/.claude/skills/`
2. Hoặc đổi `name` trong frontmatter (Claude không recognize nữa)
3. Hoặc edit description để Claude không auto-load (giữ lại để dùng explicit)

### Custom skill personal

Tạo file mới trong `~/.claude/skills/<your-skill>/SKILL.md` với frontmatter chuẩn — Claude tự pick up.

---

## Skill recipes (4 patterns đáng học)

### Recipe 1: Skill workflow đơn giản (single-file)

Áp dụng cho: đa số skill productivity (TDD, refactor, review).

```markdown
---
name: my-workflow
description: Use this skill when [trigger condition].
---

# My Workflow

## When to Activate
- [Condition 1]
- [Condition 2]

## Workflow Steps
1. [Step 1 với command cụ thể]
2. [Step 2]
3. [Verify step]

## Examples
[concrete example]
```

### Recipe 2: Skill + subagent (delegation)

Skill workflow gọi subagent cho task tốn exploration:

```markdown
## Workflow Steps
1. Đọc PRD
2. **Spawn `planner` subagent** để tạo implementation plan
3. Verify plan
4. **Spawn `tdd-guide` subagent** để execute plan
5. Review output
```

### Recipe 3: Skill + hook (auto-trigger)

Skill có hook config trong folder, install script setup hook → skill auto fire qua hook event:

```
my-skill/
├── SKILL.md
└── hooks/
    └── observe.sh    ← user thêm vào ~/.claude/settings.json hooks block
```

Ví dụ: `continuous-learning-v2` dùng pattern này — hooks `PreToolUse`/`PostToolUse` capture observations 100% reliable.

### Recipe 4: Skill với version migration

Skill có breaking change → bump version, cập nhật frontmatter:

```yaml
---
name: continuous-learning-v2
version: 2.1.0
description: ...v2.1 adds project-scoped instincts...
---
```

Trong body có "What's New in v2.1" + "Backward Compatibility" section. → User upgrade biết chính xác cái gì thay đổi.

---

## Patterns kết hợp / Combination patterns

### Skill + Subagent

Skill workflow cấp cao → subagent thực thi từng phase. Vd `/tdd` skill spawn `tdd-guide` agent trong step "implement".

### Skill + Hook

Hook trigger skill auto-execute. Vd `Stop` hook fire skill `continuous-learning` để extract pattern cuối session.

### Skill + Skill chaining

1 skill có thể gọi skill khác. Vd skill `feature-development` chain: `search-first` → `architecture-decision-records` → `tdd-workflow` → `code-review`.

### Skill + Plan Mode

Plan mode (Shift+Tab) tạo plan → `/clear` → execute với skill. Plan mode tận dụng skill `strategic-compact` để giữ context khoẻ.

### Skill + Continuous Learning v2

Pattern observed → instinct → cluster → **promote thành skill**. Skill mới sinh tự động, file vào `evolved/skills/`. → Self-improving system.

---

## Continuous Learning v2: case study đặc biệt (giải Q15)

> **Đây là skill đáng phân tích riêng vì nó là pattern "skill sinh ra skill".**

### v1 → v2 → v2.1 evolution

| Feature | v1 | v2 | v2.1 |
|---------|----|----|------|
| **Observation** | Stop hook (1× / session) | PreToolUse + PostToolUse (mỗi tool call, 100% reliable) | Same |
| **Analysis** | Main context (tốn token) | Background agent (Haiku, cheap) | Same |
| **Granularity** | Full skills | **Atomic instincts** | Same |
| **Confidence** | None | 0.3–0.9 weighted | Same |
| **Evolution path** | Direct skill | Instincts → cluster → skill/command/agent | Same |
| **Sharing** | None | Export/import instincts | Same |
| **Storage** | — | Global (`~/.claude/homunculus/`) | **Project-scoped + global** |
| **Cross-project contamination** | N/A | Risk | Isolated by default |

### Instinct — đơn vị atomic của learning

```yaml
---
id: prefer-functional-style
trigger: "when writing new functions"
confidence: 0.7              # 0.3 tentative → 0.9 near certain
domain: "code-style"
source: "session-observation"
scope: project               # project | global
project_id: "a1b2c3d4e5f6"
---

# Prefer Functional Style

## Action
Use functional patterns over classes when appropriate.

## Evidence
- Observed 5 instances of functional pattern preference
- User corrected class-based approach to functional on 2025-01-15
```

### Confidence dynamics

| Score | Meaning | Behavior |
|-------|---------|----------|
| 0.3 | Tentative | Suggested, không enforce |
| 0.5 | Moderate | Apply khi relevant |
| 0.7 | Strong | Auto-approved |
| 0.9 | Near-certain | Core behavior |

**Tăng confidence khi:** pattern lặp lại, user không correct, instinct khác agree.
**Giảm confidence khi:** user explicitly correct, không observed lâu, contradiction xuất hiện.

### Project-scoped vs global (v2.1 innovation)

| Pattern type | Scope | Lý do |
|--------------|-------|-------|
| Language/framework conventions | **project** | React patterns không nên áp cho Django project |
| Code style preferences | **project** | Mỗi codebase có style riêng |
| Security practices | **global** | Validate input đúng mọi project |
| Tool workflow (Grep before Edit) | **global** | Universal good habit |
| Git practices (conventional commits) | **global** | Universal |

### Auto-promotion: project → global

Instinct cùng ID xuất hiện ≥ 2 project + avg confidence ≥ 0.8 → auto-promote thành global.

### Vì sao Hook (không phải Skill) cho observation?

> "v1 dùng skill để observe. Skills là **probabilistic** — fire ~50–80% of the time tuỳ Claude judgment."

Hook fire **100% deterministic**. → Mọi tool call observed. Không miss pattern.

### 6 commands user-facing

```bash
/instinct-status      # Xem instincts đã học (project + global)
/evolve              # Cluster instincts thành skills/commands
/instinct-export     # Export instincts ra file
/instinct-import     # Import instincts từ user khác
/promote             # Promote project → global
/projects            # List projects + instinct counts
```

---

## Anti-patterns / Sai lầm hay gặp

1. **Skill description quá generic** — "Helps with code" → Claude không biết khi nào auto-load. Cụ thể: "Use this skill when writing TypeScript components with React hooks."
2. **Tạo skill cho one-off task** — overhead không justify. Chỉ tạo skill khi confident sẽ tái dùng ≥3 lần.
3. **Skill body chỉ có theory, không có command/example cụ thể** — Claude không biết execute thế nào. Mỗi step phải có command exact hoặc code example.
4. **Skill multi-file mà không có config.json** — khó maintain version. Multi-file skill nên có config riêng.
5. **Mix curated skill và generated skill cùng folder** — pollute curated set. Tuân theo placement policy: `skills/` cho curated, `~/.claude/skills/` cho generated.
6. **Skill không có "When to Activate"** — Claude phải đoán trigger condition. Section này là minimum required.
7. **Skill chain quá dài** (>5 skills nested) — debug khó, latency cao. Refactor thành 1 skill cấp cao gọi subagent thay vì chain.
8. **Skill description ngầm assumption** — vd "use when working with auth" mà không nói auth nào (OAuth? JWT? Session?). Cụ thể hoá.
9. **Quên `/evolve` trong continuous-learning v2** — instincts tích luỹ nhưng không promote thành skill → wasted observation. Nên `/evolve` định kỳ.
10. **Cài project-scoped instinct mà chạy ngoài git repo** — fallback về global, contaminate. Luôn chạy trong git context.

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| **`/skill-create`** command | Sinh skill từ git history (local analysis) |
| **`/skill-creator analyze`** (GitHub App) | Sinh skill từ repo history (advanced, 10k+ commits) |
| **`/instinct-*`** commands | Manage continuous-learning v2 instincts |
| **`/evolve`** | Cluster instincts → skill/command/agent |
| **`/skill-stocktake`** skill | Audit existing skills cho quality |
| **`docs/SKILL-PLACEMENT-POLICY.md`** | Convention curated vs generated |

---

## Cross-references

- [[(C) Hooks]] — alternative khi không cần reasoning; cũng là trigger mechanism cho skill
- [[(C) Subagents]] — alternative khi cần delegate; skill thường spawn subagent trong workflow
- [[(C) Shortform Guide summary]] — "Skills are the primary workflow surface" + setup mẫu
- [[(C) Longform Guide summary]] — continuous learning architecture (Stop-hook v1)
- [[(C) README summary]] — skill list 60+ trong "What's Inside" section
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) Commands]] khi entity page Commands tạo (skill > command, skill là durable unit)

## Citations

- `skills/tdd-workflow/SKILL.md` (lines 1–100, 12.8KB total) — single-file skill example với frontmatter, when to activate, principles, workflow steps
- `skills/continuous-learning-v2/SKILL.md` (full file, 12.3KB) — multi-file skill example + giải Q15 (instinct architecture, confidence scoring, project scoping, auto-promotion)
- `the-shortform-guide.md`, lines 13–34 — skills > commands, durable unit
- `the-longform-guide.md`, lines 89–102 — continuous learning Stop-hook v1
- `README.md`, lines 375–440 — skill list ~60 entries
- `00 Sources/everything-claude-code/CLAUDE.md` (auto-loaded) — skill format convention (When to Use / How It Works / Examples)
- Skills count verified: `ls -d skills/*/ | wc -l` = 185 (giải Q2 phần skills count)

---

## TODO cho lần ingest tiếp

- [ ] Đọc `docs/SKILL-PLACEMENT-POLICY.md` để verify "curated vs generated" convention
- [ ] Đọc `skills/iterative-retrieval/SKILL.md` để có entity page riêng cho pattern này (hiện đang nằm trong (C) Subagents)
- [ ] Đọc `skills/strategic-compact/SKILL.md` cho memory management
- [ ] Đọc `skills/agent-harness-construction/SKILL.md` — có vẻ meta-skill về build harness, đáng curiosity
- [ ] Đọc `skills/skill-stocktake/SKILL.md` — skill audit tool, có thể dùng để health-check Storm Bear vault sau này
- [ ] Verify với Anthropic docs xem skill có là khái niệm chính thức của Claude Code, hay đây là ECC convention extension
- [ ] Compare với "Anthropic Skills" được nhắc ở system available skills (anthropic-skills:*) — có cùng format không?
