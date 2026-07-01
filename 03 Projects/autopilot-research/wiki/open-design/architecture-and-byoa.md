# Architecture & bring-your-own-agent (BYOA)

## Source

`nexu-io/open-design` README + `docs/agent-adapters.md`, `docs/architecture.md`, `docs/skills-protocol.md`, `AGENTS.md` (fetched via gh api / WebFetch, 2026-07-01, Workflow `wf_4a91a8b2-2bb` agents `multica`, `opendesign-arch`, `license-security`). The daemon-architecture lineage is credited to [`multica-ai/multica`](https://github.com/multica-ai/multica) → [[open-design/the-originals]].

## The shape of it

```
 Desktop app / browser (Next.js UI, sandboxed iframe preview)
        │  HTTP + SSE
 ┌──────▼─────────────────────────────────────────────┐
 │  Local daemon  (Node 24 · Express · SSE · SQLite)   │  ← binds 127.0.0.1 by default
 │                                                     │
 │   ├─ Adapter layer (apps/daemon/src/agents.ts)      │  detect() / capabilities() / run()
 │   │    spawns your CLI via execFile (no shell)      │
 │   │    Claude Code · Codex · Cursor · Copilot ·     │
 │   │    Gemini · OpenCode · Qwen · Kimi · Hermes …   │
 │   │                                                 │
 │   └─ BYOK proxy  POST /api/proxy/{anthropic,openai, │  ← for "no CLI installed"
 │        azure,google,ollama,senseaudio}/stream       │    OpenAI-compatible endpoints
 │                                                     │
 │   Storage: better-sqlite3   Creds: config.toml 0600 │
 └─────────────────────────────────────────────────────┘
        │ reads
   Filesystem of composable content:
   skills/*/SKILL.md  ·  design-systems/*/DESIGN.md  ·  plugins (open-design.json)
```

## 1. The daemon (the only privileged process)

- **Stack:** Node 24 · Express · **SSE** streaming · **`better-sqlite3`** storage.
- **Binds `127.0.0.1` by default** (loopback only). LAN exposure is opt-in and requires **both** `OD_BIND_HOST` *and* `OD_ALLOWED_ORIGINS` to be set explicitly.
- It is the *single privileged process* — the pattern inherited from **multica**. The UI talks to it; it spawns agents and holds credentials; nothing else is trusted.

## 2. PATH-scan agent detection + the adapter contract

The defining BYOA mechanism. On startup the daemon **scans your `PATH`** for known coding-agent CLIs and lists the ones it finds (the video's demo detected four: Claude Code, OpenCode, Copilot CLI, Kilo). Each supported CLI is one **adapter** entry in `apps/daemon/src/agents.ts`; the README's claim is **"adding a new CLI is one entry."**

The adapter contract is a three-phase interface (`docs/agent-adapters.md`):

| Phase | Method | Job |
|---|---|---|
| Discovery | `detect()` | is this CLI on the PATH? which version? |
| Capability negotiation | `capabilities()` | what does it support (tools, streaming, models)? |
| Execution | `run(params)` | spawn it (`execFile`, **no `shell: true`**) and yield `AgentEvent` objects |

**Skill injection** happens via one of three strategies (preference-ordered): native skill loading → prompt injection → file-placed workflow. This is how a `SKILL.md` reaches a CLI that has no native skill concept.

**Named agents (platform table, 15):** Claude Code, Codex, Cursor, VS Code Copilot, Copilot CLI, Gemini, OpenCode, OpenClaw, Antigravity, Cline, Trae, Kimi, Pi Agent, Mistral Vibe, Hermes Agent. The hero image claims **21** (adding Grok Build, Qwen, Qoder, Kiro, Kilo, DeepSeek, Reasonix, Aider, Devin). Reconcile as: **~15 first-class native adapters + more via BYOK proxy**; the exact number is a moving target (see [[open-design/caveats-and-safety]]).

## 3. The BYOK proxy (no-CLI fallback)

If you have no coding-agent CLI, the daemon exposes `POST /api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream` — paste a `baseUrl` + `apiKey` + `model` for OpenAI, Anthropic, Azure OpenAI, Google Gemini, Ollama, LM Studio, vLLM, or any OpenAI-compatible endpoint. Same loop, no process spawn. (README also advertises **per-target SSRF protection** at the proxy edge — see the caveat below.)

## 4. The three-layer composition model

Open Design separates *three* kinds of content, each contributable independently:

1. **Plugins** carry **runnable workflows** (an `open-design.json` manifest: marketplace metadata + inputs + pipeline + capabilities).
2. **Skills** embody the **agent's design taste** — a `SKILL.md` folder (the Claude Code convention) extended with an **`od:` frontmatter block** (`mode`, `platform`, `scenario`, `preview.type`, `design_system.requires`, `default_for`, `fidelity`, `example_prompt`).
3. **Design systems** encode **brand tokens** — a portable **`DESIGN.md`** (see [[open-design/design-md-as-source-of-truth]]).

At generation time the prompt is composed as a stack: **`BASE_SYSTEM_PROMPT` + `DESIGN.md` + `SKILL.md`**. Swapping the skill or design system in the top bar changes the next send (cached in-memory per session). This is the concrete "harness" — the model is a swappable slot; the skills + design system are what you actually tune.

## 5. MCP integration (`od mcp install`)

Beyond driving CLIs directly, Open Design ships an **MCP stdio server** that exposes design files as a queryable API. One line — **`od mcp install <agent>`** — wires that server into a coding agent's config (supports `--print` dry-run and `--uninstall`). This is how your Claude Code session *inside another repo* can reach Open Design's skills/design-systems.

## 6. Security posture (what to actually check)

- ✅ **Loopback by default** (`127.0.0.1`); LAN needs explicit `OD_BIND_HOST` + `OD_ALLOWED_ORIGINS`. Connector credentials + live-artifact preview routes stay loopback-only regardless.
- ✅ **Credentials** stored locally in `config.toml` (mode **`0600`**) or browser localStorage; the README states they are **never sent to Open Design's own servers**.
- ✅ **`execFile` without `shell: true`** for agent spawning — avoids shell injection. Privilege model is *agent-delegated* (the daemon spawns the CLI; the CLI does file writes), so it's only as safe as the CLI you point it at.
- ✅ **Postinstall script is safe** (decompresses a bundle + local builds; **no network calls** — verified by the `license-security` agent).
- ⚠️ **"No telemetry" is really opt-in PostHog** — a no-op unless `POSTHOG_KEY` is set, and disableable in settings, but the blanket "no telemetry" README wording is imprecise.
- ⚠️ **SSRF protection is *claimed* but not confirmed** in the HTTP adapter code the skeptic read — the loopback-only default is your actual mitigation.

Full risk treatment + install precautions: [[open-design/caveats-and-safety]].

## Key Takeaways

- The **local daemon is the whole trick**: it PATH-scans for your coding-agent CLIs and drives them through a one-entry-per-CLI **adapter contract** (`detect/capabilities/run`), or falls back to a **BYOK proxy** for raw endpoints.
- **Three separable layers** — plugins (workflows) · skills (`SKILL.md` taste) · design-systems (`DESIGN.md` tokens) — compose into the prompt as `BASE + DESIGN.md + SKILL.md`. The model is the swappable part.
- The architecture is **borrowed from `multica-ai/multica`** (a general agent-orchestration daemon, Jan 2026), applied to the design vertical.
- Security is **sound-by-default but over-claimed in prose**: loopback binding, `0600` creds, and shell-less spawning are real; "no telemetry" (opt-in PostHog) and "SSRF protection" (unconfirmed in code) are the two claims to verify yourself before exposing it beyond localhost.
