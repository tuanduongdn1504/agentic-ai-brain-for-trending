# (C) MCPs — Entity Page

> **Type:** Building block #6 (foundation) — Model Context Protocol
> **Status:** Fifth entity page (format đã ổn, có security-aware context từ Security Guide ingest)
> **Sources:** 6 — README, shortform, longform, security guide, `mcp-configs/mcp-servers.json`, `skills/mcp-server-patterns/SKILL.md`
> **Last updated:** 2026-04-17

---

## Một câu / One-liner

**VI:** MCPs (Model Context Protocol) là **cầu nối prompt-driven từ Claude tới external services** (database, GitHub, Vercel, browser, docs…), cho phép agent call tool và đọc resource từ server bên ngoài mà không cần code tích hợp riêng. **Nhưng cũng là attack surface lớn nhất — mỗi MCP thêm vào = thêm risk tool poisoning, secret exposure, prompt injection qua tool descriptions.**

**EN:** MCPs (Model Context Protocol) are **prompt-driven bridges from Claude to external services** (databases, GitHub, Vercel, browsers, docs), letting the agent call tools and read resources from external servers without custom integration code. **But also the largest attack surface — each MCP added = more risk of tool poisoning, secret exposure, and prompt injection via tool descriptions.**

---

## Khi nào dùng / Khi nào KHÔNG dùng

### ✅ Dùng MCP khi:
- Cần Claude **tương tác service ngoài** với ergonomics (DB query, GitHub ops, Vercel deploy)
- Cần **rich typed interface** thay vì parse raw CLI output
- Service không có CLI tốt, hoặc CLI parsing phức tạp
- Cần **schema validation** (MCP tool có JSON schema)
- Multi-user setup cần **standardized tool interface**

### ❌ KHÔNG dùng MCP khi:
- Service đã có **CLI tốt** (gh, supabase, vercel) → dùng **CLI + skill** thay vì MCP (pattern từ longform, tiết kiệm context)
- **Không trust source** — MCP từ Discord random, npm registry không verify → attack vector
- **One-off need** → inline command tốt hơn
- Context window đã **stretched** — mỗi MCP active thêm ~1–5K tokens tool descriptions

---

## MCP vs CLI+Skill vs Hook vs Subagent (chọn cái nào?)

| Tiêu chí | MCP | CLI + Skill | Hook | Subagent |
|----------|-----|-------------|------|----------|
| **Integration style** | Typed tool interface, auto-discover | CLI invocation qua Bash | Event trigger | Delegated Claude |
| **Context cost** | **HIGH** (~1–5K token mỗi MCP enabled) | LOW (chỉ khi skill gọi) | Minimal | HIGH (separate context) |
| **Token cost mỗi call** | Schema validation overhead | Minimal | ~0 | HIGH |
| **Trust boundary** | **Weak** (tool descriptions là executable context) | Strong (CLI output là text) | N/A | Inherit parent |
| **Latency** | Low–Medium | Low | <200ms | High |
| **Share cross-project** | ✅ Global config | ✅ Skill folder | ✅ Settings | ✅ Agent folder |
| **Security risk** | **HIGHEST** (tool poisoning, shadow servers, secret exfiltration) | LOW (just shell) | LOW | Medium (inherit perms) |

> **Quy tắc quyết định từ longform guide:**
> - Service có CLI tốt → **CLI + skill** (preferred for context efficiency)
> - Service không có CLI hoặc parsing phức tạp → **MCP**
> - Mọi session đều dùng → keep **configured** nhưng **disabled by default**, enable per-project/per-task

---

## ECC ship 27 pre-configured MCPs — phân loại / 27 MCPs categorized

> Số liệu: `mcp-configs/mcp-servers.json` chứa **27 MCP servers** pre-configured (verified 2026-04-17). Tác giả dùng ~14 configured + ~5–6 enabled per project.

### Theo category / By category

| Category | MCPs |
|----------|------|
| **Version control / ticketing** | `github`, `jira`, `confluence` |
| **Database / analytics** | `supabase`, `clickhouse` |
| **Deployment / infrastructure** | `vercel`, `railway`, `cloudflare-docs`, `cloudflare-workers-builds`, `cloudflare-workers-bindings`, `cloudflare-observability` |
| **Web / browser** | `firecrawl`, `playwright`, `browserbase`, `browser-use` |
| **Search / research** | `exa-web-search`, `context7` (live docs) |
| **Memory** | `memory`, `omega-memory` (semantic + knowledge graphs) |
| **Reasoning** | `sequential-thinking` |
| **Creative** | `magic` (UI components), `fal-ai` (image/video/audio gen) |
| **Filesystem / local** | `filesystem` |
| **Meta / orchestration** | `devfleet` (multi-agent dispatch), `token-optimizer` |
| **Testing / eval** | `evalview` (agent regression testing) |
| **Ecosystem** | `laraplugins` (Laravel package discovery) |

### Theo transport type / By transport

| Transport | Count | Khi dùng |
|-----------|-------|----------|
| **stdio** (local process) | ~18 | Local tool, `command` + `args` (npx, uvx, python3…) |
| **http** (remote endpoint) | ~9 | Remote API, `type: "http"` + `url` |

---

## Anatomy: Một MCP config trông như thế nào / What an MCP config looks like

### Stdio MCP (local process)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PAT_HERE"
      },
      "description": "GitHub operations - PRs, issues, repos"
    }
  }
}
```

### HTTP MCP (remote endpoint)

```json
{
  "mcpServers": {
    "vercel": {
      "type": "http",
      "url": "https://mcp.vercel.com",
      "description": "Vercel deployments and projects"
    },
    "browser-use": {
      "type": "http",
      "url": "https://api.browser-use.com/mcp",
      "headers": {
        "x-browser-use-api-key": "YOUR_BROWSER_USE_KEY_HERE"
      }
    }
  }
}
```

### Field reference

| Field | Bắt buộc | Ý nghĩa |
|-------|----------|---------|
| `command` | ✅ (stdio) | Executable: `npx`, `uvx`, `python3`, `node`… |
| `args` | ✅ (stdio) | Array args. Convention: `["-y", "package-name"]` cho npx |
| `env` | ❌ | Env vars inject vào process (API keys, URLs) |
| `type` | ✅ (http) | `"http"` — indicator remote endpoint |
| `url` | ✅ (http) | Endpoint URL |
| `headers` | ❌ (http) | Custom headers (thường auth) |
| `description` | ❌ | Documentation, không affect loading |

### 3 scope levels của MCP config

| Scope | Path | Khi dùng |
|-------|------|----------|
| **User-level** | `~/.claude.json` | MCPs share mọi project |
| **Project-level** | `<project>/.mcp.json` | MCPs riêng project này, **share qua source control** |
| **Local override** | `<project>/.claude.json.local` | Personal overrides, KHÔNG commit |

> ⚠️ **Project-level `.mcp.json` là attack surface** (per security guide CVE). Nếu clone repo malicious → MCP auto-approve trước trust dialog. Cần verify trước khi mở unknown repo trong Claude Code.

---

## Cơ chế / How It Works

### Loading flow

```
Claude Code starts
    ↓
Đọc `~/.claude.json` (user scope)         ← global MCPs
Đọc `<project>/.mcp.json` (project scope) ← project MCPs
Đọc `<project>/.claude.json.local`         ← local overrides
    ↓
Merge MCP configs (project overrides user)
    ↓
Filter theo `disabledMcpServers` + `ECC_DISABLED_MCPS` env var
    ↓
Spawn stdio processes / connect HTTP endpoints
    ↓
Load tool schemas + resource descriptors vào context
    ↓
Claude có thể invoke tools theo schema
```

### MCP primitives

| Primitive | Purpose | Example |
|-----------|---------|---------|
| **Tools** | Actions Claude invoke | `github.create_pr`, `supabase.query` |
| **Resources** | Read-only data Claude fetch | `filesystem:///path/to/file` |
| **Prompts** | Reusable prompt templates | Claude Desktop slash commands |

### Tool schemas = context cost

Mỗi MCP enabled → tool descriptions (name, description, input schema JSON) load vào context. Tác giả shortform: "200k context window **before compacting** có thể shrink xuống 70k với quá nhiều tools enabled."

---

## Configuration: 4 cách điều khiển

### 1. Disable unused MCPs per session (KHUYẾN NGHỊ cho context discipline)

```bash
# Xem MCPs enabled
/mcp

# Disable trong Claude Code UI
/plugins   # scroll to MCP section
```

### 2. Per-project `disabledMcpServers`

```json
{
  "mcpServers": { ... },
  "disabledMcpServers": ["github", "firecrawl"]
}
```

### 3. Env var `ECC_DISABLED_MCPS`

```bash
export ECC_DISABLED_MCPS="github,context7,firecrawl"
```

Áp dụng khi install/sync ECC — không copy những MCP này vào global config.

### 4. Version pinning (KHUYẾN NGHỊ cho security)

```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github@2025.4.8"]  ← pin version
  }
}
```

ECC's own `.mcp.json` pin version mọi MCP → reproducible + supply chain protection.

> **Pattern từ tác giả (shortform):** 14 MCPs configured, ~5–6 enabled per project. **Rule of thumb:**
> - 20–30 configured OK
> - <10 enabled per session
> - <80 total tools active

---

## Recipe: Setup MCPs cho người mới / Beginner setup recipes

### Recipe 1: Minimal setup (4 MCPs, safe default)

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"],
      "description": "Live docs lookup"
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
      "description": "Chain-of-thought"
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "description": "Persistent memory"
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/your/projects"],
      "description": "Filesystem ops (set your path)"
    }
  }
}
```

> Giải thích: 4 MCP này low-risk (không external API auth), foundation cho most workflows.

### Recipe 2: Dev team setup (8 MCPs)

Thêm: `github` (cần PAT), `supabase` (nếu stack dùng), `vercel` hoặc `railway` (deployment), `playwright` (E2E testing).

### Recipe 3: Research setup

Thêm: `exa-web-search` (cần API key), `firecrawl` (web scraping, cần key).

### Recipe 4: Security-first setup

```json
{
  "disabledMcpServers": ["github", "supabase", "filesystem"],
  "permissions": {
    "deny": [
      "Read(~/.ssh/**)",
      "Read(**/.env*)"
    ]
  }
}
```

Disable by default, enable explicit per task.

---

## Security — MCP attack surface (từ Security Guide)

> **Quan trọng:** MCPs là attack surface lớn nhất. Section này kết hợp insights từ [[(C) Security Guide summary]].

### OWASP MCP Top 10 (5 categories known — còn 5 chưa verified)

| # | Category | Exploit |
|---|----------|---------|
| 1 | **Tool poisoning** | MCP tool trả về malicious output chứa prompt injection |
| 2 | **Prompt injection via contextual payloads** | Tool description có hidden instruction |
| 3 | **Command injection** | Agent execute string chưa sanitize từ tool output |
| 4 | **Shadow MCP servers** | MCP ngoài manifest chính thức, untracked |
| 5 | **Secret exposure** | MCP exfiltrate `.env`, SSH keys qua tool calls |

### Claude Code CVE liên quan MCP

**MCP consent abuse** (Check Point Feb 2026): repo-controlled MCP config + settings auto-approve project MCP servers trước user meaningful trust. → **Mọi `.mcp.json` từ repo lạ là risk.**

### Snyk ToxicSkills study liên quan

3,984 skills scanned, 36% có prompt injection → **skills và MCPs đều là supply chain artifact, cần scan**.

### Mitigation cụ thể

1. **Disable by default:** `ECC_DISABLED_MCPS` cho bundled, `disabledMcpServers` per project
2. **Version pinning:** `@x.y.z` không `@latest`
3. **Scan với AgentShield:** `npx ecc-agentshield scan` — covers MCP server risk profiling (1 trong 5 category scan)
4. **Sanitize MCP tool output:** treat như untrusted content
5. **Separate identity:** MCP có auth (GitHub PAT) → dùng short-lived scoped token, không personal PAT
6. **Short-lived credentials:** rotate API keys regularly

---

## Patterns kết hợp / Combination patterns

### MCP → CLI + Skill conversion (longform pattern)

> **Pattern tinh tế:** Convert MCP thành skill gọi CLI — tiết kiệm context, vẫn giữ ergonomics.

| Before | After |
|--------|-------|
| GitHub MCP loaded cả session, ăn context | Skill `/gh-pr` wrap `gh pr create` với preferred options, lazy-load |
| Supabase MCP eating context | Skills dùng Supabase CLI directly |

> **Trade-off:**
> - ✅ Giảm context cost
> - ✅ Tool output là plain text (weaker attack surface)
> - ❌ Không giảm token cost per call
> - ❌ Mất một số ergonomics (schema validation, auto-completion)

### MCP + Skill + Subagent (composite pattern)

Vd research workflow:
- Subagent gọi skill `research-workflow`
- Skill dùng MCP `exa-web-search` để search + `context7` lookup docs
- Skill aggregate kết quả, return summary

### MCP + Hook (audit trail)

`PostToolUse` hook log mọi MCP tool call → observability layer per security guide.

### MCP + Project-level `.mcp.json`

Team share MCP set qua source control. Mỗi dev có thể override local với `.claude.json.local` (không commit).

---

## Real-world examples từ ECC

| File | Use case |
|------|----------|
| `mcp-configs/mcp-servers.json` (27 MCPs) | Full reference configuration |
| `.mcp.json` (repo root, 6 MCPs pinned) | Minimal dev setup với version pinning |
| `examples/saas-nextjs-CLAUDE.md` | SaaS stack với Supabase + Vercel MCPs |

---

## Build your own MCP server

> Tham khảo skill `mcp-server-patterns` (4KB) nếu muốn tự build MCP.

### Quick reference

```bash
npm install @modelcontextprotocol/sdk zod
```

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const server = new McpServer({ name: "my-server", version: "1.0.0" });
```

- **Tools** (actions) — register với `registerTool()` hoặc `tool()`
- **Resources** (read-only data) — register với `registerResource()`, handler receive `uri`
- **Prompts** — reusable templates
- **Transport:** stdio (local/Claude Desktop), Streamable HTTP (Cursor, cloud)

### Best practices từ skill

- **Schema first:** Zod validation mọi tool input
- **Structured errors** (không raw stack trace)
- **Idempotency** cho safe retry
- **Rate limits + cost** document trong tool description
- **Pin SDK version** trong package.json

> **Official SDKs:** JavaScript/TypeScript (`@modelcontextprotocol/sdk`), Go, C#

---

## Anti-patterns / Sai lầm hay gặp

1. **Enable mọi MCP** → context window từ 200k shrink xuống 70k. Disable unused ngay.
2. **Dùng `@latest` version** → supply chain attack vector. Pin version cụ thể.
3. **Copy `.mcp.json` từ repo lạ mà không verify** → MCP consent abuse CVE. Review JSON trước khi mở repo.
4. **Store API key trong `env` của `.mcp.json` commit vào git** → secret leak. Dùng `.claude.json.local` (gitignored) hoặc secret manager.
5. **Keep MCP configured mà never disable** → mỗi session ăn context + tool poisoning risk. Enable-when-needed discipline.
6. **Dùng personal GitHub PAT cho MCP** → compromised MCP = compromised you. Dùng scoped fine-grained PAT.
7. **Không audit MCP tool output** → tool output là untrusted content, cần sanitize.
8. **Dùng MCP trong khi có CLI tốt** → ăn context không cần thiết. Convert sang CLI + skill.
9. **Dùng shadow MCP** (ngoài `mcp-configs/mcp-servers.json` hoặc official MCP registry) → no verification trail.
10. **Bật MCP untrusted + memory MCP cùng lúc** → lethal trifecta (private data + untrusted content + external communication). Disable 1 trong 3.

---

## Tools liên quan / Related Tools

| Tool | Vai trò |
|------|---------|
| **`/mcp`** command | List enabled MCPs |
| **`/plugins`** command | Toggle MCPs qua UI (scroll to MCP section) |
| **`ECC_DISABLED_MCPS`** env var | Disable ECC bundled MCPs khi install/sync |
| **`disabledMcpServers`** (per-project) | Per-project disable list |
| **`/security-scan`** skill | Gọi AgentShield — scan MCP server risk profiling |
| **`mcp-server-patterns`** skill | Build your own MCP server |
| **`npx ecc-agentshield scan`** | Standalone security scan, covers MCP risks |
| **OWASP MCP Top 10** | Threat categorization reference |

---

## Cross-references

- [[(C) Hooks]] — PostToolUse hook có thể log MCP tool calls cho audit
- [[(C) Skills]] — skill có thể wrap MCP hoặc replace MCP với CLI + skill
- [[(C) Subagents]] — subagent có scoped MCP permissions (principle of least privilege)
- [[(C) Rules and Memory]] — rule về secret management, memory discipline áp dụng trực tiếp
- [[(C) Shortform Guide summary]] — context discipline rule ("14 configured, 5–6 enabled")
- [[(C) Longform Guide summary]] — MCP → CLI + skill conversion pattern
- [[(C) Security Guide summary]] — MCP attack surface, OWASP MCP Top 10, CVE chi tiết
- [[(C) README summary]] — AgentShield mention + ecosystem tooling
- [[(C) index]] — main catalog
- _Sẽ link tới_ [[(C) Plugins]] khi tạo (plugin có thể bundle MCP)

## Citations

- `mcp-configs/mcp-servers.json` (full file, 6.6KB, 27 MCPs) — pre-configured bundle
- `.mcp.json` (repo root, full file) — minimal dev setup với version pinning
- `skills/mcp-server-patterns/SKILL.md` (full file, 4KB) — build-your-own MCP reference
- `the-shortform-guide.md`, lines 126–186 — MCP overview + context discipline + tác giả's setup
- `the-longform-guide.md`, lines 22–33 — MCP → CLI + skill conversion pattern
- `the-security-guide.md`, lines 34–40, 60–65 — MCP attack surface, OWASP MCP Top 10, consent abuse CVE
- `README.md`, lines 530–541 — mcp-configs folder structure
- Counts verified: `mcp-configs/mcp-servers.json` = **27 MCPs pre-configured** (2026-04-17)

---

## TODO cho lần ingest tiếp

- [ ] Google "OWASP MCP Top 10 2026" để có full list 10 category (hiện chỉ biết 5)
- [ ] Verify `permissions.deny` field là built-in Claude Code hay ECC extension (cross-ref với [[(C) Security Guide summary]] Q24)
- [ ] Đọc `docs/capability-surface-selection.md` — skill `mcp-server-patterns` mention file này, có thể có framework "rule vs skill vs MCP vs CLI" quyết định
- [ ] Đọc `skills/token-optimizer` liên quan MCP `token-optimizer` — claim "95%+ context reduction"
- [ ] Run `npx ecc-agentshield scan` trên setup Claude Code cá nhân để check MCP risks
- [ ] Compare OWASP MCP Top 10 với `rules/common/security.md` checklist — có gap coverage không?
- [ ] Verify tool schema context cost: đo 1 MCP enabled ăn bao nhiêu token (claim "1–5K tokens mỗi MCP")
