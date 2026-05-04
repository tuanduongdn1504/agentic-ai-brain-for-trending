# (C) BIZOS core product — 19-screen business OS + KPI cascade

**Cross-references:** Cluster 1 (User-facing README + /guide + 19 screens) + Cluster 3 (Technical engines) | Pattern #22 AGENTS.md strengthening | Pattern #29 License-Category-Diversity strengthening | v12 codymaster (VN-in-VN peer) | v32 claude-howto (VN-diaspora peer) | v36 pi-mono (YELLOW precedent)

## 1. One-sentence identity

BIZOS ("Business Operating System") is a Next.js 16 + Supabase cold-start business application (18 stars, 2 days old) that wires a company's daily tasks into a **4-level KPI cascade (task → personal → team → company) terminating in P&L / Balance Sheet / Cash Flow / what-if Forecast**, with compensation-rule-engine + OKR + audit built in — shipped by Alex Le (Titan Labs, VN) as VN-primary + EN-secondary bilingual across 19 screens.

## 2. Positioning (verbatim, VN+EN)

> **VN:** "Hệ thống vận hành công ty: Task → KPI cá nhân → KPI phòng ban → KPI công ty → Tài chính."
> **EN:** "Company OS: Task → personal KPI → team KPI → company KPI → Financials."
> (/guide page philosophy): "Không phải HRM, không phải BI dashboard đơn thuần. BIZOS là Business Operating System — nơi mọi task hằng ngày, KPI, lương thưởng và tài chính đều được nối vào một chuỗi logic thống nhất."

**Framing:** Not a replacement for HRIS (Workday, BambooHR), not a BI tool (Tableau, PowerBI), not a CRM. Positions as a **unifying layer** above existing function-specific tools — though in practice, ships as a standalone comprehensive platform (64-table schema covers HR + KPI + finance + recruiting + knowledge etc.).

## 3. 19-screen inventory

| # | Route | Function |
|---|-------|----------|
| 01 | `/dashboard` | 6 KPI cards + hero donut + revenue trend + 3 AI insight cards (30-sec company snapshot) |
| 02 | `/org` | Reactflow org chart + headcount by department + "span of control 1:5-1:8" heuristic |
| 03 | `/departments` | Cost-center + KPI-center per dept (budget_monthly + KPI completion) |
| 04 | `/people` | Employee directory + per-person KPI + skill matrix |
| 05 | `/kpi` | 4-level tree (company → dept → team → employee) + status coloring (green ≥100% / yellow 85-99% / red <85%) |
| 06 | `/operations` | Task board + SLA + `linked_kpi_id` attachment |
| 07 | `/compensation` | Payroll + IncentiveSimulator + 5-tier bonus rule engine |
| 08 | `/projects` | Milestones + ROI + project_budgets + dependencies |
| 09 | `/finance` | P&L + Balance Sheet + Cash Flow + budget vs actual + cost centers |
| 10 | `/settings` | Company config + roles + imports + bonus rules |
| 11 | `/reports` | Report Center (schedules + exports) |
| 12 | `/alerts` | Alert rules + severities (info / warning / danger / critical) |
| 13 | `/approvals` | Multi-step approvals (bonus / budget / hiring) |
| 14 | `/audit` | Append-only audit log (last 100 entries) |
| 15 | `/okr` | Objectives + key_results + okr_alignments cascade |
| 16 | `/forecast` | **What-if simulator** — change leaf KPI %, propagate via weighted-sum cascade (max 10 iterations), see Net Profit delta |
| 17 | `/recruiting` | Job requisitions + candidates + skill gap |
| 18 | `/knowledge` | sop_documents + playbooks + checklists |
| 19 | `/profile` | Per-user account page |
| 20 | `/settings` | (menu 10) |
| 21 | `/guide` | In-app bilingual tutorial (800 lines TSX) — **corpus-first** |

## 4. KPI cascade — central abstraction

**Data model:**
- `kpis` table: `level` enum (company/department/team/employee) + `parent_kpi_id` self-reference + `weight` numeric + `owner_employee_id` / `owner_department_id` / `owner_team_id`
- `kpi_formulas` table: JSONB AST stored per-KPI (10 operators: sum/sub/mul/avg/weighted_avg/ratio/milestone/ref/const/manual)
- `kpi_targets` / `kpi_actuals` — per-period values
- `kpi_thresholds` — color-band config
- `kpi_audit_logs` — change history

**Runtime:**
- `buildKpiRows` → enriches kpis with target/actual/completion/status
- `buildKpiTree` → constructs parent-child tree
- `simulateImpact(rows, changes)` — 10-iteration weighted-sum propagation

**End-to-end workflow** (README + /guide):
```
Task (/operations)
  → KPI cá nhân (/people/:id)
    → KPI phòng ban (/departments/:id)
      → KPI công ty (/kpi)
        → Payroll (/compensation, rule engine)
          → Tài chính (/finance)
            → Forecast what-if (/forecast)
```

**Traceability promise** (README):
> "Mỗi bước đều truy vết được. Đổi 1 KPI lá ở Forecast sẽ thấy tác động lên Net Profit ngay lập tức."

## 5. Demo-mode fallback (corpus-first zero-friction evaluation UX)

**Without Supabase credentials:**
- App auto-enables demo mode
- Ships 14 employees + 14 KPIs + payroll + accounting + alerts + approvals + OKRs + requisitions + SOPs + audit logs
- All 19 screens render end-to-end
- CRUD buttons no-op

**Mechanism:** `lib/queries/index.ts` `safeFetch<T>(query, fallback)` — try Supabase, fall through to `lib/queries/demo.ts` (21KB dataset) on null/empty/error.

**Evaluation flow for newcomer:**
```
git clone https://github.com/ungden/bizos-company-os
cd bizos-company-os
pnpm install
pnpm dev
# Open http://localhost:3000 → auto-redirect /login → 
# /login stub accepts any email → browse all 19 screens
```

5-minute evaluation experience = **corpus-first** for business-application scope.

## 6. i18n VN+EN first-class

- `lib/i18n/dict.ts` = **626 entries** with `{ vi, en }` each
- `DEFAULT_LOCALE = "vi"` (VN-primary)
- Top-bar toggle (`VI / EN`)
- All UI strings + status labels + menu items + error messages + tips + philosophy + howto steps bilingual
- /guide page bilingual at philosophy + tips + 19 per-screen summaries + 3 workflows
- **Production-grade i18n at cold-start (2 days old)** — not a backfill, shipped day 1

## 7. Stack (verbatim + package.json)

- **Next.js 16.2.4** (App Router + Server Components + Server Actions)
- **React 19.2.4** + React DOM 19.2.4
- **TypeScript** (typed throughout; `types/domain.ts` custom types)
- **Tailwind CSS v4** + shadcn-style UI primitives (`components/ui/`)
- **lucide-react** 1.8.0 (icon library)
- **Recharts** 3.8.1 (line / bar / donut / sparkline charts)
- **reactflow** 11.11.4 (org chart + KPI tree visualization)
- **Supabase** (`@supabase/ssr` 0.10.2 + `@supabase/supabase-js` 2.104.1) — Postgres + Auth + Storage + RLS
- **TanStack Table** 8.21.3 (data grid)
- **React Hook Form** 7.73.1 + **Zod** 4.3.6 (validation)
- **date-fns** 4.1.0
- **Docker + pnpm + Vercel + Railway** (4 deploy surfaces)

## 8. Next.js 16 breaking changes reflected

- `middleware.ts` → `proxy.ts` (root-level; calls `updateSession` from `@/lib/supabase/proxy`)
- `proxy` function signature matches Next 16 API
- AGENTS.md explicit warning to AI coding agents: "This is NOT the Next.js you know... Read the relevant guide in `node_modules/next/dist/docs/` before writing any code."

**Corpus-first:** First Storm Bear wiki where the subject uses stable-release Next 16 (prior Next.js projects would have been ≤ 15).

## 9. Scale signals

- **GitHub:** 18 stars / 25 forks / 0 watchers / 0 open issues / 0 PRs
- **Age:** ~2 days (pushed 2026-04-22, wiki built 2026-04-24)
- **Language:** TypeScript 90.5% + PLpgSQL 9.0%
- **Commits:** 7 visible on main
- **Releases:** 0 (package.json shows 0.1.0, no GitHub releases tagged)
- **Repo size:** Not disclosed by GitHub UI, estimated ~5-10 MB source
- **Fork-to-star ratio:** 25/18 = 1.388 (138%) — **inverted compared to typical pattern** (stars > forks is standard OSS signal; bizos has forks > stars indicating template-use adoption vs popularity discovery)

**Corpus comparison:**
- Smallest prior: codymaster v12 at 38 stars / 21 forks (55% fork ratio)
- Bizos 18 stars / 25 forks (138% fork ratio) = **corpus-first inverted fork-to-star**

## 10. Pattern relevance

| Pattern | Relevance | Notes |
|---------|-----------|-------|
| **#22 AGENTS.md** (confirmed) | STRENGTHENS | 327B minimum-viable sub-variant + outside-scope adoption |
| **#29 License-Category-Diversity** (confirmed) | STRENGTHENS | Absent-LICENSE + README-proprietary sub-category = new 4th structural variant |
| **#27 Community-Viral Scale Path** (confirmed) | COUNTER-EVIDENCE | Fork > star at 18-star scale = template-use not viral-discovery |
| **#12 Governance-Depth** (confirmed) | BASELINE reinforcement | Solo + cold-start + minimum governance = expected per #12 (baseline case; v35 claude-hud counter-evidence re-framed as outlier) |
| **#73 Regional-Archetype-Registry T1** (confirmed v36) | CROSS-TIER observation only | VN author but outside-scope, not T1. #73 is T1-scoped. Observation of cross-tier VN author pattern noted for potential future cross-tier meta-pattern. |
| NEW #74 Business-OS-as-Product Outside-Scope Sub-Type | OBSERVATION-TRACK (N=1 cold-start) | Single data point at 2-day-old 18-star cold-start; insufficient for architectural pattern |
| NEW #75 Template-Use Fork-Star Anomaly | OBSERVATION-TRACK (N=1 episodic) | Inverted ratio 138% as cold-start template-use signal; episodic |

## 11. Corpus-firsts contributed

1. First in-app bilingual tutorial page (`/guide`) as first-class menu item (800 lines TSX)
2. First absent-LICENSE-file wiki (README-only proprietary statement)
3. First 2-day-old cold-start wiki subject
4. First fork > star (138% ratio) observation
5. First VN solo-developer at outside-scope tier (VN T1: codymaster v12 + claude-howto v32 now joined cross-tier)
6. First Next.js 16 stable wiki (middleware → proxy.ts rename)
7. First business-OS-as-product content genre (7th outside-scope sub-type candidate)
8. First 64-table business-domain relational-DB wiki
9. First 7-role RBAC matrix (ceo / cfo / hr_admin / dept_head / team_lead / employee / auditor) with SQL scope-function helpers
10. First JSONB AST business-formula engine (10 operators) wiki
11. First 5-tier bonus-threshold + team/company multipliers rule engine wiki
12. First VN labor-law hardcoded assumptions (10% employee + 23.5% employer BHXH)
13. First demo-fallback safeFetch pattern (zero-friction evaluation)
14. First apparent Claude-Code-built production artifact wiki (signals: `.claude/launch.json` + AGENTS.md framework-warning + 800-line /guide + CLAUDE.md `@AGENTS.md` pointer)

## 12. Key tensions

- **Scale vs ambition mismatch:** 18 stars + 25 forks suggests very early; 64-table schema + 19 screens + bilingual i18n suggests ambitious spec (likely a real internal Titan Labs tool open-sourced, not organic viral growth)
- **License vs README:** Absent LICENSE file makes "fork to learn" statement legally unenforceable; any commercial fork requires explicit written permission from Alex Le
- **Demo-mode completeness:** All 19 screens render without Supabase → suggests screens are UI-complete with seed data but CRUD wiring may be partial
- **Roadmap vs actual:** All 11 phases marked ✅ in README but 0 live customer deployments disclosed

## 13. Open questions → `01 Analysis/(C) open questions.md`

See 22 open questions on project origin, commercial posture, pattern applicability, Storm Bear fit.
