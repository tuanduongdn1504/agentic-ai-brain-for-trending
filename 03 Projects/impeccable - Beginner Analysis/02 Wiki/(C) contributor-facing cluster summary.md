# (C) Cluster: Contributor-facing — technical architecture + governance + distribution

## In one sentence

Impeccable is a single deployable design-skill replicated across **14 harness-specific directories** (CORPUS-RECORD multi-target distribution) with a 9-file governance discipline (README + CLAUDE + AGENTS + DESIGN + DEVELOP + HARNESSES + PRODUCT + STYLE + NOTICE), Apache-2.0 + NOTICE.md derivative-attribution chain, and a TDD-enforced anti-pattern detection pipeline.

## Repository topology

```
pbakaus/impeccable/
├── README.md                  (entry-point + install instructions)
├── CLAUDE.md                  (Claude-specific routing — auxiliary)
├── AGENTS.md                  (Repository Guidelines: code style + build + testing)
├── DESIGN.md                  (7 design domains + 27 anti-patterns)
├── DEVELOP.md                 (build system + skill architecture v3.0+)
├── HARNESSES.md               (11-harness spec-compliance matrix)
├── PRODUCT.md                 (vision + target user + restraint philosophy)
├── STYLE.md                   (editorial voice + denylist + read-aloud test)
├── NOTICE.md                  (Apache-2.0 derivative-attribution chain)
│
├── skill/                     ← canonical skill source
│   ├── SKILL.md
│   ├── agents/                (sub-agent definitions)
│   ├── reference/             (35 markdown files: 7 reference domains + 28 command-like files)
│   └── scripts/               (build + load-context.mjs)
│
├── .claude/skills/impeccable/         ← Claude Code deployable
├── .claude-plugin/                    ← Claude plugin format
├── .cursor/skills/impeccable/         ← Cursor deployable
├── .codex/agents/                     ← Codex CLI TOML-based
├── .gemini/skills/impeccable/         ← Gemini CLI deployable
├── .opencode/skills/impeccable/       ← OpenCode deployable
├── .agents/skills/impeccable/         ← Generic agents/ convention
├── .kiro/skills/impeccable/           ← Kiro
├── .pi/skills/impeccable/             ← Pi
├── .qoder/skills/impeccable/          ← Qoder
├── .rovodev/skills/impeccable/        ← Rovo Dev (Atlassian)
├── .trae/skills/impeccable/           ← Trae
├── .trae-cn/skills/impeccable/        ← Trae Chinese variant
├── .impeccable/                       ← own metadata
│
├── cli/                       (npx impeccable detect CLI)
├── extension/                 (browser extension package)
├── plugin/                    (plugin package)
├── functions/api/download/    (Cloudflare worker for bundle downloads)
├── site/                      (Astro homepage at impeccable.style)
├── demos/landing-demo/        (showcase demo)
├── notes/                     (working notes)
├── scripts/                   (orchestration scripts)
├── tools/                     (build tooling)
└── tests/                     (Bun + node:test TDD harness)
```

## Multi-harness distribution model — CORPUS-RECORD

**14 harness directories** is corpus-first by a wide margin. Prior corpus records:

| Wiki | Subject | Provider/Harness count |
|------|---------|------------------------|
| v71 | agents-best-practices | 2 (Anthropic + OpenAI synthesis) |
| v72 | DeepSeek-TUI | 9 (provider matrix) |
| v73 | cc-switch | 12 (provider matrix CORPUS-RECORD at v73) |
| **v75** | **impeccable** | **14 (harness-target matrix NEW CORPUS-RECORD)** |

The shape differs from prior records. Earlier corpus records measured **provider/API portability** (one client supporting N upstream APIs). Impeccable measures **harness-installation-target portability** (one skill replicated into N harness-specific directories). Same underlying axis — cross-vendor distribution — measured one layer down: at the skill-installation-pathway level rather than the runtime-API level.

HARNESSES.md is itself a NEW corpus artifact: a comparative spec-compliance document for an agentic-skill ecosystem. The 11-harness compliance matrix it documents shows uneven maturity (Claude Code = most comprehensive / Trae = "no official skills docs found yet" / Gemini CLI validates only `name`+`description` ignoring other fields), which is unusual evidence: a single skill author is doing the cross-harness-spec interoperability research that the harness vendors haven't standardized.

## Governance file count = 9 (extensive)

Prior corpus governance file counts:
- Routine v2.2 classification axis: 0-2 light / 3-4 medium / 5-6 heavy / 7+ extensive
- Impeccable = 9 files = corpus-second-extensive (v65 claude-code-system-prompts had highest count at ~12; v75 impeccable = 9 sits in upper band)

Each file has a focused single concern: README (entry) / CLAUDE (routing) / AGENTS (contributor rules) / DESIGN (the design system) / DEVELOP (build) / HARNESSES (distribution matrix) / PRODUCT (vision) / STYLE (editorial) / NOTICE (license attribution). No file overlap.

## Build system + testing

- Bun runtime + bun.lock + pnpm-lock.yaml (dual lockfile = both Bun and pnpm packaging targets)
- `bun run dev` / `bun run build` / `bun run test` / `bun run test:live-e2e`
- Test files `*.test.js` or `*.test.mjs` via `bun --test` or `node --test`
- TDD order for anti-pattern detection: fixture → failing test → rule implementation → adapter wiring (browser + jsdom)
- Cloudflare Worker for bundle downloads at `/functions/api/download/`
- Astro for site framework + biome.json for formatting + wrangler.toml for Cloudflare deploy

## License + attribution chain

**Apache 2.0** + dedicated `NOTICE.md` documenting a 2-source derivative-attribution chain:

1. **Anthropic frontend-design skill** (Apache 2.0, Copyright 2025 Anthropic, PBC) — parent skill that impeccable extends; located at `github.com/anthropics/skills/tree/main/skills/frontend-design`. Extensions: 7 domain-specific reference files (typography / color-and-contrast / spatial-design / motion-design / interaction-design / responsive-design / ux-writing) + 23 commands + expanded pattern documentation.

2. **ehmo/typecraft-guide-skill** (Apache 2.0) — incorporated tactical additions in the typography reference: dark-mode compensation / font-display strategies / variable font guidance / responsive measure coupling / text-wrapping techniques / optical sizing / paragraph rhythm conventions. Located at `github.com/ehmo/typecraft-guide-skill`.

**Pattern Library implication:** corpus-first 2-source NOTICE.md derivative chain (single Apache-2.0 derivative crediting BOTH a parent skill AND a third-party tactical-additions source). Distinct from Pattern #45 sub-typologies 45a-45d (which addressed tier-based / wrapper-based / artifact-scope-split / book-content-exclusion) — this is **license-attribution-as-multi-source-derivative-chain**.

## skills-lock.json (minimal)

```json
{
  "version": 1,
  "skills": {}
}
```

Empty schema-establishing template — Pattern #66 supply-chain-manifest-pattern observed at sub-mechanism candidate level. Mechanism is in-place but not yet pinning anything. v76+ stale-check.

## Editorial discipline as build-gate

STYLE.md's denylist isn't documentation — it's **validator-enforced**. The build runs a denylist check against generated copy. Words like `seamless` / `robust` / `elevate` / `empower` / `delve` / em-dashes fail the build. This is corpus-first **editorial-discipline-as-build-validator** (Pattern #28 sister observation — anti-bloat-via-build-validator distinct from v73 cc-switch's anti-bloat-via-documented-refusal).

## Commit / release discipline

Commits use imperative subjects (`Fix: ...`, `Add ...`). Releases are component-specific with distinct version tags. Skill releases (e.g., `Skill 3.1.1` 2026-05-14) versioned separately from CLI / extension / plugin packages. Per-component versioning under one repo = Pattern #66 supply-chain integrity layer (clear release-boundary discipline).

## What's missing / what to watch

- `skills-lock.json` is empty — populated yet?
- `.trae-cn/` is the only i18n branch — Chinese variant of Trae, no other locales yet
- Designer rationale of OKLCH-only choice — referenced in DESIGN.md but no extended treatise yet (DEVELOP.md and DESIGN.md split the technical/aesthetic discussion across files)
- No MCP server — skill-only artifact, not protocol-server pattern
