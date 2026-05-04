# (C) Entity: Keygraph Ecosystem + Shannon Pro

> **Type:** Entity page (ecosystem + commercial)
> **Wiki:** shannon v45
> **Role in wiki:** Commercial/ecosystem entity — Keygraph company + Shannon Pro commercial tier + Tower managed service + open-core playbook

---

## 1. Identity

- **Publisher:** Keygraph (commercial startup)
- **Homepage:** [keygraph.io](https://keygraph.io/)
- **Tagline:** *"Find real vulnerabilities. Prove they're exploitable."*
- **Headline:** *"The Unified AppSec Platform"*
- **Compliance:** SOC 2 Type I certified
- **Social:** Twitter [@KeygraphHQ](https://twitter.com/KeygraphHQ) / LinkedIn [Keygraph](https://linkedin.com/company/keygraph)
- **Contact:** [shannon@keygraph.io](mailto:shannon@keygraph.io)
- **Team:** not publicly disclosed (no named founders via keygraph.io WebFetch; "About Us" page linked but not ingested)
- **HQ location:** not specified
- **Funding:** not disclosed

## 2. Product portfolio (2 products)

| Product | Description |
|---------|-------------|
| **Shannon** | AI-powered AppSec + pentesting platform. 2-tier: Shannon Lite (AGPL-3.0 OSS, this repo) + Shannon Pro (commercial). |
| **Tower** | Managed security service offering full Keygraph platform + fractional vCISO support. |

**Tower = corpus-first managed-vCISO-service tier at T5 AI-pentester scope.**

## 3. Commercial segmentation

- **Enterprise:** large orgs needing CI/CD + SSO + compliance
- **Startup:** startup stage (OSS lead-gen pathway)
- **Verticals:** Fintech & Banking / Healthcare / SaaS & Cloud
- **Use cases:** CI/CD Security / Penetration Testing / Compliance & Audit

## 4. Customer case studies

**3 customer logos** cited on keygraph.io:
- **Optexity**
- **Scowtt Inc.**
- **Mesmer**

**1 verbatim testimonial** (João De Paula, CEO & Co-Founder, Mesmer):
> *"If you're serious about not just compliance but actual security, Keygraph is the way to go!"*

## 5. Shannon Pro positioning

**From SHANNON-PRO.md opening:**
> *"Shannon Pro is Keygraph's comprehensive AppSec platform, combining SAST, SCA, secrets scanning, business logic security testing, and autonomous pentesting in a single correlated workflow."*

**3 pillars:**
1. **Agentic static analysis** (CPG-based data flow + SCA reachability + secrets + business logic)
2. **Static-dynamic correlation** (static findings → dynamic exploitation queue → PoC per finding)
3. **Enterprise deployment** (self-hosted runner + CI/CD + GitHub PR scan + service boundaries)

## 6. Shannon Pro Stage 1 — 5 SAST capabilities

### 6.1 Data Flow Analysis (CPG-based)

- **Code Property Graph:** AST + Control Flow Graph + Program Dependence Graph unified
- **3 phases:** Source/Sink Extraction → Path Tracing with Contextual Reasoning (LLM at every node) → Path Validation (autonomous Claude agent confidence-scored)
- **Key differentiator:** context-dependent sanitization analysis (not hard-coded safe-function list)

### 6.2 Point Issue Detection

LLM-based single-location vulns: weak crypto / hardcoded creds / insecure config / missing security headers / weak RNG / disabled cert validation / permissive CORS.

### 6.3 Business Logic Security Testing (corpus-first at T5)

**4-phase pipeline:**
1. **Invariant Discovery** (LLM derives business-logic invariants)
2. **Fuzzer Generation** (adversarial scenarios per invariant, not random)
3. **Violation Detection** (execute against stubbed test env)
4. **Exploit Synthesis** (full PoC with reproduction steps + security impact)

**Documented example:** CWE-639 Cross-Tenant Data Access IDOR — Org B user accesses Org A docs via document ID enumeration → complete multi-tenant isolation breach.

### 6.4 SCA with Reachability Analysis

4-step CPG-reachability process distinguishes reachable CVEs from noise. Framework-level uses detection + function-level CPG node query + entry-point trace.

### 6.5 Secrets Detection (3-tier)

Regex baseline + LLM (dynamic/custom/obfuscated) + **liveness validation** (read-only API auth check).

## 7. Additional Pro capabilities

- **Boundary Analysis** — monorepo scoping by service/microservice/team routing (corpus-first at T5)
- **False Positive Tagging** — mark as FP → auto-flagged on subsequent scans
- **Compliance Evidence** — automated SOC 2 + HIPAA evidence generation (bridges compliance ↔ continuous-security)
- **OWASP alignment** — WSTG + Top 10 broadly aligned

## 8. Static-Dynamic Correlation (the core differentiator)

**Flow:**
1. Static analysis produces findings
2. Enrichment adds priority + confidence + app context
3. CWEs → 5 attack domains (best-fit heuristic; multi-domain routed to most-exploitation-relevant; business logic routed with static context preserved)
4. Exploit agents attempt real PoC attacks against running application
5. Confirmed exploits traced back to exact source code location

**Developer receives:** proof-of-reality + line-of-code-to-fix (both stages correlated).

**Corpus-first architectural pattern at T5 AI-pentester.**

## 9. Deployment model — Self-hosted Runner

**Split (verbatim from SHANNON-PRO.md):**
- **Customer data plane:** clones code + executes scans + all LLM API calls using customer keys
- **Keygraph control plane:** job orchestration + scan scheduling + reporting UI
- Control plane receives ONLY aggregate findings (no code / no raw LLM content)

**Parallel:** GitHub Actions self-hosted runners architecture.

**Corpus-first self-hosted-runner + code-never-leaves-customer-network model at T5.**

## 10. Security architecture (enterprise-grade)

- **Per-organization isolated compute** (ECS managed or customer-provisioned self-hosted)
- **Ephemeral code handling** — workspace deleted immediately post-scan; disconnected cleanup runs regardless of scan outcome
- **Encrypted storage** — code snippets encrypted pre-DB-write; S3 deliverables encrypted at rest; org-specific buckets
- **Network isolation** — private subnets + org-specific security groups

**Corpus-first enterprise-security documentation at T5** (rivals commercial SaaS like GitHub Enterprise / HashiCorp Vault).

## 11. 2-tier capability matrix (Lite vs Pro)

| Capability | Shannon Lite | Shannon Pro |
|------------|--------------|-------------|
| Licensing | AGPL-3.0 (OSS) | Commercial |
| Static Analysis | Code review prompting | Full agentic SAST + SCA + secrets + business-logic |
| Dynamic Testing | Autonomous pentest | + static-dynamic correlation |
| Analysis Engine | Code review prompting | CPG-based data flow |
| Business Logic | N/A | Automated invariant discovery + fuzzer + exploit synthesis |
| Integration | Manual CLI | Native CI/CD + GitHub PR scanning + enterprise support + self-hosted runner |
| Deployment | CLI | Managed cloud OR self-hosted runner |
| Boundary Analysis | N/A | Automatic + team routing |
| **Best For** | Local testing of own apps | Enterprise AppSec posture mgmt |

## 12. Community + Support

- **1:1 Office Hours:** Thursdays, 2 time zones (US/EU 10am PT + Asia 2pm IST). Free 15-min booking via Cal.com ([link](https://cal.com/george-flores-keygraph/shannon-community-office-hours))
- **Discord:** [discord.gg/cmctpMBXwE](https://discord.gg/cmctpMBXwE)
- **Bug reports:** GitHub Issues
- **Feature requests:** GitHub Discussions
- **Shannon Pro Inquiry:** [Cal.com/team/keygraph/shannon-pro](https://cal.com/team/keygraph/shannon-pro)

**⚠️ Contributing policy:** *"At this time, we're not accepting external code contributions (PRs). Issues are welcome for bug reports and feature requests."*

**Corpus-first at 40K-star T5:** Issues-only-no-PRs governance. Unusual — most T5s at similar scale accept PRs. Aligns with AGPL commercial-startup strategy (control contributor-license-grants).

## 13. Commercial playbook (open-core 2-tier + Tower)

**Pattern #31 Open-Core Commercial Entity — 8th data point observations:**

1. **OSS core** (AGPL-3.0 copyleft) = protects against vendor appropriation + preserves community access
2. **Proprietary Pro tier** = domain-specific differentiators (CPG / business-logic-fuzzer / static-dynamic correlation / self-hosted runner)
3. **Managed service tier (Tower)** = fractional vCISO + managed full Keygraph platform
4. **Compliance wrapper** = SOC 2 Type I certification
5. **Transparent capability docs** = COVERAGE.md (Lite) + SHANNON-PRO.md (Pro) 26 KB dedicated
6. **Sample-reports in repo** = proof-of-capability artifact
7. **Customer testimonials** = named customers (Optexity / Scowtt / Mesmer) + 1 CEO quote
8. **Commercial funnel** = Cal.com booking + email + Discord + office hours

**Observational at v45:** Shannon's **most-detailed Pro-tier documentation file** (SHANNON-PRO.md 26 KB) is a corpus-first Pattern #31 sub-variant-strengthening observation. If N=2 of similar mature-open-core-with-dedicated-Pro-docs emerges in future wikis → formal sub-variant formalization candidate.

## 14. Pattern implications

### Pattern #31 Open-Core Commercial Entity (CONFIRMED v24) — N=8 STRENGTHENING

8 data points: fish-speech v20 / Skyvern v24 / OpenHands v30 / crawl4ai v29 / GitNexus v33 / DeepTutor v38 / browser-use v41 / **shannon v45**.

### Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v36 mini-audit) — N=7 STRENGTHENING

7 data points (v36 onward): VoltAgent awesome-design-md / Frank Fiegel awesome-mcp-servers / BMAD-METHOD / Keygraph / [prior confirmed 3] + shannon. Comprehensive funnel stack at shannon: 2-product + Tower managed + 3 testimonials + SOC 2 + Cal.com + office hours + Discord + Trendshift.

### Pattern #17 Ecosystem-Layer variant 3 commercial-startup — STRENGTHENING

Keygraph 2-product portfolio (Shannon + Tower) + customer named + compliance + enterprise/startup/vertical segmentation = full variant 3 commercial-startup ecosystem data point.

## 15. Corpus-firsts contributed

1. Most-detailed Pro-tier documentation file (SHANNON-PRO.md 26 KB) at T5
2. Tower managed vCISO service tier at T5 AI-pentester (managed-service sibling to Pro)
3. SOC 2 Type I certification explicit at commercial-startup Shannon scope
4. CPG (Code Property Graph) architecture documented at T5 AI-pentester
5. Static-dynamic correlation pipeline architectural pattern
6. Business-logic invariant-fuzzer-generation 4-phase pipeline
7. SCA with CPG reachability at T5
8. Secrets detection with liveness validation (read-only API verification)
9. Boundary analysis for monorepo scoping at T5
10. False-positive tagging as first-class feature
11. Self-hosted runner model (customer data plane + Keygraph control plane) at T5
12. Encrypted-at-rest code snippets + org-specific S3 buckets + private subnet enterprise-security documentation
13. Compliance evidence generation (SOC 2 / HIPAA) as Pro feature
14. Issues-only-no-PRs governance at 40K-star T5
15. 3 named customer testimonials at commercial-startup T5
16. CWE-639 cross-tenant IDOR full end-to-end documented business-logic example

## 16. Cross-references

- **Core product peer:** [[Shannon Lite core]] (same wiki)
- **T5 9-way meta:** [[T5 9-way AI-pentester meta]] (same wiki)
- **Pattern #31 peers (8 data points):** [[fish-speech]] v20 / [[Skyvern]] v24 / [[OpenHands]] v30 / [[crawl4ai]] v29 / [[GitNexus]] v33 / [[DeepTutor]] v38 / [[browser-use]] v41
- **Pattern #50 peers:** [[awesome-design-md]] v25 / [[awesome-mcp-servers]] v31 / [[BMAD-METHOD]] v11 / [[pi-mono]] v36
- **Self-hosted-runner peer:** [[GitNexus]] v33 (self-hosted Enterprise) — Shannon's split-architecture is more-detailed documentation
- **Academic-commercial fusion peer:** [[OpenHands]] v30 (UIUC + CMU co-founders + All Hands AI) — Shannon is commercial-only (no disclosed academic lineage)
- **2-tier-with-dedicated-Pro-docs peer:** none (corpus-first)
