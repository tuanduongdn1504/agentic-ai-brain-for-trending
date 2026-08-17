# (C) deepseek-harness — Deep Dive

**Subject:** `deepseek-ai/deepseek-harness` — *"DeepSeek Harness: Everything is a Plugin."*
**Wiki:** v235 · **Date:** 2026-08-17 · **Author of record:** DeepSeek AI (`deepseek-ai`), **NOT Anthropic**
**License:** MIT · **Version:** `0.1.0-rc.5` (developer preview) · **Released:** 2026-08-13
**Provenance:** ⚠️ **NOT source-cloned.** Hand-fetched: rendered repo page · raw `README.md` · raw `package.json` · `docs/` tree · `packages/` tree · `packages/llm` tree · `packages/subagent` tree · raw `packages/llm/llm-pi-ai/README.md` · deepseek.com/harness · landscape/press via WebSearch. All corpus claims hand-verified by grep.

---

## 1. What it actually is

A **plugin-composable agent runtime** — not a coding-agent product. DeepSeek open-sourced the *harness* rather than a finished CLI:

> "It uses an architecture where **everything is a plugin**, and is powered by Cordis"

Run it:

```sh
npx @deepseek-ai/dsh web        # → Web UI on http://127.0.0.1:3080
```

The swappable set (deepseek.com/harness, verbatim): **"models, tools, skills, sessions, sandboxes, storage, loops, scheduling, and the UI."** The *main agent loop itself* is a plugin — decomposed into interceptable Turn/Step stages rather than hardcoded control flow.

**Scale (press/code-read-stated):** ~453,000 lines of TypeScript across ~219 workspace packages, ~170,000 lines of documentation, **1,386 decision records**, 12,293 commits.

**The warning is in the README, in bold:**

> "DeepSeek Harness is currently in _developer preview_ and is iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.**"

---

## 2. Cordis — the kernel underneath

Cordis is **not DeepSeek's**. It is an independent **meta-framework** (a framework for building frameworks) by the developer **shigma**, and has been the plugin foundation of the **Koishi** chatbot framework for four years.

Its single defining capability is **disposability** — load, unload and reload plugins with *complete cleanup of side effects*. Three mechanisms:

- `ctx.effect` — reversible side effects
- lifecycle events — `ready` / `dispose` / `fork`
- a service system for dependency ordering

That is what makes "everything is a plugin" mean something operationally rather than decoratively: a plugin can be swapped at runtime without leaking state.

DeepSeek **vendors and rescopes** it — `@deepseek-ai/cordis` exists on npm (npm-listing-stated) — with CI attribution machinery around it: `verify-cordis-config`, `gen-cordis-catalog`, `gen-cordis-api`, `verify-vendored-links`, `gen-third-party-notices`, `verify-dsh-package-licenses`, `rescope-vendor`. Attributed vendoring, not silent bundling.

---

## 3. The three findings that matter to this vault

### ⭐ 3.1 The LLM seam runs on Pi — a corpus subject (#57)

`packages/llm/` contains only five directories: `llm` (core seam + streaming vocabulary), `token-meter`, `llm-retry`, `llm-deepseek`, **`llm-pi-ai`**.

`packages/llm/llm-pi-ai/README.md`, verbatim:

> "Generic multi-provider adapter for the harness LLM seam backed by [`@earendil-works/pi-ai`](https://www.npmjs.com/package/@earendil-works/pi-ai)."
>
> "pi-ai installs several provider SDKs and lazy-loads the one selected by the catalog model."

**`@earendil-works/pi-ai` is the npm package of `earendil-works/pi` = corpus subject v228** (itself the revisit of **v36 `badlogic/pi-mono`**, Mario Zechner → Earendil Inc.).

So a frontier lab's flagship agent runtime gets its **multi-provider model access from a corpus subject's SDK**. Providers named in that README: **OpenAI · Anthropic · DeepSeek · Azure · AWS Bedrock · Google Vertex** (+ Codex referenced).

⚠️ Two corrections this forces:

- The widely-repeated press line *"supports nearly 40 model providers … through plugin adapters"* is **not** a set of 40 first-party adapters. There is **no `llm-anthropic` package.** Breadth arrives through **one** package wrapping pi-ai. The "~40" figure is press-stated and unverified; the **six named providers are source-verified**.
- The code-level read *"ships exactly two models, `deepseek-v4-flash` and `deepseek-v4-pro`"* (1M context / 256K output cap) is also true — that is the **shipped default catalog**, not the provider ceiling. Both facts are correct and are reconciled by the two-adapter structure (`llm-deepseek` = defaults, `llm-pi-ai` = breadth).

**Claude is reachable in dsh, first-class, via the pi-ai seam.**

⭐ **The corpus-level observation:** Pi is now the corpus's most-depended-upon subject. **llm-space v221** (ByteDance's DeerFlow team) is built on Pi Agent Core; **deepseek-harness v235** backs its LLM seam with pi-ai. Two frontier-adjacent Chinese labs, independently, both build on one Austrian solo developer's runtime. And the sharpest critique of dsh — *"token usage runs roughly 10× versus Pi"* — measures it against the very project it depends on.

### ⭐ 3.2 It ships Claude Code as a delegatable subagent

`packages/subagent/` contains `subagent-acp`, **`subagent-claude-code`**, **`subagent-codex`**, `subagent-dsh-sdk`, `subagent-fork-in-process`, `subagent-in-process-driver`, `subagent-spawn-in-process`, `subagent`, `tool-subagent`, `tool-subagent-control`, `tool-subagent-report`.

Repo-stated:

> `subagent-claude-code/` — "Starts a real **Claude Code** child through the **official Claude Agent SDK**"
> `subagent-codex/` — "Starts a real Codex app-server child"

Plus `packages/hooks/` ships **hook bridges for Claude Code and Codex that run your existing `hooks.json`**. Both paths are off by default.

⚠️ A press summary described this as resolving "each product's binary from the host PATH." The repo's own wording is stronger and more specific: **the official Claude Agent SDK**. Reported as source-stated.

This is the inverse of harness *emulation*. **openinterpreter v223** minted "Harness-Emulation Coding Agent" — one binary that *reimplements* a target's native harness (`/harness claude-code`) to squeeze performance out of cheap models. DeepSeek does the opposite: it **delegates to the real thing** and bridges your real hooks. Emulate vs. delegate is a clean, load-bearing distinction.

### ⭐ 3.3 Traceability as an architectural guarantee

- **Append-only session logs** — anything visible to the model is permanently recorded.
- **Event-driven main loop** — Turn/Step stages are interceptable, so the loop is observable and replaceable.
- **Code Mode** — batches multiple tool calls into a single TypeScript execution block (`demo:code-mode` in `package.json`).
- **Self-modifying toolsets** — an agent can inspect and modify its own plugin tree (disabled by default).

The first of these is the one that matters for hireui: *"anything visible to the model is permanently recorded"* is, almost word for word, the audit requirement in the **RATIFIED candidate-LLM legibility ADR**.

---

## 4. Sandboxing (source/code-read-stated)

| Platform | Mechanism |
|---|---|
| Linux | probes **bubblewrap**, falls back to a native **Landlock** launcher (`native/landlock-run` is a workspace) |
| macOS | **seatbelt** |
| Windows | a **write-restricted token** — and the docs state plainly that **"reads, network, and process visibility stay unrestricted"** |

That Windows disclosure is a **#83 honest-disclosure POSITIVE**: the gap is documented rather than papered over.

---

## 5. Protocol + instruction-file surface

- **MCP: client-only.** *"dsh consumes MCP servers, it does not present itself as one."* → **NOT a #18 B1-MCP subject** (the pi v228 / lobehub v222 handling). `packages/mcp` exists on the consumer side.
- **ACP** — `packages/acp`, `subagent-acp`, `@agentclientprotocol/sdk 0.25.1`, a `demo:acp` script, `examples/acp-agent/cordis.yml`. Same posture as grok-build v215 (ACP-embeddable) and openinterpreter v223 (`interpreter acp`). **ACP ≠ MCP.**
- Reads **AGENTS.md and CLAUDE.md** → a **Pattern #12** LLM-routing-artifacts instance.
- `packages/skill` is first-class (+ a `verify-skill-invocation-metadata` CI gate).
- Other seams worth noting: `compaction` (→ headroom v144), `lsp` (→ the #23 code-graph family), `e2b` (→ the open-lovable v224 sandbox thread), `guard`, `credentials`, `identity`, `plan`, `goal`, `workflow`, `jobs`, `schedule`, `spill`, `typert`.

---

## 6. The honest weaknesses

Reported because they are load-bearing, not to be balanced away:

- **Developer preview**, `0.1.0-rc.5`, breaking changes promised in bold.
- **Ecosystem compatibility ~19%** — 41 of 219 integrations succeeding.
- **~10× token usage versus Pi** — from the critical review; unverified by me, but it is the single most important number for anyone considering running it.
- **A confirmed context-duplication bug.**
- **No evaluation story at all** — `BENCHMARK.md` is a 3-line stub; no eval harness anywhere in the tree; zero evaluation claims. For a runtime this large that is a striking gap.
- **Squashed-merge history** — the whole codebase "arrived as one squashed merge," described as *contributor-hostile*. Real provenance opacity.
- **`"postinstall": "node scripts/install-lefthook.mjs"`** — a postinstall script. ⚠️ Pointed, given that the project whose SDK it depends on (**pi v228**) is the corpus's strongest supply-chain *positive* exemplar precisely for `--ignore-scripts` + lifecycle allowlists + `min-release-age`.
- Nothing above the core loop: no artifacts surface, no session sharing, no metering.
- Critics' verdict: infrastructure research asking *"is an agent OS viable?"* — with a suggested **3–6 month wait** before production adoption.

**Star velocity:** ~92,700 stars in 28 hours (2026-08-13), ~138.5k by day four — page/press-stated only. Per **§37.4** the GitHub API is mocked in this environment, so velocity is unestablishable → **explicitly NOT a Pattern #52 claim**, extraordinary as the figure is.

---

## 7. Landscape

**NOT world-first.** Agent frameworks with plugin systems are a dense field — LangChain, LlamaIndex, Dify, AutoGen, Semantic Kernel, eliza — and Cordis itself has been powering Koishi for four years. dsh's distinctive is the *degree* (the loop, the UI, the scheduler and storage are all plugins on a disposability kernel) and the *provenance* (a frontier lab shipping the runtime rather than the product).

**Direct peer framing** — VentureBeat headlined it *"open source rival to Claude Code,"* launched alongside DeepSeek V4-Pro on the API at higher prices.

---

## 8. Corpus position

| Link | Relationship |
|---|---|
| **grok-build v215** §C | The natural home row — "Open-Sourced First-Party Frontier-Lab Agentic Coding CLI/TUI," **N=1, PROMOTION-ELIGIBLE at N=2.** See the Verdict: candidacy recorded, **not** self-executed. |
| **pi v228 / v36** | **Genuine #57** — declared, named, npm-linked dependency (`@earendil-works/pi-ai`) for the whole multi-provider seam; also the yardstick in the 10×-token critique. |
| **llm-space v221** | The *other* Pi-dependent subject → Pi is now a two-lab dependency. |
| **openinterpreter v223** §C | Sharp CONTRAST — emulate a harness vs **delegate to the real one**. |
| **DeepSpec v186** | Same org — the corpus's first first-party `deepseek-ai` subject. This is the **second**. |
| **DeepSeek-TUI v72** | A *third-party* TUI for DeepSeek models; dsh is first-party and a runtime, not a chat TUI. |
| **Kilo Code v177 · CodePilot v161 · larksuite v143** | The coding-agent-products meta-cluster the overdue audit must reconcile. |
| **PilotDeck v175 · cortex-hub v181 · lobehub v222** | Self-contained agent-platform family; v181/v222 were NO-MINT on packaging-not-capability grounds. |
| **headroom v144 · #23 family · open-lovable v224** | `compaction`, `lsp`, `e2b` seam cross-refs. |
| **Pattern #12** | Reads AGENTS.md + CLAUDE.md. |
| **Agent-primitive convergence** (grok-build v215 watch axis) | Reinforced hard — skills/subagents/hooks/plan/MCP/ACP is now cross-vendor vocabulary, and DeepSeek adopts Anthropic's `hooks.json` and Claude Agent SDK directly. |

---

*Built inline and fully hand-verified per `feedback_wiki_verify_independently_check_collisions` — no workflow, no subagent (the oversized shim overflows subagent context; the v200→v234 self-throttle). Collision by sanity-anchored hand-grep: `deepseek-harness` = 0 hits in `_state/` + `_patterns/`; anchors DeepSpec 56 / DeepSeek-TUI 115 / openinterpreter 50 all hit richly → the grep works, so the zero is trustworthy.*
