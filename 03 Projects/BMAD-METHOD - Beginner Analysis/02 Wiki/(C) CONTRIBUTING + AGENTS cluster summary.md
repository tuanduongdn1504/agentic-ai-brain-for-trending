# (C) CONTRIBUTING + AGENTS cluster summary — BMAD-METHOD

> **Sources:** `CONTRIBUTING.md` (6.8 KB, WebFetch Phase 0) + `AGENTS.md` (465 bytes, WebFetch Phase 2)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster these two

Both are **dev-process files**. CONTRIBUTING = how humans contribute to BMAD. AGENTS.md = how AI contributors (Claude etc.) should behave inside the repo. Together they define the **developer-operations surface** for BMAD maintainers + contributors. Clustered because neither is large enough for solo summary, and together they tell the dev-workflow story.

## 2. AGENTS.md — entire file

The file is 465 bytes. Full contents (verbatim):

```markdown
# BMAD-METHOD

Open source framework for structured, agent-assisted software delivery.

## Rules

- Use Conventional Commits for every commit.
- Before pushing, run `npm ci && npm run quality` on `HEAD` in the exact checkout you are about to push.
  `quality` mirrors the checks in `.github/workflows/quality.yaml`.

- Skill validation rules are in `tools/skill-validator.md`.
- Deterministic skill checks run via `npm run validate:skills` (included in `quality`).
```

### Interpretation

- **AGENTS.md here = pre-commit contract for AI coding agents**. Not the "12+ agents" list (that lives in README + `bmad/bmm/agents/`)
- **3 enforceable rules:** Conventional Commits / `npm run quality` before push / skill validator compliance
- **Convention match:** deer-flow, autoresearch, ECC all have AGENTS.md files as AI-coding-agent instructions. **Markdown agent skill convention** — universal across 11 wikis now
- **Minimal scope:** BMAD's AGENTS.md is **tiny vs deer-flow's substantial AGENTS.md**. BMAD keeps AI-agent rules minimal because the product itself IS agent orchestration — the rules go in the product, not the contrib contract

⚠️ **Correction to Phase 0 assumption:** Phase 0 log flagged AGENTS.md as "mystery" (Q14). Not a mystery — it's just genuinely minimal. Three rules, no pointer to detailed docs. **Closed question.**

## 3. CONTRIBUTING.md — governance + dev workflow

### Branching + publishing

- **Trunk-based development** — single `main` branch, short-lived feature branches
- **Auto-publish to `@next` tag** on merge to main (continuous npm release for `@next` channel)
- **Weekly stable → `@latest`** — manual promotion to stable npm tag
- **Breaking-change policy:** bundled into major versions (CHANGELOG confirms: v2, v4, v6 each had user-migration events)

### PR discipline

- **200-400 lines ideal** per PR
- **800 max** hard ceiling
- Signal: PRs must be reviewable — no 2000-line refactor dumps
- Matches Superpowers/GSD PR discipline; stricter than ECC (solo maintainer, no ceiling)

### Code standards for AI-generated contributions

> "Natural-language markdown core — no code in core"

- **Core framework = markdown agent definitions**, not code
- Agents are `.md` files with frontmatter + role descriptions
- Code belongs to tooling (CLI installer, validator) in `tools/`
- **AI-generated code standards** — explicit acknowledgment that contributors use LLMs; project requires same `quality` gate pass regardless of human/AI origin

### Skill validator

- `npm run validate:skills` checks markdown agent definitions for structural compliance
- Rules in `tools/skill-validator.md` (not fetched; logged as deep-dive candidate)
- Deterministic — same input → same pass/fail. No LLM-in-the-loop validation (contrast with some subjective-eval frameworks)

## 4. Natural-language markdown core — the big idea

BMAD's philosophical commitment:

- **Core = `.md` files describing agent behaviors** (no `.js` / `.ts` / `.py` in core)
- **Tooling = `.js`** (installer, validator, CLI — in `tools/`)
- **Extensions = variable** (BMB builds more agents → more `.md`; BMGD adds game-dev domain → more `.md` + templates)

**Why this matters:**
- Agents are **readable by humans and LLMs directly** — no parser needed
- Contributors write prose, not code, for core
- Lowers contribution barrier for non-programmers (PMs, designers can write agent definitions)
- Makes forking + customizing trivial — edit `.md`, reinstall

**Contrast with siblings:**
- **gstack:** TS/JS role files
- **GSD:** agents are `.md` but workflow is JSON/TS
- **Superpowers:** markdown skills + bash scripts
- **ECC:** markdown skills + code samples
- BMAD = **most markdown-pure** of T1

## 5. Contribution flow (inferred from CONTRIBUTING + AGENTS)

1. Fork / branch from `main`
2. Write `.md` agent/workflow or fix tooling code
3. `npm ci && npm run quality` locally (mirrors CI)
4. Conventional Commit message
5. PR 200-400 lines
6. Merge → auto-publish `@next`
7. Wait for weekly `@latest` promotion (if feature warrants stable)

## 6. Governance signals

| Signal | BMAD |
|--------|------|
| Entity | BMad Code, LLC |
| License | MIT |
| Trademark | BMad / BMAD-METHOD™ |
| Hosting | GitHub (bmad-code-org) |
| Community | Discord + YouTube (active) |
| Maintainer count | LLC team (not solo) — size unclear |
| PR queue | Active, churn-heavy |
| Commit style | Conventional Commits enforced |
| CI | `.github/workflows/quality.yaml` — lint + validate:skills + test |

## 7. Comparison to T1 sibling dev-ops

| Axis | BMAD | ECC | Superpowers | gstack | GSD |
|------|------|-----|-------------|--------|-----|
| PR ceiling | 800 | — | — | — | — (explicit) |
| Trunk-based | ✅ | ✅ | ✅ | ✅ | ✅ |
| Auto-publish `@next` | ✅ | ❌ | ❌ | ✅ | ❌ |
| Markdown-pure core | ✅ (strictest) | ✅ | Partial | ❌ (TS) | Partial |
| Skill validator | ✅ (deterministic) | ❌ | ❌ | ❌ | ❌ |
| LLC / corporate | LLC | Solo | Solo | YC | Solo |

→ BMAD has the **most formal dev-process of T1**. Explicit PR ceiling, explicit quality gate, explicit skill validator, explicit auto-publish. Most "corporate" ops posture.

## 8. Storm Bear operator implications

If Storm Bear wants to contribute to BMAD:
- **Barrier = low** for `.md` agent contributions (no code)
- **Barrier = medium** for tooling contributions (npm quality gate, conventional commits)
- **Barrier = high** for architectural changes (breaking-change budget owned by LLC)
- **VN contribution pathway:** README_VN translation improvements are a clear onramp (current is machine-quality; native speaker polish would be welcomed)

## 9. Cross-reference to other wikis

- **deer-flow AGENTS.md** — substantial AI-coding-agent instructions (different tone, product ≠ agent-as-methodology)
- **Superpowers** — similar PR discipline, markdown-skills pure
- **vault `05 Skills/llm-wiki-ingest.md`** — parallel philosophy (markdown-pure skills), convergent independently

## Open questions surfaced

- How many core maintainers at BMad Code, LLC? → Q21
- Skill validator rules — what does `tools/skill-validator.md` enforce structurally? → Q22
- VN translation improvement = good first issue for native speaker? Policy on translation PRs? → Q23
- ~~AGENTS.md mystery~~ → **CLOSED** (minimal by design, 3 rules, no hidden pointer)
