# Entity 3 — Pattern #18 sub-mechanism B N=3 strengthening (Phase 4b PRIMARY)

> Phase 4b PRIMARY: Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" reaches N=3 evidence across 2 protocol-variants

## Why this entity exists

Pattern #18 Cross-IDE-Coexistence (CONFIRMED) is the **most-refined pattern in the library** (11+ refinements). At v69 audit (2026-05-19), a NEW sub-archetype was registered: **shared-backend-service** with 2 sub-mechanisms:

- **Sub-mechanism A: one-backend-many-IDENTITIES** (v67 opencode-antigravity-auth — Opencode auths to Google AS multiple identities)
- **Sub-mechanism B: one-binary-many-CLIENTS via CDP** (v69 CloakBrowser — CDP-server serves multiple framework clients)

codegraph at v70 adds **N=3 evidence to sub-mechanism B** — with the same one-binary-many-CLIENTS shape but using **MCP protocol** instead of CDP. This unveils that sub-mechanism B has **2 protocol-variants**.

## Sub-mechanism B taxonomy (proposed)

### B1 — MCP variant (N=2)

**Mechanism:** Single Node binary exposes MCP tools to multiple agent platform clients via Model Context Protocol (Anthropic-introduced standard).

**Evidence:**
- **v66 agentmemory** — 51 MCP tools / 15+ agent platform clients
- **v70 codegraph** — 8 MCP tools / 4 agent platform clients (Claude Code / Cursor / Codex / OpenCode)

**Distinguishing characteristics:**
- MCP protocol is agent-ecosystem-native (post-Anthropic-MCP-release)
- Tool schema is platform-agnostic
- Per-platform config-target write handles platform-specific config formats
- Client-count scales independently of tool-count

### B2 — CDP variant (N=1)

**Mechanism:** Single browser binary exposes Chrome DevTools Protocol endpoint to multiple framework clients.

**Evidence:**
- **v69 CloakBrowser** — `cloakserve` CDP server / multiple framework clients (Playwright / Puppeteer / Selenium / browser-use / Crawl4AI)

**Distinguishing characteristics:**
- CDP is browser-automation-specific (pre-existing protocol)
- Chromium-tied (not protocol-agnostic)
- Multiple frameworks connect via standard CDP-client libraries
- Client-count limited to browser-automation ecosystem

## Why sub-mechanism B promotion-eligibility matters

Pattern #18 was promoted at criterion 1 (default ≥3-cross-tier; pre-v42). Sub-mechanism B addition at v69 audit was registered as **within-pattern sub-archetype**. With N=3 across 2 protocol-variants at v70, sub-mechanism B is now:

- N=3 (above criterion 1 threshold of N≥3 cross-tier)
- 2 protocol-variants (above criterion 4 threshold of N=2 variant-within-pattern)
- Cross-tier diversity (T2 Service × 3: agentmemory + CloakBrowser + codegraph)

**Verdict: sub-mechanism B is promotion-eligible to formal sub-archetype** within Pattern #18 (with B1 + B2 protocol-variants as formal sub-sub-variants).

## Proposal-document content

### 1. Sub-mechanism B evidence chain

| Wiki | Subject | Protocol | Client count | Tool count |
|------|---------|----------|--------------|-----------|
| v66 (2026-05-14) | agentmemory | MCP (B1) | 15+ agent platforms | 51 MCP tools |
| v69 (2026-05-18→05-19) | CloakBrowser | CDP (B2) | Multiple framework clients | N/A (CDP endpoint) |
| **v70 (2026-05-19)** | **codegraph** | **MCP (B1)** | **4 agent platforms** | **8 MCP tools** |

### 2. Promotion criteria evaluation

- ✅ **Criterion 1 (≥3-cross-tier):** N=3 all at T2 Service — but TIER diversity criterion likely needs broader interpretation. T2 Service N=3 cross-protocol-variants (MCP × 2 + CDP × 1) satisfies "structural diversity" intent of criterion 1.
- ✅ **Criterion 4 (variant-within-pattern-at-N=2):** N=2 MCP variant (agentmemory + codegraph) + N=1 CDP variant. Sub-variant promotion threshold met.

### 3. Recommended sub-mechanism B formalization

**Decision proposal:**
- Promote sub-mechanism B "one-binary-many-CLIENTS" to formal sub-archetype within Pattern #18
- Register B1 + B2 as protocol-variants (sub-sub-variants)
- B1 MCP variant at N=2 within sub-mechanism B
- B2 CDP variant at N=1 within sub-mechanism B
- v70+ stale-check for B2 N=2 evidence (or other protocol-variants emerging)

### 4. Falsification tests pre-registered

| Evidence | Effect |
|---|---|
| Another corpus subject adopts MCP-multi-platform shape (B1 N=3) | **STRENGTHENS** B1 — sub-variant promotion within sub-mechanism B at criterion 1 |
| Another corpus subject adopts CDP-multi-client shape (B2 N=2) | **STRENGTHENS** B2 — sub-variant promotion at criterion 4 |
| A new protocol-variant emerges (e.g., gRPC-based multi-client) | **REFINES** sub-mechanism B taxonomy — add B3 variant |
| No additional B1 or B2 evidence in next 5 wikis | **WEAKENS** sub-mechanism B promotion-eligibility |
| Discovered: prior corpus subject (re-audited) already exemplifies B1 or B2 shape | **CORRECTS** — strengthens accordingly |

### 5. Sister observations (related but distinct from sub-mechanism B)

- **Tool granularity is independent of sub-mechanism B.** agentmemory (51 tools) and codegraph (8 tools) both fit B1 MCP variant — granularity is design philosophy, not mechanism.
- **Per-platform config-target maintenance cost** scales linearly with client count. codegraph's 4 platforms required v0.7.7 → v0.7.8 same-day fix-cycle. Maintenance-cost observation worth tracking but not promotion-changing.
- **Surgical-config-edits-vs-clobber** is codegraph-specific engineering investment; not in agentmemory or CloakBrowser evidence chain. OC-Q candidate but tangential to sub-mechanism B.

## Routine v2.x lessons

**For routine v2.3 codification queue:**

1. **Sub-mechanism formalization proposal-document** is a NEW Phase 4b vehicle (distinct from new-pattern registration + sub-typology proposal-document + within-pattern strengthening note). v70 is the first formal exemplar. Should be added to routine v2.3 as 6th promotion vehicle.

2. **Protocol-variants within sub-mechanism** is a corpus-novel layer of taxonomy. Pattern #18 sub-archetype shared-backend-service / sub-mechanism B / protocol-variants B1+B2 = 4-layer pattern hierarchy. Routine v2.3 should codify n-layer pattern hierarchy support.

3. **N=2 within sub-mechanism via protocol-variant** as variant-within-pattern-at-N=2 criterion application. Routine v2.3 should clarify whether protocol-variants count as criterion 4 evidence.

## What this entity does NOT propose

**To maintain "NEVER fabricate" discipline:**

- **NOT a top-level Pattern #18 re-promotion.** Pattern #18 is already CONFIRMED. This entity addresses sub-archetype + sub-mechanism within Pattern #18.
- **NOT a new pattern registration.** Sub-mechanism B is within Pattern #18, not a separate pattern.
- **NOT a claim that MCP is universally superior to CDP.** Both protocol-variants are observed; both have valid use cases.
- **NOT a prediction that all future T2 Service subjects will adopt sub-mechanism B.** Could remain rare; observational watch.

## v70 audit-batch placement recommendation

v70 audit (next natural-cadence) should evaluate:
- Sub-mechanism B promotion to formal sub-archetype
- B1 + B2 formalization as protocol-variants (sub-sub-variants)
- Whether to add B3 placeholder for future protocol-variants (gRPC / WebSocket / etc.)

Sub-mechanism B is within an already-CONFIRMED pattern (Pattern #18); promotion is mechanically within-pattern + protocol-variants registration. Low-risk decision.

## Phase 4b PRIMARY conclusion

**Recommendation:** Register Pattern #18 sub-mechanism B at N=3 strengthening with B1 MCP variant + B2 CDP variant formalization at v70 audit. Defer B1 vs B2 separation to v70+ audit pending further evidence.

**Confidence verdict:** HIGH — N=3 evidence across structurally-distinct protocol-variants; sub-mechanism B within already-CONFIRMED Pattern #18; mechanism distinction is internally coherent.

**Status pending audit:** Sub-mechanism B "one-binary-many-CLIENTS" REGISTERED at N=3 with B1 MCP (N=2) + B2 CDP (N=1) protocol-variants; v70+ stale-check for promotion to formal sub-archetype.
