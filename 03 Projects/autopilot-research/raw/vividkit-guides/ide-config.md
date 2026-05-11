# Cấu Hình IDE - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/ide-config

> Extracted from: ide-config.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Cấu Hình Provider IDE

Dùng bất kỳ AI provider nào với Claude Code extension

Cấu hình Claude Code VS Code extension (và các IDE fork từ VS Code) để chuyển hướng request qua các provider thay thế như Antigravity, GLM, Kimi, hoặc MiniMax.

Config này chỉ áp dụng cho cửa sổ chat của Claude Code extension — không phải cửa sổ chat AI tích hợp sẵn của Cursor, Windsurf, hay các AI coding IDE khác.

### IDE Được Hỗ Trợ

Bất kỳ IDE nào dựa trên VS Code hỗ trợ Claude Code extension:

VS Code

Chính thức

Cursor

VS Code fork

Windsurf

VS Code fork

Google Antigravity

VS Code fork

### Cách Hoạt Động

Claude Code extension đọc biến môi trường để xác định nơi gửi API request. Bằng cách ghi đè các biến này, bạn có thể chuyển hướng traffic sang bất kỳ API proxy tương thích Anthropic:

1

ANTHROPIC_BASE_URL  — URL endpoint API của provider

2

ANTHROPIC_AUTH_TOKEN  — API key hoặc auth token của bạn

3

ANTHROPIC_MODEL  — Model mặc định sử dụng

4

ANTHROPIC_DEFAULT\_\*\_MODEL  — Map tầng Opus/Sonnet/Haiku sang model của provider

### Các Bước Thiết Lập

Bước 1: Mở VS Code Settings (JSON) — Mở command palette và tìm user settings JSON:

`Cmd/Ctrl + Shift + P → "Preferences: Open User Settings (JSON)"`

Bước 2: Thêm Biến Môi Trường — Dưới đây là ví dụ config cho MỘT provider (AGY). Xem section "Cấu Hình Provider" bên dưới để xem đầy đủ các provider.

``` text-sm
"claudeCode.environmentVariables": [
  ,

  // Ví dụ: AGY via CCS (CLIProxy)
  // Xem section "Cấu Hình Provider" bên dưới để xem đầy đủ các provider
  ,
  ,
  ,
  ,
  ,
  
]
```

Bước 3: Khởi Động Lại Claude Code — Sau khi lưu settings.json, khởi động lại Claude Code extension hoặc reload cửa sổ VS Code để áp dụng thay đổi.

### Cấu Hình Provider

5 providers

Copy config block cho provider bạn muốn vào mảng environmentVariables. Chỉ kích hoạt MỘT provider tại một thời điểm.

Bạn có thể cấu hình tương tự cho các provider khác (ví dụ Codex, Kiro, ...). Provider CLIProxy (như AGY) dùng CCS local proxy — tham khảo config AGY làm mẫu. Provider APIProxy (như GLM, Kimi) kết nối trực tiếp API — tham khảo config GLM/Kimi làm mẫu.

Mặc định: Claude Subscription

Claude Code mặc định sẽ sử dụng Claude subscription của bạn (đã OAuth với claude.ai). Nếu đã config các provider bên dưới và muốn quay lại dùng Claude sub, hãy xóa (hoặc comment) tất cả các config đã set đi.

Quan Trọng: Rủi Ro Bị Ban Tài Khoản Google

Google đang tích cực ban các tài khoản sử dụng Antigravity/Gemini OAuth với công cụ bên thứ ba (OpenCode, CLIProxy, CCS, ProxyPal, AntigravityManager, v.v.). Việc xác thực tài khoản Google với các công cụ này có thể vi phạm ToS và dẫn đến mất quyền truy cập vào tất cả dịch vụ Google. Mọi rủi ro xin tự chịu trách nhiệm.

#### Antigravity (AGY) via CCS

CLIProxy ⚠️ High Risk Cần CCS chạy local. Auth được quản lý tự động.

Cần CCS chạy local. Auth được quản lý tự động.

``` text-sm
// Antigravity (AGY) via CCS (CLIProxy)
,
,
,
,
,

```

 

#### GLM (z.ai)

APIProxy Lấy API key từ z.ai/manage-apikey

Lấy API key từ z.ai/manage-apikey

``` text-sm
// GLM (z.ai) API Proxy
,
,

```

 

#### Kimi (Moonshot AI)

APIProxy Lấy API key từ kimi.com/code/console

Lấy API key từ kimi.com/code/console

``` text-sm
// Kimi (Moonshot AI) API Proxy
,
,

```

 

#### MiniMax

APIProxy Lấy API key từ platform.minimaxi.com

Lấy API key từ platform.minimaxi.com

``` text-sm
// MiniMax API Proxy
,
,

```

 

#### Alibaba Cloud Coding Plan

APIProxy Lấy API key từ Alibaba Cloud Coding Plan (Apsara DevOps)

Lấy API key từ Alibaba Cloud Coding Plan (Apsara DevOps)

``` text-sm
// Alibaba Cloud Coding Plan (APIProxy)
,
,

```

 

### Chọn Model

Chọn giữa các phiên bản Claude Opus. Phiên bản mới hơn có thể cải tiến nhưng có thể tiêu tốn nhiều token hơn cho cùng một tác vụ.

Chỉ Dành Cho NgườI Dùng Claude Subscription

Config này chỉ dành cho ngườI dùng có Claude subscription chính chủ (qua claude.ai). Thêm vào file settings.json của IDE (cùng vị trí với các config provider ở trên).

Lưu ý Token Usage

Opus 4.6 (mới nhất) có thể tiêu tốn nhiều token hơn Opus 4.5 cho cùng một tác vụ. Nếu muốn giảm token usage, hãy cân nhắc chuyển về Opus 4.5.

#### Claude Opus 4.6

Latest Mặc định

Model mới nhất với khả năng tối đa. Có thể dùng nhiều token hơn 4.5.

``` text-sm
// Không cần config - comment out hoặc xóa "claudeCode.selectedModel" để dùng model mới nhất
// "claudeCode.selectedModel": "claude-opus-4-6"
```

#### Claude Sonnet 4.6

Mới

Model nhẹ hơn, mới hơn — phù hợp cho các tác vụ hàng ngày với token usage thấp hơn.

``` text-sm
"claudeCode.selectedModel": "claude-sonnet-4-6"
```

 

#### Claude Opus 4.5

Token Efficient

Phiên bản trước với token consumption thấp hơn cho chất lượng tương đương.

``` text-sm
"claudeCode.selectedModel": "claude-opus-4-5-20251101"
```

 

### Mẹo Chuyên Nghiệp

Chỉ Một Provider

Chỉ kích hoạt MỘT provider block tại một thời điểm. Comment các block khác để tránh xung đột.

Auto Auth với CCS

Các provider CLIProxy (AGY, Codex, Kiro...) tự động xử lý auth qua CCS — không cần API key.

Thinking Budget

Đặt `MAX_THINKING_TOKENS` để điều chỉnh độ sâu suy luận. Giá trị cao hơn = kỹ hơn nhưng chậm hơn.

Cấu Hình Model

ANTHROPIC_MODEL là bắt buộc. ANTHROPIC_DEFAULT\_\*\_MODEL là tùy chọn — chỉ cần set khi muốn dùng model khác nhau cho từng tầng (Opus/Sonnet/Haiku).

### Config Nâng Cao

Các cài đặt bổ sung cho power user. Chỉ dùng khi hiểu rõ rủi ro.

Cảnh Báo Bảo Mật

Config này bỏ qua các prompt xin quyền. Chỉ dùng nếu bạn hoàn toàn tin tưởng AI và hiểu rõ rủi ro. Code và hệ thống của bạn có thể bị ảnh hưởng.

#### Bypass Permissions

Bỏ qua tất cả permission prompts và cho phép Claude tự động thực thi lệnh. Thêm vào file settings.json của IDE.

``` text-sm
"claudeCode.allowDangerouslySkipPermissions": true,
"claudeCode.initialPermissionMode": "bypassPermissions"
```

 

#### Settings JSON Schema

Kích hoạt tính năng tự động hoàn thành và xác thực cho file cấu hình Claude Code. Đã được nâng cấp lên 139 dòng với schema bổ sung cho watch và content. Thêm vào file settings.json của IDE.

``` text-sm
"json.schemas": [
  
]
```

 

Muốn chuyển đổi provider nhanh từ terminal? Xem CCS.

[ Tìm hiểu về CCS](/vi/guides/ccs)

