# (C) OpenSandbox — Deep Dive

**Wiki:** v244 · **Date:** 2026-08-19 · **Subject:** [`opensandbox-group/OpenSandbox`](https://github.com/opensandbox-group/OpenSandbox)
**Tagline (verbatim):** *"Secure, Fast, and Extensible Sandbox runtime for AI agents."*
**License:** Apache-2.0 · **Page-stated:** ~14.3k★ / 1.3k forks / 57 watchers / 86 open issues ⚠️ *(§37.4 — the GitHub API is mocked in this environment; star/fork figures are page-stated, **not** API-verified, and are **not** a Pattern #52 velocity claim)*

**✅ SOURCE-CLONED TWICE.** A `--depth 1` working tree at HEAD **`b8cabe532392063851f8594e38e016b324c89468`** (2026-08-19 14:01:08 +0800, 125 MB, 2,221 tracked files) plus a blobless full history (**2,400 commits on `HEAD`, 2,545 on `--all`**). Every number below states its basis. **All git counts are `HEAD`-only unless marked `--all`** (v243 **D27**).

---

## 0. One-paragraph summary

OpenSandbox is a self-hostable control plane that creates, runs, inspects and destroys **isolated sandboxes for AI agents** — the compute substrate an agent executes code in. It ships a FastAPI lifecycle server with two runtime backends (Docker and Kubernetes), SDKs in six languages, an `osb` CLI, a first-party **MCP server**, six installable **agent skills**, and 26 runnable examples — nine of which target a *different* coding agent. It is **Alibaba's** project: the root commit is from an `@alibaba-inc.com` address, 1,160 of 2,400 commits (48.3%) come from that domain, and 1,674 files carry `Copyright <year> Alibaba Group Holding Ltd.` But it no longer *looks* like Alibaba's project, because in mid-2026 it was moved out of the `alibaba/` GitHub org into a members-less `opensandbox-group/`, given a vendor-neutral `GOVERNANCE.md`, a 19-proposal Kubernetes-style enhancement process, an OpenSSF Best Practices badge and a CNCF Landscape entry. **The de-branding is the story — and so is the CI job that will not let it finish.**

---

## 1. What it actually is (claims verified against source)

The README lists seven feature bullets. Verified one by one:

| README claim | Reality | Status |
|---|---|---|
| "SDKs, CLI, and MCP" | `sdks/sandbox/{python,javascript,go,kotlin,csharp}` + `sdks/code-interpreter/{python,javascript,csharp}` + Kotlin + `sdks/mcp/sandbox/python`; `cli/` = the `osb` CLI | ✅ **IMPLEMENTED** |
| "Sandbox Protocol" — extensible custom runtimes | `specs/` holds public OpenAPI contracts (incl. `specs/execd-api.yaml`), with `specs/AGENTS.md` declaring them the source of truth | ✅ **IMPLEMENTED** |
| "Sandbox Runtime" — Docker + K8s | `server/opensandbox_server/services/docker/` and `services/k8s/`; plus a full Go operator in `kubernetes/` (CRDs, controller, task-executor, Helm charts, Kind e2e) | ✅ **IMPLEMENTED** |
| "Sandbox Environments" — Command, Filesystem, Code Interpreter | `sandboxes/code-interpreter/` image; `components/execd/` = the in-sandbox execution daemon | ✅ **IMPLEMENTED** |
| "Network Policy" — ingress + per-sandbox egress | `components/ingress/`, `components/egress/` (Go sidecars; egress uses mitmproxy) | ✅ **IMPLEMENTED** |
| "Credential Vault" — inject secrets without exposing them | OSEP-0012 (76.6 KB), `status: implemented`; CLI skill + guide | ✅ **IMPLEMENTED** |
| "🏰 **Strong Isolation** — supports gVisor, Kata Containers, Firecracker microVM" | ⚠️ **See §5. This is configuration passthrough, not an isolation implementation.** | ⚠️ **OVERSTATED** |

**Scale (tracked files, stated basis).** 2,221 files / **804,531 total tracked lines**, of which **12,579 lines are lockfiles** (19 lockfiles). By area: `sdks/` 161,495 lines (802 files) · `components/` Go 81,912 · `kubernetes/` Go 45,379 · `server/opensandbox_server/` Python 25,254 · `server/tests/` 29,504 · `oseps/` 15,057 lines / 784,678 bytes.
⚠️ **Generated-code basis unresolved:** only 12 files under `sdks/` carry a "generated / do not edit" marker, so the 161,495-line SDK figure is *either* largely hand-written across six languages *or* generated without markers. **I could not settle which** — do not cite it as hand-written LOC.

**Tests.** **447 test files** across six languages: 236 Go (`_test.go`), 137 Python, 47 Kotlin/Java/C#, 27 JS/TS. `server/tests/` alone is 66 `test_*.py` files / 29,504 lines. A workflow agent computed a test-to-source ratio of **≈0.52**. There is a real e2e layer (`real-e2e.yml`, `tests/{go,python,javascript}`, Kind-based K8s e2e).

---

## 2. ⭐⭐⭐ THE HEADLINE — the de-branding that CI will not allow

### 2.1 The migration is a stated fact, not an inference

Commit **`e435df408f591528a580f3fbb6f118597f6f7f45`** (2026-07-06 18:37 +0800, PR **#1197**, merged by `ninan-nn`) has the body:

> **"Update repository links after GitHub org migration"**

It touched **24 files, +99 / −98**: README badges, `CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/config.yml`, three Helm `Chart.yaml`s, chart READMEs and `NOTES.txt`, K8s deployment docs, `sandboxes/code-interpreter/README{,_zh}.md`, `sdks/sandbox/go/README.md`, `server/TROUBLESHOOTING.md`, `docker-compose.example.yaml`, four example TOML configs, `specs/execd-api.yaml` — **and `server/opensandbox_server/startup_guard.py`** (an issue URL).

The diff shows the substitution directly: `github.com/alibaba/OpenSandbox` → `github.com/opensandbox-group/OpenSandbox`, and the Trendshift badge's alt text changing from `alibaba%2FOpenSandbox` to `opensandbox-group%2FOpenSandbox`.

⭐ **A bonus the mocked GitHub API cannot give me:** the pre-migration README carried a **hardcoded** star badge, `Stars-11.6k`, which this commit replaced with a live shields.io badge. So the repo's own git history contains a **dated star snapshot: ~11.6k on 2026-07-06.** With third-party reporting of ~7k within 72 hours of the 2026-03-03 launch and 14.3k page-stated today, that is a legitimate in-repo velocity anchor. *(Method note worth keeping: when the API is unavailable, a repo's own committed badge history is a dated metric source.)*

### 2.2 What the migration did not touch — and could not

The migration swept every surface a human reads. It did not touch **a single `go.mod`**. Verified: `git show --stat e435df40 | grep -c 'go.mod'` → **0**.

Present-tree state of all **10** Go modules:

| Declared module path | Count |
|---|---|
| `github.com/alibaba/OpenSandbox/...` (capital S) — `sdks/sandbox/go`, `sdks/sandbox/go/poolredis`, `kubernetes/` (as `sandbox-k8s`), `tests/go` | **5** |
| `github.com/alibaba/opensandbox/...` (lowercase) — `components/{execd,egress,ingress,internal,nodeagent}`, `examples/chrome` | **6** |
| `github.com/opensandbox-group/...` | **0** |

*(5 + 6 = 11 matches across 10 files: one module file references both forms.)* There are **797** in-tree references to `github.com/alibaba/` versus **87 files** mentioning `opensandbox-group`.

This is **not sloppiness — it is the cost of Go's design.** A Go module path *is* its identity; changing it breaks every downstream importer. So the rename stopped exactly where renaming becomes a breaking change.

But the consequence is real: **`README.md:90` still instructs `go get github.com/alibaba/OpenSandbox/sdks/sandbox/go`** — an install command that works only because GitHub permanently redirects the org they migrated away from. I verified by fetch that `github.com/alibaba/OpenSandbox` resolves and serves `opensandbox-group`'s content and star count, i.e. **a redirect**. ⚠️ *I could not verify from inside the clone whether the Go module proxy honours that redirect; treat "the `go get` line still works" as inferred from the HTTP redirect, not tested.*

And the split leaks into external registries too. The **OpenSSF Best Practices badge (project 12588) — passing at 100%** — still lists its Repository URL as **`https://github.com/alibaba/OpenSandbox`**.

### 2.3 🔴 The part a robot re-asserts on every pull request

`.github/workflows/verify-license.yml` — *"Verify License Headers"* — runs **`on: pull_request: branches: [main]`** and executes `scripts/verify-license.sh`. That script contains, at lines 35–36:

```bash
LICENSE_OWNER="Alibaba Group Holding Ltd."
LICENSE_REGEX="Copyright [0-9]{4} ${LICENSE_OWNER// / }"
```

It scans tracked files across 14 extensions (`go py sh kt kts java ts tsx js jsx toml html css sql tf`) plus `Dockerfile`, and **fails the build listing every violation.** Ignored: `LICENSE`, `NOTICE`, `docs/`, plus generated/mock Go files.

Which is why the header count is so clean: **1,674 files** carry `Alibaba Group Holding Ltd.` — 845 dated 2026, 528 dated 2025 in the sampled extensions; by extension: 678 `.py`, 624 `.go`, 112 `.kt`, 72 `.cs`, 62 `.ts`, 57 `.sh`, 17 `.toml`, 12 `.java`, 9 `.kts`, 5 `.yaml`, 4 `.mjs`, 3 `.c`. The only other holder found anywhere is a single `Copyright 2022.` outlier. *(Three files have a typo'd `Ltd..`)*

⭐⭐⭐ **So the corporate identity is not merely fossilized — it PROPAGATES. Every new file that any of the 119 contributors adds must assert Alibaba's copyright in order to merge.** The project moved out of the `alibaba/` org, wrote a `GOVERNANCE.md` that mentions Alibaba **zero times** (verified: `grep -ci alibaba GOVERNANCE.md` → 0), and simultaneously maintains a required status check that re-brands the codebase on every PR.

**That is not hypocrisy; it is a precise picture of what open-source vendor-neutrality can and cannot reach.** Documents are cheap to neutralize. Build gates, module paths, package coordinates and copyright headers are not — because those are the ones with downstream consumers.

### 2.4 The rest of the identity surface

| Surface | Identity it asserts |
|---|---|
| GitHub org (current) | `opensandbox-group` — **zero public members** |
| GitHub org (pre-July 2026) | `alibaba` |
| Go modules (10 files) | `github.com/alibaba/OpenSandbox` **and** `github.com/alibaba/opensandbox` — two case-distinct namespaces |
| Maven | `com.alibaba.opensandbox:sandbox` |
| npm | `@alibaba-group/opensandbox` |
| NuGet | `Alibaba.OpenSandbox` |
| PyPI | `opensandbox`, `opensandbox-cli`, `opensandbox-mcp`, `opensandbox-code-interpreter` — **the only un-branded coordinates** |
| Container images | `docker.io/opensandbox/*`, `ghcr.io/opensandbox-group/opensandbox/*`, **and** `sandbox-registry.cn-zhangjiakou.cr.aliyuncs.com/opensandbox/*` |
| Copyright (CI-enforced) | `Alibaba Group Holding Ltd.` |
| Docs site | `open-sandbox.ai` |
| Conduct contact | `conduct@opensandbox.io` |
| K8s API group | `sandbox.opensandbox.io/v1alpha1` |

⚠️ **A finding I nearly fabricated and killed by checking.** `opensandbox.io` appears **406** times versus `open-sandbox.ai`'s **9**, which looks like two rival websites. It is not: substantially all 406 are **Kubernetes API-group, annotation and label prefixes** (`sandbox.opensandbox.io/v1alpha1`, `opensandbox.io/id`, a reserved `opensandbox.io/` annotation prefix) — the standard K8s domain-shaped-identifier convention, plus one `api.opensandbox.io` example base URL. **There is no two-website defect. Do not cite one.**

---

## 3. ⭐⭐⭐ The agent-context layer — and the one commit that diagnosed and fixed drift together

### 3.1 The bridge: 6 `AGENTS.md`, 2 `CLAUDE.md`, 2 incompatible mechanisms

Six directories carry an `AGENTS.md` (28,282 bytes total):

| Path | Bytes | `CLAUDE.md` beside it? |
|---|---|---|
| `AGENTS.md` (root) | 7,414 | ✅ **85-byte prose stub** (mode `100644`) |
| `cli/AGENTS.md` | 5,136 | ❌ none |
| `kubernetes/AGENTS.md` | 7,671 | ❌ none |
| `sdks/AGENTS.md` | 3,816 | ❌ none |
| `server/AGENTS.md` | 2,081 | ✅ **9-byte symlink** (mode `120000`) |
| `specs/AGENTS.md` | 2,164 | ❌ none |

`git ls-files -s | grep '^120000'` returns **exactly one** symlink in the whole repository: `server/CLAUDE.md → AGENTS.md`.

The root stub, in full:

```
# OpenSandbox Claude Guide

See `AGENTS.md` for all rules, routing, and conventions.
```

⭐ **So OpenSandbox solves the same problem twice, two different ways, and puts the stronger mechanism in the weaker place.** Claude Code does not read `AGENTS.md` natively; both mechanisms bridge that gap and **neither can go stale** (the stub carries no content to drift). But they are not equivalent: the symlink *delivers the content*, while the stub costs the agent a second read and a hop it may not take. The symlink sits at `server/` — one subdirectory. **The root, the file Claude Code reads first, got the weaker one.**

### 3.2 ⭐⭐⭐ The commit that is the vault's own D22, diagnosed and structurally fixed in one PR

`server/CLAUDE.md` was introduced by **`fb5a2c911f039b5a17c167c21596c2944972b16e`** (2026-06-18 17:07 +0800, by `epha` = `@Pangjiping`), a squash of PR **#1100**. Its body, verbatim:

```
docs(server): streamline AGENTS.md and DEVELOPMENT.md (#1100)

* docs(server): streamline AGENTS.md and DEVELOPMENT.md

Remove generic boilerplate (IDE config, naming conventions, debugging/profiling,
contributing workflow), outdated content (flat project structure tree, "Planned"
K8s roadmap, stale internal implementation details), and duplicated information.

Recommend bridge network mode over host mode in examples and docs.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* docs(server): add CLAUDE.md symlink to AGENTS.md

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 4.6 <noreply@anthropic.com>
```

⭐⭐⭐ **Read those two bullets together.** Bullet one *deletes* stale agent-facing prose — by name: *"outdated content … 'Planned' K8s roadmap, stale internal implementation details."* Bullet two *makes that class of staleness impossible* for the harness-specific filename, by replacing a copy with a symlink. **The diagnosis and the structural fix, in one PR — and `Claude Opus 4.6` is co-author on both.**

This is **v241's D22** (*agent-facing prose goes stale first*) and **v243's symlink answer** occurring together, in one commit, in a stranger's repository. It is the strongest single artifact this run has produced for the vault's own problem.

⚠️ **Chronology, stated honestly.** `AGENTS.md` first appeared **2025-12-24** (`bf317b78`, 贾岛, *"docs: add repository guidelines"*) — only **41 days** after the root commit and well before the public launch. It was revised 2026-05-07 (`470f0c5f`, 贾岛, *"Update agent guidance docs"*). The `osb skills` command landed **2026-03-26**. The symlink came **2026-06-18**. So: **the agent-context layer is nearly as old as the project, but the symlink is a ~3-month retrofit onto it.** A workflow critic framed the whole layer as "a retrofit after the platform existed" — that is **wrong for `AGENTS.md`** (it predates the launch) and **right for the symlink**.

### 3.3 The root `AGENTS.md` is a genuinely good router — with a source-of-truth table

It is not a rules dump. It opens: *"Use this file as the root router for the monorepo. **Prefer the nearest `AGENTS.md` in the directory tree** for task-specific instructions."* Then a repository map, then eleven explicit routing rules (`For specs/**, or API contract … read specs/AGENTS.md`), including a fallback for unmapped areas: *"use the nearest `README.md`, `DEVELOPMENT.md`, and CI workflow as the next source of truth."*

⭐ **The part worth stealing is a "Content ownership — single source of truth" table** — seven content types, each with an owning location and a rule (user docs → `docs/`; publishable package READMEs → package dir; OSEPs → `oseps/`, with *"`docs/community/oseps.md` only indexes GitHub proposals"*). Plus guardrails in **Always / Ask first / Never** form, of which two lines are directly transferable:

- Always: *"Keep spec, implementation, SDKs, docs, examples, config, and CLI behavior aligned when user-visible behavior changes."*
- Ask first: *"**Intentional drift between a public contract and its implementation**"* — drift as a thing you must get *permission* for.
- Never: *"Edit generated output as the only fix."*

🔴 **And nothing verifies any of it.** `.pre-commit-config.yaml` holds only generic hooks (trailing-whitespace, check-yaml, detect-private-key). No CI job and no script references `AGENTS.md` or `CLAUDE.md`. The doctrine is good; the enforcement is absent — **exactly the v243 shape.** The irony is sharp: the one documentation-adjacent thing they *do* enforce in CI is the copyright header (§2.3).

### 3.4 ⭐⭐ The `osb skills` installer — six harnesses, rendered from one source

`cli/src/opensandbox_cli/skills/` holds **six** skills (~43.9 KB total), and `skills/troubleshoot-sandbox/SKILL.md` sits at root. `cli/pyproject.toml:76` ships `src/opensandbox_cli/skills/**` as package data, so **`pip install opensandbox-cli` puts the skills on disk**, and `osb skills install --target <t>` writes them into the user's harness. `cli/src/opensandbox_cli/commands/skills.py` declares `_TARGETS`:

| Target | Label | Destination (project / user) | Mode |
|---|---|---|---|
| `claude` | Claude Code | `.claude/skills` / `~/.claude/skills` | copy |
| `cursor` | Cursor | `.cursor/rules` / `~/.cursor/rules` | copy |
| `codex` | Codex | `.codex/skills/{slug}/SKILL.md` / `~/.codex/...` | copy |
| `copilot` | GitHub Copilot | `.github/copilot-instructions.md` | **append** |
| `windsurf` | Windsurf | `.windsurfrules` | **append** |
| `cline` | Cline | `.clinerules` | **append** |

⭐ It distinguishes **copy** (harnesses with a skills *directory*) from **append** (harnesses with a single instruction *file*), and a `render_skill_for_target()` function emits each target's native format from the one canonical Markdown source. That is the **Pattern #84 84c "CLI-generates-native-formats-from-canonical-source"** mechanism (v76 `agent-skills-standard`, v75 `impeccable`), shipped by an infrastructure vendor.

The skills themselves are well-built — real trigger-shaped frontmatter and an anti-generic-advice doctrine:

> `name: sandbox-lifecycle` … `description: … Trigger when users want help provisioning a sandbox, choosing create flags, checking runtime state…`
> Body: *"Use OpenSandbox lifecycle commands directly **instead of giving generic container advice**. Prefer a verified lifecycle flow over isolated commands."*

The six cover: `sandbox-lifecycle`, `command-execution`, `file-operations`, `network-egress`, `credential-vault`, `sandbox-troubleshooting`.

⭐⭐ **The contrast writes itself.** The *hard* version of the drift problem — one canonical skill, six harnesses, two different file layouts — they solved **with code, from a single source**. The *easy* version — one file, two names — they solved **by hand, twice, differently.** (v243 found the mirror image: symlinked so two files could not diverge, then hand-copied a paragraph into three files where it diverged immediately. **Two independent projects, opposite errors, same root cause: whatever a machine does not generate, humans will let diverge.**)

### 3.5 Four ways in, and Claude Code is one of nine

OpenSandbox exposes itself to agents four ways: the **MCP server** (`sdks/mcp/sandbox/python` → `pip install opensandbox-mcp`; docs describe it as exposing the Python SDK "as MCP tools for Claude Code, Cursor, and other MCP-capable clients", with stdio *and* http configs), the **six installable skills**, **six-language SDKs**, and the **`osb` CLI**. That is a **Pattern #18 sub-archetype B1-MCP** instance and the most complete agent-facing surface an infrastructure product has presented in this corpus.

`examples/` holds **26** entries, of which **nine target a distinct coding agent** — `claude-code`, `codex-cli`, `gemini-cli`, `kimi-cli`, `qwen-code`, `opencode`, `openclaw`, `nullclaw`, plus `deep-agents` — with frameworks alongside (`langgraph`, `google-adk`, `agent-sandbox`, `harbor-evaluation`) and environments (`chrome`, `playwright`, `desktop`, `vscode`, `windows`, `aks-kata`). The `claude-code` example is three files (`README.md`, `main.py`, `screenshot.jpg`) that run the Claude CLI *inside* a sandbox. **28 files / 116 hits mention Claude or Anthropic.**

⭐ **This is harness-agnostic infrastructure that names Claude Code first.** Unlike every DSH-chain subject (v235–v242), OpenSandbox is not a Claude competitor or a Claude wrapper — it is the *floor* all nine agents stand on. `aks-kata` (Azure + Kata) also explains the lone `microsoft.com` contributor's 24 commits.

---

## 4. ⭐⭐ Provenance — 340 trailers, three harnesses, three conventions, and a collapse

**All counts `HEAD` / 2,400 commits unless marked.**

| Signal | Commits | Trailer lines | `--all` |
|---|---|---|---|
| `Co-Authored-By: Claude` (`noreply@anthropic.com`) | **197** | **340** | 228 commits |
| `Made-with: Cursor` | 37 | 37 | — |
| `Co-authored-by: Cursor <cursoragent@cursor.com>` | 9 | 9 | — |
| `Copilot Autofix powered by AI` (bot) | 18 | 20 | — |
| `copilot-swe-agent[bot]` | 1 | 1 | 31 (all Copilot) |
| Codex / Devin / Windsurf / Cline trailers | **0** | 0 | — |
| `Claude-Session:` URLs | **0** | 0 | — |

**Claude model-version census of the 340 lines** — Opus 4.6 **162** (103 + 38 `(1M context)` + 19 lowercase + 2) · Opus 4.7 **130** (100 + 26 lowercase + 4 `1M`) · Opus 4.8 **23** · Opus 4.5 **5** · Sonnet 4.6 **5** · Sonnet 4.5 **1** · Opus 5 **1** · Fable 5 **1** · `Claude` unversioned **11** · `Claude Code` **1**. → **329 of 340 (96.8%) name a model version**; **49 (14.4%) name `(1M context)`**; **49 lines use the lowercase `Co-authored-by:` spelling**, so two trailer spellings coexist. Max in one commit: **28** (`ed3aa1c9`), then 17, 9, 7, 6.

**D26 applies, and cuts the other way from v243.** 197 commits carry 340 lines — a mean of **1.73**, not v243's 5.48 — because this repo is **merge-commit-dominant** (726 merge commits; only 253 subjects end in `(#NNNN)`; highest PR referenced **#1568**), so individual commits survive and trailers are not aggregated. ⭐ **Same metric, different merge strategy, different meaning: the commits↔lines gap measures how much a repo squashes.** (PR #1100 in §3.2 is a squash — three bullets, three trailers, one commit — which is where the excess comes from.)

⭐ **Three harnesses, three conventions.** Claude's `Co-Authored-By:` is a **Claude Code default**. `Made-with: Cursor` is Cursor's own, non-standard trailer. Copilot's presence is **almost entirely a bot** — `Copilot Autofix powered by AI` via `github-advanced-security[bot]` and `github-code-quality[bot]` — i.e. *automated security fixes*, not a human coding with Copilet. So on the human-authored axis, Claude leads Cursor ~197 : ~46 and Copilot ~197 : 1.

⚠️ **An error I caught in my own first pass:** a naive `git log --grep=cursor -i` returns **51**, but ~5 of those match the *word* "cursor" in code prose (`cursor-based log polling`, `tail cursor`, `EXECD-ISOLATED-TAIL-CURSOR`). **Only the trailer forms are provenance.** Grep the trailer, not the word.

🔴 **The collapse.** Claude-trailered commits by month: 2025-11 **1** · 2026-02 **3** · 2026-03 **33** · 2026-04 **14** · 2026-05 **35** · **2026-06 91** · 2026-07 **11** · 2026-08 **9**. Total commits by month: 2025-12 142 · 01 184 · 02 214 · **03 401** · 04 305 · 05 191 · 06 256 · **07 422** · 08 284.
⭐ **June was the Claude peak (91 of 256 commits = 36%). July was the repo's busiest month ever (422 commits) and carried 11.** Attribution fell ~88% while activity rose ~65%. ⚠️ **I cannot tell whether they stopped using Claude or stopped emitting the trailer** — a trailer is a *setting*, not a measurement. **Do not present this as reduced usage.** It is a documented discontinuity in the *record*, and it is a live caution about how much any trailer census can carry.

**Branch-name provenance** (from 47 parseable merge subjects): `bump/` 19, `fix/` 7, `feat/` 6, `dependabot/` 5, `docs/` 2, **`codex/` 2**, `refactor/` 1, `ci/` 1, **`agent/` 1**. The org migration itself landed on **`codex/update-repo-links`** — so the commit that de-branded the project was written on a branch named after a *different vendor's* agent.

**Human shape.** Root commit **`1914b7d526754f1b1ccd852aa9548e5501e6c8e5`**, 2025-11-13 17:07:04 +0800, **贾岛 `<wenxiang.jin@alibaba-inc.com>`**, *"Add Apache License 2.0"* — **one** root commit, no history rewrite, and (unlike v241) the git metadata describes the same project as the tree. Age ~**279 days** to HEAD; **119 distinct author emails** on `HEAD`. Domain census (commits): **alibaba-inc.com 1,160** · users.noreply.github.com 768 · **zju.edu.cn 108** (Zhejiang University) · gmail 98 · 163.com 56 · qq.com 49 · **mercadona.com 28** (the Spanish grocery chain) · **microsoft.com 24** · icloud 23 · didiglobal 12 · m.fudan.edu.cn 8 · sangfor 6 · jd.com 5 · tencent.com 1. By *distinct authors*: 31 noreply, 31 gmail, **12 alibaba-inc.com**, 7 163.com, 6 qq.com. **173 tags**, all component-scoped (`server/v0.2.2` latest).

⚠️ **A workflow critic reported "3 Claude trailer commits / 0.125%" and concluded the project is "not Claude-Code-native."** It sampled the **last 50 commits** and blamed a "blobless clone limitation" that does not exist — commit *messages* are fully present in a blobless clone; only file blobs are omitted. The true figure is **197 commits / 8.2%**, a **65× error**, and it would have inverted this section. It also reported "5 commits from alibaba-inc.com" (actual: 1,160) and an 18-item OSEP tally (actual: 19). **This is v241's D21 and v243's D27 recurring: a verifier checked a real question against the wrong population, then trusted a limitation it had invented.**

---

## 5. ⚠️ "Strong Isolation" — passthrough, not implementation (and a real trade-off inside it)

README:33 claims *"Supports secure container runtimes like gVisor, Kata Containers, and Firecracker microVM for enhanced isolation between sandbox workloads and the host."*

Grepping the whole tree for `gvisor|runsc|kata|firecracker` across `.py .go .yaml .toml`, the hits land **only** in: the README, `server/configuration.md`, `server/opensandbox_server/config.py` (a `SecureRuntimeConfig` model + validation), and **tests**. There is **no gVisor, Kata or Firecracker integration code**. What exists is a `secure_runtime` config block carrying `type` (`""` / `gvisor` / `kata` / `firecracker`), a `docker_runtime` name, and a `k8s_runtime_class` that becomes the pod's `runtimeClassName` (`config.py:808–813`: *"When specified, pods will have runtimeClassName set to this value"*).

**That is the architecturally correct way to use these runtimes** — you install gVisor or Kata on your nodes and select them per-workload. But it means the claim belongs to *Kubernetes*, not to OpenSandbox: **OpenSandbox does not isolate; it lets you tell your cluster which isolator to use, and the operator must install it.** State it that way.

⭐ There *is* real engineering here, and it is more interesting than the marketing: a **compatibility matrix enforced in validators.** From `server/tests/test_validators.py:702–745`, `ensure_egress_runtime_compatible()`:

- `test_rejects_gvisor_with_network_policy` → **gVisor + their egress NetworkPolicy is REJECTED** (the error message names "gVisor")
- `test_allows_kata_with_network_policy` → **Kata + egress policy is allowed**
- `firecracker` requires `k8s_runtime_class` and is **Kubernetes-only** (`configuration.md:273,280`); `docker` cannot use it

⭐⭐ **So choosing their strongest isolation costs you their egress control.** That is a genuine, non-obvious, security-relevant trade-off, encoded in code and tests rather than hidden — and it is the sort of thing the README's single 🏰 bullet actively obscures.

---

## 6. Security posture — the corpus's first positive counter-example to the broken-auth triad

### 6.1 🔴 → ⭐ The unauthenticated default, and the gate I initially missed

The lifecycle server defaults to binding **`0.0.0.0`** (`config.py:473`) and `server.api_key` defaults to **`None`** (`config.py:546–548`). And `middleware/auth.py:85–87` reads:

```python
# If no API keys configured AND no tenant provider → skip auth
if not self._is_multi_tenant and not self.valid_api_keys:
    return await call_next(request)
```

My first framing was "auth fails open" — **that framing was wrong and I withdraw it.** `server/opensandbox_server/startup_guard.py` implements `api_key_confirm()`, and the server **refuses to start** without an explicit acknowledgment:

1. `OPENSANDBOX_INSECURE_SERVER=YES` → proceeds, logging a warning;
2. else, on an interactive TTY → an **ANSI-red** prompt demanding the exact string `YES`, with a **30-second timeout that aborts**, and a link to tracking issue **#750**;
3. else (non-interactive, no env var) → `RuntimeError: "Startup blocked: server.api_key is empty in non-interactive mode."`

⭐⭐ **This is an informed-consent gate, and it fails CLOSED on timeout.** It is documented in four places (`server/configuration.md:67`, `docs/components/server.md:121`, `docs/getting-started/configuration.md:45,77`) and in four example configs **including Chinese-language ones** (`example.config.zh.toml`, `example.config.k8s.zh.toml`). Their own e2e scripts and `server-test.yml` set the env var, which is the correct use.

⭐⭐⭐ **This is the sharpest positive contrast in the corpus.** The vault recorded a *broken-authentication triad* at **v231** (`require_auth:false` + wildcard CORS while holding live sessions) and **v232** (auth fails open, `0.0.0.0`, wildcard CORS). OpenSandbox ships the same convenience mode and **gates it behind explicit, timed, logged, bilingually-documented consent.** It is the pattern those two subjects should have had — and it is directly liftable.

### 6.2 🔴 The finding that survives: the proxy-path bypass

`middleware/auth.py:82–83`, evaluated **before** the api-key check:

```python
if self._is_proxy_path(request.url.path) and not self._is_multi_tenant:
    return await call_next(request)
```

with `_PROXY_PATH_RE = re.compile(r"^(/v1)?/sandboxes/[^/]+/proxy/\d+(/|$)")` and an explicit `".." in path` rejection. `EXEMPT_PATHS = ["/health", "/version", "/docs", "/redoc", "/openapi.json"]`.

🔴 **So in single-tenant mode, requests to a sandbox's proxy route skip authentication *even when an API key IS configured*.** The operator who does the right thing still has an unauthenticated path to every sandbox's exposed ports, gated only on knowing a sandbox ID.

⚠️ **Scope this honestly.** The regex is tight (numeric port, traversal-rejected), and OSEP-0011 *"Secure Access Endpoint"* (`status: implemented`) plus the `[ingress.secure_access]` signed-route-token machinery in `config.py:232–358` exist precisely to protect sandbox endpoints — so the intent is that the *proxy* layer carries its own token scheme rather than the global API key. **I did not verify end-to-end whether a `SecureAccessToken` is required on that route when `secure_access` is unconfigured**, and that is the question that decides whether this is a design boundary or a hole. **Flagged, not concluded.** It is the first thing to test in any pilot, and the sharpest thing to report upstream.

⭐ **The shape is still worth stating:** the consent gate protects the operator who configured *nothing*; a separate code path un-protects the operator who configured *something*.

### 6.3 What is strong

- **`SECURITY.md`** is well above corpus norm: GitHub private vulnerability reporting; a 48-hour acknowledgment commitment; **release signing via GitHub/Sigstore attestations, cosign keyless container signatures and Maven Central signatures**; and a **Cryptographic Key Length Policy** aligned to OpenSSF `crypto_keylength` (≥112-bit symmetric, ≥2048 RSA, ≥224 EC) with **named enforcement points** (Go SDK transport cert validation; K8s controller webhook/metrics TLS) and named escape hatches (`AllowWeakServerCertKeyLengths`, `--allow-weak-tls-keylengths`).
- **OpenSSF Best Practices #12588 = passing, 100%** — Basics 13/13, Change Control 9/9, Reporting 8/8, Quality 13/13, Security 16/16 (externally verified by fetch).
- Images published to three registries, **cosign keyless-signed with provenance attestations**, with a documented verification guide and "pin by digest" advice.
- **Supply chain: 19 lockfiles; ZERO npm lifecycle scripts across all 5 `package.json` files** (no `postinstall`/`preinstall`/`prepare`/`prepublish`). Contrast v242, which needed a 5-allow/3-deny policy because it *had* scripts.
- **No mirror substitution in any lockfile.** ⚠️ **But two Dockerfiles do rewrite upstreams:** `kubernetes/Dockerfile.image-committer:19,38` runs `sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'`, and `:25` plus `kubernetes/Dockerfile:36` set `GOPROXY=https://goproxy.cn,direct`. **Scope: 2 files, the image-build path only — dependency *resolution* stays canonical.** Not the v240-class lockfile-mirror defect, but if you build their K8s images yourself, your Alpine packages and Go modules arrive through Alibaba/China mirrors — a trust boundary worth knowing about in a security product.

### 6.4 ⭐ D28 — an absent config file is not an absent check

**24** workflows in `.github/workflows/`, **11** triggered on `pull_request`. Grepping all of them for `codeql|trivy|gosec|bandit|semgrep|dependency-review|scorecard|snyk` returns **zero hits**, and there is **no `.github/dependabot.yml`**.

⚠️ **Concluding "no security scanning, no dependabot" would be wrong** — and the provenance record proves it: **18 `Copilot Autofix powered by AI` commits** via `github-advanced-security[bot]` / `github-code-quality[bot]`, and **5 `dependabot/` merge branches**. Both are configured through **GitHub's default setup / repository settings, which leave no file in the tree.**

⭐ **New rule → D28: a tree-only audit systematically under-reports a repo's automated security posture, because GitHub code scanning and Dependabot security updates can be enabled entirely in settings. The detector is the bot's commit trailers, not the workflow directory.** (This is the third consecutive ship to sharpen the same class of method error: **D26** what a body-grep counts, **D27** which refs it counts over, **D28** whether the config is in the tree at all.)

Their in-tree CI is nonetheless substantive: per-component test workflows (`server-test`, `execd-test`, `egress-test`, `ingress-test`, `nodeagent-test`, `kubernetes-test`, `sdk-tests`), `real-e2e.yml`, `kubernetes-nightly-build.yml`, seven `publish-*` workflows, `release-preflight.yml`, `pr-label-check.yml` and **`verify-license.yml`** (§2.3).

---

## 7. ⭐⭐ Governance — vendor-neutral in every document, vendor-specific in the build

**19 OSEPs** (OpenSandbox Enhancement Proposals), **15,057 lines / 784,678 bytes**, with `oseps/README.md`, `oseps/CONTRIBUTING.md`, `osep-template.md.template` and `init-osep.sh`. Statuses use **Kubernetes KEP vocabulary exactly** (`provisional` → `implementable` → `implementing` → `implemented`), and it is a *working* process, not theatre:

| Status | Count | OSEPs |
|---|---|---|
| **implemented** | **10** | 0001 FQDN egress · 0002 kubernetes-sigs/agent-sandbox · 0004 secure container runtime · 0005 client-side pool · 0008 pause/resume rootfs snapshot · 0009 auto-renew on ingress · 0010 OpenTelemetry · 0011 secure access endpoint · 0012 credential vault · 0014 multi-tenancy |
| implementing | 5 | 0003 volumes · 0013 isolated execution API · 0017 resilient SDK transport · 0018 execd as sandbox init · 0019 node-agent collection |
| draft | 2 | 0015 pod snapshot (94.0 KB) · 0016 unified umbrella release governance |
| implementable | 1 | 0006 developer console |
| provisional | 1 | 0007 fast sandbox runtime (80.3 KB) |

The largest are 0015 (94.0 KB), 0007 (80.3 KB), 0012 (76.6 KB), 0019 (67.8 KB), 0018 (63.1 KB), 0001 (53.7 KB). ⚠️ A workflow critic computed a design-to-code ratio and concluded *"NOT a documentation-first project"* — ~785 KB of proposals against ~271 K LOC of source. Fair; but 785 KB of ratified design text on a **279-day-old** repo is still far denser process than this corpus normally sees, and **10 of 19 shipped** is the number that makes it credible.

⭐ **OSEP-0002 verifies a real standards bet.** `kubernetes-sigs/agent-sandbox` — the Kubernetes SIG project launched November 2025 — is supported for real, not aspirationally: `status: implemented` (authored `@jwx0925`, 2026-01-23), `AgentSandboxRuntimeConfig` in `config.py:685–698`, a `kubernetes.workload_provider = "agent-sandbox"` setting wired through `cli.py:257–258`, `examples/agent-sandbox/`, and two test files (`test_agent_sandbox_provider.py`, `test_agent_sandbox_template.py`). **OpenSandbox is aligned to an emerging Kubernetes standard it did not author** — which is the same vendor-neutrality play as the org migration.

**But `GOVERNANCE.md` (9.5 KB) never names the company.** It defines Maintainers and Project Maintainers, subsystem ownership, rough consensus, escalation and a simple-majority Project-Maintainer vote with recusal for conflicts of interest. It mentions **Alibaba zero times.** And it contains this fallback:

> *"Until a dedicated `MAINTAINERS.md` is added, the fallback `*` owners in [CODEOWNERS] are the Project Maintainers."*

There is **no `MAINTAINERS.md`** (verified). So the de-facto Project Maintainers are `.github/CODEOWNERS`' default owners — **`@jwx0925 @hittyt @Pangjiping @ninan-nn`** — with eight handles total across the file (`+ @Generalwin @Spground @fengcone @kevinlynx`), and `/oseps/` owned by all eight.

⭐⭐ **Put §2.3 and §7 side by side and the whole subject resolves into one sentence: the document that decides who owns the project does not name Alibaba, and the CI job that must pass on every pull request will not let any file omit it.**

`CONTRIBUTING.md` is 20.0 KB. There is **no AI-authorship disclosure requirement anywhere** — which makes the 340 Claude trailers, like v243's 905, a **left-on default rather than a policy.** *(Consistent with the July collapse: nobody was ever required to emit them.)*

---

## 8. Documentation integrity — better than the corpus norm, with two real gaps

**In their favour** (the fair-direction checks):

- ⭐ **`cli/AGENTS.md` is CLEAN.** A workflow critic flagged it as *"67 days stale."* I tested every path it names — `src/opensandbox_cli/{client,main,output,skill_registry}.py`, `commands/`, `skills/`, `tests/test_{cli_help,commands,skills}.py`, `../sdks/AGENTS.md`, `../specs/AGENTS.md` — and **all 11 exist.** ⭐ **`mtime` is not drift. A file that has not changed in 67 days because it is still correct is not stale** — and calling it stale is the same category error as calling an unchanged doc fresh. **The critic's claim is REFUTED.**
- The docs site is a static VitePress config (`docs/.vitepress/config.mts`) with *"no build-time code generation"*, **72 markdown files**, a declared directory taxonomy, mandatory YAML frontmatter (`title` + `description`), an images convention, and a hard gate in the root `AGENTS.md`: *"`cd docs && pnpm docs:build` — must complete with zero errors."*

**The two real gaps:**

- ⭐ **A v240 inventory-rule instance, live.** Of 71 non-README docs, **11 are unreferenced anywhere in `config.mts`** — but **9 of those are `index.md` section landing pages**, which VitePress routes by directory. The genuinely unreachable content pages are **two**: **`docs/examples/deep-agents.md`** and **`docs/components/egress-mitmproxy-sse-truncation.md`**. Both exist, both are real content, neither has a nav path. ⚠️ **Cite two, not eleven** — the nine indexes are not a defect, and reporting 11 would be the kind of inflation this vault exists to catch. That `deep-agents.md` is an *agent-integration* page makes it the more interesting of the two.
- ⚠️ **OSEP-0016 is `draft` while the practice has already run ahead of it.** *"Unified Umbrella Release Governance"* (created 2026-07-21, `@Pangjiping`, 38.7 KB) proposes unified versioning and an umbrella cadence — and **173 component-scoped tags already exist** (`server/v0.2.2` latest), with **no BOM file and no `releases/` directory** (verified absent). This is the *inverse* of ordinary drift: not documentation over-claiming, but a governance spec **trailing** a practice that is already shipping. Worth watching, not a defect.
- ⚠️ Three files carry a typo'd `Copyright 2026 Alibaba Group Holding Ltd..` (double period) — cosmetic, and it passes the regex.

---

## 9. Prior art and the mint question

**Established, with dated sources** (from web research; ⚠️ third-party, not in-repo):

| Project | First release | License | Self-hostable OSS? |
|---|---|---|---|
| **Kata Containers** | Dec 2017 | Apache-2.0 | ✅ |
| **gVisor** (Google) | May 2018 | Apache-2.0 | ✅ |
| **Firecracker** (AWS) | Nov 2018 | Apache-2.0 | ✅ |
| **E2B** | 2023 | proprietary managed + partial OSS | ⚠️ partial |
| **Daytona** | pre-2026 | AGPL-3.0 → **closed source June 2026** | ❌ *no longer* |
| **kubernetes-sigs/agent-sandbox** | Nov 2025 (KubeCon Atlanta) | Apache-2.0 | ✅ |
| **OpenSandbox** | **public 2026-03-03** (root commit 2025-11-13) | Apache-2.0 | ✅ |

**NOT world-first, on four grounds.** (1) The isolation substrate predates it by 6–8 years, and OpenSandbox **delegates** to it rather than implementing it (§5). (2) E2B (2023) and Daytona precede it as agent-sandbox products. (3) `kubernetes-sigs/agent-sandbox` defined the Kubernetes-native shape **three months before** OpenSandbox's public launch, and OpenSandbox **supports** that standard (OSEP-0002) rather than setting it. (4) Anthropic ships first-party sandboxing for Claude Code, and OpenAI/Google ship hosted code execution.

⭐ **But two facts reframe its position.** **Daytona went closed-source in June 2026** — so the leading open-source self-hostable rival exited the category two months before this analysis, not because OpenSandbox won but because the incumbent left. And ~7k stars within 72 hours of launch (third-party sourced) → 11.6k on 2026-07-06 (in-repo badge, §2.1) → 14.3k page-stated is real, sustained traction.

⚠️ **The "multi-language SDKs from day one" novelty claim in the press is a *feature* claim, not a capability first, and the comparison to E2B's launch SDK support is unverified.** Do not repeat it as a first.

**Corpus position — verified by my own grep, not delegated.** Searching `_state/03c-projects-v61-v183.md` and `_patterns/06-library-vocab-registry.md`: **E2B appears 14 + 10 times, and every occurrence is as a dependency or substrate *inside another subject***, never as a subject. Sandboxes have appeared as: open-lovable v224's live preview (E2B), Strix v190's Kali sandbox, grok-build v215's worktrees, DSH v235's sandbox plugin seam, ClawWork v233's harness. **No §C standalone describes the sandbox/code-execution layer itself.** There is exactly one `micro-VM` mention in the entire corpus.

⭐⭐ **So OpenSandbox is the corpus's FIRST subject that IS the execution substrate** — the compute sibling of a family the corpus has minted repeatedly: browser (`browser-use` v41), iOS simulator (`serve-sim` v183), web/social reach (`Agent-Reach` v174), Office documents (`OfficeCLI` v206), stealth browser (`camofox` v179), database (`tabularis` v212). Those are all *capability layers for agents*, and each minted. **The one an agent needs most — somewhere safe to run code — was missing.**

→ **The mint recommendation, the ruling, and its counter-argument are in the Verdict document.** It is not decided here.

---

## 10. Non-claims — what this analysis does NOT assert

- ❌ **NOT world-first** at sandboxing, isolation, or agent code execution (§9).
- ❌ **NOT a Pattern #52 velocity claim.** Stars/forks are page-stated; the GitHub API is mocked (§37.4). The 11.6k badge anchor is in-repo and dated; the "7k in 72 hours" figure is third-party.
- ❌ **Do NOT cite "340 Claude-co-authored commits."** It is **197 commits / 340 trailer LINES** (§4, D26).
- ❌ **Do NOT cite any git count without its ref population.** `HEAD` and `--all` differ by 145 commits (§4, D27).
- ❌ **Do NOT say OpenSandbox implements gVisor/Kata/Firecracker isolation.** It passes a `runtimeClassName` through; you install the runtime (§5).
- ❌ **Do NOT say "auth fails open."** Withdrawn. There is a real, fail-closed informed-consent startup gate (§6.1).
- ❌ **Do NOT report the proxy-path bypass as a confirmed vulnerability.** The `secure_access` token layer may cover it; I did not verify end to end (§6.2).
- ❌ **Do NOT claim "no security scanning / no dependabot."** Both run via GitHub settings, invisible in the tree (§6.4, D28).
- ❌ **Do NOT claim two rival websites.** `opensandbox.io` is the K8s API group (§2.4).
- ❌ **Do NOT cite "11 unlisted docs."** Two content pages; nine are section indexes (§8).
- ❌ **Do NOT claim the July Claude-trailer collapse means reduced Claude usage.** A trailer is a setting (§4).
- ❌ **Do NOT claim `cli/AGENTS.md` is stale.** All 11 paths it names exist (§8).
- ❌ **Not verified:** whether the Go module proxy honours the `alibaba/` → `opensandbox-group/` redirect; the generated-vs-hand-written split of the 161,495 SDK lines; whether the MCP server has real downstream consumers; that `opensandbox-group` is a legal entity distinct from Alibaba (no evidence found either way).

---

## 11. Error ledger — 9 caught, 4 mine

| # | Error | Whose | Correction |
|---|---|---|---|
| 1 | "Auth fails open" | **mine** | A real fail-closed consent gate exists (`startup_guard.py`) — framing **withdrawn** (§6.1) |
| 2 | "Alibaba affiliation is concealed" | **mine** | It is in 1,674 copyright headers and every install coordinate; the gap is the **org page**, not the substance — this **exonerated** the project (§2) |
| 3 | 51 "Cursor" commits | **mine** | ~46 trailer lines; ~5 were the word "cursor" in code prose (§4) |
| 4 | "Two rival websites" | **mine (avoided)** | `opensandbox.io` is the K8s API group — killed before it was written (§2.4) |
| 5 | "3 Claude trailers / 0.125% / not Claude-Code-native" | critic | **197 commits / 340 lines / 8.2%** — a 65× error from sampling 50 commits and inventing a blobless limitation (§4) |
| 6 | "5 commits from alibaba-inc.com" | critic | **1,160** commits, 12 distinct authors (§4) |
| 7 | "8 implemented / 18 OSEPs" | critic | **10 implemented / 19 total** (§7) |
| 8 | "`cli/AGENTS.md` 67 days stale" | critic | **REFUTED** — all 11 named paths exist; `mtime` ≠ drift (§8) |
| 9 | "11 unlisted docs" | lens | **2** content pages; 9 are section indexes (§8) |

**Workflow:** 23 agents (7 map → 14 adversarial verifiers → prior-art → completeness critic), **23/23 completed, 0 errors, 1 empty result** (the `sdks-cli-integrations` lens failed to call `StructuredOutput`; its surface was covered by hand), **~2.40M subagent tokens, 657 tool uses, 758s.** Verdicts: **10 CONFIRMED, 4 PARTIALLY_CORRECT, 0 REFUTED** — a cleaner verifier run than v243's (which returned two false REFUTEDs). ⭐ `Workflow` now **stable across six consecutive ships.** Every headline finding in this document was hand-verified by me directly, per the vault's standing rule.

---

## 12. New method rules

- **⭐ D28 — an absent config file is not an absent check.** GitHub code scanning and Dependabot security updates can be enabled entirely in repository settings, leaving nothing in the tree. A workflow-directory grep therefore *under*-reports automated security posture; the detector is the bot's commit trailers. Completes the trio: **D26** (what a body-grep counts), **D27** (which refs it counts over), **D28** (whether the config is in the tree at all).
- **⭐ D29 — `mtime` is not drift; test the claims, not the date.** A file unchanged for 67 days because it is still accurate is not stale. Staleness is *content disagreeing with reality* — check every path and command a doc names. (Derived from refuting the critic's `cli/AGENTS.md` claim; this is the discipline that makes the vault's own `verify-vault-docs` meaningful rather than a recency alarm.)
- **⭐ D30 — when the API is mocked, read the repo's own committed badges.** A hardcoded `Stars-11.6k` badge replaced in a dated commit gave a verifiable dated metric that §37.4 otherwise forbids. Committed badge history is an in-repo metrics source.
- **⭐ D26 extended — the commits↔trailer-lines gap measures merge strategy.** v243: 165 commits / 905 lines (mean 5.48, squash-dominant). v244: 197 / 340 (mean 1.73, merge-commit-dominant). **Same metric, different meaning; report the ratio and the strategy together.**

*Analysis by Claude (Opus 5) for Storm Bear · v244 · 2026-08-19 · source-cloned twice, all headline claims hand-verified.*
