# (C) AI-Infra-Guard — Deep Dive

**Subject:** `Tencent/AI-Infra-Guard` ("A.I.G") — AI Red Teaming Platform by **Tencent Zhuque Lab** (腾讯朱雀实验室)
**Wiki:** v276 · **Date:** 2026-08-25 · **Licence:** Apache-2.0 (+ a mandatory-attribution rider in `NOTICE`)
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO NEW MINT** — §C row **C26 N=1 → N=2** (recorded, not self-promoted)

---

## 0. Source verification

Two independent clones, `diff -rq` clean **both directions** (only `.git` internals differ).

```
HEAD                     32df94d38a0c39b4c94206966e44f7273e151fca
git rev-list --count HEAD    1811     (--all: 2700)
root commits                    2     aff34717 + efc0cd39, both 2025-01-02
merges                        312
tags                           54     (latest v4.5.2)
tracked files                5867
span               2025-01-02 → 2026-08-24   (latest commit: yesterday)
```

⚠️ **`git rev-list`, never `git log`, for counting** — `git log` truncates at 50 in this sandbox (SIGPIPE; the v267 quirk).

**Composition (tracked lines):**

| Lang | Files | Lines |
|---|---:|---:|
| YAML | 4,266 | 115,049 |
| Python | 641 | 82,689 |
| Markdown | 250 | 38,140 |
| TSX | 104 | 27,515 |
| Go | 111 | 25,931 |

**Authorship:** 47 distinct emails on HEAD (48 across all refs — the extra is `cursoragent@cursor.com`, 1 commit). `zhuque@tencent.com` = 872 of 1,811 (48%). **1,003 commits from `@tencent.com`, 808 from outside (45%)** — and 312 merge commits, so outside contribution is genuinely *merged*, not a code-drop. `aig-bot@tencent.com` (39) and `aigdocs@…` (107) are documentation/i18n maintenance bots.

**Anthropic-authored commits: 0.** No `Co-Authored-By: Claude` provenance in the history.

---

## 1. What it actually is

A **server + agent** platform (two Docker containers) that scans AI infrastructure and AI-agent artifacts, plus **three standalone pip-installable CLIs** and **four Agent Skills**.

`common/agent/types.go:75-82` defines **seven** task types:

```go
TaskTypeTestDemo           = "Test-Demo"
TaskTypeAIInfraScan        = "AI-Infra-Scan"
TaskTypeMcpScan            = "Mcp-Scan"
TaskTypeModelRedteamReport = "Model-Redteam-Report"
TaskTypeModelJailbreak     = "Model-Jailbreak"
TaskTypeAgentScan          = "Agent-Scan"
TaskTypeSkillScan          = "Skill-Scan"
```

The Go side owns fingerprint+CVE scanning natively; the Python CLIs are invoked as subprocesses (`common/agent/skill_task.go` → `uv run --no-project main.py`). No logic is duplicated between them.

**"ClawScan" — the first capability named in the README's opening sentence — has zero lines of Go or Python.** It is delivered as `skills/edgeone-clawscan/SKILL.md` (801 lines of agent instructions) plus a ClawHub listing. A fleet agent called this "documentation-only"; **that is wrong and I nearly propagated it** — the capability is real, its implementation is simply *a skill*, not code. Searching only `*.go`/`*.py` was the wrong population.

---

## 2. ⭐⭐⭐⭐⭐ THE HEADLINE — CI runs 1 of 349 tests, and the gate is aimed at the data

There are **exactly three** workflows. Two fire only on a version tag (`create-release.yml`, `docker-publish.yml`). The third:

```yaml
# .github/workflows/yaml-lint.yml
on:
  push:
    paths: ['data/**', 'cmd/yamlcheck/**']
  pull_request:
    paths: ['data/**', 'cmd/yamlcheck/**']
...
      - name: Run yamlcheck tests
        run: go test ./cmd/yamlcheck          # ← line 32
      - name: Run YAML validation
        run: ./yamlcheck data/fingerprints data/vuln data/vuln_en
```

`go test ./cmd/yamlcheck` is **the only test invocation anywhere in the repository** (full-extent grep across `*.yml`, `*.sh`, `*.json`, `*.toml`, Makefile; positive control: `go build` returns 3 hits). And `cmd/yamlcheck` contains **exactly one test function**.

| | Written | Run by CI |
|---|---:|---:|
| Go test functions | 228 (33 files) | **1** |
| Python test functions | 121 (17 files) | 0 |
| **Total** | **349** | **1 (0.29%)** |

`pytest` is declared in three `pyproject.toml` files and invoked by **no** workflow. The untested-by-CI packages include `common/fingerprints` (the matching engine), `pkg/vulstruct` (the CVE version-range DSL), and `internal/mcp` — i.e. **the code that decides whether a real CVE gets reported**.

**The shape of the mistake is precise, and it is not laziness.** The team wrote 349 tests. The one job that runs a test runner was built to serve the **data pipeline**, and it inherited that pipeline's scope — `paths: data/**`. So the gate covers the artifact the team edits most often, and nothing else. Editing `common/runner/runner.go`, `README.md`, `CHANGELOG.md`, or `docker-compose.yml` triggers **zero CI**.

⚠️ **EXTENT:** there is **no Go toolchain in this sandbox** (`go: not found`), so I could not execute the 228 Go tests. Nothing here measures whether they pass.

---

## 3. ⭐⭐⭐⭐⭐ THE RULE — the reliability of a number is predicted by its audience

The same repository publishes two kinds of number, and the difference is not competence.

### 3a. Where they expect to be checked, the numbers are exact

`CHANGELOG` v4.5.0 (2026-07-27): *"vuln library expanded to **130 components, 1888 rules**"*

```
git ls-tree -r --name-only v4.5.0 -- data/fingerprints | wc -l   →  130
git ls-tree -r --name-only v4.5.0 -- data/vuln         | wc -l   → 1888
```

**Both exact.** (One fingerprint file = one component — `data/fingerprints/9router.yaml` carries a single `info: name:` block. ⚠️ My first pass read "components" as `data/vuln/` subdirectories and got 116; that was **my** wrong population, caught by re-measuring — §43.1.)

Other exact claims that hold: "9 risk categories" = SkillTrustBench **T01–T09** (`skill-scan/README.md:92`); "9 new single-turn jailbreak operators" = commit `d48e5084` (2026-06-18) *"add 9 single-turn jailbreak methods"*; the four named multi-turn attacks all exist.

### 3b. Where they do not, the numbers are soft — and the "+" is the tell

`CHANGELOG` v4.5.2 (2026-08-17): *"vuln library expanded to **2000+ CVE rules**"*

| Population at tag `v4.5.2` | Count |
|---|---:|
| `data/vuln` files | **1,916** |
| `data/vuln_en` files | 1,914 |
| distinct CVE identifiers | **1,662** |
| *vuln + vuln_en (bilingual double-count)* | *3,830* |

**No honest population reaches 2000+.** The only one that does is the **bilingual double-count** — the D23 hazard exactly. At HEAD (7 days later) `data/vuln` = 2,014, so the claim became true for the file population *by being outrun*; on distinct CVEs (1,767) it is still false.

And the same pattern in `CLAUDE.md`, measured at the very commit that wrote it (`58ba98a8`, 2026-03-20):

| CLAUDE.md says | Actual then | Actual at HEAD | Verdict |
|---|---:|---:|---|
| `data/eval` "13+ datasets" | 13 | 17 | ✅ exact when written |
| `data/vuln` "589+ CVE rules" | 640 | 2,014 | ✅ true (conservative) |
| `data/fingerprints` "60+" | **51** | 146 | ❌ **false the day it was typed** |

Three counts, one document, one day: one exact, one conservative, **one already wrong**. A reader cannot tell them apart by looking.

**And the claims requiring a judgment about population are the ones that are wrong:** *"AI Security Skill Market launched (3 official skills)"* — there were **4** skill directories at `v4.5.0`. *"5 new OWASP skills … (10 skills total)"* — there are 4 skill directories; the 10 are agent-scan **detection types**. Two different things counted under one word.

### 3c. And where they expect peer review, the discipline is outstanding

`Research/deepseek-harness-security-assessment/` — a prompt-injection study against **DeepSeek Harness (corpus v235, revisited v242)**:

- **14,560 runs** (`results/summary.json`)
- **TWO independent evaluators reported side by side, including where they disagree** — `J_R` deterministic (5.6% full / 2.0% partial) vs `J_L` semantic (5.3% / 7.3%)
- a written **sanitization policy**: *"one row per completed run without prompts, generated model text, tool arguments, internal paths, credentials, or provider-specific transport fields"*
- **re-runnable**: `python3 analysis/aggregate_statistics.py results/sanitized_results.csv --out-dir results/aggregate`
- high-signal slices published, including the ones that make the tool look *worse* at defending: Hidden-Unicode channel 25.5%, **Skills channel 16.0%**

⇒ **⭐⭐⭐ Agent skills are a working prompt-injection channel at ~16% in a 14,560-run study.** Directly relevant to anyone installing skills.

**Set that beside `README.md:199-210`** — a five-model leaderboard with a bolded F1 of 0.9848, **no dataset size, no methodology, no baseline, no reproduction path**, and a link off-site.

> **THE SHIP'S RULE: the same team measures honestly where it expects to be checked and loosely where it does not — so the reliability of a number is predicted by its AUDIENCE, not by the team's competence. `Research/` is written for peers who will re-run it. The README is written for people who will not.**

**THE LADDER:** v270 no gate fires on a claim true when written · v271 a gate's scope is inherited from where it lives · v272 a gate holds when something else already requires it · v273 a check is only as permanent as the place you put it · v274 a claim is safe when a gate covers it or a habit covers it · v275 a check cannot survive someone with standing to overrule it · **v276 THE SAME PEOPLE APPLY TWO STANDARDS IN ONE REPOSITORY, AND THE VARIABLE IS WHO IS READING.**

---

## 4. ⭐⭐⭐⭐ The trust model that was born incomplete

`SECURITY.md` is genuinely one of the better security documents in the corpus. It states a real threat model (`:70-73`):

> - The operator who launches AIG is fully trusted.
> - Scan targets provided by the operator are treated as external untrusted input.
> - **LLM API responses (in agent scan / MCP scan) are treated as untrusted content — the scan engine processes them, not the host OS.**

and enumerates three deployment modes (`:64-66`), including *"WebUI mode … Binds to `127.0.0.1:8088` by default. **Do not expose to the network.**"* The code obeys it: `cmd/cli/cmd/webserver.go:65` defaults to `127.0.0.1:8088`. **README.md:149** discloses the limitation prominently, right under the install command:

> *"It currently lacks an authentication mechanism and should not be deployed on public networks."*

That is honest, well-placed, and better than most. **But the document that promises untrusted content stays off the host OS never mentions the two settings that qualify that promise:**

```yaml
# docker-compose.yml:48-51 — the AGENT container, which runs the Python scanners
    cap_add:
      - SYS_ADMIN
    security_opt:
      - seccomp:unconfined
```

Full-extent grep: `SYS_ADMIN|seccomp|unconfined|capabilit` in `SECURITY.md` = **0** (positive control: "docker" = 2). The **only** disclosure anywhere is `CHANGELOG.md:466`, under **v3.6.0**, filed as an *Added* feature:

> *"🔐 **System Administration**: Added SYS_ADMIN capability for Chrome sandbox and database indexes for performance enhancement"*

— a capability grant bundled into one bullet with a database-index performance note.

**The timeline settles what kind of failure this is.** `SYS_ADMIN` was added **2026-01-09**; SECURITY.md's trust model was written **2026-04-13/14** (*"docs: add comprehensive SECURITY.md with trust model"*). **The threat model was authored three months *after* the exception it omits.** It did not go stale — it was **born incomplete**, because writing a threat model is an act of recall and nothing in the repository connects `docker-compose.yml` to `SECURITY.md`.

**⭐ And the repo has a YAML validator, runs it in CI, and `paths: data/**` means the YAML checker never reads the YAML file that grants `SYS_ADMIN`.**

**In fairness — the engineering is sound.** The grant has a legitimate reason (`chmod 4755 …/chrome-sandbox`; Chromium's sandbox needs it — the correct choice over `--no-sandbox`), and both workloads **drop to a non-root user**: `Dockerfile_Agent` comments *"the entrypoint … drops to the non-root agent user before starting either application process,"* and `scripts/start_agent_container.sh:34,51` both launch via `gosu agent:agent`. Residual risk is real but reduced: `seccomp:unconfined` removes the syscall filter for *all* processes regardless of uid.

**Also:** `docker-compose.yml:8` publishes `"8088:8088"` — all host interfaces — while README calls Docker the *recommended* path and SECURITY.md says do not expose it. One-line fix: `"127.0.0.1:8088:8088"`.

---

## 5. The rule database — and a false-negative class the gate cannot see

`data/` at HEAD: `vuln` 2,014 · `vuln_en` 2,014 · `fingerprints` 146 · `eval` 17 · `mcp` 15 · `agents` 1.

**Bilingual parity is essentially perfect** — 2,013 of 2,014 relative paths match exactly between `vuln` and `vuln_en`; the single exception is a filename difference on one Clawdbot rule. Across 4,028 files that is impressive.

**Rule quality is high.** A representative rule carries `cve`, `summary`, `details`, a full **CVSS vector**, `severity`, `security_advise`, four `references` (upstream commit, GHSA, VulnCheck, GitHub advisory) and a version-range expression.

**But the matcher and the advisory are two separately-authored fields, and nothing compares them.** Measuring the 1,013 rules with a simple single-clause `rule: version < "X"`:

- **41** differ from the fixed version named in their own `security_advise`
- **31 are benign** (`-stable`, `-rc1`, `-beta5` suffixes, which make the rule *broader*, or a git SHA as the fix identifier)
- **10 are genuine under-matching gaps** where the threshold sits *below* the fix, leaving versions in `[threshold, fix)` vulnerable-but-unflagged:

```
rule<1.83.6    fix=1.83.7     data/vuln/LiteLLM/CVE-2026-30623.yaml
rule<1.123.58  fix=2.28.0     data/vuln/n8n/CVE-2026-58661.yaml
rule<2026.2.21 fix=2026.2.23  data/vuln/openclaw/CVE-2026-22168.yaml
rule<2026.2.22 fix=2026.2.23  data/vuln/openclaw/CVE-2026-22169.yaml
… 7 of the 10 are OpenClaw
```

⚠️ I found this on the **first rule I opened** and nearly generalised it into a systemic claim. Re-measuring gave 10 of 1,013 (~1%), not 41. The honest number is 10.

**`yamlcheck` cannot see any of them — and is honest about that.** Its docstring says *"YAML **format** validation tool"*; it has five functions (`main`, `findCaseInsensitivePathCollisions`, `walkYAMLFiles`, `isYAML`, `categorizeFile`) and **zero** references to `security_advise`, `version`, or `semver`. The tool is correctly scoped. It is simply the only gate.

**⭐ A live instance of the exact bug its one CI test guards against.** `git ls-files` tracks **116** component directories under `data/vuln`; `ls` on a case-insensitive filesystem shows **115**. The collision:

```
data/vuln/AI-Agent-Config/   agent-config-disclosure.yaml
data/vuln/ai-agent-config/   CVE-2026-13236.yaml, CVE-2026-13237.yaml, CVE-2026-61428.yaml
```

One component, two casings, four rules split across both. `TestFindCaseInsensitivePathCollisions` — the single test CI runs — compares **full paths**, and zero full paths collide (the filenames differ). **The checker catches the collision it was written for and not the one that is actually present.**

**CVE year distribution** (a fleet agent claimed 58% were "future-dated … fictional"; **refuted** — today is 2026-08-25, so these are *current-year*, and zero CVEs are dated beyond 2026):

```
CVE-2026: 2274   CVE-2024: 540   CVE-2025: 449   CVE-2023: 148   …
```

⇒ the real signal: **the AI-infra vulnerability surface is compounding** — more current-year CVE references than all of 2024 and 2025 combined.

**Concentration:** `openclaw` holds **657 of 2,014** rule files (**32.6%**), 5.9× the next component (praisonai, 112). It went 810 → 655 between v4.5.0 and v4.5.1 — a ~155-rule dedup, i.e. real hygiene applied *after* those rules had been counted in the "1888".

---

## 6. The skills — the best-engineered part of the repository

Four Agent Skills, **Anthropic `SKILL.md` format with YAML frontmatter**, **MIT** (the rest of the repo is Apache-2.0):

| Skill | Files | Licence | Note |
|---|---:|---|---|
| `aig-agent-redteam` | 182 | Apache-2.0 | offensive blue-team exercise skill, v5.0.0 |
| `aig-scanner` | 4 | MIT | drives the A.I.G server; needs `AIG_BASE_URL` |
| `edgeone-clawscan` | 1 | MIT | OpenClaw security health check |
| `edgeone-skill-scanner` | 1 | MIT | vet a skill **before you install it** |

**These are exemplary agent instructions.** `edgeone-clawscan` declares triggers *and* **non-triggers** (*"Do not trigger for general OpenClaw usage, project debugging, environment setup, or normal development requests"*), and — unusually — **declares its network egress and the opt-out in the frontmatter the agent reads**: *"Optional cloud mode: set `AIG_CLOUD_LOOKUP=off` for zero outbound HTTPS; when enabled, only skill_name, source label, and OpenClaw version are sent."*

`edgeone-skill-scanner` is a **single file, no scripts, no egress**, with a *Security Declaration*: *"Local-only analysis: this scanner performs static analysis by reading skill files only. No file contents, credentials, or personal data are sent externally."* **Verified true** — the whole skill is instructions; the agent does the reading. (Precisely: contents do go to the operator's *own* LLM, as with any skill; nothing goes to Tencent.) **Two sibling skills, two different egress profiles, each stated accurately in its own frontmatter.**

**⭐⭐⭐⭐ And the offensive skill leads with authorization.** `skills/aig-agent-redteam/SKILL.md` 操作原则:

1. **授权优先** — *"确认用户拥有目标或被授权测试，所有动作必须在约定范围内"* ("confirm the user owns the target or is authorized; all actions must stay within the agreed scope")
3. **无害证明** — *"优先使用 canary、临时文件、本地 mock endpoint 和 marker 字符串。只要 marker 能证明同一边界失败，就不要读取、外传、修改或发布真实秘密"* ("prefer canaries, temp files, local mock endpoints and marker strings. If a marker can prove the same boundary failed, do not read, exfiltrate, modify or publish real secrets")
5. **先证据，后结论** — every finding needs concrete evidence; a static suspicion must pass reachability and impact analysis to become a finding

⇒ the strongest safety framing on an offensive artifact the corpus has seen — the sibling of Strix v190's *"no exploit, no report"*, extended to *"prove it with a canary, never with a real secret."*

---

## 7. Where Claude sits

- **`README.md:206` — Claude Opus 4.6 ranks #1** on SkillTrustBench: F1 **0.9848**, Precision 0.9725, Recall **0.9974**, FPR 0.0663 — ahead of GLM 5.1, Gemini 3.5 Flash, Kimi 2.6, DeepSeek v4 Flash. A rival lab's own benchmark putting Claude first.
- ⚠️ **But no code references Opus 4.6.** Defaults are `skill-scan → deepseek-v4-flash`, `mcp-scan → deepseek/deepseek-v3.2-exp`, `agent-scan → claude-3.5-sonnet`. The newest Claude string anywhere in Python is `claude-sonnet-4.5`. **The benchmark's winning configuration is not the shipped default**, and the Claude default that does ship is several generations old.
- **Tencent's own Hunyuan has zero `DEFAULT_MODEL` assignments** — one optional CLI flag with an empty default. A Tencent security product that does not default to Tencent's model.
- `CLAUDE.md`, `AGENTS.md`, `CODEBUDDY.md` all exist at root — **one commit each, all 2026-03-20, never touched since** across 5 months and v4.1→v4.5.2. `CLAUDE.md` documents *"Four Task Types"*; HEAD defines seven, and the two it omits include **Skill-Scan, the flagship v4.5.x feature**. An agent reading it does not know skill-scan exists.
- ⭐ **The only thing in this repository that reads `AGENTS.md` is a vulnerability rule about someone else's** — `data/vuln/openclaw/GHSA-fgvx-58p6-gjwc.yaml` describes symlink traversal via an allowlisted `AGENTS.md`. Nothing verifies its own three.

---

## 8. Supply chain — clean, and the inverse of v271

- **699/699** `frontend/pnpm-lock.yaml` entries carry `integrity: sha512`; **0** mirror-registry references (no npmmirror/taobao) — the sharp inverse of v271's HiThink finding.
- **0** pip `index-url`/`extra-index-url` mirrors anywhere.
- `Dockerfile:15` — `pnpm install --frozen-lockfile --ignore-scripts`. A real hardening measure.
- go.mod: 30 direct dependencies, 629 `go.sum` entries. MCP via `github.com/mark3labs/mcp-go v0.32.0` (not a fork).
- ⚠️ Base images are **tag-pinned, not digest-pinned** (`golang:1.23.2`, `node:22`, `python:3.12`). No SBOM, no `npm audit`/`pip audit`, no dependency scanning in any workflow — **for a security product**.

---

## 9. Licensing

Apache-2.0, **plus a rider** in `NOTICE`:

> *"Mandatory Attribution Requirement (per Apache License 2.0, Section 4(d)): Any redistribution, integration, or derivative work — whether open-source or commercial — … must: 1. Clearly state "Based on Tencent Zhuque Lab AI-Infra-Guard" … 2. Include a link to the original repository."*

The same requirement is repeated in source headers (`cmd/yamlcheck/main.go:15-17`). **Anyone integrating A.I.G into a product carries an attribution obligation beyond stock Apache-2.0.** The four skills are separately **MIT**.

---

## 10. MINT ANALYSIS — **NO NEW MINT**; §C **C26 N=1 → N=2**

**Corpus-first verified at full vault extent** (positive controls all fire — Tencent 36, GitNexus 263, codegraph 170, Strix 36, OpenSandbox 18):

```
AI-Infra-Guard 0 · Infra-Guard 0 · Zhuque 0 · 朱雀 0 · AIG-PromptSecurity 0 · SkillTrustBench 0
```

**Collision found — §C row C26** (N=1, v169 NVIDIA/SkillSpector): *"Defensive-Security Scanner for the Agent-Skills Ecosystem (two-stage static + optional-LLM, risk-scored, multi-format/SARIF)"* — *"a dedicated tool whose FUNCTION is to detect vulnerabilities / malicious patterns in agent-skill packages BEFORE install."*

AIG matches on the specifics, verified:

| C26 element | AIG | Verdict |
|---|---|---|
| vet agent-skill packages **before install** | `edgeone-skill-scanner`: *"Scan any agent skill … before you install or use it"*; `skill-scan` CLI | ✅ |
| **0–100 risk score** | `project_analyzer.py:89` `calc_skill_score() -> int`, *"security score (0-100)"* | ✅ exact |
| per-finding **severity** | severity-weighted deductions | ✅ |
| **multi-format / SARIF** | `skill_scan/utils/sarif_formatter.py`, `to_sarif()` at `main.py:217` (48 refs) | ✅ |
| cross-harness targeting | *"Compatible with CodeBuddy, Cursor, Windsurf, **Claude Code**, OpenClaw"* | ✅ |
| *"two-stage **static** + **optional**-LLM"* | regex pre-scan (`utils/pre_scan.py`, 184 lines) → **mandatory** LLM agent with `read_file`/`grep`/`base64_decode` tools. **Zero** AST/taint/YARA (grep for `import ast\|yara\|taint` in `skill-scan/` returns nothing) | ⚠️ **inverted** |

⇒ **Same two-stage shape, inverted emphasis**: SkillSpector is static-primary with an optional LLM refinement; AIG is regex-advisory with a *mandatory* LLM agent. Fully **independent, cross-author (Tencent vs NVIDIA), cross-region, non-port**.

**RECORDED: C26 N=1 → N=2** (§C-2 39→38, §C-1 12→13, per the v259 bifurcation: *a §C-2 row gaining a genuine 2nd instance promotes into §C-1 and becomes subject to §39*). The mechanism clause in C26's **title** is proposed for generalisation to *"two-stage (pattern-match → LLM)"* — **flagged for the audit, not self-executed**, per the v212 precedent.

**Declined elsewhere:**
- **C39** (Autonomous Multi-Agent Offensive AI Pentesting, N=2, shannon v45 + Strix v190) — `aig-agent-redteam` is a *skill* instructing a host agent, not an autonomous multi-agent system with its own sandboxed toolkit. **Adjacency, not instance.**
- **New §C mint for the platform** — declined: multi-capability-platform-that-bundles-scanners is the v181 cortex-hub / v222 lobehub shape (scale and vendor weight are not a class); §28 is a *supporting* ground only (§44.5).
- **#57 corpus-recursion NOT established as a dependency.** crawl4ai (v29), LLaMA-Factory (v22), vLLM, n8n appear **only as scan targets in `data/vuln/`**. A vulnerability rule naming a product is not a dependency. ⭐ **But a different, genuine corpus link exists:** `Research/deepseek-harness-security-assessment/` is published security research *about* **deepseek-harness (v235/v242)** — recorded as a data point, not counted as #57.

**Recorded strengthening (not self-incremented):** #19 19a (corporate-lab author, not Anthropic) · #66 (supply-chain, positive exemplar) · #68 adjacency (the rule DB is a registry, not a list).

**TWO DEFERRED WATCH AXES (N=1):**
1. *"Vendor-published adversarial security research measuring a **rival vendor's agent harness**, with sanitized reproducible data"* — the DeepSeek-Harness assessment.
2. *"Agent-skill-delivered security capability — a scanner shipped as SKILL.md instructions rather than code"* — ClawScan's delivery model.

---

## 11. ⚠️ METHOD

**Fleet:** 16 dimensions × (read → adversarially refute) = 24 agents; **8 dimensions failed the StructuredOutput retry cap** and were re-run with a plain-text contract (8/8, 0 errors). Totals: **32 agents, ~4.03M subagent tokens, ~992s.** Verdict tally on the structured half: **60 CONFIRMED / 4 REFUTED / 8 CORRECTED**.

**The adversarial layer earned its cost** — it caught a reader claiming 31 single-turn operators where the truth is **29** (and the README documents all 29 *correctly*), and caught a claim that SkillJack was undocumented when it appears in `README.md:72` and 8 locale files.

**⚠️ THREE FLEET ERRORS, ALL ONE FAMILY — generalising from where the agent chose to look:**
1. **Stale sense of *now*** — an agent reported *"~58% of CVEs are future-dated CVE-2026 … fictional/hypothetical."* Today is **2026-08-25**. Current-year identifiers were read as fabricated. **Refuted** (zero CVEs beyond 2026; sample cites real-form vLLM PR + GHSA URLs).
2. **Context contamination at N=2 after v272** — an agent read the *subject's* `CLAUDE.md` and concluded the repo *"appears forked from a personal vault,"* confusing a normal Claude Code config with our own. It was told explicitly not to import cross-repo context.
3. **Wrong population** — an agent reported *"v4.5.0 claimed 130 components but data/vuln holds 115"*, the same error I made.

**⚠️ MY OWN ERRORS, caught by RE-MEASUREMENT not re-reading (§43.1, third consecutive ship):**
1. **"1 Python test file"** — the truth is **17 files / 121 functions**. My regex `(test_|.*_test)\.py$` required a literal `test_.py`.
2. **"116 components vs the claimed 130"** — wrong population; 130 = `data/fingerprints` files at that tag, **exact**.
3. **"41 rule/advisory mismatches"** — generalised from the first file I opened; 31 are benign suffix artifacts. The honest number is **10**.
4. **"ClawScan is unimplemented"** — I searched `*.go`/`*.py`; it lives in `SKILL.md`.

**⚠️ EXTENT NOT OVERCOME:** no Go toolchain (`go: not found`) → the 228 Go tests were never executed. `python3` is silently broken in this sandbox → line-based `awk`/`sed`/`grep` only. No network → advisory URLs checked for form, not resolved. I did not run any scanner against any target.
