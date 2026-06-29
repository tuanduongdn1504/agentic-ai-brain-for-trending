# Your current setup, mapped onto the 6 levels

> **Source:** [[claude-code-memory-systems/_index]]. This article is the operator-specific synthesis — where *your* actual systems sit on the taxonomy, and the two upgrades worth making. Based on the vault `CLAUDE.md` files + your `~/.claude/.../memory/MEMORY.md` (visible in this session).

## The map

| Your system | Level(s) | Evidence | State |
|---|---|---|---|
| **`~/.claude/projects/.../memory/MEMORY.md`** + per-fact topic files | **L1 + manual L2** | Native auto-memory index (L1) you maintain by hand with L2 *discipline*: one-fact-per-file, `MEMORY.md` as a 1-line-pointer index, `**Why:**` / `**How to apply:**` (= date/what/why), `[[name]]` cross-links, typed (`user`/`feedback`/`project`/`reference`) | ✅ Running; **missing only the injection hook + `reorganize` ritual** |
| **autopilot-research vault** (this project) | **L5** (industrialized) | raw/ (read-only) + wiki/ (LLM-owned) + `_master-index.md` + per-topic `_index.md` + `[[wiki links]]` + compile/query/audit verbs + loop-log = Karpathy LLM Wiki, productized | ✅ Mature (20+ topics) |
| **Storm Bear curated vault** (`/Users/Cvtot/KJ OS Template`) | **L5** (industrialized) | Same LLM-Wiki pattern at larger scale (Pattern Library, `_state/` chapters, 12-rule CLAUDE.md) | ✅ Mature |
| **hireui** (`/Users/Cvtot/monorepo/hireui`) | **L1/L2 (per-repo)** | Its own CONSTITUTION + BMAD harness + `.pilot-log` = project-scoped operational memory | ✅ Running; could adopt L2 hooks |
| **Telegram / cross-device access** | *adjacent to L6* | [[telegram-remote-control-stack/_index]] is cross-*device* control, **not** cross-*tool memory* — you have no L6 shared brain | ❌ Not present |

## The key realization

**You are not a beginner on this taxonomy — you're already at L1+L2+L5, just with the L2 automation done by hand.** Your `MEMORY.md` index is *textbook* Connolly/Huryn ([[claude-code-memory-systems/level-2-reliable-recall-hooks]]): index file + one-fact files + date/why entries + the "ask before editing existing notes" safety rule + the typed-staging→promotion lifecycle (your `reference`/`project` types ≈ their `domain`/`tools`). The video's "most of you should stop at Level 2" lands as: **you've already arrived; just remove the manual upkeep.**

## The two upgrades worth making (everything else: skip, on purpose)

### Upgrade 1 — automate your manual L2 (hook + ritual). Highest leverage, ~1 hour.
You already keep the index + files by hand. Add:
- a **`reorganize memory`** ritual (run in plan mode periodically — dedupe, merge, split, re-sort, re-index) so the index doesn't drift; and
- *optionally* a **SessionStart/PreToolUse `additionalContext` hook** to auto-inject `MEMORY.md` so recall stops depending on Claude reading it.
→ Pilot **A1/A2** in the methods file.

### Upgrade 2 — add semantic retrieval (L3) to the *vaults*, so retrieval scales. Medium effort.
Your two vaults are L5 and **growing past keyword-search comfort** (the Storm Bear vault already hit a 146K-token CLAUDE.md that forced the `_state/` refactor — that *is* context rot). Karpathy's own escape hatch is a hybrid search tool (`qmd`) over the wiki; MemSearch is the Claude-Code-native version. Either gives meaning-based retrieval over the wiki without abandoning markdown.
→ Pilot **B7/B8** in the methods file.

### What to consciously NOT adopt (and why)
- **L4 (MemPalace):** verbatim recall is opaque (non-markdown) — it fights your whole readable-markdown, version-controlled philosophy. Skip unless you hit a specific "exact words from weeks ago" need.
- **L6 (OpenBrain/Mem0):** you live mostly inside Claude Code; you don't switch tools constantly. Adds cost + latency + an off-laptop DB for a problem you don't have. Revisit only if you start doing serious work in ChatGPT/Cursor *and* need shared memory.
- The video's own author stops at **L3** — and his use case is broader (multi-tool Agentic OS) than yours. For you, **L1+L2 automated + L3 retrieval on the vaults** is the complete, honest endpoint.

## The strategic tension to hold (don't resolve by averaging)

The video argues **L5 (LLM Wiki) is for research, not operational memory** — and your vaults *are* L5 used heavily. This is **not** a reason to abandon the vault; it's a reason to **keep two systems separate** ([[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]]):
- **Operational memory** = `~/.claude/.../memory/` (L1/L2/L3) — "what did I decide / how do I work."
- **Research knowledge base** = the vaults (L5) — "what do I know about topic X."

Trying to make the vault do operational recall (or stuffing research synthesis into `MEMORY.md`) is the mistake the video is actually warning against. Your instinct to run both is correct — just keep the boundary crisp.

## Key Takeaways

- You're already at **L1 + a hand-run L2 + two industrialized L5 vaults** — not starting from zero.
- Your `~/.claude/.../memory/MEMORY.md` is **textbook L2 structure**; the only gap is **automation** (hook + `reorganize` ritual).
- **Two upgrades:** (1) automate L2 (~1 h, highest leverage); (2) add **L3 semantic retrieval to the vaults** so retrieval scales past keyword search (the `_state/` refactor was context rot in action).
- **Deliberately skip L4 + L6** — they fight your readable-markdown/own-your-data philosophy and solve problems you don't have.
- Keep **operational memory (L1/L2/L3)** and the **research wiki (L5)** as **two separate systems** — that separation *is* the video's real lesson.
