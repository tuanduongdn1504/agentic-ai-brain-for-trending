# (C) Internal engines + 64-table schema + 7-role RLS

**Cross-references:** Cluster 3 (Technical engines) | v12 codymaster (AST parallel) | v15 multica (Postgres+Next.js peer) | v17 spec-kit ("built from spec" parallel) | Pattern observations: 64-table corpus-first business-domain schema

## 1. Identity

The "engine room" of BIZOS: three production runtimes + one demo-fallback infrastructure + a 64-table relational schema + a 7-role row-level-security matrix. Combined footprint ~10 files of code (~380 lines of engine TypeScript + ~940 lines of SQL). This is the architectural core that justifies the "Business Operating System" label — the 19 screens are mostly presentation layer over this engine+schema foundation.

## 2. KPI Formula Engine — `lib/kpi/formulaEngine.ts` (81 lines)

**Purpose:** Evaluate business formulas stored as JSONB AST in `kpi_formulas.formula_data`.

**10 operators:**

| Op | Semantics | Example AST |
|----|-----------|-------------|
| `const` | Literal numeric constant | `{const: 100}` |
| `ref` | Lookup from context `refs` map (default 0) | `{ref: "mql"}` |
| `sum` | Σ args | `{op: "sum", args: [{ref:"a"}, {ref:"b"}]}` |
| `sub` | Left-to-right reduce as subtraction chain | `{op: "sub", args: [{ref:"revenue"}, {ref:"cost"}]}` |
| `mul` | Π args | `{op: "mul", args: [{ref:"mql"}, {ref:"close"}]}` |
| `avg` | Arithmetic mean | `{op: "avg", args: [...]}` |
| `weighted_avg` | Current impl = equal weights (structurally weighted placeholder) | `{op: "weighted_avg", args: [...]}` |
| `ratio` | Numerator / denominator (zero-division → 0) | `{op: "ratio", numerator: {ref:"revenue"}, denominator: {ref:"employees"}}` |
| `milestone` | Step function: for each `{at, value}`, return last where `__input ≥ at` | `{op: "milestone", steps: [{at:0.8, value:0.5}, {at:1, value:1}]}` |
| `manual` | Pre-set value (escape hatch) | `{op: "manual", value: 42}` |

**Companion function:** `describeFormula(def)` returns human-readable string (`"mql × close"`, `"revenue / employees"`, etc.) for UI display.

**Storage pattern:**
```sql
create table kpi_formulas (
  id uuid primary key,
  kpi_id uuid references kpis(id) unique,
  formula_type text not null,
  formula_data jsonb  -- AST
);
```

**Architectural observation:** Data-defined formulas (stored in DB) vs code-defined formulas (hardcoded). Advantages: non-engineers can edit formulas via UI; schema migrations don't ripple into formula changes; audit trail via `kpi_audit_logs`. Trade-offs: type safety weaker than TypeScript; formula evaluator must be kept in sync with AST schema.

## 3. KPI Cascade Engine — `lib/kpi/cascade.ts` (93 lines)

**3 exported functions:**

### `buildKpiRows(kpis, targets, actuals) → KpiRow[]`
Joins per-KPI records with current-period target + actual, computes:
- `completion` = `actualRow.completion_rate ?? (target && actual ? actual/target : null)`
- `status` via 4-band logic: `green ≥100% / yellow ≥85% / red <85% / na null`

### `buildKpiTree(rows) → KpiNode[]`
Constructs parent-child forest via `parent_kpi_id` self-references. Returns root nodes each with `children: KpiNode[]` recursive.

### `simulateImpact(rows, changes) → Record<id, {before, after, delta_pct}>`

**Algorithm:**
```
1. Initialize next[id] = row.actual || 0 for all rows
2. For each (leaf_id, deltaPct) in changes: next[leaf_id] *= (1 + deltaPct/100)
3. Repeat up to 10 iterations:
   for each row r with children:
     weighted = Σ(next[child.id] × child.weight) / Σ child.weight
     if |weighted - next[r.id]| > 0.0001: next[r.id] = weighted; changed=true
   break if no changes
4. Return {id → {before: row.actual, after: next[id], delta_pct}}
```

**Edge handling:**
- Zero-weight children: `|| 1` fallback in denominator sum
- Zero-division in delta_pct: `before === 0 → delta_pct = 0`
- Cycle prevention: `guard = 10` iterations max
- Convergence threshold: `0.0001` delta

**Used by:** `/forecast` screen (client Simulator with sliders).

**Corpus observation:** Fixed-point weighted-sum propagation is simple and correct for acyclic trees; documented cycle-protection via hard iteration cap. Not validated for adversarial cyclic parent_kpi_id references (schema doesn't enforce acyclic constraint via triggers/CTEs).

## 4. Compensation Rule Engine — `lib/compensation/ruleEngine.ts` (100 lines)

**Default rule:**
```typescript
{
  name: "Default tiered bonus",
  base_bonus_pct: 15,  // 15% of base_salary at 100% KPI completion
  thresholds: [
    { completion_min: 0,   multiplier: 0 },    // <80% = no bonus
    { completion_min: 0.8, multiplier: 0.5 },  // 80-89%
    { completion_min: 0.9, multiplier: 0.75 }, // 90-99%
    { completion_min: 1.0, multiplier: 1.0 },  // 100-119%
    { completion_min: 1.2, multiplier: 1.5 }   // ≥120% = 150% bonus
  ],
  team_multiplier: 1,
  company_multiplier: 1
}
```

**`computePayroll(input: ComputePayrollInput) → PayrollBreakdown`:**
1. `mult = pickMultiplier(rule, kpi_completion)` step function
2. `kpi_bonus = base_salary × (base_bonus_pct/100) × mult`
3. `team_bonus = (team_completion ≥ 1) ? kpi_bonus × (team_multiplier - 1) + base_salary × 0.02 : 0`
4. `company_bonus = (company_completion ≥ 1) ? base_salary × 0.03 × company_multiplier : 0`
5. `gross_pay = base_salary + allowance + commission + kpi_bonus + team_bonus + company_bonus - penalty + adjustment`
6. `net_pay = round(gross × 0.9)` — simulated VN employee deductions (BHXH + thuế ~10%)
7. `company_cost = round(gross × 1.235)` — simulated VN employer burden (+23.5% BHXH employer)

**Output: 12-field `PayrollBreakdown`** (base / allowance / commission / kpi_bonus / team_bonus / company_bonus / penalty / adjustment / gross / net / company_cost / multiplier_applied).

**Regional assumption:** VN Bảo Hiểm Xã Hội (BHXH) rates hardcoded. Generalizing would require per-country tax-rule engine (currently not implemented).

**Corpus-first:** Only corpus wiki with production compensation-rule-engine tied to domain-specific legal/tax assumptions.

## 5. Demo-fallback safeFetch — `lib/queries/index.ts` (103 lines)

**Generic wrapper:**
```typescript
async function safeFetch<T>(query: (sb: Sb) => QueryLike, fallback: T): Promise<T> {
  try {
    const sb = await createClientOrNull();
    if (!sb) return fallback;                    // No Supabase env
    const { data } = await query(sb);
    if (!data || (Array.isArray(data) && data.length === 0)) return fallback;  // Empty response
    return data as T;
  } catch {
    return fallback;                             // Any error
  }
}
```

**15 wrapped fetchers:**
- `fetchEmployees` / `fetchDepartments`
- `fetchKpis` / `fetchKpiActuals(period)` / `fetchKpiTargets(period)`
- `fetchTasks` / `fetchPayroll` / `fetchProjects` / `fetchAccounting`
- `fetchAlerts` / `fetchApprovals`
- `fetchObjectives` / `fetchKeyResults`
- `fetchRequisitions` / `fetchSops` / `fetchAuditLogs`

**Demo data (`lib/queries/demo.ts`, 21KB):**
- `demoEmployees` (14 records)
- `demoKpis` / `demoKpiActuals` / `demoKpiTargets` (14 KPIs; sample period 2026-04)
- `demoTasks` / `demoPayroll` / `demoProjects` / `demoAccounting`
- `demoAlerts` / `demoApprovals`
- `demoObjectives` / `demoKeyResults`
- `demoRequisitions` / `demoSops` / `demoAuditLogs`

**Architectural significance:** Demo-fallback = zero-friction evaluation primitive. Clone → `pnpm install && pnpm dev` → browse all 19 screens in 5 minutes without Supabase account.

## 6. 64-table relational schema — 11 domain areas

### 6.1 Organization (8 tables)
- `companies` — tenant root; currency default VND, timezone default Asia/Ho_Chi_Minh, JSONB settings
- `business_units` — BU subdivisions within company
- `departments` — cost-center + KPI-center; references `head_employee_id`, `budget_monthly`
- `teams` — within departments; references `lead_employee_id`
- `positions` — job codes with `base_salary_min/max`
- `employees` — master record; references dept/team/position/manager; `auth_user_id` UNIQUE links to Supabase auth
- `employee_reporting_lines` — versioned reporting-to-manager history
- `employment_contracts` — versioned with `starts_at / ends_at / base_salary / allowances jsonb`

### 6.2 RBAC (1 table + 5 SQL helpers)
- `user_roles` — `(auth_user_id, company_id, role app_role, scope_department_id?, scope_team_id?)` with UNIQUE composite constraint
- SQL helpers: `current_company_id()` / `has_role(target)` / `has_any_role(variadic)` / `current_employee_id()` / `is_dept_head_of(dept)`

### 6.3 KPI (7 tables)
- `kpis` — master KPI records with `level kpi_level` (company/dept/team/employee), `parent_kpi_id` self-ref, `weight numeric`, `target_frequency kpi_frequency` (daily/weekly/monthly/quarterly/yearly), `owner_*` FKs
- `kpi_formulas` — JSONB AST per KPI (1:1 unique)
- `kpi_dependencies` — graph edges between KPIs (beyond simple parent)
- `kpi_targets` — per-period target values
- `kpi_actuals` — per-period actual values with `completion_rate`
- `kpi_thresholds` — color-band config (green/yellow/red cutoffs)
- `kpi_audit_logs` — change history

### 6.4 Operations (6 tables)
- `sla_rules` — service-level agreement templates
- `tasks` — with `linked_kpi_id`, `priority task_priority`, `type task_type`, `status task_status`
- `task_recurrences` — recurring task templates
- `task_outputs` — deliverables produced by tasks (bridge to KPI actuals)
- `task_status_logs` — task state-transition history
- `workload_snapshots` — per-employee workload samples

### 6.5 Compensation (7 tables)
- `compensation_plans` — per-employee comp package
- `salary_components` — base / allowance / commission / etc.
- `bonus_rules` — per-role or per-position rule bindings (refs `ruleEngine.ts`)
- `commission_rules` — sales commission tiers
- `payroll_periods` — monthly close cycles
- `payroll_entries` — per-period per-employee payroll breakdown
- `adjustment_entries` — one-off payroll adjustments with approval trail

### 6.6 Projects (6 tables)
- `projects` — with `status project_status`
- `project_members`, `project_milestones`, `project_budgets`, `project_roi_records`, `project_dependencies`

### 6.7 Finance (8 tables)
- `chart_of_accounts` — COA hierarchy
- `cost_centers` — typically 1:1 with departments
- `accounting_entries` — journal entries
- `budgets` / `budget_lines` — per-cost-center budgets
- `ar_ap_records` — accounts receivable / payable
- `cashflow_records` — cash flow periods
- `financial_snapshots` — P&L / BS / CF computed snapshots

### 6.8 OKR (3 tables)
- `objectives` — quarterly objectives
- `key_results` — measurable per-objective
- `okr_alignments` — bridges objectives across dept/team/person

### 6.9 Recruiting (4 tables)
- `job_requisitions`, `candidates`, `skill_matrix`, `training_needs`

### 6.10 Knowledge (3 tables)
- `sop_documents`, `playbooks`, `checklists`

### 6.11 Governance (11 tables)
- `approvals` + `approval_steps` — multi-step approval flows
- `alert_rules` + `alerts`
- `reports` + `report_schedules`
- `notifications`
- `audit_logs`
- `integrations` — external service bindings
- `import_jobs` — CSV/data import tracking
- `app_settings` — per-company settings jsonb

## 7. Enum types (12)

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
- + `pgcrypto` extension for UUID generation

**Schema pattern:** `do $$ begin create type ... exception when duplicate_object then null; end $$;` — idempotent enum creation (re-runnable seed).

## 8. Row-Level Security (RLS) — 7 roles

**Role matrix:**

| Role | Scope | Read access | Write access |
|------|-------|-------------|--------------|
| `ceo` | Company-wide | All tables | All except audit |
| `cfo` | Company-wide | Finance + KPI + reports + approvals | Finance + approve |
| `hr_admin` | Company-wide | People + comp + recruiting | People + comp + recruiting |
| `dept_head` | Own dept (via `scope_department_id`) | Dept tasks + KPI + budget | Own dept |
| `team_lead` | Own team (via `scope_team_id`) | Team tasks + KPI | Own team |
| `employee` | Self + team visibility | Own profile + team tasks + KPI view | Own profile + task status |
| `auditor` | Company-wide READ-ONLY | All tables | None |

**Multi-tenant key:** Every table has `company_id` — enforced via RLS policies referencing `current_company_id()` helper.

**Idempotent RLS enable pattern:**
```sql
do $$ declare t text; begin
  foreach t in array array['companies','business_units', ... 60+ tables] loop
    execute format('alter table %I enable row level security', t);
  end loop;
end $$;
```

## 9. Seed data (`db/seed.sql`, 11.2KB)

- `BIZOS Demo` company (UUID `00000000-0000-0000-0000-00000000c001`)
- 4 demo users: `ceo@bizos.demo` / `hr@bizos.demo` / `cfo@bizos.demo` / `sales.head@bizos.demo`
- Minimal KPI cascade structure
- Sample employees, tasks, payroll entries

**User creation flow (README):**
1. Run `db/schema.sql` in SQL Editor
2. Run `db/policies.sql` for RLS
3. Run `db/seed.sql` for BIZOS Demo
4. Create Supabase auth users via dashboard
5. Update `employees.auth_user_id` and `user_roles` to link

## 10. 4 deploy configurations

| Surface | Files | Mechanism |
|---------|-------|-----------|
| **Vercel** | `vercel.json` (224B) | Auto-detect Next.js + env-var mapping |
| **Railway** | `railway.json` (369B) + `Dockerfile` | Nixpacks OR Docker path |
| **Docker** | `Dockerfile` (38 lines, 3-stage) | node:22-alpine + pnpm@10 + non-root `app:app` user + port 3000 |
| **Local** | `pnpm install && pnpm dev` | Demo mode without env, live with Supabase env |

**Healthcheck:** `/api/health` endpoint (standard GET 200).

## 11. Pattern relevance

| Pattern | Relevance |
|---------|-----------|
| **#22 AGENTS.md** (confirmed) | 327B minimum-viable AGENTS.md + CLAUDE.md `@AGENTS.md` pointer = smallest-surface sub-variant |
| **#29 License-Category-Diversity** (confirmed) | Proprietary-by-default via absent LICENSE file + README statement = new 4th structural sub-category |
| **#12 Governance-Depth** (confirmed) | Solo + cold-start + minimum governance = baseline-case reinforcement |

## 12. Key absences

- ❌ No migrations framework — single-file `schema.sql` + `policies.sql` + `seed.sql` manual-run
- ❌ No ORM layer — direct Supabase client queries
- ❌ No GraphQL / API layer — Next.js Server Actions + Server Components only
- ❌ No test harness (unit / integration / E2E)
- ❌ No type generation from DB schema (types in `types/domain.ts` hand-written)
- ❌ No load testing / benchmarks
- ❌ No horizontal scaling strategy disclosed

## 13. Cross-wiki echo

- **v15 multica** — closest technical peer (Next.js + Postgres 17 + pgvector) but T2 agent-platform scope; bizos has zero agent primitives
- **v12 codymaster** — VN + solo + CodeGraph AST → bizos JSONB AST analog for business formulas
- **v29 crawl4ai** — Apache-2.0 OSS → bizos proprietary-by-default opposite posture
- **v17 spec-kit** — "built from spec" → bizos schema comment cites "spec Mục 7 & 8" suggesting spec-first methodology possibly aligned with SDD
- **v23 Unsloth** — performance kernels → bizos performance concern is KPI-cascade 10-iteration convergence loop
