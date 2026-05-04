# (C) CONTEXT + CLAUDE + AGENTS cluster summary — googleworkspace/cli

> **Sources:** CLAUDE.md (1 line) + AGENTS.md (209 lines, 9 sections) + CONTEXT.md (44 lines, 4 sections)
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Why cluster — novel tri-file agent documentation pattern

googleworkspace/cli is the **first corpus project with explicit tri-file agent documentation**:

| File | Audience | Purpose | Size |
|------|----------|---------|------|
| **CLAUDE.md** | Claude Code contributor | 1-liner pointer to AGENTS.md | 110 B / 1 line |
| **AGENTS.md** | AI + human contributors | Full contributor guidelines | 11,980 B / 209 lines |
| **CONTEXT.md** | **AI agents at runtime** | Rules of engagement for gws USERS (agents), not contributors | 2,669 B / 44 lines |

**CONTEXT.md is the novel piece.** Prior corpus:
- BMAD v11: AGENTS.md (3-rule minimal) — contributor only
- Superpowers: skills as docs — contributor + user
- codymaster v12: CLAUDE.md absent, AGENTS.md absent — uses `.claude-plugin/` manifest
- notebooklm-py v7: single mega-SKILL.md — user-facing

**googleworkspace/cli separates:**
- **Who builds it** (AGENTS.md) — the framework contributors
- **How to use it** (CONTEXT.md) — the runtime agents consuming the CLI

This is **architectural clarity about audience**. No prior project makes the distinction explicit.

## 2. CLAUDE.md — the pointer pattern

Full content (verbatim):

> *When contributing to this repository, you must strictly follow all guidelines outlined in the AGENTS.md file.*

**Observations:**
- 1 line, 110 bytes
- Pure pointer — no content duplication
- Matches BMAD v11 pattern: tiny AGENTS.md-as-contract (but BMAD had rules inline; googleworkspace delegates to longer AGENTS.md)
- Signals: "Claude Code is one AI-agent framework among many; our contributor contract is language-agnostic"
- **De-Claude-centrism** — Google doesn't privilege Claude. AGENTS.md is the source of truth.

**Implication for future wikis:** the 1-liner CLAUDE.md → AGENTS.md delegation may become standard. Saves content duplication across AI frameworks (Claude / Cursor / Gemini / Codex all follow same AGENTS.md).

## 3. AGENTS.md — 9 sections, 209 lines

### Section 1: Project Overview
**Dynamic Discovery** emphasis (IMPORTANT block):
> *"This project does NOT use generated Rust crates (e.g., `google-drive3`) for API interaction. Instead, it fetches the Discovery JSON at runtime and builds clap commands dynamically."*

**Package manager** (NOTE): `pnpm` not `npm` for Node.js assets in repo.

### Section 2: Build & Test
- `cargo build` / `cargo clippy -- -D warnings` / `cargo test`
- **Test coverage requirement:** `codecov/patch` mandates tests for new/modified lines
- **Testability discipline:** "extract testable helper functions rather than embedding logic in main/run"

### Section 3: Changesets
- Every PR requires `.changeset/<descriptive-name>.md`
- Semantic versioning designation: `patch` / `minor` / `major`
- Format:
  ```markdown
  ---
  "@googleworkspace/cli": patch
  ---
  <description>
  ```

**Parallel to BMAD v11** (changeset-driven) + Superpowers. Common pattern among maturing frameworks.

### Section 4: Architecture
- Two-crate workspace:
  - `crates/google-workspace/` — library (discovery, validation, client)
  - `crates/google-workspace-cli/` — binary (auth, commands, execution)
- Two-phase argument parsing:
  1. Identify service from argv[1]
  2. Fetch Discovery Document + build clap tree
  3. Re-parse remaining args

### Section 5: Demo Videos
- VHS-based (terminal recorder)
- Art in `art/` folder
- Scene organization conventions

### Section 6: Input Validation & URL Safety
**Security model:** *"Assume all CLI arguments are potentially adversarial."*

**Validator functions** (in `crates/google-workspace/src/validate.rs`):

| Function | Rejects |
|----------|---------|
| `validate_safe_output_dir()` | Absolute paths, `../` traversal, symlinks, control chars |
| `validate_safe_dir_path()` | Same as above for read ops |
| `validate_resource_name()` | Path traversal `..`, control chars, `?`, `#` |
| `encode_path_segment()` | Unencoded special chars |
| Clap `value_parser` | Values outside allowlist |

**Key distinction:** *"Environment variables are trusted inputs; CLI arguments are not."*

**This is the most formalized adversarial-input model in corpus.** ECC AgentShield handles security at tooling layer; gws embeds it in framework core.

### Section 7: PR Labels
8 labels for issue/PR organization:
- `area: discovery` (Discovery document ops)
- `area: http` (request/response)
- `area: docs` (documentation)
- `area: tui` (UI wizard)
- `area: distribution` (packaging + release)
- `area: auth` (OAuth + credentials)
- `area: skills` (AI skill generation)
- Plus default + bug/feature labels

**Structured triage discipline.**

### Section 8: Helper Commands
`+verb` prefix convention. **Anti-patterns (must NOT do):**
- Wrap single Discovery API call
- Expose existing response data via custom flags
- Replicate Discovery params as custom flags

**DO:**
- Multi-step orchestration (e.g., `gws gmail +triage` = list + classify + apply labels)
- Format translation (markdown → Gmail HTML)
- Multi-API composition (`gws workflow +meeting-prep` = calendar + drive + docs)

### Section 9: Environment Variables
20+ env vars organized in 5 groups (auth / config / OAuth client / sanitization / logging / helpers).

## 4. CONTEXT.md — agent runtime rules (novel)

Full structure:

### Section 1: Header (lines 1-4)
Describes gws CLI for agent reader.

### Section 2: Rules of Engagement for Agents (3 rules)

**Rule 1 — Schema Discovery:**
> *"If you don't know the exact JSON payload structure, run `gws schema <resource>.<method>` first to inspect the schema before executing."*

**Rule 2 — Context Window Protection:**
> *"Workspace APIs (like Drive and Gmail) return massive JSON blobs. ALWAYS use field masks when listing or getting resources by appending `--params '{\"fields\": \"id,name\"}'` to avoid overwhelming your context window."*

**Rule 3 — Dry-Run Safety:**
> *"Always use the `--dry-run` flag for mutating operations (create, update, delete) to validate your JSON payload before actual execution."*

### Section 3: Core Syntax
```bash
gws <service> <resource> [sub-resource] <method> [flags]
```

### Section 4: Key Flags
- `--params '<JSON>'`
- `--json '<JSON>'`
- `--page-all`

## 5. Why CONTEXT.md matters

Three architectural insights:

### Insight 1 — Separation of concerns
Contributors ≠ runtime agents. Different audiences need different docs. googleworkspace formalizes this.

### Insight 2 — Context-window as first-class concern
Rule 2 names "Context Window Protection" as a rule of engagement. This is the context-rot problem from GSD (T1 v5) elevated to user-facing rule.

### Insight 3 — Dry-run as safety primitive
Rule 3 mandates dry-run for mutations. Safety discipline in runtime docs, not just contributor docs.

**Parallel to codymaster v12's Self-Healing:** different solution to same problem. codymaster's FIX/DERIVED/CAPTURED is auto-repair at the framework level. gws's CONTEXT.md rules are human-enforced discipline at the user level.

## 6. Tri-file pattern as corpus contribution

If v13's pattern generalizes, future framework wikis should expect:
- `CLAUDE.md` (1-liner pointer)
- `AGENTS.md` (contributor guidelines, N sections)
- `CONTEXT.md` (runtime agent-user rules, 3-5 rules)

**Routine v2 candidate:** detect tri-file pattern during Phase 0; if present, use it as source cluster.

## 7. Cross-project comparison of agent documentation

| Project | Agent doc strategy | Depth |
|---------|---------------------|-------|
| ECC v1 | Distributed skills + rules | Rich but scattered |
| Superpowers v2 | Skills library | User-focused |
| gstack v3 | Role definitions | Per-role |
| goclaw v4 | CLAUDE.md + Architecture | Contributor |
| course v6 | Lessons-as-docs | Teaching |
| notebooklm-py v7 | Mega-SKILL.md (26KB) | Combined user+contrib |
| build-your-own-x v8 | README only | Aggregator |
| deer-flow v9 | Substantial AGENTS.md | Contributor |
| autoresearch v10 | program.md as agent skill | User-only |
| BMAD v11 | AGENTS.md 3-rule minimal + CONTRIBUTING | Contributor minimal |
| codymaster v12 | `.claude-plugin/` manifest | Plugin-level |
| **googleworkspace/cli v13** | **CLAUDE.md + AGENTS.md + CONTEXT.md tri-file** | **Most structured** |

→ Evolution visible: corpus trending from scattered → structured agent documentation. v13 = current peak.

## 8. Build & test discipline

From AGENTS.md §2:

**Required per PR:**
- `cargo test` passes
- `cargo clippy -- -D warnings` clean
- `codecov/patch` covers new/modified lines
- Changeset file at `.changeset/<name>.md`

**Testability rule (important):**
> *"Extract testable helper functions rather than embedding logic in main/run where it's hard to unit-test."*

**Parallel to BMAD's skill validator, stricter than most T1 peers.**

## 9. Cross-references

- [[(C) README summary]] — positioning, 11 services, install channels
- [[(C) 110 Skills + Helper Commands cluster summary]] — skill taxonomy
- [[(C) Dynamic Discovery Service Architecture]] (Phase 3 entity) — architecture driven by AGENTS.md constraint

## Open questions surfaced

- Changeset tool (JS npm) on Rust project — why? (Q23)
- `codecov/patch` coverage threshold specifics? (new — Q26)
- Helper command anti-patterns enforced how? (Q20)
- Label taxonomy complete or evolving? (new — Q27)
