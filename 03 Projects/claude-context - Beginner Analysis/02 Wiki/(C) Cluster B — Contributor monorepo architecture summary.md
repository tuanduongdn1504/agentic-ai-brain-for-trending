# (C) Cluster B — Contributor + monorepo architecture summary

> **Source files in cluster:** `CONTRIBUTING.md` (190 lines) + `packages/core/CONTRIBUTING.md` (1.2K) + `packages/mcp/CONTRIBUTING.md` (3.5K) + `packages/vscode-extension/CONTRIBUTING.md` (3.1K) + `packages/chrome-extension/CONTRIBUTING.md` (7.1K) + `package.json` + `pnpm-workspace.yaml` + `.npmrc` + build scripts + Git history
> **Scope:** Developer setup + monorepo build/release + per-package architecture + contribution workflow + governance structure

---

## 1. Monorepo architecture

**Tool:** pnpm workspaces (pnpm >= 10.0.0 required; Node.js 20.x-22.x)

**From `pnpm-workspace.yaml`:**
```yaml
packages:
  - packages/*
  - examples/*
ignoredBuiltDependencies:
  - faiss-node
```

**Build orchestration (from `package.json` root scripts):**
```json
"build": "pnpm -r --filter='!./examples/*' build && pnpm -r --filter='./examples/*' build"
"build:core": "pnpm --filter @zilliz/claude-context-core build"
"build:vscode": "pnpm --filter semanticcodesearch compile"
"build:mcp": "pnpm --filter @zilliz/claude-context-mcp build"
"release:core": "pnpm --filter @zilliz/claude-context-core... run build && pnpm --filter @zilliz/claude-context-core publish --access public --no-git-checks"
"release:mcp": "pnpm --filter @zilliz/claude-context-mcp... run build && pnpm --filter @zilliz/claude-context-mcp publish --access public --no-git-checks"
"release:vscode": "pnpm --filter @zilliz/claude-context-core build && pnpm --filter semanticcodesearch run webpack && pnpm --filter semanticcodesearch release"
"benchmark": "node scripts/build-benchmark.js"
```

**Observations:**
- **4 separate release targets** — core / mcp / vscode / (chrome coming)
- **No lockstep versioning** (unlike pi-mono v36's 200+ lockstep releases). Per-package independent versioning — pragmatic for independent package consumers.
- **`--no-git-checks`** — bypass git cleanliness check for publish (speed over safety; acceptable for corporate-startup dev velocity).
- **`benchmark` script** — `scripts/build-benchmark.js` exists; Phase 2 probe confirmed build-benchmark.json at root.

### 4-package breakdown

| Package | Public name | Role | Distribution |
|---------|-------------|------|--------------|
| **core** | `@zilliz/claude-context-core` | Core indexing engine (embedding + vector DB + splitter + sync abstraction) | npm (public) |
| **mcp** | `@zilliz/claude-context-mcp` | MCP protocol server (4 tools: index / search / clear / status) | npm (public) |
| **vscode-extension** | `semanticcodesearch` | VS Code extension | Visual Studio Marketplace |
| **chrome-extension** | (unnamed public) | GitHub browser code search | Chrome Web Store (Coming Soon) |

### 5 source-tree modules in core

From `packages/core/src/`:
1. **embedding/** — OpenAI + VoyageAI + Gemini + Ollama abstraction
2. **splitter/** — AST (Tree-sitter) + LangChain character-based
3. **sync/** — Incremental synchronization (Merkle-tree logic likely here)
4. **vectordb/** — Milvus + Zilliz Cloud adapters
5. **utils/** — support utilities

Plus top-level files:
- `context.ts` (50.6K) — main Context orchestrator
- `handlers.ts` (49.7K) — handler registration
- `snapshot.ts` (24.2K) — snapshot/state management (likely Merkle-tree implementation)
- `config.ts` (11.2K) — config validation + defaults
- `embedding.ts` (4.6K) + `sync.ts` (6.9K) — top-level wrappers

**`snapshot.ts` 24.2K size is architectural signal** — substantial state-management infrastructure, consistent with Merkle-tree incremental indexing claim in README.

---

## 2. CONTRIBUTING.md governance analysis

### Structure (190 lines, 12 sections)

1. Getting Started (prereqs + Fork/Clone + Platform-Specific Setup + Install + Build + Dev)
2. Project Structure (verbatim monorepo tree diagram)
3. Package-Specific Development (links to 3 per-package CONTRIBUTING.md)
4. Development Workflow (Building + Package-Specific)
5. Making Changes (Commit Guidelines — conventional commits + PR Process)
6. Contribution Areas (Priority + Ideas for Contribution)
7. Reporting Issues
8. Getting Help (GitHub Issues + Discussions — NOTE: Discord not directed for issues)
9. License

### Conventional commits (enforced)

Format: `type(scope): description`

**Types:** `feat` / `fix` / `docs` / `refactor` / `perf` / `chore`

**Scopes:** `core` / `vscode` / `mcp` / `examples` / `docs`

**6 types + 5 scopes = 30-combination matrix.** Standard conventional-commits; not novel in corpus but disciplined.

### Priority areas (verbatim)

- Core Engine (indexing performance/accuracy)
- Embedding Providers (add more embedding services)
- Vector Databases (extend integration options)
- Documentation (examples + guides)
- Bug Fixes (reported issues)

### Contribution ideas (verbatim)

- New programming languages (Tree-sitter grammar additions)
- Code chunking strategies improvement
- Search result ranking enhancement
- Configuration options
- More usage examples

**Observation:** CONTRIBUTING.md is practical and extension-focused — invites specific types of PRs (new languages, new embedding providers, new vector DBs) rather than framework-general refactors.

### Governance absences (Pattern #22 + #24 observations)

- **AGENTS.md:** ❌ ABSENT at repo root (continues T4-abstention majority: graphify v16 / GitNexus v33 / markitdown v28 / crawl4ai v29 all abstain; only gws v13 has formal AGENTS.md at T4)
- **SECURITY.md:** ❌ ABSENT at root (Pattern #24 T1-standard; T4 weaker norm)
- **CODE_OF_CONDUCT.md:** ❌ ABSENT
- **SUPPORT.md:** ❌ ABSENT (Discord + GitHub Issues/Discussions direction in CONTRIBUTING instead)

**Governance profile at T4 commercial-startup:** light + distributed (per-package CONTRIBUTINGs + single root CONTRIBUTING). No corporate-formalization depth (unlike spec-kit v17 6-file set). Consistent with Pattern #12 governance-depth-correlates-with-organization refinement: **commercial-startup ≠ big-corp formalization depth.** Zilliz-scale commercial is between solo-governance and big-corp-governance.

---

## 3. Per-package CONTRIBUTING.md observations

### packages/core/CONTRIBUTING.md (1.2K)
Thin — refers back to root CONTRIBUTING.md for most workflow. Adds core-specific build commands + source-tree overview.

### packages/mcp/CONTRIBUTING.md (3.5K)
MCP-specific: MCP server debugging via MCP Inspector + stdio-transport troubleshooting + env-variable propagation patterns. Corpus-first MCP-server-specific contributor doc observed.

### packages/vscode-extension/CONTRIBUTING.md (3.1K)
VS Code extension-specific: webpack config + Marketplace publishing + extension manifest + `@vscode/vsce` tooling. Also vscode-extension has own LICENSE (MIT) — redundant but safe.

### packages/chrome-extension/CONTRIBUTING.md (7.1K)
**Largest per-package CONTRIBUTING** — suggests Chrome extension is actively developed despite "Coming Soon" Marketplace status. Likely contributor-attraction signal for browser-ext work.

**Meta-observation:** 4-tier CONTRIBUTING hierarchy (root + 4 per-package) = structurally distributed governance without corporate-formalized depth. Practical developer onboarding prioritized over compliance theater.

---

## 4. Commit history analysis

**168 commits on master branch** — recent scaffolding phase (~1 year project, active).

From `git log` patterns visible in clone (last 5 commits observed during probe):
- Milvus gRPC fixes (infrastructure maintenance)
- Custom collection-name support (feature extension)
- Active development cadence

**Repo activity:** healthy — last pushed same week as WebFetch (2026-04-22 confirmed as "pushed" signal).

---

## 5. Dev tooling stack

**From `package.json` devDependencies:**

| Tool | Version | Role |
|------|---------|------|
| `@types/node` | ^20.0.0 | TypeScript types |
| `@typescript-eslint/eslint-plugin` + `parser` | ^8.31.1 | Lint |
| `eslint` | ^9.25.1 | Lint engine |
| `typescript` | ^5.8.3 | Language |
| `rimraf` | ^6.0.1 | Cross-platform clean |
| `tree-sitter-cli` | ^0.25.6 | AST grammar CLI |
| `assert` / `browserify-zlib` / `https-browserify` / `stream-http` / `url` / `vm-browserify` / `os-browserify` | various | Browser polyfills (for VSCode webview + Chrome Ext WASM) |

**Stack observations:**
- **Tree-sitter explicit** (corpus-first T4 code-indexing with tree-sitter-cli dev dep exposed) — validates AST-chunking claim structurally
- **No test runner explicit at root** (tests likely per-package)
- **Browser polyfills** — `browserify-zlib` + `https-browserify` + `stream-http` + `url` + `vm-browserify` + `os-browserify` = VSCode webview / browser-extension compatibility layer
- **ESLint + TypeScript strict** — enforced via `lint` / `typecheck` root scripts

**`.npmrc` (427B observed):** likely pnpm + npm registry config; not unusual.

**`.eslintrc.js` (749B):** rules config; standard.

---

## 6. Examples directory

From `examples/README.md` (86 bytes — minimal):
> Points to `basic-usage/` — *"Basic indexing and search example"*

**`basic-usage/`** is the single example. Contents not probed in depth (outside scope) but listed in `pnpm-workspace.yaml` as workspace package.

**Corpus-first observation at T4 code-indexing:** **Workspace-level example as first-class monorepo citizen.** Most T4 wikis have external-repo examples or doc-embedded snippets; claude-context bundles `basic-usage` inside the repo as a workspace package that consumes `@zilliz/claude-context-core` like any external user would.

---

## 7. Build benchmark & release discipline

**`scripts/build-benchmark.js`** (referenced but not deeply probed) + `build-benchmark.json` (927 bytes) at root.

**Benchmark purpose (inferred):** Build-time regression detection. Performance culture: Zilliz-scale vector infrastructure demands measurable build stability.

**Release discipline:**
- 3 separate release scripts (core / mcp / vscode)
- `--access public` for npm (unscoped access)
- `--no-git-checks` flag accepts unclean working tree (startup-velocity tradeoff)

---

## 8. Governance density comparison to T4 peers

| Wiki | Root govt files | Per-package govt | AGENTS.md | SECURITY.md | CODE_OF_CONDUCT |
|------|-----------------|------------------|-----------|-------------|-----------------|
| gws v13 (corporate-broad) | 3+ | N/A | ✅ (tri-file) | ✅ | — |
| notebooklm-py v7 (solo-narrow) | 1-2 | N/A | — | — | — |
| graphify v16 (solo-broad-local) | 3 | N/A | ✅ | ✅ (first standalone) | — |
| TrendRadar v19 (solo-broad-external-regional) | 2-3 | N/A | — | — | — |
| markitdown v28 (corporate-narrow-utility) | 3-4 | N/A | CLA + CoC | — (implicit) | ✅ |
| crawl4ai v29 (solo-enterprise-scale) | 3-4 | N/A | — | — | — |
| GitNexus v33 (solo-student-with-commercial) | 3-4 | N/A | — | — | — |
| **claude-context v40 (commercial-ecosystem-startup)** | **3 (README + LICENSE + CONTRIBUTING)** | **4 per-package CONTRIBUTINGs** | ❌ | ❌ | ❌ |

**Observation:** claude-context governance is **distributed across monorepo** (root + 4 per-package CONTRIBUTINGs) rather than **consolidated at root** (norm for non-monorepo T4). Different spatial distribution, similar overall depth. No exceptional formalization.

---

## 9. Pattern Library observations

| Pattern | Status | Observation |
|---------|--------|-------------|
| #2 Distribution Evolution | Strengthening | 4-package monorepo + per-package releases + workspace-level example |
| #12 Governance-Depth | Observational refinement | **Commercial-startup corporate ≠ big-corp formalization.** Zilliz governance lighter than Microsoft/Google corporate (markitdown v28 / gws v13); heavier than solo (graphify v16 same-depth but monorepo-distributed) |
| #22 AGENTS.md T4-abstention | Strengthening | 5 of 8 T4 wikis abstain (claude-context continues trend) |
| #24 SECURITY.md T1-standard | T4-absence observation | At T4, SECURITY.md is minority convention |
| #17 variant 3 commercial-startup | Strengthening | Monorepo + 4-package release independence = commercial-startup ecosystem operations |

---

## 10. Novel observations / corpus-firsts

1. **4-tier distributed governance** — root CONTRIBUTING + 4 per-package CONTRIBUTINGs; monorepo-native governance profile at T4
2. **Workspace-level `basic-usage` example as first-class monorepo citizen** — vs external doc snippets common at T4
3. **`--no-git-checks` publish-flag** — startup-velocity explicit tradeoff
4. **4 independent release targets** vs pi-mono v36's 200-release lockstep — commercial-startup opts for per-package independence
5. **Build-benchmark infrastructure** — `scripts/build-benchmark.js` + `build-benchmark.json`; performance-culture signal
6. **Per-package CONTRIBUTING size signals priority:** chrome-extension 7.1K (largest; "Coming Soon" but actively contributor-attractive) > mcp 3.5K > vscode 3.1K > core 1.2K
7. **Browser polyfill surface** — 7 polyfills (browserify-zlib + https-browserify + stream-http + url + vm-browserify + os-browserify + assert) indicates serious VSCode webview + Chrome Extension runtime coverage

---

## 11. Summary

claude-context monorepo is a **4-package pnpm workspace** (core + mcp + vscode-ext + chrome-ext) with **per-package independent releases** + **workspace-level example**. Governance is **distributed light** — root CONTRIBUTING + 4 per-package CONTRIBUTINGs + MIT license; AGENTS.md + SECURITY.md + CODE_OF_CONDUCT absent. Conventional commits enforced (6 types × 5 scopes). Build-benchmark infrastructure signals performance culture. 4-package structure reflects distinct product surfaces: MCP (agent-audience) + VSCode (IDE-audience) + Chrome (browser-audience) + Core (library-audience). Commercial-startup governance depth is between solo and big-corp — distributed but not formalized.
