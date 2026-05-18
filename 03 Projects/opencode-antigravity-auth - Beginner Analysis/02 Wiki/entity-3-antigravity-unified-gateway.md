# (C) Entity 3: Antigravity Unified Gateway — Google's Claude/Gemini/GPT-OSS gateway

**Type:** Phase 4b PRIMARY entity — Pattern #83 Honest-Deficiency-Disclosure N=3 strengthening target
**Slot:** Entity 3 of 4
**Sibling entities:** [Entity 1 — OAuth bridge core](entity-1-oauth-bridge-core.md) / [Entity 2 — Multi-account quota-multiplexing](entity-2-multi-account-quota-multiplexing.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. What Antigravity is (per plugin's own discovery doc)

The plugin's `docs/ANTIGRAVITY_API_SPEC.md` opens with this verbatim characterization:

> *"Antigravity is Google's **Unified Gateway API** for accessing multiple AI models (Claude, Gemini, GPT-OSS) through a single, consistent Gemini-style interface. It is NOT the same as Vertex AI's direct model APIs."*

**Key characteristics (verbatim):**
- Single API format for all models (Gemini-style)
- Project-based access via Google Cloud authentication
- Internal routing to model backends (Vertex AI for Claude, Gemini API for Gemini)
- Unified response format (`candidates[]` structure for all models)

The doc is dated **"Last Updated: December 13, 2025"** with status **"Verified by Direct API Testing"**. This is not a contract with Google; it is an empirical discovery dossier. The plugin's continued operation depends on the gateway behaving consistently with what was discovered — a relationship with NO vendor commitment.

---

## 2. Why this entity is the Phase 4b PRIMARY target

Three reasons make Antigravity the PRIMARY pattern-library-implication entity for v67:

**Reason 1 — Pattern #83 N=3 evidence:** The plugin's README opens with an explicit `[!CAUTION]` block warning that *"Using this plugin (and any proxy for Antigravity) violates Google's Terms of Service. A number of users have reported their Google accounts being **banned** or **shadow-banned**."* This is textbook Pattern #83 Honest-Deficiency-Disclosure evidence — the deficiency being disclosed is the closed-vendor enforcement risk that the plugin's existence depends on circumventing.

**Reason 2 — Closed-vendor-internal-gateway-as-discovered-surface:** This is the FIRST corpus subject documenting a closed-vendor product whose API was discovered (not granted), verified by direct testing, and used at scale (10.5K stars). The corpus-distinctive observation is that the gateway uses Google-internal URL conventions (`/v1internal:*` action paths) and OAuth scopes (`cclog`, `experimentsandconfigs`) that signal non-public-API status.

**Reason 3 — Multi-vendor brokering by closed vendor:** Antigravity hosts Anthropic (Claude Opus 4.6 + Sonnet 4.6) and OpenAI (GPT-OSS 120B Medium) models inside Google's IDE alongside Google's own (Gemini 3 Pro/Flash). This is **competitor-model-hosting-by-closed-vendor** — Google brokering Anthropic + OpenAI models inside its own product. Strengthens Pattern #84 cross-vendor-ecosystem-tolerance at the closed-vendor level (vs. v62/v65's open-source-cross-vendor-cooperation evidence).

---

## 3. Three endpoint environments (the plugin's fallback chain)

From `docs/ANTIGRAVITY_API_SPEC.md`:

| Environment | URL | Status (as of plugin v1.6.0) |
|-------------|-----|------------------------------|
| **Daily (Sandbox)** | `daily-cloudcode-pa.sandbox.googleapis.com` | ✅ Active |
| **Production** | `cloudcode-pa.googleapis.com` | ✅ Active |
| **Autopush (Sandbox)** | `autopush-cloudcode-pa.sandbox.googleapis.com` | ❌ Unavailable |

The plugin's endpoint fallback chain is **daily → autopush → prod**. Why Google exposes 3 environments to consumer OAuth tokens — and why the plugin can fall back across them — is not documented; this is the kind of operational fact that gets discovered, not announced.

(Per the v1.5.0 CHANGELOG, the plugin v1.5.0 also fetches Antigravity's own version-check endpoint at startup to stay current with what Antigravity expects — "Dynamic Antigravity Version".)

---

## 4. API actions (verbatim)

```
/v1internal:generateContent      — Non-streaming request
/v1internal:streamGenerateContent?alt=sse  — Streaming (SSE) request
/v1internal:loadCodeAssist       — Project discovery
/v1internal:onboardUser          — User onboarding
```

The `/v1internal:*` URL path prefix and verb-suffix syntax (`:generateContent` rather than RESTful `/v1/generateContent`) are signatures of **internal Google API conventions** (these match the gRPC-derived AIP / Google AIP-136 patterns).

---

## 5. Required headers (verbatim from API spec)

```http
Authorization: Bearer {access_token}
Content-Type: application/json
User-Agent: antigravity/1.15.8 windows/amd64
X-Goog-Api-Client: google-cloud-sdk vscode_cloudshelleditor/0.1
Client-Metadata: {"ideType":"ANTIGRAVITY","platform":"MACOS","pluginType":"GEMINI"}
```

The `Client-Metadata` header carries Antigravity Manager's identity claims. The plugin reproduces this exact header shape (per v1.5.1 CHANGELOG) to be indistinguishable from the real Antigravity client. The `User-Agent: antigravity/1.15.8 windows/amd64` is verbatim what the real Antigravity desktop client sends.

**OAuth scopes (5):**
```
https://www.googleapis.com/auth/cloud-platform
https://www.googleapis.com/auth/userinfo.email
https://www.googleapis.com/auth/userinfo.profile
https://www.googleapis.com/auth/cclog
https://www.googleapis.com/auth/experimentsandconfigs
```

`cclog` and `experimentsandconfigs` are non-standard Google scopes — `cclog` likely refers to **Cloud Code log** (the predecessor or rename of Antigravity); `experimentsandconfigs` likely refers to Google's internal A/B-testing infrastructure. Neither is documented in Google's public OAuth scope reference.

---

## 6. Available models (verbatim)

| Model name | Model ID | Vendor | Status |
|------------|----------|--------|--------|
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Anthropic | ✅ Verified |
| Claude Opus 4.6 Thinking | `claude-opus-4-6-thinking` | Anthropic | ✅ Verified |
| Gemini 3 Pro High | `gemini-3-pro-high` | Google | ✅ Verified |
| Gemini 3 Pro Low | `gemini-3-pro-low` | Google | ✅ Verified |
| GPT-OSS 120B Medium | `gpt-oss-120b-medium` | Other | ✅ Verified |

**Internal routing:** Antigravity routes Claude requests to Vertex AI (Anthropic-on-Google-Cloud) and Gemini requests to Google's Gemini API. GPT-OSS routing is not specified by the doc (likely Vertex AI's GPT-OSS hosting).

Plus additional Gemini variants documented at the plugin's README level (Gemini 3.1 Pro, Gemini 3 Flash with minimal/low/medium/high thinking levels) that the plugin exposes but the API-spec doc treats as variants of the verified core set.

---

## 7. Wire format requirements (critical)

The doc states bluntly:

> *"**⚠️ IMPORTANT: Must use Gemini-style format. Anthropic-style `messages` array is NOT supported.**"*

**Contents:**
```json
{
  "contents": [
    { "role": "user", "parts": [{ "text": "Your message" }] },
    { "role": "model", "parts": [{ "text": "Assistant response" }] }
  ]
}
```

**Role values:**
- `user` — Human messages
- `model` — Assistant responses (**NOT** `assistant` — Anthropic's convention is rejected)

**System instructions:** Must be `{ "parts": [...] }` object, NOT plain string. Plain string returns 400.

**Generation config:** Standard `maxOutputTokens` / `temperature` / `topP` / `topK` / `stopSequences` / `thinkingConfig`.

**Tools / function calling:**
```json
{
  "tools": [{ "functionDeclarations": [{ "name": "...", "parameters": {...} }] }]
}
```

**Function name rules:** Must start with letter or underscore; allowed chars `a-zA-Z0-9_.:-`; max 64 chars; NO slashes or spaces. This is the source of the troubleshooting note "MCP tool name starts with a number" — Antigravity rejects function names beginning with digits (e.g., `1mcp_*`).

---

## 8. JSON Schema feature compatibility matrix (verbatim)

| Feature | Antigravity status |
|---------|-------------------|
| `type`, `properties`, `required`, `description`, `enum`, `items` | ✅ Supported |
| `anyOf`, `allOf`, `oneOf` | ✅ Supported (converted to `any_of`/`all_of`/`one_of` internally) |
| `additionalProperties` | ✅ Supported |
| `const` | ❌ Use `enum: [value]` instead |
| `$ref` | ❌ Inline the schema |
| `$defs` / `definitions` | ❌ Inline definitions |
| `$schema` / `$id` | ❌ Strip metadata |
| `default` / `examples` | ❌ Strip documentation fields |
| `title` (nested) | ⚠️ Caution (may cause issues) |

The plugin's `schema-transform.ts` module handles all conversions automatically. The strict subset informs which JSON Schema features upstream tools (e.g., MCP servers) can rely on; anything outside the supported set must be transformed by the plugin before reaching Antigravity.

---

## 9. Response format (the unified envelope)

All Antigravity responses use the same envelope regardless of which underlying model handled the request:

```json
{
  "response": {
    "candidates": [
      {
        "content": {
          "role": "model",
          "parts": [{ "text": "Response text" }]
        },
        "finishReason": "STOP"
      }
    ],
    "usageMetadata": {
      "promptTokenCount": 16,
      "candidatesTokenCount": 4,
      "totalTokenCount": 20
    },
    "modelVersion": "claude-sonnet-4-6",
    "responseId": "msg_vrtx_..."
  },
  "traceId": "abc123..."
}
```

**Response ID format reveals routing:**

| Model type | Response ID prefix | Example |
|------------|-------------------|---------|
| Claude | `msg_vrtx_*` | `msg_vrtx_01UDKZG8PWPj9mjajje8d7u7` |
| Gemini | Base64-like | `ypM9abPqFKWl0-kPvamgqQw` |
| GPT-OSS | Base64-like | `y5M9aZaSKq6z2roPoJ7pEA` |

The `msg_vrtx_*` prefix on Claude responses reveals **Vertex AI** as the underlying Claude provider — confirming Antigravity is routing Claude requests through Google's Vertex-AI-hosted Anthropic offering, not directly to Anthropic.

---

## 10. The Google Search grounding limitation

The doc documents an Antigravity API constraint:

> *"Gemini models support Google Search grounding, but **it cannot be combined with function declarations** in the same request."*

The plugin's workaround (`google_search` tool added v1.3.1):
1. Model calls `google_search(query, urls?, thinking?)`
2. Plugin makes a **separate API call** to Antigravity with only `{ googleSearch: {} }` (no function declarations)
3. Parses `groundingMetadata` from response
4. Returns formatted markdown with sources + citations

**This is API-limitation-as-architectural-workaround.** The plugin synthesizes a separate API call to bridge two mutually-exclusive Antigravity capabilities (tool use + search grounding) into a single user-facing experience.

---

## 11. Pattern #83 N=3 evidence catalog

The Antigravity entity's relationship to Pattern #83 Honest-Deficiency-Disclosure produces multiple distinct disclosure surfaces:

| # | Disclosure surface | What's disclosed |
|---|-------------------|------------------|
| 1 | README `[!CAUTION]` block (open-by-default) | "Using this plugin violates Google's Terms of Service" + "accounts banned or shadow-banned" |
| 2 | README "Legal" footer (collapsed `<details>`) | "Terms of Service risk" + "Account risk" + "No guarantees" + "Assumption of risk" |
| 3 | README "Intended Use" | "Personal / internal development only; Not for production services or bypassing intended limits" |
| 4 | docs/ANTIGRAVITY_API_SPEC.md "Last Updated" + "Verified by Direct API Testing" | Explicit empirical-discovery status (not vendor contract) |
| 5 | CHANGELOG entries | Repeated honest naming of detection-patterns + enforcement-mechanism responses ("Auth headers aligned with official Gemini CLI... to reduce 'account ineligible' errors and potential bans"; "Linux users now masquerade as macOS"; "Skip account over 90% to prevent Google penalties") |

All five disclosure surfaces satisfy Pattern #83's 3 criteria:
1. **Explicit numerical or categorical deficiency disclosure** — categorical (TOS violation + account ban + shadow-ban + ineligibility) and quantitative (90% threshold)
2. **User-facing surface** (README + CHANGELOG + release notes) — yes, README opens with it
3. **Does NOT minimize or normalize** the deficiency — "Your account may be suspended or permanently banned" is the opposite of minimization

→ Pattern #83 N=3 promotion-eligible at next audit (v64 + v65 + v67 = 3 subjects with matching disclosure discipline).

---

## 12. Pattern #84 refinement evidence

Pattern #84 Cross-Vendor Ecosystem-Tolerance (CANDIDATE N=2 at v66) gets NUANCED evidence from this entity:

**PRO #84:** Antigravity hosts Claude + GPT-OSS alongside Gemini = closed-vendor brokers competitors. Substantial cross-vendor cooperation at vendor level.

**CONTRA #84:** Google actively enforces against unauthorized Antigravity access (account bans, shadow-bans, 403 `validation_required` challenges, soft quota threshold pressures). Vendor tolerance has hard limits.

**Reconciliation:** The repo itself (10.5K stars, npm package, 91 releases) is tolerated at the **sub-DMCA threshold** — no legal challenge to the artifact. Individual unauthorized USAGE is enforced at the account level. This refines Pattern #84's tolerance-mechanism scope:

→ **Refinement statement:** *Vendor-tolerance distinguishes between the artifact (tolerated as fair-research / dev-utility / community speech) and the usage (enforced at account level). Account-level enforcement is a release valve that allows vendor to maintain plausible non-enforcement against the tool while still defending the business model.*

This refinement is a candidate sub-mechanism within Pattern #84 (84a tool-tolerance, 84b usage-enforcement). Flag for v68 audit consideration.

---

## 13. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v65 claude-code-system-prompts](../../claude-code-system-prompts - Beginner Analysis/CLAUDE.md)** | Same closed-vendor-product-surface engagement axis: claude-code-system-prompts is third-party reverse-engineering of Anthropic's product; this Antigravity API spec is the plugin author's reverse-engineering of Google's gateway. Both are "discovered-surfaces" with empirical-only validation. |
| **[v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md)** | Counter-example — codex-plugin-cc is published BY the vendor (OpenAI) FOR a competitor (Anthropic Claude Code). Opposite arrangement: this plugin is published BY an unauthorized solo developer TO use a closed vendor's (Google's) internal gateway. |

---

## 14. References

- docs/ANTIGRAVITY_API_SPEC.md (634 lines, primary)
- README.md §"Terms of Service Warning" + §"Legal"
- CHANGELOG.md (267 lines)
- Cross-cluster: `cluster-1-readme-and-tos-framing.md` + `cluster-3-quota-api-and-changelog.md`
- **Phase 4b PRIMARY proposal-document:** [Pattern-83 promotion proposal](../01 Analysis/(C) Pattern-83 Honest-Deficiency-Disclosure N=3 promotion proposal.md) (TO BE WRITTEN at Phase 4b)
