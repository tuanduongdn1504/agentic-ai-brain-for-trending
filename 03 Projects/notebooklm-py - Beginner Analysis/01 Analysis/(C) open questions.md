# (C) Open Questions — notebooklm-py

> Placeholder. Append findings as wiki build progresses.

## Questions surfaced Phase 0

1. **RPC stability window** — How long before Google breaks the undocumented API? Historical data via git log would show. Fragility = operational risk for anyone building on top.
2. **OpenClaw relationship** — SKILL.md mentions OpenClaw compatibility. Is OpenClaw a framework I should add to corpus? (Potential 8th wiki candidate)
3. **Agent isolation enforcement** — AGENTS.md recommends `NOTEBOOKLM_HOME=/tmp/<agent-id>`. Is this actually enforced or advisory? Without enforcement, parallel agents collide.
4. **Premium plan testing** — Plan tiers (Standard 50 / Plus 100 / Pro 300 / Ultra 600 sources). Library doesn't enforce limits. Does it throttle gracefully or fail loud?
5. **Windows compatibility post-v0.3.1** — Changelog shows multiple Windows fixes Jan 2026. Stable now or still flaky?
6. **Storm Bear use case viability** — For VN Scrum coaching, does NotebookLM support Vietnamese content well? Course material + retro transcripts + 1:1 notes in Vietnamese.
7. **Cross-agent workflow conflict** — If Claude Code + Codex both use skill on same machine, do they collide on same credentials/profile?
8. **Cost model** — NotebookLM is Google paid product. Storm Bear budget consideration for serious use.
9. **Tier 4 classification robustness** — Is this actually Tier 4 ("bridge"), or is it a cross-cutting axis any Tier 1 agent can adopt? Could be both. Need second Tier 4 entrant to validate.
10. **Skill vs Tier 1 framework** — notebooklm-py ships a Skill (`SKILL.md` + `notebooklm skill install`). Does this make it partially Tier 1? Or is "ships a skill" different from "IS a framework"?
11. **Undocumented API reverse engineering maintenance** — Single solo maintainer (teng-lin) handles all RPC fragility. Bus factor = 1. If maintainer stops, library dies within weeks.
