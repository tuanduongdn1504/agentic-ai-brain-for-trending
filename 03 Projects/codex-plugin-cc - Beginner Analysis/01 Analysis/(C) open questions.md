# Open questions — codex-plugin-cc Beginner Analysis

## On the project

1. Is `/codex:adversarial-review` purely prompt-framing, or does it dispatch a separate Codex session with adversarial system prompt? (Source said "reframes existing review function" — clarify if "function" = same Codex session or new session-with-different-prompt)
2. Why did OpenAI publish FOR Claude Code (rival platform) rather than only their own Codex CLI? Strategic motive: marketshare protection? Developer UX optimization? Acknowledgment of Claude Code's UX advantage?
3. License Apache-2.0 (not MIT) — does this signal anything beyond default OpenAI licensing? Apache-2.0 has explicit patent grant; relevant for AI-tool space.
4. What's in `plugins/codex/agents/` — separate Codex agent definitions? Or same as Claude Code skill format?
5. `plugins/codex/hooks/` — hooks for what? Pre-review / post-review? Authentication? Session lifecycle?
6. Background-task primitive (`/codex:rescue --background`) — corpus-first explicit background-job management for delegated AI work?
7. Does codex-plugin-cc work bidirectionally — can Codex CLI invoke Claude Code? Or one-direction-only Claude-Code → Codex?

## On the org / archetype

8. Is this OpenAI's first-ever plugin published for a competitor platform? Or precedent (e.g., GitHub Copilot extensions for VSCode forks)?
9. Apache-2.0 signaling — OpenAI's recent licensing practice across plugins?
10. v1.0.4 with 26 commits = highly-condensed development; team size at OpenAI working on this?

## On Pattern Library implications

11. Pattern #76 counter-evidence: should "adversarial-review-as-prompt-framing variant" register as NEW Pattern #77, or as sub-variant of #76, or as observation-track only?
12. Cross-vendor cooperation (OpenAI → Claude Code): NEW Pattern #77 candidate, or extension of Pattern #19 corporate-strategic archetype?
13. T4 sub-taxonomy: 2-axis at v60 (content-transformation N=8 + protocol-translation N=1); v61 cc-sdd added install-time-skill-format-translator (different mechanism). v62 codex-plugin-cc = competitor-platform-bridge-as-plugin. Is T4 now 4-axis taxonomy or are these all sub-variants of "translation-bridge" parent?
14. Pattern #57 57c — does codex-plugin-cc README explicitly cite Claude Code primitives or anthropics/skills? Implicit citation via plugin marketplace install command vs explicit textual citation distinction.

## On Storm Bear vault applicability

15. Does codex-plugin-cc fit Storm Bear pilot ranking? (vs cc-sdd v61 + free-claude-code v60 already at HIGH-OPERATIONAL)
16. ChatGPT subscription requirement for codex-plugin-cc — Storm Bear has it but cost-benefit calc?
17. /codex:adversarial-review use-case mapping for vault Scrum-coaching software work?

## On corpus methodology

18. v63 EARLY mini-audit registered Pattern #76 N=1 stale-flagged 1 wiki ago. Counter-evidence at v62 (immediate next ship) = fastest counter-evidence cycle in corpus history. Routine v2.2 candidate: codify "fast-counter-evidence detection" as Phase 0.5 expanded check?
19. Cross-vendor cooperation observation = potential NEW pattern. Should Phase 0 classification axis "Org type" expand to include "competitor-publishing-for-rival-platform" sub-archetype?
20. Apache-2.0 license — is this corpus base-rate increasing? (Track: spec-kit Apache, magika Apache, codex-plugin-cc Apache vs MIT-default for many others)
