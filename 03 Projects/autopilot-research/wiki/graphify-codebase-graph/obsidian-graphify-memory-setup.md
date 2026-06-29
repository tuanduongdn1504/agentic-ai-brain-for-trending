# Obsidian + Graphify as a memory system (the lucasrosati deep-dive)

> **Source:** [[graphify-codebase-graph/_index]]. Deep-dive of [github.com/lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) — the repo behind the "**71.5× fewer tokens per session on Claude Code with Obsidian + Graphify**" framing. Of all the originals, this is the one **closest to what you already do** (an Obsidian LLM Wiki).

## What it is

A **3-layer persistent-memory system** built around a single centralized **Obsidian vault**:

1. **Persistent Memory Layer** — atomic **Zettelkasten** notes with mandatory YAML frontmatter, organized into `permanent/`, `logs/`, `chats/`, and project MOCs (maps-of-content).
2. **Codebase Knowledge Graph Layer (Graphify)** — tree-sitter AST code graphs (**$0 in AST-only mode**) emitted into `graphify/<project>/`, surfaced inside Obsidian's native graph view via wikilinks.
3. **Chat Import Pipeline** — a **daily cron job** runs `claude_to_obsidian.py`: extracts Claude conversations (Code *or* Web via a browser extension), auto-detects origin, keyword-tags them, inserts wikilinks to existing notes, and files them under `chats/code/` or `chats/web/`.

- Session commands in a root `CLAUDE.md`: `/resume`, `/save`.
- Build: `/graphify . --obsidian --obsidian-dir ~/vault/graphify/<project>` (skill form) or `graphify extract . --out ./graphify-out` (headless).
- **MIT**, Python 85.8% / Shell 14.2%, ~786 stars, created 2026-04-12. Requires `pip install graphifyy` + `pip install claude-conversation-extractor`.

## The discipline it enforces (sound familiar?)

- **1 concept per permanent note**, mandatory frontmatter, **kebab-case filenames**, **≥2 wikilinks per note.**
- Recommended Obsidian graph filters: `path:permanent` (manual notes only), `path:graphify` (code structure only), `tag:chat-import` (imported convos), `-path:graphify -path:chats` (your manual annotations without generated noise).

> This is **textbook Zettelkasten** — and structurally near-identical to your vault's librarian rules (one-fact-per-file, frontmatter, `[[wiki links]]`, kebab-case). The difference is **what's automated.**

## Overlap & difference vs your hand-curated vault

| | Your vault (Storm Bear / autopilot) | lucasrosati setup |
|---|---|---|
| Note shape | 1-concept, frontmatter, `[[links]]`, kebab-case | **Identical** |
| Knowledge capture | **Hand-curated** by the librarian | **Automated**: cron chat-import + AST-generated structural notes |
| Code structure | Described in prose articles | **Auto-generated** from `graph.json` into vault notes |
| Synthesis | Curated articles + Pattern Library | None — it's capture + structure, not synthesis |
| Scope | Multi-project, hand-written summaries | Single vault, auto-routed imports |

- **What you could borrow:** the **automated chat-import pipeline** is the genuinely novel piece — a cron that turns every Claude conversation into a tagged, wikilinked vault note is a *capture* mechanism your manual memory doesn't have. (Compare your `~/.claude/.../memory/` L2 system in [[claude-code-memory-systems/your-current-setup-mapping]].)
- **What to be wary of:** auto-generated AST notes can **flood** a curated vault with low-signal nodes — hence its own filter recommendations. Keep generated content in a **separate folder** (`graphify/`, `chats/`) so it never pollutes your curated `wiki/`.

## ⚠️ Claims to treat as unverified

- The **"71.5× per session"** headline is the **same cherry-picked number** as upstream Graphify, re-applied — **no derivation provided** in the repo. See [[graphify-codebase-graph/token-savings-reality]].
- A repo test claims **"499× token reduction per query"** on a React+Supabase 126-file project — **vendor claim, no reproducible methodology.** Don't quote it as fact.
- Gotcha noted in the repo: Graphify filenames with parentheses (e.g. `myFunction().md`) can confuse Obsidian indexing (needs an app restart).

## Key Takeaways

- It's a **3-layer Obsidian memory system**: Zettelkasten notes + Graphify code graphs + an **automated daily chat-import cron** — the last being the part worth stealing.
- **Structurally near-identical to your vault's note discipline** — the difference is automation vs curation.
- **Keep generated graph/chat notes in separate folders** so they don't drown curated synthesis.
- Its 71.5× / 499× numbers are **unverified vendor claims** — benchmark before believing.
