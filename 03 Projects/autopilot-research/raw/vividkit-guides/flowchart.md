# Quy Trình Chọn Command - VividKit Documentation | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/flowchart

> Extracted from: flowchart.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Tìm Lệnh Phù Hợp

Hướng dẫn toàn diện để chọn command phù hợp dựa trên use case của bạn.

##  Chọn Bộ Công Cụ

  Engineer Kit 

  Marketing Kit 

###  Sơ Đồ Quyết Định Tương Tác

Click vào bất kỳ node hoặc đường path nào để highlight lộ trình đến command. Hoặc click vào các command button ở trên để xem đường đi tương ứng.

BETA

 

 

### Danh sách Commands

Chọn để xem đường dẫn

BETA 

### 

BETA

Click vào nút hoặc đường path để highlight lộ trình. Click vào command ở trên để xem path.

###  Khởi Tạo Dự Án Mới

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:bootstrap` | Khởi tạo dự án đầy đủ với research, tech stack, planning, design, implementation | Bắt đầu dự án hoàn toàn mới |
| `/ck:docs init` | Phân tích codebase và tạo documentation | Tham gia dự án có sẵn hoặc setup docs |

** Mẹo:** New Project Flow: /bootstrap → tự động xử lý mọi thứ bao gồm Git init, tech stack research, wireframes và initial implementation.

###  Xây Dựng Feature

#### Chưa biết muốn gì

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:brainstorm` | Ideation với lời khuyên chuyên gia | Khám phá ý tưởng, validate approaches, xem pros/cons |

** Quan trọng:** /brainstorm KHÔNG implement - chỉ tư vấn. Sau khi brainstorm, dùng /ck:plan hoặc /ck:cook để implement.

** Quan trọng:** /brainstorm KHÔNG implement - chỉ tư vấn. Sau khi brainstorm, dùng /ck:plan hoặc /ck:cook để implement.

#### Biết muốn gì

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:cook` | ⚡⚡⚡ All-in-one: research → plan → implement → test → review | **FAST mode** - Quick iterations, features đơn giản |
| `/ck:cook` | ⚡⚡⚡ All-in-one: research → plan → implement → test → review | **FAST mode** - Quick iterations, features đơn giản |
| `/ck:plan` | Tạo plan chi tiết không code | **SAFE mode** - Features phức tạp, cần approval trước |
| `/ck:cook @plan.md` | Implement plan có sẵn từng bước | Sau khi /ck:plan được approved |
| `/code @plan.md` | Execute plan có sẵn từng bước | Sau khi /ck:plan được approved |

** Sự khác biệt chính:**\
• `/ck:cook` = Tốc độ, plan nội bộ, straight to implementation\
• `/ck:plan` → `/ck:cook` = An toàn, tạo plan có thể review trước

** Sự khác biệt chính:**\
• `/ck:cook` = Tốc độ, plan nội bộ, straight to implementation\
• `/ck:plan` → `/code` = An toàn, tạo plan có thể review trước

###  Sửa Lỗi

#### Chẩn đoán trước

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:debug` | Phân tích và tìm root cause | Không biết lỗi gì |
| `/ck:fix` | Smart fix routing - tự động route theo loại issue | Biết issue, muốn fix nhanh |

** Smart Routing:** Chỉ cần dùng /fix \<mô tả issue\> và nó sẽ tự động route tới command chuyên biệt phù hợp!

###  Git Operations

| Command | Mô tả | Options |
|----|----|----|
| `/ck:git` | Git operations với natural language | `cm` `cp` `pr` `merge` |
| `/ck:worktree` | Tạo isolated worktree | Làm việc song song nhiều features |

** Mẹo:** Sử dụng ngôn ngữ tự nhiên thay vì commands cố định. Chỉ cần nói "commit my changes" hoặc "create a PR for this feature"!

###  Git Operations Legacy

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:git cm` | Stage all + commit (không push) | Lưu work locally |
| `/ck:git cp` | Stage + commit + push | Sẵn sàng share changes |
| `/ck:git merge` | Merge branches | Combine feature branch to main |
| `/ck:git pr` | Tạo pull request | Request code review |

###  Documentation

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:docs init` | Tạo documentation ban đầu cho dự án | Dự án mới/chưa có docs |
| `/ck:docs summarize` | Tóm tắt các thay đổi codebase | Sau major changes |
| `/ck:docs update` | Cập nhật documentation hiện có | Giữ docs đồng bộ |

###  Khám phá & Nghiên cứu

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:scout` | Tìm kiếm codebase song song nhanh | Tìm files liên quan cho task |
| `/ck:scout ext` | Tìm kiếm mở rộng với Gemini 2M context | Khám phá codebase sâu |
| `/ck:watzup` | Review các thay đổi gần đây trong branch hiện tại | Wrap up work, hiểu recent commits |

###  Hỏi đáp & Học tập

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:ask` | Tư vấn kỹ thuật & kiến trúc | Cần advice về architecture, trade-offs |
| `/coding-level [0-5]` | Đặt độ sâu giải thích | Tùy chỉnh responses theo experience |

** Coding Levels:**\
• `0` = ELI5 (không biết code)\
• `1` = Junior (0-2 năm)\
• `2` = Mid-Level (3-5 năm)\
• `3` = Senior (5-8 năm)\
• `4` = Tech Lead (8-10 năm)\
• `5` = God Mode (mặc định, hiệu quả tối đa)

###  Quản lý dự án

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:plans-kanban` | Dashboard trực quan cho plans | Xem tiến độ plan, timeline visualization |
| `/ck:preview` | Universal markdown/directory viewer | Xem plans, docs dễ đọc |
| `/ck:test` | Chạy tests và phân tích kết quả | Verify code changes work |

###  Design Commands

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:frontend-design` | UI/UX design với screenshot analysis | Tạo/cải thiện UI components |
| `/ck:remotion` | Video design với React | Tạo video animations |
| `/ck:threejs` | 3D graphics với Three.js | Tạo 3D visualizations |
| `/ck:ai-artist` | AI image generation | Tạo artwork, assets |

###  Code Review

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:review codebase` | Comprehensive codebase review | Quality assessment, tìm issues |
| `/ck:review codebase parallel` | Parallel review với nhiều agents | Large codebase, cần speed |

###  Các biến thể Planning

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ck:plan` | Auto-detect complexity | Planning chung |
| `/ck:plan --fast` | Quick planning cho tasks đơn giản | Small features, quick fixes |
| `/ck:plan --hard` | Deep planning với extensive research | Complex, multi-phase features |
| `/ck:plan --parallel` | Plan nhiều tasks độc lập | Nhiều features không liên quan |
| `/ck:plan validate` | Validate và review plan có sẵn | Trước khi execution |
| `/ck:plan archive` | Archive plan đã hoàn thành | Clean up finished work |

###  Common Workflows

#### Workflow 1: Build Feature (Safe)

1\. `/ck:brainstorm` → Khám phá options

2\. `/ck:plan` → Review plan

3\. `/clear` hoặc `/compact`

4\. `/ck:cook @plan.md` → Implement

5\. `/ck:git cp` → Push

6\. `/ck:git pr` → PR

#### Workflow 1: Build Feature (Safe)

1\. `/ck:brainstorm` → Khám phá options

2\. `/ck:plan` → Review plan

3\. `/clear` hoặc `/compact`

4\. `/code @plan.md` → Implement

5\. `/ck:git cp` → Push

6\. `/ck:git pr` → PR

#### Workflow 2: Build Feature (Fast)

1\. `/ck:cook` → Research → Plan → Implement → Test → Review

2\. `/ck:git cp` → Commit và push khi approved

#### Workflow 2: Build Feature (Fast)

1\. `/ck:cook` → Research → Plan → Implement → Test → Review

2\. `/ck:git cp` → Commit và push khi approved

#### Workflow 3: Debugging & Fixing

1\. `/ck:debug` → Tìm root cause

2\. `/ck:fix` → Smart routing

3\. `/ck:git cm` → Commit fix locally

#### Workflow 3: Debugging & Fixing

1\. `/ck:debug` → Tìm root cause

2\. `/ck:fix` → Smart routing

3\. `/ck:git cm` → Commit fix locally

#### Workflow 4: New Project Setup

1\. `/ck:bootstrap` → Full setup

2\. Follow onboarding

#### Workflow 5: Tham gia dự án

1\. `/ck:docs init` → Analyze codebase

2\. `/ck:scout` → Explore structure

#### Workflow 6: Code Review

1\. `/ck:test` → Chạy tests

2\. `/ck:review codebase` → Review toàn diện

3\. `/ck:simplify` → Refine code

4\. `/ck:git pr` → Tạo PR

#### Workflow 7: Design Implementation

1\. `/ck:frontend-design` → Tạo design

2\. `/ck:cook` → Implement

3\. `/ck:test` → Verify

#### Workflow 8: Research

1\. `/ck:scout` → Tìm files liên quan

2\. `/ck:research` → Deep dive topic

3\. `/ck:ask` → Hỏi chuyên gia

###  Pro Tips

** Speed vs Safety Trade-off:**\
• Dùng /ck:cook khi confident và muốn speed\
• Dùng /ck:plan → /ck:cook @plan.md khi precision và review quan trọng

** Speed vs Safety Trade-off:**\
• Dùng /ck:cook khi confident và muốn speed\
• Dùng /ck:plan → /code khi precision và review quan trọng

** Best Practice:**\
• Dùng /ck:cook cho hầu hết tasks - có internal planning\
• Dùng /ck:plan trước khi /ck:cook @plan.md cho tasks phức tạp cần review

** Không mix workflows:**\
• ❌ `/ck:plan` → `/ck:cook` (cook có planning riêng)\
• ✅ `/ck:plan` → `/code` (flow đúng)\
• ✅ `/ck:cook` standalone (có internal planning)

** Git safety:**\
• `/ck:git cm` = commit only (safe cho experimentation)\
• `/ck:git cp` = commits VÀ pushes (không thể undo dễ dàng)

** Git safety:**\
• `/git:cm` = commit only (safe cho experimentation)\
• `/git:cp` = commits VÀ pushes (không thể undo dễ dàng)

###  Cheat Sheet Tóm tắt

| Tình huống | Command |
|----|----|
| Build something mới hoàn toàn | `/ck:bootstrap` |
| Có ý tưởng nhưng chưa biết approach | `/ck:brainstorm` |
| Biết chính xác muốn gì, làm nhanh | `/ck:cook` |
| Biết chính xác muốn gì, làm nhanh | `/ck:cook` |
| Muốn plan kỹ trước khi code | `/ck:plan → /ck:cook` |
| Muốn plan kỹ trước khi code | `/ck:plan → /code` |
| Có lỗi, không biết tại sao | `/ck:debug → /ck:fix` |
| Có lỗi, biết nguyên nhân | `/ck:fix` |
| Cần lưu work | `/ck:git cm` hoặc `/ck:git cp` |
| Cần lưu work | `/git:cm` hoặc `/git:cp` |
| Cần hiểu codebase | `/ck:docs init` |
| Cần advice kiến trúc | `/ck:ask` |
| Có gì thay đổi gần đây? | `/ck:watzup` |
| Xem plans trực quan | `/ck:plans-kanban` hoặc `/ck:preview` |
| Mình mới học, giải thích dùng từ ngữ dễ hiểu chút nhé | `/coding-level 1` |
| Cần help với ClaudeKit | `/ck:ck-help` |

Không chắc? Dùng /ck-help

`/ck:ck-help` → Full documentation\
`/ck:ck-help fix` → Category guide cho fix commands\
`/ck:ck-help plan --hard` → Chi tiết specific command\
`/ck:ck-help how to debug` → Task-based recommendations

###  Sơ Đồ Quyết Định Tương Tác

Click vào bất kỳ node hoặc đường path nào để highlight lộ trình đến command. Hoặc click vào các command button ở trên để xem đường đi tương ứng.

 

 

### Lệnh Marketing

Chọn để xem đường dẫn

### 

Click vào nút hoặc đường path để highlight lộ trình. Click command ở trên để xem path.

###  Bắt Đầu & Học ClaudeKit

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ckm:ck-help` | Học cách sử dụng ClaudeKit Marketing | Lần đầu sử dụng Marketing Kit |
| `/ckm:init` | Setup workspace marketing với brand, personas, templates | Chuẩn bị môi trường làm việc |

###  Quản Lý Campaigns

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ckm:campaign` | Tạo & quản lý campaigns multi-channel | Launch campaigns phức hợp |
| `/ckm:email` | Thiết kế email flows & sequences | Email marketing, drip campaigns |
| `/ckm:social` | Schedule & quản lý social content | Social media marketing |

###  Tạo Content

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ckm:write` | Tạo content (8 modes: fast, good, cro, blog...) | Viết blogs, copy, marketing content |
| `/ckm:video` | Tạo video scripts & storyboards | Video marketing, YouTube |
| `/ckm:slides` | Tạo pitch decks & presentations | Sales pitches, training materials |

###  Growth & Tối Ưu

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ckm:launch-strategy` | Chiến lược go-to-market cho sản phẩm mới | Product launches |
| `/ckm:pricing-strategy` | Tối ưu pricing tiers & revenue | Pricing optimization |
| `/ckm:form-cro` | Tối ưu forms để tăng conversion | CRO, lead generation |

###  Phân Tích & Chiến Lược

| Command | Mô tả | Khi nào dùng |
|----|----|----|
| `/ckm:competitor` | Phân tích đối thủ cạnh tranh | Market research, positioning |
| `/ckm:seo` | SEO audit & keyword research | SEO optimization, pSEO |
| `/ckm:funnel` | Thiết kế & tối ưu funnels | Funnel optimization |

###  Design & Quản Lý

| Command       | Mô tả                               | Khi nào dùng            |
|---------------|-------------------------------------|-------------------------|
| `/ckm:design` | Tạo logos, banners, social graphics | Visual content creation |
| `/ckm:kanban` | Quản lý tasks dạng kanban board     | Task management         |
| `/ckm:brand`  | Quản lý brand guidelines            | Brand consistency       |

###  Marketing Workflows

#### Workflow 1: Content Campaign

1\. `/ck:brainstorm` → Tìm ideas

2\. `/ckm:plan` → Lên kế hoạch

3\. `/ckm:write:good` → Viết content

4\. `/ckm:social` → Schedule posts

5\. `/ckm:analyze` → Đo lường

#### Workflow 2: Email Campaign

1\. `/ckm:persona` → Xác định audience

2\. `/ckm:email` → Design flow

3\. `/ckm:write:cro` → Viết copy

4\. `/ckm:campaign` → Launch

5\. `/ckm:form-cro` → Optimize

#### Workflow 3: Product Launch

1\. `/ckm:competitor` → Research market

2\. `/ckm:launch-strategy` → Plan launch

3\. `/ckm:pricing-strategy` → Set pricing

4\. `/ckm:write` → Create assets

5\. `/ckm:campaign` → Execute launch

#### Workflow 4: SEO Content

1\. `/ckm:seo` → Keyword research

2\. `/ckm:competitor` → Content gaps

3\. `/ckm:plan` → Content calendar

4\. `/ckm:write:blog` → Write articles

5\. `/ckm:funnel` → Optimize flow

###  Marketing Pro Tips

#### 1 Luôn bắt đầu với Research

Chạy /ckm:competitor và /ckm:seo trước khi tạo content để hiểu market positioning.

#### 2 Brainstorm trước khi Plan

Dùng /ck:brainstorm để khám phá campaign angles trước khi commit vào plan.

#### 3 Chọn đúng Write Mode

/ckm:write:fast cho drafts, :good cho quality, :cro cho conversion-focused.

#### 4 Optimize dựa trên Data

Sau launch, dùng /ckm:analyze và /ckm:form-cro để cải thiện conversion.

#### Độ phức tạp Commands

⚡ Đơn giản, nhanh

⚡⚡ Trung bình

⚡⚡⚡ Phức tạp

⚡⚡⚡⚡ Nâng cao

###  Tổng Kết & Trợ Giúp

#### Bắt Đầu Nhanh

`/ckm:ck-help` → Học basics

`/ckm:init` → Setup workspace

`/ck:brainstorm` → Bắt đầu ideation

#### Cần Trợ Giúp?

`/ckm:watzup` → Session summary

`/ck:ask` → Hỏi expert

`/ck:coding-level` → Adjust depth

#### Tài Nguyên

[→ Tất cả Commands](/vi/guides/commands) [→ Workflows Guide](/vi/guides/workflows) [→ ClaudeKit là gì?](/vi/guides/what-is-claudekit)

  Stable v1.3.2: /ckm:\*    Cross-kit Skills: /ck:\* 

