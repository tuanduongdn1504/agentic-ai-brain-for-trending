---
title: "(C) openinterpreter — Deep Dive"
subject: "openinterpreter/openinterpreter"
wiki: v223
date: 2026-07-22
author_note: "Claude-generated (C). Source hand-fetched (rendered repo + raw README) + WebSearch identity/landscape; NOT source-cloned (the v200→v222 self-throttle — the ~205K shim overflows every subagent >200K → deep-dive workflows fail prompt-too-long)."
---

# Open Interpreter (the new Rust one) — Deep Dive

> ⚠️ **READ THIS FIRST — this is NOT the famous 2023 Python "Open Interpreter."**
> The URL the operator gave is `github.com/openinterpreter/openinterpreter` (**no hyphen** — the org name repeated as the repo name). That is a **different, newer repository** from the world-famous `openinterpreter/open-interpreter` (**with a hyphen**), Killian Lucas's 2023 Python "natural language interface for computers" (runs code locally, ~59k★, one of the first "ChatGPT-that-runs-code-on-your-machine" projects).
>
> `openinterpreter/openinterpreter` is **the company's official 2026 Rust rewrite** — *"the new Rust version of Open Interpreter, based on [OpenAI] Codex"* — a **coding agent optimized for low-cost / open models** whose headline capability is **harness emulation**. The classic Python project "continues as a community-maintained fork at `endolith/open-interpreter`." **Same org (Open Interpreter Inc. / Killian Lucas), completely different codebase, language, and thesis.** Conflating the two would be a serious identity error (the v192 palmier-pro "it's-not-a-coding-tool" / v205 system_prompts_leaks "not-a-revisit" near-miss discipline).

## One-sentence summary

`openinterpreter/openinterpreter` is Open Interpreter Inc.'s **open-source (Apache-2.0), Rust, terminal coding agent — a fork of OpenAI's Codex CLI — rebuilt to squeeze maximum agentic performance out of cheap / open-weight models (Kimi K3, DeepSeek, Qwen, Z.AI/GLM) by *emulating each model's native agent harness*** (a swappable `/harness` that becomes `claude-code`, `kimi-code`, `qwen-code`, `deepseek-tui`, `zcode`, `swe-agent`, `native`, `minimal`, …), with native OS sandboxing and Agent-Client-Protocol (ACP) editor embedding.

## Provenance & identity (hand-verified)

| Field | Value | Source / caveat |
|---|---|---|
| Repo | `openinterpreter/openinterpreter` | rendered page + raw README |
| **Distinct from** | `openinterpreter/open-interpreter` (Python, "natural language interface for computers", 2023) | the famous one; **now community-forked to `endolith/open-interpreter`** |
| Author / org | **Open Interpreter Inc.** — the `openinterpreter` GitHub org, **Killian Lucas's** company (the same org that hosts the classic `open-interpreter`) | WebSearch; **NOT Anthropic** |
| Tagline | *"A coding agent for open models like Kimi K3"* (repo desc) / *"A coding agent optimized for low-cost models"* (README) | verbatim |
| Language | **Rust 96.6%** / Python 2.6% / (Starlark/TS/Shell/PS trace) | page-stated |
| License | **Apache-2.0** | page-stated |
| Base | **A fork of OpenAI's Codex CLI**; *"Codex SDK compatible with one-line binary override"* | README |
| Latest release | **0.0.34** (2026-07-18) | page-stated |
| Releases | **62** | page-stated |
| Stars / forks | **~67.1k★ / ~5.8k forks** | ⚠️ **page-stated §37.4 (GitHub API mocked) → NOT a #52 velocity claim.** The high count for a v0.0.x repo likely reflects the **Open-Interpreter brand / org**, not organic velocity — flag, don't infer. |
| Install | `curl -fsSL https://www.openinterpreter.com/install \| sh` (mac/Linux) · `irm https://www.openinterpreter.com/install.ps1 \| iex` (Windows) · invoke `i` or `interpreter` | README |
| Local state | `~/.openinterpreter` | README |

**The pivot story (the load-bearing fact):** Open Interpreter Inc. **abandoned/community-handed-off its famous Python flagship and rebuilt the whole thing in Rust as a Codex fork**, re-scoping the product from *"a natural-language interface for computers"* (2023: run ANY task via code) to *"a coding agent optimized for low-cost models"* (2026: run agentic **coding** well on **cheap** models). The Python `open-interpreter` lives on only as a community fork (`endolith/open-interpreter`). This is the **same company reinventing its own flagship inside the 2026 Codex-CLI-fork wave** — directly parallel to grok-build v215 (SpaceXAI's Rust Codex-adjacent harness) and the broader coding-agent-products cluster.

## What it IS (and is not)

- **IS:** an interactive **terminal coding agent (TUI)** — you type `i`, chat, it reads your codebase / edits files / runs shell commands, agentically, inside an OS sandbox. A Claude-Code / Codex-CLI **peer**, open-source, model-agnostic, tuned for cheap models.
- **IS NOT:** the 2023 Python "run any computer task via natural language" tool; a hosted service; a library; a Claude-first product (Claude is *one harness among many*, and the product is explicitly optimized for **non-Claude** open models).

## The distinctive capability — HARNESS EMULATION

This is the wiki-worthy idea, and it is genuinely distinct from anything in the corpus.

**The insight:** a model's *agentic* performance is not just a function of the model — it depends heavily on the **harness** it runs in (the exact system prompt + tool schemas + turn loop + formatting the model was RL-tuned against). Kimi K3 was optimized against Moonshot's "Kimi Code" harness; Qwen against "qwen-code"; DeepSeek against its TUI harness; Claude against Claude Code. Run a model under a *foreign* harness and you leave capability on the table.

**The move:** Open Interpreter ships **one binary that can *become* any of those harnesses on demand.** A `/harness` command swaps the active harness among (README-stated):

`native` · `claude-code` · `claude-code-bare` · `zcode` (Z.AI/GLM) · `kimi-code` · `kimi-cli` · `qwen-code` · `deepseek-tui` · `swe-agent` · `minimal`

So you point OI at a cheap/open model **and** select that model's *native* harness → you get "maximum K3 performance with a Codex-like interface." The **Kimi Code harness was reimplemented Rust-native** specifically to extract max Kimi K3 performance. The pitch: *a fork of Codex focused on emulating the agent harness that gets the best out of low-cost models.*

**Why this matters for the vault (Goal #1):** it is a productized statement of the exact thesis the vault's `harness-engineering` thread studies (TNT-Cursor-CLI-factory / Archon / Adaptive-engineering / loop-engineering v189 / grok-build v215): **the harness is the lever, not just the model.** Reading OI's harness definitions is a concrete, side-by-side "what does the claude-code harness actually contain vs the kimi-code harness" study — a rare artifact for understanding *what makes Claude Code effective* by contrast.

## Architecture & features (README-stated; NOT source-cloned)

- **Rust, a Codex fork.** Inherits Codex's agent loop, tool set, and CLI shape; "Codex SDK compatible with one-line binary override" (drop-in for Codex-SDK consumers).
- **Native sandboxing** on macOS / Linux / Windows — commands run in an OS-level sandbox (the classic OI "an agent running code on your machine" risk, mitigated at the OS layer rather than a Docker requirement).
- **Provider / model switching** from the terminal; harness switching via `/harness`.
- **Agent Client Protocol (ACP):** `interpreter acp` runs OI as an ACP agent, so it embeds in ACP-compatible editors (Zed etc.). ⚠️ ACP is a **consumed external standard** (Zed-ecosystem), **NOT corpus-first** — it recurs at free-claude-code v60, agent-of-empires v162, grok-build v215.
- **Model focus:** Kimi K3 (Rust-native harness) · DeepSeek · Z.AI/GLM (`zcode`) · Qwen (`qwen-code`). Claude via `claude-code` / `claude-code-bare` harnesses (one option among many).
- **Local state** under `~/.openinterpreter`.
- README references **OpenAI's Codex** (the base) and **Vercel Labs' agent-browser** (a browser sub-capability).

## Corpus-recursive links (hand-noted, one flagged-unverified)

- **`deepseek-tui` is a named emulated harness → DeepSeek-TUI = corpus subject v72** (`Hmbown`, a Rust TUI for DeepSeek-V4). OI's `/harness deepseek-tui` emulates that harness class. This is **stronger than a landscape mention** (it reimplements the harness's behavior) → a genuine corpus-recursive cross-reference, **leaning #57** — but ⚠️ **NOT source-verified** that OI's `deepseek-tui` harness is specifically Hmbown's v72 codebase vs the generic "DeepSeek TUI" harness concept. Recorded as a notable corpus-recursive cross-ref, hand-caveated (the `feedback_wiki_verify_independently_check_collisions` discipline — don't assert a #57 lineage I haven't source-confirmed).
- **`zcode` = Z.AI/GLM harness → GLM-5 = corpus subject v176** (Zhipu's open-weights frontier model). A target-model cross-ref.
- **Based on OpenAI Codex CLI** — Codex is a landscape peer, **not a corpus subject** (also grok-build v215's base). NOT #57.
- **Kimi K3** = Moonshot's model (vault topic #65 "Kimi K3"). Target-model cross-ref.
- **Vercel Labs agent-browser** — a vercel-labs cross-ref (vercel-labs = agent-skills-of-vercel v51 in the corpus, a *different* repo). Light note.

## Honest caveats (foregrounded)

1. **NOT source-cloned** — everything here is from the rendered repo page + raw README + WebSearch (the v200→v222 self-throttle: the ~205K shim overflows every subagent >200K, so the deep-dive workflows fail prompt-too-long and were not run). The harness internals, the Rust architecture, and the exact Codex-fork delta are page/README-stated, not code-verified.
2. **A Codex fork** — the hard base (agent loop, sandboxing, tool set) is upstream OpenAI Codex; OI's original contribution is the **harness-emulation layer + open-model tuning + the Kimi-Code Rust reimplementation**, not a from-scratch agent.
3. **Star count is page-stated + likely brand/org-carried** — ~67.1k★ on a v0.0.x repo is not organic velocity; treat as a data-point, NOT #52.
4. **"Maximum K3 performance" / harness-emulation performance claims are the project's own** — unbenchmarked here.
5. **Young despite 62 releases** — v0.0.34; a fast-iterating 2026 project, not a stable 1.0.
6. **Claude is deliberately secondary** — the product exists to run *non-Claude* cheap/open models well. On-goal as *agent infrastructure + a cost lever*, not as a Claude-first tool.

## Landscape (WebSearch)

The 2026 open-source CLI-coding-agent field is crowded and Codex-fork-heavy: **OpenAI Codex CLI** (Rust, the base) · **OpenCode** · **Aider** · **Goose** · **Pi** · **Claude Code** / **Gemini CLI** (platform agents) · and the vault's own coding-agent subjects **grok-build v215** (SpaceXAI's Rust harness), **Kilo Code v177** (IDE-embedded), **DeepSeek-TUI v72**. "Harness engineering" is a recognized 2026 concept (a `harness-engineering` GitHub topic; `awesome-cli-coding-agents` catalogs harnesses). Open Interpreter's distinctive contribution within this field = **productized, swappable, multi-harness *emulation* matched to the model** — corpus-first for that surface, and plausibly novel in the field, though scoped conservatively as **corpus-first NOT asserted-world-first** (harness-engineering is an active field; credit it).

## Sources

- Rendered repo page + raw `README.md` (hand-fetched 2026-07-22)
- WebSearch: Open Interpreter identity / Killian Lucas / the Python→Rust pivot / `endolith/open-interpreter` community fork / the Codex-fork + harness-emulation thesis / the 2026 CLI-coding-agent landscape
- Corpus collision hand-grep over `_state/` + `_patterns/` + `03 Projects/` (open-interpreter appears only as an ollama landscape mention → collision-clean)
