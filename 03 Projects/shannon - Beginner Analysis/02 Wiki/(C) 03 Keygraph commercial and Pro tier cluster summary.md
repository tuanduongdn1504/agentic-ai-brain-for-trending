# (C) Cluster 3: Keygraph Commercial + Shannon Pro + Pro-tier Documentation

> **Sources:** SHANNON-PRO.md (26.2 KB, 256 lines) + keygraph.io WebFetch + README Product Line section + README Community/Support + sample-reports/ directory (3 real pentests)
> **Cluster role:** Commercial positioning + Pro-tier architecture + open-core 2-tier strategy + ecosystem playbook
> **Status:** ✅ Complete

---

## 1. Keygraph company positioning (from keygraph.io WebFetch)

- **Headline:** *"The Unified AppSec Platform"*
- **Tagline:** *"Find real vulnerabilities. Prove they're exploitable."*
- **Positioning:** Unified application security platform combining AI pentesting + static analysis + dependency scanning + secrets detection + business logic security testing.

**Compliance:** **SOC 2 Type I certified.**

**Key differentiators claimed (verbatim):**
- *"Real exploits, not false positives"*
- *"Autonomous pentesting across 13 specialized agents in 5 phases"*
- *"Code Property Graph transformation with data flow analysis"*
- *"Pentest-grade reports with reproducible proof-of-concept exploits"*

## 2. Keygraph 2-product portfolio

| Product | Description |
|---------|-------------|
| **Shannon** | AI-powered AppSec + pentesting platform (Lite AGPL OSS + Pro commercial) |
| **Tower** | Managed security service offering full Keygraph platform + fractional vCISO support |

**Tower = corpus-first managed-vCISO-service tier at T5 AI-pentester.** Bridges product + services.

## 3. Commercial positioning

- **Enterprise focus** (mentioned for Enterprise segment)
- **Startup-friendly** (Startup stage)
- **Industry-specific verticals:** Fintech & Banking / Healthcare / SaaS & Cloud
- **Use cases:** CI/CD Security / Penetration Testing / Compliance & Audit

## 4. Customer case studies (from keygraph.io)

**3 customer logos** displayed:
- **Optexity**
- **Scowtt Inc.**
- **Mesmer**

**1 named testimonial** (attributed to João De Paula, CEO & Co-Founder of Mesmer):
> *"If you're serious about not just compliance but actual security, Keygraph is the way to go!"*

**Team/Founders:** Not publicly disclosed via keygraph.io (no named leadership in fetched content). "About Us" page linked but not ingested. **HQ location:** Not specified.

## 5. Shannon Pro positioning (SHANNON-PRO.md 26KB)

**Opening framing (verbatim):**
> *"Shannon Pro is Keygraph's comprehensive AppSec platform, combining SAST, SCA, secrets scanning, business logic security testing, and autonomous pentesting in a single correlated workflow."*

**Three-pillar value prop:**
1. **Agentic static analysis:** CPG-based data flow + SCA with reachability + secrets detection + business logic security testing
2. **Static-dynamic correlation:** static findings fed into dynamic pipeline + exploited against running application → every reported vuln has working PoC
3. **Enterprise deployment:** self-hosted runner (code + LLM calls never leave customer infrastructure) + CI/CD integration + GitHub PR scanning + service boundary detection

## 6. Problem framing (why open-core + Pro tier)

**From SHANNON-PRO.md §"The Problem: Fragmented AppSec and Alert Fatigue":**
> *"Modern engineering teams face two compounding security challenges. First, traditional static analysis tools (SCA, SAST, and secrets scanners) operate without context, producing high volumes of false positives that erode developer trust. Second, penetration testing remains an expensive, periodic exercise that cannot keep pace with continuous deployment."*

**Result (claimed):** *"A fragmented security posture where static tools cry wolf, dynamic assessments arrive too late, and engineering teams treat security as compliance theater rather than a source of genuine protection."*

**Pro solution:** *"Shannon Pro addresses both problems in a single platform by replacing pattern-based static analysis with LLM-powered reasoning and augmenting it with a fully autonomous AI pentester that validates findings at runtime."*

## 7. Shannon Pro Stage 1 — Agentic Static Analysis (5 capabilities)

### 7.1 SAST: Data Flow Analysis (CPG-based)

**Code Property Graph (CPG):**
- Unified structure combining AST + CFG (control flow graph) + PDG (program dependence graph)
- Nodes = program constructs; edges = syntactic + control-flow + data-dependence
- **Corpus-first CPG at T5** — prior CPG peer was GitNexus v33 at T4 scope (knowledge-graph bridge), different role

**3 phases:**
1. **Source and Sink Extraction** — deterministic pattern matching baseline + LLM agent discovers custom patterns + filtering agent removes test/mock fixtures
2. **Path Tracing with Contextual Reasoning** — LLM analyzes EVERY node along path for sanitization + context-specific sufficiency (vs hard-coded safe-function list)
3. **Path Validation** — autonomous Claude agent confirms control-flow + logic correctness; confidence scores; only validated paths proceed to reporting

**Core insight (verbatim):**
> *"Security fixes are context-dependent. A function that makes data safe for one SQL query might not protect a different query. A custom sanitizer that a team wrote will not be recognized by pattern-based tools. Traditional tools rely on a hard-coded list of safe functions; Shannon Pro reasons about what the code is actually doing."*

### 7.2 SAST: Point Issue Detection

Single-location vulnerabilities via LLM:
- Weak encryption algorithms
- Hardcoded credentials / API keys
- Insecure configuration (debug mode enabled in production)
- Missing security headers
- Weak random number generation
- Disabled certificate validation
- Overly permissive CORS

### 7.3 SAST: Business Logic Security Testing

**Corpus-first architectural pattern at T5.**

**Why business logic bugs are missed (verbatim):**
> *"Pattern-based scanners and traditional SAST are structurally incapable of finding business logic vulnerabilities. These bugs do not involve malformed input reaching a dangerous sink. Instead, they involve legitimate operations that violate unstated rules about how the application should behave."*

**4-phase pipeline:**
1. **Invariant Discovery** — LLM agent deep semantic analysis → derives invariants (e.g., *"document access must verify that the document belongs to the requesting user's organization"*)
2. **Fuzzer Generation** — generate targeted fuzzer to violate each invariant; specific adversarial scenarios (not random inputs)
3. **Violation Detection** — execute against stubbed test environment; when fuzzer succeeds → confirmed business logic vulnerability
4. **Exploit Synthesis** — full PoC with step-by-step reproduction + specific API calls / user actions + observed vs expected behavior + security impact

**Real-world example documented (verbatim from SHANNON-PRO.md):**
- **Vulnerability:** CWE-639 Cross-Tenant Data Access (IDOR)
- **Invariant:** *"Document access must verify that the document belongs to the requesting user's organization."*
- **Fuzzer:** extracted GetDocument handler logic, mocked DB, tested cross-org access combinations
- **Violation confirmed:** Organization B user accessed Organization A documents via document ID
- **Full 5-step PoC synthesized** — auth as Org B → enumerate Org A document ID → GET /api/document?document_id=victim-doc-123 → system returns 200 with Org A data
- **Impact:** Complete multi-tenant isolation breach

### 7.4 SCA with Reachability Analysis

**4-step reachability process (verbatim):**
1. AI agent researches each CVE to identify exact vulnerable function / framework / conditions
2. For framework-level issues: check whether app actually uses affected framework in practice
3. For function-level issues: CPG queried for nodes where vulnerable function is used; if no nodes → not reachable
4. If nodes found: trace execution flow from entry points; proven executable → flagged; used-but-not-callable → marked "likely reachable"

**Advantage:** Differentiates reachable CVEs from noise. Prior Pattern #18 MCP-style tool-integration vs Shannon's CPG-reachability = different architectural approach.

### 7.5 Secrets Detection

**3-tier hybrid approach:**
1. Regex pattern matching (AWS keys / API tokens baseline)
2. LLM-based detection (dynamically constructed credentials / custom formats / obfuscated tokens)
3. **Liveness validation** — agent determines API context, attempts read-only API call to verify credential is active

**Read-only validation discipline:** identity-verification endpoints only; avoid triggering side-effects / account lockouts. In self-hosted runner → all validation within customer network.

## 8. Boundary Analysis (monorepo scoping)

For large-scale / monorepo architectures:
- Agent analyzes repository + identifies logical boundaries (service / frontend vs backend / microservice)
- Users review + confirm + optionally edit boundaries
- Select which to include in scan
- Findings tagged by boundary → clear routing to responsible team

**Corpus-first scoping mechanism at T5.**

## 9. False Positive Tagging

Any finding can be marked FP. On subsequent scans, same finding auto-flagged as likely-FP to prevent repeated triage.

**Discipline observation:** Prior T5s didn't document FP-tagging as first-class feature.

## 10. Shannon Pro Stage 2 — Autonomous Dynamic Pentesting

**Execution model (verbatim from SHANNON-PRO.md):**
> *"Phases 1 and 2 (reconnaissance) run sequentially. Phases 3 and 4 (vulnerability analysis and exploitation) run as pipelined parallel: each vulnerability/exploit pair is independent. When a vulnerability agent finishes for a given attack domain, the corresponding exploit agent starts immediately, even if other vulnerability agents are still running."*

**Pipelined-parallel** is the key differentiator from naïve parallel (all-finish-then-all-start) seen in other T5s.

**Core principle (verbatim):**
> *"POC or it didn't happen. Shannon Pro never reports a vulnerability without a working proof-of-concept exploit. Exploitation agents classify each finding as EXPLOITED, POTENTIAL, or FALSE POSITIVE. Only EXPLOITED findings (with concrete evidence) make it to the final report."*

## 11. Static-Dynamic Correlation (the core differentiator)

**From SHANNON-PRO.md §Static-Dynamic Correlation:**
> *"Shannon Pro's distinguishing capability is the correlation between its static and dynamic analysis stages."*

**Flow:**
1. Static analysis produces findings
2. Enrichment phase adds priority + confidence + application context
3. CWEs mapped to 5 attack domains via best-fit heuristic (multi-domain CWEs routed to most-exploitation-relevant agent)
4. CWEs without clean mapping (e.g., business logic) routed to exploitation queue with static context preserved
5. Exploit agents attempt real PoC attacks against running application

**Example chain documented:**
- Static data-flow vuln (unsanitized input → SQL query) → NOT reported as theoretical risk
- Fed to exploit-injection agent → attempts exploitation against live app
- Confirmed exploit → traced back to exact source code location
- Developers get BOTH proof-of-reality AND line-of-code-to-fix

**Corpus-first architectural pattern:** Static-dynamic correlation at T5 AI-pentester scope.

## 12. Deployment model — Self-hosted Runner

**From SHANNON-PRO.md §Self-Hosted Runner (verbatim):**
> *"Shannon Pro supports a self-hosted runner deployment model, following the same architecture as GitHub Actions self-hosted runners. The data plane (the runner that clones code, executes scans, and makes all LLM API calls) runs entirely within the customer's infrastructure using the customer's own LLM API keys. Source code never leaves the customer's network, and no code or LLM interactions pass through Keygraph's systems."*

**Split:**
- **Customer data plane:** clones code + executes scans + LLM API calls (customer keys)
- **Keygraph control plane:** job orchestration + scan scheduling + reporting UI
- Control plane receives ONLY aggregate findings (no code / no raw LLM content)

**Corpus-first** self-hosted runner model at T5 AI-pentester scope (prior T5 cloud-tier = Skyvern Cloud proprietary; not self-hosted equivalent).

## 13. Security architecture (container isolation + data handling)

**From SHANNON-PRO.md §Container Isolation:**

**Per-Organization Infrastructure:**
- Each org gets isolated compute environment
- Managed: Keygraph provisions dedicated ECS infrastructure + IAM roles + task queues per org
- Self-hosted: org provisions + controls data plane
- **Never shared compute environments** across organizations

**Ephemeral Code Handling:**
- Target repo cloned to temp workspace inside isolated container
- Scan executes against local copy
- Immediately after scan → entire workspace deleted (including all cloned code)
- *"Source code is never persisted after a scan finishes. Even if a scan fails or is cancelled, a disconnected cleanup process executes regardless."*

**Encrypted Storage:**
- Code snippets encrypted before DB write
- S3 deliverables encrypted at rest
- Org-specific buckets with org-scoped access policies

**Network Isolation:**
- Isolated workers in private subnets
- Org-specific security groups
- Network-level separation

**Corpus-first enterprise-security-hardening documentation at T5.** Rivals commercial-grade SaaS security profiles (comparable to GitHub Enterprise / HashiCorp Vault architecture documentation).

## 14. 2-tier capability comparison (from SHANNON-PRO.md)

| Capability | Shannon Lite | Shannon Pro |
|------------|--------------|-------------|
| **Licensing** | AGPL-3.0 (open source) | Commercial |
| **Static Analysis** | Code review prompting | Full agentic SAST/SCA/secrets/business-logic |
| **Dynamic Testing** | Autonomous AI pentest framework | Autonomous AI pentesting + static-dynamic correlation |
| **Analysis Engine** | Code review prompting | CPG-based data flow + LLM reasoning at every node |
| **Business Logic** | N/A | Automated invariant discovery + test scenario generation + exploit synthesis |
| **Integration** | Manual / CLI | Native CI/CD + GitHub PR scanning + enterprise support + self-hosted runner |
| **Deployment** | CLI / manual | Managed cloud or self-hosted runner (customer data plane + Keygraph control plane) |
| **Boundary Analysis** | N/A | Automatic service boundary detection + team routing |
| **Best For** | Local testing of own applications | Enterprise application security posture management |

## 15. Compliance integration

**From SHANNON-PRO.md §Compliance Integration:**
> *"Within the broader Keygraph ecosystem, Shannon Pro serves as the primary engine for automated compliance evidence generation. By automating penetration testing and static analysis requirements, Shannon Pro generates real-time evidence for frameworks such as SOC 2 and HIPAA, transforming security testing from a periodic audit obligation into a continuous component of the compliance program."*

**Bridges compliance ↔ continuous-security.**

## 16. Methodology standards

**From SHANNON-PRO.md §Methodology Standards:**
> *"Shannon Pro follows AI-assisted white-box testing methodology broadly aligned with OWASP Web Security Testing Guide (WSTG) and OWASP Top 10 standards. All dynamic testing produces confirmed, exploitable findings with reproducible proof-of-concept exploits. Static analysis covers established CWE categories with LLM-powered validation to minimize false positive rates."*

**OWASP WSTG alignment** documented in Shannon Lite's COVERAGE.md (Cluster 1 §13).

## 17. Governance + Contributing

**From README §Community & Support:**
> *"Contributing: At this time, we're not accepting external code contributions (PRs)."*

- **Issues-only** governance
- Bug reports → GitHub Issues
- Feature requests → GitHub Discussions
- Discord community
- **1:1 Office Hours** Thursdays (2 time zones, US/EU + Asia) — free 15-min booking via Cal.com
- **Shannon Pro Inquiry** via Cal.com/team/keygraph/shannon-pro

**Social:**
- Twitter: [@KeygraphHQ](https://twitter.com/KeygraphHQ)
- LinkedIn: [Keygraph](https://linkedin.com/company/keygraph)
- Email: [shannon@keygraph.io](mailto:shannon@keygraph.io)

**Corpus-first observation:** Issues-only-no-PRs governance at 40K-star T5 is unusual. Most T5s at similar scale (Skyvern 21K AGPL / browser-use 90K MIT / OpenHands 72K MIT) accept PRs. Shannon's approach aligns with commercial-startup AGPL strategy to control contributor-license-grants. Observational — not registered as pattern (N=1).

## 18. Pattern implications

### Pattern #31 Open-Core Commercial Entity (CONFIRMED v24) — STRENGTHENING N=8

**8 data points now (v24 → v45):**
1. fish-speech v20 (outside-scope foundation-model, custom non-OSI)
2. Skyvern v24 (T5 browser-agent, AGPL-3.0, Skyvern Cloud)
3. OpenHands v30 (T5 SWE, MIT core + separate-enterprise)
4. crawl4ai v29 (T4 bridge, Apache-2.0 + Cloud API closed beta)
5. GitNexus v33 (T4 bridge, PolyForm Noncommercial)
6. DeepTutor v38 (T5 education, academic-commercial fusion)
7. browser-use v41 (T5 browser-viral, MIT core + Cloud proprietary)
8. **shannon v45 (T5 AI-pentester, AGPL-3.0 + Pro commercial + Tower managed service)**

**Shannon's distinctive contribution:** **Most-detailed Pro-tier documentation file** (SHANNON-PRO.md 26 KB) + **+ Tower managed service tier** (2-layer commercial: Pro self-service + Tower managed vCISO). Observational candidate for **Pattern #31 sub-variant formalization at future audit** if N=2 of mature-open-core-with-dedicated-docs-and-managed-service-tier emerges.

### Pattern #50 Commercial-Funnel Companion Platform (CONFIRMED v36 mini-audit) — STRENGTHENING N=7

Keygraph's 2-product + 3-customer testimonial + SOC 2 Type I + Cal.com booking + office hours = comprehensive commercial funnel. Strengthens pattern.

### Pattern #17 variant 3 commercial-startup — STRENGTHENING

Keygraph commercial-startup ecosystem: Shannon OSS Lite + Shannon Pro + Tower managed service + 3 customers + SOC 2 + Trendshift badge = strong variant 3 data point.

## 19. Corpus-firsts in Cluster 3

1. Shannon Pro = corpus-first dedicated 26 KB Pro-tier documentation file at T5
2. CPG (Code Property Graph) at T5 AI-pentester scope
3. Static-dynamic correlation pipeline (static findings → dynamic exploitation queue)
4. Business-logic invariant-fuzzer-generation 4-phase pipeline
5. SCA with CPG reachability at T5
6. Secrets detection with liveness validation (read-only API verification)
7. Boundary analysis for monorepo scoping at T5
8. False positive tagging as first-class feature
9. Self-hosted runner model (customer data plane + Keygraph control plane) at T5 AI-pentester
10. Encrypted-at-rest code snippets + S3 org-specific buckets + private subnet isolation enterprise-security documentation
11. Tower managed vCISO tier (managed-service sibling to Pro)
12. Compliance evidence generation (SOC 2 / HIPAA) as first-class Pro feature
13. Issues-only-no-PRs governance at 40K-star T5 scope
14. 3-customer named testimonials + 1 verbatim CEO quote at commercial-startup T5
15. SOC 2 Type I certification claim at commercial-startup Shannon tier
16. CWE-639 cross-tenant IDOR documented as full end-to-end example of business-logic-fuzzer pipeline

## Cross-wiki links

- Commercial peers: [[Skyvern]] v24 (commercial-entity T5) / [[OpenHands]] v30 (academic-commercial T5) / [[crawl4ai]] v29 (T4 Cloud commercial) / [[fish-speech]] v20 (foundation-model commercial) / [[GitNexus]] v33 (PolyForm commercial) / [[browser-use]] v41 (MIT + Cloud)
- Enterprise-security peers: [[OpenHands]] v30 separate-license-enterprise-directory; [[GitNexus]] v33 self-hosted Enterprise; Shannon uniquely documents self-hosted-runner architecture in 26KB PRO.md
- Sample-reports-in-repo peer: none (corpus-first)
- CPG peers: [[GitNexus]] v33 (code → knowledge graph at T4 bridge) — distinct role (bridge vs pentesting)
- Compliance peers: none explicit; Shannon first corpus-first SOC 2 + HIPAA auto-evidence at T5
