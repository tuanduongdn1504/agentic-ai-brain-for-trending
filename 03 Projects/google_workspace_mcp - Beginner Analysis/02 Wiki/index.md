# google_workspace_mcp — Wiki (v140)

> **One line:** A FastMCP-based **MCP server** that gives any MCP client (Claude Desktop/Code, VS Code, LM Studio) **full natural-language control of 12 Google Workspace services** through one OAuth-secured server.
> **Tier:** T2 Service (MCP integration server). **Verdict:** GOAL-ALIGNED INCLUDE 3/4 (a FAIL · b/c/d STRONG).
> **Repo:** `taylorwilsdon/google_workspace_mcp` · MIT · Python 3.10+ · website workspacemcp.com.
> **§37 provenance:** ≈2.6k★ / 784 forks / 16 watchers / 52 issues / 49 PRs (as of 2026-06, repo page — *stated, NOT API-verified; env mocks GitHub API*).

## What it is

An MCP server exposing the **Google Workspace API surface** as agent tools. README opener (verbatim):

> "Full natural language control over Google Calendar, Drive, Gmail, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through all MCP clients, AI assistants and developer tools."

Tagline: *"Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI."*

## Services covered (12)
Gmail · Drive · Calendar · Docs · Sheets · Slides · Forms · Chat · Apps Script · Tasks · Contacts · Custom Search — **50+ tools** total, with first-class file attachment/download and fine-grained editing.

## Architecture / tech stack
- **Framework:** jlowin **FastMCP 2.13.0+** (`gofastmcp.com`, the popular OSS MCP-server framework — *not* an Anthropic product) with the native `GoogleProvider` (Dynamic Client Registration + CORS for OAuth 2.1).
- **Language:** Python 3.10+. **License:** MIT (permissive, no CLA, no telemetry).
- **Storage:** local dir or GCS backend; optional Valkey/Redis for OAuth proxy state; Fernet credential encryption.

## Three things worth studying

### 1. Graduated tool tiers (`--tool-tier core | extended | complete`)
Cumulative least-privilege tool exposure: **Core** (essential read/search/create) → **Extended** (labels, batch, advanced search) → **Complete** (comments, headers/footers, publishing). Rationale is **API-quota + permission-scope + tool-count surface** — register only what you need. ("Start with `core` and upgrade as needed.") *(Phase 4b PRIMARY — corpus-first Library-vocab N=1.)*

### 2. OAuth that scales from laptop to multi-tenant
- **OAuth 2.0** — confidential + public PKCE clients.
- **OAuth 2.1 multi-user** (`MCP_ENABLE_OAUTH21`) — multiple users on one server via bearer tokens, auto-refresh; mutually exclusive with `--single-user` and service-account modes.
- **Service account** domain-wide delegation (impersonation).
- **Stateless mode** (`WORKSPACE_MCP_STATELESS_MODE`) — *no filesystem writes; credentials never hit disk*, tokens held in the OAuth 2.1 session store. Built for containers/ephemeral deploys.

### 3. Three transports
- **stdio** — legacy local-only, integrated OAuth callback.
- **streamable-HTTP** — recommended; modern HTTP transport, OAuth 2.1 multi-user.
- **reverse proxy** — behind nginx/Cloudflare via `WORKSPACE_EXTERNAL_URL`.

## Install (quick)
```
uvx workspace-mcp --tool-tier core      # run via uv, core tier
# or: uv run main.py
```
Env: `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, `WORKSPACE_MCP_PORT`, `MCP_ENABLE_OAUTH21`, …
Optional Claude skill: symlink/copy `skills/managing-google-workspace/` → `~/.claude/skills/managing-google-workspace` for better Workspace tool-routing.

## MCP clients
Claude Desktop · Claude Code · VS Code MCP · LM Studio · any MCP-1.0-compliant client.

## Corpus connectivity
- **Pattern #18 B1 "MCP / one-binary-many-CLIENTS"** — strong N+1 instance (MCP cluster: v66 agentmemory, v70 codegraph, v119 nature-MCP, v132 supermemory, v134 obsidian-second-brain).
- **Pattern #84 multi-harness** — N+1 (one protocol, many clients).
- **Bundled Claude skill** — agentskills.io-*adjacent* routing artifact (not a 57k `npx skills add` implementer).
- See `01 Analysis/` for the full Phase 0.9 verdict + Phase 4b proposal.

## Pilot note
**Tier-1 pilotable, conditional.** If you want an agent to touch your *own* Gmail/Calendar/Drive/Docs, this is the lowest-friction MCP route: `uvx workspace-mcp --tool-tier core` against a Google OAuth client, scoped read-only first, reversible by removing the server config. Use `install-snapshot` and start at `core` / read-only mode. (Real-account OAuth = real blast radius; start minimal.)
