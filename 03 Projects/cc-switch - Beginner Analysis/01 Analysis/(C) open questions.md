# cc-switch Open Questions

## Author + Origin

1. **Who is farion1231?** Chinese-language README at 32KB suggests Chinese-speaking developer; Chinese-aligned sponsor ecosystem (20+ Chinese API relay providers). Solo individual or small team?
2. **Why "cc"-prefix naming?** Convergent with v61 cc-sdd naming pattern — "cc" as Claude Code shorthand becoming community convention?
3. **Was Claude Code the primary motivation, or did multi-runtime aggregation grow from organic feature-creep?**
4. **20+ sponsors — financial relationship structure?** Is this a sponsor-funded project? What % of farion1231's time is supported by sponsor revenue?

## Architecture

5. **Why Tauri 2 over Electron?** Performance/binary-size advantage clear, but Tauri ecosystem maturity vs Electron in 2025-2026?
6. **Why SQLite as SSOT instead of JSON config files?** Atomic writes + mutex + relations clearly motivate, but adds toolchain complexity for simple use case.
7. **What's the failure mode of the "Temp file + rename" atomic-write pattern?** Pre-empts most config-corruption; edge cases?
8. **Dual-way sync (write live + backfill from live) — race condition risk?** Mutex-protected SQLite mitigates but what about external-process writes between switch and backfill?
9. **Cross-runtime MCP/Skills/Prompts sync — semantic mapping problem?** Claude Code's CLAUDE.md ↔ Codex's AGENTS.md ↔ Gemini's GEMINI.md — how does cc-switch handle format-divergence?

## Multi-Runtime + Pattern #84 84c

10. **Why 6 runtimes specifically?** Claude Code + Codex + Gemini CLI + OpenCode + OpenClaw + Hermes Agent — chosen by user demand or maintainer preference?
11. **50+ provider presets — testing matrix?** Each preset has different auth/endpoint/quirks. How are they validated?
12. **OpenClaw is community fork — relationship with cc-switch?** OpenClaw appears in 4 of 6 runtimes managed; v73 is the second corpus subject mentioning OpenClaw (v67 opencode-antigravity-auth was first).

## Pattern #52 HIGH-NOT-EXTREME Sub-Class

13. **Is 259/d × 289d sustainable at 12mo+ window?** v75 audit will need extrapolation evidence.
14. **Comparison with v72 DeepSeek-TUI (267/d × 120d) and v69 CloakBrowser (172/d × 86d):** v73 cc-switch at lower velocity but 2-3x longer sustain — sub-class definition validated at extended-sustenance dimension.
15. **What signals would indicate velocity DECAY?** Sponsor churn? Issue close-rate dropping? CHANGELOG release cadence slowing?

## Supply-Chain + Pattern #66

16. **Atomic-writes-as-architectural-primitive** — corpus-first explicit formalization. Has cc-switch documented any past config-corruption incident that motivated this discipline?
17. **macOS code-signing + notarization** — Apple Developer ID + notarization process explicit. Same level for Windows MSI (signed)?
18. **20+ sponsor entries in README — quality control on sponsor recommendations?** README warns: "Only official website: ccswitch.io" — implies aware of impersonation/fork-confusion risk. Sister to v69 CloakBrowser look-alike-repo warning.

## Community + Governance

19. **CHANGELOG at 133KB — release cadence?** Per `pushed_at` of 2026-05-19, very recent activity. Multi-daily releases sustained?
20. **923 open issues — issue-triage workload?** With 75K stars + 4.8K forks, the maintainer-load is significant. Does farion1231 have helpers?
21. **Sponsor-content-as-README boilerplate vs core content:** Sponsor section dominates first ~140 lines of README. Acceptable trade-off for sponsor revenue?

## Storm Bear Vault Integration

22. **Should Storm Bear pilot cc-switch FIRST or AFTER vendor-diversification trial?** cc-switch is MOST DIRECTLY RELEVANT vault pilot candidate seen in 73-wiki corpus — manages Claude Code + 5 alternatives at unified UI layer.
23. **Pilot rank — #1 candidate?** Recommended pilot sequence may now be: cc-switch FIRST (unified-management installation = lowest infrastructure overhead with immediate vendor-diversification awareness) → codegraph SECOND (read-only) → agents-best-practices skill THIRD → agentmemory FOURTH → DeepSeek-TUI FIFTH.
24. **Cost concerns:** No subscription cost (MIT-licensed binary), but provider API costs continue. cc-switch helps optimize provider selection (50+ preset providers; 20+ relay options).

## Future Roadmap

25. **Tauri 3 transition path?** Tauri 2 is current; how does cc-switch handle major framework version upgrade?
26. **Pattern #84 84c1 vs 84c2 vs 84c3 sub-typology?** v71 + v72 + v73 evidence within 84c shows quantitative escalation. v75 audit should consider splitting 84c into sub-types.
27. **OC-Q "Sponsor-Density-As-Corpus-Signal" — promotion path?** If v76+ wiki adds another 10+ sponsor subject, promote to formal observational candidate.
28. **Pattern #18 sub-archetype #8 "multi-runtime-aggregator-desktop-app" — N=2 candidate?** No other corpus subject yet matches. v76+ stale-check.
29. **Hermes Agent integration depth?** Hermes-agent appears in repo topics but is corpus-adjacent. Pending corpus subject?
30. **`ccswitch://` deep-link protocol — emerging convention?** Could influence v74+ corpus subjects to adopt similar URL-based config-import patterns.

---

**Status:** Open questions raised at Phase 0; some answered via Phase 2-4 source ingestion. Unanswered questions logged for v75+ audit consideration.
