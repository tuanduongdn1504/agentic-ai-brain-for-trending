# Source provenance — what's verified vs flagged

> **Source:** [[claude-code-memory-systems/_index]]. Constitutional rule #4 (never fabricate) + Storm Bear prime directive (don't make things up). This topic was built **primary-source-first**: the video gave the *map*, and the originals (the gist, the repos, the article) were **fetched directly** to verify the detail — rather than relying on a NotebookLM bundle. This log tiers every load-bearing claim.

## Sources fetched directly (primary)

| # | Source | URL | Used for |
|---|---|---|---|
| Video | Simon Scrapes, "Every Claude Code Memory System Compared" | [UHVFcUzAGlM](https://www.youtube.com/watch?v=UHVFcUzAGlM) | The 6-level taxonomy + the decision guide (yt-dlp full transcript, 8,276 words) |
| Orig | Karpathy LLM Wiki gist | [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | L5 deep-dive (architecture, verbs, index/log, retrieval) |
| Orig | John Connolly, "How I finally sorted my Claude Code memory" | [youngleaders.tech](https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory) | L2 deep-dive (folder structure, the hook .py/.sh + settings.json, reorganize, 5-day results) |
| Orig | Paweł Huryn note (the original concept) | [substack](https://substack.com/@huryn/note/c-216337711) | L2 origin (predates auto-memory; date/what/why) |
| Orig | MemSearch (Zilliz) | [github](https://github.com/zilliztech/memsearch) | L3 (install, files, hybrid search, commands) |
| Orig | MemPalace | [github](https://github.com/MemPalace/mempalace) | L4 (two-DB arch, install, `mine`, benchmarks) |
| Orig | claude-mem | [github](https://github.com/thedotmack/claude-mem) | L3 alt (MCP 3-tier, hooks, dashboard) |
| Orig | OpenBrain / OB1 | [github](https://github.com/NateBJones-Projects/OB1) | L6 (Postgres/Supabase, MCP gateway, setup) |

## ✅ Verified against the primary source

- **L2 folder structure + discipline** (`memory.md` index / `general.md` / `domain/` / `tools/`, 200-line budget, date/what/why, write-immediately, lazy-load) — **confirmed in Connolly's article + Huryn's note.**
- **L2 hook is `.py` + `.sh` + `settings.json`, injects via `additionalContext`, getppid session id, flag-file fast path, 5-day 189→63-line result** — **confirmed in Connolly's article.**
- **Karpathy LLM Wiki: 3-layer (raw immutable / wiki LLM-owned / schema), ingest+query+lint verbs, `index.md` as retrieval, `log.md` append-only, no vector DB until scale (`qmd`), "bookkeeping is the bottleneck", Memex framing** — **confirmed verbatim-level in the gist.**
- **MemSearch: two-line install, Milvus/Zilliz, markdown-first, `.memsearch/` layout, hybrid BM25+dense+RRF, `/memory-recall` + `/memory-config`** — **confirmed in repo.**
- **MemPalace: SQLite entity-graph + ChromaDB verbatim chunks, palace metaphor, `mine`/`sweep` idempotent, install via `uv/pipx/pip`** — **confirmed in repo.**
- **claude-mem: MCP + 3-tier (summaries/timeline/observations), SQLite FTS5 + Chroma, worker on :37777, 5 hooks, privacy `<private>` tags, dashboard** — **confirmed in repo.**
- **OpenBrain: Postgres/Supabase, `thoughts` table (text+embedding+tags+timestamp), pgvector, MCP server + Edge Functions, ~45-min setup, FSL-1.1-MIT, you-own-export** — **confirmed in repo.**

## ⚠️ Flagged — video claim, NOT independently confirmed

| Claim | Where | Status |
|---|---|---|
| **"Kairos"** — leaked, unreleased Anthropic always-on memory daemon that consolidates notes "while you sleep" | Video L1 | **UNVERIFIED RUMOR.** Single-source, leak-derived; no first-party Anthropic confirmation. Directional point (Anthropic investing in native memory) is plausible; the **name + behavior are not confirmed.** Do not assert as fact. |
| **OpenBrain "less than \$1/month" / "10–30p on Supabase free tier"** | Video L6 | **VIDEO CLAIM.** The OB1 repo does **not** state pricing. Plausible for a tiny Supabase free-tier project, but unconfirmed by the source. |
| **MemPalace "highest benchmark score of any memory system ever published"** | Video L4 | **VENDOR/MARKETING CLAIM.** The author himself hedges ("apparently"). Repo cites 96.6%/98.4%/≥99% R@5 on LongMemEval — real numbers, but **"best ever" is not an independent finding.** |

## ⚠️ Flagged — naming / mechanism discrepancies (resolve by inspecting the tool)

| Item | Discrepancy | Resolution |
|---|---|---|
| **OpenClaw vs "Open Claude"** | Video (auto-transcript) says **"Open Claude"**; the MemSearch repo says it ports **"OpenClaw"** | The **repo is primary** → **"OpenClaw"** is the more reliable name. The *architecture* (long-term `memory.md` + daily notes + "dreaming" promotion) is consistent across both. Cross-ref [[claude-code-clones/_index]] which also records **OpenClaw** as a leak-derived Claude Code fork. |
| **MemSearch hook: `UserPromptSubmit` vs `Stop`** | Video says it **injects top-3 via `UserPromptSubmit`**; README emphasizes **capture via a `Stop` hook** + auto-invocation | These are **different phases** (inject-before vs capture-after) and a plugin can use both. **Confirm exact hooks by inspecting the installed plugin** before quoting one. Both agree retrieval is **hook-driven + auto**, not manual. |
| **MemPalace "AAAK" symbolic index** | Both video + repo say it exists; **full AAAK syntax is not publicly documented** | Treat AAAK as **real but under-documented** — describe its *purpose* (dense LLM-scannable pointer index), don't invent its grammar. |
| **L2 hook event: SessionStart vs PreToolUse** | Video frames it as SessionStart; Connolly's code uses **PreToolUse** (first-call flag) | Both produce the same effect (index loaded once, before real work). Documented in [[claude-code-memory-systems/level-2-reliable-recall-hooks]]. |

## Cross-topic conflict flagged (Rule 7)

- **Two "Simon Scrapes 6 levels" taxonomies exist.** [[ai-operating-system/_index]] records a *different* video's framing ("static files → session-local → append-only logs → categorized → auto-categorized → semantic search"). **This** dedicated 41-min video's taxonomy (native → hooks → semantic → verbatim → knowledge-base → cross-tool) is the **authoritative** one. Do not blend. See [[claude-code-memory-systems/overview]].

## Optional next step — adversarial workflow

This topic was **not** put through a multi-agent verification Workflow (unlike [[multi-agent-orchestration/source-provenance]] / [[cowork-third-party-inference/source-provenance]]), because it was built primary-source-first. If you want the same belt-and-suspenders adversarial pass (refute the Kairos rumor, confirm the exact MemSearch hooks, price-check OpenBrain), say so and I'll run it — it needs your explicit go-ahead (it spawns ~20+ agents).

## Key Takeaways

- **Built primary-source-first** — the gist, the repos, and the article were fetched directly; the video supplied the map.
- **Verified:** all the level architectures + the L2 hook mechanics + the Karpathy LLM Wiki internals.
- **Flagged as video-only:** **Kairos** (rumor), **OpenBrain pricing**, **MemPalace "best benchmark ever."**
- **Naming to watch:** **OpenClaw** (not "Open Claude"); MemSearch's exact hook event; AAAK's undocumented grammar.
- **Conflict:** this is the **authoritative** Simon Scrapes 6-level taxonomy vs the looser one in [[ai-operating-system/_index]].
