# (C) Cluster 1: README + Positioning + Shannon Lite Features

> **Sources:** README.md (39.6 KB, 892 lines) + COVERAGE.md (8.5 KB) + LICENSE (AGPL-3.0 33.7 KB) + GitHub repo metadata (WebFetch) + Trendshift badge + sample-reports/
> **Cluster role:** User-facing documentation — installation, features, philosophy, AGPL terms, safety/ethics framing
> **Status:** ✅ Complete

---

## 1. Verbatim positioning

- **Tagline:** *"Shannon — AI Pentester by Keygraph"*
- **Description:** *"Shannon is an autonomous, white-box AI pentester for web applications and APIs. It analyzes your source code, identifies attack vectors, and executes real exploits to prove vulnerabilities before they reach production."*
- **Problem statement:** *"Thanks to tools like Claude Code and Cursor, your team ships code non-stop. But your penetration test? That happens once a year. This creates a massive security gap. For the other 364 days, you could be unknowingly shipping vulnerabilities to production."*
- **Solution positioning:** *"Shannon closes that gap by providing on-demand, automated penetration testing that can run against every build or release."*
- **Core principle (stated explicitly):** *"No Exploit, No Report"* + *"Only vulnerabilities with a working proof-of-concept are included in the final report."*

## 2. Scale signals (GitHub probe)

| Metric | Value |
|--------|-------|
| Stars | **40.1K** |
| Forks | **4.4K** (11.0% ratio) |
| Watchers | 195 |
| Open issues | 17 (tightly-managed) |
| Latest release | **v1.1.0, 2026-04-21** (3 days old at ingestion) |
| License | AGPL-3.0 (33.7 KB full-text LICENSE file) |
| Default branch | main |
| Topics | security-audit / penetration-testing / pentesting / security-automation / security-tools |
| Homepage | [keygraph.io](https://keygraph.io/) |
| Badge | [Trendshift repository 15604](https://trendshift.io/repositories/15604) |
| Created | ~16 months ago (calculated from scale: ~40K / ~2.5K per month) |

## 3. Product line (2-tier open-core)

| Edition | License | Best For |
|---------|---------|----------|
| **Shannon Lite** (this repo) | AGPL-3.0 | Local testing of own applications |
| **Shannon Pro** | Commercial | Organizations needing single AppSec platform (SAST/SCA/secrets/business-logic/pentest with CI/CD + self-hosted) |

> **"This repository contains Shannon Lite, the core autonomous AI pentesting framework. Shannon Pro is Keygraph's all-in-one AppSec platform..."**

## 4. Shannon Lite features (verbatim)

- **Fully Autonomous Operation:** *"A single command launches the full pentest. Shannon handles 2FA/TOTP logins (including SSO), browser navigation, exploitation, and report generation without manual intervention."*
- **Reproducible Proof-of-Concept Exploits:** *"The final report contains only proven, exploitable findings with copy-and-paste PoCs."*
- **OWASP Vulnerability Coverage:** *"Identifies and validates Injection, XSS, SSRF, and Broken Authentication/Authorization."*
- **Code-Aware Dynamic Testing:** *"Analyzes source code to guide attack strategy, then validates findings with live browser and CLI-based exploits."*
- **Integrated Security Tooling:** *"Leverages Nmap, Subfinder, WhatWeb, and Schemathesis during reconnaissance and discovery phases."*
- **Parallel Processing:** *"Vulnerability analysis and exploitation phases run concurrently across all attack categories."*

## 5. 5-phase pipeline architecture (from README)

```
Pre-Recon → Recon → [Vuln × 5 parallel] → [Exploit × 5 parallel] → Report
```

1. **Pre-Reconnaissance** — nmap + subfinder + whatweb + source code scan
2. **Reconnaissance** — attack surface mapping + browser exploration (code ↔ runtime correlation)
3. **Vulnerability Analysis** — 5 parallel agents (injection / xss / auth / authz / ssrf) producing hypothesized exploitable paths
4. **Exploitation** — 5 parallel exploit agents executing PoCs via browser automation + CLI + custom scripts; discard-if-no-PoC
5. **Reporting** — consolidate validated findings; de-dup; severity; remediation; copy-paste PoCs

**"Each scan runs in its own ephemeral Docker container (`docker run --rm`) with a per-invocation Temporal task queue, enabling concurrent scans with different target repositories."**

## 6. Installation / deployment surfaces

**3 distinct deployment surfaces (corpus-first breadth for T5 AI-pentester):**

1. **npx (recommended)** — `npx @keygraph/shannon setup` → `npx @keygraph/shannon start -u <url> -r /path/to/repo`
2. **Clone and Build** — `git clone` → `pnpm install` → `pnpm build` → `./shannon start -u <url> -r <path>`
3. **Self-hosted Pro runner** (commercial tier) — customer data plane + Keygraph control plane

### Prerequisites

- Docker (required even for npx — worker image pulled from Docker Hub ~1 GB)
- Node.js 18+ (for npx)
- pnpm (for Clone+Build)
- **One of 5 AI provider options:**
  - **Anthropic API key** (recommended)
  - **Claude Code OAuth token**
  - **AWS Bedrock** (via `CLAUDE_CODE_USE_BEDROCK=1` + bearer token)
  - **Google Vertex AI** (via service account)
  - **Custom Base URL** (for LiteLLM proxy; *"Only Claude models officially supported"*)

### 3 model tiers (env vars)

- `ANTHROPIC_SMALL_MODEL` — Claude Haiku 4.5 (summarization)
- `ANTHROPIC_MEDIUM_MODEL` — Claude Sonnet 4.6 (security analysis)
- `ANTHROPIC_LARGE_MODEL` — Claude Opus 4.6 (deep reasoning)

## 7. CLI commands + workspaces

```bash
npx @keygraph/shannon setup                    # one-time credential config
npx @keygraph/shannon start -u <url> -r <repo>  # run pentest
npx @keygraph/shannon logs <workspace>         # tail logs
npx @keygraph/shannon status                   # running workers
npx @keygraph/shannon workspaces               # list workspaces
npx @keygraph/shannon stop [--clean]           # stop + optional full cleanup
npx @keygraph/shannon uninstall                # remove ~/.shannon/
```

**Workspaces + resume:**
- Every run creates workspace (auto-named or `-w <name>`)
- Stored in `./workspaces/` (local) or `~/.shannon/workspaces/` (npx)
- Resume by passing same `-w` — Shannon detects completed agents via `session.json`
- Each agent checkpointed via git commit — resume from clean validated state
- Temporal Web UI at `http://localhost:8233`

**Options:** `-c <config>` / `-o <output>` / `-w <name>` / `--pipeline-testing` (minimal prompts, 10s retries) / `--debug` (preserve worker container post-exit)

## 8. Configuration (YAML) — auth + rules

Example config structure (from README):

```yaml
description: "Next.js e-commerce app on PostgreSQL..."

authentication:
  login_type: form
  login_url: "https://your-app.com/login"
  credentials:
    username: "test@example.com"
    password: "yourpassword"
    totp_secret: "LB2E2RX7XFHSTGCK"  # 2FA auto-handled
  login_flow:
    - "Type $username into the email field"
    - "Type $password into the password field"
    - "Click the 'Sign In' button"
  success_condition:
    type: url_contains
    value: "/dashboard"

rules:
  avoid:
    - description: "AI should avoid testing logout"
      type: path
      url_path: "/logout"
  focus:
    - description: "AI should emphasize testing API endpoints"
      type: path
      url_path: "/api"

pipeline:
  retry_preset: subscription     # 6h max backoff, 100 retries
  max_concurrent_pipelines: 2    # 1-5, default 5
```

Supports form / SSO / API / basic auth. TOTP automatic via `generate-totp` CLI (per CLAUDE.md).

## 9. Sample reports (in `sample-reports/` directory)

**3 real pentest reports shipped in repo** — corpus-first proof-of-capability artifact in a T5:

| Target | Finding count | Notable |
|--------|---------------|---------|
| **OWASP Juice Shop** (37.8 KB report) | 20+ vulns | Authentication bypass + full user DB exfiltration via SQLi + privilege-escalation + IDOR + SSRF |
| **c{api}tal API** (Checkmarx, 25 KB report) | ~15 critical+high | Root command injection via denylist bypass + JWT auth bypass + Mass Assignment privilege escalation + zero XSS false-positives |
| **OWASP crAPI** (37.9 KB report) | 15+ critical+high | Multiple JWT attacks (alg confusion / alg:none / weak key) + full PostgreSQL compromise + SSRF forwarding auth tokens + zero XSS false-positives |

All 3 share "zero false-positive" demonstrations and production-grade formatting.

## 10. Benchmark

*"Shannon Lite scored 96.15% (100/104 exploits) on a hint-free, source-aware variant of the XBOW security benchmark."*

**[Full results with detailed agent logs at KeygraphHQ/xbow-validation-benchmarks](https://github.com/KeygraphHQ/xbow-validation-benchmarks/blob/main/xben-benchmark-results/)**

**Corpus-first:** XBOW benchmark in Storm Bear corpus. 8th data point for Pattern #8 Research-Benchmark (prior: WebBench Skyvern / WebVoyager Skyvern / SWE-Bench OpenHands / ICLR papers / ACL papers / ICSE papers / course leaderboards / SkillsBench). Pentesting-domain benchmark new category.

## 11. AGPL-3.0 terms (verbatim summary from README)

- *"Shannon Lite is released under the GNU Affero General Public License v3.0 (AGPL-3.0)"*
- *"This license allows you to: Use it freely for all internal security testing. Modify the code privately for internal use without sharing your changes."*
- *"The AGPL's sharing requirements primarily apply to organizations offering Shannon as a public or managed service (such as a SaaS platform). In those specific cases, any modifications made to the core software must be open-sourced."*

**Practical implication:** Private internal use = no derivative-disclosure. Offering as SaaS = must open-source modifications.

## 12. Ethical framing (⚠️ prominent in README)

**7 explicit disclaimer sections:**

1. **Potential for Mutative Effects & Environment Selection** — *"DO NOT run Shannon on production environments."* "Sandboxed, staging, or local development environments where data integrity is not a concern." Recommend VM isolation.
2. **Legal & Ethical Use** — *"You must have explicit, written authorization from the owner of the target system before running Shannon. Unauthorized scanning and exploitation of systems you do not own is illegal and can be prosecuted under laws such as the Computer Fraud and Abuse Act (CFAA). Keygraph is not responsible for any misuse of Shannon."*
3. **LLM & Automation Caveats** — human oversight required; Claude-only officially supported; Lite has LLM-context-window scope limits
4. **Scope of Analysis** — targets exploitable vulns (Auth / Injection / XSS / SSRF); does NOT cover vulnerable-dependency CVEs or static-only issues (Pro tier focus)
5. **Cost & Performance** — **1-1.5 hours per run**; **~$50/run with Claude Sonnet 4.5**
6. **Windows Antivirus False Positives** — Windows Defender may flag exploit code in reports; use Docker/WSL2
7. **Security Considerations** — *"do not point it at untrusted or adversarial codebases. Like any AI-powered tool that reads source code, Shannon Lite is susceptible to prompt injection from content in the scanned repository."*

**Corpus-first at T5:** Most-prominent ethical framing in any T5 wiki (surpasses Skyvern's 3-section disclaimer + paperclip v14's alignment-theory framing).

## 13. COVERAGE.md — explicit WSTG mapping

COVERAGE.md (8.5 KB) maps Shannon Lite capabilities to **OWASP Web Security Testing Guide (WSTG)** checklist. Explicit ✅/blank per WSTG test ID. Summary of covered categories:

- **WSTG-INFO** (Information Gathering): 6/10 ✅
- **WSTG-CONF** (Configuration): 2/14 ✅ (network infra + subdomain takeover)
- **WSTG-IDNT** (Identity): 5/5 ✅ (full coverage)
- **WSTG-ATHN** (Authentication): 9/11 ✅ (near-full coverage)
- **WSTG-ATHZ** (Authorization): 5/5 ✅ (full coverage)
- **WSTG-SESS** (Session Management): 8/11 ✅
- **WSTG-INPV** (Input Validation): 7/20 ✅ (reflected XSS / stored XSS / SQLi / code-injection / command-injection / SSTI / SSRF)
- **WSTG-CRYP** (Cryptography): 2/4 ✅
- **WSTG-BUSLOGIC** (Business Logic): 0/10 — **explicit Pro-tier focus**
- **WSTG-CLIENT** (Client-side): 6/14 ✅
- **WSTG-APIT** (API Testing): 3/3 ✅ (full coverage including GraphQL)

**Corpus-first at T5:** Explicit OWASP WSTG mapping file = transparent capability-claim discipline.

## 14. Branding divergence observation (Pattern #58 4th data point)

**Top of README (verbatim):**
> *"[📢 Sunsetting Router Mode (claude-code-router)`. →](https://github.com/KeygraphHQ/shannon/discussions/301)"*

**Analysis:**
- `claude-code-router` experimental integration sunsetting
- Migration path: Anthropic-compatible proxy (LiteLLM)
- Public discussion notice (#301) = feature-deprecation-with-transparent-notice
- **4th observation data point for Pattern #58 Branding-Package Divergence** (after OMC v27 `oh-my-claude-sisyphus` npm divergence + ruflo v42 package vs display / rowboat v43 website/website-ng / magika v44 website-transition)
- Sub-variant sub-classification: **feature-deprecation-with-public-discussion-notice** (distinct from branding-divergence and website-transition observations)
- Stays OBSERVATION-TRACK (promoted v42 mini-audit); episodic, not architectural

## 15. Corpus-firsts in Cluster 1

1. AI-pentester T5 sub-archetype (9th T5)
2. White-box source-code-aware dynamic testing at T5 scope
3. 4 security-tool integration suite (Nmap + Subfinder + WhatWeb + Schemathesis)
4. XBOW benchmark usage (pentesting-domain benchmark family)
5. 3 sample-reports in repo (Juice Shop + c{api}tal + crAPI)
6. Most-prominent 7-section ethical framing at T5
7. Explicit OWASP WSTG capability-mapping file (COVERAGE.md)
8. Temporal Web UI bundled for scan monitoring
9. Dedicated SHANNON-PRO.md 26KB Pro-tier documentation file (referenced from README; fully documented Cluster 3)
10. 5 AI provider options (Anthropic direct + Claude Code OAuth + AWS Bedrock + Google Vertex + Custom Base URL)
11. 3-tier model routing (small/medium/large via env vars)
12. "POC or it didn't happen" / "No Exploit, No Report" principle explicit
13. Workspaces + git-checkpoint resume mechanism
14. `claude-code-router` feature-deprecation-with-public-notice (Pattern #58 4th observation)
15. Issues-only-no-PRs governance at 40K scale

## Cross-wiki links

- Peers: [[Skyvern]] v24 (T5 AGPL browser) / [[browser-use]] v41 (T5 MIT browser) / [[OpenHands]] v30 (T5 SWE academic-commercial) / [[DeepTutor]] v38 (T5 education) / [[rowboat]] v43 (T5 personal-productivity) / [[deer-flow]] v9 + [[autoresearch]] v10 + [[paperclip]] v14 (earlier T5)
- Pattern #31 peers: [[fish-speech]] v20 / [[Skyvern]] v24 / [[OpenHands]] v30 / [[crawl4ai]] v29 / [[GitNexus]] v33 / [[DeepTutor]] v38 / [[browser-use]] v41
- Pattern #58 peers: [[oh-my-claudecode]] v27 / [[ruflo]] v42 / [[rowboat]] v43 / [[magika]] v44
