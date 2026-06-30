# Sand Castle deep-dive — `@ai-hero/sandcastle`

## Source

The **load-bearing new original** of the podcast. Deep-dived directly against the repo via `gh api`: **[mattpocock/sandcastle](https://github.com/mattpocock/sandcastle)** — *"Orchestrate sandboxed coding agents in TypeScript with `sandcastle.run()`."*

> ⚠️ One verification agent claimed Sand Castle was "fabricated" (it searched "Sand Castle" with a space and missed the repo). **Overridden** — the repo demonstrably exists and was deep-read in full. See [[pocock-agentic-workflow/source-provenance]].

## What it is

A **TypeScript library for running AI coding agents inside isolated sandboxes**. It abstracts the lifecycle of sandboxed agent execution — branch strategy, git-worktree management, commit collection, session capture — so you can spin up an agent, let it work, and pull its commits back to the host. This is the **engine behind Matt's AFK / queue workflow**: it's how he parallelizes agents safely instead of letting a raw agent loose on his machine.

## Verified facts (gh api, 2026-06-29/30)

- **npm package:** `@ai-hero/sandcastle` (scoped to avoid collision with an unrelated unscoped `sandcastle` on npm). Install: `npm install --save-dev @ai-hero/sandcastle`.
- **Version:** 0.12.0 · **License:** MIT · **Language:** TypeScript 100% · **Stars:** 6,519 · **Forks:** 649 · **Open issues:** 68 · **Created:** 2026-03-17 · actively pushed (2026-06-29).
- **Release cadence:** ~50 version entries in the CHANGELOG (0.1.x → 0.12.0) — very active. 0.12.0 bumped the default Claude Code model **opus-4-7 → opus-4-8**.
- **Maturity signals:** ~53 test files (~48% of ~110 TS files); **20 ADRs** (Architecture Decision Records, 0001–0020); built on the **Effect** framework for async coordination.

## The mechanism

- **Entry points:** `run()`, `interactive()`, `createSandbox()`, `createWorktree()`. Canonical call:
  ```ts
  import { run, claudeCode, docker } from "@ai-hero/sandcastle";
  await run({ agent: claudeCode("claude-opus-4-8"), sandbox: docker() });
  ```
- **5 built-in sandbox providers:** **Docker** (bind-mount), **Podman** (bind-mount), **Vercel** (cloud Firecracker microVMs via `@vercel/sandbox`), **Daytona** (isolated; present but lightly documented), and **no-sandbox** (host passthrough — *unsafe for AFK*, dev only). Custom providers via `createBindMountSandboxProvider` / `createIsolatedSandboxProvider`.
- **6 agent providers (provider-agnostic):** Claude Code, OpenAI Codex, Pi, Cursor, OpenCode, GitHub Copilot CLI. (The podcast frames it around Claude Code, but it isn't Claude-only.)
- **`fork()`** continues from the last captured session under a new session id, leaving the parent's session JSONL untouched — enabling **parallel agents** (`Promise.all([parent.fork(a), parent.fork(b)])`). Documented in ADR-0018 ("fork-is-session-only"). Concurrent forks need an explicit `branch` strategy.
- **Three branch strategies for getting commits back to the host:**
  - `head` — agent writes directly to the host working directory;
  - `merge-to-head` — agent works on a temp branch, merged back to HEAD when done;
  - `branch` — commits land on an explicitly named branch.
  - `run()` returns a result with a `commits: { sha }[]` list — this is the **"pull commits back into your local workspace"** Matt describes.

## Two important reality-checks

1. **Security model — bind-mount is *de facto*, not a documented guarantee.** Matt warns a raw agent "might randomly delete your home directory or exfiltrate your env vars," positioning Sand Castle as the fix. **Verified nuance:** the bind-mount strategy mounts *only the repo worktree* by default (not `/home`), so home-dir deletion is prevented **as a side effect** of the mount design — but the README makes **no explicit security claims** about home-dir deletion or env-var exfiltration. Isolation relies on standard Docker/Podman container boundaries. Treat "agents can't escape" as *reasonable by construction*, not a certified guarantee — and don't use the `no-sandbox` provider for AFK.
2. **GitHub Actions — Matt's "agent-review action" is his repo's *internal CI*, not a published action.** In the podcast he opens the Actions tab of his Sand Castle repo and shows an "agent review" run on a PR ("just a prompt I have locally"). **Verified:** the repo *does* contain `.github/workflows/agent-review.yml` (plus `agent-explore`, `agent-implement`, `agent-implement-pr`, `agent-update-branch`, `ci`, `release`) — but these are **internal automation for Sand Castle's own development**, tightly coupled to its structure with hardcoded secrets. **There is no reusable `action.yml` you can `uses:` from another repo.** You'd replicate the *pattern* (Sand Castle + a review prompt wired into your own Actions), not install a turnkey action.

## How it fits Matt's workflow

Sand Castle is the substrate under "queues, not loops": issues are the queue; a label (`agent-implement`) fires a Sand Castle run inside GitHub Actions; the agent works **AFK** in a sandbox; commits come back as a PR; a review agent comments; you merge → the item leaves the queue. It can run **locally** (Docker/Podman) or **remotely** (Vercel sandboxes) so you're not constrained by your laptop. Sibling lineage: [[../autonomous-loops-human-in-the-loop/_index]], and the org-scale version in [[../harness-engineering/_index]].

## Key Takeaways

- **Sand Castle = `@ai-hero/sandcastle`** — a real, actively-maintained TS library (MIT, 6.5K★) for **running coding agents in sandboxes** and pulling their commits back.
- **5 sandbox providers** (Docker/Podman/Vercel/Daytona/no-sandbox) × **6 agent providers** — it's **not Claude-only**.
- **`run()` + `fork()` + 3 branch strategies** are the core API; `fork()` is what parallelizes agents.
- **Security is by-construction, not certified** — bind-mounts limit blast radius; the README claims no formal guarantees. Never AFK with `no-sandbox`.
- **The GitHub-Actions "agent-review" is internal CI**, not a turnkey published action — replicate the pattern, don't expect to install it.
