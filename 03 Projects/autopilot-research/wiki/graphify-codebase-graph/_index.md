# graphify-codebase-graph

> **Topic index.** **Graphify** — a tool that reads your project *once*, builds a **queryable knowledge graph** of how everything connects, and then your AI coding agent reads *that graph* at the start of every session instead of re-scanning files. The pitch: stop burning tokens re-deriving your codebase from scratch each session.
>
> **Origin:** AI Stack Engineer, **"OpenCode + Graphify: Stop Wasting Tokens in Opencode, Every Developer Use this"** ([-L_faOE-H5g](https://www.youtube.com/watch?v=-L_faOE-H5g), 2026-04-21, 10:11, ~47K views). Per the operator's "**double deep-dive into the original resource**" ask, this topic deep-dives the **originals the video is built on**: the [Graphify repo](https://github.com/safishamsi/graphify) (safishamsi, the tool itself), [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (the *intellectual* origin — and your whole vault's foundation), [OpenCode](https://github.com/sst/opencode) (the demo surface + its plugin system), and [lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) (Obsidian + Graphify as a memory system).
>
> **⚠️ Adversarially verified** (Workflow `wf_2f2a5052-7ac`, 11 agents). Verification produced four load-bearing corrections — the **71.5× number is real but cherry-picked** (independent tests show 7.3× / ~7-8%), the **Karpathy attribution is overstated** (inspired-by, not built-by/endorsed-by), the **cost model is accurate**, and **install safety differs sharply between your vault and hireui**. Full log: [[graphify-codebase-graph/source-provenance]].

---

## The headline for *you*

**Graphify is an automated, programmatic version of the exact pattern your entire vault runs on** — Karpathy's LLM Wiki. You hand-curate `raw/ → wiki/ → CLAUDE.md`; Graphify auto-extracts `code+docs → graph.json → GRAPH_REPORT.md`. So this isn't a foreign tool — it's a **machine that does, in minutes, a narrow slice of what your librarian does by hand**. The interesting question isn't "should I switch?" (you shouldn't — the graph is a *structural map*, not curated synthesis) but "**where can an auto-built graph augment my manual curation, and where can it cut Claude Code's token bill?**" See [[graphify-codebase-graph/karpathy-llm-wiki-lineage]] and the pilot menu.

It also slots cleanly onto the **memory taxonomy** you already mapped: Graphify is roughly an **automated L3/L5 hybrid** — a knowledge graph (not a vector DB, not a hand-written wiki) that loads at session start via a hook. See [[claude-code-memory-systems/_index]].

---

## Articles

- [[graphify-codebase-graph/overview]] — the problem (cold-start re-scan every session), the "contractor vs. internal wiki" mental model, what Graphify is, where it wins, where it's a waste of time.
- [[graphify-codebase-graph/three-pass-architecture]] — **the technical deep-dive**: Pass 1 tree-sitter (local/free) → Pass 2 Faster-Whisper (local/free) → Pass 3 LLM extraction (the *only* paid pass, cached, incremental); `graph.json`, god nodes, Leiden communities, SHA256 caching, `.graphifyignore`, all the outputs.
- [[graphify-codebase-graph/cli-and-commands]] — the full CLI surface (`graphify .`, `--update`, `--watch`, `query`/`path`/`explain`, `install`, `hook install`, exports) + the exact install ritual.
- [[graphify-codebase-graph/opencode-integration]] — **OpenCode** (SST's open-source agent), `AGENTS.md`, `opencode.json`, and the `tool.execute.before` plugin that makes Graphify "always on" by injecting "read the graph first" before every bash call.
- [[graphify-codebase-graph/token-savings-reality]] — **the 71.5× forensics**: what that number actually measures, the independent numbers (7.3× / ~7-8%), realistic expectations by corpus size, the amortization trap, and the benchmark you should run yourself.
- [[graphify-codebase-graph/karpathy-llm-wiki-lineage]] — **deep-dive into the original idea**: Karpathy's LLM Wiki pattern, the truth about the attribution, and a side-by-side of Graphify's auto-graph vs. your hand-maintained vault.
- [[graphify-codebase-graph/security-and-install-safety]] — supply-chain posture, the **typosquat risk (Issue #280)**, the Pass-3 data-flow privacy question, and a **go/no-go split: safe for the vault, risky for hireui**.
- [[graphify-codebase-graph/obsidian-graphify-memory-setup]] — the **lucasrosati** deep-dive: Obsidian + Graphify + automated chat-import as a 3-layer memory system, and exactly where it overlaps with (and differs from) your hand-curated vault.
- [[graphify-codebase-graph/source-provenance]] — verified-vs-flagged claim log + the workflow record.

## Pilot methods (how to apply this to your flow)

**16 ranked methods** across your flows live in `output/(C) 2026-06-20-graphify-opencode-pilot-methods.md` — six angles: **(A) the autopilot-research vault** (graph it; auto-extract relationships your librarian then curates), **(B) the Storm Bear curated vault**, **(C) hireui / Goal #2** (token-cut on a sandbox branch — with the security caveats), **(D) the Claude Code / OpenCode harness** (install + git-hook sync + `graphify query`), **(E) $0 pass-3 via local Ollama** (ties to [[cowork-third-party-inference/_index]]), **(F) Scrum/team** (the graph as an onboarding + architecture-comms artifact). Plus a skip-list and a critic reframe.

## Cross-topic links

- **Your vault's foundation:** [[graphify-codebase-graph/karpathy-llm-wiki-lineage]] — Graphify ≈ automated LLM Wiki (the pattern in the project `CLAUDE.md`).
- **Memory taxonomy:** [[claude-code-memory-systems/_index]] — Graphify is an automated L3/L5 (graph-as-memory, hook-injected). Sister tool to MemSearch/MemPalace.
- **Cost discipline:** [[claude-api-cost-optimization/_index]] — Graphify is a *context-engineering* token lever (load a compact graph, not raw files); compare to caching / programmatic tool calling / compaction.
- **The demo surface:** [[claude-code-clones/_index]] — OpenCode is one of the named Claude Code clones.
- **$0 inference:** [[cowork-third-party-inference/_index]] — point Pass 3 / queries at a local Ollama model and the only paid pass becomes free.
- **Graphify *is* a skill:** [[claude-skills/_index]] — it installs as a platform skill (`graphify install`) with progressive disclosure.
- **Parent discipline:** [[harness-engineering/_index]] — "load less, at the right time" is the same context-loading thesis.

## Key Takeaways

- **One sentence:** Graphify builds a knowledge graph of your project once, and your agent reads the graph instead of re-grepping files every session.
- **Three passes, one paid:** tree-sitter (code, free) + Faster-Whisper (audio/video, free) + LLM extraction (docs/PDF/images — the only token cost, cached + incremental). **Code-only repos pay $0.**
- **The 71.5× is real but cherry-picked.** Expect **2-8×** on a normal codebase; the headline is a 52-file mixed-media best case. Benchmark your own repo before believing it.
- **It's an automated LLM Wiki** — the same Karpathy pattern your vault runs on, minus the curation. Karpathy inspired it; he didn't build or endorse it.
- **Safe for your vault** (`uv tool install graphifyy`, skip hooks, no PII) — **risky for hireui** (typosquat → secrets, GDPR, I-8 governance, no LLM there yet).
