# (C) Commands (Legacy) — Entity Page

> **Type:** Building block #2 (foundation) — **LEGACY, đang migrate sang Skills**
> **Status:** Seventh entity page — **FOUNDATION 7/7 COMPLETE** ✅
> **Sources:** 5 — README, shortform, `commands/plan.md`, `commands/learn.md`, plus cross-ref với [[(C) Skills]]
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** Commands là **slash-entry shims** (vd `/tdd`, `/plan`, `/code-review`) — cho user gõ `/<name>` để trigger workflow. **Đang bị deprecate** vì logic thực đã move vào Skills — commands chỉ còn là "legacy compatibility layer" để user habit cũ vẫn hoạt động.

**EN:** Commands are **slash-entry shims** (like `/tdd`, `/plan`, `/code-review`) — letting users type `/<name>` to trigger workflows. **Being deprecated** — real logic has moved into Skills; commands remain only as a "legacy compatibility layer" for existing user habits.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng command khi:
- **Team quen** gõ command cụ thể (muscle memory) và không muốn đổi
- **Backward compat** cho setup cũ chưa migrate sang skills
- Cần quick-invoke với **short name** (`/plan` nhanh hơn tìm skill)
- Cần trigger cụ thể ngoài auto-load của skill

### ❌ KHÔNG dùng command khi:
- Viết workflow mới → **dùng skill** (commands deprecated, tương lai có thể bị remove)
- Cần structure/reasoning phức tạp → skill có format chuẩn hơn
- Cần share/distribute → skill có ecosystem tốt hơn
- Muốn auto-load theo context → skill có description-based trigger, command không

> **Quy tắc vàng theo shortform guide:** *"Slash entries are convenient, but the real durable unit is the underlying skill."*

---

## Command vs Skill vs Hook vs Subagent (chọn cái nào?)

| Tiêu chí | Command (legacy) | Skill (primary) | Hook | Subagent |
|----------|------------------|-----------------|------|----------|
| **Invocation** | User gõ `/<name>` | User gõ `/<name>` HOẶC auto-load theo description | Event tự động | Orchestrator delegate |
| **Structure** | Ít quy định (markdown tự do) | Format chuẩn (When to Use / How It Works / Examples) | JSON trong settings.json | Markdown + frontmatter |
| **Auto-activation** | ❌ Chỉ manual | ✅ Via description match | ✅ Via event matcher | ✅ Via description |
| **Discoverability** | `/<tab>` completion | `/<tab>` + skill registry | N/A (background) | `/agents` registry |
| **Distribution** | Part of plugin hoặc manual copy | Part of plugin + has case study path (continuous-learning evolve) | Part of plugin (auto-load) | Part of plugin |
| **Status trong ECC** | **LEGACY** (migrating) | ✅ **PRIMARY** | Stable | Stable |
| **Security risk** | LOW (just prompt) | LOW-MED (workflow can invoke tools) | MED (code execution) | MED (separate context) |

> **Quy tắc quyết định (ECC ngày nay):**
> - **Viết mới** → luôn dùng **Skill**
> - **Maintain code cũ** → command OK, nhưng plan migrate
> - **Một-lần task** → inline, không tạo command

---

## ECC ship 79 commands — phân loại / 79 commands categorized

> Số liệu verified: `ls commands/ | wc -l` = **79** ✅ match README Quick Start. **Q2 fully resolved:** agents 48, skills 185, commands 79 — all match Quick Start; changelog v1.10.0 all outdated (38/156/72).

### Theo category

| Category | Commands |
|----------|----------|
| **Core workflow** | `/plan`, `/tdd`, `/e2e`, `/code-review`, `/build-fix`, `/checkpoint`, `/eval`, `/feature-dev`, `/refactor-clean` |
| **Language-specific** (build/review/test per ngôn ngữ) | `/go-build`, `/go-review`, `/go-test`, `/cpp-build`, `/cpp-review`, `/cpp-test`, `/flutter-build`, `/flutter-review`, `/flutter-test`, `/kotlin-build`, `/kotlin-review`, `/kotlin-test`, `/gradle-build`, `/python-review` |
| **Multi-agent orchestration** | `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, `/multi-workflow`, `/orchestrate` |
| **Learning / continuous learning** | `/learn`, `/learn-eval`, `/evolve`, `/instinct-status`, `/instinct-export`, `/instinct-import`, `/prune` |
| **Hook management** | `/hookify`, `/hookify-configure`, `/hookify-help`, `/hookify-list` |
| **ECC meta / harness** | `/harness-audit`, `/loop-start`, `/loop-status`, `/model-route`, `/pm2`, `/quality-gate`, `/sessions` |
| **Skill utilities** | `/skill-create` (sinh skills từ git history), `/skill-stocktake` |
| **Ecosystem tool integration** | `/aside`, `/claw`, `/devfleet`, `/jira`, `/docs`, `/context-budget`, `/agent-sort` |
| **Generative** | `/gan-build`, `/gan-design` |
| **Setup helpers** | `/codex-setup`, `/setup-pm` |

### 3 name forms cần biết

| Context | Form | Ví dụ |
|---------|------|-------|
| **Plugin install** (namespaced) | `/<namespace>:<command>` | `/ecc:plan "Add auth"` |
| **Manual install** (root level) | `/<command>` | `/plan "Add auth"` |
| **Disabled** | `/plugin` → toggle off | N/A |

---

## Anatomy: Một command file trông như thế nào / What a command file looks like

### Format 1: Với frontmatter (auto-trigger, recommended)

```markdown
---
description: Restate requirements, assess risks, and create step-by-step
             implementation plan. WAIT for user CONFIRM before touching any code.
---

# Plan Command

This command invokes the **planner** agent to create a comprehensive
implementation plan before writing any code.

## What This Command Does
1. Restate Requirements
2. Identify Risks
3. Create Step Plan
4. Wait for Confirmation

## When to Use
Use `/plan` when:
- Starting a new feature
- Making significant architectural changes
...

## How It Works
[Detailed workflow]

## Example Usage
[Concrete example]

## Integration with Other Commands
[Related commands]

## Related Agents
This command invokes the `planner` agent.
```

### Format 2: Không frontmatter (manual invocation only)

```markdown
# /learn - Extract Reusable Patterns

Analyze the current session and extract any patterns worth saving as skills.

## Trigger
Run `/learn` at any point during a session when you've solved a non-trivial problem.

## What to Extract
- Error Resolution Patterns
- Debugging Techniques
- Workarounds
- Project-Specific Patterns

## Output Format
[Skill file template]

## Process
[Steps]
```

### Frontmatter fields

| Field | Bắt buộc | Ý nghĩa |
|-------|----------|---------|
| `description` | ❌ (nhưng khuyến nghị) | Nếu có → command có thể auto-trigger theo context match |

> **Note:** Commands DON'T use `name`, `tools`, `model` fields như agents/skills. Chỉ có `description` optional. Name của command = filename (`plan.md` → `/plan`).

### Body sections convention (loose)

Không strict như skill. Thường có:
- **What This Command Does** — bullet list các action
- **When to Use** — trigger conditions
- **How It Works** — workflow chi tiết
- **Example Usage** — concrete example
- **Integration** — liên kết commands khác
- **Related Agents / Skills** — underlying delegate

---

## Cơ chế / How It Works

```
User types `/plan Add auth`
    ↓
Claude Code parse command name
    ↓
Look up `<command-name>.md` trong:
  - ~/.claude/commands/  (user-level)
  - <project>/.claude/commands/ (project-level)
  - plugin-installed commands
    ↓
Inject command body vào context as prompt
    ↓
Claude execute workflow defined in body
    ↓
Nếu body reference agent/skill → delegate/invoke
```

### Command là "shim" — real logic ở đâu?

Per shortform guide: *"Durable logic should live in skills."*

Ví dụ `/plan`:
- Command file (`commands/plan.md`) chỉ define WHEN to invoke
- Body note: *"This command invokes the **planner** agent"*
- Real logic: `agents/planner.md` (đã phân tích trong [[(C) Subagents]])

### Migration path cho mỗi command

| Command legacy | Migration target |
|----------------|------------------|
| `/plan` | Skill + planner agent (or newer `/prp-plan`) |
| `/tdd` | Skill `tdd-workflow` + tdd-guide agent |
| `/code-review` | Skill `code-review` + code-reviewer agent |
| `/build-fix` | Skill + build-error-resolver agent |
| `/e2e` | Skill `e2e-testing` + e2e-runner agent |
| `/refactor-clean` | Skill + refactor-cleaner agent |
| `/learn` | Skill `continuous-learning` (v1 Stop-hook based) |
| `/evolve` | Skill `continuous-learning-v2` |
| `/instinct-*` | Part of skill `continuous-learning-v2` 6 commands |

> **Pattern:** Mỗi command thường map 1-1 với skill + agent combo. Command chỉ là entry point.

---

## Configuration: Naming / Discovery / Disable

### Discovery

```bash
# List available commands (plugin install, namespaced)
/plugin list everything-claude-code@everything-claude-code

# Manual discovery (not namespaced)
<tab> completion sau khi gõ /

# Xem command file gốc
cat ~/.claude/commands/<command>.md
```

### Custom command

Tạo file mới trong `~/.claude/commands/<my-command>.md` với format ở trên → Claude Code pick up tên file thành `/my-command`.

### Disable

- Xoá file khỏi `~/.claude/commands/`
- Hoặc `/plugin` → toggle off plugin chứa command đó

---

## Patterns kết hợp / Combination patterns

### Command → Skill (recommended migration path)

1. Identify command đang dùng thường (vd `/plan`)
2. Tạo skill tương đương với format chuẩn (When to Use / How It Works / Examples)
3. Skill có description-based auto-trigger → có thể không cần user gõ `/plan` nữa
4. Keep command file làm compat shim nếu team quen

### Command → Subagent

Nhiều command chỉ là delegate cho subagent (`/plan` → `planner` agent). Có thể skip command step, invoke subagent directly qua main Claude: *"Use the planner agent to design X."*

### Command chaining (sequential phases)

```
/plan Add notification system
  → User confirm
/tdd Implement phase 1
  → User verify
/code-review
  → User approve
/checkpoint
```

Mỗi command trigger 1 phase — pattern giống "Sequential Phases Orchestration" từ [[(C) Longform Guide summary]].

### Command + Multi-agent (advanced)

`/multi-plan`, `/multi-execute` là orchestrator commands cho multi-agent workflows. **CẢNH BÁO:** theo README, multi-* commands cần `ccg-workflow` runtime cài riêng:

```bash
npx ccg-workflow  # initialize runtime
```

Không có runtime này, multi-* commands sẽ không chạy đúng.

---

## Real-world examples từ repo

| File | Pattern |
|------|---------|
| `commands/plan.md` | Frontmatter + full structure + points to agent |
| `commands/learn.md` | No frontmatter + manual-invoke workflow |
| `commands/tdd.md` | Frontmatter + skill delegation |
| `commands/multi-plan.md` (9.1KB) | Complex orchestration command |
| `commands/pm2.md` (6.5KB) | Tool wrapper command |

---

## Anti-patterns / Sai lầm hay gặp

1. **Viết command mới thay vì skill** → đi ngược migration path. Viết skill luôn.
2. **Command body có logic phức tạp** không point tới agent/skill → không tái dùng được, hard to test.
3. **Command description quá generic** → "do stuff" → Claude không biết khi nào trigger.
4. **Duplicate logic** giữa command body và skill body — source of truth không rõ.
5. **Hardcode paths** trong command body → không portable across projects.
6. **Dùng multi-* commands mà chưa cài `ccg-workflow`** → silent fail.
7. **Không track migration status** — không biết command nào đã có skill replace, command nào chưa.
8. **Quên namespace khi plugin install** → user gõ `/plan` thay vì `/ecc:plan` → not found.
9. **Command chỉ gồm 1 dòng prompt** — không cần command, gõ trực tiếp nhanh hơn.
10. **Không update command khi underlying agent/skill thay đổi** → stale behavior.

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| `/plugin list` | Discover commands installed |
| `<tab>` completion | Autocomplete command name |
| `/skill-create` | Migrate command → skill |
| `/skill-stocktake` | Audit xem command/skill duplicate không |
| `npx ccg-workflow` | Runtime cho multi-* commands |

---

## Cross-references

- [[(C) Skills]] — **migration target**, primary workflow surface; command là shim của skill
- [[(C) Subagents]] — command thường delegate cho agent (vd `/plan` → planner agent)
- [[(C) Hooks]] — alternative cho enforcement (command manual, hook automatic)
- [[(C) Plugins]] — command bundled trong plugin.json
- [[(C) Shortform Guide summary]] — "Skills > Commands" guiding principle
- [[(C) Longform Guide summary]] — sequential phases pattern (command chain)
- [[(C) README summary]] — 79 commands counted, namespaced form
- [[(C) index]] — main catalog

## Citations

- `commands/plan.md` (full file, 3.8KB) — example with frontmatter, point to agent
- `commands/learn.md` (full file, 1.6KB) — example without frontmatter
- `the-shortform-guide.md`, lines 13–34 — "commands/ layer is legacy slash-entry compatibility"
- `README.md`, lines 442–475, 254 — full command list, namespacing convention, multi-* runtime warning
- Counts verified: `ls commands/ | wc -l` = 79 ✅ match README Quick Start. **Q2 fully resolved.**

---

## TODO cho lần ingest tiếp

- [ ] Đọc 1-2 multi-* command (vd `multi-plan.md` 9.1KB) để hiểu multi-agent orchestration sâu hơn
- [ ] Verify `ccg-workflow` runtime là gì, install như thế nào, có open source không
- [ ] Check `commands/` count trong `plugin.json` vs filesystem — có discrepancy giống agents (38 vs 48) không?
- [ ] Đọc `commands/skill-create.md` — công cụ migration command→skill, quan trọng cho adoption
- [ ] Đọc `commands/evolve.md` — kết nối với continuous-learning v2
- [ ] Tìm hiểu `/prp-plan`, `/prp-implement` — newer replacement được mention trong `plan.md`. Có phải là skill mới thay `/plan` không?
