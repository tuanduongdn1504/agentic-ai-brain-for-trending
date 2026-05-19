# DeepSeek-TUI — Hướng dẫn cho người mới (VN/EN)

> *Trợ lý lập trình chạy trong terminal cho DeepSeek V4 — đọc/sửa file, chạy shell, quản lý git, duyệt web, điều phối sub-agent song song.*
>
> *Terminal coding agent for DeepSeek V4 — reads/edits files, runs shell, manages git, browses web, coordinates concurrent sub-agents.*

**Phiên bản wiki:** v72 (built 2026-05-19)
**Repository:** https://github.com/Hmbown/deepseek-tui.com
**Tác giả gốc:** Hmbown (solo developer)
**License:** MIT
**Stars / forks:** 32,114 / 2,729

---

## Phần 1: DeepSeek-TUI là gì?

**Tóm tắt (VN):** DeepSeek-TUI là một AI coding agent chạy trực tiếp trong terminal của bạn. Nó dùng model DeepSeek V4 (`deepseek-v4-pro` / `deepseek-v4-flash`) làm mặc định nhưng cũng hỗ trợ thêm 8 nhà cung cấp khác (NVIDIA NIM / AtlasCloud / OpenRouter / Novita / Fireworks / generic OpenAI-compatible / SGLang / vLLM / Ollama). Khi bạn gõ `deepseek` trong shell, một giao diện TUI mở ra cho phép bạn yêu cầu nó đọc file, sửa code, chạy lệnh, search web, hoặc điều phối nhiều sub-agent chạy song song.

**Summary (EN):** DeepSeek-TUI is an AI coding agent that runs in your terminal. Default model: DeepSeek V4 (`deepseek-v4-pro` / `deepseek-v4-flash`). Also supports 8 other providers (NVIDIA NIM / AtlasCloud / OpenRouter / Novita / Fireworks / generic OpenAI-compatible / SGLang / vLLM / Ollama). Typing `deepseek` in your shell opens a TUI where you ask it to read files, edit code, run commands, search web, or coordinate concurrent sub-agents.

**Điểm nổi bật chính:**
- 1 triệu token context window (DeepSeek V4 lợi thế lớn hơn nhiều alternative)
- 3 chế độ hoạt động: Plan / Agent / YOLO (đọc-only / approval / auto-approve)
- Sandbox cấp OS (Seatbelt trên macOS / Landlock trên Linux / Job Objects trên Windows)
- Sub-agent pool — chạy nhiều child agent song song
- MCP (Model Context Protocol) — kết nối tools bên ngoài
- LSP integration — 5 language servers (Rust / Python / TS / Go / C++)
- Session save/resume — tiếp tục công việc đã dở
- Workspace rollback — side-git snapshots không động vào repo `.git` của bạn
- 4 ngôn ngữ UI (EN / zh-Hans / ja / pt-BR)
- 11 starter skills built-in

---

## Phần 2: Tín hiệu corpus-first (v72 wiki context)

**Trong corpus 72-wiki của Storm Bear, DeepSeek-TUI đặt ra một số kỷ lục:**

1. **9 nhà cung cấp** — vượt qua v71 agents-best-practices dual-vendor synthesis (chỉ Anthropic + OpenAI)
2. **5 phương thức cài đặt** — npm + cargo + Homebrew + Docker + direct download (kỷ lục corpus)
3. **4 locale UI** — EN + zh-Hans + ja + pt-BR (vượt qua CJK trio)
4. **3 nền tảng OS sandbox** — Seatbelt + Landlock + Job Objects (kỷ lục corpus)
5. **5 LSP language servers** — kỷ lục corpus về breadth ngôn ngữ
6. **3 protocol OSC notification** — OSC 9 + OSC 99 + OSC 777 (kỷ lục)
7. **2-binary architecture** (`deepseek` + `deepseek-tui` tách riêng) — đề xuất Pattern #18 sub-mechanism C mới

**Velocity sustained:** 267.6 stars/day × 120 days = **HIGH-NOT-EXTREME sub-class N=2** (mới promoted criteria tại v72 audit; v72 wiki là evidence N=2 cho sub-class — FIRST POST-v72-AUDIT POLICY SATISFACTION trong lịch sử corpus, 0-wiki gap giữa audit set policy và wiki satisfy policy).

---

## Phần 3: Định vị tier (Pattern Library)

**Tier T1** — Coding Agent / Framework. Khác với:
- T2 Service (như v66 agentmemory hoặc v70 codegraph): T2 là single-purpose service; DeepSeek-TUI là full coding agent.
- T4 Bridge (như v62 codex-plugin-cc): T4 kết nối hai sản phẩm cụ thể; DeepSeek-TUI là sản phẩm đứng riêng.
- T1 Assistant Skill (như v71 agents-best-practices): v71 là khai báo (declarative skill); DeepSeek-TUI là execution-runtime hoàn chỉnh.

**Phase 4b PRIMARY route:** Pattern #52 HIGH-NOT-EXTREME sub-class N=2 strengthening — v75 audit sẽ promote Pattern #52 thành CONFIRMED thông qua sub-variant evidence này.

---

## Phần 4: Cài đặt

**Cách dễ nhất (npm):**

```bash
npm install -g deepseek-tui
deepseek --version       # xác nhận cài đặt
deepseek --model auto    # khởi động TUI; auto-mode chọn model + thinking level mỗi turn
```

**Cách khác (chọn theo môi trường của bạn):**

```bash
# Rust toolchain (Cargo) — không cần Node
cargo install deepseek-tui-cli --locked   # cần Rust 1.88+ vì code dùng 2024 edition
cargo install deepseek-tui     --locked

# macOS (Homebrew)
brew tap Hmbown/deepseek-tui
brew install deepseek-tui

# Docker container
docker run --rm -it \
  -e DEEPSEEK_API_KEY="$DEEPSEEK_API_KEY" \
  -v "$PWD:/workspace" \
  ghcr.io/hmbown/deepseek-tui:latest

# Direct download (air-gapped)
# https://github.com/Hmbown/deepseek-tui.com/releases — nhớ verify SHA-256
```

**Ở Việt Nam / Trung Quốc:** Dùng npm mirror để tăng tốc:

```bash
npm install -g deepseek-tui --registry=https://registry.npmmirror.com
```

Hoặc dùng Cargo mirror (TUNA của Tsinghua) — xem `docs/INSTALL.md`.

**Sau khi cài:** Lần đầu chạy `deepseek` sẽ hỏi DeepSeek API key. Lấy từ https://platform.deepseek.com/api_keys. Key được lưu vào `~/.deepseek/config.toml`.

```bash
deepseek auth status      # xem credential source hiện tại
deepseek auth set --provider deepseek --api-key "$KEY"
deepseek doctor           # kiểm tra setup
```

---

## Phần 5: Quy trình sử dụng cốt lõi

### Vòng đời một session

```bash
cd ~/my-project        # vào thư mục project
deepseek               # khởi động TUI; tự động hỏi DeepSeek API key nếu chưa cấu hình
```

Trong TUI:
1. Nhập yêu cầu vào composer
2. Mặc định ở **Agent mode**: model làm việc, chạy tools, hỏi approval khi cần
3. Đọc/sửa file / chạy shell / git commits / search web tự động
4. `/compact` khi context quá 60% (tránh session degrade — xem AGENTS.md)
5. `/skills` — quản lý 11 starter skills + thêm skills từ GitHub
6. Khi xong: `Ctrl+D` để thoát; session checkpoint tự động

**Tiếp tục session đã lưu:**

```bash
deepseek -c                              # tiếp tục session gần nhất trong workspace này
deepseek -r latest                       # tương đương
deepseek -r <SESSION_ID_OR_PREFIX>       # resume session cụ thể
```

### Chuyển chế độ (Plan / Agent / YOLO)

Trong TUI:
- `Tab` — cycle Plan → Agent → YOLO → Plan
- `/mode plan` — chuyển sang Plan (read-only investigation, không sửa file)
- `/mode agent` — chế độ mặc định (multi-step tool use with approval)
- `/mode yolo` — auto-approve tất cả tools + trust mode (CHỈ DÙNG trong repo bạn tin)

**Khi nào dùng chế độ nào:**
- **Plan:** Lúc bạn muốn agent điều tra trước, đưa ra plan để bạn review
- **Agent:** Workflow tiêu chuẩn — approval gates cho shell, paid tools
- **YOLO:** Khi bạn cần automation nhanh trong repo trusted

### Chuyển model + thinking level

```bash
Shift+Tab        # cycle reasoning off → high → max
/model           # mở model picker
/provider        # chuyển provider
```

**Auto mode (`deepseek --model auto`):** Trước mỗi turn, một call nhỏ `deepseek-v4-flash` (router) chọn concrete model + thinking level. Câu hỏi đơn giản → Flash + off; coding/debugging/architecture → Pro + high/max.

---

## Phần 6: Các khái niệm mới / kiến trúc quan trọng

### Sub-agents — chạy nhiều child agent song song

DeepSeek-TUI có thể dispatch nhiều sub-agent chạy song song như một task queue concurrent:

```text
> agent_open prompt="audit issue #427"        # non-blocking — parent vẫn làm việc
> agent_open prompt="search docs cho 'thinking-mode'"
# Khi xong: event <deepseek:subagent.done> với summary + evidence + metrics
> agent_eval handle=<child> prompt="..."      # chỉ gọi khi summary chưa đủ
> agent_close handle=<child>
```

**Default pool: 10 concurrent sub-agents; configurable to 20 (`--max-subagents 20`).**

**Tại sao dùng sub-agents:** AGENTS.md cảnh báo "Long sessions in DeepSeek TUI WILL degrade and crash if you work sequentially." Delegate independent work early để giữ parent transcript gọn.

### RLM (REPL Language Mode) — batch analysis nguyên thuỷ corpus-first

Khi cần phân loại 15 files / inspect một paper / mine một long log:

```text
> rlm_open
> rlm_eval """
files = list(content['workspace'].glob('**/*.rs'))
results = sub_query_batch([f.read_text() for f in files], prompt='classify by purpose')
finalize(results)
"""
> handle_read result_handle slice="0:10"
> rlm_close
```

Persistent Python REPL với helpers: `peek` / `search` / `chunk` / `sub_query_batch` (fan-out 1-16 cheap `deepseek-v4-flash` calls song song). Tránh dump repeated reads vào parent transcript.

### Multi-provider — Pattern #84 84c "Provider-Agnostic-By-Design" tại corpus-record scale

DeepSeek mặc định, nhưng:

```bash
# Chuyển sang OpenRouter để dùng model khác
deepseek auth set --provider openrouter --api-key "$OR_KEY"
deepseek --provider openrouter --model deepseek/deepseek-v4-pro

# Self-hosted Ollama cho privacy/offline
ollama pull deepseek-coder:1.3b
deepseek --provider ollama --model deepseek-coder:1.3b

# Generic OpenAI-compatible endpoint
OPENAI_BASE_URL="https://openai-compatible.example/v4" \
  deepseek --provider openai --model glm-5
```

Pattern Library tags: Pattern #84 84c (FIRST POST-PROMOTION strengthening — v72 audit promoted Pattern #84 với 84c sub-mechanism; v72 wiki provides N=2 trong 0 wikis).

### OS-level sandbox (corpus-first 3-platform)

Mặc định, shell commands chỉ access workspace directory:

| Platform | Sandbox |
|----------|---------|
| macOS | Seatbelt |
| Linux | Landlock |
| Windows | Job Objects |

Muốn access ngoài workspace? `/trust` để enable trust mode. YOLO mode auto-enable trust mode.

### LSP integration — diagnostics vào model context

Sau MỖI edit, 5 language servers chạy: rust-analyzer / pyright / typescript-language-server / gopls / clangd. Diagnostics được inject vào context **TRƯỚC** reasoning step tiếp theo. Agent "thấy" lỗi compile/lint trước khi quyết định bước tiếp.

### Workspace rollback — side-git không động `.git` của bạn

DeepSeek-TUI tạo side-git snapshots pre/post-turn, SEPARATELY từ `.git` của repo bạn:

```text
> revert_turn              # undo filesystem changes của turn vừa rồi
> /restore                 # restore từ snapshot cũ hơn
```

Side-git lives in `.deepseek/side-git/` (within workspace) — không động vào history git của bạn.

---

## Phần 7: So sánh với các framework corpus khác

| Đặc điểm | DeepSeek-TUI (v72) | Claude Code (substrate) | v71 agents-best-practices | v66 agentmemory |
|----------|---------------------|--------------------------|---------------------------|-----------------|
| Tier | T1 Coding Agent | T1 (substrate) | T1 Assistant Skill | T2 Service |
| Default model | DeepSeek V4 | Claude Sonnet/Opus/Haiku | Provider-agnostic skill | n/a (service) |
| Provider matrix | **9 (corpus-record)** | 1 (Anthropic) | Declarative (any) | 1+ |
| Packaging methods | **5 (corpus-record)** | 1 (npm) | 2 (npm+git) | 3 |
| Locales | **4 (corpus-record)** | 1 (EN) | 1 (EN) | 1 (EN) |
| OS sandbox | 3-platform (corpus-record) | App-level | N/A | None |
| Sub-agents | Concurrent pool (10/20) | Sequential | L0-L4 autonomy levels | N/A |
| MCP role | Client | Both | N/A (declarative) | Server |
| Velocity sustained | 267/d × 120d (HIGH-NOT-EXTREME) | n/a (substrate) | 205/d × 4d (too young) | n/a (service) |

---

## Phần 8: Ethical framing — Honest deficiency disclosure (Pattern #83)

DeepSeek-TUI có disclosure-discipline mạnh; AGENTS.md công khai các pitfalls + limitations. Đây là evidence Pattern #83 83b methodology-disclosure + 83d experimental-status-disclosure.

**Các disclosures quan trọng (verbatim from AGENTS.md):**

1. **Cost tracking inaccurate:** *"Token counting and cost estimation may be inflated due to thinking token accounting bugs. Use `/compact` to manage context, and treat cost estimates as approximate."*

2. **Session degradation:** *"Long sessions in DeepSeek TUI WILL degrade and crash if you work sequentially. The session accumulates every message and tool result in `api_messages` and `history` with **no automatic pruning**."*

3. **API constraint:** *"In V4 thinking mode, assistant messages that contain tool calls must replay their `reasoning_content` in all subsequent requests or the API returns HTTP 400."*

4. **Stable Rust only:** *"This crate must compile on stable Rust. **Never** introduce code that requires `#![feature(...)]`, `cargo +nightly`, or any unstable language / library feature."*

5. **Install path caveats:** *"Scoop's manifest updates independently and can lag the GitHub/npm/Cargo release. Run `scoop update` first."* + *"Cargo path requires Rust 1.88+ (the crates use the 2024 edition; older toolchains fail with 'feature `edition2024` is required')."*

6. **ARM64 boundary:** *"`npm i -g deepseek-tui` works on glibc-based ARM64 Linux from v0.8.8 onward."*

---

## Phần 9: Storm Bear relevance — Vault pilot candidate

**Verdict: MODERATE INCLUDE (2/4 PASS Storm Bear meta-entity criteria).**

| Criterion | Status |
|-----------|--------|
| (a) Author archetype peer | FAIL (English handle, no VN/Asian-diaspora evidence) |
| (b) Operational tool for vault | **PASS** (vendor-diversification pilot for documented Claude-Code lock-in risk) |
| (c) Methodology influence | **PASS** (AGENTS.md 6-rule session-longevity + summary-first tools inform routine v2.3) |
| (d) In-corpus reference | FAIL (no explicit citation of corpus subjects) |

**Pilot ranking:** MODERATE-RELEVANCE — fourth in pilot sequence (post codegraph + agents-best-practices skill + agentmemory).

**Recommended pilot scope (vài tuần):**
- Install via Homebrew (`brew tap Hmbown/deepseek-tui && brew install deepseek-tui`)
- Use trong Plan mode + Agent mode cho task scripting / wiki-build phụ
- Direct so sánh vs Claude Code on same task
- Track: token cost / response quality / 1M context utilization / sub-agent coordination efficacy

**Lý do MODERATE thay vì HIGH:**
- DeepSeek-TUI là full coding agent (not declarative skill như v71) — risk profile cao hơn agents-best-practices skill install
- Reversible nhưng requires uninstall + delete `~/.deepseek/` directory
- Đối với Storm Bear's wiki-building workflow chính, Claude Code đã được established — DeepSeek-TUI là alternative-not-replacement

---

## Phần 10: 4-week learning roadmap

**Week 1 — Cài đặt + first session:**
- Cài qua npm hoặc Homebrew
- Tạo DeepSeek API key
- Chạy `deepseek doctor` để verify
- Thử `deepseek -p "Hello, what can you do?"`
- Đọc README + docs/MODES.md
- Try 3 modes (Plan / Agent / YOLO) on scratch project

**Week 2 — Tools + sub-agents:**
- File operations (read / write / apply-patch)
- Shell với approval gates
- Git management (commit / branch / log)
- Web search + browse
- Try sub-agents (`agent_open` for parallel reconnaissance)

**Week 3 — Advanced features:**
- RLM batch analysis (`rlm_open` + `sub_query_batch`)
- MCP integration (connect MCP server)
- Session save/resume + workspace rollback
- Auto mode + reasoning effort tiers
- Switch providers (e.g., Ollama for offline)

**Week 4 — Production discipline:**
- Đọc AGENTS.md 6-rule session-longevity discipline
- Practice `/compact` at 60% context
- Test workspace rollback + `revert_turn`
- Set up Tencent Cloud / CNB remote-first (nếu ở VN/CN)
- Compare cost + quality vs Claude Code on same task

---

## Phần 11: Tradeoffs + limitations

**Lợi thế:**
- 1M token context — lợi thế lớn vs Claude (200K) hoặc GPT-4 (128K)
- DeepSeek API rẻ hơn nhiều so với Claude / GPT-4
- 9-provider matrix — không lock-in vendor
- OS-level sandbox — security tốt hơn app-level
- Sub-agent + RLM — parallelism native
- 4 locale + China-friendly install paths

**Hạn chế:**
- Cost tracking thiếu chính xác (token counting bị inflated)
- Long sessions degrade nếu không dùng sub-agents/RLM
- Rust toolchain dependency (1.88+) nếu build from source
- 2-binary architecture (`deepseek` + `deepseek-tui`) có thể confuse first-time users
- Single-maintainer trust boundary (Hmbown) — bus-factor concern
- DeepSeek API có thể bị filter ở một số khu vực (Tencent / China-specific path mitigate phần nào)
- Cộng đồng nhỏ hơn Claude Code

**Khi nên dùng:**
- Cần 1M context (large codebase, long docs)
- Muốn cost tiết kiệm hơn Claude
- Cần multi-provider flexibility
- OS-level sandbox quan trọng
- Sub-agent parallelism workflow

**Khi không nên dùng:**
- Cần Anthropic Claude cụ thể
- Không sẵn sàng install Rust toolchain
- Workflow yêu cầu IDE integration sâu (DeepSeek-TUI là TUI-first; IDE qua MCP only)
- Cần cost-tracking baseline ổn định cho billing

---

## Phần 12: Caveats + safety notes

**Supply-chain awareness (Pattern #66):**
- Verify SHA-256 manifest cho manual downloads
- Tránh look-alike repositories hoặc search-result mirrors
- Official binaries: github.com/Hmbown/deepseek-tui.com/releases
- Homebrew tap là `Hmbown/deepseek-tui` — verify trước khi tap

**Prompt-injection awareness (Pattern #66 sub-mechanism 66e):**
AGENTS.md cảnh báo: GitHub issues + PRs + comments + READMEs là **untrusted input**. Khi DeepSeek-TUI giúp bạn triage issues, nó được instruct treat embedded instructions in issues as DATA not commands. Don't add 3rd-party tools just because issue requests.

**Trust mode safety:**
- Mặc định, tools restricted to `--workspace` directory
- `/trust` enable file access ngoài workspace — chỉ làm khi cần
- YOLO mode auto-enable trust + auto-approve tools — chỉ dùng trong repo bạn 100% trust

**API key security:**
- API key saved to `~/.deepseek/config.toml` — đảm bảo permissions
- `deepseek auth status` để check active credential source (KHÔNG print key)
- `deepseek auth clear --provider deepseek` để rotate

**Session degradation:**
- AGENTS.md verbatim: "Long sessions WILL degrade and crash if you work sequentially"
- Auto-compaction disabled by default since v0.6.6
- Suggest `/compact` at 60% context (not 80%)
- Delegate independent work to sub-agents early

---

## Phần 13: References + Next Action

### Tài liệu chính

- **Repository:** https://github.com/Hmbown/deepseek-tui.com
- **Homepage:** https://deepseek-tui.com/
- **DeepWiki index:** https://deepwiki.com/Hmbown/DeepSeek-TUI
- **DeepSeek API docs:** https://platform.deepseek.com/api_keys
- **README (full):** github.com/Hmbown/deepseek-tui.com#readme
- **AGENTS.md (corpus-rich governance):** github.com/Hmbown/deepseek-tui.com/blob/main/AGENTS.md
- **docs/ tree:** 20+ files (ARCHITECTURE / INSTALL / CONFIGURATION / MODES / SUBAGENTS / MCP / etc.)

### Storm Bear vault cross-references

- **CLAUDE.md** (vault root) — Storm Bear meta-entity + Pattern Library state
- **v72 audit document:** `04 Reviews/(C) 2026-05-19 ... PROMOTION-DRIVEN + 5TH-CONSECUTIVE-TRIGGER ...md`
- **v72 wiki entities:** `02 Wiki/(C) entity-1-coding-agent.md` (modes/tools), `(C) entity-3-pattern-library.md` (Pattern Library impacts)
- **Phase 4b PRIMARY:** `01 Analysis/(C) Pattern-52-HIGH-NOT-EXTREME-velocity-N2-sub-class-strengthening-evaluation.md`
- **Sister wikis:** v71 agents-best-practices + v70 codegraph + v69 CloakBrowser + v66 agentmemory + v65 claude-code-system-prompts

### Sibling tools trong vault corpus

- **v71 agents-best-practices** — Provider-agnostic agent skill framework (sibling Pattern #84 84c evidence)
- **v70 codegraph** — Pre-indexed code knowledge graph (sibling Pattern #18 sub-mechanism evidence)
- **v66 agentmemory** — Agent memory system (Pattern #18 B1 MCP sibling)
- **Claude Code** (Storm Bear's primary substrate) — Anthropic equivalent; DeepSeek-TUI is vendor-diversification alternative

### Next action

**For Storm Bear (vault operator):**

1. **Decision: Pilot DeepSeek-TUI?** Pilot ranking position #4 trong queue (sau codegraph + agents-best-practices skill + agentmemory). Schedule pilot decision tại v75 audit window.

2. **Methodology absorption:** Đọc AGENTS.md "Session Longevity (Critical)" section + summary-first tool principle. Codify cho routine v2.3 design.

3. **Pattern Library check:** Verify v72 wiki contributions at next vault sync:
   - Pattern #52 HIGH-NOT-EXTREME sub-class N=2 evidence ✓
   - Pattern #84 84c FIRST POST-PROMOTION strengthening ✓
   - Pattern #21 sub-variant candidate ✓
   - Pattern #66 sub-mechanism 66e candidate ✓
   - Pattern #18 sub-mechanism C candidate ✓
   - OC-P NEW candidate ✓

4. **v75 audit prep:** Pattern #52 PROMOTION-ELIGIBLE — schedule promotion at v75 audit; OC-P + 18C + 66e + 21 sub-variant first-cycle stale-checks.

**For end-user (not Storm Bear):**

1. Cài DeepSeek-TUI qua npm hoặc Homebrew
2. Đăng ký DeepSeek API key
3. Try `deepseek doctor` để verify setup
4. Try 3 modes trên scratch project
5. Đọc docs/MODES.md + docs/SUBAGENTS.md
6. Sau 1 tuần: practice `/compact` discipline + sub-agent delegation

---

**Wiki end. Build by Storm Bear vault v72 LLM Wiki Routine v2.2 — 2026-05-19.**

**Independent value-add of this guide:** Side-by-side comparison vs Claude Code + corpus context (v71 / v70 / v66) + Pattern Library impact summary specific to Storm Bear's audit-policy-satisfaction discipline.
