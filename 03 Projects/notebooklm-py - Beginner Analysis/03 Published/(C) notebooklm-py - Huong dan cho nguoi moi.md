# (C) notebooklm-py — Hướng dẫn cho người mới

> Target audience: Researchers, Scrum coaches, knowledge workers người Việt dùng Google NotebookLM và muốn tự động hoá via Python/CLI/Claude Code
> Reading time: ~35 min
> Language: Bilingual (VN primary, EN technical terms)
> Source: `teng-lin/notebooklm-py`

---

## Part 1 — notebooklm-py là gì

### 1.1 Giới thiệu 1 phút

**notebooklm-py** = **Python library + CLI + agent Skill** cho Google NotebookLM, unofficial nhưng cung cấp **features mà web UI không có**.

3 surfaces (cách dùng):
1. **Python API** — viết code tích hợp vào app
2. **CLI** — dùng terminal, script, cron job
3. **Agent Skill** — Claude Code / Codex tự động invoke

**Stats:** 11,043 stars, 1,466 forks, MIT license, v0.3.4 (active 1-2 tuần/release), Python 3.10-3.14.

**Author:** `teng-lin` (solo developer).

### 1.2 Tại sao cần, khi nào web UI không đủ?

Google NotebookLM có web interface nhưng **9 tính năng dưới đây chỉ có trong library:**

1. Batch downloads (tải hàng loạt artifacts)
2. Quiz/Flashcard export JSON/Markdown/HTML
3. Mind map JSON extraction
4. Slide deck PPTX (PowerPoint chỉnh sửa được)
5. Individual slide revision (sửa 1 slide cụ thể)
6. Report template customization (`--append` thêm hướng dẫn riêng)
7. Chat history lưu thành note
8. Source fulltext programmatic access
9. Programmatic sharing (auto-share không click)

**Nếu bạn chỉ dùng NotebookLM casual — web UI đủ.**
**Nếu bạn cần automation, export, team workflow — library cần thiết.**

### 1.3 Ai nên dùng?

**Rất phù hợp:**
- Researchers cần export artifacts để vào LMS/Obsidian/Notion
- Scrum coaches muốn retro → podcast pipeline
- Team leads cần batch-generate briefing reports
- AI agent operators (Claude Code users) muốn agent tự quản lý NotebookLM

**Ít phù hợp:**
- Casual user chỉ cần "hỏi tài liệu một vài câu" → web UI đủ
- Team không có NotebookLM paid plan
- Người không thoải mái với CLI / Python

**Mix phù hợp:**
- Cần 1 trong 9 tính năng exclusive

---

## Part 2 — Cài đặt và xác thực

### 2.1 Cài đặt

```bash
# Basic
pip install notebooklm-py

# Với browser auth (recommended cho dev)
pip install "notebooklm-py[browser]"
playwright install chromium

# Latest từ GitHub (nếu cần feature chưa release)
pip install git+https://github.com/teng-lin/notebooklm-py@main
```

**Yêu cầu:** Python 3.10+, có tài khoản Google NotebookLM (Standard / Plus / Pro / Ultra tùy nhu cầu).

### 2.2 Xác thực lần đầu

```bash
notebooklm login
# Mở browser → đăng nhập Google → cookies lưu vào ~/.config/notebooklm-py/
```

**Kiểm tra:**
```bash
notebooklm status              # Email đã login
notebooklm auth check --test   # Full diagnostic
notebooklm doctor              # Health check
```

### 2.3 Cho CI/CD hoặc server không browser

```bash
# Option 1: Env var với storage_state.json
export NOTEBOOKLM_AUTH_JSON='{"cookies":...}'

# Option 2: Profile-based
export NOTEBOOKLM_PROFILE=production

# Option 3: Custom config dir (cho isolation multi-agent)
export NOTEBOOKLM_HOME=/tmp/agent-$AGENT_ID
```

---

## Part 3 — 3 surfaces — dùng cái nào khi nào

### 3.1 CLI — cho quick tasks + scripts

**Khi dùng:**
- Ad-hoc research
- Shell script automation
- Cron jobs
- Claude Code invokes (via skill)

**Examples:**

```bash
# Workflow cơ bản: create → add → ask → generate → download
notebooklm create "Retro Q1 2026"               # create notebook
notebooklm source add https://retro.md -n <id>  # add source URL
notebooklm ask "Top blockers?" -n <id> --json   # chat query
notebooklm generate audio "Focus action items" -n <id> --wait
notebooklm download audio ./retro.mp3 -n <id>
```

### 3.2 Python API — cho application integration

**Khi dùng:**
- Python app cần embedded automation
- Complex workflow logic
- Parallel operations

**Example:**

```python
import asyncio
from notebooklm import NotebookLMClient

async def generate_retro_podcast(urls, output_path):
    async with await NotebookLMClient.from_storage() as client:
        nb = await client.notebooks.create("Retro Q1 2026")
        for url in urls:
            await client.sources.add_url(nb.id, url, wait=True)
        task = await client.artifacts.generate_audio(
            nb.id, "Focus on action items and blockers"
        )
        await client.artifacts.wait_for_completion(nb.id, task.task_id)
        await client.artifacts.download_audio(nb.id, output_path)

asyncio.run(generate_retro_podcast(
    ["https://retro1.md", "https://retro2.md"],
    "./q1-retro.mp3"
))
```

### 3.3 Agent Skill — cho Claude Code / Codex

**Khi dùng:**
- Agent tự động handle NotebookLM tasks
- User nói natural language → agent executes
- Zero-code integration

**Cài đặt skill:**
```bash
notebooklm skill install   # populates ~/.claude/skills/notebooklm
```

Bây giờ Claude Code hiểu NotebookLM. User nói:
> "Turn my Q1 retro notes into a podcast, focus on action items"

Claude Code:
1. Loads SKILL.md (26KB reference)
2. Executes CLI workflow tự động
3. Returns podcast path cho user

---

## Part 4 — 9 Web-UI-Exclusive Capabilities chi tiết

### 4.1 Batch downloads
```bash
notebooklm download audio --all
notebooklm download slide-deck --all
```
**Value:** Tải 10 artifacts trong 1 lệnh thay vì 10 clicks.

### 4.2 Quiz/Flashcard structured export
```bash
notebooklm generate quiz -n <id> --difficulty medium --wait
notebooklm download quiz ./quiz.json --format markdown
```
**Value:** JSON/MD/HTML output → import vào LMS, in flashcards, translate bulk.

### 4.3 Mind map JSON
```bash
notebooklm download mind-map ./map.json
```
**Value:** Import vào Obsidian / Miro / Mermaid.

### 4.4 Slide deck PPTX
```bash
notebooklm download slide-deck ./slides.pptx --format pptx
```
**Value:** Edit trong PowerPoint, add logo company, customize branding.

### 4.5 Individual slide revision
```bash
notebooklm generate revise-slide "Make slide 3 more concise" \
  --artifact <id> --slide 3 --wait
```
**Value:** Sửa 1 slide (30 sec) thay vì regenerate deck (15-20 min).

### 4.6 Report template customization
```bash
notebooklm generate report -n <id> \
  --format briefing-doc \
  --append "Include Q1 risk matrix in appendix"
```
**Value:** Reports theo format công ty thay vì generic templates.

### 4.7 Chat history persistence
```bash
notebooklm ask "Summarize sources" --save-as-note --note-title "Q1 Summary"
notebooklm history --save   # save entire conversation
```
**Value:** Q&A thành note vĩnh viễn trong notebook.

### 4.8 Source fulltext access
```bash
notebooklm source fulltext <src_id> --json
```
**Value:** Đọc full indexed text để verify/extract.

### 4.9 Programmatic sharing
```python
await client.sharing.set_sharing_state(nb_id, public=True)
```
**Value:** Tự động share trong CI/CD, batch permission updates.

---

## Part 5 — Storm Bear use cases cụ thể

### 5.1 Scrum retro → podcast pipeline

**Workflow:**
1. Meeting transcript (Zoom/Meet)
2. `notebooklm create "Retro Q1"`
3. `notebooklm source add transcript.md -n <id>`
4. `notebooklm generate audio "Focus on action items" -n <id> --format deep-dive --length long --wait`
5. `notebooklm download audio ./q1-retro-podcast.mp3 -n <id>`
6. Team listens on commute next morning

**Value for VN team:**
- Some team members prefer audio (đi làm xe máy)
- Retro đủ dài (45-90 min) cho deep-dive format
- Audio = natural for team retrospectives

### 5.2 Coaching research aggregation

**Workflow:**
1. Notebook với 20 sources (books + articles về Scrum/Agile)
2. `notebooklm source add-research "Vietnamese Scrum team challenges" --mode deep`
3. Generate comprehensive report với `--append "Focus on VN context"`
4. Export Markdown → import vào Storm Bear vault

### 5.3 Team knowledge quiz

**Workflow:**
1. Notebook với team playbook documents
2. `notebooklm generate quiz --difficulty medium --quantity more`
3. `notebooklm download quiz ./quiz.json --format html`
4. Send HTML to team Slack/email
5. Team self-assesses knowledge

### 5.4 Cross-wiki synthesis (Storm Bear vault)

**Workflow:**
1. Notebook với 7 beginner guides từ Storm Bear vault
2. Ask: "Compare feature framework, methodology framework, education, bridge: when use which?"
3. Save response as note
4. Add note to vault cross-reference

---

## Part 6 — So sánh với 6 siblings Storm Bear

### 6.1 Tier positioning

| Project | Tier | Purpose | Verb |
|---------|------|---------|------|
| **notebooklm-py** | **Tier 4 (NEW)** | **Bridge to external service** | **Integrate** |
| ECC | Tier 1 | Dev tool (Claude Code) | Use |
| Superpowers | Tier 1 | Methodology + TDD | Use |
| gstack | Tier 1 | Specialist roles | Use |
| GSD | Tier 1 | Context rot + 14 harnesses | Use |
| goclaw | Tier 2 | Multi-tenant platform | Deploy |
| ai-agents-for-beginners | Tier 3 | Learn concepts | Learn |

### 6.2 Relationship to each sibling

- **ECC/Superpowers/gstack/GSD** — notebooklm-py skill installable into all (Tier 1 tools adopt Tier 4 bridge)
- **goclaw** — could bundle notebooklm-py skill per-tenant (Tier 2 embeds Tier 4)
- **course** — Lesson 11 (MCP/Agentic Protocols) conceptually covers what Tier 4 bridges do

### 6.3 Not competing

notebooklm-py doesn't compete với Tier 1 tools. **Tier 1 agent installs Tier 4 skill.** Complementary.

---

## Part 7 — Autonomy rules (quan trọng với agent users)

### 7.1 Agent chạy tự động không cần hỏi

- `status`, `list`, `fulltext` (read-only)
- `login`, `auth check` (auth setup)
- `use`, `profile switch` (context)
- `ask` without `--save-as-note` (ephemeral)
- `source wait`, `artifact wait` (background waits)

### 7.2 Agent phải confirm trước khi

- `delete` (destructive)
- `generate *` (expensive + slow)
- `download` (writes disk)
- `ask --save-as-note`, `history --save` (persistence)

**Why:** Giới hạn cost, prevent accidental data loss, respect filesystem.

---

## Part 8 — Lộ trình 2-tuần / 2-week roadmap

### Week 1 — Setup + Solo use

- Day 1: Install + auth + test basic CRUD (`create`, `source add`, `ask`)
- Day 2-3: Try generate audio + download (first podcast!)
- Day 4-5: Try generate report + slide-deck + quiz (multi-artifact)
- Day 6-7: Explore `--json` outputs, write first shell script automation

**Deliverable:** 1 real use case shipped (podcast from real project research).

### Week 2 — Team + Agent integration

- Day 8-9: Install skill (`notebooklm skill install`) cho Claude Code
- Day 10-11: Test agent invocations ("create podcast about X")
- Day 12-13: Write Python wrapper cho team-specific workflow (e.g., retro pipeline)
- Day 14: Document in vault, share với team

**Deliverable:** Team-aware workflow (e.g., retro podcast pipeline live).

---

## Part 9 — Rủi ro và hạn chế

### 9.1 RPC fragility

Library dùng **undocumented Google APIs**. Google có thể break anytime:
- Method IDs change → requests fail
- Request format change → parsing fails
- Auth flow change → login fails

**Mitigation:**
- Pin version stable: `pip install "notebooklm-py==0.3.4"`
- Don't pin critical workflows; have fallback (manual web UI)
- Monitor maintainer's GitHub issues for breakage reports

### 9.2 Bus factor = 1

teng-lin là solo maintainer. Nếu maintainer dừng:
- RPC fragility không ai fix → library dies
- Community forks possible nhưng not guaranteed

**Mitigation:**
- Don't build mission-critical infra on this
- Have manual fallback workflow

### 9.3 Google NotebookLM paid plan

Library không cung cấp NotebookLM — bạn phải có Google account + plan.
- Standard 50 sources/notebook
- Plus 100
- Pro 300
- Ultra 600

**Mitigation:** Budget planning. Library doesn't add cost; Google does.

### 9.4 Rate limits

Google throttle:
- Audio/video generation: 10-20 min each, rate-limited
- Research (deep): 15-30 min, sequential
- Bulk generation → expect failures + retry

**Mitigation:** Queue requests, not parallel. Respect Google's pace.

### 9.5 Browser auth friction

Install `chromium` ~300 MB.
**Mitigation:** CI/CD: use `NOTEBOOKLM_AUTH_JSON` env var instead of browser.

---

## Part 10 — Tiếp theo nên làm gì

### 10.1 Sau 2-week roadmap

**Option 1 — Integrate into Storm Bear routine:**
Add optional Phase 4c: "Generate NotebookLM podcast from published guide." Opt-in per wiki.

**Option 2 — Deeper skill writing:**
Fork SKILL.md, customize cho Vietnamese Scrum coaching context. Contribute back as community skill variant.

**Option 3 — Advance to Tier 1 tool integration:**
Integrate với ECC workflow — Claude Code skill invokes notebooklm-py for research questions.

**Option 4 — Build team workflow:**
Automate weekly team retro podcast pipeline via cron + notebooklm-py.

### 10.2 Red flags

- **Hard-coding notebook IDs in version control** — token in repo = leak risk
- **Parallel agents, shared profile** — credential chaos
- **Storing MP3 artifacts in git** — binary bloat
- **Trusting auto-generated reports without review** — AI slop risk
- **Pinning critical business workflow** — RPC fragility = business risk

---

## Part 11 — Contribution opportunities

### 11.1 Cho Storm Bear vault

- ✅ **Wiki này = first comprehensive Tier 4 analysis** trong Storm Bear corpus
- Contribute lại upstream? — VN translation `README.vi.md` + SKILL.vi.md (unique VN offering)

### 11.2 Cho VN community

- Blog post "NotebookLM đầy đủ với notebooklm-py" — dev VN context
- Zalo group về NotebookLM automation? (parallel to goclaw's Zalo approach)
- YouTube tutorial "Retro → podcast workflow" in Vietnamese

### 11.3 Cho library upstream

- Vietnamese language testing (quality check cho Vietnamese content)
- Documentation PRs (add VN use case examples)
- Test report for VN NotebookLM content

---

## Tóm tắt / Summary

**notebooklm-py = unofficial Python API + CLI + Skill cho Google NotebookLM.** 9 web-UI-exclusive features unlock automation, export, agent integration. **First Tier 4 "bridge/connector" trong Storm Bear corpus.**

**Khi dùng:**
- Có NotebookLM paid plan + automation/export needs → adopt
- Chỉ dùng NotebookLM casual → web UI đủ

**Risk aware:**
- RPC fragility (undocumented APIs)
- Bus factor 1 (solo maintainer)
- Don't pin critical workflows

**Next:** Install skill, test 1 real use case (retro podcast?), evaluate integration into Storm Bear routine.

---

## Cross-references

- Main vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Wiki entities:
  - [[../02 Wiki/(C) CLI Surface]]
  - [[../02 Wiki/(C) Python API Architecture]]
  - [[../02 Wiki/(C) Skill Integration (Claude Code + Codex + OpenClaw)]]
  - [[../02 Wiki/(C) Web-UI-Exclusive Capabilities]]
- Siblings (Tier 1):
  - `../../Everything Claude Code - Beginner Analysis/03 Published/*`
  - `../../Superpowers - Beginner Analysis/03 Published/*`
  - `../../gstack - Beginner Analysis/03 Published/*`
  - `../../get-shit-done - Beginner Analysis/03 Published/*`
- Siblings (Tier 2):
  - `../../goclaw - Beginner Analysis/03 Published/*`
- Siblings (Tier 3):
  - `../../ai-agents-for-beginners - Beginner Analysis/03 Published/*`
- Taxonomy (v6 3-tier): `../../ai-agents-for-beginners - Beginner Analysis/03 Published/(C) Agent framework taxonomy v2 - 3 tier.md`
- Taxonomy (v7 4-tier, session này): [[(C) Agent framework taxonomy v3 - 4 tier with bridge]]
