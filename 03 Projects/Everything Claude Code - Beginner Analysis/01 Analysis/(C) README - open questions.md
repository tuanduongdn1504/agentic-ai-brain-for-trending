# (C) README — Open Questions & Observations

> Working notes từ lần ingest README.md ngày 2026-04-17.
> Working notes from README.md ingest on 2026-04-17.

## Câu hỏi / Open Questions

> Đã update sau khi ingest [[../02 Wiki/(C) Shortform Guide summary]] ngày 2026-04-17.

1. ✅ **Skills vs Commands** — **TRẢ LỜI:** Skills là "durable unit" — bundle reusable với structure, supporting files, codemaps. Commands chỉ là slash-entry shim cho legacy compatibility, đang bị migrate sang skills. Người mới nên học **skills trước**, dùng commands chỉ vì gõ tắt nhanh. *(Source: shortform guide line 13–34)*
2. ✅ **Mâu thuẫn số lượng** — **TRẢ LỜI ĐỦ:** Đếm trực tiếp filesystem 2026-04-17:
    - `ls agents/ | wc -l` = **48** ✅ match Quick Start (48), ❌ NOT match changelog v1.10.0 (38)
    - `ls -d skills/*/ | wc -l` = **185** ≈ match Quick Start (183), ❌ NOT match changelog (156)
    - `ls commands/ | wc -l` = **79** ✅ match Quick Start (79), ❌ NOT match changelog (72)
    - **Verdict:** **Quick Start chính xác toàn bộ. Changelog v1.10.0 outdated trên cả 3 số.**
    - **Bonus discovery:** `plugin.json agents array` chỉ có 38 files (match changelog), trong khi filesystem có 48 → **10 agents mới chưa được add vào manifest**. Contribution opportunity #4. *(Source: filesystem + plugin.json 2026-04-17)*
3. ⏸ **Plugin vs manual install** — chưa giải trực tiếp. Shortform guide không bàn install path; TROUBLESHOOTING.md (chưa đọc) có thể có.
4. ⏸ **`rules/` không tự cài** — chưa giải. Vẫn cần check `install.sh`.
5. ⏸ **multi-* commands cần `ccg-workflow` riêng** — chưa giải.
6. ⏸ **ECC 2.0 alpha** — chưa giải.
7. ✅ **Continuous Learning v1 vs v2** — **TRẢ LỜI ĐỦ:** v1 = Stop-hook (1×/session, probabilistic ~50–80% fire); v2 = PreTool+PostTool hooks (100% deterministic) + atomic **instincts** (one trigger / one action / confidence 0.3–0.9 weighted) + background Haiku observer agent + evolution pipeline (instincts → cluster → skill/command/agent). **v2.1** thêm project-scoped instincts (12-char hash từ git remote URL) + auto-promotion (cùng instinct ID ≥ 2 project + avg confidence ≥ 0.8 → promote thành global). 6 commands user-facing: `/instinct-status`, `/evolve`, `/instinct-export`, `/instinct-import`, `/promote`, `/projects`. *(Source: skills/continuous-learning-v2/SKILL.md, full file 12.3KB. Detailed case study trong [[../02 Wiki/(C) Skills]])*
8. ✅ **Iterative Retrieval** — **TRẢ LỜI:** Đây là pattern giải "sub-agent context problem" (sub-agent chỉ biết literal query, không biết PURPOSE). 4-step loop: (1) orchestrator evaluate return → (2) hỏi follow-up trước khi accept → (3) sub-agent về source, lấy answer, return lại → (4) loop max 3 cycles. **Key:** pass **objective context** không chỉ query. Vd thay "search authentication" → "search authentication, context: refactor middleware, cần tất cả entry point". *(Source: longform lines 256–267)*

### Câu hỏi MỚI từ shortform guide:

9. **Hook profiles `minimal/standard/strict`** (đề cập trong README v1.8.0 changelog) — shortform không nhắc. ECC mặc định cài profile nào? Khác nhau cụ thể như thế nào?
10. **`ralph-wiggum` plugin** ("loop automation") — tên hài hước, không rõ làm gì cụ thể. Có liên quan đến `autonomous-loops` skill trong README không?
11. **`mgrep` vs `grep`/`rg`** — tác giả nói "significant improvement". Cải tiến cụ thể ra sao? Hybrid BM25/vector? *(Lưu ý: vault root CLAUDE.md cũng nhắc đến `qmd` — tool tương tự cho LLM Wiki pattern. Có thể đáng so sánh.)*
12. **`/fork` vs git worktrees** — guide phân biệt rõ "non-overlapping" vs "overlapping". Nhưng technical mechanism của `/fork` là gì? Nó tạo branch git hay chỉ branch conversation?
13. **`hookify` plugin** — tạo hook qua hội thoại. Có phải Claude Code official plugin không, hay 3rd-party? Có an toàn để dùng không?
14. **Editor recommendation = Zed** — tác giả thích Zed. Mình đang dùng Obsidian (cho wiki) + ??? cho code. Có cần switch không, hay VSCode/Cursor là fine?

### Câu hỏi MỚI từ longform guide:

15. ✅ **`continuous-learning` v2 "instinct-based với confidence scoring"** — **TRẢ LỜI ĐỦ:** xem Q7 ở trên. Confidence tăng khi pattern lặp + user không correct + instinct khác agree; giảm khi user correct + không observed lâu + contradiction. Promotion: project→global khi cùng ID xuất hiện ≥2 project + avg ≥0.8 (auto), hoặc user gọi `/promote <id>`. *(Source: skills/continuous-learning-v2/SKILL.md)*
16. **`mgrep` 50-task benchmark** — số liệu "~50% token reduction" reproduce được không? Benchmark public ở đâu? **→ check `mixedbread-ai/mgrep` repo hoặc longform guide image source.**
17. **Authority hierarchy** ("system prompt > user message > tool result") — tác giả tuyên bố như fact. Verify với Anthropic docs chính thức trước khi viết vào published guide.
18. **Plan mode "default option clears context"** — feature này có sẵn từ phiên bản Claude Code nào? Người mới có thể relyon được không?
19. **`llms.txt` standard** — proposal của ai? Adoption rate ra sao? **→ google "llms.txt spec".**
20. **`pass@k=70%` base rate trong example** — đây là số tác giả pick để minh hoạ, hay đo từ benchmark thật? Nếu thật, benchmark nào?
21. **Sequential phases với `/clear` giữa các agent** — khi `/clear`, làm sao agent N+1 inject FILE output từ agent N? Đường dẫn file là parameter, hay convention? **→ đọc agent files cụ thể (planner.md, etc.) để xem họ chuẩn hoá thế nào.**
22. **Memory persistence hooks ở `hooks/memory-persistence/`** — đây là hook ECC tự build hay built-in của Claude Code? Nếu ECC build thì độ tin cậy ra sao? **→ đọc folder đó.**

## Câu trả lời tự nhiên / Self-resolved

- Sequential phases dùng FILE để pass output (rule #5 của longform). `/clear` chỉ xoá conversation, không xoá file. → câu hỏi technical mechanism đã rõ. Cái CHƯA rõ là convention naming/path (Q21).

### Câu hỏi MỚI từ security guide:

23. **OWASP MCP Top 10 exact list** — guide nhắc 5 category (tool poisoning, prompt injection via contextual payloads, command injection, shadow MCP servers, secret exposure) — nhưng chỉ 5/10. Còn 5 category nữa là gì? **→ google "OWASP MCP Top 10 2026".**
24. **`permissions.deny` field trong `settings.json`** — built-in Claude Code feature hay ECC extension? Cần biết vì sẽ recommend trong published guide. **→ verify Claude Code official docs.**
25. **Dead-man switch reference implementation** — skill `autonomous-loops` có cover heartbeat + process-group kill không? **→ đọc skill đó.**
26. **"Agent 1 parse, Agent 2 act" separation** — giống sequential phases từ longform (RESEARCH → PLAN → IMPLEMENT), nhưng nhấn security angle. Đây là cùng pattern với variant khác không? **→ document cross-link sau khi viết (C) MCPs.**
27. **CVE-2026-25253 OpenClaw exposure** — 17,470 instances exposed. Storm Bear có dùng OpenClaw không? Nếu có thì rõ nguy cơ; nếu không thì skip. **→ confirm với user.**
28. **`npx ecc-agentshield scan` kết quả cho Storm Bear vault** — actionable, should run. **→ action item tương lai.**

## Quan sát / Observations

- **Repo rất lớn**: 30+ folders, 40+ files ở root, 67KB README. Người mới dễ overwhelm. **Beginner roadmap cực kỳ cần thiết** — đây chính là value prop của project Storm Bear.
- **Cross-harness positioning**: ECC không chỉ cho Claude Code. Hỗ trợ Cursor, Codex, OpenCode, Gemini, Antigravity. → có thể tận dụng để team không bị lock-in một harness.
- **Security là first-class**: AgentShield, security guide riêng 27.9KB, security skill, security-reviewer agent. Đáng note vì nhiều project AI khác bỏ qua phần này.
- **Bilingual gốc**: repo đã có README.zh-CN.md (35KB) và docs/ với pt-BR, zh-TW, ja-JP, ko-KR, tr. **Chưa có tiếng Việt** → có thể là contribution opportunity nếu wiki của mình thành công.
- **Có dashboard GUI** (`ecc_dashboard.py`, Tkinter) — bất ngờ. Dùng để explore agents/skills/commands trực quan. Đáng thử cho người mới.
- **Tests rất nhiều** (997+) — chứng tỏ repo nghiêm túc về reliability, không phải toy project.
- **Tác giả ship liên tục**: có 9+ versions từ Feb 2026 đến Apr 2026 (3 tháng). Tốc độ cao = good signal nhưng cũng có nghĩa docs nhanh stale.
- **Naming dễ nhầm**: 3 identifier khác nhau (GitHub repo, plugin id, npm package). Phải nhớ context khi search/install.

## Cờ đỏ / Red flags & cautions

- **Phần README sau line 600 chưa đọc** — có thể có nội dung quan trọng chưa capture. **Action:** lần sau đọc nốt.
- **Số liệu version drift** — README có vẻ chưa được update hết khi v1.10.0 ra. Cần cross-check với code thật trước khi viết guide.
- **`multi-*` commands có dependency ngoài** không rõ pricing/licensing.
- **Repo CLAUDE.md mention `the-shortform-guide.md`** trong guides table nhưng tên file thật là `the-shortform-guide.md` — consistent. Tuy nhiên README dùng từ "Shorthand Guide" còn file là "shortform" — terminology hơi lệch.

## Cần làm gì tiếp / What to do next

1. **Đọc nốt README** từ line 600 → end (~700 lines còn lại) để capture đủ
2. **Ingest `the-shortform-guide.md`** — đây là entry point chính thức cho người mới theo lời README
3. **Verify số liệu agents/skills/commands** bằng cách đếm trực tiếp từ folder
4. **Tạo entity page đầu tiên** — chọn 1 trong 3: `Agents`, `Skills`, hoặc `Hooks` (concept nền tảng)
