# (C) Entity Page — Core Skill Collection (7 Vercel-Engineering-authored skills)

**Type:** Core product entity
**Tier:** T1 Agent-as-assistant — corporate-narrow-skill-library sub-archetype
**Source:** vercel-labs/agent-skills repo (`00 Source/agent-skills/`)
**Cross-refs:** awesome-claude-skills v50 (curation contrast) / aidevops v47 (Pattern #22 22c) / gh-aw v48 (Pattern #22 22a) / pi-mono v36 (T1 monorepo) / claude-howto v32 (T1 tutorial) / claude-code-best-practice v34 (T1 best-practice aggregator) / claude-hud v35 (T1 display utility) / multica v15 (forward-citation source — Pattern #57 57c)

---

## 1. Identity (verbatim)

**Repo:** `vercel-labs/agent-skills`
**Tagline:** *"Vercel's official collection of agent skills"*
**README first line:** *"A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities."*
**Format reference:** *"Skills follow the [Agent Skills](https://agentskills.io/) format."*

## 2. Core product

7 SKILL.md files spanning 1,367 lines of agent instructions. Each skill is a self-contained markdown document with YAML frontmatter (`name`, `description`, optional `license` + `metadata`) + bash scripts (where applicable) + supporting `references/` or `rules/` directories.

**Distinct from awesome-claude-skills v50 aggregator:** Vercel agent-skills is an **author-built collection**, not a curation. All 7 skills authored by Vercel Engineering (per README + per YAML `metadata.author: vercel` for all 7).

## 3. Skill catalog

### Rule-aggregator skills (5 of 7 — declarative content)

| # | Skill | YAML name | Lines | Domain | Rule count |
|---|---|---|---|---|---|
| 1 | composition-patterns | `vercel-composition-patterns` | 89 | React component architecture | ~7+ rules with `architecture-` / `state-` / `patterns-` / `react19-` prefix taxonomy |
| 2 | react-best-practices | `vercel-react-best-practices` | 149 | React/Next.js performance | 70 rules across 8 categories (waterfalls / bundle / SSR / data fetch / re-render / rendering / JS micro / 8th unstated) |
| 3 | react-native-skills | `vercel-react-native-skills` | 121 | React Native + Expo | 16 rules across 7 sections (perf / layout / animation / images / state / arch / platform) |
| 4 | react-view-transitions | `vercel-react-view-transitions` | 320 | View Transition API | `<ViewTransition>` + `addTransitionType` + CSS pseudo-elements + Next.js `transitionTypes` |
| 5 | web-design-guidelines | `web-design-guidelines` (no `vercel-` prefix) | 39 | UI/UX/a11y audit | 100+ rules across 11 categories (accessibility / focus / forms / animation / typography / images / perf / nav / dark mode / touch / i18n) |

### Practical-script skills (2 of 7 — imperative actions)

| # | Skill | YAML name | Lines | Domain | Maturity |
|---|---|---|---|---|---|
| 6 | deploy-to-vercel (README label: vercel-deploy-claimable) | `deploy-to-vercel` | 296 | Agentic Vercel deployment with claim-URL ownership transfer | **v3.0.0 — most mature in repo** |
| 7 | vercel-cli-with-tokens (not in README list) | `vercel-cli-with-tokens` | 353 | Token-authenticated Vercel CLI workflows | v1.0.0 |

**5:2 split** weighted toward declarative rule-aggregator. Vercel's strategic emphasis: **content-as-skill** (capture engineering best-practice) over **action-as-skill** (operational tasks). Both genres ship side-by-side.

## 4. Authorship (Pattern #19 archetype 4 strengthening)

**Verbatim attribution:** *"from Vercel Engineering"* (README §react-best-practices)

**YAML metadata:** All 7 skills declare `metadata.author: vercel`

**No individual lineage cited** — neither in README nor in any SKILL.md. Pattern #19 archetype 4 (no-explicit-individual-lineage) strengthening at corporate-collective level. Joins:
- magika v44: "Google Research Anti-Abuse team" (corporate-research-team)
- gh-aw v48: GitHub corporate (no individual authors cited)
- Vercel v51: "Vercel Engineering" (corporate-collective)

Distinct from individual-lineage corpus wikis (Karpathy v10, John Lam v17, etc.).

## 5. Per-skill structure conventions

All skills follow:
- `<skill-dir>/SKILL.md` (REQUIRED — agent-loaded definition with YAML frontmatter)
- `<skill-dir>/scripts/` (OPTIONAL — bash automation)
- `<skill-dir>/references/` or `<skill-dir>/rules/` (OPTIONAL — supporting docs)
- `<skill-dir>.zip` at sibling level (REQUIRED per AGENTS.md, but only 5 of 7 actually shipped)

Most-elaborate skill structure: **composition-patterns** ships its own AGENTS.md + README.md + metadata.json + rules/ INSIDE the skill directory (sub-skill governance).

## 6. SKILL.md format spec compliance

Per repo AGENTS.md/CLAUDE.md (identical-mirror; see Cluster 2):

**REQUIRED YAML fields:** `name`, `description` (with trigger phrases)
**OPTIONAL YAML fields observed:** `license`, `metadata.author`, `metadata.version`, `argument-hint`

**Best practices (verbatim):**
> *"Keep SKILL.md under 500 lines"*

**Verified compliance:** All 7 skills under 500 lines (max 353 = vercel-cli-with-tokens).

**On-demand loading:**
> *"Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant."*

This is the architectural primitive that allows scale: 7 skills × ~500 lines × 0 startup-context-cost = no startup penalty regardless of catalog size.

## 7. Trigger-phrase activation convention (corpus-first verbatim user-quotes)

Skills activate via verbatim user-quote trigger phrases declared in YAML `description`:

| Skill | Trigger phrases (verbatim) |
|---|---|
| deploy-to-vercel | *"Deploy my app"*, *"Deploy this to production"*, *"Push this live"*, *"Deploy and give me the link"*, *"create a preview deployment"* |
| vercel-cli-with-tokens | *"deploy to vercel"*, *"set up vercel"*, *"add environment variables to vercel"* |
| web-design-guidelines | *"Review my UI"*, *"Check accessibility"*, *"Audit design"*, *"Review UX"*, *"Check my site against best practices"* |
| react-view-transitions | API-specific: *"`startViewTransition`"*, *"`ViewTransition`"*, *"transition types"* |
| composition-patterns | Task-described: *"Refactoring components with boolean prop proliferation"* |
| react-best-practices | Task-described: *"writing, reviewing, or refactoring React/Next.js code"* |
| react-native-skills | Task-described: *"building React Native components, optimizing list performance"* |

**Two trigger styles:**
1. **End-user quote-style:** *"Deploy my app"* — verbatim natural-language phrases users actually say
2. **API-reference style:** *"`startViewTransition`"* — technical terms users mention when working in domain
3. **Task-description style:** *"writing, reviewing, or refactoring..."* — paraphrased work-context

Most skills mix all three styles in the description.

## 8. Per-skill license metadata variation (Pattern #29 29-absent-3 N=2)

| Skill | YAML `license:` declared? |
|---|---|
| composition-patterns | ✅ MIT |
| react-best-practices | ✅ MIT |
| react-native-skills | ✅ MIT |
| react-view-transitions | ✅ MIT |
| deploy-to-vercel | ❌ |
| vercel-cli-with-tokens | ❌ |
| web-design-guidelines | ❌ |

**Repo-level state:**
- ❌ No `LICENSE` file at root
- ✅ README §License says "MIT"

**Pattern #29 29-absent-3 strengthening (N=1 → N=2):**
- v50 awesome-claude-skills: 29-absent-3 N=1 stale-flagged at registration (per-skill license variation; some sub-skills LICENSE.txt'd)
- v51 vercel-labs/agent-skills: 29-absent-3 N=2 (per-skill YAML `license:` variation; absent root LICENSE; README OSI MIT claim)

**Promotion-candidate at next mini-audit:** structural-N=2 criterion clear (both wikis exhibit 3-property signature: absent root LICENSE + README OSI claim + per-skill license metadata variation).

## 9. Per-skill semantic versioning

All 7 skills declare YAML `metadata.version`:
- 6 at v1.0.0 (initial release maturity)
- **deploy-to-vercel at v3.0.0** (most mature)

3 major versions on deploy-to-vercel suggests v1 → v2 → v3 evolution within the 4.5-month repo lifespan. Other skills appear stable at initial release.

## 10. Build tooling (`packages/react-best-practices-build/`)

Single-skill build pipeline: compiles per-rule MD files into the consolidated `react-best-practices/SKILL.md`.

Implication: Vercel intends rule-aggregator skills to scale via build-pipeline (per-rule source-of-truth → SKILL.md output) rather than hand-maintenance of consolidated SKILL.md.

Currently only `react-best-practices` has documented build tooling. composition-patterns has structural readiness (rules/ directory + AGENTS.md "full compiled document" reference) but no separate build package.

## 11. Pattern Library impact (this entity contributes)

| Pattern | Action |
|---|---|
| #17 variant 5 ecosystem-scale commercial platform | N=3 default-criterion strengthening (HuggingFace + Microsoft + Vercel) |
| #19 archetype 4 corporate-collective lineage | Strengthening (Vercel Engineering corporate-collective; joins magika v44 + gh-aw v48) |
| #22 22d identical-mirror | NEW sub-variant N=1 stale-flagged registration (verified via `diff` zero-output) |
| #29 29-absent-3 | N=2 strengthening (per-skill license metadata variation; absent root LICENSE; README OSI claim) |
| #50 50a claim-URL-as-funnel-terminus | Observational data point (vercel-deploy-claimable bipartite preview-URL + claim-URL) |
| #57 57c forward-citation-then-wiki | NEW sub-variant N=1 stale-flagged registration (multica v15 cited "Vercel agent-skills import (first)" 36 wikis pre-v51) |
| #59 npx-skills-add observational | Sub-variant within Pattern #59 (3rd-party non-Anthropic registry install verb) |
| #18 MCP corporate-official-tier-absent | Counter-evidence observational |
| #27 corporate-amplified-organic | Sub-path strengthening (~5,700 stars/mo at 4.5mo) |
| #2 4-surface install | Standard-T1 observation (npx skills + manual cp + paste-to-claude.ai + per-skill zip) |

## 12. Storm Bear vault relevance

**Direct utility (HIGH for SKILL.md format reference):** Vercel's SKILL.md format spec (YAML frontmatter + trigger phrases + 500-line cap + on-demand loading + scripts-not-inline + bash conventions) is the **most-direct corpus template for Storm Bear vault `05 Skills/` directory expansion**. Currently vault skills (e.g., `llm-wiki-routine-v2.1.md`, `llm-wiki-ingest.md`, `brain-setup.md`) are prose markdown without YAML frontmatter. Adopting Vercel-style YAML frontmatter would:
- Enable trigger-phrase-based skill activation (vs current "manually invoke skill")
- Enable on-demand loading (vs current "always loaded")
- Enable per-skill versioning + license metadata (vs current implicit)

**Pilot proposal:** Convert 1 vault skill to Vercel-style SKILL.md format as proof-of-concept. Likely candidate: `llm-wiki-routine-v2.1.md` (the most-invoked skill).

**Indirect utility (MEDIUM):**
- claim-URL deployment workflow as agentic-pattern reference (not directly applicable to Scrum coach role)
- Per-rule prefix-namespace (composition-patterns `architecture-` / `state-` / `patterns-` / `react19-`) as taxonomy reference if vault skills scale

**No direct utility:**
- React/Next.js/React Native rule-aggregator skills are domain-mismatched with markdown-vault (no UI code)

## 13. Tradeoffs + caveats

**Strengths:**
- High SKILL.md quality + format-spec compliance
- Production-grade vercel-deploy-claimable workflow with thoughtful state-detection logic
- Light governance enables fast iteration (4.5 months → 25.7K stars + 7 skills + v3.0.0 maturity on deploy-to-vercel)
- Corporate-amplified-organic distribution (no aggressive marketing observed; growth via Vercel ecosystem reach)

**Caveats:**
- Light governance gaps (no SECURITY / CONTRIBUTING / CoC / LICENSE-file)
- Per-skill license metadata variation (3 of 7 skills lack `license:` declaration)
- Skill scope is narrow to React/Next.js/Vercel ecosystem (not generic agent skills)
- README label vs YAML name vs directory name divergence (3 conventions per skill)
- AGENTS.md "REQUIRED zip" + "REQUIRED scripts/" partially aspirational (composition-patterns + react-native-skills missing zips; rule-aggregator skills have rules/ not scripts/)
- Slight positioning drift: README says "AI coding agents" (broader); AGENTS.md says "Claude.ai and Claude Code" (Anthropic-specific)
- Slight positioning drift: AGENTS.md says skills are "for working with Vercel deployments" but only 2 of 7 are Vercel-specific

**Forward-looking:**
- If skill catalog scales to 30+, repo will resemble awesome-claude-skills v50 hybrid form-factor (Pattern #68 awesome-list-genre)
- Currently structurally distinct from #68 (no curation; only Vercel-Engineering-authored)
- Build pipeline (`packages/react-best-practices-build/`) may extend to other rule-aggregator skills

End of entity page.
