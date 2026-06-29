# Graphify — The Three-Pass Architecture (technical deep-dive)

> **Source:** [[graphify-codebase-graph/_index]]. Verified against the Graphify repo docs (`how-it-works.md`, README) via Workflow `wf_2f2a5052-7ac`. Cost-model claim **verified accurate** (see [[graphify-codebase-graph/source-provenance]]).

The video says it's "worth understanding the three passes because it tells you where your money actually goes." Here's the full mechanism.

## Pass 1 — Code (tree-sitter) · LOCAL · FREE

- Static parse via **tree-sitter** across **~25-36 languages** (Python, TS/JS, Go, Rust, Java, C/C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, Elixir, Bash, SQL, Vue/Svelte/Astro, etc. — plus specialized: Terraform/HCL, Salesforce Apex, package manifests like `pyproject.toml`/`go.mod`/`pom.xml`).
  - *(Sources disagree on the exact count — "20", "25", "36+ grammars" all appear. Treat it as "most mainstream languages.")*
- Extracts **every class, function, import, and call** → a deterministic code/call graph.
- **No model is called. Costs nothing in API tokens.** Pure static analysis, runs entirely on your machine.

## Pass 2 — Audio/Video (Faster-Whisper) · LOCAL · FREE

- If your corpus has meeting recordings, tutorial videos, MP3/WAV, or **YouTube links**, Graphify transcribes them **locally** with **Faster-Whisper**.
- Transcription is **seeded by the "god nodes"** from the Pass-1 code graph (the highest-connectivity concepts) so the transcript extraction focuses on domain-relevant content.
- **No API tokens, no network calls.** GPU (CUDA) is preferred; CPU fallback works but is slower. Transcripts are cached.

## Pass 3 — Docs / PDFs / images / transcripts (LLM) · PAID · ONCE

- For **markdown, PDFs, images, READMEs, docs, and the Pass-2 transcripts**, Graphify fires **parallel LLM sub-agents** through *your* configured model provider to pull out **concepts and relationships**.
- **This is the only pass that hits the API.** It outputs JSON fragments (nodes, edges, group relationships) that merge into the unified graph.
- It **runs once per corpus**, then the result is **cached**. **Skipped entirely if the corpus is code-only.**
- Office files (DOCX/XLSX) + Google Workspace require optional extras + auth.

> **Cost takeaway:** passes 1-2 are genuinely $0 (local compute is the only cost). Pass 3 is the wallet — and it's a *one-time* cost per corpus, linear in the number of **non-code** files. Point it at a local model (Ollama) and Pass 3 + queries become $0 too — see [[cowork-third-party-inference/_index]].

## The graph itself (`graph.json`)

- **NetworkX node-link format.** Nodes carry metadata (`id`, `label`, `file_type`, `source_file`).
- **Edges are confidence-tagged:**
  - `EXTRACTED` = 1.0 (from the deterministic AST — certain)
  - `INFERRED` = variable (from LLM inference)
  - `AMBIGUOUS` = uncertain (conflicting signals)
- **Persistent across sessions; never pasted into a prompt whole** — the agent *queries* it.
- **`graph.json` ships with a git merge driver** → parallel commits union-merge automatically, so two devs editing the graph never get conflict markers.

## "God nodes" and "communities"

- **God nodes** = the most heavily-connected concepts (highest-degree hubs). If 40 files touch one module, that module becomes a big node. Auto-detected; used to focus Pass-3 extraction and seed Pass-2 transcription.
- **Communities** = clusters detected with the **Leiden algorithm** on edge density. **No embeddings needed** — the semantic-similarity edges already exist. Auto-named (or `Community N` with `--no-label`). The report ranks *surprising cross-community connections*.

## Caching + incremental updates

- **SHA256 fingerprints** skip unchanged files entirely; cache lives in `graphify-out/cache/`.
- `--update` reprocesses **only changed files**. **Code-file changes trigger instant AST-only rebuilds — no LLM calls.** Doc/PDF/image changes re-trigger Pass 3 (token cost) for just those files.

## `.graphifyignore`

- Same syntax as `.gitignore` (including `!` negation). Drop `node_modules/`, `vendor/`, `dist/`, etc.
- Graphify **also respects `.gitignore` automatically**; if both exist, patterns merge and `.graphifyignore` wins on conflict.
- A single `.graphifyignore` at repo root works even when you run Graphify on a subfolder.

## Outputs (`graphify-out/`)

| Artifact | What it is |
|---|---|
| `graph.html` | Interactive **star-map** — colored dots (concepts/functions/classes/docs/images) + lines; click a node to see its files; filter by community; search. (>5000 nodes → use JSON instead.) |
| `GRAPH_REPORT.md` | The human-readable summary: high-connectivity (god) nodes, surprising connections, design rationale lifted from `# NOTE:` / `# WHY:` / `# HACK:` comments, + 4-5 suggested questions. **This is what the agent reads first.** |
| `graph.json` | The full machine-readable graph (queryable). |
| `cache/` | SHA256 cache for incremental updates. |
| *(optional)* | `obsidian/` vault, markdown `wiki/`, `graph.svg`, `graph.graphml` (Gephi/yEd), Neo4j/FalkorDB `cypher.txt`, Mermaid call-flow HTML, an MCP server. |

## Key Takeaways

- **Two free local passes + one paid LLM pass** — and the paid one is once-per-corpus, cached, incremental, and skipped for code-only repos.
- The graph is **NetworkX JSON with confidence-tagged edges** — not a vector DB, not embeddings (communities come from Leiden on the existing edges).
- **God nodes** = the hubs everything connects to; **communities** = topical clusters.
- The agent reads **`GRAPH_REPORT.md`** (and queries `graph.json`), never the whole graph — that's the token win.
- Keep it in sync with `--update` (cheap) or a git hook (see [[graphify-codebase-graph/cli-and-commands]]).
