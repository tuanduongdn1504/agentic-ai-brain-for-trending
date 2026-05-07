# Gaps for Production — what these tips/tricks videos don't cover

The 6 creators are heavy on **local-development productivity** and almost silent on **enterprise-scale production**. If you're running Claude Code on personal projects, the gaps below don't matter. If you're shipping to paying users or processing sensitive data, you need to fill them.

## Production gaps in the corpus

### 1. CI/CD orchestration and deployment gates
The corpus discusses "PR loops" (Sean Kochel's `ship-and-watch`) and basic linting integration. It does **not** cover:
- Formal CI/CD pipeline integration (GitHub Actions, GitLab CI, CircleCI).
- Automated deployment gates beyond linting — security scans, integration tests, staging deploys, canary rollouts.
- Rollback automation when post-deploy metrics regress.

### 2. Network isolation for autonomous agents
Chase AI mentions `--dangerously-skip-permissions` as a speed move. Boris Cherny notes non-technical users run code in VMs. Neither covers:
- VPC isolation to prevent accidental (or prompt-injection-induced) data exfiltration.
- Network air-gapping for agents working with sensitive data.
- Outbound traffic auditing — what's the agent actually sending where?

### 3. Enterprise secrets management
Eric Tech mentions adding Stripe keys to `.env.local`. Production environments require:
- Integration with secrets managers (AWS Secrets Manager, HashiCorp Vault, Doppler).
- Prevention of secret leakage in "verbose mode" logs.
- Auto-rotation hooks when keys are exposed in commits.
- Audit trails for secret access.

### 4. IP, licensing, and compliance auditing
Zero coverage of:
- Auditing AI-generated code for open-source license violations (e.g., GPL-licensed snippets pulled from training data).
- Industry regulation compliance — HIPAA (healthcare), SOC2 (enterprise), PCI-DSS (payments), GDPR (EU data).
- Provenance tracking — which lines in this PR were AI-generated vs human-written?

### 5. Observability and runtime monitoring
Tips focus on fixing bugs *during development*. Production needs:
- Performance monitoring of AI-built systems under load.
- Reliability monitoring (uptime, error rates, latency percentiles).
- Tracing requests through AI-generated code paths to diagnose production issues.

### 6. Multi-user state management
"Agent teams" and "swarms" are discussed only as parallel work by a single human operator. Real teams need:
- Shared state when multiple developers all use Claude Code on the same codebase.
- Conflict resolution beyond git worktrees (which only handle directory isolation, not semantic conflicts).
- Cross-session conversation handoff between team members.

## Recommended follow-up topics for next loops

Ranked by impact for someone running Claude Code in production:

1. **CI/CD integration for autonomous agents** — automated fail-safe pipelines that audit Claude's PRs before they reach production. Highest immediate ROI.
2. **Network-isolated sandboxing** — best practices for running Claude Code inside restricted Docker containers or VPCs. Risk-reduction critical.
3. **Automated security/vulnerability scanning** — Snyk, SonarQube integration to scan Claude-generated code for SQL injection, XSS, etc. that "vibe coders" might miss.
4. **Agent governance and audit logs** — permanent searchable record of every command Claude executed on production infra. Compliance + post-mortem analysis.
5. **Enterprise cost and token budgeting** — managing/capping token spend across distributed teams to avoid bill shock.
6. **IP and licensing scans for AI code** — workflows to verify AI-generated code doesn't contain protected snippets from training data.
7. **Infrastructure as Code (IaC) with Claude** — Terraform, Kubernetes management without risking catastrophic deletions.

## Cross-references

- [[../workflow-ai-coding/gaps-and-followups]] has overlapping gaps. The intersection (CI/CD, secrets, observability, IP) is where production-Claude-Code expertise *most* needs to grow.
- [[../claude-code-hooks/_index|claude-code-hooks]] covers the hook layer that's foundational to several of these (path protection, audit logging, etc.).
- For an individual operator: pick #1 (CI/CD) and #4 (audit logs) first. They have the lowest setup cost and prevent the highest-cost incidents.

## Why these gaps exist

Speculative but worth naming: the YouTube tips/tricks format rewards **immediately-applicable** content. "10 cheating tricks" gets clicks; "how to integrate audit logging with your SIEM" doesn't. The gap isn't expertise scarcity — it's content-format mismatch. Look for these topics in conference talks and engineering blogs, not in the 10-minute creator-economy YouTube space.
