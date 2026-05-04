# (C) Cluster — Technical engines + 64-table schema + 7-role RLS

**Sources:** `lib/kpi/formulaEngine.ts` (81 lines) + `lib/kpi/cascade.ts` (93 lines) + `lib/compensation/ruleEngine.ts` (100 lines) + `lib/queries/index.ts` (103 lines) + `lib/queries/demo.ts` (21KB) + `db/schema.sql` (28.9KB, 64 tables) + `db/policies.sql` (8.3KB, 7 roles RLS) + `db/seed.sql` (11.2KB) + `proxy.ts` + `Dockerfile` + deploy configs

## 1. KPI Formula Engine (`lib/kpi/formulaEngine.ts`)

**JSONB AST evaluator** — 10 operators:

| Op | Behavior |
|----|----------|
| `const` | Return literal constant |
| `ref` | Resolve from `ctx.refs[def.ref]` (defaults to 0 if missing) |
| `sum` | Reduce args to sum |
| `sub` | Reduce args left-to-right as subtraction chain |
| `mul` | Reduce args to product |
| `avg` | Mean of args |
| `weighted_avg` | Current impl uses equal weights; structurally weighted |
| `ratio` | `numerator / denominator` (with zero-division guard → 0) |
| `milestone` | Step function: for each `{at, value}`, return last matched value where `__input >= at` |
| `manual` | Return pre-set `def.value` |

**Signature:**
```typescript
evaluateFormula(def: KpiFormulaDef, ctx: FormulaContext): number
// ctx = { refs: Record<string, number> }
```

**Describe function:** `describeFormula(def)` returns human-readable string (e.g., `"mql × close"` for `{op:"mul",args:[{ref:"mql"},{ref:"close"}]}`)

**Storage:** `kpi_formulas` DB table (column 11 of schema) with `formula_type text` + JSONB data column

**Corpus-first observation:** JSONB AST formula engine is a production domain pattern uncommon in corpus (most frameworks use code-defined primitives not data-defined formulas). Cross-wiki: codymaster v12 CodeGraph operates on codebase ASTs; bizos operates on business-formula ASTs.

## 2. KPI Cascade Engine (`lib/kpi/cascade.ts`)

**`buildKpiRows(kpis, targets, actuals)`** — enriches each KPI with:
- `target` = target_value for current period
- `actual` = actual_value for current period  
- `completion` = `actualRow.completion_rate ?? (target && actual ? actual/target : null)`
- `status`:
  - ≥100% → "green"
  - ≥85% → "yellow"
  - <85% → "red"
  - null → "na"

**`buildKpiTree(rows)`** — constructs parent-child tree via `parent_kpi_id`; returns array of root nodes. Each `KpiNode = KpiRow & { children: KpiNode[] }`.

**`simulateImpact(rows, changes)`** — what-if propagation:
1. Build `next` map initialized with each row's actual
2. Apply percentage changes to leaf KPIs (`next[id] = current * (1 + deltaPct/100)`)
3. Iteratively recompute parent KPIs as weighted sum of children: `Σ (child_value × child.weight) / Σ child.weight`
4. Max 10 iterations (`guard = 10`)
5. Return `{ id → { before, after, delta_pct } }` map

**Used by:** `/forecast` screen (client-side `<Simulator />` with sliders)

**Corpus-first observation:** Iterative weighted-sum propagation with convergence loop at N=10 iterations — simple fixed-point algorithm, explicit guard against cycles.

## 3. Compensation Rule Engine (`lib/compensation/ruleEngine.ts`)

**Default bonus rule:**
```typescript
{
  name: "Default tiered bonus",
  base_bonus_pct: 15,  // 15% of base salary at target
  thresholds: [
    { completion_min: 0,   multiplier: 0 },
    { completion_min: 0.8, multiplier: 0.5 },
    { completion_min: 0.9, multiplier: 0.75 },
    { completion_min: 1.0, multiplier: 1.0 },
    { completion_min: 1.2, multiplier: 1.5 }
  ],
  team_multiplier: 1,
  company_multiplier: 1
}
```

**Payroll computation:**
1. `mult = pickMultiplier(rule, kpi_completion)` → step-function on thresholds
2. `kpi_bonus = base_salary × (base_bonus_pct/100) × mult`
3. `team_bonus` = if team_completion ≥ 1: `kpi_bonus × (team_multiplier - 1) + base_salary × 0.02`
4. `company_bonus` = if company_completion ≥ 1: `base_salary × 0.03 × company_multiplier`
5. `gross_pay = base + allowance + commission + kpi_bonus + team_bonus + company_bonus - penalty + adjustment`
6. `net_pay = round(gross × 0.9)` (simulated ~10% tax/BHXH deduction)
7. `company_cost = round(gross × 1.235)` (simulated +23.5% for employer BHXH)

**Hardcoded VN assumptions:**
- 10% employee tax/social-insurance deduction (Vietnam Bảo Hiểm Xã Hội)
- 23.5% employer social-insurance burden (VN standard)
- VND currency assumed

**Output: `PayrollBreakdown`** with 12 fields (base / allowance / commission / kpi_bonus / team_bonus / company_bonus / penalty / adjustment / gross_pay / net_pay / company_cost / multiplier_applied)

**Corpus-first observation:** Only corpus wiki with production compensation-rule-engine tied to domain-specific legal/tax assumptions (VN BHXH). Cross-regional implication: localized to VN labor law at default-rule level.

## 4. Demo-fallback `safeFetch` pattern (`lib/queries/index.ts`)

```typescript
async function safeFetch<T>(query: (sb: Sb) => QueryLike, fallback: T): Promise<T> {
  try {
    const sb = await createClientOrNull();
    if (!sb) return fallback;
    const { data } = await query(sb);
    if (!data || (Array.isArray(data) && data.length === 0)) return fallback;
    return data as T;
  } catch {
    return fallback;
  }
}
```

**15 fetch functions** each wrapping a Supabase query with demo fallback:
- `fetchEmployees`, `fetchDepartments`, `fetchKpis`, `fetchKpiActuals`, `fetchKpiTargets`
- `fetchTasks`, `fetchPayroll`, `fetchProjects`, `fetchAccounting`
- `fetchAlerts`, `fetchApprovals`
- `fetchObjectives`, `fetchKeyResults`, `fetchRequisitions`, `fetchSops`, `fetchAuditLogs`

**Demo dataset** (`lib/queries/demo.ts`, 21KB):
- 14 employees
- 14 KPIs (4-level cascade)
- Payroll entries
- Accounting entries
- Alerts + Approvals
- Objectives + Key Results
- Job requisitions
- SOP documents
- Audit logs

**Architectural observation:** Demo-fallback is zero-friction evaluation primitive. Fresh clone + `pnpm install && pnpm dev` renders all 19 screens in 5 minutes without Supabase credentials. Write operations (CRUD buttons) no-op in demo mode.

## 5. 64-table schema — 11 domain areas

**Domain area breakdown** (from `db/schema.sql`):

| # | Domain | Tables | Count |
|---|--------|--------|-------|
| 1 | **Organization** | companies, business_units, departments, teams, positions, employees, employee_reporting_lines, employment_contracts | 8 |
| 2 | **RBAC** | user_roles | 1 |
| 3 | **KPI** | kpis, kpi_formulas, kpi_dependencies, kpi_targets, kpi_actuals, kpi_thresholds, kpi_audit_logs | 7 |
| 4 | **Operations** | sla_rules, tasks, task_recurrences, task_outputs, task_status_logs, workload_snapshots | 6 |
| 5 | **Compensation** | compensation_plans, salary_components, bonus_rules, commission_rules, payroll_periods, payroll_entries, adjustment_entries | 7 |
| 6 | **Projects** | projects, project_members, project_milestones, project_budgets, project_roi_records, project_dependencies | 6 |
| 7 | **Finance** | chart_of_accounts, cost_centers, accounting_entries, budgets, budget_lines, ar_ap_records, cashflow_records, financial_snapshots | 8 |
| 8 | **OKR** | objectives, key_results, okr_alignments | 3 |
| 9 | **Recruiting** | job_requisitions, candidates, skill_matrix, training_needs | 4 |
| 10 | **Knowledge** | sop_documents, playbooks, checklists | 3 |
| 11 | **Governance** | approvals, approval_steps, alert_rules, alerts, reports, report_schedules, notifications, audit_logs, integrations, import_jobs, app_settings | 11 |
| **Total** | | | **64** |

**Enum types (12):**
- `employment_type` (fulltime / parttime / contract / intern / freelance)
- `employee_status` (active / onboarding / on_leave / terminated)
- `kpi_level` (company / department / team / employee)
- `kpi_frequency` (daily / weekly / monthly / quarterly / yearly)
- `task_priority` (low / normal / high / urgent)
- `task_type` (growth / maintenance / admin / urgent)
- `task_status` (todo / in_progress / blocked / review / done / cancelled)
- `project_status` (draft / active / paused / done / cancelled)
- `approval_status` (pending / approved / rejected / cancelled)
- `alert_severity` (info / warning / danger / critical)
- `app_role` (ceo / cfo / hr_admin / dept_head / team_lead / employee / auditor)
- (extension) `pgcrypto` for UUID generation

**Multi-tenant keying:** Every table has `company_id uuid references companies(id)` — multi-tenant-by-company.

**Audit columns:** Most tables have `created_at timestamptz not null default now()`; some `updated_at` with trigger (not inspected deeply).

**Corpus observation:** 64-table business-domain schema is the largest explicit schema documented in Storm Bear corpus (prior largest: multica v15 with Postgres 17 + pgvector but no table-count disclosed at this granularity; graphify v16 has graph-DB not relational). Bizos is a corpus-first production-domain relational-database artifact.

## 6. 7-role RLS (`db/policies.sql`)

**Role matrix:**

| Role | Scope | Typical permissions |
|------|-------|---------------------|
| `ceo` | Company-wide | All data read + approve top-level |
| `cfo` | Company-wide | Finance + approvals + reports |
| `hr_admin` | Company-wide | People + compensation + recruiting |
| `dept_head` | Scoped via `scope_department_id` | Own dept KPI + tasks + budget |
| `team_lead` | Scoped via `scope_team_id` | Own team tasks + KPI |
| `employee` | Own records + team visibility | Own profile + tasks + KPI view |
| `auditor` | Read-only company-wide | Audit log + reports |

**SQL helpers:**
- `current_company_id()` — returns caller's company_id from `user_roles` (first active role; multi-company users must switch context per-session)
- `has_role(target app_role)` — exists-check current user has target role in current company
- `has_any_role(variadic roles)` — same as above for multiple roles
- `current_employee_id()` — returns caller's employee ID
- `is_dept_head_of(dept uuid)` — scoped dept-head check

**RLS enablement:**
- `do $$ foreach t in array[...] loop enable RLS end $$` pattern
- Array of 60+ tables all RLS-enabled
- Per-table policies defined individually (not inspected in depth but ~190 lines total in policies.sql)

**Corpus observation:** 7-role RBAC matrix with SQL-level scope functions = most detailed RBAC in Storm Bear corpus. Closest corpus comparison: multica v15 with first-class agents + RBAC not documented at this granularity.

## 7. Next.js 16 specifics (corpus-first)

- **`proxy.ts` (not middleware.ts)** — Next 16 renamed middleware convention
- **Server Components + Server Actions** — App Router pattern
- **`@supabase/ssr`** — server-component-compatible Supabase client (not the classic `@supabase/supabase-js` browser client)
- **`layout.tsx` in `(app)` route group** — app shell with Sidebar + Topbar + Footer applied across 19 screens
- **`(auth)` route group** — login / signup / reset-password with separate layout
- **App Router only** — no pages/ directory

## 8. Ecosystem primitives at the component layer

**`components/` organization (9 folders):**

| Folder | Contents |
|--------|----------|
| `ui/` | button, card, input, badge, label, separator, tabs (shadcn-style primitives) |
| `layout/` | Sidebar, Topbar, PageHeader, Footer |
| `charts/` | AreaTrend, BarCompare, DonutStat, MiniSpark (recharts wrappers) |
| `kpi/` | KpiCard, KpiHeroDonut, KpiStatusBadge, KpiTreeGraph |
| `widgets/` | ProgressList, ActivityFeed, MiniCalendar, StatChip, InsightCard |
| `org/` | OrgGraph (reactflow) |
| `tables/` | DataTable (TanStack Table wrapper) |
| `forecast/` | Simulator (client, sliders) |
| `compensation/` | IncentiveSimulator |

**9 folder buckets** organizing the UI primitives systematically. Not a "design system" per se but a consistent component taxonomy.

## 9. 4 deploy surfaces

1. **Vercel** (recommended for Next.js) — auto-detects `vercel.json` + Next.js framework
2. **Railway** (Docker) — detects `Dockerfile` + `railway.json` (Nixpacks alternative possible)
3. **Docker** (multi-stage node:22-alpine) — 38-line Dockerfile; builds independently + runs as non-root
4. **Local** (`pnpm install && pnpm dev`) — demo mode without env, live mode with Supabase env

Healthcheck endpoint: `/api/health` (standard GET, not inspected)

## 10. Key absences (technical cluster)

- ❌ No test files (`*.test.ts`, `*.spec.ts`, `__tests__/`, `tests/`, `e2e/`) — zero visible test harness
- ❌ No CI workflows (`.github/workflows/*.yml`)
- ❌ No Storybook / component catalog
- ❌ No API documentation (OpenAPI / Swagger)
- ❌ No benchmarks / load testing
- ❌ No contribution-gate (no PR template, no CODEOWNERS)
- ❌ No observability (no Sentry / Datadog / LogRocket config visible)

## 11. Key phrases (verbatim from source)

From `lib/queries/index.ts` comment:
> "Khi chưa cấu hình Supabase, trả demo dataset để UI vẫn render được. Khi có Supabase, query thật + fallback demo nếu lỗi/không có data."
>
> Translation: "Without Supabase config, return demo dataset so UI still renders. With Supabase, real query + fallback to demo if error/no data."

From `lib/kpi/cascade.ts` comment:
> "Ứng dụng đơn giản: áp delta vào KPI lá, rồi propagate lên parent bằng tổng có trọng số (weight) của children."
>
> Translation: "Simple: apply delta to leaf KPI, then propagate to parent via weighted sum of children."

From `db/schema.sql` header:
> "BIZOS — Business Operating System (Supabase / Postgres schema). Bám theo spec Mục 7 & 8: organization, KPI, operations, compensation, projects, finance, goals/OKR, recruiting, knowledge, governance, rbac."
>
> Translation: "Follows spec sections 7 & 8: organization, KPI, operations, compensation, projects, finance, goals/OKR, recruiting, knowledge, governance, rbac."
>
> **Inference:** Project appears to have been built from a written spec (sections numbered 7 & 8 referenced). Spec document not included in repo but implied by consistent schema structure.

## 12. Cross-wiki echo

- v15 multica — Postgres 17 + pgvector + Next.js T2 closest technical peer (but T2 not outside-scope; bizos has no agent primitives)
- v12 codymaster — VN + solo + CodeGraph AST — bizos has analogous JSONB AST for business formulas
- v29 crawl4ai — Apache-2.0 OSS comparison (bizos proprietary-by-default opposite license posture)
- v23 Unsloth — Performance-focused kernels; bizos performance concern is KPI-cascade propagation loop (max 10 iterations with convergence guard)
- v17 spec-kit — "built from spec" parallel (bizos schema comment cites "spec Mục 7 & 8")
