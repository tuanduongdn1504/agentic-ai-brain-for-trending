# (C) Entity 2 — gsd-build Ecosystem + GSD-1 successor relationship

## gsd-build organization

| Field | Value |
|---|---|
| Org name | gsd-build |
| GitHub | https://github.com/gsd-build |
| Created | 2026-02-09 |
| Public repos | 8 (per probe data) |
| Homepage | gsd.build |
| Contact | contact@gsd.build |
| Discord | discord.com/invite/nKXTsAcmbT |

## Repos under gsd-build org (per brief probe)

The 8 repos in gsd-build include (some inferred from README + brief):
- **gsd-2** (this wiki subject; 6,619 stars; created 2026-03-11; v2.78.1)
- **get-shit-done** (GSD-1 predecessor; 57,396 stars per current probe vs 8K at v5 wiki publication; created earlier)
- Other repos likely include: docs / extension catalog / daemon-deployment / similar — not individually probed (would require additional API calls)

**Pattern #17 variant 1 strengthening**: gsd-build org has multi-repo ecosystem with **one viral flagship (GSD-1) + one active successor (gsd-2) + 6 supporting repos**. 19th+ data point for variant 1 (solo-or-small-team-multi-publisher).

## GSD-1 vs GSD-2 successor relationship

### From VISION.md (verbatim)

> ## Relationship to GSD-1
>
> GSD-2 is the future. GSD-1 continues to serve its community but GSD-2 is where active development, new features, and architectural investment happen. The goal is to eventually migrate GSD-1 users to GSD-2.

### From README headline

> **The evolution of [Get Shit Done](https://github.com/gsd-build/get-shit-done) — now a real coding agent.**

### Verbatim anti-positioning

> The original GSD went viral as a prompt framework for Claude Code. It worked, but it was fighting the tool — injecting prompts through slash commands, hoping the LLM would follow instructions, with no actual control over context windows, sessions, or execution.

### Migration tooling

`/gsd migrate` parses GSD-1's `.planning` directories → GSD-2's `.gsd/` format:
- Maps phases → slices, plans → tasks, milestones → milestones
- Preserves completion state (`[x]` phases stay done, summaries carry over)
- Consolidates research files
- Shows preview before writing
- Optionally runs agent-driven review of output for quality assurance
- Supports format variations including milestone-sectioned roadmaps with `<details>` blocks, bold phase entries, decimal phase numbering, duplicate phase numbers across milestones

## GSD-1 → GSD-2 transition: what we know vs don't know

### KNOWN (per repo evidence)
- gsd-build org owns BOTH repos
- gsd-2 explicitly cites GSD-1 as predecessor in README + VISION
- Migration tool exists (one-way GSD-1 → GSD-2)
- Both repos use $GSD Solana token branding
- GSD-2 ARCHITECTURALLY DIFFERENT (standalone CLI built on Pi SDK vs prompt framework injecting into Claude Code)

### UNKNOWN (honest gaps)
- **Author identity**: GSD-1 author = TÂCHES (per Storm Bear v5 wiki); GSD-2 LICENSE + ADRs = Lex Christopherson
  - Possible explanations: (a) same person under different identity; (b) handed off within org; (c) gsd-build org has multiple maintainers
  - **Documented in `00 OPEN-QUESTIONS.md` as Q1**
- **Migration adoption rate**: How many GSD-1 users have actually migrated? Not observable from gsd-2 repo alone.
- **GSD-1 sunset timeline**: VISION says "eventually migrate"; no specific date or end-of-support announcement observed
- **Whether GSD-1 receives ANY active development**: README says "continues to serve its community"; CHANGELOG only covers gsd-2; would need to check GSD-1 repo activity

## Pattern #58 NEW sub-variant 58e successor-repo-not-rename

**Sub-variant taxonomy after gsd-2 v54** (per Pattern #58 sub-variant evolution since v42 mini-audit):

| Sub-variant | Mechanism | N | Wikis |
|---|---|---|---|
| 58a | rename-without-npm-rename | 1 | OMC v27 (`oh-my-codex` → `oh-my-claudecode` repo, npm preserved) |
| 58b | rebrand-with-transitional-preserve | 1 | ruflo v42 (triple-package parallel distribution) |
| 58c | rebrand-repo-keep-npm-package | 1 | omo v52 (repo `oh-my-opencode` → `oh-my-openagent`, npm `oh-my-opencode` preserved + dual-bin alias) |
| 58d | feature-deprecation-with-public-discussion-notice | 1 | shannon v45 (`claude-code-router` router-mode sunset at Discussion #301) |
| **58e NEW** | **successor-repo-not-rename** (planned successor in NEW repo with explicit migration roadmap) | **1** | **gsd-2 v54** |

**Mechanism distinction for 58e**: Unlike 58a/b/c (single repo evolves), 58e creates a NEW repo for the successor while keeping the original repo alive. The original may receive minimal maintenance; the new repo absorbs active development. Migration path is explicit (tool + roadmap + VISION statement).

**Status**: N=1 stale-flagged; promotion-candidate at structural-N=2 if another corpus example emerges.

## Pattern #57 6th data point — explicit-vendored-package-metadata sub-variant

gsd-2's vendoring of pi-mono v36 packages is **strongest Pattern #57 evidence to date**. Prior data points:

| # | Wiki | Recursive citation type | Mechanism |
|---|---|---|---|
| 1 | OMC v27 | Self-aware citation (cites ECC v1 + Superpowers v2) | README acknowledgment |
| 2 | bizos v37 | Subject-built-with-corpus-tools | Apparent Claude-Code-built (4 inferential signals) |
| 3 | ollama v46 | Compound-2-wiki cross-corpus citation | Pi integration doc cites pi-mono v36 + autoresearch v10 |
| 4 | aidevops v47 | CREDITS.md cites awesome-design-md v25 + Google Stitch | 3rd-party-unaware-recursive |
| 5 | awesome-claude-skills v50 | Aggregator-mediated multi-citation | obra/superpowers cited 5× + anthropics/skills cited 5× |
| 6 | vercel-labs v51 | Forward-citation-then-wiki | multica v15 cited Vercel agent-skills 36 wikis BEFORE v51 wiki built |
| **7** | **gsd-2 v54** | **Explicit-vendored-package-metadata** | 4 packages with `package.json` description "vendored from pi-mono" verbatim |

(Note: brief said 5th data point; actual count post-v51/v52 = ~6th-7th depending on whether sub-variants are counted as separate observations vs strengthening. **Honest verdict**: gsd-2 = 6th or 7th Pattern #57 data point; routine v2.1 mini-audit can clarify counting convention.)

**Sub-variant 57d candidate**: machine-readable-vendoring-metadata — distinct from narrative citation (57a) / aggregator-mediated (57b) / forward-citation-then-wiki (57c).

**Why it's strongest**: package.json metadata is **searchable + deterministic + ungameable**. A future analyst can grep `"vendored from"` across all corpus and find this evidence without ambiguity. Other Pattern #57 data points required narrative interpretation.

## Pattern #50 watch — multi-component infrastructure

gsd-build's component architecture suggests potential commercial-cloud-tier emergence (see `(C) Cluster 3` for full table). Currently observational watch — no Pro tier advertised in README. **Sister to ruflo v42 + rowboat v43 + shannon v45 multi-component commercial-funnels but at gsd-build = no advertised paid tier yet.**

## Cross-corpus connections summary

| Corpus wiki | Connection to gsd-2 |
|---|---|
| **pi-mono v36** | gsd-2 vendors 4 of 7 pi-mono packages with explicit "vendored from pi-mono" metadata |
| **get-shit-done v5 (GSD-1)** | gsd-2 = explicit planned successor with migration tool + roadmap |
| **spec-kit v17** | SDD methodology peer (Pattern #21 un-stale candidate) |
| **aidevops v47** | SDD-elements-shared peer (Pattern #21 un-stale candidate) |
| **system-prompts-leaks v21** | Pattern #37 N=1 source ($GSD token N=2 here) |
| **gh-aw v48** | Pattern #66 by-design defense N=1 source (managed RTK binary + telemetry-discipline N=2 here) |
| **OMC v27** | Pattern #58 58a precedent (gsd-2 = 58e NEW sub-variant) |
| **ollama v46** | Pi integration via gsd-2 Ollama extension (`Ollama` bundled extension #19) — bidirectional ecosystem reinforcement |

## Storm Bear pilot relevance ranking (post-v54)

**LOW-MEDIUM observational + MEDIUM-HIGH conditional**:

- **NOT in top-11 pilot ranking** — Storm Bear vault use case (Markdown-knowledge-vault Scrum coach) does not directly need autonomous coding agent
- **Conditional MEDIUM-HIGH**: If Storm Bear ever spins up custom Scrum-tool development (e.g. internal Scrum dashboard / agent assistant for retros), gsd-2 is **strong candidate** for that work specifically — direct successor to GSD-1 which Storm Bear v5 evaluated
- **Architectural reference HIGH**: state-machine-from-disk + extension-first + worktree forensics + structured journal events are direct vault-routine-v2.2 candidate templates (see `(C) Entity 4`)
- **Avoidance criteria**: $GSD Solana token presence requires Storm Bear ethical evaluation if commercializing on top of gsd-2 (probably acceptable if Storm Bear doesn't endorse the token explicitly)

## Cross-references

- See `(C) Cluster 1` for README + VISION + GSD-1 anti-positioning verbatim
- See `(C) Entity 1` for core product capabilities
- See `(C) Entity 3` for Pi SDK cross-corpus deep-dive
- See `(C) Entity 4` for Storm Bear meta-entity vault-architectural lessons
- See `00 OPEN-QUESTIONS.md` Q1-Q2 for authorship identity questions
