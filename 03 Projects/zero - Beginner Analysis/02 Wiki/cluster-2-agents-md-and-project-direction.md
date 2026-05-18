# (C) Cluster 2: AGENTS.md + project direction + safety + development workflow

**Source:** [AGENTS.md](https://raw.githubusercontent.com/vercel-labs/zero/main/AGENTS.md) (107 lines, ~3.5 KB)
**Cluster focus:** Contributor expectations / breaking-changes policy / safety expectations / development workflow / project layout / release workflow

---

## 1. AGENTS.md self-description (verbatim opening)

The file title is **`# Contributor Notes`** (not "AGENTS.md" frontmatter) but the filename uses the corpus-standard `AGENTS.md` convention.

Opening 3 lines:

> *"Zero is a pre-1 experiment in building an agent-first programming language."*
>
> *"Keep public-facing changes honest about what works today without weakening that positioning."*

**Corpus observation:** The instruction *"Keep public-facing changes honest about what works today without weakening that positioning"* is a deliberate **honesty-as-positioning-asset** stance. Honest disclosure is treated as a brand asset, not a liability. This corroborates Pattern #83 N=4 reading from Cluster 1.

---

## 2. Project direction policy (verbatim)

**Breaking-changes policy (lines 7-22, full):**

> *"Zero is still being shaped around the needs of agents. Breaking changes are acceptable when they move the language, standard library, compiler, or tooling closer to that goal."*
>
> *"Do not preserve legacy behavior by default. Prefer the clearer agent-facing design over compatibility shims, migration layers, or carrying old paths forward. Keep examples, docs, tests, and command contracts aligned with the new behavior so the repository describes one coherent current system."*
>
> *"This does not mean broad churn for its own sake. Make direct changes that advance Zero's agent-first goals: on-the-fly learnability, deterministic inspection and repair, strong standard-library coverage, exceptional developer experience, and regular patterns over syntactic convenience."*

**Corpus observation #1:** *"Do not preserve legacy behavior by default"* is a **deliberate anti-compatibility stance** — opposite of the typical software engineering norm. Distinct from v62 codex-plugin-cc (compatibility-preserving), v66 agentmemory (versioned migrations), v67 opencode-antigravity-auth (Storage V4 migration chain v1→v4). Zero v68 inverts: **breaking changes are the default; compatibility is the deviation.**

**Corpus observation #2:** *"Keep examples, docs, tests, and command contracts aligned with the new behavior so the repository describes one coherent current system"* is a **synchronicity-discipline-as-policy** statement. Forces the entire repo to evolve together rather than accumulating stale-references. Distinct from v64 claude-seo's manifest-drift CI (Pattern #81 candidate — version-string-consistency); zero's discipline is BEHAVIORAL-consistency across docs/tests/examples/contracts.

**Pattern Library implication:** This is **Pattern #81 Manifest-Drift evolution candidate** — Pattern #81 was registered N=1 at v66 for version-string drift across files. Zero v68 extends the concept to BEHAVIORAL drift (docs/tests/contracts must match runtime behavior). Sister observation flag for Pattern #81 v68 stale-check.

---

## 3. Safety expectations (verbatim)

**Lines 25-32:**

> *"Security vulnerabilities should be expected. Zero is not ready for production systems, sensitive data, or trusted infrastructure."*
>
> *"Run and develop Zero in safe environments: isolated workspaces, disposable inputs, and systems where compiler crashes, malformed output, or unsafe runtime behavior cannot damage production state. Treat generated artifacts and examples as experimental unless they have been reviewed for the specific environment where they will run."*

**Corpus observation:** This is **disclosure-of-specific-risk-modes** beyond the generic "experimental" disclaimer:
- compiler crashes
- malformed output
- unsafe runtime behavior

Naming specific failure modes rather than generic risks = **stronger Pattern #83 evidence** than typical pre-1.0 disclaimers. Compares to v67 opencode-antigravity-auth's "account ban / shadow-ban" specific-mode disclosure (TOS-axis) — zero v68 names specific safety-axis failure modes.

The phrase *"Treat generated artifacts and examples as experimental unless they have been reviewed for the specific environment where they will run"* is **specifically responsible-AI-output framing** — recognizing that Zero may generate downstream artifacts that could be misused if propagated without review. Distinct from "this software has bugs" — more like "this software's OUTPUT is also experimental until reviewed."

---

## 4. Development workflow (verbatim)

**Lines 35-49:**

> *"- Build the local compiler with `make -C native/zero-c`."*
> *"- Use `bin/zero` for focused checks."*
> *"- Keep examples runnable and docs copyable."*
> *"- Prefer small, direct changes over broad refactors."*
> *"- Use direct emitters for compiler output."*

**5 development principles:**
1. **Build via Make in native/zero-c** — bootstrap compiler
2. **bin/zero for focused checks** — CLI dispatcher
3. **Keep examples runnable + docs copyable** — synchronicity-discipline restated
4. **Small direct changes over broad refactors** — anti-churn (corroborates project direction)
5. **Direct emitters for compiler output** — compiler-internal idiom

**Useful Checks block (lines 44-49):**

```sh
npm run docs:test
npm run conformance
npm run native:test
npm run command-contracts
```

**Focused compiler work block (lines 53-59):**

```sh
bin/zero check --json <file-or-package>
bin/zero graph --json <file-or-package>
bin/zero size --json <file-or-package>
bin/zero explain <diagnostic-code>
bin/zero fix --plan --json <file-or-package>
```

**Corpus observation:** `bin/zero fix --plan --json` is the **fix-plan-as-structured-output** primitive — agents can request a fix PLAN (JSON-structured) rather than just running a fix. Distinct from `apply --auto` which is destructive. Zero treats fix-as-plan + fix-as-application as separate stages, giving agents inspection-before-action capability. Corpus-first observation: **fix-plan-as-first-class-primitive at compiler level.**

`bin/zero explain <diagnostic-code>` is also corpus-distinctive — diagnostic codes have explainability built into the compiler, similar to TypeScript's `tsc --explainFiles` but unified with the fix-plan system.

---

## 5. Project layout (verbatim, lines 61-68)

```
- `native/zero-c/`:     native compiler implementation.
- `compiler-zero/`:     Zero-authored compiler sources.
- `examples/`:          small runnable programs and packages.
- `conformance/`:       language and CLI fixtures.
- `docs-site/`:         public documentation site.
- `scripts/`:           validation and release support tooling.
```

**Corpus observation #1: Self-hosted compiler architecture.** Two compiler implementations:
- `native/zero-c/` — bootstrap C compiler (the actual binary users install)
- `compiler-zero/` — Zero-authored Zero compiler (self-hosting in progress?)

This is the **classic bootstrapped-compiler pattern** — write the language in another language first, then re-write the compiler in the language itself. **Corpus-first observation** — Zero is the FIRST corpus subject with self-hosted compiler bootstrap.

**Corpus observation #2: Conformance fixtures as separate directory.** v68 zero's `conformance/` directory exists for language + CLI fixtures. This is **conformance-test-suite-as-first-class-artifact** — separate from `tests/` directory. Distinct discipline: tests check implementation, conformance fixtures check behavior-contracts. Corpus-first observation.

**Corpus observation #3: docs-site/ as separate workspace.** The public docs (zerolang.ai) live in `docs-site/` and have their own package.json — separate from the compiler workspace. Distinct from v64 claude-seo (docs co-located) and v66 agentmemory (docs in main repo). Two-package monorepo pattern with `pnpm` (per `docs:install` script in package.json: `pnpm --prefix docs-site install`).

---

## 6. Public Docs Policy (verbatim, lines 70-74)

> *"Docs should describe current user-facing behavior, not internal development history. Avoid release-planning language, validation-report narratives, and implementation diary details in pages intended for external readers."*

**Corpus observation:** This is **policy-against-implementation-diary-leakage-to-docs**. Distinct from v65 claude-code-system-prompts (Piebald-AI does opposite — documents implementation history continuously). Zero's policy: external docs are about CURRENT behavior, not historical evolution.

Aligns with Zero's "synchronicity-discipline" (Cluster 2 §2) — the repo represents one coherent current system, not an evolution-of-systems.

---

## 7. Release workflow (verbatim, lines 76-107)

The release workflow is **manual, single-maintainer-controlled**:

> *"Releases are manual, single-branch affairs. The maintainer controls the changelog voice and format."*

**7-step release process:**

1. Create release branch (e.g., `ctate/v0.1.1`) — **MAINTAINER NAMESPACE: `ctate/`**
2. Bump version in **5 files**:
   - `package.json`
   - `package-lock.json`
   - `docs-site/package.json`
   - `extensions/vscode/package.json`
   - `native/zero-c/src/main.c`
3. Update command-contract expectations that assert the compiler version
4. Write `CHANGELOG.md` entry wrapped in `<!-- release:start -->` and `<!-- release:end -->` markers
5. Remove release markers from previous entry (only latest entry has markers)
6. Include `### Contributors` section in marked changelog entry; derive from commit authors + `Co-authored-by` trailers since previous tag
7. Run focused checks:
   ```sh
   make -C native/zero-c
   bin/zero --version --json
   npm run test:zero
   npm run command-contracts:local
   npm run docs:test
   ```

**Corpus observations:**

**Observation #1: Single-maintainer release voice.** *"The maintainer controls the changelog voice and format."* — corporate Vercel Labs publishes Zero, but release maintenance is single-individual (`@ctate` per release-branch namespace). This is **single-individual-maintainer-within-corporate-org** — distinct corpus archetype. Within Pattern #19 ecosystem-portfolio-builder sub-archetypes (corporate-strategic), this is a sub-pattern variant: **corporate-published-but-individual-maintained**.

**Observation #2: 5-file manifest-drift discipline IS Pattern #81 candidate evidence.** Pattern #81 Manifest-Drift-As-First-Class-CI-Concern was registered N=1 at v66 from v64 claude-seo (5-version-source CI assertions). Zero v68 has 5-file version bump discipline (matches the structural property: ≥3 file locations) but it's documented in AGENTS.md as MANUAL workflow, not CI-enforced.

The Pattern #81 promotion criteria require:
1. CI explicitly asserts version-string consistency across ≥3 file locations
2. Drift causes mechanical PR-block (not just warning)
3. Framework documents this as discipline (CONTRIBUTING.md or similar) rather than incidental check

Zero v68 satisfies (3) — discipline documented in AGENTS.md. But (1) and (2) require CI enforcement which AGENTS.md does NOT establish — the workflow is described as MANUAL ("Releases are manual, single-branch affairs"). So Zero v68 is **partial N=2 evidence for Pattern #81** — discipline documented but enforcement is manual not CI.

→ Sister observation flag: Pattern #81 v68 evaluation: discipline-documented-but-not-CI-enforced sub-variant.

**Observation #3: Changelog markers as machine-readable release-body extraction.** `<!-- release:start -->` / `<!-- release:end -->` markers let the release workflow extract changelog content for GitHub release body. **Markers-as-machine-readable-content-boundary** — corpus-distinctive simple solution to changelog-as-release-narrative.

**Observation #4: Contributors derived from commit authors + Co-authored-by trailers.** This is **automated-attribution-from-git-trailers** — same mechanism that this very repository's commit messages use. Corpus-distinctive convention adoption.

---

## 8. Contributors discipline (CHANGELOG cross-reference)

The CHANGELOG v0.1.2 entry shows:

```
### Contributors

- @ctate
- @badlogic
- @chenrui333
- @heylakatos
- @onevcat
```

And v0.1.1:

```
### Contributors

- @ctate
- @mvanhorn
```

**Pattern Library implications:**

**Pattern #82 Gamified-Curated Community Contribution (CANDIDATE N=1 v66):** Zero v68's per-release contributor lists are **simpler attribution-discipline** than v64 claude-seo's Pro Hub Challenge (which is a NAMED CURATED PROGRAM with explicit submission process). Zero v68 contributor listings are mechanical (extracted from commit trailers).

**Verdict:** Pattern #82 N=2 evidence is **WEAK** — same outcome (named-attribution per release) but different mechanism (programmatic extraction vs. named challenge program). Lean toward **sister observation not direct N+1**.

Alternative reading: register a NEW Pattern candidate "Automated-Per-Release-Contributor-Attribution-From-Git-Trailers" — distinct from Pattern #82's gamified-curated mechanism. But this would be a thin observation — defer registration unless v69 or later wikis provide N=2 evidence of the same mechanism.

---

## 9. Cluster 2 summary — corpus-firsts + corpus-records

| # | Observation | Status |
|---|-------------|--------|
| 1 | Anti-compatibility stance ("Do not preserve legacy behavior by default") | corpus-first |
| 2 | Synchronicity-discipline-as-policy (examples + docs + tests + contracts must align with current behavior) | corpus-first |
| 3 | Disclosure-of-specific-risk-modes (compiler crashes / malformed output / unsafe runtime behavior named explicitly) | corpus-distinctive (stronger than typical "experimental" disclaimer) |
| 4 | Responsible-AI-output framing ("Treat generated artifacts and examples as experimental unless they have been reviewed") | corpus-first |
| 5 | Fix-plan-as-first-class-primitive at compiler level (`bin/zero fix --plan --json`) | corpus-first |
| 6 | Self-hosted compiler bootstrap architecture (`native/zero-c/` + `compiler-zero/`) | **corpus-first** |
| 7 | Conformance-test-suite-as-first-class-artifact (separate from `tests/`) | corpus-first |
| 8 | Policy-against-implementation-diary-leakage-to-docs | corpus-first |
| 9 | Corporate-published-but-individual-maintained sub-pattern (Vercel Labs publishes; `@ctate` single maintainer with namespace release branches) | corpus-first within Pattern #19 |
| 10 | Markers-as-machine-readable-content-boundary (release markers for GitHub release body extraction) | corpus-distinctive |
| 11 | Automated-attribution-from-git-trailers (Contributors auto-extracted from commit authors + Co-authored-by) | corpus-distinctive |
| 12 | 5-file manifest-drift discipline (documented; not CI-enforced) — partial Pattern #81 evidence | Pattern #81 sister observation |

---

## 10. Pattern Library implications from Cluster 2

- **Pattern #83 N=4 strengthening** consolidated (specific-risk-mode disclosure + responsible-AI-output framing).
- **Pattern #19 ecosystem-portfolio-builder sub-archetype: corporate-published-but-individual-maintained** — Vercel Labs publishes corporately, `@ctate` maintains individually with namespace release branches. Distinct from v65 Piebald-AI (corporate-org publishing-and-maintaining) and from gotalab v61 / forrestchang v63 / AgriciDaniel v64 (solo individuals). NEW sister observation within already-CONFIRMED Pattern #19.
- **Pattern #81 Manifest-Drift partial N=2 evidence** — 5-file version-bump discipline documented in AGENTS.md but workflow is MANUAL, not CI-enforced. Sister observation flag for v68 audit (Pattern #81 was N=1 stale-risk-flagged at v66; v68 zero is "discipline-documented but not enforced" sub-variant).
- **Pattern #82 Gamified-Curated WEAK N=2** — per-release attribution discipline but mechanism is different from v64 Pro Hub Challenge. Sister observation; lean toward "different mechanism" interpretation.
- **NEW observational candidate: Self-Hosted Compiler Bootstrap** — native-language-bootstrap + self-hosted-Zero-compiler. Classic compiler engineering pattern, corpus-first in the wiki context.
- **NEW observational candidate: Anti-Compatibility-As-Project-Policy** — explicit "do not preserve legacy behavior by default." Corpus-first stance.
- **NEW observational candidate: Synchronicity-Discipline-As-Policy** — examples + docs + tests + contracts aligned with current behavior as repository invariant. Distinct from Pattern #81 (version-strings) — this is BEHAVIORAL alignment.

---

## 11. References

- AGENTS.md (107 lines) — primary source
- CHANGELOG.md (44 lines) — Contributors block cross-reference
- Cross-cluster: cluster-1 (design axioms) + cluster-3 (CHANGELOG + skills + compiler architecture)

## 12. Next cluster

Cluster 3: Skills protocol integration + compiler architecture + CHANGELOG history — skills/zero/SKILL.md + package.json + CHANGELOG.md + native/zero-c (referenced) + compiler-zero (referenced).
