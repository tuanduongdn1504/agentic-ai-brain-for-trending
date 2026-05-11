# Claude Code Remote Control - VividKit Documentation | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/remote-control

> Extracted from: remote-control.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



 /remote-control

## Remote Control — Điều khiển từ xa

Code trên điện thoại. Tiếp tục trên laptop. Chuyển đổi tức thì.

Tính năng chính thức của Claude Code cho phép bạn tiếp tục session đang chạy trên máy tính từ điện thoại, tablet hoặc bất kỳ trình duyệt nào.

### Yêu cầu

Tài khoản trả phí

Pro / Max / Team / Enterprise

Đăng nhập claude.ai

Không hỗ trợ API key

Chạy claude trước

Chấp nhận workspace trust 1 lần trong project

### Cách bật Remote Control

1

Cách 1: Server mode (nhiều session) — Chạy server, hiển thị URL + QR code để kết nối

claude remote-control

2

Cách 2: Bắt đầu session với remote — Mở session Claude Code kèm remote control ngay

claude --remote-control "My Project"

3

Cách 3: Trong session đang chạy — Gõ lệnh này trong Claude Code đang chạy để bật remote

/remote-control \# or shorthand: /rc

4

Bật vĩnh viễn (mọi session) — Dùng /config để bật remote control cho tất cả session tương lai

/config \# Set: remoteControl: true

### Kết nối từ thiết bị khác

1.  1 Chạy một trong các lệnh bật ở trên — URL và QR code sẽ xuất hiện trong terminal.
2.  2 Trên điện thoại/tablet: scan QR code hoặc mở URL trực tiếp.
3.  3 Hoặc mở claude.ai/code → tìm session theo tên (icon máy tính màu xanh).
4.  4 Nhấn Spacebar để hiện/ẩn QR code khi dùng claude remote-control.

### Giới hạn cần biết

-  Không hỗ trợ API key — phải đăng nhập qua claude.ai
-  Terminal phải chạy liên tục — đóng terminal = kết thúc session
-  Mất mạng \> 10 phút → session timeout tự động
-  Ultraplan và Remote Control không thể chạy cùng lúc

[ Tài liệu chính thức Remote Control](https://code.claude.com/docs/en/remote-control) [ Về Mobile Coding](/vi/guides/mobile-coding)

