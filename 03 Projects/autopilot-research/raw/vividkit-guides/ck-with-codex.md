# Workflow ClaudeKit trên Codex CLI - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/ck-with-codex

> Extracted from: ck-with-codex.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



  Hướng dẫn ClaudeKit + Codex CLI 

## Workflow ClaudeKit trên Codex CLI

Codex CLI là runtime terminal native của OpenAI. Dùng `ck migrate -a codex` để cài nội dung ClaudeKit vào các vị trí Codex-native, sau đó khởi chạy qua CCS bằng `ccsx`, `ccsx codex`, hoặc `ccsxp` — tất cả mà không cần ghi đè vĩnh viễn config provider của Codex.

#### Lần đầu nghe đến CCS?

Phần cài đặt Codex có hướng dẫn từng bước ngay bên dưới. Muốn tìm hiểu kỹ hơn về CCS — provider, tài khoản OAuth, routing, và dashboard — ghé qua trang hướng dẫn CCS đầy đủ.

[Xem hướng dẫn CCS ](/vi/guides/ccs)

### Các mảnh ghép khớp với nhau ra sao

**Hai nhiệm vụ, không chồng chéo.** `ck migrate -a codex` đọc source ClaudeKit từ thư mục đang làm việc và ghi file Codex-native vào các vị trí global. CCS chỉ khởi chạy Codex với target runtime đúng và override provider tạm thời.\
\
**Lưu ý:** ngay cả `-g` cũng đọc CWD trước (giới hạn upstream của `claudekit-cli`) — `cd ~` trước khi chạy migrate nếu bạn muốn global → global.

SOURCE

#### Project nguồn (./.claude/)

`ck migrate` tìm file source từ repo hiện tại trước, sau đó fallback về `~/.claude/*` khi loại source thiếu ở local.

MIGRATE

#### File CK Codex global

Với `-g`: ghi `~/.codex/` + `~/.agents/skills/` + `~/.codex/AGENTS.md`. Commands được lưu dưới dạng skill `source-command-`, không phải `~/.codex/prompts/`.\
Bỏ `-g` để dùng các phiên bản project-local dưới `.codex/` và `.agents/skills/`.

ROUTE

#### CLIProxyAPI :8317

Proxy HTTP local nhúng trong CCS Runtime.

- `ccsx codex` → qua CCS Runtime, CLIProxy ngầm bên dưới, không cần config thêm
- `ccsxp` → trực tiếp CLIProxy; qua CCS set `CLIPROXY_API_KEY=ccs-internal-managed`, hoặc truyền key riêng nếu tự host

Bỏ qua trong chế độ native auth thuần.

RUNTIME

#### Runtime Codex CLI

Cùng binary `codex` của OpenAI, nhưng được CCS khởi chạy nên kế thừa routing provider và config OAuth — gọi `codex` trực tiếp sẽ bypass CCS. Các entrypoint phổ biến:

- `ccsx` (subscription GPT OAuth native)
- `ccsx codex` (CCS Runtime + CLIProxy)
- `ccsxp` (shortcut CLIProxy trực tiếp)

Setup (per source project) ck migrate -a codex → ~/.codex/ + ~/.agents/skills

Runtime (per launch) ccsx codex → CCS injects -c model_provider="ccs_runtime" → :8317/api/provider/codex

#### Prompts vs Skills trong Codex

`ck migrate -a codex` ghi các thư mục skill tái sử dụng và có thể vẫn ghi file prompt tương thích khi phát hiện commands. Coi output prompt là tương thích cũ, không phải bề mặt workflow chính của Codex.

file prompt

##### Không còn được ghi

Trước đây ở `~/.codex/prompts/*.md`. OpenAI đã deprecate Codex custom prompts, và `claudekit-cli` cũng theo từ `v4.1.0` — commands giờ được migrate dưới dạng skill có scope. Đường dẫn prompts cũ không còn được ghi.

thư mục skill

##### Playbook workflow

Nằm ở `~/.agents/skills/skill-name/SKILL.md`. Skills mang theo các hướng dẫn sâu hơn, references, scripts, và rules mà Codex có thể load khi task khớp.

Trong Codex CLI hiện tại, `$skill-name` là cách gọi nội dung ClaudeKit đã migrate — đó là bề mặt workflow. `/command-name` được dành riêng cho built-in của Codex CLI (vd. `/init`, `/compact`) và KHÔNG chạy commands CK đã migrate.

Agents Codex project và global độc lập với nhau — không merge hay override. Giữ định nghĩa repo-only trong `.codex/agents/agent-name.toml` và rules repo-only trong `AGENTS.md` của project để chúng đi cùng codebase, không đi theo máy của bạn.

### Vì sao vẫn cần CCS?

Codex CLI thuần là đủ cho một tài khoản local đơn lẻ. Thêm CCS khi bạn muốn Codex kèm routing tài khoản dùng chung, kiểm tra quota trực tiếp, và một dashboard duy nhất cho lớp runtime.

#### Routing tài khoản theo quota

Với session Codex routing qua CCS, CLIProxy quản lý rotation runtime. CCS cung cấp các nút điều khiển: `routing set`, `pause`, `resume`, và `default` để bỏ qua tài khoản đã hết quota hoặc đang tạm dừng.

#### Theo dõi quota Codex trực tiếp

`ccs cliproxy quota --provider codex` lấy về cửa sổ quota Codex live cho các tài khoản đã xác thực, bao gồm cửa sổ năm tiếng và hàng tuần khi upstream cung cấp.

#### Analytics runtime tập trung

`ccs config` mở dashboard với thống kê CLIProxy: tổng số request, đếm thành công/thất bại, phân bố model, và tổng token chia thành input và output.

#### Một nơi quản lý cây cầu

Dùng cùng dashboard để quản lý provider, tài khoản OAuth, trạng thái routing, analytics, và cài đặt runtime tương thích Codex thay vì phải sửa các file rải rác.

Quan trọng: CCS không tự sinh ra thêm quota. Rotation chỉ hữu ích khi bạn có nhiều tài khoản đủ điều kiện hoặc project với pool quota độc lập — ví dụ, nhiều **tài khoản subscription OpenAI ChatGPT**, mỗi tài khoản có cửa sổ usage Codex riêng. Nếu các tài khoản dùng chung pool quota upstream, failover vẫn sẽ chạm cùng một giới hạn.

### Setup trong năm phút

Chạy setup máy một lần. Chạy `ck init` trong từng project, sau đó chạy `ck migrate -a codex` từ project mà bạn muốn copy nội dung ClaudeKit vào các vị trí Codex-native. Không có `-g`, ghi sẽ là project-local (`.codex/`, `.agents/skills/`); thêm `-g` để ghi global (`~/.codex/`, `~/.agents/skills/`). Để global → global, `cd ~` trước — xem caveat ở Step 4.\
\
**Lưu ý phiên bản:** hướng dẫn này theo `claudekit-cli` `v4.1.0+`. Chạy `ck update -y` để cập nhật.

1.  

    

    

    

    

    

    Step 01 ·  một lần 

    

    #### Cài CCS và ClaudeKit

    Đã cài rồi? Cập nhật bằng `ccs update` và `ck update -y`. CCS lo routing; ClaudeKit ship skills và file tương thích prompt cũ.

    

    

    

    

       shell

    

    

    kiểm tra `ccs --version` · `ck --version`

    

    

    

    ``` bg-slate-100
    $npm install -g @kaitranntt/ccs
    $npm install -g claudekit-cli
    ```

     

    

2.  

    

    

    

    

    

    Step 02 ·  oauth 

    

    #### Xác thực Codex qua CCS

    Hai cách để nối một hoặc nhiều tài khoản Codex OAuth vào CLIProxyAPI. Chọn cách hợp với workflow của bạn — cả hai đều dẫn về cùng OAuth flow.

    

    

    

    

    

       Cách A · Dashboard

    

    ##### Thêm qua dashboard CLIProxy

    Mở `ccs config` → click **CLIProxy** (`/cliproxy`) → chọn **Codex** → cuộn đến **Accounts** → **Add**. Picker model hiện ra; hoàn tất OAuth trên trình duyệt.

    

    ``` bg-slate-100
    $ccs config
    # → CLIProxy → Codex → Accounts → Add
    ```

     

    

    

    

    

       Cách B · CLI

    

    ##### Thêm qua prompt CLI một lần

    `ccs codex --auth` báo bạn đã xác thực bao nhiêu tài khoản Codex và hỏi có thêm tài khoản nữa không. Nhấn `y` để mở OAuth flow trên trình duyệt (fallback paste-callback nếu headless).

    

    ``` bg-slate-100
    $ccs codex --auth
    # [i] 1 account(s) already authenticated for Codex
    # [?] Add another account? (y/N): y
    ```

     

    

    

    

3.  

    

    

    

    

    

    Step 03 ·  kiểm tra 

    

    #### Xác nhận cây cầu Codex hoạt động tốt

    Chạy `ccs doctor` và xem dòng `Codex Auth`. Thấy `[OK] Authenticated (DD/MM/YYYY)` nghĩa là cây cầu đã nối xong và bạn có thể đi tiếp. Pipe qua `grep -i codex` để chỉ tập trung vào các dòng Codex.

    

    

    

    

       shell

    

    

    thành công Dòng `Codex Auth` hiển thị `[OK] Authenticated`

    

    

    

    ``` bg-slate-100
    $ccs doctor 2>&1 | grep -i codex
    # Codex Auth │ [OK] │ Authenticated (09/05/2026)
    ```

     

    

4.  

    

    

    

    

    

    Step 04 ·  migrate 

    

    #### Khởi tạo ClaudeKit, sau đó migrate từ project đó

    `ck init` đặt layout source ClaudeKit. `ck migrate -a codex` sau đó copy nội dung đó vào các vị trí Codex-native.

    

    

    

    

    

    

    

    

    

     quan trọng 
    ##### Source bỏ qua `-g` — destination thì theo

    

    

    

    

    Flag

    

    

    Source (read)

    

    

    Destination (write)

    

    

    no flag

    

    

    CWD has `.claude/*`

    

    

    `.codex/*` — project-local

    

    

    `-g`

    

    

    CWD has `.claude/*` (upstream bug)

    

    

    `~/.codex/*` — global

    

    

    **Global → global:** chạy `cd ~` trước để căn CWD, rồi `ck migrate -a codex -g --dry-run` để xác minh SOURCE trước khi áp dụng.

    

    

    

    

    

    

       shell

    

    

    init đặt layout source `.claude/*` trong CWD

    

    

    

    ``` bg-slate-100
    $cd your-project
    $ck init
    ```

     

    

    

    

    

       preview

    

    In SOURCE và DESTINATION mà không động vào disk. Xác nhận SOURCE đúng cái bạn muốn copy.

    

    ``` bg-slate-100
    $ck migrate -a codex --dry-run
    ```

     

    

    

    

    

       apply

    

    Ghi file Codex-native thật. Chỉ chạy sau khi `--dry-run` trông đúng.

    

    ``` bg-slate-100
    $ck migrate -a codex --yes
    ```

     

    

    

    

5.  

    

    

    

    

    

    Step 05 ·  launch 

    

    #### Khởi chạy Codex với ClaudeKit sẵn sàng

    Cả hai entrypoint dưới đây đều mở Codex qua CCS. Chọn interactive cho việc `$ck:*`; chọn `exec` cho prompt một lần và script. Dùng `ccsx codex` khi bạn cụ thể muốn quota routing của CCS Runtime.

    

    

    

    

    

       interactive

    

    ##### Session Codex nhiều lượt

    Mở REPL Codex native. Tốt nhất cho chuỗi `$ck:plan`, `$ck:cook`, và `$ck:review` khi bạn tiếp tục cùng một context.

    

    ``` bg-slate-100
    $ccsx codex
    # alias for: ccs codex --target codex
    ```

     

    

    

    

    

       non-interactive

    

    ##### Một lần qua `codex exec`

    Stream một prompt non-interactive, in response, thoát. Dùng cho shell pipeline, hook CI, và sửa nhanh.

    

    ``` bg-slate-100
    $ccsx codex exec 'draft a $ck:plan for the auth refactor'
    ```

     

    

    

    

### Khởi chạy Codex với CCS

CCS expose nhiều entrypoint runtime cho Codex CLI native. Nếu bạn bỏ qua phần text prompt, CCS sẽ mở session Codex interactive — tốt nhất cho việc `$ck:*` nhiều lượt vì bạn có thể xem plan, tinh chỉnh hướng dẫn, và tiếp tục trong cùng context Codex.

#### Giải mã các entrypoint runtime

CCS expose các target alias Codex native cộng với một shortcut cliproxy. Chọn dựa trên việc bạn muốn routing GPT OAuth thông thường, rotation quota của CCS Runtime, hay CLIProxy trực tiếp.

<table class="w-full text-left text-sm">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead class="bg-slate-100/70 dark:bg-slate-800/60 text-[11px] uppercase tracking-wider text-slate-500 dark:text-slate-400">
<tr>
<th class="px-5 py-3 font-semibold w-[18%]">Lệnh</th>
<th class="px-5 py-3 font-semibold w-[37%]">Định tuyến qua</th>
<th class="px-5 py-3 font-semibold">Dùng khi</th>
</tr>
</thead>
<tbody class="divide-y divide-slate-200/70 dark:divide-slate-800">
<tr class="align-top hover:bg-slate-50 dark:hover:bg-slate-900/70 transition-colors">
<td class="px-5 py-4">
 <code class="px-2 py-1 rounded-md border font-mono text-[12.5px] text-sky-700 dark:text-sky-300 bg-sky-50 dark:bg-sky-950/40 border-sky-200 dark:border-sky-800/60">ccsx</code>
</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">Target Codex native với routing GPT/Codex OAuth có sẵn</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">Bạn muốn launcher Codex native ngắn nhất và một tài khoản GPT/Codex OAuth là đủ.</td>
</tr>
<tr class="align-top hover:bg-slate-50 dark:hover:bg-slate-900/70 transition-colors">
<td class="px-5 py-4">
 <code class="px-2 py-1 rounded-md border font-mono text-[12.5px] text-violet-700 dark:text-violet-300 bg-violet-50 dark:bg-violet-950/40 border-violet-200 dark:border-violet-800/60">ccsx codex</code>
</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">Profile Codex built-in qua CCS Runtime + CLIProxy</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">  Khuyên dùng  Bạn muốn rotation quota qua nhiều tài khoản GPT và theo dõi quota trực tiếp qua <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">ccs cliproxy quota --provider codex</code>.</td>
</tr>
<tr class="align-top hover:bg-slate-50 dark:hover:bg-slate-900/70 transition-colors">
<td class="px-5 py-4">
 <code class="px-2 py-1 rounded-md border font-mono text-[12.5px] text-amber-700 dark:text-amber-300 bg-amber-50 dark:bg-amber-950/40 border-amber-200 dark:border-amber-800/60">ccsxp</code>
</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">Override provider CLIProxy trực tiếp</td>
<td class="px-5 py-4 text-slate-600 dark:text-slate-300 leading-relaxed">Bạn muốn đường đi mỏng hơn, bỏ qua CCS Runtime và nói thẳng với CLIProxy. Nếu đi qua CCS thì set <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">CLIPROXY_API_KEY=ccs-internal-managed</code>; nếu tự host CLIProxy riêng thì truyền key tùy ý vào <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">CLIPROXY_API_KEY</code>. Pin <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">CODEX_HOME</code> về <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">~/.codex</code> trừ khi đã set <code class="sourceCode mandoc px-1.5 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800/90 text-purple-700 dark:text-purple-300 border-slate-200 dark:border-slate-700/60 font-mono text-[0.9em] border whitespace-normal break-words [overflow-wrap:anywhere]">CCSXP_CODEX_HOME</code>.</td>
</tr>
</tbody>
</table>

**Lưu ý:** các entrypoint này inject `model_provider`, `base_url`, và `env_key` qua `-c` lúc khởi chạy — chỉ runtime. Editor dashboard ở `ccs config → Compatible → Codex CLI` hiển thị lớp user đã lưu, không phải các override này.

 `ccsx`

Định tuyến qua  
Target Codex native với routing GPT/Codex OAuth có sẵn

Dùng khi  
Bạn muốn launcher Codex native ngắn nhất và một tài khoản GPT/Codex OAuth là đủ.

 `ccsx codex`

Định tuyến qua  
Profile Codex built-in qua CCS Runtime + CLIProxy

Dùng khi  
Bạn muốn rotation quota qua nhiều tài khoản GPT và theo dõi quota trực tiếp qua `ccs cliproxy quota --provider codex`.

  Khuyên dùng 

 `ccsxp`

Định tuyến qua  
Override provider CLIProxy trực tiếp

Dùng khi  
Bạn muốn đường đi mỏng hơn, bỏ qua CCS Runtime và nói thẳng với CLIProxy. Nếu đi qua CCS thì set `CLIPROXY_API_KEY=ccs-internal-managed`; nếu tự host CLIProxy riêng thì truyền key tùy ý vào `CLIPROXY_API_KEY`. Pin `CODEX_HOME` về `~/.codex` trừ khi đã set `CCSXP_CODEX_HOME`.

#### Chế độ full quyền (`--yolo`)

Flag `--yolo` truyền `--dangerously-bypass-approvals-and-sandbox` cho binary Codex bên dưới. Hoạt động ở mọi entrypoint: `ccsx --yolo`, `ccsx codex --yolo`, `ccsxp --yolo`, hoặc trực tiếp `codex --yolo` mà không cần CCS. Codex tự duyệt mọi tool call — ghi file, chạy shell, cài package — giống hệt `--dangerously-skip-permissions` của Claude Code.

   shell

``` bg-slate-100
$ccsx --yolo
$ccsx codex --yolo
$codex --yolo
```

 

Không có rào chắn. `--yolo` tắt mọi xác nhận. Codex có thể xóa file, chạy lệnh phá, và cài package mà không hỏi. Chỉ dùng trong môi trường bỏ được hoặc khi bạn tin tưởng scope prompt hoàn toàn.

#### Gọi workflow ClaudeKit bằng `$...`

Sau migration, Codex có thể dùng nội dung CK đã cài. Trong chế độ interactive, chạy một workflow tại một thời điểm và để Codex tiếp tục cùng session.

   codex repl

``` bg-slate-100
>$ck:plan design the billing retry flow
>$ck:cook plans/260509-1231-billing-retry/
```

 

### Workflow chạy mượt trên Codex như trên Claude Code

Các chuỗi ClaudeKit này hoạt động tốt nhất sau khi \`ck migrate -a codex\` đã cài skills, agents, rules, prompt cũ, và hooks tương thích Codex.

Vòng build

#### Plan → Cook → Test

Vòng build quen thuộc. `$ck:plan` lên design, `$ck:cook` code, `$ck:test` kiểm tra. Codex thường chạy nhanh ở bước cook.

`$ck:plan` → `$ck:cook` → `$ck:test`

   shell · ccsx

``` bg-slate-100
$ccsx '$ck:plan add OAuth2 PKCE flow'
$ccsx '$ck:cook plans/260509-0807-oauth-pkce/'
$ccsx '$ck:test --coverage'
```

 

Vòng triage

#### Fix → Test → Review

`$ck:fix` triage một test hoặc log lỗi, sau đó `$ck:test` chạy lại và `$ck:review` audit diff trước khi commit.

`$ck:fix` → `$ck:test` → `$ck:review`

   shell · ccsx

``` bg-slate-100
$ccsx '$ck:fix flaky billing webhook test'
$ccsx '$ck:test billing/'
$ccsx '$ck:review --staged'
```

 

Điều tra

#### Scout → Brainstorm → Plan

`$ck:scout` khám phá file, `$ck:brainstorm` cân nhắc trade-off, `$ck:plan` chốt hướng đi. Điều tra thuần, không sửa code.

`$ck:scout` → `$ck:brainstorm` → `$ck:plan`

   shell · ccsx

``` bg-slate-100
$ccsx '$ck:scout where rate-limit logic lives'
$ccsx '$ck:brainstorm sliding window vs token bucket'
$ccsx '$ck:plan adopt token bucket'
```

 

[](/vi/guides/commands)

Tham khảo

Catalog command đầy đủ

Mọi command `$ck:*`, làm gì, và khi nào nên dùng.

 [](/vi/guides/workflows)

Tham khảo

Tất cả công thức workflow

Chuỗi dài hơn: ship, debug, retro, và nhiều hơn.

