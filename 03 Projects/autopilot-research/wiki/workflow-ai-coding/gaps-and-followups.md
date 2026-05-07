# Gaps and Follow-ups — what's missing

The 6 talks are heavy on **feature development and refactoring loops**. Several critical zones for a professional AI-integrated lifecycle are weak or absent.

## Gaps in the corpus

### Production incident response (AIOps)
Sources focus on greenfield/refactor work. Almost no discussion of agents triaging live production incidents, analyzing real-time logs, or performing automated rollbacks. The loop terminates at "merged to main" — what happens at 3am on Saturday is uncharted.

### Data privacy and IP
Brief mention of preventing PII leaks in logs. No coverage of:
- Legal implications of feeding sensitive enterprise data into context windows.
- Ownership of AI-generated code.
- Compliance with data-residency rules when models are hosted in different regions.

### Infrastructure as Code (IaC) and orchestration
"Orchestration" in these talks means task management and local dev tooling. No detail on agents handling Terraform, Kubernetes, or AWS — environments where errors have direct financial and security consequences.

### Legacy codebase archaeology
Speakers say "bad codebases make bad agents" and suggest architectural improvements. They don't provide a workflow for **massive undocumented legacy monoliths** where an agent can't simply explore and understand without specific reverse-engineering strategies. COBOL, old Java, C++ legacy — invisible.

### Non-technical stakeholder collaboration
Plan Mode and Grill Me facilitate developer-AI alignment. There's a gap in how visual-first stakeholders (UX designers, PMs without terminal fluency) participate in these feedback loops. The agent workflow is implicitly developer-centric.

## Recommended follow-up topics for next loops

Ranked by relevance to an individual operator running these patterns in real work:

1. **AI-native observability and automated remediation** — how to connect agents to monitoring stacks (Datadog, Prometheus) to **automatically fix production bugs**, not just build features. Highest operational ROI.
2. **Multi-model governance** — orchestrating different model providers (Claude for implementation, GPT for security review) to avoid lock-in and optimize for each model's strengths.
3. **Cost-benefit analysis and token economics** — implementing cost-tracking guardrails at enterprise scale. Beyond the "token billionaire" mindset, what does ROI look like for 5,000 parallel agents?
4. **AI design systems and visual feedback loops** — multimodal feedback that lets agents "see" UI regressions or design inconsistencies that text-based TDD misses.
5. **Formal verification and security compliance** — formal methods, OWASP Top 10 scanning as part of reviewer-agent personas. How do you ensure "free code" doesn't introduce systemic vulnerabilities?
6. **Human-AI social dynamics and team structure** — impact of harness engineering on junior-developer mentorship and team morale when "hands-on-keyboard" gives way to steering and reviewing.
7. **Deep legacy modernization frameworks** — methodology for using AI to decompose 10+-year-old monoliths into Pocock's "deep modules", specifically in COBOL/Java/C++.

## Topics to queue

If running this autopilot routine, three of the seven follow-ups are high-signal next-loop candidates:

- **#1 AIOps + automated remediation** — distinct enough corpus, lots of recent content (Datadog AI, PagerDuty AI Ops, etc.).
- **#2 Multi-model governance** — current zeitgeist, lots of opinionated takes.
- **#5 Security compliance** — undercovered in the AI-engineering corpus, valuable contrast.

The remaining four (cost economics, design systems, social dynamics, legacy modernization) are valuable but more diffuse — better suited to ad-hoc deep-dive than autopilot.

See [[overview]] for the philosophical frame and [[practical-takeaways]] for the rules these speakers DO cover.
