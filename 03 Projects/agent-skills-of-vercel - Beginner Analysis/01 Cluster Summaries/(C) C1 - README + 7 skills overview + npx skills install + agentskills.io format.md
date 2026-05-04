# (C) Cluster Summary 1 — README + 7 skills overview + npx skills install + agentskills.io format

**Source files:** `00 Source/agent-skills/README.md` (170 lines)
**Cluster theme:** User-facing positioning + skill catalog + installation + format reference

---

## Verbatim positioning

Title: **"Agent Skills"**

Tagline (verbatim): *"A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities."*

Format reference (verbatim): *"Skills follow the [Agent Skills](https://agentskills.io/) format."*

License section (verbatim, last line): *"MIT"* — claim only; no `LICENSE` file at repo root.

## 7 skills inventory

| # | README label | Directory name | YAML `name:` | SKILL.md lines | License declared in YAML |
|---|---|---|---|---|---|
| 1 | react-best-practices | `react-best-practices` | `vercel-react-best-practices` | 149 | ✅ MIT |
| 2 | web-design-guidelines | `web-design-guidelines` | `web-design-guidelines` | 39 | ❌ |
| 3 | react-native-guidelines | `react-native-skills` | `vercel-react-native-skills` | 121 | ✅ MIT |
| 4 | react-view-transitions | `react-view-transitions` | `vercel-react-view-transitions` | 320 | ✅ MIT |
| 5 | composition-patterns | `composition-patterns` | `vercel-composition-patterns` | 89 | ✅ MIT |
| 6 | vercel-deploy-claimable | `deploy-to-vercel` | `deploy-to-vercel` | 296 | ❌ |
| 7 | (not in README list) | `vercel-cli-with-tokens` | `vercel-cli-with-tokens` | 353 | ❌ |

**Total SKILL.md content:** 1,367 lines across 7 skills.

**Corpus-first observations from inventory:**
- README label vs directory name vs YAML `name:` divergence (3 different naming conventions in same skill: e.g., `react-native-guidelines` README label / `react-native-skills` directory / `vercel-react-native-skills` YAML name)
- `vercel-` prefix in YAML name serves as namespace-disambiguation when distributed to Claude Code's `~/.claude/skills/` directory
- 4 of 7 skills declare explicit `license: MIT` in YAML frontmatter; 3 do not — **per-skill license metadata variation** within a single repo
- README lists 6 skills but 7 directories exist; `vercel-cli-with-tokens` is undocumented in README (possible work-in-progress or sibling-of-deploy-to-vercel companion)

## Per-skill summary

### 1. react-best-practices (`vercel-react-best-practices` v1.0.0)

**Domain:** React + Next.js performance optimization
**Source attribution (verbatim):** *"from Vercel Engineering"*
**Rule count:** README claims 40+; SKILL.md says 70 rules across 8 categories
**Categories:** Eliminating waterfalls (Critical) / Bundle size (Critical) / Server-side perf (High) / Client-side data fetching (Medium-High) / Re-render opt (Medium) / Rendering perf (Medium) / JS micro-optimizations (Low-Medium)
**Use when:** "Writing new React components or Next.js pages" / "Implementing data fetching" / "Reviewing code for performance issues" / "Optimizing bundle size"

### 2. web-design-guidelines (no `vercel-` prefix; v1.0.0)

**Domain:** UI / UX / accessibility audit
**Rule count:** 100+ rules
**Categories:** Accessibility / Focus States / Forms / Animation / Typography / Images / Performance / Navigation & State / Dark Mode & Theming / Touch & Interaction / Locale & i18n
**Trigger phrases (verbatim):** *"Review my UI"*, *"Check accessibility"*, *"Audit design"*, *"Review UX"*, *"Check my site against best practices"*
**Corpus-first YAML field:** `argument-hint: <file-or-pattern>` (slash-command argument hint)

### 3. react-native-guidelines (`vercel-react-native-skills` v1.0.0)

**Domain:** React Native + Expo mobile performance
**Rule count:** 16 rules across 7 sections
**Sections:** Performance (FlashList, memoization) / Layout (flex, safe areas, keyboard) / Animation (Reanimated, gestures) / Images (expo-image, caching) / State (Zustand, React Compiler) / Architecture (monorepo) / Platform (iOS/Android)

### 4. react-view-transitions (`vercel-react-view-transitions` v1.0.0)

**Domain:** Native browser View Transition API for React/Next.js
**Coverage:** `<ViewTransition>` component (enter/exit/update/share triggers) + `addTransitionType` + View Transition Classes / CSS pseudo-elements + shared element transitions / `name` prop + JavaScript animations via Web Animations API + Next.js `transitionTypes` prop on `next/link` + `prefers-reduced-motion` accessibility
**Largest of the 4 rule-aggregator skills:** 320 lines

### 5. composition-patterns (`vercel-composition-patterns` v1.0.0)

**Domain:** React component architecture
**Patterns covered:** Compound components / lifting state / composing internals / avoiding prop drilling / boolean prop proliferation avoidance
**Rule prefix taxonomy:** `architecture-` / `state-` / `patterns-` / `react19-` (corpus-first per-rule prefix-namespace)
**React 19 awareness:** explicit `react19-no-forwardref` rule

### 6. vercel-deploy-claimable (directory: `deploy-to-vercel`; v3.0.0)

**Domain:** Agentic deployment to Vercel
**Most mature SKILL.md** by version (v3.0.0 — others all v1.0.0)
**Largest practical SKILL.md:** 296 lines (vercel-cli-with-tokens is 353 but more reference-oriented)
**Trigger phrases:** *"Deploy my app"*, *"Deploy this to production"*, *"Push this live"*, *"Deploy and give me the link"*
**Features:**
- Auto-detects 40+ frameworks from `package.json`
- Returns **preview URL** (live site) AND **claim URL** (transfer ownership) — bipartite output corpus-first
- Handles static HTML projects automatically
- Excludes `node_modules` and `.git` from uploads
- 4-step workflow: gather state → choose method → execute → return URLs
- Decision tree based on git remote presence + `.vercel/project.json|repo.json` linking + Vercel CLI auth state + team count

**Output (verbatim):**
```
Deployment successful!

Preview URL: https://skill-deploy-abc123.vercel.app
Claim URL:   https://vercel.com/claim-deployment?code=...
```

**Corpus-first claim-URL-as-funnel-terminus:** Pattern #50 50a sub-variant data point — agent-deployed previews funnel into Vercel ownership transfer at vercel.com/claim-deployment.

### 7. vercel-cli-with-tokens (v1.0.0)

**Domain:** Token-authenticated Vercel CLI usage (vs interactive `vercel login`)
**Largest SKILL.md:** 353 lines
**Trigger phrases (verbatim):** *"deploy to vercel"*, *"set up vercel"*, *"add environment variables to vercel"*
**Use case:** Headless / CI / automated workflows where interactive login is infeasible
**Companion to:** vercel-deploy-claimable (this skill provides token primitives; deploy-claimable provides high-level deployment)

## Installation surface (corpus-first 4-channel)

**Primary install command (verbatim from README):**
```bash
npx skills add vercel-labs/agent-skills
```

**Corpus-first `npx skills` install verb.** This invokes a third-party (non-Anthropic) registry/CLI tool published as `skills` npm package — ostensibly maintained by skills.sh / agentskills.io. Distinct from prior corpus install verbs:
- `/plugin marketplace add` (Claude Code native — Pattern #59 59a/59b)
- `npm install` (npm direct — multiple wikis)
- `pip install` (PyPI — multiple wikis)
- `cargo install` (Rust — gws v13)
- `pipx install` (isolated Python — multiple wikis)
- **NEW: `npx skills add <repo>` via skills.sh registry** (Vercel v51)

**Secondary install methods** (per AGENTS.md / CLAUDE.md):

```bash
# Claude Code direct
cp -r skills/{skill-name} ~/.claude/skills/

# claude.ai (browser)
# Add the skill to project knowledge or paste SKILL.md contents into the conversation
```

**Per-skill ZIP packaging** (5 of 7 skills have zips at `00 Source/agent-skills/skills/`):
- `deploy-to-vercel.zip`
- `react-best-practices.zip`
- `react-view-transitions.zip`
- `vercel-cli-with-tokens.zip`
- `web-design-guidelines.zip`
- (missing: `composition-patterns.zip` and `react-native-skills.zip` — possibly newer skills not yet packaged)

**Total install surfaces:** 4 (npx skills + manual cp + paste-to-claude.ai + per-skill zip download).

## Usage examples (verbatim from README)

```
Deploy my app
```
```
Review this React component for performance issues
```
```
Help me optimize this Next.js page
```

**Convention:** Skills auto-activate on natural-language triggers. Agent uses YAML `description:` + trigger-phrase matching to decide which skill to load.

## Skill structure standard (verbatim from README §"Skill Structure")

Each skill contains:
- `SKILL.md` — Instructions for the agent (REQUIRED)
- `scripts/` — Helper scripts for automation (OPTIONAL)
- `references/` — Supporting documentation (OPTIONAL)

**Verified in source repo:** All 7 skills follow this; `composition-patterns` additionally has its own `AGENTS.md` + `README.md` + `metadata.json` + `rules/` (most-elaborate per-skill structure observed); `web-design-guidelines` has rules in skill-specific files; `deploy-to-vercel` has `Archive.zip` + `resources/`.

## License section ambiguity (verbatim README §"License" entire content)

```
## License

MIT
```

**That's the entire License section.** No `LICENSE` file at repo root. Per-skill `license: MIT` declared in YAML frontmatter for 4 of 7 skills only.

**Strict legal reading:** README MIT claim is goodwill statement, not legal license. Per-skill YAML metadata for 4 skills MAY apply per-skill but is non-standard. Default copyright applies to remaining 3 skills + repo-level structure. Pattern #29 29-absent-3 sub-context strengthening (joins awesome-claude-skills v50 — but Vercel is even more clearly OSI-license-claimed-without-LICENSE-file).

## Pattern Library observations (Phase 2 cluster discipline)

**Strengthens existing patterns:**
- **#17 variant 5 ecosystem-scale commercial platform** — Vercel = N=3 default-criterion (HuggingFace + Microsoft + Vercel)
- **#29 29-absent-3 sub-context** — N=2 strengthening (awesome-claude-skills v50 + Vercel v51); per-skill license variation observed at both
- **#19 archetype 4 corporate-collective lineage** — "Vercel Engineering" cited as collective; no individuals
- **#27 corporate-amplified-organic sub-path** — 25.7K / 4.5mo = ~5,700/mo
- **#2 4-surface install** — npx skills + manual cp + paste-to-claude.ai + per-skill zip

**Counter-evidence observations:**
- **#18 MCP** — Vercel skills do NOT use MCP; corporate-official tier MCP-absent-altogether (joins T1-scale pi-mono v36 + multi T5-scope wikis)
- **#22 AGENTS.md** — Vercel ships AGENTS.md = CLAUDE.md byte-identical mirror (corpus-first 22d sub-variant)

**Cross-corpus citation (forward-citation-then-wiki):**
- **#57 57c NEW sub-variant** — multica v15 wiki entry cited "Vercel agent-skills import (first)" 36 wikis BEFORE v51

**Absences:**
- No CONTRIBUTING.md / SECURITY.md / CODE_OF_CONDUCT / LICENSE / CITATION.cff
- No tests / no CI surfaces visible / no `.github/workflows/`
- No i18n (EN-only)
- No Karpathy / John Lam / individual lineage citations
- No MCP / no plugin marketplace publishing despite Vercel's commercial-platform fit

## Cluster summary verdict

Vercel agent-skills is a **corporate-narrow-skill-library** (T1 entrant) targeting the React / Next.js / Vercel ecosystem. 7 production-quality SKILL.md files spanning 1,367 lines of agent instructions. Most mature skill (vercel-deploy-claimable v3.0.0) demonstrates the claim-URL-as-funnel-terminus agentic deployment primitive. Distribution via `npx skills add` corpus-first third-party-registry verb. Light governance (just AGENTS.md + CLAUDE.md identical-mirror + README). Pattern Library impact: 1 new sub-variant (22d identical-mirror) + 1 new sub-variant (57c forward-citation-then-wiki) + 3 strengthenings (#17 variant 5 N=3 / #29 29-absent-3 N=2 / #50 50a observational claim-URL-terminus).
