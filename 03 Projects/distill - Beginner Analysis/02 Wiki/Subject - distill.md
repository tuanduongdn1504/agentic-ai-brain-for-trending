# Subject — distill

**Repo**: https://github.com/samuelfaj/distill
**Owner**: Samuel Fajreldines (individual)
**Owner profile**: Rio Grande do Sul, Brazil + @smartplan-br company + blog samuelfaj.com + Twitter handle absent + 43 followers / 14 following / 68 public repos / GitHub since 2015-06-22 (11-year account) + bio `Github:~ samuelfaj$ `
**Tier**: T2 Service (CLI compression tool with bundled local LLM) + T1 Assistant Skill side-artifact (`skills/distill/` packaged Claude Code skill)
**License**: **NULL** (no LICENSE file; README does not declare a license)
**Primary language**: TypeScript (with bun.lock + npm workspaces hybrid)
**Created**: 2026-03-06 (80 days old at v97 ship)
**Last push**: 2026-05-19 (6 days before fetch)
**Description**: "Distill large CLI outputs into small answers for LLMs and save tokens!"
**Homepage**: not set
**Topics**: claude-code, codex, llm, tokens
**Discussions**: DISABLED

## Core metrics (v97 fetch, 2026-05-25)

| Metric | Value |
|---|---|
| Stars | 559 |
| Forks | 33 |
| Subscribers | **1** (CORPUS-LOW engagement-deficit territory; matches v76+v87+v88+v89 cluster) |
| Open issues | 4 |
| Open PRs | 0 (inferred from `subscribers_count=1` + no open PR signal) |
| Velocity | 559 / 80 days = **~7.0 stars/day LOW** (well below all Pattern #52 sub-class floors; not a Pattern #52 instance) |
| Fork ratio | 33/559 = 0.059 = 5.9% MID-LOW (within healthy range; below v76 corpus-record 0.296) |
| Total contributors | 3 (samuelfaj 68 commits + dev-gboy 1 + rafek1241 1 = effectively solo + 2 single-PR drive-by) |
| Repo size | 689 KB |
| Version | 1.5.2 (per package.json) |

## What it is

A CLI tool that compresses CLI command outputs (logs, test results, stack traces, large rg/grep/find dumps) into minimal answers for downstream LLM consumption. Operator pipes any large CLI output through `distill "<question>"` and receives a compressed answer using the bundled local fine-tuned LLM.

Headline claim from README:

> **🔥 `distill` compresses command outputs into only what the LLM actually needs. Save up to 99% of tokens without losing the signal.**

Worked example from README:

```sh
rg -n "terminal|PERMISSION|permission|Permissions|Plan|full access|default" desktop --glob '!**/node_modules/**' | distill "find where terminal and permission UI are implemented in chat screen"
```

| | Before | After |
|---|---|---|
| Tokens | 7,648 | 99 |
| Characters | 30,592 | 396 |
| Words | 10,218 | 57 |
| Reduction | — | **~98.7% saved** |

## Architecture

### Monorepo workspace

```
distill/
├── packages/
│   ├── cli/                       # CLI orchestrator (npm-published as @samuelfaj/distill)
│   ├── distill-darwin-arm64/      # Platform-binary: Apple Silicon
│   ├── distill-darwin-x64/        # Platform-binary: Intel Mac
│   ├── distill-linux-arm64/       # Platform-binary: Linux ARM
│   ├── distill-linux-x64/         # Platform-binary: Linux x64
│   └── distill-win32-x64/         # Platform-binary: Windows
├── src/                            # Shared TypeScript source
│   ├── cli.ts
│   ├── config.ts
│   ├── dataset.ts
│   ├── dsl-memory.ts
│   ├── llm.ts                     # LLM interface (calls bundled model)
│   ├── local-server.ts            # Local inference server
│   ├── onboarding.ts              # First-run UX
│   ├── prompt.ts
│   ├── stream-distiller.ts        # Streaming compression core
│   ├── text.ts
│   └── user-config.ts
├── skills/
│   └── distill/                   # Claude Code skill artifact (Pattern #84 84c.1)
├── .claude/
│   └── skills/                    # Claude Code skill install location
├── scripts/                       # Build/release scripts (Bun-run)
│   ├── build-binaries.ts
│   ├── sync-platform-packages.ts
│   ├── apply-platform-metadata.ts
│   ├── smoke-packages.ts
│   └── release-check.ts
├── test/
├── examples/
├── ANALYSIS.html                  # Published spec artifact
├── REQUIREMENTS.html              # Published spec artifact
├── TDD.html                       # Published spec artifact
├── TODO.html                      # Published spec artifact
├── bun.lock
├── package-lock.json
└── package.json                   # npm@11.7.0 workspace + bun build/test scripts
```

### Hybrid build + workspace tooling

`packageManager` is pinned to `npm@11.7.0` at the workspace root. All build/test/release scripts use `bun run`:

```json
"scripts": {
  "build:bins": "bun run scripts/build-binaries.ts",
  "sync:platforms": "bun run scripts/sync-platform-packages.ts",
  "build": "npm run build:bins && npm run sync:platforms",
  "prepare:publish-platforms": "bun run scripts/apply-platform-metadata.ts",
  "smoke:pack": "bun run scripts/smoke-packages.ts",
  "test": "bun test",
  "test:e2e": "bun test test/e2e.test.ts",
  "release:check": "bun run scripts/release-check.ts",
  "verify": "npm run test && npm run build && npm run release:check"
}
```

**Hybrid Bun + npm tooling pattern**: Bun for build/test/release-check (fast TypeScript execution + native test runner); npm for workspace + publish (mature workspace toolchain + npm registry). CORPUS-FIRST hybrid configuration in v60+ window.

### 5-platform-binary distribution via npm workspaces postinstall

User runs `npm i -g @samuelfaj/distill`. The CLI package depends on platform-specific binary packages; postinstall (via `os` + `cpu` `package.json` constraints) selects the correct platform-binary. This pattern is used at scale by `esbuild`, `swc`, `turbo` etc. but is **CORPUS-FIRST at solo-founder T2 service scale in v60+ window**.

Distinct from prior corpus distribution mechanisms:
- v83 nexu-io/open-design: 4-distribution-method matrix = source + Docker + Desktop Electron + Vercel (install-channel multiplicity)
- v85 nextlevelbuilder/ui-ux-pro-max-skill: 18-platform skill.json manifest (AI-CLI multi-CLI distribution)
- v97 distill: single install-channel (npm) + 5 platform-binary fan-out (platform-binary postinstall pattern)

### Bundled fine-tuned model

`samuelfaj/distill-1.7B-MLX` on Hugging Face:
- 1.7B parameters
- 4-bit quantization
- MLX framework (Apple Silicon Metal native)
- Distributed via Hugging Face Hub
- Auto-downloaded by `distill` onboarding on first run

Hardware requirements per README:
- 8 GB+ RAM safe-floor
- 16 GB+ comfortable

CORPUS-FIRST own-trained fine-tuned bundled Expert Language Model at single-subject solo-founder scale in 96-wiki corpus. PHASE 4b PRIMARY at v97. See proposal-document for full reasoning.

## Distill Language methodology

Secondary README section "Distill Language":

> We also teach your LLM to talk and think a more efficient way.

Accompanied by a `distill-language.png` reference image embedded in README. The methodology layer: the bundled model is fine-tuned not just on compression task but on a learned shorthand/DSL the README calls "Distill Language" that the operator's downstream LLM (Claude, Codex, etc.) is also trained to comprehend.

This is a **compression-as-trainable-discipline at LLM-output layer** that goes beyond mechanical text-summarization. CORPUS-FIRST in v60+ window.

## Spec-as-HTML-Published-at-Repo-Root

Four HTML artifacts at repo root:
- `ANALYSIS.html` (3,089 B)
- `REQUIREMENTS.html` (3,335 B)
- `TDD.html` (2,006 B)
- `TODO.html` (1,593 B)

These are dev-process documents (analysis + requirements + Test-Driven-Design plan + TODO list) published as HTML directly at repo root, not in `/docs/` or wiki. CORPUS-FIRST in v60+ window.

Distinct from:
- Pattern #78 LDS sub-mechanism 78a (CLI-enforceable rule corpus) — those are operational artifacts
- Pattern #78 sub-mechanism 78b (in-tree-curriculum) — those are learning paths
- Pattern #78 sub-mechanism 78c (educational-curriculum-LDS) — those are pedagogy
- Pattern #78 sub-mechanism 78d (operator-system-LDS-with-6-layer-codification, v78 anchor) — that is multi-layer codification

v97 is **dev-process-spec published as HTML at root** = methodology-trail-as-published-artifact. Library-vocab PROVISIONAL N=1.

## Side artifact: Claude Code skill

`skills/distill/` directory contains a packaged Claude Code skill. The skill provides slash commands and agent-runtime integration for invoking distill from inside a Claude Code session (rather than only from a separate terminal pipe). Pattern #84 84c.1 N+1 strengthening (Marketplace-Plugin-Install / repo-stored-skill mechanism).

7-instance arc:
- v85 ui-ux-pro-max-skill (anchor)
- v90 academic-research-skills (N=2 strengthening)
- v92 claude-for-legal (N=3 PROMOTION-LOCKED-IN)
- v93 anthropics/skills (N=4 strengthening)
- v94 Understand-Anything (N=5 strengthening)
- v95 claude-plugins-official (N=6 PROMOTION CONFIRMED at v96 audit; 4-layer Pattern hierarchy formal)
- **v97 distill (N=7 post-confirmed strengthening)**

84c.1 sub-sub-mechanism remains CONFIRMED at N=6+ at 4-layer Pattern hierarchy.

## Pattern Library cross-references

### Phase 4b PRIMARY: NEW Library-vocab "Own-Trained Bundled Expert Language Model at Single-Subject Solo-Founder Scale" PROVISIONAL N=1

See `01 Analysis/(C) Own-Trained-Bundled-Expert-Language-Model-N1-registration.md` for full registration document with definition + anchor evidence + cross-axis variance scoping + promotion-eligibility ladder + v2.4 codification candidates.

### Pattern #84 84d Hardware-Substrate-Tolerance N=3 PROMOTION-ELIGIBLE administrative at v100 audit

| Wiki | Substrate | Variant |
|---|---|---|
| v79 autoresearch_folktales | PyTorch MPS (Apple Silicon) | Hardware-substrate-pinned + custom MPS workarounds (FlashAttention-3 removed; native PyTorch SDPA; torch.compile disabled) |
| v94 Understand-Anything | WASM (Tree-sitter) | Software-substrate-tolerance workaround for cross-platform parser |
| **v97 distill** | **MLX (Apple Silicon Metal native)** | **Hardware-substrate-pinned + bundled-fine-tuned-model variant** |

3-variant cross-substrate spread: PyTorch-Metal + WASM-software + MLX-Apple-native. Administrative-promotion-eligible at v100 audit per routine v2.3 §3 vehicle #1.

### Pattern #57 sub-variant 57c-product 2-citation MID density

Topic tags `claude-code` + `codex` = 2 corpus-subject overlaps (Claude Code v65 + Codex v62). Below v83's 16-harness CORPUS-RECORD; below v94's ~13-citation possible CORPUS-RECORD. Within typical 2-4-citation MID range for T2 service subjects.

### Pattern #29 absent-LICENSE strengthening with NEW sub-variant

| Wiki | Variant | License declaration |
|---|---|---|
| v79 autoresearch_folktales | README-declared-MIT-no-LICENSE-file | README: "MIT", LICENSE file: absent |
| v80 SmartMacroAI | NOASSERTION | GitHub API: NOASSERTION, 404 on /contents/LICENSE |
| **v97 distill** | **NULL + README-also-silent** | GitHub API: null, README: no license mention; full silence |

NEW sub-variant "README-completely-silent" PROVISIONAL N=1 distinct from v79's README-declared + v80's NOASSERTION-API-but-attempted-LICENSE-fetch. Pattern #29 cluster now at 3-variant taxonomy candidate.

### Pattern #82 quantitative-marketing strengthening

README claims at first 25 lines:
1. "Save up to **99%** of tokens"
2. "**98.7%** tokens saved" (worked example)
3. "**1.7B** parameters - **4bit**"
4. "**8 GB+ RAM**" (safe-floor)
5. "**16 GB+** is comfortable"

5 explicit quantitative claims at README header. Above-average quantitative-marketing density for T2 service subjects.

### Pattern #66 supply-chain awareness — WEAK absence-of-evidence

No supply-chain discipline section in README. No security review of bundled-model integrity (model checksums, signature verification not documented). 4 dev-spec HTML artifacts published but no supply-chain spec.

Note: with bundled-LLM-via-Hugging-Face, supply-chain risk includes model-tampering at Hugging Face mirror (Pattern #66 sub-mechanism candidate "Model-Registry-Tampering-at-Hugging-Face-as-Supply-Chain-Risk-Vector"). Not currently surfaced by subject = corpus-novel deficiency observation.

### Pattern #19 NEW sub-mechanism candidate "Brazilian-Solo-Dev-with-Own-Fine-Tuned-LM-and-Company-Association"

PROVISIONAL N=1 (Samuel Fajreldines profile). Distinct from Pattern #19 sub-mechanism layer's existing 8+ sub-mechanism candidates (most VN-LOCATED + Chinese-Mainland + Munich + SF + Taiwan-located clusters). Pattern #19 graveyard tracking at v100 audit — current candidate count ~7-8 PROVISIONAL N=1 layer pending CONSOLIDATION review.

Phase 0.9 §25 (a)-8 sub-axis registration is the higher-priority observation; Pattern #19 sub-mechanism is the lower-priority companion observation.

## Library-vocab PROVISIONAL N=1 registrations at v97

| # | Library-vocab | Distinguishing axis |
|---|---|---|
| 1 (PRIMARY) | Own-Trained Bundled Expert Language Model at Single-Subject Solo-Founder Scale | Vertical-integration at solo-founder scale |
| 2 | Spec-as-HTML-Published-at-Repo-Root | Dev-process-spec-as-published-artifact at root |
| 3 | Bun-for-build + npm-for-workspace Hybrid Tooling | Build-tool + publish-tool axis separation |
| 4 | 5-Platform-Binary-Distribution via NPM Workspace Postinstall-Pattern at Solo-Founder T2 Scale | Distribution-mechanism at solo-founder T2 service scale (esbuild-style pattern at smaller scale) |
| 5 | Compression-as-Trainable-Discipline at LLM-Output Layer ("Distill Language") | Methodology-vocabulary axis for fine-tuned-model-as-compression-trainer |
| 6 | Brazilian-Solo-Dev with Own-Fine-Tuned-LM (Pattern #19 sub-mechanism candidate) | Profile-type axis |

## Distill Language usage in vault sessions (operator pilot guidance)

### Recommended pipe shapes for vault grep

```bash
# Hunt for pattern definitions
rg -n "Pattern #84" "_patterns/" | distill "where is 84c sub-mechanism canonically defined"

# Audit state-block extracts
awk '/Pattern #57/{p=1} p && /^---$/{p=0} p' "_state/03c-projects-v61-v95.md" | distill "summarize Pattern #57 evolution v61-v95"

# Find candidate consolidations
rg -n "PROVISIONAL N=1" "_patterns/" | distill "which Pattern #19 sub-mechanisms have aged past v100 consolidation threshold"
```

### Pilot trial sequence (~5 min)

1. `npm i -g @samuelfaj/distill`
2. `distill` (auto-onboarding; downloads samuelfaj/distill-1.7B-MLX from Hugging Face; ~1GB)
3. Test pipe: `rg -n "Library-vocab" "_state/" | distill "list distinct Library-vocab items mentioned across state chapters"`
4. Compare token cost with-distill vs without (use `wc -c` on input vs output bytes)

### Reversibility

- Uninstall CLI: `npm uninstall -g @samuelfaj/distill`
- Remove cached model: `rm -rf ~/.cache/huggingface/hub/samuelfaj--distill-1.7B-MLX`
- Remove any installed Claude Code skill: `rm -rf ~/.claude/skills/distill` (or per-project equivalent if installed in `.claude/skills/`)

## Honest deficiency-disclosure (what subject does NOT have)

- **No LICENSE file** — operator pilot use is legally ambiguous (no copyright-grant statement). Pattern #29 strengthening. Operator should pilot at fenced-scope only until LICENSE clarified.
- **No documented supply-chain discipline** — bundled-model integrity not addressable from README alone.
- **No telemetry-policy statement** — README does not declare whether the local model phones home (likely it doesn't given MLX local-only architecture, but undocumented).
- **No N=2 evidence yet for own-trained-bundled-LM Library-vocab** — pilot grades the methodology-influence axis at single-subject scope.
- **Bun-vs-npm hybrid tooling not documented** — README does not explain why both tools are used or what the operator should install.
- **Sub-1.7B model means English-only inference quality at small-LM scale** — non-English vault content (Vietnamese strings in operator's vault) may compress with reduced fidelity.

## Operator-applicability summary

**HIGH-RELEVANCE Tier-1 actionable pilot candidate position #3** (between anthropics/skills v93 #2 and claude-comstyle v87 #4). Direct vault-process utility at CLI-piping token-compression layer + LOW cost-of-trial + reversible. Addresses documented context-thrashing problem at session-pipe boundary observed throughout v60+ corpus.

**Recommended pilot sequence**: install + onboarding + 3 pipe-shape trials + token-cost-comparison measurement. ~15 min total. Reversible at every step.

**Not a methodology-influence Tier-1-special** (no foundational-vendor status; no source-authoritative reference-implementation; subject does not redefine corpus methodology-direction).
