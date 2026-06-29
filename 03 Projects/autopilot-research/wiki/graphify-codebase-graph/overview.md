# Graphify — Overview

> **Source:** [[graphify-codebase-graph/_index]]. Video: [-L_faOE-H5g](https://www.youtube.com/watch?v=-L_faOE-H5g) (AI Stack Engineer). Tool: [github.com/safishamsi/graphify](https://github.com/safishamsi/graphify).

## The problem it attacks

- You open a fresh agent session and ask *"what does this payment module do?"* Before answering, the agent opens the README, reads a config file, then walks your source files one by one — **building a mental picture from scratch, burning tokens on every read.**
- Worse, it has **no memory between sessions.** Close it, come back tomorrow → the agent starts from zero again. Same tokens burned, same files re-read, same "grepping around in the dark."
- The answer is only ever as good as whatever the agent happened to pick up along the way.

## The fix in one sentence

> Graphify reads your project **once**, builds a **knowledge graph** of how everything connects, and the agent reads **that graph** at session start instead of re-scanning your files.

## The mental model (from the video)

- A normal agent session = **a contractor who walks in on day one with no context.** They must skim everything before answering even a basic architecture question.
- Graphify = **handing that contractor the internal wiki before they start.** They already know which files are the core of the system, which modules talk to which, and where the important decisions live.
- You build that wiki **once**, and every future session gets it automatically.

> This is *exactly* the Karpathy LLM Wiki framing — the pattern your own vault runs on. Graphify is the **automated** version. See [[graphify-codebase-graph/karpathy-llm-wiki-lineage]].

## What it actually is

- A Python CLI + an **AI-assistant skill** (`pip install graphifyy`; CLI is `graphify`). Installs into 20+ agent platforms (Claude Code is the default; OpenCode, Codex, Cursor, Gemini CLI, Aider, etc.).
- **Multimodal, not just code:** point it at a folder of source code, SQL schemas, shell/R scripts, **markdown docs, PDFs, research papers, images/screenshots/diagrams, and audio/video** — it folds them all into one graph.
- Open-source (**MIT**), **YC S26-backed**, made by Safi Shamsi (London AI engineer). At the time of research: **~69.6K GitHub stars, ~1.8M PyPI downloads, v0.8.44** — very high adoption for a tool created 2026-04-03. See [[graphify-codebase-graph/security-and-install-safety]].

## How it pays for itself (the 3-pass cost model — verified accurate)

| Pass | Handles | Mechanism | Token cost |
|---|---|---|---|
| **1** | Code | tree-sitter static parse (classes/functions/imports/calls), ~25-36 languages | **$0 — fully local** |
| **2** | Audio/video | Faster-Whisper local transcription | **$0 — fully local** |
| **3** | Docs, PDFs, images, transcripts | parallel LLM sub-agents extract concepts + relationships | **Paid — but once per corpus, then cached + incremental** |

- **A code-only repo costs $0** (Pass 3 is skipped entirely).
- After the first build, the graph is cached. `graphify --update` re-processes **only changed files** (code changes = instant AST-only rebuild, no LLM). See [[graphify-codebase-graph/three-pass-architecture]].

## Where it earns its keep (and where it doesn't)

- ✅ **Worth it:** large, stable projects with **mixed content** — a codebase with a `docs/` folder full of markdown, a research vault, a folder of PDFs + meeting recordings. That's where the compounding shows.
- ❌ **Don't bother (video's own honesty):** projects **under ~10 files**. "The graph value is structural for small stuff, not token savings, and the agent can already handle that scale without help."
- ⚠️ **The headline caveat:** the famous **71.5× token reduction** is a single cherry-picked 52-file mixed-media benchmark. Independent real-world tests land at **7.3× (Python codebase)** and **~7-8% (browser-use)**. Expect **2-8×** on a normal repo. See [[graphify-codebase-graph/token-savings-reality]].

## ⚠️ Note on this video

- The transcript **never says "71.5×"** — that number comes from the repo + third-party blogs. The video sticks to the qualitative pitch + a setup walkthrough.
- The video contains a **sponsor read for "Code Sniff"** (a PR-review platform) — that's an ad, not part of Graphify, and is excluded from this wiki.

## Key Takeaways

- Graphify turns the per-session cold-start re-scan into a **one-time graph build + cheap reads thereafter.**
- The contractor-vs-internal-wiki framing **is** the LLM Wiki pattern — automated.
- Three passes; only the doc/PDF/image pass costs tokens, and only once per corpus.
- Best on **large + mixed-content** repos; pointless on tiny ones.
- Believe **2-8×**, not 71.5×, until you benchmark your own repo.
