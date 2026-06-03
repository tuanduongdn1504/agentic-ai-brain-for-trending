# google_workspace_mcp — Beginner Analysis (project CLAUDE.md)

**Subject:** `taylorwilsdon/google_workspace_mcp` (v140 wiki ship, 2026-06-03).
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG.
**Tier:** T2 Service (MCP integration server). **Routine:** v2.6 (§31/§35/§37).

## Folder map
- `01 Analysis/(C) Phase-0-and-0.9-verdict.md` — scope gate + 4-axis STRICT verdict + §35 + §37 provenance + honest non-claims.
- `01 Analysis/(C) Pattern-Library-Phase-4b.md` — PRIMARY (1 new Library-vocab standalone, filed) + secondary observations; NO state change.
- `02 Wiki/index.md` — the knowledge page (what it is, architecture, the 3 study points, install, corpus connectivity, pilot note).

## One-paragraph summary
A jlowin-FastMCP-based **MCP server** exposing **12 Google Workspace services** (Gmail/Drive/Calendar/Docs/Sheets/Slides/Forms/Chat/Apps Script/Tasks/Contacts/Search) as 50+ tools to any MCP client. Distinctive engineering: **graduated tool tiers** (`--tool-tier core|extended|complete`, least-privilege), **OAuth that scales** (2.0 PKCE → 2.1 multi-user bearer tokens → service-account delegation → stateless no-disk container mode), and **3 transports** (stdio / streamable-HTTP / reverse-proxy). MIT, Python 3.10+. Ships an optional Claude skill for Workspace tool-routing.

## Phase 4b headline
PRIMARY = NEW Library-vocab standalone **"Graduated / Least-Privilege Tool-Exposure for a Large-Surface MCP Server"** N=1 CORPUS-FIRST (filed to registry 06 §C). Strong **Pattern #18 B1 MCP** N+1. NO Pattern Library state change (46/8).

## §35 / streak
§35 STAYS CLEAR (window {v138 GA, v139 OG, v140 GA} = 1 OG ≤ 1). Streak GA:8·OG:5 [2 ov] → **GA:9·OG:5 [2 ov]**.

## Provenance caveat (§37)
All star/fork/date metrics are **stated from the repo page, NOT API-verified** — this environment mocks the GitHub API. Author location US-presumed (speculation/medium, undeclared).

Shipped on branch `wiki/v140-google-workspace-mcp` off main per the 2026-06-02 branch convention. Not auto-merged.
