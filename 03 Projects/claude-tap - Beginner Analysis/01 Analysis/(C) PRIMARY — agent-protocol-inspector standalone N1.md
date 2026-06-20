# (C) PRIMARY — v173 claude-tap: "Agent Protocol Inspector" §C standalone (CORPUS-FIRST, N=1)

**Ship:** v173 · 2026-06-20 · `liaohch3/claude-tap`
**Outcome:** 1 NEW Library-vocab §C standalone (CORPUS-FIRST, N=1). NO new top-level pattern (max stays #85). NO observability-sub-archetype N-bump (adjacency only). Counts UNCHANGED 46/10. §C surface ≈30 → ≈31.

---

## The standalone

> **"Agent Protocol Inspector (local man-in-the-middle capture + trace-viewer of an AI coding agent's live API traffic, for debugging)."**

*(Renamed on the v173 critic AMEND from the drafted "API-Traffic Interceptor / Trace-Viewer (protocol-inspection proxy) for AI Coding Agents" — the new name leads with the protocol-layer distinction that justifies the mint over an observability-instance reading. Old name retained as a search alias.)*

**Anchor:** claude-tap v173 (`liaohch3`).
**Capability:** a local man-in-the-middle PROXY you run an agent CLI *through*; it records the agent's LIVE API request/response payloads (system prompts, tool schemas, conversation, tool calls/results, reconstructed SSE streaming responses, token usage) and renders them in a self-contained HTML trace-viewer for **debugging by evidence** (structural diff between consecutive requests with character-level highlighting; full-text search; path filter; tool-schema inspector; HTML/JSONL export). Dual reverse/forward proxy modes tap 14 agent CLIs; 100% local; auth headers auto-redacted before recording.

---

## Why it mints a standalone (and why CORPUS-FIRST)

The corpus has tools that **watch an agent** and a few that **sit in the traffic path**, but none that does this exact thing:

| Neighbor | Layer | What it does | Why claude-tap is different |
|---|---|---|---|
| Observability sub-archetype (`02b`, N≈12): metering (v89/v109/v157/v158/v165) · ambient-pet (v154/v155/v156/v164/v166) · attention (v160) | logs / state / hooks | READS + DISPLAYS agent state/usage | claude-tap reads the **network wire** (raw API payloads), to **debug the protocol** — not metrics/status |
| headroom v144 | wire / proxy | INTERCEPTS the read-path to **COMPRESS** (reversible CCR) | same proxy position, **opposite purpose** — transform/shrink, not record/inspect |
| relay/reseller proxies v112 / v117 | wire | **REDIRECT** traffic to cheaper endpoints | relay for cost, not capture for inspection |
| lazyagent v165 | stored files | prune/compact/search ALREADY-STORED session files | different layer (stored files, not live wire) |

So the capability — *"a local man-in-the-middle proxy records + renders an agent's live API protocol traffic for inspection/debugging"* — is **new to the corpus**: CORPUS-FIRST, N=1.

## The load-bearing distinction (anti-"generalize-to-fit")

claude-tap *touches* the observability family (you are broadly "watching the agent"), so the tempting move is to file it as an observability sub-archetype instance and bump that N. That would be the **"generalize-the-definition-to-fit-the-2nd-instance" error** the audits repeatedly warn against. It differs on all three defining axes:

- **LAYER:** network wire (a proxy) vs logs / state files / hooks.
- **OBJECT:** raw API payloads (system prompts, tool schemas, SSE streams) vs usage metrics / run-state.
- **PURPOSE:** debug / reverse-engineer the protocol vs monitor usage / show status.

→ Recorded as an **ADJACENCY CROSS-REFERENCE** to the observability sub-archetype, **NOT an instance**, **NO N-bump.** (This is exactly the call the 3-lens + critic workflow independently confirmed; the critic's `inflation_check` = discipline HELD.)

## Secondary observations (NOT minted)

- **#84 84c "Provider-Agnostic-By-Design" — scoped, NO N-bump.** One proxy taps 14 CLIs via dual reverse/forward modes = PROTOCOL-level multi-client interception. Explicitly **NOT** the v168 ponytail "14-platform native-rule-file distribution/generation" mechanism (the v169 build-workflow contamination) — claude-tap distributes *nothing into* the clients. NO N-bump per the v86 "single-increment ≠ CORPUS-RECORD" discipline.
- **#66 privacy/security — cross-reference.** 100%-local + no hosted dashboard + auth-header auto-redaction before recording, for a tool that by design sits in the API-key path.
- **#19 19a — thin data-point.** Bare handle, no disclosed individual / portfolio.
- **LV-C4 cadence — page-stated note.** 100+ releases to v0.1.120; page-stated, not API-verified (§37.4).

## Explicit NON-claims

- NOT a new top-level pattern (max #85; the §C-standalone tier per §28 — the #86/#88 rejection at v168).
- NOT an observability-sub-archetype instance (adjacency only).
- NOT **#18 B1-MCP** — a proxy you run the CLI through, not an MCP server.
- NOT **#52** — ~1.9k★/196 forks/100+ releases/v0.1.120 page-stated, NOT API-verified (§37.4); no API-verified creation date → velocity unestablishable.
- NOT **#57** — taps corpus subjects (Claude Code/Codex/Gemini/OpenCode/OpenClaw/Pi) as *clients*, doesn't cite them as influences; Phistory (`WEIFENG2333/phistory`) is a downstream dependent, not upstream recursion.
- System-prompt capture is incidental — claude-tap is the live-capture *mechanism* behind static prompt collections (v65 claude-code-system-prompts / system-prompts-leaks), not a curated collection itself.

## Filing

- Registry row added to `_patterns/06-library-vocab-registry.md` §C.
- PROMOTION-ELIGIBLE at N=2 (a 2nd protocol-inspection / trace-viewer proxy for coding agents).
- §28: 1 new standalone (≤2 cap honored). Time-aware stale-watch ≥15 wikis AND ≥30 days (§39).
- Counts UNCHANGED: **46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** §C surface ≈30 → **≈31.**
