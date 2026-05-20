---
source: webfetch-tier-0
url: https://howznguyen.dev/blog/router-opus-gpt-subagent-workflow
title: "Kết hợp Opus + GPT trong Claude Code bằng Router và Sub-agent"
title_en: "Combining Opus + GPT in Claude Code via Router and Sub-agent"
author: howznguyen
published: 2026-05-19
language: vi
reading_time: 20 min
category: AI Agent Programming
fetched: 2026-05-20
path: 3-webfetch
notes: Vietnamese-language individual-practitioner blog post. Specific architectural pattern: router-mediated multi-provider Claude Code (Opus on Kiro as supervisor, GPT-5.5 on Codex as sub-agent default) leveraging Claude Code's built-in 3-slot model config (opus/sonnet/haiku). Includes concrete `~/.claude/settings.json` example + file-based handoff between sub-agent phases + clear task-allocation rubric (when Opus vs when GPT sub-agent).
---

# Kết hợp Opus + GPT trong Claude Code bằng Router và Sub-agent

> Blog post by **howznguyen** — May 19, 2026 — 20 min read — AI Agent Programming
> Fetched 2026-05-20 via WebFetch (Tier 0; no bypass needed)

---

## Vấn đề: để một model làm hết thì hơi phí

Trước đây mình hay dùng một model mạnh cho toàn bộ flow.

Một task kiểu:

> "Implement feature X, đọc codebase, lên plan, sửa code, chạy test, fix lỗi, review lại."

Nghe tiện. Một model làm hết từ đầu tới cuối. Nhưng dùng một thời gian thì mình thấy vài vấn đề khá rõ.

Đầu tiên là **tốn credit**. Model mạnh như Opus rất hợp để suy nghĩ, phân tích, giữ context, phát hiện hướng sai. Nhưng nếu bắt nó làm hết mấy task lặp lại kiểu rename file, thêm test case, sửa type, update import, chạy lint rồi fix format thì hơi phí.

Thứ hai là **task lớn dễ trôi context**. Một model dù mạnh tới đâu, khi conversation dài lên, nhiều file được đọc, nhiều quyết định nhỏ xuất hiện, thì flow vẫn có khả năng bị loãng. Nó có thể nhớ phần đầu, quên một constraint ở giữa, hoặc đang implement thì bị cuốn vào chi tiết.

Thứ ba là **tốc độ**. Có những phần không cần "suy nghĩ sâu". Chỉ cần chạy nhanh, chính xác, bám theo chỉ dẫn. Nếu dùng model nhanh hơn cho phần đó thì workflow mượt hơn nhiều.

Vậy nên mình bắt đầu tách vai trò:

- **Opus**: planner, supervisor, reviewer, context owner.
- **GPT sub-agent**: executor cho các task nhỏ, rõ scope, có input/output cụ thể.

> "Không phải model nào cũng nên làm mọi việc. Model mạnh nhất nên giữ vai trò cần suy luận mạnh nhất."

## Router là gì? Tại sao cần?

Hiểu đơn giản, router (hay proxy) là một lớp trung gian giúp mình dùng nhiều model/provider phía sau qua một endpoint tương thích.

Trong workflow này, router giúp mình gom nhiều model vào một chỗ để Claude Code hoặc tool tương thích OpenAI/Anthropic có thể gọi model theo tên route.

Mình đang dùng 9Router, nhưng bạn hoàn toàn có thể dùng tool khác:

- [9Router](https://9router.com) — cái mình đang dùng
- [OmniRoute](https://omniroute.online)
- CLI API Proxy
- Hoặc bất kỳ proxy nào expose được endpoint tương thích Anthropic/OpenAI

Ý tưởng đều giống nhau: gom nhiều provider vào một endpoint, rồi route theo tên model.

Ví dụ:

- `opus-4.6` trỏ tới Opus trên Kiro.
- `gpt-5.5` trỏ tới GPT-5.5.

Tên route cụ thể tuỳ bạn đặt. Ý chính là router đứng giữa.

Mình hay nghĩ router giống một cái "tổng đài chuyển mạch". Claude Code không cần quan tâm phía sau model đến từ đâu. Mình chỉ cần gọi đúng route/model name, còn router lo chuyển sang provider tương ứng.

## Mô hình supervisor / sub-agent

Mô hình mình dùng khá đơn giản.

Opus không trực tiếp cày hết mọi việc. Opus làm vai trò **supervisor**:

- đọc yêu cầu lớn
- hiểu codebase
- hỏi lại nếu thiếu
- chia task
- quyết định task nào giao cho sub-agent
- review output
- giữ context tổng
- phát hiện khi agent đi lệch

GPT sub-agent làm vai trò **executor**:

- nhận task nhỏ
- đọc file liên quan
- implement đúng scope
- trả lại summary
- không tự mở rộng phạm vi
- không tự quyết định architecture lớn

Nói nôm na: **Opus think big, GPT do fast.**

Điểm quan trọng là sub-agent phải được giao task có biên rõ. Nếu giao kiểu "làm feature này đi", nó sẽ phải tự plan lại, dễ lệch khỏi ý supervisor. Còn nếu giao kiểu "sửa 3 file này, theo contract này, không đổi public API", output ổn hơn nhiều.

## Cách setup tổng quan

### Bước 1: Chuẩn bị route trên router

Trong router của bạn, cần tạo hoặc kiểm tra route cho từng model mình muốn dùng.

Ví dụ:

```
kr/claude-opus-4.6 -> Kiro Opus 4.6
cx/gpt-5.5 -> Codex GPT-5.5
```

Tên route không nhất thiết giống ví dụ. Nhưng mình khuyên đặt tên dễ hiểu, vì lát nữa bạn sẽ dùng trong config hoặc prompt.

### Bước 2: Trỏ Claude Code về router

Claude Code cho phép config model và endpoint qua file `~/.claude/settings.json`. Đây là config mình đang dùng (với 9Router local):

```json
{
  "ANTHROPIC_BASE_URL": "http://127.0.0.1:20128/v1",
  "ANTHROPIC_AUTH_TOKEN": "YOUR_ROUTER_API_KEY",
  "ANTHROPIC_DEFAULT_OPUS_MODEL": "kr/claude-opus-4.6",
  "ANTHROPIC_DEFAULT_SONNET_MODEL": "cx/gpt-5.5",
  "ANTHROPIC_DEFAULT_HAIKU_MODEL": "cx/gpt-5.5"
}
```

Giải thích:

- `ANTHROPIC_BASE_URL`: endpoint local của router (chạy trên máy, port 20128)
- `ANTHROPIC_AUTH_TOKEN`: API key của router
- `ANTHROPIC_DEFAULT_OPUS_MODEL`: route `kr/claude-opus-4.6` — Opus chạy qua Kiro, đây là model chính (supervisor)
- `ANTHROPIC_DEFAULT_SONNET_MODEL`: route `cx/gpt-5.5` — GPT-5.5 chạy qua Codex, đây là model cho sub-agent
- `ANTHROPIC_DEFAULT_HAIKU_MODEL`: cũng trỏ về GPT-5.5 cho các task nhẹ

Prefix `kr/` và `cx/` là cách 9Router phân biệt provider. `kr` = Kiro, `cx` = Codex/OpenAI.

**Điểm quan trọng:** Claude Code chỉ có 3 slot model: opus, sonnet, và haiku. Không có tên tuỳ ý. Vậy nên cách mình tận dụng là:

- **opus** = model chính, chạy conversation, làm supervisor
- **sonnet** = model cho sub-agent (spawn agent sonnet)
- **haiku** = model cho task nhẹ nhất

Bạn map 3 slot này sang bất kỳ model nào qua router.

Với config này, khi mình dùng Claude Code bình thường, Opus sẽ là model chính. Khi spawn sub-agent bằng `spawn agent sonnet`, Claude Code sẽ tự dùng model sonnet đã config — tức GPT-5.5.

### Bước 3: Spawn sub-agent — tính năng built-in của Claude Code

Đây là phần nhiều người không biết: **sub-agent là tính năng có sẵn trong Claude Code**. Bạn không cần cài plugin, không cần MCP server riêng, không cần script wrapper.

Claude Code có một tool gọi là Agent. Khi model chính (Opus) cần giao việc cho agent khác, nó có thể tự spawn một agent con chạy model khác. Hoặc bạn gõ trực tiếp:

```
spawn agent sonnet
Task: Research the database schema for billing usage...
```

Với config ở bước 2, `sonnet` sẽ map sang `cx/gpt-5.5`. Tức là GPT-5.5 sẽ xử lý task đó trong một context riêng biệt, không ảnh hưởng conversation chính của Opus.

Điểm hay:

- Sub-agent chạy trong môi trường riêng, không làm loãng context của supervisor
- Opus vẫn giữ nguyên conversation và có thể review output khi sub-agent xong
- Có thể spawn nhiều sub-agent song song cho các task độc lập
- Sub-agent có quyền đọc/sửa file, chạy command — giống một dev thật đang làm cùng

Cách dùng trong thực tế:

```
Based on the plan above, I'm spawning two research agents in parallel:

spawn agent sonnet
Task: Research our current database schema, models, and any existing
usage tracking. List what's already in place for tracking requests.

spawn agent sonnet
Task: Research our frontend workspace components and patterns.
How do we currently display usage/quota info? Any existing components?
```

## Phân chia nhiệm vụ: khi nào Opus, khi nào GPT?

Đây là phần mình thấy quan trọng hơn cả setup. Setup xong mà chia task tệ thì vẫn loạn. Model mạnh + model nhanh không tự động tạo workflow tốt.

### Không chỉ implement — sub-agent cũng có thể research

Sub-agent không chỉ để code. Bạn hoàn toàn có thể spawn sub-agent để **tìm hiểu, đọc code, research** trước khi implement.

Ví dụ với một feature lớn, mình hay tách kiểu:

```
spawn agent sonnet
Research phase 1: Examine database layer (models, migrations,
queries). Look for existing usage/request tracking. Document findings.

spawn agent sonnet
Research phase 2: Examine frontend and API routes for workspace
usage display. Document patterns and components used.
```

Hai agent này chạy song song, mỗi agent đọc một phần codebase. Opus nhận summary từ cả hai, rồi mới lên plan tổng.

Cách này giúp:

- Opus không phải đọc hết mọi file — tiết kiệm context window
- Mỗi sub-agent tập trung vào phần riêng — output rõ hơn
- Research song song — nhanh hơn đáng kể so với đọc tuần tự

### Dùng file trung gian để chuyển tiếp giữa các giai đoạn

Một vấn đề thực tế: sub-agent giai đoạn 1 (research) làm xong, sub-agent giai đoạn 2 (implement) làm sao biết kết quả?

Cách mình hay dùng là để sub-agent ghi output ra file. File đó trở thành "bản giao việc" cho agent tiếp theo.

```
spawn agent sonnet
Research database usage tracking. Write findings to .agent/notes/billing-research.md
Include: current schema, what's tracked, what's missing, suggested additions.
```

Sau đó phase 2:

```
spawn agent sonnet
Backend implementation for billing usage feature.
Read .agent/notes/billing-research.md for context.
Implement following the gaps and suggestions listed there.
```

Sub-agent giai đoạn 2 không cần đọc lại toàn bộ codebase. Nó chỉ cần đọc file tóm tắt từ giai đoạn 1 là đủ context để implement đúng.

Mình hay dùng folder `.agent/notes/` hoặc `.agent/handoff/` cho mấy file kiểu này. Gitignore nó nếu không muốn commit.

Nhưng không nhất thiết phải tự tạo file thủ công. Bạn có thể dùng:

- **Backlog.md** — tạo task có phần notes/output, agent sau đọc task đó để lấy context
- **Knowns** — dùng `appendNotes` để ghi kết quả vào task, hoặc tạo doc riêng cho mỗi giai đoạn
- **Markdown tự cấu trúc** — folder `docs/handoff/` hoặc bất kỳ convention nào team bạn quen

### Opus nên làm gì?

- phân tích yêu cầu mơ hồ
- đọc architecture
- tìm rủi ro
- chia task
- quyết định thứ tự implement
- review code
- check xem sub-agent có đi lệch không
- tổng hợp context từ nhiều nguồn
- viết spec/plan
- xử lý bug khó
- ra quyết định đánh đổi (trade-off)

### GPT sub-agent nên làm gì?

- implement một function
- thêm test
- update type
- sửa lint
- refactor nhỏ
- migrate config đơn giản
- thêm component theo pattern có sẵn
- viết docs ngắn theo outline
- tìm usage của một API trong repo
- kiểm tra một nhóm file cụ thể

### Việc không nên giao cho sub-agent

- đổi architecture lớn
- quyết định database schema mới
- thay public API
- refactor xuyên nhiều module
- xoá code cũ
- sửa security-sensitive flow
- merge output từ nhiều agent
- quyết định đánh đổi về product

## Quản lý context: đừng cố chấp một tool

Không nhất thiết phải dùng đúng một tool nào. Tác giả đang dùng Knowns (MCP-based project memory). Nhưng bạn hoàn toàn có thể dùng cách khác:

- [Backlog.md](https://github.com/MrLesk/Backlog.md) — markdown task management
- `TODO.md` hoặc `tasks.md` tự viết
- folder `docs/`
- file `decisions.md`
- Notion/Linear/Jira nếu team đã dùng

Quan trọng không phải tên tool. Quan trọng là supervisor agent có chỗ để biết:

- task hiện tại là gì
- scope nằm ở đâu
- quyết định cũ là gì
- file nào liên quan
- tiêu chí hoàn thành là gì
- cái gì không được đụng
- đã thử gì và fail ra sao

> "Đừng cố chấp vào một tool duy nhất. Hệ thống tốt là hệ thống giúp supervisor agent giữ context đúng, không phải hệ thống có tên nghe xịn nhất."

## Debug lỗi thường gặp

- **Sai model name / prefix**: route cần đúng prefix provider, ví dụ `kr/claude-opus-4.6`, không phải `claude-opus-4.6`. Tương tự GPT cần `cx/gpt-5.5`.
- **Router chưa chạy**: `curl http://127.0.0.1:20128/v1/models -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"` — nếu connection refused thì cần start router.
- **Sai biến env**: Claude Code dùng `ANTHROPIC_AUTH_TOKEN`, không phải `ANTHROPIC_API_KEY`.
- **Session cũ**: sửa `settings.json` xong cần restart Claude Code để load config mới.
- **Sai format**: route GPT chỉ nhận OpenAI format mà router chưa chuyển đổi → lỗi body/schema. Kiểm tra chế độ tương thích.

## Tips để workflow đỡ loạn

1. **Đừng spawn agent trước khi có plan.** Task còn mơ hồ thì để supervisor làm rõ trước.
2. **Mỗi sub-agent một nhiệm vụ.** Đừng giao "implement backend, frontend, tests, and refactor". Tách ra.
3. **Ghi ràng buộc rõ.** Mấy câu như "Do not change public API", "Do not add dependencies" rất đáng tiền.
4. **Supervisor phải review diff.** Sub-agent làm xong không có nghĩa là xong.

## Khi nào workflow này không đáng dùng?

Không phải task nào cũng cần supervisor/sub-agent. Sửa typo, update copy, rename biến, fix lỗi nhỏ → dùng một agent là đủ.

Mình dùng mô hình này khi task có:

- nhiều bước
- nhiều module
- cần đọc nhiều file
- cần plan trước
- cần review kỹ
- có rủi ro trôi context
- muốn tiết kiệm credit model mạnh
- có nhiều phần implementation lặp lại

> "Workflow tốt không phải workflow phức tạp nhất. Workflow tốt là workflow vừa đủ để giảm lỗi và giảm chi phí cho loại task đang làm."

## Kết

Thay vì một model làm tất cả:

- **Opus** = nghĩ sâu, giữ context, supervise, review
- **GPT** = chạy nhanh, làm task nhỏ, implement theo scope
- **Router** (9Router, OmniRouter, CLI API Proxy...) = route model và gom provider
- **Knowns/backlog/docs** = giữ context và task state
- **Claude Code** = runtime làm việc hằng ngày

Cách này giúp tiết kiệm credit hơn, task lớn ít trôi hơn, tốc độ tốt hơn, và output ổn định hơn khi làm project thật.

> "Đừng biến tool thành tôn giáo. Mục tiêu cuối cùng vẫn là: context rõ hơn, code ít sai hơn, chi phí hợp lý hơn, và mình đỡ phải giải thích lại từ đầu mỗi lần mở terminal."

5-step starter recipe:

1. Setup router với 2 route: Opus supervisor và GPT coder.
2. Dùng Opus để plan một task vừa vừa.
3. Spawn một GPT sub-agent cho một phần implementation nhỏ.
4. Bắt Opus review diff.
5. Ghi task/context vào Knowns, `backlog.md`, hoặc một file markdown có cấu trúc.
