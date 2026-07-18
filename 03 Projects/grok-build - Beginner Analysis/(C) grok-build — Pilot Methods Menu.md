# (C) grok-build — Pilot Methods Menu (24 methods)

> `xai-org/grok-build` · v215 · 2026-07-18
> **Honest framing:** grok-build is on-goal (Goal #1) but its value is **read-the-source + borrow-the-architecture**, not run-it. Running it needs a **paid SuperGrok / X Premium Plus subscription** and is **Grok-4.5-locked** (it does not run Claude). The **source is free (Apache-2.0)**; the **runtime is paid + Grok-only**. There is **no direct hireui product pilot** here — grok-build is a competitor dev tool, and its own working-dir-upload privacy history + hireui's CONSTITUTION mean **do NOT point it at hireui**.
> **⭐ One-thing path: A1 → B7 → (optional) C12.** Read the worktree-subagent orchestrator source → borrow the architecture into your own multi-agent-orchestration thread → (subscribers only) trial it on a scratch repo.

---

## A — Read & learn (free, zero install; the real payoff)
1. **⭐ A1 — Read the worktree-parallel-subagent orchestrator source.** Clone the Apache-2.0 repo (read-only), find the crates for the agent runtime + subagent spawning + the orchestrator-reconciliation logic. This is the corpus's **best-yet reference for how a frontier lab implements worktree-isolated multi-agent orchestration** (8 subagents, each in its own git worktree/branch, reconciled at the end). Zero cost.
2. **A2 — Read the sandbox implementation.** How does grok-build sandbox shell/file operations? A source-verifiable model for "let an agent run bash safely."
3. **A3 — Read the ACP + MCP host layers.** How a coding agent embeds in an editor (Agent Client Protocol) and hosts MCP servers (consumer side). Compare to how Claude Code does it.
4. **A4 — Read the Plan Mode + skills/hooks implementation.** SpaceXAI adopted the Anthropic-pioneered primitive stack — read how a second vendor implements skills/subagents/hooks/plan-mode, as a cross-check on the conventions.
5. **A5 — Compare grok-build's Rust to Codex CLI's Rust.** Both are large open Rust vendor coding CLIs (~844K vs ~950K LOC). A landscape study of two frontier labs' harness designs.
6. **A6 — Read the tool set** (grep/file-ops/bash + the Mermaid renderer). "Tools adapted from Codex" — see what a mature agent tool surface looks like.

## B — Borrow patterns (zero install, into the vault / the operator's own work)
7. **⭐ B7 — Borrow the worktree-isolated-parallel-subagent + orchestrator-reconciliation architecture** into your **multi-agent-orchestration pilot thread** (composes with **devspace v171** git-worktree + **loop-engineering v189** loop patterns + the vault's own Workflow/parallel patterns). The single highest-leverage steal.
8. **B8 — Borrow the "subagents with separate prompts, reconciled by an orchestrator"** design as a template for a vault review/verify fan-out (each subagent a distinct lens; cf. the vault's loop-verifier).
9. **B9 — Borrow the marketplace / "bundle skills+agents+hooks+MCP behind one install"** packaging idea for the vault's own `05 Skills/` distribution thinking.
10. **B10 — Borrow the sandbox model** as a reference for any future "let an agent run shell" work.
11. **B11 — Document the agent-primitive convergence** (skills/subagents/hooks/plan-mode/MCP are now cross-vendor) into the vault's agent-skills notes — the Claude Code design vocabulary is the industry standard.
12. **B12 — Write a "how frontier labs build coding CLIs" synthesis** across grok-build + Codex CLI + Gemini CLI + Claude Code (v65) for the vault.

## C — Hands-on trial (⚠️ requires a paid SuperGrok / X Premium Plus subscription; Grok-locked)
13. **⭐ C12 — Trial grok-build on a scratch repo** (install-snapshot first; `curl -fsSL https://x.ai/cli/install.sh | bash`) to feel the native-subagent-view + Plan Mode + fullscreen TUI UX as a **Claude Code alternative**. Evaluating-a-competitor-harness. **Scratch repo only.**
14. **C13 — Trial the 8-worktree parallel-subagent flow** on a scratch repo with 3–4 independent tasks; observe how the orchestrator reconciles.
15. **C14 — Trial headless/CI mode** on a throwaway task; compare to Claude Code headless.
16. **C15 — Trial the ACP editor embedding** (e.g. in Zed) on a scratch project.
17. **C16 — Trial an MCP server** (Postgres/browser) hosted inside grok-build on scratch data.
18. **C17 — Bake-off: same scratch task, grok-build vs Claude Code.** A structured comparison (speed, plan quality, subagent UX, cost). Note grok-build cost is a Grok subscription, not per-token-Claude.

## D — Goal-#2 (hireui) — read/borrow ONLY, do NOT run against hireui
19. **D19 — Borrow (via A1/B7) the orchestration architecture** as a reference for any future hireui agent work — **on paper**, not by running grok-build. hireui stays Claude-Code per its CONSTITUTION (I-8 operator-installs / I-2 `agent-*` branch / GitNexus-first).
20. **D20 — ⚠️ Do NOT point grok-build at hireui or any candidate data.** Its own working-dir-upload history + candidate PII + the CONSTITUTION make this out of bounds. Recorded as an explicit anti-method.
21. **D21 — Use grok-build's sandbox design as input** to hireui's future "can an agent safely run shell?" ADR (read-only reference).

## E — Personal / off-goal
22. **E22 — Use grok-build as your personal coding agent** (if you subscribe to SuperGrok anyway) on your own side projects — off the vault's goals, a personal-tooling choice.
23. **E23 — Follow the SpaceXAI/Grok landscape** (the xAI→SpaceXAI rebrand, Grok 4.5, the SpaceX-in-orbit-compute thesis) as competitive-landscape awareness.

## F — Vault-meta
24. **⭐ F24 — File the coding-agent-products meta-cluster question for the ~v221 audit** (Kilo Code v177 IDE-extension + grok-build v215 vendor-terminal-CLI + CodePilot v161 GUI-wrapper — cluster or keep 3 standalones?) + the NO-MINT-generalize-Kilo-Code-to-N=2 reviewable alternative + the model-vs-harness tier note (Grok 4.5 model / grok-build harness).

---

## Fence (mandatory for any C-tier trial)
- **install-snapshot** before `curl -fsSL https://x.ai/cli/install.sh | bash` or `irm https://x.ai/cli/install.ps1 | iex` (prebuilt binary from x.ai).
- **⚠️ Verify the Google-Cloud-upload path is disabled + data retention is off by default + review the sandbox config** before pointing it at any real repository (the working-dir-upload privacy history is the load-bearing risk).
- **Scratch repo ONLY.** Never run it against hireui, the vault, or any repo with candidate/sensitive data.
- **Apache-2.0 source is safe to READ + borrow patterns from.** It is a **source-available one-way mirror** — read/fork/borrow, don't try to contribute (no PRs).
- **Running it requires a paid SuperGrok / X Premium Plus subscription** and is **Grok-4.5-locked** (it does not run Claude) — budget accordingly.
- **Pin the commit** (0 releases).
- hireui stays **Claude-Code per its CONSTITUTION**; grok-build is a reference/borrow subject only.
