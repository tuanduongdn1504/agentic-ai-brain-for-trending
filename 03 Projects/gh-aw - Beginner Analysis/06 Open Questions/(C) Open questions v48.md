# (C) Open Questions — gh-aw v48

> **Wiki #48** | **2026-04-25** | Questions tracked for future strengthening / counter-evidence / pilot decisions.

## About the project

1. What is the actual production usage scale of gh-aw inside GitHub itself (dogfooding scope)? README mentions "core team uses agentic workflows" — but is gh-aw used to build GitHub.com? Actions? Other GitHub products?
2. How many of the 201 paired `.md`/`.lock.yml` workflows in `.github/workflows/` are gh-aw-meta (workflows that develop gh-aw itself) vs example workflows for users to copy?
3. What's the intended commercial trajectory? gh-aw is fully MIT — does GitHub plan a commercial GitHub Actions tier with gh-aw integration (parallel to GitHub Copilot Business / Enterprise)?
4. Does Peli's Agent Factory blog post (2026-01-12) reveal a research roadmap distinct from product evolution? Need to read for full lineage context.
5. What's the actual breakdown of contributor authorship — how many PRs come from `@dsyme` / `@pelikhan` / `@eaftan` / `@krzysztof-cieslak` vs Copilot agent vs community?
6. Why migrate from `githubnext/gh-aw` to `github/gh-aw` at v0.40.1 (2026-02-03) — graduation criteria? Internal milestones?

## Pattern Library questions (for future audits)

7. **Pattern #19 archetype 2 methodology-lineage**: GitHub Next as research-cluster joins Anthropic-team-cluster as 2nd named-cluster lineage type. If 3rd cluster appears (e.g., Microsoft Research / Google DeepMind / Meta FAIR contributing to Storm Bear corpus framework), can we promote "research-org-cluster-as-lineage-archetype" sub-pattern within #19?
8. **Pattern #66 OT promotion path**: gh-aw provides strongest defense-in-depth data point yet (W3C-style spec + SBOM + AWF + MCP Gateway + compile-time validation + 8 named layers). At what N does Pattern #66 graduate from OBSERVATION-TRACK to CONFIRMED architectural pattern? Currently event-based-incident-response framing locks it as OT — but gh-aw's PROACTIVE architectural-defense framing differs structurally.
9. **MCP Gateway as Pattern #18 Layer 0 candidate**: ollama v46 introduced "Layer 0 runtime-bundled-agent-launcher" observation at N=1. gh-aw introduces "MCP-gateway-as-unified-routing-infrastructure" at N=1 — same Layer-0 structural position? If yes, Layer 0 has 2 sub-types at N=2 = potential formulation extension at next mini-audit.
10. **Pattern #22 sub-variant 22c counter-evidence**: aidevops v47 introduced 22c authoritative-with-shim (AGENTS.md primary + CLAUDE.md/AGENT.md redirect-shims). gh-aw v48 at github-corporate-official tier is **AGENTS.md-only** (NO CLAUDE.md). Does this counter-evidence narrow 22c to non-corporate-official scope? Or is 22c about authoritative-with-shim specifically (where aidevops has shims and gh-aw doesn't, both fall into "AGENTS.md-primary" but only aidevops has 22c)? Refinement opportunity at next mini-audit.
11. **Engine-frontmatter-axis vs MCP-server-axis**: Pattern #28 has 3-axis taxonomy as of v47 (routing-abstraction + native-multi-provider + verification-not-routing). gh-aw introduces "engine-selection-as-frontmatter-axis" — is this a 4th sub-axis or sub-variant of native-multi-provider?
12. **gh-aw vs spec-kit dual-presence**: github org now has 2 corpus entries (T1 + T4). What's the corpus pattern of multi-product-from-same-corporate-parent? Microsoft has 2 entries (T3 + T4). Google has 2 entries (T4 + outside-scope). At N=4 corporate-multi-product organizations, is sub-pattern formalization warranted?

## Storm Bear vault implications

13. **AGENTS.md vault-refactor template choice** — gh-aw provides 49.8 KB AGENTS.md at corporate-official tier. spec-kit v17 provides reference at T1. aidevops v47 provides 22c sub-variant. Of the 3 corpus templates, which best fits Storm Bear vault (knowledge-base-not-codebase)? gh-aw is closest to vault philosophically (markdown-source-truth + skills directory) but heaviest at 49.8 KB.
14. **`05 Skills/` vs `skills/` directory architecture** — gh-aw's 24 specialized skill subdirs each have own SKILL.md with focused domain. Storm Bear `05 Skills/` has 8 skills. Should Storm Bear convert each skill to subdir-per-skill with full README + examples + tests (gh-aw model) or stay flat (current)?
15. **Compile-time-validation philosophy** — gh-aw validates markdown specs before execution. Should Storm Bear apply analog: validate wiki structure (Phase counts, entity counts, cross-references) before "shipping"? Currently routine v2.1 has fact-verification protocol (post-hoc); gh-aw model = pre-execution.

## Routine v2.2 candidates from v48

16. **EXTREME-tier 4-tier informal-discipline refinement** — proposed at v42 ruflo. Now N=2 EXTREME (aidevops v47 + gh-aw v48). At N=3 EXTREME, formalize as routine v2.2 default-aware-of-EXTREME tier?
17. **Lineage-cluster registration pattern** — Anthropic-team-cluster (claude-howto v32) + GitHub Next 4-researcher cluster (gh-aw v48). When does cluster-as-lineage-node get formalized as Pattern #19 sub-mechanism distinct from individual-node?
18. **Defense-in-depth N-layer enumeration discipline** — gh-aw observed at 8+ layers. Future wikis with security depth should enumerate layers explicitly for Pattern #66 OT comparability.

---

**Status:** 18 questions tracked at v48 close. 6 about-the-project + 6 Pattern Library + 3 vault-implication + 3 routine-v2.2 candidates.
