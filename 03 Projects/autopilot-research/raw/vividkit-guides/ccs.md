# Chuyển Đổi Tài Khoản - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/ccs

> Extracted from: ccs.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## CCS - Claude Code Switch

Một lệnh, không gián đoạn, mọi provider

Chuyển đổi giữa Claude, Codex, Kiro, GLM, Kimi, Ollama và hơn thế. Nhiều tài khoản, nhiều runtime — không cần đổi config.

Được tạo bởi [ @kaitranntt](https://github.com/kaitranntt/ccs)

### Tại Sao Dùng CCS?

Bạn đang trả tiền cho nhiều gói AI — Claude Pro, ChatGPT Plus, Z.AI, Kimi, v.v. — và muốn điều khiển tất cả từ Claude Code CLI mà không phải viết lại config mỗi lần đổi provider.

  Claude Pro   ChatGPT Plus / Codex   Z.AI / GLM   Kimi   MiniMax   Alibaba Coding Plan 

 Không Có CCS

Rate limit ngắt mạch

Chạm giới hạn giữa session — context, tiến độ, mọi thứ đều đóng băng.

Đổi provider = viết lại config

Tạo settings JSON mới, sửa cliproxy config.yaml, restart Claude Code — mỗi lần đều như vậy.

Mỗi provider tự setup riêng

Auth token riêng, section riêng trong config.yaml, CLAUDE_CONFIG_DIR riêng để cách ly tài khoản.

 Với CCS

Một profile có tên cho mỗi stack

Đổi provider bằng `ccs <profile>` — không env vars, không sửa config.

Resume xuyên provider

Chạm rate limit? Tiếp tục cùng task ở provider khác bằng `--resume`.

Auth + config tự quản lý

OAuth token, cách ly tài khoản, runtime adapter — tất cả CCS lo.

 Cài đặt với 2 lệnh:

``` bg-slate-100
npm install -g @kaitranntt/ccs && ccs config
```

 

Mở dashboard tại [http://localhost:3000](http://localhost:3000) — thêm provider ở đó, rồi chạy `ccs <profile>` từ terminal.

[ CLI Cheatsheet](#cheatsheet) [ Provider Decision Tree](#decision-tree) [ Best Workflows](#workflows)

 Muốn tìm hiểu thêm về cách resume session giữa các provider? Xem [Hướng Dẫn Phục Hồi Session](/vi/guides/session-recovery).

### Tính Năng Nổi Bật

Điểm khác biệt so với các công cụ thay thế

 CLI-First 

#### Chuyển Đổi Một Lệnh

Chuyển provider bằng profile có tên — chỉ cần ccs \<provider\>. Không cần sửa env vars hay config.

 Độc Quyền 

#### Phục Hồi Session

Resume session khi bị rate limit bằng provider khác. Tính năng hiếm có trong các CLI tool.

#### Đa Runtime

Kết nối Claude Code, Codex CLI (credential ngắn hạn) và Factory Droid (adapter đa target) — một công cụ, ba runtime.

#### WebSearch & Browser

Tích hợp sẵn WebSearch và browser automation cho các provider bên thứ ba.

#### 20+ Provider, 3 Tầng Auth

13 provider OAuth qua CLIProxy, đa tài khoản Claude, và API profile BYO-key (Alibaba, MiniMax, Novita, Ollama, Llama.cpp).

#### Extended Thinking

Cờ --thinking thống nhất điều khiển ngân sách suy luận (tối đa 100K) trên Anthropic, Antigravity, Gemini hybrid và Codex theo cấp.

#### An Toàn Tài Khoản

Cách ly cross-provider, phát hiện ban và giám sát hạn ngạch để bảo vệ tài khoản Google khi chạy nhiều OAuth provider.

#### Phân Tích Ảnh & PDF

Hỗ trợ vision MCP-first cho các third-party launch (GLM/Kimi/Qwen) thiếu khả năng đọc ảnh và PDF native.

1

### Cheatsheet CLI

Tham khảo nhanh các lệnh hay dùng nhất. Phân loại theo mục đích.

#### Cơ Bản

Route Claude Code qua một provider profile.

`ccs`  Profile mặc định (Claude Pro/Max) 

`ccs <profile>`  Chạy với profile bất kỳ 

`ccs glm`  Z.AI / GLM (coder rẻ) 

`ccs kimi`  Moonshot Kimi (long context) 

`ccs codex`  OpenAI Codex (Plus/Pro) 

`ccs <profile> "<prompt>"`  One-shot prompt (không vào REPL) 

#### Cấu Hình

Quản lý profile, provider và setting toàn cục.

`ccs config`  Mở dashboard trong browser 

`ccs config channels`  Cấu hình official channels (Telegram / Discord / iMessage) 

`ccs config auth`  Cấu hình HTTP Basic Auth cho dashboard 

`ccs config thinking`  Cấu hình reasoning effort 

`ccs auth create <profile>`  Tạo profile OAuth 

`ccs api create --preset <name>`  Tạo profile API-key (preset) 

#### Vận Hành

Lệnh health check, persistence và lifecycle.

`ccs doctor`  Health check (auth + token + path) 

`ccs persist`  Lock profile hiện tại vào ~/.claude 

`ccs migrate`  Migrate từ config phiên bản cũ 

`ccs cleanup`  Xóa profile không dùng + cache 

`ccs update`  Update CCS lên bản mới nhất 

`ccs --version`  Hiển thị version CCS đã cài 

#### Runtime Targets

Đẩy profile sang runtime agent khác.

`ccs --target droid <profile>`  Định tuyến profile sang runtime cụ thể 

`ccs-droid <profile>`  Wrapper Factory Droid 

`ccsd <profile>`  Alias ngắn của ccs-droid 

`ccs-codex <profile>`  Wrapper Codex CLI native 

`ccsx <profile>`  Alias ngắn của ccs-codex 

`ccsxp <profile>`  Shortcut Codex-trên-Codex 

#### Docker

Chạy CCS trong container sandbox.

`ccs docker up`  Khởi động container CCS 

`ccs docker down`  Tắt container CCS 

`ccs docker status`  Xem trạng thái container 

`ccs docker logs`  Tail log container 

 Chạy bất kỳ lệnh nào với `--help` để xem đầy đủ option. Để xem hướng dẫn cấu hình chi tiết cho từng profile (Claude / Codex / GLM / Kimi / Gemini …), xem mục [Cây Quyết Định Provider](#decision-tree) phía dưới. Docs đầy đủ tại [docs.ccs.kaitran.ca](https://docs.ccs.kaitran.ca).

2

### Cấu Hình Providers

Chọn cách bạn muốn thiết lập các AI provider. Chọn phương thức phù hợp nhất.

#### Cây Quyết Định Tương Tác

Thủ Công

Duyệt tất cả provider được hỗ trợ theo nhà cung cấp. Click vào provider để xem env vars, đoạn cấu hình và hướng dẫn từng bước cho Claude Code CLI.

#### Web Dashboard

Giao Diện Trực Quan

Khởi chạy dashboard React tích hợp để quản lý profiles, thêm tài khoản và cấu hình providers qua giao diện trực quan hiện đại.

### Cây Quyết Định Provider

Chọn provider mà bạn có subscription để sử dụng trong Claude Code CLI.

Cây quyết định này chỉ phục vụ cấu hình chạy trong Claude Code CLI. Người dùng web app và desktop app không cần CCS.

CCS cho phép chuyển đổi nhanh giữa các subscription provider ngay trong Claude Code CLI. Chọn provider bên dưới để xem env vars và cấu hình cần thiết.

 Anthropic

 OpenAI

 Google

 Cloud AI

 IDE & DevTools

 Self-Hosted

 

Click một provider để xem hướng dẫn cài đặt

### 

Coming soon...

⚠ Rủi ro khoá tài khoản — vi phạm Google ToS

### 

 

#### Cài đặt

 — 

 

 

``` flex-1
```

 

#### Cheatsheet

 

#### Models mặc định CCS

 

#### Biến môi trường

Các biến này được CCS quản lý qua file profile — bạn không phải set thủ công vào shell.

####  Lưu ý

   

  

Click một node provider để xem cấu hình. Cuộn để zoom, kéo để pan.

### Web Dashboard

Mới

CCS đi kèm dashboard React 19 dạng routed — không phải một modal cấu hình duy nhất. Mỗi workspace phục vụ một mảng orchestration riêng.

Profiles

CLIProxy Plus

Accounts

Analytics

Health

Settings

####  Khởi chạy Dashboard

`ccs config` \# Mở dashboard (tự mở trình duyệt)

`ccs config --port 3000` \# Chỉ định port tùy chỉnh

 Dashboard sẽ tự động mở trong trình duyệt. Nếu không, truy cập thủ công tại http://localhost:PORT

####  Xem trước Dashboard

 Chế độ sáng

 Chế độ tối

Sidebar chia thành các nhóm: General, Identity & Access (Profiles, CLIProxy Plus, GitHub Copilot, Accounts), Compatible CLIs (Claude Extension, Codex CLI, Factory Droid), và System (Health, Logs, Settings).

3

### Workflow hiệu quả với CCS & ClaudeKit

Bộ recipe đã được chọn lọc để route task qua nhiều provider và runtime — tối ưu chi phí, chiều sâu hoặc context.

#### Full cycle tối ưu chi phí

Khi bạn muốn plan & review chất lượng nhưng implement khối lượng lớn với chi phí thấp.

1

\# Plan với Claude mặc định (reasoning tốt nhất)

`$ ccs "/ck:plan add payment integration"`

2

\# Implement với GLM hoặc Qwen (rẻ, nhanh)

`$ ccs glm "/ck:cook implement Stripe payment flow"`

3

\# Chạy test với GLM hoặc Qwen (vẫn rẻ)

`$ ccs glm "/ck:test run payment tests"`

4

\# Review cuối với Claude (bắt được lỗi tinh vi)

`$ ccs "/ck:code-review check payment implementation"`

#### Debug sâu với thinking model

Khi gặp test flaky hoặc bug tinh vi cần reasoning kỹ qua nhiều file.

1

\# Điều tra root cause với Codex (deep thinker)

`$ ccsx codex "/ck:debug investigate flaky webhook test"`

2

\# Cross-reference các call site với Claude mặc định

`$ ccs "/ck:scout cross-reference call sites"`

3

\# Áp dụng fix với GLM hoặc Qwen (lặp lại rẻ)

`$ ccs glm "/ck:fix apply patch + rerun tests"`

#### Routing đa runtime

Khi bạn muốn kết hợp Claude Code, Codex và Droid trong cùng một task.

1

\# Plan trong Claude Code (runtime mặc định)

`$ ccs "/ck:plan refactor auth module"`

2

\# Scaffold qua Codex (ccsx)

`$ ccsx codex "/ck:cook scaffold module"`

3

\# Chạy integration test trong Droid (ccsd) với GLM

`$ ccsd glm "/ck:test run integration suite"`

4

\# Review code cuối quay lại Claude Code

`$ ccs "/ck:code-review final pass"`

 Kết hợp provider theo từng bước: dùng model reasoning mạnh (Claude / Codex) cho plan & review, dùng coder rẻ (GLM / Qwen) cho phần implement & test khối lượng lớn. Chuyển runtime (`ccsd`, `ccsx`) khi cần agent khác.

