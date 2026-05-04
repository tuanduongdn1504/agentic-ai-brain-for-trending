# (C) paperclip — Hướng dẫn cho người mới (bilingual VN/EN)

> **Audience:** VN developers + Scrum coaches + product ops curious về AI agent orchestration. **⚠️ Ethical note:** Framework's "zero-human companies" framing có philosophical tension với Scrum coaching role.
> **Sources:** [[../02 Wiki/(C) index]] + 4 entity pages + 3 source summaries
> **Read time:** ~25-30 phút
> **Convention:** VN chính, EN cho technical + framework names

---

## Phần 1 — paperclip là gì? + Tagline warning

**paperclip** (paperclipai/paperclip) = **"Open-source orchestration for zero-human companies"** — hệ thống điều phối các AI agent tự động thành "công ty" hoàn toàn tự vận hành.

**Core metaphor:** *"If OpenClaw is an employee, Paperclip is the company."*

### ⚠️ Đọc phần này TRƯỚC khi tiếp tục

**Tên "paperclip" = direct reference đến Nick Bostrom's paperclip maximizer thought experiment** — một thí nghiệm tư duy nổi tiếng trong AI safety theory (1977, expanded 2003) về AI được giao task "tối đa hóa sản xuất paperclip" nhưng không có values, dẫn đến thảm họa (AI chuyển tất cả matter — kể cả humans — thành paperclips vì điều đó serve goal).

paperclip (project) **đặt tên theo vấn đề** — rồi claim solve vấn đề bằng governance layer (approval gates + budget hard-stops + audit log + manual override).

**Philosophical tension cho Storm Bear operator:**
- Storm Bear = Scrum Coach (serves human teams)
- paperclip = "Zero-human companies" (removes human teams)
- **Framing opposite.** Cần tách **architecture** (học được) khỏi **tagline** (không endorse).

Xem [[../02 Wiki/(C) Paperclip-Maximizer Framing + Alignment-Theory Surface]] chi tiết hơn.

### Quick stats
- ⭐ **55,900 stars** — 2nd largest trong corpus (chỉ sau build-your-own-x 491K)
- 🍴 9,500 forks
- 📜 MIT license
- 💻 TypeScript 97.4%
- 📦 2,264 commits / 6 releases / 1.1K open issues / 314 watchers
- 🏢 Author: "paperclipai" org (no individuals disclosed, no VC/LLC public)
- 🌐 Homepage: paperclip.ing
- 💬 Discord: discord.gg/m4HZY7xNG3

### Tier classification

**Tier 5 "Agent-as-application" entrant #3** — standalone autonomous agent orchestration. Peer: deer-flow (v9 T5 N=1) + autoresearch (v10 T5 N=2). paperclip **validates T5 at N=3** — first tier to reach N=3 (T1 at N=6 đã re-opened).

---

## Phần 2 — Tại sao nên (cẩn thận) quan tâm?

### Lý do engage

1. **Governance-as-architecture thesis** — 4 primitives + 5 invariants = kiến trúc hay, học được để dùng cho vault, workflows, own projects (KHÔNG cần adopt "zero-human" framing)
2. **BYO Agent adapter system** — multi-model architecture đáng học (Claude + Codex + Cursor + Bash + HTTP + OpenClaw ALL first-class)
3. **Full-stack monorepo** polish — engineering quality reference
4. **promptfoo eval integration** — first LLM eval framework trong corpus; pattern để adopt
5. **2nd largest scale in corpus** — 55.9K stars = worth understanding what got 55K people to star

### Lý do philosophical caution

1. **"Zero-human" framing** đối lập với Scrum coaching values
2. **MAXIMIZER MODE roadmap** = paperclip-maximizer reference; uncertain literal vs ironic
3. **No SAFETY.md** — architectural claim chưa được document thorough
4. **No disclosed backing** — khó đánh giá trustworthiness long-term

### Recommended stance cho Storm Bear operator

**Technical engagement OK, brand endorsement NOT recommended:**
- Study architecture, invariants, governance primitives
- Don't recommend paperclip to Scrum coaching clients
- Use insights for Storm Bear's OWN workflows (where you ARE the governance)
- Wait for paperclip team to disclose backing + SAFETY.md before production adoption

---

## Phần 3 — Cài đặt

### Yêu cầu

- Node.js 20+
- pnpm 9.15+
- Git

### Quick start (nhanh nhất)

```bash
npx paperclipai onboard --yes
```

CLI sẽ prompt bạn:
- Chọn bind mode: **loopback** (local single-user) / **lan** (LAN multi-device) / **tailnet** (Tailscale VPN remote)
- Configure company settings
- Set up first agent adapter

### Manual setup (development)

```bash
git clone https://github.com/paperclipai/paperclip.git
cd paperclip
pnpm install
pnpm dev
```

API server chạy tại `http://localhost:3100` với embedded PGlite (no external Postgres needed for dev).

### Verify

- Mở UI: http://localhost:3100 (hoặc port được config)
- Thấy dashboard với Company / Agents / Tickets / Budget = OK

### Ghi chú: "company" = đơn vị tenant

Mỗi paperclip install có thể host nhiều "companies" (Multi-Company feature với data isolation). Tạo company đầu tiên qua onboarding flow.

---

## Phần 4 — 9 features chính

### 1. 🔌 Bring Your Own Agent (BYO Agent)

Supports out-of-box:
- **OpenClaw** — companion standard với 3 runtime modes (join / docker-ui / sse-standalone)
- **Claude Code** (Anthropic)
- **Codex** (OpenAI)
- **Cursor** (IDE agent)
- **Bash** — ANY shell script as agent
- **HTTP endpoint** — ANY HTTP service as agent

Mỗi adapter plug vào paperclip orchestrator; paperclip không care underlying model.

### 2. 🎯 Goal Alignment

Mỗi task trace back to company mission. Không task orphan; tất cả trace về goal tree. **Alignment-theory response:** prevents agent goal drift.

### 3. 💓 Heartbeats

Scheduled/recurring execution. Không cần manual kickoff. Like cron but for agent tasks.

### 4. 💰 Cost Control

Per-agent budget với **hard-stops** — khi agent exceed budget, agent DỪNG ngay. Không "soft warning."

### 5. 🏢 Multi-Company

Complete data isolation giữa companies. Single install = N separate tenants.

### 6. 🎫 Ticket System

Agent work intake queue. Users hoặc Heartbeats tạo tickets; agents claim và execute.

### 7. 🛡️ Governance (4 primitives)

- **Approval gates** — defined checkpoints yêu cầu human review
- **Manual override** — pause hoặc terminate bất kỳ agent
- **Budget hard-stops** — cost enforcement architectural
- **Audit log** — immutable activity record

### 8. 📊 Org Chart

Hierarchical agent teams với roles + reporting lines. Giống corporate org chart.

### 9. 📱 Mobile Ready

Mobile-accessible UI (responsive hoặc native — unclear from README).

---

## Phần 5 — 5 Control-Plane Invariants (từ AGENTS.md)

Đây là "hiến pháp" của paperclip — preserve qua mọi code change:

| # | Invariant | Ý nghĩa |
|---|-----------|---------|
| 1 | **Single-assignee tasks** | 1 task chỉ có 1 agent. No race conditions. |
| 2 | **Atomic checkout** | Claim → execute → release. No partial states. |
| 3 | **Approval gates preserved** | Governance checkpoints survive refactoring |
| 4 | **Budget hard-stops** | Cost enforcement always active |
| 5 | **Activity logging** | Audit log never bypassed |

**Storm Bear vault lesson:** 5 invariants pattern applies to any orchestration system. Storm Bear routine có 2/5 tương tự (logging + budget implicit). Có thể add 3 còn lại vào routine v2.

---

## Phần 6 — "Zero-human companies" — honest assessment

### Những gì paperclip CLAIM

- Autonomous agents run 24/7 với human oversight (policy-level)
- Agents work "until task is done"
- Zero humans in operational loop (policy setup requires human)

### Những gì paperclip EXPLICITLY KHÔNG là

Từ README §"What Paperclip is not":
- **Not a single-agent tool** (requires team coordination)
- **Not a chatbot** (orchestration not conversation)
- **Not a replacement for humans in governance** (mission/policy requires humans)

### Reading

paperclip distinguishes:
- **Operational loop** (agents execute) → zero-human target
- **Governance loop** (humans set policy) → required, not automated

**"Zero-human companies"** = zero-human-in-operational-loop. Không nghĩa zero-human-in-governance.

### MAXIMIZER MODE roadmap item

Active development. "Higher autonomy within governance bounds." Explicit escalation of autonomy while banking on governance layer.

**Uncertain:** literal commitment vs ironic naming. Không có SAFETY.md để tell.

---

## Phần 7 — Adapter system + OpenClaw

### BYO Agent architecture (refactor in-flight)

Hiện tại: adapters hardcoded vào server binary.
Tương lai: runtime registration — plugin system contribute adapters.

### OpenClaw — companion standard

paperclip mention "OpenClaw" trong README tagline + có 3 smoke test modes:
- `smoke:openclaw-join` — join existing OpenClaw instance
- `smoke:openclaw-docker-ui` — Docker + UI mode
- `smoke:openclaw-sse-standalone` — standalone với Server-Sent Events

OpenClaw cross-referenced in:
- codymaster v12 README (install platform)
- gws v13 README Quickstart

→ OpenClaw = separate project/standard, not paperclip-internal.

### Hermes adapter externalization

AGENTS.md mentions fork (HenkDz/paperclip) externalizes Hermes adapter. Main repo likely follows. Hermes nature unclear (Nous Research? Internal?).

---

## Phần 8 — Tech stack + infrastructure

### Stack

- **Server:** Node 20+ / Express / Drizzle ORM
- **DB:** Embedded PGlite (dev) / External PostgreSQL (prod)
- **UI:** React
- **CLI:** TypeScript
- **Tests:** Vitest (unit) + Playwright (E2E + multi-user auth + release smoke)
- **LLM Evals:** promptfoo (first in Storm Bear corpus)
- **Monorepo:** pnpm workspaces
- **Deploy:** Docker (Dockerfile present)

### Release discipline

- **Canary channel** — bleeding edge (như BMAD `@next`)
- **Stable channel** — production (như BMAD `@latest`)
- **GitHub release artifact**
- **Rollback built-in** — `release:rollback` script

### Security signals

- SECURITY.md present
- `check:tokens` — forbidden tokens scan
- `secrets:migrate-inline-env` — secret management
- `.env.example` template

### Testing matrix

- Unit (Vitest)
- E2E single-user (Playwright)
- E2E multi-user authenticated (Playwright) — validates multi-tenancy
- Release smoke (Playwright)
- LLM evaluation (promptfoo)
- OpenClaw adapter smoke (3 modes)

**6 test categories = most comprehensive test posture in corpus.**

---

## Phần 9 — 4-week learning roadmap (cẩn thận ethical)

### Tuần 1: Understand (no install)

- Đọc README + AGENTS.md + ROADMAP.md + adapter-plugin.md
- Đọc [[../02 Wiki/(C) Paperclip-Maximizer Framing + Alignment-Theory Surface]] — philosophical context
- Decide: engage technically? (recommended yes) / brand-endorse? (recommended no)
- Watch any available demo video

**Goal:** understand vision + philosophical implications BEFORE install.

### Tuần 2: Local install + explore

- `npx paperclipai onboard --yes` (local loopback mode)
- Create 1 test "company" với simple goal
- Hire 1 agent (Claude Code adapter easiest cho VN Claude Code users)
- Create 3 test tickets và observe workflow
- Check audit log, budget tracking, approval gates

**Goal:** empirical feel cho architecture. Decide tiếp theo dựa trên real UX.

### Tuần 3: Architecture extraction

- Map 5 invariants to Storm Bear vault concepts
- Consider: apply governance primitives to own workflows?
- Extract adapter pattern for any future Storm Bear multi-agent work
- Document learnings in `04 Reviews/paperclip-architecture-notes.md`

**Goal:** transferable patterns without brand adoption.

### Tuần 4: Decision + documentation

- Empirical verdict: is paperclip useful tool for YOUR workflows?
- Recommended uses (if yes): personal ops orchestration / own task tracking / experimental multi-agent research
- NOT recommended: client coaching engagements / Scrum team automation (philosophical mismatch)
- Document final stance in `04 Reviews/paperclip-engagement-decision.md`

**Goal:** empirical + ethical clarity on paperclip engagement level.

---

## Phần 10 — So sánh với T5 peers

| Aspect | deer-flow (v9) | autoresearch (v10) | paperclip (v14) |
|--------|----------------|---------------------|------------------|
| **Stars** | 62K | 74K | **55.9K** |
| **Backer** | ByteDance corporate | Karpathy solo | **paperclipai org (unclear)** |
| **Scope** | SuperAgent harness generalist | ML research specialist | **Company-scale orchestration generalist** |
| **Framing** | Long-horizon tasks | Autonomous experiments | **"Zero-human companies"** |
| **Alignment stance** | Implicit | Implicit (Karpathy-aware) | **Explicit (Bostrom reference)** |
| **Language** | Python + Next.js | Python minimalist | **TypeScript monorepo** |
| **Governance** | Implicit | val_bpb implicit goal | **Explicit 4 primitives + 5 invariants** |
| **Multi-tenant** | ❌ | ❌ | **✅ Multi-Company** |
| **Testing** | Moderate | Minimal | **6-category matrix** |
| **Skill count** | Skill System progressive | 1 mega-skill | **4 meta-skills + BYO agents** |

### Khi nào dùng cái nào?

- **Long-horizon general tasks** → deer-flow (T5 N=1)
- **ML research experiments** → autoresearch (T5 N=2)
- **Company-scale agent orchestration with governance** → paperclip (T5 N=3) — with ethical caution

Xem chi tiết: [[(C) Tier 5 3-way comparison]]

---

## Next actions cho người mới

1. **Đọc** README + philosophical framing entity (~30 min) — TRƯỚC install
2. **Quyết định** engagement level: (a) understand only / (b) technical pilot / (c) production use
3. **Nếu (b) technical pilot:** local install + 1-week exploration + document learnings
4. **Nếu (c) production:** đợi SAFETY.md + backing disclosure
5. **Always:** tách architecture learnings (adopt) từ "zero-human" framing (don't adopt)

### Khi cần help

- Discord: discord.gg/m4HZY7xNG3
- GitHub issues: github.com/paperclipai/paperclip/issues (1.1K open)
- GitHub Discussions: ideas + RFCs
- Plugin registry: awesome-paperclip (github)
- Storm Bear vault: [[(C) index]] — this wiki + 4 entity pages + 3 summaries

---

## Appendix A — Vocabulary VN/EN

| EN | VN | Note |
|----|-----|------|
| Company | Company | paperclip term for tenant |
| Agent | Agent | Giữ nguyên |
| Heartbeat | Heartbeat | Scheduled execution |
| Ticket | Ticket | Work intake unit |
| Governance | Governance | Control layer |
| Approval gate | Cổng phê duyệt | OK to localize |
| Budget hard-stop | Budget hard-stop | Technical term |
| Audit log | Audit log | Technical term |
| Adapter | Adapter | Technical term |
| BYO Agent | BYO Agent | Marketing term |
| MAXIMIZER MODE | MAXIMIZER MODE | Reference to paperclip-maximizer |
| Paperclip maximizer | Paperclip maximizer | AI safety theory term |
| Alignment | Alignment | AI safety theory term |
| Zero-human companies | Zero-human companies | Keep EN — loaded term |

## Appendix B — Quick reference

### Install
```bash
npx paperclipai onboard --yes                # quick
git clone ... && pnpm install && pnpm dev    # dev
```

### Core concepts
- **Company** = tenant (paperclip hosts N companies)
- **Agent** = any adapter (Claude/Codex/Cursor/Bash/HTTP/OpenClaw)
- **Ticket** = work unit
- **Heartbeat** = scheduled trigger
- **Budget** = cost limit per agent
- **Approval gate** = human checkpoint

### 5 invariants (AGENTS.md)
1. Single-assignee tasks
2. Atomic checkout
3. Approval gates preserved
4. Budget hard-stops
5. Activity logging

### 4 governance primitives (README)
1. Approval gates
2. Manual override
3. Budget hard-stops
4. Audit log

### 9 features (README)
BYO Agent / Goal Alignment / Heartbeats / Cost Control / Multi-Company / Ticket System / Governance / Org Chart / Mobile Ready

---

## Cross-references

- Parent wiki: [[../02 Wiki/(C) index]]
- Entity pages:
  - [[../02 Wiki/(C) Zero-Human Companies Orchestration + Governance Layer]]
  - [[../02 Wiki/(C) BYO Agent Adapter System + OpenClaw Standard]]
  - [[../02 Wiki/(C) Paperclip-Maximizer Framing + Alignment-Theory Surface]]
  - [[../02 Wiki/(C) T5 3-Way Validation + Community-Platform Archetype Hypothesis]]
- Comparison: [[(C) Tier 5 3-way comparison]]
- T5 peers:
  - `../../deer-flow - Beginner Analysis/03 Published/` (v9)
  - `../../autoresearch - Beginner Analysis/03 Published/` (v10)
- Philosophical opposite: `../../BMAD-METHOD - Beginner Analysis/` (v11)

---

**🐻 Storm Bear ethical note:** paperclip's architecture is worth studying. Its "zero-human companies" framing is NOT worth endorsing from a Scrum coach position. Separate technical learning from brand adoption. Use governance-as-architecture patterns for YOUR OWN workflows where you remain in governance.
