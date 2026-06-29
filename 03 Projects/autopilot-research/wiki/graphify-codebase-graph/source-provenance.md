# Source provenance — what's verified vs flagged

> **Source:** [[graphify-codebase-graph/_index]]. Constitutional rule #4 (never fabricate) + Storm Bear prime directive. Built **primary-source-first**: the video gave the map; the originals (Graphify repo + docs, OpenCode docs, the Karpathy gist, the lucasrosati repo, PyPI) were fetched and the risky claims **adversarially verified** via Workflow `wf_2f2a5052-7ac` (11 agents: 7 deep-dive + 4 adversarial verify).

## Sources

| # | Source | URL | Used for |
|---|---|---|---|
| Video | AI Stack Engineer, "OpenCode + Graphify: Stop Wasting Tokens" | [-L_faOE-H5g](https://www.youtube.com/watch?v=-L_faOE-H5g) | The pitch, mental model, 3-pass framing, install + OpenCode walkthrough (yt-dlp full transcript, 1,753 words) |
| Orig | Graphify repo + docs | [github.com/safishamsi/graphify](https://github.com/safishamsi/graphify) | Architecture, CLI, outputs, claims, license, stars |
| Orig | Graphify on PyPI | [pypi.org/project/graphifyy](https://pypi.org/project/graphifyy/) | Package name, version, downloads, install |
| Orig | Karpathy LLM Wiki gist | [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | The original idea + attribution truth |
| Orig | OpenCode | [opencode.ai](https://opencode.ai) / [github.com/sst/opencode](https://github.com/sst/opencode) | AGENTS.md, opencode.json, plugin/hook system |
| Orig | lucasrosati/claude-code-memory-setup | [github](https://github.com/lucasrosati/claude-code-memory-setup) | Obsidian + Graphify + chat-import memory system |

## ✅ Verified against primary sources

- **3-pass architecture + cost model** (Pass 1 tree-sitter local/free; Pass 2 Faster-Whisper local/free; Pass 3 LLM extraction = only paid pass, cached, incremental, skipped for code-only) — **VERIFIED ACCURATE** against `how-it-works.md`.
- **`graph.json`** = NetworkX node-link; edges confidence-tagged (EXTRACTED=1.0 / INFERRED / AMBIGUOUS); **Leiden** community detection (no embeddings); **god nodes** = highest-degree hubs; SHA256 caching; git merge driver — **confirmed in docs.**
- **CLI surface** (`graphify .`, `--update`, `--mode deep`, `--watch`, `--wiki`, `--obsidian`, `--svg/--graphml/--neo4j`, `--mcp`, `query`/`path`/`explain`, `add`, `install [--platform]`, `hook install`) — **confirmed.**
- **OpenCode integration** (`graphify install --platform opencode` writes AGENTS.md + `.opencode/plugins/graphify.js` `tool.execute.before` hook + registers in opencode.json) — **confirmed** (with edge-case caveats below).
- **Security posture** (MIT, YC S26, ~69.6K stars, ~1.8M downloads, v0.8.44, no postinstall scripts, no telemetry, SECURITY.md, URL/prompt-injection/HTML/YAML defenses) — **confirmed via repo + PyPI.**
- **Karpathy LLM Wiki pattern** (raw/→wiki/→CLAUDE.md, humans-ask/LLM-maintains, no vector DB) — **confirmed in the gist** (the same gist your vault cites).

## ⚠️ Flagged — claim corrected or contextualized by verification

| Claim | Status |
|---|---|
| **"71.5× token reduction"** | **ACCURATE-BUT-MISLEADING.** Real for one 52-file mixed-media benchmark (Karpathy repos + 5 papers + 4 images). Independent tests: **7.3×** (Python codebase), **~7-8%** (browser-use). Scales with size (<100 files 1-3× / 100-500 5-15× / 500+ 20-40×). **No Anthropic validation.** Believe 2-8×. See [[graphify-codebase-graph/token-savings-reality]]. |
| **"Graphify came out of Karpathy"** | **OVERSTATED.** Karpathy *published the LLM Wiki pattern*; Shamsi built Graphify ~48h later as an **independent** implementation. Karpathy **did not create or endorse** it. See [[graphify-codebase-graph/karpathy-llm-wiki-lineage]]. |
| **"pile of mixed content you can never fully reconstruct"** | **GRAPHIFY MARKETING COPY, not a Karpathy quote.** The video attributes it to Karpathy; it's from Graphify's README. |
| **lucasrosati "499× per query" / "71.5× per session"** | **UNVERIFIED VENDOR CLAIMS** — no reproducible methodology in the repo. |
| **Language count "~23-36"** | Sources say 20 / 25 / 36+ grammars inconsistently. Treat as "most mainstream languages"; verify the exact list for your stack. |

## ⚠️ Mechanism / fetch caveats

- **OpenCode `tool.execute.before` reliability:** community issues report the hook **not firing** in edge cases (rtk-ai #1706) and Graphify plugins **not appearing** despite docs (#356, #755). **Verify the injected reminder actually shows** before trusting "always-on."
- **Typosquat (Issue #280):** official `graphifyy` (double-y); single-y `graphify` was **unclaimed on PyPI** — install via `uv`/`pipx` with the exact name. Maintainer's defensive registration **not confirmed done.**
- **Could not fetch:** aiopsschool.com blog (ECONNREFUSED), Karpathy's X post directly (HTTP 402 — reconstructed from the gist + secondary sources), some `levelup.gitconnected` content (paywall), OpenCode raw README (404 — used docs). None load-bearing; flagged for honesty.
- **71.5× absolute token counts** are **not published** by the repo (only the ratio).

## Key Takeaways

- **Architecture, CLI, cost model, security, and the OpenCode mechanism are verified solid.**
- **Two headline claims were corrected:** the **71.5×** (cherry-picked best case; expect 2-8×) and the **Karpathy attribution** (inspired-by, not built/endorsed-by; the "pile of mixed content" line is marketing).
- **One real risk surfaced:** the `graphifyy`/`graphify` typosquat.
- Built primary-source-first + adversarially verified; un-fetchable sources flagged rather than fabricated.
