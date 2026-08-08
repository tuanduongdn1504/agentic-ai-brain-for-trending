---
title: "(C) worldmonitor — Deep Dive"
wiki: v230
subject: koala73/worldmonitor
author: Elie Habib (koala73)
date: 2026-08-08
tags: [llm-wiki, v230, mcp, osint, geopolitics, dashboard, tauri, agpl, product-first-mcp]
---

# (C) worldmonitor — Deep Dive (v230)

> Source: `https://github.com/koala73/worldmonitor` + raw README + web landscape/identity search. **⚠️ NOT source-cloned** — WebFetch of the rendered repo page + the raw `README.md`, plus WebSearch for identity/landscape (the v200→v229 self-throttle: the ~205K CLAUDE.md shim overflows every subagent > 200K → no deep-dive workflow; all claims hand-verified). Operator-requested ("build LLM wiki for `https://github.com/koala73/worldmonitor`").

## One-line

**World Monitor** = an open-source, real-time **global-intelligence / OSINT situational-awareness dashboard** — "AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface." Its own community framing: *"CNN war room meets Bloomberg Terminal for geopolitics, but accessible to everyone."* It is a **human-usable product first** — but its maker also ships that product's own **first-party MCP server** so any coding agent can call into its intelligence data. That MCP server is the only reason this off-goal subject is in the corpus.

## What it is (source-verified from the repo page + README)

A single codebase that renders a live "war-room" dashboard of the world:

- **News + data aggregation:** 500+ curated news feeds across 15 categories with AI synthesis; **65+ external data sources** (ACLED, UCDP, NASA FIRMS, USGS, USPTO, FRED, IMF, BIS, OFAC, ECMWF, IAEA, WHO, OpenSky, ADS-B Exchange, …). README: *"Aggregates 530+ observed upstream hosts"* with a freshness monitor.
- **Dual map engine:** 3D globe via **globe.gl + Three.js**; WebGL flat map via **deck.gl + MapLibre GL** with **56 layer types**.
- **Cross-stream correlation** across military / economic / disaster signals.
- **Country Instability Index (CII v8)** scoring for **31 Tier-1 countries** (proprietary methodology).
- **Finance radar:** 29 stock exchanges + commodities + crypto.
- **Civil-unrest / protest monitoring, cyber-threat + BGP-anomaly detection.**
- **26 languages** with RTL support.
- **Six site variants from one codebase:** `worldmonitor.app`, `tech.`, `finance.`, `commodity.`, `happy.`, `energy.`
- **Native desktop app (Tauri 2, Rust)** for macOS / Windows / Linux, with a Node.js sidecar; also a PWA.
- **Local AI via Ollama** — "no API keys required."

## The corpus-relevant core — a first-party MCP server (+ REST/CLI/SDKs)

README, verbatim: **"MCP server — `https://worldmonitor.app/mcp` (Streamable HTTP). Public `tools/list`; `tools/call` authenticates with a `X-WorldMonitor-Key` header or OAuth."** And: **"World Monitor is built for agents and scripts as well as browsers."**

Full programmatic-access surface:

- **MCP server** — first-party, built-in, hosted at `worldmonitor.app/mcp` (Streamable HTTP; public `tools/list`; authenticated `tools/call`).
- **REST API.**
- **CLI** — `npm install -g worldmonitor` / `npx worldmonitor tools`.
- **SDKs** — Python (`pip install worldmonitor-sdk`), Ruby (`gem install worldmonitor`), Go (`go get github.com/koala73/worldmonitor/sdk/go`).

⚠️ **No named Claude/Anthropic client.** The AI/ML stack is **Ollama / Groq / OpenRouter / Transformers.js** (browser-side) — no Claude, no Anthropic. The MCP server is **client-agnostic**: "any MCP-aware agent" can call it, but the README names none specifically.

## Tech stack (source-verified)

- **Frontend:** vanilla TypeScript + Vite; globe.gl + Three.js; deck.gl + MapLibre GL.
- **Desktop:** Tauri 2 (Rust) with a Node.js sidecar.
- **AI/ML:** Ollama, Groq, OpenRouter, Transformers.js.
- **API contracts:** Protocol Buffers — **295 protos, 36 services**.
- **Deployment:** Vercel Edge Functions, Railway relay, Tauri, PWA.
- **Caching:** Redis (Upstash), a 3-tier cache, CDN, service worker.

## Author + reception (identity independently verified via WebSearch)

- **Elie Habib** (`koala73`) — **co-founder & CTO/CEO of Anghami** (the Middle East's leading music-streaming service; Nasdaq-listed via SPAC). Lebanese technology executive; named among the **Top 100 Arabs** (2024). World Monitor started as a **weekend side project**.
- Third-party press: **~2 million users across 190+ countries** (Silicon Canals, Arabian Business, Sunday Guardian) — a genuinely famous, mainstream-press-covered project (the system_prompts_leaks v205 "WaPo-covered" sub-facet).
- **NOT Anthropic** (§41 — no name / heritage / locale / notability rescue; famous-OSS-author ≠ (a)-rescue; the disclosed-individual (a)-axis is answered NO). **#19 19a first `koala73` / Elie-Habib / Anghami-lineage author.**

## License, metrics, install

- **License:** **AGPL-3.0-only** for source; *"Commercial use is permitted under the AGPL when you comply with its copyleft and source-availability terms,"* + separate commercial licensing available → **open-core, a hireui-productization blocker** (the meetily v196 / PilotDeck v175 / cortex-hub v181 / firecrawl v214 / OpenMontage v188 AGPL class).
- **Metrics:** **~79.9k ★ / ~11.9k forks / 229 open issues** — **page-stated (§37.4, the mocked GitHub API)** → **NOT a Pattern #52 viral-velocity claim** (a famous side-project → velocity unestablishable; "2M+ users" is third-party-press-stated, not GitHub-star-velocity).
- **Install:** `npm install worldmonitor` / `npx worldmonitor tools`; `pip install worldmonitor-sdk`; `gem install worldmonitor`; `go get …/sdk/go`; desktop binaries (Windows `.exe` / macOS ARM+Intel / Linux AppImage). No `curl|bash` evidenced in the fetched README; no postinstall confirmed (NOT source-cloned → untrusted-until-inspected).
- **Topics/tags:** `agent, ai, dashboard, geopolitics, mcp, mcp-server, monitoring, news, opensource, osint, palantir, situation`.

## Why it's in the corpus (and why it isn't a mint)

The **domain** (OSINT / geopolitical intelligence / news monitoring) is **off both goals** (Goal #1 = master Claude + autonomous agents for software dev; Goal #2 = hireui recruitment SaaS). What lands it inside the corpus is the **first-party MCP server for coding agents** — the exact agent/MCP substrate the vault studies (google_workspace_mcp v140 / palmier-pro v192 / tabularis v212 / OfficeCLI v206 / voicebox v229). It is a **product-first human-usable app whose maker also ships that app's own first-party MCP server** = the **palmier-pro v192 §C standalone** shape, at a new instance (see the Verdict doc). It is **not a mint** — an instance of an already-registered §C class + a corpus-first DOMAIN (domain ≠ a mintable capability class).

## Provenance / caveats (honest)

- **NOT source-cloned** — repo page + raw README + WebSearch only.
- The hard AI is **upstream** (Ollama / Groq / OpenRouter / Transformers.js); World Monitor is an **orchestration / aggregation / UI / MCP layer** — it builds no model.
- The **CII / instability-index methodology is proprietary + unvalidated** (a scored ranking of countries; treat as editorial, not ground truth).
- Metrics page-stated (§37.4); "2M+ users" is third-party-press-stated.
- The domain is **dual-use / privacy-sensitive** — the repo literally tags `palantir`; an OSINT/intelligence-aggregation dashboard is a surveillance-adjacent product (see the Verdict + Pilot fences).
