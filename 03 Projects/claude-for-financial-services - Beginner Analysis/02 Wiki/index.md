# Claude for Financial Services (anthropics/financial-services) — Wiki (v141)

> **One line:** **Anthropic's own production reference implementation of Claude agents** — 10 named agents + 7 vertical plugins + 2 partner plugins + 11 MCP data connectors, deployable two ways from one source (Cowork plugin **or** Managed Agents API).
> **Tier:** T1/T2 — Foundational-Vendor reference implementation (agents + skills + plugins + MCP). **Verdict:** GOAL-ALIGNED INCLUDE 4/4 (a PASS via (a)-7 · b/c/d STRONG).
> **Repo:** `anthropics/financial-services` (official Anthropic org) · Apache-2.0 · Python.
> **§37 provenance:** ≈29.5k★ / 4.1k forks / 231 watchers (as of 2026-06, repo page — *stated, NOT API-verified; env mocks GitHub API*).

## What it is
README opener (verbatim):
> "Reference agents, skills, and data connectors for the financial-services workflows we see most — investment banking, equity research, private equity, and wealth management. Everything here is available **two ways from one source**: install it as a Claude Cowork plugin, or deploy it through the Claude Managed Agents API behind your own workflow engine. Same system prompt, same skills — you choose where it runs."

A modular, fork-and-customize reference for building **production Claude agent systems**. The finance domain is the worked example; the transferable substance is the agent architecture + deployment stack.

## The Anthropic stack it exercises
Claude API · **Managed Agents API** (`/v1/agents`, headless) · **Agent SDK** (multi-agent orchestration) · **Claude Skills** (.md domain modules) · **MCP** (11 connectors) · **Claude Cowork** (plugin install target) · **Claude Code** (CLI plugin mgmt) · MS-365 add-in provisioning.

## Contents
- **`plugins/agent-plugins/`** — 10 named agents: Pitch · Meeting-Prep · Market-Researcher · Earnings-Reviewer · Model-Builder · Valuation-Reviewer · GL-Reconciler · Month-End-Closer · Statement-Auditor · KYC-Screener.
- **`plugins/vertical-plugins/`** — 7 skill+command bundles: financial-analysis (core, `/comps` `/dcf` `/lbo` `/3-statement-model` …) · investment-banking · equity-research · private-equity · wealth-management · fund-admin · operations (30+ slash commands total).
- **`plugins/partner-built/`** — LSEG + S&P Global partner-authored plugins.
- **`managed-agent-cookbooks/`** — Managed Agent templates (one dir/agent).
- **`scripts/`** — `deploy-managed-agent.sh`, `orchestrate.py` (multi-agent event loop), `sync-agent-skills.py`, `validate.py`, `check.py`.
- **`.claude-plugin/`** manifest · **CLAUDE.md** · Apache-2.0.

## Three things worth studying
1. **Dual deployment from one source** — the same `agent.yaml` (system prompt + skills + model config) ships as an interactive **Cowork plugin** *or* a headless **Managed Agents API** deployment, kept in parity by `sync-agent-skills.py` + `validate.py` drift checks. *(Phase 4b PRIMARY — corpus-first Library-vocab N=1.)*
2. **Multi-agent orchestration reference** — `orchestrate.py` event loop + **leaf-worker subagents** + **steering events / `handoff_request` routing**: a public reference for Anthropic's headless multi-agent deployment.
3. **Skill-drift as CI** — single-source skill edits propagate into bundled agents, with drift detection + manifest linting + cross-file reference resolution (Pattern #81 good pole).

## 11 MCP data connectors
Daloopa · Morningstar · S&P Global (Kensho) · FactSet · Moody's · MT Newswires · Aiera · LSEG · PitchBook · Chronograph · Egnyte · Box — one of the densest MCP-connector surfaces in the corpus.

## Install (3 paths)
```
# Cowork: paste repo URL in Settings → Plugins, or upload a plugin zip
# Claude Code (CLI):
claude plugin marketplace add anthropics/financial-services
claude plugin install financial-analysis@claude-for-financial-services
# Managed Agents (headless):
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh gl-reconciler
```

## Disclaimer (from the repo)
Outputs are draft analyst work product staged for human sign-off — the agents do not make investment recommendations, execute transactions, or approve onboarding.

## Corpus connectivity
- **(a)-7 Foundational-Vendor-Direct-Source** — ~5th Anthropic-direct-org subject (v92/v93/v95 + claude-cookbooks).
- **Pattern #84 84c.1 Marketplace-Plugin-Install** (CONFIRMED N=6) · **Pattern #18 B1 MCP** (11 connectors) · **Pattern #81 manifest-drift-as-CI** (good pole).
- See `01 Analysis/` for the full verdict + Phase 4b.

## Pilot note
**Tier-1 READ-pilot for goal #1** (not an operational install). Study `orchestrate.py` + an `agent.yaml` + a `managed-agent-cookbook` to learn Anthropic's Managed-Agents / Agent-SDK deployment architecture — the most authoritative public reference of it. An *operational* trial needs paid financial-data MCP connectors + finance data, so it does NOT join the vault's operational stack; the value is architecture study (the v113 READ-pilot shape).
