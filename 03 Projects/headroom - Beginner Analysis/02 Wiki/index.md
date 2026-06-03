# headroom — Wiki (v144)

> **One line:** **"The context compression layer for AI agents"** — compresses tool outputs / logs / RAG / files / history before they reach the LLM ("same answers, fraction of the tokens"), across library / proxy / MCP / CLI surfaces, with reversible retrieval.
> **Tier:** T2 Service (agent context-compression layer). **Verdict:** GOAL-ALIGNED INCLUDE 3/4 (a FAIL · b/c/d STRONG).
> **Repo:** `chopratejas/headroom` · Apache-2.0 · Python 76.8% + Rust 18.4% + TS.
> **§37 provenance:** ≈7.0k★ / 479 forks (as of 2026-06, repo page — *stated, NOT API-verified; env mocks GitHub API*). Benchmarks below are repo-stated.

## What it is
README opener (verbatim):
> "Headroom compresses everything your AI agent reads — tool outputs, logs, RAG chunks, files, and conversation history — before it reaches the LLM. Same answers, fraction of the tokens."

A context layer that sits **between an AI coding agent and the LLM** and shrinks the agent's read-context. Directly relevant to this vault's own **context-rot** problem (the reason `CLAUDE.md` was refactored into `_state/` chapters).

## How compression works (content-aware, NOT LLM-summarization)
| Compressor | Handles |
|---|---|
| **SmartCrusher** | universal JSON (arrays of dicts, nested, mixed) |
| **CodeCompressor** | AST-aware: Python / JS / Go / Rust / Java / C++ |
| **Kompress-base** | own HuggingFace model trained on agentic traces (prose) |
| **CacheAligner** | stabilizes prefixes for provider **KV-cache** hits |
| **CCR (reversible)** | originals kept locally; LLM fetches via `headroom_retrieve` |

**Lossy + reversible hybrid** — "originals never deleted." Repo-stated benchmarks: code search 17,765→1,408 tokens (**92%**), SRE debugging 65,694→5,118 (**92%**), GitHub triage 54,174→14,761 (**73%**); accuracy preserved (GSM8K 0.870→0.870; TruthfulQA +0.030; SQuAD-v2 97% @ 19%).

## Five deployment surfaces
| Surface | Install | Use |
|---|---|---|
| Python lib | `pip install "headroom-ai[all]"` | `from headroom import compress` |
| TS lib | `npm install headroom-ai` | `await compress(messages, {model})` |
| HTTP proxy | (pip) | `headroom proxy --port 8787` (zero code change) |
| CLI wrapper | (pip) | `headroom wrap claude\|aider\|copilot` |
| MCP server | `pip install "headroom-ai[mcp]"` | `headroom mcp install` |

Docker `ghcr.io/chopratejas/headroom:latest`; Python 3.10+. **MCP tools:** `headroom_compress` / `headroom_retrieve` / `headroom_stats`.

## Two more agent features
- **`headroom learn`** — failure-mining: mines failed agent sessions and auto-writes corrections to `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` (plugin-based, for Claude/Codex/Gemini).
- **SharedContext** — compressed context passing across multi-agent workflows (shared store, agent provenance, auto-dedup).

## Corpus connectivity
- **v97 distill sibling / token-compression cluster** — and headroom's **Kompress-base** own-model echoes distill's own-trained `distill-1.7B` → re-registers the **"Own-Trained Bundled Expert Model"** Library-vocab at **N=2**.
- **Pattern #18 B1 MCP** (ships an MCP server) · **Library-vocab #20 Token-Economy-Quantification** (benchmarks).
- **Context-rot corpus-recursive** — productizes the vault's own discipline (the `_state/` refactor; v94; v137 RLM; hello-agents Ch 9).
- See `01 Analysis/` for the full verdict + Phase 4b (PRIMARY = NEW Library-vocab "Agent Context-Compression Layer" N=1 CORPUS-FIRST).

## Pilot note — Tier-1, genuinely
**The most directly-vault-applicable pilot in a long run.** It targets the vault's own context-rot pain. Lowest-friction: `pip install "headroom-ai[all]"` → `headroom mcp install` (MCP) or `headroom wrap claude` (CLI), reversible, BYO (`install-snapshot` recommended). Even reading its compressor design (AST-aware CodeCompressor, CacheAligner KV-prefix, CCR reversible store) is worth borrowing as ideas for the vault's surgical-extract discipline. This is the kind of subject worth *piloting*, not just cataloguing.
