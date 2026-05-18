# (C) Cluster 2: Contributor docs + Architecture

**Sources:**
- [AGENTS.MD](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/AGENTS.MD) (144 lines)
- [docs/ARCHITECTURE.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/ARCHITECTURE.md) (302 lines, *"Last Updated: April 2026"*)
- [package.json](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/package.json) (66 lines)

**Cluster focus:** Module layout, code style, Claude-specific handling, session recovery, schema sanitization, dependencies.

---

## 1. AGENTS.MD positioning + governance role

The file is named **`AGENTS.MD`** (uppercase `.MD`, contra the common `AGENTS.md` filename). It self-describes verbatim:

> *"Guidance for AI agents working with this repository."*

This is the **5th corpus subject** with explicit `AGENTS.md`-style governance:
- v32 `claude-howto` had `AGENTS.md` baseline (Pattern #18 corpus baseline)
- v53+ multiple subjects through v66 corpus-cited as standard governance file
- opencode-antigravity-auth's variant is `.MD` casing (filesystem case-insensitive on macOS/Windows; case-sensitive on Linux)

The file establishes **build commands + TypeScript config + code style + module structure + key design patterns + dependencies + testing** — a near-complete onboarding doc for AI coding agents.

---

## 2. Module structure (verbatim from AGENTS.MD)

```
src/
├── plugin.ts                # Main entry, fetch interceptor
├── constants.ts             # Endpoints, headers, API config, system prompts
├── antigravity/oauth.ts     # OAuth token exchange
└── plugin/
    ├── auth.ts              # Token validation & refresh
    ├── request.ts           # Request transformation (core logic)
    ├── request-helpers.ts   # Schema cleaning, thinking filters
    ├── thinking-recovery.ts # Turn boundary detection
    ├── recovery.ts          # Session recovery (tool_result_missing)
    ├── quota.ts             # Quota checking (API usage stats)
    ├── cache.ts             # Auth & signature caching
    ├── accounts.ts          # Multi-account management & storage
    ├── storage.ts           # Persistent storage schemas (Zod)
    ├── fingerprint.ts       # Device fingerprint generation & headers
    ├── project.ts           # Managed project context resolution
    └── debug.ts             # Debug logging utilities
```

13 modules in a `plugin/` sub-package plus `plugin.ts` entry + `constants.ts` + `antigravity/oauth.ts`. Total ~15 source modules.

**Corpus observation:** The module split makes auth/state/transformation/recovery/fingerprint explicit separate concerns. This is **separation-of-concerns at the bridge-plugin level** — each architectural concern (OAuth lifecycle vs. request transformation vs. recovery vs. anti-detection fingerprinting) gets its own module. v66 agentmemory was ~6 source modules; v62 codex-plugin-cc was ~10 commits total (very few modules). opencode-antigravity-auth's module count is **corpus-high for a solo-utility plugin**.

---

## 3. TypeScript discipline (AGENTS.MD §"TypeScript Configuration")

Strictness flags enabled:
- `strict: true`
- `noUncheckedIndexedAccess`
- `noImplicitOverride`
- `noFallthroughCasesInSwitch`
- `verbatimModuleSyntax: true` — forces `import type` for type-only imports

Module config:
- `target: ESNext`, `module: Preserve`, `moduleResolution: bundler`
- `allowImportingTsExtensions: true` — `.ts` extensions in imports
- **No path aliases** — all imports relative

**Forbidden patterns** (explicit):
- No `as any`
- No `@ts-ignore`
- No `@ts-expect-error`

**Corpus observation:** This is the most strict TypeScript discipline observed in a corpus solo-utility subject. v62 codex-plugin-cc was 100% JavaScript (no TypeScript). v66 agentmemory used TypeScript but with looser flags. opencode-antigravity-auth's "no escape-hatch" discipline (no any/ignore/expect-error) is **strictness-as-correctness-pre-condition** — strict types are required for the plugin's fetch-interception + transformation reliability.

---

## 4. Code style (AGENTS.MD §"Code Style")

- 2-space indent / double quotes / trailing commas in multiline constructs / **no semicolons** (explicit project convention)
- `camelCase` functions/variables; `PascalCase` types/interfaces/classes; `UPPER_SNAKE_CASE` constants; `kebab-case` file names; `*.test.ts` colocated with source
- No `I` prefix on interfaces; no `Type` suffix
- Named exports only in `src/` — no default exports
- Async functions with **targeted try/catch (not blanket)**

Error handling discipline:
- Defensive try/catch with **graceful degradation** (fallback values, not crashes)
- Custom error classes with metadata when domain-specific
- Catch `unknown`, log, and convert to domain errors — **never empty catch blocks**
- Rate limit / quota errors trigger **account rotation, not failure**

**Corpus observation:** The phrase *"Rate limit / quota errors trigger account rotation, not failure"* is itself a corpus-first error-handling discipline statement. Most frameworks would surface a rate-limit as an error to the user; this plugin's discipline is to make it **invisible to the user** by rotating accounts. This is **graceful-degradation-by-design** at the auth layer.

---

## 5. Six key design patterns (verbatim section titles)

From AGENTS.MD §"Key Design Patterns":

1. **Request Interception** — Plugin intercepts `fetch()` for `generativelanguage.googleapis.com`, transforms to Antigravity format. Two header styles: `antigravity` (Electron-style UA + fingerprint) and `gemini-cli` (nodejs-client UA).
2. **Claude Thinking Blocks** — ALL thinking blocks are stripped from outgoing requests for Claude models. Claude generates fresh thinking each turn. This eliminates signature validation errors.
3. **Session Recovery** — When tool execution is interrupted (ESC/timeout), the plugin injects synthetic `tool_result` blocks to recover the session without starting over.
4. **Schema Sanitization** — Tool schemas are cleaned via allowlist. Unsupported fields (`const`, `$ref`, `$defs`) are removed or converted to Antigravity-compatible format.
5. **Multi-Account Load Balancing** — Accounts rotate on rate limits. Gemini has dual quota pools (Antigravity headers + Gemini CLI headers). Fingerprints are per-account and regenerated on capacity exhaustion.
6. **Fingerprint System** — Per-account device fingerprints stored in `antigravity-accounts.json`. Each fingerprint includes `deviceId`, `sessionToken`, `userAgent`, and a reduced `clientMetadata` (`ideType`, `platform`, `pluginType` — no `osVersion`, `arch`, or `sqmId`). The only header composed is `User-Agent`, built by `buildFingerprintHeaders()` in `fingerprint.ts` and applied on the antigravity request path in `request.ts`. History tracked (max 5), restorable.

**Corpus observation #1:** The combination of patterns #1 (request interception) + #6 (fingerprint system) + #5 (multi-account rotation) constitutes a **deliberate anti-detection architecture** — the plugin spends significant code mimicking Antigravity Manager's exact behavior (UA strings, header shapes, client metadata fields) to avoid triggering vendor-side anomaly detection. This is operationally distinct from "just making the API call work" — it's defending against vendor enforcement.

**Corpus observation #2:** Pattern #2 (strip ALL thinking blocks) is corpus-first — it documents an explicit architectural decision to **discard signed model state** for correctness reasons. Comment from ARCHITECTURE.md is precise:

> *"OpenCode stores thinking blocks, but may corrupt signatures. Solution: Strip ALL thinking blocks from outgoing requests. Why this works: Zero signature errors (impossible to have invalid signatures). Same quality (Claude sees full conversation, re-thinks fresh). Simpler code (no complex validation/restoration)."*

This is **principled-information-discard for simpler-correctness** — accepting redundant compute (re-thinking) in exchange for eliminating an entire failure mode (corrupted signatures).

---

## 6. Architecture overview (docs/ARCHITECTURE.md, *Last Updated: April 2026*)

The architecture doc dates `April 2026` but the latest CHANGELOG entry is `2026-02-20` (v1.6.0). **2-month documentation lag** is fairly tight for a 91-release / 5-month-old project; observable maintainer discipline.

ASCII diagram (verbatim):

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

The plugin intercepts requests to `generativelanguage.googleapis.com`, transforms them for the Antigravity API, and handles authentication, rate limits, and error recovery.

**Architectural insight:** Antigravity uses Gemini-style format for ALL models including Claude. ANTIGRAVITY_API_SPEC explicitly states: *"Must use Gemini-style format. Anthropic-style messages array is NOT supported."* So when invoking Claude through Antigravity, the plugin is **Gemini-format-in / Gemini-format-out** even though the underlying model is Anthropic Claude. Google internally routes via Vertex AI for Claude / Gemini API for Gemini, but the plugin sees one unified Gemini-style format.

---

## 7. Request flow (ARCHITECTURE.md §"Request Flow")

### Stage 1: Interception (`plugin.ts`)

```typescript
fetch() intercepted → isGenerativeLanguageRequest() → prepareAntigravityRequest()
```

- Account selection (round-robin, rate-limit aware)
- Token refresh if expired
- **Endpoint fallback: daily → autopush → prod**

### Stage 2: Request transformation (`request.ts`)

| Step | What Happens |
|------|--------------|
| Model detection | Detect Claude/Gemini from URL |
| Thinking config | Add `thinkingConfig` for thinking models |
| Thinking strip | Remove ALL thinking blocks (Claude) |
| Tool normalization | Convert to `functionDeclarations[]` |
| Schema cleaning | Remove unsupported JSON Schema fields |
| ID assignment | Assign IDs to tool calls (FIFO matching) |
| Wrap request | `{ project, model, request: {...} }` |

### Stage 3: Response transformation (`request.ts`)

| Step | What Happens |
|------|--------------|
| SSE streaming | Real-time line-by-line `TransformStream` |
| Signature caching | Cache `thoughtSignature` for display |
| Format transform | `thought: true` → `type: "reasoning"` |
| Envelope unwrap | Extract inner `response` object |

**Corpus observation:** The 7-step request transformation + 4-step response transformation = 11 explicit transformation stages between Opencode's outgoing fetch and Antigravity's expected wire format. This is **format-mismatch translation as the core engineering cost**. The plugin is approximately 50% format-translation code (compared to 10-20% in simpler bridge plugins).

---

## 8. Claude-specific handling (ARCHITECTURE.md §"Claude-Specific Handling")

The doc explicitly enumerates why Claude through Antigravity needs special handling:

1. **Gemini format** — `contents[].parts[]` not `messages[].content[]`
2. **Thinking signatures** — Multi-turn needs signed blocks or errors
3. **Schema restrictions** — Rejects `const`, `$ref`, `$defs`, etc.
4. **Tool validation** — `VALIDATED` mode requires proper schemas

### Thinking block strategy (v2.0 — formalized version)

**Problem statement (verbatim):** *"OpenCode stores thinking blocks, but may corrupt signatures."*

**Solution:** Strip ALL thinking blocks from outgoing requests.

```
Turn 1 Response: { thought: true, text: "...", thoughtSignature: "abc" }
                 ↓ (stored by OpenCode, possibly corrupted)
Turn 2 Request:  Plugin STRIPS all thinking blocks
                 ↓
Claude API:      Generates fresh thinking
```

**Tradeoffs (verbatim from doc):**
- Zero signature errors (impossible to have invalid signatures)
- Same quality (Claude sees full conversation, re-thinks fresh)
- Simpler code (no complex validation/restoration)

### Thinking injection for tool use

Claude API requires thinking before `tool_use` blocks. The plugin:

1. Caches signed thinking from responses (`lastSignedThinkingBySessionKey`)
2. On subsequent requests, injects cached thinking before `tool_use`
3. Only injects for the **first** assistant message of a turn (not every message)

Turn-boundary detection in `thinking-recovery.ts`:
```typescript
// A "turn" starts after a real user message (not tool_result)
// Only inject thinking into first assistant message after that
```

**Corpus observation:** The dual strategy (strip-all + inject-cached-for-tool-use) is a sophisticated workaround for an inherent tension between Anthropic's API requirements (thinking-before-tool-use) and Antigravity's transport (which may corrupt signatures). The plugin is doing **format normalization across asymmetric API contracts**.

---

## 9. Session recovery (ARCHITECTURE.md §"Session Recovery")

### Tool result missing error

When a tool execution is interrupted (ESC, timeout, crash), Anthropic API returns:
```
Error: tool_use ids were found without tool_result blocks immediately after
```

**Recovery flow** (`recovery.ts`):
1. Detect error via `session.error` event
2. Fetch session messages via `client.session.messages()`
3. Extract `tool_use` IDs from failed message
4. Inject synthetic `tool_result` blocks:
   ```typescript
   { type: "tool_result", tool_use_id: id, content: "Operation cancelled" }
   ```
5. Send via `client.session.prompt()`
6. Optionally auto-resume with `"continue"`

### Thinking block order error

```
Error: Expected thinking but found text
```

**Recovery** (`thinking-recovery.ts`):
1. Detect conversation is in tool loop without thinking at turn start
2. Close the corrupted turn with synthetic messages
3. Start fresh turn where Claude can generate new thinking

**Corpus observation:** Both recovery mechanisms work by **injecting synthetic messages to satisfy the API's protocol invariants**. The plugin is doing protocol-repair at the transport layer rather than surfacing errors to the user. This is **transparent-protocol-repair-as-UX-discipline** — a corpus-first observation for plugin-tier subjects.

---

## 10. Schema cleaning (ARCHITECTURE.md §"Schema Cleaning")

The plugin uses an **allowlist approach** for JSON Schema sanitization:

**Kept:** `type`, `properties`, `required`, `description`, `enum`, `items`

**Removed:** `const`, `$ref`, `$defs`, `default`, `examples`, `additionalProperties`, `$schema`, `title`

**Transformations:**
- `const: "value"` → `enum: ["value"]`
- Empty object schema → Add placeholder `reason` property

**Corpus observation:** The allowlist approach (vs. denylist) is **defensive sanitization-as-default-deny** — anything not explicitly permitted is removed. This means new JSON Schema features added by upstream tools won't accidentally leak through to Antigravity's strict validator. v66 agentmemory had no schema-sanitization layer (iii-engine handles directly). v62 codex-plugin-cc had no schema concerns. opencode-antigravity-auth's schema discipline is **bridge-correctness-as-explicit-allowlist**.

---

## 11. Dependencies (package.json)

**Runtime dependencies:**
```json
{
  "@opencode-ai/plugin": "^0.15.30",
  "@openauthjs/openauth": "^0.4.3",
  "proper-lockfile": "^4.1.2",
  "xdg-basedir": "^5.1.0",
  "zod": "^4.0.0"
}
```

5 runtime dependencies. **`zod ^4`** is explicitly emphasized in AGENTS.MD as *"NOT zod v3"* — schema validation discipline.

`proper-lockfile` + `xdg-basedir` indicate concern for:
- Concurrent access (file locking for `antigravity-accounts.json`)
- Cross-platform config-path resolution

**Engines:** `"node": ">=20.0.0"` — Node 20+ baseline.

**Dev dependencies:** Vitest 3 + coverage + UI + zod-to-json-schema. **No linter, no formatter** (AGENTS.MD: *"No linter or formatter is configured. Style is enforced by convention"*).

**Corpus observation:** 5 runtime deps is **minimum-viable** for a multi-account OAuth bridge. v66 agentmemory had 6 runtime deps with iii-sdk dominating (~98% surface). opencode-antigravity-auth's 5 deps are evenly distributed (none dominates >40% of functionality). The `zod ^4` major-version pin + Node 20+ floor signal **disciplined dependency hygiene** in a young project.

---

## 12. Testing discipline (AGENTS.MD §"Testing")

- Framework: **Vitest 3** with native ESM
- Tests colocated: `src/plugin/foo.test.ts` next to `src/plugin/foo.ts`
- Standard Vitest API: `describe`/`it`/`expect`, `vi.fn()`/`vi.spyOn()`/`vi.mock()`

Build/test scripts (from `package.json`):
```bash
npm run build              # tsc -p tsconfig.build.json
npm run typecheck          # tsc --noEmit
npm test                   # vitest run
npm run test:coverage      # coverage report
npm run test:e2e:models    # E2E: model availability check
npm run test:e2e:regression # E2E: regression suite
```

**Corpus observation:** E2E regression + E2E model-availability scripts indicate the plugin is **operationally verified against live Antigravity endpoints**, not just unit-tested. This is the FIRST corpus subject (in T4 Bridge archetype) with explicit live-endpoint E2E discipline. The cost of false-positive PR merges (vendor enforcement against accounts) makes regression testing operationally critical for this subject in a way most plugins don't experience.

---

## 13. Debugging surface (ARCHITECTURE.md §"Debugging")

Two independent debug sinks (split in v1.6.0 per CHANGELOG):
- `OPENCODE_ANTIGRAVITY_DEBUG=1` or `2` — file debug logging at `~/.config/opencode/antigravity-logs/`
- `OPENCODE_ANTIGRAVITY_DEBUG_TUI=1` — TUI panel debug output

Diagnostic questions surfaced in doc:
1. Is `isClaudeModel` true for Claude models?
2. Are thinking blocks being stripped?
3. Are tool schemas being cleaned?
4. Is session recovery triggering?

**Corpus observation:** The 4-question diagnostic is targeted at the 4 architectural transformations a maintainer would want to verify. v66 agentmemory had no comparable debug-as-architecture-instrumentation. v62 codex-plugin-cc had minimal debug surface. opencode-antigravity-auth's debug-as-architecture-instrumentation is a corpus-distinctive UX pattern for solo-utility plugins.

---

## 14. Cluster summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | Strictness-as-correctness-pre-condition (no `any` / `ts-ignore` / `ts-expect-error` discipline in TypeScript) | corpus-high for solo-utility |
| 2 | Graceful-degradation-by-design at the auth layer ("Rate limit / quota errors trigger account rotation, not failure") | corpus-first |
| 3 | Deliberate anti-detection architecture (request interception + fingerprinting + multi-account rotation as integrated mimicry) | corpus-first |
| 4 | Principled-information-discard for simpler-correctness (strip ALL Claude thinking blocks for transport reliability) | corpus-first |
| 5 | Format-translation as ~50% of plugin code (7-step request + 4-step response transformation) | corpus-first |
| 6 | Transparent-protocol-repair-as-UX-discipline (synthetic message injection to satisfy API invariants) | corpus-first |
| 7 | Bridge-correctness-as-explicit-allowlist (allowlist > denylist for schema sanitization) | corpus-distinctive |
| 8 | Live-endpoint E2E regression discipline (`test:e2e:models` + `test:e2e:regression` scripts) | corpus-first for T4 Bridge solo-utility |
| 9 | Debug-as-architecture-instrumentation (4-question diagnostic targets 4 architectural transformations) | corpus-distinctive |
| 10 | Documentation-architecture freshness (`Last Updated: April 2026` while CHANGELOG latest is 2026-02-20 = 2-month lag, tight for solo project) | corpus-distinctive |

---

## 15. Pattern Library implications from Cluster 2

- **Strengthens Pattern #66 meta-supply-chain-awareness:** the fingerprint system explicitly engineers around adversarial vendor behavior; the 90% soft quota threshold (Cluster 1 observation) is operationally aligned. This subject is meta-aware of its own supply-chain dependency on Google's tolerance and engineers operational defenses.
- **NEW observational candidate — Adversarial-Detection-Tolerant-Architecture:** When a bridge plugin's correctness depends on evading vendor anomaly detection, architectural decisions (fingerprinting, header mimicry, quota threshold defenses, fingerprint history rotation) accumulate as integrated defensive surface. v62 codex-plugin-cc had no comparable layer (OpenAI authored the bridge for its own product). v65 claude-code-system-prompts is reverse-engineering but doesn't ACT against the API — only reads. opencode-antigravity-auth's adversarial-tolerance is uniquely engineered.
- **Pattern #76 Adversarial Subagent Review Architecture (CANDIDATE N=1):** No N+1 evidence — opencode-antigravity-auth has no review-as-architecture concept. Architecturally orthogonal.
- **Pattern #18 Agent Runtime Standardization sub-archetype (v66 NEW):** The plugin's plugin-array-ordering correctness concern (Cluster 1 observation #5) is **plugin-coexistence-protocol observation** — different from Pattern #18's runtime-multiplexing-vs-translation axis. Sister observation, not direct N+1.

---

## 16. References

- AGENTS.MD (144 lines)
- docs/ARCHITECTURE.md (302 lines)
- package.json (66 lines)
- Cross-ref: cluster-1-readme-and-tos-framing.md (TOS framing)

## 17. Next cluster

Cluster 3: Multi-account quota architecture + API spec + CHANGELOG — `docs/MULTI-ACCOUNT.md` + `docs/ANTIGRAVITY_API_SPEC.md` + `docs/MODEL-VARIANTS.md` + `CHANGELOG.md`.
