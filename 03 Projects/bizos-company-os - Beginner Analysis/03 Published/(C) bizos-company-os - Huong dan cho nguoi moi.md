# (C) bizos-company-os — Hướng dẫn cho người mới / Beginner guide

> **Bilingual:** VN chính + EN kỹ thuật (parallel). Target: Vietnamese OR English developer / founder / Scrum coach / product manager evaluating `ungden/bizos-company-os` at cold-start (2-day-old, 18 stars, 2026-04 snapshot).
>
> **Written:** 2026-04-24 based on v37 wiki analysis. 22 open questions in `01 Analysis/(C) open questions.md`.

---

## ⚠️ ĐỌC TRƯỚC / READ THIS FIRST

**VN:**
Dự án này **KHÔNG có file LICENSE**. README tuyên bố là "Proprietary — Alex Le · Titan Labs" với lời nói "xem code thoải mái, fork để học". Nhưng **README không phải là LICENSE**.

Theo luật bản quyền mặc định (Mỹ + quốc tế):
- Không có LICENSE = **All rights reserved** (toàn quyền thuộc tác giả)
- Bạn **CÓ** thể xem code trên GitHub
- Bạn **KHÔNG CÓ** quyền:
  - Fork và deploy production (thậm chí cho nội bộ công ty bạn)
  - Copy code vào project khác
  - Publish một phiên bản chỉnh sửa
  - Dùng cho mục đích thương mại

**Lời mời của README "Deploy production / tuỳ biến cho công ty → email alexle@titanlabs.vn"** = channel thương mại qua email. Nếu muốn dùng thật sự, phải email Alex Le trước.

**EN:**
This project has **NO LICENSE file**. README declares "Proprietary — Alex Le · Titan Labs" with "view code freely, fork to learn" language. **But README is NOT a LICENSE.**

Under default US/international copyright:
- No LICENSE = **all rights reserved**
- You MAY view code on GitHub
- You MAY NOT:
  - Fork and deploy production (even for your own internal company)
  - Copy code into other projects
  - Publish a modified version
  - Use commercially

The README offer "Deploy production / custom for company → email alexle@titanlabs.vn" is the commercial channel. For real use, email Alex Le first.

---

## Part 1 · Bizos là gì / What is bizos

**VN:** Bizos ("Business Operating System") là một ứng dụng web nội bộ cho công ty, xây trên Next.js 16 + Supabase, với 19 màn hình + 64 bảng cơ sở dữ liệu + quản trị KPI phân cấp + engine tính lương thưởng + P&L / Balance Sheet / Cash Flow + what-if Forecast + OKR + Audit log + Recruiting + Knowledge (SOP/Playbook). Tác giả: **Alex Le** (Titan Labs, Việt Nam).

Tag-line cốt lõi: **Task → KPI cá nhân → KPI phòng ban → KPI công ty → Tài chính.** Mọi task hằng ngày được nối thẳng vào KPI, lên KPI phòng, lên KPI công ty, xuống payroll, vào P&L, và cuối cùng chạy Forecast "nếu KPI giảm 20% thì Net Profit còn bao nhiêu."

**EN:** Bizos ("Business Operating System") is an internal company web-app built on Next.js 16 + Supabase, with 19 screens + 64 DB tables + hierarchical KPI management + compensation rule engine + P&L / Balance Sheet / Cash Flow + what-if Forecast + OKRs + Audit log + Recruiting + Knowledge. Author: **Alex Le** (Titan Labs, Vietnam).

Core tagline: **Task → personal KPI → team KPI → company KPI → Financials.** Every daily task wires into KPI, rolls up to dept, rolls up to company, flows to payroll, lands in P&L, and finally runs Forecast "if KPI drops 20%, what's Net Profit?"

**Scale at wiki-build time:** 18 stars / 25 forks / 2 days old. Cold-start.

## Part 2 · Tại sao có thể interesting / Why it might be interesting

**Cho ai:**
- **Founder / CEO** công ty nhỏ (10-100 người) muốn dashboard unified thay vì 5-7 SaaS riêng
- **HR / CFO** muốn engine payroll tự động dựa trên KPI completion
- **Developer / Product manager** muốn reference implementation cho business app Next.js 16 + Supabase
- **Scrum coach** (Storm Bear operator) muốn study VN-peer-archetype + Claude-Code-built production
- **VN tech community** muốn xem framework bản địa với bilingual VN+EN + labor-law VN (BHXH) hardcoded

**Cho ai KHÔNG phù hợp:**
- Enterprise với >100 employees và compliance gắt (bizos không có SOC2, không có audit trail đủ depth cho Big 4)
- Non-VN companies (payroll rules hardcode VN BHXH — 10% nhân viên + 23.5% công ty)
- Companies cần hard multi-tenant SaaS isolation (RLS là good baseline, nhưng chưa battle-tested ở scale)
- Anyone needing production immediately — **cần email Alex Le trước** cho custom deployment

## Part 3 · Thử demo trong 5 phút / 5-minute demo

**VN + EN:**

```bash
# 1. Clone
git clone https://github.com/ungden/bizos-company-os
cd bizos-company-os

# 2. Install (requires pnpm; if missing: corepack enable && corepack prepare pnpm@10 --activate)
pnpm install

# 3. Dev
pnpm dev

# 4. Mở http://localhost:3000
# App redirect về /login → /login stub accept any email → browse 19 screens
```

**Không có Supabase? Không sao!** App tự bật **Demo mode** với:
- 14 nhân viên mẫu
- 14 KPI (4-level cascade)
- Payroll, accounting, alerts, approvals mẫu
- Tất cả 19 screens render đầy đủ — chỉ nút CRUD (Create/Update/Delete) bị no-op

**No Supabase? No problem!** App auto-enables **Demo mode** with 14 sample employees + 14 KPIs + payroll + accounting + alerts + approvals. All 19 screens render end-to-end — only CRUD buttons are no-ops.

## Part 4 · 19 màn hình — tour nhanh / 19 screens tour

| # | Route | Mục đích (VN) | Purpose (EN) |
|---|-------|---------------|--------------|
| 01 | `/dashboard` | 30 giây hiểu công ty | 30-sec company snapshot |
| 02 | `/org` | Sơ đồ tổ chức reactflow | Reactflow org chart |
| 03 | `/departments` | Phòng ban = cost center + KPI center | Departments as cost+KPI centers |
| 04 | `/people` | Nhân sự directory | Employee directory |
| 05 | `/kpi` | KPI tree 4 cấp + status coloring | 4-level KPI tree + status colors |
| 06 | `/operations` | Task board gắn `linked_kpi_id` | Task board with linked_kpi_id |
| 07 | `/compensation` | Payroll + Incentive Simulator | Payroll + Incentive Simulator |
| 08 | `/projects` | Milestones + ROI | Milestones + ROI |
| 09 | `/finance` | P&L + BS + CF | P&L + Balance Sheet + Cash Flow |
| 10 | `/settings` | Config công ty | Company config |
| 11 | `/reports` | Report Center | Reports |
| 12 | `/alerts` | Alert rules + severities | Alerts |
| 13 | `/approvals` | Multi-step approvals | Approvals |
| 14 | `/audit` | Audit log append-only | Audit log |
| 15 | `/okr` | Objectives + key_results | OKRs |
| 16 | `/forecast` | **What-if simulator** | **What-if simulator** |
| 17 | `/recruiting` | Job requisitions + pipeline | Recruiting |
| 18 | `/knowledge` | SOP / Playbook / Checklists | Knowledge |
| 19 | `/profile` | Tài khoản cá nhân | Personal account |
| 20 | `/guide` | **Tutorial trong app bilingual** | **In-app bilingual tutorial** |

**Top khám phá ưu tiên:** `/guide` (đọc trước, 800 lines VN+EN) → `/dashboard` → `/kpi` → `/forecast` → `/compensation`.

## Part 5 · Stack

**VN + EN:**
- **Next.js 16.2.4** (App Router + Server Components + Server Actions) — **first corpus wiki on stable Next 16**
- **React 19.2.4** + TypeScript
- **Tailwind CSS v4** + shadcn-style UI primitives
- **Supabase** (Postgres + Auth + Storage + RLS) via `@supabase/ssr`
- **Reactflow** (org chart + KPI tree) + **Recharts** (line/bar/donut/sparkline)
- **React Hook Form + Zod** cho validation
- **TanStack Table** cho data grid
- Deploy: Vercel / Railway / Docker / local

**Breaking change quan trọng Next 16:** `middleware.ts` đổi tên thành `proxy.ts` ở root. AGENTS.md có cảnh báo AI coding agents về training-data drift.

## Part 6 · Setup Supabase (nếu muốn run production)

**VN + EN:**

```bash
# 1. Create Supabase project at https://app.supabase.com
# 2. SQL Editor → run in order:
#    - db/schema.sql    (64 tables + enums + triggers)
#    - db/policies.sql  (RLS cho 7 role)
#    - db/seed.sql      (BIZOS Demo company)

# 3. Authentication → Users → Add user:
#    - ceo@bizos.demo
#    - hr@bizos.demo
#    - cfo@bizos.demo
#    - sales.head@bizos.demo

# 4. Link auth users to employees:
update employees set auth_user_id = '<auth-id>' where email = 'ceo@bizos.demo';
insert into user_roles (auth_user_id, company_id, role)
values ('<ceo-auth-id>', '00000000-0000-0000-0000-00000000c001', 'ceo');

# 5. Copy anon + service_role key to .env.local:
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...
NEXT_PUBLIC_APP_URL=http://localhost:3000
```

**⚠️ Quan trọng:** Trước khi chạy production, **email alexle@titanlabs.vn để xin permission** (vì project không có LICENSE).

**Important:** Before production use, **email alexle@titanlabs.vn for permission** (no LICENSE file).

## Part 7 · Lộ trình học 2 tuần / 2-week evaluation roadmap

### Tuần 1 — Khám phá / Week 1 — Exploration (6-8h)

**Day 1-2 (2h):** Clone + `pnpm install && pnpm dev` → browse all 19 screens ở demo mode. Đọc `/guide` (800 lines). Screenshots of các pattern bạn thích.

**Day 3-4 (2h):** Read `README.md` + `db/schema.sql` (64 tables, scan headers). Đọc source: `lib/kpi/formulaEngine.ts` (81 lines) + `lib/kpi/cascade.ts` (93 lines) + `lib/compensation/ruleEngine.ts` (100 lines). 

**Day 5-7 (2-4h):** Setup Supabase theo Part 6. Tạo 3-4 user test. Try create KPI, assign task, run forecast simulator. Ghi nhận 10 câu hỏi nảy sinh.

### Tuần 2 — Đánh giá / Week 2 — Assessment (4-6h)

**Day 8-10 (2h):** Mapping bizos features vs your company needs. Nếu có gap, viết list.

**Day 11-12 (2h):** Email Alex Le (`alexle@titanlabs.vn`) if considering production use:
- Hỏi custom deployment cost / engagement model
- Hỏi roadmap: có thay đổi gì trong 3-6 tháng?
- Share gap list (nếu có)

**Day 13-14 (0-2h):** Quyết định:
- **Pilot:** Email Alex Le, negotiate custom-deployment, setup staging
- **Reference only:** Giữ bizos như reference architecture, build own system
- **Skip:** Cần nhiều feature hoặc compliance không có trong bizos

## Part 8 · Ethical framing / Đạo đức

**VN:**
- Clone + đọc code + học pattern = OK (goodwill tolerated per README)
- Fork về private để thử demo 2 tuần = gray zone (GitHub ToS cho phép fork, nhưng long-term giữ fork mà không liên hệ → legal gray)
- Deploy production mà không email = **KHÔNG OK** (copyright infringement risk)
- Copy code vào project khác = **KHÔNG OK** (không có license cho quyền này)
- Derivative work (bizos-for-my-startup) = **KHÔNG OK** (cần permission viết)

**EN:**
- Clone + read code + study patterns = OK (goodwill tolerated per README)
- Fork private for 2-week demo = gray zone (ToS allows, long-term risk)
- Production deploy without email = **NOT OK** (infringement risk)
- Copy code into other projects = **NOT OK** (no license granted)
- Derivative work = **NOT OK** (explicit permission required)

**Khi nào OK:** Email Alex Le với:
- Mục đích sử dụng cụ thể
- Scope deployment (nội bộ / client / SaaS)
- Mức độ tùy biến cần thiết
- Budget và timeline

Alex Le English/Vietnamese OK per README.

## Part 9 · Storm Bear relevance / Liên quan đến Storm Bear

**Cho Storm Bear operator (VN Scrum coach):**

**Giá trị trực tiếp: TRUNG BÌNH**
- Bizos là business-OS chung, không phải Scrum-specific tool
- 64-table schema quá lớn cho Scrum coaching practice
- Tính năng compensation + BHXH không liên quan Scrum
- **Không phải pilot ưu tiên**

**Giá trị tham khảo: CAO**
- Alex Le là VN solo developer peer-archetype (giống Storm Bear operator)
- Inferred là Claude-Code-built → proof-of-concept cho "VN dev ship production software with AI"
- KPI cascade + formula AST + rule engine = reusable architectural patterns
- i18n VN+EN first-class deployment = reference for Storm Bear tương lai khi có public product
- Absent-LICENSE cautionary case study for Storm Bear's own license decision

**Action item:**
1. Study bizos 2-3 tuần (đã đề xuất ở Part 7)
2. Consider email Alex Le cho peer-exchange VN tech (không phải commercial)
3. Nếu Storm Bear build Scrum-coach agent sau này, copy pattern (KPI cascade + bilingual + demo-fallback UX)

## Part 10 · Corpus-firsts (thống kê wiki)

Bizos đóng góp những cái "đầu tiên trong Storm Bear corpus":
1. Cold-start snapshot wiki subject (2 ngày tuổi)
2. Absent-LICENSE file wiki
3. Fork > Star inverted ratio (138%)
4. Apparent Claude-Code-built production artifact subject
5. VN-in-VN outside-scope tier (trước đây VN chỉ ở T1)
6. Business-OS-as-product 7th outside-scope sub-type
7. 64-table business-domain relational schema
8. 7-role RBAC + SQL scope-function helpers
9. JSONB AST business-formula engine (10 operators)
10. 5-tier bonus thresholds + team/company multipliers
11. VN labor-law hardcoded assumptions (10% + 23.5% BHXH)
12. Demo-fallback safeFetch pattern
13. Next.js 16 stable wiki (middleware → proxy.ts)
14. In-app bilingual tutorial (`/guide` 800 lines TSX)

## Part 11 · Tradeoffs + giới hạn / Tradeoffs + limitations

**Pros:**
- ✅ Production-ready UI across 19 screens
- ✅ Zero-friction demo mode (no Supabase needed for evaluation)
- ✅ Bilingual VN+EN shipped day-1
- ✅ Comprehensive 64-table schema with multi-tenant RLS
- ✅ Clear domain methodology (KPI cascade)

**Cons:**
- ❌ No LICENSE file = legal gray zone for any real use
- ❌ 18 stars / 7 commits = cold-start (unproven at scale)
- ❌ Zero tests = quality unverified
- ❌ VN labor-law hardcoded (non-VN requires rewrite)
- ❌ Email-gated commercial = not self-serve
- ❌ No CI / no observability / no benchmarks
- ❌ Solo maintainer bus factor = 1

**Acceptable-if-you're-OK-with:**
- Small company (10-100) in Vietnam
- Willing to email Alex Le and pay for deployment
- Accepting Titan Labs ongoing vendor relationship

## Part 12 · Câu hỏi cần trả lời trước khi pilot / Questions before piloting

1. Do you need 64-table comprehensiveness OR just 8-15 core tables?
2. Is Vietnam BHXH hardcoding acceptable, or need multi-country tax engine?
3. Can you afford ongoing vendor relationship with Titan Labs (support + updates)?
4. Does absent-LICENSE block your compliance / legal review?
5. Are you willing to invest time understanding 4-level KPI cascade design?
6. Do you have design/product resources to customize 19 screens to your needs?
7. What's your fallback if Alex Le stops supporting (bus factor mitigation)?

If answers are mostly NO → don't pilot bizos, either build own or use established SaaS (Workday, BambooHR, Synergita, etc.).

## Part 13 · Tiếp theo / Next

**Nếu bạn interested:**
1. Clone và chạy demo mode (5 phút) — validate UX fit
2. Đọc `/guide` (800 lines) — understand full scope
3. Email Alex Le (`alexle@titanlabs.vn`) — initiate commercial conversation

**Nếu bạn chỉ muốn học:**
1. Clone và đọc source (4-8h)
2. Focus: `lib/kpi/*.ts` + `db/schema.sql` + `app/(app)/forecast/page.tsx`
3. Tài liệu đi kèm: [v37 wiki analysis folder] (this wiki — Alex Le + Titan Labs entity + Engines entity)

**Nếu bạn là VN tech community:**
1. Give Alex Le a star (currently 18 — visibility boost is low-cost)
2. Optional: donation PayPal `sai211dn@gmail.com`
3. Follow for ecosystem development (cold-start → where does this go?)

**Nếu bạn là Storm Bear operator (v27 diagnostic HIGH context):**
1. Prioritize v27 diagnostic HIGH bundle execution before v38 (14 sessions deferred — critical)
2. Use bizos as **reference** not pilot (pattern #4 VN peer-archetype validated)
3. Consider Alex Le as potential peer-exchange contact (VN tech community cross-connection; not commercial)

---

*Cảm ơn Alex Le cho cold-start snapshot transparency. Bizos v37 là wiki thứ 37 trong Storm Bear corpus.*

*Thanks Alex Le for cold-start snapshot transparency. Bizos v37 is the 37th wiki in Storm Bear corpus.*

**Sources:** This guide builds on `02 Wiki/` cluster summaries (3) + entity pages (4) + open questions (22). See `CLAUDE.md` for Phase 0 classification + pattern pre-check.
