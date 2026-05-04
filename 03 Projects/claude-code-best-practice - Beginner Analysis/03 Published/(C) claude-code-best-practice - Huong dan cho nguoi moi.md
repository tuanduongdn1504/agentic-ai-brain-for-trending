# claude-code-best-practice — Hướng dẫn cho người mới / Beginner's Guide

**Tác giả wiki / Wiki author:** Claude (Storm Bear vault v34 LLM Wiki)
**Ngày / Date:** 2026-04-23
**Dự án gốc / Source project:** `shanraisshan/claude-code-best-practice`
**Tagline:** *"from vibe coding to agentic engineering - practice makes claude perfect"*
**Người tạo dự án / Project creator:** Shayan Rais (Karachi, Pakistan) — Software Architect @disrupt.com, Claude Community Ambassador

---

## Part 1 — Đây là gì? / What is this?

### VN

`claude-code-best-practice` là repo GitHub **47,423 sao trong 6 tháng** bởi Shayan Rais (Pakistan), tổng hợp kiến thức cần thiết để master Claude Code — từ *"vibe coding"* (code cảm tính) đến *"agentic engineering"* (kỹ thuật agent có kỷ luật). Repo gồm **82 tip thực tế** trong 14 nhóm + **11 tính năng beta** của Claude Code đang được maintain live + **reference implementation** (Weather Orchestrator) kiến trúc Command → Agent → Skill + **bảng so sánh 10+ framework** khác trong hệ sinh thái Claude Code (bao gồm spec-kit / Everything Claude Code / Superpowers / BMAD / gstack — toàn bộ 5 framework này đều đã có trong Storm Bear corpus).

Đây là framework T1 Agent-as-assistant thứ **11** trong corpus Storm Bear, và là **framework đầu tiên do tác giả Pakistani viết** — đánh dấu mốc **Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern** (meta-pattern đăng ký bao gồm 3 vùng: Korean + VN + Pakistani).

### EN

`claude-code-best-practice` is a GitHub repo with **47,423 stars in 6 months** by Shayan Rais (Pakistan), aggregating essential knowledge for mastering Claude Code — from *"vibe coding"* to *"agentic engineering"*. Contents: **82 practical tips** across 14 categories + **11 Claude Code beta features** tracked live + **reference implementation** (Weather Orchestrator) of Command → Agent → Skill architecture + **comparison table of 10+ frameworks** in the Claude Code ecosystem (including 5 Storm Bear corpus T1 wikis: spec-kit / ECC / Superpowers / BMAD / gstack).

This is the **11th T1 entrant** in Storm Bear corpus and the **1st Pakistani-authored framework** — triggering registration of **Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern** (wrapping 3 regions: Korean + VN + Pakistani).

---

## Part 2 — Tại sao Storm Bear operator nên quan tâm? / Why should Storm Bear operator care?

**Rank #4 pilot candidate** tại v34 (sau spec-kit / claude-howto / OMC).

### Lý do chính / Main reasons

1. **82 tips trực tiếp áp dụng được cho vault CLAUDE.md refactor** — đặc biệt tip "CLAUDE.md dưới 200 dòng, lý tưởng 60 dòng" (vault root CLAUDE.md hiện đang 150K+ dòng — v32 đã flag cần refactor)
2. **Weather Orchestrator** = reference implementation chạy được — copy-adapt thành Scrum-coach-agent prototype
3. **Anthropic Community Ambassador endorsement** = credibility cho client pitch (VN Scrum coach cần signal Anthropic ecosystem alignment)
4. **Pakistani regional peer** = validation rằng non-Anglo T1 at 47K stars là khả thi (sau VN-diaspora claude-howto v32 28K + Korean OMC v27 30K)
5. **Development Workflows table** = external validation của Storm Bear corpus T1 (5/5 overlap = 100%)
6. **Boris Cherny + Dex Horthy + Cat Wu video library** = onboarding path cho Claude Code engineering insights

### Hạn chế / Caveats

- EN-only (không VN — claude-howto v32 vẫn phù hợp hơn cho VN audience)
- Solo bus factor (1 maintainer ở 47K sao = sustainability concern)
- Không có AGENTS.md (Pattern #22 gap cho enterprise adoption)
- Primary language = HTML (không chuẩn cho markdown-vault context)

---

## Part 3 — Corpus-first signals (10 observations)

1. **1st Pakistani-authored framework** ở bất kỳ tier nào trong corpus
2. **1st Claude Community Ambassador** được nhắc explicitly trong corpus
3. **1st Claude for OSS + Claude Certified Architect** badges explicit
4. **Live-delta tracker** function tại T1 — không T1 nào khác làm live release-monitor
5. **Development Workflows comparison table** — meta-reference cho 10+ framework within a framework
6. **Startups/Businesses Displaced table** — commercial-ecosystem-impact-tracking corpus-first
7. **"Billion-Dollar Questions" framing** — research questions dưới góc commercial-value-pending
8. **Cross-runtime best-practice sibling repo** (claude-code + codex-cli với same naming convention)
9. **Broadest multi-channel content distribution** at T1 (5+ channels: Reddit + YouTube + Medium + SO + LinkedIn)
10. **HTML primary language at T1** — 10 của 11 T1 wikis là TS/Python/Shell/JS primary

---

## Part 4 — Cài đặt + sử dụng / Installation + usage

### VN

```bash
# Clone repo (không có package manager; framework này là reference, clone + đọc)
git clone https://github.com/shanraisshan/claude-code-best-practice
cd claude-code-best-practice

# Đọc README như một khóa học (shanraisshan's own recommendation)
open README.md

# Thử flagship reference implementation
claude
/weather-orchestrator
```

**Không có `npm install` hay `pip install`** — repo là knowledge base, không phải package. Đọc thứ tự khuyến nghị:
1. README.md (tổng quan)
2. CONCEPTS table (15+ Claude Code features)
3. Weather Orchestrator code trong `.claude/`
4. 82 tips trong `tips/`
5. Technical reports trong `reports/`

### EN

```bash
git clone https://github.com/shanraisshan/claude-code-best-practice
cd claude-code-best-practice

open README.md

claude
/weather-orchestrator
```

No package installation — the repo IS the reference. Read in order: README → CONCEPTS → Weather Orchestrator code → 82 tips → Reports.

### Điều kiện tiên quyết / Prerequisites

- Claude Code CLI đã install (v2.1+ recommended to match shanraisshan's v2.1.116 sync)
- Git
- (Optional) Node.js — cho 3 MCP servers (playwright / context7 / deepwiki) tự invoke qua `npx`

---

## Part 5 — Command → Agent → Skill pattern (core architecture)

### VN

Kiến trúc reference của repo:

```
User → slash command (.claude/commands/<tên>.md)
      → invokes agent (.claude/agents/<tên>.md)
      → agent orchestrates skills (.claude/skills/<tên>/SKILL.md)
      → writes memory (.claude/agent-memory/<agent-name>/)
```

**Ví dụ Weather Orchestrator:**
```
User chạy: claude
User gõ: /weather-orchestrator
File .claude/commands/weather-orchestrator.md load
→ Triggers .claude/agents/weather-agent.md
→ Agent invoke các skill trong .claude/skills/weather/
→ Agent lưu memory vào .claude/agent-memory/weather-agent/
```

Mục đích: **demo trực quan** về Command → Agent → Skill + per-agent memory. Domain weather là toy (không quan trọng); quan trọng là pattern.

**Nguyên tắc quan trọng (từ CLAUDE.md của repo):** Subagent KHÔNG gọi lẫn nhau qua bash — phải dùng `Agent(subagent_type="...", prompt="...")` tool.

### EN

Reference architecture:
```
User → slash command (.claude/commands/<name>.md)
      → invokes agent (.claude/agents/<name>.md)
      → agent orchestrates skills (.claude/skills/<name>/SKILL.md)
      → writes memory (.claude/agent-memory/<agent-name>/)
```

Weather Orchestrator = runnable pedagogical demo. Toy domain chosen deliberately so the pattern stands out.

Important rule from repo's CLAUDE.md: Subagents cannot call each other via bash — use `Agent(subagent_type="...", prompt="...")` tool only.

---

## Part 6 — 82 Tips — top 10 cho Storm Bear operator / top 10 for Storm Bear operator

Trong 82 tips, đây là 10 tip có ROI cao nhất cho vault refactor:

| # | Tip | Storm Bear action |
|---|-----|-------------------|
| 1 | CLAUDE.md < 200 lines (60 ideal) | Refactor root CLAUDE.md (hiện 150K+ lines) |
| 2 | Auto-load `.claude/rules/*.md` via paths: YAML | Tạo rules subfolder với lazy-load glob |
| 3 | `<important if="...">` conditional rules | Wrap wiki-maintenance vs project rules |
| 4 | Multiple CLAUDE.md (ancestor/descendant cascade) | Validate project-level CLAUDE.md cascade |
| 5 | `/compact` at ~50% context | Document practice cho operator routine |
| 6 | `/rewind` (Esc Esc) over corrections | Document practice |
| 7 | `context: fork` in skills | Isolate skill execution cho long context |
| 8 | Skill descriptions as triggers, not summaries | Audit Storm Bear 5 skills trong `05 Skills/` |
| 9 | Keep PRs small (p50: 118 lines) + squash merge | Convention cho vault collaboration future |
| 10 | Auto Mode over `dangerously-skip-permissions` | Switch operator default |

---

## Part 7 — So sánh với framework khác trong corpus / vs other corpus frameworks

### Shayan's Development Workflows table (live counts per April 2026)

| Framework | Stars (per v34) | Agents | Commands | Skills | Methodology |
|-----------|----------------|--------|----------|--------|-------------|
| Everything Claude Code | 160K | 48 | 143 | 230 | Instinct scoring + AgentShield |
| Superpowers | 159K | 5 | 3 | 14 | TDD-first + Iron Laws |
| **claude-code-best-practice** (this wiki) | **47.4K** | **ref impl** | **ref impl** | **ref impl** | **82 tips + reference pattern** |
| Spec Kit | 89K | 0 | 9+ | 0 | Spec-driven + 9-article constitution |
| gstack | 76K | 0 | 0 | 37 | Role personas + /codex review |
| Get Shit Done | 55K | 33 | 122 | 0 | Fresh contexts + wave execution |

**⚠️ Fact-verification note:** Star counts reflect April 2026 live-API pull (shanraisshan's automation). Storm Bear wikis reflect counts at initial wiki build. Don't cross-quote without re-verification.

### Storm Bear corpus perspective

- **vs ECC / Superpowers:** ECC+SP = encyclopedia-style framework libraries. claude-code-best-practice = curated-practice tutorial + reference impl. Different role (encyclopedia vs guide).
- **vs spec-kit:** spec-kit = SDD methodology with 9-article constitution (heavy discipline). claude-code-best-practice = pattern-by-example (lighter, progression-oriented).
- **vs gstack:** gstack = role-persona approach. claude-code-best-practice = architecture-pattern approach + best-practices-catalog. Complementary.
- **vs claude-howto v32:** Both pedagogical T1 + multi-channel. Luong is VN-diaspora bilingual + tutorial repo with EPUB + CI discipline. Shayan is Pakistani EN-only + tip-dense catalog + live-tracker. Different pedagogical styles.
- **vs OMC v27:** OMC = multi-runtime orchestration (Claude + Codex + Gemini + Cursor). claude-code-best-practice = Claude-Code-primary + Codex-sibling-repo. Different scale of multi-runtime integration.
- **vs BMAD v11:** BMAD = Breakthrough Method for Agile AI-Driven Development (SCRUM-oriented methodology). claude-code-best-practice = Claude-Code-implementation-pattern-oriented. BMAD closer to operator's Scrum Coach role.

---

## Part 8 — Ethical framing / considerations

### VN

Không có vấn đề đạo đức lớn. Framework MIT license, tác giả danh tính công khai, Anthropic-ambassador endorsement. **Cân nhắc đơn giản:**

1. **Solo bus-factor ở 47K sao** — nếu Shayan dừng maintain, repo có thể stale nhanh (4 contributors total, 3 người khác chỉ 1 commit mỗi). Fork backup có thể nên cân nhắc nếu operator phụ thuộc nhiều.
2. **HTML primary language** không chuẩn cho T1 — kiểm tra kỹ repo structure trước khi adapt cho Storm Bear context.
3. **Development Workflows table bias** — shanraisshan chọn framework vào bảng theo star count + agent/command/skill axis. Frameworks không match cleanly 3 axes có thể bị underweighted. Đừng coi là ground truth.

### EN

No significant ethical concerns. MIT + identified author + Anthropic endorsement. Simple considerations:

1. **Solo bus-factor** at 47K stars — fork backup advisable if heavily depended upon
2. **HTML primary language** unusual at T1 — verify repo structure before adapting
3. **Development Workflows table bias** — framework selection via star-count + 3-axis analysis may undercount alternative methodologies; don't treat as ground truth

---

## Part 9 — Storm Bear operator relevance (chi tiết / detailed)

### Pakistani regional context

Shayan = Pakistani solo T1 @ 47K stars, 6 months. Cấu trúc gần với:
- **codymaster v12 Tody Le** (VN solo T1 @ 38 stars — smallest T1, nhưng same role-profile: solo, non-Anglo, regional)
- **claude-howto v32 Luong NGUYEN** (VN-diaspora solo T1 @ 28K stars, French-based)
- **OMC v27 Yeachan Heo** (Korean solo T1 @ 30K, Seoul-based)

**Lesson cho Storm Bear operator:** non-Anglo T1 có thể đạt 28-47K stars qua multi-channel content + Anthropic-alignment. Shayan + Luong demo 2 versions:
- Shayan: EN-only + 5+ channels + Anthropic-ambassador + Pakistani local
- Luong: 4-language + 4 channels + no-ambassador + VN-diaspora

Storm Bear operator (VN Scrum coach) có 3 template:
- **Shayan-style:** EN-only + international reach + Anthropic endorsement pursuit
- **Luong-style:** VN+EN bilingual + VN-diaspora positioning + multi-channel
- **Tody-style:** VN-primary + Vietnamese-audience-first + regional deep focus

### 82-tip vault refactor adoption pathway

**Week 1:** Read all 82 tips + identify top 10 actionable (estimated 2-3h)
**Week 2:** Refactor root CLAUDE.md from 150K+ lines to ~200 lines + extract rules to `.claude/rules/*.md` (4-6h)
**Week 3:** Test cascade (ancestor/descendant) + `<important if>` conditional rules (2-3h)
**Week 4:** Audit Storm Bear's 5 existing skills against "triggers not summaries" + `context: fork` best practice (2-3h)

**Total effort:** ~10-15 hours across 4 weeks = 1 session/week. **Single-session-executable alternative:** Week 2 alone = v27 diagnostic HIGH bundle item #1 execution.

---

## Part 10 — 4-week learning roadmap / lộ trình học 4 tuần

### Tuần 1: Đọc + chạy / Read + run (3h)

- Clone repo
- Đọc README full (~45 min)
- Chạy `/weather-orchestrator` trong Claude Code (~15 min)
- Đọc CLAUDE.md của repo (~15 min)
- Đọc 10 tips "CLAUDE.md + Rules" category (~30 min)
- Note 5 tip muốn thử trong 3 tuần tiếp

### Tuần 2: CLAUDE.md refactor cho Storm Bear vault (5h)

- Refactor root CLAUDE.md 150K+ lines → ~200 lines
- Extract nội dung ra `.claude/rules/*.md`
- Test cascade với project-level CLAUDE.md
- Document quy trình

### Tuần 3: Weather Orchestrator adapt cho Scrum Coach prototype (4h)

- Copy `.claude/commands/weather-orchestrator.md` → `.claude/commands/scrum-coach-orchestrator.md`
- Modify agent + skills cho Scrum domain
- Test cơ bản (sprint-planning / retro / DOR-DOD / user-story-split)

### Tuần 4: Review + contribute (3h)

- Submit PR cho shanraisshan's Development Workflows table (nếu có framework mới Storm Bear-sourced)
- Evaluate Anthropic Community Ambassador application
- Document Storm Bear-specific customizations

**Total: ~15h across 4 tuần.**

---

## Part 11 — Tradeoffs + limitations

### Strengths

- 82 tips high-signal-density
- Weather Orchestrator = runnable learning artifact
- Anthropic-team-alignment credibility
- Live-delta tracker function
- 5-layer settings cascade corpus-most-detailed documentation

### Weaknesses

- EN-only (no VN localization; no other language)
- HTML primary language unusual (no clear Jekyll config)
- No AGENTS.md (Pattern #22 gap)
- No SECURITY.md (contrast claude-howto 334 lines)
- Solo bus-factor
- 16 open issues (very low for 47K stars — may indicate selective triage or rapid-close)

### Differentiators

- Reference implementation + knowledge aggregator dual-role
- Anthropic-ambassador endorsement (solo T1 exclusive in corpus)
- 82-tip density
- Pakistani regional origin (corpus-first)
- 6-parallel-update-workflow maintenance infrastructure

---

## Part 12 — Next actions

### Ngay lập tức / Immediate (Week 1)

1. Clone repo + read README
2. Chạy Weather Orchestrator
3. Extract 10 high-ROI tips cho vault refactor planning

### Ngắn hạn / Short-term (Week 2-4)

4. Execute vault CLAUDE.md refactor (v27 diagnostic HIGH item #1)
5. Adopt rules subfolder pattern (v27 diagnostic HIGH item #2)
6. Test 3-scope CLAUDE.md cascade (per v32 claude-howto + v34 integration)

### Trung hạn / Mid-term

7. Evaluate Anthropic Community Ambassador application
8. Consider creating `claude-code-best-practice-vn` VN-translation fork (analog to BMAD VN fork)
9. Contribute Storm Bear-sourced observations to Development Workflows table

### Dài hạn / Long-term

10. Develop Scrum-coach-agent prototype using Weather Orchestrator pattern
11. Multi-channel content distribution strategy (Medium + YouTube + LinkedIn) for eventual Storm Bear public release

---

## Part 13 — References + next wiki

### Sources

- Repo: https://github.com/shanraisshan/claude-code-best-practice
- README (main branch): https://raw.githubusercontent.com/shanraisshan/claude-code-best-practice/main/README.md
- Author profile: https://github.com/shanraisshan
- LinkedIn: https://linkedin.com/in/shanraisshan
- Sibling repo (cross-runtime): https://github.com/shanraisshan/codex-cli-best-practice
- Sibling repo (hooks): https://github.com/shanraisshan/claude-code-hooks

### Storm Bear corpus cross-references

- `../claude-howto - Beginner Analysis/` (v32) — VN-diaspora T1 peer
- `../oh-my-claudecode - Beginner Analysis/` (v27) — Korean T1 peer
- `../codymaster - Beginner Analysis/` (v12) — VN-in-VN T1 peer
- `../Everything Claude Code - Beginner Analysis/` (v1) — US T1 peer listed in v34
- `../Superpowers - Beginner Analysis/` (v2) — US T1 peer listed in v34
- `../spec-kit - Beginner Analysis/` (v17) — Corporate T1 peer listed in v34
- `../get-shit-done - Beginner Analysis/` (v5) — US T1 peer listed in v34
- `../gstack - Beginner Analysis/` (v3) — US T1 peer listed in v34
- `../BMAD-METHOD - Beginner Analysis/` (v11) — Corporate-methodology T1 peer listed in v34
- `../agency-agents - Beginner Analysis/` (v18) — Community-viral T1 peer

### Pattern Library references

- Pattern #17 Ecosystem-Layer Organizations (CONFIRMED v15) — 11th data point
- Pattern #19 Intellectual Lineage Archetypes (CONFIRMED v20) — Boris Cherny 4th touchpoint
- Pattern #20 Solo-Scale Ceiling (CONFIRMED refined v21) — new row
- Pattern #22 AGENTS.md (CONFIRMED) — T1 solo abstention continues
- Pattern #27 Community-Viral Scale Path (CONFIRMED v21) — 11th data point
- Pattern #51 Vibe-Coding Spectrum (CONFIRMED v29 audit) — progression-framing observation
- **Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern (NEW at v34)** — consolidation-forward; promotion-ready at next mini-audit

---

*(C) Claude-generated 2026-04-23 per routine v2.1 Phase 4a. 34th LLM Wiki in Storm Bear corpus.*
