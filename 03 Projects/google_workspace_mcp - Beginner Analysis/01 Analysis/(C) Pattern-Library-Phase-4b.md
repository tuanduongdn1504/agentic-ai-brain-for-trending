# (C) google_workspace_mcp — Pattern Library Phase 4b (v140)

**Routine v2.6 · §28 anti-re-accumulation discipline (single registry / ≤2-new-standalones-per-wiki / clustering-first / filing-is-an-act).**

## PRIMARY — 1 NEW Library-vocab standalone (FILED to registry 06 §C)

### "Graduated / Least-Privilege Tool-Exposure for a Large-Surface MCP Server" — N=1 CORPUS-FIRST
- **What:** A server with a large tool surface (50+ tools across 12 services) exposes them in **cumulative tiers** — `--tool-tier core | extended | complete` — so a deployment registers only the capability/permission band it needs. *Core* = essential read/search/create; *Extended* += management ops (labels, batch, advanced search); *Complete* = full API (comments, headers/footers, publishing).
- **Why it's its own mechanism:** the tier gates **which tools are registered with the client at all** (and therefore which OAuth scopes + API-quota surface are requested) — a least-privilege / blast-radius control at the *tool-registration* layer. It is **distinct from**:
  - **Library-vocab #20 Token-Economy-Quantification** — #20 quantifies token cost; tiers are primarily about **permission-scope + API-quota + tool-count surface**, only *secondarily* about the agent's tool-list size (the README's own rationale is quota/scope, not tokens — recorded honestly).
  - **v98 progressive-disclosure-per-skill** — that loads a *skill body* on demand; this chooses *which server tools exist* up front.
- **Distinct from prior MCP subjects** (v66 agentmemory / v70 codegraph / v119 nature-MCP / v132 supermemory) — none expose a graduated tool-tier flag; those have a fixed tool set.
- **Promotion-eligibility:** N=2 if a 2nd MCP server ships a graduated/tiered tool-exposure control. **Stale-watch ~v155** (auto-retire N=1 at 15 wikis per §2/§28 if no 2nd instance).
- **§28 new-standalone count this ship = 1 (≤ 2).** Registry 06 §C actually edited (rule-5: filing is an act, not a claim).

## SECONDARY — instance notes / observations (NOT minted, §28-disciplined)

- **Pattern #18 sub-mechanism B1 "MCP / one-binary-many-CLIENTS" — N+1 strengthening.** Strong instance: one server, ≥4 MCP clients (Claude Desktop / Claude Code / VS Code MCP / LM Studio / any MCP-1.0). Top-level count UNCHANGED; B1 line continues (v70 anchor).
- **Pattern #84 multi-harness / cross-client tolerance — N+1 (modest).** One protocol (MCP) → many clients; not N native config formats, so weaker than a true 84c.2 multi-format generator.
- **Multi-Tenant / Stateless MCP Server — OBSERVATION (corpus-first, NOT minted).** OAuth 2.1 multi-user bearer tokens + `WORKSPACE_MCP_STATELESS_MODE` (no on-disk credentials, in-memory token store, containerized/ephemeral). Most corpus MCP servers are single-user local-stdio; this is the first multi-tenant/stateless one. Logged as an observation; mint only on a genuine 2nd instance (clustering-first; did NOT spend the §28 cap on it).
- **Bundled-Claude-skill-augments-its-own-MCP-server — OBSERVATION.** `skills/managing-google-workspace/` exists to improve the agent's *routing to* the server's tools (a skill paired with a server). Skill-routing-cluster adjacency; agentskills.io-*adjacent* (directory artifact, NOT a 57k `npx skills add` implementer). OBSERVATION, not minted.
- **FastMCP (jlowin) framework adoption — OBSERVATION.** FastMCP 2.13.0+ with native `GoogleProvider` (DCR + CORS for OAuth 2.1). Notes the maturing OSS MCP-server-framework layer; NOT an Anthropic product (explicit correction).
- **Pattern #66 supply-chain — thin/clean.** OAuth 2.0/2.1, Fernet credential encryption, optional GCS/Valkey backends, service-account domain-wide delegation.

## Pattern Library state change: NONE
46 confirmed / ~25 active / 8 Library-vocab CONFIRMED → UNCHANGED. PROVISIONAL standalone surface +1 (the tiered-tool-exposure item). NO top-level Pattern, NO tier sub-archetype, NO confirmed-count movement.

## Audit hand-off note
The ~v139–v140 audit (already due/overdue per the shim) OWES, among others, the **generate-vector promote-vs-split** decision (v118/v134/+v137-candidate). v140 does NOT touch that thread (an MCP integration server is neither a knowledge-wiki-generator nor a skill-generator). v140 adds: the new tiered-tool-exposure N=1 + the multi-tenant/stateless-MCP and FastMCP-framework observations for the audit's MCP-cluster review (Pattern #18 B1 is getting dense — v66/v70/v119/v132/v134/v140 — worth an audit pass on whether an "MCP-server" tier sub-archetype is forming, but NOT minted here).
