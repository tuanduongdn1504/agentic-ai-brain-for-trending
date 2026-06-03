# (C) claude-for-financial-services — Pattern Library Phase 4b (v141)

**Routine v2.6 · §28 anti-re-accumulation (single registry / ≤2-new-standalones / clustering-first / filing-is-an-act).**

## PRIMARY — 1 NEW Library-vocab standalone (FILED to registry 06 §C)

### "Dual-Deployment-from-One-Source: Interactive Plugin ⇄ Headless Managed-Agents API (same prompt + skills)" — N=1 CORPUS-FIRST
- **What:** One agent definition (`agent.yaml`: system prompt + skills + model config) ships **two interchangeable ways from a single source** — install it as an interactive **Claude Cowork** plugin (UI), or deploy it headless via the **Claude Managed Agents API** (`/v1/agents`) behind your own workflow engine. README: *"Same system prompt, same skills — you choose where it runs."* A `sync-agent-skills.py` propagates the canonical skill into the bundled agents, and `validate.py` drift-checks them, so the interactive and headless forms stay identical.
- **Why it's its own mechanism:** prior corpus plugin/skill subjects target **one** delivery surface (a Cowork/Claude-Code plugin marketplace, v95/v126; or a multi-*harness* skill that's still one interactive surface per harness, Pattern #84 84c). This is the first subject where the **same agent** is a first-class artifact in **both** an interactive-plugin runtime AND a headless-API runtime, with sync tooling guaranteeing parity. The deployment-surface duality (human-in-the-loop ⇄ programmatic) is the novel axis.
- **Distinct from:** Pattern #84 84c multi-harness (same artifact → many *interactive* clients via one protocol); v95 claude-plugins-official (marketplace distribution, single runtime kind); v140 google_workspace_mcp tool-tiers (capability gating, not deployment-surface duality).
- **Promotion-eligibility:** N=2 if a 2nd subject ships the same agent for both interactive-plugin and headless-API deployment from one source. **Stale-watch ~v156.**
- **§28 new-standalone count this ship = 1 (≤ 2).** Registry 06 §C edited (rule-5: filing is an act).

## SECONDARY — instance notes / strengthenings (administrative; NO state change)

- **Phase-0.9 (a)-7 Foundational-Vendor-Direct-Source — N+1 (CONFIRMED sub-axis).** ~5th Anthropic-direct-org subject (v92 claude-for-legal / v93 anthropics-skills / v95 claude-plugins-official / claude-cookbooks / v141). Administrative; (a)-axis ledger, not a Library-vocab standalone.
- **Pattern #84 84c.1 Marketplace-Plugin-Install — N+1 (CONFIRMED N=6).** Cowork plugin marketplace + `claude plugin marketplace add anthropics/financial-services` + `claude plugin install …@claude-for-financial-services`.
- **Pattern #18 sub-mechanism B1 "MCP" — strong N+1 instance.** **11 data-connector MCP integrations** (Daloopa/Morningstar/S&P-Kensho/FactSet/Moody's/MT-Newswires/Aiera/LSEG/PitchBook/Chronograph/Egnyte/Box) — among the densest MCP-connector surfaces in the corpus (MCP cluster v66/v70/v119/v132/v134/v140). Top-level count UNCHANGED.
- **Pattern #81 Manifest-Drift-as-CI-Concern (the GOOD pole) — N+1 instance.** `sync-agent-skills.py` (single-source skill → propagate to bundled agents) + `validate.py` (bundled-skill **drift detection**) + `check.py` (manifest lint + cross-file reference resolution). The *first-class CI* pole anchored at v64 claude-seo — contrast the inverse "names-the-drift-and-drifts-anyway" pole (v66/v113). Clean instance, NOT a promotion.
- **Foundational-Vendor Reference-Impl with Partner-Built Plugins — OBSERVATION (NOT minted).** `plugins/partner-built/{lseg,spglobal}` — partner-authored plugins inside the vendor's own reference repo. Notable governance/ecosystem move; clustering-first, mint only on a 2nd instance.
- **Managed Agents API + Agent-SDK orchestration reference — OBSERVATION.** `orchestrate.py` multi-agent event loop + leaf-worker subagents + steering-events/`handoff_request` routing = a public reference for Anthropic's headless multi-agent deployment. Goal-#1 study material; recorded, not minted (it's the subject's substance, not a cross-subject pattern yet).

## Pattern Library state change: NONE
46 confirmed / ~25 active / 8 Library-vocab CONFIRMED → UNCHANGED. PROVISIONAL standalone surface +1 (dual-deployment-from-one-source). NO top-level Pattern, NO tier sub-archetype, NO confirmed-count movement.

## Audit hand-off note
The ~v139–v140 audit (now overdue) OWES the generate-vector promote-vs-split call (v118/v134/+v137) + the override-frequency 3-in-20 review (v122+v127+v139). v141 does not touch those threads. v141 adds: the dual-deployment standalone (N=1) + the dense-MCP-connector (11) data point + the (a)-7 N+1 to the Anthropic-direct cluster. The MCP-server/MCP-connector B1 line continues to densify (v66/v70/v119/v132/v134/v140 servers + v141's 11 connectors) — flagged again for an MCP-cluster review, NOT minted here.
