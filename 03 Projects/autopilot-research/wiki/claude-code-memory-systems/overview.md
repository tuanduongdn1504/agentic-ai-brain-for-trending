# Overview — the 6 levels of Claude Code memory

> **Source:** [[claude-code-memory-systems/_index]] · Simon Scrapes [UHVFcUzAGlM](https://www.youtube.com/watch?v=UHVFcUzAGlM).

## The one question every memory system answers

> *"When you give Claude Code a task, how does it pull the right context at the right time?"*

Every system in this taxonomy is just a different answer, and they differ on exactly **two axes**:

1. **Where memory lives** — the storage mechanism + file structure. Plain markdown? Vectors in a DB? On your laptop? In the cloud?
2. **How Claude gets it** — the retrieval stage. Copied into context automatically? Searched on demand? Injected by a hook? Queried over MCP?

Hold those two axes in mind and the whole field collapses from "ridiculous to keep up with" into a clean progression.

## The universal enemy: context rot

**Context rot** = an LLM's inability to reliably recall 100% of what's in its window as the window fills up. More loaded context → worse recall. So "just put everything in `CLAUDE.md`" *fails* at scale. **Every level past Level 1 is a different strategy for loading *less*, at the *right time*.** This is the same problem [[claude-api-cost-optimization/_index]] attacks with context engineering + compaction.

## The 6 levels

| Lvl | Name | Where memory lives | How Claude retrieves | Tool / origin | Readable MD? | Local? |
|---|---|---|---|---|---|---|
| **1** | Native | `CLAUDE.md` + `.claude/.../memory/memory.md` | Auto-loaded at session start | Ships with Claude Code | ✅ | ✅ |
| **2** | Reliable recall | Structured `.claude/memory/` (index + general + domain + tools) | **Hook auto-injects** the index every session | [[claude-code-memory-systems/level-2-reliable-recall-hooks\|Connolly / Huryn]] | ✅ | ✅ |
| **3** | Semantic search | Markdown + a **vector index** | Hook injects **top-N semantic matches** on each prompt | [[claude-code-memory-systems/level-3-semantic-search\|MemSearch]] / claude-mem | ✅ (MemSearch) | ✅ |
| **4** | Verbatim recall | SQLite (entities) + **ChromaDB** (verbatim chunks) | Semantic search → exact words, via background hooks | [[claude-code-memory-systems/level-4-verbatim-mempalace\|MemPalace]] | ❌ (opaque) | ✅ |
| **5** | Knowledge base | `raw/` + `wiki/` plain markdown, Obsidian graph | Read the **index** first, drill into pages | [[claude-code-memory-systems/level-5-knowledge-base-llm-wiki\|Karpathy LLM Wiki]] / Recall | ✅ | ✅ |
| **6** | Cross-tool brain | One **Postgres** table (`thoughts`) on Supabase | Every tool queries it over **MCP** | [[claude-code-memory-systems/level-6-cross-tool-brain\|OpenBrain]] / Mem0 | ❌ (DB) | ❌ (cloud) |

**The shape of the progression:** L1→L2 = make native memory *reliable* (hooks). L2→L3 = make it *searchable by meaning* (vectors). L3→L4 = make recall *verbatim* (nothing summarized). L5 = a *different job* (build a researched knowledge base, not remember your work). L6 = make memory *portable across every AI tool* (not just Claude Code).

## The stacking insight (the most practical takeaway)

> "A lot of them stack together. You can run levels 1, 2, and 3 together with no issues — the folder structure is fairly similar." — Simon Scrapes

L1, L2, L3 all share a **markdown-first folder shape** (`memory.md` index + topic/daily files). L2 adds a session-start injection hook; L3 adds a vector index + a per-prompt injection hook *on top of the same files*. So the realistic path is **not** "pick one" — it's **layer them**. The author's own verdict: **he runs up to Level 3** in his Agentic OS.

## "Which one should I pick?" — the decision guide

The video's explicit recommendations, distilled:

- **Just starting?** → **Level 1 only.** Use `CLAUDE.md` + `memory.md` properly (keep `CLAUDE.md` < 200 lines, reference external files). 10 minutes; massive improvement. *Don't install anything.*
- **Used Claude Code a while; memory files growing?** → **Level 2.** Install the Connolly hook. *"Honestly, most of you should stop right there."*
- **Months of context; losing old decisions; keyword search failing?** → **Level 3** (MemSearch, semantic) or **Level 4** (MemPalace, verbatim word-for-word).
- **Want a researched, interconnected knowledge base on topics you care about?** → **Level 5** (LLM Wiki, or hosted Recall). *Different job from operational memory.*
- **Use multiple AI tools (ChatGPT on phone, Cursor, Claude Desktop) and want them to share one memory?** → **Level 6** (OpenBrain if you want ownership; Mem0 if you're shipping a product).

**Two triggers to move from L2 → L3 (both must be true):** (1) you've used Claude Code > 1 month and have more than a handful of memory files; (2) you've asked Claude something you *know* is in your notes and it couldn't find it.

## ⚠️ Conflict flag: two "Simon Scrapes 6 levels" exist

The existing [[ai-operating-system/_index]] article records a *different* Simon Scrapes video's "6 levels of memory" as **"static files → session-local → append-only logs → categorized → auto-categorized → semantic search."** That is **not** the taxonomy in *this* dedicated video, which is the level structure in the table above (native → hooks → semantic → verbatim → knowledge-base → cross-tool). Per Rule 7 (surface conflicts, don't average): **treat *this* topic as the authoritative memory taxonomy** (it's the dedicated 41-min deep-dive); the `ai-operating-system` phrasing was a looser paraphrase from the broader Agentic-OS video. Do not blend the two lists.

## Key Takeaways

- Two axes explain everything: **where memory lives** + **how Claude retrieves it**.
- **Context rot** is why "stuff it all in `CLAUDE.md`" breaks — every level past L1 loads *less, at the right time*.
- **Levels 1–3 stack** on a shared markdown folder shape; layer them rather than choosing.
- The honest default for most people: **Level 1 done right, then the Level 2 hook — and stop.**
- L5 (knowledge base) and L6 (cross-tool) are *different jobs*, not "more memory" — reach for them only on their specific use case.
