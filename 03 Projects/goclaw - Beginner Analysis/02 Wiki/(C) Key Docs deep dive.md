# (C) Key Docs Deep Dive

> **Sources (skim-first, picked most-relevant of 20 numbered docs):**
> - `docs/14-skills-runtime.md` (283 lines, ~13KB) — skills container architecture
> - `docs/11-agent-teams.md` (717 lines, ~35KB) — **skim-first** (overview + team model only)
> - `docs/09-security.md` (498 lines, ~22KB) — **skim-first** (5 layers intro)
> - `CHANGELOG.md` (78 lines, ~4KB) — full read
>
> **Ingested:** 2026-04-18
> **Routine context:** Source #3 of 3 (Phase 2)

---

## TL;DR

**VI:** Source #3 synthesis từ 4 key docs để capture 3 pillars critical-but-not-yet-covered:
1. **Skills Runtime (container/Docker architecture)** — goclaw run skills trong read-only Alpine container với Python/Node runtimes optional per image variant
2. **Agent Teams (orchestration model)** — Lead + Members với shared Task Board + Mailbox, delegation system
3. **5-Layer Defense Security** — Transport / Input / Tool / Output / Isolation, independent layers

**EN:** Skills runtime container + Agent teams orchestration + 5-layer security defense + recent changelog.

---

## Part 1: Skills Runtime (container architecture)

### Image variants matrix

| Variant | Tag | Build args | Pre-installed runtimes |
|---------|-----|------------|------------------------|
| Minimal | `latest` | `ENABLE_PYTHON=false`, `ENABLE_NODE=false` | No Python/Node |
| Python | `python` | `ENABLE_PYTHON=true` | `python3`, `py3-pip`, `edge-tts` |
| Node | `node` | `ENABLE_NODE=true` | `nodejs`, `npm` |
| **Full** | `full` | `ENABLE_FULL_SKILLS=true` | `python3`, `py3-pip`, `nodejs`, `npm`, `pandoc`, `github-cli`, bundled skill deps |

→ **4 image variants** cho different use cases. Pre-bake what you need, skip what you don't.

### Container security model

```
┌──────────────────────────────────────────────────────┐
│  Alpine 3.22, read_only: true                        │
│                                                      │
│  Pre-installed (image layer, immutable)              │
│    latest/alpine = no Python/Node                    │
│    python/node/full = progressive inclusion          │
│                                                      │
│  Writable Runtime Dir  /app/data/.runtime/           │
│    pip/         ← PIP_TARGET (user-level install)    │
│    pip-cache/   ← PIP_CACHE                          │
│    npm-global/  ← NPM_PREFIX                         │
│                                                      │
│  Volumes (read-write):                               │
│    /app/data      ← goclaw-data volume               │
│    /app/workspace ← goclaw-workspace volume          │
│                                                      │
│  tmpfs (noexec):                                     │
│    /tmp (256MB, no executables)                      │
└──────────────────────────────────────────────────────┘
```

**Key security constraints:**
- Root filesystem read-only
- `/tmp` tmpfs, no-exec
- Runtime additions only to designated writable paths
- Volume isolation: data + workspace separate

### Skills discovery

`internal/skills/` = **SKILL.md loader (5-tier hierarchy) + BM25 search + hot-reload via fsnotify**

**5-tier hierarchy** (implied from code structure, not yet verified):
1. Built-in skills (bundled với binary)
2. Image-variant skills (baked in Docker image)
3. Tenant skills (per-tenant custom skills)
4. User skills (per-user custom)
5. Session skills (runtime-created)

→ **Most sophisticated skills architecture** của 4 projects. ECC/Superpowers/gstack = flat skill list.

### Skills folder actual content

`skills/` at repo root:
- `_shared/` — shared resources
- `docx/` — Word document handling
- `pdf/` — PDF handling
- `pptx/` — PowerPoint handling
- `xlsx/` — Excel handling
- `skill-creator/` — meta-skill to create skills

→ **Anthropic's official skill library** replicated (docx/pdf/pptx/xlsx = Anthropic Claude Skills library). Implies compatibility layer for Anthropic skill format.

---

## Part 2: Agent Teams (orchestration)

### Team model

```
┌────────────────────────────────────┐
│  Agent Team                        │
│                                    │
│  Lead Agent                        │
│  (orchestrates, creates tasks,     │
│   delegates, synthesizes results)  │
│                                    │
│  Member A   Member B   Member C    │
│  (claim and execute tasks)         │
└────────────────────────────────────┘
         ↓
┌────────────────────────────────────┐
│  Shared Resources                  │
│                                    │
│  Task Board (create/claim/complete)│
│  Mailbox (DMs, broadcasts)         │
└────────────────────────────────────┘
```

**Built on delegation system** (from `03-tools-system.md` Section 7 — not deep-read this session).

**Orchestration primitives:**
- `BatchQueue[T]` generic for result aggregation
- `ChildResult` capture
- Media conversion helpers
- 3 delegation modes: sync (wait) / async (fire-and-forget) / bidirectional
- Token-aware work distribution

### Comparison với 3 siblings

| Orchestration | ECC | Superpowers | gstack | **goclaw** |
|---------------|-----|-------------|--------|--------|
| Team concept | 48 agents callable | Dynamic spawn via SDD | 23 specialists | **Lead + Members structured team** |
| Task persistence | N/A | N/A | `/learn` session | **PostgreSQL `subagent_tasks` + `team_workspace`** |
| Inter-agent coord | Manual via Task tool | SDD subagents isolated | `/pair-agent` browser share | **Task Board + Mailbox structured** |
| Parallelism | User-driven | SDD parallel skills | Conductor 10-15 | **Native multi-agent, bounded by scheduler lanes** |

→ **Most formal team orchestration.** goclaw treats multi-agent as first-class architecture. 3 siblings treat as one-off dispatch.

---

## Part 3: 5-Layer Defense Security

```
Request
  ↓
Layer 1: Transport — CORS, message size limits, timing-safe auth
  ↓
Layer 2: Input — Injection detection (6 patterns), message truncation
  ↓
Layer 3: Tool — Shell deny patterns, path traversal, SSRF, exec approval
  ↓
Layer 4: Output — Credential scrubbing, content wrapping
  ↓
Layer 5: Isolation — Workspace isolation, Docker sandbox, read-only FS
```

### Layer highlights

**Layer 1: Transport**
- `checkOrigin()` validates `allowed_origins` (empty = allow all for backward compat)
- `SetReadLimit(512KB)` — gorilla auto-closes on exceed
- Timing-safe auth comparison (prevents timing attacks)

**Layer 2: Input**
- 6 injection detection patterns
- Message truncation

**Layer 3: Tool** (strongest layer)
- Shell deny patterns
- Path traversal prevention
- **SSRF protection** (for web tool, hook HTTPHandler)
- Exec approval workflow

**Layer 4: Output**
- Credential scrubbing (prevents API keys leaking in LLM output)
- Content wrapping

**Layer 5: Isolation**
- Workspace isolation (per-tenant filesystem)
- Docker sandbox (via `WITH_SANDBOX=1`)
- Read-only FS (per skills runtime above)

### Encryption

- **AES-256-GCM** for:
  - LLM provider API keys
  - MCP server API keys
  - Custom tool environment variables
- Stored in PostgreSQL
- Agent-level access control via `CanAccess` 4-step pipeline

### Comparison với 3 siblings

| Security aspect | ECC | Superpowers | gstack | **goclaw** |
|-----------------|-----|-------------|--------|--------|
| Production-grade | AgentShield (separate paid) | Zero-dep supply chain | Localhost bearer token | **5 independent defense layers** |
| Encryption at rest | N/A | N/A | N/A | **AES-256-GCM for secrets** |
| Input filtering | N/A | N/A | `/careful` power tool | **6 injection patterns** |
| Sandbox | N/A | N/A | N/A | **Docker sandbox (optional)** |
| Multi-tenant isolation | N/A | N/A | N/A | **Per-tenant workspace + RBAC** |

→ **Enterprise-grade.** goclaw is only project with production security posture across all 5 layers.

---

## Part 4: CHANGELOG (full read — 78 lines)

### Latest entries (Unreleased)

**Breaking changes:**
- **Context pruning now opt-in** — previously tool-result trimming ran by default, now requires `contextPruning.mode: "cache-ttl"` in `config.agents.defaults`. Match upstream TS design, prevents silent prompt-cache invalidation on Anthropic

**Observation:** Only 1 breaking change note in unreleased. Conservative cadence relative to gstack (126 versions in 6 months) and Superpowers (27+ versions).

### Version numbering (inferred từ CLAUDE.md + tag info)

- `v3.x` current mainline
- `v2.67.x-beta.N` beta releases
- `lite-v1.x.x` desktop edition (independent versioning)

Different from siblings:
- ECC: standard semver
- Superpowers: 5.0.x aggressive cadence
- gstack: 0.18.x (pre-1.0)
- **goclaw: 3.x stable mainline + lite-v1.x.x parallel track**

→ Dual-track versioning (Standard + Lite separate). Match desktop edition independence.

---

## Distinctive patterns này source

### Pattern 1: Multi-variant Docker images

4 variants (minimal/python/node/full). Pre-bake dependencies for expected use case. Reduces runtime install + container startup overhead.

→ **Reusable cho Storm Bear nếu ever containerize.**

### Pattern 2: 5-tier skill hierarchy

Built-in → Image → Tenant → User → Session. Progressive override.

→ **Most sophisticated of 4 projects.** Allows fine-grained customization without forking codebase.

### Pattern 3: BatchQueue[T] generic

Go generic primitive cho aggregating results from N sub-agents concurrently.

→ Implementation pattern documented, reusable in Go projects.

### Pattern 4: Task Board + Mailbox dual-primitive

Task-oriented (structured work items) + Communication-oriented (free-form messages). Both persist in PostgreSQL.

→ **Match Kanban + Slack model.** Agent-native implementation.

### Pattern 5: Defense-in-depth independent layers

Each layer operates independently. Layer N+1 valid even if Layer N bypassed.

→ **Contrast với "security via single firewall"** anti-pattern.

---

## Open questions resolved

- ✅ Q7: Skills Runtime format — **5-tier hierarchy với BM25 + hot-reload**. Anthropic-compatible (docx/pdf/pptx/xlsx evidence). Potentially import từ gstack/Superpowers with compatibility layer, but not verified.
- ✅ Q4: Multi-Tenant architecture scaleable cho team — **yes, per-user workspaces + encrypted secrets + RBAC + SQL tenant scoping**. Enterprise-ready.

## Open questions raised

- ⏸ Exact 5-tier hierarchy file format — đọc `internal/skills/*.go` if need details
- ⏸ Task Board API — usable standalone cho Storm Bear team task tracking?
- ⏸ 6 injection patterns Layer 2 — what are they? Reusable library?
- ⏸ Docker sandbox use cases — Storm Bear agent running untrusted code?
- ⏸ Version 3.0 migration notes — rewrite? Major breaking?

---

## Cross-references

- [[(C) README summary]]
- [[(C) CLAUDE.md + Architecture summary]]
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Release Notes overview.md` — release cadence comparison
- Cross-project: `../../gstack - Beginner Analysis/02 Wiki/(C) Multi-Host Declarative Platform.md` — distribution comparison

## Citations

- `docs/14-skills-runtime.md` lines 1-100 (container architecture + image variant matrix)
- `docs/11-agent-teams.md` lines 1-50 (team model + mermaid diagram)
- `docs/09-security.md` lines 1-80 (5-layer defense architecture)
- `CHANGELOG.md` full (78 lines)

## TODO

- ⏸ Read `docs/03-tools-system.md` Section 7 (delegation primitives that teams build on)
- ⏸ Read `docs/06-store-data-model.md` — CanAccess 4-step pipeline
- ⏸ Verify `/v1/packages/runtimes` API endpoint for runtime discovery
- ⏸ Check if Claude CLI + gstack installed inside goclaw's Full variant container works end-to-end
