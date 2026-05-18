# (C) Cluster 1: README + agent-first design philosophy

**Source:** [README.md](https://raw.githubusercontent.com/vercel-labs/zero/main/README.md) (73 lines, ~3 KB)
**Cluster focus:** Tagline / 5 design axioms / quick-start install flow / common commands / validation scripts / pre-1.0 disclosure framing

---

## 1. Verbatim tagline + identity

**README title:** `# Zero`

**One-sentence identity (line 3):**

> *"Zero is an experiment in building an agent-first programming language."*

**Two-paragraph expanded positioning (verbatim from README, lines 5-9):**

> *"The project is exploring what changes when agents are primary users from day one: a language that can be learned on the fly, tooling that exposes structured facts for debugging and repair, and a standard library broad enough that most programs do not start with a dependency search."*
>
> *"Zero is pre-1 and intentionally unstable. The project will make breaking changes while it searches for the language, library, and tooling patterns that work best for agents. Treat today's syntax and APIs as something to explore, not something to memorize. If that sounds useful, try it with us: run examples, inspect the structured output, and send feedback about what helps agents work better."*
>
> *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure. If you plan to run or develop Zero, do so in an isolated, disposable environment."*

**Corpus-first observation #1:** The phrase **"agents are primary users from day one"** is a design-axiom statement unprecedented in the 67-prior-wiki corpus. Prior corpus subjects either (a) augment agent capabilities (T1 skill collections), (b) serve agents as backend (T2 services), (c) educate agents/humans about agents (T3), (d) bridge agent runtimes (T4), or (e) deploy agents as features (T5). Zero v68 inverts the consumer relationship: **agents are the END USER, not the augmentee.** Distinct from all prior corpus framings.

**Corpus-first observation #2:** The Pre-1.0 + intentionally-unstable + security-vulnerabilities-expected framing is **the most prominent pre-1.0 honesty disclosure in the corpus**. Stronger than v67 opencode-antigravity-auth's TOS-violation framing in directness (no "may" — directly says "should be expected"). Pattern #83 Honest-Deficiency-Disclosure N=4 candidate.

---

## 2. The 5 design axioms (verbatim from "What Zero Is Aiming For" section)

The README enumerates 5 explicit design axioms (lines 11-17):

1. **Agent-first learnability:** *"a small, regular language surface that agents can pick up quickly from examples, docs, and compiler feedback."*
2. **Standard-library depth:** *"common capabilities should live in documented, coherent library APIs instead of scattered dependency stacks."*
3. **Deterministic tooling:** *"diagnostics, graph facts, size reports, explanations, and fix plans should be structured enough for agents to inspect and act on."*
4. **Direct developer experience:** *"checking, running, formatting, inspecting, and repairing code should be fast, copyable, and scriptable."*
5. **Regularity over syntax:** *"prefer one obvious way to express most things, even when that makes code more explicit than a human might choose in another language."*

**Corpus observation:** Axiom 2 ("most programs do not start with a dependency search") is a direct counter-stance against the NPM/PyPI ecosystem norm. Axiom 5 ("one obvious way") echoes Python's Zen but inverts the human-preference axis — Zero explicitly prefers verbose-but-regular over concise-but-irregular EVEN WHEN humans would prefer concise. **This is the structural marker of "agent-first" — preferring agent-parseability over human-conciseness as a hard rule.**

**Sub-observation: Axiom 3 ("structured enough for agents to inspect and act on")** matches the broader corpus pattern of structured-JSON output for agentic tools (Pattern #21 evidence-list pattern; agentic-friendly diagnostic format). Zero formalizes this AT THE COMPILER LEVEL.

---

## 3. Quick-start install flow (verbatim)

The install path (lines 21-27):

```bash
curl -fsSL https://zerolang.ai/install.sh | bash
export PATH="$HOME/.zero/bin:$PATH"
zero --version
```

**Corpus observation:** The `curl | bash` install pattern is corpus-distinctive choice. Compare:
- v51 agent-skills-of-vercel: `pnpm install`
- v62 codex-plugin-cc: npm install + Claude Code marketplace
- v64 claude-seo: `bash install.sh` + PowerShell + plugin marketplace (3-way)
- v66 agentmemory: npm-distributed
- v67 opencode-antigravity-auth: npm install via Opencode config

Zero v68's `curl https://zerolang.ai/install.sh | bash` install is **direct-from-vendor-domain** (zerolang.ai) rather than npm-mediated. Per CHANGELOG v0.1.1: *"Adds the public installer at `https://zerolang.ai/install.sh`, with platform selection, GitHub release downloads, checksum verification, and `$HOME/.zero/bin/zero` installation."* Includes checksum verification — supply-chain-aware install.

**Pattern Library implication:** Strengthens Pattern #66 meta-supply-chain-awareness — explicit checksum verification on install. Distinguishes from naive `curl | bash` patterns that skip integrity verification.

---

## 4. Three example commands (verbatim from README)

The README shows 3 entry-point commands (lines 29-45):

```bash
zero check examples/hello.0       # Check a program
zero run examples/add.0           # Run a small executable
```

Expected output:

```text
math works
```

**Corpus observation:** File extension `.0` is Zero's chosen extension. This is a deliberate visual choice — "zero" → `.0` — making source files visually distinguishable from `.js`/`.py`/`.ts`/`.go` in mixed repos. Corpus-first observation: extension choice as project-brand signal.

---

## 5. Common commands enumerated (verbatim, lines 49-58)

```bash
zero check examples/hello.0
zero run examples/add.0
zero build --emit exe --target linux-musl-x64 examples/add.0 --out .zero/out/add
zero graph --json examples/systems-package
zero size --json examples/point.0
zero routes --json examples/web/hello
zero skills get zero --full
zero doctor --json
```

**8 commands surfaced as "common" — corpus observation:**

| Command | Function | Agent-readability axis |
|---------|----------|------------------------|
| `zero check` | Type/syntax checking | Diagnostic output |
| `zero run` | Build + execute | Direct user experience |
| `zero build` | Compile to target executable | Build chain (3 explicit targets named: `exe`, `linux-musl-x64`, with `--out` path) |
| `zero graph --json` | Module graph output | **Structured-JSON-for-agents** (axiom #3) |
| `zero size --json` | Program size report | **Structured-JSON-for-agents** |
| `zero routes --json` | Routing/endpoint enumeration | **Structured-JSON-for-agents** (web framework primitive) |
| `zero skills get zero --full` | Compiler-served version-matched skill content | **Skills-protocol integration (Cluster 3 PRIMARY)** |
| `zero doctor --json` | Environment diagnostics | **Structured-JSON-for-agents** |

**Corpus observation:** 5 of 8 commands have explicit `--json` output flag. This is **structured-JSON-as-first-class-output-format** — distinct from typical CLIs that surface JSON as a secondary `--format=json` flag. Zero's CLI design assumes agents will consume output structurally.

**Sub-observation: `zero routes`** suggests Zero has built-in web framework primitives — routes are language-level concept, not framework-level. Corpus-first integration of routing at language level (most languages defer routing to frameworks).

---

## 6. Validation scripts (verbatim)

```bash
npm run docs:test
npm run conformance
npm run native:test
npm run command-contracts
```

**Corpus observation:** Four validation layers documented in README:
1. **docs:test** — documentation tests (link integrity? example execution?)
2. **conformance** — language + CLI fixture conformance
3. **native:test** — native compiler tests
4. **command-contracts** — CLI command-output contract validation

The "command-contracts" layer is corpus-distinctive — Zero validates that CLI command outputs match documented contracts. This is **CLI-output-as-contract** discipline. Particularly relevant for agent-consumers who depend on stable structured output.

Plus benchmarks (line 71):
```bash
npm run bench
```

---

## 7. Cluster 1 summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | "Agents are primary users from day one" design axiom (inverts consumer relationship vs prior 67 corpus subjects) | corpus-first |
| 2 | Most prominent pre-1.0 honesty disclosure in corpus (security-vulnerabilities-expected + not-for-production + isolated-disposable-environment) | corpus-first explicit framing |
| 3 | Standard-library-depth-as-anti-dependency-stack design axiom | corpus-first |
| 4 | Regularity-over-syntax with explicit verbose-but-regular preference | corpus-first language-level discipline |
| 5 | File extension `.0` as visual brand signal | corpus-first |
| 6 | Structured-JSON-as-first-class-output-format (5 of 8 common commands have `--json`) | corpus-distinctive |
| 7 | Compiler-level routes primitive (`zero routes --json`) | corpus-first |
| 8 | CLI-output-as-contract validation discipline (`command-contracts`) | corpus-first |
| 9 | Curl-bash install with checksum verification at zerolang.ai vendor domain | corpus-distinctive (combines direct-install + supply-chain-aware) |

---

## 8. Pattern Library implications from Cluster 1

- **Pattern #83 Honest-Deficiency-Disclosure (CANDIDATE N=3 PROMOTION-ELIGIBLE at v67):** STRONG N=4 evidence. README opens with explicit "Security vulnerabilities should be expected" + "not ready for production systems" + "isolated, disposable environment." Consolidates Pattern #83 promotion case (already promotion-eligible from v67; v68 adds N=4 evidence).
- **Pattern #66 meta-supply-chain-awareness (CONFIRMED):** Strengthening — checksum-verified curl install + isolated-disposable-environment guidance.
- **NEW Pattern candidate: Agent-First-Language-Substrate design philosophy** — explicit "agents as primary users from day one" + 5 supporting design axioms. Distinct from "agent-augmentation" pattern (prior corpus default).
- **NEW Pattern candidate: Structured-JSON-as-First-Class-CLI-Output** — Zero's `--json` ubiquity (5 of 8 common commands) formalizes a pattern observable across recent corpus tooling but never named.
- **Pattern #52 EXTREME-VIRAL-Velocity:** 1,050 stars/day evidence captured here (full velocity analysis in Cluster 3 CHANGELOG narrative).

---

## 9. References

- README.md (73 lines) — primary source
- zerolang.ai (homepage, not fetched in detail)
- Cross-cluster: cluster-2 (AGENTS.md safety expectations corroborate) + cluster-3 (CHANGELOG release velocity)

## 10. Next cluster

Cluster 2: AGENTS.md + project direction + safety expectations + development workflow + project layout + release workflow.
