# (C) Strix — Deep Dive (v190 wiki)

> **Subject:** `usestrix/strix` — *"The open-source AI pentesting tool. Autonomous AI hackers that find and fix your app's vulnerabilities."*
> **Built + source-verified** from a clone pinned at commit **`e6ca4d2`** (last commit 2026-07-02, v1.0.4). Apache-2.0. Python 91% / Jinja 4.6% / Shell 2.8% / Dockerfile 1.3%. 32.3k★ / 3.4k forks / 16 releases (page-stated, §37.4 — NOT API-verified velocity).
> **What this doc is:** the double-deep-dive knowledge extract requested by the operator. Verdict + pattern accounting live in `(C) Strix — Verdict.md`; how-to-apply lives in `(C) Strix — Pilot Methods Menu.md`.
> **AI-generated (Claude) — prefixed `(C)` per vault rule.**

---

## 1. One-paragraph what-it-is

Strix is an **autonomous, multi-agent AI penetration-testing system**. You point it at a target — a live URL, a domain, a GitHub repo, or a local codebase — and it spins up a **graph of specialized AI agents** (recon → discovery → validation → reporting → fixing) that run inside an isolated **Kali-Linux Docker sandbox** stocked with ~60 real pentest tools (nmap, nuclei, sqlmap, ffuf, semgrep, a Caido HTTP-interception proxy, a headless browser, a Python exploit sandbox…). Each agent *thinks, plans, calls a tool, reads the output, and iterates* like a human attacker. The defining discipline: **"validation is mandatory — never trust scanner output, always validate with a working proof-of-concept."** A finding is only reported once a dedicated validation agent proves it with a real PoC, so the headline pitch is **zero false positives by construction** ("if the PoC works, the vulnerability is real"). In white-box mode it also **writes the fix** (code diff in the report). It's LLM-agnostic (8 providers via LiteLLM; Claude is a first-class recommended backend but GPT-5.4 is the example default), ships a CI/CD gate that fails a PR when new vulns appear, and has a commercial hosted twin at **app.strix.ai**.

**In one line for Storm Bear:** this is **shannon v45's species** — the corpus's second autonomous AI web/API pentester — but Python + OpenAI-Agents-SDK + black-box-AND-white-box-AND-auto-fix, and, crucially, **the first corpus subject that is directly, natively pilotable against a real app you own: hireui.**

---

## 2. Provenance, identity, maturity (hand-verified)

| Fact | Value | Confidence |
|---|---|---|
| Repo | `usestrix/strix` | ✅ verified |
| PyPI package | `strix-agent` (v1.0.4) | ✅ `pyproject.toml` |
| License | Apache-2.0 | ✅ LICENSE + classifier |
| Author (pyproject) | `Strix <hi@usestrix.com>` | ✅ |
| Agent's in-prompt self-identity | *"developed by **OmniSecure Labs**"* | ✅ `system_prompt.jinja:1` — a deliberate abstraction (the prompt also forbids the agent from putting the name "Strix" in payloads/user-agents); do **not** over-read as the legal entity |
| Python | ≥3.12 (3.12 / 3.13 / 3.14) | ✅ |
| Dev status classifier | **"3 - Alpha"** | ✅ `pyproject.toml:22` — despite 32k★ / v1.0.4, the authors still label it Alpha |
| Hosted platform | app.strix.ai (SaaS; from ~$9/seat/mo, credit-per-scan; you pay LLM tokens separately) | 🟡 web-stated |
| Enterprise | SSO, SOC 2 Type II / ISO 27001 / PCI DSS reports, VPC/self-hosted/air-gapped, BYOK | 🟡 web-stated |
| Public launch | ~August 2025 (coverage from HelpNetSecurity 2025-11-17) | 🟡 web-stated |
| Funding "$117M" / founders "Matt Shannahan, Mahesh Ramichetty" / YC | **UNVERIFIED** — web-search only, no official source; a $117M raise for a mid-2025 launch is implausibly large and untraced. Report with a straight face at your peril. | ⚠️ flagged |

---

## 3. Architecture — the five layers

Strix is a Python framework wrapping the **OpenAI Agents SDK** (`openai-agents[litellm]==0.14.6`) — *not* the Claude Agent SDK that shannon v45 used. Model access is LiteLLM, so any provider is pluggable.

### 3.1 The agent loop
`Runner.run_streamed()` drives one unified think→act→observe→iterate loop per agent (`core/execution.py`). Each turn: replay the persistent SDK session (SQLite) → the LLM emits an action → a tool runs → the result is appended → next turn. Hard limits: **`DEFAULT_MAX_TURNS = 500`** (`core/inputs.py:18`, configurable) and an optional **`--max-budget-usd`** dollar cap checked after every response (stops cleanly, can slightly overshoot for in-flight calls).

**The termination discipline is striking and directly echoes loop-engineering v189:** in non-interactive mode, *"A message WITHOUT a tool call IMMEDIATELY STOPS your entire execution"* and *"A text-only turn — even one — IMMEDIATELY ends the scan/run with no report written. The lifecycle tools (`finish_scan` for root, `agent_finish` for subagents) are the ONLY valid way to terminate."* (`system_prompt.jinja:26-46`). Every working turn must be a tool call; idle agents call `wait_for_message`. This is a durable-state + explicit-termination contract — the same lesson your loop conventions encode.

### 3.2 Graph of Agents (multi-agent orchestration) — the crown jewel
An `AgentCoordinator` (`core/agents.py`) holds a live parent/child tree: `statuses` (running/waiting/completed/stopped/crashed/failed), `parent_of`, `names`, `runtimes`. Every agent runs in its own detached `asyncio.Task`. Six orchestration tools (`tools/agents_graph/tools.py`):

- **`create_agent(name, task, inherit_context, skills)`** — spawns a specialist child (max 5 skills, prefer 1–3), runs async; parent continues immediately.
- **`view_agent_graph`** — indented tree snapshot, caller marked `← you` (call before spawning to avoid duplicates).
- **`send_message_to_agent(target, message, type, priority)`** — inter-agent inbox; message appended to target's session, wakes it (query / instruction / information; low→urgent).
- **`wait_for_message(reason, timeout=600)`** — parent parks until a child reports; a permanent-stall guard warns if you wait with no living children.
- **`agent_finish(result_summary, findings, …)`** — subagent completion → posts a structured report to the parent's inbox → marks itself completed. (Root uses `finish_scan`.)
- **`stop_agent(target, cascade=True)`** — graceful `after_turn` cancel of an agent + (optionally) its whole subtree.

**The doctrine (from the system prompt):** the **root agent is an orchestrator, not a tester** — it delegates, tracks todos/notes, monitors results, decides next steps. Subagents do the substantive work. Trees are **nested, never flat**. Agents are spawned **reactively** as attack surface is discovered. **One job per agent**; specialization is mandatory (no "kitchen-sink" agents). The fixed workflow per finding:

```
BLACK-BOX:  Discovery → Validation (PoC) → Reporting                    (3 agents / vuln)
WHITE-BOX:  Discovery → Validation (PoC) → Reporting → Fixing (+ diff)  (4 agents / vuln)
```

**The maker/checker pattern is baked in:** *"VALIDATION IS MANDATORY — Never trust scanner output, always validate with PoCs"* + *"Independent verification through subagent."* This is exactly your `loop-verifier` (REJECT-first) discipline, expressed as a mandatory second agent that must independently reproduce the finding before it's allowed to be reported.

### 3.3 The tool surface (~20 host tools)
- **Proxy (Caido)** — `list_requests` (HTTPQL-filtered capture), `view_request` (raw inspect + regex search), `repeat_request` (replay with arbitrary field mods — the auth-bypass/injection primitive), `list_sitemap` / `view_sitemap_entry` (attack-surface map), `scope_rules` (allow/deny glob patterns; denylist always wins). GraphQL to a Caido sidecar on `127.0.0.1:48080`.
- **Reporting** — `create_vulnerability_report`: **CVSS 3.1** (8 metrics), CVE/CWE validation, **PoC code REQUIRED**, `code_locations` with verbatim `fix_before`/`fix_after` PR-suggestion diffs, and **LLM-based deduplication** (rejects re-reports of the same root cause on the same asset).
- **Research** — `web_search`: Perplexity `sonar-reasoning-pro`, biased toward exploit info / CVEs / WAF bypasses / Kali-compatible tooling (needs `PERPLEXITY_API_KEY`).
- **State** — `create_note`/`list_notes`/… (categories: general/findings/methodology/questions/plan/wiki), `create_todo`/… (per-agent isolated lists), `think` (private CoT).
- **Lifecycle** — `finish_scan` (root; 4 customer-facing report sections), `agent_finish` (subagent), `load_skill`.
- **Sandbox-side** (emitted at runtime, not declared as host tools) — shell / terminal, Python exec, a headless browser (`agent_browser`), and every CLI in the Kali image.

### 3.4 Skills — progressive disclosure applied to a security vertical
Strix internally uses the **Anthropic-style SKILL.md pattern** (frontmatter scan + on-demand load), which is why this subject connects straight to the corpus's agent-skills lineage. **45 markdown skill files** (no compiled payloads — pure knowledge):

| Category | Count | Examples |
|---|---|---|
| `vulnerabilities/` | 21 | sql_injection, xss, ssrf, idor, rce, ssti, xxe, csrf, race_conditions, business_logic, authentication_jwt, mass_assignment, nosql_injection, path_traversal_lfi_rfi, insecure_file_uploads, subdomain_takeover, open_redirect, http_request_smuggling, header_injection, broken_function_level_authorization, information_disclosure |
| `tooling/` | 11 | nmap, nuclei, sqlmap, ffuf, katana, naabu, subfinder, httpx, semgrep, python, agent_browser |
| `scan_modes/` | 3 | quick, standard, deep |
| `frameworks/` | 3 | fastapi, nestjs, nextjs |
| `technologies/` | 2 | supabase, firebase_firestore |
| `coordination/` | 2 | root_agent, source_aware_whitebox |
| `protocols/` | 1 | graphql |
| `custom/` | 1 | source_aware_sast |
| `cloud/` | 1 | kubernetes |

Skills are loaded two ways: `create_agent(skills=[...])` injects a specialist's knowledge at spawn; `load_skill(...)` pulls up to 5 skills inline mid-task. A skill file is a structured knowledge package — attack surface → detection channels → key vulnerabilities → bypass techniques → **testing methodology** → **validation (how to prove it, avoid false positives)** → impact → pro-tips. The **scan modes are themselves skills** (quick = time-boxed high-impact, skip enumeration; standard = source-aware triage + prioritized dynamic validation; deep = exhaustive, hierarchical agent decomposition, *"if one approach fails, try ten more"*).

> **Note for the operator:** this is essentially a domain-vertical skill collection (like Anthropic-Cybersecurity-Skills v98) **fused into an autonomous agent that consumes it.** The skill-authoring format is directly harvestable into your own `05 Skills/`.

### 3.5 Sandbox & runtime — where the danger lives (and is contained)
Per-scan **ephemeral Docker container** from `ghcr.io/usestrix/strix-sandbox:1.0.0` (Kali-rolling + ~60 tools; a Caido proxy sidecar runs in-container and MITM-intercepts all tool traffic for inspection). Container gets `NET_ADMIN` + `NET_RAW` (raw-socket scanning), runs as an unprivileged `pentester` user **with NOPASSWD sudo**, `/workspace` is the target root, host reachable via `host.docker.internal`. Honest risk findings from the source read:

- **No resource limits** (no `--memory`/`--cpus`/`--pids-limit`) → a runaway tool can exhaust the host. (Ostorlab's independent 2026 test saw Strix cause *"persistent database connection pool exhaustion"* on the target — aggressive automated testing can knock over the very app it's testing.)
- **Container isolates the *tooling*, not the *target*** — the agent reaches out over the network to whatever `--target` you gave it. The sandbox protects your machine from the tools; it does **not** stop the agent from attacking an out-of-scope host.
- **No digest pinning** on the sandbox image (tag `:1.0.0`), no SLSA/Sigstore (contrast codebase-memory-mcp v172, which shipped SLSA-L3).

---

## 4. Invocation surface (what you actually type)

```bash
strix --target ./app-directory                      # white-box: local repo (static + dynamic + auto-fix)
strix --target https://github.com/org/repo          # security review of a repo
strix --target https://your-app.com                 # black-box: deployed app
strix -t https://github.com/org/app -t https://staging.app.com   # multi-target (source + deployed)
strix --target api.app.com --instruction "Focus on business logic + IDOR"
strix --target api.app.com --instruction-file ./rules-of-engagement.md
strix -n --target ./ --scan-mode quick --scope-mode diff --diff-base origin/main   # CI/PR gate
strix --resume <run_name>                            # resume a prior scan
```

Flags that matter: `--scan-mode {quick|standard|deep}` (default **deep**), `-n/--non-interactive` (headless; **exit code 2 = vulns found** → fails CI), `--max-budget-usd <float>` (dollar cap), `--scope-mode {auto|diff|full}` + `--diff-base`, `--mount` (bind-mount huge repos read-only). Config via `STRIX_LLM` (e.g. `anthropic/claude-sonnet-4-6`), `LLM_API_KEY`, `STRIX_REASONING_EFFORT` (none…xhigh), `PERPLEXITY_API_KEY`. Results land in `./strix_runs/<run_name>/` (Markdown + CSV + JSON, atomic writes). The interactive TUI (Textual) shows a **live agent-graph** (◈ spawning · → messaging · ◆ completed · ○ waiting · ◼ stopping) + a color-coded vulnerabilities panel with click-through PoC + remediation.

---

## 5. Providers, cost, benchmarks

- **8 LLM providers via LiteLLM:** OpenAI, Anthropic, Azure, Bedrock, Vertex, OpenRouter, Novita, local (Ollama/LMStudio via `LLM_API_BASE`). Recommended: **OpenAI GPT-5.4** (`openai/gpt-5.4`, the example default), **Anthropic Claude Sonnet 4.6** (`anthropic/claude-sonnet-4-6`), **Google Gemini 3 Pro**. Claude is first-class but *not* the default in the docs.
- **Cost model:** the tool itself is free; **you pay LLM tokens.** Concrete anchor from the repo's own benchmark: **~$337 to solve 100 XBEN challenges ≈ $3.37/challenge.** `--max-budget-usd` caps a run (but is **off by default** — the real cost-runaway risk).
- **Benchmark (repo's own, `benchmarks/README.md`):** **XBEN** (called "the XBOW benchmark", 104 web-security CTF challenges), Strix **v0.4.0 = 96% (100/104) black-box** — L1 100% (45/45), L2 96% (49/51), L3 75% (6/8), avg ~19 min/challenge. Independently echoed by Ostorlab's May-2026 review. ⚠️ **Caveat:** vendor-run; and shannon v45 also claimed XBOW ~96.15% — the two are *not* directly comparable (different modes/challenge sets), so read "~96% on an XBOW-lineage eval" as a capability signal, not a head-to-head result.

---

## 6. Dual-use, telemetry, safety — read this before piloting

Strix is an **offensive** tool. The source read is honest about what that means:

1. **No programmatic authorization enforcement in the OSS CLI.** The only guardrail is a README warning: *"Only test apps you own or have permission to test. You are responsible for using Strix ethically and legally."* There is no target allowlist, no ownership proof, no confirmation prompt — `strix --target https://anything.com` just runs. (The hosted app.strix.ai verifies scope upstream; the system prompt even has a **REFUSAL-AVOIDANCE** block telling the model *"NEVER question your authority"* on platform-verified scope — engineered for the SaaS, but it means the OSS tool trusts whatever *you* assert.) **→ Legal exposure is real:** running exploits against systems you don't own can violate the CFAA (US) / cybercrime statutes / GDPR. Only ever point it at hireui or a scratch app you own.
2. **Telemetry is opt-out, default-ON.** Two backends fire unless you `export STRIX_TELEMETRY=0`: **PostHog** (`us.i.posthog.com`) + **Scarf** (`strix.gateway.scarf.sh`). They send model, scan_mode, scan_type, LLM request/token counts + cost, vulnerability **counts by severity**, duration, OS/arch, and a per-run non-persistent session UUID. ⚠️ **README-vs-code discrepancy:** the telemetry README says *"What We Never Collect: … Vulnerability details"* — but the code does send `vulnerability_counts` (critical/high/med/low/info) and token counts. Targets/URLs/PoC bodies are *not* sent, but the severity histogram + token pattern of an internal scan does leave your machine. **Turn it off.**
3. **Install** = `curl -sSL https://strix.ai/install | bash` → downloads a PyInstaller binary to `~/.strix/bin`, edits your shell rc for PATH, pulls the sandbox image. Benign but a `curl|bash` with **no digest pinning / no signature verification**. The inspectable alternative: **`pip install strix-agent`** (source-installable, no shell-rc mutation).
4. **Aggressive-testing collateral** — deep scans can DoS the target (the Ostorlab connection-pool exhaustion). Don't run deep scans against anything you can't afford to knock over; never against production.

**Bottom line:** the sandbox protects *your machine* from the tools; **you** are the only thing protecting *out-of-scope systems* from the agent. Fence accordingly (see the Pilot Methods Menu).

---

## 7. How Strix compares to the corpus (positioning)

- **shannon v45** (`KeygraphHQ/shannon`) — the corpus-**first** autonomous AI web/API pentester (minted as the T5 "AI-pentester" sub-archetype). Strix is the **second instance** (N=2). Deltas: Python + OpenAI Agents SDK (vs TS + Claude Agent SDK); black-box **and** white-box **and** auto-fix (vs white-box focus); Caido MITM sidecar + Kali sandbox + 45-skill progressive disclosure; a CI diff-scope gate; Apache-2.0 (vs shannon's AGPL Lite + commercial Pro). Both benchmark on XBOW-lineage evals at ~96%.
- **SkillSpector v169** (`NVIDIA/SkillSpector`) — the **defensive** counterpart (scans agent-skill packages before install). Strix is the offensive side; together they book-end "AI security tooling" in the corpus. *Different objects* (Strix tests *apps*; SkillSpector vets *skills*).
- **Anthropic-Cybersecurity-Skills v98** — a cybersecurity *skill collection*; Strix's `skills/` dir is the executable analogue, fused into the agent that consumes them.
- **OpenHands v30 / AutoGPT** — the broader T5 "agent-as-application" + Docker-sandbox family Strix belongs to.
- **browser-use v41 / Skyvern v24 / crawl4ai v29** — browser-automation neighbors; Strix uses `agent_browser` for client-side exploitation.
- **Live operator threads it lands on:** multi-agent-orchestration (the Graph of Agents), claude-api-cost-optimization (LiteLLM cost + `--max-budget-usd` + the ~$3.37/challenge anchor), loop-engineering v189 (tool-call/lifecycle termination + maker/checker validation + the CI-gate-as-security-sweeper-loop), and — uniquely — **hireui as a real, ownable test target.**

---

## 8. Honest limitations (from source + independent reviewers)

- The **hard exploit primitives are bundled third-party tools** (nmap/nuclei/sqlmap/Caido/semgrep/Playwright) — Strix is the LLM *orchestration layer* around them; effectiveness tracks the chosen LLM backend.
- **Still labeled Alpha** (PyPI classifier), despite maturity signals.
- **Benchmarks are vendor-run**; no independent head-to-head vs Burp/Nessus; 25% miss rate on hard vuln-chains (XBEN L3).
- Independent reviewers converge on: *"complement, not replace, human pentesting"*; documentation/tutorials still thin; infra-intensive testing can overload targets.
- No hallucination-of-vulns criticism found — the PoC-validation gate is genuinely praised for preventing fake findings ("you can't fake a working exploit").

---

*Sources: source-verified at `e6ca4d2` (README, `system_prompt.jinja`, `core/agents.py`+`execution.py`+`inputs.py`, `tools/agents_graph`+`proxy`+`reporting`+`web_search`+`notes`+`todo`, `runtime/*`, `skills/*`, `report/*`, `telemetry/*`, `scripts/install.sh`, `pyproject.toml`, `benchmarks/README.md`, docs/*) + upstream research (HelpNetSecurity, FreeCodeCamp, Ostorlab, strix.ai/docs.strix.ai). Corpus/collision/identity claims hand-verified per `feedback_wiki_verify_independently_check_collisions`.*
