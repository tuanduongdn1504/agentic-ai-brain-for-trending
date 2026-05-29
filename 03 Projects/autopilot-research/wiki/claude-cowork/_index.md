# claude-cowork

> Anthropic's scheduled-agent / "AI employee" desktop product. Distinct from Claude Code (CLI for developers) — Cowork ships natural-language scheduling + skills + MCP + sub-agents in a non-technical desktop UI. Rebranded from earlier Claude Code packaging per Jack Roberts.

**Drained:** 2026-05-29 (autopilot loop)
**Raw source:** [`raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md`](../../raw/2026-05-29-claude-cowork-anthropic-scheduled-agent-feature.md)
**NotebookLM notebook:** `f851b538-c0cb-405f-9a8b-c46837464930`
**Sources:** 6 YouTube videos (1 anchor + 5 yt-search picks), Feb–May 2026

## Articles

- [[overview]] — what Claude Cowork is, Cowork-vs-Code-vs-Chat taxonomy disagreements, pricing positioning
- [[contextual-engineering]] — persistent `.md` "brain" file patterns (minimalist vs specialist vs automated)
- [[sandboxing-and-workspace-structure]] — dedicated workspace folder + permission discipline + the irreversibility caveat
- [[mcp-connectors-landscape]] — which MCP servers + Connectors recur (Google / Notion / Linear / Playwright / Fireflies / Mercury / custom Context-OS)
- [[scheduling-and-the-app-open-constraint]] — the hardware constraint everyone hits + Kenny Liao's cron-tool workaround + Jack Roberts's Railway alternative
- [[skills-to-plugins-pipeline]] — codify-after-success pattern + the "handover test" + skills vs plugins
- [[token-and-cost-management]] — Sonnet-for-most / Opus-for-hard, script-vs-agentic, 30-45-min session cycling
- [[production-readiness-gaps]] — what the YouTube layer doesn't cover (resilience, PII, version control, telemetry, eval suites)
- [[takeaways]] — 9 actionable rules consolidated

## Cross-links to related autopilot topics

- [[../autonomous-loops-human-in-the-loop/_index]] — Cowork is Anthropic's first-party answer to the HITL-scheduled-task pattern; cron-workaround connects directly
- [[../agent-dashboard-os/_index]] — Cowork's telemetry gap (per Gaps §5) is exactly what the agent-dashboard-os topic addresses
- [[../harness-engineering/_index]] — Cowork sits at the consumer-end of the harness-engineering spectrum (vs Claude Code at the developer end)
- [[../10x-claude-code/_index]] — productivity-multiplier framing overlaps; Cowork is the non-technical-user variant
- [[../claude-md-12-rules/_index]] — CLAUDE.md / behavioral-contract pattern recurs as Cowork's `.md` brain files

## Cross-links to Storm Bear curated vault

- [[external|Storm Bear: AutoGPT (v59)]] — first-party-employee framing predates Anthropic's Cowork by years; useful contrast
- [[external|Storm Bear: Building with Claude on Google Cloud (talk wiki)]] — also covers subagents + MCP + skills composition but at the developer/Cloud-Run layer, not the desktop-employee layer

## Key topical observations (cross-source synthesis)

- **Anchored Vietnamese tutorial (Duy Luân Dễ Thương)** treats Cowork as a desktop-scraping tool (browser → Excel); reflects a different operator persona than the US "AI employee for businesses" framing dominant in 4 of 6 sources
- **Kenny Liao** is the most-cited outlier — both for his cron-tool workaround AND his nightly-brain-dump pattern that's qualitatively different from the static-context-file approach others use
- **Three definitions of Cowork-vs-Code split** across 3 speakers (skill-level / professional-function / rebrand-history) suggests Anthropic's product positioning is still settling
- **The "Sonnet for most, Opus for hard" consensus** appears across 3 independent speakers — likely the strongest cost-management signal in the corpus

## Status

- **Compiled:** 2026-05-29
- **Stub articles:** 0
- **Gaps:** (none — initial compile)
- **Promotion candidate?** Not yet — 1 source bundle (this corpus), <5 articles in a single drain. Re-evaluate after 2+ sibling topics or audit cycle.
