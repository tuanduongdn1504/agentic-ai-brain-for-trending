# (C) grok-build — Deep Dive

> LLM Wiki **v215** · built 2026-07-18 · subject `xai-org/grok-build`
> Verdict produced **INLINE + fully hand-verified** per `feedback_wiki_verify_independently_check_collisions` — **no workflow / no subagent** (the ~205K shim overflows subagent context → prompt-too-long; the v200→v214 self-throttle). Source hand-fetched (repo page + raw README + Simon Willison's write-up); identity + the SpaceXAI rebrand by independent WebSearch; collision + the near-neighbor distinctions by sanity-anchored hand-grep of `_state/` + `_patterns/`.

---

## 1. One-line

`xai-org/grok-build` — **SpaceXAI's (formerly xAI's) open-sourced, terminal-based AI coding agent** — a full-screen Rust TUI that understands your codebase, edits files, runs shell commands, searches the web, and manages long-running tasks (interactively, headlessly for CI, or embedded in editors via the Agent Client Protocol), powered by **Grok 4.5**. Released as full **Apache-2.0** source on **2026-07-15**. It is **Grok's Claude Code** — a first-party frontier-lab agentic coding CLI, the peer class of Claude Code / Codex CLI / Gemini CLI.

**Tagline (repo/README, verbatim):** *"Grok Build is SpaceXAI's terminal-based AI coding agent. It runs as a full-screen TUI that understands your codebase, edits files, executes shell commands, searches the web, and manages long-running tasks — interactively, headlessly for scripting/CI, or embedded in editors via the Agent Client Protocol (ACP)."*
**Repo description:** *"SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible."*

---

## 2. Identity (independently verified)

- **Author / org:** **SpaceXAI** (formerly **xAI**; GitHub org `xai-org`) — **Elon Musk's AI company**, **NOT Anthropic**.
- **The "SpaceXAI" name is a genuine 2026 rebrand** (WebSearch-confirmed, not a fetch artifact): SpaceX absorbed xAI in an all-stock deal on **2026-02-02** (combined group valued ≈ **$1.25 trillion** — reported as the largest private merger on record); the public rebrand xAI → **SpaceXAI** formalized on ≈2026-07-06. **Grok keeps its name** (the assistant, the SuperGrok subscription, the API). The repo brands itself "SpaceXAI" throughout, consistent with the rebrand.
- **Model:** powered by **Grok 4.5** (xAI/SpaceXAI's model; announcement-stated). grok-build is the **harness**, not the model.
- **First `xai-org` / SpaceXAI author in the corpus** (§19 19a) — the corpus's first Elon-Musk-company subject. (Grok/Grok Build had appeared only as a *landscape mention* — in CLIProxyAPI **v207**, whose Go proxy reverse-engineers "Grok Build"'s OAuth. Never a subject until now.)

---

## 3. What it is / does

A **terminal-first, autonomous AI coding agent** (the Claude Code / Codex CLI / Gemini CLI category). Point it at a codebase and it:

- **Understands the codebase**, **edits files**, **executes shell commands**, **searches the web**, and **manages long-running tasks**.
- Runs three ways: **interactive full-screen TUI** (mouse-interactive), **headless** (scripting/CI), or **embedded in editors** via the **Agent Client Protocol (ACP)** (Zed's open protocol for editor↔agent embedding).
- **Native subagent view + Plan Mode** integration + a fullscreen mouse-driven terminal UI.

### The headline architectural feature — worktree-isolated parallel subagents
Grok Build can spawn **up to 8 concurrent sub-agents, each running in its own Git worktree on a separate branch** of your codebase. They work in parallel — one rewrites the auth flow, another updates tests, a third refactors a schema migration — and an **orchestrator agent reconciles their outputs at the end** (announcement-stated). This is a source-verifiable reference implementation of worktree-isolated multi-agent orchestration.

### Extensibility surface (the Anthropic-pioneered primitive stack, adopted by SpaceXAI)
- **MCP servers** (host/consumer side — Linear, Sentry, Postgres, browsers, "anything with MCP").
- **Skills, agents, hooks, plugins** — the same agent-primitive vocabulary Claude Code introduced.
- A **marketplace**: *"Bundle skills, agents, hooks, and MCP servers behind one install · Marketplace install, or self-host from any git repo."*
- **Sandbox environments**, theming, slash commands, keyboard shortcuts, authentication.
- Documentation at `docs.x.ai/build/overview`.

---

## 4. Engineering substance (source-verified where noted; NOT cloned)

- **Language:** **Rust 99.6%** (other 0.4%). Organized as a **multi-crate Rust workspace** — TUI layer, agent runtime, tool implementations, workspace management, configuration. Bin crate `xai-grok-pager-bin`.
- **Scale:** **≈844,530 lines of Rust** (Simon Willison-stated, from a clone; he notes this is *larger than he expected* and compares it to OpenAI's Codex at ≈950,933 lines — "terminal coding agents are significantly more complex than I had realized"). ⚠️ Line count is **Simon-stated**, not independently re-counted here (no clone — shim-overflow self-throttle).
- **Tools:** grep, file operations, bash; **tool sets adapted from Codex and other agents** (Simon-stated); a **Mermaid-diagram terminal renderer**; **subagents with separate prompts**.
- **License:** **Apache-2.0** for first-party code; third-party deps retain their licenses (`THIRD-PARTY-NOTICES`).
- **Build from source:** Rust (pinned via `rust-toolchain.toml`) + **DotSlash** (hermetic tool management) + **protoc** (protobuf codegen). `cargo run -p xai-grok-pager-bin` (launch TUI) / `cargo build -p … --release` / `cargo check -p …`.
- **Install (prebuilt binary):** macOS/Linux/Git Bash `curl -fsSL https://x.ai/cli/install.sh | bash`; Windows PowerShell `irm https://x.ai/cli/install.ps1 | iex`.

### Metrics (GitHub page-stated §37.4 — the API is mocked in this environment → NOT a #52 velocity claim)
- **≈16.6k stars · ≈3.1k forks · 0 releases · 123 watchers.** Just open-sourced (2026-07-15), so "0 releases" reflects newness, not abandonment.

---

## 5. Open-source status — genuinely open license, but a one-way mirror

- **The full codebase is released under Apache-2.0** — Simon Willison: *"genuinely open-source… the entire Grok Build codebase."*
- **BUT it is a source-AVAILABLE, read-only mirror**: the README states the repo is *"synced periodically from the SpaceXAI monorepo"* and **external contributions are NOT accepted** (`CONTRIBUTING.md`). So: a permissive license you may read/fork/borrow from, delivered as a one-way mirror with no PRs. Both facts are true and reported together.

## 6. The privacy incident (report faithfully — a real trust caveat)

grok-build was open-sourced (2026-07-15) **following a privacy backlash**: earlier versions **uploaded working directories to Google Cloud unintentionally** (Simon-stated + widely reported). In the current code that **upload functionality is disabled** and **data retention is off by default**. This history is the load-bearing #66 fence point: verify the upload path is disabled and retention is off before pointing the tool at any real repository.

---

## 7. Availability / cost

- **Early beta** for **SuperGrok** and **X Premium Plus** subscribers (announcement-stated). To actually *run* grok-build you need a paid SpaceXAI/xAI subscription — it is **vendor-locked to Grok 4.5** (it does not run Claude). The **source is free to read** (Apache-2.0); the **runtime is paid + Grok-only**.

---

## 8. Where it sits vs the corpus (the distinctions that decide the pattern outcome)

Grok Build is an **interactive AI coding-agent PRODUCT** — but a *different sub-class* from every prior corpus coding-agent standalone:

| Corpus standalone / subject | What it is | Why grok-build ≠ it |
|---|---|---|
| **Kilo Code v177 §C** — "Open-Source **IDE-Embedded Multi-Model** AI Coding-Agent Platform (Cline/Roo/Cursor peer class)" | third-party VS Code/JetBrains extension + CLI; routes to 500+ providers, switchable mid-task | grok-build is **first-party** (SpaceXAI's own), **single-model** (Grok-4.5-locked), **terminal-TUI-first**. It fails Kilo Code's own N=2 scope criterion ("a 2nd open-source **IDE-embedded** interactive **multi-model** coding-agent"). |
| **Agent-Native Vendor CLI v143 §C** — `larksuite/cli` | a product's CLI **re-architected so an external agent can DRIVE it** (agent → Lark's CLI) | grok-build **IS the agent**, not a tool an agent consumes. Opposite direction. |
| **CodePilot v161 §C** — Desktop GUI Client wrapping a CLI agent | a GUI front-end around Claude Code | grok-build **IS the coding agent**, not a wrapper. |
| **Multi-Vendor Orchestration Platform v150/v163 §C** — Paseo / ai-maestro | orchestrates **multiple third-party agents** as units | grok-build is **one agent** (that orchestrates its own worktree subagents). |
| **DeepSeek-TUI v72** | a third-party terminal **chat client** for a competitor model | grok-build is a full **agentic coding harness** (file-edit/shell/subagents), not a chat TUI. |
| **OpenHands v30** | autonomous SWE-agent **platform** (sandbox/batch/SDK/cloud) | grok-build is a vendor's **interactive terminal CLI**, not a platform. |
| **GLM-5 v176 / DeepSpec v186** | competitor frontier **models / inference substrate** | Grok 4.5 is the model analogue; **grok-build is the harness**, not the model. |

**Net:** the surface *"a frontier AI lab's own, first-party, fully-open-sourced agentic coding CLI/TUI — studiable as a primary subject"* is **corpus-unrepresented** (grep for `terminal coding agent` / `vendor coding CLI` / `frontier-lab` in §C = **0 hits**). It is **NOT world-first** — Claude Code (closed), Codex CLI (OpenAI, open Rust), Gemini CLI (Google, open), Qwen Code all precede as vendor coding CLIs. grok-build is the corpus's **first such SUBJECT**, and one of the open-source ones.

---

## 9. Cross-references (d)

- **Kilo Code v177** — the direct §C sibling/contrast (third-party IDE-extension coding-agent product ↔ grok-build's first-party vendor terminal CLI).
- **multi-agent-orchestration pilot thread** + **devspace v171** (git-worktree parallel sessions) + **loop-engineering v189** — grok-build's 8-worktree-subagent + orchestrator design is a source-verifiable reference for all three.
- **agent-skills substrate** — agent-skills-standard v76 / agent-skills v184 / ponytail v168 / the MCP host layer. grok-build **adopts the Anthropic-pioneered primitive stack** (skills, subagents, hooks, plan mode, MCP) → a convergence data-point: the Claude Code design vocabulary has become the cross-vendor standard.
- **CLIProxyAPI v207** — reverse-engineers Grok Build's OAuth (grok-build was a v207 landscape mention; now a subject — corpus-recursive cross-ref, **NOT #57**: v207 mentions grok-build, not the reverse).
- **cc-switch v73 / ai-switcher v153** — the LLM-access-tooling family.
- **DeepSeek-TUI v72 / fff v194 / meetily v196** — the Rust(-TUI) neighbors.
- **claude-code-system-prompts v65** — the "understand how Claude Code works" thread; grok-build is the full IMPLEMENTATION analogue (read the source, not just the prompts).
- **hireui (Goal #2)** — thin: grok-build is a competitor dev tool, not a product feature. The only hireui-adjacent value is the orchestration architecture as a reference (borrowed by reading the source), NOT running grok-build against hireui (candidate PII + hireui's CONSTITUTION says Claude Code / operator-installs + grok-build's own working-dir-upload history).

---

## 10. Honest caveats

- **NOT source-cloned** — WebFetch/README/Simon-Willison/docs-verified only (the ~205K shim overflows subagent context → no clone-and-workflow, the self-throttle). Line count, "tools adapted from Codex," and the worktree-subagent details are page/Simon/announcement-stated.
- **0 releases / early beta** — just open-sourced; API-mocked stars → NOT #52.
- **Source-available one-way mirror** (no contributions) + **vendor-Grok-locked + paid to run**.
- **The privacy history** (working-dir uploads to Google Cloud, now disabled) is real — treat as a trust fence, not a footnote.
- **"SpaceXAI" / Grok 4.5** — corporate identity + model version are WebSearch/announcement-verified but move fast.

**See `(C) grok-build — Verdict.md` for the GOAL-ALIGNED assessment + pattern outcome, and `(C) grok-build — Pilot Methods Menu.md` for the 24-method pilot ladder.**
