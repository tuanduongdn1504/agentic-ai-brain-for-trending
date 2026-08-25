# (C) AI-Infra-Guard — Verdict

**v276** · `Tencent/AI-Infra-Guard` · Apache-2.0 (+ mandatory-attribution rider) · HEAD `32df94d3` · 2026-08-25

---

## Rating: **GOAL-ALIGNED INCLUDE 3/4**

| Axis | Call | Basis |
|---|---|---|
| **(a) Anthropic affiliation** | **FAIL** | Tencent Zhuque Lab — a corporate security lab, not Anthropic. §41 admits no inference from notability. #19 19a. |
| **(b) Goal relevance** | **STRONG** | The subject's primary objects are **agent skills, MCP servers, and AI agents** — the operator's own working surface. It ships four Anthropic-format `SKILL.md` skills, benchmarks Claude as an agent-security engine, and publishes a 14,560-run study finding agent skills are a working prompt-injection channel. |
| **(c) Quality** | **STRONG** | 1,811 commits, 54 tags, 45% outside-contributed and merged, a real threat model, 349 tests, a 4,028-file bilingual rule DB at near-perfect parity, clean supply chain. |
| **(d) Actionability** | **STRONG** | Apache-2.0; three pip CLIs; one skill that is a single file with zero egress and is installable today. |

Cleanly goal-aligned. **No §40 needed, no override.** Streak: `GA:132` → **`GA:133 · OG:13 [7 ov]`** — **56 consecutive GA v220→v276**. §35 CLEAR ({v274, v275, v276} = 0 OG). Override review: **16th consecutive discharge**.

---

## Mint: **NO NEW MINT** — §C **C26 N=1 → N=2**

Counts **46 / 12 UNCHANGED**. §C-2 **39 → 38**, §C-1 **12 → 13**.

`skill-scan` + `edgeone-skill-scanner` are a genuine, independent, cross-author, **non-port** second instance of **C26** (v169 NVIDIA/SkillSpector) — matching on function, the **0–100 risk score**, per-finding severity, **SARIF**, and cross-harness targeting; differing on mechanism (regex→**mandatory** LLM agent vs static-AST/taint/YARA→**optional** LLM). The mechanism clause in C26's title is proposed for generalisation — **recorded for the audit, not self-executed** (v212 precedent).

**#57 NOT established.** Prior corpus subjects appear only as **scan targets**, never dependencies. Recorded separately: `Research/deepseek-harness-security-assessment/` is published research *about* corpus **v235/v242**.

---

## The one-sentence finding

> **The same team measures honestly where it expects to be checked and loosely where it does not — so the reliability of a number is predicted by its audience, not by the team's competence.**

Three numbers prove it, all from one repository:

- **`Research/`** — 14,560 runs, **two independent evaluators reported side by side including where they disagree**, a written sanitization policy, a re-runnable aggregation script. Written for peers.
- **`CHANGELOG` v4.5.0** — *"130 components, 1888 rules"*. Both **exactly** derivable at that tag. Written for people who might check.
- **`CHANGELOG` v4.5.2** — *"2000+ CVE rules"* when the tree held **1,916 files / 1,662 CVEs**, reachable only as a **bilingual double-count**. Written for people who will not.

**The "+" is the tell.** Every exact number A.I.G publishes is exact. Two of three round floors were false when typed — including `CLAUDE.md`'s *"60+"* fingerprints written on a day the tree held **51**.

---

## What is genuinely excellent

- ⭐⭐⭐ **The DeepSeek-Harness study** — the strongest measurement discipline in the repository, and it reports the results that make its own defences look *worse* (Skills channel 16.0%, Hidden-Unicode 25.5%).
- ⭐⭐⭐ **The offensive skill leads with authorization** — *"确认用户拥有目标或被授权测试"* — and with harm-minimization: *"if a marker can prove the same boundary failed, do not read, exfiltrate, modify or publish real secrets."* The sibling of Strix v190's *"no exploit, no report."*
- ⭐⭐ **Two sibling skills, two egress profiles, each declared accurately in the frontmatter the agent reads** — one *"zero outbound HTTPS with `AIG_CLOUD_LOOKUP=off`"*, the other *"Local-only analysis … nothing leaves your device"* (verified: it is a single file with no scripts).
- ⭐⭐ **`README.md:149` discloses the missing authentication** prominently, directly under the install command.
- ⭐ **Supply chain clean:** 699/699 lockfile entries `sha512`-hashed, **zero** mirror registries, `--ignore-scripts` on install — the inverse of v271.
- ⭐ **Bilingual rule parity 2,013/2,014** across 4,028 files.
- ⭐ **Defaults to DeepSeek and Claude, not to Tencent's own Hunyuan** (0 `DEFAULT_MODEL` assignments).

## Where it does not hold

- 🔴 **CI runs 1 of 349 tests (0.29%)** — the only `go test` in the repo targets `cmd/yamlcheck`, which has one test function, and fires only on `data/**` changes. `common/fingerprints`, `pkg/vulstruct`, `internal/mcp` — the code deciding whether a real CVE is reported — are never run by automation.
- 🔴 **The trust model was born incomplete.** `SECURITY.md` promises untrusted LLM content reaches *"the scan engine, not the host OS"* and never mentions `SYS_ADMIN` + `seccomp:unconfined` (grep = 0; control = 2). The capability predates the document by three months. ⭐ *And the repo's own YAML checker never reads the YAML file that grants it, because `paths: data/**`.*
- 🔴 **`docker-compose.yml:8` publishes `"8088:8088"`** to all interfaces while the docs say do not expose it. One-line fix: `"127.0.0.1:8088:8088"`.
- 🔴 **10 under-matching rules** (of 1,013 simple ones) where the matcher's threshold sits below the fix its own advisory names — a false-negative window; 7 are OpenClaw. `yamlcheck` validates *format* and cannot see it.
- 🔴 **A live case-collision the one CI test cannot catch:** `AI-Agent-Config/` vs `ai-agent-config/` — one component, two casings, four rules split. The test compares full paths; the filenames differ.
- 🔴 **Three agent-config files, one commit each, 2026-03-20, never updated.** `CLAUDE.md` documents *"Four Task Types"*; HEAD has seven, and the two omitted include **Skill-Scan, the flagship feature**.
- ⚠️ **The benchmark's winner is not the shipped default** — README ranks Claude Opus 4.6 #1; `agent-scan` defaults to `claude-3.5-sonnet`, and no code mentions Opus 4.6.
- ⚠️ **No SBOM, no dependency audit, no image digest-pinning** — in a security product.

---

## PILOT: ⭐⭐ **READ-AND-BORROW FIRST — then ONE fenced, zero-egress skill**

**Rung 0 (45 min, zero install).** `Research/deepseek-harness-security-assessment/results/RESULTS.md` — the 16% skills-channel injection rate is the number that should change your behaviour · `skills/aig-agent-redteam/SKILL.md` 操作原则 1/3/5 · both `edgeone-*` frontmatters as the model for declaring egress in a skill · `SECURITY.md:60-90` as a threat-model template · `README.md:206` beside `Research/` as the audience lesson.

**Rung 1 (20 min, the vault item).** ⭐⭐⭐ **This ship names what to gate — and it completes the arc.** v273 said *where* the inventory check must live (`bin/`, not a project folder); v274 said *how* to write its clauses (derive the population from the tree); v275 said *what to aim it at* (your published claims, not only generated files); **v276 says which claims rot: the ones with a `+`.** Add a clause to `(C) proposed-verify-vault-inventory.sh`: **every count asserted in the CLAUDE.md head block must be re-derivable by a command, and any figure written as a round floor (`N+`, `~N`, `over N`) must either be replaced by an exact count or carry a date.** A.I.G's exact numbers were all right; its floors were half wrong. **Ours are all floors.**

**Rung 2 (30 min, LOW risk, genuinely useful).** Install **`edgeone-skill-scanner`** only — a **single `SKILL.md`, no scripts, no network egress**, MIT — and run it over `05 Skills/`. This is the first corpus subject that can vet the vault's own skills, and it is the safest thing in the repository.

**Rung 3 (60 min, MEDIUM).** `pip install aig-skill-scan` in a throwaway venv, point it at a scratch copy of one skill. ⚠️ It is **LLM-driven** — it sends skill source to a model provider; set `DEFAULT_MODEL` deliberately (it defaults to `deepseek-v4-flash`). Run `install-snapshot` first.

**🔴 NEVERs.** Never `docker-compose up -d` as shipped — it publishes an **unauthenticated** UI on all interfaces and runs the scanner container with `SYS_ADMIN` + `seccomp:unconfined`; fix the port binding first. Never point A.I.G at infrastructure you do not own — the red-team skill's own principle #1. Never cite **"2000+ CVE rules"** (1,916 at that tag), **"3 official skills"** (4), or **"10 skills total"** (4 dirs). Never quote **0.9848** as A.I.G's score — it is **Claude Opus 4.6's**, on Tencent's own benchmark, with no published methodology. Never trust `CLAUDE.md`'s task list. Never assume `data/vuln` coverage implies detection — 10 rules under-match their own advisories. Never integrate the code without the **`NOTICE` attribution rider**.

---

## Suggested next action

Review + merge **`wiki/v276-ai-infra-guard`** off the v275 tip (`99c419c`). ⚠️ **`main` is at v226 — v227→v275 plus this ship are outstanding.**

Then **Rung 2**: install `edgeone-skill-scanner` and run it over `05 Skills/`. It is one file, MIT, zero egress, and it answers a question the vault has never asked itself.

**Blunt:** this is a competent security lab with a real culture of measurement that switches off at the README. The evidence is that both behaviours are in one repository, three weeks apart, from the same people. Their research directory runs two independent evaluators and publishes the disagreement between them; their changelog rounds 1,916 up to "2000+" and calls four skills three. Their threat model is careful and genuine and was written three months after the `SYS_ADMIN` grant it never mentions — not stale, *born incomplete*, because writing a threat model is an act of recall and nothing in the repo connects `docker-compose.yml` to `SECURITY.md`. They wrote 349 tests and wired one, because the only job that runs a test runner was built to serve the data pipeline and inherited its `paths:` filter. **Now turn it around.** Every number in our own CLAUDE.md head block is a floor or an estimate — "~197.6KB", "≈19", "46/12" — restated every ship, checked by nothing, and read by exactly one audience that never audits it. A.I.G proves the diagnosis is not carelessness: **when they expected a reader who would re-run the number, they published the script.** The question this ship puts to us is not whether our counts are right. It is which of them we have ever written for a reader who would check.
