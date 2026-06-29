# claude-code-memory-systems

> **Topic index.** A 6-level taxonomy of how Claude Code "remembers" — from the native `CLAUDE.md` + auto-memory that ships in the box, up to a single Postgres "brain" shared across every AI tool you use. Every level answers the *same* question two ways: **where memory lives** (storage/format) and **how Claude gets it** (retrieval).
>
> **Origin:** Simon Scrapes, **"Every Claude Code Memory System Compared (So You Don't Have To)"** ([UHVFcUzAGlM](https://www.youtube.com/watch?v=UHVFcUzAGlM), 2026-04-23, 41:21, ~130K views). Per the operator's "**double deep-dive into the original resource**" ask, this topic also deep-dives the **primary sources the video is built on**: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [John Connolly's memory write-up](https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory) (built on [Paweł Huryn](https://substack.com/@huryn/note/c-216337711)), [MemSearch](https://github.com/zilliztech/memsearch), [MemPalace](https://github.com/MemPalace/mempalace), [claude-mem](https://github.com/thedotmack/claude-mem), and [OpenBrain/OB1](https://github.com/NateBJones-Projects/OB1).
>
> **Source provenance:** primary-source-grounded (the gist, the repos, and the article were fetched directly — not via a NotebookLM bundle). Video-only claims (a leaked Anthropic "Kairos" daemon; OpenBrain's "<$1/month"; MemPalace's "highest benchmark ever") are flagged. Full tiering in [[claude-code-memory-systems/source-provenance]]. Constitutional rule #4 (never fabricate) honored.

---

## The headline for *you*

You are **already running Level 1 + a hand-maintained Level 2**: your `~/.claude/projects/.../memory/MEMORY.md` (a 200-line index pointing at one-fact-per-file topic notes, date/what/why entries) **is almost exactly** the Connolly/Huryn structure in Level 2 — you just do the upkeep manually instead of via a hook. And both your vaults (autopilot-research + the Storm Bear curated vault) **are Level 5** (Karpathy LLM Wiki). So this taxonomy isn't new tooling to adopt — it's a **map of where you already stand and the two cheap upgrades worth making** (hook-automate L2; add semantic retrieval / L3 so the vaults scale). See [[claude-code-memory-systems/your-current-setup-mapping]].

---

## Articles

- [[claude-code-memory-systems/overview]] — the core model (where memory lives × how Claude retrieves it), the 6-level table, the stacking insight (L1+L2+L3 compose), and the decision guide ("which one should I pick?").
- [[claude-code-memory-systems/level-1-native]] — `CLAUDE.md` + auto-memory + `memory.md`, the `/memory` command, **context rot** + the 200-line rule, and the (unverified) leaked **Kairos** daemon.
- [[claude-code-memory-systems/level-2-reliable-recall-hooks]] — **the deep-dive**: Connolly/Huryn's structured `.claude/memory/` (index + general + domain + tools), the `CLAUDE.md` prompt, the SessionStart/PreToolUse **auto-injection hook**, the `reorganize memory` ritual, and 5-day results.
- [[claude-code-memory-systems/level-3-semantic-search]] — search by *meaning*: **MemSearch** (Zilliz; ports the OpenClaw memory architecture; markdown-first + vector index + hook auto-injection) and the **claude-mem** alternative (MCP + SQLite/Chroma + dashboard).
- [[claude-code-memory-systems/level-4-verbatim-mempalace]] — **MemPalace**: local-first *verbatim* recall, SQLite-entities + ChromaDB-vectors, the "AAAK" symbolic index, the wings/rooms/drawers metaphor, SessionEnd/PreCompact hooks, `mine` for retro-indexing.
- [[claude-code-memory-systems/level-5-knowledge-base-llm-wiki]] — **Karpathy's LLM Wiki** (raw/ + wiki/, markdown, the librarian, the index, no vector DB) + the hosted **Recall** + the enterprise **LightRAG** — and the video's pointed **critique** (LLM Wiki = research, *not* operational memory) that directly challenges your vault thesis.
- [[claude-code-memory-systems/level-6-cross-tool-brain]] — one brain for ChatGPT + Claude + Cursor: **OpenBrain/OB1** (your own Postgres on Supabase + MCP gateway) vs the well-funded hosted **Mem0**.
- [[claude-code-memory-systems/your-current-setup-mapping]] — exactly where your `~/.claude/` memory, the autopilot vault, the Storm Bear vault, and hireui sit on the 6 levels, and the two upgrades worth making.
- [[claude-code-memory-systems/source-provenance]] — the video, the originals, and the verified-vs-flagged claim log.

## Pilot methods (how to apply this to your flow)

**17 ranked methods** across your flows live in `output/(C) 2026-06-20-claude-code-memory-systems-pilot-methods.md` — five angles: **(A) your personal `~/.claude` memory** (formalize manual L2 → hook-injected L2; add L3 retrieval), **(B) the autopilot-research vault** (it's L5 — harden it, add semantic search so retrieval scales), **(C) the Storm Bear curated vault** (the `reorganize memory` ritual; the index-first discipline), **(D) hireui** (a per-repo project memory done right), **(E) Scrum coaching** (the taxonomy as a team-knowledge lens).

## Cross-topic links

- **Sister topic (same taxonomy, looser framing):** [[ai-operating-system/_index]] — references a *different* Simon Scrapes video's "6 levels"; this dedicated video is the **authoritative** version. Discrepancy flagged in [[claude-code-memory-systems/overview]].
- **Your vault's foundation:** Level 5 *is* the LLM Wiki pattern this whole project runs on (see project `CLAUDE.md`).
- **Context-budget discipline:** [[claude-api-cost-optimization/_index]] (context engineering / compaction) — the same "context rot" problem these memory systems fight.
- **Hooks mechanics:** [[claude-code-hooks/_index]] — SessionStart / UserPromptSubmit / PreToolUse / SessionEnd / PreCompact are the load-bearing primitive for Levels 2–4.
- **Skills-as-memory:** [[claude-cowork/skills-vs-plugins-hierarchy]] + [[ai-operating-system/_index]] (progressive disclosure).

## Key Takeaways

- Every memory system answers one question — *"when Claude gets a task, how does it pull the right context at the right time?"* — and differs only on **where memory lives** + **how Claude retrieves it**.
- **Levels stack.** L1+L2+L3 share a markdown-first folder shape and compose cleanly; the video author personally runs **up to Level 3**.
- The universal enemy is **context rot** — LLM recall degrades as you stuff more into the window. Every level past L1 is a different bet on *loading less, at the right time*.
- **Markdown-first (L1/L2/L3/L5) vs opaque-DB (L4/L6):** you can read/own/port the former; the latter trade readability for verbatim recall or cross-tool reach.
- **Operational memory ≠ knowledge base.** Levels 1–4 + 6 are about *remembering your work*; Level 5 (LLM Wiki) is about *building a researched knowledge base* — the video argues they're different jobs, and that most people over-reach.
