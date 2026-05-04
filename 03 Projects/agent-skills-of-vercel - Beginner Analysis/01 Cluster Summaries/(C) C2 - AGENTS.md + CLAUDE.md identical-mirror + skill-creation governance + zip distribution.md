# (C) Cluster Summary 2 — AGENTS.md + CLAUDE.md identical-mirror + skill-creation governance + zip distribution

**Source files:** `00 Source/agent-skills/AGENTS.md` (3,281 bytes) + `00 Source/agent-skills/CLAUDE.md` (3,281 bytes — byte-identical)
**Cluster theme:** Contributor-facing governance + skill creation conventions + distribution mechanics

---

## Identical-mirror verification (corpus-first 22d sub-variant)

```
$ /usr/bin/diff AGENTS.md CLAUDE.md
[zero output — files are identical]
$ wc -c AGENTS.md CLAUDE.md
3281 AGENTS.md
3281 CLAUDE.md
```

**Both files start with the heading `# AGENTS.md`** (CLAUDE.md does NOT have a CLAUDE.md-specific heading). This is **content-as-mirror** rather than file-name-respecting separate documents.

**Distinct from prior corpus AGENTS.md sub-variants:**
- 22a: solo monolithic AGENTS.md (gh-aw v48 — 49.8KB single source-of-truth)
- 22b: minimum-viable shim (CLAUDE.md as tiny `@AGENTS.md` redirect alias; bizos v37 — CLAUDE.md is 11 bytes)
- 22c: authoritative-with-shim 3-layer hierarchy (aidevops v47 — Layer 0 [CLAUDE.md 440B + AGENT.md 420B shims] / Layer 1 root AGENTS.md 3KB / Layer 2 .agents/AGENTS.md 18KB)
- **22d NEW: identical-mirror full-content duplicated** (no canonical source designation; both files served independently with same bytes)

**Verdict:** 22d is structurally distinct from 22a/b/c. Vercel ships full content in BOTH files — no shim, no redirect, no hierarchy. Both files are independently authoritative.

**Likely rationale:** Both Claude Code and other agents (Cursor, Copilot) look for their respective filenames; rather than canonical-with-redirect, Vercel chose duplicate-with-zero-divergence-risk. Drift risk traded for storage cost.

**N=1 stale-flagged at registration; +5 v56 / +10 v61 review cadence.**

## Repository overview (verbatim from AGENTS.md/CLAUDE.md)

> *"A collection of skills for Claude.ai and Claude Code for working with Vercel deployments. Skills are packaged instructions and scripts that extend Claude's capabilities."*

**Note discrepancy:** README says skills are for "AI coding agents" (broader); AGENTS.md/CLAUDE.md says "Claude.ai and Claude Code" specifically. Repo positions broadly publicly but governance scopes to Anthropic runtimes specifically.

**Note narrowing:** AGENTS.md says skills are *"for working with Vercel deployments"* — but only 2 of 7 skills are Vercel-specific (deploy-to-vercel + vercel-cli-with-tokens). The rule-aggregator skills (react-best-practices / web-design-guidelines / etc.) are general React/Next.js perf, not Vercel-specific. Slight positioning drift between README + AGENTS.md.

## Skill creation governance

### Directory structure (verbatim AGENTS.md)

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    scripts/              # Required: executable scripts
      {script-name}.sh    # Bash scripts (preferred)
  {skill-name}.zip        # Required: packaged for distribution
```

**Note:** AGENTS.md says `scripts/` is REQUIRED, but `composition-patterns` and `react-best-practices` skills are pure-rule-aggregators with `rules/` not `scripts/`. The "REQUIRED" label is aspirational rather than enforced.

**Note:** AGENTS.md says zip file is REQUIRED, but only 5 of 7 skills have zips. composition-patterns + react-native-skills missing zips.

### Naming conventions (verbatim)

- **Skill directory:** `kebab-case` (e.g., `vercel-deploy`, `log-monitor`)
- **SKILL.md:** Always uppercase, always this exact filename
- **Scripts:** `kebab-case.sh` (e.g., `deploy.sh`, `fetch-logs.sh`)
- **Zip file:** Must match directory name exactly: `{skill-name}.zip`

**Inconsistency:** YAML `name:` field uses different naming (e.g., directory `composition-patterns` → YAML `vercel-composition-patterns`). 3 different naming conventions per skill (directory / YAML / README label).

### SKILL.md format spec (verbatim)

```markdown
---
name: {skill-name}
description: {One sentence describing when to use this skill. Include trigger phrases like "Deploy my app", "Check logs", etc.}
---

# {Skill Title}

{Brief description of what the skill does.}

## How It Works
{Numbered list explaining the skill's workflow}

## Usage
```bash
bash /mnt/skills/user/{skill-name}/scripts/{script}.sh [args]
```

**Arguments:**
- `arg1` - Description (defaults to X)

**Examples:**
{Show 2-3 common usage patterns}

## Output
{Show example output users will see}

## Present Results to User
{Template for how Claude should format results when presenting to users}

## Troubleshooting
{Common issues and solutions, especially network/permissions errors}
```

**Required YAML frontmatter:** `name` + `description`
**Optional YAML frontmatter (observed in source repo):**
- `license:` (4 of 7 skills)
- `metadata.author` (all 7 skills declare `vercel`)
- `metadata.version` (all 7 declare; v1.0.0 default; deploy-to-vercel at v3.0.0)
- `argument-hint` (web-design-guidelines only — corpus-first observation)

### Best practices for context efficiency (verbatim AGENTS.md)

> *"Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant."*

**Operational rules:**
- **Keep SKILL.md under 500 lines** — put detailed reference material in separate files
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

**Verified compliance:** All 7 SKILL.md files are under 500 lines (max is vercel-cli-with-tokens at 353).

### Script requirements (verbatim)

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files
- Reference the script path as `/mnt/skills/user/{skill-name}/scripts/{script}.sh`

**Note:** `/mnt/skills/user/...` path convention is Claude.ai-specific (Anthropic's filesystem mount in browser sandbox). Claude Code uses different path; manual `cp -r skills/{name} ~/.claude/skills/` puts skills at standard local path.

### Zip packaging (verbatim)

```bash
cd skills
zip -r {skill-name}.zip {skill-name}/
```

**Purpose:** Per-skill zip for distribution to users who can't `git clone`. Each zip is self-contained (SKILL.md + scripts/ + references/).

### End-user installation (verbatim from AGENTS.md §"End-User Installation")

**Claude Code:**
```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
> *"Add the skill to project knowledge or paste SKILL.md contents into the conversation."*

> *"If the skill requires network access, instruct users to add required domains at claude.ai/settings/capabilities."*

**Note:** This is END-USER installation guidance. The README's `npx skills add vercel-labs/agent-skills` is the BULK install path that wraps these. AGENTS.md/CLAUDE.md does NOT mention `npx skills add` — possibly because AGENTS.md is contributor-facing while README is end-user-facing.

## Governance gaps

**Absent files (per `ls` of repo root):**
- ❌ LICENSE (README claims MIT only)
- ❌ CONTRIBUTING.md
- ❌ SECURITY.md
- ❌ CODE_OF_CONDUCT.md
- ❌ CITATION.cff
- ❌ `.github/` workflows
- ❌ tests/

**Present files:**
- ✅ README.md (170 lines)
- ✅ AGENTS.md (3,281 bytes)
- ✅ CLAUDE.md (3,281 bytes — identical to AGENTS.md)
- ✅ skills/ (7 subdirs + 5 zips)
- ✅ packages/react-best-practices-build/ (build tooling for one skill)

**Governance count:** 2 governance files (AGENTS.md + CLAUDE.md), but they're byte-identical so structurally **1 governance content unit**. Plus README. **LIGHT governance.**

**Counter-evidence to Pattern #12 governance-depth correlates with maturity-ambition:** Vercel = corporate-official + commercial-extension framework + 25.7K stars at 4.5 months but **LIGHT governance** (no SECURITY / CONTRIBUTING / CoC). Joins observation: corporate-official does NOT automatically imply heavy-governance. Counter-evidence at corporate-official tier; Pattern #12 v42 refined formulation (3-factor: maintainer-philosophy + maturity-ambition + scale-tier) holds — Vercel maintainer-philosophy is "light contributor-friendly LICENSE-by-claim" + maturity-ambition is "outreach-not-foundation" + scale-tier is "corporate-amplified-startup-form".

## Build tooling (`packages/react-best-practices-build/`)

Contains build scripts to compile per-rule files into the consolidated SKILL.md for the `react-best-practices` skill. Demonstrates Vercel's intent to scale rule-aggregator skills via build-pipeline (rather than hand-maintenance). Single skill with build tooling currently.

**Implication:** rule-aggregator skills (react-best-practices / web-design-guidelines / react-native-skills / composition-patterns) may all eventually consolidate from per-rule source-of-truth via similar build pipeline. Composition-patterns has explicit `rules/` directory → `AGENTS.md` "full compiled document" reference; same architecture.

## Pattern Library observations (Phase 2 cluster discipline)

**Strengthens / introduces:**
- **#22 22d identical-mirror NEW sub-variant** — register N=1 stale-flagged
- **#12 v42 refined formulation strengthening** — corporate-official + light-governance counter-instance reinforces 3-factor model (organization alone doesn't predict)
- **#29 29-absent-3 strengthening** — repo-level absent LICENSE + per-skill license variation

**Counter-evidence:**
- **#18 MCP** — corporate-official AGENTS.md/CLAUDE.md does NOT instruct MCP usage; skills.sh registry is non-MCP; observational counter-evidence at corporate-official tier
- **#22 22a/b/c distinction** — 22d demonstrates 4th sub-variant exists; AGENTS.md ecosystem is more diverse than initially observed

**Absences (informative):**
- No CONTRIBUTING — Vercel hasn't formalized external contributor pathway despite 25.7K-star community
- No SECURITY — supply-chain awareness gap (skills install bash scripts via npx; arguably should declare process)
- No tests — quality assurance via PR review only; no CI enforcement visible

## Cluster summary verdict

Cluster 2 reveals **22d identical-mirror corpus-first** (Vercel ships AGENTS.md = CLAUDE.md byte-identical) + **light corporate governance** (counter-instance to maturity-ambition correlation when corporate-official + commercial-extension; reinforces v42 3-factor refined formulation). SKILL.md format spec well-codified (500-line cap + on-demand loading + scripts-not-inline + bash-shebang/set-e/JSON-stdout). Skill creation governance is documented but partially aspirational (composition-patterns + react-native-skills missing zips; web-design-guidelines + deploy-to-vercel + vercel-cli-with-tokens missing per-skill license metadata). Build tooling for `react-best-practices` foreshadows scale via build-pipeline rather than hand-maintenance.
