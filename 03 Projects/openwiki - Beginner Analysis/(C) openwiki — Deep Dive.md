# (C) openwiki — Deep Dive

> **Wiki v195** · subject `langchain-ai/openwiki` · MIT · TypeScript 54.6% / JavaScript 45.4% · v0.0.1 · **cloned + source-verified at commit `58b4bd3`** (release: 0.0.1, 2026-07-01) · ~1.8k★ / 146 forks / 0 GitHub releases (page-stated §37.4 — the env mocks the GitHub API, so treat all counts as page-stated, NOT velocity-verified) · **author = LangChain, Inc.** (the company behind the LangChain framework, LangGraph, Deep Agents, LangSmith) — **NOT Anthropic**.
>
> Deep-dive built from a full hand-read of the 30-file repo (README, `package.json`, `src/agent/{prompt,index,types,utils}.ts`, `src/{commands,constants,env,credentials,cli}.tsx`, the CI workflow, and its own dogfooded `openwiki/` docs) + a 6-agent read-only research workflow (LangChain identity / DeepAgents / doc-gen landscape / agents.md standard / supply-chain) that corroborated the source. Every corpus/collision claim was hand-verified separately (see the Verdict doc).

---

## 1. What it is, in one breath

**"OpenWiki is a CLI that writes and maintains documentation for your codebase, built specifically for agents."** (README, verbatim.)

Point it at a repository and it spins up an autonomous **documentation agent** that inspects the code + git history, writes a navigable Markdown wiki into an `openwiki/` directory, and — the load-bearing move — **appends a standardized "OpenWiki" reference section to your top-level `AGENTS.md` and/or `CLAUDE.md`** so your *other* coding agents (Claude Code, Codex, Cursor, …) discover and read those docs when they need repo context. Then a bundled GitHub Action re-runs it on a daily schedule, inspects the git diff since the last run, and opens a **human-review PR** with the doc updates.

The thesis, from LangChain's launch post: *agents write better code when they understand the repo they're working in* — but you don't want to stuff the whole repo into one giant instruction file. OpenWiki maintains a **separate, linkable, agent-consumable knowledge layer** that the instruction file merely points to.

**Why this vault should care:** OpenWiki is a productized, code-scoped version of *this vault's own founding pattern* — an LLM that incrementally writes and maintains a wiki so future queries don't re-derive knowledge from scratch (Karpathy's LLM-Wiki pattern). It is the closest commercial mirror of what Storm Bear does by hand, pointed at source code instead of a knowledge base.

---

## 2. Provenance & identity (hand-verified)

| Fact | Value |
|---|---|
| Repo | `github.com/langchain-ai/openwiki` (official LangChain org) |
| Author | **LangChain, Inc.** — US AI-infra company; **~$1.25B valuation** (Oct-2025 $125M Series B; ~$260M total funding; ~325 employees — press/page-stated) |
| Launch | **~2026-07-01/02** — [LangChain blog](https://www.langchain.com/blog/introducing-openwiki-an-open-source-agent-for-repo-documentation) + [official X post](https://x.com/LangChain/status/2072376975545798792) ("the easiest way to document your codebase, built specifically for agents to consume") |
| License | MIT |
| Languages | TypeScript 54.6% / JavaScript 45.4% (the JS is the compiled `dist/`) |
| Version | v0.0.1 (npm `openwiki`; release commit `58b4bd3`) |
| Scale | ~1.8k★ / 146 forks / 0 GitHub releases (page-stated §37.4; created-date not shown → **velocity unestablishable → NOT a Pattern #52 claim**) |
| Install | `npm install -g openwiki` |

LangChain's 2026 product stack, for context: **LangChain framework** (the batteries; Python/TS) → **LangGraph** (the production-grade orchestration runtime) → **Deep Agents / `deepagents`** (a "batteries-included agent harness" on top of LangGraph) → **LangSmith** (commercial observability/tracing) → **OpenWiki** (this — the newest, an applied doc agent). OpenWiki is the thin applied tip of a deep stack.

---

## 3. Architecture — the engine is DeepAgents + LangGraph

`package.json` describes it precisely: *"A CLI that uses a **DeepAgents** documentation agent to generate and maintain an OpenWiki for a codebase."* The whole tool is ~30 tracked files; the intelligence lives in a **system prompt** and a **dependency**, not in a large codebase.

**Dependencies (all first-party LangChain + mainstream):**
`@langchain/anthropic`, `@langchain/core`, `@langchain/langgraph-checkpoint-sqlite`, `@langchain/openai`, `@langchain/openrouter`, **`deepagents`** (v1.10.5), `ink` (React-in-the-terminal TUI), `marked`, `react`.

### 3.1 What DeepAgents provides (the upstream harness)

`deepagents` is LangChain's open-source **"agent harness,"** explicitly framed as an *"open-source Claude Code alternative that works with any model."* A "deep agent" bundles four things over the LangGraph runtime:

1. **A detailed system prompt** (OpenWiki supplies its own — see §4).
2. **A planning tool** (`write_todos` — a structured, status-tracked todo list held in agent state).
3. **A virtual filesystem** via pluggable backends (`ls`/`glob`/`grep`/`read_file`/`write_file`/`edit_file`) — OpenWiki uses **`LocalShellBackend`** (`virtualMode: true`, `rootDir: cwd`, 120s timeout, 100 KB output cap), which extends the filesystem backend with a shell **`execute`** tool.
4. **Subagent spawning** (a `task` tool that launches ephemeral, fresh-context, single-handoff subagents for parallel read-only research).

OpenWiki calls `createDeepAgent({ model, tools: [], checkpointer, backend, systemPrompt })` — it passes **no custom tools**; every capability (filesystem, shell, subagents, planning) comes from the harness. This is the corpus's **first subject built on DeepAgents**.

### 3.2 The rest of OpenWiki (the ~500 lines that are actually OpenWiki)

- **`src/agent/index.ts`** — the runtime: loads `~/.openwiki/.env`, resolves the provider + model, collects git context, creates the model client, builds the DeepAgents session, streams messages/tool-events to the UI, and writes update metadata. Also a **model-fallback loop** (OpenRouter 5xx → retry through a fallback model list) and an OpenRouter **debug-fetch wrapper that redacts secrets** from captured response bodies + URLs.
- **`src/agent/prompt.ts`** — the ~130-line system prompt + mode-specific instructions + user-prompt assembly (see §4).
- **`src/agent/utils.ts`** — git-evidence collection + the content-snapshot + `.last-update.json` handling.
- **`src/constants.ts`** — the 5 providers, model options, env keys, validation.
- **`src/commands.ts`** — argv parsing + help text (`--init`, `--update`, `-p/--print`, `--modelId`, `--dry-run` [dev]).
- **`src/cli.tsx`** — the Ink terminal UI + auto-exit on successful `--init`/`--update`.
- **`src/credentials.tsx` + `src/env.ts`** — interactive onboarding + `~/.openwiki/.env` persistence.

### 3.3 State & persistence

- **LangGraph `SqliteSaver` checkpointer** at `~/.openwiki/openwiki.sqlite` — persists conversation threads keyed by a SHA-256 hash of the repo path, so runs are **resumable** and chat is multi-turn. (Env dir `chmod 0700`; the checkpoint file `chmod 0600` — it contains conversation history.)
- **`openwiki/.last-update.json`** in the target repo — records `{ updatedAt, command, gitHead, model }` after a successful run, used to scope the *next* update run to commits since `gitHead`.

---

## 4. The system prompt IS the product (the "double deep dive" gold)

The single most valuable, most *borrowable* artifact in the repo is `createSystemPrompt()` in `src/agent/prompt.ts` — a ~130-line encoding of *how to write agent-first codebase documentation*. It reads like a senior tech-writer's operating manual. The disciplines, distilled:

- **Grounding.** *"Do not invent files, modules, APIs, business rules, or behavior. Ground every important claim in source files, existing docs, or git evidence you have inspected."* (The vault's own anti-fabrication rule, in a doc-agent.)
- **Discovery discipline.** Prefer targeted `grep`/`glob`/short reads over full-file reads; **never `glob **/*` from root**; inspect the tree + config + entrypoints + representative files per domain, don't read everything.
- **Subagent discipline.** May use `task` to parallelize **read-only** research; **default 1–2 subagents**, 3–4 only for small/independent domains; subagents *inspect and summarize only* — they never write; the main agent synthesizes and owns all writes; subagent reports are internal notes, never pasted into the final output.
- **Planning discipline.** Before writing final docs, create a temporary `openwiki/_plan.md` (intended pages + source evidence + open questions), then **delete it before finishing**.
- **Git discipline.** Use `git log`/`show`/`blame` to explain **why** code exists, not just what; during `--update`, inspect commits since the recorded `gitHead`; account for uncommitted changes; don't over-index on ancient history.
- **Existing-docs discipline.** Treat README/`docs/`/`SKILL.md` as *primary source material*; summarize + link rather than duplicate; if docs conflict with code, flag the likely-stale doc and prefer current source.
- **Root instruction files.** Always ensure top-level `/AGENTS.md` and/or `/CLAUDE.md` reference the OpenWiki quickstart; if both exist, duplicate the section into both; if neither, create `/AGENTS.md`; on updates, refresh the section only if missing/stale; **preserve surrounding hand-written content**; a fixed section template is used every time.
- **Security & privacy.** *"Do not read or document secret values… Do not read `.env` files."* `.env.example` OK only if placeholder-only. Keep all docs under `openwiki/`; the only files it may touch outside are `/AGENTS.md` + `/CLAUDE.md` (only the OpenWiki section).
- **Documentation goals.** Someone with zero knowledge starts at `quickstart.md` and understands the project; a future agent can make high-quality changes with less exploration; capture **business/product logic**, not just technical detail; explain **why**; include change-oriented guidance ("where to start, what to watch out for, which tests matter").
- **Section-quality rules.** No thin pages; a section dir should hold multiple substantive pages; merge stubs into `quickstart.md` or a broader page; for ≤10-file repos prefer `quickstart.md` + at most 1–2 pages; **at most 8 pages on the initial run** unless the repo is large.
- **Mode-specific behavior:**
  - **`init`** — build from scratch; inventory first (docs, entrypoints, config, domains, tests, schema, scripts); use git to understand how things came to be; `quickstart.md` first, then linked sections.
  - **`update`** — **surgical**: build a "source change → docs affected → edit needed → why" impact plan; only edit pages made inaccurate by recent changes; a **soft diff budget** (fewer than ~5 files changed → update at most 1–2 pages); **no formatting-only edits**; **may be a no-op** ("the wiki is already current").
  - **`chat`** — answer directly; don't modify docs unless explicitly asked. (This is the "Q&A over your docs and codebase" mode from the launch post.)

**This prompt is directly liftable** into the vault's own `05 Skills/` (a doc-authoring skill) and into hireui's `CLAUDE.md` — see the Pilot Methods Menu.

---

## 5. Provider model & the cost story

OpenWiki is deliberately **model-agnostic**. 5 providers, each with pre-defined models + a custom-model-ID escape hatch (`src/constants.ts`):

| Provider | Pre-defined models | Notes |
|---|---|---|
| **OpenRouter** (default) | GLM 5.2, OpenRouter Fusion, Kimi K2.7 Code, Claude Opus/Sonnet, GPT 5.4-mini/5.5 | `route: "fallback"` — auto-routes around 5xx |
| Anthropic | Claude Haiku 4.5 / Sonnet 5 / Opus 4.8 | native `ChatAnthropic` |
| OpenAI | GPT 5.4-mini / 5.5 | native `ChatOpenAI` |
| Fireworks | GLM 5.2, Kimi K2.7 Code | OpenAI-compatible baseURL |
| Baseten | GLM 5.2, Kimi K2.7 Code | OpenAI-compatible baseURL |

**The default is GLM 5.2 via OpenRouter** — *not* Claude. The OpenRouter fallback route is `[selected → gpt-5.4-mini → claude-sonnet-5]`. This is a deliberate cost decision: documentation-writing is a high-volume, low-stakes-per-token task (you re-run it daily over a whole repo), so OpenWiki defaults to a cheap, capable open model and lets you upgrade to Claude if you want. **Cross-ref: the default model `z-ai/glm-5.2` is the corpus's own v176 GLM-5 subject.** This is a concrete data point for the vault's `claude-api-cost-optimization` thread: *use a cheap model for the bulk repo-doc pass, reserve Claude for the code it then writes.*

---

## 6. The update loop & the anti-churn guard (the loop-engineering angle)

`examples/openwiki-update.yml` is a GitHub Action that turns OpenWiki into a **scheduled, unattended, human-gated maintenance loop** — the exact shape of the `loop-engineering` v189 discipline:

```yaml
on:
  schedule: [ cron: "0 8 * * *" ]   # daily, 08:00 UTC
permissions: { contents: write }
# → npm install --global openwiki
# → openwiki --update --print   (env: OPENROUTER_API_KEY, OPENWIKI_MODEL_ID=z-ai/glm-5.2, LANGSMITH_API_KEY, LANGCHAIN_TRACING_V2)
# → peter-evans/create-pull-request  (branch openwiki/update, "docs: update OpenWiki")
```

It **opens a PR, never auto-commits to your default branch** — the human reviews the doc diff. That is exactly the L1/L2 "report-only / propose-don't-act" discipline the vault's loop-verifier enforces.

**The clever engineering detail — the content-snapshot no-op guard** (`src/agent/utils.ts`): the runtime takes a **SHA-256 hash of the entire `openwiki/` tree** (excluding `.last-update.json`) *before and after* the run. `.last-update.json` is written **only if the hash changed.** So a no-op update (nothing changed since the last run → the model correctly edits nothing) doesn't bump metadata, doesn't create a PR, and doesn't churn. This is the concrete answer to "how do you run an agent on a daily cron without it generating noise every day" — a reusable pattern for *any* scheduled agent loop.

---

## 7. Its own dogfooded output (what it actually produces)

The repo commits its own `openwiki/` docs — the best available evidence of output quality. The generated `openwiki/quickstart.md` has: a one-paragraph "what this repository does," a "Start here" link list, "Key source files" (annotated), a "Documentation map," "Notes for future agents," and a "Source map" **with git-evidence commit hashes**. The generated `openwiki/architecture/overview.md` explains runtime shape, provider/model resolution, the DeepAgents backend, the content-snapshot logic, **"Why the architecture is shaped this way,"** "Major extension points," and **"Things to watch when editing"** — i.e. it genuinely explains the *why* and gives change-oriented guidance, not a file inventory. And `AGENTS.md` contains exactly the injected OpenWiki reference section (dogfooding the append feature).

Verdict on output: **high quality for a v0.0.1** — navigable, grounded, agent-oriented. The caveat is that this is the tool documenting *its own small, clean, TypeScript repo*; quality on a large, messy, multi-language monorepo is unproven (no published benchmarks).

---

## 8. Landscape — is it new? (blunt)

**No, OpenWiki is not world-first at "AI-generated codebase documentation."** It is a **well-built entrant** in a populated category, differentiated on a *conjunction*:

| Tool | What it is | How OpenWiki differs |
|---|---|---|
| **DeepWiki** (Cognition/Devin) | Hosted SaaS that auto-generates a wiki for any GitHub repo | OpenWiki is **self-hosted + writes into YOUR repo** as git commits, not an external site |
| **Context7** (Upstash) | MCP server serving up-to-date docs for **public libraries** to LLMs | OpenWiki documents **your private repo**, self-hosted |
| **Mintlify** | Managed docs platform + AI agent | Mintlify updates are **platform-hosted**; OpenWiki updates land **in-repo** as reviewable PRs |
| **Swimm** | IDE-native docs w/ deterministic **static analysis** primary | OpenWiki is **agent-first** (LLM primary), CLI + CI, not IDE-bound |
| **Komment** | Delta-triggered SaaS, 90+ languages | Komment is platform-hosted + code-delta-triggered; OpenWiki is in-repo + schedule-driven |
| **GitBook AI** | Reactive query-answering (beta) | OpenWiki is **proactive** (auto-detects code changes) + AGENTS.md-aware |

**What is genuinely differentiated** (the 4-pillar conjunction no competitor in the analyzed set combines): **agent-native** (docs *for agents to consume*) × **self-hosted CLI that writes into your repo** × **CI-maintained via a daily human-review PR** × **AGENTS.md/CLAUDE.md-aware** (it wires the docs into your agent instruction files) × **multi-provider** (BYO model). That conjunction — plus the LangChain/DeepAgents pedigree — is the story.

**The AGENTS.md context:** `AGENTS.md` is an open standard stewarded by the Agentic AI Foundation under the Linux Foundation (`github.com/agentsmd/agents.md`, ~22.7k★ — page-stated) — a cross-harness "README for agents." **Claude Code reads `CLAUDE.md` natively, NOT `AGENTS.md`** (no automatic fallback; teams sync via a `@AGENTS.md` import in `CLAUDE.md` or a symlink). OpenWiki correctly handles this by writing **both** (duplicating its section into each if both exist). A tool that *auto-generates and safely maintains* these instruction files is the notable part.

---

## 9. Security & supply-chain (honest)

- **Install: BENIGN.** `npm install -g openwiki` — no `curl|bash`, no postinstall scripts; runtime deps are all first-party LangChain packages + mainstream (`ink`/`marked`/`react`). (Treat npm/GitHub stats as page-stated — the env mocks the API.)
- **Runtime: MODERATE.** The agent runs on a DeepAgents **`LocalShellBackend`** that can **`execute` arbitrary shell** in the target repo. Critically: **`virtualMode: true` sandboxes the *filesystem tools'* paths (blocks `..`, `~`, absolute paths outside root) but does NOT restrict the shell `execute` tool** (per LangChain's own backends docs) — the agent can run shell commands with full user permissions. It also **writes to your repo** (`openwiki/` + appends to `AGENTS.md`/`CLAUDE.md`). The example CI grants `permissions: contents: write` and uses `OPENROUTER_API_KEY` + `LANGSMITH_API_KEY` secrets.
- **Mitigations (real):** the system prompt forbids reading `.env`/secrets; the OpenRouter debug wrapper redacts secrets from captured bodies; env dir `0700` / checkpoint `0600`; **all output is a reviewable git diff / PR** (human-gated); it defaults to writing only under `openwiki/` + the two instruction files.
- **Net:** benign to install, moderate to run unattended. Fence: run on a **scratch clone** first, review the PR, keep it repo-scoped, don't hand it secrets, pin the model. (No head-to-head security/quality benchmarks are published.)

---

## 10. Honest limitations

- **v0.0.1, ~3 days old** at ship; 0 GitHub releases; API surface may churn.
- **Thin layer.** The hard agent-harness engineering (filesystem/shell/subagents/planning/checkpointing/streaming) is **upstream in `deepagents` + LangGraph**. OpenWiki's own contribution is ~500 lines of glue + the (excellent) system prompt + the AGENTS.md-append feature + the content-snapshot guard. That's the right size for the job — but it means OpenWiki's ceiling is DeepAgents' ceiling.
- **No test suite** in the tracked repo (30 files; no `test/`, no `*.test.ts`).
- **Output quality unproven at scale** — dogfooded only on its own small clean repo; no benchmarks vs. Swimm/Komment/DeepWiki; multi-language coverage undocumented.
- **Cost is on you** (you pay the inference; default GLM 5.2 keeps it cheap, but a daily whole-repo pass on a large codebase is non-trivial spend if you upgrade to a frontier model).

---

## 11. Sources

- Repo (source-verified at `58b4bd3`): `github.com/langchain-ai/openwiki`
- [LangChain — Introducing OpenWiki](https://www.langchain.com/blog/introducing-openwiki-an-open-source-agent-for-repo-documentation) · [LangChain X post](https://x.com/LangChain/status/2072376975545798792)
- [DeepAgents overview (LangChain docs)](https://docs.langchain.com/oss/javascript/deepagents/overview) · [DeepAgents backends](https://docs.langchain.com/oss/javascript/deepagents/backends) · `github.com/langchain-ai/deepagentsjs`
- [agents.md standard](https://agents.md/) · `github.com/agentsmd/agents.md`
- Landscape: DeepWiki (Cognition/Devin), `github.com/upstash/context7`, mintlify.com, swimm.io, komment.ai
- LangChain funding: TechCrunch (Oct 2025, $1.25B valuation)
