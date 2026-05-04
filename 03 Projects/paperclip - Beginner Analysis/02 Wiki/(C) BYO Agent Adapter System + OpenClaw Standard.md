# (C) BYO Agent Adapter System + OpenClaw Standard

> **Type:** Entity — extensibility mechanism + companion-standard analysis
> **Parent:** [[(C) index]]
> **Sources:** [[(C) README summary]] §4; [[(C) AGENTS + ROADMAP + adapter-plugin cluster summary]] §4; package.json smoke scripts
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

paperclip is **explicitly multi-model agnostic** — the "Bring Your Own Agent" (BYO Agent) design treats any agent (OpenClaw / Claude Code / Codex / Cursor / Bash / HTTP endpoint) as a pluggable adapter. The **adapter-plugin refactor in progress** moves from hardcoded compile-time adapters to runtime-registered mutable registries. **OpenClaw appears as paperclip's companion agent standard** with 3 distinct runtime modes (join / docker-ui / sse-standalone), suggesting deeper integration than other adapters. This is **the most deliberate adapter-abstraction architecture in corpus** — paperclip's thesis is that orchestration is worth solving only if it's adapter-agnostic.

## 2. Key claims

1. **BYO Agent** — first-class feature: "any agent, any provider"
2. **6+ supported agent types** — OpenClaw / Claude Code / Codex / Cursor / Bash / HTTP endpoints
3. **Adapter refactor in progress** — moving from hardcoded to runtime-registered
4. **Mutable server + UI registries** — server authoritative, UI synchronized
5. **OpenClaw is special** — 3 smoke test modes (join / docker-ui / sse-standalone)
6. **OpenClaw referenced in other wikis** — codymaster v12 (install platform), confirms OpenClaw is independent adapter standard
7. **Hermes adapter externalization** (per fork note) — built-in adapter moved to plugin model

## 3. Evidence + sources

| Claim | Source | Confidence |
|-------|--------|-----------|
| BYO Agent feature | README §Features | High |
| Supported agents list | README §BYO Agent + package.json | High |
| Adapter refactor in progress | adapter-plugin.md + AGENTS.md fork note | High |
| Runtime registration architecture | adapter-plugin.md | High |
| OpenClaw 3 modes | package.json smoke scripts (join/docker-ui/sse-standalone) | High |
| OpenClaw independent | codymaster v12 README mentions OpenClaw as platform | Medium — corroborated |
| Hermes externalization | AGENTS.md §Fork Notes | High |

## 4. How it works — BYO Agent adapter architecture

### Adapter layers (inferred from adapter-plugin.md + AGENTS.md)

```
┌─────────────────────────────────────────────┐
│  Adapter Registry (server, authoritative)    │
│   - adapterType taxonomy                     │
│   - /detect-model routes                     │
│   - runtime registration API                 │
├─────────────────────────────────────────────┤
│  Individual Adapters                         │
│   - OpenClaw (3 runtime modes)               │
│   - Claude Code                               │
│   - Codex                                    │
│   - Cursor                                   │
│   - Bash (shell scripts)                     │
│   - HTTP endpoint (generic)                  │
│   - [plugin-contributed adapters]            │
├─────────────────────────────────────────────┤
│  paperclip orchestrator                      │
│   - Task assignment routes to adapter         │
│   - Adapter executes via its protocol         │
│   - Results return via standard interface     │
└─────────────────────────────────────────────┘
```

### Adapter responsibilities

Each adapter likely implements:
- **Capability detection** (`/detect-model`) — what can this adapter do?
- **Task execution** — receive task, run via agent, return result
- **Authentication** — adapter-specific auth (Claude API key, OpenClaw session, etc)
- **Cost reporting** — report tokens/dollars to paperclip's budget system
- **Heartbeat** — report status for monitoring
- **Termination** — respond to manual override signal

### Refactor: hardcoded → runtime

**Before (current main):** Adapters compiled into server at build time.

**After (adapter-plugin.md refactor):** Adapters registered at runtime.

**Benefits:**
- New adapters without server rebuild
- Plugin authors contribute adapters via plugin manifest
- Runtime validation of adapter availability
- UI stays synced with server's actual adapter state

**Status:** Refactor is **Phase 1** per adapter-plugin.md. Future phase integrates with plugin manifest/loader.

## 5. OpenClaw — companion standard

### OpenClaw's role

OpenClaw is referenced across multiple Storm Bear wikis:
- **codymaster v12** — listed as install platform (`OpenClaw support via symlink`)
- **paperclip v14** — primary example agent ("If OpenClaw is employee, Paperclip is company")
- **gws v13** — mentioned in README Quickstart (OpenCode/OpenClaw install path)

→ **OpenClaw is an independent agent-runtime standard**, not paperclip-internal.

### OpenClaw's 3 runtime modes (from paperclip smoke tests)

| Mode | Use case (inferred) |
|------|---------------------|
| **join** | Existing OpenClaw instance joins paperclip company (horizontal scale) |
| **docker-ui** | OpenClaw runs in Docker with UI-based interaction |
| **sse-standalone** | OpenClaw runs standalone with Server-Sent Events protocol |

paperclip smoke-tests all 3 modes → OpenClaw integration is first-class for all 3.

### Possible OpenClaw origins

Given name similarity (Open + Claw suggests open-source Claude-Code-like tool) and cross-project references:
- **Hypothesis A:** OpenClaw is the same team/ecosystem as paperclip (common org)
- **Hypothesis B:** OpenClaw is separate project that emerged as de facto standard
- **Hypothesis C:** OpenClaw is paperclip's internal code name for its agent reference implementation

None verified from README. Logged as open question (Q4).

## 6. Other adapters — named in README

### Claude Code
Anthropic's official Claude Code. Integration likely via Claude Code plugin interface. Treated as peer adapter, not privileged.

### Codex
OpenAI Codex / GPT Codex-style agent. HTTP-based likely.

### Cursor
Cursor IDE's agent mode. Integration path unclear — possibly via Cursor's HTTP server or subprocess.

### Bash
**Shell scripts as agents.** Radical abstraction — any executable shell command can be an agent. Enables "glue" scripts to participate in paperclip companies.

### HTTP endpoint
Arbitrary HTTP service. Paperclip POSTs task, service returns result. Enables any existing API to act as agent.

## 7. Hermes adapter externalization (fork note)

From AGENTS.md §Fork Notes:

> *"HenkDz/paperclip — externalized Hermes adapter branch removes built-in Hermes dependencies, allowing plugin-based registration through the Adapter Manager instead."*

**Reading:** Hermes was a built-in adapter. Fork removes it from core. Main repo likely follows.

**Open question (Q29):** What is Hermes? Possibilities:
- OpenAI's Hermes fine-tuned model family
- A specific agent implementation named Hermes
- Internal code name

## 8. Edges + failure modes

### Adapter refactor risks
- **Partial rollout** — some code paths use old hardcoded registry, others use new runtime registry → inconsistency
- **Registry synchronization** — server + UI registries can drift if not atomic
- **Plugin-contributed adapter bugs** — plugins can break paperclip stability
- **Security** — runtime-registered adapter gets full orchestration access; plugin authentication critical

### BYO Agent failure modes
- **Adapter misbehavior** — agent ignores cost reporting → budget hard-stop fails
- **Adapter slowness** — single slow adapter blocks company-wide throughput
- **Adapter version skew** — paperclip expects API v1; adapter ships v2
- **Adapter auth leakage** — credentials stored in paperclip config may leak

### OpenClaw-specific risks
- OpenClaw stability unknown (external project)
- 3-mode complexity — each mode has own failure surface
- SSE-standalone requires paperclip to manage long-lived SSE connection

## 9. Related concepts

- [[(C) Zero-Human Companies Orchestration + Governance Layer]] — what uses adapters
- [[(C) Skills + Architecture + package.json cluster summary]] — technical substrate including smoke tests
- [[(C) AGENTS + ROADMAP + adapter-plugin cluster summary]] — refactor context

## 10. Cross-project comparison

### vs T4 peer (gws v13 Dynamic Discovery)

Both paperclip adapter system + gws Dynamic Discovery = runtime-configurable integration layers.

| Aspect | gws Dynamic Discovery | paperclip BYO Adapter |
|--------|----------------------|------------------------|
| **What's dynamic** | API command surface | Agent runtime identity |
| **Source of schema** | Google Discovery JSON | Adapter self-reports via /detect-model |
| **Integration direction** | Bridge to external services | Orchestrate external agents |
| **Maturity** | Production-stable | In-flight refactor |

→ Convergent pattern at different abstraction layers. Both move from compile-time to runtime.

### vs BMAD v11 platform support

BMAD supports Claude Code + Cursor + Augment + Junie as IDE platforms (4).
paperclip supports 6+ as agent adapters (OpenClaw + Claude Code + Codex + Cursor + Bash + HTTP).

**Different scope:** BMAD = which IDE hosts the methodology; paperclip = which agent runs the task.

### vs T1 frameworks — adapter philosophy

Most T1 frameworks privilege one agent host (Claude Code typically). paperclip is **agent-agnostic from the start.** Architectural commitment reflects company-level orchestration use case — a company might employ workers with different skills (different agents for different tasks).

## 11. Open questions

- OpenClaw identity (Q4)
- Hermes adapter meaning (Q29)
- Adapter refactor completion timeline (Q20)
- Plugin manifest integration with adapters (Q20)
- Adapter security model (new — Q35)
- Adapter versioning strategy (new — Q36)
- OpenClaw 3 modes — which is production-preferred? (Q11)

## 12. Decision log

- **Pre-paperclip design:** chose multi-model-agnostic as core thesis
- **Early implementation:** adapters hardcoded (simpler)
- **Current:** refactor in-flight — runtime registration
- **Hermes externalization:** externalized (fork branch); likely merged to main eventually
- **Future:** plugin-contributed adapters via manifest system

## 13. Storm Bear relevance

- **Technical pattern applicable** — runtime adapter registration is good pattern for any extensible system
- **OpenClaw** — if companion standard to paperclip, worth investigating separately (cross-wiki opportunity — could be 15th wiki if corpus ever validates T6 agent-runtime tier)
- **Multi-agent orchestration** — if Storm Bear ever builds agentic workflows, paperclip's BYO model avoids lock-in
- **Hermes reference** — check if Hermes relates to Nous Research's Hermes model family (unverified)

## References

- README.md §Features (BYO Agent)
- adapter-plugin.md
- AGENTS.md §Fork Notes (Hermes)
- package.json scripts (OpenClaw smoke tests)
- Parent: [[(C) index]]
- Cross-wiki OpenClaw references:
  - `../../codymaster - Beginner Analysis/02 Wiki/(C) README + VN summary.md` §5
  - `../../googleworkspace-cli - Beginner Analysis/02 Wiki/(C) README summary.md` §3
