# Cluster — Root README + 7-package monorepo + contribution gate

**Source:** `github.com/badlogic/pi-mono` root README.md + GitHub repository metadata + packages/ directory
**Fetch date:** 2026-04-23
**Cluster role:** Top-level user-facing positioning + monorepo architecture overview + contribution policy

---

## Summary

pi-mono is an open-source AI agent toolkit by Austrian developer Mario Zechner (better known as `@badlogic` / `@badlogicgames`, creator of the 25K-star libGDX Java game-dev framework). Published as a multi-package TypeScript monorepo under the `@mariozechner/*` npm scope, pi-mono contains **seven interconnected packages** that together form a complete Claude-Code-style coding-agent stack — with its own LLM provider abstraction, agent runtime, interactive terminal UI framework, web components, Slack bot integration, and GPU-pod vLLM deployment utility.

The flagship product is **pi-coding-agent** (installed via `npm install -g @mariozechner/pi-coding-agent`), which the root README directs new users to first. All other packages exist as either foundation layers (`pi-ai`, `pi-agent-core`, `pi-tui`, `pi-web-ui`) or spin-off products (`pi-mom` Slack bot, `pi-pods` GPU infra). The homepage `pi.dev` was donated to Mario by `exe.dev`.

At **38,950 stars / 4,542 forks / 200+ releases in 8.5 months** (created 2025-08-09, pushed today 2026-04-23), pi-mono sits among the largest solo-author T1 agent frameworks in the Storm Bear corpus — between agency-agents (82.9K solo) and crawl4ai (64K solo) at the high end, and claude-hud (20K solo) at the low end. Primary language is **TypeScript at 96.3%** with strict typing enforced (no `any`, no inline imports per AGENTS.md).

---

## 7-package monorepo structure (from README packages table)

| Package | npm name | Description |
|---------|----------|-------------|
| **ai** | `@mariozechner/pi-ai` | Unified multi-provider LLM API (OpenAI, Anthropic, Google, Mistral, Groq, Cerebras, xAI, OpenRouter, Vercel AI Gateway, Bedrock, Copilot, Azure, ZAI, OpenCode Zen, OpenCode Go, HuggingFace, Fireworks, Kimi, MiniMax + OpenAI-compatible = **20+ providers**) with type-safe tool definitions via TypeBox, cross-provider context handoffs, thinking-as-text normalization, cost tracking built-in |
| **agent** | `@mariozechner/pi-agent-core` | Stateful agent runtime with tool execution and event streaming (built on pi-ai); supports message queues for steering/follow-up, hook system (beforeToolCall/afterToolCall), tool-call barrier before preflight |
| **coding-agent** | `@mariozechner/pi-coding-agent` | **Flagship.** Interactive terminal coding agent CLI with ~25 flags, ~20 slash commands, ~15 keybindings, 7 built-in tools (read/write/edit/bash/grep/find/ls), 4 resource types (extensions, skills, prompt-templates, themes), ~38 configuration settings, session management with branching/forking, HTML export, GitHub-gist sharing |
| **mom** | `@mariozechner/pi-mom` | Slack bot that delegates @mentions to pi coding agent; Docker-sandboxed; per-channel conversation history + file workspaces; self-managing tool installation + credential configuration; event scheduling for reminders/periodic tasks |
| **tui** | `@mariozechner/pi-tui` | Minimal terminal UI framework with differential rendering (3 strategies), CSI 2026 synchronized output for flicker-free rendering, IME support for CJK input, overlay system, markdown rendering, inline image support (Kitty + iTerm2) |
| **web-ui** | `@mariozechner/pi-web-ui` | Web components for AI chat interfaces (built on pi-ai + pi-agent-core); ChatPanel + AgentInterface; IndexedDB-backed storage; JavaScript REPL + document extraction tools; attachment + artifact renderers; Tailwind CSS v4 + mini-lit web components |
| **pods** | `@mariozechner/pi-pods` | CLI for deploying/managing LLMs on GPU pods via vLLM with auto tool-calling config for Qwen/GPT-OSS/GLM; primary support DataCrunch (NFS) + RunPod (network volumes); Vast.ai / Prime Intellect / AWS EC2 / any Ubuntu+NVIDIA+SSH compatible |

**Lockstep versioning:** All packages share the same version number; every release bumps all 7 in sync. Release semantics are unusual — `patch` = bug fixes + new features, `minor` = API breaking changes, no major releases planned.

**Release cadence:** 200+ releases in ~8.5 months ≈ 23 releases/month (extreme velocity). Latest is v0.69.0 (2026-04-22).

---

## README key sections (annotated)

### Share your OSS coding agent sessions

Distinctive ethos. Mario explicitly requests OSS contributors share their pi session data to `badlogicgames/pi-mono` on Hugging Face via the companion tool `badlogic/pi-share-hf` (154 stars; created 2026-04-05). Quote: *"Public OSS session data helps improve coding agents with real-world tasks, tool use, failures, and fixes instead of toy benchmarks."* Links to his X posts explaining methodology.

This positions pi as a **data-generating project as well as a code-generating project**. Corpus-first in Storm Bear observation: no other framework explicitly requests session-data donation to a public HF dataset.

### Contribution gate

Root README opens with this warning:

> New issues and PRs from new contributors are auto-closed by default. Maintainers review auto-closed issues daily. See CONTRIBUTING.md.

This is enforced via three GitHub Actions workflows in `.github/workflows/`:
- `issue-gate.yml` — auto-closes issues from new contributors
- `pr-gate.yml` — auto-closes PRs from new contributors without PR rights
- `approve-contributor.yml` — maintainer approval keyword handler

Approval keywords (documented in AGENTS.md):
- `lgtmi` — grants future issue auto-close exemption
- `lgtm` — grants future issue auto-close exemption AND PR-submission rights

**CONTRIBUTING.md core requirement:** Contributors must comprehend their code. AI-generated code is accepted only if submitter fully understands it. Issues must use official GitHub templates and be:
- Single-screen length maximum
- Authentic voice (no templated language)
- Explicit problem statement
- Justification for why it matters
- Intent declaration if self-implementing

Repeated violations → permanent account blocking.

### Development commands

```bash
npm install          # Install all dependencies
npm run build        # Build all packages
npm run check        # Lint, format, and type check
./test.sh            # Run tests (skips LLM-dependent tests without API keys)
./pi-test.sh         # Run pi from sources (can be run from any directory)
```

Note: `npm run check` requires `npm run build` first (web-ui `tsc` needs `.d.ts` files).

### License

**MIT** — single-license repository; no dual-licensing (contrast Unsloth v23 dual Apache+AGPL).

---

## Monorepo metadata

- **Root files:** `.gitattributes`, `.gitignore`, `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE`, `README.md`, `biome.json`, `package-lock.json`, `package.json`, `pi-test.sh`, `test.sh`, `tsconfig.base.json`, `tsconfig.json`
- **Root dirs:** `.github`, `.husky`, `.pi`, `packages`, `scripts`
- **Homepage:** `pi.dev` (donated by exe.dev)
- **Discord:** `discord.gg/3cU7Bz4UPx` — community channel
- **CI:** GitHub Actions `ci.yml` workflow for build-on-push
- **Git hooks:** Husky for pre-commit enforcement (ties to `npm run check`)
- **Linter:** Biome (config `biome.json`)
- **TS config:** Extends `tsconfig.base.json` at root; each package has own `tsconfig.json`
- **Env var convention:** `PI_*` prefix (`PI_CODING_AGENT_DIR` / `PI_PACKAGE_DIR` / `PI_SKIP_VERSION_CHECK` / `PI_TELEMETRY` / `PI_CACHE_RETENTION`)
- **Project-local config:** `.pi/settings.json` overrides global `~/.pi/agent/settings.json`

---

## Cross-reference signals

- **Claude Code alternative positioning:** pi-coding-agent competes with Claude Code directly on feature surface (sessions, slash commands, tool use, extensions, model cycling). But pi is **model-provider-agnostic** (20+ via pi-ai) while Claude Code is Anthropic-subscription-native.
- **Not a Claude Code plugin:** unlike claude-hud v35 or OMC v27, pi does NOT use Claude Code's `/plugin marketplace` distribution. It is fully standalone.
- **Session-sharing to HF:** First corpus framework with explicit upstream-to-Hugging-Face-dataset OSS-session-sharing mechanism.
- **Author lineage:** Mario brings libGDX 15-year OSS-framework-maintenance expertise from game-dev to agent-space — cross-domain founder-equity signal (see entity page on Mario).

---

*(C) Claude-generated 2026-04-23 per routine v2.1.*
