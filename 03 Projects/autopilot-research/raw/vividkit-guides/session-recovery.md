# Khôi Phục Session - VividKit Documentation | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/session-recovery

> Extracted from: session-recovery.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Khôi Phục Session & Resume

Không bao giờ mất tiến độ khi đổi model

Bị rate limit? Lỗi model? Học cách resume session, export context và tiếp tục công việc một cách liền mạch.

#### Session State Tự động

Hook session-state.cjs tự động lưu và khôi phục tiến trình session qua các lần compact và khởi động lại.

- • State được lưu vào .claude/session-state/.last-state.md
- • Tự động load khi SessionStart (khởi động hoặc sau compact)
- • Tự động lưu khi có sự kiện Stop và SubagentStop
- • State bao gồm: plan hiện tại, todo items, subagent outputs, trạng thái branch/commit
- • Lưu trữ state cũ — xoay vòng sau 10 sessions
- • Thiết kế fail-open: không chặn nếu hook gặp lỗi

Tự động lưu session state mặc định. Recovery thủ công (/resume, /export) vẫn hoạt động như fallback.

Cảnh Báo: Ban Tài Khoản Google

Google đang tích cực ban các tài khoản sử dụng Antigravity/Gemini OAuth với công cụ bên thứ ba (OpenCode, các công cụ dựa trên CLIProxy như CCS, AntigravityManager, v.v.). Việc sử dụng các công cụ này có thể vi phạm ToS của Google và dẫn đến mất quyền truy cập vĩnh viễn vào các dịch vụ Google. Sử dụng GLM hoặc Kimi thay thế.

1

#### Hiểu Về Session

Mỗi cuộc hội thoại với Claude Code tạo ra một session với ID duy nhất. Các session được lưu trữ cục bộ theo project.

 Đường dẫn file: 

  macOS 

  Linux 

  Windows 

` ~/.claude/history.jsonl `

``` text-slate-700
# Find your session ID from history
cat ~/.claude/history.jsonl | tail -5

# Look for sessionId in the JSON object
# Example output:

# Sessions are stored per-project in:
# ~/.claude/projects//.jsonl
```

Điểm Quan Trọng

Session dựa trên project. Default Claude, API profiles, và CLIProxy chia sẻ session. Chỉ có CCS sub-accounts bị cô lập.

2

#### Session Sharing

 Quan Trọng 

Default Claude, API profiles và CLIProxy chia sẻ session storage. CCS sub-accounts có session riêng biệt.

✅ SHARE Session (Switch Thoải Mái)

- • Default Claude ↔ API profiles (GLM, Kimi)
- • API profiles ↔ CLIProxy (gemini, codex, agy)
- • Default Claude ↔ CLIProxy
- • Tất cả lưu tại ~/.claude/projects//

❌ ISOLATED Session

- • CCS sub-accounts (work, personal,...)
- • Mỗi instance có folder riêng: ~/.ccs/instances//
- • Không switch được sang sub-account khác
- • Không switch được sang Default Claude/API profiles/CLIProxy

Tại sao?

Default Claude, API profiles, và CLIProxy đều dùng chung ~/.claude/. CCS sub-accounts override CLAUDE_CONFIG_DIR sang ~/.ccs/instances// nên session bị cô lập hoàn toàn.

Cách Giải Quyết (Cho CCS Sub-accounts)

**Cách 1:** Dùng /export trước khi chuyển, sau đó paste context quan trọng vào session mới.\
**Cách 2:** Copy file session .jsonl sang target config directory (vd: ~/.claude/projects// → ~/.ccs/instances//projects//).

3

#### Resume Session

Default Claude, API profiles (GLM, Kimi), và CLIProxy (gemini, codex, agy) có thể /resume lẫn nhau. Xem Session Sharing ở trên để biết chi tiết.

Option 1: Interactive resume

Shows recent sessions list to pick from

``` text-slate-700
> /resume
```

Option 2: Specific session ID

Resume with specific session ID

``` text-slate-700
> /resume 74f292c0-49fa-41c0-a2d8-dd2c3ef9c4be
```

Option 3: Command line

Resume directly when starting CCS

``` text-slate-700
ccs glm --resume
ccs agy --resume 74f292c0-49fa-41c0-a2d8-dd2c3ef9c4be
```

Tiếp Tục Liền Mạch

Tất cả context từ session trước được khôi phục. Tiếp tục đúng chỗ bạn dừng lại.

4

#### Export Context

 Cho Session Quá Lớn 

Khi context session quá lớn (100K+ tokens), /resume chỉ chuyển vấn đề sang nơi khác. Dùng /export để bắt đầu mới chỉ với context thiết yếu.

Context Bloated

Session \> 100K tokens, /resume just moves the problem

Fresh Start

Keep only essential context, discard noise

Share Externally

Teammates, documentation, backup

Step 1: Export — Export current conversation to a text file

/export \# Creates conversation.txt in current dir /export ~/backup/session \# Custom path

Step 2: Start Fresh — Start a new session with a cheaper provider

ccs glm

Step 3: Paste Context — Manually transfer the essential context

\> "Here's my previous context: \[paste key parts of export\]" \> "Continue implementing the auth handler"

Khi Nào Dùng Cái Nào?

**Dùng /resume** khi context còn healthy (Default Claude, API profiles, CLIProxy đều share session).\
**Dùng /export** khi context quá lớn, HOẶC khi chuyển sang/từ CCS sub-account (bị cô lập).

5

#### Chiến Lược Fallback Model

Setup nhiều terminal với các provider sẵn sàng. Default Claude, API profiles, CLIProxy có thể /resume lẫn nhau. Chỉ CCS sub-accounts bị cô lập.

Setup  Multiple terminals ready

\# Terminal 1: ccs work (Claude - primary) \# Terminal 2: ccs agy (Antigravity - backup) \# Terminal 3: ccs glm (GLM - cost-optimized)

Decision Logic  When Claude hits limit:

\# Context healthy? → /resume in another terminal \# Context bloated? → /export, then fresh session

Quick Switch  Resume with full context

ccs glm --resume

Claude

Chính: Task phức tạp

Antigravity

Backup: Full sức mạnh Claude

GLM

Rẻ hơn 81%: Implementation

6

#### Pro Tips

 Power User 

Các trick nâng cao để khôi phục session một cách mượt mà khi cần.

 /rename để dễ resume

Đặt tên dễ nhớ cho session thay vì dùng UUID

``` text-slate-700
# Trong session, đổi thành tên dễ nhớ:
/rename auth-feature

# Sau đó resume bằng tên hoặc UUID (cả 2 đều được):
/resume auth-feature # ✅ Dễ nhớ
/resume 74f292c0...  # ✅ Vẫn hoạt động tốt

# Hoặc chạy ngay từ terminal:
ccs glm/agy "/resume auth-feature"
```

 --continue trick

Tự động tiếp tục session cuối khi bị out bất ngờ

``` text-slate-700
# Nếu bạn bị đá khỏi session vì lý do nào đó:
ccs glm/agy/work --continue continue

# Tự động resume và tiếp tục session cuối của bạn
```

 /login account switch

Switch account Claude khi bị rate limit

``` text-slate-700
# Trong session hiện tại, khi dính rate limit:
/login

# Chọn sub-account Claude khác
# Sau đó gõ "continue" để tiếp tục làm việc
continue
```

 /compact chủ động

Nén context thông minh khi token sắp hết — giữ lại đúng thông tin cần thiết

``` text-slate-700
# Khi thấy token đã cao, % usage sắp reach limit:
/compact keep the original plan, user's request, key changes & todo tasks

# ⚠️ Tránh dùng /compact không có yêu cầu cụ thể:
/compact  # ❌ Dễ mất thông tin quan trọng!
```

Nhiều Tài Khoản Claude

Nếu bạn có nhiều sub-account Claude, bạn có thể rotate giữa chúng khi bị rate limit. Dùng /login để switch account trong cùng session (context vẫn trong memory). Lưu ý: CCS sub-accounts có session riêng biệt, không /resume được từ terminal khác.

### Checklist Khôi Phục Khẩn Cấp

Bookmark cái này. Khi gặp sự cố giữa chừng, làm theo các bước sau:

1

#### BÌNH TĨNH (DON'T PANIC)

Công việc của bạn chưa mất đâu. Session được lưu an toàn trên máy.

2

#### ĐÁNH GIÁ CONTEXT SIZE

Check xem session có bị phình to không (phản hồi chậm = khả năng cao bị đầy)

3

#### NẾU CONTEXT OK → /RESUME

Dùng /resume (Default Claude, API profiles, CLIProxy đều share session)

ccs glm --resume \# Hoặc bên trong Claude Code: /resume

4

#### NẾU CONTEXT QUÁ TẢI → /EXPORT

Export ra file và bắt đầu session mới

/export ~/backup/session.txt ccs glm \> "Context từ session trước: \[dán phần quan trọng vào đây\]"

5

#### TIẾP TỤC CODE THÔI!

Bạn đã quay trở lại guồng công việc.

####  Tiết Kiệm 80%+ Chi Phí

Bắt đầu task phức tạp với Claude, rồi /resume với GLM (API profile) cho implementation với chi phí rẻ hơn 81%.

####  Không Thời Gian Chết

Đừng để rate limit ngăn cản dòng làm việc. /resume trong provider tương thích và tiếp tục làm việc.

### Các Guide Liên Quan

[](/vi/guides/ccs)

CCS Guide

Multi-account & đổi model

[](/vi/guides/commands)

Commands

Tất cả lệnh có sẵn

