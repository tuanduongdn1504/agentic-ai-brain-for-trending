# (C) Cluster — User-facing README + /guide page + 19 screens

**Sources:** `README.md` (220 lines, VN+EN bilingual) + `app/(app)/guide/page.tsx` (800 lines VN+EN) + `mockups/` (19 PNG designs) + `lib/i18n/dict.ts` (626 entries) + `lib/nav.ts` (20 menu items)

## 1. Positioning (verbatim README)

> **EN:** "Company OS: **Task → personal KPI → team KPI → company KPI → Financials.** A Next.js + Supabase business-operating system — 19 production-grade screens, KPI cascade, compensation rule engine, P&L/BS/CF, what-if Forecast, OKRs, Audit, SOPs."
>
> **VI:** "Hệ thống vận hành công ty: **Task → KPI cá nhân → KPI phòng ban → KPI công ty → Tài chính.**"
>
> By **Alex Le** · `alexle@titanlabs.vn` · [titanlabs.vn](https://titanlabs.vn)
> Donate: PayPal (sai211dn@gmail.com)
> Custom deployment: email alexle@titanlabs.vn (VN/EN welcomed)
> Live demo: https://bizos-company-os.vercel.app
> Full /guide: https://bizos-company-os.vercel.app/guide

## 2. Core logic chain (README verbatim)

```
Task hằng ngày
  → Output cá nhân
    → KPI cá nhân
      → KPI team / phòng ban
        → KPI công ty
          → Doanh thu / Chi phí / Lợi nhuận / Dòng tiền
```

> "Mỗi bước đều truy vết được. Đổi 1 KPI lá ở **Forecast** sẽ thấy tác động lên Net Profit ngay lập tức."

**Translation:** Every step traceable. Change a leaf KPI at /forecast and immediately see impact on Net Profit.

## 3. 19 screens (navigation order)

| # | Route | Menu (VN → EN) | Purpose |
|---|-------|----------------|---------|
| 01 | `/dashboard` | Dashboard | 30-sec company snapshot — 6 KPI cards + hero donut + revenue trend + AI insight cards |
| 02 | `/org` | Sơ đồ tổ chức → Org chart | Reactflow node-edge tree + headcount-by-department |
| 03 | `/departments` | Phòng ban → Departments | Cost-center + KPI-center per department |
| 04 | `/people` | Nhân sự → People | Employee directory + per-person profile + skill matrix |
| 05 | `/kpi` | KPI Tree | 4-level cascade (company → dept → team → employee) + status coloring |
| 06 | `/operations` | Công việc → Operations | Task board with `linked_kpi_id` + SLA + task-to-KPI mapping |
| 07 | `/compensation` | Lương thưởng → Compensation | Payroll + Incentive Simulator + 5-tier bonus threshold |
| 08 | `/projects` | Dự án → Projects | Milestones + ROI tracking + project_budgets |
| 09 | `/finance` | Tài chính → Finance | P&L + Balance Sheet + Cash flow + budget + cost centers |
| 10 | `/settings` | Cài đặt → Settings | Company config + roles + imports + bonus rules |
| 11 | `/reports` | Báo cáo → Reports | Report center (schedules + exports) |
| 12 | `/alerts` | Cảnh báo → Alerts | Alert rules + severities (info/warning/danger/critical) |
| 13 | `/approvals` | Phê duyệt → Approvals | Multi-step approvals (bonus / budget / hiring) |
| 14 | `/audit` | Audit log | Append-only trail (last 100 entries) |
| 15 | `/okr` | Mục tiêu OKR → OKRs | Objectives + key_results + cascade alignments |
| 16 | `/forecast` | Forecast | **What-if simulator** — change a leaf KPI %, propagate through tree, see Net Profit delta |
| 17 | `/recruiting` | Tuyển dụng → Recruiting | Job requisitions + candidates + skill gap |
| 18 | `/knowledge` | SOP / Playbook | sop_documents + playbooks + checklists |
| 19 | `/profile` | Tài khoản → Account | Per-user account page |
| (20) | `/settings` | (menu item 10) | — |
| (21) | `/guide` | Hướng dẫn → Guide | **Corpus-first: in-app bilingual tutorial page covering all 19 screens + 3 workflows + tips** (800 lines TSX) |

## 4. 3 role-based quick-start flows (README)

**CEO / Founder:**
1. Open `/dashboard` every morning (30-sec understanding)
2. Red KPIs on `/kpi` → click for owner + actual data source
3. `/forecast` run what-if: "If Sales drops 20%, what's Net Profit?"
4. `/approvals` approve bonus / budget / hiring

**HR Admin:**
1. `/people` manage employee directory
2. `/compensation` run payroll + view Incentive Simulator
3. `/recruiting` track candidate pipeline + skill gap

**Department Head:**
1. `/departments/:id` view dept KPI + tasks + budget
2. `/operations` assign tasks + attach `linked_kpi_id`
3. `/okr` cascade quarterly objectives down to team

## 5. End-to-end workflow (README verbatim)

```
Task (/operations) → KPI cá nhân (/people/:id)
  → KPI phòng ban (/departments/:id)
    → KPI công ty (/kpi)
      → Payroll (/compensation, chạy rule engine)
        → Tài chính (/finance: P&L · BS · CF)
          → Forecast what-if (/forecast)
```

## 6. /guide page — corpus-first in-app tutorial

- **800 lines TSX** with `tServer()` i18n
- **Per-screen sections:** summary + 5-bullet howto in both VN+EN
- **3 end-to-end workflows documented:** (a) Task → KPI → Finance, (b) Month-end payroll, (c) First-time company setup
- **4 "tips" cards:** Demo mode / RLS multi-tenant / KPI formula AST / Compensation tiers
- **3-step "quick start":** SETUP → DESIGN KPI → OPERATE
- **Philosophy section:** "Không phải HRM, không phải BI dashboard đơn thuần. BIZOS là Business Operating System — nơi mọi task hằng ngày, KPI, lương thưởng và tài chính đều được nối vào một chuỗi logic thống nhất"

**Corpus-first observation:** First wiki-subject in Storm Bear corpus with in-app bilingual tutorial as a first-class screen (`/guide` is menu item 21 in nav). Contrast with external docs sites (spec-kit v17 github.io) or inline README-only docs.

## 7. i18n first-class (626 dict entries)

- `lib/i18n/dict.ts` — 626 key-value entries, each with `{ vi, en }`
- Locale switcher in top bar (Sidebar + Topbar components)
- `DEFAULT_LOCALE = "vi"` (VN-primary)
- Scope: all UI strings, status labels, menu items, error messages, tips, philosophy, howto steps
- Pattern #22 AGENTS.md strengthening: bizos ships VN-first application with full bilingual depth — **first outside-scope wiki with this depth**

## 8. Demo mode fallback

- **Without Supabase env:** App auto-enables Demo mode
- Ships 14 sample employees + 14 KPIs + payroll + accounting data
- All 19 screens render; CRUD buttons are no-ops
- Data source: `lib/queries/demo.ts` (21KB)
- Fallback mechanism: `safeFetch` in `lib/queries/index.ts` — Supabase query OR demo data on empty/error
- **Implication:** Zero-friction evaluation — clone, `pnpm install && pnpm dev`, browse all 19 screens in 5 minutes

## 9. Tech stack (README verbatim)

- **Next.js 16** (App Router · Server Components · Server Actions) + TypeScript
- **Tailwind CSS v4** + UI primitives (shadcn-style) + `lucide-react`
- **Recharts** (line · bar · donut · sparkline) + **reactflow** (Org chart, KPI tree)
- **Supabase** (Postgres · Auth · Storage · RLS) via `@supabase/ssr`
- React Hook Form + Zod · TanStack Table
- Deploy: Vercel or Railway (Dockerfile), Supabase managed cloud
- package.json: Next 16.2.4, React 19.2.4, @supabase/ssr 0.10.2, reactflow 11.11.4, recharts 3.8.1, zod 4.3.6

**Next.js 16 notes:** middleware → `proxy.ts` rename (corpus-first observation of breaking change).

## 10. Project roadmap (README)

All 11 phases marked ✅:
- P0 Bootstrap + shell + 19-page scaffold + schema + RLS + seed
- P1 Org + Department + People CRUD (demo data, live CRUD when Supabase live)
- P2 KPI formula engine + OKR + cascade + integrity checker
- P3 Operations — task board + SLA + task-to-KPI mapping
- P4 Compensation — rule engine + payroll + simulator
- P5 Projects — milestones + ROI
- P6 Finance — P&L + BS + CF + Budget + Cost center
- P7 Dashboard intelligence + Forecast simulator
- P8 Reports + Alerts + Approvals + Audit Log
- P9 Recruiting + SOP / Knowledge
- P10 Polish + Vercel production deploy

## 11. Donation + commercial CTA

- PayPal: sai211dn@gmail.com
- Custom deployment via email: alexle@titanlabs.vn (VN/EN)
- Pattern: donation-funded-OSS + commercial-consulting-gate (similar to Pattern #27 Community-Viral variants but at cold-start)

## 12. License statement (README only, NO LICENSE file)

> "Proprietary — **Alex Le · Titan Labs**. Xem code thoải mái, fork để học. Deploy production / tuỳ biến cho công ty → email `alexle@titanlabs.vn`."

**Translation:** "Proprietary — Alex Le · Titan Labs. View code freely, fork to learn. Production deploy / customize for your company → email alexle@titanlabs.vn."

**Corpus-first observation:** FIRST absent-LICENSE-file wiki in Storm Bear corpus. GitHub UI reads as "No license" — default US/intl copyright → all rights reserved → **legally**, forking to deploy commercially would require Alex Le's explicit written permission. README statement says "fork to learn" but has no legal force (README != LICENSE).

## 13. Key absences (counter-evidence observations)

- **No LICENSE file** — contrast with 35 prior corpus wikis all of which have LICENSE (MIT / Apache / GPL / AGPL / PolyForm / custom non-OSI)
- **No release tags** — cold-start posture; `v0.1.0` in package.json but no GitHub release
- **No CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT.md** — single governance file (AGENTS.md 327B, CLAUDE.md pointer)
- **No test files visible** — ships with no pytest/vitest/playwright harness
- **No CI visible in repo** — `.github/` absent; likely Vercel auto-deploy only
- **No MCP / agent primitives** — zero commands, hooks, skills, agents
- **English-primary docs in beginner-guide precedent absent** — VN-primary throughout (contrast most corpus wikis EN-primary with VN-translation-second)

## 14. 15+ corpus-firsts candidate list

1. In-app bilingual tutorial page (/guide) as first-class screen
2. Absent-LICENSE-file wiki
3. 2-day-old cold-start wiki subject (youngest in corpus — beats awesome-design-md v25 20-day age)
4. 18-star wiki subject (smallest by ~2× — codymaster v12 was 38 stars)
5. Fork>Star ratio 138% (25/18) — template-use posture
6. VN solo-developer at outside-scope tier
7. Next.js 16 production-grade showcase (first corpus wiki on Next 16)
8. Business-OS-as-product content genre (7th outside-scope sub-type candidate)
9. KPI-cascade domain methodology (not agent methodology)
10. 64 DB tables with multi-tenant RLS in corpus outside-scope
11. 7-role RBAC matrix (ceo/cfo/hr_admin/dept_head/team_lead/employee/auditor) — most-detailed RBAC in corpus
12. JSONB AST formula engine with 10 operators
13. 5-tier bonus threshold rule engine + team + company multipliers
14. Demo-fallback safeFetch pattern (zero-friction evaluation UX)
15. Next 16 middleware → `proxy.ts` rename (first corpus docs of this convention)

## 15. Cross-wiki echo

- **v12 codymaster** — closest VN peer (Tody Le = VN-in-VN at T1; Alex Le = VN-in-VN at outside-scope)
- **v32 claude-howto** — Luong Nguyen VN-diaspora T1 (complement pair to codymaster; bizos is 3rd VN entrant in corpus but first cross-tier)
- **v34 claude-code-best-practice** — Shayan Rais 47.4K aggregator T1 (bizos 18-star cold-start = opposite scale pole; same solo-non-US archetype structure)
- **v25 awesome-design-md** — 20-day age prior youngest (bizos 2-day is new youngest)
- **v36 pi-mono** — YELLOW precedent (scope-compression methodology inherited)
