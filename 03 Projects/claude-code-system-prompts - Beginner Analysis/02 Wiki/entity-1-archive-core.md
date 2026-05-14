# Entity 1 — claude-code-system-prompts core artifact

> **Type:** Foundation entity (what the archive IS)
> **Cross-references:** [Cluster 1 inventory](./cluster-1-readme-and-prompt-inventory.md) / [Cluster 2 methodology](./cluster-2-extraction-methodology.md) / [Cluster 3 CHANGELOG](./cluster-3-changelog-and-ecosystem.md)

## Identity

| Field | Value |
|---|---|
| **Full name** | Claude Code System Prompts — third-party reverse-engineering reference archive |
| **Author** | **Piebald-AI** corporate-org (commercial agentic-AI company at piebald.ai) |
| **Repo** | [`github.com/Piebald-AI/claude-code-system-prompts`](https://github.com/Piebald-AI/claude-code-system-prompts) |
| **License** | MIT |
| **Current tracked version** | **Claude Code v2.1.140** (May 12, 2026) |
| **Archive created** | 2025-11-18 — ~176 days at v65 wiki ship |
| **Last pushed** | 2026-05-13 (1 day before wiki ship) |
| **Stars / forks / subscribers** | **10,176 / 1,811 / 118** |
| **Stars-per-day** | ~57.8 (medium-high engagement; below Pattern #52 EXTREME-VIRAL 300+/day) |
| **Fork ratio** | **17.8% — CORPUS-RECORD active-deployment intent at this scale** (exceeds claude-seo v64 15.3%) |
| **Topics (GitHub)** | claude-code / claude-code-system-prompts / system-prompts |

## Function

A **reverse-engineering reference archive** that extracts and documents Claude Code's complete system prompt from the compiled `@anthropic-ai/claude-code` npm package. Updated within minutes of each Claude Code release.

**What it IS:**
- 293 markdown files in `system-prompts/` containing the extracted prompt fragments
- 211 KB CHANGELOG tracking 176 versions since v2.0.14
- `tools/updatePrompts.js` automated extraction script (19.5 KB)
- Reference material for understanding Claude Code's actual behavior

**What it IS NOT (per project CLAUDE.md):**
- Modifiable source code — editing these files does NOT change Claude Code's behavior
- An installable plugin or skill
- A vendor-published artifact (this is third-party; not maintained by Anthropic)
- A leak (extraction is mechanical from publicly-distributed npm package; Anthropic appears to tolerate)

## The 6-category, 293-file inventory

| Category | Files | Total tokens (approx) | Largest file |
|---|---|---|---|
| **Agent Prompts** | ~30 | ~30,000 | Background agent state classifier (4,405 tks) |
| **Data templates** | ~50 | ~80,000+ | Managed Agents endpoint reference (6,555 tks) |
| **System Prompt fragments** | ~50 | ~20,000 | Skillify Current Session (1,798 tks) |
| **System Reminders** | ~40 | ~5,000 | Plan mode is active (iterative) (936 tks) |
| **Tool Descriptions** | ~50 (28 Bash sub-fragments) | ~15,000 | TodoWrite (2,037 tks) |
| **Skills** | ~25 | ~50,000+ | **Model migration guide (18,340 tks — single largest file in archive)** |

**Total**: ~293 files representing ~200,000+ tokens of Claude Code's complete system prompt envelope (when all conditional fragments hypothetically activated).

## Methodology — 3-step extraction

1. **Download** latest `@anthropic-ai/claude-code` npm package
2. **Parse** compiled minified JavaScript via `tools/updatePrompts.js`
3. **Extract** 110+ prompt strings → markdown files with YAML frontmatter (Claude Code version + template variables)

**Accuracy claim**: ±20 token tolerance from runtime values (interpolated template variables like `${BASH_TOOL_NAME}` appear as literal strings).

**Update cadence**: Within minutes of each Claude Code release (implies automated CI/CD pipeline).

## Repository structure (root-only minimal)

```
claude-code-system-prompts/
├── .gitignore                # 46 B
├── CHANGELOG.md              # 211 KB / 1,896 lines / 176 versions
├── CLAUDE.md                 # 1.6 KB / project instructions
├── LICENSE                   # 1 KB / MIT
├── README.md                 # 69 KB / 405 lines / full inventory
├── system-prompts/           # dir / 293 prompt files
└── tools/
    └── updatePrompts.js      # 19.5 KB / extraction script
```

**Lean-governance discipline**: NO CI config files visible in root, NO tests directory, NO CONTRIBUTORS / CONTRIBUTING / CODE_OF_CONDUCT / SECURITY / PRIVACY files. **Contrast with claude-seo v64's 13+ governance files** — reference archives need minimal governance.

## Key disciplines encoded

### 1. Author-attribution discipline
Project CLAUDE.md explicitly states: *"Maintained by Piebald AI, not by Anthropic."*

### 2. Source-availability disclosure
Project CLAUDE.md: *"Source code is not publicly available."*

### 3. Modification-impact disclosure
Project CLAUDE.md: *"Editing files here does not change Claude Code's behavior."*

### 4. Quantified-accuracy disclosure
README: *"Likely not beyond ±20 tokens, however."*

### 5. AI-agent-meta-instruction
Project CLAUDE.md has dedicated "For AI agents working with this repository" section — **corpus-first formal section addressed to AI agents about meta-nature of the archive**.

### 6. Versioned absorption ledger
CHANGELOG: **176 versions tracked** (127 full + 49 no-change placeholder) with per-version commit hash + token delta + per-prompt change description.

### 7. Per-file YAML frontmatter
Every prompt file has YAML frontmatter recording Claude Code version + template variables. **Per-file independent versioning at extraction granularity.**

### 8. Marker conventions
`**NEW:**` for entirely new prompt files; `**REMOVED:**` for removed prompts. Documented in HTML comment at top of CHANGELOG: *"Only use **NEW:** for entirely new prompt files, NOT for new additions/sections within existing prompts."*

## Sister-tool: tweakcc

[`github.com/Piebald-AI/tweakcc`](https://github.com/Piebald-AI/tweakcc) — separately-maintained companion tool for **local patching** of Claude Code installations:

- Customize individual prompt pieces as markdown files
- Patch local npm-based or native binary Claude Code installation
- Diffing and conflict management for upstream updates

**Two-product observe-and-modify stack**: claude-code-system-prompts (observation) + tweakcc (modification) = complete control plane over local Claude Code prompts.

## Pattern Library implications snapshot

**Direct strengthenings (within already-CONFIRMED or -CANDIDATE patterns):**

1. **Pattern #78 Living-Domain-Standards Tracking N=2** — STRONGEST single-vendor-product-internals example
2. **Pattern #21 System Prompts Leaks N=2** — continuous-extraction sub-variant
3. **Pattern #19 ecosystem-portfolio-builder N=4 (corporate-org)** — Piebald commercial + claude-code-system-prompts + tweakcc
4. **Pattern #57 Recursive Corpus Reference 57c STRONGEST** — corpus-recursive at maximum depth
5. **Pattern #66 Supply Chain Awareness OT extension** — meta-supply-chain-awareness disclosure

**NEW top-level candidate:**

6. **Pattern #79 Continuous-Reverse-Engineering Reference Archive N=1 stale-flagged**

See Entity 2 + Entity 3 + Entity 4 for full Pattern Library implications.

## Why this entity matters

This is **the foundation reference** for understanding what claude-code-system-prompts IS as artifact. The 3 other entity pages build on this foundation to develop:
- Entity 2 — Pattern #78 N=2 promotion proposal (PRIMARY deliverable)
- Entity 3 — Piebald-AI ecosystem analysis (Pattern #19 N=4)
- Entity 4 — Storm Bear meta-entity (corpus-recursive maximum-depth observation)
