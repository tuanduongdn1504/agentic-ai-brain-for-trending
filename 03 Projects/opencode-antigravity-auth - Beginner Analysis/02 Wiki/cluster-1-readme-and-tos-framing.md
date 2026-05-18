# (C) Cluster 1: README + Terms-of-Service framing

**Source:** [README.md](https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/main/README.md) (718 lines, ~24 KB)
**Cluster focus:** User-facing positioning / installation flows / models table / **Terms-of-Service warning block** / variant invocation / troubleshooting surface

---

## 1. Verbatim tagline + positioning

> *"Enable Opencode to authenticate against **Antigravity** (Google's IDE) via OAuth so you can use Antigravity rate limits and access models like `gemini-3.1-pro` and `claude-opus-4-6-thinking` with your Google credentials."*

Repository title: **"Antigravity + Gemini CLI OAuth Plugin for Opencode"**.

Twitter author handle: `@dopesalmon` (X badge prominent in README header).

NPM channels: `opencode-antigravity-auth@latest` (stable) + `@beta` (bleeding-edge features).

---

## 2. "What You Get" — 7 explicit features

1. **Claude Opus 4.6, Sonnet 4.6** and **Gemini 3.1 Pro/Flash** via Google OAuth
2. **Multi-account support** — add multiple Google accounts, auto-rotates when rate-limited
3. **Dual quota system** — access both Antigravity and Gemini CLI quotas from one plugin
4. **Thinking models** — extended thinking for Claude and Gemini 3 with configurable budgets
5. **Google Search grounding** — enable web search for Gemini models (auto or always-on)
6. **Auto-recovery** — handles session errors and tool failures automatically
7. **Plugin compatible** — works alongside other OpenCode plugins (oh-my-opencode, dcp, etc.)

---

## 3. Terms-of-Service warning block (verbatim)

The README's third major section (immediately after "What You Get") is a `<details open>` block — open-by-default, not collapsed — titled:

> **"⚠️ Terms of Service Warning — Read Before Installing"**

Containing this `[!CAUTION]` block verbatim:

> Using this plugin (and any proxy for Antigravity) violates Google's Terms of Service. A number of users have reported their Google accounts being **banned** or **shadow-banned** (restricted access without explicit notification).
>
> **By using this plugin, you acknowledge:**
> - This is an unofficial tool not endorsed by Google
> - Your account may be suspended or permanently banned
> - You assume all risks associated with using this plugin

And a closing `<details>` "Legal" block at the README footer reiterates:

> **Intended Use**
> - Personal / internal development only
> - Respect internal quotas and data handling policies
> - Not for production services or bypassing intended limits
>
> **Warning**
> By using this plugin, you acknowledge:
> - **Terms of Service risk** — This approach may violate ToS of AI model providers
> - **Account risk** — Providers may suspend or ban accounts
> - **No guarantees** — APIs may change without notice
> - **Assumption of risk** — You assume all legal, financial, and technical risks
>
> **Disclaimer**
> - Not affiliated with Google. This is an independent open-source project.
> - "Antigravity", "Gemini", "Google Cloud", and "Google" are trademarks of Google LLC.

**Corpus-first observation:** This is the most explicit ToS-violation disclosure in the 66-wiki corpus to date. v62 codex-plugin-cc had a "ChatGPT subscription required" gate (commercial vendor relationship); v65 claude-code-system-prompts had a "Maintained by Piebald AI, not Anthropic" disclaimer (third-party reverse-engineering archive). **Neither prior corpus subject foregrounds an explicit acknowledgment-of-account-suspension-risk before installation.**

---

## 4. Installation flows — 2 humans + 1 LLM-agent variant

**Option A (Human, lazy):** *Paste this into any LLM agent (Claude Code, OpenCode, Cursor, etc.)*:
```
Install the opencode-antigravity-auth plugin and add the Antigravity model definitions to ~/.config/opencode/opencode.json by following: https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md
```

**Option B (Human, manual):** 4-step process — edit `opencode.json` to add `"plugin": ["opencode-antigravity-auth@latest"]` → `opencode auth login` → choose "Configure models in opencode.json" → invoke `opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max`.

**For LLM Agents (collapsed `<details>` block):** Explicit step-by-step instructions including Windows tilde-resolution note (`~` resolves to user home on all platforms including Windows; do NOT use `%APPDATA%`).

**Corpus observation:** Dual installation surface — one optimized for humans-with-LLM-as-installer, another for direct-LLM-agent invocation. The "Option A" flow is **agentic-installation-as-first-class-UX** (cf. v64 claude-seo `make install` discipline, v66 agentmemory CLI-first extensibility). NoeFabris formalizes the assumption that users won't read docs but their LLM agent will.

---

## 5. Models table (verbatim from README)

**Antigravity quota** (default routing):

| Model | Variants | Notes |
|-------|----------|-------|
| `antigravity-gemini-3-pro` | low, high | Gemini 3 Pro with thinking |
| `antigravity-gemini-3.1-pro` | low, high | Gemini 3.1 Pro with thinking (rollout-dependent) |
| `antigravity-gemini-3-flash` | minimal, low, medium, high | Gemini 3 Flash with thinking |
| `antigravity-claude-sonnet-4-6` | — | Claude Sonnet 4.6 |
| `antigravity-claude-opus-4-6-thinking` | low, max | Claude Opus 4.6 with extended thinking |

**Gemini CLI quota** (independent pool):

| Model | Notes |
|-------|-------|
| `gemini-2.5-flash` | Gemini 2.5 Flash |
| `gemini-2.5-pro` | Gemini 2.5 Pro |
| `gemini-3-flash-preview` | Gemini 3 Flash (preview) |
| `gemini-3-pro-preview` | Gemini 3 Pro (preview) |
| `gemini-3.1-pro-preview` | Gemini 3.1 Pro (preview, rollout-dependent) |
| `gemini-3.1-pro-preview-customtools` | Gemini 3.1 Pro Preview Custom Tools (preview, rollout-dependent) |

**Routing behavior (verbatim from README):**
- *Antigravity-first (default):* Gemini models use Antigravity quota across accounts.
- *CLI-first (`cli_first: true`):* Gemini models use Gemini CLI quota first.
- When a Gemini quota pool is exhausted, the plugin automatically falls back to the other pool.
- Claude and image models always use Antigravity.
- Model names are automatically transformed for the target API (e.g., `antigravity-gemini-3-flash` → `gemini-3-flash-preview` for CLI).

**Corpus-first observation:** Plugin exposes 11 distinct model identifiers (5 Antigravity-quota + 6 Gemini-CLI-quota) where 5 of the Gemini variants point to the same underlying Google model under different quota pools. This is **model-aliasing-as-quota-multiplexing** — a single physical model (e.g., Gemini 3 Pro) is exposed twice for the same user under two API endpoints to double the effective quota.

---

## 6. Multi-account setup (README §"Multi-Account Setup")

```bash
opencode auth login  # Run again to add more accounts
```

Account-management options (via `opencode auth login` interactive menu):
- **Configure models** — Auto-configure all plugin models in `opencode.json`
- **Check quotas** — View remaining API quota for each account
- **Manage accounts** — Enable/disable specific accounts for rotation

The plugin auto-rotates between accounts when one is rate-limited. The README defers load-balancing/dual-quota-pool/storage details to `docs/MULTI-ACCOUNT.md` (Cluster 3).

---

## 7. Troubleshooting section — 12+ explicit error patterns documented

Documented errors (verbatim error strings preserved where possible):

1. **`403 Permission Denied (rising-fact-p41fc)`** — plugin's default project ID falls back when no valid project; works for Antigravity but fails for Gemini CLI. Solution: create GCP project + enable `cloudaicompanion.googleapis.com` API + add `projectId` to accounts.json.
2. **"Gemini Model Not Found"** — requires `"npm": "@ai-sdk/google"` override in provider config.
3. **`Invalid JSON payload received. Unknown name "parameters" at 'request.tools[0]'`** — Gemini 3 tool-schema incompatibility. Three solutions: update beta / disable MCP servers one-by-one / npm override.
4. **`Invalid function name must start with a letter or underscore`** — MCP tool name starts with a number (e.g., `1mcp_*`). Solution: rename MCP key to start with letter (e.g., `gw`).
5. **"All Accounts Rate-Limited" (but quota available)** — cascade bug in `clearExpiredRateLimits()` hybrid mode. Solution: update beta / reauth / switch `account_selection_strategy` to `"sticky"`.
6. **Session recovery** — Type `continue` to trigger recovery; if blocked, use `/undo` to revert to pre-error state.
7. **Oh-My-OpenCode conflicts** — Disable built-in google_auth in `oh-my-opencode.json` to prevent conflicts.
8. **Infinite `.tmp` files** — when account is rate-limited and plugin retries infinitely. Cleanup: `rm ~/.config/opencode/*.tmp`.
9. **Safari OAuth callback fails (macOS)** — Safari's HTTPS-Only Mode blocks `http://localhost`. Solutions: use Chrome/Firefox / disable HTTPS-Only Mode temporarily.
10. **Port conflict (51121)** — `lsof -i :51121` then `kill -9 PID`.
11. **Docker/WSL2/remote dev** — OAuth callback requires browser-to-localhost. Solutions: VS Code port forwarding / `ssh -L 51121:localhost:51121`.
12. **Configuration key typo `plugin` vs `plugins`** — singular is correct; plural causes "Unrecognized key" error.
13. **Migrating accounts between machines** — copy `antigravity-accounts.json`; if `API key missing` error, refresh token may be invalid → re-authenticate.

**Corpus observation:** Troubleshooting section runs ~250 lines of the 718-line README — **35% of the README is failure-mode documentation**. v62 codex-plugin-cc had minimal troubleshooting (~5%); v66 agentmemory deferred troubleshooting to GitHub issues. opencode-antigravity-auth's troubleshooting-density is corpus-high for a solo-utility plugin.

---

## 8. Plugin compatibility (README §"Plugin Compatibility")

**`@tarquinen/opencode-dcp`** — DCP creates synthetic assistant messages that lack thinking blocks. Plugin ordering matters:

```json
{
  "plugin": [
    "opencode-antigravity-auth@latest",
    "@tarquinen/opencode-dcp@latest"
  ]
}
```

**`oh-my-opencode`** — disable built-in `google_auth: false` + override agent models:

```json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

**Plugins-you-don't-need warning:** *"gemini-auth plugins — Not needed. This plugin handles all Google OAuth."*

**Corpus observation:** Plugin coexistence is documented to the level of plugin-array-ordering semantics. The Opencode plugin runtime has order-dependent fetch-interception behavior. This is the FIRST corpus subject documenting plugin-ordering-as-correctness-concern in a multi-plugin agent runtime.

---

## 9. Configuration options block (verbatim category list)

The README's `## Configuration` section enumerates 4 category groups (full details in `docs/CONFIGURATION.md`):

**Model Behavior:**
- `keep_thinking` (default `false`) — preserve Claude's thinking across turns. *Warning: enabling may degrade model stability.*
- `session_recovery` (default `true`) — auto-recover from tool errors
- `cli_first` (default `false`) — route Gemini models to Gemini CLI first (Claude and image models stay on Antigravity)

**Account Rotation:**

| Setup | Recommended config |
|-------|-------------------|
| 1 account | `"account_selection_strategy": "sticky"` |
| 2-5 accounts | Default `"hybrid"` |
| 5+ accounts | `"account_selection_strategy": "round-robin"` |
| Parallel agents | Add `"pid_offset_enabled": true` |

**Quota Protection:**
- `soft_quota_threshold_percent` (default 90) — skip account when quota usage exceeds; prevents Google from penalizing accounts that fully exhaust quota
- `quota_refresh_interval_minutes` (default 15) — background quota refresh interval
- `soft_quota_cache_ttl_minutes` (default `"auto"`) — quota cache freshness

**Rate Limit Scheduling:**

| Mode | Behavior |
|------|----------|
| `cache_first` (default) | Wait for same account (preserves prompt cache) |
| `balance` | Switch immediately when rate-limited |
| `performance_first` | Round-robin |

**Corpus observation:** The phrase *"prevents Google from penalizing accounts that fully exhaust quota"* is a corpus-first: it directly states the plugin's design accounts for ADVERSARIAL VENDOR BEHAVIOR — i.e., quota-exhaustion as a vendor-side signal triggering further penalties. The 90% threshold is a deliberate operational defense against vendor enforcement.

---

## 10. Credits + Acknowledgements

The README explicitly credits:
- **[opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth)** by @jenslys — predecessor for Gemini-only auth
- **[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** — separate Antigravity-bridge project

Both predecessors are NOT in the corpus (neither is a wiki subject as of v66). NoeFabris's credit-line is short but factual.

---

## 11. Support model

**Ko-fi tipjar:**
```
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S81QBOIR)
```

Section title: *"If this plugin saves you time, consider supporting its development"*.

**Corpus observation:** Ko-fi tipjar for a TOS-violation tool is monetization-via-gratuity-model rather than monetization-via-commercial-license (the latter would require legitimate vendor relationship). v64 claude-seo had Pro Hub Challenge community-curation (Pattern #82 candidate); v66 agentmemory had no monetization visible. opencode-antigravity-auth's tipjar is the first explicit author-monetization on a single-author corpus subject of the legally-gray-utility type.

---

## 12. Cluster summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | Most explicit ToS-violation disclosure in 66-wiki corpus (`[!CAUTION]` block, open-by-default, 3-bullet user-acknowledgment block, footer Legal block) | corpus-first |
| 2 | Agentic-installation-as-first-class-UX (Option A = "paste this into any LLM agent") | corpus-second (after v64 claude-seo `make install` and v66 agentmemory's iii-CLI extensibility — opencode-antigravity-auth is the most explicit "LLM-as-installer" framing) |
| 3 | Model-aliasing-as-quota-multiplexing (same physical model exposed under 2 API quota pools for the same user) | corpus-first |
| 4 | 35% of README is failure-mode documentation (~250/718 lines troubleshooting) | corpus-high for solo-utility |
| 5 | Plugin-ordering-as-correctness-concern (plugin-array order affects fetch-interception correctness) | corpus-first |
| 6 | Explicit operational defense against adversarial vendor behavior (90% soft quota threshold = "prevents Google from penalizing accounts that fully exhaust quota") | corpus-first |
| 7 | Ko-fi tipjar on legally-gray-utility tool | corpus-first |
| 8 | Author NoeFabris (`@dopesalmon`) — solo independent | sibling to v62 codex-plugin-cc author (OpenAI corporate) — solo-utility T4 Bridge contrast |

## 13. Counter-evidence + Pattern Library implications from Cluster 1

- **Pattern #83 Honest-Deficiency-Disclosure (CANDIDATE N=2 at v66):** STRONG N=3 evidence. ToS warning is textbook: (a) explicit categorical deficiency disclosure (account suspension risk + ToS violation), (b) user-facing surface (README opens with it), (c) does NOT minimize ("Your account may be suspended or permanently banned"). All 3 promotion criteria satisfied.
- **Pattern #84 Cross-Vendor Ecosystem-Tolerance (CANDIDATE N=2 at v66):** REFINEMENT evidence. Google's apparent non-enforcement against the REPO (10.5K stars + 91 releases + active npm package — sub-DMCA threshold maintained) co-exists with active vendor enforcement at the USER-ACCOUNT level (account bans, shadow-bans). This refines #84's tolerance-mechanism scope: vendor-tolerance has account-level enforcement as a release valve.
- **NEW observational candidate:** "Explicit-ToS-Violation Tool architecture" — framework whose CORE value proposition explicitly bypasses a vendor's ToS, foregrounded with `[!CAUTION]` blocks rather than buried. Distinct from gray-area scrapers / unofficial-API-wrappers by upfront acknowledgment + multi-account-rotation infrastructure built SPECIFICALLY to absorb enforcement consequences (soft quota threshold = "prevents Google from penalizing").
- **Pattern #18 shared-backend-service sub-archetype (v66 NEW):** Possible N=2 — many-accounts-one-backend mechanism (the architectural-inverse of agentmemory's many-platforms-one-server). Flag for v68 stale-check inclusion as nuance evidence rather than direct N=2 strengthening.

---

## 14. References

- README.md (718 lines) — primary source for this cluster
- [opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth) — predecessor (not in corpus)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) — sibling project (not in corpus)

## 15. Next cluster

Cluster 2: Contributor + architecture docs (AGENTS.MD + docs/ARCHITECTURE.md + package.json) — Module layout, code style, Claude-specific handling, session recovery, schema sanitization, dependencies.
