# (C) Hooks — Entity Page

> **Type:** Building block #3 (foundation)
> **Status:** First entity page — retrofitted với 3 sections mới (Comparison, Anatomy, Combination patterns) để khớp format chuẩn
> **Sources:** 4 — README, shortform guide, longform guide, `hooks/README.md`
> **Last updated:** 2026-04-17 (retrofitted)

---

## Một câu / One-liner

**VI:** Hooks là **automation trigger theo event**, fire trước/sau tool calls hoặc tại lifecycle boundary của Claude Code session — để enforce code quality, save state, warn về anti-pattern, và automate những việc lặp lại.

**EN:** Hooks are **event-triggered automations** that fire before/after Claude Code tool calls or at session lifecycle boundaries — to enforce code quality, save state, warn about anti-patterns, and automate repetitive checks.

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng hook khi:
- Cần **enforce rule** mà Claude hay quên (vd block console.log commit, format on save)
- Cần **save state** giữa session (vd PreCompact lưu context trước khi compact)
- Cần **warn** về behavior không đúng convention (vd file > 800 lines, missing test file)
- Cần **automate** việc lặp lại (vd `prettier --write` sau mỗi Edit)

### ❌ KHÔNG dùng hook khi:
- Logic phức tạp cần reasoning → dùng **skill** thay vì hook
- Một lần (one-off) → chạy command thẳng, không cần hook
- Latency-sensitive → tránh `UserPromptSubmit` (chạy mỗi message)
- Cần Claude "biết" kết quả → hook chỉ warn qua stderr, Claude đọc được; nhưng nếu cần logic chặt thì skill tốt hơn

---

## Hook vs Skill vs Subagent (chọn cái nào?)

| Tiêu chí | Hook | Skill | Subagent |
|----------|------|-------|----------|
| **Trigger** | Event tự động (PreTool, PostTool, Stop…) | User invoke (`/skill-name`) hoặc auto via description | Orchestrator delegate |
| **Reasoning** | ❌ Không | ✅ Có (workflow + structure) | ✅ Có (full Claude inference, separate context) |
| **Latency** | Phải nhanh (< 200ms cho blocking) | Trung bình | Chậm nhất (spawn + inference) |
| **Cost** | ~0 token | Token của main session | Token RIÊNG cho subagent (cộng thêm) |
| **Mechanism** | Shell command nhận JSON stdin/stdout | Markdown workflow definition | Spawn Claude với system prompt + tool scope |
| **Output** | Stderr warning hoặc block (exit 2) | Trả về cùng conversation | Summary trả về cho orchestrator |
| **Use case điển hình** | Format on save, block console.log commit, audit | Reusable workflow như `/tdd`, `/code-review` | Delegate exploration cần nhiều file đọc |

> **Quy tắc quyết định / Decision rule:**
> - Cần **enforce / automate** không reasoning → **Hook**
> - Cần **reusable workflow** với reasoning, gọi từ user → **Skill**
> - Cần **delegate task tốn context** với scope/model riêng → **Subagent**

---

## 6 Hook Types

| # | Type | Trigger | Có thể block? | Use case điển hình |
|---|------|---------|---------------|--------------------|
| 1 | `PreToolUse` | Trước khi tool chạy | ✅ exit code 2 = block | Validation, block dangerous commands, reminder |
| 2 | `PostToolUse` | Sau khi tool chạy xong | ❌ chỉ analyze output | Format on save, typecheck, log warnings |
| 3 | `UserPromptSubmit` | Khi user gửi message | ❌ | Inject context, log query *(⚠️ thêm latency mỗi prompt)* |
| 4 | `Stop` | Claude trả lời xong (mỗi response) | ❌ | Audit modified files, persist learnings, cost tracker |
| 5 | `PreCompact` | Trước context compaction | ❌ | Save state ra file để khôi phục |
| 6 | `Notification` | Khi cần permission | ❌ | Custom permission flow |

**Bonus lifecycle (từ ECC):**

| Type | Trigger | Use case |
|------|---------|----------|
| `SessionStart` | Session mới bắt đầu | Auto-load previous context, detect package manager |
| `SessionEnd` | Session kết thúc | Cleanup log, lifecycle marker |

> **Note:** `SessionStart`/`SessionEnd` được Claude Code support; ECC sử dụng để memory persistence.

---

## Anatomy: Một hook entry trông như thế nào / What a hook entry looks like

Hooks được config qua **JSON** trong `~/.claude/settings.json` hoặc `hooks/hooks.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",                    // Tool name hoặc regex
        "description": "Tmux reminder",       // optional, hiển thị khi hook fire
        "hooks": [
          {
            "type": "command",                 // luôn là "command"
            "command": "node /path/to/hook.js",// shell command thực thi
            "async": false,                    // optional, default false
            "timeout": 30                      // optional, giây (chỉ khi async=true)
          }
        ]
      }
    ],
    "PostToolUse": [ ... ],
    "Stop": [ ... ]
  }
}
```

### Field reference

| Field | Bắt buộc | Ý nghĩa |
|-------|----------|---------|
| `matcher` | ✅ | Tool name (`Bash`, `Edit`, `Write`, …) hoặc regex/expression. Có thể dùng `\|` để OR (vd `Edit\|Write\|MultiEdit`) |
| `description` | ❌ | Tên hook để debug/log |
| `hooks[].type` | ✅ | Hiện tại luôn `"command"` |
| `hooks[].command` | ✅ | Shell command. Có thể inline `node -e "..."` hoặc gọi file `node /path/to/hook.js` |
| `hooks[].async` | ❌ | `true` = chạy background, không block. Mặc định `false`. |
| `hooks[].timeout` | ❌ | Giây, chỉ khi `async=true`. Mặc định 30s. |

### Matcher patterns hay dùng

| Matcher | Match khi |
|---------|-----------|
| `"Bash"` | Mọi Bash tool call |
| `"Edit"` | Mọi Edit tool call |
| `"Edit\|Write\|MultiEdit"` | Bất kỳ tool ghi file nào |
| `"Write"` + check file_path trong hook | Filter theo extension/path bằng JS trong command |
| `"*"` | Mọi tool (dùng trong `Stop` hook) |

> **Lưu ý:** Matcher chỉ filter theo **tool name**. Filter theo **file extension** hay **command content** phải làm trong hook script (đọc `tool_input` từ stdin JSON).

---

## Cơ chế / How It Works

```
User request
    ↓
Claude picks tool
    ↓
PreToolUse hook fires    ← có thể block (exit 2) hoặc warn (stderr)
    ↓
Tool executes
    ↓
PostToolUse hook fires   ← chỉ analyze, không block
    ↓
Claude continues / responds
    ↓
Stop hook fires          ← khi response xong
```

**Hook là shell command:**
- Nhận **JSON trên stdin** (tool name, tool input, tool output nếu Post)
- Output **JSON trên stdout** (thường echo lại data gốc)
- Warning qua **stderr** (Claude đọc được)
- Exit code: `0` = success, `2` = block (chỉ Pre), khác = error (log nhưng không block)

### Hook input schema

```typescript
interface HookInput {
  tool_name: string;          // "Bash", "Edit", "Write", "Read", ...
  tool_input: {
    command?: string;         // Bash: command đang chạy
    file_path?: string;       // Edit/Write/Read: file target
    old_string?: string;      // Edit: text bị replace
    new_string?: string;      // Edit: text thay thế
    content?: string;         // Write: file content
  };
  tool_output?: {             // CHỈ có ở PostToolUse
    output?: string;
  };
}
```

---

## Async Hooks

Cho hook chậm không nên block main flow:

```json
{
  "type": "command",
  "command": "node my-slow-hook.js",
  "async": true,
  "timeout": 30
}
```

> ⚠️ Async hook **không thể block** tool execution.
> ⚠️ Blocking hooks (PreToolUse, Stop): giữ < 200ms — không network call.

---

## Hooks ECC ship sẵn / Hooks ECC ships out of the box

> Sample, không phải full list. Xem `hooks/README.md` cho list đầy đủ.

### PreToolUse

| Hook | Matcher | Hành vi | Exit |
|------|---------|---------|------|
| **Dev server blocker** | `Bash` | Block `npm run dev` ngoài tmux | 2 (block) |
| **Tmux reminder** | `Bash` | Suggest tmux cho `npm test`, `cargo build`, `docker` | 0 (warn) |
| **Git push reminder** | `Bash` | Reminder review trước `git push` | 0 (warn) |
| **Pre-commit quality** | `Bash` | Lint staged files, validate commit msg, detect console.log/secrets | 2 hoặc 0 |
| **Doc file warning** | `Write` | Warn về `.md`/`.txt` không chuẩn (allow README, CLAUDE, CHANGELOG, …) | 0 (warn) |
| **Strategic compact** | `Edit\|Write` | Suggest `/compact` mỗi ~50 tool calls | 0 (warn) |

### PostToolUse

| Hook | Matcher | Việc làm |
|------|---------|----------|
| **Prettier format** | `Edit` | Auto-format JS/TS với Prettier |
| **TypeScript check** | `Edit` | `tsc --noEmit` cho `.ts`/`.tsx` |
| **Console.log warning** | `Edit` | Warn `console.log` trong file đã edit |
| **Quality gate** | `Edit\|Write\|MultiEdit` | Fast quality checks |
| **Build analysis** | `Bash` | Background analysis sau build (async) |
| **PR logger** | `Bash` | Log PR URL sau `gh pr create` |
| **Design quality check** | `Edit\|Write\|MultiEdit` | Warn frontend drift về template generic |

### Lifecycle

| Hook | Event | Việc làm |
|------|-------|----------|
| **Session start** | `SessionStart` | Load previous context + detect package manager |
| **Pre-compact** | `PreCompact` | Save state trước compact |
| **Session summary** | `Stop` | Persist session state khi có transcript |
| **Pattern extraction** | `Stop` | Evaluate session cho continuous learning |
| **Cost tracker** | `Stop` | Run-cost telemetry markers |
| **Console.log audit** | `Stop` | Check modified files cho `console.log` |
| **Desktop notify** | `Stop` | macOS notification (profile standard+) |
| **Session end marker** | `SessionEnd` | Cleanup log |

---

## Configuration: 3 cách điều khiển hook

### 1. Hook Profiles (env var) — KHUYẾN NGHỊ cho người mới

```bash
export ECC_HOOK_PROFILE=standard   # default
# minimal | standard | strict
```

| Profile | Khi dùng |
|---------|----------|
| `minimal` | Chỉ essential lifecycle + safety. Dùng khi muốn quiet, ít noise. |
| `standard` | Default. Balanced quality + safety checks. **Người mới start ở đây.** |
| `strict` | Thêm reminder + stricter guardrail. Dùng cho production code. |

### 2. Disable specific hooks (env var)

```bash
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"
```

Hữu ích khi 1 hook annoy mà chưa muốn xoá hẳn.

### 3. Override trong settings.json

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [],
        "description": "Override: allow all .md file creation"
      }
    ]
  }
}
```

---

## 4 Recipe người mới có thể paste-and-run

### Recipe 1: Warn về TODO/FIXME/HACK comments

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "command",
    "command": "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const i=JSON.parse(d);const ns=i.tool_input?.new_string||'';if(/TODO|FIXME|HACK/.test(ns)){console.error('[Hook] New TODO/FIXME added - consider creating an issue')}console.log(d)})\""
  }],
  "description": "Warn when adding TODO/FIXME comments"
}
```

### Recipe 2: BLOCK file > 800 lines

```json
{
  "matcher": "Write",
  "hooks": [{
    "type": "command",
    "command": "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const i=JSON.parse(d);const c=i.tool_input?.content||'';const lines=c.split('\\n').length;if(lines>800){console.error('[Hook] BLOCKED: File exceeds 800 lines ('+lines+' lines)');process.exit(2)}console.log(d)})\""
  }]
}
```

### Recipe 3: Auto-format Python với `ruff`

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "command",
    "command": "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const i=JSON.parse(d);const p=i.tool_input?.file_path||'';if(/\\.py$/.test(p)){const{execFileSync}=require('child_process');try{execFileSync('ruff',['format',p],{stdio:'pipe'})}catch(e){}}console.log(d)})\""
  }]
}
```

### Recipe 4: Reminder viết test cho file source mới

```json
{
  "matcher": "Write",
  "hooks": [{
    "type": "command",
    "command": "node -e \"const fs=require('fs');let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const i=JSON.parse(d);const p=i.tool_input?.file_path||'';if(/src\\/.*\\.(ts|js)$/.test(p)&&!/\\.test\\.|\\.spec\\./.test(p)){const testPath=p.replace(/\\.(ts|js)$/,'.test.$1');if(!fs.existsSync(testPath)){console.error('[Hook] No test file found for: '+p);console.error('[Hook] Consider /tdd')}}console.log(d)})\""
  }]
}
```

---

## Pattern nâng cao: Memory Persistence (longform guide)

Bộ 3 hook ít người biết, dùng cho cross-session memory:

| Hook | Khi fire | Việc làm |
|------|----------|----------|
| `PreCompact` | Trước khi context bị compact | Save important state ra `.claude/.tmp/<session>.md` |
| `Stop` | Session response xong | Append learnings ra session file |
| `SessionStart` | Session mới mở | Auto-load previous session file vào context |

> Implementation có sẵn ở `hooks/memory-persistence/` trong repo ECC.

---

## Pattern nâng cao: Continuous Learning (longform guide)

> **Design decision quan trọng:** dùng `Stop` hook chứ KHÔNG dùng `UserPromptSubmit`.

| Hook | Tần suất | Latency impact |
|------|----------|----------------|
| `UserPromptSubmit` | Mỗi message | ❌ Thêm latency mỗi prompt user gõ |
| `Stop` | 1 lần / session | ✅ Lightweight, không slow session |

Khi Stop fire, hook evaluate session, extract pattern non-trivial (debug technique, workaround), save thành skill mới. Lần sau gặp problem tương tự, skill auto-load.

---

## Patterns kết hợp / Combination patterns

### Hook + Subagent

Hook detect event → trigger delegation cho subagent.
**Ví dụ:** `Stop` hook detect file `.ts` đã edit → main agent tự delegate cho `typescript-reviewer` subagent. → Auto code review không cần user gõ command.

### Hook + Skill

Hook fire skill thay vì chạy logic inline.
**Ví dụ:** `PostToolUse` Edit `.py` → fire skill `python-format-and-lint` (skill chứa workflow chuẩn nhiều bước, dễ maintain hơn JSON inline).

### Hook + `/compact`

`PreCompact` hook save state → user manually `/compact` → `SessionStart` hook restore state lần sau. → Memory persistence cross-session.

### Hook chain (Pre + Post + Stop)

Cùng 1 task có thể có chain hook:
- `PreToolUse Edit .ts` → check file size
- `PostToolUse Edit .ts` → prettier + tsc --noEmit
- `Stop` → audit console.log toàn session

> **Pattern:** Pre validate → Post automate → Stop audit. 3 phase coverage cho 1 loại file.

### Hook + ECC profile

Cùng hook config, behavior khác theo `ECC_HOOK_PROFILE`:
- `minimal` — chỉ chạy hook critical
- `standard` — chạy hook quality + safety
- `strict` — thêm reminder + guardrail extra

> Cho phép share hook config team-wide, mỗi developer chọn profile theo style.

---

## Anti-patterns / Sai lầm hay gặp

1. **Paste raw `hooks.json` từ repo vào `~/.claude/`** — ❌ KHÔNG làm. File checked-in là plugin/repo-oriented. Phải qua installer:
   ```bash
   bash ./install.sh --target claude --modules hooks-runtime
   ```

2. **Dùng `UserPromptSubmit` cho việc nặng** — adds latency cho mỗi prompt. Dùng `Stop` thay thế.

3. **Hook chậm không async** — block main flow. Mark `"async": true, "timeout": 30`.

4. **Quên exit 0 trên parse error** — sẽ trông như "hook crash", confusing. Always exit 0 trên error không critical, log qua stderr với prefix `[HookName]`.

5. **Network call trong PreToolUse hook** — chậm + có thể fail. Pre/Stop hooks phải < 200ms.

6. **Hook viết tay JSON inline phức tạp** — khó debug. Dùng `hookify` plugin (`/hookify`) để tạo qua hội thoại, hoặc tách thành file `.js` riêng trong `~/.claude/scripts/`.

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| **`hookify`** plugin | Tạo hook qua conversation, không cần viết JSON tay. Run `/hookify`. |
| **`scripts/hooks/run-with-flags.js`** | Wrapper từ ECC để hook tự động respect `ECC_HOOK_PROFILE` và `ECC_DISABLED_HOOKS` |
| **`/compact`** | Trigger compact thủ công, kết hợp với `PreCompact` hook |
| **`hooks.json`** | File config chính, ECC ship file 46.8KB |

---

## Cross-references

- [[(C) Shortform Guide summary]] — 6 hook types overview + setup mẫu của tác giả
- [[(C) Longform Guide summary]] — memory persistence hooks + continuous learning Stop-hook design
- [[(C) README summary]] — `ECC_HOOK_PROFILE`/`ECC_DISABLED_HOOKS` runtime control
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) Skills]] khi entity page Skills được tạo (skill là alternative cho hook khi cần reasoning)
- _Sẽ link tới_ [[(C) Continuous Learning]] khi entity page đó được tạo

## Citations

- `hooks/README.md` (full file, 9.2KB) — chi tiết hook tables, recipes, schema, profiles
- `the-shortform-guide.md`, lines 38–73 — 6 hook types + JSON example + hookify plugin
- `the-longform-guide.md`, lines 77–102 — memory persistence hooks + continuous learning Stop-hook design
- `README.md`, lines 322–333 — `ECC_HOOK_PROFILE`, `ECC_DISABLED_HOOKS` env var
- Repo references: `rules/common/hooks.md`, `scripts/hooks/`, `hooks/hooks.json` (46.8KB, chưa ingest)

---

## TODO cho lần ingest tiếp

- [ ] Đọc `hooks/hooks.json` (46.8KB) để verify exact list hooks ECC ship — số liệu trong page này có thể incomplete
- [ ] Đọc `rules/common/hooks.md` để bổ sung "hook architecture guidelines" của ECC
- [ ] Đọc `scripts/hooks/session-start.js` (và các file khác) để verify implementation memory persistence
- [ ] Verify với Anthropic docs chính thức xem có hook type nào khác ngoài 6 types ECC liệt kê không
