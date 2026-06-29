# Original Deep-Dive: Obsidian skill (kepano/obsidian-skills) + the Karpathy LLM-Wiki it composes with

## Source

- Repo: [github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — author **Steph Ango** (GitHub `kepano`), **CEO of Obsidian**.
- Verified (`gh api`, 2026-06-29): **38,756★**, 2,746 forks, **MIT**, created **2026-01-02**, active. **`obsidianmd/obsidian-skills` = 404** (no official-org repo).
- Karpathy LLM-Wiki pattern: [gist.github.com/karpathy/442a6bf...](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (this vault's foundation).

## What the video claims

"Turn a folder of markdown files into a knowledge system Claude Code can read/write/tag/link — a miniature RAG with no DB, no embeddings, no infrastructure. And this wasn't built by some random dev — it was built by **Kepano, the CEO of Obsidian himself**." Demos: project tracking, Obsidian **base files**, per-project folders with conversation-log/links/overview constraints, and the **graph view**.

## What it actually is (verification)

- **Attribution — CONFIRMED-with-nuance:** Steph Ango (kepano) **is** Obsidian's CEO, and he **did** author this skill. BUT it's his **personal** GitHub repo (`kepano/obsidian-skills`), **not** an official Obsidian-organization product. (`obsidianmd/obsidian-skills` does not exist — verified 404.) So "built by the CEO" ✓; "official Obsidian product" ✗.
- **What it contains:** **5 *format-handling* Agent Skills** — `obsidian-markdown` (wikilinks/frontmatter), `obsidian-bases` (.base files), `json-canvas` (.canvas), `obsidian-cli` (vault CLI), `defuddle` (web extraction). They teach an agent to read/write Obsidian formats *without syntax errors*.
- **⚠️ "Zero-overhead RAG" — REFUTED as a description of the skill:** the skill is **not a RAG system**. It's format expertise. The "zero-overhead markdown knowledge base, no embeddings" *is the **Karpathy LLM-Wiki pattern*** (raw → compiled wiki → index, full-context loading at small scale) — a **separate** architecture (e.g. `ar9av/obsidian-wiki`) that **composes with** the skill. The video conflates the two. They're complementary: the skill provides format-handling; the Karpathy pattern provides knowledge-management discipline.

## Why this is the highest-relevance, lowest-novelty skill for the operator

**This vault IS the thing the video is gesturing at.** Storm Bear + autopilot-research are both Karpathy LLM-Wiki vaults; the operator's `~/.claude` memory is an L1+L2 system ([[claude-code-memory-systems/_index]]). So:

- **Value = a real upgrade, not a new idea:** installing `kepano/obsidian-skills` lets Claude Code maintain the vault's Obsidian-specific syntax (`.base`, `.canvas`, wikilink edge-cases) cleanly — fewer malformed files during compiles/audits.
- **No conceptual change:** the librarian discipline, `_master-index.md`-first, `[[wiki links]]` — the operator already does all of this by hand-rolled `CLAUDE.md` rules. The skill just makes the *agent* fluent in the formats.

## Operator relevance — concrete

- **autopilot vault:** install the skill so the drain/compile steps emit valid `.base`/`.canvas` and clean wikilinks; pair with `obsidian-cli` for graph-view-driven audits.
- **Storm Bear vault:** same, plus `defuddle` could replace ad-hoc web-extraction in ingestion.
- **Distinction to record:** keep "operational memory" (`~/.claude`) and "research wiki" (these vaults) as two systems — the same Rule-7 reconciliation already noted in [[claude-code-memory-systems/_index]].

## Install safety

MIT, no postinstall, authored by a known figure (Obsidian's CEO), copy `skills/` into `.claude/skills/`. Safe.

## Key Takeaways

- Real and by Obsidian's CEO — but his **personal** repo, **not** an official Obsidian product, and **not itself a RAG**.
- The "markdown-folder-as-knowledge-base" is the **Karpathy pattern** this vault already runs; the skill is the *format-fluency* layer that composes with it.
- Highest relevance / lowest novelty in the stack: install it as a quality upgrade to the vault toolchain.

## Related

[[claude-code-memory-systems/_index]] · [[graphify-codebase-graph/_index]] · [[ai-operating-system/_index]] · [[claude-code-skills-stack/overview]]
