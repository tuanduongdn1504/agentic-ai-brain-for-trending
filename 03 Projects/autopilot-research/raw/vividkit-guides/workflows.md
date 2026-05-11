# Quy Trình Mẫu - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/workflows

> Extracted from: workflows.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Quy Trình Mẫu

Chuỗi lệnh sẵn dùng cho các tác vụ phát triển thông dụng.

Mới với ClaudeKit?

Các quy trình này bao gồm các chuỗi lệnh hoạt động cùng nhau để hoàn thành các tác vụ phổ biến. Hoàn hảo để bắt đầu!

##  Quy Trình Mẫu

  Engineer Kit 

  Marketing Kit 

### Getting Started

 3 quy trình 

### Xây Dựng Feature Mới

Beginner

Tốt nhất cho: Thêm feature mới vào app của bạn

  ~15-30 phút    4 bước 

1

`/ck:brainstorm` Brainstorm ý tưởng

Dùng /ck:brainstorm hoặc nói "brainstorm ideas for \[feature\]" để khám phá

2

`/ck:plan` Tạo implementation plan

AI tạo plan chi tiết từng bước để build feature

3

 Review → /clear → Implement

Review plan, chạy /clear để giải phóng context (bắt buộc), rồi implement

4

`/ck:cook @plan.md` Implement plan

AI viết code theo plan, chạy tests và review công việc

/clear bắt buộc sau /ck:plan trước /ck:cook

### Quick Implementation

Intermediate

Tốt nhất cho: Features nhỏ khi bạn biết mình muốn gì

  ~10-20 phút    1 bước 

1

`/ck:cook "nhiệm vụ của bạn"` All-in-one skill

AI tự động research, plan, implement, test và review feature

/ck:cook "nhiệm vụ của bạn" tự động làm gì:

-  Research best practices và technologies
-  Tạo và execute implementation plan
-  Viết và test code
-  Review quality và best practices

 /ck:cook Flags

`--interactive`

Từng bước rà soát (mặc định)

`--fast`

Bỏ qua research, code luôn

`--parallel`

Chạy agent song song

`--auto`

Tự động duyệt mọi bước

`--no-test`

Không bắt buộc test

`--tdd` Beta

Viết test trước theo từng phase, dùng chung với mọi mode khác

--interactive là mặc định, dùng native Claude Tasks API.

### Bootstrap Project Mới

Advanced

Tốt nhất cho: Tạo app hoàn chỉnh từ đầu

  ~1-2 giờ    1 bước 

1

`/ck:bootstrap "mô tả ứng dụng của bạn"` Full project setup

AI build toàn bộ project: research, architecture, design, implementation và docs

/ck:bootstrap "mô tả ứng dụng của bạn" tự động làm gì:

-  Research và chọn tech stack
-  Project structure và architecture
-  UI/UX design và wireframes
-  Full implementation với tests
-  Comprehensive documentation

Warning: Command này dùng nhiều AI tokens

### Design & Frontend

 4 quy trình 

### Tạo Diagram Excalidraw

Intermediate

Tốt nhất cho: Tạo diagram phong cách hand-drawn với hình dạng phản ánh ý nghĩa thực sự

  ~5-15 phút    1 bước 

1

`/excalidraw` Tạo diagram

Tạo diagram Excalidraw hand-drawn từ text prompt — architecture, flowcharts, system designs

/excalidraw tự động làm gì:

-  Phong cách hand-drawn với bảng màu semantic
-  Auto-diagram: visualization codebase không cần config
-  File-based workflow với Playwright rendering
-  MCP canvas workflow để chỉnh sửa trực tiếp

Hỗ trợ auto-diagram: phân tích codebase bất kỳ và tự động tạo architecture diagram

### Diagram Publication (tech-graph)

Intermediate Beta

Tốt nhất cho: Tạo SVG diagram chất lượng publication cho docs, slides, blog post

  ~5-15 phút    1 bước 

1

`/ck:tech-graph "<topic hoặc system>"` Tạo SVG diagram

Render SVG chất lượng publication với 7 design style (modern, minimal, neon, retro,...) và 10 template (architecture, sequence, ER, flowchart, state-machine, timeline, comparison-matrix, use-case, agent-architecture, data-flow)

/ck:tech-graph "\<topic hoặc system\>" tự động làm gì:

-  7 design style: flat-icon, dark-terminal, blueprint, notion-clean, glassmorphism, claude-official, openai
-  10 diagram template gồm cả agent-architecture và data-flow
-  Built-in SVG layout best-practices (spacing, arrow routing, z-index)
-  Output sẵn sàng cho docs/slides/blog post, không cần cleanup thủ công

Kết hợp với /ck:preview --diagram để visual self-review (auto-detect collision, label overlap, arrow routing issue)

### Frontend Design Aesthetics

Advanced

Tốt nhất cho: Tạo các giao diện frontend nổi bật, chuẩn production, tránh phong cách AI chung chung

  ~30-60 phút    4 bước 

1

`/ck:ui-ux-pro-max` Design Intelligence

Phân tích tham chiếu thiết kế và system styling với kiến thức chuyên môn UX/UI

2

 Cổng Bắt Buộc

Xác định Purpose, Tone, Constraints và Differentiation trước khi code để có phong cách BOLD.

3

 Kiểm Soát Thẩm Mỹ

Cỡ chữ \>= 16px cho inputs, thiết kế mobile-first và dùng Google Fonts chuẩn hỗ trợ Tiếng Việt.

4

`/ck:frontend-design` Triển Khai Giao Diện

Code UI với cá tính mạnh thông qua điều chỉnh các thông số Design Dials.

/ck:frontend-design tự động làm gì:

-  Kiểm soát Design Dials (Sự biến đổi, mật độ, motion)
-  Tuân thủ chặt chẽ cổng ràng buộc Design Thinking
-  Quy tắc Motion: CSS-only (HTML) hoặc Motion (React)
-  Thiết kế thẩm mỹ vượt trên chuẩn mặc định chung

Anti-slop typography yêu cầu các Google Fonts đang trending hỗ trợ tiếng Việt tốt (như Inter, Outfit).

### Thiết Kế UI với AI (Stitch)

Intermediate

Tốt nhất cho: Tạo thiết kế UI độ trung thực cao từ text prompt qua Google Stitch

  ~5-15 phút    3 bước 

1

`/ck:stitch generate "prompt"` Tạo thiết kế

Tạo thiết kế UI từ text prompt bằng Google Stitch AI

2

`/ck:stitch export --format all` Export assets

Export dạng Tailwind/HTML + DESIGN.md spec để implement

3

`/ck:frontend-design` Implement components

Xây dựng React components từ design spec đã export

/ck:stitch generate "prompt" tự động làm gì:

-  Text-to-UI design qua Google Stitch API
-  Export sang Tailwind/HTML và DESIGN.md
-  Pipeline design-to-code với các skill hiện có
-  Hỗ trợ layout mobile, desktop và tablet
-  Hạn mức: 200 credits/ngày (Flash), 50/ngày (Pro)

Cài Stitch MCP server trong .claude/.mcp.json để tích hợp trực tiếp

### Debugging & Fixes

 4 quy trình 

### Sửa Lỗi (Bug Fix)

Beginner

Tốt nhất cho: Chẩn đoán và sửa lỗi có cấu trúc

  ~10-20 phút    6 bước 

1

`/ck:fix` Pipeline 6 bước

Chạy pipeline đầy đủ: Scout → Chẩn đoán → Đánh giá → Sửa → Xác minh → Phòng ngừa

2

 ① Scout

Thu thập bằng chứng — logs, stack traces, files bị ảnh hưởng

3

 ② Chẩn đoán → ③ Đánh giá

Phân tích root cause dựa trên bằng chứng, sau đó đánh giá mức độ nghiêm trọng

4

 ④ Sửa lỗi

Áp dụng fix có mục tiêu dựa trên root cause đã chẩn đoán

5

 ⑤ Xác minh

Chạy tests để xác nhận fix hoạt động và không có regression

6

 ⑥ Phòng ngừa

Thêm guards, tests, hoặc documentation để ngăn tái phát

 /ck:fix Flags

`--auto`

Tự động apply fix không cần xác nhận

`--review`

Review fix trước khi apply

`--quick`

Fix nhanh không phân tích sâu

`--parallel`

Fix nhiều issues song song

/ck:fix v2.0: RCA dựa trên bằng chứng. Flags: --auto, --review, --quick, --parallel

### Security Audit

Intermediate

Tốt nhất cho: Tìm lỗ hổng bảo mật và secrets

  ~15-25 phút    3 bước 

1

`/ck:security-scan` Quét lỗ hổng

Quét codebase tìm OWASP issues, hardcoded secrets và dependency vulnerabilities

2

`/ck:code-review --security` Review bảo mật chi tiết

Review code sâu tập trung vào authentication, authorization và data handling

3

`/ck:fix --security` Apply security fixes

AI áp dụng các fix bảo mật được đề xuất với giải thích chi tiết

/ck:security-scan tự động làm gì:

-  Phát hiện hardcoded secrets
-  Quét dependency vulnerability
-  Bao phủ OWASP Top 10
-  Đề xuất security fixes

Phát hiện SQL injection, XSS, CSRF và các OWASP Top 10 issues

### Tạo Test Scenarios

Beginner

Tốt nhất cho: Khám phá edge case toàn diện trước khi implement hoặc test

  ~5-10 phút    1 bước 

1

`/ck:scenario` Phân tích 12 chiều

Phân tách feature theo 12 chiều để tạo test scenarios toàn diện

/ck:scenario tự động làm gì:

-  Phân tách feature theo 12 chiều
-  Khám phá edge case và boundary condition
-  Tạo test scenarios với độ ưu tiên
-  Tích hợp với /ck:test để thực thi

Dùng trước khi viết test để đảm bảo coverage đầy đủ edge cases

### STRIDE Security Audit

Intermediate

Tốt nhất cho: Phân tích bảo mật STRIDE + OWASP toàn diện với auto-fix tùy chọn

  ~10-20 phút    1 bước 

1

`/ck:security` STRIDE audit

STRIDE threat modeling + OWASP scan với phân loại severity và auto-fix tùy chọn

/ck:security tự động làm gì:

-  STRIDE threat modeling framework
-  OWASP vulnerability pattern matching
-  Phân loại severity và ưu tiên
-  Auto-fix lặp đi lặp lại tùy chọn theo pattern /ck:loop

Kết hợp với /ck:security-scan để coverage vulnerability + threat toàn diện

### Planning & Review

 6 quy trình 

### Code Review với Edge Cases

Intermediate

Tốt nhất cho: Review code kỹ lưỡng với scout edge cases

  ~20-30 phút    4 bước 

1

`/ck:cook @plan.md` Implement plan

AI viết code theo plan với auto test & review cycles

2

`/ck:scout` Scout edge cases

AI scout các file bị ảnh hưởng, luồng dữ liệu, error paths và boundary conditions

3

 Code-reviewer review

Code-reviewer subagent review findings từ scout và đánh giá chất lượng code

4

`/ck:git cm` Merge & commit

Commit code đã review với conventional commit message

/ck:scout tự động làm gì:

-  Phát hiện edge case qua /ck:scout
-  Phân tích boundary conditions
-  Scout luồng dữ liệu & error paths
-  Tích hợp code-reviewer tự động

/ck:scout tích hợp code-reviewer để phát hiện edge cases trước review

### Plan + Validate + Implement

Intermediate

Tốt nhất cho: Plan đã validate với auto-propagate decisions

  ~20-40 phút    4 bước 

1

`/ck:plan` Tạo plan

AI tạo plan triển khai chi tiết với các phases

2

`/ck:plan validate` Validate quyết định plan

Validation gate kiểu phỏng vấn. Quyết định tự động propagate xuống phase files

3

 /clear (bắt buộc)

Giải phóng context trước khi implement. Bước bắt buộc

4

`/ck:cook @plan.md` Implement plan đã validate

AI implement với decisions đã validate sẵn propagate vào mỗi phase

/ck:plan validate tự động làm gì:

-  Validate plan kiểu phỏng vấn
-  Tự động propagate xuống phase files
-  Decisions đã validate hướng dẫn implementation
-  Giảm rework từ quyết định plan không rõ ràng

 /ck:plan Flags

`--hard`

Plan phức tạp nhiều phase với red-team review

`--deep` Beta

Phân tích sâu: danh sách file, kịch bản test, sơ đồ phụ thuộc theo phase

`--parallel`

Plan thiết kế cho agent chạy song song

`--two`

Plan 2 phase (plan → implement)

`--tdd` Beta

Viết test trước theo phase, dùng chung với mọi flag khác

`validate`

Cổng validation kiểu phỏng vấn

`red-team`

Spawn adversarial reviewers

/ck:plan validate decisions tự propagate xuống phase files

### Red-Team Plan Review

Advanced

Tốt nhất cho: Tìm lỗ hổng trong plan trước khi implement

  ~10-20 phút    2 bước 

1

`/ck:plan --hard "feature"` Tạo plan

Tạo plan chi tiết. Hard/parallel/two modes tự động chạy red-team sau khi tạo

2

`/ck:plan red-team plans/` Review đối kháng

Spawn hostile reviewers: Bảo mật, Failure Mode, Phá giả định, Phê bình Scope

/ck:plan --hard "feature" tự động làm gì:

-  Security Adversary (auth bypass, injection, OWASP)
-  Failure Mode Analyst (race conditions, mất dữ liệu)
-  Assumption Destroyer (deps ẩn, claims sai)
-  Scope & Complexity Critic (over-engineering, YAGNI)

Tự scale reviewers theo độ phức tạp plan (2-4 adversarial lenses)

### Nghiên Cứu & Port Tính Năng (Xia)

Advanced

Tốt nhất cho: Phân tích và port tính năng từ repos GitHub bên ngoài vào dự án của bạn an toàn

  ~10-30 phút    3 bước 

1

`/ck:xia <repo> --compare` Phân tích mã nguồn

So sánh song song kiến trúc source repo, pattern, và feature implementation

2

`/ck:xia <repo> [feature] --improve` Port & refactor

Sao chép tính năng từ source và refactor để phù hợp với local codebase

3

`/ck:test` Validate port

Chạy tests để verify tính năng đã port hoạt động đúng trong local context

/ck:xia \<repo\> --compare tự động làm gì:

-  Phân tích bất kỳ GitHub repo hay thư mục local nào
-  Đánh giá quyết định qua Challenge framework
-  AI tự tạo bảng ma trận đánh đổi (trade-offs) và điểm rủi ro trước khi thực thi

 /ck:xia Flags

Mode

`--compare`

Chỉ mổ xẻ và so sánh kiến trúc song song

`--copy`

Bê y nguyên cấu trúc gốc sang, sửa tối thiểu để chạy

`--improve`

Copy cấu trúc nhưng AI sẽ refactor và dọn anti-patterns

`--port`

Chỉ lấy ý tưởng, code lại bằng chuẩn local stack (Mặc định)

Speed

`--fast`

Bỏ qua research & validation, tiến hành auto-approve

`--auto`

Giữ nguyên luồng làm việc nhưng tự động approve các gates

`Mặc định`

Chạy workflow đầy đủ với các cổng cần phê duyệt

Nên chạy --compare trước để đánh giá sự tương thích của kiến trúc trước khi port

### Điều Hướng Knowledge Graph

Intermediate

Tốt nhất cho: Hiểu codebase lạ qua phân tích cấu trúc trước khi lập kế hoạch

  ~5-15 phút    2 bước 

1

`/ck:graphify` Build graph

Phân tích codebase với tree-sitter AST, tạo visualization tương tác + report

2

`/ck:plan` Lập kế hoạch với context

Dùng GRAPH_REPORT.md để hiểu kiến trúc trước khi tạo implementation plan

/ck:graphify tự động làm gì:

-  Hỗ trợ 20+ ngôn ngữ qua tree-sitter AST
-  Visualization HTML tương tác với search
-  Report god nodes và surprising connections
-  Tiết kiệm 71.5x token so với raw file context

Dùng --watch để cập nhật incremental khi code. MCP mode expose graph cho Claude truy vấn trực tiếp.

### Dự Đoán Impact Trước Khi Code

Intermediate

Tốt nhất cho: Phát hiện vấn đề architecture, security, performance trước khi implement

  ~5-10 phút    1 bước 

1

`/ck:predict` 5 chuyên gia tranh luận

5 persona chuyên gia tranh luận về thay đổi — architect, security, performance, UX, ops

/ck:predict tự động làm gì:

-  5 persona chuyên gia với góc nhìn riêng
-  Phân tích architecture, security, performance
-  Đánh giá tác động UX và ops
-  Báo cáo đồng thuận với xếp hạng rủi ro

Chạy trước feature lớn hoặc refactor rủi ro để phát hiện vấn đề sớm

### Research & Docs

 3 quy trình 

### Visual Documentation

Beginner

Tốt nhất cho: Tạo giải thích trực quan, sơ đồ và slide deck dạng Markdown hoặc HTML độc lập

  ~2-10 phút    3 bước 

1

`/ck:preview --explain "chủ đề"` Giải thích Markdown

Tạo sơ đồ ASCII + Mermaid kèm giải thích (mở trong novel-reader UI)

2

`/ck:preview --html --explain "chủ đề"` Giải thích HTML

HTML độc lập với theme toggle, Mermaid v11 và Chart.js — mở thẳng trên trình duyệt

3

`/ck:preview --html --slides "chủ đề"` Slide deck HTML

Slide trình bày chất lượng cao dạng HTML độc lập

/ck:preview tự động làm gì:

-  Markdown: --explain, --slides, --diagram, --ascii
-  HTML: --html --explain, --html --slides, --html --diagram
-  HTML-only: --diff, --plan-review, --recap
-  Theme toggle (sáng/tối) trong mọi trang HTML
-  Sơ đồ Mermaid v11 + biểu đồ dữ liệu Chart.js

Thêm --html vào bất kỳ mode nào để có output HTML chất lượng cao. Còn có: --diagram, --diff, --plan-review, --recap

### Research & Documentation

Beginner

Tốt nhất cho: Nghiên cứu topic và tạo tài liệu kỹ thuật

  ~10-20 phút    3 bước 

1

`/ck:research "topic"` Deep research

AI nghiên cứu topic kỹ lưỡng bằng web search và documentation

2

`/ck:docs-seeker "library"` Tìm docs thư viện

Tìm kiếm documentation chính thức qua llms.txt để lấy API info mới nhất

3

`/ck:docs` Tạo docs project

Tạo hoặc cập nhật documentation dựa trên phân tích codebase

/ck:research tự động làm gì:

-  Web search và tổng hợp
-  Tra cứu documentation thư viện
-  Tạo documentation project
-  Hỗ trợ viết technical docs

/ck:docs-seeker dùng context7 để lấy docs thư viện mới nhất

### Tạo LLMs.txt

Beginner

Tốt nhất cho: Làm cho project dễ đọc với các AI/LLM tools

  ~5-10 phút    1 bước 

1

`/ck:llms [path]` Tạo index

Tạo llms.txt theo chuẩn llmstxt.org — giúp AI đọc hiểu docs của bạn dễ dàng

/ck:llms \[path\] tự động làm gì:

-  Tuân theo chuẩn llmstxt.org
-  Tạo từ docs, README hoặc codebase
-  Bao gồm reference files và cấu trúc tổng quan
-  Hoạt động với mọi loại project

/ck:llms tạo llms.txt chuẩn hóa để AI tools có thể hiểu nhanh codebase của bạn

### Shipping

 3 quy trình 

### DevOps & Deployment

Advanced

Tốt nhất cho: Thiết lập CI/CD và deployment pipelines

  ~20-40 phút    3 bước 

1

`/ck:devops "setup CI/CD"` Cấu hình DevOps

Thiết lập CI/CD pipelines cho GitHub Actions, GitLab CI hoặc platforms khác

2

`/ck:deploy` Deploy lên platform

Deploy lên Cloudflare, Vercel, GCP hoặc Kubernetes với auto-detection

3

`/ck:test --e2e` Chạy E2E tests

Verify deployment với end-to-end tests

/ck:devops tự động làm gì:

-  Tạo CI/CD pipeline
-  Deploy đa platform
-  Cấu hình environment
-  Setup rollback và monitoring

Hỗ trợ Docker, Kubernetes, serverless và container deployments

### Ship Feature

Intermediate

Tốt nhất cho: Ship feature branch với test, review và tạo PR tự động

  ~5-10 phút    1 bước 

1

`/ck:ship [--official|--beta] [--skip-tests] [--skip-review]` Ship pipeline

Merge main, chạy test, review pre-landing, bump version, cập nhật changelog, push, tạo PR

/ck:ship \[--official\|--beta\] \[--skip-tests\] \[--skip-review\] tự động làm gì:

-  Hỗ trợ chế độ official (→main) và beta (→dev)
-  Merge origin/main (hoặc dev cho beta) trước khi test
-  Tự nhận diện npm/pytest/cargo/go test
-  Review code 2 pass + adversarial review (giai đoạn 3)
-  Bump version và cập nhật CHANGELOG.md
-  Tạo PR với summary, kết quả test và linked issues

/ck:ship tự nhận diện test runner, format version file và changelog style

### Deploy Ứng Dụng

Intermediate

Tốt nhất cho: Deploy lên Vercel, Netlify, Railway, Fly.io, AWS, GCP và nhiều hơn

  ~5-15 phút    1 bước 

1

`/ck:deploy [platform]` Auto-deploy

AI tự nhận diện project type và deploy lên 15+ nền tảng mà không cần cấu hình thủ công

/ck:deploy \[platform\] tự động làm gì:

-  Tự nhận diện project type (Next.js, Astro, Express, ...)
-  Hỗ trợ 15+ nền tảng sẵn có
-  Xử lý env vars và cấu hình build
-  Vercel, Netlify, Railway, Fly.io, AWS, GCP, Azure

/ck:deploy tự nhận diện stack và xử lý biến môi trường, build steps và cấu hình platform

### Backend & Infra

 2 quy trình 

### Database Operations

Intermediate

Tốt nhất cho: Thiết kế schema database và migrations

  ~15-30 phút    3 bước 

1

`/ck:databases "schema design"` Thiết kế schema

Thiết kế schema database với relationships, indexes và constraints

2

`/ck:plan "migration"` Plan migration

Tạo plan migration an toàn với rollback strategy

3

`/ck:cook @plan.md` Execute migration

Implement migration với proper error handling và validation

/ck:databases tự động làm gì:

-  Thiết kế schema với relationships
-  Tối ưu hóa index
-  Tạo migration script
-  Phân tích query performance

Hỗ trợ MongoDB, PostgreSQL, MySQL và SQLite

### Agentize Codebase Của Bạn

Intermediate

Tốt nhất cho: Chuyển đổi code hiện có thành CLI tools và MCP servers thân thiện với AI agent

  ~15-30 phút    3 bước 

1

`/ck:agentize --both` Tạo CLI + MCP

Wrap codebase thành CLI tool và MCP server với module core/ dùng chung

2

 Tối ưu cho AI

Output ngắn gọn, error actionable, workflow được consolidate — thiết kế cho LLM tiêu thụ

3

`/ck:deploy` Deploy lên cloud

Deploy lên Cloudflare Workers, Docker, hoặc các platform được hỗ trợ

/ck:agentize --both tự động làm gì:

-  Module core/ dùng chung cho CLI + MCP
-  Định dạng output thân thiện với agent
-  Thông báo lỗi actionable cho LLMs
-  Deploy lên Cloudflare Workers hoặc Docker

Dùng --mcp cho MCP-only hoặc --cli cho CLI-only. Mặc định --both tạo shared core/

### Media & Creative

 2 quy trình 

### Tạo Video Content

Intermediate

Tốt nhất cho: Tạo video lập trình với React

  ~20-40 phút    2 bước 

1

`/ck:remotion` Video creation

Tạo video lập trình với React và Remotion

2

`render` Render output

Export ra MP4, GIF hoặc image sequences

/ck:remotion tự động làm gì:

-  Animations và transitions
-  Text animations và captions
-  3D graphics integration
-  Audio synchronization

Tạo video compositions dựa trên React

### Showcase & Nội Dung Mạng Xã Hội

Beginner

Tốt nhất cho: Tạo trang HTML showcase đẹp mắt cho demo, bài viết, và mạng xã hội

  ~5-10 phút    1 bước 

1

`/ck:show-off` Tạo showcase

Tạo trang HTML nhiều section với parallax, chuyển đổi theme, nội dung song ngữ (VI/EN), và tự động chụp screenshots

/ck:show-off tự động làm gì:

-  Layout cuộn nhiều section với hiệu ứng parallax
-  Tự động chuyển đổi theme (system/light/dark)
-  Chụp screenshot song song ở nhiều tỷ lệ khung hình

Xuất screenshots ở tỷ lệ 16:9, 9:16, và 1:1 — sẵn sàng cho các nền tảng mạng xã hội

### Session & Management

 1 quy trình 

### Sprint Retrospective

Beginner

Tốt nhất cho: Review sprint dựa trên dữ liệu git metrics, chỉ số sức khỏe và đề xuất hành động

  ~2-5 phút    1 bước 

1

`/ck:retro [timeframe] [--compare] [--team] [--format html|md]` Phân tích sprint

Thu thập git metrics (commits, LOC, hotspots, churn), tính chỉ số sức khỏe, tạo báo cáo retrospective

/ck:retro \[timeframe\] \[--compare\] \[--team\] \[--format html\|md\] tự động làm gì:

-  Git metrics: commits/ngày, LOC thêm/xóa, file hotspots
-  Chỉ số sức khỏe: churn rate, test ratio, active day ratio
-  So sánh với kỳ trước bằng --compare
-  Phân tích theo tác giả với --team
-  Xuất định dạng HTML hoặc Markdown

/ck:retro 2w --compare --team tạo retro 2 tuần với so sánh kỳ trước và phân tích theo tác giả

### Advanced

 2 quy trình 

### Agent Teams (Song Song)

Advanced

Tốt nhất cho: Tác vụ lớn với nhiều agent chạy song song

  ~30-60 phút    2 bước 

1

`/ck:plan --hard "feature"` Tạo plan với phases

Tạo plan chi tiết với các phase có thể chạy song song cho team execution

2

`/ck:team cook @plan` Team chạy song song

Spawn nhiều dev agent song song, mỗi agent xử lý một phase. Auto test → review → merge

/ck:plan --hard "feature" tự động làm gì:

-  Nhiều dev agent song song (--devs N)
-  Pipeline tự động test → review → merge
-  Event-driven hooks + agent memory
-  Còn có: /ck:team research, /ck:team review, /ck:team debug

 /ck:team Flags

`--devs N`

Số lượng dev agent song song (mặc định: 2)

`--tester`

Thêm tester agent riêng

`--reviewer`

Thêm code reviewer agent

`--worktree`

Mỗi agent chạy trong git worktree riêng

Cần CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 trong settings.json

### Isolated Feature Branching

Intermediate

Tốt nhất cho: Phát triển song song trong các monorepos sử dụng git worktrees

  ~2-5 phút    3 bước 

1

`/ck:worktree info` Bước 1: Lấy thông tin Repo

Phân tích loại repo, base branch và các projects hiện có

2

Bước 2: Detect Branch Naming Mode

Nhận diện theo quy ước thông thường hoặc dùng --no-prefix cho key Jira chính xác

3

 Bước 3: Chuyển đổi thành Slug

Định dạng branch name thành kebab-case (hoặc bỏ qua nếu bật cờ --no-prefix)

/ck:worktree tự động làm gì:

-  Git worktrees độc lập cho từng tính năng
-  Giữ nguyên chính xác issue keys (--no-prefix)
-  Khả năng tự động nhận diện branch prefix
-  Hỗ trợ dự án có cấu trúc monorepo

Sử dụng cờ --no-prefix để giữ nguyên tên branch chính xác cho các Jira key (như ND-1377-cleanup-docs).

### Mẹo Chuyên Nghiệp

Tiết kiệm token với /clear

Sử dụng `/clear` để xóa lịch sử cuộc trò chuyện trước khi bắt đầu triển khai

Tham chiếu file với @

Sử dụng `@plan.md` để tham chiếu các file cụ thể trong lệnh

Dùng /ck:cook để triển khai

Sau khi lên kế hoạch với `/ck:plan`, chạy `/clear` rồi `/ck:cook` để triển khai plan của bạn

Scout trước khi code

Sử dụng `/ck:scout` để tìm nhanh các file liên quan trong codebase của bạn

Debug trước khi sửa

Sử dụng `/ck:debug` trước để tìm nguyên nhân gốc rễ, sau đó dùng `/ck:fix` khi đã sẵn sàng

Luôn bắt đầu với /ck:plan

Tạo một kế hoạch có cấu trúc trước, sau đó sử dụng `/ck:cook` để triển khai

Agent behavioral checklists

Các skill bao gồm behavioral checklists hướng dẫn agent ra quyết định — xem docs của skill để biết thêm

### Hướng Dẫn Liên Quan

[](/vi/guides/commands)

`Bảng Lệnh Nhanh` 

Tham khảo đầy đủ các commands với mức độ phức tạp

[](/vi/guides/flowchart)

`Tìm Lệnh Phù Hợp` 

Sơ đồ quyết định tương tác để chọn command

Cần thêm quy trình? Xem [tài liệu đầy đủ từ trang web chính thức của ClaudeKit](https://docs.claudekit.cc/docs/workflows).

### Content & Copy

 2 quy trình 

### Viết & Đăng Bài Blog

Beginner

Tốt nhất cho: Tạo nội dung blog tối ưu SEO từ đầu

  ~20-30 min    4 bước 

1

`/ckm:write:good "topic"` Nghiên cứu & soạn thảo

AI nghiên cứu chủ đề, phân tích đối thủ, và soạn nội dung tối ưu SEO

2

`/ckm:seo audit` Tối ưu SEO

Kiểm tra mật độ keyword, meta tags, và tối ưu tìm kiếm

3

`/ckm:write:enhance` Nâng cấp & hoàn thiện

Cải thiện khả năng đọc, thêm CTA, và tối ưu engagement

4

`/ckm:write:publish` Đăng nội dung

Định dạng cho CMS, thêm hình ảnh, và chuẩn bị xuất bản

/ckm:write:good "topic" tự động làm gì:

-  Phân tích nội dung đối thủ
-  Tích hợp keyword SEO
-  Tối ưu khả năng đọc
-  Định dạng sẵn cho CMS

Dùng /ckm:write:good cho nội dung chất lượng cao; /ckm:write:fast cho bản nháp nhanh

### Tạo Chuỗi Email

Intermediate

Tốt nhất cho: Xây dựng campaign email nurture tự động

  ~30-45 min    4 bước 

1

`/ckm:persona` Xác định đối tượng

Tạo buyer persona để nhắm mục tiêu thông điệp hiệu quả

2

`/ckm:email flow "welcome"` Thiết kế email flow

Tạo chuỗi tự động với timing và trigger phù hợp

3

`/ck:copywriting` Viết copy

Tạo subject line hấp dẫn và nội dung email thuyết phục

4

`/ckm:email sequence` Tạo chuỗi

Xuất chuỗi email hoàn chỉnh với các biến thể A/B

/ckm:persona tự động làm gì:

-  Nhắm đối tượng theo buyer persona
-  Thiết lập trigger tự động
-  Biến thể A/B testing
-  Xuất file sẵn cho ESP

Thêm biến thể A/B testing cho subject line để tối ưu tỷ lệ mở email

### Campaign & Analytics

 2 quy trình 

### Triển Khai Campaign Marketing

Advanced

Tốt nhất cho: Lập kế hoạch và thực thi campaign đa kênh

  ~45-60 min    5 bước 

1

`/ckm:marketing-planning` beta Lập chiến lược

Xác định mục tiêu campaign, KPI, timeline, và phân bổ ngân sách

2

`/ckm:campaign create` Tạo campaign

Thiết lập cấu trúc campaign với các kênh và thông điệp

3

`/ckm:content-marketing` beta Tạo nội dung

Tạo tài nguyên campaign trên tất cả các kênh

4

`/ckm:social schedule` Lên lịch phân phối

Lập kế hoạch và lên lịch nội dung trên các nền tảng social

5

`/ckm:analytics` beta Thiết lập tracking

Cấu hình analytics và theo dõi conversion

/ckm:marketing-planning tự động làm gì:

-  Phối hợp đa kênh
-  Lập kế hoạch phân bổ ngân sách
-  Tạo lịch nội dung
-  Thiết lập theo dõi hiệu suất

Dùng /ckm:campaign status để theo dõi hiệu suất trong quá trình chạy campaign

### Thiết Lập A/B Testing

Intermediate

Tốt nhất cho: Thử nghiệm các biến thể để tối ưu tỷ lệ conversion

  ~20-30 min    4 bước 

1

`/ckm:funnel analyze` Xác định điểm nghẽn

Phân tích funnel hiện tại để tìm cơ hội tối ưu

2

`/ckm:ab-test-setup` beta Thiết kế test

Tạo hypothesis, biến thể, và chỉ số đánh giá

3

`/ckm:plan cro` Kế hoạch triển khai

Tạo kế hoạch chi tiết để thực thi bài test

4

`/ckm:analyze report` Phân tích kết quả

Phân tích thống kê và đưa ra khuyến nghị

/ckm:funnel analyze tự động làm gì:

-  Xây dựng hypothesis
-  Thiết kế biến thể
-  Tính toán độ tin cậy thống kê
-  Triển khai phiên bản thắng

Chạy test tối thiểu 2 tuần để có kết quả có ý nghĩa thống kê

### SEO & Growth

 2 quy trình 

### Thực Hiện SEO Audit

Beginner

Tốt nhất cho: Phân tích toàn diện sức khỏe website và SEO

  ~15-25 min    3 bước 

1

`/ckm:seo audit "url"` Audit kỹ thuật

Phân tích cấu trúc site, tốc độ, thân thiện mobile, và khả năng crawl

2

`/ckm:seo keywords "niche"` Nghiên cứu keyword

Khám phá keyword giá trị cao và content gap

3

`/ckm:competitor seo "url"` Phân tích đối thủ

Phân tích thứ hạng và hồ sơ backlink của đối thủ

/ckm:seo audit "url" tự động làm gì:

-  Checklist SEO kỹ thuật
-  Bản đồ cơ hội keyword
-  Phân tích content gap đối thủ
-  Danh sách ưu tiên hành động

Chạy audit hàng tháng để theo dõi tiến độ SEO và phát hiện vấn đề sớm

### Tối Ưu Landing Page

Intermediate

Tốt nhất cho: Cải thiện tỷ lệ conversion trên landing page

  ~25-35 min    4 bước 

1

`/ckm:funnel analyze "url"` Phân tích hiệu suất

Xem xét chỉ số hiện tại, bounce rate, và luồng người dùng

2

`/ckm:form-cro "url"` beta Tối ưu form

Tối ưu trường form, CTA, và các điểm gây ma sát

3

`/ck:copywriting` Tối ưu copy

Cải thiện headlines, value proposition, và yếu tố thuyết phục

4

`/ckm:plan cro` Tạo kế hoạch CRO

Ghi lại thay đổi và thiết lập tracking cho các cải tiến

/ckm:funnel analyze "url" tự động làm gì:

-  Phân tích heatmap
-  Tối ưu trường form
-  Biến thể A/B cho copy
-  Theo dõi conversion

Tập trung tối ưu từng điểm một để đo lường tác động chính xác

### Design & Creative

 3 quy trình 

### Tạo Marketing Assets

Intermediate

Tốt nhất cho: Tạo bộ visual assets đồng nhất cho campaign

  ~30-45 min    4 bước 

1

`/ckm:brand review` Xem xét brand guidelines

Tải màu sắc, font chữ, và hướng dẫn phong cách brand

2

`/ckm:design-system` beta Hệ thống thiết kế

Tạo thư viện component phù hợp với brand

3

`/ckm:design banner` beta Tạo assets

Tạo banner, quảng cáo, và đồ họa khuyến mãi

4

`/ckm:assets-organizing` beta Tổ chức assets

Sắp xếp và xuất assets cho các nền tảng khác nhau

/ckm:brand review tự động làm gì:

-  Thiết kế nhất quán với brand
-  Xuất nhiều kích thước
-  Định dạng theo từng nền tảng
-  Tổ chức thư viện asset

Dùng /ckm:brand create để thiết lập brand guidelines trước nếu chưa có

### Thiết Kế Đồ Họa Social

Beginner

Tốt nhất cho: Tạo visual hấp dẫn cho social media

  ~15-25 min    3 bước 

1

`/ckm:design social` beta Tạo đồ họa

Tạo đồ họa social media tối ưu cho từng nền tảng

2

`/ck:copywriting` Viết caption

Tạo caption hấp dẫn kèm hashtag phù hợp

3

`/ckm:social schedule` Lên lịch đăng bài

Lập lịch đăng bài để tối ưu engagement

/ckm:design social tự động làm gì:

-  Kích thước theo từng nền tảng
-  Nhất quán với brand
-  Tạo caption tự động
-  Gợi ý hashtag

Mỗi nền tảng có kích thước hình ảnh tối ưu riêng — /ckm:design tự động định dạng

### Tạo Diagram Excalidraw

Beginner

Tốt nhất cho: Trực quan hóa marketing funnel, campaign flow, và chiến lược nội dung theo phong cách hand-drawn

  ~5-15 phút    1 bước 

1

`/excalidraw` beta Tạo diagram

Tạo diagram Excalidraw hand-drawn — marketing funnel, campaign flow, lịch content, bản đồ đối thủ

/excalidraw tự động làm gì:

-  Phong cách hand-drawn với bảng màu semantic
-  Marketing funnel, campaign flow, content map
-  Auto-diagram: visualization codebase không cần config
-  File-based workflow với Playwright rendering

Chế độ auto-diagram có thể phân tích cấu trúc project và tự động tạo diagram kiến trúc

### Strategy & Research

 2 quy trình 

### Phân Tích Đối Thủ

Intermediate

Tốt nhất cho: Hiểu rõ bức tranh cạnh tranh và cơ hội thị trường

  ~25-35 min    4 bước 

1

`/ckm:competitor list` Xác định đối thủ

Khám phá đối thủ trực tiếp và gián tiếp trong lĩnh vực

2

`/ckm:competitor analyze "url"` Phân tích chuyên sâu

Phân tích định vị, thông điệp, và giá trị độc đáo

3

`/ckm:competitor content` Audit nội dung

Phân tích chiến lược content, chủ đề, và engagement

4

`/ckm:marketing-research` beta Insight thị trường

Tổng hợp kết quả thành các insight có thể hành động

/ckm:competitor list tự động làm gì:

-  Bản đồ đối thủ cạnh tranh
-  Phân tích định vị
-  Xác định content gap
-  Ma trận cơ hội

Theo dõi 3-5 đối thủ chính đều đặn để có thông tin cạnh tranh liên tục

### Xây Dựng Kế Hoạch Marketing

Advanced

Tốt nhất cho: Tạo chiến lược marketing toàn diện

  ~40-60 min    5 bước 

1

`/ckm:persona` Xác định persona

Tạo buyer persona chi tiết và phân khúc khách hàng

2

`/ckm:marketing-research` beta Nghiên cứu thị trường

Phân tích xu hướng thị trường, quy mô, và cơ hội

3

`/ckm:funnel design` Thiết kế funnel

Vẽ bản đồ hành trình khách hàng và các điểm conversion

4

`/ckm:marketing-planning` beta Kế hoạch chiến lược

Tạo tài liệu chiến lược marketing toàn diện

5

`/ckm:dashboard` Thiết lập tracking

Cấu hình dashboard KPI và báo cáo

/ckm:persona tự động làm gì:

-  Phát triển persona
-  Chiến lược kênh phân phối
-  Phân bổ ngân sách
-  Khung KPI

Xem xét và cập nhật kế hoạch marketing mỗi quý để đạt kết quả tốt nhất

### Playbook & Orchestration

 1 quy trình 

### Chạy Marketing Playbook

Intermediate

Tốt nhất cho: Điều phối campaign marketing end-to-end với template, mục tiêu, và gợi ý thông minh

  ~30-60 min    4 bước 

1

`/ckm:play create --template saas-launch` beta Tạo playbook

Chọn từ các template: saas-launch, product-hunt-launch, content-engine, campaign-sprint

2

`/ckm:play goals set` beta Đặt mục tiêu

Xác định KPI và target — tích hợp với chỉ số GA4, GSC, Stripe

3

`/ckm:play next` beta Bước tiếp theo thông minh

AI gợi ý hành động có tác động cao nhất dựa trên khoảng cách mục tiêu và trạng thái bước

4

`/ckm:play status` beta Theo dõi tiến độ

Dashboard tổng quan tất cả bước, mục tiêu, và điểm nghẽn

/ckm:play create --template saas-launch tự động làm gì:

-  Định tuyến dependency-graph giữa các bước
-  Quality gate cho các checkpoint phê duyệt thủ công
-  Theo dõi mục tiêu tích hợp GA4/GSC/Stripe
-  Gợi ý thông minh dựa trên khoảng cách mục tiêu
-  4 template tích hợp: SaaS launch, Product Hunt, content engine, campaign sprint

Dùng /ckm:play learn để ghi lại insight sau khi hoàn thành mỗi bước

### Video & Media

 3 quy trình 

### Thiết Kế YouTube Thumbnails

Beginner

Tốt nhất cho: Tạo YouTube thumbnails tối ưu CTR với AI generation

  ~10-20 min    3 bước 

1

`/ckm:youtube-thumbnail-design` beta Thiết kế thumbnail

AI tạo thumbnail hoàn chỉnh có text qua Gemini Pro (lên đến 4K)

2

`/ck:ai-multimodal` Xem xét & tinh chỉnh

Phân tích thumbnail đã tạo và cải thiện theo phản hồi

3

`/ckm:assets-organizing` beta Tổ chức file xuất

Sắp xếp thumbnail theo video slug với quy tắc đặt tên biến thể

/ckm:youtube-thumbnail-design tự động làm gì:

-  17 phong cách art direction với đánh giá tác động CTR
-  Hướng dẫn theo niche: tech, gaming, education, cooking, fitness, business
-  Tạo hàng loạt biến thể cho A/B testing
-  Hỗ trợ ảnh khuôn mặt tham chiếu để đồng nhất brand
-  Hỗ trợ Google Font và overlay mũi tên

17 phong cách art direction: facecam, mystery, bold-text, before-after, và nhiều hơn

### Viết Script & Storyboard Video

Intermediate

Tốt nhất cho: Lập kế hoạch pre-production cho nội dung video

  ~25-40 min    3 bước 

1

`/ckm:video script "topic"` Viết script

Tạo script video với hook, nội dung chính, và CTA

2

`/ckm:video storyboard` Tạo storyboard

Phân cảnh chi tiết từng shot kèm thời lượng

3

`/ckm:elevenlabs speak` beta Tạo voiceover

Tạo giọng đọc AI từ script

/ckm:video script "topic" tự động làm gì:

-  Tối ưu hook mở đầu
-  Phân cảnh chi tiết
-  Hướng dẫn timing
-  Tùy chọn voiceover AI

Giữ video dưới 2 phút cho social media; dưới 10 phút cho YouTube

### Sản Xuất Video Content

Advanced

Tốt nhất cho: Quy trình sản xuất video đầy đủ

  ~45-60 min    4 bước 

1

`/ckm:video script` Script & lập kế hoạch

Tạo script và kế hoạch sản xuất

2

`/ckm:video create` Tạo video

Tạo video với sự hỗ trợ AI hoặc hướng dẫn chỉnh sửa

3

`/ckm:youtube social` Cắt clip

Tạo clip social media từ nội dung dài

4

`/ckm:seo keywords "video"` Tối ưu metadata

Tạo tiêu đề, mô tả, và tag SEO

/ckm:video script tự động làm gì:

-  Quy trình sản xuất đầy đủ
-  Tạo clip social
-  Tối ưu SEO
-  Xuất đa nền tảng

Dùng /ckm:youtube blog để chuyển đổi video thành bài blog

### Mẹo Chuyên Nghiệp

Tiết kiệm token với /clear

Sử dụng `/clear` để xóa lịch sử cuộc trò chuyện trước khi bắt đầu triển khai

Tham chiếu file với @

Sử dụng `@plan.md` để tham chiếu các file cụ thể trong lệnh

Dùng /ck:cook để triển khai

Sau khi lên kế hoạch với `/ck:plan`, chạy `/clear` rồi `/ck:cook` để triển khai plan của bạn

Scout trước khi code

Sử dụng `/ck:scout` để tìm nhanh các file liên quan trong codebase của bạn

Debug trước khi sửa

Sử dụng `/ck:debug` trước để tìm nguyên nhân gốc rễ, sau đó dùng `/ck:fix` khi đã sẵn sàng

Luôn bắt đầu với /ck:plan

Tạo một kế hoạch có cấu trúc trước, sau đó sử dụng `/ck:cook` để triển khai

Agent behavioral checklists

Các skill bao gồm behavioral checklists hướng dẫn agent ra quyết định — xem docs của skill để biết thêm

### Hướng Dẫn Liên Quan

[](/vi/guides/commands)

`Bảng Lệnh Nhanh` 

Tham khảo đầy đủ các commands với mức độ phức tạp

[](/vi/guides/flowchart)

`Tìm Lệnh Phù Hợp` 

Sơ đồ quyết định tương tác để chọn command

Cần thêm quy trình? Xem [tài liệu đầy đủ từ trang web chính thức của ClaudeKit](https://docs.claudekit.cc/docs/workflows).

