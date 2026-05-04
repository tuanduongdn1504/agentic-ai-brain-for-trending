# (C) deer-flow — Hướng dẫn cho người mới

> Target audience: Developers / team lead VN muốn deploy autonomous agent runs long tasks (researcher, Scrum coach automating retro synthesis, product team generating weekly briefing)
> Reading time: ~35 min
> Language: Bilingual (VN primary, EN technical terms)
> Source: `bytedance/deer-flow` (62K stars, ByteDance, v2.0)

---

## Part 1 — deer-flow là gì?

### 1.1 Giới thiệu 1 phút

**deer-flow = open-source SuperAgent harness.** ByteDance authored (parent company TikTok). 62,505 stars, MIT license. **v2.0 = complete rebuild** from v1 (Feb 2026), reached #1 GitHub Trending.

**Khác biệt vs Claude Code:**

| Claude Code (T1) | deer-flow (T5) |
|------------------|----------------|
| Interactive session | Autonomous long tasks |
| Minutes | Hours |
| User drives | Agent autonomous |
| Plugin in IDE | Standalone app (frontend + backend) |
| Single conversation | Multi sub-agent fan-out |

**Positioning:** "Runs tasks minutes-to-hours. Researches, codes, creates. Handles real workflows (data pipelines, presentations, deep research) that conversations can't."

### 1.2 Architecture 5 components

1. **Sandbox** — isolated execution (Docker hoặc filesystem)
2. **Memory** — persistent cross-session
3. **Skills** — Markdown-based, progressive loading
4. **Sub-agents** — parallel fan-out với isolated context
5. **Message Gateway** — Telegram/Slack/Feishu/WeChat/WeCom

### 1.3 Đặt trong Storm Bear ecosystem (v9 5-tier taxonomy)

| Tier | Frameworks | Purpose | Verb |
|------|-----------|---------|------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD | Use in Claude Code | Use |
| T2: Agent-as-service | goclaw | Multi-tenant platform | Deploy |
| T3: Agent-as-education | course | Learn concepts | Learn |
| T4: Agent-as-bridge | notebooklm-py | Integrate external | Integrate |
| **T5: Agent-as-application** (NEW) | **deer-flow** | **Standalone autonomous** | **Run** |

→ **First T5 entrant.** Distinct category.

### 1.4 Ai nên dùng?

**Rất phù hợp:**
- Researcher cần multi-hour deep research
- Team lead generate weekly report automation
- Product manager cần competitive analysis auto-run
- Scrum coach synthesize 10 retro transcripts into team-health report
- Developer automate content pipelines (blog posts + slides + audio)

**Ít phù hợp:**
- Interactive coding tasks (Claude Code T1 better)
- Multi-tenant SaaS (goclaw T2 better)
- Learning agent concepts (course T3 better)
- Single external service integration (notebooklm-py T4 style better)
- Solo dev without time to deploy (install complex)

**Mix phù hợp:**
- Team cần cả T1 (interactive) và T5 (autonomous) workflows

---

## Part 2 — Cài đặt

### 2.1 Prerequisites

**Option A: Docker (recommended)**
- Docker Desktop installed
- 16+ GB RAM laptop realistic
- 10+ GB free disk

**Option B: Local dev**
- Node.js 22+
- pnpm
- uv (Python package manager)
- nginx

### 2.2 Install steps

```bash
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow

# Copy config template
cp config.example.yaml config.yaml

# Edit config.yaml: add at least 1 LLM model + API key
# Example:
# models:
#   - name: gpt-4
#     provider: openai
#     api_key_env: OPENAI_API_KEY
#     base_url: https://api.openai.com/v1

# Set API key
export OPENAI_API_KEY="your-key-here"

# Run wizard
make setup

# Start services
make docker-init     # or `make check && make install` for local
make docker-start    # or `make dev` for local

# Open browser: http://localhost:2026
```

### 2.3 Verify working

- Browser opens to deer-flow web UI
- Can submit test task ("What's 2+2?")
- Task completes successfully
- Memory tab shows saved preferences

### 2.4 Common issues

- **Port conflict:** 2026/3000/8001/2024 may collide with other apps; stop other services or remap
- **Missing deps:** `make check` reports missing tools
- **Config errors:** `config.yaml` requires at least 1 model entry
- **API key missing:** env var `$OPENAI_API_KEY` must be set

---

## Part 3 — First workflows

### 3.1 Workflow: Deep research report

```
Task: "Research Vietnamese Scrum adoption trends 2024-2026, write structured report with sources"

deer-flow flow:
1. Lead agent decomposes into: [research] + [report writing]
2. Sub-agent A: web search, gather 10+ sources
3. Sub-agent B: synthesize, write report với citations
4. Lead: merge, output PDF

Duration: 20-45 min
Cost: ~$0.50-2 LLM spend (GPT-4 class)
Output: `workspace/reports/vietnamese-scrum-research.pdf`
```

### 3.2 Workflow: Multi-format content pipeline

```
Task: "Take this research report, make presentation + blog post + audio summary"

deer-flow flow:
1. Lead decomposes: [slides] + [blog] + [audio]
2. Sub-agent A: generate slides (PPTX)
3. Sub-agent B: write blog post (Markdown)
4. Sub-agent C: generate audio (TTS)
5. Lead: package deliverables

Parallel execution. Duration: 15-30 min.
```

### 3.3 Workflow: Scrum retro synthesis (Storm Bear example)

```
Task: "Analyze these 10 Scrum retro transcripts, generate team-health report + action items"

deer-flow flow:
1. Lead: upload transcripts to sandbox
2. Sub-agent A: thematic analysis
3. Sub-agent B: sentiment detection
4. Sub-agent C: action item extraction
5. Lead: synthesize team-health report

Perfect Storm Bear use case.
```

---

## Part 4 — Skills system deep dive

### 4.1 Built-in skills

- **Research:** multi-angle deep research
- **Report generation:** structured với visuals
- **Slide creation:** presentations
- **Web operations:** content creation/modification
- **Code execution:** sandbox code runs
- **File operations:** workspace management
- **Image/video:** generation + analysis

### 4.2 Progressive loading

Skills **không** all load at once. deer-flow only loads skills needed cho current task.

**Why:** Context window conservation. 100k+ token windows still have limits. Long tasks use lots of context for intermediate work.

### 4.3 Custom skills

```bash
# Create custom skill
cat > skills/custom/my-scrum-skill.md << 'EOF'
# Scrum Retro Synthesis

## Description
Analyze Scrum retro transcripts, extract themes, generate team-health reports

## Invocation
- "synthesize retro"
- "team health from retros"

## Process
1. Read all transcripts in sandbox/retros/
2. Identify recurring themes (at least 3)
3. Detect sentiment shifts
4. Extract action items
5. Generate report in sandbox/reports/team-health.md
EOF

# Restart to load
make docker-restart
```

### 4.4 Compared to Storm Bear vault skills

Storm Bear có 5 skills trong `05 Skills/` folder. deer-flow skills in `skills/` folder. **Same Markdown pattern.** Potential porting possible.

---

## Part 5 — Multi-channel gateway

### 5.1 5 platforms supported

- **Telegram** — global users
- **Slack** — Western teams
- **Feishu** — ByteDance/China enterprise
- **WeChat** — China personal + business
- **WeCom** — China corporate

### 5.2 Missing: Zalo

Vietnamese market không có support ra-of-box. Contribution opportunity.

### 5.3 How to configure

```yaml
# config.yaml
gateway:
  telegram:
    bot_token: $TELEGRAM_BOT_TOKEN
    allowed_users: [123456789]
  slack:
    bot_token: $SLACK_BOT_TOKEN
    workspace_id: T01ABC123
```

### 5.4 Submitting task via Telegram

```
You → @YourDeerFlowBot:
"research competitor X product launches, deliver summary"

DeerFlowBot → You (30 min later):
"Task complete. Report: [link] Duration: 28 min. Tokens: 12K."
```

---

## Part 6 — So sánh với 8 siblings

### 6.1 Positioning matrix

| Project | Tier | Verb | Duration | Best for |
|---------|------|------|----------|----------|
| **deer-flow** | **T5** | **Run** | **Minutes-hours** | **Autonomous long tasks** |
| ECC | T1 | Use | Interactive | Claude Code daily |
| Superpowers | T1 | Use | Interactive | Methodology + TDD |
| gstack | T1 | Use | Interactive | Specialist roles |
| GSD | T1 | Use | Interactive | Context rot + 14 harnesses |
| goclaw | T2 | Deploy | Platform ops | Multi-tenant service |
| course | T3 | Learn | Curriculum-paced | Understand concepts |
| notebooklm-py | T4 | Integrate | Per-call | NotebookLM automation |
| build-your-own-x | outside | Study | Open-ended | Programming fundamentals |

### 6.2 Complementary với Claude Code

README explicit: **"DeerFlow can invoke Claude Code via OAuth, and Claude Code can interact with DeerFlow through the `claude-to-deerflow` skill."**

Practical setup:
- **Morning:** Claude Code (T1) for interactive coding
- **Afternoon:** deer-flow (T5) for async long tasks
- **Evening:** Claude Code review deer-flow outputs

**Not either/or. Both.**

### 6.3 Devin alternative

Cognition's Devin = closed commercial. deer-flow = open MIT OSS alternative.

Feature overlap:
- Both autonomous agents
- Both handle long-horizon
- Both orchestrate sub-agents
- deer-flow adds IM gateway

Differences:
- Devin = SaaS, pay per task
- deer-flow = self-hosted, pay for LLM only

---

## Part 7 — Storm Bear use cases cụ thể

### 7.1 Scrum retro synthesis pipeline

**Setup:**
- deer-flow on team infrastructure
- Custom skill: `retro-synthesis.md`
- Slack integration

**Workflow:**
```
Coach → Slack @deer-flow:
"Synthesize last 4 sprint retros. Team health + top 3 action items."

30 min later deer-flow posts:
- Team health score + sentiment analysis
- Top 3 action items với owner suggestions
- 3-month trend comparison
```

**Value:** Saves coach 2-3 hours/month synthesis work. Reproducible process. Shareable với team.

### 7.2 Weekly coaching briefing

```
Every Monday 8 AM, deer-flow runs:
- Pull last week's team metrics
- Analyze retrospective themes
- Generate briefing for coach's Monday meeting

Delivered via email + Slack.
```

### 7.3 Client research pre-coaching

```
Coach takes on new client. Task: "Research industry X, prepare briefing."

deer-flow runs 45 min:
- Industry overview
- Common Scrum challenges in industry X
- Recent case studies
- Output: 15-page briefing PDF
```

### 7.4 Vault meta-use

deer-flow could run Storm Bear's LLM Wiki routine:
- Submit URL via Slack
- deer-flow runs 7-phase routine autonomously
- Wiki output delivered via Slack link

**Potential 10th wiki use case.**

---

## Part 8 — Lộ trình 2-tuần / 2-week roadmap

### Week 1: Install + first use

- Day 1: Install Docker + clone repo + config
- Day 2: Submit first task via web UI
- Day 3-4: Try 3 built-in skills (research, report, slides)
- Day 5-7: Submit 5 real tasks, observe quality + cost + time

**Deliverable:** 5 real outputs, feel for cost/quality trade-off.

### Week 2: Skill + Integration

- Day 8-10: Write first custom skill (Scrum retro synthesis for Cvtot)
- Day 11-12: Configure Slack/Telegram integration
- Day 13-14: Production-ize 1 real workflow (e.g., weekly briefing automation)

**Deliverable:** 1 live automation running autonomously.

---

## Part 9 — Rủi ro + Risks

### 9.1 Cost unpredictability

Sub-agents = N× LLM calls. Research + report + slides = 3-5 agents. Each 5-10 LLM calls. **Per task: $0.50-5 GPT-4 class.**

Monthly cost vary: 20 tasks × $2 = $40/month. Or: 200 tasks × $2 = $400.

**Mitigation:** Set task budget limits trong config.

### 9.2 Autonomous = risky

Long tasks = agent drifts. No human in loop. Possible:
- Wrong direction taken, keeps going
- Hallucination entrenched
- Output wrong but presented confidently

**Mitigation:** Review all outputs before ship. Don't auto-forward to clients.

### 9.3 LangGraph lock-in

deer-flow deep uses LangGraph. If LangGraph shifts direction, deer-flow affected.

**Mitigation:** Acceptable risk given ByteDance backing; but monitor LangGraph.

### 9.4 Multi-channel = attack surface

5 IM platforms = 5× exposure. Bot token leak = bot hijacked.

**Mitigation:** local trusted network deployment (README recommends). Don't expose public Internet without hardening.

### 9.5 ByteDance strategic shifts

US-China tensions, ByteDance priorities. deer-flow = OSS but funded by ByteDance.

**Mitigation:** MIT license = forkable. Community could maintain even if ByteDance shifts.

---

## Part 10 — Tiếp theo nên làm gì

### 10.1 Near-term

**Option 1 — Pilot in Storm Bear:**
Install deer-flow, deploy retro synthesis skill, run on 1 real team. Data-driven decision.

**Option 2 — Wait for v2.x stability:**
v2 is new (rebuilt from scratch). Let community battle-test, adopt v2.2 or later.

**Option 3 — Compare với alternatives:**
Research OpenHands, CrewAI, Agent Zero first. Pick winner before commit.

### 10.2 Medium-term

**Option 4 — Port Storm Bear routine to deer-flow:**
Test cross-framework portability. Learn deer-flow deeply. Validate T5 tier.

**Option 5 — VN market contribution:**
- Add Zalo integration (PR to deer-flow)
- VN translation `README_vi.md`
- Community case study: deer-flow cho VN Scrum coach

### 10.3 Long-term

**Option 6 — Enterprise deployment:**
If Scrum coaching client adopts deer-flow, Storm Bear positions as integration partner.

---

## Tóm tắt / Summary

**deer-flow = open-source SuperAgent harness cho long-horizon autonomous tasks.** ByteDance, 62K stars, v2.0 #1 Trending. **Tier 5 "Agent-as-application" — first entrant trong Storm Bear corpus.**

**Khi dùng:**
- Long tasks (minutes-hours)
- Autonomous execution
- Async delivery via IM
- Team / organization scale

**Khi không dùng:**
- Short interactive tasks (Claude Code T1)
- Multi-tenant SaaS (goclaw T2)
- Learning concepts (course T3)
- Single service integration (notebooklm-py T4)

**Cross-pollination với Storm Bear:**
- Scrum retro synthesis = killer use case
- Weekly coaching briefing automation
- Custom skills cho Scrum coach workflow
- Potential routine migration (routine v2 feature)

**Next:** Install + pilot 1 real workflow. Compare với alternatives. Decide integration path.

---

## Cross-references

- Main vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Wiki entities:
  - [[../02 Wiki/(C) SuperAgent Harness Architecture]]
  - [[../02 Wiki/(C) Skill System (Progressive Loading)]]
  - [[../02 Wiki/(C) Sub-Agent System (Parallel Fan-out)]]
  - [[../02 Wiki/(C) Message Gateway (Multi-Channel)]]
- Taxonomy v4 (5-tier, this session): [[(C) Agent framework taxonomy v4 - 5 tier with application]]
- Siblings:
  - 4 T1 trong `03 Projects/`
  - 1 T2 goclaw
  - 1 T3 course
  - 1 T4 notebooklm-py
  - 1 outside-scope build-your-own-x
