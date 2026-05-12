# Cluster 1 — README + install + 4-principle framework

## What this cluster covers

The repo's outward-facing surface: the problem statement, 4-principle framework, install paths, and intellectual lineage citation. Source files: `README.md`, `README.zh.md`, `CURSOR.md`.

## The problem statement (as authored)

forrestchang frames the artifact as a direct response to **Andrej Karpathy's X tweet** (linked: `x.com/karpathy/status/2015883857489522876`). Karpathy's three observations as quoted:

1. *"The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."*
2. *"They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."*
3. *"They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."*

Plus Karpathy's positive framing: *"LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."*

## The 4 principles → mapped to Karpathy critiques

| Principle | Karpathy critique addressed |
|-----------|------------------------------|
| **Think Before Coding** | Wrong assumptions / hidden confusion / missing tradeoffs |
| **Simplicity First** | Overcomplication / bloated abstractions |
| **Surgical Changes** | Orthogonal edits / touching unrelated code |
| **Goal-Driven Execution** | Leverage Karpathy's positive observation (loop-until-goal) |

This is a **clean 1-to-1 distillation** — not a synthesis with other methodologies. Each principle traces to a specific Karpathy quote.

## Install paths (3-way)

**Path A — Claude Code plugin marketplace (recommended):**

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Path B — per-project CLAUDE.md:**

```bash
# New project
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md

# Existing project (append)
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

**Path C — Cursor rule:**

Repo includes `.cursor/rules/karpathy-guidelines.mdc` with `alwaysApply: true`. Cursor users opening the repo in Cursor get the rule auto-applied. Cross-project: copy the `.mdc` file into target project's `.cursor/rules/`.

## Intellectual influence citation — explicit

The README opens with an inline link to a separate forrestchang project ([Multica](https://github.com/multica-ai/multica) — *"open-source platform for running and managing coding agents with reusable skills"*) and X handle (`@jiayuan_jy`). The Karpathy citation is explicit, with URL to the source tweet.

**Cross-corpus significance:** Karpathy is the **most-corpus-cited individual in Storm Bear vault** — the LLM Wiki pattern (Karpathy-originated) is the FOUNDATION of the entire vault per root CLAUDE.md "Who I Am & My Purpose" section. autoresearch v8 = 1st corpus-explicit-Karpathy-citation. v63 karpathy-skills = corpus-foundation-individual-inheritance through derivative-distillation.

## Tradeoff acknowledgment (anti-vibe positioning calibration)

README explicitly calibrates: *"These guidelines bias toward **caution over speed**. For trivial tasks (simple typo fixes, obvious one-liners), use judgment — not every change needs the full rigor."*

This is a **NEUTRAL with anti-overengineering pole** position — distinct from cc-sdd v61's anti-vibe-with-pragmatic-acknowledgment (full-workflow critique). Karpathy-skills targets *narrower* failure modes (overcomplication / silent assumptions / orthogonal edits) without rejecting vibe-coding workflow itself.

## How-to-know-it-works rubric

README provides 4 success indicators:

- Fewer unnecessary changes in diffs
- Fewer rewrites due to overcomplication
- Clarifying questions come BEFORE implementation
- Clean, minimal PRs without drive-by improvements

These are **measurable behavioral outcomes** — not abstract methodology checkpoints. Sister-pattern to cc-sdd v61's adversarial-review fresh-evidence completion gate but at lower-formality scale.

## i18n: EN + ZH

Bilingual README (`README.md` + `README.zh.md`). No JP/KR/VN.

## What's NOT here

- No spec/plan/task scaffold (NOT SDD methodology)
- No subagent role separation (NOT Pattern #76 architectural primitive)
- No protocol translation (NOT Pattern #18 Layer 2 protocol-translation T4 sub-archetype)
- No multi-platform install-time format translator (NOT cc-sdd v61's framework-scale Pattern #18)
- No corpus citation BEYOND Karpathy (no mattpocock / cc-sdd / spec-kit cross-references)
