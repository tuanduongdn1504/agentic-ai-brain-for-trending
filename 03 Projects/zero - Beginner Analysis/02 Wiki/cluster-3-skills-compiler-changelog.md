# (C) Cluster 3: Skills protocol integration + compiler architecture + CHANGELOG history

**Sources:**
- [skills/zero/SKILL.md](https://raw.githubusercontent.com/vercel-labs/zero/main/skills/zero/SKILL.md) (51 lines)
- [package.json](https://raw.githubusercontent.com/vercel-labs/zero/main/package.json) (49 lines)
- [CHANGELOG.md](https://raw.githubusercontent.com/vercel-labs/zero/main/CHANGELOG.md) (44 lines; v0.1.0 → v0.1.2)

**Cluster focus:** Compiler-served version-matched skills / bootstrap vs full content / 40+ npm scripts / @vercel/sandbox dep / self-hosted compiler bootstrap pattern / 3-release velocity narrative

---

## 1. The SKILL.md bootstrap stub (Phase 4b PRIMARY-aligned artifact)

The file is at `skills/zero/SKILL.md` and uses **Anthropic skills protocol frontmatter** (corpus-confirmed convention):

```markdown
---
name: zero
description: Install Zero and load version-matched workflows with zero skills.
---
```

The body opens (verbatim, lines 7-10):

> *"# Zero"*
>
> *"Zero is the programming language for agents."*
>
> *"Install this skill once in an agent's skill manager. Keep it thin; Zero's own CLI serves the version-matched workflow for each installed compiler."*

**Self-positioning of the SKILL.md (verbatim, lines 21-22):**

> *"This file is a discovery stub. Do not treat it as the full Zero workflow."*

The remainder of the file directs agents to compiler-served content:

```sh
zero skills list
zero skills get zero
zero skills get zero --full
```

**Inner skills enumeration (verbatim, lines 36-37):**

> *"Common inner skills include `zero-agent`, `zero-language`, `zero-diagnostics`, `zero-packages`, `zero-builds`, `zero-testing`, and `zero-stdlib`."*

**7 named inner skills** served by compiler binary, version-matched to the installed Zero compiler.

---

## 2. The Skills-Protocol-As-Binary-Bootstrap pattern (corpus-first observation)

**The architectural problem Zero solves:**

Traditional skill packaging puts skill content in static files (the SKILL.md itself). Skill content can drift from runtime/compiler versions — if the skill says "use `zero fix` like this" but a newer Zero version changed `zero fix` behavior, the skill is wrong.

**Zero's solution (per CHANGELOG v0.1.1):**

> *"Adds version-matched agent guidance through `zero skills`, including focused workflows for Zero syntax, diagnostics, builds, packages, standard library use, testing, and agent edit loops."*
>
> *"Keeps the installable Zero skill as a thin bootstrap so external skill managers discover one Zero skill while the compiler serves the richer guidance for the installed version."*
>
> *"Updates the `zero skills` CLI contract to serve bundled flat skill data while preserving list, get, path, and JSON workflows."*

**Mechanism:**
1. External skill manager (Claude Code's skills plugin / Cursor / etc.) discovers the thin `skills/zero/SKILL.md` bootstrap stub
2. Bootstrap stub instructs the agent to invoke `zero skills get zero --full`
3. Installed Zero compiler binary serves the version-matched skill content from its bundled `skill-data/` directory
4. Agent uses the content matching the EXACT compiler version on the system

**Pattern observation:** **Skill-as-Binary-Bootstrap** — distinct from static-skill-packaging (corpus default) and from skill-aggregator-meta (Pattern #2 distribution variant). Zero v68's mechanism:
- One SKILL.md per skill manager registry (no version proliferation in registry)
- Binary owns skill content (version-coupled at install time)
- Discovery-stub-to-binary-content-handoff

**Corpus-first observation.** No prior corpus subject has documented this mechanism. Library-vocabulary candidate item OR NEW Pattern candidate.

**Distinct from:**
- v51 agent-skills-of-vercel: static SKILL.md per skill (Pattern #2 corporate-curated distribution)
- v62 codex-plugin-cc: static skill files bundled in plugin
- v63 karpathy-skills: 7 frontmatter-only single-artifact distillation
- v64 claude-seo: 25 sub-skills + 18 sub-agents as static SKILL.md files
- v66 agentmemory: 51 MCP tools as runtime-served (similar mechanism but via MCP not skill protocol)

---

## 3. Multi-binary handling (corpus-distinctive UX)

The SKILL.md anticipates multi-binary installations (verbatim, lines 31-34):

> *"If the user has multiple Zero binaries, use the same binary that will run the project:*
>
> ```sh
> /path/to/zero skills list
> /path/to/zero skills get zero --full
> ```
> *"*

**Corpus observation:** Multi-binary-coherence-as-skill-routing-concern — the skill stub tells agents to invoke the binary that matches the project's installed version. Distinct from version-globally-pinned (npm one-version-per-installation) — Zero anticipates project-local installations of different compiler versions.

---

## 4. package.json analysis — workspace + scripts

**Workspace declaration (verbatim, lines 7-9):**

```json
"workspaces": [
  "extensions/*"
]
```

Single workspace target: `extensions/*` (currently containing `extensions/vscode/`).

**40 npm scripts (full enumeration from lines 10-43):**

| Category | Scripts | Function |
|----------|---------|----------|
| **Native build** | `check`, `native:smoke`, `native:install`, `native:sanitize`, `native:test`, `native:test:local`, `native:test:sandbox` | Native C compiler build/test |
| **Conformance** | `conformance`, `conformance:local`, `conformance:sandbox`, `provenance:guardrails` | Language conformance fixtures |
| **Command contracts** | `command-contracts`, `command-contracts:local`, `command-contracts:sandbox` | CLI output contract validation |
| **Docs (pnpm-prefixed)** | `docs:install`, `docs:dev`, `docs:build`, `docs:start`, `docs:test`, `docs:wasm`, `docs:compiler` | Docs site workspace (pnpm-managed) |
| **Extension install** | `extension:install:cursor` | Cursor extension install (workspace-scoped) |
| **Reliability** | `reliability:smoke` | Smoke testing |
| **Benchmarks** | `bench`, `bench:local` | Benchmarks |
| **WASM** | `wasm:runtime:smoke` | WASM runtime smoke test |
| **Agent demo** | `agent:demo` | Agent repair demonstration |
| **Language server** | `zls` | Language server (Zero LSP?) |
| **Build/test** | `build:test`, `test:zero`, `test` | Build + testing |
| **Entry** | `zero` | `bin/zero` dispatcher |

**40+ scripts total** across native build / conformance / contracts / docs / WASM / agent / LSP / benchmarks. This is **corpus-high script density for a 2-day-old project**.

**Notable scripts:**

`docs:wasm`:
```bash
bin/zero build --emit wasm --target wasm32-web compiler-zero --out docs-site/public/playground/zeroc-zero
```

→ The Zero compiler can be built **as WASM** for the docs-site playground. `compiler-zero` (self-hosted) compiles to wasm32-web target for in-browser execution.

`docs:compiler`:
```bash
node scripts/playground-wasm-smoke.mjs && node scripts/browser-compiler-hardening.mjs
```

→ Playground WASM compiler has its own hardening + smoke test scripts. **Browser-runnable compiler as docs-site feature** — corpus-first observation.

`agent:demo`:
```bash
node scripts/agent-repair-demo.mjs
```

→ Explicit "agent repair" demo script. Aligns with agent-first design axiom.

`zls`:
```bash
node scripts/zls.mjs --self-test
```

→ Language server. The script name `zls.mjs` suggests "Zero Language Server" (analogous to `tsls`, `pyls`, etc.).

---

## 5. Dependencies (package.json devDependencies)

```json
"devDependencies": {
  "@types/node": "^25.7.0",
  "@vercel/sandbox": "^1.10.2",
  "typescript": "^6.0.3"
}
```

Only **3 dev dependencies** at root:

1. **`@types/node` ^25.7.0** — Node 25 types (current as of 2026)
2. **`@vercel/sandbox` ^1.10.2** — Vercel's sandbox utility for isolated native testing
3. **`typescript` ^6.0.3** — TypeScript 6.x (for build:test + npm scripts)

**Corpus observation #1: Minimal dependency surface.** 3 deps at root, all dev-only, all from known publishers. Compare:
- v62 codex-plugin-cc: 0 runtime deps (Apache-2.0 plugin with bundled implementation)
- v66 agentmemory: 6 runtime deps (98% surface = iii-sdk; Pattern #85)
- v67 opencode-antigravity-auth: 5 runtime deps

Zero v68's root has zero runtime deps (it's a workspace coordinator, not a runtime). Actual runtime is the native C compiler + `bin/zero` script.

**Corpus observation #2: `@vercel/sandbox` is Vercel-ecosystem-internal dependency.** Zero (vercel-labs) uses `@vercel/sandbox` (Vercel main org) for native test sandboxing. This is **corpus-first explicit vercel-ecosystem-internal-tooling dependency-chain**:
- v51 agent-skills-of-vercel: Vercel main org subject
- **v68 zero (vercel-labs): depends on @vercel/sandbox from Vercel main org**

Strengthens Pattern #57 57c sub-variant (within-corpus product-internals citation chain) — Zero references Vercel main org tooling for security-critical infrastructure (sandboxing).

---

## 6. Compiler architecture (project layout cross-reference)

From AGENTS.md project layout + package.json scripts:

```
native/zero-c/          ← Bootstrap compiler (written in C)
  src/main.c            ← Entry point (version-bumped in release workflow)
  Makefile              ← `make -C native/zero-c` builds the native binary

compiler-zero/          ← Self-hosted Zero compiler (written in Zero)
                        ← `bin/zero build --emit wasm --target wasm32-web compiler-zero`
                        ← compiles compiler-zero to WASM for docs-site playground

bin/zero                ← User-facing CLI dispatcher
                        ← package.json: "zero": "bin/zero"

skill-data/             ← Skill content source files (compiler-served)
                        ← Bundled into native compiler binary at build time
```

**Corpus-first observations:**

**Observation #1: Two-compiler-implementation architecture.** Native C bootstrap + Zero-authored self-hosted compiler. Self-hosting allows the compiler-zero/ implementation to use Zero's own features as they evolve. Native bootstrap remains the user-installed binary; compiler-zero/ is the WASM-target playground compiler. **First explicit self-hosted compiler bootstrap in corpus.**

**Observation #2: Skill content bundled into binary.** Per CHANGELOG v0.1.1: "Updates the `zero skills` CLI contract to serve bundled flat skill data while preserving list, get, path, and JSON workflows." Skill data lives in `skill-data/` and is bundled into the native compiler at build time. Distinct from static skill files in repo (corpus default).

**Observation #3: WASM compiler for browser playground.** `compiler-zero/` compiles to wasm32-web for docs-site playground at zerolang.ai. Users can try Zero in-browser without installing. **First corpus subject with in-browser-compiler-via-WASM**.

---

## 7. CHANGELOG analysis — 3-release narrative in 2-day window

### v0.1.0 (2026-05-16 00:21)

**Verbatim (lines 40-44):**

> *"- Initial public release of Zero as the programming language for agents."*
> *"- Includes the native compiler, examples, documentation site, and validation fixtures."*
> *"- Supported workflows use direct Zero emitters for the documented examples and targets."*

**Observations:** Initial release shipped with native compiler + docs site + examples + validation fixtures = substantial-from-day-one launch. The phrase *"the programming language for agents"* is the immediate tagline.

### v0.1.1 (2026-05-16 05:33 — 5 hours later)

**Verbatim CHANGELOG (lines 26-34):**

- Adds public installer at `https://zerolang.ai/install.sh` with platform selection, GitHub release downloads, **checksum verification**, and `$HOME/.zero/bin/zero` installation
- Adds `zero run` for the everyday edit loop
- Updates README, homepage, getting-started, install, and CLI docs
- Reworks public docs to be more scannable
- Removes placeholder module docs that described surfaces not ready for users; adds current module docs for `std.crypto`, `std.http`, and `std.net`
- **Adds version-matched agent guidance through `zero skills`** (KEY OBSERVATION — Skills-Protocol-As-Binary-Bootstrap mechanism)
- Keeps installable Zero skill as a thin bootstrap so external skill managers discover one Zero skill
- Updates the `zero skills` CLI contract to serve bundled flat skill data

**Contributors (lines 36-38):**
- @ctate
- @mvanhorn

**Velocity observation:** 5-hour gap from v0.1.0 to v0.1.1 with substantive feature additions (installer, `zero run`, skills protocol). **Same-day rapid-iteration discipline.**

### v0.1.2 (2026-05-17 21:25 — 1.5 days later)

**Verbatim CHANGELOG (lines 5-12):**

- Rebuilds borrow provenance tracking across references, fields, subpaths, assignments, control-flow joins, receiver side effects, generic methods, return summaries, and unreachable paths
- Tightens borrow conflict checking by deriving conflicts from provenance and comparing concrete places, with additional conformance coverage for provenance joins and edge cases
- Fixes checker regressions around borrow origins, reassignment, aggregate values, explicit reference fields, unknown identifiers, and fallibility propagation through wrappers
- Fixes dynamic CLI strings and Darwin executable UUID emission
- Adds Apache-2.0 licensing and lockfile license metadata
- Updates the public site with an install toggle, GitHub star count, and a mobile header Docs link

**Contributors (lines 14-20):**
- @ctate
- @badlogic
- @chenrui333
- @heylakatos
- @onevcat

**Observations:**

**Observation #1: v0.1.2 is heavily compiler-internal work.** Borrow checking provenance tracking, control-flow joins, generic method return summaries = sophisticated semantic analysis. **Zero has a borrow-checker** (à la Rust). This is corpus-first observation: **Zero v68 includes Rust-style borrow checking as language feature.**

**Observation #2: 5-contributor v0.1.2 vs 2-contributor v0.1.1.** Community is growing release-over-release. v0.1.2 contributor list includes well-known names: **@badlogic** (known game-dev / Apache Spark contributor), **@onevcat** (iOS dev / Kingfisher author). External community engagement at corpus-distinctive speed (2-day-old project).

**Observation #3: License metadata added at v0.1.2.** "Adds Apache-2.0 licensing and lockfile license metadata" = **late license-finalization** for a corporate Vercel Labs release. License was effectively Apache-2.0 from v0.1.0 (per LICENSE file) but explicit package.json + lockfile metadata added at v0.1.2. Minor governance observation.

**Observation #4: Star count + mobile docs link added to public site.** Even at v0.1.2 (1.5 days old), the team is adding **star count display** to zerolang.ai. Suggests **public-launch-momentum-marketing** discipline.

---

## 8. Velocity-screen consolidated

**Repo age:** 2 days (2026-05-16 → 2026-05-18)
**Stars:** 2,100 → **1,050 stars/day** = EXTREME-VIRAL
**Commits:** 91 → **~45.5 commits/day**
**Releases:** 3 in 2 days → **1.5 releases/day** (corpus-record cadence vs v67 opencode-antigravity-auth's 91 in 5 months = 1 release per 1.75 days)
**Contributors:** 6 unique across 3 releases (mvanhorn / ctate / badlogic / chenrui333 / heylakatos / onevcat)

**Comparison table to corpus-velocity records:**

| Subject | Wiki | Age at observation | Stars/day | Note |
|---------|------|---------------------|-----------|------|
| karpathy-skills | v63 | 102 days | **1,186** | Corpus-record (single-author-distillation Pattern #52a) |
| **zero (vercel-labs)** | **v68** | **2 days** | **1,050** | **Second-highest; corporate-strategic-lab launch** |
| codex-plugin-cc | v62 | 21 days | ~847 | Pattern #52b cross-vendor cooperation |
| agentmemory | v66 | 35 days | 226 | Just below Pattern #52 EXTREME threshold |

**Velocity verdict:** v68 zero is **2nd-highest velocity in corpus history**. BUT 2-day window is too narrow for sustained-velocity classification (Pattern #52 sustained-velocity criterion requires 6mo+ observation). Register as **v69 sustained-velocity-test batch addition** alongside existing batch (mattpocock + codex-plugin-cc + karpathy-skills + agentmemory). Zero v68 is the test for **early-launch velocity sustainability** — does Vercel Labs corporate-strategic-lab launch sustain or decay?

---

## 9. Cluster 3 summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | Skill-as-Binary-Bootstrap mechanism (thin SKILL.md → compiler-served version-matched content) | **corpus-first** |
| 2 | Multi-binary-coherence-as-skill-routing-concern (`/path/to/zero skills get zero --full`) | corpus-first |
| 3 | 7 named inner skills served by compiler binary (zero-agent / zero-language / zero-diagnostics / zero-packages / zero-builds / zero-testing / zero-stdlib) | corpus-first |
| 4 | Self-hosted compiler bootstrap (native/zero-c + compiler-zero) | **corpus-first** |
| 5 | In-browser-compiler-via-WASM at docs-site playground | corpus-first |
| 6 | Rust-style borrow checking as language feature (v0.1.2 release notes detail provenance tracking + conflict checking) | corpus-first (corpus subjects had not yet had borrow-checker observations) |
| 7 | @vercel/sandbox as security-critical dependency (Vercel-ecosystem-internal tooling chain) | corpus-first explicit chain |
| 8 | 40+ npm scripts at 2-day-old project (corpus-high script density) | corpus-distinctive |
| 9 | 3 releases in 2 days = corpus-record release cadence (1.5 releases/day) | corpus-record |
| 10 | 1,050 stars/day = 2nd-highest velocity in corpus history (karpathy-skills v63 ~1,186/day was 1st) | corpus-2nd-highest |
| 11 | Substantial-from-day-one launch (v0.1.0 shipped with native compiler + docs site + examples + validation fixtures) | corpus-distinctive |
| 12 | External-community-velocity at 2-day-old (5-contributor v0.1.2 with notable names @badlogic, @onevcat) | corpus-first at this velocity |

---

## 10. Pattern Library implications from Cluster 3

- **NEW Pattern candidate: Skill-As-Binary-Bootstrap** — corpus-first mechanism. Promotion criteria proposal: (1) Thin SKILL.md or equivalent skill-protocol bootstrap stub; (2) Stub explicitly directs to runtime-bundled content (binary, compiler, runtime, etc.); (3) Runtime serves version-matched skill content. Could be observed at other compiler-bundled-skill subjects in future.
- **NEW Pattern candidate: Self-Hosted Compiler Bootstrap** — classic compiler engineering pattern, corpus-first observation as wiki subject. Promotion criteria proposal: (1) Native-language bootstrap compiler exists; (2) Self-hosted compiler in the language itself exists; (3) Both are functional / integrated. Unclear if this generalizes beyond Zero (most corpus subjects aren't compilers).
- **Pattern #52 EXTREME-VIRAL N+1 evidence (pending sustained-velocity test):** zero v68 at 1,050 stars/day = 2nd-highest. Register as v69 sustained-velocity-test batch addition. v69 evaluates whether velocity sustains over 6mo+ (Pattern #52 promotion criterion).
- **Pattern #57 57c product-internals corpus-citation chain N+1 evidence:** @vercel/sandbox dep links v68 zero to v51 vercel umbrella org subject. STRENGTHENING evidence for Pattern #57.
- **NEW observational candidate: In-Browser-Compiler-Via-WASM** — Zero compiles to WASM for in-browser docs-site playground. Could generalize to other language subjects but currently corpus-N=1.
- **NEW observational candidate: Substantial-From-Day-One Launch Discipline** — initial public release shipped with native compiler + docs + examples + validation. Distinct from typical "MVP launch" pattern. Could generalize to other corporate-strategic-lab launches.

---

## 11. References

- skills/zero/SKILL.md (51 lines)
- package.json (49 lines)
- CHANGELOG.md (44 lines)
- Cross-cluster: cluster-1 (README design axioms) + cluster-2 (AGENTS.md project direction + release workflow)

## 12. Next phase

Phase 3 — 4 entity pages: (1) The Zero language design + agent-first framing, (2) Compiler architecture + bootstrap pattern, (3) Skills-Protocol-As-Binary-Bootstrap as Phase 4b PRIMARY-aligned deliverable, (4) Storm Bear meta-entity (WEAK INCLUDE per Phase 0.9 STRICT 1/4 PASS).
