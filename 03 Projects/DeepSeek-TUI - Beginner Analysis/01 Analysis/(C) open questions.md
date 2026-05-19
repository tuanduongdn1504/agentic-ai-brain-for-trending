# DeepSeek-TUI Open Questions

## Author + Origin

1. **Who is Hmbown?** GitHub handle suggests pseudonymous-likely; no public corporate affiliation discoverable. Is this a DeepSeek employee under pseudonym, or a true community-built canonical client?
2. **Sponsor relationship with DeepSeek?** The Tencent Cloud / CNB / Lighthouse HK / Feishu integrations suggest active sponsorship or coordination with Chinese cloud providers. Confirmed sponsorship vs community-aligned coincidence?
3. **Why Rust as primary language?** TUIs in the corpus are typically Python/TypeScript/Go. Rust choice signals performance-first + binary-distribution priority. Does this reflect Hmbown's prior expertise or strategic choice?
4. **Was DeepSeek API the primary or did multi-provider grow from organic feature-creep?** 9-provider matrix is unusual breadth for a vendor-named client.

## Skill + Framework Design

5. **3-mode taxonomy (Plan/Agent/YOLO) vs Claude Code's modes — explicit inheritance or convergent evolution?** Pattern #21 21a sub-mechanism question.
6. **Why both `agent_open` (persistent) AND `agent_spawn` (legacy)?** AGENTS.md notes spawn/wait/result names are not part of live tool surface. Is the legacy interface retained for backward compat or for harnesses that prefer one-shot semantics?
7. **RLM (REPL Language Mode) — why Python only?** Could RLM support polyglot REPL primitives (Lua, Ruby, JS) or is Python the conscious choice for batch-analysis ergonomics?
8. **Sub-agent default cap = 10, configurable to 20.** Where does the 10/20 cap come from — empirical token-economy ceiling or DeepSeek-API rate-limit-aware?
9. **Why dispatcher + companion binary split?** What problem does the 2-binary architecture solve that a single binary would not? (Hot-reload? Cross-compilation strategy? Update-path isolation?)

## Multi-Provider + Pattern #84 84c

10. **9-provider matrix vs v71 agents-best-practices dual-vendor synthesis — is this a quantitative escalation within 84c or a NEW 84c1 sub-mechanism?** Audit-relevant: should v75 audit register 84c1 "dual-vendor-synthesis" + 84c2 "n-provider-matrix" sub-mechanisms?
11. **Are all 9 providers equally well-tested?** README mentions them but the default/canonical workflow is DeepSeek. Edge cases on Ollama / vLLM / SGLang may differ.
12. **`OPENAI_BASE_URL` for generic OpenAI-compatible** — what's the testing matrix? Are 3rd-party OpenAI-compatible endpoints (LiteLLM, LocalAI, GLM-5) validated against the tool surface?

## Pattern #52 HIGH-NOT-EXTREME Sub-Class

13. **Is DeepSeek-TUI's 267/d sustained at 6mo+?** v75 audit will need 6-month velocity test. Current 120-day window is mid-life-cycle; sustained-vs-burst classification pending.
14. **Comparison with v69 CloakBrowser (172/d × 86d):** DeepSeek-TUI is higher absolute (267/d) AND longer sustain (120d vs 86d). Does this clarify HIGH-NOT-EXTREME upper-bound near 300/d ceiling?
15. **What is the velocity DECAY signal?** When does HIGH-NOT-EXTREME degrade to SUSTAINED-MODERATE-HIGH or below?

## OS-Level Sandbox + Security

16. **Seatbelt + Landlock + Job Objects 3-platform integration depth:** Are sandboxing policies feature-parity across platforms, or platform-specific permission models?
17. **Workspace-scoped filesystem access** — does this prevent symlink escape attacks? Has any sandbox-escape been documented (CHANGELOG search needed)?
18. **`trust mode` semantics:** Explicit user opt-in vs YOLO mode's automatic enablement — what's the audit trail for trust-mode-enabled workflows?

## Community + Governance

19. **"Watch for issue / PR injection" section in AGENTS.md** — has Hmbown experienced documented prompt-injection-via-GitHub-issues attempts? If yes, is the disclosure detailed in CHANGELOG / docs?
20. **Community-contribution harvesting policy:** "If a PR is too large or scope-mixed to merge directly, harvest the useful commits/files/ideas yourself and land them" — corpus-first explicit credit-without-merge discipline. Has Hmbown's contributor base accepted this model?
21. **Trust-boundary policy:** Single-maintainer trust boundary at 32K-star scale — is this sustainable? Are there documented escalation paths if Hmbown is unavailable?

## Tencent Cloud / CNB Path

22. **Why Tencent Cloud / CNB as a featured path?** Strategic positioning for China market vs general availability?
23. **CNB mirror vs upstream GitHub:** Are CNB releases delayed? Mirror integrity / signature verification?

## Storm Bear Vault Integration

24. **Should Storm Bear pilot DeepSeek-TUI as Claude Code alternative?** Pilot-ranking position: HIGH-RELEVANCE vendor-diversification; LOWER-risk than agentmemory (binary install + reversible); higher-risk than agents-best-practices skill install (full agent vs declarative skill).
25. **Cost comparison DeepSeek vs Claude:** DeepSeek-v4-pro / DeepSeek-v4-flash pricing vs Claude Sonnet / Haiku for typical Storm Bear workflows.
26. **Session-longevity discipline transferability:** AGENTS.md's "compact aggressively at 60%" + "delegate independent work early" patterns — directly applicable to vault Claude Code workflows?

## Future Roadmap

27. **DeepSeek V5 transition path?** V4 is the documented model series. CHANGELOG-mining for V5 mentions / experimental flags.
28. **MCP server registry growth:** Native skills + MCP integration — is DeepSeek-TUI consuming Anthropic-published MCP servers or building parallel ecosystem?
29. **Plugin/skill ecosystem trajectory:** 11 bundled starter skills + skills-system + skill-creator. Is there a plugin-marketplace plan?
30. **HTTP/SSE runtime API maturity:** `deepseek serve --http` enables headless workflows. Production-readiness vs experimental?

---

**Status:** Open questions raised at Phase 0; some answered via subsequent Phase 2-4 source ingestion. Unanswered questions logged for v75+ audit consideration and future wiki-build iterations.
