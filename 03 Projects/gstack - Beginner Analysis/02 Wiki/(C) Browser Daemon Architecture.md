# (C) Browser Daemon Architecture

> **Source:** `00 Sources/gstack/ARCHITECTURE.md` (lines 1-120 + security section), CLAUDE.md browser section
> **Ingested:** 2026-04-18
> **Type:** Entity page (technical concept) — entity #3 cho gstack

---

## One-liner

**VI:** Browser Daemon Architecture là **điểm kỹ thuật độc đáo nhất của gstack** — long-lived Chromium + Bun HTTP server + localhost-only + bearer token auth + per-session UUID + binary hash version auto-restart. Result: agent có **~100-200ms latency per browser command** (vs 2-3s cold start), **persistent state across commands** (cookies, tabs, localStorage), và **security discipline** (cookies never on disk, keychain per-session, shell injection prevention).

**EN:** Browser Daemon is gstack's most technically distinctive piece — long-lived Chromium + Bun HTTP server + localhost + bearer token + UUID-per-session + binary-hash auto-restart. Gives agent sub-second browser latency + persistent state + security discipline.

---

## Khi nào dùng concept này

**Hữu ích khi:**
- Hiểu vì sao `/qa` + `/design-review` + `/browse` hoạt động được với real browser
- Design automation tooling cần long-lived process với CLI client
- Compare với Playwright MCP (slow, cold-start) or Puppeteer MCP
- Security audit gstack trước enterprise use

**Không cần để dùng gstack cơ bản** — daemon auto-starts, auto-shuts. Transparent.

---

## Comparison sibling

| Mechanism | Browser Daemon (gstack) | Playwright MCP | Browser-Use agent |
|-----------|------------------------|----------------|-------------------|
| Startup cost | ~3s first call, ~100ms after | 2-3s per command | Varies |
| State persistence | ✅ Cookies/tabs/localStorage persist | ❌ Loses between commands | ❌ Session-based |
| Security model | Localhost + bearer token + mode 0o600 state file | MCP stdio | Generic |
| Multi-agent support | ✅ Via `/pair-agent` (same browser, different tabs) | Limited | No |
| Agent latency | Sub-second | Slower | Varies |
| Auto-restart | Binary hash version change → kill+restart | Manual | Manual |
| Idle lifecycle | Auto-shutdown 30 min | Persistent | Session |

→ **Distinctive:** gstack's daemon model outperforms Playwright MCP cho long agent sessions.

---

## Sub-types: Daemon components

### 1. CLI (compiled binary)

- Source: `browse/src/` (TypeScript)
- Compiled: `bun build --compile` → ~58MB Mach-O binary (arm64 only currently)
- Installed path: `browse/dist/browse` + `browse/dist/find-browse`
- Responsibility: reads state file, POST /command to localhost:PORT

### 2. Server (Bun.serve())

- Entry: `bun run server.ts` during dev
- Responsibility: dispatches commands, talks to Chromium via CDP, returns plain text
- Framework: built-in `Bun.serve()` (no Express/Fastify)
- Routes: ~10 total

### 3. Chromium (headless)

- Launched via Playwright
- Anti-bot stealth (`/open-gstack-browser` variant)
- Branding: "GStack Browser" menu bar (vs "Chrome for Testing")
- Idle timeout: 30 minutes
- Persistent user profile (cookies, localStorage)

### 4. State file

Path: `.gstack/browse.json`
Mode: `0o600` (owner-only read)
Schema:
```json
{
  "pid": 12345,
  "port": 34567,
  "token": "uuid-v4",
  "startedAt": "2026-04-18T...",
  "binaryVersion": "abc123"
}
```
Atomic write via tmp + rename.

### 5. Keychain cache (macOS)

- Per-session cache of Keychain password + derived AES-128 key
- In-memory only, cleared on shutdown
- User must approve on first cookie import ("Allow"/"Always Allow")

---

## Anatomy: Request flow

```
1. Claude Code runs: $B snapshot -i
2. CLI binary reads .gstack/browse.json
   - If missing → spawn new server
   - If present → HTTP GET /health
3. If server healthy:
   - POST /command
   - Authorization: Bearer <token>
   - Body: {"cmd": "snapshot", "args": {"interactive": true}}
4. Server dispatches via CDP to Chromium
5. Chromium returns accessibility tree + refs (@e1, @c1)
6. Server formats as plain text, returns HTTP 200
7. CLI prints text to stdout
8. Claude Code agent reads stdout, uses refs in next command
```

**Latency breakdown:**
- First call: ~3s (Chromium cold start + server init)
- Subsequent: ~100-200ms (HTTP roundtrip + Playwright page.accessibility.snapshot())

---

## Cơ chế: Key mechanisms

### Mechanism 1: Persistent tabs + cookies

**Why daemon beats per-command:** 20+ QA commands without daemon = 40+ seconds startup overhead. State (cookies, login, tabs) lost between.

**With daemon:**
- Login once → stays logged in across commands
- Open tab once → persists
- localStorage preserved → test stateful flows

### Mechanism 2: Random port selection (10000-60000)

Retry up to 5 on collision.

**Why random vs fixed:** 10 Conductor workspaces each run own daemon → zero config, zero port conflicts. Old approach (scan 9400-9409) broke in multi-workspace setups.

### Mechanism 3: Binary-hash auto-restart

- Build writes `git rev-parse HEAD` → `browse/dist/.version`
- Each CLI invocation compares binary version vs running server's `binaryVersion`
- Mismatch → CLI kills old server, spawns new

**Result:** "Stale binary" bug class eliminated. Rebuild → next command picks up automatically.

→ **Reusable pattern** cho long-lived services.

### Mechanism 4: Bearer token auth

Every session generates UUID → written to state file mode 0o600.
All HTTP requests must include `Authorization: Bearer <token>`.
Mismatch → 401.

**Exempt endpoints:**
- `/health` (GET) — server liveness, no commands
- `/cookie-picker` (GET) — UI only, localhost-reachable

→ **Prevents other processes on same machine from talking to your browse server.**

### Mechanism 5: Cookie security (5 layers)

1. Keychain access requires user approval (macOS dialog)
2. Decryption in-process (PBKDF2 + AES-128-CBC), never disk plaintext
3. Cookie DB read-only (gstack copies to temp, opens read-only, never modifies real browser DB)
4. Key caching per-session (cleared on shutdown)
5. No cookie values in logs (metadata only: domain, name, expiry)

### Mechanism 6: Shell injection prevention

- Browser registry hardcoded (Comet, Chrome, Arc, Brave, Edge)
- DB paths constructed from known constants, never user input
- Keychain access uses `Bun.spawn()` with explicit argument arrays, not shell strings

---

## Out-of-box behavior

**On fresh install:**
- CLI binary auto-builds via `./setup`
- No daemon running until first `$B` command
- First `$B goto https://example.com`:
  - Spawns server (~3s)
  - Launches headless Chromium
  - Navigates
  - Returns HTTP 200 response

**Idle:**
- After 30 min no commands → server auto-shutdown
- Chromium killed
- State file removed

**Force restart:** Next command detects stale state → spawns new server.

---

## Configuration knobs

| Knob | Where | Default | Effect |
|------|-------|---------|--------|
| Idle timeout | Server constant | 30 min | Chromium alive this long |
| Port range | Server constant | 10000-60000 | Random + retry |
| `anti_bot_stealth` | Command flag | on for GStack Browser | vs "Chrome for Testing" |
| `headed` mode | `/open-gstack-browser` | headless default | Visible browser for debug |
| Windows fallback | Auto-detect | Node.js fallback for Bun pipe bug | bun#4253 |

→ **Minimal user knobs.** Design philosophy: opinionated, not configurable.

---

## Recipes

### Recipe 1: Debug failing /qa run

```bash
# Check daemon state
cat .gstack/browse.json

# Manual health check (bypass CLI)
TOKEN=$(jq -r .token .gstack/browse.json)
PORT=$(jq -r .port .gstack/browse.json)
curl -H "Authorization: Bearer $TOKEN" http://localhost:$PORT/health

# Force restart
pkill -f "gstack.*browse"
rm .gstack/browse.json
$B goto https://example.com  # respawns
```

### Recipe 2: Share browser across agents (`/pair-agent`)

```
/pair-agent openclaw
```

gstack prints setup instructions. Paste into OpenClaw. OpenClaw exchanges setup key for session token, creates own tab, starts browsing.

**Result:** 2 agents in same browser, different tabs, scoped tokens, tab isolation, rate limiting.

→ First time AI agents from different vendors coordinate through shared browser with real security.

### Recipe 3: Import cookies from real browser

```bash
$B setup-cookies
```

- Detects Chrome/Arc/Brave/Edge
- Prompts Keychain approval (first time)
- Copies cookies to temp DB
- Decrypts in-process, loads into Playwright context
- Never writes plaintext cookies to disk

### Recipe 4: Handoff to headed browser (auth walls)

Hit CAPTCHA/MFA? `$B handoff` opens visible Chrome at exact same page with cookies and tabs intact.

Solve problem manually. `$B resume` picks up where left off.

> "Agent even suggests handoff automatically after 3 consecutive failures."

### Recipe 5: Multi-workspace (Conductor)

Each Conductor workspace has own `.gstack/browse.json` → own daemon → own port. No cross-pollution.

---

## Advanced patterns

### Pattern: Long-lived process via ephemeral CLI

CLI exits after each command. Server persists. State file bridges them.

→ **Reusable cho any long-running service** với CLI client: DB shells, dev servers, language servers.

### Pattern: Binary hash invalidation

Version check on every CLI call → auto-reload on rebuild. Eliminates "restart your server" friction.

### Pattern: Random port + state file discovery

Multiple daemons coexist without config. Scalable to 10+ parallel workspaces.

### Pattern: Security via localhost + bearer + file mode

Three-layer security:
1. Localhost (not `0.0.0.0`) — no network reach
2. Bearer token — other processes can't talk
3. State file mode 0o600 — other users can't read token

→ Defense in depth cho dev-time service.

### Pattern: Read-only DB copy for cookie import

Copy SQLite to temp + open read-only → never touches user's real browser DB. Safe.

---

## Combination với building blocks khác

### + Specialist Roles
`/qa`, `/design-review`, `/devex-review`, `/browse`, `/setup-browser-cookies`, `/open-gstack-browser` all require daemon running.

### + Sprint Pipeline
Test phase ("Test" stage) depends on daemon. Without daemon = lose `/qa`'s "agent has eyes" superpower.

### + Multi-Host Platform
Daemon is Claude Code-primary. On other hosts, similar model but symlinks differ.

### + `/pair-agent` (Multi-Agent Coordination)
Daemon's bearer token + tab isolation makes `/pair-agent` security-sound.

### Cross-project: + ECC AgentShield
Both prioritize security. gstack enforces via architecture (localhost + bearer); ECC via scanner (AgentShield audit).

### Cross-project: + Superpowers zero-dep philosophy
Convergent: Superpowers bans external deps for server.js; gstack uses Bun + Playwright (bundled). Different trade-offs:
- Superpowers: zero-dep = auditable supply chain
- gstack: opinionated-dep = batteries-included, faster

---

## Anti-patterns

❌ **Use `mcp__claude-in-chrome__*` tools** — CLAUDE.md explicitly bans: "slow, unreliable, not what this project uses."

❌ **Commit `browse/dist/` binaries** — Mach-O arm64 only, breaks on Linux/Windows/Intel. Use `./setup` to build locally.

❌ **Bind server to `0.0.0.0`** — would expose to network. Localhost-only is intentional security.

❌ **Disable bearer token auth "for dev"** — all HTTP requests need token. Zero-exception.

❌ **Log cookie values "for debugging"** — explicit rule: metadata only (domain/name/expiry). Values truncated.

❌ **Manual kill + restart during dev** — binary hash auto-restart handles it. Manual `pkill` unnecessary.

❌ **Run 10 Conductor workspaces with shared state file** — each workspace needs own `.gstack/browse.json`. Share = race conditions.

❌ **Expect Windows pipe transport to work** — Bun has known bug (bun#4253). Node.js fallback required + Node must be on PATH.

---

## Cross-references

- [[(C) Sprint Pipeline]] — test phase consumes daemon
- [[(C) Specialist Roles]] — roles that depend on daemon
- [[(C) Multi-Host Declarative Platform]]
- [[(C) ETHOS + ARCHITECTURE summary]] — philosophical context
- [[(C) CLAUDE.md summary]] — "NEVER use mcp__claude-in-chrome__*" rule
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Distribution Model.md` — different arch philosophy

## Citations

- ARCHITECTURE.md lines 1-120 (daemon model + Bun rationale + state file + port selection + version auto-restart + security model)
- ARCHITECTURE.md lines 112-160 (ref system)
- CLAUDE.md "Browser interaction" section
- CHANGELOG v0.18.3.0 (persistence fix entry) confirms daemon lifecycle dynamics

## TODO

- ⏸ Read `browse/src/server.ts` source to verify exact Bun.serve routes
- ⏸ Confirm 4-Layer Prompt Injection Defense (v0.15.12.0) implementation location
- ⏸ Deep-dive `accessibility.snapshot()` → ref format. Worth entity page if reusable pattern
- ⏸ Pretext layout (30KB zero-deps CSS) — separate concern, investigate separately
