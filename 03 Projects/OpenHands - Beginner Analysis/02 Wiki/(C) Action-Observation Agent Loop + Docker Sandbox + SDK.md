# (C) Action-Observation Agent Loop + Docker Sandbox + SDK

> **Entity type:** Core technical entity (the agent loop + runtime)
> **Wiki:** v30 OpenHands
> **Source grounding:** ICLR 2025 paper (arXiv 2407.16741) + Nov 2025 SDK paper (arXiv 2511.03690) + README + openhands.dev product page
> **Status:** Entity page complete

---

## 1. Identity

The **Action-Observation agent loop with Docker-sandboxed execution**, exposed through a **composable Python SDK**, is the core technical entity that makes OpenHands an autonomous software engineer rather than a passive code-suggestion tool.

This entity distinguishes OpenHands across two dimensions:
- **From T5 peers:** more general than Skyvern's browser-only sandbox; more production-grade than autoresearch's git-branch isolation; more formally specified than paperclip's invariant-based orchestration
- **From T1 peers:** autonomous standalone application vs an assistant-as-plugin (ECC / gstack / oh-my-claudecode etc.)

## 2. The agent loop (ICLR 2025 formalization)

### Iterative step sequence

```
┌─────────────────────────────────────────────┐
│                                             │
│  User → Goal specification (NL task)        │
│                 │                           │
│                 ▼                           │
│  ┌─────────────────────────────┐            │
│  │ PERCEPTION                  │            │
│  │ Observe: files, terminal,   │            │
│  │ browser, IDE state          │            │
│  └────────────┬────────────────┘            │
│               │                             │
│               ▼                             │
│  ┌─────────────────────────────┐            │
│  │ ACTION SELECTION            │            │
│  │ LLM picks next action       │            │
│  │ (code edit / shell / browse │            │
│  │  / IDE / file op)           │            │
│  └────────────┬────────────────┘            │
│               │                             │
│               ▼                             │
│  ┌─────────────────────────────┐            │
│  │ SECURITY ANALYSIS (SDK)     │◀── Review  │
│  │ (pre-execution review)      │    hook    │
│  └────────────┬────────────────┘            │
│               │                             │
│               ▼                             │
│  ┌─────────────────────────────┐            │
│  │ SANDBOXED EXECUTION         │            │
│  │ Action runs in Docker       │            │
│  │ container (isolated)        │            │
│  └────────────┬────────────────┘            │
│               │                             │
│               ▼                             │
│  ┌─────────────────────────────┐            │
│  │ OBSERVATION                 │            │
│  │ Result → structured obj →   │            │
│  │ back into LLM context       │            │
│  └────────────┬────────────────┘            │
│               │                             │
│               └──→ Loop OR halt             │
│                                             │
└─────────────────────────────────────────────┘
```

### Typed Action + Observation

The SDK paper emphasizes **composable typed primitives** (inferred from abstract + production-grade framing):

- **`Action`** — dataclass with action kind + arguments. Examples:
  - `ShellAction(command: str)`
  - `FileReadAction(path: str)`
  - `FileWriteAction(path: str, content: str)`
  - `BrowserNavigateAction(url: str)`
  - `IDEAction(operation: str, args)`

- **`Observation`** — dataclass with result + metadata. Examples:
  - `CommandOutputObservation(stdout, stderr, exit_code)`
  - `FileContentObservation(content, line_count)`
  - `ErrorObservation(error_type, message)`

- **`Agent`** — base class; subclass + override `step(state) -> Action` for BYO

## 3. Docker-sandboxed runtime

### Isolation rationale

Arbitrary LLM-generated shell commands are dangerous on host. Storm Bear corpus has 5+ frameworks with sandbox-concern observations:
- [v13 gws](../../../googleworkspace-cli%20-%20Beginner%20Analysis/) AGENTS.md §6 adversarial-input-first validation
- [v14 paperclip](../../../paperclip%20-%20Beginner%20Analysis/) 5 invariants + promptfoo evals
- [v22 LlamaFactory](../../../LlamaFactory%20-%20Beginner%20Analysis/) Docker variants (CUDA+NPU+ROCm)
- [v24 Skyvern](../../../Skyvern%20-%20Beginner%20Analysis/) Playwright containerization
- [v27 oh-my-claudecode](../../../oh-my-claudecode%20-%20Beginner%20Analysis/) tmux CLI-worker architecture

OpenHands' Docker-sandbox is **native to the agent loop** — not a retrofit.

### Runtime portability (SDK paper claim)

Key SDK paper contribution: *"seamless local-to-remote execution portability."*

Same agent definition runs:
- **Local Docker** — developer laptop
- **Cloud hosted** — openhands.dev free tier + paid enterprise
- **Self-hosted Kubernetes** — enterprise tier with RBAC

Portability unlocks:
- Development/prod parity (local agent identical to deployed agent)
- Cost-optimal deployment (dev on laptop, prod in K8s cluster)
- Organizational flexibility (some teams cloud, some self-hosted)

### Corpus comparison

| Wiki | Runtime isolation | Portability |
|------|-------------------|-------------|
| v9 deer-flow | Internal infra | Self-hosted + Docker |
| v10 autoresearch | Git branch | Local-only (no cloud) |
| v14 paperclip | PGlite + Playwright | Local-to-Docker |
| v24 Skyvern | Playwright container | pip + Docker + Cloud |
| **v30 OpenHands** | **Docker-native + K8s** | **Local + Cloud + K8s (5 surfaces)** |

## 4. SDK composability (Nov 2025 paper)

### Design philosophy

SDK paper frames OpenHands as **"composable and extensible foundation for production agents"** — emphasizing Unix-style composition over monolithic framework. Paper claims *"minimal code for basic implementations while supporting advanced features."*

### Extensibility points

Inferred from paper abstract + production-grade framing:

| Extension point | Purpose |
|----------------|---------|
| **Custom Agent subclass** | BYO agent with domain-specific logic |
| **Custom Runtime adapter** | Integrate new execution backend (e.g., WebAssembly? cloud VM?) |
| **Custom LLM provider** | Add new model via routing abstraction |
| **Custom Action types** | Extend action vocabulary for new domain |
| **Pre-execution hooks** | Security analysis / audit logging / cost tracking |
| **Observation post-processing** | Context compression / summarization |
| **REST/WebSocket services** | Integrate agent into external app |

### Corpus comparison — composability

| Framework | Composability approach |
|-----------|----------------------|
| v11 BMAD | 5 modules + 12+ agents |
| v13 gws | Dynamic Discovery Service (runtime CLI tree) |
| v22 LlamaFactory | 9 training stages + 6 fine-tuning methods |
| v27 oh-my-claudecode | 8 modes + 19 agents |
| v28 markitdown | Format-scoped optional dependencies |
| **v30 OpenHands SDK** | **Typed Action/Observation + 7+ extension points + Python-import-based** |

## 5. Multi-interface environments (SDK paper)

### 3 first-class interfaces

- **CLI** — terminal-native (Claude Code-like)
- **VS Code** — agent sees + edits user's IDE state
- **VNC browser** — agent interacts with any GUI app via VNC

### VNC as novel primitive

**Corpus-first: VNC-based GUI-app-interaction as first-class agent capability.**

Storm Bear corpus prior agent-GUI primitives:
- v24 Skyvern: Playwright (browser-only, headless)
- v27 oh-my-claudecode: tmux CLI workers (terminal-only)
- v25 awesome-design-md: design-spec for AI-to-generate-UI (no interaction)

OpenHands VNC unlocks:
- Agent uses GUI apps humans use (IDE debuggers, Postman, Figma, DBeaver)
- No API/headless requirement
- Visual inspection of agent's actual browser state

## 6. Built-in security analysis

### Pre-execution review hook (SDK paper)

Unlike:
- Input sanitization (ex-post, filter inputs)
- Output sanitization (v13 gws Model Armor — ex-post, filter LLM outputs)
- Sandboxing (isolates damage but doesn't prevent)

OpenHands security analysis is **action-level pre-execution review** — agent's proposed `Action` is evaluated BEFORE runtime executes it.

### Likely implementation mechanisms

(Paper provides framing; specifics require codebase dive)
- Static analysis of shell commands for known-dangerous patterns (rm -rf /, fork bombs, exfil patterns)
- Policy-based allowlist/denylist per environment
- Human-in-the-loop approval for risky actions
- Audit log of all reviewed actions

### Corpus-first claim

First Storm Bear wiki with **agent-action-level security review in OSS core** as explicit product feature (not optional plugin, not proprietary cloud-only).

Comparison:
- v13 gws Model Armor = response-level, Google-cloud-managed
- v24 Skyvern anti-bot = Cloud-tier-only (proprietary)
- v30 OpenHands security analysis = **OSS + agent-level + pre-execution**

## 7. Lifecycle control (SDK paper)

### External observability of agent state

SDK paper claims **"lifecycle control"** as differentiator. Likely primitives:

- `agent.pause()` — suspend mid-step
- `agent.resume()` — continue from paused state
- `agent.state()` — introspect current loop phase
- `agent.history()` — retrieve action/observation sequence
- `agent.halt()` — graceful shutdown
- `agent.kill()` — force terminate

Consistent with enterprise-grade deployment (K8s orchestration, multi-user collaboration) requiring external control plane.

## 8. Production-grade vs research-prototype

### Structural differences

OpenHands explicitly positions SDK as **production-grade** (Nov 2025 paper claim) — distinct from:

- **Research prototype:** autoresearch v10 (Karpathy solo experiment)
- **Orchestration framework:** paperclip v14 (5 invariants but no K8s)
- **Specialized agent:** Skyvern v24 (browser-only)

Production-grade implies:
- Stability guarantees (SemVer + backward compatibility per 101 releases)
- Observability (lifecycle control + logging + metrics)
- Scale (Kubernetes deployment)
- Security (pre-execution review + sandbox + RBAC)

## 9. Storm Bear operator takeaway

**For building a Scrum-coach autonomous agent on OpenHands SDK:**

- SDK composability supports BYO Scrum agent class (subclass `Agent` with ceremony-specific logic)
- Docker sandbox keeps Scrum-coach experiments safe (accidental workspace operations contained)
- Multi-LLM routing means Anthropic / OpenAI / self-hosted open model all work
- Security analysis enables human-in-loop for client-facing coaching (don't let agent auto-commit to VN client repo)
- VNC potentially useful for Jira/Confluence interaction (many Scrum tools are web UIs without good APIs)

**Gap:** No Vietnamese-native documentation; VN Scrum context manually provided via system prompt.

## 10. References

- `README.md` (OpenHands/OpenHands main branch)
- ICLR 2025 paper: arXiv 2407.16741
- SDK paper: arXiv 2511.03690 (Nov 5, 2025)
- openhands.dev product page
- Sibling entity: [(C) All Hands AI Team + Open-Core Commercial + Governance](./(C)%20All%20Hands%20AI%20Team%20+%20Open-Core%20Commercial%20+%20Governance.md)
- Sibling cluster: [(C) Cluster — Core agent architecture + SDK + runtime sandbox](./(C)%20Cluster%20—%20Core%20agent%20architecture%20+%20SDK%20+%20runtime%20sandbox.md)
