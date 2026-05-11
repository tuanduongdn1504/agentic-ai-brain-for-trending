# Bảng Lệnh Nhanh - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/commands

> Extracted from: commands.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



## Bảng Lệnh Nhanh

Danh sách đầy đủ các slash commands

Slash Commands Là Gì?

Hãy nghĩ về slash commands như là **các phím tắt thần kỳ** 🪄 — chỉ cần gõ `/command` và để AI làm phần việc nặng nhọc! Không cần code, chỉ cần nói cho ClaudeKit biết bạn muốn gì.

Ví dụ

`/ck:cook "add a login button"` → AI xây dựng toàn bộ tính năng cho bạn! 🎉

Chuyển Đổi Sang Cú Pháp Mới

Tra cứu nhanh cú pháp mới nếu bạn đang dùng phiên bản cũ

  Engineer Kit 

  Marketing Kit 

**Tất cả Commands → Skills:** Toàn bộ legacy commands đã chuyển sang skills. Bạn có thể dùng `/cook` hoặc `/ck:cook`, nhưng **khuyến nghị dùng prefix /ck:** để tránh xung đột với các lệnh có sẵn của Claude Code.

####  Hướng Dẫn Chuyển Đổi

| Command cũ                  | Command mới                                  |
|-----------------------------|----------------------------------------------|
| `/debug`                    | `/ck:debug`                                  |
| `/plan`                     | `/ck:plan`                                   |
| `/code @plan.md`            | `/ck:cook @plan.md`                          |
| `/code:no-test`             | `/ck:cook add footer --no-test`              |
| `/code:parallel`            | `/ck:cook refactor api --parallel`           |
| `/code:auto`                | `/ck:cook add pagination --auto`             |
| `/plan:fast`                | `/ck:plan --fast add auth`                   |
| `/plan:hard`                | `/ck:plan --hard migrate to microservices`   |
| `/plan:archive`             | `/ck:plan archive`                           |
| `/plan:ci`                  | `/ck:fix CI build failing --auto`            |
| `/fix:ci`                   | `/ck:fix deploy pipeline error --auto`       |
| `/fix:test`                 | `/ck:fix auth tests failing --review`        |
| `/fix:types`                | `/ck:fix type errors in utils --quick`       |
| `/fix:ui`                   | `/ck:fix layout broken on mobile --parallel` |
| `/git:cm`                   | `/ck:git cm`                                 |
| `/git:cp`                   | `/ck:git cp`                                 |
| `/git:pr`                   | `/ck:git pr`                                 |
| `/git:merge`                | `/ck:git merge`                              |
| `/design:video`             | `/ck:remotion [video or component]`          |
| `/design:3d`                | `/ck:threejs spinning globe with markers`    |
| `/design:screenshot`        | `/ck:frontend-design`                        |
| `/design:describe`          | `/ck:frontend-design`                        |
| `/review:codebase`          | `/ck:code-review codebase`                   |
| `/review:codebase:parallel` | `/ck:code-review codebase parallel`          |
| `/docs:init`                | `/ck:docs init`                              |
| `/docs:update`              | `/ck:docs update`                            |
| `/docs:summarize`           | `/ck:docs summarize`                         |
| `/content:blog`             | `/ck:copywriting blog [context]`             |
| `/content:landing`          | `/ck:copywriting landing [context]`          |
| `/skill:create foo`         | `/ck:skill-creator foo`                      |
| `/integrate:stripe`         | `/ck:payment-integration stripe checkout`    |
| `/integrate:sepay`          | `/ck:payment-integration sepay webhook`      |
| `/bootstrap:auto`           | `/ck:bootstrap --auto`                       |
| `/bootstrap:auto:fast`      | `/ck:bootstrap --fast`                       |
| `/bootstrap:auto:parallel`  | `/ck:bootstrap --parallel`                   |
| `/test:ui`                  | `/ck:test ui [url]`                          |

 Show all migrations (28 more)

**Claude Code v2.1.1+:** Skills gọi qua `/skill-name [args]` hoặc `/ck:skill-name` — cả hai đều hoạt động như nhau. Nên dùng prefix `/ck:` cho các skill trùng tên với slash command có sẵn của Claude Code (vd: `/ck:plan` thay vì `/plan`).

  Marketing Kit v1.3.2  Namespace: `/mkt:*` → `/ckm:*`

Namespace Prefix Mới

/ck:\* = 49 skill chia sẻ với Engineer Kit \| /ckm:\* = 48 skill riêng marketing

####  Hướng Dẫn Chuyển Đổi

<table class="w-full text-xs border-collapse">
<thead>
<tr class="bg-purple-50 dark:bg-purple-900/20">
<th class="py-2 px-3 text-left text-xs font-semibold text-slate-500 dark:text-slate-500 border-b border-slate-200 dark:border-slate-700 w-[30%]">Command cũ</th>
<th class="py-2 px-3 text-left text-xs font-semibold text-purple-700 dark:text-purple-300 border-b border-purple-200 dark:border-purple-800 w-[70%]">Command mới</th>
</tr>
</thead>
<tbody class="text-slate-600 dark:text-slate-400">
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan [task]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:fast</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan --fast [task]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:hard</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan --hard [task]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:cro</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan --cro landing-page</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:good</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:good [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:fast</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:fast [topic]</code></td>
</tr>
</tbody>
<tbody id="migration-mkt-extra-rows" class="text-slate-600 dark:text-slate-400" style="display: none;">
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:cro</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:cro [page-url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:enhance</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:enhance [file]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:blog</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:blog [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:audit</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:audit</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:publish</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:publish [file]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:campaign:create</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:campaign:create [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:campaign:status</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:campaign:status</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:campaign:analyze</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:campaign:analyze [period]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:campaign:email</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:campaign:email [series]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:seo:keywords</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:seo:keywords [query]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:seo:audit</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:seo:audit [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:seo:pseo</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:seo:pseo [template]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:email:flow</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:email:flow [type]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:email:sequence</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:email:sequence [type]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:social:schedule</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:social:schedule</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:competitor</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:competitor [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:video:create</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:video:create [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:video:script</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:video:script [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:youtube:blog</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:youtube:blog [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:brand:update</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:brand:update [element]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:docs:init</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:docs:init</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:docs:update</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:docs:update</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/fixing</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:fix [issue] --auto|--review|--quick</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/test-orchestrator</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:test [ui|workflow] [target]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:preview</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:preview [path] --explain|--slides|--diagram|--ascii</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:storage</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:storage</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:storage:list</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:storage:list</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:storage:sync</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:storage:sync</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:storage:upload</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:storage:upload</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:storage:url</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:storage:url</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:dashboard</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:dashboard</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:dashboard:check</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:dashboard:check</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:analyze:report</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:analyze:report</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:init</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:init</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:ask [question]</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:ask [question]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:funnel [action]</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:funnel [action] [type]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:persona [action]</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:persona [action]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:parallel</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan --parallel [task]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:archive</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan archive</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:validate</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan validate</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:formula [type]</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:copywriting formula [type]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:video:storyboard</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:video:storyboard [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:youtube:infographic</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:youtube:infographic [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:youtube:social</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:youtube:social [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:docs:summarize</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:docs:summarize</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:docs:llms</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:docs:llms</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:hub</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:hub [--stop|--scan]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:slides:create</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:slides:create [topic]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:create</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:create [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:use-mcp</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:use-mcp</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:journal</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:journal</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:kanban</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:kanban</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:watzup</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:watzup</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:worktree</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:worktree</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:two</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:plan --two [task]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:plan:ci</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:fix ci [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:ck-help</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:ck-help</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:write:blog-youtube</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:write:blog-youtube [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:add</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:add [file]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:fix-logs</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:fix-logs</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:optimize</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:optimize [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:optimize:auto</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:optimize:auto [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:plan</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:plan [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:skill:update</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:skill:update [name]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:test:ui</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:test:ui [url]</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/mkt:test:workflow</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:test:workflow [name]</code></td>
</tr>
<tr class="border-b border-purple-100 dark:border-purple-900/30 bg-purple-50/30 dark:bg-purple-900/5">
<td colspan="2" class="py-1.5 px-3 text-[10px] font-semibold text-purple-600 dark:text-purple-400">📝 Renamed Skills — Marketing-exclusive (ckm:)</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/brand-guidelines</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:brand</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/campaign-management</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:campaign</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/competitor-alternatives</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:competitor</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/Debugging</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:debugging</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/email-marketing</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:email</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/seo-optimization</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:seo</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/slides-design</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:slides</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/social-media</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:social</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/video-production</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:video</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/youtube-handling</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-purple-100 dark:bg-purple-900/30 text-purple-600 dark:text-purple-400 px-1 py-0.5 rounded">/ckm:youtube</code></td>
</tr>
<tr class="border-b border-teal-100 dark:border-teal-900/30 bg-teal-50/30 dark:bg-teal-900/5">
<td colspan="2" class="py-1.5 px-3 text-[10px] font-semibold text-teal-600 dark:text-teal-400">📝 Renamed Skills — Shared with Engineer Kit (ck:)</td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/frontend-dev-guidelines</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:frontend-development</code></td>
</tr>
<tr class="border-b border-slate-100 dark:border-slate-800">
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/Problem-Solving Techniques</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:problem-solving</code></td>
</tr>
<tr>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-slate-100 dark:bg-slate-800 px-1 py-0.5 rounded">/remotion-best-practices</code></td>
<td class="py-1.5 px-3"><code class="sourceCode mandoc text-[10px] bg-teal-100 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400 px-1 py-0.5 rounded">/ck:remotion</code></td>
</tr>
</tbody>
</table>

 Show all migrations (79 more)

####  Token Consumption /skill ⚡

**⚡ = Token Consumption - Ước tính dung lượng context khi skill được activated.** Chỉ mang tính tham khảo.

**Weight-based** means the token cost scales with the skill's SKILL.md prompt size. A ⚡ skill loads \<5K tokens into context, while ⚡⚡⚡⚡ loads 50K-100K — directly reducing your remaining conversation budget.

⚡

\<5K

Dùng thoải mái

⚡⚡

5K-20K

Nhẹ nhàng

⚡⚡⚡

20K-50K

Cân nhắc khi dùng

⚡⚡⚡⚡

50K-100K

Tốn context

##  Tất Cả Lệnh Theo Danh Mục

  Engineer Kit 

  Marketing Kit 

v2.17.0 Stable v2.17.0-beta.24 Beta Phiên bản stable & beta hiện tại của Engineer Kit

###  Beta Preview

Skill mới và cải tiến lớn trong Engineer Kit Beta

`/ck:tech-graph` new

Tạo SVG technical diagram chất lượng publication

7 phong cách thiết kế (modern, minimal, neon, retro,...) và 10 template (architecture, sequence, ER, flow).\
Output SVG sẵn sàng cho docs, slides, blog post.

`/ck:scenario` enhanced

Iterative saturation mode để generate edge-case

Flag mới `--saturation` và `--iterations N` loop generation qua 12 dimension, phân loại từng candidate là New/Variant/Duplicate.\
Halt khi 2 iteration liên tiếp không sinh scenario mới — xác nhận đã coverage hết thay vì dừng tùy hứng.

`/ck:security` enhanced

Multi-persona red-team discovery loop

Mode mới `--red-team` chạy 4 attacker persona (security adversary, supply chain, insider, infrastructure) iterative trước khi sweep STRIDE/OWASP.\
Kết hợp với `--fix` để discovery + auto-fix các finding Critical/High.

`/ck:autoresearch` enhanced

Reframe thành autoresearch family router

Không còn là deprecated alias của `ck-loop` — giờ là umbrella concept anchor giải thích autoresearch pattern (Udit Goenka, MIT) và route sang 4 skill chuyên biệt: `ck-loop`, `ck-predict`, `ck-scenario`, `ck-security`.\
Bắt đầu ở đây để học lineage, rồi chọn skill chuyên biệt phù hợp.

`/ck:predict` enhanced

Chain mode refinement sau khi có verdict

Flag mới `--chain reason` chạy subjective refinement loop (generate → critique → synthesize → blind judge) lặp đến khi convergence — cho verdict CAUTION với subjective tradeoff.\
Flag mới `--chain probe` drive saturation-based interrogation để harvest missing constraint và unstated assumption khi verdict báo requirement chưa đầy đủ.

`/ck:ck-plan` enhanced

Whole-Plan Consistency Gate trước khi recommend cook

Sau khi validate/red-team chỉnh plan, tự re-scan toàn bộ plan.md + mọi phase-\*.md tìm stale term, decision đã bị supersede, draft duplicate.\
Chỉ cho cook khi zero contradiction còn lại. `--fast` không còn auto chain sang `--auto`.

`/ck:bootstrap` enhanced

Default mode đổi sang `--full` (interactive)

Behavior change: default từ `--auto` chuyển sang `--full`; `--auto` giờ là explicit autonomous opt-in.\
`--fast` giữ cook review gate thay vì force `--auto`.

`/ck:preview` enhanced

Visual self-review cho diagram output

`--diagram`/`--html --diagram` giờ load lại SVG/PNG đã render dưới dạng image rồi inspect collision (arrow xuyên box, label overlap, legend che content).\
Lặp re-render đến khi diagram clean visually.

`/ck:kanban` deprecated

Đã gỡ khỏi beta — sắp gỡ khỏi stable

Skill `/ck:kanban` standalone đã bị gỡ ở beta.8. Dùng `/ck:plans-kanban` thay thế.\
Stable users vẫn còn truy cập đến khi bản stable kế tiếp gỡ luôn.

`/ck:mcp-management` deprecated

Đã gỡ khỏi beta — thay bằng /ck:use-mcp

`/ck:mcp-management` được hợp nhất vào `/ck:use-mcp` ở beta.8 (rename assets, scripts, references).\
Stable vẫn giữ cả hai đến khi bản stable kế tiếp gỡ `mcp-management`.

`/ck:chrome-devtools` deprecated

Đã gỡ khỏi beta — thay bằng /ck:agent-browser

Skill `/ck:chrome-devtools` dựa trên Puppeteer đã bị gỡ ở beta.12. Mọi reference trong `bootstrap`, `ck-debug`, `design`, `fix`, `frontend-design`, `show-off`, `test`, và `ui-ux-designer` đã chuyển sang `/ck:agent-browser`.\
Stable vẫn giữ cả hai đến khi bản stable kế tiếp gỡ `chrome-devtools`.

###  Bắt Đầu (Cơ Bản)

Bắt đầu với quy trình cơ bản: Hướng dẫn → Cấp độ → Hỏi → Brainstorm → Lập kế hoạch → Thực thi

`/ck:ck-help` deprecated

⚡

Hướng dẫn sử dụng ClaudeKit

Khám phá commands, skills, và workflows một cách tương tác.

 1  `/ck:coding-level`

⚡

Đặt mức độ kinh nghiệm lập trình (0-5)

Tùy chỉnh giải thích từ người mới bắt đầu đến chuyên gia.

 2  `/ck:ask`

⚡

Trả lời câu hỏi kỹ thuật và kiến trúc

Tư vấn chuyên gia cho quyết định công nghệ.

` [question] `

 3  `/ck:brainstorm`

⚡

Brainstorm giải pháp với phân tích đánh đổi

Bao gồm đánh giá thẳng thắn. Điểm khởi đầu tốt cho bất kỳ tính năng nào.

 4  `/ck:plan`

⚡⚡⚡

Tạo kế hoạch triển khai chi tiết

Chế độ research, validation, và archival. Dùng subcommand archive, red-team, validate.

` archive `` red-team `` validate `

` --auto `` --fast `` --hard `` --parallel `` --two `` --no-tasks `` --deep `` --tdd `

 5  `/ck:cook`

⚡⚡⚡

Triển khai tính năng tất cả trong một

Research → plan → implement → test → review. Sử dụng Claude Tasks để điều phối.

` --interactive `` --fast `` --parallel `` --auto `` --no-test `` --tdd `

###  Lập Kế Hoạch & Nghiên Cứu

Brainstorm, lập kế hoạch và khám phá codebase

`/ck:brainstorm`

⚡

Brainstorm giải pháp với phân tích đánh đổi

Bao gồm đánh giá thẳng thắn. Điểm khởi đầu tốt cho bất kỳ tính năng nào.

`/ck:research`

⚡⚡

Nghiên cứu kỹ thuật và đánh giá công nghệ

Best practices, thiết kế giải pháp.

` [topic] `

`/ck:scout`

⚡

Quét nhanh codebase

Các agent song song để khám phá file. Dùng flag ext để lọc theo loại file.

` [search-target] `` [ext] `

`/ck:plan`

⚡⚡⚡

Tạo kế hoạch triển khai chi tiết

Chế độ research, validation, và archival. Dùng subcommand archive, red-team, validate.

` archive `` red-team `` validate `

` --auto `` --fast `` --hard `` --parallel `` --two `` --no-tasks `` --deep `` --tdd `

`/ck:sequential-thinking`

⚡⚡

Suy luận từng bước với khả năng tự điều chỉnh

Phân tích đa bước, kiểm chứng giả thuyết, lập kế hoạch thích ứng.

`/ck:problem-solving`

⚡⚡

Gỡ bế tắc khi giải quyết vấn đề phức tạp

Phá vỡ vòng lặp phức tạp, thử nghiệm giả định, đơn giản hóa bài toán.

`/ck:loop`

⚡⚡⚡

Vòng lặp tối ưu hóa tự động

Chạy N lần lặp theo metric, học từ git history, tự động giữ/bỏ thay đổi. Cho coverage, performance, bundle size.

`/ck:autoresearch` deprecated

⚡⚡⚡

Vòng lặp tối ưu hóa tự động lặp lại

Chạy N lần lặp theo metric, học từ git history, tự động giữ/bỏ thay đổi. Cho coverage, performance, bundle size.

`/ck:predict`

⚡⚡

Dự đoán kết quả và rủi ro trước khi triển khai

Phân tích thay đổi code, ước tính tác động, phát hiện lỗi tiềm ẩn trước khi xảy ra.

`/ck:xia`

⚡⚡⚡

Học hỏi, trích xuất và port tính năng từ repo khác một cách an toàn

Nghiên cứu mã nguồn thay thế (GitHub/Local) để phân tích kiến trúc tính năng. Sử dụng Challenge Framework để đánh giá rủi ro trước khi triển khai, tránh blind copy-paste.

` <github-url|owner/repo|local-path> `` [feature] `

` --compare `` --copy `` --improve `` --port `` --auto `` --fast `

###  Thiết Kế & Frontend

Thiết kế UI/UX, phát triển frontend, đồ họa 3D và công cụ trực quan

`/ck:frontend-design`

⚡⚡⚡

Tạo giao diện frontend hoàn thiện

Từ bản thiết kế, screenshots, hoặc videos.

`/ck:frontend-development`

⚡⚡⚡

Xây dựng frontend React/TypeScript

Các pattern hiện đại, MUI v7, TanStack.

`/ck:ui-styling`

⚡⚡

Tạo style UI với shadcn/ui

Radix UI + Tailwind CSS. Dark mode, hệ thống thiết kế.

`/ckm:design`

⚡⚡⚡⚡

Nhận diện thương hiệu, logo, CIP, slides, banner, icon

55 kiểu logo, 50 deliverable CIP, ảnh mạng xã hội. Tạo ảnh bằng Gemini AI.

`/ck:stitch`

⚡⚡⚡

Tạo thiết kế AI qua Google Stitch

Tạo UI chất lượng cao từ text prompt. Export Tailwind/HTML. Pipeline thiết kế sang code.

` generate `` export `

` --format all `` --format html `` --device mobile `

`/ck:ui-ux-pro-max`

⚡⚡⚡⚡

50+ styles, 161 bảng màu, 57 bộ font ghép đôi

161 loại sản phẩm, 99 hướng dẫn UX, 25 loại chart, 10 stacks.

`/ck:web-design-guidelines`

⚡⚡

Đánh giá UI theo tiêu chuẩn Web Interface Guidelines

Kiểm tra code theo tiêu chuẩn design guidelines.

`/ck:threejs`

⚡⚡⚡

Xây dựng ứng dụng web 3D với Three.js

WebGL/WebGPU. 556 ví dụ, 60 API class.

`/ck:shader`

⚡⚡⚡

Viết GLSL fragment shaders

Đồ họa thủ tục và nghệ thuật sinh tạo. Hoạt động với Three.js.

`/ck:mermaidjs-v11`

⚡

Sơ đồ luồng, biểu đồ, Gantt, timeline

Biểu đồ sequence, class, ER, state sử dụng Mermaid v11.

`/excalidraw`

⚡⚡

Diagram hand-drawn với Excalidraw

Architecture, flowcharts, system designs phong cách hand-drawn. Auto-diagram để visualization codebase không cần config.

###  AI Generation & Multimodal

Tạo hình ảnh/video, phân tích AI và xử lý media

`/ck:ai-multimodal`

⚡⚡⚡

Phân tích ảnh/audio/video với Gemini API

Tạo ảnh (Imagen 4, Nano Banana 2), video (Veo 3, Hailuo).

`/ck:ai-artist`

⚡⚡⚡⚡

Tạo ảnh qua Nano Banana

129 prompt được tuyển chọn. Bắt buộc validation.

` --mode search `` --mode creative `` --mode wild `` --mode all `` --skip `

`/ck:media-processing`

⚡⚡

FFmpeg, ImageMagick, xóa nền bằng AI

Xử lý video/audio, ảnh, và các thao tác RMBG.

`/ck:remotion`

⚡⚡

Tạo video lập trình trong React

Xây dựng video components với React và render ra MP4.

###  Xây Dựng & Triển Khai

Backend, framework, database, DevOps, mobile và deployment

`/ck:bootstrap`

⚡⚡⚡⚡⚡

Khởi tạo dự án đầy đủ từ đầu

Cài đặt tech stack, lập kế hoạch, thiết kế, và triển khai.

` --full `` --auto `` --fast `` --parallel `

`/ck:backend-development`

⚡⚡⚡

API Node.js, Python, Go

NestJS, FastAPI, Django. REST/GraphQL/gRPC.

`/ck:web-frameworks`

⚡⚡⚡

Monorepo Next.js, Turborepo

Hỗ trợ App Router, RSC, SSR, ISR.

`/ck:databases`

⚡⚡

MongoDB, PostgreSQL, SQL/NoSQL

Queries, aggregation, index, migration.

`/ck:tanstack`

⚡⚡

TanStack Start, Form, AI

Streaming/chat với TanStack AI.

`/ck:react-best-practices`

⚡⚡

Tối ưu hiệu suất React/Next.js

Từ các pattern của Vercel Engineering.

`/ck:devops`

⚡⚡⚡

Cloudflare, Docker, GCP, Kubernetes

Triển khai Workers, R2, D1, Cloud Run.

`/ck:ship`

⚡⚡⚡

Ship feature branch với pipeline tự động

merge → test → review → version → changelog → push → PR

` --official `` --beta `` --skip-tests `` --skip-review `

`/ck:mobile-development`

⚡⚡⚡

React Native, Flutter, Swift, Kotlin

Hỗ trợ SwiftUI và Jetpack Compose.

`/ck:team`

⚡⚡⚡⚡⚡

Điều phối Agent Teams

Cộng tác đa phiên song song. Template: research, implement, review, debug.

` <template> <context> `` --devs N `` --researchers N `` --reviewers N `` --delegate `

`/ck:deploy`

⚡⚡

Tự động phát hiện và triển khai lên 15 nền tảng

Vercel, Netlify, Cloudflare, Railway, Fly.io, Render, Heroku, GitHub Pages, AWS, GCP, và nhiều hơn.

` [platform] `` [environment] `

`/ck:cook`

⚡⚡⚡

Triển khai tính năng tất cả trong một

Research → plan → implement → test → review. Sử dụng Claude Tasks để điều phối.

` --interactive `` --fast `` --parallel `` --auto `` --no-test `` --tdd `

###  Git & Quản Lý Phiên Bản

Thao tác Git, conventional commits, worktree và quản lý branch

`/ck:git`

⚡

Thao tác Git với conventional commits

Tự động chia theo loại/phạm vi. Quét bảo mật trước khi commit.

` cm `` cp `` pr `` merge `

`/ck:worktree`

⚡⚡

Git worktree cô lập cho phát triển song song

Tạo feature branch trong thư mục riêng. Phù hợp cho monorepo.

###  Kiểm Thử & Debug

Testing, code review, debugging và edge-case scenarios

`/ck:test`

⚡

Chạy test cục bộ và test UI

Chạy toàn bộ suite, module cụ thể, hoặc test UI trực quan trên website thực.

` [context] `` ui [url] `

`/ck:code-review`

⚡⚡⚡

Đánh giá chất lượng code

Phát hiện edge case dựa trên Scout và điều phối pipeline Task.

` [context] `` #PR `` COMMIT `` --pending `` codebase `` codebase parallel `

`/ck:fix`

⚡⚡

Chẩn đoán & sửa lỗi có cấu trúc (v2.0)

Pipeline 6 bước: Scout → Chẩn đoán → Đánh giá → Sửa → Xác minh → Phòng ngừa. RCA dựa trên bằng chứng.

` --auto `` --review `` --quick `` --parallel `

`/ck:debug`

⚡⚡

Phân tích nguyên nhân gốc có hệ thống

Truy vết call stack, validation đa lớp. Dùng khi không biết vấn đề ở đâu.

`/ck:web-testing`

⚡⚡

Testing với Playwright, Vitest, k6

Test E2E/unit/integration/load/bảo mật/visual/a11y.

`/ck:agent-browser`

⚡⚡

CLI tự động hóa trình duyệt tối ưu cho AI

Snapshot hiệu quả về context cho các tương tác web phức tạp.

`/ck:chrome-devtools`

⚡⚡

Tự động hóa với Puppeteer

Chụp màn hình, hiệu suất, giám sát mạng, scraping.

`/ck:scenario`

⚡⚡

Khám phá các kịch bản what-if cho quyết định kiến trúc

Mô hình hóa nhiều cách tiếp cận, so sánh đánh đổi, mô phỏng kết quả.

###  Bảo Mật & Tình Báo

Audit bảo mật, quét lỗ hổng, xác thực và threat intelligence

`/ck:security`

⚡⚡⚡

Phân tích bảo mật toàn diện và tăng cường

Mô hình hóa mối đe dọa, đánh giá lỗ hổng, lộ trình khắc phục.

`/ck:security-scan`

⚡⚡

Quét codebase tìm lỗ hổng bảo mật

Phân tích bảo mật tự động với gợi ý khắc phục.

` [scope] `

` --secrets-only `` --deps-only `` --full `

`/ck:better-auth`

⚡⚡

Auth TypeScript: OAuth, 2FA, passkeys

Hỗ trợ RBAC, WebAuthn, MFA.

`/ck:cti-expert`

⚡⚡⚡⚡

Bộ công cụ điều tra CTI/OSINT

Cyber threat intelligence và open-source investigation: case timeline, recon, kiểm tra breach, digital footprint, forensics ảnh/blockchain. Không cần API key.

` [target] `

` --yolo `` --case `` --sweep `` --query `` --flow `

###  Tài Liệu & Nội Dung

Quản lý tài liệu, viết nội dung và xem file

`/ck:docs`

⚡⚡⚡

Phân tích codebase và quản lý tài liệu

Khởi tạo, cập nhật, hoặc tóm tắt tài liệu dự án.

` init `` update `` summarize `

`/ck:docs-seeker`

⚡

Tìm kiếm tài liệu thư viện/framework

Qua llms.txt (context7.com). Cách nhanh nhất để lấy tài liệu cập nhật.

`/ck:copywriting`

⚡⚡

Tiêu đề, CTA, landing page

Email copy, phong cách viết, copy tập trung vào chuyển đổi.

` [copy-type] [context] `

`/ck:mintlify`

⚡⚡

Trang tài liệu với Mintlify

MDX components, theme, OpenAPI.

`/ck:show-off`

⚡⚡

Tạo HTML showcase ấn tượng cho demo và mạng xã hội

Trang cuộn nhiều section với parallax, chuyển đổi theme, song ngữ (VI/EN). Tự động chụp từng section thành ảnh ở nhiều tỷ lệ (16:9, 9:16, 1:1).

`/ck:preview`

⚡

Xem file hoặc tạo giải thích trực quan

Markdown hoặc self-contained HTML. Modes: --explain, --slides, --diagram, --diff, --plan-review, --recap. Thêm --html để mở trên browser.

` --explain `` --slides `` --diagram `` --ascii `` --html `` --diff `` --plan-review `` --recap `

`/ck:tech-graph` beta

⚡⚡

Tạo SVG technical diagram chất lượng publication

7 phong cách thiết kế (modern, minimal, neon, retro,...) và 10 template (architecture, sequence, ER, flow). Output SVG sẵn sàng cho docs, slides, blog post.

`/ck:markdown-novel-viewer`

⚡

Đọc kiểu sách qua HTTP server

Đọc thoải mái cho các file markdown.

`/ck:llms`

⚡⚡

Tạo file llms.txt từ docs hoặc codebase

Tuân theo spec llmstxt.org. Bao gồm file tham chiếu và script tạo.

###  MCP & Tích Hợp

MCP server, thanh toán, Shopify và tích hợp AI agent

`/ck:mcp-builder`

⚡⚡⚡

Xây dựng MCP server

FastMCP (Python), MCP SDK (Node/TypeScript).

`/ck:mcp-management`

⚡⚡

Khám phá và quản lý MCP tools

Prompts, resources, và các thao tác server.

`/ck:use-mcp`

⚡

Sử dụng MCP server tools

Khám phá và thực thi thông minh.

`/ck:payment-integration`

⚡⚡⚡

SePay, Polar, Stripe, Paddle, Creem.io

VietQR và các nhà cung cấp thanh toán quốc tế.

`/ck:shopify`

⚡⚡

Ứng dụng Shopify và Liquid templates

Polaris UI, tùy chỉnh checkout.

`/ck:google-adk-python`

⚡⚡⚡

Xây dựng AI agent với Google ADK Python

Giao thức A2A, tích hợp MCP tools.

`/ck:agentize`

⚡⚡⚡

Chuyển codebase thành CLI + MCP server thân thiện AI agent

Wrap code thành CLI/MCP với shared core/. Agent-centric design. Mode: --both, --mcp, --cli.

` --both `` --mcp `` --cli `

###  Quản Lý Phiên Làm Việc

Xem lại phiên, viết nhật ký và tối ưu context

`/ck:watzup`

⚡

Xem lại thay đổi gần đây và kết thúc phiên

Xem những gì đã thay đổi, review diff, và đóng phiên làm việc.

`/ck:journal`

⚡

Viết nhật ký phân tích thay đổi

Ghi lại các suy nghĩ và quyết định kỹ thuật.

`/ck:context-engineering`

⚡

Giám sát sử dụng context và tối ưu token

Kiểm tra giới hạn và tối ưu hóa mức tiêu thụ context window.

`/ck:retro`

⚡⚡

Retrospective sprint dựa trên dữ liệu

Git metrics, chỉ số sức khỏe, và đề xuất hành động.

` [timeframe] `

` --compare `` --team `` --format html|md `

###  Theo Dõi Dự Án

Theo dõi tiến độ, kanban board và quản lý kế hoạch

`/ck:project-management`

⚡⚡

Theo dõi tiến độ và quản lý Claude Tasks

Tạo báo cáo, phối hợp tài liệu. Tasks: status, hydrate, sync, report.

` status `` hydrate `` sync `` report `

`/ck:kanban`

⚡

Bảng điều phối AI agent

Trực quan hóa task cho quy trình agent.

`/ck:plans-kanban`

⚡

Bảng kế hoạch với theo dõi tiến độ

Trực quan hóa timeline và tiến độ.

`/ck:project-organization`

⚡⚡

Tổ chức cấu trúc dự án và bố cục file

Phân tích và tái cấu trúc thư mục dự án để dễ bảo trì.

###  Tiện Ích

Quản lý skill, đóng gói code, phân tích ngữ nghĩa và công cụ hỗ trợ

`/ck:skill-creator`

⚡⚡

Tạo/cập nhật Claude skills

3 sub-agent (analyzer, comparator, grader). Hạ tầng eval với benchmarks.

`/ck:find-skills`

⚡

Khám phá và cài đặt skill từ hệ sinh thái

Tìm kiếm theo khả năng hoặc mô tả task.

`/ck:repomix`

⚡⚡

Đóng gói repositories thành file thân thiện với AI

Đầu ra định dạng XML, markdown, plain, hoặc JSON.

` --style xml `` --style markdown `` --style plain `` --style json `

`/ck:gkg`

⚡

Phân tích code ngữ nghĩa

Tích hợp GitLab Knowledge Graph.

`/ck:graphify`

⚡⚡

Xây dựng knowledge graph có thể query

Chuyển code, docs, papers, images thành knowledge graphs. Tree-sitter AST cho 20 ngôn ngữ.

` [path] `

` --mcp `` --report `` --watch `

v1.3.2 Stable Phiên bản stable & beta hiện tại của Marketing Kit

###  Bắt Đầu (Theo Từng Bước)

Bắt đầu với quy trình cơ bản: Hướng dẫn → Khởi tạo → Hỏi → Brainstorm → Lập kế hoạch → Viết

`/ckm:ck-help` deprecated

⚡

Hướng dẫn sử dụng ClaudeKit

Khám phá skill, lệnh và quy trình làm việc một cách tương tác.

 1  `/ckm:init`

⚡⚡

Khởi tạo dự án marketing

Thiết lập cấu trúc dự án, brand guidelines và không gian làm việc marketing.

 2  `/ckm:ask`

⚡

Tư vấn chuyên gia marketing

Tư vấn chuyên gia về chiến lược, kênh và chiến thuật marketing.

` [question] `

 3  `/ck:brainstorm`

⚡

Sáng tạo ý tưởng & phân tích đánh đổi

Tạo ý tưởng chiến dịch, góc nhìn và concept sáng tạo nhanh chóng.

 4  `/ckm:plan:*`

⚡⚡⚡

Lập kế hoạch chiến dịch & chiến lược

Framework RACE, SOSTAC, STP. Subcommand: cro, fast, hard, parallel.

` :cro `` :fast `` :hard `` :parallel `` :archive `` :ci `` :two `` :validate `

 5  `/ckm:write:good`

⚡⚡⚡

Viết chất lượng cao có review

Quy trình đầy đủ: nháp → review → hoàn thiện. Tốt nhất cho sản phẩm cuối.

###  Nội Dung & Copywriting

Công cụ tạo nội dung, viết copy và bài viết

`/ckm:write:*`

⚡⚡⚡

Trung tâm viết content

Viết nhanh, CRO copy, blog, audit, enhance — tất cả chế độ viết.

` :fast `` :good `` :cro `` :blog `` :audit `` :enhance `` :publish `` :formula `

`/ckm:content-marketing`

⚡⚡⚡

Chiến lược nội dung & lịch biên tập

Content pillar mapping, lịch biên tập và kế hoạch phân phối.

`/ckm:creativity`

⚡⚡

Phong cách sáng tạo & định dạng nền tảng

55 phong cách, 18 nền tảng, 12 loại voiceover, 30 danh mục chiến dịch.

`/ck:copywriting`

⚡⚡

Công thức viết copy chuyển đổi

Tiêu đề, CTA và framework thuyết phục cho copy chuyển đổi cao.

###  Quản Lý Chiến Dịch

Điều phối và theo dõi chiến dịch đa kênh

`/ckm:campaign:*`

⚡⚡⚡⚡

Điều phối chiến dịch đa kênh

Lên kế hoạch và phối hợp chiến dịch qua email, mạng xã hội, quảng cáo và nội dung.

` :create `` :status `` :analyze `` :email `

###  SEO & Phân Tích

Tối ưu tìm kiếm và phân tích hiệu suất

`/ckm:seo:*`

⚡⚡⚡

Trung tâm SEO

Nghiên cứu từ khóa, audit site, SEO lập trình — tất cả trong một lệnh.

` :audit `` :keywords `` :pseo `

`/ckm:analyze:*`

⚡⚡

Báo cáo phân tích & hiệu suất

Phân tích hiệu suất nội dung, mức độ tương tác và chuyển đổi.

` :report `

`/ckm:ab-test-setup`

⚡⚡⚡

Thiết kế & lập kế hoạch A/B test

Lên kế hoạch thí nghiệm, định nghĩa giả thuyết, kích thước mẫu và chỉ số thành công.

`/ckm:analytics`

⚡⚡

Theo dõi KPI & báo cáo

Thiết lập và theo dõi chỉ số marketing quan trọng và dashboard hiệu suất.

`/ckm:ads-management`

⚡⚡⚡⚡

Quản lý quảng cáo (Google, Meta, LinkedIn, TikTok)

Thiết lập chiến dịch, đấu thầu, creative assets và đo lường.

` [platform] `` [campaign-type] `

`/ckm:paid-ads`

⚡⚡⚡

Chiến lược PPC & tối ưu ROAS

Ad copy, retargeting, phân bổ ngân sách và tinh chỉnh hiệu suất.

` [platform] `` [campaign-type] `

###  Thiết Kế & Hình Ảnh

Thiết kế marketing, banner, logo và hình ảnh

`/ckm:design`

⚡⚡⚡⚡

Thiết kế marketing toàn diện

Thiết kế nhất quán thương hiệu cho mọi tài sản marketing với quy trình đầy đủ.

` logo `` cip `` banner `` icon `` social `` slides `

`/ckm:design-system`

⚡⚡⚡

Design token & hệ thống component

Design token 3 lớp (primitive → semantic → component), CSS variables.

###  Email & Mạng Xã Hội

Chuỗi email và outreach mạng xã hội

`/ckm:email:*`

⚡⚡⚡

Trung tâm email marketing

Luồng email, chuỗi email, newsletter — lệnh email thống nhất.

` :flow `` :sequence `

`/ckm:social:*`

⚡⚡

Trung tâm mạng xã hội

Nội dung đa nền tảng, lên lịch và phân tích.

` :schedule `

` [platform] `` [type] `

`/ckm:elevenlabs`

⚡⚡

ElevenLabs TTS & giọng nói

Chuyển văn bản thành giọng nói, clone giọng, và tạo hiệu ứng âm thanh.

` speak `` clone `` sfx `

###  Chiến Lược & Nghiên Cứu

Lập kế hoạch, phân tích đối thủ và xây dựng persona

`/ck:brainstorm`

⚡

Sáng tạo ý tưởng & phân tích đánh đổi

Tạo ý tưởng chiến dịch, góc nhìn và concept sáng tạo nhanh chóng.

`/ckm:plan:*`

⚡⚡⚡

Lập kế hoạch chiến dịch & chiến lược

Framework RACE, SOSTAC, STP. Subcommand: cro, fast, hard, parallel.

` :cro `` :fast `` :hard `` :parallel `` :archive `` :ci `` :two `` :validate `

`/ckm:competitor`

⚡⚡⚡

Phân tích tình báo đối thủ

Phân tích định vị, messaging và chiến thuật marketing của đối thủ.

` analyze `` content `` seo `` alternatives `` list `

`/ckm:persona`

⚡⚡

Xây dựng buyer persona

Persona dựa trên dữ liệu: nhân khẩu học, mục tiêu, điểm đau và kênh.

`/ckm:funnel`

⚡⚡⚡

Thiết kế & phân tích phễu

Lập bản đồ hành trình khách hàng, xác định điểm rời bỏ và tối ưu chuyển đổi.

` design `` analyze `` optimize `

`/ckm:marketing-planning`

⚡⚡⚡

Framework lập kế hoạch chiến lược

Framework RACE, SOSTAC, STP cho lập kế hoạch marketing toàn diện.

`/ckm:marketing-research`

⚡⚡⚡

Nghiên cứu thị trường & insight khách hàng

Nghiên cứu xu hướng thị trường, đối thủ và hành vi khách hàng.

`/ckm:marketing-ideas`

⚡⚡

140 chiến thuật marketing đã kiểm chứng

Duyệt chiến thuật marketing theo danh mục và áp dụng cho ngách của bạn.

`/ckm:marketing-psychology`

⚡⚡⚡

70+ mô hình tâm lý marketing

Thiên kiến nhận thức, nguyên tắc thuyết phục và mô hình hành vi người tiêu dùng.

`/ckm:play:*`

⚡⚡⚡

Playbook orchestrator với gợi ý thông minh

Tạo marketing playbook từ template với mục tiêu, milestones, và gợi ý bước tiếp theo.

` :create `` :next `` :status `` :list `` :blocked `` :learn `` :reset `` :gate `` :templates `` :goals `

###  Video & Media

Sản xuất video, YouTube và slide thuyết trình

`/ckm:video:*`

⚡⚡⚡

Sản xuất video & kịch bản

Tài liệu sản xuất đầy đủ: concept, kịch bản, danh sách cảnh quay và CTA.

` :create `` :script `` :storyboard `

`/ckm:youtube:*`

⚡⚡

Tái sử dụng & tối ưu YouTube

Tiêu đề, mô tả, tags, thumbnail và chiến lược kênh.

` :blog `` :infographic `` :social `

`/ckm:slides:*`

⚡⚡

Tạo slide thuyết trình

Deck thuyết trình cho pitch, webinar và hỗ trợ bán hàng.

` :create `

` [topic] `

`/ckm:youtube-thumbnail-design`

⚡⚡⚡

Thiết kế thumbnail YouTube tối ưu CTR

17 phong cách, hướng dẫn theo niche. Tạo ảnh AI bằng Gemini. Hỗ trợ facecam, listicle, bold-text, dark-dramatic.

` [niche] `` [style] `

###  Tăng Trưởng & CRO

Chiến lược ra mắt, định giá, giới thiệu và tối ưu chuyển đổi

`/ckm:launch-strategy`

⚡⚡⚡⚡

Ra mắt sản phẩm & go-to-market

Product Hunt, beta launch, waitlist và playbook go-to-market.

` [product] `

`/ckm:pricing-strategy`

⚡⚡⚡

Phân tầng giá & đóng gói

Freemium, Van Westendorp, giá theo tầng và chiến lược đóng gói.

` [product] `` [tier] `

`/ckm:free-tool-strategy`

⚡⚡⚡

Công cụ miễn phí cho lead gen & SEO

Engineering-as-marketing: xây công cụ miễn phí để thu hút người dùng.

` [tool-idea] `` [niche] `

`/ckm:gamification-marketing`

⚡⚡⚡

Gamification cho tương tác

Điểm, huy hiệu, bảng xếp hạng và streak cho chương trình loyalty.

` [mechanic] `` [campaign] `

`/ckm:affiliate-marketing`

⚡⚡⚡

Thiết kế chương trình affiliate

Chương trình affiliate SaaS, KOL/KOC, chống gian lận, hoa hồng 20-40%.

` [program] `` [strategy] `

`/ckm:referral-program-building`

⚡⚡⚡

Xây dựng chương trình referral

Viral loop, phần thưởng 2 chiều, lựa chọn nền tảng (Rewardful, Viral Loops).

` [product] `` [program-type] `

`/ckm:form-cro`

⚡⚡

Tối ưu chuyển đổi form

Tối ưu form lead capture, liên hệ và yêu cầu demo.

` [form-url] `

`/ckm:onboarding-cro`

⚡⚡⚡

Tối ưu luồng onboarding

Kích hoạt sau đăng ký, trải nghiệm lần đầu và empty state.

` [flow-url] `

###  Kiểm Thử & Debug

Kiểm thử, debug và review chất lượng code

`/ckm:test:*`

⚡

Kiểm thử tự động

Chạy kiểm thử tự động cho trang marketing và chiến dịch.

` :ui `` :workflow `

`/ck:code-review`

⚡⚡⚡

Review chất lượng code

Review code marketing: landing page, email và tracking script.

` codebase `` codebase parallel `

` [context] `

`/ckm:debugging`

⚡⚡

Framework debug marketing

Debug vấn đề campaign, tracking pixel, UTM, và analytics.

###  Git & Quản Lý Version

Quản lý version, commit và tạo pull request

`/ck:git`

⚡

Git operations (commit, push, PR)

Stage, commit với message, push lên remote và tạo pull request.

` cm `` cp `` pr `

`/ckm:worktree`

⚡⚡

Quản lý git worktree

Làm việc song song trên nhiều nhánh trong thư mục riêng biệt.

###  Quản Lý Session

Theo dõi tiến độ và wrap up session làm việc

`/ckm:watzup`

⚡

Xem lại thay đổi gần đây

Tổng quan nhanh trạng thái phiên hiện tại và hoạt động gần đây.

`/ckm:journal`

⚡

Viết nhật ký & ghi chú

Lưu quyết định quan trọng, bài học và context cho phiên sau.

###  Theo Dõi Dự Án

Quản lý project, kanban và tổ chức công việc

`/ckm:kanban`

⚡

Bảng điều phối agent

Bảng kanban trực quan cho task marketing và tiến trình chiến dịch.

`/ckm:dashboard:*`

⚡⚡

Marketing Dashboard

Dashboard chỉ số marketing trực quan với theo dõi KPI.

` :check `

`/ckm:brand`

⚡⚡

Quản lý brand guidelines

Tạo và cập nhật brand guidelines, màu sắc, typography và giọng điệu.

` :update `

`/ckm:docs:*`

⚡⚡

Quản lý tài liệu

Khởi tạo, cập nhật và tóm tắt tài liệu dự án marketing.

` :init `` :llms `` :summarize `` :update `

`/ckm:hub`

⚡

Content Hub + Dashboard

Dashboard trung tâm cho tất cả tài sản marketing và nội dung.

` --stop `` --scan `

`/ckm:storage:*`

⚡

Quản lý lưu trữ S3

Quản lý tài sản marketing trên S3: liệt kê, đồng bộ, upload và lấy URL.

` :list `` :sync `` :upload `` :url `

###  Công Cụ & Tiện Ích

Tạo skill, MCP và các tiện ích mở rộng

`/ckm:skill:*`

⚡⚡

Tạo marketing skill mới

Xây dựng skill marketing tùy chỉnh theo chuẩn Skillmark.

` :add `` :create `` :fix-logs `` :optimize `` :plan `` :update `

`/ckm:use-mcp`

⚡

Khám phá công cụ MCP

Kết nối và sử dụng MCP server để mở rộng khả năng marketing.

`/ckm:preview`

⚡

Xem file & giải thích trực quan

Render markdown, diagram và slide trên trình duyệt.

` --explain `` --slides `` --diagram `` --ascii `

`/ckm:content-hub`

⚡⚡

Thư viện tài sản với tìm kiếm & lọc

Thư viện tài sản trên trình duyệt với brand context, sẵn sàng R2.

` open `` browse `` search `

`/ckm:assets-organizing`

⚡

Sắp xếp tài sản marketing

Sắp xếp output theo chủ đề, định dạng ngày và slug.

` [directory] `` [asset-type] `

`/ckm:kit-builder`

⚡⚡

Xây dựng component Marketing Kit

Tạo skill, agent và workflow tùy chỉnh cho Marketing Kit.

` [component-type] `` [name] `

`/ckm:claude-code`

⚡

Hướng dẫn Claude Code (marketing)

Hướng dẫn tập trung marketing cho các tính năng và workflow của Claude Code.

Truy cập [trang tài liệu chính thức của ClaudeKit để xem hướng dẫn đầy đủ.](https://docs.claudekit.cc/docs/engineer/skills)

