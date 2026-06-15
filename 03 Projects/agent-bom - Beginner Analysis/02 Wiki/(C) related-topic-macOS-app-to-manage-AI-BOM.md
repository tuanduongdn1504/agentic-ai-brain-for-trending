# (C) Related topic — "a macOS app to manage an AI Bill of Materials" (v157, agent-bom lens)

> **Operator-requested related topic** (same ask as v156). **Headline finding is unchanged: there is no dedicated native macOS app to manage AI-BOMs** (as of 2026-06). The full landscape + standards lineage + gap analysis is in the v156 page — [`03 Projects/ai-bom - Beginner Analysis/02 Wiki/(C) related-topic-macOS-app-to-manage-AI-BOM.md`](../../ai-bom%20-%20Beginner%20Analysis/02%20Wiki/(C)%20related-topic-macOS-app-to-manage-AI-BOM.md). This page records only what **agent-bom** adds to that picture.

> **↪ See also — broader landscape + ranking:** [`00 Notes/(C) AIBOM-tool-landscape.md`](../../../../00%20Notes/(C)%20AIBOM-tool-landscape.md) — a verified ranking of ~10 AIBOM tools + the definitive macOS-app verdict (still none) + a best-Mac-front-end-substrate ranking, **where agent-bom ranks #1 as a wrap-target** (63-tool MCP server + REST). Built 2026-06-05 from a 20-repo verification sweep (74 candidates).

## What agent-bom changes about the "manage on macOS" answer
agent-bom is a **more complete "control plane"** than v156 ai-bom, but it is **still not a native macOS app** — it manages AI-BOM via:
1. **CLI** — `pip install agent-bom` → `agent-bom agents -p . -f html -o report.html` (runs natively on macOS, Python).
2. **Self-hosted dashboard** — `agent-bom serve` → a **web** dashboard (inventory / findings / graph cockpit / compliance evidence). Closest thing to a "manage" GUI; web, not native.
3. **REST API + Python/TS clients** — programmatic management.
4. **MCP server** — `agent-bom mcp server` (63 tools) → you "manage" the AI-BOM **through your agent** (Claude Code / any MCP client), which is a genuinely different management modality than a GUI.
5. **Runtime proxy/gateway** — live MCP-traffic policy enforcement (server-side, not a Mac app).
6. Docker / Helm / EKS / Postgres — server/cluster deployments.

So agent-bom widens the *non-native* surface (web dashboard + REST + MCP + gateway) but the **native-macOS gap is identical to v156**: no `.app`, no menu-bar/tray manager, no Mac App Store entry.

## Updated landscape note
The space is still **OSS CLIs + commercial web platforms**, now with **two independent OSS AI-BOM scanners** in the corpus:
- **Trusera/ai-bom** (v156) — scanner → SBOM; CLI + Flask dashboard; the OSS foundation of a commercial platform.
- **msaad00/agent-bom** (v157) — scanner **+ control plane** (REST + 63-tool MCP server + dashboard + runtime gateway + blast-radius graph); solo, self-hosted-first.
- + commercial web platforms: Mend / Snyk / JFrog / Wiz / Cycode / Sysdig / Palo Alto; + Cisco AI Defense OSS (`cisco-ai-defense/aibom`).
**None native to macOS.**

## The gap (corpus connection) — unchanged
A genuine **native macOS AI-BOM manager** still doesn't exist. agent-bom *sharpens* what one would wrap: its **MCP server** means a Mac menu-bar app could surface "AI components + blast-radius + new high-risk findings" by calling agent-bom's 63 MCP tools (rather than shelling the CLI). That would be the **governance-layer analog** of the corpus's v153 Tauri / v154 Swift / v155 Electron native-desktop management surfaces — a real, still-unfilled opportunity.

## Honest caveats
- **No such macOS app exists** — gap/landscape analysis, not a product wiki (flagged).
- agent-bom's "dashboard" is a **web** dashboard (`agent-bom serve`), not a native macOS GUI — do not overstate it.
- Landscape facts as of 2026-06, NOT API-verified; vendor capabilities change.

## Sources
- [msaad00/agent-bom](https://github.com/msaad00/agent-bom) · [agent-bom on Glama (MCP registry)](https://glama.ai/mcp/servers/@msaad00/agent-bom) · [agent-bom OpenClaw skill (playbooks)](https://playbooks.com/skills/openclaw/skills/agent-bom)
- [Trusera/ai-bom](https://github.com/Trusera/ai-bom) · [cisco-ai-defense/aibom](https://github.com/cisco-ai-defense/aibom)
- Full AI-BOM concept + standards + commercial-landscape sources: see the v156 related-topic page (Wiz / Cycode / Snyk / JFrog / Sysdig / Mend / Palo Alto / Cisco).
