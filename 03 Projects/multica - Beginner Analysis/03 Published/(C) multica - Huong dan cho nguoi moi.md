# (C) multica — Hướng dẫn cho người mới / Beginner's Guide

> **Repo:** [multica-ai/multica](https://github.com/multica-ai/multica) — 16.2K ⭐, 2K forks, v0.2.6
> **Tagline:** *"Your next 10 hires won't be human"* — open-source managed agents platform
> **Wiki:** `(C) index` — 15th LLM Wiki trong Storm Bear corpus
> **Audience:** VN developers + Scrum coaches tìm hiểu agent-orchestration platform

---

## Part 1 — Multica là gì? / What is Multica?

### 🇻🇳 Tiếng Việt

**Multica** là một **nền tảng quản lý agent mã nguồn mở** — biến các coding agent (Claude Code, Codex, Cursor Agent, v.v.) thành **"đồng đội thật sự"** trong team bạn. Bạn giao task, agent làm, bạn theo dõi tiến độ realtime qua web dashboard hoặc app desktop.

Positioning chính thức (từ `CLAUDE.md` repo): **"giống Linear nhưng agents là first-class citizens"** — tức là lấy UX của Linear (issue tracking, board, assignments, comments) và áp dụng cho agent thay vì cho người.

Tagline marketing: *"10 nhân viên tiếp theo của bạn sẽ không phải là người"*. Đây là **autonomy-maximum framing** — giống với paperclip v14 (*"zero-human companies"*) nhưng multica có tone cân bằng hơn (team collaboration chứ không phải thay người hoàn toàn).

### 🇬🇧 English

**Multica** is an **open-source managed agents platform** — turn coding agents (Claude Code, Codex, Cursor Agent, etc.) into **"real teammates"**. You assign tasks, agents execute, you track progress in real-time via web dashboard or desktop app.

Official positioning (from repo `CLAUDE.md`): **"similar to Linear but with agents as first-class citizens"** — i.e. take Linear's UX (issue tracking, boards, assignments, comments) and apply it to agents rather than humans.

Marketing tagline: *"Your next 10 hires won't be human"*. This is **autonomy-maximum framing** — parallel to paperclip v14 (*"zero-human companies"*) but with a more balanced tone (team collaboration rather than full human replacement).

---

## Part 2 — Tại sao đáng chú ý? / Why it matters

### Corpus-first signals

Trong Storm Bear corpus (15 wikis), multica đứng đầu về nhiều khía cạnh:

| Signal | Multica | Corpus context |
|--------|---------|----------------|
| **Electron desktop app** | ✅ Yes | **First** in corpus |
| **8 agent models supported** | Claude Code, Codex, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent | **Broadest BYO-agent list** |
| **skills-lock.json** | ✅ Yes | **First dependency-locked skill manifest** |
| **pgvector/Postgres 17** | ✅ Yes | **First vector-capable DB** |
| **Turborepo** | ✅ Yes | **First** in corpus |
| **Hybrid local-daemon + cloud-orchestration** | ✅ Yes | **Unique architecture** |
| **Multi-workspace (first-class)** | ✅ Yes | Native — not bolted-on |

### Tier 2 validation milestone

Multica là **Tier 2 ("Agent-as-service") entrant thứ 2** của corpus — validate multi-entrant cho tier này (cùng goclaw v4). Sau v15, **4/5 tiers** đã multi-entrant (chỉ T3 Agent-as-education còn đơn lẻ).

→ Xem `(C) T2 2-way Validation + Pattern 9 Platform-Tier Refinement + Storm Bear.md`.

---

## Part 3 — Task lifecycle / Vòng đời task

### 🇻🇳 Mô hình Linear-analog

Multica dùng **state machine nguyên tử** (atomic lifecycle):

```
enqueue → claim → start → complete
                          └── fail
```

- **enqueue** — Người dùng tạo issue (task) trong workspace
- **claim** — Agent đăng ký nhận task (atomic — chỉ 1 agent giành được)
- **start** — Agent bắt đầu execute
- **complete / fail** — Kết quả cuối

Trong lúc agent execute, **WebSocket push progress updates** về UI (Next.js web + Electron desktop). Nhưng theo `CLAUDE.md`: *"WS events invalidate queries — they never write to stores directly."* Tức là agent cập nhật → server broadcast → UI invalidate cache → refetch → render. Đây là pattern sạch hơn WebSocket-trực-tiếp-ghi-vào-UI.

### 🇬🇧 Linear-analog model

Atomic state machine: `enqueue → claim → start → complete/fail`. WebSocket pushes progress but **invalidates queries** rather than writing to stores directly — cleaner than direct WebSocket-to-UI writes.

**Parallel:** paperclip v14's "atomic checkout semantics" invariant. Both multica and paperclip enforce atomicity architecturally, though multica has lighter governance.

---

## Part 4 — Kiến trúc / Architecture

### Hybrid local-daemon + cloud-orchestration (corpus-first)

```
User machine:                          Multica Cloud (or self-hosted):
  ├─ CLI (`multica`)                     ├─ Next.js 16 web (dashboard)
  ├─ Agent Daemon                         ├─ Go API server
  │    ├─ Claude Code session              │    ├─ Chi router
  │    ├─ Cursor agent                     │    ├─ WebSocket hub
  │    ├─ Codex invocation                 │    └─ pgvector queries
  │    └─ ... (any of 8 models)            └─ PostgreSQL 17 + pgvector
  └─ File system access
       ↑                                    ↑
       └──────── WebSocket ─────────────────┘
```

**Tại sao hybrid:**
- **Privacy:** Code ở máy user, daemon execute locally
- **Cost:** Không compute trên cloud cho agent tasks
- **Subscription:** User dùng Claude Code/Cursor license của họ
- **Orchestration:** Cloud theo dõi progress, store history, cross-team collaboration

### Dual app — web + Electron desktop

```
apps/
├── web/       (Next.js 16)
└── desktop/   (Electron via electron-vite)

packages/
├── core/      (headless business logic)
├── ui/        (atomic components)
└── views/     (shared business pages — WORKS IN BOTH APPS)
```

**5 non-negotiable cross-platform rules** (từ `CLAUDE.md`):
1. Add component vào `packages/views/<domain>/`
2. Wire route ở CẢ `apps/web/` AND `apps/desktop/`
3. Dùng `useNavigation().push()` (không dùng framework-specific API trong shared code)
4. Nhận `wsId` làm parameter trong hooks, không call `useWorkspaceId()` trực tiếp
5. Platform chrome (drag strips, tab system) chỉ ở app-specific code

→ Xem `(C) Electron Desktop + Multi-Platform Architecture.md`.

---

## Part 5 — 8 agent models

Multica hỗ trợ **broadest BYO-agent list trong corpus**:

| Model | Provider | Notes |
|-------|----------|-------|
| Claude Code | Anthropic | Primary (Anthropic skills imported) |
| Codex | OpenAI | OpenAI agent |
| **OpenClaw** | Community | Cũng có ở paperclip v14 + codymaster v12 — emerging standard |
| OpenCode | Community | Open-source code agent |
| **Hermes** | Nous Research? | Cũng có ở paperclip v14 |
| Gemini | Google | Multimodal |
| Pi | Inflection AI | Personal AI |
| Cursor Agent | Cursor IDE | IDE-integrated |

**Cross-wiki ecosystem signal:** OpenClaw xuất hiện ở 3 wikis (codymaster + paperclip + multica). Hermes ở 2 wikis (paperclip + multica). Có vẻ là **emerging agent-runtime standards** — không phải runtime proprietary của 1 framework.

---

## Part 6 — skills-lock.json (first in corpus)

### Dependency-locked skill manifest

Multica là **framework đầu tiên trong corpus** lock external skill dependencies:

```json
{
  "version": 1,
  "skills": {
    "frontend-design": {
      "source": "anthropics/skills",
      "sourceType": "github",
      "computedHash": "063a0e64..."
    },
    "shadcn": { "source": "shadcn/ui", ... },
    "ui-ux-pro-max": {
      "source": "nextlevelbuilder/ui-ux-pro-max-skill",
      ...
    },
    "web-design-guidelines": {
      "source": "vercel-labs/agent-skills",
      ...
    }
  }
}
```

**Parallel:** `package-lock.json` / `pnpm-lock.yaml` / `Cargo.lock`. Áp dụng cho agent skills.

### Ecosystem cross-pollination

4 sources từ 4 orgs khác nhau — **hệ sinh thái skill đang hình thành**:

- **anthropics/skills** — Anthropic official skill registry (skill đầu tiên từ Anthropic trong corpus)
- **vercel-labs/agent-skills** — Vercel đầu tư vào agent ecosystem
- **nextlevelbuilder/ui-ux-pro-max-skill** — **nextlevelbuilder là org của goclaw v4** (T2 peer). Org này publish cross-project tools → **ecosystem-layer cross-pollination**
- **shadcn/ui** — UI lib standard

→ Xem `(C) skills-lock + Ecosystem Cross-Pollination.md`.

---

## Part 7 — Cài đặt / Installation

### 🇻🇳 Quick install

**macOS/Linux (Homebrew):**
```bash
brew install multica-ai/tap/multica
multica login
multica workspace create my-workspace
```

**Windows (PowerShell):**
```powershell
irm https://multica.ai/install.ps1 | iex
multica login
multica workspace create my-workspace
```

**Script install (Linux):**
```bash
curl -fsSL https://multica.ai/install.sh | sh
```

**Self-hosting:** Đọc `SELF_HOSTING.md` trong repo (Docker + Postgres 17 setup).

### 🇬🇧 Quick install

Three distribution channels:
- **Homebrew tap** (macOS/Linux primary)
- **PowerShell script** (Windows)
- **curl | sh** (Linux)
- **Desktop app** (Electron binary — distribution path TBD)
- **Self-hosting** (Docker + Postgres 17)

### First task

```bash
multica workspace switch my-workspace
multica task create \
  --title "Implement JWT auth" \
  --assign claude-code \
  --description "Add JWT middleware to /api/auth"
```

Daemon sẽ tự claim task, start Claude Code session, push progress via WebSocket, complete → bạn review qua dashboard.

---

## Part 8 — Multica vs Paperclip (explicit competitor)

Multica README có section **"Multica vs Paperclip"** so sánh trực tiếp:

| Aspect | Multica | Paperclip |
|--------|---------|-----------|
| **Abstraction** | Workspace + Issues (Linear paradigm) | Company + Org Chart + Employees |
| **Governance** | Lightweight | Heavy (5 invariants + 4 primitives) |
| **Target user** | Teams (multi-user native) | Solo operator (multi-user roadmap) |
| **Deployment** | Cloud-first + self-hosted | Self-hosted primary |
| **Framing** | "10 hires won't be human" | "Zero-human companies" |
| **Philosophy** | Team collaboration | Autonomous AGI-test |
| **Surfaces** | CLI + web + Electron desktop | CLI + web (self-hosted) |
| **Agent models** | 8 | 6 |

**Tóm tắt:** Multica nhẹ hơn + team-collaboration-first; Paperclip nặng governance hơn + zero-human-autonomous-first. Đây là **2 philosophies khác nhau trong cùng autonomy-maximum spectrum**.

→ Xem `(C) Linear-Analog Task Management for Agents.md` section 8.

---

## Part 9 — Ethical framing (autonomy-maximum tone)

### 🇻🇳 Cảnh báo tone

Tagline *"Your next 10 hires won't be human"* mang tone **thay thế nhân sự bằng AI**. Đây là **autonomy-maximum framing** — có tranh cãi:

- **Phía ủng hộ:** Giải phóng người khỏi repetitive coding work; scale nhỏ lên với agent help
- **Phía phản đối:** Framing này normalize job displacement; tone không phù hợp cho Scrum context (nơi human team dynamics là trọng tâm)

**Storm Bear stance:** Multica là **tool tốt cho agent orchestration**, nhưng framing marketing *không phù hợp* để giới thiệu trực tiếp cho Scrum teams. Positioning lại theo Storm Bear style: *"Multica giúp developer + Scrum team augment workflow với agents — không phải thay thế teammates."*

Tương tự cách xử lý paperclip v14's *"zero-human companies"* (xem `paperclip v14` wiki).

### 🇬🇧 Framing caution

Tagline normalizes human replacement framing. Use multica as **agent orchestration tool**, reframe away from replacement language in Scrum-team contexts. Precedent: paperclip v14 same caution.

---

## Part 10 — Storm Bear relevance

### Cho VN operator (Storm Bear user)

**Relevance level:** 🟡 **Medium** — thấp hơn BMAD/codymaster (VN translation) nhưng cao hơn autoresearch/build-your-own-x (outside domain).

**Signal points:**
- **CN (zh-CN) README không VN** — CJK-adjacent market, không direct VN
- **Linear paradigm** — VN dev teams dùng Linear/Jira quen → onboarding thấp
- **Electron desktop** — always-on workflow; có thể chạy trên Obsidian-style setup
- **Multi-workspace** — fits Scrum team-per-project pattern
- **8 agent models** — flexible cho team experiment nhiều agents
- **skills-lock.json** — pattern có thể áp dụng cho Storm Bear vault (lock LLM Wiki template version)

### 2-tuần learning roadmap

**Week 1: Try personal**
- Day 1-2: Install multica qua Homebrew, tạo workspace cá nhân
- Day 3-4: Assign 5-10 task cho Claude Code agent (backlog của Storm Bear vault itself)
- Day 5-7: Observe lifecycle — enqueue → claim → start → complete. Note failure modes.

**Week 2: Evaluate team fit**
- Day 8-10: Thử hybrid-team pilot — 1 team nhỏ experiment với multica (agents augment, not replace)
- Day 11-12: Compare với goclaw v4 (T2 peer) — pick tool fit best với team needs
- Day 13-14: Document findings vào Storm Bear vault → feed back vào cross-project Pattern Library

### NOT recommended cho

- Full Scrum team tool replacement (framing tension)
- Client coaching engagements là primary tool (philosophical mismatch)
- VN-first team without English comfort (documentation 100% EN + CN, no VI)

### Recommended cho

- Personal productivity (Storm Bear own backlog)
- Reference study (Linear-analog paradigm translation)
- Pattern mining (skills-lock + hybrid architecture là lesson cho Storm Bear)

---

## Part 11 — 4-week deep-dive roadmap

| Week | Focus | Deliverable |
|------|-------|-------------|
| **1** | Install + lifecycle exploration | Personal workspace + 20 tasks completed |
| **2** | Multi-agent comparison | Try Claude Code + Codex + Cursor Agent trên cùng task class |
| **3** | skills-lock + external skills | Import 1 external skill, study integrity hash workflow |
| **4** | Self-hosting + integration | Deploy self-hosted instance; integrate với Storm Bear vault pipeline |

---

## Part 12 — References + next steps

### Wiki pages

- [[(C) index]] — phase tracking + cross-refs
- [[(C) README + zh-CN summary]] — user-facing positioning
- [[(C) CLAUDE + AGENTS + CONTRIBUTING cluster summary]] — contributor discipline
- [[(C) Skills + Architecture + skills-lock cluster summary]] — tech substrate
- [[(C) Linear-Analog Task Management for Agents]] — core product entity
- [[(C) Electron Desktop + Multi-Platform Architecture]] — architecture entity
- [[(C) skills-lock + Ecosystem Cross-Pollination]] — novel pattern entity
- [[(C) T2 2-way Validation + Pattern 9 Platform-Tier Refinement + Storm Bear]] — tier meta-entity

### Cross-wiki siblings

- `../../goclaw - Beginner Analysis/` — **T2 peer (Tier 2 N=1)**
- `../../paperclip - Beginner Analysis/` — **explicit competitor (T5)**
- `../../codymaster - Beginner Analysis/` — shared OpenClaw mention (T1)
- `../../BMAD-METHOD - Beginner Analysis/` — T1 largest (45K ⭐)

### Official

- Repo: https://github.com/multica-ai/multica
- Homepage: https://multica.ai
- X (Twitter): @MulticaAI

### Suggested next action (Storm Bear)

**Try 1-week personal pilot.** Install Homebrew → tạo workspace → assign 10 Storm Bear vault maintenance tasks cho Claude Code. Measure lifecycle behavior. Feed learnings vào Pattern Library + evaluate multi-team pilot sau đó.

---

**Wiki 15/15 — T2 multi-entrant validation + 4/5 tiers validated. Routine `llm-wiki-routine` v1 thứ 15 auto-execution.**
