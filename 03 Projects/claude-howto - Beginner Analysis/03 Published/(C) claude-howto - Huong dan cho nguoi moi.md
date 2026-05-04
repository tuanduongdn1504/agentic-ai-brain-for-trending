# (C) claude-howto — Hướng dẫn cho người mới / Beginner Guide

> **Wiki:** v32 claude-howto (Storm Bear corpus)
> **Ngày / Date:** 2026-04-22
> **Đối tượng / Audience:** VN developer / Scrum coach / Claude Code newcomer
> **Ngôn ngữ / Languages:** Tiếng Việt + English

---

## Phần 1. Đây là gì? / What is this?

**VN:** `luongnv89/claude-howto` là bộ tài liệu dạy Claude Code theo kiểu **"learn by copy-paste"** — gồm 10 module, 45 template sẵn dùng, và hệ thống quiz tự đánh giá. Mục tiêu: master Claude Code trong một cuối tuần (11-13 giờ).

**EN:** `luongnv89/claude-howto` is a **"Master Claude Code in a Weekend"** tutorial — 10 modules, 45 copy-paste templates, interactive self-assessment slash commands. Goal: Claude Code proficiency in 11-13 hours.

**Stats:** 28,186 stars | 3,445 forks | MIT | v2.1.112 (sync'd với Claude Code 2.1+) | Tác giả Luong Nguyen (Paris, France)

**Link:** https://github.com/luongnv89/claude-howto

---

## Phần 2. Tín hiệu nổi bật / Corpus-first signals

**VN:** 12 điểm mới so với 31 wiki Storm Bear trước đó:

**EN:** 12 corpus-first observations:

1. **Quiz tương tác slash command** — `/self-assessment` + `/lesson-quiz [topic]` ship cùng product (corpus-first)
2. **25 event type cho hooks** — taxonomy đầy đủ nhất trong corpus
3. **3 variant CLAUDE.md** — project / directory / personal (named file riêng cho mỗi scope)
4. **EPUB offline** — `uv run scripts/build_epub.py` (corpus-first)
5. **4 ngôn ngữ EN+VN+CN+Ukrainian** — Ukrainian lần đầu xuất hiện trong corpus
6. **Mermaid-syntax + build-epub pre-commit hooks** — CI cho tutorial (corpus-first)
7. **"Master Claude Code in a Weekend"** — khung thời gian cuối tuần cụ thể
8. **Boris Cherny citation** — lần đầu corpus trích dẫn Boris Cherny (creator của Claude Code)
9. **Folder # ≠ learning order** — folder theo alphabet, lộ trình theo độ khó
10. **pytest + Ruff + Bandit + mypy + Codecov** — stack CI đầy đủ cho tutorial repo
11. **Đồng bộ version với upstream Claude Code** (v2.1.112)
12. **2nd VN-authored T1** — sau codymaster v12; **1st VN-diaspora-authored** (Paris vs HCMC)

---

## Phần 3. Tier placement / Vị trí taxonomy

**VN:** T1 Agent-as-assistant — tier lớn nhất (10 entrant). Đồng tầng với:
- everything-claude-code v1 (affaan-m)
- Superpowers v2 (obra/Jesse Vincent)
- gstack v3 (Garry Tan YC)
- get-shit-done v5 (TÂCHES)
- BMAD-METHOD v11 (BMad LLC)
- **codymaster v12 (Tody Le — VN-in-VN peer trực tiếp)**
- spec-kit v17 (GitHub/Microsoft corporate)
- agency-agents v18 (msitarzewski Reddit-viral 82.9K)
- oh-my-claudecode v27 (Yeachan Heo — Korean analog)

**EN:** T1 Agent-as-assistant — largest tier (10 entrants). Shares tier with 9 prior wikis listed above.

**v32 milestone:** T1 now N=10 + VN-Regional-Archetype T1 at N=2 (codymaster + claude-howto; proposed Pattern #70).

---

## Phần 4. Cài đặt / Installation

**VN 5 phút khởi động:**

```bash
# 1. Clone repo
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy slash command đầu tiên
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Thử nó — trong Claude Code gõ:
# /optimize

# 4. Thiết lập project memory
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Cài skill
cp -r 03-skills/code-review ~/.claude/skills/
```

**EN 15-minute onboarding:**
- Step 1: `git clone`
- Step 2: Copy `.md` slash command into project `.claude/commands/`
- Step 3: Test `/optimize`
- Step 4: Copy `project-CLAUDE.md` → your `./CLAUDE.md`
- Step 5: Install first skill (`cp -r 03-skills/code-review ~/.claude/skills/`)

**Optional — Dev environment** (nếu bạn contribute):

```bash
# Python tooling (uv là package manager)
pip install uv && uv venv && source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt
uv pip install pre-commit && pre-commit install

# Node tooling cho content validation
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli
```

---

## Phần 5. 10 module — lộ trình / 10-module roadmap

**VN recommended learning order** (khác thứ tự folder — folder theo alphabet):

| Order | Module | Folder | Level | Thời gian |
|-------|--------|--------|-------|-----------|
| 1 | Slash Commands | `01-slash-commands/` | Beginner | 30 min |
| 2 | Memory | `02-memory/` | Beginner+ | 45 min |
| 3 | Checkpoints | `08-checkpoints/` | Intermediate | 45 min |
| 4 | CLI Basics | `10-cli/` | Beginner+ | 30 min |
| 5 | Skills | `03-skills/` | Intermediate | 1h |
| 6 | Hooks | `06-hooks/` | Intermediate | 1h |
| 7 | MCP | `05-mcp/` | Intermediate+ | 1h |
| 8 | Subagents | `04-subagents/` | Intermediate+ | 1.5h |
| 9 | Advanced Features | `09-advanced-features/` | Advanced | 2-3h |
| 10 | Plugins | `07-plugins/` | Advanced | 2h |

**Tổng:** 11-13h cuối tuần. Copy-paste template + Mermaid diagram + quiz mỗi module.

---

## Phần 6. Pattern mới / Key architectural choices

**VN — 5 thiết kế đáng chú ý:**

1. **Quiz slash command** — `/self-assessment` quét 10 chủ đề, cho bạn learning path cá nhân. `/lesson-quiz [topic]` kiểm tra gap sau mỗi module. **Đây là corpus-first** — chưa framework nào trong 31 wiki trước embed quiz làm slash command.

2. **3 scope CLAUDE.md** — dùng template khác nhau cho:
   - Project: `project-CLAUDE.md` → `./CLAUDE.md`
   - Directory: `directory-api-CLAUDE.md` → `./src/api/CLAUDE.md`
   - Personal: `personal-CLAUDE.md` → `~/.claude/CLAUDE.md`

3. **25 hook event** — 4 nhóm (Tool / Session / Task / Lifecycle). Nhiều nhất corpus.

4. **Mermaid diagram làm primary pedagogy** — mỗi module có flow diagram giải thích how-it-works. Pre-commit hook kiểm `mermaid-syntax` parse đúng.

5. **EPUB offline** — `uv run scripts/build_epub.py` tạo ebook đọc ngoại tuyến (đầu tiên corpus).

**EN — 5 notable design choices:**
1. Quiz-as-slash-command (corpus-first)
2. 3-scope CLAUDE.md variant system (named files)
3. 25-event hook taxonomy (most comprehensive)
4. Mermaid-primary visual pedagogy with CI validation
5. EPUB offline ebook pipeline

---

## Phần 7. So với corpus frameworks / vs other corpus frameworks

| Framework | Scale | Author | Focus |
|-----------|-------|--------|-------|
| **claude-howto v32** | **28K** | **Luong (VN Paris)** | **Pedagogy — 10 modules + quiz** |
| codymaster v12 | 38 | Tody Le (VN HCMC) | Product — 79 skills |
| ECC v1 | ~5K | affaan-m | Feature-framework |
| Superpowers v2 | ~8K | Jesse Vincent | Methodology + skills |
| spec-kit v17 | 89K | GitHub/Microsoft | SDD methodology |
| BMAD v11 | 45K | BMad LLC | BMM methodology |
| agency-agents v18 | 82.9K | msitarzewski | 144 personality agents |
| OMC v27 | 30K | Yeachan Heo (Korean) | Multi-runtime orchestration |

**claude-howto phù hợp khi:** muốn học Claude Code có cấu trúc (không skim docs); có cuối tuần đầu tư; thích Mermaid + template copy-paste.

**claude-howto KHÔNG phù hợp khi:** đã master Claude Code (dùng ECC hoặc Superpowers sâu hơn); muốn methodology cứng (dùng BMAD hoặc spec-kit); cần agent framework deploy-ready (dùng codymaster hoặc agency-agents).

---

## Phần 8. Ethical + supply-chain framing ✅

**VN:** Đánh giá rủi ro — **THẤP**:
- MIT license + free forever
- Tác giả có danh tính công khai (Luong Nguyen, Montimage Paris)
- Active maintenance (sync mỗi Claude Code release)
- CI đầy đủ (pytest + Ruff + Bandit + mypy)
- SECURITY.md 334 dòng với private-disclosure channel
- Không có perverse incentive (không có commercial tier ẩn; commercial products CUStats/TextWiz là menubar app riêng biệt)

**Lưu ý supply-chain (nhẹ):**
- Subagent + skill + hook template là **copy-paste vào `.claude/` của bạn** → nên review trước khi deploy (chuẩn tutorial caveat)
- Review đặc biệt hook scripts (`.sh`) vì chạy với quyền shell

**Dùng an toàn:** OK cho personal + team + enterprise (tuân thủ MIT attribution).

**EN:** Risk assessment — **LOW**. MIT + real named author + public identity + company affiliation + production-grade CI + explicit SECURITY.md. Minor caveat: review copy-paste templates before deploying (especially shell hook scripts that run with shell privileges). Safe for personal/team/enterprise use.

---

## Phần 9. Storm Bear relevance / VN operator fit

**VN:** **Rất cao** cho Storm Bear operator. Lý do:

1. **Tác giả VN-diaspora** (Luong Paris) — structural analog với operator VN-based → framing dễ cảm nhận
2. **VN README tồn tại** (dù chỉ 73 dòng) — courtesy port cho VN audience
3. **Pedagogy 10 module × 45 template** → self-onboarding operator với Claude Code trong 13h cuối tuần
4. **3-scope CLAUDE.md pattern** → có thể refactor root CLAUDE.md của Storm Bear (đang 150K dòng)
5. **Quiz mechanism** → inspire Storm Bear wiki-quality self-assessment
6. **`skills` sibling repo** (của cùng tác giả) → template cho skill library mở rộng

**So với codymaster v12:** claude-howto = **pedagogy**; codymaster = **product**. Hai mảng khác nhau. Operator có thể dùng cả hai:
- claude-howto: upgrade bản thân (self-onboarding)
- codymaster: reference VN-peer-framework (observational)

**Rank pilot tại v32:**
1. **claude-howto v32 🆕** — self-upgrade operator (13h cuối tuần)
2. spec-kit v17 (methodology)
3. OMC v27 (multi-runtime)
4. BMAD v11 (VN methodology)
5. markitdown v28 (Scrum doc ingestion)
6. crawl4ai v29 (web research)
7-11: gws / codymaster / multica / graphify / agency-agents

claude-howto ở rank #1 vì hoàn thành nó **cải thiện khả năng dùng TẤT CẢ pilot khác** — meta-ROI.

**EN:** **HIGH relevance** for Storm Bear operator (VN-based Claude Code user + Scrum coach). Self-onboarding pathway. Consider 3-scope CLAUDE.md refactor and quiz-mechanism-inspired vault-quality diagnostic.

---

## Phần 10. 4-tuần roadmap cho Storm Bear operator

**Week 1 (Level 1 Beginner — ~3h):**
- Run `/self-assessment` — baseline tại đâu?
- Module 1 Slash Commands + Module 2 Memory
- **Action:** Compare `02-memory/project-CLAUDE.md` với Storm Bear root CLAUDE.md (150K lines) — decide scope refactor

**Week 2 (Level 1B — ~3h):**
- Module 3 Checkpoints + Module 4 CLI Basics
- **Action:** Practice `/rewind` cho safe vault experimentation; practice `claude -p` cho automated wiki-lint

**Week 3 (Level 2 Intermediate — ~5h):**
- Module 5 Skills + Module 6 Hooks
- **Action:** Evaluate `code-review / brand-voice / doc-generator` skills → adapt 1 cho Storm Bear Scrum coaching

**Week 4 (Level 2B — ~5h):**
- Module 7 MCP + Module 8 Subagents
- **Action:** Evaluate MCP server cho Storm Bear (GitHub MCP? Obsidian MCP? DB MCP?); evaluate 5 subagents relevance

**Week 5+ (nếu cần Level 3):**
- Module 9 Advanced Features + Module 10 Plugins
- Planning Mode, Extended Thinking, Background Tasks, Permission Modes

---

## Phần 11. Tradeoffs + limitations

**VN:**
- ✅ Structure rõ + copy-paste sẵn dùng + quiz assessment + Mermaid diagrams
- ⚠️ VN README thin (73 dòng vs 878 EN) — VN user vẫn cần đọc EN primary
- ⚠️ Solo author bus factor (1 Luong maintain) — dù 642 followers + active PRs mitigate
- ⚠️ Pedagogy không thay thế hands-on (phải thực hành template, không chỉ đọc)
- ⚠️ Một số template dependency-locked vào Claude Code 2.1+ (upgrade risk nếu Claude Code thay đổi breaking)
- ⚠️ Testing infrastructure cho tutorial repo là overhead nếu bạn chỉ đọc

**EN:**
- Strong structure + copy-paste ready + interactive quizzes + Mermaid diagrams
- Caveats: thin VN port, solo author bus factor, Claude Code 2.1+ version lock, hands-on required for effective learning

---

## Phần 12. Caveats + safety notes

**VN (v2.1 routine emphasis on supply-chain awareness):**
- Copy-paste template → review trước khi deploy
- Shell hooks (`.sh`) chạy với quyền shell — cẩn thận escalation
- MCP server config (`.mcp.json`) thêm external tool — review env var + credentials
- Skill scripts có thể Python — review cho security (nhất là `doc-generator` với `generate-docs.py`)

**EN:**
- Template review mandatory before deploy
- Shell hook script shell privilege escalation risk
- MCP config credential management
- Python skill script security review

Tiêu chuẩn tutorial-genre supply-chain awareness. Không cao hơn corpus average.

---

## Phần 13. References + Next action

**Repo:** https://github.com/luongnv89/claude-howto
**Author Medium:** https://medium.com/@luongnv89
**VN README:** https://github.com/luongnv89/claude-howto/blob/main/vi/README.md
**Catalog:** https://github.com/luongnv89/claude-howto/blob/main/CATALOG.md
**Learning Roadmap:** https://github.com/luongnv89/claude-howto/blob/main/LEARNING-ROADMAP.md

**Storm Bear cross-references (Pattern Library):**
- [[(C) T1 10-way + VN-Regional-Archetype N=2 Pattern Test]] — Pattern #70 proposal
- [[(C) luongnv89 — VN-Diaspora Author + Ecosystem Portfolio]] — author analysis
- [[(C) 10-Module Pedagogy + Self-Assessment Quiz]] — core product entity
- [[(C) Storm Bear Vault — VN-Diaspora T1 Relevance]] — meta-entity
- **codymaster v12** — VN-in-VN peer (Tody Le)
- **ECC v1** — feature-framework structural peer

**Next action suggestion (Claude Code rule: always end with next action):**

→ **VN:** Start Week 1 của roadmap trên — clone repo + chạy `/self-assessment` + Module 1+2. Invest 3h cuối tuần này. Result: quantified baseline + 2 module đầu hoàn tất. Đánh dấu trong GOALS.md.

→ **EN:** Start Week 1 — clone repo + run `/self-assessment` + complete Module 1-2. Invest 3 weekend hours. Result: quantified baseline + 2 modules complete. Track in GOALS.md.

---

**(C) Generated 2026-04-22 by Storm Bear routine `llm-wiki-routine-v2.1.md` — first v2.1-era execution.**
