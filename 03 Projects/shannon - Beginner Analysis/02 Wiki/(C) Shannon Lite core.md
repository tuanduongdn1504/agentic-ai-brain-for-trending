# (C) Entity: Shannon Lite — Core Product

> **Type:** Entity page (product)
> **Wiki:** shannon v45
> **Role in wiki:** Primary entity — autonomous AI pentester (Shannon Lite, AGPL-3.0, this repo)

---

## 1. Identity

- **Full name:** Shannon Lite (the OSS core framework; "Shannon" used informally in README)
- **Repo:** [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- **License:** AGPL-3.0
- **Publisher:** Keygraph (commercial startup; keygraph.io; SOC 2 Type I)
- **Scope:** T5 Agent-as-application — 9th T5 entrant + NEW AI-pentester sub-archetype

## 2. Elevator pitch (verbatim)

> *"Shannon is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production."*

Core principle: **"POC or it didn't happen" / "No Exploit, No Report"** — only exploitable findings with copy-paste PoC reach the final report.

## 3. Scale (GitHub, 2026-04-24)

| Metric | Value |
|--------|-------|
| Stars | **40.1K** (#9 approx in corpus) |
| Forks | **4.4K** (11.0%) |
| Watchers | 195 |
| Open issues | 17 (tight governance) |
| Latest release | v1.1.0 (2026-04-21) |
| Age | ~16 months (created ~late 2024) |
| Trendshift badge | repository 15604 |
| Primary lang | TypeScript |
| Trajectory | ~2.5K stars/month organic commercial-growth |

## 4. What Shannon Lite does

**Single-command autonomous web-app + API pentest** (from README Features):

1. **Fully Autonomous:** single command → full pentest (handles 2FA/TOTP logins including SSO / browser navigation / exploitation / report generation — no manual intervention)
2. **Reproducible PoC:** final report = only proven exploitable findings with copy-paste PoCs
3. **OWASP coverage:** Injection + XSS + SSRF + Broken Authentication/Authorization (+ more in dev)
4. **Code-aware dynamic:** analyzes source code → guides attack strategy → validates with live browser + CLI exploits
5. **Integrated security tooling:** Nmap + Subfinder + WhatWeb + Schemathesis during recon
6. **Parallel processing:** vuln analysis + exploitation run concurrently across 5 attack categories (pipelined parallel)

## 5. 5-phase pipeline

```
Pre-Recon → Recon → [Vuln × 5 parallel] → [Exploit × 5 parallel] → Report
```

| Phase | Agents | Role |
|-------|--------|------|
| 1. Pre-Reconnaissance | 1 (pre-recon-code) | External scans (Nmap + Subfinder + WhatWeb) + source code analysis |
| 2. Reconnaissance | 1 (recon) | Attack surface mapping; browser exploration; code ↔ runtime correlation |
| 3. Vulnerability Analysis | 5 parallel (injection / xss / ssrf / auth / authz) | Hypothesize exploitable paths; produce exploitation queue |
| 4. Exploitation | 5 parallel (conditional — skipped if queue empty) | Execute real-world attacks; classify EXPLOITED / POTENTIAL / FALSE POSITIVE |
| 5. Reporting | 1 (report-executive) | Consolidate validated findings; de-dup; severity; copy-paste PoCs |

**Pipelined-parallel execution:** when vuln agent for a domain completes → corresponding exploit agent starts immediately (doesn't wait for all vuln agents).

## 6. Agent methodology (5 vuln-analysis domains, from SHANNON-PRO.md)

| Agent | Approach | Scope |
|-------|----------|-------|
| **Injection** | Source → Sink taint | SQL / command / file / template / deserialization sinks |
| **XSS** | Sink → Source taint | HTML rendering contexts: innerHTML / document.write / event handlers / eval |
| **SSRF** | Sink → Source taint | HTTP clients / raw sockets / URL openers / headless browsers |
| **Auth** | Guard validation | Rate limiting / session management / token entropy / password hashing / HSTS / SSO OAuth |
| **Authz** | Guard validation | Horizontal (ownership) / vertical (role) / context/workflow violations |

## 7. Installation (3 surfaces)

**Surface 1: npx (recommended)**
```bash
npx @keygraph/shannon setup            # interactive wizard
npx @keygraph/shannon start -u https://your-app.com -r /path/to/repo
```

**Surface 2: Clone and Build**
```bash
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon
echo "ANTHROPIC_API_KEY=your-key" > .env
pnpm install && pnpm build
./shannon start -u https://your-app.com -r /path/to/repo
```

**Surface 3: Self-hosted Pro runner** (commercial — see Entity 2)

### Prerequisites
- Docker (always required — worker image ~1 GB from Docker Hub)
- Node.js 18+ (for npx)
- pnpm (for Clone+Build)
- One of 5 AI providers: Anthropic direct / Claude Code OAuth / AWS Bedrock / Google Vertex / Custom Base URL

## 8. 13 agents + 13 prompt files

| Phase | Prompt File | Size |
|-------|-------------|------|
| Pre-Recon | pre-recon-code.txt | 27.3 KB |
| Recon | recon.txt | 27.3 KB |
| Vuln | vuln-injection.txt / vuln-xss.txt / vuln-ssrf.txt / vuln-auth.txt / vuln-authz.txt | 18-25 KB each |
| Exploit | exploit-injection.txt / exploit-xss.txt / exploit-ssrf.txt / exploit-auth.txt / exploit-authz.txt | 24-28 KB each |
| Report | report-executive.txt | 7.1 KB |

Plus 5 shared partials (`apps/worker/prompts/shared/`): `_exploit-scope.txt` / `_rules.txt` / `_target.txt` / `_vuln-scope.txt` / `login-instructions.txt`.

**Total prompt corpus:** ~260 KB of carefully-engineered agent prompts.

## 9. Architectural highlights (from Cluster 2)

- **TypeScript monorepo** (pnpm-workspaces + Turborepo + Biome + tsdown)
- **2 apps:** `apps/cli` (`@keygraph/shannon` published to npm) + `apps/worker` (`@shannon/worker` private)
- **Temporal.io** orchestration (durable workflow + crash recovery + queryable progress + intelligent retry)
- **Ephemeral Docker containers** via `docker run --rm` — one per scan
- **Per-invocation Temporal task queue** — activities never land on worker with wrong repo mounted
- **Target repo mounted READ-ONLY** inside worker container
- **Chainguard Wolfi runtime** for minimal hardened base
- **Workspaces + git-checkpoint resume** — each agent checkpointed via git commit
- **Claude Agent SDK** (`@anthropic-ai/claude-agent-sdk` ^0.2.38) with `maxTurns: 10_000` + `bypassPermissions`
- **Playwright CLI** for browser automation with session isolation
- **generate-totp** CLI for automatic 2FA handling
- **Prompt snapshots** per-workspace for reproducibility
- **Result<T,E> + ErrorCode + ActivityLogger DI** — Temporal-agnostic testable service layer

## 10. Cost + performance profile (from README Disclaimers)

- **Wall-clock time:** 1-1.5 hours per full run
- **API cost:** ~**$50 per run** (Claude Sonnet 4.5)
- **Sandbox recommendation:** VM or dev/staging environment (never production — mutative effects intentional)

## 11. Benchmark result

**96.15% (100/104 exploits) on hint-free source-aware XBOW security benchmark.**

Full results at [KeygraphHQ/xbow-validation-benchmarks](https://github.com/KeygraphHQ/xbow-validation-benchmarks/).

**Corpus-first:** XBOW is pentesting-domain benchmark (Pattern #8 Research-Benchmark 8th data point — new benchmark family).

## 12. Coverage vs OWASP WSTG (from COVERAGE.md)

Full coverage maps explicitly; summary:
- Full coverage ✅: WSTG-IDNT (5/5) + WSTG-ATHZ (5/5) + WSTG-APIT (3/3)
- Near-full: WSTG-ATHN (9/11) + WSTG-SESS (8/11)
- Selective: WSTG-INFO (6/10) + WSTG-INPV (7/20) + WSTG-CLNT (6/14) + WSTG-CRYP (2/4)
- **Explicitly deferred to Pro:** WSTG-BUSLOGIC (0/10 — Pro's invariant-fuzzer pipeline owns this)

## 13. Ethical framing

**⚠️ Shannon requires explicit written authorization from target-system owner** (CFAA compliance). Shannon is **active exploit execution**, not passive scanning. Mutative effects possible. **DO NOT run on production.** Recommended VM isolation.

**AGPL derivative disclosure:** Internal use = no disclosure. Offering Shannon as SaaS = must open-source modifications.

**Prompt injection risk:** Shannon reads source code → susceptible to prompt injection from malicious repo contents. Don't point at adversarial codebases.

## 14. Corpus-firsts contributed

1. AI-pentester T5 sub-archetype (9th)
2. White-box source-code-aware dynamic testing at T5
3. 4 security-tool integration suite (Nmap + Subfinder + WhatWeb + Schemathesis)
4. XBOW benchmark (pentesting-domain family; Pattern #8 8th data point)
5. Temporal.io orchestration at T5
6. Pipelined-parallel execution (exploit starts per-domain-vuln-completion, not all-complete-first)
7. Autonomous 2FA/TOTP/SSO agent login handling
8. Read-only target mount + ephemeral container + per-scan task queue isolation
9. "POC or it didn't happen" principle + explicit EXPLOITED/POTENTIAL/FALSE-POSITIVE classification
10. Workspaces + git-checkpoint resume mechanism
11. Prompt snapshots per-workspace for reproducibility
12. ~260 KB prompt corpus (13 prompt files) at T5
13. Chainguard Wolfi runtime (hardened minimal Docker base)
14. 3 sample reports shipped in repo (Juice Shop / c{api}tal / crAPI)
15. Most-prominent 7-section ethical framing at T5

## 15. Cross-references

- **Commercial tier:** [[Keygraph ecosystem and Shannon Pro]] (same wiki)
- **T5 9-way meta:** [[T5 9-way AI-pentester meta]] (same wiki)
- **Closest T5 peers:**
  - [[Skyvern]] v24 — T5 AGPL commercial browser (Pattern #31 founding N=2; commercial-entity archetype precedent)
  - [[browser-use]] v41 — T5 MIT browser-viral (Pattern #48 promotion peer)
  - [[OpenHands]] v30 — T5 SWE academic-commercial (Pattern #31 N=3)
  - [[DeepTutor]] v38 — T5 education (YELLOW primitive-count precedent)
  - [[rowboat]] v43 — T5 personal-productivity
  - [[deer-flow]] v9 / [[autoresearch]] v10 / [[paperclip]] v14 — earlier T5s
- **Pattern peers:**
  - Pattern #31 (Open-Core Commercial Entity): 8th data point; joins fish-speech v20 / Skyvern v24 / OpenHands v30 / crawl4ai v29 / GitNexus v33 / DeepTutor v38 / browser-use v41
  - Pattern #29 (AGPL-3.0): 3rd project-scope AGPL after Skyvern v24 + TrendRadar v19 GPL-3.0 (non-permissive sub-family)
  - Pattern #58 (Branding Divergence): 4th observation (claude-code-router sunset)
  - Pattern #18 (Agent Runtime Standardization, MCP extended): selective MCP (TOTP-only in Pro) confirms ~70-75% adoption observation
- **Tool/runtime peers:**
  - Playwright: [[Skyvern]] v24 / [[browser-use]] v41 — Shannon uses Playwright CLI differently (pentesting tool not primary automation)
  - Claude Agent SDK: Shannon uses directly with `bypassPermissions`; other T5s use multi-provider abstractions
