# (C) Entity 1: The Zero language — agent-first design + pre-1.0 discipline

**Type:** Core product entity
**Slot:** Entity 1 of 4
**Sibling entities:** [Entity 2 — Compiler architecture](entity-2-compiler-architecture-and-bootstrap.md) / [Entity 3 — Skills-Protocol-As-Binary-Bootstrap](entity-3-skills-protocol-as-binary-bootstrap.md) / [Entity 4 — Storm Bear meta](entity-4-storm-bear-meta.md)

---

## 1. Identity

**Repository:** [github.com/vercel-labs/zero](https://github.com/vercel-labs/zero)
**Homepage:** [zerolang.ai](https://zerolang.ai)
**Author:** Vercel Labs (vercel-labs org; sub-org of Vercel main)
**Maintainer:** `@ctate` (release-branch namespace `ctate/v0.1.x`)
**License:** Apache-2.0
**Status:** v0.1.2 (2026-05-17) — pre-1.0 experimental
**Created:** 2026-05-16 (v0.1.0) — **2 days old at wiki build**
**Stats at v68 wiki build:** 2,100 stars / 136 forks / 9 watchers / 14 open issues / 91 commits / 3 releases
**Velocity:** 1,050 stars/day = EXTREME-VIRAL (2nd-highest in 67-wiki corpus history)

---

## 2. What Zero is (one-paragraph)

**Zero is a programming language whose primary users are AI agents.** Vercel Labs publishes Zero as an "agent-first" experiment exploring what design choices change when agents (rather than humans) are the primary readers, writers, debuggers, and repairers of code. The language is pre-1.0 (current v0.1.2) and explicitly unstable — breaking changes happen as the project searches for patterns that work best for agents. The README opens with a Pattern #83 honest-deficiency-disclosure: *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure."*

---

## 3. The "agent-first" inversion

Zero's design axiom inverts a typical software-engineering assumption: traditionally, programming languages are designed for humans, with tooling added later to help agents. Zero's framing reverses this — *agents are primary users from day one*. The README states (verbatim):

> *"The project is exploring what changes when agents are primary users from day one: a language that can be learned on the fly, tooling that exposes structured facts for debugging and repair, and a standard library broad enough that most programs do not start with a dependency search."*

**Structural implications for the language:**

1. **Learnability:** A small, regular surface that an LLM can pick up from examples alone, without prior training on Zero specifically. Reduces vocabulary an agent needs to memorize.
2. **Standard library depth:** Common operations live in stdlib (`std.crypto`, `std.http`, `std.net` per v0.1.1 CHANGELOG) — agents don't need to dependency-search to get networking or crypto primitives.
3. **Deterministic structured output:** Diagnostics, module graphs, size reports, and fix plans are emitted as JSON — agents can inspect and act on them mechanically.
4. **Regularity over syntax:** Verbose-but-regular wins over concise-but-irregular. *"Even when that makes code more explicit than a human might choose in another language."*

**Corpus-first observation:** Zero is the **first corpus subject explicitly framing agents as the END USER** (not the augmentee). Prior corpus subjects positioned agents as the augmentee (T1 skill collections augment Claude Code), the backend caller (T2 agentmemory), the educational target (T3 courses), the runtime to be bridged (T4 plugins), or the deployable feature (T5 apps). Zero v68 inverts: agents READ Zero programs, WRITE Zero programs, and DEBUG Zero programs.

---

## 4. The 5 explicit design axioms (verbatim)

From README §"What Zero Is Aiming For":

| # | Axiom | Verbatim |
|---|-------|----------|
| 1 | Agent-first learnability | *"a small, regular language surface that agents can pick up quickly from examples, docs, and compiler feedback."* |
| 2 | Standard-library depth | *"common capabilities should live in documented, coherent library APIs instead of scattered dependency stacks."* |
| 3 | Deterministic tooling | *"diagnostics, graph facts, size reports, explanations, and fix plans should be structured enough for agents to inspect and act on."* |
| 4 | Direct developer experience | *"checking, running, formatting, inspecting, and repairing code should be fast, copyable, and scriptable."* |
| 5 | Regularity over syntax | *"prefer one obvious way to express most things, even when that makes code more explicit than a human might choose in another language."* |

**Axiom 2 deserves special note: anti-dependency-stack stance.** Most modern language ecosystems (npm, pip, cargo) optimize for "small core + rich third-party ecosystem." Zero inverts: comprehensive stdlib so most programs don't need third-party deps. Aligns with the agent-first axiom — agents can rely on a known stdlib surface without first searching for "what package should I use for HTTP?"

**Axiom 3 is Zero's anchor to agentic tooling.** Five compiler commands emit JSON (`--json` flag):
- `zero check --json` — type/syntax checking
- `zero graph --json` — module graph
- `zero size --json` — program size report
- `zero routes --json` — routing/endpoint enumeration (Zero has **built-in routing primitive**)
- `zero fix --plan --json` — fix plan
- `zero doctor --json` — environment diagnostics

**Corpus observation: fix-plan-as-first-class-primitive.** `zero fix --plan` produces a STRUCTURED PLAN that an agent can inspect BEFORE applying. Distinct from `--auto` patterns that mutate code immediately. Zero treats fix-as-plan + fix-as-application as separate stages.

---

## 5. Pre-1.0 discipline (Pattern #83 N=4 evidence)

The pre-1.0 disclosure framing is unusually direct. README + AGENTS.md both contain explicit unbounded-failure-mode disclosure:

**README §safety (lines 7-9):**

> *"Zero is pre-1 and intentionally unstable. The project will make breaking changes while it searches for the language, library, and tooling patterns that work best for agents. Treat today's syntax and APIs as something to explore, not something to memorize."*
>
> *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure. If you plan to run or develop Zero, do so in an isolated, disposable environment."*

**AGENTS.md §safety (lines 25-32):**

> *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure."*
>
> *"Run and develop Zero in safe environments: isolated workspaces, disposable inputs, and systems where compiler crashes, malformed output, or unsafe runtime behavior cannot damage production state. Treat generated artifacts and examples as experimental unless they have been reviewed for the specific environment where they will run."*

**Pattern #83 evaluation (3 promotion criteria):**

| # | Criterion | Verdict | Evidence |
|---|-----------|---------|----------|
| 1 | Explicit numerical or categorical deficiency disclosure | ✅ STRONG PASS | Categorical: TOS not relevant but parallel categorical mode disclosure ("compiler crashes", "malformed output", "unsafe runtime behavior", "Security vulnerabilities should be expected"). Quantitative implicit (pre-1.0 = unstable surface). |
| 2 | User-facing surface | ✅ STRONG PASS | Disclosed in README opening paragraphs AND in AGENTS.md (contributor-facing). Two-surface-saturation. |
| 3 | Does NOT minimize | ✅ STRONG PASS | "Not ready for production" + "isolated, disposable environment" + "compiler crashes, malformed output, or unsafe runtime behavior cannot damage production state" — direct, not softened. |

→ **Pattern #83 N=4 evidence saturated** at 2 surfaces in single subject (similar to v67's 5-surface saturation but at less density).

---

## 6. Anti-compatibility-as-policy (corpus-first stance)

AGENTS.md states (lines 13-17, verbatim):

> *"Do not preserve legacy behavior by default. Prefer the clearer agent-facing design over compatibility shims, migration layers, or carrying old paths forward. Keep examples, docs, tests, and command contracts aligned with the new behavior so the repository describes one coherent current system."*

This is a **deliberate anti-compatibility stance** — distinct from typical software-engineering norms. Implications:

- No `@deprecated` markers carried across versions
- No compatibility shims for old syntax
- Examples + docs + tests + command-contracts must align with current behavior

**Corpus contrast:** Most corpus subjects (v62 codex-plugin-cc / v66 agentmemory / v67 opencode-antigravity-auth) carry compatibility-discipline. Zero v68 inverts: **breaking changes are the default; compatibility is the deviation.**

**Operational discipline:** Repository must describe ONE COHERENT CURRENT SYSTEM. No evolution-of-systems narrative in the docs. Each release is a fresh slate.

---

## 7. Standard library + language primitives (early evidence)

CHANGELOG v0.1.1 adds module docs for:
- `std.crypto` — cryptography stdlib
- `std.http` — HTTP stdlib
- `std.net` — networking stdlib

These are early modules — likely many more exist but module docs are still being authored.

README's common-commands list includes:
- `zero routes --json examples/web/hello` → Zero has **built-in routing primitive** for web frameworks. Corpus-first: routing as language-level concept (not framework-level).

CHANGELOG v0.1.2 details **borrow checking with provenance tracking**:

> *"Rebuilds borrow provenance tracking across references, fields, subpaths, assignments, control-flow joins, receiver side effects, generic methods, return summaries, and unreachable paths."*
>
> *"Tightens borrow conflict checking by deriving conflicts from provenance and comparing concrete places."*

**Zero has Rust-style ownership/borrow checking** as a language feature. Corpus-first observation: no prior corpus subject documented borrow-checker semantics. This positions Zero as a memory-safe systems language (not just a scripting language for agents).

---

## 8. File extension `.0` and language identity

Zero source files use `.0` extension:
- `examples/hello.0`
- `examples/add.0`
- `examples/point.0`

**Corpus observation:** Visual brand signal — "zero" → `.0`. Distinct from `.zero` or `.zr` alternatives. The choice anchors language identity in a visually distinctive single-character extension.

---

## 9. Cross-references to corpus

| Sibling | Why |
|---------|-----|
| **[v51 agent-skills-of-vercel](../../agent-skills-of-vercel - Beginner Analysis/CLAUDE.md)** | Same Vercel umbrella org parent; both engage Anthropic skills protocol. vercel-labs is SUB-ORG of vercel main. Pattern #57 57c-product corpus-citation chain (Zero depends on `@vercel/sandbox`). |
| **[v63 andrej-karpathy-skills](../../andrej-karpathy-skills - Beginner Analysis/CLAUDE.md)** | Velocity-record sibling. karpathy-skills v63 corpus-record 1,186 stars/day; zero v68 is 2nd at 1,050 stars/day. |
| [v62 codex-plugin-cc](../../codex-plugin-cc - Beginner Analysis/CLAUDE.md) | Corporate-strategic sibling (different vendor). Both Pattern #19 corporate-strategic archetype. |
| [v67 opencode-antigravity-auth](../../opencode-antigravity-auth - Beginner Analysis/CLAUDE.md) | Adjacent v2.2-routine wiki + Pattern #83 N=3→N=4 strengthening chain. |

---

## 10. Pattern Library implications from Entity 1

- **Pattern #83 N=4 strengthening** consolidated (specific-failure-mode disclosure + 2-surface-saturation).
- **NEW Pattern candidate: Agent-First-Language-Substrate** design philosophy — corpus-first inversion (agents as END USER, not augmentee).
- **NEW observational candidate: Anti-Compatibility-As-Project-Policy** — explicit "do not preserve legacy behavior by default." Corpus-first stance.
- **Pattern #18 Agent Runtime Standardization** — Zero is NOT a runtime in Pattern #18's sense (it's a language, not an agent harness). Pattern #18 doesn't apply.
- **Pattern #19 ecosystem-portfolio-builder** — corporate-strategic-lab sub-archetype evidence (vercel-labs as portfolio shape within Vercel umbrella). NOT a NEW sub-archetype within Pattern #19 (corporate-strategic already exists per v65 Piebald-AI); rather a refinement (corporate-published-but-individual-maintained sub-pattern per Cluster 2).

---

## 11. References

- README.md (73 lines) — primary
- AGENTS.md (107 lines) — project direction + safety
- CHANGELOG.md (44 lines) — release narrative
- Cross-cluster: cluster-1 (design axioms) + cluster-2 (anti-compatibility policy)
