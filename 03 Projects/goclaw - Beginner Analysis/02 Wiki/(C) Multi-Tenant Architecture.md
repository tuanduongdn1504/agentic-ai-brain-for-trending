# (C) Multi-Tenant Architecture

> **Source:** README.md (lines 72, 278-293), CLAUDE.md (key patterns + security), `docs/09-security.md` (skim), `docs/00-architecture-overview.md` module map
> **Ingested:** 2026-04-18
> **Type:** Entity page (distribution/deployment concept) — building block #3 cho goclaw

---

## One-liner

**VI:** Multi-Tenant Architecture là **điểm đặc biệt của goclaw** so với 3 siblings — goclaw designed từ ngày đầu cho **multiple users sharing 1 deployment**, mỗi user có workspace riêng, context files riêng, encrypted API keys, RBAC (admin/operator/viewer), isolated sessions, **per-tenant scoping trong SQL**, và **5-layer defense security**. 3 siblings (ECC/Superpowers/gstack) = single-user dev tools.

**EN:** Multi-Tenant Architecture is goclaw's key differentiator vs 3 siblings — designed for multiple users sharing one deployment with isolation at every layer (workspace, context, API keys, RBAC, SQL scoping, security defense).

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao goclaw targets teams/orgs, không phải cá nhân devs
- Deploying goclaw cho team Storm Bear's Scrum coaching
- Designing your own multi-tenant agent platform
- Security audit for enterprise deployment

**Không cần dùng GoClaw Lite (desktop)** — single-user mode skips multi-tenancy entirely.

---

## Comparison sibling

| Axis | ECC | Superpowers | gstack | **goclaw** |
|------|-----|-------------|--------|------------|
| Tenancy model | Single-user dev tool | Single-user dev tool | Single-user dev tool | **Multi-tenant platform** |
| User isolation | N/A (user = dev) | N/A | `./setup --team` shares repo | **Per-tenant workspace, per-user files** |
| API key storage | `.env` plaintext | N/A (uses Claude Code auth) | N/A | **AES-256-GCM in PostgreSQL** |
| Access control | N/A | N/A | N/A | **RBAC: admin/operator/viewer** |
| Session isolation | N/A | N/A | Per-session Claude Code | **Isolated sessions in PG** |
| Audit | N/A | N/A | N/A | **Security logs (`slog.Warn("security.*")`)** |
| Rate limiting | N/A | N/A | N/A | **Built-in, per-tenant** |

→ **goclaw unique.** 3 siblings = "my tool, my machine". goclaw = "shared platform, many users".

---

## Sub-types: Isolation levels

### Level 1: Tenant (organization)

- Highest-level isolation boundary
- Separate tenant = separate PostgreSQL row namespace
- All tenant-scoped tables have `tenant_id` column
- SQL queries enforce `WHERE tenant_id = $N`

### Level 2: User (within tenant)

- Individual user within tenant
- Per-user workspace (filesystem)
- Per-user context files (`user_context_files` table)
- Per-user encrypted secrets

### Level 3: Agent

- Agent-level scoping (within user)
- `agent_context_files` (agent-level defaults)
- `user_context_files` (per-user overrides)
- Agent identity dual-pattern: UUID (DB/FK) + agent_key (logs/paths/UI)

### Level 4: Session

- Within agent run
- Unique session ID
- Session state isolated in PG

### Level 5: Role (RBAC)

- **Admin** — full tenant-level access
- **Operator** — can use agents, can't admin
- **Viewer** — read-only

Plus **Master scope** (system-level, above tenant) — for global tables (e.g., `builtin_tools`, disk config).

---

## Anatomy: Tenant-scope guards (CRITICAL discipline)

From CLAUDE.md:

> "**`RoleAdmin` is not a tenant check.** Writes to **global** tables (no `tenant_id` column — e.g. `builtin_tools`, disk config, package mgmt) must gate with `http.requireMasterScope` / WS `requireMasterScope(requireOwner(...))`.
>
> Writes to **tenant-scoped** tables must gate with `http.requireTenantAdmin` + SQL `WHERE tenant_id = $N`."

**Decision table:**

| Action | Target table | Required gate |
|--------|--------------|---------------|
| Read tenant-scoped data | has `tenant_id` | `WHERE tenant_id = $N` |
| Write tenant-scoped data | has `tenant_id` | `http.requireTenantAdmin` + `WHERE tenant_id = $N` |
| Write global data | no `tenant_id` | `http.requireMasterScope` |
| System-level admin | global | `requireMasterScope(requireOwner(...))` |

**Shared predicate:** `store.IsMasterScope(ctx)`.

> See `CONTRIBUTING.md` → "Tenant-scope guards"

→ **Critical discipline.** Most multi-tenant systems muddle this, leading to privilege escalation.

### Context propagation

Tenant ID propagates via context:
- `store.WithTenantID(ctx)` — set at gateway entry
- All downstream operations check `ctx` for tenant ID
- Missing tenant ID in ctx → reject (fail-safe default)

---

## Cơ chế

### Mechanism 1: 5-layer defense security

Per `docs/09-security.md`:

```
Layer 1: Transport (CORS, message size limits, timing-safe auth)
Layer 2: Input (injection detection 6 patterns, message truncation)
Layer 3: Tool (shell deny, path traversal, SSRF, exec approval)
Layer 4: Output (credential scrubbing, content wrapping)
Layer 5: Isolation (workspace, Docker sandbox, read-only FS)
```

Each layer **independent**. Layer N+1 valid even if Layer N bypassed.

→ **Defense-in-depth pattern.** Industry standard for enterprise.

### Mechanism 2: AES-256-GCM for secrets

**Encrypted at rest:**
- LLM provider API keys
- MCP server API keys
- Custom tool environment variables

**Stored in PostgreSQL.** Decrypted in-memory when needed.

→ **Even DB dump leak = encrypted keys.** Requires separate encryption key compromise.

### Mechanism 3: `CanAccess` 4-step pipeline

Agent-level access control:

1. Check tenant scope (tenant ID match?)
2. Check user scope (user ID match? or shared?)
3. Check RBAC role (admin/operator/viewer)
4. Check agent-level access (per-agent permissions)

→ All 4 must pass. Any fail → reject.

### Mechanism 4: Session isolation

Sessions stored in PG. Each session has:
- Tenant ID + User ID + Agent ID
- Session state (messages, tool calls, memory pointers)
- RBAC + concurrency limits per-edition

Scheduler has **4 lanes**: main / subagent / cron / team. Per-session serialization prevents races.

### Mechanism 5: Workspace isolation

Per-tenant + per-user filesystem boundary:

```
/app/workspace/
├── tenant-A/
│   ├── user-1/
│   │   └── files...
│   └── user-2/
├── tenant-B/
│   └── ...
```

**Path traversal prevention:**
- `PathDenyable` interface enforces boundary
- Agent can't `../` out of assigned workspace
- File serving has 2-layer path isolation (workspace boundary + tenant scope)

### Mechanism 6: Rate limiting per tenant

Rate limiter applied per-tenant:
- Message rate
- LLM call rate
- Tool invocation rate

→ **Prevents noisy neighbor problem.** One tenant can't exhaust resources of others.

---

## Out-of-box behavior

**Default configuration:**
- Multi-tenancy **ON** in Standard edition (PostgreSQL)
- **OFF** in Lite edition (SQLite, single-user)
- RBAC enforced at all admin endpoints
- Rate limiting enabled
- Security logs to stdout (`slog.Warn("security.*")`)

**First run:**
```bash
./goclaw onboard    # Interactive wizard
```

Creates:
- First tenant (default org)
- First admin user
- Seed data (default agents, providers)

**Add user:**
- Via web dashboard (http://localhost:18790) by admin
- Or via CLI/API

---

## Configuration knobs

| Knob | Default | Effect |
|------|---------|--------|
| `allowed_origins` | empty (allow all — backward compat) | CORS whitelist cho WebSocket |
| `edition` | auto (PG = Standard, SQLite = Lite) | Feature gating |
| `tenant.max_users` | unlimited | Per-tenant user cap |
| `rate_limit.messages_per_minute` | tbd | Rate limit policy |
| `rbac.default_role` | `viewer` | New user initial role |
| `encryption.key_rotation` | tbd | AES key rotation policy |

→ (Inferred defaults. Check `config.json5`.)

---

## Recipes

### Recipe 1: Deploy goclaw for Storm Bear coaching team

```bash
# Docker compose setup
./prepare-env.sh
# Add master API key to .env
# Add tenant admin credentials
make up
```

Then:
1. Admin logs in at http://localhost:18790
2. Creates tenant "StormBear"
3. Invites team members as operators
4. Configures agents + providers
5. Team uses via web / Zalo / Telegram / etc.

**Blocker check:** CC BY-NC 4.0 license. Coaching = commercial use?

### Recipe 2: Audit multi-tenant isolation

Run invariant tests:
```bash
make test-invariants   # P0 - tenant isolation (blocking)
```

**Per CLAUDE.md:** "P0 - tenant isolation (blocking)" means these tests MUST pass before any merge.

### Recipe 3: Rotate encryption key

(Speculative — not verified)
```bash
./goclaw migrate rotate-keys --from=old-key --to=new-key
```

Re-encrypts AES-GCM keys without data loss.

### Recipe 4: Add new tenant

Via admin dashboard or API:
```http
POST /v1/admin/tenants
Authorization: Bearer <master-token>
{
  "name": "NewOrg",
  "plan": "standard"
}
```

### Recipe 5: Security event monitoring

All security events logged with `slog.Warn("security.*")`:
- `security.auth.failure`
- `security.injection_detected`
- `security.path_traversal_attempt`
- `security.ssrf_blocked`
- `security.credential_scrubbed`

Pipe to SIEM/logging tool (Datadog, Splunk, etc.) for monitoring.

---

## Advanced patterns

### Pattern: Edition system với feature gating

`internal/edition/edition.go`:
- `Lite` preset auto-selected for SQLite backend
- `Standard` preset for PostgreSQL
- Check `edition.Current()` for feature availability

**Lite gating:**
- 5 agents max
- 1 team (5 members max)
- 50 sessions
- No channels, no KG, no RBAC, no multi-tenant

**Tool gating:**
- `skill_manage`, `publish_skill` not registered in Lite
- `TeamActionPolicy` blocks comment/review/approve/reject/attach/ask_user in Lite

→ **Clean gating pattern.** Same codebase, different features per edition.

### Pattern: Dual-DB via Dialect interface

`internal/store/base/Dialect` interface enables:
- `pg/` implementation — PostgreSQL
- `sqlitestore/` implementation — SQLite

Both implementations use same interface. Application code backend-agnostic.

→ **Reusable pattern** cho any tool needing dual-DB.

### Pattern: Context key convention check

CLAUDE.md Rule #16: "Context key style convention check — check existing `context.go` pattern before introducing new key types. Mixed = code smell."

→ **Consistency matters.** Mixing context key styles = future maintenance burden.

### Pattern: Encrypted secrets via internal/crypto/

All secrets flow through `internal/crypto/` (AES-256-GCM). Centralized encryption = auditable.

→ **Centralization principle.** Don't decentralize encryption logic.

### Pattern: Per-edition rate limits

`MaxSubagentConcurrent`, `MaxSubagentDepth` configured per-edition. Lite = lower limits, Standard = higher.

---

## Combination với building blocks khác

### + 8-Stage Pipeline
ContextStage injects tenant ID via `WithTenantID()`. All stages tenant-aware.

### + 3-Tier Memory + Knowledge Vault
Per-tenant vault. Per-user memory. Isolated.

### + Agent Teams
Team = org-structured multi-agent. Within tenant boundary.

### + Provider adapters
20+ LLM providers. Each tenant can have own API keys (encrypted separately).

### + Channels
7 messaging channels. Each channel instance (e.g., Telegram bot) belongs to 1 tenant.

### Cross-project: + Storm Bear vault
Storm Bear currently single-user. If scale to coaching team:
- Option A: Deploy goclaw with Storm Bear vault imported (multi-tenant)
- Option B: Keep Storm Bear file-based (simpler), accept single-user limit
- Blocker: CC BY-NC 4.0 license

### Cross-project: + 3 siblings (ECC/Superpowers/gstack)
None are multi-tenant. Dev-tool scope. goclaw fills gap for "multi-tenant agent platform" that 3 siblings don't address.

---

## Anti-patterns

❌ **Skip tenant scope guards** — per CLAUDE.md, "`RoleAdmin` is not a tenant check." Admin role alone = NOT permission to access arbitrary tenant.

❌ **Plaintext secrets** — all secrets via `internal/crypto/`. Never add plaintext handling.

❌ **Mix context key conventions** — check `context.go` existing patterns first.

❌ **Shared filesystem across tenants** — path traversal = privilege escalation.

❌ **Skip invariant tests** — P0 blocking tier. Merge blocked if failed.

❌ **Forget edition gating** — code running in Lite may crash without feature gate. Check `edition.Current()`.

❌ **Use master scope for tenant-level ops** — master scope is system-wide admin. Tenant admin = scoped admin. Different.

❌ **Assume single-user deployment** — design for multi-tenant from day 1. Retrofitting multi-tenancy = painful.

---

## Cross-references

- [[(C) 8-Stage Agent Pipeline]] — tenant ID propagation
- [[(C) 3-Tier Memory + Knowledge Vault]] — per-tenant isolation
- [[(C) Agent Teams and Orchestration]] — team inside tenant
- [[(C) README summary]] — Multi-Tenant feature #7
- [[(C) CLAUDE.md + Architecture summary]] — tenant-scope guards discipline
- [[(C) Key Docs deep dive]] — 5-layer security
- Cross-project: all 3 siblings — N/A (single-user scope)

## Citations

- README.md line 72 (Multi-Tenant PostgreSQL feature)
- README.md lines 278-293 (Production Security)
- CLAUDE.md key pattern: tenant-scope guards
- CLAUDE.md "tenant-scope guards on admin writes" convention (lines ~195-205)
- `docs/09-security.md` 5-layer defense
- `docs/00-architecture-overview.md` module map (permissions, crypto, edition, workspace)

## TODO

- ⏸ Read `CONTRIBUTING.md` → "Tenant-scope guards" section for full decision table
- ⏸ Verify exact RBAC role capabilities (admin/operator/viewer permission matrix)
- ⏸ Check CC BY-NC 4.0 commercial use boundaries — coaching business OK?
- ⏸ Test: deploy goclaw + import Storm Bear vault + invite 2 test users → works?
- ⏸ Check rate limit defaults — reasonable for small coaching team?
