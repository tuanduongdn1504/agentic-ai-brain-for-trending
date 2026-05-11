# Permission Modes - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/permissions

> Extracted from: permissions.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Permission Modes

Cấu hình cách Claude Code xin phép — từ kiểm soát toàn bộ đến tự động thực thi với kiểm tra an toàn nền.

Tính Năng Cho Power User

Các cài đặt này kiểm soát mức độ tự chủ của Claude trên máy bạn. **Chọn mode phù hợp với mức chấp nhận rủi ro và môi trường của bạn.**

### Các Permission Mode Hiện Có

Nhấn Shift+Tab trong CLI để chuyển đổi mode. Đặt `defaultMode` trong settings để lưu lại.

<table class="w-full text-sm">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="border-b border-slate-200 dark:border-slate-700">
<th class="text-left py-3 pr-4 font-semibold text-slate-700 dark:text-slate-300">Mode</th>
<th class="text-left py-3 pr-4 font-semibold text-slate-700 dark:text-slate-300">Tự động duyệt</th>
<th class="text-left py-3 font-semibold text-slate-700 dark:text-slate-300">Phù hợp cho</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> default </code>
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Chỉ đọc file</td>
<td class="py-3 text-slate-600 dark:text-slate-400">Mới bắt đầu, công việc nhạy cảm</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> acceptEdits </code>
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Đọc + sửa file</td>
<td class="py-3 text-slate-600 dark:text-slate-400">Lặp lại code đang review</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> plan </code>
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Chỉ đọc file (không sửa)</td>
<td class="py-3 text-slate-600 dark:text-slate-400">Khám phá codebase, lên kế hoạch refactor</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> auto </code>  MỚI 
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Mọi hành động (classifier kiểm tra)</td>
<td class="py-3 text-slate-600 dark:text-slate-400">Task dài, giảm mệt mỏi prompt</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> dontAsk </code>
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Chỉ tool đã được duyệt trước</td>
<td class="py-3 text-slate-600 dark:text-slate-400">CI pipelines, môi trường hạn chế</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800 last:border-0">
<td class="py-3 pr-4">
<code class="sourceCode mandoc px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-slate-700 dark:text-slate-300"> bypassPermissions </code>  NGUY HIỂM 
</td>
<td class="py-3 pr-4 text-slate-600 dark:text-slate-400">Mọi thứ, không kiểm tra</td>
<td class="py-3 text-slate-600 dark:text-slate-400">Chỉ dùng trong container/VM cô lập</td>
</tr>
</tbody>
</table>

#### Auto Mode (Khuyến Nghị Cho Team Users)

 MỚI 

Một classifier nền review từng hành động trước khi thực thi — chặn thao tác nguy hiểm và cho phép thao tác an toàn mà không cần prompt.

##### Cách hoạt động

- • Một model classifier Sonnet 4.6 riêng đánh giá mọi hành động trước khi chạy
- • Các allow/deny rules của bạn được kiểm tra trước — classifier chỉ xử lý phần còn lại
- • Hành động chỉ đọc và sửa file trong working directory được tự động duyệt
- • Quay về prompt thủ công sau 3 lần block liên tiếp hoặc 20 lần block/session

##### Mặc định bị chặn

curl \| bash, force push, xóa hàng loạt, deploy production, gửi dữ liệu ra endpoint ngoài, cấp quyền IAM/repo, sửa đổi hạ tầng chung

##### Mặc định được phép

Thao tác file local, cài deps từ lockfile, đọc .env và gửi creds đến API tương ứng, HTTP chỉ đọc, push lên branch hiện tại

Cách A: CLI flag (thêm auto vào Shift+Tab cycle)

 

    claude --enable-auto-mode

Cách B: Settings file (mặc định lâu dài)

 

    
    }

Yêu cầu: Gói Team (Enterprise/API sắp có) · Claude Sonnet 4.6 hoặc Opus 4.6 · Admin phải bật trong [Claude Code admin settings](https://claude.ai/admin-settings/claude-code).

##### Tùy chỉnh classifier

Cho classifier biết hạ tầng nào bạn tin tưởng qua setting `autoMode`. Không đọc từ shared project settings.

 

    
    }

##### Kiểm tra & debug

 

    claude auto-mode defaults  # built-in rules
    claude auto-mode config    # effective config
    claude auto-mode critique  # AI feedback on custom rules

Research Preview: Auto mode giảm prompt nhưng không đảm bảo an toàn tuyệt đối. Bảo vệ tốt hơn bypassPermissions, nhưng không kỹ bằng review thủ công.

#### Full Bypass (bypassPermissions)

Bỏ qua mọi prompt quyền. Chỉ cần **một trong hai** cách bên dưới — CLI flag cho phiên hiện tại, hoặc settings file để đặt mặc định.

Cách A: CLI flag (phiên hiện tại)

 

    claude --dangerously-skip-permissions

or

 

    claude --permission-mode bypassPermissions

Cách B: Settings file (mặc định lâu dài)

File:

macOS

Linux

Windows

`<project>/.claude/settings.local.json` (project-local, gitignored)

 

    
    }

 CẢNH BÁO NGHIÊM TRỌNG

Không có kiểm tra an toàn nào. Trong trường hợp hiếm, Claude có thể chạy lệnh phá hủy như `rm -rf ...` nếu bị ảo giác. **Chỉ dùng trong container/VM cô lập. Ưu tiên auto mode cho giải pháp an toàn hơn.**

#### Quy Tắc Allow/Deny Chi Tiết

Kiểm soát chi tiết: cho phép lệnh an toàn, hỏi xác nhận lệnh rủi ro, chặn thao tác nguy hiểm.

File:

macOS

Linux

Windows

`<project>/.claude/settings.local.json` (project-local, gitignored)

 

    
    }

Danh sách deny chặn lệnh phá hủy (xóa database, force push, thay đổi hệ thống). Rules được đánh giá theo thứ tự: deny → ask → allow.

Ask rules: Dùng `ask` để bắt buộc prompt xác nhận cho các lệnh cụ thể, ngay cả khi chúng được allow.

Tip: settings.json supports a `"$schema"` field for IDE autocompletion. Add `"$schema": "https://claudekit.cc/schemas/ck-config.schema.json"`

#### Cú Pháp Permission Rule

Rules theo format `Tool` hoặc `Tool(specifier)`. Đánh giá theo thứ tự: **deny → ask → allow**.

| Rule                           | Hiệu quả                        |
|--------------------------------|---------------------------------|
| `Bash`                         | All Bash commands               |
| `Bash(npm run *)`              | Commands starting with npm run  |
| `Read(./.env)`                 | Reading .env in project root    |
| `Read(./secrets/**)`           | Reading any file under secrets/ |
| `Edit(/src/**/*.ts)`           | Editing .ts files in src/       |
| `WebFetch(domain:example.com)` | Fetch requests to example.com   |
| `mcp__server__tool`            | Specific MCP tool               |
| `Agent(Explore)`               | The Explore subagent            |

Để xem tài liệu đầy đủ về permission scopes và cú pháp, hãy truy cập [Tài liệu Chính thức Claude Code ](https://code.claude.com/docs/en/permissions)

