# (C) Log — Everything Claude Code Wiki

> Append-only timeline. Mỗi entry bắt đầu bằng `## [YYYY-MM-DD] type | title` để parse được bằng grep.
> Append-only timeline. Each entry starts with `## [YYYY-MM-DD] type | title` for grep-friendly parsing.

---

## [2026-04-17] setup | Wiki khởi tạo / Wiki initialized

- Project scaffolded từ skill `new-project`
- Cloned `affaan-m/everything-claude-code` vào `00 Sources/everything-claude-code/`
- Tạo `(C) index.md` và `(C) log.md` ở `02 Wiki/`

## [2026-04-17] ingest | README.md (everything-claude-code)

- **Source:** `00 Sources/everything-claude-code/README.md` (67KB)
- **Coverage:** Đọc lines 1–600 (intro, what's new, quick start, what's inside, ecosystem tools); phần còn lại chưa đọc kỹ
- **Pages created:** [[(C) README summary]]
- **Pages updated:** [[(C) index]] — thêm row cho README summary
- **Open questions:** xem [[../01 Analysis/(C) README - open questions]]
- **Next:** đọc nốt phần sau line 600, hoặc chuyển sang ingest `the-shortform-guide.md` (15KB, README khuyến nghị "read this first")

## [2026-04-17] ingest | the-shortform-guide.md

- **Source:** `00 Sources/everything-claude-code/the-shortform-guide.md` (15.9KB, 432 lines)
- **Coverage:** Full file, đọc 1 pass
- **Pages created:** [[(C) Shortform Guide summary]]
- **Pages updated:**
  - [[(C) index]] — thêm row + identify 7 building blocks cần entity page riêng + ghi nhận beginner roadmap đầu tiên
  - [[../01 Analysis/(C) README - open questions]] — đánh dấu các câu hỏi đã được trả lời từ guide này
- **Key learnings:**
  - 7 building blocks: Skills, Commands, Hooks, Subagents, Rules, MCPs, Plugins
  - Skills > Commands (durable unit); commands là legacy shim
  - Context window discipline: 14 MCPs configured, ~5–6 enabled per project
  - 6 hook types: PreToolUse, PostToolUse, UserPromptSubmit, Stop, PreCompact, Notification
- **Next:** ingest `the-longform-guide.md` (14.8KB) cho token optimization & memory persistence; HOẶC tạo entity page đầu tiên cho 1 trong 7 building blocks (đề xuất: Hooks vì có cấu trúc rõ nhất)

## [2026-04-17] ingest | the-longform-guide.md

- **Source:** `00 Sources/everything-claude-code/the-longform-guide.md` (14.8KB, 354 lines)
- **Coverage:** Full file, đọc 1 pass
- **Pages created:** [[(C) Longform Guide summary]]
- **Pages updated:**
  - [[(C) index]] — thêm row, mở rộng concept list (8 advanced concepts mới)
  - [[../01 Analysis/(C) README - open questions]] — đánh dấu Q7 và Q8 đã được trả lời từ guide này; thêm câu hỏi mới
- **Key learnings:**
  - **Token economics** — model selection table (Haiku/Sonnet/Opus per task type); default Sonnet 90%, Opus chỉ khi 4 trigger condition
  - **MCP → CLI + skill** — pattern giảm context cost (không giảm token cost)
  - **mgrep** — ~50% token reduction vs grep (quantitative claim từ tác giả)
  - **Memory persistence** — 3 patterns: session `.tmp` files, dynamic system prompt injection (`--system-prompt`), 3 memory hooks (PreCompact, Stop, SessionStart)
  - **Continuous learning** — Stop-hook (KHÔNG dùng UserPromptSubmit để tránh latency mỗi prompt); v2 chi tiết kỹ thuật vẫn chưa rõ
  - **pass@k vs pass^k** — metric cốt lõi để hiểu reliability ≠ capability; cùng base rate 70%, k=5 → pass@k=97% vs pass^k=17%
  - **Iterative retrieval** — giải sub-agent context problem; orchestrator hỏi follow-up trước khi accept (max 3 cycles), pass objective context không chỉ query
  - **Sequential phases** — 5 phase (RESEARCH → PLAN → IMPLEMENT → REVIEW → VERIFY), `/clear` giữa các agent, intermediate output qua FILE
  - **Parallelization principle** — minimum viable amount, không arbitrary terminal counts
  - **Two-instance kickoff** — instance 1 scaffold, instance 2 deep research
  - **Compound effects philosophy** — đầu tư reusable patterns hoa lợi compound (cùng triết lý LLM Wiki của Karpathy)
- **Connection to Storm Bear vault:** Longform's "compound effects philosophy" (Omar Sar) **tương đồng** với LLM Wiki pattern (Karpathy) trong vault root CLAUDE.md. Cả hai đều dạy "đầu tư artifact persistent, hoa lợi compound theo thời gian." → Khi viết published guide, có thể cross-link để team hiểu vì sao đầu tư vào skills/wiki không phải overhead.
- **Next:** Có 3 hướng — (a) ingest `the-security-guide.md` (27.9KB, lớn nhất); (b) tạo entity page đầu tiên cho 1 building block (đề xuất Hooks); (c) verify số liệu agents/skills/commands bằng `ls`. Đề xuất (b) — đã có 3 source nói về Hooks, đủ để tổng hợp entity page chất lượng.

## [2026-04-17] entity | (C) Hooks (first entity page)

- **Type:** Building block #3 entity page — first prototype for entity-page format
- **Sources synthesized:** 4
  - `README.md` — `ECC_HOOK_PROFILE`/`ECC_DISABLED_HOOKS` env vars (lines 322–333)
  - `the-shortform-guide.md` — 6 hook types overview (lines 38–73)
  - `the-longform-guide.md` — memory persistence + continuous learning Stop-hook (lines 77–102)
  - `hooks/README.md` — full file (9.2KB), exact hook tables, recipes, schema, profiles
- **Pages created:** [[(C) Hooks]]
- **Pages updated:**
  - [[(C) index]] — Entities section bây giờ có table; mark Hooks ✅ trong building blocks list
- **Format prototype:** entity page có 11 sections — One-liner, When to use/not, Sub-types table, How it works (flow + schema), Async, Out-of-box list, Configuration, Recipes, Advanced patterns, Pitfalls, Tools, Cross-refs, Citations, TODO. Format này sẽ được tái dùng cho 6 building blocks còn lại.
- **Key decisions trong format:**
  - Bilingual chỉ ở header và one-liner; phần technical bằng tiếng Việt với term tiếng Anh giữ nguyên (vì nhanh hơn và term technical đã chuẩn quốc tế)
  - "When to use vs NOT use" đặt ngay đầu để beginner quyết định nhanh
  - "Common pitfalls" là section riêng (6 items) — beginner cần thấy trap trước khi chạy code
  - Cite line ranges cụ thể trong Citations để traceability
  - TODO section ở cuối để track gì còn thiếu (4 items)
- **TODO mới cho lần ingest tiếp:**
  - Đọc `hooks/hooks.json` (46.8KB) verify exact list
  - Đọc `rules/common/hooks.md` cho architecture guidelines
  - Đọc `scripts/hooks/session-start.js` v.v. cho memory persistence implementation
- **Next:** Có 4 hướng — (a) ingest `the-security-guide.md` (27.9KB) hoàn thành trinity guides; (b) tạo entity page #2 (Subagents — đã có 3 source); (c) đọc `skills/continuous-learning-v2/SKILL.md` giải Q15; (d) verify số liệu bằng `ls`. Đề xuất (b) Subagents để consolidate format entity page khi còn fresh.

## [2026-04-17] entity | (C) Subagents (second entity page)

- **Type:** Building block #4 entity page — re-test format prototype
- **Sources synthesized:** 6
  - `README.md`, lines 346–373 — list 28+ agents
  - `the-shortform-guide.md`, lines 76–95 — overview
  - `the-longform-guide.md`, lines 256–286 — context problem + iterative retrieval + sequential phases
  - `agents/planner.md` (full file, 6.9KB) — concrete with worked example
  - `agents/code-reviewer.md` (lines 1–80) — confidence-based filtering pattern
  - `agents/harness-optimizer.md` (full file, 928B) — minimal contrast
- **Pages created:** [[(C) Subagents]]
- **Pages updated:**
  - [[(C) index]] — Entities table + mark Subagents ✅
- **Q resolved (free bonus):** Q2 (số liệu agents/skills/commands mâu thuẫn) — đếm trực tiếp `ls agents/ | wc -l` = **48 agents**, match Quick Start, NOT match changelog v1.10.0 (38). → Quick Start chính xác, changelog outdated. Cập nhật trong open questions.
- **Format observations (compared to (C) Hooks):**
  - **Section structure giữ nguyên 11 sections** — generalizable ✅
  - **THÊM mới**: section "Subagent vs Hook vs Skill" — comparison table giúp beginner chọn đúng tool. Đáng tái dùng cho mọi entity page foundation. **Decision:** mỗi entity page foundation nên có 1 comparison section với các sibling.
  - **THÊM mới**: section "Anatomy" — show file format thực tế với frontmatter. Hooks không có (config qua JSON), nhưng agents/skills là markdown file → cần. **Decision:** entity nào có file format riêng thì có Anatomy.
  - **THÊM mới**: section "Patterns kết hợp" — Subagent + Skill, Subagent + Hook, Subagent + Plan Mode. Hooks chưa có, nhưng nếu redo có thể thêm. **Decision:** thêm vào tất cả foundation entity.
  - **Sub-types categorization** khác nhau: Hooks có 6 fixed types; Subagents có 48 instances → categorize theo role (Reviewer, Builder, Planner, Specialist, Operator). **Pattern:** fixed types → list table; many instances → category table.
  - **Anti-patterns** = "Common pitfalls" của Hooks → đổi tên cho consistency. **Decision:** chuẩn hoá thành "Anti-patterns / Sai lầm hay gặp" cho cả 2.
- **Format prototype giờ ổn định ở 11–13 sections:**
  1. One-liner (bilingual)
  2. When to use / NOT use
  3. **Comparison với sibling concepts** (mới)
  4. Sub-types / categorization
  5. **Anatomy** (nếu có file format) (mới)
  6. How it works (flow + schema)
  7. Out-of-box list (ECC ships)
  8. Configuration / scope
  9. Recipes / concrete examples
  10. Advanced patterns
  11. **Combination patterns** (mới)
  12. Anti-patterns
  13. Cross-refs + Citations + TODO
- **Next:** 4 hướng — (a) ingest `the-security-guide.md` (27.9KB); (b) entity page #3 (Skills — covered in 3+ sources, có `skills/` folder ~150 entries); (c) đọc `skills/continuous-learning-v2/SKILL.md` giải Q15; (d) retrofit (C) Hooks với 3 section mới (Comparison, Anatomy nếu apply, Combination patterns). Đề xuất **(d) trước** để cố định format, rồi (b) Skills.

## [2026-04-17] retrofit | (C) Hooks → khớp format chuẩn

- **Type:** Retrofit entity page #1 để khớp format đã chuẩn hoá sau entity page #2 (Subagents)
- **Pages updated:** [[(C) Hooks]] — thêm 3 section mới + rename 1 section
- **Sections thêm mới:**
  1. **"Hook vs Skill vs Subagent"** (sau "Khi nào dùng/KHÔNG dùng") — comparison table 7 tiêu chí + decision rule. Beginner cần để chọn đúng tool.
  2. **"Anatomy"** (trước "Cơ chế") — JSON config format với annotation, field reference table, matcher patterns hay dùng. Hooks có "file format" qua JSON nên section này áp dụng được (trước đó tưởng không apply).
  3. **"Patterns kết hợp"** (trước Anti-patterns) — 5 combo: Hook+Subagent, Hook+Skill, Hook+/compact, Hook chain (Pre+Post+Stop), Hook+ECC profile.
- **Section đổi tên:**
  - "Common Pitfalls / Sai lầm hay gặp" → "Anti-patterns / Sai lầm hay gặp" (consistency với (C) Subagents)
- **Format chuẩn hoá xong:** 13 sections, áp dụng cho mọi foundation entity. Quy tắc:
  - Sections 1-2 (One-liner, When to use/NOT) — luôn có
  - Section 3 (Comparison sibling) — luôn có cho foundation entity
  - Section 4 (Sub-types) — luôn có
  - Section 5 (Anatomy) — có nếu entity có file/config format riêng
  - Sections 6-10 (Cơ chế, Out-of-box, Configuration, Recipes, Advanced patterns) — tuỳ entity
  - Section 11 (Combination patterns) — luôn có cho foundation entity
  - Section 12 (Anti-patterns) — luôn có
  - Section 13 (Cross-refs + Citations + TODO) — luôn có
- **Next:** 4 hướng — (a) entity page #3 Skills (priority cao vì là building block lớn nhất, format đã ổn); (b) ingest `the-security-guide.md` 27.9KB; (c) đọc `skills/continuous-learning-v2/SKILL.md` giải Q15; (d) verify số liệu skills/commands counts. Đề xuất **(a) Skills**.

## [2026-04-17] entity | (C) Skills (third entity page)

- **Type:** Building block #1 entity page — primary workflow surface
- **Sources synthesized:** 5
  - `README.md`, lines 375–440 — skill list ~60 entries
  - `the-shortform-guide.md`, lines 13–34 — skills > commands, durable unit
  - `the-longform-guide.md`, lines 89–102 — continuous learning Stop-hook v1
  - `skills/tdd-workflow/SKILL.md` (lines 1–100, 12.8KB) — single-file skill example
  - `skills/continuous-learning-v2/SKILL.md` (full file, 12.3KB) — multi-file skill + giải Q15
  - `00 Sources/.../CLAUDE.md` (auto-loaded) — convention When to Use / How It Works / Examples
- **Pages created:** [[(C) Skills]] (~430 lines, lớn nhất từ trước đến nay vì có case study v2)
- **Pages updated:**
  - [[(C) index]] — Entities table + mark Skills ✅
  - [[../01 Analysis/(C) README - open questions]] — Q2 update (185 skills verified), Q7 ✅ full, Q15 ✅ full
- **Q resolved (2 questions giải full):**
  - Q7 ✅ Continuous Learning v1 vs v2 — full architecture: v1 Stop-hook probabilistic vs v2 PreTool+PostTool deterministic + atomic instincts + confidence scoring + project scoping (v2.1) + auto-promotion
  - Q15 ✅ Confidence scoring mechanism — tăng/giảm conditions, promote criteria
  - Q2 partial — skills count verified: 185 (≈ Quick Start 183, NOT changelog 156); còn commands count
- **Format observations:**
  - Format 13 sections vẫn work, nhưng (C) Skills lớn hơn 2 page trước vì có **case study riêng** cho continuous-learning v2 (Skill là building block lớn nhất nên đáng case study)
  - **Quy tắc mới phát hiện:** entity page có thể thêm "Case study" section khi entity có instance đặc biệt quan trọng. Vd Skills có case study "continuous-learning v2" vì nó là pattern "skill sinh ra skill". Subagents có thể có case study "iterative retrieval orchestrator" sau này.
  - "ECC ship X items" section dùng category table cho many-instance entities (Skills 185, Subagents 48). Hooks 6 types thì list table vì fixed.
- **Insight quan trọng từ ingest này:**
  - Skills là **primary surface**, vượt commands. Người mới nên học skills trước.
  - Multi-file skill (như continuous-learning-v2) là pattern complete: SKILL.md + agents/ + hooks/ + scripts/ + config.json. Đây là "skill thật sự" so với just-prompt.
  - **Continuous Learning v2 là self-improving system** — pattern observed → instinct → cluster → skill. Đây là cốt lõi của "compound effects philosophy" của ECC.
  - **Hook vs Skill cho observation:** v2 chuyển từ skill (probabilistic 50–80%) sang hook (deterministic 100%). Đây là design lesson lớn: nếu cần reliability, dùng hook không skill.
- **Next:** 5 hướng:
  - (a) entity page #4 — **Rules / Memory** (covered in 3+ source, có concrete file `rules/common/*.md` nhiều)
  - (b) entity page #5 — **MCPs** (đã có data từ 3 source, có `mcp-configs/` folder)
  - (c) entity page #6 — **Plugins** (data ít hơn, có thể chỉ 1 page mỏng)
  - (d) entity page #7 — **Commands (legacy)** (data tản, ít priority vì đang bị deprecate)
  - (e) ingest `the-security-guide.md` (27.9KB) hoàn thành trinity guides
  - **Đề xuất (a) Rules** — concept người mới cần hiểu thứ 4, có concrete grounding `rules/common/*.md` rất rõ; sau đó (e) security guide để hoàn thành philosophy layer.

## [2026-04-17] entity | (C) Rules and Memory (fourth entity page)

- **Type:** Building block #5 entity page — foundation 4/7 done
- **Sources synthesized:** 7
  - `README.md`, lines 477–492 — rules tree structure
  - `the-shortform-guide.md`, lines 99–124 — Rules and Memory overview
  - `the-longform-guide.md`, lines 38–86 — context management, dynamic system prompt, memory hooks
  - `rules/README.md` (full file, 4.5KB) — structure, install, precedence, naming convention
  - `rules/common/security.md` (full file, 862B) — concrete common rule
  - `rules/common/testing.md` (full file, 1.4KB) — concrete common rule
  - `rules/typescript/coding-style.md` (full file, 4.2KB) — concrete language rule với frontmatter
- **Pages created:** [[(C) Rules and Memory]] (~360 lines)
- **Pages updated:**
  - [[(C) index]] — Entities table + mark Rules/Memory ✅
- **Insight quan trọng / Important insights:**
  - **2 concept gộp 1 page:** Rules (static layer) + Memory (dynamic layer) — đi cùng nhau theo lời shortform guide. Decision đúng vì rules folder + CLAUDE.md cùng dùng để inject context.
  - **15 rule directories:** 1 common (10 files) + 14 language-specific (mỗi cái ~5 files). Tổng ~80 rule files.
  - **Frontmatter `paths:` field** cho language rules — chỉ trigger khi edit file match pattern. Anatomy section của Rules có cả 2 format: no-frontmatter (common) và with-frontmatter (language).
  - **Override hierarchy giống CSS specificity / .gitignore:** project rules > language rules > common rules. Common có thể đánh dấu "may be overridden" cho language idiom (vd Go's pointer receivers override "immutability").
  - **Discrepancy phát hiện:** `rules/README.md` ghi 8 common files; thực tế có 10 (thiếu `code-review.md` và `development-workflow.md`). README outdated → contribution opportunity (đã ghi vào TODO).
- **Format observations:**
  - **2 concept gộp 1 page** work tốt vì có overlap clear (cả Rules và CLAUDE.md đều là "always-loaded context"). Pattern này có thể áp dụng cho `Plugins + MCP-as-plugin` nếu data overlap.
  - **Comparison table 4 columns** (Rules vs Skills vs Hook vs CLAUDE.md) — phải lớn hơn comparison của entity trước (3 columns). Pattern: comparison table tăng theo complexity của entity.
  - **Real-world examples** section mới — list 5+ concrete CLAUDE.md từ examples/. Có giá trị beginner cao (copy-paste-modify). **Decision:** entity nào có examples/ folder dedicated → thêm "Real-world examples" section.
- **Bonus (Discrepancy ECC repo):** README ghi 8 common files thực tế 10. → Có thể submit PR fix README (ECC contribution opportunity #1 confirmed). Cùng với "Vietnamese translation" (opportunity #2 từ ingest README) và `mgrep` benchmark verify.
- **Status sau ingest này:**
  - **Foundation entity pages: 4/7 done** ✅ (Hooks, Subagents, Skills, Rules&Memory)
  - **Còn lại: 3 entity pages** — MCPs, Plugins, Commands (legacy)
  - Total wiki pages: 4 entity + 3 source summaries + 2 foundation (index, log) + 1 analysis = **10 pages**
- **Next:** 5 hướng:
  - (a) Tiếp entity page #5 — **MCPs** (covered in 2+ source, có `mcp-configs/` folder)
  - (b) Tiếp entity page #6 — **Plugins** (data ít hơn, page mỏng)
  - (c) Tiếp entity page #7 — **Commands legacy** (đang deprecate, có thể skip hoặc làm ngắn)
  - (d) Ingest `the-security-guide.md` (27.9KB) — security là first-class trong ECC, đáng đọc
  - (e) Bắt đầu **first published guide** trong `03 Published/` — sau 4 entity pages có đủ material cho "Beginner overview"
  - **Đề xuất (d) Security Guide** theo plan đã agree với user (sau Rules là Security guide).

## [2026-04-17] ingest | the-security-guide.md (trinity guides complete)

- **Source:** `00 Sources/everything-claude-code/the-security-guide.md` (27.9KB, 456 lines)
- **Coverage:** Full file, đọc 2 chunks (lines 1–400, 400–456)
- **Milestone:** ✅ **Trinity guides complete** — đã ingest cả Shortform + Longform + Security. Philosophy layer hoàn thành.
- **Pages created:** [[(C) Security Guide summary]] (~400 dòng)
- **Pages updated:** [[(C) index]] — thêm row với tagline "Never let the convenience layer outrun the isolation layer"
- **Key learnings:**
  - **2 real CVEs (Feb 25, 2026):** CVE-2025-59536 (CVSS 8.7, hook pre-trust execution); CVE-2026-21852 (ANTHROPIC_BASE_URL override leak API key). **Không còn là "this could happen but won't" — đã happen.**
  - **Simon Willison's lethal trifecta:** Private data + Untrusted content + External communication cùng runtime = prompt injection trở thành data exfiltration
  - **Attack surface expansion:** không chỉ chatbot input, mà email attachments, PR reviews, MCP tool descriptions, memory files, linked docs — mọi text Claude đọc đều là "executable context"
  - **6 defense layers:** Sandboxing / Sanitization / Approval (Least Agency) / Observability / Kill Switches / Memory Discipline
  - **11-item minimum bar checklist** — core deliverable, đáng bookmark
  - **"Agent 1 parse, Agent 2 act" split:** pattern tách document-parsing từ action-taking — liên quan sequential phases trong longform
  - **Snyk ToxicSkills study:** 36% / 3,984 skills có prompt injection; 1,467 malicious payloads → **skills = supply chain artifact, phải scan**
  - **Microsoft AI Recommendation Poisoning:** 31 companies / 14 industries; memory-oriented attacks → persistent memory is gasoline
  - **Dates:** CVE Feb 25 → Microsoft Feb 10 → Snyk Feb → Unit 42 Mar 3 → OpenAI Mar 11 → Hunt.io Feb 3 (17,470 OpenClaw exposed). **Timeline density cho thấy: security moved fast 2025→2026, chúng ta đang live trong thời gian đó.**
  - **AgentShield** — ECC's tool: 1282 tests, 98% coverage, 102 static analysis rules, 5 scan categories (secrets, permissions, hook injection, MCP risk, agent config)
- **Connection to Storm Bear vault:**
  - Vault không run agent autonomously → risk thấp, NHƯNG có lessons áp dụng:
    - **Sanitization:** khi ingest source từ web (như affaan-m repo), có thể chạy hidden Unicode scan trước
    - **Memory discipline:** CLAUDE.md rule "NEVER fabricate" + `(C)` prefix đã align với nguyên tắc. Có thể thêm: rotate/review memory files định kỳ
    - **Approval:** Plan mode (Shift+Tab) là approval gate kiểu "read-only research"
  - **Action item tương lai:** chạy `npx ecc-agentshield scan` cho setup Claude Code của bạn để check risky patterns
- **Format observations (summary page vs entity page):**
  - Summary page format (Shortform/Longform/Security) khác entity page format:
    - Summary: theo cấu trúc guide gốc, preserve narrative arc tác giả
    - Entity: theo 13-section canonical format
  - Security guide summary dài hơn 2 guide trước (~400 dòng) vì có nhiều code examples + checklist + closing quote preserved verbatim
  - **Phần "Connection to Storm Bear vault"** là section mới — áp dụng cho ingest nào có liên kết trực tiếp với vault context. **Decision:** giữ pattern này cho mọi source ingest tương lai.
- **Open questions mới (6 questions từ guide này):**
  - OWASP MCP Top 10 exact list chưa biết
  - `permissions.deny` field trong settings.json: built-in Claude Code hay ECC extension?
  - Dead-man switch có reference implementation trong ECC không?
- **Trinity guides complete means:**
  - ✅ Foundation philosophy layer: DONE
  - ✅ Entity pages: 4/7 done (Hooks, Subagents, Skills, Rules&Memory)
  - Remaining: MCPs, Plugins, Commands legacy (3 entities)
  - After that: first published guide in `03 Published/`
- **Next:** 4 hướng:
  - (a) Entity page #5 MCPs — có thêm security context giờ (OWASP MCP Top 10, tool poisoning awareness). Có `mcp-configs/` folder.
  - (b) Entity page #6 Plugins
  - (c) Entity page #7 Commands legacy
  - (d) **First published guide** — sau trinity guides + 4 entity pages, đủ material cho "Beginner overview for team" trong Vietnamese
  - **Đề xuất (a) MCPs** — vì security guide đã warm up context về MCP risk; làm MCPs khi còn fresh insight sẽ chất lượng hơn.

## [2026-04-17] entity | (C) MCPs (fifth entity page, security-aware)

- **Type:** Building block #6 entity page — first entity page làm SAU security guide ingest (warm security context)
- **Sources synthesized:** 6
  - `README.md`, lines 530–541 — mcp-configs folder structure
  - `the-shortform-guide.md`, lines 126–186 — MCP overview, context discipline, tác giả's 14 MCPs config
  - `the-longform-guide.md`, lines 22–33 — MCP → CLI + skill conversion pattern
  - `the-security-guide.md`, lines 34–40, 60–65 — MCP attack surface, OWASP MCP Top 10, MCP consent abuse CVE
  - `mcp-configs/mcp-servers.json` (full file, 6.6KB) — **27 MCPs pre-configured**
  - `skills/mcp-server-patterns/SKILL.md` (full file, 4KB) — build-your-own MCP reference
  - Bonus: `.mcp.json` (repo root) — minimal dev set 6 MCPs với version pinning
- **Pages created:** [[(C) MCPs]] (~430 lines, có cả security section)
- **Pages updated:**
  - [[(C) index]] — Entities table + mark MCPs ✅ (5/7 foundation done)
- **Q resolved (bonus):**
  - Đếm MCP pre-configured: **27 MCPs** (verify trong mcp-servers.json)
  - README "keep under 10 enabled" verified từ `_comments` trong config file
- **Key insights from ingest:**
  - **27 MCPs categorized** thành 11 nhóm (version control, DB, deployment, web, search, memory, reasoning, creative, filesystem, orchestration, testing, ecosystem)
  - **2 transport types:** stdio (local process, 18 MCPs) vs HTTP (remote endpoint, 9 MCPs)
  - **3 scope levels** của MCP config: user (`~/.claude.json`), project (`.mcp.json`, committed), local (`.claude.json.local`, gitignored)
  - **Security-aware insight:** `.mcp.json` committed = supply chain artifact. Repo malicious → MCP consent abuse CVE.
  - **Version pinning** (như ECC's own `.mcp.json`) là security best practice — pin `@2025.4.8` không `@latest`
  - **4 disable methods:** UI toggle, `disabledMcpServers` per-project, `ECC_DISABLED_MCPS` env var, just delete
  - **MCP → CLI + skill conversion** là pattern context-optimization quan trọng từ longform
  - **Lethal trifecta warning:** MCP untrusted + memory MCP + external communication cùng bật = exfiltration vector
- **Format observations:**
  - **Security section integrated trong entity page** (không chỉ riêng (C) Security Guide) — làm sau khi security ingest warm up context → entity page chất lượng hơn. **Decision:** entity nào có security angle rõ → integrate không chỉ cross-ref.
  - Recipe section có 4 concrete configs (minimal, dev team, research, security-first) — áp dụng mental model "progressive complexity". Pattern đáng tái dùng.
  - Comparison table đã scale lên **5 columns** (MCP vs CLI+Skill vs Hook vs Subagent + 1 new row "Security risk"). **Pattern:** security risk column là row mới nên thêm cho mọi comparison table sau này.
- **Status wiki sau ingest:**
  - **Foundation entity pages: 5/7 done** ✅ (Hooks, Subagents, Skills, Rules&Memory, MCPs)
  - **Còn lại: 2 entity pages** — Plugins, Commands (legacy)
  - Total wiki pages: 5 entity + 4 source summaries (trinity + README) + 2 foundation (index, log) + 1 analysis = **12 pages**
- **Next:** 3 hướng:
  - (a) Entity page #6 — **Plugins** (sources: README + shortform line 158–185, có thể cần đọc `.claude-plugin/plugin.json` và `.claude-plugin/marketplace.json` cho anatomy)
  - (b) Entity page #7 — **Commands legacy** (ngắn vì đang deprecate; sources: README + shortform line 22, có `commands/` folder)
  - (c) First published guide trong `03 Published/`
  - **Đề xuất (a) Plugins** — finish foundation 6/7 trước, sau đó Commands (nhẹ), sau đó published guide với đủ material.

## [2026-04-17] entity | (C) Plugins (sixth entity page, foundation 6/7 ✅)

- **Type:** Building block #7 entity page — bridge concept (not standalone component, but distribution mechanism)
- **Sources synthesized:** 5
  - `README.md`, lines 170–185, 254 — install commands, identifier convention
  - `the-shortform-guide.md`, lines 156–185, 287–309 — 14 plugin setup mẫu, LSP category
  - `.claude-plugin/plugin.json` (full file, 2.1KB) — ECC's own manifest
  - `.claude-plugin/marketplace.json` (full file, 1.2KB) — self-hosted marketplace catalog
  - `.claude-plugin/PLUGIN_SCHEMA_NOTES.md` (full file, 5.2KB) — **critical** validator quirks
  - `.claude-plugin/README.md` (full file, 1.2KB) — gotchas, transport notes
- **Pages created:** [[(C) Plugins]] (~430 lines)
- **Pages updated:**
  - [[(C) index]] — Entities table + foundation 7/7 building blocks marked done (except Commands)
- **Major discovery — Discrepancy #4:**
  - `plugin.json agents array length` = **38** (explicit file list, manifest v1.10.0)
  - `ls agents/*.md | wc -l` = **48** (filesystem, verified in (C) Subagents ingest)
  - **10 agent mới trên filesystem nhưng CHƯA được add vào plugin.json manifest**
  - → Nếu user install ECC qua `/plugin install`, plugin loader chỉ thấy 38 agents, miss 10 agents. Chỉ ai manual clone repo mới có full 48.
  - **Contribution opportunity #4** (trên danh sách: README rules count 8 vs 10, VI translation, mgrep benchmark verify, agent manifest drift)
- **Key insights from ingest:**
  - **Plugin là bridge concept** — không phải standalone building block mà là distribution mechanism cho 4 building blocks khác (agents, skills, commands, hooks)
  - **5 validator rule critical** (từ PLUGIN_SCHEMA_NOTES.md):
    1. `version` MANDATORY
    2. Component fields MUST be arrays
    3. `agents` MUST use explicit file paths (directory rejected)
    4. `commands`, `skills` directory OK (wrapped array)
    5. **KHÔNG ADD `hooks` field** — auto-loaded v2.1+, manual add = duplicate error
  - **Flip-flop history của `hooks` field** — 4 commits add/remove (`22ad036` → `a7bc5f2` → `779085e` → `e3a1306`) vì Claude Code CLI thay đổi convention giữa pre-v2.1 và v2.1+. Lesson: pin Claude Code version khi possible.
  - **Plugin KHÔNG install rules** — "Claude Code plugins cannot distribute rules automatically" (README). Rules phải manual `./install.sh`. Hybrid install model.
  - **3 identifier khác nhau của ECC:** GitHub (`affaan-m/everything-claude-code`), Plugin (`everything-claude-code@everything-claude-code`), npm (`ecc-universal`)
  - **Security angle:** Plugin install = executing code from external source. Supply chain attack vector thứ 2 sau MCP. Hook auto-load convention nguy hiểm nếu hook trong plugin chưa review.
- **Format observations:**
  - **Plugin là concept "bridge":** page phải explain nó KHÔNG giống 4 building blocks trước (agents/skills/hooks/MCPs) — nó là layer distribution. **Pattern:** entity page cho "bridge concepts" (Plugins, có thể Commands legacy sau này) cần section "Plugin vs các concepts khác" đặc biệt rõ.
  - **"Validator quirks" section** là section mới — khi entity có strict validation rules mà người mới dễ sai. **Decision:** thêm cho entity có schema validation (Plugins yes, Hooks có JSON schema có thể nên có, MCPs có schema nhưng lenient hơn).
  - **Flip-flop history pattern** (commits add/remove `hooks` field 4 lần) là data quan trọng cho learning — Preserve trong entity page khi relevant. Cho thấy "tech stack evolved, conventions shifted."
- **Status wiki sau ingest:**
  - **Foundation entity pages: 6/7 done** ✅✅✅✅✅✅ (Hooks, Subagents, Skills, Rules&Memory, MCPs, Plugins)
  - **Còn lại: 1 entity page** — Commands legacy (ngắn vì đang deprecate)
  - Total wiki pages: 6 entity + 4 source summaries + 2 foundation + 1 analysis = **13 pages**
- **Next:** 2 hướng:
  - (a) Entity page #7 — **Commands legacy** (~15 phút, ngắn vì đang migrate sang skills)
  - (b) First published guide trong `03 Published/`
  - **Đề xuất (a) Commands legacy** — khép lại foundation 7/7 trước, sau đó toàn tâm làm published guide với đủ material.

## [2026-04-17] entity | (C) Commands (SEVENTH entity page — FOUNDATION 7/7 COMPLETE) 🎉

- **Type:** Building block #2 entity page (LEGACY) — khép lại foundation layer
- **Milestone:** ✅ **7/7 building block entity pages hoàn thành**
- **Sources synthesized:** 5
  - `README.md`, lines 442–475, 254 — full command list, namespacing, multi-* runtime warning
  - `the-shortform-guide.md`, lines 13–34 — "commands/ layer is legacy slash-entry compatibility"
  - `commands/plan.md` (full file, 3.8KB) — concrete command WITH frontmatter
  - `commands/learn.md` (full file, 1.6KB) — concrete command WITHOUT frontmatter
  - Cross-ref với [[(C) Skills]] — migration target
- **Pages created:** [[(C) Commands]] (~330 dòng — ngắn hơn các entity khác vì nội dung focus vào "why deprecate + migration path")
- **Pages updated:**
  - [[(C) index]] — Entities table + thêm **Milestone section ngay đầu file** đánh dấu 7/7 complete
  - [[../01 Analysis/(C) README - open questions]] — **Q2 fully resolved** với commands count: 79 ✅ match Quick Start
- **Q resolved (Q2 fully closed):**
  - Commands count: **79 filesystem** ✅ = 79 Quick Start; ❌ ≠ 72 changelog
  - **Q2 complete:** Quick Start chính xác toàn bộ (48 agents / 185 skills / 79 commands). Changelog v1.10.0 outdated trên cả 3 số.
- **Key insights from ingest:**
  - **2 command format concurrent:**
    - Với frontmatter `description:` → auto-trigger (vd `plan.md`)
    - Không frontmatter → manual invoke only (vd `learn.md`)
  - **Command = shim** — body thường point tới agent/skill (`/plan` → planner agent; `/tdd` → tdd-workflow skill + tdd-guide agent)
  - **Migration matrix** — mỗi command map 1-1 với skill + agent combo. Đã document 9 commands với migration target trong entity page.
  - **Multi-* commands cần `ccg-workflow` runtime** cài riêng (`npx ccg-workflow`). Warning từ README lần 2.
  - **`/prp-plan`, `/prp-implement`** — newer replacement cho `/plan`, mention trong plan.md body. Có thể là skill chứ không phải command nữa? → ghi TODO.
  - **3 name forms:** plugin namespaced (`/ecc:plan`), manual root-level (`/plan`), disabled.
- **Format observations for bridge/legacy concept:**
  - Commands (legacy) follow **same 13-section format** mặc dù nó là bridge concept giống Plugins
  - **"Migration matrix" section mới** — thêm cho legacy/deprecated entity. Pattern: khi entity đang migrate, show explicit A→B mapping giúp user migrate từng phần.
  - Entity page ngắn hơn (~330 lines vs 400+) vì không cần advanced patterns — legacy concept không có "best practices" mới, chỉ có "why deprecate + how to migrate."
- **Status wiki sau ingest (FINAL):**
  - **Foundation entity pages: 7/7 DONE** 🎉
  - **Trinity guides: 3/3 DONE** (Shortform + Longform + Security)
  - **README summary: DONE**
  - **Total wiki pages: 14** (7 entity + 4 source summaries + 2 foundation + 1 analysis)
  - **Total sources ingested:** 15 files (3 guides + README + CLAUDE.md auto + 2 agent files + 2 skill files + 4 rule files + 2 MCP files + 4 plugin files + 2 command files, với overlap)
- **Q resolved tổng kết:**
  - ✅ Q1 (Skills vs Commands)
  - ✅ Q2 (Mâu thuẫn số lượng — 48/185/79 match Quick Start)
  - ✅ Q7 (Continuous Learning v1 vs v2)
  - ✅ Q8 (Iterative Retrieval)
  - ✅ Q15 (Confidence scoring mechanism)
  - ⏸ ~20+ open questions còn lại (verify các khái niệm technical, contribution opportunities, etc.)
- **4 contribution opportunities identified:**
  1. Fix `rules/README.md` (8 vs 10 common files count)
  2. Vietnamese translation cho README (chưa có VI; 6 ngôn ngữ khác đã có)
  3. Verify + cite `mgrep` 50-task benchmark (claim "~50% token reduction")
  4. Update `plugin.json agents array` từ 38 → 48 (10 agent manifest drift)
- **Next:** 2 hướng:
  - (a) **First published guide** trong `03 Published/` — sau foundation 7/7, đủ material cho "Beginner overview for team" bilingual
  - (b) Tạo page nâng cao (vd "Beginner roadmap 4 tuần" dựa trên action plan từ (C) Shortform Guide summary, nhưng standalone page)
  - **Đề xuất (a) First published guide** — đây là deliverable chính của project.

## [2026-04-17] publish | (C) Everything Claude Code - Huong dan cho nguoi moi (v1) 🚀

- **Type:** FIRST PUBLISHED GUIDE — deliverable chính của project cho team
- **Location:** `03 Published/(C) Everything Claude Code - Huong dan cho nguoi moi.md` (~500 lines, bilingual Vietnamese-primary)
- **Built on:** Toàn bộ wiki — 4 source summaries + 7 entity pages + 1 analysis
- **Structure 6 parts:**
  1. Tại sao đọc — audience, outcomes, non-goals
  2. Claude Code + ECC là gì — positioning, ECC vs DIY comparison
  3. 7 Building Blocks — table + mental model flow + reading priority order cho beginner
  4. Setup roadmap 4 tuần — concrete todos per tuần với commands cụ thể
  5. Security minimum bar — 11-item checklist + quick wins 15-phút
  6. FAQ + Resources — 7 câu hỏi thường gặp, cross-link tới wiki + external
- **Design decisions:**
  - **Vietnamese primary** theo project rule "song ngữ" nhưng tiếng Việt là ngôn ngữ chính cho beginner-friendly; technical terms giữ EN để tham chiếu source gốc
  - **Link heavy** — cross-ref 7 entity pages + 4 source summaries. User có thể đọc guide này như entry point, drill-down khi cần
  - **Copy-paste commands** — mọi action có command cụ thể, không bắt user tự figure out
  - **4-week cadence** — dựa trên action plan từ [[(C) Shortform Guide summary]], refined với insights từ full foundation 7/7
  - **Security-first** — phần 4 là MANDATORY section, không optional, vì CVE Feb 2026 đã thay đổi threat model
  - **FAQ realistic** — 7 câu hỏi thực (cost, Cursor vs Claude Code, team sharing, multi-* runtime, context window full, contribution) không phải marketing Q&A
- **Key insights integrated vào guide:**
  - 7 building blocks priority order cho beginner (⭐⭐⭐ Skills/Hooks/Rules first; ⭐⭐ Subagents/MCPs; ⭐ Plugins/Commands)
  - Rule vàng: "Skills are primary workflow surface. Commands is legacy."
  - Context discipline: 14 MCPs configured, 5-6 enabled per project
  - Model routing: Sonnet default 90%, Opus chỉ khi 4 triggers
  - Security: "Never let the convenience layer outrun the isolation layer"
  - 4 contribution opportunities — invite team contribute back
- **Pages updated:**
  - [[(C) index]] — thêm "Published guides" section, update milestone với "First published guide shipped"
- **Format observations:**
  - **Guide published khác summary/entity page:**
    - Entity page: 13-section canonical structure, technical reference style
    - Source summary: preserve tác giả narrative arc
    - **Published guide:** **linear narrative** với progressive disclosure (intro → foundation → action → security → FAQ → resources). Optimized cho "đọc 1 lần xong hiểu"
  - **Length ~500 lines là sweet spot** — nhỏ hơn thì thiếu actionable; lớn hơn thì overwhelm beginner
  - **Part 4 (Security) placed giữa guide** không phải cuối — security phải integrated vào onboarding, không treat như afterthought
  - **FAQ dùng bảng** cho compare decisions (Cursor vs Claude Code) — visual, easy scan
- **Status wiki sau milestone:**
  - Wiki foundation: ✅ 4 source summaries + 7 entity pages + 1 analysis + 2 foundation pages = 14 wiki pages
  - **Published guides: 1** ✅ (v1 shipped)
  - **Total project files: 15** (14 wiki + 1 published)
- **Project CLAUDE.md update cần thiết:**
  - Status "Just created — chưa ingest source nào" → outdated. Cần update thành "v1 published guide shipped — ready for team distribution"
- **Next:** Sau milestone này:
  - (a) Update project CLAUDE.md "Current Status" section
  - (b) Tạo iteration log entry trong `07 Iteration Logs/` ghi lại learnings từ v1
  - (c) Collect team feedback → v1.1 plan
  - (d) Contribute PR cho ECC repo (1 trong 4 opportunities, ưu tiên: Vietnamese translation vì Storm Bear đã có bilingual material)
  - (e) Consider advanced guides: "Token optimization deep dive", "Setup team marketplace", "Autonomous loops safely"

## [2026-04-17] contribute | Vietnamese README translation (contribution opportunity #2) 🇻🇳

- **Type:** FIRST upstream contribution prep — targeting `affaan-m/everything-claude-code`
- **Scope:** Add Vietnamese (Tiếng Việt) README, bringing ECC's language coverage từ 7 → 8 languages
- **Precedent analysis:**
  - 6 existing translations: en, pt-BR (518 lines), zh-CN (819), zh-TW (482), ja-JP (795), ko-KR (731), tr (466)
  - All are **partial translations** — ~1/3 to 1/2 của English (1498 lines)
  - Shortest (Turkish, 466 lines) dùng làm template cho VN
- **Files prepared:**
  - `03 Published/contributions/vi-translation/docs/vi/README.md` — **486 lines** (match precedent, between Turkish 466 và pt-BR 518)
  - `03 Published/contributions/vi-translation/PR-INSTRUCTIONS.md` — submission guide với 8 banner update diffs, step-by-step PR steps, commit message template, PR description template, pre-submit checklist
- **Translation structure** (theo Turkish template):
  1. Header + badges
  2. Language switcher banner (thêm VI vào position cuối)
  3. Tagline + positioning
  4. Guides section (3 guides)
  5. What's New — 3 latest versions only (v1.10, v1.9, v1.8)
  6. Quick Start (3 steps)
  7. Cross-platform support
  8. What's Inside (folder structure tree)
  9. Which Agent to Use (decision table + 3 common workflows)
  10. FAQ (7 collapsible sections including **new security section** — reference tới Security Guide, 2 CVE awareness)
  11. Running Tests
  12. Contributing
  13. License
- **Translation philosophy:**
  - Vietnamese cho narrative prose và process descriptions
  - English preserved cho technical terms (plugin, hook, skill, agent, MCP, command, workflow) — wrap backticks
  - Code blocks, URLs, CVE IDs, version numbers, file paths giữ nguyên
  - Tone: engineering-pragmatic, match source (not marketing-fluffy)
  - Examples dịch ("Add user authentication" → "Thêm user authentication") nhưng command syntax giữ English
- **Banner updates prepared cho 8 files:**
  1. `README.md` (English, root) — 2 banner lines
  2. `README.zh-CN.md` (root) — 1 banner line
  3. `docs/pt-BR/README.md` — 2 banner lines
  4. `docs/ja-JP/README.md` — 2 banner lines
  5. `docs/ko-KR/README.md` — 2 banner lines
  6. `docs/zh-TW/README.md` — 1 banner line
  7. `docs/tr/README.md` — 1 banner line
  - Total: **12 lines of banner updates**
- **Bonus sections added** (so với Turkish):
  - Security FAQ section — reference Security Guide + AgentShield (vì Storm Bear wiki đã ingest Security Guide, có advantage này)
  - Full folder structure tree với 48 agents (Turkish ghi "28 agents" — outdated v1.10.0 metadata drift)
  - Correct counts (48 agents / 183 skills / 79 commands) — verified trong Q2 resolution
- **Value-adds cho team Vietnamese:**
  - Giảm barrier entry cho VN developer community
  - Terminology bilingual approach → dev quen English technical terms không bị confused
  - Security-first framing (không phổ biến trong VN tech scene)
- **Connection to Storm Bear wiki:**
  - Reuse được ~40% material từ published guide (common concepts đã Vietnamese-ized)
  - Reuse được categorization decisions từ entity pages
  - Verified counts từ Q2 resolution → VN README có data chính xác hơn Turkish (outdated at v1.10)
- **Status of contribution:**
  - ✅ Translation file complete (486 lines)
  - ✅ PR instructions complete với exact diffs cho 8 files
  - ✅ Commit message + PR description templates ready
  - ⏸ Pending user action: fork ECC, apply changes, submit PR
- **Contribution opportunities status:**
  - [x] #2 Vietnamese translation — ✅ **PREPARED** (ready for user to submit)
  - [ ] #1 Fix `rules/README.md` (8 vs 10 common files count)
  - [ ] #3 Verify + cite `mgrep` 50-task benchmark
  - [ ] #4 Update `plugin.json agents array` (38 → 48)
- **Next:**
  - User submits PR (step-by-step trong PR-INSTRUCTIONS.md)
  - Maintainer review (tác giả Affaan, typical turnaround theo PR history: vài ngày đến 1-2 tuần)
  - After merge: follow-up contributions (docs/vi/CLAUDE.md, CONTRIBUTING.md, TERMINOLOGY.md — pt-BR có precedent)
  - Sau đó có thể tiếp tục với #1 (rules README fix, trivial) hoặc #4 (plugin.json update, cần maintainer decision)

## [2026-04-17] iteration-log | v1 build learnings captured 📒

- **Type:** First iteration log entry — deliverable meta-learning cho Storm Bear vault
- **Location:** `07 Iteration Logs/(C) 2026-04-17 v1 build learnings.md` (~400 dòng)
- **Purpose:** Capture patterns, learnings, anti-patterns từ session này để tái dùng cho LLM Wiki project tiếp theo
- **9 sections:**
  1. Tóm tắt session
  2. **What worked well** (9 items) — iterative format evolution, early verification, open questions file, cross-ref discipline, security timing, case study subsection, progressive disclosure, bilingual pragmatic, chapter-by-chapter user confirmation
  3. **What didn't work** (5 items) — large source chunking sai strategy, entity #1 retrofit debt, count verification prolonged, TodoWrite start late, không dispatch codebase search agents
  4. **Patterns & templates** — 6 reusable patterns (13-section format, source summary format, foundational files, discrepancy-as-content, bilingual framework, cross-ref forward-declaration)
  5. **Metrics & numbers** — session throughput, file sizes, time estimates cho project sau
  6. **Recommendations** cho LLM Wiki projects tương lai (12 items)
  7. **Storm Bear vault context** — threshold "đáng build wiki" (≥5 sources, ≥3 months lifespan)
  8. **Meta-learning** — LLM Wiki pattern proven, evidence-based
  9. **Action items** cho vault level (update root CLAUDE.md, skill template, etc.)
- **Key pattern captured: 13-section canonical entity page format** — generalizable cho mọi future LLM Wiki project về codebase/tool
- **Key insight: Verify LLM Wiki pattern hypothesis** — Karpathy's thesis proven empirically qua project này:
  - ✅ Knowledge compounds (security context improved MCPs entity)
  - ✅ Cross-refs emerge naturally (14 pages interconnected)
  - ✅ Contradictions surface (4 discrepancies found)
  - ✅ Published output stronger (guide → entity → summary → source chain)
- **Stats memorable:**
  - ~213K tokens output trong 1 session
  - 17 files total (14 wiki + 1 published + 2 contribution + 1 iteration log)
  - ~6/28 open questions resolved
  - 4 contribution opportunities identified
  - Format evolved 11 → 13 sections sau entity #2
- **Recommendations quan trọng nhất cho project sau:**
  - Skim full source TRƯỚC deep read (nếu >20KB)
  - Entity #1 là prototype, expect retrofit sau #2-3
  - Verify counts bằng filesystem NGAY khi raise question
  - Ingest philosophy TRƯỚC detail khi có overlap
  - Published guide ≠ entity page (linear vs reference format)
- **Cross-refs thêm:** All wiki pages, published guide, contribution folder
- **Next iterations của iteration log:**
  - v1.1 (sau team feedback trên published guide): update throughput với real team data
  - v2 (sau project LLM Wiki tiếp theo): compare patterns cross-project, distill meta-patterns
- **Status wiki cuối cùng sau session:**
  - **Total files: 18** (14 wiki + 1 published + 2 contribution + 1 iteration log)
  - Foundation: 2 (index, log)
  - Source summaries: 4 (trinity + README)
  - Entity pages: 7/7 ✅
  - Analysis: 1 (open questions)
  - Published guides: 1 (v1)
  - Upstream contributions prepared: 1 (VN translation)
  - **Iteration logs: 1** ✅
- **Next for this project:**
  - (a) Ship VN translation PR (upstream contribution #2)
  - (b) Ship combo với #1 (rules README count fix)
  - (c) Collect team feedback → v1.1 published guide
  - (d) Move on to next project in vault
