# Cluster — Combined source summary (OpenSpec v58)

> Compressed-scope build mode (per v56 + v57 lessons). Single combined cluster covers user-facing docs + contributor-facing docs + technical/distribution surfaces.

## Sources probed

1. https://github.com/Fission-AI/OpenSpec — repo landing
2. https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/README.md — primary README
3. https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/package.json — npm package metadata
4. https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/supported-tools.md — 30+ tools enumeration
5. https://github.com/Fission-AI — Fission-AI org page

## Repository metadata (verbatim where possible)

| Field | Value |
|---|---|
| **Tagline** | "Spec-driven development (SDD) for AI coding assistants" |
| **Stars** | 45,800 |
| **Forks** | 3,200 |
| **Watchers** | 225 |
| **Open issues** | 225 |
| **Primary language** | TypeScript 98.9% |
| **License** | MIT |
| **Latest release** | v1.3.1 (April 21, 2026) |
| **Homepage** | openspec.dev |
| **Author/Org** | Fission-AI (org "no public members") |
| **Package name** | `@fission-ai/openspec` |
| **Bin entry** | `openspec` → `./bin/openspec.js` |
| **Node requirement** | `>=20.19.0` |
| **Top-level files** | `AGENTS.md / CHANGELOG.md / LICENSE / MAINTAINERS.md / README.md / README_OLD.md / WORKSPACE_REIMPLEMENTATION_*.md / build.js / eslint.config.js / flake.lock / flake.nix / openspec-parallel-merge-plan.md / package.json / package-lock.json / pnpm-lock.yaml / tsconfig.json / vitest.config.ts / vitest.setup.ts / .actrc / .coderabbit.yaml / .gitignore` |
| **Top-level dirs** | `.changeset / .devcontainer / .github / assets / bin / docs / openspec / schemas/spec-driven / scripts / src / test` |

## Positioning verbatim

> "Spec-driven development (SDD) for AI coding assistants"

> "AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written."

## 5 explicit principles

> "→ fluid not rigid
> → iterative not waterfall
> → easy not complex
> → built for brownfield not just greenfield
> → scalable from personal projects to enterprises"

## Comparison verbatim (Pattern #57 57c forward-citation evidence)

**vs. Spec Kit (GitHub):**

> "Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely."

**vs. Kiro (AWS):**

> "Powerful but you're locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use."

**vs. no specifications:**

> "AI coding without specs means vague prompts and unpredictable results. OpenSpec brings predictability without the ceremony."

**Note on anti-vibe positioning:** "vague prompts and unpredictable results" framing is structurally analogous to mattpocock v57 "real engineering, not vibe coding" — both v57 and v58 strengthen Pattern #51 anti-vibe pole consecutively.

## Quick start verbatim

```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init
```

Invocation: `/opsx:propose <what-you-want-to-build>`

## Workflow phases (proposal → specs → design → tasks → archive)

1. **Propose** (`/opsx:propose add-dark-mode`): Creates change folder containing proposal.md (rationale), specs/ (requirements), design.md (technical approach), tasks.md (implementation checklist)
2. **Apply** (`/opsx:apply`): Executes implementation tasks with progress tracking
3. **Archive** (`/opsx:archive`): Moves completed work to archive with updated specs

Extended commands: `/opsx:new`, `/opsx:continue`, `/opsx:ff`, `/opsx:verify`, `/opsx:bulk-archive`, `/opsx:onboard`

## 11 generated skill commands (per supported tool)

`openspec-propose / openspec-explore / openspec-new-change / openspec-continue-change / openspec-apply-change / openspec-ff-change / openspec-sync-specs / openspec-archive-change / openspec-bulk-archive-change / openspec-verify-change / openspec-onboard`

## 30+ supported AI tools (corpus-broadest multi-platform-by-design)

Amazon Q Developer / Antigravity / Auggie / IBM Bob Shell / **Claude Code** / Cline / CodeBuddy / Codex / ForgeCode / Continue / CoStrict / Crush / Cursor / Factory Droid / Gemini CLI / GitHub Copilot / iFlow / Junie / Kilo Code / Kimi CLI / **Kiro** / Lingma / OpenCode / Pi / Qoder / Qwen Code / RooCode / Trae / Windsurf

**Integration mechanisms:**
- **Skills installation** — pattern `openspec-*/SKILL.md` in tool-specific directories (`.claude/skills/`, `.cursor/skills/`, etc.)
- **Commands installation** — markdown / TOML / prompt formats per tool requirements

## Recommended models

> Opus 4.5 and GPT 5.2 (planning + implementation)

## Key dependencies (package.json)

- `commander` (CLI framework)
- `chalk` (terminal styling)
- `zod` (schema validation)
- `yaml` (YAML parsing)
- `ora` (loading spinners)
- `@inquirer/prompts` (interactive prompts)
- **`posthog-node` (analytics)** — supply-chain awareness flag for beginner guide caveats

## Fission-AI org

- Tagline: "From Idea to Action, Instantly"
- 2 public repos: OpenSpec (45.8K stars) + PR-QUEST (16 stars; "A more interactive & engaging way to review PR's!")
- Org page explicit: "This organization has no public members. You must be a member to see who's a part of this organization."
- Primary language: TypeScript
- No location / team size / founder identity disclosed

## Notable absences

- **No individual author attribution** in README or package.json (vs mattpocock v57 named-author + v18 agency-agents named-individual + v17 spec-kit Microsoft GitHub corporate-named-org)
- **No methodology citation chain to academic SDD literature** (vs mattpocock v57 5-book methodology lineage)
- **No "vibe coding" mention** despite anti-vibe-aligned positioning (different framing: "vague prompts and unpredictable results")
- **No CLAUDE.md** at repo root (AGENTS.md present instead — multi-tool-by-design)
- **Older README archived as README_OLD.md** — version evolution observable

## 8-12 corpus-first observations

1. **Corpus-broadest multi-platform-by-design (30+ tools)** — surpasses prior holders n8n v56 (16 LLM providers) + mattpocock v57 (8 platforms)
2. **2nd corpus SDD-methodology framework at T1** (after spec-kit v17 SDD) — same named-methodology lineage at same tier
3. **Pseudonymous-org with active-commercial-product** (Fission-AI) — corpus-first; v21 system-prompts-leaks was individual-pseudonymous + leaked-content (not active product)
4. **Per-tool skill-file generation as universal deployment format** — OpenSpec generates 11 skills × 30+ tools = 330+ artifacts; corpus-first cross-tool-skill-format-translator pattern
5. **Pattern #57 57c forward-citation** — OpenSpec README cites spec-kit v17 + Kiro (out-of-corpus) as anti-pattern foils → 57c grows N=7 → N=8 conservative-attribution post-v58
6. **Anti-vibe positioning 2 consecutive wikis** (v57 + v58) — Pattern #51 anti-vibe pole at 2nd-most-explicit position post-v57
7. **AGENTS.md present + CLAUDE.md absent** — multi-tool-by-design favors generic AGENTS.md over Claude-specific CLAUDE.md
8. **Nix flake.nix + flake.lock** — declarative reproducible-build setup uncommon in corpus
9. **`@inquirer/prompts` interactive prompts in CLI scaffolder** — sister-pattern to brain-setup-style interactive-discovery
10. **posthog-node telemetry-by-default in dev tool** — supply-chain awareness flag (Pattern #66 OBSERVATION-TRACK relevance)
11. **README_OLD.md preserved alongside README.md** — version-evolution-observable signal; uncommon discipline
12. **WORKSPACE_REIMPLEMENTATION_*.md notes at repo root** — design-decision documentation discipline observable

## Counter-evidence + supply-chain flags

- **Pattern #57 NEGATIVE for in-corpus citing-INTO-corpus**: OpenSpec cites spec-kit v17 (in-corpus) + Kiro (out-of-corpus) — Kiro citation does NOT advance 57c (requires in-corpus); only spec-kit citation counts (T1→T1 same-methodology N=1 instance for OpenSpec)
- **Supply-chain awareness:** posthog-node analytics dependency in dev tool — telemetry-by-default behavior should be flagged in beginner guide caveats section
- **Pseudonymity-vs-vault-publishing-discipline counter-example:** Fission-AI hidden members vs Storm Bear vault public-identifiable — useful contrast for vault publishing discipline (Phase 0.9 criterion (a) FAIL is structurally informative)
