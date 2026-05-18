# (C) Entity 2: Multi-account quota-multiplexing architecture

**Type:** Distribution/ecosystem entity
**Slot:** Entity 2 of 4
**Sibling entities:** [Entity 1 — OAuth bridge core](entity-1-oauth-bridge-core.md) / [Entity 3 — Antigravity Unified Gateway](entity-3-antigravity-unified-gateway.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. Architectural premise

The plugin's multi-account architecture exists to solve a single business-level problem: **a single Google account's Antigravity quota is insufficient for sustained AI coding workflows**, AND **Google enforces against accounts that fully exhaust quota**. The plugin's response is a layered defense:

1. **Add more accounts** — n accounts = n× combined quota (when not coordinated by Google)
2. **Rotate among accounts** — distribute load to avoid any single account hitting enforcement
3. **Run multiple selection strategies** — different rotation algorithms for different operational patterns
4. **Run multiple scheduling modes** — different rate-limit-response policies
5. **Add per-account fingerprints** — make accounts look distinct to backend partitioning
6. **Apply soft quota threshold** — stop using an account before it hits 100% to avoid enforcement

This is not a "load balancer for high-throughput requests." It is **enforcement-tolerant quota-multiplexing**.

---

## 2. Dual quota pools per account (the central insight)

A single Google account gets TWO independent API quotas relevant to this plugin:

| Quota pool | Endpoint | Plugin's default routing |
|------------|----------|--------------------------|
| Antigravity | `cloudcode-pa.googleapis.com` `/v1internal:*` | Default for all requests |
| Gemini CLI | `generativelanguage.googleapis.com` (standard public API) | Fallback when Antigravity exhausted, OR primary when `cli_first: true` |

**The doc's central claim (verbatim from `docs/MULTI-ACCOUNT.md`):**

> *"This effectively **doubles your Gemini quota** through automatic fallback between Antigravity and Gemini CLI pools."*

The plugin's fallback algorithm (verbatim):
1. Request uses Antigravity quota on current account
2. If rate-limited, check if ANY other account has Antigravity available
3. If yes → switch to that account (stay on Antigravity)
4. If no (all accounts exhausted) → fall back to Gemini CLI quota on current account
5. Model names auto-transformed (`gemini-3-flash` → `gemini-3-flash-preview`)

**Step 4 is the architectural key.** When an account is rate-limited on Antigravity, the plugin doesn't just give up — it switches the same account to a SEPARATE quota pool that Google bills under a different service envelope. This is **quota-arbitrage across vendor-internal API surfaces**.

(Claude and image models always stay on Antigravity — they aren't available via the Gemini CLI surface.)

---

## 3. Three account-selection strategies

Configured in `~/.config/opencode/antigravity.json`:

| Strategy | Behavior | Best for |
|----------|----------|----------|
| `sticky` | Same account until rate-limited (preserves Anthropic prompt cache) | 1 account / long conversations / prompt-cache savings |
| `round-robin` | Rotate to next account on every request | 5+ accounts / max throughput |
| `hybrid` (default) | Deterministic selection based on **health score + token bucket + LRU** | 2-5 accounts / best overall distribution |

The `hybrid` strategy is the plugin's default for the 2-5-account case. The specific algorithm computes:
- **Health score** — how recently has this account succeeded?
- **Token bucket** — does the account have request capacity available?
- **LRU** — was this account recently used? (avoid hammering one)

---

## 4. Three rate-limit scheduling modes

| Mode | Behavior | When to use |
|------|----------|-------------|
| `cache_first` (default) | Wait for same account (preserves Anthropic prompt cache) | Long conversations |
| `balance` | Switch accounts immediately on rate-limit | Quick tasks / max availability |
| `performance_first` | Round-robin distribution | Many short requests |

The `cache_first` default exists because Anthropic's prompt-cache feature is per-account and tied to specific conversation context — switching accounts mid-conversation invalidates the cache (and re-bills the prefix). Waiting (up to `max_cache_first_wait_seconds`, default 60s) for the same account preserves cache savings.

---

## 5. Quota protection: the soft threshold

`soft_quota_threshold_percent` (default `90`) is operationally significant:

> *"Skip account when quota usage exceeds this percentage. Prevents Google from penalizing accounts that fully exhaust quota."*

The plugin's stated belief is that Google adversarially penalizes accounts that hit 100% — possibly via increased rate-limiting future requests, account flagging, or 403 `validation_required` responses. The 90% threshold is a deliberate operational defense.

When ALL accounts exceed the threshold, the plugin waits for the earliest quota reset (per-model-family) rather than continuing to use a near-exhausted account. If the wait exceeds `max_rate_limit_wait_seconds`, it errors.

`quota_refresh_interval_minutes` (default 15) controls how often the plugin refreshes its quota cache via background API calls. `soft_quota_cache_ttl_minutes` (default `"auto"` = `max(2 × refresh interval, 10 minutes)`) controls cache freshness.

---

## 6. Per-account fingerprint storage

Each account in `~/.config/opencode/antigravity-accounts.json` has a per-account fingerprint:

```json
{
  "email": "user@gmail.com",
  "refreshToken": "1//0...",
  "fingerprint": {
    "deviceId": "...",
    "sessionToken": "...",
    "userAgent": "...",
    "clientMetadata": {
      "ideType": "ANTIGRAVITY",
      "platform": "MACOS" | "WINDOWS",
      "pluginType": "GEMINI"
    }
  },
  "fingerprintHistory": [/* max 5 prior fingerprints, restorable */]
}
```

Per `docs/ARCHITECTURE.md`: each fingerprint includes `deviceId`, `sessionToken`, `userAgent`, and reduced `clientMetadata` (only `ideType`, `platform`, `pluginType` — explicitly NOT `osVersion`, `arch`, or `sqmId`). The reduction in v1.5.0 was specifically aligned with Antigravity Manager's actual outgoing-header behavior.

**Storage discipline:**
- File mode `0600` (owner-read-write only) — enforced on create + tightened on load for existing files
- Concurrent-access locking via `proper-lockfile`
- `saveAccountsReplace` (destructive write) prevents deleted-account resurrection from concurrent reads

The fingerprint is regenerated on capacity-retry exhaustion *"to potentially get assigned to a different backend partition"* (per v1.3.2 CHANGELOG). Fingerprint history (max 5) is preserved per-account and restorable — implying the plugin has a deliberate state machine for fingerprint trial-and-restoration.

---

## 7. Account state machine (v4 storage schema, post-v1.5.0)

Per account:
- `enabled` (bool) — exclude from rotation when `false`
- `verificationRequired` (bool) — set when Antigravity returns 403 `validation_required`
- `verificationRequiredAt` (timestamp)
- `verificationRequiredReason` (string)
- `verificationUrl` (string) — Google's verification flow URL for the user
- `fingerprintHistory[]` (max 5)

State transitions:
- New account → `enabled: true`
- Antigravity 403 `validation_required` → `enabled: false` + `verificationRequired: true` + cooldown
- User completes verification via menu's `verify` action → probe request → if successful, `enabled: true`
- User-initiated disable via `manage accounts` menu → `enabled: false` (deliberate)

The `verificationRequired` pathway is the plugin's response to **Google's account-verification challenge as an enforcement signal** — when Google flags an account, the plugin disables it gracefully rather than continuing to retry (which would compound the flag).

---

## 8. Concurrency story (parallel agents / `pid_offset_enabled`)

When using `oh-my-opencode` with parallel subagents, multiple processes may select the same account simultaneously, causing rate-limit collisions. The plugin's solution:

```json
{ "pid_offset_enabled": true }
```

This distributes sessions across accounts based on `process.pid` (likely `pid % account_count`), giving each process a deterministic-but-distinct starting account.

This is a **coordination-via-OS-primitive** pattern — using the OS-assigned PID as the entropy source for distribution, avoiding the need for inter-process coordination (lock files, shared state) for the common case.

---

## 9. Multi-account session UX (the `opencode auth login` menu)

The interactive `opencode auth login` menu surfaces 4 user-facing actions (post-v1.5.0):

1. **Add new account** — OAuth flow + token capture
2. **Configure models** — auto-write all plugin models to `opencode.json`
3. **Check quotas** — interactive quota report across all accounts, per-model-family
4. **Manage accounts** — enable/disable individual accounts; `verify`/`verify-all` for accounts in `validation_required` state
5. **Fresh start** (when existing accounts present) — explicit a/f prompt: `"(a)dd new account(s) or (f)resh start?"`

This is a corpus-distinctive UX surface: most CLI auth plugins offer "login" as a one-shot operation. opencode-antigravity-auth's `auth login` is a multi-purpose dashboard.

A standalone quota script (`scripts/check-quota.mjs`) also exists for non-Opencode quota checks (CI, debugging) — operates against the same accounts file.

---

## 10. Plugin-coexistence considerations

The plugin documents 2 explicit ordering / coexistence constraints:

**With `@tarquinen/opencode-dcp`:** Plugin ordering matters. opencode-antigravity-auth must be listed BEFORE dcp because DCP creates synthetic assistant messages lacking thinking blocks; opencode-antigravity-auth needs to intercept the request BEFORE dcp's synthesis happens. From the README:

```json
{
  "plugin": [
    "opencode-antigravity-auth@latest",
    "@tarquinen/opencode-dcp@latest"
  ]
}
```

**With `oh-my-opencode`:** Disable its built-in Google auth:

```json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" }
  }
}
```

**Plugins-you-don't-need:** *"gemini-auth plugins — Not needed. This plugin handles all Google OAuth."*

This is **plugin-ordering-as-correctness-concern** — the runtime's plugin array is order-sensitive for fetch-interception correctness. Corpus-first observation.

---

## 11. Quota arithmetic example

**1 Google account:**
- Antigravity Claude quota (whatever Google offers Antigravity beta users)
- Antigravity Gemini quota (whatever Google offers Antigravity beta users for Gemini)
- Gemini CLI quota (separate; available via fallback for Gemini-family models)

→ **2× effective Gemini quota** (Antigravity + Gemini CLI), 1× Claude quota

**5 Google accounts (default `hybrid` strategy):**
- 5× Antigravity Claude quota
- 5× Antigravity Gemini quota
- 5× Gemini CLI quota

→ **5× Claude + 10× effective Gemini quota** (per the dual-pool fallback)

(Modulo Google's rate-limit reset windows, soft-quota-90%-threshold backoff, and any coordination Google does at the per-IP / per-fingerprint / per-account-family level.)

---

## 12. Why this architecture is corpus-distinctive

The plugin's multi-account architecture is structurally distinct from:

- **Connection pooling** — connection pools share connections to the same upstream; this plugin uses distinct identities
- **CDN-style request distribution** — CDN distributes by client location/load; this plugin distributes by quota state
- **API key rotation** — typical key rotation is for security (expiry); this plugin rotates for capacity + enforcement-avoidance
- **Service mesh load balancing** — service meshes balance based on backend health; this plugin balances based on per-account quota+fingerprint state

The closest analog in the corpus is **Pattern #18 Agent Runtime Standardization sub-archetype shared-backend-service** (v66 NEW from agentmemory). agentmemory: many-platforms (15+) → one-server. opencode-antigravity-auth: many-accounts → one-backend-gateway. Both share the "one-server-many-clients" structural property with inverted client semantics:

- agentmemory: distinct host platforms with shared service (host-shaped diversity)
- opencode-antigravity-auth: distinct authenticated identities with shared upstream (identity-shaped diversity)

---

## 13. Pattern Library implications

- **Pattern #18 shared-backend-service sub-archetype:** Possible N=2 evidence (many-accounts-one-backend mechanism). Flag for v68 stale-check as sub-archetype validation (NOT direct N=2 claim because the mechanism direction differs from agentmemory v66 N=1 baseline).
- **NEW observational candidate: Quota-Arbitrage-Across-Vendor-Internal-Surfaces** — single account exposes 2 independent quota pools because Antigravity and Gemini CLI are separate Google services; plugin treats them as mergeable. Could observe at other closed-vendor + sister-internal-product pairings (e.g., Anthropic API + Workbench, OpenAI API + Codex CLI). Library-vocabulary candidate.
- **NEW observational candidate: Enforcement-Tolerant Multi-Identity Architecture** — multi-account rotation purpose is NOT primarily throughput but enforcement-avoidance. Sub-mechanisms: per-account fingerprint diversity + fingerprint history rotation + soft quota threshold + backend-partition reassignment via fingerprint regeneration + account verification state machine. Distinct from "fault-tolerant" — survives adversarial vendor responses, not random faults.

---

## 14. References

- docs/MULTI-ACCOUNT.md (199 lines, primary)
- docs/CONFIGURATION.md (245 lines, for option details)
- CHANGELOG.md (267 lines, for evolution of fingerprint/quota systems)
- README.md §"Multi-Account Setup" + §"Configuration"
- Cross-cluster: `cluster-3-quota-api-and-changelog.md`

## 15. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v66 agentmemory](../../agentmemory - Beginner Analysis/CLAUDE.md)** | Pattern #18 shared-backend-service sub-archetype — agentmemory is many-platforms-one-server; this entity is many-accounts-one-backend |
| **[v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md)** | T4 Bridge sibling but lacks multi-account architecture (single OpenAI-account assumption) |
| **[v65 claude-code-system-prompts](../../claude-code-system-prompts - Beginner Analysis/CLAUDE.md)** | Read-only reverse-engineering archive — neither has multi-account architecture; the architectural divergence is informative |
