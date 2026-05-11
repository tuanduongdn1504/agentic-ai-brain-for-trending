# Cách ClaudeKit Hoạt Động - VividKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/how-ck-works

> Extracted from: how-ck-works.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



# Cách ClaudeKit Hoạt Động

ClaudeKit không phải là một phần mềm độc lập hay IDE mới. Nó là một bộ khung (Framework) nâng cao được tích hợp thẳng vào cấu hình native (.claude) của Claude Code trên máy bạn, biến terminal chat thành một hệ thống tự động hóa tác vụ chuyên nghiệp.

### 1. Hooks (Hệ thống ngầm)

Các script chạy lót nền tự động. Khởi tạo config, rules dự án mà bạn không cần copy-paste thủ công mỗi lần.

### 2. Skills (Kiến thức có sẵn)

Các gói kiến thức chuyên biệt (SKILL.md) kèm prompt, references và scripts. Là đơn vị thực thi chính khi bạn gõ /ck:\*.

### 3. Agents (Các chuyên gia)

Các mô hình được thiết lập riêng (Planner, Tester, Reviewer) với prompt và tool nội bộ, tập trung vào 1 chuyên môn.

### 4. Workflows (Quy trình)

Tổ hợp các Hooks, Skills và Agents chạy nối tiếp nhau từ lệnh nhập của bạn để xử lý luồng việc phức tạp trọn gói.

Cùng xem chi tiết cách Hooks, Skills, Agents và Workflows điều phối một lệnh thực tế. Chọn quy trình bên dưới và nhấn Play để khám phá cơ chế bên trong.

 Lệnh Riêng Lẻ Riêng Lẻ

  Engineer Kit 4 

  Marketing Kit 0 

 `/ck:brainstorm`   

 `/ck:plan`   

 `/ck:cook`   

 `/ck:fix`   

### Hướng dẫn sắp ra mắt...

VividKit đang hoàn thiện hướng dẫn chi tiết cho Marketing Kit.

 

 Quick Ref

Engineer Kit

Marketing Kit

### 

 bước • 

   

 

Không có combos cho kit này

### Hướng dẫn sắp ra mắt...

VividKit đang hoàn thiện hướng dẫn chi tiết cho Marketing Kit.

### 

  

 Đóng

Bước  /    Đang chạy... 

 

# /ck:brainstorm

Brainstorm giải pháp với phân tích trade-off và thẳng thắn. Design-first, không code.

 HARD GATE:   Không code, không scaffolding, không triển khai cho đến khi design được trình bày và user duyệt. Áp dụng cho mọi phiên làm việc. 

## QUY TRÌNH

1

Khảo sát

Đọc docs dự án & code patterns

2

Khám phá

Hỏi làm rõ qua AskUser

3

Phạm vi

Phân tách nếu 3+ vấn đề độc lập

4

Nghiên cứu

Agents nghiên cứu song song + web search

5

Phân tích

Đánh giá 2-3 hướng với pros/cons

6

Tranh luận

Thách thức giả định, trình bày options

7

Đồng thuận

Thống nhất hướng đi

8

Báo cáo

Viết báo cáo markdown

9

Tiếp?

Hỏi: tạo plan? → /plan

### Nguyên Tắc Cốt Lõi

- › **YAGNI** — Đừng xây thứ chưa cần
- › **KISS** — Giữ cho đơn giản
- › **DRY** — Không lặp lại code
- › Ưu tiên thẳng thắn, không vòng vo
- › Thách thức mọi giả định

### Lĩnh Vực Chuyên Môn

- › Kiến trúc hệ thống & khả năng mở rộng
- › Đánh giá & giảm thiểu rủi ro
- › Tối ưu UX/DX
- › Quản lý technical debt
- › Xác định bottleneck hiệu năng

## SKILL & AGENT STACK

Skills và agents được sử dụng trong phiên làm việc:

  planner agent   docs-manager agent   WebSearch   ck:scout   ck:docs-seeker   ck:ai-multimodal   ck:sequential-thinking   psql 

  Agent    Skill    Tool   • Tất cả tuỳ chọn — kích hoạt theo context 

## ĐẦU RA

### Báo cáo tổng hợp Markdown

  plans/reports/  ` brainstorm-YYMMDD-HHMM-slug.md `

  Mô tả vấn đề   Các hướng đánh giá   Khuyến nghị cuối   Rủi ro triển khai   Metrics thành công   Bước tiếp theo 

# /ck:plan

Lập kế hoạch triển khai với phases nghiên cứu, review red-team, và hydrate tasks. Tạo phase files có thể hành động.

## QUY TRÌNH

1

Kiểm tra

Kiểm tra Plan Context + plan đang hoạt động

2

Chế độ

Tự động phát hiện hoặc flag rõ ràng

3

Nghiên cứu

Spawn researcher agents

4

Phân tích

Đọc docs, scout codebase

5

Lập kế hoạch

Viết plan.md + phase files

6

Red Team

Review đối kháng (2-4 reviewers)

7

Xác thực

Phỏng vấn câu hỏi quan trọng

8

Hydrate

Tạo Claude Tasks từ phases

9

Bàn giao

Xuất lệnh /cook

## CHẾ ĐỘ LÀM VIỆC

| Flag | Chế độ | Nghiên cứu | Red Team | Xác thực | Cook Flag |
|----|----|----|----|----|----|
|   --auto  | Tự động | Follows mode | Follows mode | Follows mode | Follows mode |
|   --fast  | Nhanh | Skip | Skip | Skip | --auto |
|   --hard  | Khó | 2 researchers | Yes | Optional | — |
|   --deep  | Sâu | 3+ scouts/phase | Yes | Forced | — |
|   --parallel  | Song song | 2 researchers | Yes | Optional | --parallel |
|   --two  | Hai hướng | 2+ researchers | After select | After select | — |

 --tdd (tests-first mỗi phase) và --no-tasks (bỏ qua task hydration) có thể kết hợp với bất kỳ mode nào.

## HOẠT ĐỘNG ĐẶC BIỆT

### ` red-team `

2-4 code-reviewer agents thách thức giả định của plan, tìm điểm mù, test edge cases. Chạy /plan red-team.

### ` validate `

Phỏng vấn câu hỏi quan trọng (3-8 câu). Đảm bảo plan đầy đủ trước khi triển khai.

### ` archive `

Viết nhật ký ghi lại quyết định. Lưu trữ plans hoàn thành/bỏ dở để tham khảo.

# /ck:cook

Engine triển khai theo plans, chạy tests, đơn giản hóa code, và review chất lượng. Công cụ chính của ClaudeKit.

## QUY TRÌNH

1

Ý định

Phát hiện mode từ input

2

Nghiên cứu

Scout codebase (bỏ nếu fast)

3

Lập kế hoạch

Tạo plan.md + phases

4

Triển khai

Thực thi tasks theo phase

5

Test

Chạy tests qua tester agent

6

Review

Code review qua reviewer agent

7

Hoàn tất

Sync plan + docs + commit

### Nguyên Tắc Cốt Lõi

- › Theo plan chính xác
- › Test trước review
- › Delegate cho subagents (tester, reviewer)
- › Không bỏ qua kiểm tra chất lượng
- › Hoàn tất với docs + commit

### Lĩnh Vực Chuyên Môn

- › Triển khai full-stack
- › Test-driven development
- › Điều phối subagents
- › Đảm bảo chất lượng
- › Quản lý Git workflow

## SKILL & AGENT STACK

Skills và agents được sử dụng trong phiên làm việc:

  tester agent   code-reviewer agent   code-simplifier agent   git-manager agent   ck:scout   ck:test   ck:code-review 

  Agent    Skill    Tool   • Tất cả tuỳ chọn — kích hoạt theo context 

## ĐẦU RA

### Triển khai hoàn tất

` Commits + trạng thái plan cập nhật `

  Code changes đã commit   Tests pass   Quality đã review   Plan phases đánh dấu hoàn thành 

# /ck:fix

Pipeline debug có cấu trúc với phân tích nguyên nhân gốc, triển khai sửa lỗi, và phòng ngừa regression.

## QUY TRÌNH

1

Khảo sát

Thu thập bằng chứng: logs, stack traces

2

Chẩn đoán

Phân tích nguyên nhân gốc (không đoán)

3

Định tuyến

Đánh giá độ phức tạp → workflow

4

Sửa

Triển khai sửa lỗi

5

Xác minh

Chạy tests + thêm regression test

6

Hoàn tất

Docs + commit + journal

### Nguyên Tắc Cốt Lõi

- › Tìm nguyên nhân gốc, không phải triệu chứng
- › Một bug, một commit
- › Luôn thêm regression test
- › Ghi lại bản sửa
- › Không bỏ qua test thất bại

### Lĩnh Vực Chuyên Môn

- › Phân tích nguyên nhân gốc
- › Kỹ thuật debug
- › Mở rộng test coverage
- › Patterns xử lý lỗi
- › Phân tích log

## SKILL & AGENT STACK

Skills và agents được sử dụng trong phiên làm việc:

  debugger agent   tester agent   ck:scout   ck:test   ck:sequential-thinking 

  Agent    Skill    Tool   • Tất cả tuỳ chọn — kích hoạt theo context 

## ĐẦU RA

### Báo cáo sửa lỗi

` Tóm tắt inline + commit `

  Nguyên nhân gốc xác định   Sửa lỗi triển khai   Tests pass   Regression test thêm 

## Pipeline

  

 Next

 Reset

  /  

 spawned by main agent

![](data:image/svg+xml;base64,PHN2ZyB4LWJpbmQ6Y2xhc3M9IiYjMzk7dy02IGgtNiAmIzM5OyArIGdldENvbG9yQ2xhc3Moc3RlcC5jb2xvciwgJiMzOTtpY29uVGV4dCYjMzk7KSIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgeC1odG1sPSJzdGVwLmljb24iIGRhdGEtYXN0cm8tY2lkLTdrbGlhYWloPjwvc3ZnPg==)

 

![](data:image/svg+xml;base64,PHN2ZyB4LWJpbmQ6Y2xhc3M9IiYjMzk7dy01IGgtNSAmIzM5OyArIChjb2xvck1hcFtnZXRBY3RpdmVTdGVwKCkuY29sb3JdPy5pY29uVGV4dCB8fCAmIzM5OyYjMzk7KSIgZmlsbD0ibm9uZSIgdmlld2JveD0iMCAwIDI0IDI0IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgeC1odG1sPSJnZXRBY3RpdmVTdGVwKCkuaWNvbiIgZGF0YS1hc3Ryby1jaWQtYmI0YnhuaXc+PC9zdmc+)

#### 

1 2 3

``` text-xs
```

Phím tắt: Space = Play/Pause · ← → = Bước trước/sau

## Bạn đã sẵn sàng để trải nghiệm?

[ Cài đặt ClaudeKit ngay](/vi/guides/cli) [ Khám phá tất cả Lệnh](/vi/guides/commands)

