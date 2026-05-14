# claude-code-system-prompts — Hướng dẫn cho người mới / Beginner's Guide

> **Subject:** [`Piebald-AI/claude-code-system-prompts`](https://github.com/Piebald-AI/claude-code-system-prompts)
> **Built by:** [Piebald-AI](https://piebald.ai) — corporate-org behind Piebald commercial agentic IDE
> **Wiki version:** v65 — 2026-05-13 → 2026-05-14 (Storm Bear vault, llm-wiki-routine-v2.1)
> **License:** MIT
> **Stars / forks:** 10,176 / 1,811 — ~176 ngày tuổi tại thời điểm phân tích
> **Bài viết bằng tiếng Việt và tiếng Anh / Bilingual: Vietnamese & English**

---

## 1. claude-code-system-prompts là gì? / What is it?

### 🇻🇳 Tiếng Việt

`claude-code-system-prompts` là một **kho lưu trữ tham khảo (reference archive)** chứa **TẤT CẢ các phần system prompt của Claude Code** — được trích xuất tự động từ source code đã compile của Claude Code (gói npm `@anthropic-ai/claude-code`).

**Quan trọng cần hiểu:**
- Đây **KHÔNG phải plugin / skill / tool** mà bạn cài để chạy. Đây là **tài liệu tham khảo**.
- Đây **KHÔNG do Anthropic làm** — do Piebald-AI (một công ty khác) làm bằng cách đọc source code compile của Claude Code.
- Sửa file trong repo này **không thay đổi** cách Claude Code hoạt động. Nếu muốn sửa Claude Code thật, dùng tool chị em **tweakcc**.
- Cập nhật **trong vòng vài phút** sau mỗi bản release Claude Code mới.

**Phạm vi:**
- **293 file system prompt** trong thư mục `system-prompts/`
- **110+ prompt khác nhau** (một số prompt được tách thành nhiều mảnh)
- 6 nhóm chính: Agent Prompts / Data templates / System Prompt fragments / System Reminders / Tool Descriptions / Skills
- **211 KB CHANGELOG** ghi lại **176 phiên bản** Claude Code từ v2.0.14 đến v2.1.140 (12/5/2026)
- Phiên bản đang tracking tại thời điểm wiki: **Claude Code v2.1.140**

### 🇬🇧 English

`claude-code-system-prompts` is a **reference archive** containing **ALL parts of Claude Code's system prompts** — automatically extracted from Claude Code's compiled source code (the `@anthropic-ai/claude-code` npm package).

**Important to understand:**
- This is **NOT a plugin / skill / tool** you install to run. It's **reference documentation**.
- This is **NOT made by Anthropic** — it's made by Piebald-AI (a different company) by reading Claude Code's compiled source.
- Editing files in this repo does **NOT change** Claude Code's behavior. To actually modify Claude Code, use the sister tool **tweakcc**.
- Updated **within minutes** of each new Claude Code release.

**Scope:**
- **293 system-prompt files** in the `system-prompts/` directory
- **110+ distinct prompts** (some prompts split into multiple fragments)
- 6 main categories: Agent Prompts / Data templates / System Prompt fragments / System Reminders / Tool Descriptions / Skills
- **211 KB CHANGELOG** tracking **176 versions** of Claude Code from v2.0.14 through v2.1.140 (May 12, 2026)
- Tracking Claude Code v2.1.140 at wiki time.

---

## 2. Ai là tác giả? Tại sao quan tâm? / Who's the author? Why care?

### 🇻🇳 Tiếng Việt

Tác giả là **Piebald-AI** (`github.com/Piebald-AI`) — một **công ty thương mại** (không phải cá nhân solo) đang xây dựng **Piebald** — "ultimate agentic AI developer experience" tại piebald.ai.

Piebald-AI có **portfolio 3 sản phẩm:**

| Sản phẩm | Vai trò | License |
|---|---|---|
| **Piebald** (piebald.ai) | Sản phẩm thương mại — agentic AI developer experience | Commercial / closed |
| **claude-code-system-prompts** (repo này) | Kho tham khảo open-source | MIT |
| **tweakcc** | Tool patch Claude Code installation | (likely MIT) |

**Chiến lược ngầm:**
- **Piebald commercial** = sản phẩm tạo doanh thu, cạnh tranh trong cùng không gian với Claude Code
- **claude-code-system-prompts (open-source)** = thể hiện độ sâu kiến thức về Claude Code của team Piebald-AI + hút audience về piebald.ai qua README banner
- **tweakcc (open-source)** = tool thực dụng cho power-user Claude Code; tiếp tục build brand Piebald-AI

Đây là chiến lược **"quan sát-làm-marketing"** (observation-as-marketing) — open-source reverse-engineering hút Claude Code power-user, từ đó chuyển đổi sang đánh giá Piebald commercial.

**Tại sao đây là quan sát đặc biệt trong corpus Storm Bear:**

Trong 64 wiki trước, đây là **N=4 sub-archetype "corporate-observation-as-marketing-with-tooling"** trong Pattern #19 ecosystem-portfolio-builder — bổ sung **archetype corporate-org đầu tiên** (sau 3 archetype solo: gotalab v61 + forrestchang v63 + AgriciDaniel v64).

### 🇬🇧 English

The author is **Piebald-AI** (`github.com/Piebald-AI`) — a **commercial company** (NOT a solo individual) building **Piebald** — "ultimate agentic AI developer experience" at piebald.ai.

Piebald-AI has a **3-product portfolio:**

| Product | Role | License |
|---|---|---|
| **Piebald** (piebald.ai) | Commercial product — agentic AI developer experience | Commercial / closed |
| **claude-code-system-prompts** (this repo) | Open-source reference archive | MIT |
| **tweakcc** | Tool to patch Claude Code installations | (likely MIT) |

**Implicit strategy:**
- **Piebald commercial** = revenue product, competes in the same space as Claude Code
- **claude-code-system-prompts (open-source)** = demonstrates Piebald-AI's deep Claude Code expertise + draws audience to piebald.ai via README banner
- **tweakcc (open-source)** = practical tool for Claude Code power-users; further builds Piebald-AI brand

This is **"observation-as-marketing"** strategy — open-source reverse-engineering attracts Claude Code power-users who become candidates for evaluating Piebald commercial.

**Why this is a notable observation in the Storm Bear corpus:**

In the 64 prior wikis, this is the **N=4 sub-archetype "corporate-observation-as-marketing-with-tooling"** within Pattern #19 ecosystem-portfolio-builder — adding the **first corporate-org archetype** (after 3 solo archetypes: gotalab v61 + forrestchang v63 + AgriciDaniel v64).

---

## 3. Làm gì với repo này? / What do you do with this repo?

### 🇻🇳 Tiếng Việt

README cung cấp 3 cách sử dụng:

1. **Tham khảo (Reference):** Đọc để hiểu Claude Code đang dùng prompt gì, prompt thay đổi như thế nào qua các phiên bản
2. **Patch local Claude Code:** Dùng tool chị em **tweakcc** để customize các phần prompt trong Claude Code installation của bạn
3. **Đề xuất tính năng cho Claude Code:** Tạo issue tại [anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues) (Piebald-AI **không** nhận PR cho việc thay đổi prompt — họ chỉ extract, không sửa)

**Cho người mới với Claude Code:**
- Đọc `system-prompts/system-prompt-doing-tasks-software-engineering-focus.md` để hiểu Claude Code coi mình là gì
- Đọc `system-prompts/tool-description-bash-overview.md` + 28 sub-fragment Bash để thấy mức độ chi tiết về cách Claude Code đối xử với shell
- Đọc CHANGELOG (CTRL+F bản version mới nhất) để xem những thay đổi mới nhất

**Cho người làm skill/plugin cho Claude Code:**
- Đọc skill prompts của Anthropic (`skill-init-claudemd-and-skill-setup-new-version.md` 5,384 tks + `skill-verify-skill.md` 2,694 tks) để học format/style
- Đọc Data templates (50 file) để thấy Anthropic embed gì sẵn trong system prompt (8 ngôn ngữ SDK + Managed Agents docs)
- Tham khảo Model migration guide (file LỚN NHẤT trong archive — 18,340 tks) để hiểu cách Anthropic xử lý version migration

### 🇬🇧 English

The README provides 3 usage modes:

1. **Reference:** Read to understand what prompts Claude Code uses, how prompts change across versions
2. **Local Claude Code patching:** Use sister tool **tweakcc** to customize prompt pieces in your Claude Code installation
3. **Feature requests for Claude Code:** File issues at [anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues) (Piebald-AI does **NOT** accept PRs for prompt changes — they only extract, don't modify)

**For Claude Code beginners:**
- Read `system-prompts/system-prompt-doing-tasks-software-engineering-focus.md` to understand how Claude Code sees its role
- Read `system-prompts/tool-description-bash-overview.md` + 28 Bash sub-fragments to see the granularity of Claude Code's shell discipline
- Read CHANGELOG (Ctrl+F latest version) to see recent changes

**For skill/plugin builders for Claude Code:**
- Read Anthropic's skill prompts (`skill-init-claudemd-and-skill-setup-new-version.md` 5,384 tks + `skill-verify-skill.md` 2,694 tks) to learn format/style
- Read Data templates (50 files) to see what Anthropic embeds in system prompts (8 SDK languages + Managed Agents docs)
- Reference Model migration guide (LARGEST file in archive — 18,340 tks) to understand Anthropic's version-migration handling

---

## 4. Có gì đặc biệt trong corpus? / What's notable in the corpus?

### 🇻🇳 Tiếng Việt

Đây là wiki **đặc biệt nhất trong 65 wiki Storm Bear** vì 3 lý do:

**(a) Quan sát đệ quy ở độ sâu tối đa**

Claude Code là **sản phẩm được cite nhiều nhất** trong toàn bộ corpus 64 wiki trước:
- Mọi wiki T1 (mattpocock / awesome-claude-skills / agent-skills-of-vercel / karpathy-skills / claude-seo / cc-sdd / codex-plugin-cc / claude-howto / claude-hud / claude-context / oh-my-claudecode / etc.) đều reference Claude Code làm host
- Nhiều wiki T4 (free-claude-code v60 translate sang Claude Code's API) reference Claude Code
- LLM Wiki Routine v2.1 của Storm Bear **chạy ON** Claude Code

V65 = **trực tiếp document internals của sản phẩm được reference nhiều nhất** — đệ quy ở độ sâu tối đa có thể quan sát được.

**(b) Bằng chứng N=2 nhanh nhất trong lịch sử corpus cho Pattern #78 mới đăng ký**

Pattern #78 Living-Domain-Standards Tracking vừa đăng ký N=1 tại v64 (2026-05-13, claude-seo). V65 (2026-05-13/14, claude-code-system-prompts) cung cấp **bằng chứng N=2 trong vòng 1 wiki** — chu kỳ un-stale nhanh nhất trong lịch sử 64-wiki corpus.

Pattern #78 N=2:
- **78a multi-vendor industry standards** (claude-seo v64 — Google Quality Rater Guidelines + Schema.org + ISO codes)
- **78b single-vendor product-internals archive** (claude-code-system-prompts v65 — Anthropic Claude Code system prompts)

Pattern #78 **PROMOTION-ELIGIBLE tại v66 audit (accelerated)** hoặc v67 (mặc định).

**(c) Phase 0.9 STRICT 3-of-4 STRONG PASS — STRONGEST trong lịch sử 10-instance window**

Storm Bear vault có discipline Phase 0.9 STRICT để quyết định có thêm Storm Bear meta-entity (entity slot thứ 4) cho mỗi wiki hay không. Tiêu chí: (a) author archetype peer / (b) operational tool / (c) methodology-influence / (d) in-corpus-reference.

V65 đạt **3-of-4 STRONG PASS** (chỉ FAIL ở (a) — Piebald-AI corporate-org không phải solo-individual peer):
- (b) **STRONG**: Storm Bear vault chạy ON Claude Code substrate
- (c) **STRONG**: Claude Code system prompts shape vault routine design
- (d) **STRONGEST trong corpus history**: Claude Code = sản phẩm được reference nhiều nhất

V65 = INCLUDE mạnh nhất trong 10-instance Phase 0.9 post-amendment window (80% INCLUDE rate sau v65).

### 🇬🇧 English

This is the **most notable wiki in Storm Bear's 65-wiki corpus** for 3 reasons:

**(a) Maximum-depth corpus-recursive observation**

Claude Code is the **most-referenced product** across all 64 prior corpus wikis:
- Every T1 wiki (mattpocock / awesome-claude-skills / agent-skills-of-vercel / karpathy-skills / claude-seo / cc-sdd / codex-plugin-cc / claude-howto / claude-hud / claude-context / oh-my-claudecode / etc.) references Claude Code as host
- Many T4 wikis (free-claude-code v60 translates to Claude Code's API) reference Claude Code
- Storm Bear's LLM Wiki Routine v2.1 **runs ON** Claude Code

V65 = **directly documents the internals of the most-referenced product** — corpus-recursive at maximum observable depth.

**(b) Fastest N=2 evidence in corpus history for newly-registered Pattern #78**

Pattern #78 Living-Domain-Standards Tracking was just registered N=1 at v64 (2026-05-13, claude-seo). V65 (2026-05-13/14, claude-code-system-prompts) provides **N=2 evidence within 1 wiki** — fastest un-stale cycle in 64-wiki corpus history.

Pattern #78 N=2:
- **78a multi-vendor industry standards** (claude-seo v64 — Google Quality Rater Guidelines + Schema.org + ISO codes)
- **78b single-vendor product-internals archive** (claude-code-system-prompts v65 — Anthropic Claude Code system prompts)

Pattern #78 **PROMOTION-ELIGIBLE at v66 audit (accelerated)** or v67 (default).

**(c) Phase 0.9 STRICT 3-of-4 STRONG PASS — STRONGEST in 10-instance window history**

Storm Bear vault has Phase 0.9 STRICT discipline to decide whether to add Storm Bear meta-entity (4th entity slot) for each wiki. Criteria: (a) author archetype peer / (b) operational tool / (c) methodology-influence / (d) in-corpus-reference.

V65 achieves **3-of-4 STRONG PASS** (only FAILs (a) — Piebald-AI corporate-org isn't solo-individual peer):
- (b) **STRONG**: Storm Bear vault runs ON Claude Code substrate
- (c) **STRONG**: Claude Code system prompts shape vault routine design
- (d) **STRONGEST in corpus history**: Claude Code = most-referenced product

V65 = strongest INCLUDE in 10-instance Phase 0.9 post-amendment window (80% INCLUDE rate after v65).

---

## 5. Số liệu nhanh / Quick stats

### 🇻🇳 Tiếng Việt

| Thông tin | Giá trị |
|---|---|
| Stars / Forks | **10,176 / 1,811** |
| Tỷ lệ fork | **17.8%** — kỷ lục corpus về active-deployment intent (vượt claude-seo v64 15.3%) |
| Stars/day | ~57.8 (medium-high engagement; dưới ngưỡng Pattern #52 EXTREME-VIRAL 300+/day) |
| Tuổi repo | ~176 ngày (created 18/11/2025) |
| Last push | 13/5/2026 — 1 ngày trước khi build wiki |
| **CHANGELOG** | **211 KB / 1,896 dòng / 176 versions** (127 full + 49 placeholder) |
| **System-prompt files** | **293 file** trong 6 categories |
| **Token nhiều nhất 1 file** | Model migration guide — **18,340 tokens** |
| **Token nhiều nhất 1 tool description** | TodoWrite — 2,037 tokens |
| **Token nhiều nhất 1 agent prompt cluster** | Security monitor (first+second part) — 7,468 tokens combined |
| Cadence update | **Trong vòng vài phút** sau mỗi Claude Code release |
| Sister tool | **tweakcc** (separate repo) |

### 🇬🇧 English

| Metric | Value |
|---|---|
| Stars / Forks | **10,176 / 1,811** |
| Fork ratio | **17.8%** — corpus-record active-deployment intent (exceeds claude-seo v64 15.3%) |
| Stars/day | ~57.8 (medium-high engagement; below Pattern #52 EXTREME-VIRAL 300+/day threshold) |
| Repo age | ~176 days (created Nov 18, 2025) |
| Last push | May 13, 2026 — 1 day before wiki build |
| **CHANGELOG** | **211 KB / 1,896 lines / 176 versions** (127 full + 49 placeholder) |
| **System-prompt files** | **293 files** in 6 categories |
| **Largest single file (by tokens)** | Model migration guide — **18,340 tokens** |
| **Largest tool description** | TodoWrite — 2,037 tokens |
| **Largest agent prompt cluster** | Security monitor (first+second part) — 7,468 tokens combined |
| Update cadence | **Within minutes** of each Claude Code release |
| Sister tool | **tweakcc** (separate repo) |

---

## 6. Điểm cần lưu ý / Caveats

### 🇻🇳 Tiếng Việt

**(a) Đây là tài liệu tham khảo, KHÔNG sửa được**

Project CLAUDE.md cảnh báo rõ: *"For AI agents working with this repository: These files are extracted reference material, not modifiable source code. Editing files here does not change Claude Code's behavior."*

Nếu bạn muốn sửa thực sự cách Claude Code hành xử trên máy local, **phải dùng tweakcc** (sister tool).

**(b) Template variables hiện ra dạng `${VAR}`**

Một số prompt chứa biến template như `${BASH_TOOL_NAME}` — chúng được interpolate runtime bởi Claude Code, **không** được resolve trong các file ở đây. Đọc với chú ý.

**(c) Sai số ±20 token**

README công bố sai số tối đa ~20 token so với runtime values. Đủ chính xác cho mọi mục đích thực tế nhưng không phải bit-exact.

**(d) Không phải source code Claude Code**

Đây là extract từ compiled JavaScript — **không có business logic** của Claude Code, chỉ có **prompt strings**. Để hiểu Claude Code làm gì với prompt, vẫn cần thử nghiệm.

**(e) Anthropic không endorse — nhưng không chống**

Piebald-AI tự ghi: *"Maintained by Piebald AI, not by Anthropic."* Anthropic không issue DMCA hay cease-and-desist — có vẻ **tolerate** việc extraction. Đây là điểm thú vị về văn hóa ecosystem agentic-AI: vendor chấp nhận third-party reverse-engineering ở mức độ này.

### 🇬🇧 English

**(a) This is reference material, NOT modifiable**

Project CLAUDE.md explicitly warns: *"For AI agents working with this repository: These files are extracted reference material, not modifiable source code. Editing files here does not change Claude Code's behavior."*

If you want to actually modify Claude Code's behavior on your local machine, **you must use tweakcc** (sister tool).

**(b) Template variables appear as `${VAR}`**

Some prompts contain template variables like `${BASH_TOOL_NAME}` — these are interpolated at runtime by Claude Code, **not** resolved in the files here. Read with that in mind.

**(c) ±20 token tolerance**

README discloses maximum ~20 token tolerance from runtime values. Accurate enough for practical purposes but not bit-exact.

**(d) NOT Claude Code source code**

This is extracted from compiled JavaScript — **no business logic** of Claude Code, only **prompt strings**. To understand what Claude Code DOES with prompts, you still need experimentation.

**(e) Anthropic doesn't endorse — but doesn't oppose**

Piebald-AI explicitly states: *"Maintained by Piebald AI, not by Anthropic."* Anthropic has NOT issued DMCA or cease-and-desist — appears to **tolerate** the extraction. This is a notable observation about agentic-AI ecosystem culture: vendors tolerate third-party reverse-engineering at this scale.

---

## 7. Khi nào nên đọc? / When to read?

### 🇻🇳 Tiếng Việt

**Nên đọc nếu bạn:**
- Dùng Claude Code và muốn hiểu nó hành xử thế nào ở mức prompt
- Đang build skill / plugin cho Claude Code và cần ground-truth về format Anthropic dùng
- Đang nghiên cứu agentic-AI design patterns (đây là dataset chất lượng cao về agent system-prompt design)
- Muốn debug behavior lạ của Claude Code (check xem prompt nào đang active)
- Đang xem xét chuyển sang Piebald commercial OR dùng tweakcc

**KHÔNG cần đọc nếu bạn:**
- Chỉ dùng Claude Code làm tool và không quan tâm internals
- Đang tìm tool/plugin để CÀI (đây không phải installable)
- Đang tìm tutorial Claude Code (đây là REFERENCE, không phải tutorial)

### 🇬🇧 English

**Read this if you:**
- Use Claude Code and want to understand how it behaves at the prompt level
- Are building skill/plugin for Claude Code and need ground-truth on the format Anthropic uses
- Research agentic-AI design patterns (this is a high-quality dataset of agent system-prompt design)
- Want to debug strange Claude Code behavior (check which prompt is active)
- Are considering switching to Piebald commercial OR using tweakcc

**Don't need to read this if you:**
- Just use Claude Code as a tool and don't care about internals
- Are looking for a tool/plugin to INSTALL (this is not installable)
- Are looking for a Claude Code tutorial (this is REFERENCE, not tutorial)

---

## 8. Học gì từ Storm Bear vault wiki? / What does the Storm Bear vault wiki contribute?

### 🇻🇳 Tiếng Việt

Bài wiki v65 này đăng ký các **ngụ ý Pattern Library** quan trọng:

1. **Pattern #78 Living-Domain-Standards Tracking N=2 PROMOTION-ELIGIBLE tại v66 (accelerated) hoặc v67** — 78a multi-vendor (claude-seo v64) + 78b single-vendor-product-internals (v65) = N=2 cross-archetype với 2 sub-mechanisms riêng biệt
2. **Pattern #21 System Prompts Leaks N=2 strengthening tại corpus-record scale** — extension của v21 system-prompts-leaks N=1; v65 ở scale 10K stars với continuous-versioning (176 versions)
3. **Pattern #57 Recursive Corpus Reference 57c STRONGEST instance** — Claude Code = sản phẩm được cite nhiều nhất; v65 documenting internals = corpus-recursive ở độ sâu maximum
4. **Pattern #19 ecosystem-portfolio-builder N=4 strengthening tại corporate-org archetype** — Piebald-AI 4th archetype (corporate-org) sau 3 solo archetypes (gotalab/forrestchang/AgriciDaniel)
5. **Pattern #66 Supply Chain Awareness OT extension** — meta-supply-chain-awareness disclosure của Piebald-AI
6. **NEW Pattern candidate #79 Continuous-Reverse-Engineering Reference Archive N=1 stale-flagged** — 3 criteria: third-party + continuous-versioning + extraction-from-compiled-source

**Phase 0.9 STRICT 3-of-4 STRONG PASS = STRONGEST INCLUDE trong 10-instance window history.** Storm Bear meta-streak RESTARTS at 1 sau v64-RESET. Window post-v65 = 80% INCLUDE rate (8 PASS / 2 SKIP).

**Cross-pattern coupled-design N=5+ ở v65** — record corpus: 5 patterns + 1 NEW candidate cùng xuất hiện tại single wiki (sister observations: v60 N=4 + v54 3-pattern-triple).

### 🇬🇧 English

This v65 wiki registers important **Pattern Library implications:**

1. **Pattern #78 Living-Domain-Standards Tracking N=2 PROMOTION-ELIGIBLE at v66 (accelerated) or v67** — 78a multi-vendor (claude-seo v64) + 78b single-vendor-product-internals (v65) = N=2 cross-archetype with 2 distinct sub-mechanisms
2. **Pattern #21 System Prompts Leaks N=2 strengthening at corpus-record scale** — extension of v21 system-prompts-leaks N=1; v65 at 10K stars scale with continuous-versioning (176 versions)
3. **Pattern #57 Recursive Corpus Reference 57c STRONGEST instance** — Claude Code = most-cited product; v65 documenting internals = corpus-recursive at maximum depth
4. **Pattern #19 ecosystem-portfolio-builder N=4 strengthening at corporate-org archetype** — Piebald-AI 4th archetype (corporate-org) after 3 solo archetypes (gotalab/forrestchang/AgriciDaniel)
5. **Pattern #66 Supply Chain Awareness OT extension** — meta-supply-chain-awareness disclosure by Piebald-AI
6. **NEW Pattern candidate #79 Continuous-Reverse-Engineering Reference Archive N=1 stale-flagged** — 3 criteria: third-party + continuous-versioning + extraction-from-compiled-source

**Phase 0.9 STRICT 3-of-4 STRONG PASS = STRONGEST INCLUDE in 10-instance window history.** Storm Bear meta-streak RESTARTS at 1 after v64 RESET. Post-v65 window = 80% INCLUDE rate (8 PASS / 2 SKIP).

**Cross-pattern coupled-design N=5+ at v65** — corpus record: 5 patterns + 1 NEW candidate co-occurring at single wiki (sister observations: v60 N=4 + v54 3-pattern-triple).

---

## 9. Tài liệu tham khảo / Further reading

- **Project CLAUDE.md:** [../CLAUDE.md](../CLAUDE.md) — phân loại 12-axis + Phase 0.9 evidence + Pattern Library implications preview
- **Wiki index:** [../02 Wiki/index.md](../02%20Wiki/index.md)
- **Cluster 1 — README + 293-file inventory:** [../02 Wiki/cluster-1-readme-and-prompt-inventory.md](../02%20Wiki/cluster-1-readme-and-prompt-inventory.md)
- **Cluster 2 — Extraction methodology:** [../02 Wiki/cluster-2-extraction-methodology.md](../02%20Wiki/cluster-2-extraction-methodology.md)
- **Cluster 3 — CHANGELOG + Piebald-AI ecosystem:** [../02 Wiki/cluster-3-changelog-and-ecosystem.md](../02%20Wiki/cluster-3-changelog-and-ecosystem.md)
- **Entity 1 — archive core:** [../02 Wiki/entity-1-archive-core.md](../02%20Wiki/entity-1-archive-core.md)
- **Entity 2 — Pattern #78 N=2 PRIMARY deliverable:** [../02 Wiki/entity-2-pattern-78-n2-strengthening.md](../02%20Wiki/entity-2-pattern-78-n2-strengthening.md)
- **Entity 3 — Piebald-AI + Pattern #19 N=4 + Pattern #57 STRONGEST:** [../02 Wiki/entity-3-piebald-ai-and-ecosystem.md](../02%20Wiki/entity-3-piebald-ai-and-ecosystem.md)
- **Entity 4 — Storm Bear meta-entity (corpus-recursive max-depth):** [../02 Wiki/entity-4-storm-bear-meta.md](../02%20Wiki/entity-4-storm-bear-meta.md)

**External:**
- Repo gốc: https://github.com/Piebald-AI/claude-code-system-prompts
- Sister tool tweakcc: https://github.com/Piebald-AI/tweakcc
- Piebald commercial: https://piebald.ai/
- Piebald-AI X: https://x.com/PiebaldAI
- Mentioned in Awesome Claude Code: https://github.com/hesreallyhim/awesome-claude-code
- Anthropic Claude Code GitHub: https://github.com/anthropics/claude-code (issues + releases only)

---

> *Generated by Claude (Storm Bear vault, llm-wiki-routine-v2.1) on 2026-05-13 → 2026-05-14. Bilingual VN+EN.*
