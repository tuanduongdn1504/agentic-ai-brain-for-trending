# (C) aidevops — Hướng dẫn cho người mới (VN+EN bilingual)

> Dành cho người mới làm quen với `marcusquinn/aidevops` ("AI DevOps Framework") — OpenCode plugin và AI operations platform với 13 specialist agents + ~2,665+ agentic primitives. Mục tiêu: hiểu nhanh, đánh giá phù hợp, không ràng buộc commercial.

---

## Phần 1 — Một câu giới thiệu / One-line summary

**EN:** aidevops is an OpenCode plugin and AI operations platform (MIT, 5.5 months old, 212 stars, by Marcus Quinn / Jersey UK) that orchestrates 13 specialist AI agents across development + business + marketing + creative domains, with autonomous 2-minute pulse supervisor running multi-day projects without human babysitting.

**VN:** aidevops là một OpenCode plugin và nền tảng vận hành AI (giấy phép MIT, dự án mới 5.5 tháng tuổi, 212 sao, do Marcus Quinn / Jersey Anh phát triển) điều phối 13 AI agent chuyên môn xuyên suốt phát triển phần mềm + kinh doanh + tiếp thị + sáng tạo, với một "pulse supervisor" tự động chạy mỗi 2 phút quản lý các dự án nhiều ngày mà không cần con người trông nom.

**Tagline (verbatim):** *"Vibe-Coding is easy. DevOps is hard. OpenCode & Git token-efficient AI agent automation for your app, business, and personal development."*

---

## Phần 2 — Aidevops khác gì so với các framework khác trong corpus Storm Bear?

| Đặc điểm / Feature | aidevops v47 | T1 corpus peers |
|---|---|---|
| **Runtime primary** | **OpenCode (corpus-first T1 OpenCode-primary)** | Mostly Claude Code primary |
| **Domain coverage** | **13 specialist domains** (corpus-broadest tied with agency-agents) | Mostly 1 (coding) |
| **Primitive count** | **~2,665+ files (CORPUS-RECORD; 5× ruflo v42)** | 50-200 typical |
| **Governance file model** | **AGENTS.md authoritative + CLAUDE.md+AGENT.md as redirect-shims (CORPUS-FIRST inversion)** | CLAUDE.md primary |
| **Quality platforms** | **8 external (Codacy + CodeFactor + CodeRabbit + Sonar + Qlty + Bandit + secretlint + ShellCheck)** | 0-5 typical |
| **Cross-provider verification** | **Yes, for high-stakes ops (CORPUS-FIRST)** | No |
| **Autonomous supervisor** | **Yes, every 2 min via launchd, LLM-driven** | Most have manual orchestration |
| **Mission orchestration** | Yes (multi-day projects with milestones + budget tracking) | Few |
| **Voice input** | **Yes (Voice Bridge ~6-8s on Apple Silicon)** | No |
| **Auth pool (subscription rotation)** | **4 providers (Anthropic + OpenAI + Cursor + Google)** | 0-1 typical |
| **Distribution** | **5 surfaces (npm + Bun + Homebrew + curl + manual)** | 1-3 typical |
| **License** | MIT | Mostly MIT |
| **Scale (stars)** | **212 (cold-start)** | 5K-90K typical |

**Khác biệt cốt lõi / Core difference:** aidevops là **cross-domain AI-DevOps platform với OpenCode-first design**, không phải coding-only assistant. Nó quản lý không chỉ code mà còn marketing / sales / legal / health / finance — cho **solo developer hoặc small team muốn tự động hóa toàn bộ business operations** chứ không chỉ coding workflow.

---

## Phần 3 — Cài đặt nhanh / Quick install

### Prerequisites
- macOS hoặc Linux (no Windows native support)
- Node.js 18+ hoặc Bun
- Git
- (Khuyến nghị / Recommended) **OpenCode** đã cài: `bun install -g opencode-ai` hoặc tải từ https://opencode.ai/

### Cách cài / Install method (chọn 1 / pick one)

**npm (recommended):**
```bash
npm install -g aidevops && aidevops update
```

**Bun (fast):**
```bash
bun install -g aidevops && aidevops update
```

**Homebrew (macOS/Linux):**
```bash
brew install marcusquinn/tap/aidevops && aidevops update
```

**Direct curl:**
```bash
bash <(curl -fsSL https://aidevops.sh/install)
```

### Sau khi cài / Post-install

```bash
aidevops status     # Kiểm tra cài đặt / Check installation
aidevops doctor     # Detect duplicate installs + PATH conflicts
```

**Khởi động OpenCode + onboarding wizard:**
```bash
opencode  # Mở OpenCode TUI
# Trong OpenCode, gõ: /onboarding
```

`/onboarding` wizard sẽ:
- Giải thích aidevops làm gì
- Hỏi về công việc của bạn để gợi ý
- Hiển thị services nào đã configured / cần setup
- Hướng dẫn từng bước với links + commands

---

## Phần 4 — 13 specialist domain agents

### Tổng quan / Overview

| # | Agent | Domain | Storm Bear / Scrum-coach use? |
|---|---|---|---|
| 1 | **Build+** (default) | Code: research/discuss/implement/fix | ✅ DIRECT (technical work) |
| 2 | **Automate** | Workflow automation, cron, launchd | ✅ DIRECT (sprint automation) |
| 3 | **SEO** | Search optimization | 🟡 CLIENT-FACING (if Scrum coach offers SEO) |
| 4 | **Marketing-Sales** | Marketing campaigns + sales pipeline | 🟡 CLIENT-FACING |
| 5 | **Content** | Content creation + media + writing | ✅ DIRECT (blog posts, course content) |
| 6 | **Legal** | Legal advisory framing | 🟡 CLIENT-FACING (NOT a substitute for lawyer) |
| 7 | **Sales** | Sales pipeline | 🟡 CLIENT-FACING |
| 8 | **Research** | Research-deep workflows + citations | ✅ DIRECT (research clients, frameworks) |
| 9 | **Video** | Video creation (Remotion / HeyGen / Veo 3) | 🟡 ADJACENT |
| 10 | **Business** | Business operations advisory | 🟡 CLIENT-FACING |
| 11 | **Accounts** | Bookkeeping (QuickFile MCP) | ⚠️ UK-specific (QuickFile = UK accounting); not VN-relevant |
| 12 | **Social Media** | Cross-platform posting | 🟡 CLIENT-FACING |
| 13 | **Health** | Health advisory | ⚠️ NOT recommended for production health-advice (legal/medical disclaimers needed) |

**Storm Bear-relevant agents: 1, 2, 5, 8** (Build+ / Automate / Content / Research) directly applicable.

---

## Phần 5 — Pulse Supervisor: tính năng đặc biệt nhất / Most distinctive feature

**Verbatim:** *"The pulse is the heartbeat of aidevops — an autonomous AI supervisor that runs every 2 minutes via launchd. There is no human at the terminal."*

**VN:** Pulse là "nhịp tim" của aidevops — supervisor AI tự động chạy mỗi 2 phút qua launchd. **Không có con người trông nom**.

### 9 phases mỗi cycle / 9 phases per cycle:

1. **Capacity check** — kiểm tra circuit breaker, dynamic worker slots theo RAM
2. **Merge ready PRs** — Green CI + no blocking reviews → squash merge
3. **Fix failing PRs** — dispatch worker fix CI failures
4. **Detect stuck work** — PRs open 6+ hours không activity → flag/close/re-file
5. **Dispatch workers** — route open issues theo priority + `blocked-by:` deps
6. **Advance missions** — kiểm tra multi-day missions, dispatch features, validate milestones
7. **Triage quality** — đọc daily quality findings (ShellCheck/Sonar/Codacy/CodeRabbit) → tạo issues
8. **Sync TODOs** — tạo GitHub issues cho unsynced TODO entries
9. **Kill stuck workers** — workers chạy 3+ giờ không có PR → kill để giải phóng slots

**Quan trọng / Critical:** Pulse **là một LLM, không phải script**. Nó **đọc issue bodies, đánh giá context, sử dụng phán đoán**.

**Manual trigger:**
```bash
opencode run "/pulse"
```

**Auto-trigger:** launchd plist cài tự động (every 2 minutes).

---

## Phần 6 — Cross-Provider Verification: an toàn cho operations rủi ro cao

**Verbatim philosophy:** *"Same-provider models share training data and failure modes. A Claude hallucination is unlikely to be reproduced by Gemini or GPT, and vice versa."*

**VN:** Models cùng provider chia sẻ training data + failure modes. Claude hallucinate thì Gemini/GPT thường KHÔNG reproduce hallucinate đó.

### Risk taxonomy / Phân loại rủi ro:

| Risk level | Examples | Action |
|---|---|---|
| **Critical** | `git push --force` to main, `DROP DATABASE`, production deploy | **Blocked** unless second model agrees |
| **High** | Force push feature branch, data migration, secret exposure | **Warned**, verification recommended |
| **Medium** | Bulk file deletion, config changes | **Logged** |
| **Low** | Normal edits, test runs | No verification |

### Storm Bear ứng dụng / Storm Bear application:

Với Scrum coach client work, các high-stakes operations bao gồm:
- Tạo/chỉnh sửa client documents (legal contracts / SOWs / proposals)
- Email outreach to client stakeholders
- Public publishing on behalf of clients (LinkedIn / Twitter / blog)
- Schedule management (calendar invites / availability commitments)
- Financial commitments (invoices / payment requests)

**Khuyến nghị / Recommendation:** Nếu Storm Bear vault tương lai có client-facing AI workflows ở quy mô lớn, adopt cross-provider verification primitive là **future-state safety preparation**. Không phải priority hiện tại nhưng là pattern tham khảo tốt.

---

## Phần 7 — AGENTS.md authoritative + 3-layer governance hierarchy (CORPUS-FIRST)

**Aidevops là wiki đầu tiên trong corpus Storm Bear có CLAUDE.md là redirect-shim, không phải primary.**

### File hierarchy:

| Layer | File | Size | Audience |
|---|---|---|---|
| Layer 0 (shim) | `CLAUDE.md` | 440B | Anthropic Claude Code tools |
| Layer 0 (shim) | `AGENT.md` | 420B | Singular-AGENT.md tools |
| Layer 1 (dev-guide) | `AGENTS.md` (root) | 3KB | Contributors |
| Layer 2 (user-guide) | `.agents/AGENTS.md` | ~18KB | End-users (deployed to `~/.aidevops/agents/`) |

### CLAUDE.md content (440B verbatim):

```markdown
# AI DevOps Framework - Claude Redirect

**See [AGENTS.md](AGENTS.md) for the authoritative AI assistant guidance.**

This file exists for compatibility with Claude Code and other Anthropic tools that look for `CLAUDE.md`.

All instructions, documentation, and operational guidance are maintained in **AGENTS.md** as the single source of truth.
```

### Storm Bear vault analog (đề xuất / proposed):

| Layer | Storm Bear file | Purpose |
|---|---|---|
| Layer 0 | `CLAUDE.md` redirect-shim → `AGENTS.md` | Anthropic Claude compat |
| Layer 1 | `AGENTS.md` (vault root) | Developer/contributor guide |
| Layer 2 | `05 Skills/<skill>/SKILL.md` | Per-skill operational guide |
| Layer 3 | `03 Projects/<name>/CLAUDE.md` | Per-project context |

**Đây là pattern tham khảo cho v27 diagnostic HIGH item #1** (vault CLAUDE.md refactor — đã defer 27 sessions).

**Estimated effort:** 3-4 hours adoption.

---

## Phần 8 — 8-tool quality stack (corpus-record)

| Tool | Role | Storm Bear vault relevance |
|---|---|---|
| **Codacy** | Multi-tool grading | ⚠️ Low (markdown-only repo) |
| **CodeFactor** | Repository grading | ⚠️ Low (markdown-only) |
| **CodeRabbit** | AI review on PRs | ✅ HIGH (markdown PR review) |
| **SonarCloud** | Quality gate | ⚠️ Low (markdown-only) |
| **Qlty** | Universal code quality (70+ linters) | ⚠️ Low (markdown-only) |
| **Bandit** | Python security | ⚠️ Low (no Python in vault currently) |
| **secretlint** | Secret detection | ✅ HIGH (catches accidental commits) |
| **ShellCheck** | Shell script linting | ⚠️ Conditional (if vault adopts shell scripts) |

**Subset adoption (3 of 8 tools) viable for Storm Bear vault:**
1. ✅ secretlint (run via pre-commit hook on vault)
2. ✅ markdownlint (already partially used)
3. ✅ CodeRabbit on vault PRs (markdown content review)

**Estimated effort:** 1-2 hours setup.

---

## Phần 9 — Setup workflow chi tiết / Detailed setup walkthrough

### Step 1: Cài OpenCode + aidevops
```bash
# Cài OpenCode trước
bun install -g opencode-ai

# Cài aidevops
npm install -g aidevops && aidevops update
```

### Step 2: Authenticate model providers
```bash
# Anthropic Claude (qua OpenCode native OAuth — Claude Pro/Max subscribers free)
aidevops model-accounts-pool add anthropic
# Browser sẽ mở OAuth flow

# OpenAI (ChatGPT Plus/Pro)
aidevops model-accounts-pool add openai

# Cursor (đọc local IDE state)
oauth-pool-helper.sh add cursor

# Google (AI Pro/Ultra/Workspace)
aidevops model-accounts-pool add google

# Restart OpenCode sau khi add accounts
```

### Step 3: Initialize project
```bash
cd ~/your-project
aidevops init                          # Enable all features
# OR
aidevops init planning,git-workflow    # Specific features only
```

Tạo:
- `.aidevops.json` — config + enabled features
- `.agents` symlink → `~/.aidevops/agents/`
- `TODO.md` — quick task tracking
- `todo/PLANS.md` — complex execution plans
- `.beads/` — task graph DB (nếu enabled)

### Step 4: Onboarding wizard
```bash
opencode
# Trong TUI:
/onboarding
```

### Step 5: First task workflow
```bash
# Tạo task interactive
/define
# OR
/new-task

# Mỗi task tạo brief mandatory tại todo/tasks/{task_id}-brief.md

# Chạy headless worker hoặc interactive
/full-loop  # Ralph loop iterative
```

---

## Phần 10 — Storm Bear pilot evaluation roadmap (3-week)

### Week 1: Read + assess (3-5 hours)
- Read `AGENTS.md` (3KB) + `.agents/AGENTS.md` (~18KB user guide)
- Read README.md key sections (Pulse Supervisor / Multi-Model Verification / Project Bundles / Agent Design Patterns)
- Đánh giá / Evaluate fit:
  - Có phù hợp với current Storm Bear workflow? (Currently Claude-Code-primary; aidevops is OpenCode-first)
  - Có cần 13-domain coverage hay chỉ cần 1-2 domains?
  - Có cần autonomous pulse supervisor hay manual orchestration đủ?

### Week 2: Sandbox install (3-5 hours)
- Install on **non-critical test directory** (NOT vault root)
- Run `/onboarding` wizard
- Try 1-2 commands manually:
  - `/pulse` (manual trigger)
  - `/full-loop` on simple task
  - `/define` task creation
  - `aidevops status` + `aidevops doctor`
- **DO NOT** install pulse launchd plist yet (autonomous mode requires trust + budget guardrails)

### Week 3: Decision + (optional) limited adoption (2-4 hours)
- Decision tree:
  - **Adopt full framework?** Requires platform-switch from Claude Code to OpenCode + ~2,665 primitive learning curve. NOT recommended for short-term.
  - **Adopt AGENTS.md-authoritative pattern only?** ✅ RECOMMENDED. Closes v27 diagnostic HIGH item #1. 3-4h effort.
  - **Adopt 8-tool quality stack subset (3 tools)?** ✅ MEDIUM-VALUE. 1-2h effort.
  - **Adopt Lance Martin 16-pattern checklist as skill audit?** ✅ MEDIUM-VALUE. 5-7h effort across all skills.
  - **Adopt TOON format for vault subagent-index?** ⚠️ LOW-PRIORITY (theoretical token-savings only).

**Total Storm Bear pilot evaluation budget: ~12-15 hours.** Most likely outcome: partial adoption (AGENTS.md pattern + quality stack subset + Lance Martin checklist) without full framework adoption.

---

## Phần 11 — Risks + caveats / Rủi ro + lưu ý

### ⚠️ Cold-start scale (212 stars / 5.5 months)
- Aidevops at 5.5 months is YOUNG project despite mature framework surface
- Bus factor = 1 (Marcus Quinn solo maintainer)
- Battle-tested confidence LOW vs 30K+-star peers (BMAD v11 / spec-kit v17 / claude-howto v32)
- **Khuyến nghị / Recommendation:** Test in sandbox before any production-critical adoption.

### ⚠️ OpenCode-first design = friction for Claude Code primary users
- Storm Bear hiện tại Claude-Code-primary
- Adopt aidevops fully = require OpenCode platform switch + retraining workflow
- **Lower-friction alternative:** Adopt only patterns (AGENTS.md model + quality stack + Lance Martin checklist) without framework

### ⚠️ Bash-primary implementation
- 873+ shell scripts trong `.agents/scripts/`
- Nếu không thoải mái với shell scripting → friction debugging/customizing
- **Recommendation:** Run aidevops as black-box; customize sparingly

### ⚠️ Commercial positioning (`aidevops.sh` homepage)
- Marcus has dedicated commercial domain + paid pool services
- Pool services = user-owned subscription rotation (NOT SaaS reseller)
- Brand-association consideration if Storm Bear stays personal-OS focused

### ⚠️ Autonomous pulse supervisor risks
- 2-min cron + LLM judgment can produce unexpected actions
- Budget tracking + circuit breaker + worker kill mechanisms are guardrails, NOT silver bullet
- **Recommendation:** DO NOT install pulse plist on critical repos until trust established
- Cross-provider verification only kicks in for high-stakes operations; medium-risk operations are merely "logged"

### ⚠️ Ethical/legal advisory framing
- 13-agent set includes Legal + Health domains
- aidevops Legal/Health advisors are NOT licensed lawyer/medical professional substitutes
- **Disclaimer for Storm Bear use:** Always cross-check legal/health output with licensed professionals before client communication or personal decisions

### ⚠️ Data privacy
- Cross-provider model rotation sends data across multiple providers
- Auth pool reads local IDE state (Cursor especially) → ensure proper credential hygiene
- **gopass + secretlint** built-in but operator-discipline matters

---

## Phần 12 — Composability với Storm Bear vault hiện tại

**Storm Bear vault current state:**
- Markdown-based personal OS
- Claude Code primary
- 47 wikis in corpus
- 37 confirmed patterns + ~21 active candidates
- LLM Wiki Routine v2.1
- No formal quality discipline
- Single-source CLAUDE.md (vault root) at ~150K+ lines

**Aidevops composability options (lower-friction first):**

### Option A: AGENTS.md-authoritative pattern adoption (3-4h, HIGH leverage)
- Adopt Layer 0/1/2/3 governance hierarchy
- Move vault root CLAUDE.md → AGENTS.md authoritative + slim CLAUDE.md redirect
- Closes v27 diagnostic HIGH item #1

### Option B: 8-tool quality stack subset (1-2h, MEDIUM leverage)
- Add `secretlint` pre-commit hook on vault repo
- Add CodeRabbit AI PR review on vault GitHub
- Extend existing markdownlint rules

### Option C: Lance Martin 16-pattern skill audit (5-7h, MEDIUM leverage)
- Read Lance Martin pattern table from aidevops README
- Create `05 Skills/(C) skill-audit-lance-martin-16.md` framework
- Per-skill scorecard

### Option D: Full aidevops adoption (40+ hours, NOT recommended)
- Platform switch Claude Code → OpenCode
- Learn ~2,665 primitives
- Adopt 13-domain agents (most irrelevant for Storm Bear personal OS)
- Configure pulse supervisor + missions + quality stack + cross-provider verification

**Recommendation:** Option A → Option B → Option C in sequence (~10-13h total). Option D NOT recommended unless Storm Bear pivots to full AI-DevOps platform.

---

## Phần 13 — Quick reference / Tham chiếu nhanh

### Key files to read first (priority order)
1. `README.md` (142KB — read selectively; cover positioning + agent design patterns + pulse supervisor + multi-model verification + bundles)
2. `AGENTS.md` root (3KB — full read; corpus-first AGENTS.md-authoritative)
3. `.agents/AGENTS.md` (~18KB — full read; user guide deployed to `~/.aidevops/agents/`)
4. `CREDITS.md` (5.6KB — full read; intellectual lineage)
5. `CONTRIBUTING.md` (3KB — light scan)

### Key URLs
- Repo: https://github.com/marcusquinn/aidevops
- Homepage: https://aidevops.sh
- npm: https://www.npmjs.com/package/aidevops
- Author: https://github.com/marcusquinn
- License: MIT (https://opensource.org/licenses/MIT)
- Lance Martin patterns source: https://x.com/RLanceMartin/status/2009683038272401719
- Mngr (imbue-ai): https://github.com/imbue-ai/mngr/

### Key CLI commands (cheat sheet)
```bash
aidevops status              # Check installation
aidevops doctor              # Detect issues
aidevops init [features]     # Initialize project
aidevops update              # Update framework
aidevops security            # All security checks
aidevops secret              # Manage secrets (gopass)

# In OpenCode
/onboarding                  # First-run wizard
/define                      # Interactive task creation
/full-loop                   # Ralph loop iterative
/mission "<goal>"            # Multi-day project scoping
/runners                     # Batch dispatch
/pulse                       # Manual supervisor trigger
/route                       # Cost-aware model routing
/budget-analysis             # Burn-rate review
```

### Storm Bear pilot decision tree

```
Is Storm Bear primarily Claude Code? → YES (currently)
  ↓
Are you committing to OpenCode platform switch? → NO (most likely)
  ↓
Adopt patterns only, NOT framework:
  • AGENTS.md authoritative pattern (Option A) ✅
  • 8-tool quality stack subset (Option B) ✅
  • Lance Martin 16-pattern checklist (Option C) ✅
  • TOON format ⚠️ LOW priority

Total adoption: ~10-13h.
v27 diagnostic HIGH item #1 closed via Option A.
```

---

## Phần 14 — Closing notes

**aidevops v47 (212 stars / 5.5 months / Marcus Quinn / Jersey UK / MIT) is a corpus-first OpenCode-primary T1 framework with corpus-record EXTREME primitive count (~2,665+; 5× ruflo v42).** Its main value to Storm Bear is **observational + pattern-template** rather than direct framework adoption:

- AGENTS.md-authoritative pattern = direct template for vault CLAUDE.md refactor (v27 item #1)
- 8-tool quality stack = template for vault quality discipline
- Lance Martin 16-pattern checklist = skill audit framework
- Cross-provider verification = future client-facing safety primitive
- TOON format = future token-efficient catalog format

**Full framework adoption NOT recommended** for Claude-Code-primary Storm Bear operator without OpenCode platform commitment.

**Closing thought from aidevops README (verbatim):**

> *"Sane vibe-coding through structure. Built on proven patterns: aidevops implements industry-standard agent design patterns - including multi-layer action spaces, context isolation, and iterative execution loops."*

---

*(C) Generated by Claude — Bilingual VN+EN beginner guide for v47 aidevops*
