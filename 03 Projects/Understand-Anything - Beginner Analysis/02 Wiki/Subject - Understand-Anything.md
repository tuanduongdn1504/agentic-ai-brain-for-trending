# Subject — Understand-Anything

**Repo**: https://github.com/Lum1104/Understand-Anything
**Homepage**: https://understand-anything.com
**Live demo**: https://understand-anything.com/demo/
**Owner**: [[Owner - Yuxiang Lin]] (Lum1104, Shenzhen China + Georgia Tech)
**License**: MIT
**Primary language**: TypeScript
**Created**: 2026-03-15 (71 days old at v94 ship)
**Last push**: 2026-05-24 (1 day before v94 fetch — actively maintained)
**Tagline**: "Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about."

## Core metrics (v94 fetch, 2026-05-25)

| Metric | Value |
|---|---|
| Stars | 27,025 |
| Forks | 2,307 |
| Watchers (subscribers) | 111 |
| Open issues | 31 |
| Velocity | **~380.6 stars/day** = Pattern #52 EXTREME-VIRAL pulse-class |
| 90-day sub-class threshold | NOT YET satisfied at 71d (watch v97/v98 for promotion to Multi-Month-Sustained N=3) |
| Trendshift badge | Yes — featured at trendshift.io/repositories/23482 |

## What it is

A multi-platform plugin (primarily Claude Code) that turns any codebase, knowledge base, or docs into an interactive knowledge graph. Users invoke `/understand` to run a multi-agent analysis pipeline that produces a `.understand-anything/knowledge-graph.json` artifact + an interactive dashboard.

### Commands

| Slash command | Purpose |
|---|---|
| `/understand` | Run full multi-agent pipeline on current codebase; produces knowledge-graph.json |
| `/understand-dashboard` | Launch interactive dashboard (75% graph + 360px sidebar; React Flow + Zustand + TailwindCSS v4) |
| `/understand-chat` | Ask natural-language questions about the codebase |
| `/understand-diff` | Diff impact analysis — show which parts of system the current changes affect |
| `/understand-explain` | Deep-dive into a specific file or function |
| `/understand-onboard` | Generate onboarding guide for new team members |
| `/understand-domain` | Extract business domain knowledge (domains + flows + steps) — uses `domain-analyzer` agent |
| **`/understand-knowledge`** | **Analyze a Karpathy-pattern LLM wiki** — extract entities + claims + implicit relationships from articles via `article-analyzer` agent |

### 7-agent specialized pipeline

| Agent | Role |
|---|---|
| `project-scanner` | Discover files, detect languages + frameworks |
| `file-analyzer` | Extract functions/classes/imports; produce graph nodes + edges (parallel, ≤5 concurrent, 20-30 files/batch) |
| `architecture-analyzer` | Identify architectural layers (API / Service / Data / UI / Utility) |
| `tour-builder` | Generate guided learning tours ordered by dependency |
| `graph-reviewer` | Validate graph completeness + referential integrity (inline default; `--review` for full LLM review) |
| `domain-analyzer` | Extract business domains, flows, process steps (used by `/understand-domain`) |
| `article-analyzer` | Extract entities, claims, implicit relationships from wiki articles (used by `/understand-knowledge`) |

### Architecture stack

- **Monorepo**: pnpm workspaces (Node ≥22, pnpm ≥10)
- **`packages/core`**: Shared analysis engine — tree-sitter (via `web-tree-sitter` WASM), persistence, schema, tours, plugins, search (BM25 + regex hybrid). Subpath exports (`./search`, `./types`, `./schema`) to avoid pulling Node.js modules into browser.
- **`packages/dashboard`**: React + TypeScript dashboard — React Flow + Zustand + TailwindCSS v4 + prism-react-renderer source viewer
- **`understand-anything-plugin/`**: Claude Code plugin packaging all source code
- **5-plugin-manifest sync discipline**: Version bumps must hit all of `understand-anything-plugin/package.json` + `understand-anything-plugin/.claude-plugin/plugin.json` + root `.claude-plugin/plugin.json` + `.cursor-plugin/plugin.json` + `.copilot-plugin/plugin.json`

### Tree-sitter + LLM hybrid architecture

Same input → same output deterministic edges via tree-sitter (concrete syntax tree → imports / exports / function/class definitions / call sites / inheritance). LLM layer reads parsed structure alongside original source to produce plain-English summaries, tags, architectural-layer assignments, business-domain mapping, guided tours, language-concept callouts.

WASM-based tree-sitter (`web-tree-sitter`) instead of native `tree-sitter` because native bindings fail on darwin/arm64 + Node 24 — corpus-first WASM-substrate-tolerance-workaround in v60+ window.

### Multi-platform distribution (14 platforms)

| Platform | Install method |
|---|---|
| Claude Code | `/plugin marketplace add Lum1104/Understand-Anything` then `/plugin install understand-anything` |
| Cursor | Auto-discovery via `.cursor-plugin/plugin.json` |
| VS Code + GitHub Copilot | Auto-discovery via `.copilot-plugin/plugin.json` (Copilot v1.108+) |
| Copilot CLI | `copilot plugin install Lum1104/Understand-Anything:understand-anything-plugin` |
| Codex | `install.sh codex` |
| OpenCode | `install.sh opencode` |
| OpenClaw | `install.sh openclaw` |
| Antigravity | `install.sh antigravity` |
| Gemini CLI | `install.sh gemini` |
| Pi Agent | `install.sh pi` |
| Vibe CLI | `install.sh vibe` |
| Hermes | `install.sh hermes` |
| Cline | `install.sh cline` |
| KIMI CLI | `install.sh kimi` |

`install.sh` clones to `~/.understand-anything/repo` and creates platform-specific symlinks. Update: `./install.sh --update`. Uninstall: `./install.sh --uninstall <platform>`.

### 8-locale i18n

Primary English + 7 translations maintained alongside (`READMEs/`):
- 简体中文 (zh-CN)
- 繁體中文 (zh-TW)
- 日本語 (ja-JP)
- 한국어 (ko-KR)
- Español (es-ES)
- Türkçe (tr-TR)
- Русский (ru-RU)

`--language` parameter affects node summaries, dashboard UI labels, and guided tour explanations. Supported runtime values: `en` (default) / `zh` / `zh-TW` / `ja` / `ko` / `ru`.

### Graph-as-shareable-JSON workflow

- Knowledge graph is JSON — commit `.understand-anything/` (except `intermediate/` and `diff-overlay.json`) to team repo so teammates skip the pipeline
- Auto-update via `/understand --auto-update` (post-commit hook incrementally patches the graph)
- Large graphs (10MB+) tracked with **git-lfs**
- Example public-graph: `Lum1104/microservices-demo` fork with committed graph

## Pattern Library cross-references

### Pattern #52 EXTREME-VIRAL pulse-class N+1 strengthening

380.6/d × 71d = within EXTREME-VIRAL pulse threshold (>300/d), NOT YET Multi-Month-Sustained sub-class (<90d). If sustained 19+ more days, promotes to Multi-Month-Sustained EXTREME-VIRAL **N=3 PROMOTION** (joining v78 ECC + v85 ui-ux-pro-max). Watch v97/v98 audit.

### Pattern #57 sub-variant 57c-product STRONGEST corpus-citation density

~13 corpus-subject overlaps in platform-list + topic-tags = possible CORPUS-RECORD challenging v85's 10-corpus-subject-citation density:

- Claude Code (v65 + multiple harness instances)
- Codex (v62 codex-plugin-cc anchor)
- OpenCode (v67 opencode-antigravity-auth anchor)
- Antigravity (v67 sibling-context)
- Cursor (v75/v76 references)
- VS Code Copilot (v76 references)
- Copilot CLI
- Gemini CLI (v77 + others)
- Pi Agent (referenced in v75 + v76)
- Vibe CLI (v79 autoresearch_folktales)
- Hermes (v78 ECC operator)
- KIMI CLI (v89 references)
- Cline + OpenClaw (v82 huashu reference)

### Pattern #84 84c.1 Marketplace-Plugin-Install N=5 POST-PROMOTION STRENGTHENING

v85 + v90 + v92 + v93 + **v94** = 5-instance arc. `/plugin marketplace add Lum1104/Understand-Anything` + `/plugin install understand-anything` matches the 84c.1 sub-sub-mechanism canonical install-pattern.

### Pattern #19 NEW sub-mechanism 19q candidate

"Chinese-Mainland-Origin + US-Academic Profile" PROVISIONAL N=1 — Lum1104 = Yuxiang Lin Shenzhen-resident + Georgia Tech-affiliated, distinct from existing Pattern #19 sub-mechanisms:
- v82 alchaincyf (Chinese-Mainland solo-influencer + book author)
- v83 / v91 nexu-io (indie-org, locale-uncertain → China-Mainland inferred)
- v94 NEW: grad-student-at-Western-university profile

### Pattern #18 within-pattern strengthening

Multi-CLI cross-platform distribution at NEW sub-variant "auto-discovery via `.{platform}-plugin/plugin.json` directory convention" — Cursor + VS Code Copilot auto-discover via `.cursor-plugin/plugin.json` + `.copilot-plugin/plugin.json` directory naming. Distinct from v85 multi-symlink-architecture + v88 canonical-snippet auto-insertion.

### Pattern #66 supply-chain awareness

Dashboard source-content endpoint gated by access-token + graph-derived path-allowlist — distinct from v75 + v76 supply-chain-awareness instances. Within-pattern strengthening at code-viewer-security-discipline.

### Pattern #83 honest-deficiency-disclosure within-pattern

Project CLAUDE.md documents gotchas explicitly: tree-sitter native-binding failure on darwin/arm64 + Node 24; dashboard browser-import discipline; #167 issue about `inherit` model-field rejection by opencode. Pattern #83 at developer-documentation scope.

### Pattern #78 Living-Domain-Standards within-pattern

`.understand-anything/knowledge-graph.json` schema + multi-platform plugin manifests (5-plugin.json + marketplace.json) + agent definitions = mid-density LDS at single-Plugin scope. Distinct from v76 259-skill scope + v85 669+-codified-elements scope.

### Pattern #82 quantitative-marketing strengthening

5+ claims in README first 25 lines:
- "200,000 lines of code" framing
- "up to 5 concurrent, 20-30 files per batch"
- "10MB+" git-lfs threshold
- "incremental by default (only re-analyzes changed files)"
- 14-platform compatibility table

## Library-vocab candidates (PROVISIONAL N=1 registrations at v94)

### PRIMARY

**Karpathy-LLM-Wiki-Pattern Corpus-Recursive Closure at Methodology-Influence Layer** — see Phase 4b PRIMARY proposal-document for full registration. Third corpus-recursive event-class distinct from v78-anchor-self-reference + v76↔v93-direction-reversal.

### Sister-observations

1. **Karpathy-LLM-Wiki-Pattern as First-Class Product Feature** — captures the product-feature axis specifically
2. **Tree-sitter + LLM Hybrid Architecture for Reproducible-Structure-Plus-Semantic-Intent**
3. **WASM-Tree-sitter Substrate-Tolerance Workaround** (Pattern #84 84d candidate?)
4. **5-File Plugin Version-Sync Discipline**
5. **Auto-Discovery via .{platform}-plugin/plugin.json Directory Convention**
6. **Persona-Adaptive UI at Knowledge-Graph Tool Scope**
7. **Graph-as-Shareable-JSON Commit-to-Team-Repo Discipline**

## Pilot recommendation

**Tier-1 actionable position #1 NEW** — most direct vault-utility test in v60+ corpus. Storm Bear's vault is **literally** a Karpathy-pattern LLM wiki; v94's `/understand-knowledge` command is built to analyze exactly this structure.

```bash
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
/understand-knowledge ~/path/to/KJ\ OS\ Template
```

Cost: ~5-10 min. Reversible: `/plugin uninstall understand-anything`. Existing-infrastructure-overlap: vault itself + Claude Code daily usage.

## Outstanding questions for operator review

1. **Pilot decision**: trial v94 against vault now? (Tier-1 #1 actionable position; would visualize cross-wiki structure that's currently distributed across `_state/` + `_patterns/` chapter files)
2. **Cultural-cluster classification**: file Lum1104 under (a)-6 cluster-extension at China-Mainland sub-cluster N=4 (v82+v83+v91+v94) OR carve NEW sub-cluster for Chinese-Mainland-origin + Western-academic profile?
3. **Pattern #57 57c-product CORPUS-RECORD verification at v95 audit**: confirm 13-corpus-subject citation density via per-citation pressure-test (routine v2.3 §15); compare against v85's 10-citation prior record
4. **(a) sub-axis (a)-7 v92+v93 N=2 STRENGTHENING co-occurrence**: v94 does NOT contribute (a)-7 evidence (Lin not Anthropic-affiliated); separate axis from v93 — verify
