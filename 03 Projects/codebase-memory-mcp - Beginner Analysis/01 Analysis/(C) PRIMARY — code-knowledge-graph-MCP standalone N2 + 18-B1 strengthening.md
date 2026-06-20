# (C) PRIMARY — Code Knowledge-Graph MCP standalone (N=2) + Pattern #18 B1-MCP variant strengthening (N≈9)

**Ship:** v172 codebase-memory-mcp · 2026-06-20 · routine v2.6 (§31 two-tier INCLUDE / §28 anti-inflation / §37 provenance)

This is the PRIMARY Phase-4b deliverable: the Pattern-Library reasoning, written out so the next audit can act on it without re-deriving.

---

## 1. The claim

**MINT 1 NEW Library-vocab §C standalone (NOT corpus-first, N=2):**

> **"Pre-Indexed Read-Only Code Knowledge-Graph Queried by Coding Agents via MCP (SQLite + Cypher + LSP; token-reduction; 100% local)."**
> **N=2** · Anchors: **codegraph v70** (`@colbymchenry`) + **codebase-memory-mcp v172** (`@DeusData`) · **PROMOTION-ELIGIBLE at N=3.**

**PLUS — clean Pattern #18 sub-archetype B / B1-MCP variant instance-strengthening → N≈9** (separate axis; no double-count; pure strengthening, NOT a promotion).

---

## 2. Why N=2 and not N=1 corpus-first, and not "re-register OC-K"

This was the one point the v172 adversarial verification (3 lenses + critic) had to adjudicate. Three candidate framings were on the table:

| Framing | Verdict | Why |
|---|---|---|
| **Fresh corpus-first N=1** (the v158/v165/v171 shape) | ❌ REJECTED | Would erase codegraph v70's priority. v70 *already* shipped "pre-indexed code knowledge graph for AI coding agents." The capability is demonstrably **not** new to the corpus. |
| **"RE-REGISTER OC-K at N=2"** (one lens proposed this) | ❌ REJECTED (critic AMEND) | **OC-K was never in the Library-vocab registry.** It was a v70-era observational candidate ("Pre-Indexed-Context-Layer as agent augmentation strategy, N=1") that, like ~108 other per-wiki "NEW candidate" mentions, was **never carried into the registry** — exactly the "phantom count" the v2.4 consolidation cleaned up. There is nothing to *re*-register. |
| **MINT NEW §C standalone at N=2** | ✅ ADOPTED | Honest on both counts: (1) it is a *new* registry entry (the capability has no slot today), and (2) it enters at **N=2** because there is a clean, documented prior instance (codegraph v70) whose priority must be credited. |

**The discipline:** §C standalones *can* be filed at N=2 when a 2nd clean cross-author instance appears — precedent: **"voice-calibration personalization" re-registered at N=2 at v138** after its v108 N=1 had gone stale. The same logic applies here, except codegraph v70's instance was never registered at all (so this is a first registration that simply enters at N=2 rather than N=1).

**Cross-author + cross-implementation check (PASS):** codegraph v70 = `@colbymchenry`, a Node/npm package, tree-sitter → SQLite **FTS5** → symbol/edge graph, 8 MCP tools, 4 agent platforms, 19 langs. codebase-memory-mcp v172 = `DeusData` org, a **C/C++ single static binary**, tree-sitter + **hybrid LSP** → SQLite graph + **read-only Cypher** + Louvain communities, 14 MCP tools, **11** agent platforms, **158** langs. Same *capability* (agent queries a pre-built read-only code graph instead of reading files; both pitch token/tool-call reduction; both 100% local), genuinely different *authors and implementations*. A clean N=2.

## 3. The scope line — capability vs distribution structure (no double-count)

The standalone captures **ONE axis only: the capability** — "a coding agent queries a pre-indexed, read-only graph of the codebase via MCP."

It does **not** capture *how the server reaches many agents*. That is a **separate axis** — **Pattern #18 sub-archetype B / B1-MCP variant** ("one server, many MCP clients") — and codebase-memory-mcp strengthens it cleanly:

- **#18 sub-archetype B is FORMAL since the v72 audit** (it was promoted from a within-pattern sub-mechanism to a formal sub-archetype, with protocol-variants B1 MCP / B2 CDP). Its **B1-MCP variant was N-reconciled to N=7 at the v151 audit:** agentmemory v66 + codegraph v70 + nature-skills v119 + supermemory v132 + google_workspace_mcp v140 + financial-services v141 + Scrapling v149.
- **+ devspace v171** (logged loosely as "N+1", not tallied) **+ codebase-memory-mcp v172** → **N≈9.** codebase-memory-mcp's 11-client auto-detect + auto-config + instruction-injection + pre-tool-hooks is *textbook* one-server-many-MCP-clients. (Exact post-v151 tally is an audit bookkeeping item — the v151 "filing is an act, not a claim" note means each ship's "B1 N+1" should be tallied at audit.)

Keeping these on separate axes is the **v140 / v171 precedent** (v140 google_workspace_mcp = a §C capability standalone *and* a #18 B1 instance; v171 devspace = a §C capability standalone *and* a #18 B1-MCP instance). The capability and the distribution structure are orthogonal — recording both is not double-counting.

**⚠️ Correction vs the loose v171 framing (do NOT repeat it):** an earlier draft of this verdict called this "the long-deferred sub-mechanism-B → formal-sub-archetype promotion, now a clean N=4." That is wrong on two counts: (1) sub-archetype B was **already promoted at v72** — it is not pending; (2) the v151 audit **DECLINED** splitting B1-MCP into its own sub-archetype ("B1 already captures the shape; minting would relabel, not add content" — anti-inflation). So v172 is **pure instance-strengthening of an existing formal sub-archetype, NOT a promotion event.** The only genuinely-open #18 item is the routine post-v151 B1-MCP **N reconcile** (now ≈9); the stale "Pattern #18 sub-mechanism B promotion deferred" line in the v167 audit / v171 shim should be **struck** at the next audit.

## 4. Secondary observations (recorded, NOT minted)

- **Pattern #84 84c "Provider-Agnostic-By-Design" — scoped observation, NO N-bump.** 11-agent auto-config = provider-agnostic. But per the v86 audit discipline, "most platforms yet / a single new count-increment" is not a CORPUS-RECORD mint. Scoped note only. **Guard:** this is NOT the ponytail "14-platform native-rule-file distribution" mechanism (that contamination was caught + rejected at v169) — codebase-memory-mcp distributes *one MCP server* to many clients (= #18 B1-MCP), it does not author native rule files per platform.
- **Pattern #66 (supply-chain) — cross-reference, NO N-bump.** SLSA-L3 + keyless Sigstore cosign + VirusTotal 0/72 + SHA-256 + CodeQL SAST + 100%-local = an unusually mature posture for an installable agent tool (relevant precisely because the install vector is `curl | bash` of a compiled binary). Cross-referenced.
- **Library-vocab #20 "Token-Economy-Quantification" — QUALIFIED-ADJACENT, N stays 4.** The 99.2% / 412k→3.4k claim is a genuine token-economy quantification (runtime/data-structure footprint axis), but it is a **single 5-query micro-scenario, page-stated, unreplicated** → defer the N-bump to audit, per the **v168 ponytail precedent**. Not an N=5 at ship.
- **Pattern #19 19a — minimal data-point.** "DeusData" org, no disclosed individual/portfolio. Thin data-point, no sub-mechanism.

## 5. Explicit NON-claims

- **NOT a new top-level pattern** (max stays #85; §28 anti-inflation, the #86/#88 rejection at v168).
- **NOT #52** (page-stated stars/forks/releases, no API-verified creation date, §37.4 → velocity unestablishable; kin codegraph v70 was sub-threshold at ~42★/day).
- **NOT #57** (lists corpus subjects as *integration targets it augments* — OpenCode/OpenClaw/Codex — not as *influences it cites*; mentions ≠ recursion, the v171 discipline).
- **NOT a re-classification / new tier.**

## 6. Net state change

| Field | Before (post-v171) | After (post-v172) |
|---|---|---|
| Confirmed top-level patterns | 46 | **46 (UNCHANGED)** |
| CONFIRMED Library-vocab | 10 | **10 (UNCHANGED)** |
| Tracked PROVISIONAL §C surface | ≈29 | **≈30** (+1 standalone, N=2) |
| Pattern #18 B1-MCP variant | N=7 (v151 reconcile) | **N≈9** (+devspace v171 +this) |
| Library-vocab #20 | N=4 | **N=4** (QUALIFIED-ADJACENT; bump deferred) |
| Streak | GA:33 · OG:11 [7 ov] | **GA:34 · OG:11 [7 ov]** |
| §35 ceiling | clear | **clear** (window {v170,v171,v172} = 0 OG) |
| Consecutive goal-aligned ships | 18 (v153→v171) | **19 (v153→v172)** |

**Promotion-eligibility opened by v172:** (1) the new §C standalone → CONFIRMED at a genuine N=3. **NOT opened:** Pattern #18 sub-archetype B is already formal (v72) and the B1-MCP→own-sub-archetype split was declined at v151 — v172 is pure instance-strengthening (N≈9), not a promotion; the only #18 chore is the routine post-v151 B1-MCP N reconcile + striking the stale "promotion deferred" line.
