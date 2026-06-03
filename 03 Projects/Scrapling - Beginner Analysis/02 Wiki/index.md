# Scrapling — Wiki (v149)

> **One line:** **"An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl"** — a high-performance Python scraping library that *also ships a built-in MCP server + an official agent-skill* so AI agents (Claude/Cursor) can drive it to fetch and extract web content.
> **Tier:** T2 Service (adaptive web-scraping framework + bundled MCP server + official agent-skill). **Verdict:** GOAL-ALIGNED INCLUDE 3/4 (a FAIL · b/c/d STRONG).
> **Repo:** `D4Vinci/Scrapling` · BSD-3-Clause · Python 99.9% · author Karim Shoair (D4Vinci).
> **§37 provenance:** ≈59.4k★ / 5.7k forks / 226 watchers / v0.4.8 (May 11 2026) / 1,447 commits (page-stated as of 2026-06 — *NOT independently API-verified; this env mocks the GitHub API §37.4*). Created ~late-2024 (project's public history; not verified here) → velocity unestablished → **NOT a Pattern #52 claim.**

## Why it's in the corpus (the load-bearing part)
On its face Scrapling is a web-scraping library — a domain that, alone, is off goal #1. **What makes it goal-aligned is the direction of its relationship to agents:** it ships a *built-in MCP server* and an *official agent-skill* so that an AI coding agent can USE Scrapling. That's the v140/v143 shape (a capability exposed **to** agents), not the v123 shape (an app that merely calls an LLM internally).

README, verbatim:
> "🤖 **MCP Server to be used with AI**: Built-in MCP server for AI-assisted Web Scraping and data extraction. The MCP server features powerful, custom capabilities that leverage Scrapling to extract targeted content before passing it to the AI (Claude/Cursor/etc)."

- **MCP server** is a *shipped, first-class* feature: `pip install "scrapling[ai]"` installs it now (v0.4.8), with a demo. **Not roadmap** (the v146 OpenCut distinction) and **not internal dev-exhaust** (the v122/v142 distinction).
- **Official agent-skill** for its own product: an `/agent-skill` directory in the repo + an **"OpenClaw Skill"** badge → `clawhub.ai/D4Vinci/scrapling-official`. The vendor ships an official agent-skill teaching agents to use its own library — the v114 gsap / v126 Every shape.

For someone mastering "autonomous agents for software development," a stealth-capable web-data-extraction MCP is a genuinely useful agent capability (agents constantly need to read pages/docs/data). It is also directly relevant to *this vault's own research/ingestion step* — the `WebFetch`/`WebSearch` used to build this very wiki is a thin version of what Scrapling's MCP does more robustly.

## What the library itself is
| Layer | What |
|---|---|
| **Fetcher** | plain HTTP requests |
| **DynamicFetcher** | browser-driven / JS-rendered pages |
| **StealthyFetcher** | anti-bot bypass — `--impersonate`, `--solve-cloudflare`, `--no-headless` |
| **Spider framework** | Scrapy-like: concurrent crawling, multi-session, pause/resume, streaming |
| **Adaptive parsing** | "self-healing" — relocates elements after a site's markup changes |
| **Selection** | CSS · XPath · filter-based · text/regex |

Claims to outperform BeautifulSoup/Selenium; full type coverage (PyRight + MyPy). **BSD-3-Clause**, Python 99.9% (+ Dockerfile).

## CLI + surfaces
```
scrapling shell                       # interactive web-scraping REPL
scrapling extract get <url> <file>
scrapling extract fetch <url> <file>
scrapling extract stealthy-fetch <url> <file>   # --css-selector --impersonate --no-headless --solve-cloudflare
```
Install: `pip install scrapling` → extras `[fetchers]` / `[ai]` (MCP server) / `[shell]` / `[all]`; browsers via `scrapling install`; Docker `pyd4vinci/scrapling`. Multilingual READMEs: **AR / RU / CN / JP** (the Arabic README is the main signal for the author's MENA/Arabic-speaking profile).

## Corpus connectivity
- **LV-C1 Vendor-Official Agent-Tooling for Own Product → N=3** (v114 gsap library-vendor + v126 Every methodology-vendor + **v149 Scrapling library-vendor**). Scrapling is a clean structural twin of v114 (both software-library vendors shipping official agent-tooling for their own library) → the **library-vendor sub-type is now N=2** (v114+v149), and LV-C1 reaches **promotion-eligible N=3**. **PRIMARY** — see `01 Analysis/(C) Pattern-Library-Phase-4b.md`.
- **Pattern #18 B1 MCP** (one-binary-many-CLIENTS) — N+1. The MCP-server B1 line is now dense (v66/v70/v119/v132/v134/v140/v141/v144/v149) → an "MCP-server" tier-sub-archetype review is overdue (audit, not minted here).
- **Pattern #84 multi-harness / agent-tooling** — N+1 (MCP + agent-skill across Claude/Cursor/OpenClaw).
- **OpenClaw / clawhub.ai = a parallel agent-skill registry** (sibling-standard to agentskills.io) — observation, like the v121 CodexKit Codex-native note. **NOT asserted as a 57k `npx skills add` agentskills.io implementer** (the `/agent-skill` dir may or may not be an agentskills.io `SKILL.md`; flagged as a candidate for the chain reconciliation, not claimed).
- **productivity/data agent-connectivity** — sits near v140 google_workspace_mcp + v144 headroom (capability-providers for agents).

## §35 — Soft Off-Goal-Rate Ceiling
**CLEARS the breach.** Before v149 the window {v146 OG, v147 GA, v148 OG} = 2 OG was BREACHED (v148 = 2nd consecutive `[ceiling-override]`). A GOAL-ALIGNED v149 scrolls v146 out → window {v147 GA, v148 OG, v149 GA} = **1 OG ≤ 1 → CLEAR.** v149 is NOT an override; override-frequency triggers UNCHANGED (lifetime 9).

## Pilot note — Tier-1, genuinely
A real pilot for THIS vault. The Scrapling MCP would let the agent fetch + extract web content during research/ingestion more robustly than the built-in `WebFetch`. Lowest-friction, reversible: `pip install "scrapling[ai]"` → `scrapling install` (browser binaries) → register the MCP with Claude → trial a `stealthy-fetch`/extract on a real page. **`install-snapshot` recommended** (pip + a `scrapling install` browser-download step). Even a READ of its adaptive/self-healing selector design + stealth-fetch tiers is worth borrowing as ideas.

## Honest non-claims
- (a) genuinely FAILS — Karim Shoair is MENA/Arabic-speaking inferred (README_AR) but undeclared; **not** a registered cultural-peer axis, **not** (a)-7; no axis minted for a single subject (the v139 North-African / v97→v115 (a)-8 discipline).
- (b) STRONG-**not**-STRONGEST — the core product is a general-purpose scraping library; the agent surface (MCP + skill) is one delivery mode, so it's a capability-provider/connector, not the agent substrate. **Flagged for the next audit to challenge** the dual nature (scraping library vs agent tooling).
- Metrics are page-stated, NOT API-verified; **NOT a #52 claim** (velocity/age unestablished here).
- Phase 4b: **0** new standalones + **1** cluster strengthening (LV-C1 → N=3); NO new top-level Pattern, NO tier sub-archetype, NO confirmed-count change.
