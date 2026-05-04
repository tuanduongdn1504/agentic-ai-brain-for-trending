# Cluster — AGENTS.md governance + lgtm gate + release cadence

**Source:** `AGENTS.md` (root, 182+ lines) + `CONTRIBUTING.md` + `.github/workflows/` (issue-gate / pr-gate / approve-contributor) + CHANGELOG structure
**Fetch date:** 2026-04-23
**Cluster role:** Governance, contribution protocol, release discipline — the "rules of the road" for humans + agents in pi-mono

---

## Summary

pi-mono's governance surface is **unusually heavy for a solo project** and contains **two corpus-first mechanisms**: (1) the `lgtm` / `lgtmi` maintainer-approval keyword protocol (documented in AGENTS.md), and (2) the auto-close-by-default gate for new contributors (enforced by 3 GitHub Actions). Combined with a detailed AGENTS.md covering conversational style, code quality, commands, PR workflow, changelog format, provider-integration steps, release process, and **CRITICAL Git rules for parallel agents**, pi-mono's governance approximates Microsoft-corporate-level formalization at solo-maintainer scale.

The document targets **both humans and AI agents** explicitly — the first line of the README says AGENTS.md contains "project-specific rules (for both humans and agents)," and the file itself says "Multiple agents may work on different files in the same worktree simultaneously. You MUST follow these rules." This is the most explicit agent-collaboration governance discipline observed in the Storm Bear corpus at v36.

---

## AGENTS.md section map (verbatim section titles)

1. **Conversational Style** — no emojis in commits/issues/PRs/code; technical prose only; "Thanks @user" not "Thanks so much @user!"
2. **Code Quality** — no `any`, no inline imports, never downgrade to fix type errors, ask before removing functionality, no backward-compat preservation unless explicit, no hardcoded keybinding checks (must use `DEFAULT_*_KEYBINDINGS`)
3. **Commands** — `npm run check` mandatory after code changes; never `npm run dev`/`build`/`test`; `npx tsx ../../node_modules/vitest/dist/cli.js` for specific tests; test files MUST pass before commit; NEVER commit unless user asks
4. **Contribution Gate** — `lgtmi` / `lgtm` approval keywords; auto-close workflows; pkg:* labels; multi-line comment via `gh issue comment --body-file`
5. **PR Workflow** — analyze PRs without pulling locally first; no opening PRs without explicit user approval
6. **Testing pi Interactive Mode with tmux** — precise tmux scripting recipe for TUI testing
7. **Changelog** — strict `## [Unreleased]` discipline + locked released sections + GitHub-issue-link attribution
8. **Adding a New LLM Provider** — 7-step provider-integration checklist (core types + provider impl + exports/registration + model generation + tests + coding-agent integration + docs)
9. **Releasing** — lockstep versioning (all packages same version); patch = fixes+features, minor = breaking; `npm run release:patch|minor` script handles bump+changelog+commit+tag+publish
10. **CRITICAL Git Rules for Parallel Agents** — ONLY commit YOUR files, NEVER `git add -A`/`.`, FORBIDDEN: `git reset --hard` / `git checkout .` / `git clean -fd` / `git stash` / `git commit --no-verify`

---

## Corpus-first: `lgtm` / `lgtmi` maintainer-approval keyword protocol

From AGENTS.md §Contribution Gate:

> Maintainer approval comments are handled by `.github/workflows/approve-contributor.yml`

> - `lgtmi` approves future issues
> - `lgtm` approves future issues and rights to submit PRs

**Semantic:**
- `lgtmi` ("looks good to me — issues") — exempts the commenter from future issue auto-closure
- `lgtm` ("looks good to me") — exempts AND grants PR-submission rights

**Architectural novelty:** This is a **maintainer-authored approval keyword** posted at comment-time, distinct from contributor-authored opt-in signals (like `🤖🤖🤖` PR suffix in Pattern #69 v31 candidate registration via awesome-mcp-servers v31). Both mechanisms target the AI-era OSS-contributor-volume problem but from opposite sides:

- **Pattern #69a (v31 origin)** — **contributor-authored opt-in** (e.g. agent-authored PR self-declares via `🤖🤖🤖` suffix)
- **Pattern #69b (v36, pi-mono)** — **maintainer-authored approval** (e.g. single keyword comment grants contributor ongoing rights)

At v36 this strengthens #69 to N=2 with 2 structurally-distinct sub-variants. Per v2.1 structurally-unambiguous-N=2 criterion, **promotion-candidate at next mini-audit**.

---

## 3 GitHub Actions workflows (contribution gate machinery)

Observed in `.github/workflows/`:

1. **`issue-gate.yml`** — auto-closes issues from new contributors (not yet `lgtmi` or `lgtm`-approved)
2. **`pr-gate.yml`** — auto-closes PRs from new contributors without PR-submission rights
3. **`approve-contributor.yml`** — parses maintainer `lgtm` / `lgtmi` comments and grants approval to the referenced contributor

Plus: `ci.yml` (build verification) — referenced in README badge.

**Effect:** Mario gets to control signal-to-noise ratio of community inbound at 38.9K stars without hiring co-maintainers. Trade-off: new contributors face friction + potential false-negatives (quality first-time contributions auto-closed pending manual review).

**CONTRIBUTING.md explicit enforcement philosophy:**

> Repeated violations (ignoring guidelines twice or spam submissions) result in permanent account blocking.

This is stricter than typical OSS enforcement. Mario is prioritizing **tight quality control over inclusive contribution velocity**.

---

## Quality bar for issues (from CONTRIBUTING.md)

Issues must use official GitHub templates and be:

- **Single-screen length maximum** (no walls of text)
- Clear, concise
- **Authentic voice** — "avoid templated language" (a dig at AI-generated issue text)
- Explicit problem statement
- Justification for why it matters
- Intent declaration if self-implementing

Pre-PR requirements:
- Obtain `lgtm` first
- Run `npm run check` + `./test.sh` successfully
- Don't modify `CHANGELOG.md` (maintainers manage changelog)

---

## Changelog discipline

Location: **per-package** — `packages/*/CHANGELOG.md` (each package has its own). Complements lockstep versioning.

**Format rules:**
- New entries ALWAYS go under `## [Unreleased]`
- Subsections: `Breaking Changes` / `Added` / `Changed` / `Fixed` / `Removed`
- Append to existing subsections (never duplicate)
- **NEVER modify released version sections** — they're immutable
- Attribution:
  - Internal: `Fixed foo bar ([#123](https://github.com/badlogic/pi-mono/issues/123))`
  - External: `Added feature X ([#456](...) by [@username](...))`

**Issue-close-on-commit:** commit messages must include `fixes #<number>` or `closes #<number>` for auto-close.

---

## Release cadence: 200+ releases in 8.5 months

**Cadence:** ~23 releases/month average (200+ / 8.5 months).

**Lockstep bump:** every release bumps ALL 7 packages to the same version number. Latest: v0.69.0 (2026-04-22).

**Semantics (no major releases):**
- `patch` = bug fixes + new features
- `minor` = API breaking changes

**Workflow:** `npm run release:patch` or `npm run release:minor` handles the full pipeline — version bump, CHANGELOG `[Unreleased]` → numbered-release-section promotion, commit, tag, publish to npm, append new `[Unreleased]` section.

**Corpus observation:** 23 releases/month sustained over 8.5 months is **extreme velocity** compared to other corpus entries. multica v15 had 43 releases in ~months-of-project-age (slower). BMAD v11 at 45K had more traditional cadence. **Single-author-specific** — driven by Mario's own release-pace practice + lockstep auto-bump-everything.

**Not registered as pattern candidate** — N=1 is insufficient generalizability; monorepo-lockstep-auto-bump artifact could be pattern or quirk. Flagged in Mario's entity page as author-archetype observation.

---

## CRITICAL Git Rules for Parallel Agents (corpus-first)

Full verbatim from AGENTS.md:

> Multiple agents may work on different files in the same worktree simultaneously. You MUST follow these rules:
>
> **Committing**
> - **ONLY commit files YOU changed in THIS session**
> - ALWAYS include `fixes #<number>` or `closes #<number>` in the commit message when there is a related issue or PR
> - NEVER use `git add -A` or `git add .` - these sweep up changes from other agents
> - ALWAYS use `git add <specific-file-paths>` listing only files you modified
> - Before committing, run `git status` and verify you are only staging YOUR files
> - Track which files you created/modified/deleted during the session
>
> **Forbidden Git Operations**
> - `git reset --hard` - destroys uncommitted changes
> - `git checkout .` - destroys uncommitted changes
> - `git clean -fd` - deletes untracked files
> - `git stash` - stashes ALL changes including other agents' work
> - `git add -A` / `git add .` - stages other agents' uncommitted work
> - `git commit --no-verify` - bypasses required checks and is never allowed

**Novelty:** This is the **most explicit multi-agent-collaboration governance discipline observed in Storm Bear corpus at v36**. Not just a CLAUDE.md note but a hard-rule contract. Implies Mario (and/or other pi users) routinely run multiple agent processes in one worktree — an operating model few corpus frameworks contemplate.

**Pattern #12 Governance-Depth:** pi-mono N=2 counter-evidence (solo-heavy-governance) alongside claude-hud v35. If N=3 emerges, refinement: "governance-depth correlates with maintainer-philosophy more than organization-size."

---

## Adding a New LLM Provider (pi-ai 7-step)

AGENTS.md codifies the provider-extension process at §Adding a New LLM Provider:

1. **Core types (`packages/ai/src/types.ts`):** Add API identifier to `Api` union, create options interface extending `StreamOptions`, add mapping to `ApiOptionsMap`, add provider name to `KnownProvider`
2. **Provider implementation (`packages/ai/src/providers/`):** Export `stream<Provider>()` + `streamSimple<Provider>()` + provider-options interface + message/tool conversion + response parsing emitting `text`/`tool_call`/`thinking`/`usage`/`stop` standardized events
3. **Provider exports + lazy registration:** Package subpath export in `packages/ai/package.json`, type re-exports in `src/index.ts`, lazy-loader registration in `src/providers/register-builtins.ts` (NEVER static imports there), credential detection in `src/env-api-keys.ts`
4. **Model generation (`scripts/generate-models.ts`):** Fetch/parse provider model list, map to standardized `Model` interface
5. **Tests (`test/`):** Add provider to 11+ named test files (stream / tokens / abort / empty / context-overflow / image-limits / unicode-surrogate / tool-call-without-result / image-tool-result / total-tokens / cross-provider-handoff); special `cross-provider-handoff.test.ts` requires at least one pair per provider model family
6. **Coding agent (`packages/coding-agent/`):** Default model ID in `src/core/model-resolver.ts`, env var docs in `src/cli/args.ts`, README provider setup
7. **Documentation:** pi-ai README providers table + options/auth docs + env vars; CHANGELOG under `[Unreleased]`

**Corpus-relevance:** This is the **most detailed codified per-provider-integration checklist** in Storm Bear corpus at v36. Contrast TrendRadar v19 LiteLLM adopts-everything-for-free abstraction model (no per-provider discipline required downstream).

---

## Cross-reference signals

- **Pattern #12 Governance-Depth (CONFIRMED v13)** — pi-mono counter-evidence #2 (solo-heavy-governance) after claude-hud v35
- **Pattern #22 AGENTS.md T1 absence (CANDIDATE v17)** — **refinement candidate**: pi-mono has 182-line AGENTS.md at solo T1. AGENTS.md is becoming solo-T1-adopted, not just corporate-T4.
- **Pattern #69 Agent-PR Fast-Track Governance (CANDIDATE v31)** — **STRENGTHENS to N=2 structurally-unambiguous** via pi-mono `lgtm`/`lgtmi` sub-variant 69b + v31 original `🤖🤖🤖` sub-variant 69a. **Promotion-candidate at next mini-audit.**
- **Pattern #19 archetype 4 (no-lineage)** — pi-mono 13th T1 data point: no explicit AI-agent intellectual lineage cited in README or AGENTS.md.

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*
