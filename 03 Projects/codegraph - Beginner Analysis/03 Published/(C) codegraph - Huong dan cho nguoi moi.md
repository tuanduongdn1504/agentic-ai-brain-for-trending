# codegraph — Hướng dẫn cho người mới (VN + EN)

> Bilingual beginner guide for v70 wiki subject · cấu trúc song ngữ tiếng Việt + English

---

## 1. codegraph là gì? / What is codegraph?

### VN

codegraph là một **công cụ index trước (pre-index) bản đồ code** cho các AI coding agent (Claude Code / Cursor / Codex CLI / OpenCode). Thay vì agent phải đi `grep`/`find`/`Read` mỗi lần khám phá codebase, codegraph index toàn bộ code thành một SQLite database (FTS5) và cho agent truy vấn ngay tức thì.

Kết quả benchmark trên 6 codebase thực tế: **94% ít tool call hơn**, **77% nhanh hơn**, **100% local** (không gửi data ra ngoài).

### EN

codegraph is a **pre-indexed code graph tool** for AI coding agents (Claude Code / Cursor / Codex CLI / OpenCode). Instead of the agent doing `grep`/`find`/`Read` every time it explores a codebase, codegraph indexes the entire code into a SQLite database (FTS5) and lets the agent query instantly.

Benchmark results across 6 real-world codebases: **94% fewer tool calls**, **77% faster**, **100% local** (no data leaves your machine).

---

## 2. Khi nào nên dùng codegraph? / When should you use codegraph?

### VN — Use case rõ ràng

✅ **Project TypeScript/JavaScript lớn** mà Claude Code/Cursor exploration tốn nhiều token
✅ **Polyglot codebase** với nhiều language (19+ language được hỗ trợ)
✅ **Khám phá impact** khi thay đổi 1 hàm — codegraph có `impact` tool
✅ **Call graph queries** — tìm callers/callees nhanh chóng
✅ **Local-first** — không muốn upload code lên cloud service (Sourcegraph etc.)

### VN — Không nên dùng nếu:

❌ Codebase nhỏ (< 1000 file) — Claude Code's native Read/Grep đủ nhanh
❌ Single-file scripts — overhead của index không đáng
❌ Language KHÔNG được tree-sitter hỗ trợ (Erlang, Haskell, Lua, etc.)

### EN — Clear use cases

✅ **Large TypeScript/JavaScript projects** where Claude Code/Cursor exploration burns tokens
✅ **Polyglot codebases** with multiple languages (19+ supported)
✅ **Impact analysis** when changing a function — codegraph has `impact` tool
✅ **Call graph queries** — find callers/callees instantly
✅ **Local-first** — don't want to upload code to cloud services (Sourcegraph etc.)

### EN — Skip if:

❌ Small codebase (<1000 files) — Claude Code's native Read/Grep is fast enough
❌ Single-file scripts — index overhead not worth it
❌ Language NOT supported by tree-sitter (Erlang, Haskell, Lua, etc.)

---

## 3. Cài đặt và Hello World / Installation and Hello World

### VN

**Step 1 — Cài codegraph + auto-config agent của bạn:**

```bash
npx @colbymchenry/codegraph
```

Installer sẽ interactive hỏi bạn agent nào đang dùng (Claude Code / Cursor / Codex / OpenCode). Chọn rồi installer tự ghi config phù hợp.

**Step 2 — Initialize project:**

```bash
cd your-project
codegraph init -i
```

Lệnh này sẽ tạo SQLite index cho project. Lần đầu mất 30s-2min tùy size codebase.

**Step 3 — Sau đó dùng Claude Code/Cursor như bình thường.** codegraph tự động chạy như MCP server backend; agent gọi `codegraph_search`/`codegraph_context`/etc. khi cần.

### EN

**Step 1 — Install codegraph + auto-config your agent:**

```bash
npx @colbymchenry/codegraph
```

The installer is interactive — it asks which agent(s) you use (Claude Code / Cursor / Codex / OpenCode). Choose, and the installer auto-writes the appropriate config.

**Step 2 — Initialize the project:**

```bash
cd your-project
codegraph init -i
```

This creates the SQLite index for the project. First time takes 30s-2min depending on codebase size.

**Step 3 — Use Claude Code/Cursor as usual.** codegraph runs as MCP server backend; the agent calls `codegraph_search`/`codegraph_context`/etc. when it needs to.

---

## 4. 8 MCP tools cốt lõi / 8 core MCP tools

| Tool | Mục đích / Purpose |
|------|--------------------|
| `codegraph_search` | Tìm symbols (function/class/variable) theo tên / Find symbols by name |
| `codegraph_context` | Build context cho 1 task cụ thể / Build relevant context for a task |
| `codegraph_callers` | Tìm gì call function này / Find what calls a function |
| `codegraph_callees` | Tìm function này call gì / Find what a function calls |
| `codegraph_impact` | Analyze impact khi đổi 1 symbol / Analyze code affected by changing a symbol |
| `codegraph_node` | Lấy chi tiết 1 symbol + source / Get details of a specific symbol with source |
| `codegraph_files` | Lấy structure của file đã index / Get indexed file structure |
| `codegraph_status` | Check health của index / Check index health |

---

## 5. 19+ language được hỗ trợ / 19+ supported languages

| Language | Extension(s) |
|----------|-------------|
| TypeScript | `.ts`, `.tsx` |
| JavaScript | `.js`, `.jsx`, `.mjs` |
| Python | `.py` |
| Go | `.go` |
| Rust | `.rs` |
| Java | `.java` |
| C# | `.cs` |
| PHP | `.php` |
| Ruby | `.rb` |
| C | `.c`, `.h` |
| C++ | `.cpp`, `.hpp`, `.cc` |
| Swift | `.swift` |
| Kotlin | `.kt`, `.kts` |
| Scala | `.scala`, `.sc` |
| Dart | `.dart` |
| Svelte | `.svelte` |
| Vue | `.vue` |
| Liquid | `.liquid` |
| Pascal/Delphi | `.pas`, `.dpr`, etc. |

---

## 6. 13 framework có route detection / 13 frameworks with route detection

codegraph nhận biết và liên kết URL routes với handler functions cho 13 framework:

- **Backend:** Django / Flask / FastAPI / Express / Laravel / Rails / Spring / Gin (chi/gorilla/mux) / Axum (actix/Rocket) / ASP.NET / Vapor
- **Frontend:** React Router / SvelteKit

Khi bạn hỏi *"What handles `/api/users` route?"* trong Claude Code, codegraph trả về handler function trực tiếp.

---

## 7. Comparison với native Claude Code tools / Comparison with native Claude Code tools

### VN

| Task | Native Claude Code | Với codegraph |
|------|---------------------|---------------|
| Tìm 1 function | `grep -r "function foo"` (chậm + nhiều output) | `codegraph_search "foo"` (instant) |
| Tìm callers | `grep -r "foo("` (false positives + slow) | `codegraph_callers "foo"` (precise) |
| Impact analysis | Manual reasoning (high token cost) | `codegraph_impact "foo"` (mechanical) |
| File structure | `find . -name "*.ts"` + `Read` mỗi file | `codegraph_files` (pre-indexed) |

### EN

| Task | Native Claude Code | With codegraph |
|------|---------------------|----------------|
| Find a function | `grep -r "function foo"` (slow + noisy) | `codegraph_search "foo"` (instant) |
| Find callers | `grep -r "foo("` (false positives + slow) | `codegraph_callers "foo"` (precise) |
| Impact analysis | Manual reasoning (high token cost) | `codegraph_impact "foo"` (mechanical) |
| File structure | `find . -name "*.ts"` + `Read` each file | `codegraph_files` (pre-indexed) |

---

## 8. Pre-indexed vs runtime — tại sao khác biệt / Pre-indexed vs runtime — why it matters

### VN

**Default Claude Code exploration:**
- Spawn Explore agents
- Mỗi agent grep + Read + glob
- Tiêu tốn token mỗi tool call
- Phải re-explore mỗi session

**Với codegraph:**
- Index 1 lần (auto-sync sau đó qua file watcher)
- Mỗi query → instant lookup vào SQLite
- Không có file Read sau khi index xong
- Persistent across sessions

Kết quả: VS Code codebase exploration giảm từ 52 calls / 97s → 3 calls / 17s. **94% ít hơn, 82% nhanh hơn.**

### EN

**Default Claude Code exploration:**
- Spawns Explore agents
- Each agent greps + Reads + globs
- Burns tokens on every tool call
- Must re-explore each session

**With codegraph:**
- Index once (auto-syncs via file watcher afterward)
- Each query → instant lookup against SQLite
- Zero file Read after indexing
- Persistent across sessions

Result: VS Code codebase exploration drops from 52 calls / 97s → 3 calls / 17s. **94% fewer, 82% faster.**

---

## 9. Lộ trình thử nghiệm 1 tuần / 1-week experimentation roadmap

### VN

**Day 1 — Hiểu và cài**
- Đọc README codegraph
- Run `npx @colbymchenry/codegraph` → install với target agent của bạn
- Trên 1 project TypeScript existing: `codegraph init -i`
- Verify: `codegraph status` show stats

**Day 2-3 — Sử dụng thực tế**
- Mở Claude Code trên project
- Hỏi 1 câu khám phá thông thường: *"What functions are responsible for X?"*
- Observe: Claude Code dùng `codegraph_search`/`codegraph_context` thay vì grep+Read
- Compare token usage trước/sau

**Day 4-5 — Impact + call graph**
- Thử: *"What would break if I rename function X?"* → `codegraph_impact`
- Thử: *"What calls function X?"* → `codegraph_callers`
- Đánh giá precision (false positive rate)

**Day 6 — Multi-agent (nếu có nhiều agent)**
- Cài codegraph cho thêm 1 agent khác (Cursor / Codex / OpenCode)
- Verify config được write đúng nơi
- So sánh experience giữa các agent

**Day 7 — Quyết định**
- codegraph có giảm token usage thực tế?
- Có precision đủ tốt?
- Có justification keep installed?

### EN

**Day 1 — Understand and install**
- Read codegraph README
- Run `npx @colbymchenry/codegraph` → install with your target agent
- On an existing TypeScript project: `codegraph init -i`
- Verify: `codegraph status` shows stats

**Day 2-3 — Real usage**
- Open Claude Code on the project
- Ask a typical exploration question: *"What functions are responsible for X?"*
- Observe: Claude Code uses `codegraph_search`/`codegraph_context` instead of grep+Read
- Compare token usage before/after

**Day 4-5 — Impact + call graph**
- Try: *"What would break if I rename function X?"* → `codegraph_impact`
- Try: *"What calls function X?"* → `codegraph_callers`
- Evaluate precision (false positive rate)

**Day 6 — Multi-agent (if you use multiple)**
- Install codegraph for an additional agent (Cursor / Codex / OpenCode)
- Verify config written to correct location
- Compare experience between agents

**Day 7 — Decide**
- Does codegraph actually reduce token usage?
- Is precision good enough?
- Worth keeping installed?

---

## 10. Tại sao codegraph quan trọng / Why codegraph matters

### VN

codegraph đại diện cho **một shape T2 Service mới** trong corpus Storm Bear: **MCP server cho multi-platform agent augmentation** (cùng shape với v66 agentmemory).

Đây là **N=3 evidence cho Pattern #18 sub-mechanism B "one-binary-many-CLIENTS"** (agentmemory MCP + CloakBrowser CDP + codegraph MCP) — một observation mạnh về cách T2 Service service đang evolve.

Khía cạnh quan trọng:
1. **Pre-indexed context** thay vì runtime exploration — kỹ thuật mới, lợi ích lớn (94% token savings)
2. **100% local** — không gửi data ra ngoài (privacy-first)
3. **Multi-agent từ ngày 1** — không phải Claude-Code-only
4. **AST-deterministic** — không phụ thuộc LLM-summarization

### EN

codegraph represents a **new T2 Service shape** in the Storm Bear corpus: **MCP server for multi-platform agent augmentation** (same shape as v66 agentmemory).

It's **N=3 evidence for Pattern #18 sub-mechanism B "one-binary-many-CLIENTS"** (agentmemory MCP + CloakBrowser CDP + codegraph MCP) — strong observation about how T2 Service tools are evolving.

Key aspects:
1. **Pre-indexed context** instead of runtime exploration — novel approach, large benefit (94% token savings)
2. **100% local** — no data leaves your machine (privacy-first)
3. **Multi-agent from day 1** — not Claude-Code-only
4. **AST-deterministic** — not dependent on LLM-summarization

---

## 11. Đọc thêm / Further reading

### VN

- **README:** [github.com/colbymchenry/codegraph#readme](https://github.com/colbymchenry/codegraph#readme) — đầy đủ API + benchmark + roadmap
- **CHANGELOG:** [github.com/colbymchenry/codegraph/blob/main/CHANGELOG.md](https://github.com/colbymchenry/codegraph/blob/main/CHANGELOG.md)
- **CLAUDE.md (subject):** [github.com/colbymchenry/codegraph/blob/main/CLAUDE.md](https://github.com/colbymchenry/codegraph/blob/main/CLAUDE.md) — architecture rules cho contributors
- **npm:** [npmjs.com/package/@colbymchenry/codegraph](https://www.npmjs.com/package/@colbymchenry/codegraph)
- **Author:** [colbymchenry.com](https://colbymchenry.com)

**Corpus siblings (trong vault này):**
- v66 agentmemory — same T2 Service MCP shape (memory layer thay vì code-graph)
- v62 codex-plugin-cc — cross-vendor plugin cho Claude Code (codegraph supports Codex CLI)
- v67 opencode-antigravity-auth — Opencode ecosystem subject (codegraph supports OpenCode)
- v69 CloakBrowser — Pattern #18 sub-mechanism B CDP variant sibling

### EN

- **README:** [github.com/colbymchenry/codegraph#readme](https://github.com/colbymchenry/codegraph#readme) — full API + benchmarks + roadmap
- **CHANGELOG:** [github.com/colbymchenry/codegraph/blob/main/CHANGELOG.md](https://github.com/colbymchenry/codegraph/blob/main/CHANGELOG.md)
- **CLAUDE.md (subject):** [github.com/colbymchenry/codegraph/blob/main/CLAUDE.md](https://github.com/colbymchenry/codegraph/blob/main/CLAUDE.md) — architecture rules for contributors
- **npm:** [npmjs.com/package/@colbymchenry/codegraph](https://www.npmjs.com/package/@colbymchenry/codegraph)
- **Author:** [colbymchenry.com](https://colbymchenry.com)

**Corpus siblings (in this vault):**
- v66 agentmemory — same T2 Service MCP shape (memory layer instead of code-graph)
- v62 codex-plugin-cc — cross-vendor plugin for Claude Code (codegraph supports Codex CLI)
- v67 opencode-antigravity-auth — Opencode ecosystem subject (codegraph supports OpenCode)
- v69 CloakBrowser — Pattern #18 sub-mechanism B CDP variant sibling

---

**Closing note / Lời kết:**

VN: codegraph là **pilot candidate mạnh** cho Storm Bear vault — augment Claude Code trên TypeScript codebase (hireui-harness primary). Setup đơn giản, reversible (`codegraph uninit`), value-add ngay tức thì. Khuyến nghị fenced pilot 1 tuần.

EN: codegraph is a **strong pilot candidate** for the Storm Bear vault — augments Claude Code on TypeScript codebases (hireui-harness primary). Simple setup, reversible (`codegraph uninit`), immediate value-add. Recommended as 1-week fenced pilot.

— v70 wiki · 2026-05-19 · colbymchenry/codegraph
