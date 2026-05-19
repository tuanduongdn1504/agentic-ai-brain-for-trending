# (C) Pattern #18 sub-mechanism B "one-binary-many-CLIENTS" N=3 protocol-variants formalization

> Phase 4b PRIMARY proposal-document for v70 codegraph wiki · routine v2.2 · audit-target v70+ batch

## Executive summary

**Proposal:** Register Pattern #18 sub-archetype shared-backend-service sub-mechanism B "one-binary-many-CLIENTS" at **N=3 evidence with 2 protocol-variants formalized** (B1 MCP variant N=2 + B2 CDP variant N=1).

**Confidence:** **HIGH** — N=3 evidence cross-protocol-variants; sub-mechanism B within already-CONFIRMED Pattern #18; mechanism distinction (MCP vs CDP) is internally coherent + observable.

**Status at registration:** Sub-mechanism B REGISTERED at N=3 with protocol-variants B1 + B2. Sub-mechanism B promotion to formal sub-archetype DEFERRED to v70+ audit (criterion 1 ≥3-cross-tier requires broader interpretation since all 3 are T2 Service; criterion 4 variant-within-pattern-at-N=2 met via B1 N=2 + B2 N=1).

**Routine v2.x lessons captured:** Sub-mechanism formalization proposal-document as NEW Phase 4b vehicle (6th promotion vehicle). Protocol-variants within sub-mechanism as corpus-novel taxonomy layer.

---

## 1. Pattern #18 background

**Pattern #18 Cross-IDE-Coexistence** is the **most-refined pattern in the library** (11+ refinements). CONFIRMED pre-v42. Multiple layers + sub-archetypes + sub-mechanisms already registered.

At v69 OVERDUE-NATURAL-CADENCE mini-audit (2026-05-19), **NEW sub-archetype shared-backend-service** was registered with 2 sub-mechanisms:

- **Sub-mechanism A: one-backend-many-IDENTITIES** (v67 opencode-antigravity-auth) — Opencode auths to Google AS multiple identities
- **Sub-mechanism B: one-binary-many-CLIENTS** (v69 CloakBrowser) — single binary serves multiple framework clients (initially registered with CDP variant only)

codegraph at v70 adds N=3 evidence to sub-mechanism B but with a **different protocol variant** — exposing that sub-mechanism B has multiple protocol-variants worth formalizing.

---

## 2. codegraph N=3 evidence

### 2.1 codegraph mechanism description

codegraph is a **TypeScript Node binary** that exposes 8 MCP tools to 4 agent platforms (Claude Code / Cursor / Codex CLI / OpenCode) via Model Context Protocol. The architectural diagram (verbatim from README) is:

```
Claude Code / Cursor / Codex CLI / opencode
            ↓
    CodeGraph MCP Server
    ├── Search tool
    ├── Callers/Callees
    └── Context builder
            ↓
    SQLite Graph Database
```

**Architectural shape:** 4 agent clients ABOVE the MCP server ABOVE the SQLite database. Multi-client connecting to single server = sub-mechanism B "one-binary-many-CLIENTS."

### 2.2 Protocol identification

codegraph uses **MCP (Model Context Protocol)** — same protocol as v66 agentmemory. NOT CDP (CloakBrowser's protocol).

### 2.3 Distinguishing characteristics

| Axis | codegraph (v70) | agentmemory (v66) | CloakBrowser (v69) |
|------|-----------------|-------------------|---------------------|
| Protocol | **MCP** | **MCP** | **CDP** |
| Tool count | 8 | 51 | N/A (CDP endpoint) |
| Client count | 4 agent platforms | 15+ agent platforms | Multiple framework clients |
| Tier | T2 Service | T2 Service | T2 Service |
| Domain | Code knowledge graph | Persistent memory | Stealth browser |

---

## 3. Sub-mechanism B taxonomy (proposed)

### 3.1 B1 — MCP variant

**Mechanism:** Single binary exposes MCP tools to multiple agent platform clients via Model Context Protocol (Anthropic-introduced standard).

**Evidence (N=2):**
- **v66 agentmemory** — `rohitg00/agentmemory` — 51 MCP tools / 15+ agent platform clients (Claude Code / Cursor / Cline / Continue / etc.)
- **v70 codegraph** — `colbymchenry/codegraph` — 8 MCP tools / 4 agent platform clients (Claude Code / Cursor / Codex / OpenCode)

**Distinguishing characteristics:**
- MCP protocol is agent-ecosystem-native (post-Anthropic-MCP-release ~late-2024)
- Tool schema platform-agnostic; per-platform config-target write handles platform-specific config formats
- Client-count scales independently of tool-count
- Both N=2 subjects are MIT/Apache-2.0 + solo-individual archetype + T2 Service

### 3.2 B2 — CDP variant

**Mechanism:** Single browser binary exposes Chrome DevTools Protocol endpoint to multiple framework clients.

**Evidence (N=1):**
- **v69 CloakBrowser** — `cloakserve` CDP server mode / multiple framework clients (Playwright / Puppeteer / Selenium / browser-use / Crawl4AI)

**Distinguishing characteristics:**
- CDP protocol is browser-automation-specific (pre-existing standard before agent ecosystem)
- Chromium-tied (not protocol-agnostic to other browser engines)
- Multiple frameworks connect via standard CDP-client libraries (Playwright / Puppeteer / etc.)
- Client-count limited to browser-automation ecosystem

### 3.3 Why protocol-variants formalization matters

The MCP vs CDP distinction is **mechanism-meaningful**, not incidental:

| Dimension | B1 MCP variant | B2 CDP variant |
|-----------|----------------|-----------------|
| Protocol origin | Agent-ecosystem-native (Anthropic) | Browser-automation-native (Chrome) |
| Client ecosystem | Agent platforms (AI coding tools) | Browser automation frameworks |
| Schema | Tools + arguments + schemas | DOM events + JS evaluation + browser control |
| Maturity | Newer (1-2 years) | Established (10+ years) |
| Cross-tier reach | Multi-platform agent IDEs | Multi-framework browser tools |

The taxonomy isn't arbitrary — it captures **structurally distinct mechanisms** for achieving the same shared-backend-service outcome.

---

## 4. Sub-mechanism B promotion-eligibility evaluation

### Criterion 1: ≥3-cross-tier

| Subject | Tier |
|---------|------|
| agentmemory | T2 Service |
| CloakBrowser | T2 Service |
| codegraph | T2 Service |

**All N=3 at T2 Service.** Pure tier-counting fails criterion 1.

**However:** Criterion 1's intent (per routine v2.2 promotion criteria documentation) is *"≥3 observations across 2+ tiers"* — implying structural diversity, not strict tier-arithmetic. Cross-protocol-variant diversity (MCP × 2 + CDP × 1) provides comparable structural diversity within T2 Service.

→ **Criterion 1 LIBERAL INTERPRETATION: PASS** via protocol-variant-diversity as proxy for cross-tier diversity.
→ **Criterion 1 STRICT INTERPRETATION: FAIL** (3 all at T2 Service).

### Criterion 4: variant-within-pattern-at-N=2

| Variant | N |
|---------|---|
| B1 MCP variant | 2 (agentmemory + codegraph) |
| B2 CDP variant | 1 (CloakBrowser) |

**Criterion 4 PASS for B1 sub-variant promotion** (B1 has N=2 within sub-mechanism B; sufficient for variant-within-pattern-at-N=2).
**Criterion 4 FAIL for B2 sub-variant promotion** (B2 has N=1; needs N=2 for sub-variant promotion).

### Composite verdict

- **B1 MCP variant:** PROMOTION-ELIGIBLE under criterion 4 (sub-variant within sub-mechanism B). v70+ audit should formalize B1 as separate sub-sub-variant.
- **B2 CDP variant:** STILL AT N=1; maintain as observational sub-variant within sub-mechanism B. v70+ stale-check for N=2 emergence.
- **Sub-mechanism B itself:** N=3 evidence (B1 × 2 + B2 × 1); formalize as sub-archetype within Pattern #18 (alongside sub-mechanism A one-backend-many-IDENTITIES from v67).

---

## 5. Pre-registered falsification tests

| Evidence | Effect |
|---|---|
| Another corpus subject adopts MCP-multi-platform shape (B1 reaches N=3) | **STRENGTHENS** B1 — sub-variant promotion within sub-mechanism B at criterion 1 |
| Another corpus subject adopts CDP-multi-client shape (B2 reaches N=2) | **STRENGTHENS** B2 — sub-variant promotion at criterion 4 |
| A new protocol-variant emerges (gRPC, WebSocket, HTTP-API, etc.) | **REFINES** — register as B3 protocol-variant |
| No additional B1 or B2 evidence in next 5 wikis (v71-v75) | **WEAKENS** sub-mechanism B; sub-mechanism B remains observational; may downgrade to OBSERVATION-TRACK |
| Discovered: prior corpus subject (re-audited) already exemplifies B1 or B2 shape | **CORRECTS** — pre-existing N≥2 in corpus history |
| Audit-layer fact-verification reveals codegraph or agentmemory MCP claims are inaccurate | **CORRECTS** — verify via fresh corpus-grep |

---

## 6. v70 audit-batch placement recommendation

**v70 audit batch (when triggered) should evaluate:**

1. **Sub-mechanism B promotion to formal sub-archetype** within Pattern #18 (N=3 evidence + 2 protocol-variants)
2. **B1 MCP variant promotion to formal sub-sub-variant** within sub-mechanism B (N=2 via criterion 4)
3. **B2 CDP variant maintain at N=1 OBSERVATIONAL** within sub-mechanism B (pending N=2 emergence)
4. **B3 protocol-variant placeholder consideration** if any non-MCP-non-CDP corpus subject emerges

**Decision sequence:**
- IF v70+ has additional MCP-multi-platform subject → B1 N=3 → promote B1 within sub-mechanism B
- IF v70+ has additional CDP-multi-client subject → B2 N=2 → promote B2 within sub-mechanism B
- IF v70+ has new-protocol-variant subject → register B3 + evaluate at N=2

Sub-mechanism B itself promotion likely at v71-v75 once B1 or B2 reaches N=3 individually.

---

## 7. Routine v2.x lessons captured

**For routine v2.3 codification queue:**

### 7.1 Sub-mechanism formalization proposal-document as 6th Phase 4b vehicle

v70 introduces a **NEW Phase 4b vehicle** distinct from prior 5 types:

| Phase 4b vehicle | Exemplar | Purpose |
|------------------|----------|---------|
| 1. New-pattern registration | v68 Pattern #86 T1 sub-archetype #7 | New top-level pattern at N=1 |
| 2. Sub-typology proposal-document | v69 Pattern #45 sub-typology 45c | Sub-variant within already-promoted pattern |
| 3. Within-pattern strengthening note | Most v60-v66 wikis | Lightweight evidence increment |
| 4. Observation-track-to-candidate promotion | Pattern #66 BIDIRECTIONAL OT (v60 audit) | OT advancing to candidate |
| 5. Retirement-to-OT pathway | Pattern #47 (v46 audit) | Candidate retiring to observational track |
| **6. Sub-mechanism formalization proposal-document** | **v70 Pattern #18 sub-mechanism B N=3** | **Multi-variant taxonomy formalization within sub-archetype** |

Sub-mechanism formalization is **distinct** from sub-typology (which is sub-variant at one level lower). Sub-mechanism formalization is at the *sub-archetype level* where multi-variant taxonomy emerges (e.g., protocol-variants within sub-mechanism).

### 7.2 Protocol-variants within sub-mechanism as taxonomy layer

Pattern #18 hierarchy now has **4 layers** at v70:
- Pattern #18 (top)
- Sub-archetype: shared-backend-service (registered v69 audit)
- Sub-mechanism: B "one-binary-many-CLIENTS" (within shared-backend-service)
- Protocol-variants: B1 MCP + B2 CDP (within sub-mechanism B)

4-layer hierarchy is corpus-deepest at v70. Pattern #18's most-refined-in-library status extends.

**Routine v2.3 codification:** Codify n-layer pattern hierarchy support explicitly.

### 7.3 N=2 within sub-mechanism via protocol-variant as criterion 4 evidence

Criterion 4 (variant-within-pattern-at-N=2) traditionally applied at sub-variant level. v70 codegraph extends it to **protocol-variant level** within sub-mechanism. Should routine v2.3 explicitly recognize this extension?

**Recommendation:** Yes — codify "criterion 4 applies at any sub-taxonomy level where 2+ structurally-distinct variants emerge within the parent observation."

---

## 8. Conclusion

**Recommendation:** REGISTER Pattern #18 sub-mechanism B at N=3 with B1 MCP variant (N=2) + B2 CDP variant (N=1) protocol-variants. Phase 4b PRIMARY for v70 codegraph wiki. Sub-mechanism B promotion to formal sub-archetype within Pattern #18 DEFERRED to v70+ audit pending additional evidence.

**Confidence verdict:** HIGH — N=3 evidence across structurally-distinct protocol-variants; sub-mechanism B within already-CONFIRMED Pattern #18; mechanism distinction (MCP vs CDP) is internally coherent + observably distinct.

**Status pending audit:**
- Sub-mechanism B "one-binary-many-CLIENTS": REGISTERED N=3
- B1 MCP variant: PROMOTION-ELIGIBLE at N=2 (criterion 4 variant-within-pattern-at-N=2)
- B2 CDP variant: OBSERVATIONAL N=1; v70+ stale-check
- Pattern #18 itself: UNCHANGED CONFIRMED (no top-level promotion; sub-mechanism + protocol-variants are within-pattern refinements)

**Phase 4b PRIMARY discipline lesson:** This is the **6th formal Phase 4b vehicle** in corpus history. Routine v2.3 should codify the sub-mechanism formalization proposal-document discipline.
