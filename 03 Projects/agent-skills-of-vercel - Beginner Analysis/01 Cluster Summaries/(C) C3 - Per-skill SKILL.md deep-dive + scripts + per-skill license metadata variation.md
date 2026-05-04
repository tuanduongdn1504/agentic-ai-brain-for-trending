# (C) Cluster Summary 3 — Per-skill SKILL.md deep-dive + scripts + per-skill license metadata variation

**Source files:** 7 SKILL.md files at `00 Source/agent-skills/skills/<name>/SKILL.md` (1,367 lines total)
**Cluster theme:** Per-skill technical scope + script integration + per-skill license metadata variation + corpus-first observations

---

## YAML frontmatter analysis (per-skill license metadata variation)

| Skill | YAML name | YAML license | YAML version | YAML author | Other YAML fields |
|---|---|---|---|---|---|
| composition-patterns | `vercel-composition-patterns` | ✅ MIT | 1.0.0 | vercel | — |
| deploy-to-vercel | `deploy-to-vercel` | ❌ | 3.0.0 | vercel | — |
| react-best-practices | `vercel-react-best-practices` | ✅ MIT | 1.0.0 | vercel | — |
| react-native-skills | `vercel-react-native-skills` | ✅ MIT | 1.0.0 | vercel | — |
| react-view-transitions | `vercel-react-view-transitions` | ✅ MIT | 1.0.0 | vercel | — |
| vercel-cli-with-tokens | `vercel-cli-with-tokens` | ❌ | 1.0.0 | vercel | — |
| web-design-guidelines | `web-design-guidelines` | ❌ | 1.0.0 | vercel | `argument-hint: <file-or-pattern>` |

**Per-skill license metadata variation observed:**
- 4 skills declare `license: MIT` in YAML frontmatter
- 3 skills do NOT declare `license:` — fall back to repo-level README MIT claim
- No skill declares non-MIT license in YAML

**Pattern observation:** Rule-aggregator skills (composition-patterns / react-best-practices / react-native-skills / react-view-transitions) consistently declare license; practical-script skills (deploy-to-vercel / vercel-cli-with-tokens / web-design-guidelines) do not. Possible explanation: rule-aggregator content is curated with explicit IP framing; practical scripts are operational utilities where IP framing is implicit.

**Pattern #29 29-absent-3 N=2 strengthening:**
- v50 awesome-claude-skills: 29-absent-3 N=1 (per-skill license variation observed at sub-component scale: 9 of 31 top-level skills have per-skill LICENSE.txt; YAML frontmatter `license:` for some)
- v51 vercel-labs/agent-skills: 29-absent-3 N=2 (4 of 7 SKILL.md files declare `license:` in YAML)

**Promotion-candidate at next mini-audit:** 29-absent-3 N=2 structural-unambiguous-at-N=2 criterion clear (both wikis exhibit absent-LICENSE-file + README-OSI-license-claim + per-skill-license-metadata-variation as 3-property structural signature).

## Per-skill SKILL.md scope deep-dive

### 1. composition-patterns (`vercel-composition-patterns`, 89 lines SKILL.md)

**Architecture:** Slim SKILL.md → cites per-rule `rules/` directory + full compiled `AGENTS.md`

**Rule prefix taxonomy (corpus-first per-rule prefix-namespace):**
- `architecture-` (HIGH priority): `architecture-avoid-boolean-props`, `architecture-compound-components`
- `state-` (MEDIUM priority): `state-decouple-implementation`, `state-context-interface`, `state-lift-state`
- `patterns-` (MEDIUM priority): `patterns-explicit-variants`, `patterns-children-over-render-props`
- `react19-` (MEDIUM priority): `react19-no-forwardref`

**Per-skill structure (most-elaborate among 7):**
- `SKILL.md` (entry point — 89 lines)
- `AGENTS.md` (skill-level — separate from repo-level AGENTS.md)
- `README.md` (skill-level)
- `metadata.json` (machine-readable skill metadata)
- `rules/` (per-rule MD files)

**Corpus-first observation:** Per-skill `metadata.json` + skill-level AGENTS.md/README — most-structured skill in the 7. Hints at scaling pattern for rule-aggregator skills.

### 2. deploy-to-vercel (296 lines, v3.0.0 — most mature)

**4-step decision tree:**

**Step 1: Gather Project State** (4 parallel checks):
```bash
git remote get-url origin                                # check git remote
cat .vercel/project.json || cat .vercel/repo.json        # check Vercel link
vercel whoami                                            # check CLI auth
vercel teams list --format json                          # list teams
```

**Step 2: Choose Deploy Method** (decision matrix based on Step 1 outputs):
- Linked + git remote → **Git Push** (preferred path; triggers Vercel auto-deploy)
- Linked + no git → **Vercel CLI** (`vercel deploy --prebuilt`)
- Not linked + git remote → **Import via dashboard prompt**
- Not linked + no git → **Claimable deployment** (the corpus-first pattern)

**Step 3: Execute** (per chosen method)

**Step 4: Return preview URL + claim URL**

**Claim URL workflow (corpus-first deployment-claim-mechanism):**

```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...
```

User visits claim URL → authenticates with Vercel account → deployment ownership transfers from ephemeral agent-deploy account to user's permanent Vercel account. Solves the chicken-and-egg of "agent doesn't have my Vercel auth so deploy must be ephemeral, but I want permanent ownership."

**Pattern #50 50a observational data point:** claim-URL-as-funnel-terminus is the strongest observed deployment-claim-mechanism in the corpus.

**Team selection logic (verbatim partial):**
> *"If the user belongs to multiple teams, present all available team slugs as a bulleted list and ask which one to deploy to. Once the user picks a team, proceed immediately to the next step — do not ask for additional confirmation."*

Hints at Vercel's UX bias: ask once, proceed efficiently. Pass team via `--scope` on all subsequent CLI calls.

**Safety guard (verbatim):**
> *"Always deploy as preview (not production) unless the user explicitly asks for production."*

**Note:** also explicitly forbids `vercel project inspect` / `vercel ls` / `vercel link` in unlinked directories (will silently link as side-effect). Only `vercel whoami` is "safe to run anywhere."

### 3. react-best-practices (149 lines, with separate `packages/react-best-practices-build/` build tooling)

**70 rules across 8 categories** (SKILL.md spec; README claims 40+):
1. **Eliminating Waterfalls** (Critical) — fetch parallelization, route-level prefetch
2. **Bundle Size** (Critical) — code splitting, lazy loading, tree shaking
3. **Server-side Performance** (High) — RSC vs Client, streaming
4. **Client-side Data Fetching** (Medium-High) — SWR, React Query, mutation patterns
5. **Re-render Optimization** (Medium) — memo, useMemo, useCallback
6. **Rendering Performance** (Medium) — virtualization, batching
7. **JavaScript Micro-optimizations** (Low-Medium) — primitive ops, allocation patterns
8. (8th category implied by SKILL.md but not enumerated in README)

**Build pipeline:** `packages/react-best-practices-build/` compiles per-rule MD files into consolidated SKILL.md. Single skill with documented build pipeline.

### 4. react-native-skills (`vercel-react-native-skills`, 121 lines)

**16 rules across 7 sections** (smaller than react-best-practices):
- Performance (Critical): FlashList vs FlatList, memoization, heavy compute via runOnJS
- Layout (High): flex patterns, safe areas, keyboard avoidance
- Animation (High): Reanimated 3+, gesture handler patterns
- Images (Medium): expo-image, caching strategies, lazy loading
- State (Medium): Zustand patterns, React Compiler integration
- Architecture (Medium): monorepo structure, imports
- Platform (Medium): iOS/Android specific patterns

**Mobile-specific scope** — only React Native skill in the 7. Distinct from web-focused composition-patterns + react-best-practices + react-view-transitions + web-design-guidelines.

### 5. react-view-transitions (320 lines — largest rule-aggregator)

**Domain:** Browser-native View Transition API for React/Next.js
- `<ViewTransition>` component (corpus-first React 19 API documentation in skill format)
- `addTransitionType` — directional/context-specific animations
- View Transition Classes + CSS pseudo-elements (`::view-transition-group`, `::view-transition-image-pair`)
- Shared element transitions via `name` prop (list-to-detail morphing)
- JavaScript animations via Web Animations API
- Next.js `transitionTypes` prop on `next/link` (Vercel framework integration)
- Ready-to-use CSS animation recipes (fade, slide, scale, flip)
- Accessibility: `prefers-reduced-motion`

**React 19 + Next.js App Router specific** — newest skill in terms of API recency.

### 6. vercel-cli-with-tokens (353 lines — largest SKILL.md)

**Token-authenticated CLI workflow** (vs interactive `vercel login`):

**Step 1: Locate the Vercel Token** — works through 4 scenarios in order:
1. Token in user's environment (`VERCEL_TOKEN` env var)
2. Token from CI secrets
3. Token from teammate-shared password manager
4. Token to be newly generated at vercel.com/account/tokens

**Step 2: Set up token auth** for subsequent commands.

**Step 3: Common operations** with token (deploy, env vars, project linking, env-set, link --repo).

**Step 4: Token security guidance** (don't commit, rotate periodically, use `--scope` for team isolation).

**Companion skill to deploy-to-vercel:** Provides token primitives; deploy-to-vercel uses them as building block.

### 7. web-design-guidelines (39 lines — smallest)

**Smallest SKILL.md** — basically a manifest pointing at separate rules.

**11 rule categories** (100+ rules total, per README):
- Accessibility (aria-labels, semantic HTML, keyboard handlers)
- Focus States (visible focus, focus-visible patterns)
- Forms (autocomplete, validation, error handling)
- Animation (prefers-reduced-motion, compositor-friendly transforms)
- Typography (curly quotes, ellipsis, tabular-nums)
- Images (dimensions, lazy loading, alt text)
- Performance (virtualization, layout thrashing, preconnect)
- Navigation & State (URL reflects state, deep-linking)
- Dark Mode & Theming (color-scheme, theme-color meta)
- Touch & Interaction (touch-action, tap-highlight)
- Locale & i18n (Intl.DateTimeFormat, Intl.NumberFormat)

**Corpus-first YAML field `argument-hint: <file-or-pattern>`** — slash-command argument hint convention. Tells Claude how to expect arguments when invoking the skill (analogous to bash command-line arg hints).

## Skill scope taxonomy

| Type | Skills | Characteristic |
|---|---|---|
| **Rule-aggregator (declarative)** | composition-patterns / react-best-practices / react-native-skills / react-view-transitions / web-design-guidelines (5/7) | Curated rules; "review for compliance" workflow; explicit `license: MIT` for 4/5 (web-design-guidelines exception); per-rule prefix-namespace (composition-patterns) |
| **Practical-script (imperative)** | deploy-to-vercel / vercel-cli-with-tokens (2/7) | Bash workflows; "do this thing" workflow; no `license:` field; v3.0.0 maturity (deploy-to-vercel) |

**5:2 split** weighted toward declarative rule-aggregator. Vercel's strategic emphasis is **content-as-skill** (capture engineering best-practice rules) rather than pure **action-as-skill** (do operational tasks).

## Cross-skill conventions

**Skill activation:** YAML `description:` includes trigger phrases (verbatim quotes from user) → agent matches user input against trigger phrases → activates skill on match.

**Example trigger phrases observed:**
- deploy-to-vercel: "Deploy my app", "Deploy this to production", "Push this live", "Deploy and give me the link", "create a preview deployment"
- vercel-cli-with-tokens: "deploy to vercel", "set up vercel", "add environment variables to vercel"
- web-design-guidelines: "Review my UI", "Check accessibility", "Audit design", "Review UX", "Check my site against best practices"
- react-view-transitions: extensive trigger list including specific API references ("`startViewTransition`", "`ViewTransition`", "transition types")

**Convention:** Trigger phrases are written from end-user perspective + sometimes include API/term references for technical specificity. Discoverability mechanism.

## packages/react-best-practices-build/ build tooling

Contents (probed):
- Build script likely TypeScript/JavaScript that processes per-rule MD files
- Outputs: consolidated SKILL.md (149 lines) for distribution

Single-skill build tooling. May extend to other rule-aggregator skills as Vercel scales the catalog.

## Pattern Library observations (Phase 2 cluster discipline)

**Per-skill license metadata variation strengthening:**
- **#29 29-absent-3 N=2 strengthening** — vercel-labs/agent-skills exhibits all 3 properties of 29-absent-3 sub-context (absent LICENSE + README OSI claim + per-skill license variation)

**Per-skill semantic versioning:**
- All skills declare YAML `version:` (deploy-to-vercel at 3.0.0 mature; others at 1.0.0)
- Reinforces Pattern #58 Branding-Package Divergence observation: per-skill independent versioning within same repo

**YAML field expansion:**
- `argument-hint:` corpus-first (web-design-guidelines)
- `license:` per-skill variation
- `metadata.author` + `metadata.version` consistent

**Trigger-phrase convention:**
- Verbatim user-quote trigger phrases — Pattern #59 (Plugin Marketplace Native) sub-observation: skills use natural-language activation rather than slash-commands

**Counter-evidence to skills-as-MCP:**
- All 7 skills are pure SKILL.md + bash + claude.ai/Code direct
- No skill exposes MCP tools
- Pattern #18 corporate-official-tier MCP-absent-altogether reinforced

**Absences (informative):**
- No tests for any skill (no `tests/` directory in any skill)
- No CI for skill validation
- No skill-level CONTRIBUTING / SECURITY

## Cluster summary verdict

Cluster 3 reveals **per-skill license metadata variation** (Pattern #29 29-absent-3 N=2 strengthening), **rule-aggregator-vs-practical-script 5:2 skill scope taxonomy** (Vercel emphasizes content-as-skill over action-as-skill), **claim-URL-as-funnel-terminus deployment workflow** (Pattern #50 50a observational), **per-rule prefix-namespace at composition-patterns** (corpus-first), and **`argument-hint:` YAML field corpus-first** (web-design-guidelines). Skills under 500-line cap discipline (max 353); on-demand loading well-respected. SKILL.md format spec is well-documented in repo-level AGENTS.md but PARTIALLY aspirational (composition-patterns + react-native-skills missing zips; 3 of 7 missing per-skill license metadata).
