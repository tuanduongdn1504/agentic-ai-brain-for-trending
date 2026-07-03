# How Claude memory actually works — four surfaces, zero vector DBs

## Sources (all T1 Anthropic, fetched by workflow agents + main-loop ground-checks)

- claude.ai memory: [support.claude.com — "Use Claude's chat search and memory…"](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- API memory tool: [platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) (**main-loop fetched in full**)
- Managed Agents memory + Dreams: [platform.claude.com/docs/en/managed-agents/memory](https://platform.claude.com/docs/en/managed-agents/memory) + [/managed-agents/dreams](https://platform.claude.com/docs/en/managed-agents/dreams)
- Claude Code auto-memory: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (**main-loop fetched in full**)

## The four surfaces

### 1. claude.ai (consumer) — timed summary synthesis
- "Memory is a **synthesis of key insights across your chat history** that is **updated every 24 hours**." Visible, editable, project-scoped. → Consolidation trigger = **time-based (24h)**, not conversation-count. Same summary-not-retrieval family as ChatGPT.

### 2. Claude API memory tool — client-side files (GA)
- Tool type **`memory_20250818`**, **generally available on the Messages API — no beta header** (per current platform docs; the claude-api skill confirms). Client-side: "Claude requests file operations, and your application executes them" against a `/memories` directory you control.
- Commands: `view`, `create`, `str_replace`, `insert`, `delete`, `rename`. The API auto-injects a memory protocol prompt ("ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE… ASSUME INTERRUPTION").
- **No automatic consolidation** — the model curates its own files; pairing with **context editing** (clears old tool results) and **compaction** (server-side summarization) is the documented long-session pattern.
- Security burden is on the implementer: path-traversal validation on every command is required (`/memories/../../secrets.env` is the documented attack).

### 3. Managed Agents — memory stores + the Dreams feature
- A memory store is "a workspace-scoped collection of **text documents**… mounted as a directory inside the session's sandbox. The agent reads and writes it with the same file tools it uses for the rest of the filesystem" (FUSE mount at `/mnt/memory/<store>/`; ≤100KB per memory; immutable per-mutation versions with redact).
- **Dreams — Anthropic's literal consolidation agent**: "A dream reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store: **duplicates merged, stale or contradicted entries replaced with the latest value, and new insights surfaced**." Trigger = **explicit API call**, not automatic.

### 4. Claude Code — CLAUDE.md + auto-memory
- Two systems: CLAUDE.md (human-written instructions) + **auto memory** (Claude-written learnings) at `~/.claude/projects/<project>/memory/` — `MEMORY.md` index (first **200 lines or 25KB** loaded every session) + on-demand topic files. "Claude decides what is worth remembering." No documented scheduled consolidation. *(This is the operator's own memory system — the one maintaining the notes for this very wiki.)*

## The two headline facts

1. **Zero vector databases.** Across all four documented surfaces, no embeddings, no similarity search, no RAG — files, mounts, and timed summaries. The video's "semantic and episodic memory live in vector stores… this is how Claude memory works" is REFUTED by every Anthropic primary source (both adversarial verifiers, 15/15 claims CONFIRMED against docs).
2. **Consolidation exists but is never count-gated:** 24-hour timer (claude.ai), explicit Dreams call (Managed Agents), model-discretion (Claude Code), none (API tool — you build it). And with OpenAI's "Dreaming V3," **both vendors independently converged on dream vocabulary** for background memory reorganization in 2026 — the sleep-consolidation metaphor made literal ([[memory-taxonomy-and-cogsci-lineage]]).

## ⚠️ "AutoDream" — reported-only

A third-party blog (zenvanriel.com) describes a Claude Code "AutoDream" auto-consolidation cycle (≥24h + ≥5 sessions; Orient→Gather→Consolidate→Prune; <25KB output; "shipped ~2026-03"). **The official Claude Code memory docs (fetched 2026-07-03) contain no such feature.** Treat as unverified single-source — same status as the prior "Kairos daemon" rumor in [[../claude-code-memory-systems/level-1-native]]. Details in [[caveats-and-corrections]].

## Key Takeaways

- Anthropic's answer to agent memory is **"files the model reads and writes"** at every layer — the strongest production counterexample to vector-store-by-default, and the pattern the operator's vault already embodies.
- The API memory tool + context editing + compaction is the **buildable kit for hireui's memory layer** — no new infrastructure, ZDR-eligible, storage stays in your app.
- Dreams (explicit, auditable, reorganize-don't-append) is the design to copy for a consolidation pilot: merge duplicates, replace stale values, surface insights — the same verbs as the vault's `consolidate-memory` skill.
