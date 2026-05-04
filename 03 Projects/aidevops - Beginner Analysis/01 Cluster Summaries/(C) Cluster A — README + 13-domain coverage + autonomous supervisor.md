# (C) Cluster A — README + 13-domain coverage + autonomous supervisor

**Source:** `README.md` (142,376 bytes — 2nd-largest in corpus after ruflo v42 280KB)
**Audience:** Outside-world (potential users / contributors / press)

## What it is (verbatim opening)

> "An [OpenCode](https://opencode.ai/) plugin and AI operations platform for launching and managing development, business, marketing, and creative projects. 13 specialist AI agents handle the automatable work across every domain so your time is preserved for real-world discovery and decisions that AI cannot yet reach."

> "One conversation, autonomous project delivery — with enterprise-level security & quality-control."

> "Founded by Marcus Quinn on 9th November 2025 to help anyone level-up their AI & Open-Source game."

GitHub description: *"Vibe-Coding is easy. DevOps is hard. OpenCode & Git token-efficient AI agent automation for your app, business, and personal development."*

## Recommended setup (verbatim, README §"Why This Framework?")

> "Recommended setup: OpenCode + Claude models (Anthropic). All features, agents, and workflows are designed and tested for OpenCode first. Claude models (haiku, sonnet, opus) deliver the best results across all agent tiers."

**This is corpus-first OpenCode-as-primary T1 framework.** All prior 13 T1 entrants either Claude-Code-primary (ECC v1, SP v2, gstack v3, GSD v5, BMAD v11, codymaster v12, spec-kit v17, agency-agents v18, claude-howto v32, claude-code-best-practice v34, claude-hud v35) OR multi-runtime-balanced (OMC v27 4 runtimes / pi-mono v36 standalone). Aidevops uniquely positions OpenCode as default platform.

## 13 specialist domain agents

(README §"Agent Structure" claims "13 primary agents (Build+, Automate, SEO, Marketing, etc.) with specialist @subagents on demand")

Per `.agents/` top-level directory listing + `.agents/commands/` files:

| # | Domain | Role |
|---|---|---|
| 1 | **Build+** (default) | Code: research → discuss / implement / fix; intent detection from user phrasing |
| 2 | **Automate** | Workflow automation, scheduled tasks, cron, launchd |
| 3 | **SEO** | Search-optimization (60 subagents in `.agents/seo/`; 40+ external SEO tools — Semrush / Ahrefs / DataForSEO / etc.) |
| 4 | **Marketing-Sales** | Marketing campaigns + sales workflow |
| 5 | **Content** | Content creation + media + writing |
| 6 | **Legal** | Legal-document drafting + advisory framing |
| 7 | **Sales** (subset of Marketing-Sales above; sometimes co-listed) | Pipeline management |
| 8 | **Research** | Research-deep-agent workflows + citation discovery |
| 9 | **Video** | Video creation (Remotion + HeyGen + Veo 3 prompt design) |
| 10 | **Business** | Business operations + advisory |
| 11 | **Accounts** (Accounting via QuickFile MCP) | Bookkeeping + financial workflow |
| 12 | **Social Media** | Social campaigns + cross-platform posting |
| 13 | **Health** | Health-domain advisory (corpus-first health agent at T1) |

**13 domain coverage = corpus-broadest.** Prior T1 entrants:
- ECC v1: feature-framework (1 domain — coding)
- agency-agents v18: 12-14 divisions (close 2nd; engineering/design/marketing/sales/specialized/game-dev/spatial/paid-media/product/PM/testing/support/finance/academic)
- BMAD v11: agile methodology (1 domain — software development)
- All other T1 entrants: 1-2 domains primarily

aidevops v47 ties or slightly exceeds agency-agents v18 in cross-domain breadth. Distinct: agency-agents agents are **personality-driven roles** (Whimsy Injector / Reality Checker / Reddit Community Builder); aidevops agents are **functional-domain orchestrators** with deep tooling (each has dozens of subagents + helper scripts + service integrations).

## Autonomous Pulse Supervisor (CORPUS-FIRST architectural primitive)

(README §"Pulse Supervisor: Autonomous AI Operations" — verbatim summary)

**The pulse is the heartbeat of aidevops — an autonomous AI supervisor that runs every 2 minutes via launchd. There is no human at the terminal.**

**Per-cycle operations (9 phases):**

| Phase | Action |
|---|---|
| Capacity check | Circuit breaker, dynamic worker slots calculated from available RAM |
| Merge ready PRs | Green CI + no blocking reviews → squash merge (free, no worker slot needed) |
| Fix failing PRs | Dispatch worker to fix CI failures or address review feedback |
| Detect stuck work | PRs open 6+ hours with no activity → flag or close and re-file |
| Dispatch workers | Route open issues to worker slots with priority + `blocked-by:` deps |
| Advance missions | Check active multi-day missions, dispatch features, validate milestones, track budget |
| Triage quality | Read daily quality sweep findings (ShellCheck / SonarCloud / Codacy / CodeRabbit) → create issues |
| Sync TODOs | Create GitHub issues for unsynced TODO entries, commit ref changes |
| Kill stuck workers | Workers running 3+ hours with no PR are killed to free slots |

**Operational intelligence:**
- **Struggle-ratio:** computes `messages / max(1, commits)` per active worker. >30 with >30 min elapsed + zero commits = "struggling". >50 after 1 hour = "thrashing".
- **Circuit breaker:** prevents cascading failures by tracking success/failure rates
- **Dynamic concurrency:** worker slot count adapts to RAM
- **Stale assignment recovery:** auto-unassigns dead workers
- **Priority ordering:** green PRs > failing PRs > high-priority/bug > active missions > product repos > smaller > oldest

**Verbatim:** *"The pulse is an LLM, not a script. It reads issue bodies, assesses context, and uses judgment."*

**Manual trigger:** `opencode run "/pulse"` (otherwise launchd every 2 min).

**Spec:** `.agents/scripts/commands/pulse.md`.

## Mission orchestration

(README §"Missions: Multi-Day Autonomous Projects")

> "/mission scopes a high-level goal into milestones and features. The pulse dispatches workers, validates milestones, tracks budget, and advances through the project automatically (mission-dashboard-helper.sh)"

**Two execution modes:**
- **Full** — Worktree + PR per feature, standard review flow (production code)
- **POC** — Direct commits, skip ceremony (prototypes)

Mission state in committed JSON file → any session can pick up where last pulse left off.

Spec: `.agents/workflows/mission-orchestrator.md`

## Multi-Model Verification (CORPUS-FIRST cross-provider safety)

(README §"Multi-Model Verification: Cross-Provider Safety")

**High-stakes operations are verified by a second AI model from a different provider before execution.**

| Risk | Examples | Action |
|---|---|---|
| **Critical** | `git push --force` to main, `DROP DATABASE`, production deploy | Blocked unless second model agrees |
| **High** | Force push to feature branch, data migration, secret exposure | Warned, verification recommended |
| **Medium** | Bulk file deletion, config changes | Logged |
| **Low** | Normal edits, test runs | No verification |

**Mechanism:**
1. `pre-edit-check.sh` screens against high-stakes taxonomy
2. For critical/high → `verify-operation-helper.sh` sends operation context to second model (different provider than primary)
3. Verifier independently assesses safety
4. On disagreement → blocked (critical) or warned (high)
5. All decisions logged for audit

**Why cross-provider?** Verbatim: *"Same-provider models share training data and failure modes. A Claude hallucination is unlikely to be reproduced by Gemini or GPT, and vice versa."*

**Cost:** "Verification uses the cheapest model tier (haiku-equivalent) — cost is minimal per check."

**Configuration:** Per-repo via `.agents/reference/high-stakes-operations.md`. Opt-out: `VERIFY_ENABLED=false` (not recommended).

**Pattern #28 NEW SUB-AXIS proposed at next mini-audit:** verification-not-routing as cross-provider-safety mechanism (distinct from prior #28 data points which were routing/abstraction-focused).

## Project Bundles (auto-configuration)

7 built-in bundles auto-detect project type from marker files:

| Bundle | Detection | Default model | Quality gates |
|---|---|---|---|
| **web-app** | `package.json` + framework markers | sonnet | Full (lint/test/build/a11y) |
| **library** | `package.json` w/ `main`/`exports` | sonnet | Full + API docs |
| **cli-tool** | `bin` field in package.json | sonnet | ShellCheck + test |
| **content-site** | CMS markers, `wp-config.php` | haiku | Lighthouse + SEO |
| **infrastructure** | `Dockerfile` / `terraform/` / `ansible/` | sonnet | ShellCheck + security scan |
| **agent** | `AGENTS.md` / `.agents/` | opus | Agent review + prompt quality |
| **schema** | (DB schema markers) | sonnet | (schema-specific) |

Resolution priority: explicit `bundle` field > `.aidevops.json` > auto-detection. CLI: `bundle-helper.sh`.

## 30+ external service integrations

(README §"Comprehensive Service Coverage" — categories only, not enumerated)

| Category | Examples |
|---|---|
| **Infrastructure & Hosting** | Hostinger / Hetzner / Closte / Coolify / Cloudron / Vercel / AWS / DigitalOcean |
| **Domain & DNS** | Cloudflare / Spaceship / 101domains / AWS Route53 / Namecheap |
| **Git Platforms** | GitHub (gh) + GitLab (glab) + Gitea (tea) — CLI-enhanced |
| **AI Orchestration Frameworks** | Langflow / CrewAI / AutoGen |
| **Video Creation** | Remotion / Veo 3 prompt design / MuAPI / yt-dlp |
| **WordPress** | LocalWP / MainWP |
| **Security & Quality** | gopass / Vaultwarden / SonarCloud / CodeFactor / Codacy / CodeRabbit / Snyk / Socket / Sentry / Cisco Skill Scanner / VirusTotal / Secretlint / OSV Scanner / Qlty / Gemini Code Assist |
| **AI Prompt Optimization** | Augment Context Engine / Repomix / DSPy / DSPyground / TOON |
| **Documents & OCR** | Document Creation Agent / LibPDF / MinerU / Unstract / GLM-OCR |
| **Communications** | Twilio / Telfon / Matrix / SimpleX / Matterbridge (20+ platforms) |
| **Voice AI** | Voice Bridge / Speech-to-Speech / Pipecat |
| **Performance** | PageSpeed / Lighthouse / WebPageTest / Updown.io |
| **AI & Documentation** | Context7 / Local llama.cpp models |
| **Local Development** | Localdev (dnsmasq + Traefik + mkcert) |

## 20 MCP integrations

| MCP | Purpose | Tier | Key required |
|---|---|---|---|
| Augment Context Engine | Semantic codebase | Global | Yes |
| Claude Code MCP | Claude as sub-agent | Global | No |
| Amazon Order History | Order data | Per-agent | No |
| Chrome DevTools | Browser automation | Per-agent | No |
| Context7 | Library docs | Per-agent | No |
| Docker MCP | Container mgmt | Per-agent | No |
| Google Analytics | Analytics | Per-agent | Yes |
| Google Search Console | Search performance | Per-agent | Yes |
| Grep by Vercel | GH code search | Per-agent | No |
| LocalWP | WordPress DB | Per-agent | No |
| macOS Automator | macOS automation | Per-agent | No |
| Playwriter | Browser w/ extensions | Per-agent | No |
| QuickFile | Accounting | Per-agent | Yes |
| Repomix | Codebase packing | Per-agent | No |
| Sentry | Error tracking | Per-agent | Yes |
| shadcn | UI components | Per-agent | No |
| Socket | Dependency security | Per-agent | No |
| Unstract | Doc extraction | Per-agent | Yes |
| OpenAPI Search | OpenAPI specs | Per-agent | No |
| Cloudflare Code Mode | Cloudflare API (2,500+ endpoints in 2 tools) | Per-agent | Yes |

**Per-agent MCP filtering** (Pattern #18 sub-observation): MCPs disabled globally, enabled per-agent via config. **Zero context overhead when unused.** Each agent gets ~12-20 tools (multi-layer-action-space pattern).

**Bun-installed globally for instant startup** (~0.1s vs 2-3s with npx). 3-tier loading strategy: eager-at-startup OR on-demand-when-subagent-invoked.

## Imported skills (6 sources)

| Skill | Source | Description |
|---|---|---|
| cloudflare-platform | dmmulroy/cloudflare-skill | 60 Cloudflare products |
| heygen | heygen-com/skills | AI avatar video API |
| remotion | remotion-dev/skills | Programmatic video |
| video-prompt-design | snubroot/Veo-3-Meta-Framework | Veo 3 prompt engineering |
| animejs | animejs.com (via Context7) | JS animation |
| caldav-calendar | ClawdHub | CalDAV sync |
| proxmox-full | ClawdHub | Proxmox VE management |

**Cisco Skill Scanner security gate** on import + update (CRITICAL/HIGH blocks; MEDIUM/LOW warns). VirusTotal advisory layer (70+ AV engines). Audit trail in `.agents/SKILL-SCAN-RESULTS.md`.

**Pattern #18 sub-observation:** Cisco AI Defense Skill Scanner = corpus-first dedicated skill-supply-chain security tool integration. Marcus's `marcusquinn/aidevops` is **2nd corpus subject with explicit supply-chain security tooling** (after crawl4ai v29 LiteLLM fork response).

## Agent Design Patterns lineage (CORPUS-FIRST Lance Martin / LangChain citation)

(README §"Agent Design Patterns" — full table verbatim from source)

> "aidevops implements proven agent design patterns identified by Lance Martin (LangChain)."

| Pattern | aidevops Implementation |
|---|---|
| Give Agents a Computer | `~/.aidevops/.agent-workspace/`, 873+ helper scripts |
| Multi-Layer Action Space | Per-agent MCP filtering (~12-20 tools each) |
| Knowledge Graph Routing | `subagent-index.toon` maps 900+ agents by domain/purpose/dependency |
| Progressive Disclosure | Subagent routing with content summaries, YAML frontmatter, read-on-demand |
| Offload Context | `.agent-workspace/work/[project]/` for persistence |
| Cache Context | Stable instruction prefixes for prompt caching |
| Isolate Context | Sub-agents with separate windows + tool permissions |
| Multi-Agent Orchestration | TOON mailbox + agent registry + supervisor dispatch |
| Compaction Resilience | OpenCode plugin injects dynamic state at compaction time |
| Ralph Loop | `/full-loop`, `full-loop-helper.sh` |
| Evolve Context | `/remember`, `/recall` with SQLite FTS5 + opt-in semantic search |
| Pattern Tracking | `/patterns` + `memory-helper.sh` |
| Token-Efficient Serialisation | TOON format (20-60% reduction vs JSON/YAML) |
| Cost-Aware Routing | `model-routing.md` 7-tier + `/route` |
| Model Comparison | `/compare-models` (live) + `/compare-models-free` (offline) |
| Response Scoring | `/score-responses` with structured criteria |

**16 patterns documented with implementations.** Source x.com/RLanceMartin/status/2009683038272401719.

**Pattern #19 archetype 2 methodology-lineage** = NEW INDIVIDUAL INFLUENCE NODE (Lance Martin = 4th individual influence node alongside Karpathy / John Lam / Anthropic-team-cluster). 18+ Pattern #19 archetype-2 methodology-lineage data points across corpus; aidevops introduces Lance Martin specifically.

## Voice Bridge (Apple Silicon-optimized)

> "Mic → Silero VAD → Whisper MLX (1.4s) → OpenCode (4-6s) → Edge TTS (0.4s) → Speaker"

Round-trip ~6-8s on Apple Silicon. The agent can edit files / run commands / create PRs all by voice.

CLI: `voice-helper.sh talk`. Engines swappable (whisper-mlx / faster-whisper / edge-tts / macos-say). Voice exit phrases: "that's all" / "goodbye" / "all for now".

**Corpus-first explicit voice-input-to-AI-coding-agent at T1** (Storm Bear LLM Wiki Routine v2.1 doesn't yet have voice-input documented — potential routine v2.2 enhancement).

## Quality discipline stack (8 external platforms — corpus-most)

README badge inventory:
- **GitHub Actions Code Quality Analysis** workflow
- **SonarCloud** Quality Gate
- **CodeFactor** repository grading
- **Qlty** maintainability badge
- **Codacy** Grade
- **CodeRabbit** AI review
- **Snyk** vulnerability scanning (referenced)
- **Bandit** Python security linting
- **secretlint** secret detection
- **ShellCheck** for all shell scripts
- **Gemini Code Assist** (Google)

**11 documented quality tools / 8+ external platforms = corpus-record.** Prior corpus-most: pi-mono v36 (~6 tools) / spec-kit v17 (~5).

## Storm Bear pilot relevance MEDIUM-HIGH (observational)

**Direct utility (LOW-MEDIUM):**
- 13-domain agent breadth maps to Scrum-coach service surface (technical/business/marketing/legal/content advisory)
- Mission orchestration could automate Scrum coaching backlog management
- Ralph loops + git worktree parallel = Storm Bear could adopt
- Voice Bridge = experimental Storm Bear voice-input pilot
- Cross-provider verification = direct relevance for client-facing operations safety

**Friction:**
- OpenCode-first design (Storm Bear is Claude-Code-primary)
- ~2,665+ primitive learning curve (EXTREME — 5× ruflo)
- Cold-start scale (212 stars) = lower battle-tested confidence
- Commercial positioning (paid pool services) = mixed open-core lineage friction
- Bash-primary implementation = friction for non-Bash operator

**Composability:**
- Storm Bear vault could adopt aidevops AGENTS.md-authoritative pattern (without adopting full framework)
- Storm Bear could adopt 8-tool quality stack (Codacy + CodeFactor + CodeRabbit + Sonar + Qlty + Bandit + secretlint + ShellCheck) independently of aidevops framework
- TOON format = potential Storm Bear vault token-efficient serialization adoption

## Cross-references

- **Pattern #18** Agent Runtime Standardization — OpenCode-as-primary T1 sub-observation NEW
- **Pattern #19** archetype 2 methodology-lineage — 4th individual-influence-node Lance Martin
- **Pattern #22** AGENTS.md Industry Standard — 3-layer governance hierarchy formulation extension
- **Pattern #28** Multi-Provider AI Support — verification-not-routing as cross-provider-safety NEW sub-axis
- **Pattern #57** Recursive Corpus Reference — 4th data point (CREDITS.md cites VoltAgent v25 + Google Stitch v25 referenced)

---

*(C) Generated by Claude — Cluster A summary for v47 aidevops*
