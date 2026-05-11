# Hướng Dẫn ClaudeKit CLI - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/cli

> Extracted from: cli.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Hướng Dẫn ClaudeKit CLI

Cài đặt ClaudeKit, chạy lệnh claude, và sử dụng các skill AI mạnh mẽ từ terminal của bạn!

ClaudeKit CLI là gì?

ClaudeKit CLI giúp bạn thiết lập ClaudeKit trong các dự án, sau đó bạn sử dụng Claude Code để nhận trợ giúp AI. Cài đặt ClaudeKit, chạy claude, và tận hưởng các skill mạnh mẽ như UI/UX Pro Max — tất cả từ terminal của bạn!

Quy trình làm việc nhanh

\$ ck init \# Thiết lập ClaudeKit trong dự án của bạn

\$ claude \# Bắt đầu Claude Code CLI

→ Sau đó chat với AI để xây dựng UI đẹp mắt ngay lập tức! 🎨

Lưu ý: ClaudeKit CLI là công cụ miễn phí giúp cài đặt các kit. Engineer Kit và Marketing Kit là sản phẩm trả phí cần mua riêng. [Mua ClaudeKit (Giảm 20%)](https://claudekit.cc/?ref=OMG49S8R)

##  Giao diện trong Terminal của bạn

Đây chính xác là những gì bạn sẽ thấy khi sử dụng ClaudeKit CLI

Terminal — bash — 80×24

 Phát lại

➜ ~/projects claude

Đang khởi động Claude Code CLI...

Nhập tin nhắn của bạn (hoặc /help để xem lệnh)

You: Using ui-ux-pro-max skill, tạo một landing page cho studio yoga

 AI đang suy nghĩ...

✓ Đang tìm kiếm domain sản phẩm: làm đẹp/sức khỏe

✓ Style guide: tối giản + thanh lịch

✓ Typography: Playfair Display + Inter

✓ Bảng màu: pastel nhẹ nhàng (#E8E5F2)

✓ Thiết Kế Hoàn Tất!

Đã tạo: yoga-studio-landing.html

\- Bảng màu hoa oải hương êm dịu

\- Typography Playfair Display thanh lịch

\- Thiết kế ưu tiên mobile responsive

\- Tuân thủ WCAG AA

 Các file được tạo trong thư mục hiện tại

➜ ~/projects ls -la

drwxr-xr-x 5 user staff 160 Dec 3 15:20 .

drwxr-xr-x 12 user staff 384 Dec 3 15:15 ..

-rw-r--r-- 1 user staff 8420 Dec 3 15:20 yoga-studio-landing.html

➜ ~/projects open yoga-studio-landing.html

 Đang mở trong trình duyệt mặc định...

→ Bạn đang ở trong Claude Code CLI. Cứ tiếp tục chat!

You:

Using ui-ux-pro-max skill, làm cho các nút nổi bật hơn với hiệu ứng hover

 AI:

Tôi sẽ cải thiện kiểu dáng nút với:

• Hiệu ứng chuyển đổi mượt mà (200ms)

• Hiệu ứng phóng to (hover:scale-105)

• Đổ bóng khi hover

• Chỉ báo con trỏ rõ ràng

✓ Đã cập nhật yoga-studio-landing.html

➜ ~/projects ▊

1

### Thiết Lập Dự Án

`ck init`

Khởi tạo ClaudeKit trong dự án của bạn (thiết lập một lần)

2

### Bắt Đầu Claude Code

`claude`

Mở trợ lý AI tương tác - chat và lặp lại

3

### Sử Dụng Skill

`Using ui-ux-pro-max skill...`

Bên trong Claude, kích hoạt trí tuệ thiết kế mạnh mẽ

##  Hướng Dẫn Bắt Đầu Nhanh

Khởi động ClaudeKit CLI trong 3 bước đơn giản

1

### Cài Đặt ClaudeKit CLI

Cài đặt công cụ ClaudeKit CLI toàn cục:

\$

npm install -g claudekit-cli

\# hoặc với bun

bun add -g claudekit-cli

\# Kiểm tra cài đặt

ck --version

2

### Khởi Tạo ClaudeKit trong Dự Án của Bạn

Điều hướng đến dự án của bạn và thiết lập ClaudeKit:

\$

cd ~/projects/my-project

ck init

\# Chế độ tương tác - làm theo hướng dẫn

\# Tạo thư mục .claude/ chứa các file ClaudeKit

💡 Chọn Cách Thiết Lập:

Khi chạy `ck init`, bạn sẽ thấy hai tùy chọn:

- **Global (Khuyên dùng):** Cài đặt cho tài khoản người dùng của bạn. Hoạt động mọi nơi.
- **Local:** Chỉ cài đặt cho thư mục dự án cụ thể này.

Chọn "Global" thường là dễ nhất!

⚙️ Xác Thực Thông Minh (CK CLI v3.16.0+):

ClaudeKit sử dụng xác thực đa lớp để tải kit từ private repository. Kiểm tra theo thứ tự:

- **1. Biến môi trường** - GITHUB_TOKEN hoặc GH_TOKEN (tốt nhất cho CI/CD)
- **2. GitHub CLI** - Nếu `gh` đã đăng nhập (khuyến nghị cho local)
- **3. OS Keychain** - Token đã lưu từ lần đăng nhập trước
- **4. Prompt Tương Tác** - Hướng dẫn bạn tạo và lưu token

`gh auth login` \# Khuyến nghị: Đăng nhập GitHub CLI trước

💡 **Git Clone Mode:** Dùng `ck init --use-git` để sử dụng git credentials có sẵn thay thế.

3

### Bắt Đầu Claude Code & Tạo Dự Án!

Khởi động Claude Code CLI và trò chuyện với AI:

\$

claude

\# Khởi động Claude Code CLI tương tác

Đang khởi động Claude Code CLI...

You: Using ui-ux-pro-max skill, tạo một landing page cho quán cà phê của tôi

 Vậy đó! AI sẽ tìm kiếm cơ sở dữ liệu thiết kế và tạo code đẹp mắt cho bạn.

##  Thói Quen Hàng Ngày

💡 Mẹo chuyên nghiệp: Chạy các lệnh này trước khi bắt đầu công việc để đảm bảo bạn luôn có các khả năng thông minh mới nhất.

### 1 Cập Nhật Công Cụ CLI

 

\$ ck update

\$ ck update --beta --yes

 

Đảm bảo `claudekit-cli` của bạn có các tính năng và bản sửa lỗi mới nhất.

💡 **Mẹo hay:** Chạy `ck update --beta --yes` để vừa update CLI vừa update Kit lên bản beta mới nhất, tự động cài dependencies.

### 2 Cập Nhật Engineer Kit

 

\$ ck init --kit engineer

Hoặc qua cờ global:

\$ ck init -g --kit engineer

 

Tự động hoàn toàn (không interactive):

\$ ck init -g --kit engineer --yes --install-skills

 

Cài bản beta mới nhất:

\$ ck init -g --kit engineer --yes --install-skills --beta

 

Cập nhật bộ kit `engineer` để lấy các prompt và khả năng AI mới nhất.

### 3 Cập Nhật Marketing Kit

 

\$ ck init --kit marketing

Hoặc qua cờ global:

\$ ck init -g --kit marketing

 

Tự động hoàn toàn (không interactive):

\$ ck init -g --kit marketing --yes --install-skills

 

Cài bản beta mới nhất:

\$ ck init -g --kit marketing --yes --install-skills --beta

 

Cập nhật bộ kit `marketing` cho sáng tạo nội dung, viết quảng cáo, và tài sản thương hiệu.

CÔNG CỤ MẠNH MẼ

## CCS - Claude Code Switch

Cần chuyển đổi giữa tài khoản công việc/cá nhân hoặc sử dụng các mô hình rẻ hơn như Gemini/GLM? CCS là một công cụ wrapper mạnh mẽ cho Claude Code giúp bạn tiết kiệm tiền và hợp lý hóa quy trình làm việc.

Cảnh Báo: Ban Tài Khoản Google

Google đang tích cực ban các tài khoản sử dụng Antigravity/Gemini OAuth với công cụ bên thứ ba (OpenCode, các công cụ dựa trên CLIProxy như CCS/ProxyPal, AntigravityManager, v.v.). Điều này có thể vi phạm ToS của Google và dẫn đến mất quyền truy cập vĩnh viễn vào các dịch vụ Google. Cân nhắc sử dụng GLM hoặc Kimi như các lựa chọn an toàn hơn.

 Tiết kiệm ~80% chi phí  Đa tài khoản  Ủy quyền nhanh

[Xem Hướng Dẫn CCS ](/vi/guides/ccs)

## Nâng cao: Cấu hình settings.json

Tùy chỉnh Claude Code toàn cục hoặc cục bộ bằng cách tạo một file `settings.json` (ví dụ: `~/.claude/settings.json`).

###  Global Settings

`~/.claude/settings.json`

Applies everywhere across all projects

###  Local Settings

`.claude/settings.json`

Overwrites global settings for this specific project

Luôn bao gồm tham chiếu `"$schema"` để kích hoạt tính năng tự động hoàn thành và xác thực trong trình soạn thảo của bạn:

 

``` text-[#E6E6E6]

}
```

**Lưu ý Chuyển đổi:** Nếu trước đây bạn đã sử dụng `includeCoAuthoredBy`, tính năng này hiện đã được thay thế bằng cấu hình `attribution`:

"includeCoAuthoredBy": true

"attribution": 

####  Lưu Trữ Trạng Thái Phiên (Session State)

Claude Code hiện tự động lưu trạng thái phiên của bạn qua các lần khởi động lại. Trạng thái này được lưu tại thư mục `.claude/session-state/`.

####  Thay Đổi Namespace

Các kỹ năng cốt lõi đã được chuyển qua namespace `ck:` để dễ dàng sử dụng và tổ chức gọn gàng hơn.

Thay vì dùng lệnh `/debug` hoặc `/plan`, hiện tại bạn nên dùng `/ck:debug` và `/ck:plan`.

### Cấu Hình .ck.json

Tất cả các cài đặt có sẵn cho file cấu hình `.ck.json`.

 Vị Trí File

Cấp dự án (ưu tiên hơn global, được khuyên dùng):

.claude/.ck.json (project)

Toàn cầu (áp dụng cho tất cả dự án):

  macOS 

  Linux 

  Windows 

` ~/.claude/.ck.json `

Default .ck.json Configuration

 

``` text-[#E6E6E6]
,
  "plan": -",
    "dateFormat": "YYMMDD",
    "validation": 
  },
  "locale": ,
  "project": ,
  "gemini": ,
  "skills": 
  }
}
```

| Cài đặt | Mặc định | Mô tả |
|----|----|----|
| codingLevel | -1 (auto) | Experience level for tailored output (-1=auto, 0-5) |
| statusline | "full" (Beta) / "minimal" (Stable) | Status bar display mode ("minimal" or "full") |
| privacyBlock | true | Block access to .env and sensitive files |
| docs.maxLoc | 800 | Max lines of code for doc generation |
| plan.namingFormat | "-" | Plan directory naming pattern |
| plan.dateFormat | "YYMMDD" | Date format in plan names |
| plan.validation.mode | "prompt" | Plan validation mode |
| plan.validation.questions | "3-8" | Number of validation questions |
| locale.responseLanguage | null | Response language (null = English) |
| project.type | "auto" | Project type detection |
| project.packageManager | "auto" | Package manager detection |
| gemini.model | "gemini-3-flash-preview" | Default Gemini model for research |
| skills.research.useGemini | true | Use Gemini for research tasks |

### Mẹo Chuyên Nghiệp cho Người Dùng CLI Nâng Cao

Sử Dụng Dấu Ngoặc Kép cho Yêu Cầu Nhiều Từ

Luôn bọc yêu cầu của bạn trong dấu ngoặc kép: "yêu cầu của bạn ở đây"

Tham Chiếu File với @

Sử dụng `@tên_file` để cho AI biết những file nào cần sửa đổi

Cấu Hình Statusline & Gemini Model

- `statusline`: đặt thành `"minimal"` hoặc `"full"` (hiển thị đầy đủ)
- `gemini.model`: mặc định là `gemini-3-flash-preview`
- Tự động lưu lại ngữ cảnh đang làm việc vào thư mục `.claude/session-state/` để không bị mất khi bạn tắt terminal

Cấu hình trong `.ck.json`.

