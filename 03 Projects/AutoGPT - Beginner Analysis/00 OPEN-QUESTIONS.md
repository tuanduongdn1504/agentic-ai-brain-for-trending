# 00 OPEN-QUESTIONS — AutoGPT v59 LLM Wiki

## License-axis questions

1. **PolyForm-Shield-vs-Noncommercial flavor distinctions** — Shield restricts use as competing service while Noncommercial restricts commercial use entirely. Does Pattern #72 rename cleanly capture both? Verify wording at v60 mini-audit.
2. **What was the licensing history of AutoGPT?** README at probe scope shows current state. Was there a pre-March-2024 license different from current MIT + PolyForm-Shield? Could verify via git log on LICENSE file. Relevant for Pattern #29 license-evolution sub-observation if license shifted (would be observable-historical-license-shift data point).
3. **Does the autogpt_platform/ folder PolyForm-Shield restrict Storm Bear from running it for client Scrum-coaching?** Per PolyForm Project's PolyForm-Shield text: "permitted to use the software for any purpose other than building a product or service that competes with the licensor's product or service." Does Storm Bear's Scrum-coaching consultation business compete? Likely NO (Scrum-consulting ≠ AI-agent-platform). But needs explicit decision at v60+ if pilot proposed.

## Pattern-test questions

4. **Is AutoGPT cited by ANY of 58 prior corpus subjects?** If corpus grep returns N≥1 hits, Pattern #57 BIDIRECTIONAL-ABSENCE observation revises. Conservative-discipline assumes NO at probe scope; needs full grep at v60 mini-audit. **HIGH-PRIORITY question for v60.**
5. **Is Toran Bruce Richards explicitly named-attribution in current README?** WebFetch did not capture explicit name. Worth verifying at LICENSE / CITATION.cff / package.json author field for Pattern #19 archetype 4 founder-attribution evidence.
6. **Pattern #19 founder-personal → org-stewardship sub-variant N=2 with n8n v56** — promotion candidate at v60. What is the 3rd corpus instance to look for? (founder-with-public-attribution + org-scale commercial entity = look for OpenAI / Anthropic / spec-kit-Microsoft variants at next subjects).
7. **Is AGENTS.md content materially different from CLAUDE.md content?** If parallel content (AGENTS.md = same instructions as CLAUDE.md) → Pattern #22 observation = file-format-redundancy. If divergent → Pattern #22 observation = role-divergence (AGENTS.md for agents-other-than-Claude / CLAUDE.md Claude-specific). Verify at v60.

## Architectural questions

8. **Is autogpt_platform/ a Python+TS hybrid OR is Platform Python-only and Classic Frontend TS?** Probe captured 69% Python + 29.4% TS but didn't disaggregate by sub-component. Affects Pattern #25 polyglot sub-variant interpretation.
9. **What runtime substrate does AutoGPT Platform use for agent execution?** Is it Pi-SDK-style (gsd-2 v54 vendoring observation) or own-runtime? Affects Pattern #18 sub-observation tracking.
10. **Forge toolkit role** — is it for AutoGPT-internal-developer-extension or for external-developer-using-AutoGPT-as-platform? Affects T1-vs-T5 tier-placement nuance.

## Pilot-relevance questions

11. **Storm Bear pilot-relevance estimate** — currently MEDIUM-LOW pending license-acceptability decision. Specifically: Can Storm Bear deploy autogpt_platform on cloud-tier (agpt.co paid) for client Scrum-coaching workflows without violating PolyForm-Shield non-compete? Likely YES (Scrum-consulting ≠ AI-platform-competition) but needs explicit license-decision at v60.
12. **What concrete Scrum-coaching workflow would AutoGPT solve uniquely?** Compared to (a) n8n v56 (workflow-automation generalist with 16-LLM-providers), (b) OpenSpec v58 (SDD methodology framework), (c) mattpocock v57 (skill-library), AutoGPT's distinct value-add for Scrum is unclear at probe scope. Maybe: agent-builder for autonomous sprint-metrics-aggregation? Maybe: Forge for custom Scrum-agent development? Needs concrete use-case workshop at v60+.

## Audit-decision questions

13. **Does v60 mini-audit fire EARLY at v59 given 2 un-stale events?** Routine v2.1 says trigger ratio 0.95:1 (no — currently 0.436:1) OR active count ≥30 (no — currently 17 unchanged). Un-stale events do NOT auto-trigger early mini-audit. **Decision: carry to v60 natural cadence.** 12+ promotion-candidates queued = v60 mini-audit projected to be LARGEST in corpus history.
14. **Should the v60 mini-audit be pre-scheduled with explicit agenda BEFORE v60 wiki ships?** Given 12+ items queued, agenda-pre-registration would prevent scope-creep. New routine v2.2 candidate: "pre-registered mini-audit agenda when N≥10 candidates queued."

## Storm Bear meta SKIP-validation questions

15. **Is the v59 disciplined-skip the FIRST in 41-streak history?** Per CLAUDE.md analysis YES. Confirms session-66 STRICT amendment is exercising both directions (satisfiable + skippable). Goodhart's-law correction working as designed.
16. **What are the first-mover-authority-without-lineage characteristics?** AutoGPT didn't cite anybody but became foundational. Distinguishes from citation-supported-authority (mattpocock v57 books) + personal-claim-supported-authority (automate-faceless-content v55 "OG AI Wizard") + corporate-organizational-authority (spec-kit v17 GitHub). NEW sub-variant Pattern #19 candidate at v60 mini-audit if 2nd first-mover-authority-without-lineage emerges.
