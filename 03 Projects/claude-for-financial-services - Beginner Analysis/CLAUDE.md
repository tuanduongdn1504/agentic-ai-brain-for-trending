# claude-for-financial-services — Beginner Analysis (project CLAUDE.md)

**Subject:** `anthropics/financial-services` ("Claude for Financial Services"), v141 wiki ship, 2026-06-03.
**Verdict:** GOAL-ALIGNED INCLUDE 4/4 — (a) PASS [(a)-7 Foundational-Vendor-Direct-Source] · (b) STRONG · (c) STRONG · (d) STRONG.
**Tier:** T1/T2 — Foundational-Vendor reference implementation. **Routine:** v2.6 (§31/§35/§37).

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis STRICT verdict + §35 + §37 + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY (1 new Library-vocab standalone, filed) + administrative N+1 strengthenings; NO state change.
- `02 Wiki/index.md` — the knowledge page.

## One-paragraph summary
Anthropic's official **production reference implementation of Claude agents** for financial services — 10 named agents + 7 vertical plugins + 2 partner-built plugins (LSEG, S&P Global) + 11 MCP data connectors. Distinctive: the **same agent deploys two ways from one source** (interactive Cowork plugin ⇄ headless Managed Agents API, parity-checked by `sync-agent-skills.py`/`validate.py`); a documented multi-agent `orchestrate.py` loop with leaf-worker subagents + `handoff_request` steering. Apache-2.0, Python. The finance *domain* is the worked example; the goal-#1 value is the **agent architecture + Managed-Agents/Agent-SDK deployment** reference.

## Phase 4b headline
PRIMARY = NEW Library-vocab standalone **"Dual-Deployment-from-One-Source: Interactive Plugin ⇄ Headless Managed-Agents API"** N=1 CORPUS-FIRST (filed registry 06 §C). Administrative N+1: (a)-7 (~5th Anthropic-direct) · Pattern #84 84c.1 (N=6) · Pattern #18 B1 MCP (11 connectors) · Pattern #81 manifest-drift-CI (good pole). NO Pattern Library state change (46/8).

## §35 / streak
§35 STAYS CLEAR (window {v139 OG, v140 GA, v141 GA} = 1 OG ≤ 1; the two aBaiAutoplus declines were refusals, not ships). Streak GA:9·OG:5 [2 ov] → **GA:10·OG:5 [2 ov]**.

## Provenance caveat (§37)
≈29.5k★ / 4.1k forks **stated from the repo page, NOT API-verified** (env mocks the GitHub API). Owner = anthropics official org (stated). NOT a #52 claim.

## Pilot
**Tier-1 READ-pilot** (architecture study of Managed-Agents/Agent-SDK), NOT an operational install (needs paid financial-data MCP connectors). v113 shape.

Shipped on branch `wiki/v141-anthropic-financial-services`, stacked on the unmerged v140 branch, off main per the 2026-06-02 convention. Not auto-merged.
