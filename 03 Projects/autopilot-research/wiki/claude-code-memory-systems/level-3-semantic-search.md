# Level 3 — Semantic search: meaning, not just keywords

> **Source:** [[claude-code-memory-systems/_index]] · video [16:55–23:45] + deep-dive of [MemSearch](https://github.com/zilliztech/memsearch) (Zilliz) and the [claude-mem](https://github.com/thedotmack/claude-mem) alternative.

**The problem L3 solves:** run L2 for months across multiple projects and (1) `general.md` bloats past efficient reading, and (2) **keyword** search breaks — your notes summarize topics, so the exact words you search for aren't there. L3 indexes meaning.

## The pattern it ports: the OpenClaw* memory architecture

L3's design comes from a standalone agent's memory system (the video calls it **"Open Claude"**; the MemSearch repo calls it **"OpenClaw"** — naming flagged in [[claude-code-memory-systems/source-provenance]]). Its **3 layers**:

1. **`memory.md`** — long-term **durable facts** (preferences, decisions, business facts). Loaded at session start.
2. **Daily notes** — **one file per date**, a running log (what happened / decided / shipped / failed). Today + yesterday load automatically; older ones stay on disk but out of context.
3. **"Dreaming"** (optional) — a **background process** that reads daily notes, **scores** them, **promotes** recurring ones into long-term `memory.md`, and lets stale stuff be forgotten. (Same idea as L2's `reorganize memory`, but automatic + score-driven.)

> Net effect: a real **short-term vs long-term** memory split, with promotion deciding what gets durably remembered.

## MemSearch (Zilliz) — the port into Claude Code

Zilliz (the team behind the **Milvus** vector DB) extracted that architecture into a Claude Code plugin.

- **Install (two lines):**
  ```
  /plugin marketplace add zilliztech/memsearch
  /plugin install memsearch
  ```
  Then `/reloadplugins` (or Ctrl-C twice + reopen). Install **for this repo only** to keep it scoped.
- **Markdown-first philosophy** (kept from OpenClaw): everything stays in **readable markdown you can port** — same `memory.md` + daily-notes file structure. The vector index sits *beside* the markdown, it doesn't replace it.
- **How retrieval works:** it **chunks your documents into semantic vectors**, then uses a **hook to auto-inject the top matches into context**. The *video* names the **`UserPromptSubmit`** hook injecting the **top-3 semantic matches** as soon as you type. The *repo README* emphasizes a **`Stop` hook** that captures every conversation turn + auto-invocation "when Claude senses the question needs history." (Capture-on-Stop and inject-on-UserPromptSubmit are different phases; the repo is the primary source — confirm exact hooks by inspecting the plugin. Flagged in source-provenance.)
- **Retrieval depth:** "3-layer progressive retrieval" (L1 semantic search → L2 chunk expansion → L3 transcript parsing); **hybrid search** (BM25 + dense vectors + RRF reranking); SHA-256 content hashing to skip unchanged content on re-index.
- **Files it creates:** `.memsearch/` (config/state) + `memory/` daily markdown + `.memsearch/PROJECT.md` + `.memsearch/USER.md` + `.memsearch/skill-candidates/` (distilled procedural memory) + `.memsearch/milvus.db` (Milvus Lite default).
- **Commands:** `/memory-recall` (explicit recall) + `/memory-config` (manage PROJECT.md / USER.md / skill distillation). Natural-language auto-invocation also works.
- **Verify it's working:** have a few conversations, then list `.memsearch/memory/` and confirm today's file exists — or run the `memory recall` skill.

## The alternative: claude-mem (MCP-based)

Also popular, similar goal, **different philosophy** — the video judges it "a bit overkill for what we need."

- **What it is:** a Claude Code plugin that auto-captures everything Claude does, **compresses it with AI**, and injects relevant context into future sessions.
- **Architecture:** **MCP tools** + a **3-tier storage model** — *summaries* (compact index, ~50–100 tokens), *timeline* (chronological context), *observations* (full detail, ~500–1,000 tokens, fetched selectively). Backed by **SQLite + FTS5** and a **Chroma** vector DB, with a worker service (HTTP on port **37777**) and **5 lifecycle hooks** (SessionStart / UserPromptSubmit / PostToolUse / Stop / SessionEnd).
- **Install:** `npx claude-mem install` *or* `/plugin marketplace add thedotmack/claude-mem` + `/plugin install claude-mem`.
- **Extras:** web **dashboard** (`localhost:37777`), team collaboration, cost/token visibility, **privacy labels** (`<private>` tags), beta "Endless Mode".
- **The two differences that matter (video's framing):**
  1. **MCP vs hook injection** — claude-mem retrieves via **MCP tool calls Claude must decide to make**; MemSearch **auto-injects from a local index** (no decision needed).
  2. **Opaque DB vs plain markdown** — claude-mem stores **in the background DB**; MemSearch keeps **readable markdown you can re-open and port**.

## Which, and why MemSearch wins for this use case

The video picks **MemSearch**: auto-injection (no "remember to search") + everything in **readable, portable markdown** + OpenClaw's proven memory patterns, all **inside Claude Code**. claude-mem's dashboard/team/cost layer is real value if you want a *management* surface — but it's a heavier, MCP-gated, DB-backed bet.

## Key Takeaways

- L3 adds **semantic (meaning-based) retrieval** when L2's keyword search stops scaling — and a **hook auto-injects** the top matches so you never have to ask.
- It ports the **OpenClaw 3-layer architecture**: long-term `memory.md` + per-day notes + **"dreaming"** promotion (auto-consolidation).
- **MemSearch** (Zilliz/Milvus): two-line install, **markdown-first + vector index**, hybrid BM25+dense, `/memory-recall`. The recommended L3.
- **claude-mem**: MCP + SQLite/Chroma + dashboard + privacy labels — more features, but **MCP-gated retrieval** + **opaque DB**; "overkill" for plain operational memory.
- **Decision axis that recurs all the way up:** *auto-injected readable markdown* (MemSearch) vs *tool-called opaque DB* (claude-mem). You'll see it again at L4 and L6.
