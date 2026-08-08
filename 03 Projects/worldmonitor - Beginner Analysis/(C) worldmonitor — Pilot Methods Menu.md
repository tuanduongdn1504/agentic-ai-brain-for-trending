---
title: "(C) worldmonitor — Pilot Methods Menu"
wiki: v230
subject: koala73/worldmonitor
date: 2026-08-08
one_thing_path: "A1 → B5 → (optional) C11"
tags: [llm-wiki, v230, pilot, product-first-mcp, agent-nativity]
---

# (C) worldmonitor — Pilot Methods Menu (v230)

**Blunt framing:** worldmonitor is a genuinely impressive, famous, mature OSINT/geopolitical-intelligence dashboard — but its **domain is off both goals** and **Claude appears nowhere** in it. There is **no product to adopt** into hireui or the Claude/agents practice. The on-goal value is **(1)** the corpus-structural payoff (it's the non-port **N=4** of the palmier-pro v192 product-first-MCP-retrofit §C standalone → the promotion-to-CONFIRMED flag) and **(2)** the **first-party-MCP architecture** as a hireui agent-nativity reference — a 4th data-point beside palmier-pro's `ToolExecutor`, tabularis's read-only-gated MCP, and voicebox's FastMCP-at-`/mcp`. So this is an **honest ~16-method read/borrow/fence menu, NOT a padded 24.**

> ⭐ **One-thing path: A1 → B5 → (optional) C11.** Read the hosted-first-party-MCP + auth design (zero install) → borrow the product-first-MCP-retrofit shape + the header/OAuth auth model into hireui's agent-nativity / first-party-MCP spec → optionally use the free public dashboard/MCP endpoint personally for situational awareness.

---

## A — Read + learn (zero install, on-goal)

- **⭐ A1** Read the **MCP-server design** (`worldmonitor.app/mcp`, Streamable HTTP; public `tools/list`; `tools/call` auth via `X-WorldMonitor-Key` **or** OAuth). It's the 4th first-party-MCP-on-a-product-first-app design you can compare side-by-side (palmier-pro local 51-tool `ToolExecutor` / tabularis local 4-tool read-only-gated / voicebox local FastMCP-4-tool / **worldmonitor hosted, auth-gated**). The **hosted + auth** variant is the new data-point.
- **A2** Read the **multi-surface access design** (one product exposed as web + Tauri desktop + MCP + REST + CLI + Python/Ruby/Go SDKs, all over **Protocol Buffers** contracts — 295 protos / 36 services). A masterclass in "one contract, many surfaces."
- **A3** Read it as the **N=4 corpus data-point** for the v192 standalone — confirm the promotion-to-CONFIRMED case for the next audit (only §C→CONFIRMED promotion, #23, was at N=4).
- **A4** Read the **local-AI-via-Ollama** design (no API keys) as the DeepSeek-TUI v72 / meetily v196 / AIRI v210 privacy-first-inference thread. ⚠️ NOT Claude.

## B — Borrow patterns into the vault / hireui (zero install)

- **⭐ B5** Lift the **product-first-MCP-retrofit shape** into hireui's **agent-nativity / first-party-MCP spec**: a human-usable product whose maker also ships its own first-party MCP server as a secondary agent path. Now a **4-instance reference** (palmier-pro / tabularis / voicebox / worldmonitor) → the design is corroborated, not speculative.
- **B6** Borrow the **MCP auth model** (`X-WorldMonitor-Key` header + OAuth; public `tools/list` but authenticated `tools/call`) into hireui's LLM-integration + api-security ADRs (the api-security thread: public read-metadata vs authenticated action). A clean "safe MCP surface" template.
- **B7** Borrow the **six-variants-from-one-codebase** build pattern (worldmonitor/tech/finance/… from a single base) as a reference if hireui ever needs multi-tenant/vertical builds — but this is a nice-to-have, not core.
- **B8** Note the **Protobuf-contract-first** discipline (typed contracts across every surface) → cross-refs the api-types thread (hireui = REST+OpenAPI typed contracts, not GraphQL); a legible-seam data-point.

## C — Hands-on, scratch / personal (off-goal, fenced)

- **⭐ C11** Use the **free public dashboard** (`worldmonitor.app`) + the **free hosted MCP endpoint** personally for situational awareness — zero install, zero risk. If you want an agent to query it, wire the MCP endpoint into your own Claude Code with a `X-WorldMonitor-Key` (public `tools/list` first). **Never** wire candidate/recruitment data through it (it's an OSINT aggregator).
- **C12** Optionally install-snapshot + `npx worldmonitor tools` in a **scratch dir** to inspect the CLI/MCP tool surface. Treat as untrusted (NOT source-cloned; multi-install-method).
- **C13** Optionally run the **Tauri desktop app** (signed binary) on a scratch machine for a local war-room. Personal-use only.

## D — hireui (borrow ARCHITECTURE only; ⚠️ AGPL + OSINT fences)

- **⭐ D14** Adopt the **first-party-MCP-server pattern** as a design for hireui's own future MCP server (the palmier `ToolExecutor` + tabularis read-only-gated + voicebox FastMCP + worldmonitor hosted-auth references), on an `agent-*` branch, per hireui's CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first; no LLM spend yet → design/spec). worldmonitor's contribution = the **hosted + `X-WorldMonitor-Key`/OAuth auth** variant.
- **D15** ⚠️ Do **NOT** productize worldmonitor's code or fork-and-serve it — **AGPL-3.0 network copyleft** would require open-sourcing hireui. Borrow architecture only.
- **D16** ⚠️ Do **NOT** replicate its OSINT scraping/aggregation of 65+ third-party sources — ToS / copyright / GDPR gray zone; and **never route candidate data through any third-party intelligence aggregator**.

## F — Vault-meta

- **⭐ F17** File the **v192 §C standalone N=3→N=4** update + the **promotion-to-CONFIRMED (#12) doubly-reinforced flag** + the **"web-first/hosted-MCP → generalize the 'Native Application' clause to 'Product-First Application'"** boundary note for the next audit.
- **F18** File the **corpus-first OSINT/geopolitical-intelligence DOMAIN** data-point + the **mainstream-press-coverage** sub-facet (the system_prompts_leaks v205 WaPo shape) + the **first koala73/Elie-Habib/Anghami-lineage author** (#19 19a).

---

## Fence (mandatory)

- **AGPL-3.0** blocks hireui productization — borrow ARCHITECTURE only (the meetily v196 / firecrawl v214 AGPL class).
- **OSINT / dual-use / Palantir-tagged** — a consumer intelligence-aggregation dashboard is a privacy-sensitive, surveillance-adjacent domain. Borrow the **MCP design**, not the surveillance product. **Never** wire candidate/recruitment data through it.
- **NOT source-cloned** → treat all install methods as untrusted-until-inspected; install-snapshot + inspect before `npx`/`npm install`/desktop binaries; pin a commit.
- **hireui** stays hand-built per its CONSTITUTION (I-2 / I-8 / GitNexus-first).
