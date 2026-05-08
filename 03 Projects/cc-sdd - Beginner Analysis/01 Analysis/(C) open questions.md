# Open questions — cc-sdd Beginner Analysis

> Generated at Phase 0; refined during Phase 2-3; surfaces residual uncertainty + future research directions.

---

## On the project itself

1. Is "Kiro IDE" a verified independent project, or is it gotalab's framing/coinage? (CHANGELOG mentions "Removed Amazon book reference" at v3.0.2 — Kiro might be Amazon's IDE methodology, but verification needed)
2. What's the relationship between cc-sdd's `.kiro/` directory convention and any external Kiro IDE? Is gotalab implementing someone else's methodology or extending their own naming?
3. Why was "Ralph Loop dependency" deprecated at v3.0.0? What was Ralph Loop providing that Skills mode now natively provides?
4. v3.0.0's shift from `/kiro:command` (colon syntax) to `/kiro-discovery` (dash syntax) — is this an Agent Skills mode constraint, or a stylistic choice?
5. The "P0 / P1 wave" task-priority model — is this gotalab's own convention or borrowed from a methodology I haven't covered?
6. EARS (Easy Approach to Requirements Syntax) — first time corpus has explicit EARS reference. Worth exploring as future Pattern Library entry?
7. cc-sdd's File Structure Plan (FSP) primitive — is this corpus-first as a separate spec artifact, or just renamed design.md content?

## On the author / archetype

8. Is gotalab the FIRST solo-Japanese T1 author in corpus? (Need to verify against full project list — v51 ollama is GitHub Inc / vercel-labs is Vercel / etc.)
9. gotalab's ecosystem-portfolio (cc-sdd 3.3K + skillport 385 + uxaudit 36 + claude-code-marimo 24) — does this fit Pattern #19 first-mover-authority-without-lineage variant? Or is it different (ecosystem-builder-with-multiple-products)?
10. Zenn presence (zenn.dev/gotalab) — Japanese tech publishing platform. Does this affect i18n or methodology-distribution patterns observed?

## On Pattern Library implications

11. Does Pattern #21 un-stale require N=2 *cross-tier* observations OR N=2 *cross-archetype* observations? v25 audit phrased it "ideally at different tier" — preference, not gate. v61 evidence is N=4 cross-archetype (corporate / pseudonymous-org / solo-product-line / solo-Japanese) all T1.
12. Should SDD methodology meta-pattern be promoted as Pattern #21 (current candidate) or as new pattern (consolidation-forward)?
13. Pattern #18 "agent-platform-format-translation-installer" sub-archetype — is N=1 (cc-sdd) at registration, or does OpenSpec v58 30+ tools per-tool format translation count as N=2 prior observation? Risk of overlap pre-check failure (>70%).
14. Pattern #51 vibe-coding nuance — counter-evidence-driven refinement candidate? cc-sdd is anti-vibe-with-pragmatic-acknowledgment ("vibe coding genuinely outpaces formal contracts" sometimes). Does this narrow Pattern #51's spectrum or just add a refinement?

## On Storm Bear vault applicability

15. Is cc-sdd a viable pilot replacement for ad-hoc Claude Code workflows in vault project work? `npx cc-sdd@latest --claude-skills` would install Skills mode harness — measurable test possible.
16. Does cc-sdd's "boundary-first design discipline" + "File Structure Plan" port well to solo-vault-author scenarios, or is it sized for team-scale?
17. EARS-format requirements — would these add useful structure to Storm Bear `04 Reviews/` weekly notes, or would the discipline be over-engineered for solo journal-flow work?

## On corpus methodology

18. v60 mini-audit rejected Pattern #21 un-stale via gsd-2 v54 on lineage-grounds. v61 cc-sdd resolves the same blocker on independence-grounds. Should a corpus-routine improvement be codified: "un-stale candidates that fail lineage-test should re-evaluate on independence-test before staying stale"?
19. Phase 0.9 STRICT 1-of-4 check produced 6-instance window 83% INCLUDE rate (v56-v61). Is this rate evidence the criteria are calibrated correctly, or evidence corpus subjects systematically pass 3-of-4 on the borderline-PASS path?
20. Pattern #21 promotion question (raised in section 11): if promoted at next mini-audit, what criterion? Default ≥3 across 2+ tiers (FAIL — all T1) vs structural-unambiguity-at-N=2 (PASS — all 4 SDD frameworks structurally unambiguous) vs meta-pattern-at-N=3-consolidation (PASS — could consolidate Pattern #21 + observations from spec-kit/OpenSpec/cc-sdd subsequent observations).
