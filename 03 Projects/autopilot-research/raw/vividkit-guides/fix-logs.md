# Sửa Lỗi Từ Log - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/fix-logs

> Extracted from: fix-logs.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Sửa Lỗi Từ Log

Debug thông minh với /ck:fix — từ log lỗi đến code chạy được chỉ với một lệnh

##  Cách Hoạt Động

Khi có logs.txt, /ck:fix chuyển sang workflow phân tích log — pipeline 6 phase, mỗi phase dùng agent chuyên biệt.

1

Phân Tích Log

debugger agent đọc logs.txt

2

Tìm Code

Explore agents tìm vị trí lỗi

3

Lên Kế Hoạch

planner agent tạo chiến lược

4

Sửa Lỗi

Áp dụng fix vào source code

5

Kiểm Tra

tester agent xác nhận fix

6

Review

code-reviewer kiểm tra chất lượng

##  Bắt Đầu Nhanh

1

### 1. Ghi log ra file

Chuyển hướng output ứng dụng vào `logs.txt` để AI đọc được lỗi.

`npm run dev 2>&1 | tee logs.txt`

2

### 2. Tái tạo lỗi

Chạy ứng dụng và kích hoạt lỗi. Đảm bảo log lỗi được ghi vào logs.txt.

3

### 3. Chạy lệnh sửa

Yêu cầu AI phân tích logs:

`/ck:fix` Mention logs.txt trong prompt để trigger log-analysis workflow

Template:

`/ck:fix "analyze logs.txt and fix errors"`

##  Các Chế Độ

Chọn chế độ phù hợp với tình huống:

`--auto`

Tự động — auto-approve nếu chất lượng cao (mặc định)

Lỗi đơn giản/vừa, để AI xử lý

`--quick`

Nhanh: debug → fix → review

Type errors, lint, lỗi nhỏ

`--review`

Người duyệt — dừng ở mỗi bước

Code production/quan trọng, bảo mật

`--parallel`

Song song nhiều fullstack-developer agents

2+ lỗi độc lập trong logs

##  Ví Dụ Sử Dụng

`/ck:fix "analyze logs.txt and fix errors"` Full log analysis pipeline

`/ck:fix "check logs.txt for auth errors" --auto` Fix có focus, chế độ tự động

`/ck:fix "fix errors in logs.txt" --quick` Sửa nhanh lỗi đơn giản trong log

`/ck:fix "deploy pipeline error" --auto` Sửa CI/CD (thay /fix:ci)

##  Cài Đặt Ghi Log

Các cách capture log tùy theo stack:

Node.js / npm `npm run dev 2>&1 | tee logs.txt`

Python `python app.py 2>&1 | tee logs.txt`

Go `go run . 2>&1 | tee logs.txt`

Docker `docker compose up 2>&1 | tee logs.txt`

PowerShell `npm run dev *>&1 | Tee-Object logs.txt`

`tee` chỉ có sẵn trên macOS & Linux. Trên Windows, dùng `Tee-Object` trong PowerShell.

Mẹo Hay

Thêm log piping vĩnh viễn vào package.json scripts:

`"dev:log": "npm run dev 2>&1 | tee logs.txt"`

##  Mẹo

### Tập trung lỗi mới nhất

Debugger đọc 30 dòng cuối trước, rồi mở rộng nếu cần. Giữ logs.txt sạch — xóa trước khi tái tạo lỗi.

### Dùng tee, không redirect

`2>&1 | tee logs.txt` hiện output trên terminal VÀ ghi vào file. Redirect `>` ẩn terminal output.

### Quy tắc 3 lần

Nếu 3+ lần sửa thất bại, skill dừng lại và yêu cầu xem xét kiến trúc. Không loop vô hạn.

### Kết hợp với /ck:debug

Để điều tra sâu mà không auto-fix, dùng `/ck:debug` trước, rồi `/ck:fix` để áp dụng.

##  Lệnh Liên Quan

`/ck:fix --quick` Sửa nhanh lỗi type/lint

`/ck:fix --parallel` Sửa nhiều lỗi cùng lúc

`/ck:fix --review` Chế độ review từng bước

`/ck:debug` Điều tra sâu không auto-fix

