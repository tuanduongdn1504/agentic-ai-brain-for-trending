# (C) Entity 2: Compiler architecture + bootstrap pattern

**Type:** Distribution/ecosystem entity
**Slot:** Entity 2 of 4
**Sibling entities:** [Entity 1 — The Zero language](entity-1-zero-language-and-agent-first-design.md) / [Entity 3 — Skills-Protocol-As-Binary-Bootstrap](entity-3-skills-protocol-as-binary-bootstrap.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. Two compiler implementations (self-hosted bootstrap)

Zero ships **two distinct compiler implementations**:

```
native/zero-c/          ← Native C bootstrap compiler (currently the user-installed binary)
  src/main.c            ← Entry point — version is bumped at release time per AGENTS.md
  Makefile              ← `make -C native/zero-c` builds the native binary

compiler-zero/          ← Self-hosted Zero-authored compiler (Zero compiling Zero)
                        ← `bin/zero build --emit wasm --target wasm32-web compiler-zero`
                        ← Compiles to WASM for the docs-site browser playground
```

**Why two compilers?** This is the **classic bootstrapped-compiler pattern**:

1. **Write the language in another language first** — Zero's bootstrap compiler is written in C (`native/zero-c/src/main.c` is the entry point)
2. **Use the bootstrap compiler to compile the self-hosted compiler** — `compiler-zero/` is the Zero source for a Zero compiler
3. **Eventually retire the bootstrap when self-hosting is complete** (aspirational; current state appears to retain both)

**Corpus-first observation:** This is the **FIRST corpus subject with self-hosted compiler bootstrap architecture**. No prior corpus subject documented a language compiler (let alone a self-hosted one).

**Specific evidence of self-hosting in motion:** package.json `docs:wasm` script:

```bash
bin/zero build --emit wasm --target wasm32-web compiler-zero --out docs-site/public/playground/zeroc-zero
```

This script uses `bin/zero` (which dispatches to the native C compiler binary) to BUILD `compiler-zero/` (the Zero-authored compiler) as WASM. The output (`zeroc-zero`) is the in-browser playground compiler.

→ **The native compiler can compile the self-hosted compiler.** This is the bootstrap chain.

---

## 2. The `bin/zero` CLI dispatcher

`bin/zero` is the user-facing CLI script (per package.json: `"zero": "bin/zero"`). It dispatches user commands to:

- Native compiler binary (built from `native/zero-c/`)
- Compiler-zero WASM (for in-browser playground)
- JavaScript scripts (e.g., `scripts/zls.mjs` for language server)
- Skill content (bundled `skill-data/` served via `zero skills`)

**Common commands routed through `bin/zero`:**

```bash
zero check examples/hello.0       # → native binary
zero run examples/add.0           # → native binary (build + execute)
zero build --emit exe ...         # → native binary
zero graph --json ...             # → native binary
zero size --json ...              # → native binary
zero routes --json ...            # → native binary
zero fix --plan --json ...        # → native binary
zero explain <diagnostic-code>    # → native binary
zero doctor --json                # → native binary
zero skills list                  # → native binary (serves from skill-data/)
zero skills get zero --full       # → native binary
zero --version --json             # → native binary (used in CI verification)
```

**Corpus observation:** All user-facing commands route through `bin/zero`. The dispatcher pattern centralizes Zero's CLI surface — distinct from polyglot CLIs that expose multiple binaries.

---

## 3. Native build chain (Make + C)

Bootstrap chain (per AGENTS.md development section):

```bash
make -C native/zero-c
```

Builds the native C compiler. Output binary is placed in `$HOME/.zero/bin/zero` for users (per install script) or `bin/zero` symlink for development.

**Package.json scripts:**

```bash
npm run native:install        # `make -C native/zero-c install-local`
npm run native:smoke          # smoke test
npm run native:sanitize       # `bash scripts/sanitizer-smoke.sh` (memory sanitizers?)
npm run native:test           # sandboxed test
npm run native:test:local     # direct test (env-guarded)
npm run native:test:sandbox   # sandboxed test (default)
```

**Corpus observation:** Native tests default to **sandboxed execution** via `@vercel/sandbox` (per `scripts/native-test-sandbox.mjs`). The `local` variants require `ZERO_NATIVE_TEST_ALLOW_LOCAL=1` env guard. **Sandbox-by-default for native test execution** = defensive engineering choice — runs untrusted compiler-output code in isolated environments.

---

## 4. Conformance + command-contracts validation layers

Per package.json scripts:

```bash
npm run conformance              # `node conformance/run.mjs`
npm run conformance:local        # direct
npm run conformance:sandbox      # sandboxed (default)
npm run provenance:guardrails    # `node scripts/provenance-guardrails.mjs`

npm run command-contracts        # CLI output contract validation
npm run command-contracts:local  # direct
npm run command-contracts:sandbox # sandboxed (default)
```

**Corpus observation:**

**Conformance** = language + CLI fixture conformance. Tests that the compiler implements the documented language correctly.

**Command-contracts** = validates CLI command outputs match documented contracts. Particularly relevant because Zero's CLI emits JSON that agents depend on — output drift would break agent consumers.

**Provenance guardrails** = (per CHANGELOG v0.1.2) borrow provenance tracking validation. Specific to the compiler's borrow-checker semantics.

→ **Four-layer validation:** native:test + conformance + command-contracts + provenance:guardrails. **Corpus-distinctive multi-layer validation for a 2-day-old project.**

---

## 5. WASM compilation + in-browser playground

The `compiler-zero/` (Zero-authored compiler) can be compiled to WASM (`wasm32-web` target):

```bash
bin/zero build --emit wasm --target wasm32-web compiler-zero --out docs-site/public/playground/zeroc-zero
```

This produces `zeroc-zero` WASM binary deployed to docs-site at `docs-site/public/playground/`. Users can run Zero in-browser at zerolang.ai without installing.

**Browser-compiler hardening (per `docs:compiler` script):**

```bash
node scripts/playground-wasm-smoke.mjs && node scripts/browser-compiler-hardening.mjs
```

Both smoke-tests + hardening checks for the WASM playground compiler.

**Corpus-first observation:** **In-browser-compiler-via-WASM at docs-site playground** — no prior corpus subject had documented WASM-compiled compilers for browser playgrounds. Distinct from typical "language playground" services (most use server-side execution); Zero compiles the compiler itself to WASM for client-side execution.

---

## 6. Distribution mechanism

**Install path (verbatim from README):**

```bash
curl -fsSL https://zerolang.ai/install.sh | bash
export PATH="$HOME/.zero/bin:$PATH"
zero --version
```

**Per CHANGELOG v0.1.1:**

> *"Adds the public installer at `https://zerolang.ai/install.sh`, with platform selection, GitHub release downloads, checksum verification, and `$HOME/.zero/bin/zero` installation."*

**Install pipeline:**
1. `curl` fetches `install.sh` from `zerolang.ai` (Vercel-hosted Vercel-Labs domain)
2. Script detects platform (Linux / Darwin / etc.)
3. Downloads platform-specific binary from GitHub Releases
4. Verifies checksum against known-good values
5. Installs to `$HOME/.zero/bin/zero`

**Corpus observation:** The **checksum verification step** is corpus-distinctive — most `curl | bash` installers in the corpus skip integrity verification. Zero strengthens Pattern #66 meta-supply-chain-awareness via explicit checksum step.

**Build targets supported (per common-commands README):**
- `exe` (host platform)
- `linux-musl-x64` (static-musl Linux)
- `wasm32-web` (WASM for browser)

Likely additional targets (Darwin, Linux glibc, Windows) but not enumerated in README. CHANGELOG v0.1.2 mentions "Darwin executable UUID emission" fix → Darwin target exists.

---

## 7. Editor integrations

Per project layout + package.json workspaces:

```
extensions/vscode/        ← VS Code extension (workspace member)
```

The single workspace target is `extensions/*`. Currently only VS Code. Per package.json scripts:

```bash
npm run extension:install:cursor    # `npm run install:cursor -w zero-lang`
```

Suggests Cursor integration also exists (through workspace package `zero-lang`). The workspace name `zero-lang` matches the `name` field in package.json: `"name": "zero-lang-workspace"`.

**Corpus observation:** Multi-editor integration (VS Code + Cursor) at 2-day-old project. Editor extensions are part of the v0.1.x release process per AGENTS.md release workflow §"Bump the release version in `extensions/vscode/package.json`."

---

## 8. Language server (`zls.mjs`)

Per package.json:

```json
"zls": "node scripts/zls.mjs"
```

And the full test command includes `--self-test`:

```bash
npm run zls -- --self-test
```

**Corpus observation:** Zero has a **JavaScript-implemented language server** (LSP). Named `zls` analogous to `tsls` (TypeScript), `pyls` (Python). Distinct from the native compiler (`bin/zero`) — LSP runs as JavaScript script.

Suggests Zero's LSP is implemented in JS while the compiler is in C. This is a corpus-distinctive split — most languages have LSP in the same language as the compiler.

---

## 9. Test surface (corpus-distinctive comprehensiveness for a 2-day-old project)

The full `npm test` script (verbatim from package.json):

```bash
npm run conformance &&
npm run native:test &&
npm run wasm:runtime:smoke &&
npm run test:zero &&
npm run docs:test &&
npm run zls -- --self-test &&
npm run agent:demo &&
npm run test -w zero-lang
```

**8 test layers** chained:
1. **Conformance** — language + CLI fixture conformance
2. **Native test** — native compiler tests (sandboxed)
3. **WASM runtime smoke** — WASM target smoke
4. **test:zero** — Zero-authored test files (`make -C native/zero-c && npm run build:test --silent && node --test .zero/test-js/*.test.js`)
5. **Docs test** — `node --test docs-site/src/tests/*.test.mjs`
6. **ZLS self-test** — language server self-test
7. **Agent demo** — `node scripts/agent-repair-demo.mjs`
8. **Workspace test** — extensions test (`npm run test -w zero-lang`)

**Corpus observation:** 8-layer test pipeline at 2-day-old project. Even v66 agentmemory (which is mature) had ~5 test layers. v68 zero's test density is corpus-distinctive — driven by need for early-stage compiler reliability.

**`scripts/agent-repair-demo.mjs`** — corpus-distinctive demo script that probably exercises the `zero fix --plan --json` workflow. Agent-first repair flow as a first-class test target.

---

## 10. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v51 agent-skills-of-vercel](../../agent-skills-of-vercel - Beginner Analysis/CLAUDE.md)** | Same Vercel umbrella org parent; `@vercel/sandbox` dep links Zero (vercel-labs) to Vercel main org tooling |
| [v66 agentmemory](../../agentmemory - Beginner Analysis/CLAUDE.md) | Pattern #85 Platform-Primitive Foundation — Zero is NOT a Platform-Primitive Foundation (uses C bootstrap; doesn't delegate infrastructure to host platform). Distinct from agentmemory's iii-engine exclusive delegation. |
| [v67 opencode-antigravity-auth](../../opencode-antigravity-auth - Beginner Analysis/CLAUDE.md) | Adjacent T4-Bridge-vs-PROVISIONAL-T1-language; both engage @vercel-style sandbox infrastructure (different sandboxes but both vendor-published) |

---

## 11. Pattern Library implications from Entity 2

- **NEW observational candidate: Self-Hosted Compiler Bootstrap** — corpus-first. Two-implementation architecture (native C + Zero-authored). Could generalize if other corpus subjects implement compilers; currently corpus-N=1.
- **NEW observational candidate: In-Browser-Compiler-Via-WASM** — playground compiler compiled to WASM. Could generalize to other language subjects but currently corpus-N=1.
- **Pattern #66 meta-supply-chain-awareness strengthening** — checksum verification on install + sandbox-by-default for native tests + `@vercel/sandbox` for security-critical sandboxing.
- **Pattern #57 57c product-internals corpus-citation chain N+1** — `@vercel/sandbox` links v68 (vercel-labs) to v51 (Vercel main org) corpus subject. STRENGTHENING evidence.
- **Pattern #85 Platform-Primitive Foundation NOT applicable** — Zero has its own C bootstrap + self-hosted compiler. Does NOT delegate infrastructure to a host platform (criterion (a) violated). Pattern #85 N=1 stale-flagged status retained.

---

## 12. References

- AGENTS.md project layout + release workflow + development sections
- package.json (40+ scripts; 8-layer test pipeline; @vercel/sandbox dep)
- CHANGELOG.md (v0.1.0 substantial-from-day-one; v0.1.1 installer + skills protocol; v0.1.2 borrow checker)
- Cross-cluster: cluster-2 (AGENTS.md) + cluster-3 (CHANGELOG + skills + compiler architecture)
