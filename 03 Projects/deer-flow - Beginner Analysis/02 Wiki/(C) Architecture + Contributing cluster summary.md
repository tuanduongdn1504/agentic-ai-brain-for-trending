# (C) Architecture + Contributing cluster summary

> Nguồn: `CONTRIBUTING.md` (10 KB) + architectural hints từ README
> Purpose: Development architecture + code structure + workflow

## TL;DR

deer-flow = **layered architecture** with Nginx unified entry, Frontend (TypeScript/Next.js), Gateway API (Python), LangGraph Server. Code split: `backend/src/` (gateway + agents + MCP + skills + sandbox) và `frontend/` (React). Dev workflow: feature branch → format → PR. CI enforces formatting + tests (unit + E2E). Docker recommended. Adding skills + agents = documented at high level; implementation details in backend config docs.

---

## Part 1 — Architecture (layered)

### System diagram

```
Browser
   ↓
Nginx (port 2026) — unified entry
   ↓ routes
   ├── Frontend (port 3000) — Next.js/React
   ├── Gateway API (port 8001) — Python (domain logic)
   └── LangGraph Server (port 2024) — agent orchestration
```

### Routing rules

- `/api/langgraph/*` → LangGraph Server (agents handle)
- Other `/api/*` → Gateway API (Python handles)
- Static assets → Frontend

### Why layered design

1. **Separation of concerns** — UI ≠ business logic ≠ agent orchestration
2. **Scalability** — can split frontend vs backend scale independently
3. **Language choice** — TypeScript for UI (ecosystem), Python for agents (LangGraph)
4. **Security boundary** — Nginx controls external exposure
5. **Reverse proxy benefits** — SSL termination, rate limiting, auth (future)

### Comparison to sibling architectures

| Sibling | Architecture |
|---------|--------------|
| ECC (T1) | Plugin in Claude Code process |
| goclaw (T2) | Go binary + multi-tenant platform |
| notebooklm-py (T4) | 4-layer library (CLI/Client/Core/RPC) |
| **deer-flow (T5)** | **Layered web app (Nginx/Frontend/Gateway/LangGraph)** |

→ **deer-flow most complex architecturally** — full-stack app requires more layers.

---

## Part 2 — Code Structure

### Backend organization
```
backend/src/
├── gateway/        ← API endpoints (REST)
├── agents/         ← LangGraph agent definitions
├── mcp/            ← Model Context Protocol integration
├── skills/         ← Skill implementations
└── sandbox/        ← Execution environment
```

### Frontend organization
```
frontend/
└── [Next.js structure]
    ├── React components
    └── UI logic
```

### Skills organization (separate folder)
```
skills/
├── public/         ← Built-in skills
└── custom/         ← User-created skills
```

### Configuration
```
config.example.yaml   ← Template, copied to config.yaml
config.yaml           ← User-configured (models, search, sandbox)
extensions_config.example.json   ← Extensions config template
.env.example          ← Environment template
```

---

## Part 3 — Development Workflow

### Branching
```bash
git checkout -b feature/your-feature-name
# Make changes
# Format code (REQUIRED)
git commit -m "feat(scope): description"
# Submit PR
```

### Formatting (enforced by CI)

**Backend:**
```bash
make format   # runs ruff
```

**Frontend:**
```bash
pnpm format:write   # runs Prettier + ESLint
```

**CI rejects unformatted code.**

### Testing

**Backend:**
```bash
make test   # unit tests
```

**Frontend:**
```bash
make test          # unit tests
make test-e2e      # E2E (when frontend files change)
```

### Development cycle
1. Feature branch
2. Changes với hot-reload enabled
3. Format before commit
4. Unit + E2E tests
5. PR submit
6. CI checks pass
7. Review + merge

---

## Part 4 — Adding New Capabilities

### Skills (Markdown-based)

CONTRIBUTING.md references skills system but **detailed instructions aren't in main guide** — directs contributors to backend config docs.

**Inferred pattern (from README):**
- Skill = Markdown file defining capability
- Progressive loading = loaded when context needs
- Public (built-in) vs custom (user) separation

### Agents (LangGraph)

Also referenced but detailed instructions point to separate docs.

**Inferred pattern (from README):**
- Sub-agents spawned by lead agent
- Isolated context per sub-agent
- Parallel fan-out + synthesis pattern

---

## Part 5 — Commit Conventions (implied)

Standard semantic commits based on conventions:
- `feat(scope):` new feature
- `fix(scope):` bug fix
- `refactor(scope):` refactor
- `docs(scope):` documentation
- `test(scope):` tests
- `style:` style-only

**Scopes:** likely match code structure (gateway, agents, mcp, skills, sandbox, frontend).

---

## Part 6 — Signals of Engineering Maturity

### Strong signals
- ✅ **Enforced formatting** (ruff backend, Prettier+ESLint frontend)
- ✅ **Multi-tier testing** (unit + E2E)
- ✅ **CI gates** (rejection on unformatted / untested)
- ✅ **Hot-reload dev loop**
- ✅ **Semantic commits**
- ✅ **Docker-first development**
- ✅ **Layered separation** (Nginx + Frontend + Gateway + LangGraph)

### Potential weak signals
- ⚠️ Adding skills/agents documented weakly (reading between lines)
- ⚠️ Windows-specific support unclear
- ⚠️ Performance benchmarking not explicit
- ⚠️ Production hardening guidance limited in CONTRIBUTING

---

## Part 7 — Comparison: engineering maturity across 9 wikis

| Wiki | Formatting enforced | Tests CI | Commit conventions | Docker-first |
|------|---------------------|----------|-------------------|--------------|
| ECC (T1) | Yes | Yes | Yes | No (plugin) |
| Superpowers (T1) | Yes | Yes | Yes | No |
| gstack (T1) | Yes | Yes | Yes | No |
| GSD (T1) | Yes | Yes | Yes | No |
| goclaw (T2) | Yes | Yes | Yes | Yes |
| course (T3) | N/A (docs) | N/A | Standard | N/A |
| notebooklm-py (T4) | Yes (ruff+mypy) | Yes (unit/integration/E2E) | `feat/fix/refactor/style` | No |
| build-your-own-x (outside) | N/A (aggregator) | N/A | N/A | N/A |
| **deer-flow (T5)** | **Yes (ruff+Prettier+ESLint)** | **Yes (unit + E2E)** | **Standard semantic** | **Yes** |

→ **deer-flow = strong engineering discipline** comparable to goclaw (T2) và notebooklm-py (T4). ByteDance corporate standards visible.

---

## Part 8 — Operational considerations

### Production deployment (from README)
- **Local trusted-network deployment recommended**
- Production requires:
  - Strict security measures
  - IP allowlists
  - Authentication gateways
- **Not designed as public SaaS** out of box

### Observability
Not detailed in CONTRIBUTING. Presumably LangGraph provides agent tracing.

### Secrets management
`.env` based. Environment variables. No secrets manager integration by default.

### Multi-user considerations
Not explicitly addressed. deer-flow appears designed as single-tenant or small-team tool, not multi-tenant SaaS (goclaw is different in that regard).

---

## Cross-references

- Main positioning: [[(C) README summary]]
- Install flow: [[(C) Install + Setup summary]]
- Related entities:
  - [[(C) SuperAgent Harness Architecture]] (draws from this cluster)
  - [[(C) Skill System (Progressive Loading)]] (skills/ folder detail)
  - [[(C) Sub-Agent System (Parallel Fan-out)]] (agents/ folder design)
- Sibling dev workflows:
  - `../../notebooklm-py - Beginner Analysis/02 Wiki/(C) Architecture + Release cluster summary.md` (4-layer comparison)
  - `../../goclaw - Beginner Analysis/02 Wiki/(C) Multi-Tenant Architecture.md`
