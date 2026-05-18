# (C) Cluster 3: Quota architecture + Antigravity API + CHANGELOG history

**Sources:**
- [docs/MULTI-ACCOUNT.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/MULTI-ACCOUNT.md) (199 lines)
- [docs/ANTIGRAVITY_API_SPEC.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/ANTIGRAVITY_API_SPEC.md) (634 lines, *"Verified by Direct API Testing"*, *"Last Updated: December 13, 2025"*)
- [docs/MODEL-VARIANTS.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/docs/MODEL-VARIANTS.md) (182 lines)
- [CHANGELOG.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/CHANGELOG.md) (267 lines, v1.0.0–v1.6.0 = 91 releases in 5 months)

**Cluster focus:** Dual quota pools, account selection strategies, scheduling modes, variant system, Antigravity API surface, CHANGELOG evolution as evidence of vendor-enforcement learning.

---

## 1. Antigravity API self-description (verbatim)

From `ANTIGRAVITY_API_SPEC.md` opening:

> *"Antigravity is Google's **Unified Gateway API** for accessing multiple AI models (Claude, Gemini, GPT-OSS) through a single, consistent Gemini-style interface. It is NOT the same as Vertex AI's direct model APIs."*

**Key characteristics (verbatim):**
- Single API format for all models (Gemini-style)
- Project-based access via Google Cloud authentication
- Internal routing to model backends (Vertex AI for Claude, Gemini API for Gemini)
- Unified response format (`candidates[]` structure for all models)

**Endpoints (3 environments):**

| Environment | URL | Status |
|-------------|-----|--------|
| Daily (Sandbox) | `daily-cloudcode-pa.sandbox.googleapis.com` | ✅ Active |
| Production | `cloudcode-pa.googleapis.com` | ✅ Active |
| Autopush (Sandbox) | `autopush-cloudcode-pa.sandbox.googleapis.com` | ❌ Unavailable |

**API actions:**
- `/v1internal:generateContent` — non-streaming
- `/v1internal:streamGenerateContent?alt=sse` — streaming (SSE)
- `/v1internal:loadCodeAssist` — project discovery
- `/v1internal:onboardUser` — user onboarding

**Corpus observation:** Antigravity is **closed-vendor's-internal-gateway-discovered-as-surface**. The `/v1internal:*` path prefix is Google's internal indication; this is NOT a public API. The plugin's existence depends on continued endpoint stability without contract guarantees. The doc's *"Verified by Direct API Testing"* assertion is the plugin's strongest validity claim — it's an empirical discovery, not a vendor contract.

**Required OAuth scopes (5):**
```
https://www.googleapis.com/auth/cloud-platform
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/cclog
https://www.googleapis.com/auth/experimentsandconfigs
```

The `cclog` and `experimentsandconfigs` scopes are non-standard / internal-Google — a signal that the plugin is impersonating Antigravity Manager's exact OAuth scope set.

---

## 2. Available models on Antigravity (verbatim from API spec)

| Model name | Model ID | Type | Status |
|------------|----------|------|--------|
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Anthropic | ✅ Verified |
| Claude Opus 4.6 Thinking | `claude-opus-4-6-thinking` | Anthropic | ✅ Verified |
| Gemini 3 Pro High | `gemini-3-pro-high` | Google | ✅ Verified |
| Gemini 3 Pro Low | `gemini-3-pro-low` | Google | ✅ Verified |
| GPT-OSS 120B Medium | `gpt-oss-120b-medium` | Other | ✅ Verified |

**Corpus observation:** Antigravity hosts a multi-vendor model gateway including OpenAI's GPT-OSS. This is **third-vendor inclusion** — Google's IDE is brokering OpenAI models alongside Anthropic Claude and its own Gemini. Strengthens Pattern #84 cross-vendor-ecosystem-tolerance evidence at the closed-vendor level (Google brokering competitor models inside its own IDE).

---

## 3. Wire format requirements (verbatim from API spec)

**Critical incompatibilities** (would cause 400 errors):
- Must use Gemini-style `contents[].parts[]` format — NOT Anthropic-style `messages[].content[]`
- `systemInstruction` must be object with `parts`, NOT plain string
- `role: "model"` for assistant messages — NOT `role: "assistant"`

**JSON Schema support matrix:**

| Feature | Status |
|---------|--------|
| `type`, `properties`, `required`, `description`, `enum`, `items` | ✅ Supported |
| `anyOf`, `allOf`, `oneOf` | ✅ Supported (converted to `any_of`/`all_of`/`one_of` internally) |
| `additionalProperties` | ✅ Supported |
| `const`, `$ref`, `$defs`, `$schema`, `$id`, `default`, `examples` | ❌ NOT supported — strip or transform |
| `title` (nested) | ⚠️ Caution |

**Function name rules:**
- First char: letter `a-z A-Z` or underscore `_`
- Allowed: `a-zA-Z0-9` + `_` `.` `:` `-`
- Max 64 chars
- NOT allowed: `/`, spaces, other special chars

---

## 4. Multi-account architecture (docs/MULTI-ACCOUNT.md)

**Load balancing (4 explicit behaviors):**
1. **Sticky account selection** — Sticks to same account until rate-limited (preserves Anthropic's prompt cache)
2. **Per-model-family limits** — Rate limits tracked separately for Claude and Gemini
3. **Antigravity-first for Gemini** — All Gemini requests use Antigravity quota first, then fall back to Gemini CLI when exhausted across all accounts
4. **Smart retry threshold** — Short rate limits (≤5s) retried on same account
5. **Exponential backoff** — Increasing delays for consecutive rate limits

### Dual quota pools — verbatim claim

> *"This effectively **doubles your Gemini quota** through automatic fallback between Antigravity and Gemini CLI pools."*

**Fallback mechanism (verbatim):**
1. Request uses Antigravity quota on current account
2. If rate-limited, plugin checks if ANY other account has Antigravity available
3. If yes → switch to that account (stay on Antigravity)
4. If no (all accounts exhausted) → fall back to Gemini CLI quota on current account
5. Model names auto-transformed (`gemini-3-flash` → `gemini-3-flash-preview`)

**Corpus observation:** The "doubles your Gemini quota" claim is operationally precise: one Google account = two independent API quota pools because Antigravity and Gemini CLI are separate Google services with separate quotas (despite hitting the same underlying Gemini model). This is **quota-arbitrage as architectural primitive**.

### Account selection strategies (3 explicit)

| Strategy | Behavior | Best for |
|----------|----------|----------|
| `sticky` | Same account until rate-limited | Prompt cache preservation |
| `round-robin` | Rotate to next account on every request | Maximum throughput |
| `hybrid` | Deterministic selection based on health score + token bucket + LRU | Best overall distribution |

### Account storage schema (v3 → v4 migration in CHANGELOG)

`~/.config/opencode/antigravity-accounts.json` structure (current v4 — file mode `0600` per v1.5.0):

```json
{
  "version": 3,
  "accounts": [
    {
      "email": "user1@gmail.com",
      "refreshToken": "1//0abc...",
      "projectId": "my-gcp-project",
      "enabled": true
    },
    {
      "email": "user2@gmail.com",
      "refreshToken": "1//0xyz...",
      "enabled": false
    }
  ],
  "activeIndex": 0,
  "activeIndexByFamily": {
    "claude": 0,
    "gemini": 0
  }
}
```

**Per-model-family active-index tracking** is corpus-distinctive — the plugin tracks which account is currently active SEPARATELY for Claude vs Gemini, because each model family has different rate-limit characteristics on Antigravity.

---

## 5. Variant system (docs/MODEL-VARIANTS.md)

The plugin exposes Opencode's `variant` mechanism for thinking-budget configuration:

```bash
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
```

**Variant formats per model family:**

| Family | Format | Example |
|--------|--------|---------|
| Claude | `thinkingConfig.thinkingBudget` (tokens) | `{ "thinkingConfig": { "thinkingBudget": 8192 } }` |
| Gemini 3 | `thinkingLevel` (string) | `{ "thinkingLevel": "high" }` |
| Gemini 2.5 | `thinkingConfig.thinkingBudget` (tokens) | `{ "thinkingConfig": { "thinkingBudget": 8192 } }` |

**Gemini 3 thinking levels:**

| Level | Flash | Pro | Description |
|-------|-------|-----|-------------|
| `minimal` | ✅ | ❌ | Minimal thinking, lowest latency |
| `low` | ✅ | ✅ | Light thinking |
| `medium` | ✅ | ❌ | Balanced thinking |
| `high` | ✅ | ✅ | Maximum thinking (default) |

> *"The API rejects invalid levels (e.g., `"minimal"` on Pro). Configure variants accordingly."*

**Tier-suffixed legacy names** (`antigravity-claude-opus-4-6-thinking-low`, `antigravity-gemini-3-pro-high`, etc.) are still accepted but **variants are recommended for cleaner UX**: *"Cleaner model picker — 7 models instead of 12+ / Simpler config / Automatic quota routing / Flexible budgets / Future-proof"*.

**Corpus observation:** Variant system is a UX delegation — the plugin maps Opencode's generic variant slot to model-family-specific thinking formats. This is **format-abstraction-as-end-user-affordance** — hiding format asymmetry behind a consistent invocation syntax.

---

## 6. CHANGELOG evolution as evidence of vendor-enforcement learning

The 267-line CHANGELOG covers v1.0.0 (2025-12-10) → v1.6.0 (2026-02-20) = 91 releases in 159 days = ~1 release every 1.75 days. Selected entries reveal **the plugin learning to dodge vendor enforcement**:

### v1.3.1 (2026-01-21) — Anti-detection auth-header alignment

> *"**Auth headers aligned with official Gemini CLI** — Updated authentication headers to match the official Antigravity/Gemini CLI behavior, reducing 'account ineligible' errors and potential bans (#178)"*

Specific header updates (verbatim CHANGELOG):
- `GEMINI_CLI_HEADERS["User-Agent"]`: `9.15.1` → `10.3.0`
- `GEMINI_CLI_HEADERS["X-Goog-Api-Client"]`: `gl-node/22.17.0` → `gl-node/22.18.0`
- `ANTIGRAVITY_HEADERS["User-Agent"]`: Updated to full Chrome/Electron user agent string
- Token exchange + userinfo fetch now include `Accept`, `Accept-Encoding`, `User-Agent`, `X-Goog-Api-Client` headers

**Significance:** Issue #178 was the user-facing signal of an enforcement pattern. The plugin's response = mimic Google's official client more precisely.

### v1.3.2 (2026-01-27) — Detection-pattern defenses

3 features in one release explicitly framed as detection-evasion:

1. **Request timing jitter** — *"configurable random delay to requests to reduce detection patterns and improve rate limit resilience"*
2. **Header randomization for fingerprint diversity** — *"Headers are now randomized to create more diverse fingerprints, reducing the likelihood of requests being grouped and rate-limited together"*
3. **Per-account fingerprint persistence** — *"Fingerprints are now persisted per-account in storage, allowing consistent identity across sessions and enabling fingerprint history tracking"*

Plus: **Regenerate fingerprint after capacity retry exhaustion** — *"to potentially get assigned to a different backend partition"*.

### v1.4.5 (2026-02-05) — Soft quota threshold

> *"**Soft Quota Protection** — Skip accounts over 90% usage threshold to prevent Google penalties, with configurable `soft_quota_threshold_percent` and wait/retry behavior"*

The 90% threshold is **direct operational defense against quota-exhaustion-as-vendor-penalty-trigger**.

### v1.5.0 (2026-02-11) — Account verification flow + secure permissions

> *"**Account Verification Flow** — Auth login menu now supports `verify` and `verify-all` actions. When Antigravity returns a 403 with `validation_required`, the account is automatically disabled, marked with a verification URL, and cooled down."*

> *"**Dynamic Antigravity Version** — Plugin version is now fetched at startup from the Antigravity updater API, with a changelog-scrape fallback and a hardcoded last-resort. Eliminates stale 'version no longer supported' errors after Antigravity updates"*

> *"**Storage V4 Schema** — New storage version adds `verificationRequired`, `verificationRequiredAt`, `verificationRequiredReason`, `verificationUrl`, and `fingerprintHistory` fields per account."*

> *"**Secure File Permissions** — Credential storage files are now created with mode `0600` (owner read/write only). Existing files with overly permissive modes are tightened on load"*

### v1.5.1 (2026-02-11, same day) — Header identity alignment + Linux removal

> *"**Header Identity Alignment** — `ideType` changed from `IDE_UNSPECIFIED` to `ANTIGRAVITY` and `platform` from `PLATFORM_UNSPECIFIED` to dynamic `WINDOWS`/`MACOS` (based on `process.platform`). Now matches Antigravity Manager behavior"*

> *"**Linux Fingerprints — Removed** `linux/amd64` and `linux/arm64` from `ANTIGRAVITY_PLATFORMS` and fingerprint generation. Linux users now masquerade as macOS (Antigravity does not support Linux as a native platform)"*

**Significance:** Linux users get an explicitly fabricated macOS fingerprint because real Linux fingerprints flagged accounts. This is **adversarial-detection-tolerance: forced platform-misrepresentation as defensive correctness**.

### v1.6.0 (2026-02-20) — Debug sink split + header strip

> *"**Header Normalization** — `x-goog-user-project` is now stripped across Antigravity and Gemini CLI request styles."*

Header strip rationale (from v1.5.0 Fixed): *"#410: Strip x-goog-user-project header for ALL header styles, not just Antigravity. This header caused 403 errors on Daily/Prod endpoints when the user's GCP project lacked Cloud Code API"*.

---

## 7. CHANGELOG-derived corpus observations

| # | Observation | Status |
|---|-------------|--------|
| 1 | The plugin's evolution is dominated by anti-detection adaptations: timing jitter, header randomization, fingerprint diversity, platform masquerading | corpus-first explicit evolution-as-anti-detection-learning |
| 2 | Each detection-pattern is observed in production (issues #178, #410, etc.) then patched — i.e., the user community is the sensor network for vendor enforcement | corpus-first |
| 3 | "Plugin version is now fetched at startup from the Antigravity updater API" — the plugin reads Google's OWN version-check endpoint to stay current with what Antigravity expects | corpus-first vendor-impersonation as continuous-self-maintenance |
| 4 | Storage V4 schema adds `verificationRequired` / `verificationUrl` per-account fields = state machine for vendor-imposed verification challenges | corpus-first |
| 5 | "Linux users now masquerade as macOS" — explicit platform-misrepresentation as defensive correctness | corpus-first |
| 6 | Issue references (#178, #207, #233, #263, #286, #337, #368, #370, #377, #381, #384, #410, #444, #454, #397) — issue-driven defensive engineering pattern | corpus-first explicit issue-as-enforcement-signal pipeline |
| 7 | 91 releases in 5 months at average 1.75-day cadence = corpus-high author-velocity for a non-corporate solo subject | corpus-record for solo-utility plugin |
| 8 | Three independent endpoint environments (Daily / Production / Autopush sandbox) with explicit endpoint fallback chain in code | corpus-first |

---

## 8. Pattern Library implications from Cluster 3

- **Pattern #83 Honest-Deficiency-Disclosure N=3 evidence consolidated:** The CHANGELOG itself is a deficiency-disclosure surface — each "Fixed #N" entry candidly names the detection-pattern or vendor-imposed failure. The "Linux users now masquerade as macOS" disclosure is brutally honest. CHANGELOG also openly discloses bypass mechanisms.
- **Pattern #84 Cross-Vendor Ecosystem-Tolerance — NUANCED EVIDENCE:**
  - **PRO #84:** Antigravity hosts Claude + Gemini + GPT-OSS via one gateway — Google is brokering Anthropic + OpenAI models inside its IDE. Substantial cross-vendor cooperation at vendor level.
  - **CONTRA #84:** Google ACTIVELY enforces against unauthorized use of Antigravity (account bans, shadow-bans, 403 `validation_required`) — vendor tolerance has hard limits.
  - **Reconciliation:** The repo itself is tolerated (sub-DMCA); individual unauthorized usage is enforced. Refines #84 to clarify tolerance-mechanism scope: **enforcement-at-the-use-not-the-tool** is the distinguishing mechanism.
- **NEW observational candidate — Adversarial-Detection-Tolerant Architecture (cross-cluster):** Multiple sub-mechanisms accumulating across the plugin's evolution: (1) header mimicry, (2) timing jitter, (3) header randomization, (4) per-account fingerprint diversity, (5) fingerprint history rotation, (6) backend-partition reassignment via fingerprint regeneration, (7) soft quota thresholds, (8) platform masquerading. Architecturally distinct from "fault-tolerant" (= survives random errors); this is "enforcement-tolerant" (= survives adversarial vendor responses).
- **NEW observational candidate — Issue-As-Enforcement-Signal Pipeline:** User-reported issues function as the sensor network for vendor enforcement patterns; each pattern triggers a defensive engineering response in the next minor release. Distinct from ordinary bug-fix pipelines because the issue is NOT a code defect — it's a vendor response.
- **Pattern #18 Agent Runtime Standardization sub-archetype evidence (v66 NEW):** STRONG N=2 evidence for the **shared-backend-service sub-archetype** but the mechanism is the inverse of agentmemory:
  - agentmemory v66: many-platforms (15+ host platforms) → one-server (single agentmemory deployment)
  - opencode-antigravity-auth v67: many-accounts (Google OAuth accounts) → one-backend (Antigravity Unified Gateway)
  - Both share the "one-server-many-clients" structural property but with different client semantics. Flag for v68 stale-check as sub-archetype validation.

---

## 9. Cluster 3 summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | Closed-vendor's-internal-gateway-discovered-as-surface (Antigravity is Google's `/v1internal:*` not public API) | corpus-first |
| 2 | Quota-arbitrage as architectural primitive (single account → 2× quota via dual pools) | corpus-first |
| 3 | Per-model-family active-index tracking (different active account for Claude vs. Gemini) | corpus-first |
| 4 | Format-abstraction-as-end-user-affordance (variant slot maps to family-specific thinking format) | corpus-distinctive |
| 5 | Vendor-impersonation as continuous-self-maintenance (plugin reads Google's version-check endpoint to stay current) | corpus-first |
| 6 | Issue-as-enforcement-signal pipeline (defensive engineering driven by user-reported enforcement patterns) | corpus-first |
| 7 | Adversarial-detection-tolerant architecture accumulating across 8 sub-mechanisms | corpus-first |
| 8 | 91 releases / 5 months / 1.75-day cadence at solo-utility scale | corpus-record |
| 9 | Multi-vendor model brokerage by closed vendor (Google hosting Claude + Gemini + GPT-OSS inside Antigravity) | corpus-first |

---

## 10. References

- docs/MULTI-ACCOUNT.md (199 lines)
- docs/ANTIGRAVITY_API_SPEC.md (634 lines)
- docs/MODEL-VARIANTS.md (182 lines)
- CHANGELOG.md (267 lines)
- Cross-ref: cluster-1 (ToS framing) + cluster-2 (architecture + fingerprint system)

## 11. Next phase

Phase 3 — 4 entity pages: (1) OAuth bridge core, (2) Multi-account quota-multiplexing architecture, (3) Antigravity Unified Gateway API as Phase 4b PRIMARY-aligned deliverable, (4) Storm Bear meta-entity (MODERATE INCLUDE per Phase 0.9 STRICT 2/4 PASS).
