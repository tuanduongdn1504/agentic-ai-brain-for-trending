# ClaudeKit có làm hỏng setup Claude Code hiện tại của tôi không? - VividKit - Visual Interface cho ClaudeKit | VividKit

> Source URL: https://www.vividkit.dev/vi/guides/coexistence

> Extracted from: coexistence.html
> Method: bypass-403-escalation Tier 1 (Playwright + readability-lxml + pandoc)



  Coexistence guide 

## ClaudeKit có làm hỏng setup Claude Code hiện tại của tôi không?

Trả lời ngắn: **không, mặc định không.** ClaudeKit cài vào `./.claude/` của project hiện tại, preserve project config đã có, và merge chọn lọc `settings.json`. Command cần cẩn thận là `ck init --fresh`.

### Có đụng global config của tôi không?

Không, trừ khi thêm `--global`. Kit content mặc định cài trong project này.

### Có overwrite CLAUDE.md không?

Không trong update thường nếu file đã tồn tại. `CLAUDE.md` được xem là user config và bị skip.

### Custom skills của tôi sao?

Còn nguyên với install thường. `--fresh` có thể xóa file CK-tracked hoặc folder kit legacy.

### Project đã có .claude/ thì sao?

`ck init` thường scan `.claude/` trong project, protect custom files, và merge `.claude/settings.json`.

### Sau khi cài, ClaudeKit ở đâu?

Mặc định, ClaudeKit chỉ cài vào project bạn đang mở. Nó không thay đổi cài đặt Claude Code dùng chung trên máy bạn.

 ✓ Khuyên dùng 

#### Project install (mặc định)

``` bg-white/70
$ ck init
```

Ở: ./.claude/ (chỉ folder này)

- ✓ Ghi kit files vào `./.claude/` của *project này*
- ✓ `CLAUDE.md` và user config đã có trong project được preserve
- ✓ `./.claude/settings.json` đã có được merge chọn lọc
- ✓ `~/.claude/` global của bạn không bị đụng

 Chỉ khi bạn yêu cầu 

#### Global install (opt-in)

``` bg-white/70
$ ck init --global
```

Ở: ~/.claude/ (home của bạn)

- ! Dùng `~/.claude/` mặc định, hoặc `CLAUDE_CONFIG_DIR` nếu có set
- ! Global `settings.json` được merge chọn lọc; `CLAUDE.md` đã có được preserve
- ! Ảnh hưởng mọi project bạn mở

Claude đọc global và local CLAUDE.md thế nào?

Claude có thể load cả global và project `CLAUDE.md`. Các file này được nối vào context, không đơn giản là file sau thay file trước.

[Đọc Claude Mechanics](/vi/guides/claude-mechanics#config-hierarchy)

### ClaudeKit tránh clobber setup của bạn thế nào

Khi chạy `ck init` trong project đã có Claude Code config, ClaudeKit không bắt bạn chọn từng file một. Nó tự bảo vệ các file project config quan trọng, merge `settings.json`, và chỉ hỏi xác nhận nếu có file khác có nguy cơ bị ghi đè.

 ★ Default 

#### Protected user config

Các file đã có như `.gitignore`, `.mcp.json`, `.ck.json`, `.ckignore`, `.repomixignore`, và `CLAUDE.md` được preserve. File project-local trong `.claude/` nhưng không thuộc kit cũng được scan và protect.

Default cho `ck init` và update thường.

#### Selective settings merge

`settings.json` merge hooks và MCP servers, dedupe commands, preserve entries chỉ của user.

Chỉ bị bỏ qua khi bật `--force-overwrite-settings`; `--fresh` tự bật flag đó.

#### Overwrite confirmation

Với file khác đã tồn tại, interactive mode liệt kê conflicts và hỏi có tiếp tục không.

`--yes`, CI, hoặc non-interactive sẽ skip prompt; protected files và `settings.json` vẫn theo rule riêng, còn conflicts khác có thể bị overwrite.

#### ClaudeKit biết file nào do nó cài thế nào

ClaudeKit ghi file đã cài vào `metadata.json` và track riêng hooks/MCP servers đã inject. Metadata này dùng cho selective update, uninstall, và phân tích `--fresh`.

metadata.json + settings.json

ClaudeKit-tracked — refresh được

"hooks/session-init.cjs"

ownership: "ck"

User-owned — preserve

"your-custom-hook.sh"

preserved during settings merge

### Command nên backup trước khi chạy

`ck init --fresh` là full reset. Khi có `metadata.json` hiện tại, nó xóa file ClaudeKit-owned và ClaudeKit-modified, đồng thời preserve tracked user-created files. Nếu không có metadata dùng được, nó fallback sang xóa các kit folders: `commands/`, `agents/`, `skills/`, `rules/`, `hooks/`. Không có auto-backup.

#### Cái gì có thể bị xóa

Install legacy hoặc thiếu metadata có thể mất mọi thứ trong các folder này. Install hiện tại có tracking sẽ xóa CK-owned/modified files trong đó.

commands/ · agents/ · skills/ · rules/ · hooks/

 Flag `-y` không làm `--fresh` an toàn hơn; cứ xem nó là destructive cho tới khi đã backup.

#### Cách dùng `--fresh` an toàn

1.  

    1

    

    ##### Backup trước

    Copy folder `.claude/` sang folder timestamp. Mất 2 giây.

    

    ``` bg-slate-100
    $ cp -r ./.claude "./.claude.bak.$(date +%s)"
    ```

     

    

2.  

    2

    

    ##### Chạy `--fresh` có ý thức

    Bạn đã có safety net, nên file custom nào thiếu có thể restore thủ công.

    

    ``` bg-slate-100
    $ ck init --fresh
    ```

     

    

3.  

    3

    

    ##### Restore phần cần

    Copy file custom từ backup ngược trở lại, từng folder một.

    

    ``` bg-slate-100
    $ cp -r ./.claude.bak.<timestamp>/skills/my-skill ./.claude/skills/
    ```

     

    

Chỉ cần refresh kit content? Dùng `ck init --yes`. Chỉ dùng `ck update -y` khi muốn update CLI package; sau đó ClaudeKit có thể tự refresh kit content cho project/global đã cài, và sẽ bỏ qua nếu content đã latest.

### FAQ

ClaudeKit có overwrite CLAUDE.md của tôi không? 

`ck init` thường preserve `CLAUDE.md` đã có vì file này nằm trong user config. Global mode có thể copy `~/.claude/CLAUDE.md` khi chưa có; với `--fresh`, global `CLAUDE.md` có thể bị replace.

Custom commands và skills của tôi sao? 

`ck init` thường scan custom `.claude` files và protect chúng. Ngoại lệ là `--fresh`: nó xóa CK-owned/modified files, và install legacy thiếu metadata sẽ fallback sang xóa component directories.

Uninstall ClaudeKit thế nào? 

Dùng `ck uninstall`. Command này hỗ trợ `--local`, `--global`, `--all`, `--dry-run`, `--yes`, và mặc định preserve user-created hoặc modified files. Chỉ dùng `--force-overwrite` khi thật sự muốn full removal.

Update ClaudeKit an toàn thế nào? 

`ck init --yes` chỉ refresh kit content, không update CLI package. `ck update -y` update CLI package trước; sau đó có thể tự refresh kit content cho local/global install nếu content chưa latest. Tránh `--fresh` cho update thường.

