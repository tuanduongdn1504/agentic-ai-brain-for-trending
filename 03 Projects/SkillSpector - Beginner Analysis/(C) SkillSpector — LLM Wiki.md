# (C) SkillSpector — LLM Wiki (v169)

> **Ship:** v169 · 2026-06-20 · branch `wiki/v169-skillspector` off `main` (based at `db37cc0` = v168, which is not yet merged — branching off `main`/`b55e0d4` would orphan v168's cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG
> **Pattern outcome:** 1 NEW Library-vocab §C standalone (CORPUS-FIRST) — *"Defensive-Security Scanner for the Agent-Skills Ecosystem"* (N=1). SECONDARY observations only (NO mint): a scoped **Pattern #84 84c** note (multi-LLM-provider backend, NOT rule-distribution) + a **Pattern #17 variant-2** data-point (first NVIDIA-org author). NO new top-level pattern. NO confirmed-count change (**46 / 10**).
> **Tier:** T1 developer security tool / CLI scanner (defensive vulnerability scanner for AI-agent skill packages; CLI + Docker + MCP server + Claude-Code/Codex/Gemini-CLI integration).
> ✅ **Continues the domain variation.** This is **not** a return to the v153→v166 "operating/monitoring AI coding agents" niche — SkillSpector neither watches, hosts, nor orchestrates running agents. It is the corpus's **first defensive-security subject for the agent-skills ecosystem**, pairing naturally with v168 ponytail under an emerging *"agent-skills quality & safety tooling"* meta-theme (ponytail = make the agent write **less**; SkillSpector = verify a skill is **safe** before you install it). And it is the **first disclosed major-vendor (NVIDIA) author** after a long run of pseudonymous-handle ships ((a) FAIL at v160/v164/v165/v166/v168).
>
> ⚠️ **Two synthesis corrections recorded for the record** (the build workflow's agents shared two cascade errors; both overridden at synthesis): **(1)** the agents tagged this OFF-GOAL CAPTURE reasoning "(a) FAIL → off-goal" — **wrong:** routine v2.5 §31 keys the tier on **(b) only** (`(b) MODERATE+ → GOAL-ALIGNED`); v168 ponytail shipped `(a) FAIL · (b) STRONG` as GOAL-ALIGNED, and SkillSpector is the same shape. **(2)** the agents imported v168 ponytail's *"14-platform cross-harness rule distribution / multi-format-output #84 84c"* profile onto SkillSpector — **contamination:** SkillSpector is a *scanner* (4 output formats, 3 LLM providers), not a ruleset distributed as native rule files to 14 harnesses. See §6.

---

## 1. What it is

`NVIDIA/SkillSpector` — verbatim tagline:

> *"Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks."*

A **defensive-security scanner** that analyzes an AI-agent *skill package* **before you install it** and tells you whether it is dangerous. You point it at a local directory or a git URL; it runs a two-stage detection pipeline and returns a **risk score (0–100)** with severity labels, the specific findings, and actionable recommendations. It targets the skill/extension artifacts consumed by **Claude Code, Codex CLI, Gemini CLI, and MCP tools** — the exact things an autonomous-agent developer downloads and runs with very little vetting today.

The motivating premise (README-cited, see §3): a large empirical study found that **~26% of agent skills contain vulnerabilities and ~5% show likely-malicious intent**, yet skills are installed with almost no security review. SkillSpector is the pre-install gate.

It is **NVIDIA's** project (the `NVIDIA` GitHub org) — the **first NVIDIA-authored subject in the 169-wiki corpus** (v72 referenced *NVIDIA NIM* only as an LLM provider, not as an author).

## 2. Capabilities

- **Two-stage detection pipeline** — a fast **static** pass (pattern-matching, AST analysis, taint-tracking, YARA signatures) followed by an **optional LLM semantic** pass that reasons about intent. `--no-llm` runs static-only (free, no API key); the LLM stage adds semantic judgement on top.
- **64 vulnerability patterns across 16 categories** — prompt injection, data exfiltration, privilege escalation, supply-chain risks, dangerous code execution (`exec`/`eval`/`subprocess` via AST), and MCP-specific issues. Skills with executable scripts are the highest-risk class.
- **MCP-specific detection** — **tool poisoning** and **least-privilege / permission-declaration mismatches** (an MCP tool that requests more than it declares).
- **Live CVE lookups (SC4 / OSV.dev)** — queries the **OSV.dev** vulnerability database in real time for known-vulnerable dependencies, with an **automatic offline fallback** and **no auth required**.
- **Risk scoring + severity labels** — a 0–100 score plus per-finding severity and recommendations, so the output is a decision, not just a dump.
- **Multi-format output** — `--format terminal | json | markdown | sarif`. **SARIF** is the key one: it drops straight into CI pipelines and IDE security panels (GitHub code-scanning, etc.).
- **Pluggable multi-LLM-provider backend** — the semantic stage can run on **OpenAI, Anthropic, or NVIDIA `build.nvidia.com`**, selected via `SKILLSPECTOR_PROVIDER` + the matching API-key env var. Defaults are declared in `model_registry.yaml` (a Claude **Opus** model is the stated Anthropic default — see §7 for the exact-id caveat).
- **Exportable LangGraph workflow** — the whole scan is a LangGraph graph, importable as a Python API for programmatic / pipeline use.
- **Distribution** — clone + `uv venv` + `make install`, **or** Docker (`make docker-build` → `docker run … skillspector scan ./my-skill/ --no-llm`, no local Python needed). CLI commands: `skillspector scan ./my-skill/` and `skillspector scan https://github.com/user/my-skill`.

## 3. The research backing

SkillSpector's README frames the tool around an empirical study it calls **"Agent Skills in the Wild"** (cited as **Liu et al., 2026**):

- **42,447 skills analyzed**; **26.1% contain vulnerabilities**; **5.2% show likely-malicious intent**; **skills with executable scripts are 2.12× more likely to be vulnerable**.

⚠️ **Provenance (§37):** these figures are **README-cited / page-stated only.** The study is presented as **third-party external research** that *informed* the tool's design — it is **not** linked to a published paper or preprint, the author affiliations are not disclosed, and (in this mocked-API sandbox) it could not be independently verified. Treat the "research-backed" framing as a stated motivation, not a verified claim. It is a real and useful design rationale; it is not load-bearing for the pattern classification.

## 4. Architecture / how it works

- **Stack:** Python 96.8% + **YARA** 2.1% (rule files) + small "other". Apache-2.0. Docker (`python:3.12-slim-bookworm`). `pyproject.toml` + `uv.lock`, `Makefile`, `.pre-commit-config.yaml`, `langgraph.json`, `model_registry.yaml`, `SECURITY.md`, `THIRD_PARTY_NOTICES.md`. Source under `src/skillspector/`; `docs/` and `tests/` present.
- **Static stage:** YARA signature matching (the 16-category rule library) + Python **AST** analysis for dangerous calls + **taint-tracking** to trace untrusted input to dangerous sinks.
- **Semantic stage (optional):** the findings + skill content are passed to an LLM (provider-pluggable) that judges intent and reduces false positives — the "is this *actually* malicious or just unusual?" pass.
- **External augmentation:** the **OSV.dev** API call for live CVE data (SC4) — a live-lookup capability layered onto the otherwise-local scan.
- **Orchestration:** LangGraph composes the stages into a single workflow that is also exposed as a Python API.

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** The author is **NVIDIA** — a fully-disclosed major US corporate vendor, *not* a cultural-peer and *not* Anthropic. The vault's criterion-(a) is a cultural-peer / disclosed-identity axis whose only major-vendor carve-out, **(a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-specific** (v92/v141). Corporate-org status alone does **not** PASS (a): the precedent is airtight — **v141 Anthropic = (a) PASS via (a)-7; v140 Google = (a) FAIL; v143 ByteDance = (a) FAIL.** NVIDIA falls with Google/ByteDance. No (a)-rescue, no axis minted (the v151-rec-(ii) / v160 / v164–v168 discipline). It doesn't need one — it is goal-aligned via (b).
- **(b) STRONG.** A defensive-security scanner for the **agent-skills ecosystem** is dead-center on goal #1 ("master Claude and autonomous agents for software development"). It operates on the exact artifact type the vault itself **authors** (`05 Skills/`, 9 skills) and **installs** (it just evaluated the ponytail Claude-Code plugin at v168), and it is **directly pilotable** — point it at the vault's own skills. Held **STRONG (not STRONGEST):** it is a third-party tool *about* skills (passive validation), not the substrate (Claude/Anthropic) and not a behavior layer that changes how the agent works (the v161/v168 "near-STRONGEST" calibration is reserved for substrate-coupled subjects).
- **(c) STRONG.** Apache-2.0; a mature LangGraph pipeline; a 16-category YARA rule library + AST + taint-tracking; live OSV.dev CVE integration; MCP-aware checks; four output formats incl. SARIF for CI; Docker + pre-commit + a model registry. Research-grounded design (page-stated, §3). The one real maturity caveat: **0 published releases** (continuous `main` development, 36 commits) → it is pre-release tooling (see §9 pilot fence).
- **(d) STRONG.** 1 NEW corpus-first §C standalone (the defensive-scanner capability) + a scoped Pattern #84 84c observation (multi-LLM-provider backend) + a Pattern #17 variant-2 data-point (first NVIDIA-org author) + a clean cross-reference to Pattern #66 (active-scanner complement to passive supply-chain-awareness). See §6.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is STRONG (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s outcome does **not** affect the tier — off-goal capture is defined by `(b) FAIL`, which does not apply here.

## 6. Pattern Library outcome — 1 NEW §C standalone + secondary observations (NO mint)

**PRIMARY — 1 NEW Library-vocab §C standalone, N=1, CORPUS-FIRST:**

- **"Defensive-Security Scanner for the Agent-Skills Ecosystem (two-stage static + optional-LLM, risk-scored, multi-format/SARIF)."** A dedicated tool whose **whole purpose** is to detect vulnerabilities / malicious patterns in agent-skill *packages* before install: static pattern-match + AST + taint-tracking + YARA + live-CVE (OSV.dev) → optional LLM semantic judgement → a 0–100 risk score + SARIF/JSON/markdown output. **Corpus-first** — no prior subject is a defensive security scanner *for agent skills*. Honestly distinguished from the corpus's two nearest security neighbors: **shannon (v45)** = an *offensive* autonomous AI **web/API pentester** (T5 agent-as-application; attacks running apps), and **magika (v44)** = Google-Research **ML file-type classification** (security-adjacent content routing). SkillSpector is neither offensive nor a classifier — it is *defensive vetting of skill artifacts*. **§28: 1 new standalone (≤2 cap honored).** PROMOTION-ELIGIBLE at a genuine 2nd defensive scanner for agent skills; time-aware stale-watch (≥15 wikis AND ≥30 days, §39).

**SECONDARY observations (NOT minted):**

- **Pattern #17 variant-2 (big-tech-curator) — NVIDIA-org-authored OSS, a clean data-point.** SkillSpector is the **first NVIDIA author** in the corpus (variant-2 = big-tech-org OSS; magika v44 = the Google-Research 2b instance). Recorded as a data-point strengthening of an already-CONFIRMED pattern. **The proposed new "2c security-research-lab" sub-distinction is REJECTED (§28)** — NVIDIA's internal org-unit (official-product vs research-lab) is not disclosed, so 2a-vs-2b is undetermined; no new sub-mechanism.
- **Pattern #84 84c "Provider-Agnostic-By-Design" — a scoped, distinct instance via the LLM backend, recorded as an OBSERVATION, not a sub-mechanism mint.** SkillSpector's semantic stage runs equally on OpenAI / Anthropic / NVIDIA = provider-agnostic *by design on the LLM-backend axis*. ⚠️ This is **NOT** ponytail's 84c.1/84c.2 mechanism (distributing native rule files to 14 harnesses) — that "14-platform cross-harness distribution / multi-format-output" framing was **v168 ponytail's profile contaminating the build workflow** and is explicitly rejected here. SkillSpector is a scanner with 4 *output formats* and 3 *LLM providers*, not a ruleset distributed across platforms.
- **Pattern #66 supply-chain — cross-referenced, NOT instanced.** SkillSpector is the **active-scanner complement** to #66's *passive supply-chain-awareness* (where prior subjects merely screen `curl|bash` or are *aware* of supply-chain risk, SkillSpector is a dedicated tool that scans + scores + reports). Supply-chain is just **1 of its 16 categories**, so the primary home is the §C standalone, not #66. NOT a #66 mint.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Current confirmed max is **#85**; the security-scanner shape is captured at the §C-standalone tier per §28 (no #86+). (This is the same anti-inflation discipline that rejected the over-reaching #86/#88 proposals at v168.)
- **NOT Pattern #52 (viral velocity).** Page-stated **8.3k★ / 632 forks / 36 commits / 0 releases** are NOT API-verified (§37.4) and no creation date is shown → velocity is unestablishable → not a #52 claim.
- **NOT Pattern #57 (corpus-recursion / agentskills.io chain).** SkillSpector *scans* skills; it is not an agentskills.io skill-authoring implementer, and it cites no corpus subjects.
- **NOT Pattern #18 (agent-runtime-standardization / shared-backend service).** The exportable LangGraph workflow is a library API, not a shared backend or runtime standard.

**Counts UNCHANGED: 46 patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL surface **≈27 → ≈28** (+1 §C standalone).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** ≈**8.3k★ / 632 forks / 36 commits / 40 open issues / 42 open PRs / 0 published releases.** Apache-2.0. Python 96.8% + YARA 2.1%. Owner = `NVIDIA` org. **No creation date shown** on the rendered repo → age & velocity unestablishable → **explicitly NOT a Pattern #52 claim.** Zero releases + continuous-`main` development = pre-release tooling.
- **Research study (page-stated, third-party, unverified):** "Agent Skills in the Wild" / **Liu et al., 2026** — 42,447 skills; 26.1% vulnerable; 5.2% likely-malicious; scripts 2.12× more vulnerable. **README-cited only; no published paper/preprint link; author affiliations undisclosed; not NVIDIA's own study.**
- **Model defaults (repo/registry-stated, treat as approximate in a mocked env):** the build recon read `model_registry.yaml` as listing a Claude **Opus** model as the Anthropic default (reported `claude-opus-4-5`, with `claude-opus-4-6` also present), an OpenAI default (README `gpt-5.4` vs registry `gpt-5.2`/`gpt-5.3-chat`), and **no NVIDIA model id** in the registry. Exact ids are page/registry-stated and not load-bearing — the durable fact is *pluggable OpenAI/Anthropic/NVIDIA providers with a Claude-Opus Anthropic default*.

## 8. Streak / state

- **Streak:** `GA:30 · OG:11 [7 ov]` → **`GA:31 · OG:11 [7 ov]`** (31st GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35:** rolling-3-ship window {v166 GA, v168 GA, **v169 GA**} = **0 OG → STAYS CLEAR.** (v167 was an audit, not a ship.) **16 consecutive goal-aligned ships v153→v169.**
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Tracked PROVISIONAL surface ≈27 → **≈28** (+1 §C standalone).

## 9. Pilot note

**Strong, immediately-useful, and the lowest-risk pilot candidate the vault has seen:** point SkillSpector at the vault's own **`05 Skills/`** (9 skills) and let it scan for prompt-injection / data-exfiltration / privilege-escalation / dangerous-code patterns. It is a **read-only scanner** — it does not modify the skills, unlike v168 ponytail which installs hooks into your CLI configs — so the blast radius is minimal.

- **Pilot fence:** Apache-2.0, reversible. Needs Python/`uv` **or** Docker. Run **`--no-llm` first** (free static-only pass, no API key, no token spend); only add the LLM stage if the static pass flags something worth a semantic second opinion. ⚠️ **0 releases / continuous `main`** → pin a commit SHA; treat findings as advisory (a young scanner has false positives + gaps). If useful, wire a `bin/skillspector-audit.sh` static-only gate over `05 Skills/`.
- **Levers:** v169 **continues the domain variation** (defensive-security, a third distinct domain after v166 observability and v168 code-minimalism) — it is *not* a reversion to the operating/monitoring niche. The **PILOT lever still formally stands** (zero of the catalogued subjects piloted); SkillSpector + ponytail are now the two strongest, on-goal, immediately-useful pilot candidates, and SkillSpector is the safer first pilot.

## Suggested next action

Commit the v169 ship on `wiki/v169-skillspector` (don't merge — operator reviews + merges; note the branch is based on v168/`db37cc0`, which is itself unmerged). Then **pilot SkillSpector `--no-llm` on the vault's own `05 Skills/`** — it is read-only, free in static mode, on-goal, and discharges the standing PILOT lever with the least risk of any candidate to date.
