# (C) Entity 1: OAuth bridge core — `opencode-antigravity-auth` plugin

**Type:** Core product entity
**Slot:** Entity 1 of 4
**Sibling entities:** [Entity 2 — Multi-account quota-multiplexing](entity-2-multi-account-quota-multiplexing.md) / [Entity 3 — Antigravity Unified Gateway](entity-3-antigravity-unified-gateway.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. Identity

**Repository:** [github.com/NoeFabris/opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)
**NPM package:** `opencode-antigravity-auth` (`@latest` + `@beta` channels)
**Author:** NoeFabris ([@dopesalmon](https://x.com/dopesalmon))
**License:** MIT
**Current version:** v1.6.0 (released 2026-02-20)
**First release:** v1.0.0 (2025-12-10) — 159 days old at wiki build
**Stats at v67 wiki build:** 10,500 stars / 1 fork / 29 watchers / 30 open issues / 691 commits / 91 releases

---

## 2. What it does (one-paragraph)

`opencode-antigravity-auth` is a runtime plugin for the open-source [Opencode](https://github.com/sst/opencode) AI coding assistant that intercepts outgoing `fetch()` requests to Google's `generativelanguage.googleapis.com` and routes them through Google's Antigravity Unified Gateway API. With the plugin installed and authenticated, an Opencode user gains access to Claude Opus 4.6, Claude Sonnet 4.6, Gemini 3 Pro/Flash, and Gemini 3.1 Pro — all billed against the user's Google Antigravity quota rather than Anthropic or Google direct API spend. Multi-account rotation, dual-quota-pool routing, session recovery, and Claude-thinking-block handling are all bundled in the same plugin.

---

## 3. Architectural role

The plugin sits between Opencode (the AI coding assistant runtime) and Google's Antigravity API (the closed-vendor Unified Gateway). It is a **T4 Bridge** in the corpus taxonomy — neither an agent framework nor a service primitive nor a documentation archive, but a translation layer between two incompatible API contracts.

```
┌─────────────────────────────────────────────────────────────────┐
│  OpenCode ──▶ Plugin ──▶ Antigravity API ──▶ Claude/Gemini      │
│     │           │              │                   │            │
│     │           │              │                   └─ Model     │
│     │           │              └─ Google's gateway (Gemini fmt) │
│     │           └─ THIS PLUGIN (auth, transform, recovery)      │
│     └─ AI coding assistant                                      │
└─────────────────────────────────────────────────────────────────┘
```

The plugin's contract with Opencode is: *receive `fetch()` to Gemini generative-language endpoints; transform; forward to Antigravity; transform response back.* The contract with Antigravity is: *send Gemini-formatted requests with antigravity headers + valid OAuth Bearer token; receive `candidates[]`-shaped responses.*

---

## 4. Module decomposition

15 source modules organized into 4 architectural layers (per AGENTS.MD §"Module Structure"):

**Entry layer (1 module):**
- `plugin.ts` — Main entry point, fetch interceptor

**OAuth layer (2 modules):**
- `antigravity/oauth.ts` — OAuth token exchange
- `plugin/auth.ts` — Token validation & refresh

**Request/response transformation layer (4 modules):**
- `plugin/request.ts` — Request transformation (core logic)
- `plugin/request-helpers.ts` — Schema cleaning, thinking filters
- `plugin/thinking-recovery.ts` — Turn boundary detection
- `plugin/recovery.ts` — Session recovery (`tool_result_missing`)

**State + multi-account layer (6 modules):**
- `plugin/quota.ts` — Quota checking (API usage stats)
- `plugin/cache.ts` — Auth & signature caching
- `plugin/accounts.ts` — Multi-account management & storage
- `plugin/storage.ts` — Persistent storage schemas (Zod)
- `plugin/fingerprint.ts` — Device fingerprint generation & headers
- `plugin/project.ts` — Managed project context resolution

**Plus** `constants.ts` (endpoints, headers, API config, system prompts) + `plugin/debug.ts` (debug logging).

---

## 5. The six design patterns (from AGENTS.MD)

1. **Request interception** — fetch() interceptor on `generativelanguage.googleapis.com` URLs
2. **Claude thinking blocks stripped (ALL of them)** — eliminates signature validation errors
3. **Session recovery** — synthetic `tool_result` injection when execution is interrupted
4. **Schema sanitization** — allowlist (`const` → `enum`, strip `$ref`/`$defs`/etc.)
5. **Multi-account load balancing** — dual quota pools + per-account fingerprints
6. **Fingerprint system** — per-account `deviceId`/`sessionToken`/`userAgent` mimicking Antigravity Manager

These six concerns map cleanly to the 4 architectural layers: request interception (entry) + Claude thinking (transformation) + session recovery (transformation) + schema sanitization (transformation) + multi-account (state) + fingerprint (state).

---

## 6. The Claude-thinking-block decision (architectural commitment)

The plugin's most consequential single architectural decision is to **strip all thinking blocks from outgoing Claude requests**. The documented tradeoff (from `docs/ARCHITECTURE.md`):

> *"OpenCode stores thinking blocks, but may corrupt signatures. Solution: Strip ALL thinking blocks from outgoing requests. Why this works: Zero signature errors (impossible to have invalid signatures). Same quality (Claude sees full conversation, re-thinks fresh). Simpler code (no complex validation/restoration)."*

This is **principled-information-discard for simpler-correctness** — the plugin accepts the cost of Claude re-thinking each turn (additional compute + latency) in exchange for eliminating an entire class of failure modes (corrupted signature responses).

A second-order workaround handles Claude's tool-use requirement (thinking must precede `tool_use`):
1. Cache signed thinking from response (`lastSignedThinkingBySessionKey`)
2. On subsequent requests, inject cached thinking before `tool_use`
3. Only inject for first assistant message of a turn

The turn-boundary detection (in `thinking-recovery.ts`) explicitly defines: *"A 'turn' starts after a real user message (not tool_result). Only inject thinking into first assistant message after that."*

---

## 7. Session recovery: synthetic message injection

When tool execution is interrupted (ESC / timeout / crash), Anthropic's API returns:

> `Error: tool_use ids were found without tool_result blocks immediately after`

The plugin's recovery flow (`recovery.ts`):

1. Detect via `session.error` event
2. Fetch session messages via `client.session.messages()`
3. Extract `tool_use` IDs from failed message
4. Inject synthetic `tool_result` blocks:
   ```typescript
   { type: "tool_result", tool_use_id: id, content: "Operation cancelled" }
   ```
5. Send via `client.session.prompt()`
6. Optionally auto-resume with `"continue"`

A second recovery path handles `Expected thinking but found text` errors by closing the corrupted turn with synthetic messages and starting fresh.

**Architectural pattern:** synthetic-message-injection-as-API-protocol-repair. The plugin upholds the API's protocol invariants by inserting messages that make the API-side state machine happy, hiding the underlying failure from the user.

---

## 8. Schema sanitization (allowlist approach)

The Antigravity API has strict JSON Schema requirements (per `docs/ANTIGRAVITY_API_SPEC.md`):

**Kept:** `type`, `properties`, `required`, `description`, `enum`, `items`, `anyOf`, `allOf`, `oneOf`, `additionalProperties`
**Removed:** `const`, `$ref`, `$defs`, `default`, `examples`, `$schema`, `$id`, `title`

**Transformations:** `const: "value"` → `enum: ["value"]` ; Empty object schema → placeholder `reason` property.

The allowlist approach means new JSON Schema features added by upstream tools (e.g., MCP servers) won't accidentally leak through to Antigravity's strict validator. This is **bridge-correctness-as-default-deny**.

---

## 9. Dependencies + technical baseline

**Runtime dependencies (5):**
- `@opencode-ai/plugin@^0.15.30` — host plugin interface
- `@openauthjs/openauth@^0.4.3` — OAuth client
- `proper-lockfile@^4.1.2` — concurrent-access file locking
- `xdg-basedir@^5.1.0` — XDG-compliant config-path resolution
- `zod@^4.0.0` — schema validation (explicitly NOT v3)

**Engine baseline:** Node ≥20
**Build:** TypeScript 5+ with strict + `noUncheckedIndexedAccess` + `noImplicitOverride` + `verbatimModuleSyntax`
**Tests:** Vitest 3 + colocated `*.test.ts` files + E2E `test:e2e:models` + `test:e2e:regression` scripts (live-endpoint testing)
**No linter, no formatter** — style enforced by convention

---

## 10. Forbidden practices (TypeScript discipline)

The AGENTS.MD enforces explicit forbidden patterns:
- No `as any`
- No `@ts-ignore`
- No `@ts-expect-error`

Combined with strict mode + `noUncheckedIndexedAccess`, this is **strictness-as-correctness-pre-condition** — the plugin's fetch-interception + format-translation reliability depends on absolute type discipline. There is no escape hatch.

---

## 11. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md)** | Same T4 Bridge archetype: OpenAI publishes Apache-2.0 plugin bridging Codex to Claude Code. Both single-author plugins bridging cross-vendor agentic ecosystems. Counter-direction: codex-plugin-cc bridges *into* Claude Code; opencode-antigravity-auth bridges *into* Opencode (the open-source Claude Code competitor). |
| **[v65 claude-code-system-prompts](../../claude-code-system-prompts - Beginner Analysis/CLAUDE.md)** | Same closed-vendor-product-surface engagement axis. Antigravity Unified Gateway API spec (this plugin's docs/ANTIGRAVITY_API_SPEC.md) is a discovered-via-empirical-testing artifact, analogous to claude-code-system-prompts' continuous reverse-engineering of Claude Code internals. |
| **[v66 agentmemory](../../agentmemory - Beginner Analysis/CLAUDE.md)** | Recent solo-author npm plugin in adjacent corpus position. agentmemory is T2 Service on Platform-Primitive Foundation; opencode-antigravity-auth is T4 Bridge auth-plugin. Different mechanisms but adjacent solo-author-npm-plugin archetype. |

---

## 12. Counter-evidence + Pattern Library implications

- **Pattern #66 meta-supply-chain-awareness (CONFIRMED v59-ish):** STRENGTHENING evidence. The plugin's existence depends on Google's continued tolerance of Antigravity gateway access; engineering response includes platform masquerading, fingerprint diversity, soft-quota thresholds.
- **Pattern #76 Adversarial Subagent Review Architecture (CANDIDATE N=1):** No evidence — orthogonal to this subject's architecture.
- **Pattern #85 Platform-Primitive Foundation (CANDIDATE N=1, v66 NEW):** NOT N+1 evidence. The plugin uses `@opencode-ai/plugin` as a dependency but does not self-identify as a running instance of Opencode, does not count internals in Opencode units, and does not extend via Opencode CLI. It's an ordinary heavy-dependency plugin.
- **NEW observational candidate: Adversarial-Detection-Tolerant Architecture** — 8+ sub-mechanisms (request interception + fingerprint diversity + timing jitter + header randomization + per-account fingerprint persistence + fingerprint history rotation + soft quota thresholds + platform masquerading) constitute integrated defensive surface against vendor enforcement.

---

## 13. References

- README.md (718 lines, primary)
- AGENTS.MD (144 lines)
- docs/ARCHITECTURE.md (302 lines)
- package.json (66 lines)
- Cross-cluster: `cluster-1-readme-and-tos-framing.md` + `cluster-2-contributor-and-architecture.md`
