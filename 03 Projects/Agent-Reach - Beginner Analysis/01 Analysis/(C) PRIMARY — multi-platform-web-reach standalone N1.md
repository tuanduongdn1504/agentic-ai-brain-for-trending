# (C) PRIMARY — v174 Agent-Reach: "Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents" §C standalone (CORPUS-FIRST, N=1)

**Ship:** v174 · 2026-06-20 · `Panniantong/Agent-Reach`
**Outcome:** 1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1). NO new top-level pattern (max stays #85). NO improper N-bumps. Counts UNCHANGED 46/10. §C surface ≈31 → ≈32.

---

## The standalone

> **"Multi-Platform Web/Social Read+Search Capability Layer for Coding Agents (one unified install bundling per-platform readers/searchers behind ordered primary+fallback backends that auto-switch on failure; zero-paid-API posture)."**

**Anchor:** Agent-Reach v174 (`Panniantong` / Neo Reid).
**Capability:** a single install gives a coding agent **federated read+search reach across 13 heterogeneous external platforms** — open web (Jina Reader) · YouTube (yt-dlp) · RSS (feedparser) · semantic web search (Exa via mcporter, no key) · GitHub (gh) · Twitter/X · B站 · Reddit · Xiaohongshu · LinkedIn · V2EX · Xueqiu · podcasts (Whisper) — where **each platform is abstracted behind an ordered list of primary+fallback backends** with real-time functional detection that **auto-switches on failure** (e.g. yt-dlp→bili-cli when B站 blocks yt-dlp), on a **zero-mandatory-API-fee** posture, framed explicitly as *"a capability layer, not just another tool."*

---

## Why it mints a standalone (and why CORPUS-FIRST)

The corpus has web tools, but none with this shape. The defining axis is the **CONJUNCTION**: (multi-platform federation) × (capability-layer-for-agents) × (ordered primary+fallback routing with auto-switch) × (zero-paid-API free-method posture).

| Neighbor | What it is | Why Agent-Reach is different |
|---|---|---|
| **crawl4ai** (v29) | single LLM-friendly web crawler/scraper library | no per-platform readers (no Twitter/Reddit/YouTube handlers), no ordered fallback lists, no auto-switch — one crawler, not a federation |
| **browser-use** (v42–v47 era) | browser *automation* for agents (fill forms, click) | drives a browser to *act*; Agent-Reach *reads/searches content* — complementary, opposite job |
| **Scrapling** (v149) | undetectable scraping *library* + official agent-tooling (Library-vocab #21) | the *authoring* chain (a library that ships its own skills); Agent-Reach *integrates pre-existing tools* under unified orchestration — different layer/function |
| **google_workspace_mcp** (v140) | MCP server giving an agent reach into **one vendor's** suite | single vendor (Google); Agent-Reach federates **13 heterogeneous** platforms with fallback routing |
| **Jina Reader / Exa** | individual backend providers | **components Agent-Reach incorporates**, not competitors — it is the orchestrator above them |

So the capability — *"one install gives a coding agent federated, auto-failover read+search reach across many heterogeneous external platforms, free"* — is **new to the corpus**: CORPUS-FIRST, N=1.

## Corpus-collision verification (because a verifier hallucinated one)

The corpus-first claim was challenged in verification by an alleged collision with **"v142 claude-web-research."** This was **independently checked and DISMISSED as a confabulation**:
- A grep over all `_state/` chapters found **no** subject named "web-research", "claude-web", or "claude-web-research" anywhere — only the generic *phrase* "web research" inside unrelated entries' prose.
- **v142 is `OrcaSlicer-bambulab`** — a 3D-printing slicer (STRICT Phase-0.9 0/4 → SKIP, 6th lifetime operator override, T5 out-of-scope). Not a web tool.
- Chapter `_state/04` (the cited source) holds only **v30–v39**, so the citation itself is bogus.

The fabrication was **not propagated** into the docs. CORPUS-FIRST N=1 stands on the dedicated collision lens's real grep (Lens 2: CONFIRM, high) **and** the independent grep. (This is the "verify before recommending; never propagate fabrications" discipline working as intended.)

## Secondary observations (NOT minted)

- **#84 84c "Provider-Agnostic-By-Design" — scoped, NO N-bump.** LLM-agnostic; supports Claude Code / OpenClaw / Cursor / Windsurf + any shell agent. Explicitly **NOT** the v168 ponytail "14-platform native-rule-file distribution/generation" mechanism (the v169 build-workflow contamination) — Agent-Reach is a shared layer that *many agents consume*; it distributes *nothing into* the clients. NO N-bump per the v86 discipline.
- **#66 privacy/security — cross-reference.** Local-only `600`-perm creds + no-upload + open-source backends + `--safe`/`--dry-run` + clean uninstall + an explicit "use disposable accounts (封号风险)" warning, for a tool that handles platform cookies.
- **#19 19a — indie-builder portfolio data-point.** `Panniantong` / **Neo Reid** = a disclosed solo-founder ("all employees are AI") with a small public portfolio (Agent-Reach + `xfetch`) — richer than the recent bare-handle authors; a data-point, no new sub-mechanism.
- **#12 LLM-routing-artifacts — INCIDENTAL scoped cross-ref, NO N-bump.** The install writes skill files + MCP config into the agent (per the uninstall) — a side-effect of capability exposure, not the core pattern. #12 is CONFIRMED N=5+ and high-density only when routing/aggregation is the *primary* function (v171/v172); here it is secondary.
- **Adjacencies (NOT members):** multi-backend failover = **data-access** routing (distinct from #18 #8 Multi-Source-LLM-*inference*-aggregator); zero-paid-API = **data-access** economics (distinct from **LV-C2** free/cheap-*inference* economics).

## Explicit NON-claims

- NOT a new top-level pattern (max #85; the §C-standalone tier per §28 — the #86/#88 rejection at v168).
- NOT **#52** — 35.2k★/2.8k forks/v1.5.0/7 releases page-stated, NOT API-verified (§37.4); no API-verified creation date → velocity unestablishable (the high star count notwithstanding).
- NOT **#57** — supports Claude Code/OpenClaw/Cursor/Windsurf as *clients it provisions*, doesn't cite them as influences; mentions ≠ recursion.
- NOT **#18 B1-MCP** — a CLI capability-aggregator that *uses* MCP for some backends, not a single MCP server distributed to many clients.

## Filing

- Registry row added to `_patterns/06-library-vocab-registry.md` §C.
- PROMOTION-ELIGIBLE at N=2 (a 2nd multi-platform federated read+search capability layer for coding agents).
- §28: 1 new standalone (≤2 cap honored). Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).
- Counts UNCHANGED: **46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** §C surface ≈31 → **≈32.**
