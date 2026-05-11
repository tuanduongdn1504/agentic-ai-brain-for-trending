# Custom Hooks - VividKit Documentation | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/hooks

> Extracted from: hooks.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Custom Hooks

ClaudeKit hooks tự động hóa workflow bằng cách phản ứng với lifecycle events của Claude Code — session start, tool calls, agent completion, và hơn thế.

Custom Hooks là gì?

Hooks là shell commands được cấu hình trong `~/.claude/settings.json` tự động kích hoạt khi có Claude Code events. Mỗi hook nhận JSON context qua stdin và có thể inject guidance, chặn actions, hoặc lưu state.

 16 hooks trong 5 categories   12 shared utility modules 

### Hook Lifecycle Events

Hooks phản ứng với các Claude Code events:

` SessionStart `  startup, resume, clear, compact 

` UserPromptSubmit `  mỗi user prompt 

` PreToolUse `  trước khi chạy tool 

` PostToolUse `  sau khi chạy tool 

` SubagentStart `  subagent được spawn 

` SubagentStop `  subagent hoàn thành 

` Stop `  session kết thúc 

` TaskCompleted `  task hoàn thành 

` TeammateIdle `  teammate sắp idle 

### Vòng đời Session

 4 hooks 

Khởi tạo, lưu trữ và theo dõi trạng thái session xuyên suốt vòng đời.

` session-init.cjs `  EK + MK 

Khởi tạo session với project detection, load config, và setup environment. Kích hoạt khi startup, resume, clear, và compact.

 Triggers:   SessionStart 

` session-state.cjs `  EK only 

Lưu và khôi phục tiến trình session qua các lần compact. Lưu plan, todo items, và trạng thái branch.

 Triggers:   PostToolUse  Stop  SubagentStop 

` usage-quota-cache-refresh.cjs `  EK only 

Giữ cache usage quota cho statusline. Throttle thông minh: 60s cho prompt, 300s cho tool events.

 Triggers:   SessionStart  UserPromptSubmit  PostToolUse 

` usage-context-awareness.cjs `  EK + MK 

Config gate wrapper cho usage-quota-cache-refresh. Bật usage awareness qua ck-config flag.

 Triggers:   (config-gated) 

### Inject Context

 3 hooks 

Inject rules, thông tin environment, và team context vào prompts và subagents.

` dev-rules-reminder.cjs `  EK + MK 

Inject session info, development rules, modularization reminders, và plan context vào mỗi prompt.

 Triggers:   UserPromptSubmit 

` subagent-init.cjs `  EK + MK 

Inject context tối giản (~200 tokens) vào subagents dùng env vars từ SessionStart.

 Triggers:   SubagentStart 

` team-context-inject.cjs `  EK only 

Inject thông tin đồng đội và task summary khi spawn Agent Team teammates. Non-blocking, fail-open.

 Triggers:   SubagentStart 

### Chất lượng Code

 3 hooks 

Enforce naming conventions, nhắc simplify code, và định dạng plan.

` descriptive-name.cjs `  EK + MK 

Enforce đặt tên file theo kebab-case mô tả rõ ràng khi tạo file mới.

 Triggers:   PreToolUse (Write) 

` simplify-gate.cjs `  EK only 

Thay thế post-edit-simplify-reminder. Tự động trigger code-simplifier khi vượt ngưỡng edit (400 LOC / 8 files).

 Triggers:   PostToolUse (Edit/Write/MultiEdit) 

` plan-format-kanban.cjs `  EK only 

Cảnh báo khi plan.md dùng tên file làm link text thay vì tên dễ đọc.

 Triggers:   PostToolUse (Edit/Write/MultiEdit) 

### Bảo mật & An toàn

 2 hooks 

Chặn truy cập vào file nhạy cảm và thư mục bị hạn chế.

` privacy-block.cjs `  EK + MK 

Chặn truy cập file nhạy cảm (.env, credentials). Cần user phê duyệt để tiếp tục.

 Triggers:   PreToolUse (Bash/Glob/Grep/Read/Edit/Write) 

` scout-block.cjs `  EK + MK 

Chặn truy cập thư mục theo .ckignore patterns. Dùng gitignore-spec matching.

 Triggers:   PreToolUse (Bash/Glob/Grep/Read/Edit/Write) 

### Workflow & Teams

 3 hooks 

Điều phối planning, task tracking, và team agent collaboration.

` cook-after-plan-reminder.cjs `  EK only 

Nhắc chạy /ck:cook sau khi Plan subagent hoàn thành. Xuất plan path cho session mới.

 Triggers:   SubagentStop (Plan) 

` task-completed-handler.cjs `  EK only 

Log task completions và inject progress context khi agents đánh dấu task hoàn thành.

 Triggers:   TaskCompleted 

` teammate-idle-handler.cjs `  EK only 

Inject available task context khi teammate idle. Có thể ngăn idle qua exit code.

 Triggers:   TeammateIdle 

### Deprecated

 1 hook 

Hooks đã bị vô hiệu hoặc đã bị remove khỏi distribution hiện tại.

` skill-dedup.cjs `  Deprecated   EK only 

Ngăn local skills shadow global versions. Bị vô hiệu từ v2.9.1 do race condition với parallel sessions.

 Triggers:   (disabled) 

### Shared Utility Library

Tất cả hooks dùng chung utility modules trong hooks/lib/ cho các concerns chung.

` ck-config-utils `  Đọc/validate cấu hình .ck.json 

` colors `  Format màu ANSI 

` config-counter `  Đếm skills, hooks, agents 

` context-builder `  Build session context với ngưỡng WARN 70% / CRITICAL 90% 

` git-info-cache `  Cache git status cho hiệu suất 

` hook-logger `  Structured diagnostics với performance tracking 

` privacy-checker `  Chặn truy cập file nhạy cảm (.env, credentials) 

` project-detector `  Nhận diện loại project và package manager 

` scout-checker `  Kiểm tra scout agents có sẵn 

` session-state-manager `  Quản lý lưu trạng thái session 

` transcript-parser `  Parse transcripts hội thoại Claude 

` usage-limits-cache `  Atomic cache cho usage quota snapshots 

Thêm hooks sắp ra mắt...

Slack notifications, auto-commit, và nhiều hơn!

Tìm hiểu thêm các built-in hooks của ClaudeKit tại [ClaudeKit Documentation ](https://docs.claudekit.cc/docs/engineer/configuration/hooks)

