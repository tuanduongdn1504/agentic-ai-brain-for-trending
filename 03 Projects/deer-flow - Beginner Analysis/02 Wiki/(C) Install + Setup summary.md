# (C) Install + Setup summary — deer-flow

> Nguồn: `Install.md` (4.7 KB, fetched 2026-04-18)
> Purpose: Installation + configuration reference cho deer-flow v2.0

## TL;DR

deer-flow supports **Docker-preferred** và **local dev fallback** setup. **`make setup`** = interactive wizard. **`config.yaml`** required (with at least 1 LLM model entry). Prerequisites: Docker OR (`node`, `pnpm`, `uv`, `nginx`). Idempotent setup commands. Unified entry `http://localhost:2026`.

## Setup paths

### Path 1: Docker (recommended)
```bash
docker info                # verify Docker available
make docker-init           # prepare prerequisites
make docker-start          # launch services (stopped after init)
```

**Why recommended:**
- Isolated, consistent dev environment
- Sandbox containment works naturally
- No system-level dependency conflicts

### Path 2: Local dev (fallback)
```bash
make check                 # detects missing dependencies
# Required: node, pnpm, uv, nginx

make install               # if check passes
make dev                   # launch all services
```

**Prerequisites checked:**
- `node` (>= 22 per CONTRIBUTING)
- `pnpm` (Node package manager)
- `uv` (Python package manager, modern pip replacement)
- `nginx` (reverse proxy)

## Core Prerequisites

Always required:
- Repo cloned from `https://github.com/bytedance/deer-flow.git`
- Repo root files: `Makefile`, `backend/`, `frontend/`, `config.example.yaml`
- `config.yaml` file (created from `config.example.yaml`)

## Configuration Requirements

### `config.yaml` essentials

- **Models section (required):** at least 1 entry under `models`
- **Environment variables:** `$OPENAI_API_KEY` etc. = user-supplied
- **API keys:** DO NOT assume exist; user must provide

### Installation wizard behavior

`make setup` guides through:
- LLM provider selection (GPT, Gemini, Qwen, Doubao, DeepSeek, Kimi)
- Web search configuration
- Sandbox preferences (Docker vs filesystem)

### Operating principles

- **Idempotent** — safe to re-run setup
- **No `sudo`** without explicit approval
- **No system package install** without approval
- **Stop on failures** with clear blockers + minimal next steps

## Port map

| Port | Service |
|------|---------|
| 2026 | Nginx (unified entry, browser connects here) |
| 3000 | Frontend (Next.js) |
| 8001 | Gateway API (Python) |
| 2024 | LangGraph Server (agent orchestration) |

**Access URL:** `http://localhost:2026` — everything behind Nginx.

## Troubleshooting

**Install.md provides:**
- "Do not assume API keys or model credentials exist"
- Config inspection limited to placeholder detection
- No sudo or system package installation without approval

**Install.md does NOT explicitly cover:**
- Windows-specific quirks
- macOS vs Linux differences
- Common error messages
- Debug flags

→ **Gaps.** Community likely files issues; Install.md expected to evolve.

## Cost / resource considerations

Install.md doesn't detail but implied:
- Docker Desktop = ~1-2 GB RAM overhead
- Node + Python environments = multi-GB
- Multiple services running simultaneously = significant resource draw
- **Laptop 16 GB RAM minimum realistic**; production scaling needs more

## Sequencing for beginners

1. Clone repo
2. Copy `config.example.yaml` → `config.yaml`
3. Add at least 1 LLM model entry in `config.yaml`
4. Add API key in `.env` (or environment variable)
5. Run `make setup` (wizard guides rest)
6. Run `make docker-init && make docker-start` (or local path)
7. Open `http://localhost:2026` in browser

## Comparison to sibling install processes

| Sibling | Install pattern | Complexity |
|---------|-----------------|------------|
| **ECC** | Plugin install trong Claude Code | Low |
| **Superpowers** | Skills install | Low |
| **gstack** | Setup script | Medium |
| **GSD** | `npx get-shit-done-cc` | Low (npm) |
| **goclaw** | Docker + config | Medium-high (platform) |
| **course** | Git clone + Jupyter | Low |
| **notebooklm-py** | `pip install` + `notebooklm login` | Low-medium |
| **build-your-own-x** | N/A (aggregator) | N/A |
| **deer-flow** | **Docker/local + Nginx + multi-service** | **High (app)** |

→ **Most complex install of all 9 wikis.** Because full-stack app (frontend + backend + orchestrator + proxy), not skill/plugin.

## Cross-references

- Main positioning: [[(C) README summary]]
- Architecture detail: [[(C) Architecture + Contributing cluster summary]]
- Related entities: [[(C) SuperAgent Harness Architecture]]
