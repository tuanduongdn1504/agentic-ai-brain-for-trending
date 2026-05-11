# Migrate ClaudeKit sang Công cụ AI Khác - VividKit Documentation | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/migrate

> Extracted from: migrate.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Chuyển ClaudeKit sang Công cụ Khác

Một lệnh. Toàn bộ agents, skills, rules — ở mọi nơi.

`ck migrate` giúp bạn mang toàn bộ cấu hình ClaudeKit (agents, commands, skills, config, rules, hooks) sang bất kỳ AI coding tool nào khác, với tính năng so sánh thông minh.

###  Bắt đầu nhanh

Chọn item để cài

`ck migrate --install`

 

Xem trước kế hoạch reconcile

`ck migrate -a codex --dry-run`

 

Giữ nguyên các mục đã xóa

`ck migrate --respect-deletions`

 

Sang Cursor

`ck migrate --agent cursor`

 

Sang tất cả

`ck migrate --all`

 

Chỉ config + rules

`ck migrate --all --config --rules`

 

###  Nội dung được migrate

 Agents

 Commands

 Skills

 Config (CLAUDE.md)

 Rules (.claude/rules/)

 Hooks (.claude/hooks/)

### Hướng dẫn từng bước

Dành cho mọi người

Hướng dẫn này dành cho người không chuyên về kỹ thuật. Chỉ cần copy-paste lệnh — không cần biết lập trình.

1

#### Đảm bảo đã cài ClaudeKit (ck)

Mở terminal và kiểm tra ck có sẵn không:

ck --version

Nếu thấy số phiên bản, bạn sẵn sàng rồi. Nếu không, hãy vào vividkit.cc/guides để cài ClaudeKit trước.

2

#### Chạy lệnh migrate

Thay \<tool\> bằng tên công cụ đích:

\# Tự động phát hiện tool đã cài\
ck migrate

\# Tool cụ thể\
ck migrate --agent cursor\
ck migrate --agent antigravity\
ck migrate --agent windsurf

**Mẹo:** Dùng --dry-run trước để xem trước kết quả mà không ghi file.

3

#### Trả lời các câu hỏi

Công cụ sẽ hỏi một vài câu (chọn provider, cài project hay global, xử lý conflict thế nào). Dùng mũi tên để chọn và Enter để xác nhận. Để bỏ qua tất cả và dùng mặc định:

ck migrate --all --yes

✓

#### Xong! Mở công cụ đích của bạn

Agents, rules và config đã được cài vào định dạng của công cụ mới. Mở Cursor, Windsurf hoặc công cụ bạn chọn — nội dung đã sẵn sàng.

###  Quá trình migrate hoạt động như thế nào

 Bước 1 

#### Khám phá

Đọc toàn bộ thư mục .claude/ để thu thập agents, commands, skills, rules, hooks và config — tạo danh sách đầy đủ trước khi thực hiện bất kỳ thay đổi nào.

 Bước 2 

#### Chọn Provider

Phát hiện các công cụ đã cài trên máy. Bạn có thể chỉ định với --agent \<name\> hoặc migrate tất cả cùng lúc bằng --all.

 Bước 3 

#### So sánh & lên kế hoạch

Dùng checksum để so sánh nội dung nguồn và đích. Tạo kế hoạch rõ ràng: file nào cần cài mới, cập nhật, bỏ qua hoặc xóa — không đoán mò.

 Bước 4 

#### Thực thi

Chuyển đổi nội dung sang định dạng từng provider (vd: .cursorrules, .windsurfrules), ghi file vào đúng vị trí và merge hook config mà không làm mất cấu hình cũ.

 Bước 5 

#### Tổng kết

In báo cáo rõ ràng về những gì đã cài, bỏ qua hoặc thất bại.

###  Công cụ được hỗ trợ

| Công cụ | Agents | Commands | Skills | Config | Rules | Hooks | Flag |
|----|----|----|----|----|----|----|----|
| OpenCode |  |  |  |  |  | — | `--agent opencode` |
| Cursor |  | — |  |  |  | — | `--agent cursor` |
| Windsurf |  |  |  |  |  | — | `--agent windsurf` |
| GitHub Copilot |  | — |  |  |  | — | `--agent github-copilot` |
| Antigravity | — |  |  |  |  | — | `--agent antigravity` |
| Cline |  | — |  |  |  | — | `--agent cline` |
| Roo |  | — |  |  |  | — | `--agent roo` |
| Codex |  |  |  |  |  |  | `--agent codex` |
| Kilo |  | — |  |  |  | — | `--agent kilo` |
| Kiro |  | — |  |  |  | — | `--agent kiro` |
| Droid |  |  |  |  |  |  | `--agent droid` |
| Goose |  | — |  |  |  | — | `--agent goose` |
| OpenHands |  | — |  |  |  | — | `--agent openhands` |
| Gemini CLI |  |  |  |  |  |  | `--agent gemini-cli` |
| Amp |  | — |  |  |  | — | `--agent amp` |

###  Hai chế độ: Install và Reconcile

ck migrate tự động chọn chế độ phù hợp dựa trên trạng thái registry. Bạn cũng có thể chỉ định bằng tay.

`--install` Chọn cài đặt

Chọn tương tác từng agent/command/skill/hook để cài. Mặc định khi registry trống hoặc checksum không xác định.

`--reconcile` Reconcile

So sánh với registry rồi áp dụng đúng các thay đổi (cài mới/cập nhật/bỏ qua/xóa). Mặc định khi registry hợp lệ.

`--reinstall-empty-dirs`

Cài lại các mục khi thư mục type của chúng trống/thiếu (mặc định: bật).

`--respect-deletions`

Giữ nguyên thư mục trống — bỏ qua heuristic auto-reinstall khi bạn đã chủ đích xóa các mục.

Lưu ý

- --install và --reconcile loại trừ nhau — chỉ truyền một
- --reinstall-empty-dirs và --respect-deletions loại trừ nhau
- --force ghi đè quyết định skip theo từng mục; --reinstall-empty-dirs là heuristic theo từng thư mục

###  Xử lý Xung đột

Khi file đích đã bị chỉnh sửa bên ngoài, ck migrate sẽ đưa ra lựa chọn:

Ghi đè

Thay thế hoàn toàn bằng nội dung nguồn

Merge thông minh

Cố gắng merge thay đổi của bạn với nguồn

Bỏ qua

Giữ nguyên file hiện tại

Xem diff

Xem sự khác nhau trước khi quyết định

**Tự động xử lý:** Thêm --yes để bỏ qua mọi câu hỏi conflict và dùng mặc định an toàn. Thêm --force để cài lại mọi thứ kể cả đã bị xóa hay chỉnh sửa.

 Tham khảo tất cả Options

#### Options chế độ

|  |  |
|----|----|
| `--install` | Chế độ chọn item để cài (tương tác) |
| `--reconcile` | Chế độ reconcile (so sánh với registry) |
| `--reinstall-empty-dirs` | Cài lại khi thư mục type trống (mặc định: bật) |
| `--respect-deletions` | Giữ nguyên các mục đã xóa — bỏ qua auto-reinstall |

#### Options chọn đích

|                          |                                          |
|--------------------------|------------------------------------------|
| `-a, --agent <provider>` | Công cụ đích (có thể dùng nhiều lần)     |
| `--all`                  | Migrate sang tất cả provider được hỗ trợ |
| `-g, --global`           | Cài globally thay vì project             |
| `-y, --yes`              | Bỏ qua tất cả câu hỏi xác nhận           |
| `-f, --force`            | Cài lại mọi thứ kể cả đã xóa/chỉnh sửa   |
| `--dry-run`              | Xem trước kế hoạch, không ghi file       |

#### Chọn nội dung migrate

|                   |                                                       |
|-------------------|-------------------------------------------------------|
| `--only-agents`   | Chỉ migrate agents                                    |
| `--only-commands` | Chỉ migrate commands                                  |
| `--only-skills`   | Chỉ migrate skills                                    |
| `--config`        | Chỉ migrate CLAUDE.md                                 |
| `--rules`         | Chỉ migrate .claude/rules/                            |
| `--hooks`         | Chỉ migrate .claude/hooks/                            |
| `--skip-agents`   | Bỏ qua migrate agents                                 |
| `--skip-commands` | Bỏ qua migrate commands                               |
| `--skip-skills`   | Bỏ qua migrate skills (giữ symlinks/layout tùy chỉnh) |
| `--skip-config`   | Bỏ qua migrate config                                 |
| `--skip-rules`    | Bỏ qua migrate rules                                  |
| `--skip-hooks`    | Bỏ qua migrate hooks                                  |
| `--source <path>` | Đường dẫn CLAUDE.md tùy chỉnh                         |

###  Hướng dẫn liên quan

[](/vi/guides/ide-config)

Hướng dẫn Cấu hình IDE

Cấu hình VS Code dùng provider thay thế

[](/vi/guides/ccs)

Hướng dẫn CCS

Chuyển đổi provider từ terminal

