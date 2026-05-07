# OpenSpec v58 — Open Questions

## High priority (resolve at v60 mini-audit or sooner)

1. **Q1: Who is behind Fission-AI?** Org page states "no public members"; package author "OpenSpec Contributors"; no individual founder visible. Is this a startup in stealth, a community project, or a corporate side-project? Investigation hooks: PR-QUEST sibling repo contributors / commit author git history / posthog-node telemetry endpoint owner / npm package publisher email (if visible).
2. **Q2: Pattern #57 57c sub-variant promotion candidate.** With OpenSpec v58 → spec-kit v17 citation, 57c reaches N=8 conservative-attribution. Is this enough evidence to formally extend 57c formal-statement or promote a sub-variant? Defer to v60 mini-audit (2-wiki runway).
3. **Q3: Org-level-pseudonymity sub-variant** (CLAUDE.md observation #4) — Fission-AI is corpus-first org-level-pseudonymous-with-active-commercial-product (vs v21 system-prompts-leaks individual-pseudonymous-leaked-content). N=1 stale-flagged v63/v68; needs 2nd observation for promotion candidate.

## Medium priority

4. **Q4: posthog-node telemetry default-on?** OpenSpec ships posthog-node analytics dependency. Does default install opt-in or opt-out for telemetry? Supply-chain awareness flag for beginner guide caveats section.
5. **Q5: Per-tool skill/command file generation mechanism.** OpenSpec generates 11 skills × 30+ tools = ~330+ artifacts. How are tool-specific formats determined (YAML / TOML / markdown)? Is this corpus-first cross-tool-skill-format-translator pattern?
6. **Q6: Comparison to mattpocock v57 plugin manifest.** Both v57 and v58 deploy skill-files as the universal deployment-format. v57 = single .claude-plugin manifest declares 13 skills. v58 = generates per-tool skill files for 30+ tools. Are these structurally distinct sub-variants of skill-file-as-deployment-target Layer 0 sub-axis?

## Low priority / observational

7. **Q7: Which 11 generated skill commands map to which workflow phases?** propose / explore / new-change / continue-change / apply-change / ff-change / sync-specs / archive-change / bulk-archive-change / verify-change / onboard — full ontology check at v60 if 57c sub-variant work.
8. **Q8: Schemas/spec-driven directory.** Does OpenSpec define a schema for SDD specifications? If schema-driven, does it parallel Pattern #69 EXTREME primitive-count or a different axis?
9. **Q9: 25+ vs 30+ tools count discrepancy.** README claims "20+ AI assistants" / "25+ tools"; supported-tools.md docs list 30+. Standardize at v60 with `gh api` or recent docs probe.
10. **Q10: Dashboard support reference.** README mentions "dashboard support — visual tracking". Is there a separate dashboard product or is it CLI-only? Pattern #2 distribution-evolution probe.

## Vault-internal

11. **Q11: STRICT-amendment N=3 emergent pattern.** v56 + v57 + v58 = 3 consecutive STRICT-passing wikis with named-methodology + in-corpus-citation as common signal. Should Phase 0.9 formal-statement be amended at v60 to recognize this emergent pattern?
12. **Q12: 22-streak verification.** Confirm 0 new active candidates registered post-v58; Pattern Library state should remain 17 active. If org-level-pseudonymity (CLAUDE.md observation #4) registered as standalone, streak breaks at v58 not v57.
