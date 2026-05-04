# (C) agent-skills-of-vercel — Open Questions

Questions surfaced during v51 build. Some answered; others flagged for future investigation.

## Answered (during build)

1. **Is `agentskills.io` Anthropic-affiliated or third-party?** → Third-party. README says "Skills follow the [Agent Skills](https://agentskills.io/) format" — agentskills.io is independent format spec hosted at skills.sh. Vercel's homepage `https://skills.sh/vercel-labs/agent-skills` confirms skills.sh is registry / agentskills.io defines spec. NOT Anthropic-owned.

2. **Are CLAUDE.md and AGENTS.md actually identical?** → YES. Verified via `diff` — byte-identical 3,281-byte files, both starting `# AGENTS.md`. This is corpus-first 22d identical-mirror sub-variant.

3. **Did multica v15 actually cite Vercel agent-skills?** → YES. Pattern Library line 2969 + vault CLAUDE.md row 2969 confirms `"Vercel agent-skills import (first)"` cited at v15 (36 wikis pre-v51). Validates Pattern #57 57c forward-citation-then-wiki sub-variant N=1 registration.

4. **Does Vercel meet Pattern #17 variant 5 criteria (>$1B + multi-product + OSS + commercial + >10y)?** → YES. Vercel valued ~$3.25B in 2024 funding round, founded 2015 (~10 years); products: Next.js (OSS) + Vercel Cloud (commercial) + AI SDK + v0.dev + Vercel Toolbar + multiple ecosystem libraries. Variant 5 N=3 strengthening default-criterion-clean.

5. **How many skills does this repo ship?** → 7 (initial probe said 6; verified 7 by listing dirs: composition-patterns / deploy-to-vercel / react-best-practices / react-native-skills / react-view-transitions / vercel-cli-with-tokens / web-design-guidelines).

6. **Per-skill license metadata coverage?** → 4 of 7 SKILL.md files declare `license: MIT` in YAML frontmatter (composition-patterns / react-best-practices / react-native-skills / react-view-transitions). 3 do NOT (deploy-to-vercel / vercel-cli-with-tokens / web-design-guidelines). Validates Pattern #29 29-absent-3 N=2 strengthening (also: README MIT claim + no LICENSE file at root + per-skill variation).

## Open / unresolved

7. **Why 4-of-7 skills declare license but 3 don't?** Hypothesis: skills imported from existing internal Vercel sources (vercel-cli-with-tokens / deploy-to-vercel / web-design-guidelines) are practical scripts where license metadata may be implicit; rule-aggregator skills (composition-patterns / react-best-practices / react-native-skills / react-view-transitions) make license explicit because content is curated rules. **Not verified — operator can ask Vercel.**

8. **What is `skills.sh` exactly?** Is it a Vercel-built registry or third-party? Homepage is `https://skills.sh/vercel-labs/agent-skills` but agentskills.io is the spec author. Likely independent project (analogous to npm vs Node.js). Not investigated further at v51.

9. **Will Vercel publish more skills?** Repo created 2025-12-08 (~4.5 months at v51); 7 skills. Cadence unclear. If Vercel scales to 30+ skills, would shift toward awesome-claude-skills v50 hybrid form-factor (Pattern #68).

10. **Does `vercel-deploy-claimable` pattern map cleanly to other commercial deployment platforms?** Could Netlify / Railway / Cloudflare Pages adopt similar claim-URL-as-funnel-terminus? Pattern #50 50a observation applies broadly but commercial-platform-claimable-deployment as architectural primitive is corpus-first at Vercel.

11. **Is the YAML `license:` field per-skill an emerging standard?** Or Vercel-specific? Compare with awesome-claude-skills v50 — different sub-skills there have different licenses too (some Apache-2.0, some not). Per-skill license metadata as YAML field may become #29 sub-variant if 2 more wikis exhibit.

12. **Why did `composition-patterns` skill rename to `vercel-composition-patterns` in YAML `name:` but the directory is `composition-patterns`?** Directory uses generic name; YAML uses Vercel-prefixed name for namespace disambiguation when published to Claude. Corpus-first observation: directory-name vs YAML-name divergence as namespace mechanism. Not registered (single observation; consolidation-forward).

13. **Does Vercel use these skills internally?** I.e., is this dogfooding or pure outreach? Repo scale (25.7K stars in 4.5 months) suggests external adoption-driven, but no internal-use evidence in README.

14. **How does claim-URL-deployment workflow handle abandoned previews?** vercel-deploy-claimable returns claim URL — but if user never claims, deployment lifecycle? Likely falls back to Vercel's standard preview-cleanup (24h or so). Beyond wiki scope.

15. **What does `argument-hint: <file-or-pattern>` (web-design-guidelines YAML) signal?** Likely a slash-command convention for Claude Code — first appearance in corpus. Could be Pattern #X candidate at N=2 if another skill exhibits.

## Strategic open questions (Storm Bear vault)

16. **Should Storm Bear adopt SKILL.md format for vault `05 Skills/` directory?** Currently vault uses prose markdown. SKILL.md YAML frontmatter (`name` + `description` + trigger phrases + on-demand loading) would be more agent-friendly. Direct pilot candidate.

17. **Should Storm Bear's vault CLAUDE.md adopt 22d identical-mirror approach (CLAUDE.md = AGENTS.md byte-for-byte)?** Pros: zero divergence risk. Cons: 2× storage; either file edit must mirror. Compare with 22a monolithic single-file (gh-aw v48) and 22c authoritative+shim (aidevops v47). Operator decision per v27 diagnostic HIGH item #1.

18. **Is `vercel-deploy-claimable` workflow applicable to Storm Bear publishing?** I.e., agent-deployed wiki preview → claim-URL transfer to operator account. Potential for vault-as-published-asset pipeline. Speculative.

19. **Should Storm Bear publish a public skill collection (analogous to vercel-labs/agent-skills) for Scrum coaching skills?** Aspirational; far from current state. Pattern #17 variant 5 reference for archetype if Storm Bear ever scales.

End of OPEN-QUESTIONS.
