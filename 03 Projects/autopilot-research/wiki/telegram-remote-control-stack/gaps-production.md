# Gaps for Production — what's missing when you scale beyond solo/team

Synthesized across all 4 drains. The bundle is heavy on **personal/hobbyist setups**; thin on **production-grade operations**. If [[operator-recipes|Recipes A-D]] are working but you're growing past them, here's what to expect to add.

## 1. Secrets management

**The problem in the bundle:** API tokens (Telegram, Discord, GitHub, OpenAI, Anthropic, Trading APIs) live in plain-text files:
- `~/.claude/mcp.json`
- `~/Library/Application Support/Claude/claude_desktop_config.json`
- Shell-pasted during interactive `/configure`

**What production needs:**
- Environment-variable injection (`secret_ref: arn:aws:secretsmanager:...` instead of literal value)
- Vault integration: AWS Secrets Manager, HashiCorp Vault, Doppler
- Auto-rotation hooks when a key is exposed (e.g., GitHub secret scanning catches a token committed → rotate automatically)
- Audit trail: who accessed which secret when

**Where to start:** wrap the Channels plugin's `/telegram:configure` with a script that pulls the token from `op` (1Password CLI) or `aws secretsmanager get-secret-value` instead of pasting.

## 2. Identity and Access Management (IAM/RBAC)

**The problem in the bundle:** Allow-list is binary — you're in or out. Once in, you can run "all commands" if auto-approve is on.

**What production needs:**
- Per-command scoping: this user can run `git pull` but not `rm`
- Role-based: `dev-readonly` vs `prod-readwrite` vs `admin`
- Time-bound: this user has access for the next 4 hours, then expires
- Approval workflows: dangerous commands require second-person sign-off

**Where to start:** Recipe C's custom `fastmcp` IAM wrapper. Maintain `permissions.json` keyed by Discord User-ID; check before every tool execution; deny + audit-log denied attempts.

## 3. Observability and audit logs

**The problem in the bundle:** You see Claude's terminal output in real-time — but no permanent record. If a Ralph loop ran for 5 hours and damaged something, there's no trace of which decision led where.

**What production needs:**
- Append-only audit log: every command, prompt, tool call, exit code, timestamp, user
- Centralized log aggregation: CloudWatch / Datadog / Loki
- Searchable: "show all commands user X ran on day Y"
- Tamper-evident: logs themselves should be immutable from inside the agent

**Where to start:**
- Pipe Claude Code stdout through `ts | tee` to a daily log file
- Forward log files to centralized service via `vector` or `fluentbit`
- Set retention policy (e.g., 90 days hot, 1 year cold)

## 4. FinOps — token cost guardrails

**The problem in the bundle:** Developers Digest warns about runaway autonomous loops. Bundle doesn't cover **enterprise-scale cost management**.

**What production needs:**
- Per-user, per-project token budgets
- Real-time spend dashboards
- Hard caps (kill the agent if it tries to spend $X in Y minutes)
- Anomaly detection (this user usually spends $5/day, today they're at $50 — investigate)

**Where to start:**
- Anthropic Console has usage alerts — set them
- Wrap Claude invocations in a budget-checker (read recent usage → kill if over threshold)
- Tag every API call with project + user metadata for downstream analysis

## 5. High Availability + failover

**The problem in the bundle:** Recommendations are "Mac Mini that stays on" or "VPS". Both are **single point of failure**.

**What production needs:**
- Hot standby: secondary instance ready to take over within seconds of primary failure
- Geographic distribution: at least one instance per region you operate in
- Health checks: automatic failover when primary stops responding
- Telegram bot routing: requests should reach whichever instance is healthy

**Where to start:**
- Containerize Claude Code + Channels plugin
- Run on Kubernetes (or simpler: docker-compose on 2 VPS in different regions)
- Use Cloudflare Load Balancer or Tailscale's resource health checks

## 6. Infrastructure as Code (IaC)

**The problem in the bundle:** Setup is entirely manual — copy-paste-driven. No reproducibility.

**What production needs:**
- Terraform / Pulumi / Ansible for VPS provisioning
- Dockerfile for the Claude Code + plugin container image
- Compose / Helm chart for the full stack
- CI pipeline to roll changes safely

**Where to start:**
- Capture your manual VPS setup as an Ansible playbook (~1-2 days)
- Then Terraform for the underlying resource creation
- Then a CI pipeline that validates changes don't break the running setup

## 7. Process management — auto-start, auto-restart

**The problem in the bundle:** `tmux` keeps sessions alive across SSH disconnects but **doesn't survive a reboot**. Bundle creators don't cover this.

**What production needs:**
- systemd unit (Linux) or launchd plist (macOS) to auto-start `claude --channels` on boot
- Restart-on-crash with exponential backoff
- Health check probes
- Log rotation

**Where to start:**

```ini
# /etc/systemd/system/claude-channels.service
[Unit]
Description=Claude Code Channels listener
After=network.target

[Service]
Type=simple
User=claude-user
WorkingDirectory=/home/claude-user
ExecStart=/usr/local/bin/tmux new-session -d -s claude 'claude --channels'
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable claude-channels
sudo systemctl start claude-channels
```

This is the missing piece in NetworkChuck's tutorial that gets you past the next reboot.

## 8. Network egress filtering

**The problem in the bundle:** Bundle covers ingress security (UFW, Fail2Ban) thoroughly. **Egress** (what your machine can REACH OUT to) is uncovered.

**What production needs:**
- Whitelist outbound destinations: `api.anthropic.com`, `api.telegram.org`, `api.github.com` — and that's it
- Block exfiltration: if the agent is compromised, it can't send your code to attacker-controlled servers
- Egress logging: who tried to call where, when

**Where to start:**
- Configure UFW egress rules (default deny outbound, allow specific destinations)
- Use Pi-hole or NextDNS to filter at DNS level
- Or move the workload to a VPC with explicit egress filtering

## 9. Compliance + IP

**The problem in the bundle:** Zero coverage of:
- Open-source license auditing of AI-generated code
- HIPAA / SOC2 / PCI-DSS compliance for AI in regulated industries
- IP ownership of AI-generated code
- Provenance tracking (which lines came from AI vs human)

**What production needs:**
- License scanning (FOSSA, ScanCode) on AI-generated PRs
- Audit trail showing AI vs human authorship per commit
- Compliance attestations from your AI vendor (Anthropic provides some)

**Where to start:** mostly contracts and tooling outside Claude Code itself. Worth flagging to legal/compliance early.

## 10. Multi-user state management

**The problem in the bundle:** Recipe C addresses small teams via Discord channels. **Larger teams** (10+) need:
- Per-user conversation isolation (different team members shouldn't see each other's prompts)
- Resource quotas (one user can't monopolize the bot)
- Cross-user collaboration patterns (handoff: "user A started this, user B continues")
- Role-based UI (manager view vs IC view)

**Where to start:** at this scale, you've outgrown plug-and-play Channels. Time to build a custom orchestrator that handles team-level state.

## When these gaps don't matter

If you're:
- Solo
- On personal projects
- In a hobby phase
- Total spend <$100/mo
- Comfortable with manual ops

→ Recipe A or B is fine. Don't over-engineer.

The gaps above start mattering when:
- You're doing client work (compliance + audit)
- Spending >$500/mo (FinOps)
- Team >5 people (RBAC + multi-user)
- Code is sensitive IP (egress filtering + secrets)
- 24/7 reliability is a business requirement (HA + IaC)

## Recommended next-loop topics

If pursuing this stack to production, the next autopilot research loops should cover:

1. **AI agent observability** — Datadog AI / OpenTelemetry for agents / specialized AI ops platforms
2. **Vault patterns for AI agents** — secrets management specific to agentic workflows
3. **Multi-agent governance** — RBAC, audit, compliance for teams running 10+ Claude instances
4. **AI cost optimization** — token caching, prompt compression, model routing
5. **Container patterns for Claude Code** — running headless Claude in Kubernetes safely
6. **Egress filtering for autonomous agents** — preventing prompt-injection-induced exfil
7. **Multi-region HA for messaging-bridge agents** — geographic failover patterns

These would graduate this stack from "personal automation" to "enterprise infrastructure".

## Cross-references

- [[overview]] § decision matrix — production needs change which recipe applies
- [[operator-recipes]] — current recipes hit walls at production scale; this article maps where
- [[../10x-claude-code/gaps-production|10x-claude-code § gaps-production]] — substantial overlap; intersection (CI/CD, observability, IP, secrets) is where production-Claude-Code expertise needs to grow
- [[../workflow-ai-coding/gaps-and-followups|workflow-ai-coding § gaps]] — strategic-frame gaps that complement these tactical ones
