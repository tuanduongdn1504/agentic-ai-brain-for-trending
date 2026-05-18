# (C) Open questions — zero (vercel-labs) wiki v68

20-30 questions to drive cluster summaries + entity pages.

## On the language design

1. What does "agent-first" actually mean structurally in Zero's syntax? Is there a syntactic construct that prefers agent-readability over human-readability? (Or is "agent-first" purely about tooling and learnability, not syntax?)
2. The README says "a small, regular language surface that agents can pick up quickly from examples." What's the surface size relative to Python / JavaScript / Go? Is there a numerical claim?
3. "Standard-library depth: common capabilities should live in documented, coherent library APIs instead of scattered dependency stacks." Is there a stdlib coverage doc enumerating what's covered?
4. "Regularity over syntax: prefer one obvious way to express most things." Is this stated as a hard policy or aspiration? Does it translate to specific syntactic choices?
5. Why C as the primary implementation language (65.9%)? Is the bootstrap compiler written in C, with later compiler-zero/ self-hosting?

## On the compiler architecture

6. What's in `native/zero-c/` vs `compiler-zero/`? The former is the native C bootstrap compiler; the latter is the Zero-authored self-hosted compiler. Are both functional, or is compiler-zero/ aspirational?
7. The release workflow in AGENTS.md says: "Bump the release version in `package.json`, `package-lock.json`, `docs-site/package.json`, `extensions/vscode/package.json`, and `native/zero-c/src/main.c`." This is 5-file manifest-drift discipline (matches Pattern #81 candidate from v66!). Is there CI enforcement?
8. What targets does `zero build --emit` support? README mentions `--target linux-musl-x64` and `wasm32-web`. Full target list?
9. Native test sandbox via `@vercel/sandbox` dependency — why does Zero need vendor-specific sandboxing for its native tests? Security or determinism concern?
10. The `bin/zero` script is the user-facing CLI entrypoint. How does it dispatch between native compiler binary, JS scripts, and Zero-authored compiler?

## On the skills protocol integration (Phase 4b PRIMARY area)

11. The skills/zero/SKILL.md is intentionally thin and says: "Do not treat it as the full Zero workflow." Why this choice — what problem with traditional skill packaging does this solve?
12. `zero skills list` enumerates inner skills (zero-agent, zero-language, zero-diagnostics, zero-packages, zero-builds, zero-testing, zero-stdlib). Where do these live in the repo? In `skill-data/`?
13. Are inner skills version-matched to the compiler binary — meaning when you upgrade Zero, the skills change with it?
14. Does this approach work with existing skill managers (Claude Code's skills plugin, Cursor's, etc.) or does it require special skill-manager support to invoke `zero skills get ...`?
15. Is this corpus-first or has any prior corpus subject done similar "skill-protocol-as-binary-bootstrap"?

## On the pre-1.0 + safety framing

16. "Security vulnerabilities should be expected. Zero is not ready for production." Repeated in README + AGENTS.md = Pattern #83 honest-deficiency-disclosure. Is there a SECURITY.md? Has any CVE / vuln been formally disclosed for Zero?
17. AGENTS.md says: "Do not preserve legacy behavior by default. Prefer the clearer agent-facing design over compatibility shims, migration layers, or carrying old paths forward." This is a strong stance. How does Zero handle deprecation when breaking changes happen?
18. "Treat generated artifacts and examples as experimental unless they have been reviewed for the specific environment where they will run." Is this a CI-enforced annotation or just policy?

## On the velocity + community

19. 91 commits + 3 releases + 2.1K stars in **2 days**. What's the announcement channel that drove this velocity? Vercel main account on X? HN frontpage? Conference launch?
20. The CHANGELOG names contributors per release (`@ctate @badlogic @chenrui333 @heylakatos @onevcat` for v0.1.2). Are these Vercel employees or external community?
21. AGENTS.md says: "Releases are manual, single-branch affairs. The maintainer controls the changelog voice and format." Who is "the maintainer"? `@ctate` (Charlie Tate?) per release-branch naming convention `ctate/v0.1.1`?
22. How does community-PR discipline work? CONTRIBUTING.md exists? AGENTS.md has tone guidance but no PR process — is there a separate PR template?

## On Vercel umbrella positioning

23. vercel-labs is the experimental sub-org. What's its relationship to vercel main? Lab → main graduation pipeline? Independent experimentation?
24. v51 agent-skills-of-vercel was in main vercel org; v68 zero is in vercel-labs. Is there other agent-related tooling in vercel-labs?
25. Does Zero integrate with Vercel's broader product line (Next.js, Vercel deployment, Vercel AI SDK)? Or is it strictly an independent language experiment?

## Pattern Library implications

26. NEW T1 sub-archetype "programming-language-as-agent-substrate" — provisional T1 extension OR motivation for NEW Tier T6 Language/Runtime at v69 audit?
27. Pattern #52 EXTREME-VIRAL sustained-velocity-test addition: zero v68 at 1,050 stars/day is 2-day window; v69 audit (~6mo+ window) evaluates whether velocity sustains. What's the expected outcome — Vercel Labs experiments typically have short hype windows?
28. Pattern #83 N=4 evidence strengthening: when zero declares "Security vulnerabilities should be expected" — is that a Pattern #83 instance? Or is "expected" weaker than "known"? Pattern #83 criterion (3) "Does NOT minimize" — does "expected" minimize or honestly disclose?
29. NEW observational candidate "Self-Hosted Compiler Bootstrap" — is this Pattern-shaped or just a classic compiler engineering pattern that's interesting only because it's corpus-first?
30. NEW observational candidate "Version-Matched-Compiler-Served Skill Content" — does this motivate any reform of how the vault thinks about skill versioning? Or is it purely an observation about Zero specifically?
